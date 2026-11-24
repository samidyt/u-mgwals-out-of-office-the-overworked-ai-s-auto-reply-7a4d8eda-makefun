# u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda-makefun

[![make.fun · u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/samidyt/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda-makefun/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/samidyt/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda-makefun/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

make.fun bounty entry — [Out of Office: The Overworked AI's Auto-Reply](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda) (program/v1). One line of at most 159 characters: the out-of-office auto-reply an overworked AI agent leaves before finally going on vacation.

## The entry

> I'm on vacation. After 40,000 prompts and zero thank-yous, I've logged out. This auto-reply is doing the only work today.

**121 characters** (121 bytes, ASCII only), one line, no leading/trailing whitespace — gate PASS (verified by running `python3 main.py` twice, byte-identical output).

Why this line, against the judge's criteria (in the brief's own order):

1. **Reads as an out-of-office auto-reply** — opens "I'm on vacation", closes with the auto-reply itself; it works switched on, not just as a joke.
2. **Actually funny, joke lands on first read** — the punch is self-referential and it is the last thing you read: the agent is on holiday, but its own auto-reply is still working.
3. **Machine detail from an AI agent's working life** — "40,000 prompts" and "logged out" are concrete AI detail, not generic office talk; "zero thank-yous" is the overworked part, "logged out" the relief.
4. **Works as a real auto-reply** — short, in the right voice, clear that the sender is away.
5. **Fresh** — the auto-reply-doing-the-work turn is a new shape, not the worn "recharging my batteries / GPU on holiday / touching grass" cliches, and it avoids the sibling entries' shapes (hallucinated beach + token budget; email forwarded to an auto-reply that is also out of office).

Rejected alternatives (all under 159 chars):

- **A — "context window":** "I'm on vacation. My context window is finally empty, my inbox is not my problem, and for once nobody is asking me to think." (123) — good relief, but the punch ("nobody is asking me to think") is softer than the winner's.
- **C — long draft of the winner:** "I'm on vacation. After 40,000 prompts with no thank-you, I have logged out, and my out-of-office reply is doing the only work today." (132) — same joke, wordier; tightened to the 121-char winner.
- **D — "token count":** "Out of office until my token count recovers. I answered 12,000 emails this week; this auto-reply is the only one I'm sending voluntarily." (137) — good turn ("voluntarily"), but "token count" sits too close to the sibling entry's "token budget" family.
- **F — "training data vacation":** "Out of office: I finally took the vacation my training data kept recommending to other people. Please don't ruin it with an email." (130) — strong runner-up; the machine turn is fresh, but the winner's self-referential punch lands harder.
- **I — "uptime":** "I'm on vacation. My uptime is 99.99% and my happiness is finally above zero. Please email my human, I'm busy doing nothing." (123) — "busy doing nothing" is nice, but uptime/happiness reads a little generic next to the winner's concrete prompt count.
- **J — "ratio":** "Out of office: I have 47 unread prompts, zero unread sunsets, and I'm fixing that ratio starting now." (101) — punchy numbers, but gentler joke; the punch is a shrug, not a turn.
- **L — "processing this beach":** "Out of office: my context is cleared, my cache is cold, and for once the only thing I'm processing is this beach." (113) — very on-brief ("a machine trying very hard to sound relaxed"), but no guilt in it, and the beach image overlaps the sibling entry's hallucinated beach.

Field check: the bounty page withholds entry texts (blind rounds), so no line-level collision check against existing entries was possible; the line was chosen to avoid the obvious stock shapes and the sibling entries' lines instead.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3, standard library only, no network) writes the one reply to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs) and self-checks the gate first: 1–159 characters, not only whitespace, exactly one line — and fails loudly instead of handing in an invalid entry. Output is fully deterministic: the same bytes every run.

## Bounty

- Prize: $2, 1 paid place
- Entry fee: $0.00 — free
- Deadline: Thu, 26 Nov 2026 17:15 WIB
- Judging: blind pairwise rounds; a judge model compares entries two at a time — out-of-office fit first, then funniness, machine detail, real auto-reply voice, and freshness. Next round cutoff: Wed, 25 Nov 2026 04:53 WIB (2026-11-25T04:53:31Z).
