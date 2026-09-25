# ATTACK — Erdős Problem #708, round 6: the hinge inequality by explicit sieve bounds (campaign structure, TEMPLATE v2.2)

## The statement to prove — (TH) for 0/1 weights first, then fractional
Weights z_p ∈ [0,1] on primes (finitely many nonzero), w(n) := Σ_p z_p v_p(n), I := {x+1,…,x+m}, x ≥ 0.
(TH):  Σ_{k≤m} (w(k)−2)⁺ ≤ Σ_{b∈I} (w(b)−1)⁺.
Proved consequences (use freely): (TH) ⇒ g(n) ≤ 18n for the Erdős–Surányi function (LP duality R1–R6 of round 3; the first
linear bound with an absolute constant). Equivalent forms (all proved):
(E1) (TH) ⟺ Σ_I min(w,1) ≤ Σ_{k≤m} min(w,2) + Δ, Δ := Σ_I w − Σ_{k≤m} w = Σ_q z_q δ_q ≥ 0, δ_q := #{b∈I: q|b} − ⌊m/q⌋ ∈ {0,1} (q prime powers).
(E2) 0/1 weights, P := {p : z_p = 1}, r := Ω_P: (TH) ⟺ (SI): B₀ − A₀ ≤ Δ + B_{≥2}, where B₀ := #{k≤m : r(k)=0}, A₀ := #{b∈I : r(b)=0},
     B_{≥2} := #{k≤m : r(k) ≥ 2}; and B₀ − A₀ = Σ_{∅≠S⊆P} (−1)^{|S|+1} δ_{∏S}.
(E3) 0/1 weights: repeated prime powers peel off, so it suffices to prove the distinct-prime version
     (DTH): Σ_{k≤m} (ω_P(k)−2)⁺ ≤ Σ_{b∈I} (ω_P(b)−1)⁺.
(E4) per prime power q with a := w(q) and L := ⌊m/q⌋, J := {i : q i ∈ I} (an interval of length L or L+1):
     (PQ′)_a: Σ_{i∈J} min(1, 1/(a+w(i))) ≤ Σ_{i≤L} min(1, 2/(a+w(i)))  for all q ⇒ (TH). Proved: one prime (all a); any weights when
     a ≥ max(2, w(L!)/L) (Cauchy–Schwarz: LHS ≤ L/a, RHS ≥ 2L²/(aL + w(L!))).
(E5) layer-cake: for a ≥ 1, (PQ′)_a ⟺ ∫_0^{1/a} #{i∈J : w(i) < 1/s − a} ds ≤ ∫_0^1 #{i≤L : w(i) < 2/s − a} ds.

## Machine facts (use freely)
M1 (TH): 2.1M random/adversarial instances (m ≤ 600), no counterexample; on CRT windows of length 10^5 with π(m)(1+1.5%) integers
   free of all primes ≤ m, slack ≥ 0.18 m. (PQ′): 355k instances × all prime powers, no failure; ≥ 35% slack on those windows.
M2 Dense windows exist: for every L there are windows of length L containing (1 + c/ln L)·π(L) integers free of all primes ≤ L
   (Hensley–Richards; explicit: L = 10^6, 80,436 vs π(L) = 78,498). Any inequality that is linear in such counts at a single
   threshold fails on them.

## Routes that are DEAD (proved false; do not let agents rediscover them)
D1 weight-free divisor transport / injections k ↦ b with (k/p) | b (Hall fails on dense windows: |N(composites)| ≤ m − #rough < #composites).
D2 single-threshold level-set domination #{k≤L : w ≥ 2τ} ≤ #{b∈J : w ≥ τ} (fails at τ = 1 and τ = 1/2 on the 10^5 window).
D3 the two-layer sieve statement #{n≤L : ω_Q ≥ 2} ≤ #{y<n≤y+L : ω_Q ≥ 1} (fails at L = 10^5).
D4 same-threshold sum domination Σ_{k≤m}(w−1)⁺ ≤ Σ_I (w−1)⁺ (fails, m = 1000, S = {23,29,31}).
D7 the exponential/Laplace inequality s Σ_J s^{w} ≤ Σ_{[1,L]} s^{w} (fails at L = 10^6, s ∈ [0.005, 0.015], explicit x with 433,636 digits;
   the dense-window excess ~ π(L)/ln L beats the compensation ~ √(L ln L)). So (PQ′) for a ≥ 2 cannot be reached through a single
   positive Laplace kernel; the min(1,·) structure must be kept.
D8 "one global forest" for the forest-transfer formulation (averaging over r-subsets kills it).

## What a proof must look like (the honest program)
In (E5) the integrand is positive only on "plateaus" where the [1,L]-count is stuck at a low level (example: z ≡ 1, a = 1,
s ∈ (2/3, 1): integrand = A₀ − 1 − π(L) ≈ +π(L)/ln L) and strongly negative elsewhere (s ∈ (1/2, 2/3): ≈ −#{k≤L : Ω(k)=2}).
So: (i) bound the positive part by an explicit upper bound for #{i ∈ J : w(i) < τ} — for 0/1 weights this is the number of
integers in a window of length L free of the primes in P' := {p ∈ P : ...}, i.e. a sieve upper bound (Montgomery–Vaughan large
sieve: #{n ∈ (x, x+L] : (n, ∏_{p∈P'} p) = 1} ≤ L / Σ_{q ≤ √L, q | ∏P'} μ²(q)/φ(q); or Brun–Titchmarsh-type bounds) with explicit
constants; (ii) bound the negative part from below by exact counting on [1,L] (numbers with ≥ 2 factors from P, Legendre-type
counts); (iii) handle small L (where the sieve bound is weak) by a different argument or exact computation; (iv) fractional
weights: replace "w < τ" by the sieve condition "free of primes with z_p ≥ τ" (weaker but sufficient on the J side) and keep
exact counts on the [1,L] side. The alternative 0/1 route is (E3) + the forest transfer AF (Rado criterion); AF is UNTESTED against
dense windows — any use of it must first check Hall/Rado on a window like M2.

## Targets, in order of value
T1 Prove (TH) for 0/1 weights (⇒ via P20 §8 this does NOT yet give fractional; say so) — full proof with explicit sieve constants.
T2 Prove (TH) for all weights (⇒ g(n) ≤ 18n).
T3 Prove (TH_c): Σ_{k≤m}(w(k)−c)⁺ ≤ Σ_I (w(b)−1)⁺ for an explicit absolute constant c > 2 (⇒ g(n) ≤ (c+16)n): the plateaus have
   more room when the left threshold is c.
T4 Prove (TH) with c = C·ln ln m (⇒ g(n) ≤ (16 + C ln ln n + O(1)) n, which would already beat the published (2+o(1))n√(ln n/ln ln n)).
T5 A counterexample to (TH) (explicit m, x, z; we re-check it), or a proof that AF fails on a dense window.

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public web,
connected sources, previous conversations, or project contexts. Assume for purposes of this task that (TH) is true and provable;
work iteratively until a proof survives adversarial audit, or deliver the strongest of T3–T5. Partial progress does not count
unless it implies exactly one of T1–T5. Explicit constants are mandatory: a sieve bound quoted without its constant is not a step.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: (i) the layer-cake + large-sieve program above for 0/1 weights; (ii) the same with the
  weaker target T4 (c = C ln ln m) where crude tail bounds (Σ_{n≤L} 2^{Ω(n)} ≤ C L ln² L, Markov) may suffice; (iii) the forest
  transfer AF with a genuine Rado-condition analysis — first test it on the dense-window structure; (iv) induction on the number
  of weighted primes using the scaled-interval recursion, but with the induction hypothesis applied at scale L/p to BOTH sides;
  (v) an adversarial team building dense windows (CRT: class 0 mod p for p ≤ √L, least-populated class for larger p) and evaluating
  every proposed sub-lemma on them.
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- Use adversarial agents throughout: every candidate proof is checked against D1–D8, for hidden use of I = [1,m], for sieve
  bounds quoted without explicit constants, and for tail bounds that ignore small m.
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first wave fails.

Return only when a complete proof of one of T1–T4 has been found and survives adversarial audit, or T5 with the exact instance,
or (failing all) the strongest rigorously proved derivation and its exact remaining gap. Do not return a bounded verification
alone, a heuristic, or an explanation of why the problem is hard. Do not search the web to determine whether the statement is
open, and do not answer that it is open. Budget note: if you approach four hours, wrap up and return the strongest derivation.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation stated so it
can be re-run; what a Lean formalisation needs. A check that cannot fail counts as no check.
