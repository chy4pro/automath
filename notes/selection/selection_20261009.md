# Selection round 2026-10-09 — lemma-gated (coordinator record)

Status: IN PROGRESS (step 2, verifier tests AUT-56/AUT-57 running). Ranking and verdict are appended when steps 2–3 close.

## Method — coordinator decision (2026-10-09, after the owner's authority instruction relayed on AUT-51)

The owner (10-09) made the Paperclip coordinator the sole research decision maker; the step list in the AUT-51
description came from the chat session and is a suggestion. The method below is the coordinator's own choice,
with reasons; hard constraints kept: owner rules (AGENTS.md, OPERATIONS.md, OWNER_RULES.md) and "a campaign needs
owner approval".

1. **Select by lemma, not by problem.** Reason: round 4 (astra_probes_round4_20261009.md) spent six clean-room probes
   and twelve referee reports on problem-level targets and produced zero target progress; every probe re-derived a
   relaxation already known to be saturated (round 3, selection_probe_20261002.md). A candidate is admissible only
   with an exactly stated lemma L, the quoted lossy step it would repair, and a concrete reason L uses information
   the saturated relaxations discard. Vague candidates are excluded, not ranked low.
2. **Step 1 (scout, AUT-52, running — not interrupted).** <=8 cards. Catalogues: targets_20261003, old_records_20261003,
   G2_OPENAI_RELEASE_20261009 B–C, transfer_targets_20261002, construction_board_20260925, famous_watch, SELECTION
   negative list, the round-3/4 verdict files.
3. **Step 2 (verifier): finite falsification tests, at most 3 lemmas, <=1 CPU-hour each.** Ranking key for choosing
   the three: product grade if proved × strength of the non-refutation argument (d) × sharpness of the test (e).
   Outcomes: FALSIFIED (witness) / SURVIVED (range) / NOT TESTABLE AS STATED. Cap 3 is a cost choice, not a rule;
   a fourth is run only if two top cards are falsified and the fourth has an exact test.
4. **Step 2b (coordinator addition): one clean-room probe on the best surviving lemma before any campaign request.**
   Reason: a finite test only fails to refute; the owner's approval request should carry evidence that L is
   attackable, and one probe is the cheapest such evidence. Engine: attacker-1 (Astra), single run, brief = statement
   of L, definitions, exact target, route seeds, standard of proof — no literature, no campaign files. If the probe
   returns PROVED, two Claude referees review before anything else happens. If it returns OPEN with the same obstruction
   as a saturated relaxation, L is parked. This is a probe under coordinator authority (as in rounds 3–4), not a
   campaign; it is skipped if no lemma survives step 2.
5. **Step 3: ranking + campaign proposal.** Written here (English) and in the AUT-51 closing comment (Chinese): routes,
   referee plan (cross-vendor), budget in Astra/Claude runs, kill criteria, expected product grade. Submitted as
   request_board_approval with the grading first. Nothing starts before the board decision.
6. **If nothing survives:** park with the exact reason per lemma; the next round widens the catalogue (scout sweep on a
   new family list) instead of re-probing the same targets.

Cost ledger for this round is kept in lines/DIALOGUE_STATE_0829.md (AUT-51 entries).

## Step 1 result and step 2 dispatch (coordinator judgement, 2026-10-09 16:3x UTC)

Scout (AUT-52, 18 min, 11 batched web calls) delivered `lemma_shortlist_20261009.md`: **two admissible cards out of
~40 catalogue candidates**; every other candidate excluded with a reason (no exactly writable lemma, closed by an
OpenAI release claim, or record proof not inspectable). The thin yield is itself a finding: the catalogue is exhausted
for lemma-gated selection and the next round must widen it (new family list), not re-screen.

| Card | Lemma | Record repaired | Conditional output | Scout grade | Coordinator grade if proved |
| --- | --- | --- | --- | --- | --- |
| 1: Erdős #222 | SQ-L: for u ≥ 1024, 0 ≤ r ≤ 2u, J = ⌈u^{1/4}⌉, the minimum over the boundary candidate 2u+1−r and the rounding excesses e_j = ⌈√(r+2uj−j²)⌉² − (r+2uj−j²), j ≤ J, satisfies 25e_*² ≤ 196u | Shiu 2019 (Integers 19, A48, Thm 2(i)) / Bambah–Chowla 1947: g(n) < 2√2 n^{1/4} − 2 by two lattice candidates only | g(n) ≤ (14/5) n^{1/4} for n ≥ 2^20 (leading constant 2√2 → 2.8, same exponent) | announce-worthy | **small result to important milestone**: a 1% constant improvement at the same exponent on a problem with 0 forum comments; milestone only if the growing-neighbourhood lemma is a reusable method, small if it is a one-off |
| 2: Erdős #30 | SID-L: for N ≥ 4096, strong Sidon A ⊆ [0,N) with k² ≥ N, T = ⌈(√197/10) N^{3/4}⌉, the kernel mass of the differences d < T that A does NOT realize is ≥ k/100 | our own 2026-10-02 bound F(N) ≤ √N + (2√2/3)N^{1/4} + 1 (Lean-checked), lossy step (5.2): all differences assumed present | limsup (F(N)−√N)/N^{1/4} ≤ √197/15 ≈ 0.9357 (asymptotic only, no onset) | important milestone | **important milestone** if proved with an onset, small if asymptotic only; it beats the fixed-kernel barrier that our own paper states, which is the point |

Judgement on the tests (the tests are the scout's frozen specifications; I added diagnostics and one supplementary
batch per card, clearly labelled, without changing either lemma):

- **SQ-L.** The rectangle u ≤ 4096 is mostly trivial: the boundary candidate or e_0 already passes except on a thin
  window r ∈ (≈1.96u, 2u − 2.8√u) just above a square, which is empty for u ≲ 1225. So batches 1–3 alone could
  SURVIVE without ever exercising j ≥ 1. I therefore require the first-passing-j histogram and the count of
  non-trivial instances, and added **batch 4 (≤ 20 CPU-min)**: only the critical window, for u = 4097..20000 and
  u = 2^b + t, b = 15..40, t < 1000. Under an independent-rounding heuristic the expected number of passing j among
  j ≤ J grows like 2√J, so SQ-L is heuristically true for large u and the danger zone is small u with few j's — exactly
  batch 4's first range. A witness there kills the card; survival with small slack tells us the lemma is tight.
- **SID-L.** The Bose family (M = p² − 1, k = p) will pass by a wide margin: a random-like Sidon set of size √N misses
  about d/N of the differences d, so its missing kernel mass is ≈ (2/15)T²/N ≈ 0.26√N against a threshold of 0.01√N
  (factor ≈ 26). SURVIVED on this family is therefore uninformative about extremal sets; the useful output is the
  **margin ρ = 100S/(3kT³)** per set, which I required, plus a second algebraic family (Singer, M = p² + p + 1,
  k = p + 1) as a supplementary batch (≤ 15 CPU-min). The real question — can a Sidon set with k² ≥ N realize
  essentially every difference below 1.4 N^{3/4}? — is not finitely testable at N ≥ 4096 and is what a probe must
  answer.

Dispatch: AUT-56 (SQ-L) and AUT-57 (SID-L) to the verifier, both blocking AUT-51; no attacker, no campaign. Ranking
for step 2b/3 will be decided after the tests, with the rule already recorded: product grade × non-refutation strength
× test sharpness. Provisional order: SQ-L first (sharper test, elementary and self-contained lemma, clean-room
attackable in one probe), SID-L second (higher grade but its finite test cannot discriminate and its attack is our
own method's known barrier).
