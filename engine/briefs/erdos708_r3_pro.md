# ATTACK — Erdős Problem #708, round 3: the bounded regime a_n < 8n³ (campaign structure, TEMPLATE v2.2)

## The problem (Erdős 1992 §1; Erdős–Surányi 1959; $100)
g(n) = least g such that for every 1 < a_1 < … < a_n and every x ≥ 0, some (at most) g integers in I = {x+1, …, x+a_n}
have product divisible by a_1 ⋯ a_n. Known: g(2) = 2, g(3) = 4, g(4) ≥ 5, g(5) ≥ 6, g(n) ≥ (2−o(1))n. Asked: g(n) ≤ 2n?

## What is now PROVED (2026-09-03; all machine-verified; use freely) — m := a_n, P := ∏a_i
G1 (counting) for d ≤ m: #{a ∈ A : d | a} ≤ ⌊m/d⌋ ≤ #{b ∈ I : d | b}. Whole interval: P | m! | ∏I.
G2 (atoms) q_p(a) = p^{v_p(a)}; pairwise coprime; ∏ = a. Per-prime placement: for each prime p, the atoms of p from distinct
   a's can be given DISTINCT multiples in I with enough p-valuation (sort exponents descending; the j largest come from j
   distinct a's divisible by p^{e_j}, so ⌊m/p^{e_j}⌋ ≥ j). Elements used for different primes may coincide: safe, because
   capacities are per prime.
G3 (bins) a set of small atoms with product f ≤ m/H has ≥ ⌊m/f⌋ ≥ H multiples in I; if the total number of demands
   (large atoms + bins) is ≤ H, every bin gets a private multiple outside the large-atom positions, and P | ∏B, |B| ≤ H.
G4 (Theorem A) g(n) ≤ n(⌈log₂2n⌉ + ⌈log₂⌈log₂2n⌉⌉ + 2): next-fit bins, and per a at most 2κ+1 demands because κ+1 pairwise
   coprime factors > T = m/H would multiply beyond m (T^{κ+1} > m when m^κ > H^{κ+1}); parameters r = ⌈log₂2n⌉, s = ⌈log₂r⌉,
   H = n(r+s+2), κ = ⌊(r+s+1)/2⌋.
G5 (Theorem B) g(n) ≤ (2+o(1)) n √(ln n/ln ln n): maximal merging of bins (any two bins multiply above T) gives
   D ≤ min(Σω(a_i), 2n ln m/ln(m/H) + 1), and (1/n)Σω(a_i) ≤ [ln(m/n) + (t−1)e ln(1+ln m)]/ln t for every t > 1
   (identity t^{ω(k)} = Σ_{d|k sqfree}(t−1)^{ω(d)}, distinctness of the a_i, AM–GM).
G6 (Theorem C — the long-interval case is DONE) if m ≥ 8n³ then with C = m/(2n): every a has at most one atom > C and
   splits into two coprime parts, either (atom > C, cofactor < 2n) or (two parts ≤ C, by the two-bin packing lemma: integers
   ≤ C with product ≤ C^{3/2} split into two classes with products ≤ C); large atoms placed per prime (G2), small parts get
   private multiples (≥ 2n each, ≤ 2n−1 forbidden). Hence 2n elements suffice and the split-assignment statement S holds.
G7 (exact tools) min|B| for any concrete (A, x) is computable exactly (DP over capped valuation vectors); we will re-run
   every finite claim. The Erdős–Surányi extremal family (pair products of ℓ primes within a factor √2, the common multiple u
   in the middle of the interval) has m ≈ p² with n = C(ℓ,2) ≈ (0.4p/ln p)²/2, i.e. m ≈ n(ln n)²·const ≪ 8n³ — it lies INSIDE
   the remaining regime, and there the minimum is 1 + ℓ(ℓ−3) + O(1) = (2−o(1))n.
G8 (the exact obstruction to O(n) in G5) an a_i may have ≈ √(ln n/ln ln n) "medium" atoms (each ≤ T but pairwise products
   > T) and the bin scheme pays one element per bin; a linear bound needs medium atoms of DIFFERENT a_i to share
   representatives (an element divisible by p^e q^f can serve a p-atom of one a and a q-atom of another).
G9 (traps that killed earlier attempts) a shared element contributes its valuations once (B is a set); "all a ≤ m/2 get
   distinct multiples in an interval of length m" is FALSE (van Doorn–Li–Tang 2026: only min(k, ⌈2√k⌉) disjoint pairs are
   guaranteed in an interval of length 2·max); "take a sub-solution and repair with two points" fails
   (A' = {2,4,8,10,12}, I = {1..16}, B' = {8,12,15,16}, a_6 = 16 needs 2^4 from two elements of I∖B' — impossible).

## Targets, in order of value
T1 Prove S (⇒ g(n) ≤ 2n) for m < 8n³ — this is now the WHOLE problem. Natural first sub-target: extend G6's threshold
   downward (e.g. m ≥ c·n² or m ≥ c·n^{1+ε}), by a k-bin packing that uses the per-prime sharing of G2/G8 for medium atoms.
T2 g(n) ≤ C·n for an explicit constant C (any linear bound): combine G6 (m ≥ 8n³) with a new argument for m < 8n³, where
   now ln m ≤ ln(8n³) = O(ln n) — note G5's second bound gives D ≤ 2n ln m/ln(m/H) + 1, so with H = εm... find the right H.
T3 g(n) ≤ (2+ε)n for m < 8n³ and n large (the (2+o(1))n question).
T4 A counterexample: an (A, x) with m < 8n³ and min|B| > 2n (give it explicitly; we will check it by exact DP).

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public
web, connected sources, previous conversations, or project contexts. Assume for purposes of this task that S is true
for m < 8n³ and provable; work iteratively until a proof survives adversarial audit, or deliver the strongest of T2–T4.
Partial progress does not count unless it implies exactly one of T1–T4.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: (i) sharpen the packing: with m < 8n³ every atom is < 8n³, so atoms are "small
  numbers" — use the per-prime placement (G2) for ALL atoms of size > m/(2n) and pack the rest; count how many atoms per a
  exceed m/(2n) when m < 8n³; (ii) exploit that in the bounded regime ln m = O(ln n) and apply G5's machinery with H = 2n,
  computing exactly when D ≤ 2n fails and what structure the failing instances must have; (iii) a matching/flow
  formulation of S on the "medium" atoms with capacities, and a Hall-type condition proved from G1 for m < 8n³;
  (iv) induction on n that controls the sub-solution (it must avoid the unique multiples of the removed elements);
  (v) an adversarial team searching for T4 counterexamples among structured A (pair/triple products of primes, prime
  powers, mixed) with m just below 8n³ and near the Erdős–Surányi family, testing each by exact DP.
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- Use adversarial agents throughout: every candidate proof is checked for G9, for hidden distinct-multiple assumptions,
  and for capacity double-use at a single element. Reject status reports and "routine" claims.
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first wave
  fails.

Return only when a complete proof of one of T1–T3 has been found and survives adversarial audit, or T4 with the exact
instance, or (failing all) the strongest rigorously proved derivation and its exact remaining gap. Do not return a bounded
verification alone, a heuristic, or an explanation of why the problem is hard. Do not search the web to determine whether
the statement is open, and do not answer that it is open. Budget note: if you approach four hours, wrap up and return the
strongest derivation rather than fail silently.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; the split rule and the
assignment rule as algorithms we can implement; what a Lean formalisation needs. A check that cannot fail counts as no check.
