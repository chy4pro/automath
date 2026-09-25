# MICRO-LEMMA — Erdős Problem #708, round 13 (single-shot): the all-pairs shadow certificate for unequal masses

## Setting (all proved, use freely)
Atoms p^j with weights α_{p,j} ≥ 0, Σ_j α_{p,j} ≤ 1; S₀(n) = Σ α_{p,j} 1[p^j | n]; for a fixed integer k ≤ m write a_p := Σ_{p^j | k} α_{p,j} ∈ [0,1] and let
q_p be the largest active prime power of p at k. Counting certificates: if c_D ≥ 0 satisfy (F) Σ_{D|n} c_D ≤ (S₀(n) − 1)⁺ for every n ≥ 1, then for every
window I of m consecutive integers Σ_{b∈I}(S₀(b) − 1)⁺ ≥ Σ_D c_D ⌊m/D⌋.
PROVED (32 shadows): if S₀(k) > 64, group the primes into 32 disjoint groups G_r of mass Σ_{p∈G_r} a_p ∈ (4/3, 2]; D_r := ∏_{p∈G_r} q_p are pairwise
coprime, ∏ D_r | k; if t of the D_r divide n then S₀(n) > 4t/3 so (S₀(n)−1)⁺ > t/3; hence c_{D_r} = 1/3 is feasible and
Σ_I (S₀−1)⁺ ≥ (1/3) Σ_r ⌊m/D_r⌋ ≥ (32/3)(1 − 6^{−31}) m/k^{1/32} (AM–GM: Σ 1/D_r ≥ 32 (∏D_r)^{−1/32} ≥ 32 k^{−1/32}).
PROVED (equal masses): if 65 groups have masses exactly x_1 = … = x_65 = 1 (65 distinct primes with a_p = 1), the certificate c_{D_i D_j} = 2/65 on all
C(65,2) pair products is feasible, because u divisors of the pair type dividing n means u = C(s,2) for s active groups and (2/65)C(s,2) ≤ s − 1 for
s ≤ 65; its value is (2/65) Σ_{i<j} ⌊m/(D_iD_j)⌋ ≥ 64(1−ε) m/k^{2/65} (AM–GM on the C(65,2) products, each ≤ k^{2/65} on average) — better than the
32-shadow bound (exponent 2/65 < 1/32). This would extend the sparse-core range from 10^2887 to about 10^2957.

## Targets, in order of value
T1 UNEQUAL MASSES. Suppose S₀(k) > 64 and the primes are grouped into N groups with masses x_1, …, x_N ∈ (β, 1] for some β ∈ (0,1] (any grouping
   allowed; N may exceed 65). Find the largest λ (as a function of N, β) such that the pair certificate c_{D_iD_j} = λ for all i < j satisfies (F):
   i.e. prove for every n: if the set A(n) of groups whose D_i divides n has size s, then λ C(s,2) ≤ (Σ_{i∈A(n)} x_i − 1)⁺ — note Σ_{i∈A} x_i > sβ.
   Give the exact condition (λ C(s,2) ≤ sβ − 1 for all 2 ≤ s ≤ N suffices; is it necessary? handle s with sβ ≤ 1) and the resulting lower bound
   Σ_I (S₀−1)⁺ ≥ λ Σ_{i<j} ⌊m/(D_iD_j)⌋ ≥ λ C(N,2)(1 − ε) m (∏ D_i)^{−2/N} with an explicit ε, hence ≥ c(N,β) m/k^{2/N}. Optimise N and β for a k with
   S₀(k) > 64 (masses a_p ≤ 1; the packing gives at most ⌊64/β⌋+1 groups of mass > β; state exactly how many groups of mass in (β,1] one can
   guarantee from total mass > 64 — e.g. β = 64/65 gives 65 groups only for equal masses; find the true guarantee for arbitrary masses).
T2 From T1, the best explicit constant c and exponent 2/N in Σ_I (S₀−1)⁺ ≥ c m/k^{2/N} valid for EVERY atom system with S₀(k) > 64, and the
   resulting range m ≤ M for the inequality c m^{1−2/N} ≥ 6.24·10^{−90} m (this is the new sparse-core range). Give log10 M.
T3 Triples and higher: the certificate c_D = μ_ℓ on all ℓ-fold products; feasibility condition μ_ℓ C(s,ℓ) ≤ (sβ − 1)⁺; value ≥ μ_ℓ C(N,ℓ)(1−ε) m k^{−ℓ/N};
   show which ℓ, N minimise the exponent ℓ/N subject to feasibility and total mass 64, and confirm or refute that N/ℓ ≈ 32.5 is optimal.

## Task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web or other sources.
Every claimed lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; every constant explicit; every finite computation stated so it can
be re-run. Do not return a heuristic or an explanation of why the problem is hard.
