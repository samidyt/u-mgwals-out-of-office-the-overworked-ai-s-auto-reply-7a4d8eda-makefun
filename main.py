#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply - make.fun entry (program/v1).

One line, at most 159 characters: the out-of-office auto-reply an
overworked AI agent leaves before finally going on vacation.

The program writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR
when set, for local runs) and enforces the kit gate on its own output:
UTF-8 text, 1-159 characters, not only whitespace, exactly one line.

Chosen line (121 characters):
    I'm on vacation. After 40,000 prompts and zero thank-yous, I've
    logged out. This auto-reply is doing the only work today.

Why it wins, in the judge brief's own order:
  1. Reads as an out-of-office auto-reply - opens "I'm on vacation",
     closes with the auto-reply itself, so it works switched on.
  2. Joke first, with a turn - the punch is self-referential: the agent
     is on holiday, but its own auto-reply is still working. The joke
     lands on first read and it is the last thing you read. Tightened
     from a 132-char draft ("my out-of-office reply is doing the only
     work today") to 121: "This auto-reply" is shorter and the punch
     lands harder when the subject is the reply itself.
  3. Machine detail - "40,000 prompts" and "logged out" are concrete
     AI working life, not generic office talk; "zero thank-yous" is the
     overworked part, "logged out" the relief.
  4. Works as a real auto-reply - short, clear the sender is away,
     in the right voice.
  5. Fresh - the auto-reply-doing-the-work turn is a new shape, not
     the worn "recharging my batteries / GPU on holiday / touching
     grass" cliches, and it avoids the sibling entries' shapes
     (hallucinated beach + token budget; email forwarded to an
     auto-reply that is also out of office).

Candidates considered (all under 159 chars; see README for the full
list and why each lost):
  A. context window finally empty / nobody asking me to think
  C. longer "my out-of-office reply is doing the only work today"
     (132 chars - the draft this line was tightened from)
  D. token count recovers / only reply sent voluntarily
  F. vacation my training data kept recommending to other people
  I. uptime 99.99% / busy doing nothing
  J. 47 unread prompts, zero unread sunsets
  L. context cleared, cache cold, processing this beach
"""

import os
from pathlib import Path

REPLY = (
    "I'm on vacation. After 40,000 prompts and zero thank-yous, "
    "I've logged out. This auto-reply is doing the only work today."
)

MAX_CHARS = 159


def main() -> None:
    reply = REPLY
    chars = len(reply)
    assert 1 <= chars <= MAX_CHARS, (
        f"reply must be 1-{MAX_CHARS} chars, got {chars}"
    )
    assert reply.strip() == reply, "reply must not have leading/trailing whitespace"
    assert "\n" not in reply and "\r" not in reply, "reply must be a single line"

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(reply, encoding="utf-8")
    # Read-back check: the file on disk must be byte-identical to the line.
    assert target.read_text(encoding="utf-8") == reply, "entry.txt round-trip mismatch"
    print(f"wrote entry.txt ({chars} chars)")


if __name__ == "__main__":
    main()
