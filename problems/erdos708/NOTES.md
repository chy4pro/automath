# Erdős #708 — dialogue working notes (2026-09-03)

Statement (Er92c §1): g(n) = least g such that for every 1 < a_1 < … < a_n and every x ≥ 0 some g integers in
(x, x + a_n] have product ≡ 0 mod ∏a_i. Known: g(2)=2, g(3)=4, g(n) ≥ (2−o(1))n (ES 1959). No upper bound recorded.

## Verified facts (gn_dp.py = exact min|B| by DP over capped valuation vectors)
- ES family l=3 (17,19,23), x=74072 → 4; l=4 (41,43,47,53), x=26348553 → 6 (p_i² multiples save one element each).
- P17 intermediate examples: A=(10,12,15,20), x=50 → 5 (mechanism: 25 > a_n = 20, so E_5 = 3 costs three 5-multiples,
  all with poor 2/3-valuations); A=(5,10,12,15,20), x=50 → 6. Hence g(4) ≥ 5, g(5) ≥ 6. Worst x < 3600 same.
- Per-prime dominance (easy lemma): #{a ∈ A : p^j | a} ≤ ⌊a_n/p^j⌋ ≤ #{b ∈ I : p^j | b}; hence for each prime p an
  injection φ_p : {a : p | a} → I with v_p(φ_p(a)) ≥ v_p(a) exists (nested Hall). Gives only |B| ≤ Σ_a ω(a) (non-linear).
- Trap (both Q20 responses): a shared element contributes its valuation ONCE. Mandatory test for any algorithm: the l=3
  ES instance must output ≥ 4 elements.
- Distinct-multiples matching for a ≤ a_n/2 is NOT available: van Doorn–Li–Tang (arXiv 2603.28636, Erdős #650) —
  an interval of length 2·max(A) guarantees only min(m, ⌈2√m⌉) disjoint (a, multiple) pairs, optimally.

## Reformulation worth attacking (dialogue): the split-assignment problem
Choose for each a a factorisation a = d₁(a)·d₂(a) with gcd(d₁,d₂) = 1 (d₂ = 1 allowed) and assign each of the ≤ 2n
"demands" d ∈ {d₁(a), d₂(a)} to an element β(d) ∈ I such that for every element b and every prime p,
Σ_{d : β(d) = b} v_p(d) ≤ v_p(b). Then B = β(demands) has |B| ≤ 2n and ∏A | ∏B.
Conjecture S: such a split and assignment always exist. S ⇒ g(n) ≤ 2n. S holds on the ES family (halves = the two primes;
u absorbs one demand per prime, singles the rest). S is a finite integer-feasibility question for each (A, x) — test it
by ILP/backtracking on adversarial instances before any proof attempt. Where S could fail: several a's sharing a prime p
with p² > a_n (each element then absorbs ≤ 1 unit of p) — but #{a : p | a} ≤ ⌊a_n/p⌋ ≤ #multiples of p in I, so the
p-units alone always fit; failures must come from cross-prime packing.
Weaker but still new: any assignment with k demands per a ⇒ g ≤ k·n; a 3-split (T2 with C = 3) may be provable first.

## S test results (22:18 CDT)
split_assign.py: S feasible on ES l=3, ES l=4, P17's (10,12,15,20)/x=50 and (5,10,12,15,20)/x=50, and 965,773 random instances (n ≤ 5, a_n ≤ 60): 0 infeasible.
Structural observation: capacity constraints are per prime; composite demands are the only cross-prime coupling; S holds outright when every a has ≤ 2 distinct primes (finest split + per-prime dominance). Counterexamples, if any, need a's with ≥ 3 primes and scarce composite multiples.
Gacha (search_small_n.py, a_n ≤ 60): n=4 best 5 (P17's instance), n=5 best 5 — no instance beyond P17's.

## Round 4 working notes (06:19 CDT, 09-04): the hinge inequality (TH) and the injection route
- (TH): Σ_{k≤m}(w(k)−2)⁺ ≤ Σ_{b∈I}(w(b)−1)⁺, w = Σ z_p v_p, 0 ≤ z_p ≤ 1. Equivalent (correct sign): Σ_I min(w,1) − Σ_K min(w,2) ≤ Σ_I w − Σ_K w.
  Machine tests: 2.1M (hinge_test2.py), no counterexample. z ≡ 1 on all primes makes (TH) trivial (RHS−LHS ≥ m − π(m) − 2); the tight
  cases are single primes with two multiples in I (slack 0) — so the difficulty is in mixed/fractional weights.
- Injection route (P20's): φ: K₂ → I injective with (k/p) | φ(k) for some prime p | k gives w(φ(k)) ≥ w(k) − 1 and hence (TH).
  Weight-free version (INJ): φ on all of {2..m}. Tested: 105,160 instances (exhaustive x-window for m ≤ 40, random m ≤ 400):
  no failure (inj_full_test.py); K₂-version 97,196 tests, no failure (injection_test.py).
- OBSTRUCTION (dialogue): Hall for T = all composites reads |N(T)| = m − #{b ∈ I : lpf(b) > m/2} ≥ m − 1 − π(m), i.e.
  #{b ∈ I : lpf(b) > m/2} ≤ π(m) + 1. The rough positions in a window of length m form an admissible set w.r.t. the primes
  ≤ m/2 and every admissible pattern is realised by some x (CRT), so the maximum count is ≥ ρ*(m), the Hensley–Richards
  admissible-tuple maximum, which exceeds π(m) from m = 3159 and (Hensley–Richards 1974) satisfies limsup(ρ*(m) − π(m)) = ∞.
  Hence (INJ) FAILS for infinitely many m (with astronomically large x — invisible to the tests). Any proof of (TH) via an
  injection must use the weights (K₂ depends on z), and for weights where K₂ = all composites (TH) is trivial anyway. So the
  weight-free matching lemma cannot be the whole proof; audit P20's matching lemma against exactly this T.

### 07:08 CDT — P20 harvested; (NM)/(SB) refuted; new sufficient condition (PQ)
- P20 (144 min) reduced (TH) to the weight-free perfect matching (NM) [k ~ b iff ∃ prime p | k with (k/p) | b] ⟺ (SB)
  [divisor-closed C: |C ∩ I| ≤ |C^{[1]} ∩ [1,m]|]. Reduction valid; target FALSE: m=20000, centred-sieve x has 2270 rough
  numbers (lpf > m/2) in I, but every k adjacent to a rough b is 1 or prime, so |N(T)| ≤ π(m)+1 = 2263 < |T|.
  Files: hr_construct.py, nm_counterexample_m20000.txt. General mechanism: Hensley–Richards dense admissible sets.
- Surviving statements: (LAYER) #{k ≤ m: w(k) > t+1} ≤ #{b ∈ I: w(b) > t} (t ≥ 1) — 1.63M tests, min slack 1;
  (Tail21) #{n ≤ L: ω_Q(n) ≥ 2} ≤ #{y < n ≤ y+L: ω_Q(n) ≥ 1} — 3.86M tests at L ≤ 700, holds at the m=20000 window.
  Caveat: (LAYER) for z ≡ 1, t = 1 needs π(x+m) − π(x) ≤ π(m) + 1 + #{k ≤ m: Ω(k) = 2} — true with room but only via
  sieve upper bounds (Brun–Titchmarsh / large sieve), not elementary counting.
- New per-prime-power sufficient condition (dialogue): with θ_b = min(1, 1/w(b)), θ'_k = min(1, 2/w(k)):
  (TH) ⟺ Σ_I min(w,1) ≤ Σ_K min(w,2) + Δ, and both sides expand over prime powers q (z_q := z_p), so (TH) follows from
  (PQ)_q: Σ_{b ∈ I, q | b} min(1, 1/w(b)) ≤ δ_q + Σ_{k ≤ m, q | k} min(1, 2/w(k)),  δ_q = N_I(q) − ⌊m/q⌋ ∈ {0,1},
  for every prime power q with z_q > 0. Writing b = q i', k = q i this is a statement at scale L = ⌊m/q⌋ comparing an interval
  of length L(+1) with [1, L] under f(u) = min(1, 1/(u + w(q))) vs g(u) = min(1, 2/(u + w(q))) — the factor 2 is the slack.
  Tested in pq_test.py (see ledger for the result).

### 07:54 CDT — round 5 status: (PQ′) one prime PROVED (Q25); framework for the general case
- One prime (Q25, audited): Σ_J φ(v_p(i)) ≤ Σ_{[1,L]} φ(v_p(i)) for every nonincreasing φ (telescoping + #{J : p^t | i} ≥ ⌊L/p^t⌋),
  so (PQ′) follows from f_a ≤ g_a. Fails for ≥ 2 primes at the same threshold (extra pq-multiple).
- Finite-difference (Möbius) expansion: any φ of the valuation vector on the weighted primes S has φ(v(i)) = Σ_{d | i, d S-smooth} c_d,
  c_d = mixed finite difference of φ at the exponent vector of d. Hence Σ_J φ − Σ_{[1,L]} φ = Σ_d c_d ε_d(J), ε_d(J) := N_J(d) − ⌊L/d⌋ ∈ {0,1},
  ε_d = 1 ⟺ (x mod d) + (L mod d) ≥ d. (PQ′) ⟺ Σ_d c_d^{(f)} ε_d(J) ≤ Σ_d (c_d^{(g)} − c_d^{(f)})⌊L/d⌋ = Σ_{i≤L} (g−f)(w(i)).
  For a ≥ 1, f_a = 1/(a+u) has c_d of sign (−1)^{ω(d)+1}-ish (alternating derivatives). The free-pattern bound (all ε_d = 1 where
  c_d > 0) is FALSE (C(π(L),2) pairs each ≈ 2/(a(a+1)(a+2)) ≫ L/a), so the arithmetic constraint on which ε_d can be 1
  simultaneously (Σ_{d > L} ε_d ≤ Σ_{i∈J} τ(S-part of i)) is essential.
- P21's Laplace candidate (LAP): Σ_J t^{w+1} ≤ Σ_{[1,L]} t^w for t ∈ (0,1] ⇒ (PQ′) for a ≥ 2 (f_a = ∫e^{-(a+u)s}, g_a = 2f_a there;
  shift by one gives Σ_J 1/(a+w) ≤ Σ 1/(a−1+w) ≤ 2Σ 1/(a+w) when a + w ≥ 2). Tests: 154,637 instances × 14 t, no failure; positive
  slack on the extreme windows for t < 1. Does NOT cover a < 2 (e.g. q = p with z_p ≤ 1), where the min in g matters.

### 08:33 CDT — (LAP) is much tighter than (PQ′); likely false for large L
- adv_window.py / adv_window2.py: objective-driven CRT windows. (PQ′): ≥ 35% relative slack at L = 10^5 for a ∈ [0.5, 3].
  (LAP) with all primes ≤ L weighted: 0.7% slack at t = 0.01 (L = 10^5). Mechanism: LHS ≈ tR + t²N₁′, RHS ≈ 1 + tπ(L) + t²N₂ with
  R − π(L) the Hensley–Richards excess; slack/RHS ≈ 1/(tπ) − (R−π)/π + t(N₂−N₁′)/π, minimised over t ≈ 2√(N₂−N₁′)/π − (R−π)/π,
  and 2√(N₂−N₁′)/π ~ √(ln L lnln L / L) → 0 while (R−π)/π ~ c/ln L. So (LAP) should fail for L ≳ 10^6 (run in progress).
  Consequence: the Laplace route (P21's candidate) cannot prove (PQ′) for a ≥ 2 in general; a proof of (PQ′) must keep the min(1,·)
  structure / trade slack across thresholds, and must survive windows with π(L)(1 + c/ln L) weight-free elements.

### 09:11 CDT — D7: (LAP) is FALSE (L = 10^6 certificate)
- adv_window3.py: centred sieve (class 0 for p ≤ 1000) + greedy classes minimising Σ (1−t)t^{c+1} over positions with c ≤ 1 (t = 0.01),
  CRT over all primes ≤ 10^6 → window with 80,436 elements free of all primes ≤ L (π(L) = 78,498; excess 1938 = 2.5%).
  Exact evaluation: Σ_J t^{w+1} > Σ_{n≤L} t^{Ω(n)} for t ∈ [0.005, 0.015] (t=0.005: 405.03 vs 398.77). So the Laplace
  candidate fails; any route to (PQ′) for a ≥ 2 through Σ_J t^{w+1} ≤ Σ_{[1,L]} t^w is dead. Predicted by the slack formula
  1/(tπ) − (R−π)/π + t(N₂−N₁′)/π (both terms ~ L^{-1/2} vs excess ~ 1/ln L).
- What survives: the layer-cake form with slack traded across thresholds. For a ≥ 1: (PQ′) ⟺ ∫_0^{1/a} #{J: w < 1/s − a} ds ≤
  ∫_0^1 #{[1,L]: w < 2/s − a} ds. Positive integrand only on plateaus where the [1,L]-count is stuck at a low level (e.g. z ≡ 1,
  a = 1: s ∈ (2/3, 1) gives R − 1 − π(L) ≈ excess), negative part ≈ N₂/6 ≫ excess. A proof needs an explicit upper bound for
  #{i ∈ J : w(i) < τ} (large sieve / Montgomery–Vaughan: ≤ 2L/ln L for the weight-free count when all primes ≤ L are weighted)
  against counting lower bounds on [1,L]; fractional weights complicate the sieve condition. This is the honest remaining program.

### 12:05 CDT — round 6 status; AF flow relaxation; a cleaner 0/1 form
- Q26: AF for |P| ≤ 3 is trivial (only multiples of pqr carry units). af_flow_test.py: the flow relaxation of AF (units of k → b with
  some pair of S(k) dividing b, capacity (ω(b)−1)⁺, forest constraint dropped) is feasible on dense/random/symmetric windows for
  m ≤ 3000 with P = primes ≤ m/2, ≤ m, ≤ √m; capacity ≈ 3.3 × demand. So (DTH) has large slack; the 0/1 difficulty is not capacity.
- 0/1 (TH) ⟺ (SI) B₀ − A₀ ≤ Δ + B_{≥2}; with B₀ − A₀ = Σ_{∅≠S⊆P} (−1)^{|S|+1} δ_{∏S} and Δ = Σ_{p∈P} Σ_{j≥1} δ_{p^j}, the |S| = 1
  terms cancel: 0/1 (TH) ⟺ Σ_{S⊆P, |S|≥2} (−1)^{|S|+1} δ_{∏S} ≤ Σ_{p, j≥2} δ_{p^j} + #{k ≤ m : Ω_P(k) ≥ 2}.
  For the symmetric window (b₀ divisible by all of P) the subsets with ∏S > m contribute Σ_{d | P#, d ≤ m} μ(d) (a restricted Mertens
  sum), so that adversary is harmless; general windows need the alternating structure of δ over the divisor lattice.
- P22 (Pro) intermediates: LP forest dual certificate; Fano-plane obstruction to any single global forest (= D8); shifted-sieve lemma
  attempts for c = 3, 4; prime-set moment LP. Decision: this is the last round on the linear bound; rotate slot 1 afterwards.

### 12:51 CDT — COUNTING CERTIFICATES (dialogue): see engine/briefs/erdos708_counting_certificate.md (principle proved; LP evidence; explicit family C_r with proved dual feasibility; C_2 proves the 0/1 hinge inequality for P = all primes ≤ m up to m ≈ 10^48).

### 14:12 CDT — P23: two-anchor certificate fails for P = primes in [53,653] at m = 10^8 (V_2 = 1,595,615 < W_ω = 1,602,217); V_r for r = 2..6: [(2, 1595615), (3, 2266053), (4, 2845025), (5, 3364142), (6, 3843681)]. Anchors must be chosen adaptively (for P without small primes, more anchors cost little). Theorem A (P22) remains the all-m 0/1 result.

### 16:02 CDT — constant improvement (Q29 idea + dialogue computation): θ = 1/(4H) gives the one-level condition G(4H)^k H^ρ/ρ! ≤ 1/(2(k+1)); with exact minimal ρ*_j the budget satisfies (A*+1)/H ≤ 8.98 for all sampled L ≤ 2^(2·10^5) (constant_check.py); with H_RS = max(4, lnln L + B₁ + 1/ln²L) (Rosser–Schoenfeld) ≤ 12.75. Asymptotic floor 2e + 2/(e ln 2) ≈ 6.5. Missing for a theorem: an analytic proof of (A*+1)/H ≤ 9 (or 10) for all L beyond a finite range, plus interval-arithmetic certification of the finite range.
