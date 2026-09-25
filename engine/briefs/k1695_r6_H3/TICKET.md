# TICKET K6-H3 — normal forms of the local maxima of the Krylov dimension; the kd = n−1 layer in closed form

Self-contained; no internet; no essay. Output to `engine/harvest/k1695_r6_H3/` (create): `REPORT.md`
ending with `DONE-K6H3`, scripts, logs. Exact arithmetic; reuse `engine/harvest/k1695_r6_H2/scan.c`.
Read `engine/harvest/k1695_r6_H2/REPORT.md` first (mechanism, single-step recurrence, residual lemma).

## Goal
Find the invariant structure of the local maxima (M, i) of kd — states where e_i is not cyclic for M
and no column transposition increases the Krylov dimension — so that a potential function WITHOUT
local maxima can be guessed and then proved, or so that the residual lemma of K6-H2 can be proved
by hand in the top layer kd = n − 1.

## Part A — normal forms (data mining, exact)
Symmetries preserving "local maximum with index i": simultaneous permutation conjugation
M ↦ P_ρ M P_ρ⁻¹ with ρ(i) = i (relabel the other coordinates); right multiplication by transpositions
is NOT a symmetry (it is the move); field automorphisms (Frobenius) for non-prime fields; scaling
M ↦ λM. For each cell GL(3,4), GL(3,5), GL(4,2), GL(4,3), GL(5,2): list the orbits of local maxima
under these symmetries with one representative each (M, i, K = Krylov basis, χ_M, χ_K, kd), and for
each orbit: the set of neutral transpositions (same-K / generic) and the escaping second steps.
Look for and REPORT: (i) whether K always has a basis of vectors with a specific support pattern
(e.g. K = span(e_i, w) with w having a 0 at exactly the coordinates …); (ii) whether M restricted to
K and the quotient M̄ on Fⁿ/K have a fixed relation (e.g. χ_K and χ_M/χ_K share a root ⟺ …);
(iii) which pairs (a, b) are generic-neutral: is it always the pairs with exactly one of a, b in
some coordinate set determined by K (e.g. a ∈ supp(K), b ∉ …)? Formulate the pattern as exact
predicates and machine-check them on ALL local maxima of all cells (not just orbit representatives).

## Part B — the kd = n − 1 layer in closed form (any n, any field)
If kd(M, e_i) = n − 1 then K is an M-invariant hyperplane through e_i: K = ker ψ for a left eigenvector
ψᵀ M = λψᵀ with ψ_i = 0. For a transposition τ = (a b): kd(M P_τ, e_i) = n ⟺ no left eigenvector of
N = M P_τ vanishes at i. Derive the exact criterion: left eigenvectors of N at λ′ satisfy
ψ′ᵀ((M − λ′I) + λ′ ddᵀ) = 0 (a rank-one update of M − λ′). Split: (i) λ′ ∉ spec M: ψ′ ∝ (M − λ′)⁻ᵀ d,
existence iff the secular scalar 1 + λ′ dᵀ(M − λ′)⁻¹ d = 0 (⟺ λ′ is an eigenvalue of N), and
ψ′_i = 0 ⟺ dᵀ(M − λ′)⁻¹ e_i = 0 — so the bad λ′ are the common roots of χ_N(λ′) and the polynomial
p_{ab}(λ′) := dᵀ adj(M − λ′) e_i (degree ≤ n − 1); (ii) λ′ ∈ spec M: use Lemma T's clauses (g = 1, 2, …)
to describe the left eigenvectors of N at λ′ and their i-th coordinates. Hence a transposition (ab)
ASCENDS iff Res(χ_N, p_{ab}) ≠ 0 and the eigenvalue-of-M cases are clean. Write this out exactly,
machine-check it against the scan on all kd = n − 1 states in GL(4,2), GL(4,3), GL(5,2) (counts of
ascending pairs predicted vs observed, 0 disagreements, negative control that fails), and then
ATTEMPT the proof of the residual lemma in this layer: show that if every (ab) is blocked (the
resultant vanishes or an eigenvalue case bites), then some (ab) is generic-neutral and after it some
(cd) is clean — using that ψ (the obstruction at M) has ψ_i = 0 and that a generic neutral step
replaces K by another hyperplane ker ψ′ with ψ′ ≠ ψ (up to scale) and ψ′_i = 0.

## Part C — one more potential
Test the potential Φ = (kd, number of DISTINCT M-invariant subspaces of dimension kd containing e_i
that are Krylov spaces of some (MP_τ, e_i) over the transposition neighbourhood) — i.e. "how many
different K's are one step away"; and Φ′ = (kd, −(number of neutral transpositions)). Scan both on
all cells; report trap counts.

## Report
Orbit tables, the exact predicates found (with their check lines), the closed-form kd = n−1
criterion with its check, the proof attempt with its exact residual, the two potential scans. End
with `DONE-K6H3`.
