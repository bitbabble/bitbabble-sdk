import {
  AuthenticationError,
  BitBabbleError,
  InsufficientCreditsError,
  RateLimitError,
} from "./errors.js";
import type { BitBabbleClientOptions, SentimentResult } from "./types.js";

const DEFAULT_BASE_URL = "https://data.bitbabble.net/api/v1";

export class BitBabbleClient {
  private readonly apiKey: string;
  private readonly baseUrl: string;

  constructor(apiKey: string, options?: BitBabbleClientOptions) {
    if (!apiKey) {
      throw new AuthenticationError("An API key is required");
    }
    this.apiKey = apiKey;
    this.baseUrl = options?.baseUrl?.replace(/\/+$/, "") ?? DEFAULT_BASE_URL;
  }

  async sentiment(text: string): Promise<SentimentResult> {
    const res = await fetch(`${this.baseUrl}/sentiment`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${this.apiKey}`,
      },
      body: JSON.stringify({ text }),
    });

    if (!res.ok) {
      await this.handleError(res);
    }

    return (await res.json()) as SentimentResult;
  }

  private async handleError(res: Response): Promise<never> {
    const body = await res.text().catch(() => "");

    switch (res.status) {
      case 401:
        throw new AuthenticationError(body || undefined);
      case 402:
        throw new InsufficientCreditsError(body || undefined);
      case 429:
        throw new RateLimitError(body || undefined);
      default:
        throw new BitBabbleError(
          body || `Request failed with status ${res.status}`,
          res.status,
        );
    }
  }
}
