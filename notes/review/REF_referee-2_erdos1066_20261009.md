PASS

# Referee report (referee-2): Erdős #1066, probe PROBE_ASTRA_6_20261009.md (round 4)

Reviewed file: `problems/erdos1066/PROBE_ASTRA_6_20261009.md` (334 lines). Nothing else under the project tree was read. No web, no papers. Line numbers below refer to the reviewed file.

**Verdict: PASS.** Every statement labelled as proved survived an independent re-derivation. Every finite table in §7 was reproduced exactly with my own code. 1,800 additional random penny graphs (multi-lattice and generic) gave no counterexample to the lattice lemma, to the partition, to the exact averaging identity behind (1), or to (1) itself. The STATUS line (PARTIAL) is honest, and the conditional 13n/48 statement is clearly labelled as conditional on s ≥ 3n/4. The only remarks are editorial and do not affect validity (listed at the end). The mathematical value toward the target is small (see "Value").

## 1. Claim-by-claim verdicts (re-derived on paper before reading the author's justification)

**Definitions (l. 9–13).** P is finite, |x−y| ≥ 1 for x ≠ y, and edges are exactly the pairs at distance 1. This matches the brief. S = degree-6 vertices, T = P \ S, and α_w is the maximum-weight independent set. OK.

**§1, degree ≤ 6 and the regular hexagon at degree 6.** |u−v|² = 2 − 2cos θ ≥ 1 gives θ ≥ π/3, and summing the gaps gives d ≤ 6, with equality only for the regular hexagon. Correct.

**§1, 3-degeneracy (l. 44) and α_w ≥ w(P)/4.**
- Take a generic linear functional. Its minimizer x has all other points in the open half-plane bounded by a line through x, so its neighbour directions lie in an open arc of length π.
- Four neighbours would need three gaps of at least π/3 each, i.e. total span ≥ π. That is impossible, so x has degree ≤ 3.
- The argument applies to every point subset, so every induced subgraph is a penny graph and is 3-degenerate. That gives a 4-colouring, and the heaviest colour class has weight ≥ w/4.

Correct, standard, and no Four Colour Theorem is needed.

**§2, lattice compatibility.**
- L_a is independent of the chosen neighbour, because R²u = Ru − u and the lattice Zu + ZRu is R-invariant. If a, b ∈ S are adjacent, then L_a = L_b. Correct.
- Common neighbour x with d(x) ≤ 5: the identity x + R(a−x) − a = (I−R)(x−a) = R⁻¹(x−a) holds, because 1 − e^{iπ/3} = e^{−iπ/3}. So x + R(a−x) is one of a's six neighbours, all of which lie in P since d(a) = 6. It is also at distance 1 from x. The same holds for R⁻¹, which gives three distinct neighbours of x, as in (4). Two 3-subsets of a set of size ≤ 5 intersect, so b−x = R^{i−j}(a−x). Hence L_a = x + Z(a−x) + ZR(a−x) = L_b. Correct.
- The d(x) = 6 case reduces to the adjacent case twice. Correct.
- H-components (l. 76): by transitivity, each component C of H has one lattice L_C containing C ∪ N(C). Correct.
- l. 78: no G-edge joins S-vertices in different H-components, since such vertices would be at distance 1 ≤ 2. All S-neighbours of a T-vertex lie in one component, because any two of them share the neighbour x. Correct.

**§3, colouring.**
- In the basis (u, Ru), |au + bv|² = a² + ab + b². The value 1 occurs only for the six listed (a,b): from (a + b/2)² + 3b²/4 = 1 we get |b| ≤ 1, then substitute.
- On those six vectors the colour change Δ(a+2b) is ±1 or ±2, never 0 mod 3. So χ_C properly colours all unit edges inside L_C.
- Any two adjacent points of C ∪ N(C) differ by a unit vector of L_C. So χ_C is proper on G[C ∪ N(C)], and in particular χ_C(x) differs from the colour of every S-neighbour of x.

**§3, the partition T₀/T₁/T₂ (l. 92).** It is well defined and exhaustive:
- q(x) = 0 if x has no S-neighbour.
- Otherwise q(x) is the number of distinct χ_C-colours on N(x) ∩ S, for the unique component C. This lies in {1,2}, because the colour χ_C(x) is excluded.
- Basis independence: shifting the origin by (c,d) adds −(c+2d). Rotating the basis (u, Ru) → (Ru, R²u) maps the colour a+2b to b−a ≡ −(a+2b) mod 3. Both operations only permute the classes, so q is well defined.
- Every x ∈ T has exactly one value of q, so T₀, T₁, T₂ partition T (empty parts allowed).

**§3, random colouring and (5).**
- I is independent: there are no same-colour edges inside a lattice, and no S–S edges between components.
- U ∩ N(I) = ∅, so I ∪ J is independent for every independent J ⊆ U. With §1 this gives α_w ≥ w(I) + w(U)/4 for every colour choice.
- Pr(v ∈ I) = 1/3 for v ∈ S. For x ∈ T, Pr(x ∈ U) = 1 − q(x)/3, because only the colour k_C of x's single component matters.
- Linearity of expectation gives exactly (1), and max ≥ average. Correct.

**(2) and (6).**
- Unit weights give (4s + 3t₀ + 2t₁ + t₂)/12. Rounding up is legitimate because α is an integer.
- 3t₀ + 2t₁ + t₂ ≥ n − s gives the bound ⌈(n+3s)/12⌉.
- (6): substituting t₀ = n − s − t₁ − t₂ gives (3n + s − t₁ − 2t₂)/12. Replacing t₁ + 2t₂ by its maximum 2(n−s) gives (n+3s)/12.

All correct.

**(3) and the threshold remarks (l. 26–34).**
- s ≥ 3n/4 gives (n+3s)/12 ≥ 13n/48, and 13/48 − 6/23 = 11/1104 (exact).
- (n+3s)/12 > 6n/23 ⇔ 69s > 49n. Correct.
- max{n/4, (n+3s)/12} = n/4 ⇔ s ≤ 2n/3. Correct.
- The conditional hypothesis is non-vacuous: hexagonal patches B_r satisfy s ≥ 3n/4 from r = 7 on (n = 169, s = 127). I checked this.

**§4, the strip family F_(W,H).**
- Triangular bands have squared distance (k−i+1/2)² + 3/4, with contact iff k ∈ {i, i−1}. Square bands have (k−i)² + 1, with contact iff k = i. Rows two or more steps apart are separated vertically by at least 1 + √3/2.
- I re-derived the degree list (7) by hand:
  - corners have degrees 2, 3, 3, 2;
  - interior-row endpoints have one 3 and one 4 per row;
  - top and bottom non-corner vertices have degree 4;
  - interior vertices have degree 5.
- This gives n₂ = 2, n₃ = H, n₄ = 2W + H − 6, n₅ = (W−2)(H−2), and |E| = (5WH − 2W − 3H)/2. Correct, including W = 2 and H = 2.
- (8) follows from (7).
- The 3-colouring (2i mod 3 on even rows, 2i+1 mod 3 on odd rows) is proper: the changes are 2, ±1 and −1.
- (9): when 3 | W, each triangular band, in the stated order, splits into consecutive triangles. So α = WH/3. Correct.
- Curvature 1 − 5/2 + 3·(1/3) + 2·(1/4) = 0. Correct.

**§5, (10)–(12).**
- The exponential-clock selection probability λ_v/(λ_v + Σλ_u) is correct, so (10) holds.
- (11): 2/3 + H/4 + (2W+H−6)/5 + (W−2)(H−2)/6 = WH/6 + W/15 + 7H/60 + 2/15. Correct. At M = 4 the ratio is 53/240. Correct.
- (12): for 2 ≤ i ≤ W−3 and 2 ≤ j ≤ H−3, the vertex and all its neighbours are interior, hence of degree 5, so the term is exactly 1/6 for every f. All other terms are ≤ 1. Also WH − (W−4)(H−4) = 4(W+H−4). Correct.
- The M ≥ 72 and M ≥ 80 consequences are correct (see the onset remark in "Editorial notes").
- The unrestricted-rates remark (l. 234) is correct: the supremum of (10) over positive rates equals α(G). It is correctly presented as showing why "suitable weights exist" would be circular, not as an impossibility.

**§6.**
- Item 1: 6/23 − 1/4 = 1/92. Correct.
- Item 3: the stars at 0 and 3u lie in different H-components (no common neighbour, since |0 − 3u| = 3). u ~ 2u, and both are selected with probability 1/9 under independent halo colourings. Correct.
- Item 4: the regular-pentagon star has neighbour distances 2 sin(π/5) ≈ 1.17557 > 1 and 2 sin(2π/5) > 1. It is a degree-5 vertex with no triangle. Correct.
- Last paragraph: 6/23 − 8/31 = 2/713. Correct.

**Circularity or silent lemmas.** None found. The only external facts used are elementary: law of cosines, min of independent exponentials, linearity of expectation. The 8n/31 theorem is explicitly not used.

## 2. Independent re-checks (own Python code, exact arithmetic where stated)

Total CPU was about 3.5 minutes. No solvers were used, and nothing was written under the project tree except this report.

1. **§7, first table and strip table**, exact arithmetic.
   - Method: points stored as (X, A, B) with (x, y) = (X/2, (A + B√3)/2). The sign of 4|p−q|² − 4 was decided exactly. Exact α was computed by the include/exclude recurrence with memoization.
   - R₁…R₆: (n, E, s, α) = (1,0,0,1), (4,5,0,2), (9,16,1,4), (16,33,4,6), (25,56,9,9), (36,85,16,12).
   - B₀, B₁, B₂: (1,0,0,1), (7,12,1,3), (19,42,7,7).
   - All 18 strips F_(W,H), W = 1..6, H ∈ {2,4,6}: (n, E, α) agree cell by cell with the report's table. For example, W = 6 gives (12,21,4), (24,48,8), (36,75,12).
   - The degree counts (7) and the edge formula were asserted for all W ≥ 2. F_(3,4) has (n₂,n₃,n₄,n₅) = (2,4,4,2) and F_(6,6) has (2,6,12,16).
   - 4α ≥ n and 12α ≥ n + 3s hold throughout.
   - **Exact agreement on all 27 objects.**
2. **§7, star-union table**, exact lattice coordinates; my own H-components, q and α.

   | Centres | n | s | H-components | (t₀,t₁,t₂) | Numerator | α |
   |---|---:|---:|---:|---|---:|---:|
   | (0,0),(1,0) | 10 | 2 | 1 | (0,6,2) | 22 | 4 |
   | (0,0),(1,1) | 12 | 2 | 1 | (0,10,0) | 28 | 5 |
   | (1,0),(0,1),(−1,1) | 13 | 3 | 1 | (0,7,3) | 29 | 5 |
   | (0,0),(3,0) | 14 | 2 | 2 | (0,12,0) | 32 | 6 |

   **Exact agreement on all four rows.**
3. **Random stress test of §2–§3** (floating point with tolerance 1e−6; contacts are exact by construction, and ambiguous distances are asserted absent).
   - Graphs: 1,800 random penny graphs with n ≤ 40, built as one to three randomly rotated, partially thinned hexagonal lattice patches placed to touch each other, plus up to 12 generic "two-contact" points.
   - Per graph, I asserted:
     - the lattice of every H-component contains the component and all its neighbours (integrality of coordinates);
     - every T-vertex has its S-neighbours in one component;
     - every T-vertex with S-neighbours has q ∈ {1,2} and its own colour is not among them;
     - for every one of the 3^{#components} colour choices, I is independent;
     - the exact rational average of w(I) + w(U)/4 equals the right side of (1).
   - Inequality (1) was then checked with exact α_w, for unit weights and two random integer weight vectors per graph.
   - Coverage: up to 14 degree-6 vertices and up to 3 H-components per graph; 956 graphs had ≥ 2 components. 8,984 T₂-vertices occurred in total.
   - **No violation.** The minimum relative slack of (1) was 1/3.
4. **Arithmetic.** All checked with exact fractions:
   - 13/48 − 6/23 = 11/1104; 6/23 − 8/31 = 2/713; 6/23 − 1/4 = 1/92; 6/23 − 7/27 = 1/621.
   - (11) holds exactly on F_(2,2), F_(3,4), F_(5,6), F_(8,10), F_(12,12). The M = 4 value is 53/240.
   - The (12) K-region claim (all degree-5 closed neighbourhoods; K = (M−4)²) was verified on F_(8,8) and F_(12,12).
   - 2 sin(π/5) = 1.17557050458494625831 at 40-digit precision.

## 3. Errors

None found that affect any proved statement.

## 4. Editorial notes (non-blocking; no repair needed for correctness)

- **l. 222–228, l. 250, "explicit onsets":** M ≥ 72 and M ≥ 80 are valid sufficient onsets but not the first M where bound (12) works. Bound (12) divided by M² is already < 6/23 for every even M ≥ 70, and < 1/4 for every even M ≥ 78 (M² − 80M + 160 > 0 ⇔ M > 77.98). The report never claims sharpness. Suggest the wording "sufficient onsets".
- **Notation clashes:** H is both the auxiliary graph on S (l. 76) and the strip height (l. 124 on). M is both the strip side (l. 155 on) and the large rate (l. 234). These are harmless but should be renamed.
- **l. 82:** "Take a unit vector u" should read "one of the six unit vectors of L_C".
- **l. 78:** "no G-edges between different components of H" should say explicitly "between S-vertices in different components". Edges from C to T-vertices adjacent to C are of course present.

## 5. Honest status

**PARTIAL is correct and not dressed up.**
- The unconditional content is:
  - α ≥ ⌈n/4⌉ (the standard 3-degeneracy bound, a known fact);
  - the weighted certificate (1), a correct and fully proved lemma that is easy but not trivial;
  - its corollary α ≥ ⌈(n+3s)/12⌉.
- The only bound above 6/23 is restricted to the class s ≥ 3n/4 (more precisely 69s > 49n). The STATUS line, l. 26–34 and §8 all say so explicitly, and state that no c > 6/23 is proved for all penny graphs.
- The negative results (§4–§5) are explicitly scoped as obstructions to the explored estimates (degree-only Caro–Wei; density-of-exceptional-vertices discharging), not as counterexamples to the target. The report itself notes that the strip family has α = n/3.
- HIT would be wrong, since nothing holds for all penny graphs. OPEN would undersell it slightly: a genuine, fully proved bound strictly above 6/23 holds on a non-empty restricted class. That class includes hexagonal patches with r ≥ 7, and it beats the known 8/31 once s > 65n/93.

## 6. Value

The reusable piece is the weighted certificate (1). Each degree-6 vertex is worth 1/3, and each other vertex is worth 1/4, 1/6 or 1/12 according to how many lattice colours its rigid-patch neighbours use. Together with the lattice-compatibility lemma (common neighbour ⇒ same lattice, so H-components are rigid), it could serve as one ingredient in a discharging or weighted argument. The negative results are elementary but correct: the triangle–square strips F_(W,H) have no degree-6 vertices, all but 4M−4 vertices of degree 5, and α = n/3. On them, every degree-only Caro–Wei certificate is ≤ n/6 + (10/3)(2M−4).

The exact remaining obstruction is the s-poor regime. When s ≤ 2n/3, (1) gives only n/4, and when s = 0 the whole report gives only n/4. The target needs a gain of more than n/92 over the four-colour bound for penny graphs dominated by degree-≤5 vertices. Nothing in the report addresses that gain.

## 7. What I could not check

- I did not run the author's Node.js scripts, and could not verify the reported CPU timings (§8) or the counts of recursive calls and memo-table sizes (§7). I reproduced the results, not the runs.
- The random stress test is evidence, not proof. The proof of (1) was verified by hand, line by line.
- I made no novelty assessment; the report claims none.
