PASS-WITH-REPAIRS

# Referee report: PROBE_ASTRA_4 (Erdős #86, T3), round 4

Reviewed file: `problems/erdos86/PROBE_ASTRA_4_20261009.md` (390 lines). Nothing else under the repository was read. No web, no papers. All re-derivations below were done from the task's statement and standard mathematics before reading the author's justification; all finite checks were re-run with my own independent code (python3 + numpy + mpmath, no SAT/ILP/LP solver), total about 95 CPU-seconds.

Summary verdict: every mathematical statement labelled as proved is correct, every reported exact number was reproduced exactly, and the report is honest about not reaching the target. Repairs are needed only in (i) the status label, which should be OPEN rather than PARTIAL, since both proved bounds are weaker than both known bounds quoted in the brief, and (ii) Section 4.2, whose "exact obstruction" at 5/8 is correct but not sharp: the degree-histogram relaxation is exhausted exactly at r, as I show below.

## 1. Claim-by-claim verdicts

### Section 1 (averaging, full vertices, π₄ ≤ 4^(−1/3)) — CORRECT
- Face counts 2^(n−k)·C(n,k) and edge-in-face count C(n−1,k−1): re-derived. Average k-face density = e·C(n−1,k−1)/(2^(n−k)C(n,k)·k2^(k−1)) = e/(n2^(n−1)) = p using kC(n,k) = nC(n−1,k−1). Monotonicity of a_n and existence of π₄: correct.
- Two full vertices of a 3-cube at distance 2 force a square: correct (the four edges of the square u,u^i,u^j,u^{ij} are all incident to u or to v=u^{ij}). Same-parity distinct vertices of Q₃ are at distance 2: correct. So ≤ 2 full vertices per C₄-free Q₃ (verified by enumeration, max number of degree-3 vertices = 2).
- Σ_v C(d(v),3) ≤ 2·2^(n−3)C(n,3) ⇒ E(d)_3 ≤ (n)_3/4: correct double count (vertex + 3 present directions = full vertex of a 3-face).
- (d)_3 ≥ ((d−2)_+)³ for integers d ≥ 0: correct; convexity of x ↦ ((x−2)_+)³ and Jensen with E d = np: correct. p ≤ 2/n + ((n)_3/(4n³))^(1/3) ≤ 4^(−1/3) + 2/n: correct. 4^(−1/3) = 0.629960524947… confirmed.
- Conventions: spanning subgraphs, isolated vertices counted, expectation over all 2^n vertices, p = e/(n2^(n−1)): used consistently throughout Sections 1–5.

### Section 2 (Q₄ certificate (1) ⇔ (2) ⇔ (3)) — CORRECT, reproduced exactly
- Equivalences: C(i,2)+C(i,4)−i = 0,−1,−1,0,3 for i = 0..4, so T₂+T₄−2e = −n₁−n₂+3n₄; T₃ = n₃+4n₄ and Σn_i = 16 give (3) ⇔ (1). Correct.
- At most 2 full vertices per parity class of Q₄ (same parity ⇒ distance 2 or 4; 2 excluded): correct.
- The enumeration partition: a full vertex translated to 0000 fixes 4 edges; each of the 6 weight-2 vertices has 3 allowed states for its two downward edges (both present would close a square through 0000); the remaining 16 edges (12 between weights 2 and 3, 4 between weights 3 and 4) are free; 3⁶·2¹⁶ = 47,775,744 candidates, each C₄-free graph with 0000 full occurring exactly once. Correct. Every 4-cycle of Q_n is a coordinate square: correct. Translation invariance of the histogram makes the rooted check sufficient; the no-full-vertex case is trivial. Correct.
- The table (19,975,328 / 4,877,691 / 147,744 / 1,296 valid rooted graphs with min n₁+n₂ = 4 / 6 / 9 / 12; total 25,002,059; zero violations) was reproduced exactly by my own numpy implementation (see §3 below). (1) is tight for f = 3 and f = 4.
- Appendix A code read line by line: edge order, incidence masks, the pairs/free partition, base-3 decoding and square test are all as described.

### Section 3 (averaging to (7), the cubic, the root) — CORRECT
- Identity E_F Σ_{v∈F} C(d_F(v),k) = 16·C(4,k)·q_k: re-derived. (F, v∈F) uniform ⇔ v uniform and 4 directions uniform; a present k-subset lies in the chosen 4-set with probability C(n−k,4−k)/C(n,4) = (4)_k/(n)_k; summing over C(d,k) subsets gives C(4,k)(d)_k/(n)_k. Correct.
- (4): 96q₂+16q₄ ≤ 2·E_F e_F = 64p. Correct.
- (5): the with-replacement mixture argument gives (d)_k/(n)_k ≥ (d/n)^k − C(k,2)/n, including d < k. Correct.
- (6): 6(ET²−1/n)+(ET⁴−6/n) ≤ 4p, Jensen for t², t⁴ with ET = p ⇒ p⁴+6p²−4p ≤ 12/n. Correct; the constant 12 = 6·1+6 is right.
- g(t) = t⁴+6t²−4t, g'(r) = 4r³+12r−4 = 12(1−r) (since 4r³ = 16−24r): confirmed numerically (both 4.4901981724…). g'' > 0, r < 2/3 (cubic at 2/3 is 8/27 > 0) ⇒ g(p) ≥ 4(p−r) for p ≥ r ⇒ (7): p ≤ r + 3/n for n ≥ 4. Correct. Note (7) is vacuous for n ≤ 24 (r + 3/n ≥ 3/4 ≥ a_n for n ≥ 4) but it is explicit, as claimed.
- r = 0.62581681895846671601… (mpmath, 40 digits). Integer bracket: numerators −3348659416260042279926088 and 3826280656413965615148079 at 625816818958/10¹² and 625816818959/10¹² reproduced exactly. (5/8)³+6(5/8)−4 = −3/512 exactly, so r > 5/8. Correct.
- The regular substitution into (1) gives 4p(1−p)³+6p²(1−p)²−3p⁴ = 4p−6p²−p⁴ ≥ 0, i.e. exactly p⁴+6p²−4p ≤ 0: consistent with (6).

### Section 4.1 — CORRECT
T₃ < 16 is false: all 8 labelled 24-edge C₄-free Q₄ graphs are 3-regular (reproduced). Max T₃ by number of full vertices f = 0,1,2,3,4 is 16,15,16,16,16 (reproduced).

### Section 4.2 (5/8 mixture) — CORRECT but not sharp (repair R2)
- All five witnesses decoded with the stated edge order; each has zero squares; histograms, e, T₂, T₃, T₄ exactly as tabulated. Weights sum to 512; weighted histogram (162,1080,2700,3000,1250) = 16·C(4,i)·5^i·3^(4−i)/8 exactly, i.e. Binomial(4,5/8)·16. Correct.
- The logical claim "a relaxation retaining only face-averaged Q₄ degree histograms plus one-vertex moment constraints cannot rule out 5/8, even using all valid Q₄ degree-histogram inequalities" is correct as stated: the Binomial(4,5/8) histogram lies in the convex hull of achievable histograms, so no linear histogram inequality excludes it, and the Dirac law at 5/8 satisfies every moment constraint.
- However the obstruction is stronger than stated. I computed the convex hull of all 828 achievable histograms (points (n₁,n₂,n₃,n₄), 8 facets) and the largest p for which the Binomial(4,p)·16 histogram lies in it: p_max = 0.625816819005 (bisection to 1e−12; agrees with r to the precision of the hull tolerance), and the unique tight facet is −n₁−n₂+3n₄ ≤ 0, i.e. inequality (1). Consequences: (a) (1) is the optimal Q₄ degree-histogram inequality for the regular/Jensen route; (b) the route is exhausted exactly at r, not merely "cannot beat 5/8"; (c) the heading "the exact obstruction" in Section 4 should refer to r, with the 5/8 mixture as a convenient rational witness. Nothing in the report is false; it understates its own negative result. The author's caveat that no global construction of density 5/8 is asserted is correct and necessary.

### Section 4.3 (Q₅) — CORRECT
- (8): 2T₃+5n₀+n₁ ≤ 160. Each 3-set of present directions lies in 2 of the 10 4-faces; a degree-0 vertex is isolated in 5 faces, degree-1 in 1, degree ≥ 2 in none. Verified as an exact integer identity on random C₄-free Q₅ subgraphs (6 seeds). Regular substitution gives 4p³+(1−p)⁴ ≤ 1 ⇔ p⁴+6p²−4p ≤ 0: expanded and confirmed. Correctly labelled as "not a new improvement".
- Full-vertex count in Q₅ (≤ 2 per parity class, q₅ ≤ 1/8, p⁵ ≤ 1/8+10/n, (1/8)^(1/5) = 0.65975…): correct, and correctly labelled weaker.
- 56/80 = 7/10 is not re-proved; the report says so.

### Section 4.4 — CORRECT
Path count q₂ ≤ 1/2 ⇒ π₄ ≤ 2^(−1/2); neighbour-degree sum Σ_{y∼x} d(y) ≤ nd−C(d,2) ⇒ 3Σd² ≤ (2n+1)Σd ⇒ p ≤ 2/3+1/(3n): both re-derived, correct. The hand-classification gap (0000 and 0111 both full) is described honestly and not claimed.

### Section 5.1 — CORRECT (but trivial)
The 4-edge Q₃ example compresses to the square (0,1),(0,2),(1,3),(2,3); confirmed. Shows only that the naive OR/AND compression is not C₄-preserving.

### Section 5.2 — CORRECT (but yields only 3/4)
Shearer with each edge in n−1 squares; Gibbs inequality against the λ-weighted law on the 15 allowed square patterns, P(λ) = 1+4λ+6λ²+4λ³; E|Z_F| = 4p by symmetrisation; result p ≤ log₂P(λ)/(4log₂λ) > 3/4 for all λ > 1, infimum 3/4 (numerically 0.9167, 0.8002, 0.7751 at λ = 10, 10³, 10⁶). H(Z) ≤ n+log₂n!: correct. All correct, all trivial relative to the target.

### Section 5.3 — CORRECT
Root bits of the translated, direction-permuted mixture are i.i.d. Bernoulli(5/8): follows from the Binomial(4,5/8) degree law and permutation symmetry. Correct; scope limitation stated.

### Section 6 — reproduced
Q₃: 2902 C₄-free labelled subgraphs, counts by edges (1,12,66,220,489,744,756,468,138,8,0,0,0), 35 degree multisets, ex(Q₃,C₄) = 9: all reproduced. Q₄: counts by edges for e = 0..24 and total 1,226,436,381 reproduced exactly (independence-polynomial method, not the author's method); 828 histograms; ex(Q₄,C₄) = 24 with exactly 8 extremal labelled graphs. Rooted and labelled counts are mutually consistent: 16/f times the rooted count equals the labelled count for f = 1..4 (319,605,248 / 39,021,528 / 787,968 / 5,184).

## 2. Errors found
None in the mathematics. No circularity (the limit π₄ is established in Section 1 before use in Section 3; (1) is used only after the certificate; (5) is proved before use). No silently assumed lemma. Quantifiers and onsets (n ≥ 3 for Section 1, n ≥ 4 for (4)–(7), n ≥ 5 for (8)) are explicit and correct.

## 3. Repairs required
- R1 (status line). Replace PARTIAL by OPEN. The two bounds proved (0.62996 and 0.62582) are weaker than both bounds quoted in the brief (0.6068 elementary, 0.60318 SDP); under the pipeline's rule that a bound weaker than the known bound is not progress, the headline is a known-weaker result and the honest status is OPEN with an explicit negative result. The remainder of the line ("The requested bound below 0.60318 is OPEN", "no claim of novelty") is already honest.
- R2 (Section 4, title and 4.2 last paragraphs). State the sharp obstruction: the face-averaged Q₄ degree-histogram relaxation with regular degrees has value exactly r, attained at the facet (1); the 5/8 mixture is a rational witness that is not extremal. Suggested one-line proof for the author: the convex hull of the 828 histograms in the n₁..n₄ coordinates has 8 facets, and bisection on p shows the Binomial(4,p) histogram leaves the hull exactly through facet (1) at p = r.
- R3 (Section 3, optional). Remark that (7) is non-trivial only for n ≥ 25.

## 4. Independent re-checks actually run
1. Q₃ exhaustive (4096 masks): 2902 C₄-free; edge-count vector, 35 degree multisets, ≤ 2 degree-3 vertices. Agrees.
2. Q₄ labelled count via layer pairs and the independence polynomial of the overlap graph (2902² ordered pairs × 9 polynomial terms): counts by edges and total 1,226,436,381 agree exactly with Section 6; 0 graphs with ≥ 25 edges.
3. Q₄ histogram inequality (1) over all 1,226,436,381 labelled graphs by a vectorised layer method (2902 × 2902 × 256 table, 58 s): zero violations; min(n₁+n₂) by full count f = 0..4 is 0,4,6,9,12; max T₃ by f is 16,15,16,16,16; 8 extremal 24-edge graphs, all cubic; 828 distinct histograms. Agrees.
4. Appendix A rooted certificate re-implemented in numpy (47,775,744 candidates, 8 s): 25,002,059 valid; per-f counts 19,975,328 / 4,877,691 / 147,744 / 1,296; min n₁+n₂ = 4 / 6 / 9 / 12; zero violations. Exact agreement.
5. Five mixture witnesses decoded, square-checked, histograms and (e,T₂,T₃,T₄) recomputed; weights sum 512; weighted histogram (162,1080,2700,3000,1250). Exact agreement.
6. Cubic: r to 40 digits, integer bracket numerators, g'(r) = 12(1−r), −3/512 at 5/8, 4^(−1/3), (1/8)^(1/5), entropy-bound values. Exact agreement.
7. Identity (8) in Q₅ checked as an exact integer identity on 6 random greedy C₄-free subgraphs; (4), (5), (6), (7) and the Section 1 inequality checked on 4 random greedy C₄-free subgraphs of Q₇ (densities ≈ 0.45, so these are only sanity checks).
8. Convex hull of the 828 achievable Q₄ histograms (scipy ConvexHull, 8 facets); max p with Binomial(4,p)·16 inside = 0.625816819005, tight facet = (1). New information, see R2.

## 5. What I could not check
CPU timings, the claim that the Node scripts were run with the stated flags, the first (extrema-tabulating) layer enumeration's extra output, and the floating-point exploratory search for the weights (irrelevant to the conclusions, which are verified exactly). ex(Q₅,C₄) = 56 was taken from the brief by both the author and me.

## 6. Honest status
OPEN (toward the target), with two correct but known-weaker bounds and one correct negative result. Not HIT: no statement with c < 0.60318 or any new structural lemma about near-extremal Q₄/Q₅ configurations that could feed such a bound. Not PARTIAL under the pipeline's convention, because the headline bound r = 0.6258 sits above both the elementary 0.6068 and the SDP 0.60318; the author's own text concedes this. Nothing is dressed up beyond the single word PARTIAL: no conditional statement is presented as unconditional, and the scope of the 5/8 obstruction is stated carefully (if anything too weakly).

## 7. Value
Usable lemma: the certified Q₄ inequality n₁+n₂ ≥ 3n₄ (equivalently T₃+n₀ ≤ 16), tight at 3 and 4 full vertices, together with the clean face-averaging machinery (4)–(7) that converts any Q₄ histogram inequality into an explicit finite bound with error 3/n. Usable negative result: by the hull computation above, (1) is the best Q₄ degree-histogram inequality, so the whole "Q₄ degree profile + Jensen/regularity" route (seed (a) at the 4-cube level) is exhausted at exactly r = 0.6258 > 0.60318; likewise single-root direction entropy (seed (b)) cannot see below 5/8. The exact remaining obstruction is that any improvement must use information that is not a function of the per-face degree histogram, e.g. joint statistics of overlapping 4-faces, Q₅ configurations beyond their averaged Q₄ faces, or edge-type/correlation data as in the coloured-4-cube flag algebra; the report identifies this correctly but proves nothing in that direction.
