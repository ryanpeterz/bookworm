import sys
import cred  # sets API-key by side effect
import hunk
import openai
import ratelimiter
import tokenlimiter
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.FileHandler(".gpt3.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

# OpenAI docs describe a 20qpm rate limit for free tier
# which seems to mean "no more than 2 queries in any 6-sec period"
rate_limiter = ratelimiter.RateLimiter(
    max_calls=1,
    period=3.1,
    callback=lambda until: logger.debug(f"ratelimited until {until}"))

token_limiter = tokenlimiter.TokenLimiter(
    max_tokens=150000,
    period=60,
    callback=lambda tokens: logger.debug("tokenlimited by {token} token burn"))

MODEL        = "text-davinci-003"
TEMPERATURE  = .7
TOKEN_BUDGET = 4096


def politely(prompt: hunk.Hunk, model: str = MODEL) -> hunk.Hunk:
    logger.info(f"prompt[{prompt.tokens}]:\n{prompt.text}")

    with rate_limiter:
        with token_limiter as burn:
            burn(TOKEN_BUDGET)  # overkill in most cases
            response = openai.Completion.create(
                model=model,
                prompt=prompt.text,
                max_tokens=TOKEN_BUDGET - prompt.tokens)
            # TODO(b/): immediately restore unused tokens
            # unburn(TOKEN_BUDGET - response["usage"]["total_tokens"])

    logger.info(f"response:\n{response}")

    # in this implementation, only one choice is returned
    return hunk.of_text(response["choices"][0]["text"].strip())


__all__ = ["politely"]


def _run_test():
    response = politely(hunk.of_text("test"))
    

if __name__ == "__main__": _run_test()
