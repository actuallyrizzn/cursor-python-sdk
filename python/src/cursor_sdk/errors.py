"""Exception classes for the Cursor SDK.

This module defines the exception hierarchy used throughout the SDK
for handling API errors, authentication failures, rate limits, and
network issues.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional
from types import TracebackType


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
    body: Any = None  # Any is necessary as error bodies can be dict, list, str, or other types
    headers: Optional[Mapping[str, str]] = None
    method: Optional[str] = None
    url: Optional[str] = None

    def __str__(self) -> str:  # pragma: no cover
        # Keep the default repr noise out of user output.
        context = ""
        if self.method and self.url:
            context = f" ({self.method} {self.url})"
        return f"Cursor API error {self.status_code}: {self.message}{context}"


class CursorAuthError(CursorAPIError):
    """Raised on 401/403 responses."""


class CursorRateLimitError(CursorAPIError):
    """Raised on 429 responses."""


class CursorNetworkError(CursorError):
    """Raised on network/transport errors."""

    def __init__(
        self,
        message: str,
        *,
        cause: Exception,
        method: Optional[str] = None,
        url: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.__cause__ = cause
        self.method = method
        self.url = url

    def __str__(self) -> str:  # pragma: no cover
        context = ""
        if self.method and self.url:
            context = f" ({self.method} {self.url})"
        return f"{self.args[0]}{context}"
