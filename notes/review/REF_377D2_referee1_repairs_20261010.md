PASS-WITH-REPAIRS

Resumed referee-1 session of AUT-100 (same session that wrote the first-round report `notes/review/REF_377D2_referee1_20261010.md`). Read only: the revised `main.tex`, `REVISION_REPORT.md`, my earlier report, and the EGRS page images p. 85–89.

# REF #377-D2 repair confirmation — revised note on EGRS Theorem 4

## Verdict (provisional)

All four repairs I asked for are applied (R1, R2, R4, plus the optional R3). The new proof of (LOCAL) is correct step by step, but it rests on two imported counts. The revision quotes both as "uniform" estimates and attributes that uniformity to EGRS. **The page images do not print uniformity.** EGRS p. 86 reads "for each p with x^{1/(r+1)+eps} < p < x^{1/r-eps}, A(p;x) = x/2^r + o(x)". EGRS p. 88 reads "then we see by (1) that A(p,q;x) = x/2^{r+t} + o(x)". Neither says "uniformly"; EGRS only use uniformity implicitly, when they sum over p and q. The gap is REPAIRABLE, and a short self-contained proof of the uniform counts is given below (repair N1). No FATAL gap was found.

## Repairs required in this round

* **N1 (lines 250–269 and 282–294; eq:input1, eq:input2).** "uniformly for ..." in eq:input1 and eq:input2, and "The imported assertions say e_i -> 0", overstate what is printed. Two fixes are possible:
  - (a) Write "EGRS state these counts pointwise with o(x); their summation over p, q uses, and their argument via (1) gives, the uniform form, which we now prove." Then insert the lemma below.
  - (b) Quote the displays as pointwise and add the lemma as the actual input.

  **Lemma (nested scales; effective).** Let X >= 1, 0 < eps < 1, and let positive integers w_1 < ... < w_m satisfy w_1 >= X^eps >= 2, w_{i+1}/w_i >= X^eps (1 <= i < m) and X/w_m >= X^eps. Then #{1 <= n <= X : (n mod w_i) < w_i/2 for all i} = 2^{-m} X + O(m X^{1-eps}), with an absolute implied constant (independent of the w_i).

  **Proof.** Go downward from i = m. The set defined by the conditions for indices >= i is a disjoint union of runs of consecutive integers. A complete run has the form [c w_i, c w_i + ceil(w_i/2)), and every run except possibly the two at the ends of [1, X] is complete. Intersecting one complete run of length about w_{i+1}/2 with the w_i-periodic condition gives (w_{i+1}/(2 w_i) + O(1)) complete runs at level i, plus O(1) partial runs of length <= w_i. The integer count changes by a factor 1/2 up to an additive O(w_i) per parent run. There are O(X/w_{i+1}) parent runs, so level i adds O(X w_i/w_{i+1}) = O(X^{1-eps}). The top level contributes O(w_m) = O(X^{1-eps}). The number of runs at level i+1 is O(X/w_{i+1}), because the w_j grow geometrically with ratio >= X^eps >= 2. Replacing ceil(w/2) by w/2 costs O(X/w_i) = O(X^{1-eps}) per level, since w_i >= w_1 >= X^eps. Summing over the m levels gives the claim. QED.

  **Application.** For a retained prime p in band r, Kummer gives p ∤ B_n iff 2(n mod p^i) < p^i for all i >= 1.
  - The conditions for i <= r use the moduli p < p^2 < ... < p^r. The ratios are p > X^a > X^eps, and X/p^r > X^{r eps}.
  - The condition for i = r+1 is automatic for n <= X, because p^{r+1} > X^{1+(r+1)eps} > 2X once X^{(r+1)eps} > 2. The conditions for i > r+1 follow from the one for i = r+1.
  - For a pair (p, q) the merged moduli are p^i, q^j. Condition (5) is exactly the hypothesis of the lemma.

  So e_1, e_2 = O(L X^{-eps}) uniformly, which is even effective. This also removes any dependence on the unread lemma (1) of EGRS (I could not locate (1) on pp. 85–89; it is on an earlier page).
* **N2 (Provenance section, lines 838–845; coordinator text).** "Both asked for the same three repairs" is accurate for my report only if R3 is counted as optional. My report listed R1, R2 and R4 as required and R3 as optional, and all four are applied. Suggested wording: "three required repairs and one optional simplification". For my report, the sentence about rerunning both meshes byte-identically and an independent computation inside all four intervals is accurate. My empirical sanity check was at n of about 1e10 (mean about 11% below c_N(1/2)), which fits "9–12% below". I cannot confirm the other referee's or the verifier's statements and did not read them.

## Checked so far (independently re-derived)

1. **R1 → Lemma lem:alternating.** I checked: eq:successive by integrating out the last coordinate; the decreasing terms (J_{k+1} <= J_k/4); the Leibniz bracket A(1-A/2) <= c_N <= A < 1/4; that E_K(u) is increasing on [0, K+2); and the strict inequality A(1/2) < 1/4. Complete and correct.
2. **R2 → subsec:local, Lemma lem:local.**
   - Removed band-edge mass R_X = 2L eps/a + L E. Correct.
   - First-moment error m_X, including the shift p <= n <= X → 1 <= n <= X costing X^{b-1}. Correct.
   - Classes I and II are empty for s > 1/a. Correct.
   - Within one prime, consecutive powers have ratio p > X^eps, so failure of (5) between retained primes forces X^{-eps} <= p^u/q^v <= X^eps with u, v <= L. Correct; this is the ratio reading of the printed "p^u q^v".
   - The q-exponent interval has length 2eps/v, so the excluded-pair mass is <= L^2 H(2eps/a + E) + 2HR_X. Correct.
   - Diagonal 1/(X^a - 1). Correct.
   - Second-moment and variance expansion. I recomputed limsup V_X <= (4L + 2L^2 + 8L) log(b/a) eps/a = (12L + 2L^2) log(b/a) eps/a. Correct.
   - Endpoint shift for n in [X^{1-rho}, X]. Correct.
   - Logic of Chebyshev followed by eps → 0. Correct.

   Subject to N1, the proof is complete.
3. **Remark rem:printed6.** (10/9)(27/20)^2/(4/3) = 21870/14400 = 243/160, so the difference is log(243/160)/8 > 0. Correct.
4. **R3 → subsec:G.** I checked: pointwise f >= G_delta + S_{delta,1-rho}; bounded convergence in density implies convergence in mean; EGRS Theorem 2 (p. 86–87: lim (1/x) sum f(n) = c_0, matching eq:inputmean and c_0 = A(1)); then rho → 0 and Markov. Correct.
5. **R4 → scope.** I checked: the abstract (no claim for 1/2 < alpha < 1); the Introduction (lines 64–68); the title of Theorem thm:main ("for 0 < alpha <= 1/2"); Remark rem:scope; and the closing paragraph of sec:false (lines 639–643). Applied completely.
6. **Sieve section (subsec:sieve).**
   - Sandwich eq:sandwich. Correct.
   - Mass bound and tensor telescoping k C^{k-1} m zeta. Correct.
   - Slab bound (3/4) l A^{k-1}, since g <= 3/4 on (0, 1/2] (band r: (r+1)2^{-r} <= 3/4). Correct.
   - Floor error n^{-eps} e^C and the deep slab. Correct.
   - Diagonal binom(k,2) C^{k-2}/(n^delta - 1). Correct.
   - Assembly with the four eta/4 pieces and |c_{D,delta} - c_D| <= A(delta) e^{A} < 2A(delta). Correct.
7. **subsec:T.**
   - Legendre formula; carries; large-digit count with a_p = ceil(p/2), b_p = floor(p/2). Correct.
   - Block bound: blocks may be taken to start at 1, so ceil(X/p^h) blocks. Correct.
   - 2(V+1)h^V(a_p/p)^h → 0 (including p = 2). Correct.
   - Tail <= 1/H and the finite part <= H 2^{-V-2}. Correct.
8. **sec:false.** v_2 = 1 from the single nonzero Legendre term i = h+1; floor(y/4)/y >= 1/4 - 1/y; uniqueness of density limits; and the D_alpha consequence. Correct.
9. **Numerics, new mathematics in subsec:errors.**
   - z <= 1/5. Correct.
   - eta_Q <= 2(M+R)/Q: the refinement has <= M+R pieces, and ceil - floor < 2 + 2^{-20}, so the integer width is <= 2. Correct.
   - Slab (3/2) h e^{A_s} < 3h. Correct.
   - Rounding sum (m_+^k - m_-^k)/k! <= eta_Q e^{m_+} < 3 eta_Q for m_+ <= 1. Correct.
   - Width bound eq:width. Correct.
   - The continuity modulus 0 <= J_k(beta) - J_k(alpha) <= 3(beta-alpha)A(beta)^{k-1}/(4k!), summing to (3/4)e^{1/4}(beta-alpha) < 2(beta-alpha). Correct; the slab of width beta-alpha has density <= 3/4 on (0, 1/2].
   - The table matches my first-round rerun of mesh 16384 (all 16 endpoints), and the mesh-4096 interval matches.
   - Minor: line 650 says the construction works for any rational alpha, but the program implements only alpha = 1/s. Suggest adding "the supplied program implements alpha = 1/s".
10. **Related work.** It makes no mathematical claim about this note beyond what is proved. It says Theorem 4 concerns a different quantity from the cited index-density results, which is accurate as a description of this note. I did not check the literature claims themselves; novelty is checked separately.

## Not yet checked / could not check

* Application check for the lemma's hypothesis w_1 >= X^eps: w_1 = min(p,q) > X^a > X^eps, since eps < a/4.
* `main.pdf` was only spot-checked by text extraction: 15 pages, and seven key strings from `main.tex` are present ("uniformly", "Corrected Theorem 4", "three repairs", "0.160401041573", "log(243/160)", "ratio intended", "Nothing is claimed"). I did not check full equality with `main.tex`.
* Endpoint example re-evaluated at 30 digits: the two values are 0.0359603 and 0.0881962, and 8 times their difference is 0.4178876 = log(243/160).
* The files under `code/` (not in my permitted read list for this round). I did not confirm they are byte-identical to the first-round programs.
* EGRS lemma (1), which is not on pp. 85–89. Repair N1 makes it unnecessary.
