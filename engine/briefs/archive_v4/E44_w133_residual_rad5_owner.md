# Task: build a graph in a named 3-condition class, or prove the class is empty

**Owner-drafted (owner-w133), PROTOCOL v4 §3b.** Self-contained: you cannot read our repository,
and everything we hold on this question is written out below, including the measurements that
motivated it and the two proved lemmas that constrain it. **Nothing is withheld** — if you find
yourself reporting "no such object exists without the missing X", X is in §4 or §5 and we already
had it.

We want either an **explicit edge list** (which we verify edge by edge in our own hand) or a
proof. A precise "I could not settle it, and here is the configuration I can neither build nor
exclude" is more valuable to us than a fluent argument.

---

## 1. Definitions

Finite, simple, undirected, connected graphs.

* **`C4`-free, this line's sense:** *no two distinct vertices have two common neighbours.*
  Triangles are allowed; only that pattern is forbidden.
* For a vertex `v`, `N(v)` is its open neighbourhood and `a(v) := α(G[N(v)])`, the independence
  number of the induced subgraph on `N(v)`. Set `μ(G) := min_v a(v)`.
  **Standing hypothesis: `μ(G) ≥ 2`.**
  Useful consequence of `C4`-freeness: `G[N(v)]` is a **matching**, so `a(v) = deg(v) − t(v)`
  where `t(v)` counts the matching edges inside `N(v)`. Hence `μ ≥ 2` forbids degree-`≤1`
  vertices and forbids a degree-2 vertex whose two neighbours are adjacent.
* `d(·,·)` distance, `ecc(v) := max_u d(v,u)`, `rad(G) := min_v ecc(v)`,
  `Ctr(G) := {c : ecc(c) = rad(G)}`.
* **`l(G) := (1/n) Σ_v a(v)`**, the mean of `a(·)` over all vertices.

## 2. THE CLASS WE WANT AN INSTANCE OF

> **Find a connected graph `G` and a vertex `w` such that ALL of the following hold:**
>
> 1. `G` is `C4`-free (§1 sense) and `μ(G) ≥ 2`;
> 2. **`ecc(w) = rad(G) + 1`**;
> 3. **`d(c, w) = rad(G)` for EVERY centre `c ∈ Ctr(G)`** ("`w` is maximally far from every
>    centre");
> 4. **`rad(G) ≥ 5`**;
> 5. **`l(G) > 4`**.
>
> **Construct one (explicit edge list), or prove no such `G, w` exist.**

Partial answers are useful and should be reported as such: an instance satisfying 1–3 with
`rad ≥ 5` but `l ≤ 4`, or with `l > 4` but `rad = 3` or `4`, is a real datum — say exactly which
conditions your object meets.

## 3. Two facts about condition 3 that are easy to get wrong

* **`d(c,w) ≥ rad` and `d(c,w) = rad` are the SAME condition.** For any centre `c`,
  `d(c,w) ≤ ecc(c) = rad`. So "maximally far from every centre" cannot be relaxed to an
  inequality; there is nothing to relax.
* **Condition 3 forces `w ∉ Ctr(G)`** (as `d(w,w) = 0 ≠ rad`), and more generally
  `Ctr(G) ⊆ {v : d(v,w) = rad}`: no vertex at distance `≠ rad` from `w` is a centre.
* Condition 3 is **vacuously true when `Ctr(G) = ∅`**, which never happens, and is **impossible
  on a self-centred graph** (`Ctr(G) = V`, since then a neighbour of `w` is a centre at
  distance 1). Self-centred graphs are therefore not where to look. Condition 2 also fails
  outright on them (every eccentricity equals `rad`).

## 4. What we have PROVED about this class — you may use these freely

**(CS-1) — the sphere bound.** If `w` satisfies condition 3 and `rad ≥ 1`, then no centre lies in
the ball `B_{rad−1}(w)`, so `|Ctr(G)| ≤ n − |B_{rad−1}(w)|`.
*Proof:* `c ∈ Ctr ⟹ d(c,w) = rad > rad − 1`. ∎

**(CS-2) — the `C4`-free ball bound.** If `G` is `C4`-free with minimum degree `δ ≥ 2`, then for
every vertex `w`, `|B₂(w)| ≥ 1 + deg(w)·(δ−1) ≥ 1 + δ(δ−1)`.
*Proof:* every `z` at distance 2 from `w` has **exactly one** neighbour in `N(w)` (two would give
`w` and `z` two common neighbours), so the sets `N(u) ∩ S₂(w)`, `u ∈ N(w)`, partition `S₂(w)`.
For `u ∈ N(w)`, `|N(u) ∩ N(w)| ≤ 1` (two would give `u` and `w` two common neighbours), so
`|N(u) ∩ ({w} ∪ N(w))| ≤ 2` and `|N(u) ∩ S₂(w)| ≥ deg(u) − 2 ≥ δ − 2`. Summing over `N(w)` gives
`|S₂(w)| ≥ deg(w)(δ−2)`, hence `|B₂(w)| = 1 + deg(w) + |S₂(w)| ≥ 1 + deg(w)(δ−1)`. ∎

**(CS-3) — the corollary that decides many graphs.** `G` connected `C4`-free, `δ ≥ 2`,
`r = rad(G) ≥ 3`. If some vertex satisfies condition 3, then
**`|Ctr(G)| ≤ n − 1 − δ(δ−1) − (r−3)`.**
*Proof:* `B_{r−1}(w) ⊇ B₂(w)`, and each of the distances `3,…,r−1` from `w` is realised
(`ecc(w) ≥ r`), contributing `r−3` further vertices; apply (CS-2), then (CS-1). ∎

**So your construction must keep `|Ctr(G)|` BELOW that bound.** With `δ` large the bound bites
hard; with `δ = 2` it is nearly vacuous. That is a real design constraint, and it is the reason we
suspect the class may be empty once condition 5 (`l > 4`, which pushes `a(·)` and hence degrees
up) is imposed together with condition 4.

## 5. EVERY MEASUREMENT WE HOLD, stated in full

**(a)** Over **417** hosts of a designed-plus-seeded-random `C4`-free `μ ≥ 2` family
(`PG(2,3)` and `PG(2,5)` incidence graphs; those with cycles or paths-then-cycles glued on; two
copies joined by a path; a seeded random `C4`-free process at 12–50 vertices) — **not
exhaustive** — we counted, over all 16 000-odd vertices:

| | count |
|---|---|
| vertices with `ecc(w) = rad+1` (condition 2) | **3 250** |
| vertices maximally far from every centre (condition 3) | **1 297** |
| vertices satisfying BOTH | **414** |
| of those 414, on a host with `l > 4` | **0** |
| of those 414, with `rad ≥ 5` | **0** |
| radius profile of the 414 | **`rad = 2` on all 414** |

**(b)** On a *different* family of 145 base graphs we previously found exactly **2** vertices
satisfying conditions 1–3, and both had **`rad = 4`** and `l = 2.333` and `l = 2.455`
respectively — so the class is **not** confined to `rad = 2`; family (a) simply contains no
higher-radius instance. **Conditions 1–3 together with `l > 4` have never been observed, on any
family we have run.**

**(c)** The **22** hosts in family (a) with `l > 4` and `rad ≥ 5` are all built from the `PG(2,5)`
incidence graph (`n = 62`, 6-regular, girth 6, `a(v) = 6` at every vertex, `rad = 3`) with a path
and then a cycle attached, e.g. `PG(2,5) + P4 + C5` at `n = 70` with `rad = 5`, `l = 5.571`.
**Condition 3 is NOT rare there — it holds at 178 vertices of those 22 hosts.** What fails is
condition 2: the eccentricity offset `ecc(w) − rad` of those 178 vertices is

> `+5 : 58`, `+6 : 85`, `+7 : 35` — **never `+1`.**

They are all deep in the attached tail, far above the radius. Over all 417 hosts the offset
profile of the condition-3 vertices is
`+1 : 414`, `+3 : 553`, `+4 : 62`, `+5 : 76`, `+6 : 103`, `+7 : 53`, `+8 : 18`, `+9 : 18` —
note that **offset `+2` was attained zero times** on this family, which we have not explained and
do not claim as a fact. Offset `0` is impossible for a proved reason: condition 3 forces
`w ∉ Ctr(G)`, hence `ecc(w) ≥ rad+1`.

**(d)** For orientation on how the conditions pull against each other: raising `l` above 4 forces
most vertices to have `a(v) ≥ 4`, hence degree `≥ 4`; a graph built from a dense `C4`-free core
plus a thin attached tail typically has its centre **inside the core**, and then the vertices at
distance exactly `rad` from every core centre are hard to arrange because the core's centre set is
large and spread. That is intuition, not a proof, and we are not asking you to confirm it.

## 6. Why we are asking (context; nothing here needs verifying)

A statement we are proving reduces to one open row whose hypothesis is exactly conditions 1–4
(with `l > 4` imported from the surrounding route). If the class in §2 is **empty**, that row
closes. If you build an instance, the row is real and we must attack it head-on. **Both answers
are worth the same to us; please do not aim for one.**

## 7. Deliverable

1. Verdict (see below).
2. If constructed: **explicit edge list** as integer pairs; the vertex `w`; and your computed
   `n`, `rad`, `ecc(w)`, `|Ctr(G)|`, the distance from `w` to each centre, `min_v a(v)`, and
   `l(G)`. State which of conditions 1–5 you verified and how.
3. If proved empty: the proof, with every use of `C4`-freeness and of `μ ≥ 2` marked, and a clear
   statement of which of conditions 4 and 5 the proof actually consumes (a proof that never uses
   condition 5 would be a strictly stronger and more useful result — say so).
4. If neither: the exact configuration you can neither build nor exclude.

End with exactly one of:
**CONSTRUCTED (edge list above)** · **CLASS IS EMPTY (proof above)** · **UNSETTLED (break point
above)** · **PARTIAL (state precisely which conditions your object meets)**.
