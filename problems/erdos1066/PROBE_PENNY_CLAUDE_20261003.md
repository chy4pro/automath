STATUS: OPEN — no constant c > 8/31 was proved, so nothing reaches the current bar c > 6/23 (about 0.26087). The probe produced proved lemmas about the structure of a minimal counterexample, exact finite checks, a verified 4-chromatic penny graph with alpha/n = 6/19, and a list of obstructions. None of these is a new lower bound for alpha.

# Erdős #1066 (penny graphs, independence number): clean-room probe, 2026-10-03

Rules followed: no web access, no papers, no repository files read. Only the brief, standard mathematics and my own computations were used. No agents were spawned and nothing was posted.

Mid-task bar update from the coordinator: unrefereed manuscripts reportedly claim alpha >= ceil(7n/27) and alpha >= ceil(6n/23). A hit now means a proved c > 6/23. **My method is stuck below even 8/31.** I did not reconstruct a complete minimal-counterexample proof of any constant above 1/4. What I can prove is listed in Section 2 and what blocks each route is in Section 4.

---

## 0. Summary (10 lines)

1. An exact framework (Lemma 1): alpha >= cn holds for all penny graphs iff every nonempty penny graph has a nonempty independent set I with |N[I]| <= |I|/c. For c = m/(4m-1) the condition reads "savings" s(I) := 4|I| - |N[I]| >= |I|/m. So 8/31, 7/27, 6/23 and 5/19 correspond to m = 8, 7, 6, 5.
2. Proved: a boundary-turning lemma (Lemma 4) and an alternating-boundary lemma (Lemma 5). If delta >= 3 and the outer face is a chordless simple cycle of length b, some alternate set I of boundary vertices has s(I) >= 3 (b even) or s(I) >= 2 (b odd). Corollary: a minimal counterexample for c = m/(4m-1) of this shape has b >= 6m+2 (b even) or b >= 4m+3 (b odd). For 6/23 that means b >= 38 or b >= 27.
3. Proved: a segment version (Lemma 6) and an explicit reducible "closed 120° lattice corner of depth 4" (Lemma 7: 5 vertices, s = 1).
4. Proved: in a chain of rhombi (pairs of unit triangles) sharing tips, each hinge turns by at most 60°. Chains of k <= 5 rhombi have end tips at distance >= sqrt3 (Lemma 8). So a "5-rhombus Moser ring", which would give exactly 5/16, is NOT realizable.
5. Verified construction: a 6-rhombus ring with one closing contact. It has n = 19, is 4-chromatic and has alpha = 6. The alpha upper bound is proved by hand and the realizability is checked numerically with margin 0.0767. So alpha/n = 6/19, about 0.3158, which is above 5/16. I could not reconstruct the 5/16 family clean-room.
6. Exact computations (own exhaustive search, cross-checked against brute force) of the smallest independent set with s >= 1 in lattice hexagons of side S. Results: S = 3, 4 give 3; S = 5, 6 give 4; S = 7, 8, 9, 10 give 5. For S = 7, s >= 2 needs 7 vertices and s >= 3 needs 8. Hence "a set of size <= 4 with s >= 1 always exists" is false, and the savings-1 framework cannot go below m = 5.
7. Searches for a global obstruction (a penny graph with no small good set) found none. This covered lattice discs, lattice hexagons, dodecagonal square–triangle patches, hexagon-plus-square-shell patches, and annealing in the 30°/15° direction worlds. The best such graphs have minimal good-set size 3–5.
8. Failed routes, with exact obstructions in Section 4:
   - local savings-1 sets;
   - boundary-alternating sets;
   - a potential-function induction alpha >= cn + lambda·Σ(6-d) (K3 against an interior step forces c <= 5/23);
   - random lattice-phase colouring, which proves alpha >= n1/3 - f1/9 but drops to 2/9 on the 3.4.6.4 tiling and to 0 on the snub square tiling.
9. No LP/discharging computation was carried out. I could not make the local-configuration space finite in this session, so there are no extracted rules to report. The sanity check against 5/16 is satisfied trivially, because no c above 8/31 is claimed.
10. Cost: about 15 CPU-minutes of Python (numpy/scipy, at most 2 threads), no SAT/ILP solvers, no paid resources.

---

## 1. Setting and the exact framework

P is a finite set of points in R^2 with pairwise distances >= 1. G = G(P) joins the pairs at distance exactly 1. Every induced subgraph of a penny graph is a penny graph (take the sub-point-set).

Notation:
- N(I) is the set of vertices outside I that have a neighbour in I; N[I] = I ∪ N(I).
- The *savings* of an independent set I is s(I) := 4|I| - |N[I]|.
- tau-angles: for a vertex v on a simple outer cycle C with interior angle theta_v in (0°, 360°), let tau_v := 180° - theta_v. Then Σ_{v in C} tau_v = 360° (exterior angles of a simple polygon).

**Lemma 1 (exact equivalence).** Fix c in (0,1]. The following are equivalent:
(i) alpha(G) >= c|V(G)| for every penny graph G;
(ii) every penny graph G with V(G) nonempty has a nonempty independent set I with |N[I]| <= |I|/c.

*Proof.*
- (ii) ⇒ (i), by induction on n = |V(G)|. The case n = 0 is trivial. Take I from (ii) and let G' = G - N[I], which is a penny graph with fewer vertices. No edge joins I to V(G'), so alpha(G) >= |I| + alpha(G') >= |I| + c(n - |N[I]|) >= cn.
- (i) ⇒ (ii). A maximum independent set I is maximal, so N[I] = V(G). Then |I| = alpha(G) >= c|N[I]|. ∎

Two remarks. Since alpha is an integer, (i) gives alpha >= ceil(cn). For c = m/(4m-1), the inequality |N[I]| <= |I|/c is equivalent to s(I) >= |I|/m; call such an I *m-good*.

The lemma shows the framework loses nothing in principle. Every difficulty lies in finding *local* (bounded-size) good sets, which is what a finite case analysis needs. "Savings-1 sets of size <= m" is the special case s(I) >= 1 with |I| <= m.

Constants: m = 8 gives 8/31 ≈ 0.25806, m = 7 gives 7/27 ≈ 0.25926, m = 6 gives 6/23 ≈ 0.26087, m = 5 gives 5/19 ≈ 0.26316. The old m = 9 gives 9/35.

## 2. Proved lemmas

**Lemma 2 (local exclusions).**
(a) If d(v) <= 2 then s({v}) >= 1. So {v} is m-good for every m >= 1.
(b) For non-adjacent u, w: s({u,w}) = 6 - d(u) - d(w) + |N(u) ∩ N(w)|. So {u,w} is m-good (m >= 2) whenever |N(u) ∩ N(w)| >= d(u) + d(w) - 5. In particular, two degree-3 vertices at graph distance exactly 2 always form a good pair.
(c) If |vu| = |vw| = 1 and |uw| >= 1, then the angle uvw is at least 60°. Consequently, if all edges at v lie in a closed sector of angle theta, then d(v) <= 1 + floor(theta/60°).

*Proof.* (a) and (b) are direct counting: |N[{u,w}]| = d(u) + d(w) + 2 - |N(u) ∩ N(w)|. (c) is the law of cosines. ∎

**Lemma 3 (triangle runs).**
- Call a maximal sequence of consecutive unit triangles around v a run.
- A vertex v has at most 2 runs.
- If v has 2 runs, they contain at most 3 triangles in total and v has at most 1 free edge.
- If v has one run of t triangles (t <= 5), v has at most 4 - t free edges.
- A vertex in no unit triangle has degree <= 5.

*Proof.* A run of t triangles spans exactly 60t°. Distinct runs and the remaining edges are separated by angles strictly greater than 60° (an angle of exactly 60° creates a triangle, by Lemma 2(c) and the law of cosines). Write r for the number of runs and k for the number of free edges. Then 60(Σ t_i) + 60(r + k) < 360. ∎

**Lemma 4 (boundary turning).**
Hypotheses:
- G is a penny graph whose outer face is bounded by a simple cycle C.
Conclusions:
- For v in C, every edge at v lies in the closed interior sector of angle theta_v.
- Hence 4 - d(v) >= 3 - theta_v/60° = tau_v/60°.
- Therefore Σ_{v in C} (4 - d(v)) >= 6.

*Proof.* An edge leaving v into the open exterior sector would meet the outer face, which is impossible. Lemma 2(c) gives d(v) <= 1 + theta_v/60°. Then sum and use Σ tau_v = 360°. ∎

Consequences: every convex corner of C (tau_v > 0) has degree <= 3. If delta >= 3, convex corners have degree exactly 3 and tau_v <= 60°.

**Lemma 5 (alternating boundary set).**
Hypotheses:
- G is a penny graph with delta(G) >= 3.
- The outer face of G is bounded by a simple cycle C = v_0 v_1 ... v_{b-1}.
- C is chordless: no edge of G joins two non-consecutive vertices of C.
Conclusions:
(a) If b is even, one of I_0 = {v_0, v_2, ...} and I_1 = {v_1, v_3, ...} satisfies s(I) >= 3.
(b) If b is odd, some I_j = {v_j, v_{j+2}, ..., v_{j+b-3}} (indices mod b, (b-1)/2 vertices) satisfies s(I_j) >= 2.

*Proof.*
- Independence. The I-vertices are pairwise non-consecutive on C (b >= 4, since delta >= 3 rules out b = 3 with a chordless cycle). Chordlessness then gives independence.
- Every vertex of C is in I or C-adjacent to an I-vertex, so C ⊆ N[I].
- Each v in I has exactly two neighbours on C, so at most d(v) - 2 neighbours outside C. Hence |N[I]| <= b + Σ_{v in I} (d(v) - 2).
- Case (a), b = 2|I|. Then |N[I]| <= Σ_{v in I} d(v), so s(I) >= Σ_{v in I} (4 - d(v)) >= Σ_{v in I} tau_v / 60° by Lemma 4. The two classes together carry 360°, so one class carries at least 180°, giving s >= 3.
- Case (b), |I_j| = (b-1)/2. Then |N[I_j]| <= 1 + Σ_{I_j} d. So s(I_j) >= Σ_{I_j} tau / 60° - 1. Each vertex lies in exactly (b-1)/2 of the b sets I_j, so the average of Σ_{I_j} tau is 180°(b-1)/b. Hence some j has s(I_j) >= 3(b-1)/b - 1 = 2 - 3/b > 1, and since s is an integer, s >= 2. ∎

The lemma was validated numerically on 261 random penny clusters with delta >= 3 and simple chordless outer cycle, plus lattice hexagons. The total turning was 360° every time and the bound was never violated (Section 3.4).

**Corollary 5'.**
- Under the hypotheses of Lemma 5, G has an m-good set whenever b <= 6m (b even) or b <= 4m + 1 (b odd).
- A minimal counterexample to alpha >= m n/(4m-1) whose outer boundary is a chordless simple cycle therefore has b >= 6m + 2 (even) or b >= 4m + 3 (odd).
- For the 6/23 bar (m = 6) this means b >= 38 or b >= 27.

*Proof.* s >= 3 with |I| = b/2 is m-good iff b <= 6m. s >= 2 with |I| = (b-1)/2 is m-good iff b <= 4m + 1. ∎

**Lemma 6 (boundary segment).**
Hypotheses: as in Lemma 5, with 1 <= k and 2k <= b - 2.
Set-up:
- I = {v_0, v_2, ..., v_{2k-2}}.
- Let X be the number of odd-indexed v_{2i+1} (0 <= i <= k-2) that are *closed 120° corners*, meaning theta = 120° and d = 3.
Conclusion: s(I) >= Σ_{v in I} tau_v / 60° - 1 + X.

*Proof.*
- N[I] contains v_{-1}, ..., v_{2k-1}, which are 2k + 1 boundary vertices.
- Take a closed corner u = v_{2i+1}. Its third neighbour w lies at 60° from both C-edges, so w is adjacent to v_{2i} and v_{2i+2}. Also w is not on C, by chordlessness.
- So w is counted twice in Σ_{v in I}(d(v) - 2). If several closed corners share one w, the corresponding I-pairs are consecutive pairs of a path, and the overlap at w is |N(w) ∩ I| - 1, which is at least their number.
- Hence |N[I]| <= 2k + 1 + Σ_{I}(d - 2) - X, and s(I) >= Σ_I (4 - d) - 1 + X. Conclude with Lemma 4. ∎

**Lemma 7 (reducible closed 120° corner of depth 4).**
Set-up:
- Fix a vertex v and unit vectors e, w with angle(e, w) = 120°.
- Let p_{i,j} := v + i·e + j·w (i, j >= 0).
Hypotheses:
- All 15 points p_{i,j} with i + j <= 4 belong to P.
- d(v) = 3.
- d(p_{3,0}) = d(p_{0,3}) = 4.
Conclusion: I = {p_{0,0}, p_{3,0}, p_{2,1}, p_{1,2}, p_{0,3}} is independent with s(I) >= 1. So it is m-good for every m >= 5.

*Proof.*
- The pairwise distances in I are >= sqrt3, so I is independent.
- Each I-vertex has at most one neighbour outside {p_{i,j} : i + j <= 4}:
  - v has none.
  - p_{3,0} and p_{0,3} have degree 4 with three neighbours at level <= 4.
  - p_{2,1} and p_{1,2} have five lattice neighbours at level <= 4. The only position for a sixth neighbour is the lattice point at level 5, because it must be >= 60° from both angular neighbours that are 120° apart.
- So |N[I]| <= 15 + 4 = 19 = 4·5 - 1. ∎

Exhaustive search (Section 3.2) shows that in large lattice hexagons no independent set of size <= 4 has s >= 1. So size 5 is optimal for savings-1 sets at this corner.

**Lemma 8 (rhombus chains cannot curl fast).**
Set-up:
- R_1, ..., R_k are "rhombi" in a penny configuration. Each R_i is two unit equilateral triangles sharing an edge, with tips t_{i-1}, t_i at distance sqrt3.
- Consecutive rhombi share a tip.
Conclusions:
- At every hinge t_i (1 <= i <= k-1), the angle t_{i-1} t_i t_{i+1} lies in [120°, 240°]. Equivalently, the turning is at most 60° in absolute value.
- For k <= 5, |t_k - t_0| >= sqrt3 > 1.

*Proof.*
- The four middle vertices adjacent to t_i lie at directions a ± 30° and b ± 30°, where a and b point to t_{i-1} and t_{i+1}. Lemma 2(c) forces |a - b| >= 120° both ways round.
- For k = 5, let phi_j be the segment directions with |phi_{j+1} - phi_j| <= 60°. Project Σ_j e(phi_j) onto e(phi_2). The middle term contributes 1, terms j = 1, 3 contribute >= cos 60°, and terms j = 0, 4 contribute >= cos 120°. The sum is >= 1, so |t_5 - t_0| >= sqrt3.
- k = 2, 3, 4 are similar, with bounds 3, 2sqrt3 and 3; k = 1 is trivial. ∎

Corollaries:
- The Moser spindle is not a penny graph (case k = 2).
- A "Moser-type odd ring" needs k >= 6 rhombi. Such a ring is k rhombi in a chain plus one contact t_0 t_k. It would have n = 3k + 1 and alpha = k.
- k = 5 would give exactly 5/16, but it is impossible.

**Proposition 9 (verified 4-chromatic penny graph with alpha/n = 6/19).**
Construction:
- Turning t* = 54.8586862563° at all five hinges of a 6-rhombus chain, with segment length sqrt3, starting at (0,0) in direction 0°.
- The middles of each rhombus are at the segment midpoint ± (1/2)·(unit normal).
Data:
- 19 points: 7 tips and 12 middles.
- Exactly 31 unit pairs: 30 rhombus edges plus the closing contact t_0 t_6.
- The minimum distance over all other pairs is 1.076679.

Coordinates (6 decimals):
- tips: (0,0), (1.732051,0), (2.729011,1.416358), (2.144650,3.046856), (0.474980,3.507510), (-0.862767,2.407314), (-0.733098,0.680123);
- middles: (0.866025,±0.5), (1.821663,0.995977), (2.639398,0.420382), (1.966146,2.062917), (2.907515,2.400298), (1.176836,2.795191), (1.442795,3.759175), (0.123706,2.571238), (-0.511493,3.343586), (-0.299335,1.581151), (-1.296529,1.506286).

Claim: alpha = 6 and chi = 4.

*Proof.*
- alpha >= 6: the tips t_0, ..., t_5 are independent.
- alpha <= 6. An independent set J takes at most one middle per rhombus. If J uses middles of r >= 1 rhombi, these kill at least r + 1 of the 7 tips (they form r edges of the tip path). So |J| <= r + (7 - r - 1) = 6. If r = 0, at most 6 tips are usable because t_0 t_6 is an edge.
- chi = 4. In any 3-colouring, both tips of a rhombus get the same colour, so all tips do. This contradicts the edge t_0 t_6. ∎

Note that 6/19 ≈ 0.31579 is above 5/16 = 0.3125. Single rings give k/(3k+1) >= 6/19, so the 5/16 family must be genuinely two-dimensional. I did not find it.

**Proposition 10 (random lattice-phase bound; proved but weak).**
Set-up:
- Triangle components (TCs) are the classes of unit triangles under "share an edge".
- Every TC lies in one congruent copy of the triangular lattice: a triangle sharing an edge with a lattice triangle is its reflection, which is again a lattice triangle.
- Every TC therefore carries a lattice 3-colouring that is proper on all unit pairs inside the TC.
- n1 is the number of vertices in exactly one TC; f1 is the number of edges joining such vertices of different TCs.
Claim: alpha(G) >= n1/3 - f1/9.

*Proof.* Pick one colour class per TC uniformly and independently, keep the vertices of the chosen classes among those counted in n1, and delete one endpoint of each conflicting edge. A conflict has probability 1/9. Two vertices of the same TC at distance 1 are lattice neighbours and never conflict. ∎

## 3. Computations (all own code: Python with numpy/scipy; no SAT/ILP solvers)

### 3.1 Tools and their validation

- **Exact maximum independent set.** Branch and bound with a greedy clique-cover bound, simplicial reductions and component splitting. Agreed with brute force on 200 random graphs with n <= 13.
- **Exhaustive minimal good-set search.** It enumerates independent sets that are connected in the distance-2 graph, using ESU enumeration with an independence filter. This restriction is exact because s is additive over parts with disjoint closed neighbourhoods. The search returns the least |I| with s(I) >= t. It agreed with brute force on 300 random graphs (n <= 11) for t = 1 and t = 2.
- **Beam search** (heuristic, width 40–400) for good sets in larger graphs. It only gives upper bounds on the minimal size.

### 3.2 Minimal good-set sizes (exhaustive unless marked)

| graph | n | least \|I\| with s >= 1 | further |
|---|---|---|---|
| lattice hexagon, side 3 | 37 | 3 | |
| side 4 | 61 | 3 | |
| side 5 | 91 | 4 | |
| side 6 | 127 | 4 | |
| side 7 | 169 | 5 | s >= 2 needs 7; s >= 3 needs 8 |
| sides 8, 9, 10 | 217, 271, 331 | 5 | |
| dodecagonal square–triangle patch (6 lattice sectors and 6 radial square strips), R = 4, 5 | 91, 127 | 3 | |
| hexagon core + square-row shell (various), pruned to delta >= 3 | 193–537 | 2–3 | |
| lattice discs, random radius 3–7 (beam) | 34–174 | 2–3 | |
| deep interior of the lattice, I kept at distance >= 4 from the boundary (beam, size <= 12) | 169 | none found up to 12 | best s = -3 at sizes 7–12 |

The minimal sets in hexagons are alternate boundary vertices running from a corner to the next corner (Lemma 6 with X = 1), or the corner wedge (Lemma 7).

Annealing over lattice regions (400 steps) and over general 30°/15°-direction configurations (600 steps each, delta >= 3 enforced) never exceeded a minimal good-set size of 4. So no penny graph without small good sets was found. This is evidence, not proof, that the "unexcluded configuration" in the literature argument at m = 7 is a proof-technique artifact rather than a real global obstruction.

### 3.3 Independence ratios

| configuration | n | alpha | alpha/n |
|---|---|---|---|
| random sticky growth (each new disc touches 2 old ones), 300 samples | 30 | — | min 1/3, mean 0.369 |
| dense growth in the 30°-direction world, several runs | 30–80 | — | min exactly 1/3 |
| annealing to minimise alpha - n/3 (30°-direction world, 3 runs × 1500 steps) | 30–33 | — | never below 1/3 |
| snub square tiling (3.3.4.3.4), 6×6 torus quotient | 144 | 48 | 1/3 |
| snub square patches (disc cuts, radius 2–5) | 12–84 | — | 0.333–0.40 |
| Prop. 9 ring (6 rhombi + contact) | 19 | 6 | 0.3158 |

For the snub square tiling the density is exactly 1/3. The upper bound holds because each vertex lies in 3 triangles and there are as many triangles as vertices; the 6×6 torus gives a matching periodic set. Variants of Prop. 9 with 1–3 hinges closed to exactly 60° (31–34 edges), and all deletions of 1–3 vertices from them, never had alpha/n < 6/19.

### 3.4 Validation of Lemma 5

Outer cycles were computed with a rightmost-turn face walk, and the orientation was fixed by signed area. Over 296 pruned random clusters the outcomes were: 151 even, 110 odd, 13 with a non-simple boundary, 22 with chords. In every one of the 261 admissible cases:
- the turning sum was 360°;
- s(I) >= Σ_I tau/60° held for both parity classes (even case);
- the best I_j had s >= 2 (odd case).

Lattice hexagons gave s = 6. That is above the bound 3 because of the closed-corner overlaps of Lemma 6.

### 3.5 LP / discharging

Not carried out. A discharging LP needs a finite list of local configurations around a convex hull vertex, with angle variables. The geometry is continuous: open angles in (60°, 120°), arbitrary rhombi, and vertices in two triangle runs. In this session I could not reduce it to a finite list that is provably exhaustive, so there are no extracted rules.

## 4. Routes tried and exact obstructions

1. **Local savings-1 sets (the m/(4m-1) framework).** Rigorous negative fact: the lattice hexagon of side 7 has no independent I with |I| <= 4 and s(I) >= 1. So "every penny graph has a savings-1 set of size <= 4" is false, and savings-1 arguments cannot beat m = 5, i.e. 5/19. A proof of anything above 6/23 by this route needs m <= 5, which means handling every hull configuration with at most 5-element sets. My hull analysis stopped at the following points:
   - the closed 120° corner of depth 4 (Lemma 7) is reducible;
   - corners with an open angle (tau < 60°) or with a non-lattice backing were not classified.

   The general framework with ratio s/|I| >= 1/m and larger sets is not obstructed by hexagons (side 7: 2/7 at size 7, 3/8 at size 8). There the obstruction is purely the size of the case analysis.
2. **Boundary-alternating sets (Lemmas 5 and 6).** The global set has savings 3 but size b/2. It is only good if b <= 6m (36 for 6/23). The localized version needs Σ_I tau/60° + X >= 2 inside a window of 2m boundary steps. The exact blocking situation is a long outer cycle whose total turning of 360° is spread out, or offset by reflex corners, so that no window of length <= 2m contains two same-parity turning units. Corner wedges (Lemma 7) cover only closed, lattice-backed corners.
3. **Potential-function induction alpha >= cn + lambda·Σ_v (6 - d(v)).** K3 forces 1 >= 3c + 12·lambda. An interior step that removes N[v] for a degree-6 lattice vertex forces 1 - 7c + 18·lambda >= 0. Together these give c <= 5/23 ≈ 0.217 < 1/4. A potential λ·(#components) does not help at the hull, because local removals keep the graph connected.
4. **Random lattice-phase colouring (Prop. 10).** It is proved, but on the 3.4.6.4 tiling (each vertex in one triangle and two free edges, so f1 = n) it gives only 2/9. On the snub square tiling every vertex lies in two rhombus components, so n1 = 0 and the bound is 0. Combining it with a Grötzsch 3-colouring of the free-edge graph (which is triangle-free and planar) loses a factor 3 in the worst case. No variant reached 0.26.
5. **Searching for a global counterexample to small good sets (Section 3.2).** None was found.
6. **Constructions toward 5/16.** The natural 16-vertex candidate is a 5-rhombus ring with a closing contact, which would have alpha = 5 exactly. Lemma 8 proves it unrealizable. The best verified construction is 6/19. The 5/16 family was not reconstructed.

## 5. Sanity check against 5/16

No new lower bound is claimed, so there is nothing to contradict. All proved statements are consistent with 6/19 (Prop. 9) and with 5/16. The verified example has alpha/n = 6/19 > 5/16. Every lemma above is a statement about the existence of local savings, and each holds in the 6/19 ring: it has degree-2 middles, and by Lemma 2(a) those are good immediately.

## 6. Cost

- About 15 CPU-minutes of Python in total, mostly single-threaded (two runs once in parallel). Wall time: one session of about 2 hours.
- No solvers, no paid cloud, no network.
- Scratch scripts were kept only in the session scratch area and are not part of the repository.
- The exhaustive search and the ring coordinates above are enough to reproduce the key numbers.
