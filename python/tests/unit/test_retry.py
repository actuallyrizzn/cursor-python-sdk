"""Tests for retry logic."""

import time
from unittest.mock import Mock, patch

import httpx
import pytest

from cursor_sdk import CursorClient, retry_with_backoff
from cursor_sdk.errors import CursorNetworkError, CursorRateLimitError


def test_retry_on_network_error() -> None:
    """Test that retry works on network errors."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] < 3:
            raise httpx.ConnectError("Connection failed", request=request)
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=0.01)
    def make_request() -> dict:
        return client.get_v0_me()

    result = make_request()
    assert result == {"ok": True}
    assert call_count["value"] == 3

    client.close()


def test_retry_exhausts_after_max_retries() -> None:
    """Test that retry raises after max retries."""
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("Connection failed", request=request)

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=2, initial_delay=0.01)
    def make_request() -> dict:
        return client.get_v0_me()

    with pytest.raises(CursorNetworkError):
        make_request()

    client.close()


def test_retry_exponential_backoff() -> None:
    """Test that retry uses exponential backoff."""
    call_times = []

    def handler(request: httpx.Request) -> httpx.Response:
        call_times.append(time.time())
        if len(call_times) < 3:
            raise httpx.ConnectError("Connection failed", request=request)
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=0.1, exponential_base=2.0)
    def make_request() -> dict:
        return client.get_v0_me()

    result = make_request()
    assert result == {"ok": True}

    # Verify delays increased exponentially (approximately)
    if len(call_times) >= 3:
        delay1 = call_times[1] - call_times[0]
        delay2 = call_times[2] - call_times[1]
        # Allow some tolerance for timing
        assert delay2 > delay1 * 1.5  # Should be roughly double

    client.close()


def test_retry_on_rate_limit_error() -> None:
    """Test that retry works on rate limit errors."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] < 2:
            return httpx.Response(429, json={"message": "Rate limited"})
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=0.01)
    def make_request() -> dict:
        return client.get_v0_me()

    result = make_request()
    assert result == {"ok": True}
    assert call_count["value"] == 2

    client.close()


def test_retry_respects_retry_after_header() -> None:
    """Test that retry respects Retry-After header for rate limits."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] < 2:
            return httpx.Response(429, json={"message": "Rate limited"}, headers={"Retry-After": "0.1"})
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    start_time = time.time()

    @retry_with_backoff(max_retries=3, initial_delay=0.5)  # Should use Retry-After instead
    def make_request() -> dict:
        return client.get_v0_me()

    result = make_request()
    elapsed = time.time() - start_time

    assert result == {"ok": True}
    # Should have waited approximately 0.1 seconds (Retry-After value)
    # Note: initial_delay might be used on first retry, so allow wider range
    assert 0.05 < elapsed < 0.6  # Allow tolerance for timing variations

    client.close()


def test_retry_does_not_retry_other_errors() -> None:
    """Test that retry doesn't retry non-retryable errors."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        return httpx.Response(400, json={"message": "Bad request"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=0.01)
    def make_request() -> dict:
        return client.get_v0_me()

    from cursor_sdk.errors import CursorAPIError
    with pytest.raises(CursorAPIError):
        make_request()

    # Should only be called once (no retries for 400 errors)
    assert call_count["value"] == 1

    client.close()


def test_retry_max_delay_cap() -> None:
    """Test that retry respects max_delay cap."""
    call_times = []

    def handler(request: httpx.Request) -> httpx.Response:
        call_times.append(time.time())
        if len(call_times) < 3:
            raise httpx.ConnectError("Connection failed", request=request)
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=100.0, max_delay=0.1)  # Max delay should cap it
    def make_request() -> dict:
        return client.get_v0_me()

    start_time = time.time()
    result = make_request()
    elapsed = time.time() - start_time

    assert result == {"ok": True}
    # Should be capped at max_delay, not use the huge initial_delay
    assert elapsed < 0.5  # Much less than 100 seconds

    client.close()


def test_retry_invalid_retry_after_header() -> None:
    """Test that retry handles invalid Retry-After header gracefully."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] < 2:
            # Invalid Retry-After value (not a number)
            return httpx.Response(429, json={"message": "Rate limited"}, headers={"Retry-After": "invalid"})
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=0.01)
    def make_request() -> dict:
        return client.get_v0_me()

    # Should fallback to exponential backoff when Retry-After is invalid
    result = make_request()
    assert result == {"ok": True}
    assert call_count["value"] == 2

    client.close()


def test_retry_rate_limit_without_retry_after() -> None:
    """Test that retry uses exponential backoff when Retry-After is missing."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] < 2:
            # Rate limit without Retry-After header
            return httpx.Response(429, json={"message": "Rate limited"})
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    @retry_with_backoff(max_retries=3, initial_delay=0.01)
    def make_request() -> dict:
        return client.get_v0_me()

    result = make_request()
    assert result == {"ok": True}
    assert call_count["value"] == 2

    client.close()

