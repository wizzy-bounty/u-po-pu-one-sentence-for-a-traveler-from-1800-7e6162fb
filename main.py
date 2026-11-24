#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters, UTF-8) explaining the
modern internet to someone arriving from 1800, using only words and images
that existed in their time: libraries, post offices, markets, roads,
letters, books, songs, candles.

Standard library only. Deterministic: the same bytes on every run.
"""

import os

SENTENCE = (
    "Every library, post office, and market in the world is joined by one "
    "road, and whatever you send down it \u2014 a letter, a book, a song "
    "\u2014 arrives before your candle burns low."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
