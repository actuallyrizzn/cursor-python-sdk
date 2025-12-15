"""Tests for path parameter sanitization and security."""

import httpx
import pytest

from cursor_sdk import CursorClient


def test_path_param_rejects_path_traversal() -> None:
    """Test that path parameters reject path traversal attempts."""
    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(200)))

    # Test various path traversal attempts
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("../admin")
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("../../etc/passwd")
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_teams_groups_group_id("group/../admin")

    client.close()


def test_path_param_rejects_slashes() -> None:
    """Test that path parameters reject slashes."""
    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(200)))

    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("id/extra")
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_teams_groups_group_id("group\\path")

    client.close()


def test_path_param_rejects_control_characters() -> None:
    """Test that path parameters reject control characters."""
    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(200)))

    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("id\ninjection")
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("id\rinjection")
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("id\0null")

    client.close()


def test_path_param_rejects_empty_string() -> None:
    """Test that path parameters reject empty strings."""
    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(lambda r: httpx.Response(200)))

    with pytest.raises(ValueError, match="cannot be empty"):
        client.get_v0_agents_id("")
    with pytest.raises(ValueError, match="cannot be empty"):
        client.get_teams_groups_group_id("")

    client.close()


def test_path_param_url_encodes_special_chars() -> None:
    """Test that path parameters are URL encoded for special characters."""
    def handler(request: httpx.Request) -> httpx.Response:
        # httpx automatically decodes the path, so check the raw URL string
        url_str = str(request.url)
        # The space should be encoded as %20 in the URL
        assert "%20" in url_str or "test%20id" in url_str
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))
    # Space should be encoded
    result = client.get_v0_agents_id("test id")
    assert result == {"ok": True}
    client.close()


def test_path_param_allows_valid_characters() -> None:
    """Test that valid path parameters are accepted."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    # Valid characters should work
    result = client.get_v0_agents_id("valid-id_123")
    assert result == {"ok": True}

    result = client.get_teams_groups_group_id("group-123")
    assert result == {"ok": True}

    result = client.delete_settings_repo_blocklists_repos_repo_id("repo_123")
    assert result == {"ok": True}

    client.close()


def test_path_param_injection_attempts() -> None:
    """Test various injection attempt patterns are properly handled."""
    def handler(request: httpx.Request) -> httpx.Response:
        # Verify the URL is properly encoded
        url_str = str(request.url)
        # Special characters should be URL encoded
        assert "%27" in url_str or "%3B" in url_str or "%3C" in url_str or "%3E" in url_str
        return httpx.Response(200, json={"ok": True})

    client = CursorClient("test_key", base_url="https://example.test", transport=httpx.MockTransport(handler))

    # SQL injection patterns - these will be URL encoded (safe)
    result = client.get_v0_agents_id("'; DROP TABLE--")
    assert result == {"ok": True}

    # Command injection patterns with slashes should be rejected
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("id; rm -rf /")

    # XSS patterns with slashes should be rejected
    with pytest.raises(ValueError, match="contains invalid character"):
        client.get_v0_agents_id("<script>/alert</script>")

    # But XSS without slashes will be URL encoded (safe)
    result = client.get_v0_agents_id("<script>alert('xss')")
    assert result == {"ok": True}

    client.close()

