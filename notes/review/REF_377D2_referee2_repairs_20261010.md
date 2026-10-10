PASS-WITH-REPAIRS

Session lineage: resumed referee-2 session of AUT-101; my earlier report was REF_377D2_referee2_20261010.md. I read only the revision files named in the follow-up and EGRS pp. 85–90; I did not read the other referee's reports.

# REF #377-D2 — repair confirmation (referee-2)

**Object.** I reviewed `publish/automath-papers/erdos377/main.tex`, together with the author's `REVISION_REPORT.md` and the EGRS page images pp. 85–90. Line numbers refer to `main.tex`.

**Summary.**
- **My three repairs.** R1, R2 and R3 are applied correctly and completely.
- **The new mathematics.** It is correct: the LOCAL proof, the sieve/measure passage, the T and G sections, the η_Q width bound, and the continuity modulus.
- **Repairs still needed (all textual, none mathematical).**
  - The revision attributes the word "uniformly" to two EGRS displays that do not print it (S1).
  - Two sentences in the coordinator's provenance paragraph do not describe my review accurately (S2, S3).
  - Neither changes any result.
- **Scope.** No statement exceeds what is proved, in quantifiers, scope or effectiveness.

## 1. My earlier repairs

**R1 — applied.**
- Lemma lem:alternating (l. 178–213) proves (k+1)!J_{k+1} ≤ k!J_k·A by integrating out the last coordinate (eq:successive, l. 193–197).
- It then deduces that the terms decrease and gives the bracket J_1−J_2 ≤ c_N ≤ J_1.
- With J_2 ≤ A²/2 this yields A(1−A/2) ≤ c_N ≤ A < 1/4 (eq:bracket, l. 143).
- I re-derived each step. At α = 1/2 the bracket is 0.148258 ≤ c_N ≤ 0.161260, which contains the certified interval [0.160401041573, 0.160401748642].
- The geometric tail and the monotonicity of E_K(u) in u (l. 206–212) are correct.

**R2 — applied, with one attribution defect (S1 below).**
- Section subsec:local (l. 239–311) and Lemma lem:local (l. 313–418) now give exactly the three-step argument I asked for: termwise first moment, termwise second moment with the excluded pairs, and Chebyshev, followed by the endpoint shift from n to X.
- l. 278–280 explicitly declines to infer sub-sum concentration from the full second moment, and declines to use printed (6).
- The ratio reading is eq:ratio (l. 358–364).
- The endpoint example is Remark rem:printed6 (l. 420–434). I checked it at 30 digits: printed (6) gives 0.0359603, the true value is 0.0881962, and 8×(difference) = log(243/160) = 0.41788762810672… (exact match).

**R3 — applied.**
- The scope appears in the abstract (l. 41), the introduction (l. 64–68), thm:main ("for 0<α≤1/2"), Remark rem:scope (l. 168–176) and the end of sec:false (l. 641–643).
- The bracket and §sec:false use only s ≥ 2.

## 2. The localized moment proof, checked as a proof

**Imported statements against the page images.**
- **eq:input1 (l. 250–256).**
  - p. 86 prints, after (4): "for each p with x^{1/(r+1)+ε} < p < x^{1/r−ε}, A(p;x) = x/2^r + o(x)".
  - A(p;x) is defined on p. 86 as |{k : p ≤ k < x, p ∤ C(2k,k)}|.
  - The band and the count match, and the strict/non-strict endpoint change costs ≤ 1/X, as stated in l. 247–249.
- **eq:input2 (l. 257–269).**
  - p. 88 prints: "if we now assume (5) w_{k+1}/w_k > x^ε, k = 1,…,r+t−1, x/w_{r+t} > x^ε, then we see by (1) that A(p,q;x) = x/2^{r+t} + o(x)".
  - A(p,q;x) is defined on p. 87 as |{k : p,q ≤ k ≤ x, (C(2k,k), pq) = 1}|.
  - The conditions and the main term match.
- **eq:inputmean (l. 270–277).** This matches Theorem 2 (p. 86) and the value of c_0 on p. 87.
- **The excluded-pair condition.** p. 88 prints "x^{−ε} ≤ p^u q^v ≤ x^ε for some 1 ≤ u ≤ r, 1 ≤ v ≤ t". The paper reads it as a ratio and says so (l. 362–364). That reading is correct.

**S1 (REPAIRABLE, attribution; l. 253–256, 262–269, 289–291).**
- **The defect.** Neither display prints "uniformly". p. 86 says "for each p", and p. 88 says "for … (5) … then … + o(x)". Uniformity in p and in (p,q) is implicit, because EGRS sum these o(x) over p on p. 87 and over (p,q) on p. 88. Yet the text says the display *is* the uniform statement ("uniformly for …", and "The imported assertions say e_i → 0").
- **Statement (1).** Statement (1), which p. 88 invokes, is on a page outside the images I was given. I could not see whether it is printed in uniform form.
- **The uniform statements are true.**
  - **eq:input1 (one line).** Use complete blocks of p^r consecutive n: each contains exactly ⌈p/2⌉^r good residues. The top digit is automatically < p/2 because p^{r+1} > X^{1+(r+1)ε}. This gives A_1/X = 2^{−r}(1+O(1/p))^r + O(X^{−rε}), uniformly.
  - **eq:input2 (nested intervals).** The pair conditions are exactly n mod w_l < c_l·w_l, with c_l = ⌈p/2⌉/p or ⌈q/2⌉/q; this is exact for every n ≤ X, since digit_{i−1} < ⌈p/2⌉ ⟺ n mod p^i < ⌈p/2⌉p^{i−1}. On each good interval of length c_l·w_l ≥ w_{l−1}X^ε/2, count the finer conditions, and induct downward from l = r+t. This gives X·Πc_l·(1 + O((r+t)X^{−ε})), uniformly under (5) and within the trimmed bands.
  - So nothing in the argument is false.
- **Repair (either option).**
  - (a) Change "uniformly for" and "The imported assertions say" to "in the uniform form in which they are used in the summations on pp. 87–88 (uniformity is not printed in the displays)".
  - (b) Better: add the proof of eq:input1 above (3 lines) and the nested-interval proof of eq:input2 (about 8 lines). This makes Lemma lem:local independent of the unseen (1).

**Every other step of lem:local — checked, all correct.**
- **Removal.** L = ⌈2/a⌉ is at least 1/a + 1, so every band boundary in [a,b] is some 1/j with j ≤ L. The removed set has total length ≤ 2Lε, its reciprocal mass is ≤ 2Lε/a + LE, and its g-mass is ≤ 2Lε/a.
- **Retained pieces.** There are ≤ L of them, so the band-sum error is ≤ LE.
- **m_X.** I checked it term by term: e_1H + X^{b−1}H + LE + (LE + 4Lε/a).
- **Excluded pairs.**
  - Classes I and II are empty because s > 1/a.
  - In a trimmed band, p^r < X^{1−rε} gives X/w_{r+t} > X^ε.
  - The same-prime ratio is p > X^a > X^ε, since ε < a/4.
  - So a failure of (5) forces eq:ratio.
  - For fixed (p,u,v), the exponent window for q has length ≤ 2ε/v. Hence the bound 2HR_X + L²H(2ε/a + E).
- **Second moment.**
  - The diagonal term is ≤ 1/(X^a − 1).
  - The variance bound V_X follows from −2λE S ≤ −2λ² + 2λm_X.
  - limsup V_X ≤ (4L + 2L² + 8L)·log(b/a)·ε/a = (12L + 2L²)·log(b/a)·ε/a, which matches l. 396.
- **Endpoint shift.** The symmetric difference lies in (X^{a(1−ρ)}, X^a] ∪ (X^{b(1−ρ)}, X^b], and E_X decreases in its argument. This gives eq:endpointshift. The density bound is X^{−ρ} + P(|S^X − λ| > η/2).
- **eq:MX.** This uses both Rosser–Schoenfeld bounds: the upper one needs X^u ≥ 286, hence X ≥ 286^{1/a}. A prime exactly at an endpoint costs ≤ X^{−a} each.

## 3. Mathematics not in the record I reviewed

- **Sieve and measure passage (l. 436–521).**
  - eq:massbound and the choice of C are correct.
  - The tensor-telescoping error kC^{k−1}mζ is correct.
  - g ≤ (r+1)2^{−r} ≤ 3/4 on (0,1/2].
  - The slab bound (3/4)ℓA^{k−1} is correct (integrate the last coordinate).
  - Inner and outer box unions differ inside a slab of width ≤ 2kh.
  - The floor error is n^{−ε}e^C.
  - The near-boundary products have limit ≤ (3/4)εΣA^{k−1}/k!.
  - The diagonal is C(k,2)C^{k−2}/(n^δ − 1).
  - No independence is assumed beyond LOCAL. Correct.
- **T(n) (l. 523–561).**
  - Legendre's formula: each summand is 0 or 1, and each large digit forces a carry.
  - Q_{p,V}(h_p) counts the residues correctly, and ⌈X/p^h⌉ ≤ 2X/p^h.
  - The bound 2(V+1)h^V(a_p/p)^h → 0 holds, including at p = 2.
  - The tail is ≤ 1/H, and the finite part is ≤ H·2^{−V−2} when every v_p > V.
  - Correct.
- **Small primes, subsec:G (l. 563–586).**
  - f ≥ G_δ + S_{δ,1−ρ} holds pointwise, since the ranges are disjoint and lie in [1,n].
  - A bounded sequence that converges in density converges in mean, and S is bounded by eq:RS.
  - Theorem 2 then gives limsup E G_δ ≤ c_0 − ∫_δ^{1−ρ} g, which tends to A(δ) as ρ → 0.
  - Markov's inequality finishes the bound.
  - This is cleaner than the record's L²/uniform-integrability route, and correct.
- **δ-removal (l. 588–600).** 0 ≤ J_k − J_k^{(δ)} ≤ A(δ)A^{k−1}/(k−1)!, so the total change is ≤ A(δ)e^A < 2A(δ). The η/4 assembly (l. 601–616) checks out: the lower side gives c_N − η/2 and the upper side c_N + η.
- **sec:false (l. 618–643).** For n = 2^h only the term i = h+1 of Legendre's formula is nonzero, and it equals 1 (checked for every i). The lower bound ⌊y/4⌋/y ≥ 1/4 − 1/y holds, including h = 0. The uniqueness of a density limit is argued correctly.
- **η_Q bound (l. 735–743).**
  - The common refinement has ≤ M + R pieces.
  - Each scaled log enclosure is narrower than 2^{−20}, so the rounded integer width is ≤ 2.
  - Numerically, Q·η_Q equals the number of segments at every s ∈ {2,3,4,5} and M ∈ {4096, 16384} (e.g. 15929 ≤ 32896 at s = 2, M = 16384). So the bound holds with room to spare.
- **Width formula eq:width.**
  - The slab between the inner and outer sums has Σt ∈ ((M+1−k)h, (M+k)h], width (2k−1)h ≤ 2kh, which gives the term (3/2)h·e^{A_s} < 3h.
  - The rounding term is ≤ η_Q·e^{m_+} < 3η_Q when A_s + η_Q ≤ 1.
  - Adding twice the radius gives 3h + 3η_Q + 4τ_R + 2E_K. Correct.
  - This bound is a convergence guarantee only; the table rests on the computed bounds.
- **Continuity modulus (l. 770–782).**
  - J_k(β) − J_k(α) is the slab mass {α < Σt ≤ β} divided by k!, which is ≤ (3/4)(β−α)A^{k−1}/k!.
  - Summing gives ≤ (3/4)e^{1/4}(β−α) ≈ 0.963(β−α) < 2(β−α).
  - Correct for 0 < α ≤ β ≤ 1/2.
- **Remark rem:scope and l. 650–651.** The claim "works for any rational α by clipping the top band" is true of the construction. The shipped program supports only α = 1/s (`--s` takes integers). Suggested wording: "the program as shipped handles α = 1/s; the construction extends …". This is cosmetic.
- **Table (l. 788–805).** All 16 endpoints are identical to density_16384.txt, and 2830047 > 4·707069. The SHA-256 hashes of code/{density_intervals.py, density_4096.txt, density_16384.txt, check_convolution.py} equal those of the originals I reran byte-identically in my first review.
- **Statements versus proofs.** thm:main, prop:nolimit and rem:scope claim exactly what is proved:
  - for each fixed α ∈ (0,1/2] and each η: natural density and Cesàro convergence;
  - the explicit series with an explicit truncation error;
  - no limit along all integers;
  - no effective threshold in n, and nothing for 1/2 < α < 1.
  
  The abstract matches.

## 4. Related work and Provenance (coordinator text)

- **Related work (l. 70–95).** It makes no mathematical claim beyond the paper; its claims are about the literature and the search, which were not checked, as instructed. "This note does not address" Problem 377 is accurate.
- **Provenance (l. 833–851).**
  - **S2 (REPAIRABLE, l. 839).** "Both asked for the same three repairs." My report asked for exactly these three. But the author's own repair map in REVISION_REPORT.md lists four items from referee 1, including an optional simplification of the small-prime argument applied in subsec:G. Suggested wording: "Both asked for these three repairs (referee 1 also suggested an optional simplification, applied in subsec:G, §4.5)".
  - **S3 (REPAIRABLE, l. 848–849).** "Empirical proportions at n≈10^9–10^12 lie 9–12% below the limits" does not describe my numbers.
    - At n ∈ [10^11, 10^12] I measured mean N = 0.1392 against 0.1604 at α = 1/2 (13.2% below) and 0.0530 against 0.0599 at α = 1/3 (11.4% below).
    - At larger n (10^14–10^24, α = 1/3 and 1/4) I measured 11.5–17.3% below.
    - Suggested wording: "roughly 9–17% below the limits, depending on α and on the range of n".
  - **"Computed the four constants by an independent method; all values fell inside."** For me this holds for the converged values; my coarsest Volterra grid at α = 1/5 was just outside. Suggest "the converged values".
  - **Not checkable by me.** The verifier's check of v_2 for h ≤ 300 is not part of my review.
  - **Otherwise accurate.** The rest of the paragraph describes my review accurately: PASS-WITH-REPAIRS, no fatal gap, byte-identical reruns at both meshes, and an independent method.

## Tests run in this session

- SHA-256 comparison of the four code/data copies against the originals: identical.
- η_Q and segment counts for s = 2..5 and M ∈ {4096, 16384}: all within 2(M+R).
- Endpoint example at 30 digits: 8×(difference) = log(243/160) exactly as stated.
- eq:bracket at α = 1/2: 0.148258 ≤ [0.1604010, 0.1604018] ≤ 0.161260.
- Reused from my first review rather than repeated: the reruns at both meshes, the convolution check, the bin checks against mpmath, and the independent Volterra solve.

## Could not check

- EGRS statement (1), on a page before p. 85, which was not supplied. See S1: the needed uniform forms are re-derived above, independently of (1).
- Whether main.pdf matches main.tex. No PDF tools are available here; I reviewed the TeX source.
- The other referee's report and the verifier's run.
