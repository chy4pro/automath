# ATTACK — the contour estimate ML for Erdős Problem #1212 (single-shot variant, TEMPLATE v2.2, round 3)

## The problem (a single precise estimate; proving it resolves Erdős #1212)
Coarse grid Λ = ℤ², φ(i,j) = (2i+1, 2j+1). A coarse vertex v is CLOSED if gcd(2i+1, 2j+1) > 1 (prime–prime
closures have density 0 and may be ignored in upper bounds). For a finite set S ⊂ Λ let
   δ(S) = density of translations t ∈ Λ such that every vertex of t+S is closed.
Let C_n be the set of simple closed ∗-contours (steps of sup-norm ≤ 1) of length n surrounding the origin; write
N_n = |C_n| (N_n ≤ 8·7^{n−1} trivially). Prove:
   (ML)  there is q < 1/8 (or any explicit decay F(n) with Σ_n N_n F(n) < 1 − 8/π² ≈ 0.18943) such that
         δ(Γ) ≤ q^n for every Γ ∈ C_n and every n.
Then, by the Peierls criterion (given below), the open component of a suitable translate of the origin is infinite,
which yields the infinite admissible path of Erdős #1212.

## Known givens — all PROVED (rounds 1–2 + dialogue; every finite claim machine-checked); use freely
G1 (exact density) For finite S ⊂ Λ: density of translates with every vertex of t+S COPRIME is
   ∏_{p≥3} (1 − |S mod p| / p²); single vertex: 8/π². (CRT over primes; independence across primes is exact.)
G2 (Peierls criterion) If Σ_{n} Σ_{Γ∈C_n} δ(Γ) < 1 − 8/π² then some translate has an open origin not surrounded by a
   closed contour, hence an infinite open component, hence an infinite admissible path. So ML suffices.
G3 (single-prime recurrence) For Γ ∈ C_n and a prime p, every residue class a ∈ (ℤ/pℤ)² contains at most ⌊n/p⌋
   vertices of Γ (at most 1 if n < p): congruent vertices are ≥ p apart in sup norm, so the arcs between k of them
   have total length ≥ kp. Corollary: a prime p > n can close at most one vertex.
G4 (prime-simple contours) If each vertex of Γ is closed by a distinct odd prime, the density is ≤ σ₃^n with
   σ₃ = Σ_{p≥3} p^{−2} = 0.2022474…; with primes ≥ 5 only, σ₅ = 0.0911363….
G5 (bounded clusters) For a finite set P of odd primes with L = ∏P, every ∗-connected component of P-closed vertices
   lies in one L×L cell between the lines i ≡ 0 (mod L), j ≡ 0 (mod L). In particular a contour of length
   n > 4L cannot be closed by primes of P alone.
G6 (structure of closures) A vertex v is closed by p iff v ≡ a_p (mod p) for the unique class a_p with
   φ(a_p) ≡ (0,0) (mod p), i.e. iff both coordinates of φ(v) are ≡ 0 mod p; the set of p-closed vertices is the
   lattice coset a_p + pℤ², one vertex per p×p block.
G7 (numerics) 1 − 8/π² = 0.189431…; Σ_{p≥3} 1/p² = 0.20225; Σ_{p≥5} 1/p² = 0.09114; Σ_{p≥7} 1/p² = 0.05114;
   Σ_{p≥11} 1/p² = 0.03073; Σ_{p≥13} 1/p² = 0.02247.

## Why the naive product fails and what must be handled
Closures at different vertices of Γ are not independent: a single prime p closes every vertex of Γ in the coset
a_p + pℤ², and by G3 a long contour can be closed by few small primes many times each (up to ⌊n/p⌋ vertices per
prime). The estimate must charge each vertex either to a "new" prime (cost ≤ 1/p² each, summable as in G4) or to a
repeated prime (cost 0 for the repeat but a strong geometric constraint: the repeats sit on a p-periodic lattice, and
by G5 finitely many small primes cannot close a contour by themselves).

## Current task statement
Give a rigorous standalone proof of (ML) — or of any explicit F with Σ N_n F(n) < 1 − 8/π² — using your own
knowledge and reasoning, without searching the public web, connected sources, previous conversations, or project
contexts. Assume for purposes of this task that a complete proof exists. Work iteratively until a correct proof has
been reached. Human experts have not written this estimate down; that is not evidence that it is hard — it is a
finite-combinatorics-plus-CRT statement.

Partial progress does not count unless it implies exactly ML (or a variant sufficient for G2). Restating G1–G7,
bounded computations, and heuristics are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents:
  (i) charging scheme: order the vertices of Γ along the contour; when a vertex is closed by a prime not used before,
      pay ≤ 1/p² (G1 exact); when closed by a used prime, the vertex must lie in the same p-coset as an earlier one,
      which forces the contour to travel ≥ p in sup norm between them (G3) — bound the number of contours compatible
      with a given pattern of repeats and sum;
  (ii) multi-scale / coarse-graining: fix B; primes ≤ B cannot close a contour of length > 4∏_{p≤B} p by themselves
      (G5), so at least a proportion of vertices must be closed by primes > B, each such prime closing ≤ ⌊n/p⌋
      vertices; use Σ_{p>B} p^{−2} → 0 as the parameter and choose B to beat the contour count;
  (iii) exact density for the union of closures: δ(Γ) ≤ Σ over assignments f: V(Γ) → primes of ∏_{p} p^{−2·[p ∈ f(V)]}
      with the constraint that vertices sharing a prime are congruent mod p (each prime contributes 1/p² ONCE per
      coset it closes, independent of how many contour vertices lie in that coset) — organise the sum by the set of
      distinct primes used and the number of cosets per prime;
  (iv) entropy comparison: show the number of contours of length n that admit a closing assignment using only
      primes with total cost ≥ q^n is at most (1/q)^{n}·(something summable), i.e. a "cost vs count" argument;
  (v) an alternative sufficient statement: prove that the expected number (over translations) of closed ∗-contours
      surrounding the origin is < 1 − 8/π², counting contours by their vertex set rather than by length;
  (vi) if ML fails as stated, find the sharpest true version (e.g. F(n) = n^{−c}·q^{n/log n}) and check whether it
      still beats the contour count.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at an equal-strength statement is NOT close to completion.
- Use adversarial agents throughout: every candidate bound is checked for treating closures as independent, for
  double-counting cosets, for ignoring that a prime closes a whole coset, and for hidden dependence between the
  primes used; test every bound numerically on small contours (n ≤ 12) against the exact density from G1.
- Require concrete inequalities with explicit constants — not plans.
- Do not stop after the first wave fails.

Return a complete proof if one survives adversarial audit. If none does, return instead: (1) the strongest
rigorously proved derivation you reached, as numbered lemmas — e.g. ML proved for contours whose closing primes are
all ≥ B, or an explicit bound δ(Γ) ≤ F(n) with its exact summation constant, or a proved bound on the number of
cosets a contour of length n can meet; (2) the exact remaining gap as a precise open statement; (3) every
machine-checkable artefact you built (explicit small-contour density tables, counts N_n for n ≤ 14, worst-case
contours). Do not return an empty answer, a bare statement of failure, a status report, or an explanation of why the
problem is hard. Do not search the web to determine whether the statement is open, and do not answer that it is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation
stated so it can be re-run; what a Lean formalisation needs. A check that cannot fail counts as no check.
