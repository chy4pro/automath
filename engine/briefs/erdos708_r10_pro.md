# ATTACK — Erdős Problem #708, round 10: can COUNTING give an absolute constant? (TEMPLATE v2.3, inequality type, prove-or-refute)

## The statement
Weights z_p ∈ [0,1] on primes (finitely many nonzero), w(n) := Σ_p z_p v_p(n), m ≥ 1, x ≥ 0, I := {x+1,…,x+m}, K := {1,…,m}.
   (TH_c)   Σ_{k≤m} (w(k)−c)⁺ ≤ Σ_{b∈I} (w(b)−1)⁺.
PROVED: (TH_c) for all weights with m = a_n < 8n³ ⇒ g(n) ≤ (c+16)n (LP duality), and 2n suffice for a_n ≥ 8n³. An ABSOLUTE constant c
in (TH_c) gives the first linear bound for the Erdős–Surányi function (Erdős asks for 2n).

## What is PROVED (use freely)
P1 (round 8, refereed) (TH_c) for all weights with c = 1 + 149e ln(1+ln m). (round 9, engine-proved, under independent referee now)
   the same with c = 20 ln ln m, m ≥ 3. Architecture of both: random thinning of the moduli ≤ y = L^{1/(k+1)} with probability θ ≍ 1/H,
   H = e ln(1+ln L); two-term Bonferroni [r ≥ k] ≥ C(r,k) − kC(r,k+1) with the interval counts L/d − 1 < N_J(d) < L/d + 1, giving
   #{n ∈ J : ν_D ≥ k} ≥ L e_k/(4(8H)^k); the union bound #{n ≤ L : ν_D ≥ 2k+ρ} ≤ L e_k H^ρ/ρ!; hence a gain G at cost ρ ≈ eH + O(k ln H);
   geometric layers q = 51/50 encode X(n) = Σ_p min(u_p v_p(n),1); weighted ordering identity; quotient intervals; peel w = E + S.
P2 THEOREM A (round 6): 0/1 weights, threshold ≤ 20 ln ln m, same method without thinning.
P3 COUNTING CERTIFICATES: if Σ_{d|n} c_d ≤ (w(n)−1)⁺ for all n ≥ 1 (F) then Σ_I (w−1)⁺ ≥ V(c) := Σ_{c_d>0} c_d ⌊m/d⌋ − Σ_{c_d<0} |c_d|(⌊m/d⌋+1);
   so (TH_c) holds for (m,z) and all x as soon as V(c) ≥ Σ_K (w−c)⁺. Explicit 0/1 family with anchors R = first r primes:
   c_d = (−1)^{|A|} (d = ∏A, A ⊆ R, |A| ≥ 2), c_d = (−1)^{|A|+1} (d = q∏A, q ∉ R, A ≠ ∅); (F) holds since Σ_{d|n} c_d = (|A₀|−1)⁺ + |Q₀|[A₀≠∅].
   r = 2 proves the 0/1 (TH_2) for P = all primes ≤ m and every m ≤ 10⁷; V_2(m) − Σ_K(ω−2)⁺ = −(1/3) m ln ln m + (29/18 − M/3) m + o(m),
   so r = 2 FAILS beyond m ≈ 10⁴². Two anchors also fail for P = primes in [53,653], m = 10⁸; three anchors work there.
   LP-optimal certificates (constraint generation, exact) exist for 0/1 weights, P = all primes ≤ m, m ≤ 1000 (V* = 907 vs W = 321 at
   m = 1000; support: prime powers with c = 1, pairs containing the 2–3 smallest primes with c = 1, triples with c = −1) and for fractional
   weights (m ≤ 200, ≤ 7 primes).

## Coordinator's analysis (my intuition — test it, do not trust it)
A1 Where the ln ln is INTRINSIC in P1: (i) the two-term Bonferroni needs θ·Σ_{d≤y} 1/d ≲ 1, i.e. θ ≲ 1/H; (ii) thinning at rate θ forces the
   [1,L]-threshold B ≳ 1/θ ≈ H (a level-B integer must keep ≳ 1 modulus after thinning); (iii) t-term Bonferroni instead pays e_{k+t}/e_k ≈
   H^t/t!, small only for t ≳ eH. Splitting the moduli into scales ln p ∈ [2^i, 2^{i+1}) makes each scale's H a constant (ln 2) but there are
   ln ln L scales and the budgets ADD. So no variant of thinning + Bonferroni + union bound reaches an absolute constant; the ln ln must be
   paid ONCE by an argument that is not a sum over scales.
A2 Heuristic for the anchor family with r fixed anchors R and P = all primes ≤ m: V_r(m) ≈ m ln ln m · (1 − ∏_{a∈R}(1 − 1/a)) + O_r(m), while
   Σ_K(ω − c)⁺ ≈ m ln ln m − cm. Fixed anchors therefore lose a factor ∏(1−1/a) ≈ e^{−γ}/ln p_r of the main term: an absolute c needs
   ln p_r ≳ (ln ln m)/c, i.e. the anchor set must GROW with m, and then the 2^r anchor subsets each cost ≈ π(m/2) from the (⌊m/d⌋+1) side.
   Either a hierarchical certificate (anchors of anchors) fixes this, or counting with both interval bounds is provably insufficient.
A3 The decisive object is the ABSTRACT ADVERSARY: a multiset (or probability measure) of valuation patterns t = (v_p(t))_p, |multiset| = m,
   with ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1 for every d ≤ m (N(d) = number of patterns divisible by d), minimising Σ_t (w(t)−1)⁺. By LP duality its value
   equals max_c V(c) over certificates (F). If the adversary can push Σ(w−1)⁺ below Σ_K(w−c)⁺ for every absolute c (at some m, z), counting
   with both interval bounds cannot give a linear bound and genuinely arithmetic input (CRT correlations of the ±1 errors) is needed.

## Targets (equal rank; prove-or-refute)
T1 PROVE: a certificate family (F) for ALL weights (or first for 0/1 weights and all prime sets P) with V(c) ≥ Σ_K (w − C)⁺ for an explicit
   absolute C and all m. Routes: hierarchical/adaptive anchors (anchors = primes of largest z_p/p); certificates built from thinning (the
   expectation of a random-anchor certificate is a certificate); the LP support pattern above as the ansatz.
T2 REFUTE: an explicit abstract adversary (A3) — a family of valuation-pattern multisets, one for each m in an infinite sequence, satisfying
   both interval bounds for all d and with Σ_t (w(t)−1)⁺ ≤ Σ_K (w−c)⁺ − 1 for c → ∞ (say c = c(m) → ∞ as slowly as you can), for 0/1 weights
   and P = all primes ≤ m. Give the construction explicitly enough that we can verify a small instance by computer. This would prove that
   Section-8-type counting certificates cannot give an absolute constant, and identify exactly which arithmetic fact must be used instead.
T3 The 0/1 case with an absolute constant for ALL prime sets P (adaptive anchors): a full proof, or an explicit P (with m) where every
   certificate with anchors ⊆ P fails at threshold c = 3.
T4 A different route to an absolute constant that pays the ln ln once (e.g. treat the ⌊(ln ln L)/C⌋ smallest-weight-adjusted moduli exactly by
   CRT classes with both interval bounds, and the rest by the round-9 sieve at a constant threshold), fully proved.
Rule: no intermediate statement is used before an adversarial agent has tried to break it on dense windows (Hensley–Richards) and on abstract
multisets; every lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; end with "final claim ← lemmas ← unproved items".

## Machine facts
M1 (TH_2): 2.1·10⁶ instances (m ≤ 600), no counterexample; on dense windows of length 10⁵ the slack is ≥ 0.18m; equality only at x = 0 with one prime.
M2 Every argument using only the lower bounds N_I(d) ≥ ⌊m/d⌋ at a single threshold fails on dense windows (weight-free matching,
   single-threshold level sets, Laplace transform, two-layer sieve). Both interval bounds are necessary.
M3 LP certificate values (0/1, all primes ≤ m): m = 300: 223.5 vs W = 59; 500: 407.4 vs 124; 1000: 907 vs 321.

## Current task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively and use multiagents
aggressively and dynamically: (i) an adversary team building A3 multisets (both interval bounds!) and computing their Σ(w−1)⁺; (ii) a
certificate team (hierarchical anchors, thinning-expectation certificates); (iii) a T4 team; (iv) a referee team checking every constant.
Budget: about two hours; then return the strongest rigorously proved statement among T1–T4 with its exact gap (do not fail silently).

## Output contract
Numbered lemmas with status tags; every constant explicit; every construction explicit enough to be re-run by us (small instance for T2);
what a Lean formalisation needs. A check that cannot fail counts as no check.
