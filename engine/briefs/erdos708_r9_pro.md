# ATTACK — Erdős Problem #708, round 9: the hinge inequality with an ABSOLUTE constant (TEMPLATE v2.3, inequality type)

## The statement to prove
Weights z_p ∈ [0,1] on primes (finitely many nonzero), w(n) := Σ_p z_p v_p(n), m ≥ 1, x ≥ 0, I := {x+1,…,x+m}, K := {1,…,m}.
   (TH_c)   Σ_{k≤m} (w(k)−c)⁺ ≤ Σ_{b∈I} (w(b)−1)⁺.
PROVED: (TH_c) for all weights supported on the primes dividing ∏a_i with m = a_n < 8n³ ⇒ g(n) ≤ (c+16)n (LP duality), and 2n suffice
for a_n ≥ 8n³. So (TH_c) with an ABSOLUTE constant c, for all m, gives g(n) ≤ (c+16)n — a linear bound for the Erdős–Surányi function,
which is what Erdős's $100 question is about (he asks for 2n; any absolute constant would be the first linear bound).

## What is PROVED (use freely; all audited by us and by an independent referee)
P1 THEOREM (round 8): for all weights, all m ≥ 16, all x: (TH_{c_m}) with c_m = 1 + 149e ln(1 + ln m). Proof: (a) k-th order two-term
   Bonferroni [r ≥ k] ≥ C(r,k) − kC(r,k+1); (b) gain-G sieve lemma for pairwise-coprime moduli D: for 1 ≤ G ≤ 2H, 1 ≤ k ≤ R−1
   (R = ⌊log₂ L⌋, H = e ln(1+ln L), L₀ = ln(H+2)): G·#{n ≤ L : ν_D(n) ≥ 2k+ρ(k)} ≤ #{n ∈ J : ν_D(n) ≥ k}, ρ(k) = ⌈16H + 16kL₀/√ln(2+k/H)⌉,
   proved by random thinning (keep each modulus ≤ y = L^{1/(k+1)} with probability 1/(8H)), Bonferroni + the interval counts
   L/d − 1 < N_J(d) < L/d + 1 for the lower bound #{n ∈ J : ν ≥ k} ≥ L e_k/(4(8H)^k), and the union bound #{n ≤ L : ν ≥ 2k+ρ} ≤ L e_k H^ρ/ρ!
   for the upper bound (e_j = elementary symmetric functions of 1/d over the small moduli); (c) exact dyadic encoding
   min(u_q v_q(n),1) ≥ 2^{−j} ⟺ q^{⌈2^{−j}/u_q⌉} | n, so X(n) := Σ_q min(u_q v_q(n),1) satisfies X ≤ Σ_j 2^{−j} N_j ≤ 2X with N_j = ν_{D_j};
   (d) weighted sieve lemma: #{n ≤ L : X(n) ≥ 149H} ≤ #{n ∈ J : X(n) ≥ 1} (Q = 1+⌊log₂(R−1)⌋ ≤ 2H dyadic levels, gain G = Q pays for the
   union over levels, budget A ≤ 148H + 2); (e) weighted ordering identity: with r_p(n) = min(a_p v_p(n), N), R = Σ r_p, prefix sums R_{<p},
   (R(n) − T − N)⁺ ≤ Σ_{p|n} r_p(n)[R_{<p}(n) ≥ T] ≤ (R(n) − T)⁺; (f) quotient intervals and the peel w = E + S.
   The constant 149 is loose by ≈ 2.5× (the literal budget gives A+1 ≈ 0.3·149H). Where the ln ln comes from: H = e ln(1 + ln L) bounds
   Σ_{p≤y} 1/p; the tail #{n ≤ L : ν ≥ s} ≤ L H^s/s! only becomes small for s ≫ H, i.e. the method compares the [1,L]-count ABOVE the
   typical value of ν with the J-count at level k; an absolute constant needs a comparison at the typical level.
P2 THEOREM A (round 6): 0/1 weights, threshold c*(m) ≤ 20 ln ln m, same method without thinning.
P3 COUNTING CERTIFICATES: if Σ_{d|n} c_d ≤ (w(n)−1)⁺ for all n then Σ_I (w−1)⁺ ≥ Σ_{c_d>0} c_d ⌊m/d⌋ − Σ_{c_d<0} |c_d|(⌊m/d⌋+1) =: V(c);
   (TH_2) holds for (m,z) and all x as soon as V(c) ≥ Σ_K (w−2)⁺. LP-verified certificates exist for fractional weights (m ≤ 200, ≤ 7 primes,
   z ∈ {1, 0.7, 0.4, mixed}) and 0/1 weights (all primes ≤ m, m ≤ 1000, margin ≥ 2.8×). Explicit 0/1 family: anchors R = first r primes,
   c_d = (−1)^{|A|} for d = ∏A (A ⊆ R, |A| ≥ 2), c_d = (−1)^{|A|+1} for d = q∏A (q ∉ R, A ≠ ∅); (F) holds since Σ = (|A₀|−1)⁺ + |Q₀|[A₀≠∅];
   with r = 2 it proves the 0/1 (TH_2) for P = all primes ≤ m and every m ≤ 10^7 (fails beyond ~10^42; more anchors needed for prime sets
   without small primes). Feasible certificates for all weights: affine c_1 = −1, c_{p^j} = z_p (value Σ_K w − m − 1) and, per prime,
   increments c_{p^j} = (z_p j − 1)⁺ − (z_p(j−1) − 1)⁺.

## Machine facts
M1 (TH_2): 2.1·10⁶ instances (m ≤ 600), no counterexample; on dense windows of length 10⁵ (Hensley–Richards: more integers free of small
   primes than [1,m]) the slack is ≥ 0.18m. Equality cases: x = 0 and a single prime only.
M2 Every argument that used only lower bounds N_I(d) ≥ ⌊m/d⌋ at a single threshold failed on dense windows (weight-free matching,
   single-threshold level sets, Laplace transform, two-layer sieve without a growing threshold). Both bounds must be used.

## Targets, in order of value (prove-or-refute, equal rank)
T1 (TH_c) for ALL weights and all m with an explicit ABSOLUTE constant c (any c; c = 2 is the conjecture). Routes: (i) a comparison at
   the typical level: instead of the union bound L e_k H^ρ/ρ! on [1,L], compare the distribution of ν on [1,L] with that on J via
   inclusion–exclusion over the small moduli with BOTH interval bounds — the 0/1 certificate family already does this for anchors; find
   the fractional analogue (certificates c_d built from thinning: expected value of a random-anchor certificate is itself a certificate);
   (ii) the certificate LP: guess the general certificate from the LP solutions at m ≤ 200 (their support: prime powers p^j with c = 1,
   pairs containing the two or three smallest weighted primes with c = 1, triples with c = −1) and prove (F) and V ≥ W for all m;
   (iii) an iterated / multi-scale sieve: apply the gain-G lemma at scale L, then at scale L/p for the quotient intervals, so that the
   ln ln L is paid once, not at every level.
T2 (TH_c) with c = C ln ln ln m, or with c = C ln ln m and an explicit C ≤ 20 for all weights (improves the constant in the published bound;
   a clean restatement of the round-8 proof with optimised θ, G and budget may already give ≈ 60e).
T3 Refute: an explicit (m, z) and an explicit abstract multiset of valuation patterns satisfying ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1 for all d with
   Σ_t n_t (w(t)−1)⁺ < Σ_K (w−c)⁺ for the c you are attacking (this would show counting alone cannot give that c), or an explicit
   counterexample to (TH_c) for an absolute c (we re-check everything).
T4 The 0/1 case with an absolute constant c for all m and all prime sets P (an explicit certificate family with adaptive anchors,
   or a sieve argument at the typical level).
Rule: no intermediate statement is used before an adversarial agent has tried to break it on dense windows and on abstract multisets;
every lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; end with a dependency list "final claim ← lemmas ← unproved items".

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; partial progress
counts only if it implies exactly one of T1–T4. Use multiagents aggressively and dynamically: (i) typical-level comparison / thinned
certificates; (ii) certificate LP pattern-finding with exact (F)-checks on adversarial valuation patterns; (iii) multi-scale sieve;
(iv) an adversarial team (abstract multisets, dense windows, many light primes, high prime powers); (v) T2 as the fallback. Budget:
about two hours; then return the strongest rigorously proved derivation with its exact gap (do not fail silently).

## Output contract
Numbered lemmas with status tags; every constant explicit; every finite computation stated so it can be re-run; what a Lean
formalisation needs. A check that cannot fail counts as no check.
