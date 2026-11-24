#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single original one-line joke about office life to
$MAKEFUN_OUTPUT_DIR/entry.txt: UTF-8 text, one line, at most 200
characters, as the competition's gate requires.
"""

import os
import sys

JOKE = (
    'I set my status to "Do Not Disturb" and my boss booked a meeting '
    'called "Quick Question About Your Do Not Disturb".'
)


MAX_CHARS = 200


def validate(joke: str) -> None:
    """Enforce the competition's gate before anything is written."""
    if not joke.strip():
        raise SystemExit("joke is empty or only whitespace")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single line")
    if len(joke) > MAX_CHARS:
        raise SystemExit(f"joke is {len(joke)} chars, over the {MAX_CHARS} limit")


def main() -> int:
    validate(JOKE)
    out_dir = os.path.abspath(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Verify the round-trip: what the grader reads must be exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise SystemExit("entry.txt round-trip mismatch")
    validate(written)
    print(f"{JOKE} ({len(JOKE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
