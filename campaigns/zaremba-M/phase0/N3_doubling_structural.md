# N3: is the exponential loss structural? (Zaremba campaign, Phase 0)

Written 2026-09-26. Scratch scripts: `profile.py` and `n3_numbers.py`. Their full text and output are in §5 and in Appendix A, so this file does not depend on the scratchpad.

## 0. Answer in one paragraph

The factor 2^{-k}, with k ≈ 1/c, is **structural for the method** and **not intrinsic to the problem**.

- **Structural for the method (proved below, Lemmas A and B).** Every MMS/Shkredov-shape argument has two stages.
  - It certifies an ℓ²-flattening profile of the walk measure on SL2(F_p), and the gain per self-convolution doubling is at most g.
  - It converts that profile into a spectral bound with the Plancherel/Frobenius (quasirandomness) step.
  - For such an argument the best exponent obtainable is Θ(g·2^{-(2-h0)/g})/L0. Here h0 is the entropy that the girth stage certifies (in log_p units), and "2" = log_p(|G|/d_min) is the quasirandomness offset.
  - Shkredov's δ = c/2^{k+4} with k = ⌈1/c⌉+1 has exactly the shape of this optimum, with the identification 1/c ↔ (2-h0)/g.
  - Consequence: no re-bookkeeping of the iteration can recover more than O(1) bits of log2 M (about 3–5 bits under my identification). All real savings must come from the gain per doubling, c.
- **Not intrinsic to the problem (refuted numerically and by Lemma A).** For the actual Lemma-14 walk the ℓ² entropy grows **linearly in the walk length**, with slope 2·log_p(N/(2√(N−1))), up to at least h = 5 (p = 100003) and h = 2.7 (p = 1000003). Lemma A says linear growth is equivalent to a spectral gap. The method only certifies growth that is **logarithmic in the length** (a constant gain per doubling). The whole loss is that gap.
- **Few-step answer.** A single application of an energy bound cannot work: one Frobenius step needs certified h > 2, which is far above what the girth stage certifies. A few steps can work if each doubling gains Ω(1).
  - An ideal (tempered) doubling needs only 4–5 doublings from h0 ∈ [0.1, 0.2].
  - The needed per-doubling gain is c ≥ 1/470 for log2 M ≤ 500, c ≥ 1/122 for log2 M ≤ 150, and c ≳ 1/15 for log2 M ≲ 40 (Shkredov normalisation, §7).
  - "Avoid iterating" is the wrong goal. The goal is "make each iteration gain a constant".

## 1. Sources

Read (PDF text extracted myself):
- Shkredov arXiv:2603.14116v2: Lemmas 14, 15, Corollary 16 (pp. 9–10); §5.1–5.4 eqs (130)–(157) (pp. 31–37); Appendix eqs (158)–(159), Thm 38, Thm 39, Lemma 40 (pp. 38–39).
- Moshchevitin–Murphy–Shkredov (MMS) arXiv:2212.14646: Lemma 4 and its sketch, eqs (14)–(19) (pp. 5–6); eq (22)–(24) (p. 7).
- MMS arXiv:1808.05845 ("Popular products and continued fractions", arXiv numbering): Thm 9 and its proof eqs (48)–(55) (pp. 21–22); Thm 15 (ℓ²-flattening) and its proof eqs (30)–(45) (pp. 17–20); Cor 21 / Prop 20 (Frobenius); Thm 19 (Helfgott, δ = 1/3024 quoted from Kowalski IMRN 2013); Cor 23. The published Israel J. version is cited in 2212.14646 as "[30, Lemma 12/13, Prop 5/7]". Those numbers do not match the arXiv numbering I read, so I cite by arXiv number.
- Shkredov arXiv:2111.05751 (girth-free BG): Thm 7, Thm 9, eqs (15)–(18) (pp. 6–8), where ζ = 1/2^{t+2}, t ≪ log p/log K and the final saving is N^{-exp(-Ω(1/δ))}.
- Zhang arXiv:2605.02518: pp. 1–3 only (Thm 2.1 triple product, Thm 2.4 ℓ²-flattening; Remark 1.3 says the effective M is large). Zhang's route has the same flattening structure; I did not read his iteration count.
- Rudnev–Shkredov arXiv:1812.01671: grep only (Thm 2, exponent 1/20; footnote 1/15, 1/12). Not re-derived.

**Unread:**
- Shkredov, Uspekhi 2021 survey (Russian Math. Surveys 76:6, 1065; mathnet rm10029). Mathnet full text was not reachable from the container: the getFT link returns a "document not available" page. It is not in Shkredov's arXiv atom feed (grep of titles). Theorem 49 / Corollary 50, the exact source of "δ = c/2^{k+4}, k = ⌈1/c⌉+1" and of the min{…} defining c, is therefore **unread**. My normalisation match in §3 is an inference from the formula's shape.
- Helfgott 2008, Bourgain–Gamburd 2008, Kowalski 2013, Murphy 1907.13569 (BSG): unread directly. I used them only as quoted in MMS/Shkredov.
- Web search was unavailable (session budget exhausted). Sources came by direct arXiv PDF download.

## 2. Where exactly the exponential enters (traced)

Chain for prime q = p (Shkredov Appendix + MMS 2212.14646 sketch + MMS 1808.05845 Thm 9 proof):

1. **Girth stage (linear, lossless up to constants).**
   - G = {v^j u^{-j} : j ≤ N}. Its Cayley graph has girth ≥ τ log_N p (τ = 1/5 in MMS 2212.14646 p. 5; τ = 1/4 in Shkredov eq. (159) area; see N2 for the discrepancy).
   - For m = τ/4·log_N p the walk r_{G,2m} has coset non-concentration K = p^{τ/6} (MMS 2212 eq. (17)).
   - The Hölder step (MMS 2212 eq. (18)) costs the 1/(2l) root with l ≈ m. That is a **length-proportional** conversion, and since p^{1/m} = N^{4/τ} it only produces the harmless factors τ and 1/6 in κ = δ/6.
2. **Flattening stage (the source of 2^{-k}).**
   - MMS 1808 Thm 15: ‖μ^{(2^k)}‖²₂ − 1/|G| ≤ C*^k K^{-c* k}. The gain per **doubling** is the fixed factor K^{-c*}, set by the non-concentration level K of the **initial** measure.
   - The proof of Thm 9 applies Cauchy–Schwarz k+1 times: σ*^{2^{k+1}} ≤ |Y|^{2^{k+1}−1}·⟨f_Y, η^{(2^k)} * f_Y⟩ (eq. (49)).
   - It then applies the Frobenius bound ‖μ*f‖₂ ≤ p‖μ‖₂‖f‖₂ (Cor 21) with ‖η^{(2^k)}‖₂ ≲ p^{-3/2} (eqs. (50)–(52)). This gives the saving p^{-1/2} **before** the 2^{k+1}-th root, i.e. δ = 2^{-(k+2)} with k = 3 log p/(c* log K) (eqs. (53)–(55)).
   - Shkredov 2111.05751 eq. (17)–(18) is the same computation: ζ = 1/2^{t+2}, final N^{-exp(-Ω(1/δ))}.
3. **Shkredov's explicit form** (Appendix p. 38–39): log N·κ = (6m)^{-1}τδ log p = δ log N/6; δ = c/2^{k+4}, k = ⌈1/c⌉+1; c ≥ min{1/3, 1/(8C2), τ/(4C2), 0.5c_H/(C1+C2)} = 1/1640 with C1 = 9, C2 = 32, c_H = 1/20.
   - Shkredov states κ ≥ 2^{-1656}. My arithmetic, δ/6 = 2^{-(1645 + log2 1640 + log2 6)}, gives log2(1/κ) = 1658.26, matching DESIGN's inconsistency (a), which N2 owns.

So the exponential enters at one place only: **the number of doublings needed to push the ℓ² norm to the quasirandom threshold, times the root extraction that turns a length-2^k statement into a length-1 statement.** The girth stage and the final Hölder step are polynomial. BSG and Helfgott do not create the exponential. They set the size of the per-doubling gain c, and the exponential then turns small c into 2^{-1/c}.

## 3. Two lemmas that make "structural for the method" precise

Notation: G = SL2(F_p), |G| = p³ − p. d = (p−1)/2 is the minimal dimension of a nontrivial irreducible representation (Frobenius). μ is a symmetric probability measure on G, and λ = λ(μ) = max_{ρ≠1} ‖μ̂(ρ)‖_op. For the P¹ action, the permutation representation is 1 ⊕ (dimension-p part), so the Zaremba operator satisfies ‖T₀‖ ≤ λ. Define the **excess entropy** h(L) := −log_p(‖μ^{(L)}‖²₂ − 1/|G|), and θ := log_p(1/λ).

**Lemma A (two-sided ℓ²/spectral sandwich).** For every L ≥ 1,
  (h(L) − log_p(|G|/d)) / (2L) ≤ θ ≤ h(L)/(2L), with log_p(|G|/d) = 2 + o(1).

*Proof.* Plancherel gives ‖μ^{(L)}‖²₂ = |G|^{-1} Σ_ρ d_ρ ‖μ̂(ρ)^L‖²_HS. Since μ is symmetric, μ̂(ρ) is self-adjoint, so ‖μ̂(ρ)^L‖_op = ‖μ̂(ρ)‖_op^L.
- Lower bound on the excess: the ρ attaining λ contributes d_ρ‖μ̂(ρ)^L‖²_HS ≥ d·λ^{2L}, so ‖μ^{(L)}‖²₂ − 1/|G| ≥ d λ^{2L}/|G|, i.e. λ^{2L} ≤ (|G|/d)·p^{−h(L)}.
- Upper bound on the excess: ‖μ̂(ρ)^L‖²_HS ≤ d_ρ λ^{2L} and Σ_ρ d_ρ² = |G|, so the excess is ≤ λ^{2L}, i.e. λ^{2L} ≥ p^{−h(L)}. ∎

So the conversion "ℓ² profile → spectral gap" loses **only the additive offset 2** in h. Anything the method loses beyond that is in how it bounds h(L) from below. It also follows that the true profile of any expander is linear: 2θL ≤ h(L) ≤ 2θL + 2 + o(1).

**Lemma B (optimum of the doubling scheme).** Suppose the only certified information is h(2^j L0) ≥ h0 + j·g for j ≥ 0, with h0 < 2, together with the monotonicity of ‖μ^{(L)}‖₂ in L (Young). Then the best bound Lemma A yields is
  θ* = max_L (h_cert(L) − 2)/(2L) = (h0 − 2 + j*g)/(2^{j*+1}L0), where j* = ⌈(2−h0)/g⌉ + 1,
and θ* ∈ [g, 2g)/(2^{j*+1}L0). Hence log2(1/(θ* L0)) = (2−h0)/g + log2(1/g) + O(1).

*Proof.*
- h_cert is constant on [2^j L0, 2^{j+1}L0), so the maximum is attained at dyadic L.
- Put a_j = h0 − 2 + jg and f(j) = a_j/(2^{j+1}L0). Then f(j+1)/f(j) = (a_j + g)/(2a_j), which is ≥ 1 iff a_j ≤ g.
- So f increases until the first j with a_j ≥ g and decreases after it. At that j, a_j ∈ [g, 2g). ∎

Checked numerically (`n3_numbers.py`, Appendix A): for (h0, g) = (0.1, 1/1640), (0.1, 1/512), (0, 1/1640), (0.1, 1/40), (0.1, 1/20) the brute-force argmax equals ⌈(2−h0)/g⌉+1 in all five cases.

**Match with Shkredov.**
- Lemma B gives (numerator ∝ g) / 2^{(number of doublings)+1} with number of doublings = ⌈(2−h0)/g⌉ + 1.
- Shkredov gives c/2^{k+4} with k = ⌈1/c⌉ + 1.
- These agree in form under 1/c ↔ (2−h0)/g (c = the per-doubling gain normalised by the distance to saturation). The extra 2^{-3} and the /6 are constant factors.
- **Inference, not verified against the unread Theorem 49:** Shkredov's bookkeeping sits within about 3–5 bits of the scheme's optimum. Re-optimising the iteration (stopping time, root extraction, Hölder order) cannot move log2 M by more than O(1) bits.

**What Lemma B does and does not prove.**
- It proves that any argument whose inputs are (i) a certified doubling profile with gain ≤ g and (ii) the ℓ²→spectral conversion is limited to log2(1/κ) ≥ (2−h0)/g − O(log(1/g)). Lemma A shows (ii) is essentially lossless, so no smarter final step rescues a small g.
- It does **not** construct a non-concentrated measure on SL2(F_p) whose true profile is logarithmic (which would show the flattening constants are sharp). I know of no such family, and the Zaremba walk is not one of them (§5).
- DESIGN's requested form "κ ≤ C/(2^j m)" holds for MMS-shape arguments with j = number of doublings ≈ (2−h0)/g: κ·log N ≈ θ log p, with L0 ≍ m.

## 4. Why the per-doubling gain is bounded, and why the obvious fix is circular

The per-doubling gain in MMS 1808 Thm 15 is K^{c*}. The proof (eqs. (39)–(45)) reaches a contradiction in two cases:
- growth |S|^{1+ε} ≪ M^C|S| (the Helfgott/product-theorem branch, controlled by c_H and the BSG exponents);
- concentration µ^{(ℓ)}(gΓ) ≫ M^{−C−3}, which contradicts the **inherited** bound µ^{(ℓ)}(gΓ) ≤ K^{-1}.

The second branch caps the gain M at K^{1/(C+3)} **for every ℓ**, because the proof never improves the coset bound along the walk. In Shkredov's min{…} this is the term τ/(4C2) (K = p^{τ/6}). With τ = 1/4 it equals 1/512; with τ = 1/5 it equals 1/640. The binding term is 0.5·c_H/(C1+C2) = 1/1640 (product theorem divided by the BSG exponents).

**Lemma C (Borel-coset control from ℓ² needs h > 2).** Let B be the Borel subgroup and x₀ ∈ P¹. For any measure ν on G, Σ_{y∈P¹} ν({g : g x₀ = y})² ≤ |B|·‖ν‖²₂, and |B| = p(p−1).

*Proof.* {g : g x₀ = y} is a left coset of Stab(x₀) ≅ B. Apply Cauchy–Schwarz on each coset and sum. ∎

So the group ℓ² bound controls Borel-coset masses of µ^{(L)} only once h(L) > 2 + (target). In the range h < 2 where the doublings happen, the Borel-coset masses of µ^{(L)} are exactly the time-L distribution of the P¹ walk, which is the object whose decay we are trying to prove. Upgrading the frozen K along the walk is therefore not free: for Borel cosets it is essentially the Zaremba statement itself. (Dihedral and exceptional cosets are not analysed here.)

## 5. The truth is linear (numerics; refutes "intrinsic to the problem")

**Observation.** Each g_j(x) = 1/(x+2j) − 2j is an **involution**. Its matrix [[−2j, 1−4j²],[1, 2j]] squares to I; the script asserts y[y] = id for every j in every run. So T = (1/N)Σ P_{g_j} is self-adjoint, and the relevant tree is the N-regular Cayley tree of the free product (Z/2)^{*N}. Its Kesten spectral radius is 2√(N−1)/N. This, not a free-group value, is the comparator that the campaign numerics match (note for N8; I did not edit its files).

`profile.py`: h_P1(L) := −log_p‖T^L δ_∞ − u‖²₂ on P¹(F_p). Its per-step increment tends to the constant 2·log_p(N/(2√(N−1))):

| p | N | Kesten slope 2log_p(1/r) | h at L=1,2,4,8,12 | increment at the last step |
|---|---|---|---|---|
| 100003 | 16 | 0.1260 | 0.241, 0.424, 0.747, 1.333, 1.890 (L=36: 5.069) | 0.1301 (L=36) |
| 1000003 | 64 | 0.2018 | 0.301, 0.553, 1.016, 1.891, 2.740 | 0.2108 (L=12) |
| 100003 | 4 | 0.0250 | L=1: 0.120; L=25: 1.013; L=55: 1.853 | 0.0271 (L=55) |

Growth is linear in L from the first step onward. For N = 64, the gain from L=4 to L=8 is 0.875 in log_p units **per doubling**, against the method's certified gain of order 1/1640. Empirical κ_true = −log r/log N = 0.104 (N=4), 0.262 (16), 0.335 (64), 0.375 (256), tending to 1/2. On P¹ there is no offset: ‖T^L δ − u‖²₂ ≤ ‖T₀‖^{2L}. The offset 2 in Lemma A exists only because the flattening machinery must run on the group.

## 6. Anatomy: the exponent is (offset − girth entropy)/gain

log2(1/κ_method) ≈ (2 − h0)/g + log2(1/g) + O(1), where:
- **2** = log_p(|G|/d_min): the price of converting ℓ² on SL2(F_p) into a spectral bound (Lemma A). It is intrinsic to group-side arguments.
- **h0** = the girth-stage entropy, ≈ (girth/2)·log_p(N/(2√(N−1))), about τ/2 or less (τ = 1/4 or 1/5). This is linear and lossless.
- **g** = the per-doubling flattening gain (Shkredov's c ≈ 1/1640). This is where BSG (C1+C2 = 41), the Helfgott/Rudnev–Shkredov exponent (c_H = 1/20) and the frozen coset cap (τ/(4C2)) all enter.

The exponential in 1/c is the conversion of a **small constant gain per doubling** into a length 2^{(2−h0)/g}. That is how the method turns "logarithmic entropy growth" into a spectral gap.

## 7. Few-step arguments: what would and would not work

(a) **One application of any energy bound on the group: impossible.**
- The single Frobenius step needs certified h > 2 at the input (Lemma A), and the girth stage certifies h0 ≈ 0.1.
- A pure-girth route would need tree-likeness up to 2L with 2L·log_p(N/(2√(N−1))) > 2, i.e. girth ≳ 4 log_N p for large N. The Moore-type ceiling ((N−1)^{girth/2} ≲ p³) is ≈ 6 log_N p. The proven value is τ = 1/5–1/4.
- A counting heuristic (pairs of length-L words, collision probability ≈ p^{-3}) suggests girth ≈ 3 log_N p for this family. That is below 4, so even the true girth would probably not suffice. This is heuristic only and not a proposed route.

(b) **A few doublings suffice if each gains a constant.**
- The raw entropy h_raw(L) := −log_p‖µ^{(L)}‖²₂ satisfies h_raw(2L) ≤ 2h_raw(L), since ‖µ*µ‖²₂ ≥ (µ*µ(e))² = ‖µ‖⁴₂ for symmetric µ. So one doubling at most doubles the entropy, and the excess h and h_raw agree while h < 3 − o(1).
- With ideal doubling, ⌈log2(2/h0)⌉ = 5 doublings (h0 = 0.1) or 4 doublings (h0 = 0.125 or 0.2) are enough.
- So iteration costs only 2^{O(log(1/h0))}, which is polynomial. The damage comes only from a small g.

(c) **Gain thresholds.** Under Shkredov's own chain, log2 M(c) = ⌈1/c⌉ + 5 + log2(6/c) + log2(10·18·40). The last term, 12.81 bits, is my overhead choice: (157) with ε < 1/18 and M* ≥ 40M. This gives 1671.1 at c = 1/1640, close to DESIGN's "~1680"; the other overhead terms belong to N1/R1.
- log2 M ≤ 500 needs 1/c ≤ 470.
- log2 M ≤ 150 needs 1/c ≤ 122.
- log2 M ≲ 40 needs 1/c ≈ 15.
- In Lemma-B units (g, log_p of the squared norm): g = 1/40 gives log2(1/(θL0)) = 83.3 and g = 1/20 gives 44.3, both at h0 = 0.1.

(d) **Power-type ("multiplicative") flattening, h(2L) ≥ (1+β)h(L).**
- This gives log2(1/(θL0)) ≈ log2(2/h0)/log2(1+β): 61.4 for β = 1/20 and 121.3 for β = 1/40 (brute force 66.6 and 127.6, h0 = 0.1).
- But β = 1/1640 gives 4914 bits, worse than additive. The additive/multiplicative distinction does not matter by itself. What matters is the size of the gain and whether it is capped by the frozen K (§4).

(e) **Asymmetric flattening (convolve with a fixed ν of small entropy).** This would give linear profiles. But "‖ν*f‖₂ ≤ p^{−c}‖f‖₂ for all mean-zero f" is by definition λ(ν) ≤ p^{−c}, which is circular. BG avoids the circularity only by applying structure theory (BSG + product theorem) to self-convolutions of comparable measures. DESIGN says Murphy's asymmetric group-action BSG carries its own 2^{2J} loss; I did not read it.

(f) **Arguments with no doubling at all** are exactly the non-growth routes in DESIGN:
- R3: a one-shot bilinear/incidence bound at fixed N. Its barrier is the square-root/completion barrier, not 2^{1/c}.
- R4: an automorphic spectral gap. That is polynomial by nature; its obstruction is thinness.

N3 does not rank those routes. It shows only that they are the only ones not subject to Lemma B.

## 8. Consequences for the campaign

1. **Iteration re-bookkeeping in R1 is worth at most O(1) bits** (about 3–5, inferred): the Lemma B optimum against Shkredov's c/2^{k+4}. Do not spend budget there.
2. **R2 must be judged only by its per-doubling gain c.** Announce-worthy needs c ≥ 1/470 (normalisation as in Shkredov's appendix). Strong needs c ≥ 1/122. A BSG-free lemma leaves the coset-cap term τ/(4C2). If C2 disappears, the cap becomes about τ/4 in some normalisation. Whether it vanishes has to be checked against the unread Theorem 49; that is N1's job.
3. **The moonshot (κ polynomial) inside the growth paradigm** needs a per-doubling gain of Ω(1). Lemma C shows the frozen coset cap cannot be lifted by ℓ² bounds in the relevant range. Lifting it for Borel cosets is essentially the target statement, so an R2 moonshot must beat the cap by a genuinely new non-concentration input for µ^{(L)} beyond the girth window.
4. DESIGN's framing "few-step argument avoids iterating" should read "**each step gains Ω(1)**". Iteration itself is cheap (4–5 ideal doublings).

## 9. Items for referees (RB1/RB2)

- Check Lemma A's normalisation (Plancherel with d_min = (p−1)/2 for SL2; Steinberg dimension p for the P¹ permutation representation).
- Check the identification 1/c ↔ (2−h0)/g against Uspekhi Theorem 49 once someone obtains it. This is the one unverified link in the "within 3–5 bits" claim.
- Lemma C covers Borel cosets only. Dihedral and exceptional cosets are not analysed.
- Structural-optimality is proved relative to the certificate, not by an extremal measure (§3, last paragraph).

## Appendix A: script outputs (verbatim)

`n3_numbers.py`:
```
c=1/1640: k= 1641  log2(1/kappa)= 1658.264
overhead bits log2(10*18*40)= 12.814  => log2 M ~ 1671.08
log2 M <= 500  needs 1/c <= 470
log2 M <= 150  needs 1/c <= 122
h0=0.1 g=1/1640: argmax j=3117 (formula ceil((2-h0)/g)+1=3117); log2(1/theta*L0)=3128.68; (2-h0)/g+log2(1/g)=3126.68
h0=0.1 g=1/512: argmax j=974 (formula ceil((2-h0)/g)+1=974); log2(1/theta*L0)=983.74; (2-h0)/g+log2(1/g)=981.8
h0=0.0 g=1/1640: argmax j=3281 (formula ceil((2-h0)/g)+1=3281); log2(1/theta*L0)=3292.68; (2-h0)/g+log2(1/g)=3290.68
h0=0.1 g=1/40: argmax j=77 (formula ceil((2-h0)/g)+1=77); log2(1/theta*L0)=83.32; (2-h0)/g+log2(1/g)=81.32
h0=0.1 g=1/20: argmax j=39 (formula ceil((2-h0)/g)+1=39); log2(1/theta*L0)=44.32; (2-h0)/g+log2(1/g)=42.32
mult: h0=0.1 beta=1/20: log2(1/theta*L0)=66.62; log2(2/h0)/log2(1+b)=61.4
mult: h0=0.1 beta=1/40: log2(1/theta*L0)=127.56; log2(2/h0)/log2(1+b)=121.32
mult: h0=0.1 beta=1/1640: log2(1/theta*L0)=4926.09; log2(2/h0)/log2(1+b)=4914.5
ideal doubling h0= 0.1 / 0.125 / 0.2: doublings to reach 2: 5 / 4 / 4
N 4 kappa_true 0.1038 | N 16 0.2616 | N 64 0.3352 | N 256 0.3754
```
(In Lemma-B units, g is measured in log_p of the squared norm with target offset 2. Shkredov's c is normalised differently, so the 3128 at g = 1/1640 is **not** his 1658. The comparable quantity is the shape.)

`profile.py` (core):
```python
# maps y_j = g_j on P^1(F_p), index p = infinity; assert y[y]==id (involution)
f = delta_inf;  for L in 1..: f = sum(f[y_j])/N;  h = -log_p(sum((f-1/(p+1))^2))
```
