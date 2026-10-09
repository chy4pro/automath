PARTIAL — document and commit-history comparison completed. X replies and Zenodo creation metadata were not accessible; the public PDFs omit the numerical certificate vectors/checker; forum time-zone and edit history were not established. No global priority claim or proof/certificate validation is made.

**Scope and evidence labels.** This is a literature/status dossier, accessed 9 October 2026 UTC. READ means primary text or primary metadata was inspected; it does not certify the mathematics. SECONDARY means a fact is relayed by another source. NOT ACCESSIBLE records a specific access or artifact gap. LIVE CLAIM marks an author's unverified public claim. PROVED below means that a proof is written in the source, as requested, not that this scout has refereed it. ASSERTED includes numerical verification reported without the full certificate and checker being available. Comparisons explicitly marked “inference” are comparisons of the READ statements, not new proofs.

**Main findings.**

- **READ:** the two October 5 files are not the earliest relevant repository artifacts. Commit `7e78435dd9692e6bc0d2635ec11a98078016a0ee`, authored and committed **2026-10-01 12:48:40 UTC**, added both earlier smoothing PDFs. GitHub records signature verification at **12:48:41 UTC**. Its `Sidon_smoothing_limit.pdf`, Theorem 1, already states the exact two-sided smoothing infimum; Theorems 4.4 and 5.1, Proposition 5.2 and Appendices B–C contain the relevant written arguments. [October 1 commit][C1], [earlier limit manuscript][E].
- **READ; comparison inference:** our R1 is the stronger cardinality statement: exact coefficient (c_*=2\sqrt2/3), additive (+1), every integer (N\ge207,360,000). Akwei's numerical certificate has reported coefficient (0.9428095208\ldots>c_*), a stated certified ceiling (0.942809522), and a safely rounded displayed bound (0.9428096). His exact (c_*) is an infimum/continuum attainment statement, not an exact-coefficient (O(1)) cardinality theorem. [R1][R1], [D, Theorem 5.3, p.18][D], [L, Theorems 1–2, pp.2–3][L].
- **READ; comparison inference:** the two optimality statements share the ramp autocorrelation, uniform-renewal measure, (a=4/3), boundary constant (2/3), and product (8/9). They quantify over different objects: a general positive-measure capacity in R2 versus Hou–Zhao covering certificates in Akwei. The latter does not state the full R2 theorem. Mixtures alone do not put its mixed autocorrelations outside R2's kernel class; a relation between certificate boundary cost and positive capacity is still needed for a formal implication. This dossier does not supply that proof. [R2, §§1,3–7][R2], [L, §§2–5][L].
- **READ / LIVE CLAIM:** an additional reply already exists under our proof claim, dated **17:23 on 5 October 2026, site time**. Akwei acknowledges our sharper bound, says he found no gap in the proof, and says a revision will cite our Zenodo record. He identifies the October 1 placeholder-author PDFs as his work and asserts independent discovery. These statements are not independent verification of authorship, independence, or our proof. [Reply 9297][F2].

**Source identity and reading coverage.**

READ: D and L were read throughout, including all numbered statements, references, appendices and figure captions. Each downloaded October 5 PDF has **30 pages**; the repository README's 23-page description belongs to the older layout. E was also read throughout (23 pages). B was inspected for its statements, dating, and the transition from a conjectured to a proved exact infimum; it was not fully refereed or fully read. Text extraction used JavaScript and PDF font maps; no embedded document code, supplied optimizer or checker was executed, and no Python was run. Some decorative/combining glyphs required comparison with the cleaner E layout. The figures were read through their captions and accompanying text, not independently analysed as images.

| ID | Immutable primary document | Internal date / identity | File fingerprint (SHA-256) |
| --- | --- | --- | --- |
| READ D | [A Data Science Analysis of Erdős Problem 30][D], 30 pp. | John Akwei; Version 4; 30 September 2026. PDF creation metadata: 5 October 14:31:32 UTC. | `d4250a43006f1e5854a5860f67c51655f547ad0f2a802dd8950a422ea927e613` |
| READ L | [The limit of vector-valued smoothing for Sidon sets is 2√2/3][L], 30 pp. | John Akwei; heading dated 5 October; retained manuscript date 26 September 2026. PDF creation/modification: 5 October 13:47:40 UTC. | `08264c7f7f1e6e24ced64d4d05a24db9964d8c86ee5384a1a75a2b353251fb9c` |
| READ E | [Vector-valued smoothing for Sidon sets cannot beat 2√2/3][E], 23 pp. | Placeholder author/affiliation fields; internal date 26 September. PDF creation: 1 October 12:43:32 UTC. | `24b4dec1699443d0aeab44d19015a55aa944de6b02a05f17d26e3f76cda591ba` |
| READ B | [A barrier for vector-valued smoothing certificates for Sidon sets][B], 16 pp. | Placeholder author/affiliation fields; internal date 25 September. PDF creation: 1 October 12:43:33 UTC. | `8dd2227367eef123a71610bc9eaa29206f0974d898e9649b2251d23d936c2739` |

READ: the downloaded bytes' Git blob hashes agree with the repository tree: D `bbb0bfdf593bcbf8702688016dc464e509f892e0`; L `5a612e1826f7013d49a6beb376317096e4f1f2b5`; E `188adfcde554264e4b1202eb2c3797a4f0d77087`; B `2d7d5cd305ac85933b9b7e5a8e5e8629bcf591bc`. Internal manuscript dates and PDF creation dates are not evidence of public availability on those dates. [Repository tree][TREE].

**(1) Exact claims and certification status.**

READ: L §1, p.2, and E §1, p.1, use the strong Sidon convention: all unordered sums (a+b) with (a\le b), including diagonals, are distinct; equivalently nonzero ordered differences are distinct. D p.4 abbreviates the wording, but uses the same Golomb-ruler convention and framework. None presents a weak-Sidon-only result.

READ: the certificate class is defined in L §§2.1–2.3, pp.4–5 (E pp.3–4; D pp.8–9). Fix arbitrary integers (m,L,K\ge1). Kernels (p^{(k)}\in\mathbb R^m) are nonnegative and each sums to one. Mixing weights satisfy (\lambda_k\ge0), (\sum_k\lambda_k=1). Boundary vectors (u^{(k)},v^{(k)}\in\mathbb R^{Lm}) are real, not required to be nonnegative, and are extended by one for (j\ge Lm). For every (q=0,\ldots,Lm), both

\[
\sum_k\lambda_k\sum_{i=0}^{m-1}p_i^{(k)}u_{q+i}^{(k)}\ge1,
\qquad
\sum_k\lambda_k\sum_{i=0}^{m-1}p_{m-1-i}^{(k)}v_{q+i}^{(k)}\ge1
\]

must hold. Its constants are

\[
a=m\sum_k\lambda_k\sum_i(p_i^{(k)})^2,
\qquad
b=1+\frac1m\sum_k\lambda_k\sum_{j<Lm}\big((u_j^{(k)})^2+(v_j^{(k)})^2-2\big),
\qquad\gamma=\sqrt{ab}.
\]

READ: the symmetric subfamily requires symmetric kernels and (u=v=w). The two infima range over all certificates and all resolutions, including all finite numbers of kernels. Continuum certificates replace the kernels by probability densities (\rho_k) supported on ([0,1]), with finite (a=\sum_k\lambda_k\int\rho_k^2), and measurable real profiles (\omega_k,\omega'_k) on ([0,\infty)) satisfying (\omega_k-1,\omega'_k-1\in L^1\cap L^2). They impose the two covering inequalities at every real shift (u\ge0), using (\rho_k(x)) and (\rho_k(1-x)), respectively. Here (b=1+\sum_k\lambda_k\int_0^\infty(\omega_k^2+\omega_k'^2-2)). Lemma 2.5 embeds every discrete certificate with unchanged (a,b). D initially describes the compact-tail profiles coming from discrete certificates; its extremal profile has an exponentially decaying, noncompact tail, as in L.

| Evidence / status | Exact statement, scope and locator |
| --- | --- |
| READ — PROVED (written proof) | L Theorem 1, p.2; Theorem 4.4, p.8; Corollary 4.5, p.9: every discrete or continuum certificate in the defined symmetric/two-sided families has (ab\ge8/9). Consequently (\gamma^*_{\rm sym}\ge\gamma^*\ge c_*). D Theorem 4.1, p.13, and Theorem 4.7, p.16, state the same result. E Theorem 1, p.2, and Theorem 4.4, pp.6–7, already contain it. |
| READ — PROVED (written proof) | L Theorem 5.1, p.9; D Theorem 5.1, p.17; E Theorem 5.1, p.7: (\rho(x)=2x\) on ([0,1]); the reversed end uses (\omega'\equiv1), and the other uses (\omega(t)=e^t-1\) for (0\le t<1), (\omega(t)=\int_0^1x r(t-x)\,dx\) for (t\ge1), where (r) is the uniform-renewal density. These profiles give (a=4/3,b=2/3,\gamma=c_*). |
| READ — PROVED (written proof) | L Proposition 5.2, p.9, Appendix B, pp.27–28; D Proposition 5.2, p.18; E Proposition 5.2, p.7, Appendix B, pp.20–21: for every integer (m\ge2), a one-kernel two-sided certificate exists at (L=\max(2,\lceil(2/\kappa)\log m\rceil)), with (a=4/3-1/(3m^2)) and (ab\le8/9+C\log(m)/m^2). (C) depends on unspecified renewal-decay constants (C_0,\kappa>0). Thus (\gamma^*=c_*). This is an infimum, not a finite discrete certificate at equality. |
| READ — ASSERTED numerical certification; artifacts NOT ACCESSIBLE | L Theorem 2, p.3, Appendix A, pp.26–27; D Theorem 5.3, p.18, Table A1, p.28; E Theorem 2, p.2, Appendix A, p.20: (m=512,L=8,K=1), 8194 covering inequalities reportedly verified over (\mathbb Q); (a=1.3333320618\ldots), (b=0.6666679802\ldots), (\gamma=0.9428095208\ldots<0.942809522). The displayed cardinality bound is (h(N)\le\sqrt N+0.9428096N^{1/4}+O(1)). The kernel coordinates are (p_i=(2i+1)/m^2); the full repaired boundary vector and checker are absent. |
| READ — PROVED conditional implication (written proof) | L Proposition 2.3, p.5; Lemma C.1, pp.29–30; Corollary C.2, p.30 (E pp.4,22–23). Given a valid two-sided certificate and integer (h\ge1), put (H=mh); if (N\ge2LH), every strong Sidon set of size (k) in ({0,\ldots,N-1}) satisfies (k^2\le(N-1+bH)(1+(k-1)a/H)). D Proposition 3.1, p.9, records its consequence. This analytic implication is separate from the asserted numerical certificate. |
| READ — ASSERTED/OPEN | L §6.4, p.12; E p.9; D p.19: equality for the symmetric infimum remains open; the stated bracket is (c_*\le\gamma^*_{\rm sym}<0.942810893), whose upper endpoint is another claimed exact-arithmetic certificate. |

READ: short verbatim statement excerpts (only line wrapping normalized):

> “Every continuum certificate satisfies b ≥ 4w/3 − (w²/2)·a for every w > 0. Consequently a·b ≥ 8/9.” — L, Theorem 4.4, p.8; also E, pp.6–7.

> “Every continuum certificate satisfies b ≥ 4w/3 − (w²/2)·a for every w > 0.” — D, Theorem 4.7, p.16.

READ: the other statements above are precise restatements; their displayed mathematical conclusions are transcribed. In particular L Corollary C.2 gives, for a fixed certificate, (N_1=N+bm), (\gamma=\sqrt{ab}), and every (N\ge N_0(a,b,m,L)),

\[
h(N)\le\sqrt{N_1}+\gamma N_1^{1/4}+\frac{\gamma^2}{2}
       +\frac{\gamma^3}{8N_1^{1/4}}
=\sqrt N+\gamma N^{1/4}+\frac{ab}{2}+o(1).
\]

READ: **no numerical value or explicit formula for (N_0(a,b,m,L)) is given.** The proof only says the condition (N\ge2LH) eventually holds for its chosen (H). The additive term is described more precisely than a bare (O(1)), but this is not an explicit-onset theorem. No stronger onset than R1 is stated. L's Proposition 5.2 does not state a uniform additive constant while (m\to\infty).

READ / NOT ACCESSIBLE: L Appendix A, p.27, says the optimizer, rational verifier and plain-text certificates must be obtained from the author and are to accompany a later publication. D Appendix A.4, p.30, lists private working filenames and future deposits, not their contents. The current recursive repository tree contains four PDFs, README, eight physics documents and an unrelated arXiv script; it contains none of these Sidon certificate/checker files. Therefore the requested stronger evidence category **NUMERICALLY CERTIFIED (certificate + checker available)** was not established here. No contact was made to obtain them.

READ: B Theorem A, p.2, states the weaker method lower bound (\sqrt{(\pi^2+16)/32}=0.89912465\ldots); Theorem B states the same numerical ceiling (0.942809522). Its Theorem 5.3, p.13, gives continuum attainment, but p.14 explicitly leaves discrete convergence unproved and Conjecture 5.6 states the exact infimum. E supersedes that gap with Proposition 5.2 and its appendix. Both were added by the same October 1 commit; their September internal dates do not prove successive public releases.

**(2) Citations, visible overlap and acknowledgment.**

| Evidence | Finding and locator |
| --- | --- |
| READ | Neither D nor L contains a citation or link to our Zenodo records, `chy4pro/automath`, our X post, Haoyu Chen, or our proof claim. The complete references are D p.27 and L pp.25–26. The full-text search was checked against these lists and the surrounding text. E likewise has no such citation. This is an observation about the accessed versions, not all future versions. |
| READ | Hou–Zhao is explicitly credited throughout. D p.9 and references p.27, L Proposition 2.1 p.4 and reference [10] p.25, specify arXiv:2607.01169v3, 4 September 2026, **Theorem 2.1**. D notes that its previous version called this Lemma 2.1. Hou–Zhao's exact (0.9434925907\ldots) is relayed by D; its primary paper was not independently reread for this task. |
| READ | Neither D nor L names Madeiros or wustep/Wu in its references. D Table 9, p.19, has an unnamed 11-kernel entry (0.94301). SECONDARY comparison with our related-work table suggests Wu q2, but D does not identify it, so that attribution is not established by D. L Table 1, p.2, omits that entry as well. |
| READ | D title page credits Anthropic Claude Fable 5.1 and Claude Opus 5.5. LIVE CLAIM: forum post 9295 says Claude assistance is credited in both documents. No corresponding Claude/Anthropic acknowledgment was found in L's complete extracted text or references. |
| READ; comparison inference | The ramp and its reflection have the identical autocorrelation (4/3-2|t|+(2/3)|t|^3) on (|t|\le1), zero outside. L Theorem 5.1 and E Theorem 5.1 state this in factored form. L's multiplier (\mu_1=2\sum_{n\ge0}U^{*n}) is four times R2's (v=\tfrac12\sum_{n\ge0}U^{*n}). Both texts display the quadratic lower expression (4s/3-as^2/2), optimized at (s=4/(3a)), and product (8/9). This is recognizable mathematical overlap. It is not evidence of copying or direction of influence. E already contains these items in the earlier dated commit. |
| READ / LIVE CLAIM | Reply 9297, under proof claim 386, acknowledges our exact coefficient and (+1), says its author read the proof and ran the checker without finding a gap, and promises a Zenodo citation in a revision. It also identifies the identical autocorrelation and factor-four renewal normalization. The independence claim remains the author's assertion. |

READ: forum post 9295 is displayed at **15:04 on 5 October 2026**. The complete post was fetched, including both PDF links, the non-refereed/not-on-arXiv disclosure, the claimed 8194 checks, and the request-only availability of certificates/checker. No post-specific edit marker is visible. The displayed 6 April page-edit date belongs to the problem description, not this October post. **NOT ACCESSIBLE:** no edit history or historical revision of post 9295 was obtained. No time-zone conversion was inferred from an unlabelled site timestamp.

**(3) Overlap with R1 and R2.**

READ; numerical comparison inference: (c_*=0.942809041582063\ldots). The posted ceiling exceeds it by approximately (4.80417937\times10^{-7}); the printed certificate value exceeds it by approximately (4.79217937\times10^{-7}). The rounded cardinality coefficient (0.9428096) exceeds it by (5.58417937\times10^{-7}). Thus the “within (5\times10^{-7})” description fits the unrounded certificate, not the rounded displayed coefficient. These are elementary decimal comparisons, not certificate checks.

READ; comparison inference: R1 improves the coefficient and supplies a uniform explicit onset. Akwei's Corollary C.2 has third-order term (ab/2\approx0.444), but at a larger coefficient and an unspecified onset; it is not uniformly stronger than R1. His continuum equality and infimum allow arbitrarily close discrete coefficients as stated in Proposition 5.2, but do not state R1's exact coefficient with a fixed (O(1)) remainder. The methods are different formulations of the same smoothing/energy mechanism: Hou–Zhao's finite covering program with two boundary vectors versus direct continuous scalar capacity.

| Evidence: READ statement comparison | Our R2 | Akwei L, Theorems 1/4.4/5.1 |
| --- | --- | --- |
| Object quantified | Even, nonnegative (f\in C_0(\mathbb R)\cap L^1(\mathbb R)), integral one, (a=f(0)>0); no positive definiteness or factorization required. | Finite mixtures of autocorrelations of nonnegative probability densities on ([0,1]), plus two admissible covering profiles per kernel. |
| Optimized quantity | (\beta(f)=\liminf_{T\to\infty}(C_f(T)-T)), with (C_f) defined using nonnegative probability measures on the closed interval. | (b), the summed boundary squared-profile cost, and (\inf\sqrt{ab}) over covering certificates/resolutions. |
| Lower conclusion | (a\beta(f)\ge8/9), including infinite (\beta). | (ab\ge8/9) at every allowed certificate. |
| Equality | Actual positive capacity has intercept (2/3) for the ramp autocorrelation, with explicit exponential bounds. | Continuum boundary profiles have cost (2/3); discrete certificates approach the infimum with stated (O(\log m/m^2)) error. |
| Barrier scope | Fixed kernel, nonnegative difference majorization, full infinite lattice sum; the method consequence separately assumes (\limsup C_f(T)/T\le1). | Exactly the defined symmetric and two-sided covering-certificate families, including all finite (K,m,L). Symmetric attainment remains open. |

READ; comparison inference: this is **neither the identical theorem nor a theorem that proves the full R2 statement**. R2's kernel hypotheses encompass the mixed autocorrelations described in L §3; saying merely “scalar versus mixtures” misses that overlap. To transfer R2's lower bound to a certificate's (b), one needs an explicit comparison such as (\beta(R)\le b_{\rm certificate}); identifying optimal costs would require more. Neither text supplies a comparison with the other paper's definitions. **No unconditional theorem-to-theorem implication is certified by this literature read.** In particular, non-implication has not been proved either. Their equality example and the general-kernel capacity extension should be recorded separately. Establishing the bridge would be proof work beyond this assignment.

READ: the common loss is documented explicitly in L Proposition 7.1, p.13, and D Proposition 6.1, p.20. Their identity contains three nonnegative discarded terms: covering slack (c(A)^2-k^2), the Cauchy–Schwarz defect (V(A)), and weighted missing-difference slack ((N-1+bH)\Delta(A)). R1 §5 likewise replaces the actual positive-difference set by all positive integers using nonnegativity, then bounds the kernel sum. This describes the sources' proof structure; it is not a proposed improvement.

**(4) Dated record, with UTC uncertainty kept visible.**

READ unless otherwise labelled. Git author and committer dates are shown separately even when equal. GitHub verification timestamps add server-side evidence for the Akwei uploads. A commit date alone is not a historical public-visibility log; the October 5 author reply also asserts the October 1 public posting. No independent visibility archive was obtained.

| UTC date/time, or explicitly unconverted site time | Item | Author date / committer date / other evidence |
| --- | --- | --- |
| 2025-12-31 16:33:51 UTC | Science repository created | GitHub `created_at`; repository is public at access. [Repository API][REPO] |
| September 25 / 26 / 30, time unknown | B / E and L / D internal manuscript dates | READ inside documents; **not publication timestamps**. |
| 2026-10-01 12:48:40 UTC | B and E added in [7e78435][C1] | Author 12:48:40; committer 12:48:40; GitHub `verified_at` 12:48:41. E already includes exact infimum, continuum ramp, numerical bound, pair-relaxation conjecture, and Appendices B–C. |
| 2026-10-01 12:54:37 UTC | [9a0e394 README][README1] describes both earlier papers | Author 12:54:37; committer 12:54:37. It explicitly describes the (c_*) limit and (0.9428096) cardinality bound. |
| 2026-10-02 12:51:22 UTC | Our [14710db G2 record][C2] states R1 | Author 12:51:22; committer 12:51:22. This is the stated result/G2 item; distinguish it from the next standalone proof. |
| 2026-10-02 13:00:01 UTC | Our [302feeb standalone R1 proof/checker][C3] | Author 13:00:01; committer 13:00:01; theorem (1.1) has exact coefficient, (+1), and (120^4) onset. |
| 2026-10-02 13:37:08 UTC — SECONDARY | Zenodo v1 [23103980][Z1] creation | Relayed in the assignment; API and record page returned 403, so creation metadata was not independently READ. |
| 2026-10-02 14:49:00 UTC | Our [9fd3168 optimality theorem][C4] | Author 14:49:00; committer 14:49:00. **This version assumes (C_f(T)=T+b+o(1)) with finite (b)** and proves (ab\ge8/9); it is not yet the unrestricted liminf wording. |
| 2026-10-02 approximately 15:3x UTC — SECONDARY | Zenodo v2 [23105891][Z2] | Relayed approximate date; exact creation metadata NOT ACCESSIBLE. |
| 2026-10-02 15:34:55 UTC | Our [11ff867 revised R2][C5] | Author 15:34:55; committer 15:34:55. The patch removes the finite-intercept assumption and introduces the current general liminf theorem and separate slope hypothesis. The commit also records v2 publication; this is not a substitute for Zenodo server metadata. |
| 2026-10-02 approximately 16:3x UTC — SECONDARY | Our [X announcement][X] | Relayed time; post/replies NOT ACCESSIBLE in this check. |
| UTC unknown; site displays 2026-10-02 19:06:21 | Our [proof claim 386][CLAIM] | READ submission timestamp. This differs from the approximate 20:0x time in the brief. Site time-zone not established; no UTC conversion asserted. |
| 2026-10-05 13:51:23 UTC | L added in [15609b5][C6] | Author 13:51:23; committer 13:51:23; GitHub verification 13:51:24. |
| 2026-10-05 14:33:04 UTC | D added in [6b32990][C7] | Author 14:33:04; committer 14:33:04; GitHub verification 14:33:05. |
| 2026-10-05 14:37:16 UTC | README expands the report description | Author and committer both 14:37:16, commit `156dfb2620d96e8ea6cc975d6208c342db4f96ff`. [Commit list][COMMITS] |
| UTC unknown; site displays 15:04 on 2026-10-05 | Akwei [post 9295][F1] | READ current text; no visible edit marker; historical edits not established. |
| UTC unknown; site displays 17:23 on 2026-10-05 | Akwei [reply 9297][F2] to our proof claim | READ acknowledgment, earlier-upload assertion, and citation promise. |
| 2026-10-08 14:49:49 UTC | Latest README revision | Author and committer both 14:49:49, commit `34ab41de8b0b3e2c738ac76fb2f2556e1c8aae3a`; no PDF changes in this commit. [Commit list][COMMITS] |

READ: the GitHub per-path API returned **one commit for each of D, L, E and B**, with fewer than 100 results and no second page required. Those four entries are all the reachable file history returned, not a claim that deleted/unreachable histories cannot exist. The repository-wide list returned 21 commits. The prior relevant upload is the October 1 pair, not the earlier physics/code files.

READ; bounded chronological conclusion: **for (i) an exact coefficient (c_*) in a cardinality theorem with fixed (O(1)) remainder, our October 2 standalone R1 is the first such item among the compared documents.** E has an earlier exact continuum value and infimum, but not that cardinality theorem. **For (ii) the exact (c_*) smoothing-limit statement, Akwei's October 1 E is earlier in the located dated record than either October 2 version of R2.** The full general-kernel positive-capacity theorem is a different statement and is not present in E. These conclusions distinguish the results and use the located records; **a bounded search is not a global priority claim**, nor does it independently establish who discovered what first.

**(5) Mathematically relevant observations and remaining boundaries.**

- READ / LIVE CLAIM: none of D, L or E identifies an error in our work; they do not cite it. Reply 9297 says the author found no gap and reports successful checker/capacity calculations. Its only specific correction is a lost superscript in the site's rendered (120^4) onset. The current fetched claim source contains `120^4`; no historical formatting version was obtained.
- READ: Akwei reaches the identical continuum constant by the reflected ramp and a two-sided extension of Hou–Zhao. No discrete certificate, cardinality theorem, or proved method limit below (c_*) is stated. L §6.3, p.12 (D p.12) reports an extrapolated product (0.888888880), slightly below (8/9), but explicitly as an extrapolation of multiplier-family numerics, not a feasible sub-barrier certificate. No contradiction to R2 is established.
- READ: L Proposition 7.3, pp.14–15, and D Proposition 6.3, p.21, contain a written upper-bound argument for the level-one moment relaxation (\widehat h_2(N)), including a normalized limsup at most (c_*). L Theorem 7.6, p.18, and D Theorem 6.5, p.22, report only four finite numerical instances, (N\in\{10^4,10^5,10^6,10^7\}), within 1.03 below (\sqrt N+c_*N^{1/4}). D explicitly describes double-precision FFT checks, not exact-arithmetic verification.
- READ / ASSERTED: the full statement (\widehat h_2(N)=\sqrt N+c_*N^{1/4}+O(1)) is **Conjecture 7.7** in L p.18 (E p.14), **Conjecture 6.6** in D p.22; the authors say the required error analysis has not been written. The abstract, discussion, README and forum's broader “same second-order constant” language must not be promoted into a proved asymptotic barrier for all pair-statistics arguments. This is a discrepancy of stated scope, not a referee verdict on the underlying proof.
- READ / ASSERTED: claims concerning diminishing three-/four-point gains and logarithmic growth in the construction survey are numerical evidence at finite sizes. D pp.5–8,23–26 and L pp.20–25 do not solve Erdős #30 or establish a general moment-hierarchy impossibility theorem.

SECONDARY for underlying ruler optimality; READ as D's reported values: D p.6, Table 1 gives the following optimal Golomb-ruler lengths, attributed to existing records. They were not independently searched or certified here. The interval convention is ruler span at most (N-1); D p.4 reports exact (h(N)) through (N=586), including (h(586)=28).

| Marks (k) | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reported optimal span | 55 | 72 | 85 | 106 | 127 | 151 | 177 | 199 | 216 | 246 | 283 | 333 | 356 | 372 | 425 | 480 | 492 | 553 | 585 |

**Bounded trace check and access gaps.**

READ: the additional trace check ran from **2026-10-09 19:04:19.626 to 19:08:47.983 UTC**, approximately 4.47 minutes, within the 20-minute limit. It covered the public forum profile, the proof-claim reply, GitHub profile/repository metadata and the available file histories, arXiv author search, and the stated X URLs/search. The October 1 files and README are positive earlier traces. The September manuscript dates were not treated as earlier public traces.

READ: the forum profile exposed post 9295 and proof-claim reply 9297; no earlier matching forum post was found there. The GitHub profile links `@JohnAkwei`; the public repository-list search identified Science as the relevant repository. The arXiv author query `au:Akwei` returned three papers by **Bernard Akwei**, not John, and none about Sidon smoothing. LIVE CLAIM: post 9295 says the work had not been posted to arXiv or refereed as of its date. This search does not exclude an unindexed or differently attributed submission.

NOT ACCESSIBLE: the supplied X status returned 404 to direct retrieval and an error in the browser tool, so replies were not inspected. The public X profile yielded a limited logged-out timeline; the direct search yielded an application shell, not search results. No absence-of-replies inference is warranted. General web queries for the author/title/constants and the X status ID produced no useful matching earlier trace. OpenAlex/Semantic Scholar, erdosproblemaday and Mathlib/Zulip were not additional search lanes in this narrowly scoped check; no completeness claim about them is made.

NOT ACCESSIBLE: both Zenodo APIs and record pages returned 403. READ: the forum/claim pages and reply endpoint succeeded through direct retrieval despite browser-tool failures. No edit-history or time-zone data was exposed in those responses or the FAQ. These are the precise residual gaps in the PARTIAL status; the requested literature comparison is complete to this source boundary.

**Access ledger.** All times below are UTC request-start times. Primary document links are pinned to the commits identified by the retrieved per-path history; blob hashes were compared against the downloaded bytes. Failed browser attempts are summarized after the direct-source ledger. API requests were read-only.

[D]: https://github.com/johnakwei/Science/blob/6b3299078de2dc1a837d3e51d6fa438300143eac/A_Data_Science_Analysis_of_Erdos_Problem_30.pdf
[L]: https://github.com/johnakwei/Science/blob/15609b5ab23a9b5abb4e37684ce5071c7fadb6e5/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf
[E]: https://github.com/johnakwei/Science/blob/7e78435dd9692e6bc0d2635ec11a98078016a0ee/Sidon_smoothing_limit.pdf
[B]: https://github.com/johnakwei/Science/blob/7e78435dd9692e6bc0d2635ec11a98078016a0ee/Sidon_smoothing_barrier.pdf
[R1]: https://github.com/chy4pro/automath/blob/302feebe0395cd6f8251b170c57843112670f472/problems/erdos30/SIDON_BOUND_PROOF.md
[R2]: https://github.com/chy4pro/automath/blob/11ff8676a7ba1791b5a0a3f5630793116cdfa336/problems/erdos30/KERNEL_OPTIMALITY.md
[C1]: https://github.com/johnakwei/Science/commit/7e78435dd9692e6bc0d2635ec11a98078016a0ee
[C2]: https://github.com/chy4pro/automath/commit/14710db592ac3197a084b5787c1e4d039714c1af
[C3]: https://github.com/chy4pro/automath/commit/302feebe0395cd6f8251b170c57843112670f472
[C4]: https://github.com/chy4pro/automath/commit/9fd3168bdd13058d3ba49221b40126c518a62a2f
[C5]: https://github.com/chy4pro/automath/commit/11ff8676a7ba1791b5a0a3f5630793116cdfa336
[C6]: https://github.com/johnakwei/Science/commit/15609b5ab23a9b5abb4e37684ce5071c7fadb6e5
[C7]: https://github.com/johnakwei/Science/commit/6b3299078de2dc1a837d3e51d6fa438300143eac
[F1]: https://www.erdosproblems.com/forum/thread/30#post-9295
[F2]: https://www.erdosproblems.com/forum/thread/proof-claim:6342b22f36484ea28285c2c7d4ca288a#post-9297
[CLAIM]: https://www.erdosproblems.com/forum/thread/30/proof-claims#proof-claim-386
[REPO]: https://api.github.com/repos/johnakwei/Science
[TREE]: https://api.github.com/repos/johnakwei/Science/git/trees/main?recursive=1
[COMMITS]: https://api.github.com/repos/johnakwei/Science/commits?per_page=100
[README1]: https://github.com/johnakwei/Science/blob/9a0e39426400552f94925cb6945ddcc5a0aa239b/README.md
[Z1]: https://zenodo.org/records/23103980
[Z2]: https://zenodo.org/records/23105891
[X]: https://x.com/HaoyuChn/status/2106093758110728328

| Evidence / retrieval | Access UTC | Source URL |
| --- | --- | --- |
| READ (HTTP 200) | 2026-10-09 19:02:37.855 | [repo](https://api.github.com/repos/johnakwei/Science) |
| READ (HTTP 200) | 2026-10-09 19:02:37.880 | [tree](https://api.github.com/repos/johnakwei/Science/git/trees/main?recursive=1) |
| READ (HTTP 200) | 2026-10-09 19:02:37.882 | [commits](https://api.github.com/repos/johnakwei/Science/commits?per_page=100) |
| READ (HTTP 200) | 2026-10-09 19:02:37.884 | [profile](https://api.github.com/users/johnakwei) |
| READ (HTTP 200) | 2026-10-09 19:02:37.884 | [forum](https://www.erdosproblems.com/forum/thread/30) |
| READ (HTTP 200) | 2026-10-09 19:02:37.885 | [report](https://raw.githubusercontent.com/johnakwei/Science/main/A_Data_Science_Analysis_of_Erdos_Problem_30.pdf) |
| READ (HTTP 200) | 2026-10-09 19:02:37.887 | [limit](https://raw.githubusercontent.com/johnakwei/Science/main/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf) |
| READ (HTTP 200) | 2026-10-09 19:02:54.368 | [commits](https://api.github.com/repos/johnakwei/Science/commits?per_page=100&path=A_Data_Science_Analysis_of_Erdos_Problem_30.pdf) |
| READ (HTTP 200) | 2026-10-09 19:02:54.395 | [commits](https://api.github.com/repos/johnakwei/Science/commits?per_page=100&path=The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf) |
| READ (HTTP 200) | 2026-10-09 19:02:54.396 | [commits](https://api.github.com/repos/johnakwei/Science/commits?per_page=100&path=Sidon_smoothing_limit.pdf) |
| READ (HTTP 200) | 2026-10-09 19:02:54.400 | [commits](https://api.github.com/repos/johnakwei/Science/commits?per_page=100&path=Sidon_smoothing_barrier.pdf) |
| READ (HTTP 200) | 2026-10-09 19:03:27.483 | [Sidon_smoothing_limit.pdf](https://raw.githubusercontent.com/johnakwei/Science/7e78435dd9692e6bc0d2635ec11a98078016a0ee/Sidon_smoothing_limit.pdf) |
| READ (HTTP 200) | 2026-10-09 19:03:27.509 | [Sidon_smoothing_barrier.pdf](https://raw.githubusercontent.com/johnakwei/Science/7e78435dd9692e6bc0d2635ec11a98078016a0ee/Sidon_smoothing_barrier.pdf) |
| READ (HTTP 200) | 2026-10-09 19:03:27.510 | [README.md](https://raw.githubusercontent.com/johnakwei/Science/9a0e39426400552f94925cb6945ddcc5a0aa239b/README.md) |
| READ (HTTP 200) | 2026-10-09 19:03:27.511 | [7e78435dd9692e6bc0d2635ec11a98078016a0ee](https://api.github.com/repos/johnakwei/Science/commits/7e78435dd9692e6bc0d2635ec11a98078016a0ee) |
| READ (HTTP 200) | 2026-10-09 19:03:27.511 | [johnakwei](https://www.erdosproblems.com/forum/user/johnakwei) |
| READ (HTTP 200) | 2026-10-09 19:04:52.418 | [proof-claims](https://www.erdosproblems.com/forum/thread/30/proof-claims) |
| NOT ACCESSIBLE (HTTP 403) | 2026-10-09 19:04:52.472 | [23103980](https://zenodo.org/api/records/23103980) |
| NOT ACCESSIBLE (HTTP 403) | 2026-10-09 19:04:52.476 | [23105891](https://zenodo.org/api/records/23105891) |
| READ (HTTP 200) | 2026-10-09 19:04:52.480 | [14710db](https://api.github.com/repos/chy4pro/automath/commits/14710db) |
| READ (HTTP 200) | 2026-10-09 19:04:52.483 | [302feeb](https://api.github.com/repos/chy4pro/automath/commits/302feeb) |
| READ (HTTP 200) | 2026-10-09 19:04:52.485 | [9fd3168](https://api.github.com/repos/chy4pro/automath/commits/9fd3168) |
| NOT ACCESSIBLE (HTTP 404) | 2026-10-09 19:04:52.490 | [2106093758110728328](https://x.com/HaoyuChn/status/2106093758110728328) |
| NOT ACCESSIBLE for complete timeline/search; HTTP 200 | 2026-10-09 19:04:52.491 | [JohnAkwei](https://x.com/JohnAkwei) |
| READ (HTTP 200) | 2026-10-09 19:05:41.054 | [comments](https://www.erdosproblems.com/forum/proof-claims/386/comments) |
| READ (HTTP 200) | 2026-10-09 19:05:41.130 | [query](https://export.arxiv.org/api/query?search_query=au:Akwei&start=0&max_results=20) |
| NOT ACCESSIBLE for complete timeline/search; HTTP 200 | 2026-10-09 19:05:41.131 | [search](https://x.com/search?q=from%3AJohnAkwei%20(Sidon%20OR%20smoothing%20OR%200.9428)%20until%3A2026-10-03&src=typed_query&f=live) |
| NOT ACCESSIBLE (HTTP 403) | 2026-10-09 19:05:41.132 | [23103980](https://zenodo.org/records/23103980) |
| NOT ACCESSIBLE (HTTP 403) | 2026-10-09 19:05:41.132 | [23105891](https://zenodo.org/records/23105891) |
| READ (HTTP 200) | 2026-10-09 19:07:00.606 | [15609b5ab23a9b5abb4e37684ce5071c7fadb6e5](https://api.github.com/repos/johnakwei/Science/commits/15609b5ab23a9b5abb4e37684ce5071c7fadb6e5) |
| READ (HTTP 200) | 2026-10-09 19:07:00.607 | [6b3299078de2dc1a837d3e51d6fa438300143eac](https://api.github.com/repos/johnakwei/Science/commits/6b3299078de2dc1a837d3e51d6fa438300143eac) |
| READ (HTTP 200) | 2026-10-09 19:07:54.959 | [github-repos](https://api.github.com/users/johnakwei/repos?per_page=100&sort=updated) |
| READ (HTTP 200) | 2026-10-09 19:07:54.986 | [our-kernel-history](https://api.github.com/repos/chy4pro/automath/commits?path=problems%2Ferdos30%2FKERNEL_OPTIMALITY.md&per_page=100) |
| READ (HTTP 200) | 2026-10-09 19:07:54.987 | [site-faq](https://www.erdosproblems.com/faq) |
| READ (HTTP 200) | 2026-10-09 19:08:25.050 | [11ff8676a7ba1791b5a0a3f5630793116cdfa336](https://api.github.com/repos/chy4pro/automath/commits/11ff8676a7ba1791b5a0a3f5630793116cdfa336) |

READ: additional browser-only retrievals occurred on 2026-10-09 before 19:06:21 UTC; their exact request-second timestamps were not exposed by that tool. The [current repository page](https://github.com/johnakwei/Science) and [current L file wrapper](https://github.com/johnakwei/Science/blob/main/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf) were visible. The [current D file wrapper](https://github.com/johnakwei/Science/blob/main/A_Data_Science_Analysis_of_Erdos_Problem_30.pdf), [problem page](https://www.erdosproblems.com/30), the [L raw redirect](https://github.com/johnakwei/Science/raw/refs/heads/main/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf) and [E raw redirect](https://github.com/johnakwei/Science/raw/refs/heads/main/Sidon_smoothing_limit.pdf), raw-content PDF parsing, forum/claim, Zenodo and the supplied X status failed or returned no readable text in that tool; direct-source results above determine the evidence labels. These attempts provide no extra dating evidence.

READ: browser searches during 19:04–19:05 UTC used the exact query strings `"John Akwei" Sidon smoothing 2026`, `"johnakwei" "0.9428"`, `"Sidon_smoothing_limit"`, `site:arxiv.org "Akwei" Sidon`, `site:x.com/JohnAkwei ("Sidon" OR "smoothing" OR "2√2")`, `"2106093758110728328"`, and `"vector-valued smoothing" "Akwei"`. No matching earlier source from these results was used. This negative retrieval is not evidence of absence.

READ: the comparison additionally used the repository checkout of R1 §1/§5–7, R2 §0–1/§3–7, and the [paper related-work table](https://github.com/chy4pro/automath/blob/main/publish/automath-papers/erdos30/main.tex), inspected during 19:02–19:09 UTC. Their historical theorem statements were checked against the public commit patches linked above. The concept DOI [10.5281/zenodo.23103979](https://doi.org/10.5281/zenodo.23103979) was READ as the target in claim 386, not as a successfully retrieved Zenodo record.
