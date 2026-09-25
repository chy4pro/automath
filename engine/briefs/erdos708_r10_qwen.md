# MICRO-LEMMA — Erdős Problem #708, round 10 (single-shot): asymptotics of the r-anchor certificate value

## Setting (all proved, use freely)
m ≥ 2, P = all primes ≤ m, ω(n) = number of distinct prime factors, W_c(m) := Σ_{n≤m} (ω(n) − c)⁺. For a fixed set R = {p_1 < … < p_r} of the
first r primes define the certificate c_d = (−1)^{|A|} for d = ∏_{a∈A} a (A ⊆ R, |A| ≥ 2), c_d = (−1)^{|A|+1} for d = q ∏_{a∈A} a (q prime, q ∉ R,
A ⊆ R, A ≠ ∅), c_d = 0 otherwise. PROVED: Σ_{d|n} c_d = (|A₀(n)|−1)⁺ + |Q₀(n)|·[A₀(n) ≠ ∅] ≤ (ω(n)−1)⁺, where A₀(n) = R ∩ {p | n}, Q₀(n) = the other
prime factors. Its value is V_r(m) := Σ_{c_d>0} c_d ⌊m/d⌋ − Σ_{c_d<0} |c_d| (⌊m/d⌋ + 1), and PROVED: Σ_{b=x+1}^{x+m} (ω(b)−1)⁺ ≥ V_r(m) for every x ≥ 0.
Known for r = 2: V_2(m) = ⌊m/6⌋ + Σ_{5≤q≤m/2} (⌊m/2q⌋ + ⌊m/3q⌋ − ⌊m/6q⌋ − 1), and V_2(m) − W_2(m) = −(1/3) m ln ln m + (29/18 − M/3) m + o(m)
(M = Meissel–Mertens constant), so the r = 2 certificate proves W_2(m) ≤ V_2(m) only for m below ≈ 10⁴².

## Targets, in order of value
T1 PROVE the asymptotic formula for general fixed r: V_r(m) = m ln ln m · (1 − ∏_{a∈R} (1 − 1/a)) + κ_r m + o(m), with κ_r explicit (in terms of M,
   the p_i and the subset sums), and the error term made explicit (O(m/ln m) or better) with an explicit constant.
T2 Using T1 and W_c(m) = m ln ln m + (M − c) m + o(m) (prove this too, with explicit error), determine for each r the largest constant c and the
   range of m for which the r-anchor certificate proves W_c(m) ≤ V_r(m); in particular show that for every FIXED r and every fixed c the
   inequality fails for all large m (so fixed anchors cannot give an absolute constant), and quantify how r must grow with m
   (r = r(m) → ∞) to keep V_{r(m)}(m) ≥ W_c(m) for a fixed c — or show that no choice r(m) works because the 2^r subset terms cost too much.
T3 The same for the anchor set R = the r smallest primes of an arbitrary prime set P ⊆ [2, m] (P need not contain small primes), with
   the main term expressed through Σ_{p∈P} 1/p.

## Task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web or other
sources. Every claimed lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; every constant explicit; every finite computation
stated so it can be re-run. Do not return a heuristic or an explanation of why the problem is hard.
