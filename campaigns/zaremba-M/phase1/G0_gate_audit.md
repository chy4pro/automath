OPEN

# G0 gate audit: explicit Zaremba constant

2026-09-26 UTC. Internal report to the existing coordinator. This is a source and mathematical audit, not a publication claim. No R2 explorer report was read. Global-memory was unavailable to the root session; no presets were changed. No dependency installation, SAT computation, cloud job, or external communication was performed.

## 1. Findings and verdict

| Flag | Result |
|---|---|
| F1, doubling normalization | **The appendix count is the optimistic reading.** Survey (60) decreases squared L2 mass by a power of `K_*`, not by the same power of `p`. With `K_*=p^(tau/6)`, the gain is `g=tau*c/6`. The literal count is `ceil((2-h0)/g)+1`, not `ceil(1/c)+1`. The precise conclusion and its qualifications are in Sections 3–5. |
| C6, symmetry | **The cited Rudnev–Shkredov theorem requires symmetry.** The translated BSG subset need not be symmetric. Standard symmetrization multiplies the tripling exponent by 3. The two sensitivity rows, 1/4200 and 1/1930, refer to different bookkeeping, as derived below. |
| F5, Lemma 14 versus Lemma 15 | **Repaired directly.** Simultaneous shifts and Cauchy–Schwarz derive Corollary 16 from Lemma 14 alone, with exponent `kappa_14/2` whenever `kappa_14<=1/2`. No quantitative Lemma 15 is needed for this step. See the complete proof in Section 6. |
| BSG exponents 9 and 32 | **Unverified.** The printed references do not directly supply this pair. The author's arXiv TeX comments reveal the intended arithmetic but do not prove its set inclusions. The concurrent N6 audit independently found the same issue. See Section 7. |
| 1673.05 | **Reproduced exactly as a conditional ledger value:** `1645+log2(1388762496/5)=1673.049224652...`. It assumes the optimistic count and the phase-0 overhead choices. It is not a certified theorem. |

**Verdict on the printed `2^2000` chain.** I cannot certify it from the sources checked. In the literal survey/MMS normalization, its displayed `c=1/1640` and `k=1641` do not fit together: the same `c` in (60) yields roughly 69,000–79,000 doublings for the illustrative initial entropies below. Independently, the growth citation has a symmetry hypothesis and the asserted BSG exponents remain unverified. The lost factor 6 in the numerical value of kappa is a small arithmetic error, and the Lemma-14/Lemma-15 integration issue has an elementary repair; neither fixes the doubling discrepancy. This is an implication gap in the audited numerical chain, **not a disproof of the existence theorem or of the numerical bound by some other argument**. The final IMRN version cited by the appendix remains unread. RB1/RB4 must check these findings before any external conclusion about the literature.

The task's request for a completely verified exact constant cannot honestly be fulfilled while these inputs are unverified. This report instead supplies the exact conditional function, an explicit reconstruction with stated hypotheses, and the failed implication. An unverified number is not promoted to a proved bound.

## 2. Sources actually inspected

All specified phase-0 files were read, including B's script. Those files are context, not independent verification.

* [Shkredov v2](https://arxiv.org/pdf/2603.14116v2): Lemmas 14–15, Corollary 16, Section 5.4 and Appendix; corresponding [arXiv source](https://arxiv.org/src/2603.14116v2) inspected in memory. Printed and commented-out material are distinguished below.
* [MMS22](https://arxiv.org/pdf/2212.14646): Lemma 4, (15)–(19), with the matching arXiv TeX. The revised **IMRN 2026 rnag048 text is unread**.
* [MMS18 v2](https://arxiv.org/pdf/1808.05845v2): Theorem 15 and proof, (24)–(38), the symmetrization inequality on printed p.18, and (48)–(55). These are the arXiv numbers.
* [Shkredov survey, journal record](https://www.mathnet.ru/eng/rm10029): primary PDF text for pp.1098–1100 was retrieved through indexed Math-Net excerpts, including (60)–(64) and the statement of Corollary 50. Direct PDF links redirected or timed out. **I did not obtain an independent full-PDF extraction or read the entire survey.** Phase-0 N1 has a fuller reading. The indexed formula typography occasionally loses superscripts, so the audit below relies on (60) and its explicitly displayed proof, not a guessed exponent in the theorem's typesetting.
* [Rudnev–Shkredov v3](https://arxiv.org/pdf/1812.01671v3): Theorem 2, Lemma 3, and the surrounding discussion. The Mathematika version's numbering was not independently checked.
* [Murphy](https://arxiv.org/pdf/1907.13569): Lemma 12 and its explanation. Its exponent is an unspecified absolute constant.
* [Tao, noncommutative product estimates, v3](https://arxiv.org/pdf/math/0601431v3): Proposition 4.5 and the energy BSG theorem/proof; the arXiv TeX was also read. [Tao's official errata](https://teorth.github.io/tao-web/additive-combinatorics.html) were checked.
* Tao–Vu book: the concurrent N6 worker directly inspected the book and communicated the relevant statements and discrepancies. **This G0 worker did not independently read that book PDF.** Its statements below are explicitly attributed to that audit.
* Helfgott 2008 PDF was opened, but its proof was not audited. Bourgain–Gamburd 2008 and Zhang v2 were not independently read for this task. Their results are not used here as independently verified quantitative inputs.

No numerical spectral experiment was run. Arithmetic below used exact integer/rational operations in JavaScript; decimals are final evaluations of logarithms, not interval-certified enclosures. Python3 is unavailable in this container.

## 3. F1: normalize the quantity before counting doublings

Write `G=SL_2(F_p)`, `n=|G|=p(p^2-1)`, and `d=(p-1)/2`. The quasirandomness ratio is exactly

\[
 Q_p=\frac nd=2p(p+1).                                      \tag{1}
\]

Let `nu` be the uniform measure on the determinant-one generator family, and put

\[
 \mu=(\nu*\widetilde\nu)^{*m},\qquad
 t_j=\|\mu^{*2^j}-u_G\|_2^2,
 \qquad t_0\le C_0p^{-h_0}.
                                                               \tag{2}
\]

The order in `nu*tilde(nu)` matters. Its Fourier matrices are positive semidefinite, so if `s` is the largest nontrivial singular value of convolution by `nu`, Plancherel gives

\[
 s^{4m2^j}\le Q_p t_j.                                      \tag{3}
\]

This also bounds the operator on the nonconstant part of the projective-line action. Its dimension-p representation would improve the constant in `Q_p`, but not the exponent 2. Multiplying the generator family by the fixed determinant-minus-one inversion matrix preserves the operator norm and gives the Lemma-14 family. Restricting indicator functions to `F_p` does not increase an L2 norm. Replacing the projective-line mean `|A||B|/(p+1)` by `|A||B|/p` costs at most `sqrt(|A||B|)/p`, harmless for all exponents used here and `N<=p`.

Survey (60), after division by the appropriate total masses, has the form

\[
 t_{j+1}\le D_j K_*^{-c_K}t_j.                              \tag{4}
\]

Here `t` is **squared** L2 mass. `D_j` includes the dyadic and absolute factors. For a fixed number of iterations it is at worst `p^{o(1)}` in the applications considered below. If `K_*=p^a`, then the squared-mass saving in powers of `p` is

\[
 g=a c_K,\qquad a=\tau/6.                                  \tag{5}
\]

Taking square roots changes the saving to `p^{-g/2}`. It does not remove `a`. In particular, the three quantities `c_K`, the squared-mass p-saving `g`, and an L2-norm p-saving are different.

Suppose for the moment that a stated `g>0` is rigorously available, with

\[
 t_j\le C_j p^{-h_0-jg}.
\]

For `v_j=h_0+jg-2>0`, (1)–(3) imply

\[
 s\le [2(1+1/p)C_j]^{1/(4m2^j)}
        p^{-v_j/(4m2^j)}.                                 \tag{6}
\]

Let `m<=b log_N p`. For fixed parameters and sufficiently large `p`, the prefactor can be absorbed by using half the exponent. Thus a conservative, explicit exponent is

\[
 \kappa_{14}=\frac{v_j}{8b\,2^j}.                         \tag{7}
\]

The absorbed coefficient changes the onset, which remains unspecified. If `C_j` is actually a known constant, it suffices that `2(1+1/p)C_j <= p^{v_j/2}`. This exhibits the exact role of that coefficient instead of silently setting it to 1.

### 3.1 Exact optimal count for a constant-gain certificate

Ignoring the already separated fixed prefactor, maximize

\[
 f(j)=\frac{h_0+jg-2}{2^j},\qquad j\in\mathbb Z_{\ge0}.
\]

For `h0<2`, comparison of consecutive terms shows

\[
 f(j+1)\ge f(j)\quad\Longleftrightarrow\quad h_0+jg-2\le g.
\]

One maximizing choice is therefore

\[
 \boxed{j_* = \left\lceil\frac{2-h_0}{g}\right\rceil+1},
 \qquad g\le v_{j_*}<2g.                                  \tag{8}
\]

When `(2-h0)/g` is an integer there is a tie with the next integer. This formula concerns what a specified certificate proves, not the actual spectral norm of the walk.

Combining (5) and (8) gives the requested literal-survey count:

\[
 \boxed{j_K(c_K,\tau,h_0)
   =\left\lceil\frac{6(2-h_0)}{\tau c_K}\right\rceil+1.}   \tag{9}
\]

For `tau=1/4`, `c_K=1/1640`, `g=1/39360`:

| Hypothesized/certified `h0` | `j_K` | Conditional `log2 M_B`, retaining the appendix prefactor |
|---:|---:|---:|
| 0 | 78,721 | 78,753.0492 |
| 1/24 | 77,081 | 77,113.0492 |
| 1/20 | 76,753 | 76,785.0492 |
| 1/8 | 73,801 | 73,833.0492 |
| 1/4 | 68,881 | 68,913.0492 |

Only the row `h0=a=1/24` follows immediately from a cap `mu(gH)<=p^{-a}` by taking `H={e}` and using `||mu||_2^2<=||mu||_infinity`. Larger `h0` requires a separately certified girth/return-probability input, with the correct walk length. The other rows are sensitivities, not assertions that all these entropies were proved for the appendix's chosen `m`.

The MMS22 convention has `tau=1/5`, `m=(tau/4)log_N p`, whereas the appendix writes `tau=1/4`, `m=tau log_N p`. These are distinct parameter assignments. Neither removes (5). Finite-length floors and choosing a nearby dyadic length also require slack; they cannot explain a factor approximately 40–50 in the count.

### 3.2 How MMS (19) is obtained, and what it does not say

The fully displayed MMS18 argument (51)–(55) takes `K^{c_K j}=p^3`, makes the measure's squared norm of order `p^{-3}`, uses the action estimate with factor `p`, and takes a `2^{j+1}`-th root. This yields

\[
 j\simeq\frac{3}{a c_K},\qquad \delta=2^{-j-2}.             \tag{10}
\]

Allowing initial entropy replaces the numerator 3 by `3-h0`, with strict slack for coefficients. With `a=1/24` and `c_K=1/1640`, the unslacked `h0=0` value is `118080`. Stopping just beyond the spectral threshold 2 gives (8), a real improvement over going all the way to entropy 3. It does **not** give 1641.

MMS22 (19) is a sketch of this mechanism. Its phrase about an arbitrary `F` cannot be a literal universal inequality: `F=delta_e` already fails. The following parenthetical requires balanced functions, and the actual input is a convolution with the nonconcentration hypotheses. Equations (2)–(7) specify this missing qualification explicitly. Also, the cap proved at length `2m` cannot be transferred to a shorter dyadic convolution merely by monotonicity; the first-stage lemma must be reapplied at that length, or a longer dyadic length must be used. This is another place where a fully numerical reconstruction needs its own length bookkeeping.

### 3.3 What would make 1641 valid?

The formula `ceil(1/c)+1` matches (8) if one has certified

\[
 g=(2-h_0)c.
                                                               \tag{11}
\]

For example, from `h0=0`, it is consistent with an L2-**norm** saving `p^{-c}`, hence a squared-norm saving `p^{-2c}`. That is much stronger than (4) at the same numerical `c`.

Alternatively one may define a normalized constant

\[
 c_{\rm normalized}=\frac{a c_K}{2-h_0}.
\]

Then `ceil(1/c_normalized)+1` is correct, but its numerical lower bound must be recomputed. Substituting `1/1640` for both constants is unjustified. No displayed estimate in the sources inspected makes that identification. The appendix count is therefore optimistic relative to the cited literal inequality. This conclusion does not rule out another, stronger flattening proof.

## 4. Reconstructing the flattening step with explicit exponent constraints

This section supplies a checkable conditional replacement for the unexplained minimum. It does not assume that the appendix's `c` has already been verified.

Assume a symmetric probability `mu` on `G` satisfies

\[
 \mu(xH)\le p^{-a}\quad(H<G),\qquad
 \|\mu-u_G\|_2^2\le p^{-h_0},\quad 0<a\le1.
                                                               \tag{12}
\]

Every convolution power inherits the cap. Young's inequality preserves the excess-norm upper bound. Assume the following translated BSG statement, keeping its coefficients visible:

\[
 E(P)\ge |P|^3/K_1\quad\Longrightarrow\quad
 B\subset x^{-1}P,\quad
 |B|\ge\alpha |P|K_1^{-C_1},\quad
 |B^3|\le\beta K_1^{C_2}|B|.                              \tag{13}
\]

Here `alpha,beta>0` are fixed constants. They have not been numerically extracted for the claimed `(9,32)` pair. Let the symmetric growth input have coefficient `gamma>0` and exponent `c_H`.

For `r=mu^{*L}-u_G`, set `t=||r||_2^2`, `t'=||r*r||_2^2`, and suppose

\[
 t'>p^{-g}t.                                              \tag{14}
\]

Quasirandomness gives `t'<=Q_p t^2`, so `t>p^{-g}/Q_p`. We have `||r||_1<=2`. Separate positive and negative dyadic levels above `p^{-10}`. They are symmetric because `r` is symmetric. The fourth-root energy is the normalized Schatten-4 norm of the Fourier matrices and obeys the triangle inequality. The tail has negligible norm compared with `(t')^{1/4}` when `g<1/3` and `p` is sufficiently large.

Consequently, for one level `P` and its lower height `Delta`, one may take

\[
 J=2\lceil10\log_2p\rceil+2,\qquad D=(4J)^4,
\]

and obtain

\[
 t'\le D\Delta^4 E(P),\qquad
 \Delta^2|P|\le t,\qquad \Delta|P|\le2.                   \tag{15}
\]

The extra 2 in `J` safely covers endpoints of the decomposition. All tail assertions concern only an unspecified sufficiently large onset; no finite-prime assertion is being made here.

Equations (14)–(15) now give, without suppressing the dyadic factor,

\[
 E(P)\ge\frac{|P|^3}{4D p^g},\quad K_1=4D p^g,            \tag{16}
\]
\[
 \Delta|P|\ge D^{-1/2}p^{-g/2},\qquad
 |P|\ge D^{-1}p^{h_0-g},\qquad
 |P|\le16D Q_p p^{2g}\le64D p^{2+2g}.                    \tag{17}
\]

For example, the lower size bound follows from `t p^{-g}<D t^2|P|`; the mass bound follows from `t p^{-g}<D(Delta|P|)^2t`. These are the two estimates that determine the exponents, rather than an arbitrary substitution into the printed minimum.

Apply (13). For the standard symmetry repair put `X=B union B^{-1} union {e}`. Write `sigma=3` for this repair; `sigma=1` would require a genuinely applicable nonsymmetric growth theorem with the asserted exponent. The following three cases explain all constraints.

**Growth case.** If `B` generates `G` and `X^3!=G`, standard symmetrization and growth give

\[
 \gamma |B|^{c_H}\le27\beta^3 K_1^{3C_2}.
\]

Together with (13) and (17), the p-exponent on the opposing side is

\[
 h_0c_H-g\{3C_2+c_H(1+C_1)\}.                            \tag{18}
\]

It is positive, and hence contradicts (14) for sufficiently large `p`, if

\[
 g<\frac{h_0c_H}{3C_2+c_H(1+C_1)}.                       \tag{19}
\]

To see explicitly where the unspecified coefficients go, the contradiction follows once

\[
 p^{h_0c_H-g[3C_2+c_H(1+C_1)]}
 >\frac{27\beta^3}{\gamma\alpha^{c_H}}
   4^{3C_2+C_1c_H}D^{3C_2+c_H(1+C_1)}.
                                                               \tag{20}
\]

**Whole-group case.** If `X^3=G`, the upper tripling estimate and the upper bound in (17) contradict one another provided

\[
 g<\frac1{3C_2+2}.                                      \tag{21}
\]

For example a sufficient finite condition is
`p^{1-(3C2+2)g} > 3456 beta^3 4^{3C2} D^{3C2+1}`.

**Subgroup case.** If `B subset H<G`, the mass on `xH` is at least `Delta|B|`. On the other hand

\[
 \sum_{y\in xH}|r(y)|\le p^{-a}+|H|/n\le3p^{-a}.          \tag{22}
\]

The last bound uses `index(H)>=d+1`, which follows from the nontrivial permutation representation on `G/H`; it does not require inspecting each subgroup in Dickson's list. Thus (13) and (17) contradict (22) if

\[
 g<\frac{a}{C_1+1/2}.                                   \tag{23}
\]

A sufficient finite condition is
`p^{a-g(C1+1/2)} > 3 alpha^{-1}4^{C1}D^{C1+1/2}`.

These calculations prove the following conditional exponent statement:

\[
 \boxed{0<g<\Gamma_\sigma:=
 \min\left\{\frac13,
 \frac{h_0c_H}{\sigma C_2+c_H(1+C_1)},
 \frac{a}{C_1+1/2},
 \frac1{\sigma C_2+2}\right\}.}                           \tag{24}
\]

For standard symmetrization `sigma=3`; its constants were displayed above. For `sigma=1` the same exponent algebra applies only under the stronger growth input. The first term `1/3` is convenient slack in this presentation, not a claim that it is sharp. For rational inputs choose, for instance, a specified rational `eta in (0,1)` and `g=(1-eta)Gamma_sigma`. **Strict inequality matters:** a power of `log p` cannot be absorbed while retaining an exponent exactly at a critical endpoint. The statement that it “only changes q0” is correct only after retaining a positive power margin.

Thus (24) is an explicit rational exponent function under the stated inputs; the onset is not explicit because `alpha,beta,gamma` are not explicit here. The entire `(9,32)` substitution remains conditional until (13) is established with that pair. This distinction prevents the reconstructed lemma from being misreported as a fully effective theorem.

## 5. C6: precise symmetry loss

Rudnev–Shkredov Theorem 2 assumes a symmetric generating set of sufficient size. Its exponent is `c_H=1/20`. Murphy's translated BSG subset is not asserted to be symmetric. Symmetry of the level set `P` does not imply symmetry of `B subset x^{-1}P`.

The standard conversion, explicitly quoted in MMS18 p.18 from Helfgott's growth survey, is

\[
 |(B\cup B^{-1}\cup\{e\})^3|
 \le\left(3\frac{|B^3|}{|B|}\right)^3|B|.                \tag{25}
\]

Thus a tripling exponent `C2` becomes `3C2`. Since `|X|>=|B|` and `|X|<=3|B|`, the remaining multiplicative constants are absolute. The cardinality threshold in the RS theorem is eventually satisfied in the growth case of Section 4, because (19) forces the lower bound for `|B|` to be a positive power of `p`.

For `h0=a`, divide (19) by `a`: the sharp K-scale critical exponent is

\[
 c_{K,\rm sym}^{\rm crit}
 =\frac{c_H}{3C_2+c_H(1+C_1)}=\frac1{1930}
 \quad(C_1=9,C_2=32,c_H=1/20).                            \tag{26}
\]

The slack formula instead gives

\[
 \frac{c_H}{2(C_1+3C_2)}=\frac1{4200}.                   \tag{27}
\]

Without the symmetry loss, the analogous sharp critical value is `1/650`. All three are conditional on the BSG pair. A rigorous use of a critical value such as (26) takes a strictly smaller exponent, for example `1/1931`, or explicitly retains the logarithmic losses.

If one **also** imposes the appendix's optimistic count, (26) and (27) yield the phase-0 illustrative log values `1963.2841` and `4234.4059`, respectively. This confirms the arithmetic interpretation of both sensitivity rows. Neither row solves F1. Under the literal K-scale count with `h0=a=1/24`, the sharp endpoint `1/1930` would require `90711` doublings; a strict choice `1/1931` requires `90758`.

The cited theorem therefore does not validate Lemma 40 as printed for arbitrary nonsymmetric sets with exponent `1/20`. This audit has not proved that such a stronger theorem is false; it has proved that the stated citation and the automatic symmetry conversion do not give it.

## 6. F5: a complete Lemma-14-to-Corollary-16 repair

Work in `F_p`, and define inverse only on nonzero elements. Let

\[
 C(A,B)=\#\{(a,b)\in A\times B:ab=1\}.
\]

Equivalently `C(A,B)=<1_A,J1_B>`, where `(Jf)(x)=f(x^{-1})` for `x!=0` and `(Jf)(0)=0`. This operator has L2 norm at most 1, so there is no projective-line main-term ambiguity in the following argument.

Suppose `A=[N] dotplus Lambda_1`, `B=[N] dotplus Lambda_2`, with injective sums, and assume Lemma 14 with exponent `kappa_14>0` and coefficient `C_14`. For an integer `t>=0`, the interval boundary bound and the disjoint representations give

\[
 |A\triangle(A+t)|\le2t|\Lambda_1|=2t|A|/N,
\]

and likewise for `B`. This remains valid when translates wrap modulo `p`, by bounding each interval's boundary separately. The triangle inequality and the contraction property of `J` imply

\[
 |C(A+t,B+t)-C(A,B)|
 \le2\sqrt{2t/N}\sqrt{|A||B|}.                           \tag{28}
\]

For `1<=j<=H`, set `t=2j`. Lemma 14 is exactly a bound on the average of `C(A+2j,B+2j)`, and translations preserve both cardinalities. Averaging (28) therefore yields

\[
 \boxed{\left|C(A,B)-\frac{|A||B|}{p}\right|
 \le\left(C_{14}H^{-\kappa_{14}}+4\sqrt{H/N}\right)
       \sqrt{|A||B|}.}                                  \tag{29}
\]

Take `H=floor(sqrt N)`. For `N>=4`, `H>=sqrt N/2`, so

\[
 \left|C(A,B)-\frac{|A||B|}{p}\right|
 \le (2^{\kappa_{14}}C_{14}+4)\sqrt{|A||B|}
       N^{-\min(\kappa_{14}/2,1/4)}.                    \tag{30}
\]

The finitely many smaller `N` can be absorbed in the coefficient. Thus for `0<kappa_14<=1/2`,

\[
 \boxed{\kappa_C=\kappa_{14}/2.}                         \tag{31}
\]

Every exponent in the proposed constant chain is in this range. This proves the exact halving used by B's ledger **without using Lemma 15**. Optimizing `H` in (29) instead gives `kappa_C=kappa_14/(1+2kappa_14)` with a changed absolute coefficient. That modest optimization is unnecessary to reproduce the ledger, so (31) is retained.

This is an elementary integration repair. It neither computes the missing Lemma-15 exponent nor repairs a wrong Lemma-14 exponent. It applies for arbitrary injective interval unions, with no density assumption.

## 7. BSG constants: what is checked and what is still missing

Murphy's Lemma 12 has an unspecified exponent. Tao's Proposition 4.5 starts from `|AA^{-1}|<=L|A|` and gives a symmetric `S` with

\[
 |S|\ge |A|/(2L),\qquad
 |AS^nA^{-1}|\le2^nL^{2n+1}|A|.                         \tag{32}
\]

This formula was independently read. It does not itself state the pair `(9,32)` for a subset of a translate of the original high-energy set.

The Shkredov v2 TeX comments after Theorem 39 contain the arithmetic

`(1,7) -> (1*2+1)*(7+1)+7+1`

and a proposed lower cardinality of order `|A|/K^9`. These are unpublished comments in the source, not a displayed proof. They indicate the intended use of a subset `A'` of size roughly `|A|/K` with difference set at most roughly `K^7|A|`, so `L` would be of order `K^8`.

There is a concrete inclusion issue. If `T=S intersection a^{-1}A'`, then the `n=1` quantity in (32) controls

\[
 TT T^{-1}\subset a^{-1}A'SA'^{-1}a,
\]

but it does not automatically control `T^3`. The `n=2` estimate does give

\[
 T^3\subset a^{-1}A'S^2,
 \qquad |T^3|\le4L^5|A'|.                               \tag{33}
\]

Using the standard popular-intersection choice `|T|>=|A'|/(2L)` then gives `|T^3|<=8L^6|T|`, producing exponent 48 rather than 32 under that *conditional* `L=K^8` input. This locates what extra argument would be needed; it is not a counterexample to Theorem 39.

The N6 worker additionally checked the Tao–Vu book: Lemma 2.13 is an abelian lemma; the noncommutative graph theorem is 2.44, with related statements 2.41–2.46. Tao's official errata correct powers in Theorem 2.29 and explicitly warn that Lemma 2.41 does not imply the old Corollary 2.42 as written. The revised statement uses Proposition 4.5. These facts mean that edition and product order must be specified when extracting exponents.

Tao's arXiv v3 energy BSG theorem has product exponent 8. The N6 audit derives a fully sourced but much weaker translated pair `(19,108)` from it and (32); G0 has not substituted that fallback into a Zaremba theorem. The safe status of the requested pair is **UNVERIFIED**, not “verified by Murphy” and not “false.”

## 8. Exact rational ledger and the value 1673.05

Use distinct names: `M_0` is the initial continued-fraction alphabet, `M_*` the enlarged alphabet, and `B_final` the resulting partial-quotient bound. The Appendix's calligraphic threshold and Theorem 8's `100M` output should not be silently identified.

Let the overhead tuple be

\[
 \mathcal O=(\varepsilon,r,u,\ell,R,s_C,b),
\]

where `N=p^{2 epsilon}`, `N_*=N^{1/r}`, `1-w_M<=u/M`, `M_*>=R M_0`, the final conversion is bounded by `ell M_*`, and `kappa_C=kappa_14/s_C`. For the phase-0 B reading,

\[
 r=10,\ u=99/100,\ \ell=4,\ R=198/5,
 \ s_C=2,\quad \varepsilon\uparrow1/18.                  \tag{34}
\]

The source locations are Section 5.4's `N_*` and positivity condition, Theorem 38's dimension bounds, Lemma 10's factor 4, and (31) above. The ratio `R=198/5` is the exact solution of `10(99/100)/R<=1/4`; the appendix rounds it up to 40.

The sufficient exponent inequality is

\[
 1-w_{M_0}<\frac{2\varepsilon\kappa_C}{r},\qquad
 M_0>\frac{ur s_C}{2\varepsilon\kappa_{14}}.              \tag{35}
\]

The associated real-valued threshold is

\[
 B_{\rm thr}
 =\ell\max\left\{R\max\left(1000,
 \frac{ur s_C}{2\varepsilon\kappa_{14}}\right),200\right\}.
                                                               \tag{36}
\]

The `200` is the appendix's prime-denominator choice; it is not the unrelated delta-assumption term `100 delta^{-60}`. Once the inverse-gap term dominates, define

\[
 O_B=\frac{\ell Rur s_C}{2\varepsilon}.
\]

At the limiting values (34),

\[
 O_B=4\cdot\frac{198}5\cdot\frac{891}{10}\cdot2
 =\frac{705672}{25},\qquad
 \log_2O_B=14.7847820518268\ldots.                         \tag{37}
\]

### 8.1 General function using a correctly normalized certificate

Given rational `c_K,tau,h0`, set `a=tau/6`, `g=a c_K`; alternatively choose rational `g<Gamma_sigma` from (24), with its BSG hypotheses. Put

\[
 j=\left\lceil\frac{2-h_0}{g}\right\rceil+1,
 \qquad v=h_0+jg-2,
 \qquad \kappa_{14}=\frac{v}{8b2^j}.
\]

Then (36), including its maxima, is the exact-rational threshold function. In the inverse-gap regime its logarithm is

\[
 \boxed{F_{\rm cert}
 =j+\log_2\left(\frac{8b O_B}{v}\right).}                \tag{38}
\]

All ceilings and the argument of the logarithm are exact rationals/integers. `log2` of a rational is generally not rational, so “exact-rational log2 M” is interpreted as this exact symbolic form followed by a decimal display. Formula (24) specifies how `C1,C2,c_H` and the symmetry choice enter `g`; `tau,h0` enter separately. This prevents a hidden change of normalization in the function requested by the task.

For integer alphabets and strict inequalities, fix a rational `epsilon<1/18` compatible with all retained assembly conditions and take

\[
 M_0=\max\left\{1000,
 \left\lfloor\frac{ur s_C}{2\varepsilon\kappa_{14}}\right\rfloor+1\right\},
\quad M_*=\lceil R M_0\rceil,
\quad B_{\rm final}=\ell\max\{M_*,200\}.                 \tag{39}
\]

The phase-0 value at `epsilon=1/18` is an infimum in this ledger, not an attained endpoint. Moreover, Section 5.4 contains further `o_M(1)`/earlier assembly conditions. Unless their exact finite-M margin is extracted, (36)–(39) are a conditional overhead ledger, **not a complete new end-to-end certification**. Using a concrete smaller epsilon, for example `1/20`, costs only `log2(10/9)` bits in this ledger; checking the remaining assembly inequalities is still required.

### 8.2 Reproducing the appendix/B reading

Now deliberately impose the appendix's equations, without asserting that they have been proved:

\[
 c_{\rm app}=\min\{1/3,(8C_2)^{-1},\tau/(4C_2),
 c_H/[2(C_1+C_2)]\},
\]
\[
 k_{\rm app}=\lceil1/c_{\rm app}\rceil+1,\qquad
 \kappa_{14}=c_{\rm app}/(6\,2^{k_{\rm app}+4}).            \tag{40}
\]

Their exact B-ledger function is

\[
 \boxed{F_{\rm app}=k_{\rm app}+4+
   \log_2(6O_B/c_{\rm app}).}                            \tag{41}
\]

For `(C1,C2,c_H,tau)=(9,32,1/20,1/4)`, the minimum is `1/1640`, and

\[
 \begin{aligned}
 k_{\rm app}&=1641,\\
 \log_2(1/\delta)&=1645+\log_2 1640
                   =1655.6794801\ldots,\\
 \log_2(1/\kappa_{14})&=1645+\log_2 9840
                   =1658.2644426\ldots,\\
 B_{\rm thr}&=2^{1645}\frac{1388762496}{5},\\
 F_{\rm app}&=\boxed{1673.049224652053\ldots}.
 \end{aligned}                                         \tag{42}
\]

Thus the appendix's `2^{-1656}` lower bound belongs to delta, not to `delta/6`. This is the exact lost factor 6.

Replacing only `k_app` by the literal count (9) in (41) gives the numerical sensitivity table in Section 3. For `b=tau` and `v=g`, (38) is one bit smaller than that table; the appendix prefactor is conservative once the corrected count is supplied. The difference of one bit has no bearing on the normalization failure.

For clarity, the symmetry sensitivity values are:

| Input for optimistic (41) | Value |
|---|---:|
| `c=1/1640` | 1673.049224652 |
| `c=1/1930` | 1963.284129685 |
| `c=1/4200` | 4234.405918165 |
| `c=1/650` | 681.714040460 |

The last row is nonsymmetric sharp bookkeeping under a growth hypothesis not supplied by RS. The middle sharp row is a critical endpoint and still needs a small strict loss. None is an unconditional theorem.

## 9. Reproducible arithmetic and disposition

The following small JavaScript calculation is the arithmetic performed in this audit; the mathematical inputs are in the numbered displays above. It writes no files and uses no external package.

```javascript
const gcd = (a,b) => b ? gcd(b,a%b) : a;
const Q = (n,d=1n) => { const z=gcd(n,d); return [n/z,d/z]; };
const sub = ([a,b],[c,d]) => Q(a*d-c*b,b*d);
const div = ([a,b],[c,d]) => Q(a*d,b*c);
const ceil = ([a,b]) => (a+b-1n)/b;
const log2Q = ([a,b]) => Math.log2(Number(a))-Math.log2(Number(b));
const O = Q(705672n,25n);
const Fapp = d => Number(d+5n) + Math.log2(Number(6n*d)) + log2Q(O);
console.log(Fapp(1640n)); // 1673.0492246520535
for (const h of [Q(0n),Q(1n,24n),Q(1n,20n),Q(1n,8n),Q(1n,4n)]) {
  const j=ceil(div(sub(Q(2n),h),Q(1n,39360n)))+1n;
  console.log(h.map(String).join('/'),String(j),
    Number(j+4n)+Math.log2(9840)+log2Q(O));
}
```

**Gate disposition:** F5 is closed by (28)–(31). C6's citation question is closed affirmatively, with the quantified repair (25)–(27). F1 is resolved at the level of what the literal cited inequality yields: (9), not the appendix count. A stronger source/proof could still repair the numerical claim, so the campaign's end-to-end G0 gate remains **OPEN**. BSG `(9,32)` and the final cited journal version are the remaining source checks; hidden assembly/onset constants must remain visible. No original conjecture, fully effective threshold, or improved Zaremba bound is claimed.
