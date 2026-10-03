STATUS: PARTIAL — no coefficient improvement (delta > 0 NOT obtained; the 1/3 target stays OPEN). Proved: M >= ceil(n/3) for every n (a +1 over Szemerédi exactly when n ≡ 1 mod 3), via an exact "defect identity" plus a farthest-circle lemma. Also: exact obstructions, an exactly verified n = 8 configuration, and small-n values.

# Erdős #1082: clean-room probe (distinct distances from one point, no three collinear)

Date: 2026-10-03. Clean-room conditions: no literature, no web, no repository files. Only this brief and standard mathematics were used.
Priority and novelty are **unchecked**: no G2/literature check was done. The results in Section 1 are elementary, and something equivalent may already be known.
Verification level: Sections 1–2 are hand proofs by a single model. Nobody else has reviewed them, and nothing is formalized. Section 4 gives the numerics and says for each item whether it is exact or floating-point.

---

## 0. Setting, notation, exact conventions

* `P` is a set of `n >= 3` points in R^2, with no three collinear.
* For `p ∈ P`, the *classes* of `p` are the nonempty level sets of `q ↦ |pq|` on `P \ {p}`. `M(p)` is the number of classes. Their sizes are `a_1(p), …, a_{M(p)}(p)`, with `Σ_i a_i(p) = n − 1`. `M := max_p M(p)`.
* `A(p) := Σ_i C(a_i(p), 2)` is the number of unordered pairs `{q, r} ⊂ P \ {p}` with `|pq| = |pr|`. We say `p` is an *apex* of the *base* `{q, r}`.
* Apexes of a base `{q, r}` lie on its perpendicular bisector, so there are at most 2 of them. `Z_j` (j = 0, 1, 2) is the number of bases (unordered pairs of P) with exactly `j` apexes. `Z_0 + Z_1 + Z_2 = C(n,2)`.
* `V_p := Σ_i (a_i(p) − 3)^2` is the class-size variance around 3.
* `R(p) := max_q |pq|` and `F(p) := {q : |pq| = R(p)}` (the farthest class). `h` is the number of vertices of conv(P).

**Double count (exact).** Each base is counted once for each of its apexes. Hence
`Σ_p A(p) = Z_1 + 2 Z_2 = n(n−1) − Z_1 − 2 Z_0`.  (DC)

Szemerédi's argument is (DC) together with `A(p) >= (n−1)((n−1)/M(p) − 1)/2` (Cauchy–Schwarz). It gives
`Σ_p (n−1)/M(p) <= 3n`. This bounds the **harmonic mean** of the `M(p)` by `(n−1)/3`, so `M >= ceil((n−1)/3)`.

---

## 1. Proved results

### Lemma 1 (pointwise identity)
For every `p`: `A(p) = (5/2)(n−1) − (9/2) M(p) + V_p / 2`.

*Proof.* For every integer `a`, `C(a,2) = 3 + (5/2)(a−3) + (1/2)(a−3)^2`. (Check a = 1, 2, 3, 4: 0, 1, 3, 6.) Sum this over the `M(p)` classes and use `Σ_i (a_i − 3) = n − 1 − 3M(p)`. ∎

### Proposition 2 (exact defect identity)
For every `P` with no three collinear:

```
9 · Σ_p M(p)  =  3 n (n−1)  +  D(P),      where   D(P) := Σ_p V_p + 2 Z_1 + 4 Z_0  >= 0.
```

*Proof.* Sum Lemma 1 over `p` and substitute (DC):
`(5/2)n(n−1) − (9/2)ΣM(p) + (1/2)ΣV_p = n(n−1) − Z_1 − 2Z_0`. Rearranging and multiplying by 2 gives the identity. ∎

Consequences, with exact quantifiers:

* (2a) `M >= (1/n)Σ_p M(p) = (n−1)/3 + D(P)/(9n)`. Szemerédi's bound is the case `D >= 0`.
* (2b) **Sufficient condition for the target.** If `D(P) >= 9 δ n^2` for every admissible `P` with `n >= n_0`, then `M >= (1/3 + δ) n − 1/3` for all such `P`. This even holds for the *average* of the `M(p)`.
* (2c) **Necessary structure of a counterexample family.** If `M <= (1/3 + ε) n`, then `D(P) <= 9 n M − 3n(n−1) <= 9 ε n^2 + 3n`. So all but at most `9εn^2 + 3n` of the roughly `n^2/3` pairs (p, class) are classes of size exactly 3, and at most `(9/2)εn^2 + (3/2)n` bases fail to have 2 apexes.

The identity checks numerically (exact integer equality) on six test sets: the n = 8 configuration of §2.2, the k-gon plus center for k = 5, 7, 9, the regular heptagon, and 12 random points.

### Lemma 3 (enclosing circles through >= 3 points)
Let `𝒟` be the set of closed disks `D` with `P ⊂ D` and `|∂D ∩ P| >= 3`. Then `|𝒟| <= h − 2`.

*Proof.* Take `D ∈ 𝒟` and set `B_D := ∂D ∩ P`. A disk is strictly convex, so every point of `B_D` is an extreme point of `P`, that is, a hull vertex. Let `Q_D := conv(B_D)`. This is a convex polygon with `k_D >= 3` vertices, all of them hull vertices of P.

*Separation.* Take distinct `D, D' ∈ 𝒟` with centers `c, c'` and radii `r, r'`. If `c = c'`, then `r ≠ r'`, say `r < r'`. Then `B_{D'} ⊂ ∂D'` lies outside `D`, which contradicts `P ⊂ D`. So `c ≠ c'`.
Let `f(x) := (|x−c|^2 − r^2) − (|x−c'|^2 − r'^2)`. This is a non-constant affine function.
For `x ∈ B_D`, `f(x) = 0 − pow_{D'}(x) >= 0` because `x ∈ D'`. For `y ∈ B_{D'}`, `f(y) = pow_D(y) <= 0`.
Hence `Q_D ⊂ {f >= 0}` and `Q_{D'} ⊂ {f <= 0}`, so the two polygons have disjoint interiors.

*Angle count.* At each hull vertex `v`, the polygons `Q_D` that have `v` as a vertex occupy pairwise disjoint angular sectors inside the interior angle `θ_v` of conv(P) at `v`. Therefore
`Σ_{D∈𝒟} (k_D − 2)π = Σ_D (sum of the angles of Q_D) <= Σ_v θ_v = (h − 2)π`.
Each term on the left is at least `π`. So `|𝒟| <= h − 2`. ∎

### Lemma 3' (enclosing circles through exactly 2 points)
Let `E_2` be the set of pairs `{a,b}` such that some closed disk `D ⊇ P` has `∂D ∩ P = {a,b}`. Then `|E_2| <= 2h − 3`. Moreover `#{p ∈ P : |F(p)| = 2} <= 2|E_2| <= 4h − 6`.

*Proof.* Apply the same separating affine function `f` to two such disks. Two segments `ab ≠ cd` from `E_2` could cross only at a point of `{f = 0}`, and then both segments would lie in `{f = 0}`. That forces `{a,b} = {c,d} = ∂D ∩ ∂D' ∩ P`, a contradiction. So `E_2` is a non-crossing straight-line graph on the `h` hull vertices, which are in convex position, and therefore has at most `2h − 3` edges.
If `F(p) = {a,b}`, then `p` lies on the bisector of `ab`. That bisector contains at most 2 points of `P`. ∎

### Theorem 4 (main proved result)
For every `n >= 2` and every set `P` of `n` points in the plane with no three collinear:

```
(1/n) Σ_p M(p)  >=  (n−1)/3 + (n − h + 2)/(9n)      and hence      M  >=  floor((n−1)/3) + 1  =  ceil(n/3).
```

When `n ≡ 1 (mod 3)` this is `M >= (n+2)/3`, one more than Szemerédi's `(n−1)/3`. For `n ≢ 1 (mod 3)` it coincides with the old bound.

*Proof.* If `|F(p)| >= 3`, the disk `D(p, R(p))` belongs to `𝒟`. Distinct `p` give distinct disks because the centers differ. By Lemma 3, `#{p : |F(p)| = 3} <= h − 2`. Every other `p` has a class, namely `F(p)`, of size different from 3, so `V_p >= 1`. Hence `D(P) >= Σ_p V_p >= n − h + 2 >= 2`. Proposition 2 then gives the average bound. In particular `max_p M(p) > (n−1)/3`, which implies `M >= floor((n−1)/3) + 1`. The case n = 2 is trivial. ∎

**Equivalent statement of the equality case.** Szemerédi's bound is attained exactly only if `n ≡ 1 (mod 3)` and every class of every point has size 3 (so every base has exactly 2 apexes). Theorem 4 shows that this configuration does not exist. The obstruction is only at the outermost level, because the farthest circles of the `n` points would give `n` distinct enclosing circles through 3 points, while at most `h − 2 <= n − 2` exist.

### Corollary 5 (small hull, n ≡ 0 mod 3)
If `n ≡ 0 (mod 3)` and `h < (n + 16)/10`, then `M >= n/3 + 1`.

*Proof.* Suppose `M <= m := n/3`. For each `p`, put `W_p := V_p + 9(m − M(p)) >= 0`. Proposition 2 gives `Σ_p W_p + 2Z_1 + 4Z_0 = 9nm − 3n(n−1) = 3n`.
Now bound `W_p` from below:
* If `M(p) < m`, then `W_p >= 9`.
* If `M(p) = m`, then `Σ_i (a_i − 3) = −1`, so `V_p >= 1`.
* If additionally `|F(p)| = 1`, the class `F(p)` contributes `(1−3)^2 = 4`, and the other classes have deviations summing to `+1`, so `V_p >= 5`.

By Lemmas 3 and 3', `#{p : |F(p)| = 1} >= n − (h−2) − (4h−6) = n − 5h + 8`. Hence `3n >= n + 4(n − 5h + 8)`, that is, `h >= (n + 16)/10`. ∎

(For `n ≢ 0 (mod 3)` the same bookkeeping gives nothing, because the slack `9nM − 3n(n−1)` is `2n` or `3n` while each `|F(p)| = 1` point costs only 1 extra unit. This is recorded as an obstruction, not a result.)

**Honest size of the gain.** Theorem 4 is a lower-order improvement: +1 on one residue class mod 3. Corollary 5 is +1 on another residue class, but only under a hull-size hypothesis. Neither touches the coefficient 1/3.

---

## 2. Exact obstructions (why the coefficient was not improved)

### 2.1 The Szemerédi inequality is asymptotically sharp for the harmonic mean
Take `P_k` = the regular k-gon (k odd) plus its center O, so `n = k + 1`. It has no three collinear points: k is odd, so no two vertices are antipodal, and the line through O and a vertex meets the opposite edge at its midpoint.
* `M(O) = 1`, and `M(v) = (k+1)/2` for every vertex v.
* Every vertex pair has exactly 2 apexes (O and the vertex opposite the pair).
* Every pair `{O, v}` has 0 apexes, because a chord of length R would need `j/k = 1/6`, which is impossible for odd k.

So `Z_2 = C(k,2)`, `Z_1 = 0`, `Z_0 = k`, and the harmonic mean of `M(p)` is `n^2/(3n−2) = (n−1)/3 + 5/9 + O(1/n)`. This was checked numerically for k = 5…15.

Consequence: **any argument whose only output is the inequality `Σ_p 1/M(p) <= 3n/(n−1)` (or any inequality that P_k satisfies up to O(n)) cannot improve 1/3.** The improvement has to use the gap between max and harmonic mean, that is, balance.
Proposition 2 does this: P_k has `D ≈ n^2`, coming from `V_O = (k−3)^2`.

### 2.2 Saturation + perfect balance happens (n = 8), so class-size variance must be used
Take two concentric squares rotated by 45° with radius ratio `1/(2 sin 15°)`. Explicit coordinates, all in Q(√3):

```
(-1/2, 1-√3/2), (-1/2, -√3/2), (-(1+√3)/2, -(√3-1)/2), (-√3/2, 1/2),
((1-√3)/2, (1-√3)/2), (-√3/2, -1/2), (-1, 0), (0, 0)
```

Verified in **exact arithmetic** over Q(√3), with numbers represented as `a + b√3` and Fraction coefficients:
* no three collinear;
* `M(p) = 3` for all 8 points, with class sizes `(4,2,1)` at every point;
* **all 28 bases have exactly 2 apexes**: `Z_0 = Z_1 = 0`, `A(p) = 7 = n − 1` for every `p`;
* the whole defect is variance: `D = Σ V_p = 8·6 = 48`;
* across the 28 connecting lines, the mirror-line counts are `s(L) ∈ {0,1,3}` with multiplicities 8, 16, 4.

Consequences:
* `⌊n/2⌋ = 4` fails at n = 8. (The brief already says the ⌊n/2⌋ conjecture is false.)
* An argument that only produces deficient bases (`Z_0, Z_1`) from "every point is an apex of ≈ n bases" cannot work at n = 8. Any proof of `D >= c n^2` must use class-size variance.

### 2.3 A two-ring family with M = n/2 − 1 (context for the upper side)
Fix `k ≡ 0 (mod 4)`. Let `P = {e^{2πij/k}} ∪ {ρ e^{iπ(2j+1)/k}}` with `ρ = √(1 + cos^2(π/k)) − cos(π/k)`. Then `n = 2k` and **M <= k − 1 = n/2 − 1**, proved below assuming no three points are collinear.

*Proof.* A ring-0 point sees `k/2` chord values on its own ring and `k/2` cross values `1 + ρ^2 − 2ρcos((2b+1)π/k)`. The choice of ρ makes the chord with `a = k/4` (squared length 2) equal the cross value at angle `π − π/k`, which is one merge. The ring-1 coincidence (ring chord `2ρ^2` equals the cross value at angle `π/k`) is **the same quadratic** `ρ^2 + 2ρcos(π/k) − 1 = 0`. By rotational symmetry, every point has at most `k − 1` classes. ∎

No three collinear: checked in float64 for every `k ≡ 0 (mod 4)` with `k <= 100`. The minimum |cross product| is `>= 3.7e−5` for unit-scale points. k = 4…12 was rechecked at 50–60 digits. There is no general proof of non-collinearity.
For these sets the average of `M(p)` is about n/2, so `D ≈ 1.5 n^2`; the family is far from the 1/3 regime.

### 2.4 Exact Szemerédi equality is locally consistent at every single point
In the hypothetical `D = 0` world, every class is a triangle with circumcenter `p`. Each pair of `P` lies in exactly 2 such triangles. For each `q`, the map "triangle containing q ↦ its circumcenter" is a bijection onto `P \ {q}`. The "link" of `q` is a 2-factor whose consecutive centers `c, c'` satisfy `σ_{cc'}(q) ∈ P` (reflection in the line `cc'`).

These constraints can be satisfied at any one point. Take `p` at the origin, and the other `n − 1` points (with `n − 1` odd) at the angles of a regular `(n−1)`-gon, with radius constant on each class triple. Then the bisector of every pair inside a class passes through `p` and through the vertex `j` with `2j ≡ a + b (mod n−1)`, so every such base has exactly 2 apexes.
**So any contradiction must be global.** The only global contradiction found here is the farthest-circle count, and it is an `O(n)` defect, not `Ω(n^2)`.

### 2.5 The circle-depth (order-k Voronoi / k-set) route gives at most O(n) defect
In the `D = 0` world, the class circles at outer level `s` would give `n` distinct circles through 3 points with exactly `3s` points of `P` outside.
For sets in general position (no 4 cocircular), the counts `E_j` (circles through 3 points with exactly `j` inside) satisfy `E_j + E_{n−3−j} = 2(j+1)(n−j−2)`. This is checked numerically for n = 9, 12, 15 on random and convex-ish sets. It is the planar lift of the j-facet count for 3-D convex position.
Already for `t >= 0` outside points, the upper bound `E_{n−3−t} <= 2(t+1)(n−t−2)` is `>= n`, so the identity alone forces nothing.
The level `t = 0` is forced only by the extra input `E_0 >= n − 2` (Delaunay triangles). That is Lemma 3.
For `t >= 3` one would need lower bounds `E_t >= (2t+1)n − O(t^2)`, which are false in general: the convex-ish test sets have `E_t ≈ E_{n−3−t}`.
Two further caveats:
* The tight configuration may contain 4 cocircular points, where the identity needs a perturbation argument.
* Under approximate equality (`D = o(n^2)`), class levels stop aligning with depth.

**Dead end for δ > 0.**

### 2.6 Incidence and kite routes see only orders of magnitude
`Σ_L s(L) = Z_2`, where `s(L)` is the number of mirror pairs of `P` across the connecting line `L`. Point–bisector incidence bounds (Szemerédi–Trotter type) give `O(n^2)` with unspecified constants and cannot see the constant 2. Section 2.2 shows `Z_2 = C(n,2)` exactly at n = 8.
The constraints found are all `O(n)` in size:
* hull edges have `s(L) = 0`;
* lines with `j` points on one side have `s(L) <= j`;
* under "no 4 cocircular", `s(L) <= 1` (two mirror pairs form an isosceles trapezoid, which is cocircular).

These give `Z_0 + Z_1 >= h` in the no-4-cocircular case. That changes D by `O(n)` only.

### 2.7 Nearest-neighbour level
In the `D = 0` world, the minimum-distance graph would be 3-regular on its support. The angle (>= 60°) and planarity constraints do not exclude this. The farthest-distance graph *is* excluded (Hopf–Pannwitz style / Lemma 3). The nearest level gives nothing.

### What a δ > 0 proof would need (precise reformulation)
By (2b), it suffices to prove `D(P) = Σ_p Σ_i (a_i(p) − 3)^2 + 2Z_1 + 4Z_0 >= c n^2` for every admissible `P`.
Equivalently, rule out sets with no three collinear in which all but `εn^2` of the (point, class) pairs are 3-point circles centered at the point, and all but `εn^2` perpendicular bisectors of pairs pass through 2 points of `P`.
Sections 2.1 and 2.2 show that each of the two slack sources can vanish separately (at the level `O(n)`, resp. exactly at n = 8). Nothing here decides whether they can vanish **simultaneously** up to `o(n^2)`; Theorem 4 only rules out vanishing *exactly*. This is the exact open core.

---

## 3. Small n: what is known after this probe

| n | proved lower bound | best construction found (M) | status |
|---|---|---|---|
| 3 | 1 | 1 (equilateral) | exact 1 |
| 4 | **2** (Thm 4; old bound 1) | 2 (square) | exact 2 |
| 5 | 2 | 2 (regular pentagon) | exact 2 |
| 6 | 2 | 3 (regular hexagon; pentagon + center) | M = 2 numerically excluded (see §4.3), **not proved** |
| 7 | **3** (Thm 4; old bound 2) | 3 (regular heptagon) | exact 3 |
| 8 | 3 | 3 (two squares, §2.2, exact) | exact 3 |
| 9 | 3 | 4 (regular 9-gon) | open in {3,4} |
| 10 | **4** (Thm 4; old 3) | 5 (regular 10-gon; 9-gon + center) | open in {4,5} |
| 11 | 4 | 5 (regular 11-gon) | open in {4,5} |
| 12 | 4 | 6 (regular 12-gon; two rings) | open in {4,5,6} |
| 13 | **5** (Thm 4; old 4) | 6 (regular 13-gon) | open |
| 16 | 6 | 7 (two rings, k = 8, §2.3) | open |

"Proved" means proved in this note by a hand argument that nobody else has reviewed. Constructions for n = 8 are verified exactly. For n = 16 the verification is float plus 60-digit mpmath, with an exact algebraic identity for the coincidence.

---

## 4. Numerics (what was run, exactly)

All runs used python3 with numpy/scipy/mpmath, at most 2 threads, and no SAT/ILP solvers.

1. **Pool searches (simulated annealing over subsets, objective = max M + penalties).**
   * Triangular-lattice pools (exact integer arithmetic): the best results were *worse* than regular polygons. For example n = 10 gave M = 6. Lattices force collinear triples, and no-3-collinear subsets have few coincidences.
   * Cyclotomic pools `Z[ζ_12]`, `Z[ζ_10]` with coefficients in {−1,0,1} and radius <= 1.5 (float, tolerance 1e−7): found the n = 8, M = 3 set of §2.2, which was then re-verified exactly. Nothing beat ⌊n/2⌋ for n = 9…12.
   * A 24-direction multi-ring pool performed poorly (SA too weak); no information from it.
   * These searches are heuristic and give **upper bounds only**.
2. **Two-ring scan.** Two concentric regular k-gons with offset `πφ/(2k)` for φ = 0..3, optional center, and every radius ratio that creates at least one coincidence of the form chord = cross distance (k <= 12). A second scan with offset π/k covered k <= 30. Best: M = n/2 − 1 exactly when `k ≡ 0 (mod 4)`. There were also sporadic hits: k = 10 (golden ratio, M = 9), k = 21 (M = 20), k = 30 (M = 29). Section 2.3 gives the general mechanism.
3. **n = 6, M = 2 (structure enumeration + numerical realizability).**
   * Enumerated every assignment of a class partition of type (3,2), (4,1) or (5) to each of 6 points.
   * Pruned by two necessary geometric conditions: at most 2 apexes per base, and no 3-set inside a class of two different centers (two circles share at most 2 points). 13,152 labelled structures survive, which is **29 up to relabelling**.
   * Each structure was solved by Levenberg–Marquardt on its distance-equality system (fixing two points at (0,0) and (1,0)). There were 3000 random starts per structure, and success meant residual < 1e−11 plus non-degeneracy (no coincident points, no three collinear).
   * **No structure was realized. In fact no exact solution was found at all, degenerate or not.**
   * Calibration: the same pipeline at n = 5 (82 structures, 400 starts) does recover the regular pentagon.
   * Conclusion: strong numerical evidence that the minimum M for n = 6 is 3. This is **not a proof**; a certified algebraic elimination for the 29 systems would close it.
4. **Exact checks.** The n = 8 set in Q(√3), with exact rational arithmetic on `a + b√3`. The defect identity (Prop. 2) is an exact integer equality on six test sets. The circle-depth identity in §2.5 was checked on 9 random/convex sets.

Minimal exact-check recipe for §2.2: represent each coordinate as `(a, b)` meaning `a + b√3` with `a, b ∈ Q`. Compute the squared distances `dx^2 + dy^2` using `(a,b)(c,d) = (ac + 3bd, ad + bc)`. Group them by exact equality, and test collinearity by an exact zero cross product.

---

## 5. Routes tried and their exact status

| route (from brief) | outcome | exact obstruction |
|---|---|---|
| (1) kites / two apexes per base | reformulated: `Z_2 = Σ_L s(L)`; hull edges have s = 0 | saturation `Z_2 = C(n,2)` occurs exactly at n = 8 (§2.2); incidence bounds lack the constant (§2.6) |
| (2) apex + base with class-size weights | reduced to the identity of Prop. 2, so any weighting is subsumed by the variance term | the class-size variance must be forced to be Ω(n^2); no mechanism was found |
| (3) second moment over classes | this *is* Prop. 2 (V_p is the second moment around 3) | same as (2) |
| (4) near-extremal "all classes size 3" geometry | **exact case refuted** (Thm 4); approximate case open | only the outermost level is constrained (Lemma 3; §2.5); the structure is locally consistent at every point (§2.4) |
| farthest-circle counting with hull size | Cor. 5 (n ≡ 0 mod 3, small hull) | linear defect only |

---

## 6. Cost

* Compute: about 45 CPU-minutes in total on at most 2 threads, mostly the SA pool searches and the n = 6 realizability runs (29 structures × 3000 LM starts). No paid resources, no network, no solvers.
* Single clean-room probe; no agents were spawned and nothing was posted.
