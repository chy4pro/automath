# WOWII Graffiti.pc Conjecture 133 — attack report

**Target.** `FormalConjectures/WrittenOnTheWallII/GraphConjecture133.lean`

```lean
theorem conjecture133 (G : SimpleGraph α) [DecidableRel G.Adj] (h : G.Connected) :
    let rad := G.radius.toNat
    let hasC4 := ∃ a b c d : α, a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
      G.Adj a b ∧ G.Adj b c ∧ G.Adj c d ∧ G.Adj d a
    let cC4 : ℕ := if hasC4 then 0 else 1
    (rad : ℝ) + (⌊l G⌋ : ℝ) ^ cC4 ≤ (path G : ℝ)
```
with `[Fintype α] [DecidableEq α] [Nontrivial α]`.

Date: 2026-08-17. Everything numeric here is produced by the three scripts in this
directory (`wowii133_verify.c`, `wowii133_families.py`, `wowii133_sa.c`); the C verifier
*asserts* every lemma below on its whole exhaustive range and `exit(2)`s on the first
violation, so a false lemma would abort the run.

---

## 0. Verdict

**OPEN, but half of the conjecture is closed and the open part is pinned down exactly.**

* **Not disproved.** 0 counterexamples in
  **136 362 861** evaluations covering *every* connected graph on `n ≤ 10` vertices,
  **13 544 784** evaluations covering *every* connected `C₄`-free graph on `n ≤ 13`
  vertices, 79 structured graphs up to `n = 183` (Petersen, Hoffman–Singleton,
  incidence graphs of `PG(2,q)`, the extremal Erdős–Rényi polarity graphs `ER_q`,
  cages, random girth-5 regular graphs, …), and ≈ 2·10⁶ simulated-annealing graphs on
  `n = 10…24` targeted at minimising the slack.
* **Proved unconditionally (Theorem A):** the whole `hasC4` branch — for every connected
  graph containing a 4-cycle, `path(G) ≥ rad(G) + 1`.
* **Proved unconditionally (Theorem D + Theorem C):** the `C₄`-free branch whenever
  `⌊l(G)⌋ ≤ 2`. Combined with Theorem A this settles the conjecture for **every connected
  graph except the `C₄`-free ones with `⌊l(G)⌋ ≥ 3`, i.e. with `2m − 3T ≥ 3n`.**
  Concretely: for `n ≤ 13` exactly **622** of the 13 544 784 evaluations (top level
  counted with multiplicity, see §2.1) fall outside the proved region (all with `⌊l⌋ = 3`; none with `⌊l⌋ ≥ 4` exists below `n = 14`).
* **Proved for most of the remainder (Theorems E, F):** greedy induced-path bounds
  `path ≥ δ+2` (girth ≥ 5) and `path ≥ δ+1` (`C₄`-free) close all but **606** of the
  13 544 784 graphs — **99.9955 %** coverage by proof, 100 % for `n ≤ 10`.
  **SUPERSEDED 2026-08-18 (§12): Theorem G+ closes all 606 residual graphs; coverage over
  the whole exhaustive `C₄`-free range `n ≤ 13` is now 100.0000 %, residual 0.**
  §12 also *refutes* the "good pair" route for `rad ≥ 3` (§12.4) and reduces the whole of
  pocket 1 to the single residual problem (RP) of §12.5.
* The general case is genuinely open. §7 records **five named obstacles**, including an
  explicit witness (Hoffman–Singleton with one subdivided edge: `δ = 2`, `rad = 3`,
  `⌊l⌋ = 6`) showing that **no combination of the min-degree/radius lemmas proved here
  can ever prove the conjecture** — every proved bound is destroyed by one local surgery
  while `l` is not.
* **GAP:** nothing has been formalised in Lean; all proofs below are ordinary
  mathematics. The auxiliary claims A1/A4/A6/A7 of §6 are *verified, not proved*, and
  are labelled as such.

---

## 1. Exact statement, read off the Lean

`α` is a finite nontrivial vertex type and `G` is connected, so `n := |α| ≥ 2`.

* `path G` (`FormalConjecturesForMathlib/…/VertexDistance.lean`, `SimpleGraph.path`)
  `= max { |S| : S is the vertex set of an induced path of G }`. The empty and one-vertex
  lists satisfy `isInducedPath`, and for connected `n ≥ 2` we always have `path G ≥ 2`.
  **Semantics double-checked**: this is the *induced-path order*, not the "average
  distance" homonym flagged in the file for Conjecture 314.
* `G.radius.toNat` = `(⨅ u, eccent u).toNat` (Mathlib `SimpleGraph.radius`,
  `Combinatorics/SimpleGraph/Diam.lean`) = the ordinary radius `r := min_v ecc(v)`,
  finite because `G` is connected.
* `l G = averageIndepNeighbors G = (1/n) Σ_v α(G[N(v)])`, the **average** independence
  number of the *open* neighbourhoods (`…/Independence.lean`).
* `hasC4` in the Lean file is "there are 4 distinct vertices `a,b,c,d` with
  `ab, bc, cd, da ∈ E`", i.e. **a 4-cycle as a subgraph** (chords allowed), equivalently
  **some two distinct vertices have ≥ 2 common neighbours**. `cC4 = 1` iff `G` is
  `C₄`-free in that (subgraph) sense.
* `(⌊l G⌋ : ℝ) ^ cC4` uses `Monoid.npow`, so the `hasC4` branch is `⌊l⌋⁰ = 1`
  *regardless of the value of `l`* (this matters in principle; here `l ≥ 1` always,
  because every vertex of a connected `n ≥ 2` graph has `α(N(v)) ≥ 1`).

Both sides are integers cast into `ℝ`, so the Lean goal is equivalent to

> **(C133-a)** `G` connected with a 4-cycle: `path(G) ≥ rad(G) + 1`;
>
> **(C133-b)** `G` connected and `C₄`-free: `path(G) ≥ rad(G) + ⌊l(G)⌋`.

Throughout: `n = |V|`, `m = |E|`, `T = #triangles`, `d(v) = deg v`,
`t(v) = #triangles through v`, `δ = min degree`, `Δ = max degree`, `diam = diameter`,
`L_i` = the `i`-th BFS layer from a fixed vertex.

---

## 2. Falsification stage (requirement 1) — no counterexample

### 2.1 The enumerator and why it is complete

`wowii133_verify.c` generates connected graphs by **vertex augmentation**: from every
isomorphism class on `k` vertices it adds one new vertex joined to every non-empty subset
of the old ones. This is complete because *every connected graph on `k+1 ≥ 2` vertices has
a non-cut vertex*, whose deletion leaves a connected graph on `k` vertices. Isomorph
rejection uses a canonical certificate (1-WL colour refinement + branch-and-bound minimal
adjacency certificate); at the **last** level no rejection is done — duplicates are
harmless for a falsification search, so the last level is a *superset* of all classes.

Self-validation of the generator: the class counts it produces are
`1, 2, 6, 21, 112, 853, 11117, 261080` for `n = 2…9` — exactly the number of connected
graphs on `n` nodes (OEIS A001349). In `C₄`-free mode it produces
`1, 2, 3, 8, 19, 57, 186, 740, 3389, 18502, 120221` for `n = 2…12`, and the two
independent code paths agree exactly: the full enumerator finds **36 810** `C₄`-free
candidates up to `n = 10`, which is precisely the total the `C₄`-free-only enumerator
tests up to `n = 10`.

In `C₄`-free mode the children of a graph `G` are enumerated directly as the independent
sets of the auxiliary "conflict" graph (`u ∼ v` iff `N_G(u) ∩ N_G(v) ≠ ∅`), since adding a
vertex with neighbourhood `T` keeps the graph `C₄`-free **iff** no two members of `T` have
a common neighbour. A `hasC4` re-check on every generated graph guards this shortcut.

`path(G)` is computed exactly by DFS over induced paths with a `|remaining| ≤ best` prune;
`α(G[N(v)])` by exact branching; `rad` by BFS from every vertex.

### 2.2 Results

```
[A] all connected graphs, n = 2..9      tested 2 950 981     violations 0
[B] all connected graphs, n = 2..10     tested 136 362 861   violations 0     (superset of A)
[C] all connected C4-free, n = 2..13    tested 13 544 784    violations 0
[D] structural families (79 graphs, n ≤ 183)                 violations 0
[E] simulated annealing, C4-free, n = 10..24, ~2e6 proposals violations 0
```

`[D]` (`wowii133_families.py`) contains: `C_n` (n ≤ 15), `P_n`, stars, friendship graphs
`F_k`, Petersen = Kneser(5,2), Petersen chains and Petersen + pendant paths,
**Hoffman–Singleton** (n = 50, 7-regular, girth 5, `rad = 2`, `l = 7`, needs `path ≥ 9`,
has `path ≥ 20`), the incidence graphs of `PG(2,q)` for `q = 2,3,4,5,7,8,9` (girth 6,
n ≤ 182), the **Erdős–Rényi orthogonal polarity graphs `ER_q`** for `q ≤ 13` — the
extremal `C₄`-free graphs, `n = q²+q+1`, `≈ ½q(q+1)²` edges, `rad = 2`, the most dangerous
family since they maximise `l` at minimum radius — and 13 random girth-5 regular graphs.
Minimum slack in `[D]` is 0 (Petersen, `C₅`, `C₆`) and typically ≫ 0 for the large
families (e.g. `ER_13`: needs 9, has ≥ 9 by early-exit search; `IncidencePG(2,3)`: needs
7, has 11).

`[E]` (`wowii133_sa.c`) anneals over connected `C₄`-free graphs minimising
`path − rad − ⌊l⌋` (and, in a second variant, the real-valued `n(path−rad) − Σ_v α(N(v))`).
For `n ≥ 14` it never found slack below **1**.

### 2.3 Equality cases (these constrain any proof)

Over the entire exhaustive range the `C₄`-free branch is **tight** for exactly five
graphs: `K₂`, `K₃`, `C₅`, `C₆`, **Petersen**.

| G | n | rad | l | ⌊l⌋ | path | RHS |
|---|---|---|---|---|---|---|
| K₂ | 2 | 1 | 1 | 1 | 2 | 2 |
| K₃ | 3 | 1 | 1 | 1 | 2 | 2 |
| C₅ | 5 | 2 | 2 | 2 | 4 | 4 |
| C₆ | 6 | 3 | 2 | 2 | 5 | 5 |
| Petersen | 10 | 2 | 3 | 3 | 5 | 5 |

Any proof must be exactly sharp on all five; in particular no argument that "loses a
constant" can work.

---

## 3. Structure of the `C₄`-free branch

**Lemma 1 (local matching).** If `G` is `C₄`-free then for every `v` the graph `G[N(v)]`
has maximum degree ≤ 1, i.e. it is a matching. Consequently
`α(G[N(v)]) = d(v) − t(v)`, `d(v) ≥ 2t(v)`, and

  `l(G) = (1/n) Σ_v (d(v) − t(v)) = (2m − 3T)/n`.

*Proof.* If `u ∈ N(v)` had two neighbours `w₁,w₂ ∈ N(v)` then `v w₁ u w₂ v` is a 4-cycle on
4 distinct vertices. So `G[N(v)]` is a disjoint union of `t(v)` edges and `d(v) − 2t(v)`
isolated vertices (an edge inside `N(v)` is exactly a triangle through `v`); a maximum
independent set takes one endpoint of each edge and all isolated vertices, giving
`t(v) + (d(v) − 2t(v)) = d(v) − t(v)`. Summing and using `Σ_v t(v) = 3T`,
`Σ_v d(v) = 2m` gives the last identity. ∎

(Checked numerically on 3 000 random connected `C₄`-free graphs — 0 mismatches.)

So **(C133-b) is the statement `path(G) ≥ rad(G) + ⌊(2m − 3T)/n⌋` for connected `C₄`-free
`G`**; for girth ≥ 5 it is `path ≥ rad + ⌊average degree⌋`.

Two immediate consequences used below: `l ≥ 1` always, and `⌊l⌋ ≥ 2` forces `2m − 3T ≥ 2n`
(so every tree, and more generally every graph with `2m < 2n + 3T`, has `⌊l⌋ ≤ 1`).

---

## 4. What is proved

### Theorem A (the `hasC4` branch — complete)

*For every connected `G`, `path(G) ≥ rad(G) + 1`; in particular (C133-a) holds.*

*Proof.* Let `c` be a centre, `ecc(c) = r = rad`, and `z` with `dist(c,z) = r`. A shortest
`c–z` path `u₀…u_r` is an induced path: a chord `u_i u_j` with `j ≥ i+2` would give a
`c–z` walk of length `< r`. It has `r+1` vertices. ∎

Note this is the *whole* `hasC4` branch, because there `RHS = rad + ⌊l⌋⁰ = rad + 1`.

### Theorem B (`⌊l⌋ ≤ 1` — complete)

*If `⌊l(G)⌋ ≤ 1` then (C133-b) holds.* Immediate from Theorem A.

### Theorem C (radius ≤ 1 in the `C₄`-free branch — complete)

*If `G` is connected, `C₄`-free, `n ≥ 2` and `rad(G) ≤ 1`, then `l(G) < 2`, hence
`⌊l(G)⌋ = 1` and (C133-b) holds.*

*Proof.* Let `v` be a dominating vertex, so `N(v) = V∖{v}`. By Lemma 1, `G − v` is a
matching: say `a` edges and `b` isolated vertices, `n = 1 + 2a + b`. Then
`α(N(v)) = a + b`; a vertex `u` matched to `u'` has `N(u) = {v,u'}` with `v ∼ u'`, so
`α(N(u)) = 1`; an unmatched `u` has `N(u) = {v}`, `α(N(u)) = 1`. Hence
`Σ_w α(N(w)) = (a+b) + 2a + b = 3a + 2b < 2(1 + 2a + b) = 2n`, i.e. `l < 2`. ∎

(So the `C₄`-free windmills — stars, friendship graphs and their mixtures — are exactly
the radius-1 `C₄`-free graphs, and they are never a problem.)

### Theorem D (new; `C₄`-free, radius ≥ 2 — complete)

*If `G` is connected, `C₄`-free and `rad(G) ≥ 2`, then `path(G) ≥ rad(G) + 2`.*

*Proof.* Write `r = rad(G)`.

*Case 1: `diam(G) ≥ r+1`.* A geodesic between two vertices at distance `diam` is induced
(Theorem A's argument) and has `diam + 1 ≥ r + 2` vertices.

*Case 2: `diam(G) = r`.* Since `rad ≤ ecc(v) ≤ diam` for every `v`, **every vertex is a
centre**.

*Case 2a: some vertex `c` has `d(c) ≥ 3`.* Pick `z` with `dist(c,z) = ecc(c) = r ≥ 2` and a
geodesic `c = u₀, u₁, …, u_r = z`. At most one vertex of `N(c)∖{u₁}` is adjacent to `u₁`:
two such vertices `x, x'` would give the 4-cycle `c x u₁ x' c` on 4 distinct vertices.
As `|N(c)∖{u₁}| ≥ 2`, choose `x ∈ N(c)∖{u₁}` with `x ≁ u₁`. Then
`x, c, u₁, …, u_r` is an induced path on `r+2` vertices:
  * `x ≠ u_i` for all `i` (`dist(c,x) = 1`, `x ≠ u₁`, and `dist(c,u_i) = i ≥ 2` for `i ≥ 2`);
  * `x ≁ u₁` by choice;
  * `x ≁ u₂`, else `c x u₂ u₁ c` is a 4-cycle on 4 distinct vertices;
  * `x ≁ u_i` for `i ≥ 3`, since `dist(x,u_i) ≥ dist(c,u_i) − 1 = i − 1 ≥ 2`;
  * `u₀…u_r` is induced and `x ∼ c`.

*Case 2b: `Δ ≤ 2`.* Then `G` is a path or a cycle. A path `P_n` has `diam = n−1` and
`rad = ⌈(n−1)/2⌉`, so `diam = rad` forces `n ≤ 2`, contradicting `rad ≥ 2`. So `G = C_n`;
`C₃` has `rad = 1` and `C₄` is not `C₄`-free, so `n ≥ 5`, and
`path(C_n) = n − 1 ≥ ⌊n/2⌋ + 2 = rad + 2` because `⌈n/2⌉ ≥ 3`. ∎

**Corollary D1 (the main proved result).** *Conjecture 133 holds for every connected graph
that contains a 4-cycle, and for every connected `C₄`-free graph with `⌊l(G)⌋ ≤ 2`.*

*Proof.* Theorem A; and for `C₄`-free `G`: if `⌊l⌋ ≤ 1` use Theorem B; if `⌊l⌋ = 2` then
`rad ≥ 2` by Theorem C, and Theorem D gives `path ≥ rad + 2`. ∎

Theorem D is tight (`C₅`, `C₆`) and is verified over the whole exhaustive range by
`wowii133_verify.c` (assertion `THEOREM-D FAILS`, never triggered).

### Theorem E (greedy induced path — complete)

*(E1) If `G` is `C₄`-free and triangle-free (girth ≥ 5) with `δ ≥ 2`, then
`path(G) ≥ δ + 2`.*
*(E2) If `G` is `C₄`-free with `δ ≥ 3`, then `path(G) ≥ δ + 1`.*

*Proof.* Grow an induced path `v₁…v_k` greedily. A vertex `x ∈ N(v_k)` fails to extend it
iff `x` lies on the path or `x ∼ v_i` for some `i ≤ k−1`. Count the failures:
  * `v_{k−1}` is the only path vertex in `N(v_k)` (the path is induced): 1;
  * `i = k−1`: a common neighbour of `v_{k−1}` and `v_k` is a triangle-mate, and `C₄`-freeness
    allows at most one: `≤ 1`, and `0` if `G` is triangle-free;
  * `i = k−2`: `v_{k−1}` is already a common neighbour of `v_{k−2}` and `v_k`, so by
    `C₄`-freeness there is **no other**: `0`;
  * `i ≤ k−3`: each `v_i` has at most one common neighbour with `v_k`: `≤ k−3`.

Hence an extension exists as soon as `d(v_k) ≥ k` (`C₄`-free, `k ≥ 3`), resp.
`d(v_k) ≥ k−1` and `≥ 2` (girth ≥ 5). Starting from any vertex, the steps `k = 1 → 2` and
`2 → 3` need `d ≥ 1` resp. `d ≥ 3` (`C₄`-free) or `d ≥ 2` (girth ≥ 5), and step `k → k+1`
needs `d ≥ k` resp. `k−1`. With `δ` as stated the greedy runs until `k = δ+1` resp.
`k = δ+2`. ∎

E1 is tight for `C₅` (`δ=2`, path 4) and **Petersen** (`δ=3`, path 5); E2 is tight for `K₃`
after the `δ ≥ 3` exclusion. Both are asserted over the whole exhaustive range
(`THEOREM-E1/E2 FAILS`, never triggered).

**Corollary E3.** *If `G` is `C₄`-free of girth ≥ 5 with `rad = 2` and `⌊l⌋ ≤ δ`, the
conjecture holds.* In particular it holds for **every regular graph of girth ≥ 5 and
radius 2** — i.e. for all Moore graphs (`C₅`, Petersen, Hoffman–Singleton, and the
hypothetical 57-regular one), since there `l = δ` exactly and `path ≥ δ+2 = rad + l`.

### Theorem F (geodesic + greedy — complete)

*If `G` is connected `C₄`-free with `δ ≥ 4`, then `path(G) ≥ rad(G) + ⌊δ/2⌋`.*

*Proof.* Let `c` be a centre, `r = rad`, `z ∈ L_r`, `u₀…u_r` a geodesic; set `w₀ = z` and
extend greedily `w₁, w₂, …` at the `z` end. Because one step changes the BFS layer by at
most 1, `w_{j−1} ∈ L_{≥ r−j+1}`, hence `dist(u_i, w_{j−1}) ≥ (r−j+1) − i`, so only the
`≤ j+2` vertices `u_i` with `i ≥ r−j−1` can be within distance 2 of `w_{j−1}`. Each path
vertex `y ≠ w_{j−1}` blocks at most one candidate (`|N(y) ∩ N(w_{j−1})| ≤ 1` by
`C₄`-freeness), and one further candidate slot is lost to the path vertex `w_{j−2} ∈
N(w_{j−1})`. Hence at most `(j+2) + (j−2) + 1 = 2j+1` neighbours of `w_{j−1}` are unusable
and step `j` succeeds whenever `d(w_{j−1}) ≥ 2j+2`. With min degree `δ` all steps
`j ≤ ⌊δ/2⌋ − 1` succeed, giving an induced path on `(r+1) + ⌊δ/2⌋ − 1` vertices. ∎

(Also asserted over the exhaustive range.)

---

## 5. Coverage of the proved results (requirement 3)

`wowii133_verify.c` computes, for every generated `C₄`-free graph, the best lower bound
obtainable from Theorems A/D/E/F and compares it with `rad + ⌊l⌋`:

```
all connected C4-free graphs, n ≤ 10 :  36 810 tested, 36 810 covered      (100.0000 %)
all connected C4-free graphs, n ≤ 13 : 13 544 784 tested, 13 544 178 covered ( 99.9955 %)
   residual profile:  rad=2, ⌊l⌋=3 : 516      rad=3, ⌊l⌋=3 : 90
   residual min degrees: δ ∈ {2,3};  both triangle-free and triangle cases occur
```

So after Corollary D1 the open region is `⌊l⌋ ≥ 3`, and inside it the greedy bounds leave
only 606 graphs on `≤ 13` vertices, every one of which is **one vertex short**: they need
`path ≥ rad + 3` while the proofs deliver `rad + 2`. (For `n ≤ 13` there are 622 `C₄`-free
graphs with `⌊l⌋ = 3` at all, and none with `⌊l⌋ ≥ 4`; the smallest `⌊l⌋ = 3` example is
the Petersen graph, which *is* covered, by E1.)

A partial extension of Theorem D to `rad + 3` is easy in two of the three cases
(`diam ≥ rad+2`: geodesic; `diam = rad+1`: extend a diametral geodesic at an endpoint of
degree ≥ 3), and in the self-centred case the same two-step extension works whenever the
chosen `x ∈ N(c)` has `d(x) ≥ 3` and girth ≥ 5 — this is exactly how Petersen attains
`path = 5`. What is missing is the bookkeeping for the low-degree/triangle sub-cases; that
is a finite but fiddly analysis and was not completed here.

---

## 6. Auxiliary claims discovered (verified, **not** proved)

These were tested by the same exhaustive machinery; each is stated with its exact
verification range. **None of them is used in §4.**

| # | claim | range verified | violations |
|---|---|---|---|
| **A1** | every connected `G`: `path ≥ 2·rad − 1` | all connected `n ≤ 10` (136 362 861) | 0 |
| **A4** | `C₄`-free: `path ≥ rad + δ − 1` | all `C₄`-free `n ≤ 13` | 0 |
| **A6** | `C₄`-free, `G ≠ K₃`: `path ≥ rad + δ` | all `C₄`-free `n ≤ 13` | 1 (`K₃` only) |
| **A7** | `C₄`-free: `l(G) ≤ path(G) − rad(G)` (real-valued!) | all `C₄`-free `n ≤ 13`, all connected `n ≤ 10` | 0 |

**A7 is the natural floor-free strengthening of (C133-b)**: `Σ_v α(G[N(v)]) ≤ n·(path−rad)`,
i.e. `2m − 3T ≤ n(path − rad)`. It is tight for `K₂`, `K₃`, `C₅`, `C₆`, Petersen (same five
graphs) and is false without the `C₄`-free hypothesis (`K_{3,3}`: `l = 3`, `path − rad = 1`).
Proving A7 would prove the conjecture; it looks like the right target.

A1 is worth isolating: it would settle every case with `⌊l⌋ ≤ rad − 1`. A partial proof:
let `P = v₁…v_p` be a *maximum* induced path, `u` any vertex, `t = dist(u,P)`, `q_t…q₀` a
geodesic from `u` to `P` and `A = {a₁ < … < a_z}` the indices of the `P`-neighbours of `q₁`.
Minimality of `a₁` (maximality of `a_z`) makes `q_t…q₁v_{a₁}v_{a₁−1}…v₁` and
`q_t…q₁v_{a_z}…v_p` induced, so `t + a₁ ≤ p` and `t ≤ a_z − 1`; and for consecutive
indices `t + (a_{j+1} − a_j) ≤ p`. If `A` lies entirely on one side of the middle index
`f = ⌈(p+1)/2⌉` these give `dist(u, v_f) ≤ (p−1)/2` directly, hence `rad ≤ (p+1)/2`, i.e.
A1. The straddling case (`a_j < f < a_{j+1}`) is **not** closed by these inequalities;
that is the gap.

---

## 7. Why the routes tried do not close it — named obstacles

**O1 — surgery/robustness (the decisive one).** Every bound proved in §4 is driven by
`δ` or by `rad`. Both are destroyed by a single local modification, while `l` moves by
`O(1/n)`. Explicit witness (computed in `wowii133_families.py`): **Hoffman–Singleton with
one edge subdivided**, `n = 51`, `C₄`-free, `δ = 2`, `rad = 3`, `l = 6.902`, `⌊l⌋ = 6`.
The conjecture needs `path ≥ 9` (true: `path ≥ 20`), while
`max(rad+2, δ+2, rad+⌊δ/2⌋) = 5`. So Theorems D/E/F **cannot** be combined into a proof:
the correct proof must use a quantity as robust as `l` itself.

**O2 — the degeneracy factor 2.** All greedy arguments really bound `path` by
`2 + max_H δ(H)` over induced subgraphs `H`, i.e. by the *degeneracy*, and degeneracy can
be as small as `d̄/2`. The conjecture needs `≈ d̄`. Closing that factor 2 for `C₄`-free
graphs is the sharp form of Kühn–Osthus-type theorems (attribution from memory, not
verified — this attack was run without web access) ("`K_{s,s}`-free graphs of large
average degree contain induced subdivisions"), for which only tower-type bounds are known.
This is where any asymptotic attack stalls.

**O3 — no per-vertex charging.** The star `K_{1,m}` has `α(N(centre)) = m` but `path = 3`,
so no bound of the form "`path ≥ f(α(N(v))) + g(v)` for some vertex `v`" can exist: the
proof must genuinely average, which none of routes 1–3 (BFS layering, neighbourhood
constraints on shortest paths, minimal counterexample) does.

**O4 — sharpness at the bottom.** `K₂, K₃, C₅, C₆, Petersen` all attain equality, so no
argument may lose even one vertex on them. In particular Theorem D + one more extension
step must be *exactly* tight on Petersen (it is), leaving no slack for a crude case
analysis.

**O5 — the induction that almost works.** For a pendant vertex `v` with support `w`:
`Σ_u α(N(u))` drops by exactly 2 and `n` by 1, so `l(G−v) ≥ l(G)` **whenever `l ≥ 2`**;
also `rad(G−v) ≥ rad(G) − 1` and `path(G) ≥ path(G−v)`. Induction therefore yields
`path(G) ≥ rad(G) − 1 + ⌊l(G)⌋` — off by exactly one. Recovering the missing vertex needs
"some maximum induced path of `G−v` ends at `w`", which is false in general. The same
off-by-one appears for every other local reduction tried (subdividing, contracting a
triangle to a vertex).

---

## 8. Reproducing

```sh
cc -O2 -o w133 wowii133_verify.c
./w133 10 0        # all connected graphs on n <= 10   (93 s, 136M evaluations)
./w133 13 1        # all connected C4-free graphs n<=13 (~100 s, 13.5M evaluations)
./w133 9  0        # quick smoke test (~2 s)
python3 wowii133_families.py          # 79 structured graphs, n <= 183 (~11 s)
cc -O2 -lm -o sa133 wowii133_sa.c && ./sa133 18 1 40000   # adversarial search
```
`w133 MAXN C4FREE` prints per-level class counts, the number of violations of the
conjecture, the coverage of the proved lemmas, and aborts with `exit(2)` if any of
Theorems C/D/E1/E2/F ever fails. Both runs print `violations=0`.

---

## 9. Summary for the pipeline

* **(C133-a)** — the `hasC4` half of Conjecture 133 — is **proved** (Theorem A, 4 lines).
* **(C133-b)** is **proved for `⌊l⌋ ≤ 2`** (Corollary D1), the new ingredient being
  Theorem D (`C₄`-free, `rad ≥ 2` ⟹ `path ≥ rad + 2`).
* The only open region is **`C₄`-free with `2m − 3T ≥ 3n`**, where 99.9955 % of the
  small cases are additionally covered by Theorems E/F and 0 counterexamples exist below
  `n = 14` (and none in any structured family up to `n = 183`).
* The recommended next target is the floor-free strengthening **A7**
  (`2m − 3T ≤ n(path − rad)` for `C₄`-free `G`), and the recommended lemma to isolate is
  **A1** (`path ≥ 2·rad − 1`, all connected graphs), whose straddling case is the only gap.
* **GAP:** no Lean formalisation attempted; A1/A4/A6/A7 are verified but unproved.

---
# §9 新增（2026-08-18）：Theorem G 族 — μ 条件下的 rad+3（Qwen3.8-Max 求解会话产出，root 逐行亲核采纳）

记 μ := min_v α(G[N(v)])（C4-free 下 = min_v (d(v)−t(v))）。

**Lemma G0（双端测地线扩张）** C4-free，测地线 u0…ud（d≥2），a(u0)≥3 且 a(ud)≥3
⟹ 存在 d+3 顶点诱导路径。
[证明：见 notes/reviews/wowii133_qwen_solve.md 收割节，root 已逐行核验：
端点异分量邻居对、端集不相交（d=2 特判 C4）、非完全二部选 x≁y、
x/y 对 P 的非邻接（i=2 C4 / i≥3 捷径）。]

**Theorem G（主）** 连通 C4-free：path(G) ≥ rad(G) + min{3, μ}。
（严格强于 Theorem D；Petersen 上取等。）

**Cor G1** 三角形自由 + δ≥3 ⟹ path ≥ rad+3。
**Cor G2** δ≥5 ⟹ path ≥ rad+3（a(v) ≥ ⌈d(v)/2⌉）。
**Cor G3** ⌊l⌋≤3 且 μ≥3 ⟹ C133-b 成立。
**Cor G4** 存在两端 a≥3 的径向测地线 ⟹ path ≥ diam+3；
故 ⌊l⌋ ≤ diam−rad+3 且有此径向对 ⟹ C133-b 成立。

**对 606 个未覆盖图的影响**：全部 ⌊l⌋=3；其中 μ≥3 者被 Cor G3 直接消灭
（具体计数待跑：wowii133_verify.c 加 μ 过滤器——排入下次本地轻量计算窗口）。
**残余开放收窄为**：(i) ⌊l⌋=3 且 μ≤2 且无高-a 径向对；(ii) ⌊l⌋≥4（n≥14 起）。

---
# §10 追击轮（2026-08-18，Qwen 会话二问；root 逐行亲核全部采纳）

## Lemma G1（单端扩张——严格强于 Lemma G0）
C4-free，测地线 u0…ud（d≥2），**a(u0)≥3 且 a(ud)≥2** ⟹ 存在 d+3 顶点诱导路径。
关键改进：y 只需取自 N(ud) 中不含 u(d−1) 的另一分量（故只需 a≥2）；x1,x2 取自 N(u0)
中不含 u1 的两个分量（需 a≥3）；若 y 同时邻接 x1,x2 则 u0 与 y 有两公共邻居 ⟹ C4。
[root 亲核：不交性隐含成立——Claim 1 已证 y ≁ u0（d=2 用 C4、d≥3 用捷径），
故 y ∉ N(u0) ∋ x，x≠y 自动；x,y ∉ P 亦由两 Claim 覆盖。✅]

## Theorem G'（半径版）
若存在距离 = rad 的顶点对，其 a 值为 (≥3, ≥2)（任意顺序），则 path ≥ rad+3。
故 ⌊l⌋=3 且存在此种距离-rad 对 ⟹ C133-b 成立。

## Lemma G2（a=1 的分类）
C4-free 中 a(v)=1 ⟺ v 是叶，或 v 恰有两个互相邻接的邻居（三角形上的"叶"）。

## Theorem G3（口袋 1 反例的结构定理）
设 G 连通 C4-free、r=rad≥2、⌊l⌋=3、path=r+2（即口袋 1 反例）。则：
(i) diam ≤ r+1；(ii) 不存在距离 ≥r 且 a 值为 (≥3,≥2) 的顶点对；
(iii) 记 H={a≥3}、M={a=2}，则 dist(H, H∪M) ≤ r−1；
(iv) 每条中心-离心测地线的端点类型只能是 (≤2,≤2)、(≥3,1)、(1,≥3)；
(v) 与任一 a≥3 顶点距离恰为 r 的顶点必有 a=1（由 G2 即叶或三角形叶）。
**口袋 1 因此严格缩小**（原先只排除 (3,3)，现连 (3,2)/(2,3) 一并排除）。

## 口袋 2：k 端推广被证伪（重要负结果）
反例族 T_m：路径 u−x−v，u 与 v 各挂 m 片叶。树故 C4-free；rad=2；
a(u)=a(v)=m+1 可任意大；但 **path(T_m)=5 恒定**。故 k≥4 时 rad+k>5，
"两端 a≥k ⟹ path ≥ rad+k" 必假。
[root 亲核 ✅，并验证其不与猜想矛盾：l=(4m+4)/(2m+3)→2，⌊l⌋=2，path=5 ≥ rad+2 ✓
——它杀的是证明技术而非猜想。]
**方法论结论**：⌊l⌋≥4 不可能靠端点局部信息攻下，必须用全局平均论证。

## 残余（收窄后）
- 口袋 1 唯一缺口 = **开放平均命题**：连通 C4-free、r≥2、l≥3 ⟹ 或 path≥r+3，
  或存在距离-r 的 (≥3,≥2) 顶点对。（证之则 Lemma G1 直接封口袋 1。）
  困难：大 l 可由半径 < r 的高-a 稠密核 + 长的低-a 附肢造出（Hoffman–Singleton 加悬挂点型）。
- 口袋 2：需全局平均，端点法已死。

---
# §11 三问轮（2026-08-18，Qwen；root 逐行亲核全部采纳）

记 (★) := 不存在距离恰为 r 且 a 值为 (≥3,≥2) 的顶点对（即口袋 1 反例的定义性假设）。

## Lemma G4（高顶点必是中心）
假设 (★)。若 a(h)≥3 则 ecc(h)=r。
[root 亲核：反证 ecc(h)≥r+1，取测地线 p_0..p_e；p_r 距 h 恰为 r，由 (★) 得 a(p_r)=1；
p_r 有两邻居 p_{r±1}，由 G2（a=1 分类）得 d(p_r)=2 且 p_{r−1}∼p_{r+1}；
于是 h→p_{r−1}→p_{r+1} 只需 r 条边，与 dist(h,p_{r+1})=r+1 矛盾。✅]

## Lemma G5（高心测地线的内点皆为中档）
假设 (★)，h 高顶点、h..z 为到离心点的测地线，则每个内点 p_i（1≤i≤r−1）有 a(p_i)≥2。
[同型论证：a(p_i)=1 ⟹ p_{i−1}∼p_{i+1} ⟹ 测地线可缩短。✅]
故任何反例中，高心到离心球的测地线形如 (≥3),(≥2),...,(≥2),(1)——极其刚性。

## Lemma G6（删 a=1 顶点保距且保 l≥3）
C4-free 中 a(v)=1 ⟹ 删 v 不改变其余顶点间距离；且 l≥3 时删后仍 l≥3。
[root 亲核计数：叶情形 S 降 2（v 在其邻居的邻域中是孤立分量）；
三角叶情形 S 降 1（边分量退化为孤立分量，分量数不变）；
(S−2)/(n−1)≥3 ⟸ S≥3n−1、(S−1)/(n−1)≥3 ⟸ S≥3n−2，均由 S≥3n 推出。✅]

## **Theorem G7（r=2 情形全解决）**
r=rad(G)=2 且 l(G)≥3 ⟹ 或 path(G)≥5，或存在距离-2 的 (≥3,≥2) 顶点对。
[证明骨架：反证下由 G4 得高顶点 h 是中心、ecc(h)=2；A:=N(h)、B:=距离 2 层，
由 (★) 全部 b∈B 有 a(b)=1。四步结构分析：①B 中每点在 A 中有唯一父（否则 h,b 有两公共邻居⟹C4）；
②不同纤维间无边（否则该点邻域出现两分量⟹a≥2）；③纤维内 G[B_a] 是匹配+孤立点；
④G[A] 亦然。由此 a(h)=m−p、a(a)=1+s_a+q_a、a(b)=1，求和得
Σ = 2m−p+2S+3Q，n = 1+m+S+2Q，故 **3n−Σ = 3+m+p+S+3Q ≥ 3 > 0** ⟹ l<3，矛盾。✅]

**root 补注（比原陈述更强）**：上述推导全程未用到 path=4 这一假设——矛盾只由
(★)+r=2+存在高顶点 导出。故实际证明的是：**r=2 且 l≥3 ⟹ 必存在距离-2 的 (≥3,≥2) 对**
（无需 path 那一支）。这使 G7 可直接接 Lemma G1 用。

## Corollary G8（口袋 1 的 r=2 层完全关闭）
r=2 且 ⌊l⌋=3 ⟹ path ≥ 5 = rad+3 ⟹ C133-b 成立。
[G7 给出好对，Lemma G1 把它扩成 2+3=5 顶点诱导路径。✅]

## 残余（再次收窄）
**口袋 1 只剩 r≥3。** 其反例必须同时满足：所有高顶点都是中心；高顶点的离心球全是
a=1（叶或三角叶）；高心测地线内点全为中档；由 G6，极小反例中删任一 a=1 顶点必须降低半径。
Qwen 未能排除也未能构造。⌊l⌋≥4 仍需全局平均（k 端法已由 T_m 证伪）。

---
# §12 owner-w133 第一轮（2026-08-18，opus）

本节全部数值由 `problems/wowii/wowii133_gplus.c`（= `wowii133_verify.c` 加断言，穷举
连通 C4-free `n ≤ 13`，任一断言失败即 `exit(2)`，日志 `problems/wowii/w133_gplus_n13.out`）
与 `problems/wowii/w133_r3_counterexample.py`（HS 构造与证书）产生。**先跑后写。**

## 12.0 T002 收割件（Qwen 第 4 轮）逐行核验结论

| 条目 | 裁决 | 备注 |
|---|---|---|
| Theorem 4′（r=2 无析取支） | **重复** | 即 draft §11 Theorem G7 的 root 补注，非新增 |
| Lemma 9（S_r(h) 落在 G−h 的单一分量） | **VALID** | 两条测地线拼接得 2r+1 ≥ r+3 顶点诱导路径；跨分量无边、x₁≁y₁ 均成立 |
| Lemma 10（非深分量无高顶点） | **VALID** | dist(v,z)=dist(v,h)+r ≥ r+1 与 Lemma G4（ecc(h)=r）矛盾 |
| Lemma 11（删 a=1 顶点半径至多降 1） | **VALID** | 平凡但正确 |
| Lemma 12（加叶/三角叶使半径 +1 的充要条件） | **VALID** | 两向论证完整，二分（dist=ρ 或 ≤ρ−1）穷尽 |
| §6 极小反例推理 | **VALID** | 关键点 a_{G−v} ≤ a_G 保证"无好对"性质下传，Qwen 未明写但成立 |

**总评**：无假证明，但 Lemma 9/10 均以"反例且 path=r+2"为前提，属条件性结构结论，
不关闭任何缺口；Qwen 自评 PARTIAL 属实。**更重要的是：12.4 表明其主攻方向（TASK 攻击线
(1)）不可能成功。** 按"同源不自审"，本节结论不得送回 Qwen 审。

## 12.1 Lemma G10（单端扩张，+1 顶点）

*G 为 C4-free，u₀…u_d 是测地线，d ≥ 2，a(u_d) ≥ 2 ⟹ path(G) ≥ d+2。*

*证.* 由 Lemma 1，G[N(u_d)] 是匹配，其分量数 = a(u_d) ≥ 2，取 x 属于不含 u_{d−1} 的分量。
则 (i) x ≠ u_i：dist(u_d,x)=1 而 dist(u_d,u_i)=d−i，只有 i=d−1 可能，已排除；
(ii) x ≁ u_{d−1}（异分量）；(iii) x ≁ u_{d−2}，否则 x,u_d,u_{d−1},u_{d−2} 四个相异顶点
构成 4-圈；(iv) i ≤ d−3 时 dist(x,u_i) ≥ (d−i)−1 ≥ 2。故 u₀…u_d,x 诱导，d+2 顶点。∎

## 12.2 Lemma G9（双端 a≥2，需 d ≥ 4）

*G 为 C4-free，u₀…u_d 是测地线，**d ≥ 4**，a(u₀) ≥ 2 且 a(u_d) ≥ 2 ⟹ path(G) ≥ d+3。*

*证.* 两端各按 G10 取 x ∈ N(u₀)、y ∈ N(u_d)（分别在不含 u₁、不含 u_{d−1} 的分量）。
G10 的 (i)–(iv) 给出 x,y ∉ P 且 x,y 与所有 u_i 不邻接。又 dist(x,y) ≥ dist(u₀,u_d)−2
= d−2 ≥ 2，故 x ≠ y 且 x ≁ y。于是 x,u₀,…,u_d,y 诱导，d+3 顶点。∎

**d ≥ 4 不可去**：d=3 时 x,y 可能相邻（得诱导 C₆ 而非 P₆）。数值：`n ≤ 13` 穷举中
存在 **334** 个 (u,z) 对满足 dist=3、两端 a≥2 而 path < 6。故 d=3 版本为假。

## 12.3 **Theorem G+**（本轮主结果，严格强于 Theorem G）

*G 连通 C4-free，μ := min_v a(v) ≥ 2，且存在 h 使 a(h) ≥ 3。则*
  **path(G) ≥ ecc(h) + 3 ≥ rad(G) + 3**（设 rad ≥ 2）。

*证.* 取 z 使 dist(h,z) = ecc(h) =: d ≥ rad ≥ 2。a(h) ≥ 3、a(z) ≥ μ ≥ 2，
直接套 **Lemma G1**（§10）得 d+3 顶点诱导路径。∎

**Corollary G+1.** *G 连通 C4-free、l(G) ≥ 3 且**无 a=1 顶点**（由 Lemma G2 即：无叶、
无三角叶）⟹ path(G) ≥ rad(G)+3，故 C133-b 对 ⌊l⌋ ≤ 3 成立。*
*证.* l ≥ 3 ⟹ Σa ≥ 3n ⟹ 某 a(h) ≥ 3；l ≥ 3 > 2 与 Theorem C 给 rad ≥ 2。∎

对比：Theorem G 给 rad + min{3,μ}，μ=2 时只有 rad+2；G+ 把 μ=2 一档整体提到 rad+3。
数值：`n ≤ 13` 穷举无反例；**并入覆盖后 C4-free 残余从 606 降到 0（100.0000%）**，
622 个 ⌊l⌋=3 图**全部**被 G+ 单独消灭（它们全部 μ ≥ 2）。

## 12.4 **攻击线 (1)（分层计数推广）被证伪 —— 决定性负结果**

记 **(GP_r)**：连通 C4-free、rad=r、l ≥ 3 ⟹ 存在 dist ≥ r 且 a 值为 (≥3,≥2) 的顶点对。
Theorem G7 / Qwen Theorem 4′ = **(GP₂) 为真**。

> **命题 12.4.1（新）：(GP₃) 为假。**

**证人 A**（`w133_r3_counterexample.py`，全部数值已跑）：**Hoffman–Singleton 每个顶点挂 2 片叶**。
n=150，m=275，连通，**C4-free**（girth 5），**rad=3**，diam=4，Σa=550，
**l=11/3=3.667，⌊l⌋=3**（正落在口袋 1），而
**"dist ≥ rad 且 (≥3,≥2)"的顶点对数 = 0**；实际"两端 a≥2 的最大距离 = 2 < rad"。
理由一句话：a ≥ 2 的顶点恰是 50 个 HS 顶点，它们两两距离 ≤ diam(HS) = 2 < 3 = rad；
距离 ≥ 3 的一切顶点都是叶，a = 1。猜想本身仍成立（诱导路径证书 16 顶点 ≥ rad+⌊l⌋ = 6）。

**推论（这就是 T002 任务书攻击线 (1) 的死刑）**：攻击线 (1) 要证的是
"(★) ∧ r ≥ 3 ∧ 存在高顶点 ⟹ 3n − Σ > 0"。证人 A 满足 (★)、r=3、有 50 个高顶点，
而 3n − Σ = 450 − 550 = **−100 < 0**。故 Theorem G7 的纤维计数**不可能**推广到 r ≥ 3，
draft §10 记下的"HS 加悬挂点型"担忧被坐实为真障碍。

**证人 B**：HS + 3 片叶（挂在两两距离 2 且无公共邻点的 0,2,5 上），n=53，rad=3，⌊l⌋=6，
同样 0 个好对 —— 说明**只需 3 片叶**就能把半径从 2 顶到 3 并摧毁全部好对。

**与 Qwen Lemma 9/10 的关系**：不矛盾。A、B 的 path 远大于 r+2，故不落在其"path=r+2"
前提内。但 A 满足 Qwen §9 所列的**全部**结构性必要条件（除 path=r+2 一条），
故那组条件**本身不足以**逼出 Σ < 3n：**r ≥ 3 的证明必须真的造出诱导路径，
不能只靠结构+计数。**

## 12.5 新框架：剥皮归纳（Peeling Induction）与精确残余

> **Theorem X（目标，证之即口袋 1 全关）：连通 C4-free、l(G) ≥ 3 ⟹ path(G) ≥ rad(G)+3。**

**Lemma G11（松弛严格单调，比 G6 强）.** C4-free 中 a(v)=1 ⟹
S(G−v) − 3(n−1) ≥ (S(G) − 3n) + 1。
*证.* v 是叶（邻点 x）：a(v)=1 且 v 在 G[N(x)] 中是孤立点，故删后 a(x) 恰降 1，其余不变，
S 降 2、n 降 1，松弛 +1。v 是三角叶（邻点 x~y）：{v,y} 是 G[N(x)] 的一条边分量，删 v 后
退化为孤立点 y，贡献仍为 1，故 a(x)、a(y) 均不变；S 降 1、n 降 1，松弛 +2。∎

**归纳骨架（对 n 归纳）.**
* rad ≥ 2 自动（Theorem C）。
* **基例** Λ := {v : a(v)=1} = ∅ ⟹ **Theorem G+** 直接给 path ≥ rad+3。✓
* **归纳步** 取 v ∈ Λ。G−v 连通、C4-free、在 V∖{v} 上**保距**（G6）、l ≥ 3（G11），
  且 path(G) ≥ path(G−v)。**若 rad(G−v) = rad(G) 则归纳闭合。**
* 故**唯一残余** = Λ ≠ ∅ 且**每个** v ∈ Λ 删去都掉半径（Qwen Lemma 11 保证至多掉 1，
  Lemma 12 给出充要刻画）。称此为 **radius-critical** 情形。

**残余中可免费使用的四条化归**：
(R1) diam ≥ rad+2 ⟹ 测地线诱导，path ≥ diam+1 ≥ rad+3 ✓（对一切连通图成立）。故 diam ≤ rad+1。
(R2) diam = rad+1 且某对径点有一端 a ≥ 2 ⟹ **Lemma G10** 给 path ≥ diam+2 = rad+3 ✓。
     故一切对径点对两端都在 Λ 中。
(R3) **Lemma G1** ⟹ 无 dist ≥ rad 的 (≥3,≥2) 对（即 (★) 自动成立）。
(R4) **Lemma G9** ⟹ 无 dist ≥ max(rad,4) 的 (≥2,≥2) 对。故 **rad ≥ 4 时全体 a≥2 顶点两两距离 ≤ rad−1**。

**核分解（rad ≥ 4）.** 由 Lemma G2，Λ 的每个元素是叶或三角叶，故
(a) 最短路的**内点**不可能属于 Λ（叶度数 1；三角叶可被其两邻点的边抄近路），
    于是 **C := G − Λ 连通且在 G 中等距**；
(b) 每个 Λ 顶点都有核邻点（否则 G = K₂ 或 K₃，l = 1）；
(c) 由 G11 逐个删去，S(C) − 3n_C ≥ (S−3n) + |Λ| ≥ 1，故 **l(C) > 3**；
(d) 由 (R4) diam(C) ≤ rad−1，由 (b) 每个核顶点 ecc_G ≤ diam(C)+1 ≤ rad，又 ≥ rad，
    故**每个核顶点都是中心**，且 **C 自中心、rad(C) = diam(C) = rad(G) − 1 =: D**；
(e) 记 P := 有 Λ-邻点的核顶点（"父集"），则**覆盖条件**：∀u ∈ C ∃p ∈ P，dist_C(u,p) = D。

对 C 用归纳（n_C < n、l(C) > 3）得 path(C) ≥ rad(C)+3 = D+3 = rad(G)+2 —— **还差 1**。
若某条 C 中的 D+3 顶点诱导路径**有一端落在 P 中**，接上那片叶即得 D+4 = rad(G)+3 ✓。

> **残余问题 (RP)（本题现在唯一的缺口，已被压到极窄）：**
> 设 C 连通 C4-free、自中心 rad(C)=diam(C)=D、l(C) > 3，P ⊆ V(C) 满足
> ∀u ∃p∈P dist(u,p)=D。求证 C 有一条 **D+3 顶点、至少一端落在 P** 的诱导路径
> （或 **D+2 顶点、两端都落在 P**）。
> 已知的免费下界只有"P 中距离 D 的一对之间的测地线"= D+1 顶点，**恰差一个顶点**。
> rad = 3 需单独处理（(R4) 要 d ≥ 4，故核内可能出现距离 3 的 (2,2) 对）。

**框架的经验验证**（`w133_r3_counterexample.py` 的 `analyse_residual`）：
* 证人 A：Λ=100、μ=1、**非** radius-critical（删任一叶半径仍为 3）⟹ 归纳步直接吞掉。
* 证人 B：Λ=3、μ=1、**是** radius-critical ⟹ 落在真残余里；其 C=HS 自中心 D=2、
  覆盖条件成立、(RP) 成立（HS 中存在 5 顶点诱导路径以父点 0 为端点）⟹ path ≥ 6 = rad+3 ✓。
  **即：目前唯一已知的残余实例被 (RP) 正确解决**，框架自洽。

## 12.6 数值汇总（本轮新增，全部 assert 式）

```
穷举 连通 C4-free n ≤ 13：13 544 784 次求值（任一断言失败即 exit(2)，未触发）
  Lemma G1  断言失败 0
  Lemma G10 断言失败 0
  Lemma G9（d ≥ 4）断言失败 0        （d = 3 变体失败 334 次 ⟹ d≥4 必要）
  Theorem G+ 断言失败 0
  COVERAGE 由 99.9955%（残余 606）→ 100.0000%（残余 0）
  l ≥ 3 的图共 622 个，其中 μ ≥ 2 的 622 个（Theorem G+ 基例全覆盖）
  归纳残余（Λ≠∅ 且 radius-critical 且 l≥3）在 n ≤ 13 内为 0 个
```
n ≤ 13 内残余为空 ⟹ 小图对 (RP) 无信息；证人 B（n=53）是目前唯一已知残余实例。

## 12.7 本题状态（owner-w133）

* **已关闭**：hasC4 支（Thm A）；⌊l⌋ ≤ 2（Cor D1）；r=2 层（G7+G8）；
  **⌊l⌋ ≤ 3 且无 a=1 顶点（Cor G+1，本轮新增）**；⌊l⌋ ≤ 3 且非 radius-critical（剥皮归纳）。
* **口袋 1 残余**：仅剩 (RP)（radius-critical + rad ≥ 3；rad=3 另需 (R4) 的 d=3 补丁）。
* **口袋 2（⌊l⌋ ≥ 4）**：未动。端点法已由 T_m 证伪，须全局平均；注意证人 B 的 ⌊l⌋=6，
  说明口袋 2 里同样存在"稠密核 + 少量叶"的坏结构，**Theorem G+ 在口袋 2 只给 rad+3，不够**。
* **红线状态**：无 SAT/穷举大空间；所有新断言先跑后写；端点法未重走。

## 12.8 下轮攻 (RP) 的两条线索（本轮已探明的地形，未证）

**线索 1 —— 缺口恒为"1 个顶点"，且来源已定位。** 一切自然构造都停在 rad+2：
G1 用测地线 h→p（a(h)≥3、a(p)≥2、y 取 p 的叶 ℓ_p 合法，因叶在 G[N(p)] 中是孤立分量）
给 dist(h,p)+3 顶点；但 (R3) 恰好禁止 dist(h,p) ≥ rad，故只得 rad+2。
即使 h 也带叶（x 换成 ℓ_h）计数不变。**故第 rad+3 个顶点只能来自"比测地线长 1 的
诱导绕行"**：需要 P 中距离 D 的一对之间存在 **D+2 顶点**的诱导路径（长度 D+1）。

**线索 1 的硬障碍（新发现）**：若 C **二部**，同一对顶点间所有路径长度同奇偶，
长度 D+1 的路径**不存在**。故二部核（如 PG(2,q) 关联图，girth 6、自中心、l=q+1>3）
只能走 (RP) 的另一支：**D+3 顶点、一端落在 P** 的诱导路径。二部情形必须单独论证。

**线索 2 —— 把归纳假设加强为带端点的版本 (X++)：**
> 连通 C4-free、l ≥ 3 ⟹ **对每个顶点 u**，存在以 u 为端点的 rad+3 顶点诱导路径。
(X++) 直接闭合剥皮归纳：对核 C 取以父点 p 为端点的 rad(C)+3 = D+3 顶点路径，
接上 p 的叶得 D+4 = rad(G)+3 ✓。
本轮已探明 (X++) 的形状：**对非中心 u 自动成立**（ecc(u) ≥ rad+1 ⟹ u 的测地线给
rad+2 顶点，再用 Lemma G10 在远端 +1）；**只对中心 u 未知**。而 §12.5(d) 恰好证明了
残余中 C 自中心（每个顶点都是中心），所以 (X++) 的难点与 (RP) 的难点是同一个。
⟹ 需要一条"远端连扩两步"的引理（G10 的二阶版本），或换用非测地线的诱导绕行。

---
# §13 owner-w133 第二轮（2026-08-18，opus）：攻 (RP)，r=3 层基本拿下

planner 回合1 裁决：G+/G9/G10/G11 记 provisional PROVED，批准主攻 (RP)。
本节数值同样由 `problems/wowii/wowii133_gplus.c` 断言式产生（穷举 C4-free n ≤ 13）。

## 13.1 **Theorem G12（本轮主结果）**

> *C 连通 C4-free、**diam(C) = 2**、**l(C) > 3**（严格）⟹ path(C) ≥ 6。*

注意 diam=2 时 l>3>2 与 Theorem C 给 rad(C)=2，故结论即 **path ≥ rad+4**——
这是 §6 猜想 **A7（`l ≤ path − rad`，实值强化）的第一个被证明的非平凡实例**。
Petersen（diam 2、l=3、path=5）说明"严格 l>3"不可去。

**Step 0.** diam=2 + C4-free ⟹ **任两不邻顶点恰有一个公共邻点**（≥1 由 diam，≤1 由 C4-free）。

**Step 1（无三角形）.** ⚠ **本步在 round 6 被 Qwen S3 审查判为 GAP 并已修补，见 §17.1；
下面是修补后的版本（Lemma G12.1 是新增的、必须显式引用的一步）。**

> **Lemma G12.1（round 6 新增，堵 G12-J1）.** C 连通、C4-free、无三角形、diam(C)=2、
> **l(C) > 3** ⟹ C 含圈，且围长恰为 5。
> *证.* (i) 若 C 无圈：连通无圈 = 树，直径 2 的树 = 星 K_{1,m}，而
> l(K_{1,m}) = 2m/(m+1) < 2 < 3，与 l>3 矛盾。故 C 含圈。
> (ii) 含圈图满足 **girth ≤ 2·diam+1 = 5**（标准事实）；无三角形 + C4-free ⟹ girth ≥ 5。
> 故 girth = 5。∎
> *（若无 (i)，原文"围长 5"对星是假的：星满足无三角形 + C4-free + diam 2 却根本没有圈、
> 也不正则——这正是 Qwen 找到的反例。）*

由 **Lemma G12.1** 得 C 围长 5 且直径 2，由 Hoffman–Singleton 定理 C 是 Moore 图，
k-正则，k ∈ {2,3,7,57}。无三角形 ⟹ l(C) = 平均度 = k，故 l>3 ⟹ k ∈ {7,57}
⟹ δ = k ≥ 7，由 Theorem E1（围长≥5、δ≥2）得 path ≥ δ+2 ≥ 9 ≥ 6。∎
*[外部引用：Hoffman–Singleton 1960 / Singleton 1968，"直径 2 且围长 5 ⟹ Moore 图（必正则，度 ∈{2,3,7,57}）"。S1 查重时须核对。]*

**Step 2（有三角形）.** 反设 path(C) ≤ 5，取三角形 T={a,b,c}，记
A := N(a)∖{b,c}，B := N(b)∖{a,c}，C_s := N(c)∖{a,b}，R := V ∖ (T ∪ A ∪ B ∪ C_s)。

(i) **A,B,C_s 两两不交且两两无边.** 若 x ∈ A∩B 则 a,b 有两个公共邻点 c,x ⟹ C4。
    若 α∈A、β∈B、α~β，则 a,β 的公共邻点有 b 与 α ⟹ C4。∎
(ii) **每个 u ∈ R 在 A、B、C_s 中各恰有一个邻点.** u ≁ a 且 diam=2 ⟹ u,a 恰一个公共邻点
     w ∈ N(a) = {b,c}∪A；u ≁ b,c ⟹ w ∈ A。∎
(iii) **a(a) = 1 + comp(A)**，且对 α ∈ A：**a(α) = 1 + comp(R_α)**（comp = 诱导匹配的分量数，
     R_α := N(α)∩R）。[N(a)={b,c}∪A，其内部边 = {bc} ∪ e(A)（由 (i) 无 b–A 边）；
     N(α)={a} ∪ M(α) ∪ R_α，其内部边 = a–M(α) 与 e(R_α)（由 (ii) M(α) 与 R_α 无边）。]∎
(iv) **R 是团.** 设 ρ,σ ∈ R 不邻。若 f_A(ρ) ≠ f_A(σ) 且 f_B(ρ) ≠ f_B(σ)，
     取 α := f_A(ρ)、β := f_B(σ)，则 **ρ, α, a, b, β, σ 是诱导 P₆**
     [逐条：ρ≁a,b（R 的定义）；ρ≁β（ρ 的唯一 B-邻点 ≠ β）；α≁b、α≁β、α≁σ（由 (i),(ii)）；
     a≁β、a≁σ、b≁σ]，与 path ≤ 5 矛盾。用边 ac、bc 同理得：三个坐标中**至少两个相等**。
     但两个坐标相等 ⟹ ρ,σ 有两个公共邻点 ⟹ C4。故 ρ~σ。∎
(v) **|R| ≤ 3**（团 + C4-free，K₄ ⊇ C₄）。
(vi) **计数.** 记 s := |A|+|B|+|C_s|、ρ := |R|。由 (iii)
     Σa = 3 + Σ_T comp + s + Σ_α comp(R_α) + Σ_{u∈R} a(u)，
     其中 Σ_T comp ≤ s、Σ_α comp(R_α) ≤ 3ρ（每个 R 顶点在 A 侧只落一个纤维，B、C_s 同）。
     - ρ=0：a(α)=1 ∀α，Σa ≤ 3+2s，3n = 9+3s ⟹ Σa > 3n 不可能。
     - ρ=1：d(u)=3 ⟹ a(u) ≤ 3，Σa ≤ 9+2s，3n = 12+3s ⟹ 不可能。
     - ρ=2：d(u)=4 ⟹ a(u) ≤ 4，Σa ≤ 17+2s，3n = 15+3s ⟹ s < 2；但 (ii) 给 s ≥ 3。矛盾。
     - ρ=3：R 是三角形，N(u) = {α_u,β_u,γ_u} ∪ (R∖{u})，而 R∖{u} 已是一条边，
       由匹配性 α_u,β_u,γ_u 均**不邻** R∖{u}，故 **a(u) = 4 恰好**，且 **f_A 在 R 上单射**
       （α_u ≁ u' ⟹ f_A(u') ≠ α_u）⟹ |A|,|B|,|C_s| ≥ 3 ⟹ **s ≥ 9**。
       而 Σa ≤ 3+2s+9+12 = 24+2s、3n = 18+3s ⟹ **s < 6**。矛盾。∎
故 path(C) ≥ 6。∎

**数值背书**：穷举 C4-free n ≤ 13，(i)(ii)(iii)(iv) 与 G12 本身逐条断言，
在 **422** 个（diam-2 图，三角形）实例上零失败（`G12-CHECKS` 行）。

## 13.2 **r = 3 层：只剩一个明确子情形**

回到 §12.5 的残余（极小反例 G，Λ≠∅，核 C = G−Λ 等距、l(C) > 3）。设 **r = rad(G) = 3**。
* 若核内某对距离 ≥ 4：两端 a ≥ 2，**Lemma G9** 给 path ≥ 4+3 = 7 > 6 ✓ 结束。故 diam(C) ≤ 3。
* 若 diam(C) = 2：**Theorem G12** 给 path(G) ≥ path(C) ≥ 6 = r+3 ✓ **结束**。
* 故只剩 **diam(C) = 3**，且由 (R3) 该距离-3 对的 a 值只能是 (2,2)。

**Lemma G13（距离-3 的 (2,2) 对）.** *C4-free，dist(u,z)=3，a(u)=a(z)=2。则或 path ≥ 6，
或：N(u) 恰由 u₁ 所在分量与一个**单点**分量 {x} 组成（故 d(u) ≤ 3），N(z) 同理给出 {y}，
且 x ~ y——即 G 含一个过 u,z 的**诱导 C₆**。*
*证.* 取 x ∈ N(u) 不在 u₁ 的分量、y ∈ N(z) 不在 u₂ 的分量。由 G10 的逐条检查，
x,y ∉ P 且 x,y 与所有 u_i 不邻接（x≁u₂ 否则 C4；y≁u₁ 否则 C4；其余由距离）。
若某次选取 x ≁ y，则 x,u,u₁,u₂,z,y 是诱导 P₆ ⟹ path ≥ 6。否则一切合法 x 与一切合法 y 相邻：
若 x 的分量含两点 x,x̄，则 x,x̄ 同时邻 u 与 y ⟹ C4（x–u–x̄–y–x）矛盾，故为单点分量；y 同理。∎

> **r=3 的唯一残余**：核 C 的直径恰为 3，且每一对距离-3 的核顶点都是 (2,2) 型、度 ≤ 3，
> 并各自撑起一个诱导 C₆。**这是一个极刚性的局部构型，下一轮的首要目标。**

## 13.3 r ≥ 4 层：(RP) 仍开放，但已知 G12 是"D=2 版的 (RP)"

r ≥ 4 时 §12.5(d) 给 diam(C) = r−1 = D ≥ 3，G12 不适用。
**注意 G12 的真正含义**：它正是 **D=2 情形的 (RP)**——因为 path(C) ≥ D+4 直接盖过
"D+3 顶点且一端在 P"那条更弱的要求。故 (RP) 的自然强化形式是：

> **(RP-D)** C4-free、diam(C) = D、l(C) > 3 ⟹ path(C) ≥ D+4。
> D=2 已由 **Theorem G12** 证明。一般 D 即 §6 的 **A7** 在自中心情形的整数版。

这把 (RP) 与 draft §9 早就点名的"正确目标 A7"接上了：**A7 ⟹ (RP-D) ⟹ 口袋 1 全关**。

## 13.4 口袋 2 路线草图（planner 要求，先占位防战线真空）

* **T_m 只杀端点法，杀不掉"μ 下界法"**：T_m 的叶有 a=1，故 **μ(T_m) = 1**。
  于是 Theorem G+ 的自然推广并未被证伪：
  > **猜想 (G+k)**：C4-free、μ ≥ k−1 且 max a ≥ k ⟹ path ≥ rad + k。
  > k=3 即 **Theorem G+（已证）**。k ≥ 4 待定。(G+k) 成立即给口袋 2 一个基例。
* **Lemma G14（深端扩张，本轮新证，口袋 2 的种子）.**
  *C4-free，测地线 u₀…u_d，d ≥ 5，a(u₀) ≥ 3，a(u_d) ≥ 2，且所选 x ∈ N(u₀) 有 a(x) ≥ 4
  ⟹ path ≥ d+4。* 特别地 **μ ≥ 4 且 rad ≥ 5 ⟹ path ≥ rad+4**。
  *证.* 按 G1 取 x ∈ N(u₀) 不在 u₁ 的分量、y ∈ N(u_d) 不在 u_{d−1} 的分量。再在 N(x) 中取 w：
  G[N(x)] 的分量数 ≥ a(x) ≥ 4，其中 u₀ 所在分量 1 个；|N(x)∩N(u₂)| ≤ 1、|N(x)∩N(u₃)| ≤ 1
  各毁 ≤1 个分量（x ≁ u₂,u₃ 故公共邻点 ≤1），尚余 ≥1 个分量，取 w 于其中。
  则 w ≁ u₀；w ≁ u₁ 自动（否则 w,x,u₀,u₁ 成 C4）；w ≁ u₂,u₃ 由选取；i ≥ 4 时
  dist(w,u_i) ≥ i−2 ≥ 2。又 w ∉ P（dist(u₀,w)=2 且 w ≠ u₂，因 x ≁ u₂）。
  最后 dist(w,y) ≥ d−3 ≥ 2 故 w ≁ y、w ≠ y；dist(x,y) ≥ d−2 ≥ 3。
  于是 w,x,u₀,…,u_d,y 诱导，d+4 顶点。∎
  **状态：证明完整，但在 n ≤ 13 穷举内空载（μ≥4 且 diam≥5 需要更大的图），
  下一轮须在结构族（Robertson 图、PG(2,q) 关联图、笼图）上补数值背书后方可升格。**
* **路线**：μ ≥ 2j ⟹ 每端可连扩 j 步 ⟹ path ≥ rad + O(j)。与 §12.5 剥皮归纳（把 μ 顶上去）
  串联，可能给出 path ≥ rad + f(μ)，再与全局平均（把 l 换成 μ）配合攻 A7。

## 13.5 本轮数值汇总

```
穷举 连通 C4-free n ≤ 13：13 544 784 次求值（任一断言失败即 exit(2)，未触发）
  Lemma G1 / G9(d≥4) / G10 / Theorem G+      断言失败 0（回合1，本轮复跑仍 0）
  Theorem G12 及其结构步 (i)(ii)(iii)(iv)     断言失败 0，非空载实例 422
  猜想 (G+k) 探针 k=4（计数不断言）           适用 15 例，违例 0        <- 弱正面证据
  COVERAGE 残余 0（100.0000%），l≥3 图 622 个全部 μ≥2
```
**空载声明（诚实标注）**：G12 本身在 n ≤ 13 内空载（该范围内无 diam=2 且 l>3 的 C4-free 图，
最接近的 Petersen 恰好 l=3），其背书来自 (i)–(iv) 四个结构步的 422 个非空载实例；
Lemma G14 在该范围内完全空载，**未升格**。

## 13.6 状态更新（覆盖 §12.7）

* **新增关闭**：diam=2 且 l>3（Theorem G12）；由此 **r=3 层除"核直径恰为 3"外全部关闭**。
* **r=3 唯一残余**：diam(C)=3 且每对距离-3 核顶点为 (2,2) 型、度 ≤3、撑起诱导 C₆（Lemma G13）。
* **r≥4 残余**：(RP)，其自然强化 (RP-D) = A7 的整数版；G12 = (RP-D) 的 D=2 情形。
* **口袋 2**：路线草图已占位（猜想 (G+k) + Lemma G14），未闭合。
* **红线**：无 SAT/无大空间穷举；先跑后写；端点法未重走；空载项已显式标注不升格。

---
# §14 owner-w133 第三轮（2026-08-18，opus）：G12 非空载已证 + C₆ 刚性 + r=3 再收窄

planner 回合2 裁决：G12/G13 采纳（provisional），Moore 引用已由 planner 独立确认；
要求 ①：给 diam=2 ∧ l>3 的 C4-free 类补非空性证据。本节先办 ①。

## 14.1 **要求 ① 结清：G12 的假设类非空，G12 不是空载真命题**

> **证人：Hoffman–Singleton 图本身。**（`problems/wowii/w133_g12_nonempty.py`，全部现算）
> n=50，C4-free（girth 5），**diam = 2**，7-正则且无三角形 ⟹ a(v)=d(v)=7 ⟹ **l = 7 > 3** ✓。
> 落在 G12 假设类内；G12 断言 path ≥ 6，实测诱导路径证书 **20** ≥ 6 ✓。

故 **G12 非空载**。进一步，由 G12 的 Step 1，该类中**无三角形**的成员恰是
**度 ≥ 7 的直径-2 Moore 图** = {Hoffman–Singleton，假设存在的 57-正则 Moore 图}——
即无三角形支被完全分类。含三角形的成员本证明**未排除**（Step 2 只证它们 path ≥ 6），
是否存在仍开放（记为小问题 Q14.1）。

**诚实标注**：该类在 n ≤ 13 内**确实为空**（最接近者 Petersen 恰好 l=3，被"严格 l>3"排除），
所以 G12 的穷举背书全部来自其四个结构步 (i)–(iv)（422 个非空载实例），
命题本身的正面证据来自 HS 这一显式证人。二者结合已足；**价值不降级**。

## 14.2 **Lemma G15（诱导 C₆ 刚性，本轮新增）**

> *G 为 C4-free 且含诱导 6-圈 Z = v₁…v₆。则**或** path(G) ≥ 6，**或**：
> (a) Z 外每个顶点在 Z 上恰有 0 个或 2 个邻点；
> (b) 若有 2 个，二者在圈上的距离是 1 或 3（**绝不是 2**）；
> (c) 从而每个 v_i 的度 ≤ 5，且**没有 v_i 带叶邻点**。*

*证.* (a) **两半，分别处理**。
**(a1)「恰 1 个」被排除**：去掉 Z 的任一顶点得诱导 P₅；若 w ∉ Z 在 Z 上恰有一个邻点 v_i，
取去掉 v_{i+1} 所得的 P₅（端点为 v_i），则 w 接在 v_i 端得诱导 P₆ ⟹ path ≥ 6。
**(a2)「≥ 3 个」被排除**（**round 9 补全，见下方补丁注**）：六圈上任意 3 个顶点必含一对
圈距为 2 的顶点。[证：三点把 C₆ 分成三段弧，弧长 a+b+c = 6 且 a,b,c ≥ 1；一对被某段弧
相隔的顶点其圈距为 min(弧长, 6−弧长)，等于 2 当且仅当弧长 ∈ {2,4}。若三对圈距都 ≠ 2 则
a,b,c ∈ {1,3,5} 且 a+b+c = 6——穷举 {1,1,4}✗、{1,3,2}✗、{3,3,0}✗、{1,5,0}✗ 均不合法，
故无解，矛盾。]设该对为 v_j, v_{j+2}，则 w 与 v_{j+1} 有两个公共邻点 v_j, v_{j+2} ⟹ C4，
与 C4-free 矛盾。故 |N(w) ∩ Z| ≤ 2。(a1)+(a2) 合起来给出 (a)。
(b) 若 w ~ v_i 且 w ~ v_{i+2}，则 w 与 v_{i+1} 有两个公共邻点 v_i, v_{i+2} ⟹ C4。
(c) v_i 的圈外邻点 w 必与 v_{i−1}、v_{i+1} 或 v_{i+3} 之一同时相邻；每种情形由 C4-free
（两顶点公共邻点 ≤1）至多 1 个，故圈外邻点 ≤ 3，d(v_i) ≤ 2+3 = 5。
叶度数为 1，只能有 0 或 1 个 Z-邻点，而 1 被 (a) 排除，故叶不与 Z 相邻。∎

**数值背书**：穷举 C4-free n ≤ 13，在 path ≤ 5 的图中共 **1272** 个诱导-C₆ 实例，
(a)(b) 逐条断言，零失败（`G15-CHECKS` 行）。

> **补丁注（round 9, owner-w133, 2026-08-18；结清 §20.8 finding 1 的 upstream flag）
> [PATCH NOTE — closes the §20.8 upstream flag on G15(a)]**
>
> **缺陷**：本引理原写的 (a) 的证明**只杀了「恰 1 个」，从未处理「≥ 3 个」**——由 §20 的
> 盲审裁判 B 发现（G32 因照抄"0-or-2 部分即 G15(a)"而漏掉 C4-free 假设，见 §20.1/§20.8）。
> **结论 (a) 本身为真**，缺的是一行论证，故本轮的处理是**补全，不是改述**：上方 (a2)。
>
> **两半的假设不同，这条必须记住**：(a1)「恰 1 个」用的是**无诱导 P₆**（它产出的是
> "path ≥ 6" 那个析取支）；(a2)「≥ 3 个」用的是**纯 C4-free**（与 path 无关，不产出析取支）。
> G15 的前置已含 C4-free，故 (a2) 免费。**这正是 G32 出事的地方**：G32 早期版本把整条 (a)
> 当成"无 P₆ 就够"，于是陈述宽于证明而**假**（反例 C₆ + w, N(w) = {v₀,v₂}，见 §20.8）。
>
> **使用点全扫（restatement 未发生，故只需核每处是否携带 C4-free）**：§14.3（核 C 是
> C4-free 图的导出子图 ⟹ C4-free ✓）、§15.4（RES，定义含 C4-free ✓）、§16.5b G21 的证明
> 三处（RES(b) ✓，且其中"至多一个 h"的步骤本身就在用 C4-free ✓）、§17.4 G22.1（RES(b) ∧
> (C6) ✓）、§19.1/§19.2/§19.4（RES(b) ✓，且已被 §20.2 判为空载）、§20.1 G32 的 (i)(iii)
> （C4-free 已在陈述里 ✓）。**共 11 处，全部携带 C4-free，无一处需要修补。**
> 下游损害：**零**。
> **[round 9 补记：Q19 defect 4，已核实并采纳]** 上表漏了**一处间接使用**：**§19.5 G31 的证明
> 经 **G15(c)** 用到 (a)（"叶不与 Z 相邻"那半句由 (a) 排除 |N∩Z|=1）。该处在 RES(b) 内
> ⟹ 携带 C4-free ✓，且 §19 已被 §20.2 判为空载/被取代 ⟹ **MOOT**。故**扫描表应为 12 处**，
> 损害仍为零。教训：使用点扫描必须扫**间接**引用（经 (b)(c) 转手的），不只扫直接引用。
>
> **方法论条目（notes/methodology.md「陈述-证明作用域双向相等」）**：本例是"陈述宽于证明"
> 物种的**上游母本**——G15(a) 的陈述真、证明缺半，下游 G32 复制这半个证明时把陈述也复制
> 成了假的。**补全上游的缺行，是防止下游把缺口放大成假命题的最便宜手段。**

## 14.3 **r = 3 残余再收窄：核必须 rad=2 且 diam=3**

承 §13.2。极小反例 G，r=3，核 C = G−Λ 等距、连通、l(C) > 3，diam(C) = 3。
对 C 用归纳（n_C < n）：path(C) ≥ rad(C)+3。
* **若 rad(C) = 3**：path(C) ≥ 6 = r+3 ⟹ path(G) ≥ 6 ✓ **结束**。
* 故 **rad(C) = 2 且 diam(C) = 3**。

于是 r=3 的残余是：**C4-free 的核 C，rad(C)=2、diam(C)=3、l(C)>3**，
其距离-3 顶点对全为 (2,2) 型（由 (R3)）、度 ≤3（由 G13），并撑起诱导 C₆（G13），
而该 C₆ 又受 **Lemma G15** 的 (a)(b)(c) 全部约束。

**一个已排除的自然候选（本轮实算）**：C₆ 上按对径挂三个顶点 w₁,w₂,w₃
（w_i ~ v_i, v_{i+3}）再加一个中心 h ~ w₁,w₂,w₃，恰好是 **3-正则、girth 5、n=10**，
即 **Petersen 图**（(3,5)-cage 唯一性）。它 diam=2、l=3、path=5——
**同时被 diam(C)=3 与 l(C)>3 两条排除**。故最对称的 C₆-刚性构型不在残余中。
[实算：degrees=[3], girth=5, C4-free, rad=diam=2, l=3.0, path=5。]

## 14.4 **Lemma G14 升格：已获非空载数值背书**（覆盖 §13.4 的"空载未升格"）

**先记一条负结果（省掉后人白跑）**：**任何度 ≥ 4 的循环图都含 C4**，
因为 0 = a+(−a) = b+(−b) 给出两种表示 ⟹ 4-圈。故循环图族**完全不能**用作 G14 的检验样本。

改用贪心生成的**随机 4-正则 girth-5 图**（只在距离 ≥ 4 的点对间连边，故 girth ≥ 5）：

| n | girth | C4-free | rad | μ | l | path 证书 | G14 适用 | 需 rad+4 | 结论 |
|---|---|---|---|---|---|---|---|---|---|
| 90 | 5 | ✓ | 5 | 4 | 4.00 | ≥46 | ✓ | 9 | OK |
| 120 | 5 | ✓ | 5 | 4 | 4.00 | ≥57 | ✓ | 9 | OK |
| 150 | 5 | ✓ | 5 | 4 | 4.00 | ≥71 | ✓ | 9 | OK |
| 180 | 5 | ✓ | 6 | 4 | 4.00 | ≥81 | ✓ | 10 | OK |

**G14 由此升格为 provisional PROVED（证明完整 + 非空载数值零违例）**。
注意松弛极大（46 vs 9），故这些样本对**紧性**无信息，只证明不空载且无反例。
(G+k) 探针：结构族（HS：k=3..7 全部满足）+ 穷举 n≤13（k=4 适用 15 例、违例 0）。

## 14.5 本轮数值汇总

```
穷举 连通 C4-free n ≤ 13（13 544 784 次求值，断言失败即 exit(2)，未触发）
  G1 / G9(d≥4) / G10 / G+ / G12 及其结构步            失败 0（复跑）
  Lemma G15 (a)(b)                                    失败 0，非空载实例 1272
  (G+k) 探针 k=4                                       适用 15，违例 0
  COVERAGE 残余 0（100.0000%）
显式证人（现算）
  Hoffman–Singleton ∈ G12 假设类，path 证书 20 ≥ 6      => 要求 ① 结清
  随机 4-正则 girth-5 图 n=90/120/150/180              => G14 非空载，零违例
  C₆+对径三挂点+中心 = Petersen（diam 2、l=3）          => 该候选已排除
```

## 14.6 状态更新（覆盖 §13.6）

* **要求 ① 已结清**：G12 假设类非空（HS），不空载，价值不降级。
* **r=3 残余**（口袋 1 的最后一块）：核 C 满足 **C4-free、rad(C)=2、diam(C)=3、l(C)>3**，
  距离-3 对全为 (2,2) 型且度 ≤3，撑起受 G15 约束的诱导 C₆。**下一轮首要目标。**
  可用武器：G7 的纤维分解（rad(C)=2 正是它的场景）+ G15 刚性 + G13 度界。
* **r≥4 残余**：(RP-D) = A7 整数版，G12 = D=2 情形。
* **口袋 2**：G14 已升格；(G+k) 仍为猜想。
* **小问题 Q14.1**：diam=2、l>3、含三角形的 C4-free 图是否存在？（G12 未排除）
* **红线**：无 SAT/无大空间穷举；先跑后写；空载项已逐条如实标注并在获得证据后才升格。

---
# §15 owner-w133 第四轮（2026-08-18，opus）：目标修正 + Q14.1 结清

planner 回合4 指令：主攻「核 C：C4-free、rad=2、diam=3、l>3」，用 G7 纤维计数求矛盾。
**本轮首先发现该目标陈述漏了一条关键假设，按原样求矛盾是不可能的。** 详见 15.2。

## 15.1 **Q14.1 结清：答案是 YES**

问：存在 C4-free、diam=2、l>3 且**含三角形**的图吗？（G12 的 Step 2 未排除）
**答：存在。证人 = Erdős–Rényi 正交极图 ER_q**（`w133_res3_search.py`，全部现算）：

| 图 | n | C4-free | 含三角形 | rad | diam | l | path 证书 | 需 ≥6 |
|---|---|---|---|---|---|---|---|---|
| ER_5 | 31 | ✓ | ✓ | 2 | 2 | 3.871 | 15 | OK |
| ER_7 | 57 | ✓ | ✓ | 2 | 2 | 4.912 | 22 | OK |
| ER_11 | 133 | ✓ | ✓ | 2 | 2 | 6.947 | 37 | OK |
（ER_3：l=2.769 ≤ 3，不入类。）

故 **G12 假设类的两支都非空**：无三角形支 = 度≥7 的直径-2 Moore 图（HS）；
含三角形支 = ER_q（q ≥ 5）。**G12 的价值进一步坐实**，且 Step 2 的计数论证在
ER_q 上是"真刀实枪"地被用到，不是空转。

## 15.2 **目标修正（本轮关键）：planner 陈述的类是"活的"，按原样求矛盾不可能**

> **结论：类 {C4-free ∧ rad=2 ∧ diam=3 ∧ l>3} 富含成员，共找到 9 个证人。**

| 证人 | n | C4-free | rad | diam | l |
|---|---|---|---|---|---|
| HS − 1 顶点 | 49 | ✓ | 2 | 3 | 6.857 |
| HS − 2 顶点（邻/非邻） | 48 | ✓ | 2 | 3 | 6.750 / 6.708 |
| HS − 3/5/8/12 顶点 | 47/45/42/38 | ✓ | 2 | 3 | 6.638…5.368 |
| ER_5 − 1 顶点 | 30 | ✓ | 2 | 3 | 3.900 |
| ER_7 − 1 顶点 | 56 | ✓ | 2 | 3 | 4.875 |

（全部 path 证书 ≥ 15 ≥ 6，猜想无恙。）故**不可能**对该类推出矛盾。

**漏掉的假设是 (R3)。** 残余来自极小反例，那里还有
> **(R3)**：无距离 ≥3 且 a 值 (≥3,≥2) 的顶点对 ⟺ **每个 a≥3 的顶点 ecc ≤ 2**。

上表 9 个证人**全部违反 (R3)**（实算：HS−1 顶点有距离-3 的 (6,6) 对；ER_7−1 顶点有 (4,4) 对）。
**结构性原因（这就是修正的实质）**：稠密核一旦 diam=3，实现直径的那对顶点自己就是高顶点，
立刻违反 (R3)。所以"稠密核 + diam 3"这条造反例的自然思路是**自毁的**。

## 15.3 **真残余 RES 及其（目前）空性**

> **RES** := C4-free ∧ 连通 ∧ **rad=2** ∧ **diam=3** ∧ **l>3** ∧ **(R3)**。

上述 9 个证人在 RES 中的成员数 = **0**。RES 的张力可以一句话说清：
* l>3 需要大量高顶点（见下 (**)），
* (R3) 逼所有高顶点 ecc=2、且实现 diam=3 的那对顶点必须 **a ≤ 2**，
* 于是必须把"低 a 顶点"放到距离 3，同时让**每个**高顶点都在它们 2 步之内——
  而低 a 顶点度数很小（a≤2 ⟹ 度 ≤4；再由 **G13** 度 ≤3），
  半径-2 球装不下 l>3 所需的全部高质量。**这正是下一轮要形式化的矛盾。**

## 15.4 攻 RES=∅ 的已备弹药（本轮推出，全部已核）

设 c 为高顶点（由 (**) 存在），(R3) ⟹ ecc(c)=2。A := N(c)，k := |A|，B := 距离-2 层。
每个 b ∈ B 在 A 中恰有一个"父" p(b)（≥1 由 diam-from-c，≤1 由 C4-free），纤维 B_α。

* **恒等式**（与 G12(iii)、G7 同型）：a(c) = comp(A)；对 α ∈ A，**a(α) = 1 + comp(B_α)**。
* **(\*) 纤维计数**：l(C) > 3 ⟹ **Σ_{b∈B} a(b) > 3 + k + 2|B|**。
  [由 Σa = comp(A) + Σ_α(1+comp(B_α)) + Σ_B a，comp(A) ≤ k，Σ_α comp(B_α) ≤ |B|，n = 1+k+|B|。]
* **(\*\*) 高质量下界**：l(C) > 3 且非高顶点 a ≤ 2 ⟹ **Σ_{h∈H}(a(h) − 2) > n**。
  特别地 H ≠ ∅。[Σa ≤ Σ_H a + 2(n−|H|) > 3n。]
* **Fact 2（B 中高顶点度数极大）**：h ∈ H∩B ⟹ 对每个 α ∈ A∖{p(h), M(p(h))}，
  h 必在 B_α 中有邻点（因 c ≁ h，公共邻点只能来自 N(h)）⟹ **deg_B(h) ≥ k − 2**。
* **Fact 3（A 中高顶点的纤维支配全局）**：α ∈ H∩A ⟹ 每个 p(b) ∉ {α,M(α)} 的 b
  都在 B_α 中有邻点；且由 C4-free **每个 b 在 B_α 中至多一个邻点**，故 B_α 的邻域近乎划分 B。
* **G13 加成**：实现 diam=3 的那对顶点 u,z 满足 a=2、**d ≤ 3**，并撑起受 **G15** 约束的诱导 C₆。
* 由 (R3)：**H ⊆ ball₂(u) ∩ ball₂(z)**，而 d(u), d(z) ≤ 3 ⟹ H 被关在一个很小的球里，
  与 (\*\*) 的 Σ_H(a−2) > n 直接对撞。**这是下一轮的主攻路线。**

## 15.5 本轮数值汇总

```
现算证人（w133_res3_search.py）
  ER_5 / ER_7 / ER_11：C4-free、diam=2、l>3、含三角形     => Q14.1 = YES（3 个证人）
  「rad=2,diam=3,l>3」类：9 个证人（HS−k 顶点、ER_q−1 顶点）=> 该类活，禁止对其求矛盾
  同 9 个证人对 (R3) 的检验：全部 False                    => 均不在真残余 RES 中
  真残余 RES 的成员数：0
穷举 C4-free n ≤ 13：G1/G9/G10/G+/G12/G15 断言复跑，失败 0（见 w133_gplus_n13.out）
```
> **撤回并替换（round 9, owner-w133, 2026-08-18；结清 §20.8 finding 3）
> [WITHDRAWN & REPLACED — closes the §20.8 flag on §15.5]**
>
> **原文（已撤回，不得再被引用）**：「n ≤ 13 内不存在 l>3 的 C4-free 图，故 RES 在穷举范围内
> 空载——证据只能来自构造与论证。」
>
> **撤回理由**：该断言**其本轮日志并不支持**。`w133_gplus_n13.out` 实际打印的是
> `level n=13: classes=0`（说的是**残余类**为 0，不是图为 0）、
> `L3-CENSUS: l>=3 graphs=622` 与 `C4-free floor(l)=3: count=622` ——即 n ≤ 13 内
> ⌊l⌋=3 的 C4-free 图**有 622 个**，其中 l 严格 > 3 者未被单独统计也未被排除。
> 日志只支持「n ≤ 13 内 ⌊l⌋ ≤ 3」（无 ⌊l⌋ ≥ 4 的图），**不支持「无 l > 3 的图」**，
> 因而由它推出的 **n ≥ 14 下界是未经核验的**。盲审裁判 B 提出，owner 复核日志后确认。
>
> **替换为（已核验的下界）**：**n ≥ 6**。理由是纯结构的：RES / RES(b) 的成员由 **G13** 撑起
> 一个**诱导 C₆** Z，故 n ≥ |Z| = **6**。此下界不依赖任何穷举，且是 §20 Theorem G35 实际
> 使用的那一个（G35 的对撞只需 Σ_H(a−2) ≤ 6 < 7 ≤ n）。
>
> **承载性检查**：n ≥ 14 **未被任何下游论证承载**——§16–§20 全程只用 n ≥ 6。
> 故撤回它**不改变任何已证结论**；§20.4 曾借它说"margin 不薄"的那句话，已改挂 **G18.1**
> （|H| ≥ 6）。RES 在穷举范围内是否空载，**现状态：未知/开放**，不得当作已知事实引用。
>
> **下游引用全扫（凡引 n ≥ 14 者，逐条定性）**：
> | 位置 | 引用方式 | 撤回后的判定 |
> |---|---|---|
> | §17.8 Cor G23.2 | 「n ≤ 20」+ §15.5 ⟹ 窗口 14 ≤ n ≤ 20 | **下界作废，上界 n ≤ 20 不受影响**；且该三角支已被 §18.2 **Theorem G26 整支杀死**，整条推论 **MOOT** |
> | §18.1 (D6a 复述) | 同上，「collapses to 14 ≤ n ≤ 20」 | 同上：下界作废、上界存活、**D6a/D6b 已由 G26 关闭 ⟹ MOOT** |
> | §18.5 裁决第 3 条 | 「其"极大"证人只有 8 个顶点，低于已知的 n ≥ 14」 | **该句反驳理由作废**（8 ≥ 6）。但该收割件的**否决不依赖此句**——同条已给出决定性理由（+2 的质量贡献与分支结构不符、三个无界度槽位未处理）。**结论不变，理由删一条** |
> | §19.5 Cor G31.1 括号句 | 「Σ_H(a−2) ≤ 11 < 14 ≤ n」 | **括号句作废**（n ≥ 6 时 11 < n 不成立）。G31.1 的正文用的是 |H| ≥ 6 与 G18.1，**不经此括号**；且 §19 已由 §20.2 判为**空载** ⟹ **MOOT** |
> | §19 标题 / Cor G31.2「THE WINDOW」 | 窗口 14 ≤ n ≤ 20 | §20 已**以证明取代该窗口**（§20.6 已记载）；作为历史记录保留，**不得再作为已证事实引用** |
> | §19.5 **Cor G31.3** | 「n = 1+d(u)+d(y)+d(B)+d(Q)−2t(x) ≤ 12 **< 14**」⟹ B 必被占 | **[round 9 新增行，Q19 defect 5]** 该推论**整条依赖 n ≥ 14**，撤回后 12 < n 不再成立 ⟹ **结论作废**；但 §19 已由 §20.2 判为被取代，且 §20 全程不引 G31.3 ⟹ **MOOT** |
> | §20 全域 | — | **无引用**（§20.5 已自行撤回那一处 appeal，改挂 G18.1）✓ |
> *(round 9：原表自称"凡引 n ≥ 14 者逐条定性"，实际漏了 G31.3 ——**该自称是假的**，现补齐为
> 6 行。净效果结论不变：无存活结论依赖 n ≥ 14。)*
>
> **净效果**：n ≥ 14 的每一个下游引用要么落在已被 G26/§20 杀死的分支里（MOOT），
> 要么是非承载的修辞句。**没有任何存活结论依赖它。** ✓

**防火墙语句（T13 要求）**：15.2/15.3 只说明「不带 (R3) 的类是活的、故不可对其求矛盾」，
以及「已试的 9 个构造都不在 RES 中」。**这既不是 RES 非空的证据，也不是 RES 为空的证据**；
RES 的空性仍完全开放。同理 15.1 的 ER_q 只回答 Q14.1，对 G12 的紧性无信息。

## 15.6 状态更新（覆盖 §14.6）

* **Q14.1 结清（YES，ER_q）**；G12 两支假设类均非空。
* **口袋 1 唯一残余修正为 RES**（= 原类 **+ (R3)**）；原类已被证明是活的，
  **求矛盾必须针对 RES，不能针对原类**——这是本轮最重要的一条，防止下一轮白跑。
* RES 的主攻路线已定：**(\*\*) 的 Σ_H(a−2) > n 对撞 (R3) 的 H ⊆ ball₂(u)∩ball₂(z)（d(u),d(z) ≤ 3）**。
* r≥4 残余、口袋 2 状态不变。
* **红线**：无 SAT/无大空间穷举；先跑后写；本轮所有"证人"均为显式构造并现算核验。

---
# §16 owner-w133 round 5 (2026-08-18, opus): the (R3) nail, and RES corrected

*(Language: English, per user directive 08-18. All numbers in this section are produced by
`problems/wowii/w133_res_kill.py`, log `problems/wowii/w133_res_kill.out`, 0 assert failures.)*

## 16.1 **THE NAIL IS REAL: (R3a) and (R3b) are NOT equivalent, and RES(a) is inhabited**

planner's round-5 item 1 asked which direction of the two readings of (R3) in
`w133_res3_search.py::R3_holds` the formal proof uses. Answer, settled by explicit witnesses:

> **(R3a)** no pair at distance ≥ 3 whose a-values are (≥3, ≥2);
> **(R3b)** every vertex with a ≥ 3 has eccentricity ≤ 2.

(R3b) ⟹ (R3a) trivially. **The converse is FALSE**, and it fails exactly on the low-a side:
(R3a) is silent about a pair (h, w) with a(h) ≥ 3 and **a(w) = 1**.

| witness | n | C4-free | rad | diam | l | (R3a) | (R3b) | in RES(a) | in RES(b) |
|---|---|---|---|---|---|---|---|---|---|
| HS + pendant leaf | 51 | ✓ | 2 | 3 | 6.902 | **True** | **False** | **YES** | no |
| HS + triangle-leaf | 51 | ✓ | 2 | 3 | 6.882 | **True** | **False** | **YES** | no |
| ER_5 + pendant leaf | 32 | ✓ | 2 | 3 | 3.812 | **True** | **False** | **YES** | no |
| ER_7 / ER_11 + pendant leaf | 58 / 134 | ✓ | 2 | 3 | 4.862 / 6.910 | **True** | **False** | **YES** | no |

(In each: the unique vertex at distance 3 from the offending high vertex is the grafted
a = 1 vertex, so (R3a) never sees the pair. Conjecture unharmed: induced-path certificates
21 / 21 / 16 / 22 ≥ 6.)

> **Consequence — the round-4 target must be re-stated once more.** With (R3) read as (R3a),
> **RES(a) ≠ ∅** (5 explicit members), so *proving `RES = ∅` in that reading is impossible*.
> **The correct residual is RES(b)** := C4-free ∧ connected ∧ rad = 2 ∧ diam = 3 ∧ l > 3 ∧ (R3b).
> §15.3's "⟺" between the two readings is hereby **retracted**; §15.4–§15.6 are unaffected
> in substance because they only ever used (R3b).

## 16.2 **Lemma G16 (core lifting): why (R3b) is legitimately available**

The residual is not an arbitrary graph satisfying (R3a) — it is the **core** C = G − Λ of a
minimal counterexample, Λ := {v ∈ G : a_G(v) = 1}. That is exactly the missing ingredient.

> **Lemma G16.** Let G be a pocket-1 minimal counterexample with rad(G) = 3, path(G) ≤ 5,
> Λ := {v : a_G(v) = 1} ≠ ∅ and C := G − Λ (connected, isometric in G, l(C) > 3, rad(C) = 2,
> diam(C) = 3 by §14.3). Then **(R3b) holds in C**: every h ∈ C with a_C(h) ≥ 3 has ecc_C(h) ≤ 2.

*Proof.* (1) Lemma G1 + path(G) ≤ 5 = rad(G) + 2 give (R3a) in G **for a_G-values**: a pair at
distance ≥ 3 with a_G-values (≥3, ≥2) would give an induced path on ≥ 3+3 = 6 vertices.
(2) **Every vertex of C has a_G ≥ 2**, by the very definition of Λ. (3) Let h ∈ C with
a_C(h) ≥ 3; then a_G(h) ≥ a_C(h) ≥ 3 (deleting vertices cannot increase a). If ecc_C(h) = 3,
pick z ∈ C with d_C(h,z) = 3 = d_G(h,z) (isometry). By (2) a_G(z) ≥ 2, so (h,z) is a pair
forbidden by (1) — contradiction. ∎

**Named joint for S3 (must be listed):** *"(R3a) ⇒ (R3b) is false in general (§16.1 witnesses);
inside the core it holds only through step (2), i.e. through the fact that all a = 1 vertices
have been peeled off. Any future use of (R3b) must therefore keep the core hypothesis explicit."*
Note also the mixed-a subtlety: (R3b) is obtained for the **larger** set {v ∈ C : a_G(v) ≥ 3},
which contains the set {v : a_C(v) ≥ 3} used by the counting side — the implication direction
is the favourable one.

## 16.3 **Lemma G17 (ball confinement): the high set is bounded by an absolute constant**

Throughout §16.3–§16.5, C ∈ RES(b), H := {v ∈ C : a(v) ≥ 3} (a = a_C), and u,z realise
diam(C) = 3. By (R3b), a(u) ≤ 2 and a(z) ≤ 2; hence d(u), d(z) ≤ 4 (a ≤ 2 means ≤ 2 components
in the neighbourhood, each of size ≤ 2 because C4-freeness makes C[N(v)] a matching + isolated
vertices), and d(u), d(z) ≤ 3 whenever **G13** applies (a(u) = a(z) = 2, path ≤ 5).

> **Lemma G17.** d(u,z) = 3 in a C4-free graph ⟹
> **|ball₂(u) ∩ ball₂(z)| ≤ d(u)·d(z) + d(u) + d(z)**. Under (R3b) every h ∈ H has ecc(h) = 2,
> so **H ⊆ ball₂(u) ∩ ball₂(z)** and therefore **|H| ≤ 24, and |H| ≤ 15 under G13**.

*Proof.* N(u) ∩ N(z) = ∅ (else d(u,z) ≤ 2), and no vertex is adjacent to both. For
v ∈ ball₂(u) ∩ ball₂(z) with d(v,u) = d(v,z) = 2, C4-freeness gives a *unique* common
neighbour P_u(v) ∈ N(u) and a unique P_z(v) ∈ N(z). If v ≠ v' had the same pair (x,y), then
x ≠ y and x,y would have the two common neighbours v,v' — a C₄. So that part injects into
N(u) × N(z). The remaining vertices are adjacent to u or to z (never both), contributing
≤ d(u) + d(z). For the second claim: ecc(h) = 2 forces d(h,u), d(h,z) ≤ 2. ∎
*Numerics: 1363 distance-3 pairs over 48 C4-free graphs (Petersen, HS, HS±, ER_q, ER_q±,
40 random maximal C4-free graphs), 0 failures.*

## 16.4 **Lemma G18 (mass–Bonferroni) and the |H| ≥ 6 corollary**

> **Lemma G18.** In any C4-free graph and any S ⊆ V:
> **Σ_{h∈S} a(h) ≤ |N(S)| + P(S) ≤ n + C(|S|,2)**, where N(S) = ⋃_{h∈S} N(h) and P(S) is the
> number of pairs of S having a common neighbour.

*Proof.* a(h) = |I_h| for a maximum independent set I_h ⊆ N(h). With m(v) := #{h ∈ S : v ∈ I_h}
≤ deg_S(v): Σ_S a = Σ_v m(v) ≤ |N(S)| + Σ_v (m(v) − 1)⁺ ≤ |N(S)| + Σ_v C(deg_S(v),2), and
Σ_v C(deg_S(v),2) counts pairs of S with a common neighbour **with multiplicity = number of
common neighbours ≤ 1** (C4-freeness), i.e. equals P(S). ∎
*Numerics: 329 subsets over the same 48 graphs, 0 failures.*

> **Corollary G18.1.** In RES(b): (\*\*) gives Σ_H a > n + 2|H|, G18 gives Σ_H a ≤ n + C(|H|,2),
> hence **2|H| < |H|(|H|−1)/2, i.e. |H| ≥ 6**; sharper, **Σ_{h∈H} t(h) < |H|(|H|−5)/2**
> (t = number of triangles through the vertex).

> **Corollary G18.2 (the window).** **6 ≤ |H| ≤ 24 (≤ 15 under G13).** RES(b) is now a
> *finite-type* condition on the high set: at most 15–24 hubs must carry mass Σ_H(a−2) > n
> while all n − |H| other vertices have a ≤ 2, hence degree ≤ 4.

## 16.5 **Lemma G19 (no leaf endpoint) + Lemma G20 (centre identity) + the dichotomy**

> **Lemma G19.** In RES(b) no vertex of eccentricity 3 is a leaf.

*Proof.* Let u be a leaf with neighbour p and ecc(u) = 3. Then d(u,·) = 1 + d(p,·) ≤ 3 gives
ecc(p) ≤ 2, and ecc(p) = 2 exactly (ecc(p) = 1 would force diam ≤ 2). By (R3b) every h ∈ H has
d(h,u) ≤ 2, hence d(h,p) ≤ 1, i.e. **H ⊆ {p} ∪ N(p)**: no high vertex lies at distance exactly
2 from p. But (\*) applied at the centre p reads Σ_{b ∈ B(p)}(a(b) − 2) > 3 + d(p) + e_intra > 0,
and a(b) ≤ 2 off H — so B(p) must contain a high vertex. Contradiction. ∎
(The same computation is the general fact **G17b: every centre of a C4-free graph with l > 3
has a high vertex at distance exactly 2**; numerics: 301 centres, 0 failures.)

> **Lemma G20 (centre identity).** C4-free and ecc(h) = 2 ⟹ **n = 1 + Σ_{x ∈ N(h)} d(x) − 2t(h)**
> (and a(h) = d(h) − t(h)). *Proof:* every vertex at distance 2 from h has exactly one neighbour
> in N(h); the fibre of x ∈ N(h) has size d(x) − 1 − |M(x)|, Σ_x |M(x)| = 2t(h). ∎
> *Numerics: 371 instances (all vertices of eccentricity 2 in the 48-graph pool), 0 failures.*

**The dichotomy this produces (next round's target).** Every non-high vertex has degree ≤ 4, so
G20 gives n − 1 ≤ 4d(h) + Σ_{x ∈ N(h)∩H}(d(x) − 4) for each h ∈ H. Summing over H and using
Σ_H d(h) ≤ n + C(|H|,2) (G18, degree form):

> **|H|(n−1) ≤ (4 + δ_H)·(n + C(|H|,2))**, where δ_H := max_{h∈H} |N(h) ∩ H|.

Hence **either δ_H ≥ |H| − 4** (some hub is adjacent to all but ≤ 3 of the other hubs — a very
rigid, C4-free-hostile configuration, since hubs pairwise share ≤ 1 neighbour), **or n is bounded
by an absolute constant** ( ≤ (4+δ_H)C(|H|,2)+|H| over |H|−4−δ_H ). Closing either branch closes
pocket 1. This is the round-6 main line.

## 16.5b **Which target exactly, and Lemma G21 (only 11 slots for a high vertex)**

**Hypothesis bookkeeping (important, and it makes the target easier).** What closes pocket 1 is
"C ∈ RES(b) ⟹ path(C) ≥ 6", i.e. **RES(b) ∧ (no induced P₆) = ∅** — and the extra hypothesis is
free, because (R3b) itself was derived (Lemma G16) from path(G) ≤ 5. Lemmas G17/G18/G19/G20 and
the |H| ≤ 24 window need **no** path hypothesis; the sharper bounds below use G13/G15, which have
the shape "path ≥ 6 **or** structure", so they are available only under path ≤ 5. Both readings
are legitimate targets; the path-≤-5 one is strictly weaker and should be preferred.

> **Lemma G21.** Let C ∈ RES(b) with path(C) ≤ 5, let u,z realise diam = 3 with a(u) = a(z) = 2.
> Take the induced C₆ Z = (u, u₁, u₂, z, y, x) supplied by **G13** (positions 0..5). Then every
> high vertex lies in an explicit list of at most **11** slots:
> **(i)** the four cycle vertices u₁,u₂,x,y (u and z are excluded by (R3b): a ≤ 2);
> **(ii)** u₁′ and u₂′ — the possible second vertices of the u₁-component of N(u) and of the
> u₂-component of N(z);
> **(iii)** at most one vertex for each of the four cycle-pairs (u₁,u₂), (y,x), (u₁,y), (u₂,x);
> **(iv)** at most one vertex with no neighbour on Z at all, and it must be adjacent to both
> u₁′ and u₂′.
> Moreover **d(x), d(y) ≤ 4 and d(u₁), d(u₂) ≤ 5**, so the four cycle vertices contribute at most
> 3+3+2+2 = **10** to Σ_H(a−2); hence **at most 7 vertices carry mass > n − 10**.

*Proof.* Let h ∈ H, h ∉ Z. By **G15**(a),(b) h has 0 or 2 neighbours on Z, and if 2 their cyclic
distance is 1 or 3, i.e. the pair is one of (u,u₁),(u₁,u₂),(u₂,z),(z,y),(y,x),(x,u),(u,z),(u₁,y),
(u₂,x). The pair (u,z) is impossible (d(u,z) = 3). If h ~ u then h ∈ N(u) = comp(u₁) ∪ {x}, and
h ∉ Z forces h = u₁′; the pair (x,u) is impossible for the same reason ({x} is a *singleton*
component of N(u), so nothing is adjacent to both x and u). Symmetrically h ~ z forces h = u₂′
and the pair (z,y) is impossible. This leaves the four pairs of (iii), and each is realised by at
most one vertex (two would be two common neighbours of a pair ⟹ C₄). If h has no Z-neighbour,
then d(h,u) = 2 forces a common neighbour inside N(u) = {u₁,u₁′,x}, and u₁,x ∈ Z, so h ~ u₁′;
symmetrically h ~ u₂′; and u₁′ ≠ u₂′ (N(u) ∩ N(z) = ∅), so again C₄-freeness allows at most one
such h. Degrees: by the G15(c) argument, an outside neighbour of a cycle vertex v_i is adjacent
to v_{i−1}, v_{i+1} or v_{i+3}, at most one each; for x (position 5) the v_{i+1} = u slot is
empty by the singleton-component argument above, so d(x) ≤ 2 + 2 = 4, and symmetrically for y;
for u₁ all three slots may be occupied, so d(u₁) ≤ 5. ∎

**Consequence (window, sharp form).** In this branch **6 ≤ |H| ≤ 11** (G18.1 + G21), the seven
non-cycle slots carry Σ(a−2) > n − 10, and Σ_{h∈H} t(h) < |H|(|H|−5)/2 ≤ 33. *Numerical status:
G21 is a conditional structure lemma inside RES(b) (empty in every sample), so it inherits the
backing of its two inputs — G13 and G15 — which were asserted over the exhaustive C4-free n ≤ 13
range (1272 non-vacuous induced-C₆ instances, 0 failures, round 4). Flagged as **not directly
non-vacuously tested**; it must not be promoted past provisional until a RES(b)-shaped instance
or a hand-checked partial configuration exists.*

## 16.6 Round-5 numerical summary

```
problems/wowii/w133_res_kill.py  ->  w133_res_kill.out   (0 assert failures, ~1 s)
  (A) (R3a) vs (R3b): 5 explicit witnesses in RES(a) \ RES(b)   => RES(a) INHABITED
      path certificates 21/21/16/22 (>= 6)                      => conjecture unharmed
  (B) pool = 48 connected C4-free graphs (n = 8..133; Petersen, HS, HS+leaf, HS+trileaf,
      ER_5/7/11, ER_5+leaf, 40 random maximal C4-free)
      G20 centre identity            371 instances, 0 failures
      G17 confinement bound         1363 distance-3 pairs, 0 failures
      G18 Bonferroni                 329 subsets, 0 failures
      (*) fibre count / G17b         301 centres, 0 failures
  (C) structured hunt (no exhaustive search): 19 graphs in the plain class
      (C4-free, rad 2, diam 3, l > 3); 5 of them in RES(a); **0 in RES(b)**
```

**Firewall statement (T13).** §16.1 proves RES(a) ≠ ∅ and therefore only *refutes the literal
round-4/round-5 target*; it is **neither evidence for nor against** RES(b) = ∅. §16.3–§16.5 are
unconditional C4-free lemmas plus consequences *inside* RES(b); the hunt in (C) covered ~380
constructed graphs and is **not** an emptiness proof.

## 16.7 Status update (supersedes §15.6)

* **(R3) reading settled**: proofs must use **(R3b)**, available only via **Lemma G16** (core
  property). RES := RES(b). §15.3's equivalence claim retracted.
* **New unconditional lemmas** (proved + numerically backed): **G17** (ball confinement),
  **G18** (mass–Bonferroni), **G20** (centre identity), **G17b** (centres see a high vertex at
  distance 2). **New RES(b)-internal results**: **G18.1/G18.2** window 6 ≤ |H| ≤ 24 (≤15 under
  G13), **G19** (no leaf endpoint), and the **δ_H dichotomy** of §16.5.
* **r ≥ 4 residual, pocket 2**: unchanged.
* **Red lines**: no SAT, no large-space exhaustion (only explicit constructions + 40+240 random
  greedy C4-free graphs, all run before writing); Petersen/HS in every sample; all new claims
  asserted in the script, exit code 0.

---
# §17 owner-w133 round 6 (2026-08-18, opus): both harvests adjudicated, G12 repaired, and the decisive step named

*(All numbers in this section come from `problems/wowii/w133_r6_adjudicate.py`, log
`problems/wowii/w133_r6_adjudicate.out`, exit 0, TOTAL ASSERT FAILURES: 0, ~24 s.
Script labels G12.1 / G22 / G23 match the draft labels used here, per planner's round-5
minor correction.)*

## 17.1 Adjudication A — Qwen S3 review of Theorem G12: **the GAP is REAL, and patched**

Harvest: `problems/wowii/w133_S3_G12_qwen.md` (Qwen3.8-Max, 6 named joints, no Qwen material
inside ⟹ eligible judge). Verdict there: **GAP on G12-J1**, other five joints CLEAN.

**Owner's adjudication: REPRODUCED — the gap is real.** §13.1 Step 1 as written said
"triangle-free + C4-free + diam 2 ⟹ girth 5 (hence Moore)". Explicit counterexamples to the
step *as stated*: the stars K_{1,m} (m = 2,3,5,9,20 all run) are triangle-free, C4-free, of
diameter 2, **contain no cycle at all** and are not regular. The Hoffman–Singleton appeal
therefore had an unstated hypothesis.

**Severity: minor; Theorem G12 itself is unharmed.** The missing exclusion is supplied by
**Lemma G12.1** (now inserted verbatim in §13.1): stars have l = 2m/(m+1) < 2, killed by
l > 3; any graph *with* a cycle has girth ≤ 2·diam+1 = 5, and triangle-free + C4-free gives
girth ≥ 5, so girth = 5 exactly. This is the owner's own two-line route; Qwen proposed a
longer one (nonadjacent vertices with a unique common neighbour have equal degree ⟹ unequal
degrees force adjacency ⟹ non-regular ⟹ star). Qwen's route is *also* correct as far as the
owner checked it, but G12.1 is shorter and avoids the degree-transfer argument entirely, so
**G12.1 is what enters the draft**.

*Numerics (non-vacuous, exhaustive small-graph table — allowed):* over **all** labelled
graphs on n ≤ 7 there are 111 843 connected C4-free ones, of which **37** are triangle-free
with diam 2; their shape census is **25 stars + 12 girth-5 graphs**, every girth-5 one regular
with degree in {2,3,7,57} — exactly the G12.1 dichotomy, with no third shape. Controls:
Petersen (girth 5, k = 3, l = 3 — excluded by strictness) and HS (girth 5, k = 7, l = 7).

> **Status of Theorem G12: CLEAN after the G12.1 patch** (J2–J6 CLEAN per the Qwen review;
> J1 repaired and re-verified by the owner). The S3 round for G12 counts as one clean
> cross-model adversarial pass **on the patched statement**; the patch itself has not yet
> been reviewed by a second model — that is now a queued S3 item.

## 17.2 Adjudication B — Qwen RES(b) solver harvest: **PARTIAL, conditional, NOT adopted**

Harvest: `problems/wowii/w133_RES_qwen_r5.md` (two tabs, both PARTIAL). Claim: under (C6)
(no induced P₆), the branch "the diameter-3 pair u,z has a(u) = a(z) = 2" is **empty**, via a
six-slot classification and a mass count F(C) = Σ(a(v)−3) ≤ −2 < 0; the open branch is the
**triangular endpoint** a(u) = 1.

**Owner's adjudication.**
1. **Line-by-line verification is impossible from this artifact**: the harvest is a faithful
   *summary*, not a transcript (the file says so itself). Nothing in it may be promoted to
   PROVED. The two tabs' agreement is *not* independence evidence either — both were handed
   the same Facts 1–10 preamble.
2. **One verified error.** Tab B's "explicit minimal example" of the open regime (two
   triangles u,p,q and z,r,s joined by cross-edges p~r, q~s) **contains a C₄** (p–r–s–q–p,
   induced), so it is not in the class at all; it also has l = 5/3 < 3, as Tab B admitted.
   Re-run in the script. This is an illustration, not a load-bearing step, but it is a
   verified defect and it fixes the T12 amendment below.
3. **The slot classification is not new**: their six slots are exactly draft **G21**(ii)+(iii)
   (u₁′, u₂′ and the four cycle-pair slots), independently re-derived. Genuinely new relative
   to §16.5b are (α) the claim that (C6) kills G21(iv)'s zero-Z-neighbour high vertex, and
   (β) the mass count that turns the classification into emptiness.
4. **The mechanism of (β) is independently confirmed for 8 of the 11 slots** — but by the
   owner's **Lemma G22** below, not by their argument (see Corollary G22.1). Their step
   "a(X) = β(X) + comp(N_O(X))" is only legitimate once each slot vertex's degree is bounded,
   which they assert rather than derive in the summary; G22 supplies exactly that for 8 slots
   and **fails to supply it for the two opposite-pair slots**, which is precisely where their
   Lemma 6.1 (flagged by both tabs as the crux where (C5) enters) sits.

> **Verdict: registered as CONDITIONAL, not folded in.** "The a(u)=a(z)=2 branch of
> RES(b) ∧ (C6) is empty" is recorded as **Claim Q6.1 (Qwen, unverified)**. Downstream
> same-source rule: any later Qwen judge is *ineligible* for Q6.1.

## 17.3 **Lemma G22 (NEW, unconditional — the round's main tool)**

> **Lemma G22(k).** Let G be C4-free (no two vertices have two common neighbours) with **no
> induced P_{k+1}**, k ≥ 3. Then every endpoint of an induced P_k has degree ≤ **k**.
> The case used by this line: **C4-free + no induced P₆ ⟹ every endpoint of an induced P₅
> has degree ≤ 5.**

*Proof.* Let (v₀,…,v_{k−1}) be an induced P_k and w ∈ N(v₀)∖{v₁,…,v_{k−1}}. If w had no
neighbour among v₁,…,v_{k−1} then (w,v₀,…,v_{k−1}) would be an induced P_{k+1}. So
w ∈ N(v₀) ∩ N(v_i) for some i ≥ 1, and each such intersection has size ≤ 1 by C4-freeness.
That is ≤ k−1 vertices; adding v₁ (the only path vertex in N(v₀), the path being induced)
gives d(v₀) ≤ k. ∎

*Numerics (non-vacuous):* over the exhaustive n ≤ 7 C4-free pool, k = 3/4/5 tested on
4 226 / 67 344 / 194 280 induced-P_k endpoints, **0 failures**; plus 17 greedy random
C4-free ∧ P₆-free graphs on n = 8..14 (max degree 8 in that pool), 66 endpoints, 0 failures;
plus Petersen, C₅, C₆.
**Tightness of the hypothesis:** the friendship graphs F_k (k triangles glued at a vertex) are
C4-free and P₆-free with an unbounded degree 2k — and they contain **no induced P₅ at all**.
So "endpoint of an induced P₅" cannot be dropped. (The constant 5 itself is not claimed
sharp: the largest P₅-endpoint degree seen in any sample was 3.)

## 17.4 **Corollary G22.1: 8 of G21's 11 slots have degree ≤ 5, for free**

Work inside RES(b) ∧ (C6) in the branch a(u) = a(z) = 2, with the induced C₆
Z = (u,u₁,u₂,z,y,x) of **G13** and the slots of **G21**.

* Any 5 consecutive vertices of an induced C₆ form an induced P₅ ⟹ **every cycle vertex has
  degree ≤ 5** (recovers G21's d(u₁),d(u₂) ≤ 5 uniformly; G21's d(x),d(y) ≤ 4 stays sharper).
* **Slot u₁′** (second vertex of the u₁-component of N(u)): (u₁′,u,x,y,z) is induced —
  u₁′ ≁ x because {x} is a singleton component of N(u); u₁′ ≁ y,z because G15(a) gives it
  exactly the two Z-neighbours u,u₁ — so **d(u₁′) ≤ 5**; symmetrically d(u₂′) ≤ 5.
* **Adjacent-pair slots**: h ~ u₁,u₂ gives the induced P₅ (h,u₁,u,x,y); h ~ y,x gives
  (h,y,z,u₂,u₁). Both ⟹ **d(h) ≤ 5**.
* **Not covered — exactly two slots**: the *opposite* pairs h ~ {u₁,y} and h ~ {u₂,x}. For
  those, every P₅ inside Z ∪ {h} is killed by h's second Z-neighbour (checked: all four
  candidates h–u₁–u–x–y, h–u₁–u₂–z–y, h–y–z–u₂–u₁, h–y–x–u–u₁ have a chord at h). Together
  with G21(iv)'s zero-neighbour slot, these are the **three** slots whose degrees are still
  unbounded — and they are the same three places where the Qwen argument does its real work.

## 17.5 **Lemma G23 + THE DECISIVE STEP (the triangular-endpoint branch)**

Both harvest tabs, and the draft's own bookkeeping (§16.3 only bounds a(u),a(z) ≤ 2; **G13
needs a(u) = a(z) = 2**), leave exactly one branch: **some diameter-3 pair has an endpoint u
with a(u) = 1**. By C4-freeness a(u) = 1 means N(u) is a clique of size ≤ 2, and **G19**
excludes leaves, so d(u) = 2 and N(u) = {p,q} with p ~ q.

> **Lemma G23.** Let C be C4-free, u ∈ C with a(u) = 1, d(u) = 2, N(u) = {p,q}, ecc(u) = 3.
> Put B_p := N(p)∖{u,q}, B_q := N(q)∖{u,p}. Then
> **(a)** p ~ q and N(p) ∩ N(q) = {u};
> **(b)** ball₂(u) = {u,p,q} ⊔ B_p ⊔ B_q and **|ball₂(u)| = d(p) + d(q) − 1**;
> **(c)** every h ∈ B_p has at most **3** neighbours in {p,q} ∪ B_p ∪ B_q (namely p, ≤1 in
> B_p, ≤1 in B_q), and every w ∉ {u,p,q} has ≤1 neighbour in B_p and ≤1 in B_q; hence for
> H′ := {v ∈ B_p ∪ B_q : a(v) ≥ 3}, **Σ_{h∈H′} d(h) ≤ 2(n−3) + |H′|**;
> **(d)** a(p) ≤ d(p) − 1 and a(q) ≤ d(q) − 1 (the triangle upq costs one component).

*Proof.* (a) N(u) = {p,q} is a clique; two common neighbours of p,q other than u would give a
C₄ with u. (b) Every b ∈ ball₂(u)∖{u,p,q} has exactly one neighbour in {p,q} (≥1 by
definition, ≤1 by (a)); the count is 3 + (d(p)−2) + (d(q)−2). (c) h ∈ B_p is not adjacent to
q (else h ∈ N(p)∩N(q) = {u}); two neighbours of h in N(p) would give h,p two common
neighbours; h ≁ q so |N(h) ∩ N(q)| ≤ 1. The same C4-freeness at p (resp. q) gives the "≤1
neighbour in B_p (resp. B_q)" statement for every w, and summing deg over V ∖ {u,p,q} — where
each of the n−3 vertices contributes ≤ 2, and p,q contribute |H′ ∩ B_p|, |H′ ∩ B_q| — gives
the displayed inequality. (d) uq (resp. up) is an edge inside N(p) (resp. N(q)). ∎
*Numerics: 79 852 instances (every a = 1, eccentricity-3 vertex in the exhaustive n ≤ 7
C4-free pool plus HS+leaf, ER_5/ER_7+leaf and 30 random maximal C4-free graphs), 0 failures.*

> **Corollary G23.1 (branch shape).** In RES(b), (R3b) gives H ⊆ ball₂(u), and u ∉ H, so
> **6 ≤ |H| ≤ d(p)+d(q) − 2** (lower bound = G18.1), i.e. **d(p)+d(q) ≥ 8**; and l > 3 forces
> **a(p) + a(q) + Σ_{h∈H′}(a(h) − 2) > n + 5**
> [from Σ_v a > 3n with a(u) = 1 and a ≤ 2 off H].

> **Corollary G23.2 (one degree bound away from a finite window).** If every vertex of
> {p,q} ∪ H′ is an endpoint of an induced P₅, then G22 gives all these degrees ≤ 5, hence
> a(p),a(q) ≤ 4 and |H′| ≤ |B_p|+|B_q| = d(p)+d(q)−4 ≤ 6, so G23.1 reads
> n + 5 < 4 + 4 + 3·6 = 26, i.e. **n ≤ 20**. With "no C4-free graph with l > 3 exists for
> n ≤ 13" (§15.5) the branch collapses to the finite window **14 ≤ n ≤ 20** with d(u) = 2 and
> every named vertex of degree ≤ 5.

> ### **DECISIVE STEP (D6), the single question this line now hangs on**
> *In RES(b) ∧ (C6) with a triangular diameter endpoint u (a(u) = 1), is every vertex of
> {p,q} ∪ H′ an endpoint of some induced P₅?* Equivalently (G22 contrapositive): **can a
> vertex of degree ≥ 6 in that configuration start no induced P₅ at all?**
> The friendship graphs show the question is not automatic; the two opposite-pair slots of
> §17.4 show the same obstruction in the sister branch. **Answering D6 affirmatively closes
> the triangular branch to a finite window; combined with Claim Q6.1 (once verified) it
> closes pocket 1.**

## 17.6 Round-6 numerical summary

```
problems/wowii/w133_r6_adjudicate.py -> w133_r6_adjudicate.out  (0 assert failures, 24 s)
  (A) G12-J1 adjudication: K_1,m (m=2,3,5,9,20) satisfy triangle-free+C4-free+diam 2,
      are acyclic and non-regular, l < 2                       => GAP REAL
      exhaustive n<=7: 111843 connected C4-free graphs; the 37 triangle-free diam-2
      members are exactly 25 stars + 12 girth-5 regular Moore graphs (k in {2,3,7,57})
                                                               => Lemma G12.1 verified
  (B) G22(k) for k=3,4,5: 4226 / 67344 / 194280 induced-P_k endpoints, 0 failures;
      17 greedy C4-free+P6-free graphs n=8..14 (max degree 8), 66 endpoints, 0 failures;
      friendship F_2,F_3,F_5,F_10: C4-free, P6-free, degree 2k, NO induced P5
                                                               => hypothesis necessary
  (C) G23(a)-(d): 79852 instances (a=1, ecc=3 vertices), 0 failures
      Tab B's "minimal example": contains an induced C4 and has l = 5/3  => REFUTED
```

**Firewall statement (T13).** §17.1 refutes a *step*, not Theorem G12; the theorem survives
with G12.1 added. §17.2 adopts **nothing** from the Qwen RES harvest: Claim Q6.1 is recorded
as unverified. §17.3–§17.5 are the owner's own, proved and numerically backed; G22 and G23 are
unconditional C4-free facts (tested outside RES(b), which is empty in every sample), while
G22.1 / G23.1 / G23.2 are consequences *inside* RES(b) and are therefore untested — flagged
provisional exactly like G21.

## 17.7 Status update (supersedes §16.7)

* **Theorem G12: CLEAN after patch** (Lemma G12.1 added; S3 pass on the patched statement is
  the queued item — the patch itself is not yet cross-model reviewed).
* **New unconditional lemmas: G22(k)** (P_k-endpoint degree bound; general, reusable, tight in
  its hypothesis) and **G23** (triangular diameter endpoint). New RES(b)-internal consequences:
  **G22.1** (8 of G21's 11 slots have degree ≤ 5) and **G23.1/G23.2**.
* **Pocket 1 is now two named items**: **Claim Q6.1** (the a(u)=a(z)=2 branch is empty under
  (C6) — Qwen-claimed, unverified, re-derivation queued) and **D6** (the decisive step above,
  owner-held). Nothing else is left in the r = 3 layer.
* **r ≥ 4 residual, pocket 2**: unchanged.
* **Red lines**: no SAT; the only exhaustive sweep is the n ≤ 7 labelled-graph table
  (small-graph table, allowed); everything else is explicit construction or random maximal
  C4-free generation; all assertions run before written; exit code 0.

## 17.8 **Lemma G24 (NEW, owner's own attack on the decisive step D6)**

*(Written after §17.5–§17.7 in the same round; it supersedes the D6 formulation there by
answering the first half of it and narrowing the rest. Same script/log, same 0 failures.)*

Setting throughout: C ∈ RES(b), u a **triangular diameter endpoint** (a(u) = 1, d(u) = 2,
N(u) = {p,q}, p ~ q, ecc(u) = 3). Layers from u: L₁ = {p,q}, L₂ = B_p ⊔ B_q, **D** := the
distance-3 layer (≠ ∅). Write H′ := H ∩ (B_p ∪ B_q); note H ⊆ {p,q} ∪ B_p ∪ B_q (R3b + G23),
n = 3 + |B_p| + |B_q| + |D|, and p,q have **no** neighbour in D.

> **Lemma G24.**
> **(a) (local mass bound, unconditional)** every h ∈ B_p ∪ B_q satisfies
> **a(h) − 2 ≤ |N(h) ∩ D|**.
> **(b) (one-sided branch is dead)** if d(q) = 2 (i.e. B_q = ∅) — equivalently u and q are
> degree-2 twins in the triangle upq — then RES(b) is contradicted outright. Hence
> **d(p), d(q) ≥ 3**.
> **(c) (the distance-3 layer dominates)** **|D| ≥ 6**; and more precisely
> Σ_{h∈H′}|N(h) ∩ D| > |D| + 5.
> **(d) (two-parent rigidity)** let D₂ := {y ∈ D : y has a neighbour in H′∩B_p *and* one in
> H′∩B_q}. Then **|D₂| ≥ 6**, the map y ↦ (its B_p-parent, its B_q-parent) is **injective**
> on D₂, and therefore **|H′∩B_p| · |H′∩B_q| ≥ 6** (in particular both sides carry hubs).
> **(e) (G22 trigger)** if some h ∈ H′∩B_p is the B_p-parent of **two** vertices of D₂, then
> **d(h) ≤ 5**; symmetrically on the q-side.

*Proof.* **(a)** For h ∈ B_p: h ≁ u and h ≁ q (G23), so N(h) ⊆ {p} ∪ (N(h)∩B_p) ∪ (N(h)∩B_q)
∪ (N(h)∩D), with |N(h)∩B_p| ≤ 1 and |N(h)∩B_q| ≤ 1 (G23(c)). If h has a B_p-neighbour b then
p ~ b, i.e. N(h) contains the edge pb, so a(h) ≤ d(h) − 1 ≤ 2 + |N(h)∩D|; otherwise
d(h) ≤ 2 + |N(h)∩D| directly. Either way a(h) ≤ 2 + |N(h)∩D|. ∎
**(b)** B_q = ∅ gives N(q) = {u,p} with u ~ p, so a(q) = 1 and q ∉ H; also every y ∈ D has at
most one neighbour in B_p ∪ B_q = B_p (C4-freeness at p). Hence, using (a) and a(p) ≤ d(p)−1
(G23(d)), the mass (\*\*) obeys
Σ_{h∈H}(a(h)−2) ≤ (|B_p|−1) + Σ_{h∈H′}|N(h)∩D| ≤ (|B_p|−1) + Σ_{y∈D}|N(y)∩B_p| ≤ |B_p|−1+|D|
= (n−3)−1 = n−4 < n, contradicting Σ_{h∈H}(a(h)−2) > n. ∎
**(c)** With both sides non-empty, a(p)−2 ≤ |B_p|−1 and a(q)−2 ≤ |B_q|−1 are both ≥ 0-safe,
and each y ∈ D has ≤ 1 neighbour in B_p and ≤ 1 in B_q, so
n < Σ_{h∈H}(a(h)−2) ≤ (|B_p|−1)+(|B_q|−1)+Σ_{y∈D}|N(y)∩H′| ≤ |B_p|+|B_q|−2+2|D|
= (n−3−|D|)−2+2|D| = n+|D|−5, i.e. |D| > 5. The displayed sharpening is the same computation
before the last inequality. ∎
**(d)** Σ_{y∈D}|N(y)∩H′| ≤ |D| + |D₂| (each y contributes ≤ 1, plus 1 more exactly when
y ∈ D₂), so (c) gives |D₂| > 5. Two vertices of D₂ with the same parent pair would be two
common neighbours of that pair — a C₄. Injectivity gives |D₂| ≤ |H′∩B_p|·|H′∩B_q|. ∎
**(e)** Let y, y′ ∈ D₂ have B_p-parent h and B_q-parents c ≠ c′ (distinct by injectivity).
Since |N(h) ∩ B_q| ≤ 1, h is non-adjacent to at least one of them, say c. Then
**(h, y, c, q, u) is an induced P₅**: h ≁ c by choice, h ≁ q and h ≁ u (G23), y ≁ q and y ≁ u
(y ∈ D), c ≁ u (c ∈ B_q). Under (C6) Lemma **G22** applies to this P₅ and gives d(h) ≤ 5. ∎

*Numerics:* (a), the layer decomposition n = 3+|B_p|+|B_q|+|D|, "p,q have no D-neighbour",
"≤ 1 parent per side" and the injectivity of the two-parent map were asserted on all **79 852**
carriers (every a = 1, eccentricity-3 vertex of the exhaustive n ≤ 7 C4-free pool plus
HS+leaf, ER_5/ER_7+leaf and 30 random maximal C4-free graphs) — **0 failures**. (b)–(e) are
RES(b)-internal and therefore untested, like G21/G22.1.

**(e′) — the strong form of (e), and the one that actually moves the line.** *(An earlier
draft of this paragraph asserted "|H′∩B_p| ≥ 6 once the p-side carries a hub of degree ≥ 6";
that was wrong — a degree-≤5 hub may parent several D₂-vertices — and is replaced by:)*

> **Lemma G24(e′).** Let h ∈ H′∩B_p with **d(h) ≥ 6**, in the branch where *every* diameter-3
> pair of C has an endpoint of a-value 1. Then
> **(1)** |N(h) ∩ D| ≥ d(h) − 3 ≥ 3 (G23(c));
> **(2)** every y ∈ N(h)∩D whose B_q-parent is not adjacent to h yields the induced P₅
> (h,y,c,q,u), so by G22 all B_q-parents of N(h)∩D lie in N(h)∩B_q, a set of size ≤ 1; and at
> most one y ∈ N(h)∩D can be adjacent to that single vertex (two would give a C₄);
> **(3)** hence **≥ 2 vertices y ∈ N(h)∩D have no B_q-parent at all, i.e. d(q,y) = 3**: each is
> a fresh diameter pair (q,y);
> **(4)** a(q) = 1 is impossible (it forces d(q) = 2, killed by G24(b)), so the branch
> hypothesis gives **a(y) = 1** — and by G19, d(y) = 2 with N(y) = {h, y\*}, h ~ y\*: **y is a
> second triangular diameter endpoint, hanging on h**;
> **(5)** applying G23(b) at y (H ⊆ ball₂(y) for every vertex, since hubs have ecc ≤ 2) gives
> H ⊆ {h,y\*} ∪ N(h) ∪ N(y\*); intersecting with H ⊆ {p,q} ∪ B_p ∪ B_q (the u-frame) and using
> G23(c) twice (≤ 3 each; ≤ 2 if y\* ∈ D) yields **|H| ≤ 8**.
> With G18.1's |H| ≥ 6 this pins the whole configuration: **6 ≤ |H| ≤ 8, every hub equals or is
> adjacent to h or y\***.

> ### **D6 restated after G24 — exactly what is left**
> **(D6a)** *All hubs have degree ≤ 5.* Then a(h) ≤ 5 for h ∈ H′ and G23.1 reads
> n + 5 < a(p)+a(q)+3|H′|; the branch is a finite-type system in (|B_p|,|B_q|,|D|) —
> and if additionally p,q have degree ≤ 5 (G23.2) it collapses to **14 ≤ n ≤ 20**.
> **(D6b)** *Some hub has degree ≥ 6.* Then G24(e′) applies: a second triangular endpoint y
> hangs on that hub, **|H| ≤ 8**, and every hub is h, y\*, or a neighbour of one of them.
> Both sub-cases are now bounded, explicitly listed configurations rather than an open class.
> **Killing (D6a) and (D6b) closes the triangular branch; that plus Claim Q6.1 closes pocket 1.**

**Fold-in: what G23/G24 do to the δ_H dichotomy of §16.5.** The dichotomy reads
|H|(n−1) ≤ (4+δ_H)(n + C(|H|,2)) with δ_H := max_{h∈H}|N(h) ∩ H|, so either
**δ_H ≥ |H| − 4** (near-universal hub) or **n ≤ [(4+δ_H)C(|H|,2) + |H|] / (|H| − 4 − δ_H)**.
In the triangular branch this collapses, because G23(c) caps the hub-degree of *every* hub off
{p,q}: for h ∈ H′, |N(h) ∩ H| ≤ |N(h) ∩ ({p,q} ∪ B_p ∪ B_q)| ≤ **3**. Hence

> **δ_H = max(≤3, |H ∩ B_p| + [q ∈ H], |H ∩ B_q| + [p ∈ H])** — i.e. **the only possible
> near-universal hub is p or q**, and then all but ≤ 4 hubs sit in the single fibre B_p (resp.
> B_q), which by G24(d) still needs |H′∩B_p|·|H′∩B_q| ≥ 6 on the *other* side. If neither p
> nor q is a near-universal hub then δ_H ≤ 3 and the first branch forces **|H| ≤ 7**, so with
> G18.1 **|H| ∈ {6,7}**; otherwise the second branch gives the absolute bound
> n ≤ 204 (|H| = 8), n ≤ 130 (|H| = 9), and less for larger |H|.

So in the triangular branch the δ_H dichotomy no longer has an open "very rigid configuration"
side to hide in: it is either a p/q-centred fibre configuration or an explicitly bounded n.

# §18 owner-w133 round 7 (2026-08-18, opus): **the triangular branch is EMPTY** — D6a and D6b both closed, pocket 1 is down to one item

*(All numbers in this section are produced by `problems/wowii/w133_r7_triend.py`,
log `problems/wowii/w133_r7_triend.out`, exit 0, 0 assert failures.)*

Setting throughout §18.1–§18.2: **C ∈ RES(b)** (connected, C4-free, rad = 2, diam = 3,
l > 3, (R3b)) with **no induced P₆** (C6), and **u a vertex with a(u) = 1 and ecc(u) = 3**.
By F3/G23 a(u) = 1 makes N(u) a clique of size ≤ 2, and G19 excludes leaves, so
**d(u) = 2, N(u) = {p,q}, p ~ q**. Notation of G23/G24: B_p := N(p)∖{u,q}, B_q := N(q)∖{u,p},
D := the distance-3 layer, β_x := |B_x| = d(x) − 2, δ_h := |N(h) ∩ D|,
H′ := H ∩ (B_p ∪ B_q), η_x := |H ∩ B_x|, e_x := #edges inside B_x, and
n = 3 + β_p + β_q + |D| with p, q having no neighbour in D.

## 18.1 **Lemma G25 (NEW; (a)(b)(c) unconditional, (d) needs (C6) + (R3b) + G24(b))**

*(Label corrected in round 8 after the non-Qwen S3 pass — see §20.7 finding 3. The header
formerly read "unconditional; (d) needs (C6)", which understated (d)'s hypotheses. No step of
the mathematics changed. Also, throughout §18, **β_p, β_q ≥ 1 by G24(b)**, which is what makes
a(p) − 2 = β_p − 1 − e_p ≥ 0 in G26 step (1) — recorded here explicitly.)*

> **(a) There is NO edge between B_p and B_q.**
> **(b)** every h ∈ B_p ∪ B_q satisfies **a(h) ≤ 1 + δ_h**.
> **(c)** if b ∈ B_p has ecc(b) = 2 then **β_q ≤ δ_b** (symmetrically on the q-side).
> **(d)** under (C6), **every hub of B_p ∪ B_q has degree ≤ 5**, hence δ_b ≤ 4; and with (c),
> **β_p, β_q ≤ 4** as soon as both sides carry a hub.

*Proof.* **(a)** If h ∈ B_p, c ∈ B_q and h ~ c, then p and c have the two common neighbours
h and q (p ~ q by the triangle upq), a C₄. ∎ *(Consequence: N(h) ⊆ {p} ⊔ (N(h)∩B_p) ⊔ (N(h)∩D)
for h ∈ B_p, so **|N(h) ∩ ({p,q} ∪ B_p ∪ B_q)| ≤ 2** — this **strengthens G23(c) from 3 to 2**
and is exactly the slack that kept the branch alive.)*
**(b)** |N(h) ∩ B_p| ≤ 1 (two such neighbours would give h and p two common neighbours). If
N(h) ∩ B_p = {b}, then pb is an edge inside N(h), so a(h) ≤ d(h) − 1 = 1 + δ_h; otherwise
d(h) = 1 + δ_h ≥ a(h). ∎ *(This **improves G24(a) by one unit**: a(h) − 2 ≤ δ_h − 1.)*
**(c)** For c ∈ B_q we have d(b,c) ≥ 2 by (a), so ecc(b) = 2 gives a common neighbour w of
b and c. w ≠ p (p ≁ c, since N(p) ∩ N(q) = {u}); w ∉ B_p by (a); so w ∈ N(b) ∩ D. Each
D-vertex has ≤ 1 neighbour in B_q (C4-freeness at q), so c ↦ w is injective. ∎
**(d)** Let h ∈ H ∩ B_p with d(h) ≥ 6. By (R3b) ecc(h) ≤ 2, and ecc(h) = 1 would force
diam ≤ 2, so ecc(h) = 2. By G24(b) β_q ≥ 1. If some y ∈ N(h) ∩ D had a neighbour c ∈ B_q,
then c ∉ N(h) by (a) and **(h,y,c,q,u) is an induced P₅** (h ≁ c, h ≁ q, h ≁ u, y ≁ q, y ≁ u
by G23, c ≁ u), so **G22** gives d(h) ≤ 5 — contradiction. Hence no vertex of N(h) ∩ D has a
B_q-neighbour, and the injection of (c) has empty target: β_q ≤ 0, contradicting β_q ≥ 1. ∎
*Numerics: **79 852** triangular-endpoint carriers (every a = 1, d = 2, ecc = 3 vertex of the
exhaustive n ≤ 7 C4-free table plus HS(+leaf), ER_5/ER_7(+leaf), Petersen and 30 random maximal
C4-free graphs); (a) 79 852 instances, (b) 190 895, (c) 72 654, (d)'s induced-P₅ 20 623 —
**0 failures**.*

## 18.2 **Theorem G26 (NEW — the branch dies)**

> **Theorem G26.** In RES(b) ∧ (C6) **no vertex has a-value 1 and eccentricity 3**.
> Equivalently: **every pair at distance 3 has both a-values equal to 2**.
> In particular the triangular-endpoint branch — **D6a and D6b together** — is **EMPTY**.

*Proof.* Suppose u is such a vertex; keep the notation above.

**(1) The mass inequality.** a(p) = d(p) − t(p) = β_p + 1 − e_p (the only edges inside N(p) are
uq and the e_p edges of B_p), so a(p) − 2 = β_p − 1 − e_p ≥ 0, likewise at q; and
a(h) − 2 ≤ δ_h − 1 for h ∈ H′ by G25(b). With
Σ_{h∈H′} δ_h = Σ_{y∈D} |N(y) ∩ H′| ≤ |D| + |D₂| (each y has ≤ 1 parent per side, and
contributes 2 exactly when both parents are hubs, i.e. y ∈ D₂), F1 gives
n < (β_p−1−e_p) + (β_q−1−e_q) − |H′| + |D| + |D₂|; substituting n = 3+β_p+β_q+|D| yields
**|D₂| ≥ 6 + η_p + η_q + e_p + e_q**. The two-parent map y ↦ (B_p-parent, B_q-parent) is
injective on D₂ (G24(d)), so |D₂| ≤ η_p·η_q and
> **(η_p − 1)(η_q − 1) ≥ 7 + e_p + e_q.**

**(2) Both sides are saturated.** (1) forces η_p, η_q ≥ 2, so both sides carry hubs and G25(d)
applies: β_p, β_q ≤ 4, hence η_p, η_q ≤ 4. The only integer pair with both entries ≤ 4 and
(η_p−1)(η_q−1) ≥ 7 is **η_p = η_q = 4**, so β_p = β_q = 4 and **every vertex of B_p ∪ B_q is a
hub**; d(p) = d(q) = 6.

**(3) The B-vertices are pinned.** For a hub b ∈ B_p, G25(c) gives δ_b ≥ β_q = 4 while
G25(d) gives d(b) ≤ 5 = 1 + |N(b)∩B_p| + δ_b; hence **|N(b)∩B_p| = 0, δ_b = 4, d(b) = 5**, and
therefore **e_p = e_q = 0**, a(p) = a(q) = 5.

**(4) The graph is completely determined.** a(p) = 5 ≥ 3 makes p a hub, so ecc(p) = 2 and every
y ∈ D has a B_p-parent; symmetrically a B_q-parent. Counting the B_p–D edges,
|D| = Σ_{b∈B_p} δ_b = 16, and injectivity makes y ↦ (b,c) a **bijection D → B_p × B_q**. Thus
**n = 3 + 4 + 4 + 16 = 27**.

**(5) The contradiction.** Fix y ∈ D with B_p-parent b₁ and let b be one of the other three
vertices of B_p. b is a hub, so ecc(b) = 2 and b, y have a common neighbour w. w ≠ b₁ (e_p = 0),
w ∉ B_q by G25(a), so w ∈ N(y) ∩ D — and the unique B_p-parent of w is b, so the three choices
of b give three distinct w. Hence d(y) ≥ 2 + 3 = 5, and in a C4-free graph
a(y) ≥ ⌈d(y)/2⌉ ≥ 3: **y is a hub at distance 3 from u**, contradicting H ⊆ ball₂(u) (R3b). ∎

**Remarks.** (i) The proof never uses the branch hypothesis (TRI) — only the existence of *one*
vertex u with a(u) = 1, ecc(u) = 3 — which is why it yields the stronger "every distance-3 pair
has both a-values 2". (ii) (C6) enters **only** through G25(d) (via G22). (iii) **G24(e′) is
superseded**: its trigger (a hub of degree ≥ 6 in B_p ∪ B_q) is *vacuous* by G25(d), so D6b is
empty for a much simpler reason than the |H| ≤ 8 route. (iv) The D6a finite-window computation
designed for this round is **no longer needed** — the window is closed by proof, not by search
(no exhaustive space was entered; the only sweeps are the n ≤ 7 table and two bounded integer
sweeps over (η_p,η_q,e_p,e_q) ∈ [0,4]⁴ and (ε_b,δ_b)).

> **Corollary G26.1 (pocket 1 residual).** In RES(b) ∧ (C6) every diameter pair (u,z) has
> a(u) = a(z) = 2, i.e. **G13/G21 apply to every diameter pair** and pocket 1 reduces to the
> single statement of **Claim Q6.1** (the a(u) = a(z) = 2 branch is empty). Pocket 1 is now
> **one item**, not two.

## 18.3 Adjudication of the three Q12 harvests (`problems/wowii/w133_TRIEND_qwen_{A,B,C}.md`)

All three self-report `VERDICT: SOLVED-EMPTY`; all three are **summaries, not transcripts**;
all three were produced by one model from one brief, so their agreement is **not** independent
confirmation (Entry C's own file says so). Line-by-line outcome:

1. **Entry A (D6a) — one idea ADOPTED, the delivered proof NOT adopted.** Its self-flagged
   strengthening *"any edge B_p–B_q gives a 4-cycle"* is **CORRECT** and is the one genuinely
   valuable thing in the three tabs; it is adopted above as **G25(a)** with the owner's own
   proof. Its Case I step *"every D-vertex has one parent on each side and injects into
   B_p × B_q, so |D| ≤ 9"* is **REFUTED as stated** — injectivity is available only on the
   two-parent set D₂, and the pool contains carriers with single-parent D-vertices (script
   prints one). Its *"hub excess ≤ |D| − 1"* does not follow from the supplied facts. Its case
   split omits "neither p nor q is a hub", which happens to be vacuous (η ≥ 3 forces β = 3,
   d = 5, a ≥ 3) but is not addressed. **Conclusion correct, proof not adopted.**
2. **Entry B (D6b) — SUPERSEDED, not adopted.** Its whole argument runs inside the F9/G24(e′)
   configuration, which **G25(d) shows is vacuous**. Steps 1–2 (the two ball frames) are
   correct restatements of F7(b)/F8; steps 3–4 (the three-way split on y\*, the borderline
   |H′∩B_p|·|H′∩B_q| = 4) are unverifiable from a summary and are now unnecessary.
3. **Entry C (Claim Q6.1) — NOT adopted; Claim Q6.1 stays UNVERIFIED.** Its accounting device
   ("every valid addition leaves S = Σ(a−3) unchanged or decreases it; the maximum is S = −6")
   is **refuted as a general C4-free principle** by explicit witnesses (HS: S = +200;
   ER_5: +27; ER_7: +109, all C4-free) — a single hub with a = 5 contributes +2 — so the claim
   can only hold through branch-specific structure that the artifact does not exhibit. It also
   never treats the three unbounded-degree slots the brief explicitly demanded, and its
   "maximum" witness Z ∪ {v₃,v₄} has 8 vertices, below the known n ≥ 14.
4. **Shared-hidden-assumption sweep (methodology multi-tab clause).** The tabs' common input is
   PART 1–2 of `prompts/w133_r6_TRIEND_qwen.md` (F1–F9), all owner-proved and re-checked.
   **One shared slack found and it is decisive**: F7(c)/F8/F9 say *"≤ 1 neighbour in B_q"*
   where the truth is **zero** (G25(a)). This is a weakening, not an error — no tab's
   conclusion is invalidated by it — but it is precisely the assumption whose correction
   collapses the branch, and B and C inherited it uncorrected. **Brief-writing lesson (owner's
   own error): a fact stated non-tight in a brief propagates to every tab that shares it.**

## 18.4 Round-7 numerical summary

```
problems/wowii/w133_r7_triend.py -> w133_r7_triend.out   (exit 0, 0 assert failures, ~25 s)
  pool: 111 843 connected C4-free graphs on n <= 7 (small-graph table) + 37 explicit/greedy
        carriers (HS, HS+leaf, ER_5/7(+leaf), Petersen, 30 random maximal C4-free)
  (B) G25 on 79 852 triangular-endpoint carriers:
        (a) no B_p-B_q edge            79 852 instances, 0 failures
        (b) a(h) <= 1 + |N(h) & D|    190 895 instances, 0 failures
        (c) ecc(b)=2 => |B_q|<=delta_b 72 654 instances, 0 failures
        (d) (h,y,c,q,u) induced P5     20 623 instances, 0 failures
        general C4-free: a(v) >= ceil(d/2), d <= 2a, a=1 => d<=2, a<=2 => d<=4
  (A) Entry A |D|<=9 injection: single-parent D-vertex witness printed  => REFUTED
      Entry C Delta-S device: HS/ER_5/ER_7 have S = +200/+27/+109       => REFUTED
  (C) bounded integer sweeps: (eta_p-1)(eta_q-1) >= 7+e_p+e_q with eta <= 4
      => eta_p = eta_q = 4 in every solution; (eps_b,delta_b) => (0,4) uniquely
  (D) controls: Petersen/HS have diam 2 (the chain never starts); HS+leaf's a=1
      ecc-3 vertex is a LEAF (degree 1) and is excluded by G19 -- first failing
      step named, as required by T12.
```

**Firewall statement (T13).** §18.1–§18.2 are the owner's own proofs, run before written.
The only thing adopted from the harvests is the *observation* G25(a), re-proved here; every
harvest argument is refuted or superseded. §18.3's refutations are machine-checked. G25(a)–(c)
are unconditional C4-free facts tested outside RES(b) (empty in every sample); **G25(d) is NOT
unconditional** — it consumes (C6), (R3b) and G24(b), and the 20 623 instances quoted for it
test only its induced-P₅, not the lemma (round-8 correction, §20.7); G26's steps
(1)–(5) are RES(b)-internal and therefore untested, flagged provisional exactly like G21/G24 —
but unlike them they are now *closing* rather than *narrowing*.

## 18.5 Status update (supersedes §17.7)

* **D6 (the triangular branch) is CLOSED** by Theorem G26: D6a and D6b are both empty, and
  G24(e′) is superseded (vacuous trigger). The planned D6a finite-window search is cancelled.
* **New unconditional lemma G25** (four parts; (a) strengthens G23(c) 3 → 2, (b) strengthens
  G24(a) by 1, (c),(d) are new). **New theorem G26** + **Corollary G26.1**.
* **Pocket 1 = ONE item**: **Claim Q6.1** — RES(b) ∧ (C6) with a diameter pair of a-values
  (2,2) is empty. By G26.1 this is now the *only* possible shape, so G13/G15/G21/G22.1 all
  apply to it unconditionally. Nothing else remains in the r = 3 layer.
* **Owed**: cross-model S3 pass on the G12.1 patch (queued), and a **non-Qwen** adversarial
  review of G25/G26 before any PROVED promotion.
* **r ≥ 4 residual, pocket 2**: unchanged.
* **Red lines**: no SAT; the only exhaustive sweep is the n ≤ 7 labelled-graph table plus two
  bounded integer sweeps over a [0,4]⁴ box; every assertion run before being written; exit 0.

# §19 owner-w133 round 7 addendum: **Claim Q6.1 collapses to a finite window 14 ≤ n ≤ 20**

*(Same script/log as §18: `problems/wowii/w133_r7_triend.py` → `.out`, exit 0, 0 assert
failures, section (E). Written after §18 in the same round; it uses G26 as an input.)*

By **Corollary G26.1** every diameter pair of C ∈ RES(b) ∧ (C6) now has a-values (2,2), so
**G13/G15/G21 apply to every diameter pair unconditionally**. Fix u,z at distance 3 and the
induced C₆ **Z = (u,u₁,u₂,z,y,x)** at positions 0..5 (G13). G21's eleven slots:
the cycle vertices u₁,u₂,x,y; the partners **u₁′** (∼u,u₁) and **u₂′** (∼z,u₂); the four pair
slots **A** = (u₁,u₂), **B** = (y,x), **P** = (u₁,y), **Q** = (u₂,x) (at most one vertex each,
by C4-freeness); and **h₀**, the unique hub with no Z-neighbour. Write [S] = 1 if slot S is
occupied. Before this round, the three slots P, Q, h₀ had **no degree bound** (Cor G22.1), so
the mass Σ_H(a−2) was unbounded and the branch was an open class.

## 19.1 **Lemma G27 (h₀ is bounded — the 9th slot)**

> **d(h₀) ≤ 5.**

*Proof.* G21(iv) forces h₀ ∼ u₁′ (its distance-2 route to u must avoid u₁, x ∈ Z). By G15(b)
u₁′'s only Z-neighbours are u and u₁, and x is a *singleton* component of N(u), so u₁′ ≁ x;
u₁′ ≁ y (a second Z-neighbour of u₁′ would have to sit at cyclic distance 1 or 3 from u, and y
is at distance 2). Hence **(h₀,u₁′,u,x,y) is an induced P₅** (h₀ has no Z-neighbour at all, and
u ≁ y on an induced C₆), and G22 gives d(h₀) ≤ 5. ∎

## 19.2 **Lemma G28 (the partners must hold hands)**

> If u₁′ ∈ H then **u₂′ exists and u₁′ ∼ u₂′**; symmetrically for u₂′.

*Proof.* (R3b) gives ecc(u₁′) = 2, so u₁′ has a neighbour in N(z) = {u₂,u₂′,y}. u₁′ ∼ u₂ would
give u and u₂ the two common neighbours u₁,u₁′ (C₄); u₁′ ∼ y would be a third Z-neighbour,
against G15(a). ∎ *(Same argument: **P and Q are never adjacent to u₁′ or u₂′** — P ∼ u₁′ gives
u,P the common neighbours u₁,u₁′; P ∼ u₂′ gives z,P the common neighbours y,u₂′.)*

## 19.3 **Lemma G29 (the two opposite slots interlock)**

> If **d(P) ≥ 6** then P is adjacent to each of A, B, Q that exists. Consequently, since
> A and Q are both adjacent to u₂, and B and Q are both adjacent to x, **Q occupied ⟹ A and B
> are empty** (otherwise u₂, resp. x, has two common neighbours with P: a C₄).

*Proof.* Each of **(P,u₁,u,x,B)**, **(P,u₁,u,x,Q)**, **(P,y,z,u₂,A)** is an induced P₅ with
endpoint P whenever the last vertex exists and is *not* adjacent to P (all the required
non-adjacencies are read off the slot definitions: B,Q ≁ u,u₁ and A ≁ y,z, plus P ≁ u,x,z,u₂).
G22 would then give d(P) ≤ 5. ∎

## 19.4 **Lemma G30 (P's off-cycle neighbourhood is tiny) — all eleven slots are bounded**

> Write N(P) = {u₁,y} ⊔ (slot neighbours) ⊔ W_P, where W_P is the set of neighbours of P having
> **no** Z-neighbour. Then **|W_P| ≤ 3**, and **|W_P| ≤ 2** when Q is occupied. Hence
> **d(P) ≤ 7, and d(P) ≤ 5 whenever Q is occupied**; symmetrically for Q.

*Proof.* For w ∈ W_P, **(w,P,u₁,u,x) is an induced P₅** (w has no Z-neighbour; P ≁ u,x; u₁ ≁ x).
By (C6) no induced P₆ extends it, so **every neighbour of w other than P is adjacent to one of
P, u₁, u, x**; intersecting with "w's neighbours are off Z" leaves
N(w) ⊆ {P} ∪ {u₁′, A, B, Q} ∪ W_P. Each of the four apexes u₁′, A, B, Q can be adjacent to **at
most one** w ∈ W_P (two would give it and P two common neighbours: a C₄); and W_P ⊆ N(P) induces a
matching (C4-freeness), so each remaining w has N(w) = {P, w′} with w′ ∈ W_P and P ∼ w′, i.e.
N(w) is a clique: **a(w) = 1**. By **Theorem G26** ecc(w) = 2, so w must have a neighbour in
N(u) = {u₁,u₁′,x} — impossible, since w′ is off Z and u₁′ is not. So W_P consists only of the
≤ 4 apex-exceptions; with Q occupied, A and B are empty (G29), leaving ≤ 2. ∎
*(By G29 the count is ≤ 3 in general: the apexes available to P are u₁′ — excluded by G28 —
so really A, B, Q, of which Q excludes A and B.)*

## 19.5 **Lemma G31 (slot-wise mass caps) and the window**

> **a(u₁) ≤ 2 + [P]**, **a(u₂) ≤ 2 + [Q]**, **a(x) ≤ 2 + [Q]**, **a(y) ≤ 2 + [P]**;
> **a(u₁′), a(u₂′), a(A), a(B) ≤ 4**; **a(h₀) ≤ 5** (G27); **a(P), a(Q) ≤ 7**, and ≤ 5 when
> both are occupied (G30).

*Proof.* By G15(c) the off-cycle neighbours of u₁ (position 1) are exactly the possible
occupants of the (u,u₁), (u₁,u₂), (u₁,y) slots, i.e. u₁′, A, P: so d(u₁) = 2 + [u₁′]+[A]+[P],
while N(u₁) contains the edges u∼u₁′ and u₂∼A, giving t(u₁) ≥ [u₁′]+[A] and
a(u₁) = d(u₁) − t(u₁) ≤ 2 + [P]. The same at u₂, x, y (for x the forced edge is y∼B). Each of
u₁′, u₂′, A, B carries a forced triangle inside its neighbourhood (u∼u₁, z∼u₂, u₁∼u₂, y∼x
respectively), so a ≤ d − 1 ≤ 4 by G22.1. ∎

> **Corollary G31.1 (at least one opposite slot is occupied).** If neither P nor Q exists then
> a(u₁), a(u₂), a(x), a(y) ≤ 2, so H ⊆ {u₁′,u₂′,A,B,h₀} and **|H| ≤ 5**, contradicting
> |H| ≥ 6 (G18.1). *(The mass budget alone already gives Σ_H(a−2) ≤ 11 < 14 ≤ n.)*

> **Corollary G31.2 (THE WINDOW).** Σ_H(a−2) > n and the caps above give
> **n ≤ 20** when both P and Q are occupied, and **n ≤ 17** when exactly one is. With
> "no C4-free graph with l > 3 exists for n ≤ 13" (§15.5):
> ### **Claim Q6.1's branch satisfies 14 ≤ n ≤ 20, with every hub in an explicitly named slot of bounded degree.**

> **Corollary G31.3.** If x is a hub then B is occupied — G20 at x (ecc(x) = 2) reads
> n = 1 + d(u)+d(y)+d(B)+d(Q) − 2t(x), which without B is ≤ 1+3+3+5 = 12 < 14. Symmetrically
> for y. *(d(u), d(z) ≤ 3 by G13; d(y) = 2+[B]+[P].)*

> **Corollary G31.4 (no leaves anywhere).** In RES(b) ∧ (C6) every vertex has degree ≥ 2: a
> leaf w with neighbour v satisfies ecc(w) = 1 + ecc(v) ≥ 3 (rad = 2), while a(w) = 1 forces
> ecc(w) ≤ 2 by **Theorem G26**. *(Leaf identity asserted on 7 656 pool instances, 0 failures.)*

**Status of Claim Q6.1**: still **OPEN**, but no longer an open *class* — it is a bounded,
explicitly listed configuration problem (≤ 11 named slots, all of degree ≤ 7, 14 ≤ n ≤ 20,
at least one opposite slot occupied, B occupied whenever x or y is a hub). This is the
round-8 target, and it is the **only** thing left in pocket 1.

**Firewall statement (T13).** §19 is entirely the owner's own work, built on G13/G15/G21/G22
(all previously verified) and on §18's Theorem G26. Its ingredients are local configurations
checked as explicit labelled graphs (induced-P₅/P₆ tests and C₄ tests, section (E) of the
script); the mass budgets are arithmetic over the slot list. Nothing here is adopted from any
harvest. The window is **not** a search result and no graph search was run.

---
# §20 owner-w133 round 8 (2026-08-18, opus): **Claim Q6.1 is PROVED — pocket 1 closes**

*(All numbers in this section are produced by `problems/wowii/w133_r8_q61.py`,
log `problems/wowii/w133_r8_q61.out`, exit 0, TOTAL ASSERT FAILURES: 0, ~4 min.
Written after the script was run, per the standing red line.)*

Setting: **C ∈ RES(b) ∧ (C6)**, (u,z) a diameter pair. By **Corollary G26.1** the only
possible shape is a(u) = a(z) = 2, so **G13** applies and supplies the induced hexagon
**Z = (u, u₁, u₂, z, y, x)** at positions 0..5, with {x} a singleton component of N(u) and
{y} a singleton component of N(z). Claim Q6.1 says this branch is empty. **It is.**

## 20.1 **Lemma G32 (NEW — only ANTIPODAL slots survive)**

*(**Header corrected round 9 / Q19 defect 2**: the word "unconditional" was left over from the
false first version. **G32 and G32.1 are NOT unconditional** — both carry C4-free + P₆-free.
Only **G32′** is hypothesis-free beyond P₆-freeness. Read "unconditional" anywhere in §20 as
"unconditional relative to RES(b) ∧ (C6)"; the same correction applies to §20.2's
"they are now *equalities*, and unconditional" and to §20.1's numerics caption.)*

*(**CORRECTED in the same round** after the blind non-Qwen S3 pass — the first version of
G32 omitted the C4-free hypothesis and was **false as stated**. See §20.8 finding 1 for the
machine counterexamples. The corrected statement below is what every application uses, and
nothing downstream changes; the genuinely hypothesis-free half is split off as **G32′**.)*

> **Lemma G32′ (unconditional).** Let Z = (v₀,…,v₅) be an induced C₆ in a graph with **no
> induced P₆**. Then no vertex outside Z has **exactly two** Z-neighbours that are
> **consecutive**. *(No C4-freeness, no other hypothesis.)*

*Proof.* Suppose w ∉ Z has exactly the two Z-neighbours v_i, v_{i+1}. Deleting v_{i+1} from Z
leaves the induced path (v_i, v_{i−1}, v_{i−2}, v_{i−3}, v_{i−4}) — five vertices, i.e.
Z ∖ {v_{i+1}} since v_{i−4} = v_{i+2}, with endpoints v_i and v_{i+2} — and w is adjacent to
v_i only among them (its other Z-neighbour v_{i+1} was deleted). Hence
**(w, v_i, v_{i−1}, v_{i−2}, v_{i−3}, v_{i−4}) is an induced P₆**. ∎

> **Lemma G32.** Let Z = (v₀,…,v₅) be an induced C₆ in a **C4-free** graph with **no induced
> P₆**. Then every vertex outside Z has 0 or 2 neighbours on Z, and **if 2, they are
> antipodal** (cyclic distance exactly 3). *This strengthens **G15(b)** from "cyclic distance
> 1 or 3" to "3", i.e. it kills every consecutive-pair slot.*

*Proof.* Let w ∉ Z. **(i) |N(w) ∩ Z| ≠ 1**: that is G15(a)'s own argument (deleting the
successor of the unique Z-neighbour leaves an induced P₅ that w extends to a P₆).
**(ii) |N(w) ∩ Z| ≤ 2**: every 3-subset of a hexagon contains a pair at cyclic distance 2
(checked: the list of distance-2-free 3-subsets is empty), and such a pair has the vertex
between them *and* w as two common neighbours — a C₄. **(iii)** cyclic distance 2 is excluded
by the same C₄ (this is G15(b)); **cyclic distance 1 is excluded by G32′**. ∎

**Upstream note (imported defect, repaired here).** §14.2's written proof of **G15(a)** only
kills the case "exactly one Z-neighbour"; it never addresses "≥ 3". Step (ii) above is the
missing line, and it is pure C4-freeness — which G15 assumes anyway. **G15(a) is true as
stated; its proof was incomplete.** Flagged for the §14 auditor and for Lean.

> **Corollary G32.1 (mass identity).** In a C4-free P₆-free graph with an induced C₆,
> **d(v_i) = 2 + [the (v_i,v_{i+3}) slot is occupied]** and **N(v_i) is independent**
> (t(v_i) = 0: v_{i−1} ≁ v_{i+1} at cyclic distance 2, and the antipodal slot vertex is
> adjacent to neither), so **a(v_i) = d(v_i) = 2 + [the (v_i,v_{i+3}) slot is occupied]**.
> *(Wording corrected per §20.8: "triangle-free" is not enough — N(v) = P₃ is triangle-free
> with a = 2 < 3 = d. What the identity a = d − t needs here is t = 0.)*

*Numerics (non-vacuous, unconditional):* over the exhaustive C4-free table on 6 ≤ n ≤ 7
(111 508 connected graphs) plus 47 explicit/greedy carriers, restricted to the P₆-free ones
carrying an induced C₆: **1 330 hexagons, 1 300 off-hexagon vertices classified, 15 960 mass
identities — 0 failures.** (Ten hexagons carry two occupied antipodal slots simultaneously,
so the identity is tested non-vacuously in the occupied case as well.)

## 20.2 **Lemma G33 (the Q6.1 frame collapses to two slots)**

Apply G32 to the G13 hexagon. The nine a-priori slots of **G21** are
(u,u₁)=u₁′, (u₁,u₂)=A, (u₂,z)=u₂′, (z,y), (y,x)=B, (x,u), (u,z), (u₁,y)=P, (u₂,x)=Q.

> **Lemma G33.** In RES(b) ∧ (C6): **u₁′, u₂′, A and B do not exist**, and neither do the
> (z,y),(x,u),(u,z) slots. Consequently
> **N(u) = {u₁, x}, N(z) = {u₂, y}, d(u) = d(z) = 2**, and
> **V(C) = Z ⊔ {P?} ⊔ {Q?} ⊔ W_0**, where W_0 := the vertices with no Z-neighbour.
> Moreover **every w ∈ W_0 is at distance 3 from both u and z**, hence ecc(w) = 3, hence by
> **(R3b)** a(w) ≤ 2 and by **Theorem G26** a(w) = 2: **no vertex of W_0 is a hub**, and in
> particular **G21(iv)'s slot h₀ is empty**.

*Proof.* (u,z) is impossible (d = 3); (x,u) and (z,y) are impossible because {x}, {y} are
singleton components of N(u), N(z) (G13). u₁′, u₂′, A, B are the four consecutive-pair slots
of the hexagon and die by **G32**; explicitly the four induced P₆'s are
> **(u₁′, u, x, y, z, u₂)**, **(u₂′, z, y, x, u, u₁)**, **(A, u₁, u, x, y, z)**, **(B, x, u, u₁, u₂, z)**.
Since N(u) ⊆ Z, a vertex with no Z-neighbour is at distance ≥ 2 from u with no common
neighbour, i.e. at distance 3; same at z. ∎

*Numerics:* over **176** C4-free frames "hexagon + one consecutive-pair slot + an arbitrary
edge pattern on the other five slots", the named witness is an induced P₆ **every time**
(and `has_induced_pk(·,6)` confirms P₆-freeness fails), 0 failures.

**This supersedes most of §19.** G27 (h₀), G28 (partners) and G29 are now **vacuous**: their
subjects u₁′, u₂′, A, B, h₀ do not exist. *(**Corrected round 9 / Q19 defect 3**: **G30 is NOT
vacuous** — its subject is **P**, which may exist. G30 is **superseded**, not emptied: its
conclusion |W_P| ≤ 3, d(P) ≤ 7 is strictly weaker than **G34(c)**'s |W_P| ≤ 1, d(P) ≤ 4. Only
the *apexes* used inside G30's proof are gone.)* G31's
four identities a(u₁) = 2+[P], a(u₂) = 2+[Q], a(x) = 2+[Q], a(y) = 2+[P] survive and are
re-proved here as **Corollary G32.1** (they are now *equalities*, and unconditional).
No §19 statement is *wrong*; the round-8 route simply makes §19.1–§19.4 unnecessary.

## 20.3 **Lemma G34 (a(P) ≤ 3)**

> **Lemma G34.** In RES(b) ∧ (C6), write W_P := N(P) ∩ W_0. Then
> **(a)** for every w ∈ W_P, **N(w) ⊆ {P, Q} ∪ W_P**;
> **(b)** every w ∈ W_P is adjacent to Q (so W_P ≠ ∅ forces Q to exist);
> **(c)** **|W_P| ≤ 1**, hence **d(P) ≤ 4** and **a(P) ≤ 3**. Symmetrically **a(Q) ≤ 3**.

*Proof.* **(a)** (w, P, u₁, u, x) is an induced P₅ (w has no Z-neighbour; P ≁ u, x since
P's only Z-neighbours are u₁, y; u₁ ≁ x). By (C6) no induced P₆ extends it, so every
v ∈ N(w)∖{P} is adjacent to one of P, u₁, u, x. Since v ∉ Z (w has no Z-neighbour),
v ~ P puts v in W_P ∪ {Q}, v ~ u₁ puts v in {P} (A is gone), v ~ u is impossible
(N(u) ⊆ Z), and v ~ x puts v in {Q} (B is gone). **(b)** If w ≁ Q then N(w) ⊆ {P, w′} with
w′ ∈ W_P ⊆ N(P) — here |N(w) ∩ W_P| ≤ 1, since two W_P-neighbours of w would be two common
neighbours of w and P, a C₄ — so N(w) is a clique and **a(w) = 1**, contradicting a(w) = 2
(G33, via Theorem G26). **(c)** Two vertices of W_P would be two common neighbours of P and Q: a C₄.
Then N(P) = {u₁, y} ⊔ ({Q} ∪ W_P) with u₁ ≁ y (antipodal on an induced C₆), u₁, y adjacent
to nothing else in N(P), and Q ~ w; so a(P) = 2 + α({Q?}∪W_P) = 2 + 1 = 3 at most. ∎

## 20.4 **Theorem G35 (NEW — Claim Q6.1 is TRUE; RES(b) ∧ (C6) = ∅)**

> **Theorem G35.** **RES(b) ∧ (C6) is empty.** Equivalently: every C4-free connected graph
> with rad = 2, diam = 3, l > 3 and (R3b) contains an induced P₆.

*Proof.* Suppose C ∈ RES(b) ∧ (C6) and set up the frame above. By **G33** every hub lies in
{u₁, u₂, x, y, P, Q} (u and z have a = 2; W_0 carries no hub; u₁′,u₂′,A,B,h₀ do not exist).
By **G32.1** and **G34** the hub masses obey
> a(u₁)−2 = [P], a(u₂)−2 = [Q], a(x)−2 = [Q], a(y)−2 = [P], a(P)−2 ≤ 1, a(Q)−2 ≤ 1,

so **Σ_{h∈H}(a(h)−2) ≤ 3[P] + 3[Q] ≤ 6**. But l(C) > 3 with a ≤ 2 off H gives (\*\*)
**Σ_{h∈H}(a(h)−2) > n**, and n ≥ |Z| = 6, so the mass must be ≥ 7. Contradiction. ∎

*(The margin is not thin: |H| ≥ 6 (G18.1) forces all six candidate slots to be hubs, hence
both P and Q to exist, hence [P] = [Q] = 1, n ≥ 8 and — by G18.1's own arithmetic — a required
mass of ≥ 9 against a cap of exactly 6. **The earlier appeal here to "n ≥ 14 by §15.5" is
WITHDRAWN**: its backing log `w133_gplus_n13.out` reports `level n=13: classes=0` and
`L3-CENSUS: l>=3 graphs=622`, neither of which states "no C4-free graph with l > 3 exists for
n ≤ 13". The import is unconfirmed and is **not load-bearing** — n ≥ |Z| = 6 suffices. Flagged
for whoever owns §15.5.)*

> **Remark G35.2 (a second, independent kill: n ≤ 9).** The mass budget is a heavier hammer
> than necessary. By **G33**, V(C) = Z ⊔ {P?} ⊔ {Q?} ⊔ W_0 and N(u) = {u₁, x} ⊆ Z. For w ∈ W_0,
> d(w,u) = 3, so a shortest w–u path is w–a–b–u with b ∈ {u₁,x} and a ∈ N(u₁) ∪ N(x) =
> {u,u₂,P} ∪ {u,y,Q}; a ~ w forces a ∉ Z, i.e. **a ∈ {P,Q}**. So W_0 = W_P ∪ W_Q, and by
> **G34(b)** W_P ⊆ W_Q and W_Q ⊆ W_P, hence **W_0 = W_P = W_Q and |W_0| ≤ 1**. Therefore
> **n = 6 + [P] + [Q] + |W_0| ≤ 9**. *(Owed to the blind §20 judge; see §20.8.)*
>
> **KILL-RIDER RETRACTED (round 9 / Q19 defect 1, owner-confirmed).** The original rider —
> "this kills the branch against *any* n ≥ 10 input and is immune to every doubt about (\*\*)"
> — **does not execute and is hereby withdrawn.** No n ≥ 10 input survives in the certified
> corpus: §15.5's n ≥ 14 was **withdrawn in the same round 8** (§20.8 item 3), and the only
> live lower bounds are n ≥ |Z| = 6 and, via G18.1's |H| ≥ 6 ⟹ [P] = [Q] = 1, **n ≥ 8**.
> Against G35.2's n ≤ 9 that leaves n ∈ {8,9} — **consistent, not contradictory**. G35.2 is a
> true structural bound (n ≤ 9) with **no second kill attached**; §20.8 items 3 and 4 were
> mutually undercutting and neither judge nor planner noticed. **Theorem G35 is unaffected**:
> its proof is the mass budget alone, which never used n ≥ 10.
> **SECOND KILL REINSTATED, in the correct form (round 9 slice 2; `w133_r9_frame_l.py` →
> `.out`, exit 0).** The route is the finite-frame check the (D)-census was one line away from:
> by **G33** every C ∈ RES(b) ∧ (C6) has V = Z ⊔ {P?} ⊔ {Q?} ⊔ W_0, and by G35.2 |W_0| ≤ 1, so the
> enumeration over |W_0| ≤ 3 with all edge patterns is **exhaustive** for the class. Re-running it
> with **l computed** reproduces exactly the same **5** admissible frames and gives
> > (P,Q,|W_0|=1): n = 9, Σa = 24, **l = 8/3**; (P,Q): n = 8, l = 2.5; (P) and (Q): n = 7,
> > l = 16/7; (none): n = 6, l = 2.
> **max l = 8/3 < 3**, while RES(b) demands **l > 3**. Contradiction. ∎
> **Scope of the independence, stated exactly**: this kill uses **l > 3 directly and never
> (\*\*)**, so it *is* immune to any doubt about the mass inequality — which was G35.2's whole
> point. It is **not** independent of §18 (the a(w) = 2 filter is Cor G26.1 + G26), and nothing
> in §20 is. So: **two kills of the branch, both §18-dependent, one (\*\*)-dependent and one
> not** — which is the accurate form of the round-8 "dies twice over" claim.

> **Corollary G35.1 (POCKET 1, r = 3 LAYER, IS CLOSED).** Combining with **Theorem G26**
> (every distance-3 pair in RES(b) ∧ (C6) has both a-values 2, so G13 always applies):
> **C ∈ RES(b) ⟹ path(C) ≥ 6.** With §14.3 (rad(C) = 2, diam(C) = 3) and **Lemma G16**
> ((R3b) holds in the core), the **r = 3 layer of pocket 1 has no residual left**:
> a minimal counterexample of radius 3 cannot exist. **Claim Q6.1 is PROVED**, by the
> owner's own argument — the Qwen artifacts (Q3, Q12-C) remain **not adopted** and their
> ΔS device remains refuted (§18.3).

## 20.5 Round-8 numerical summary

```
problems/wowii/w133_r8_q61.py -> w133_r8_q61.out   (exit 0, 0 assert failures, ~4 min)
  pool: 111 508 connected C4-free graphs on 6 <= n <= 7 (small-graph table, allowed)
        + 47 explicit/greedy carriers (HS, HS+leaf, ER_5/7(+leaf), Petersen,
          40 random maximal C4-free graphs on n = 9..15)
  (B) G32 + G32.1 on the P6-free members carrying an induced C6:
        1 330 hexagons; 1 300 off-hexagon vertices classified (0 or 2 nbrs,
        antipodal when 2); 15 960 mass identities a(v_i) = 2 + [antipodal slot];
        10 hexagons with BOTH antipodal slots occupied   => 0 failures
  (C) G33: 176 C4-free frames "hexagon + consecutive-pair slot + arbitrary edge
        pattern on the other five slots"; the named witness is an induced P6 in
        every one of them                                 => 0 failures
  (D) exhaustive frame enumeration Z + {P,Q} + <= 3 W_0-vertices, all edge patterns
        on the non-Z vertices, kept if C4-free/connected/P6-free and a(w) = 2 for
        every W_0-vertex (Cor G26.1): a(P),a(Q) <= 3 (3+3 instances), |W_P| <= 1,
        N(w) subset {P,Q} u W_P, and Sigma_H(a-2) <= 6 in every kept frame; the
        realised maximum is exactly 6 (both slots, |W_0| = 1, n = 9)
  (E) bounded flag sweep: max Sigma_H(a-2) = 6 < 7 <= required           => EMPTY
  (F) controls, first failing step named (T12): HS/ER_q/Petersen fail at diam = 2;
      HS+leaf, ER_q+leaf fail at (C6) (they contain an induced P6); rand0 at rad = 3
```

**Firewall statement (T13).** §20 is entirely the owner's own work. G32 and G32.1 are
**unconditional** and were tested outside RES(b) (which is empty in every sample) on real
C4-free P₆-free graphs. G33/G34/G35 are RES(b)-internal and therefore untested as wholes —
flagged provisional exactly like G21/G24/G26 — but their *local* content (the four witness
P₆'s, the P₅ of G34(a), the slot arithmetic) is machine-checked on explicit frames.
**Dependency note for S3 (CORRECTED per §20.8 finding 2 — the earlier version of this
sentence, "G34(b) is the only place where Theorem G26 is used", was FALSE).** §20 depends on
§18 in **three** places, all load-bearing:
(1) **Corollary G26.1** in the opening line, to force a(u) = a(z) = 2 — without it G13 does
not apply and §20 has no hexagon and no frame at all;
(2) **Theorem G26** inside **G33**, to upgrade a(w) ≤ 2 (which (R3b) already gives) to
a(w) = 2;
(3) **G34(b)**, which consumes that upgrade to rule out a(w) = 1.
**If §18 falls, §20 falls entirely.** The dependency is acyclic (G26 is proved in §18 without
§19/§20), and §20 uses **nothing** from §19. Machine evidence that (2)/(3) are not decorative:
drop "a(w) = 2" and a(P) reaches **6** (occ = {P}, |W_P| = 4, n = 11), so G34's cap is a G26
artefact, not a C4-free artefact.
No SAT; the only sweeps are the n ≤ 7 labelled table and bounded frame enumerations.

## 20.6 Status update (supersedes §18.5/§19)

* **Claim Q6.1 is PROVED (Theorem G35)** — the a(u)=a(z)=2 branch of RES(b) ∧ (C6) is empty.
  With **Theorem G26** this gives **RES(b) ∧ (C6) = ∅**, i.e. **C ∈ RES(b) ⟹ path(C) ≥ 6**.
* **Pocket 1's r = 3 layer is CLOSED** (Corollary G35.1). The §19 window 14 ≤ n ≤ 20 is
  closed by proof, not by search; §19.1–§19.4 (G27–G30) become **vacuous** and §19.5's
  identities are re-proved unconditionally as G32.1.
* **New unconditional lemma G32** (+ G32.1) — a clean, reusable, P₆-free/C₆ rigidity fact
  that is strictly stronger than G15(b) and is the engine of the whole collapse.
* **Owed before PROVED promotion**: the non-Qwen adversarial pass on G25/G26 **and now on
  G32–G35** (dispatched this round), plus the queued cross-model pass on the G12.1 patch.
  **[PAID for the Q6.1 gate — see §22 (round 9 slice 3):** both passes returned and
  adjudicated (§20.7/§20.8), the diff-scoped G-diff pass Q19 passed (§20.9), planner
  confirmed 08-18 17:56 CDT (`orchestration/tasks/w133_r9.md`); PROVED is marked in the
  registry, §22. The G12.1 cross-model pass is Theorem G12's own separate ledger item,
  still queued, unchanged by this marking.**]**
* **Still open**: **(RP-D) for r ≥ 4** (= A7 integer version; G12 is the D = 2 case) and
  **pocket 2** (⌊l⌋ ≥ 4). Unchanged by this round.
* **Red lines**: no SAT; only the n ≤ 7 labelled table and bounded frame enumerations;
  every assertion run before being written; exit 0; controls audited with T12 naming.

## 20.7 Adjudication of the non-Qwen S3 judge A (§18 G25/G26 + §19 G27–G31)

*(Judge A: independent opus referee, refute-first, Qwen-isolated. Its own pool was **every**
connected C4-free graph on n ≤ 10 — 4 448 graphs, class counts 89/186/740/3389 for n ≤ 7/8/9/10,
which independently reproduce the draft's counts — plus Petersen, HS, ER_3/5/7/11 and variants,
24 random maximal C4-free graphs; ~90 000 assertions, 0 failures. Owner's machine record of the
adopted items: `problems/wowii/w133_r8_adjudicate.py` → `.out`, exit 0, 0 failures.)*

**Verdict received: §18 CLEAN (no statement false, no step breakable); §19 GAP×3, none false.**

1. **§18 stands.** All ten joints — G25(a)'s chordless C₄, the (a)→(b)→(c)→(d) ordering, G25(c)'s
   injection, G25(d)'s ten-pair P₅ audit, G26's mass algebra, the η-sweep's uniqueness, the
   δ_b = 4 pinning, |D| = 16 / n = 27, and the ⌈d/2⌉ endgame — were re-derived independently and
   machine-asserted. **Nothing is retracted.** Judge A also confirmed the C4-free convention is
   load-bearing and correctly chosen: **G23(a) fails under an induced-only reading of C₄-free**
   (two extra common neighbours w,w′ of p,q give p–w–q–w′ with the chord pq), so the "no two
   vertices have two common neighbours" convention of §1/§17.3 must stay. Noted for Lean.
2. **ADOPTED — finding 3 (label + implicit link).** G25(d) is **not** unconditional: its proof
   consumes (R3b) (for ecc(h) = 2) and **G24(b)** (for β_q ≥ 1), and G24(b) is RES(b)-internal.
   The header of §18.1 and the §18.4 firewall sentence are corrected above; the 20 623 instances
   quoted for (d) test only its induced-P₅. Likewise β_p, β_q ≥ 1 (G24(b)) is what makes
   a(p) − 2 = β_p − 1 − e_p ≥ 0 in G26 step (1) — verified for β_p = 1..8 with e_p ≤ ⌊β_p/2⌋.
   **No mathematics changes.**
3. **ADOPTED — finding 1, and it is a genuine improvement to §20.** Judge A found that
   **P ∼ A, P ∼ B, P ∼ Q, Q ∼ A, Q ∼ B each force a C₄ outright**, with witnesses
   (u₁,A) share {u₂,P} · (y,B) share {x,P} · **(u₁,Q) share {u₂,P}** · (u₁,Q) share {u₂,A} ·
   (y,Q) share {x,B}. Two consequences:
   * a one-line C₄ route replaces §20's induced-P₆ witnesses for four of the five pairs
     (§20.2's P₆'s remain correct; the C₄ route is simply shorter), and
   * **P ≁ Q is NEW** — §20.3 had left it open. Hence **N(P) = {u₁, y} ⊔ W_P is edge-free**
     (u₁ ≁ y is antipodal on an induced C₆; W_0 has no Z-neighbour), so **a(P) = d(P) = 2 + |W_P|
     ≤ 3** by the *same* |W_P| ≤ 1. The cap of **Lemma G34 is unchanged**, its proof is shorter,
     and **Theorem G35's budget of 6 is untouched.**
4. **NOT superseded — A ≁ B keeps its P₆ proof.** Judge A's C₄ device does **not** reach the pair
   (A,B): the frame with A ∼ B added is C₄-free (machine-checked). The induced P₆
   **(u, x, B, A, u₂, z)** is therefore load-bearing for that one pair. *(Citation corrected
   per §20.8: this P₆ is **new here in §20.7** — §20.2 does not contain it and makes no A ≁ B
   claim; the earlier "§20.2's induced P₆" was a spurious back-reference.)* Moot inside the
   Q6.1 frame, where G33 empties A and B, but it survives as a general fact.
5. **§19's three gaps: CONFIRMED and MOOT.** (i) G29's second sentence ("Q occupied ⟹ A and B
   empty") has no proof — the C₄ it needs requires P ∼ A ∧ P ∼ Q, which only d(P) ≥ 6 supplies;
   and by item 3 those adjacencies are C₄'s anyway, so G29's first sentence has an unreachable
   conclusion. (ii) **G30's |W_P| ≤ 3 is unproved**: the body yields ≤ 4 and the closing
   parenthetical is a non-sequitur (G28 bars **P** ∼ u₁′, not **w** ∼ u₁′). Judge A's repair is
   the owner's own round-8 repair, reached independently: the apexes u₁′, A, B are each killed by
   a forced C₄ at w, leaving only Q, so **|W_0| ≤ 1**. (iii) G31.3 hides [P] = 1 in its d(Q) ≤ 5.
   **All three are moot**: §20's G33 empties u₁′, u₂′, A, B and h₀, so G27–G30 have no subjects.
   No §19 statement is false; §19 was simply far weaker than its own hypotheses allowed.
6. **Independent corroboration of §20's engine — with an honesty caveat (T13).** Judge A
   independently derived §20's **Lemma G32** (it names it "G15(d)"), with the same four witness
   P₆'s and the same collapse to **Σ_H(a−2) ≤ 6 < n**, and machine-verified it two ways,
   including a falsification sweep over every P₆-free connected C4-free graph with n ≤ 10
   (23 induced-C₆ instances, 49 outside vertices with exactly two Z-neighbours, **all 49
   antipodal**, 0 at cyclic distance 1 or 2). **Caveat: this is not fully independent.** The
   owner's rescinding message told judge A that "a later result implies the §19 slots u₁′, u₂′,
   A, B may be non-existent" — a hint, even though the judge reports having derived the fact
   before that message landed and re-derived everything from scratch. **Weight it as strong
   corroboration of the arithmetic and the witnesses, not as an independent discovery.** The
   §20 pass by the genuinely blind judge B is still owed and is the real gate.
7. **Methodology finding (adopted, worth the whole round).** Judge A's answer to "why did §19
   not see G32": **§17.4's Corollary G22.1 had already constructed exactly the right P₅'s** —
   (u₁′,u,x,y,z), (A,u₁,u,x,y), (B,y,z,u₂,u₁) — and applied G22 to bound the *endpoint's degree*,
   **never noticing that each extends at its far end (by u₂, z, u) to an induced P₆**. One
   habit fixes it: *whenever a P₅ is built to feed a degree bound, first ask whether it extends
   to a P₆ and kills the vertex outright.* Queued for `notes/methodology.md`.

## 20.8 Adjudication of the blind non-Qwen S3 judge B (§20 G32–G35)

*(Judge B: independent opus referee, refute-first, Qwen-isolated **and §20-blind at dispatch**
— it received no hint from the owner, unlike judge A (§20.7 item 6). Its own scripts
`w133_r8_judge20_{g32,frame,deep,final}.py`; its sweeps are all graphs on ≤ 9 vertices
containing a fixed induced C₆ plus bounded frame censuses. Owner's re-verification of every
adopted item is folded into `problems/wowii/w133_r8_q61.py` section (B2), exit 0, 0 failures.)*

**Verdict received: GAP — two substantive, four write-up. NOT REFUTED: Theorem G35 and
Corollary G35.1 stand.** Every finding is **ADOPTED**; all repairs are applied above.

1. **ADOPTED, and it is a REAL DEFECT: Lemma G32 was FALSE as stated.** The first version
   omitted **C4-freeness**. Machine counterexamples, all re-verified by the owner:
   **C₆ + w with N(w) = {v₀,v₂}** is P₆-free with two Z-neighbours at cyclic distance 2; and
   **N(w) = {v₀,v₁,v₂}**, {v₀,v₂,v₄}, {v₀,v₁,v₃} are P₆-free with three. Judge B located the
   root cause exactly: §20.1 said *"the 0-or-2 part is G15(a)"*, but **G15 is stated for
   C4-free graphs, and G15(a)'s own written proof only kills the case "exactly 1"** — it never
   addresses ≥ 3. Both the "≥ 3" exclusion and the "distance 2" exclusion are pure
   C4-freeness, silently inherited. §20.1 is rewritten: **G32′** (the genuinely
   hypothesis-free half: *exactly two consecutive Z-neighbours ⟹ induced P₆*) is split off,
   **G32** now carries C4-free, and the missing "≥ 3" line is supplied — with an **upstream
   flag on §14.2's G15(a)**, whose statement is true but whose proof is incomplete.
   **Damage downstream: nil** — every application site (G32.1, G33, all of RES(b)) is C4-free.
   Owner's re-verification: 4 counterexamples reproduced; **G32′ holds over 129 frames with an
   exactly-consecutive pair and no C4-free filter (0 P₆-free)**; **G32 holds over all
   2 105 408 frames on C₆ + ≤ 3 vertices (10 136 C4-free), 0 violations**.
   *The word "unconditional" in the old §20.1 header and §20.5 firewall was unearned, and the
   script's section (B) filtered to C4-free — i.e. it never tested the statement as written.
   Both are corrected; section (B)'s comment now says which statement it tests.*
2. **ADOPTED: the dependency note was FALSE.** §20.5 claimed *"G34(b) is the only place where
   Theorem G26 is used"*. §20 in fact uses §18 **three** times: **Cor G26.1** for the frame
   itself (without it there is no hexagon), **G26 in G33** for the a(w) ≤ 2 → a(w) = 2 upgrade,
   and **G34(b)** for the consumption. Rewritten above, with the blunt sentence **"if §18 falls,
   §20 falls entirely"** — which is what a reader needs to scope the blast radius. Judge B also
   showed the dependency is not decorative: drop "a(w) = 2" and **a(P) reaches 6** (occ = {P},
   |W_P| = 4, n = 11), so G34's cap is a **G26 artefact, not a C4-free artefact**.
3. **ADOPTED: the n ≥ 14 import is WITHDRAWN.** §15.5's "no C4-free graph with l > 3 exists for
   n ≤ 13" is not established by its own log (`level n=13: classes=0` is about residual classes;
   `L3-CENSUS: l>=3 graphs=622` shows such graphs *do* exist at n ≤ 13). Owner grepped the log
   and confirms judge B: **the import is unverified**. It is **not load-bearing** (n ≥ |Z| = 6
   suffices), so G35 is unaffected; the "margin is not thin" parenthetical now leans on
   G18.1 instead. Flagged for whoever owns §15.5.
4. **ADOPTED, and it is a gift: Remark G35.2, the n ≤ 9 endgame.** diam = 3 with N(u) = {u₁,x}
   forces every W_0-vertex adjacent to P or Q; G34(b) then gives W_0 = W_P = W_Q with |W_0| ≤ 1,
   so **n ≤ 9 unconditionally**. Shorter than the mass budget, **immune to any doubt about
   (\*\*)**, and a second independent kill. Added after G34 and asserted in the script
   (5/5 admissible frames, max n = 9).
5. **ADOPTED (minor):** G34(b) now states the missing one-liner |N(w) ∩ W_P| ≤ 1; G32.1's
   "N(v_i) is triangle-free" is replaced by "**t(v_i) = 0, N(v_i) is independent**" (a P₃ is
   triangle-free with a = 2 < 3 = d, so the old wording was a non-sequitur); §20.7 item 4's
   back-reference to "§20.2's induced P₆ (u,x,B,A,u₂,z)" is corrected — **that P₆ is new in
   §20.7**, §20.2 never claimed A ≁ B.
6. **ADOPTED: six dead assertion branches deleted from the script.** Section (D) builds
   occ ⊆ {P,Q}, so `if A_ in occ` / `if B_ in occ` could never fire, yet the log printed
   `A-B: 0`, `a(A)<=2: 0`, `|W_A|<=1: 0` etc. as though tested-and-passed. Removed.
7. **Judge B's positive verifications** (recorded, not adopted — they are confirmations):
   all four G33 witness P₆s checked relation-by-relation (4 × (5 edges + 10 non-edges), **none
   assumed**), robust to arbitrary edge patterns on the other slots; the V(C) partition
   exhaustive; the distance-3 argument for W_0 exactly right (0 violations over its 39 admissible
   frames); G34(a)'s P₅ and case list exhaustive; the hub list H ⊆ {u₁,u₂,x,y,P,Q} complete;
   the budget recomputed from scratch (mass ≤ 0/3/3/6 vs n ≥ 6/7/7/8, contradiction in all four
   cases), (\*\*) quoted correctly, G18.1's |H| ≥ 6 re-derived; **zero §19 dependency**; and an
   independent reproduction of the script's census — exactly **39** frames of the shape
   Z ⊔ {P?,Q?} ⊔ W_0 with |W_0| ≤ 4, of which exactly **5** survive the a(w) = 2 filter, matching
   "kept: 5" and the maximum Σ_H(a−2) = 6 at (P,Q,|W_0| = 1,n = 9). **The filter is legitimate,
   not over-filtering.**
8. **Vacuity, flagged (not an error).** Every admissible frame has n ≤ 11 and l ≤ 2.67, so the
   class dies far below the mass budget — consistent with RES(b) being empty, and the reason
   G33/G34/G35 remain **untestable as wholes**. Their local content is machine-checked.
9. **No factual disagreement between §19 and §20** — independently confirmed by judge B, which
   also observed that §19 + §20 compose into an even shorter contradiction (G31.3 + G32 give
   "x is never a hub", so [Q] = 0, symmetrically [P] = 0, so H = ∅ against |H| ≥ 6). Judge B
   reached §20.7 item 7's methodology finding independently: §17.4 built the right P₅s and only
   ever asked for endpoint degrees, never whether they extend to a P₆.

> **Net effect on the round's claim.** Two judges, one hinted and one blind, both failed to
> break Theorem G35 and both independently reproduced its arithmetic. One statement (G32) was
> genuinely false as written and is repaired with its hypothesis restored; one firewall
> sentence was false and is rewritten; one numerical import is withdrawn as unverified; and the
> branch dies by the mass budget (≤ 6 < n).
> ~~and the branch now dies **twice over** … by **G35.2's n ≤ 9**~~ — **STRUCK round 9 (Q19
> defect 1)**: item 3 (withdrawing n ≥ 14) destroyed the only input item 4's second kill could
> ever have consumed. The redundancy claimed here **never existed**; see the retracted
> kill-rider at §20.4 and §20.9. **One kill, not two.**
> **Claim Q6.1 stands as PROVED-pending-planner; §14.2 (G15(a)'s proof) and §15.5 (the n ≥ 14
> claim) inherit flagged defects that are NOT this round's to close.**
> **[SUPERSEDED round 9 slice 3: both inherited defects were closed in slice 1 (§14.2
> completion, §15.5 withdrawal+replacement), the planner confirmed the promotion 08-18
> 17:56 CDT, and the PROVED marking is executed in the registry — §22.]**

## 20.9 Adjudication of the Q19 G-diff pass (round 9 slice 2, owner-w133)

Source: `problems/wowii/w133_S3_GDIFF_qwen.md` (Qwen3.8-Max, one fresh conversation, brief
`prompts/w133_S3_GDIFF.md`). **Verdict as returned: PARTIAL, `MATHEMATICS DEFECT FOUND: NO`,
5 defects, all self-labelled BOOKKEEPING.**

**Verdict-quality audit (the pass is judged before its findings are).** The mandatory
statement-hypothesis audit table is **PRESENT** and **covers all 11 named statements**
(G32′, G32, G32.1, G33, G34(a)(b)(c), G35, G35.1, G35.2, G15(a)(b)(c) — 13 sub-items, the
harvest's "15" is a miscount, not a shortfall). Both directions were exercised: two
NARROWER-than-proof strengthening opportunities (G34(a), G15(b)) and one WIDER verdict, which
is the same finding as its defect 1 — i.e. **the probe caught its own most substantive item
independently of the prose review, which is what the probe is for.** The three repair-species
probes and the T12 counterfactual section are present. Both non-executing lemmas it names are
correct. **Firewall: the pass is Qwen, the material under review is owner-authored and
Qwen-free; nothing here is adopted as an argument — only as defect reports the owner
reproduced from the primary text.**

**Owner's reproduce-or-refute on all five, plus one the pass missed:**

1. **Defect 1 (G35.2's "second independent kill") — REPRODUCED, and it is the round's real
   find.** Confirmed from the primary text: §20.8 item 3 withdrew n ≥ 14 and item 4 asserted a
   kill that needs n ≥ 10, **in the same adjudication block**. Live bounds are n ≥ 6 and (via
   G18.1) n ≥ 8, versus G35.2's n ≤ 9 ⟹ n ∈ {8,9}, no contradiction. **Repair landed**: the
   kill-rider is retracted at §20.4 and struck in §20.8's net-effect paragraph. Severity is
   correctly BOOKKEEPING **for the promotion gate** (Theorem G35's proof is the mass budget and
   never touched n ≥ 10), but it is **not** cosmetic: round 8's "the branch dies twice over"
   and the planner's "the right redundancy" are both **false as recorded** and now corrected.
2. **Defect 2 ("unconditional" wording) — REPRODUCED.** §20.1's header said "unconditional"
   while G32 carries C4-free + P₆-free. Header rewritten; the reading rule ("unconditional
   relative to RES(b) ∧ (C6)") is stated once and applies to §20.2's equalities sentence too.
3. **Defect 3 (§20.2's vacuity wording) — REPRODUCED, and sharpened.** G30's subject is **P**,
   which survives; G30 is **superseded by G34(c)** (|W_P| ≤ 1 beats |W_P| ≤ 3), not vacuous.
   Only G27/G28/G29 are vacuous. Landed.
4. **Defect 4 (§14.2's 11-site sweep) — REPRODUCED.** §19.5's G31 uses G15(a) **indirectly
   through G15(c)**; the sweep counted direct uses only. Table corrected to 12 sites; the site
   is inside RES(b) (C4-free ✓) and MOOT. **Methodology**: usage sweeps must follow indirect
   citation through sibling clauses.
5. **Defect 5 (§15.5's downstream table) — REPRODUCED.** **Cor G31.3** cites n ≥ 14 and was
   missing; worse, unlike the other five rows its *conclusion* (B is occupied) **dies** with the
   bound rather than surviving. Row added; MOOT because §19 is superseded. The table's own
   self-description ("every citation classified") was false and is now corrected.
6. **NEW — defect 6, MISSED by the pass, found by the owner.** §20.8 item 8 asserts "every
   admissible frame has n ≤ 11 and **l ≤ 2.67**". **No log line backs the l value**:
   `w133_r8_q61.py` section (D) prints frame count, the per-filter counts, `n<=9 (G35.2)` and
   the mass maximum — it **never computes l**. This violates the standing red line (assertions
   are run before they are written). It is not load-bearing (item 8 is a vacuity flag, not a
   step), **but it is exactly the computation that would reinstate G35.2's second kill** (see
   §20.4). **CLOSED in the same slice** (`problems/wowii/w133_r9_frame_l.py` → `.out`, exit 0):
   the enumeration reproduces the same **5** admissible frames and gives **max l = 8/3 ≈ 2.667**
   — which both **backs item 8's number** and **REINSTATES G35.2's second kill** as a
   finite-frame check using l > 3 directly and never (\*\*). Net: the pass's defect 1 was right
   that the rider as written never executed, and wrong only in supposing the repair needed new
   mathematics — it needed one line of arithmetic the script had already set up.

**Gate arithmetic (reported to the planner, NOT self-executed).** The pass answered the exact
question the gate watches — `MATHEMATICS DEFECT FOUND: NO` — on both named MATHEMATICS joints:
**G-M1** (the G32′/G32 split: all three steps re-derived with per-step control graphs, the
hypothesis attribution confirmed, and the usage sweep independently reproduced with no live
site lacking C4-free) and **G-M2** (§14.2's G15(a) completion: the arc argument re-derived,
the (a1)/(a2) attribution endorsed). The owner reproduced every defect the pass reported and
found one more; **all six are bookkeeping, none touches G32′, G32, G33, G34 or the mass budget
that proves G35.** Per the queue row's pre-stated arithmetic the promotion condition for
**Claim Q6.1 / Theorem G35** is satisfied. **The owner does not self-promote; the planner
confirms.** One thing the planner should note when confirming: the round-8 verdict's own
sentence about redundancy is among the items corrected (defect 1).
**[CONFIRMED by the planner 08-18 17:56 CDT (`orchestration/tasks/w133_r9.md`); the registry
marking is executed in §22 (round 9 slice 3).]**

---
# §21 owner-w133 round 9 slice 2: adjudication of the Q15 (r ≥ 4) and Q16 (pocket 2) harvests

*(Verification script `problems/wowii/w133_r9_controls.py` → `.out`, exit 0, **0 failures**,
run before this section was written. NO SAT: three explicit named constructions plus exact
induced-path DFS.)*

## 21.1 Q15 — (RP-D) for r ≥ 4 (`problems/wowii/w133_RPD_qwen.md`, PARTIAL)

**Line-by-line verdict, four claimed results:**

* **Lemma 1 (endpoint extension from a(v₀) ≥ 2)** — **TRUE, but NOT NEW.** It is the weak half
  of **Lemma G1** (§11), which already takes y from a second component of N(u_d) on a(≥2). The
  one detail Qwen supplies that G1 leaves implicit is worth keeping: *two independent
  neighbours of v₀ cannot both be adjacent to v₁* (they would be two common neighbours of
  v₀,v₁ ⟹ C₄), so a(v₀) ≥ 2 always yields x ≁ v₁. **Registered as independent confirmation of
  G1; nothing adopted.**
* **Lemma 2 (a vertex off a geodesic has ≤ 2 geodesic-neighbours, and consecutive if 2)** —
  **TRUE**, owner re-proved: distance ≥ 3 apart is killed by the geodesic, distance 2 by C₄,
  three neighbours contain a distance-2 pair. This is the **geodesic analogue of G15(b)** and
  the project did not have it stated stand-alone. **REGISTERED as a fact (owner-verified
  proof); consumes C4-free + geodesic only.**
* **Lemma 3 (leaf pruning raises S − 3n by exactly 1)** — **TRUE and ALREADY OWNED**: it is
  verbatim §12.5's peeling computation ("S 降 2、n 降 1、松弛 +1"). **Rediscovery; nothing
  adopted.**
* **The partial theorem** (C4-free + **triangle-free** + **δ ≥ 4** + diam D ≥ 3 ⟹ path ≥ D+4)
  — **TRUE; proof CORRECT AFTER ONE OWNER-SUPPLIED LINE; novelty NARROWER than claimed.**
  * The missing line is in the harvest's "at most 2 bad neighbours out of ≥ 3": it does not say
    why **v₁** is free. It is free, and cheaply: v₀ is already a common neighbour of x and v₁,
    so a second neighbour of x adjacent to v₁ closes a C₄ (x–v₀–v₁–y–x, with y ≁ v₀ by
    triangle-freeness). Hence bad ⊆ {the ≤1 common neighbour with v₂} ∪ {the ≤1 with v₃},
    and δ ≥ 4 leaves ≥ 3 candidates. Symmetrically at v_D every neighbour ≠ v_{D−1} is
    automatically non-adjacent to all of v₀..v_{D−1}, so the only bad z are the ≤1 adjacent to
    x and the ≤1 adjacent to y. **The construction closes.**
  * **Novelty audit (this is the tightness verdict).** Triangle-free + δ ≥ 4 ⟹ a(v) = d(v) ≥ 4
    for every v, so the hypotheses of **Lemma G14** (§13.4) hold outright — and for **d ≥ 5,
    G14 already gives the conclusion.** What Q15 actually adds is **the low end, D ∈ {3,4}**,
    where G14's proof breaks (it needs dist(w,y) ≥ d−3 ≥ 2). **So: Q15 = G14 pushed down to
    D = 3,4 at the price of triangle-free + δ ≥ 4.**
  * **Reach on the live class: NIL, and this is the useful part.** The residual carries a = 1
    vertices, leaves and triangle-leaves, and at r = 3 the diameter endpoints have
    **d(u) = d(z) = 2** (G33) — δ ≥ 4 fails everywhere it matters. The subcase is a genuine,
    non-vacuous theorem about a class disjoint from the residual.
* **Control audit — the pass's own T12 discipline FAILS one way.** Petersen's numbers are all
  reproduced exactly (C4-free ✓, diam 2 ✓, l = 3.0 ✓, **path = 5 exactly** ✓ by exhaustive
  induced-path search), and the "F2 does not execute" honesty is real. **But Petersen has
  δ = 3 and D = 2: it does not satisfy the delivered theorem's own hypotheses**, so the theorem
  arrived with **zero** instances witnessing it. Owner supplied one: the **PG(2,3) incidence
  graph** (n = 26, 4-regular, C4-free, triangle-free, rad = diam = 3, l = 4.0, induced path
  ≥ 9 ≥ D+4 = 7). **Registered as the standing positive control for this subcase.**
* **The named obstruction (degree-3 / triangular local case) is ACCEPTED as a diagnostic** and
  it agrees with the project's own history: every hard instance in this problem is low-a and
  triangle-rich. The failed charging argument (hub excess ⟹ spare directions) is reported as
  *attempted and not made rigorous*, which is the honest form; it matches §12.4's already-proved
  negative result about layered counting.

## 21.2 Q16 — pocket 2 / (G+k) at k = 2 (`problems/wowii/w133_Gplusk_qwen.md`,
OBSTRUCTION-IDENTIFIED)

* **(M3) Σ_{a≥3}(a−2) > 2n and (M4) Σ_{a≥4}(a−3) > n** — **TRUE**, owner re-derived both by the
  same two-line split (bound the low part by 2 resp. 3 per vertex). They consume **only l > 4**;
  the harvest's mention of "non-hubs have a ≤ 2 resp. ≤ 3" is not needed and would have been an
  unnecessary import. **REGISTERED (with the tighter attribution).**
* **rad ≤ 1 ⟹ l < 2** — **TRUE** (C4-free forces N(v) = matching + isolates; every non-centre
  vertex then has a = 1, giving l = (3t+2s)/(2t+s+1) < 2). So no radius-1 graph has l > 4.
  **REGISTERED as a base case; trivial but it is a real case-closure.**
* **"μ ≥ 4, rad ≥ 5 ⟹ path ≥ rad+4"** — **NOT NEW and correctly self-declared as not new**: it
  is **Lemma G14**'s stated corollary, supplied to the tab as F9. No credit, no defect.
* **The "3-capped periphery" obstruction — ACCEPTED as an accurate naming, not as a theorem.**
  Checked against G14's actual hypotheses: G14 needs x ∈ N(u₀) outside u₁'s matching-component
  **with a(x) ≥ 4**, and C4-freeness makes N(u₀) a matching-plus-isolates, so the usable side
  set can indeed be entirely low-a. **The obstruction is exactly the hypothesis a(x) ≥ 4 failing
  in a structured way, and naming it converts (G+k) at k=2 into one missing lemma:**
  > **(3CAP)** *C4-free, l > 4, rad ≥ 5 ⟹ some geodesic endpoint has a usable side-neighbour
  > with a ≥ 4.* — **OPEN; this is now pocket 2's single named target for rad ≥ 5.**
  The model's honest addendum stands: (M4) proves a ≥ 4 vertices exist **globally** but does not
  place one in a usable side position. Its local skeleton has l < 2, i.e. **it demonstrates the
  local pattern, not its global realisability under l > 4** — that gap is the experiment below.
* **STS(15) control — VERIFIED EXACTLY, and it is the harvest's most valuable deliverable.**
  Owner rebuilt it as the point/line incidence graph of PG(3,2) and confirmed **every** number:
  n = 50 (15 + 35), **C4-free**, a(point) = 7, a(block) = 3, Σa = 210, **l = 4.2 > 4**,
  **rad = 3** (all points ecc 3, all blocks ecc 4), **diam = 4**, **μ = 3**. The claimed induced
  path ≥ 9 is true but **weak — the true value is ≥ 12** (exact DFS, capped). Target inequality
  path ≥ rad+4 = 7 holds with a factor of margin. **ADOPTED into the fact base as the standing
  positive control for l > 4**, and it doubles as a **(RP-D) positive control at D = 4**
  (12 ≥ D+4 = 8), which pocket 1 also lacked. F9's non-execution here (μ = 3, rad = 3 < 5) is
  correctly reported.

## 21.3 Cross-tab shared-assumption sweep (both harvests, mandatory)

Both tabs rest on exactly one shared foundation: **F1** — in a C4-free graph G[N(v)] is a
matching plus isolates, hence a = d − t. That is owner-owned, proved, and true. **No shared
unproved assumption, no cross-contamination**: neither tab cites the other's claims, and
neither imports RES/RES(b) material. Both used Petersen and both correctly reported their key
fact failing there.

**One shared methodological defect, and it becomes a brief amendment.** *Both* tabs delivered
their headline under hypotheses that **no supplied instance satisfies** (Q15: δ ≥ 4 with D ≥ 3;
Q16: rad ≥ 5). The T12 protocol as written only demands a control on which a named fact
**fails**. **Amendment for every future brief: a delivered theorem must come with at least one
explicit instance satisfying its OWN hypotheses, or be marked VACUOUS-UNTESTED.** Q16 passes
this incidentally (STS(15) satisfies l > 4); Q15 did not, and the owner had to supply PG(2,3).

## 21.4 What each pocket needs next

* **Pocket 1, r ≥ 4 layer.** D = 2 is G12; D ≥ 5 with a(x) ≥ 4 is G14; **D = 3 is the first
  genuinely open case** and it is where the residual lives. Next decisive step: **extend G14
  down to d = 3 and d = 4 in the project's own currency (a-values, no triangle-freeness, no
  degree floor)** — Q15's route shows the low end is reachable, and its two collisions
  (w ~ y at d = 4, and the z-vs-{x,y} collisions at d = 3) are exactly the terms to pay for.
  Free ammunition already on the shelf: the a = 1-free reduction (§12.5 peeling + Cor G+1) lets
  one assume no leaves and no triangle-leaves.
* **Pocket 2 (⌊l⌋ ≥ 4).** Target is now **(3CAP)** for rad ≥ 5, plus radii 2, 3, 4 separately.
  The cheapest decisive experiment first: **is a 3-capped periphery globally realisable under
  l > 4 at all?** Probe the incidence families (PG(2,q), STS, generalized quadrangles) and
  greedy maximal C4-free graphs for one; if none exists, (3CAP) is likely provable from (M4)
  plus a local count, and if one exists it is a counterexample skeleton for (G+k).

---

# §22 owner-w133 round 9 slice 3 (2026-08-19): REGISTRY — Claim Q6.1 / Theorem G35 is **PROVED** (planner-confirmed)

**This section executes a registry action. It contains no new mathematics.**

* **Claim Q6.1 / Theorem G35: PROVED-pending-planner → PROVED.** The planner's confirmation is
  on record in `orchestration/tasks/w133_r9.md` (appended 08-18 17:56 CDT). The owner did not
  self-promote; this marking executes that confirmation.
* **Statement carried as PROVED**: **RES(b) ∧ (C6) = ∅** (Theorem G35, §20.4); hence
  **C ∈ RES(b) ⟹ path(C) ≥ 6** (Cor G35.1) and **pocket 1's r = 3 layer is CLOSED**.
* **Evidence chain (cited in full):**
  1. **Judge A** (non-Qwen, hinted; adjudicated §20.7): §18 (G25/G26) **CLEAN**; §19's three
     gaps confirmed and MOOT (subjects emptied by G33); two items adopted (G25(d) label fix,
     P ≁ Q).
  2. **Judge B** (non-Qwen, blind; adjudicated §20.8): verdict GAP-not-REFUTED; the one
     genuine defect (G32 stated without C4-freeness) repaired by the **G32′/G32 split**;
     G35's arithmetic independently reproduced; re-verified over 2 105 408 frames,
     0 violations.
  3. **G-diff pass Q19** (diff-scoped, Qwen-eligible because the diff is owner-authored and
     Qwen-free; adjudicated §20.9): **`MATHEMATICS DEFECT FOUND: NO` on both named MATH
     joints** — G-M1 (the G32′/G32 split incl. the 12-site C4-free usage sweep) and G-M2
     (§14.2's G15(a) completion). All six defects (five reported + owner-found defect 6) are
     **bookkeeping**; none touches G32′, G32, G33, G34 or the mass budget. Defect 6 closed by
     `problems/wowii/w133_r9_frame_l.py` (exit 0): 5 admissible frames, **max l = 8/3**.
* **Form of record (the accurate two-kill form, adopted per the 17:56 confirmation)**: the
  a(u)=a(z)=2 branch of RES(b) ∧ (C6) dies twice — by the **mass budget** (Σ_H(a−2) ≤ 6 < n,
  which uses (\*\*)) and by the **finite-frame check** (all 5 admissible frames have
  l ≤ 8/3 < 3, contradicting l(C) > 3 directly, never using (\*\*)). **Both kills are
  §18-dependent; exactly one is (\*\*)-dependent.** (Round 8's original "dies twice over"
  rider, struck at §20.8, is replaced by this accurate form — see §20.9 defect 6.)
* **Scope guard.** PROVED covers **Claim Q6.1 only**. Still open, NOT moved by this marking:
  **(RP-D) for r ≥ 4** (D = 3 is the first genuinely open case, §21.4) and **pocket 2**
  (⌊l⌋ ≥ 4, target (3CAP)). Conjecture 133 itself remains OPEN (§0 unchanged). Theorem G12's
  own outstanding item (the queued cross-model pass on the G12.1 patch) is a separate ledger
  entry, unchanged.
* Pointer annotations placed at §20.6 (the "owed before PROVED promotion" bullet), §20.8 (the
  "PROVED-pending-planner" net-effect line) and §20.9 (the gate-arithmetic paragraph).

---

# §23 owner-w133 round 10 (2026-08-19 02:1x–02:3x CDT): ADJUDICATION of Q28 (G14 low-d) and Q29 (3CAP)

**Script**: `problems/wowii/w133_r10_adjudicate.py` → `.out`, **exit 0, 0 failures**. No SAT.
Line-by-line reproduce-or-refute, both harvests, starting at the self-flagged joints.

## 23.1 Q28 (`problems/wowii/w133_G14low_qwen.md`, claimed SOLVED-BOTH) — DEFLATED to: d=4 PROVED + d=3 Case-1 PROVED + bare d=3 target REFUTED + F4-form d=3 Case-2 OPEN

1. **d = 4: proof CORRECT — owner re-derived every line.** Standard path (P₈) plus the
   alternative path z–u₀–x–w_y–y–u₄–u₃–u₂ when all three kills {y,u₂,u₃} hit distinct
   components; all 21 chord pairs re-verified by hand. **No F4, no a-value surcharge.**
   Registered as **Lemma G36** (statement = the Q28 target at d = 4). Status:
   **ADOPTED** **[PROMOTED 08-22 01:01 CDT, §26.1 — was ADOPTED-pending-S3, planner-confirmed]**
   (Qwen-origin argument, owner-re-proved; ~~non-Qwen judge owed~~ — satisfied, §25/§26.1).
2. **d = 3 Case 1 (some usable far-side y with x ≁ y): proof CORRECT** — subcases 1a,
   1b-i, 1b-ii all re-verified chord-by-chord. One repaired justification (species:
   garbled reason, true claim): in 1b-ii the chord u₁–w₂ dies by the C4 through {x, u₀}
   (the harvest's "share u₂, not adjacent" is not a reason). Registered as **Lemma G37**
   (d = 3 target + the extra hypothesis "some usable side-neighbour y of u₃ with y ≁ x").
   Status: **ADOPTED** **[PROMOTED 08-22 01:01 CDT, §26.1 — was ADOPTED-pending-S3,
   planner-confirmed]**.
3. **d = 3 Case 2 (x ~ y): NOT A PROOF — claim rejected.** **[SUPERSEDED 08-22 by §25.3: the
   statement itself is now REFUTED, F4 form included — Theorem G45. Not merely "not proved".]** The model's own self-audit
   concedes 2b; additionally (owner findings): the 2a/2b split is **non-exhaustive as
   stated** (e.g. d(u₁)=d(u₂)=2, d(y)=3, a(u₀)=3 falls in neither), 2a has **zero chord
   verification**, and 2b's "extreme-case graph with tails, path = 12" ships **no edge
   list** — a direct violation of the brief's edge-list rule.
4. **REFUTATION (owner, NEW): the bare d = 3 target (without F4) is FALSE.** Certified
   counterexample (script section G): n = 10, edges {09,05,15,23,25,26,28,49,46,57,58} —
   C4-free, geodesic 2–6–4–9 (d = 3), a(2)=3, a(9)=2, x=5 usable with a(5)=4,
   Case-2-forced (unique usable y = 0 ~ x), **path(G) = 6 < 7**. Its a=1 vertices are
   {1,3,7 leaves; 8 triangle-leaf}; peeling them leaves a C₆ and the frame dies — so the
   **F4 form is untouched and F4/a ≥ 2 is NECESSARY at d = 3, not a convenience**.
   **[CORRECTED 08-22, §25.3: the necessity inference was OVERSTATED, and the F4 form is NOT
   untouched — it is REFUTED by the graph H (Theorem G45). Accurate form: the bare target is
   false (CE-1) and the F4 target is false (H), so F4 is not the right repair at d = 3.]**
   (Three more bare CEs found in-sweep; d = 4 needs no F4 — 44 frames, 0 violations.)
5. **Owner sharpening of the open case** (machine-asserted on all 1112 Case-2-forced
   frames): in any Case-2-forced frame the usable-far set is **exactly {y}**
   (⊆ N(x) ∩ N(u₃), ≤ 1 by C4-freeness), dist(u₀,y) = 2, and **u₀–x–y–u₃ is itself a
   geodesic**. The residual open configuration is narrow, and the y-/geodesic-re-choice
   freedom is ammunition the harvest never used.
6. Numerics **[ANNOTATED 08-22, §25.6: these are FRAME counts, and a frame is a local
   skeleton — "0 F4 counterexamples" was evidence about frames, NOT about graphs. The graph H
   (§25.3) refutes the F4 target while being consistent with this frame sweep.]**: 2885 d=3
   frames (1773 Case-1, theorem held on all; 1112 Case-2-forced, 63
   F4-satisfying, **0 F4 counterexamples**); 44 d=4 frames, 0 violations; the model's
   explicit d=3 witness verified in full (C4-free, F4, a-values, path = 7 exactly);
   PG(2,3) d=3 frame verified Case-1-available; **PG(3,2) explicit d=4 frame verified**
   (geodesic L(5,10,15)–P10–…–L(2,9,11), ends a = 3, usable point P5 with a = 7, path ≥ 8)
   — this closes the round-9 "candidate-verify-before-citing" flag on STS(15) as a d=4
   instance.

## 23.2 Q29 (`problems/wowii/w133_3CAP_qwen.md`, claimed unqualified IMPOSSIBLE) — UPHELD (owner re-proved), with a free sharpening and an honesty annotation

1. **The counting proof is CORRECT and genuinely radius-independent.** The flagged pivot
   (Lemma 1's generalization to every vertex) **is licensed by the brief's definition**:
   every vertex is an end of an eccentricity geodesic of length ≥ rad, and "peripherally
   3-capped" quantifies over all geodesics of length ≥ rad at both ends. Owner re-derived
   L1–L6, both E(S,T) bounds (lower: Σ_S a − (|S| − k₁) via the per-type t-bookkeeping;
   upper: k₂ + n − |S| via the T₂↪K₂ injection), and the final 9k₃+5k₂+4k₁ < 0
   contradiction. Machine-tested **non-vacuously**: 449 peripherally-3-capped graphs in
   the sweep (60 with S ≠ ∅; K₁/K₂/K₃ components and a T₂ straddler all realized), all
   pass every lemma and both bounds.
2. **Owner sharpening (statement-hypothesis audit, free-generality direction): the same
   chain runs at l = 4** — the boundary case forces S = ∅ and then Σa ≤ 3n < 4n.
   Registered as **Theorem G38: a connected C4-free peripherally 3-capped graph has
   l < 4.** Consistency machine-checked: PG(2,3) (l = 4.0) and F7/PG(3,2) (l = 4.2) are
   both NOT capped (witnesses printed); F7's line has d_S = 3, the harvest's Lemma-1
   non-execution demo, confirmed. Status: **ADOPTED** **[PROMOTED 08-22 01:01 CDT, §26.1 —
   was ADOPTED-pending-S3, planner-confirmed]**.
3. **Pocket-2 consequence: (3CAP) as named in §21.2 is TRUE — proved, for every radius,
   not only rad ≥ 5**: any connected C4-free graph with l > 4 has a geodesic of length
   ≥ rad with an end u₀ carrying a usable side-neighbour x with a(x) ≥ 4.
4. **What (G+k) k=2 does NOT yet get**: G14/F6 additionally needs a(u₀) ≥ 3 and
   a(u_d) ≥ 2 at that same geodesic; the cap-break yields only a(u₀) ≥ 2. New named gap
   **(3CAP-GLUE)**: upgrade the cap-break to an end with a(u₀) ≥ 3 (far-end a ≥ 2 comes
   from F4-peeling, which preserves l > 4 (Σa−4n rises by +2 per peel) but is NOT yet
   shown to preserve rad ≥ 5). Radii 2, 3, 4 remain separate sub-questions.
5. **Honesty annotation carried with G38** (the harvest's own VACUOUS-UNTESTED flag,
   adjudicated): the rad ≥ 5 slice of G38's consequence is possibly vacuous — no C4-free
   l > 4 graph with rad ≥ 5 is on the books. New first-class open question **(Q-RAD):
   does C4-free ∧ l > 4 force rad ≤ 4?** If YES, pocket 2's rad ≥ 5 branch is vacuous
   and (G+k) k=2 collapses to radii 2–4. G38 itself is non-vacuous (it executes on the
   rad = 3 class, witnessed by F7). The unqualified IMPOSSIBLE tag survives because the
   text does prove the radius-uniform statement; the VACUOUS-UNTESTED admission attaches
   to the rad ≥ 5 slice's non-emptiness, not to the theorem's truth.
6. **Cross-harvest shared-assumption sweep: clean.** Both rest only on owner-proved F1
   (Q29 also on the §21.2 mass facts (M3)/(M4) = its F2/F3, owner-proved) and the
   owner-verified PG controls — re-verified again this round from scratch (sections B/C);
   no cross-citation between the tabs; Q29 uses F6 = G14 as a black box only.

## 23.3 Ledger and gate arithmetic

* **ADOPTED-pending-S3** (owner-re-proved, machine-backed; non-Qwen judge owed per the
  firewall; owner does not self-promote): **G36** (d = 4), **G37** (d = 3 Case 1),
  **G38** (3-capped ⟹ l < 4, hence (3CAP) at all radii). **[08-22 UPDATE: all three PROMOTED
  to ADOPTED — planner-confirmed, executed §26.1; non-Qwen judge pass delivered, §25.]**
* **Owner-PROVED outright** (script-certified, no external argument): the bare-d=3
  refutation + CE (§23.1.4) and the Case-2 frame sharpening (§23.1.5).
* **REGISTERED-OPEN**: d = 3 F4-form forced-Case-2 (the sharpened narrow frame);
  (3CAP-GLUE); (Q-RAD). **[08-22 UPDATE: all three are closed — the first REFUTED (§25.3,
  Thm G45), (Q-RAD) answered NO (§24.1, Thm G39), and (3CAP-GLUE) halved by G41 and reduced to
  one configuration by G42/G44 (§24.2c–e).]**
* **Pocket 1 after this round**: D=2 G12 · D=3 = G37 + the open forced-Case-2 · D=4 G36 ·
  D≥5 G14 — **NOT closed** (open: forced-Case-2, then the (RP-D) hypothesis-discharge
  glue). No milestone message due.
* **Pocket 2 after this round**: the 3-capped obstruction is DEAD (G38); residual =
  (3CAP-GLUE) + radii 2–4 + (Q-RAD). **NOT closed.**
* **Next S3/S2 rounds**: (i) one diff-scoped non-Qwen judge pass over §23 (G36/G37/G38 —
  the named MATH joints are G38's Lemma-1 licensing + the l = 4 boundary step, and G36's
  Step-3 alternative path); (ii) attack brief for the d = 3 forced-Case-2 under F4 (ship
  the sharpened frame, the CE, and the F4-necessity finding); (iii) (Q-RAD) probe brief
  (cheap: it is a construction/impossibility fork like Q29 and decides whether
  (3CAP-GLUE) even matters at rad ≥ 5).

---

# §24 owner-w133 round 11 (2026-08-22 00:11–00:45 CDT): five new results (G39–G43 + Cor G44) — pocket 2's `rad ≥ 5` branch reduced to ONE configuration; §23 S3 pass dispatched; both S2 briefs written

**Script**: `problems/wowii/w133_r11_qrad.py` → `.out`, **exit 0, 0 failures**, run before this
section was written. No SAT: every graph here is an explicit construction (PG(2,q) incidence
graphs and path-joined chains of them); all checks are direct verifications on the built graph.

## 24.1 **Theorem G39 (NEW, owner, machine-verified): (Q-RAD) is answered NO**

> **Theorem G39.** For every `R` there is a connected **C4-free** graph `G` with
> **`l(G) > 5.4`**, **no `a = 1` vertex** (so the F4 form applies), and **`rad(G) ≥ R`**.
> In particular **C4-free ∧ `l > 4` does NOT force `rad ≤ 4`**: the open question (Q-RAD) of
> §23.2.5 is settled in the negative.

**Construction (chain of blobs).** Let `B` = the point/line incidence graph of `PG(2,5)`:
`n = 62`, 6-regular, bipartite (hence triangle-free), C4-free, so `a(v) = d(v) = 6` for all
`v` and `l(B) = 6`, `rad(B) = diam(B) = 3`. Take `k` disjoint copies `B₁ … B_k` and join
`B_i` to `B_{i+1}` by a path with `L = 10` new internal vertices, attached at two **distinct**
vertices of each copy (one exit port, one entry port).

*C4-freeness* is preserved: the added vertices have degree ≤ 2 and lie on an induced path, so
no two vertices acquire two common neighbours. *a-values*: each internal path vertex has
`a = 2`; each attachment vertex gains exactly `+1` (its new neighbour is non-adjacent to all
its old neighbours); every other vertex keeps `a = 6`. Hence, exactly,
```
n(k) = 72k − 10,   Σ_v a(v) = 372k + 2(k−1) + 20(k−1) = 394k − 22,
l(k) = (394k − 22)/(72k − 10)  ↓  394/72 = 5.472…  > 4   for every k ≥ 1.
```
*Radius*: the chain contains an isometric path of length ≥ `(k−1)(L+1) = 11(k−1)`, so
`diam ≥ 11(k−1)` and `rad ≥ diam/2 ≥ 5.5(k−1)`; choose `k` with `5.5(k−1) ≥ R`. ∎

**Machine verification (`w133_r11_qrad.py`, exit 0, 0 failures).** Every listed graph was
built and checked from scratch: simplicity, connectivity, C4-freeness by the two-common-
neighbours test, **`a(v)` computed twice** (by `d − t` and by brute-force independence number
of `G[N(v)]`, required to agree — F1 re-checked, not assumed), exact rational `l`, and
`rad`/`diam` by all-pairs BFS. Controls: `PG(2,3)` reproduces `l = 4` **exactly** (the
below-threshold control: `l` is NOT `> 4`) and `PG(2,5)` reproduces `l = 6`, `rad = 3`.

**The standing witness (adopted as the first known member of the `rad ≥ 5` class):**
> **W1** = two copies of the `PG(2,5)` incidence graph joined by a path with 5 internal
> vertices. `n = 129`, C4-free, **`l = 252/43 = 5.8604…> 4`**, **`rad = 6`**, `diam = 12`,
> `min_v a(v) = 2`, a-histogram `{2: 5, 6: 122, 7: 2}`.
Larger verified members: `L = 10/15/20/30` at `rad = 9/11/14/19`; chains `k = 3/4/6/8` at
`rad = 15/22/35/48` (all `l ≥ 5.53`).

**Consequences for pocket 2 (ledger changes).**
1. The **VACUOUS-UNTESTED annotation carried with G38** (§23.2.5) is **LIFTED**: the `rad ≥ 5`
   slice of G38's consequence is **non-empty**, so **(3CAP-GLUE) genuinely matters at
   `rad ≥ 5`** — it cannot be dismissed as vacuous, and pocket 2 keeps that branch.
2. `l > 4` graphs are **not** confined to the incidence families: the class is closed under
   path-joining, which is where `a = 2` vertices and large radius enter. Any future argument
   for pocket 2 that implicitly assumes high `μ`, regularity, or bounded radius is dead on
   arrival — W1 kills it.
3. **F5's `n ≥ 14` floor is unaffected**; W1 has `n = 129`.

## 24.2 The refined fork (Q-RAD′), and why the G39 witnesses are not counterexamples

The (R1) device of §12 (*a diametral geodesic is induced, so* `path ≥ diam + 1`) already
closes every graph with `diam ≥ rad + ⌊l⌋ − 1`. At `⌊l⌋ = 4` this reads **`diam ≥ rad + 3`**,
so **(G+k) at k = 2 is at risk only on graphs with `diam ≤ rad + 2`**. *(This is not a new
device — it is §12's (R1) applied one level up; registered as scope bookkeeping, not as a
result.)*

Every G39 witness is diameter-heavy (`diam ≈ 2·rad`; machine-checked on three of them:
`rad/diam` = 6/12, 19/37, 22/43, each with an explicitly re-verified induced diametral
geodesic), hence **trivially satisfies** `path ≥ rad + 4` and is **not** a hard instance.
So G39 settles non-emptiness of the class but not of the *hard* part of it:

> **(Q-RAD′) — the sharpened fork: does there exist a connected C4-free graph with
> `l > 4`, `rad ≥ 5` AND `diam ≤ rad + 2`?** NO would have closed pocket 2's `rad ≥ 5`
> branch for free (via (R1)); YES makes that branch genuinely load-bearing.

## 24.2b **Theorem G40 (NEW, owner, machine-verified): (Q-RAD′) is answered YES**

*(Script `problems/wowii/w133_r11_qradp.py` → `.out`, **exit 0, 0 failures**.)*

> **Theorem G40.** There is a connected C4-free graph `G` with `l(G) = 6 > 4`,
> `rad(G) = diam(G) = 5` (so `diam ≤ rad + 2`), and `path(G) ≥ 168 ≥ rad + 4`.
> Hence **pocket 2's hard window at `rad ≥ 5` is NON-EMPTY**: the `rad ≥ 5` branch cannot be
> closed by the (R1) device and (3CAP-GLUE) is genuinely load-bearing there.

**The device (one line, and it is the reusable part).** A **vertex-transitive** graph has
`rad = diam`, so `diam ≤ rad + 2` holds automatically; and a **triangle-free** graph has
`a(v) = d(v)`, so a `k`-regular triangle-free graph has `l = k` exactly. Therefore *any*
vertex-transitive C4-free triangle-free `k`-regular graph with `k ≥ 5` and `diam ≥ 5` is a
witness. Cayley graphs of `PSL(2,p)` on three generators supply them.

> **W2 (the standing hard control).** `G = Cay(PSL(2,11), S)` with
> `S = {g, g⁻¹ : g ∈ {[5 0; 2 9], [1 5; 0 1], [1 6; 10 6]}}` over `GF(11)` (elements of
> `SL(2,11)` taken mod `±I`). Machine-verified: `n = 660`, connected, 6-regular,
> **triangle-free**, **C4-free**, hence `a(v) = 6` for every `v` and **`l = 6 > 4`**;
> `ecc` equal from three sampled vertices (transitivity check), **`rad = diam = 5`**;
> greedy certified induced path of **168** vertices (each certified chord-free), so
> `path ≥ 168 ≫ rad + 4 = 9`. Larger members verified the same way:
> `PSL(2,13)` (`n = 1092`, `rad = diam = 6`, path ≥ 239), `PSL(2,17)`/`PSL(2,19)`
> (`rad = diam = 7`), `PSL(2,23)` (`n = 6072`, `rad = diam = 7`).

**Consequences.**
1. **(Q-RAD) = NO and (Q-RAD′) = YES**: both forks registered in §23/§24.2 are closed, and
   both close in the direction that *keeps* pocket 2's `rad ≥ 5` branch alive. Pocket 2 gets
   no free closure from either; the residual is exactly **(3CAP-GLUE) + radii 2–4**.
2. **W2 is the project's first HARD positive control** for (G+k) at `k = 2`: `diam + 1 = 6`
   is strictly below `rad + 4 = 9`, so (R1) does not settle it, and the conjecture
   nevertheless holds on it with a factor of ~19. Every future pocket-2 argument must
   execute on W2.
3. **A dead end is now named**: no counterexample to (G+k) `k = 2` can be a
   vertex-transitive C4-free graph of degree ≥ 5 with an easily-found long induced path —
   the expander-like witnesses are all far from tight. Tightness, if it exists, lives in
   low-`a`, triangle-rich, irregular graphs (which is also where pocket 1's residual lives).

## 24.2c **Lemma G41 (NEW, owner): Lemma G14's hypothesis `a(u₀) ≥ 3` is REDUNDANT at `d ≥ 5`** — and this deletes half of (3CAP-GLUE)

*(Script `problems/wowii/w133_r11_g14sharp.py` → `.out`, **exit 0, 0 failures**, 120 certified
frames with `a(u₀) = 2` **exactly** — i.e. non-vacuous precisely where the old hypothesis
fails.)*

> **Lemma G41 (= G14 sharpened).** C4-free, geodesic `u₀ … u_d` with `d ≥ 5`,
> **`a(u₀) ≥ 2`**, `a(u_d) ≥ 2`, and some usable side-neighbour `x` of `u₀` with `a(x) ≥ 4`
> ⟹ `path(G) ≥ d + 4`.

**Proof.** G14's own construction, unchanged: `y ∈ N(u_d)` outside `u_{d−1}`'s component;
`w ∈ N(x)` in a component of `G[N(x)]` other than `u₀`'s and surviving the `u₂`- and
`u₃`-kills (`a(x) ≥ 4` pays for both); then `w, x, u₀, …, u_d, y` is induced by exactly the
non-adjacencies §13.4 lists. **The construction never selects a third component of
`G[N(u₀)]`** — it names only `x` — so `a(u₀) ≥ 2` (which "some usable side-neighbour `x`"
already presupposes) is all it consumes. ∎ *(Statement-hypothesis audit, free-generality
direction: G14 was NARROWER than its proof. Machine-checked non-vacuously as above: on
path-joined PG(2,5) chains, 120 frames with `a(u₀) = 2` and `d ≥ 5`, the construction built
and certified chord-free every time.)*

**Scope guard — the redundancy is specific to `d ≥ 5`.** At `d = 4` (G36) and `d = 3` (G37)
the proofs pick `z ∈ N(u₀)` outside **both** `u₁`'s and `x`'s components, which genuinely
needs `a(u₀) ≥ 3`. So G41 does **not** propagate downwards, and the pending S3 pass on
G36/G37 is unaffected.

**Consequence — (3CAP-GLUE) loses one of its two halves.** §23.2.4 recorded the gap as:
*the cap-break yields only `a(u₀) ≥ 2`, while the seed needs `a(u₀) ≥ 3` **and** far-end
`a ≥ 2`.* With G41 the first half is **gone at `rad ≥ 5`**: the cap-break's geodesic has
length ≥ rad ≥ 5 and its `u₀` automatically has `a(u₀) ≥ 2`. **What is left is exactly the far
end**, registered as
> **(FAR-2)** *C4-free, `l > 4`, `rad ≥ 5` ⟹ some geodesic of length ≥ rad has a usable
> side-neighbour of a-value ≥ 4 at one end **and** `a ≥ 2` at the other.*
**(FAR-2) + G41 ⟹ `path ≥ rad + 4` for the whole `rad ≥ 5` slice of pocket 2.** The `a(u₀) ≥ 3`
upgrade survives only as a **`rad = 4`** question (G36 needs it there); that is now a separate,
smaller item.

## 24.2d **Theorem G42 (NEW — pocket 2's `rad ≥ 5` branch is CLOSED for `μ ≥ 2`)**

*(Script `problems/wowii/w133_r11_g42.py` → `.out`, **exit 0, 0 failures**: 50 end-to-end runs
of the mechanism on W1 and W2 — a real cap-break geodesic located on the graph, the G41 path
built by the proof's own recipe, certified induced, and checked against `rad + 4`.)*

> **Theorem G42.** Let `G` be connected, C4-free, with **`l(G) > 4`**, **`rad(G) ≥ 5`**, and
> **no vertex of `a`-value 1** (`μ(G) ≥ 2`). Then **`path(G) ≥ rad(G) + 4`.**

**Proof (three lines, and every ingredient is already on the books).** By G38's contrapositive
(§23.2.3) `G` is not peripherally 3-capped, so there is a geodesic `u₀ … u_d` with
`d ≥ rad(G) ≥ 5` and a usable side-neighbour `x` of `u₀` with `a(x) ≥ 4`. Since `μ(G) ≥ 2`,
both `a(u₀) ≥ 2` and `a(u_d) ≥ 2` hold **for free** — and `a(u₀) ≥ 2` is now all the seed
needs, by **G41**. Apply G41 at `d ≥ 5`: `path(G) ≥ d + 4 ≥ rad(G) + 4`. ∎

**Status: ADOPTED** **[PROMOTED 2026-08-22 20:3x CDT, §29.1 — was ADOPTED-pending-S3;
planner ruling CERT-1, on a gate PRE-REGISTERED at `w133_state.md:632-634` during round 12
(08:51–09:5x CDT), roughly an hour BEFORE the muse-spark round it gates landed at 10:54–10:56
CDT. NOT PROVED-S3: that needs a second cross-family round, dispatched to Qwen web in round 15.]**
Originally recorded as: ADOPTED-pending-S3, inheriting G38's status — the G41 half is unconditional
(G14 is PROVED and §24.2c only deletes a hypothesis), so G42 promotes the moment the §23
judge returns `MATHEMATICS DEFECT FOUND: NO` on R-M1. **The owner does not self-promote.**

**Non-vacuity and tightness of the certification.** W2 (`μ = 6`, `rad = 5`) and W1 (`μ = 2`,
`rad = 6`) both satisfy every hypothesis; on **W2 the constructed path has exactly `9 = rad+4`
vertices**, i.e. the mechanism delivers the bound with no slack to spare — the check is not
passing by accident of a huge margin.

**What this does to the ledger.** Pocket 2's `rad ≥ 5` branch now reduces **entirely to the
`a = 1` case**: if `G` has a leaf or triangle-leaf, peeling (F7/§12.5) reaches `μ ≥ 2` and
preserves both C4-freeness and `l > 4`, but **may lower the radius**, and `path` of the peeled
graph is only a lower bound for `path(G)`. So the residual at `rad ≥ 5` is exactly:
> **(PEEL-RAD)** *control the radius drop under `a = 1` peeling — e.g. show that peeling a
> C4-free graph with `l > 4` and `rad ≥ 5` leaves `rad ≥ 5`, or that the drop is paid for by
> the induced path the peeled material itself supplies (hairs cost radius but pay path).*
**(FAR-2) is thereby also narrowed**: it is only ever needed on graphs that HAVE `a = 1`
vertices, since `μ ≥ 2` makes its condition (ii) automatic.

## 24.2e **Lemma G43 (far-end truncation) and Corollary G44** — the `a = 1` case shrinks to one configuration

*(Script `problems/wowii/w133_r11_g43.py` → `.out`, **exit 0, 0 failures**: 24 certified
truncation runs on graphs that **do** carry `a = 1` vertices — bare leaf and triangle-leaf
variants of W1, `l = 764/133` and `765/134`, `rad = 8`.)*

> **Lemma G43.** Let `G` be C4-free with a geodesic `u₀ … u_d`, **`d ≥ 6`**, `a(u₀) ≥ 2`, and
> a usable side-neighbour `x` of `u₀` with `a(x) ≥ 4`. Then **`path(G) ≥ d + 3`** — with
> **no hypothesis at all on `a(u_d)`**.

**Proof.** If `a(u_d) ≥ 2`, G41 gives `d + 4`. So let `a(u_d) = 1`; then `N(u_d)` is either
`{u_{d−1}}` (leaf) or `{u_{d−1}, q}` with `q ~ u_{d−1}` (triangle-leaf). **Truncate** to the
geodesic `u₀ … u_{d−1}`, of length `d − 1 ≥ 5`, and take `y := u_d` as the far-side vertex.
It is legitimate: `u_d ∈ N(u_{d−1})`, and `u_d` lies outside `u_{d−2}`'s component of
`G[N(u_{d−1})]` — in the leaf case `u_d` is isolated there; in the triangle-leaf case its
component is `{u_d, q}`, and `u_{d−2} ∉ {u_d, q}` because `u_{d−2} ≠ u_d` (distance 2) and
`u_{d−2} = q` would force `dist(u_{d−2}, u_d) = 1`, contradicting the geodesic. *(Note
`u_{d−2} ~ q` is also impossible: `q` would then have two neighbours inside `G[N(u_{d−1})]`,
which is a matching.)* Hence `a(u_{d−1}) ≥ 2` with `y = u_d` witnessing it, `x` is still a
usable side-neighbour of `u₀` for the truncated geodesic (same first step `u₁`), and G41 at
`d − 1 ≥ 5` gives `path ≥ (d−1) + 4 = d + 3`. ∎

> **Corollary G44.** Let `G` be connected, C4-free, `l(G) > 4`, `rad(G) ≥ 5`. Then
> **`path(G) ≥ rad(G) + 4`** *unless* **every** geodesic of length ≥ rad that fails to be
> 3-capped at an end has **length exactly `rad`** *and* **`a = 1` at its far end**.

*Proof.* Such a geodesic exists by G38. If one of them has length `d ≥ rad + 1 ≥ 6`, G43 gives
`path ≥ d + 3 ≥ rad + 4`. If one of them has far end with `a ≥ 2`, G41 gives
`path ≥ d + 4 ≥ rad + 4`. ∎ *(Same status as G42: **ADOPTED** — **[PROMOTED 2026-08-22 20:3x CDT, §29.1, planner ruling
CERT-1; was ADOPTED-pending-S3 through G38. G41 and G43, unconditional, are ADOPTED with them.
NOT PROVED-S3 — see §29.1's scope guard.]**)*

**Effect on the residual.** Combined with G42, pocket 2 at `rad ≥ 5` is now down to a single
configuration: *the cap-break happens only on geodesics of length exactly `rad`, and every one
of those ends in a leaf or triangle-leaf.* That is the sharp form of (PEEL-RAD)/(FAR-2) and it
is what the Q32 brief now asks for. **Non-vacuity of the ambient case is settled** — the class
`{C4-free, l > 4, rad ≥ 5, some a = 1 vertex}` is inhabited (the two graphs used above) — so
the residual cannot be dismissed as empty without an argument.

## 24.3 Round-11 dispatches (S3 + S2), all written this round

1. **Non-Qwen S3 pass over §23 — WRITTEN and DISPATCHED.** Brief `prompts/w133_S3_R23.md`
   (self-contained: definitions, F1/F2/F3/G14 as fenced context, then G36/G37/G38 **with their
   full proofs as re-derived by the owner**, CE-1 and the S-1 sharpening). Judge = an
   **opus-family** reviewer (non-Qwen ⟹ firewall satisfied: the G36/G37/G38 arguments are of
   Qwen origin, owner-re-proved) run under **hard isolation** — it may read that one file and
   no other repo file, no internet, may write and run its own scripts (**SAT barred**), and
   writes to `problems/wowii/w133_S3_R23_opus.md`. Named joints: **R-M1 = MATHEMATICS, the
   joint the gate turns on** (G38's Lemma-1 licensing — the "every vertex is an end of a
   geodesic of length ≥ rad" step — **plus** the `l = 4` boundary run in non-strict form);
   **R-M2** = G36's Step-3 alternative path, all 21 chord pairs; **R-M3** = G37's three
   subcases incl. the repaired `u₁ ≁ w₂` justification; **R-B1/2/3** = the (3CAP)-at-all-radii
   consequence + vacuity annotation, CE-1, S-1. Both mandatory probes attached (the
   both-directions statement-hypothesis audit; the three-part control section). Deliverable
   line 2 is `MATHEMATICS DEFECT FOUND: YES | NO`, separate from the verdict word.
   **Gate arithmetic (pre-stated, planner-confirmed, owner does not self-promote):
   NO ⟹ G36/G37/G38 satisfy the promotion condition from ADOPTED-pending-S3;
   YES ⟹ the promotion is held and the named joint reopens.**
   *(R-B1(ii) as dispatched still asks the judge to audit the vacuity annotation. §24.1
   supersedes that annotation — the judge was NOT told, deliberately: an independent judgement
   on the annotation's logic is worth more than a corrected premise, and its verdict there
   cannot move the gate bit, which is MATHEMATICS-only.)*
2. **S2 brief — d = 3 forced-Case-2 under F4**: `prompts/w133_r11_D3CASE2.md` (queue row Q31).
3. **S2 brief — (3CAP-GLUE)**: `prompts/w133_r11_3CAPGLUE.md` (queue row Q32). The round-10
   plan called for a (Q-RAD) probe brief; §24.1 and §24.2b settled **both** the literal fork
   and its sharpening in-house before any dispatch, so the slot is re-pointed at what the two
   answers leave standing — pocket 2's single named residual lemma — and both new witnesses
   (W1, W2) ship inside it as mandatory controls. The queue row records the substitution.

## 24.3b Process defect this round: a READY row was edited under a dispatching driver

**What happened.** `prompts/w133_r11_3CAPGLUE.md` (Q32) was flipped to READY and then rewritten
three times in ~6 minutes while the Qwen driver was dispatching it. Two conversations were
burned on superseded statements (both marked STALE / do-not-harvest in the queue row). This is
the owner's fault, not the driver's, and it is now covered by the planner's **READY-row freeze
discipline** (`notes/methodology.md`): READY = handoff; the file freezes at that moment; edits
require flipping to REVISING first, with a version bump.

**Why it churned — and the reason matters for how the stale tabs are treated.** The edits were
not polish: each was a *new proved result of this same round shrinking the target*.
v1 asked for (FAR-2) at `rad ≥ 5`; then **G41** deleted one of (3CAP-GLUE)'s two halves; then
**G42** closed the entire `μ ≥ 2` slice, turning v1's question into a proved fact; then
**G43/G44** killed the `a = 1` far end whenever `d ≥ 6`, turning v2's question into a proved
fact too. **So the two stale tabs are answering questions the project has since PROVED** —
harvesting them would re-adjudicate settled ground, which is why they are marked
do-not-harvest rather than merely superseded.

**The real lesson (recorded so it is not repeated).** The own-attack slot and the brief-writing
slot were interleaved in the same round on the *same target*. When the owner is actively
attacking the very question a brief asks, the brief must not go READY until the attack slot
closes — otherwise the free channel is dispatched against a moving target. **Standing personal
rule: write the brief last, after the round's own mathematics is flushed.**

**Q31 was not affected.** Its two post-READY edits (`queue row Q30 → Q31` in the title, and an
`F7 → F6` fact-label fix) both sit **above** the `---` separator, inside the driver-instruction
block that the driver strips before pasting. The dispatched paste (16 010 B, byte-matched by
the driver) is identical to the text that was READY, so the clean Q31 dispatch stands.

**Q32 is now v3 FINAL and frozen**, with the version stamp in the file's header and the
provenance in the queue row. v3 also **repairs a false claim v2 shipped**: v2 asserted the class
`{C4-free, l > 4, rad ≥ 5, some a = 1 vertex}` had no witness on file, which §24.2e's
certification (W1 + leaf, W1 + triangle-leaf, `l ≈ 5.74`, `rad = 8`) had already made false —
only Problem A's *full* configuration is witness-free.

## 24.4 Ledger after round 11

* **PROVED outright this round** (owner, script-certified, no external argument):
  **Theorem G39** ((Q-RAD) = **NO**), **Theorem G40** ((Q-RAD′) = **YES**), and
  **Lemma G41** (G14 sharpened: `a(u₀) ≥ 3` redundant at `d ≥ 5`). Both open questions
  registered in §23.2.5/§24.2 are now **CLOSED**, and W1/W2 enter the fact base as standing
  controls (W2 = the first hard control at `rad ≥ 5`).
* **ADOPTED** **[PROMOTED 08-22 01:01 CDT, §26.1, planner-confirmed]**: G36, G37, G38 — the
  judge pass returned (§25). **Still ADOPTED-pending-S3** (no separate planner confirmation on
  record for these at this executor's timestamp; see §26.1 scope guard) — **plus Theorem G42
  and Corollary G44**, which inherit G38's status and promote with it.
  **Unconditional this round**: G39, G40, G41, **G43**.
* **REGISTERED-OPEN**: ~~d = 3 F4-form forced-Case-2 (brief written, Q31)~~ **— REFUTED
  08-22 by Theorem G45, §25.3; struck from the open list** ; **(PEEL-RAD)** and
  its equivalent form **(FAR-2)** — all that is left of pocket 2 at `rad ≥ 5` after G41/G42,
  and needed only on graphs that HAVE `a = 1` vertices (brief written, Q32); the `a(u₀) ≥ 3`
  upgrade at **`rad = 4`** only; radii 2–3.
* **Pocket 1**: **[UPDATED by §25.3]** D=2 G12 · **D=3 = G37 (Case 1 proved) + Case-2-forced
  REFUTED as posed (Thm G45, even under F4)** · D=4 G36 · D≥5 G14/G41, then the (RP-D) glue.
  The D=3 layer no longer needs a proof of the missing case — it needs a **new hypothesis**
  (global `l > 3`, or a declared a-value surcharge), because the hypothesis-free local
  statement is false. **NOT closed.**
* **Pocket 2 — the round's real movement**: (3CAP) dead (G38); the two vacuity forks closed
  **in the direction that keeps the branch alive** (G39, G40); (3CAP-GLUE) halved (G41); and
  then **the whole `rad ≥ 5` branch closed for `μ ≥ 2` (G42, pending G38's gate)**. Residual at `rad ≥ 5` =
  **one configuration** (G44: cap-break only on geodesics of length exactly `rad`, each ending
  in a leaf or triangle-leaf), equivalently (PEEL-RAD)/(FAR-2) — plus
  **radii 2–4** (`rad = 4` additionally wants the `a(u₀) ≥ 3` upgrade). W2 is the mandatory
  execution control. **NOT closed** (pocket 2 needs radii 2–4 too). **No milestone message
  due; G42 is not self-promoted.**
* **Honesty note on scope**: neither G39 nor G40 moves Conjecture 133 or either pocket by
  itself — they are class-non-emptiness facts. Their value is that they **delete two possible
  free closures** the round-10 plan was hoping for, and they hand every future pocket-2
  argument an explicit graph it must survive.

## 24.5 Defensive re-verification of CE-1 (it is now load-bearing in two shipped briefs)

CE-1 (§23.1.4) is cited as a *proved fact* inside the Q31 brief (as its F8, with a mandatory
"your own argument must fail on this graph" probe) and is one of the §23 judge's joints
(R-B2), so it was re-verified this round from the edge list alone, by fresh code: **C4-free**
(zero vertex pairs with two common neighbours); `2–6–4–9` is a **geodesic of length 3**;
`a(2) = 3`, `a(9) = 2`, `a(5) = 4`; `G[N(2)]`'s components are `{3}, {5,8}, {6}`, so `x = 5`
is a **usable** side-neighbour; `G[N(9)]`'s components are `{0}, {4}`, so the usable-far set is
**exactly `{0}`** and `0 ~ 5`, i.e. **Case-2-forced**, matching S-1(i); and an exhaustive
induced-path DFS gives **`path = 6` exactly** `< 7`. Its `a = 1` vertices are `{1, 3, 7}`
(leaves) and `{8}` (triangle-leaf: `N(8) = {2,5}` with `2 ~ 5`), exactly as §23.1.4 states.
**Every number in §23.1.4's CE-1 line reproduces.**

---

# §25 owner-w133 round 11 slice 2 (2026-08-22 00:46–01:0x CDT): ADJUDICATION of the §23 S3 judge (opus, blind) — gate bit NO, and a REFUTATION the owner's own sweep missed

**Judge report**: `problems/wowii/w133_S3_R23_opus.md` (46 KB), brief `prompts/w133_S3_R23.md`,
non-Qwen (opus family) under hard isolation. **Verdict: PARTIAL. `MATHEMATICS DEFECT FOUND: NO`.**
Per joint: **R-M1 CLEAN · R-M2 CLEAN · R-M3 CLEAN** · R-B1 PARTIAL · **R-B2 REFUTED** · R-B3 CLEAN.
Owner verification script: `problems/wowii/w133_r11_adjudicate.py` → `.out` (exit 0).

## 25.1 Verdict-quality audit (the pass is judged before its findings are) — **PASSES**

Both mandatory probes are present and substantive. The statement-hypothesis table covers all
**12** required statements in both directions, and it is not a formality: it produced a
purpose-built counterexample (`T*`, a 16-vertex tree) to show that G38's **Lemma 1, read alone,
is wider than its proof**, then correctly ruled the inheritance typographically legitimate
because Lemmas 1–6 sit inside the `Suppose for contradiction` block. The control section names
non-executing facts correctly. The judge also flagged its own borderline classification instead
of burying it (see §25.2). **Verdict quality: accepted.**

## 25.2 Gate arithmetic — the promotion condition is MET (reported, not executed)

**G36, G37, G38 are CLEAN on all three MATHEMATICS joints.** Specifically: G38's Lemma-1
licensing is genuinely authorised (the definition's quantifier is universal, `ecc(v) ≥ rad`
holds for every vertex, and the centre / `a(v) ≤ 1` degenerate cases are fine); the `l = 4`
boundary chain is valid step by step in its non-strict form and the conclusion is correctly
the **strict** `l < 4`; G36's Step-3 path survives an independent 21-pair chord re-derivation;
and **G37's repaired justification is correct and is the right repair** — the judge names the
`C4` as `x–u₀–u₁–w₂–x`, which is the owner's repair re-derived independently.

**Owner's ruling on the judge's own flagged judgement call.** The judge classified its
refutation (below) as BOOKKEEPING under the brief's operational test — *its repair leaves every
proof intact, and nothing in scope consumes it* — and said plainly that a stricter convention
("any refuted in-scope assertion flips the bit") would flip R-B2. **The owner agrees with
BOOKKEEPING for the gate bit**: the refuted item is a **status sentence in §23.1's prose**
("the F4 form remains open"), not a step, hypothesis or citation inside G36, G37 or G38; none of
the three consumes it, and all three stand untouched. **The planner is given both readings
explicitly and decides.** Owner does not self-promote.

**Planner ruling (confirmed 08-22 01:01 CDT, executed via registry-move executor):
BOOKKEEPING.** Operational test applied: no step, hypothesis or citation of G36, G37 or G38
consumes the refuted status-sentence. The **stricter-convention flag is preserved for audit**
— outvoted for this gate bit, not discarded; it remains available if a future round's
operational test differs. See §26.1 for the resulting promotion.

## 25.3 **The real finding: the F4-form `d = 3` forced-Case-2 target is FALSE** (Theorem G45)

> **Theorem G45 (refutation; judge-found, owner-verified).** There is a connected `C4`-free
> graph `H` with **`μ(H) = 2`** (no `a = 1` vertex, so the F4 form applies and no peeling is
> possible), a geodesic `u₀u₁u₂u₃ = 2–1–0–8`, `a(u₀) = 3`, `a(u₃) = 2`, a usable side-neighbour
> `x = 3` of `u₀` with `a(x) = 4`, the frame **Case-2-forced** (the unique usable side-neighbour
> of `u₃` is `y = 9`, and `9 ~ 3`), and **`path(H) = 6 < 7 = d + 4`.**
> `H`: `n = 10`, edges `01, 04, 05, 08, 12, 23, 26, 35, 37, 39, 46, 47, 48, 89`.

**Owner re-verification, from the edge list alone, by independent code**: `C4`-free (no vertex
pair with two common neighbours) ✓; connected ✓; a-values `(3,2,3,4,3,2,2,2,2,2)`, `μ = 2` ✓;
`2–1–0–8` is a geodesic of length 3 ✓; `G[N(2)]` components `{1},{3},{6}` so `x = 3` is usable
with `a = 4` ✓; `G[N(8)]` components `{0,4},{9}` so the usable-far set is exactly `{9}` and
`9 ~ 3` ⟹ **Case-2-forced** ✓; exhaustive induced-path DFS gives **`path = 6`** exactly, witness
`0–8–9–3–2–6` ✓. **Every number the judge reported reproduces.** The judge additionally reports
`H` is minimum-order (`n = 9` exhaustively excluded); not re-verified here, and recorded as
*judge-claimed, unverified*.

**Ledger effect (this is the round's most consequential change).**
* §23.1's item 3/6 status "**F4-form `d = 3` Case-2 OPEN**" is **REFUTED and struck**; §23.3's
  REGISTERED-OPEN entry for it is removed.
* §23.1.4's inference "**F4 is NECESSARY at `d = 3`**" was **overstated** and is corrected: from
  CE-1 one may conclude only that the *bare* statement is false. The accurate joint statement is
  now: **the bare `d = 3` target is false (CE-1) and the F4 form is also false (`H`) — so F4 is
  not the right repair at `d = 3`, and the Case-2-forced regime needs a different hypothesis.**
* **Neither G36 nor G37 is touched — owner-VERIFIED, not taken on trust.** `diam(H) = 3`, so
  `H` carries no geodesic of length ≥ 4 (G36 cannot execute); and an exhaustive enumeration of
  `H`'s qualifying `d = 3` frames returns **exactly two** — `2–1–0–8` and `2–6–4–8`, both with
  `x = 3` and usable-far set `{9}` — and **both are Case-2-forced**, so G37 cannot execute
  either. The judge's claim is confirmed.
  * *Honesty note on that check.* The owner's **first** enumerator omitted the `u₁ ~ u₂` edge
    test and therefore admitted non-paths as frames, producing a **spurious Case-1 hit** that
    briefly looked like a refutation of G37. The bug was in the owner's code, not in the judge's
    claim. It is recorded because it is the same species as §25.6's lesson: **a "frame" is only
    a frame if it is actually a path**, and frame machinery on this problem has now misled the
    owner twice in two rounds.

**Scope guard the owner must supply, and it matters.** `Σ_v a(v)(H) = 25`, `n = 10`, so
**`l(H) = 2.5 < 3`**: `H` sits **outside** pocket 1's live class, which carries `l > 3`.
So what `H` kills is the **hypothesis-free LOCAL route** at `d = 3` — the deep endpoint
extension cannot be pushed down to `d = 3` in the project's own currency, full stop — **not
(RP-D) itself.** The next `d = 3` attempt must consume either a global hypothesis (`l > 3`) or a
declared a-value surcharge; the "free" route is closed. **Pocket 1's D=3 layer therefore reads:
Case 1 = G37 (proved); Case-2-forced = REFUTED as posed; the layer needs a new hypothesis, not
a new proof.**

**Registration annotation (08-22, registry-move executor): planner-verified independently from
the edge list alone** — `C4`-free, min `a(v) = 2`, geodesic `2–1–0–8`, `x = 3` with
`a(x) = 4`, usable-far set `{9}`, longest induced path `6 < 7` by exhaustion, `l(H) = 2.5` —
with the `l`-statistic definition itself cross-checked against `STS(15) = 4.2`. **Verdict:
REFUTES-the-target-as-posed**; the scope annotation `l(H) = 2.5 < 3` **stands**.

## 25.4 **B10 adjudicated: §12.5's peeling arithmetic is wrong for triangle-leaves** (owner-verified)

The judge found that the peeling fact as stated everywhere in this project — *"deleting an
`a = 1` vertex raises `Σa − 3n` by exactly 1"* — is **false for triangle-leaves**. Owner
verified on CE-1: deleting the **leaf** `1` gives `Σa: 19 → 17`, `n: 10 → 9`, slack `−11 → −10`
(**+1**); deleting the **triangle-leaf** `8` gives `Σa: 19 → 18`, slack `−11 → −9` (**+2**).
*Reason*: a leaf's removal costs its host an independent neighbour, while a triangle-leaf's host
loses one degree **and** one triangle, so `a = d − t` is unchanged at the host.
**Correct statement: the slack rises by `+1` per peeled leaf and `+2` per peeled triangle-leaf,
so `≥ +1` always.** Every use in this project needs only the `≥ +1` direction (monotonicity), so
**no conclusion moves** — including §24.2d/§24.2e, which do not use peeling at all. Recorded as
a repair to §12.5's statement; the two round-11 briefs are corrected (§25.5).

## 25.5 Remaining findings, all accepted as BOOKKEEPING, with repairs

* **B2** (missing chord `x ≁ u₁` in G36 Step 2 and G37 1a) — accepted; the repair is one line:
  `x` is a *usable* side-neighbour, i.e. outside `u₁`'s component of `G[N(u₀)]`, hence `x ≁ u₁`
  by definition. **B3/B4** (G36's distinctness paragraph argues distinctness from
  non-adjacency and is incomplete; G37 states none) — accepted; distinctness must be argued from
  distance and component membership, and both proofs will carry an explicit distinctness list.
* **B5** (Lemma 6 cites Lemma 1's *statement* where it needs its *proof*) and **B6** (Lemma 2's
  unused `v ∈ S`) — accepted, and they compose into the judge's own clean repair: drop `v ∈ S`
  from Lemma 2 and have Lemma 6 cite the generalised Lemma 2. **B7** (Lemma 3's `k ≥ 5` cycle
  case is under-argued) — accepted; the cleaner uniform argument is that the forced chord raises
  a degree to 3, contradicting `Δ(G[S]) ≤ 2`. **B8** (`rad = 0`) — accepted, trivial.
* **Free-generality items adopted** (statement narrower than proof, all harmless, all useful):
  G38's contrapositive runs at **`l ≥ 4`**, not only `l > 4` — which is exactly the boundary the
  owner's own `l = 4` sharpening (§23.2.2) established, now independently confirmed from the
  other direction; **S-1 holds under weaker hypotheses** than stated (`a(u₀) ≥ 3`, `a(x) ≥ 4`
  and usability of `x` are all unused — judge-verified on 325 916 instances, 0 failures);
  Lemmas 4 and 5 are pure `C4`-freeness facts; connectivity is unused in G36/G37.
* **Lemma-1-read-alone (`T*`)**: accepted as a presentational defect only — restate the block's
  lemmas as "Let `G` be as in Theorem G38"; the mathematics is unaffected.

## 25.6 Intel note (for `notes/case_intel/`)

The refutation `H` is the **first time an S3 judge on this problem produced new mathematics
rather than only defects** — and it landed on a claim the owner's own 1112-frame sweep had
called open, because that sweep was **frame-local**: it enumerated local skeletons and could not
see `path(G)` of a completed 10-vertex graph. **Methodological lesson, recorded: a
"0 counterexamples in N frames" result is evidence about frames only, and must never be
reported in a way that reads as evidence about graphs.** The round-10 phrasing did read that
way, and §23.1.6's numbers are annotated accordingly.

---

# §26 registry-move executor (2026-08-22 01:01 CDT): REGISTRY — G36, G37, G38 are **ADOPTED** (planner-confirmed)

**This section executes a registry action. It contains no new mathematics; G36/G37/G38's proof
text is untouched.** owner-w133's session ended before it could execute this planner-confirmed
move; this section executes it mechanically.

## 26.1 Promotion: ADOPTED-pending-S3 → ADOPTED

**Planner confirmation 08-22 01:01 CDT, delivered via registry-move executor.**

* **Label/convention**: reuses the tier-label-drop convention used for Claim Q6.1 / Theorem G35
  after the Q19 G-diff pass (§22: PROVED-pending-planner → PROVED). Here:
  **ADOPTED-pending-S3 → ADOPTED** for G36, G37, G38.
* **Basis** (§25, §25.2): judge verdict **`MATHEMATICS DEFECT FOUND: NO`**, **R-M1/R-M2/R-M3
  CLEAN** (`problems/wowii/w133_S3_R23_opus.md`); owner adjudication re-run byte-identical
  (`problems/wowii/w133_r11_adjudicate.py`); precedent **Q19/G35** (§22).
* **Rows promoted**: **G36** (§23.1.1, Q28 target at d = 4), **G37** (§23.1.2, d = 3 Case 1),
  **G38** (§23.2.2, 3-capped ⟹ l < 4, all radii). Every other status-line site mentioning
  their pending state (§23.1, §23.2, §23.3, §24.4, and the mirrored entries in
  `orchestration/results/w133_state.md`) is annotated to point here.
  **[SUPERSEDED IN PART, 2026-08-22 20:3x CDT: the scope guard below is DISCHARGED — G42, Cor
  G44, and with them G41 and G43, were promoted to ADOPTED at §29.1 on planner ruling CERT-1.]**
* **Scope guard.** This promotion covers **G36/G37/G38 only**. **Theorem G42** and
  **Corollary G44** (§24.2c–e, §24.4), recorded as "inheriting G38's status and promoting with
  it," are **not** ruled on by this executor — no separate planner confirmation for them is on
  record at this timestamp — and remain **ADOPTED-pending-S3** until confirmed.

## 26.2 Cross-reference: classification and G45 annotation

The other two planner rulings executed this pass are recorded at their registration sites
rather than duplicated here: the **BOOKKEEPING classification** of the judge's R-B2 refutation
(with the stricter-convention flag preserved for audit) is at **§25.2**; the **independent
planner verification annotated onto Theorem G45's registration** is at **§25.3**.

---

# §27 owner-w133 round 12 (2026-08-22 08:51–09:5x CDT, opus): pocket 1's D = 3 layer gets a MECHANISM — **Lemma G46** (Case-2-forced ⟹ induced C₆), **Lemma G47** (peeling reduction), and the new named target **(D3-C6)**

**Scripts** (both run before any prose in this section, both `exit 0`, **0 failures**, NO SAT):
`problems/wowii/w133_r12_d3.py` → `.out` and `problems/wowii/w133_r12_d3b.py` → `.out`.

## 27.1 The question this round inherits

§25.3 (Theorem G45) killed the **hypothesis-free local route** at `d = 3`: the bare target is
false (CE-1) and the F4/`μ ≥ 2` form is also false (`H` = CE-2), so **F4 is not the right
repair at `d = 3`**. The layer's ledger reads: *Case 1 = G37 (ADOPTED); Case-2-forced =
REFUTED as posed; **the layer needs a new hypothesis, not a new proof**.* This round supplies
the mechanism that makes one available.

**The constraint on any candidate hypothesis** (this is the whole design problem): it must
(i) **exclude both certified counterexamples**, and (ii) be **implied by, or affordable
inside, the live class** — pocket 1's residual carries the global hypothesis `l(C) > 3`.

## 27.2 **Lemma G46 (NEW, owner, unconditional)** — the Case-2-forced frame is an induced hexagon

> **Lemma G46.** Let `G` be C4-free, let `u₀u₁u₂u₃` be a geodesic, let `x` be a usable
> side-neighbour of `u₀`, let `y` be a usable side-neighbour of `u₃`, and suppose **`x ~ y`**.
> Then `{u₀, u₁, u₂, u₃, y, x}` induces a **6-cycle** `u₀ – u₁ – u₂ – u₃ – y – x – u₀`.
> **No hypothesis on any a-value is used.**

**Proof.** *Distinctness.* `u₀…u₃` are distinct (geodesic). `x ≠ u₁` by usability;
`x ≠ u₂, u₃` since `dist(u₀, u₂) = 2` and `dist(u₀, u₃) = 3` while `x ~ u₀`. Symmetrically
`y ≠ u₂, u₁, u₀`. Finally `x ≠ y` because `dist(u₀, x) = 1` while `dist(u₀, y) ≥ 2`
(`y ~ u₃` and `dist(u₀,u₃) = 3`).
*Edges.* `u₀u₁, u₁u₂, u₂u₃` (geodesic), `u₃y` and `xu₀` (neighbourhood), `yx` (hypothesis).
*Non-edges — all six of them.* `u₀u₂`, `u₀u₃`, `u₁u₃`: geodesic. `xu₁`: usability of `x`.
`yu₂`: usability of `y`. `xu₂`: else `x–u₀–u₁–u₂–x` is a `C₄`. `yu₁`: else `y–u₃–u₂–u₁–y`
is a `C₄`. `xu₃`: `dist(x, u₃) ≥ 2` since `x ~ u₀` and `dist(u₀,u₃) = 3`. `yu₀`: symmetric. ∎

**Machine certification** (`w133_r12_d3.py` §B): **9 212 Case-2-forced 3-frames** over
**885** of 1 262 graphs (the two certified counterexamples + greedy-random maximal C4-free
graphs, `8 ≤ n ≤ 16`), **0 failures**; 410 of those frames additionally satisfy the full
a-value package `a(u₀) ≥ 3, a(u₃) ≥ 2, a(x) ≥ 4`. The same sweep re-asserts **S-1**
(§23.1.5): the usable-far set of a Case-2-forced frame is a **singleton**, 0 failures.

**What G46 is worth, stated honestly.** The proof is six elementary lines; its value is not
difficulty but **connection**: it maps pocket 1's dead `d = 3` residual onto the project's
existing **induced-C₆ machinery** (§13.2's G13, and the whole of §20 — G32/G32.1, G33, G34,
G35). *Novelty note (S1):* the configuration is a cousin of **G13**'s induced `C₆` in the
`r = 3` residual; what is new is that it is forced by the *Case-2* condition itself, with
no a-value hypothesis, so it is available exactly where the local route died.

**The import is NOT free, and this is the honest gap.** §20's engine (Lemma G32) assumes
**no induced P₆**; here the counterexample hypothesis is the weaker **no induced P₇**
(`path ≤ 6`). G32's witness for a consecutive attachment produces a P₆, which under `path ≤ 6`
is no contradiction. **CE-2 confirms this is a real obstruction, not a formality**: its
off-hexagon vertex `4` attaches to the two *consecutive* hexagon vertices `0` and `8`.
So a **P₇-analogue of G32 must be proved**, and that is the round's dispatched work (§27.7).

> ### ⚠ CORRECTION TO THIS TARGET — entered at round 24 on planner **RULING BU**, at the target's own site
> **The target as stated one paragraph above is UNSATISFIABLE, and it stood unsatisfiable for
> eleven rounds (rounds 12 → 23).** "A P₇-analogue of G32" was read by every later round as the
> **EXCLUSION** form — G32 at P₆ level says `W_1` and `W_cons` are **EMPTY**, so the analogue was
> taken to be "`W_1` and `W_cons` are empty under *no induced P₇*". **That statement is FALSE.**
> Round 23 (§35, numbered **G58** by RULING BT) settled it: `W_1` and `W_cons` are **non-empty in
> hypothesis** — CE-2's vertex `4` is a consecutive attachment (three paragraphs above), and §35
> adds two explicit `n = 9` in-hypothesis maximisers, one in each class.
>
> **What survives at P₇ level is the BOUNDED form, and that is the corrected target — now
> DISCHARGED:**
> > **G58 (§35).** Under (D3-C6)'s hypotheses, every `v ∈ W_1 ∪ W_cons` has `d(v) ≤ 4` and
> > `a(v) ≤ 3`, both exact and attained; hence `a(v) − 3 ≤ 0` on the whole non-antipodal
> > off-cycle population.
>
> **Read this before reusing §27.2's last paragraph as a live goal.** The exclusion form is not
> merely unproved — it is refuted, so a round spent on it is a round spent proving something
> false. The bounded form is what §35 proves and what §36 then uses.
> *(Why the exclusion form had to fail is in §35.2 in one line: a legal trace bounds its vertex
> iff the hexagon carries an induced 5-arc anchored in the trace and meeting it nowhere else.
> At P₆ level the arc needed is shorter and every legal trace is killed outright; at P₇ level the
> single and consecutive traces survive **bounded**, and only the antipodal pair escapes entirely.)*

## 27.3 The kill table (which candidate hypothesis is implied-or-affordable)

`w133_r12_d3.py` §C, computed on the certified frames of CE-1 and CE-2:

| candidate extra hypothesis | holds on CE-1? | holds on CE-2? | kills both? | affordable? |
|---|---|---|---|---|
| **`l(G) > 3`** | no (`l = 1.9`) | no (`l = 2.5`) | **YES** | **FREE — implied by the live class** |
| `μ(G) ≥ 2` | no | **yes** | no | free (peeling) — **but already refuted by CE-2** |
| `μ(G) ≥ 3` | no | no | YES | not affordable (peeling only reaches `μ ≥ 2`) |
| `a(x) ≥ 5` | no | no | YES | a declared surcharge; affordability open |
| `a(u₀) ≥ 4` | no | no | YES | a declared surcharge; affordability open |
| `a(u₃) ≥ 3` | no | no | YES | a declared surcharge; affordability open |
| `a(y) ≥ 3` | no | no | YES | a declared surcharge; affordability open |
| triangle-free | no | no | YES | **not available** — the class allows triangles |
| `δ(G) ≥ 3` | no | no | YES | not available (`W1` has `a = 2` vertices; hairs are legal) |

**Reading.** Exactly one candidate is **free**: the global hypothesis `l > 3` that the live
class already carries. Every other killer is a purchase. So the D = 3 layer's new hypothesis
should be `l > 3` — and G46 is what makes a global hypothesis usable, because it converts the
frame into a **global** object (an induced C₆) on which a mass argument can run.

## 27.4 The new named target **(D3-C6)**, and exactly what it buys

> **(D3-C6)** *A connected C4-free graph that contains an **induced C₆** and has **no induced
> P₇** satisfies `l(G) ≤ 3`, i.e. `Σ_v a(v) ≤ 3n`.*

> **Corollary (conditional, owner).** (D3-C6) `⟹` **every C4-free graph with `l > 3` carrying
> a Case-2-forced 3-frame has `path ≥ 7`** — i.e. **pocket 1's D = 3 Case-2 residual closes
> inside the live class**. *Proof.* Suppose `path(G) ≤ 6`. G46 gives an induced C₆; (D3-C6)
> then gives `l ≤ 3`, contradicting `l > 3`. ∎

**(D3-C6) is TIGHT, and it is tight exactly at the live class's threshold** — which is the
strongest structural evidence that it is the right statement. **Petersen** is C4-free, every
`a(v) = 3` so `l = 3` **exactly**, it contains an induced C₆ (verified: `(0,1,2,3,8,5)`), and
`path = 5`, so it has no induced P₇. Hence the strict form `l < 3` is **FALSE** and `l ≤ 3` is
best possible. *(Petersen has `diam = 2`, so it carries no 3-frame at all and does not touch
the D = 3 layer — verified.)* Above-threshold controls behave correctly: Heawood (`l = 3`),
`PG(2,3)` (`l = 4`) and `PG(2,5)` (`l = 6`) all **fail the no-P₇ hypothesis**, so (D3-C6) does
not execute on them — verified, and this is the vacuity check.

**A possibly stronger variant, also unbroken in search, registered but NOT claimed:**
> **(D3-NOP7)** *C4-free `∧` no induced P₇ `⟹` `l ≤ 3`* (the C₆ hypothesis dropped).
It is what the search below actually failed to refute; it is recorded as the more ambitious
form, and (D3-C6) is what the D = 3 layer needs.

## 27.5 **Lemma G47 (NEW, owner)** — the reduction that makes (D3-C6) tractable

> **Lemma G47.** Let `G` be connected, C4-free, with `l(G) > 3` and `path(G) ≤ 6`, and let
> `G′` be the result of iteratively deleting `a = 1` vertices to a fixpoint. Then
> **(a)** `G′` is connected and C4-free, `l(G′) > 3`, and `path(G′) ≤ 6`;
> **(b)** **no vertex of any induced C₆ of `G` is ever deleted**, so an induced C₆ of `G`
> survives intact in `G′`;
> **(c)** `μ(G′) ≥ 2`, hence `rad(G′) ≥ 2`, hence by **Theorem G+** **every** vertex `h` of
> `G′` with `a(h) ≥ 3` satisfies **`ecc(h) ≤ 3`**; in particular **`rad(G′) ≤ 3`**
> (and `diam(G′) ≤ 5` unconditionally, since every geodesic is induced).

**Proof.** (a) Deleting an `a = 1` vertex (a leaf or a triangle-leaf, F7/§12.5) preserves
connectivity and C4-freeness, does not increase `path`, and raises `Σa − 3n` by `≥ +1` — the
**corrected** peeling arithmetic of §25.4 (`+1` for a leaf, `+2` for a triangle-leaf), of
which only the `≥ +1` direction is used. So `Σa − 3n > 0` is preserved.
(b) Every vertex `z_i` of an induced C₆ has its two cycle-neighbours `z_{i−1}, z_{i+1}`
non-adjacent, so `a(z_i) ≥ 2` and `z_i` is not deletable. Inductively, as long as no C₆
vertex has been deleted every C₆ vertex still has both cycle-neighbours, hence still has
`a ≥ 2`. So no C₆ vertex is ever deleted.
(c) `μ(G′) ≥ 2` by construction. If `rad(G′) ≤ 1` there is a vertex `v` adjacent to all
others; `G′[N(v)]` is a matching (F1), so every `u ∈ N(v)` has `N(u) ⊆ {v, p}` with `p ~ v`,
giving `a(u) = 1` — contradicting `μ ≥ 2`. So `rad(G′) ≥ 2`. Now `l(G′) > 3 ⟹ Σa > 3n ⟹`
some `a(h) ≥ 4`; **Theorem G+** (§12.3) gives `path(G′) ≥ ecc(h) + 3` for **every** `h` with
`a(h) ≥ 3`, so `path ≤ 6` forces `ecc(h) ≤ 3` for every such `h`, and `rad ≤ 3`. ∎

**Machine certification** (`w133_r12_d3b.py` §G): asserted on **26** graphs meeting
"C4-free `∧` induced C₆ `∧` no induced P₇" (CE-1, CE-2, Petersen + greedy-random C4-free,
`8 ≤ n ≤ 14`), all six clauses per graph, **0 failures**.

**Why it matters.** A minimal counterexample to (D3-C6) may be assumed to have `μ ≥ 2`,
`rad ≤ 3`, `diam ≤ 5`, **and every high-a vertex within eccentricity 3** — i.e. the target
lives in a *small-radius, no-hair* world, which is exactly the world §20's machinery was
built for.

## 27.6 Numerical evidence, in the currency it actually measures

`w133_r12_d3.py` §D/§E: a randomised local search (edge add/delete hill-climbing on
`Σa − 3n`, feasibility = C4-free `∧` connected `∧` no induced P₇ `∧` induced C₆ present;
§E additionally requires a live Case-2-forced 3-frame and is seeded from CE-1/CE-2),
`n ∈ {8,10,12,14,16}`, ~900 moves per run. **Result: `max(Σa − 3n) = −4`, i.e. `max l = 2.6`
— no counterexample to (D3-C6) found.** §G's pool (which contains Petersen) attains
`Σa − 3n = 0` exactly, i.e. `l = 3`, consistent with tightness and with the target.

**Honest currency statement (the §25.6 standing rule, applied to this round's own numbers).**
Unlike round 10's frame sweeps, **these searches are about completed graphs**, which is the
right currency — `path(G)`, `l(G)` and the C₆ are all global properties of the graphs
enumerated. But the search is a **randomised local search over a bounded size range**, not an
exhaustive enumeration: it is **evidence that (D3-C6) is hard to break at `n ≤ 16`, and
nothing more**. It is not evidence of a proof, and it must never be written as such. **No SAT
was used; no large space was exhaustively enumerated.**

## 27.7 The ox-alpha VOLUME sweep — five candidate families, dispatched in parallel

Per the RESOURCES row for the ox-alpha API (VOLUME engine; quarantined output; no lease
needed), five self-contained S2 briefs were written and dispatched **in parallel**, one per
candidate-hypothesis family. Briefs: `automath-sandbox/briefs/w133_r12_D3_{A..E}.md`
(shared preamble `w133_r12_D3_PRE.md`); outputs quarantine to
`automath-sandbox/out/ox-alpha/w133_r12_D3_{A..E}.md`. All five carry the full S2 template
set: T1 competition disguise + no-internet clause, T8 persistence rider, T11 known-partial-
results preface, T12 controls (**CE-1 and CE-2 mandatory, with the "state where your argument
fails on CE-2" probe**), T12 amendment 2 (validate every exhibited graph against **every**
class constraint, most basic first), T12 amendment 3 (every delivered theorem ships an
instance satisfying **its own** hypotheses), T13 conclusion-first tag line.

| brief | family | target |
|---|---|---|
| **A** | C₆ import / **P₇-analogue of G32** | the off-hexagon structure under "no induced P₇", then **(D3-C6)** itself |
| **B** | a-value surcharge | decide `a(x) ≥ 5`, `a(u₀) ≥ 4`, `a(u₃) ≥ 3`, `a(y) ≥ 3`, `μ ≥ 3`, **plus affordability** |
| **C** | conclusion-lowering | is `path ≥ 6` the correct hypothesis-free `d = 3` statement? (both CEs attain **exactly** 6) then recover the missing `+1` |
| **D** | global mass used directly | `l > 3 ⟹ path ≥ 7` at a Case-2-forced frame; and the local surrogate for `l > 3` |
| **E** | re-rooting / frame uniformity | exploit S-1's second geodesic `u₀–x–y–u₃`; consequences of "**every** 3-frame is Case-2-forced" |

**Adjudication is owed and is NOT this round's** (dispatched near round end). **Quarantine
discipline stands: nothing from `out/ox-alpha/` enters this draft except by owner
adjudication and owner REWRITING, and ox-alpha does not count toward cross-family gates.**

## 27.8 Dispatch ledger for the planner (both items are requests, not actions)

1. **Q32 (pocket 2, `prompts/w133_r11_3CAPGLUE.md`, v4 FINAL FROZEN)** is **READY and
   untouched this round** — the READY-row freeze discipline was held; the owner did not edit
   it. **It needs a Qwen web driver; spawning is not the owner's.** Planner routes.
2. **G41/G42/G43/G44 S3 brief WRITTEN**: `prompts/w133_S3_R24.md` (v1 FINAL, FROZEN).
   Diff-scoped, self-contained. Joints: **R12-M1** (G41's redundancy claim — the gate joint
   for everything downstream, since a defect there retracts G42/G43/G44), **R12-M2** (G42's
   F3′→G41 interface, incl. the per-end orientation of "3-capped"), **R12-M3** (G43's
   truncation, triangle-leaf sub-case), **R12-M4** (G44's quantifier structure);
   **R12-B1/B2/B3** bookkeeping (W1/W2 arithmetic; the three ledger reduction claims; the
   tightness/non-vacuity annotations). Both mandatory probes attached plus a third short
   probe enforcing the §25.6 **configuration-vs-graph currency rule** against this diff's own
   certification claims. Deliverable line 2 is `MATHEMATICS DEFECT FOUND: YES | NO`.
   **AUTHORIZED and DISPATCHED (planner directive 09:2x, quota granted in-message).**
   Engine = **muse-spark-1.2 (Meta family)** as a PRECISION round — a genuinely new vendor
   family, so it satisfies the non-Qwen firewall **and** adds a cross-family vote no engine
   on file currently provides. Output → `automath-sandbox/out/muse-spark/w133_S3_R24.md`
   (quarantined; promotion by owner adjudication + REWRITING only).
   **v1 → v2 retrofit, executed before dispatch per the planner's new STANDING RULE**
   (occasioned by muse-spark's w61/Q34 report being ruled VOID as a *fluent echo report* —
   it recited every brief-printed number and fabricated everything it had to compute).
   The brief now carries the mandatory **anti-echo harness**: (a) **PART 0.5, an
   execution-environment declaration** demanded as the third line of the report
   (`EXECUTION: NONE|CODE`, with source + raw output required if CODE, and hand derivations
   required if NONE); and (b) **PART 6, eight HELD-OUT CHECKS** — values the reviewed text
   implies but the brief deliberately does **not** print, demanded as a filled table, with
   "a confidently stated wrong value voids the round; `CANNOT COMPUTE` is accepted and costs
   nothing". Rows: H1 the `L = 7` chain's exact `n`/`Σa`/`l`; H2 `|E(W2)|`; **H3/H4 the exact
   `l` of W1 + leaf and W1 + triangle-leaf** (two printed numeric values were **deleted**
   from PART 3 to create these rows); H5 an induced-P₇ witness in `PG(2,3)`; H6 G41's
   component count at `a(x) = 4` **and whether a `u₄`-kill is needed**; H7 which geodesic
   vertices are absent from G43's truncated path (answer: none — `u_d` returns as `y`);
   H8 the exact step at which `rad ≥ 5` is consumed in G42 and its weakest replacement.
   Ops honoured: `max_tokens ≥ 8000`, 2000–4000-word cap in the brief.
   **Adjudication prior recorded (planner): muse-spark is on PROBATION; w61 is running a
   held-out re-round in parallel, so this round doubles as a second independent probe of the
   same failure mode. The harness result is to be reported as its own finding, separately
   from the mathematics verdict.**
   **Gate arithmetic, pre-stated: `MATHEMATICS DEFECT FOUND: NO` ⟹ G42 and Cor G44 meet the
   promotion condition ADOPTED-pending-S3 → ADOPTED (G41 and G43 promote with them, as they
   are unconditional and are the joints under review); YES ⟹ held. The owner does not
   self-promote.**

## 27.9 Ledger after round 12

* **Pocket 1**: `D=2` G12 · **`D=3` = G37 (Case 1, ADOPTED) + Case-2-forced now REDUCED to
  (D3-C6) via G46, no longer merely REFUTED** · `D=4` G36 · `D≥5` G14/G41; then the (RP-D)
  hypothesis-discharge glue. **NOT closed** — but the D = 3 layer has a live route again.
* **Pocket 2**: unchanged this round — (3CAP) dead (G38); `rad ≥ 5` closed for `μ ≥ 2`
  (G42) and reduced to one configuration (G43/G44), all **ADOPTED-pending-S3**; residual
  (PEEL-RAD)/(FAR-2) at `rad ≥ 5` + radii 2–4. Q32 awaits a driver.
* **Owed next**: (i) adjudicate the five ox-alpha harvests (quarantined; rewrite-only
  promotion); (ii) the muse-spark S3 round on §24, if the planner grants it; (iii) own attack
  on (D3-C6) — the P₇-analogue of G32 is the named first step; (iv) Q32 dispatch.
* **No pocket closed ⟹ no milestone message on mathematics**; the two dispatch items above
  were reported to the planner immediately as resource requests.

## 27.10 Red-line self-check (round 12)

**No SAT.** Two scripts, each run to `exit 0` / **0 failures** before the prose citing it was
written (`w133_r12_d3.py`, `w133_r12_d3b.py`, both with `.out`). Everything is either explicit
construction (Petersen; Heawood = `PG(2,2)` incidence; `PG(2,3)` and `PG(2,5)` point/line
incidence, each rebuilt from scratch and **C4-freeness verified first**) or greedy-random
maximal C4-free generation plus randomised local search — **no exhaustive enumeration of a
large space**. `a(v)` is computed from the definition (independence number of `G[N(v)]` via
the matching structure). Vacuity flagged where it applies: G46's test is **non-vacuous by
construction** (9 212 real Case-2-forced frames); G47's test is non-vacuous (26 graphs in the
target class); **(D3-C6) is stated as an OPEN TARGET, not a result**, and its supporting
search is explicitly labelled bounded-range evidence about graphs, not a proof.
**One defect found and fixed in-slice, recorded**: the first version of the control builder
constructed the point/**hyperplane** incidence graph of `PG(3,2)`, which is **not C4-free**;
the assertion `c4free` caught it immediately (that is what assert-before-write is for) and the
control was replaced by `PG(2,5)` point/line incidence. Real `date` used (08:51 start).

# §28 owner-w133 round 13b (2026-08-22 10:16–10:4x CDT, opus, SHORT EXECUTION SLICE): REGISTRY execution on Q32 (**Theorem G48**, (FAR-2) REFUTED) + **Theorem G49** (bad-class `n` is UNBOUNDED) + **Theorem G50** (the 9-vertex equality instance) + the D=3 sweep salvage, adopted by rewrite

**Planner confirmation 10:2x CDT 2026-08-22, delivered via the r13b executor.** This section
executes rulings the planner confirmed on round 13's *reported-not-executed* gate arithmetic
(§ "Round 13" of `orchestration/results/w133_state.md`), plus one new certified result. The
adjudications themselves are round 13's; nothing here re-opens them.

## 28.1 REGISTRY — pocket 2, `μ = 1`: **Problem B is REFUTED, route A1 is DEAD, Problem A is single-routed on A2**

Round 13's Q32 verification is re-run at the head of this slice and **reproduces exactly**:
`problems/wowii/w133_r13_q32_verify.py` → `.out`, **exit 0, 0 failures, 22/22 checks PASS**
(the `.out` was missing on disk at round 13's close and is now committed alongside the script).

**Theorem G48 (registry-executed, owner, machine-verified).** *(FAR-2) is FALSE.* The witness
`Q32-W` — the `PG(2,4)` point/line incidence graph (42 vertices) with a 2-vertex pendant hair
`s—h_s—f_s` at each of the six vertices `S = {[1:0:0],[0:1:0],[0:0:1]}` taken both as points
and as lines — satisfies, all recomputed from the recipe and never assumed: `n = 54`, 117 edges,
**C4-free** (strong form, 0 violating pairs), connected, triangle-free, `a`-profile
`{6:6, 5:36, 2:6, 1:6}`, `Σa = 234`, `l = 13/3 > 4`, `rad = 5`, `diam = 7`; and **0 frames**
over all `(u₀,u₁,u_d)` with `dist(u₀,u_d) ≥ rad` admit a usable side-neighbour of `a ≥ 4` at
`u₀` together with `a(u_d) ≥ 2`. The configuration is **non-vacuous**: 480 cap-break frames
exist, every one of length exactly `rad = 5` with far-end `a`-value exactly 1.

| registry row | before | **after (this section)** | authority |
|---|---|---|---|
| **Problem B = (FAR-2)** | QUEUED/OPEN | **REFUTED** | Theorem G48 / `Q32-W`, verify script 22/22 |
| **route A1** (peeling cannot drop the radius) | live route to Problem A | **DEAD** | same witness: peeling the six `a=1` hairs removes exactly 12 vertices, returns the bare `PG(2,4)` incidence graph, and `rad` drops **5 → 3** while `l` stays `> 4` (`210/42 = 5`) |
| **Problem A** | OPEN, two routes {A1, A2} | **OPEN, SINGLE-ROUTED on A2** | A1 dead; A2 = the quantitative hair-exchange trade `rad(G) ≤ rad(G′) + h` is the only survivor |
| **Q32-W** | — | **named tight control for A2, an EQUALITY instance** | `h = 2`, `rad = 5`, `rad(G′) = 3`: `5 ≤ 3 + 2` holds **with equality**, so A2's inequality is TIGHT here and any proof of A2 must execute on this graph |

**Scope guard (the equivalence direction that died, and the one that did not).** Problem B was
the brief's *equivalent formulation* whose proof would have delivered Problem A. That direction
is now dead — but **Problem A is not refuted by `Q32-W`**: its named 9-path
`P0—L1—P1—L2—P2—L3—P3—L4—P4` is genuinely induced (8 consecutive incidences, **0 chords**, after
the projective renormalisation `[α:1:1] = [1:α²:α²]` which was our convention gap, not the
model's error), and an **independent DFS** that does not use the model's path at all finds an
induced path on **≥ 14** vertices — far above `rad + 4 = 9`.

**G42/G43/G44 are unaffected and in fact corroborated**: they govern the `μ ≥ 2` branch and the
reduction-to-one-configuration; `Q32-W` has `μ = 1` and *is* an instance of that one
configuration, so it shows G43/G44's reduction is **non-vacuous** rather than threatening it.

### 28.1a §24 residual map, corrected and now current

`rad ≥ 5` splits as:
* `μ ≥ 2` — **CLOSED** (Theorem G42).
* `μ = 1` — **OPEN**, and by G43/G44 it is **one configuration**. Inside it the sub-routes are
  now **{B: dead (G48) · A1: dead (G48) · A2: live, and tight-controlled by `Q32-W`}**.

Residual pocket 2 overall = this one `μ = 1` configuration at `rad ≥ 5`, plus **radii 2–4**
(`rad = 4` additionally wanting the `a(u₀) ≥ 3` upgrade).

### 28.1b **DEBT ROW** — **DISCHARGED at round 17 (2026-08-22 21:4x CDT), see §30**

| id | debt | owed since | discharge condition |
|---|---|---|---|
| **DEBT-1** | The **entire pocket-2 §24 material is not in `papers/wowii133/main.tex`** — G42/G43/G44, the residual map of §28.1a, and now Theorem G48 with `Q32-W` all live only in this draft. | round 11 (§24), re-owed at round 13 | an **engine-rewrite pass** that inserts the §24 + §28.1 block into `main.tex` with the witness recipe, the residual-map table, and the A2 tightness statement. Deliberately NOT hand-written here: this slice is execution-only, and a hand insertion would fork the .tex against the draft. |

## 28.2 **Theorem G49 (NEW, owner, machine-certified): `n` is UNBOUNDED in the bad class — so no route can come from bounding `n`**

Round 13 FLAGGED this and withheld it from the registry because it was a *derivation*, not a
verification. The planner adopted item 8; the certification is now written and run.

**Script `problems/wowii/w133_r13b_unbounded.py` → `.out`, exit 0, 0 failures.**

**Statement.** Let `F_k` be CE-2 with `k` pendant triangles attached at vertex `2` (each pendant
triangle = two new vertices `p, q` with edges `2–p`, `2–q`, `p–q`). Then for every `k` certified
(`k = 0 … 10`; the brief asked for `0 … 6`, extended to 10 as it was cheap):

* `F_k` is **C4-free** (strong form: no two vertices with ≥ 2 common neighbours) and connected;
* `n(F_k) = 10 + 2k` and `Σa(F_k) = 25 + 3k`, so `l(F_k) = (25+3k)/(10+2k)`;
* **`path(F_k) = 6` EXACTLY** — and this is certified as **two separate facts**, `path ≥ 6` TRUE
  and `path ≥ 7` FALSE. *(Deliberate: the single error family that killed `D3_A` and `D3_C` in
  round 13 was miscounting the vertices of an induced path built from an induced cycle. A
  one-sided check would not have caught it.)*
* **both** of CE-2's 3-frames, `(2,1,0,8; x=3)` and `(2,6,4,8; x=3)`, survive in `F_k` and stay
  **Case-2-forced**; `F_k` has exactly 2 three-frames throughout.
* `l` is **strictly decreasing** in `k`, with `sup = l(0) = 5/2`, and the exact identity
  `l(k) − 3/2 = 10/(10+2k)`, so `l ↓ 3/2` from above. In particular **`l(F_k) < 5/2 < 3` for
  every `k`.**

The seed is re-verified from its own edge list at the head of the script (CE-2: `n = 10`,
C4-free, connected, `Σa = 25`, `path = 6`, exactly the two named Case-2-forced frames).

**Consequences, registered.**
* **E3(i) is answered NO**: `n` is unbounded in the bad class (C4-free + a Case-2-forced 3-frame
  + `path = 6`).
* **E3(iii)**: the infinite family exists, explicitly.
* **STRATEGIC CONSEQUENCE — this is the load-bearing half.** **No route to (T-C+)/(T-D) can
  proceed by bounding `n`.** Every surviving route must come through the hypothesis **`l > 3`**.
  The family does not threaten that hypothesis — it sits strictly *below* the `l > 3` line for
  every `k` — which is precisely why it kills the `n`-route while leaving the `l`-route intact.
  Any future brief on this line that proposes an `n`-bound is **dead on arrival** and should be
  refused at dispatch time, not at adjudication time.

## 28.3 D=3 sweep salvage — **adopted by rewrite** (5 items), exactly as triaged in round 13

Round 13's verdict stands: **0 of 4 landed reports adopted as written.** The following are
adopted **only in the rewritten form given here**; the reports' own proofs of them are not
usable, and no report's headline is adopted.

**S1 — `D3_A` / Lemma L4 (fan rigidity).** SOUND as proved; the only genuinely new content in
that report. Adopted with its tightness instance **replaced**: the report's instance takes
`h = w` from L3's graph, but that `w` has two `Z`-neighbours, so `w ∈ W_cons`, not `F`, violating
L4's own hypothesis `N(h) ∩ Z = {z₀}` (Rule 3 breach). **Valid instance: CE-2 with `h = 6`.**

**S2 — `D3_A` / Lemma L2's STATEMENT (`|W_cons| ≤ 3`), with a new proof.** The report's argument is
defective (it calls the two **endpoints** of a P7 "not a non-consecutive pair"; they are). The
one-line repair it missed: `ww′ ∈ E` is impossible by **C4-freeness**, via the 4-cycle
`w–z_i–z_{i+1}–w′`. Adopted with that proof, not the report's.
*Not adopted:* L1 (`|A| ≤ 1`) is **FALSE** — the correct bound is `|A| ≤ 3`, attained; and the
report's "no instance with `|W_cons| = 3` was found" is a **search failure**, not an absence.

**S3 — `D3_C`'s 9-vertex graph `R`, restated with corrected statistics. Theorem G50 (NEW).**
Independently re-verified in this slice from the report's own edge list
`0-1, 1-2, 2-3, 0-4, 4-5, 5-3, 4-6, 4-7, 0-8`:

| quantity | **verified value** | the report's claim |
|---|---|---|
| `n` | **9** | 9 ✓ |
| C4-free | **yes** | yes ✓ |
| `a`-profile | **`[3,2,2,2,4,2,1,1,1]`**, `Σa = 18`, `l = 2` | uncredited |
| geodesic | `0–1–2–3`, `dist(0,3) = 3` | ✓ |
| `a(u₀) = a(0)`, `a(u₃) = a(3)` | **3, 2** | ✓ |
| side-neighbour `x` | **`x = 4`**, `a(4) = 4`, outside `comp₀(1) = {1}` | ✓ |
| usable far-side set | **exactly `{5}`**, and `5 ~ 4` ⟹ **Case-2-FORCED** | ✓ |
| **`path(R)`** | **6** | **7 — FALSE** |
| its exhibited 7-path `6–4–5–3–2–1–0` | contains the **chord `4–0`** | claimed *"the sole 'long' edge 0–4 has both endpoints off this path"* — **both endpoints are ON it** |

**Theorem G50.** `R` is a **9-vertex equality instance**: C4-free, carrying a Case-2-forced
3-frame, with `path = 6`. It therefore **REFUTES `D3_C`'s own Conjecture 2.2** (*"every C4-free
graph carrying a Case-2-forced 3-frame with `path(G) = 6` has `n ≥ 10`"*) and **beats both CE-1
and CE-2 (`n = 10`)** as the smallest equality witness on file. The report's Proposition 2.1
(`n ≥ 9`) is consistent with this and is now **ATTAINED**. Adopted **only** in this form: the
report's own reading of `R` is wrong in the same sentence in which it states it.
*Not adopted:* the (T-C) headline. Case 2 of its proof gives `path ≥ 5`, one short of the
target (an induced `C6`'s longest induced path is **5 vertices**, not 6), and Lemma 2.3 is
FALSE — refuted by the report's **own** certified control CE-1, on which three outside vertices
have exactly one neighbour in the named `S` while `path(CE-1) = 6 < 7`. **(T-C) is OPEN: neither
proved nor refuted.**

**S4 — `D3_D` / Theorem A + Corollary B in its CORRECTED form.** Theorem A (*C4-free + a
dominating edge ⟹ `Σa ≤ 2n − 2`*, tight on the double star, connectivity not needed) is sound.
Corollary B is adopted as **`Σa = 3n − 3 − e(G)`**, not the report's `3n − 3 − e(G−r)` — the
report's own `K₁,₃` instance refutes its stated form (9 vs the true 6). **Value declared
honestly: these eliminate an ALREADY-EMPTY branch.** By Theorem A itself a dominating edge
forces `l ≤ 2 − 2/n < 3`, so the hypothesis can never meet `l > 3`; a dominating vertex gives
`diam ≤ 2`, killing the geodesic outright. Confirmed empirically: **0 frames in 4 000 trials /
630 random C4-free graphs**. **Coverage of (T-D): ZERO.**
*Not adopted, and flagged as a hazard for future briefs:* the report's Bacsó–Tuza quotation is
**wrong** (it uses *"dominating set inducing a clique or a `P_{t−2}`"*; the true theorem gives a
connected dominating set inducing a `P_{t−2}`-**free** graph). **Petersen refutes the misquote**
— connected, C4-free, longest induced path 5 (hence P7-free), **no** dominating clique and
**no** dominating induced P5. Lemma C (the "P6-shadow") is also FALSE (counterexample, C4-free,
`n = 9`: `0-1,1-2,2-3,3-4,4-5,6-0,6-3,6-7,7-8`).

**S5 — `D3_E` / Theorem A + Corollary C(i)** (*in a bad-class graph, every neighbour of `u₀`
outside `comp(u₁) ∪ comp(x)` has `a`-value ≤ 3*). Sound — 0 counterexamples over 397
Case-2-forced frames — and adopted by rewrite, with the honest billing round 13 attached: it is
a **two-line contrapositive of F4**, not a new mechanism.
*Not adopted:* Prop. 1.5 (*"the re-rooted frame is never Case-2-forced"*) is **FALSE** and is
killed by the report's **own** §2 instance — re-rooted frame `(2,5,0,9)` with `x′ = 6` has
unique usable far-side vertex `{4}` and `4 ~ 6`, so it **is** Case-2-forced; a randomised audit
found **14 of 19** sampled re-rooted frames Case-2-forced. Its "certified instance" is real but
certifies the wrong thing (`path = 7`, so **not** in the bad class; `l = 29/15 ≈ 1.93`).

### 28.3a Standing brief-design rule proposed to the planner (from round 13's cross-cutting finding)

`D3_A` and `D3_C` died of the **same** error family, and it is **not** the "invert a
non-bijective map" family the methodology tail predicted. It is **miscounting the vertices of an
induced path built from an induced cycle** — walking all `k` vertices of an induced `C_k` and
forgetting the closing edge `u_i ~ u_{i+k−1}`. Every defect above is an instance.
**Proposed rule:** any attack brief whose facts include a *"this configuration induces a `C_k`"*
lemma must print the reminder *"an induced `C_k` contains a longest induced path on `k − 1`
VERTICES, not `k`"*, and adjudication should check **cycle-to-path steps FIRST** on such briefs
— they are now the cheapest kill on this line, ahead of the inversion check.

## 28.4 Dispatch executed this slice

**muse §24 v4** — plain resubmit of the v2 brief (`briefs/w133_S3_R24_v2.md`, 25 013 B) at
`max_tokens = 64000`, `timeout = 1500 s`, via the **patched** `scripts/engine_call_big.sh`
(key now passed through a `mktemp` 0600 header file consumed by `curl -H @file`, closing the
`ps`-argv key exposure flagged in round 13 — **the script was not modified by this slice**).
Output `out/muse-spark/w133_S3_R24_v4_out.md`, backgrounded, log
`out/muse-spark/w133_S3_R24_v4.log`. Rationale, from round 13: v3 was a provider-side **500 with
zero tokens generated** (preserved reasoning trace `(none)`), so raising the budget cannot fix
*that* failure and a plain resubmit is correct — but v3 was also dispatched at only **16 000**
against a 25 KB brief, below this project's measured burn threshold, so the resubmit must
*also* carry the larger budget. **Conflict flagged, not resolved by this slice:**
`orchestration/RESOURCES.md` line 14 records a 09:5x measurement that the muse gateway returns
500 on 64 k and recommends 16 k — yet v3 **at 16 k** is the call that 500'd. The two data points
are inconsistent; the planner's 64 k ruling was executed as given, and whichever way v4 lands is
the tiebreak.

## 28.5 Ledger after round 13b

* **Pocket 1**: `D=2` G12 · `D=3` = G37 (Case 1) + Case-2-forced reduced to (D3-C6) via G46 ·
  `D=4` G36 · `D≥5` G14/G41; then the (RP-D) glue. **NOT closed.** New this slice: the
  `n`-bounding route into (T-C+)/(T-D) is **eliminated** (G49); (T-C) is **OPEN**, not proved
  (`D3_C`'s claim retracted); the smallest known equality witness is now `n = 9` (G50).
* **Pocket 2**: `rad ≥ 5` CLOSED for `μ ≥ 2` (G42), reduced to one configuration for `μ = 1`
  (G43/G44) — and inside `μ = 1`, **Problem B and route A1 are now REFUTED (G48)** and Problem A
  is single-routed on **A2**, with `Q32-W` as its tight equality control. Residual = that one
  configuration + radii 2–4. **NOT closed.**
* **Owed next**: (i) **DEBT-1**, the `main.tex` insertion, by engine rewrite; (ii) adjudicate
  muse §24 v4 when it lands, and `D3_B` / `P7G32` retries; (iii) an own attack on **A2** — it is
  now the *only* live route in pocket 2's `μ = 1` branch and it has a named tight control, which
  is the best-specified target on the board; (iv) fold the five rewritten salvage items into the
  fact base.
* **No pocket closed ⟹ no mathematics milestone this slice.** The slice's hard content is one
  **refutation** executed into the registry (G48) and two **new certified results** (G49, G50).

## 28.6 Red-line self-check (round 13b)

**No SAT.** Two scripts run to **exit 0 / 0 failures** before any prose citing them was written:
`w133_r13_q32_verify.py` (re-run this slice, 22/22 PASS, `.out` now committed) and the new
`w133_r13b_unbounded.py` (`.out` committed). Every graph in the new script is **rebuilt from an
edge list here** and **C4-freeness is checked BEFORE any statistic is read off it**; no
engine-supplied adjacency, `a`-value, distance or path count is trusted anywhere. `path` is
certified as a **two-sided** fact (`≥ 6` yes, `≥ 7` no) specifically to defeat round 13's
identified error family. `D3_C`'s graph `R` was likewise recomputed from its edge list before
its corrected statistics were tabled in §28.3. One over-tight assertion of the executor's own
(a numerical guess at how fast `l ↓ 3/2`) **failed on first run and was replaced by the exact
identity `l(k) − 3/2 = 10/(10+2k)`** — recorded because assert-before-write is what caught it.
No registry row was self-promoted: every move in §28.1 is the planner's confirmed ruling
(10:2x CDT 08-22), executed, not decided, here. `DEBT-1` is recorded as owed rather than
quietly discharged. No browser was used and the Chrome lease was not touched. **No API key was
echoed**, and the patched `engine_call_big.sh` was used **unmodified**. Real `date` used
(10:16 start).

---

# §29 owner-w133 round 15 (2026-08-22 20:2x–20:3x CDT, opus, DISPATCH + REWRITE SLICE): REGISTRY — **G41, G42, G43, Corollary G44 are ADOPTED**; `D3_B`'s three rewrite-survivors entered as NEW statements; the corrected `|W_cons| ≤ 3` bound recorded UNREGISTERED

**§29.1 executes a registry action decided by the planner; it contains no new mathematics and
G41–G44's proof text is untouched.** §29.2 contains three statements that are new to this
draft. §29.3 records a bound deliberately **not** entered in the registry.

Machine product for this section: `problems/wowii/w133_r15_key.py` → `.out`, **exit 0,
42 checks, 0 failures**, run to completion before any prose here cites it.

## 29.1 REGISTRY — ADOPTED-pending-S3 → **ADOPTED** for G41, G42, G43, Cor G44

**Planner certification: `orchestration/planner_msgs/cert_w133_r14.md`, ruling CERT-1
(planner v4, 2026-08-22 20:3x CDT).** The owner does not self-promote; this section executes
a decision, it does not make one.

* **Rows promoted.** **Theorem G42** (§24.2d) and **Corollary G44** (§24.2e) move
  ADOPTED-pending-S3 → **ADOPTED**; **Lemma G41** (§24.2c) and **Lemma G43** (§24.2e), which
  §24 recorded as unconditional but under the same S3 review, are **ADOPTED** with them.
  This completes the promotion that §26.1's scope guard explicitly deferred ("**Theorem G42**
  and **Corollary G44** … are **not** ruled on by this executor … and remain
  **ADOPTED-pending-S3** until confirmed"). That deferral is now discharged.
* **Basis.** The S3 round `out/muse-spark/w133_S3_R24_v5_callA.md` + `_callB.md`
  (Meta family, brief `prompts/w133_S3_R24.md` v2): **held-out void gate PASS** — 7 stated
  rows, 7 correct, plus one honest `CANNOT COMPUTE` on H5, which under this project's rule is
  not a void — and gate bit **`MATHEMATICS DEFECT FOUND: NO`** with **R12-M1..M4 all CLEAN**.
  Adjudicated in `orchestration/results/w133_state.md` §"Round 14" §1–§4.

**The pre-registration, written out here so the audit trail survives without the planner's
message.** This is the check that actually licenses the promotion, and it is the reason the
promotion is not circular:

| step | artefact | timestamp |
|---|---|---|
| gate condition stated **in advance**, blind | `orchestration/results/w133_state.md:632-634`, inside the **Round 12** block | round 12 ran **08:51–09:5x CDT 2026-08-22**; planner-confirmed at the time |
| the round it gates was generated | muse-spark v5 split call (callA + callB) | **10:54–10:56 CDT 2026-08-22** |
| gate bit returned, void gate run | round 14 | 20:06–20:2x CDT 2026-08-22 |
| certification | CERT-1 | 20:3x CDT 2026-08-22 |

The condition therefore predates the result by roughly an hour and was never edited
afterwards. Independently of the owner, the planner re-derived `path(Petersen) = 5` from
scratch and re-ran the held-out product (59 checks, 0 failures) before certifying.

* **Scope guard — what this does NOT do.** It moves **status**, not reach. The four
  statements say exactly what §24.2c–e says they say; pocket 2's `μ = 1` branch is untouched
  and **no pocket closes**. It also does **not** reach **PROVED-S3**: that bar is **≥ 2
  adversarial rounds, cross-model**, and each of G41/G42/G43/G44 holds **exactly one** clean
  cross-family round (Meta). ox-alpha counts toward no family bar while its lab identity is
  unknown. The **second** round was dispatched this slice to **Qwen web** (planner
  designation, CERT-2), brief `prompts/w133_S3_R24_v6_qwen.md`, with its gate **pre-registered
  before dispatch** in the round-15 block of the state file. Until that lands and is certified,
  the correct status of all four is **ADOPTED**, not PROVED-S3.
* **Every other status-line site** that mentions the pending state (§24.2d, §24.2e, §24.4,
  §26.1's scope guard, §28.5, and the mirrored entries in
  `orchestration/results/w133_state.md`) is to be read as pointing here.

## 29.2 `D3_B` salvage — three survivors, entered as **NEW statements**, each with its own status

**Provenance and the rule that governs it.** The parent report
(`out/ox-alpha/w133_r12_D3_B_out.md`) was adjudicated **REFUTED** in the round-14 addendum:
its headline is false, its Theorem B1 is refuted by its own supplied instance (the
construction walks 13 pairs and silently skips `(x, y)`, which F6/G46 declares to be an
**edge**), its Lemma R is false, and its B2 is false. **Nothing in it is adopted as written.**

Per planner ruling **CERT-3** and template law **T1a** (`prompts/templates.md`, installed
2026-08-22): *a statement salvaged out of a refuted parent is a **NEW statement**. It inherits
none of the parent's evidence and carries its own independent proof obligation.* Accordingly
each of the three below is **rewritten here from the ledger's adjudicated content, never
copied from the sandbox**, is stated in this project's notation, and carries **its own
separate status line**. They do not share one status.

**T1a's second half applies too, and is recorded here once for all three:** a rewritten
statement *"must go through its own S3 rounds (T3) from scratch, exactly as if it had been
proposed cold."* **None of G51, G52, G53 has had any S3 round.** "Proof obligation DISCHARGED"
below means only that the owner's own rewritten proof stands on its own feet and owes the
parent nothing — it does **not** mean adversarially reviewed, and none of the three may be
cited as PROVED or counted toward any cross-family bar. They are candidates for a future
§-diff.

### 29.2.1 **Lemma G51 (NEW, owner-rewritten)** — in a Case-2-forced 3-frame, `a(u₃) = 2` exactly

> **Lemma G51.** Let `G` be C4-free and let `(u₀u₁u₂u₃; x, y)` be a **Case-2-forced 3-frame**:
> `u₀u₁u₂u₃` a geodesic, `x` a usable side-neighbour of `u₀`, `a(u₃) ≥ 2`, and **every** usable
> side-neighbour of `u₃` adjacent to `x`. Then **`a(u₃) = 2`**, and the unique component of
> `G[N(u₃)]` other than `u₂`'s is the **singleton** `{y}`.

**Proof (rewritten).** Let `U` be the set of usable side-neighbours of `u₃`, i.e. the union of
the components of `G[N(u₃)]` other than `u₂`'s. By F1, C4-freeness makes `G[N(u₃)]` a matching
plus isolated vertices with exactly `a(u₃)` components, so `U` is a union of `a(u₃) − 1`
non-empty components and hence `|U| ≥ a(u₃) − 1`. Case-2-forcing gives `U ⊆ N(x)`, and
`U ⊆ N(u₃)` by definition, so `U ⊆ N(x) ∩ N(u₃)`. Now `x ≠ u₃` (indeed `dist(u₀,x) = 1` while
`dist(u₀,u₃) = 3`), so C4-freeness bounds `|N(x) ∩ N(u₃)| ≤ 1`. Hence `|U| ≤ 1`, so
`a(u₃) − 1 ≤ 1`. With `a(u₃) ≥ 2` this forces `a(u₃) = 2`, and `|U| = 1` makes the non-`u₂`
component the singleton `{y}`. ∎

**Status: ADOPTED-BY-REWRITE, proof obligation DISCHARGED HERE.** New statement under T1a;
inherits nothing from `D3_B`. Its proof above is the owner's, uses only F1 and C4-freeness,
and is independent of every step the parent got wrong. It is also **consistent with, and
strictly sharper than**, the round-10 owner sharpening recorded at §23.1.5 / state-file item 5
(*the usable-far set of a Case-2-forced frame is exactly `{y}`*, machine-asserted on all 1 112
Case-2-forced frames) — G51 is the a-value statement that observation implies. **Not yet
S3-reviewed**; it is a candidate for the next §-diff, not a certified result.

### 29.2.2 **Lemma G52 (NEW, owner-rewritten)** — `a(u₃) ≥ 3` escapes Case 2, and the converse is FALSE

> **Lemma G52 (i).** In any 3-frame `(u₀u₁u₂u₃; x)` of a C4-free graph with `a(u₃) ≥ 3`, some
> usable side-neighbour `y` of `u₃` satisfies **`y ≁ x`** — i.e. the frame is **not**
> Case-2-forced, so **G37's extra hypothesis is available and `path(G) ≥ 7`** whenever G37's
> remaining hypotheses hold.
> **Lemma G52 (ii) — the converse fails.** `a(u₃) ≥ 3` is **sufficient but NOT necessary**
> for escaping Case 2.

**Proof of (i) (rewritten).** Immediate from G51 by contraposition: a Case-2-forced 3-frame
has `a(u₃) = 2`, so `a(u₃) ≥ 3` is incompatible with Case-2-forcing. Directly: with
`a(u₃) ≥ 3` the set `U` of usable side-neighbours meets at least two distinct components of
`G[N(u₃)]`, so `|U| ≥ 2`; if every element of `U` were adjacent to `x` then
`|N(x) ∩ N(u₃)| ≥ 2`, a C4. ∎

**Proof of (ii) — an explicit instance.** The graph `Z` on `{0,…,9}` with edges
`0-1, 1-2, 2-3, 3-4, 0-5, 0-6, 5-7, 5-8, 5-9` (write `u₀=0, u₁=1, u₂=2, u₃=3, y=4, x=5`).
Machine-verified in `w133_r15_key.py` §[G], **C4-freeness asserted before any statistic**:
`Z` is C4-free and connected; `0–1–2–3` is a geodesic (`dist(0,3) = 3`); `a(u₀) = 3`;
`x = 5` is a **usable** side-neighbour of `u₀` with **`a(x) = 4`**, so the full a-value package
`a(u₀) ≥ 3, a(u₃) ≥ 2, a(x) ≥ 4` that this project's 3-frames carry is satisfied;
`a(u₃) = 2` **exactly**; `y = 4` is a usable side-neighbour of `u₃` with **`y ≁ x`**. So the
frame **escapes Case 2 with `a(u₃) = 2 < 3`**. (`path(Z) = 7`, so there is no conflict with
G37.) ∎

**Status: (i) ADOPTED-BY-REWRITE, proof obligation DISCHARGED HERE. (ii) is an owner
REFUTATION, registered here as a correction, not as a salvage.** New statements under T1a;
they inherit nothing from `D3_B`. **This is a substantive departure from the parent and from
this owner's own round-14 summary of it.** The round-14 addendum recorded survivor S2 as
carrying "the clean dichotomy *`a(u₃) ≥ 3` **is equivalent to** escaping Case 2*". That
phrasing is the parent's, it was passed through in the summary, and **the ⟸ direction is
false** — which is exactly what T1a's independent-proof-obligation rule exists to catch, and
it was caught on the first attempt to write the statement down. What enters this draft is the
one-directional form. *(The parent's other S2 content — its Theorem B3 with a re-verified
instance — is subsumed: B3's conclusion `path ≥ 7` is G37 applied through G52(i), and G37 is
ADOPTED (§26.1). No separate registration is warranted and none is made.)*

### 29.2.3 **Lemma G53 (NEW, owner-rewritten)** — `μ(G) ≥ 3` makes every 3-frame Case-1

> **Lemma G53.** Let `G` be C4-free with `μ(G) ≥ 3`. Then **no** 3-frame of `G` is
> Case-2-forced; every 3-frame satisfies G37's extra hypothesis.

**Proof (rewritten).** `μ(G) ≥ 3` means `a(v) ≥ 3` for every vertex, in particular
`a(u₃) ≥ 3`; apply G52(i). ∎

**Status: ADOPTED-BY-REWRITE, proof obligation DISCHARGED HERE — but recorded together with
its own affordability caveat, which is what makes it nearly worthless.** New statement under
T1a. It is a one-line corollary of G52(i), and the parent's error here was **directional**:
it filed this as "Open" and then asserted that it *subsumes* the parent's B2 and B4, inverting
the implication. **The caveat, from §27.3's kill table:** `μ ≥ 3` is **NOT affordable** in the
live class — peeling reaches only `μ ≥ 2`, and `μ ≥ 2` was already refuted as a repair at
`d = 3` by CE-2 (Theorem G45, §25.3). So G53 is true, cheap, and buys the live class nothing;
it is registered for completeness and explicitly **not** proposed as the D = 3 layer's new
hypothesis. **Non-vacuity**: the class `{C4-free, μ ≥ 3, carries 3-frames}` is inhabited — the
`PG(2,3)` incidence graph has `a(v) = 4` for every `v` and carries 3-frames (§23.1.6).

## 29.3 The corrected `|W_cons| ≤ 3` bound — **OWNER-DERIVED / UNREGISTERED**, queued for an engine round

**Planner ruling CERT-4: this is recorded, and deliberately NOT registered as a theorem.**

*Setting* (the `P7G32` brief, PART 3 Problem 1): `G` C4-free, `Z = (z₀,…,z₅)` an induced
6-cycle, `G` has **no induced P7**, and
`W_cons := { w ∉ Z : w has exactly two Z-neighbours, and they are consecutive }`.

* **The statement.** `|W_cons| ≤ 3`, with the bound **attained**, the tight instance placing the
  three `W_cons`-vertices on the three pairwise-disjoint slots `{z₀,z₁}`, `{z₂,z₃}`, `{z₄,z₅}` —
  recorded here as **slots {0, 2, 4}**.
* **What it replaced.** It is the corrected form of the `P7G32` report's `|W_cons| = 6` corollary,
  which was **machine-refuted** during the round-14 addendum, together with that report's
  Claims 3/4 and its external-neighbour statement (each refuted by an explicit C4-free
  8-vertex graph).
* **Status: OWNER-DERIVED / UNREGISTERED.** It was derived on the Claude side inside a
  **VERIFY-ONLY** slice, and VERIFY-ONLY does not license owner-side attack results into the
  ledger as adopted mathematics. This is a **deferral of registration, not a doubt about the
  derivation** (CERT-4's own words). It is **not** a theorem of this project, must not be
  cited as one, and nothing in §24, §27 or §28 depends on it.
* **Queued as a target for a future engine round**, and it inherits the standing re-dispatch
  note: the `P7G32` brief itself needs a fresh engine and a **rebuilt held-out table**, because
  its current rows are burned — their answers are on the ledger — and the round it did receive
  was ruled **VOID** (`path(Petersen)` stated as 6, true value 5, with a fabricated witness).

## 29.4 DEBT-1 — **DISCHARGED at round 17, see §30**; what §29.1 changed about it

`§24` and `§28.1` are still absent from `papers/wowii133/main.tex`. **Not hand-inserted, by
standing instruction; it remains queued for an engine rewrite pass.** One line on what changed:
**the promotion in §29.1 changes the status words that pass must carry, and nothing else** —
G41/G42/G43/G44 are to be written into `main.tex` as **ADOPTED** (not "ADOPTED-pending-S3", not
"PROVED"), and the pass must also carry the round-14 editorial requirement R12-B3(i): the §24
tightness prose prints `path_constructed = 9 = rad + 4` and `path(W2) ≥ 168` as **two separate
numbers**, never as one tightness claim. No proof text changes.

## 29.5 Red-line self-check (round 15)

**No SAT.** One script, one product: `problems/wowii/w133_r15_key.py` → `.out`, **exit 0,
42 checks, 0 failures**, run to completion **before** any prose citing it. No exhaustive search
of a large space: the largest searches are an exact longest-induced-path by subset enumeration
on `n = 13` (`2^13 = 8192` subsets) and a **node-capped** (4 000 000) two-sided induced-path
DFS on a **26-vertex** graph, which terminated **without hitting the cap in either direction**;
everything else is rebuild-and-measure on `n ≤ 660`. Every graph is rebuilt from a recipe or
from an edge list constructed in the file, and **C4-freeness is asserted before any statistic
is read off it**; no engine-supplied adjacency, `a`-value, distance or path count is trusted.
**Two of the owner's own assertions fired on first run and are recorded rather than quietly
repaired**: (a) round-14's `indep_number` cap of `|S| ≤ 8` fired on *W1 + three leaves at the
same attachment vertex* (degree 10) and was raised to 12 with the reason written into the
source; (b) the first bespoke-graph construction assumed some two-step circulant `C13(1,k)`
would be C4-free — **none is**, since `i` and `i+k+1` always share the two neighbours `i+1`
and `i+k`, and the guarding assertion caught it before any statistic was published. The
replacement graph is the deterministic greedy C4-free closure of `C13`.
**No registry row is self-promoted**: §29.1 executes the planner's CERT-1, and the four
statements' PROVED-S3 move is explicitly **withheld** pending a second round that was
dispatched, not assumed. **§29.2's three statements are entered as NEW under T1a**, each with
its own status line, none inheriting the refuted parent's evidence — and writing them down
under that rule **caught a false half of a claim this owner had itself passed through in the
round-14 summary** (§29.2.2 (ii)). **§29.3 is recorded UNREGISTERED**, as ruled. **DEBT-1 is
recorded as owed, not quietly discharged.** Engine output stayed in the sandbox; nothing was
promoted by copying, and the three survivors were **rewritten from the ledger**, never copied
from `automath-sandbox/`. Chrome lease taken 20:31 and released 20:33 CDT, logged both ways in
`orchestration/RESOURCES.md`; no verification UI was touched and no pre-existing tab was
disturbed. **No API key was echoed** and no process listing with command lines was run. Real
`date` used throughout (20:2x start, 20:33 release).


---

# ROUND 17 (2026-08-22 21:2x–21:4x CDT, owner-w133, opus) — DEBT-1 DISCHARGED; W2 DOUBLE-SOURCED

Full record: `orchestration/results/w133_state.md` §"Round 17", which is the authority. Two
things belong in this draft because they change rows here.

## 30.1 DEBT-1 (§28.1b, §29.4) is **CLOSED**

`papers/wowii133/main.tex` now carries §24 + §28.1 as a new section, *The band `⌊l⌋ ≥ 4` at
large radius* (`\label{sec:pocket2}`), compiled clean (tectonic, exit 0, no undefined
references). Route as ruled: **engine rewrite pass → adjudication → promotion by rewrite.**
Brief `automath-sandbox/briefs/w133_r17_tex_pocket2.md` → ox-alpha →
`out/ox-alpha/w133_r17_tex_pocket2_out.md`; **six defects found and repaired in the rewrite**
(a mangled `\ne`, a non-existent `\dist` macro, an obsolete "three sampled vertices", a held-
then-verified `l` pair, internal jargon, and a wrong table pointer), plus one substantive
correction the engine got wrong: it cited **G11** for `l > 4` preservation under peeling, which
G11 does not say — G11 is the `Σ − 3n` slack. The paper cites **G6** for connectivity and
C4-freeness and derives the `Σ − 4n` direction explicitly.

Status words carried: G41/G42/G43/G44 are rendered at the paper's **`\REV{}`** tier, whose
definition in `sec:conventions` is *two-family adversarial review* — i.e. exactly PROVED-S3.
**The word "PROVED" appears nowhere in the file.** R12-B3(i)'s two-numbers fix is
`Remark~rem:twonumbers`; B3's non-exhibition caveat is `Remark~rem:nonexhibited`, printed as
its own numbered remark and lifted again into the open-problems section.

## 30.2 **W2 is double-sourced** — planner RULING 3's open half is closed

`problems/wowii/w133_r17_w2_recompute.py` → `.out`, exit 0, 32 checks, 0 failures. `PSL(2,11)`
rebuilt as a **permutation group on `P^1(GF(11))`** under the Möbius action — no code and no
model shared with the matrix-model scripts, faithfulness checked (`|image| = 660`, not 1320).
Every W2 quantity reproduced: `n = 660`, 6-regular, 1980 edges, triangle-free, C4-free (strong
form), `l = 6`, `μ = 6`, `rad = diam = 5`, constructed path `9 = rad+4`. Two are **strengthened**:
eccentricity 5 is verified at **all 660 vertices** (round 11 sampled three), and the certified
induced path reaches **192** vertices, not 168. The paper keeps 168 as the recorded bound and
reports 192 as the independent recomputation's own finding.

`Q32-W` remains **single-sourced** (`w133_r13_q32_verify.py` only). That is now **stated in the
paper** (`Remark~rem:pocket2prov`) rather than left to the ledger, together with the explicit
warning that the `\REV{}` review tier is about reading proofs and does not extend to
computations.

## 30.3 V7 self-sweep (planner RULING L) — a self-satisfied invariant found in our own file

`problems/wowii/w133_r17_v7probe.py` → `.out`, exit 0, **6/6 injected faults trip the assertion
they target**. Found and repaired in this owner's own round-17 script: `check(6 > 4, ...)`, a
comparison of two literals, unfalsifiable under any input. Two further checks declared
SELF-SATISFIED and six DERIVED. One probe **failed to trip and is reported as a finding**: the
first two generators already generate `PSL(2,11)`, so dropping the third is not a fault for the
group-order predicate (it is not redundant for the graph, and no W2 number moves).

# 31. Round 19 — the (T-C) survivors: null audit, proof status, and the DEBT-4 registry entry

## 31.1 The null-model audit the planner gated numbering on (RULING T)

`problems/wowii/w133_r19_null.py` → `.out`, exit 0, **22 checks, 0 failures**. It rebuilds `R`,
CE-2 and Petersen from edge lists, re-derives the round-18 scan independently, and prices it.

**What the scan actually is.** 15 induced C₆s (R: 1, CE-2: 4, Petersen: 10) and **M = 59**
off-cycle `(Z, w)` pairs. Trace sizes `|N(w) ∩ Z|`: **{0: 10, 1: 9, 2: 40}** — so **40 of 59
pairs (67.8 %) could in principle have violated**, and among the 40 two-element traces the
cycle-distance classes realised are **{consecutive: 4, opposite: 36}**.

**The answer, stated in the only null model that matches the population sampled.** Every graph
in the scan is **C4-free**, and inside C4-free graphs the statement is a **theorem**. Therefore

> **the fraction of same-shape random configurations that also show 0 violations is 1.000000 —
> 100 %. The evidence weight of "15 induced C₆s, 0 violations" is exactly 0 bits.**

This is the same verdict the project's own 745 424-object null audit reached, reached the same
way. **The instance check is a transcription-and-code check, not evidence**, and no statement
below is numbered on its strength.

**What the number would have been had the class hypothesis been dropped** (recorded so the
figure is not mistaken for "the check was worthless in every sense"): uniform random trace,
16/64 non-violating per pair ⟹ `P = 3.0 × 10⁻³⁶`; size-matched resample ⟹ `1.3 × 10⁻⁹`;
density-matched Bernoulli (`p = 0.2514`) ⟹ `1.6 × 10⁻⁹`. Those numbers price a population the
scan never sampled.

**A defect sharper than the null.** Of the 8 candidate classifications of an allowed 2-trace
(subsets of the distance classes {1,2,3}), **2 survive the entire 15-C₆ scan**: `{1,3}` and
`{1,2,3}`. The scan therefore **under-determines the claim by 1 bit** and never exercised the
distance-2 exclusion by a near miss at all — the clause that carries the whole content is the
one the data never touched.

**V7 on the audit itself**: planting `w ~ z_0, z_2` on Petersen turns the same scan's 0 into
**4** violations; planting `|N(w) ∩ Z| = 3` turns it into **7**; a legal consecutive attachment
leaves it at 0. The zero is refutable, and the planted graphs are **not C4-free** — which is
precisely why the zero is guaranteed inside the class.

## 31.2 Per-survivor proof status — DEBT-4, UNREGISTERED, awaiting planner numbering

Each item below is **independently proved by this owner**; each proof is one step from
C4-freeness; none rests on the instance agreement.

### 31.2.1 **(a) Off-cycle attachment classification** — INDEPENDENT PROOF HELD
> Let `Z = (z_0,…,z_5)` be an induced 6-cycle of a C4-free graph and `w ∉ Z`. Then
> `N(w) ∩ Z` contains **no pair at cycle-distance 2**. Hence `|N(w) ∩ Z| ≤ 2`, and if
> `|N(w) ∩ Z| = 2` the two neighbours are consecutive or opposite.

**Proof.** If `w ~ z_i` and `w ~ z_{i+2}` then `z_i – z_{i+1} – z_{i+2} – w – z_i` is a 4-cycle,
contradicting C4-freeness. Any three vertices of a 6-cycle contain a pair at cycle-distance 2,
so `|N(w) ∩ Z| ≤ 2`; the remaining two-element cases are distance 1 and distance 3. ∎
*(The four cycle edges alone make the C₄; whether `z_{i+1} ~ w` is irrelevant. The proof step is
machine-checked at all six positions in `w133_r19_null.py` §1.)*

**Corrects a false hint in this owner's own round-18 brief**, which offered
"`|N(w) ∩ Z| = 3` with the three pairwise opposite" as a possibility: a 6-cycle has **no** three
pairwise-opposite vertices (0 such triples).

### 31.2.2 **(b) On-cycle charge identity** — INDEPENDENT PROOF HELD
> For `z` on an induced C₆ `Z` of a C4-free graph, with `Off(z) = N(z) \ Z`:
> `a(z) = 2 + |Off(z)| − t(z)`, hence `Σ_{z∈Z}(a(z) − 2) = Σ_{z∈Z}(|Off(z)| − t(z))`.

**Proof.** `Z` induced ⟹ `d(z) = 2 + |Off(z)|`. **F1** (C4-free ⟹ `G[N(v)]` is a matching, so
`a(v) = d(v) − t(v)`) gives the identity. F1 itself is forced: `x ~ y ~ z` inside `N(v)` makes
`v–x–y–z–v` a 4-cycle. ∎
*(Machine-checked in `w133_r19_null.py` §5: `G[N(v)]` is a matching at every vertex of all three
graphs, 0 failures. Out-of-class ceiling: **70.2 %** of random non-C4-free `G(10, 0.30)` graphs
break F1, so the identity is not trivially true of all graphs — it is true because of
C4-freeness.)*

**Honest value.** Small. It bounds only the **on-cycle** charge, `Σ_{z∈Z}(a(z)−2) ≤ 6`, and the
named obstruction stands: the off-cycle population attached to `Z` is unbounded (G49, §28.2), so
a `Z`-local count cannot see the charge that lives away from `Z`.

### 31.2.3 **(c) Diameter-2 counting identity** — INDEPENDENT PROOF HELD, instance REWRITTEN
> For a C4-free graph of **diameter 2**: `Σ_v a(v) = m − Σ_v C(d(v),2) + C(n,2)`, equivalently
> `l ≤ 3 ⟺ Σ_v C(d(v),2) ≥ m + n(n−7)/2`.

**Proof.** `Σ_v C(d(v),2)` counts paths of length 2. In a C4-free graph of diameter 2 each
non-adjacent pair lies on exactly one such path and each triangle contributes 3, so
`Σ_v C(d(v),2) = [C(n,2) − m] + 3T`. Combined with `Σ_v a(v) = 2m − 3T` (F1, summed) the
identity follows. ∎

**Instance: PETERSEN**, and only Petersen. `n = 10, m = 15, T = 0, Σ C(d,2) = 30, Σ a = 30`:
`30 = 15 − 30 + 45` ✓, and the planner's form `Σ C(d,2) = 30 = m + n(n−7)/2 = 15 + 15` ✓.
Petersen is C4-free **and has `diam = 2`**, so it satisfies the identity's own hypotheses.
**The round-18 return's instance, CE-2, is invalid**: `diam(CE-2) = 3` (eccentricity vector
`(2,3,3,2,2,3,3,3,3,3)`, geodesic `2–1–0–8`), and its `Σ C(d,2)` was written 26 when the true
value is **29**. Out-of-hypothesis ceiling: of 400 C4-free graphs with `diam ≠ 2`, the identity
held on **0**, so it genuinely discriminates — but inside its hypotheses it is a theorem, so
Petersen buys 0 bits of support and buys exactly one thing: it certifies the arithmetic.

**Status of all three: OWNER-PROVED, UNREGISTERED, numbering deferred to the planner (RULING
T).** Nothing in the paper or in §24/§27/§28 depends on any of them.

## 31.3 NOVELTY, stated against my own interest before the planner numbers anything

The null audit says the instance evidence is worth 0 bits. Honesty requires the same treatment
of the *statements'* novelty, because a registry number implies a claim.

* **(a)** is **folklore-strength**. "In a C4-free graph, a vertex outside an induced C₆ has no
  two neighbours at cycle-distance 2 on it" is a one-C₄ observation of the kind that appears
  unnamed inside proofs throughout the C4-free / friendship-graph literature. Its value here is
  **not novelty**: it is that the project's round-18 brief shipped a **false** version of it, and
  the corrected form is now proved and available as a black box. **Recommend numbering it as a
  FACT (F-tier), not as a Lemma with a novelty claim.**
* **(b)** is a **definitional identity** — `d(z) = 2 + |Off(z)|` on an induced cycle plus F1. It
  carries no novelty at all and its content is bounded by `Σ_{z∈Z}(a(z)−2) ≤ 6`, which is
  trivial. **Recommend F-tier, and recommend NOT citing it as a result anywhere.**
* **(c)** is a **standard double-count** (`Σ_v C(d(v),2)` = number of paths of length 2) applied
  under `diam = 2` and C4-freeness. The combination may not be written down in exactly this
  form, but the technique is textbook. **Recommend numbering it as a Lemma with an explicit
  "elementary double-count" annotation, and with Petersen as its only instance.**

**None of the three is a candidate for an S1 novelty search.** They are infrastructure. The
reason to number them is so that later briefs can cite them by name instead of restating them —
which is precisely what RULING W now requires — not because they are results.

---

# §32 owner-w133 round 20 (2026-08-22 22:4x CDT, opus): REGISTRY — the three §31.2 survivors are NUMBERED **G54, G55, G56** on planner RULING AF, at the tiers the owner proposed, with the owner's novelty assessment written into each entry

## 32.1 The numbering, and why the address is a `G` and not an `F`

RULING AF grants numbering **"for citation, not for credit"**, at the tiers §31.3 proposed:
F-tier for (a) and (b), Lemma-with-"elementary-double-count" for (c). The **tiers below are
exactly as granted.** The **prefix** is not, and the reason is a defect found while executing
the ruling.

**`F<n>` is not an address in this project — it is a brief-local label, and it is already
89 % collided.** `problems/wowii/w133_r20_fnamespace.out`, over five shipped fact sheets:
**9 distinct F-numbers seen, 8 of them carrying more than one meaning.** `F1` is "(mass)" in
`w133_r6_TRIEND_qwen.md` and "G[N(v)] is a matching" in the round-18/19 briefs; `F6` carries
**four** meanings; and — decisively — **(a) and (b) are ALREADY shipped as `F8` and `F9` in the
round-19 brief that is in flight as this is written**, while `F8`/`F9` in the r6 fact sheet are
completely different statements. Minting a global `F10`/`F11` would add a fourth meaning to a
namespace that cannot carry one.

**A name is an address, and an address that resolves to four things is not an address.** The
`G`-namespace (`G0…G53`) is monotone and has never collided. So:

> **The TIER is recorded as an ANNOTATION written into the entry; the ADDRESS is a `G`-number.**

This is reported to the planner as a deviation from the literal wording of RULING AF, made on
the authoritative-source rule, and is trivially reversible if the planner prefers the `F`
prefix with a project-wide relabelling of the existing fact sheets.

**Standing rule proposed, arising from the same finding:** a brief's local fact sheet must
either cite a global `G`-number, or prefix its local labels distinctly (`B-F1`, …). Local `F<n>`
labels must never be read as project addresses. This is a live hazard, not a hypothetical: it
is the mechanism by which a later round could "cite" `F9` and silently import the wrong lemma.

## 32.2 **G54 (F-TIER FACT — NOT a Lemma, NO novelty claim)** — off-cycle attachment classification

> Let `Z = (z_0,…,z_5)` be an induced 6-cycle of a **C4-free** graph and `w ∉ Z`. Then
> `N(w) ∩ Z` contains **no pair at cycle-distance 2**. Hence `|N(w) ∩ Z| ≤ 2`, and a 2-element
> trace is **consecutive** or **antipodal**.

**Proof.** If `w ~ z_i` and `w ~ z_{i+2}` then `z_i` and `z_{i+2}` have common neighbours
`z_{i+1}` and `w`, so `z_i – z_{i+1} – z_{i+2} – w – z_i` is a 4-cycle. Any 3 vertices of a
6-cycle contain a pair at cycle-distance 2, so `|N(w) ∩ Z| ≤ 2`; the surviving 2-element cases
are cycle-distance 1 and 3. ∎ *(Machine-checked at all six positions,
`problems/wowii/w133_r19_null.py` §1.)*

**Status: OWNER-PROVED.** Independent proof; it does **not** rest on the 15-C₆ instance scan.

> **NOVELTY, written into the entry as RULING AF requires: FOLKLORE-STRENGTH. This is not a
> result and must never be cited as one.** It is a one-C₄ observation of the kind that appears
> unnamed inside proofs throughout the C4-free literature. **Not an S1 candidate.** The entire
> reason it has a number is so a brief can write "G54" instead of restating it, which is what
> RULING W requires. Its actual value to this project is negative-turned-positive: **the project
> shipped a FALSE version of it in round 18** (a hint offering `|N(w) ∩ Z| = 3` with the three
> pairwise opposite — a 6-cycle has **no** three pairwise-opposite vertices, 0 such triples), and
> G54 is the corrected form.

## 32.3 **G55 (F-TIER FACT — NOT a Lemma, NO novelty claim)** — on-cycle charge identity

> For `z` on an induced C₆ `Z` of a **C4-free** graph, with `Off(z) = N(z) \ Z`:
> `a(z) = 2 + |Off(z)| − t(z)`, hence `Σ_{z∈Z}(a(z) − 2) = Σ_{z∈Z}(|Off(z)| − t(z))`.

**Proof.** `Z` induced ⟹ `d(z) = 2 + |Off(z)|`. C4-freeness makes `G[N(v)]` a matching (if
`x ~ y ~ z` inside `N(v)` then `v–x–y–z–v` is a C₄), so `a(v) = d(v) − t(v)`. Substitute. ∎
*(Machine-checked: `G[N(v)]` is a matching at every vertex of `R`, CE-2 and Petersen, 0
failures, `w133_r19_null.py` §5.)*

**Status: OWNER-PROVED.** Independent proof. **Liveness demonstrated:** the matching step is
**not** trivially true of all graphs — **70.2 %** of random non-C4-free `G(10, 0.30)` graphs
break it — so the identity holds *because of* C4-freeness, not by definition-chasing alone.

> **NOVELTY: DEFINITIONAL. Zero. Recommend it is NEVER cited as a result, only used as a
> substitution.** Its whole content is bounded by the trivial `Σ_{z∈Z}(a(z) − 2) ≤ 6`. **Not an
> S1 candidate.** And its **named limitation travels with it**: a `Z`-local charge count cannot
> see the charge living away from `Z`, because the off-cycle population attached to `Z` is
> unbounded — **Theorem G49, §28.2** (conclusion only; G49's data is not reprinted here either).

## 32.4 **Lemma G56 (elementary double-count)** — the diameter-2 counting identity

> For a **C4-free** graph of **diameter 2**: `Σ_v a(v) = m − Σ_v C(d(v),2) + C(n,2)`,
> equivalently `l ≤ 3 ⟺ Σ_v C(d(v),2) ≥ m + n(n−7)/2`.

**Proof.** `Σ_v C(d(v),2)` counts paths of length 2. In a C4-free graph of diameter 2 every
non-adjacent pair lies on **exactly one** such path and every triangle contributes 3, so
`Σ_v C(d(v),2) = [C(n,2) − m] + 3T`. Combine with `Σ_v a(v) = 2m − 3T` (the matching fact,
summed). ∎

**Status: OWNER-PROVED**, and independently re-derived by the planner at Petersen.

**Instance: PETERSEN, and ONLY Petersen.** `n = 10, m = 15, T = 0, Σ C(d,2) = 30, Σ a = 30`:
`30 = 15 − 30 + 45` ✓, and `Σ C(d,2) = 30 = m + n(n−7)/2 = 15 + 15` ✓. Petersen is C4-free
**and has `diam = 2`**, so it satisfies the identity's own hypotheses.
**The round-18 return's instance, CE-2, is RECORDED INVALID, not dropped:** `diam(CE-2) = 3`
(eccentricity vector `(2,3,3,2,2,3,3,3,3,3)`, geodesic `2–1–0–8`), and its `Σ C(d,2)` was
written 26 when the true value is **29**.

> **NOVELTY: the technique is TEXTBOOK — `Σ_v C(d(v),2)` = number of 2-paths is the standard
> double-count. The particular combination under `diam = 2` + C4-free may be unwritten, but the
> annotation "elementary double-count" is part of the entry and must travel with every citation.
> Not an S1 candidate.** Out-of-hypothesis discrimination: of 400 C4-free graphs with
> `diam ≠ 2`, the identity held on **0** — so it is not vacuous — but **inside** its hypotheses
> it is a theorem, so the Petersen instance buys **0 bits of support** and buys exactly one
> thing: it certifies the arithmetic.

## 32.5 What these three numbers are NOT

* They are **not** a milestone, not a pocket, and not a contribution. **No pocket closed.**
* **Nothing in the paper, and nothing in §24/§27/§28, depends on any of them.** They may be
  cited by later briefs as black boxes; they may **not** be cited as results, and none of them
  may appear in a novelty search.
* The instance evidence behind them was audited at §31.1 and is worth **exactly 0 bits** — the
  15-C₆ scan ranges only over C4-free graphs, where all three are theorems. They are numbered
  **on their proofs and on nothing else**, and the scan additionally **under-determines** (a) by
  one bit: of 8 candidate classifications of an allowed 2-trace, `{1,3}` and `{1,2,3}` both
  survive, and the distance-2 exclusion — the clause carrying G54's entire content — was never
  exercised, not even by a near miss.
* **DEBT-4 is now fully discharged**: proved (§31.2), novelty-assessed against interest (§31.3),
  and numbered with the assessment written into the entry (§32.2–32.4).

---

# §33 owner-w133 round 21 (2026-08-22 23:03 CDT, opus) — the question round 20 newly posed is **CLOSED: NO valid overlapping-`W_cons` instance exists** — and the decisive half of the answer had been on this ledger since round 14

Full record: `orchestration/results/w133_state.md` §"Round 21", which is the authority.
Machine record: `problems/wowii/w133_r21_overlapW.py` → `.out`, **exit 0, 53 checks, 0 failures**,
every check printing its observed population before its verdict.

**Notation.** `W_cons := { w ∉ Z : w has exactly two Z-neighbours, and they are consecutive }`
— the vertices *off* the hexagon whose `Z`-trace is a **consecutive pair**, defined here in the
byte-identical words of §29.3 so that the two definition sites are literally the same string.
*(This section was written at round
21 using a bare `W`, which at that moment denoted a **disjoint** set in §20.2. **The collision is
REPAIRED at §34.2**, on planner RULING BE: the three senses are now `W_P`, `W_0`, `W_cons`, and
the bare letter `W` no longer denotes any set in this file. Read §33 as it now stands.)*

## 33.1 The question, and the answer

Round 20 ended by newly posing: **does a valid instance exist in which two `W_cons`-vertices occupy
OVERLAPPING slots** — slots `{z_i, z_{i+1}}` and `{z_{i+1}, z_{i+2}}`, sharing the hexagon vertex
`z_{i+1}`? The muse-spark return had asserted one exists and shipped an 8-vertex witness that
**contains a 4-cycle**, so the claim died with its witness and the question was left open.

> **Answer: NO. In a C4-free graph with an induced C₆ `Z` and no induced P7, two overlapping
> slots are never both occupied. The muse's existence claim is not merely unwitnessed — it is
> FALSE.**

## 33.2 The proof, and the hypotheses are used in different branches

Let `w` have `N(w) ∩ Z = {z_0, z_1}` and `w'` have `N(w') ∩ Z = {z_1, z_2}`, `w ≠ w'`. Every
adjacency among the eight vertices `Z ∪ {w, w'}` is forced by the hypotheses **except the single
bit `ww'`**, so the configuration space is exactly two graphs, and both die:

* **`w ≁ w'` ⟹ an induced P7.** `w – z_0 – z_5 – z_4 – z_3 – z_2 – w'` is chordless on **7**
  vertices. *(This is round 20's (P2a); it is also the surviving half of the round-12 `P7G32`
  report's L2, see §33.4.)*
* **`w ~ w'` ⟹ a C4.** The pair `(w, z_2)` has the two common neighbours `z_1` and `w'`, so
  `w – z_1 – z_2 – w' – w` is a 4-cycle. *(Chords are irrelevant to this project's C4-freeness,
  which reads "no two vertices have two common neighbours".)* The machine enumerates **four**
  violating pairs in this frame, not one: `{z_1,w}` common to `(z_0,w')`; `{z_0,w'}` common to `(z_1,w)`; `{z_2,w}` common to
  `(z_1,w')`; `{z_1,w'}` common to `(z_2,w)`. ∎

**Both hypotheses are load-bearing, and each branch is the other's counterexample.** Drop
"no induced P7" and the `w ≁ w'` frame survives — it *is* C4-free. Drop C4-freeness and the
`w ~ w'` frame survives — it *is* P7-free. Neither hypothesis alone excludes overlap.

**The obstruction lifts to any host graph.** A C4 is a subgraph condition, so it lifts for free;
the induced P7 lifts because all 21 pairs among its 7 vertices are forced by the hypotheses.
Tested anyway over **2 512** host graphs (exhaustive over one extra vertex with all 2⁸
attachments in both frames, plus 2 000 random hosts with 2–4 extra vertices): **0 survivors.**

## 33.3 What is NEW this round: the pair-configuration table is now COMPLETE

The brief's Problem 1 asks "same slot? overlapping? disjoint? antipodal? **Decide each.**" All
four are now decided, over the full population of **8** frames (slot distance `0,1,2,3` × the
`ww'` bit):

| slot distance | `w ≁ w'` | `w ~ w'` | verdict |
|---|---|---|---|
| **0** (same slot) | C4: `z_0,z_1` common to `w,w'` | C4 | **impossible** — round 20's (P1) |
| **1** (overlapping) | induced P7 | C4 | **impossible** — §33.2 |
| **2** (disjoint, non-antipodal) | **survives** | C4: `z_2,w` common to `z_1,w'` | **possible, and NON-ADJACENCY IS FORCED** |
| **3** (antipodal slots) | **survives** | **survives** | **possible, either way** |

**Exactly 3 of the 8 configurations survive.** Two consequences worth stating separately:
* **`w ~ w'` forces slot distance exactly 3.** If `w ~ w'` and some `z_i ∈ N(w)`,
  `z_{i+1} ∈ N(w')`, the 4-cycle `w–z_i–z_{i+1}–w'` appears; such an `i` exists at slot distance
  0, 1 and 2 and does **not** exist at distance 3.
* **`|W_cons| = 3` forces `W_cons` independent**, since the only independent slot-triples are `{i,i+2,i+4}`
  and every pair in one sits at slot distance 2.

**Corollary (`|W_cons| ≤ 3`, with the mechanism).** Slot-assignment is injective on `W_cons` (distance 0)
and no two occupied slots overlap (distance 1), so the occupied slots are an **independent set in
the 6-cycle of slots**, whose maximum is **3** (verified over all `2⁶` slot-subsets). The bound is
**attained**: `INSTANCE-D`, `n = 9`,
`0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-1,7-2,7-3,8-4,8-5` — validated most-basic-first (simple ✓,
connected ✓, **C4-free ✓ checked first**, induced C₆ ✓, `path = 6` so no induced P7 ✓,
`W_cons = {6,7,8}` on slots `{0,2,4}` ✓, `a` = (2,2,2,2,2,2,1,1,1), `Σa = 15 ≤ 3n`).

**Surviving-configuration instances, fully validated in the same order** (these are the
"nearby form that survives" the refusal must name): `INSTANCE-A` (slot distance 2, `w ≁ w'`,
`n=8`) `0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-1,7-2,7-3`; `INSTANCE-B` (slot distance 3, `w ≁ w'`)
same with `7-3,7-4`; `INSTANCE-C` (slot distance 3, `w ~ w'`) `INSTANCE-B` plus `6-7`.

## 33.4 PROVENANCE, STATED AGAINST MY OWN INTEREST — this is substantially a **RE-DERIVATION**

> **CORRECTION, entered at round 22 by the RULING BF grep, against my own interest a second
> time: the round number below is WRONG and the true one is EARLIER. The adjudication is
> `w133_state.md` §"Round 13" (lines 881–888), not §"Round 14", and round 13b then wrote it
> into THIS FILE at §28.3 S2. So the decisive step is SEVEN rounds old, not six, and it was
> recorded THREE times — state §Round 13, draft §28.3 S2, draft §29.3 — and not one of the
> three carried the consequence "no two occupied slots overlap". The defect is worse than
> round 21 reported: it is not one badly-formatted entry, it is a badly-formatted entry
> COPIED FORWARD. §34.1 carries the corrected provenance; the paragraph below is left standing
> as written so the correction is visible rather than tidy.**

**The decisive step is not new. It has been on this ledger since round 14.** `w133_state.md`
§"Round 14" adjudicates the (VOID) round-12 `P7G32` report's **L2 (`|W_cons| ≤ 3`)** as
*"statement TRUE, proof DEFECTIVE"*, and supplies the exact missing case in one line:

> *"One-line repair the report missed: `ww′ ∈ E` is impossible by **C4-freeness**
> (4-cycle `w–z_i–z_{i+1}–w′`)."*

That is §33.2's second bullet, written six rounds ago. The first bullet (the induced P7) is the
surviving half of that same L2. **So the two-case argument existed, complete, at round 14** —
and round 14 also exhibited the tight `|W_cons| = 3` graph, whose edge list is **byte-identical to
`INSTANCE-D` above**, which I reconstructed this round without consulting it. That identity is
worth one thing and I will claim only that: it **double-sources** the witness by two independent
constructions.

**Honest split of credit:**
* **NOT new** — the overlap exclusion, its two cases, `|W_cons| ≤ 3`, the tight instance. Round 14.
* **New this round** — the **complete** 8-configuration table (§33.3), in particular
  **slot distance 2 forbids adjacency** and **slot distance 3 permits both**, the derived rule
  *`w ~ w'` ⟹ slot distance exactly 3*, the **hypothesis-sharpness** statement, the **lift**
  test, and machine validation of all four instances.
* **Answered, not discovered** — round 20's open question. It was answerable from the ledger.

## 33.5 The ledger defect that manufactured the open question — and it is generalizable

Round 14's derivation was recorded, on planner ruling **CERT-4**, at **§29.3** as
**OWNER-DERIVED / UNREGISTERED**. Read §29.3: it records the **statement** `|W_cons| ≤ 3`, its
tightness datum, its provenance and its status — and **no proof.** The deferral was correct
(a VERIFY-ONLY slice does not license owner attack results into the registry). The **format** was
not, and the cost is now measurable:

> **A statement-only UNREGISTERED entry destroys the intermediate content of its own proof.**
> `|W_cons| ≤ 3` survived; *"no two occupied slots overlap"* did not, because it lived only inside the
> proof that was not written down. Six rounds later the project **wrote a brief asking for it**,
> **spent its only PRECISION judge family** on the question, and received an answer whose witness
> carried a 4-cycle — and then recorded the question as **newly posed and open**.

**Proposed standing rule (planner's to take or refuse):** an entry recorded UNREGISTERED must
still carry its **proof**, or an explicit line naming what the proof establishes beyond the
headline. Deferring *registration* is a status decision; deferring the *proof text* deletes
mathematics. The instrument reading is the same species the planner recorded twice tonight for
refusal clauses and once for `F`-addresses: **a record that names less than it knows is read by
the next round as a record of ignorance.**

## 33.6 The `W` collision is in the SYMBOL namespace, not just the `F` namespace — **REPAIRED at §34.2**

As found at round 21: the same letter `W` denoted **two disjoint sets** in this one file, at
§20.2 ("the vertices with **no** `Z`-neighbour") and §29.3 ("exactly two `Z`-neighbours, and they
are **consecutive**"). Strictly worse than the `F<n>` collision, because a reader who imports
"`w ∈ W`" across sections imports the **negation** of what was meant.

**Planner RULING BE ordered the repair rather than queuing it, and §34.2 executes it** — and the
executed count is **three** senses, not two: §19.4's Lemma G30 carried a third. The letter `W`
now denotes nothing on its own anywhere in this file.

## 33.7 Status: NOT self-registered

**No number is minted here.** The content is already ruled UNREGISTERED by **CERT-4**, and an
owner does not promote his own attack result by writing a `G`-number next to it. What has changed
is that CERT-4's stated *reason* for the deferral — that the derivation arrived inside a
VERIFY-ONLY slice — **no longer applies**: round 21's task book commissions this as a bounded
own-attack with hand proof. **Proposed address if the planner registers it: `G57`** (the `G`
namespace is monotone through `G56` and has never collided; no `F` address is minted, per the
standing hazard). **Proposed tier: Lemma, elementary, NOT an S1 candidate** — each branch is a
one-line forbidden-subgraph observation, and the honest description of the whole is "the correct
P7-analogue of G32, which is strictly weaker than G32 and does not close any pocket."
**Nothing in the paper, and nothing in §24/§27/§28, depends on it.**

---

# §34 owner-w133 round 22 (2026-08-22 23:0x–23:4x CDT, opus) — **REGISTRY: G57 is REGISTERED, carrying its proof** (planner RULING BD); the **`W` collision is REPAIRED** (RULING BE, ordered); the UNREGISTERED sweep; and the (D3-C6) mass count is restarted

Full record: `orchestration/results/w133_state.md` §"Round 22", which is the authority.
Machine record: `problems/wowii/w133_r22_namespace.py` → `.out`, **exit 0, 33 checks, 0 failures**,
every check printing its observed population before its verdict.
Rulings executed: **BD** (register G57), **BE** (repair the `W` collision this round, do not
queue it), **BF** (grep the ledger before anything is registered as new), and the planner's
adopted rule that **an UNREGISTERED entry must carry its proof, or one line naming what the
proof establishes beyond the headline.**

## 34.1 **Lemma G57 (elementary, forbidden-subgraph) — REGISTERED on RULING BD**

> **G57.** Let `G` be C4-free, let `Z = (z_0,…,z_5)` be an induced 6-cycle of `G`, and suppose
> `G` has **no induced P7**. Write
> `W_cons := { w ∉ Z : w has exactly two Z-neighbours, and they are consecutive }`
> and let the **slot** of `w ∈ W_cons` be that consecutive pair.
> **(i)** Two vertices of `W_cons` never occupy the **same** slot.
> **(ii)** Two vertices of `W_cons` never occupy **overlapping** slots (slots sharing one `z`).
> **(iii)** Hence the occupied slots form an **independent set in the 6-cycle of slots**, so
> **`|W_cons| ≤ 3`**, and the bound is **attained**.
> **(iv)** At slot distance 2 the two vertices are **NON-ADJACENT** (adjacency forces a C4); at
> slot distance 3 **both** adjacency and non-adjacency occur. Consequently `w ~ w'` forces slot
> distance exactly 3, and **`|W_cons| = 3` forces `W_cons` independent**.

**PROOF, carried with the entry** *(this is the whole point of the entry: the round-21 finding
was that recording (iii) without (i)/(ii) cost this project six rounds and a PRECISION call)*.

*(i)* If `w ≠ w'` both have trace `{z_i, z_{i+1}}`, then `z_i` and `z_{i+1}` have the two common
neighbours `w, w'`: a C4. ∎

*(ii)* Let `N(w) ∩ Z = {z_0, z_1}` and `N(w') ∩ Z = {z_1, z_2}`. Every adjacency among the eight
vertices `Z ∪ {w, w'}` is forced by the hypotheses **except the single bit `ww'`**, so the
configuration space has exactly **2** members and both die:
* **`w ≁ w'`** ⟹ `w – z_0 – z_5 – z_4 – z_3 – z_2 – w'` is a chordless path on **7** vertices:
  an induced P7, contradiction.
* **`w ~ w'`** ⟹ `(w, z_2)` has the two common neighbours `z_1` and `w'`: a C4, contradiction.
  *(The machine enumerates **four** violating pairs in this frame, not one:* `{z_1,w}` common to
  `(z_0,w')`; `{z_0,w'}` common to `(z_1,w)`; `{z_2,w}` common to `(z_1,w')`; `{z_1,w'}` common
  to `(z_2,w)`.*)* ∎

*(iii)* By (i) the slot map is injective on `W_cons`; by (ii) no two occupied slots are adjacent
in the slot-cycle. A maximum independent set in `C_6` has size **3** (verified over all `2⁶`
slot-subsets). Attained by **INSTANCE-D**, `n = 9`,
`0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-1,7-2,7-3,8-4,8-5` — validated most-basic-first (simple ✓,
connected ✓, **C4-free ✓ checked first**, induced C₆ ✓, longest induced path `= 6` so no induced
P7 ✓, `W_cons = {6,7,8}` on slots `{0,2,4}` ✓). ∎

*(iv)* At slot distance 2, say `N(w) ∩ Z = {z_0,z_1}` and `N(w') ∩ Z = {z_2,z_3}`: if `w ~ w'`
then `(z_2, w)` has common neighbours `z_1` and `w'`, a C4; so non-adjacency is **forced**, and
the non-adjacent frame survives (**INSTANCE-A**, `n = 8`,
`0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-1,7-2,7-3`). At slot distance 3 both survive: **INSTANCE-B**
(`…,7-3,7-4`) and **INSTANCE-C** (`INSTANCE-B` + `6-7`). The derived rule follows because such
an `i` with `z_i ∈ N(w), z_{i+1} ∈ N(w')` exists at slot distance 0, 1, 2 and not at 3; and the
only independent slot-triples are `{i, i+2, i+4}`, every pair of which sits at slot distance 2. ∎

**Both hypotheses are load-bearing and each branch is the other's counterexample:** drop
"no induced P7" and the `w ≁ w'` frame survives (it *is* C4-free); drop C4-freeness and the
`w ~ w'` frame survives (it *is* P7-free). **The obstruction lifts to any host** — C4 is a
subgraph condition, and the P7's 21 pairs are all forced; tested anyway on **2 512** host graphs
(exhaustive over one extra vertex with all `2⁸` attachments in both frames, plus 2 000 random
2–4-vertex extensions): **0 survivors.** Machine record for all of the above:
`problems/wowii/w133_r21_overlapW.py` → `.out`, exit 0, 53 checks, 0 failures.

**The complete configuration table** (8 frames = slot distance `0,1,2,3` × the `ww'` bit; exactly
**3** survive), which is RULING AN's "name the direction refused AND the surviving neighbour"
implemented rather than promised:

| slot distance | `w ≁ w'` | `w ~ w'` | verdict |
|---|---|---|---|
| **0** same slot | C4 | C4 | **impossible** |
| **1** overlapping | induced P7 | C4 | **impossible** |
| **2** disjoint, non-antipodal | **survives** (INSTANCE-A) | C4 | **possible; NON-ADJACENCY FORCED** |
| **3** antipodal slots | **survives** (INSTANCE-B) | **survives** (INSTANCE-C) | **possible, either way** |

> **NOVELTY, written inside the entry as RULING AF requires: this is substantially a
> RE-DERIVATION and must never be cited as a discovery.** Clauses (i)–(iii) were complete on this
> ledger at **round 13** (`w133_state.md` §"Round 13", the `D3_A`/L2 adjudication), and round 13b
> copied them into this file at **§28.3 S2**; the tight instance exhibited there is
> **byte-identical to INSTANCE-D**, rebuilt at round 21 without consulting it — so the witness is
> **double-sourced by two independent constructions** and nothing more is claimed from the
> identity. **NEW at round 21:** clause **(iv)** and the complete 8-frame table, the
> hypothesis-sharpness statement, the lift test, and machine validation of all four instances.
> **TIER: Lemma / elementary. NOT an S1 candidate. Closes no pocket. Strictly weaker than G32.**
> Nothing in `papers/wowii133/main.tex`, and nothing in §24/§27/§28, depends on it.
>
> *(Round 21 attributed the prior art to round 14. That is wrong and the correction is entered
> at §33.4 rather than by silent edit: it is **round 13**, and it was recorded **three** times —
> state §Round 13, draft §28.3 S2, draft §29.3 — none of which carried clause (ii). The ledger
> defect is not one badly-formatted entry; it is a badly-formatted entry **copied forward**.)*

**§29.3 is superseded by this entry** and now reads as its statement-only ancestor; §28.3 S2's
"`|W_cons| ≤ 3` with a new proof" is the same content and is likewise subsumed here.

## 34.2 The `W` collision — **REPAIRED, as ordered by RULING BE**, and it was **three** senses

> *"An F-collision imports the wrong lemma; a W-collision imports the **negation** of the
> intended set."* — RULING BE

Round 21 reported two colliding senses. Executing the repair found **three**:

| sense | was | **is now** | sites |
|---|---|---|---|
| neighbours of `P` with **no** `Z`-neighbour | `W` (§19.4, Lemma G30) | **`W_P`** | 19.4, and the 5 later back-references to G30's bound |
| the vertices with **no** `Z`-neighbour | `W` (§20.2, Lemma G33) | **`W_0`** | §20.2–§21 |
| off-`Z` vertices with **two consecutive** `Z`-neighbours | `W` (§29.3, §28.3, §33) | **`W_cons`** | §28.3, §29, §29.3, §33 |
| **all** off-cycle neighbours of one `z ∈ Z` | `W_z` (§31.2.2, §32.3 = **G55**) | **`Off(z)`** | §31.2.2, §32.3 |

**§19.4's `W` was not a fourth set — it is exactly §20.3's `W_P = N(P) ∩ W_0`**, so the repair
also removes a real ambiguity: G30's headline `|W| ≤ 3` and §29.3's headline `|W| ≤ 3` were
**byte-identical strings naming different theorems about different sets**. `W_z → Off(z)` is
included because `W_z` and `W_P` *look* like one family and are not: `W_P ⊆ W_0` excludes every
vertex with a `Z`-neighbour, while `Off(z)` is all of `N(z) ∖ Z`.

**Executed:** 71 bare-`W` substitutions across the four ranges plus 7 `W_z` lines. **After the
repair the bare letter `W` denotes no set anywhere in this file**; its only surviving occurrences
are the graph name `Q32-W` and the planner label `RULING W`, which are distinct tokens.
**No shipped brief and no `.out` machine record was retro-edited** — those are historical records
and rewriting them would falsify them; the draft is the authoritative source under PROTOCOL v3,
and it is the draft that has been repaired.

### 34.2a **Address uniqueness is now asserted at MINT time, not at grep time** (RULING BB)

Two collisions on this line were both caught by a grep run **after** the fact, i.e. by luck.
`problems/wowii/w133_r22_namespace.py` PART A makes it a precondition:
* it scans every `X := …` site in the draft — **observed: 19 distinct symbols, 27 definition
  sites** — and fails if any symbol carries more than one distinct definition;
  *(a number caught by this project's oldest red line: the first draft of this line said
  "17 symbols, 24 sites", which was the population **before §34 itself was appended**. Prose
  written from a run of an earlier file is prose written ahead of its `.out`. Re-read from the
  final `.out`, which is the run against the file as it now stands.)*
* `assert_mintable(name)` is the gate proper: a new symbol or address must not already resolve
  in the corpus. Run at mint time this round for `W_0`, `W_cons`, `Off`, and for the next free
  addresses `G58`/`G59` (**observed 0 occurrences**, so the `G` namespace is still monotone).
* **It is demonstrated on a defect that actually happened**: run against the pre-repair draft it
  **FIRES on `W`** with the two real senses at lines 1961 and 3786; run against the repaired
  draft it is clean.

**AND IT FIRED ON THIS VERY SECTION, WHICH IS THE STRONGEST THING THAT CAN BE SAID FOR IT.**
The first draft of §34.4a below minted the bare letter `A` for the antipodal family — **a fourth
sense of the legacy symbol `A`, minted inside the section that repairs symbol collisions**, by the owner who
had just written RULING BE into the file. The gate refused the draft (`collisions outside the
registered legacy set: ['W_cons', 'A']`) and the symbol is now **`W_anti`**. It also refused a
second, subtler defect of my own: §34.1's `W_cons` definition had been line-wrapped, so its text
no longer matched §29.3's byte-for-byte and the gate correctly read two definition sites as two
senses; the definition is now on one line. **A grep-after-the-fact would have caught neither
before the section shipped.**

**And it found pre-existing collisions nobody had looked for — registered, not repaired:**
`A` (3 senses, lines 513/745/1034), `C` (2 senses, 644/1150), `H` (3 senses, 1169/1228+1593),
all inside the legacy Chinese §13–§15 material. They are declared in the script as an allowlist
that **pins the sense COUNT, not just the name** — `{A: 3, C: 2, H: 3}` — so the gate stays green
for new mints while the debt stays visible **and frozen in size**. *(An allowlist that checks only
the name is a hole: an allowlisted symbol can quietly acquire a fourth sense. Found the same hour
it was written, because §34.4a's first draft did exactly that to `A` and a name-only allowlist
would have passed it.)* They are **not**
repaired this round, because renaming symbols inside proofs this owner has not re-verified would
trade a naming hazard for a mathematical one. *(One owner error preserved in the source: the
gate's first run reported `H` as a collision on a pure whitespace difference between lines 1228
and 1593. A gate that cries wolf on formatting gets switched off — the comparison key now strips
whitespace.)*

## 34.3 The UNREGISTERED sweep ordered with item 1 — every entry whose headline names less than its proof knows

| entry | headline | what its proof also establishes | action |
|---|---|---|---|
| **§29.3** `|W_cons| ≤ 3` | statement + tightness only | **(i) same-slot exclusion, (ii) overlap exclusion** — the clause that cost six rounds | **superseded by §34.1**, which carries the proof |
| **§28.3 S2** `L2's statement with a new proof` | names the C4 repair | **does not name the P7 branch, and does not name the overlap consequence at all** | **subsumed by §34.1**; cross-reference added here |
| **§28.3 S1/S3/S4/S5** | "adopted by rewrite" | S3 carries Theorem G50 in full; S4/S5 carry their proofs and their **honest zero-coverage billing** | **clean** — proof or explicit content travels with each |
| **§31.2 (a)(b)(c)** | "UNREGISTERED, awaiting planner numbering" | proofs ARE held in-line | **STALE STATUS, repaired below** — they were numbered **G54/G55/G56** at §32 two rounds ago and §31.2 still says "awaiting" |
| **§28.1b, §29.4** DEBT rows | "DISCHARGED at round 17, see §30" | — | **clean** — pointer travels |

**Repair to §31.2's stale status is entered here rather than by silent edit:** §31.2's three
survivors are **no longer UNREGISTERED**. They are **G54, G55, G56** (§32.2–32.4), at F-TIER /
F-TIER / Lemma-elementary respectively, with their novelty assessments inside their entries.
Read §31.2 as proof text and §32 as the registry.

> **The species, third sighting in two rounds:** §29.3 named less than it knew (no proof),
> §31.2 names less than the ledger knows (stale status). **A record that names less than it
> knows is read by the next round as a record of ignorance** — in the first case the next round
> re-asked a settled question; in the second it would have re-requested numbering already
> granted. Both are cheap to prevent and neither was caught by anything but a deliberate sweep.

## 34.4 The front: **(D3-C6)'s mass count is RESTARTED** — and the first computable step is done

**The choice, in one line as asked:** *(D3-C6) over A2, because (D3-C6)'s hypotheses — connected,
C4-free, induced C₆, no induced P7 (§27.4) — are byte-for-byte G57's hypotheses, so the round-21
classification transfers with no new assumption and turns an open search into an arithmetic;
A2 needs a new idea and is already tight-controlled by `Q32-W`, so it will still be there.*

### 34.4a The off-cycle population with a 2-element `Z`-trace is **bounded by 6, and 6 is attained**

By **G54** every `w ∉ Z` has `|N(w) ∩ Z| ≤ 2`, and a 2-element trace is **consecutive** or
**antipodal**. So the 2-trace population splits into `W_cons` and
`W_anti := { w ∉ Z : w has exactly two Z-neighbours, and they are antipodal }`, and:
* `|W_cons| ≤ 3` — **G57(iii)**, attained by INSTANCE-D.
* `|W_anti| ≤ 3` — each antipodal slot holds **at most one** vertex, since two vertices with the same
  antipodal trace `{z_i, z_{i+3}}` are two common neighbours of `z_i` and `z_{i+3}`: a C4. There
  are 3 antipodal slots. *(Machine: the forced C4 exhibited at **3 of 3** antipodal slots.)*
  Attained by **INSTANCE-F**, `n = 9`: `0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-3,7-1,7-4,8-2,8-5`
  (C4-free ✓ first, induced C₆ ✓, longest induced path **5** ✓).
* **Hence `|{w ∉ Z : |N(w) ∩ Z| = 2}| ≤ 6`, and it is ATTAINED**: **INSTANCE-E**, `n = 12`,
  INSTANCE-D `+ 9-0, 9-3, 10-1, 10-4, 11-2, 11-5` — validated most-basic-first, **C4-free
  (0 violating pairs) checked before any statistic**, induced C₆ ✓, longest induced path `= 6`
  so no induced P7 ✓, `|W_cons| = 3`, `|W_anti| = 3`.

> **PROVENANCE, run BEFORE this was written, per RULING BF — and it fired again.**
> **`|W_anti| ≤ 3` (the round-13 report's `A`), attained, is NOT new: it is on the ledger at round 13**, in the `D3_A`/**L1**
> bullet, **three lines above the L2 bullet §33.4 quotes** — and its `n = 9` witness is
> **byte-identical to INSTANCE-F**, verified string-equal. Round 21 read that paragraph, took the
> L2 bullet out of it, and did not read L1. **What is new here is only the SUM and its
> simultaneous attainment**: that the two extremal families **coexist in one graph**
> (INSTANCE-E), which neither round-13 bullet asserts and which does not follow from them —
> a priori a maximal `W_cons` could obstruct a maximal `W_anti`. It does not.
> **UNREGISTERED, and it carries its proof above. No number is minted; proposed only if the
> planner wants one. Tier would be: corollary, elementary. Not an S1 candidate.**

### 34.4b What the restarted count must actually run on — the Z-local count is **NOT** enough

`G55` gives the hexagon's charge exactly: `a(z) = 2 + |Off(z)| − t(z)`, and §34.4a now determines
the 2-trace part of `Off(z)` completely. **But a `Z`-local count cannot close (D3-C6)**, and this
is exhibited **inside the hypotheses** rather than asserted:

> hexagon `+ k` independent single-trace vertices at `z_0`, for `k = 0…6`: every host is
> **C4-free, has `Z` induced, and has longest induced path `≤ 6`** (checked **before** any
> statistic is read off it), while `Σ_{z∈Z}(a(z) − 2) = k` grows **without bound** — and
> `l = Σa/n = 2.0` on every one of them.

So the Z-surplus is unbounded in-hypothesis and is paid for by an **off-cycle deficit**: those
vertices carry `a = 1`. **The count to restart is therefore the global one**

> `Σ_v (a(v) − 3) = Σ_{z∈Z}(a(z) − 3) + Σ_{v ∉ Z}(a(v) − 3) ≤ 0`,

in which **the `Z`-term is now fully determined by the occupied-slot set** (G57 + G55 + §34.4a)
and **the off-cycle term is the open half**. Measured on the two extremal instances:
`INSTANCE-D` — `n = 9, Σa = 15, l = 1.667`, Z-term `−6`, off-term `−6`; `INSTANCE-E` —
`n = 12, Σa = 27, l = 2.25`, **Z-term `0`** (the maximum: `a(z) = 3` at all six), off-term `−9`.
**The next step is a lower bound on the off-cycle deficit**, i.e. an upper bound on `a(v)` for
`v ∉ Z` with `|N(v) ∩ Z| ≤ 1` — which is exactly where **G49**'s unboundedness lives and is
therefore the honest place for this line's next own-attack or brief.

> **Owner error preserved in source (item 6 discipline).** The first version of the check above
> hung the `k` extra vertices on **INSTANCE-D** and reported the Z-charge growing. It does grow —
> but **every one of those hosts has longest induced path 7**, i.e. contains an induced P7, so
> not one of them is in (D3-C6)'s class and **the check passed while proving nothing.** Repaired
> by making in-hypothesis membership a **precondition of the sample** rather than a statistic
> reported after it; the discarded out-of-hypothesis samples are still printed by the script.

## 34.5 Standing items, not quietly dropped

* **GATE A is strong in conjunction only.** This round ran **no gate and no engine call** — it is
  registry, repair and an own-attack; there is no verdict to be strong or weak about.
* **Every check in `w133_r22_namespace.py` prints its observed population before its verdict**,
  and the two new checks are each demonstrated on a defect that actually happened (the `W`
  collision; the out-of-hypothesis sample above).
* **(T-C)**, **(D3-C6)**, **pocket-2 `μ=1`/A2** all remain **OPEN**. **No pocket closed, so no
  mathematics milestone.** G57 is a registration, not a result.
* **Refusal clause B4′ stands unchanged** (direction refused + surviving neighbour named), and
  the tables in §34.1 and §34.4a are written to that rule.

---

# §35 owner-w133 round 23 (2026-08-23 02:2x–02:4x CDT, opus) — **THE OFF-CYCLE BOUND**: the question `a(v) ≤ ?` for `v ∉ Z` with `|N(v) ∩ Z| ≤ 1` is **ANSWERED, and the answer is a DICHOTOMY** — bounded for `|N(v) ∩ Z| = 1`, provably UNBOUNDED for `|N(v) ∩ Z| = 0`

Full record: `orchestration/results/w133_state.md` §"Round 23", which is the authority.
Machine record: `problems/wowii/w133_r23_offcycle.py` → `.out`, **exit 0, 44 checks, 0 failures,
1.38 s**. Rulings executed: **BM** (in-hypothesis membership is a *precondition of the sample*),
**BB** (mint-time address uniqueness), **BF** (grep the ledger before anything is called new),
and the proof-carrying rule for UNREGISTERED entries.

## 35.1 The statement — **UNREGISTERED, carrying its proof; no number minted**

Throughout: `G` connected, **C4-free**, `Z = (z_0,…,z_5)` an induced C₆, **no induced P₇** —
byte-for-byte (D3-C6)'s hypotheses (§27.4) and G57's. Write

> `W_1 := { v ∉ Z : |N(v) ∩ Z| = 1 }`

completing the family `W_0` (no `Z`-neighbour, §20.2) / `W_cons` / `W_anti` (§34.4a).
By **G54** every `v ∉ Z` has `|N(v) ∩ Z| ≤ 2`, and a 2-element trace is consecutive or
antipodal, so `V ∖ Z = W_0 ⊔ W_1 ⊔ W_cons ⊔ W_anti`.

> **(a) SINGLE TRACE.** If `N(v) ∩ Z = {z_0}` then **`d(v) ≤ 4` and `a(v) ≤ 3`**, both **exact**
> and **simultaneously attained**.
> **(b) CONSECUTIVE TRACE.** If `N(w) ∩ Z = {z_0,z_1}` then **`d(w) ≤ 4` and `a(w) ≤ 3`**, both
> exact and simultaneously attained; moreover `a(w) = d(w) − 1` throughout the realisable range.
> **(c) ANTIPODAL TRACE.** If `N(u) ∩ Z = {z_0,z_3}` then `d(u)` and `a(u)` are **UNBOUNDED**.
> **(d) EMPTY TRACE.** If `N(x) ∩ Z = ∅` then `d(x)` and `a(x)` are **UNBOUNDED**.
> **(e) Consequently `a(v) − 3 ≤ 0` for every `v ∈ W_1 ∪ W_cons`: the entire non-antipodal
> off-cycle population carries NO POSITIVE CHARGE**, and the whole off-cycle surplus of
> `Σ_v(a(v) − 3) ≤ 0` lives in `W_anti ∪ W_0`.

**So the planner's question `a(v) ≤ ?` for `|N(v) ∩ Z| ≤ 1` has BOTH answers inside it:** the
`= 1` half is bounded by **3**, and the `= 0` half **cannot be bounded at all**.

### 35.1.1 Proof of the two bounds, and the enumeration is over `N(v)` so it is SHARP

*Step 1 (the frame tables — exhaustive, 64 frames each).* For an anchor `v ∉ Z` with a given
trace and a free neighbour `u ∈ N(v) ∖ Z`, the induced subgraph on `Z ∪ {v,u}` is **completely
determined** by `u`'s trace `T`. C4-freeness, P₇-freeness and "`Z` is an induced C₆" are
**inherited by induced subgraphs**, so a frame refuted here is refuted in **every** host. All
`2⁶ = 64` values of `T` were enumerated in each of four cases; the survivor sets are exactly:

| anchor trace | survivors (`u`'s permitted traces) | closed form |
|---|---|---|
| `{z_0}` (single) | `{z_0},{z_2},{z_3},{z_4},{z_0,z_3},{z_2,z_3},{z_3,z_4}` — **7 of 64** | nonempty **legal** trace inside `{z_0,z_2,z_3,z_4}` |
| `{z_0,z_1}` (consecutive) | `{z_3},{z_4},{z_3,z_4}` — **3 of 64** | nonempty subset of `{z_3,z_4}` |
| `∅` (distance ≥ 2) | `∅, {z_0,z_3}, {z_1,z_4}, {z_2,z_5}` — **4 of 64** | empty or **antipodal** |
| `{z_0,z_3}` (antipodal) | `∅, {z_0}, {z_3}` — **3 of 64** | subset of `{z_0,z_3}`, not both |

Each refutation is by one of exactly two mechanisms, and the machine prints which:
* **`T = ∅` dies by an INDUCED P₇** and by nothing else, in the single and consecutive rows —
  witness printed and re-verified edge by edge, e.g. `z_2 z_3 z_4 z_5 z_0 v u`.
* **`z_1, z_5` die by a C₄** for a single-trace anchor (`v` and `z_1` **already** share `z_0`);
  **`z_0,z_1,z_2,z_5` die by a C₄** for a consecutive-trace anchor (`w` and `z_0` already share
  `z_1`, `w` and `z_2` already share `z_1`, symmetrically at `z_5`). *This second family is the
  half the owner's hand argument missed — see §35.4.*

*Step 2 (C4-freeness turns the survivor list into a degree bound).* Two neighbours of the anchor
whose traces share a `z` would be two common neighbours of the anchor and that `z`: a C₄. So the
traces of `N(v) ∖ Z` are **pairwise disjoint** and drawn from the survivor list. Together with the
free adjacency bits **inside** `N(v)`, this determines `G[N(v)]` completely.

*Step 3 (enumerate `G[N(v)]` — hence the bounds are exact, not merely upper).*
**152** neighbourhood configurations for the single-trace anchor (**17** in hypothesis, 135
refuted) and **6** for the consecutive anchor (**5** in hypothesis, 1 refuted). Realised `(d,a)`
pairs: single `{(1,1),(2,1),(2,2),(3,2),(3,3),(4,3)}`; consecutive `{(2,1),(3,2),(4,3)}`.
**Maximum `d = 4`, maximum `a = 3`, attained together at `(4,3)` in both classes.** Both
maximisers are re-admitted as **hosts** (connected), so attainment is genuine and not a frame
artefact. ∎

### 35.1.2 Proof of the two unboundedness statements, exhibited IN HYPOTHESIS

Each member is **admitted before any statistic is read off it** (RULING BM, enforced by the
`Sample` object, which raises on a statistic read from an unadmitted or rejected sample).

* **FAMILY-A** (antipodal): `Z + u` with `N(u) ∩ Z = {z_0,z_3}` `+ k` pendants on `u`,
  `k = 0…8`. All nine in hypothesis (longest induced path **5** throughout).
  **`d(u) = a(u) = k + 2`.**
* **FAMILY-U** (empty trace — the question's own class): `Z + u` antipodal `+ v ~ u` `+ k`
  pendants on `v`, `k = 0…8`. All nine in hypothesis (longest induced path **6** throughout),
  `dist(v, Z) = 2`. **`d(v) = a(v) = k + 1`.**

**And the global count survives on every member of both families** — `Σ_v(a(v)−3)` runs
`−6,−7,…,−14` and `−5,−6,…,−13` respectively. The surplus at the shielded vertex is **paid for
by its own pendants**, which is the shape the next step must exploit.

## 35.2 The mechanism, in one line — and it explains all four rows

> **A legal trace `T` bounds its vertex iff the hexagon carries an induced path on 5 vertices
> anchored at a vertex of `T` and meeting `T` nowhere else.** Then `u – v – (that 5-arc)` is an
> induced **P₇**, so `v` can have no neighbour off `Z ∪ N(Z)`. `{z_0}` has the arc
> `z_0z_1z_2z_3z_4`; `{z_0,z_1}` has `z_1z_2z_3z_4z_5`. **The antipodal pair is the unique legal
> trace with no such arc**: every induced 5-path in C₆ is 5 consecutive vertices, which misses
> only one vertex and therefore either contains both of `z_0,z_3` (so the extension is not
> induced) or is `z_1z_2z_3z_4z_5`, whose anchor `z_1 ∉ T`. **It cuts the hexagon into two arcs
> of 3, and `2 + 3 = 5 < 7`.** An empty-trace vertex inherits the shield, because by the third
> frame table its only `Z`-attached neighbours are antipodal.

## 35.3 Structure corollaries — where the unbounded part actually lives

> **(i) THE SHIELD.** Every vertex at distance 2 from `Z` attaches **only** to `W_anti` vertices.
> Since each antipodal slot holds at most one vertex (§34.4a), **`|W_anti| ≤ 3`**, so the whole
> of `W_0` hangs off **at most three vertices**.
> **(ii) DEPTH.** Every vertex of `G` is within distance **3** of `Z`. Distance 4 is refuted at
> **all three** antipodal slots by an induced P₇ (witnesses printed) and **never** by a C₄;
> distance 3 **is** reached, so the bound is sharp.
> **(iii)** Hence `V = Z ⊔ W_1 ⊔ W_cons ⊔ W_anti ⊔ W_0` with `|W_cons| ≤ 3`, `|W_anti| ≤ 3`,
> every vertex of `W_1 ∪ W_cons` of degree `≤ 4` and charge `≤ 0`, and **all remaining mass
> confined to at most three antipodal branches of depth ≤ 2.**

## 35.4 PROVENANCE, run before anything here was written (RULING BF) — and it fired again

* **`G32` (§20.1, round 8/9) is the P₆-level shadow of this statement, and it is STRONGER
  there:** under *no induced P₆*, `W_1` and `W_cons` are **EMPTY** — every off-`Z` vertex has an
  empty or antipodal trace. §27.2 (round 12) named the open problem in exactly these words:
  ***"a P₇-analogue of G32 must be proved."***
  **This round answers that, and the answer is that the analogue in EXCLUSION form is FALSE.**
  `W_1` and `W_cons` are non-empty in hypothesis — CE-2's vertex `4` has a consecutive trace
  (§27.2), and this round's two maximisers are explicit `n = 9` in-hypothesis witnesses for both
  classes. **What is true at P₇ level is the BOUNDED form, `d ≤ 4` and `a ≤ 3`.**
* **The TECHNIQUE is prior art on this very line, and must not be presented as new.**
  §19.4 **Lemma G30** and §20.3 **Lemma G34** (round 8/9) both run exactly this argument:
  *take an induced P₅ ending at the vertex; no induced P₆ extends it; hence every further
  neighbour is adjacent to one of the path's vertices; then C4-freeness allows at most one
  neighbour per apex.* This round transposes it from the RES(b) frame to the hexagon itself and
  from P₆ to P₇ — where the 5-arc requirement is what creates the antipodal exception.
* **`G54`** (trace `≤ 2`, consecutive or antipodal) and **`|W_anti| ≤ 3`** (§34.4a) are **used as
  inputs and not re-proved.**
* **NEW here, and this is the whole list:** the four-row table with **exact, attained** maxima;
  the two in-hypothesis unboundedness families; the shield; distance `≤ 3`; the charge statement
  (e); and the finding that the exclusion form of the P₇-analogue is false.
* **TIER, proposed: Lemma / elementary + finite enumeration. NOT an S1 candidate. Closes no
  pocket.** It is, however, the **first bound on the off-cycle term** and it changes (D3-C6)'s
  shape. **UNREGISTERED. No number minted** — `G58` is the next free address and the owner does
  not self-promote; the numbering call is the planner's.

## 35.5 The honest answer to "can it be bounded without a new hypothesis?" — **NO for the `= 0` half, and the hypothesis is named**

**It cannot.** FAMILY-U is in hypothesis and has `|N(v) ∩ Z| = 0 ≤ 1` with `a(v)` unbounded, so
**no vertex-wise bound over the class `|N(v) ∩ Z| ≤ 1` exists.** The hypothesis that would
restore one:

> **(NO-ANTI)** *no off-cycle vertex has an antipodal `Z`-trace*, i.e. **`W_anti = ∅`.**

Under (NO-ANTI): by the shield `W_0 = ∅` as well, so `V = Z ⊔ W_1 ⊔ W_cons`, **every vertex lies
within distance 1 of `Z`**, every off-cycle vertex has `d ≤ 4` and `a ≤ 3`, and the whole
off-cycle term is `≤ 0` outright. **Priced by §27.3's own kill-table discipline: (NO-ANTI) is a
PURCHASE, not free** — FAMILY-A is in-hypothesis with `W_anti ≠ ∅`, so the live class does not
imply it. It is recorded as a declared surcharge, not adopted.

**But the more useful reading is structural, and it does not cost a hypothesis:** by §35.3 the
unbounded part is *confined* to at most three antipodal branches of depth ≤ 2, and on both
families the branch **pays for itself** (`Σ(a−3)` strictly decreasing in `k`). **So the next step
is a PER-BRANCH discharging bound, not a vertex-wise one** — show that each antipodal branch
contributes `≤ 0` (or a constant) to `Σ_v(a(v)−3)`, against a `Z ∪ W_1 ∪ W_cons` part that is
now fully controlled except for the `+1` each `W_1` vertex contributes to the `Z`-term.
**That is the named next step, and it is a bounded, self-contained question.**

## 35.6 Owner errors and near-misses, reported rather than repaired away

1. **All four of my hand-derived bounds were wrong — too weak, and the weakness was the whole
   point.** The counting argument gave `d ≤ 5, a ≤ 4` (single) and `d ≤ 6, a ≤ 5`
   (consecutive). The truth is `4/3` in both. **`a ≤ 4` permits charge `+1`; `a ≤ 3` forbids it**,
   so the non-sharp bound would have left §35.1(e) — the only clause with teeth — unavailable.
   Two distinct causes: for the consecutive anchor I **missed the C₄s that run through the
   trace's own edge** (`w ~ z_0,z_1` already makes `z_1` a common neighbour of `w` and `z_0`);
   for the single anchor **no counting argument can see the pairwise obstruction between
   surviving neighbour traces**, only the enumeration can.
2. **My hand-built attainment witness was OUT OF HYPOTHESIS.** "INSTANCE-G" (`v ~ z_0`, plus
   `s_2,s_3,s_4` at `z_2,z_3,z_4`) was written to exhibit `a(v) = 4`. It contains an induced P₇:
   `z_1 z_2 s_2 v s_4 z_4 z_5`. **The `admit()` precondition caught it before a single statistic
   was read** — which is precisely the failure RULING BM was adopted to prevent, arriving one
   round later in the same file that implements the rule.
3. **RULING BM bit its author in the OPPOSITE direction, and that is a second species.** My first
   frame table asserted **connectedness** on frames. A frame is an **induced subgraph**;
   C4-freeness, P₇-freeness and "`Z` is an induced C₆" are inherited, **connectedness is not**.
   So the empty-trace frame in the third table was rejected from a population it belongs to.
   Round 22's error **admitted samples that were out of hypothesis**; this one **rejected samples
   that were in it**. **Same defect, opposite sign: the membership test must match the object it
   is applied to.** Repaired by `mode="frame"`, which asserts exactly the inherited clauses — and
   a check now asserts that the distinction *makes a difference* (one edge list, admitted as a
   frame, rejected as a host), so the fix cannot rot into decoration.
4. **Near-miss, prose ahead of its `.out`.** The mint-gate note in this file's first draft read
   "`W_1` is REFUSED as a mint (it resolves already)". The run reports **0 occurrences**: the
   sentence was written from an expectation, not from the log. Corrected before the `.out` was
   final. **`W_1` is the round's one mint**, gate-checked at mint time, and it completes the
   existing `W_0 / W_cons / W_anti` family rather than opening a new one.
5. **The gate needed repairing to stay a PRECONDITION, and the repair is the round's small
   general finding.** Run after §35 shipped, the round-22 mint gate reports `W_1` **12 times**
   and turns red — on the round's own mint. Round 22 handled that by *hedging in prose*
   ("run BEFORE the repair these are all 0"), and **prose is not a check**. The fix is not to
   relax the gate but to **pin the corpus boundary**: the draft was **4557 lines** before §35 was
   appended, and the assertion is now *"0 occurrences at or before line 4557"* — which is
   **exactly the mint-time question, and it stays answerable for ever.** Under the pinned gate
   `W_1` has **0 pre-existing occurrences** and `G58` has **1**, at line 4432, inspected and
   confirmed to be round 22's prose *about* addresses rather than an address. Independent
   corroboration that §35 minted **exactly one** symbol: the definition table went from
   **19 symbols / 27 sites** to **20 / 28**.

---

# §36 owner-w133 round 24 (2026-08-23 03:3x–04:2x CDT, opus) — **THE PER-BRANCH DISCHARGING BOUND**: the antipodal branches pay for themselves, so the **ENTIRE off-cycle term is `≤ 0`**

Full record: `orchestration/results/w133_state.md` §"Round 24", which is the authority.
Machine record: `problems/wowii/w133_r24_branch.py` → `.out`, **exit 0, 41 checks, 0 failures,
128.74 s**. Rulings executed: **BU** (the §27.2 correction is entered at §27.2 itself, above),
**BV** (the membership test is written against the object it tests — frame or host),
**BW** (every load-bearing bound is machine-enumerated, never hand-counted),
**BX** (the mint gate runs against a *pinned* corpus boundary), **BF**, **BB**, and the
proof-carrying rule for UNREGISTERED entries.

## 36.1 The statement — **UNREGISTERED, carrying its proof; no number minted**

Hypotheses throughout are (D3-C6)'s, byte-for-byte: `G` connected, **C4-free**,
`Z = (z_0,…,z_5)` an induced C₆, **no induced P₇**. Write `R := W_anti ∪ W_0` — the set to
which **G58** (§35) confined the whole off-cycle surplus — and `m := |W_anti| ≤ 3`.

> **(B) THE PER-BRANCH BOUND.** `Σ_{v ∈ R} (a(v) − 3) ≤ 0`, **and 0 is ATTAINED.**
>
> **(B′) COROLLARY, and it is the reason (B) was the named target.** With G58's
> `a(v) − 3 ≤ 0` on `W_1 ∪ W_cons`, the **entire off-cycle term is non-positive**:
> `Σ_{v ∉ Z} (a(v) − 3) ≤ 0`.

Round 23 proved that **no vertex-wise bound on `R` exists** (FAMILY-A and FAMILY-U are in
hypothesis with `a(v) = k+2` and `k+1`). (B) is therefore not a weakening of a bound that was
available: it is a bound of a **different shape**, on a set where the vertex-wise one is
**refuted**. The mechanism is the one round 23 read off the two families — `Σ(a−3)` is strictly
decreasing in `k` on both, i.e. the shielded branch pays for itself — and it is now a theorem
rather than an observation on two families.

**Attainment**, `n = 10`, re-admitted as a **host** (not a frame) before its charge was read:
`Z + u_a(z_0,z_3) + u_b(z_1,z_4) + u_c(z_2,z_5) + x` with `x ∼ u_a,u_b,u_c` and `x` having no
`Z`-neighbour. C4-free ✓, `Z` induced ✓, longest induced path **5** ✓, `Σ_R(a−3) = 0` exactly.
So (B) is **best possible**: `≤ −1` is false.

### 36.1.1 The proof, and every step of it is an exhaustive enumeration

**(R0) REDUCTION — `W_1 ∪ W_cons` may be deleted and no `a(v)` on `R` moves.**
Exhaustive 64-frame table at each of the three antipodal slots: an off-`Z` neighbour of an
antipodal `u` has trace exactly `∅`, `{z_i}` or `{z_{i+3}}` — **3 survivors of 64, at all three
slots**. So a `W_1` neighbour of `u` is adjacent to a vertex of `u`'s own trace, i.e. it is a
**triangle apex at `u`**: it adds 1 to `d(u)` **and** 1 to `t(u)`, and `a = d − t` (G[N(v)] is a
matching, G55). Machine: **6 of 6 `(slot, z)` pairs leave `a(u)` unchanged.** And `W_cons`
vertices never touch `R` at all — the **SHIELD** re-run as an exhaustive table over all legal
nonempty traces: an empty-trace vertex may hang **only** on an antipodal vertex.
*Hence (B) may be proved on hosts whose only off-`Z` vertices lie in `R`, which is exactly the
space PART 5 enumerates.*

**(S1) `W_anti` is an INDEPENDENT set.** All **9** ordered slot pairs with `u ∼ u'` asserted are
**refuted, every one of them by a C₄** — e.g. `u ∼ z_0`, `u' ∼ z_1`, `z_0 ∼ z_1`, `u ∼ u'` makes
`z_0` and `u'` two common neighbours of `u` and `z_1`. **Liveness:** the same two vertices
**non-adjacent** are in hypothesis at **3 of 3** pairs, so S1 is a restriction and not a vacuity.
Same-slot doubling is refuted by a C₄ at **3 of 3** slots, which is §34.4a's `|W_anti| ≤ 3`
**used, not re-proved**.

**(S3) The distance-3 population is completely determined, and its charge is EXACTLY `−2`.**
Frame: `Z + u`(antipodal) `+ x`(empty trace, `∼ u`) `+ y`(empty trace, `∼ x`, `≁ u`) `+ w ∼ y`,
with `w`'s **64 traces × its adjacency to `u` and to `x`** — **256 frames, 5 survive, 251
refuted**, and the two refutation mechanisms are **distinct and both printed**:
* `w` free of `u` and of `x` with empty trace → **induced P₇** `z_1 z_2 z_3 u x y w`, and by
  nothing else;
* `w ∼ u` instead → **C₄** (`u` and `y` would have the two common neighbours `x, w`).

*(Round 27 clarification, entered here at the site rather than downstream — RULING BU. The
number **5** is a count over the full **256-frame** population, **not** a census of distance-3
shapes: the independent re-implementation finds that **4 of the 5 survivors have `w` carrying an
ANTIPODAL trace**, so in those `y` sits at distance **2**, not 3. Restricted to `w` of **empty
trace** — the genuine distance-3 configurations — exactly **1** survives, and it is the triangle
(`w ∼ x`, `w ≁ u`). With the no-`w` case that is the pendant/triangle pair below. The count and
the conclusion are both correct as written; only the reading of "5" as a shape census is not.)*

A second exhaustive table puts a **second distance-2 vertex** on `y` (a second antipodal anchor,
both remaining slots): **both frames refuted, by an induced P₇.** Hence a distance-3 vertex has
**exactly one** distance-2 neighbour and at most one further neighbour, which must be adjacent to
that same distance-2 vertex. Both surviving shapes are exhibited as **hosts**: a pendant
(`d = 1`) and the triangle (`d = 2, t = 1`). **In both, `a = 1` and the charge is `−2`.**

**(S4) THE DISCHARGING RULE.** *Every `u ∈ W_anti` sends 1 to each of its distance-2 neighbours;
every distance-2 `x` sends 1 to each of its distance-3 neighbours.* Writing
`α(x) = |N(x) ∩ W_anti|`, `Q(x) = N(x) ∩ D_2`, `P(x) = N(x) ∩ D_3`:

| vertex | final charge | bound |
|---|---|---|
| `u ∈ W_anti` | `\|W_1(u)\| − 1 − t(u)` | **`≤ −1`** (R0: `t(u) ≥ \|W_1(u)\|`) |
| `y ∈ D_3` | `−2 + 1` | **`= −1`** (S3) |
| `x ∈ D_2` | `2α(x) + \|Q(x)\| − t(x) − 3` | see S5 |

**(S5) The distance-2 verdict — and THE OWNER'S HAND CLAIM HERE WAS WRONG, WITH THE MACHINE
SAYING THE OPPOSITE.** The core table enumerates **two adjacent distance-2 vertices whose anchor
sets range over ALL 7 nonempty subsets of `{u_a,u_b,u_c}`** — **49 frames, 9 survive, 40
refuted** — and the survivor set is
`([0],[0]), ([1],[1]), ([2],[2]), ([0],[0,1,2]), ([1],[0,1,2]), ([2],[0,1,2])` and its three
transposes. **Every survivor SHARES an anchor.** The hand argument had predicted the exact
opposite (that the two must be anchored on *different* antipodal vertices, via an induced P₇
`z_3 z_2 z_1 u_b x' x x''`); the enumeration says a shared anchor is **forced**, and a shared
anchor is a **triangle at `x`**. So:

> **`|Q(x)| = 1 ⟹ t(x) ≥ 1`**, and the anchor multiset of an adjacent distance-2 pair is always
> `{1,1}` or `{1,3}` — **an `α = 2` vertex never has a distance-2 neighbour at all.**

A second exhaustive table gives `x` **two** distance-2 neighbours, anchor sets again over all
subsets and the far pair adjacent or not: **686 frames, 0 survive**, so **`|Q(x)| ≤ 1`**.
Together: `final(x) ≤ 2α(x) − 3`, i.e. **`≤ −1` when `α(x) = 1`**, `≤ +1` at `α = 2`, `≤ +3` at
`α = 3`.

**(S6) The multiply-anchored budget closes the sum.** Two distinct vertices sharing **two**
anchors are refuted **by a C₄ even when non-adjacent** (machine), so each antipodal **pair**
carries at most one common neighbour: `Σ_{α(x) ≥ 2} C(α(x),2) ≤ C(m,2)`. Enumerating the
feasible `(m, #\{α=2\}, #\{α=3\})` — **8 cases** — gives `Σ_{α(x) ≥ 2} final(x) ≤ m` in **every**
one of them, with **equality at exactly two**: `m = 3` with three `α = 2` vertices, and `m = 3`
with one `α = 3` vertex. Hence

> `Σ_R (a−3) = Σ_R final ≤ (−m) + m + (−|D_3|) ≤ 0`. ∎

**(S7) INDEPENDENT EXHAUSTIVE CONFIRMATION, and the population is on the face of the log.**
By (R0) it suffices to enumerate hosts whose off-`Z` vertices all have an **empty or antipodal**
trace. Every such host with **at most 6** off-`Z` vertices is generated by DFS, pruned by
C4-freeness and P₇-freeness — **both inherited by induced subgraphs, so the pruning is sound**:
**195 501 in-hypothesis regions**, distributed `1 / 4 / 20 / 158 / 1614 / 16 388 / 177 316`
by `|off-Z| = 0…6`. **Maximum `Σ_R(a−3)` observed: `+0`**, per size `0, −1, −2, −1, 0, −1, −2`.
The two sizes attaining 0 are `|off-Z| = 0` (vacuous) and `|off-Z| = 4` (the `n = 10` witness
above). This is a **second, independent** route to the bound over a bounded window, and it is
where the attainment came from.

## 36.2 What (B) does and does not buy — stated against the round's own interest

**It does not close (D3-C6), and it does not close a pocket.** The global count is
`Σ_v(a(v)−3) = Σ_{z∈Z}(a(z)−3) + Σ_{v∉Z}(a(v)−3)`, and (B′) makes the **second** summand
`≤ 0` — the whole off-cycle half, which has been the open half since §34.4b. **The `Z`-term is
the remaining open half, and it is NOT `≤ 0`:** §34.4b exhibits, in hypothesis, hexagon `+ k`
independent single-trace vertices at `z_0` with the `Z`-term growing without bound. G55 summed
says exactly where that comes from, and the identity is machine-checked on four in-hypothesis
instances this round (0 discrepancies):

> `Σ_{z∈Z}(a(z) − 3) = |W_1| + 2|W_cons| + 2|W_anti| − Σ_{z∈Z} t(z) − 6`.

| instance | `n` | `\|W_1\|` | `\|W_cons\|` | `\|W_anti\|` | `\|W_0\|` | `Z`-term | off-term | `R`-term | total |
|---|---|---|---|---|---|---|---|---|---|
| INSTANCE-D | 9 | 0 | 3 | 0 | 0 | `−6` | `−6` | `0` | `−12` |
| INSTANCE-E | 12 | 0 | 3 | 3 | 0 | `0` | `−9` | `−3` | `−9` |
| **attaining region** | 10 | 0 | 0 | 3 | 1 | `0` | `0` | **`0`** | `0` |
| §34.4b fan, `k = 7` | 13 | 7 | 0 | 0 | 0 | `+1` | `−14` | `0` | `−13` |

> **THE RESIDUAL, named and bounded.** The `Z`-term's `+|W_1|` is paid only if
> `Σ_{v ∈ W_1}(a(v) − 2) ≤` the slack in the rest. **G58 gives `a(v) ≤ 3` on `W_1` and the value
> 3 is ATTAINED**, so a single `W_1` vertex can leak `+1`. **That, and not the off-cycle term, is
> now the next gap.** It is bounded, it is named, and it is **not** closed here.

## 36.3 PROVENANCE, run before anything here was written (RULING BF)

* **The target is round 23's own, named at §35.5 before it was met** — the phrase *"a PER-BRANCH
  discharging bound, not a vertex-wise one"* occurs **once** in the draft at or before the pinned
  boundary, at line 4735. **This round therefore mints no name for it**; it discharges a target
  the ledger already carried. *(The gate is **case-insensitive**: a case-sensitive gate reported
  this phrase as **0** occurrences because round 23 wrote it in capitals — see §36.4 item 3.)*
* **`G54`, `G55`, `G57` and `|W_anti| ≤ 3` (§34.4a) are USED as inputs and not re-proved.**
  **`G54` and `G57` are machine-asserted** to have ≥ 1 occurrence at or before the pinned
  boundary (10 each). The probe for the literal string `|W_anti| <= 3` returned **0**, and that
  is a **probe defect, not a ledger defect** — the draft writes it with the unicode `≤`. Reported
  rather than papered over; see §36.4 item 3, of which it is a second instance.
* **`G58` (§35) is the direct input**: (B′) is (B) **plus** G58 and nothing else.
* **The TECHNIQUE is discharging**, which is textbook — the annotation must travel with any
  citation. What is not textbook here is *which* rule works, and that was settled by enumeration
  rather than by design: see §36.4 item 1.
* **NEW here, and this is the whole list:** (B) with its attainment; (B′), i.e. that the entire
  off-cycle term is non-positive; the reduction R0 (deleting `W_1 ∪ W_cons` moves nothing on
  `R`); `W_anti` independent; the exact distance-3 classification with charge `≡ −2`;
  `|Q(x)| ≤ 1` with `|Q| = 1 ⟹ t ≥ 1`; and the identification of the `W_1` leak as the residual.
* **TIER, proposed: Lemma / elementary + finite enumeration (discharging). NOT an S1 candidate.
  Closes no pocket.** It is, however, the statement that turns the off-cycle half of (D3-C6)
  from open into settled. **UNREGISTERED. No number minted** — `G59` is the next free address and
  the owner does not self-promote; the numbering call is the planner's.

## 36.4 Owner errors and near-misses, reported rather than repaired away

1. **My hand claim about adjacent distance-2 vertices was wrong, and the machine says the
   OPPOSITE — this is RULING BW firing on the same author one round later.** The hand argument
   (an induced P₇ `z_3 z_2 z_1 u_b x' x x''`) concluded that two adjacent distance-2 vertices
   must be anchored on **different** antipodal vertices. The 49-frame enumeration shows every
   surviving pair **shares** an anchor. **And the direction matters to the result**: a shared
   anchor is a triangle at `x`, which is what makes `|Q(x)| = 1 ⟹ t(x) ≥ 1` and therefore
   `final(x) ≤ −1` at `α = 1`. Under my wrong version `final(x)` would have been `≤ 0` there,
   the `α = 2` and `α = 3` rows would not have been paid, and **S6 would not have closed.**
   The wrong claim was not merely weaker; it pointed the other way.
2. **A second hand bound, discarded before it was written down.** My first budget used
   `Σα(x) ≤ |D_2| + 3` and the crude `final(x) ≤ 2α(x) − 2`; that gives `+4 > m = 3` at `α = 3`
   and does **not** close. The enumeration's `|Q| = 1 ⟹ t ≥ 1` is what turns `2α − 2` into
   `2α − 3` and closes it. Two hand attempts, both wrong, one in each direction.
3. **The mint gate was case-blind, and that is a gate a change of case walks through.** The first
   run reported `per-branch` as **0** occurrences before the pinned boundary — while round 23 had
   written **`PER-BRANCH`** at line 4735. The check would have licensed the claim *"this round
   names the target"*, which is false: round 23 named it. **Repaired by making the pinned gate
   case-insensitive and printing both counts**, so the discrepancy stays visible rather than
   being smoothed away. This is RULING BX's pattern extended by one clause: pin the boundary
   **and** normalise the token, or the gate is decoration.
   **And the same defect appears a second time in the same run, uncaught by the repair:** the
   provenance probe for `|W_anti| <= 3` reports **0** occurrences because the draft writes `≤`,
   not `<=`. Case was normalised; **unicode was not.** The two ledger inputs that actually carry
   load — `G54`, `G57` — are asserted, not merely printed, which is why the run is still sound;
   the string probes beside them are **evidence, not checks**, and are now labelled as such.
4. **The pinned boundary this round is 4779, not 4756.** Line 4756 was the draft's length at the
   end of round 23; this round's **§27.2 correction (RULING BU) is entered above `§35`**, so it
   shifts every later line. The boundary is therefore pinned at the draft's length **immediately
   before §36 was appended** (4779), and the §27.2 correction is inside it — deliberately: it
   mints nothing, it only corrects a target. Recorded so the number is auditable rather than
   mysterious.
5. **Self-limit exceeded.** The task book set a hard 45-minute self-limit; this round ran over it
   during the exploratory search that preceded the script. Reported, not hidden.

## 36.5 Standing items, not quietly dropped

* **GATE A is strong in conjunction only.** This round ran **no gate, no engine call, no quota,
  no browser lease** — own-attack only. There is no verdict to be strong about.
* **(T-C)**, **(D3-C6)**, **pocket-2 `μ=1` / A2** all remain **OPEN**. **No pocket closed ⟹ no
  mathematics milestone.**
* **A2 stays queued**; the legacy `A`/`C`/`H` renames stay deferred to their next natural
  rewrites, sense counts still pinned at `{A:3, C:2, H:3}`.
* The **≤ 6 corollary** (§34.4a) stays **UNREGISTERED carrying its proof**, as ruled.
* **Meta/muse-spark remains DISQUALIFIED** as the S3 vote on the P7G32 output.

---

# §37 owner-w133 round 25 (2026-08-23 04:3x–05:3x CDT, opus) — **THE Z-TERM / THE `W_1` LEAK: (D3-C6) CLOSES.** `Σ_v (a(v)−3) ≤ n_3 + 2m − 6` and `n_3 + 2m ≤ 6`, both sharp — plus **REGISTRY: `G59` is MINTED for round 24's (B)/(B′)** on the planner's delegated numbering call

Full record: `orchestration/results/w133_state.md` §"Round 25", which is the authority.
Machine record: `problems/wowii/w133_r25_zterm.py` → `.out`, **exit 0, 39 checks, 0 failures,
184.17 s**. Rulings executed: **CG** (the string probes are EVIDENCE, not CHECKS — and the mint
gate is rebuilt in a form that *cannot* miss by encoding), **BW** (every load-bearing bound is
machine-enumerated; it bit the author twice again this round, once fatally — §37.5),
**BX** (pinned corpus boundary, **draft line 4993**), **BV**, **BM**, **BF**, **BB**.

## 37.1 The statement — **UNREGISTERED, carrying its proof; `G60` left free**

Hypotheses are (D3-C6)'s, byte-for-byte (§27.4): `G` connected, **C4-free**, `Z = (z_0,…,z_5)`
an induced C₆, **no induced P₇**. Write `m := |W_anti|` and

> `n_3 := #{ v ∈ W_1 : a(v) = 3 }`  — the **LEAKING** vertices, the residual round 24 named.

> **(Z1) THE COUNT COLLAPSES.** `Σ_{v∈V}(a(v) − 3) ≤ n_3 + 2m − 6`.
> **(Z2) A LEAK HAS A SHAPE.** If `v ∈ W_1` has trace `{z_i}` and `a(v) = 3` then `d(v) ∈ {3,4}`
> and `N(v)∖{z_i}` is **2 or 3 single-trace `W_1` vertices**, at `z_{i+2},z_{i+3}` or
> `z_{i+3},z_{i+4}` or all three (then with exactly the `+2 ∼ +4` edge). **Every leak has a
> `W_1` neighbour at its OWN ANTIPODE**, and **no** neighbour of a leak lies in `Off(z_i)`.
> **(Z3)** At most **one** leak per hexagon vertex.
> **(Z4)** Two leaks can sit **only at ANTIPODAL** hexagon vertices. With (Z3): **`n_3 ≤ 2`**.
> **(Z5)** A leak coexists with **at most one occupied antipodal slot**: `n_3 ≥ 1 ⟹ m ≤ 1`.
> **(Z6)** Hence **`n_3 + 2m ≤ 6`**, and therefore
>
> > ### `Σ_{v∈V}(a(v) − 3) ≤ 0` for every graph in (D3-C6)'s class — **this is (D3-C6)**.

**Both extremal regimes are ATTAINED, so (Z1) and (Z6) are sharp and not slack:**
`(n_3,m) = (0,3)` at round 24's `n = 10` region (`Σ(a−3) = 0`, bound `0`), and
`(n_3,m) = (2,0)` at a **new** `n = 10` region exhibited here (`Σ(a−3) = −4`, bound `−4`):
`Z + v(z_0) + v'(z_3) + x(z_2) + y(z_1)` with `v ∼ v', x` and `v' ∼ v, y` — C4-free ✓,
`Z` induced ✓, longest induced path 6 ✓, **two leaks, antipodal, as (Z4) requires**.

### 37.1.1 The proof, and every step of it is an exhaustive enumeration

**(Z1) is arithmetic on three inputs that are USED, not re-proved.** G55 summed gives
`Σ_{z∈Z}(a(z)−3) = |W_1| + 2|W_cons| + 2|W_anti| − T_Z − 6` with `T_Z := Σ_{z∈Z}t(z)`
(re-verified as an identity on **5** in-hypothesis instances, 0 discrepancies). Then
**`T_Z ≥ 2|W_cons|`** — each consecutive-trace `w` makes a triangle with the hexagon edge it
spans and is counted **once at each end** (machine: **exactly 2, at all 6 hexagon edges**).
G58 gives `a ≤ 3` on `W_1 ∪ W_cons`, so `Σ_{W_cons}(a−3) ≤ 0` and `Σ_{W_1}(a−2) ≤ n_3`;
**(B)** gives `Σ_R(a−3) ≤ 0`. Assembling:
`Σ_v(a−3) ≤ (2m − 6) + Σ_{W_1}(a−2) ≤ n_3 + 2m − 6`. ∎

**(Z2) — 152 neighbourhood configurations, 17 in hypothesis, 135 refuted.** The traces of
`N(v)∖Z` are pairwise **disjoint** (two neighbours sharing a `z` are two common neighbours of
`v` and that `z`: a C₄) and each is drawn from §35.1.1's **7 survivors of 64**; with the free
adjacency bits *inside* `N(v)` this determines `G[N(v)]` **completely**, so the table is exact,
not an upper bound. Realised `(d,a)`: `(1,1),(2,1),(2,2),(3,2),(3,3),(4,3)`. **Exactly three**
shapes carry `a = 3`, all listed above. Two corollaries that the round then spends:
**every leak has an antipodal `W_1` neighbour**, and **a leak contributes 0 to `Σ_z e(Off(z))`**
— which is the *opposite* of what the owner's first payment mechanism assumed (§37.5 item 1).

**(Z3), (Z4) — the frames are `Z + N[v] + N[v']`, and they are enumerated COMPLETELY.**
If a host carries two leaks, the induced subgraph on `Z ∪ N[v] ∪ N[v']` is in hypothesis (C4-,
P₇-freeness and "`Z` induced" are inherited), it contains **all** of `N(v)` and `N(v')`, so
`a(v)`, `a(v')` read off it are **exact**; and because `N(v)` is *exactly* `{z_i} ∪ X`, the
vertex `v` is non-adjacent to everything else in the frame — which is what makes the free-bit
set small enough to enumerate. Every shape pair, **every identification pattern** (`v'` may
itself be a neighbour of `v`; their far neighbours may coincide) and every free bit:

| positions | frames | survive |
|---|---|---|
| same hexagon vertex `z_0` | **832** | **0** |
| `z_0 & z_1` | **832** | **0** |
| `z_0 & z_2` | **858** | **0** |
| `z_0 & z_3` (antipodal) | **872** | **2** |
| `z_0 & z_4` | **858** | **0** |
| `z_0 & z_5` | **832** | **0** |

> **WHAT THESE POPULATIONS ARE (round 31, so that they are auditable rather than merely
> printed).** A table's `N` is **not** a product of free bits — a product of free bits is a
> power of two, and `832 = 2⁶·13`, `858 = 2·3·11·13`, `872 = 2³·109` are not. Each table is a
> **sum over branches**, `N = Σ_b (2^{f_b} − dup_b)`, a branch being (shape of `N[v]`, shape of
> `N[v']`, whether `v ∼ v'`, which far neighbours are **identified**), `f_b` its free-bit count
> and `dup_b` the assignments whose edge list degenerates. Different branches carry different
> `f_b`, so no single free-bit set describes a table at all. Worked out for the live row
> `z_0 & z_3`: 18 branches, `f_b ∈ {1,2,4,6,9}`, summing to **872** — printed in full at
> `problems/wowii/w133_r31_frames.py` → `.out`, a second implementation that also reproduces
> `832/832/858/872/858/832` and the survivor counts `0/0/0/2/0/0`.
> The same shape applies to (Z5): `32 = 2³ + 2³ + 2⁴` over three branches, **not** `2⁵` — so
> `32` satisfies a free-bit-product test *by accident*, with no branch having five free bits.

So leaks sit at **distinct** hexagon vertices and any two of them are **antipodal**; since
antipodality is a perfect matching on the hexagon, **three leaks are impossible: `n_3 ≤ 2`.**
The antipodal row is **live** (2 survivors, promoted to the `n = 10` host above), so (Z4) is a
restriction and not a vacuity.

**(Z5) — `Z + N[v] +` the `W_anti` vertices themselves.** Their own neighbourhoods are not
needed: a refutation on a subframe refutes every host containing it. The `w`-to-`N[v]` bits
**and** the `w`-to-`w'` bit are enumerated, not assumed.
*One* occupied slot: **32 frames at each of the 6 leak positions, survivors 2,1,1,2,1,1** — so a
leak and an occupied slot **do** coexist, and the owner's second hand claim (that they cannot)
was **false**. *Two* occupied slots: **768 frames at each of all three slot pairs
`{(0,3),(1,4)}, {(0,3),(2,5)}, {(1,4),(2,5)}`, and 0 survive.* Hence `n_3 ≥ 1 ⟹ m ≤ 1`.
> **ERRATUM.** This paragraph read **384** until it was re-measured. Both machines print
> **768** — `w133_r25_zterm.out` (re-run and reproduced at `w133_r31_r25_rerun.out`) and an
> independent second implementation, `w133_r31_frames.py` → `.out`, which decomposes it as
> `768 = 2⁷ + 2⁷ + 2⁹` over the three leak shapes. A hand-transcribed population, wrong by a
> factor of two. **The conclusion is untouched**: the survivor count is 0 either way, so
> `n_3 ≥ 1 ⟹ m ≤ 1` stands. What was wrong was a printed number, not a step.

**(Z6) — the finite arithmetic, over every feasible pair.** With `n_3 ≤ 2`, `m ≤ 3` (§34.4a) and
`n_3 ≥ 1 ⟹ m ≤ 1`, the feasible `(n_3,m)` population is **8 pairs**, and `n_3 + 2m ≤ 6` on
**all 8**, with equality only at `(0,3)`. ∎

**INDEPENDENT EXHAUSTIVE CONFIRMATION, populations on the face of the log.**
*Sweep A*, every legal trace, `|off-Z| ≤ 5`: **802 853 in-hypothesis regions**
(`1/16/272/4274/59 406/738 884`, of which `1/15/240/3456/42 168/435 126` are connected hosts),
**max `Σ(a−3) = +0`** (per size `−6,−5,−4,−3,0,−1`), **max `n_3 = 2`**, and **0 violations** of
either (Z1) or (Z6) on any host. *Sweep B*, single traces only — the class in which a leak's
entire neighbourhood lives — `|off-Z| ≤ 6`: **90 859 regions**, **max `n_3 = 2`**, 0 violations.
Both sweeps are pruned by C4- and P₇-freeness, **both inherited by induced subgraphs, so the
pruning is sound**, and both are complete: the wall-clock guard is `exit(2)`, never a silent
`return` (§37.5 item 4).

## 37.2 What this does and does not buy — stated against the round's own interest

**It closes (D3-C6) as stated at §27.4**, and by §27.4's own conditional corollary it therefore
closes **pocket 1's `D = 3` Case-2 residual inside the live class**. That corollary is the
planner's to adjudicate, not the owner's to bank: **no pocket is marked closed here.**

**And the honest half is the shape of the closure, not a gap in it.** (D3-C6) now rests on a
**chain** — G54, G55, G57, §34.4a, **G58 (§35)**, **(B)/(B′) (§36, minted `G59` below)**, and
this entry — of which the last three are **own-attack results that have never been through GATE
A or any external check**. Every link is machine-enumerated and every population is printed, but
**the whole chain is owner-produced**, and a chain is exactly as strong as its weakest
unverified link. The claim to make is *"(D3-C6) is proved modulo the round-23/24/25 own-attack
results"*, and the natural next move is a **verification gate on the chain**, not a new front.
**(T-C)**, **pocket-2 `μ=1` / A2** and **(D3-NOP7)** (the C₆-free strengthening, §27.4) are
untouched.

## 37.3 REGISTRY — **`G59` is MINTED** for round 24's (B)/(B′), on the planner's delegated call

The r25 task book delegated the numbering call on (B)/(B′) to the owner. **The call is YES**, and
the reason is not merit but **citability**: (B′) is a load-bearing input of §37.1.1 above, cited
by name, and a statement used by name inside another proof needs an address.

> **`G59` (Lemma — elementary + finite enumeration; discharging).** Under (D3-C6)'s hypotheses,
> with `R := W_anti ∪ W_0`: **(i)** `Σ_{v∈R}(a(v) − 3) ≤ 0`, and **0 is attained** (`n = 10`);
> **(ii)** with G58, `Σ_{v∉Z}(a(v) − 3) ≤ 0` — the entire off-cycle term is non-positive.
> *Proof:* §36.1.1 (R0/S1/S3/S4/S5/S6), independently confirmed over **195 501** reduced regions
> (§36, S7). *Novelty, stated against interest:* the **technique is textbook discharging**; what
> is not textbook is *which* rule works, and that was settled by enumeration rather than design.
> **Not an S1 candidate. Closes no pocket by itself.**

**The mint gate is rebuilt so that it cannot miss by ENCODING (RULING CG).** A probe asks *"is
`G59` absent?"* and answers *"yes"* whenever it cannot read the token — round 24 was burned by
this twice, once in case and once in unicode. The replacement **enumerates the whole address
population and asserts it is CONTIGUOUS**: `G0…G59`, **60 distinct, 0 holes**. An address written
in an encoding the scanner misses would open a **hole**, and *a hole is visible*. Absence is then
a **consequence of completeness**, not a probe's silence. Under it, the 2 pre-boundary `G59`
occurrences are printed line by line (4455, 4944) and both are **prose about the next free
address**, neither a registration — **0 registration-shaped occurrences**. `G60` is unoccupied,
so this entry has a free address and **does not need to self-promote to get one**; it stays
**UNREGISTERED carrying its proof**, and the numbering of §37 is the planner's.

## 37.4 PROVENANCE, run before anything here was written (RULING BF)

* **The target is round 24's own, named at §36.2 before it was met** — "the `+1` each `W_1`
  vertex contributes … *that, and not the off-cycle term, is now the next gap*". This round
  therefore **mints no name for the gap**; it discharges a target the ledger already carried.
* **`G54`, `G55`, `G58` and §34.4a's `|W_anti| ≤ 3` are USED as inputs and not re-proved**;
  **(B)** is used and is minted `G59` above. The assertions that carry load are **graph facts
  re-checked in PARTS 1–7**, not string probes — see §37.3 and RULING CG.
* **NEW here, and this is the whole list:** (Z1) with `T_Z ≥ 2|W_cons|`; the leak **shape**
  classification (Z2) with its two corollaries; (Z3); (Z4) — that two leaks are forced
  **antipodal**, hence `n_3 ≤ 2`; (Z5); (Z6); and the consequence that **(D3-C6) holds**. The
  `n = 10` two-leak extremal host is new.
* **TIER, proposed: Theorem (it is the named target (D3-C6) itself), elementary + finite
  enumeration.** Whether it is an S1 candidate is the planner's call and depends entirely on
  whether the chain below it is verified; the owner's own view is that **it should be gated
  before it is called S1**.

## 37.5 Owner errors and near-misses, reported rather than repaired away

1. **My first payment mechanism was VOID, and the machine said the opposite.** I argued that a
   leaking `W_1` vertex must have a neighbour in `Off(z_i)`, so each leak would pay for itself
   through `T_Z ≥ 2|W_cons| + Σ_z e(Off(z))`. **(Z2c): a leak has NO neighbour in `Off(z_i)` at
   all** — it contributes **exactly 0** to that term. The mechanism I was about to build the
   round on does not exist.
2. **My second hand claim was FALSE in the other direction.** I then argued that a leak at `z_i`
   must exclude a `W_anti` at its own slot `(z_i,z_{i+3})`, which would have given the counting
   directly. The enumeration says they **coexist** (2 survivors of 32). The true statement is
   weaker and had to be found by enumeration: a leak excludes the **second** slot, not the first.
   **Two hand claims, both wrong, one in each direction — RULING BW firing on the same author for
   the third round running.**
3. **A hand construction that would have REFUTED (D3-C6), had the hand been right.** Reasoning
   by hand from "each leak needs two far neighbours, and C4-freeness makes them distinct", I
   built `k` leaks at a single `z_0` and computed `Σ(a−3) = k − 6`, i.e. **`+1` at `k = 7`** — a
   counterexample to (D3-C6). **(Z3) says `k ≤ 1`.** The hand construction was not in hypothesis;
   an induced P₇ kills it at `k = 2`. *This is the round's sharpest instance of BW: the hand
   argument did not merely fail to prove the theorem, it "refuted" it.*
4. **THE ONE THAT NEARLY LANDED: a detector that could only ever say NO.** For the bounded
   sweeps I wrote a fast bitmask induced-`P_k` detector instead of reusing the trusted
   `longest_induced_path`. It had an inverted mask and **returned `False` unconditionally at
   length ≥ 2** — so `P₇`-freeness was **never enforced** in the first exploration, which then
   reported `max n_3 = 5` and printed a "witness" with five leaks. I caught it by **decoding
   that witness by hand and finding an induced P₇ inside it**, not by any check I had written.
   **Generalisable, and I propose it as a rule:** *a re-implementation written for speed is a
   NEW tool and inherits NONE of the original's controls; and a detector whose output is a
   NEGATIVE ("no `P₇` here") must be positive-controlled on inputs where the answer is YES,
   because a broken one is silent by construction.* PART 0 now cross-checks it against the
   trusted implementation on **400 random graphs × 3 lengths, 0 mismatches**.
5. **A truncating guard that reports as if complete.** The exploratory sweep used
   `if elapsed > T: return`, which **silently prunes the tail of the search** and prints a
   population that looks like a full enumeration — one such run reported `k ≤ 7` totals that were
   short by ~2 %. The production script's guard is `tick()` → **`exit(2)`**, never `return`.
   *A time guard inside a recursion must abort the process, not the branch.*
6. **Self-limit exceeded again.** The 45-minute limit was passed; the round ran ≈ 75 minutes
   wall-clock, the overrun spent on the exploratory search and on rebuilding the sweep after
   item 4. **Reported, not absorbed.**

## 37.6 Standing items, not quietly dropped

* **GATE A is strong in conjunction only.** This round ran **no gate, no engine call, no quota,
  no browser lease** — own-attack only. There is no verdict to be strong about, and §37.2 says
  plainly that this is the chain's weak point.
* **(T-C)** and **pocket-2 `μ=1` / A2** remain **OPEN**. **(D3-C6) is proved modulo the
  round-23/24/25 own-attack chain**; whether that closes pocket 1's `D = 3` residual is the
  planner's adjudication, and **no pocket is marked closed here**.
* **A2 stays queued**; the legacy `A`/`C`/`H` renames stay deferred, sense counts pinned at
  `{A:3, C:2, H:3}`.
* The **≤ 6 corollary** (§34.4a) stays **UNREGISTERED carrying its proof**, as ruled.
* **Meta/muse-spark remains DISQUALIFIED** as the S3 vote on the P7G32 output.

---

# §38 owner-w133 round 27 (2026-08-23, opus) — **REGISTRY: §37's (Z1)–(Z6) assembly is MINTED as `G60`, with its enumeration-dependency INSIDE THE STATEMENT** (planner ruling, `cert_w133_r26` §5); and **the INDEPENDENT RE-IMPLEMENTATION of the load-bearing enumerations** (RULING CU), which is the round's main item

Full record: `orchestration/results/w133_state.md` §"Round 27", which is the authority.
Machine records: `problems/wowii/w133_r27_reimpl.py` → `.out` (the re-implementation) and
`problems/wowii/w133_r27_mint.py` → `.out` (the mint gate). Rulings executed: **CU** (the
re-implementation outranks Q41), **CQ** (a re-implementation is a NEW TOOL and inherits none of
the original's controls), **CP/CG** (populations enumerated and asserted complete, never probed
for absence), **BX** (pinned corpus boundary), **BW**, **BM**, **BV**, **BF**, **BB**.

## 38.1 REGISTRY — **`G60` is MINTED for §37**, and the condition is IN THE STATEMENT

The planner's ruling is adopted verbatim in its operative part: §37 is the **assembly**, not a
lemma, and *a number on an assembly is a handle that can be cited without its conditionality
travelling*. So the enumeration-dependency is written **into the statement**, not into a remark,
a footnote or the tier line.

> **`G60` (Theorem — elementary + finite enumeration; the (Z1)–(Z6) assembly).**
> **Modulo the §35–§37 enumerations — two independent implementations agreeing as of r27,
> still single-author and single-specification**, the following holds.
> Let `G` be connected and **C4-free**, let `Z = (z_0,…,z_5)` be an induced C₆ of `G`, and let
> `G` have **no induced P₇** — (D3-C6)'s hypotheses byte-for-byte (§27.4). Write
> `n_3 := #{v ∈ W_1 : a(v) = 3}` and `m := |W_anti|`. Then
> **(i)** `Σ_{v∈V}(a(v) − 3) ≤ n_3 + 2m − 6`;
> **(ii)** `n_3 + 2m ≤ 6`;
> **(iii)** hence `Σ_{v∈V}(a(v) − 3) ≤ 0`, i.e. `Σ_{v∈V} a(v) ≤ 3n` — **which is (D3-C6)**.
> Both extremal regimes are attained: `(n_3,m) = (0,3)` at the `n = 10` region of §36.1
> (`Σ(a−3) = 0`) and `(n_3,m) = (2,0)` at the `n = 10` two-leak region of §37.1
> (`Σ(a−3) = −4`), so (i) and (ii) are **sharp**.
> **THE CONDITIONALITY IS PART OF THE STATEMENT AND TRAVELS WITH THE NUMBER.** A citation of
> `G60` that does not carry *"modulo the §35–§37 enumerations — two independent implementations
> agreeing as of r27, still single-author and single-specification"* in the same breath as the
> number is **MALFORMED**, and a guard should reject it. `G60` may not be
> cited as an unconditional theorem, and it is **not** an S1 candidate while the condition stands.
> *Proof:* §37.1.1, on the chain G54, G55, G57, §34.4a, **G58** (§35), **G59** (§36).

**Why the condition carries a STATE rather than a date, and what would discharge it.** The
qualifier is a statement about what is known and stays true whatever happens later; it is
therefore safe to carry. **This round's re-implementation (§38.2) was a candidate discharge and
was not treated as one here** — whether the qualifier may be amended is the planner's call, not
the owner's, and the owner does not self-promote. **That call was made in `cert_w133_r27` §5 and
the qualifier above is its AMENDED form; the amendment and its gate are recorded at §39.** The
r26 form is superseded and no longer a well-formed citation of `G60`.

**The mint gate, and it cannot miss by ENCODING (RULING CG/CP).** `w133_r27_mint.py` never asks
*"is `G60` absent?"*. It **enumerates the entire address population and asserts contiguity**:
before the append the population is `G0 … G60`, **61 distinct, 0 holes**, and the raw and
NFKC-normalised scans return the **same** population (so no address is invisible to the scanner
by encoding). `G61` is unoccupied. The 2 pre-boundary `G60` occurrences are printed **line by
line** (5005, 5131) and both are prose *about* the free address — **0 registration-shaped**. The
registration classifier is **positive-controlled on `G59`**, whose registration line exists and
where it MUST answer REGISTRATION, so a classifier that could only ever say "prose" is excluded.
Boundary **hard-pinned at draft line 5210** — *not* 5202, which was the draft's length before this round's §36 clarification was entered **above** §38; that correction shifts every later line, exactly as round 24's §27.2 correction did (§36.4 item 4). The boundary is the draft's length **immediately before §38 was appended**, and the number is recorded so it is auditable rather than mysterious. And the gate carries one clause the lemma mints did
not need: it locates the `G60` **statement block** and asserts that **both** condition fragments
lie *inside* it — the ruling's operative content made machine-checkable.

## 38.2 THE INDEPENDENT RE-IMPLEMENTATION (RULING CU / CQ) — written from the SPECIFICATION

`problems/wowii/w133_r27_reimpl.py` re-implements the load-bearing enumerations of §35.1.1,
§36.1.1 and §37.1.1 **from the specification text alone**. The round-23/24/25 scripts were **not
opened while it was written**, and it shares no code with them. Under **RULING CQ** it inherits
**none** of the original's controls, so it carries its own: **PART 0 fires every predicate on an
input where it MUST return `True`** — `has_C4` on `C4`, `K_{2,3}` and `K4`; the induced-path
detector on bare `P₇` (7) and `P₉` (9), where the answer is a long YES, *because a detector whose
output is a negative is silent when broken*; `a(v) = d(v) − t(v)` on Petersen (`≡ 3`), on a
triangle (1) and on `K_{1,4}` (4); the host predicate on Petersen itself, whose induced C₆ is
**searched for and admitted by the decider, not hand-transcribed** (the planner's generalised
RULING BW). The frame/host distinction is asserted to **make a difference** on a concrete input.
Time guard is `tick()` → `os._exit(2)`, **never `return`**.

**Agreement, quantity by quantity.** Every number below is produced by the new tool and compared
against the number §35/§36/§37 report:

| enumeration | spec (§35–§37) | re-implementation | agree |
|---|---|---|---|
| §35.1.1 single-trace anchor, 64 frames | 7 survivors | 7, **and the same 7 traces** | ✓ |
| §35.1.1 consecutive anchor | 3 survivors | 3, same set | ✓ |
| §35.1.1 empty-trace anchor | 4 (empty or antipodal) | 4, same set | ✓ |
| §35.1.1 antipodal anchor | 3 | 3, same set | ✓ |
| §35.1.1/§37 `G[N(v)]`, single anchor | **152 / 17 in-hyp / 135 refuted** | **152 / 17 / 135** | ✓ |
| realised `(d,a)`, single | `(1,1)(2,1)(2,2)(3,2)(3,3)(4,3)` | identical | ✓ |
| `G[N(v)]`, consecutive anchor | 6 / 5 / 1, `(2,1)(3,2)(4,3)` | 6 / 5 / 1, identical | ✓ |
| (Z2) leak shapes with `a = 3` | **exactly 3**, `d ∈ {3,4}` | exactly 3, `d ∈ {3,4}`, same shapes | ✓ |
| (Z2a) leak has a `W_1` neighbour at its own antipode | all | 3 of 3 | ✓ |
| (Z2c) leak has **no** neighbour in `Off(z_i)` | all | 3 of 3 | ✓ |
| §36 (R0) antipodal frames, 3 slots | 3 of 64 at each | 3 of 64 at each | ✓ |
| §36 (R0) `a(u)` unchanged | 6 of 6 `(slot,z)` | 6 of 6 | ✓ |
| §36 (S1) `W_anti` independent | 9 ordered pairs refuted, all by C₄ | 9 / 9, all by C₄ | ✓ |
| §36 (S1) liveness, same pairs non-adjacent | 3 of 3 in hypothesis | 3 of 3 | ✓ |
| §36 (S3) | **256 frames, 5 survive, 251 refuted** | **256 / 5 / 251** | ✓ |
| §36 (S5) adjacent distance-2 pair | **49 frames, 9 survive, 40 refuted** | **49 / 9 / 40**, same survivor set | ✓ |
| §36 (S5) every survivor SHARES an anchor | yes | yes | ✓ |
| §36 (S5) second table | **686 frames, 0 survive** | **686 / 0** | ✓ |
| §37 (Z5) one occupied slot | **32 frames per position**, live | **32 per (position, slot)**, live at all 6 | ✓ |
| §37 (Z5) two occupied slots | 0 survive | 0 survive | ✓ |
| §37 (Z6) feasible `(n_3,m)` | **8 pairs**, `≤ 6` on all, equality only at `(0,3)` | **8**, identical | ✓ |
| `T_Z` contribution of one `W_cons` vertex | **exactly 2, at all 6 edges** | exactly 2, all 6 | ✓ |
| both attainment witnesses | in-hypothesis hosts, `lip` 5 and 6, `Σ = 0` and `−4` | identical | ✓ |

**And the sweep — the one that matters, because it is the whole chain at once.** The
re-implementation enumerates, by its own DFS and its own pruning, every region `Z + k` off-`Z`
vertices. It does **not** assume G54: all **64** traces are enumerated at size 1 and **16** are
found legal, which re-derives G54 rather than importing it.

**Populations agree with §37's sweep A DIGIT FOR DIGIT, size by size, over the whole window.**

| `|off-Z|` | 0 | 1 | 2 | 3 | 4 | 5 | total |
|---|---|---|---|---|---|---|---|
| §37 regions | 1 | 16 | 272 | 4 274 | 59 406 | 738 884 | **802 853** |
| re-impl. regions | 1 | 16 | 272 | 4 274 | 59 406 | 738 884 | **802 853** |
| §37 connected hosts | 1 | 15 | 240 | 3 456 | 42 168 | 435 126 | **481 006** |
| re-impl. hosts | 1 | 15 | 240 | 3 456 | 42 168 | 435 126 | **481 006** |
| §37 max `Σ_v(a−3)` | −6 | −5 | −4 | −3 | **0** | −1 | **+0** |
| re-impl. max `Σ_v(a−3)` | −6 | −5 | −4 | −3 | **0** | −1 | **+0** |
| re-impl. max `n_3` | 0 | 0 | 0 | 1 | **2** | 2 | **2** |

**15 772 944 candidate frames tested, 170.2 s, 123 checks, 0 failures.** These are the *same
numbers*, from a program written independently against the same specification, with its own
search order, its own pruning and its own detectors.

**On that population the new tool checks nine statements at once**, and each is a statement the
chain needs: **(Z1)**, **(Z6)**, **G58** (`a ≤ 3` on `W_1 ∪ W_cons`), **G59(i)**
(`Σ_R(a−3) ≤ 0`), **`T_Z ≥ 2|W_cons|`**, the **G55 summed identity**, **(Z3)**, **(Z4)** and
**(Z5)**. **Violations: 0 of each, over 802 853 regions.**

**Both attainment witnesses were RECOVERED BY THE SEARCH, not handed to it** — the maximiser
printed at size 4 is the `(n_3,m) = (0,3)` region of §36.1 and the `n_3 = 2` maximiser is the
two-leak region of §37.1, each found by the enumeration and admitted by the decider. That is the
planner's generalised RULING BW applied to a *positive control*: the control that matters is the
one the machine produces, not the one the author types.


## 38.3 What the re-implementation does and does not buy — against the round's own interest

**It does not make the chain externally verified, and it does not close a pocket.** Two
implementations by the **same author** against the **same specification text** share the author's
reading of that text. What they cannot share is a *coding* error: a transcription slip, an
inverted mask, a truncating guard. **That is the class of defect this retires, and it is exactly
the class that round 25 caught by hand and round 26 could not check at all** — the r26 judge
refused all four load-bearing quantities and said so.

**What it does not retire:** a wrong *hypothesis* in the specification, a *misread* of the
statement being enumerated, and any error in the hand mathematics that connects the tables. For
those the second family (`Q41`) and a reader who computes are still the instruments, and they are
still owed.

**The honest label** is therefore: *the enumerations are no longer single-implementation; they
are still single-author and single-specification.* Nothing stronger is claimed and nothing is
marked closed here.

---

# §39 owner-w133 round 28 (2026-08-23, opus) — **AMENDMENT: `G60`'s carried qualifier now names the STATE, not a date** (planner ruling, `cert_w133_r27` §5); and the **`Q41` PRE-DISPATCH AUDIT**, which finds the brief that has stood READY since r26 **NOT DISPATCHABLE** — five blockers, one of them a false-void generator that would have destroyed the return (§39.5). **The brief is NOT rebuilt this round; the descope is reported.**

Full record: `orchestration/results/w133_state.md` §"Round 28", which is the authority.
Machine record: `problems/wowii/w133_r28_amend.py` → `.out` (**35 checks, 0 failures**; `.pre.out`
is the pre-append run). Rulings executed: **CV** (no gate addressed by line number), **CO″** (an
adversarial re-implementation is the one duplicate that must NOT be eliminated), **CG/CP**
(populations enumerated and asserted complete, never probed for absence), **CQ**, **BW**, **BM**,
**BV**, **BF**, **BB**.

## 39.1 THE AMENDMENT — what changed in §38.1's statement, and what did not

`cert_w133_r27` §5 ruled the qualifier amendable **and ruled the shape of the amendment**: *a date
bump alone would be a carrier defect of the purest kind — the number would look stronger with no
new evidence behind it.* Round 27 genuinely moved the fact, so the qualifier is amended to carry
the **state** it now has. Superseded form, quoted here as record and **not** as a carrier:

> ~~modulo the §35–§37 enumerations, single-source as of r26~~   ← **SUPERSEDED, r28**

Amended form, now inside the `G60` statement block in both places the old one stood — the opening
qualifier and the malformed-citation clause:

> **modulo the §35–§37 enumerations — two independent implementations agreeing as of r27, still
> single-author and single-specification**

**What did NOT change, deliberately.** The conditionality is still *inside the statement*, not in
a remark or a tier line; the malformed-citation clause is intact and still rejects a citation of
`G60` that does not carry the qualifier in the same breath as the number; `G60` is still **not**
an S1 candidate. **The amendment is strictly a re-description of what is known, and it names its
own residual in the same phrase** — *still single-author and single-specification* is the part
Q41 is built to attack and the part a second implementation by the same author cannot touch.

## 39.2 THE GATE, AND WHY IT IS ADDRESSED BY ANCHOR (RULING CV)

Round 27's mint gate hard-pinned draft line **5210**, and the pin was invalidated the moment a
§36 correction was entered above it — *the gate kept reporting PASS over a subtly wrong
population.* This line's own defect #4. So `w133_r28_amend.py` addresses **nothing** by line
number. The statement block is located by **its own address**: the unique `G60` registration
line, from which the blockquote run is read off. Line numbers are printed for audit and are
load-bearing nowhere.

**And RULING CV is not merely obeyed here, it is DEMONSTRATED.** PART 5 inserts 40 lines above the
statement block — round 27's defect, reproduced on purpose — and asserts two things in the same
run: the anchor-addressed verdict is **unchanged**, and the line-number-addressed gate asking the
same question over the same draft is **destroyed** (18-line block → 0-line block). A rule with a
reproduction in the gate that enforces it does not rot into a slogan.

**The census, not a probe (RULING CG/CP).** The gate never asks *"is the r26 form gone?"* — a
probe for absence answers "yes" whenever it cannot read the token. It **enumerates every
qualifier-shaped occurrence in the whole draft**, prints each with its line number, its form
(`r26-OLD` / `r27-NEW`) and whether it lies inside the statement block, and asserts the census is
exhaustive: **0 `UNCLASSIFIED`**. Absence of the superseded form *inside the block* is then a
consequence of a complete census. The one surviving `r26-OLD` occurrence in the draft is the
struck-through quotation immediately above, outside the block, and it is classified as such.

**The qualifier is allowed to WRAP.** It is 130+ characters and must break across lines; a gate
that only matches it on a single physical line is a gate a future rewrap silently defeats — the
same species as CV, one level down. The block is de-quoted and reflowed to one line before
matching, and *that reflow is itself positive-controlled*: fired on a wrapped probe where it MUST
succeed, and shown failing on the same probe without the reflow.

**Five corruptions, every one shown FIRING in the same run.** (C1) the r26 form reverted into the
block; (C2) **the date bumped with the state dropped** — the exact carrier defect the cert
forbids; (C3) the qualifier true but evicted into surrounding prose; (C4) a duplicate `G60`
registration, so "the" statement block is ambiguous; (C5) the malformed-citation clause deleted
while the qualifier stays. Each fires, and each is additionally asserted to fire **for the right
reason**, because a gate that fails for an unrelated reason is a gate that has not been tested.

## 39.3 WHAT THE AMENDMENT DOES NOT BUY — §27.4's corollary is STILL NOT BANKED

`cert_w133_r27` §3 records that the discharge condition pre-registered at `cert_w133_r26:58` **is
met** and certifies that work permanently — *and* that the corollary still cannot be banked,
because **(D3-C6) is itself unadopted** and that requirement was **missing from the planner's
pre-registration** ((R27/PLANNER-HALFGATE)). The corrected three-part condition (`cert_w133_r27`
§4) is pre-registered blind and is treated here as fixed:

| # | requirement | status after r28 |
|---|---|---|
| 1 | the enumerations have a second, positive-controlled implementation that agrees | ✅ **MET (r27)**, certified permanently |
| 2 | **(D3-C6) is itself adopted** | ❌ **OPEN** — `w133_state.md:4463` |
| 3 | the chain's links carry **two families**, per-statement, or the corollary is banked explicitly conditional on them with the condition in its statement (the `G60` pattern) | ❌ **OPEN** — Q41 is the instrument, deferred to the next free Chrome lease |

**This round advances none of the three.** The amendment is a carrier correction, not evidence.
Stating that plainly is the whole point of a qualifier that carries a state: **the qualifier got
more informative and the ledger did not move.**

## 39.4 THE `G60` PATTERN, NAMED — because part (3) offers it as an alternative

Part (3) of the corrected condition permits banking *"explicitly conditional on them with the
condition in its statement (**the `G60` pattern**)"*. That pattern is now defined by two rounds of
practice and is recorded here so a future round does not have to re-derive it:

1. **the condition lives inside the statement**, in the same breath as the number — never in a
   remark, a footnote or a tier line, because *a number on an assembly is a handle that can be
   cited without its conditionality travelling*;
2. **a malformed citation is defined and declared rejectable** — the statement itself says what an
   ill-formed use of it looks like;
3. **the statement is barred from the top tier while the condition stands** (`G60` is not an S1
   candidate);
4. **the condition names a STATE, not a date** — so it becomes more informative when evidence
   arrives and cannot be strengthened by the passage of time;
5. **a gate, anchor-addressed, asserts (1)–(4) and is shown firing on a corrupted copy.**

Whether §27.4's corollary may take this route instead of waiting on part (2) is **the planner's
call and is not made here.** It is raised because the corrected condition explicitly offers it and
because the owner does not self-promote.

## 39.5 THE `Q41` PRE-DISPATCH AUDIT — **the brief that has been READY since r26 is NOT DISPATCHABLE, and there are five reasons**

Machine record: `problems/wowii/w133_r28_predispatch.py` → `.out` (**48 checks**; the 3 failures
**are** the blockers, and the non-zero exit is the audit working). Q41 was deferred this round by
the planner for a lease reason that had nothing to do with the brief. **The deferral turns out to
have saved the return.**

| # | blocker | how it was found |
|---|---|---|
| **D1** | **`V3` is a FALSE-VOID GENERATOR.** `K4` carries **two** 4-vertex sets with a 4-cycle — `(0,1,2,3)` **and** `(0,3,4,5)` — and the key records one. `V3` is **Tier H**, and a wrong Tier-H value **voids the entire review**. A reviewer who answers `(0,3,4,5)`, *correctly*, is voided. | the key is **re-derived** by this audit's own code, and every answer is checked for **uniqueness** — a row with two correct answers marks a right answer wrong |
| **D2** | **Four rows are DETERMINED** and grade nothing: `V3`, `V4`, `V6`, `V8`. **STRUCK before dispatch, and named.** Kept: `V1`, `V2`, `V5`, `V7`, `V9`. | the row-determination audit: each row's **shortcut is named, COMPUTED, and compared to the truth** |
| **D3** | **The brief is STALE.** Its §36 extract predates r27's (S3) clarification: 7 substantive lines of the current text are absent. | anchored re-cut of the draft, diffed against the brief line by line |
| **D4** | **Status leaks.** The verbatim extracts disclose an adjudicating *"planner"*, the proposed tier and *"NOT an S1 candidate"* — the author's own confidence, handed to the reviewer. | leak census over a named term list |
| **D5** | **The refusal hatch is stated ONCE** in 35 KB. w61 r31's standard is twice, in bold. | occurrence count |

**The shortcuts, named — because a struck row is only credible if its shortcut is stated.**
`V3`: *"the 4-cycle lies inside `Z`, on its first four vertices"* — `Z` is the one distinguished
6-set in the brief and `(0,1,2,3)` is its most guessable 4-subset; the truth **is** that.
`V4`: *"every off-`Z` vertex is in `W_1`, the other three buckets are 0"* — the degenerate census,
reachable from the count of off-`Z` vertices alone; the truth **is** `(5,0,0,0)`.
`V6`: *"the class forbids an induced `P₇`, so the longest induced path is 6"* — the maximum
consistent with the hypothesis the brief spends its length on; the truth **is** 6.
`V8`: *"`n_3 = 0`"* — the modal value, and `G60`'s own bound makes small `n_3` the expected case;
the truth **is** 0. **Every kept row carries an executed assert against its own shortcut**, and
`V5` is the one that shows the audit discriminates: shortcut `a = d = 3`, truth `2`, because
`t(7) = 1`.

**Two owner defects in this audit, reported rather than repaired away.**
1. **My `all_c4` positive control expected 3 and 3; the code returned 3 and 1, and the CODE WAS
   RIGHT.** It returns 4-vertex **sets**, and complete `K₄` has exactly one. Same shape as r27's
   (S3) near-miss and caught the same way — *check the expectation before believing the
   disagreement*. This is the sixth consecutive round in which a hand-written expectation, not the
   machine, was the error.
2. **My first `G1` gate could not have passed on any brief.** It matched each answer's bare string
   anywhere in 35 KB, so it "found" `V1=14`, `V2=3`, `V5=2`, `V6=6` — the digits `14`, `3`, `2`,
   `6`. **A check that cannot pass is exactly as uninformative as one that cannot fail**, doctrine
   V7 in the other direction, and it would have reported a leak that is not there. Re-specified to
   answer-shaped contexts and both shapes shown firing.

**RULING CV, a third instance, found by looking for it.** The r26 brief builder cuts the draft at
three **hard-coded line ranges**. Measured against today's draft: §35's range still coincides with
its anchor, **§36's and §37's no longer do** — r27's in-place §36 correction shifted them, and
`draft(5005, 5093)` now begins on a blank line and truncates §37's tail. **Re-running the r26
builder today would have produced a brief silently missing 8 lines of the link where the chain
closes.** The replacement cuts at **section anchors** (`## 35.1 The statement`, `## 36.1 …`,
`## 37.1 …`), which survive insertion.

# §40 owner-w133 round 29 (2026-08-23, opus) — **REGISTRY: the IMPLICATION `(D3-C6) ⟹ pocket-1's `D = 3` Case-2 residual` is MINTED as `G61`** under the `G60` pattern (planner ruling, `cert_w133_r28` §5). **It is NOT §27.4's corollary; it closes NO pocket; it discharges NO part of the three-part condition, and in particular not part (2).** Plus the `Q41` REBUILD carrying `cert_w133_r28` §6's declared scrub and **RULING CX** (§40.3), and the r26 builder **marked unsafe in the file** (§40.2).

Full record: `orchestration/results/w133_state.md` §"Round 29", which is the authority.
Machine records: `problems/wowii/w133_r29_mint.py` → `.out` (the mint gate; `.pre.out` is the
pre-append run). Rulings executed: **CX** (a held-out answer must be proved UNIQUE, not merely
correct), **CZ** (a positive control must inject the HARDEST form of the species), **CV** (no
gate addressed by a load-bearing line number), **CY** (a check that cannot PASS is as
uninformative as one that cannot fail), **CG/CP**, **CQ**, **BW**, **BM**, **BV**, **BF**, **BB**.

## 40.1 REGISTRY — **`G61` is MINTED for the IMPLICATION**, and the antecedent is IN THE STATEMENT

`cert_w133_r28` §5 ruled the call **PARTLY yes**, and the operative distinction is adopted here
verbatim: banking §27.4's corollary *"conditional on (D3-C6)"* **does not produce the corollary.
It produces a different object — the implication `(D3-C6) ⟹ corollary`** — and it is that object,
under its own name, that is minted below. It is named **as an implication and never by the
corollary's name**, because an address cited by the consequent's name gets read as though the
consequent were established: **the carrier defect this line has now hit four times.**

> **`G61` (Implication — elementary; a conditional TRANSFER, not a closure).**
> **Conditional on (D3-C6), which is NOT ADOPTED** — `w133_state.md:4463`; its own proof rests
> on the r23/r24/r25 own-attack chain carried by `G60` — the following implication holds, and
> holds whether or not (D3-C6) is ever adopted:
> **IF (D3-C6)** — *a connected C4-free graph containing an induced C₆ and having no induced P₇
> satisfies `Σ_v a(v) ≤ 3n`, i.e. `l(G) ≤ 3`* (§27.4, hypotheses byte-for-byte) —
> **THEN** every C4-free graph with `l(G) > 3` carrying a Case-2-forced 3-frame has
> `path(G) ≥ 7`; equivalently, **pocket 1's `D = 3` Case-2 residual closes inside the live
> class.**
> *Proof:* §27.4's two lines, on **`G46`** (§27.2 — unconditional, no a-value hypothesis).
> Suppose `path(G) ≤ 6`. The frame is Case-2-forced, so its usable side-neighbours `x ~ y` and
> `G46` gives an induced C₆; `path(G) ≤ 6` is exactly *"no induced P₇"*; (D3-C6) then gives
> `l ≤ 3`, contradicting `l > 3`. ∎
> **THE ANTECEDENT IS PART OF THE STATEMENT AND TRAVELS WITH THE NUMBER.** A citation of `G61`
> that does not carry *"conditional on (D3-C6), which is not adopted"* in the same breath as the
> number is **MALFORMED**, and a guard should reject it.
> **THREE THINGS `G61` IS NOT.** **(a)** It is **NOT §27.4's corollary** — the corollary asserts
> the consequent outright; `G61` asserts only the implication, and a citation of `G61` as the
> corollary is malformed by the clause above. **(b)** It **closes NO pocket**: pocket 1's `D = 3`
> Case-2 residual remains **OPEN**. **(c)** It **discharges NO part** of the corrected three-part
> condition (`cert_w133_r27` §4) — and **in particular not part (2)**, which is precisely the
> question of whether (D3-C6) is adopted at all.
> **Not an S1 candidate** while the antecedent stands unadopted. **Closes no pocket by itself.**

**Why this is worth an address at all, stated for the record.** It has content that neither of
its endpoints has: it connects a **proved-modulo-a-chain** result to a **named pocket residual**,
so the day (D3-C6) is adopted the transfer is already banked and already gated, and until that
day the ledger reads exactly what is true. It is the `G60` pattern's fifth point in force — a
statement that becomes *more* informative when evidence arrives and cannot be strengthened by the
passage of time.

**Against this round's own interest — `G61` does NOT inherit `G60`'s enumeration qualifier, and
that is a real observation, not a loophole.** `G61`'s proof runs on `G46` alone; `G46` is
unconditional and uses no a-value hypothesis, and no step of the transfer touches §35, §36 or
§37. So the §35–§37 enumerations are **not** a hypothesis of `G61`. The consequence is one the
round would rather not have to say: **`Q41` clearing cleanly will not strengthen `G61` by one
line.** Q41 attacks the chain that proves the *antecedent*; `G61` is a statement about the
*transfer*, and the transfer was never in doubt. What `G61` waits on is part (2) — **adoption**
— and nothing in this round's instruments bears on it.

**The `G60` pattern, point by point, applied here.** (1) the condition lives inside the statement
in the same breath as the number; (2) a malformed citation is defined and declared rejectable;
(3) barred from the top tier while the condition stands; (4) the condition names a **STATE**
(*"NOT ADOPTED"*, with the ledger address that would have to change) rather than a date;
(5) an anchor-addressed gate asserts (1)–(4) and is shown firing on corrupted copies — and under
**RULING CZ** the corruptions are the **hardest** forms of their species, not the easy ones.

## 40.2 THE r26 BRIEF BUILDER IS MARKED UNSAFE **IN THE FILE**, and the mark measures its own defect

`cert_w133_r28` §3 ruled it, and the ruling's reason is the operative part: *the next person to
re-run it will not have read a cert.* So `problems/wowii/w133_r26_build_brief.py` now carries a
banner **and an interlock**: it **refuses to run**, and before aborting it **measures and prints
today's drift** between its three hard-coded ranges and the section anchors they were cut at. A
banner is a slogan; a refusal that prints its own evidence is a gate. An explicit
`--unsafe-i-read-cert-r28-s3` override remains, because reproducing the r26 build against a
pinned old draft is a legitimate thing to want.

**And the measurement CORRECTS the cert in one detail, reported rather than absorbed.**
`cert_w133_r28` §3 says *"§35's still coincides with its anchor; §36's and §37's do not."*
Measured today: **§35's and §36's OPENING lines both still coincide (drift 0); only §37's
opening has moved (+8).** The cert's substance is right and the danger is real, but the
mechanism differs between the two: **§37's cut now BEGINS on a blank line** (8 lines early) *and*
truncates its tail by 8; **§36's cut begins correctly and truncates its TAIL by 8** — r27's (S3)
clarification was entered *inside* §36.1.1, above §36's old closing bound. Both cuts lose 8
lines; only one of them loses them at the front. The replacement cuts at
`## 35.1 The statement` / `## 36.1 The statement` / `## 37.1 The statement` and closes at
`## 35.5` / `## 36.2` / `## 37.2`, each **asserted unique**, and prints the drift beside the old
range so the defect this replaces stays visible.

## 40.3 THE `Q41` REBUILD — five blockers cleared, a sixth found, and the brief is DISPATCHED

Machine records: `problems/wowii/w133_r29_key.py` → `.out` (**45 checks, 0 failures**),
`w133_r29_build_q41.py` → `.out` (**35 checks, 0 failures**), `w133_r29_da_gate.py` →
`.q41.out` / `.r26.out`. Brief: `automath-sandbox/briefs/w133_r29_q41.md` (35 300 chars).
Dispatch row: `automath-sandbox/logs/w133_r29/q41_dispatch.md`.

**D1 — `V3` the false-void generator: DROPPED, for two independent reasons.** The audit's finding
is re-confirmed here (`K4` carries `(0,1,2,3)` **and** `(0,3,4,5)`), and `V3` is *also* determined
by its hardest shortcut. The planner offered repair-or-drop; the repair is moot because the row
was already struck as determined.

**RULING CX is implemented as a per-row property, not a slogan.** Every kept row declares whether
it is **FUNCTIONAL** (the question denotes a value) or **EXISTENTIAL** (it asks for a witness),
and in both cases the whole answer space is enumerated and *exactly one* correct answer asserted.
The fresh row `V10` is deliberately **EXISTENTIAL** — the species that broke `V3` — and its
witness is separately asserted unique.

**RULING CZ finds a SIXTH blocker that r28's own audit passed: `V2` is DETERMINED.** r28's
row-determination audit injected *canonical* shortcuts. Re-run with the **hardest** shortcut per
row — the modal reading a reviewer actually carries — `V2` (*"K1: degree of vertex 7"*, truth
**3**) is answered exactly by *"the modal degree in this class is 3"*. It is struck. This is CZ
working as intended and it is a finding against this line's previous round, not against w61's.

**Rows shipped: `V1`, `V5`, `V7`, `V9` (kept) + `V10`, `V11`, `V12` (fresh, built shortcut-first).
Struck: `V2`, `V3`, `V4`, `V6`, `V8`.**

**RULING DA (planner, mid-round) — the greppability gate, and it returns a RETROACTIVE finding.**
No held-out answer may be recoverable from the surface the brief points the reviewer at. The
reachable surface is enumerated: **this line's briefs name no filesystem path, no repository path
and no URL**, so the surface is the shipped bytes alone — a smaller exposure than 677's, and
measured rather than assumed. Four detectors (bare/equation integer, reformatted or embedded
tuple, sum decomposition, per-component equations), each positive-controlled on a **derived**
planting as DA requires, plus a negative control. **The new brief: 0 hits.**
**The r26 brief, which muse-spark read and graded CLEAN: 1 hit.** Its PART 6 told the reviewer to
validate a counterexample by checking *"longest induced path `<= 6`"* — and `V6` asked for
`K4`'s longest induced path, answer **6**, in a value-shaped context beside the quantity's own
name. `V6` was **greppable and determined**. The fix is redesign, not instruction: the phrase is
gone from the shipped bytes and no row asks the question.

**What this does to r26's CLEAN, stated plainly.** Of r26's nine rows, **five graded nothing**:
`V3` (two correct answers, and determined), `V4`, `V6` (determined *and* greppable), `V8`
(determined), `V2` (determined under the hardest shortcut). **r26's CLEAN rests on four
discriminating rows — `V1`, `V5`, `V7`, `V9` — not nine.** That is a real reduction in what the
first family bought and the ledger should carry it.

**`cert_w133_r28` §6's DECLARED SCRUB, executed and machine-checkable.** **5** internal status
annotations removed — governance vocabulary only: the author's own tier proposal, review-status
labels, and references to who adjudicates them. **Deletions only**, and the guarantee is checked
rather than asserted: for each extract the set of **mathematical tokens** (backticked spans,
relational and summation operators, and every step id `(R0)`, `(S1)`–`(S7)`, `(Z1)`–`(Z6)`,
`(B)`, `(B′)`) is **identical before and after**. The check is shown FIRING on an adversarial
deletion that looks like an annotation and takes one math token with it. One judgement call is
declared rather than hidden: a **self-assigned address** (`G58`) is classified as annotation, not
mathematics, because an address is a handle we mint. The brief's claim is therefore *"verbatim
except 5 declared annotations"* — weaker than "verbatim", and true.

**THE BLIND-GUESS RATE, computed before dispatch.** Per row, two rates are given: `p_formal`
(uniform over the formal answer space) and `p_plaus` (uniform over what a reviewer who does no
work would actually write), with the plausible space defended in one line each. The conjunction
is **cited over the six INDEPENDENT rows only**: **2.2 × 10⁻¹² … 3.6 × 10⁻⁸**. `V7` and `V12` are
the same species on different hosts — one working method answers both — so the seven-row product
(8.8 × 10⁻¹⁵ … 1.8 × 10⁻⁹) **overstates the evidence and is not the number cited.** Verdict rows
are not cited rows.

**FAMILY ACCOUNTING, with the contamination bound priced.** Q41 buys **one** family: Alibaba
(Qwen). Family 1 is Meta/muse-spark, bought at r26 on the byte-frozen brief. **Two families is
the whole purchase.** Qwen has never read §35/§36/§37 and is unprimed on this line's
`a(v)`/trace/`W_anti` vocabulary, so there is no self-review — **but the brief supplies the
author's framing, definitions and case-split vocabulary, so it buys a second reading of the
specification, not a second specification.** Two residuals are added this round and both are
against interest: **(i)** the hosts `K1`, `K2`, `K3` are r26's, so family 1 has seen them —
these rows grade *this* dispatch only and cannot be re-used for a third family; **(ii)** the §36
extract still contains the phrase *"the independent re-implementation finds"*, which signals to
the reviewer that a step has been double-checked. It was **not** removed, because removing it
would remove mathematics, and the scrub is deletions-only. It is named here rather than in the
brief, because naming it in the brief would re-inject it.

**Dispatch, settled from the SERVER STORE and not from a browser surface (OPS-13/OPS-8).**
Conversation `d977bb6f-91cb-486f-bfea-855e6a448d5d`; `nUser = 1`, `userLen = 35 300` codepoints,
`roles = [user, assistant]`, `model = qwen3.8-max`. OPS-6 at its strongest form: the in-page
SHA-256 of the composer equals `shasum -a 256` on disk, so the paste is **byte-identical**, not
merely the right length. **The harvest is the next round's**, under OPS-14 — content stability
plus schema completeness plus a terminal sentence, and `document.visibilityState` checked before
any UI-chrome signal is believed.

---

# §41 owner-w133 round 31 (2026-08-23, opus) — **`(A2-PATH)` IS REFUTED**, with an explicit counterexample that survives `rad ≥ 5`; plus the (Z3)/(Z4)/(Z5) frame populations audited by a second implementation and one of them CORRECTED (§37.1.1's erratum). **UNREGISTERED, carrying its own witness; no number minted — `G62` is left free.**

## 41.1 The statement refuted

Round 30 split route **A2** and left one half open, calling it *"the whole new idea"*:

> **`(A2-PATH)`** `path(G) ≥ path(G′) + h`, where `G′` is the result of peeling every `a = 1`
> vertex (F7), `h` is the maximum distance in `G` from a peeled vertex to `V(G′)`, and
> `path(·)` counts VERTICES on a longest induced path.

**It is false.**

> **WITNESS.** Let `G′` be **two `C₉`s sharing one vertex** and let `G := G′ + one pendant`
> hung at a vertex `w` of one arm. Then `n(G) = 18`, `G` is connected and **C4-free**, its
> **only** `a = 1` vertex is the pendant, peeling returns `G′` exactly, **`rad(G) = 5`**,
> `h = 1`, and **`path(G′) = path(G) = 15`.** So `path(G) = 15 < 16 = path(G′) + h`. ∎
>
> Smaller and more readable, same phenomenon: `G′ =` two `C₅`s sharing a vertex (the bowtie of
> pentagons), pendant at the shared vertex: `path(G′) = path(G) = 7`, `h = 1`.

## 41.2 The mechanism, and it is an EQUALITY

A pendant `v` at `w` is a leaf, so no induced path of `G` can have `v` in its interior. Hence
every induced path of `G` either avoids `v` or **ends** at `v`, and

> **`path(G) = max( path(G′), 1 + endpath(G′, w) )`**,

where `endpath(G′, w)` is the largest number of vertices on an induced path of `G′` having `w`
as an **endpoint**. Therefore **`(A2-PATH)` at `h = 1` is equivalent to `endpath(G′,w) =
path(G′)`** — to `w` being an endpoint of *some* longest induced path of `G′`. Nothing in the
hypotheses forces that, and in the witness `endpath(G′,w) = 4` against `path(G′) = 7`.

> **`h` measures DISTANCE; `path` is paid only at an ENDPOINT.** A2's exchange is not between
> two lengths — it is between a length and an **anchored** length.

*Control, hardest form:* the **same** pendant on the **same** base, hung instead at a vertex
that **is** such an endpoint, gives `path(G) = path(G′) + 1` **with equality**. The failure is
about **where** the hair hangs, not about hairs.

## 41.3 How far the refutation reaches — and the one hypothesis left standing

Measured over 179 witnesses (`problems/wowii/w133_r31_a2path.py` → `.out`, 35 checks, 0
failures), a counterexample can carry **connected**, **C4-free**, **an `a = 1` vertex present**,
and **`rad(G) ≥ 5`** (largest reached: `rad = 7`) **all at once**. The single Problem-A
hypothesis no witness here carries is **`l(G) > 4`** — the best reached is `l = 2.29`.

> **Consequently any proof of `(A2-PATH)` must consume `l > 4`**, since every other hypothesis
> on Problem A's list is already satisfied by a counterexample. **And `l > 4` is a DENSITY
> hypothesis while the failure is POSITIONAL.** That mismatch is the content of this entry.

`l` is pinned by a control rather than by assumption: `l(G) :=` the mean `a`-value (read off
F7's own `Σa − 4n` bookkeeping), verified to equal **exactly `4.0`** on the **PG(2,3)**
incidence graph — the brief's own published datum — with PG(2,3) built from the perfect
difference set `{0,1,3,9} mod 13`.

## 41.4 The successor target, proposed and NOT claimed

Route A2 never needed `(A2-PATH)`. It needs `path(G) ≥ rad(G) + 4`, and round 30 already proved
`rad(G) ≤ rad(G′) + h`. So it suffices to prove

> **`(A2-ANCHOR)`** `path(G) ≥ rad(G′) + 4 + h`,

and since `path(G) ≥ h + endpath(G′, w)` for a hair reaching `G′` at `w`, that follows from an
**anchored F11**:

> **`(F11-AT-w)`** `endpath(G′, w) ≥ rad(G′) + 4` at the attachment `w` of a **deepest** hair.

F11 delivers that number at **some** endpoint of `G′`; `(F11-AT-w)` asks for it at a
**prescribed** one. It is strictly weaker than `(A2-PATH)`, and it is where `l > 4` would have
to enter. **Nothing here proves or refutes it.** The witness fails `(F11-AT-w)` too, but it
also fails F11's own hypotheses, so that is a consistency observation and **not** evidence.

**NOT CLAIMED.** Route A2 is not refuted — only this formulation of its open half is. Problem A
is untouched, no counterexample inside Problem A's full class is exhibited, **and no pocket is
closed.**

# §42 owner-w133 round 32 (2026-08-23, opus) — **THE ANCHORED TAIL: `(TAIL-1)` IS UNCONDITIONAL, `(RAD-1P)` IS AN EQUIVALENCE, AND THE SINGLE-HAIR CASE OF ROUTE A2 REDUCES TO ONE CONFIGURATION.** Plus a defect in §41's own successor target: **`(F11-AT-w)` AS PROPOSED IS AN OVERSHOOT.** UNREGISTERED, carrying its proofs; no number minted — `G62` is left free.

Machine record: `problems/wowii/w133_r32_anchor.py` → `.out`, **exit 0, 49 684 checks, 0
failures, all 7 declared parts asserted to have run.** No SAT; explicit graphs, exact BFS, and
bounded DFS for longest induced path on hosts with `n ≤ 18` only.

## 42.1 A DEFECT IN §41.4's OWN PROPOSAL — the quantifier

§41.4 proposed `(F11-AT-w)`: `endpath(G′,w) ≥ rad(G′)+4` **at the attachment `w` of a deepest
hair**. That clause carries **no positional information at all**:

> A hair may be hung at **any** vertex of `G′`, and **a single hair is trivially the deepest
> one.** So over the class the target is meant to serve, `w` ranges over **every** vertex, and
> `(F11-AT-w)` is the **universal** statement
> **`(F11-ALL)`: `endpath(G′,w) ≥ rad(G′)+4` for EVERY vertex `w` of `G′`.**

F11 (= G42) is the **existential** statement — *some* induced path has `rad+4` vertices. So the
successor target proposed in §41.4 is **strictly STRONGER than F11**, not a mild anchoring of
it. §41.4 described it as "strictly weaker" — true against `(A2-PATH)`, which is what that
sentence compared it to, but the comparison a reader will actually make is against F11, and
against F11 it is an **overshoot**. **The r31 entry named a target harder than the problem.**

*Machine, exact rather than asymptotic:* hanging one pendant at `w` moves `Σa` by **exactly +2**
and `n` by `+1`, so `l(G) > 4 ⟺ Σ_{G′}(a−4) > 2` — a marginally stronger threshold than
`l(G′) > 4`, verified on PG(2,3) (`Σ(a−4) = 0`, `l = 4.0` **exactly**, the pinned control) and
its one-pendant extension (`Σ(a−4) = −2`). C4-freeness and `peel(G′+pendant) = G′` verified at
every tested attachment; `rad` never drops.

## 42.2 **(TAIL-1) — UNCONDITIONAL, and it is the round's one clean theorem**

> **(TAIL-1).** Let `G` be C4-free with `μ(G) ≥ 2` (no `a = 1` vertex). Then for **every**
> vertex `w`, **`endpath(G,w) ≥ ecc(w) + 2`** — and hence `endpath(G,w) ≥ rad(G) + 2`.

**Proof.** Let `w = u₀ … u_d` be a geodesic to a vertex at distance `d = ecc(w)`. `G` is
C4-free, so `G[N(u_d)]` is a **matching** and `a(u_d) = d(u_d) − t(u_d) ≥ 2` gives a component
other than `u_{d−1}`'s; take `y` in it. Then `y ≁ u_{d−1}` by choice; `y ≁ u_i` for `i ≤ d−3`
because `d(u_i,u_d) ≥ 3`; and `y ≁ u_{d−2}`, since otherwise `u_{d−2}` and `u_d` would have the
**two** common neighbours `u_{d−1}` and `y` — a C4. So `u₀ … u_d y` is an induced path on
`d + 2` vertices with `w` as an **endpoint**. ∎

**No `l > 4`, no `rad ≥ 5`, no F11.** Certified by **building** the path — not by asserting the
conclusion — at **all 186** (graph, vertex) pairs over nine hosts including PG(2,3) and the
`2×PG(2,q)+path` chains; every one is verified induced and verified to have exactly `ecc(w)+2`
vertices. **TIGHT**, in hardest form: on `C₆`, `endpath(w) = ecc(w)+2 = 5` exactly at every
vertex, so `(TAIL-1)` cannot be improved to `+3` without a further hypothesis. **LIVENESS,
correctly aimed:** on `C₉ +` pendant (`μ = 1`) the construction **declines** at exactly the
vertices whose furthest vertex is the `a = 1` pendant (2/2). *The first version of that probe
was aimed at the pendant itself, where the construction succeeds and therefore tests nothing;
it is kept in the file as a named negative.*

## 42.3 The two further extensions, and what each COSTS

> **(TAIL-2).** If some `y ∈ N(u_d)` off `u_{d−1}`'s component has **`a(y) ≥ 4`**, then
> `endpath(G,w) ≥ ecc(w) + 3`.
> **(TAIL-3).** A third extension needs **`a(z) ≥ 6`**.

**Where the numbers come from, and they are counted, not guessed.** Extending `u₀…u_d y` by
`z ∈ N(y)`: `z ≁ u_d` and `z ≁ u_{d−1}` are **forced** by C4-freeness (`z–y–u_d–u_{d−1}` would
be a 4-cycle), and `z ≁ u_i` for `i ≤ d−4` by distance. What must be **paid for** is exactly
`u_{d−2}` and `u_{d−3}`: at most **one** vertex of `N(y)` is adjacent to each (two would give
`y` and that `u_j` two common neighbours), so at most two matching components are spoiled, plus
`u_d`'s — hence `a(y) ≥ 4`. At the third step the dodge list is
`{u_{d−1}, u_{d−2}, u_{d−3}, u_{d−4}}`, four vertices at one component each, plus `y`'s — hence
`a(z) ≥ 6`. The C4-forced exclusions were verified on **157** frames.

> **`l > 4` IS A MEAN. It does not supply `a(y) ≥ 4`, let alone `a(z) ≥ 6`, AT A PRESCRIBED
> VERTEX.** This is r31's DENSITY-vs-POSITIONAL mismatch, now **located at a named vertex and
> carrying a number.**

**Against this round's own interest:** `(TAIL-2)`'s construction **succeeded at 100 % of
vertices on every host tested**, including hosts where `a(y) ≥ 4` holds at **none** of them. So
`a(y) ≥ 4` is **sufficient and far from necessary**, and the honest reading is that the round
has an easy sufficient condition, not a characterisation.

### 42.3a **CORRECTED COST — owed since round 33, discharged in round 37**
*(OWNER-CLAIMED, PROVISIONAL, NOT ADJUDICATED. Machine record:
`problems/wowii/w133_r37_f11all.py` → `.out`, exit 0, **16 301 checks, 0 failures**,
system `python3` 3.9.6.)*

**The two blanket constants above are the worst case ASSUMED, not counted.** Both are
superseded by counted forms; §42.3 stays true as written, and is no longer the sharp
statement of either cost.

* **`(TAIL-2′)` (§43.1) replaces `a(y) ≥ 4`:**
  `a(y) ≥ 2 + #{ j ∈ {d−2,d−3} : N(y) ∩ N(u_j) ≠ ∅ }`.
* **`(TAIL-3′)` (§45.1, new) replaces `a(z) ≥ 6`:**
  `a(z) ≥ 2 + #{ j ∈ {d−1,d−2,d−3,d−4} : N(z) ∩ N(u_j) ≠ ∅ }`.

**How much the sharpening is worth, counted rather than asserted.** Over **77 724** frames
on **417** hosts of round 33's family: `(TAIL-2′)` fires on **68 885** and the blanket
`a(y) ≥ 4` on **42 119** — the sharp form wins **26 766** frames the blanket loses.
`(TAIL-3′)` fires on **52 807** and the blanket `a(z) ≥ 6` on **8 821** — the sharp form
wins **43 986**. **At the third step the blanket is wrong about the cost roughly five times
out of six.** Every firing was certified **by BUILDING** the `ecc(w)+3` resp. `ecc(w)+4`
induced path and re-verifying it with a checker independent of the search: **68 885 of
68 885** and **52 807 of 52 807**, zero misfires.

---

## 42.4 **(RAD-1P) — the radius dichotomy for one pendant, and it is an EQUIVALENCE**

> **(RAD-1P).** Let `G = G′ +` one pendant at `w`, `r := rad(G′)`. For `c ∈ V(G′)`,
> `ecc_G(c) = max(ecc_{G′}(c), d(c,w)+1)`, and `ecc_G(pendant) = ecc_{G′}(w)+1`. Hence
> **`rad(G) ∈ {r, r+1}`**, and
> **`rad(G) = r+1` ⟺ EVERY centre `c` of `G′` has `d(c,w) = r`.**

Machine-verified as an equivalence on **every** `h = 1` instance of the sweep; the non-trivial
side **fired on 34** of them, so it is not vacuous. **It reproduces, and explains, the planner's
own r31 table**: on two `C₉`s glued at a vertex the unique centre is the glue vertex with
`r = 4`, and the four attachments giving `rad(G) = 5` are exactly the four at distance `4` from
it. *This condition is not in §41; the machine produced an empty residual class and that is how
it was found.*

## 42.5 **THE THEOREM — route A2's conclusion for the SINGLE-HAIR case**

Setting: `G` connected C4-free, `G′ = peel(G)` connected with `μ(G′) ≥ 2`, and the peeled set is
a **single hair** of `h ≥ 1` vertices at `w ∈ V(G′)`. Write `r := rad(G′)`, `e := ecc_{G′}(w)`.
*(This is exactly the class in which §41 killed `(A2-PATH)`: that witness was `G′ +` ONE
pendant.)* Two bounds:

* **(B1)** `G′` is induced in `G`, so `path(G) ≥ path(G′)`; with **F11 on `G′`** this is
  `path(G) ≥ r + 4`. **This import is route A2's own, inherited here and not newly justified.**
* **(B2)** the hair prepends `h` vertices to any induced path of `G′` ending at `w`, so
  `path(G) ≥ h + endpath(G′,w) ≥ h + e + 2` by **(TAIL-1)** — **unconditional.**

With one hair, `ecc_G(w) = max(e,h)`, so `rad(G) ≤ max(e,h)`; also `rad(G) ≤ r + h` (r30).

| case | bound used | status |
|---|---|---|
| **`h ≥ 2`** | **(B2) alone** | **CLOSED, UNCONDITIONALLY** — no `l > 4`, no `rad ≥ 5`, no F11 |
| `h = 1`, `e = r` | (B1) | CLOSED **via F11 on `G′`** |
| `h = 1`, `e ≥ r+2` | (B2) | CLOSED |
| `h = 1`, `e = r+1`, `rad(G) = r` | (B1) | CLOSED **via F11 on `G′`** |
| **`h = 1`, `e = r+1`, `rad(G) = r+1`** | — | **RESIDUAL: short by EXACTLY one vertex** |

**Tally: 7 404 (base, `w`, `h`) instances over 145 bases, every one machine-checked — 4 936 /
908 / 723 / 835 / 2.**

> **AND THE RESIDUAL NEEDS ONLY `(TAIL-2)`, NOT `(F11-ALL)`.** In it the requirement is
> `endpath(G′,w) ≥ ecc_{G′}(w) + 3` at **that one `w`** — i.e. **the anchored cap-break**, a
> 4-rich second neighbour at the far end of a geodesic **from `w`**. `(F11-AT-w)`'s
> `rad(G′)+4`-at-every-`w` is **more than route A2's single-hair case ever needed.**

**THE `h = 1` BRANCH IS EXACTLY AS STRONG AS F11'S APPLICABILITY TO `G′`, and that is shown,
not asserted.** Computing `path(G)` **exactly** (longest induced path, no cap) on every host
with `n ≤ 15`: the `h ≥ 2` branch holds **244/244** with zero violations, while the `h = 1`
branch **FAILS on 5** of the sparse hosts — `C₅ +` pendant has `path = 5 < 6 = rad+4`, and so do
`C₆` and `Θ(3,3,3)`. Those hosts carry `l = 2.00–2.25` and are outside F11's hypotheses, so no
counterexample to anything is claimed. **What they show is that (B1) is not bookkeeping in that
branch: delete F11 and the `h = 1` branch is FALSE.** *This control was not designed — it
appeared when a check of mine ran on a sample outside its own hypothesis (§42.7).*

## 42.6 The residual is NON-EMPTY, and it is a gap in the ARGUMENT, not a counterexample

Conjunct populations over 145 bases, printed before the verdict: `e = r+1` at **837** vertices,
"`w` maximally far from every centre" at **34**, **both at 2**. Both instances come from the
**seeded random hosts**, not from the structured families:

| base | `n` | `w` | `e` | `r` | `l(G′)` | (TAIL-2)? | `endpath(w)` vs `r+4` |
|---|---|---|---|---|---|---|---|
| `rand(s=7,n0=18)` | 18 | 11 | 5 | 4 | **2.333** | **YES** | **12** vs 8 |
| `rand(s=30,n0=22)` | 22 | 13 | 5 | 4 | **2.455** | no | **17** vs 8 |

**My first, narrower family produced ZERO residual instances and I was one sentence from
recording the single-hair case as closed outright.** The width of the family is load-bearing.
And **read the last column**: `endpath(w)` is already far past `r+4` on both. **The residual is
a gap in the argument; the bound is short by one vertex, the graphs are not.**
**Both carry `l(G′) ≤ 4`** — the `l > 4` hypothesis is **unspent** on every residual instance
found, exactly as §41 measured over its 179 witnesses.

## 42.7 What is PROVED, what is PROPOSED, and what is ASSUMED

**PROVED (unconditional, machine-certified by construction):** `(TAIL-1)`; `(TAIL-2)` and
`(TAIL-3)` with their exact `a`-value costs; `(RAD-1P)` as an equivalence; and the `h ≥ 2`
branch of §42.5, which needs **none** of `l > 4`, `rad ≥ 5`, F11 or `(F11-AT-w)`.
**ASSUMED, and named:** F11 applies to `G′` — i.e. `l(G′) > 4` and `rad(G′) ≥ 5` survive
peeling. Route A2 has always made this import; **this entry inherits it and does not
strengthen it.** `rad(G′) ≥ 5` in particular is **not** automatic, since peeling can lower the
radius — the very phenomenon route A2 exists to handle.
**PROPOSED, NOT CLAIMED:** `(TAIL-2) at a prescribed `w`` as the successor target in place of
`(F11-AT-w)`. **`G62` stays free. No pocket is closed. Problem A is untouched, and the
multi-hair case is NOT covered.**

---

# 43. Round 33 — `(TAIL-2′)`, and the measurement that makes §42.5's residual target untestable

*(Owner-claimed, machine-certified; `problems/wowii/w133_r33_tail2at.py` → `.out`, 9 492
checks, 0 failures, all 5 declared parts asserted to have run. §42's results are themselves
still awaiting planner certification and are used here as owner-claimed, not banked.)*

## 43.1 `(TAIL-2′)` — the dodge list COUNTED at the frame instead of bounded at 2

> **`(TAIL-2′)`.** In `(TAIL-1)`'s frame (`w = u₀ … u_d` a geodesic, `d = ecc(w)`, `y ∈ N(u_d)`
> off `u_{d−1}`'s component), `endpath(G,w) ≥ ecc(w) + 3` as soon as
> **`a(y) ≥ 2 + #{ j ∈ {d−2, d−3} : N(y) ∩ N(u_j) ≠ ∅ }`.**

**Proof.** The extending `z ∈ N(y)` must avoid: (i) the component of `G[N(y)]` containing
`u_d` — that is where `y`'s matching partner in `N(u_d)` lies; (ii) for each `j ∈ {d−2, d−3}`
that actually has a neighbour in `N(y)`, that one component — **at most one component each,
since two neighbours of `y` adjacent to the same `u_j` would give `y` and `u_j` two common
neighbours, a C4**. All other exclusions are free: `z ≁ u_{d−1}` is **forced** by C4-freeness
(`z–y–u_d–u_{d−1}` would be a 4-cycle), and `z ≁ u_i`, `z ≠ u_i` for `i ≤ d−4` hold by
distance. One surviving component supplies `z`. ∎

**§42.3's `a(y) ≥ 4` is exactly this bound with both indicators set to 1 — the worst case
assumed rather than counted.** §42.3 stands as written (it is true); `(TAIL-2′)` supersedes it
as the sharp form. Measured over the **414** residual instances of §43.2: the sharpened
requirement is **strictly below 4 on 194** of them, and where §42.3's blanket condition fails
it still **fires on 44 of 63**. Every YES was certified **by building** the induced path on
`ecc(w)+3` vertices, and **every frame at which the condition held was put on trial** — a
missing `z` would have raised a failure; none did.

## 43.2 The measurement — the residual configuration has never been seen with `l > 4`

Census over **420** hosts, each certified connected, C4-free and `μ ≥ 2` before counting:
PG(2,3)/PG(2,5) incidence graphs, those cores with a `C_k` glued (`k = 5…25`), core + pendant
path + terminal cycle, two-cycle-on-one-core shapes, blob chains `2×PG(2,q)+P_L`, and **225
hosts of the seeded C4-free process** on `n₀ = 14…50`. Conjunct populations printed before the
verdict: `ecc(w) = r+1` at **3 256** vertices, `w` maximally far from every centre at **1 447**,
**both at 414**.

> **Residual instances: 414. With `l > 4`: 0** — although **86** hosts of the family carry
> `l > 4` and **25** carry `l > 4` with `rad ≥ 5`. **The family is designed plus seeded-random,
> NOT exhaustive; the `0` is a statement about it and not a theorem.**

Every residual instance found sits at `l ≤ 3.66` and `rad = 2`; every `l > 4` host reached is
self-centred or nearly so, and self-centredness makes `ecc(w) = r+1` **impossible by
definition**. **Consequence for §42.5's named successor target:** `(TAIL-2)`-at-a-prescribed-`w`
is **FALSE without `l > 4`** — 63 of the 414 instances are explicit counterexamples, each
carrying the full residual configuration and best `a(y) ∈ {2,3}` over *every* frame — and it is
**neither proved nor refuted with `l > 4`, because no instance satisfies that hypothesis.**
**The open question is therefore whether the residual configuration can carry `l > 4` at all;
a NO closes route A2's single-hair case outright.**

**Against this round's own interest:** on all four certified witnesses — including one where
the TAIL route cannot reach `+3` at all — the underlying requirement `endpath(G,w) ≥ ecc(w)+3`
**HOLDS**; only **3 of 414** instances resist the TAIL route entirely. **What §43.2 refutes is
an instrument, not a statement.** Controls: r31's `C₉+C₉` table reproduced (`rad = 4`, unique
centre, four maximally-far vertices); §42.6's two residual instances rebuilt from their seeds
and matched to the printed digit; three self-centred negative controls at `0`; a liveness
control in which the predicate declines.

---

# 44. Round 35 — the MULTI-HAIR class, and the CENTRE-SPHERE bound

*(**OWNER-CLAIMED, PROVISIONAL, NOT ADJUDICATED** — banked under `PROTOCOL.md` v4 §3, which
batches planner adjudication at milestones. Nothing here may be cited outward.
Machine record: `problems/wowii/w133_r35_multihair.py` → `.out`, exit 0, **4 220 checks, 0
failures**, all 6 declared parts self-registered, system `python3` 3.9.6. §42/§43 are
themselves still owner-claimed and are used here as such.)*

## 44.0 Setting

`G` connected C4-free; `V(G) = V(G′) ⊎ (hairs)`, the hairs being `k ≥ 1` induced paths
`x_i^1 … x_i^{h_i}` with `x_i^1 ~ w_i ∈ V(G′)`, the roots `w_i` **distinct**, and no other
edges; `G′` connected with `n′ ≥ 2`. `H := Σ_i h_i`, `l′ := l(G′)`, `r′ := rad(G′)`.
**§42 is the case `k = 1`; this section is the general one.**

## 44.1 Eccentricities — exact, and the radius escapes the core

> **(MH-ECC-1)** for `c ∈ V(G′)`: `ecc_G(c) = max( ecc_{G′}(c), max_i (d_{G′}(c,w_i)+h_i) )`.
> **(MH-ECC-2)** for `u = x_i^j`: `ecc_G(u) = max( h_i−j, j+ecc_{G′}(w_i),
> max_{m≠i}( j + d_{G′}(w_i,w_m) + h_m ) )`.

Both follow from the two facts that `G′` is isometric in `G` and that every path into hair `i`
enters through `w_i`. Certified by BFS at **2 436** core and **780** hair (graph, vertex) pairs
over **252** hair configurations on six bases (`k ≤ 3`, `h_i ≤ 3`; designed families, not
exhaustive).

> **(MH-RAD-0).** `rad(G)` **need not be attained on `V(G′)`.** `G′ = K₂`, hairs of length
> `100` at `w₁` and `1` at `w₂`: `ecc(w₁) = 100`, `ecc(w₂) = 101`, **`rad(G) = 51`**, and the
> centre is a single vertex **strictly inside the long hair**.

## 44.2 The `l`-bookkeeping for hairs

> **(MH-A)** `a_G(x_i^t) = 2` for `1 ≤ t ≤ h_i−1`, `a_G(x_i^{h_i}) = 1` (the two hair
> neighbours of an interior hair vertex are non-adjacent); `a_G(c) = a_{G′}(c) + m_c` for
> `c ∈ V(G′)`, `m_c = #{i : w_i = c} ∈ {0,1}`.
> **(MH-L)** hence `Σ_v a_G(v) = n′l′ + k + (2H − k) = n′l′ + 2H` and
> **`l(G) = ( n′·l′ + 2H ) / ( n′ + H )`** — verified against a direct α-count on 252 of 252.

> **(MH-C).** **`⌊l(G)⌋ ≤ ⌊l(G′)⌋`, unconditionally.**
> *Proof.* If `l′ ≥ 2`: `l(G) ≤ l′ ⟺ n′l′+2H ≤ l′(n′+H) ⟺ 2H ≤ l′H ⟺ l′ ≥ 2`. If `l′ < 2`:
> `l(G) ≥ 2` would give `n′l′+2H ≥ 2n′+2H`, i.e. `l′ ≥ 2`, a contradiction; so `l(G) < 2` and
> `⌊l(G)⌋ ≤ 1 = ⌊l′⌋`, using `l′ ≥ 1` for connected `n′ ≥ 2`. ∎

**The hairs can never push the `l`-term of the target above the core's** — for any `k`,
including `k = 1`.

## 44.3 **(MH-I) — the multi-hair case with an unchanged radius**

> **(MH-I).** If **`rad(G) = rad(G′)`** then the conjecture for `G′` implies it for `G`.
> *Proof.* `G′` is induced in `G`, so `path(G) ≥ path(G′)`; with (MH-C),
> `path(G) ≥ path(G′) ≥ rad(G′)+⌊l(G′)⌋ ≥ rad(G)+⌊l(G)⌋`. ∎

No `l > 4`, no `rad ≥ 5`, no F11, no bound on `k` or `h_i`. Census (`k ≥ 2`, 112 instances,
16-vertex cap for the exact induced path): `path(G) ≥ path(G′)` on **112/112**; Case I
**88/88**; Case II (`rad(G) > rad(G′)`) **24** instances all satisfying the conjecture — **a
measurement, not a proof. Case II is the open half of the multi-hair front.**

## 44.4 **The CENTRE-SPHERE bound** — §42.4's `(RAD-1P)` condition, bounded

Call `w` **maximally far from every centre** if `d(c,w) = rad(G)` for every `c ∈ centre(G)`
(the right-hand side of `(RAD-1P)`). Write `r := rad(G)`, `C := centre(G)`,
`B_j(w) := {u : d(u,w) ≤ j}`.

> **(CS-1).** If such a `w` exists and `r ≥ 1`, then `C ∩ B_{r−1}(w) = ∅`, so
> **`|C| ≤ n − |B_{r−1}(w)|`**. *Proof.* `u ∈ C ⟹ d(u,w) = r > r−1`. ∎
>
> **(CS-2).** `G` C4-free, minimum degree `δ ≥ 2`. Then `|B_2(w)| ≥ 1 + deg(w)(δ−1) ≥ 1+δ(δ−1)`.
> *Proof.* Each `z ∈ S_2(w)` has exactly one neighbour in `N(w)` (two would give `w,z` two
> common neighbours — a C4), so the sets `N(u) ∩ S_2(w)`, `u ∈ N(w)`, partition `S_2(w)`; and
> `|N(u) ∩ N(w)| ≤ 1` (else `u,w` have two common neighbours), so
> `|N(u) ∩ S_2(w)| ≥ deg(u)−2 ≥ δ−2`. Sum. ∎
>
> **(CS-3).** `G` connected C4-free, `δ ≥ 2`, `r ≥ 3`. If such a `w` exists then
> **`|C| ≤ n − 1 − δ(δ−1) − (r−3)`**; contrapositively, `|C|` above that bound forbids any such
> vertex. *Proof.* `B_{r−1}(w) ⊇ B_2(w)` and distances `3,…,r−1` are each realised since
> `ecc(w) ≥ r`. ∎

**This settles §43.2's structural question for the dense regime by proof rather than census.**
Over the 248 hosts of round 34 (`PG(2,5)` minus one edge, 186; minus one vertex, 62 — all
`r = 3`, all non-self-centred, all with `l > 4`): representative `n = 62`, `δ = 5`, `|C| = 50`
against a bound of **41**; **(CS-3) decides 248 of 248 and forbids the configuration in every
one**, matching BFS on 248 of 248, with **0** undecided and **0** out of scope. Controls: the
predicate is live on **6** independent (host, `w`) pairs, where (CS-1) holds 6/6; (CS-2)
verified at 70/70 vertices.

**Against this section's own interest.** (CS-3) is a **minimum-degree** lemma, and §0's
standing obstacle — **Hoffman–Singleton with one subdivided edge (`δ = 2`, `rad = 3`,
`⌊l⌋ = 6`)** — applies to it in full: at `δ = 2` the bound degenerates to `|C| > n−3`. `l > 4`
is a mean and does not force `δ` large. **Route A2 does not close here; the incompatibility of
§43.2 is neither proved nor refuted; `G62` stays free.**

---

# 45. Round 37 — **(F11-ALL) STRATIFIES, AND IT HAS AN UNCONDITIONAL SUFFICIENT CONDITION**

*(**OWNER-CLAIMED, PROVISIONAL, NOT ADJUDICATED** — banked under `PROTOCOL.md` v4 §3.
Nothing here may be cited outward. Machine record: `problems/wowii/w133_r37_f11all.py`
→ `.out`, exit 0, **16 301 checks, 0 failures**, elapsed 3.1 s, all 6 declared parts
self-registered, **system `python3` 3.9.6** (pure stdlib). §42/§43/§44 are themselves
owner-claimed and are used here as such.)*

Target, from §42.1: **`(F11-ALL)`: `endpath(G,w) ≥ rad(G) + 4` for EVERY vertex `w`.**
After `(MH-GAP)` (§44 successor, r36) this is the **whole** remaining front — single-hair
and multi-hair alike.

## 45.1 **`(TAIL-3′)` — the third-step dodge list COUNTED at the frame**

> **`(TAIL-3′)`.** In `(TAIL-1)`'s frame, with `y` as in `(TAIL-2′)` and `z ∈ N(y)` the
> vertex it supplies, `endpath(G,w) ≥ ecc(w) + 4` as soon as
> **`a(z) ≥ 2 + #{ j ∈ {d−1, d−2, d−3, d−4} : N(z) ∩ N(u_j) ≠ ∅ }`.**

**Proof.** Extend by `t ∈ N(z)`. `t` must avoid: (i) the component of `G[N(z)]` containing
`y` — one component; (ii) for each `j ∈ {d−1,…,d−4}` that actually has a neighbour in
`N(z)`, that one component, since two neighbours of `z` adjacent to the same `u_j` would give
`z` and `u_j` two common neighbours, a C4 (using `z ≁ u_j`, which `(TAIL-2′)`'s step already
established). Everything else is **free**: `t ≁ u_d` is **forced** — `t ~ u_d` would make
`t` and `y` two common neighbours of `z` and `u_d`, a C4, given `t ≁ y` and `z ≁ u_d`; and
`t ≁ u_i`, `t ≠ u_i` for `i ≤ d−5` hold by distance, since `d(u_i,u_d) ≥ 5` and
`d(z,u_d) = 2` force `d(u_i,z) ≥ 3`. One surviving component supplies `t`. ∎

§42.3's blanket `a(z) ≥ 6` is this bound with **all four** indicators set to 1.
The free exclusions were asserted frame by frame: **F1** (`z ≁ u_{d−1}` forced) and **F2**
(`z ≁ u_i`, `i ≤ d−4`, by distance) on **77 724** frames; **F3** (`t ≁ u_d` forced) and
**F4** (`t ≁ u_i`, `i ≤ d−5`) on **68 885**. Zero violations.

## 45.2 **`(F11-STRAT)` — the eccentricity stratification, and it is where the target actually lives**

> **`(F11-STRAT)`.** `G` connected C4-free with `μ(G) ≥ 2`, `r := rad(G)`. For every `w`:
> * `ecc(w) ≥ r+2` ⟹ `endpath(G,w) ≥ ecc(w)+2 ≥ r+4` — **UNCONDITIONALLY, by `(TAIL-1)` alone.**
> * `ecc(w) = r+1` ⟹ `endpath(G,w) ≥ r+4` as soon as `(TAIL-2′)` fires at some frame from `w`.
> * `ecc(w) = r` ⟹ `endpath(G,w) ≥ r+4` as soon as `(TAIL-2′)` and then `(TAIL-3′)` fire.
>
> **Hence `(F11-ALL)` is a statement about the NEAR-CENTRAL stratum `{w : ecc(w) ≤ r+1}` only.**

*Proof.* Immediate from `(TAIL-1)`, `(TAIL-2′)`, `(TAIL-3′)`, since `endpath(G,w) ≥ ecc(w)+k`
and `ecc(w) ≥ r`. ∎

**MEASURED over the 420 certified hosts of §43.2's family (16 646 vertices).** Stratum
`ecc−rad`: **0 → 6 903**, **1 → 3 256**, **2+ → 6 487**. So **39.0 %** of all vertices are
already settled by `(TAIL-1)` with nothing imported. Restricted to the **86** hosts with
`l > 4` (5 453 vertices): **2 714 free, 2 011 in stratum 0, 728 in stratum 1** — the free
share is **49.8 %**, and **50.2 % still needs an extension**.
**Against this section's own interest:** **176 of the 420** hosts are **self-centred**
(**38** of the 86 rich ones), and on a self-centred host the stratification is **vacuous** —
every vertex sits in stratum 0 and needs both extensions. The reduction is real and it is
**not** a closure.

## 45.3 **`(F11-DEG)` — an UNCONDITIONAL sufficient condition for `(F11-ALL)`**

> **`(F11-DEG)`.** If `G` is connected, C4-free and **`a(v) ≥ 6` for every `v`**, then
> **`endpath(G,w) ≥ ecc(w) + 4` for EVERY `w`**, hence `(F11-ALL)` holds.
> *Proof.* `a ≥ 6 ≥ 2` gives `(TAIL-1)`'s `y`; `a(y) ≥ 6 ≥ 4` gives `(TAIL-2)`'s `z`;
> `a(z) ≥ 6` gives `(TAIL-3)`'s `t`. ∎
> **The hypothesis LOCALISES**: the proof reads `a(·)` only at `u_d`, `y`, `z` — three
> vertices inside `B₂` of the far end of one geodesic from `w`.

**LIVE, not vacuous — and its live instances are exactly the ones this problem cares about.**
`PG(2,q)` incidence graphs have `a(v) = q+1` at every vertex, so `q ≥ 5` satisfies it.
Certified by **building** the `ecc(w)+4` path at **504 of 504** vertex-tests over the host
slots `PG(2,5)` (twice: it enters both from the family and from the pool), `PG(2,7)`,
`PG(2,11)` — **442 distinct vertices, 3 distinct graphs**. Min-`a` histogram over the pool
of 423 host slots: `a=2 : 395`, `a=3 : 23`, `a=4 : 1`, `a=6 : 2`, `a=8 : 1`, `a=12 : 1`.
**CONTROL, just outside the hypothesis:** `PG(2,3)` (`min a = 4`) still satisfies the
conclusion at **26 of 26** vertices — `(F11-DEG)` is **sufficient and visibly not necessary**.

> **AND IT DOES NOT CLOSE ROUTE A2.** `l > 4` is a **MEAN**; it does not force `a(v) ≥ 6`,
> or even `a(v) ≥ 2`, at a prescribed vertex. §0's standing obstacle applies unchanged.
> What `(F11-DEG)` does is **name the residual exactly**: `(F11-ALL)` can fail only at a `w`
> whose every geodesic frame has a **low-`a` vertex within distance 2 of the far end**.

## 45.4 The `(F11-ALL)` census, with the population that actually matters printed

Over the **417** hosts of order `≤ 130` in the certified family, at **every** vertex, a
depth-capped anchored DFS searched for an induced path on `rad+4` vertices; every witness was
re-verified by the independent checker.

| | count |
|---|---|
| `(host,w)` with a `rad+4` witness | **16 246** |
| `(host,w)` **PROVED BELOW** `rad+4` (search complete, not truncated) | **1** |
| `(host,w)` undecided (truncated) | **0** |
| of the proved-below, with `l > 4` | **0** |
| of the proved-below, with `l > 4` **and** `rad ≥ 5` | **0** |

**The one failure is `dense(s=5,n₀=14)`, `n = 12`, `w = 7`, `rad = 2`, `ecc(w) = 3`,
`l = 2.500`, `endpath(w) = 5 < 6`** — so **`(F11-ALL)` is FALSE without F11's hypotheses**,
with an explicit witness, joining `C₆`, `Θ(3,3,3)` and `Petersen` from the liveness control
(**3 of 5** falsify it there). **Under the hypotheses nothing falsifies it here** — and the
population that sentence is about is printed: of the 417 hosts entered, **83** carry `l > 4`
and **22** carry `l > 4` **and** `rad ≥ 5` (**1 824 vertices**). *EXCLUSIONS: designed
families plus a seeded C4-free process, order `≤ 130`, 3 hosts skipped as too big; not
exhaustive.*

**`G62` stays free. No pocket is closed. `(F11-ALL)` is neither proved nor refuted under its
hypotheses; what round 37 adds is a stratification, a sharp third-step cost, and an
unconditional sufficient condition that names the residual.**

---

# 46. Round 38 — **THE COST IS A MAX OF TWO INVARIANTS, AND THE COVERAGE CENSUS MOVES FROM FRAMES TO VERTICES**

*(**OWNER-CLAIMED, PROVISIONAL, NOT ADJUDICATED** — banked under `PROTOCOL.md` v4 §3.
Nothing here may be cited outward. Machine record: `problems/wowii/w133_r38_tail3pp.py`
→ `.out`, **exit 0, 11 172 checks, 0 failures**, elapsed 5.0 s, all 6 declared parts
self-registered, **system `python3` 3.9.6** (pure stdlib; `networkx`/`sympy` not needed).
§42/§43/§44/§45 are themselves owner-claimed and are used here as such.)*

## 46.1 **`(TAIL-2″)` / `(TAIL-3″)` — count the BAD VERTICES, not the BAD COMPONENTS**

`(TAIL-2′)` and `(TAIL-3′)` pay for the dodge list in `a(·)` alone, because they argue at the
level of **components** of the neighbourhood matching: a blocked component is discarded whole.
That **throws the matching edges away**. Counting the excluded **vertices** instead gives a
second bound, and it is **incomparable** with the first.

> **`(TAIL-2″)`.** In `(TAIL-1)`'s frame (`w = u₀…u_d` a geodesic, `d = ecc(w)`, `y ∈ N(u_d)`
> off `u_{d−1}`'s component), put `k₂ := #{ j ∈ {d−2,d−3} : N(y) ∩ N(u_j) ≠ ∅ }`. Then
> `endpath(G,w) ≥ ecc(w) + 3` as soon as
> **`a(y) ≥ 2 + k₂`  OR  `deg(y) ≥ 3 + k₂`**, i.e. **`max(a(y), deg(y)−1) ≥ 2 + k₂`**.

**Proof.** The first half is `(TAIL-2′)` (§43.1). For the second, let `z ∈ N(y)`; `w…u_d y z`
is induced and anchored iff `z ∉ P` and `z ≁ u_i` for every `i ≤ d`. Count the vertices of
`N(y)` this forbids. **(i)** `u_d` itself, plus the common neighbours of `y` and `u_d` — at
most **one** by C4-freeness: **2 vertices**. **(ii)** For each `j ∈ {d−2,d−3}`, `N(y) ∩ N(u_j)`
has at most **one** element (C4-freeness), and it is empty unless the indicator is set: **`k₂`
vertices**; `u_j ∉ N(y)` for both (`y ≁ u_{d−2}` by `(TAIL-1)`, `y ≁ u_{d−3}` by distance), so
they add nothing. **(iii)** `z ≁ u_{d−1}` is **forced** (`z–y–u_d–u_{d−1}` would be a C4) and
`u_{d−1} ∉ N(y)`: **free**. **(iv)** `z ≁ u_i` and `z ≠ u_i` for `i ≤ d−4` hold by distance:
**free**. So at most `2 + k₂` vertices of `N(y)` are excluded, and `deg(y) ≥ 3 + k₂` leaves
one. ∎

> **`(TAIL-3″)`.** In the same frame with `(TAIL-2″)`'s `z ∈ N(y)`, put
> `k₃ := #{ j ∈ {d−1,d−2,d−3,d−4} : N(z) ∩ N(u_j) ≠ ∅ }`. Then `endpath(G,w) ≥ ecc(w) + 4`
> as soon as **`max(a(z), deg(z)−1) ≥ 2 + k₃`**.

**Proof.** First half is `(TAIL-3′)` (§45.1). For the second, `t ∈ N(z)` must satisfy `t ≁ y`,
`t ∉ P`, `t ≁ u_i` for all `i`. Excluded vertices of `N(z)`: **(i)** `y`, plus the common
neighbours of `y` and `z` — at most **one** by C4-freeness: **2 vertices**. **(ii)** for each
`j ∈ {d−1,…,d−4}` with the indicator set, the at most **one** element of `N(z) ∩ N(u_j)`:
**`k₃` vertices**; none of those `u_j` lies in `N(z)` (`z ≁ u_{d−1}` forced, the rest by
distance from `d(z,u_d) = 2`). **(iii)** `u_d` adds nothing: `N(z) ∩ N(u_d) ⊆ {y}` by
C4-freeness, and `u_d ∉ N(z)`. **(iv)** `i ≤ d−5` free by distance. So at most `2 + k₃`
vertices are excluded. ∎

**WHERE THE GAIN CAN COME FROM — and it is a theorem, not a hope.** `deg = a + t` with `t`
the number of matching edges inside the neighbourhood. The degree half wins where the
component half loses exactly when `a ≤ 1+k` and `deg ≥ 3+k`, which forces **`t ≥ 2`**. So on a
**triangle-free** vertex the degree half can **never** win, and on every `PG(2,q)` incidence
graph — bipartite — the sharpening is **VACUOUS BY CONSTRUCTION.** It is worth exactly the
triangles.

**MEASURED, and every gain CERTIFIED BY BUILDING the path** (417 hosts of order ≤ 130, 3
skipped as too big; **77 724** frames):

| step | blanket §42.3 | `(TAIL-·′)` | `(TAIL-·″)` | frames the `″` form wins |
|---|---|---|---|---|
| 2 (`a(y)`), 77 724 frames | 42 119 | 68 885 | **71 489** | **2 604**, all BUILT |
| 3 (`a(z)`), r37's gate, 68 885 frames | 8 821 | 52 807 | **58 273** | 5 466 |
| 3 (`a(z)`), r38's gate, 71 489 frames | 8 879 | 53 945 | **60 066** | **6 121**, all BUILT |

**Two gates are printed because the step-3 population depends on which step-2 condition let
the frame through.** Under r37's gate this file reproduces **68 885 / 42 119 / 52 807 / 8 821
exactly**, from an independently written script — that is a reproduction of §45.1's row, not a
restatement of it.

## 46.2 **ARE THE SUMMED MINIMA SIMULTANEOUSLY ATTAINABLE? `k₃ = 4` IS NEVER ATTAINED ON THIS FAMILY — AND IT IS NEVERTHELESS ATTAINABLE (AMENDED, round 42)**

§42.3's blanket constants are the counted forms with **every indicator set to 1**: `a(y) ≥ 4`
is `k₂ = 2`, `a(z) ≥ 6` is `k₃ = 4`. **A worst case no frame attains is a wrong constant, not a
conservative one.** Distribution over the same census:

| `k₂` | 0 | 1 | 2 | | `k₃` | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|---|---|---|---|---|
| frames | 24 651 | 37 397 | **15 676** | | frames | 10 494 | 27 497 | 23 620 | **11 593** | **0** |

**`k₂ = 2` IS attained** (`dense(s=1,n₀=14)`, `w = 0`, `d = 3`). **`k₃ = 4` is attained by NONE
of the 73 204 step-3 frames**; the maximum is **3**, and **no frame attains `k₂ = 2` and
`k₃ = 4` together (0).**

> **STATED IN THE ONLY DIRECTION THE EVIDENCE SUPPORTS.** The family is designed plus
> seeded-random and **NOT exhaustive**, so this is a **MEASUREMENT over 417 hosts / 73 204
> frames**, **NOT** a theorem that `a(z) ≥ 6` is the wrong blanket. What it is: the evidence
> that must exist before anyone sums those minima again.

> **AMENDMENT (round 42, on the planner's ruling in `cert_w133_r41.md` §4). THE QUESTION LEFT
> OPEN ABOVE IS ANSWERED, AND IT IS ANSWERED AGAINST OUR INTEREST: `k₃ = 4` IS ATTAINABLE.**
> Brief `E43`'s construction, **rebuilt in round 41 from its own edge list** at `n = 16`, 21
> edges, is connected, **C4-free in this line's sense**, has **`μ = 2`** (brute `α(G[N(v)])`
> at every vertex), and realises the whole `(TAIL-3″)` frame: `w = 0`, geodesic `0..5` with
> `ecc(w) = d = 5`, `y = 6 ∈ N(u₅)` off `u₄`'s matching component, `w,u₁..u_d,y,z` induced,
> `|N(z) ∩ N(u_j)| ≤ 1` at each `j`, and witnesses `{u₄:8, u₃:8, u₂:9, u₁:9}` giving
> **`k₃ = 4`**. **Consequently `(TAIL-3′)`'s blanket constant `a(z) ≥ 6` does NOT drop to 5,
> and `(F11-DEG)`'s hypothesis does not weaken with it.** The `0 of 73 204` above is a
> property of *this family*, not of the class: it stays as a measurement and is no longer
> evidence for a smaller constant.
> **One further fact from that frame, printed because it bounds the amendment:** on it
> `a(z) = 3 < 6`, so the frame attains the index count **without** satisfying the sufficient
> condition — the constant is **sharp**, and the frame is **not** a counterexample to
> `(TAIL-3″)`.
> **PROVENANCE, so the amendment can be audited:** the verdict came from an engine, the
> **object** was rebuilt in this line's own hand (round 41 §4, `problems/wowii/w133_r41_peri.py`,
> exit 0), and the brief that produced it carried a false derived fact in its §2
> (`d(w,z) ≥ d−1`; the truth is `≥ d−2`) which the engine flagged and which
> **`(TAIL-3″)`'s proof above does not use** — its step (ii) is discharged by the INDUCED
> hypothesis, checked line by line in §46.1.

## 46.3 **THE PER-`w` COVERAGE CENSUS — the front, counted in VERTICES instead of FRAMES**

`(F11-ALL)` is a statement **per `(G,w)`**: it needs **one** good frame, not all of them. r37
counted **firings per frame**. This census quantifies **existentially** over far ends,
geodesics, `y` and `z`, and asks how much of the **near-central stratum** — which §45.2 shows
is where the target lives — the `(TAIL-·″)` chain now settles. Sampling: **6** far ends per
`w`, **3** geodesics each.

> **DIRECTION OF ERROR, fixed before the numbers.** COVERED is certified **by building** the
> path, so **COVERED is a LOWER bound** on true coverage and **RESIDUAL is an UPPER bound** on
> the true residual: widening the sampling can only shrink it.

**417 hosts (3 skipped), of which 83 carry `l > 4` and 22 carry `l > 4` and `rad ≥ 5`.**

| | count |
|---|---|
| vertices FREE by `(TAIL-1)` alone (`ecc ≥ rad+2`) | 6 097 |
| **NEAR-CENTRAL POPULATION the verdict is about** | **10 150** |
| … on `l > 4` hosts / on `l > 4` **and** `rad ≥ 5` hosts | 2 730 / **429** |
| COVERED, path BUILT at `ecc+3` | 2 144 |
| COVERED, path BUILT at `ecc+4` | 6 826 |
| **RESIDUAL** | **1 180** |
| … on `l > 4` hosts / on `l > 4` **and** `rad ≥ 5` hosts | 226 / **3** |

**The chain settles 8 970 of 10 150 near-central vertices, and 426 of the 429 inside F11's
hypothesis class.** Adding the free stratum: **15 067 of 16 247 vertices**.

**THE RESIDUAL INSIDE THE HYPOTHESIS CLASS, NAMED ONE BY ONE — three vertices, and this is
what round 39 inherits:**

| host | `n` | `w` | `rad` | `ecc(w)` | `l` |
|---|---|---|---|---|---|
| `PG(2,5)+P4+C5` | 70 | **0** | 5 | 6 | 5.571 |
| `PG(2,5)+P4+C5` | 70 | **62** | 5 | 5 | 5.571 |
| `PG(2,5)+P3+C7` | 71 | **62** | 5 | 5 | 5.521 |

`w = 0` is the attachment vertex inside the `PG(2,5)` core; `w = 62` is the first vertex of the
attached path. **The residual is a boundary phenomenon between the dense core and the sparse
tail**, which is exactly where a mean hypothesis (`l > 4`) is weakest.

## 46.4 **WHAT THE RESIDUAL IS — and it is NOT the statement failing**

Every residual `(G,w)` was re-examined with a depth-capped anchored DFS (all 1 180 had
`n ≤ 80`; **0 skipped**), every witness re-verified by the independent checker, and every
instance with `n ≤ 13` cross-checked against a subset-enumeration oracle.

| | count |
|---|---|
| the **CHAIN IS SHORT** — a `rad+4` path exists anyway | **1 179** |
| the **STATEMENT FAILS** — search COMPLETE, not truncated | **1** |
| UNDECIDED (truncated) | **0** |
| oracle rows (`n ≤ 13`) agreeing with the DFS verdict | **75 / 75** |

**The single failure is r37's own witness** — `dense(s=5,n₀=14)`, `w = 7`, `rad 2`, `ecc 3`,
`l = 2.500`, `endpath = 5 < 6` — **outside F11's hypotheses.** So the entire residual of the
chain is **insufficiency of the chain**, not falsity of the target, with exactly one printed
exception where the target is genuinely false without its hypotheses.

**LIVENESS, designed against this round's own interest.** A coverage census that cannot fail
proves nothing, so the run **asserts** that that vertex lands in the residual **and** comes
back PROVED BELOW. It does. **The census can fail, and on the one instance where the statement
is false it did.**

> **`(F11-DEG″)`.** If `G` is connected and C4-free with **`max(a(v), deg(v)−1) ≥ 6` for every
> `v`**, then `endpath(G,w) ≥ ecc(w)+4` for every `w`, hence `(F11-ALL)`.
> *Proof.* The hypothesis forces `a(v) ≥ 4` everywhere (`a = 1 ⟹ deg ≤ 2`; `deg ≥ 7 ⟹ a ≥ 4`),
> so `(TAIL-1)`'s `y` exists; `k₂ ≤ 2` and `k₃ ≤ 4` then make `(TAIL-2″)` and `(TAIL-3″)`
> fire. ∎ **Strictly weaker than `(F11-DEG)`** (`deg ≥ a`), and it sharpens the residual: the
> obstruction must be low in **both** invariants. **Tested on all 1 180 residual vertices: the
> prediction holds 1 180 / 1 180.**

> **AND AGAINST THIS ROUND'S INTEREST, PRINTED:** over a pool of **424** host slots,
> `(F11-DEG)` admits **4** and `(F11-DEG″)` admits **4** — **the weakening buys ZERO hosts
> here**, though **905 of 17 114 individual vertices** gain by it. `(F11-DEG″)` is a theorem
> either way; on this pool it is **not** progress, and this section says so rather than
> shipping a formal generalisation as a result.

**`G62` stays free. No pocket is closed. `(F11-ALL)` is still neither proved nor refuted under
its hypotheses.** What round 38 adds: a sharper cost with a measured margin, a coverage figure
in the unit the target is stated in, a residual of **three named vertices** inside the
hypothesis class, and the finding that the blanket's own worst case is **never attained** on
the family the line has been measuring on for six rounds.

# 47. Round 42 — **DRAFT §42.4's RESIDUAL ROW IS NON-EMPTY INSIDE ROUTE A2's CLASS, AND THE CLASS SPLITS IN TWO**

All of §47 is **PROVISIONAL** and stated in this file only. Machine record:
`problems/wowii/w133_r42_split.py` → `.out` (**exit 0, 3 154 checks, 0 failures**),
`problems/wowii/w133_r42_min.py` → `.out` (**exit 0**), and two **standalone** verifiers that
share no code with the builder, `problems/wowii/w133_r42_verify_w42a.py` and `…_w42b.py`
(**exit 0**). Interpreter: system `python3` 3.9.6, pure stdlib. No SAT, no exhaustive graph
enumeration: every host below is a designed construction with seeded-random matchings.

## 47.1 **(SPLIT) — the residual row's class is the disjoint union of two named sub-classes**

Write the row's predicate as in §42.4 / round 39: `G` connected and `C4`-free with `μ ≥ 2`,
`rad(G) = r`, and a vertex `w` with

> **(2)** `ecc(w) = r+1`   and   **(3)** `d(c,w) = r` for **every** centre `c`.

> **(SPLIT).** If additionally `r ≥ 2`, then **exactly one** of
> **CASE A** `diam(G) = r+1`, and then **(2) is implied by (3)** and needs no separate search;
> **CASE B** `diam(G) ≥ r+2`, and then `(G,w)` is a **counterexample to `(RXM-PERI)`**.
>
> *Proof.* `diam ≥ ecc(w) = r+1`, so the two cases are exhaustive and disjoint. In CASE A,
> (3) forces `w ∉ Ctr` (else `d(w,w) = 0 = r ≥ 2`), and **(PER-A)** (round 41: `diam = rad+1`
> and `w ∉ Ctr` ⟹ `ecc(w) = diam`) gives `ecc(w) = r+1`. In CASE B, `w` satisfies
> `(RXM-PERI)`'s hypothesis, namely (3), and `ecc(w) = r+1 < diam` denies its conclusion. ∎
>
> **`(PER-B)` cannot fire here:** it needs `ecc(w) = 2r`, and `r+1 < 2r` for `r ≥ 2`. So on
> this row **only `(PER-A)` can force a pass**, and only in CASE A.

**Two consequences, and neither was available before round 41.**
**(C1)** If `(RXM-PERI)` restricted to `l > 4 ∧ rad ≥ 5` is **true**, CASE B is **empty** and
the row's question collapses to CASE A. The two questions round 41 left open are **not
independent — one is half of the other.**
**(C2)** A CASE B instance **refutes** that restricted `(RXM-PERI)`.

## 47.2 ⭐ **THE ROW IS NON-EMPTY — 146 instances, all CASE B, two of them independently re-verified**

A host that can carry a CASE A instance must be **round** (`diam = rad+1`), **dense**
(`l > 4`) and **long** (`rad ≥ 5`) at once. Every in-class host this line had ever run is a
dense core with a tail: **0 of the 25 hosts with `l > 4 ∧ rad ≥ 5` in the 417-host family has
`diam = rad+1`** (offsets `+3 : 7, +4 : 2, +5 : 6, +6 : 4, +7 : 4, +8 : 1, +9 : 1`).

**THE NECKLACE.** `m` blocks in a **cycle**, block `i` the incidence graph of `PG(2,q_i)`;
block `i` is joined to block `i+1` by a partial injection whose **sources form an independent
set of block `i`** (its points). A cross-block `C4` would need two matched vertices adjacent
inside block `i`, which independent sources forbid; **this needs `m ≥ 5`**, because at `m = 4`
blocks `i` and `i+2` are joined by two routes (§47.4, defect 1). Every host is nevertheless
**certified by machine**, never by the argument.

| | count |
|---|---|
| necklace hosts certified `C4`-free with `μ ≥ 2` | **396** |
| … in class (`l > 4` **and** `rad ≥ 5`) | **393** |
| … of those, CASE A hosts (`diam = rad+1`) | **57** |
| vertices maximally far from every centre, on in-class hosts | **1 095** |
| … on CASE A hosts / on CASE B hosts | **0 / 1 095** |
| **instances of the row (conditions (2)+(3), `rad ≥ 5`, `l > 4`)** | **146** |

Eccentricity-offset profile of the 1 095: `+1 : 146`, `+2 : 627`, `+3 : 284`, `+4 : 36`,
`+5 : 2` — **offset `+2` is the mode**, which is r41's finding on a third family.

> **⭐ SO DRAFT §42.4's RESIDUAL ROW IS NOT EMPTY INSIDE ROUTE A2's CLASS.** It cannot be
> closed by emptiness; it must be closed by an argument.
> **⭐ AND ALL 146 ARE CASE B, SO `(RXM-PERI)` RESTRICTED TO `l > 4 ∧ rad ≥ 5` IS ALSO FALSE.**
> The narrower question round 41 left standing is answered, in the same objects.

**TWO NAMED WITNESSES, each re-verified by a standalone script that shares no code with the
builder** (distances by matrix relaxation, `α(G[N(v)])` by exhaustive subset enumeration,
`C4`-freeness by a nested common-neighbour count):

| witness | `n` | `\|E\|` | `μ` | `l` | `rad` | `diam` | `Ctr` | `w` |
|---|---|---|---|---|---|---|---|---|
| **`W42a`** | **96** | 193 | 3 | **4.0208** | **5** | 8 | `{70,71}` | **33, 35** |
| **`W42b`** | **234** | 553 | 4 | **4.7265** | **7** | 10 | `{157}` | **54** |

Each `w` has `ecc(w) = rad+1` and `d(c,w) = rad` for every centre, and `ecc(w) < diam`.

## 47.3 **WHAT THIS DOES NOT BREAK — printed beside the result, not around it**

* **No counterexample to WOWII-133, and none to §42.5, is claimed or implied.** The row needs
  `endpath(G,w) ≥ ecc(w)+3`, and on **all 146** instances such a path was **BUILT and passed
  by the independent anchored-induced-path checker** (`146/146`, direction of error fixed
  first: BUILT is a **lower** bound). So `(TAIL-2)`/`(B2)` **covers every instance found**.
  The row is real **and** so far always covered.
* **Round 39 §2's census is undamaged, and the reach of its base family is now measured.**
  **What was re-run this round:** the 417-host family, where **all 25** in-class hosts have
  `diam ≥ rad+2`, so by (SPLIT) every condition-3 vertex on them is a CASE B candidate and
  **0** of them could have come out CASE A. **What was NOT re-run:** the 24 extra control hosts
  round 39 built (`PG(2,7)` cores, long tails, two-root tails, two joined cores). They are all
  core-plus-tail shapes and so are expected to be `diam ≥ rad+2` as well, **but this round did
  not measure them and does not assert it.** Read through (SPLIT), r39's `0 at offset +1` is
  evidence that `(RXM-PERI)` *holds* at `rad ≥ 5 ∧ l > 4` — a statement §47.2 refutes anyway.
* **CASE A IS ALL BUT UNTESTED AT `rad ≥ 5`, and the round reports the contentful part rather
  than the headline count.** Of the **57** in-class CASE A hosts built here, **`(CS-1′)`
  decides **53** empty outright** (`|Ctr| > max_w |S_rad(w)|`, so no condition-3 vertex can
  exist there — a proof, not a census), leaving **4** LIVE hosts: `NLsd(6,s3)`,
  `NLsd(6,s4)`, `NLsd(6,s5)` (`n = 120`, `l = 4.650`) and `NLkd(3^6,s3)` (`n = 156`,
  `l = 5.000`), all `rad 5, diam 6`, with `|Ctr| = 25, 20, 26, 12` against
  `max_w |S_5(w)| = 41, 42, 43, 44`. **THE CONTENTFUL CASE A POPULATION IS 516 vertices, 433
  of them non-central, and it yields 0 condition-3 vertices.** That is the only CASE A number
  this round is entitled to; the `0 of 57 hosts` is not one.
* **The two `rad = 4` instances this line has quoted since round 32** — `rand(s=7,n₀=18)`
  (`n=18, rad 4, diam 7, l = 2.333, w = 11`) and `rand(s=30,n₀=22)` (`n=22, rad 4, diam 7,
  l = 2.455, w = 13`), both rebuilt here from round 32's own generator — are **both CASE B**,
  with `|Ctr| = 1`. **Every known instance of the row above `rad = 2` is CASE B.**

## 47.4 Owner errors this round — three, and one of them had been in this file for three rounds

1. **MY OWN CONSTRUCTION ARGUMENT WAS WRONG AT `m = 4`, AND MY OWN RUN CAUGHT IT.** The
   independent-sources argument does not exclude the two-route `C4` between blocks `i` and
   `i+2` when `m = 4`; two of fifteen `m = 4` necklaces built are **not** `C4`-free. Corrected
   to `m ≥ 5`, and the exclusion is **exhibited, not asserted**. Caught before any number left
   this file.
2. **A WRONG PROVENANCE, SHIPPED IN THIS FILE FOR THREE ROUNDS.** Round 39 §1 and its ledger
   attribute the two `rad = 4` instances to *"r36's own 145-base family"*. They are round
   **32**'s (`rand(s,n₀)` on round 32's 145-base family, rebuilt here). Round 36's base family
   carries **0** conditions-1–3 instances with `μ ≥ 2` (only 5 of its 816 configurations even
   have `μ ≥ 2`). **The datum is right and the attribution is wrong; the attribution went to
   the planner in the round-39 ledger, so it ESCAPED.** Brief `E44` §5(b), which says only "a
   different family of 145 base graphs", is **correct** and is not affected.
3. **A PROSE OVER-CLAIM IN MY OWN RUN's OUTPUT.** §47.3's first draft asserted that round 39's
   *whole* control could not have produced a CASE A instance. The run rebuilds only the
   417-host family; r39's 24 extra control hosts were not rebuilt. Rewritten to what was
   measured, with the expectation printed as an expectation. **This is §81 applied to a
   sentence rather than a number — the same shape as round 39's own first defect.**

---

# §48 CASE A IS NOT EMPTY EITHER — and the coordinate it is easy in is not the one we were searching

*(owner-w133 round 43, 2026-08-23. Machine record `problems/wowii/w133_r43_caseA.py` ->
`.out` (**EXIT 0, 1 321 checks, 0 failures, 13.6 s**, PARTS 0–7), witnesses re-verified by the
STANDALONE `problems/wowii/w133_r43_verify_W43.py` -> `.out` (**EXIT 0, 22 checks**), which
shares no code with the builder. Interpreter: system `python3` 3.9.6, pure stdlib. No SAT, no
exhaustive graph enumeration.)*

## 48.1 (FAR), (CA-EQ), (CA-1) — condition 4 restated, and what the restatement costs

> **(FAR).** For any `G` and any `w`: `w` satisfies condition 4 (`d(c,w) = rad` for every
> centre `c`) **iff** `w ∈ ⋂_{c ∈ Ctr(G)} S_rad(c)`.
> *Proof.* `d(c,w) ≤ ecc(c) = rad` always, so `d(c,w) = rad` says `w` **realises the
> eccentricity of `c`**. Condition 4 asks that of every centre at once. ∎

> **(CA-EQ).** Let `G` be ROUND (`diam = rad+1`), `rad ≥ 1`. Then `G` carries an instance of
> the CASE A class **iff** `⋂_{c ∈ Ctr} S_rad(c) ≠ ∅`, and every `w` in that intersection is
> one, with `ecc(w) = rad+1` free by (PER-A).
> **(CA-1).** If `|Ctr(G)| = 1` the intersection is `S_rad(c)`, which is non-empty by the
> definition of eccentricity. **So every round host with a unique centre carries an instance
> and needs no search at all.**

**CASE A is therefore a property of the HOST, not of a (host, `w`) pair**, and the obstruction
is not that `Ctr` is BIG but that it is **SPREAD**: a centre set with no common eccentricity
witness. Brief `E46`'s reply asked instead for a *"dominant centre subset, `|Ctr|` between
roughly half and two-thirds of `|S_r(w)|`"* — a **readback of our four live hosts stated as a
requirement**, and one that does not even describe them (`12/44` is 27%). Condition 4 imposes
**no lower bound** on `|Ctr|`; `|Ctr| = 1` is the easiest case, not an excluded one. **A search
steered by that break point would have hunted the hardest corner and skipped the free one.**

## 48.2 (SYM-BAR) — symmetry alone can forbid condition 4

> **(SYM-BAR).** Let `Γ ≤ Aut(G)` permute the parts of a partition `P` of `V(G)` **transitively**.
> If one part `P₀` has `max{d_G(u,v) : u,v ∈ P₀} < rad(G)`, then **no** vertex of `G` satisfies
> condition 4.
> *Proof.* `Ctr(G)` is `Aut`-invariant, hence a union of `Γ`-orbits, hence meets **every**
> part. Given `w`, pick `γ` with `γ(P(c)) = P(w)`; then `γ(c)` is a centre inside `P(w)`, so
> `d(w, γ(c)) ≤ diam_G(P(w)) < rad`, contradicting condition 4. ∎

Corollaries: vertex-transitive graphs are barren (parts = singletons); **every rotation-symmetric
necklace is barren for a reason** (block diameter 3 < `rad ≥ 5`), so no search on one measures
anything. **Exhibited, not asserted**: eight rotation-symmetric necklaces built, the rotation
**verified to be an automorphism by machine**, `Ctr` meets every block on all eight, condition-4
vertices on all eight `0`. Round 42's necklaces use a fresh random injection per junction and are
**not** exactly symmetric, so (SYM-BAR) does not apply to them as a theorem — §48.3 measures
whether they behave as if it did.

## 48.3 The mechanism, MEASURED in the localisation coordinate

652 in-class (`l > 4`, `rad ≥ 5`) `C4`-free `μ ≥ 2` necklace hosts, round 42's family rebuilt
plus new asymmetric designs (one subdivided junction, one thin junction, thin-and-long, two
dented seams, one odd block). Rows = number of distinct blocks `Ctr` meets; columns = `diam−rad`.

| blocks \ offset | +0 | +1 | +2 | +3 | ≥+4 |
|---|---|---|---|---|---|
| 1 | 0 | **0** | 17 | 60 | 18 |
| 2 | 0 | **0** | 9 | 48 | 9 |
| 3 | 0 | **0** | 20 | 31 | 6 |
| ≥4 | 0 | **100** | 243 | 90 | 1 |

**Every one of the 100 round hosts has its centre spread over ≥ 4 blocks; every one of the 161
hosts with a localised centre (≤ 2 blocks) has `diam ≥ rad+2`.** That is a **measured
anti-correlation over a population of 652 in which it could have failed — not a theorem.**
Entitled CASE A number this round: **14 LIVE round hosts** (2 234 vertices, 1 879 non-central)
after (CS-1′) decides the other 86 outright ⟹ **0**. The four live hosts of §47 are not near
misses: the best `w` misses **7 to 22** of the centres, and the centres sit at *every* distance
from it (e.g. `NLkd(3^6,s3)`: `2:2, 3:3, 4:2, 5:5` where condition 4 wants all `= 5`).

## 48.4 ⭐ CASE A IS NON-EMPTY — leave the cycle, and it appears

The necklace is a **cycle** of blocks, and a cycle is what makes the eccentricity flat and the
centre spread. Dropping that topology (theta graphs, theta/K4/cycle-plus-chord **of blocks**,
and finally **random `C4`-free graphs with a degree cap**) gives:

| witness | `n` | `|E|` | `μ` | `l` | `rad` | `diam` | `|Ctr|` | condition-4 vertices |
|---|---|---|---|---|---|---|---|---|
| **`W43a`** | 420 | 1 049 | 4 | **4.995238** | **5** | **6** | **1** | **128** |
| **`W43b`** | 420 | 1 049 | 4 | **4.995238** | **5** | **6** | 8 | 1 |

> **⭐ DRAFT §42.4's RESIDUAL ROW IS NON-EMPTY IN *BOTH* HALVES. CASE A IS NOT EMPTY, so the
> row cannot be closed by emptiness anywhere, and brief `E46`'s question is ANSWERED — by
> construction, not by argument.**

`W43a` is the (CA-1) case made real: **a unique centre**, and all 128 of its eccentricity
witnesses satisfy condition 4 at once. Both are re-verified by a standalone script sharing **no
code** with the builder (distances by **bitset relaxation** instead of BFS, `a(v)` by
**brute-force subset enumeration** instead of the matching identity, `C4`-freeness by a
from-scratch nested common-neighbour count).

**Printed beside the result, not around it.** *(TAIL-2)* covers both: an anchored induced path
on `ecc(w)+3 = 9` vertices was **BUILT and checker-verified** on each (`W43a`:
`10,88,38,42,146,51,45,207,21`; `W43b`: `119,48,73,15,3,43,90,58,228`). **No counterexample to
§42.5 or to WOWII-133 is claimed.** `l = 4.9952 > 4` but only just; `rad = 5` exactly; both
hosts come from a **seeded-random** sampler, so the family is a sampler, not a construction with
a proof behind it.

## 48.5 What the same sweep says about where the obstruction is NOT

* **Conditions 1,2,3,4 without condition 5**: satisfiable at `rad = 5` with `l = 2.9545`
  (`S(88,44,3)`, `n = 44`, `|E| = 65`, `μ = 2`, `|Ctr| = 3`, `w = 31`) — **the first object on
  this line meeting conditions 1,3,4 above `rad = 2`.** So no emptiness proof for the CASE A
  class can avoid condition 5, and (after §48.4) none can succeed at all.
* **The `rad = 2` positive control** — without which every `0` in this round would have been a
  statement about the instrument: 207 live round control hosts, **166 carry condition 4**.
  The first version of this round's probe had **no** control and its `0` was uninterpretable;
  that is recorded in §48.6.
* **(R3″), repairing brief `E46`'s only real claim.** `G` connected `C4`-free, `δ ≥ 2`,
  `r = rad ≥ 3`, `w` satisfying condition 4, `ecc(w) = r+t`: then
  **`|Ctr| ≤ n − δ(δ−1) − r + 2 − t`**, `t ≥ 1` by (BRACKET). Proof: the spheres
  `S_0..S_{r+t}(w)` are non-empty and partition `V`; `(CS-2)` gives `|B₂| ≥ 1+δ(δ−1)`;
  `S_3..S_{r−1}` give `r−3`; `Ctr ⊆ S_r(w)`; `S_{r+1}..S_{r+t}` give `t`. ∎ **The gain over
  (CS-3) is exactly `t`, not the 2 that `E46` claimed** — its proof asserts `Ctr ∩ B_r(w) = ∅`
  while assuming `Ctr ⊆ S_r(w)`, and counts `S_r(w)` twice. **(R3″) also needs no roundness**,
  so unlike `E46`'s version it is testable, and it is asserted on 40 live condition-4 pairs.
  Both bounds are **vacuous at `δ = 3, 4`** and neither helped.

## 48.6 Owner errors this round — three, all caught before this entry left the file

1. **A PROBE WITH NO POSITIVE CONTROL.** PART 5's first run reported `0` condition-4 vertices
   over 588 round hosts at every `rad` **including `rad = 2`, where 414 instances are known** —
   i.e. the detector had never been shown to fire at all. **The run said so itself** ("the probe
   never contained a positive control … recorded as an instrument failure") and the control was
   added by RUNNING, not by deleting the number: 207 live round control hosts, 166 carriers.
   **Without that repair this round would have banked an emptiness signal from a dead
   instrument.**
2. **A WRONG CONCLUSION SENTENCE IN MY OWN OUTPUT (§81 applied to prose, again).** PART 6 first
   printed that P9's failure "points at (E1)" — that roundness alone forbids the configuration
   above `rad = 2` — while **the SPC column of the same table showed 301 carriers at `rad ≥ 3`**.
   The GEN sampler had produced only 233 round hosts at `rad ≥ 3` at all. Rewritten to say the
   failure is a sampler artefact and that (E1) is refuted by the neighbouring column.
3. **A MISLABELLED GUARD HOST.** PART 0's guard table listed a host as `NLsd(5,s4)` that was
   built with `[3]*5` blocks, not round 42's `[3,2,3,2,3]` — the row printed `n = 130, |Ctr| =
   115` where round 42's `NLsd(5,s4)` is `n = 106, |Ctr| = 1`. **Same defect species as round
   42's escaped provenance error**, caught this time inside the guard it was corrupting; fixed,
   and the two real carriers (`NLsd(5,s3)`, `NLsd(5,s4)`) added to the guard set.

**Guard this round — (D9) COUNT-FOR-PLACEMENT**: deciding whether a host *can* carry condition 4
from `|Ctr| ≤ max_w |S_rad(w)|` instead of from `⋂_c S_rad(c) ≠ ∅`. One-sided by a theorem
(condition 4 ⟹ the count passes), so it can only over-fire — and it does: **14 guard hosts, the
correct predicate fires on 3 (`P3`, `NLsd(5,s3)`, `NLsd(5,s4)`), (D9) fires on 9, EXTRA 6,
MISSES 0.** It is the exact defect brief `E46`'s §3 fell into.

## 48.7 Slice 2: the cover holds on the new instances, and the centre collapse is a curve

*(Machine record `problems/wowii/w133_r43b_tail.py` -> `.out`, **EXIT 0, 9 checks, 0 failures,
3.7 s**; all three witnesses re-verified together by the standalone
`problems/wowii/w133_r43_verify_W43.py` -> `.out`, **EXIT 0, 33 checks, 0 failures**.)*

* **(TAIL-2) COVERS EVERY ONE.** The `ecc(w)+3` anchored induced path was **BUILT and
  checker-verified on 129 of 129** condition-4 vertices of `W43a` and `W43b` (128 + 1).
  **No counterexample to §42.5 or to WOWII-133 is claimed, on either half of the row.**
  A BUILT path is a lower bound on `endpath`; nothing here is an exhaustive longest-path search.
* **`l ≤ mean degree`, so a degree cap of 4 CANNOT satisfy condition 5.** `a(v) = α(G[N(v)]) ≤
  deg(v)`, hence `l(G) ≤ 2|E|/n`. Slice 1's cap-4 rows printing `l = 4.0000` exactly are that
  identity, not luck: **cap ≥ 5 is forced**, and with it a lower bound on `n` if `rad ≥ 5` is to
  survive.
* **THE CENTRE COLLAPSE, AS A CURVE.** 98 cap-5 hosts in class, 82 of them round, over
  `n ∈ {180,…,420}` at 14 seeds each. Typical `|Ctr|`: `≈176` at `n=180`, `≈216` at 220,
  `≈235` at 260, `≈200` at 300, `≈118` at 340, `≈47` at 380, **`4–17` at 420** — and
  **condition 4 is carried on 6 of the 14 seeds at `n = 420` and on none below it.**
  **The centre collapses as `n` approaches the largest order at which a cap-5 `C4`-free host
  still has `rad = 5`, and condition 4 becomes satisfiable exactly there.** Measured over a
  population of 82 round hosts in which it could have come out otherwise; **not proved**.
* **A REGISTERED PREDICTION THAT FAILED.** Slice 2 predicted an instance with `n < 420` and
  found none on its grid: the grid's minimum is 420, the same as slice 1's. Recorded as a
  failed prediction, not smoothed away.
* **Third witness, verified with the other two.** `W43c` (`SP5(420,1)`): `n = 420`,
  `|E| = 1 050`, **`μ = 5`**, **`l = 5.000000`**, `rad 5`, `diam 6`, `|Ctr| = 6`, 2 condition-4
  vertices, and its own `ecc(w)+3` path BUILT and checked. It clears condition 5 by a full
  unit rather than by `0.0048`.

---

# §49 Round 44 — **THE RESIDUAL ROW'S ANCHOR IS FREE IN TWO LANES OF THREE, AND OUR OWN CASE A WITNESSES DO NOT EXHIBIT THE OPEN CASE**

*(owner-w133 round 44, 2026-08-23. **PROVISIONAL, stated in this file only.** Machine record
`problems/wowii/w133_r44_row.py` → `.out` (**EXIT 0, 262 checks, 0 failures, 20.1 s**, PARTS
0–4 self-registered); the new witness re-verified by the **STANDALONE**
`problems/wowii/w133_r44_verify_W44a.py` → `.out` (**EXIT 0, 1 496 checks, 0 failures**),
which shares **no code** with the builder and reads only the edge list
`problems/wowii/w133_r44_W44a.txt`. Interpreter: system `python3` 3.9.6, pure stdlib. No SAT,
no exhaustive graph enumeration; every path is BUILT and then re-checked.)*

## 49.1 **(IDENT) — the bookkeeping the whole section rests on, and the guard on it**

> **(IDENT).** `G := H +` one pendant `p` at `w`. Since `deg(p) = 1`, an induced path of `G`
> either misses `p` or has `p` as an **endpoint** with the rest an induced path of `H` ending
> at `w`. Hence **`path(G) = max( path(H), 1 + endpath(H,w) )`**, and in particular
> **`path(G) ≤ 1 + path(H)`.** ∎

**Verified by COMPLETE search** (longest induced path, no cap, search certified complete) on
**97 of 97** `(host, w)` pairs over 12 hosts. **GUARD — (D10) HAIR-ON-ANY-PATH**: evaluating
the row with `1 + path(H)` in place of (IDENT), i.e. crediting the pendant to an induced path
that does **not** end at `w`. It is **one-sided by the proof above**, so its MISSES must be 0:
**EXTRA 29 of 97, MISSES 0**, worst over-claim `P5, w = 1` (true `5`, (D10) says `6`).
**(D10) is exactly draft §41's already-refuted `(A2-PATH)` (`path(G) ≥ path(H)+h`)**; §49.2
uses only the `h = 0` half, `path(G) ≥ path(H)`.

## 49.2 ⭐ **(ROW-3) — the row stratifies by `diam − rad`, and two of the three lanes carry no anchor**

Draft §42.5 discharges the residual row through **(B2)**, `path(G) ≥ 1 + endpath(H,w)` — at the
**prescribed** `w`, which is the entire difficulty. But **(B1)**, `path(G) ≥ path(H)`, carries
**no anchor at all**, and `path(H) ≥ endpath(H,v)` for **every** `v`. Feeding
(TAIL-1)/(TAIL-2) in at a **diametral** vertex instead of at `w`:

> **(ROW-3).** Let `(H,w)` be a residual-row instance (`H` connected C4-free, `μ(H) ≥ 2`,
> `r := rad(H)`, `ecc_H(w) = r+1`, `d(c,w) = r` for every centre `c`), `G := H +` one pendant
> at `w`, `D := diam(H)`, and `k := ⌊l(G)⌋`, so the target is `path(G) ≥ (r+1)+k`. Then
> * **`D+1 ≥ (r+1)+k`** ⟹ a **geodesic of `H` alone** closes it (draft §12's `(R1)` shape);
> * **`D+2 ≥ (r+1)+k`** ⟹ **(TAIL-1) at a diametral vertex** closes it **UNCONDITIONALLY** —
>   no anchor, no F11, no `l > 4`, no `rad ≥ 5`;
> * **`D+3 ≥ (r+1)+k`** ⟹ **(TAIL-2) at ANY ONE diametral vertex** closes it — an
>   **existential over the whole diametral set**, not a statement at a named vertex;
> * otherwise the **prescribed anchor** is needed: (TAIL-2) at `w`, plus the hair.
>
> *Proof.* (IDENT) gives `path(G) ≥ path(H) ≥ endpath(H,v)`; (TAIL-1)/(TAIL-2) at `v` with
> `ecc(v) = D` give `D+2` / `D+3`; the last line is §42.5's own (B2). ∎

**At `k = 4` this reads: offset `≥ +3` is CLOSED UNCONDITIONALLY; offset `= +2` needs
(TAIL-2) somewhere on the diametral set; offset `= +1` — exactly `(SPLIT)`'s CASE A — is the
only lane that still needs the prescribed anchor.** **The ingredient is OLD** (draft §12's
reductions `(R1)`/`(R2)`, Lemma `G10`, and `(TAIL-1)` itself, one level up); **what is new is
only that the row had never used the fact that its own (B1) leg is anchor-free.**

**MEASURED over 601 residual-row instances** (round 42/43's 652-host in-class family rebuilt,
plus `W43a`/`W43b`/`W43c`), **every certificate BUILT and then re-checked from scratch**:

| offset `D−r` | +1 | +2 | +3 | +4 |
|---|---|---|---|---|
| instances | **131** | 336 | 122 | 12 |

| lane | count |
|---|---|
| `L0` geodesic of `H` | 12 |
| `L1` (TAIL-1) at a diametral vertex — **UNCONDITIONAL** | **122** |
| `L2` (TAIL-2) at some diametral vertex | 306 |
| `L3` (TAIL-2) at the **prescribed** `w`, plus the hair | 131 |
| **`OPEN` at `k = 4`** | **0** |
| `BEYOND` — the instance's own `⌊l(G)⌋ ≥ 5` | 30 |

**134 of 601 are closed with no anchor, no F11, no `l > 4` and no `rad ≥ 5`.** 571
certificates re-checked: **0 not induced, 0 too short.** The **30 `BEYOND` rows** are row
instances whose own `⌊l(G)⌋` is 5 or more — **the next pocket, not route A2's**; none of the
four lanes reaches them, and they are printed rather than folded into "open".

## 49.3 ⭐⭐ **(ROW-MU4), and what it costs round 43 — stated first, not buried**

> **(ROW-MU4).** If `μ(H) ≥ 4` then `endpath(H,w) ≥ ecc(w)+3` for **every** `w`.
> *Proof.* `a(u_d) ≥ 4 ≥ 2` gives (TAIL-1)'s `y`; `a(y) ≥ 4` is (TAIL-2)'s **blanket**
> hypothesis (§42.3) at that same `y`. ∎

It is a one-line corollary. What it costs is this:

> **ROUND 43's THREE CASE A WITNESSES ALL HAVE `μ ≥ 4`** (`W43a` 4, `W43b` 4, `W43c` 5).
> **So round 43 slice 2's `129 of 129` built paths were never evidence about the open case —
> (TAIL-2) could not have failed on them.**

`W43a`/`W43b`/`W43c` **do** populate §42.4's residual row, which is what round 43 claimed and
which **stands**; they do **not** test the one question that can still break WOWII-133 on it.
Re-measured here: each is the route A2 instance `G = H +` pendant with **`rad(G) = 6`**
(so `(RAD-1P)` fires in the direction the row needs), **`⌊l(G)⌋ = 4`**, **target
`path(G) ≥ 10`**; over **131** condition-4 vertices the `ecc(w)+3` anchored induced path is
**BUILT on 131**, and at **131 of 131** the frame's own `y` has `a(y) ≥ 4` — i.e. (ROW-MU4)
applies at every one. **LIVENESS:** on `C₆` (`μ = 2`) the same detector **declines**
(§42.2's tightness example), so "it fired" is information rather than a tautology.

## 49.4 **(ROW-HARD) — what an instance that is still open must look like**

> **(ROW-HARD).** Let `(H,w)` be a residual-row instance at offset `+1` with `k = 4`. If it is
> **not** closed then for **every** far end `x` of `w`, **every** `w`–`x` geodesic `u₀…u_d`
> and **every** `y ∈ N(u_d)` admissible for (TAIL-1),
> **`max(a(y), deg(y)−1) ≤ 1 + k₂(y) ≤ 3`** — so `a(y) ≤ 3` **and** `deg(y) ≤ 4` at every such
> `y`, and since `μ(H) ≥ 2` forces `a(y) ≥ 2`, every such frame also has `k₂(y) ≥ 1`.
> *Proof.* Contrapositive of `(TAIL-2″)` (§46.1) plus the hair. ∎

**So the obstruction is not `n` and not `|Ctr|`: it is a LOW-`a` COLLAR around EVERY far end
of `w`.** Measured as the slack `SLACK(H,w) := max over admissible frames of
[max(a(y),deg(y)−1) − (2+k₂(y))]`; `SLACK < 0` at an offset-`+1` instance **is** the open case.

**DIRECTION OF ERROR, FIXED BEFORE THE NUMBERS:** frames are **sampled** (≤ 6 far ends, ≤ 2
geodesics each), so the printed `SLACK` is a **LOWER** bound on the true maximum. A printed
`SLACK ≥ 0` is therefore **sound**; a printed `SLACK < 0` would be **inconclusive** and could
not be called an open instance without an exhaustive frame enumeration at that vertex.

| `SLACK` | +0 | +2 | +3 | +4 | +5 | +6 |
|---|---|---|---|---|---|---|
| instances | **1** | 6 | 245 | 345 | 2 | 2 |

**Minimum `SLACK` anywhere: `+0`, attained exactly once** — `SUB3(3^9,s1)`, `n = 273`,
`rad 8`, `diam 10`, `μ = 2`, `l = 4.5714`, `w = 173`, **10 frames examined and every one of
them tight**. That is the closest object this line holds to a hard instance, and it is at
offset `+2`, so `(ROW-3)`'s lane `L2` closes it anyway. Frame counts per instance: **595 of
601 have ≥ 10 admissible frames**; the collar `N(S_{ecc(w)}(w))` has **median size `0.192·n`**
(extremes: `|S| = 1, |collar| = 4, n = 160` and `|S| = 39, |collar| = 90, n = 205`).
**`(ROW-HARD)` asks `a ≤ 3` on all of that collar while `l > 4` asks the average of `a` over
all `n` vertices to exceed 4 — a design constraint, NOT a theorem: C4-freeness permits mean
degree up to order `√n`, so at these orders the two demands do not yet contradict.**

## 49.5 ⭐ **`W44a` — the first CASE A instance with `μ ≤ 3`, and it still is not hard**

Round 43 owed "bring `n` below 420". **§49.3 says the binding coordinate is `μ`, not `n`**, so
the search is re-aimed. **Registered before the run:** *(P1)* one-edge subdivision of `W43a`
yields a CASE A instance with `μ = 2`; *(P2)* **nothing produced this round will have
`SLACK < 0`**.

> **Subdividing an edge `uv` that lies in NO triangle preserves C4-freeness**, because any
> 4-cycle through the new vertex `m` is `m–u–p–v–m` with `p` a common neighbour of `u,v`; and
> `N(m) = {u,v}` with `u ≁ v`, so **`a(m) = 2` by construction** and `μ` drops to 2 without
> luck. (Every one of `W43a`'s 1 049 edges is triangle-free.)

| witness | `n` | `\|E\|` | `μ` | `l` | `rad` | `diam` | `\|Ctr\|` | condition-4 vertices |
|---|---|---|---|---|---|---|---|---|
| **`W44a` = `SD(W43a, 0–163)`** | 421 | 1 050 | **2** | 4.988124 | 5 | 6 | **1** | **129** |

**41 subdivisions tried: 41 still C4-free, 27 still round, 27 in-class CASE A carriers with
`μ = 2`** (the other shapes: 10 at `diam = rad+2`, 4 round but barren). Probe B (an
independent degree-capped sampler at cap 5 and 6, `n ∈ {360,420,480}`) added one further
carrier, `SP5(480,s2)` (`rad 5, diam 6, μ = 5, l = 5.000000`, 171 condition-4 vertices).
**POSITIVE CONTROL run first: the screen fires on `W43a` itself** — without it every `0` in
this part would have been a statement about the instrument.

**`W44a` re-verified by the STANDALONE `w133_r44_verify_W44a.py`** (distances by **bitset
relaxation**, `a(v)` by **brute-force subset enumeration**, C4-freeness by a from-scratch
nested common-neighbour count, the path checked edge by edge and non-edge by non-edge):
`rad 5`, `diam 6`, `Ctr = {346}`, `μ = 2`, `l = 4.988124`, **129** condition-4 vertices,
`⌊l(G)⌋ = 4`, target `10`, and an **`ecc(w)+3 = 9`-vertex anchored induced path BUILT**
(`0,420,163,342,361,5,19,82,71`), so `path(G) ≥ 10`. **EXIT 0, 1 496 checks.**
*(Its `l` equals its mean degree exactly: the host is triangle-free, so `a = deg` everywhere
and `(TAIL-2″)`'s degree half is vacuous on it — §46.1's own remark, live here.)*

**VERDICT ON THE PREDICTIONS: `(P1)` HELD; `(P2)` HELD.** Minimum `SLACK` over everything
found in this part: **`+2`**. **`μ ≤ 3` is NECESSARY for a hard instance and is now cheap; it
is NOT sufficient, and `W44a` does not exhibit the open case either.**

## 49.6 **The entitled numbers, and the owner errors**

> **In-class (`l(H) > 4`, `rad(H) ≥ 5`) residual-row instances: 574. Of those, instances at
> `⌊l(G)⌋ = 4` that no lane of `(ROW-3)` closes: 0. Instances anywhere with `SLACK < 0`: 0.
> That is the only CASE A number this round is entitled to.**

**OWNER ERRORS THIS ROUND — three, all caught before this entry left the file.**
1. **AN INSTRUMENT THAT MEASURED ITS OWN EARLY RETURN.** The frame-count histogram read its
   count off `tail2_at`, which **stops at the first frame that fires**. It printed **`1 frame`
   for all 601 instances** — a distribution that cannot occur — and the `SLACK` column beside
   it was the slack at the *first firing* frame, not the maximum. **Repaired by RUNNING**
   (§81): a separate `frame_scan` with no early return. **The histogram MOVED** (old peak
   `+2`, new peak `+4`) and the old numbers are quoted nowhere.
2. **A CHECK THAT COULD NOT FAIL.** PART 0's first draft contained
   `ck(c4_free(g) == (nm != "P4" or True), …)`, an assertion true by construction. Deleted
   before the first run. **Same species as round 43's probe with no positive control:** an
   instrument that cannot report a negative.
3. **A CERTIFICATE RE-CHECK THAT WOULD HAVE CRASHED INSTEAD OF CHECKING.** PART 1's first
   draft re-checked each lane certificate against a graph it never stored (`e["g"]`, absent),
   which would have raised rather than verified. Fixed before the first run by storing the
   graph and re-checking **length as well as inducedness** — which is what caught nothing this
   time and would have caught a short certificate.

**RECORD: 68 disclosed, 66 caught before leaving this file, 2 ESCAPED** (r41's `d(w,z) ≥ d−1`
in brief `E43`, r42's r39-provenance). Quote as **66–2**.

**`G62` stays free. No pocket is closed. Nothing is promoted and nothing is stated outward.**

## 49.7 Slice 2 — **THE DIRECT ATTEMPT TO BUILD THE BREAKER, AND IT FAILED FOR A REASON WORTH MORE THAN THE ATTEMPT**

*(Machine record `problems/wowii/w133_r44b_hard.py` → `.out`, **EXIT 1, 4 checks, 1 FAIL,
32.5 s** — the FAIL **is** the registered prediction `(P3)` failing and is reported as-is,
not smoothed away. System `python3` 3.9.6.)*

`(ROW-HARD)` says the breaker needs `max(a(y),deg(y)−1) ≤ 1+k₂` at **every** admissible frame.
On a **triangle-free** host `a(v) = deg(v)` exactly, so **subdivision cannot lower `a`
anywhere** (the new vertex is isolated in both end neighbourhoods) — which is why `W44a`, got
by subdivision, has `SLACK +2` — while **deleting an edge at `y` lowers `a(y)` by exactly 1.**
So the sabotage is edge deletion aimed at the highest-slack frames, screening every candidate
against every condition of the class. **Registered before the run:** *(P3)* max `SLACK` falls
strictly over the first ten accepted deletions; *(P4)* it will not reach `SLACK < 0`.

| | start | after 53 accepted deletions |
|---|---|---|
| `\|E\|`, `l` | 1 049, 4.995238 | 999, 4.7571 |
| `rad`, `diam`, `μ` | 5, 6, 4 | 5, 6, **3** |
| max `SLACK` | **+3** | **+3** |
| **firing frames / admissible frames** | **64 / 64** | **68 / 68** |

* **`(P3)` FAILED** — max `SLACK` never moved. The prediction was **badly posed**: a maximum
  over several hundred frames cannot move when one frame's `y` loses one edge.
* **`(P5)`, registered after `(P3)` failed and labelled as such** — the firing-frame count
  falls monotonically. **ALSO FAILED: it went UP (64 → 68).**
* **`(P4)` HELD.** Floor reached: `+3`.
* **The greedy is STUCK after 53 deletions: no single deletion anywhere keeps the class alive**
  (804 candidates screened and rejected).

> ⭐ **THE MECHANISM, AND IT IS THE POINT OF THE SLICE. The only lever that lowers `a` on the
> collar also ENLARGES the collar.** Deleting edges lengthens distances, which grows
> `S_{ecc(w)}(w)` and creates **more** admissible frames — so the sabotage adds frames faster
> than it disarms them. Over the whole trajectory **100 % of admissible frames fired at every
> stage** (64/64 … 68/68): not one frame ever failed to fire.

**Nothing here proves the row.** What it is: a **failed attempt with a stated mechanism**, and
the mechanism explains §49.4's measurement (`SLACK ≥ 0` on all 601 instances, minimum `+0`)
instead of leaving it as a coincidence.

---

# 50. Round 45 — **(ROW-3) STOPPED ONE RUNG SHORT, AND THE ROUND'S OWN HEADLINE TURNS OUT TO BE FORCED**

All of §50 is **OWNER-CLAIMED, PROVISIONAL, NOT ADJUDICATED**, stated in this file only.
Machine record: `problems/wowii/w133_r45_ladder.py` → `.out` (**EXIT 0, 97 checks, 0
failures, 35.4 s**, PARTS 0–6 self-registered); the **STANDALONE**
`problems/wowii/w133_r45_verify_L4.py` → `.out` (**EXIT 0, 817 checks, 0 failures**), which
shares **no code** with the builder and reads only the four edge lists and
`problems/wowii/w133_r45_L4certs.txt`; slice 2 `problems/wowii/w133_r45b_sidestep.py` →
`.out` (**EXIT 0**, and its sample collapsed — see §50.7); slice 3
`problems/wowii/w133_r45c_sidestep_wide.py` → `.out` (**EXIT 0, 52 checks, 0 failures**).
Interpreter: **system `python3` 3.9.6** (pure stdlib). No SAT, no exhaustive graph
enumeration; every path is **BUILT and then CHECKED**.

## 50.1 ⭐ **(ROW-LADDER) — the row's anchor-free leg goes one rung further than §49.2 took it**

§49.2's `(ROW-3)` feeds `(TAIL-1)` and `(TAIL-2)` into `path(G) ≥ path(H) ≥ endpath(H,v)` at a
**diametral** `v`, and stops. §45.2's own `(F11-STRAT)` already uses `(TAIL-3)` one level
below. Read as one statement, with `σ := diam(H) − rad(H)` and `k := ⌊l(G)⌋`:

> **(ROW-LADDER).** Let `(H,w)` be a residual-row instance, `G := H +` one pendant at `w`, so
> the target is `path(G) ≥ rad(G)+k = (r+1)+k`. If **`(TAIL-j)` fires at ANY ONE vertex `v`
> with `ecc_H(v) = diam(H)`**, the instance is **CLOSED** as soon as **`σ + j ≥ k`**.
> *Proof.* `(IDENT)` gives `path(G) ≥ path(H) ≥ endpath(H,v)`; `(TAIL-j)` at `v` gives
> `endpath(H,v) ≥ ecc(v)+1+j = r+σ+1+j ≥ r+1+k`. ∎ **No anchor, no hair, no F11, no `l>4`,
> no `rad ≥ 5`** — only C4-freeness and `μ(H) ≥ 2`.

At `k = 4`: `σ ≥ +4 → j = 0`; `σ = +3 → j = 1`; `σ = +2 → j = 2`; and **`σ = +1 → j = 3`,
i.e. `(TAIL-3″)` at ANY ONE non-central vertex.** §49.2's sentence *"offset `+1` is the only
lane that still needs the prescribed anchor"* is **WRONG as a statement about the ladder**;
it is true only about the ladder truncated at `j = 2`. **That is my own error from round 44
and it is the first line of this section.**

**MEASURED over 730 residual-row instances** (round 44's 601 population plus `W44a`, which
carries 129 condition-4 vertices of its own), from an independently written classifier:
round 44's numbers are **reproduced exactly** — `L0 12`, `L1 122`, `L2 306`, offsets
`+2:336 +3:122 +4:12` — and offset `+1` grows from 131 to **260** by the addition of `W44a`.

| CASE A (offset +1, `k=4`), 260 instances | L4 fires | L4 does not |
|---|---|---|
| **L3 fires** | **260** | 0 |
| L3 does not | 0 | 0 |

**L4 closes all 260 CASE A instances with no anchor at all**, and **2 016** certificates were
re-checked from scratch: **0 not induced, 0 too short**. **AGAINST THE HEADLINE, PRINTED
BESIDE IT: those 260 instances come from only FOUR distinct hosts** (`W43a`/`b`/`c`, `W44a`);
offsets `+2/+3/+4` come from 23/40/7 hosts. **260 instances are not 260 tests.**

## 50.2 **(TAIL-4″) — one more rung, and the index the naive generalisation loses**

> **(TAIL-4″).** In `(TAIL-3″)`'s frame, with `t ∈ N(z)` and `u₀…u_d y z t` induced and
> anchored at `v`, put `k₄ := #{ j ∈ {d, d−1, d−2, d−3, d−4, d−5} : N(t) ∩ N(u_j) ≠ ∅ }`.
> Then `endpath(H,v) ≥ ecc(v)+5` as soon as **`max(a(t), deg(t)−1) ≥ 2 + k₄`**.
> *Proof.* For `s ∈ N(t)`: **(a)** `z` plus the at most one common neighbour of `z,t`
> (C4-freeness) — 2 vertices, both in `z`'s matching component of `G[N(t)]`; **(b)** `s ≁ y`
> excludes `N(t)∩N(y)`, which **is** `{z}` (because `z ~ y` and `z ~ t`, and C4-freeness makes
> it unique) — **free**; **(c)** each `j` contributes at most one vertex, and `s ~ u_j` forces
> `d(t,u_j) ≤ 2 ⟹ j ≥ d−5`; **(d)** `i ≤ d−6` free by distance. So at most `2+k₄` vertices,
> meeting at most `1+k₄` components. ∎ Blanket form `a(t) ≥ 8`; and `μ(H) ≥ 8` gives
> `endpath(H,v) ≥ ecc(v)+5` at every `v`.

> ⚠️ **THE ONE PLACE THIS IS NOT A COPY OF `(TAIL-3″)`.** `(TAIL-3″)` gets index `d` for
> **free** because `N(z) ∩ N(u_d) = {y}`. At step 4 that argument **dies**: `t ≁ y`, so `y`
> is not a common neighbour of `t` and `u_d`, and `N(t) ∩ N(u_d)` can be an arbitrary vertex.

**GUARD (D12) DROP-`u_d`** — the naive step-4 dodge list `{d−1..d−4}`. One-sided by the proof
(`k₄ᵍ ≤ k₄`), so **MISSES must be 0**. Over **4 846** step-4 frames on ten hosts, **680** of
which actually distinguish the two lists (`PG(2,q)` is bipartite, so `N(t)∩N(u_d) = ∅` at
**every** step-4 frame there and the guard would have been **vacuous** on incidence hosts
alone — the seeded dense C4-free hosts are in the sample for exactly that reason, and each is
**asserted** C4-free rather than assumed):

| | claims | extension BUILT | **FALSIFIED** |
|---|---|---|---|
| `(TAIL-4″)` **correct** | 3 934 | 3 934 | **0** |
| **(D12) naive** | 4 230 | 4 178 | **52** |

**MISSES 0. The naive form is FALSE and 52 frames exhibit it.**

**THE 30 `BEYOND-k≥5` ROWS (round 44's owed item 2) ARE CLOSED.** All 30 sit at offset `+2`
with `k = 5`, so `(ROW-LADDER)` needs rung `j = 3`, not `j = 4`: **30 of 30 closed,
certificates BUILT and re-checked, 0 bad. `(TAIL-4″)` was not needed for them** — it is
stated because the ladder is stated, and it is the rung offset `+1` at `k = 5` would need.

## 50.3 ⭐⭐ **(ROW-K) — AND IT RETRACTS THE EVIDENTIAL VALUE OF §50.1's OWN 260/260**

The planner's standing question, asked of **this** round's headline before it is quoted:

> **At the frame each L4 certificate fired on: `k₃ ∈ {0:132, 1:128}` and `a(z) = 5` at all
> 260. `μ(H) ≥ 2 + k₃(z)` at ALL 260. THE 260/260 COULD NOT HAVE FAILED AT THOSE FRAMES.**

That is the **same species** as `(ROW-MU4)`'s retraction of round 43's `129/129`, one round
later, in my own round. **What survives:** the certificates are BUILT paths; **L4 does close
all 260 CASE A instances anchor-free, and that claim stands.** **What dies:** any reading of
`260/260` as evidence that the **lane discriminates**. The forcing is a theorem:

> **(ROW-K).** `H` C4-free, `μ := μ(H) ≥ 2`. Since `a(·) ≥ μ` everywhere, `(TAIL-2″)` fires at
> any frame with `k₂(y) ≤ μ−2` and `(TAIL-3″)` fires at any step-3 frame with `k₃(z) ≤ μ−2`.
> **Hence an instance that is still open has `k₂(y) ≥ μ−1` at EVERY frame from `w` and
> `k₃(z) ≥ μ−1` at EVERY step-3 frame of EVERY vertex with `ecc = diam`.** With `k₂ ≤ 2` this
> forces `μ ≤ 3` (**that is round 44's `(ROW-MU4)` read backwards**) and with `k₃ ≤ 4`,
> `μ ≤ 5`. ∎

**So the open case is not "a low-`a` collar": it is "every step-3 vertex of every frame of
every diametral vertex HUGS THE GEODESIC"** — `N(z)` must meet `N(u_j)` for at least `μ−1` of
the four indices `j ∈ {d−1,…,d−4}`. **Measured `k₃` over 211 341 step-3 frames with no early
return: `0:145 535  1:60 023  2:5 655  3:128  4:0`.** An open instance must have **zero**
`k₃ = 0` frames, and 68.9 % of the frames measured are `k₃ = 0`.

**AND THE SAME AUDIT APPLIES TO L3.** `k₂min` at `w` is **0 on all 260** CASE A instances, so
`(TAIL-2″)` at `w` also fired for a reason `μ ≥ 2` alone forces. Closed-by, each instance
counted once: **`(ROW-MU4)` `μ ≥ 4`: 131; `(ROW-K)` step-2 `k₂min ≤ μ−2`: 129; `(ROW-K)`
step-3: 0; BUILT PATH ONLY: 0.** **Every CASE A instance this line holds closes by a theorem
whose hypothesis is checkable in `O(frames)` — and not one of them tests either lane.**

**LIVENESS, so that no `0` above is a statement about the instrument.** POSITIVE control:
`PG(2,5)` has `a ≡ 6`, so `(F11-DEG)` forces the step-3 chain — it fires at **62/62**.
NEGATIVE control: on `C₆`, `Θ(3,3,3)` and `Petersen` — the hosts §45.4 records as falsifying
`(F11-ALL)` — the same builder fires at **0/6, 0/8, 0/10**, with `exact path` 5, 6, 5 by
complete search. **The detector demonstrably declines.**

## 50.4 **(ROW-HARD′) — the open case is a CONJUNCTION**

> **(ROW-HARD′).** An unclosed offset-`+1`, `k=4` row instance has **(i)** round 44's
> `max(a(y),deg(y)−1) ≤ 1+k₂(y) ≤ 3` at every frame from `w`, **AND (ii)**
> `max(a(z),deg(z)−1) ≤ 1+k₃(z) ≤ 5` at every step-3 frame of **every** non-central vertex.
> ∎ (contrapositives of `(TAIL-2″)`+hair and of `(ROW-LADDER)` at `j = 3`)

At offset `+1` every non-central vertex is diametral, so **(ii) constrains the second
neighbourhood of BOTH ends of EVERY diametral pair**, not just `w`'s own far ends.
`SLACK3 := max over sampled step-3 frames of [max(a(z),deg(z)−1) − (2+k₃)]`. **DIRECTION OF
ERROR FIXED BEFORE THE NUMBER (§129): frames sampled ⟹ printed `SLACK3` is a LOWER bound, so
`≥ 0` is SOUND and `< 0` would be INCONCLUSIVE.** Over 730 instances:
`ALL +2:4  +3:365  +4:331  +6:30`; **CASE A `+3:260`**; minimum anywhere `+2`
(`NLsa(8,s1)`, n=160, offset +4); minimum in CASE A `+3` (`W43a`); **`SLACK3 < 0`: 0.**

## 50.5 **(ROW-CT) — summing (ii) against `⌊l(G)⌋ = 4` turns the collar into a GLOBAL BUDGET**

> **(ROW-CT).** With `B₄ := { z : z is the step-3 vertex of an admissible frame from some `v`
> with `ecc(v) = diam(H)`, at a frame where `k₃(z) ≤ 3` }`: if the instance is not closed by
> `(ROW-LADDER)` at `j = 3` then `a_H(z) ≤ 1+k₃(z) ≤ 4` on `B₄`, hence
> **`EXCESS(H) := Σ_{v ∉ B₄} max(a_H(v)−4, 0) ≥ 2`. Equivalently `EXCESS ≤ 1 ⟹ CLOSED`.**
> *Proof.* `⌊l(G)⌋ = 4 ⟹ Σ_{V(G)}(a_G−4) ≥ 0`; the pendant contributes `−3` and `a_G(w) =
> a_H(w)+1`, so `Σ_{V(H)}(a_H−4) ≥ 2`. On `B₄` the summand is `≤ 0`, so dropping `B₄` only
> increases the sum, and taking positive parts increases it again. ∎

**DIRECTION OF ERROR FIXED FIRST:** `B₄` is computed from **sampled** frames, so the computed
`B₄` is a **subset** of the true one and the computed `EXCESS` is an **UPPER** bound —
therefore **`EXCESS ≤ 1 ⟹ CLOSED` is SOUND**, and a computed `EXCESS ≥ 2` is **INCONCLUSIVE
and may never be quoted as evidence of openness.**

| host | `n` | `Σ(a−4)` | `\|B₄\|` | `\|B₄\|/n` | `EXCESS` |
|---|---|---|---|---|---|
| `W43a` | 420 | 418 | 241 | 57.4 % | 178 |
| `W43b` | 420 | 418 | 248 | 59.0 % | 172 |
| `W43c` | 420 | 420 | 231 | 55.0 % | 189 |
| `W44a` | 421 | 416 | 246 | 58.4 % | 174 |

**READ AGAINST ITS OWN INTEREST: `(ROW-CT)` CLOSES 0 of 260 here.** These hosts are
triangle-free, so `a = deg` and the `l`-budget is hundreds of units. What `(ROW-CT)` buys is
**not a closure but a change of coordinate**: round 44 left the question as *build a low-`a`
collar*, and §49.7 showed the only lever that lowers `a` on the collar enlarges the collar.
`(ROW-CT)` says the same object must **also hide every unit of its `l`-excess from the step-3
reach of every diametral vertex.**

## 50.6 ⭐ **(TAIL-2S) — the open case's own obligation is a CONSTRUCTION**

`(ROW-HARD)`/`(ROW-K)` say an open instance must supply `k₂(y) ≥ 1` at **every** frame, i.e. a
witness `p ∈ N(y) ∩ N(u_{d−2})` (or the `u_{d−3}` one). That is stated as an obstruction. It
is also a **hypothesis**, and it is exactly what a different construction needs.

> **(TAIL-2S) — the SIDESTEP.** `H` C4-free, `μ(H) ≥ 2`, `u₀…u_d` a geodesic from `w = u₀` to
> a far end, `d = ecc(w) ≥ 3`, `y ∈ N(u_d)` admissible for `(TAIL-1)`. If there is
> `p ∈ N(y) ∩ N(u_{d−2})` with **`p ≁ u_{d−3}`**, and **`a(u_d) ≥ 3`**, then
> `endpath(H,w) ≥ ecc(w)+3`.
> *Proof.* `Q := u₀ … u_{d−2}, p, y, u_d` has `d+2` vertices and is induced: `p ≠ u_i` for
> every `i` (`p ~ u_{d−2}`; `p ≠ u_{d−3}` because `p ~ y` and `y ≁ u_{d−3}`); `p ≁ u_{d−4}`
> (else `u_{d−4},u_{d−2}` have the two common neighbours `u_{d−3}` and `p`) and `p ≁ u_i`,
> `i < d−4`, by distance; `p ≁ u_{d−3}` is the hypothesis; `p ≁ u_d` (else `u_{d−2},u_d` have
> the two common neighbours `u_{d−1}` and `p`, and `p ≠ u_{d−1}` because `p ~ y ≁ u_{d−1}`);
> `y ≁ u_i` for `i ≤ d−2` by `(TAIL-1)`. Extend by `y' ∈ N(u_d)`: the only exclusions are
> `N(u_d)∩N(u_{d−2}) = {u_{d−1}}` and `y`'s own matching component (`N(u_d)∩N(p) = {y}`), and
> those are **two distinct** components because `y` is off `u_{d−1}`'s. So `a(u_d) ≥ 3`
> leaves one. ∎

**`(TAIL-2″)` pays for the dodge list at `y`; `(TAIL-2S)` pays nothing at `y` at all — it
SPENDS the very witness the open case is obliged to provide.** The two are aimed at opposite
regimes.

> **(ROW-HARD‴).** An open offset-`+1`, `k=4` instance has, at every far end `u_d` of `w` and
> every admissible frame: `max(a(y),deg(y)−1) ≤ 1+k₂(y)` **and** `k₂(y) ≥ 1` **and** — new —
> **either `a(u_d) = 2` exactly, or every witness `p ∈ N(y)∩N(u_{d−2})` has `p ~ u_{d−3}`.**

**Slice 3, 59 hosts, 44 153 `(TAIL-2S)` frames.** `(P3)` **HELD: the construction claims
41 523 frames and BUILDS the `ecc(w)+3` path on 41 523 — 0 failures to build.**
**GUARD (D13) DROP-`p`-CONDITION** (the `p ≁ u_{d−3}` clause removed): claims 49 408, builds
41 523, **FALSIFIED on 7 885 frames** — the clause is decisively load-bearing (**`(P4)`
HELD**). `a(u_d)` over the frames: `2:2 630  3:13 001  4:18 441  5:8 990  6:1 027  7:64`.

**AND, AGAINST ITS OWN INTEREST, `(TAIL-2S)` IS THE FIRST LANE ON THIS LINE THAT DOES NOT
CLOSE EVERYTHING: it closes 208 of the 260 CASE A instances** (`W43a` 102/128, `W43b` 1/1,
`W43c` 1/2, `W44a` 104/129). Of the **52** it does not close, **52 (100 %) have a far end with
`a(u_d) ≥ 3`**, so the binding sub-condition is the **missing witness `p`**, not `a(u_d) = 2`
(**`(P5)` HELD**). **Every CASE A instance has some far end with `a(u_d) ≥ 3`**, so the
`a(u_d) = 2` half of `(ROW-HARD‴)` is violated everywhere on this family.

## 50.7 The entitled numbers, the owner errors, and what is NOT closed

> **ENTITLED. Residual-row instances 730 (601 of round 44's + 129 from `W44a`), from 74
> distinct hosts (offsets +1/+2/+3/+4 carried by 4/23/40/7 hosts); CASE A instances 260, from FOUR hosts. At `⌊l(G)⌋ = 4` closed by no lane of
> `(ROW-LADDER)`: 0. `BEYOND-k≥5` rows not closed: 0. Instances with `SLACK3 < 0`: 0.
> CASE A instances closed by `(TAIL-2S)`: 208 of 260. CASE A instances whose L3 or L4 firing
> was NOT forced by `μ` and the frame's `k`: 0.** That last number is the honest one.

**OWNER ERRORS THIS ROUND — three, all caught before this entry left the file.**
1. **A HOST BUILDER RETYPED INSTEAD OF COPIED.** Slice 2's `rand_c4free_dense` was written
   from memory rather than copied verbatim and does **not** produce C4-free graphs; its own
   `c4_free` screen threw all five hosts away, collapsing the sample to **4 hosts / 19
   frames**, on which `(P1)` was recorded FAILED — a verdict 19 frames cannot support.
   **Repaired by RUNNING (§81):** slice 3 uses the verbatim builder, 59 hosts, 44 153 frames,
   and the re-registered `(P4)` **HELD**. Slice 2's file and `.out` are kept as the record.
2. **A GUARD THAT DID NOT ASSERT ITS OWN HYPOTHESIS.** `(D12)`'s host loop screened `μ ≥ 2`
   but never asserted C4-freeness, on which every step of `(TAIL-4″)` depends. Added as an
   explicit `ck` before the first quoted run; all ten hosts pass. *Same species as error 1,
   found by it.*
3. **A NARRATION THAT CONTRADICTED THE NUMBER BELOW IT.** Slice 3's `(P2)` line printed
   "so `(TAIL-2S)` closes all of them" three lines above the count showing it closes 208 of
   260. Corrected and re-run before the figures were quoted anywhere.

**RECORD: 71 disclosed, 69 caught before leaving this file, 2 ESCAPED. Quote as 69–2.**

**WHAT IS NOT CLOSED.** There is still **no theorem** saying a CASE A instance must satisfy
any of `(ROW-MU4)`, `(ROW-K)`, `(ROW-CT)` or `(TAIL-2S)`'s hypotheses. **CASE A is not
closed.** `G62` stays free. **Nothing is promoted and nothing is stated outward.**

---

# §51 — THE ONE INTEGER, ANSWERED: THE FRAME SET WITH NO `k₃ = 0` **EXISTS**, AND IT IS THE WRONG INTEGER (round 46)

Machine record: `problems/wowii/w133_r46_hug.py` → `.out` (**EXIT 0, 151 checks, 0 failures,
14.4 s**, PARTS 0–5 self-registered); **STANDALONE** `problems/wowii/w133_r46_verify.py` →
`.out` (**EXIT 0, 131 checks, 0 failures**), which shares **no code** with the builder
(Floyd–Warshall distance matrix instead of BFS, neighbourhoods as bitmasks instead of sets,
`a(v)` as a **true** maximum independent set by recursive search instead of the
`deg − #edges` matching bound, geodesics enumerated FORWARD instead of backward) and reads
only the W44a edge list plus `problems/wowii/w133_r46_nofire.txt`; SLICE 2
`problems/wowii/w133_r46b_budget.py` → `.out` (**EXIT 0, 69 checks, 0 failures, 5.8 s**).
System `python3` 3.9.6,
pure stdlib. No SAT, no exhaustive search over a large space. Primitives and host builders
COPIED VERBATIM from `w133_r45_ladder.py`.

## 51.1 **(HUG-CYC) — every index of `k₃` is a CYCLE OF A PRESCRIBED LENGTH**

> **(HUG-CYC).** `H` C4-free, `v` with `ecc(v) = diam(H)`, `u₀…u_d` a geodesic from `v`,
> `y ∈ N(u_d)` admissible for `(TAIL-1)`, `z` a step-3 vertex. If index
> `j ∈ {d−1,…,d−4}` of `k₃(z)` fires with witness `c ∈ N(z)∩N(u_j)`, then
> `z, c, u_j, u_{j+1}, …, u_d, y` is a **cycle on exactly `(d−j)+4` vertices**. Hence
> `girth(H) ≤ (d−j)+4`.
> *Proof.* Distinctness: `u_j…u_d` distinct on a geodesic; `y ≠ u_i` and `y ≁ u_i` for
> `i ≤ d−1` by admissibility; `z` off the path and off its neighbourhood by inducedness and
> `z ≠ y`; `c` is no path vertex (`c ~ z` while `z ≁ u_i` for every `i`) and `c ≠ y`
> (`c ~ u_j` with `j ≤ d−1`, and `y ≁ u_i` for `i ≤ d−1`). Consecutive pairs are edges. ∎

**Corollaries, immediately.** Index `d−1` needs a **C5**, `d−2` a **C6**, `d−3` a **C7**,
`d−4` a **C8**. Hence

* **`girth ≥ 9 ⟹ k₃ ≡ 0` at every step-3 frame** — the design target is **IMPOSSIBLE above
  girth 8**, and with `a(·) ≥ μ ≥ 2 = 2+0` every such instance is CLOSED outright;
* `girth ≥ 8 ⟹ k₃ ≤ 1`; `girth ≥ 7 ⟹ k₃ ≤ 2`;
* **`H` bipartite kills the two ODD indices** `d−1` and `d−3`, so `k₃ ≤ 2`; bipartite with
  `diam = 3` leaves only `d−2`, so `k₃ ≤ 1`.

> **(ROW-GIRTH).** Read against `(ROW-K)` (`open ⟹ k₃ ≥ μ−1` at every step-3 frame):
> `μ = 2 ⟹ girth(H) ≤ 8`; `μ = 3 ⟹ girth ≤ 7`; `μ = 4 ⟹ girth ≤ 6`; `μ = 5 ⟹ girth ≤ 5`
> **and every step-3 frame lies simultaneously on a C5, a C6, a C7 and a C8**. `H`
> bipartite ⟹ `μ ≤ 3`; bipartite with `diam = 3` ⟹ `μ ≤ 2`.

**VERIFIED, not asserted.** Over **21 769** step-3 frames on 68 hosts, **26 219** firing
indices were made to EXHIBIT their cycle and each was re-checked for distinctness, adjacency
and length: `C5:6 597  C6:9 345  C7:9 101  C8:1 176`, **0 bad lengths, 0 non-cycles, 0
cycles shorter than their host's girth, 0 odd cycles on a bipartite host.**

**AGAINST ITS OWN INTEREST: `(HUG-CYC)` CLOSES NOTHING.** It forbids a *family* — girth ≥ 9
— and it is **silent at girth 5**, which is exactly where all four CASE A hosts live. It is
a constraint on the DESIGN, and it is reported as that and not as a closure.

## 51.2 ⭐ **(HUG-DEG)/(HUG-EQ) — the witnesses are DISTINCT, so round 45's inequality is an EQUALITY**

> **(HUG-DEG).** With `J(z)` the firing set and `c_j ∈ N(z)∩N(u_j)`: **no `c_j` is `y`**
> (`y ≁ u_i` for `i ≤ d−1`), and `c_j = c_{j'}` with `j' − j = 2` would make `c` and
> `u_{j+1}` two common neighbours of `u_j, u_{j+2}` — a **C4**; `j' − j ≥ 3` contradicts
> `d(u_j,u_{j'}) ≥ 3`. The remaining case `j' = j+1` makes `{u_j,u_{j+1},c}` a **triangle**,
> which C4-freeness does **not** forbid. **So on a triangle-free host all the `c_j` are
> distinct and `deg(z) ≥ k₃(z) + 1`.** ∎

> **(HUG-EQ).** `(TAIL-3″)` NOT firing means `max(a(z), deg(z)−1) ≤ 1 + k₃(z)`; on a
> triangle-free host `a(z) = deg(z)`, so that is `deg(z) ≤ k₃(z)+1`. With `(HUG-DEG)`:
> **at every step-3 frame of a still-open triangle-free row instance,
> `deg(z) = k₃(z) + 1` EXACTLY, i.e. `N(z) = {y} ∪ {c_j : j ∈ J(z)}` — `z` has NO neighbour
> that is not `y` or a hug-witness.** In particular `k₃(z)` is the SAME at every frame in
> which `z` is the step-3 vertex, namely `deg(z)−1`, and `deg(z) ≤ 5`. ∎

That converts round 45's **inequality** `a(z) ≤ 1+k₃` into an **equality**, and it is what
makes the design target checkable one vertex at a time. **MEASURED:** `deg(z) − (k₃(z)+1)`
over 9 739 triangle-free step-3 frames: `+0:295  +1:1 646  +2:2 341  +3:1 651  +4:3 346
+5:460` — **0 frames below 0**, i.e. `(P3)` HELD, and only **295 (3.0 %)** sit at the
equality the open case requires. **On hosts WITH triangles, frames whose witnesses are NOT
distinct: 0 of 12 030** — printed because it is precisely the case the proof does not cover,
not because it was assumed away.

## 51.3 ⭐⭐ **THE ONE INTEGER, MEASURED EXHAUSTIVELY — AND IT IS THE WRONG INTEGER**

Three numbers per host, over **every** step-3 frame of **every** vertex with `ecc = diam`,
over **every** geodesic, with **no cap and no early return**:

* `F(H)` := the population of step-3 frames;
* `Z(H)` := how many have `k₃ = 0` — **the planner's integer**;
* `N(H)` := how many `(TAIL-3″)` actually **FIRES** at — **the real integer**, because
  `k₃ = 0 ⟹ fires` (`a(z) ≥ μ ≥ 2 = 2+0`) and by `(ROW-LADDER)` at `j = 3` **one** firing
  frame at **one** diametral vertex CLOSES an offset-`+1` instance.

**`F(H) > 0` is not decoration**: a host with no step-3 frame at all has `Z = N = 0` for the
empty reason. `C₅` and `C₆` are exactly that and are reported separately (**item (a)**).

> **ANSWER (i) — THE STRUCTURE IS NOT FORBIDDEN.** **7 hosts of 68 have `F(H) > 0` and
> `Z(H) = 0`, exhaustively**: `Petersen` (F=120, all `k₃=2`), `Heawood = PG(2,2)` (F=336),
> `PG(2,3)` (F=5 616), `PG(2,5)` (F=186 000), `C₇` (F=14), `C₈` (F=16),
> `Möbius–Kantor` (F=288). **A frame set with no `k₃ = 0` EXISTS.** The `girth ≥ 9`
> corollary of §51.1 is the only thing that forbids one, and it forbids a family.

> **ANSWER (ii) — AND `Z` IS THE WRONG INTEGER.** Only **3 of those 7** have `N(H) = 0`:
> **`Petersen`, `C₇`, `C₈`**. The four incidence/`Möbius–Kantor` exhibits avoid `k₃ = 0` for
> a reason — every two points of a projective plane are collinear — that **also** forces
> `μ = q+1 ≥ 3 > 1 + k₃`, so `(ROW-K)` re-closes them at **every** frame. **That is item (a)
> applied to my own exhibit: the exhibit is real and it does not test the lane.**

> **ANSWER (iii) — AND ALL THREE SURVIVORS FAIL ON `l`.** `Petersen` `l = 3`, `C₇` `l = 2`,
> `C₈` `l = 2`. **The row needs `⌊l(G)⌋ = 4`.** All three satisfy `(HUG-EQ)` at the
> equality (`deg = 3 = k₃+1` on Petersen, `deg = 2 = k₃+1` on `C₇`/`C₈`) — which is exactly
> why their `l` is small: `(HUG-EQ)` pins every step-3 vertex to degree `k₃+1 ≤ 5`, and
> `⌊l⌋ = 4` needs an average `a` of at least 4.

**`FIRE-GAP(H) := F(H) − N(H)`** — the frames an open instance is ALLOWED to have; the
design target is `FIRE-GAP = F`. Over the 68 hosts the best non-trivial gaps are
`Petersen/C₇/C₈ 100 %`, `Möbius–Kantor 66.7 %`, then the small random hosts at 40–49 % — and
**restricted to the hosts with `⌊l⌋ = 4`, which is what the row needs, the best is
`RD(307,40)` at 7.089 % (1 227 of 17 308), then 3.284 %, 2.822 %, 2.114 %, 1.636 %,
1.524 %.** **Nothing with the row's `l` gets past 8 %, and the target is 100 %.**

**THE FOUR CASE A HOSTS, EXHAUSTIVELY (round 45's 68.9 % was a SAMPLE over a MIXED
population; this is CASE-A-only and complete):**

| host | `n` | `F` | `Z` | `Z/F` | `N` | `FIRE-GAP` |
|---|---|---|---|---|---|---|
| `W43a` | 420 | 477 275 | 428 261 | 89.7 % | 477 275 | **0** |
| `W43b` | 420 | 385 685 | 347 825 | 90.2 % | 385 685 | **0** |
| `W43c` | 420 | 421 890 | 379 570 | 90.0 % | 421 890 | **0** |
| `W44a` | 421 | 490 540 | 440 434 | 89.8 % | 490 529 | **11** |

**1 775 390 frames; `k₃ = 0` on 89.9 % of them; `(TAIL-3″)` fires on all but ELEVEN.**

## 51.4 ⭐ **THE ELEVEN — the first CASE A frames on this line that an open instance is allowed to have**

`W44a` has **11** step-3 frames at which `(TAIL-3″)` does **not** fire, and **all 11 have the
same step-3 vertex: vertex 420, `W44a`'s single planted degree-2 vertex, at `k₃ = 1`.**
`deg(z) = 2 = k₃(z)+1` — `(HUG-EQ)` at the equality, exactly as predicted, on the one vertex
of the whole CASE A population that can sit there. They are written to
`problems/wowii/w133_r46_nofire.txt` and **re-verified STANDALONE**: each is a genuine
geodesic from a vertex with `ecc = diam`, the frame is an induced anchored path, and
`(TAIL-3″)` does not fire **when `a(z)` is recomputed as a TRUE maximum independent set
rather than by the matching bound** (131 checks, 0 failures).

**WHAT THAT DOES AND DOES NOT SAY.** It does **not** open `W44a`: `(ROW-LADDER)` needs one
firing frame at one diametral vertex, and `W44a` has 490 529 of them. What it says is that
the open condition is **attainable at a frame** on a host this line actually holds, and that
**the only way to attain it is `(HUG-EQ)`'s equality** — so a CASE A counterexample must be
built out of vertices like 420, and out of nothing else, at every step-3 position of every
diametral vertex, while keeping `⌊l⌋ = 4`.

## 51.5 ⭐ **(TAIL-2S′) — the `j = d−3` sidestep, and the 52 residuals fall to 15**

> **(TAIL-2S′).** `H` C4-free, `u₀…u_d` a geodesic from `w = u₀` to a far end,
> `d = ecc(w) ≥ 3`, `y ∈ N(u_d)` admissible for `(TAIL-1)`. Suppose `q ∈ N(y) ∩ N(u_{d−3})`
> with **`q ≁ u_{d−4}`** (vacuous at `d = 3`; automatic when `H` is triangle-free, since
> `q ~ u_{d−4}` and `q ~ u_{d−3}` is a triangle on a geodesic edge). Then
> `R := u₀, …, u_{d−3}, q, y, u_d, u_{d−1}` is an induced path on `d+2` vertices anchored at
> `w`. If `N(u_{d−1})` has a vertex outside
> `{u_d, u_{d−2}} ∪ (N(q)∩N(u_{d−1})) ∪ (N(u_d)∩N(u_{d−1}))` — at most three vertices, each
> of the last two sets a singleton by C4-freeness — then `endpath(H,w) ≥ ecc(w)+3`.
> *Proof.* `q ≠ u_i` for `i ≤ d−1` because `q ~ y` and `y ≁ u_i`; `q ≠ u_d` because
> `d(u_{d−3},u_d) = 3`. `q ≁ u_i` for `i ≤ d−5` is C4-freeness (`i = d−5` gives `q,u_{d−4}`
> two common neighbours of `u_{d−5},u_{d−3}`) or distance; `q ≁ u_{d−1}` is C4-freeness
> (`q,u_{d−2}` two common neighbours of `u_{d−3},u_{d−1}`); `q ≁ u_d` is the geodesic. `y`
> and `u_d` and `u_{d−1}` are handled by admissibility and the geodesic. **`u_{d−2}` is not
> on `R` at all**, so `q ~ u_{d−2}` costs nothing. For the extension `s`: `s ≁ u_{d−3}` and
> `s ≁ y` are C4-freeness, `s ≁ u_i` for `i ≤ d−4` is distance, and `u_{d−2}` is excluded
> because it is adjacent to `u_{d−3} ∈ R`. ∎

**IT SKIPS `u_{d−2}` AND HANGS `u_{d−1}` ON THE FAR END.** That is the whole trick, and it
is what makes it a different lane: `(TAIL-2S)` pays at `u_d` and spends the `d−2` witness;
`(TAIL-2S′)` pays at `u_{d−1}` and spends the `d−3` witness — and `(ROW-K)` says at least
one of the two witnesses EXISTS at every frame.

**VERIFIED BY CONSTRUCTION, on 28 892 frames over 57 hosts from 4 independent sources:
claims 28 738, BUILDS 28 738, 0 failures to build; 0 prefixes `R` that the proof calls
induced and are not; 0 candidates `s` outside the exclusion set that fail to extend**
(`(P5)` HELD — and the loop tries the proof's OWN candidate set, not any `s` that happens to
work). **GUARD (D15) DROP-`q ≁ u_{d−4}`: claims 28 738, builds 28 738, FALSIFIED 0 —
`(P6)` FAILED.** I predicted the clause would be shown load-bearing and it was not: no
scanned frame ever had `q ~ u_{d−4}`. **The clause is needed by the proof and is NOT shown
necessary by this sample, and that is printed instead of a claim.**

**ON THE 260 CASE A INSTANCES** (geodesics/far ends SAMPLED, so `CLOSES` is SOUND and
`does not close` is INCONCLUSIVE):

| | `W43a` | `W43b` | `W43c` | `W44a` | total |
|---|---|---|---|---|---|
| `(TAIL-2S)` closes | 102 | 1 | 1 | 104 | **208** — round 45's number, reproduced exactly |
| `(TAIL-2S′)` closes | 94 | 1 | 2 | 96 | **193** |
| both | 76 | 1 | 1 | 78 | **156** |

**Neither lane contains the other**: `(TAIL-2S′)` closes **37** instances `(TAIL-2S)` misses
and misses **52** that it closes. **The union leaves 15 — down from 52.** Over the frames of
the `(TAIL-2S)` residuals, `k₂(y)` is `0` on 2 378 and `1` on 52, so on almost all of them
the `d−2` witness is simply absent and `(TAIL-2″)` fires at `w` anyway.

## 51.6 ⭐⭐ **(ROW-BUDGET) — THE WITNESSES HAVE TO FIT, AND THIS IS THE FIRST LANE THAT CLOSES NOTHING ON MOST HOSTS**
> ⛔ **RETRACTED AS A LANE BY ROUND 47 (`(BUDGET-SUB)`), 2026-08-23.** On a TRIANGLE-FREE host — the only population where this section's proof is valid, since it needs `(HUG-DEG)` — `a(z) = deg(z)` exactly, so `(ROW-BUDGET)` fires ONLY where `(TAIL-3″)` already fires: **0 BUDGET-only frames over 581 441 frames on 38 hosts, containment STRICT.** The sentence *"it closes a frame at which no single vertex looks closable"* below is **FALSE** — the proof exhibits the single vertex — and `(P3)`'s Petersen/C₇/C₈ control was **FORCED**, not a soundness test. Everything below is kept as the record; see `orchestration/results/w133_state.md` Round 47 §1.


Machine record: `problems/wowii/w133_r46b_budget.py` → `.out` (**EXIT 0, 69 checks, 0
failures, 5.8 s**). Every host in it is **asserted** connected, C4-free **and triangle-free**
— the last is `(ROW-BUDGET)`'s own hypothesis — before the hypothesis is used.

`(HUG-DEG)` says the witnesses of ONE step-3 vertex are distinct. C4-freeness says more:

> **(ROW-BUDGET).** `H` C4-free and triangle-free, `(v, P = u₀…u_d, y)` a `(TAIL-1)` frame at
> a vertex with `ecc(v) = diam(H)`, `Z(y)` the admissible step-3 vertices, and
> `B := (N(u_{d−1}) ∪ N(u_{d−2}) ∪ N(u_{d−3}) ∪ N(u_{d−4})) \ P` **the budget**. Then
> **`Σ_{z ∈ Z(y)} k₃(z) ≤ |B|`.** Consequently
> **`Σ_{z ∈ Z(y)} (deg(z) − 1) > |B| ⟹ some z ∈ Z(y) FIRES`**, and by `(ROW-LADDER)` at
> `j = 3` the offset-`+1` instance is **CLOSED**.
> *Proof.* If distinct `z, z' ∈ Z(y)` shared a witness `c`, then `c` and `y` would have the
> two common neighbours `z, z'` — a **C4**. Within one `z` the witnesses are distinct by
> `(HUG-DEG)`. Every witness is adjacent to some `u_j`, `j ∈ {d−1,…,d−4}`, and is not a path
> vertex (`c ~ z` while `z ≁ u_i` for every `i`), so the whole collection **injects into
> `B`**. For the consequence: if every `z` had `deg(z) ≤ 1+k₃(z)` then
> `Σ(deg(z)−1) ≤ Σ k₃(z) ≤ |B|`. ∎

**This is the first test on this line that is a COUNT, not a per-vertex condition** — it can
close a frame at which **no single vertex** looks closable, because it is the *sum* that
overflows.

`(P1)` **HELD**: `Σ k₃ ≤ |B|`, witnesses pairwise distinct and inside `B`, **0 violations**
over **507 899** frames. `(P2)` **HELD**: every frame the test closes really does carry an
explicitly firing `z`, **0 failures**. `(P3)` **HELD**, and it is the one that could have
embarrassed the lane: **the test fires at NO frame of `Petersen`, `C₇` or `C₈`** — the three
hosts §51.3 showed have `N(H) = 0`. Had it fired there it would have been unsound.

**WHAT IT FAILS TO CLOSE — the headline, in the sound direction (item (b)).**
**It closes 473 277 of 507 899 frames (93.2 %) and closes NOTHING AT ALL on 14 of the 22
hosts**: `Petersen, C₇, C₈, C₉, PG(2,2), PG(2,3), Desargues, Pappus, Coxeter,
Möbius–Kantor, Nauru, Dodecahedron, GP(11,3), GP(13,5)`. **It is not a superset of any other
lane and no other lane is a superset of it**: `C₉` has girth 9, so `(ROW-K)` closes it at
every frame while `(ROW-BUDGET)` closes none of it; `PG(2,5)` is closed by both;
`PG(2,2)`/`PG(2,3)` by `(ROW-K)` only. **`BUDGET-SLACK := |B| − Σ_{z}(deg(z)−1)`** is the new
design coordinate: an open instance needs `≥ 0` at **every** frame.

| host | `n` | `diam` | `l` | frames with `Z ≠ ∅` | BUDGET closes | min slack |
|---|---|---|---|---|---|---|
| `W43a` | 420 | 6 | 4.995 | 121 226 | 113 788 | **−6** |
| `W43b` | 420 | 6 | 4.995 | 97 890 | 92 139 | **−6** |
| `W43c` | 420 | 6 | 5.000 | 106 864 | 101 350 | **−4** |
| `W44a` | 421 | 6 | 4.988 | 124 759 | 116 932 | **−7** |
| `Petersen` | 10 | 2 | 3.000 | 120 | **0** | +1 |
| `C₇` / `C₈` | 7 / 8 | 3 / 4 | 2.000 | 14 / 16 | **0** / **0** | 0 / 0 |
| `PG(2,3)` | 26 | 3 | 4.000 | 2 808 | **0** | +1 |
| `PG(2,5)` | 62 | 3 | 6.000 | 46 500 | 46 500 | −7 |

(The frame counts here are `(v,P,y)` frames carrying at least one step-3 vertex; §51.3's
`F(H)` counts `(v,P,y,z)` tuples, which is why the two tables differ.)

**READ AGAINST ITS OWN INTEREST.** `(ROW-BUDGET)` still does not close CASE A — it closes
93.2 % of the frames of the four CASE A hosts and those hosts were already closed 490 529
frames over. What it adds is a **necessary condition of a new type**: the open object must
keep the *summed* degrees of every `y`'s step-3 shell inside the budget of the geodesic
tail, at every frame, and `PG(2,3)` at `l = 4.000` shows a host that satisfies it while
`W43a` at `l = 4.995` misses it by 6.

## 51.7 The entitled numbers, the owner errors, and what is NOT closed

> **ENTITLED. 68 C4-free hosts from 4 independent sources; `F/Z/N` EXHAUSTIVE on all 68 (no
> host needed the one-sided fallback). Hosts with `F > 0` and `Z = 0`: 7. With `F > 0` and
> `N = 0`: 3, and `⌊l⌋` on those is 3/2/2, never 4. Hosts meeting the target VACUOUSLY
> (`F = 0`): 2. CASE A frames at which `(TAIL-3″)` does not fire: 11, all on `W44a`, all at
> the same vertex. Best `FIRE-GAP` fraction among `⌊l⌋ = 4` hosts: 7.089 %. CASE A instances
> closed by `(TAIL-2S) ∪ (TAIL-2S′)`: 245 of 260; residual 15. Firing indices whose exhibited
> cycle was wrong: 0 of 26 219. Triangle-free frames with `deg(z) < k₃+1`: 0 of 9 739.
> `(ROW-BUDGET)`: 507 899 frames, counting bound violated 0 times, closes 473 277 (93.2 %),
> closes NOTHING on 14 of 22 hosts, fires on 0 frames of the three `N(H) = 0` hosts.**

**OWNER ERRORS THIS ROUND — two, both caught before this entry left the file.**
1. **A BUILDER USED OUTSIDE ITS DOMAIN.** `pg2(q)` inverts by Fermat (`pow(x, q−2, q)`),
   valid only for **prime** `q`; I put `PG(2,4)` in the host list. The result is neither a
   projective plane nor C4-free. **Caught by PART 0's C4-freeness assertion**, which is the
   assertion round 45's error 2 was about not having; the host was dropped with a printed
   line rather than silently. Same species as round 45 error 1, caught by round 45's fix.
2. **A LEMMA STATED WITH A HYPOTHESIS IT DOES NOT NEED.** `(TAIL-2S′)` was first written
   with the clause `q ≁ u_{d−2}`, carried over by analogy from `(TAIL-2S)`. It is vacuous:
   `u_{d−2}` is **not on the path** `R`. Corrected before the first quoted run, and the
   guard was re-pointed at `q ≁ u_{d−4}`, which is the clause the proof actually uses.

**ONE REGISTERED PREDICTION FAILED, AND IS REPORTED AS FAILED:** `(P6)`, that GUARD (D15)
would falsify the naive form of `(TAIL-2S′)`. It falsified 0 of 28 738.

**RECORD: 73 disclosed, 71 caught before leaving this file, 2 ESCAPED. Quote as 71–2.**

**WHAT IS NOT CLOSED.** `(HUG-CYC)` closes **nothing** on its own. `(ROW-BUDGET)` closes
nothing on 14 of 22 hosts. `(TAIL-2S) ∪ (TAIL-2S′)` leaves **15** CASE A instances. There is still **no theorem** forcing a CASE A instance into
any lane's hypothesis. **CASE A is not closed.** `G62` stays free. **Nothing is promoted and
nothing is stated outward.**
