RESEARCH NOTE — transfer targets for the exact-boundary-capacity tool. Same-session derivations by one Claude agent, UNREVIEWED.
Literature status is from a bounded web/arXiv pass (2026-10-02, ~20:10–20:40 UTC); it is NOT a G2. No novelty or priority is claimed anywhere below.

# Where the exact boundary constant transfers (2026-10-02)

## 0. The tool, in the form used below

From `problems/erdos30/SIDON_BOUND_PROOF.md` §2–§5, §7 and `KERNEL_OPTIMALITY.md` §1:

* Kernel f = h * h~, h(t) = 2(1-t) on [0,1]; f >= 0, even, nonincreasing on [0,inf), integral 1,
  a = f(0) = 4/3, and sum_{d>=1} f(d/T) <= T/2 for every T > 0.
* Lemma 6: for L >= 1 there is a finite signed measure nu_L with potential f*nu_L = 1 on the closed
  [0,L] and E(nu_L,nu_L) <= L + b + 200 e^{-alpha L}, b = 2/3, alpha = log(4/3).
  By Cauchy–Schwarz any positive measure mu of mass k on [0,L] has E(mu,mu) >= k^2/(L + b + eps).
* Barrier (1D, scalar method): a*b >= 8/9 for every admissible kernel; the ramp attains it.

Generic consequences used repeatedly (all are elementary and were re-derived here):

| shape of the final scalar inequality | second-order constant | Lindström-type value (a*b = 1) |
|---|---|---|
| k^2 <= (N/T + b)(T + A k), A = (multiplier)*a | sqrt(A*b) * N^{1/4} | sqrt(multiplier) |
| Sidon in [N]^d, product kernel | ((d+1)/2) (ab)^{d/(d+1)} N^{d^2/(2d+2)} | (d+1)/2 |
| three-term AM–GM (2D problems) | 3 (product of the three weights)^{1/3} | 3 × (same with 1's) |

The 2D products need no new capacity lemma: for a product kernel F = f(x/T1) f(y/T2) and the
product test measure nu_{L1} ⊗ nu_{L2}, the potential is identically 1 on the box and the energy is
the product of the 1D energies (Fubini). Non-box regions (discs, hexagons) DO need a new lemma.

New ingredient found in this pass (sonar sequences only): when one coordinate marginal of the
point set is known exactly (one dot per column), Cauchy–Schwarz against lambda ⊗ nu_L, with
lambda the exact column measure, replaces the boundary constant b in that coordinate by the first
moment m1 = ∫|t| f(t) dt (1/3 for the triangle kernel). See §3.1.

## 1. Ranked table

Constants are second-order coefficients (or diameter coefficients where stated). "Ours" = what the
method gives; every "ours" entry is an unreviewed same-session derivation.

| # | target | current record (source, year) | argument behind record | ours | improvement? | missing lemma | confidence |
|---|---|---|---|---|---|---|---|
| 1 | Sonar sequences: n rows, m columns, one dot/column, all difference vectors distinct; max m | m < n + 5n^{2/3} (Thm 4, large n); proof gives m < n + 4n^{2/3} + 4n^{1/3} + 1; "Comment: more careful computation shows m < n + 3n^{2/3} + 2n^{1/3} + 9 for all n" (no proof printed). Erdős–Graham–Ruzsa–Taylor, Combinatorica 12 (1992) 39–44 | Erdős–Turán R×R windows, boundary loss 1 in both coordinates; optimum of that method is exactly 3 (checked numerically, §4) | **m <= n + 2 n^{2/3} + O(n^{1/3})** (triangle kernel + exact column marginal in x, ramp + exact capacity in y). Cos-bump x-kernel would give ≈ 1.949 (not worked out rigorously) | yes, 3 → 2 vs the unproved comment; 4–5 → 2 vs the printed proofs | none for the asymptotic statement; explicit O(n^{1/3}) term and onset need writing (numerically ≈ +2.62 n^{1/3} for n ≥ 1e5) | medium-high (algebra and numerics checked; new exact-marginal step unreviewed; no post-1992 upper bound found, search bounded) |
| 2 | Weak Sidon sets (a_i + a_j distinct for i < j) in [N] | W(N) <= N^{1/2} + (sqrt3 − gamma) N^{1/4} + O(1), gamma >= 0.0089, i.e. coefficient ≈ 1.7232. Balogh–Füredi–Roy, Amer. Math. Monthly 130 (2023) 437–445 (arXiv 2103.15850, Thm 5.1). Earlier: Kayll, Discrete Math. 299 (2005): sqrt3; Ruzsa 1993: 4 (+11) | Lindström/Kayll small-difference count with diagonal multiplier 3, plus BFR "tension" | **sqrt(8/3) = 1.63299** | yes (1.7232 → 1.6330) | none (3-AP accounting is BFR's own structural lemma, re-proved §3.2); explicit onset: redo §6 algebra (scan: "+2" works for N >= 90^4) | high |
| 3 | g-thin Sidon sets = g-Golomb rulers = B_2^-[g] (each nonzero difference <= g times), g >= 2 | diam >= g^{-1}k^2 − (2 − eps) g^{-1} k^{3/2} − O(k), eps >= 0.0062 g^{-4} (journal abstract; arXiv v1 says eps >= 0.02 g^{-2}): Carter–Hunter–O'Bryant, Acta Math. Hungar. 175 (2025) 108–126 (arXiv 2310.20032). Explicit size form: S_t(n) < sqrt(tn) + (tn)^{1/4} + 1/2, BFR (6.1); BFR Thm 6.2: (1 − gamma_t) with gamma_t unspecified, proof omitted | Lindström set-systems + tension | **|A| <= sqrt(gN) + (2sqrt2/3)(gN)^{1/4} + 1 for gN >= 120^4**; diameter: g·diam >= k^2 − (4sqrt2/3) k^{3/2} − O(k) | yes for every g >= 2 (coefficient 1 − O(g^{-4}) → 0.9428) | none: literal substitution N → gN in Lemma 7 / §6 | high |
| 4 | Difference triangle sets / strict optical orthogonal codes: min scope m(n,k), n rulers with k+1 marks, all differences distinct | m(n,k) >= n(k^2 − 2k sqrt k + (k + sqrt k)/4) for all n,k: Kløve, IEEE Trans. IT 34 (1988) 355–361, Thm 2 (statement read from Chee–Colbourn 1997, not from Kløve). LP bounds (Lorentzen–Nilsen 1991, Shearer 1999) are numerical/small cases | Erdős–Turán windows summed over rulers | **m(n,k) >= n((sqrt(4k + 8/9) − 2sqrt2/3)/2)^4 − 1 = n(k^2 − (4sqrt2/3)k^{3/2} + O(k)) for k >= 20365, all n** | asymptotically yes (2 → 1.8856); irrelevant for the small k that engineering tables care about | none: literal substitution N → (m+1)/n | high |
| 5 | Distinct-difference configurations, square grid, Manhattan diameter r: max dots m | m <= r/sqrt2 + (3/2^{4/3}) r^{2/3} + O(r^{1/3}) (= 1.19055): Blackburn–Etzion–Martin–Paterson, IEEE Trans. IT 56 (2010) 1216–1229, Thm 9 (arXiv 0811.3832). Leading term attained by their construction | Erdős–Turán with Lee-sphere windows; boundary via covering count | **r/sqrt2 + 3·2^{-4/3}(8/9)^{2/3} r^{2/3} = r/sqrt2 + 1.10064 r^{2/3}** | yes (7.5% on the second term) | none: product kernel in u = x+y, v = x−y; index-2 lattice sum | medium-high (no later bound found; search bounded) |
| 6 | Sidon sets in [N]^d (d >= 2), Golomb rectangles | F([N]^d) <= N^{d/2} + O(N^{d^2/(2d+2)}): Lindström, J. Number Theory 4 (1972) 261–265 (as quoted by O'Bryant 2004 and Lee 2014; primary paywalled, NOT read). Cilleruelo 2010 (JCTA 117) supplied the LOWER bound, not the upper | box windows (inferred from the exponent; unverified) | c_d = ((d+1)/2)(8/9)^{d/(d+1)}: d=2: 1.38672, d=3: 1.83090 | unknown: whether any explicit constant was published is unverified; the ab = 1 analogue is (d+1)/2 | none for boxes | derivation high; improvement status unknown |
| 7 | Sidon sets in a union of k intervals (total size n), k = o(n^{1/4}) | sqrt n + sqrt k n^{1/4} + o(n^{1/4}): Riblet, Acta Math. Hungar. 167 (2022) 533–547, Thm 3.1(iii) (arXiv 2202.01296) | windows; boundary loss u per interval | sqrt(8k/9) only if every interval is long (>= ~0.25 T); worst case gives sqrt k again | not in general | short intervals: ramp capacity C(L) − L → 1/a = 3/4 as L → 0 (> 2/3), so a·sup(C − L) = 1 — needs a new idea | low |
| 8 | DDC in hexagonal grid / Euclidean diameter (BEMP Thms 11, 12–15) | BEMP 2010, e.g. Euclidean: (sqrt(pi)/2) r + 3 pi^{1/3}2^{-5/3} r^{2/3} | windows of the region's shape | not computed | unknown; leading terms not tight there (BEMP Table I), so the second term matters less | capacity of non-axis-parallel boundaries: oblique 1D projections of the kernel and kernel-shape optimisation | low |
| — | Golomb ruler length G(k) (same problem as R1, listed for completeness) | published CHO 2025: k^2 − 1.96365 k^{3/2} − O(k); preprint Hou–Zhao 2026: 2·0.943493 = 1.886985 | — | k^2 − (4sqrt2/3) k^{3/2} − O(k) = 1.885618 | direct corollary of R1, not a new transfer | none | as R1 |

Recommendation: items 2, 3, 4, 5 are each a half-page corollary of Lemmas 6–7; they could be one
"corollaries" note after a G2 per item. Item 1 has the largest gain and a new step (exact column
marginal); it deserves its own isolated referee before anything else. Item 6 needs only a primary
read of Lindström 1972 to decide whether it is an improvement or a first explicit constant.

## 2. Part 1 — status of every candidate checked

Access window 2026-10-02 ~20:10–20:40 UTC. "Read" = primary text inspected in this pass.

(a) **Sidon sets in [N]^d.** Upper bound N^{d/2} + O(N^{d^2/(2d+2)}) is Lindström 1972 (Theorem 1
of "On B2-sequences of vectors", per O'Bryant's annotated bibliography, arXiv math/0407117 p.22,
and per S. J. Lee, arXiv 1405.4227 §1). Cilleruelo 2010 ("Sidon sets in N^d", JCTA 117, 857–871)
proved the lower bound F([n]^d) >= n^{d/2} − O(n^{5d/16}). Neither secondary source prints an
explicit second-term constant; the primary (ScienceDirect) returned 403/bot pages, so whether
Lindström's proof has an explicit constant is **unverified**. Argument: the exponent d^2/(2d+2) is
exactly the box-window Erdős–Turán balance (re-derived §3.6), so a box-window argument is likely.

(b) **Sidon sets in Z_N and finite abelian groups.** Counting gives k(k−1) <= N − 1, attained
infinitely often (Singer). No boundary, no window term: **no transfer.** (F_2^n has a different,
leading-order problem.)

(c) **B_2[g] / g-Golomb rulers.** Two different problems:
* sum version r_{A+A}(x) <= g: the *leading* constant is open (Cilleruelo–Ruzsa–Trujillo,
  Green, Yu, Martin–O'Bryant, Cilleruelo–Jiménez-Urroz; status as summarised in Johnston–Tait–
  Timmons, arXiv 2105.03706). Kernel/autoconvolution problem at leading order; the boundary term
  is irrelevant. **No transfer.**
* difference version (g-thin, g-Golomb rulers): leading term sqrt(gN) is asymptotically sharp
  (Caicedo–Martos–Trujillo, "g-Golomb rulers", Rev. Integr. 33 (2015) 161–172, as cited by BFR
  Thm 6.1). Second-order record: CHO 2025 / BFR (6.1). **Target #3.**

(d) **Golomb rulers and DTS.** Golomb ruler length: corollary of R1 (table, last row).
DTS: Kløve's closed form (above) is the only general asymptotic lower bound found; Chee–Colbourn
(IEEE IT 43, 1997), Shearer (EJC 6, 1999, LP), Shehadeh–Kingsford–Kschischang (arXiv 2502.19517,
2025) all cite Kløve/LP and add constructions. Ma–Yi (arXiv 2608.13739, Aug 2026) use "Kløve's
small-difference argument" for packings, not a new DTS asymptotic. **Target #4.**

(e) **Sonar / Costas / Golomb rectangles.** Sonar: EGRT 1992 (read; pages 42–43). Their own
abstract says 4n^{2/3}, Theorem 4 says 5n^{2/3}, the post-proof Comment says 3n^{2/3} + 2n^{1/3} + 9
"for all n" without proof. Ruiz–Trujillo–Caicedo (arXiv 1311.1679, 2013) and Delgado–Martos–Trujillo
(IEEE Access 2022) are constructions; no later upper bound was found. Moreno–Games–Taylor 1993 is
by its title a construction table (not read). Blokhuis–Tiersma 1988 concerns radar arrays (a
different, row-restricted condition; not read). Costas arrays: no upper-bound question.
Golomb rectangles = Sidon sets in [n1]×[n2] → item 6. **Target #1.**

(f) **Optical orthogonal codes, lambda = 1.** Cyclic OOCs: Johnson bound by counting in Z_N, no
boundary, **no transfer.** Strict OOCs are equivalent to DTS (Chu–Golomb, as stated in
Shehadeh et al. 2025 §II-C) → item 4.

(g) **B_h, h >= 3 and k-fold Sidon sets.** Leading constants open (B_h: Green 2001 etc.;
k-fold Sidon: Cilleruelo–Timmons 2014 upper (N/k)^{1/2} + O(·) vs constructions (1/k + o(1))N^{1/2}
for some coefficient sets). Second-order terms are not the frontier. **No transfer.**

(h) **Weak Sidon** → **target #2** (record BFR 2023 Thm 5.1, read). **LM rulers**
(Gupta–O'Bryant arXiv 2605.14229): diameter order n^{3/2}; the energy method with the first
moment gives diam >= k^{3/2}/(2 sqrt(a m1)); the best h >= 0 found numerically is the cosine bump
with a·m1 = pi^2/32 = 0.30843, i.e. 0.9003 k^{3/2} < their 2sqrt2/3 = 0.9428. **No transfer**
(unless signed-h kernels reach a·m1 < 0.28125; unexplored; trivial lower bound a·m1 >= 1/4).

(i) Infinite Sidon sequences: skipped as instructed.

Extras found: Manhattan DDC (item 5), unions of intervals (item 7), hex/Euclidean DDC (item 8),
modular sonar sequences (trivial bound n <= m + 1 from shift 1, method gives exactly that: no
gain), difference bases (covering problem, leading constant: not a boundary-term problem).

## 3. Part 2 — derivations

Notation: a = 4/3, b = 2/3, gamma = 2sqrt2/3, eps(L) = 200 e^{-alpha L}, alpha = log(4/3).
"[unverified]" marks steps not independently reviewed; all algebra below was re-checked
numerically (§4) but that is not a proof review.

### 3.1 Sonar sequences (item 1)

Set-up. Columns j = 0..m−1, values f_j in {0..n−1}; sonar ⇔ the vectors (j − j', f_j − f_j')
over ordered pairs j ≠ j' are pairwise distinct (vectors with positive first coordinate are distinct
by definition; their negatives have negative first coordinate). Point measure mu = Σ_j δ_{(j,f_j)}.

Kernel F(x,y) = f1(x/T1) f2(y/T2), f1(t) = (1 − |t|)_+ (triangle, autocorrelation of 1_[0,1],
a1 = 1), f2 = ramp autocorrelation (a2 = 4/3). T1 integer in [1,m], T2 real in (0,n].
F is the autocorrelation of a product function, hence positive definite (as in Lemma 2).

Upper bound. E_F(mu,mu) = (4/3) m + Σ_{distinct v, v1≠0} F(v) <= (4/3)m + (Σ_{v1≠0} f1(v1/T1))(Σ_{v2∈Z} f2(v2/T2))
<= (4/3)m + (T1 − 1)(T2 + 4/3), using Σ_{v1∈Z} f1(v1/T1) = T1 exactly for integer T1 and
Σ_{v2} f2(v2/T2) <= T2 + a2.

Lower bound (the new step). Let lambda = Σ_{i=0}^{m−1} δ_i (the exact column marginal) and rho the
T2-dilate of nu_L, L = n/T2 >= 1, so that ∫ f2((y − s)/T2) d rho(s) = 1 for y in [0,n].
With nu = lambda ⊗ rho: E_F(mu,nu) = Σ_j Σ_i f1((j−i)/T1) · 1 = Λ, and E_F(nu,nu) = Λ · E(nu_L,nu_L).
Cauchy–Schwarz gives Λ <= E_F(mu,mu)(L + 2/3 + eps(L)). For the triangle and integer 1 <= T1 <= m,
Λ = Σ_{i,j<m} (1 − |i−j|/T1)_+ = m T1 − (T1^2 − 1)/3 (identity checked for all m < 40).

Result (rigorous modulo review):

    m T1 − (T1^2 − 1)/3  <=  (n/T2 + 2/3 + eps(n/T2)) · ( (4/3) m + (T1 − 1)(T2 + 4/3) ).      (S)

Asymptotics. Divide by T1; with m = n + O(n^{2/3}) and T1, T2 ≍ n^{2/3}:
m <= n + T1/3 + (2/3) T2 + (4/3) n^2/(T1 T2) + O(n^{1/3}).
AM–GM over the three terms: minimum 3·((1/3)(2/3)(4/3))^{1/3} n^{2/3} = 3·(8/27)^{1/3} n^{2/3} = 2 n^{2/3},
at T1 = 2 n^{2/3}, T2 = n^{2/3}. Hence **m <= n + 2 n^{2/3} + O(n^{1/3})**.

Bookkeeping of the gain. General form: 3((a1·m1)(a2·b2))^{1/3}, m1 = ∫|t| f1.
EGRT windows = (a1 b1)(a2 b2) = 1·1 → 3. Exact capacity in both directions (no marginal trick):
3(8/9)^{2/3} = 2.7735. Exact marginal + box y: 3(1/3)^{1/3} = 2.080. Both: 2.000.
So most of the gain comes from the exact column marginal, a sibling of the exact-capacity idea,
not from b = 2/3 itself. With h >= 0 the infimum of a1·m1 found numerically is pi^2/32 (cosine
bump h = (pi/2) sin(pi x) on [0,1]), giving 3(pi^2/36)^{1/3} ≈ 1.949 [lattice-sum errors for that
kernel not worked out]. Trivial floor of this route: a1·m1 >= 1/4 ⇒ constant >= 3(2/9)^{1/3} ≈ 1.817.

Explicit form [numerical scan only, not a proof]: the minimum of the bound from (S) over a grid of
(T1,T2) gives m − n − 2n^{2/3} ≈ 2.62 n^{1/3} for 1e5 <= n <= 1e10, and is already below EGRT's
comment bound at n = 1000 (305 vs 329). A clean "for all n >= n0" statement needs the §6-style
monotonicity argument.

### 3.2 Weak Sidon sets (item 2)

Structure (BFR §5.1, re-proved): let r(d) = #{(x,y) ∈ A^2 : x − y = d}. If d > 0 has two
representations (x,y) ≠ (x',y'), then x + y' = x' + y with both pairs of distinct elements, so the
two unordered pairs coincide; as x ≠ x', this forces x = y' or x' = y, i.e. the two pairs form a
3-AP with common difference d. Three representations would give a 4-term AP (x, x+d, x+2d, x+3d)
and x + (x+3d) = (x+d) + (x+2d), a forbidden coincidence. Hence r(d) <= 1 + [d ∈ P], P = set of
3-AP common differences. An element y is the middle of at most one 3-AP (else (y−d)+(y+d) =
(y−e)+(y+e)), and distinct 3-APs have distinct differences, so |P| <= k − 2.

Energy: E <= a k + 2Σ_{d>=1} f(d/T) + 2Σ_{d∈P} f(d/T) <= a k + T + 2a(k − 2) < 4k + T.
With Lemma 6 (A translated into {0..N−1}, 0 < T <= N):

    k^2 <= (N/T + 2/3 + eps(N/T)) (T + 4k).        (W)

Scalar optimum: effective diagonal A = 3a = 4, so the coefficient is sqrt(A b) = sqrt(8/3) = 1.63299
at T = sqrt6 N^{3/4}. Kayll's sqrt3 is the same accounting with ab = 1. Within this accounting the 1D
barrier ab >= 8/9 makes sqrt(8/3) optimal; better needs a bound |P| <= theta k (coefficient
sqrt((1 + 2theta)·8/9)).
Explicit version [scan only]: with T = sqrt6 x^3, x = N^{1/4}, the test point y = x^2 + sqrt(8/3) x + 2
satisfies the scalar contradiction for all scanned x in [90, 1e6]; P_0(y) = (4/3)x^2 − (2/3)sqrt(8/3)x − 4/3
(exact expansion, analogous to (6.5)). Expected statement: W(N) <= sqrt N + sqrt(8/3) N^{1/4} + 2 for
N >= ~90^4, to be proved as in §6.

### 3.3 g-thin Sidon sets (item 3)

r(d) <= g for all d ≠ 0, so E <= a k + gT. With S = gT and L = N/T = gN/S:
k^2 <= (gN/S + 2/3 + eps)(S + (4/3)k) — literally (5.1) with N replaced by gN (the condition T <= N
is L >= 1). §6 then gives, for gN >= 120^4, **k <= sqrt(gN) + (2sqrt2/3)(gN)^{1/4} + 1**, and in
diameter form g·diam(A) >= k^2 − (4sqrt2/3) k^{3/2} − O(k), i.e. b^(g) <= 1.8856/g vs CHO's (2 − eps_g)/g.
Note the onset gN >= 120^4 replaces BFR's "all n >= t".

### 3.4 Difference triangle sets (item 4)

Rows X_1..X_n ⊂ [0,m], |X_i| = K = k+1, all positive differences across all rows distinct.
Σ_i E(mu_i,mu_i) <= n a K + T (each positive difference used once), and each
E(mu_i,mu_i) >= K^2/(L + b + eps), L = (m+1)/T. Hence with S = T/n:
K^2 <= ((m+1)/(nS) + 2/3 + eps)(S + (4/3)K) — the Sidon inequality with N replaced by (m+1)/n.
If (m+1)/n >= 120^4 (automatic from the trivial bound m >= n k(k+1)/2 once k >= 20365):
k <= y^2 + gamma y, y = ((m+1)/n)^{1/4}, so

    m(n,k) >= n ((sqrt(4k + 8/9) − 2sqrt2/3)/2)^4 − 1 = n (k^2 − (4sqrt2/3) k^{3/2} + O(k)).

Kløve: n(k^2 − 2k^{3/2} + (k + sqrt k)/4). Ours wins asymptotically; for small k Kløve and the LP
bounds remain the relevant ones (our onset is a proof artefact of Lemma 6's error term).

### 3.5 Manhattan distinct-difference configurations (item 5)

Pairwise Manhattan distance <= r ⇔ in u = x+y, v = x−y every coordinate range is <= r (since
|Δx| + |Δy| = max(|Δu|,|Δv|)); so no anticode classification is needed. The image lattice is
Λ = {(u,v): u ≡ v mod 2}. Product kernel f(u/T) f(v/T); off-diagonal
<= S_e^2 + S_o^2 − a^2 <= T^2/2 + 2aT + a^2, where S_e = Σ_j f(2j/T) <= T/2 + a and S_o = Σ_j f((2j+1)/T) <= T/2 + a
(monotonicity). Product test measure ⇒

    m^2 <= (r/T + 2/3 + eps(r/T))^2 ((16/9) m + T^2/2 + 2aT + a^2).        (M)

With m = r/sqrt2 + delta: delta <= a^2 r^2/(2T^2) + bT/sqrt2 + O(r^{1/3}); optimum T^3 = sqrt2 a^2 r^2/b gives
delta <= 3·2^{-4/3} (ab)^{2/3} r^{2/3}. With ab = 1 this is exactly BEMP's 3/2^{4/3}; with ab = 8/9 it is
1.10064 r^{2/3}. BEMP's leading term r/sqrt2 is attained by their construction (Table I), so the
r^{2/3} term is the frontier.

### 3.6 Sidon sets in [N]^d (item 6)

Each nonzero difference vector occurs once. Product kernel, product test measure:
k^2 <= (N/T + 2/3 + eps)^d (a^d k + (T + a)^d − a^d), since Σ_{v∈Z^d} Π f(v_i/T) <= (T + a)^d.
Second-order balance: 2c = d b t + a^d t^{-d} at T = t N^{(d+2)/(2d+2)}, minimised at
t^{d+1} = a^d/b: c_d = ((d+1)/2)(ab)^{d/(d+1)}. ab = 1 → (d+1)/2; ramp → 1.38672 (d=2), 1.83090 (d=3).
Open side question: non-product kernels could in principle lower c_d (the 1D barrier only covers
product kernels through their factors).

### 3.7 Why unions of intervals do not transfer directly (item 7)

Positive capacity is monotone in the gaps and additive once gaps exceed the kernel range, so
C(union) <= Σ_i C([0,L_i]). But for the ramp, C(L) − L is not <= 2/3 for short intervals:
discrete-grid values C(L) − L = 0.750 (L → 0, exactly 1/a), 0.711 (0.1), 0.669 (0.25), 0.646 (0.5),
0.674 (1.0), 0.6665 (>= 2). An adversary using many short intervals forces a·sup(C − L) = 1, i.e.
Riblet's sqrt k. A gain needs either a length hypothesis or a multi-scale argument.

## 4. Numerical checks actually run (numpy/scipy/mpmath, scratchpad scripts, not committed)

* 1D discrete capacity (signed solve, up to 801 grid points, weights all positive): ramp
  C(L) − L ≈ 0.6665 for L >= 2; triangle ≈ 1.000. Sanity only; discrete capacities approximate the
  continuous one from below.
* Scalar inequalities solved for the extremal size (min over a (T)-scan, mpmath 30–40 digits):
  sonar (S): (m_max − n)/n^{2/3} = 2.0264, 2.0026, 2.0003, 2.0000 at n = 1e6, 1e9, 1e12, 1e15;
  EGRT window inequality: 3.0205, 3.0020, 3.0002, 3.0000.
  Weak Sidon (W): 1.63433 (1e12), 1.63299 (1e24) → sqrt(8/3).
  g-thin g = 2, 5: 0.94281 at gN = 1e24 → 2sqrt2/3.
  [N]^2: 1.38683 (1e16) → 1.38672; [N]^3: 1.83106 (1e16) → 1.83090.
  Manhattan (M): 1.10068 at r = 1e15 → 1.10064 (BEMP 1.19055).
  DTS: (K^2 − M'_min)/K^{3/2} = 1.8767, 1.8847, 1.8855 at K = 1e4, 1e6, 1e8 → 1.88562.
* Finite consistency checks (no failures): triangle identity Λ = mT − (T^2 − 1)/3 for all m < 40;
  lattice sums Σ f_ramp(d/T) <= T + a and the index-2 lattice bound at T = 3.7, 10, 55.5, 200;
  for the quadratic sonar sequences a_i = i^2 mod p (p = 31, 61, 101; Sidon property verified by
  brute force) both sides of the energy sandwich hold at two (T1,T2) choices; greedy weak Sidon
  sets (N = 3000, 20000) satisfy r(d) <= 2, repeated differences are 3-AP differences, |P| <= k − 2
  and E <= 3ak + T. These are sanity checks, not proofs.
* Kernel functional a·m1 over h >= 0 (200-point grid, L-BFGS): minimum 0.30842 ≈ pi^2/32
  (cosine bump); uniform 1/3, Gaussian 1/pi.

Cost: no paid resources; model-token cost not measured.

## 5. Suggested next gates (not started)

1. G2 per item 1–5 (MathSciNet/Google Scholar citations of EGRT 1992, BFR 2023, CHO 2025,
   Kløve 1988, BEMP 2010), including whether someone already used exact-marginal weighting for sonar.
2. Isolated referee for (S) and its asymptotics (item 1) before any write-up.
3. Primary read of Lindström 1972 for item 6.
4. If 1–3 pass: one corollaries note (items 2–5) plus a separate sonar note; explicit onsets via the
   §6 monotonicity template.

## Sources (accessed 2026-10-02)

* EGRT 1992 scan: https://mathweb.ucsd.edu/~ronspubs/92_02_distinct_slopes.pdf (pp. 39–43 read)
* BFR: https://arxiv.org/abs/2103.15850 (v2, §5, §6 read); journal DOI 10.1080/00029890.2023.2176667
* CHO: https://arxiv.org/abs/2310.20032 (§4 read); journal abstract via Crossref DOI 10.1007/s10474-024-01499-8
* Chee–Colbourn 1997 (Kløve Thm): https://arxiv.org/abs/0712.2553
* Shearer 1999: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v6i1r31/pdf
* Shehadeh–Kingsford–Kschischang 2025: https://arxiv.org/abs/2502.19517
* Ma–Yi 2026: https://arxiv.org/abs/2608.13739
* BEMP 2010: https://arxiv.org/abs/0811.3832 (§IV, Table I read)
* Lee 2014: https://arxiv.org/abs/1405.4227 ; O'Bryant bibliography: https://arxiv.org/abs/math/0407117
* Riblet 2022: https://arxiv.org/abs/2202.01296 (Thm 3.1 read)
* Cilleruelo–Timmons k-fold: https://arxiv.org/abs/1310.5374 ; Cilleruelo–Ruzsa–Vinuesa: https://arxiv.org/abs/0909.5024
* Johnston–Tait–Timmons B_k[g]: https://arxiv.org/abs/2105.03706
* Hou–Zhao: https://arxiv.org/abs/2607.01169 (v3; closing remarks on bounded-multiplicity extensions)
* Gupta–O'Bryant: https://arxiv.org/abs/2605.14229
* Ruiz–Trujillo–Caicedo sonar: https://arxiv.org/abs/1311.1679
* Not accessible / not read: Lindström 1972 (ScienceDirect 403), Kløve 1988 original, Kayll 2005,
  Moreno–Games–Taylor 1993, Blokhuis–Tiersma 1988, Robinson 1985/1997, Cilleruelo 2010 full text.
