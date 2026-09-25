# Task: attempt to prove a multi-hair eccentricity/radius identity for graphs (WOWII-133 line)

We want a genuine proof attempt of a precise, self-contained graph-theory claim. If you cannot
complete it, say so plainly and describe exactly where you got stuck — an honest "I could not
close this, here is the obstruction" is far more useful than a proof sketch with a hidden gap.
Give reasoning and a verdict, not confidence language.

## Background (self-contained)

All graphs are simple, finite, connected, undirected. For a graph `H` and `u,v ∈ V(H)`, `d_H(u,v)`
is the usual shortest-path distance. `ecc_H(v) := max_{u ∈ V(H)} d_H(v,u)` is the eccentricity of
`v` in `H`. `rad(H) := min_v ecc_H(v)`.

**Hair (pendant path) construction.** Let `G'` be a finite connected graph. Fix `k ≥ 2` distinct
vertices `w_1, w_2, ..., w_k ∈ V(G')` ("attachment points") and positive integers
`h_1, h_2, ..., h_k ≥ 1` ("hair lengths"). For each `i`, attach a **hair** at `w_i`: a path
`w_i = x_i^0 - x_i^1 - x_i^2 - ... - x_i^{h_i}`, where `x_i^1, ..., x_i^{h_i}` are FRESH vertices
(not in `G'`, and distinct across different `i`'s hairs, and distinct from all other hairs' fresh
vertices), with edges only along this path (`x_i^{j}` adjacent to `x_i^{j+1}`, and `x_i^0 = w_i`
adjacent to `x_i^1`) and NO other edges added anywhere. Let `G` be the graph on
`V(G') ∪ {x_i^j : 1 ≤ i ≤ k, 1 ≤ j ≤ h_i}` with `E(G) = E(G') ∪ (\text{all the hair edges just
described})`. `G` is connected since `G'` is and each hair is attached to a `G'`-vertex.

This is called the **multi-hair case** (`k ≥ 2`; the "single-hair case", `k=1`, is a separately
established easier case you do NOT need to re-derive — it is not part of this task).

## The claim to prove (Target A: the replacement radius identity)

> For every vertex `c ∈ V(G')` (i.e., every vertex of the original core, viewed as a vertex of the
> bigger graph `G`):
> ```
> ecc_G(c) = max( ecc_{G'}(c),  max_{1 ≤ i ≤ k} ( d_{G'}(c, w_i) + h_i ) )
> ```
> That is, the eccentricity of a core vertex `c` inside the enlarged graph `G` is the larger of
> (a) its old eccentricity computed purely within `G'`, and (b) the distance-plus-hair-length to
> the farthest tip among all `k` hairs.

**What you must establish, precisely and completely:**
1. **Prove the formula for `c ∈ V(G')`** as stated. (Sketch of the idea, which you should verify
   rather than assume: for any target vertex `u` in `G`, either `u ∈ V(G')`, in which case
   `d_G(c,u) = d_{G'}(c,u)` — you should justify why attaching pendant hairs to `G'` cannot create
   any SHORTER path between two `G'`-vertices than existed in `G'` already, i.e. `G'` is an
   isometric/distance-preserving subgraph of `G` — or `u` lies on some hair `i` at depth `j`
   (`u = x_i^j`, `1 ≤ j ≤ h_i`), in which case `d_G(c, u) = d_{G'}(c, w_i) + j`, which is maximized
   over `j` at `j = h_i`. Taking the max over all such `u` gives the claimed formula. Fill in and
   verify every step of this, including why `G'` is isometrically embedded in `G`.)
2. **Determine and prove the correct analogous formula for `ecc_G(u)` when `u` itself lies ON a
   hair** (i.e. `u = x_i^j` for some `i`, `1 ≤ j ≤ h_i`) — this case is NOT covered by the formula
   above (which is only for `c ∈ V(G')`) and is needed for a complete description of
   eccentricities in `G`, in particular to correctly compute `rad(G) = min_{v ∈ V(G)} ecc_G(v)`.
   Work out the formula (in terms of `j`, `h_i`, `d_{G'}(w_i, \cdot)`, and the eccentricities of
   `w_i` and the other hairs) and prove it.
3. Using parts 1 and 2, state and prove (or explain why it needs more information) a formula or
   useful bound for `rad(G)` itself in terms of `rad(G')`, the `d_{G'}(\cdot, w_i)` distances, and
   the hair lengths `h_i`. In particular: is it always true that the minimum in `rad(G)` is
   achieved by some `c ∈ V(G')` (never by a vertex on a hair)? Prove or disprove this.

## Context for why this is useful (you do not need to use or verify this, it is background only)

This identity is meant to generalize a special case already established for `k=1`:
`ecc_G(c) = max(ecc_{G'}(c), d(c,w)+h)` for a single hair of length `h` at `w`. The multi-hair
generalization above has been proposed but **never proved or even attempted** — you are the first
attempt at it.

## What we want from you

A complete, rigorous proof of Target A parts 1–3 above, or as much of it as you can actually
close. Be careful about edge cases: `k=2` vs larger `k`; hairs attached at the same or different
`G'`-vertices... wait, attachment points `w_1,...,w_k` are required distinct by the setup above,
but consider whether your proof implicitly needs anything beyond that (e.g., does it matter
whether some `w_i` is itself on the shortest path between two other `w_j`'s?). State any additional
hypothesis your proof needs beyond what's given, if any.

End your answer with exactly one of: **PROOF COMPLETE** (for all three parts — give the full
argument), **PARTIAL** (state exactly which parts you closed and which you could not, and why),
or **CLAIM APPEARS FALSE** (give an explicit counterexample `G'`, attachment data, and the
vertex/distance computation that breaks the formula).
