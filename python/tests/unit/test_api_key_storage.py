"""Tests for API key storage security."""

import httpx
import pytest

from cursor_sdk import CursorClient


def test_repr_does_not_expose_api_key() -> None:
    """Test that __repr__ does not expose the API key."""
    api_key = "secret_key_12345"
    client = CursorClient(api_key, base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(200)))

    repr_str = repr(client)
    assert api_key not in repr_str
    assert "secret" not in repr_str.lower()
    assert "CursorClient" in repr_str

    client.close()


def test_str_does_not_expose_api_key() -> None:
    """Test that __str__ does not expose the API key."""
    api_key = "secret_key_12345"
    client = CursorClient(api_key, base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(200)))

    str_repr = str(client)
    assert api_key not in str_repr
    assert "secret" not in str_repr.lower()
    assert "CursorClient" in str_repr

    client.close()


def test_error_messages_do_not_expose_api_key() -> None:
    """Test that error messages do not expose the API key."""
    api_key = "secret_key_12345"
    client = CursorClient(api_key, base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(500, json={"error": "Internal error"})))

    from cursor_sdk.errors import CursorAPIError
    with pytest.raises(CursorAPIError) as exc_info:
        client.get_v0_me()

    error_str = str(exc_info.value)
    assert api_key not in error_str
    assert "secret" not in error_str.lower()

    client.close()

