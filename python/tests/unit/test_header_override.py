"""Tests for header override protection."""

import httpx
import pytest

from cursor_sdk import CursorClient


def test_authorization_header_cannot_be_overridden() -> None:
    """Test that Authorization header cannot be overridden by extra headers."""
    client = CursorClient(
        "test_key",
        default_headers={"Authorization": "should-be-overridden"},
    )

    # Try to override Authorization in extra headers
    headers = client._build_headers({"Authorization": "Bearer malicious"})

    # Authorization should always be set from api_key/auth, not from extra headers
    assert headers["Authorization"].startswith("Basic ")
    assert "Bearer malicious" not in headers["Authorization"]
    client.close()


def test_extra_headers_are_merged_correctly() -> None:
    """Test that extra headers are merged without overriding Authorization."""
    client = CursorClient("test_key", default_headers={"X-Custom": "default"})

    headers = client._build_headers({"X-Custom": "override", "X-New": "value"})

    # Default headers should be merged
    # Extra headers should override default headers (except Authorization)
    assert headers["X-Custom"] == "override"
    assert headers["X-New"] == "value"
    # Authorization should still be set correctly
    assert headers["Authorization"].startswith("Basic ")
    client.close()


