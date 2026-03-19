# bitbabble-sdk

Official JavaScript/TypeScript SDK for the [BitBabble](https://bitbabble.net) sentiment analysis API.

**Get 100 tokens free when you sign up.** Create an account at [bitbabble.net](https://bitbabble.net) to receive your API key.

## Creating an Account

1. Go to [bitbabble.net](https://bitbabble.net)
2. Sign up for a new account
3. Copy your API key from the dashboard
4. **100 tokens** are credited automatically—no credit card required

## Installation

```bash
npm install bitbabble-sdk
```

## Quick Start

```typescript
import { BitBabbleClient } from "bitbabble-sdk";

const client = new BitBabbleClient("bb_your_api_key");
const result = await client.sentiment("I love this product!");

console.log(result);
// {
//   sentiment: "positive",
//   score: 0.82,
//   confidence: "high",
//   cached: false
// }
```

## API

### `new BitBabbleClient(apiKey, options?)`

| Parameter          | Type     | Description                              |
| ------------------ | -------- | ---------------------------------------- |
| `apiKey`           | `string` | Your BitBabble API key                   |
| `options.baseUrl`  | `string` | Override the API base URL (optional)     |

### `client.sentiment(text)`

Analyze the sentiment of a text string (1–140 characters).

Returns a `Promise<SentimentResult>`:

| Field        | Type                                   | Description                              |
| ------------ | -------------------------------------- | ---------------------------------------- |
| `sentiment`  | `"negative" \| "neutral" \| "positive"` | Predicted sentiment label                |
| `score`      | `number`                               | Score from -1 (bearish) to +1 (bullish)  |
| `confidence` | `"low" \| "medium" \| "high"`          | Confidence of the prediction             |
| `cached`     | `boolean`                              | Whether the result was served from cache |

## Error Handling

The SDK throws typed errors for API failures:

```typescript
import {
  BitBabbleClient,
  AuthenticationError,
  InsufficientCreditsError,
  RateLimitError,
} from "bitbabble-sdk";

try {
  const result = await client.sentiment("some text");
} catch (err) {
  if (err instanceof AuthenticationError) {
    // 401 — invalid or missing API key
  } else if (err instanceof InsufficientCreditsError) {
    // 402 — out of credits
  } else if (err instanceof RateLimitError) {
    // 429 — too many requests
  }
}
```

## Requirements

- Node.js 18+ (uses native `fetch`)

## License

MIT
