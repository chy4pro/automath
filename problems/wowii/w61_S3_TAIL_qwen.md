# Q24 — w61 Lemma TAIL S3, zero-rounds statement with two blocked consumers (Qwen3.8-Max)

- Target: Lemma TAIL (§7.13 D) and its `λ = [2]` instance inside Observation
  FAN-5. Blocks Observation FAN-5's second half and the `ν ≤ 6` elimination
  of Theorem GFANν.
- Dispatched: 08-18 18:2x CDT, owner-intel round 14 (brief `prompts/w61_S3_TAIL_qwen.md`, 41 KB)
- Harvested: 08-18 19:0x CDT, owner-intel round 15 (evening harvest)
- Conversation: https://chat.qwen.ai/c/d0b2dfe0-4fe6-4a9f-8dc4-c9baebb3306d
- Model confirmed: Qwen3.8-Max
- Completion confirmed via true-bottom scroll to the static action-icon row,
  held static across a follow-up poll.

## VERDICT (model's own line)

> VERDICT: PARTIAL — Lemma TAIL and the FAN-5 λ = [2] instance are
> mathematically correct under the intended nonempty L ≥ λ1 hypothesis; I
> found no MATHEMATICS defect in the load-bearing conclusion, only
> repairable bookkeeping/boundary defects.

**Zero mathematics defects. First-ever round on Lemma TAIL, comes back
effectively clean modulo boundary bookkeeping.**

## Refutation log / own implementation

Wrote an independent value-multiset Havel-Hakimi implementation from the
appendix spec (own pseudocode given in full), calibrated against K2 (residue
1) and C3..C9 (all match ⌈n/3⌉) — all calibration values agreed. Searched
partitions λ with |λ| ≤ 12, L = 0..15; **zero in-scope mismatches** against
`(L - λ1) + s0(λ)` for the certified region L ≥ λ1. Explicitly recomputed
`steps([2,2,2,2]) = 2` for the FAN-5 λ=[2] instance from scratch (not reused
from the brief).

## Joint table

| joint | verdict | note |
|---|---|---|
| J-TAIL-BLOCK | PARTIAL | one-step block claim correct for t>λ1; parenthetical "true at t=L" is false in the permitted equality case L=λ1 (needs a zero-step clause) |
| J-TAIL-IND | CLEAN | loop bounds, multiplicity preservation, and the (L-λ1)+s0(λ) arithmetic all verified |
| J-TAIL-EQUIV | PARTIAL | equivalence correct under L≥λ1; over-claims as a standalone rider if that hypothesis is dropped — smallest failure λ=[4], L=2 |
| J-TAIL-DEF | PARTIAL | steps definition consistent with residueAux; but λ1:=max λ undefined for λ=∅ (missing convention) |
| J-FAN5 | CLEAN | λ=[2] instance recomputed independently: total = L for every L≥2; first half correctly attributed to Lemma FAN-3 |
| J-SCOPE | CLEAN | Lemma TAIL is a pure multiset statement, needs none of residue=α/GFan/diam=4/f=α+1; graph-theoretic placement over-hypothesises but doesn't harm the proof |

## Defects (all BOOKKEEPING, all repairable, conclusion survives in every case)

1. **Equality-case gap**: proof's opening parenthetical "(true at t=L)" is
   false when L=λ1 (zero descent steps needed). Repair: add "if L=λ1, there
   is nothing to prove."
2. **λ1 := max λ undefined for λ=∅**. Repair: nonempty-λ hypothesis, or
   convention λ1=0 for empty/zero case. Conclusion survives for the actual
   consumers (ν≥1, E=0 ⟹ λ always nonempty in practice).
3. **"Consequently" equivalence over-claims if L≥λ1 is silently dropped.**
   Smallest explicit failure found: λ=[4], L=2 — `s0([4])=4=λ1` but
   `steps([4,2,2,2])=3≠2`. Repair: state the hypothesis explicitly in the rider.

## Boundary probes (explicit smallest failures found, all correctly outside the lemma's stated hypothesis)

- λ=[3], L=1: direct steps=1, formula gives (1-3)+4=2 — mismatch, but L<λ1 (out of scope).
- λ=[2], L=0: direct steps=1, formula gives (0-2)+2=0 — mismatch, out of scope.
- λ=[4], L=2 (the key control): direct steps([4,2,2,2])=3, not L=2 — this is
  the witness used across Defects 2/3 and the T12 counterfactual-availability
  control.

## Repair-species probes

- Probe 1: J-TAIL-EQUIV correctly identified as the primary rider requiring
  explicit L≥λ1 retention; both directions of the equivalence verified once
  restated. Secondary riders (cross-check sentence, FAN-5 citation caveat)
  checked, both procedural/non-load-bearing.
- Probe 2: the LOW/SL-style widening here (dropping to "depends only on λ")
  is true inside L≥λ1 and false outside it — GFANν's own proof already
  handles boundary rows L<λ1 separately, so the contagion is contained, but
  the rider itself needs the hypothesis restated.
- Probe 3: no box-vs-branch artifact — Lemma TAIL's induction is general,
  not box-supported; GFANν's finite case list is a genuine branch reduction
  from hand-proved bounds, not a box standing in for a general claim.

## T12 controls

- **Control A (L<λ1)**: λ=[4], L=2 — hypothesis fails, equivalence rider
  fails as predicted (the deliberately-triggered counterfactual).
- **Control B (repeated maximum)**: λ=[2,2], L=2 (=λ1) — Lemma TAIL still
  works (steps=3, matches formula), but **Lemma FAN-6' would not execute**
  on this control since the maximum isn't unique — the named non-executing
  lemma required by the T12 amendment (not a TAIL defect, an availability note).
- **Control C**: λ=[2], L=2 — the actual FAN-5 instance, TAIL available with
  zero descent, steps=2=L, confirmed.
- Witness validation: all three exhibited multisets checked against the
  basic multiset-form constraint (`[L]^{L+1} ∪ λ` with correct multiplicity)
  before anything else; λ=[4],L=2 explicitly flagged as a counterfactual
  control (violates L≥λ1), not an in-scope witness.

## What the model could NOT check

Did not re-run the archived scripts or reuse any appendix-quoted count
(explicitly avoided reuse per the brief's instruction); did not print a full
mismatch log for the entire |λ|≤12, L≤15 box outside the in-scope region
(spot-checked boundary witnesses instead); did not verify graph-realizability
of the counterfactual multiset controls (not needed — TAIL is a multiset
lemma); Theorem GFANν / Corollary GFANν-HC out of scope, checked only how
they use Lemma TAIL.

## Out-of-scope observations (noticed anyway, non-load-bearing)

- Possible `ν=0` issue in Theorem GFANν (E=0 residue could be empty; needs
  ν≥1 or the λ1=0 convention).
- Lemma FAN-6' at the single part `[1]`: "second-largest ≤ w-2" convention
  question for w=1 — doesn't affect TAIL/FAN-5.
- Status/S3-round claims are procedural, not independently verifiable from
  text alone, don't affect mathematical correctness.

## Caveats for owner-w61 / planner

- **UNVERIFIED by owner-w61** — re-verify line by line before adoption.
- **CLEAN on mathematics, 3 bookkeeping/boundary defects** — per the row's
  own consequence note: "CLEAN ⟹ FAN-5's citation caveat (Repair W2) can be
  lifted and the row moves; also unblocks Q25's J-GFANNU input." The verdict
  tag returned is PARTIAL (not CLEAN) due to the 3 repairable boundary
  defects, but zero mathematics defects were found — same
  PARTIAL-vs-CLEAN-threshold question flagged for Q23 applies here too.
  **Note**: Q25 (the GFAN family S3 round meant to consume this TAIL round's
  clean status via J-GFANNU) is CAPTCHA/dead-blocked this round — see
  qwen_queue.md Q25 row and this round's Chrome-lease note; it has NOT
  consumed this result yet.
