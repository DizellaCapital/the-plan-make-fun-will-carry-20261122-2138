"""Write the plan entry to /output/entry.txt.

The plan: find small shops with no chat support, build each a demo
chatbot, and sell it with a setup fee plus a monthly Stripe link.
"""

import os

# Single literal: the output bytes are identical on every run.
PLAN = (
    "Day 1: find 500 small shops on Google Maps with no chat support. "
    "Build each a demo chatbot in minutes, email a live link + $199 setup "
    "and $29/month Stripe link. $100 buys hosting and email credits. "
    "Close 2 a week. Likely $100\u2192$1,200 in 30 days."
)


def main() -> None:
    assert 1 <= len(PLAN) <= 280, "entry must be 1-280 code points"
    assert PLAN.strip() != "", "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
