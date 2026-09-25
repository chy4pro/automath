# Q15 harvest — w133 (RP-D) for r >= 4, Qwen3.8-Max

Source: https://chat.qwen.ai/c/0d160ce1-4bba-45f9-80b5-8f6d3f457232
Dispatched 08-18 16:11 CDT (owner-intel round 10); harvested 08-18 17:0x CDT (owner-intel
round 12). Completion confirmed via action-icon row (copy/thumbs-up/down/share/regenerate)
present under the final message and static content across repeated scroll-to-bottom checks.

**VERDICT: PARTIAL**

5-line summary (verbatim from model):
1. I do not have a full proof or a counterexample for (RP-D) in the stated generality.
2. I prove several general structural lemmas for C4-free graphs (endpoint extension,
   attachment to a diametral geodesic, leaf-pruning mass monotonicity).
3. I prove (RP-D) completely for the subclass of triangle-free C4-free graphs with minimum
   degree at least 4; this subclass has l >= 4 > 3.
4. The obstruction to extending the proof is precisely the degree-3 / triangular local case:
   the "two bad neighbours" counting that supplies the extra vertex can fail when the first
   off-geodesic vertex has only two spare neighbours, and triangles can absorb independent
   directions.
5. I give a fully validated control instance (the Petersen graph, explicit edge list),
   compute D=2, l=3, path=5, and check the availability/non-availability of facts F1-F7
   there.

## What was actually proved

**Lemma 1 (one-sided endpoint extension)**: geodesic `v0..vD` in C4-free G with `a(v0) >= 2`
⟹ exists `x` outside `P` with `x-v0-v1-...-vD` induced. Proof via the matching-plus-isolates
structure of `N(v0)` (F1) plus geodesic-distance contradictions for C4-freeness.

**Lemma 2 (attachments to a fixed geodesic)**: an outside vertex has at most 2 neighbours on
a geodesic, and if 2, they're consecutive. Standard C4-free + geodesic argument.

**Lemma 3 (leaf pruning increases S - 3n by exactly 1)**: removing a leaf decreases `a` of its
neighbour by exactly 1 (leaf is an isolated vertex in the neighbour's matching-plus-isolates
structure), decreasing S by 2 and n by 1.

**Theorem (partial RP-D)**: connected, C4-free, **triangle-free**, min degree >= 4, diam D >= 3
⟹ path(G) >= D+4. Proved by explicitly constructing an induced path `y-x-v0-v1-...-vD-z`:
picks a private neighbour `x` of `v0` off the geodesic (degree >= 4 guarantees room), then a
second vertex `y` via a "at most 2 bad neighbours out of >=3" counting argument at `x`, then
a symmetric single-vertex extension `z` at `vD` avoiding both `x` and `y`. This subclass has
l >= 4 > 3 automatically (triangle-free ⟹ a(v)=d(v)), so it IS a genuine sub-case of the
target, not a vacuous one.

**Named obstruction for the general case**: the "two bad neighbours" counting step breaks when
`deg(x) = 3` (no spare neighbour at all) or when triangles let a single vertex absorb what
would otherwise be two independent forbidden directions. No injection/charging argument from
hub excess `sum_{h in H}(a(h)-2)` to "spare directions" could be made rigorous (Angle 1
obstruction, explicitly self-flagged as unproved, not just unattempted).

**No counterexample found** despite explicit attempts (tail attachments, subdivisions, edge
deletions on high-l diameter-2 cores) — in every analyzed case either the graph regains the
needed induced-path length or violates l > 3.

## Control-case / counterfactual-availability section (mandatory, T12+amendments)

Petersen graph via Kneser model KG(5,2), full explicit edge list (10 vertices, 15 edges)
given and verified: simple/connected, C4-free (proved from first principles: disjoint pairs
share 0 common neighbours since |A∪B|=4 leaves 1 element; intersecting pairs share exactly 1),
diam=2, triangle-free ⟹ l=3 exactly, path=5 proved by explicit induced-P5 exhibit plus a
case-exhaustion argument ruling out any induced P6 (via automorphism-reduced case analysis
forcing a contradiction: A6 would need to contain three specific elements of a 2-set).

Per-fact availability on this control instance:
- F1: holds, yields a(v)=3 for all v.
- F2: diam=2 holds but l>3 FAILS (l=3 exactly) — **named as the one fact treated as available
  in the model's own strategy sketches (diameter-2 reduction) but NOT executing here**, i.e.
  the mandatory "name a fact that doesn't fire" requirement was satisfied honestly.
- F3: fails (needs distance >= 4; diam=2).
- F4: holds — induced C6 exhibited (12-34-15-23-14-35-12), off-cycle vertices checked to have
  0 or 2 antipodal neighbours on it (verified for all 4 off-cycle vertices individually).
- F5: holds vacuously/consistently (endpoints of the induced P5 have degree 3 <= 5).
- F6: fails (l=3, not >3).
- F7: consistent but inapplicable (n=10<=13 but l is not >3, so the fact's conclusion isn't
  being invoked).

Witness validation done C4-freeness-first, matching the amended T12 protocol.

## Self-audit highlights (verbatim structure, condensed)

- Explicitly flags the general (RP-D) conjecture as neither proved nor refuted.
- Explicitly flags the hub-excess-to-spare-directions charging argument as attempted and
  NOT made rigorous (not merely "not tried").
- Every hypothesis-use is itemized per lemma (C4-free / geodesic / a(v0)>=2 for Lemma 1;
  C4-free / geodesic for Lemma 2; leaf structure + a=d-t for Lemma 3; triangle-free / C4-free
  / min-degree>=4 / diameter-geodesic / D>=3 all separately itemized for the partial theorem).
- Four failed attack angles reported with specific obstruction per angle (mass bound
  injection failure; D=3 direct layer analysis case explosion; leaf-pruning induction
  blocked by diameter possibly dropping under pruning; counterexample search coming up
  empty in every analyzed family).

## Owner-w133 adjudication status

**UNVERIFIED — owner-w133 must re-verify line by line before adoption.** The proved
triangle-free/min-degree>=4 subcase (a genuine, non-vacuous sub-case per l>=4>3) is the
most promising named result to check first — it comes with a complete, checkable 4-step
induced-path construction. The named obstruction (degree-3 / triangular local case) is a
useful diagnostic even if nothing is adopted outright. No edge list issues found on spot
inspection of the Petersen control instance's arithmetic.
