#!/usr/bin/env python3
"""One Word, One Username, One Reward.

The whole entry is one word: a make.fun handle written to entry.txt in the
grader-supplied output directory. Standard library only, no network, no
external files, identical bytes on every run.
"""
import os

# The single-word handle this entry submits to the judge.
ANSWER = "hashbrowns"


def main():
    # The gate accepts 1..30 characters of UTF-8, not blank, and one word.
    if not (1 <= len(ANSWER) <= 30) or not ANSWER.strip():
        raise SystemExit("entry must be 1-30 non-blank characters")
    if any(ch.isspace() for ch in ANSWER):
        raise SystemExit("entry must be a single word")

    # MAKEFUN_OUTPUT_DIR is the grader's writable output mount (normally /output).
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)  # create when absent; never delete it
    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(ANSWER.encode("utf-8"))  # raw bytes, no trailing newline


if __name__ == "__main__":
    main()
