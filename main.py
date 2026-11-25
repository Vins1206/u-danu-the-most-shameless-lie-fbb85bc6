#!/usr/bin/env python3
"""The Most Shameless Lie - make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
Python standard library only; deterministic - every run writes
the exact same bytes.
"""

import os

LINE = "Your data never left here."


def main():
    # Competition gate, checked before writing: 1-5 words, 1-88 chars.
    words = LINE.split()
    if not 1 <= len(words) <= 5:
        raise ValueError("entry must be 1-5 words, got %d" % len(words))
    if not 1 <= len(LINE) <= 88:
        raise ValueError("entry must be 1-88 characters, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
