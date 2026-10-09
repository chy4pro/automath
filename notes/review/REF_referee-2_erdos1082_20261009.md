PASS-WITH-REPAIRS

# Referee report: Erdős #1082 probe PROBE_ASTRA_3 (round 4), referee-2

Reviewed file: `problems/erdos1082/PROBE_ASTRA_3_20261009.md` (776 lines). I read no other file under the repository and used no web sources or papers. I used only the target brief and standard mathematics. Line numbers (Lnn) refer to the reviewed file.

**Bottom line.** Every statement the report labels as proved survived my line-by-line re-derivation, and every reported finite check that I re-implemented gave exact agreement. I found no mathematical error. Four repairs are still needed: R1 relabels the status, R2 narrows the scope of the status line, R3 fixes the wording of a refuted claim, and R4 is cosmetic. The honest status is **OPEN**, not PARTIAL. The report proves nothing new toward the target. Its positive content is a re-proof of the known ⌈n/3⌉ bound plus exact bookkeeping, and its real contribution is a set of correctly scoped negative results.

---

## 1. Claim-by-claim verdicts

### §1 Exact accounting (L21–76): all correct

| Item | Verdict | How re-derived |
|---|---|---|
| Conventions (L23–40) | OK | Bases are unordered pairs, so there are N/2 of them. An apex lies on the perpendicular bisector, so k_b ≤ 2 by no-three-collinear. I = Σ_{p,i} C(a,2) = Σ_b k_b because both sides count the pairs (apex, unordered base). D = Σ_b(2−k_b) = N − I. Conventions are used consistently in all later sections. |
| C ≥ 0 (L41–43) | OK | The summand (a−2)(a−3)/2 equals 1, 0, 0 at a = 1, 2, 3 and is positive for a ≥ 4. The identities need C to be an integer, which holds. |
| Identity (L47) | OK | Expanding gives (a²−5a+6)/2 + (4a−6)/2 = a(a−1)/2. |
| (2) 3T = N + D + C | OK | Since Σa = N, we get I = 2N − 3T + C, then substitute I = N − D. |
| (1) M ≥ (n−1)/3 + (D+C)/(3n) | OK | Follows from T ≤ nM. The consequence (1/3 + c/3)n − 1/3 is correct. |
| (3) E = D + 3C, 9T = 3N + 2D + E | OK | (a−3)² − 3(a−2)(a−3)/2 = (a−3)(−a)/2. Also Σa² = Σ(2C(a,2) + a) = 2I + N, so the sum is (3N − 2I − N)/2 = D. |
| (4) 9nM = 3N + 2D + V | OK | There are nM − T padded zeros, each contributing 9. |

### §2 Strictness argument (L78–130): correct (and a re-proof of the known bound)

- **"First" (L83–88): OK.** |x−v|² = |x−u|² − 2(x−u)·(v−u) + d² ≤ d² gives 2(x−u)·(v−u) ≥ |x−u|² > 0 for every x ≠ u, including x = v.
- **"Second" (L90–101): OK.** The four endpoints are exposed points of conv S, so they are in convex position. With no three collinear, the quadrilateral is nondegenerate. Two disjoint pairs that do not cross are opposite sides. The diagonals meet at an interior point O, which lies on neither side, so both triangle inequalities are strict.
- **"Third" (L103–114): OK.** All diameter neighbours of a are hull vertices by "First". The proof uses the standard criterion for convex position: two chords with four distinct endpoints cross exactly when their endpoints interleave on the hull cycle. The two admissible open arcs (a→b avoiding c, and e→a avoiding c) are disjoint, and the cases x = b and x = e are handled. I also tested this numerically (§4 below): in every configuration where a vertex had ≥ 3 diameter neighbours, every inner neighbour in angular order had degree exactly 1.
- **Conclusion (L116–125): OK.** Equality M = (n−1)/3 forces T = N/3 and D = C = 0, hence E = 0. The class at distance d around a nonisolated vertex is exactly its set of diameter neighbours, so it would have size 3, a contradiction. The integer step is correct.
  - Remark: strictness is only needed when n ≡ 1 (mod 3). For other n, M ≥ (n−1)/3 already gives ⌈n/3⌉.
  - This is the known bound stated in the brief. The proof is a valid, self-contained re-proof, not progress.

### §3 Route (a) (L132–206): all proved statements correct

- **(6), (7), and the η-variant: OK.** (7) follows from 3n((1/3+ε)n + B) − n(n−1) = 3εn² + (3B+1)n, together with E ≤ 3R (because D ≥ 0).
- **(8) U ≤ 4E and J ≤ 6E: OK.**
  - Cases a = 1, 2: 1 ≤ 16, 2 ≤ 4, 0 ≤ 24, 1 ≤ 6.
  - Case a ≥ 4: I expanded both stated factorisations, (b−1)(4b+3) = 4b² − b − 3 and (b−1)(11b+6) = 11b² − 5b − 6. Both are correct.
  - No bounded-class-size hypothesis is used.
- **(9): OK.** Exceptional bases ≤ D + J ≤ D + 6E = 7D + 18C ≤ 18R. For ε = B = 0 we get R ≤ n and E ≤ 3n, so U ≤ 12n and there are at most 18n exceptional bases. Both constants are correct.
- **Kite and graph H (L178–190): OK.**
  - H is simple because two distinct circles share at most 2 points, while two distinct bases span at least 3 points.
  - There are no loops, because apexes p ≠ q give circles with different centres.
  - Distinct classes give distinct circles.
  - Degree ≤ 3.
- **(10): OK.** 3A₃ = N − U. The quantity 3A₃ − 2e(H) counts the missing half-edges. Each one is charged either to a base with k_b = 1 (injective, since that base has only one apex) or to the bad incidence (q, b) at the other apex (injective, since (q, b) determines the base b and hence the remaining apex p). So 3A₃ − 2e(H) ≤ b₁ + J ≤ D + J.
- **§3.1, eight-point planar K₄: OK, verified exactly.** Details are in §4 below. The configuration is genuinely planar (integer coordinates, all 56 orientation determinants nonzero) and genuinely saturated: H = K₄ with 3A₃ − 2e(H) = 0. The claim it refutes is worded imprecisely; see R3.
- **§3.2, odd regular polygon plus centre: OK.**
  - Apexes: vertex k is on the bisector line through O at angle π(i+j)/m exactly when 2k ≡ i+j (mod m). For odd m this has a unique solution, and k ∉ {i, j}.
  - The m bases {O, v} have no apexes: 2 sin(πr/m) = 1 would need m = 6r.
  - Each vertex has (m−1)/2 classes of size 2 plus the singleton {O}.
  - I re-derived (12) by hand: T = 1 + m(m+1)/2, I = m(m−1), D = 2m, C = (m−2)(m−3)/2 + m, E = (m−3)² + m((m−1)/2 + 4).
  - D/n² < 2/m holds. The report scopes this correctly (L284–285): it rules out only "D alone is quadratic". This is an easy negative result.
- **§3.3, subsampling (13): OK.** The identity is exact (I checked it over all 2⁸ subsets, §4 below). The accompanying claim that it "does not amplify" is a heuristic remark, and the report presents it as one (L299–300).

### §4 Route (b) (L302–435): all proved statements correct

- **(14)–(15): OK** by expanding X_b².
- **Weight w(a) = 2/(a−1): OK.** It gives C(a,2)·w(a) = a and w(3) = 1.
- **(16): OK.** In the homogeneous case the Cauchy–Schwarz inequality holds with equality.
- **(17): OK.** D = 2b₀ + b₁ and Σ(2−k_b)² = 4b₀ + b₁. The two gaps are 2b₀ and b₁.
- **(18): OK.** Three non-collinear points determine a unique circle, so each triple is counted at most once. The homogeneous ratio is (N/3)/(N(n−2)/6) = 2/(n−2).
- **§4.1, F₄ᵈ metric model: OK.**
  - ρ is symmetric (subspaces are closed under negation) and strictly metric, since all values lie in (1, 2).
  - Each class is (x + L_j) \ {x}, of size 3.
  - Apexes of {a, b} are exactly the two other points of the affine line a + F₄(b−a), so k_b = 2.
  - The class-intersection and triple-uniqueness claims hold; I also checked them by computer.
  - **The model does not live in the plane, and the report says so (L362–363).** Its "obstruction" applies only to the stated list of hypotheses (L397–401). Within that scope it is genuine: the model satisfies k_b ≤ 2, the combinatorial shadows of concyclicity (two classes share ≤ 2 points; a triple lies in ≤ 1 class), and has all classes of size 3. So neither class-size-weighted double counting nor any second moment of the k_b or class sizes can gain anything without a Euclidean input.
  - It is in fact stronger than the report states. Since n = 4ᵈ ≡ 1 (mod 3), the model has M = (n−1)/3 < ⌈n/3⌉, so the listed hypotheses cannot even recover the known bound. This is consistent with L409–410.
  - Additional observation (mine, computed): the model's H is a disjoint union of K₄'s, one per affine line. For d = 3, e(H) = N/2 = 2016 and A₃ = T = 1344 = 4·336. This is the abstract analogue of §3.1 with the four centres collapsed onto the four base points, which is exactly the four-equidistant-points pattern the report identifies (L403–407) as impossible in the plane. That non-planarity proof (L405–407) is correct.
- **§4.2, Petersen attempt: OK.**
  - The facts about the Petersen graph are correct; I checked the common-neighbour formula by computer.
  - Fixing the image of vertex 0 is justified by vertex-transitivity: if B = σ(A) and τ ∈ Aut(A) has τ(0) = σ⁻¹(0), then B = (στ)(A) with (στ)(0) = 0.
  - The residual graph of an edge-disjoint pair is 3-regular, so the λ = 0, μ = 1 test does identify the Petersen graph.
  - The outcome agrees with the classical fact that K₁₀ cannot be decomposed into three Petersen graphs. The report correctly scopes it as a failed construction, not a general nonexistence claim (L433–435).

### §5 items 8–9 (L460–469): OK

- Item 8: row sum 3·(n−1)/3 = n−1, total N/2, mean over C(n,2) axes equal to 1.
- Item 9: D_ij = u_i + u_j − 2x_i x_j − 2y_i y_j, so the squared-distance matrix has rank ≤ 4.
- Neither item claims anything beyond this.

### §6 tables (L486–549): OK

All reported numbers that I re-ran agree exactly (§4 below).

## 2. Errors

None in the mathematics. I found no circularity, no hypothesis used before it is available, no silently assumed lemma, and no unspecified error terms.

## 3. Required repairs

- **R1 (L1, L775–776; status label).** Change PARTIAL to **OPEN**. Measured against the brief, the positive content consists of:
  - a re-proof of the bound M ≥ ⌈n/3⌉, which the brief already lists as known;
  - exact rewritings (2)–(4) of the standard isosceles double count;
  - direct stability consequences (6)–(10) of those rewritings.

  None of these is a statement toward M ≥ (1/3+δ)n − O(1). Everything else is a negative result about proof strategies, which is what the pipeline's "OPEN with the exact obstruction" covers. The *content* of the status line is honest: it says "re-proved" and "No δ > 0 … is proved". Only the label is too generous.
- **R2 (L1, scope).** Replace "explicit obstructions to both proposed counting routes" with something like "explicit obstructions to the purely combinatorial (abstract-metric) relaxations of both routes, and a planar saturated K₄ refuting local defect propagation". The body is correctly scoped (L362–363, L397–401, L284–285); the status line is broader than the body.
- **R3 (L232–233; also L441–442).** State the refuted claim precisely as: "every connected component of H contains a vertex of degree < 3, i.e. a missing half-edge". The literal wording "must meet a deficient base or a non-size-3 class" is *not* refuted by the example. Every one of the eight points is the centre of singleton classes, the bases {4,5}, {4,6}, … have k_b = 0, and globally D = C = 44 (R = 88 > N = 56).
- **R4 (L92–99; cosmetic).** The cyclic labels A, B, C, D clash with the defect quantities C and D defined in §1. Rename them, e.g. P₁, …, P₄.
- **Optional (L17).** The sentence "This sufficient condition is stronger than merely proving the target" should say what it means: D + C ≥ cn² is equivalent to the average statement T ≥ ((1+c)n² − n)/3. It implies the target, but it might fail even if the target is true.

## 4. Independent re-checks actually run

All checks used my own Python 3 code. I did not run the report's Node code; instead I read its logic and re-implemented every check. Arithmetic was exact (integers or rationals) except where stated. Total CPU was a few seconds.

Every check in the table below also asserted all of the following, with zero failures:
- k_b ≤ 2, and simplicity of H with maximum degree ≤ 3;
- (2), (3), (8), (9), (10);
- in the random-set check, additionally (4), (17), (18), and M > (n−1)/3.

| Check | What I ran | Result |
|---|---|---|
| 4×4 grid (§6.1) | All 65,536 subsets. Collinear triples found independently. All identities above asserted on every retained subset. | **Exact agreement.** 44 collinear triples, 4,795 retained subsets. Per-n counts, minimum M and minimum D+C equal the report's table in every row: (120,1,4), (516,2,9), (1278,2,12), (1668,3,22), (998,4,30), (204,5,45), (11,6,58). |
| F₄ᵈ models (§6.2) | My own F₄ multiplication via logarithm tables. Directions normalised projectively (first nonzero coordinate equal to 1), which is a different canonicalisation from the report's. d = 1, 2, 3. | **Exact agreement.** (n, T, M, I) = (4,4,1,12), (16,80,5,240), (64,1344,21,4032), with D = C = E = 0 and b₂ = number of bases. Maximum class intersection is 2 (d = 1, 2); every triple lies in at most 1 class (d = 1, 2, 3). |
| Polygon plus centre (§6.3) | Every odd m from 3 to 31, using actual Euclidean coordinates at 60 significant digits rather than the report's labels. Checked that distances are equal exactly when labels are equal (unequal pairs differ by at least 0.0205), that there are no three collinear, and every formula in (11)–(12), plus b₀ = m and b₁ = 0. | **Exact agreement** with all four table rows (m = 3, 5, 9, 31). This is a numerical cross-check of the analytic argument in §3.2. |
| Eight-point K₄ (§3.1, §6.4) | Integer squared distances. All 56 orientation determinants. Circumcentres computed with exact rationals. | **Exact agreement.** Minimum \|det\| = 76734. The four circumcentres are exactly points 4–7. Classes are exactly {0,1,2}, {0,1,3}, {0,2,3}, {1,2,3}; all others are singletons. The apex pairs are exactly as listed. T = 48, M = 7, I = 12, D = C = 44, E = 176, A₃ = 4, e(H) = 6, 3A₃ − 2e(H) = 0. Points 0–3 are not concyclic. |
| Petersen search (§4.2, §6.4) | (i) Brute force over all 10! permutations. (ii) A line-for-line port of the report's DFS. | (i) 2,880 edge-disjoint embeddings in total and 288 with vertex 0 fixed, giving **24** distinct second copies (2880/120). None has a Petersen residual; all 24 residuals are triangle-free but not Petersen. (ii) nodes = **13,810**, leaves = **288**, nothing found. **Exact agreement.** |
| (13) subsampling | The exact expectation over all 2⁸ subsets for q ∈ {1/3, 1/2, 5/7}, on the eight-point set and on an 8-point no-three-in-line set from the 4×4 grid. | Equals q²N − q³I = q²((1−q)N + qD) exactly. |
| Universal-claim stress tests | 1,232 random no-three-collinear integer sets (n ≤ 14, small boxes, many coincident distances); 671 subsets of the triangular lattice (exact squared norms); 10 configurations of lattice points on a common circle, with and without the centre (n up to 48). | Zero failures. The triangular-lattice sets got as low as R/N = 0.5. |
| Diameter lemma (§2) | The random sets above (crossing property tested with exact orientations), plus 974 "fan" configurations: up to 10 lattice points on a circle within a 55° arc around a centre, with random interior points added. | Zero failures. There was always a nonisolated vertex of degree ≤ 2. Disjoint diameter edges always crossed. Every inner diameter neighbour of a high-degree vertex had degree exactly 1. |

## 5. Honest status

**OPEN.** The report proves no δ > 0 and no conditional or restricted statement toward M ≥ (1/3+δ)n − O(1). The known bound is re-proved, and the identities are exact restatements of the standard double count. The negative results are correct and properly scoped in the body. Apart from the label (R1) and the slightly broad wording in the status line (R2), nothing is dressed up: no conditional claim is presented as unconditional, and no bound weaker than the known one is presented as progress.

## 6. Value

The usable lemma is the exact identity 3T = N + D + C (equivalently 9T = 3N + 2D + E), with the stability package (7)–(10) and its explicit constants. Any planar lemma of the form R = D + C ≥ cn² immediately gives δ = c/3 with onset n ≥ 2 and B = 1/3, and the near-extremal structure is explicit: a graph H on the size-3 classes that is almost 3-regular, built from kites.

The usable negative results are:
- The F₄ᵈ model shows that no argument using only the metric axioms, class sizes, k_b ≤ 2, and the combinatorial forms of circle uniqueness can even reach ⌈n/3⌉, let alone (1/3+δ)n. A genuinely Euclidean input is mandatory, and "no four pairwise-equidistant points" (equivalently, no collapse of a K₄-component's centres onto its base points) is the concrete fact the model violates.
- The eight-point example shows that saturated K₄ components of H exist in the plane.

The exact remaining obstruction is to exclude, quantitatively and uniformly in n, planar sets in which all but o(n²) bases have two apexes whose classes both have size 3. Equivalently, one needs a Euclidean lower bound R ≥ cn², or control of the cross term in (15).

## 7. What I could not check

- **The Node code block itself.** I did not execute it (I have no Node runtime in my clean room). I read it and confirmed that its logic matches the descriptions:
  - the F₄ reduction modulo x² + x + 1 via `z ^= 7`, and canonicalisation by the minimum over scalar multiples;
  - the expected polygon apexes `[inv2*(a+b)%m, m]`;
  - the identity assertions in `stats`.

  I then re-implemented every check independently (§4).
- **The CPU and wall-clock records in §8 and the provenance statements in L7.** These cannot be verified and are irrelevant to the mathematics.
- **Whether the average-type route R ≥ cn² is true for planar sets.** This is the open core and outside the scope of this review. My small random experiments (minimum R/N = 0.5 among the triangular-lattice samples) are not evidence either way.
