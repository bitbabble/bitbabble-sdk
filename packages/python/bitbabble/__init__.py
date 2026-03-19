"""Official Python SDK for the BitBabble sentiment analysis API."""

from bitbabble.client import BitBabbleClient
from bitbabble.errors import (
    AuthenticationError,
    BitBabbleError,
    InsufficientCreditsError,
    RateLimitError,
)
from bitbabble.types import SentimentResult

__all__ = [
    "BitBabbleClient",
    "BitBabbleError",
    "AuthenticationError",
    "InsufficientCreditsError",
    "RateLimitError",
    "SentimentResult",
]
