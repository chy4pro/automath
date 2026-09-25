# Task: construct a graph attaining `k₃ = 4`, or prove none exists

**Owner-drafted (owner-w133), PROTOCOL v4 §3b.** The mathematics below is the authority; the
keeper builds/dispatches and does not alter it. This brief is self-contained — you cannot read
any repository, and nothing you need has been withheld. **The measurement we already hold is
stated in full in §5; please do not report it back to us as a discovery.**

An honest "I could not settle this" with the exact point of failure is worth far more to us than
a fluent argument we then have to unpick. If you produce a graph, give it as an **explicit edge
list** — we verify every edge in our own hand and never take a described graph on trust.

---

## 1. Setting and conventions

All graphs are finite, simple, undirected, connected.

**`C4`-free, in this line's sense:** *no two distinct vertices have two common neighbours.*
Equivalently: no 4-cycle on four distinct vertices, induced or not. (Triangles are ALLOWED and
occur; only the two-common-neighbours pattern is forbidden.)

**Consequence you will need constantly.** For every vertex `v`, the graph induced on the open
neighbourhood `N(v)` is a **matching** (every vertex of `N(v)` has at most one neighbour inside
`N(v)`). *Reason:* if `x, y, z ∈ N(v)` with `x~y` and `x~z`, then `v` and `x` have the two common
neighbours `y` and `z`. Hence, writing
`a(v) := α(G[N(v)])` (independence number of the neighbourhood) and `t(v)` for the number of
matching edges inside `N(v)`,

> **`a(v) = deg(v) − t(v)`.**

**Standing hypothesis of the class:** `μ(G) := min_v a(v) ≥ 2`.

`d(·,·)` is graph distance, `ecc(v) := max_u d(v,u)`.

## 2. The frame — stated in full, including every derived fact we hold

Fix a vertex `w` and a **geodesic** `w = u₀, u₁, …, u_d` with `d = ecc(w)` (so `u_d` is a vertex
farthest from `w`). Because it is a geodesic, `d(w, u_j) = j` for all `j`, and `u_i ~ u_j` only
when `|i − j| = 1`.

Choose `y ∈ N(u_d)` lying in a **component of the matching `G[N(u_d)]` other than `u_{d−1}`'s**.
(Under `μ ≥ 2` such a `y` exists: `a(u_d) ≥ 2` means the matching has at least two components.)
Then choose `z ∈ N(y)` such that `w, u₁, …, u_d, y, z` is an **induced** path anchored at `w`.

**Derived facts we already hold about this frame — all of them, so that none is rediscovered and
mis-reported as an obstruction:**

* **`y ≁ u_{d−1}`** — they lie in different components of the matching `G[N(u_d)]`.
* **`y ≁ u_{d−2}`** — otherwise `u_{d−1}` and `y` are two common neighbours of the pair
  `{u_{d−2}, u_d}`, which `C4`-freeness forbids.
* **`y ≁ u_j` for every `j ≤ d−3`** — by distance: `y ~ u_d` gives `d(w,y) ≥ d−1`, so `y` cannot
  be adjacent to a vertex at distance `≤ d−3` from `w`.
* **`z ≁ u_d` and `z ≁ u_j` for all `j`** — this is exactly the requirement that
  `w, u₁, …, u_d, y, z` be **induced**; it is imposed, not derived.
* Consequently **`d(z, u_d) = 2`** (via `y`), and `d(w,z) ≥ d − 1`.

## 3. THE QUESTION

For the frame above define the **dodge list** at `z`:

> **`k₃ := #{ j ∈ {d−1, d−2, d−3, d−4} : N(z) ∩ N(u_j) ≠ ∅ }`  (indices clipped to `0 ≤ j ≤ d`).**

> **QUESTION. Does there exist a connected `C4`-free graph `G` with `μ(G) ≥ 2`, a vertex `w`, and
> a frame `(u₀…u_d, y, z)` as in §2, with `k₃ = 4` — i.e. `z` has a common neighbour with EACH of
> `u_{d−1}, u_{d−2}, u_{d−3}, u_{d−4}` simultaneously?**
>
> **Construct one (explicit edge list), or prove none exists.**

`d ≥ 5` is needed for all four indices to be in range; you may take `d` as large as you like.

## 4. Two `C4`-forced facts you will otherwise rediscover and mis-report as obstructions

These are **not** obstructions to `k₃ = 4`; they are the shape of the problem.

* **No single vertex is adjacent to both `u_{d−1}` and `u_{d−3}`** — `u_{d−2}` would then be a
  second common neighbour of that pair. Likewise no single vertex is adjacent to both `u_{d−2}`
  and `u_{d−4}`. **So the four "common neighbours" witnessing `k₃ = 4` cannot be economised: the
  witnesses for `u_{d−1}` and `u_{d−3}` must be distinct vertices, and likewise for `u_{d−2}` and
  `u_{d−4}`.**
* **Adjacency to two CONSECUTIVE `u_j` IS allowed.** A vertex adjacent to `u_{d−1}` and `u_{d−2}`
  creates a triangle, not a `C4`. Triangles are legal here. Do not exclude this case.

Also note `|N(z) ∩ N(u_j)| ≤ 1` for each `j` (two would be a forbidden pair), so each of the four
indicators is witnessed by exactly one vertex when it fires.

## 5. THE MEASUREMENT WE ALREADY HOLD — stated so that you are testing the question, not the brief

Over **417** host graphs of a designed-plus-seeded-random `C4`-free `μ ≥ 2` family (projective-plane
incidence graphs `PG(2,q)`, those with cycles and paths glued on, and a seeded random `C4`-free
process; **not exhaustive**), we walked **73 204** step-3 frames of exactly the shape in §2 and
measured the distribution of `k₃`:

| `k₃` | 0 | 1 | 2 | 3 | **4** |
|---|---|---|---|---|---|
| frames | 10 494 | 27 497 | 23 620 | 11 593 | **0** |

**The maximum attained is 3. `k₃ = 4` occurred zero times.** We also measured the analogous
2-index quantity `k₂ := #{ j ∈ {d−2, d−3} : N(y) ∩ N(u_j) ≠ ∅ }`: it attains its maximum 2 on
15 676 frames, so *that* one is attainable; and `k₂ = 2` together with `k₃ = 4` occurred 0 times.

**This is a measurement on one family, not a theorem, and it is exactly why we are asking.**

## 6. Why the answer matters (context; you need not verify this)

We carry a step-3 sufficient condition of the form `a(z) ≥ 2 + k₃`, and a blanket version
`a(z) ≥ 6` which is that condition with all four indicators set. If `k₃ = 4` is **unattainable**,
the blanket constant drops from 6 to 5. If it **is** attainable, the blanket constant is sharp and
we stop looking. Either answer is useful; a wrong answer is expensive.

## 7. Deliverable

Structure your answer as:

1. Your verdict, one of the three below.
2. If constructed: the **explicit edge list** (pairs of integers), the vertex `w`, the geodesic
   `u₀…u_d`, the vertices `y` and `z`, and the four witnesses `x_j ∈ N(z) ∩ N(u_j)`. State `n`,
   confirm `C4`-freeness in this brief's sense, and confirm `a(v) ≥ 2` at every vertex.
3. If proved impossible: the proof, with every use of `C4`-freeness marked.
4. If neither: **exactly** where the argument breaks — a named configuration you can neither build
   nor exclude.

End with exactly one of:
**CONSTRUCTED (edge list above)** · **IMPOSSIBLE (proof above)** · **UNSETTLED (break point above)**.
