# ATTACK — Erdős Problem #1212, strengthened infinite path — ROUND 2 (campaign structure, TEMPLATE v2.2)

## The problem
Let G be the graph on V = { (x,y) : x,y ≥ 1 integers, gcd(x,y) = 1 } with (x,y) ~ (x',y') iff |x−x'| + |y−y'| = 1.
A vertex is ADMISSIBLE if min(x,y) > 1 and at least one coordinate is composite. Prove that G contains an infinite
simple path all of whose vertices are admissible.

## Known givens — all PROVED (round 1 + dialogue, every item machine-checked); use freely
G1 (parity compression) An even–odd vertex has no admissible vertical neighbour; an odd–even vertex has no admissible
   horizontal neighbour; turns happen only at odd–odd vertices. Equivalent problem: an infinite simple path in the
   COARSE grid of odd–odd points (step 2), where a coarse point is open iff it is coprime and not prime–prime, and a
   coarse edge between (x,y),(x+2,y) is open iff gcd(x+1,y) = 1 (the midpoint is then automatically admissible since
   x+1 is even and > 2); symmetrically for vertical coarse edges.
G2 (leaf lemma) (n,n+1) has at most one admissible neighbour; no infinite admissible path lives in |y−x| ≤ 1.
G3 (run lemma) A horizontal run on composite row Y over [X,X'] is admissible iff no prime of Y divides any x in
   [X,X']; so X'−X < lpf(Y). Symmetric for columns. Rails all divisible by one fixed prime are impossible.
G4 (no bounded band) Both coordinates are unbounded along any admissible infinite path.
G5 (factorial shift) If Q is a multiple of lcm(1..M) and 2 ≤ a ≠ b ≤ M then gcd(Q+a,Q+b) = gcd(a,b) and Q+a is
   composite; hence any finite coprime lattice path in [2,M]² translates by (Q,Q) to an admissible path with all
   coordinates composite. Arbitrarily long finite admissible paths exist. (König does not apply: starts move outward.)
G6 (rough twin composites) For A = ∏_{p≤B} p the numbers 4A⁴ ± 1 are composite, differ by 2, and have all prime
   factors > B: 4A⁴−1 = (2A²−1)(2A²+1), 4A⁴+1 = (2A²−2A+1)(2A²+2A+1).
G7 (bounded clusters) For a finite prime set P with L = ∏P, the set of points with a common factor in P has only
   finite ∗-connected components: the lines x = kL+1 and y = kL+1 contain none of them.
G8 (periodic criterion) For T = (A,B), z = (x,y) coprime, D = Bx − Ay ≠ 0, g = gcd(A,B): every z + kT is coprime iff
   rad(D) | rad(g). No translation-periodic admissible path exists with T = (m,m); exhaustive searches found no
   periodic corridor for T = (L,L), L ∈ {6,30,210,2310}, |y−x| ≤ 1000.
G9 (exact coarse densities) Under random translation an odd–odd point is coprime with density ∏_{p≥3}(1−1/p²) = 8/π²;
   two adjacent coarse points are both non-coprime with density 1 − 2·8/π² + ∏_{p≥3}(1−2/p²) ≈ 0.0241; for a finite
   set S the all-open density is ∏_{p≥3}(1 − |S mod p|/p²). Obstacles at different vertices are NOT independent: the
   same prime p recurs at vertices differing by elements of pℤ².
G10 (machine evidence) In [2,N]² the admissible graph has one giant component (plus its mirror) whose share of the
   admissible vertices grows: 14.1% (N=2000), 27.3% (4000), 35.3% (8000); admissible density → 6/π² ≈ 0.608 above the
   Z² site threshold 0.5927. An explicit admissible simple path of length 6151 from (1064,919) to (5000,1333) was found
   running along adjacent odd semiprime rows (899 = 29·31, 901 = 17·53, 893 = 19·47) with switches between composite
   columns — "semiprime highways".

## The two routes that remain, stated exactly
R-A (Peierls) It suffices to prove: Σ over simple closed ∗-contours Γ in the coarse grid surrounding the origin of the
   density of translates t such that every vertex of t+Γ is closed is < 1 − 8/π². Then some coarse point is open and
   not enclosed by a closed contour, its open component is infinite (planar separation), and expanding coarse edges
   yields the path. G7 controls the repeated-prime labels from any finite prime set; tail primes have small Σ p^{−2};
   what is missing is a multi-scale bound uniform in the contour length that handles the recurrence of one prime along
   a contour (a prime p can close at most one vertex per residue class of pℤ², i.e. at most ⌈|Γ|/p⌉-ish vertices in a
   row of the contour — make this precise and sum).
R-B (explicit highways) Build the path explicitly: rows Y = q·r with primes q, r both larger than the length of the
   horizontal runs used on them, columns X = s·t similarly; choose the corner residues by CRT so every run avoids the
   multiples of the rail's primes; the difficulty is proving that a suitable next rail always exists within reach, which
   requires only elementary sieve bounds (Brun/Selberg upper bounds for the number of bad candidates in a window, and a
   lower bound for rough composites in a window) — no unproved prime-gap input is allowed.

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation, and reasoning, without searching the public
web, connected sources, previous conversations, or project contexts. Assume for purposes of this task that a complete
affirmative proof exists. Work iteratively until a correct proof has been reached. Round 1 (four hours) established
G1–G10 and stopped at R-A; do not spend agents re-deriving them.

Partial progress does not count unless it implies exactly the resolution of the entire problem above. Reductions to
unproved conjectures (prime gaps, twin primes, Schinzel), bounded computations, and candidate paths without a proof
that they continue forever are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio: R-A with the recurrence of a single prime along a contour handled by the
  residue-class counting above; R-A with a coarse-graining (renormalisation) of the grid into blocks of side L = ∏_{p≤B} p
  so that G7 makes small primes harmless and only primes > B contribute, with Σ_{p>B} 1/p² as the parameter; R-B with
  explicit CRT-chosen semiprime rails and elementary sieve bounds; a hybrid where R-B supplies the open seed and R-A
  only needs to rule out enclosure at large scales; and a "descent" argument proving that for every R the admissible
  vertices with |v| ≥ R contain an explicit path from radius R to 2R.
- Do not tell most agents the currently favored approach; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at a lemma equivalent in strength to the original problem is NOT close to completion.
- Keep several incompatible routes alive across rounds; cross-pollinate only after independent agents have exposed
  each route's real strengths and gaps.
- Use adversarial agents throughout: every candidate proof is checked for gaps, hidden conditionals, handwaving,
  circular use of an equivalent statement, and especially for treating obstacle events at different vertices as
  independent. Reject status reports, vague optimism, and any claim that an unproved statement is "routine."
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first
  wave fails. Do not return because approaches fail or agents report theorem-strength gaps. Produce a complete proof if
  one survives audit; otherwise report only the strongest rigorously proved derivation and its exact remaining gap.

Return only when a complete proof has been found and survives adversarial audit. Do not return a reduction, partial
result, isolated missing lemma, "best effort" summary, or an explanation of why the problem is difficult. Do not search
the web to determine whether the problem is open, and do not answer that it is open.

## Output contract (ours, applied AFTER the audit passes)
Numbered lemmas, each step elementary and independently checkable; the verification path (for R-B: the explicit path
algorithm and its first 200 vertices; for R-A: the explicit contour estimate with all constants, and the resulting
explicit open seed point); every finite computation stated so it can be re-run; what a Lean formalisation needs.
A check that cannot fail counts as no check.
