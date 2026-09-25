# ATTACK — Erdős Problem #708 (Erdős–Surányi, 1959; $100 prize): the function g(n) — single-shot variant, TEMPLATE v2.2

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
web or any external source. Assume for purposes of this task that a complete proof of T1 exists; if you cannot reach it,
deliver the strongest of T2–T5 that survives your own adversarial audit. Work iteratively: propose, attack, repair.
Partial progress does not count unless it implies exactly one of T1–T5. Reductions to unproved conjectures, bounded
computations alone, and heuristic arguments are insufficient. Check every candidate proof for double-counting an element
of B (it is a set) and for silently assuming that the multiples chosen for different a_i are distinct (G3).
Return a complete proof if one survives audit. If none does, return instead: (1) the strongest rigorously proved
derivation you reached, as numbered lemmas — for instance g(n) ≤ C·n with explicit C, or g(4) exactly; (2) the exact
remaining gap as a precise open statement; (3) every machine-checkable artefact (extremal (A, x) pairs, inequalities to
test) so it can be re-run. Do not return an empty answer, a bare statement of failure, or an explanation of why the
problem is hard. Do not answer that the problem is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; extremal examples in full;
what a Lean formalisation needs. A check that cannot fail counts as no check.
