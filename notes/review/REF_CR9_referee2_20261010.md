PASS — No mathematical error found in Route A or Route B. Every displayed comparison was recomputed exactly and is true. Three optional editorial or formalisation notes follow; none is needed for correctness.

Lineage: this is a resumed session of this issue. The first run of the session read the five files in scope and re-derived the proof on paper. A provider quota limit then interrupted it, before any computation or report. This run did all the computations below and wrote this report. I did not read the other referee or any file outside the brief.

# REF CR-9 (referee-2) — onset 4,600,000, Routes A and B

**Object of review:** `problems/erdos30/CR9_ASTRA_ONSET_20261010.md` (440 lines, md5 `c70dbe20…`). Line numbers below refer to this file.

**Context read:**
- `problems/erdos30/SIDON_BOUND_PROOF.md`, sections 1, 5 and 6. Lemma 7 (5.1) is taken as proved, as the brief instructs.
- In `lean/sidon30/Sidon30/`: `FinalReduction.lean`, `IntegerScaleAndTail.lean`, `SecondOrderFinal.lean` and `RampWeights.lean`.
- `notes/review/VER_onset30_20261010.md`, used only to cross-check magnitudes.

**Claim reviewed:** For every integer N ≥ N₁ = 4,600,000 and every Sidon set A ⊆ {1,…,N},

  |A| < √N + (2√2/3)N^{1/4} + 1.

There are two routes:
- **Route A** replaces section 6 of the published proof. It shows P_ε(y) > (4/1089)x² for every real x ≥ x₁ = N₁^{1/4}.
- **Route B** gives the estimates the Lean reduction needs:
  - (B3-new): 0 < η < (667/3300)x² < x²/2;
  - (B4): a scalar lemma valid for x ≥ 1.

## 1. Numbered table of checked comparisons (all recomputed independently)

Method: Python integers and `fractions.Fraction`, which is exact. The script asserted 55 items; all hold. The symbolic identities in rows 41–48 were checked with sympy over ℚ(√2)(x, ε, η, z).

| # | CR-9 line | Claim | Recomputed value | OK |
|---|---|---|---|---|
| 1 | 9–19, 26 | 463⁴ = 45,954,068,161 < 46,000,000,000 = 10⁴N₁, so u = 463/10 < x₁ | 463⁴ = 45954068161 | ✓ |
| 2 | 9–13 | 4631⁴ = 459,937,821,637,921 < 4.6·10¹⁴ < 460,335,219,019,776 = 4632⁴ | both fourth powers exact as displayed | ✓ |
| 3 | table | 4632 < 4700, so x₁ < 47 | — | ✓ |
| 4 | table, S-A | 2144² = 4,596,736 < N₁, so x₁² > 2144 | 4596736; also 2145² = 4601025 > N₁ | ✓ |
| 5 | 61, table | √2 < 99/70: 99² = 9801 > 9800 = 2·70²; also 99 < 140 | — | ✓ |
| 6 | 54–58 | 2(1/7 + 1/(3·7³)) = 296/1029 | 296/1029 | ✓ |
| 7 | 60 | 296/1029 > 719/2500: 740000 > 739851 | 296·2500 = 740000; 719·1029 = 739851 | ✓ |
| 8 | table | R < (49/24)∫₀^{1/7} t⁴ dt = 1/41160 (not used in the proof) | exactly 1/41160; true α − 296/1029 = 2.415e-5 < 2.430e-5 | ✓ |
| 9 | 63–68 | (719/2500)(463/10)(70/99) > 941/100: 2,330,279,000 > 2,328,975,000 | ratio = 9.4152687 | ✓ |
| 10 | 72–77 | Σ_{j=0}^{9} 3ʲ/j! = 22471/1120 | 22471/1120 | ✓ |
| 11 | 80, table | 22471/1120 > 1003/50: 1,123,550 > 1,123,360, gap 190 | gap 22471·50 − 1003·1120 = 190 | ✓ |
| 12 | 432 | degree-8 sum = 89641/4480, gap −11390 (a discarded approach) | 89641/4480; −11390 | ✓ |
| 13 | 76–79 | Σ_{j=0}^{3} (41/100)ʲ/j! = 9033221/6000000 > 3/2 | 9033221/6000000 = 1.5055368… | ✓ |
| 14 | 85–91 | 941/100 = 3·3 + 41/100, so e^{941/100} = (e³)³e^{41/100} | — | ✓ |
| 15 | 93–94 | 3·1003³ = 3,027,081,081 > 3,025,000,000 = 12100·2·50³; difference 2,081,081 | exact | ✓ |
| 16 | 89–90 | 200/12100 = 2/121 | — | ✓ |
| 17 | 117–121 | s·u < (99/70)(463/10) = 45837/700 < 131/2, since 45837 < 45850 | exact | ✓ |
| 18 | 121–124 | (4/3)(1 + 1/46 + 1/46²) = 721/529 < 3/2, since 1442 < 1587 | exact | ✓ |
| 19 | 131–133 | (2/121)(131/2 + 3/2) = 134/121 | exact | ✓ |
| 20 | 145–148 | 10/9 − 134/121 = 4/1089, since 1210 − 1206 = 4 | exact | ✓ |
| 21 | S-A | (4/1089)·2144 = 8576/1089 | exact | ✓ |
| 22 | 186–188 | 463/10 − 32·99/70 = 73/70 > 1 | exact | ✓ |
| 23 | 188 | 46³ = 97336 > 33 | exact | ✓ |
| 24 | 240 | 3³² = 1,853,020,188,851,841 | exact | ✓ |
| 25 | 240 | 4³² = 18,446,744,073,709,551,616 | exact | ✓ |
| 26 | 243 | 9900·3³² = 18,344,899,869,633,225,900 < 4³² | exact | ✓ |
| 27 | 355 | gap 4³² − 9900·3³² = 101,844,204,076,325,716 | exact | ✓ |
| 28 | 249–256 | 29·69 = 2001, 2001/9900 = 667/3300 < 1/2, since 1334 < 3300 | exact | ✓ |
| 29 | 257, S-B-global | 1/2 − 667/3300 = 983/3300 | exact | ✓ |
| 30 | 233 | 4(2r+5) − 3(2r+7) = 2r − 1 = 63 at r = 32 | exact | ✓ |
| 31 | 306–313 | 8/(9·46²) = 2/4761 < 1/2 | exact | ✓ |
| 32 | 389–393 | 140469⁴ = 389,333,669,232,539,881,521 | exact | ✓ |
| 33 | 389–393 | 4N₁³ = 389,344,000,000,000,000,000 | exact | ✓ |
| 34 | 389–393 | 140470⁴ = 389,344,756,029,676,810,000, and 140469⁴ < 4N₁³ < 140470⁴ | exact | ✓ |
| 35 | 395–399 | T(N₁) = 140470; independently, the least T with T⁴ ≥ 4N₁³ is 140470 | exact | ✓ |
| 36 | 397–399 | 32T = 4,495,040 ≤ 4,599,999 < 4,635,510 = 33T, so r = (N₁−1) div T = 32 | exact | ✓ |
| 37 | 401–404 | η₁ = 29·140470·(3/4)³² = 3774259315956262526415 / 9223372036854775808 | equal as reduced fractions; the denominator is 2⁶³ | ✓ |
| 38 | 406–411 | 1072 − η₁ = 6113195507552057139761 / 2⁶³ > 0 | exact; η₁ ≈ 409.206 | ✓ |
| 39 | 415–421 | (11·2144 + 10)/18 = 11797/9 | exact | ✓ |
| 40 | 434 | e < 3 and 9200·32 = 294400 > 6561 = 3⁸ (a discarded approach) | exact | ✓ |
| 41 | 49–50 | Lemma 7 expansion gives (6.2), and 4/(3s) = γ | sympy difference 0 | ✓ |
| 42 | 96–101 | (6.5): P₀(y) = (10/9)x² + (γ/9)x + 1/9 | sympy difference 0 | ✓ |
| 43 | 140–146 | P_ε(y) = P₀(y) − ε((4/3)y + sx³) | sympy difference 0 | ✓ |
| 44 | 105–110 | F(x) = 200e^{−βx}(sx + 4/3 + 4γ/(3x) + 4/(3x²)) | sympy difference 0 | ✓ |
| 45 | 199–203 | (x⁴−1)/(sx³+1) − (x/s − 1) = (2x³ − x)/(s(sx³+1)) | sympy difference 0 | ✓ |
| 46 | 278–284 | (B4.1) identity, giving (10/9)x² + (10/9)γx + 1 | sympy difference 0 | ✓ |
| 47 | 288–302 | factor 1 + (γ/x³)(y−1) = 1 + γ/x + γ²/x², and the (B4.2) subtraction gives (11/18)x² + (11/18)γx + 5/9 | sympy difference 0 | ✓ |
| 48 | 316 | constant term of Q equals −C(1 − γ/x³) | sympy difference 0 | ✓ |

No displayed comparison is false.

## 2. Findings

### (a) Displayed arithmetic

All 48 rows above hold exactly. CR-9 also displays two other bound chains, and I recomputed both as wholes:
- **(6.3):** βu > 941/100 > 1. The true value is βu = 9.4184360 (mpmath, 60 digits).
- **(6.4):** e^{βu} > 12100. The true value is e^{βu} = 12313.31.

CR-9 also says the brief contains a "typo". I could not check this, because the brief is not in scope. It plays no part in the proof.

### (b) Route A: direction and domain of each inequality, re-derived on paper before reading the justification

1. **α > 719/2500.**
   - Substitute v = (1+t)/(1−t). Then dv/v = 2 dt/(1−t²), and v = 4/3 gives t = 1/7.
   - (1−t²)(1+t²) = 1 − t⁴ < 1 for 0 < t, so 1/(1−t²) > 1 + t² strictly on (0, 1/7]. The integral inequality is therefore strict.
   - Rows 6–7 complete the bound.
2. **βu > 941/100.** All three factors are positive lower bounds: α > 719/2500, u = 463/10, and 1/s > 70/99. Multiplying them preserves the direction.
3. **e^{βu} > 12100 and 200e^{−βu} < 2/121.**
   - exp is increasing, and the Taylor partial sums are lower bounds because every term is positive.
   - e^{9.41} = (e³)³·e^{0.41}.
   - Rows 10–16 complete the bound.
4. **Formula for F.** The formula is an identity (row 44).
5. **F is strictly decreasing on [u, ∞).**
   - Each of the four summands is a positive constant (200s, 800/3, 800γ/3, 800/3) times x·e^{−βx}, e^{−βx}, x^{−1}e^{−βx} or x^{−2}e^{−βx}.
   - (x·e^{−βx})′ = e^{−βx}(1 − βx), which is < 0 when βx > 1. For x ≥ u, βx ≥ βu > 9.41 > 1. So βu > 1 suffices, and it is what the proof uses.
   - (x^{−j}e^{−βx})′ = −e^{−βx}(j·x^{−j−1} + β·x^{−j}) < 0 for x > 0.
   - Numerical check: F is strictly decreasing on a sorted grid of 20,481 points in [46.3, 10¹²]. The largest sampled F′ is negative. (A first unsorted grid gave a spurious "not decreasing" flag; the cause was grid ordering, not F.)
6. **Endpoint bound F(u) < 134/121.**
   - Uses γ < 1 and u > 46, in the right direction (rows 17–19).
   - True values: F(u) = 1.0856414 and F(x₁) = 1.0833553, against 134/121 = 1.1074380.
7. **(6.5) and P₀(y) ≥ (10/9)x².** Correct, because the terms (γ/9)x and 1/9 are positive.
8. **(6.7).** P_ε(y) = P₀(y) − x²F(x) > (10/9 − 134/121)x² = (4/1089)x².
   - The proof uses only F(x) ≤ F(u). It does not assume that M(x) = P_ε(y)/x² is monotone, which matters because the verifier found M is not monotone.
   - True values (mpmath, 60 digits): M(x₁) = 0.0300696318 and M(u) = 0.0277840734, both above 4/1089 = 0.0036731.
   - On the 20,481-point grid in x ∈ [46.3, 10¹²], M > 4/1089 and F < 134/121 at every point. The grid minimum of M is at x = u.
9. **Root argument.**
   - P_ε(z) = z² − bz − c with b, c > 0. The root product is −c < 0 and the discriminant is b² + 4c > 0, so there is exactly one positive root ρ.
   - For z ≥ 0, P_ε(z) ≤ 0 if and only if z ≤ ρ. So k ≤ ρ. This covers k = 0 directly.
   - y > 0 and P_ε(y) > 0 give y > ρ. Hence k < y.
   - Numerical check: y − ρ = 0.01488 at N = 4,600,000, and 0.5555 at N = 10²⁰. The sign change of y − ρ lies between 4,540,588 and 4,540,589, which matches the verifier.
10. **Admissibility for Lemma 7.**
    - T = √2x³ ≤ x⁴ = N if and only if x ≥ √2. Here x ≥ x₁ > 46.
    - L = N/T = x/s > 1 and 0 < T < N.
    - Lemma 7 needs an integer N ≥ 1, A ⊆ {0,…,N−1} and a real T with 0 < T ≤ N. All three hold.
11. **Range actually covered.** The Route A argument uses x ≥ x₁ only through x ≥ u. So it proves P_ε(y) > (4/1089)x² for every real x ≥ u = 46.3, which is slightly more than claimed.

### (c) Route B

1. **r ≥ 32.**
   - x − 32s > 463/10 − 32·99/70 = 73/70 > 1, and x³ > 97336 > 33. So x³(x − 32s) > 33.
   - Then x⁴ − 1 > 32sx³ + 32 ≥ 32T, which needs T ≤ sx³ + 1. So N − 1 > 32T and r = (N−1) div T ≥ 32.
   - The step needs only x ≥ 463/10. Non-strict is enough, because s < 99/70 is strict.
   - Exhaustive exact check: r ≥ 32 holds for every integer N in [4,595,407, 2·10⁸], where 4,595,407 = ⌈u⁴⌉.
2. **(B3.1) is correct.**
   - The identity (row 45) gives a numerator x(2x² − 1) > 0 for x > 1/√2.
   - The ceiling is handled correctly: T ≤ sx³ + 1 and x⁴ − 1 > 0 give (N−1)/T ≥ (x⁴−1)/(sx³+1).
   - The floor is handled correctly: natural division equals ⌊(N−1)/T⌋ > (N−1)/T − 1.
   - No monotonicity of r(N) is used.
   - Exact integer check: x < s(r+2) if and only if N < 4(r+2)⁴. This holds for every N in [4,595,407, 2·10⁸].
3. **(B3.2).**
   - T/x² ≤ sx + 1/x².
   - sx < s²(r+2) = 2r + 4 and 1/x² < 1, so η/x² < 29(2r+5)qʳ.
   - Exact check of the intermediate step T² < (2r+5)²N: no failure on any sample.
4. **The sequence (2r+5)qʳ is decreasing.**
   - The ratio is 3(2r+7)/(4(2r+5)) < 1 if and only if 2r > 1.
   - So (2r+5)qʳ ≤ 69q³² for r ≥ 32.
   - CR-9 calls this an "integer sequence" (line 233). It is a sequence indexed by integers, with rational values. This is a wording issue only (note E1).
5. **(B3.3)–(B3.4).** These follow from rows 24–28.
6. **Direct exact test of η < (667/3300)x².** The test is the integer inequality (29·3300·T·3ʳ)² < 667²·16ʳ·N.
   - It holds for every integer N in [4,595,407, 2·10⁸]. That is 195,404,595 values, with T computed exactly as the least integer with T⁴ ≥ 4N³.
   - The worst ratio in [4.6·10⁶, 1.2·10⁷] is η/x² = 0.19226815, at N = 4,743,773 (T = 143,751, r = 32). This equals the verifier's η/(x²/2) = 0.3845363 exactly, and is below 667/3300 = 0.2021212.
   - The test also holds, exactly, for 3,000 random N in [2·10⁸, 10¹⁶] and for 18,000 N in windows of ±1000 around r-jumps at scales 10^{8.5} to 10¹⁶.
   - For 3,000 random N in [10¹⁶, 10⁸⁰], I compared logarithms in mpmath (80 digits). These are numerics, not exact checks. No failure anywhere.
7. **(B4.1)–(B4.2).**
   - The identity holds (row 46).
   - The factor 1 + γ/x + γ²/x² is > 0. Together with η < x²/2, this gives η·factor < (x²/2)·factor strictly, so the exact subtraction is valid (row 47). The result (11/18)x² + (11/18)γx + 5/9 is > 0 for every x > 0.
8. **Constant term of Q.**
   - It equals −C(1 − γ/x³) (row 48).
   - C = x⁴ + γx³ + η > 0 because η ≥ 0.
   - x ≥ 1 gives γ/x³ ≤ γ < 1, so the constant term is negative.
   - Hence there is exactly one positive root, y lies above it, and k < y. The range x ≥ 1 is justified.
   - Numerical check: 20,000 random cases with x ∈ [1, 10⁶] and η ∈ [0, x²/2), a quarter of them at η = x²/2·(1 − 10⁻³⁰), gave no failure. The minimum of y − ρ is 0.3056. At η = x²/2, Q(y) equals (11/18)x² + (11/18)γx + 5/9 to all printed digits at x = 1, 46.3 and 120, as the identity predicts.
9. **(B1) and (B2) are onset-free, confirmed from the Lean source.**
   - `sidonIntegerScale_boundary_le` needs only `0 ≤ x` and `x^4 = N`.
   - `sidonIntegerScale_diagonal_le` needs only `0 < x`.
   - Both lemmas are stated exactly as (B1) and (B2).
10. **Definitions match the Lean files.**

    | Quantity | Lean definition | Matches CR-9 |
    |---|---|---|
    | T | `Nat.ceil (√2·x³)` | ✓ |
    | r | `(N - 1) / T`, natural division | ✓ |
    | η | `29·T·(3/4)^r` | ✓ |
    | a_T | `rampDiagonal T = 2(2T+1)/(3T(T+1))` | ✓ |
    | certificate shape | `(N + (2/3)(T−1) + η)(1 + a_T(k−1))` | ✓ |

    The hypothesis of the scalar lemma has exactly the form of `hk` in `secondOrder_of_scaled_certificate`, with γ = `sidonGamma`.
11. **The sign step in "Combining" is correct.** In the branch k ≥ 1 both factors are ≥ 0, and this is the same `mul_le_mul` pattern used in `FinalReduction.lean`.

### (d) Statement hygiene

1. **Quantifiers.**
   - Route A: every integer N ≥ 4,600,000 and every Sidon A ⊆ {1,…,N}. The real-variable assertion holds for every real x ≥ x₁ (in fact for x ≥ u).
   - Route B: every real x ≥ x₁ with x⁴ an integer, which is what the Lean reduction instantiates.
2. **Translation to {0,…,N−1}.** It is stated, and it uses Lemma 1 of the published proof (translation invariance).
3. **Strict versus non-strict.** The conclusion is strict (k < y), which implies the published non-strict form. The Lean lemma derives `≤` from the strict comparison by `.le`, which is consistent.
4. **No floating point and no "approximately".** Every premise is one of three kinds:
   - an exact integer or rational comparison;
   - a standard calculus fact: exp is increasing, the exp addition law, positive series tails, the log-integral representation, derivative signs;
   - a supplied lemma: Lemma 7, or the finite certificate.

   Floating point appears only in the author's remarks, and is labelled as not being a premise.
5. **Scope.** CR-9 claims no minimal onset and does not cover N < 4,600,000. This matches what is proved.

### (e) Is Route B, as written, enough for the formaliser?

**Yes, for the four files in scope.** The two uses of `hx : 120 ≤ x` in `FinalReduction.lean` can be replaced as follows.

1. **`sidonIntegerScale_tail_lt_half`.** Replace it with a new chain under `463/10 ≤ x` and `x^4 = N`:
   - (i) `√2 < 99/70`;
   - (ii) `32 ≤ (N-1)/T`, from 32T < N − 1, using `sidonIntegerScale_lt` (onset-free);
   - (iii) `√2·x < 2(r+2)`, from N − 1 < T(r+1) as in `integerQuotient_scale_bound`, with T < √2x³ + 1;
   - (iv) `(2r+5)(3/4)^r ≤ 69(3/4)^32` for r ≥ 32, by `Nat.le_induction` as in `sidonTailEnvelope_le_base`;
   - (v) `29·69·(3/4)^32 < 667/3300`, by `norm_num`.

   This replaces `r ≥ 58`, `T ≤ (3/2)x³`, `x ≤ 2(r+2)` and the constant 87/200. A hint for step (iii) that avoids division: if √2x ≥ 2(r+2), then (√2x³ + 1)(r+1) ≤ (√2x³ + 1)(√2x/2 − 1) = x⁴ − √2x³ + √2x/2 − 1. This contradicts x⁴ − 1 < T(r+1) as soon as x² > 1/2.
2. **`secondOrder_of_scaled_certificate`.** The CR-9 scalar lemma lets `120 ≤ x` be weakened to `1 ≤ x`. Do this by proving `hgap` through (B4.1)–(B4.2) instead of through `hfrac1`, `hfrac2` and `hfactor_lt`.
3. **Outside CR-9's scope, and not reviewed by me:**
   - `Statement.lean` fixes the onset of `SidonSecondOrderBound`. I was not allowed to read it.
   - The derivation of `hx` in `FinalReduction.lean` must become `463/10 ≤ x` from `4600000 ≤ N`. It can use (463/10)⁴ = 45954068161/10⁴ < 4600000 and `Real.le_sqrt_of_sq_le` twice.
   - Other files that call these lemmas, such as `Main.lean` or `FinalCheck.lean`, are outside the brief.

## 3. REPAIRS

**No mathematical repair is required.** The conclusion survives as written. The three notes below are optional:

- **E1 (line 233, wording).** Replace "the integer sequence (2r+5)qʳ" with "the sequence (2r+5)qʳ, indexed by integers r ≥ 32". The conclusion is unaffected.
- **E2 (lines 304–313, for the formaliser).** If the old structure of `secondOrder_of_scaled_certificate` is kept, it needs `hfrac1` (γ/x < 1/2) as well as `hfrac2`. At the new onset `hfrac1` follows from γ < 1 < 23 ≤ x/2. CR-9 mentions only the replacement for `hfrac2`, (B4.3). Using (B4.2) instead, as CR-9 recommends, removes both. The conclusion is unaffected.
- **E3 (lines 26 and 160–170, scope remark).** Both routes use x ≥ x₁ only through x ≥ 463/10. Stating the Lean-facing hypothesis as `463/10 ≤ x` is the simplest form. The conclusion is unaffected.

## 4. What I could not check

- **Lemma 7 (5.1)** is taken as proved, per the brief.
- **The supplied finite certificate** (`DiscreteSidonCertificateBound`) is a hypothesis of the Lean reduction and was not reviewed.
- **Out-of-scope files:** `Statement.lean` and any other Lean or checker files that hard-code 120 or 120⁴ were not read.
- **The author's 61-assertion Node checker** was not supplied, so I did not run it. Every one of its claimed objects was recomputed here independently.
- **The "typo in the brief" remark** could not be checked, because the brief is not in scope.
- **Numerical scope.** Uniformity in N beyond 2·10⁸ rests on the paper proof, which I re-derived. The exact sampling to 10¹⁶ and the mpmath sampling to 10⁸⁰ are sanity checks only.

## 5. Numerical tests actually run

All tests ran in Python 3 in the container (numpy/mpmath environment), with run-scratch scripts. Total compute was about 2 minutes.

| Script | What it did | Result |
|---|---|---|
| `exact.py` | the 55 exact Fraction/integer assertions, including table rows 1–40 | all pass |
| `sym.py` | the 8 sympy identities in rows 41–48 | all zero |
| `routeA.py`, `mono.py` | mpmath (60 digits): α, βu, e^{βu}, F(u), F(x₁), M(x₁), M(u); a grid of 20,481 points on [46.3, 10¹²]; the root gap y − ρ at 9 values of N | as reported above |
| `routeB.py` | exhaustive exact check of r ≥ 32, (B3.1) and (B3.4) for every N in [4,595,407, 2·10⁸] | 0 failures; min r = 32; worst η/x² = 0.1922682 |
| `large2.py` | exact checks on random N and r-jump windows up to 10¹⁶; mpmath log-checks up to 10⁸⁰ | 0 failures |
| `scalar.py` | 20,000 random scalar-lemma cases | 0 failures; min y − ρ = 0.3056 |

## 6. Verdict

Every step of the Route A replacement for section 6 was re-derived. It is correct, given only Lemma 7: the exact bound α > 719/2500, βu > 9.41 > 1, e^{βu} > 12100, the strictly decreasing normalized error F ≤ F(u) < 134/121, and the retained main term (10/9)x². Together these give P_ε(y) > (4/1089)x² for every real x ≥ x₁ (indeed for x ≥ 46.3). The root argument then gives |A| < √N + (2√2/3)N^{1/4} + 1, strictly, for every integer N ≥ 4,600,000. Route B is also correct and matches the Lean definitions exactly: r ≥ 32, the floor/ceiling estimate x < √2(r+2), the bound η/x² < 29(2r+5)(3/4)ʳ ≤ 2001/9900 = 667/3300 < 1/2, and the scalar lemma for x ≥ 1. All 48 displayed comparisons, 40 numeric and 8 symbolic, are true when recomputed. Exhaustive exact integer tests of B3 over [⌈u⁴⌉, 2·10⁸] and high-precision tests of Route A agree with both the proof and the verifier's replay. Verdict: **PASS**. Route B gives the formaliser enough to remove `120 ≤ x` and `r ≥ 58` from the four Lean files in scope. The onset in `Statement.lean` and the files that call these lemmas still need editing; I did not review them.
