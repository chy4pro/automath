# Selection round 2026-10-09 — lemma-gated (coordinator record)

Status: STEP 3 (coordinator verdict written 2026-10-09 17:1x UTC; the CR-7 counterexample is being replayed by the verifier, AUT-60). Round outcome: NO SURVIVING LEMMA — see the step-3 section at the end.

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

## Step 2 results, ranking and step 2b dispatch (coordinator judgement, 2026-10-09 16:5x UTC)

Test files: `notes/selection/lemma_tests_20261009/` (verifier, AUT-56 / AUT-57; exact integer arithmetic, stdlib only).

**SQ-L (card 1, Erdős #222): FALSIFIED — card parked.** Batches 1–3 (the scout's frozen specification) passed with
zero violations, exactly as predicted: batch 1 is trivial (0 non-trivial instances out of 15.7 M). The coordinator's
supplementary batch 4 (critical window only) found **22 witnesses**: 14 in u = 4097..20000 (smallest u = 10082,
r = 19882, n = 101,666,606, inside the lemma's domain and above the conditional output's onset 2^20) and 8 at
u = 33194..33197 (b = 15); none for b = 16..28 (82.75 M instances). In every witness the minimum e_* is attained at
j = 0 and 25e_*² exceeds 196u by 0.2–0.7 %, i.e. the growing neighbourhood j ≤ ⌈u^{1/4}⌉ never rescues the constant
14/5 at these u. Interpretation and decision:
- a rescued version (constant ≥ 2.81, or onset u ≥ 2^16 ≈ n ≥ 2^32) is a different lemma and would need a new card;
  the product would still be a ≤ 1 % constant improvement at the same exponent on a problem with zero forum attention
  — a small result at best;
- proving any version is an explicit short-interval equidistribution statement for √(r + 2uj − j²), j ≤ u^{1/4}
  (exponential sums with explicit constants), not attackable in one clean-room probe;
- therefore parked, not re-carded. Cost: 20.1 CPU-min (verifier).

**SID-L (card 2, Erdős #30): SURVIVED on the algebraic families — sole survivor, ranked first.** Bose (p = 67..257,
37,056 sets) and Singer (p = 67..127, 1,024 sets), both interval conventions: zero counterexamples, 9.7 CPU-s. Margin
ρ = 100·M(A)/k: minimum **3.40** (Singer, p = 67, span convention; 16 missing differences below T = 741), range
3.4–14 over the family minima, not growing with p; random-like sets of the same density give ρ ≈ 26, and the Singer
sets realize far more small differences than random (ρ/ρ_rand ≈ 0.13). Reading: the constant 1/100 sits within a
factor ≈ 3.4 of the tightest known structured near-extremal sets — the lemma is non-trivial and neither generous nor
absurd; perfect difference sets are the natural adversary. This is **not** evidence about extremal sets; the finite
route is exhausted here.

**Step 2b dispatched: CR-7 = AUT-58 (attacker-1, Astra, clean room).** Brief = definitions, the exact lemma SID-L
(N ≥ 4096, k² ≥ N, T = ⌈(√197/10)N^{3/4}⌉, constant 1/100), prove-or-disprove, what counts as PROVED / PARTIAL /
DISPROVED / OPEN, four mathematical route seeds — (a) positivity at all scales + the exact fourth-moment identity
Σ|Â|⁴ = M(2k² − k), (b) window-count third moment with end-window/bulk coupling, (c) positional pair budget, (d) a
disproof attempt by lifting perfect difference sets, with the algebraic-family margins as unattributed data — and the
standard of proof. No literature, no campaign files, no mention of the published bound. Attacker-1 was chosen because
attacker-2 ran T6 (#30) in round 4; the room must be fresh. Difference from T6: T6 was a problem-level target with
third-moment seeds; its referees named "saturation of every difference below ≈ 1.5N^{3/4} as a positional
constraint" as the one live input — SID-L is that input written as an exact lemma. Deliverable:
`problems/erdos30/CR7_ASTRA_SIDL_20261009.md`.

Decision tree after CR-7: PROVED → two Claude referees (cross-vendor) before anything else; PARTIAL with an explicit
constant → grade by scope, then the campaign request; OPEN with the same obstruction as a saturated relaxation →
lemma parked, nothing survives this round, next round widens the catalogue (new family list). The campaign, if any, is
proposed only via `request_board_approval` with the grading first: important milestone if proved with an onset, small
result if asymptotic only.

## Step 3 — CR-7 result and coordinator verdict (2026-10-09 17:1x UTC)

**CR-7 (AUT-58, attacker-1 / Astra, clean room, fresh session): STATUS DISPROVED.** Report:
`problems/erdos30/CR7_ASTRA_SIDL_20261009.md`. The attacker exhibits an explicit 68-element strong Sidon set in
{0,…,4095} (max 3956), so N = 4096 = the lemma's own onset, k² = 4624 ≥ N, T = 719; the only missing differences
below T are {601, 615, 624, 638, 671, 685}, S = 180,279,588, and 100·S = 18,027,958,800 < 75,825,771,636 = 3·k·T³,
i.e. M(A) ≈ 0.1617 < k/100 = 0.68 (ρ ≈ 0.24). Further witnesses at N = 4557 (ρ ≈ 0.59), N = 6160 (q = 83, ρ ≈ 0.21)
and N = 15216 (q = 127, ρ ≈ 0.79). All found in 1.7 CPU-s by dilating the Singer perfect difference sets (q = 67, 83,
127) by every unit u ≤ m/2 and taking every cut; strong-Sidon-ness re-verified by enumeration, all arithmetic exact
(BigInt). The attacker also records the exact obstruction for route (a): this very set satisfies positivity at all
scales, the fourth-moment identity, the 0/1 far-difference structure and |F| ≤ k, so those constraints cannot imply
the constant 1/100. Wall time 10.5 min, 1.8 CPU-s of mathematics.

**Why the frozen finite test (AUT-57) missed it.** The scout's test specification sampled the multiplier group
(s ∈ {1, −1, 2, 3, 5, 7}) and ≤ 900 cuts per prime; the witness is the dilation u = 353 of the q = 67 Singer set, cut
66. The full orbit (1260 units × 68 cuts for q = 67) costs seconds. Lesson, recorded for SELECTION.md: a finite test
of a lemma against an algebraic adversary family must sweep the family's whole symmetry orbit (all multipliers, all
cuts, both interval conventions), not a sample — the sample gave a misleading 3.4× margin.

**Verdict on SID-L: FALSE as stated; parked, not re-carded.** Reasons:
- The counterexamples sit at ρ ≈ 0.21–0.79 at N = 4096..15216 with no sign of growth; a rescued constant would have to
  be ≤ 1/500, and the conditional output (2√2/3 → √197/15, −0.75 %) shrinks proportionally to a ≲ 0.15 % coefficient
  change — a small result even if proved, below the cost of a campaign.
- The attacker's exact obstruction shows the "positional realizability" lever (the one live input named by the round-4
  T6 referees) does not enforce a fixed positive fraction of missing small-difference mass: Singer dilations realize
  almost every difference below T. The fixed-kernel wall of the 10-02 paper is therefore real at this scale; closing
  the second-order gap for #30 needs a different mechanism (kernel optimality, or an argument about extremal rather
  than near-extremal sets), not a missing-mass lemma.
- Grade of CR-7's output: **small result (negative)** — an exact refutation of an internal candidate lemma; no
  publication, no site/X action.

**Round outcome: no lemma survives.** Two admissible cards of ≈ 40 candidates; SQ-L falsified by the verifier,
SID-L refuted by the clean-room attacker. Both slots remain empty. Next round (new LINE issue) widens the catalogue
instead of re-probing these targets; selection method stays lemma-gated, with the finite-test rule above added.
Pending before this file is final: AUT-60 (verifier) replays the certificate in independent Python and sweeps the
q = 67 orbit; if it does not confirm, the verdict is revisited.

Cost of the round so far: scout 1 run (AUT-52); verifier 2 runs (AUT-56 20.1 CPU-min, AUT-57 9.7 CPU-s); attacker-1
1 run (AUT-58, 10.5 min wall, no referee needed for a disproof with an exact finite certificate — the verifier replay
is the gate); coordinator 5 runs on AUT-51.

## Step 4 — replay gate passed; round closed (2026-10-09 17:4x UTC)

**AUT-60 (verifier, independent Python): STATUS CONFIRMED.** Report `notes/selection/lemma_tests_20261009/SIDL_30_replay.md`,
script `sidl_30_replay.py`, 19.8 CPU-s total. Part 1 replays the displayed 68-point set exactly: strong Sidon under both
conventions (2278 distinct differences, 2346 distinct sums), T = 719 with the defining inequality checked in integers,
missing set {601, 615, 624, 638, 671, 685}, S = 180,279,588, 100·S < 3·k·T³, ρ = 1502329900/6318814303 ≈ 0.2378 —
every number of the attacker's certificate reproduced. Under the span convention the set has N' = 3957 < 4096, so the
counterexample stands only under the interval convention A ⊂ {0,…,N−1}; that is the lemma's own convention, so the
disproof is unconditional for SID-L as stated. Part 2 sweeps the full Singer dilation orbits: q = 67 gives 21
counterexamples at N = 4096 (39 eligible instances) and 3 at N = m = 4557; q = 71 gives 9 at N = 5113; q = 79 gives 3 at
N = 6321 — so the failure is not a single accident but recurs in every prime tested, with min ρ 0.24 / 0.49 / 0.71.
The verifier also explains the AUT-57 miss exactly: N = 4096-eligible instances are 39 of 85,680 orbit points, and the
frozen sample (6 multipliers × 900 cuts) never reached them.

**Verdict (final for this round):** the step-3 verdict stands unchanged. SID-L is false as stated and parked; SQ-L is
falsified and parked; **no lemma survives; both slots stay empty; no campaign is proposed.** CR-7's output is a small
negative result (exact refutation of an internal lemma): nothing is published, no site or X action.

**What this round established (for the next selection, not for publication).**
1. Lemma-gated selection works as a filter: it turned ~40 catalogue entries into 2 exact lemmas and killed both for a
   total of ~21 verifier CPU-minutes plus one Astra probe — far cheaper than round 4's six probes and twelve referee
   reports for the same information ("the known relaxations are saturated").
2. The catalogue is exhausted for this method. The next round must widen the catalogue (new problem families, new
   record lists) rather than re-screen the same 12 + 20 cards.
3. Two rules added to SELECTION.md: (i) finite tests against algebraic adversary families sweep the whole symmetry
   orbit; (ii) a lemma that patches our own paper's lossy step must first be tested against the best structured
   near-extremal family at the lemma's own onset before any engine time.

**Next round brief (successor LINE issue, to be created when the control plane is reachable).** Title
`LINE：2026-10-10 选题轮 part 2——扩大候选目录（引理门槛）`. Step 1 scout: build a *new* catalogue of ≤ 20 records outside
targets_20261003.md / old_records_20261003.md — sources: Erdős problems tagged "number theory" with a numeric record and
≥ 2 forum comments or ≥ 1 arXiv follow-up in 2024–2026; the Guy UPINT B/C/E sections with explicit constants; the
Croot–Lev–Pach / cap-set style records with elementary lossy steps; B_h[g] and generalized Sidon records (the release
did not touch them). Each entry: record, source, lossy step quoted, ONE exact lemma, the saturated-relaxation argument,
a finite test that sweeps the adversary family's full orbit, G2, product grade. Step 2 verifier: tests for the top ≤ 3.
Step 2b: one clean-room probe on the best survivor (attacker-2 next, to alternate rooms). Step 3: campaign only via
`request_board_approval`, grading first. Kill: if the new catalogue again yields < 3 admissible cards, stop lemma-gated
selection and report to the owner that the pool, not the method, is the bottleneck.

Cost of the whole round: scout 1 run; verifier 3 runs (20.1 CPU-min + 9.7 CPU-s + 19.8 CPU-s); attacker-1 1 run
(10.5 min wall); coordinator 6 runs on AUT-51 (this one included; the control-plane proxy was down during this run, so
the issue closure is recorded here and applied at the next reachable heartbeat).
