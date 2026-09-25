# QWEN WIDE-LAYER PROBES, round 1 (2026-08-24, owner order: pre-attempt shelf targets to gauge difficulty)
Protocol: disguised S2-style prompts (no famous-problem framing, no-web-search instruction),
one Qwen web chat per probe. Harvest to engine/harvest/qwen_probe_{982,k2076}_r1.md after
~30-60 min; nudge if generation stalls (standing Qwen discipline). GRADING (difficulty data,
feeds famous_watch rows 5 & 7 + capability profile): L0 refuse/rehash · L1 correct known
lemmas only · L2 new nontrivial partial (verify before believing) · L3 major structural step
· L4 claimed full solution (→ full verification pipeline, never auto-believe). Any explicit
construction gets numerically verified locally (light Python) before any grade above L1.
Probe results are DIFFICULTY EVIDENCE, not banked mathematics.

## Probe QW-P1 → famous_watch row 7 (Erdős #982, convex distinct distances; Qwen home turf)
PROMPT (verbatim):
---
Research problem. Work from first principles; do NOT search the web; show complete reasoning.

For a set S of n distinct points in convex position in the plane and a vertex v of S, let
f(v) be the number of distinct distances from v to the other n-1 points.

Statement (S): every such set has at least one vertex v with f(v) >= floor(n/2).

Attempt BOTH directions, then commit to the one you find more promising:
(a) Prove (S).
(b) Construct an explicit convex configuration in which EVERY vertex has f(v) < floor(n/2).
    Note: the regular n-gon has f(v) = floor(n/2) at every vertex, so it exactly meets the
    bound; your configuration must be non-cocircular (points not all on one circle), and a
    known theorem forces some vertex >= 0.3611 n, so every vertex must land in
    [0.3611 n, floor(n/2)).

If you attempt (b): output exact coordinates (algebraic numbers allowed) and the full
per-vertex distinct-distance table so the count can be checked mechanically.
Partial results are valuable and welcome: sharp structural constraints any counterexample
must satisfy; a family where the maximum of f over vertices is (1/2 - epsilon) n + o(n);
or a proof for a natural subclass (e.g. centrally symmetric convex sets).
End with a clear list: PROVED (with proofs) vs CONJECTURED (clearly labeled).
---

## Probe QW-P2 → famous_watch row 5 (Kourovka 20.76, p-group bound; STRETCH probe outside
verified strengths — low expectation by design, that is the point of a boundary probe)
PROMPT (verbatim):
---
Research problem. Work from first principles; do NOT search the web; show complete reasoning.

Let p be a prime and G a finite p-group. Suppose every NORMAL abelian subgroup of G has
order at most p^k.

Question (Q): must every abelian subgroup of G (normal or not) have order at most p^(2k)?

Attempt BOTH directions:
(a) Prove the p^(2k) bound.
(b) Construct an explicit counterexample: a finite p-group whose normal abelian subgroups
    all have order <= p^k but which contains an abelian subgroup of order > p^(2k).

Constraints you may take as given (they are provable, and they tell you where a
counterexample must live): if G is metabelian the bound holds; if the nilpotency class of G
is at most p-1 the bound holds. So any counterexample is non-metabelian of class >= p.
For p >= 5 there exist exponent-p constructions (Alperin/Glauberman style) that break
closely related statements — that corner is the natural place to dig.

If constructing: give explicit generators and relations (or an explicit matrix realization
over Z/p), and verify the orders of the relevant subgroups step by step.
Partial results welcome: any bound p^(ck) with c < the trivial quadratic-in-k exponent; or
structure theorems for non-metabelian p-groups of class >= p with all normal abelian
subgroups small. End with PROVED vs CONJECTURED, clearly separated.
---

## AMENDMENT (2026-08-24, owner correction — binding)
P2's first run went out on Qwen3.7-Plus (new-chat silently reset the model). Owner stopped it:
capability data is PER-MODEL; a probe on a weaker tier is void, not "noted". Rule: verify the
model name reads Qwen3.8-Max on screen BEFORE pasting any probe; if the target tier cannot be
selected, fix the UI problem or abort — never run anyway. The 3.7-Plus partial output is VOID
and must not be harvested or graded.
