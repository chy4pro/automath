# MICRO-LEMMA — Erdős Problem #708, round 11 (single-shot): the single-scale case of the 0/1 hinge inequality by counting

## Setting (all proved, use freely)
m ≥ 1, x ≥ 0, I = {x+1,…,x+m}, K = {1,…,m}. P a finite set of primes, w(n) := ω_P(n) = #{p ∈ P : p | n}. Target inequality
   (TH_2)   Σ_{k∈K} (w(k) − 2)⁺ ≤ Σ_{b∈I} (w(b) − 1)⁺   for every x ≥ 0.
PROVED (counting certificates): if real numbers (c_d), finitely many nonzero, satisfy (F) Σ_{d|n} c_d ≤ (w(n) − 1)⁺ for EVERY n ≥ 1, then
Σ_I (w−1)⁺ ≥ V(c) := Σ_{c_d>0} c_d ⌊m/d⌋ − Σ_{c_d<0} |c_d| (⌊m/d⌋ + 1), because ⌊m/d⌋ ≤ N_I(d) ≤ ⌊m/d⌋ + 1 for every d.
PROVED (affine certificate): Σ_I (w−1)⁺ ≥ Σ_K w − m, so (TH_2) holds whenever #{k ≤ m : w(k) = 0} ≤ #{k ≤ m : w(k) ≥ 2}. This fails when P has
no small primes (e.g. P = primes in [53,653], m = 10⁸: 61,911,251 integers with w = 0 against 7,944,229 with w ≥ 2).
PROVED (binomial identity): Σ_{j=0}^{t} (−1)^j C(s,j) = (−1)^t C(s−1,t), hence for odd t: Σ_{j=2}^{t} (−1)^j C(s,j) = s − 1 − C(s−1,t) ≤ s − 1 for every s ≥ 0.

## Coordinator's proposed certificate (check every step; it is not yet proved)
For odd t ≥ 3 let c_d := (−1)^{ω(d)} for squarefree d composed of primes of P with 2 ≤ ω(d) ≤ t, and c_d := 0 otherwise. Then (F) holds
(by the identity, with equality s − 1 when s = w(n) ≤ t), and
   V(c) − Σ_K (w−2)⁺ = #{k ≤ m : w(k) ≥ 2} − Σ_{k≤m, w(k)>t} C(w(k)−1, t) − N_odd(P,t),   N_odd(P,t) := #{d : ω(d) odd, 3 ≤ ω(d) ≤ t}.
If t ≥ max_{k≤m} w(k) the middle term vanishes. For P ⊆ (y, y ln y] one has max_{k≤m} w(k) ≤ ln m / ln y =: u, N_odd ≤ Σ_{j odd ≤ t} C(|P|, j),
and #{k ≤ m : w(k) ≥ 2} ≈ m (Σ_{p∈P} 1/p)²/2 · (1 + o(1)) — so counting should prove (TH_2) for every single-scale P once y is large enough.

## Targets, in order of value
T1 PROVE, with explicit constants: there are y₀ and a function t(m,P) such that for every prime set P ⊆ (y, y ln y] with y ≥ y₀ and every m ≥ 1,
   (TH_2) holds for every x (the odd-depth certificate above, or a better one). State precisely the condition on (m, y, P) under which the
   certificate value exceeds Σ_K (w−2)⁺, with explicit error terms (use only elementary bounds: ⌊m/d⌋ ≥ m/d − 1, C(|P|,j) ≤ |P|^j/j!, and the
   number of integers ≤ m with at least two prime factors in P bounded below by Σ_{p<q∈P} ⌊m/pq⌋ − Σ_{p<q<r} ⌊m/pqr⌋).
T2 Extend T1 to P ⊆ (y, y^{1+ε}] for a fixed ε > 0, or show where the odd-depth certificate stops working (the count N_odd against m).
T3 The obstruction to several scales: for P = P₁ ∪ … ∪ P_S with P_i ⊆ (y_i, y_i ln y_i) and w_i := ω_{P_i}, prove the identity
   Σ_i (w_i(n) − 1)⁺ − (w(n) − 1)⁺ = (#{i : w_i(n) ≥ 1} − 1)⁺ for w(n) ≥ 1, and give the cheapest certificate (c'_d) with Σ_{d|n} c'_d ≤
   −(#{i : w_i(n) ≥ 1} − 1)⁺ for all n (so that the sum of per-scale certificates plus c' is feasible), with its value estimated explicitly in
   terms of S and the Σ_{p∈P_i} 1/p. This quantifies what a multi-scale certificate must pay.

## Task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web or other
sources. Every claimed lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; every constant explicit; every finite computation
stated so it can be re-run. Do not return a heuristic or an explanation of why the problem is hard.
