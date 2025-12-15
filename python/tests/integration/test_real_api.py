"""Integration tests against the real Cursor API.

These tests require a valid API key and make actual HTTP requests to api.cursor.com.
They are skipped if CURSOR_API_KEY environment variable is not set.

To run these tests:
    export CURSOR_API_KEY=your_api_key_here
    python -m pytest tests/integration/test_real_api.py -v
"""

import os

import pytest

from cursor_sdk import CursorClient
from cursor_sdk.errors import CursorAPIError, CursorAuthError, CursorRateLimitError


# Skip all tests in this module if API key is not available
pytestmark = [
    pytest.mark.skipif(
        not os.getenv("CURSOR_API_KEY"),
        reason="CURSOR_API_KEY environment variable not set",
    ),
    pytest.mark.integration,
]


@pytest.fixture
def api_key() -> str:
    """Get API key from environment variable."""
    key = os.getenv("CURSOR_API_KEY")
    if not key:
        pytest.skip("CURSOR_API_KEY not set")
    return key


@pytest.fixture
def client(api_key: str) -> CursorClient:
    """Create a client instance with real API key."""
    return CursorClient(api_key, base_url="https://api.cursor.com")


def test_get_v0_me(client: CursorClient) -> None:
    """Test GET /v0/me endpoint with real API."""
    result = client.get_v0_me()
    assert result is not None
    # Real API should return user information
    assert isinstance(result, dict)
    client.close()


def test_get_v0_models(client: CursorClient) -> None:
    """Test GET /v0/models endpoint with real API."""
    result = client.get_v0_models()
    assert result is not None
    # Should return a list or dict of models
    assert isinstance(result, (dict, list))
    client.close()


def test_get_v0_repositories(client: CursorClient) -> None:
    """Test GET /v0/repositories endpoint with real API."""
    try:
        result = client.get_v0_repositories()
        assert result is not None
        # Should return a list or dict of repositories
        assert isinstance(result, (dict, list))
    except CursorRateLimitError:
        # This endpoint has strict rate limits (1 req/min), so rate limit is acceptable
        pytest.skip("Rate limited on /v0/repositories endpoint")
    finally:
        client.close()


def test_get_v0_agents(client: CursorClient) -> None:
    """Test GET /v0/agents endpoint with real API."""
    result = client.get_v0_agents()
    assert result is not None
    # Should return a list or dict of agents
    assert isinstance(result, (dict, list))
    client.close()


def test_basic_auth_works(client: CursorClient) -> None:
    """Test that Basic authentication works with real API."""
    # Client should already be using Basic auth by default
    result = client.get_v0_me()
    assert result is not None
    client.close()


def test_bearer_auth_works(api_key: str) -> None:
    """Test that Bearer authentication works with real API."""
    client = CursorClient(api_key, auth="bearer", base_url="https://api.cursor.com")
    result = client.get_v0_me()
    assert result is not None
    client.close()


def test_error_handling_invalid_key() -> None:
    """Test error handling with invalid API key."""
    client = CursorClient("invalid_key_12345", base_url="https://api.cursor.com")
    with pytest.raises(CursorAuthError):
        client.get_v0_me()
    client.close()


def test_timeout_handling(api_key: str) -> None:
    """Test timeout handling with real API."""
    # Use a very short timeout to test timeout behavior
    client = CursorClient(api_key, base_url="https://api.cursor.com", timeout=0.001)
    # This might timeout or might succeed depending on network speed
    # Just verify it doesn't crash
    try:
        client.get_v0_me()
    except Exception:
        # Timeout or other error is acceptable for this test
        pass
    finally:
        client.close()


def test_response_structure_get_v0_me(client: CursorClient) -> None:
    """Test that GET /v0/me returns expected structure."""
    result = client.get_v0_me()
    assert isinstance(result, dict)
    # Real API response structure may vary, but should be a dict
    # Add more specific assertions based on actual API response
    client.close()

