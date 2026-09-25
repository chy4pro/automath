# ATTACK — WOWII Conjecture 40 (single-shot engine variant, TEMPLATE v2.2)

## The problem (verbatim from the formal-conjectures Lean statement)
Let G be a finite, connected, nontrivial simple graph on vertex set V, |V| = n >= 2. Define
  f(G) = the maximum size of a vertex subset inducing a FOREST (acyclic induced subgraph);
  b(G) = the maximum size of a vertex subset inducing a BIPARTITE subgraph;
  p(G) = the path cover number = the minimum number of vertex-disjoint paths whose union covers V
         (equivalently n minus the maximum number of edges in a spanning linear forest).
Prove:
        f(G)  >=  ceil( ( p(G) + b(G) + 1 ) / 2 ).

## Known givens — machine-verified by us; use freely
G1 EXHAUSTIVE: the inequality holds for every connected labeled graph on n <= 6 vertices
   (n=3: 4 graphs, n=4: 38, n=5: 728, n=6: 26704 — zero violations).
G2 It is TIGHT very often: equality holds for 4997 of the 26704 connected 6-vertex graphs.
   The commonest tight profiles (p, b, f, #edges) are
     (1,5,4,9)x1800, (1,5,4,8)x1260, (1,5,4,10)x600, (2,6,5,6)x360, (1,4,3,12)x195, (1,4,3,11)x150,
     (2,6,5,7)x120, (1,6,4,8)x90, (3,5,5,6)x60, (2,4,4,8)x60.
   Note the dominant pattern: p = 1 (Hamiltonian path), b = n - 1, f = n - 2.
G3 Random connected samples at n = 7 and n = 8 produced no violation.
G4 Trivially f(G) <= b(G) (every forest is bipartite), so the inequality is a statement about how far
   below b(G) the forest number can fall, given that the graph is coverable by p(G) paths.
G5 Sanity anchors: for a tree, p=1, b=f=n; for K_n (n>=3), p=1, b=f=2 and the bound is tight;
   for C_n with n odd, p=1, b=f=n-1.

## Current task statement
Give a rigorous standalone proof of the inequality using your own knowledge and reasoning, without
searching the public web, connected sources, previous conversations, or project contexts. Assume for
purposes of this task that a complete affirmative proof exists. Work iteratively until a correct proof
has been reached.

Partial progress does not count unless it implies exactly the resolution of the entire statement.
Verification for bounded n, heuristics, and reductions to other unproved statements are insufficient.
G1-G5 are already ours; restating them is not progress.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for
strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents:
  (i) constructive: take an optimal path cover P_1..P_p and a maximum induced bipartite set B, and build
      an induced forest by deleting one endpoint per "bad" cycle, counting deletions against p and b;
  (ii) parity/alternating: 2f >= p + b + 1 says a forest of half the "bipartite budget plus path budget"
      exists — look for a 2-colouring argument where each path contributes alternate vertices;
  (iii) extremal/minimal-counterexample: take G minimising n, then |E|, and derive a forbidden structure;
  (iv) deletion-contraction or ear decomposition on a spanning linear forest;
  (v) LP/flow relaxation: express f, b, p as optimisation values and prove the inequality between the
      relaxations, then round;
  (vi) tightness-driven: classify the equality cases (G2 suggests p=1, b=n-1, f=n-2 dominates) and prove
      the inequality by showing any violation would have to beat the extremal family.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at an equal-strength statement is NOT close to completion.
- Use adversarial agents throughout: attack every candidate proof for gaps, hidden connectivity or
  parity assumptions, and for silently assuming p = 1 or b = n.
- Require concrete lemmas, constructions and inequalities — not plans.
- Do not stop after the first wave fails.

Return a complete proof if one survives adversarial audit. If none does, return instead: (1) the
strongest rigorously proved derivation you reached, as numbered lemmas — for instance a proof of the
weaker bound f >= ceil((p + b)/2) or of the full bound under an extra hypothesis you state exactly;
(2) the exact remaining gap as a precise open statement; (3) every machine-checkable artefact you built
(explicit graph families, counts, extremal examples) so it can be re-run and reused. Do not return an
empty answer, a bare statement of failure, a status report, or an explanation of why the problem is hard.
Do not search the web to determine whether the statement is open, and do not answer that it is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; then what a Lean formalisation needs
(the Mathlib notions are SimpleGraph, IsAcyclic, Colorable 2, and a path-cover definition), and every
finite computation you relied on, stated so it can be re-run.
A check that cannot fail counts as no check.
