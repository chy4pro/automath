# SELECTION SCAN 09-03/04 (after the #708 publication) — honest register

Read (statement + additional text + comment counts) for #1108, #1137, #1142, #1184, #1186, #1188, #1194, #1199, #1200,
#1201, #1203, #1206, #1209, #1210, plus the top-40 of the attention-scored list (dominated by famous hard problems:
sum-product, Sidon, Collatz, $500–$10000 prizes — not for us).

## Slot 1 decision: STAY on #708 (rounds 3+)
Reason: the reduction to a_n < 8n³ turned the $100 question into a bounded-regime packing statement; both engines have
momentum (P19 is already at "maximal merging leaves ≤ 2n−1 factors; remaining issue = a weighted Hall condition; LP
optimum ≤ n with factor-2 rounding" after 30 min). A resolution would be a full Erdős-problem solution. Rotate only if two
rounds produce nothing new.

## Reserve slot-1 candidates (same machinery family)
- #709 (Erdős–Surányi f(n): distinct multiples a_i | x_i in an interval of length f(n)·a_n; known (log n/log log n) ≪ f(n) ≪ n^{1/2}).
  Improving the upper bound below n^{1/2} uses exactly our per-prime/bin tools; risk: van Doorn's group is active on the
  family (solved #650 with ChatGPT + Aristotle; lower bound comment on #709, 2026-03).
- #1210 (Σ_{a∈A} 1/(n−a) ≤ Σ_{p<n} 1/p + O(1) for pairwise coprime A ⊂ [1,n)): elementary-looking, but Erdős says the
  statement in [Er77c] was "not quite correct" — must pin the statement from [Er80] before any engine hour.
- #1203 (F(n) = max_k ω(n+k)·log log k/log k → ∞?): my heuristic — for typical n, k ≈ (log n)^A with typical
  ω(n+k) ≈ log log n gives F(n) ≳ log log log n/A, so the claim is plausible but the growth is triple-log; proving it for
  ALL n needs "every interval of polylog length contains an integer with ω ≥ log log n/log log log n" — deep sieve
  territory. Not for us.
- Rejected: #1108 (k-th powers among sums of factorials — Diophantine, hopeless), #1137/#1142 (prime gaps / n−2^k
  primes — analytic), #1184 (Dickman-function asymptotics), #1186 (δ_k for monochromatic APs — computational SAT-type,
  crowded), #1194 (perfect difference sets, 8 comments), #1199 (Owings' conjecture — Ramsey theory), #1200
  (Erdős–Ruzsa prime covering — the same Jacobsthal wall as #1212), #1201 (11 comments), #1206 (Sidon cubes — active
  literature 2024–26), #1209 (trivial counterexamples already noted).

## Slot 2 candidates (certain, data)
- #1188: F(x) = number of minimal distinct covering systems with moduli ≤ x — exact small values with our #1189 tooling
  (needs residue enumeration, not only moduli sets); check the 5 comments/1 claim first.
- #463: we already computed (n − F(n))/√n records (repo erdos-357 data) — an OEIS submission needs the owner's account.
- #1189 follow-up: I(k) for k = 9 (needs the k=8 pipeline scaled; feasibility unknown).
