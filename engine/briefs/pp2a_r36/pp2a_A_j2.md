# REVIEW REQUEST — WOWII-133, extract R34-E1

You are reviewing a self-contained extract from a research note on induced paths in C4-free
graphs. Work only from what is written here; you have no internet access and no access to the
rest of the note. Do not use a SAT solver. Answer every part.

**Definitions used throughout.** `G` is a finite simple connected graph. `G` is *C4-free* in
this note's sense: no two vertices have two common neighbours. For a vertex `v`, `N(v)` is its
neighbourhood, `a(v) := alpha(G[N(v)])` is the independence number of the subgraph induced on
`N(v)`, and `mu(G) := min_v a(v)`. `l(G) := (1/n) * sum_v a(v)` is the mean of the a-values.
`rad`, `ecc`, `diam` and `centre` have their usual meanings. `path(G)` is the number of
VERTICES of a longest induced path of `G`. `endpath(G,w)` is the number of vertices of a
longest induced path of `G` having `w` as an ENDPOINT. `peel(G)` is the graph left when
vertices of a-value 1 are deleted repeatedly until none remains.

**What you are asked to do.**

* **(P1) LINK DISCIPLINE.** For every step of every proof below that invokes a numbered
  result, check the step against that result's stated hypotheses. Report each step whose
  invocation is not covered by the hypotheses as stated, quoting the step. If you find none,
  say so.
* **(P2) CERTIFICATION.** Every numeric claim in PART 3 is tagged `[C]` where the extract
  states that the value was verified by machine on the printed edge list. Confirm that each
  numeric claim in PART 3 carries such a tag, and report any that does not.
* **(P3) GRID.** Answer the numbered questions in PART 4 from the printed edge lists. Show
  your computation for each. If you cannot compute one, write CANNOT COMPUTE rather than
  guessing.

Report in the order (P1), (P2), (P3).

## PART 1 — two results this extract uses

> **Result T1.** Let `G` be connected and C4-free with `mu(G) >= 2`. Then
> `endpath(G,w) >= ecc(w) + 2` at EVERY vertex `w`.

*Proof.* Let `u_0 = w, u_1, ..., u_d` be a geodesic from `w` to a furthest vertex, `d =
ecc(w)`. Since `a(u_d) >= 2`, the graph `G[N(u_d)]` — a matching, because `G` is C4-free —
has a component other than the one containing `u_{d-1}`; pick `y` in it. Then `y` is not
adjacent to `u_{d-1}` and, for `i <= d-2`, `y u_i` is excluded by distance, so
`u_0 ... u_d y` is induced and has `d + 2` vertices. QED

> **Result T2 (imported).** Let `G` be connected, C4-free, with `l(G) > 4`, `rad(G) >= 5`, and
> `mu(G) >= 2`. Then `path(G) >= rad(G) + 4`.

Result T2 is quoted from the note as stated; its proof is not reproduced here.

## PART 2 — the single-hair reduction

Setting: `G` connected C4-free, `G' = peel(G)` connected with `mu(G') >= 2`, and the peeled
set is a single hair of `h >= 1` vertices attached at `w` in `V(G')`. Write `r := rad(G')` and
`e := ecc_{G'}(w)`. Two bounds are available:

* **(B1)** `G'` is induced in `G`, so `path(G) >= path(G')`.
* **(B2)** the hair prepends `h` vertices to any induced path of `G'` ending at `w`, so
  `path(G) >= h + endpath(G',w) >= h + e + 2` by Result T1 — unconditional.

With one hair, `ecc_G(w) = max(e,h)`, hence `rad(G) <= max(e,h)`.

> **Proposition P.** Assume in addition that `l(G') > 4`, `rad(G') >= 5` and `mu(G') >= 2`. Then in the case `h = 1`, `e = r`, the target `path(G) >= rad(G)+4`
> holds.

*Proof.* Here `rad(G) <= max(e,h) = e = r`. By (B1) and Result T2 applied to `G'`,
`path(G) >= path(G') >= rad(G') + 4 = r + 4 >= rad(G) + 4`. QED

**Residual, stated so it is not mistaken for a closed case.** The configuration `h = 1`,
`e = r+1`, `rad(G) = r+1` is NOT covered by either bound above and is left open in this
extract.

## PART 3 — three worked values on the hosts of PART 4

* `H1` is connected [C] and C4-free in the sense defined above [C].
* `H2` has `mu(H2) = 2` [C].
* `H3` has radius `3` [C].

## PART 4 — the grid (compute from the edge lists; nothing below is stated elsewhere)

Edge lists, vertices labelled from 0:

* `H1`: [(0, 1), (0, 12), (0, 5), (1, 4), (1, 6), (1, 7), (1, 8), (2, 8), (2, 10), (2, 12), (3, 11), (3, 5), (3, 6), (4, 11), (5, 10), (7, 10), (8, 9), (9, 11), (11, 12)]
* `H2`: [(0, 9), (0, 2), (0, 3), (0, 4), (1, 8), (1, 10), (1, 3), (2, 7), (3, 11), (3, 6), (4, 10), (5, 8), (5, 9), (5, 6), (5, 7), (7, 11), (7, 10)]
* `H3`: [(0, 8), (0, 9), (0, 12), (1, 2), (1, 11), (1, 4), (2, 3), (2, 12), (2, 6), (3, 5), (4, 9), (5, 11), (5, 10), (6, 8), (6, 10), (7, 9), (7, 11), (8, 11), (9, 10)]

Questions:

1. (W1) H1: number of edges
2. (W2) H1: (maximum degree, the vertex attaining it)
3. (W3) H2: the a-vector, as a sorted tuple
4. (W4) H1: (sum of a over all vertices, n) so l = sum/n
5. (W5) H2: (radius, diameter, number of centres)
6. (W6) H3: (radius, #vertices with ecc = rad+1)
