# ATTACK — Erdős Problem #708, round 6 (single-shot): the forest-transfer statement AF — prove it or break it

## Setting (all proved, use freely)
P a finite set of primes, m ≥ 1, x ≥ 0, I := {x+1,…,x+m}. For an integer n let S(n) := {p ∈ P : p | n} and ω(n) := |S(n)|.
The distinct-prime hinge inequality
   (DTH): Σ_{k≤m} (ω(k)−2)⁺ ≤ Σ_{b∈I} (ω(b)−1)⁺
implies the 0/1 case of a hinge inequality that gives g(n) ≤ 18n for the Erdős–Surányi function of Problem #708. (DTH) has no known
counterexample (millions of tests). Facts: for every d, #{b∈I : d | b} ≥ ⌊m/d⌋ = #{k≤m : d | k}. Windows I exist (Hensley–Richards)
with MORE integers free of all primes ≤ m than [1,m] has (explicit: m = 10^6, 80,436 vs π(m)+1 = 78,499); any argument that ignores
which prime factors the b's have will fail on them.

## The statement AF (arithmetic forest transfer)
For each k ≤ m with ω(k) = d ≥ 3 choose a forest F_k with d−2 edges on the vertex set S(k) (e.g. a spanning tree minus an edge).
Each edge e = {p,q} ∈ F_k is a "unit"; it may be sent to any b ∈ I with pq | b. AF asserts: the F_k and the destinations can be
chosen so that (a) each pair (b, e) is used at most once, and (b) for every b the set of edges sent to b is a forest on S(b).
Then Σ_k (ω(k)−2)⁺ = #units ≤ Σ_b (ω(b)−1)⁺, i.e. (DTH). By Rado's theorem (direct sum over b of the graphic matroids of K_{S(b)}),
for fixed forests F_k AF holds iff for every family U of units: Σ_{b∈I} rank_{graphic}({e_u : u ∈ U, e_u ⊆ S(b)}) ≥ |U|.
Single-label capacity is automatic: #{k≤m : pq | k} ≤ #{b∈I : pq | b}. A single global forest for all k cannot work (averaging).

## Targets, in order of value
T1 Prove AF for all P, m, x (⇒ (DTH) ⇒ 0/1 hinge inequality).
T2 Prove AF when |P| ≤ 3 (all m, x), with the explicit choice of forests and destinations.
T3 Prove (DTH) directly for |P| ≤ 3 by counting (inclusion–exclusion on the surpluses δ_d := #{b∈I : d|b} − ⌊m/d⌋ ∈ {0,1}).
T4 A counterexample to AF (explicit P, m, x, and a family U violating the Rado condition for EVERY choice of forests), or to (DTH)
   itself (we re-check it). Think about windows where I contains many integers free of small primes while [1,m] contains many
   integers with ≥ 3 prime factors from P.
T5 Prove that AF reduces to a statement about the surplus pattern (δ_d)_{d} only, and state that statement exactly.

## Task statement
Give a rigorous standalone proof using your own knowledge, computation and reasoning, without searching the public web or other
sources. Assume for purposes of this task that AF is true and provable; work until a proof survives your own adversarial audit,
or deliver the strongest of T2–T5. Partial progress does not count unless it implies exactly one of T1–T5. Do not return a bounded
verification alone, a heuristic, or an explanation of why the problem is hard. Do not answer that the statement is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation stated so it
can be re-run. A check that cannot fail counts as no check.
