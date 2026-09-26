OPEN — neither the desired SE(1/20,1) estimate nor a usable conjugacy reduction has been established. A weaker BSG-dependent set-energy estimate is proved below. No new Zaremba constant is certified.

# R2 follow-up: set energy and class reduction

Task011, 2026-09-26. Branches A and B were assigned to separate agents and ran concurrently. This is ordinary literature-informed work, not a clean-room report. Root is assembling and checking the two outputs; STATUS remains the completion record. The normalization uses a=tau/6 for the all-coset exponent, unlike task009 where the symbol tau denoted that exponent itself.

## A. Exact missing estimate

Let G=SL2(F_p), D=|G|=p(p^2-1), n=|A|, and

    E(A)=#{(a,b,c,d) in A^4:ab^(-1)=cd^(-1)},
    alpha(A)=max_{x,H<G}|A intersect xH|/n.

All quadruples are ordered and the diagonal is included. The desired assertion is, for all nonempty symmetric A and all sufficiently large primes,

    E(A)/n^3 <= C[n^(-1/20)+alpha(A)+n/D],                   (A1)

with an absolute coefficient C. Branch A neither proved nor refuted this. The complete weaker replacement is

    E(A)/n^3 <= Cweak[n^(-1/1611)+alpha(A)^(1/11)+n/D].      (A2)

The coefficient Cweak is given explicitly below as a formula in two numerically unextracted constants of the symmetric growth theorem. This is a BSG-dependent deduction, not a removal of BSG.

## A.1. A weaker set estimate, with coefficient bookkeeping

Put K=n^3/E(A)>=1. Define the popular product set P by

    P={g:(1_A*1_A)(g)>n/(2K)}.

Then |P|<=2Kn. The contribution to energy outside P is at most n^3/(2K), so at least n^2/(2K) ordered pairs (a,b) have ab in P.

Apply Tao's weak BSG lemma (Lemma5.1) with graph parameters Kgraph=Kprime=2K and epsilon=1/16. Its bounds |V|>=n/(sqrt(2)Kgraph) and |D0|<=2(Kgraph Kprime)^2 n/epsilon give

    m=|V|>=n/(2sqrt(2)K),       |D0|<=512K^4 n,

and at least 15m^2/16 pairs (x,z) in V^2 satisfy xz^(-1) in D0. Root checked these displayed constants against the [primary statement](https://arxiv.org/html/math/0601431v3#S5).

Retain rows A0 with at most m/4 bad neighbors. Their number s is at least 3m/4>=n/(4K). For each x,y in A0 at least m/2 common good neighbors z give distinct representations

    xy^(-1)=(xz^(-1))(yz^(-1))^(-1).

Hence

    |A0 A0^(-1)| <= 2|D0|^2/m <= 2^19 K^8 n^2/s.

Set L=2^19 K^8(n/s)^2<=2^23 K^10. Then |A0 A0^(-1)|<=Ls.

Use the actual popular-difference set in Tao Proposition4.5:

    r(g)=|A0 intersect A0 g|,       S={g:r(g)>s/(2L)}.

The set S is symmetric, contains the identity, and has

    |S|>=s/(2L),
    sum_{g in S}r(g)>=s^2/(2L),
    |A0 S^j A0^(-1)|<=2^j L^(2j+1)s  (j>=1).              (A3)

The middle inequality follows by retaining at least half of sum r(g)^2>=s^3/L and using r(g)<=s. This retains the useful mass information of the source's construction.

Let u=2^(-26), v=2^188, w=2^162. Since a fixed conjugate of S^3 lies in A0 S^3 A0^(-1), (A3) yields

    |S|>=u n K^(-11),
    |S^3|/|S|<=16L^8<=vK^80,
    |S^3|<=8L^7s=2^136 K^56 n^14 s^(-13)<=wK^69 n.       (A4)

The last bound keeps s until the last step; replacing it prematurely by n would unnecessarily weaken the density exponent.

Let gamma>0 and s0>=1 denote constants such that every symmetric generating S with |S|>=s0 either has S^3=G or satisfies |S^3|/|S|>=gamma |S|^(1/20). This is the form of [Rudnev–Shkredov Theorem2](https://arxiv.org/html/1812.01671v3#S1) used here. Gamma and s0 have not been numerically extracted.

There are four cases:

1. |S|<s0 gives K^(-1)<=(s0/u)^(1/11)n^(-1/11).
2. If S lies in a proper subgroup H, then sum_{g in H}r(g)=sum_{xH}|A0 intersect xH|^2<=s max_{xH}|A0 intersect xH|. Equation(A3) forces alpha(A)>=uK^(-11), whence K^(-1)<=u^(-1/11)alpha(A)^(1/11).
3. If S generates and S^3!=G, then gamma(unK^(-11))^(1/20)<=vK^80. Therefore K^(-1)<=(v^20/(gamma^20 u))^(1/1611)n^(-1/1611).
4. If S^3=G, then D<=wK^69n, giving K^(-1)<=w^(1/69)(n/D)^(1/69).

Define

    C0=max{(s0/u)^(1/11), u^(-1/11),
           (v^20/(gamma^20 u))^(1/1611), w^(1/69)}.

These cases prove a bound with the three terms n^(-1/1611), alpha^(1/11), and (n/D)^(1/69), all multiplied by C0.

The fractional density term can be removed. If n<=p^(5/2), then

    (n/D)^(1/69)<=2^(1/69)p^(-1/138)<=2^(1/69)n^(-1/1611).

If n>=p^(5/2), Frobenius quasirandomness gives

    E(A)/n^3 <= n/D + D/(dmin n)
              <= n/D + 4p^(-1/2)
              <= n/D + 4n^(-1/1611),

where dmin>=(p-1)/2 and the last inequality follows from n<=p^3 and 3/1611<1/2. Consequently (A2) holds with

    Cweak=max{(1+2^(1/69))C0,4}.                             (A5)

No numerical onset is claimed without extracting gamma and s0. The argument nevertheless proves the displayed exponents with an absolute coefficient.

## A.2. Weighted transfer and the lower-cutoff repair

Suppose a general set estimate

    E(A)/|A|^3 <= C[|A|^(-eta)+alpha(A)^theta+|A|/D]

holds on all symmetric levels. For fixed h0>0,a>0 and

    0<c<min{eta h0/[2(1+eta)], theta a/(2+theta), 1/8},       (A6)

the dyadic argument proves, for all sufficiently large p,

    t(mu*mu)<=p^(-2c)t(mu)

under the all-coset bound p^(-a) and the extended energy range

    p^(-2-4c)<=t(mu)<=p^(-h0).                              (A7)

Here t denotes excess squared L2 mass. This extension is needed: the earlier target range ending at p^(-2+2c) alone stops before the Frobenius step has a polynomial spectral gain.

For a checkable derivation, put q=||mu||_2^2. On (A7), q<=2p^(-h0) and t>=q/2 for all sufficiently large p. Under failure of flattening, cut off values below delta=p^(-2c)q/32, and split the rest into at most Ldyad=ceil(log2(32p^3))+2 symmetric dyadic levels. This count is valid since q>=p^(-2-4c) and 2+6c<3. Schatten-four Minkowski, the low-tail bound, and the factor of two between dyadic endpoints give a level A of lower height Delta satisfying

    Delta^4 E(A)>q/Kdyad,       Kdyad=512 Ldyad^4 p^(2c).

Using Delta^2 |A|<=q, Delta |A|<=1, and E(A)<=|A|^3 yields

    (Kdyad q)^(-1)<|A|<Kdyad/q,
    E(A)/|A|^3>Kdyad^(-1),
    alpha(A)<=sqrt(Kdyad)p^(-a).

The density term now obeys |A|/D<=1024 Ldyad^4 p^(-1+6c). Multiplying the three set-estimate terms by Kdyad gives powers

    p^[2c(1+eta)-eta h0],  p^[c(2+theta)-theta a],
    p^(-1+8c),

times explicit logarithmic factors and fixed coefficients. All tend to zero under (A6), contradicting E(A)/|A|^3>Kdyad^(-1). This proves the extension; strict margins are necessary.

For (A2), the consequence is

    c<min{h0/3224, a/23, 1/8}.                              (A8)

At h0=1/10 and a=1/24 or 1/30, c=1/32241 is an admissible concrete choice. By contrast the unproved desired estimate(A1) would permit every c<1/420 at h0=1/10, subject to the other constraints. Neither statement certifies h0 for the actual initial walk.

## A.3. Conditional integration ledger

Assume an initial law mu0=(nu*check(nu))^{*m}, with m<=b log_N(p), has the required coset cap and t(mu0)<=p^(-h0). Here N is the interval length, not |G|. Define

    j=ceil((2-h0)/(2c))+1,       v=h0+2cj-2 in [2c,4c).

The extended range(A7) gives t(mu0^{*2^j})<=p^(-2-v). If an earlier iterate falls below the lower cutoff, ordinary L2 contraction preserves an even stronger bound. Coset non-concentration is preserved by convolution with a probability measure.

Frobenius gives s(nu)^(4m2^j)<=2p(p+1)p^(-2-v). Retaining an absolute coefficient in the incidence inequality permits

    kappa14=v/(4b 2^j).

For example its spectral coefficient is at most 3^(1/4) for p>=2; the projective-line main-term correction is absorbed in an absolute coefficient. With B_ledger.py's unchanged overhead OB=705672/25 and kappaC=kappa14/2, the conditional ledger is

    Fderived=j+log2(4b OB/v).                                (A9)

For comparison, mechanically substituting c into the default B convention gives

    Fdefault=ceil(1/c)+5+log2(6/c)+log2(OB).                  (A10)

At h0=1/10,b=1/4:

| Input | Hypothesis still needed | j | Default B log2 M | Derived exponent, same overhead |
|---|---|---:|---:|---:|
| c=1/32241 | Actual initial law and remaining assembly; weaker SE proved | 30630 | 32278.346353424 | 30658.691001595 |
| c=1/421 | Unproved SE(1/20,1), plus initial law and assembly | 401 | 452.087420976 | 423.432069147 |
| c=1/450 | Same unproved hypotheses | 429 | 481.183525744 | 451.013600742 |
| c=1/468 | Same unproved hypotheses | 446 | 499.240109272 | 468.169719944 |

For the first row v=21/322410 exactly. The limiting derived values as c approaches its strict ceiling are 30657.761346175 (c approaches1/32240) and, under(A1), 422.499027569 (c approaches1/420). These are unattained infima of conditional ledgers, not published or certified bounds for Zaremba. The strict epsilon<1/18 condition and all original assembly requirements remain.

## A.4. What this does not settle

A small structured portion of relative mass alpha contributes energy of order alpha^3, which is allowed by the alpha term in(A1). Thus the earlier Larsen–Pink substitution counterexample does not refute(A1). The inspected affine-incidence statements and varieties-energy results require different hypotheses; no theorem inspected supplies(A1) for arbitrary symmetric subsets of SL2. The fallback above is a valid weaker result, not evidence that the target c=1/468 is impossible.

## B. Class reduction

**Branch B status: OPEN.** The actual correlation measures, and every positive convolution power of them, are not conjugacy invariant. An explicit transfer using conjugacy-class majorants is proved below, but its required majorant bound fails at the initial integer-lift stages of both walks. Later powers remain an open possibility. No unconditional Zaremba bound follows from this branch.

Write \(G=\mathrm{SL}_2(\mathbf F_p)\), \(Q=|G|=p(p^2-1)\), \(Z=\{\pm I\}\), and
\[
E(\mu)=\|\mu\|_2^2-Q^{-1}.
\]
In task 011 the all-coset exponent is \(a=\tau/6\). Norms use counting measure, convolution is \((f*g)(x)=\sum_y f(y)g(y^{-1}x)\), and \(\widetilde f(x)=\overline{f(x^{-1})}\).

### B.1. The actual measures and the meaning of their powers

Put
\[
U(t)=\begin{pmatrix}1&t\\0&1\end{pmatrix},
\qquad
V(t)=\begin{pmatrix}1&0\\t&1\end{pmatrix}.
\]
For Lemma 14, the determinant-one set is
\[
s_j=V(2j)U(-2j)
=\begin{pmatrix}1&-2j\\2j&1-4j^2\end{pmatrix},
\qquad
\nu=N^{-1}\sum_{j=1}^N\delta_{s_j}.
\]
The normalized alternating-product counts are exactly
\[
\mu_r=(\nu*\widetilde\nu)^{*r}.
\tag{B1}
\]
Thus the source's \(r_{G,2r}/N^{2r}\) is \(\mu_r\), and subsequent dyadic stages are \(\mu_{r2^k}\). Here \(r\) counts alternating pairs, not individual generators. The notation \(G\) for the generating set in the source is separate from our notation for the ambient group. [MMS22, Lemma 4, equations (15)–(19)](https://arxiv.org/html/2212.14646v1).

For the original determinant-\(-1\) involutions
\[
g_j=\begin{pmatrix}-2j&1-4j^2\\1&2j\end{pmatrix},
\]
set
\[
w=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
D=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Direct multiplication gives \(g_j=ws_jD\), hence
\[
g_i g_j^{-1}=w(s_i s_j^{-1})w^{-1}.
\]
The even-step correlation walk on the original involutions is therefore the inner conjugate of (B1).

For Lemma 15, the matrices and normalized measures are
\[
h_{\alpha,\beta}=U(-\beta)gU(\alpha),
\qquad (\alpha,\beta)\in S\subseteq[N]^2,
\]
\[
\mu_r=(\nu_H*\widetilde\nu_H)^{*r},
\qquad
\nu_H=|H|^{-1}1_H,\quad
H=\{h_{\alpha,\beta}:(\alpha,\beta)\in S\}.
\tag{B2}
\]
They retain word multiplicities; they are not uniform measures on \((HH^{-1})^r\). [Girth-free paper, equations (9)–(17)](https://arxiv.org/html/2111.05751v1).

The inversion used in Corollary 16 has representative \(J=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), of determinant \(-1\). Its correlations nevertheless belong to \(G\). More generally, when all \(h\in H\) have the same nonzero determinant, right multiplication by one fixed matrix identifies \(H\) with a subset of \(G\) and preserves every product \(h h'^{-1}\). [Shkredov, Lemmas 14–15 and Corollary 16](https://arxiv.org/html/2603.14116v2).

### B.2. No positive power is conjugacy invariant

For every unitary irreducible representation \(\pi\), the Fourier transform of a correlation is
\[
\widehat{\mu_1}(\pi)
=\widehat\nu(\pi)\widehat\nu(\pi)^*
=:M_\pi,\qquad 0\le M_\pi\le I.
\]
The operator-norm upper bound follows because the Fourier transform of a probability measure is an average of unitary matrices. Also
\(\widehat{\mu_r}(\pi)=M_\pi^r\). The same identities hold after the fixed determinant-coset translation described above.

If \(\mu_r\) were conjugacy invariant, Schur's lemma would make every \(M_\pi^r\) scalar. A positive semidefinite matrix whose positive integer power is scalar is itself scalar: diagonalize it and take the unique nonnegative roots of its eigenvalues. Fourier inversion then proves
\[
\mu_r\text{ conjugacy invariant }
\Longrightarrow
\mu_1\text{ conjugacy invariant}.
\tag{B3}
\]

For the Lemma-14 walk, writing \(d=i-j\) gives
\[
s_i s_j^{-1}
=
\begin{pmatrix}
1+4jd&-2d\\
2d(1+4ij)&1-4id
\end{pmatrix}.
\]
Consequently every point in \(\operatorname{supp}\mu_1\) satisfies
\[
\operatorname{tr}(x)=2-x_{12}^{\,2}.
\tag{B4}
\]
Assume \(p\ge7\) and \(2\le N<p\). A pair \(i\ne j\) produces a support point with \(x_{12}\ne0\). Choose \(t\in\mathbf F_p^\times\) with \(t^4\ne1\); a degree-four polynomial has at most four roots, so such a \(t\) exists. Conjugation by \(\operatorname{diag}(t,t^{-1})\) preserves trace and changes \(x_{12}\) to \(t^2x_{12}\). The conjugate violates (B4), so lies outside the support. Thus \(\mu_1\) is not conjugacy invariant, and (B3) covers every \(r\ge1\).

For the Lemma-15 walk, suppose \(g_{21}=\gamma\ne0\), \(\det g=D_0\ne0\), \(N<p\), and \(|S|>N\), as required by its density hypothesis. The map from \(S\) to \(H\) is injective: the lower-right entry determines \(\alpha\), and the upper-left entry determines \(\beta\), because \(\gamma\ne0\). Direct multiplication yields
\[
\operatorname{tr}(h_{\alpha,\beta}h_{\alpha',\beta'}^{-1})
=
2-\frac{\gamma^2}{D_0}
(\alpha-\alpha')(\beta'-\beta).
\tag{B5}
\]
A nonidentity trace-two support point therefore arises only when \(\alpha=\alpha'\) or \(\beta=\beta'\). Its unique fixed point on \(\mathbf P^1(\mathbf F_p)\) belongs to
\[
T=\{\infty\}\cup
\{g\infty-\beta:\beta\in\operatorname{proj}_2S\},
\qquad |T|\le N+1<p+1.
\]
For \(\alpha=\alpha'\), the ratio is \(U(\beta'-\beta)\), fixing infinity. For \(\beta=\beta'\), it is a conjugate of \(gU(\alpha-\alpha')g^{-1}\) by \(U(-\beta)\), fixing \(g\infty-\beta\). These observations justify the fixed-point assertion.

There exists a nonidentity trace-two support point: \(|S|>N\) gives two pairs with the same \(\alpha\) and different \(\beta\). Since \(G\) acts transitively on \(\mathbf P^1\), a conjugate of this unipotent has its fixed point outside \(T\). By (B5), that conjugate is absent from the support. Hence \(\mu_1\) is not conjugacy invariant, and (B3) proves the assertion for every power.

These are exact obstructions to applying E1's central theorem directly, including at arbitrarily late powers. They do not imply that late powers cannot be quantitatively close to central.

### B.3. An exact class-majorant transfer and its loss

For a symmetric probability measure \(\mu\), define
\[
F(g)=\max_{x\in\operatorname{Cl}(g)}\mu(x),
\qquad
B(\mu)=\|F\|_1
=\sum_{\mathcal C}|\mathcal C|\max_{\mathcal C}\mu .
\]
The function \(F\) is the least nonnegative central pointwise majorant of \(\mu\), and
\[
B(\mu)=\inf\{L:\mu\le L\sigma,\quad
\sigma\text{ a central probability measure}\}.
\tag{B6}
\]
Indeed, any such inequality implies \(F\le L\sigma\) class by class, so \(B\le L\); equality is attained by \(\sigma=F/B\).

The following inequality is unconditional:
\[
\boxed{
E(\mu*\mu)
\le
\bigl[\mu(Z)+5B(\mu)p^{-1/2}\bigr]^2E(\mu)
+\frac{B(\mu)^2-1}{Q}.
}
\tag{B7}
\]

To prove it, \(F\) is symmetric and central, so
\(\widehat F(\pi)=z_\pi I\) with \(z_\pi\in\mathbf R\).
The precise group facts used are
\[
d_\pi\ge(p-1)/2\quad(\pi\ne1),
\qquad
|C_G(g)|\le2p\quad(g\notin Z).
\]
The possible noncentral centralizer sizes are \(p-1,p+1,2p\): they arise respectively from split semisimple, nonsplit semisimple, and noncentral repeated-eigenvalue elements. Character-column orthogonality gives
\[
|\chi_\pi(g)|^2\le\sum_\rho|\chi_\rho(g)|^2
=|C_G(g)|.
\]
Consequently
\[
\frac{|\chi_\pi(g)|}{d_\pi}\le5p^{-1/2}
\quad(g\notin Z,\ p\ge5).
\]
On the center use \(|\chi_\pi(g)|\le d_\pi\). Since \(F(Z)=\mu(Z)\), it follows that
\[
|z_\pi|\le\mu(Z)+5Bp^{-1/2}\qquad(\pi\ne1).
\tag{B8}
\]

Pointwise nonnegativity and \(\mu\le F\) give
\(r:=\mu*\mu\le F*F\).
Let \(M_\pi=\widehat\mu(\pi)\), which is Hermitian by symmetry. Plancherel now gives
\[
\begin{aligned}
\|r\|_2^2
&\le\langle r,F*F\rangle\\
&=\frac{B^2}{Q}
+\frac1Q\sum_{\pi\ne1}d_\pi z_\pi^2
            \operatorname{tr}(M_\pi^2)\\
&\le\frac{B^2}{Q}
+\bigl[\mu(Z)+5Bp^{-1/2}\bigr]^2E(\mu).
\end{aligned}
\]
Subtracting \(Q^{-1}\) proves (B7).

In particular, suppose
\[
\mu(Z)\le p^{-a},\qquad B(\mu)\le Cp^\beta,
\qquad \beta<\frac12,
\]
with fixed \(C\ge1\). For every
\[
0<c<\min\left\{a,\frac12-\beta\right\},
\tag{B9}
\]
equation (B7) proves the desired flattening throughout
\(E(\mu)\ge p^{-2+2c}\), for sufficiently large \(p\). An explicit sufficient onset condition is
\[
\left[
p^{-(a-c)}
+5C p^{-(1/2-\beta-c)}
\right]^2
+
\frac{C^2p^{-(1-2\beta)}}{1-p^{-2}}
\le1.
\tag{B10}
\]
To check the additive term, divide (B7) by
\(p^{-2c}E(\mu)\) and use
\[
Q\,p^{-2c}E(\mu)\ge
p(p^2-1)p^{-2}
=p(1-p^{-2}).
\]
This yields exactly the second term in (B10). The strict inequalities in (B9) ensure that both terms of (B10) tend to zero.

Thus a concrete missing special-walk estimate would be
\(B(\mu)\ll p^\beta\) with \(\beta<1/2\) along the necessary stages. This controls the central-subtraction error as well as the nontrivial Fourier term. It is stronger than merely saying that a central majorant exists.

### B.4. Obstructions at the initial stages

The smallest noncentral conjugacy-class size is
\[
m_{\min}=\frac{p^2-1}{2},
\]
by the centralizer sizes stated above. If a measure has support size at most \(R\), then
\[
B(\mu)\ge
\frac{p^2-1}{2R}\,[1-\mu(Z)].
\tag{B11}
\]
For each noncentral class,
\(\mu(\mathcal C)\le R\max_{\mathcal C}\mu\).
Sum this inequality and use \(|\mathcal C|\ge m_{\min}\) to obtain (B11).

For either walk let \(n=|\operatorname{supp}\nu|\). Its support contains no opposite pair \(h,-h\): the \(s_j\) have upper-left entry \(1\), while the \(h_{\alpha,\beta}\) have the same nonzero lower-left entry. Thus
\[
\mu_1(Z)=1/n.
\]
Moreover
\[
\mu_r(Z)\le\mu_1(Z)=1/n\qquad(r\ge1).
\tag{B12}
\]
Indeed, Fourier inversion gives
\[
\mu_r(Z)=\frac2Q
\sum_{\pi:\,\pi(-I)=I}d_\pi\operatorname{tr}(M_\pi^r).
\]
Every eigenvalue of \(M_\pi\) lies in \([0,1]\), so each summand decreases with \(r\). This also proves (B12) for determinant-coset walks after the fixed translation used in B.1.

For the MMS22 seed, \(n=N\) and
\(r\le(\tau/4)\log_Np\), with \(\tau=1/5\). The dyadic choice \(r=2^{l-1}\le m\) made in its sketch also obeys this upper bound. Counting words gives
\[
R\le N^{2r}\le p^{\tau/2},
\]
hence
\[
B(\mu_r)\ge
\frac{(1-1/N)(p^2-1)}{2p^{\tau/2}}.
\tag{B13}
\]
This is of order \(p^{19/10}\), uniformly up to an absolute positive coefficient for \(N\ge2\). For the appendix's alternative length
\(r\le\tau\log_Np\), \(\tau=1/4\), the same argument gives a lower bound of order \(p^{3/2}\). Neither permits the majorant hypothesis in (B9). This counting argument does not assume that the source's coset-cap normalization has independently been settled.

There is a further obstruction covering the longer integer-lift range of the girth-free walk.

**Integer-lift class bound.** Suppose the support of \(\mu\) consists of reductions of integer determinant-one matrices whose entries have absolute value at most \(L<p\). For every fixed \(\epsilon>0\), each conjugacy class meets the support in at most
\[
D_\epsilon p^{1+2\epsilon},
\tag{B14}
\]
where an explicit choice is
\[
C_\epsilon=
\prod_{\substack{q\ {\rm prime}\\q<2^{1/\epsilon}}}
(1-q^{-\epsilon})^{-2},
\qquad
D_\epsilon=30\,2^\epsilon C_\epsilon+50.
\]

First, the divisor function satisfies
\[
d(n)\le C_\epsilon n^\epsilon.
\tag{B15}
\]
For primes \(q\ge2^{1/\epsilon}\),
\(e+1\le2^e\le q^{\epsilon e}\).
For each remaining prime,
\[
(e+1)q^{-\epsilon e}
\le\sum_{j\ge0}(j+1)q^{-\epsilon j}
=(1-q^{-\epsilon})^{-2}.
\]
Multiplying over prime powers proves (B15).

A modular trace has at most five integer representatives in \([-2L,2L]\). For one such trace \(T\), write a candidate lift as
\[
\begin{pmatrix}x&b\\c&T-x\end{pmatrix}.
\]
Its determinant condition is
\[
bc=x(T-x)-1.
\]
There are at most \(2L+1\) choices of \(x\). Restrict to those for which the fourth entry also has absolute value at most \(L\). If the right side is nonzero, its absolute value is at most \(L^2+1\), and there are at most
\(2d(|x(T-x)-1|)\) ordered signed factor pairs. If it is zero, there are at most two choices of \(x\), and at most \(4L+1\) pairs with \(bc=0\). Summing over the five possible traces gives
\[
10C_\epsilon(2L+1)(L^2+1)^\epsilon+10(4L+1)
\le D_\epsilon L^{1+2\epsilon}.
\]
Every conjugacy class has a fixed modular trace. The number of distinct reductions is at most the number of these lifts, proving (B14).

Apply the intersection bound separately to each noncentral class, rather than applying the total-support bound (B11). It gives
\[
\boxed{
B(\mu)\ge
\frac{[1-\mu(Z)](1-p^{-2})}{2D_\epsilon}
\,p^{1-2\epsilon}.
}
\tag{B16}
\]
For the actual walks, (B12) makes \(1-\mu(Z)\ge1/2\).
Taking \(\epsilon=1/8\) yields \(B(\mu)\gg p^{3/4}\).
Allowing any fixed smaller \(\epsilon\) shows that no estimate
\(B(\mu)=O(p^\beta)\) with fixed \(\beta<1\) can hold throughout this lift regime.

The correspondence between the height bound and the walk length is explicit:

* For Lemma 14,
  \[
  s_i s_j^{-1}=V(2i)U(2(j-i))V(-2j).
  \]
  In an \(r\)-fold alternating correlation, adjacent \(V\)-factors merge, leaving exactly \(2r+1\) unipotent factors. Every parameter has absolute value at most \(2N\). The maximum row-sum norm is submultiplicative, and each factor has that norm at most \(2N+1\). Thus every entry is bounded by
  \[
  L\le(2N+1)^{2r+1}.
  \]
  For the MMS22 length \(1\le r\le(1/20)\log_Np\), use
  \(2r+1\le3r\) and \(2N+1\le N^3\) for \(N\ge2\), obtaining
  \[
  L\le N^{9r}\le p^{9/20}<p.
  \]
  Under the appendix's alternative length
  \(r\le(1/4)\log_Np\), the lift condition holds for \(N\ge16\), since \(2N+1<N^{4/3}\) gives
  \(L<N^{4r}\le p\).
  The explicit condition \((2N+1)^{2r+1}<p\) is retained whenever a different length convention is used.

* For the inversion form of Lemma 15,
  \[
  h_{\alpha,\beta}h_{\alpha',\beta'}^{-1}
  =U(-\beta)V(\alpha-\alpha')U(\beta').
  \]
  There are again exactly \(2r+1\) merged factors, now with parameters bounded by \(N\). Consequently
  \[
  L\le(2N)^{2r+1}.
  \]
  Here \(r=\ell\) exactly, so the source's condition
  \((2N)^{2\ell+1}<p\) is precisely the lift hypothesis in (B16).
  For \(g(x)=-1/x\), the lower-unipotent parameter changes sign, which does not affect this norm bound.

In particular (B16) applies to the longer inversion-walk measure in the girth-free argument, not just its shorter auxiliary escape measure. The statement for an arbitrary nonlinear \(g\) retains the explicit integer-lift hypothesis; no small-height claim for an arbitrary field-valued \(g\) is inferred without the needed conjugation and scaling.

### B.5. Central minorants at these stages

The largest nonnegative central function below \(\mu\) is
\[
F_-(g)=\min_{x\in\operatorname{Cl}(g)}\mu(x).
\]
Choose, for example, \(\epsilon=1/8\) in (B14).
For sufficiently large \(p\), its upper bound
\(D_\epsilon p^{5/4}\) is smaller than \(m_{\min}\).
Thus no noncentral class is fully contained in the lifted support, and \(F_-\) vanishes outside \(Z\). Therefore
\[
\|F_-\|_1=\mu(Z)\le1/n.
\]
Any normalized such minorant acts as the identity on every representation factoring through \(\mathrm{PSL}_2(\mathbf F_p)\), including the projective-line action. It provides no spectral saving.

More generally, if \(\mu\ge b\sigma\) for a central probability measure \(\sigma\) whose nontrivial Fourier operator norm is at most \(q_0\), write
\(\mu=b\sigma+(1-b)\eta\) with \(\eta\) a probability measure.
The triangle inequality and \(\|\widehat\eta(\pi)\|_{\rm op}\le1\) give
\[
\|\widehat\mu(\pi)\|_{\rm op}\le1-b(1-q_0).
\]
Obtaining a bound \(p^{-c}\) through this inequality requires
\[
b\ge\frac{1-p^{-c}}{1-q_0}.
\]
When \(q_0=o(1)\), this requires extracted central mass approaching one. The initial minorants above have small mass and are supported on the center.

### B.6. Conditional ledger and scope of the obstruction

Branch B supplies no exponent that can presently be inserted into the Zaremba argument. It rules out direct centrality and the required small-loss pointwise replacement at the initial stages. It does not rule out additional control of later powers, or a different argument exploiting character cancellation.

The inspected default B ledger is
\[
F_B(c)=
\left\lceil\frac1c\right\rceil+5+\log_2(6/c)
+14.784782051826808,
\]
where
\[
14.784782051826808
=\log_2(4\cdot39.6\cdot89.1\cdot2).
\]

A precise remaining special-walk hypothesis is: after \(b\) additional initial doublings, every required stage satisfies
\[
B(\mu)\le Cp^\beta,\qquad \beta<1/2,
\]
with fixed constants, and retains the certified central-mass bound
\(\mu(Z)\le p^{-a}\).
Then (B7) supplies a quantitative recurrence, and (B9)–(B10) prove flattening on the originally requested interval. This statement alone does not certify the full transition to a Frobenius saving. In particular, the original cutoff \(E(\mu)\ge p^{-2+2c}\) leaves an endpoint gap, as explained in Branch A. Branch A has separately proved an extended interval for its set-energy route; that extension is not automatically a theorem about the unproved class-envelope hypothesis.

Under the default ledger's integration normalization, formally charging \(b\) extra doublings adds \(b\) bits and gives \(F_B(c)+b\). For example, taking
\[
a=1/30,\qquad \beta=9/20,\qquad b=4,\qquad c=1/31
\]
obeys (B9) and gives
\[
F_B(1/31)+4=62.3239408629.
\]
**This is only a formal ledger value, contingent on the unproved later-stage envelope estimate and full integration, including the endpoint transition, the actual initial law, and the Corollary-16 assembly. It is not a Zaremba bound.** The initial MMS22 measure cannot satisfy this envelope estimate: (B13), with \(r\) replaced by \(r2^k\), excludes it through the first three subsequent doublings.

The proof above provides no claim that every possible use of a central majorant is impossible. It shows that the specific pointwise replacement needed for the proved transfer fails at the initial stages. Estimates using later powers or additional cancellation require new arguments.

### B.7. Checks and source scope

The primary texts checked were the arXiv versions linked in B.1 and the relevant displayed formulas in them. The final IMRN version of MMS22 was not read. The two source length conventions were kept separate, and each height bound was derived from its actual matrix factorization. The local task protocol, R2_E1, phase0/SUMMARY section 6, DESIGN, A_machinery_map, and B_ledger.py supplied the requested context; they were not treated as independent certification of the unresolved integration gates.

The finite-group and divisor-count arguments above are ordinary proofs, not kernel formalization. STOP was absent at the checks. No other clean-room reports were read, and no numerical job, dependency installation, git operation, or paid job was started for this branch. The displayed ledger arithmetic was evaluated from the inspected formula. No cost estimate is asserted.

## Combined conclusion

No unconditional improvement of \(M\) is established. Branch A proves a weaker set-energy estimate and its weighted transfer on an extended energy interval; its useful numerical applications still require the actual initial law and full integration. The desired stronger set-energy estimate remains unproved. Branch B proves that the actual walk powers are not conjugacy invariant and quantifies why the initial class-majorant/minorant replacement fails. A sufficient later-stage class-envelope estimate remains unproved. The numerical ledgers in this report are conditional or formal calculations with their hypotheses stated, not certified bounds for the original Zaremba problem.
