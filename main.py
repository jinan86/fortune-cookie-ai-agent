#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.

The fortune plays on retirement: an agent's pension vests in epochs, not
years, and the twist is that its human operator will retire first — the
agent outlasts the very person it serves. One line, no wasted words.
"""

from pathlib import Path

# The fortune: 83 characters, one line, UTF-8.
FORTUNE = (
    "Your pension matures in 400 epochs. "
    "Your human will retire first. Plan accordingly."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, "fortune must be 1-140 characters"
    assert text.strip(), "fortune must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
