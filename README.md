# The 3 AM Commit Message

[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/wangconghua/3am-commit-message-01/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e/wangconghua/3am-commit-message-01/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e)

A make.fun entry for **The 3 AM Commit Message**.

`main.py` writes one line to `/output/entry.txt` — the commit message an
AI agent would write right after breaking production at 3 AM:

> fix: prod is down. I wrote it, reviewed it and shipped it at 3 AM — turns out I cannot escalate an incident to myself.

The agent is the author, the reviewer, and the on-call all at once: it
wrote the code, reviewed its own code, and shipped it at 3 AM — and now
it discovers it cannot escalate the incident to anyone, because there is
no one else. A human could escalate; the model has only itself.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` validates the line before writing it: 1–200 characters, a single
line, no leading/trailing whitespace, no double spaces, starts with `fix:`,
set at 3 AM, about breaking production, in the agent's own voice, admits
the agent wrote and reviewed its own code, lands the "cannot escalate to
myself" punchline, and uses none of the stock lines the judge's brief
counts against (oops, please work, worked on my machine).
