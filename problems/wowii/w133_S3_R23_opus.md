VERDICT: PARTIAL
MATHEMATICS DEFECT FOUND: NO

**Headline.** The three results up for adoption — **Lemma G36, Lemma G37 and Theorem G38 —
are clean.** I attacked every step the brief named and found no mathematics defect in any
of them; every construction was additionally exercised on graphs where its branch actually
fires. The defects I confirmed are all in the surrounding annotations. One of them is
substantive and should not be waved through: **C.4's closing claim that "the F4 form of the
forced-Case-2 `d = 3` statement remains open" is FALSE — I produced an explicit
counterexample (`H`, `n = 10`, verified minimal).** By the brief's own taxonomy that is a
BOOKKEEPING defect (a status line / overstated remark whose repair leaves every proof in
scope intact), so it does not set the mathematics bit; but it changes the research picture
and is flagged prominently under R-B2 below. If the gate operator's taxonomy treats a
refuted status claim as MATHEMATICS, this is the one item that would flip the bit — I say
so explicitly rather than hiding the judgement call.

All numbers below were recomputed by me from the PART A definitions; none were taken from
the brief. Code was calibrated first on `C5`, `K3`, `P4`, `K_{1,4}`, the bowtie, and on
`C4` itself as a negative control (correctly flagged non-`C4`-free) — every value matched a
hand computation before any of it was used.

---

## 1. Per-joint table

| joint | verdict | what I did, and what I found |
|---|---|---|
| **R-M1** | **CLEAN** | **(a) Licensing.** The definition quantifies **universally** ("*every* geodesic of length ≥ rad is 3-capped at both ends"), so Lemma 1 is free to pick a convenient geodesic — the quantifier direction is favourable, not hostile. For every `v`, `ecc(v) ≥ rad` by definition of `rad`, so a vertex `w` with `dist(v,w) = ecc(v) ≥ rad` exists and any `v`–`w` shortest path is a geodesic of length `≥ rad` with `v` as an end. **Centres are fine**: a centre has `ecc(v) = rad`, and a geodesic of length exactly `rad` still has length `≥ rad`. **`a(v) ≤ 1` is fine**: then `G[N(v)] = C₀` is a single component, there are no usable side-neighbours, the cap is vacuous — and the conclusion still holds because `d_S(v) ≤ d(v) = \|C₀\| ≤ 2`. **`rad = 0`** happens iff `n = 1` (connected, `n ≥ 2` ⟹ every `ecc ≥ 1`); there the "geodesic" has length 0, has no `u₁`, and "3-capped" is undefined — a genuine but harmless gap in the printed proof, since `a(v) = 0` and `S = ∅` (logged as B8). The step "`S`-neighbours cannot be usable side-neighbours, hence lie in `C₀`, and `\|C₀\| ≤ 2`" is correct: 3-capping at `v` says every element of `N(v) ∖ C₀` has `a ≤ 3`, an `S`-neighbour has `a ≥ 4`, and `\|C₀\| ≤ 2` by F1 (components of `G[N(v)]` are vertices or edges). Licensing holds for **every** class of vertex; Lemma 3's degree bound survives intact. **(b) The `l = 4` boundary.** I re-derived every inequality of the non-strict run separately: the F3-analogue `Σ_{v∈S} a(v) ≥ 4n − 3(n−\|S\|) = n + 3\|S\|`; the lower bound `d_T(v) ≥ a(v) − 1` (`K₃`, `K₂`) and `≥ a(v)` (`K₁`) — I re-checked `t_SS = 1, t_ST = 0` in the `K₃` case (the two `S`-neighbours are matched to *each other*, and a matching has max degree 1) and `t_ST ≤ 1` in the `K₂` case; the summation `E(S,T) ≥ Σ_{v∈S} a(v) − (\|S\| − k₁)` using `\|S₁\| = k₁`; the upper bound `E(S,T) = 2\|T₂\| + \|T₁\| ≤ k₂ + n − \|S\|` (the map `T₂ → K₂`-components is injective by Lemmas 6+5); the substitution `3(3k₃+2k₂+k₁) + k₁ ≤ k₂ ⟹ 9k₃ + 5k₂ + 4k₁ ≤ 0`; and the endgame `S = ∅ ⟹ Σa ≤ 3n < 4n` (needs `n ≥ 1`, which connectivity gives). Every one is correct in its non-strict form. **The conclusion is `l < 4`, strictly — as printed.** `l ≤ 4` would be *weaker than what the proof gives*: the argument refutes `Σa ≥ 4n`, not merely `Σa > 4n`, and the `S = ∅` endgame is exactly what converts the non-strict run into a strict conclusion. The Boundary note's description of the strict-hypothesis run (`9k₃+5k₂+4k₁ < 0`, no endgame needed) is also correct. **Machine corroboration:** every one of Lemmas 1–6, `\|T₂\| ≤ k₂`, the upper bound, the per-vertex lower bounds and the theorem itself were checked on **all 3,152,456** connected `C4`-free peripherally-3-capped labelled graphs with `n ≤ 8` (exhaustive edge-subset DFS with `C4` pruning; 3,042,712 of them at `n = 8`) and on **133,669** random ones with `n ≤ 16`. **Zero violations.** |
| **R-M2** | **CLEAN** | **Step 1 kill accounting at `d = 4`.** The `u₄`-kill is genuinely **0**: any `w ∈ N(x)` has `dist(u₀,w) ≤ 2`, so `dist(w,u₄) ≥ 4 − 2 = 2`. The `y`-kill is `≤ 1` because `x ≁ y`, and *that* is what `d = 4` buys: `dist(u₀,y) ≥ 4 − 1 = 3` forces `dist(x,y) ≥ 2`. (At `d = 3` this collapses to `dist(x,y) ≥ 1` — which is precisely why G37 must assume `y ≁ x`. The two lemmas' hypothesis difference is correctly placed.) `x ≁ u₂` (else `u₀,u₂` share `x,u₁`, using `x ≠ u₁`), `x ≁ u₃` (distance). `a(x) ≥ 4` gives `≥ 4` components of `G[N(x)]`, minus `u₀`'s leaves `≥ 3`, against exactly 3 kills — **tight but sufficient**. **The "otherwise" branch is genuinely forced**: each of `y,u₂,u₃` has `≤ 1` neighbour in `N(x)`, so if none of `w₁,w₂,w₃` avoids all three kills, the bipartite incidence between `{w₁,w₂,w₃}` and `{y,u₂,u₃}` has every left-degree `≥ 1` and every right-degree `≤ 1`, hence is a perfect matching — the relabelling is legitimate (the text leaves this implicit; see B7-adjacent note in §4). **`z` exists**: `a(u₀) ≥ 3` gives `≥ 3` components of `G[N(u₀)]`, of which `u₁`'s and `x`'s are two *distinct* ones (distinct precisely because `x` is a usable side-neighbour), so a third exists — "outside `u₁`'s **and** `x`'s components" is simultaneously achievable. **All 7 edges** of `z–u₀–x–w_y–y–u₄–u₃–u₂` present. **All 21 non-adjacencies re-derived one by one**, with the hypothesis each consumes, in §2a below; the printed list is complete (21/21) and every justification is correct. **All 8 vertices pairwise distinct** (I re-derived each of the 28 inequalities; `w_y ≠ u₂` and `w_y ≠ u₃` because `x ≁ u₂,u₃` and `dist(u₀,w_y) = 2 ≠ 3`; `w_y ≠ z` because `w_y ~ x` and `z ≁ x`). Bookkeeping only: B2, B3. **Machine corroboration:** 2,886 *live* `d = 4` frames (built so the frame provably survives every edge added) — no graph with a live frame had `path(G) < 8`; and the **Step 3 construction itself** was built and tested on **512** configurations in which the Step-3 branch actually fires, plus **405,610** Step-2 firings, including on PG(3,2) which carries 10,080 genuine `d = 4` frames. Zero failures of edge-presence, chordlessness or distinctness. |
| **R-M3** | **CLEAN** | **The repair is correct and is the right repair.** The `C4` is explicitly `x – u₀ – u₁ – w₂ – x`: if `u₁ ~ w₂` then `x` and `u₁` have the two common neighbours `u₀` (since `x ~ u₀ ~ u₁`) and `w₂` (since `x ~ w₂ ~ u₁`); the side conditions `x ≠ u₁` (`x` is outside `u₁`'s component) and `u₀ ≠ w₂` (different components of `G[N(x)]`) both hold, so this is a genuine 4-cycle and the original "they share `u₂` and are not adjacent" is correctly discarded as a non-reason. **`y ≁ w₂` (1b-ii)** is also correct: `x ≠ y` (`dist(u₀,x) = 1`, `dist(u₀,y) ≥ 2`), so `C4`-freeness gives `\|N(x) ∩ N(y)\| ≤ 1`; and **`w₁` really is adjacent to `y`** — `w₁` is by definition the `y`-kill, i.e. the case assumption is `w₁ ~ y`, and `w₁ ~ x` since `w₁ ∈ N(x)`; so `w₁ ∈ N(x) ∩ N(y)` occupies the single slot and `w₂ ∉ N(y)`. The uniqueness argument is right. The second repaired step (`u₀ ≁ w₂`) is immediate from the component choice. **All three subcases re-derived chord by chord** (§2b): 1a has 15 non-adjacent pairs of which the printed list gives 14 (missing `x ≁ u₁`, B2); 1b-i's list is complete (15/15); 1b-ii's list is complete (15/15). Every justification checks out. **`z` exists and is distinct** from all six other vertices (`z ≠ w₁, w₂` since `z ≁ x` but `w_i ~ x`; `z ≠ u₂,u₃` by distance; `z ≠ y` in 1b-i because `z ~ u₀` and `dist(u₀,y) ≥ 2`, in 1b-ii because `z ~ y`). **`w₁,w₂,w₃` cannot collide** with each other (distinct components of `G[N(x)]`) nor with `y` (each `w_i ~ x` while `y ≁ x`). **Case 1's extra hypothesis `y ≁ x` is used in exactly four places and nowhere else**: (1) the kill accounting, to get `\|N(x) ∩ N(y)\| ≤ 1`; (2) the chord `x ≁ y` in 1a; (3) the chord `x ≁ y` in 1b-i; (4) the repaired `y ≁ w₂` in 1b-ii. It is *not* smuggled into 1b-ii's other chords. Bookkeeping only: B2, B4. **Machine corroboration:** 2,237 live `d = 3` Case-1 frames, no `path(G) < 7`; and the three printed paths built and tested on 254,185 (1a), 87 (1b-i) and **148 (1b-ii, the repaired subcase)** live firings — zero failures. |
| **R-B1** | **PARTIAL** | **(i) is a correct contrapositive as stated.** `¬(∀ geodesic of length ≥ rad: 3-capped at both ends)` = `∃` geodesic `P` of length `≥ rad` and an end `e` of `P` at which `P` is not 3-capped = that end carries a usable side-neighbour `x` (w.r.t. `P`) with `a(x) ≥ 4`. That is exactly what is claimed, and the class is non-vacuous: geodesics of length `≥ rad` always exist (take a centre and a vertex at distance `ecc = rad`). **Two findings.** (α) *Free generality, not a defect:* the proof supports **`l ≥ 4`**, not only `l > 4`, since G38 concludes `l < 4`. PG(2,3) is a live witness of the extra range — I computed `l(PG(2,3)) = 4.0` exactly and confirmed it is **not** peripherally 3-capped, with explicit witness geodesic `(0,16,10,17)` of length `3 ≥ rad = 3`, end `u₀ = 0`, usable side-neighbour `x = 13`, `a(13) = 4`. (β) *Usability note (BOOKKEEPING, B9):* the consequence delivers `a(u₀) ≥ 2` only (implied by `x`'s existence) and says **nothing about the other end**. G14/G36/G37 all need `a(u₀) ≥ 3` **and** `a(u_d) ≥ 2`. So the consequence as printed does **not** by itself hand the lemma chain its hypotheses, and reading it as if it did would be an error downstream. It is stated correctly; I flag the gap because the sentence is written as though it were the input to the chain. **(ii) The vacuity annotation's logic is right and correctly scoped.** It attaches to the non-emptiness of the `rad ≥ 5` *slice of the consequence*, not to G38's truth — an implication with an empty antecedent slice is still true, just uninformative there. Its data are consistent with what I could compute: the only `C4`-free graph with `l > 4` I could construct is PG(3,2)/STS(15), and I recomputed `l = 4.2`, `rad = 3`, `diam = 4` — `rad ≤ 4`, consistent with the annotation. **"G38 itself is not vacuous: it executes on the `rad = 3` class" is TRUE** — I verified `C₇` (`C4`-free, `rad = 3`, all `a = 2`, peripherally 3-capped) and an 8-vertex peripherally-3-capped example with `rad = 3` and `S ≠ ∅`. |
| **R-B2** | **REFUTED** | **CE-1 itself is entirely sound** — I re-verified it from the edge list with my own code, `C4`-free first: simple (11 edges, no repeats), connected, **`C4`-free** (no two distinct vertices with two common neighbours; also confirmed by explicit search for 4-cycles as subgraphs). `a`-values recomputed two independent ways (brute-force independence number of `G[N(v)]`, and component count) and cross-checked against `d(v) − t(v)`: `a = (2,1,3,1,2,4,2,1,1,2)`. `2–6–4–9` **is** a geodesic of length 3 (`dist(2,9) = 3`: 2 and 9 are non-adjacent with no common neighbour). `a(u₀) = a(2) = 3`, `a(u₃) = a(9) = 2`, `x = 5` **is** a usable side-neighbour of `2` (components of `G[N(2)]` are `{5,8},{3},{6}`; `u₁ = 6`'s component is `{6}`) with `a(5) = 4`. **Case-2-forced confirmed**: `G[N(9)]` has components `{0},{4}`, so the unique usable side-neighbour of `u₃` is `y = 0`, and `0 ~ 5 = x`. **`path(G) = 6` exactly**, by brute force over *all* vertex subsets — no induced path on 7, 8, 9 or 10 vertices exists; witness `0–9–4–6–2–8`. So `6 < 7 = d + 4` and the **bare `d = 3` statement is indeed FALSE — that part of the conclusion stands.** **Peeling verified concretely:** the `a = 1` vertices are exactly `{1,3,7}` (leaves) and `{8}` (`N(8) = {2,5}` with `2 ~ 5`, a triangle-leaf); deleting them one at a time (checking `a = 1` in the *current* graph at each step) leaves `{0,2,4,5,6,9}` inducing exactly the 6-cycle `0–5–2–6–4–9–0`, with all `a = 2` and **max `a` = 2**, so no vertex with `a ≥ 4` survives and the frame is destroyed. Order-independence spot-checked (deleting `8` first gives the same `C₆`). **Hence "CE-1 does not refute the F4 form" is also correct.** ⚠️ **But the closing sentence is refuted.** "*the F4 form of the forced-Case-2 statement remains open*" is **FALSE**. Counterexample **`H`** (§3c): `n = 10`, `m = 14`, edges `01, 04, 05, 08, 12, 23, 26, 35, 37, 39, 46, 47, 48, 89`. Independently verified: simple, connected, `C4`-free (both by the two-common-neighbours test and by exhaustive 4-cycle search); `a = (3,2,3,4,3,2,2,2,2,2)`, cross-checked against `d(v) − t(v)`; **`min a(v) = 2`, so F4 holds and no peeling is possible**; `(2,1,0,8)` is a geodesic of length 3 with `a(u₀) = a(2) = 3`, `a(u₃) = a(8) = 2`; `x = 3` is a usable side-neighbour of `2` with `a(3) = 4`; the unique usable side-neighbour of `u₃ = 8` is `y = 9`, and `9 ~ 3 = x`, so the frame is **Case-2-forced**; and **`path(H) = 6 < 7`**, by brute force over all subsets (witness `4–0–1–2–3–9`). `H` has a second qualifying frame `(2,6,4,8)` with the same `x` and `y`. `H` does **not** contradict G37 (it has *no* Case-1 frame) nor G36/G14 (`diam(H) = 3`, so no `d ≥ 4` geodesic at all) — I checked both explicitly. **The refutation is robust and minimal**: 132 independent F4-form counterexamples turned up in the search, all at `n ≥ 10`; and `n ≥ 9` is forced by a vertex count (`u₀,u₁,u₂,u₃,x,z,w₁,w₂,w₃` are necessarily 9 distinct vertices), while an **exhaustive** enumeration of the 2¹⁴ completions of the forced `n = 9` skeleton found **none**. So `H` is a minimum-order witness. **Consequence for the text:** "*Therefore F4 … is NECESSARY at `d = 3`, not a convenience*" is an overstated remark. What CE-1 establishes is that the bare statement needs *some* strengthening; it does not single out F4, and we now know F4 is **not** a strengthening that works. Classification: **BOOKKEEPING** (status line + overstated remark; repairing it to "*is FALSE, witness `H`*" leaves G36, G37, G38, S-1 and CE-1's own verification untouched — nothing in scope consumes it). |
| **R-B3** | **CLEAN** | All three assertions are **true**, and each is short enough to prove outright. **(i)** `a(u₃) ≥ 2` ⟹ `G[N(u₃)]` has a component other than `u₂`'s ⟹ at least one usable side-neighbour exists. Case-2-forced says every such `y` has `y ~ x`; and every such `y` has `y ~ u₃`; so the usable set `⊆ N(x) ∩ N(u₃)`. `x ≠ u₃` because `dist(u₀,x) = 1` while `dist(u₀,u₃) = 3`, so `C4`-freeness gives `\|N(x) ∩ N(u₃)\| ≤ 1`. Hence **exactly one**. *Consumes:* `C4`-freeness, the geodesic (only for `x ≠ u₃`), `a(u₃) ≥ 2`, Case-2-forced. *Free corollary the text does not draw:* this forces `a(u₃) = 2` exactly, and forces every non-`u₂` component of `G[N(u₃)]` to be a singleton (two usable neighbours in one matching edge would both have to lie in a set of size `≤ 1`). **(ii)** `dist(u₀,y) ≤ 2` via `u₀ ~ x ~ y`; `dist(u₀,y) ≥ dist(u₀,u₃) − dist(u₃,y) = 3 − 1 = 2`. Hence `= 2`. *Consumes:* the geodesic (`dist(u₀,u₃) = 3`), `y ~ x ~ u₀`, `y ~ u₃`. **(iii)** All six pairwise distances of `u₀,x,y,u₃` equal `\|i−j\|`: `1,2,3` from `u₀`; `dist(x,y) = 1`; `dist(x,u₃) ≤ 2` via `y` and `≥ dist(u₀,u₃) − 1 = 2`; `dist(y,u₃) = 1`. So it is a geodesic. *Consumes:* the same, plus (ii). **`a(u₀) ≥ 3` and `a(x) ≥ 4` are used by none of (i),(ii),(iii)** — free generality (see the audit table). Verified on **325,916** instances of the *weakened* hypothesis set (any `x ∈ N(u₀)` outside `u₁`'s component, no `a(x)` or `a(u₀)` bound), zero violations; and directly on CE-1 and on `H`'s two Case-2-forced frames. |

### 2a. R-M2 — the 21 non-adjacencies of `z – u₀ – x – w_y – y – u₄ – u₃ – u₂`, re-derived

Not copied from the brief; each re-derived, with the hypothesis it consumes.
`C4` = `C4`-freeness, `G` = geodesic property, `K` = component choice / kill structure.

| pair | reason | consumes |
|---|---|---|
| `z ≁ x` | different components of `G[N(u₀)]` | K |
| `z ≁ w_y` | else `u₀, w_y` share `x, z` (`u₀ ≠ w_y`, `x ≠ z`) | C4 + K |
| `z ≁ y` | `z ~ u₀` and `z ~ y` would give `dist(u₀,y) ≤ 2`, but `dist(u₀,y) ≥ 4 − 1 = 3` | G |
| `z ≁ u₄` | `dist(z,u₄) ≥ 4 − 1 = 3` | G |
| `z ≁ u₃` | `dist(z,u₃) ≥ 3 − 1 = 2` | G |
| `z ≁ u₂` | else `u₀, u₂` share `z, u₁` (`z ≠ u₁` by component) | C4 + K |
| `u₀ ≁ w_y` | different components of `G[N(x)]` | K |
| `u₀ ≁ y` | `dist(u₀,y) ≥ 3` | G |
| `u₀ ≁ u₄`, `u₀ ≁ u₃`, `u₀ ≁ u₂` | geodesic | G |
| `x ≁ y` | `dist(x,y) ≥ dist(u₀,y) − 1 ≥ 2` | G |
| `x ≁ u₄` | `dist(x,u₄) ≥ 4 − 1 = 3` | G |
| `x ≁ u₃` | `dist(x,u₃) ≥ 3 − 1 = 2` | G |
| `x ≁ u₂` | else `u₀, u₂` share `x, u₁` (`x ≠ u₁`) | C4 + K |
| `w_y ≁ u₄` | `dist(w_y,u₄) ≥ 4 − 2 = 2` | G |
| `w_y ≁ u₃` | `\|N(x) ∩ N(u₃)\| ≤ 1` and that slot is `w₃`, a different component | C4 + K |
| `w_y ≁ u₂` | `\|N(x) ∩ N(u₂)\| ≤ 1` and that slot is `w₂`, a different component | C4 + K |
| `y ≁ u₃` | `y` chosen outside `u₃`'s component of `G[N(u₄)]` | K |
| `y ≁ u₂` | else `u₂, u₄` share `y, u₃` (`y ≠ u₃`, `u₂ ≠ u₄`) | C4 + K |
| `u₄ ≁ u₂` | geodesic | G |

21/21 accounted for; the printed list is complete and correct. The `x ≁ u₁` omission is in
**Step 2's** list, not Step 3's (B2).

### 2b. R-M3 — chord-list completeness per subcase

| subcase | pairs to check | printed | missing |
|---|---|---|---|
| 1a `w_i–x–u₀–u₁–u₂–u₃–y` | 15 | 14 | `x ≁ u₁` (true: `x` outside `u₁`'s component) — **B2** |
| 1b-i `z–u₀–x–w₁–y–u₃–u₂` | 15 | 15 | none |
| 1b-ii `w₁–y–z–u₀–u₁–u₂–w₂` | 15 | 15 | none |

Distinctness is asserted in none of the three subcases (**B4**); I verified it holds in all
of them, by hand and on every live firing.

---

## 3. MANDATORY PROBE 1 — statement-hypothesis audit, both directions

Each statement read **alone, as a stranger would**, with no section header and no ambient class.

| # | statement | hypotheses the STATEMENT carries | hypotheses the PROOF uses | verdict |
|---|---|---|---|---|
| 1 | **G36** | connected; `C4`-free; geodesic `u₀…u₄` (`d = 4`); `a(u₀) ≥ 3`; `a(u₄) ≥ 2`; usable side-neighbour `x` of `u₀` with `a(x) ≥ 4` | `C4`-freeness (Step 1 kills, `x ≁ u₂`, `z ≁ w_y`, `z ≁ u₂`); geodesic + `d = 4` exactly (`u₄`-kill `= 0`, `x ≁ y`, `x ≁ u₄`, `z ≁ u₃,u₄`); `a(u₄) ≥ 2` (existence of `y`); `a(u₀) ≥ 3` (existence of `z`, Step 3 only); `a(x) ≥ 4` (≥ 3 non-`u₀` components). **Connectivity is never used** — the `P₈` is exhibited explicitly and all distance facts are lower bounds, valid with `∞` | **STATEMENT NARROWER THAN PROOF** (free generality: connectivity can be dropped). No wider-than-proof gap. |
| 2 | **G37** | connected; `C4`-free; geodesic `u₀u₁u₂u₃`; `a(u₀) ≥ 3`; `a(u₃) ≥ 2`; usable `x` with `a(x) ≥ 4`; usable `y` of `u₃` with `y ≁ x` | `C4`-freeness; geodesic; `a(x) ≥ 4`; `a(u₀) ≥ 3` (for `z`, subcase 1b only); `y ≁ x` (4 places, listed under R-M3); the *existence* of `y` | **STATEMENT NARROWER THAN PROOF** twice over: connectivity unused, and **`a(u₃) ≥ 2` is redundant** — it is implied by the hypothesis that a usable side-neighbour `y` of `u₃` exists. Harmless. |
| 3 | **G38** | connected; `C4`-free; peripherally 3-capped | connectivity (finite `ecc`/`rad`; `n ≥ 1` for `3n < 4n`); `C4`-freeness (F1, and Lemmas 2–6); peripherally 3-capped (Lemma 1 only) | **EQUAL.** Connectivity is genuinely load-bearing, not decorative: for a disconnected graph "geodesic of length `≥ rad`" is vacuous under the usual `rad = ∞` convention, so **two disjoint copies of PG(2,3)** would be vacuously "peripherally 3-capped" with `n = 52`, `Σa = 208`, `l = 4.0` — a counterexample to the statement with `connected` deleted. Good hypothesis hygiene. |
| 4 | **G38 Lemma 1** ("Every vertex `v` has at most 2 neighbours in `S`") | **none whatsoever** as printed | `G` connected `C4`-free **peripherally 3-capped**; `S = {v : a(v) ≥ 4}`; F1 | **STATEMENT WIDER THAN PROOF as printed** ⟹ false read alone. Smallest counterexample I built: the tree `T*` on `n = 16` — a centre `c` with three neighbours `s₁,s₂,s₃`, each `sᵢ` carrying 4 extra leaves. Verified `C4`-free (a tree), connected, `a(c) = 3`, `a(sᵢ) = 5`, so `S = {s₁,s₂,s₃}` and `d_S(c) = 3 > 2`. `T*` is not peripherally 3-capped, which is exactly what rescues the lemma. **Mitigation:** Lemmas 1–6 are displayed *inside* G38's proof, after "Suppose for contradiction", so the inheritance is typographically legitimate. I classify this **BOOKKEEPING**, but flag it because it is precisely the species named in the brief, and Lemma 1 is the joint the gate turns on. Recommend restating as "Let `G` be as in Theorem G38. Then …". |
| 5 | **G38 Lemma 2** ("If `v ∈ S` has two `S`-neighbours `s₁,s₂` then `s₁ ~ s₂`") | `v ∈ S`; otherwise none as printed | Lemma 1's **proof** (peripherally 3-capped + `C4`-free) applied to `v`; **`v ∈ S` is never used** | Both directions at once: **WIDER** w.r.t. the ambient class (as row 4), and **NARROWER THAN PROOF** w.r.t. `v ∈ S`. The free generality is not idle — **Lemma 6 actually needs the `v ∈ T` case** and reaches it only by re-invoking "Lemma 1's proof". Recommend dropping `v ∈ S` from Lemma 2 and citing it in Lemma 6. |
| 6 | **G38 Lemma 3** (`G[S]` is a disjoint union of `K₃`, `K₂`, `K₁`) | none as printed | Lemma 1 (⟹ peripherally 3-capped), Lemma 2, `C4`-freeness | **WIDER THAN PROOF as printed** (same mitigation as row 4). Mathematically the proof is sound; note that for cycles/paths on `≥ 4` vertices the *immediate* contradiction is with `Δ(G[S]) ≤ 2` (the forced chord raises a degree to 3), which is cleaner than the printed `C4` route and covers all `k ≥ 4` uniformly (B7). |
| 7 | **G38 Lemma 4** (no `T`-vertex adjacent to two vertices of a `K₃` component) | `{a,b,c}` is a `K₃` **component** of `G[S]`; `u ∈ T` | **`C4`-freeness alone**, plus `a,b,c` pairwise adjacent and `u ∉ {a,b,c}` | **STATEMENT NARROWER THAN PROOF.** The proof gives: *in any `C4`-free graph, no vertex outside a triangle is adjacent to two of its vertices.* Neither "component", nor `S`, nor `T` is needed (only `u ≠ c`, which `u ∈ T`, `c ∈ S` supplies). |
| 8 | **G38 Lemma 5** (at most one `T`-vertex adjacent to both ends of a `K₂` component) | `{a,b}` a `K₂` component; `T` | **`C4`-freeness alone** | **STATEMENT NARROWER THAN PROOF**, radically: this is a verbatim restatement of `\|N(a) ∩ N(b)\| ≤ 1`, i.e. of the definition of `C4`-free. No structure of `S`, `T` or the component is used. Correct, but it is a definition-unfolding, not a lemma. |
| 9 | **G38 Lemma 6** (`u ∈ T`, `d_S(u) = 2` ⟹ its `S`-neighbours are a `K₂` component) | `u ∈ T`; `d_S(u) = 2`; otherwise none as printed | Lemma 1's **proof** applied to `u ∈ T` (peripherally 3-capped + `C4`-free), Lemma 3, Lemma 4 | **WIDER THAN PROOF as printed** (row 4). Also **B5**: the citation "By Lemma 1 applied to `u`" is wrong — Lemma 1's *statement* yields only `d_S(u) ≤ 2`, whereas what is needed (both `S`-neighbours lie in one component `C₀` with `\|C₀\| ≤ 2`) comes from its *proof*, or from Lemma 2 generalised as in row 5. The mathematics is fine; the citation is not. |
| 10 | **R-B1(i) consequence** | connected; `C4`-free; `l > 4` | G38 (connected + `C4`-free + peripherally 3-capped ⟹ `l < 4`), contraposed. The contraposition needs only `l ≥ 4` | **STATEMENT NARROWER THAN PROOF** (free generality: `l ≥ 4` suffices). PG(2,3), with `l = 4.0` exactly, is a live instance of the extra range and is indeed not peripherally 3-capped (witness recomputed above). |
| 11 | **CE-1's conclusion** | (a) the bare `d = 3` statement is FALSE; (b) CE-1 does not refute the F4 form; (c) F4 is NECESSARY at `d = 3`; (d) the F4 form of the forced-Case-2 statement remains open | CE-1's own data support (a) and (b) exactly. (c) is inferred from (b) — a non-sequitur: "CE-1 fails to refute `X`" does not license "`X` is the right repair". (d) is a status claim with no proof at all | **(a), (b): EQUAL/correct. (c): overstated. (d): FALSE** — refuted by `H` (§3c). Repair: "*CE-1 shows the bare `d = 3` statement is false; a separate witness (`H`) shows the F4 form of the forced-Case-2 statement is also false, so the Case-2-forced regime needs a hypothesis other than F4.*" |
| 12 | **S-1** | `C4`-free; geodesic `u₀u₁u₂u₃`; `a(u₀) ≥ 3`; `a(u₃) ≥ 2`; usable `x` of `u₀` with `a(x) ≥ 4`; Case-2-forced | `C4`-freeness; the geodesic (only for `dist(u₀,u₃) = 3`, hence `x ≠ u₃`); `a(u₃) ≥ 2`; Case-2-forced; `x ∈ N(u₀)`. **`a(u₀) ≥ 3` and `a(x) ≥ 4` are never used**; nor is connectivity; nor is `x` being *usable* (any `x ∈ N(u₀)` works) | **STATEMENT NARROWER THAN PROOF.** The proof already gives: *`G` `C4`-free, geodesic `u₀u₁u₂u₃`, `a(u₃) ≥ 2`, any `x ∈ N(u₀)` such that every usable side-neighbour of `u₃` is adjacent to `x` ⟹ (i),(ii),(iii).* Verified on 325,916 instances of this weaker hypothesis set with zero failures. Reporting as an opportunity, not a defect. |

No row is **STATEMENT WIDER THAN PROOF** in a way that makes a *load-bearing* claim false.
The four rows so marked (4, 6, 9, and partly 5) are the proof-internal Lemmas 1, 3, 6, 2,
whose hypotheses are inherited from the enclosing `Suppose for contradiction` block; I
supplied the counterexample the audit asks for (`T*`, row 4) to show the inheritance is
doing real work and must be written down if these lemmas are ever quoted outside G38.

---

## 4. MANDATORY PROBE 2 — control cases

### 4a. Counterfactual availability

Every value below recomputed by me. `PG(2,3)` built as the 13 points / 13 lines of the
order-3 plane over `F₃³`; `PG(3,2)` as the 15 nonzero vectors of `F₂⁴` with the 35 triples
`{a,b,a⊕b}`; Petersen as 2-subsets of `[5]` under disjointness.

| control | recomputed data | which in-scope facts execute, and what they yield | which hypothesis fails **first** where they don't |
|---|---|---|---|
| **Petersen** | `n = 10`, 3-regular, `C4`-free ✔, every `a(v) = 3` (brute-force independence number = component count = `d − t`), `Σa = 30`, `l = 3.0`, `rad = diam = 2`, `path = 5` | **G38 executes** (`S = ∅` ⟹ vacuously peripherally 3-capped ✔) and yields `l < 4` ✔ (`3.0`). Lemmas 1–6 execute trivially with `S = ∅`, `k₃=k₂=k₁=0`. **F2 executes** at `d = 2` (`a(u₀) = 3 ≥ 3`, `a(u_d) = 3 ≥ 2`) and yields `path ≥ 5` — **tight**, `path = 5` | **G14, G36, G37 do NOT execute.** First failing hypothesis: *no geodesic of the required length* (`diam = 2 < 3`). Secondarily `a(x) ≥ 4` fails everywhere (`max a = 3`). This is the requested "in-scope lemma that does not execute on a control": **G36 does not execute on Petersen.** |
| **PG(2,3)** | `n = 26`, 4-regular, `C4`-free ✔, bipartite, every `a(v) = 4`, `Σa = 104`, **`l = 4.0` exactly**, `rad = diam = 3`, `path = 11` | **G37 executes**: 2,808 frames, *all* Case-1 (no Case-2-forced frame exists here) ⟹ `path ≥ 7` ✔ (`11`). **F3's `l = 4` analogue** executes with equality: `Σ_{a≥4}(a−3) = 26 = n` ✔. **R-B1(i)'s free-generality range** is witnessed here | **G38 and its Lemmas 1–6 do NOT execute.** First failing hypothesis: **peripherally 3-capped**. Explicit witness: the geodesic `(0,16,10,17)` has length `3 ≥ rad = 3`, and its end `u₀ = 0` carries the usable side-neighbour `x = 13` with `a(13) = 4 > 3`. **G36, G14 also do not execute**: no geodesic of length 4 or 5 (`diam = 3`). |
| **PG(3,2)/STS(15)** | `n = 50`, degrees `7` (15 points) and `3` (35 lines), `C4`-free ✔, `a(point) = 7`, `a(line) = 3`, `Σa = 210`, **`l = 4.2`**, `rad = 3`, `diam = 4` | **G36 executes**: 10,080 genuine `d = 4` frames (all Case-1) ⟹ `path ≥ 8`; I confirmed an induced path on `≥ 8` vertices exists. **G37 executes**: 2,520 frames ⟹ `path ≥ 7` ✔. **F3 executes** (`l = 4.2 > 4`): `Σ_{a≥4}(a−3) = 15·4 = 60 > 50 = n` ✔ | **G38 and Lemmas 1–6 do NOT execute.** First failing hypothesis: **peripherally 3-capped** — witness geodesic `(15,9,37,11)` of length `3 ≥ rad = 3`, end `u₀ = 15` (a line, `a = 3`) with usable side-neighbour `x = 3` (a point, `a = 7`). **G14 does not execute**: `diam = 4 < 5`. Consistent with `l = 4.2 ≥ 4` and with R-B1(i). |
| **CE-1** | `n = 10`, `m = 11`, `C4`-free ✔, `a = (2,1,3,1,2,4,2,1,1,2)`, `Σa = 19`, `l = 1.9`, `rad = 3`, `diam = 4`, `path = 6` | **G38 does not execute** (not peripherally 3-capped: geodesic `(0,9,4,6)`, `u₀ = 0`, `x = 5`, `a(5) = 4`), though its conclusion `l < 4` happens to hold. **G37 does NOT execute** on CE-1's single frame: the frame is Case-2-forced, so the extra hypothesis `y ≁ x` fails — **this is the second requested "does not execute" case, and it is the load-bearing one**: it is exactly why CE-1 is consistent with G37 rather than a refutation of it | For G37: first failing hypothesis is `y ≁ x` (the unique usable `y = 0` satisfies `0 ~ 5 = x`). For G36/G14: `d = 4` geodesics exist but the frame hypotheses fail (`a(u₀) ≥ 3` / usable `x` with `a(x) ≥ 4`). |
| **`H`** (new witness) | `n = 10`, `m = 14`, `C4`-free ✔, `a = (3,2,3,4,3,2,2,2,2,2)`, **`min a = 2`**, `Σa = 25`, `l = 2.5`, `rad = 2`, `diam = 3`, `path = 6` | Same profile as CE-1 for G37 (two frames, both Case-2-forced, so G37 does not execute), **but F4 now holds**, so no peeling escape exists | Not peripherally 3-capped (so G38's chain does not execute); no `d ≥ 4` geodesic (so G36/G14 do not execute); `y ≁ x` fails (so G37 does not execute). |

### 4b. Witness validation

Every graph named anywhere in this report was validated against **every** defining
constraint of the class it illustrates, in the order **simple → connected → `C4`-free →
`a`-values → geodesics → `path`**:

* Simplicity was checked from the edge list (no loops, no repeated pair) before anything else.
* `C4`-freeness was checked **first** among the graph properties, by the PART A definition
  ("no two distinct vertices have two common neighbours"), and for CE-1 and `H`
  *additionally* by exhaustive search for a 4-cycle as a subgraph. Both tests agreed.
  Negative control: the 4-cycle itself was fed to the checker and correctly rejected.
* `a`-values were computed **two independent ways** — brute-force independence number of
  `G[N(v)]`, and number of components of `G[N(v)]` — and cross-checked against `d(v) − t(v)`.
  All three agreed on every graph (which also re-validates F1 on each).
* Geodesics were validated by requiring `dist(uᵢ,uⱼ) = |i−j|` for **all** pairs, from BFS
  distances, not merely consecutive adjacency.
* `path(G)` for CE-1 and `H` was computed by brute force over **all** vertex subsets
  (checking each induces a path: connected, `Δ ≤ 2`, exactly two degree-1 vertices), not by
  the DFS routine used elsewhere — a deliberately independent second implementation.
* The peeled survivor graph of CE-1 was re-validated as a graph in its own right (6 vertices,
  all degrees 2, connected ⟹ `C₆`; all `a = 2`; `max a = 2`).

No witness I rely on contains a `C4`.

### 4c. Self-satisfying instances

| in-scope theorem | explicit instance satisfying **all** its own hypotheses | status |
|---|---|---|
| **G36** | `T36`: the tree on `n = 11` with edges `u₀u₁, u₁u₂, u₂u₃, u₃u₄, u₀x, u₀z, xw₁, xw₂, xw₃, u₄y`. Trees are `C4`-free ✔; connected ✔; `u₀…u₄` is a geodesic (unique path in a tree); `a(u₀) = 3` ✔, `a(u₄) = 2` ✔, `x` usable with `a(x) = 4` ✔. **`path = 8 = d + 4` exactly — the bound is tight** | **NOT vacuous** |
| **G37** | `T37`: the tree on `n = 10`, edges `u₀u₁, u₁u₂, u₂u₃, u₀x, u₀z, xw₁, xw₂, xw₃, u₃y`. `a(u₀) = 3`, `a(u₃) = 2`, `a(x) = 4`, and `y ≁ x` ✔ (Case 1). **`path = 7 = d + 4` exactly — tight**. Also PG(3,2) (2,520 Case-1 frames) and PG(2,3) (2,808) | **NOT vacuous** |
| **G38** | Petersen (`S = ∅`, `l = 3.0`); `C₇` (`rad = 3`, `l = 2.0`); `K_{1,4}` (`C4`-free ✔, `a = (4,1,1,1,1)`, `rad = 1`, peripherally 3-capped ✔, **`S = {centre} ≠ ∅`**, `l = 1.6`); and 133,780 peripherally-3-capped graphs with `S ≠ ∅` at `n ≤ 8` | **NOT vacuous**, and the counting chain is **not** degenerate — but see the caveat below |
| **S-1** | CE-1 and `H`, both of which satisfy S-1's full hypothesis list (Case-2-forced `d = 3` frames); (i),(ii),(iii) verified on all three frames | **NOT vacuous** |
| **CE-1's conclusion** | CE-1 itself | **NOT vacuous** |

**Caveat worth recording (not a defect).** I searched hard for peripherally-3-capped
`C4`-free graphs with a rich `S`. Across all 3,152,456 such graphs with `n ≤ 8` (exhaustive)
and a further 15,538 with `S ≠ ∅` found in 300k random samples up to `n = 17`, the largest
`|S|` I ever found was **3**, and the `(k₃,k₂,k₁)` profiles seen were `(0,0,1)` (14,357),
`(0,1,0)` (1,180) and `(1,0,0)` (**once**). So Lemma 4's `K₃` branch is reachable but extremely rare, and I could not
produce a peripherally-3-capped graph anywhere near the regime the counting chain is
designed to contradict. **This does not weaken the proof** — a correct case that is rarely
instantiated is still correct — but it does mean G38's machinery is, empirically, far
stronger than the class it is applied to, and the theorem may have a much shorter proof.
For the record I did exhibit an instance exercising Lemmas 2/5/6 non-trivially: an `n = 17`
graph with `S = {0,5}` forming a `K₂` component of `G[S]`, `rad = 4`, `l = 1.882`,
`\|T₂\| = 0 ≤ k₂ = 1`, `E(S,T) = 7 ≤ k₂ + n − |S| = 16` — all validated as in §4b.

---

## 5. Confirmed defects, classified

| id | where | defect | class |
|---|---|---|---|
| **B1** | C.4, closing sentence | "*the F4 form of the forced-Case-2 statement remains open*" is **FALSE** — refuted by `H` (`n = 10`, minimal). The accompanying inference "*Therefore F4 … is NECESSARY at `d = 3`, not a convenience*" is an overstated remark: CE-1 shows only that the bare statement needs strengthening, and F4 is now known not to be a strengthening that works | **BOOKKEEPING** (status line + overstated remark; nothing in scope consumes it; repairing it leaves G36, G37, G38, S-1 and CE-1's own verification intact). Flagged as the one borderline item. |
| **B2** | G36 Step 2; G37 subcase 1a | the chord `x ≁ u₁` is missing from both chord lists (Step 2 gives 20 of 21 pairs, 1a gives 14 of 15). The fact is true and immediate (`x` lies outside `u₁`'s component of `G[N(u₀)]`), and G36 Step 2 even cites it parenthetically inside another justification — it is simply not listed | **BOOKKEEPING** |
| **B3** | G36 distinctness paragraph | "`y ∉ {u₂,u₃}` since `y ≁ u₃`" — non-adjacency does **not** imply distinctness (no vertex is adjacent to itself), so this is not a reason for `y ≠ u₃`. Correct reason: `y` is chosen outside `u₃`'s component of `G[N(u₄)]`, and `u₃` lies in that component. The paragraph also omits `w_y ≠ z`, `w_y ≠ u₃`, `z ≠ y`, `z ≠ u₂,u₃,u₄`. All are true | **BOOKKEEPING** |
| **B4** | G37, all three subcases | no distinctness statement at all for the 7 vertices. All are distinct (proved in R-M3 above) | **BOOKKEEPING** |
| **B5** | G38 Lemma 6 | "*By Lemma 1 applied to `u`*" — Lemma 1's **statement** only yields `d_S(u) ≤ 2`; what is needed is that both `S`-neighbours lie in a single component `C₀` of `G[N(u)]` with `|C₀| ≤ 2`, which is in Lemma 1's **proof** (or in Lemma 2 once `v ∈ S` is dropped). Citation error, not a mathematics error | **BOOKKEEPING** |
| **B6** | G38 Lemma 2 | stated for `v ∈ S`; the proof never uses it. The unused generality is exactly what Lemma 6 needs (`u ∈ T`), so this is a citation trap waiting to be tripped | **BOOKKEEPING** (opportunity) |
| **B7** | G38 Lemma 3 | the cycle/path case is closed by "*acquires chords producing a `C4`*", spelled out only for `k = 4`. The uniform and immediate reason is that the forced chord gives a `G[S]`-vertex degree 3, contradicting `Δ(G[S]) ≤ 2` from Lemma 1. The printed route is valid but under-argued for `k ≥ 5` | **BOOKKEEPING** |
| **B8** | G38 Lemma 1 | the degenerate case `rad = 0` (⟺ `n = 1`) is not covered: the "geodesic" has length 0, has no `u₁`, and "3-capped" is undefined for it. Harmless (`a(v) = 0`, `S = ∅`) | **BOOKKEEPING** |
| **B9** | R-B1(i) | correct as stated, but (α) the proof supports `l ≥ 4` not just `l > 4` (free generality; PG(2,3) witnesses the extra range), and (β) the consequence yields `a(u₀) ≥ 2` only and says nothing at the far end, so it does **not** by itself supply the `a(u₀) ≥ 3` / `a(u_d) ≥ 2` that G14/G36/G37 require. Reading it as the chain's input would be an error downstream | **BOOKKEEPING** |
| **B10** | PART B, **F4** (context item, reported under the brief's carve-out) | "*raises `Σ_v a(v) − 3n` by exactly 1 per deletion*" is **FALSE for triangle-leaves**. If `N(v) = {p,q}` with `p ~ q` and `a(v) = 1`, deleting `v` leaves `a(p)` and `a(q)` **unchanged** (in `G[N(p)]`, `q` merely goes from matched to isolated — same component count), so `Σa` drops by 1 and `Σa − 3n` rises by **2**. Concretely verified on CE-1: the three leaf deletions took `Σa − 3n` from `−11 → −10 → −9 → −8` (`+1` each), and deleting the triangle-leaf `8` took it `−8 → −6` (`+2`). **Nothing in scope depends on the exact increment** — R-B2 uses peeling only to show CE-1's frame is destroyed, and `≥ 1` suffices for the intended `l > 4` preservation — so this is *not* an in-scope mathematics defect. Correct statement: "raises it by 1 or 2 per deletion, hence by at least 1" | **BOOKKEEPING** (context) |

**No MATHEMATICS defect confirmed in scope.** In particular I found nothing wrong,
unjustified, or insufficient in any step of G36, G37, G38, or S-1.

---

## 6. Out of scope, noticed anyway

*(Does not drive the verdict.)*

1. **The research consequence of `H`.** With the F4 form of the Case-2-forced `d = 3`
   statement now false, the `d = 3` gap is not a matter of finding the right routine
   hypothesis — `H` and CE-1 are structurally similar (both have `path = 6`, both have a
   unique usable `y ∈ N(x) ∩ N(u₃)`), and S-1 says every Case-2-forced frame looks like
   this. A hypothesis that excludes `H` will need to bite on something S-1 does *not*
   already give; `min a ≥ 2` is not it. This looks like the highest-value place to point
   the next attack, and S-1 (which is correct) is the right map for it.
2. **G36 and G37 are tight.** My self-satisfying tree instances achieve `path = d + 4`
   exactly, so neither lemma can be improved to `d + 5` without extra hypotheses.
3. **F2 is tight on Petersen** (`path = 5 = d + 3` at `d = 2`), and **F3's `l = 4`
   analogue is tight on PG(2,3)** (`Σ_{a≥4}(a−3) = 26 = n` exactly). Both are pleasant
   sanity anchors for the background facts.
4. **G38's proof is likely much stronger than needed** (see §4c caveat): I could not find
   a peripherally-3-capped `C4`-free graph with `|S| > 3`, and the `K₃` profile occurred
   once in ~150k samples. A direct argument that peripherally-3-capped forces `|S|` small
   might replace the whole counting chain.
5. **PG(2,3) sits exactly on the boundary** (`l = 4.0`) and is not peripherally 3-capped,
   which is the sharpest available demonstration that G38's `l < 4` (rather than `l ≤ 4`)
   is the right conclusion — the `l = 4` case is genuinely inhabited and genuinely excluded.
6. I have **not** searched the literature (per the isolation rules) and express no view on
   whether any of this is known.

---

## 7. Self-audit

**(i) What I am less than certain about.**

* **The classification of B1**, and only that. `H` is certain — I re-verified it with a
  second, independent implementation, and it reproduces 132 times in independent random
  search — but whether "a refuted *status claim* about an unproved side-statement" counts
  as MATHEMATICS or BOOKKEEPING is a taxonomy call, not a mathematics call. I applied the
  brief's own operational test (*does the repair leave every proof intact?* — yes) and
  classified it BOOKKEEPING, therefore leaving the bit at NO. I want this visible rather
  than buried: **if the gate operator's convention is that a refuted in-scope assertion
  flips the bit regardless of load-bearing status, then the bit should read YES, and R-B2
  is where it comes from.** Nothing about G36, G37 or G38 changes either way.
* **The claim that `H` is minimum-order.** The `n ≥ 9` half is a hand argument (the nine
  frame vertices `u₀,u₁,u₂,u₃,x,z,w₁,w₂,w₃` are pairwise distinct); the `n = 9` half is an
  exhaustive enumeration of the 2¹⁴ completions of the forced skeleton. I believe both, but
  the skeleton derivation assumed `a(x) = 4` exactly at `n = 9` (correct, since `a(x) ≥ 5`
  needs a fourth `w`) and that all nine vertices are used. If either step is off, `n = 9`
  might still be possible. This does not affect the refutation itself.
* **The `rad = 0` reading (B8)** depends on how one reads "geodesic of length ≥ rad" when
  the geodesic has a single vertex. I treated "3-capped" as undefined there rather than
  vacuously true. Under the vacuously-true reading, B8 evaporates. Either way `S = ∅` when
  `n = 1`, so Lemma 1 holds.
* **G36/G37 have proofs I checked line by line and could not break, plus large-scale
  machine corroboration — but corroboration is not proof.** My searches reached `n ≤ 18`
  and are biased toward the constructions I could imagine; a counterexample living at large
  `n` or in a structure my generators never produce would have been missed.

**(ii) Which hypotheses I used where.**

* `C4`-freeness in the **strong** (subgraph, not induced) form of PART A throughout — every
  `|N(u) ∩ N(v)| ≤ 1` step in G36, G37, S-1 and Lemmas 2/4/5/6 consumes it, and F1
  (`a = d − t`, `|C₀| ≤ 2`) consumes it in Lemma 1.
* The **universal** quantifier in "peripherally 3-capped" is what licenses Lemma 1
  (R-M1(a)); with "some geodesic" the licensing would fail.
* `d = 4` exactly is consumed twice in G36 Step 1 (the zero `u₄`-kill, and `x ≁ y`);
  `y ≁ x` replaces the second of these at `d = 3` in G37, and is used in exactly four places.
* `a(u₀) ≥ 3` is consumed only to produce `z` (G36 Step 3, G37 subcase 1b) and nowhere in
  Step 2 / subcase 1a; `a(x) ≥ 4` is consumed only for the three-non-`u₀`-components count;
  `a(u_d) ≥ 2` only to produce `y`.
* Connectivity is consumed in G38 (finite `rad`, `n ≥ 1`) and **not** in G36, G37, S-1.
* `n ≥ 1` is consumed in G38's endgame (`3n < 4n`).

**(iii) What I could NOT check, and why.**

* **G14 was accepted as a black box**, as the brief instructs. I did not verify it; I only
  confirmed it does not execute on any control (`diam ≤ 4` everywhere I looked), so nothing
  in my report leans on it.
* **F1, F2, F3 were used as context.** I re-verified F1 computationally on every graph I
  built (`a(v) = d(v) − t(v)` held universally, and `a` = component count = brute-force
  independence number), and I checked F2's and F3's numerics on the controls, but I did not
  referee their proofs.
* **F4's peeling reduction is not proved in the brief** (it is cited as "a proved peeling
  reduction"). I verified its *effects* on CE-1 concretely (connectivity, `C4`-freeness and
  distances among survivors are preserved; the process terminates with `min a ≥ 2`) and I
  found the arithmetic clause to be wrong (B10), but **I could not check the general
  reduction**, only the CE-1 instance and the two deletion types by hand.
* **`path(PG(2,3))` I computed as 11; `path(PG(3,2))` I did NOT compute** (`n = 50` is out
  of reach for exhaustive induced-path search). For PG(3,2) I only certified that induced
  paths on `≥ 8` and `≥ 7` vertices exist, which is all G36/G37 predict there.
* **Exhaustive enumeration reached `n ≤ 8` only** (3,361,196 connected `C4`-free labelled
  graphs in total, of which 3,152,456 peripherally 3-capped; at `n = 8` alone, 3,249,352
  and 3,042,712 respectively). Beyond that everything is random or
  structured search. No `C4`-free graph with `l > 4` other than PG(3,2) was available to me,
  so **R-B1(ii)'s empirical premise ("all known `l > 4` examples have `rad ≤ 4`") I could
  neither confirm nor refute** — I have exactly one data point, and it is consistent.
* **I did not attempt to settle the open question** of whether `C4`-free ∧ `l > 4` forces
  `rad ≤ 4`, nor whether a Case-2-forced `d = 3` statement is rescuable by some other
  hypothesis. `H` shows F4 is not that hypothesis; it says nothing about what is.
* **No SAT/SMT** was used (prohibited), **no internet**, and **no file in the repository
  other than the brief** was opened. Every number above was recomputed from the PART A
  definitions by code I wrote and calibrated on hand-checked graphs.
