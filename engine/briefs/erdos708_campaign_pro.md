# ATTACK — Erdős Problem #708 (Erdős–Surányi, 1959; $100 prize): the function g(n) — campaign structure, TEMPLATE v2.2

## The problem (statement verbatim from Erdős, "Some of my forgotten problems in number theory", Hardy–Ramanujan J. 15 (1992), §1)
Let g(n) be the smallest integer for which, if 1 < a_1 < a_2 < … < a_n is any sequence of n integers, then for every x ≥ 0
one can find g(n) integers among x+1, x+2, …, x+a_n whose product is a multiple of a_1 a_2 ⋯ a_n; i.e. there are integers
x < u_1 < u_2 < … < u_{g(n)} ≤ x + a_n with u_1 ⋯ u_{g(n)} ≡ 0 (mod a_1 ⋯ a_n).
QUESTION (Erdős–Surányi; Erdős offers $100): is g(n) ≤ (2+o(1))n? Perhaps even g(n) ≤ 2n?

## Known givens — every item PROVED or machine-verified; use freely
G1 g(2) = 2 (Gallai), g(3) = 4 (Erdős–Surányi 1959; Gallai gave g(3) ≥ 4).
G2 (lower bound, Erdős–Surányi) g(n) ≥ (2−o(1))n. Construction: primes p_1 < ⋯ < p_l with 2p_1² > p_l², A = {p_i p_j : i<j},
   n = C(l,2), a_n = p_{l−1}p_l. Choose x so that u := x + ⌊a_n/2⌋ ≡ 0 (mod p_1⋯p_l) with v_{p_i}(u) = 1. Since every
   p_i p_j > a_n/2, u is the ONLY multiple of every p_i p_j in the interval; every other element of the interval is
   divisible by at most one p_i, with valuation ≤ 2 (one multiple of p_i² when p_i² < a_n, none of p_i³). Each prime needs
   valuation l−1; u supplies 1; so ≈ l−3 further elements per prime are forced: |B| ≥ 1 + l(l−3) + O(1) = (2−o(1))n.
   VERIFIED by exact dynamic programming: l=3, primes 17,19,23 (n=3, a_n=437, x=74072): min|B| = 4; l=4, primes
   41,43,47,53 (n=6, a_n=2491, x=26348553): min|B| = 6 (the p_i²-multiples for 41,43,47 each save one element). For
   random x the same A needs only n elements — the extremal x is the one placing u in the middle.
G3 (why the obvious induction fails) Let u be the unique multiple of a_n in the interval, and B' a solution for
   A' = A∖{a_n} in the same (longer) interval. If u ∉ B', then B' ∪ {u} works, giving g(n) ≤ g(n−1)+1 — but u ∈ B' is
   exactly what G2's construction forces (u is the unique multiple of every a_i). Any induction must control which
   elements the sub-solution uses.
G4 (structure of the extremal examples, heuristic) An element of the interval that is divisible by several a_i's but with
   too small valuations is "shared" and is what forces extra elements. Every a ≤ a_n has at most one prime factor > √a_n.
   For a_i with ≥ 3 prime factors within a factor 2 of each other, multiples of pairs p_i p_j exist in the interval besides
   u and can serve two primes at once — such A's are cheaper for us; the pair-products of G2 are the tight case.
G5 (finite verification) For any concrete (A, x), min|B| is computable exactly by dynamic programming over capped
   valuation vectors (states ∏_p (E_p+1), E_p = v_p(∏A)); we will re-run every finite claim you make.
G6 (no upper bound is recorded) Neither Erdős 1992 nor the problem's page records ANY upper bound for g(n) — not even a
   linear one. The trivial bound |B| ≤ n + Σ_i ω(a_i) is NOT linear in n. A proof of g(n) ≤ C·n for any constant C is
   therefore already new.

## Targets, in order of value — each is a complete deliverable on its own
T1 g(n) ≤ 2n (or (2+o(1))n): the full $100 question.
T2 g(n) ≤ C·n for an explicit constant C (e.g. 3n or 4n): a new theorem; state C explicitly.
T3 g(n) ≤ n·(1 + h(n)) with an explicit slowly growing h.
T4 Exact values: g(4), g(5) with proof (upper bound argument + extremal example verified by G5).
T5 If you believe the answer is NO: an explicit family with |B| ≥ (2+c)n, checkable by G5 for its smallest member.

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public
web, connected sources, previous conversations, or project contexts. Assume for purposes of this task that a complete
proof of T1 exists; if you cannot reach it, deliver the strongest of T2–T5 that survives audit. Work iteratively until a
correct proof has been reached.

Partial progress does not count unless it implies exactly one of T1–T5. Reductions to unproved conjectures (prime gaps,
Cramér, Jacobsthal-type conjectures), bounded computations alone, and heuristic arguments are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: (i) charging arguments — each a_i pays for at most two elements of B, via a
  matching / Hall-type argument between the a_i and multiples in the interval, with a separate treatment of the "shared"
  elements of G3; (ii) prime-by-prime greedy: cover the valuation demand E_p for each prime using elements of highest
  valuation, and bound the total count by Σ_i (number of distinct primes of a_i that are "large" for a_i) + (small-prime
  overhead), proving the small-prime overhead is O(n); (iii) induction on n with a strengthened hypothesis that forbids
  the sub-solution from using a prescribed set of ≤ k elements (so that u ∉ B'); (iv) the LCM viewpoint: replace A by the
  set of prime powers p^{v_p(∏A)} and reduce to a covering problem on the interval; (v) an adversarial team building
  worst cases beyond pair-products (triples, prime powers, mixed) and testing every proposed inequality on them with G5.
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at a lemma equivalent in strength to the original problem is NOT close to completion.
- Keep several incompatible routes alive across rounds; cross-pollinate only after independent agents have exposed each
  route's real strengths and gaps.
- Use adversarial agents throughout: every candidate proof is checked for gaps, hidden conditionals, handwaving, and
  especially for double-counting an element of B (a set!) or for assuming the multiples chosen for different a_i are
  distinct. Reject status reports, vague optimism, and any claim that an unproved statement is "routine."
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first wave
  fails. Do not return because approaches fail or agents report theorem-strength gaps.

Return only when a complete proof of one of T1–T5 has been found and survives adversarial audit, or (failing that) with
the strongest rigorously proved derivation and its exact remaining gap. Do not return a bounded verification alone, a
heuristic, or an explanation of why the problem is hard. Do not search the web to determine whether the statement is
open, and do not answer that it is open. Budget note: if you approach four hours, wrap up and return the strongest
derivation rather than fail silently.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; for T4 the extremal (A, x)
in full so that G5 can re-run it; for T5 the smallest member of the family in full; what a Lean formalisation needs.
A check that cannot fail counts as no check.
