import json

import httpx
import pytest

from cursor_sdk import CursorClient
from cursor_sdk.errors import CursorAPIError, CursorAuthError, CursorNetworkError, CursorRateLimitError


def test_request_parses_json_response() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "GET"
        assert request.url.path == "/teams/members"
        return httpx.Response(200, json={"teamMembers": []})

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.get_teams_members() == {"teamMembers": []}
    client.close()


def test_request_parses_csv_response_by_content_type() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            content=b"a,b\n1,2\n",
            headers={"content-type": "text/csv"},
        )

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.get_analytics_ai_code_commits_csv().startswith("a,b")
    client.close()


def test_request_parses_csv_response_by_path_suffix() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        # No content-type, but .csv path should still be treated as csv.
        return httpx.Response(200, content=b"x\n")

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.get_analytics_ai_code_changes_csv() == "x\n"
    client.close()


def test_request_returns_none_for_empty_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(204)

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.post_bugbot_repo_update(json={"repo": "x"}) is None
    client.close()


def test_request_returns_none_for_304_not_modified() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(304)

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.get_analytics_team_dau() is None
    client.close()


def test_request_falls_back_to_text_when_not_json() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"plain text", headers={"content-type": "text/plain"})

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.get_v0_models() == "plain text"
    client.close()


def test_request_raises_auth_error_from_json_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"message": "nope"})

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAuthError) as exc:
        client.get_v0_me()
    assert exc.value.status_code == 401
    assert exc.value.message == "nope"
    client.close()


def test_request_raises_rate_limit_error_from_text_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(429, content=b"Too Many Requests")

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorRateLimitError) as exc:
        client.get_settings_repo_blocklists_repos()
    assert exc.value.status_code == 429
    assert "Too Many Requests" in exc.value.message
    client.close()


def test_request_raises_generic_api_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, json={"error": "boom"})

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorAPIError) as exc:
        client.get_teams_groups()
    assert exc.value.status_code == 500
    assert exc.value.message == "boom"
    client.close()


def test_request_raises_network_error_on_transport_failure() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("fail", request=request)

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    with pytest.raises(CursorNetworkError):
        client.get_teams_members()
    client.close()


def test_post_sends_json_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        payload = json.loads(request.content.decode("utf-8"))
        assert payload == {"x": 1}
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))
    assert client.post_teams_spend(json={"x": 1}) == {"ok": True}
    client.close()
