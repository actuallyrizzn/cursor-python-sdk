import json
from pathlib import Path

import httpx
import pytest

from cursor_sdk.client import ENDPOINT_SPECS, CursorClient


def _docs_endpoints() -> set[tuple[str, str]]:
    repo_root = Path(__file__).resolve().parents[3]
    j = json.loads((repo_root / "docs" / "api-endpoints.json").read_text())
    return {(e["method"], e["path"]) for p in j["pages"] for e in p.get("endpoints", [])}


def test_sdk_covers_all_documented_endpoints() -> None:
    sdk = {(m, p) for (m, p, _name) in ENDPOINT_SPECS}
    assert sdk == _docs_endpoints()


@pytest.mark.parametrize("method,path,fn_name", list(ENDPOINT_SPECS))
def test_each_endpoint_method_emits_correct_request(method: str, path: str, fn_name: str) -> None:
    expected_path = path.replace(":repoId", "repo").replace(":groupId", "group")
    expected_path = expected_path.replace("{id}", "id")

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == method
        assert request.url.path == expected_path
        if path.endswith(".csv"):
            return httpx.Response(
                200,
                content=b"a,b\n1,2\n",
                headers={"content-type": "text/csv"},
            )

        return httpx.Response(200, json={"ok": True}, headers={"content-type": "application/json"})

    client = CursorClient("k", base_url="https://example.test", transport=httpx.MockTransport(handler))

    fn = getattr(client, fn_name)

    kwargs = {}
    if ":repoId" in path:
        kwargs["repo_id"] = "repo"
    if ":groupId" in path:
        kwargs["group_id"] = "group"
    if "{id}" in path:
        kwargs["id"] = "id"

    if method in ("POST", "PATCH"):
        result = fn(**kwargs, json={"ok": 1})
    else:
        result = fn(**kwargs)

    if path.endswith(".csv"):
        assert isinstance(result, str)
        assert result.startswith("a,b")
    else:
        assert result == {"ok": True}
    client.close()
