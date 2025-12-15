"""Synchronous HTTP client for Cursor's public APIs.

This module provides the CursorClient class which implements a synchronous
interface to all documented Cursor API endpoints. Each endpoint is exposed
as a method on the client instance.
"""

from __future__ import annotations

import base64
from typing import Any, Literal, Mapping, MutableMapping, Optional
from types import TracebackType

import httpx

from cursor_sdk.errors import (
    CursorAPIError,
    CursorAuthError,
    CursorNetworkError,
    CursorRateLimitError,
)

AuthType = Literal["basic", "bearer"]


# Tuple of (HTTP method, path template, method name) for all API endpoints.
# Path templates use :paramName or {paramName} format for path parameters.
# Method names are derived from HTTP method + path (e.g., GET /teams/members -> get_teams_members).
ENDPOINT_SPECS: tuple[tuple[str, str, str], ...] = (
    ("DELETE", "/settings/repo-blocklists/repos/:repoId", "delete_settings_repo_blocklists_repos_repo_id"),
    ("DELETE", "/teams/groups/:groupId", "delete_teams_groups_group_id"),
    ("DELETE", "/teams/groups/:groupId/members", "delete_teams_groups_group_id_members"),
    ("DELETE", "/v0/agents/{id}", "delete_v0_agents_id"),
    ("GET", "/analytics/ai-code/changes", "get_analytics_ai_code_changes"),
    ("GET", "/analytics/ai-code/changes.csv", "get_analytics_ai_code_changes_csv"),
    ("GET", "/analytics/ai-code/commits", "get_analytics_ai_code_commits"),
    ("GET", "/analytics/ai-code/commits.csv", "get_analytics_ai_code_commits_csv"),
    ("GET", "/analytics/by-user/agent-edits", "get_analytics_by_user_agent_edits"),
    ("GET", "/analytics/by-user/ask-mode", "get_analytics_by_user_ask_mode"),
    ("GET", "/analytics/by-user/client-versions", "get_analytics_by_user_client_versions"),
    ("GET", "/analytics/by-user/commands", "get_analytics_by_user_commands"),
    ("GET", "/analytics/by-user/mcp", "get_analytics_by_user_mcp"),
    ("GET", "/analytics/by-user/models", "get_analytics_by_user_models"),
    ("GET", "/analytics/by-user/plans", "get_analytics_by_user_plans"),
    ("GET", "/analytics/by-user/tabs", "get_analytics_by_user_tabs"),
    ("GET", "/analytics/by-user/top-file-extensions", "get_analytics_by_user_top_file_extensions"),
    ("GET", "/analytics/team/agent-edits", "get_analytics_team_agent_edits"),
    ("GET", "/analytics/team/ask-mode", "get_analytics_team_ask_mode"),
    ("GET", "/analytics/team/client-versions", "get_analytics_team_client_versions"),
    ("GET", "/analytics/team/commands", "get_analytics_team_commands"),
    ("GET", "/analytics/team/dau", "get_analytics_team_dau"),
    ("GET", "/analytics/team/leaderboard", "get_analytics_team_leaderboard"),
    ("GET", "/analytics/team/mcp", "get_analytics_team_mcp"),
    ("GET", "/analytics/team/models", "get_analytics_team_models"),
    ("GET", "/analytics/team/plans", "get_analytics_team_plans"),
    ("GET", "/analytics/team/tabs", "get_analytics_team_tabs"),
    ("GET", "/analytics/team/top-file-extensions", "get_analytics_team_top_file_extensions"),
    ("GET", "/settings/repo-blocklists/repos", "get_settings_repo_blocklists_repos"),
    ("GET", "/teams/audit-logs", "get_teams_audit_logs"),
    ("GET", "/teams/groups", "get_teams_groups"),
    ("GET", "/teams/groups/:groupId", "get_teams_groups_group_id"),
    ("GET", "/teams/members", "get_teams_members"),
    ("GET", "/v0/agents", "get_v0_agents"),
    ("GET", "/v0/agents/{id}", "get_v0_agents_id"),
    ("GET", "/v0/agents/{id}/conversation", "get_v0_agents_id_conversation"),
    ("GET", "/v0/me", "get_v0_me"),
    ("GET", "/v0/models", "get_v0_models"),
    ("GET", "/v0/repositories", "get_v0_repositories"),
    ("PATCH", "/teams/groups/:groupId", "patch_teams_groups_group_id"),
    ("POST", "/bugbot/repo/update", "post_bugbot_repo_update"),
    ("POST", "/settings/repo-blocklists/repos/upsert", "post_settings_repo_blocklists_repos_upsert"),
    ("POST", "/teams/daily-usage-data", "post_teams_daily_usage_data"),
    ("POST", "/teams/filtered-usage-events", "post_teams_filtered_usage_events"),
    ("POST", "/teams/groups", "post_teams_groups"),
    ("POST", "/teams/groups/:groupId/members", "post_teams_groups_group_id_members"),
    ("POST", "/teams/spend", "post_teams_spend"),
    ("POST", "/teams/user-spend-limit", "post_teams_user_spend_limit"),
    ("POST", "/v0/agents", "post_v0_agents"),
    ("POST", "/v0/agents/{id}/followup", "post_v0_agents_id_followup"),
    ("POST", "/v0/agents/{id}/stop", "post_v0_agents_id_stop"),
)

__all__ = ["CursorClient", "AuthType", "ENDPOINT_SPECS"]


class CursorClient:
    """Synchronous client for the public Cursor APIs."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.cursor.com",
        auth: AuthType = "basic",
        timeout: float = 30.0,
        transport: Optional[httpx.BaseTransport] = None,
        default_headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")

        self._api_key = api_key
        self._auth = auth
        self._default_headers = dict(default_headers or {})
        self._client = httpx.Client(base_url=base_url, timeout=timeout, transport=transport)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "CursorClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def _auth_header_value(self) -> str:
        """Generate the Authorization header value.

        Note: Basic authentication uses base64 encoding, which is NOT encryption.
        The credentials are easily decodable. Always use HTTPS to protect credentials
        in transit. The httpx client enforces HTTPS by default.
        """
        if self._auth == "bearer":
            return f"Bearer {self._api_key}"

        token = base64.b64encode(f"{self._api_key}:".encode("utf-8")).decode("ascii")
        return f"Basic {token}"

    def _build_headers(self, extra: Optional[Mapping[str, str]] = None) -> MutableMapping[str, str]:
        # Default headers should never override authentication.
        headers: MutableMapping[str, str] = dict(self._default_headers)
        headers["Authorization"] = self._auth_header_value()
        if extra is not None:
            headers.update(extra)
        return headers

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        json: Any = None,
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any:
        try:
            resp = self._client.request(
                method,
                path,
                params=params,
                json=json,
                headers=self._build_headers(headers),
                timeout=timeout,
            )
        except httpx.HTTPError as e:
            raise CursorNetworkError("Request failed due to a network error.", cause=e) from e

        if resp.status_code == 304:
            return None

        if 200 <= resp.status_code < 300:
            if not resp.content:
                return None

            content_type = resp.headers.get("content-type", "")
            if "text/csv" in content_type or path.endswith(".csv"):
                return resp.text

            if "application/json" in content_type or content_type.endswith("+json"):
                return resp.json()

            # Fallback: try to parse as JSON, otherwise return as text
            try:
                return resp.json()
            except ValueError:
                return resp.text

        body: Any = None
        message = resp.reason_phrase or "Request failed."
        try:
            body = resp.json()
            if isinstance(body, dict):
                message = str(body.get("message") or body.get("error") or message)
        except ValueError:
            body = resp.text if resp.text else None
            if body:
                message = str(body)

        exc_cls = CursorAPIError
        if resp.status_code in (401, 403):
            exc_cls = CursorAuthError
        elif resp.status_code == 429:
            exc_cls = CursorRateLimitError

        raise exc_cls(resp.status_code, message, body=body, headers=dict(resp.headers))

    def delete_settings_repo_blocklists_repos_repo_id(self, repo_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """DELETE /settings/repo-blocklists/repos/:repoId"""
        return self._request('DELETE', f'/settings/repo-blocklists/repos/{repo_id}', params=params, headers=headers, timeout=timeout)

    def delete_teams_groups_group_id(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """DELETE /teams/groups/:groupId"""
        return self._request('DELETE', f'/teams/groups/{group_id}', params=params, headers=headers, timeout=timeout)

    def delete_teams_groups_group_id_members(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """DELETE /teams/groups/:groupId/members"""
        return self._request('DELETE', f'/teams/groups/{group_id}/members', params=params, headers=headers, timeout=timeout)

    def delete_v0_agents_id(self, id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """DELETE /v0/agents/{id}"""
        return self._request('DELETE', f'/v0/agents/{id}', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_changes(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/ai-code/changes"""
        return self._request('GET', '/analytics/ai-code/changes', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_changes_csv(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/ai-code/changes.csv"""
        return self._request('GET', '/analytics/ai-code/changes.csv', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_commits(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/ai-code/commits"""
        return self._request('GET', '/analytics/ai-code/commits', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_commits_csv(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/ai-code/commits.csv"""
        return self._request('GET', '/analytics/ai-code/commits.csv', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_agent_edits(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/agent-edits"""
        return self._request('GET', '/analytics/by-user/agent-edits', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_ask_mode(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/ask-mode"""
        return self._request('GET', '/analytics/by-user/ask-mode', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_client_versions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/client-versions"""
        return self._request('GET', '/analytics/by-user/client-versions', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_commands(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/commands"""
        return self._request('GET', '/analytics/by-user/commands', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_mcp(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/mcp"""
        return self._request('GET', '/analytics/by-user/mcp', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_models(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/models"""
        return self._request('GET', '/analytics/by-user/models', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_plans(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/plans"""
        return self._request('GET', '/analytics/by-user/plans', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_tabs(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/tabs"""
        return self._request('GET', '/analytics/by-user/tabs', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_top_file_extensions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/by-user/top-file-extensions"""
        return self._request('GET', '/analytics/by-user/top-file-extensions', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_agent_edits(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/agent-edits"""
        return self._request('GET', '/analytics/team/agent-edits', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_ask_mode(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/ask-mode"""
        return self._request('GET', '/analytics/team/ask-mode', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_client_versions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/client-versions"""
        return self._request('GET', '/analytics/team/client-versions', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_commands(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/commands"""
        return self._request('GET', '/analytics/team/commands', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_dau(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/dau"""
        return self._request('GET', '/analytics/team/dau', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_leaderboard(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/leaderboard"""
        return self._request('GET', '/analytics/team/leaderboard', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_mcp(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/mcp"""
        return self._request('GET', '/analytics/team/mcp', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_models(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/models"""
        return self._request('GET', '/analytics/team/models', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_plans(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/plans"""
        return self._request('GET', '/analytics/team/plans', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_tabs(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/tabs"""
        return self._request('GET', '/analytics/team/tabs', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_top_file_extensions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /analytics/team/top-file-extensions"""
        return self._request('GET', '/analytics/team/top-file-extensions', params=params, headers=headers, timeout=timeout)

    def get_settings_repo_blocklists_repos(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /settings/repo-blocklists/repos"""
        return self._request('GET', '/settings/repo-blocklists/repos', params=params, headers=headers, timeout=timeout)

    def get_teams_audit_logs(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /teams/audit-logs"""
        return self._request('GET', '/teams/audit-logs', params=params, headers=headers, timeout=timeout)

    def get_teams_groups(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /teams/groups"""
        return self._request('GET', '/teams/groups', params=params, headers=headers, timeout=timeout)

    def get_teams_groups_group_id(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /teams/groups/:groupId"""
        return self._request('GET', f'/teams/groups/{group_id}', params=params, headers=headers, timeout=timeout)

    def get_teams_members(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /teams/members"""
        return self._request('GET', '/teams/members', params=params, headers=headers, timeout=timeout)

    def get_v0_agents(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /v0/agents"""
        return self._request('GET', '/v0/agents', params=params, headers=headers, timeout=timeout)

    def get_v0_agents_id(self, id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /v0/agents/{id}"""
        return self._request('GET', f'/v0/agents/{id}', params=params, headers=headers, timeout=timeout)

    def get_v0_agents_id_conversation(self, id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /v0/agents/{id}/conversation"""
        return self._request('GET', f'/v0/agents/{id}/conversation', params=params, headers=headers, timeout=timeout)

    def get_v0_me(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /v0/me"""
        return self._request('GET', '/v0/me', params=params, headers=headers, timeout=timeout)

    def get_v0_models(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /v0/models"""
        return self._request('GET', '/v0/models', params=params, headers=headers, timeout=timeout)

    def get_v0_repositories(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """GET /v0/repositories"""
        return self._request('GET', '/v0/repositories', params=params, headers=headers, timeout=timeout)

    def patch_teams_groups_group_id(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """PATCH /teams/groups/:groupId"""
        return self._request('PATCH', f'/teams/groups/{group_id}', params=params, json=json, headers=headers, timeout=timeout)

    def post_bugbot_repo_update(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /bugbot/repo/update"""
        return self._request('POST', '/bugbot/repo/update', params=params, json=json, headers=headers, timeout=timeout)

    def post_settings_repo_blocklists_repos_upsert(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /settings/repo-blocklists/repos/upsert"""
        return self._request('POST', '/settings/repo-blocklists/repos/upsert', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_daily_usage_data(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /teams/daily-usage-data"""
        return self._request('POST', '/teams/daily-usage-data', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_filtered_usage_events(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /teams/filtered-usage-events"""
        return self._request('POST', '/teams/filtered-usage-events', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_groups(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /teams/groups"""
        return self._request('POST', '/teams/groups', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_groups_group_id_members(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /teams/groups/:groupId/members"""
        return self._request('POST', f'/teams/groups/{group_id}/members', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_spend(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /teams/spend"""
        return self._request('POST', '/teams/spend', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_user_spend_limit(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /teams/user-spend-limit"""
        return self._request('POST', '/teams/user-spend-limit', params=params, json=json, headers=headers, timeout=timeout)

    def post_v0_agents(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /v0/agents"""
        return self._request('POST', '/v0/agents', params=params, json=json, headers=headers, timeout=timeout)

    def post_v0_agents_id_followup(self, id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /v0/agents/{id}/followup"""
        return self._request('POST', f'/v0/agents/{id}/followup', params=params, json=json, headers=headers, timeout=timeout)

    def post_v0_agents_id_stop(self, id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Any:
        """POST /v0/agents/{id}/stop"""
        return self._request('POST', f'/v0/agents/{id}/stop', params=params, json=json, headers=headers, timeout=timeout)
