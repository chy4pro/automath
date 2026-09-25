# TICKET K6-H — is the Krylov dimension a hill-climbing potential? (exact scan, C)

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_H/` (create): `scan.c`,
logs, `REPORT.md` ending with `DONE-K6H`. Exact GF(q) tables (self-checked), no floating point.
Reuse the audited field/matrix primitives from `engine/harvest/k1695_r6_T/search.c` if convenient.

## Definitions
For A ∈ GL(n,q), a permutation σ (P_σ e_j = e_{σ(j)}, so A P_σ has columns of A permuted), and an
index i, let `kd(A, σ, i) := dim span{e_i, M e_i, …, M^{n−1} e_i}`, M = A P_σ (the Krylov dimension;
= n iff e_i is a cyclic vector of M). Known: for every A and i some σ has kd = n on GL(5,2), GL(4,3),
GL(4,4) (exhaustive) — the (S′) property. The question here is LOCAL: define the transposition graph on
S_n (σ ~ στ for a transposition τ). Call (A, σ, i) a **local maximum** if kd(A, σ, i) < n and
kd(A, στ, i) ≤ kd(A, σ, i) for every transposition τ (all n(n−1)/2 of them). Also record the
**strict-ascent** variant: no neighbour with kd(στ) > kd(σ), and the **weak** variant: no neighbour
with kd(στ) ≥ kd(σ) + 1 AND no neighbour of equal kd that itself has an ascending neighbour (2-step).

## Cells (exhaustive; print populations and check them against ∏(qⁿ − qⁱ))
GL(3,q) for q ∈ {2,3,4,5,7}; GL(4,2); GL(4,3); GL(5,2) — for EVERY A, every i, every σ.
For each cell print: the number of (A, σ, i) triples with kd < n; the number of local maxima (strict
sense); the number of local maxima in the weak sense; the distribution of kd at local maxima; and the
FIRST five local maxima found (A, σ, i, kd, and the kd of all neighbours). Also the analogous counts
for the potential `kd_max(A, σ) := max_i kd(A, σ, i)` (index free) and for `cyc(A, σ) := n − (number
of invariant factors of A P_σ different from 1)` i.e. n minus the nullity-defect Σ_μ (g_μ − 1)
(compute it as n − max over μ of nullity(M − μ) … no: compute the DEFECT δ(M) = Σ_μ max(0, g_M(μ) − 1)
over μ in GF(q²) (enough for n ≤ 5? — no: for n = 5 a derogatory eigenvalue can have degree ≤ 2, so
GF(q²) suffices; state this) and ask whether δ has local minima > 0).

## Controls (must print)
- Positive: for A = I (n ≥ 2) and any i, kd(I, σ, i) = length of the cycle of σ containing i; check
  that local maxima of kd in this case are exactly the σ whose cycle through i has length n−1?? — no:
  compute and PRINT what they are; assert at least that σ = id is not a local maximum for n ≥ 2.
- Negative: implement a deliberately wrong kd (e.g. dimension of span{e_i, Me_i} only) and show the
  local-maximum counts change.
- Cross-check kd against an independent rank routine on 10⁴ random triples per cell.

## Report
Per cell, the table above. Then the honest one-line answer to: "does hill-climbing on kd (or on
δ) from ANY σ reach a cyclic AP_σ, on these cells?" If local maxima exist, print the smallest with
its full neighbourhood — that is the object of interest. End with `DONE-K6H`.
