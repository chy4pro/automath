DONE — isolated source audit completed; no fully numerical replacement Zaremba bound is certified below.

# F1 second audit: normalization, symmetry, and BSG constants

Date: 2026-09-26. Task: 012. Verdict on whether the appendix proves its printed numerical claim **as printed: NO**. This is a verdict on the displayed argument, not a disproof of the claimed mathematical bound.

The contraction scale is $K_*^{-c}$, not $p^{-c}$. The cited $1/20$ growth theorem requires symmetry, which the appendix's BSG output does not assert. The references inspected do not state the pair $(C_1,C_2)=(9,32)$; the TeX comments reveal the intended exponent calculation, but do not supply its missing noncommutative set inclusions. There is also an independent arithmetic error in the printed lower bound for $\kappa$.

**Smallest explicit final digit bound certified by this audit: none.** Numbers such as $2^{68913}$, $2^{77113}$, or the larger numbers below are conditional accounting outputs, not established replacement theorems. In particular, their coefficient and prime onset have not been certified.

## Scope and sources

I did not read `G0_gate_audit.md`, any R2 report, other research reports, or other agents' results. I independently fetched the public sources. Only the task, inbox protocol, required operating entry point, and tool/skill metadata were consulted locally. STOP was absent at the initial check and the subsequent check. No global-memory recall tool or skill was exposed by the metadata searches; no recall result or user notice is invented.

Sources actually inspected:

1. Shkredov, [arXiv:2603.14116v2, HTML](https://arxiv.org/html/2603.14116v2), especially equations (130)–(159), Theorems 38–39 and Lemma 40; also the [v2 TeX source](https://arxiv.org/src/2603.14116v2), `main.tex`, including its commented arithmetic.
2. Shkredov, [Russian Mathematical Surveys 76 (2021), 1065–1122](https://www.mathnet.ru/eng/rm10029), Theorem 49, equation (60), and its proof, printed pp. 1098–1101. The PDF links redirected/failed on direct opening; the relevant pages were read through the indexed primary-PDF text at [Math-Net](https://www.mathnet.ru/links/8c711726b638d3dc7bde8e3f220c0ad1/rm10029_eng.pdf). This access limitation is recorded rather than represented as a successful full-PDF download.
3. Moshchevitin–Murphy–Shkredov, [arXiv:2212.14646, §2](https://arxiv.org/html/2212.14646), equations (17)–(19).
4. Tao, [Product set estimates for non-commutative groups](https://arxiv.org/html/math/0601431), especially Proposition 4.5 and Lemma 3.4.
5. Tao–Vu, [Additive Combinatorics, primary book PDF](https://math.bme.hu/~gabor/oktatas/SztoM/TaoVu.AddComb.pdf), Lemma 2.13, Theorems 2.29 and 2.44, and the energy-to-graph argument of Lemma 2.30.
6. Murphy, [Group action combinatorics](https://arxiv.org/html/1907.13569), Lemma 12 and its provenance; its TeX source was also inspected.
7. Rudnev–Shkredov, [primary arXiv full text](https://arxiv.org/html/1812.01671), Theorem 2 in that rendering, and the [2022 publication record](https://doi.org/10.1112/mtk.12120). The appendix cites published Theorem 5. I verified the symmetry hypothesis and $1/20$ formula in the accessible full text; I did not independently verify the published theorem numbering behind Wiley's access page. The arXiv abstract metadata and rendered body differ on $1/21$ versus $1/20$, so the body theorem, not the abstract, is the source used here.

Source prose quotations are deliberately short. Displayed formulas below are the mathematical statements being audited; deductions are supplied independently.

## Q1. The unit of one flattening step

The decisive source display is survey equation (60):

\[
T_{2s}(f)\ll T_s(f)\,|A|^{2s}K_*^{-c}. \tag{S60}
\]

Set $R_s=T_s(f)/|A|^{2s}$, with the balanced function $f=1_A-|A|/|\mathbf G|$. Dividing (S60) by $|A|^{4s}$ gives

\[
R_{2s}\ll R_sK_*^{-c}. \tag{1}
\]

Thus the **squared** $L^2$ excess decreases by $K_*^{-c}$, up to the indicated constant. The $L^2$ norm itself decreases by $K_*^{-c/2}$. With the appendix's

\[
\tau=\frac14,\qquad K_*=p^{\tau/6},
\]

the squared-mass exponent gained per doubling is

\[
g=\frac{\tau c}{6}=\frac{c}{24}. \tag{2}
\]

If the initial normalized excess is at most $p^{-h_0}$, iteration yields $p^{-h_0-jg+o(1)}$ after $j$ doublings. Here $o(1)$ allows the fixed finite collection of implicit constants to be absorbed as $p\to\infty$; it does not provide a numerical onset.

The appearance of the target exponent 2 can also be derived. Plancherel and the nontrivial representation dimension $d_{\min}\asymp p$ give

\[
\|\widehat\nu(\rho)\|_{\mathrm{op}}^2
\leq \frac{|\mathrm{SL}_2(\mathbb F_p)|}{d_\rho}
       \|\nu-u\|_2^2
\ll p^{2-h}, \tag{3}
\]

where $u$ is uniform and $\|\nu-u\|_2^2\leq p^{-h}$. Crossing $h=2$ with a strict margin therefore suffices for the spectral step. A safe integer bookkeeping choice is

\[
\boxed{\quad k=\left\lceil\frac{2-h_0}{g}\right\rceil+1.\quad} \tag{4}
\]

The extra step gives positive room to absorb constants. It is not a formula for the unknown numerical prime threshold.

This reading agrees with MMS's dependence in (19). Its display is

\[
\sum_s F(s)\sum_{x\in B}B(sx)
\ll |B|\|F\|_1p^{-\delta}, \tag{M19}
\]

with $\delta=2^{-k-2}$ and $k\ll\log p/\log K(f)$. The source immediately requires balanced functions; (M19) is not true for an arbitrary uncentered positive $F$. In particular, the dependence on $\log p/\log K$ cannot be discarded when extracting an explicit constant.


A possible alternative interpretation is that the appendix silently redefines its numerical $c$ as a $p$-exponent after adapting the survey proof. No displayed $p$-scale flattening inequality with that numerical constant is supplied. The source equation (S60) cannot justify that interpretation merely by renaming $c$; this audit does not rule out a stronger direct lemma that would have to be proved separately.

### What can be used for $h_0$?

These possibilities must not be conflated:

* **$h_0=1/4$** is the formal collision-free $G^m$ starting-point calculation: $|G^m|=N^m=p^{\tau}$, and the uniform law then has squared norm $p^{-\tau}$. This requires identifying the actual measure with that uniform positive-word law and handling the integer word length. Neither the notation $G^m$ nor a coset bound alone proves that identification for the alternating convolution used by MMS. The corresponding numbers below are conditional on this stronger starting estimate.
* **$h_0=1/24$** follows directly from a normalized coset bound with $K=p^{1/24}$: apply it to singleton cosets to obtain $\|\nu\|_\infty\leq p^{-1/24}$, hence $\|\nu-u\|_2^2\leq\|\nu\|_2^2\leq p^{-1/24}$. MMS (17) provides this form of bound for its specified convolution. Its transfer to a differently chosen word length still has to be checked.
* **$h_0=0$** is the trivial probability-measure bound. It gives a conservative accounting row requiring no initial power saving in squared mass.

MMS prints $m=(\tau/4)\log_Np$, whereas the appendix prints $m=\tau\log_Np$. MMS also selects a dyadic word length before applying (19). These choices are not literally identical, and this audit does not silently equate their starting measures.

### Exact arithmetic if the appendix's claimed BSG pair is granted

The appendix displays

\[
c\geq\min\left\{\frac13,\frac1{8C_2},
\frac\tau{4C_2},\frac{c_H}{2(C_1+C_2)}\right\}=\frac1{1640}. \tag{A-c}
\]

For $C_1=9,C_2=32,c_H=1/20,\tau=1/4$, the four entries are exactly $1/3,1/256,1/512,1/1640$. Thus, **conditional on (A-c) being valid**, set $c=1/1640$; then $g=1/39360$.

The appendix further prints

\[
\delta=\frac c{2^{k+4}},\qquad
\log N\cdot\kappa=(6m)^{-1}\tau\delta\log p
=\frac\delta6\log N. \tag{A-extract}
\]

Keeping those extraction overheads exactly gives

\[
\kappa=\frac{1}{9840\,2^{k+4}},\qquad
\log_2\kappa^{-1}=k+4+\log_2(9840). \tag{5}
\]

The letter $\delta$ here is the appendix's spectral bookkeeping variable. It is not the density parameter $\delta$ in the second term $100\delta^{-60}$ of (157).

| Reading / initial estimate | $k$ | Exact $\log_2\kappa^{-1}$ | Decimal |
|---|---:|---|---:|
| Appendix's stipulated $\lceil1/c\rceil+1$ | 1641 | $1645+\log_2 9840$ | 1658.2644426002 |
| (S60), with $h_0=1/4$ | 68881 | $68885+\log_2 9840$ | 68898.2644426002 |
| (S60), with $h_0=1/24$ | 77081 | $77085+\log_2 9840$ | 77098.2644426002 |
| (S60), with $h_0=0$ | 78721 | $78725+\log_2 9840$ | 78738.2644426002 |

For example, $(2-1/4)39360=68880$, and $(2-1/24)39360=77080$, exactly. Even a hypothetical $p^{-c}$ contraction with $h_0=1/4$ would require $k=2871$ by the same criterion, not 1641. The first row is therefore the appendix's asserted arithmetic, not a separately validated spectral argument.

There is an additional numerical error already in that first row. Formula (5) does **not** give the printed $\kappa\geq2^{-1656}$. At the stated worst-case $c=1/1640$,

\[
\kappa=\frac{2^{-1645}}{9840}<2^{-1658},\qquad
\frac{2^{-1656}}{\kappa}=\frac{9840}{2048}=4.8046875.
\]

The safe integer lower bound from this arithmetic is $\kappa\geq2^{-1659}$. Rounding errors of this size are small compared with the missing normalization factor, but should still be corrected.

### What “$\log_2 M$” means, and the missing coefficients

There is **no unique exact $\log_2 M$ determined by the printed text**: (156) leaves $o_M(1)$ unspecified and (157) leaves $O(M_*)$ unspecified. Also, Theorem 8 uses $\mathcal M$ as the lower threshold for its parameter $M$, while its actual digit cap is $100M$. These are different quantities.

For a reproducible comparison, the following explicit *conditional* choice accounts for the printed horizon loss $N_*=N^{1/10}$, Theorem 38's factor 40, and a fixed admissible-looking $\varepsilon$. Take

\[
\varepsilon=\frac1{36},\quad
M_0=\left\lceil\frac{10}{\kappa\varepsilon}\right\rceil
=\left\lceil\frac{360}{\kappa}\right\rceil,
\quad M_*=40M_0. \tag{6}
\]

Why the factor 10 suffices for the main exponent comparison: put $\alpha=1-w_{M_0}$, $\beta=1-w_{M_*}$. Theorem 38 gives $\alpha\leq0.99/M_0$ and $\beta\leq\alpha/10$. The exponent of $p$ in $|A|N_*^{\kappa}$ is at least

\[
1-\alpha+2\varepsilon(\alpha-0.9\beta+0.1\kappa)
\geq1-\alpha+0.2\varepsilon\kappa>1.
\]

This proves a strict exponent margin for the displayed size-versus-error comparison. It does not quantify its multiplicative constants, the other geometric conditions, or the $o_M(1)$ in (156).

Ignoring only the bounded ceiling increment in (6), $M_*=14400\kappa^{-1}$. From (5),

\[
\log_2(14400\kappa^{-1})
=k+4+\log_2(141696000).
\]

Since $2^{27}<141696000<2^{28}$, the least dyadic upper power for $40\lceil360/\kappa\rceil$ in all these rows has exponent **$k+32$**. The ceiling increment, at most 40, is far below the gap to the next dyadic power. The explicit $100M_0$ cap from Theorem 8 instead has exponent **$k+33$**, since $2^{28}<354240000<2^{29}$.

| Reading | Conditional dyadic exponent for $M_*$ from (6) | Conditional dyadic exponent for $100M_0$ |
|---|---:|---:|
| Appendix's $k=1641$ | **1673** | **1674** |
| Correct scale, $h_0=1/4$ | **68913** | **68914** |
| Correct scale, $h_0=1/24$ | **77113** | **77114** |
| Correct scale, $h_0=0$ | **78753** | **78754** |

The first column reproduces the roughly 1673-versus-$7\cdot10^4$ comparison without representing it as a theorem. The appendix itself chooses 2000, not 1673; it does not print the choices in (6). If the actual digit conclusion is $C_{\mathrm{digit}}M_*$, the unknown factor contributes approximately $\log_2 C_{\mathrm{digit}}$ more bits. Setting that factor to 1 is an extra assumption.

## Q2. Symmetry and its quantitative cost

The accessible Rudnev–Shkredov theorem applies to a **symmetric generating set** $A\subseteq\mathrm{SL}_2(\mathbb F_p)$, with $|A|$ larger than an absolute constant. Its alternative is

\[
A^3=\mathrm{SL}_2(\mathbb F_p)
\quad\text{or}\quad K\gg|A|^{1/20},\qquad |A^3|=K|A|. \tag{RS}
\]

The appendix's Lemma 40 drops the symmetry hypothesis. The relevant set in the flattening proof is the translated BSG set $P_*\subseteq p_0^{-1}P$, not the original matrix family. Theorem 39 does not assert $P_*=P_*^{-1}$. A symmetric dyadic set $P$, if one has it, does not make an arbitrary subset of a translate symmetric.

The original family also is not symmetric: for the printed $g_j$,

\[
g_j^{-1}=\begin{pmatrix}1-4j^2&2j\\-2j&1\end{pmatrix}.
\]

For odd $p$ and $0<j<p$, its upper-left entry differs from the upper-left entry 1 of every $g_i$. This observation alone is not the BSG obstruction, but prevents confusing the different sets.

Here is an explicit sufficient symmetrization loss, derived using noncommutative Ruzsa triangle inequalities. Suppose $|B^3|\leq L|B|$, and put $n=|B|$. Then $|B^2|\leq Ln$, and

\[
|B^2B^{-1}|\leq\frac{|B^3|\,|B^{-2}|}{|B|}\leq L^2n,
\qquad |B^{-1}B^2|\leq L^2n.
\]

The second inequality follows by applying the first to $B^{-1}$ and taking inverses. Another triangle inequality gives

\[
|BB^{-1}B|\leq\frac{|B^2|\,|B^{-2}B|}{|B|}\leq L^3n.
\]

Taking inverses covers all eight sign patterns of length three. Thus $H=B\cup B^{-1}$ satisfies

\[
|H^3|\leq8L^3|B|\leq8L^3|H|. \tag{7}
\]

If an identity-containing version is desired, $H=B\cup B^{-1}\cup\{e\}$ gives the safe bound $27L^3|H|$. Consequently **a factor 3 in the tripling exponent is a proved sufficient loss**; optimality of that factor is not asserted.

Granting the appendix's BSG exponents, (7) replaces $C_2=32$ by 96 while retaining the size exponent $C_1=9$. The subset $B\subseteq p_0^{-1}P$ remains available for the subgroup-mass argument. Applying the same printed minimum conservatively with this replacement gives

\[
\min\left\{\frac13,\frac1{768},\frac1{1536},
\frac1{40(9+96)}\right\}=\frac1{4200}. \tag{8}
\]

This is **conditional arithmetic within that minimum formula**, not a proof that every hidden constant in the flattening argument has been accounted for. It is not necessary to multiply 1640 mechanically by 3: direct replacement gives 4200, while 4920 would be a further conservative degradation.

For $c=1/4200$, $g=1/100800$, and the extraction overhead retained from (A-extract):

| Reading | $k$ | $\log_2\kappa^{-1}$ | Conditional dyadic exponent for $M_*$ in (6) |
|---|---:|---:|---:|
| Appendix's stipulated $\lceil1/c\rceil+1$ | 4201 | $4205+\log_2 25200=4219.6211361133$ | **4234** |
| Correct scale, $h_0=1/4$ | 176401 | $176405+\log_2 25200=176419.6211361133$ | **176434** |
| Correct scale, $h_0=1/24$ | 197401 | $197405+\log_2 25200=197419.6211361133$ | **197434** |
| Correct scale, $h_0=0$ | 201601 | $201605+\log_2 25200=201619.6211361133$ | **201634** |

For the corresponding $100M_0$ cap, add 1 to the last column. These rows still assume the unverified original $(9,32)$ BSG assertion.

## Q3. What the BSG references give

Tao–Vu Theorem 2.29 is the additive statement. Its noncommutative counterpart is Theorem 2.44, with the same graph-level constants. Writing its two input parameters as $K_g,K'_g$, its displayed conclusions are

\[
|A'|\geq\frac{|A|}{4\sqrt2K_g},\qquad
|B'|\geq\frac{|B|}{4K_g},\qquad
|A'B'|\leq2^{12}K_g^4(K'_g)^3|A|^{1/2}|B|^{1/2}. \tag{TV}
\]

These control a product of **two refinements**, not a tripling set. Murphy Lemma 12 concludes

\[
|S|\gg(\alpha/K)^C|A|,\qquad
|S^3|\ll(K/\alpha)^C|S|,
\quad S\subseteq a^{-1}A, \tag{Mu}
\]

with an unspecified absolute $C$, citing Tao–Vu 2.44 and Tao Proposition 4.5. Murphy does not give 9 and 32 there.

For counting measure, the exact growth display in Tao Proposition 4.5 is

\[
|AS^nA^{-1}|\leq2^nD^{2n+1}|A|,\qquad n\geq1, \tag{T45}
\]

under $|AA^{-1}|\leq D|A|$, with $S=S^{-1}$ and $|S|\geq |A|/(2D)$. The order and inverse at the right endpoint are essential. Tao–Vu Lemma 2.13 is an additive precursor, not literally this noncommutative proposition.

The v2 TeX has these two arithmetic comments immediately below the claimed pair:

```tex
%(1,7) -> (1*2+1)*(7+1)+7+1
%|S| \ge |A_*|^2/(K^7 |A|) \ge |A|/K^9
```

They explain the intended calculation $3\cdot8+8=32$ and $2+7=9$. They do **not** establish the necessary set-theoretic transitions. In particular, (TV)'s $K^7|A|$ bounds $A'B'$, not $A'A'^{-1}$; and (T45) at $n=1$ bounds $ASA^{-1}$, not an arbitrary translated subset's positive cube. Neither inverse can be removed by commutativity in the setting under audit.

**Answer concerning $(9,32)$: not verified from the cited results.** The references supply (TV), (T45), and an unspecified polynomial conclusion (Mu). This does not prove that $(9,32)$ is false or unobtainable by a stronger argument; it means the claimed derivation has not been supplied.

### A fully reproducible, conservative replacement extraction

To show quantitatively what can be obtained without the disputed transitions, here is a direct consequence of the references. Let $n=|A|$, $K\geq1$, and use the quotient-energy convention

\[
E(A)=\sum_x r_{AA^{-1}}(x)^2\geq n^3/K.
\]

All representations are ordered; diagonal pairs are included. Thresholding at $n/(2K)$ gives a graph on $A\times A^{-1}$ with at least $n^2/(2K)$ edges and a product set of size at most $2Kn$: outside the threshold, the squared representation mass is at most $n^3/(2K)$; inside it, divide the remaining squared mass by the upper bound $n$ for each representation function. The product-set bound follows by dividing total mass $n^2$ by the threshold.

Apply (TV) with $K_g=K'_g=2K$. It yields $X\subseteq A,Y\subseteq A^{-1}$ satisfying the convenient weakened constants

\[
|X|\geq\frac n{16K},\quad |Y|\geq\frac n{8K},\quad
|XY|\leq2^{19}K^7n.
\]

Ruzsa's triangle inequality gives

\[
|XX^{-1}|\leq\frac{|XY|^2}{|Y|}\leq2^{41}K^{15}n.
\]

Set $a=|X|$, $D=|XX^{-1}|/a\leq2^{45}K^{16}$. Tao's proof takes

\[
S=\{s:|X\cap Xs|>a/(2D)\},\qquad S=S^{-1}.
\]

For completeness, its energy calculation proves more than just a cardinality lower bound. Since

\[
\sum_s|X\cap Xs|^2\geq a^3/D,
\]

the portion on $S$ is at least $a^3/(2D)$; each summand's underlying intersection is at most $a$. Hence

\[
\sum_{s\in S}|X\cap Xs|\geq a^2/(2D).
\]

Averaging over $x_0\in X$ supplies

\[
V=x_0^{-1}X\cap S,\qquad
|V|\geq a/(2D)\geq2^{-50}K^{-17}n.
\]

Here $e\in V$, $V\subseteq x_0^{-1}A$, and

\[
x_0V^3x_0^{-1}\subseteq XS^2X^{-1}.
\]

Using (T45) at $n=2$ gives the rigorous positive-cube estimate

\[
|V^3|\leq4D^5a\leq8D^6|V|
\leq2^{273}K^{96}|V|. \tag{9}
\]

Thus **$(C_1,C_2)=(17,96)$**, with the displayed coefficients, is one certified conservative replacement for the *non-symmetric translated-subset* statement. No optimality is claimed.

There is also a useful direct symmetric version. Put $W=V\cup V^{-1}\subseteq S$. Applying (T45) at $n=3$, and bounding $|S^3|$ by one of its conjugate copies inside $XS^3X^{-1}$, gives

\[
|W^3|\leq|S^3|\leq8D^7a\leq16D^8|W|
\leq2^{364}K^{128}|W|. \tag{10}
\]

Moreover $|W|\geq2^{-50}K^{-17}n$, and it retains the witness $V\subseteq x_0^{-1}A$, with $|V|\geq |W|/2$. This is sufficient to retain a translated subset for a subgroup-concentration contradiction. It does not assert that the whole symmetric set $W$ lies in a single translate of $A$.

For orientation only, substituting $C_1=17,C_2=128$ into the appendix's minimum gives $c=1/5800$. Formula (4) would then give $k=243601$ at $h_0=1/4$, or $k=272601$ at $h_0=1/24$; the conditional $M_*$ exponents from (6) are 243634 and 272634 respectively. This substitution has not been promoted into a certified flattening theorem: the displayed coefficients in (9)–(10), the dyadic decomposition constants, and the other steps must still be propagated.

## Q4. What is and is not certified

The appendix's final formula is

\[
\max\{O(M_*),\widetilde M\}
\sim\max\{10(\kappa\varepsilon)^{-1},100\delta^{-60}\}=O(1). \tag{A157}
\]

For its prime-only existence argument, the appendix chooses $\widetilde M=200$ and $M_*\geq40M$. These are useful explicit inputs. They do not turn the first $O(M_*)$, the admissibility condition $\varepsilon<1/18-o_M(1)$, or the finite-prime starting conditions into explicit inequalities by themselves.

The defects established in this audit are independent:

1. (S60) measures contraction in powers of $K_*$; the claimed number 1641 does not account for the exponent $\tau/6=1/24$, or specify a compatible initial-mass/target calculation.
2. The cited growth theorem's symmetry assumption is absent from the BSG invocation. Equation (7) gives a concrete repair with a quantifiable cost.
3. The pair $(9,32)$ is not supplied by the cited theorem statements or by the TeX arithmetic comments. Equations (9)–(10) provide a verified but worse alternative extraction.
4. Even accepting the appendix's step count and constants, its displayed $\kappa\geq2^{-1656}$ does not follow arithmetically.
5. The relation between an explicit spectral exponent and a complete final digit bound still has unverified coefficients, parameter admissibility, and prime onset.

Accordingly the honest answer is **NO, $\mathcal M=2^{2000}$ is not justified by the argument as printed**. The smallest explicit numerical digit bound that this source audit can certify with a complete derivation is **not determined**. The right output at this stage is a corrected conditional dependency calculation and a list of the specific missing estimates, not an unconditional replacement power of 2.

This audit proves the normalization arithmetic, the symmetrization estimate (7), and the conservative BSG extractions (9)–(10). It does not prove the full original conjecture, certify a numerical prime threshold, or perform kernel formalization. Arithmetic checks used exact integer formulas and JavaScript numerical evaluation; no new dependencies or paid cloud resources were used. No monetary cost was exposed by the tools.
