import base64

import httpx
import pytest

from cursor_sdk import CursorClient


def test_basic_auth_header_value() -> None:
    client = CursorClient("key_abc")
    token = base64.b64encode(b"key_abc:").decode("ascii")
    assert client._auth_header_value() == f"Basic {token}"
    client.close()


def test_bearer_auth_header_value() -> None:
    client = CursorClient("tok", auth="bearer")
    assert client._auth_header_value() == "Bearer tok"
    client.close()


def test_build_headers_merges_default_and_extra() -> None:
    client = CursorClient(
        "k",
        default_headers={"X-Foo": "1", "Authorization": "will-be-overridden"},
    )

    headers = client._build_headers({"X-Bar": "2"})
    assert headers["X-Foo"] == "1"
    assert headers["X-Bar"] == "2"

    # Always set Authorization from api_key/auth.
    assert headers["Authorization"].startswith("Basic ")
    client.close()


def test_api_key_required() -> None:
    with pytest.raises(ValueError, match="api_key is required"):
        CursorClient("")


def test_context_manager_calls_close() -> None:
    closed = {"value": False}

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"ok": True})

    transport = httpx.MockTransport(handler)

    class SpyClient(CursorClient):
        def close(self) -> None:  # type: ignore[override]  # SpyClient.close intentionally overrides parent but type checker flags it
            closed["value"] = True
            super().close()

    with SpyClient("k", base_url="https://example.test", transport=transport) as c:
        assert c.get_teams_members() == {"ok": True}

    assert closed["value"] is True
