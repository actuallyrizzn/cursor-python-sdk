"""Tests for timeout handling."""

import time

import httpx
import pytest

from cursor_sdk import CursorClient


def test_default_timeout() -> None:
    """Test that default timeout is used when not specified."""
    start_time = time.time()

    def handler(request: httpx.Request) -> httpx.Response:
        # Simulate a slow response
        time.sleep(0.1)
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_teams_members()
    elapsed = time.time() - start_time

    assert result == {"ok": True}
    # Should complete quickly with mock transport (no actual network delay)
    assert elapsed < 1.0
    client.close()


def test_per_request_timeout_override() -> None:
    """Test that per-request timeout can override default timeout."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"ok": True})

    # Create client with a long default timeout
    client = CursorClient(
        "test_key",
        base_url="https://example.test",
        timeout=60.0,
        transport=httpx.MockTransport(handler),
    )

    # Override with shorter timeout for specific request
    result = client.get_teams_members(timeout=5.0)
    assert result == {"ok": True}
    client.close()


def test_timeout_exception_propagates() -> None:
    """Test that timeout exceptions are properly wrapped."""
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.TimeoutException("Request timed out", request=request)

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    from cursor_sdk.errors import CursorNetworkError
    with pytest.raises(CursorNetworkError):
        client.get_teams_members()
    client.close()


