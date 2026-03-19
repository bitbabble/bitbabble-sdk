from __future__ import annotations

from typing import Literal

from typing import TypedDict


Sentiment = Literal["negative", "neutral", "positive"]
Confidence = Literal["low", "medium", "high"]


class SentimentResult(TypedDict):
    """Result returned by the sentiment analysis endpoint."""

    sentiment: Sentiment
    """Predicted sentiment label."""
    score: float
    """Score from -1 (bearish) to +1 (bullish)."""
    confidence: Confidence
    """Confidence of the prediction."""
    cached: bool
    """Whether the result was served from this user's cache."""
