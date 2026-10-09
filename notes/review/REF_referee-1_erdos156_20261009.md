PASS-WITH-REPAIRS

# Referee report: PROBE_ASTRA_1_20261009 (T1, Erdős #156)

Referee: referee-1 (independent, clean room). Files read: only `problems/erdos156/PROBE_ASTRA_1_20261009.md` and the task brief. No web, no papers, no other repository material. All code below is my own (python3), run in this session; total compute under 1 CPU-minute.

Verdict in one line: every statement the report labels as proved is correct, and every reported exact check reproduces to the digit; the single repair required is the STATUS word itself, which should be OPEN (with the exact obstruction) rather than PARTIAL, plus two cosmetic precision fixes.

## 1. Claim-by-claim verdicts

### Section 1 (blocking criterion, inequality (1), (2))
- Criterion "A ∪ {x} not Sidon iff x ∈ T(A) ∪ Q(A)" for x ∉ A: CORRECT. I re-derived the case split (x+a = b+c; 2x = b+c; x+a = x+b; x+a = 2x) and confirmed completeness, including the repetition convention. Verified exhaustively on all 84,274 Sidon subsets of [N], N ≤ 24 (1,436,132 comparisons, 0 failures).
- (1) |B(A)| ≤ (m³+m)/2: CORRECT. For each of m choices of c, unordered pairs with repetition from A∖{c} number (m−1)m/2, giving m²(m−1)/2; plus m(m−1)/2 midpoints; plus m. Sum is m + (m³−m)/2 = (m³+m)/2.
- (2) 2N ≤ m³+m for every maximal set: CORRECT (trivial consequence). Confirmed on every maximal set, N ≤ 24.
- Honesty: correctly labelled as a lower bound, not progress.

### Section 2.1 (one representative per residue)
- Lift is Sidon: CORRECT (reduce mod M, D Sidon, representatives unique).
- Any other x ≡ d (d ∈ D) is addable: CORRECT. I checked both blocking mechanisms, including the sub-case e = d (then f = g = d forced by the modular Sidon property, so x = a_d). Exhaustively confirmed in 6.3 re-run: 3,488 occupied-residue points over 407 lifts, all addable.

### Section 2.2 (criterion for several levels; (3), (4))
- "C Sidon iff all positive within-fibre differences are distinct, counted across all d": CORRECT, given D modular Sidon (stated). Re-derived: a modular reduction pins the unordered residue pair; within one class it is Sidonness of S_d; across two classes d ≠ e a nontrivial collision is exactly a nonzero difference shared by S_d and S_e, and conversely.
- (3) Σ_d C(|S_d|,2) ≤ H−1 when S_d ⊆ {0..H−1}: CORRECT. (4) t ≤ H−1: CORRECT (C(1+t_d,2) ≥ t_d).
- The two-layer counterexample (d+0M)+(e+M) = (d+M)+(e+0M): CORRECT.

### Section 2.3 (lift-repair bound (5))
- s(HM) ≤ k + H − 1 + u: CORRECT, with u = number of initially addable points of I with residue outside D (depending on the lift). Proof is phase-restricted greedy plus monotonicity of blocking. Confirmed on all 407 lifts (H = 2,3; M = 7, 13, 21): the restricted first phase added exactly H−1 at most in every row, and the final size satisfied (5) every time.
- Assessment: mathematically valid, but the content is monotonicity plus (4). It is a bookkeeping lemma, not a bound on s(N); the report says this itself ("Obtaining such an outside-residue coverage estimate ... is the missing step").

### Section 2.4 (Singer perfect difference set, (6))
- Construction and proof: CORRECT (trace is a nonzero F_q-linear form of kernel dimension 2; for α ∉ F_q the forms Tr(z), Tr(αz) are independent; one projective common zero gives the unique representation of each nonzero quotient element as a difference).
- Cosmetic repair R2: the independence argument writes "Tr((α−c)z) = 0 for some c ∈ F_q", i.e. it only treats the dependence Tr(αz) = c·Tr(z). The general dependence λTr(z) + μTr(αz) = 0 should be stated; the case μ = 0 forces λ = 0 and the case μ ≠ 0 reduces to the written one. No gap in substance.
- Independently verified: I constructed Singer sets from GF(q³) for q = 7, 11, 13, 17, 19 (M = 57, 133, 183, 307, 381) and confirmed the perfect-difference property for each.

### Section 3 (cubic curve, (7)–(10))
- C_p Sidon: CORRECT (first two coordinates determine S = a+b and P = ab).
- (8) w = u³ + (3/2)δS with δ = v − u²: re-derived symbolically, CORRECT.
- (9) discriminant S²−4P = (S−2u)² + 2δ: CORRECT.
- Character count: number of y with y²+c a square or zero is (p+χ(−c))/2 for c ≠ 0: CORRECT (re-derived from Σ_y χ(y²+c) = −1 and 1+χ(−c) zeros).
- (7) |T_p| = (p³−p²+2p)/2: CORRECT; the character sum over δ ≠ 0 cancels since δ ↦ −2δ permutes F_p* and χ sums to zero.
- Midpoint formula (u, u²+d², u³+3ud²) and criterion χ(2): CORRECT.
- (10): CORRECT, both branches. Exhaustively confirmed for all nine primes 5 ≤ p ≤ 31 (see §3 below), including the criterion (8)–(9) at every point of F_p³.
- Honesty: explicitly labelled as a group-model negative result; no interval statement is claimed. Correct.

### Section 4.1 (witness structure)
- Exactly k ordered representations x = a+b−c for x ∉ D: CORRECT (indexed by b through the unique representation of x−b).
- (11) h_x = (k−t_x)/2 and "support determines the negative vertex" (via 2(c−c') = 0 in an odd-order group): CORRECT.
- Vertex degree ≤ 3 in F_x: CORRECT (one positive role, one negative role, one midpoint).
- Σ_x t_x = k(k−1) and 2a−c ∉ D: CORRECT.
- (12) g ≥ (k−1)²/2: CORRECT (k(k−1)/5 ≤ (k−1)²/2 for k ≥ 2).
- At most one common 3-support between distinct x, y ∈ G, via x−y = 2(c_y−c_x): CORRECT.
- All of these structural claims verified by code on D for M = 7, 13, 21 (the report's sets) and on Singer sets up to M = 381 (not in the report).

### Section 4.2 (probability tools)
- Harris/FKG for decreasing events via total covariance: CORRECT (standard).
- (13) two-sided Janson-type recurrence: re-derived. The identity q_i − (1−p_i)q_{i−1} = P(E_i ∩ B ∩ C^c) − p_i P(B ∩ C^c) is CORRECT, the union bound over earlier neighbours is CORRECT, and the telescoping with multipliers in [0,1] is CORRECT.

### Section 4.3 ((14), (15))
- w_x ≥ b using log(1−z) ≥ −z/(1−z), 1/(1−ρ³) ≤ 8/7, 1/(1−ρ²) ≤ 4/3 for ρ ≤ 1/2: CORRECT.
- E U ≥ g b ≥ (k−1)²b/2: CORRECT.
- Numerically: P(I_x = 1) ≥ w_x held at every x ∈ G in every exact and Monte Carlo test (minimum slack ≥ 0, see §3).

### Section 4.4 (covariance, (16))
- Intersecting-pair counts (≤ 15k/2 for 3-supports, ≤ 100 pairs involving a 2-support): CORRECT as upper bounds. Union sizes (≥ 4 for distinct 3-supports; ≥ 3 for pairs involving a 2-support, including the case of a 2-support contained in a 3-support): CORRECT.
- w_xy ≤ w_x w_y + 5ρ² + ρ³: CORRECT (1 − Π(1−z_i) ≤ Σ z_i over at most one shared 3-support and five shared 2-supports).
- Cov(I_x, I_y) ≤ ε and (16): CORRECT. Chebyshev requires E U > 0, which (15) gives.
- Numerically: Cov(I_x,I_y) ≤ ε held exactly for all pairs on M = 57 and M = 133 (maximum covariance about 0.17 versus ε ≥ 6.8); the ε bound is very loose, which does not affect validity.

### Section 4.5 ((17) and onsets)
- All constant steps re-derived: ρ ≤ 1/2 from L ≥ 6 log(2C) and log L ≤ L/2; (8/7)kρ³ ≤ L/12 from the third component of L_0; (40/3)ρ² ≤ 10/3; log L ≤ L/16 for L ≥ 128; the three power bounds; 2/(k−1)² ≤ 8/k². CORRECT.
- (17) P(all outside points blocked) ≤ J(C) k^{−1/6} for k ≥ exp(L_0): CORRECT. I evaluated (16) and (17) in 50-digit arithmetic at L = L_0, L_0+10, 2L_0 for (C,θ) = (1,0.3), (2,0), (0.5,0.32), (3,0.25), (10,0.3): (16) ≤ (17) in every case.
- Repair R3 (presentation, not validity): the onset is astronomically large and this should be stated frankly next to (17). For C = 1, θ = 0.3 the onset is k ≥ exp(2.35·10^11); for C = 2, θ = 0 it is k ≥ e^128. At every size I could test (k ≤ 20) the right side of (16) exceeds 1 by one to four orders of magnitude, so the bound is vacuous there even though the underlying phenomenon (U is typically large) is already visible: for k = 20, ρ = k^{−1/3} the exact-model P(U = 0) is about 0.003 while (16) gives about 311.

### Section 5 (stopping points)
- Item 6 (ℓ³ four-term collision supports, expectation ≥ m⁴/(1000N)): re-derived, CORRECT (d > c since b > a; d ≤ 5ℓ−1 ≤ N; increasing order recovers (a,b,c); ℓ ≥ N/10 for N ≥ 10).
- The other items are honest descriptions of non-results; nothing is used as a theorem.

### Section 6 (finite checks)
All four tables reproduced exactly; see §3.

## 2. Errors found

None affecting validity. No circularity, no hypothesis used before it is available, no silently assumed lemma. Quantifier and convention usage (unordered sums with repetition; group vs integer; Q as solutions of 2x = a+b in odd order) is consistent throughout.

## 3. Independent re-checks (my own python3 code)

1. Exhaustive enumeration of all Sidon subsets of [N], 1 ≤ N ≤ 24, by DFS with incremental sum sets; at every node, blocking criterion versus direct addability for every outside point; at every maximal node, inequality (2). Result: all 24 rows of table 6.1 (s(N), number of Sidon subsets, number of maximal Sidon subsets) agree exactly; totals 84,274 subsets and 1,436,132 comparisons agree exactly; 0 criterion failures; (2) never violated. Minimal examples found: {5,6,9} in [10], {10,11,16,19} in [22], {12,14,19,22,23} in [24] (the report's examples are different attaining sets; both are valid).
2. Perfect difference sets M = 7, 13, 21: perfect-difference and Sidon properties; k ordered witnesses per outside x; vertex degree ≤ 3; at most one common 3-support per pair; witness-family criterion vs direct modular addability on all 8 + 16 + 32 subsets (688 comparisons, 0 failures). Hole histograms agree exactly with 6.2 (M = 7: 0:1, 1:3, 4:4; M = 13: 0:5, 6:6, 9:5; M = 21: 0:6, 5:6, 6:3, 12:1, 13:9, 15:1, 16:6). Exact rational moments agree exactly with all six table rows (e.g. M = 21, ρ = 1/4: E U = 13662/1024, E U² = 192510/1024, P(U = 0) = 16/1024); G for M = 21 has 15 points, the point with t_x = 5 is omitted, as stated.
3. Lifts (6.3): all 407 height assignments for H = 2, 3; every lift integer Sidon; all 3,488 occupied-residue points addable; minimum initial holes 3, 8, 5, 13, 7, 19 and best ascending-greedy final sizes 4, 5, 5, 6, 6, 7 agree exactly; two-phase repair added at most H−1 in phase one in every row and satisfied (5) in every case.
4. Cubic curves (6.4), p = 5, 7, 11, 13, 17, 19, 23, 29, 31: |T_p|, |Q ∪ C_p| = p(p+1)/2, and the unblocked count agree exactly with the table and with (7), (10) in the correct χ(2) branch; the criterion (8)–(9) matched membership in T_p at all p³ points for every p (0 mismatches).
5. Beyond the report: Singer sets built from GF(q³) for q = 7, 11 (exact over all 2^k subsets) and q = 13, 17, 19 (20,000 Monte Carlo samples) at ρ ∈ {1/2, 0.3, k^{−1/3}}. In every case P(I_x = 1) ≥ w_x for all x ∈ G, Var U ≤ g + g(g−1)ε, E U ≥ g b, and (for the exact cases) Cov(I_x, I_y) ≤ ε for all pairs.
6. Constant chain of 4.5 at and beyond the onset in 50-digit arithmetic, five (C,θ) pairs: (16) ≤ (17) throughout; ρ ≤ 1/2 throughout.

What I could not check: nothing in the report is left unverified. The asymptotic statement (17) is verified by proof re-derivation plus high-precision evaluation at the onset; it cannot be tested by sampling because the onset exceeds any constructible example.

## 4. Honest status

The honest status for the research target is OPEN, not PARTIAL. Reasoning:
- The only positive "bound" proved, (5), is a trivial consequence of monotone blocking plus the elementary difference count (4); it bounds nothing about s(N) without the unproved estimate u ≤ Ck.
- Sections 3 and 4 are correct negative results: an exact non-maximality count for one specific algebraic set in a group model, and a second-moment proof that one specific sampler fails. Neither moves the upper bound. The report itself writes "The brief's improved upper-bound target remains OPEN" in its scope paragraph, and its STATUS line admits "No bound s(N) ≪ N^(1/3)(log N)^θ with θ < 1/3 is proved".
- Nothing is dressed up inside the body: the Section 4 obstruction is explicitly scoped to "independent thinning of perfect difference sets" and the Section 3 count is explicitly a group-model statement. The only overstatement is the status word.

Repair R1: change the STATUS word from PARTIAL to OPEN, keeping the rest of the first line. R2 and R3 are as stated above (Section 2.4 dependence argument; frank onset statement next to (17)).

## 5. Value assessment

Usable lemma: Section 2.2's exact criterion (3) is a clean, correct statement that stacking several integer levels over a modular Sidon support costs at most H−1 extra elements in total before the occupied fibres are saturated, which reduces route (a) to the single question of bounding the unblocked points in unoccupied residues (u in (5)). Usable negative results: (10) shows the cubic curve in F_p³ leaves roughly half of the group unblocked, so it is not a candidate host without a fundamentally different repair; (16)–(17) show that pure independent thinning of a Singer set at density k^{−1/3}(log k)^θ, θ < 1/3, leaves unblocked outside points with probability at least 1 − J(C)k^{−1/6}, so a second-moment argument cannot rescue the unmodified sampler. Note also that this sampler can never yield a maximal set unless A = D (omitted elements of D stay addable), so it only ever models the outside-coverage half of the problem.

Exact remaining obstruction: no construction in the report controls the number of initially unblocked points in unoccupied residues (u in (5)) or the cost of repairing the holes left by random thinning; both routes stop exactly where the known union-bound log factor enters, and nothing proved here removes it.
