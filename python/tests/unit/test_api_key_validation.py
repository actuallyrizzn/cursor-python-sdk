"""Tests for API key validation."""

import pytest

from cursor_sdk import CursorClient


def test_api_key_validation_disabled_by_default() -> None:
    """Test that API key validation is disabled by default."""
    # Should work without validation
    client = CursorClient("short", base_url="https://example.test")
    client.close()


def test_api_key_validation_rejects_short_keys() -> None:
    """Test that validation rejects keys that are too short."""
    with pytest.raises(ValueError, match="too short"):
        CursorClient("ab", base_url="https://example.test", validate_api_key=True)


def test_api_key_validation_rejects_invalid_characters() -> None:
    """Test that validation rejects keys with invalid characters."""
    with pytest.raises(ValueError, match="invalid characters"):
        CursorClient("key with spaces", base_url="https://example.test", validate_api_key=True)

    with pytest.raises(ValueError, match="invalid characters"):
        CursorClient("key@invalid", base_url="https://example.test", validate_api_key=True)

    with pytest.raises(ValueError, match="invalid characters"):
        CursorClient("key#invalid", base_url="https://example.test", validate_api_key=True)


def test_api_key_validation_accepts_valid_keys() -> None:
    """Test that validation accepts valid key formats."""
    # Valid keys should pass
    client = CursorClient("key_abc123", base_url="https://example.test", validate_api_key=True)
    client.close()

    client = CursorClient("token-123", base_url="https://example.test", validate_api_key=True)
    client.close()

    client = CursorClient("valid_key_123", base_url="https://example.test", validate_api_key=True)
    client.close()


def test_api_key_validation_minimum_length() -> None:
    """Test that validation enforces minimum length."""
    # Exactly 3 characters should pass
    client = CursorClient("abc", base_url="https://example.test", validate_api_key=True)
    client.close()

    # Less than 3 should fail
    with pytest.raises(ValueError, match="too short"):
        CursorClient("ab", base_url="https://example.test", validate_api_key=True)

