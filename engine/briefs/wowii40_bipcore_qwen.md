# ATTACK — the bipartite core of WOWII 40 (single-shot variant, TEMPLATE v2.2)

## The problem
Let G be a finite, connected, BIPARTITE simple graph on n >= 2 vertices. Define
  f(G) = maximum size of a vertex set inducing a forest;
  p(G) = path cover number = minimum number of vertex-disjoint paths covering V(G)
         (= n minus the maximum number of edges in a spanning linear forest).
Prove:
        f(G)  >=  ceil( ( n + p(G) + 1 ) / 2 ).

## Why this exact statement
For bipartite G the maximum induced bipartite set is all of V, so b(G) = n and this IS the
b(G) = n case of the inequality f >= ceil((p+b+1)/2). It is the residual core of that problem:
together with the monotonicity statement p(G[B]) >= p(G) for a maximum induced bipartite set B,
it implies the general inequality for ALL connected graphs.

## Known givens — machine-verified here; use freely, re-derive if you prefer
G1 EXHAUSTIVE: the bipartite statement holds for every connected bipartite labeled graph with n <= 6
   (n=3: 3 graphs, n=4: 19, n=5: 195, n=6: 3031 — zero violations).
G2 It is frequently TIGHT: equality in 601 of the 3031 connected bipartite 6-vertex graphs, and in
   75 of 195 at n=5, 7 of 19 at n=4, 3 of 3 at n=3.
G3 The companion monotonicity claim p(G[B]) >= p(G) (B a maximum induced bipartite set of an arbitrary
   connected G) survived 75,854 (graph, maximum-B) pairs over all connected graphs with n <= 6 with
   ZERO counterexamples — so the reduction route is not blocked by an easy counterexample.
G4 PROVED (by us, verified exhaustively for n <= 6): for any graph, 2 f(G) >= b(G) + 2; for bipartite G
   this reads 2 f(G) >= n + 2, i.e. the target with p replaced by 1. So the whole content of the
   bipartite core is the improvement from "+1" to "+p(G)".
G5 PROVED: f(G) >= p(G) (endpoints of a minimum path cover form an independent set).
G6 PROVED: if v is a leaf then f(G) = f(G-v)+1, and p(G) <= p(G-v)+1; hence one may assume min degree
   >= 2, i.e. G is its own 2-core. For trees the statement is immediate.
G7 Tight examples to respect: even cycles C_{2k} (n = 2k, p = 1, f = n-1); K_{m,m} (p = 1, f = m+1);
   stars K_{1,m} (p = m-1, f = n); C_4 with t pendant vertices at one vertex (p = t, f = n-1).

## Current task statement
Give a rigorous standalone proof of the bipartite statement using your own knowledge and reasoning,
without searching the public web, connected sources, previous conversations, or project contexts.
Assume for purposes of this task that a complete affirmative proof exists. Work iteratively until a
correct proof has been reached.

Partial progress does not count unless it implies exactly the resolution of the entire statement.
Bounded verification, heuristics, and restatements of G1-G7 are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for
strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents:
  (i) spanning-linear-forest accounting: fix a maximum spanning linear forest L (so p = n - |E(L)|);
      delete vertices to kill the cycles of G that are not cycles of L, and charge each deletion to an
      edge NOT in L;
  (ii) alternating 2-colouring along the paths of an optimal cover: keep alternate vertices of each
      path and repair conflicts, aiming at (n + p)/2 kept vertices;
  (iii) feedback vertex set duality: n - f(G) is the minimum feedback vertex set; restate the target as
      fvs(G) <= floor((n - p - 1)/2) and attack via cycle-packing/covering (Erdos-Posa style) in the
      bipartite setting where every cycle has even length >= 4;
  (iv) minimal-counterexample with min degree >= 2 (G6), where every vertex lies on a cycle;
  (v) 2-connected reduction: prove the statement for 2-connected bipartite graphs and glue over blocks,
      tracking how f and p behave under block decomposition;
  (vi) extremal: classify the tight families of G2/G7 and show any counterexample must beat them.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at an equal-strength statement is NOT close to completion.
- Use adversarial agents throughout: attack every candidate proof for gaps, for silently assuming
  2-connectivity or p = 1, and for miscounting the ceiling parity.
- Require concrete lemmas, constructions and inequalities — not plans.
- Do not stop after the first wave fails.

Return a complete proof if one survives adversarial audit. If none does, return instead: (1) the
strongest rigorously proved derivation you reached, as numbered lemmas — e.g. the statement for
2-connected bipartite graphs, or for graphs of maximum degree 3, or the weaker bound
f >= ceil((n+p)/2); (2) the exact remaining gap as a precise open statement; (3) every machine-checkable
artefact you built (explicit graph families, counts, extremal examples). Do not return an empty answer,
a bare statement of failure, a status report, or an explanation of why the problem is hard. Do not
search the web to determine whether the statement is open, and do not answer that it is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; then what a Lean formalisation needs
(Mathlib: SimpleGraph, IsAcyclic, Colorable 2, spanning linear forest), and every finite computation you
relied on, stated so it can be re-run. A check that cannot fail counts as no check.
