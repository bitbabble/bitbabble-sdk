# BitBabble SDK

Official SDKs for the [BitBabble](https://bitbabble.net) sentiment analysis API.

| Package | Language | Registry |
| --- | --- | --- |
| [`bitbabble`](packages/javascript/) | JavaScript / TypeScript | npm |
| [`bitbabble-sdk`](packages/python/) | Python | PyPI |

## Quick Start

### JavaScript / TypeScript

```bash
npm install bitbabble
```

```typescript
import { BitBabbleClient } from "bitbabble";

const client = new BitBabbleClient("bb_your_api_key");
const result = await client.sentiment("I love this product!");
// { sentiment: "positive", score: 0.82, confidence: "high", cached: false }
```

### Python

```bash
pip install bitbabble-sdk
```

```python
from bitbabble import BitBabbleClient

client = BitBabbleClient(api_key="bb_your_api_key")
result = client.sentiment("I love this product!")
# {"sentiment": "positive", "score": 0.82, "confidence": "high", "cached": False}
```

## API Documentation

Full API reference at [bitbabble.net/docs](https://bitbabble.net/docs).

## Publishing

Both packages are published automatically via GitHub Actions when a release is created:

- **npm** — see [`.github/workflows/publish-npm.yml`](.github/workflows/publish-npm.yml)
- **PyPI** — see [`.github/workflows/publish-pypi.yml`](.github/workflows/publish-pypi.yml)

### Required Secrets

| Secret | Description |
| --- | --- |
| `NPM_TOKEN` | npm access token with publish permission |
| `PYPI_API_TOKEN` | PyPI API token (or use trusted publishing with OIDC) |

## License

MIT
