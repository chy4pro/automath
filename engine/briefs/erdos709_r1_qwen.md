# MICRO-LEMMA — Erdős Problem #709, round 1 (single-shot): the Erdős–Surányi upper bound, made explicit

## Setting (pinned from erdosproblems.com/709)
f(n) is minimal such that for any set A = {a_1,…,a_n} ⊆ [2,∞) ∩ ℕ of size n and any interval I of f(n)·max(A) consecutive integers there are
distinct x_1,…,x_n ∈ I with a_i | x_i. Known (Erdős–Surányi 1959): (log n)^c ≪ f(n) ≪ n^{1/2}; lower bound improved to f(n) ≫ log n/log log n (2026).
Reformulation (proved): with m = max(A), L = f·m, distinct representatives exist iff Hall's condition holds: for every B ⊆ A,
N_I(B) := #{x ∈ I : some a ∈ B divides x} ≥ |B|. Counting facts: ⌊L/d⌋ ≤ N_I(d) ≤ ⌊L/d⌋+1 for every d; N_I(B) ≥ ⌊L/a⌋ ≥ f for any a ∈ B, so only
|B| > f can be deficient; Bonferroni N_I(B) ≥ Σ_{a∈B}⌊L/a⌋ − Σ_{a<a'}(⌊L/lcm(a,a')⌋+1).

## Targets, in order of value
T1 PROVE f(n) ≤ C√n with an explicit C (reconstruct the classical argument: split A into small elements a ≤ √m and large ones; each large a has at
   least f multiples in I; handle the small ones by Hall + counting), stating every inequality with constants. Say exactly which step forces √n.
T2 Exact small values: determine f(1), f(2), f(3) (and f(4) if feasible) by proof: give the extremal sets A and windows I attaining the maximum,
   and the matching argument showing no larger interval is needed. (f(1) = 1 trivially; for n = 2, A = {a, b}: an interval of length f·max(A)
   must contain a multiple of a and a different multiple of b — work out the worst case, e.g. a | b.)
T3 A lower-bound construction of your own: an explicit family A_n and window I with a deficient set B for L = c·n^{c'}·max(A) with c' > 0, or a
   proof that no such polynomial deficiency exists for lcm-structured families A = {d·1,…,d·n} (compute N_I(B) for B = the whole set).

## Task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web or other sources.
Every claimed lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; every constant explicit; every finite computation stated so it can
be re-run. Do not return a heuristic or an explanation of why the problem is hard.
