export class BitBabbleError extends Error {
  constructor(
    message: string,
    public readonly status: number,
  ) {
    super(message);
    this.name = "BitBabbleError";
  }
}

export class AuthenticationError extends BitBabbleError {
  constructor(message = "Invalid or missing API key") {
    super(message, 401);
    this.name = "AuthenticationError";
  }
}

export class InsufficientCreditsError extends BitBabbleError {
  constructor(message = "Insufficient credits") {
    super(message, 402);
    this.name = "InsufficientCreditsError";
  }
}

export class RateLimitError extends BitBabbleError {
  constructor(message = "Too many requests") {
    super(message, 429);
    this.name = "RateLimitError";
  }
}
