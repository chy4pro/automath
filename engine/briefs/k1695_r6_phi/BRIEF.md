# BRIEF K6-PHI — prove (or break) the monotonicity of the potential Φ′ = (kd, −ν) (ChatGPT Pro, math tier; do not search the internet)

You are given an exact combinatorial-linear-algebra conjecture with strong finite evidence. Produce a
PROOF over an arbitrary field, or an explicit COUNTEREXAMPLE (a field, an n×n matrix, an index), or
the exact residual statement you cannot close. No essays; every claim with its argument.

## Setting
F a field, M ∈ GL(n, F), v = e_i a standard basis vector. Krylov dimension
kd(M, i) := dim span{e_i, M e_i, M² e_i, …} (= n iff e_i is a cyclic vector of M, in which case M is
nonderogatory). Moves: right multiplication by a transposition matrix, M ↦ M P_τ (τ = (a b) swaps
columns a and b of M). With d := e_a − e_b: P_τ = I − ddᵀ and M P_τ = M − (Md)dᵀ, a rank-one update.
Facts (proved): K := Krylov(M, e_i) is M-invariant (M invertible). For τ = (ab): if dᵀK = 0 then
M P_τ = M on K and kd is unchanged with the same Krylov space; if d ∈ K then (M P_τ)K ⊆ K and kd does
not increase; otherwise ("generic": d ∉ K, dᵀK ≠ 0) the new Krylov space leaves K. Call τ NEUTRAL for
(M, i) if kd(M P_τ, i) = kd(M, i), and let ν(M, i) := number of neutral transpositions (out of n(n−1)/2).
A LOCAL MAXIMUM is (M, i) with kd(M, i) < n such that no transposition increases kd.

## Evidence (exhaustive, exact, all of GL(3,q) for q ∈ {2,3,4,5,7}, GL(4,2), GL(4,3), GL(5,2))
1. Local maxima exist (e.g. GF(4): M = ((1,α,1),(α,1,1),(1,0,0)), i = 2, kd = 2; all three
   transpositions neutral).
2. At every local maximum some neutral transposition τ has kd(M P_τ P_τ′, i) > kd(M, i) for a further
   transposition τ′ (the "two-step" always exists).
3. **Φ′ := (kd, −ν), ordered lexicographically, has NO local maximum below kd = n on any scanned cell:
   at every kd-local maximum there is a NEUTRAL transposition τ with ν(M P_τ, i) < ν(M, i).**
Consequently the conjecture:
> **(Mono)** For every field F, every M ∈ GL(n,F) and i with kd(M, i) < n: either some transposition
> increases kd, or some neutral transposition τ has ν(M P_τ, i) < ν(M, i).
(Mono) ⟹ hill-climbing on Φ′ terminates at kd = n ⟹ for every A ∈ GL(n,F) and every i there is a
permutation σ with e_i a cyclic vector of A P_σ ⟹ Thompson's conjecture (Kourovka 16.95).

## Tools you may use
- The rank-one recurrence: for N = M − u dᵀ (u = Md), the Krylov vectors of e_i under N are
  x₀ = e_i, x_{j+1} = M x_j − u (dᵀ x_j).
- Top layer kd = n − 1: K = ker ψ for a left eigenvector ψᵀM = λψᵀ with ψ_i = 0. A transposition (ab)
  increases kd iff no left eigenvector of N = M P_τ vanishes at i. Left eigenvectors of N at μ satisfy
  yᵀ((M − μI) + μ ddᵀ) = 0; for μ ∉ spec M this gives yᵀ ∝ dᵀ(M − μ)⁻¹ with the secular condition
  1 + μ dᵀ(M − μ)⁻¹ d = 0, and y_i = 0 ⟺ dᵀ(M − μ)⁻¹ e_i = 0.
- In the top layer: d ∈ K ⟺ ψ_a = ψ_b; dᵀK = 0 ⟺ ψ ∝ d.
Suggested first target: prove (Mono) in the top layer kd = n − 1, then for kd = n − 2, then in general;
or find the counterexample at n = 6 (we have not scanned n = 6). State exactly what you proved.
