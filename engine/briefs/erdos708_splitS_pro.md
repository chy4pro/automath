# ATTACK — Erdős Problem #708 via the split-assignment statement S (campaign structure, TEMPLATE v2.2)

## The problem (Erdős, Hardy–Ramanujan J. 15 (1992) §1; Erdős–Surányi 1959; $100)
g(n) = least g such that for every 1 < a_1 < … < a_n and every x ≥ 0, some g integers in I = (x, x + a_n] have product
divisible by a_1 ⋯ a_n. Known: g(2) = 2, g(3) = 4, g(n) ≥ (2−o(1))n. Asked: g(n) ≤ 2n? or (2+o(1))n? No upper bound of any
kind is recorded (none in terms of n alone; the trivial Σ_i ω(a_i) depends on a_n).

## The statement to prove — S (split assignment). S implies g(n) ≤ 2n immediately.
S: for every A and I as above there exist, for each a ∈ A, a coprime factorisation a = d_1(a)·d_2(a) (d_2 = 1 allowed) and
a map β from the ≤ 2n "demands" {d_1(a), d_2(a)} to elements of I such that
   (capacity) for every element b ∈ I and every prime p:  Σ_{demands d with β(d) = b} v_p(d) ≤ v_p(b).
Then B = image(β) satisfies |B| ≤ 2n and ∏A | ∏B (each element's valuations are used at most once — B is a SET).

## Known givens — all PROVED or machine-verified; use freely
G1 (counting) for every integer d ≤ a_n: #{a ∈ A : d | a} ≤ ⌊a_n/d⌋ ≤ #{b ∈ I : d | b}. In particular for each prime power
   p^j: #{a : p^j | a} ≤ #{b ∈ I : p^j | b}.
G2 (per-prime dominance, proved) hence for each prime p there is an injection φ_p : {a : p | a} → I with v_p(φ_p(a)) ≥ v_p(a)
   (nested Hall). Consequence: with the FINEST split (one demand per prime power of a) the capacity assignment always
   exists — but that uses up to Σ_a ω(a) elements. S asks for the same with ≤ 2 demands per a.
G3 (decoupling) the capacity constraint couples two demands only if they share a prime. Demands that are prime powers
   never interfere across primes. Hence S holds whenever every a has at most 2 distinct prime factors (finest split =
   2-split, G2 applies prime by prime). Any counterexample to S must use a's with ≥ 3 distinct primes, where at least one
   demand is composite and competes for two capacities at once (e.g. demand 6 and demand 4 both wanting 12).
G4 (the extremal family, Erdős–Surányi) primes p_1 < … < p_l with 2p_1² > p_l², A = {p_i p_j}, x chosen so that u = x + ⌊a_n/2⌋
   is the unique common multiple of every a with v_{p_i}(u) = 1. Every solution needs ≥ 1 + l(l−3) + O(1) elements. S is
   satisfied here by the split (p_i, p_j): u absorbs one demand per prime, the rest go to single-prime multiples.
   Exact DP values: l=3 (17,19,23), x=74072: min|B| = 4; l=4 (41,43,47,53), x=26348553: min|B| = 6.
G5 (machine evidence) S verified feasible by exact backtracking on the two Erdős–Surányi instances above, on
   A=(10,12,15,20), x=50 (min|B| = 5, so g(4) ≥ 5) and A=(5,10,12,15,20), x=50 (min|B| = 6, so g(5) ≥ 6), and on 965,773
   random instances with n ≤ 5, a_n ≤ 60: 0 infeasible.
G6 (the trap that killed two previous attempts) any argument that picks "a multiple of each a" or "a multiple of each
   part" and then adds valuations as if the chosen elements were distinct is wrong: a shared element counts once. Also
   FALSE: "all a ≤ a_n/2 can be matched to distinct multiples in an interval of length a_n" — van Doorn–Li–Tang (2026)
   show only min(m, ⌈2√m⌉) disjoint (a, multiple) pairs are guaranteed in an interval of length 2·max, optimally.
   Mandatory test for every algorithm: on G4 with l=3 it must output ≥ 4 elements and say where the 4th comes from.

## Targets, in order of value
T1 Prove S (⇒ g(n) ≤ 2n, the $100 question).
T2 Prove S with k demands per a for an explicit k ≥ 3 (⇒ g(n) ≤ k·n) — a first linear bound, already new.
T3 Prove g(n) ≤ F(n) for any explicit F depending on n alone (e.g. O(n log n)) — first explicit bound, new.
T4 A counterexample to S (a concrete A, x where no 2-split assignment exists) together with the DP value min|B| for it;
   if min|B| ≤ 2n there, S is the wrong route and you must say what replaces it.

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public
web, connected sources, previous conversations, or project contexts. Assume for purposes of this task that S is true
and provable; work iteratively until a proof survives adversarial audit, or deliver T2/T3/T4.
Partial progress does not count unless it implies exactly one of T1–T4.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: (i) choose d_1(a) = the largest prime-power divisor of a (or the part of a
  above √a_n) and prove the composite d_2-demands pack by a greedy in decreasing order of d_2 with a Hall/König argument
  on the "multiples of d_2 with free capacity"; (ii) LP duality / fractional assignment then rounding, using G1 as the
  supply–demand inequality for every d; (iii) induction on the number of distinct primes with G3 as the base case
  (≤ 2 primes per a), merging one prime at a time; (iv) network flow with prime-capacitated nodes; (v) an adversarial
  team searching for counterexamples to S among a's with ≥ 3 primes and scarce composite multiples (demand 6 vs 4 at
  12-type conflicts), testing each candidate exactly.
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- Use adversarial agents throughout: every candidate proof is checked for G6, for hidden use of distinct multiples,
  and for capacity double-use at a single element. Reject status reports and "routine" claims.
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first
  wave fails.

Return only when a complete proof of one of T1–T3 has been found and survives adversarial audit, or T4 with the exact
instance, or (failing all) the strongest rigorously proved derivation and its exact remaining gap. Do not return a
bounded verification alone, a heuristic, or an explanation of why the problem is hard. Do not search the web to
determine whether the statement is open, and do not answer that it is open. Budget note: if you approach four hours,
wrap up and return the strongest derivation rather than fail silently.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; the split rule and the
assignment rule stated as algorithms we can implement; what a Lean formalisation needs. A check that cannot fail counts
as no check.
