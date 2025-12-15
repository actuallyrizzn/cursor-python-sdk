"""Tests for error response parsing."""

import httpx
import pytest

from cursor_sdk import CursorClient
from cursor_sdk.errors import CursorAPIError, CursorAuthError


def test_error_with_message_field() -> None:
    """Test error response with 'message' field."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"message": "Bad request message"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 400
    assert exc.value.message == "Bad request message"
    client.close()


def test_error_with_error_field() -> None:
    """Test error response with 'error' field."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"error": "Error field message"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 400
    assert exc.value.message == "Error field message"
    client.close()


def test_error_with_both_message_and_error_fields() -> None:
    """Test error response with both 'message' and 'error' fields - message takes priority."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"message": "Message takes priority", "error": "This is ignored"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 400
    assert exc.value.message == "Message takes priority"
    client.close()


def test_error_with_nested_error_object() -> None:
    """Test error response with nested error object."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json={"error": {"code": "ERR001", "message": "Nested error"}})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    # The nested error object should be converted to string representation
    assert exc.value.status_code == 400
    # The error field should be converted to string
    assert "Nested error" in exc.value.message or str({"code": "ERR001", "message": "Nested error"}) in exc.value.message
    client.close()


def test_error_with_non_dict_json_body() -> None:
    """Test error response with non-dict JSON body (e.g., array or string)."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json=["error", "list"])

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 400
    # Should fallback to reason phrase or default message
    assert exc.value.body == ["error", "list"]
    client.close()


def test_error_with_text_body() -> None:
    """Test error response with plain text body."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, content=b"Plain text error message", headers={"content-type": "text/plain"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 400
    assert "Plain text error message" in exc.value.message
    client.close()


def test_error_with_empty_body() -> None:
    """Test error response with empty body."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, content=b"")

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 400
    # Should use reason phrase or default message
    assert exc.value.message
    client.close()


def test_auth_error_message_extraction() -> None:
    """Test that auth errors properly extract message from JSON."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"message": "Invalid credentials"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAuthError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 401
    assert exc.value.message == "Invalid credentials"
    client.close()


