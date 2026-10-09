# Selection round 2026-10-10 (part 2 of the lemma-gated round) — coordinator record

Status: STEP 2 DISPATCHED 2026-10-09 18:0x UTC (LINE issue AUT-62). Predecessor: selection_20261009.md (round AUT-51,
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
