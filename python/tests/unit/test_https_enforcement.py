"""Tests for HTTPS enforcement."""

import warnings

import httpx
import pytest

from cursor_sdk import CursorClient


def test_https_enforced_by_default() -> None:
    """Test that HTTP URLs are rejected by default."""
    with pytest.raises(ValueError, match="HTTP URLs are not allowed"):
        CursorClient("test_key", base_url="http://example.com")


def test_http_allowed_with_flag() -> None:
    """Test that HTTP is allowed when allow_http=True."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        client = CursorClient(
            "test_key",
            base_url="http://example.com",
            allow_http=True,
            transport=httpx.MockTransport(lambda r: httpx.Response(200, json={"ok": True})),
        )

        # Should have a warning
        assert len(w) == 1
        assert "insecure" in str(w[0].message).lower()
        assert "HTTP" in str(w[0].message)

        # But should still work
        result = client.get_v0_me()
        assert result == {"ok": True}

        client.close()


def test_https_allowed_without_flag() -> None:
    """Test that HTTPS works without the flag."""
    client = CursorClient(
        "test_key",
        base_url="https://example.com",
        transport=httpx.MockTransport(lambda r: httpx.Response(200, json={"ok": True})),
    )

    result = client.get_v0_me()
    assert result == {"ok": True}

    client.close()


def test_http_warning_message() -> None:
    """Test that HTTP warning message is appropriate."""
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        CursorClient("test_key", base_url="http://example.com", allow_http=True)

        assert len(w) == 1
        assert "insecure" in str(w[0].message).lower()
        assert "production" in str(w[0].message).lower()

