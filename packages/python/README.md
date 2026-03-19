# bitbabble-sdk

Official Python SDK for the [BitBabble](https://bitbabble.net) sentiment analysis API.

## Installation

```bash
pip install bitbabble-sdk
```

## Quick Start

```python
from bitbabble import BitBabbleClient

client = BitBabbleClient(api_key="bb_your_api_key")
result = client.sentiment("I love this product!")

print(result)
# {
#     "sentiment": "positive",
#     "score": 0.82,
#     "confidence": "high",
#     "cached": False,
# }
```

## API

### `BitBabbleClient(api_key, *, base_url=...)`

| Parameter  | Type  | Description                          |
| ---------- | ----- | ------------------------------------ |
| `api_key`  | `str` | Your BitBabble API key               |
| `base_url` | `str` | Override the API base URL (optional) |

### `client.sentiment(text)`

Analyze the sentiment of a text string (1–140 characters).

Returns a `SentimentResult` (TypedDict):

| Field        | Type                                       | Description                              |
| ------------ | ------------------------------------------ | ---------------------------------------- |
| `sentiment`  | `"negative" \| "neutral" \| "positive"`    | Predicted sentiment label                |
| `score`      | `float`                                    | Score from -1 (bearish) to +1 (bullish)  |
| `confidence` | `"low" \| "medium" \| "high"`              | Confidence of the prediction             |
| `cached`     | `bool`                                     | Whether the result was served from cache |

## Error Handling

```python
from bitbabble import (
    BitBabbleClient,
    AuthenticationError,
    InsufficientCreditsError,
    RateLimitError,
)

try:
    result = client.sentiment("some text")
except AuthenticationError:
    # 401 — invalid or missing API key
    ...
except InsufficientCreditsError:
    # 402 — out of credits
    ...
except RateLimitError:
    # 429 — too many requests
    ...
```

## Requirements

- Python 3.8+
- [httpx](https://www.python-httpx.org/)

## License

MIT
