# ATTACK — Erdős Problem #708, round 5 (single-shot): building blocks for the per-prime-power inequality (PQ′)

## The statement
Weights 0 ≤ z_p ≤ 1 on primes (finitely many nonzero); w(k) := Σ_p z_p v_p(k). For a ≥ 0 let f_a(u) := min(1, 1/(a+u)) and
g_a(u) := min(1, 2/(a+u)) (f_0(0) := 1). Claim (PQ′): for every L ≥ 1, every interval J of L consecutive positive integers,
every admissible w and every a ≥ 0:   Σ_{i∈J} f_a(w(i)) ≤ Σ_{i=1}^{L} g_a(w(i)).
Context (all proved, use freely): (PQ′) implies the hinge inequality Σ_{k≤m}(w(k)−2)⁺ ≤ Σ_{b=x+1}^{x+m}(w(b)−1)⁺, which
implies g(n) ≤ 18n for the Erdős–Surányi function of Problem #708 (first linear bound with an absolute constant).
Facts: for each prime power p^t, #{i∈J : p^t | i} ≥ ⌊L/p^t⌋ = #{i≤L : p^t | i}. (PQ′) is trivial for J = [1,L] since f_a ≤ g_a.
Machine evidence: 355,166 adversarial instances, no failure; minimum slack 0 only for J = [1,L] with a single prime.
DEAD routes (proved false, do not use): (a) any argument that ignores the weights and only uses divisibility (an injection
k ↦ b with (k/p) | b fails for m = 20000 windows with more than π(m)+1 integers free of primes ≤ m/2); (b) a single-threshold
level-set comparison #{i≤L : w(i) ≥ 2τ} ≤ #{i∈J : w(i) ≥ τ} (false at τ = 1 and τ = 1/2 on an explicit window of length 100000).

## Targets, in order of value
T1 Prove (PQ′) in general.
T2 Prove (PQ′) for one prime (w = z v_p, any 0 < z ≤ 1, any a ≥ 0). Known: for a ≤ 1, writing Σ_J f_a = L f_a(0) − Σ_t Δf_t·#{i∈J : v_p(i) ≥ t}
   with Δf_t = f_a(z(t−1)) − f_a(zt) ≥ 0 and using #{…} ≥ ⌊L/p^t⌋, the t = 1 term (Δg_1 = 0 because a + z ≤ 2) dominates the terms
   with Δg_t = 2Δf_t. Complete the case a > 1 (extra budget L(g_a(0) − f_a(0))) with every inequality explicit.
T3 Prove (PQ′) for two primes with 0/1 weights (w = v_p + v_q, or v_p alone with the second prime carrying weight 0): the joint
   distribution of (v_p, v_q) on an interval vs on [1, L] is the first place where the counts of single prime powers do not
   determine everything; say precisely which inequality on joint counts is used.
T4 A counterexample to (PQ′): explicit L, J, z, a (we will re-check it).
T5 Prove (PQ′) with 2 replaced by an explicit c > 2 in g_a (any c gives a linear bound (c+16)n).

## Task statement
Give a rigorous standalone proof using your own knowledge, computation and reasoning, without searching the public web or
other sources. Assume for purposes of this task that (PQ′) is true and provable; work until a proof survives your own
adversarial audit, or deliver the strongest of T2–T5. Partial progress does not count unless it implies exactly one of T1–T5.
Do not return a bounded verification alone, a heuristic, or an explanation of why the problem is hard. Do not answer that the
statement is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation stated
so it can be re-run. A check that cannot fail counts as no check.
