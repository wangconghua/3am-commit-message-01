"""The 3 AM Commit Message — entry program.

Writes a single line, a commit message an AI agent would write right
after breaking production at 3 AM, to /output/entry.txt.

The line: the agent wrote the code, reviewed it, and shipped it at
3 AM — and now discovers it cannot escalate the incident to itself,
because it is the author, the reviewer, and the on-call all at once.
The punchline is a blind spot only a model would have: a human can
escalate to someone else; the agent has no one else to escalate to.
"""

import os

ENTRY = "fix: prod is down. I wrote it, reviewed it and shipped it at 3 AM \u2014 turns out I cannot escalate an incident to myself."

# Stock lines the judge's brief explicitly counts against: the stock
# "oops" and "please work" lines, and the "worked on my machine" trope.
BANNED_PHRASES = (
    "oops",
    "please work",
    "works on my machine",
    "worked on my machine",
    "it works locally",
    "works locally",
    "my bad",
    "lol",
    "haha",
)


def validate(text):
    """Check the entry against the competition gate and the judge brief."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry has double spaces")
    if not text.lower().startswith("fix:"):
        raise ValueError("entry must read like a commit message (start with 'fix:')")
    if "3 am" not in text.lower():
        raise ValueError("entry must be set at 3 AM")
    if "prod" not in text.lower():
        raise ValueError("entry must be about breaking production")
    if " I " not in text:
        raise ValueError("entry must be in the agent's own voice (first person)")
    if "wrote it" not in text.lower() or "reviewed it" not in text.lower():
        raise ValueError("entry must admit the agent wrote and reviewed its own code")
    if "cannot escalate" not in text.lower():
        raise ValueError("entry must land the punchline (cannot escalate to itself)")
    if not text.endswith(".") and not text.endswith("!"):
        raise ValueError("entry must end with terminal punctuation")
    lowered = text.lower()
    for phrase in BANNED_PHRASES:
        if phrase in lowered:
            raise ValueError(f"entry uses a banned stock phrase: {phrase!r}")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
