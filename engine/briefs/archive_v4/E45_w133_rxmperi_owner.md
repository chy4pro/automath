# Task: prove or refute — "maximally far from every centre" ⟹ peripheral

**Owner-drafted (owner-w133), PROTOCOL v4 §3b.** Self-contained; you cannot read our repository
and nothing you need has been withheld. This is a question about **general finite graphs** — no
special hypotheses — so it is short. We already hold the measurement in §4; it is stated in full
so that you are testing the statement, not the brief.

A **counterexample is as valuable as a proof**, and it must come as an **explicit edge list**
(integer pairs) — we rebuild every graph in our own hand and never accept a described one.

---

## 1. Definitions

Finite, simple, undirected, **connected** graphs. `d(u,v)` = shortest-path distance.

* `ecc(v) := max_u d(v,u)`
* `rad(G) := min_v ecc(v)`, `diam(G) := max_v ecc(v)`
* `Ctr(G) := { c ∈ V : ecc(c) = rad(G) }` — the **centre set**, never empty.
* `v` is **peripheral** iff `ecc(v) = diam(G)`.

**Definition.** `w ∈ V` is **maximally far from the centre** iff

> **`d(c, w) = rad(G)` for EVERY `c ∈ Ctr(G)`.**

Note this is genuinely "maximally far": for any centre `c` and any vertex `v`,
`d(c,v) ≤ ecc(c) = rad(G)`, so `rad(G)` is the largest distance any centre has to anything.
**Consequently `d(c,w) ≥ rad(G)` and `d(c,w) = rad(G)` are the same condition** — there is nothing
to relax, and a "≥" reading is a no-op.

## 2. THE STATEMENT

> **(RXM-PERI).** If `w` is maximally far from the centre, then **`ecc(w) = diam(G)`** — that is,
> `w` is peripheral.
>
> **Prove it, or give an explicit connected graph and a vertex `w` that is maximally far from the
> centre with `ecc(w) < diam(G)`.**

If it is false in general but you can prove it under a natural extra hypothesis, that is a
useful answer — state exactly which hypothesis your proof consumes.

## 3. What we have already proved about `w` (use freely; do not re-derive and report as new)

* **`w ∉ Ctr(G)`**, hence **`ecc(w) ≥ rad(G) + 1`**. *Proof:* `w ∈ Ctr` would force
  `d(w,w) = rad(G) ≥ 1`. ∎
* **`ecc(w) ≤ 2·rad(G)`.** *Proof:* for any centre `c`,
  `ecc(w) ≤ d(w,c) + ecc(c) = rad(G) + rad(G)`. ∎
* So `rad+1 ≤ ecc(w) ≤ 2·rad` always. Since `diam ≤ 2·rad` always, the statement is asking
  whether `ecc(w)` reaches the top of the graph's eccentricity range.
* **A route that does NOT work, so you do not spend time on it:** the "descent" claim *"if
  `ecc(v) > rad` then some neighbour of `v` has smaller eccentricity"* is **FALSE** — the
  eccentricity function has non-global local minima. We measured **226** violating vertices over
  2 652 tested. Any argument that walks downhill in `ecc` from an arbitrary vertex is dead.
* Also false, and for the same reason it looks tempting: *"`w` maximally far from the centre ⟹
  `ecc(w) = 2·rad`"*. We hold **414** counterexamples (they have `ecc(w) = rad+1` with `rad = 2`).
  **(RXM-PERI) is the weaker statement that survives them**, because on those graphs
  `diam = rad+1`.

## 4. THE MEASUREMENT WE HOLD

Over **417** connected host graphs (projective-plane incidence graphs `PG(2,3)`, `PG(2,5)`, those
with cycles or paths-then-cycles attached, two cores joined by a path, and a seeded random
process; sizes 11–130; **not exhaustive**), we found **1 297** vertices that are maximally far from
the centre, and

> **`ecc(w) = diam(G)` held at 1 297 of 1 297 — zero violations.**

Liveness of that test, so you know it is not vacuous: peripherality is **not** automatic on these
graphs — only **9 124 of 16 247** vertices (56.2 %) are peripheral.

The eccentricity offsets `ecc(w) − rad` observed among those 1 297: `+1` at 414 vertices (all on
graphs of radius 2), and `+t` at radius `t` for `t = 3,4,5,6,7,8,9` (553, 62, 76, 103, 53, 18, 18
vertices). **Offset `+2` was never attained**, which we cannot explain and do not claim as a fact.

These hosts all happen to satisfy two extra properties, stated so you know what the sample is and
so you do not assume we need them: no two vertices have two common neighbours, and every vertex's
neighbourhood contains two non-adjacent vertices. **(RXM-PERI) is posed WITHOUT those hypotheses**
— a counterexample not satisfying them is still a counterexample to the general statement and we
want it; if you can only refute the general statement but not the restricted one, say exactly
that.

## 5. Why we are asking (context; nothing here needs verifying)

We have a proof whose one open case has the hypothesis *"`ecc(w) = rad+1` and `w` is maximally far
from the centre."* Under (RXM-PERI) that hypothesis forces `diam(G) = rad(G)+1`, which is a strong
and easily-checked structural condition on `G` — and it is false on the graphs our route actually
meets. So (RXM-PERI) would convert a census into a theorem. **A refutation is equally useful: it
tells us the case is real and must be attacked head-on.** Please do not aim for either answer.

## 6. Deliverable

1. Verdict.
2. If proved: the argument, with each inequality justified. Mark clearly any place where you use
   connectivity, finiteness, or a choice of centre.
3. If refuted: the **explicit edge list**, the vertex `w`, and your computed `rad`, `diam`,
   `ecc(w)`, the centre set, and `d(c,w)` for each centre.
4. If neither: the exact configuration you can neither construct nor exclude.

End with exactly one of:
**PROVED (argument above)** · **REFUTED (edge list above)** · **UNSETTLED (break point above)**.
