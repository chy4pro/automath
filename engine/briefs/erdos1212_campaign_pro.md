# ATTACK — Erdős Problem #1212, strengthened infinite path in the visible-lattice-point graph (campaign structure, TEMPLATE v2.2)

## The problem
Let G be the graph whose vertex set is V = { (x,y) : x >= 1, y >= 1 integers, gcd(x,y) = 1 }, in which
(x,y) and (x',y') are adjacent iff |x - x'| + |y - y'| = 1 (they differ by exactly 1 in exactly one
coordinate). Call a vertex (x,y) ADMISSIBLE if min(x,y) > 1 and at least one of x, y is composite.
Prove: there exists an infinite sequence of pairwise distinct admissible vertices v_0, v_1, v_2, ... with
v_i adjacent to v_{i+1} for every i >= 0 (an infinite simple path in G through admissible vertices only;
since the vertices are distinct, |v_i| -> infinity).

## Known givens — all PROVED (by us, with one-line reasons); use freely, re-derive if you prefer
G1 (why the classical route fails) Without the compositeness condition, the path
   (p_k,p_{k+1}) -> (p_k,p_{k+1}+1) -> ... -> (p_k,p_{k+2}) -> (p_k+1,p_{k+2}) -> ... -> (p_{k+1},p_{k+2})
   over consecutive primes works for k >= 4 (it needs p_{k+2} < 2 p_k). But its corner vertices
   (p_k, p_{k+1}) are prime-prime, hence NOT admissible. So the strengthened problem forbids exactly
   that construction.
G2 (leaf lemma, proved and machine-checked) For n >= 2 the vertex (n, n+1) has at most ONE admissible
   neighbour: (n, n+2) when n is odd, (n-1, n+1) when n is even; the other three neighbours have a common
   factor 2 or equal coordinates. Hence no admissible infinite path uses the band |y - x| <= 1 except
   possibly at its starting vertex. The same holds with x and y exchanged.
G3 (run lemma) On a horizontal run {(x,Y) : X <= x <= X'} with Y composite, all vertices are admissible
   iff gcd(x,Y) = 1 for every x in [X,X']; this forces X' - X < lpf(Y) (least prime factor) and the
   interval to avoid every multiple of every prime factor of Y. Symmetrically for vertical runs at a
   composite X.
G4 (no fixed-prime rails) A staircase whose horizontal-run rows are all multiples of one prime Q and whose
   vertical-run columns are all multiples of one prime P cannot exist: by G3 it needs P < Q (a run between
   consecutive multiples of P must avoid multiples of Q) and Q < P simultaneously.
G5 (no bounded band) Any path confined to a band of finitely many rows y in [Y, Y+m] is cut infinitely often:
   pick one prime factor q_j of each composite row and one of each prime row's neighbour as needed; every x
   divisible by the product of the chosen primes is inadmissible on every row of the band (gcd > 1 on
   composite rows, prime-prime or gcd > 1 on the rest). Hence both coordinates must be unbounded along
   any admissible infinite path.
G6 (diagonal parametrisation) gcd(x, x+d) = gcd(x, d): along the direction y = x + d admissibility
   depends on gcd(x,d) = 1, min(x, x+d) > 1, and compositeness of x or x+d.
G7 (machine evidence, not a proof; dialogue 09-02) In the box [2,N]^2 the admissible subgraph has:
   N = 600: largest component 3,444 vertices, no far-edge component larger than 54;
   N = 2000: one component of 329,016 vertices (39% of all admissible vertices), touching the far edge,
   spanning x in [153,1974], y in [1064,2000]. Admissible-vertex density 0.5742 (N=600), 0.5850 (N=2000),
   with limit 6/pi^2 = 0.6079 > 0.5927 (site-percolation threshold of Z^2). The component containing the
   region {x + y <= 21} is finite (42 vertices). So the expected answer is YES, the path must start far from
   the origin, and its existence is a supercritical-percolation phenomenon that a proof must make explicit.

## Current task statement
Give a rigorous standalone proof of the above using your own knowledge, computation, and reasoning,
without searching the public web, connected sources, previous conversations, or project contexts.
Assume for purposes of this task that a complete affirmative proof exists. Work iteratively until a
correct proof has been reached.

Partial progress does not count unless it implies exactly the resolution of the entire problem above.
In particular, reductions to other unproved conjectures (any unproved statement about prime gaps,
twin primes, or Schinzel's hypothesis is forbidden as an input), computational verification through any
fixed parameters, and candidate paths without a proof that they continue forever are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for
strategy X." Instead:
- Begin with a genuinely diverse portfolio of approaches: substantially different formulations,
  invariants, reductions, algebraic viewpoints, structural inductions, decompositions, embeddings,
  extremal arguments, and computational sanity checks. Families worth separate agents:
  (i) an explicit staircase of short horizontal and vertical runs whose rows and columns are composite
      "rails" chosen by the Chinese remainder theorem, with the primes of the rails growing along the
      staircase so that G3 and G4 are respected (rails of the form P*m with m coprime to the run);
  (ii) rails on which BOTH coordinates are composite, so that only coprimality (a periodic condition)
      has to be arranged, with compositeness supplied by residue classes such as 0 mod 4, 0 mod 9,
      0 mod 25 chosen by CRT;
  (iii) a path following a direction y ~ c x for a suitable rational or irrational c, using G6 and
      the distribution of composites in short intervals (only elementary facts such as Bertrand-type
      bounds proved from scratch are allowed);
  (iv) a periodic-pattern approach: exhibit a finite pattern of moves that, translated by a vector
      (a,b), stays admissible for all translates beyond some point, proving admissibility by congruence
      conditions plus explicit compositeness certificates;
  (v) a "descent from infinity" argument: show that for every large R the admissible vertices with
      |v| >= R contain a path from radius R to radius 2R with an explicit description, then chain;
  (vi) computational exploration of the giant component (G7) to extract a repeating corridor, then a
      proof that the corridor continues.
- Do not tell most agents the currently favored approach; preserve independence in early rounds so
  agents do not converge on the same attractive but incomplete reduction.
- Maintain an explicit registry of approach families, grouped by mathematical idea, not wording. If
  many agents converge on one family, redirect some toward underexplored formulations.
- A route ending at a lemma equivalent in strength to the original problem is NOT close to completion.
  When a route stalls at a theorem-strength missing lemma, mark it blocked; reopen only on a genuinely
  new mechanism, invariant, or construction.
- Keep several incompatible routes alive across rounds; cross-pollinate only after independent agents
  have exposed each route's real strengths and gaps.
- Use adversarial agents throughout: every candidate proof is checked for gaps, hidden conditionals,
  handwaving, and circular use of an equivalent statement; in particular check every claimed coprimality
  along every run, every claimed compositeness, that consecutive vertices really differ by exactly 1 in
  exactly one coordinate, and that the vertices are pairwise distinct. Reject status reports, vague
  optimism, and any claim that an unproved statement is "routine."
- Require concrete lemmas, constructions, equations, or counterexamples to proposed sublemmas.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop
  after the first wave fails. Do not return because approaches fail or agents report theorem-strength gaps.
  Produce a complete proof if one survives audit; otherwise report only the strongest rigorously proved
  derivation and its exact remaining gap.

Return only when a complete proof has been found and survives adversarial audit. Do not return a
reduction, partial result, isolated missing lemma, "best effort" summary, or an explanation of why the
problem is difficult. Do not search the web to determine whether the problem is open, and do not answer
that it is open.

## Output contract (ours, applied AFTER the audit passes)
Deliver the proof as numbered lemmas, each step elementary and independently checkable, plus:
(1) the verification path — an explicit description of the path (a formula or algorithm producing v_i),
    the first 200 vertices listed so a checker can verify adjacency, coprimality, and admissibility, and
    what a Lean formalisation needs; (2) every finite computation you relied on, stated so it can be re-run.
A check that cannot fail counts as no check.
