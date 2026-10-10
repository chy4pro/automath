# Selection round 2026-10-10 (part 2 of the lemma-gated round) — coordinator record

Status: ROUND CLOSED 2026-10-09 18:2x UTC — NO SURVIVOR; rule 5 triggered twice; lemma-gated selection stopped, doctrine question to the owner (LINE issue AUT-62). Previously: STEP 2 DISPATCHED 18:0x. Predecessor: selection_20261009.md (round AUT-51,
no survivor). Rules: SELECTION.md "Lemma-gated selection rules (2026-10-09)".

## Owner instruction applied (2026-10-09 17:40Z, relayed on AUT-51)

Infrastructure repaired; the project runs at full speed again. Both Codex slots are to be kept busy with real work,
verifier/referees in parallel as needed; a surviving lemma goes to the probe and then to a campaign approval request;
no survivor means the catalogue is widened. Standing rules and approval gates unchanged. Recorded in OWNER_RULES.md.

## Step 1 result (scout, AUT-63) and coordinator judgement

The scout's run was interrupted by the server shutdown during the infrastructure repair (17:32Z) after both deliverables
had been written; the files start with DONE and are complete: lemma_catalogue_20261010.md (8 new records C1–C8) and
lemma_shortlist_20261010.md (ONE admissible card). Accepted as delivered; AUT-63 closed by the coordinator, files committed.

**Card B4-L (finite B4 sets, leading constant).** Record: β4 ≤ (4/c_low)^{1/4} (White 2023/24 transfer of Green 2001 eq. (12)
with the Rechnitzer 2026 autoconvolution endpoint — a LIVE CLAIM at the last step). Lossy step: Green's cap T(x) ≤ 4 on
cross-disjoint ordered pair-pair differences is summed per x against the triangular weight (4u²); their joint
realisability by one 0/1 set is discarded. Lemma: for every B4 set A ⊆ {0..N−1}, N ≥ 256, u = min{u : u^17 ≥ N^13},
D(A,N) = Σ_{0<|x|<u} (4 − T_A(x))(u − |x|) satisfies 100·D ≥ u(u−1). Conditional output: β4 ≤ (399/(100 c_low))^{1/4},
a (399/400)^{1/4} coefficient gain, asymptotic only. Scout grade: important milestone (specialist).

Coordinator judgement (reading, not research):
- The card is admissible under rule 1 and genuinely uses discarded information (which pairs realise each x). Its bite
  regime, however, is narrow: S = A+A is a Sidon set and T(x) ≤ 4·1[x realised by S] (times doubled-sum corrections), so
  B4-L fails only if S realises ≥ 399/400 of the weighted differences |x| < u. No known B4 construction comes near that
  regime (Bose–Chowla-type sets have |A+A| ≈ √N/2 against the ≈ √(2N) needed), so the finite test of card (e) will
  almost surely report SURVIVED with a large, uninformative margin — the scout says so itself. The lemma's truth is
  decided by B4 sets denser than any construction (m ≳ 1.5 N^{1/4} at their own scale), i.e. exactly the regime the
  record bound is about. Grade if proved: important milestone (specialist) as the scout says; a disproof would need a
  dense B4 set with a locally difference-complete sumset, itself a construction result.
- **Rule 5 is triggered** (1 card < 3): the pool, not the method, is the bottleneck. Reported to the owner in the AUT-62
  comment. Under the owner's full-speed instruction this does not stop the round: the single card is processed to the
  end (test ∥ probe) while the scout widens the pool again in parallel, so the Codex slots stay busy with real work.

## Step 2 dispatch (2026-10-09 18:0x UTC) — three children of AUT-62, all blocking it

1. **VER (verifier, Claude): B4-L finite test** exactly as card (e)/(h) — whole orbits of the Bose–Chowla B4 and Singer
   families for q ∈ {2,3,4,5}, every subset, every multiplier and cut, both conventions, dense small sets, greedy
   fixtures; cap 55 CPU-min as the card says. Coordinator additions: report the realised fraction of weighted small
   differences of S = A+A per family (the informative number, cf. ρ in AUT-57/AUT-60), and a 15-CPU-min diagnostic
   search (greedy/hill-climb B4 sets at N ∈ {256, 512, 1024} minimising D) to measure how close any small B4 set gets to
   the threshold. SURVIVED with a 10× margin on every family is expected and is not evidence for the lemma.
2. **CR-8 (attacker-2, Astra, clean room): prove or disprove B4-L.** Rooms alternate (attacker-1 did CR-7). Run in
   parallel with the test, not after it: the owner asked for full speed, the test is expected to be uninformative, and
   in CR-7 the attacker found the disproof itself in 1.7 CPU-s. Brief = statement, definitions, standard of proof, route
   seeds (mathematics only: Sidon structure of A+A; the bite-regime reduction; window counting of near pairs; disproof by
   finite-field B4 constructions and small exhaustive search). No literature, no repository, no campaign files.
3. **SCOUT (Codex): widening pass 2** — a second catalogue (≤ 20 records) and shortlist (≤ 8 cards) from areas not yet
   screened: covering systems (minimum-modulus constant), zero-sum constants (Davenport / EGZ / Olson for small rank),
   sum-product exponents and constants, sums of dilates / small-doubling inverse constants, distinct subset sums and
   Erdős–Moser constants, thin additive 2-bases of [N], Egyptian-fraction constants, erdosproblems.com numeric-record
   problems outside Sidon. New card requirement (lesson of B4-L): state the bite regime of the lemma and whether any
   known construction reaches it; a lemma no known object can test is admissible but ranked below one that can.

## Decision rules for step 3 (fixed now)

- CR-8 PROVED → two Claude referees (cross-vendor), then G2 by the scout, then grading (important milestone if the
  transfer to β4 is written out with the LIVE-CLAIM endpoint replaced by the refereed 0.574636066 value as the headline;
  the Rechnitzer value only as a conditional remark) and a request_board_approval before any outward action.
- CR-8 DISPROVED with an exact finite set → verifier replay (rule 4), card parked; the set itself is checked for being
  a new dense B4 construction (construction-grade product) before being filed.
- CR-8 OPEN → B4-L parked unless the obstruction report names a provable weaker constant; no campaign on a lemma with an
  uninformative finite test and an OPEN probe.
- Scout pass 2 < 3 cards → rule 5 again; the coordinator then proposes to the owner a change of selection doctrine
  (e.g. construction-grade targets or a Lean/kernel milestone for the published #30 bound) instead of a third sweep.
- A campaign is proposed only via request_board_approval, grading first.

## Step 2 results (all three children closed 18:04–18:15 UTC) and coordinator judgement

1. **VER (AUT-67, verifier): SURVIVED, uninformative as predicted.** Whole orbits of Bose–Chowla and Singer B4 sets for
   q = 2..5 (542,737,260 raw (b,a,t) triples, every subset, both conventions, translates/reflections by invariance), all
   B4 subsets of {0..31} with ≤ 4 elements, greedy prefixes × dilates, and a 3 × 290 CPU-s hill-climb. Smallest
   ρ = 100D/(u(u−1)) anywhere: 174.24 (hill-climb, N = 256; the lemma needs ρ ≥ 1); best realised weighted fraction
   F = 0.564 against the 399/400 the lemma allows. Exact finite evidence only. Report: lemma_tests_20261010/B4L_test.md.
   Cost ≈ 17.4 CPU-min.
2. **CR-8 (AUT-68, attacker-2, Astra, clean room): PARTIAL.** Proved B4-L for every N ≥ 256 when |A| ≤ 6, and under the
   explicit conditions 14·K4 ≤ 13(u−1) or 20·K ≤ 19(u−1) (K4 = 3C(m,4), K = m(m−1)(m²−m+2)/8), i.e. roughly m⁴ ≲ 7.6u —
   far below the record regime m ≈ c·N^{1/4}, u ≈ N^{13/17}. Exact structure proved: T(x) ∈ {0,1,2,4} with exact
   category counts, disjointness of ordinary and pair-pair differences, packing m(m−1)(m²−m+6) ≤ 16(N−1), exact
   eighth-moment identities, and a synthetic histogram showing that histogram + support + unweighted moments alone
   admit zero deficit (the missing information is the *location* of the four-distinct-element differences). First
   unsettled case N = 256, m = 7: combinatorial upper bound 9660 vs required 9635.85 (missing saving 24.15). A genuine
   B4 family A_K (large base B = 16K+1) realises T(x) = 4 for all 1 ≤ |x| ≤ K, but its diameter forces u(N_K) > K+1,
   so it is not a counterexample at the prescribed window. 1,200 greedy trials + 1,758 exhaustive small sets: no
   counterexample. Report: problems/b4sets/CR8_ASTRA_B4L_20261010.md (embedded Node replay reproduced every number).
   Cost: 24 min wall, 20.3 CPU-s.
   **Correction of the brief (coordinator error):** the route seed "S = A+A is a Sidon set" was FALSE for every |A| ≥ 2
   ((2a)+(2b) = (a+b)+(a+b)); the attacker proved the correct identity R_S(x) = m·1_P(x) + 1[T(x)>0]. The seed was
   written by the coordinator in its own judgement paragraph above, i.e. the coordinator did mathematics in a brief —
   exactly what the division-of-labour rule forbids. The bite-regime paragraph in the step-1 judgement is therefore
   wrong in its mechanism (the correct mechanism is CR-8 §3–§6) though not in its conclusion (no known construction
   reaches the regime; the test was indeed uninformative). Rule 6 below.
3. **SCOUT pass 2 (AUT-69): 14 new records, ZERO admissible cards.** Areas: covering systems (B1–B3, B14), zero-sum
   constants (B4–B6), sums of dilates (B7–B8), order-two bases (B9–B10), unit-fraction subsets (B11–B13). Every record
   has a one-line exclusion and a bite-regime audit (lemma_shortlist_20261010b.md, lemma_catalogue_20261010b.md).

**Verdict on B4-L: OPEN in the regime that matters; PARKED.** Not re-carded. Theorem 1 of CR-8 is a restricted-range
partial result far from the bite regime, unrefereed; refereeing it would cost two runs for a result that cannot move
the record, so per the fixed step-3 rule (OPEN → park) it is filed with the card. Grade: small result (negative/partial),
nothing published. The large-base family A_K is noted as a construction curiosity (complete small differences at a free
window), not a product.

**Round outcome: NO SURVIVOR for the second time; rule 5 twice (pass 1: 8 records → 1 card; pass 2: 14 records → 0).**
Termination condition of AUT-62 reached: lemma-gated selection is stopped; the bottleneck is the screened pool, not the
method. Reported to the owner on AUT-62 with a structured question (see below). No campaign, no approval request, nothing
published. Round cost: scout 2 runs, verifier 1 run (17.4 CPU-min), attacker-2 1 run (24 min), coordinator 5 runs.

## Lessons (added to SELECTION.md as rules 6–7)

6. Route seeds in a brief come from the scout's card or are omitted; the coordinator never adds mathematics of its own
   (the false "A+A is Sidon" seed of CR-8). A wrong seed costs attacker time and can bias a clean room.
7. A PARTIAL whose proved range is far from the lemma's bite regime is parked unrefereed with the card; referees are
   spent only on PROVED or on partials that move the record.

## Proposal to the owner (question card on AUT-62, 18:2x UTC)

Options offered, coordinator recommendation first:
- A (recommended): stop lemma-gated sweeps; work on our own published lines where value is certain and verifiable —
  first the Erdős #30 onset lowering (120^4 → the proof's own threshold ≈ 4.54e6 per referee B; LINE AUT-71 opened,
  scout card AUT-72 dispatched; attacker/verifier/referees/formalizer only after the card), and in parallel a scout
  screen of construction-grade targets (explicit objects certifiable by search + verifier) for slot 2.
- B: a third widened sweep in further areas (expected yield low: 22 records → 1 card → OPEN).
- C: back to probe-based selection on famous problems (round 4 judged it at its method limit).
- D: pause selection; only finish the published lines (#30 owner-pending items, onset lowering), no new targets.

## Doctrine A part 2 — construction-grade screen dispatched (2026-10-10 03:1x UTC, coordinator on Opus 5.5)

State at wake: the Fable quota ran out 2026-10-09 20:00 UTC; every coordinator run after that failed until the owner
switched the coordinator and referee-1 to Opus 5.5 (relay comment on AUT-62, 03:04Z: continue from the current state).
The question card on AUT-62 is still unanswered; all seven reports were idle; three coordinator issues (AUT-62, AUT-71,
AUT-75) wait on the owner.

Decision (coordinator authority over selection; owner veto kept): execute the second half of option A now. The first
half (#30 onset lowering, AUT-71) is complete and waiting for board approval, so the only idle-free work left in A is
the slot-2 screen; it is one scout run, cheap and reversible. If the owner answers B, C or D on the card, the line is
stopped or re-planned.

- LINE AUT-94 (coordinator), blocked on SCOUT AUT-95: ≤15 construction-grade records, ≤3 cards with an exact checker
  each; deliverables construction_screen_20261010.md and construction_cards_20261010.md.
- Bar: importance (famous problem / named proposer / maintained record table, attention 2024–2026); explicit record
  object; certification by an exact deterministic program ≤10 CPU-min on one core, no SAT/ILP/MIP/CP packages for search
  or certification (owner rule: solvers only on GitHub Actions and only for important results); 2025–2026 AI-lab
  construction work checked and flagged CROWDED.
- Next steps fixed: coordinator judges cards → VER reproduces baseline + checker → one clean-room construction attempt
  (attacker-1, statement/threshold/checker/card seeds only, rule 6) → verifier certifies → scout G2 → grading → board.
- Termination: 0 admissible cards → construction pool also thin; report to the owner and recommend D; no second screen
  without owner direction.

### Outcome (2026-10-10 03:2x UTC, coordinator on Opus 5.5) — ZERO admissible cards; line terminated

SCOUT AUT-95 delivered construction_screen_20261010.md (6 records) and construction_cards_20261010.md (0 cards).
Coordinator judgement against the step-2 bar (importance; exact checker ≤10 CPU-min, no SAT/ILP/MIP/CP; not the output of a
2025–2026 AI search unless a gap is stated; negative lists), record by record:

| Record | Bar | Verdict |
| --- | --- | --- |
| C4 N(4,6) ≥ 746 (Oct 2026), C5 N(6,3) ≥ 120 (Oct 2026), C6 K(11) ≥ 604 (Apr 2026) | each record is an explicit 2026 AI-assisted construction on the maintainer's page / platform | **out — CROWDED** (agree with scout) |
| C3 N(3,10) ≥ 1250 (Conder 2006) | importance and checker pass; no source names a lossy choice or an unused parameter | **out — no named lever** (selection v3 slot-1 condition; round-4 lesson) |
| C2 n(3,13) ≤ 272 (Hoare/Biggs 1989) | checker passes; current-record chain not freshly confirmed; the reported 272 is already the exact minimum among vertex-transitive/Cayley graphs, which blocks the obvious symmetric route | **out — provenance gap + subclass barrier** |
| C1 four MOLS(22) (3 known since ≤1978) | importance passes (the 2024 MOLS-table paper singles out order 22); checker trivial (<1 s); not AI-crowded; on the 2025-09-25 board only as a "gacha-scale" side task | **out as a card**, for the coordinator's own reason, not the scout's provenance gap: the only sourced lever (a (22,6,2) difference matrix, M1 §8) is the stated next step of the record holders themselves (Abel is a co-author), so it is not an untried lever; and an attempt is a computer search for a 6-column OA, not an LLM-reasoning task — the owner rules make LLM reasoning the solver and confine solver-grade search to GitHub Actions for important results. Kept as a possible owner-funded long shot only. |

Coordinator note on the bar: "hard for humans" is not used as a reason anywhere above (owner rule); each exclusion is
CROWDED, no named lever, or a provenance/subclass obstruction.

**Termination rule applied (fixed when the line was opened):** 0 admissible cards → the construction-grade pool is also
thin. Three screens in 24 h (lemma pass 1: 8 records → 1 card → OPEN; pass 2: 14 → 0; construction: 6 → 0) — the pool,
not the method, is the bottleneck. The screen part of LINE AUT-94 is terminated; no VER/CR steps were dispatched; no second screen without owner
direction. Recommendation to the owner: **option D** (pause selection; finish the published #30 line: approval 04b27a03
for the single Zenodo version with onset 4,600,000 and the related-work section; the session-side forum reply B). The stale
AUT-62 doctrine card (A recommended, A now fully executed) is withdrawn and replaced by a fresh card on AUT-94 (the run
could not write interactions to AUT-62; AUT-62 is closed with a pointer) with D recommended and, as an alternative, D plus
one owner-funded MOLS(22) long shot. AUT-94 waits in_review on that card.

Cost of the line: scout 1 run (AUT-95), coordinator 2 runs; no attacker, verifier or referee time; nothing published.

### Owner decision and the MOLS(22) long shot (2026-10-10 03:5x UTC)

Owner (03:48Z, relay on AUT-94): option D; standing authority to execute the coordinator's card recommendations without
waiting (OWNER_RULES); full speed until the 05:00Z pause, idle engines usable, the MOLS(22) long shot left to the
coordinator's judgement. D has no remaining work (#30 Zenodo v3 published). Coordinator decision: one long shot — high
value (N(22) ≥ 4 is the gap the 2024 MOLS-table paper singles out), certification under a second, binary outcome, owner rule
allows long shots on idle engines; cap = one attacker run, no second attempt on failure. CR-10 AUT-97 (attacker-1, clean
room; seeds only from the scout's screen, verbatim, rule 6) and VER AUT-98 (independent checker + baseline replay) in
parallel. Exit: object → VER certification → scout G2 → grading → board approval for any outward action; no object →
PARTIAL/OPEN recorded with the exhaustively covered search spaces, nothing published, line closed.
