"""Tests for content-type edge cases."""

import httpx
import pytest

from cursor_sdk import CursorClient


def test_missing_content_type_header() -> None:
    """Test handling of responses with missing content-type header."""
    def handler(request: httpx.Request) -> httpx.Response:
        # No content-type header, but JSON content
        return httpx.Response(200, content=b'{"key": "value"}', headers={})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_models()
    # Should fallback to JSON parsing
    assert result == {"key": "value"}
    client.close()


def test_malformed_content_type() -> None:
    """Test handling of malformed content-type header."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b'{"key": "value"}', headers={"content-type": "invalid/type"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_models()
    # Should fallback to JSON parsing
    assert result == {"key": "value"}
    client.close()


def test_content_type_with_charset() -> None:
    """Test handling of content-type with charset parameter."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            content=b'{"key": "value"}',
            headers={"content-type": "application/json; charset=utf-8"},
        )

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_models()
    assert result == {"key": "value"}
    client.close()


def test_json_content_type_variants() -> None:
    """Test handling of various JSON content-type variants."""
    test_cases = [
        "application/json",
        "application/json; charset=utf-8",
        "application/vnd.api+json",
        "application/hal+json",
    ]

    for content_type in test_cases:
        def handler(request: httpx.Request) -> httpx.Response:
            return httpx.Response(200, content=b'{"key": "value"}', headers={"content-type": content_type})

        client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
        result = client.get_v0_models()
        assert result == {"key": "value"}
        client.close()


def test_non_json_content_fallback() -> None:
    """Test fallback to text when content is not JSON."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"plain text response", headers={"content-type": "text/plain"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_models()
    assert result == "plain text response"
    client.close()


def test_invalid_json_fallback_to_text() -> None:
    """Test that invalid JSON falls back to text."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"not valid json {", headers={"content-type": "application/json"})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_models()
    assert result == "not valid json {"
    client.close()


