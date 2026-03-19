from __future__ import annotations

import httpx

from bitbabble.errors import (
    AuthenticationError,
    BitBabbleError,
    InsufficientCreditsError,
    RateLimitError,
)
from bitbabble.types import SentimentResult

DEFAULT_BASE_URL = "https://data.bitbabble.net/api/v1"


class BitBabbleClient:
    """Client for the BitBabble sentiment analysis API."""

    def __init__(self, api_key: str, *, base_url: str = DEFAULT_BASE_URL) -> None:
        if not api_key:
            raise AuthenticationError("An API key is required")
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")

    def sentiment(self, text: str) -> SentimentResult:
        """Analyze the sentiment of *text* (1–140 characters).

        Returns a ``SentimentResult`` dict with ``sentiment``, ``score``,
        ``confidence``, and ``cached`` keys.
        """
        response = httpx.post(
            f"{self._base_url}/sentiment",
            json={"text": text},
            headers={
                "Authorization": f"Bearer {self._api_key}",
            },
        )

        if response.status_code != 200:
            self._handle_error(response)

        return response.json()  # type: ignore[return-value]

    @staticmethod
    def _handle_error(response: httpx.Response) -> None:
        body = response.text
        status = response.status_code

        if status == 401:
            raise AuthenticationError(body or "Invalid or missing API key")
        if status == 402:
            raise InsufficientCreditsError(body or "Insufficient credits")
        if status == 429:
            raise RateLimitError(body or "Too many requests")

        raise BitBabbleError(body or f"Request failed with status {status}", status)
