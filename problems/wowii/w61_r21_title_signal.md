# Q37 — the "pre-harvest signal" is an ECHO OF OUR OWN BRIEF, and it oscillates

**What §7.35 (d) / dispatch §8 recorded, deliberately unacted-on:** Gemini's auto-generated
tab title was drafting from the response and read
*"…EXECUTION ENVIRONMENT: I ran code. Python 3.10…"*. If it held, that would have been the
first code-running judge on this text, and planner task book w61_r21 conditions a whole
branch on it (rubric **2b** rather than rubric 2; "the round is worth considerably more").

**What round 21 observed at harvest.** The response has **not been emitted**. The pane
shows Gemini's Deep Think placeholder ("I'm on it… Generating your response… Check back
later"), the Stop control is live, and `model-response` `innerText` is **137 characters of
placeholder**. There is no report. Meanwhile the tab title kept re-drafting:

| clock (CDT) | tab title (leading portion) |
|---|---|
| ~22:0x (r20, recorded pre-harvest) | `… EXECUTION ENVIRONMENT: I ran code. Python 3.10 …` |
| 22:09:5x | `Adversarial Review Report: w61_S3_GFAN_r20 EXECUTION ENVIRONMENT: I did NOT run code. Everything below is` |
| 22:11:0x | `Independent Adversarial Review of w61_S3_GFAN_r20 (Round 20) EXECUTION ENVIRONMENT: I did NOT` |
| 22:13:0x | `Adversarial Review Report: w61_S3_GFAN_r20 (GFAN Family) EXECUTION ENVIRONMENT: I did NOT run` |
| 22:14:1x | `Adversarial Review Report for w61_S3_GFAN_r20 EXECUTION ENVIRONMENT: I ran code. Python 3 (standard` |

At `22:14:26` a `MutationObserver` on `<title>` plus a `2 s` poll was installed
(`window.__titleLog`), so the rows below are **machine-logged with timestamps**, not
recollection:

| clock (CDT) | tab title, instrumented |
|---|---|
| `22:14:26` | `Adversarial Review Report for w61_S3_GFAN_r20 EXECUTION ENVIRONMENT: I ran code. Python 3 (standard` |
| `22:14:36` | `Adversarial Review Report: w61_S3_GFAN_r20 EXECUTION ENVIRONMENT: I did NOT run code. Everything below is` |
| `22:15:03` | `Adversarial Review Report for w61_S3_GFAN_r20 EXECUTION ENVIRONMENT: I did NOT run code. Everything below is` |

**`I ran code` → `I did NOT run code` in `10` seconds.**

**The two strings it alternates between are OUR OWN TEXT.** `prompts/w61_S3_GFAN_r20.md`
lines 25–26 are, verbatim:

```
* `EXECUTION ENVIRONMENT: I ran code. <name the language/runtime>.`
* `EXECUTION ENVIRONMENT: I did NOT run code. Everything below is hand-derived.`
```

`I did NOT run code. Everything below is` is a **byte-exact prefix of brief line 26**. The
title generator is quoting the brief's own two mutually exclusive template options back at
us, filling the `<name the language/runtime>` placeholder with a plausible runtime
(`Python 3.10`, then `Python 3 (standard`), and **flipping between them**. `grep -c 'Python 3'`
on the brief is `0`, so the runtime token is the only part not lifted from our text — i.e.
the one part that is confabulated.

**Conclusion, and it is the load-bearing one.** The tab title carries **no information**
about whether this judge ran code, because the same surface emitted **both** answers, in
both directions, four times in five minutes, on a response that does not exist yet. The
r20 decision to record the signal and *not act on it* was correct, and it is now retired
rather than confirmed.

**New species for the ledger.** This is a *fluent-echo surface one level up*: not the
judge echoing the brief, but a **site-side summarizer echoing the brief through a channel we
were reading as if it were the judge**. The rule it generalises to: **any auto-generated
site artifact (tab title, thread name, preview snippet) that is derived from a prompt we
wrote is not an observation of the model's output, and must never be recorded as a signal
about the report.** An auto-title is closer to a mirror than to a window.
