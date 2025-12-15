"""Exception classes for the Cursor SDK.

This module defines the exception hierarchy used throughout the SDK
for handling API errors, authentication failures, rate limits, and
network issues.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional


__all__ = [
    "CursorError",
    "CursorAPIError",
    "CursorAuthError",
    "CursorRateLimitError",
    "CursorNetworkError",
]


class CursorError(Exception):
    """Base exception for the Cursor SDK."""


@dataclass(frozen=True)
class CursorAPIError(CursorError):
    status_code: int
    message: str
    body: Any = None
    headers: Optional[Mapping[str, str]] = None

    def __str__(self) -> str:  # pragma: no cover
        # Keep the default repr noise out of user output.
        return f"Cursor API error {self.status_code}: {self.message}"


class CursorAuthError(CursorAPIError):
    """Raised on 401/403 responses."""


class CursorRateLimitError(CursorAPIError):
    """Raised on 429 responses."""


class CursorNetworkError(CursorError):
    """Raised on network/transport errors."""

    def __init__(self, message: str, *, cause: Exception) -> None:
        super().__init__(message)
        self.__cause__ = cause
