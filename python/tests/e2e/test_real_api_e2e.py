"""End-to-end tests against the real Cursor API.

These tests make actual HTTP requests to api.cursor.com and verify
the complete request/response cycle works correctly.

These tests require a valid API key and are skipped if CURSOR_API_KEY
environment variable is not set.

To run these tests:
    export CURSOR_API_KEY=your_api_key_here
    python -m pytest tests/e2e/test_real_api_e2e.py -v
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
    pytest.mark.e2e,
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


class TestRealAPIE2E:
    """End-to-end tests against the real Cursor API."""

    def test_complete_round_trip_get_v0_me(self, client: CursorClient) -> None:
        """Test complete round trip for GET /v0/me."""
        result = client.get_v0_me()
        assert result is not None
        assert isinstance(result, dict)
        client.close()

    def test_complete_round_trip_get_v0_agents(self, client: CursorClient) -> None:
        """Test complete round trip for GET /v0/agents."""
        result = client.get_v0_agents()
        assert result is not None
        # Should be a list or dict
        assert isinstance(result, (dict, list))
        client.close()

    def test_complete_round_trip_get_v0_repositories(self, client: CursorClient) -> None:
        """Test complete round trip for GET /v0/repositories."""
        try:
            result = client.get_v0_repositories()
            assert result is not None
            # Should be a list or dict
            assert isinstance(result, (dict, list))
        except CursorRateLimitError:
            # This endpoint has strict rate limits (1 req/min), so rate limit is acceptable
            pytest.skip("Rate limited on /v0/repositories endpoint")
        finally:
            client.close()

    def test_complete_round_trip_get_v0_models(self, client: CursorClient) -> None:
        """Test complete round trip for GET /v0/models."""
        result = client.get_v0_models()
        assert result is not None
        # Should be a list or dict
        assert isinstance(result, (dict, list))
        client.close()

    def test_context_manager_works(self, api_key: str) -> None:
        """Test that context manager works with real API."""
        with CursorClient(api_key, base_url="https://api.cursor.com") as client:
            result = client.get_v0_me()
            assert result is not None

    def test_multiple_requests_same_client(self, client: CursorClient) -> None:
        """Test making multiple requests with the same client."""
        # Make multiple requests to verify connection reuse
        result1 = client.get_v0_me()
        result2 = client.get_v0_models()
        
        # Skip repositories if rate limited (has strict 1 req/min limit)
        try:
            result3 = client.get_v0_repositories()
            assert result3 is not None
        except CursorRateLimitError:
            # Rate limit is acceptable for this endpoint
            pass

        assert result1 is not None
        assert result2 is not None

        client.close()

    def test_error_handling_unauthorized(self) -> None:
        """Test error handling for unauthorized requests."""
        client = CursorClient("invalid_key_for_testing", base_url="https://api.cursor.com")
        with pytest.raises(CursorAuthError) as exc_info:
            client.get_v0_me()
        assert exc_info.value.status_code in (401, 403)
        client.close()

    def test_rate_limit_error_handling(self, client: CursorClient) -> None:
        """Test rate limit error handling (if triggered)."""
        # This test may or may not trigger rate limiting depending on API usage
        # Just verify the client handles it gracefully
        try:
            # Make many rapid requests (if needed to trigger rate limit)
            for _ in range(10):
                client.get_v0_me()
        except CursorRateLimitError:
            # Rate limit error is expected and should be handled
            pass
        except CursorAPIError:
            # Other API errors are also acceptable
            pass
        finally:
            client.close()

    def test_retry_logic_with_real_api(self, api_key: str) -> None:
        """Test retry logic with real API (if applicable)."""
        from cursor_sdk.retry import retry_with_backoff

        client = CursorClient(api_key, base_url="https://api.cursor.com")

        @retry_with_backoff(max_retries=3, initial_delay=0.1)
        def make_request() -> dict:
            return client.get_v0_me()

        result = make_request()
        assert result is not None
        client.close()

