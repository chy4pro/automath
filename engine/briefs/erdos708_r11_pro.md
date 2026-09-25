# ATTACK — Erdős Problem #708, round 11: the SPARSE CORE of the fractional hinge inequality (TEMPLATE v2.3, inequality type, prove-or-refute)

## The statement
Weights z_p ∈ [0,1] on primes (finitely many nonzero); S(n) := Σ_p min(z_p v_p(n), 1) = Σ_{p,j} α_{p,j} 1[p^j | n] with atoms
α_{p,j} := min(z_p j, 1) − min(z_p (j−1), 1) ≥ 0 (finitely many nonzero). m ≥ 1, x ≥ 0, I := {x+1,…,x+m}, K := {1,…,m}.
   (TH_C)   Σ_{k≤m} (S(k) − C)⁺ ≤ Σ_{b∈I} (S(b) − 1)⁺   for all z, m, x, with an ABSOLUTE constant C.
PROVED: (TH_C) for S implies it for w_z = Σ_p z_p v_p (peel w = E + S), and then g(n) ≤ (C+16)n for the Erdős–Surányi function — the first
linear bound. This is the whole game now.

## What is PROVED (use freely)
P1 Counting certificates: if (c_d) satisfy (F) Σ_{d|n} c_d ≤ (S(n)−1)⁺ for every n ≥ 1, then Σ_I (S−1)⁺ ≥ V(c) := Σ_{c_d>0} c_d ⌊m/d⌋ −
   Σ_{c_d<0} |c_d| (⌊m/d⌋+1). Affine certificate c_1 = −1, c_{p^j} = α_{p,j}: V = Σ_K S − m − 1, so (TH_C) holds whenever Σ_K min(S, C) ≥ m+1.
P2 0/1 case, threshold 4, every prime set (refereed, published): y = ⌊m^{1/3}⌋, S₀ = P ∩ [2,y], η = (1+1/y) Σ_{p∈S₀} 1/p; η ≤ 2 → certificate
   c_{p^j} = 1 (j ≥ 2), c_{pq} = 11/21, c_{pqr} = −1/7 on S₀ (feasible since r(r−1)(13−r)/42 ≤ (r−1)⁺; value ≥ A + E₂/3 via C(|S₀|,3) ≤ E₃ and
   3E₃ ≤ ηE₂); η > 2 → affine certificate with a greedy subset of harmonic mass in [3/2, 2).
P3 (engine-proved this evening, under independent referee — treat as CONDITIONAL until you re-derive it) Dense fractional branch: with
   H_64(m,z) := Σ_{p^j ≤ m/64} α_{p,j}/p^j, if H_64 ≥ 17/16 then (TH_65) holds; atoms with p^j > m/64 contribute ≤ 1 in total to each k ≤ m.
   Hence full fractional (TH_65) ⇐ (SC_64): for m > 4096 and H_64 < 17/16, Σ_K (S₀(k) − 64)⁺ ≤ Σ_I (S₀(b) − 1)⁺ where S₀ uses only p^j ≤ m/64.

## Dead routes (engine-proved this evening; do not retry them, but you may re-verify)
D1 Positive-coefficient level-set / dyadic combinations of 0/1 instances cannot control the right side (fake hinges), with any constant.
D2 '0/1 vertices ⇒ whole cube [0,1]^P' is FALSE as an abstract principle (9 coordinates: LHS = 7 copies of [9], RHS = the 36 pairs;
   7(t−4)⁺ ≤ C(t,2) at every vertex, but z ≡ 1/2 gives 7/2 > 0). Multiplicative structure must be used explicitly.
D3 Independent or dependent Bernoulli rounding of the weights leaves an unremovable fake cost.
D4 Positive pair coefficients are infeasible when two primes can divide n with total weight < 1; no fixed-degree pointwise polynomial
   certificate handles arbitrarily small weights — the certificate must be hierarchical (all orders).
D5 The +1 per negative coefficient is sharp against the abstract adversary; the random-partition certificate (Möbius aggregation of a random
   grouping of atoms into r blocks) captures Σ_K F_r ≥ Σ_K (S−r)⁺ but has signed error E_r = Σ_{γ<0} |γ|; the sliding-window certificate
   (order the atoms, c_A = Leb{t : the unit window [t,t+1] meets exactly the atoms A}) is nonnegative and (F)-feasible but captures only
   Σ (run length − 1)⁺ over runs of active atoms in the fixed order.

## Coordinator's analysis (test it)
A1 In the sparse core the natural mean is < 17/16, so S₀(k) is typically ≈ 1 and the left side counts rare integers with ≥ 64 units of
   small-modulus atom mass. Any argument must beat the abstract adversary, who may put the +1 on every negative modulus; so certificates
   with many negative coefficients over huge atom sets are hopeless (D5) — the number of atoms can be ≈ π(m/64) with tiny weights.
A2 The 0/1 sparse branch worked because pair/triple moduli ≤ m^{1/3}·… made the negative cost C(|S₀|,3) ≤ E₃ 'free'. The fractional analogue
   must make every negative coefficient's +1 dominated by a matching floor count, e.g. by using only moduli d ≤ m/64 with ⌊m/d⌋ ≥ 64 so that
   +1 ≤ (1/64)⌊m/d⌋ — a 1/64 relative loss, which is exactly why 64 appears. Explore: certificates whose negative support is restricted to
   d ≤ m/64 with coefficients bounded by a constant times the positive mass they correct.
A3 Threshold-aware hierarchical ansatz: c_A = f(α_A) for atom sets A ordered by size, with f built from the sliding-window measure
   (nonnegative) plus a bounded negative correction only on moduli ≤ m/64. Decide whether such a certificate can prove (SC_64) with an
   absolute constant, or whether the abstract adversary restricted to the sparse core can beat every constant.

## Targets (equal rank; prove-or-refute)
T1 PROVE (SC_r) for some absolute r (r = 64 or any other), hence fractional (TH_C) and g(n) ≤ (C+16)n. Full proof, every constant.
T2 PROVE (RP_64): E_64 ≤ Σ_K min((S−64)⁺, 64) for the random-partition certificate (⇒ (TH_129) ⇒ g(n) ≤ 145n), or the analogous
   statement for any explicit hierarchical certificate.
T3 REFUTE: an explicit abstract adversary inside the sparse core (a family of valuation-pattern multisets, one for each m in an infinite
   sequence, satisfying ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1 for all d) with Σ_t (S₀(t)−1)⁺ < Σ_K (S₀ − c)⁺ for c → ∞ — proving that counting with both
   interval bounds cannot give a linear bound and identifying the arithmetic input needed; or an explicit counterexample to fractional
   (TH_C) itself (we re-check everything by computer; give a small instance).
T4 A different reduction that avoids the sparse core (e.g. a sieve-type comparison at the typical level that pays ln ln only once, combined
   with P2's certificates on the small primes).
Rule: no intermediate statement is used before an adversarial agent has tried to break it on Hensley–Richards windows and on abstract
multisets; every lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; end with 'final claim ← lemmas ← unproved items'.

## Machine facts
M1 (TH_2) for fractional weights: no counterexample in 2.1·10⁶ instances (m ≤ 600); dense windows of length 10⁵ leave slack ≥ 0.18m.
M2 Exact LP (abstract adversary with both bounds) for fractional weights, m ≤ 200, ≤ 7 primes: threshold 2 always certified.

## Current task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; use multiagents
aggressively and dynamically: (i) a certificate team on A2/A3 and (RP_64); (ii) an adversary team building sparse-core multisets with both
interval bounds and computing their exact cost (LP for small m, constructions for large m); (iii) a T4 team; (iv) a referee team checking
every constant. Budget: about three hours; then return the strongest rigorously proved statement among T1–T4 with its exact gap.

## Output contract
Numbered lemmas with status tags; every constant explicit; every construction explicit enough to be re-run by us; what a Lean
formalisation needs. A check that cannot fail counts as no check.
