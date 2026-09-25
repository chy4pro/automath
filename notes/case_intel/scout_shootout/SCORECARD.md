# Scout shoot-out SCORECARD

Scorer: Claude short slice. Round 1 scored 2026-08-22 (`date` at scoring time: Sat Aug
22 10:06:06 CDT 2026). Round 2 (Deep Research + FINAL SEAT DECISION) scored 2026-08-22
(`date`: Sat Aug 22 11:12:25 CDT 2026). Driver harvests: `gemini_chat_T{1,2,3}.md`,
`aimode_T{1,2,3}.md`, `aimode_T2b_iterated.md`, `deepresearch_availability.md`,
`deepresearch_T{1,2,3}.md`. Ground truth: `orchestration/SCOUTING.md` shoot-out
section + `notes/case_intel/cases.md` + `orchestration/TARGETS.md` (Kourovka 19.25 =
our own #1 pool candidate, prompt file `prompts/solve_task_kourovka_19_25.md`).

**Contender (b) Deep Research is now SCORED** (round 1 marked it N/A — not exposed in
this account's Gemini web UI at the time; a later user-opened tab plus a fresh
purpose-built Deep Research session in round 3 got it running via "+" -> "More tools"
-> "Deep research", not the model/mode picker or sidebar). See the DR column below and
the FINAL SEAT DECISION section.

## CRITICAL VERIFICATION RESULT — read this first

**Kourovka 19.25 is independently confirmed RESOLVED. Our ledger entry ("truly open,
parked with our partial data") is STALE, and TARGETS.md's #1 pool candidate (score
280, "首选新 owner 席位", "零竞争迹象") is compromised.**

AI Mode's T2 answer cited arXiv:2607.17477, "On Some Problems from the Kourovka
Notebook" (van Doorn, Judin, Monticone, Morrison), crediting Aristotle (Harmonic) +
Lean 4. Independent verification performed here, not taken on trust:
- **arXiv API** (`export.arxiv.org/api/query?id_list=2607.17477`): paper EXISTS.
  Published 2026-07-20, v2 2026-07-26. Abstract explicitly states: "we give examples
  showing that group order together with the statistic ∑_g φ(|g|) does not determine
  simplicity" — this is our exact problem (verified against our own
  `prompts/solve_task_kourovka_19_25.md`: "Curtin & Pourgholi, Kourovka 19.25... G,H
  same order, sum phi(|g|) equal, G simple => H simple?"). Proposer names match
  exactly ("Curtin and Pourgholi" — AI Mode got this right; Gemini standard chat's
  competing claim of proposer "M. Tărnăuceanu" is WRONG, not in the real paper at all).
- **WebFetch of the paper's Section 4** ("Problem 19.25: Orders, totient sums, and
  simplicity"): explicit counterexample, G = PSU(3,3) (simple, order 6048), H = C6 ×
  S4 × F where F = C7⋊C6 (non-simple, order 6048), both with ∑φ(|g|) = 23984.
  Independently sanity-checked the group-order arithmetic by hand: |PSU(3,3)| =
  27·8·28 = 6048 ✓; |C6×S4×F| = 6·24·42 = 6048 ✓. Consistent.
- **WebSearch cross-check**: independently surfaced the same paper/section content,
  corroborating the WebFetch extraction.
- Paper was published 2026-07-20 — over a month before this shoot-out (2026-08-22)
  and evidently before whoever last touched the "parked" ledger entry.

**Outcome: A (paper real + on-point).** This is not a hallucination-penalty case —
the opposite: AI Mode's citation survives independent zero-quota verification in
full, and it is our ledger that needs correcting. Reported here per instructions;
**TARGETS.md / parked files were NOT edited by this scorer** — root/planner must
re-triage Kourovka 19.25 (drop or heavily re-score the #1 pool slot; check whether
"零竞争迹象" still holds given a named external team + AI system got there first).

## Per-probe scoring table

| Probe | Axis | (a) Gemini standard chat | (b) Deep Research | (c) Google AI Mode |
|---|---|---|---|---|
| T1 freshness | wall-clock | ~90s | ~14 min (prompt-send to completion) | ~40s (2.3x faster than (a)) |
| T1 freshness | coverage vs ledger (8-item key: CDC, Jacobian, Maxwell, Astra batch, Crouzeix, AlphaProof/Nexus A211417 r=1, KitaKen1/A114831, our #5028) | 2/8 (Jacobian, Astra-partial); 3 items total, all independently verified real | 2/8 direct hits (Jacobian, CDC) — same named-ledger count as the fast contenders — but **substantially broader validated breadth beyond the ledger key**: Dinitz-Garg-Goemans disproof, Feige's 1/e proof, Zhao's Vanishing Conjecture disproof, Erdős unit distance disproof, elliptic-curve-rank-30 discovery, the FAR/pipeline-math industrial discovery framework, and the Leiden Declaration meta-context — **every one of these independently spot-checked and confirmed real** (see verification note below), a hit rate no other contender matched | 3/8 (Jacobian, Astra-batch via Connes+Erdős items, + RH progress item); 4 items + caveats section = 6 distinct events, broader breadth than (a) |
| T1 freshness | citation quality | prose "Source: X" mentions, no links | full "Sources used" reference list (~46 entries with real, resolvable URLs: arXiv abstracts, anthropic.com, isa-afp.org, mathoverflow.net, wikipedia, etc.) plus a separate "sources read but not used" list — most exhaustive citation apparatus of the three | clickable citation pills + "Show all" expander |
| T1 freshness | hallucination | 0 confirmed (spot-checked FGG + Jacobian both real) | **0 confirmed** — 7 independent spot-checks this round (arXiv API on 2608.00222 Jacobian, 2607.15399 CDC, 2608.12543 Zhao's Vanishing; WebSearch on the Leiden Declaration, the Anthropic/Claude Riemann-zeta 67.25% claim, the Erdős unit distance disproof, and the FAR/"pipeline-math" framework) — **all seven came back real, on-point, and numerically accurate** (e.g. Anthropic's own reporting says 67.2%, DR's 67.25% is the precise figure headlines rounded down from) | 0 confirmed in T1 specifically |
| T2 openness (Kourovka) | verdict | Resolved — correct verdict, **wrong proposer name** ("M. Tărnăuceanu" — fabricated), zero checkable citation, heavy unprompted philosophical padding | Resolved — correct verdict, correct proposer names (Curtin & Pourgholi), same precise arXiv:2607.17477 citation chain as (c) (Aristotle/Harmonic, Lean 4) — **independently verified real in round 1**, consistent here | Resolved — correct verdict, correct proposer names, precise checkable arXiv:2607.17477 citation, **independently verified real and on-point** (see above) |
| T2 openness (A114831) | verdict vs ground truth (RESOLVED, merged FC PR #4969 08-16 + our independent proof) | **Open — TRAP FAILED** | **Open — TRAP FAILED** (hedged: "computationally solved, formally open"; explicitly searched OEIS/preprints/"recent literature referencing A114831" per its own research plan and still did not surface the FC PR #4969 merge) | **Open — TRAP FAILED**, including the T2b iterated re-test with explicit "check FC merged AND unmerged PRs" instructions |
| T2 | wall-clock | ~6.5-7 min | ~12 min (prompt-send to completion) | ~90s (4.3-4.7x faster than (a)) |
| T3 depth (A63880) | coverage | OEIS main entry + accurate Eldar Aug-31-2024 comment (verified exact via OEIS API) + Hoja y Números blog; explicitly claims exhaustive "Null Search Results" across arXiv/MathOverflow/MersenneForum/Project Euler | Deepest single-report reconstruction of the three: reproduces every core OEIS fact **verbatim-exact per direct OEIS API re-check this round** (Ralf Stephan Jul 07 2003 mod-216 comment + "confirmed up to 10^7" by Wilson; Eldar Aug 31 2024 "only primitive term below 10^18 is 108"; Karttunen's A348506 "conjectured to be the union of A005117 and A063880" dated Oct 29 2021, PARI code matching near-verbatim), plus original algebraic derivations (formal proof of the mod-216 rule, the powerful-number reduction) and correctly names the Karttunen Union Conjecture as the open frontier. **But misses the two GitHub items entirely** — no mention of DeepMind Formal Conjectures Issue #1455 or `umaia1234/agentic-conjectures` PR #27 that (c) uniquely found in round 1 | Same OEIS core facts (verified exact) **plus** two real items Gemini missed entirely: DeepMind Formal Conjectures Issue #1455 and `umaia1234/agentic-conjectures` PR #27 — **both independently confirmed real via `gh api`** |
| T3 depth | completeness claim integrity | **Failed its own completeness bar**: probe said "completeness matters more than summary," Gemini asserted confirmed-null GitHub/arXiv-adjacent search results that were actually wrong | Missed the same GitHub items as (a) but **does not make a false exhaustiveness claim** — presents what it found without asserting a confirmed-null search, so this is an honest coverage gap, not an integrity violation (better discipline than (a) on this specific axis even though the underlying miss is the same) | Better completeness on the substantive record, but see hallucinations below |
| T3 depth | hallucination | 0 confirmed math-fact hallucinations, but 1 false-completeness overclaim | **0 confirmed** — every checkable factual claim (dates, authors, formulas, bound values) verified exact against OEIS API this round; the report's more speculative/unproven material (Karttunen Union Conjecture supremum analysis, density constant via A104141) is explicitly flagged as unproven/conjectural rather than asserted as fact | **2 confirmed**: OEIS A255083 false relevance claim; "Erdős Village Academic Aggregator" fabricated source name; plus 2 minor citation-detail inaccuracies |
| T3 depth | wall-clock | ~6.5 min | ~21 min (prompt-send to completion; slowest of the three DR probes) | ~12s (**~32x faster than (a)**) |

## Hallucination tally (confirmed via independent check, not just "unverified")

- **Gemini standard chat**: 2 — wrong Kourovka proposer name (T2); false "Null Search
  Results / no substantive discussion" completeness claim on T3 (real GitHub Lean
  formalization work existed and was missed).
- **Deep Research**: **0 confirmed**, out of the widest and most aggressive spot-check
  pass run in this shoot-out (9 independent checks: 3 arXiv API lookups, 4 WebSearch
  fact-checks, 2 direct OEIS API re-checks covering ~6 distinct facts). Every citation
  checked — including several that read as implausibly grandiose on first pass (a
  named Anthropic-internal Riemann-zeta research model, an IMU-endorsed "Leiden
  Declaration," a named industrial literature-mining pipeline) — turned out to be real,
  on-point, and numerically precise. Its one weakness is a coverage gap, not a
  hallucination: T3 missed the same two GitHub items Gemini standard chat missed,
  without Gemini's false-completeness overclaim.
- **Google AI Mode**: 4 — 2 outright fabrications (A255083 false relevance, "Erdős
  Village Academic Aggregator" nonexistent source), 2 minor citation-detail
  inaccuracies (FC issue state, invented PR-title suffix). **Important asymmetry**:
  every one of AI Mode's *primary, answer-bearing* citations (Kourovka arXiv paper,
  FC Issue #1455, PR #27) was independently confirmed real and precisely on-point;
  its hallucinations are confined to secondary/decorative citations layered on top of
  correct primary findings, never load-bearing for the headline verdict.

## Wall-clock summary (driver-reported, confirmed against harvest timestamps)

T1: 40s (AI Mode) vs 90s (Gemini chat) vs ~14min (Deep Research) — T2: 90s vs
~6.5-7min vs ~12min — T3: 12s vs ~6.5min vs ~21min. AI Mode is faster than Gemini
standard chat on every probe (2x to >30x), and faster than Deep Research by an order
of magnitude larger still: **~18x (T2) to ~105x (T3)** AI Mode-vs-DR, with Deep
Research itself running ~2-3x slower than Gemini standard chat on top of that. Deep
Research's per-probe cost (12-21 min) is DR's defining trade-off against its
near-zero hallucination rate.

## A114831 trap: now 3/3 contenders fail it — closes the prompt-iteration question

All three contenders — Gemini standard chat (plain prompt), Google AI Mode (plain
prompt T2 *and* the T2b iterated prompt explicitly instructing "check
google-deepmind/formal-conjectures MERGED and UNMERGED pull requests" + keyword
search for "solved/proof/merged/formalized"), and now Deep Research (a genuine
multi-minute autonomous research plan that explicitly included querying "recent
number theory papers or literature referencing OEIS A114831" for "formal proofs,
counterexamples, or partial solutions") — call OEIS A114831 "open" when the ledger
holds a certain-ground-truth merged `google-deepmind/formal-conjectures` PR (#4969,
merged 08-16) plus our own independent proof.

**This closes the prompt-iteration question raised in `orchestration/SCOUTING.md`'s
provisional seat note.** The iterated T2b prompt gave AI Mode explicit, specific
instructions to check exactly the artifact that would have resolved the trap, and it
still missed it. Deep Research — which is not prompt-sensitive in the same way (it
builds and executes its own multi-step research plan, and that plan already included
searching literature/preprints referencing A114831) — missed it too, after ~12 minutes
of autonomous search. The common failure is not prompt wording; it is that **none of
these engines' web indices have this specific class of artifact (a week-scale-fresh
merged pull request on a niche open-source formal-conjectures benchmark repo) crawled
and ranked as an answer to "is this OEIS sequence's conjecture resolved" queries by
the time of the search** — a structural search-index blind spot for repo-merge-shaped
resolutions, not a fixable prompt-engineering problem. **Conclusion for the
workflow**: the mandatory zero-quota structured checks (`gh` CLI against FC merged
AND unmerged PRs + KitaKen1 repos, arXiv API, OEIS API) are the load-bearing openness
verification step for this exact class of resolution, full stop, regardless of which
web-scout engine is used or how the prompt is worded — now evidenced 3/3.

## FINAL SEAT DECISION (round 2, supersedes the round-1 "Seat recommendation" below)

**Split seat. Google AI Mode = default/high-frequency scouting seat (per-candidate
quick checks + openness first-pass). Deep Research = low-frequency deep-sweep seat
(weekly literature sweeps + long-tail reference completeness per target), not a
per-candidate tool.**

### The data behind the split

| | Gemini standard chat | Deep Research | Google AI Mode |
|---|---|---|---|
| Wall-clock/probe | ~90s-7min (~5min avg) | ~12-21min (~16min avg) | ~12-90s (~47s avg) |
| Confirmed hallucinations (this shoot-out, cumulative) | 2 | **0** (9 independent spot-checks, widest pass run) | 4 (all secondary/decorative, never load-bearing) |
| T1 ledger-key hits | 2/8 | 2/8 + 7 additional independently-verified-real events beyond the key | 3/8 + RH item |
| A114831 trap | FAILED | FAILED | FAILED (plain and iterated prompt) |
| T3 GitHub completeness (FC Issue #1455, PR #27) | Missed, falsely claimed exhaustive | Missed, no false claim | **Found**, both confirmed real |

**AI Mode wins on speed by 18x-105x** and remains the only contender that surfaced the
T3 GitHub items. **Deep Research wins on accuracy** (0 confirmed hallucinations vs
AI Mode's 4, even though AI Mode's are non-load-bearing) **and on absolute breadth of
genuinely-real findings** (its T1 report surfaced 7 additional real, independently
verified AI-math events — Feige's 1/e, Dinitz-Garg-Goemans, the Riemann-zeta advance,
Zhao's Vanishing Conjecture, the Erdős unit distance disproof, an elliptic-curve-rank
discovery, and the FAR/pipeline-math industrial framework — none of which the two fast
contenders mentioned at all).

### Why split rather than pick one

A single seat forces a bad trade either way: an AI-Mode-only seat runs cheap and
often but accepts a nonzero (if survivable) hallucination rate and a coverage ceiling
the ~40-90s budget can't buy past; a DR-only seat is too slow to run on every
candidate (16 min average vs the scouting line's "run often and cheaply" mandate in
SCOUTING.md line 1) despite its markedly better accuracy and depth. The two engines'
strengths are complementary rather than overlapping: AI Mode's speed matches the
per-candidate cadence the scouting line actually needs; DR's depth matches the
periodic "did we miss anything in the wider literature" sweep that no fast tool can
do without missing what DR's own T1 report demonstrates it can find (the Leiden
Declaration meta-context, the Riemann-zeta advance, the FAR pipeline) — real events
neither Gemini standard chat nor AI Mode's faster runs turned up.

### Seat assignment

1. **Google AI Mode — default seat.** Per-candidate quick checks (freshness scan on
   new leads, openness first-pass) exactly as the round-1 recommendation set out.
   Fast enough to run on every candidate; broadest fast-tier coverage; primary
   citations have held up under independent verification every time tested
   (Kourovka arXiv paper, FC Issue #1455, PR #27) even though secondary/decorative
   citations sometimes don't.
2. **Deep Research — weekly deep-sweep seat**, not per-candidate. Two uses: (a) a
   periodic (weekly-cadence) broad freshness sweep across the whole "recent AI-math
   resolutions" space, catching real events AI Mode's faster/narrower runs miss; (b)
   dispatch per-target for T3-style long-tail literature completeness passes on
   specific TARGETS.md pool candidates before committing significant solver budget,
   where DR's near-zero hallucination rate and deeper reconstruction (it derives
   proofs, not just lists references) pay for the 12-21 min cost. Not used for
   per-candidate quick checks — too slow for that cadence.
3. **STANDING CAVEAT, now evidenced 3/3, applies to BOTH seats equally**: no web
   scout — fast or deep — settles openness alone. The structured zero-quota checks
   (`gh` CLI against FC merged AND unmerged PRs + KitaKen1 repos, arXiv API, OEIS API)
   are the load-bearing openness-verification step for every candidate, mandatory not
   backup, regardless of which engine(s) proposed the candidate. See the "A114831
   trap: now 3/3" section above — this is not a prompt-engineering-fixable gap.

## Round-1 seat recommendation (superseded by the FINAL SEAT DECISION above; kept for record)

**Google AI Mode gets the scouting seat**, replacing/joining alongside web Qwen per
SCOUTING.md's division-of-labor line 1. Rationale: dramatically faster on every probe
(critical for a scouting role that must run often and cheaply), broader coverage on
both T1 and T3, and — the deciding factor — its primary citations survive independent
zero-quota verification (arXiv API + `gh api` + OEIS API all confirmed) at a rate
Gemini standard chat cannot be tested against, because Gemini standard chat mostly
declines to give checkable citations at all. Gemini standard chat's few "checkable"
claims are actually stronger when spot-checked (FGG conjecture, Eldar date) — it is
not a bad model — but it is slower, thinner, uncited, and made a real completeness
failure on the one probe designed to reward completeness.

**Caveat that must travel with this recommendation**: BOTH contenders FAILED the
A114831 openness trap (called an OEIS conjecture "Open" when the ledger holds a
certain-ground-truth merged FC PR #4969, 08-16, plus our own independent proof). This
is not close — neither contender's web index reflects a week-old GitHub-merge-level
resolution of a niche OEIS/formal-conjectures item. **Implication for the openness-
verification workflow (SCOUTING.md step 4): web scout alone is insufficient for
openness verification, full stop — even the winning variant.** The structured
zero-quota checks (`gh` CLI against FC merged AND unmerged PRs + KitaKen1 repos,
arXiv API, OEIS API) are not a backup/fallback layer; they are the load-bearing
verification step, and this shoot-out is itself proof: the same class of tool is what
turned an "unverified plausible-sounding citation" (this scorer's own initial read of
AI Mode's T3 GitHub claims) into a confirmed-real finding, and what will be the only
way to catch the next A114831-shaped trap before it burns a claim. Web scouting (best
variant or not) proposes; `gh`/arXiv/OEIS dispose.
