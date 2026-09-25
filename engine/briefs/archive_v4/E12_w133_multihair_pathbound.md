# Task: attempt to prove a two-hair induced-path bound, and use it to attack the multi-hair case of a graph conjecture (WOWII-133 line)

We want a genuine proof attempt. If you cannot complete a part, say so plainly and describe
exactly where you got stuck. An honest "I could not close this, here is the obstruction" beats a
proof sketch with a hidden gap. Give reasoning and a verdict, not confidence language.

## Background (self-contained)

All graphs are simple, finite, connected, undirected, and (throughout this problem family)
**`C4`-free**: no 4 distinct vertices `a,b,c,d` with edges `ab,bc,cd,da` (a 4-cycle as a subgraph;
chords allowed; equivalently, no two vertices have 2 or more common neighbours).

For a graph `H`, `d_H(u,v)` = shortest-path distance, `ecc_H(v) = max_u d_H(v,u)`,
`rad(H) = min_v ecc_H(v)`. An **induced path** in `H` is a sequence of distinct vertices
`v_0,...,v_m` with `v_i` adjacent to `v_{i+1}` for all `i`, and NO other adjacencies among the
`v_i` (no "chords"). `path(H) :=` the maximum number of vertices in an induced path of `H`.

For `v ∈ V(H)`, `N(v)` = the open neighbourhood (vertices adjacent to `v`, not including `v`).
`a(v) := α(H[N(v)])`, the independence number of the subgraph induced on `N(v)` (the largest set
of pairwise-non-adjacent neighbours of `v`). `l(H) := (1/|V(H)|) · Σ_v a(v)`, the AVERAGE of
`a(v)` over all vertices. `μ(H) := min_v a(v)`.

**The conjecture this line is attacking (Conjecture 133, `C4`-free branch — stated for context,
you do not need to prove the conjecture itself, only the lemma below which is a tool toward it):**
for every connected `C4`-free graph `H`, `path(H) ≥ rad(H) + ⌊l(H)⌋`.

**Hair (pendant path) construction — identical to a parallel task, restated here so this brief is
self-contained.** Let `G'` be a finite connected `C4`-free graph. Fix `k ≥ 2` distinct vertices
`w_1,...,w_k ∈ V(G')` and hair lengths `h_1,...,h_k ≥ 1`. For each `i`, attach a pendant path
`w_i = x_i^0 - x_i^1 - ... - x_i^{h_i}` of FRESH vertices (distinct across hairs), with edges only
along the path, no other edges added. Let `G` be `G'` plus all `k` hairs. (Attaching pendant paths
to a `C4`-free graph cannot create a `C4`, so `G` is automatically `C4`-free too — you may use
this without proof, but feel free to double check it if useful.) This is the **multi-hair case**
(`k ≥ 2`).

## Target B: the two-hair induced-path bound

> For any two DISTINCT indices `i ≠ j` among `1,...,k`:
> ```
> path(G) ≥ h_i + d_{G'}(w_i, w_j) + 1 + h_j
> ```
> i.e., there is an induced path in `G` using at least `h_i + d_{G'}(w_i,w_j) + 1 + h_j` vertices,
> namely: the tip-to-`w_i` portion of hair `i` (`h_i` extra vertices plus `w_i` itself), a
> SHORTEST path in `G'` from `w_i` to `w_j` (using `d_{G'}(w_i,w_j) - 1` internal vertices plus the
> two endpoints — count carefully so your final vertex-count formula is exactly right and matches
> the stated bound), and the `w_j`-to-tip portion of hair `j`.

**What you must do:**
1. **Prove Target B rigorously.** In particular you must justify: (a) that a shortest
   (`G'`-geodesic) path between `w_i` and `w_j` is automatically an INDUCED path within `G'` (this
   is a general fact about geodesics in any graph — prove it: if a geodesic had a chord between
   two non-consecutive vertices, that chord would give a shorter path, contradicting minimality);
   (b) that concatenating this geodesic with the two hair segments produces an INDUCED path in the
   full graph `G`, not merely a walk — you need to rule out any unwanted adjacency between a hair
   vertex and a non-adjacent vertex of the geodesic, and between the two hairs' vertices, using the
   construction rules above (hair vertices other than `w_i` have no edges outside their own hair).
   Get the vertex count exactly right: state the total number of vertices on the concatenated path
   as a function of `h_i, h_j, d_{G'}(w_i,w_j)` and confirm it equals the claimed bound.

2. **Use Target B (together with the parallel fact, which you may take as GIVEN without proof
   here: the "replacement radius identity"
   `ecc_G(c) = max(ecc_{G'}(c), max_i(d_{G'}(c,w_i)+h_i))` for `c ∈ V(G')`, and
   `rad(G) = min_{c \in V(G')} ecc_G(c)` — assume both of these) to attempt a genuine proof
   attempt of the multi-hair case of Conjecture 133's `C4`-free branch: **show
   `path(G) ≥ rad(G) + ⌊l(G)⌋`** using Target B as your main tool, i.e. find (or bound) two hair
   indices `i,j` and use the resulting path bound together with a bound on `rad(G)` (from the
   given radius identity) and a bound relating `l(G)` to `l(G')` and the hairs' contribution, to
   close the inequality — or determine precisely which additional fact/hypothesis you would need
   to close it, and state that gap exactly.

**Context for part 2 (background only, you do not need to re-derive this — a template you may
adapt):** the already-solved SINGLE-hair case (`k=1`) closes via two sub-bounds that you may look
to for the shape of the argument (do not assume they transfer automatically — check each step):
`(B1) path(G) ≥ path(G') ≥ r+4` (where `r := rad(G')`, via a separately-proved fact about `G'`
itself, not something you need to re-derive), and
`(B2) path(G) ≥ h + endpath(G',w) ≥ h + ecc_{G'}(w) + 2` (where `endpath(G',w)` denotes the
longest induced path in `G'` starting AT `w`, and there is an already-proved unconditional fact
`endpath(H,w) ≥ ecc_H(w) + 2` for any `C4`-free connected `H` with `μ(H) ≥ 2` — you may use this
fact as given, it is not part of your task). The single-hair proof splits into cases by `h` and
`ecc_{G'}(w)` vs `rad(G')`, closing all but one residual configuration. Your task is the
MULTI-hair analogue using Target B (the two-tip path, not a single tip-to-core bound), which has
never been attempted.

## What we want from you

Full rigorous work on part 1 (required), and a genuine, honest attempt at part 2 — go as far as
you can, and if you cannot close the full inequality, report exactly which configurations of
`(k, h_1,...,h_k, l(G'), rad(G'))` remain open and why, mirroring the style of "residual case"
reporting (state the gap precisely, do not paper over it).

End with exactly one of: **PART 1 COMPLETE, PART 2 COMPLETE** (full proof of both), **PART 1
COMPLETE, PART 2 PARTIAL** (state the residual gap precisely), **PART 1 COMPLETE, PART 2 NOT
CLOSED** (state why), or **PART 1 FAILED** (if you cannot even establish Target B — explain
exactly where).
