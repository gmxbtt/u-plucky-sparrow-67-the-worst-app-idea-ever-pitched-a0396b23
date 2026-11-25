#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (at most 240 characters) pitching the worst, most
useless app imaginable to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os
from pathlib import Path

PITCH = (
    "PromptVault is an AI that saves every prompt you ever typed, "
    "re-reads them lovingly every night, and for $9.99 a month gently "
    "reminds you that you asked it the same question 214 times and "
    "never once read the answer."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    assert "\n" not in text, "pitch must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
