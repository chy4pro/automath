PASS-WITH-REPAIRS

# Referee report: PROBE_ASTRA_2_20261009.md (T6, Erdős #30 beyond the kernel barrier), round 4

Referee: referee-1 (clean room: only the file under review, the task brief, and standard mathematics; no other repository files, no web). Independent checks in python3 (~10 CPU-seconds total).

Summary verdict. Every statement the report labels as proved is correct; I re-derived each step and found no gap, circularity, or silently assumed lemma. All reported exact computations (Sections 1.5, 4.1, 4.2, 4.3) reproduce exactly. The required repairs concern the STATUS label and two presentation points, not the mathematics: the three "proved" items are elementary and none of them constrains the constant c, so the honest status is OPEN, not PARTIAL (details in the Status section below).

## 1. Claim-by-claim verdicts

Line numbers refer to the file under review.

### Scope and conventions (lines 3-11)
- Sidon = distinct positive differences, stated equivalent to unique unordered sums with repetition. VALID (both directions re-derived; the degenerate case a=b is handled correctly by positivity of differences).
- Explicit disclaimer that f and C(N,T) are not specified in the brief and that V_tri is the author's own test energy (line 9). Honest and appropriate.

### 1.1 Exact moment formulas, eq. (1)-(4) (lines 27-67)
- (1): sum r = S, sum r^2 = S+2P, sum r^3 = S+6P+6H. VALID. Each point lies in exactly T of the W windows (a <= x <= a+T-1 stays inside [1,W]); a pair/triple lies in max(0, T-span) windows; u^2 = u+2C(u,2), u^3 = u+6C(u,2)+6C(u,3) checked.
- (2): VALID (D(d) <= 1 and sum_{d<T}(T-d) = T(T-1)/2).
- (3): V_tri = Q/T >= 0 and positive-definiteness of the triangular kernel. VALID; the normalization m^2 T/W is just the window mean, as the report says.
- (4): 6H = W mu(mu-1)(mu-2) + 3(mu-1)Q + R. VALID, re-derived symbolically (R = sum r^3 - 3 mu sum r^2 + 2 W mu^3, substitute sum r^3 = 3 sum r^2 - 2S + 6H and sum r^2 = W mu^2 + Q). Also verified exactly (rational arithmetic) on all 87,240 (N,A,T) instances with N <= 16.
- Remark at line 67 ("a lower bound for H cannot by itself be substituted for a lower bound for Q"). VALID as stated. Note, however, that the Sidon property supplies only UPPER bounds on third-order correlations (C_3(u,v) <= 1, line 106), and by (4) an upper bound on H bounds 3(mu-1)Q + R from above, never Q from below. This makes Proposition 1.4 expected rather than surprising; see repairs.

### 1.2 Integrality, eq. (5)-(8) (lines 69-98)
- (5) Q >= W theta(1-theta), with equality iff all r in {q,q+1}. VALID (expanded sum (r-q)(r-q-1) >= 0 by hand).
- (6): VALID; floor(y) >= y/2 for y >= 1, W <= 2N, m >= sqrt(N)/2.
- (7), (8): VALID (u(u-q)(u-q-1) >= 0 for integers u >= 0; Cauchy-Schwarz on r^{3/2}, r^{1/2}).

### 1.3 Third-order correlation bounds, eq. (9)-(11) (lines 100-137)
- C_3(u,v) <= 1: VALID.
- (9) H <= C(T,3): VALID (span count sum_{v=2}^{T-1}(v-1)(T-v) = C(T,3)).
- (10) H <= U_T <= sqrt(2T) T(T-1)/2: VALID. k_d+2 = floor((1+sqrt(1+8d))/2) is exactly the largest q0 with q0(q0-1) <= 2d, so an endpoint pair of difference d has at most k_d interior points; at most one endpoint pair per d. k_d <= sqrt(2d) from (k_d+2)(k_d+1) <= 2d.
- (11) U_T >= T^{5/2}/64 for T >= 64: VALID (count of d in [ceil(T/4), floor(T/2)] is >= T/4 - 1/4 >= T/8 for T >= 8; T-d >= T/2; k_d >= sqrt(2d) - 5/2 >= sqrt(T)/4 for T >= 64). Numerically confirmed for every T in [64, 3000] with exact integer arithmetic (the inequality in fact already holds from T = 4 on).

### 1.4 Proposition (lines 139-199)
- Construction of balanced arrays, Q = k(W-k)/W <= W/4: VALID.
- S_max = s(W+1), q = s, k = s at S_max: VALID.
- Balanced array minimizes sum r(r-1) at fixed mass; minimum nondecreasing in mass: VALID (exchange argument; +2q per unit mass).
- sum r(r-1) <= s^6 - s^4 + s^2 + s <= s^6 - s^3 = T(T-1) for s >= 2: VALID.
- Every integer in [0, T(T-1)/2] is a subset sum of {1,...,T-1}: VALID (standard induction).
- H <= (8/3) s^7 < 4 s^7 <= s^{15/2}/64 <= U_T for s >= 65536: VALID; the onset is exactly sqrt(s) >= 256. H <= C(T,3) for s >= 8: VALID.
- (12) Q/(Tm) <= 1/(2s): VALID.
- Quantifiers: the proposition is explicitly about integer arrays satisfying the listed scalar constraints, "not asserted to come from a set A" (line 154), and the unenforced conditions (window boundary ramps, compatibility of individual C_3(u,v) with one set) are listed at line 199. Honest.
- Independent check: all six (s,m) aggregate instances of Section 4.3 reproduce (see Section 3 below). I additionally computed the exact U_T for T = s^3 with s in {2,3,4,5,8,16,32,64,128} and found H <= U_T for the balanced arrays at every one of them, so the onset s >= 65536 is an artifact of the chain through (11), not a feature of the statement.

### 1.5 Example sets A, B (lines 201-223)
- Both sets Sidon with the identical difference set {1,...,13,16,17}; W=22, S=30, P=10, H(A)=1, H(B)=0, sum r^2 = 50 for both, sum r^3 = 96 and 90, Q = 100/11, V_tri = 20/11. ALL VALUES REPRODUCED EXACTLY.
- "Identical sum f((a-b)/T) for every f": VALID (identical ordered-difference multisets). "R changes by exactly 6": VALID from (4).

### 2. Proposition (lines 225-301)
- b_i = 2p i + (i^2 mod p), 0 <= i <= p-2, is Sidon: VALID (2p | difference of residue differences forces equal index gaps h, then h invertible mod p and p odd force i = k). I also verified Sidon-ness by brute force for all odd primes p < 300 (even including the index i = p-1, which the report omits only to get exactly 2m = p-1 points).
- B0 = 8m^2+2 (residue of (p-2)^2 is 4 for p > 4): VALID.
- Joint Sidon property of A_left union A_right: VALID. Internal differences are <= B0; cross differences are >= N - B0 > B0 once N > 2B0 (the report uses the slightly stronger N > 2B0+1, which holds since (100/69)^4 > 4 and 4m^4 > 16m^2+5 for m >= 3).
- Endpoint placement L >= 2p^2 > B0+1 for m >= 30: VALID (100000/328509 > 3/10 checked by cross-multiplication; m^2 - 8m - 3 > 0 at m = 30).
- Disjoint windows (2L <= N^{3/4}/5 < N): VALID.
- (13), (14): VALID (mean value theorem on t^{1/4}; (69/100)^4 < 1).
- Infinitely many primes: VALID (and unnecessary to belabour).
- Limitation paragraph (line 301) is honest: only 2m ~ 1.38 N^{1/4} points, no bulk, difference 1 absent.
- Independent check: all four rows of the table at lines 412-423 reproduce exactly (N, L, B0, number of differences, smallest difference 69/111/273/1041, both window counts = m). The onset p >= 61 is conservative: the construction already works at p = 59 (L = 7424 > B0+1 = 6731); it fails for p <= 53. Not an error.

### 2.1 Difference budgets (15)-(16) (lines 303-321)
- VALID. q(q-1) distinct differences in {1,...,L-1}; q^2 cross differences in [N-2L+1, N-1], an interval of 2L-1 integers. The numerical constants 4761/500 and 4761/1000 and the onsets N >= 256 (for the floor absorptions) and N >= 10^4 (for ratio < 1) check out.

### 3. Other closures (lines 323-363)
- Item 2 (jump identity sum (r(x)-r(x-1))^2 = 2m - 2D(T)): VALID.
- Item 3 (telescoping, m <= s^2 + s + 1/2 at N = s^4): VALID; this is the classical N^{1/4}-coefficient-1 argument, correctly derived, including sqrt(1+1/s) <= 1 + 1/(2s).
- Item 4 (fourth Fourier moment = 2m^2 - m): VALID.
- Item 5 (triples with equal sum are pairwise disjoint; C(m,3) <= Nm): VALID.
- Items 1 and 6 are summaries; consistent with the body.

### 4. Computations (lines 365-453)
- Table 4.1 (Sidon-subset counts for N <= 24, F(N), largest saturated initial difference run): REPRODUCED EXACTLY, all 24 rows. Totals 6,276 sets and 87,240 (N,A,T) instances for N <= 16 also match my enumeration.
- 4.2, 4.3: reproduced (above).

## 2. Errors found

None in the mathematics. No step uses a hypothesis before it is available; no circularity; conventions (unordered sums with repetition, positive differences, window counts over x in [1,W]) are used consistently throughout.

## 3. Independent re-checks actually run

All exact (Python integers / fractions.Fraction / Decimal at 60 digits), ~10 CPU-seconds total.

1. Exhaustive enumeration of all Sidon subsets of {1..N} for N <= 24 (recursion on increasing elements with a used-difference set). Counts, F(N) and the saturated-run column agree with the report's table in all 24 rows. F(N) also agrees with the known optimal Golomb ruler lengths 1, 3, 6, 11, 17.
2. For every Sidon A subset {1..16} and every T in [1,N]: identities (1) and (4) (exact rationals), inequalities (2), (5), (7), (8), (9), (10), and H = sum C(r,3). 87,240 instances, 0 failures.
3. Section 1.5 sets A, B: difference sets, Sidon-ness, W, S, P, H, sum r^2, sum r^3, Q, V_tri at (N,T) = (18,5). Exact agreement.
4. U_T computed exactly for T <= 3000; (11) holds for all T in [64, 3000] (and for all T >= 4); U_T <= sqrt(2T) T(T-1)/2 holds for all T tested.
5. Section 2 family for p = 61, 101, 257, 1009: N = ceil((100m/69)^4) via exact integer arithmetic, L = floor(floor(N^{3/4})/10) via exact integer fourth root (this equals floor(N^{3/4}/10)), all C(2m,2) positive differences distinct, window counts exactly m and m, 2L < N, inequalities (13) and (14) checked at 60-digit precision. The four table rows (N, L, B0, number of differences, smallest difference) agree exactly.
6. Section 4.3 aggregate checks at s = 65536 and s = 100000 for m in {s^2, s^2 + floor(94s/100), s^2 + s}: sum r(r-1) <= T(T-1), (64H)^2 <= T^5, H <= C(T,3), 2s k(W-k) <= WTm. All six pass. Extra: with exact U_T at s in {2,...,128}, H <= U_T also holds, although (64H)^2 <= T^5 fails for 3 <= s <= 64 (so the proof's onset really comes from (11), as stated).
7. Onset probe for Section 2: the construction works at p = 59 and fails at p <= 53; the stated onset p >= 61 is therefore safe.

## 4. What I could not check

Nothing in the report is unverifiable; all statements are finite or fully elementary. I did not reproduce the author's Node.js CPU timings (irrelevant to correctness).

## 5. Honest status

The STATUS line says PARTIAL. In my judgement the honest status is OPEN, for the following reasons.

- Section 1 (identities (1)-(4), bounds (5)-(11)) is routine bookkeeping; (4) is an algebraic identity and (9)-(11) are counting bounds. None interacts with the kernel barrier.
- Proposition 1.4 is correct but essentially tautological: the only third-order input available from the Sidon property is the upper bound C_3(u,v) <= 1, hence only upper bounds on H; by identity (4) an upper bound on H can only bound 3(mu-1)Q + R from above. The balanced array satisfies every upper bound because it has the minimal possible H. So the proposition records that an approach nobody should expect to work does not work. It is a valid negative statement about the author's own relaxation, not a general obstruction, and the report does say this (lines 154, 199); but the word "limitation" in the STATUS line reads stronger than the content.
- The Section 2 proposition is a special case of a trivial general fact: any Sidon set of q points inside a window of length L and any Sidon set of q points inside a disjoint window placed at distance > L are jointly Sidon, and a Sidon set of q ~ 0.69 N^{1/4} points fits in a window of length L ~ 0.1 N^{3/4} with enormous room (q^2 ~ 0.48 N^{1/2} << L). The quadratic-residue construction and the prime p are unnecessary decoration. The brief's realizability obstruction is about coexisting with the bulk and saturating every short difference, which the report explicitly does not address (line 301).
- Nothing in the report produces any inequality on c, any kappa > 0, or any restriction on the extremal profile beyond the budget inequalities (15)-(16), which the report itself shows are slack by a factor ~N^{1/4}.

The report is otherwise honest: it states on line 1 that no bound with c < 2 sqrt(2)/3 is proved, it labels V_tri as its own test energy, and it lists the unenforced conditions. There is no group-vs-interval conflation (everything is in the integers) and no single-sampler result presented as general. The overstatement is confined to the PARTIAL label and to the unqualified phrase "realizing both proposed endpoint clusters".

## 6. Repairs required for PASS

R1 (line 1). Replace PARTIAL by OPEN, or at minimum append: "all three items are elementary and none constrains c." Qualify the endpoint clause as "realizing both endpoint clusters with no bulk and no short-difference saturation."

R2 (Section 1.4, after line 154 or at line 199). State explicitly that the relaxation contains only upper bounds on third-order quantities, that the Sidon property yields no lower bound on H or on R, and that by (4) an upper bound on H cannot lower-bound Q; hence the proposition is the expected outcome and its real content is "seed (a) needs a third-order LOWER bound from the 0/1 structure, which C_3 <= 1 does not give." Optionally note that the exact H <= U_T holds for the balanced arrays already for small s (checked for s <= 128), so s >= 65536 is only a proof onset.

R3 (Section 2, after line 301). Add that the construction is an instance of the general two-window gluing fact above, so the specific prime construction carries no additional information about the target.

R4 (line 272, wording). "All internal differences within either block are distinct, including across the two blocks" should read: "the internal differences of the left block and those of the right block are pairwise distinct, since all are differences of distinct pairs of the Sidon set {b_i}."

## 7. Value assessment

Usable negative result: the Sidon property gives only upper bounds on third-order window correlations (C_3(u,v) <= 1, hence H <= U_T <= sqrt(2T) T^2/2), and by the exact identity (4) upper bounds on H cannot produce a lower bound on the residual Q; so seed (a) in its literal form (third-order correlations as the extra 0/1 input) cannot work unless some third-order LOWER bound, or control of the centered third moment R, is extracted from the set structure. The two six-point sets of Section 1.5 are a clean witness that pair data do not determine H. Usable lemma: the endpoint budgets (15)-(16) show that isolated end-cluster counting is slack by a factor of order N^{1/4}, so any realizability obstruction for seed (b) must couple the end clusters to the bulk and to the saturation of short differences. The exact remaining obstruction is unchanged from the brief: no quantity has been identified that is of order |A| in the residual energy and that distinguishes 0/1 sets from the balanced relaxations.
