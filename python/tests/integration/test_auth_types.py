"""Integration tests for all authentication types."""

import base64

import httpx
import pytest

from cursor_sdk import CursorClient


def test_basic_auth_integration() -> None:
    """Test Basic auth works end-to-end."""
    api_key = "test_basic_key"

    def handler(request: httpx.Request) -> httpx.Response:
        auth_header = request.headers.get("Authorization", "")
        expected = "Basic " + base64.b64encode(f"{api_key}:".encode("utf-8")).decode("ascii")
        if auth_header != expected:
            return httpx.Response(401, json={"message": "Unauthorized"})
        return httpx.Response(200, json={"authenticated": True, "auth_type": "basic"})

    client = CursorClient(api_key, auth="basic", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_me()
    assert result == {"authenticated": True, "auth_type": "basic"}
    client.close()


def test_bearer_auth_integration() -> None:
    """Test Bearer auth works end-to-end."""
    api_key = "test_bearer_token"

    def handler(request: httpx.Request) -> httpx.Response:
        auth_header = request.headers.get("Authorization", "")
        expected = f"Bearer {api_key}"
        if auth_header != expected:
            return httpx.Response(401, json={"message": "Unauthorized"})
        return httpx.Response(200, json={"authenticated": True, "auth_type": "bearer"})

    client = CursorClient(api_key, auth="bearer", base_url="https://example.test", transport=httpx.MockTransport(handler))
    result = client.get_v0_me()
    assert result == {"authenticated": True, "auth_type": "bearer"}
    client.close()


def test_both_auth_types_work() -> None:
    """Test that both Basic and Bearer auth work correctly."""
    # Test Basic
    basic_key = "basic_key_123"
    def basic_handler(request: httpx.Request) -> httpx.Response:
        auth = request.headers.get("Authorization", "")
        expected = "Basic " + base64.b64encode(f"{basic_key}:".encode("utf-8")).decode("ascii")
        if auth == expected:
            return httpx.Response(200, json={"auth": "basic"})
        return httpx.Response(401)

    basic_client = CursorClient(basic_key, auth="basic", base_url="https://example.test", transport=httpx.MockTransport(basic_handler))
    assert basic_client.get_v0_me() == {"auth": "basic"}
    basic_client.close()

    # Test Bearer
    bearer_key = "bearer_token_456"
    def bearer_handler(request: httpx.Request) -> httpx.Response:
        auth = request.headers.get("Authorization", "")
        if auth == f"Bearer {bearer_key}":
            return httpx.Response(200, json={"auth": "bearer"})
        return httpx.Response(401)

    bearer_client = CursorClient(bearer_key, auth="bearer", base_url="https://example.test", transport=httpx.MockTransport(bearer_handler))
    assert bearer_client.get_v0_me() == {"auth": "bearer"}
    bearer_client.close()


