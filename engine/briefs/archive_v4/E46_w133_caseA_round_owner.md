# Task: build a ROUND, DENSE, LONG graph with a vertex far from every centre — or prove none exists

**Owner-drafted (owner-w133), PROTOCOL v4 §3b. BUILT FROM OWNER ROUND 42 (2026-08-23).**
This brief replaces `E44` (built from round 42's predecessor, round 39), which is **STRUCK**:
round 42 answered E44's question by building 146 instances of the class E44 asked about. What
survives is the half of that class E44 never separated out, and it is the subject here.

Self-contained: you cannot read our repository, and **everything we hold on this question is
written out below**, including the proofs, the measurements, the construction family we used,
the defect we found in our own construction argument, and a full edge list of the object that
answered the *other* half. **Nothing is withheld.** If you find yourself reporting "no such
object exists without the missing X", X is in §4, §5 or §6 and we already had it.

We want either an **explicit edge list** (which we verify edge by edge in our own hand) or a
proof. A precise *"I could not settle it, and here is the configuration I can neither build nor
exclude"* is worth more to us than a fluent argument.

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
  `diam(G) := max_v ecc(v)`, `Ctr(G) := {c : ecc(c) = rad(G)}`,
  `S_j(w) := {v : d(v,w) = j}`, `B_j(w) := {v : d(v,w) ≤ j}`.
* **`l(G) := (1/n) Σ_v a(v)`**, the mean of `a(·)` over all vertices.

## 2. THE CLASS WE WANT AN INSTANCE OF

> **Find a connected graph `G` and a vertex `w` such that ALL of the following hold:**
>
> 1. `G` is `C4`-free (§1 sense) and `μ(G) ≥ 2`;
> 2. **`rad(G) ≥ 5`**;
> 3. **`diam(G) = rad(G) + 1`** — the graph is *round*: exactly one eccentricity above the
>    radius, and no more;
> 4. **`d(c, w) = rad(G)` for EVERY centre `c ∈ Ctr(G)`** (`w` is *maximally far from every
>    centre*);
> 5. **`l(G) > 4`**.
>
> **Construct one (explicit edge list), or prove no such `G, w` exist.**

**Note that `ecc(w) = rad+1` comes free and must not be searched for separately** — see (PER-A)
in §4. Conditions 3+4 force it.

Partial answers are useful and should be reported as such: an instance meeting 1–4 but with
`l ≤ 4`, or meeting 1,3,4,5 with `rad = 3` or `4`, is a **real datum** — say exactly which
conditions your object meets. A proof of emptiness that never uses condition 5 would be
strictly stronger and more useful; say so if that is what you have.

## 3. Facts about condition 4 that are easy to get wrong

* **`d(c,w) ≥ rad` and `d(c,w) = rad` are the SAME condition.** For any centre `c`,
  `d(c,w) ≤ ecc(c) = rad`. There is nothing to relax.
* Condition 4 forces `w ∉ Ctr(G)` (as `d(w,w) = 0 ≠ rad`), and more generally
  `Ctr(G) ⊆ S_rad(w)`: **no vertex at distance `≠ rad` from `w` is a centre.**
* Condition 4 is **impossible on a self-centred graph** (`Ctr = V`: a neighbour of `w` would be
  a centre at distance 1). Condition 3 already excludes self-centred graphs (`diam = rad+1 ≠
  rad`), so the two conditions pull in the same direction, and **that tension is the whole
  problem**: condition 3 wants eccentricities flat, condition 4 wants the flat-minimum set
  small and pushed onto one sphere around `w`.

## 4. What we have PROVED. Use these freely; they are ours and they hold.

**(PER-A) — why condition 3 makes `ecc(w) = rad+1` free.** If `diam = rad+1` and `w ∉ Ctr(G)`,
then `ecc(w) = diam = rad+1`.
*Proof:* `ecc(w) ≥ rad+1 = diam` since `w` is not a centre, and `ecc(w) ≤ diam` always. ∎

**(PER-B).** If `ecc(w) = 2·rad` then `ecc(w) = diam`.
*Proof:* for any centre `c` and any `x,y`, `d(x,y) ≤ d(x,c)+d(c,y) ≤ 2·rad`, so `diam ≤ 2·rad`;
and `ecc(w) ≤ diam`. ∎ *(Included because it is the other way a vertex is forced peripheral; it
cannot fire here, since `rad+1 < 2·rad` for `rad ≥ 2`.)*

**(BRACKET).** If `w` satisfies condition 4 then `rad+1 ≤ ecc(w) ≤ 2·rad`, unconditionally.
*Proof:* lower bound as in (PER-A); upper bound `ecc(w) ≤ d(w,c) + ecc(c) = rad + rad`. ∎

**(CS-1) — the sphere bound.** If `w` satisfies condition 4 and `rad ≥ 1`, then no centre lies
in `B_{rad−1}(w)`, so `|Ctr(G)| ≤ n − |B_{rad−1}(w)|`.
*Proof:* `c ∈ Ctr ⟹ d(c,w) = rad > rad−1`. ∎

**(CS-1′) — the sharp form, and it is the design constraint that matters most here.** If `w`
satisfies condition 4 and `ecc(w) = rad + t`, then
**`|Ctr(G)| ≤ |S_rad(w)| = n − |B_{rad−1}(w)| − Σ_{j=1..t} |S_{rad+j}(w)|`.**
*Proof:* `c ∈ Ctr ⟹ d(c,w) = rad` **exactly**, so every centre lies on the single sphere
`S_rad(w)`, and the spheres partition `V`. ∎
**Contrapositive, which is how we use it:** if `|Ctr(G)| > max_{w ∉ Ctr} |S_rad(w)|`, the graph
**cannot** contain a condition-4 vertex at all. This is a proof, not a heuristic, and it is
cheap to evaluate — **evaluate it on your candidate before you look for `w`.**

**(CS-2) — the `C4`-free ball bound.** If `G` is `C4`-free with minimum degree `δ ≥ 2`, then for
every vertex `w`, `|B₂(w)| ≥ 1 + deg(w)·(δ−1) ≥ 1 + δ(δ−1)`.
*Proof:* every `z` at distance 2 from `w` has **exactly one** neighbour in `N(w)` (two would
give `w` and `z` two common neighbours), so the sets `N(u) ∩ S₂(w)`, `u ∈ N(w)`, partition
`S₂(w)`. For `u ∈ N(w)`, `|N(u) ∩ N(w)| ≤ 1`, so `|N(u) ∩ ({w} ∪ N(w))| ≤ 2` and
`|N(u) ∩ S₂(w)| ≥ deg(u) − 2 ≥ δ − 2`. Summing over `N(w)` gives `|S₂(w)| ≥ deg(w)(δ−2)`,
hence `|B₂(w)| ≥ 1 + deg(w)(δ−1)`. ∎

**(CS-3).** `G` connected `C4`-free, `δ ≥ 2`, `r = rad(G) ≥ 3`. If some vertex satisfies
condition 4, then **`|Ctr(G)| ≤ n − 1 − δ(δ−1) − (r−3)`.**
*Proof:* `B_{r−1}(w) ⊇ B₂(w)`, each of the distances `3,…,r−1` from `w` is realised, apply
(CS-2) then (CS-1). ∎ *(With `δ = 2` this is nearly vacuous; it bites when `δ` is large.)*

## 5. EVERY MEASUREMENT WE HOLD, stated in full — including the ones against us

**(a) The class of §2 is NON-EMPTY at `rad = 2`.** Over a family of 417 designed-plus-seeded-
random `C4`-free `μ ≥ 2` hosts we found **414** vertices satisfying conditions 1, 3, 4 (i.e.
`diam = rad+1` and maximally far from every centre) — **every one of them at `rad = 2`,
`diam = 3`, and every one on a host with `l ≤ 4`**. So the *shape* asked for exists; the
question is whether it survives `rad ≥ 5` **and** `l > 4`.

**(b) We dropped condition 3 and the class is non-empty — 146 instances.** Round 42 (ours)
built a new host family (§6) and searched it. Over **396** hosts certified `C4`-free with
`μ ≥ 2`, **393** of them in class (`l > 4` and `rad ≥ 5`):

| | count |
|---|---|
| vertices maximally far from every centre (condition 4) | **1 095** |
| … of them on hosts with `diam = rad+1` (condition 3) | **0** |
| … of them on hosts with `diam ≥ rad+2` | **1 095** |
| of the 1 095, those with `ecc(w) = rad+1` | **146** |

**So `rad ≥ 5`, `l > 4`, condition 4 and `ecc(w) = rad+1` are simultaneously satisfiable —
146 times — and every single one of those instances has `diam ≥ rad+2`, i.e. FAILS condition
3.** §7 gives one of them in full. **Do not hand us another one of these: that question is
closed.**

**(c) The measurement that is against us, and it is the reason this brief exists.** Of the 393
in-class hosts above, **57** satisfy condition 3 (`diam = rad+1`) with `rad ≥ 5` and `l > 4` —
the first such hosts this line has ever had. On **53 of the 57**, `|Ctr(G)| > max_w |S_rad(w)|`,
so by **(CS-1′)** each is **provably free of condition-4 vertices** and our search over them
tested **nothing**. That leaves **4** hosts on which the answer could have gone either way:

| host | `n` | `l` | `rad` | `diam` | `|Ctr|` | `max_w |S_rad(w)|` |
|---|---|---|---|---|---|---|
| `NLsd(6,s3)` | 120 | 4.650 | 5 | 6 | 25 | 41 |
| `NLsd(6,s4)` | 120 | 4.650 | 5 | 6 | 20 | 42 |
| `NLsd(6,s5)` | 120 | 4.650 | 5 | 6 | 26 | 43 |
| `NLkd(3^6,s3)` | 156 | 5.000 | 5 | 6 | 12 | 44 |

**516 vertices, 433 of them non-central and so eligible for condition 4 — and 0 of them
satisfies it.** That is the entire evidence we have for emptiness: **four hosts.** We are not
quoting "0 of 57"; we are telling you that 53 of those 57 were decided by a counting lemma
before the search began.

**(d) The mechanism, as far as we can see it, stated as intuition and not as fact.** Condition
3 makes eccentricities flat, and flat eccentricities make `Ctr` **large** (over our 57 round
in-class hosts `|Ctr|` ran from 12 to 275, with `n` from 106 to 434, and only the four smallest
centre sets survived (CS-1′)). Condition 4 needs `Ctr`
to fit inside one sphere `S_rad(w)`. Those pull against each other, and (CS-1′) is the exact
statement of the pull. **A construction therefore needs a round graph with a SMALL centre set**
— and we do not know whether roundness at `rad ≥ 5` with `l > 4` permits one. That is the
question. We are **not** asking you to confirm the intuition.

**(e) `rad = 4` data point.** Two graphs of ours (`n = 18` and `n = 22`, `C4`-free, `μ = 2`,
`l = 2.333` and `2.455`) have `rad = 4`, a vertex maximally far from every centre with
`ecc(w) = rad+1` — and **`diam = 7` on both**, so both fail condition 3 as well. **Every
instance we know above `rad = 2` fails condition 3.**

## 6. THE FAMILY WE BUILT, AND THE DEFECT WE FOUND IN OUR OWN ARGUMENT

You may reuse this or ignore it; we give it because withholding it would waste your time.

**The necklace.** Take `m` blocks arranged in a **cycle**; block `i` is the point–line
incidence graph of the projective plane `PG(2,q_i)` (`q ∈ {2,3,5}`: `n = 14, 26, 62`,
`(q+1)`-regular, girth 6, `rad = diam = 3`, `a(v) = q+1` at every vertex). Join block `i` to
block `i+1` by a **partial injection** from a set of block-`i` vertices to distinct block-`i+1`
vertices, and choose the **sources to be an independent set of block `i`** — its points will
do.

*Why it is `C4`-free:* a cross-block `C4` would need two matched vertices `v ~ x` inside block
`i` whose images are adjacent inside block `i+1`; independent sources make `v ~ x` impossible.
Two vertices of the same block share at most one neighbour inside it, and their images are
distinct. **⚠ THIS ARGUMENT IS FALSE AT `m = 4`, and our own run caught it**: at `m = 4`,
blocks `i` and `i+2` are joined by **two** routes (through `i+1` and through `i+3`), so a
vertex of block `i` and a vertex of block `i+2` can pick up one common neighbour on each route.
**Two of fifteen `m = 4` necklaces we built are not `C4`-free.** The corrected statement needs
**`m ≥ 5`**. We state this because we would rather hand you a corrected argument than a clean
one. **Certify `C4`-freeness by machine anyway; the argument is not what makes the object
correct.**

*Density:* `l` sits a little above `q+1` averaged over the blocks, so mixing `PG(2,3)` blocks
(`a = 4`) with `PG(2,2)` blocks (`a = 3`) lands `l` just above 4, and `PG(2,5)` blocks
(`a = 6`) put it comfortably above. *Length:* `rad` grows with `m`.
*What it did NOT give us:* round hosts with a small centre. Varying the matching densities per
block (we tried schedules like `(1.0, 0.4)`, `(1.0, 0.6, 0.3)`, `(0.9, 0.2, 0.7, 0.35)`) breaks
enough symmetry to produce `|Ctr| = 1` or `2` — **but every host on which it did so came out
with `diam ≥ rad+2`, i.e. NOT round.** Round and small-centred together is exactly what we
could not build.

## 7. THE OBJECT THAT ANSWERED THE OTHER HALF, IN FULL

`W42a`: `n = 96`, 193 edges, `C4`-free, `μ = 3`, `l = 4.020833`, `rad = 5`, **`diam = 8`**,
`Ctr = {70, 71}`, and `w ∈ {33, 35}` each has `ecc(w) = 6 = rad+1` and `d(c,w) = 5 = rad` for
both centres. It meets conditions 1, 2, 4, 5 and **fails condition 3** (`diam = 8 ≠ 6`).
Vertices are `0..95`; edges (unordered):

```
0-14 0-17 0-20 0-23 0-28 1-13 1-17 1-18 1-19 1-26 2-16 2-17 2-22 2-24 2-32 3-15 3-17 3-21
3-25 3-37 3-87 4-13 4-14 4-15 4-16 4-27 5-14 5-19 5-22 5-25 5-33 6-14 6-18 6-21 6-24 6-36
7-13 7-23 7-24 7-25 7-35 8-16 8-19 8-21 8-23 8-30 8-82 9-15 9-18 9-22 9-23 9-34 10-13 10-20
10-21 10-22 10-29 10-84 11-15 11-19 11-20 11-24 11-38 12-16 12-18 12-20 12-25 12-31 26-34
26-36 26-38 26-51 27-33 27-36 27-37 28-35 28-36 28-39 28-49 29-33 29-34 29-35 29-47 30-34
30-37 30-39 31-33 31-38 31-39 32-35 32-37 32-38 40-48 40-50 40-52 40-60 41-47 41-50 41-51
41-54 42-49 42-50 42-53 42-62 43-47 43-48 43-49 43-64 44-48 44-51 44-53 44-65 45-47 45-52
45-53 45-56 46-49 46-51 46-52 46-66 54-62 54-64 54-66 55-61 55-64 55-65 55-71 56-63 56-64
56-67 56-70 57-61 57-62 57-63 58-62 58-65 58-67 58-80 59-61 59-66 59-67 60-63 60-65 60-66
68-76 68-78 68-80 68-90 69-75 69-78 69-79 69-92 70-77 70-78 70-81 70-82 71-75 71-76 71-77
71-87 72-76 72-79 72-81 72-88 73-75 73-80 73-81 73-84 74-77 74-79 74-80 74-94 82-90 82-92
82-94 83-89 83-92 83-93 84-91 84-92 84-95 85-89 85-90 85-91 86-90 86-93 86-95 87-89 87-94
87-95 88-91 88-93 88-94
```

**A natural attack, offered because it is what we would try next:** shrink this object's
diameter to `rad+1` without destroying `μ ≥ 2`, `l > 4` or the centre's position. We do not
know whether that is possible; if you show it is **not**, say exactly what obstructs it.

## 8. Why we are asking (context; nothing here needs verifying)

A statement we are proving has one open row whose hypothesis is conditions 1, 2, 4, 5 plus
`ecc(w) = rad+1`. Round 42 showed that row is **non-empty** — §7 is an instance — so it cannot
be closed by emptiness. What remains unknown is the **round** half, conditions 1–5 together.
If it is **empty**, that half of the row closes for a structural reason and we learn the
mechanism; if you **build** one, the row is real in both halves and we attack it head-on.
**Both answers are worth the same to us; please do not aim for one.**

## 9. Deliverable

1. Verdict (see below).
2. If constructed: **explicit edge list** as integer pairs; the vertex `w`; and your computed
   `n`, `rad`, `diam`, `ecc(w)`, `Ctr(G)`, the distance from `w` to **each** centre,
   `min_v a(v)`, and `l(G)`. State which of conditions 1–5 you verified and how.
   **Check (CS-1′) on your object before sending it**: `|Ctr| ≤ |S_rad(w)|` is necessary, and
   an object failing it is wrong regardless of anything else you computed.
3. If proved empty: the proof, with **every** use of `C4`-freeness and of `μ ≥ 2` marked, and a
   clear statement of which of conditions 2 and 5 the proof actually consumes.
4. If neither: the exact configuration you can neither build nor exclude.

End with exactly one of:
**CONSTRUCTED (edge list above)** · **CLASS IS EMPTY (proof above)** · **UNSETTLED (break point
above)** · **PARTIAL (state precisely which conditions your object meets)**.
