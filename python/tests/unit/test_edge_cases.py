"""Tests for edge cases and coverage gaps."""

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

import httpx
import pytest

from cursor_sdk import CursorClient
from cursor_sdk.errors import CursorRateLimitError


def test_large_response_handling() -> None:
    """Test handling of large JSON responses."""
    # Create a large response (simulate large dataset)
    large_data = {"items": [{"id": i, "data": "x" * 100} for i in range(1000)]}
    large_json = json.dumps(large_data)

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=large_json.encode("utf-8"), headers={"content-type": "application/json"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_agents()

    assert isinstance(result, dict)
    assert len(result["items"]) == 1000
    client.close()


def test_concurrent_requests() -> None:
    """Test that client can handle concurrent requests (thread safety)."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    results = []
    errors = []

    def make_request() -> None:
        try:
            result = client.get_v0_me()
            results.append(result)
        except Exception as e:
            errors.append(e)

    # Create multiple threads making concurrent requests
    threads = [threading.Thread(target=make_request) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # All requests should succeed
    assert len(results) == 10
    assert len(errors) == 0
    assert all(r == {"ok": True} for r in results)

    client.close()


def test_rate_limit_error_with_retry_after() -> None:
    """Test rate limit error handling with Retry-After header."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] == 1:
            return httpx.Response(429, json={"message": "Rate limited"}, headers={"Retry-After": "1"})
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    # First call should raise rate limit error
    with pytest.raises(CursorRateLimitError) as exc_info:
        client.get_v0_me()

    assert exc_info.value.status_code == 429
    assert exc_info.value.headers is not None
    # Headers are case-insensitive, check both cases
    assert "Retry-After" in exc_info.value.headers or "retry-after" in exc_info.value.headers

    client.close()


def test_network_error_retry_scenario() -> None:
    """Test network error scenarios that might need retry."""
    call_count = {"value": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        call_count["value"] += 1
        if call_count["value"] == 1:
            raise httpx.TimeoutException("Request timed out", request=request)
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    from cursor_sdk.errors import CursorNetworkError
    # First call should raise network error
    with pytest.raises(CursorNetworkError):
        client.get_v0_me()

    # Second call should succeed
    result = client.get_v0_me()
    assert result == {"ok": True}

    client.close()


def test_empty_response_handling() -> None:
    """Test handling of various empty response scenarios."""
    test_cases = [
        (204, None),  # No Content
        (200, b""),   # Empty body
        (200, None), # None body
    ]

    for status_code, content in test_cases:
        def handler(request: httpx.Request) -> httpx.Response:
            if content is None:
                return httpx.Response(status_code)
            return httpx.Response(status_code, content=content)

        client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
        result = client.get_v0_me()
        assert result is None
        client.close()


def test_malformed_json_response() -> None:
    """Test handling of malformed JSON responses."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"{invalid json", headers={"content-type": "application/json"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    # Should fallback to text
    result = client.get_v0_me()
    assert isinstance(result, str)
    assert "invalid json" in result
    client.close()


def test_very_long_path_parameter() -> None:
    """Test handling of very long path parameters."""
    long_id = "a" * 1000  # Very long ID

    def handler(request: httpx.Request) -> httpx.Response:
        # Verify the long ID is properly URL encoded
        assert long_id in request.url.path or "%61" in request.url.path
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_agents_id(long_id)
    assert result == {"ok": True}
    client.close()

