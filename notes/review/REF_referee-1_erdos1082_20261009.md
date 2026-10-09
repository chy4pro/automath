PASS-WITH-REPAIRS

# Referee report: PROBE_ASTRA_3_20261009.md (Erdős #1082, T2, round 4)

Reviewed file: `PROBE_ASTRA_3_20261009.md` only, plus the target brief. No other repository material, no web, no papers.

Verdict summary. Every statement the report labels as proved is correct; I re-derived each by hand and reproduced every reported finite check exactly with independent Python code. The repairs concern honesty of the STATUS line and the scope claimed for the two "obstructions", not the mathematics. The honest status is OPEN (nothing beyond the brief's known bound is proved toward the target), with one usable bookkeeping reduction and one usable negative result.

## 1. Claim-by-claim verdicts

### §1 Exact accounting — PASS
- Conventions (lines 29–32): isosceles incidence = (apex p, unordered base {x,y}), k_b = number of apexes; apexes lie on the perpendicular bisector of xy, which contains ≤ 2 points of S (x, y themselves are never on it), so k_b ≤ 2. Correct.
- I = Σ_{p,i} C(a_{p,i},2) = Σ_b k_b (both count incidences once); D = 2·C(n,2) − I = N − I. Correct.
- C ≥ 0: summand (a−2)(a−3)/2 is 1, 0, 0, ≥1 for a = 1, 2, 3, ≥4. Correct. E ≥ 0 trivially.
- Identity C(a,2) = 2a − 3 + (a−2)(a−3)/2: expands to (a²−a)/2. Correct. Summing over the T classes with Σa = N gives I = 2N − 3T + C; with I = N − D this is (2): 3T = N + D + C. Correct. T ≤ nM gives (1). Correct.
- (a−3)² − 3(a−2)(a−3)/2 = a(3−a)/2: checked. Σ a² = 2I + N, so the sum is (3N − 2I − N)/2 = N − I = D. Hence E = D + 3C and 9T = 3N + 2D + E, (3). Correct.
- (4): V = E + 9(nM − T) and 9nM = 3N + 2D + V. Correct.

### §2 Strictness M > (n−1)/3 — PASS (re-proof of a known bound)
- Diameter endpoints are exposed hull vertices: from |x−v|² ≤ |u−v|² one gets 2(x−u)·(v−u) ≥ |x−u|² > 0, so u is the unique minimiser of x ↦ x·(v−u). Correct.
- Two diameter edges with disjoint endpoints cross: four exposed vertices are in convex position; a non-crossing matching makes them opposite sides, and strict triangle inequalities at the diagonal intersection O (O is not on line AB since that would make A, B, C collinear) give 2d < |AC| + |BD| ≤ 2d. Correct.
- Some non-isolated vertex has diameter-degree ≤ 2: with neighbours b, c, e of a in hull order, any further edge cx (x ∉ {a,b,e}) would have to cross both ab and ae, which forces x into two disjoint open hull arcs; x = b or x = e gives a non-crossing disjoint pair. Correct, and complete in the case where no vertex has degree ≥ 3.
- Equality M = (n−1)/3 forces T = N/3, D = C = 0, E = 0, all classes of size 3, hence every non-isolated vertex of the diameter graph has degree 3: contradiction. So M > (n−1)/3 and, by n mod 3, M ≥ ⌈n/3⌉ for n ≥ 2. Correct. This is exactly the bound the brief lists as known; the report says "re-proved", which is honest.

### §3 Stability — PASS
- (6), (7): R = 3T − N ≤ 3nM − N; M ≤ (1/3+ε)n + B ⇒ R ≤ 3εn² + (3B+1)n, E ≤ 3R ≤ 9εn² + (9B+3)n. Correct.
- (8): a ≤ 4(a−3)² for a ∈ {1,2} and for a ≥ 4 via (b−1)(4b+3) ≥ 0; C(a,2) ≤ 6(a−3)² via (b−1)(11b+6)/2 ≥ 0 (both polynomial identities re-expanded). Correct.
- (9): non-good bases ≤ D + J ≤ D + 6E = 7D + 18C ≤ 18R. Correct.
- Kite statement and graph H (lines 178–190): distinct size-3 classes are distinct circles (different centre or different radius), two distinct circles share ≤ 2 points, so H is simple; degree ≤ 3. Correct.
- (10): 3A₃ = N − U; the charging of missing half-edges to k_b = 1 bases (≤ D) or to bad incidences at the other apex (≤ J) is injective within type. Correct.

### §3.1 Eight-point planar K₄ — PASS (as a finite statement), scope caveat
- Verified exactly: all 56 determinants non-zero, minimum |det| = 76734; the classes at points 4–7 are exactly {0,1,2}, {0,1,3}, {0,2,3}, {1,2,3}; all other classes singletons; the six apex pairs are exactly as listed; n = 8, T = 48, M = 7, I = 12, D = C = 44, E = 176; 22 bases have k_b = 0, 6 have k_b = 2. H = K₄ on the four size-3 classes.
- Caveat (repair R2 below): the configuration is globally about as defective as possible (D + C = 88 against N = 56; every class at the four base points 0–3 is a singleton). What it refutes is only the statement "every connected component of H, with H's vertices restricted to size-3 classes, contains a missing half-edge". It does not refute any local argument that is also allowed to look at the distance classes at the base points of the kites, and it says nothing about seed (a) as stated in the brief (a global o(n²) statement with geometric input).

### §3.2 Odd polygon plus centre — PASS
- No three collinear, apex pattern (two apexes for vertex pairs: O and vertex (i+j)/2 mod m; zero apexes for {O, v} because chord length 1 needs 6 | m), D = 2m, and all of (12) re-derived by hand and confirmed exactly for m = 3, …, 31 (also cross-checked that the integer labels agree with floating-point distances to 1e−9, minimum label gap > 0.02 at m = 31).
- Value caveat: this only shows D alone has no quadratic lower bound. The report's own sufficient condition needs R = D + C, and here C ≈ m²/2 and M ≈ n/2, so the family obstructs a route nobody needs. The report says so (lines 284–285).

### §3.3 Subsampling — PASS
- (13) is linearity of expectation. I verified it exactly (rational arithmetic, all 256 subsets of the eight-point set) for q = 1/2, 1/3, 3/4.

### §4 Weights and second moments — PASS
- (14), (15): interchange of finite sums; the cross term appears only for k_b = 2. Correct. w(a) = 2/(a−1) makes a class of size a ≥ 2 contribute a. Correct.
- (16): in the homogeneous data all N/2 values X_b equal 2w(3), Cauchy–Schwarz is tight. Correct.
- (17): D = 2b₀ + b₁, Σ(2−k_b)² = 4b₀ + b₁, differences 2b₀ and b₁. Correct.
- (18): a non-collinear triple has one circumcentre, so Σ C(a,3) ≤ C(n,3); homogeneous ratio 2/(n−2). Correct.

### §4.1 F₄^d metric model — PASS
- Symmetric since −1 = 1; all positive distances in (1,2) so the triangle inequality holds (strictly for distinct triples); classes (x + L_j)\{x} of size 3; apex set of {a,b} is exactly the two other points of the affine line a + F₄(b−a), so k_b = 2 for every base; T = N/3, I = N, D = C = E = 0, M = (n−1)/3. Class intersections ≤ 2 and triple uniqueness: correct. Verified by my own code for d = 1, 2, 3 (n = 4, 16, 64), including the triangle inequality for d ≤ 2, maximum class intersection 2, maximum triple multiplicity 1, and the pairwise-equidistant 4-point lines.
- The negative conclusion (lines 397–401) is correctly scoped: any proof using only the listed axioms fails. The identified missing planar fact (no four pairwise equidistant points) is correct; note M = (n−1)/3 < ⌈n/3⌉ in the model, so §2 already separates the model from the plane, but only by one unit.

### §4.2 Petersen attempt — PASS
- My own backtracking gives 13 810 nodes, 288 leaves, no decomposition; independently, there are exactly 24 labelled Petersen copies edge-disjoint from the fixed one with vertex 0 fixed (288 = 24 × 12, the vertex stabiliser of Aut(Petersen)), and none leaves a Petersen residual. The srg(10,3,0,1) common-neighbour criterion used for the residual is a correct characterisation of the Petersen graph. The vertex-transitivity justification for fixing perm[0] = 0 is correct.

### §5–6 — PASS
- Items 1–9 are consistent with the body. Item 8 (row sum n−1, total N/2, mean 1) and item 9 (rank ≤ 4 of the squared-distance matrix) are correct.
- §6.1 table reproduced exactly: 44 collinear triples, 4 795 retained subsets; per n the counts 120/516/1278/1668/998/204/11, minimum M 1/2/2/3/4/5/6, minimum D + C 4/9/12/22/30/45/58. §6.2 and §6.3 tables reproduced exactly.

## 2. Errors
None in the mathematics. No circularity, no hypothesis used before it is available, no silent lemma. All quantifiers and onsets are explicit (n ≥ 2 for (5); every n ≥ 2 for (1)–(4)).

## 3. Repairs required
- R1 (line 1, STATUS). Replace PARTIAL by OPEN. Nothing beyond the brief's known bound M ≥ ⌈n/3⌉ is proved toward the target; (1)–(4) are exact bookkeeping identities (a reformulation, not a bound), and (7)–(10) are their immediate consequences. The report's own closing paragraph (lines 471–475) describes an OPEN outcome.
- R2 (line 1 and lines 231–233, 441–442). "Explicit obstructions to both proposed counting routes" overstates. Route (b): the F₄^d model is a genuine obstruction to the pure-counting form of route (b) (weights, histogram moments, two-apex bound, intersection bounds), but not to route (b) with geometric control of the cross term in (15), as the report itself notes at line 452. Route (a): the eight-point K₄ refutes only a component-local propagation on H as defined; it is not an obstruction to seed (a). Suggested wording: "an obstruction to any purely combinatorial version of route (b), and a counterexample to one local propagation variant of route (a)".
- R3 (lines 246–285, optional). State up front that §3.2 bounds D only, that R is quadratic in the family, and that it therefore does not bear on the sufficient condition (1); the paragraph at 284–285 does this but only after the heading promises a "universal" negative result.

## 4. Independent re-checks actually run
All in Python 3 (integer / rational arithmetic unless stated), own code written from the definitions, not from the report's JavaScript; total CPU under 2 minutes.
1. 4×4 grid: all 65 536 subsets; 44 collinear triples; 4 795 retained subsets; for each, k_b ≤ 2, I = N − D, 3T = N + D + C, E = D + 3C, M ≥ ⌈n/3⌉, 3M > n − 1 all hold; the per-n table agrees exactly.
2. Eight-point set: 56 determinants, min 76734, none zero; classes, apex pairs, and all counts as reported.
3. Odd polygon plus centre, m = 3, …, 31: all of (11)–(12), apex pattern (C(m,2) bases with 2 apexes, m with 0), and consistency of the integer labels with floating-point distances.
4. F₄^d, d = 1, 2, 3: all of (19), class intersections ≤ 2, triple uniqueness, triangle inequality (d ≤ 2), existence of pairwise-equidistant 4-sets.
5. Petersen search: 13 810 nodes, 288 leaves, none found; cross-checked by enumerating the 24 distinct labelled edge-disjoint copies directly.
6. Identity (13): exact expectation over all 2⁸ subsets of the eight-point set for q = 1/2, 1/3, 3/4; agrees with q²N − q³I.
7. 300 random integer point sets (n = 4..14, no three collinear): the diameter graph always has a non-isolated vertex of degree ≤ 2; k_b ≤ 2; M ≥ ⌈n/3⌉ and 3M > n − 1 always hold.

## 5. Honest status
OPEN. The target (δ > 0) is untouched. The report re-derives the known bound and provides correct exact identities and two negative results of unequal weight. PARTIAL would be defensible only if the pipeline counts a reformulation plus negative results as partial progress; by the definition given to the referee (OPEN = nothing beyond trivialities / known facts proved toward the target), it is OPEN. Nothing conditional is presented as unconditional. The F₄ model is clearly labelled non-planar.

## 6. What I could not check
- No claims were beyond reach. The identity (13), the K₄ example, the polygon family and the F₄ model are all finite or closed-form and were fully checked. The CPU-time table in §8 cannot be verified and is immaterial.

## 7. Value
Usable lemma: the exact identity 3T = N + D + C (hence M ≥ (n−1)/3 + (D+C)/(3n)) and its stability corollaries (7)–(10): if M ≤ (1/3+ε)n + B then all but ≤ 18(3εn² + (3B+1)n) bases are kites whose two apex classes both have size 3, and the kite graph H is 3-regular up to that many missing half-edges. Usable negative result: the F₄^d model shows that any proof using only the metric axioms, k_b ≤ 2, class-size counting, pairwise class intersections ≤ 2, triple uniqueness and histogram-based weighted moments cannot give δ > 0; a proof must use a planar fact the model violates (the model contains pairwise-equidistant 4-sets, has no notion of the kite diagonal pq being the perpendicular bisector of xy, and does not satisfy the rank-4 constraint). Exact remaining obstruction: prove R = D + C ≥ c n² for an explicit c > 0 and onset (or, more weakly, a direct bound on max_p t_p) from the geometry of an almost 3-regular kite graph H whose edges are perpendicular-bisector kites; neither seed in the brief has been shown to deliver this, and no quantitative geometric input beyond the single-unit strictness of §2 was found.
