PASS-WITH-REPAIRS

# Referee report (referee-2): T6 Erdős #30, Astra probe `problems/erdos30/PROBE_ASTRA_2_20261009.md`

Date: 2026-10-09. Clean-room review: I read only the file under review and the task brief. No web, no papers, no other repository files.

**Bottom line.** I re-derived every statement the report labels as proved and found no false step, gap, circularity, or wrong onset. Quantifiers and conventions are consistent: integer setting throughout; positive differences; D(d) counts unordered pairs; V_tri sums over ordered pairs including the diagonal; the fourth moment counts ordered quadruples. Every finite check I re-ran agrees exactly. **The STATUS line is overstated, though.** Nothing in the report moves toward c < 2√2/3. Each proved item is one of three things: elementary bookkeeping; a no-go for a relaxation the authors chose themselves, which is strictly weaker than the premise theorem; or a construction that realises the end-cluster *counts* only, which is automatic at these parameters. The honest status is **OPEN**, with auxiliary side results. The body text is careful and disclaims all of this. The headline and status label must be repaired (R1–R3 below). The verdict is therefore PASS-WITH-REPAIRS rather than PASS.

## 1. Claim-by-claim verdicts

Line numbers refer to the reviewed file.

| Location | Claim | Verdict | How I re-derived it |
|---|---|---|---|
| L7 | Sidon ⇔ unique unordered sums (with repetition) | Correct | Both directions by hand. The repeated-summand case is the 3-AP case a−b=b−d. |
| (1) L29–33 | Σr = S, Σr² = S+2P, Σr³ = S+6P+6H | Correct | W=N+T−1 means no window is truncated, so each point lies in exactly T windows. A pair a<b lies in (T−(b−a))₊ common windows and a triple in (T−(c−a))₊. I checked u² = u+2C(u,2) and u³ = u+6C(u,2)+6C(u,3) by expansion. |
| (2) L45 | Σr² ≤ mT+T(T−1) | Correct | D(d) ≤ 1 and Σ_{d<T}(T−d) = T(T−1)/2. |
| (3) L53 | V_tri = Q/T ≥ 0; kernel positive definite | Correct | Σ_{a,b} g = m + 2P/T = Σr²/T (ordered pairs with diagonal), and Q = Σr² − S²/W. T·g((a−b)/T) = \|[a,a+T−1]∩[b,b+T−1]\| for integers a, b, so the kernel matrix is a Gram matrix. |
| (4) L60 | 6H = Wμ(μ−1)(μ−2) + 3(μ−1)Q + R | Correct | Re-expanded R = Σr³ − 3μΣr² + 2Wμ³ by hand. Exact on 87,240 + 809,379 instances (§4). |
| (5) L77 | Q ≥ Wθ(1−θ), with equality iff r ∈ {q, q+1} | Correct | Σ(r−q)(r−q−1) = Q − Wθ(1−θ). |
| (6) L86 | normalised integrality gain ≤ 2N^{−1/4} | Correct | T ≥ N^{3/4}/2 and W ≤ 2N−1. |
| (7), (8) | cubic and Cauchy–Schwarz inequalities | Correct | (7) holds for every integer q, not only ⌊μ⌋. |
| (9) | C₃ ≤ 1; H ≤ C(T,3) | Correct | Σ_{v}(v−1)(T−v) counts the 3-subsets of {1..T} by span. |
| (10) L121–123 | H ≤ U_T ≤ √(2T)·T(T−1)/2 | Correct | Span-capacity argument: q₀(q₀−1) ≤ 2d, and at most one endpoint pair per d. k_d ≤ √(2d) because √(1+8d) ≤ 1+√(8d). The floor formula equals the integer definition for d < 3000. |
| (11) L127 | U_T ≥ T^{5/2}/64 for T ≥ 64 | Correct | The number of admissible d is ≥ (T−1)/4 ≥ T/4−1 ≥ T/8. Numerically (exact integers) (11) holds for every 4 ≤ T ≤ 20000. |
| Prop. 1.4 L141–199 | scalar relaxation admits Q/(Tm) ≤ 1/(2s) for s ≥ 65536, s² ≤ m ≤ s²+s | Correct **as stated** (see E3 on scope) | Re-derived every step. S_max = s(W+1), so q = k = s at that mass. The balanced minimiser is monotone in mass. Σr(r−1) ≤ s⁶−s⁴+s²+s ≤ s⁶−s³. The subset-sum lemma for {1..T−1} holds. The chain H ≤ (8/3)s⁷ < s^{15/2}/64 ≤ U_T needs √s ≥ 256, which is the only source of the onset 65536. C(T,3) ≥ T³/24. Q/(Tm) ≤ (s+1)/(4s²) ≤ 1/(2s). |
| §1.5 L201–223 | homometric Sidon pair with H(A)=1, H(B)=0 at T=5 | Correct | All 15 differences {1..13,16,17} recomputed for both sets. W=22, S=30, P=10, Σr²=50, Σr³ = 96 / 90, Q = 100/11, V_tri = 20/11, R(A) = 366/121, R(B) = −360/121, R(A)−R(B) = 6. (These are the two optimal 6-mark Golomb rulers.) |
| §2 Prop. L229–299 | Sidon A ⊂ [1,N], 2m points, exactly m in each end window of length L=⌊N^{3/4}/10⌋; (13), (14) | Correct | Sidon proof of b_i = 2pi + (i² mod p) re-done: the size bound forces equal gaps h, then h(j+i) ≡ h(l+k), so i = k. B₀ = 8m²+2 (true for p ≥ 5). Cross differences exceed B₀ once N > 2B₀+1, and 4m⁴ > 16m²+5 for m ≥ 3. L > 2p² > B₀+1 for m ≥ 30. (13) follows from the mean-value bound on t^{1/4}. Euclid gives infinitely many primes. |
| (15), (16) L305–321 | endpoint difference budgets and their slack | Correct | Both budgets re-derived. N^{3/4} ≥ 64 gives L−1 ≥ N^{3/4}/20 and 2L−1 ≥ N^{3/4}/10. Checked exactly for all 256 ≤ N ≤ 200000 and N = 10⁶,…,10¹⁸. |
| §3.2 L329–334 | Σ(Δr)² = 2m − 2D(T); Σr² ≥ (m−D(T))/2 | Correct | r is extended by 0 on **both** sides (x ≤ 0 and x ≥ W+1). Exact on all instances N ≤ 16. |
| §3.3 L336–344 | M(M+1) ≤ h(h+1)(N−1); m ≤ s²+s+½ at N=s⁴ | Correct | The bound j(N−1) on the j-th telescoped sum also holds when j > m−j (only m−j < j pairs survive). Exact on all instances N ≤ 16. |
| §3.4 L346–353 | ∫\|F\|⁴ = 2m²−m | Correct | Standard. Exact check. |
| §3.5 L355–359 | equal-sum triples are disjoint; C(m,3) ≤ 3N⌊m/3⌋ | Correct | Exact check, N ≤ 16. |
| §4.1–4.3 | tables and aggregate checks | Exact agreement | See §4 below. |

## 2. Errors and over-statements

No mathematical error was found. The problems are with the status and with how the results are framed.

**E1 — status label (L1, also L452).** "PARTIAL" is not justified. Breaking down what was proved:
- (1)–(11) are elementary inclusion and counting identities.
- Prop. 1.4 is witnessed by a flat array, for a relaxation weaker than the premise theorem (E3).
- §2 realises only the cluster counts, which is automatic (E2).
- §3 restates textbook facts (Erdős–Turán/Lindström telescoping, E(A) = 2m²−m).

The report itself says "No bound with c < 2√2/3 is proved" and "the requested improvement … remains open". None of the results is a statement toward the target, a restricted case of it, or a non-trivial obstruction. Honest status: **OPEN**.

**E2 — "realizing both proposed endpoint clusters" (L1, heading L225, L299, L361).** In the brief, an end cluster is part of an extremal profile: about √N points in total, and every difference below about 1.5N^{3/4} used exactly once. The construction gives something much weaker:
- It has only 2m ≈ 1.38N^{1/4} points in total.
- It uses no difference below p+1 ≈ 1.38N^{1/4}.
- It fits each cluster in length 8m²+3 ≈ 3.8N^{1/2}, far below L ≈ 0.1N^{3/4}.

That the counts are realisable is automatic. A Sidon set of m points needs length only about m² ≈ 0.48N^{1/2}, and L ≈ 0.1N^{3/4} is much larger. Splitting one Sidon set of size 2m and pushing the halves to the two ends handles the cross differences. L301 states the limitation correctly. The status line and the §2 heading do not. L361 ("Section 2 supplies actual simultaneous endpoint clusters") repeats the over-reading.

**E3 — scope of Prop. 1.4 (L139–199, L1).** The relaxation uses one triangular kernel at one scale T = N^{3/4}. Its admissible range is the triangular-kernel second-order range c ≤ 1. The premise theorem is sharper: for N = s⁴ ≥ 120⁴, it already excludes every m > s² + (2√2/3)s + 1. Part of the Proposition's range is therefore empty for real Sidon sets: (s² + 0.9428s + 1, s² + s] is non-empty for all s ≥ 18, so for every s ≥ 65536. Two consequences:
- Prop. 1.4 is a no-go for "triangular kernel + scalar cubic and integrality constraints". It is *not* a no-go for third-order information added on top of the optimal-kernel argument, which is where the 2√2/3 barrier lives.
- The witnessing arrays have every entry ≥ q ≥ s−1 ≥ 65535. Every genuine window profile has r(1), r(W) ∈ {0,1}.

L9, L154 and L199 partly disclose this ("not the brief's optimized residual energy", "window boundary conditions … not enforced"). The phrase "even for cardinalities throughout the second-order range in question" (L199) should say exactly which range is meant.

**Minor points (not errors):**
- L123: "the first of these inequalities" is ambiguous. It means k_d ≤ √(2d), not H ≤ U_T.
- L266: "The residue is 4 because p ≥ 61" — p ≥ 5 suffices.
- L141: the onset s ≥ 65536 is only an artefact of using (11). With exact U_T, the Proposition's conclusions hold for every s in [2,300] (§4(e)).

## 3. Required repairs

- **R1 (L1, L452).** Change the status line to: "OPEN — no statement toward c < 2√2/3. Side results: exact window-moment identities (1)–(4); a no-go for the single-scale triangular-kernel + scalar-cubic relaxation (Prop. 1.4); a counts-only realisation of the end-cluster sizes in a Sidon set of total size 2m ≈ 1.38N^{1/4}." At L452, replace "partial-result/obstruction report" accordingly.
- **R2 (L1, L225, L299, L361).** Replace "realizing both proposed endpoint clusters" with "realizing the end-cluster counts (≈0.69N^{1/4} points in each end window of length ≈0.1N^{3/4}) in a Sidon set of total size 2m, with no bulk and no difference below p+1". Add one sentence saying this is expected because m² ≪ L. At L361, replace "actual simultaneous endpoint clusters" with "the cluster counts alone".
- **R3 (L199).** Add: "The relaxation admits m up to s²+s, which includes cardinalities m > s² + (2√2/3)s + 1 already excluded by the premise bound. It is therefore strictly weaker than the known pair-only argument, and the witnessing arrays violate r(1) ≤ 1. The proposition is a no-go for this relaxation only, not for third-order information combined with the optimal kernel."
- **R4 (cosmetic).** L123: write "the inequality k_d ≤ √(2d)". L266: write "p ≥ 5". Optionally, L141: note that the onset comes from (11) and is not sharp.

## 4. Independent re-checks

All checks used my own Python code with exact integer or rational arithmetic, plus mpmath at 60 digits for (13)/(14). Total CPU was under one minute. No SAT/ILP solver was used.

**(a) Sidon enumeration (§4.1 table).** I enumerated all Sidon subsets of {1..24} by recursion. For N ≤ 14 I cross-checked completeness against brute force over all 2^N subsets, and checked the Sidon property of every enumerated set independently. Results match the table at L380–404 in all 24 rows, exactly:
- Number of Sidon subsets: 2, 4, 7, 13, 22, 36, 57, 91, 140, 216, 317, 463, 668, 962, 1359, 1919, 2666, 3694, 5035, 6845, 9188, 12366, 16417, 21787.
- F(N): 1,2,2,3,3,3,4×5,5×6,6×7.
- Saturation column: 0,1,1,3,3,3,6,…,6,9,…,9,13,…,13.
- Example sets: {1,2}, {1,2,4}, {1,2,5,7}, {1,3,8,9,12}, {1,2,5,11,13,18}.
- Totals for N ≤ 16: 6,276 sets and 87,240 (N,A,T) instances. These agree.

**(b) Identities on small sets.** On all 87,240 instances with N ≤ 16 I checked (1), (2), (3), (4), (5), (7), (8), H ≤ U_T ≤ C(T,3), the jump identity, E(A) = 2m²−m, the telescoping inequality, and triple-sum disjointness with C(m,3) ≤ 3N⌊m/3⌋, all using rationals. Result: **0 failures**. As an extension beyond the report, I checked (1), (2), (4)·W², (5), (7) and H ≤ U_T on all **809,379** instances with 17 ≤ N ≤ 22, integer-only. Result: **0 failures**. (My first run of this extension failed because I had scaled my own encoding of (4) wrongly; after fixing that, 0 failures.)

**(c) §1.5 values.** Exact agreement (values listed in §1 above).

**(d) U_T, (10) and (11).** U_T in closed form (summing over d grouped by k_d) agrees with brute force for T < 400 and T = 1000, 5000. (11) holds for every 4 ≤ T ≤ 20000 and fails only for T ≤ 3. The upper bound in (10) holds for all T ≤ 20000.

**(e) Prop. 1.4.** For s = 65536 and s = 100000 I checked the six m values of L432–435. All checks pass: Σr(r−1) ≤ T(T−1), 2P even, (64H)² ≤ T⁵, 2s·k(W−k) ≤ WTm, H ≤ C(T,3), and H ≤ U_{s³} computed **exactly**:
- U_{65536³} = 501283189871849667468955412816850504.
- U_{100000³} = 11925694879998897014748731606983480136.

The same checks pass for **every** m in [s², s²+s] at both values of s. With exact U_T, the conclusions also hold for every s ∈ [2,300] and every m in that range.

**(f) §2 / §4.2.** For p = 61, 101, 257, 1009 I get exactly:
- N = 3573458, 27572977, 1184250334, 284659565968.
- L = 8218, 38050, 638384, 38971250.
- B₀ = 7202, 20002, 131074, 2032130.
- Number of differences: 1770, 4950, 32640, 507528.
- Minimum difference: 69, 111, 273, 1041.

In each case A is Sidon, has exactly m points in each window, satisfies (13) (e.g. 4.51e−7 ≤ 9.26e−6 at p = 61) and (14), and fits in windows of length 8m²+3. For all odd primes 29 ≤ p < 600 every property holds. It fails only for p ≤ 23, which is below the stated onset 61.

**(g) (16).** Holds for every 256 ≤ N ≤ 200000 and N = 10^k with 6 ≤ k ≤ 18, using exact floors for q and L. Both ratios are < 1 for every tested N ≥ 10000.

**(h) Robustness probe (mine, not a claim of the report).** I added end caps r(x) ≤ ⌊√x⌋ and r(W+1−x) ≤ ⌊√x⌋ to the Prop. 1.4 relaxation, which forces r(1) = 1 and |Δr| ≤ 1, and water-filled the mass. I tried s = 100, 1000, 10⁴ with m = s² + ⌊cs⌋ for c ∈ {0.5, 0.9, 0.94, 0.97, 1.0}. In every case Σr(r−1) ≤ T(T−1) still holds and Q/(Tm) ≈ 1/(3s): between 3.4e−3 and 5.8e−3 at s = 100, and between 3.3e−5 and 5.8e−5 at s = 10⁴. So the boundary omission is *not* what drives Prop. 1.4; the no-go survives these elementary end conditions. Caveat: the caps ⌊√x⌋ are a heuristic stand-in for r(x) ≤ F(x), not exact Sidon constraints.

## 5. What I could not check

- The premises: the known bound and the kernel-barrier statement. The report also takes them as given.
- The report's Node.js runs, its CPU figures, and its clean-room declaration.
- Whether the no-go in (h) survives the *full* realisability of r as the window profile of a Sidon set. I did not attempt this; it is outside the referee scope.

## 6. Honest status

**OPEN.** All proofs are correct. But none of the proved items is a statement toward F(N) ≤ √N + cN^{1/4} + o(N^{1/4}) with c < 2√2/3, nor a restricted case of it. The two "negative" results are both one level too weak to bear on the target:
- Prop. 1.4 works at the triangular-kernel level c = 1, not at the 2√2/3 barrier.
- §2 realises the counts only, not the forced cluster structure.

Nothing is hidden in the body text. The over-statement sits in the status label and the headline phrasing (E1–E3).

## 7. Value

Usable from the report:
- Identity (4). It shows that a lower bound on the third-order count H transfers to the residual Q only together with control of the centred third moment R. The homometric pair in §1.5 shows this is a real issue even for optimal Golomb rulers.
- A clean negative lemma: scalar third-moment, integrality and span-capacity constraints cannot produce κ > 0 at the triangular-kernel level, and by probe (h) this stays true after adding end caps.
- Section 2.1 (with §2): the end clusters cannot be refuted by counting differences inside or across the two windows.

The remaining obstruction is exactly the brief's target. One needs a quantitative inequality that couples the near-saturation of all differences below about 1.5N^{3/4} with the ≈ √N-point hyperuniform bulk and the end clusters — a positional or realisability constraint on the window profile — and it must work on top of the optimal-kernel argument, not the triangular one. The report provides none.
