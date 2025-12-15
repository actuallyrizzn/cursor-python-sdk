"""Retry utilities for handling transient errors."""

from __future__ import annotations

import time
from functools import wraps
from typing import Any, Callable, TypeVar

from cursor_sdk.errors import CursorNetworkError, CursorRateLimitError

T = TypeVar("T")


def retry_with_backoff(
    max_retries: int = 3,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
    exponential_base: float = 2.0,
    retry_on: tuple[type[Exception], ...] = (CursorNetworkError, CursorRateLimitError),
) -> Callable[[Callable[..., T]], Callable[..., T]]:
    """Decorator to retry a function with exponential backoff.

    Args:
        max_retries: Maximum number of retry attempts (default: 3)
        initial_delay: Initial delay in seconds before first retry (default: 1.0)
        max_delay: Maximum delay in seconds between retries (default: 60.0)
        exponential_base: Base for exponential backoff calculation (default: 2.0)
        retry_on: Tuple of exception types to retry on (default: network and rate limit errors)

    Returns:
        Decorated function that will retry on specified exceptions

    Example:
        ```python
        @retry_with_backoff(max_retries=5, initial_delay=0.5)
        def make_request():
            return client.get_v0_me()
        ```
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            last_exception: Exception | None = None
            delay = initial_delay

            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except retry_on as e:
                    last_exception = e

                    # Don't retry on the last attempt
                    if attempt == max_retries:
                        raise

                    # For rate limit errors, use longer delay
                    if isinstance(e, CursorRateLimitError):
                        # Use Retry-After header if available, otherwise use exponential backoff
                        retry_after = None
                        if hasattr(e, "headers") and e.headers:
                            # Headers are case-insensitive
                            retry_after_str = e.headers.get("Retry-After") or e.headers.get("retry-after")
                            if retry_after_str:
                                try:
                                    retry_after = float(retry_after_str)
                                except (ValueError, TypeError):
                                    pass

                        if retry_after:
                            delay = min(retry_after, max_delay)
                        else:
                            # Exponential backoff for rate limits
                            delay = min(initial_delay * (exponential_base ** attempt), max_delay)
                    else:
                        # Exponential backoff for network errors
                        delay = min(initial_delay * (exponential_base ** attempt), max_delay)

                    time.sleep(delay)

            # This should never be reached, but type checker needs it
            if last_exception:  # pragma: no cover
                raise last_exception
            raise RuntimeError("Retry logic failed unexpectedly")  # pragma: no cover

        return wrapper

    return decorator

