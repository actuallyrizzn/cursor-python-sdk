"""Python SDK for Cursor's public APIs.

This package provides a synchronous client for interacting with the Cursor API,
along with custom exception types for robust error handling and retry utilities.
"""

from cursor_sdk.client import CursorClient
from cursor_sdk.errors import (
    CursorAPIError,
    CursorAuthError,
    CursorError,
    CursorNetworkError,
    CursorRateLimitError,
)
from cursor_sdk.retry import retry_with_backoff

__all__ = [
    "CursorClient",
    "CursorError",
    "CursorAPIError",
    "CursorAuthError",
    "CursorRateLimitError",
    "CursorNetworkError",
    "retry_with_backoff",
]
