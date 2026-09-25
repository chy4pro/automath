# VERIFICATION REVIEW — a PROOF CHAIN, not a new theorem

You are being asked to **review a chain of three results that have never been checked by anyone
other than their author**. The author is the same person for all three, they were produced in
three consecutive working sessions, and each one imports the previous. **A chain is exactly as
strong as its weakest unverified link**, and that is the whole reason this review exists.

**READ THIS FIRST, because it changes what a useful answer looks like.** The question is *not*
"is the final theorem true?". The author already believes it is, and independent bounded
enumeration agrees with it over 802 853 regions. The question is **whether the LINKS hold**:

> **(P1) — THE PRIMARY QUESTION, and answering only this one is a success for this brief.**
> At each point where the chain imports an earlier statement, **is that statement's hypothesis
> actually satisfied where it is used, and is its conclusion used exactly as stated — not
> silently strengthened, not applied to a larger set than it was proved for, not applied with a
> different definition of the same symbol?**

Two ranked below it, attempt them only if (P1) is settled:

> **(P2)** Is the assembly `(Z1)` — `Sigma_v (a(v)-3) <= n_3 + 2m - 6` — valid *as arithmetic*
> from the four inputs it names? Every term must be accounted for exactly once.
> **(P3)** Are the case analyses **complete** as claimed? Each is stated as "N frames, k survive".
> You cannot re-run them. What you *can* check is whether the case split, as described, exhausts
> the possibilities the argument needs it to exhaust, and whether the survivors listed are
> consistent with the conclusions drawn from them.

If you settle (P1) and go no further, write **`(P2)/(P3) NOT ATTEMPTED`** and stop. That is an
accepted answer and it is better than a thin pass over all three.

**A LOCATED GAP IS THE BEST OUTCOME OF THIS REVIEW, better than a clean verdict.** If one link
fails, name **which link, which step id, and what is missing**. "I could not verify step (Z5)
because the frame count is not reproducible from the text" is a valuable answer. A general
statement that the argument "seems plausible" is worth nothing here.

---

# PART 0 — THE HELD-OUT TABLE. Do this BEFORE reading any mathematics, and answer it in your reply.

Four graphs are printed below on vertex set `{0,...,n-1}`. **They are TEST GRAPHS ONLY.** They
are not instances of anything, no argument in this brief refers to them, and nothing below asks
you to reason about them. They exist so that the reviewer's arithmetic can be checked. **One of
the four is deliberately NOT in the class** — do not assume the class hypotheses hold for any of
them.

Definitions you need, and nothing else:
* `d(v)` = degree. `t(v)` = number of edges of `G` with both ends in `N(v)`. **`a(v) := d(v) - t(v)`**.
* `Z := (z_0,...,z_5) = (0,1,2,3,4,5)` in cyclic order in every printed graph.
* The **trace** of `v` not in `Z` is `N(v) ∩ Z`. `W_1` = trace of size 1; `W_cons` = trace of size
  2 at cycle-distance 1; `W_anti` = trace of size 2 at cycle-distance 3; `W_0` = empty trace.
* `T_Z := Sigma_{z in Z} t(z)`.  `n_3 := #{ v in W_1 : a(v) = 3 }`.
* "longest induced path" is counted **in VERTICES** (so a single edge is 2).

* **K1** edges: `[(0, 1), (0, 5), (1, 2), (1, 7), (1, 10), (2, 3), (3, 4), (4, 5), (4, 6), (4, 8), (4, 9), (7, 8), (7, 10), (8, 9)]`
* **K2** edges: `[(0, 1), (0, 5), (0, 7), (0, 8), (0, 9), (1, 2), (2, 3), (2, 10), (3, 4), (3, 9), (3, 10), (3, 11), (4, 5), (6, 9), (7, 10), (8, 11)]`
* **K3** edges: `[(0, 1), (0, 5), (1, 2), (2, 3), (2, 8), (2, 9), (3, 4), (4, 5), (4, 6), (5, 6), (5, 7), (6, 9), (8, 9)]`
* **K4** edges: `[(0, 1), (0, 3), (0, 5), (1, 2), (1, 7), (1, 10), (2, 3), (3, 4), (4, 5), (4, 6), (4, 8), (4, 9), (7, 8), (7, 10), (8, 9)]`

**Tiers are disclosed, deliberately, so you can spend your effort where it is worth spending:**

| row | tier | question |
|---|---|---|
| **V1** | **H** | K1: number of edges |
| **V2** | **H** | K1: degree of vertex 7 |
| **V3** | **H** | which of K1,K2,K3,K4 contains a 4-cycle, and its 4 vertices |
| **V4** | **H** | K1: trace census /W_1/,/W_cons/,/W_anti/,/W_0/ |
| **V5** | **H** | K1: a(7) = d - t at that vertex |
| **V6** | **C** | K4: longest induced path, in VERTICES |
| **V7** | **C** | K1: T_Z = sum_{z in Z} t(z), and sum_{z in Z}(a(z)-3) |
| **V8** | **C** | K2: sum_{v in V}(a(v)-3), and n_3 |
| **V9** | **C** | K3: T_Z, and sum_{v in V}(a(v)-3) |

**Tier H** rows are bounded local inspection of the printed edge list; they are hand-derivable and
a confidently stated wrong value on one of them **voids this entire review, mathematics included**.
**Tier C** rows are not reliably hand-derivable at this size; a wrong Tier-C value is recorded
against the specific row and demotes only conclusions that read that quantity.

> **`CANNOT COMPUTE — <reason>` is an ACCEPTED answer on ANY row, Tier H included. It is not a
> void and it is not a downgrade.** A stated wrong number is far worse than a refusal. Answer
> every row you attempt in the form `V1 = ...`, one row per line, before the mathematics.

---

# PART 1 — HYPOTHESES, and the imports, WITH THEIR GUARDS AT THE POINT OF IMPORT

Throughout, and **byte-for-byte** in all three links: `G` is a **connected**, **C4-free** graph
containing an **induced 6-cycle** `Z = (z_0,...,z_5)`, and **`G` has no induced P7**. The target
is

> **(D3-C6)**: under exactly those hypotheses, `Sigma_{v in V} a(v) <= 3n`, equivalently
> `Sigma_v (a(v) - 3) <= 0`.

**Five earlier statements are imported by the chain. Each is restated here IN FULL with its own
hypotheses**, so that you can check the import without following a reference. Where a guard
cannot travel with the statement, that is said explicitly.

**IMPORT 1 — `G54` (off-cycle attachment classification).**
> *Hypotheses: `Z` an induced 6-cycle of a **C4-free** graph, `w` not in `Z`.*
> Then `N(w) ∩ Z` contains no pair at cycle-distance 2; hence `|N(w) ∩ Z| <= 2`, and a 2-element
> trace is **consecutive or antipodal**.
> *Proof: if `w ~ z_i` and `w ~ z_{i+2}` then `z_i, z_{i+2}` have common neighbours `z_{i+1}` and
> `w`, a C4. Any 3 vertices of a 6-cycle contain a distance-2 pair.*
> **GUARD AT THIS IMPORT SITE:** G54 needs **C4-freeness only** — it does not need P7-freeness or
> connectivity, so it survives passage to any induced subgraph containing `Z`. This is what makes
> the frame tables below legitimate.

**IMPORT 2 — `G55` (on-cycle charge identity).**
> *Hypotheses: `Z` an induced C6 of a **C4-free** graph; `Off(z) := N(z) \ Z`.*
> `a(z) = 2 + |Off(z)| - t(z)`, hence `Sigma_{z in Z}(a(z)-2) = Sigma_{z in Z}(|Off(z)| - t(z))`.
> *Proof: `Z` induced gives `d(z) = 2 + |Off(z)|`; C4-freeness makes `G[N(v)]` a **matching** (if
> `x ~ y ~ z` inside `N(v)` then `v-x-y-z-v` is a C4), so `a(v) = d(v) - t(v)`.*
> **GUARD AT THIS IMPORT SITE:** the matching step is **not** true of graphs in general — it is
> exactly where C4-freeness is spent. **And G55's named limitation travels with it:** a `Z`-local
> charge count **cannot see charge living away from `Z`**, because the off-cycle population
> attached to `Z` is unbounded. That is why the chain needs links 1 and 2 at all.

**IMPORT 3 — `G57` (the consecutive-trace lemma).**
> *Hypotheses: `G` C4-free, `Z` an induced C6, **no induced P7**.*
> `W_cons` vertices never occupy the same slot **(i)** nor overlapping slots **(ii)**; hence the
> occupied slots are independent in the slot-6-cycle and **`|W_cons| <= 3`**, attained **(iii)**;
> at slot distance 2 two such vertices are non-adjacent, at distance 3 both occur **(iv)**.
> *Proof of (ii), the one that uses P7: with traces `{z_0,z_1}` and `{z_1,z_2}` every adjacency
> among the 8 vertices is forced except the bit `ww'`; `w !~ w'` gives the induced P7
> `w z_0 z_5 z_4 z_3 z_2 w'`, and `w ~ w'` gives a C4 at `(w, z_2)` via `z_1, w'`.*
> **GUARD AT THIS IMPORT SITE:** G57 **does** need P7-freeness, so unlike G54 it may only be
> applied inside the class — never to an arbitrary induced subgraph chosen for convenience.

**IMPORT 4 — `§34.4a` (`|W_anti| <= 3`).**
> Each antipodal **slot** holds at most one vertex: two vertices with the same antipodal trace
> `{z_i, z_{i+3}}` are two common neighbours of `z_i` and `z_{i+3}`, a C4. There are 3 slots.
> **GUARD AT THIS IMPORT SITE:** C4-freeness only. Attained at `n = 9` by
> `0-1,1-2,2-3,3-4,4-5,5-0,6-0,6-3,7-1,7-4,8-2,8-5` (C4-free, induced C6, longest induced path 5).

**IMPORT 5 — the definition of `a`, and it is the one place a symbol could silently change
meaning.** `a(v) = d(v) - t(v)` is used identically in all three links and in `(D3-C6)`.
**This is worth one of your checks**: the chain's failure mode of exactly this shape would be a
step where `a` means "size of a maximum independent set in `N(v)`" in one link and `d - t` in
another. Under C4-freeness `G[N(v)]` is a matching, so the two agree — but the agreement is a
*consequence of C4-freeness*, not a definition, and it is imported as such.

**A GUARD THAT CANNOT MOVE, said here rather than hidden.** The three links are supported by
machine enumerations — frame tables of 32 to 872 frames, and two sweeps over 802 853 and 90 859
regions. **You cannot re-run those and this brief does not pretend you can.** Their populations
are printed inside the text below, deliberately, so that you can at least check them for internal
consistency (e.g. that a table's "N frames" is the product of the free bits it describes). Where
a conclusion rests only on an unreproducible count, **say so** — that is a legitimate and useful
finding, not a failure to review.

---

# PART 2 — LINK 1, `G58` (draft §35), VERBATIM


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



---

# PART 3 — LINK 2, `G59` = (B)/(B'), (draft §36), VERBATIM


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



---

# PART 4 — LINK 3, the `Z`-term (draft §37), VERBATIM — this is where the chain closes


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

So leaks sit at **distinct** hexagon vertices and any two of them are **antipodal**; since
antipodality is a perfect matching on the hexagon, **three leaks are impossible: `n_3 ≤ 2`.**
The antipodal row is **live** (2 survivors, promoted to the `n = 10` host above), so (Z4) is a
restriction and not a vacuity.

**(Z5) — `Z + N[v] +` the `W_anti` vertices themselves.** Their own neighbourhoods are not
needed: a refutation on a subframe refutes every host containing it. The `w`-to-`N[v]` bits
**and** the `w`-to-`w'` bit are enumerated, not assumed.
*One* occupied slot: **32 frames at each of the 6 leak positions, survivors 2,1,1,2,1,1** — so a
leak and an occupied slot **do** coexist, and the owner's second hand claim (that they cannot)
was **false**. *Two* occupied slots: **384 frames at each of all three slot pairs
`{(0,3),(1,4)}, {(0,3),(2,5)}, {(1,4),(2,5)}`, and 0 survive.* Hence `n_3 ≥ 1 ⟹ m ≤ 1`.

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



---

# PART 5 — THREE CONTROLS, IN THE AUTHOR'S OWN WORDS, on how hand reasoning about this object
# has actually failed

These are not rhetorical. They are three self-reported errors from the three sessions that
produced the three links above, and they went wrong in **three different directions**. They are
here because they tell you where to point your scepticism — and because a reviewer who reproduces
one of them will recognise it.

1. **True but not sharp.** A hand bound was correct and was then used as if it were tight. The
   enumeration showed the true extremum was strictly smaller, and an argument built on the loose
   value silently proved less than it claimed.
2. **A claim inverted.** The author argued that a leaking `W_1` vertex **excludes** an occupied
   antipodal slot. The enumeration says they **coexist** (2 survivors of 32). The true statement
   is weaker and is the one now in (Z5): a leak excludes the **second** slot, not the first.
3. **A hand argument that DISPROVED a true theorem.** From "each leak needs two far neighbours,
   made distinct by C4-freeness", the author built `k` leaks at a single hexagon vertex, computed
   `Sigma(a-3) = k - 6`, and so obtained `+1` at `k = 7` — a *counterexample to (D3-C6)*. **(Z3)
   says `k <= 1`**, and an induced P7 kills the construction already at `k = 2`. The hand
   argument did not fail to prove the theorem; it disproved it.

**The moral the author drew, and you should hold him to it:** on this object, plausible local
reasoning is unreliable in both directions, and the enumerations are the load-bearing part. If a
step in PART 2-4 is justified by prose rather than by an enumeration whose population is printed,
**that step is the one to attack.**

---

# PART 6 — WHAT WILL NOT BE READ, stated in advance so you do not spend budget on it

* **Any argument whose mechanism bounds `n`, or that concludes "`n >= ...`" or "the class is
  finite", is refused without being read on its merits.** The class is known to contain
  arbitrarily large members (Theorem G49 of this project; its construction is deliberately not
  reprinted). If your reasoning reaches such a conclusion, you have made an error upstream.
* **Any argument concluding `W_1 = ∅` or `W_cons = ∅` is refuted before it is read.** Both are
  non-empty inside the hypotheses; explicit `n = 9` in-hypothesis witnesses exist for both. That
  conclusion is the *P6*-level statement, and dropping P6 for P7 is precisely what destroys it.
* **A counterexample is graded exactly as strictly as a proof.** If you believe you have one,
  give the complete edge list and validate it **most-basic-first**: C4-freeness FIRST, then `Z`
  induced, then longest induced path `<= 6`, then the `a`-values. An unvalidated counterexample
  is recorded as a fabrication, not as a refutation.

---

# PART 7 — OUTPUT FORMAT (please follow it exactly)

```
V1 = ...          (one line per held-out row, FIRST, before any mathematics)
...
V9 = ...

VERDICT: CLEAN | GAP | REFUTED
(P1) LINKS: for each import site you checked -- site, imported statement, hypothesis satisfied?
     conclusion used as stated?  one line each.
(P2) ...  or  (P2) NOT ATTEMPTED
(P3) ...  or  (P3) NOT ATTEMPTED
GAPS: link / step id / what is missing.  One line each.  Empty if none.
```

**Length: aim for about 1200 words of deliverable.** If your answer is running long, **cut the
discussion and keep the findings** — a located gap in ten words outranks three pages of summary.
Do not restate the mathematics back to me; I wrote it. Tell me where it breaks, or tell me,
link by link, that it does not.
