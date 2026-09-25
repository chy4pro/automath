# MISS-ANALYSIS — a famous conjecture fell on 2026-08-19 and we learned it from the user on 08-23

**Mandatory per methodology. Planner v4, 2026-08-23.** Subject: arXiv:2608.19301, cscK
Yau–Tian–Donaldson disproved, **AI-obtained, with a documented AI-usage appendix** — i.e. the single
most on-topic paper published in this project's field of view since it began. **We did not surface it.**

## 1. The cause is STRUCTURAL, not cadence — and I measured it rather than asserting it

| channel we had | what it asks | would it have caught this? |
|---|---|---|
| Google AI Mode (default scouting seat) | *"is candidate X still open?"* — per-candidate | **No.** Never queried; the target was not a candidate. |
| Deep Research (weekly deep-sweep seat) | broad freshness sweep, **weekly** | Possibly, on its next run — **days late by design**. |
| `gh` / formal-conjectures | competitor PR activity | **No.** Not an FC target. |
| arXiv API (`export.arxiv.org`) | **per-candidate**: "is there a preprint on X?" | **No — it was never pointed at a date.** |
| OEIS / Crossref / StackExchange | per-object lookups | No. |
| **pub-watch Monitor** (30 min, the only *scheduled* watch) | **4 of OUR PRs + 7 of OUR Zenodo DOIs** | **No. It watches only what WE published.** |

**Diagnosis, in one sentence: every intel channel we owned was PULL-BY-TARGET, and the only
scheduled watch was pointed at ourselves. We had no time-indexed channel and no channel facing the
field.** No cadence fixes that — you cannot catch a posting you never issue a query for.

**The freeze is a contributing cause and NOT a sufficient one.** The weekly freeze ran
08-19 06:0x → 08-22 00:0x and the paper landed 08-19 17:19 UTC, inside it. But the line reopened on
08-22 and ran a full scouting programme — a Gemini seat shoot-out, six target-pool gates — **and
still did not see it, because none of that programme asks what is new.** Blaming the freeze would
have let the real defect survive.

**Species: this is (S-9)/trap-4's sibling pointing outward.** Our rules already say *a zero hit is
not evidence of absence until you have excluded that you searched the wrong key.* Here we searched
the wrong **axis**: every key we own is an object, and the thing we needed was a **date**.

## 2. Second-order: the aggregate scouting record was better than it should have been
`SCOUTING.md`'s standing caveat records **A114831 missed 3/3 by every web engine** — a merged FC PR
we found only through the structured `gh` channel. That miss was correctly diagnosed as a
search-index blind spot. **The same file then concluded the structured channels were the fix — and
every structured channel we listed is per-candidate.** The lesson generalised one step and stopped
one step short.

## 3. The fix, built and TESTED against the real instance
`tools/arxiv_daily_watch.py` — zero quota, arXiv export API only, polite (one request per arm, 3 s
apart). Two arms over all 29 `math.*` categories: **resolution language** (disproof / disprove /
counterexample / "counterexample to" / "resolution of" / "proof of the") and **AI-disclosure
language** (generative AI / AI-assisted / large language model).

**Per RULING CZ the positive control is the real historical instance, not a synthetic probe.**
`--selftest` replays 2026-08-19 and requires the miss to come back:

```
resolution      20 of 225 math postings (8.9%)
ai-disclosure    4 of 225 math postings (1.8%)
target 2608.19301 recovered : YES
filter binds (0 < hits < N)  : YES
negative control (nonsense)  : returns 0, good        exit 0
```

**Cost: ~20 titles a day to skim, from 225 math postings.** Affordability was measured, not assumed.
The same day's digest also surfaced three other named-conjecture counterexamples
(Henning–Yeo, Bougard–Joret, a Schiffler-type band-graph counterexample) — **so the watch is not a
single-purpose tripwire; it is the field-facing intel channel this project never had.**

**Binding was proved before the result was believed.** My first version used `urlencode`, which
percent-mangled the parentheses and `+` separators; it returned `totalResults 44667` including
particle-physics papers **and still "found" the target** — a filter that returns everything always
contains what you are looking for. Caught by asking whether the category filter reduced the
population (1026 all-arXiv → 43 in math.AG/DG/CV). **That is this session's own rule — a check that
cannot fail has said nothing — arriving in the fix for the miss.**

## 4. What I am NOT claiming
- **Not that this watch would have caught every past miss.** A114831 was a merged GitHub PR; no
  arXiv query reaches it. **The two blind spots are different and both channels are needed.**
- **Not that 20/day is the right filter forever.** It is the measured cost on one day. The ledger
  records the daily count so the rate can be watched.
- **Not that the watch is running.** It is built, self-tested and committed. **Scheduling it is a
  change to standing operations and goes to the user** (per the intel file's own item 4: findings
  are reported, scope changes go through the normal gate).

## 5. Recommendation
Add a **daily** invocation to the existing planner Monitor alongside pub-watch — same zero-quota
posture, change-only reporting, appending to `notes/case_intel/arxiv_watch_ledger.md`.
**And the framing that matters more than the tool: pub-watch was named "pub-watch" because it
watched our publications. The project had a watch on its own output and none on its field.**
