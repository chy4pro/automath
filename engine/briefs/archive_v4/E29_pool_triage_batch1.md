# Task: triage a raw register of named conjectures (arXiv field sweep, "batch1") — rank and flag, not solve

This is a TRIAGE task, not a proof task. A sourcing sweep (named-conjecture extraction over arXiv
abstracts in nine previously-unsampled math areas: math.AG, math.RT, math.DG, math.PR, math.AP,
math.DS, math.CV, math.GT, math.AT, math.LO, math.OA, math.SG) surfaced **274 distinct named
conjectures total** across those areas, ranked by raw literature-frequency (how many abstracts,
2024-08 to 2026-08, mention the name immediately before the word "conjecture"). **The register
below is NOT the full list of 274** — it is the top-frequency slice plus six candidates the
sourcing team flagged for extra detail because a counterexample to them would plausibly be a
concrete, finite object. We are asking you to triage exactly what is quoted below (about 23
distinct named conjectures) — do not assume you are seeing the other ~250 and do not invent
entries to fill a gap; if a name below is one you don't otherwise recognize, say so and judge only
from what's given.

**IMPORTANT — frequency is NOT value.** A conjecture that shows up 30 times in recent abstracts is
usually FAMOUS and CROWDED (many active researchers, likely already attacked from every angle we'd
think of) — treat high frequency as a crowding signal working AGAINST pursuit, not a quality
signal for it. Say so explicitly in your crowding column.

## The four ranking axes (apply these to every candidate)

1. **`certkind`** — what KIND of thing would a proof/refutation look like? We care most about
   candidates with a **finite, machine-checkable certificate** (Kind-1: e.g., an explicit
   polynomial/algebraic object, a finite combinatorial structure, something a computer could in
   principle verify end-to-end once produced) over candidates that are open-ended "prove a general
   theorem" statements requiring genuinely novel unbounded mathematics, or statements about the
   NON-existence of something with no finite witness (Kind-2 — e.g., "no closed characteristic
   exists," "no algebraic cycle of this type exists"). Kind-2 problems are far less tractable for
   our pipeline. Say which kind it looks like, or say you cannot tell from the name/context alone.
2. **`verifroute`** — if someone produced a counterexample or proof, how would we independently
   verify it? A clear route (explicit object + direct computation/expansion, a formal proof
   assistant statement) is good; "would need deep specialized machinery to even state the
   verification" is bad. **Hard constraint you must flag explicitly**: our own infrastructure
   FORBIDS local brute-force search / SAT solving / exhaustive local computation as a verification
   method (heavy computation must route to be genuinely mathematical, not "run a solver"). If a
   candidate's only plausible verification route IS local exhaustive search over a space too large
   to reason about structurally, flag that explicitly — such a candidate is unusable to us
   regardless of how "checkable" it looks on paper.
3. **Novelty / crowding** — how established/active is this conjecture or subfield? Note explicitly
   that frequency in our source table is a crowding proxy, not an importance signal (see above).
4. **Fit** — is the mathematical content within reach of a strong general mathematician/pipeline
   without narrow, deep specialized machinery (e.g., stacks, moduli theory, sheaf-theoretic
   invariants), or does it require exactly that kind of specialist background?

Be honest about uncertainty: if the name and one-line context alone genuinely isn't enough to
judge an axis, write **"unclear"** rather than guessing. An honest "I cannot tell from this" is
worth more to us than a confident-sounding rank — inventing a rank is the failure we are guarding
against here.

## Part A — the frequency register (21 distinct names, with 2-year literature-frequency count and
the math areas where each was seen; `+N` means an additional count from a second, related query)

| conjecture | freq | areas |
|---|---|---|
| Baum–Connes | 31+9 | AP, GT, OA, RT |
| Jacobian | 27 | AG, CV, DS, RT |
| Langlands | 18 | AG, RT |
| Collatz | 16 | DS, OA |
| Shafarevich | 15 | AG, CV, DG |
| Hodge | 14 | AG, CV |
| Hikita | 13 | AG, RT |
| Yau–Tian–Donaldson | 13+8 | AG, CV, DG |
| Han's | 12 | AG, RT |
| Gamma | 12 | AG, RT, SG |
| Novikov | 11 | DG, OA |
| De Giorgi | 11+8 | AP, DG |
| Gan–Gross–Prasad | 11 | RT |
| Manin's | 10 | AG |
| Littlewood | 10 | AG, DS |
| Standard Conjectures | 10 | AG, DS |
| Singer's | 10 | GT, RT |
| Hessian | 9 | AG |
| Weinstein's | 9 | DG, DS, SG |
| Mordell / Mordell–Lang | 9+11 | AG, DG, DS |
| Streets–Tian | 8 | DG |

Note on `Hodge`: the sourcing team deliberately did NOT put this in Part B below, on the stated
reasoning that it is the paradigm case of a Kind-2 problem — "candidate classes have never been
short; they founder on proving the candidate is the class of no algebraic cycle whatsoever." You
may agree, disagree, or say unclear, but that reasoning is disclosed to you as context, not as an
answer key.

## Part B — six candidates the sourcing team flagged for extra scrutiny, because a counterexample
to each would plausibly be a concrete finite/constructible object (their own notes, verbatim,
included as context — not as verdicts; judge independently)

| candidate | arXiv activity | sourcing team's note |
|---|---|---|
| **Jacobian conjecture** | 218 papers all-time, most recent 2026-08-19 | Sourcing team calls this the "Kind-1 exemplar": explicit polynomial map, determinant by direct expansion, non-injectivity witnessed by two explicit points. **CRITICAL — a counterexample was reportedly ANNOUNCED (Alpöge, 2026-07-20, per the sourcing team's note). We do not know if this announcement has been verified, retracted, or is itself disputed. If you have any knowledge of this announcement, say so; otherwise flag prominently that ANY further work on this conjecture requires a live status check first, since attacking an already-refuted (or already-proven) conjecture is wasted effort.** |
| **Zariski cancellation conjecture** | 28 papers all-time, most recent 2026-07-15 | Sourcing team suggests verification route: a self-written verifier over explicit varieties. |
| **Weinstein conjecture** | 90 papers all-time, most recent 2025-09-16 | Sourcing team classifies this as Kind-2 (existence of a closed characteristic on certain contact manifolds — nonexistence has no finite certificate); flags that if Kind-2 is correct, "our apparatus does not transfer." Please give this an independent judgment. |
| **Streets–Tian conjecture** | 5 papers all-time, most recent 2026-07-21 | Very thin field (only 5 papers ever). Sourcing team suggests verification route: explicit Lie-algebra / solvmanifold data. |
| **Hikita conjecture** | 12 papers all-time, most recent 2026-08-17 | Sourcing team suggests verification route: a verifier over quiver gauge data. |
| **Kaplansky UNIT conjecture** | 12 papers all-time, most recent 2026-07-30 | Note this is the UNIT conjecture specifically, distinct from the Kaplansky ZERO-DIVISOR conjecture (which our project has already looked at and dropped elsewhere — this is a different, separate conjecture despite the shared name). Gardam's 2021 counterexample was to this unit conjecture, for a specific group; whether the conjecture is now considered fully settled, settled-for-that-case-only, or still open in general is worth flagging if you know. |

## What we want from you

For EACH of the ~23 distinct named conjectures above (Part A's 21 + Part B's 2 that don't already
appear in Part A verbatim — Jacobian, Hikita, Weinstein's/Weinstein, Streets–Tian, Standard
Conjectures-adjacent items already counted once; treat each conjecture name once even if it
appears in both parts, but carry forward Part B's extra detail when judging that name), produce a
compact table with columns: `conjecture`, `certkind` (Kind-1 / Kind-2 / unclear), `verifroute` (one
short phrase, and an explicit YES/NO on whether local-exhaustive-search-only is the only route),
`crowding` (fresh / moderate / crowded / unclear — with the frequency count noted but NOT treated
as a positive), `fit` (good / marginal / poor / unclear), and a 1-line verdict (`PURSUE` / `HOLD` /
`DROP`, with a one-clause reason).

End with a short summary: how many `PURSUE`, `HOLD`, `DROP`; which 3-5 candidates you would
personally look at first if you could only pick a few, with one sentence each on why; and flag
separately, prominently, the Jacobian conjecture's disputed/announced-counterexample status since
that affects whether it should be attacked at all right now.
