# BitBabble SDK

Official SDKs for the [BitBabble](https://bitbabble.net) sentiment analysis API.

**Get 100 tokens free when you sign up.** Create an account at [bitbabble.net](https://bitbabble.net) to receive your API key and start analyzing sentiment in seconds.

| Package | Language | Registry |
| --- | --- | --- |
| [`bitbabble-sdk`](packages/javascript/) | JavaScript / TypeScript | npm |
| [`bitbabble-sdk`](packages/python/) | Python | PyPI |

## Creating an Account

1. Go to [bitbabble.net](https://bitbabble.net)
2. Sign up for a new account
3. Copy your API key from the dashboard
4. **100 tokens** are credited automatically to your account when you sign up—no credit card required

## Quick Start

### JavaScript / TypeScript

```bash
npm install bitbabble-sdk
```

```typescript
import { BitBabbleClient } from "bitbabble-sdk";

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

## Version Bumping

To bump versions in both packages before merging:

```bash
./scripts/bump.sh patch   # 1.0.0 → 1.0.1
./scripts/bump.sh minor   # 1.0.0 → 1.1.0
./scripts/bump.sh major   # 1.0.0 → 2.0.0
```

Then commit the changes and merge.

## Publishing

Both packages are published automatically via GitHub Actions when you merge to `main`:

- **npm** — see [`.github/workflows/publish-npm.yml`](.github/workflows/publish-npm.yml)
- **PyPI** — see [`.github/workflows/publish-pypi.yml`](.github/workflows/publish-pypi.yml)

### Required Secrets

| Secret | Description |
| --- | --- |
| `NPM_TOKEN` | npm access token with publish permission |
| `PYPI_API_TOKEN` | PyPI API token (or use trusted publishing with OIDC) |

## License

MIT
