# TICKET K6-H2 — the two-step ascent: mechanism, exact characterisation of local maxima, and a proof attempt

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_H2/` (create): `REPORT.md`
ending with `DONE-K6H2`, scripts, logs. Exact arithmetic. Read first `engine/harvest/k1695_r6_H/REPORT.md`
and reuse its `scan.c` (the kd computation and the cell enumeration are audited).

## Facts (from K6-H, exhaustive on GL(3,q≤7), GL(4,2), GL(4,3), GL(5,2))
kd(A, σ, i) := dim Krylov(A P_σ, e_i). Local maxima (kd < n, no transposition neighbour with larger kd)
EXIST (first in GL(3,4): A = [[1,2,1],[2,1,1],[1,0,0]] over GF(4), σ = id, i = 2, kd = 2, all three
neighbours kd = 2), but "one equal step then an ascent" NEVER fails on any scanned cell (weak two-step
trap count 0 everywhere). Also for kd_max(A,σ) = max_i kd and for the defect δ. So the conjecture:
**(H2) for every A ∈ GL(n,F), σ and i with kd(A,σ,i) < n there is a path σ → στ₁ → στ₁τ₂ (τ_k
transpositions, possibly with τ₂ = id) along which kd never decreases and strictly increases at
the end.** (H2) ⟹ (S′) ⟹ 16.95, by iterating.

## Tasks
1. **Structure of local maxima.** For each scanned cell (rerun the K6-H scan with extra output): for
   every local maximum (A, σ, i), record: kd; the Krylov space K = span(e_i, Me_i, …) (M = AP_σ); the
   eigenstructure of M; which transpositions are "neutral" (kd unchanged) and which decrease; and for
   the successful two-step (τ₁ neutral, τ₂ ascending) how τ₁ changes the Krylov space. Print the
   first five with full data. Look for the invariant pattern: e.g. is the Krylov space K at a local
   maximum always M-invariant with a specific structure (K = a sum of generalised eigenspaces)?
   Is the neutral step τ₁ always one that moves K without changing its dimension, in a way that a
   Lemma-T-type rank-one update can then increase? Formulate the mechanism as precisely as the data
   allows (exact statements, machine-checked on all local maxima in the cells).
2. **Exact single-step criterion.** Derive and prove (over every field) the rule for how kd changes
   under a transposition: with M = AP_σ and M′ = M P_τ = M − (m_a − m_b) dᵀ (columns a,b of M
   swapped; d = e_a − e_b), express the Krylov space of e_i under M′ in terms of that under M. Note
   that kd(M′, e_i) is the dimension of the smallest M′-invariant subspace containing e_i. Prove at
   least: (i) if i ∉ {a, b} and e_a − e_b ∈ K^⊥-type conditions … — find the right statement; at
   minimum give an exact formula/algorithm for kd(M′, e_i) − kd(M, e_i) ∈ {…} and its possible range
   (is it always in {−?, …, +1}? measure on the cells first, then prove the range).
3. **Proof attempt for (H2).** Using 1–2, try to prove: from a local maximum, the two-step exists.
   Key idea to test: at a local maximum with kd = k < n, K is M-invariant of dimension k (Krylov
   spaces are invariant once they stop growing); choose τ₁ moving a coordinate inside K's support
   pattern so that K′ (new Krylov space) is a different k-dimensional M′-invariant space "closer" to
   containing a coordinate that can be reached… — formulate a potential finer than kd (e.g. the pair
   (kd, number of coordinates j with e_j ∈ K) or (kd, dim(K ∩ span of standard basis vectors)))
   and TEST whether that refined potential has NO local maxima on the scanned cells (add it to the
   scan). A potential with no local maxima at all, plus a proof that its ascent step always exists,
   IS a proof of (S′). Try at least two candidate refined potentials and report the scan for each.
4. Report: the mechanism (exact), the single-step criterion with proof and check, the refined
   potentials with their scan tables, and the proof attempt with its exact residual. End with
   `DONE-K6H2`.
