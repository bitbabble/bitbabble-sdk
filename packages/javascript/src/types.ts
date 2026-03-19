export type Sentiment = "negative" | "neutral" | "positive";
export type Confidence = "low" | "medium" | "high";

export interface SentimentResult {
  sentiment: Sentiment;
  /** Score from -1 (bearish) to +1 (bullish) */
  score: number;
  confidence: Confidence;
  /** Whether the result was served from this user's cache */
  cached: boolean;
}

export interface BitBabbleClientOptions {
  /** Override the base URL (defaults to https://bitbabble.net/api/v1) */
  baseUrl?: string;
}
