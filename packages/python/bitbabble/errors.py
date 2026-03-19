from __future__ import annotations


class BitBabbleError(Exception):
    """Base exception for all BitBabble API errors."""

    def __init__(self, message: str, status: int) -> None:
        super().__init__(message)
        self.status = status


class AuthenticationError(BitBabbleError):
    """Raised on 401 — invalid or missing API key."""

    def __init__(self, message: str = "Invalid or missing API key") -> None:
        super().__init__(message, 401)


class InsufficientCreditsError(BitBabbleError):
    """Raised on 402 — insufficient credits."""

    def __init__(self, message: str = "Insufficient credits") -> None:
        super().__init__(message, 402)


class RateLimitError(BitBabbleError):
    """Raised on 429 — too many requests."""

    def __init__(self, message: str = "Too many requests") -> None:
        super().__init__(message, 429)
