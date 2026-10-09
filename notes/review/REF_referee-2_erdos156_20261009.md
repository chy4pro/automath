PASS-WITH-REPAIRS

# Referee report (referee-2), Erdős #156: Astra probe `problems/erdos156/PROBE_ASTRA_1_20261009.md`

Clean-room review. I read only the probe file (446 lines) and the target brief in the task. I did not read any other repository file, the web or papers. Line numbers below refer to the probe file.

**Bottom line.** I re-derived every statement labelled as proved, and I found no mathematical error. No failing line, no circularity, no hypothesis used before it is available. Every finite table in §6 reproduced exactly with independent Python code. The required repairs concern labelling and status (R1), plus three small precision and presentation points (R2–R4). On the merits, the honest status for the target is **OPEN**. The report proves correct auxiliary lemmas and two model-specific negative results, but no statement about s(N) beyond the classical lower bound. PARTIAL is acceptable only if it is explicitly scoped to "auxiliary lemmas only". Line 446 ("PARTIAL for the research target") contradicts line 9 and must be changed.

---

## 1. Claim-by-claim verdicts

### §1. Blocking criterion and (1)–(2) (lines 13–35): CORRECT
- **Criterion (line 21).** Re-derived. For x ∉ A, the new sums are x+a (a ∈ A) and 2x.
  - A collision x+a = b+c gives x ∈ T(A). Here b = c is allowed, so the repetition convention is respected. The case a ∈ {b,c} would force x ∈ A.
  - A collision 2x = b+c gives x ∈ Q(A), and b ≠ c because x ∉ A.
  - x+a = x+b and x+a = 2x are impossible.
  - Conversely, x = a+b−c with c ∉ {a,b} gives the collision x+c = a+b.
  - Group remark (line 23): Q defined as all solutions of 2x = a+b, including a = b, is also correct in groups with 2-torsion, where 2x = 2a with x ≠ a is a genuine collision.
- **(1).** The count is m + m·m(m−1)/2 + m(m−1)/2 = (m³+m)/2. Checked.
- **(2).** 2N ≤ m³+m is correct. This is the classical N^{1/3} lower bound with an explicit constant, and the report correctly says it is not progress (line 33).
- **Line 35.** Monotonicity of the blocked set, which gives s(N) ≤ |A| + #holes(A), is correct.

### §2.1 (lines 41–45): CORRECT
Integer Sidon-ness of one-representative lifts holds, and every other integer in an occupied residue class is addable. Invertibility of 2 is not needed. The count k(H−1) is correct for I = {0,…,HM−1}.

### §2.2 Criterion and (3)–(4) (lines 49–69): CORRECT, minor presentation gap (R3)
- **"Only if" direction.** Re-derived; this is the direction used for (3). A repeated positive difference s−t = u−v gives either a within-fibre collision (d+Ms)+(d+Mv) = (d+Mu)+(d+Mt), which is nontrivial because s ≠ t, or a cross-fibre collision (d+Ms)+(e+Mv) = (d+Mt)+(e+Mu). This direction does not need D to be Sidon.
- **"If" direction.** This needs D Sidon in Z/MZ together with representatives in {0,…,M−1}, so that the residue identity d+e ≡ f+g with {d,e} = {f,g} becomes an integer identity. That hypothesis appears only in the heading ("modular Sidon support"), not in the statement.
- **Repetition convention.** A 3-term AP s, t, v inside S_d gives the repeated positive difference s−t = t−v and the collision s+v = 2t. This is correctly counted as a collision under the repetition convention.
- **(3) and (4).** Σ C(|S_d|,2) ≤ H−1 and t ≤ H−1 follow, using C(1+t_d,2) ≥ t_d.

### §2.3 Bound (5) (lines 73–77): CORRECT
- **Proof.** Phase 1 keeps the set inside the family C of §2.2 with S_d ⊆ {0,…,H−1}, so t ≤ H−1, and it ends with every D-residue point blocked. Phase-2 additions are unblocked with respect to the current set, hence initially unblocked by monotonicity, and they have residue outside D. So there are at most u of them, and translation gives (5).
- **Labelling remark (optional, R4).** (5) is an unconditional inequality; it holds for every choice of the a_d. Only its usefulness is conditional on u being small. Calling it "conditional" (lines 1, 71) is harmless but slightly misleading.
- **Example at line 79.** (1+c+C)k−1 is correct. The report correctly declines to infer anything for N not of the form HM.
- **Collision at line 83.** Correct.

### §2.4 Singer family, (6) (lines 89–105): CORRECT
- **Trace.** The trace is nonzero because a nonzero polynomial of degree q² has at most q² < q³ roots, so its kernel has dimension 2.
- **Size and representations.** D has (q²−1)/(q−1) = q+1 elements. For α ∉ F_q, Tr(z) and Tr(αz) are independent forms; otherwise Tr((α−c)z) ≡ 0. Their common kernel is a line, so there is exactly one ratio representation.
- **Arithmetic.** M = (q+1)² − (q+1) + 1 = q²+q+1.
- **Sidon from difference uniqueness.** Correct, including 2a = c+d.
- **Independent check.** I implemented exactly this construction (trace-zero powers of a primitive element of F_{q³}, reduced mod M) for q = 2, 3, 5, 7, 11, 13. Every output is a perfect difference set with M = k²−k+1.

### §3 Moment curve in F_p³, (7)–(10) (lines 109–158): CORRECT, group model only
- **Formulas re-derived by hand.**
  - c = S−u and P = uS − (u²+v)/2.
  - w = S³ − 3SP − (S−u)³ = u³ + (3/2)(v−u²)S, which is (8).
  - Discriminant S²−4P = (S−2u)² + 2δ, which is (9).
- **Point count.** #{y : y²+c is a square or 0} = (p+χ(−c))/2. The proof via counting solutions of z²−y² = c is correct. Summing over δ ≠ 0 kills the character term, so each u contributes p(p−1)/2 + 1, which gives (7).
- **Midpoints and (10).** The midpoint is (u, u²+d², u³+3ud²), giving S = 2u and discriminant 2d². This yields (10).
- **Scope.** The statement is about the additive group F_p³, which is not cyclic and not an interval. The report says so (lines 158, 323). It shows the candidate is far from maximal (about p³/2 holes) and claims nothing more.

### §4.1 Witness structure (lines 168–198): CORRECT, one presentation gap (R3)
All of the following were re-derived:
- exactly k ordered representations, and c ∉ {a,b};
- (11);
- no three-element support with two different negative vertices, since 2(c−c') = 0 and M = k²−k+1 is odd;
- Σ_x t_x = k(k−1), because 2a−c ∉ D;
- (12), since k(k−1)/5 ≤ (k−1)²/2 holds for every k ≥ 5/3;
- at most one common three-element support for x ≠ y, from x−y = 2(c_y−c_x) and difference uniqueness.

**Gap at lines 178–179.** The text bounds the vertex degree by "two triple supports plus the midpoint witness". It does not say why diagonal two-element supports {a,c} (x = 2a−c) do not raise the degree. The bound ≤ 3 is still true. The positive-role equation x = d+b−c fixes the single representation in which d is positive, whether it is a triple (b ≠ d) or a diagonal (b = d). The negative-role equation fixes the single unordered pair {a,b}, possibly a = b. So the bound covers the whole family F_x. I confirmed computationally (below) that the maximum degree over all supports, diagonals included, is exactly 3.

### §4.2 Harris inequality and (13) (lines 202–220): CORRECT
- **Harris.** The law of total covariance gives Cov = E[Cov(·|X)] + ρ(1−ρ)Δf·Δg. Both Δ terms are ≤ 0 for decreasing functions, and the induction is valid.
- **(13).** I re-derived the identity q_i − (1−p_i)q_{i−1} = P(E_i∩B∩C^c) − p_i·P(B∩C^c), using that E_i is independent of B. The union bound and the iteration with multiplier in [0,1] are correct.

### §4.3–4.4 First and second moment, (14)–(16) (lines 226–271): CORRECT
- **Lower bound.** b uses (k/2)·(8/7)ρ³ + 5·(4/3)ρ², which gives (15).
- **Pair bound.** Union-family degree ≤ 6. Triple–triple adjacent pairs number ≤ 15k/2, each contributing ≤ 2ρ⁴. Pairs involving a two-element support number ≤ 100, each contributing ≤ 2ρ³. Removing duplicate factors costs ≤ 5ρ² + ρ³. Together these give ε.
- **(16).** Cov ≤ ε and Var U ≤ g + g(g−1)ε, then Chebyshev, 1/g ≤ 2/(k−1)² and 1/b² = exp(8kρ³/7 + 40ρ²/3). All steps check.

### §4.5 Specialisation, (17) (lines 277–313): CORRECT, one imprecision (R2)
Re-derived:
- ρ ≤ 1/2 from L ≥ 6 log(2C) and log L ≤ L/2;
- (8/7)kρ³ = (8/7)C³L^{3θ} ≤ L/12 ⇔ L^{1−3θ} ≥ (96/7)C³ (equality at L = L₀ when that term is the maximum);
- ρ² ≤ C²k^{−5/8}, ρ³ ≤ C³k^{−15/16} and kρ⁴ ≤ C⁴k^{−1/4}, using L^{4/3} ≤ k^{1/12} for L ≥ 128;
- the final exponent −1/4 + 1/12 = −1/6.

**Imprecision at line 313 (R2).** The negative-θ remark says "for k ≥ e". The coupling ρ_θ ≤ ρ_0 needs only L ≥ 1, but the θ = 0 bound then needs k ≥ K(C,0).

**Onset size.** The onset is effective but astronomically large, which the report does not state:
- K = e^{128} ≈ 10^{55.6} for C = 1, θ = 0;
- about 10^{1.02·10^{11}} for C = 1, θ = 0.3;
- about 10^{2.27·10^{113}} for C = 1, θ = 0.33.

So (17) is explicit but vacuous in any computable range. That is not an error, but it should be said (R4).

**Scope.** The section is about Z/MZ and about one sampler (independent thinning of a fixed perfect difference set). It concerns coverage of points outside D only. The report states all three restrictions (lines 162, 164, 315, 325) and does not present the result as an interval statement or as a general obstruction.

### §5 Stopping points (lines 319–331): CORRECT
Item 6 was re-derived: ℓ = ⌊N/5⌋ ≥ N/10 for N ≥ 8, d ≤ 5ℓ−1 ≤ N, there are ℓ³ distinct supports, and ℓ³r⁴ ≥ m⁴/(1000N). No item claims more than it shows.

### §6 Finite checks: ALL REPRODUCED EXACTLY (details in §3 below)

---

## 2. Errors and repairs

**Errors invalidating a claimed statement: none found.**

Required repairs:
- **R1 (status and honesty), lines 1 and 446.**
  - Line 446 ("The final disposition is PARTIAL for the research target") contradicts line 9 ("The brief's improved upper-bound target remains OPEN") and the status line's own "No bound … is proved". Replace it with "OPEN for the research target; auxiliary lemmas and model-specific negative results proved".
  - On line 1, either use OPEN, or keep PARTIAL with the explicit qualifier "(auxiliary lemmas only; target OPEN)".
  - Also on line 1, add the scope qualifiers: "cubic-curve coverage counts *in the group F_p³*" and "obstruction for independent thinning of perfect difference sets *in Z/MZ, outside-D coverage only*".
- **R2, line 313.** Replace "for k ≥ e" with "for k ≥ K(C,0) (the coupling itself needs only k ≥ e)".
- **R3, lines 49–53 and 178–179.**
  - In §2.2, state the hypothesis "D ⊆ Z/MZ Sidon, representatives in {0,…,M−1}", and note that the direction used for (3) does not need it.
  - In §4.1, add one sentence explaining that diagonal supports are covered by the same positive-role and negative-role uniqueness, so the degree bound 3 holds for all of F_x.

Optional:
- **R4, lines 71 and 277–291.** Call (5) unconditional, with conditional use. Record the size of the onset K(C,θ) = exp(L₀), including the bound L₀ ≥ ((96/7)C³)^{1/(1−3θ)}, which blows up as θ → 1/3.

---

## 3. Independent re-checks actually run

All checks used my own Python (numpy / mpmath via the automath venv), single process, well under 5 CPU-minutes in total. No SAT/ILP solvers were used.

1. **§6.1, every Sidon subset of [N] for N = 1..24.** Depth-first search with incremental sum sets. At every node I compared the direct addability test against the T ∪ Q criterion for every outside point, and checked (2) at every maximal node.
   - Results: s(N) matches all 24 rows; Sidon-subset counts match all rows (the empty set is included, as in the report); maximal-subset counts match all rows.
   - Totals: 84,274 subsets and 1,436,132 comparisons, with 0 criterion failures and 0 violations of (2). All match the report.
   - Second, fully independent method: brute force over all 2^N subsets with a naive Sidon test, for N ≤ 16. This gave identical counts, maximal counts and s(N).
   - The three example minimisers {2,5,6} ⊂ [10], {4,7,12,13} ⊂ [22] and {1,2,4,8,20} ⊂ [24] are all maximal Sidon.
2. **§6.2, perfect difference sets M = 7, 13, 21.**
   - Perfectness and pair-sum uniqueness hold. Each outside point has k ordered representations; the maximum vertex degree is 3; the maximum number of shared triple supports is 1.
   - Comparisons: 32 + 144 + 512 = 688, with 0 failures.
   - All three histograms match exactly.
   - All 18 exact moments (EU, EU² and P(U=0) at ρ = 1/2 and 1/4) match as unreduced fractions. For example, for M = 21 at ρ = 1/4: EU = 13662/1024, EU² = 192510/1024, P(U=0) = 16/1024.
   - g = 4, 9, 15. For M = 21, t_x is (1 × 15, 5 × 1), confirming the one excluded point.
3. **§6.3, all 407 height assignments.**
   - All 3,488 D-residue comparisons were addable, with 0 failures.
   - The table rows (minimum initial holes 3/8/5/13/7/19 and best ascending-greedy sizes 4/5/5/6/6/7) match exactly.
   - In the two-phase repair, the maximum number of phase-1 additions equals H−1 in every row. Every final set was maximal, and (5) held for every assignment, including that phase-2 additions were ≤ u.
4. **§6.4, moment curve.**
   - Full enumeration of T_p, of the midpoints, and of the unblocked count, for p = 5, 7, 11, 13, 17, 19, 23, 29, 31.
   - Every table entry matches, and so do (7) and (10). The discriminant criterion (8)–(9) gave 0 mismatches over all of F_p³.
   - I extended the check to p = 37 and 41, where (7) and (10) also hold exactly.
5. **§2.4 construction.** Singer sets were built from the trace for q = 2, 3, 5, 7, 11, 13 (k = 3, 4, 6, 8, 12, 14). All are perfect with M = k²−k+1.
6. **§4 inequalities, exact.** For each of these Singer sets and ρ ∈ {1/2, 1/3, 1/4, 0.1, 0.05}, I enumerated all 2^k subsets exactly and verified:
   - Σt_x = k(k−1), h_x = (k−t_x)/2, degree ≤ 3 (diagonals included) and g ≥ (k−1)²/2;
   - at most 1 shared triple support (the observed maximum of shared two-element supports was 2, against the bound 5);
   - P(I_x=1) ≥ w_x ≥ b for every x ∈ G;
   - P(I_x=I_y=1) ≤ w_xy + (the (13) error term) for every pair, and w_xy ≤ w_xw_y + 5ρ² + ρ³;
   - max Cov(I_x,I_y) ≤ ε, EU ≥ gb, and P(U=0) ≤ Var U/(EU)² ≤ RHS(16).
   
   Zero violations in 30 parameter sets. The bounds are very lossy: for example, at k = 14, ρ = 1/4 the maximum covariance is 0.0996 against ε = 4.27.
7. **(13) and Harris on arbitrary families.** I tested 3,000 random families of events (n ≤ 10 coordinates, up to 8 events, supports of size ≤ 3). Half were monotone and half were arbitrary events determined by their support. I computed exact probabilities and found max(LHS − RHS) of (13) = +5.6·10⁻¹⁶, and max(∏(1−p_i) − P(none)) = +5.6·10⁻¹⁶ for the monotone half. Both are at floating-point rounding, so there are no violations.
8. **§4.5 onset algebra.** High-precision mpmath check (80 digits), done in log space to avoid cancellation, for C ∈ {0.01, 0.1, 0.5, 1, 2, 5, 10}, θ ∈ {0, 0.1, 0.2, 0.3, 0.33, 0.3333} and L = L₀·{1, 1.0001, 1.5, 2, 10, 10², 10³, 10⁶}. That is 336 cases.
   - ρ ≤ 1/2 holds in every case.
   - (16) ≤ J(C)k^{−1/6} holds in every case. The minimum slack is 17.58 in log scale, because the k^{−1/4} and k^{1/12} estimates are very generous.
   - (8/7)kρ³ ≤ L/12 holds everywhere except 10 cases at L = L₀ exactly. There the inequality is an exact equality, and the relative discrepancy is about 10⁻⁷⁸, which is rounding.
   - A first naive run that did not work in log space showed spurious "failures" from catastrophic cancellation at L about 10^{41371}. These were artefacts, removed by the log-space rewrite.

## 4. Honest status

**OPEN** for the target s(N) ≪ N^{1/3}(log N)^θ, θ < 1/3. What the report proves is:
- (a) the classical lower bound with an explicit constant;
- (b) a correct but elementary reduction lemma (5);
- (c) an exact computation showing that one algebraic candidate in a non-cyclic group is far from maximal;
- (d) a rigorous concentration statement showing that one specific sampler, in the group model, fails at sub-logarithmic density.

None of these is a bound on s(N) beyond what is known, a restricted case of the target, or an interval statement. HIT is clearly not warranted.

Apart from line 446, the report is careful not to dress anything up:
- the obstruction is repeatedly scoped to one sampler (lines 9, 162, 315, 325, 327);
- the group setting is stated;
- §2.3 explicitly declines the truncation inference.

So PARTIAL is defensible only in the weak sense "auxiliary lemmas proved". With R1 applied, the report is honest.

## 5. Value

**Usable lemma.** The fibre-repair inequality (3)/(4)/(5) is usable. For any lift of a modular Sidon set to {0,…,HM−1}, all holes inside occupied residue classes are repaired by at most H−1 greedy additions in total, so a lift construction only has to control outside-residue holes. The exact witness structure of perfect difference sets in §4.1 (k ordered representations, degree ≤ 3, ≤ 1 shared triple) is also reusable.

**Usable negative result.** Independent thinning of a perfect difference set at |A| ≍ M^{1/3}(log M)^θ with θ < 1/3 leaves outside holes with probability ≥ 1 − J(C)k^{−1/6}, so second-moment methods cannot rescue an *independent* sampler. This is the rigorous form of the first-moment heuristic that produces the log.

**Remaining obstruction.** This part is my heuristic reading, not a claim of the report. For a lift A = {d + M·h_d}, an outside residue r is blocked at level j exactly when j = h_a + h_b − h_c + (carry ∈ {−1,0,1}) for one of its witnesses (the (k+t_r)/2 unordered representations of r as a+b−c mod M, plus at most one midpoint; about k/2 of them). So u ≤ Ck at H ≍ k needs a correlated, design-like choice of heights under which the witness levels of almost every outside residue cover {0,…,H−1}. Independent heights incur a coupon-collector loss that forces H ≍ k/log k, which is exactly the (N log N)^{1/3} scale. That correlated height design (or an equivalent repair), followed by passage to every N, is the missing step.

## 6. What I could not check

- The report's provenance and process claims: what was read, the use of Node, the CPU timings, and "no repository material read".
- The unspecified "floating-point evaluations of the coarse mean/variance bounds" mentioned in §6.2. I substituted my own exact checks of every Section 4 inequality.
- I did not attempt the target itself, per the brief.
