# ATTACK — Erdős Problem #709 (Erdős–Surányi matching function f(n)), round 1 (TEMPLATE v2.3, inequality type, prove-or-refute)

## The statement (erdosproblems.com/709, verbatim)
Let f(n) be minimal such that, for any A = {a_1,…,a_n} ⊆ [2,∞) ∩ ℕ of size n, in any interval I of f(n)·max(A) consecutive integers there
exist distinct x_1,…,x_n ∈ I such that a_i | x_i. Obtain good bounds for f(n), or even an asymptotic formula.
KNOWN: Erdős–Surányi (1959): (log n)^c ≪ f(n) ≪ n^{1/2}. Site comments (2026): f(n) ≫ log n/log log n (from van Doorn's lower bound on the
Erdős–Pomerance F(n,m) with A = {2,…,n+1}, using F(n,m) ≤ f(n)·n), and f(n) ≫ √(log n/log log n) via #711. The UPPER bound n^{1/2} has not
been improved since 1959 (checked 09-05: arXiv 2607.10431 concerns F(n)−f(n,n), not this upper bound).

## Reformulation (PROVED, trivial)
Fix A, m := max(A), L := f·m, I a window of L consecutive integers. A system of distinct representatives exists iff Hall's condition holds:
for every B ⊆ A, N_I(B) := #{x ∈ I : some a ∈ B divides x} ≥ |B|. Failure means a 'deficient' B: few integers in I divisible by members of B.
So f(n) ≤ f_0 iff for every A of size n and every window of length f_0·max(A), every B ⊆ A has N_I(B) ≥ |B|.
Counting inputs available: for a single d, ⌊L/d⌋ ≤ N_I(d) ≤ ⌊L/d⌋ + 1; for a set B, inclusion–exclusion over lcm's; N_I(B) ≥ max_{a∈B} ⌊L/a⌋ ≥ ⌊L/m⌋ = f
trivially, so only |B| > f can be deficient; and N_I(B) ≥ Σ_{a∈B}⌊L/a⌋ − Σ_{a<a'∈B}(⌊L/lcm(a,a')⌋+1) (Bonferroni).

## Tools we have proved on the sister problem #708 (product version; use freely)
P1 Two-sided interval counts with LP duality turn such statements into finite 'hinge' inequalities; nonnegative counting certificates.
P2 Sieve lemma for intervals: for pairwise coprime moduli D and a set J of L consecutive integers, #{n ∈ J : ν_D(n) ≥ k} ≥ L e_k/(4(8H)^k) with
   H = e ln(1+ln L) (random thinning + two-term Bonferroni + interval counts), and #{n ≤ L : ν_D(n) ≥ 2k+ρ} ≤ L e_k H^ρ/ρ!.
P3 Cube-root peel: at most two prime factors > L^{1/3} divide an integer ≤ L.
P4 The Erdős–Surányi n^{1/2} argument itself (reconstruct it: pigeonhole on the elements of A that are ≤ √m versus > √m, each large a has ≥ f
   multiples in I and the small ones are handled by counting) — identify exactly where √ enters.

## Coordinator's analysis (test it)
A1 The hard sets A are those with many elements sharing large common factors (lcm structure), e.g. A = {d·1, d·2, …}: then N_I(B) ≈ L/d·(harmonic
   sum) for B = multiples of d. Deficiency needs |B| > N_I(B) ≈ (L/d) Σ_{b∈B} 1/(b/d)·(inclusion–exclusion) — quantify via the 'divisor-density'
   Σ_{a∈B} 1/a with lcm corrections. Hall's condition with the harmonic-sum heuristic suggests f(n) ≪ (log n)^{O(1)} might be true and n^{1/2}
   is far from the truth — decide which.
A2 Fractional relaxation (König): distinct representatives exist iff the fractional matching number is ≥ n; LP duality gives a dual certificate
   (a weighting y on I and a covering of A). This is the analogue of our #708 duality and may give an explicit bound like f(n) ≪ n^{1/2−δ} from
   the two-sided counts alone; test the fractional version numerically for random A and adversarial windows before proving.
A3 Refutation side: find A (e.g. A = {d, 2d, …, nd} for suitable d, or A = multiples of a primorial) and a window x (congruence conditions) with a
   deficient B for L = c·max(A)·n^{c'} — an explicit lower bound f(n) ≫ n^{c'} would be new and important; the current lower bounds are only
   polylog, so the truth is wide open in between.

## Targets (equal rank; prove-or-refute)
T1 PROVE f(n) ≪ n^{1/2−δ} for an explicit δ > 0 (or f(n) ≪ n^{1/2}/(log n)^c), with every constant explicit.
T2 PROVE f(n) ≪ (log n)^{O(1)} (the plausible truth) — via Hall + counting/sieve + duality; state exactly which counting input is needed.
T3 REFUTE polylog: an explicit family (A_n, window) with f(n) ≫ n^{c} for some c > 0 (we re-check by computer at small n — give small instances).
T4 Exact/structured small cases: determine f(n) for n ≤ 6 by a proof (extremal A and windows), and the exact growth for the family A = {2,…,n+1}
   (the Erdős–Pomerance F(n,m) normalised by n) — connect to the known F(n) − f(n,n) results.
Rule: no intermediate statement is used before an adversarial agent has tried to break it on lcm-structured sets A and congruence-defined
windows; status tags PROVED / CONDITIONAL / CONJECTURED; end with 'final claim ← lemmas ← unproved items'.

## Machine facts
M1 (to be produced by us at small n) — none yet; treat f(n) values as unknown; do not invent numerics.

## Current task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; use multiagents
aggressively: (i) reconstruct Erdős–Surányi's n^{1/2} proof and locate the loss; (ii) Hall/LP duality team; (iii) adversary team (lcm-structured
A, congruence windows, small-n exact search by hand); (iv) referee team. Budget: about two hours; then return the strongest rigorously
proved statement with its exact gap.

## Output contract
Numbered lemmas with status tags; every constant explicit; every construction explicit enough to be re-run; what a Lean formalisation needs.
A check that cannot fail counts as no check.
