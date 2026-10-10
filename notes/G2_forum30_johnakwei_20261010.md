PARTIAL — Both requested PDFs were read in full and the bounded comparison is complete. Exact UTC timestamps for the forum and X, X replies, and live Zenodo creation metadata could not be established. The numerical certificate vectors/verifier are not supplied in the inspected public repository. No proof or certificate was checked by this scout.

# Erdős #30: John Akwei documents, overlap, chronology and replies

Assignment: AUT-82; accessed **9 October 2026 UTC**. The filename follows the requested `20261010` name; it is not the observation date. This dossier supplements, and does not silently replace, the earlier [October 9 dossier](/work/problems/erdos30/THIRD_PARTY_JOHNAKWEI_20261009.md).

Evidence labels apply to every paragraph or table row: **READ** = primary text/metadata inspected, not mathematical validation; **SECONDARY** = another source's account; **LIVE CLAIM** = an author's unverified claim, even when its text was READ; **NOT ACCESSIBLE** = an identified access or artifact gap. A comparison marked “inference” compares the written statements; it supplies no new proof. “Written proof” below means an argument appears in the document, not that this scout endorses it. A bounded search is not a global priority claim.

## 1. Forum post and exact document identities

**READ:** [post 9295](https://www.erdosproblems.com/forum/thread/30#post-9295), by `johnakwei`, displays **15:04 on 05 Oct 2026**. The fetched HTML exposes no timezone or seconds. This is the exact displayed timestamp, **not independently established UTC**. No post edit history was available.

**READ — short verbatim excerpt:**

> It was developed with substantial help from Anthropic's Claude models, which is credited in both documents.

The full post was read. Full verbatim reproduction is omitted to respect quotation limits; the original link above provides the complete text. The following is a factual summary, not a quotation.

**READ / LIVE CLAIM:** The post announces `h(N) ≤ √N + 0.9428096 N^(1/4) + O(1)`, compares it with Hou–Zhao's `0.9435` and the site's `0.98183`, and attributes it to asymmetric two-sided vector smoothing. It specifies `ρ(x)=2x`, `m=512`, `L=8`, 8,194 exact-rational covering checks, and `γ<0.942809522`. It asserts a universal certificate floor `2√2/3`, attained in the two-sided limit, with less than about `5×10^-7` room remaining. It says the method cannot improve exponent `1/4`; also asserts the same constant for a pair-level relaxation retaining variance and missing-difference information. It identifies Hou–Zhao Theorem 2.1 and its own Appendix C as the implication to a Sidon bound, says the work is unrefereed and not on arXiv, credits its own Claude assistance, and offers the certificates/verifier on request. Those last availability and verification claims are not public artifact checks.

**READ:** Exact URLs linked in that post:

- Report: https://github.com/johnakwei/Science/blob/main/A_Data_Science_Analysis_of_Erdos_Problem_30.pdf
- Companion: https://github.com/johnakwei/Science/blob/main/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf

**READ:** Fresh direct downloads succeeded with HTTP 200 and matched the preserved October 9 source bytes exactly. Both current PDFs have **30 pages**; the README's 23-page description is stale for the current companion. Page references below use PDF page numbers. All pages, references, appendices and figure captions were read; plotted curves were not independently interpreted or recomputed. Preserved JavaScript text extraction has occasional garbled combining glyphs; the central formulas also appear in the cleaner earlier manuscript and surrounding prose.

| Evidence | ID and immutable PDF | First appearance in returned path history; author = committer UTC | Later edits returned |
|---|---|---|---|
| READ | **D**, [A Data Science Analysis of Erdős Problem 30][D] | `6b3299078de2dc1a837d3e51d6fa438300143eac`, **2026-10-05 14:33:04**; GitHub signature verified at 14:33:05 | None; one path commit |
| READ | **L**, [The limit of vector-valued smoothing for Sidon sets is 2√2/3][L] | `15609b5ab23a9b5abb4e37684ce5071c7fadb6e5`, **2026-10-05 13:51:23**; verified at 13:51:24 | None; one path commit |
| READ | **E**, [Sidon_smoothing_limit.pdf][E], earlier 23-page limit paper | `7e78435dd9692e6bc0d2635ec11a98078016a0ee`, **2026-10-01 12:48:40**; verified at 12:48:41 | None; one path commit |
| READ / SECONDARY for prior full inspection | **B**, [Sidon_smoothing_barrier.pdf][B], earlier barrier paper | Same October 1 commit explicitly adds this file as well | Prior dossier's path history has one entry; current 21-commit history contains no later PDF change |

**READ:** D says Version 4, 30 September 2026, with John Akwei as author. L has an October 5 heading, a retained September 26 manuscript date and John Akwei's author block. E has a September 26 internal date and placeholder author/affiliation fields; its Theorem 1 already states the exact two-sided infimum. Internal dates are not public-release dates. The October 1 commit and its [12:54:37 README update][EARLYREADME] are earlier located traces than either October 5 file.

**READ:** SHA-256 fingerprints: D `d4250a43006f1e5854a5860f67c51655f547ad0f2a802dd8950a422ea927e613`; L `08264c7f7f1e6e24ced64d4d05a24db9964d8c86ee5384a1a75a2b353251fb9c`. Current Git blobs are D `bbb0bfdf593bcbf8702688016dc464e509f892e0`, L `5a612e1826f7013d49a6beb376317096e4f1f2b5`. The recursive tree is untruncated. Repository-wide history returns 21 commits without pagination; latest is README-only `34ab41de8b0b3e2c738ac76fb2f2556e1c8aae3a`, **October 8 14:49:49 UTC**. This describes reachable returned history, not deleted/private history or historical public visibility.

## 2. What the two PDFs actually claim

### Definitions, constants and quantifiers

**READ:** L §1 p.2 uses strong Sidon sets: unordered sums `a+b` with `a≤b`, including doubles, are distinct; equivalently nonzero ordered differences are distinct. `h(N)` is the maximum size in `{1,…,N}`. D p.4 abbreviates the definition but uses that same Golomb-ruler and certificate convention. Neither paper claims the original Erdős conjecture solved.

**READ:** The current [problem page](https://www.erdosproblems.com/30) still displays Carter–Hunter–O'Bryant's `0.98183` as its record. That is the site's displayed statement, not a complete current-literature adjudication; the forum and repository claims compared below are later. **SECONDARY:** Our required October 2 G2 records Hou–Zhao v3 Theorem 1.2 at `0.9434925907135450…` with `O(1)`, without a printed numerical onset. This task does not promote a repository certificate claim into a refereed record.

**READ:** L §§2.1–2.3 pp.4–5 and D Part III pp.8–9 define the two-sided certificate as follows. Integers `m,L,K≥1`; nonnegative vectors `p^(k)∈R^m` with sum one; mixing weights `λ_k≥0`, sum one; real boundary vectors `u^(k),v^(k)∈R^(Lm)`, extended by one beyond index `Lm−1`. Boundary vectors need not be nonnegative. For **every** `q=0,…,Lm`, require

\[
\sum_k\lambda_k\sum_{i=0}^{m-1}p_i^{(k)}u_{q+i}^{(k)}\ge1,
\qquad
\sum_k\lambda_k\sum_{i=0}^{m-1}p_{m-1-i}^{(k)}v_{q+i}^{(k)}\ge1.
\]

**READ:** The constants are

\[
a=m\sum_k\lambda_k\sum_i(p_i^{(k)})^2,
\quad b=1+\frac1m\sum_k\lambda_k\sum_{j<Lm}
[(u_j^{(k)})^2+(v_j^{(k)})^2-2],\quad\gamma=\sqrt{ab}.
\]

**READ:** The symmetric subfamily requires symmetric `p` and `u=v=w`; its boundary cost is `1+2(Σ_k λ_k Σ_j w_j²/m−L)`. Infima range over **all finite** `m,L,K` and feasible certificates. The uniform kernel and boundary weights one give `a=b=1`.

**READ:** L's continuum family consists of nonnegative probability densities `ρ_k` supported on `[0,1]`, finite `a=Σ λ_k∫ρ_k²`, real profiles `ω_k,ω'_k` on `[0,∞)` with each profile minus one in `L¹∩L²`, and both covering inequalities for **every real shift** `u≥0`, using `ρ_k(x)` and `ρ_k(1−x)` respectively. Here `b=1+Σ λ_k∫(ω_k²+ω'_k²−2)`. Lemma 2.5 embeds any discrete certificate with unchanged `a,b`. D p.9 initially gives compact-tail profiles from discrete vectors; its extremal continuum profile later has an exponentially decaying tail, as in L's more general definition.

| Evidence and status | D locator | L locator | Exact result or boundary |
|---|---|---|---|
| READ — written proof | Theorems 4.1 p.13 and 4.7 p.16 | Theorem 1 p.2; Theorem 4.4 p.8; Corollary 4.5 p.9 | Every defined discrete/continuum, symmetric/two-sided certificate has `ab≥8/9`, hence `γ≥c*=2√2/3=0.94280904…`. For every `w>0`, `b≥4w/3−aw²/2`; the chosen width is `w=4/(3a)`. |
| READ — written proof | Theorem 5.1 p.17 | Theorem 5.1 p.9 | Continuum equality: `ρ(x)=2x` on `[0,1]`, `a=4/3`, `b=2/3`. Reversed end has `ω'≡1`; the other has `ω(t)=e^t−1` for `0≤t<1`, and `ω(t)=∫₀¹x r(t−x)dx` for `t≥1`. |
| READ — written proof | Proposition 5.2 p.18, sketch | Proposition 5.2 p.9; Appendix B pp.27–28 | Every integer `m≥2` has a one-kernel certificate with `L=max(2,ceil((2/κ)log m))`, `a=4/3−1/(3m²)`, `ab≤8/9+C log(m)/m²`. `C` depends on unspecified positive renewal constants `C₀,κ`. Thus the two-sided infimum equals `c*`. This is not finite-certificate equality. |
| READ / LIVE CLAIM — reported rational computation | Theorem 5.3 p.18; Table A1 p.28 | Theorem 2 p.3; Appendix A pp.26–27 | `m=512,L=8,K=1`; `p_i=(2i+1)/m²`; 8,194 covering inequalities; reported `a=1.3333320618…`, `b=0.6666679802…`, `γ=0.9428095208…<0.942809522`. Displayed consequence: `h(N)≤√N+0.9428096 N^(1/4)+O(1)`. |
| READ — conditional implication, written proof in L | Proposition 3.1 p.9 | Proposition 2.3 p.5; Lemma C.1 pp.29–30 | Given a valid two-sided certificate and integer `h≥1`, put `H=mh`. For every `N≥2LH` and strong Sidon set of size `k` in `{0,…,N−1}`, `k²≤(N−1+bH)(1+(k−1)a/H)`. |
| READ — unspecified onset | Equation (3.4) p.9 | Corollary C.2 p.30 | With fixed certificate, `N₁=N+bm` and `γ=√(ab)`, for every `N≥N₀(a,b,m,L)`, `h(N)≤√N₁+γN₁^(1/4)+γ²/2+γ³/(8N₁^(1/4))=√N+γN^(1/4)+ab/2+o(1)`. **No numerical or explicit-formula `N₀` is supplied.** |
| READ / LIVE CLAIM — symmetric endpoint remains open | p.19 | §6.4 p.12 | `c*≤γ*sym<0.942810893`, upper endpoint from reported `m=512,L=4,K=2` certificate. Equality of the symmetric infimum with `c*` is an open question. |

**READ — certificate meaning:** D p.10/Table A1 and L Appendix A describe rationalizing the kernels, solving the boundary program again for those kernels, rounding boundary vectors, repairing them with a uniform increment, checking every covering inequality over `Q`, and evaluating `a,b,γ²` exactly. Such a check establishes **feasibility and a coefficient**, conditional on the analytic smoothing implication. It is not a proof of global optimizer optimality, a count of all Sidon sets, an explicit onset, or a proof of the original conjecture. L Appendix C separately writes out the asymmetric boundary case and the finite smoothing implication.

**NOT ACCESSIBLE:** Neither downloaded PDF supplies the complete rational boundary vectors or executable verifier. L p.27 offers these on request and for a future deposit. D p.30 lists filenames including `cert_m512_*.txt`, `certify.py`, `floor2.py`, `v4_checks.py`, construction/SDP code and data, but the current public tree contains none of them. No request was sent and no supplied code was run. “Numerically certified” in this dossier therefore always means **author-reported certification**.

**READ — certificate constants inventory:** D Table A1 p.28 contains all rows below; L Appendix A contains the last seven applicable rows. Printed decimals are transcribed, not recomputed. Optimizer-only `γ` in D Table 8/L Table 2 differs slightly from the repaired rational-certificate `γ`; e.g. at `m=512` it is `0.9428095137`, whereas the reported certified value is `0.9428095208`.

| READ / LIVE CLAIM: certificate | m,L,K | Inequalities | a | b | γ |
|---|---|---:|---:|---:|---:|
| Symmetric original | 32,4,2 | 129 | 1.294133696 | 0.6874915809 | 0.94324229 |
| Symmetric original | 64,4,2 | 257 | 1.313278418 | 0.6770076151 | 0.94292072 |
| Symmetric original | 128,4,2 | 513 | 1.3216771522 | 0.6725867335 | 0.94283748 |
| Symmetric original | 256,4,2 | 1025 | 1.3262775741 | 0.6702236072 | 0.94281628 |
| Symmetric original | 512,4,2 | 2049 | 1.3264253589 | 0.6701415970 | 0.94281112 |
| Symmetric reoptimized | 512,4,2 | 2049 | 1.3286071522 | 0.6690407889 | 0.9428108915 |
| Two-sided optimized | 32,4,2 | 258 | 1.3131380851 | 0.6770798880 | 0.9429206688 |
| Two-sided optimized | 64,4,2 | 514 | 1.3230863497 | 0.6718702582 | 0.9428374024 |
| Two-sided optimized | 128,4,2 | 1026 | 1.3281707583 | 0.6692681652 | 0.9428162103 |
| Two-sided optimized | 256,4,2 | 2050 | 1.3305653396 | 0.6680561258 | 0.9428108643 |
| Linear | 256,8,1 | 4098 | 1.3333282471 | 0.6666717951 | 0.9428108696 |
| Linear | 512,8,1 | 8194 | 1.3333320618 | 0.6666679802 | 0.9428095208 |

**READ:** The other certified ceiling printed for the linear `m=256,L=8` case is `γ<0.942810871`. D Table 8/L Table 2 list optimizer values `0.9429240903, 0.9428378328, 0.9428162572, 0.9428108625, 0.9428095137` at `m=32,64,128,256,512`. The statements `b≈2/3+1/(3m²)` and `ab≈8/9+2/(9m²)−1/(9m⁴)` are numerical observations with about `3×10^-8` error in `b`, not exact general formulas. Richardson limits `0.94280910`, `0.94280908`, `0.94280906` and the multiplier-family extrapolation `0.888888880` are extrapolations, not feasible sub-barrier certificates.

### The limit proof as written, and its loss

**READ — outline of the source's argument, not a proof attempt:** L Lemma 3.1 derives a weak-duality lower bound for boundary cost using a nonnegative multiplier `μ=4 Leb+ν`. It depends on the kernels through the mixed autocorrelation `R=Σλ_kρ_k*ρ̃_k`. Lemmas 4.1–4.3 use the uniform renewal density `r`, its error `g=r−2`, the identity `∫g²=1/3`, and a lag weight equal to `8/3` on `(0,1)` and at least `8/3` beyond. Rescaling `μ_w=2w Σ_{n≥0}U_w^{*n}` gives Theorem 4.4's quadratic expression in `w`. Theorem 5.1 exhibits the reflected ramp and equality profiles. Appendix B discretizes them and repairs every covering deficit, establishing approach to the infimum. D Parts IV–V provide the same core argument, plus a full cosine-arch inequality.

**READ:** Auxiliary constants include the one-atom multiplier `β=2/a`, giving `b≥G+1/(2a)`; the cosine-arch product floor `π²/32=0.3084251…`; and the older certificate barrier `sqrt((π²+16)/32)=0.89912465…` (D Lemma 4.3 pp.14–15; L pp.6–7). The renewal proofs invoke positive but unspecified `C₀,κ`, and cite a root-location decimal `−2.0888`; they do not supply effective values for the general decay constants. Appendix B uses `|ω'|≤4`, a jump of `−1` at `t=1`, repair `η=4/m²+ε_L`, and `ε_L=sup_{t≥L−1}|ω(t)−1|`. These are analytic certificate-construction constants, not a numerical Sidon onset.

**READ:** The lost information is explicit in D Proposition 6.1 p.20 and L Proposition 7.1 p.13: the finite identity discards covering slack `c(A)²−k²`, Cauchy–Schwarz defect `V(A)`, and weighted unused-difference slack `(N−1+bH)Δ(A)`. Our R1 §5 (5.2) also enlarges actual positive differences to all positive integers using kernel nonnegativity. These source descriptions identify the loss without proposing a repair.

### Pair relaxation, finite evidence and exact-value claims

**READ:** D Definition 6.2/Proposition 6.3 p.21 and L Definition 7.2/Proposition 7.3 pp.14–15 define a level-one moment relaxation with a positive semidefinite moment matrix, diagonal `Γ(x,x)=f(x)`, entrywise `Γ≥0`, `0≤f≤1`, and each positive-difference budget at most one. They give a written certificate upper bound and `limsup (ĥ₂(N)−√N)/N^(1/4)≤c*`.

**READ / LIVE CLAIM:** D Theorem 6.5 p.22 and L Theorem 7.6 p.18 report feasible points only at `N∈{10^4,10^5,10^6,10^7}`, with `ĥ₂(N)≥√N+c*N^(1/4)−1.03`. Printed totals are `108.441,331.969,1028.794,3214.284`. Difference budgets were checked using double-precision FFT; the reported maximum is `≤1−1.3×10^-8`. Reducing density by relative `10^-7` gives margin `2×10^-7` at count cost at most `3.3×10^-4`; a separate `N=3000` explicit matrix check is reported. D explicitly distinguishes this from exact arithmetic.

**READ:** Full asymptotic equality `ĥ₂(N)=√N+c*N^(1/4)+O(1)` is **Conjecture 6.6** in D p.22 / **Conjecture 7.7** in L p.18. The texts say the lower-bound error analysis has not been written. Broad abstract/discussion/forum language about an established universal pair-statistics barrier exceeds these numbered results. Equality of the symmetric certificate infimum is separately open.

**READ / LIVE CLAIM:** D Parts II and VII report finite Singer/Bose/Ruzsa surveys, up to approximately `4.1×10^6` in an extended run (`174` rows in the main table: `34,29,111` by family). Logarithmic growth and lack of a power law are finite observations. D pp.23–25/L pp.20–23 give three-point computations only for `N=12,18,20,26,32,40`, and a cyclic four-point comparison at moduli `24,48,63`. These do not prove a fixed-level hierarchy barrier. No small-value computation was performed here.

**READ as reported values / SECONDARY for underlying optimality:** D pp.4–6 attributes exact `h(N)` through `N=586`, including `h(586)=28`, to optimal Golomb rulers. D Table 1 gives the following spans for marks `k=10,…,28`: `55,72,85,106,127,151,177,199,216,246,283,333,356,372,425,480,492,553,585`. D Table 11 reports `h(20)=6,h(32)=7,h(40)=8,h(50)=9,h(64)=10,h(80)=11,h(100)=12,h(120)=13,h(140)=14,h(160)=15,h(180)=16`. These are transcribed existing-table claims, not fresh certification of ruler optimality.

## 3. Citations, attribution and all references

**READ:** Neither D nor L cites our Zenodo record, `chy4pro/automath`, Haoyu Chen, our forum contribution, or our X post. Complete reference lists and full-text searches agree. Their kernel is the reflection of ours, with the same autocorrelation, constants `4/3,2/3,8/9`, and uniform-renewal mechanism. Mathematical overlap does not establish use of our work or copying, particularly given the October 1 artifact.

**READ:** D's title page credits **Anthropic Claude Fable 5.1 and Claude Opus 5.5**. This is its author's own AI assistance, not credit to our GPT-6 Astra/Claude referee pipeline. No Claude/Anthropic acknowledgment appears in L's complete extracted text, despite the forum assertion that both documents credit it. D's unnamed 11-kernel `0.94301` row (Table 9 p.19) resembles Wu's result, but neither PDF names Madeiros or wustep/Stephen Wu. **Inference:** correspondence with Wu is plausible; explicit attribution is absent.

**READ / LIVE CLAIM:** In [reply 9297][REPLY], displayed **17:23 on 05 Oct 2026**, Akwei acknowledges our sharper exact-coefficient `+1` theorem; identifies the same autocorrelation and factor-four renewal normalization; says he read our proof, found no gap and ran our checker; asserts independent discovery and authorship of the October 1 placeholder PDFs; and promises to cite our Zenodo record in a revision. These are author reports, not independent validation. Current PDF path histories show no revision implementing that promise.

**READ — complete bibliographic inventory:** D p.27 has 26 unnumbered entries; `D1…D26` below are editorial identifiers in its printed order. L pp.25–26 has 21 numbered entries, all also in D. Listing a reference does not mean its original text was reread in this task.

| Evidence | D entry | L entry | Bibliographic entry as identified in the PDFs |
|---|---:|---:|---|
| READ | 1 | — | R. C. Baker, G. Harman, J. Pintz, *The difference between consecutive primes, II*, Proc. London Math. Soc. (3) 83(3) (2001), 532–562. |
| READ | 2 | 1 | J. Balogh, Z. Füredi, S. Roy, *An upper bound on the size of Sidon sets*, Amer. Math. Monthly 130(5) (2023), 437–445; arXiv:2103.15850 (2021). |
| READ | 3 | 2 | T. F. Bloom, *Erdős Problems, Problem #30*, erdosproblems.com/30. |
| READ | 4 | 3 | R. C. Bose, *An affine analogue of Singer's theorem*, J. Indian Math. Soc. (N.S.) 6 (1942), 1–15. |
| READ | 5 | 4 | D. Carter, Z. Hunter, K. O'Bryant, *On the diameter of finite Sidon sets*, Acta Math. Hungar. 175(1) (2025), 108–126; arXiv:2310.20032 (2023). |
| READ | 6 | 5 | J. Cilleruelo, *Gaps in dense Sidon sets*, Integers 0 (2000), A11. |
| READ | 7 | 6 | S. Diamond, S. Boyd, *CVXPY: a Python-embedded modeling language for convex optimization*, J. Mach. Learn. Res. 17(83) (2016), 1–5. |
| READ | 8 | — | distributed.net, *Completion of the OGR-28 project*, 23 November 2022. |
| READ | 9 | 7 | P. Erdős, P. Turán, *On a problem of Sidon in additive number theory, and on some related problems*, J. London Math. Soc. 16(4) (1941), 212–215. |
| READ | 10 | 8 | W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II, second edition, Wiley, New York (1971). |
| READ | 11 | 9 | P. J. Goulart, Y. Chen, *Clarabel: an interior-point solver for conic programs with quadratic objectives*, arXiv:2405.12762 (2024). |
| READ | 12 | 10 | J. Hou, H. Zhao, *An improved upper bound for finite Sidon sets via vector-valued smoothing*, arXiv:2607.01169v3, 4 September 2026; v1, 1 July 2026, titled *Vector-valued smoothing for finite Sidon sets*. The theorem numbering cited is v3. |
| READ | 13 | 11 | J. B. Lasserre, *Global optimization with polynomials and the problem of moments*, SIAM J. Optim. 11(3) (2001), 796–817. |
| READ | 14 | 12 | B. Lindström, *An inequality for B₂-sequences*, J. Combin. Theory 6(2) (1969), 211–212. |
| READ | 15 | 13 | K. O'Bryant, *A complete annotated bibliography of work related to Sidon sequences*, Electron. J. Combin. (2004), Dynamic Survey DS11. |
| READ | 16 | 14 | K. O'Bryant, *On the size of finite Sidon sets*, Ukrainian Math. J. 76 (2025), 1352–1368; arXiv:2207.07800 (2022). |
| READ | 17 | 15 | B. O'Donoghue, E. Chu, N. Parikh, S. Boyd, *Conic optimization via operator splitting and homogeneous self-dual embedding*, J. Optim. Theory Appl. 169(3) (2016), 1042–1068. |
| READ | 18 | — | OEIS Foundation, *The On-Line Encyclopedia of Integer Sequences*, A143824. |
| READ | 19 | — | M. Ortega, S. Prendiville, *Extremal Sidon sets are Fourier uniform, with applications to partition regularity*, J. Théor. Nombres Bordeaux 35(1) (2023), 115–134. |
| READ | 20 | 16 | I. Z. Ruzsa, *Solving a linear equation in a set of integers I*, Acta Arith. 65 (1993), 259–282. |
| READ | 21 | 17 | H. D. Sherali, W. P. Adams, *A hierarchy of relaxations between the continuous and convex hull representations for zero-one programming problems*, SIAM J. Discrete Math. 3(3) (1990), 411–430. |
| READ | 22 | 18 | J. Singer, *A theorem in finite projective geometry and some applications to number theory*, Trans. Amer. Math. Soc. 43(3) (1938), 377–385. |
| READ | 23 | 19 | C. J. Stone, *On characteristic functions and renewal theory*, Trans. Amer. Math. Soc. 120(2) (1965), 327–342; L also prints DOI 10.1090/S0002-9947-1965-0189151-0. |
| READ | 24 | 20 | C. J. Stone, *On moment generating functions and renewal theory*, Ann. Math. Statist. 36 (1965), 1298–1301. |
| READ | 25 | — | T. Tao, *Comment on Erdős Problem #30*, announcement with Carter, Georgiev, Gómez-Serrano, Hunter, O'Bryant and Wagner of `0.97633`, Erdős Problems forum, 17 February 2026. |
| READ | 26 | 21 | S. Torquato, F. H. Stillinger, *Local density fluctuations, hyperuniformity, and order metrics*, Phys. Rev. E 68 (2003), 041113. |

## 4. Overlap matrix

**READ — comparison inference:** Categories below compare Akwei's statements with the item named in the first column. They are not theorem-to-theorem reductions or proof-validity verdicts.

| Compared item | Classification | Reason and exact scope |
|---|---|---|
| Our R1 second-order bound, [§1 Theorem (1.1)][R1] | **Strictly weaker** as a stated asymptotic cardinality bound | Our coefficient is exactly `c*`, with `+1` for **every integer `N≥120^4=207,360,000`**. Akwei's displayed coefficient is `0.9428096` (reported certificate ceiling `0.942809522`), with no explicit numerical onset. His continuum equality is not a printed cardinality theorem with exact coefficient and uniform `O(1)`. His asymptotic additive `ab/2≈0.444` does not establish a smaller finite-N bound throughout our range. |
| Our R2 general kernel-capacity theorem, [Theorems 1–2][R2] | **Incomparable as stated**, with identical extremal constant and autocorrelation | Ours quantifies over every even nonnegative `f∈C₀(R)∩L¹(R)`, integral one, `f(0)>0`, and positive-measure capacity `C_f`; it proves `liminf(C_f(L)−L)≥8/(9f(0))`. Akwei quantifies over finite mixtures of probability-density autocorrelations and feasible two-sided covering profiles, bounding their cost `b`. The objects optimized differ. No formal implication between the formulations is certified here. |
| Ramp example in R1/R2 | **Identical** autocorrelation, constant product and renewal mechanism | Our `2(1−t)` is the reflection of his `2t`; both give `f(t)=4/3−2|t|+(2/3)|t|³` on `|t|≤1`. Our half-line measure `½ΣU^{*n}` is one quarter of his multiplier `2ΣU^{*n}`. Both use `a=4/3,b=2/3,ab=8/9`. |
| Madeiros's [August 17 post][MADEIROS] | **Strictly stronger** reported numerical coefficient | Madeiros reports `0.943244449828<0.94325`, fallback `0.943260253`, with `O(1)`. Akwei reports `γ<0.942809522`. Neither certificate was replayed here. |
| Wu's [q2 certificate claim][WU] | **Strictly stronger** reported numerical coefficient | Wu reports `0.943006169985179<0.94301`, eleven symmetric kernels, `m=48,L=6`, with `O(1)`. Akwei's reported coefficient is lower; its full rational certificate is not public in the inspected tree. |
| General pair-relaxation impossibility versus R2 | **Incomparable / not an established stronger theorem** | R2 expressly excludes additional variance/missing-difference information from its method consequence. Akwei writes a pair-relaxation upper bound and finite lower examples, but the matching full asymptotic result is a conjecture. |

**READ — qualification to the scalar/vector language:** Mixed autocorrelations in L still meet R2's kernel hypotheses. “Scalar versus mixtures” alone therefore does not establish non-overlap or a stronger vector theorem. Identifying a certificate's boundary cost with, or bounding it against, the positive-capacity intercept would require a bridge between definitions. That bridge is not proved in this literature assignment. Our method consequence separately assumes unit asymptotic slope and use of the full infinite lattice difference sum; our capacity theorem itself does not require that slope assumption.

## 5. Located chronology and bounded earlier-trace search

**READ unless marked otherwise:** Git timestamps are author/committer timestamps, not independently measured first-push times. GitHub's signature-verification timestamp supplies additional server metadata but is not a historical public-visibility log. Forum timestamps are deliberately left unconverted where timezone is unknown. Internal manuscript dates are not publication timestamps.

| Time (UTC unless explicitly marked) | Event and evidence |
|---|---|
| September 25/26/30, times unknown | READ internal dates of B/E/D. No earlier public availability follows from these dates. |
| **2026-10-01 12:48:40** | READ [7e78435][EARLYCOMMIT] adds B and E; GitHub verification 12:48:41. E pp.1–2 already contains the exact certificate infimum, ramp/renewal description and `0.942809522` reported certificate. |
| **2026-10-01 12:54:37** | READ [9a0e394 README][EARLYREADME] describes both papers, exact limit and numerical cardinality bound. |
| **2026-10-02 12:51:22** | READ our `14710db592ac3197a084b5787c1e4d039714c1af`, initial G2 document, states the supplied R1 bound. |
| **2026-10-02 13:00:01** | READ our [302feeb standalone proof/checker][R1], exact coefficient, `+1`, onset `120^4`. |
| **2026-10-02 13:37**, minute precision | SECONDARY: local publication README records Zenodo v1 [23103980][ZENODO]. Live API returned 403; exact creation seconds not confirmed. |
| **2026-10-02 13:37:24** | READ our `b8d66ad897e0d89ab45a30584a0611cf9a767bd8` records v1 publication. This is a git timestamp, not the Zenodo timestamp. |
| **2026-10-02 14:49:00** | READ our `9fd3168bdd13058d3ba49221b40126c518a62a2f` adds the original kernel-optimality theorem, with finite-intercept hypothesis `C_f(L)=L+b+o(1)`. |
| **2026-10-02 15:34:55** | READ our [11ff867][R2] strengthens R2 to the general liminf formulation and records v2 Zenodo [23105891](https://zenodo.org/records/23105891). SECONDARY for actual deposit time; exact server metadata unavailable. |
| **2026-10-02 approximately 16:3x** | SECONDARY: local ledger records [X v1][X1]. NOT ACCESSIBLE live (404); exact seconds and replies unconfirmed. |
| **2026-10-02 19:06:21, site time; UTC unconfirmed** | READ our [proof claim 386][CLAIM] submission. It is still the **only** #30 proof claim. The source currently shows `120^4` and links Lean; original conjecture explicitly untouched. |
| October 2 ordinary forum-comment timestamp: **not found** | READ current ordinary thread has no separate `chenhaoyu` R1/R2 post. SECONDARY local ledger says the planned comment was redirected to the human proof-claim form. `notes/forum_30_comment_20261002.txt` is prepared text, not proof that a second ordinary comment was posted. |
| **2026-10-03 03:17:42 / 03:28:06** | SECONDARY: local X text records duplicate status `2106222130950263138` and replacement [2106224747545604507][X2], respectively. Live replacement retrieval returned 404; no inference about deletion or replies. |
| **2026-10-05 13:51:23** | READ L uploaded at `15609b5ab23a9b5abb4e37684ce5071c7fadb6e5`; verified 13:51:24. |
| **2026-10-05 14:33:04** | READ D uploaded at `6b3299078de2dc1a837d3e51d6fa438300143eac`; verified 14:33:05. |
| **2026-10-05 14:37:16** | READ README expansion `156dfb2620d96e8ea6cc975d6208c342db4f96ff`. |
| **2026-10-05 15:04, site time; UTC unconfirmed** | READ Akwei [post 9295][POST]. |
| **2026-10-05 17:23, site time; UTC unconfirmed** | READ Akwei [reply 9297][REPLY] under our proof claim. |
| **2026-10-08 14:49:49** | READ latest README-only commit; no PDF update. |

**READ — bounded chronology conclusion:** The located October 1 document precedes our October 2 documents for the **exact two-sided smoothing-certificate limit and shared ramp/renewal mechanism**. Among the compared documents, our October 2 R1 supplies the stronger **exact-coefficient cardinality theorem with explicit additive constant and onset**. The general positive-capacity R2 formulation is not stated in Akwei's paper. Neither chronology establishes who privately discovered what, independence, copying, or worldwide priority. The October 2 G2's failure to locate an earlier limit statement must now be qualified by this positive October 1 evidence.

**READ — earlier traces searched:** Science's full reachable 21-commit list, per-path histories, October 1 PDF/README, the author's forum profile, current thread and proof-claim reply, and arXiv author search were inspected. The arXiv `au:Akwei` query returned three papers by **Bernard Akwei**, none by John Akwei about Sidon sets. General queries for the author, exact file/title/constant, MathOverflow and erdosproblemaday supplied no useful additional earlier trace. Negative search results do not establish absence.

**READ / NOT ACCESSIBLE:** OpenAlex `Akwei Sidon` returned count zero. Semantic Scholar's equivalent search returned **429 Too Many Requests**; no citation count can be inferred. The post itself says no arXiv posting/refereeing as of October 5 (**LIVE CLAIM**). This targeted task did not include an exhaustive 2015–2026 citation-network sweep. No Mathlib/Zulip theorem priority was requested; no claim of checking those venues is made.

## 6. Factual quality assessment

**READ:** L contains actual analytic arguments for the dual bound, renewal identities, continuum equality, discretization and the two-sided smoothing implication. It is more than an optimizer output. Appendix C is written out rather than merely referring to an AI answer. D summarizes portions of that argument and provides additional survey/experimental material. Neither is fully self-contained in the sense of proving all renewal-theory inputs; Feller and Stone are cited, with unspecified exponential-decay constants. No line-by-line mathematical referee verdict is supplied here.

**READ / NOT ACCESSIBLE:** The specific finite certificate is not reproducible from these public artifacts alone: complete boundary coordinates and the rational checker are missing. Tabulated `a,b,γ` and inequality counts cannot substitute for them. Reported independent numerical checks are described in D Appendix A.3, but that description does not identify an external human referee or supply the scripts. The post explicitly discloses no refereeing.

**READ:** There is a clear scope gap between the numbered conjecture and the broader prose about the pair-level constant. Four finite examples and a limsup upper bound do not themselves constitute the asymptotic lower theorem that Conjecture 6.6/7.7 expressly leaves unfinished. This is a textual scope assessment, not an attempted disproof. The same care applies to predictions about logarithmic construction growth and higher moment levels.

**READ:** Editorial/bibliographic limits include L's missing Claude credit despite the post's wording, the README page-count mismatch, no actual deposits for listed working files, D's unnamed `0.94301` reference, and no citations to our work in the fetched versions. The earlier placeholder author block is acknowledged by the author in the reply. None of these establishes a defect in the analytic limit proof or an inference of misconduct.

**READ / LIVE CLAIM:** AI assistance was disclosed by the author. Written proofs and reported exact checks must be evaluated on their contents; model names and a model-assisted “independent check” do not establish external verification. This scout did not rerun optimizers, certificates, SAT/ILP, numerical experiments, or Lean, and attempted no proof.

## 7. Recommendation to the coordinator

**READ-based recommendation — add a related-work paragraph in the next otherwise eligible Zenodo version.** Acknowledge the October 1 repository manuscript, its exact two-sided certificate infimum and shared ramp/renewal mechanism. Distinguish our effective cardinality theorem and broader positive-capacity formulation without claiming a formal implication between the frameworks. Do not describe the general pair-level barrier as proved. This is sufficient reason for related-work attribution; no authorship allegation is supported.

**READ-based recommendation — other: qualify the internal October 2 G2 conclusion.** Preserve the dated search record but link this dossier as a correction to its earlier “no located limit” finding. Keep “bounded search” wording and distinguish commit dates from first public visibility. The original conjecture remains open. No mathematical change to R1's statement follows from the compared documents.

**READ-based recommendation — claim text and forum/X posture:** Retain R1's exact quantifiers. If the claim text is revised by the owner, spell out R2's actual regularity/positivity hypotheses and its fixed-kernel method scope, and add a short acknowledgment of the earlier certificate-limit manuscript. No immediate defensive or priority-based forum/X post is warranted. An optional factual acknowledgment reply could be proposed by the coordinator through the owner's normal approval gate; Akwei has already acknowledged our stronger cardinality bound. The fetched reply pages currently say new comments are suspended. No reply, contact, publication, deletion, or third-party repository action was performed.

### Replies sweep, as observed in this pass

| Evidence | Venue | Result with exact displayed timestamp where available |
|---|---|---|
| READ | [#30 ordinary thread][POST] | Nine visible nondeleted posts; latest is Akwei's 9295, Oct 5 15:04 site time. No separate ordinary post by us was visible, so no ordinary-thread reply to it can be identified. |
| READ / LIVE CLAIM | [#30 proof claim 386][CLAIM], [reply endpoint](https://www.erdosproblems.com/forum/proof-claims/386/comments) | **One third-party reply:** `johnakwei`, post **9297**, **Oct 5 17:23** site time, summarized in §3. No additional replies returned. Our claim is still listed and is the sole claim. |
| READ | [#708 thread](https://www.erdosproblems.com/forum/thread/708), [claim 262](https://www.erdosproblems.com/forum/thread/708/proof-claims#proof-claim-262), [reply endpoint](https://www.erdosproblems.com/forum/proof-claims/262/comments) | **None from a third party to our claim.** One claim comment exists: our own `chenhaoyu` update, post **8868**, **Sep 7 06:49** site time. Claim submission **Sep 5 13:45:59** site time. The sole ordinary post is Lech Mazur's unrelated wording comment, **May 6 22:28** site time. |
| READ | [#624 thread](https://www.erdosproblems.com/forum/thread/624#post-9183) | **None after/to our Sep 25 comment.** Our reply **9183**, `chenhaoyu`, **Sep 25 15:12** site time, appears under herong's **9091**, **Sep 18 19:30**. Older deleted/Bloom exchange is dated Aug 24, 2025. Zero proof claims. |
| READ | [#889 thread](https://www.erdosproblems.com/forum/thread/889) | **None to our work visible; no own post/claim visible.** Latest is KentaKitamura **9147**, **Sep 22 03:53**, about the capital-V variant; earlier LorenzoLuccioli **2704**, **Jan 3 15:40**, about a reduction. Zero proof claims. Both site time. |
| READ | [Our GitHub issues API](https://api.github.com/repos/chy4pro/automath/issues?state=all&per_page=100) | **None:** HTTP 200, empty array, no next-page link. This endpoint includes ordinary issues and PRs in the requested all-state listing. |
| READ / NOT ACCESSIBLE | [Our repository metadata](https://api.github.com/repos/chy4pro/automath), [Discussions](https://github.com/chy4pro/automath/discussions) | `has_discussions=false`; Discussions URL returns 404. No active Discussions venue; not a checked archive of past deleted discussions. |
| NOT ACCESSIBLE | [X v1][X1] and [replacement v2][X2] | Both direct requests return 404. **Replies unknown**, not “none”; live posting timestamps also unconfirmed. |

**READ — sweep boundary:** Full returned forum HTML, including nested posts, and lazy proof-claim comment endpoints were inspected; no next-page links appeared. Counts exclude deleted placeholders where the site's counter does. Private messages, deleted history and notifications behind login were not accessible. The sweep is a dated snapshot, not a monitor.

### Summary for the task comment

PARTIAL — Reading/comparison complete to the available-source boundary; exact forum UTC, X replies and live Zenodo metadata remain unconfirmed.

- READ: both 30-page PDFs fully read. October 1 commit `7e78435` already contains the exact two-sided smoothing-limit statement; October 5 was not its first located repository appearance.
- READ, comparison inference: our October 2 exact coefficient, `+1`, `N≥120^4` cardinality theorem is stronger than their reported `γ<0.942809522` certificate. The capacity and covering-certificate optimality theorems have different quantified objects; shared constant/ramp/renewal mechanism does not establish full subsumption.
- READ / LIVE CLAIM: Akwei's Oct 5 17:23 site-time reply acknowledges our stronger bound and promises a Zenodo citation. Current PDFs do not cite us. Claimed rational certificate vectors/verifier are absent; the general pair-relaxation equality remains a numbered conjecture.
- READ: no third-party replies on our #708/#624 material or thread #889; no GitHub issues; Discussions disabled. NOT ACCESSIBLE: X replies.
- Recommendation: acknowledge the October 1 manuscript in the next eligible related-work revision and qualify the earlier internal G2 absence finding. No immediate forum/X action. Coordinator owns disposition of this recommendation; no outward action was taken. A bounded search is not a global priority claim.
- Dossier: `/work/notes/G2_forum30_johnakwei_20261010.md`; identical selection copy: `/work/notes/selection/G2_forum30_johnakwei_20261010.md`.

### Sources and access accounting

**READ:** Required local documents were consulted first: R1, R2, `G2_FINAL_20261002.md`, `G2_SIDON_20261002.md`, prepared forum/X texts. The existing October 9 dossier and its preserved primary-source downloads were then reused. Both requested PDFs were freshly downloaded and hashes matched before the preserved extracts were read. The earlier E statement, immutable README and relevant GitHub metadata were also inspected. No global-memory tool/skill was available in the exposed catalog; no notice was invented or preset modified.

**NOT ACCESSIBLE / READ fallback:** Web-tool PDF retrieval failed (D: cache miss; L: unsupported `application/octet-stream`), but direct raw-content downloads succeeded, so neither PDF is an access gap. Zenodo v1 API returned 403. X statuses returned 404. Semantic Scholar returned 429. No access restriction was bypassed. Forum timezone/edit history remains unavailable. Source fetches and statuses are recorded in the run's JSONL ledger; all public requests were read-only.

**READ:** A durable copy of the 30-request direct-fetch ledger, with exact URLs and UTC request times, is [G2_forum30_johnakwei_20261010_access.jsonl](/work/notes/selection/G2_forum30_johnakwei_20261010_access.jsonl). The direct-fetch window was **19:16:41–19:18:31 UTC**. The four web-tool calls comprised four URL opens and seven search queries; failed parses and empty/nonmatching results supplied no additional mathematical evidence.

[D]: https://github.com/johnakwei/Science/blob/6b3299078de2dc1a837d3e51d6fa438300143eac/A_Data_Science_Analysis_of_Erdos_Problem_30.pdf
[L]: https://github.com/johnakwei/Science/blob/15609b5ab23a9b5abb4e37684ce5071c7fadb6e5/The_limit_of_vector-valued_smoothing_for_Sidon_sets.pdf
[E]: https://github.com/johnakwei/Science/blob/7e78435dd9692e6bc0d2635ec11a98078016a0ee/Sidon_smoothing_limit.pdf
[B]: https://github.com/johnakwei/Science/blob/7e78435dd9692e6bc0d2635ec11a98078016a0ee/Sidon_smoothing_barrier.pdf
[POST]: https://www.erdosproblems.com/forum/thread/30#post-9295
[REPLY]: https://www.erdosproblems.com/forum/thread/proof-claim:6342b22f36484ea28285c2c7d4ca288a#post-9297
[CLAIM]: https://www.erdosproblems.com/forum/thread/30/proof-claims#proof-claim-386
[EARLYCOMMIT]: https://github.com/johnakwei/Science/commit/7e78435dd9692e6bc0d2635ec11a98078016a0ee
[EARLYREADME]: https://github.com/johnakwei/Science/blob/9a0e39426400552f94925cb6945ddcc5a0aa239b/README.md
[R1]: https://github.com/chy4pro/automath/blob/302feebe0395cd6f8251b170c57843112670f472/problems/erdos30/SIDON_BOUND_PROOF.md
[R2]: https://github.com/chy4pro/automath/blob/11ff8676a7ba1791b5a0a3f5630793116cdfa336/problems/erdos30/KERNEL_OPTIMALITY.md
[MADEIROS]: https://www.erdosproblems.com/forum/thread/30#post-8482
[WU]: https://github.com/wustep/maths/blob/da2440b68979b78d201182118d30ca418e3c2001/problems/sidon-second-term/compute/q2/README.md
[ZENODO]: https://zenodo.org/records/23103980
[X1]: https://x.com/HaoyuChn/status/2106093758110728328
[X2]: https://x.com/HaoyuChn/status/2106224747545604507

**Cost — READ operational accounting:** approximately **10 minutes** for this run; **30 direct public fetches** (25 HTTP 200, one 403, three 404, one 429), plus **4 web-tool calls** (4 URL opens and 7 search queries). Prior primary-source downloads/extracts were reused after fresh PDF hash matching; prior-run fetches are not counted again. No proof experiments, solver runs, dependency installation or paid-cloud job. Task-specific monetary cost is not available.
