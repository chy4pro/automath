# N1: where c ≥ min{1/3, 1/(8C2), τ/(4C2), 0.5·c_H/(C1+C2)} = 1/1640 comes from

Task N1, Zaremba campaign Phase 0. Written 2026-09-26. All sources below were read by me from the PDFs. Anything I did not read is marked "unread".
The texts were extracted with pymupdf. Line references point to the extracted text, and page numbers are the printed ones.

## 0. Verdict (short)

1. **The min{...} and 1/1640 appear in exactly one place**: Shkredov, arXiv:2603.14116v2, Appendix (§6), printed pp. 38–39. It is one displayed line with **no derivation**.
   It is introduced by "following the argument of the proof of [53, Theorem 49] in the case of SL(F_p), we find". Here [53] = Shkredov, *Non-commutative methods in additive combinatorics and number theory*, Russian Math. Surveys 76(6) (2021) 1065–1122 (Uspekhi 76:6(462), 119–180). I read both the English and the Russian PDF from mathnet.ru (rm10029).
2. **The survey has no min{...}, no 1/1640, no τ, no C1/C2 and no c_H in Theorem 49 or Corollary 50.** Theorem 49's proof is an "outline" (English p. 1098: "Let us present an outline of the proof of Theorem 49"). It says "c, 0 < c < 1/4, is an absolute constant specified below" (p. 1098) and "the constants c_j and C may change from line to line" (p. 1099). The BSG constants appear there as a single C.
   So **each of the four terms is Shkredov's own unpublished bookkeeping.** Only the *structure* can be traced to the survey's case analysis. I reconstruct it below.
3. My explicit reconstruction (§3) works in the survey's framework with G = SL2(F_p). It gives one constraint per case of the proof:
   - **1/3**: reproduced exactly. It comes from the BSG-free "P almost all of G" regime plus quasirandomness.
   - **0.5·c_H/(C1+C2)**: reproduced as the growth case (BSG, then Lemma 40), with a slack factor ≈ 2. The same lemmas, with sharper bookkeeping, give c_H/(C2 + c_H(1+C1)) = **1/650**.
   - **1/(8C2)**: its structure is reproduced: the case P_*^3 = G, which uses only the BSG tripling constant C2. The factor 8 is not reproduced. The survey's own displayed chain gives 1/(4C2), and my chain gives 1/(C2+2).
   - **τ/(4C2)**: **not reproduced.** No case of the survey argument produces a τ. It can only enter through the Zaremba-specific inputs: girth τ, K(G^m) = p^{τ/6}, N^m = p^{τ/4}.
4. **The binding term is 0.5·c_H/(C1+C2) = 1/1640.** Both C2-only terms are non-binding whenever τ ≥ 2c_H, which holds for τ = 1/4 and for τ = 1/5. **So the τ = 1/4 vs 1/5 question (N2) does not change c.**
5. **If BSG is bypassed:** the terms 1/(8C2), τ/(4C2) and 0.5c_H/(C1+C2) all disappear as written. 1/3 stays. The growth term is replaced by the exponent of whatever lemma replaces BSG plus growth. Precise statement in §5.
   **If BSG is replaced** by one with exponents (C1', C2'): c = c_H/(2(C1'+C2')) as long as c_H ≤ τ/2 and c_H ≤ 1/4.
6. Six issues for referees and other tasks (§4): symmetry in Lemma 40; the citation numbering "[50, Theorem 5]"; C1 = 9 and C2 = 32 not being in Murphy's paper; the appendix's "κ ≥ 2^-1656" is really δ ≥ 2^-1656; a possible normalization problem in "k = ⌈1/c⌉+1"; improving c_H alone cannot reach c ≥ 1/450.

## 1. Exact source text

**Shkredov 2603.14116v2, §6 Appendix, p. 38–39** (verbatim apart from typesetting):

> Theorem 39. Let G be a group, A ⊆ G and E(A) ⩾ |A|^3/K. Then there is a ∈ A and a set A_* ⊆ a^{-1}A such that |A_*| ≫ |A|/K^{C1} and |A_*^3| ≪ K^{C2}|A_*|. One can take C1 = 9 and C2 = 32.
> [preceded by: "The constants C1, C2 from Theorem 39 can be obtained if one combines Theorem 2.29 and Lemma 2.13 (which is [60, Proposition 4.5]) of [61], see details in [48]." [61] = Tao–Vu book, [60] = Tao, Combinatorica 2008, [48] = Murphy arXiv:1907.13569]
>
> Also, we need [50, Theorem 5].
> Lemma 40. Let p be a prime number and A ⊆ SL2(F_p) be a generating set. Then |A^3| ≫ min{|SL2(F_p)|, |A|^{1+c_H}}, where c_H = 1/20.
>
> Then, following the argument of the proof of [53, Theorem 49] in the case of SL(F_p), we find
> c ⩾ min{1/3, (8C2)^{-1}, τ(4C2)^{-1}, 0.5 c_H (C1 + C2)^{-1}} = 1/1640 .
> It implies that k = ⌈c^{-1}⌉ + 1 = 1641. So, κ ⩾ 2^{-1656}, and in view of the bound (157) our desired estimate (158) follows.

Other parts of the appendix used here (p. 38): "put τ = 1/4, m = τ log_N p, K(G^m) = p^{τ/6} (see [42, Lemmas 12, 21] and [43, Page 7])". Also: "log N · κ = (6m)^{-1} τ δ log p = 6^{-1} δ log N, where δ = c/2^{k+4}, k = ⌈c^{-1}⌉ + 1 and c > 0 is an absolute constant."

**What c is.** The survey's Theorem 49 conclusion is |{(a_1..a_2k) : h = a_1⋯a_2k}| = |A|^{2k}/|G| + O(|A|^{2k} K_*^{-ck}). Its key step is (60): T_{2s}(f) ≪ T_s(f)|A|^{2s}K_*^{-c}. So c is the **per-doubling ℓ²-flattening saving exponent**.

**Survey [53], Theorem 49 (English p. 1098, verbatim):**
> Let G be a d-quasirandom group such that, for each generating set X ⊆ G, |X^3| ⩾ min{|G|, |X|^{1+c_*}} (59), where c_* > 0 is some absolute constant. Let A ⊆ G be any set such that max_{g∈G, Γ⩽G} |A ∩ gΓ| ⩽ |A|/K. Put K_* = min{d, K}. Then |{(a_1,…,a_2k) ∈ A^{2k} : h = a_1⋯a_2k}| = |A|^{2k}/|G| + O(|A|^{2k}/K_*^{ck}) for each h ∈ G.

The outline of the proof (pp. 1098–1100) has these steps:
- (Q) the quasirandom bound T_{2s}(f) ≤ T_s(f)^2|G|/d;
- a dyadic level set P = {Δ < r ≤ 2Δ}, with T_{2s}(f) ≪ L^4(2Δ)^4E(P) (61) and E(P) ≫ |P|^3/K_1 (62), where K_1 = K_*^c L^4;
- Δ|P| ≫ |A|^s/K_1 (63);
- BSG "in Murphy's form (see Theorem 10)" gives P_* ⊆ p^{-1}P, |P_*| ≫ |P|/K_1^C, |P_*^3| ≪ K_1^C|P_*|;
- three cases: (a) P_* generates G and P_*^3 ≠ G (growth); (b) P_*^3 = G; (c) P_* ⊆ H < G.

Survey Theorem 10 (p. 1077) is Theorem 39 with a single unspecified C. Survey Corollary 50 (p. 1100–1101) turns Theorem 49 into ‖Â(ρ)‖ ≤ |A|^{1-ε(δ)} when K_* ≥ |G|^δ, with k ≫ 1/δ and ε(δ) ≪ exp(−O(1/δ)). This is where the exponential loss 2^{-1/c} comes from.
The Russian version (Теорема 49, Следствие 50, "0 < c < 1/4") has identical content.

**Explicit written-out versions of the same argument, which I read to check the reconstruction:**
- MMS arXiv:1808.05845 (= [42] in Shkredov and [30] in MMS 2022), §6, Theorem 15 and its proof (pp. 17–20). It uses a weighted BSG (Lemma 18: E(A) ≫ M^{-9}|A|^3), Lemma 17 BSG with an unspecified C, and Helfgott–Kowalski growth δ = 1/3024. It has the same three cases, and there too c_* is "sufficiently small" with no number. Theorem 9 of that paper gives k = 3 log p/(c_* log K) and δ(k) = 1/2^{k+2}. Girth: Theorem 24 of that paper is used with τ_0 = 1/4 (p. 25).
- Shkredov arXiv:1802.09066 (= survey ref. [128]), Theorem 50 with its proof in the appendix (pp. 53–56, eqs. (152)–(165)). It has explicit dyadic constants (2^5 L^4, ζ = 2^{-7}L^{-4}M^{-1}) but a non-explicit BSG C and growth exponent. The constraint on c_* is again not computed ("Finding M satisfying both (164), (165) … we obtain the required dependence").

**MMS arXiv:2212.14646 (= [43])**, Lemma 4 sketch (pp. 5–6), eqs. (15)–(19). Girth ≥ τ log_N p with **τ = 1/5**; (17) holds with m = (τ/4) log_N p and K(G) = p^{τ/6}; (19) has δ = 1/2^{k+2}, "k ≪ log p / log K(f), see … [40, Section 6, Theorem 49]". Here [40] in MMS 2022 is the same survey.

## 2. The four terms as numbers (exact rationals)

With C1 = 9, C2 = 32, c_H = 1/20:

| term | τ = 1/4 (appendix) | τ = 1/5 (MMS 2022) |
|---|---|---|
| 1/3 | 1/3 | 1/3 |
| 1/(8C2) | 1/256 | 1/256 |
| τ/(4C2) | 1/512 | 1/640 |
| 0.5·c_H/(C1+C2) = (1/40)/41 | **1/1640** | **1/1640** |

The min is 1/1640 for both values of τ.

**General dominance facts (exact):**
- τ/(4C2) ≥ c_H/(2(C1+C2)) ⇔ τ(C1+C2) ≥ 2c_H·C2. This holds whenever τ ≥ 2c_H, because (C1+C2) ≥ C2.
- 1/(8C2) ≥ c_H/(2(C1+C2)) ⇔ C1+C2 ≥ 4c_H·C2. This holds whenever c_H ≤ 1/4.
- 1/3 ≥ c_H/(2(C1+C2)) ⇔ C1+C2 ≥ 1.5·c_H.

Hence, **for any BSG constants and c_H ≤ min{1/4, τ/2}, the printed formula reduces to c = c_H/(2(C1+C2)).**

## 3. Derivation of each term (reconstruction; my work, not in print)

**Setup (the survey's Theorem 49 specialized to G = SL2(F_p), normalized to measures).**
- d = (p−1)/2 (Frobenius; survey Theorem 47), |G| = p^3 − p.
- μ = 1_A/|A|. The non-concentration hypothesis is μ(gΓ) ≤ 1/K for every proper Γ, including Γ = {e}, so ‖μ‖_∞ ≤ 1/K. K_* = min{d, K}.
- f = μ − 1/|G|. r is the s-fold alternating convolution of f and f'. Then r = ν − 1/|G| with ν a probability measure (as in MMS 2018 p. 18 and Shkredov 2018 p. 54), so ‖r‖_1 ≤ 2 and ‖r‖_∞ ≤ 1/K + 1/|G|.
- t_s := ‖r‖_2^2 (the survey's T_s(f)/|A|^{2s}).
- Goal (60): t_{2s} ≤ t_s·K_*^{-c}. Assume it fails.
- L = number of dyadic levels, which is O(log p) = K_*^{o(1)}. Below I write ≲ for "up to L^{O(1)} and absolute constants". Such factors cannot change c because q0 is not explicit.

**Facts used by every case:**
- (Q) Survey display on p. 1098: t_{2s} ≤ t_s^2|G|/d. So we may assume t_s ≥ d·K_*^{-c}/|G|.
- (61) t_{2s} ≲ Δ^4 E(P), with |P|Δ^2 ≤ t_s and |P|Δ ≤ ‖r‖_1 ≤ 2.
- (E) From (61) and the failure of (60): E(P) ≳ t_sK^{-c}/Δ^4 ≥ |P|K^{-c}/Δ^2 ≥ |P|^3K_*^{-c}/4. So ζ := E(P)/|P|^3 ≳ K_*^{-c} =: 1/K_1.
- (Δ) t_sK^{-c} < t_{2s} ≲ (Δ|P|)^2·Δ^2|P| ≤ (Δ|P|)^2 t_s. So Δ|P| ≳ K_*^{-c/2}.
- (size) t_sK^{-c} ≲ Δ^4|P|^3 ≤ t_s^2|P|, and t_s ≤ ‖r‖_∞‖r‖_1 ≤ 4/K. So |P| ≳ K_*^{1−c}.
- (up) t_sK^{-c} ≲ (Δ|P|)^4/|P| ≤ 16/|P|. Combined with (Q): d·K_*^{-2c}/|G| ≲ 1/|P|.

**Term 1/3: the regime where P is almost all of G, with no BSG.** Suppose |P| ≥ |G|/K_1 = |G|K_*^{-c}. Then (up) gives d·K_*^{-2c} ≲ K_*^{c}, i.e. d ≲ K_*^{3c}. Since d ≥ K_*, this is a contradiction iff **c < 1/3**. This reproduces the term exactly, using only survey Theorem 47/(57) (quasirandomness) and the dyadic step (61). It uses **no BSG and no growth**.

**Term 1/(8C2): case (b), P_*^3 = G.** BSG (Theorem 39) gives |G| = |P_*^3| ≪ K_1^{C2}|P_*| ≤ K_1^{C2}|P|. So |P| ≳ |G|K_*^{-cC2}. Then (up) gives d ≲ K_*^{c(2+C2)}, a contradiction iff c < 1/(C2+2) = 1/34.
The survey's own chain (p. 1100) first weakens T_s ≥ K_*^{1−c}|A|^{2s}/|G| to √K_*·(…), using c ≤ 1/2, and then √K_*/K^c to K_*^{1/4}, using c < 1/4. That gives K_*^{1/4} ≲ K_1^{C2}, i.e. c < 1/(4C2). One more factor 2 (K_1 ≈ K_*^{2c}) gives Shkredov's 1/(8C2).
**Status:** the case and the dependence on C2 alone are certain. The constant 8 is not reproducible from the printed text. **The term depends on BSG only through the tripling exponent C2.**

**Term 0.5·c_H/(C1+C2): case (a), growth.** P_* generates G and P_*^3 ≠ G.
- Lemma 40 gives |P_*|^{c_H} ≪ |P_*^3|/|P_*| ≪ K_1^{C2}.
- BSG gives |P_*| ≫ K_1^{-C1}|P|.
- Combining these with (size): c_H(1 − c − cC1) ≤ c·C2 + o(1). This is a contradiction iff **c < c_H/(C2 + c_H(1+C1)) = (1/20)/(32.5) = 1/650.**

Two slacker versions of the same chain give Shkredov's term exactly:
- (α) the survey's display |P|^{1+c_H}K_1^{-C1(1+c_H)} ≪ |P_*|^{1+c_H} ≤ |P_*^3| ≪ K_1^{C2}|P|, followed by C1(1+c_H)+C2 ≤ 2(C1+C2);
- (β) using |P| ≥ K_*^{1/2} (from (size) and c ≤ 1/2) together with C1·c_H + C2 ≤ C1 + C2.

Both give c < 0.5·c_H/(C1+C2).
**Status:** the case is certain, and it is the only term involving c_H and C1. The factor 0.5 is slack. **With Lemma 40 exactly as Shkredov states it, the same lemmas give 1/650, not 1/1640.** This is bookkeeping only, and is subject to the symmetry caveat in §4(i).

**Case (c): P_* inside a proper subgroup H. This gives no printed term.**
- Lower bound: Σ_{x∈aH}|r(x)| ≥ Δ|P_*| ≳ Δ|P|K_1^{-C1} ≳ K_*^{-c(1/2+C1)}.
- Upper bound: Σ_{x∈aH}|r(x)| ≤ ν(aH) + |H|/|G| ≤ 1/K + 1/(p+1) ≤ 2/K_*. (Right cosets are left cosets of conjugates, so the hypothesis applies.)
- This is a contradiction iff c < 1/(C1 + 1/2) = 2/19. That is implied by the c_H term, so omitting it from the min is harmless.

**Term τ/(4C2): not reproduced.** The survey argument has no τ. In the Zaremba application τ enters only through the first-stage inputs: girth ≥ τ log_N p; K(G^m) = p^{τ/6}; with MMS's m = (τ/4) log_N p, N^m = p^{τ/4}.
- A condition of the form K_1^{C2} < p^{τ/4} (= N^m) would give exactly cC2 < τ/4 if c were measured in powers of p rather than of K_*. I cannot confirm this.
- The term is **non-binding** for τ ∈ {1/4, 1/5} (see §2), so it does not affect the record.
- It involves BSG only through C2.

**Summary of the case-to-term map:**

| printed term | case in survey proof | lemma(s) it uses | uses BSG? | my sharp value (C1=9, C2=32, c_H=1/20) |
|---|---|---|---|---|
| 1/3 | |P| ≳ |G|/K_1, quasirandom | Thm 47/48, (57), (61) | no | 1/3 (exact match) |
| 1/(8C2) | (b) P_*^3 = G | Thm 39 (C2 only), (Q) | C2 only | 1/(C2+2) = 1/34 |
| τ/(4C2) | unknown (application-specific) | Thm 39 (C2) + girth/first stage | C2 only | none in my chain |
| 0.5c_H/(C1+C2) | (a) growth | Thm 39 (C1, C2) + Lemma 40 | C1 and C2 | c_H/(C2+c_H(1+C1)) = 1/650 |
| (not printed) | (c) subgroup | Thm 39 (C1), non-concentration | C1 only | 2/(2C1+1) = 2/19 |

## 4. Issues found (for RB1, RB2, N2, N5, N6)

(i) **Symmetry in Lemma 40.** Shkredov states Lemma 40 for any generating set. Rudnev–Shkredov arXiv:1812.01671v3 Theorem 2 (the 1/20 result) assumes **A symmetric**. The same holds for the survey's Theorem 21 and for Moshchevitin–Shkredov arXiv:1911.07487 Theorem 13.
The survey (p. 1083) says only that dropping symmetry "will change only a little the absolute constants", with no exponent given. The P_* produced by Theorem 39 is not symmetric.
With the standard symmetrization X = P_* ∪ P_*^{-1} ∪ {e} and |X^3| ≤ (3K)^3|P_*| (Helfgott; quoted as MMS 2018 p. 18, "[26, Eq. (3.2)]"), C2 becomes 3C2 in cases (a) and (b). My sharp growth term then becomes c_H/(3C2 + c_H(1+C1)) = **1/1930**, which is worse than 1/1640, and case (b) becomes 1/(3C2+2) = 1/98.
**Whether Shkredov's 1/1640 is actually justified depends on a non-symmetric 1/20 that I could not find in print.** Possible fixes: a BSG that outputs a symmetric approximate group (Tao's Prop 2.43/2.44 route, as in Shkredov 2018 (158)–(160)), which has its own constants, unread for Tao–Vu; or a non-symmetric version of the RS proof.

(ii) **Citation numbering.** Lemma 40 cites "[50, Theorem 5]". In arXiv v3 of 1812.01671, Theorem 5 is the Aff(F_p) result and the SL2 statement is Theorem 2. The published Mathematika 68(3) numbering is unread.

(iii) **C1 = 9 and C2 = 32 are not in Murphy.** Murphy 1907.13569 Lemma 12 has an unspecified absolute C and cites Tao–Vu Theorem 2.44, not 2.29. The values 9/32 are Shkredov's own extraction from Tao–Vu Thm 2.29 + Lemma 2.13 and Tao 2008 Prop 4.5, both unread. This is N6's to verify.

(iv) **κ vs δ.** With c = 1/1640, k = 1641: log2(1/δ) = (k+4) + log2(1640) = 1655.68, so δ ≥ 2^{-1656}; and κ = δ/6 gives log2(1/κ) = 1658.26. So the appendix's "κ ≥ 2^{-1656}" is the bound for δ; the /6 was dropped. This agrees with the DESIGN note, and N2 owns it.

(v) **Normalization of c against k = ⌈1/c⌉+1 (flag for N2/RB1; unresolved).** In the survey (Cor 50: k ≫ 1/δ when K_* ≥ |G|^δ) and in MMS 2018 Thm 9 (k = 3 log p/(c_* log K)), the number of doublings is proportional to log|G|/(c·log K_*). With K = p^{τ/6}, that is k ≈ 18/(cτ) = 72/c for τ = 1/4, or 90/c for τ = 1/5, not ⌈1/c⌉+1.
If Shkredov's c is the survey's per-step exponent, the chain as printed understates k by a factor of about 50–90. That would put log2 M in the 10^5 range, not ≈1680.
It is also possible that his c is normalized differently, e.g. per step in powers of p; the τ in the τ/(4C2) term hints at such a mixed normalization. **I could not decide this from the printed text. It needs an independent re-derivation of (19) with explicit constants before any baseline number is quoted.**

(vi) **Improving c_H alone cannot reach the announce threshold under the printed min.** With C2 = 32 fixed, c ≤ min{1/256, τ/128} = 1/512 (τ = 1/4) or 1/640 (τ = 1/5). Both are below 1/450, however large c_H is. Reaching c ≥ 1/450 needs C2 ≤ 450τ/4 = 28.1 (τ = 1/4) or 22.5 (τ = 1/5), and C1 + C2 ≤ 11.25 while c_H = 1/20.
(This holds for the printed min. Under my reconstruction the τ-term does not exist and the large-case term is 1/34, so the cap would be different.) This is relevant to N5 ("lever (ii) is dead").

## 5. What changes if the BSG step is bypassed or replaced (the precise answer)

**A. BSG replaced by another BSG-type theorem with exponents (C1', C2')**, keeping Lemma 40 and Shkredov's bookkeeping:
c = min{1/3, 1/(8C2'), τ/(4C2'), c_H/(2(C1'+C2'))}. This equals c_H/(2(C1'+C2')) whenever c_H ≤ min{1/4, τ/2} (§2).
- Needed for c ≥ 1/450: C1'+C2' ≤ 11.25 (c_H = 1/20).
- Needed for c ≥ 1/110: C1'+C2' ≤ 2.75.
- With my sharp bookkeeping, the growth term is c_H/(C2' + c_H(1+C1')), which gives c ≥ 1/450 when C2' + (1+C1')/20 ≤ 22.5. The symmetry caveat (i) still applies.

**B. BSG bypassed** (R2: a direct energy-to-growth or flattening lemma):
- **1/(8C2) disappears.** Case (b) no longer exists as a BSG case. Large P is then handled by quasirandomness alone:
  - for |P| ≳ |G|/K_1 by the 1/3 computation;
  - for p^2K_*^{c} ≲ |P| ≲ |G|/K_1 by E(P) ≤ |P|^4/|G| + |P|^2|G|/d (Parseval plus d-quasirandomness);
  - so the new lemma is needed only for |P| ≲ p^2K_*^{c}.
- **τ/(4C2) disappears as written**, since it depends on BSG through C2. A τ-dependent condition without C2 may remain from the first-stage input; its form is unknown (see §3).
- **0.5·c_H/(C1+C2) disappears.** It is replaced by the exponent of the new lemma. Suppose the lemma has the form "E(P) ≤ |P|^{3−c_E} unless P puts ≥ |P|^{1−c_S} of its mass in one coset of a proper subgroup". Then the growth case gives c < c_E(1−c), i.e. **c < c_E/(1+c_E)** (sharp), or 0.5·c_E with Shkredov's slack (β). The subgroup case gives a condition in c_S, which replaces 2/(2C1+1).
- **1/3 stays.** It is BSG-free.
- The DESIGN's "min collapses to min{1/3, 0.5c_H} = 1/40" is the special case c_E = c_H = 1/20 with Shkredov's slack; the sharp version is c_H/(1+c_H) = 1/21. **It assumes an energy lemma with the same exponent 1/20 as tripling growth for non-concentrated sets in SL2(F_p). I did not find such a lemma in any source I read.** Rudnev–Shkredov's energy results that I saw are for Aff(F_p).

**C. Resulting κ under Shkredov's printed chain** (k = ⌈1/c⌉+1, δ = c/2^{k+4}, κ = δ/6; subject to issue (v)):

| c | k | log2(1/δ) | log2(1/κ) |
|---|---|---|---|
| 1/1930 (sym. caveat) | 1931 | 1945.91 | 1948.50 |
| 1/1640 (printed) | 1641 | 1655.68 | 1658.26 |
| 1/650 (sharp, Lemma 40 as stated) | 651 | 664.34 | 666.93 |
| 1/512 (c_H→∞, τ=1/4 cap) | 513 | 526.00 | 528.58 |
| 1/450 | 451 | 463.81 | 466.40 |
| 1/110 | 111 | 121.78 | 124.37 |
| 1/40 (BSG-free, c_E=1/20, slack) | 41 | 50.32 | 52.91 |

Mapping to log2 M adds the κ-independent overhead from (157) (10/(κε) with ε < 1/18, M* ≥ 40M, and so on). That belongs to the ledger task (Agent B) and is not recomputed here.
Moving 1/1640 → 1/650 is **constant bookkeeping**. Under the campaign rules it is not announce-worthy, and it is only valid if caveat (i) is resolved in its favour.

## 6. Sources

**Read (PDF text):**
- Shkredov arXiv:2603.14116v2 (§6 Appendix pp. 38–39; Lemmas 14–15 and Cor. 16 p. 9; eqs. 148–151 p. 35).
- Shkredov, Russian Math. Surveys 76(6) 2021: English and Russian full text from mathnet.ru rm10029. Read: Theorems 9, 10, 20, 21, 47, 48, 49, Cor. 50 and the outline proof.
- MMS arXiv:2212.14646 (Lemma 4 sketch, eqs. 14–19).
- MMS arXiv:1808.05845 (§6 Theorem 15 proof, Lemmas 17–18, Theorem 19 δ = 1/3024, Theorem 9, girth τ_0 = 1/4).
- Shkredov arXiv:1802.09066 (Theorem 50 and its appendix proof, eqs. 152–165).
- Rudnev–Shkredov arXiv:1812.01671v3 (Theorems 2 and 5, footnote on 1/12, the 1/15 remark).
- Murphy arXiv:1907.13569 (Lemma 12, Prop. 11, Theorem 24 part (1)).
- Moshchevitin–Shkredov arXiv:1911.07487 (Theorem 13).
- Zhang arXiv:2605.02518 (abstract and intro only; no explicit constants; Remark 1.3 "effectively computable").

**Unread:**
- Tao–Vu, *Additive Combinatorics*: Thm 2.29, Lemma 2.13, Thm 2.44, Prop 2.43.
- Tao, Combinatorica 2008, Prop 4.5.
- Rudnev–Shkredov, Mathematika 68(3) 2022 (published numbering of "Theorem 5").
- Helfgott, Ann. Math. 2008.
- Bourgain–Gamburd, Ann. Math. 2008.
- Kowalski's explicit Helfgott (1/1512).

None of the unread items is needed to locate the min{...}. The first two are needed to confirm C1 = 9 and C2 = 32 (N6), and the third to settle caveat (ii).
