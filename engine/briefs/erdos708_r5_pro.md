# ATTACK — Erdős Problem #708, round 5: the per-prime-power inequality (PQ) ⇒ (TH) ⇒ g(n) ≤ 18n (campaign structure, TEMPLATE v2.2)

## The statement to prove — (PQ′), a comparison of an interval with [1, L]
Fix weights 0 ≤ z_p ≤ 1 on the primes (finitely many nonzero) and w(k) := Σ_p z_p v_p(k) (completely additive).
For a real parameter a ≥ 0 put f_a(u) := min(1, 1/(a+u)) and g_a(u) := min(1, 2/(a+u)) = min(1, 2 f_a(u)) (u ≥ 0; f_0(0) := 1).
Prove: for every L ≥ 1, every interval J of L consecutive positive integers, every admissible w and every a ≥ 0,
        Σ_{i∈J} f_a(w(i)) ≤ Σ_{i=1}^{L} g_a(w(i)).                                                             (PQ′)
Only the values a = w(q) = j·z_p for prime powers q = p^j are needed, but (PQ′) for all a ≥ 0 is the clean target.

## Why (PQ′) suffices (all steps PROVED and checked; use freely)
(TH) is the hinge inequality Σ_{k≤m}(w(k)−2)⁺ ≤ Σ_{b∈I}(w(b)−1)⁺, I = {x+1,…,x+m}; it implies g(n) ≤ 18n (R1–R6 below).
R7 (exact form) (TH) ⟺ Σ_{b∈I} min(w(b),1) ≤ Σ_{k≤m} min(w(k),2) + Δ, Δ := Σ_{b∈I} w(b) − Σ_{k≤m} w(k) ≥ 0.
R8 (expansion over prime powers) with z_q := z_p for q = p^j, w(n) = Σ_{q | n} z_q; θ_b := min(1, 1/w(b)), θ′_k := min(1, 2/w(k)):
    Σ_I min(w,1) = Σ_q z_q Σ_{b∈I, q|b} θ_b,   Σ_K min(w,2) = Σ_q z_q Σ_{k≤m, q|k} θ′_k,   Δ = Σ_q z_q δ_q,
    δ_q := #{b∈I : q|b} − ⌊m/q⌋ ∈ {0,1}. Hence (TH) follows from
    (PQ)_q:  Σ_{b∈I, q|b} min(1, 1/w(b)) ≤ δ_q + Σ_{k≤m, q|k} min(1, 2/w(k))   for every prime power q with z_q > 0.
R9 (rescaling) writing b = q i′ and k = q i, w(q i) = w(q) + w(i) = a + w(i) with a = w(q) = j z_p; the i′ form an interval J of
    length ⌊m/q⌋ + δ_q and the i run over [1, ⌊m/q⌋]. Since f_a ≤ 1, the δ_q extra element is paid by δ_q, so (PQ′) with
    L = ⌊m/q⌋ gives (PQ)_q. Thus (PQ′) ⇒ (PQ) ⇒ (TH) ⇒ g(n) ≤ 18n.
R1–R6 (from round 3, all proved): fractional cover LP τ* with y_b ∈ [0,1]; strong duality τ* = max_z [Σ_{a∈A} w_z(a) − Σ_{b∈I}(w_z(b)−1)⁺];
    z_p ≤ 1 suffices; extreme points have ≤ |P| fractional coordinates; |P| < 16n when m = a_n < 8n³; for m ≥ 8n³ two-n suffice
    (known theorem). (TH) ⇒ τ* ≤ 2n ⇒ |B| ≤ 2n + |P| < 18n.

## What is already PROVED about (PQ′) (use freely)
G1 (single prime, a ≤ 1) If w = z v_p (one prime), then with Δf_t := f_a(z(t−1)) − f_a(zt) ≥ 0, Δg_t likewise, the counts
    #{i∈J : v_p(i) ≥ t} ≥ ⌊L/p^t⌋ = #{i≤L : v_p(i) ≥ t} give Σ_J f_a ≤ L f_a(0) − Σ_t Δf_t ⌊L/p^t⌋ and Σ_{[1,L]} g_a = L g_a(0) − Σ_t Δg_t ⌊L/p^t⌋.
    Always Δg_t ≤ 2Δf_t, and Δg_t = 0 while a + zt ≤ 2. For a ≤ 1 the t = 1 term contributes +Δf_1⌊L/p⌋ = (z/(a+z))⌊L/p⌋, which
    dominates the negative terms Σ_{t≥2} Δf_t ⌊L/p^t⌋ ≤ (z/4)·L/(p(p−1)). So (PQ′) holds for one prime and a ≤ 1; the case a > 1
    has the extra budget L(g_a(0) − f_a(0)) = L·(min(1,2/a) − 1/a) > 0 and is routine but NOT yet written out — do it.
G2 (x = 0) J = [1, L] is trivial since f_a ≤ g_a.
G3 (tests) (PQ) checked on 355,166 random and adversarial instances (m ≤ 500, 0/1, fractional, p^{−θ} weights; x = 0, random,
    x ≡ −1 mod ∏S, and windows centred at a number divisible by high powers of all weighted primes), every prime power q:
    no failure; minimum slack 0 only at x = 0 with a single prime power. (TH) itself: 2.1 million instances, no failure.
    On two extreme windows built from dense admissible patterns (m = 20000 and m = 100000, x with 4298 resp. 21599 digits,
    containing 2270 resp. 9735 integers with no prime factor ≤ m/2, more than π(m)+1) and nine weight choices, (PQ) has
    minimum slack ≥ 0 (equality only at a prime power q > m/2) and (TH) has slack ≥ 0.18 m.
G4 (tight cases) equality in (PQ′) forces J = [1,L]-like behaviour: a + w(i) ≤ 1 for all i ∈ J, i.e. f = g on J.

## Routes that are DEAD (proved false; do not let agents rediscover them)
D1 Weight-free divisor transport: the statement "there is an injection φ: [1,m] → I with (k/p) | φ(k) for some prime p | k"
    (round-4 target (NM)/(SB)) is FALSE: for m = 20000 the window above has 2270 integers with no prime factor ≤ m/2, and every
    k adjacent to such an integer is 1 or prime, so Hall fails (|N(T)| ≤ π(m)+1 = 2263 < 2270). Any proof of (PQ′)/(TH) must use
    the weights, not divisibility alone.
D2 Single-threshold level-set domination: "#{i≤L : w(i) ≥ 2τ} ≤ #{i∈J : w(i) ≥ τ}" (which would give (PQ′) by the layer-cake
    formula f_a(u) = ∫_0^1 [a+u < 1/s] ds) is FALSE: on the m = 100000 window with z ≡ 1 on primes ≤ m/2 it fails at τ = 1 by 142
    and at τ = 1/2 by 5275, while (PQ) and (TH) hold there with room. So a layer-cake proof must trade slack between thresholds.
D3 The two-layer sieve statement #{n≤L : ω_Q(n) ≥ 2} ≤ #{y<n≤y+L : ω_Q(n) ≥ 1} is FALSE (m = 100000 window: 90299 > 90265).
D4 Same-threshold sum domination Σ_{k≤m}(w(k)−1)⁺ ≤ Σ_{b∈I}(w(b)−1)⁺ is FALSE (m = 1000, S = {23,29,31}, window centred at
    23²·29²·31²): the hinge shift 2 → 1 is essential.
D5 Per-prime(-power) domination of counts is not sufficient for (TH) (the thresholds differ); it IS the whole story for one prime.
D6 Prefix-sum domination Σ_{i≤r} w(x+i) ≥ Σ_{i≤r} w(i) (true: the difference is w(C(x+r,r))) does not imply the hinge inequality.

## Targets, in order of value
T1 Prove (PQ′) for all admissible w and all a ≥ 0 (⇒ g(n) ≤ 18n, the first linear bound with an absolute constant).
T2 Prove (PQ)_q for the values a = w(q) only, or (TH)/(BH) directly by any other route.
T3 Prove (PQ′) for 0/1 weights (z_p ∈ {0,1}), and say exactly what is missing for fractional weights.
T4 A counterexample to (PQ′) with a of the form w(q), or to (TH): explicit L, J, z, a (we re-check it). Then say what a repaired
    inequality would be.
T5 Prove (PQ′) with g_a(u) = min(1, c/(a+u)) for some explicit c > 2 (⇒ (TH) with 2 replaced by c ⇒ g(n) ≤ (c+16)n).

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public web,
connected sources, previous conversations, or project contexts. Assume for purposes of this task that (PQ′) is true and
provable; work iteratively until a proof survives adversarial audit, or deliver the strongest of T2–T5.
Partial progress does not count unless it implies exactly one of T1–T5.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: (i) induction on the number of weighted primes, tracking BOTH sides exactly when a
  prime is added (the multiples of p in J form a scaled interval of length ⌊L/p⌋ or ⌊L/p⌋+1 on which w is shifted by z_p —
  a recursive structure at scale L/p; the induction hypothesis must be used at the smaller scale for both sides, not termwise);
  (ii) the layer-cake route with slack traded between thresholds: f_a(u) = ∫_0^1 [a+u < 1/s] ds, g_a(u) = ∫_0^1 [a+u < 2/s] ds,
  so (PQ′) ⟺ ∫_0^1 ( #{i∈J : w(i) < 1/s − a} − #{i≤L : w(i) < 2/s − a} ) ds ≤ 0; D2 says the integrand is positive for some s,
  so bound the positive part by an explicit sieve estimate (Brun–Titchmarsh / large-sieve upper bounds for integers in a
  window free of the weighted small primes, with explicit constants) and the negative part from below by counting;
  (iii) convexity/concavity of the difference Σ_J f_a − Σ_{[1,L]} g_a in each z_p and in a — where is the extreme case?;
  (iv) exact finite verification of (PQ′) for small L and a search for the tightest cases (which J, z, a make the slack small?)
  to see the structure a proof must respect; (v) an adversarial team trying to break (PQ′): windows centred at highly divisible
  numbers, windows with dense admissible patterns of weight-free integers, fractional weights on many primes, a near 1.
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- Use adversarial agents throughout: every candidate proof is checked for hidden use of J = [1,L], for confusing the factor 2
  in g with the additive shift in (TH), for using a single-threshold level-set comparison (D2), and for weight-free transport (D1).
  Reject status reports and "routine" claims.
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first wave fails.

Return only when a complete proof of one of T1–T3/T5 has been found and survives adversarial audit, or T4 with the exact
instance, or (failing all) the strongest rigorously proved derivation and its exact remaining gap. Do not return a bounded
verification alone, a heuristic, or an explanation of why the problem is hard. Do not search the web to determine whether the
statement is open, and do not answer that it is open. Budget note: if you approach four hours, wrap up and return the
strongest derivation rather than fail silently.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation stated
so it can be re-run; what a Lean formalisation needs. A check that cannot fail counts as no check.
