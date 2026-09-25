# ATTACK — Erdős Problem #708, round 4: the hinge inequality (TH) ⇒ g(n) ≤ 18n (campaign structure, TEMPLATE v2.2)

## The statement to prove — (TH), an inequality about additive functions on intervals
For every integer m ≥ 1, every integer x ≥ 0, and every choice of weights 0 ≤ z_p ≤ 1 on the primes p, put
   w(k) := Σ_p z_p · v_p(k)   (v_p = p-adic valuation; w is completely additive; only finitely many z_p matter).
Prove:  Σ_{k=1}^{m} (w(k) − 2)⁺  ≤  Σ_{b=x+1}^{x+m} (w(b) − 1)⁺        (TH)
where t⁺ = max(t, 0). Equivalently (subtract Σ w over both ranges):
   #-weighted form: Σ_{b∈I} min(w(b), 1) − Σ_{k≤m} min(w(k), 2) ≤ Σ_{b∈I} w(b) − Σ_{k≤m} w(k),   I = {x+1, …, x+m}.
A weaker statement suffices for the application: (BH) — the same inequality with the left sum restricted to any subset
A ⊆ {1, …, m}, and z supported on the primes dividing ∏A.

## Why it matters (all steps PROVED and checked; use freely)
Context: g(n) = least g such that for every 1 < a_1 < … < a_n and every x ≥ 0 some (at most) g integers in
I = {x+1, …, x+a_n} have product divisible by ∏a_i (Erdős–Surányi 1959; Erdős asks for 2n; known: (2−o(1))n ≤ g(n) ≤
(2+o(1)) n √(ln n/ln ln n), and 2n suffices when a_n ≥ 8n³; a bound C·n with an ABSOLUTE constant is unknown).
R1 (fractional cover LP) with m = a_n, P = primes dividing ∏A, R_p = Σ_a v_p(a):
   τ* = min Σ_b y_b  s.t. Σ_b v_p(b) y_b ≥ R_p (p ∈ P), 0 ≤ y_b ≤ 1.  Feasible (y ≡ 1, since ∏A | m! | ∏I).
R2 (strong duality) τ* = max_{z ≥ 0} [ Σ_{a∈A} w_z(a) − Σ_{b∈I} (w_z(b) − 1)⁺ ].
R3 (z_p ≤ 1 suffices) for z_p ≥ 1 the objective is linear in z_p with slope R_p − S_p ≤ 0, S_p := Σ_{b∈I} v_p(b), because
   #{b ∈ I : p^j | b} ≥ ⌊m/p^j⌋ ≥ #{a ∈ A : p^j | a} for every j.
R4 (rounding) an optimal extreme point has ≤ |P| fractional coordinates; rounding them up gives a SET B ⊆ I with
   ∏A | ∏B and |B| ≤ τ* + |P|.
R5 (few primes) if m < 8n³ then |P| < 16n (∏_{p∈P} p ≤ ∏A ≤ m^n < (8n³)^n while (16n+1)! > (8n)^{8n} > (8n³)^n).
R6 (assembly) (BH) ⇒ Σ_a w(a) ≤ 2n + Σ_a (w(a)−2)⁺ ≤ 2n + Σ_b (w(b)−1)⁺ ⇒ τ* ≤ 2n ⇒ |B| ≤ 2n + |P| < 18n for
   m < 8n³; for m ≥ 8n³ the known theorem gives 2n. Hence (BH) ⇒ g(n) ≤ 18n for all n.
Sanity facts about (TH): (a) x = 0 is trivial (I = [1,m]); (b) z supported on one prime: LHS = Σ_{j≥3}⌊m/p^j⌋ ≤
   Σ_{j≥2} #{b∈I : p^j | b} = RHS; (c) Σ_{b∈I} w(b) ≥ Σ_{k≤m} w(k) for every z ≥ 0 (prime-power counts in any interval
   of length m are ≥ those in [1,m]); (d) 2.1 million random and adversarial tests (m ≤ 600; 0/1, fractional, and
   p^{−θ} weights; x = 0, random, and x ≡ −1 mod ∏S so that x+1 is divisible by a whole block of primes): no
   counterexample; the minimum slack 0 occurs only at x = 0 with a single prime.
Traps: the hinge thresholds differ (2 on the left, 1 on the right) — the inequality is NOT implied by per-prime-power
   domination alone, and it is not a majorization statement about the multiset {w(b)}; the danger is an interval whose
   weight is spread thinly (many b with 0 < w(b) ≤ 1) while [1,m] concentrates weight on few smooth numbers.

## Targets, in order of value
T1 Prove (TH) (⇒ g(n) ≤ 18n, the first linear bound with an absolute constant).
T2 Prove (BH) (the A-restricted form) — same consequence.
T3 Prove (TH) for 0/1 weights only, and say exactly what is missing for fractional weights (the dual optimum need not be
   0/1, so this alone does not close R6).
T4 A counterexample to (TH) or (BH): explicit m, x, z (we will re-check it); then say what a repaired inequality would be.
T5 Prove (TH) with the constant 2 on the left replaced by some explicit c ≥ 2 (⇒ g(n) ≤ (c+16)n).

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public
web, connected sources, previous conversations, or project contexts. Assume for purposes of this task that (TH) is true
and provable; work iteratively until a proof survives adversarial audit, or deliver the strongest of T2–T5.
Partial progress does not count unless it implies exactly one of T1–T5.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: (i) write w = Σ_{p,j} z_p [p^j | ·] and compare I with [1,m] prime power by
  prime power, using that for each q = p^j the multiples of q in I are a translate-and-truncation of those in [1,m];
  build a bijection or a coupling between I and [1,m] under which w does not drop by more than... (find the right
  transport statement: e.g. a map φ: [1,m] → I with w(φ(k)) ≥ w(k) − 1 and |φ⁻¹(b)| ≤ ... ); (ii) induction on the number
  of primes with z_p > 0, adding one prime at a time and tracking how both sides change; (iii) reduce to 0/1 weights by
  convexity/concavity in each z_p (the objective is piecewise linear in z; check whether extreme points are 0/1 after
  the restriction 0 ≤ z_p ≤ 1 from R3); (iv) an exact finite verification for small m as a guide, and a search for
  the tightest cases (which m, x, z make the slack small?) to see the structure a proof must respect; (v) an adversarial
  team trying to break (TH) with fractional weights on many primes and intervals starting at x ≡ −1 (mod ∏S).
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- Use adversarial agents throughout: every candidate proof is checked for hidden use of x = 0 symmetry, for confusing
  the thresholds 1 and 2, and for treating per-prime domination as sufficient. Reject status reports and "routine" claims.
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first
  wave fails.

Return only when a complete proof of one of T1–T3/T5 has been found and survives adversarial audit, or T4 with the exact
instance, or (failing all) the strongest rigorously proved derivation and its exact remaining gap. Do not return a bounded
verification alone, a heuristic, or an explanation of why the problem is hard. Do not search the web to determine whether
the statement is open, and do not answer that it is open. Budget note: if you approach four hours, wrap up and return the
strongest derivation rather than fail silently.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation
stated so it can be re-run; what a Lean formalisation needs. A check that cannot fail counts as no check.
