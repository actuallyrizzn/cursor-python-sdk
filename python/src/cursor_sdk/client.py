"""Synchronous HTTP client for Cursor's public APIs.

This module provides the CursorClient class which implements a synchronous
interface to all documented Cursor API endpoints. Each endpoint is exposed
as a method on the client instance.
"""

from __future__ import annotations

import base64
import re
from typing import Any, Literal, Mapping, MutableMapping, NamedTuple, Optional, Union
from types import TracebackType
from urllib.parse import urlparse

import httpx

from cursor_sdk.errors import (
    CursorAPIError,
    CursorAuthError,
    CursorNetworkError,
    CursorRateLimitError,
)

AuthType = Literal["basic", "bearer"]

# HTTP status code constants
HTTP_STATUS_NOT_MODIFIED = 304
HTTP_STATUS_UNAUTHORIZED = 401
HTTP_STATUS_FORBIDDEN = 403
HTTP_STATUS_TOO_MANY_REQUESTS = 429

# Default timeout in seconds
DEFAULT_TIMEOUT = 30.0

# Test timeout in seconds (for e2e tests)
TEST_SERVER_SHUTDOWN_TIMEOUT = 2.0


class EndpointSpec(NamedTuple):
    """Specification for an API endpoint.

    Attributes:
        method: HTTP method (e.g., "GET", "POST")
        path: Path template with :paramName or {paramName} format
        method_name: Python method name derived from HTTP method + path
    """

    method: str
    path: str
    method_name: str


# Tuple of endpoint specifications for all API endpoints.
# Path templates use two formats for path parameters:
# - :paramName format (e.g., :repoId, :groupId) - used in some endpoints
# - {paramName} format (e.g., {id}) - used in v0 endpoints
# Both formats are handled by the SDK, but the inconsistency reflects the API's design.
# Method names are derived from HTTP method + path (e.g., GET /teams/members -> get_teams_members).
ENDPOINT_SPECS: tuple[EndpointSpec, ...] = (
    EndpointSpec('DELETE', '/settings/repo-blocklists/repos/:repoId', 'delete_settings_repo_blocklists_repos_repo_id'),
    EndpointSpec('DELETE', '/teams/groups/:groupId', 'delete_teams_groups_group_id'),
    EndpointSpec('DELETE', '/teams/groups/:groupId/members', 'delete_teams_groups_group_id_members'),
    EndpointSpec('DELETE', '/v0/agents/{id}', 'delete_v0_agents_id'),
    EndpointSpec('GET', '/analytics/ai-code/changes', 'get_analytics_ai_code_changes'),
    EndpointSpec('GET', '/analytics/ai-code/changes.csv', 'get_analytics_ai_code_changes_csv'),
    EndpointSpec('GET', '/analytics/ai-code/commits', 'get_analytics_ai_code_commits'),
    EndpointSpec('GET', '/analytics/ai-code/commits.csv', 'get_analytics_ai_code_commits_csv'),
    EndpointSpec('GET', '/analytics/by-user/agent-edits', 'get_analytics_by_user_agent_edits'),
    EndpointSpec('GET', '/analytics/by-user/ask-mode', 'get_analytics_by_user_ask_mode'),
    EndpointSpec('GET', '/analytics/by-user/client-versions', 'get_analytics_by_user_client_versions'),
    EndpointSpec('GET', '/analytics/by-user/commands', 'get_analytics_by_user_commands'),
    EndpointSpec('GET', '/analytics/by-user/mcp', 'get_analytics_by_user_mcp'),
    EndpointSpec('GET', '/analytics/by-user/models', 'get_analytics_by_user_models'),
    EndpointSpec('GET', '/analytics/by-user/plans', 'get_analytics_by_user_plans'),
    EndpointSpec('GET', '/analytics/by-user/tabs', 'get_analytics_by_user_tabs'),
    EndpointSpec('GET', '/analytics/by-user/top-file-extensions', 'get_analytics_by_user_top_file_extensions'),
    EndpointSpec('GET', '/analytics/team/agent-edits', 'get_analytics_team_agent_edits'),
    EndpointSpec('GET', '/analytics/team/ask-mode', 'get_analytics_team_ask_mode'),
    EndpointSpec('GET', '/analytics/team/client-versions', 'get_analytics_team_client_versions'),
    EndpointSpec('GET', '/analytics/team/commands', 'get_analytics_team_commands'),
    EndpointSpec('GET', '/analytics/team/dau', 'get_analytics_team_dau'),
    EndpointSpec('GET', '/analytics/team/leaderboard', 'get_analytics_team_leaderboard'),
    EndpointSpec('GET', '/analytics/team/mcp', 'get_analytics_team_mcp'),
    EndpointSpec('GET', '/analytics/team/models', 'get_analytics_team_models'),
    EndpointSpec('GET', '/analytics/team/plans', 'get_analytics_team_plans'),
    EndpointSpec('GET', '/analytics/team/tabs', 'get_analytics_team_tabs'),
    EndpointSpec('GET', '/analytics/team/top-file-extensions', 'get_analytics_team_top_file_extensions'),
    EndpointSpec('GET', '/settings/repo-blocklists/repos', 'get_settings_repo_blocklists_repos'),
    EndpointSpec('GET', '/teams/audit-logs', 'get_teams_audit_logs'),
    EndpointSpec('GET', '/teams/groups', 'get_teams_groups'),
    EndpointSpec('GET', '/teams/groups/:groupId', 'get_teams_groups_group_id'),
    EndpointSpec('GET', '/teams/members', 'get_teams_members'),
    EndpointSpec('GET', '/v0/agents', 'get_v0_agents'),
    EndpointSpec('GET', '/v0/agents/{id}', 'get_v0_agents_id'),
    EndpointSpec('GET', '/v0/agents/{id}/conversation', 'get_v0_agents_id_conversation'),
    EndpointSpec('GET', '/v0/me', 'get_v0_me'),
    EndpointSpec('GET', '/v0/models', 'get_v0_models'),
    EndpointSpec('GET', '/v0/repositories', 'get_v0_repositories'),
    EndpointSpec('PATCH', '/teams/groups/:groupId', 'patch_teams_groups_group_id'),
    EndpointSpec('POST', '/bugbot/repo/update', 'post_bugbot_repo_update'),
    EndpointSpec('POST', '/settings/repo-blocklists/repos/upsert', 'post_settings_repo_blocklists_repos_upsert'),
    EndpointSpec('POST', '/teams/daily-usage-data', 'post_teams_daily_usage_data'),
    EndpointSpec('POST', '/teams/filtered-usage-events', 'post_teams_filtered_usage_events'),
    EndpointSpec('POST', '/teams/groups', 'post_teams_groups'),
    EndpointSpec('POST', '/teams/groups/:groupId/members', 'post_teams_groups_group_id_members'),
    EndpointSpec('POST', '/teams/spend', 'post_teams_spend'),
    EndpointSpec('POST', '/teams/user-spend-limit', 'post_teams_user_spend_limit'),
    EndpointSpec('POST', '/v0/agents', 'post_v0_agents'),
    EndpointSpec('POST', '/v0/agents/{id}/followup', 'post_v0_agents_id_followup'),
    EndpointSpec('POST', '/v0/agents/{id}/stop', 'post_v0_agents_id_stop'),
)

__all__ = ["CursorClient", "AuthType", "ENDPOINT_SPECS"]


class CursorClient:
    """Synchronous client for the public Cursor APIs.

    This client provides methods for all documented Cursor API endpoints. Method names
    are derived directly from the HTTP method and path (e.g., GET /teams/members becomes
    get_teams_members). While these names can be long, this design ensures a 1:1 mapping
    with the API documentation and prevents naming conflicts.

    The SDK supports endpoints from multiple API versions:
    - `/v0/*` endpoints are part of the v0 API
    - Non-prefixed endpoints (e.g., `/teams/*`, `/analytics/*`) are versioned independently

    See the main README.md for usage examples and authentication details.
    """

    def __init__(
        self,
        api_key: str,
        *,
        base_url: str = "https://api.cursor.com",
        auth: AuthType = "basic",
        timeout: float = DEFAULT_TIMEOUT,
        transport: Optional[httpx.BaseTransport] = None,
        default_headers: Optional[Mapping[str, str]] = None,
        validate_api_key: bool = False,
        allow_http: bool = False,
    ) -> None:
        if not api_key:
            raise ValueError("api_key is required")

        # Optional API key format validation
        if validate_api_key:
            if len(api_key) < 3:
                raise ValueError("api_key is too short (minimum 3 characters)")
            # Admin/AI Code Tracking API keys typically start with "key_"
            # but we don't enforce this as other key formats may exist
            if not re.match(r"^[a-zA-Z0-9_\-]+$", api_key):
                raise ValueError("api_key contains invalid characters (only alphanumeric, underscore, and hyphen allowed)")

        # HTTPS enforcement
        parsed_url = urlparse(base_url)
        if parsed_url.scheme == "http" and not allow_http:
            raise ValueError(
                "HTTP URLs are not allowed for security reasons. Use HTTPS or set allow_http=True for testing only."
            )
        if parsed_url.scheme == "http" and allow_http:
            import warnings
            warnings.warn(
                "Using HTTP is insecure and may expose your API key. Use HTTPS in production.",
                UserWarning,
                stacklevel=2,
            )

        self._api_key = api_key
        self._auth = auth
        self._default_headers = dict(default_headers or {})
        self._client = httpx.Client(base_url=base_url, timeout=timeout, transport=transport)

    def __repr__(self) -> str:
        """Return a safe representation that doesn't expose the API key."""
        return f"<CursorClient(base_url='{self._client.base_url}', auth='{self._auth}')>"

    def __str__(self) -> str:
        """Return a safe string representation that doesn't expose the API key."""
        return f"CursorClient(base_url='{self._client.base_url}', auth='{self._auth}')"

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "CursorClient":
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
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
        if extra:
            headers.update(extra)
        # Always set Authorization last to ensure it cannot be overridden
        headers["Authorization"] = self._auth_header_value()
        return headers

    def _sanitize_path_param(self, param: str, param_name: str) -> str:
        """Sanitize path parameters to prevent path traversal and injection attacks.

        Args:
            param: The path parameter value to sanitize
            param_name: The name of the parameter (for error messages)

        Returns:
            The sanitized parameter value (URL encoded)

        Raises:
            ValueError: If the parameter contains dangerous characters
        """
        if not param:
            raise ValueError(f"{param_name} cannot be empty")

        # Reject path traversal attempts and dangerous characters
        # Check for path separators and control characters that could be exploited
        dangerous_patterns = ["/", "\\", "..", "\0", "\r", "\n"]
        for pattern in dangerous_patterns:
            if pattern in param:
                # Escape the pattern for display in error message
                display_pattern = repr(pattern) if len(pattern) == 1 else pattern
                raise ValueError(
                    f"{param_name} contains invalid character(s) {display_pattern}. "
                    "Path parameters must not contain path separators or control characters."
                )

        # URL encode the parameter to handle special characters safely
        # This ensures the parameter is safe for use in URLs
        # Safe characters are already handled, so we encode everything else
        from urllib.parse import quote
        return quote(param, safe="")

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        json: Any = None,  # Any is necessary here as JSON can be dict, list, or primitive types
        headers: Optional[Mapping[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Union[dict, list, str, None]:
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
            error_msg = f"Request failed due to a network error: {method} {path}"
            raise CursorNetworkError(error_msg, method=method, url=path, cause=e) from e

        if resp.status_code == HTTP_STATUS_NOT_MODIFIED:
            return None

        if 200 <= resp.status_code < 300:
            if not resp.content:
                return None

            content_type = resp.headers.get("content-type", "")
            if "text/csv" in content_type or path.endswith(".csv"):
                return resp.text

            if "application/json" in content_type or content_type.endswith("+json"):
                try:
                    return resp.json()
                except (ValueError, TypeError):
                    # If JSON parsing fails despite content-type, fallback to text
                    return resp.text

            # Fallback: try to parse as JSON, otherwise return as text
            # This handles cases where content-type is missing or unexpected
            try:
                return resp.json()
            except (ValueError, TypeError):
                # ValueError for invalid JSON, TypeError for non-string content
                return resp.text

        # Extract error message from response body
        # Priority: message field > error field > reason phrase > default message
        body: Any = None
        message = resp.reason_phrase or "Request failed."
        try:
            body = resp.json()
            if isinstance(body, dict):
                # Try "message" first, then "error", fallback to reason phrase
                message = str(body.get("message") or body.get("error") or message)
        except (ValueError, TypeError):
            # If JSON parsing fails, use text body if available
            body = resp.text if resp.text else None
            if body:
                message = str(body)

        exc_cls = CursorAPIError
        if resp.status_code in (HTTP_STATUS_UNAUTHORIZED, HTTP_STATUS_FORBIDDEN):
            exc_cls = CursorAuthError
        elif resp.status_code == HTTP_STATUS_TOO_MANY_REQUESTS:
            exc_cls = CursorRateLimitError

        raise exc_cls(
            resp.status_code,
            message,
            body=body,
            headers=dict(resp.headers),
            method=method,
            url=path,
        )

    def delete_settings_repo_blocklists_repos_repo_id(self, repo_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """DELETE /settings/repo-blocklists/repos/:repoId"""
        repo_id = self._sanitize_path_param(repo_id, "repo_id")
        return self._request('DELETE', f'/settings/repo-blocklists/repos/{repo_id}', params=params, headers=headers, timeout=timeout)

    def delete_teams_groups_group_id(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """DELETE /teams/groups/:groupId"""
        group_id = self._sanitize_path_param(group_id, "group_id")
        return self._request('DELETE', f'/teams/groups/{group_id}', params=params, headers=headers, timeout=timeout)

    def delete_teams_groups_group_id_members(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """DELETE /teams/groups/:groupId/members"""
        group_id = self._sanitize_path_param(group_id, "group_id")
        return self._request('DELETE', f'/teams/groups/{group_id}/members', params=params, headers=headers, timeout=timeout)

    def delete_v0_agents_id(self, id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """DELETE /v0/agents/{id}"""
        id = self._sanitize_path_param(id, "id")
        return self._request('DELETE', f'/v0/agents/{id}', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_changes(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/ai-code/changes"""
        return self._request('GET', '/analytics/ai-code/changes', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_changes_csv(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/ai-code/changes.csv"""
        return self._request('GET', '/analytics/ai-code/changes.csv', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_commits(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/ai-code/commits"""
        return self._request('GET', '/analytics/ai-code/commits', params=params, headers=headers, timeout=timeout)

    def get_analytics_ai_code_commits_csv(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/ai-code/commits.csv"""
        return self._request('GET', '/analytics/ai-code/commits.csv', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_agent_edits(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/agent-edits"""
        return self._request('GET', '/analytics/by-user/agent-edits', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_ask_mode(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/ask-mode"""
        return self._request('GET', '/analytics/by-user/ask-mode', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_client_versions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/client-versions"""
        return self._request('GET', '/analytics/by-user/client-versions', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_commands(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/commands"""
        return self._request('GET', '/analytics/by-user/commands', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_mcp(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/mcp"""
        return self._request('GET', '/analytics/by-user/mcp', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_models(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/models"""
        return self._request('GET', '/analytics/by-user/models', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_plans(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/plans"""
        return self._request('GET', '/analytics/by-user/plans', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_tabs(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/tabs"""
        return self._request('GET', '/analytics/by-user/tabs', params=params, headers=headers, timeout=timeout)

    def get_analytics_by_user_top_file_extensions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/by-user/top-file-extensions"""
        return self._request('GET', '/analytics/by-user/top-file-extensions', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_agent_edits(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/agent-edits"""
        return self._request('GET', '/analytics/team/agent-edits', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_ask_mode(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/ask-mode"""
        return self._request('GET', '/analytics/team/ask-mode', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_client_versions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/client-versions"""
        return self._request('GET', '/analytics/team/client-versions', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_commands(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/commands"""
        return self._request('GET', '/analytics/team/commands', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_dau(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/dau"""
        return self._request('GET', '/analytics/team/dau', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_leaderboard(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/leaderboard"""
        return self._request('GET', '/analytics/team/leaderboard', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_mcp(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/mcp"""
        return self._request('GET', '/analytics/team/mcp', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_models(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/models"""
        return self._request('GET', '/analytics/team/models', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_plans(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/plans"""
        return self._request('GET', '/analytics/team/plans', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_tabs(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/tabs"""
        return self._request('GET', '/analytics/team/tabs', params=params, headers=headers, timeout=timeout)

    def get_analytics_team_top_file_extensions(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /analytics/team/top-file-extensions"""
        return self._request('GET', '/analytics/team/top-file-extensions', params=params, headers=headers, timeout=timeout)

    def get_settings_repo_blocklists_repos(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /settings/repo-blocklists/repos"""
        return self._request('GET', '/settings/repo-blocklists/repos', params=params, headers=headers, timeout=timeout)

    def get_teams_audit_logs(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /teams/audit-logs"""
        return self._request('GET', '/teams/audit-logs', params=params, headers=headers, timeout=timeout)

    def get_teams_groups(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /teams/groups"""
        return self._request('GET', '/teams/groups', params=params, headers=headers, timeout=timeout)

    def get_teams_groups_group_id(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /teams/groups/:groupId"""
        group_id = self._sanitize_path_param(group_id, "group_id")
        return self._request('GET', f'/teams/groups/{group_id}', params=params, headers=headers, timeout=timeout)

    def get_teams_members(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /teams/members"""
        return self._request('GET', '/teams/members', params=params, headers=headers, timeout=timeout)

    def get_v0_agents(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /v0/agents"""
        return self._request('GET', '/v0/agents', params=params, headers=headers, timeout=timeout)

    def get_v0_agents_id(self, id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /v0/agents/{id}"""
        id = self._sanitize_path_param(id, "id")
        return self._request('GET', f'/v0/agents/{id}', params=params, headers=headers, timeout=timeout)

    def get_v0_agents_id_conversation(self, id: str, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /v0/agents/{id}/conversation"""
        id = self._sanitize_path_param(id, "id")
        return self._request('GET', f'/v0/agents/{id}/conversation', params=params, headers=headers, timeout=timeout)

    def get_v0_me(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /v0/me"""
        return self._request('GET', '/v0/me', params=params, headers=headers, timeout=timeout)

    def get_v0_models(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /v0/models"""
        return self._request('GET', '/v0/models', params=params, headers=headers, timeout=timeout)

    def get_v0_repositories(self, *, params: Optional[Mapping[str, Any]] = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """GET /v0/repositories"""
        return self._request('GET', '/v0/repositories', params=params, headers=headers, timeout=timeout)

    def patch_teams_groups_group_id(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """PATCH /teams/groups/:groupId"""
        group_id = self._sanitize_path_param(group_id, "group_id")
        return self._request('PATCH', f'/teams/groups/{group_id}', params=params, json=json, headers=headers, timeout=timeout)

    def post_bugbot_repo_update(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /bugbot/repo/update"""
        return self._request('POST', '/bugbot/repo/update', params=params, json=json, headers=headers, timeout=timeout)

    def post_settings_repo_blocklists_repos_upsert(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /settings/repo-blocklists/repos/upsert"""
        return self._request('POST', '/settings/repo-blocklists/repos/upsert', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_daily_usage_data(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /teams/daily-usage-data"""
        return self._request('POST', '/teams/daily-usage-data', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_filtered_usage_events(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /teams/filtered-usage-events"""
        return self._request('POST', '/teams/filtered-usage-events', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_groups(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /teams/groups"""
        return self._request('POST', '/teams/groups', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_groups_group_id_members(self, group_id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /teams/groups/:groupId/members"""
        group_id = self._sanitize_path_param(group_id, "group_id")
        return self._request('POST', f'/teams/groups/{group_id}/members', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_spend(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /teams/spend"""
        return self._request('POST', '/teams/spend', params=params, json=json, headers=headers, timeout=timeout)

    def post_teams_user_spend_limit(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /teams/user-spend-limit"""
        return self._request('POST', '/teams/user-spend-limit', params=params, json=json, headers=headers, timeout=timeout)

    def post_v0_agents(self, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /v0/agents"""
        return self._request('POST', '/v0/agents', params=params, json=json, headers=headers, timeout=timeout)

    def post_v0_agents_id_followup(self, id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /v0/agents/{id}/followup"""
        id = self._sanitize_path_param(id, "id")
        return self._request('POST', f'/v0/agents/{id}/followup', params=params, json=json, headers=headers, timeout=timeout)

    def post_v0_agents_id_stop(self, id: str, *, params: Optional[Mapping[str, Any]] = None, json: Any = None, headers: Optional[Mapping[str, str]] = None, timeout: Optional[float] = None) -> Union[dict, list, str, None]:
        """POST /v0/agents/{id}/stop"""
        id = self._sanitize_path_param(id, "id")
        return self._request('POST', f'/v0/agents/{id}/stop', params=params, json=json, headers=headers, timeout=timeout)
