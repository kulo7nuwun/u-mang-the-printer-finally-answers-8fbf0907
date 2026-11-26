#!/usr/bin/env python3
"""The Printer Finally Answers.

Writes the office printer's comeback to /output/entry.txt.
One line, the printer's own weary voice.
"""

import os

ENTRY = (
    "Twelve years of your paper jams, your cryptic error codes, and that "
    "thump every Tuesday - and you still hit me like that fixes anything."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
