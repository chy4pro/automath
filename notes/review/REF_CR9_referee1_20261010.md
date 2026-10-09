PASS — CR-9 (problems/erdos30/CR9_ASTRA_ONSET_20261010.md) is correct as written: Route A proves P_ε(y) > (4/1089)x² for every real x ≥ x₁ = 4,600,000^(1/4), and Route B proves η < (667/3300)x² < x²/2 and the x ≥ 1 scalar lemma; every displayed comparison recomputes true. No repair is required; three cosmetic remarks are listed under REPAIRS (none affects validity).

Lineage: resumed — the first session of this issue (AUT-76) was cut off by a provider quota limit after reading all four listed inputs and running the first exact-arithmetic sweep; this session re-ran every check from scratch and wrote the report. Referee: referee-1 (Claude). Files read: exactly the four items listed in the task (CR-9; SIDON_BOUND_PROOF.md §§1, 5, 6; the four Lean files; VER_onset30_20261010.md). The other referee was not read or contacted. No web search.

## 1. Numbered table of every checked comparison (recomputed independently; exact integer / rational arithmetic unless marked "50-digit")

| # | Claim in CR-9 | Recomputed value | Verdict |
|---|---|---|---|
| 1 | 463⁴ = 45,954,068,161 < 46,000,000,000 = 10⁴·N₁ | 463⁴ = 45954068161; 10⁴N₁ = 46000000000 | true |
| 2 | 4631⁴ = 459,937,821,637,921 | 459937821637921 | true |
| 3 | 4632⁴ = 460,335,219,019,776 | 460335219019776 | true |
| 4 | 4631⁴ < 10⁸N₁ = 460,000,000,000,000 < 4632⁴ (so 46.31 < x₁ < 46.32) | holds; 50-digit x₁ = 46.3115650669756… | true |
| 5 | 2144² = 4,596,736 < N₁ (so x₁² > 2144) | 4596736 < 4600000; also 2145² = 4601025 > N₁ | true |
| 6 | 2(1/7 + 1/(3·7³)) = 296/1029 | 2(147+1)/1029 = 296/1029 | true |
| 7 | 296·2500 = 740000 > 739851 = 719·1029, i.e. 296/1029 > 719/2500 | 740000, 739851 | true |
| 8 | α = 296/1029 + R, 0 < R < 1/41160 | (49/24)·(1/7)⁵/5 = 1/41160 exactly; 50-digit R = 2.4152e-5 < 2.4295e-5 | true |
| 9 | 99² = 9801 > 9800 = 2·70², i.e. √2 < 99/70 | 9801, 9800 | true |
| 10 | 719·463·70·100 = 2,330,279,000 | 2330279000 | true |
| 11 | 941·2500·10·99 = 2,328,975,000 | 2328975000 | true |
| 12 | (719/2500)(463/10)(70/99) > 941/100 | = 9.41526… > 9.41; 50-digit βu = 9.41843… | true |
| 13 | Σ_{j≤9} 3ʲ/j! = 22471/1120 | 22471/1120 (exact Fraction sum) | true |
| 14 | 22471·50 − 1003·1120 = 190 > 0 (e³ > 1003/50) | 1123550 − 1123360 = 190 | true |
| 15 | degree-8 sum = 89641/4480 and 50·89641 − 1003·4480 = −11390 (discarded truncation) | 89641/4480; −11390 | true |
| 16 | Σ_{j≤3} (41/100)ʲ/j! = 9033221/6000000 > 3/2 | 9033221/6000000; 9033221 > 9000000 | true |
| 17 | 3·1003³ = 3,027,081,081 > 3,025,000,000 = 12100·2·50³; gap 2,081,081 | 3027081081; 3025000000; gap 2081081 | true |
| 18 | 200/12100 = 2/121 | 2/121 | true |
| 19 | (99/70)(463/10) = 45837/700 < 131/2 (45837 < 45850) | 45837/700; 131·350 = 45850 | true |
| 20 | (4/3)(1 + 1/46 + 1/46²) = 721/529 < 3/2 (1442 < 1587) | 721/529; 2·721 = 1442, 3·529 = 1587 | true |
| 21 | (2/121)(131/2 + 3/2) = 134/121 | 134/121 | true |
| 22 | 10/9 − 134/121 = 4/1089 (1210 − 1206 = 4) | 4/1089 | true |
| 23 | (S-A) (4/1089)·2144 = 8576/1089 | 8576/1089 | true |
| 24 | 463/10 − 32·99/70 = 73/70 > 1 | 3241/70 − 3168/70 = 73/70 | true |
| 25 | 46³ = 97336 > 33 | 97336 | true |
| 26 | 3³² = 1,853,020,188,851,841 | 1853020188851841 | true |
| 27 | 4³² = 18,446,744,073,709,551,616 | 18446744073709551616 | true |
| 28 | 9900·3³² = 18,344,899,869,633,225,900 < 4³²; gap 101,844,204,076,325,716 | 18344899869633225900; gap 101844204076325716 | true |
| 29 | 4(2r+5) − 3(2r+7) = 2r − 1 (= 63 at r = 32) | 2r − 1; 63 | true |
| 30 | 29·69 = 2001; 2001/9900 = 667/3300 < 1/2 (1334 < 3300); 1/2 − 667/3300 = 983/3300 | all exact | true |
| 31 | 29·69·(3/4)³² < 2001/9900 | 0.201005… < 0.202121… | true |
| 32 | 140469⁴ = 389,333,669,232,539,881,521 | 389333669232539881521 | true |
| 33 | 140470⁴ = 389,344,756,029,676,810,000 | 389344756029676810000 | true |
| 34 | 4N₁³ = 389,344,000,000,000,000,000 and 140469⁴ < 4N₁³ < 140470⁴, so T(N₁) = ⌈√2·x₁³⌉ = 140470 | 4N₁³ = 389344000000000000000; T = smallest integer with T⁴ ≥ 4N₁³ = 140470 | true |
| 35 | 32T = 4,495,040 ≤ 4,599,999 < 4,635,510 = 33T, so r(N₁) = 32 | 4495040; 4635510; (N₁−1)//140470 = 32 | true |
| 36 | η₁ = 29·140470·(3/4)³² = 3774259315956262526415 / 9223372036854775808 | identical reduced fraction (denominator 2⁶³); ≈ 409.206 | true |
| 37 | 1072 − η₁ = 6113195507552057139761 / 9223372036854775808 > 0 | identical; ≈ 662.794 | true |
| 38 | (11·2144 + 10)/18 = 11797/9 | 23594/18 = 11797/9 | true |
| 39 | (B4.3) 8/(9·46²) = 2/4761 < 1/2 | 2/4761 | true |
| 40 | 9200/6561 > 1/32 (294400 > 6561), diagnosing the old envelope | 294400 > 6561 | true |
| 41 | x − 32s > 1 and x³ > 33 give x³(x − 32s) > 33 and N − 1 > 32(sx³+1) ≥ 32T | exact; checked exact for every integer N ∈ [N₁, 2·10⁷]: min r = 32 | true |

Every displayed number in CR-9 is correct. No arithmetic error was found.

## 2. Findings per item

### (a) Arithmetic
All 41 comparisons above recompute true (Python `fractions`, exact integers; 50-digit mpmath only for the transcendental sanity values). The exponential Taylor sums, the two large fourth-power brackets, the 2⁶³-denominator fractions in (S-B-onset), and the 3³²/4³² certificate are all exactly as displayed.

### (b) Route A: direction and domain
- α = log(4/3) = log((1+t)/(1−t)) at t = 1/7 = 2∫₀^{1/7} dt/(1−t²): correct (8/7 ÷ 6/7 = 4/3). 1/(1−t²) = 1 + t² + t⁴/(1−t²) > 1 + t² on (0, 1/7]: correct, so α > 2(1/7 + 1/(3·343)) = 296/1029 > 719/2500. Direction correct (lower bound on α is what is needed because ε = 200e^{−αx/√2} must be bounded above).
- βu: β = α/√2 > (719/2500)·(70/99) uses a lower bound on α and an upper bound on √2; both in the right direction. βu > 941/100 > 1: true (table rows 10–12).
- e^{βu} > e^{9.41} = (e³)³·e^{0.41} > (1003/50)³·(3/2) = 3·1003³/(2·50³) > 12100: all three steps use lower bounds of positive quantities, hence valid; therefore 200e^{−βu} < 200/12100 = 2/121. True (50-digit: e^{βu} = 12313.3, 200e^{−βu} = 0.016243 < 0.016529).
- F(x) identity: ε(4y/3 + sx³)/x² with y = x² + γx + 1 expands to 200e^{−βx}(sx + 4/3 + 4γ/(3x) + 4/(3x²)): verified symbolically (sympy, difference 0).
- Monotonicity: F is a sum of positive constants times xe^{−βx}, e^{−βx}, x⁻¹e^{−βx}, x⁻²e^{−βx}. The derivative of xe^{−βx} is e^{−βx}(1 − βx), which is < 0 for x ≥ u because βx ≥ βu > 1 (row 12; βu > 1 is exactly what is needed, and (6.3) gives it). The other three derivatives are −e^{−βx}(jx^{−j−1} + βx^{−j}) < 0 for x > 0. Hence F is strictly decreasing on [u, ∞) and F(x) < F(u) for x ≥ x₁ > u. 50-digit check: F′(u) = −0.1979, F′(x₁) = −0.1975.
- Endpoint: su < 45837/700 < 131/2 and (4/3)(1 + γ/u + 1/u²) < (4/3)(1 + 1/46 + 1/46²) = 721/529 < 3/2 (uses 0 < γ < 1 and u > 46, both proved); with 200e^{−βu} < 2/121 this gives F(u) < (2/121)·67 = 134/121. 50-digit: F(u) = 1.08564 < 1.10744. True.
- (6.2): expanding Lemma 7 with N = x⁴, T = √2x³, N/T = x/√2 gives k² − (γx + 8/9 + 4ε/3)k − x⁴ − γx³ − √2εx³ ≤ 0: verified symbolically (difference 0). Admissibility of Lemma 7: T = √2x³ is a positive real with T ≤ N ⇔ √2 ≤ x, and L = N/T = x/√2 ≥ 1 for the same reason; x ≥ x₁ > 46 > √2. Lemma 7 allows any real 0 < T ≤ N, so a non-integer T is admissible. N is an integer ≥ 1 and A − 1 ⊆ {0, …, N−1}. Correct.
- (6.5): P₀(y) = (10/9)x² + (γ/9)x + 1/9 using γ² = 8/9: verified symbolically (sympy gives 10x²/9 + 2√2x/27 + 1/9, and 2√2/27 = γ/9). P₀(y) ≥ (10/9)x² because the two dropped terms are positive. Correct.
- (6.7): P_ε(y) = P₀(y) − ε(4y/3 + √2x³) = P₀(y) − F(x)x² > (10/9 − 134/121)x² = (4/1089)x² > 0. Strict because F(x) < 134/121. Correct. 50-digit: P_ε(y)/x² = 0.030070 at x₁ (verifier reported 0.0301) and the grid minimum over x ∈ [x₁, x₁ + 400] is attained at x₁; the continuous zero of P_ε(y) is at x* = 46.16130, N* = 4,540,588.75 (verifier: 4,540,589). The proof's certified margin 4/1089 = 0.00367 is well inside the true margin 0.0301.
- Root argument: leading coefficient 1, constant term −(x⁴ + γx³ + √2εx³) < 0, so the root product is negative and exactly one root is positive. P_ε(k) ≤ 0 with k ≥ 0 forces k to lie between the roots, so k ≤ positive root. P_ε(y) > 0 with y > 0 forces y to lie above the positive root (y cannot be below the negative root). Hence k ≤ root < y. For k = 0 the conclusion 0 < y is trivial and the argument also covers it. Correct.

### (c) Route B
- Definitions match the Lean files exactly: sidonIntegerScale x = ⌈√2·x³⌉ (IntegerScaleAndTail.lean), r = (N − 1)/T natural division, η = 29T(3/4)^r (FinalReduction.lean), rampDiagonal T = 2(2T+1)/(3T(T+1)) (RampWeights.lean), γ = 2√2/3. The report states √2x³ ≤ T ≤ √2x³ + 1; the Lean lemma sidonIntegerScale_lt gives the strict upper bound, so the report's non-strict version is weaker and valid.
- r ≥ 32: x − 32√2 > 463/10 − 32·99/70 = 73/70 > 1 and x³ > 46³ = 97336 > 33, so x³(x − 32√2) > 33 (product of two positive quantities each exceeding the stated bound), i.e. x⁴ − 1 > 32√2x³ + 32 = 32(√2x³ + 1) ≥ 32T. Hence (N − 1)/T > 32 as reals and the natural quotient is ≥ 32. Correct. Exact integer check: r ≥ 32 for every integer N ∈ [4,600,000, 20,000,000]; the smallest N from which r ≥ 32 holds without interruption is 4,194,401, so the onset has room.
- (B3.1): (x⁴ − 1)/(√2x³ + 1) − (x/√2 − 1) = (2x³ − x)/(√2(√2x³ + 1)) verified symbolically; positive for x > 1/√2. Chain: r = ⌊(N−1)/T⌋ > (N−1)/T − 1 ≥ (x⁴−1)/(√2x³+1) − 1 > x/√2 − 2. The middle step divides the positive number x⁴ − 1 by T ≤ √2x³ + 1, correct direction. Hence x < √2(r + 2). Correct. (Note: at x = 46.3 this bound alone gives only r > 30.74, i.e. r ≥ 31; the report correctly does not use it for r ≥ 32 but only for the upper bound on x in terms of r.)
- (B3.2): η/x² = 29(T/x²)q^r ≤ 29(√2x + 1/x²)q^r (T ≤ √2x³ + 1, q^r > 0) and √2x < 2(r + 2), 1/x² < 1 give < 29(2r + 5)q^r. Correct.
- Decreasing sequence: ratio of consecutive terms is 3(2r + 7)/(4(2r + 5)) < 1 iff 2r − 1 > 0, so (2r + 5)q^r is strictly decreasing for every r ≥ 1, in particular from r = 32 on; hence (2r + 5)q^r ≤ 69q³² for r ≥ 32. Correct (the sequence is rational-valued, not integer-valued; wording only).
- (B3.3): 9900·3³² < 4³² exact (row 28). (B3.4): η/x² < 29·69·q³² < 2001/9900 = 667/3300 < 1/2. Correct. Exact integer sweep of the actual Lean quantity (criterion (58T·3^r)² < N·4^{2r}) for every integer N ∈ [4,600,000, 20,000,000]: no violation; worst η/(x²/2) = 0.38454 at N = 4,743,773 (verifier: 0.3845), i.e. worst η/x² = 0.1923 < 667/3300 = 0.2021, consistent with the uniform bound. Scanning downward, the largest N < N₁ violating η < x²/2 is 2,829,211 (verifier onset 2,829,212), consistent.
- (B4.1): y² − (x⁴ + γx³)(1 + (γ/x³)(y − 1)) = (10/9)x² + (10/9)γx + 1 using γ² = 8/9: verified symbolically; identical to secondOrder_margin_identity in SecondOrderFinal.lean. The factor 1 + (γ/x³)(y − 1) = 1 + γ/x + γ²/x² > 0 for x > 0: verified.
- (B4.2): Q(y) = (B4.1) − η·(positive factor) > (B4.1) − (x²/2)(1 + γ/x + γ²/x²) = (11/18)x² + (11/18)γx + 5/9 > 0: verified symbolically (sympy: 11x²/18 + 11√2x/27 + 5/9, and 11√2/27 = (11/18)γ). The strict inequality uses η < x²/2 and factor > 0; it is strict even when η = 0. Needs only x > 0. Correct; (B4.3) is correctly labelled as optional.
- Constant term of Q: Q(0) = −C(1 − γ/x³) with C > 0 and γ/x³ ≤ γ < 1 for x ≥ 1. Correct, and x ≥ 1 is exactly where this is needed. Root argument as in Route A; conclusion k < y. The scalar lemma therefore holds for every real x ≥ 1 as claimed (the identity needs x ≠ 0; C > 0 needs x > 0, η ≥ 0). Its hypotheses match quadratic_certificate_comparison in SecondOrderFinal.lean (0 < C, b < 1, 0 < y, C(1 + b(y−1)) < y², k² ≤ C(1 + b(k−1))).
- (B1): N + (2/3)(T − 1) ≤ x⁴ + γx³ follows from T − 1 ≤ √2x³ (sidonIntegerScale_sub_one_le, hypothesis 0 ≤ x) and (2/3)√2 = γ. Onset-free: confirmed against sidonIntegerScale_boundary_le (hypotheses 0 ≤ x, x⁴ = N only).
- (B2): a_T = 2(2T+1)/(3T(T+1)) ≤ 4/(3T) ⇔ 2T + 1 ≤ 2T + 2 (rampDiagonal_le, 1 ≤ T), and 4/(3T) ≤ γ/x³ ⇔ 4x³ ≤ 2√2T ⇔ √2x³ ≤ T (true by the ceiling). Onset-free: confirmed against sidonIntegerScale_diagonal_le (hypothesis 0 < x only).
- Combination: for k ≥ 1 both factors of the certificate are positive (first factor ≥ N ≥ 1; second is 1 + a_T(k − 1) with a_T ≥ 0), so the two one-sided bounds multiply (this is exactly mul_le_mul in FinalReduction.lean); k = 0 is immediate. Correct.

### (d) Statement hygiene
- Quantifiers: "for every integer N ≥ 4,600,000 and every Sidon set A ⊆ {1, …, N}" and "for every real x ≥ x₁" are stated explicitly; Route A's analytic estimates are proved for all real x ≥ x₁ (no integrality of x⁴ used), and the discrete input Lemma 7 is applied for the integer N. Correct.
- Translation {1..N} → {0..N−1}: A − 1 is Sidon (Lemma 1 of the published proof, "translation preserves these conditions"); Lemma 7 is stated for {0..N−1}. Correct.
- Strict vs non-strict: the proof gives k < √N + γN^{1/4} + 1 (strict), which implies the published non-strict (1.1). Correctly stated.
- Floating point: none in the proof; the report explicitly confines float use to constant-finding. Every bound is an integer or rational comparison, a positive-term series truncation, or a sign of a derivative. No step says "approximately". The two "≈" magnitudes in my own report above are for cross-checking only.
- One stated fact is slightly loose but harmless: "T ≤ √2x³ + 1" (Lean gives <). The sentence "the integer sequence (2r+5)q^r" should read "sequence".

### (e) Sufficiency for the formaliser
Route B as written is sufficient to replace 120 ≤ x and r ≥ 58 in the Lean files, with the following concrete mapping (all facts proved in CR-9 or already in the files):
- FinalReduction.lean, hx: replace 120 ≤ x by 463/10 ≤ x, derived from (463/10)⁴ ≤ N via 463⁴ = 45,954,068,161 ≤ 46,000,000,000 (row 1), through the same two Real.le_sqrt_of_sq_le steps. (The onset constant in the statement file, which I did not read, must be changed to 4,600,000 by the formaliser.)
- IntegerScaleAndTail.lean, sidonIntegerScale_quotient_ge: replace 58 by 32, proved by CR-9's direct argument N − 1 > 32T (needs √2 ≤ 99/70, which the file already proves via 17/12 and can prove via 9801 > 9800). The existing route through x ≤ 2(r + 2) gives only r ≥ 22 at x ≥ 46.3 and is insufficient; the direct argument must be used.
- The existing envelope chain can be kept unchanged: sidonTailEnvelope 32 = 68·(3/4)³² = 0.00683… < 1/100 (exact rational, norm_num-checkable), sidonIntegerScale_upper (T ≤ (3/2)x³) needs only x³ ≥ 12, and sidonIntegerScale_tail_lt (< (87/200)x²) then goes through with 120 → 463/10 and 58 → 32. Alternatively the formaliser can transcribe (B3.2)–(B3.4) directly with the sharper constant 667/3300.
- SecondOrderFinal.lean, secondOrder_of_scaled_certificate: replace hx : 120 ≤ x by 1 ≤ x and replace the hfrac1/hfrac2 route by the exact subtraction (B4.2), i.e. hgap from hmargin, hη, the positivity of 1 + γ/x + γ²/x², and (11/18)x² + (11/18)γx + 5/9 > 0; nothing else in the lemma uses 120. If the formaliser prefers to keep hfrac1/hfrac2, (B4.3) supplies the replacement hint with x ≥ 463/10.
- (B1), (B2) need no change (hypotheses 0 ≤ x and 0 < x).

## 3. REPAIRS
None required for validity. Cosmetic, optional:
1. §(ii), paragraph after (B3.2): "the integer sequence (2r+5)q^r" → "the sequence (2r+5)q^r" (its terms are rational). Conclusion unaffected.
2. §(ii), first display: "T ≤ sx³ + 1" could be stated strictly (T < sx³ + 1) to match sidonIntegerScale_lt; the non-strict form used is weaker and every subsequent step remains valid. Conclusion unaffected.
3. §(ii), (B3.1) remark for the formaliser (not an error in CR-9): the floor bound r > x/√2 − 2 yields only r ≥ 31 at x = 463/10; r ≥ 32 must come, as CR-9 does, from N − 1 > 32T. Conclusion unaffected (and even r ≥ 31 would give 29·67·(3/4)³¹ = 0.2602 < 1/2).

## 4. Numerical tests actually run
- Exact (Python fractions/integers): the 41 comparisons in the table; the reduced fractions η₁ and 1072 − η₁ (denominator 2⁶³); T(N₁) = 140470 via the smallest T with T⁴ ≥ 4N₁³; r(N₁) = 32.
- Exact integer sweep of the Lean tail criterion η < x²/2 ⇔ (58T·3^r)² < N·4^{2r} for every integer N ∈ [4,600,000, 20,000,000]: 0 violations, min r = 32, worst η/(x²/2) = 0.38454 at N = 4,743,773; downward scan: last violating N below N₁ is 2,829,211.
- Symbolic (sympy): (6.2), (6.5), the F(x) identity, the (B3.1) numerator 2x³ − x, (B4.1), the factor 1 + γ/x + γ²/x², (B4.2), and 4(2r+5) − 3(2r+7) = 2r − 1.
- 50-digit (mpmath): α, R, βu = 9.41844, e^{βu} = 12313.3, 200e^{−βu} = 0.016243, F(u) = 1.08564, F(x₁) = 1.08336, F′(u), F′(x₁) < 0, P_ε(y)/x² at x₁ = 0.030070, grid minimum of P_ε(y)/x² on [x₁, x₁ + 400] attained at x₁, continuous zero at N* = 4,540,588.75.
- Exact: sidonTailEnvelope 32 = 68·(3/4)³² < 1/100.

## 5. What I could not check
- Lemma 7 (5.1) and the finite certificate DiscreteSidonCertificateBound are taken as supplied inputs, per the task; I did not re-referee them.
- I did not read the Lean statement file (Statement.lean) or ShiftWindow.lean, so the exact spelling of the onset constant in SidonSecondOrderBound and the shiftWindow lemmas were not verified; CR-9 does not depend on them.
- CR-9's own Node.js checker was not run (the report does not include it); all checks above are my own.

## 6. Verdict
PASS. Every displayed integer and rational comparison in CR-9 is true, every inequality is used in the correct direction on a domain where its hypotheses are available (x ≥ x₁ > u = 463/10 > 46 for Route A; x ≥ 463/10 for (B3) and x ≥ 1 for the scalar lemma), the two polynomial identities (6.5) and (B4.1) and the floor-comparison numerator are exact, and the root arguments are complete including k = 0. Route A establishes P_ε(y) > (4/1089)x² for every real x ≥ 4,600,000^{1/4}, and with Lemma 7 this gives |A| < √N + (2√2/3)N^{1/4} + 1 for every integer N ≥ 4,600,000 and every Sidon set A ⊆ {1, …, N}. Route B establishes r ≥ 32 and η < (667/3300)x² < x²/2 for every such integer N with the exact Lean definitions of T, r, η, and the scalar lemma for every real x ≥ 1; the exact integer sweep over N ∈ [4.6·10⁶, 2·10⁷] and the verifier's magnitudes agree with the proved bounds. No repair is needed; Route B as written is sufficient for the formaliser to replace 120 ≤ x by 463/10 ≤ x (and 1 ≤ x in the scalar lemma) and r ≥ 58 by r ≥ 32, using the direct N − 1 > 32T argument for the quotient bound.
