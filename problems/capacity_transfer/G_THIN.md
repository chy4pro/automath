PROVED — informed transfer proof. Stage A: PASS (all scale and scalar steps proved explicitly). This is a mathematical proof with finite exact checks, not a Lean formalisation or a novelty verdict.

# Sets with bounded nonzero difference multiplicity

## 1. Convention and explicit theorem

For a finite set \(A\subset\mathbb Z\), write

\[
 r_A(d)=\#\{(a,b)\in A^2:a-b=d\}.
\]

Fix an integer \(g\ge1\). The hypothesis here is \(r_A(d)\le g\) for every nonzero integer \(d\). Equivalently, \(|A\cap(A+d)|\le g\) for every \(d\ne0\). This is the \(g\)-thin convention of [Balogh–Füredi–Roy, Section 6](https://arxiv.org/html/2103.15850v2#S6). It concerns ordered **differences**, sometimes denoted \(B_2^-[g]\); it is not the sum-representation hypothesis called \(B_2[g]\). Negative differences have the same multiplicities as positive ones. Zero differences are unrestricted and number exactly \(|A|\).

**Theorem.** Let \(N,g\ge1\) be integers, with \(gN\ge120^4=207\,360\,000\). If \(A\subseteq\{1,\ldots,N\}\) has \(r_A(d)\le g\) for every \(d\ne0\), then

\[
 |A|<\sqrt{gN}+\frac{2\sqrt2}{3}(gN)^{1/4}+1.
 \tag{G1}
\]

This is uniform in \(g,N,A\); no fixed-\(g\) asymptotic assumption or condition \(g\le N\) is required. The non-strict version follows. A stronger diameter form holds: if \(D=\max A-\min A>0\) and \(gD\ge120^4\), replace \(N\) by \(D\) in \(G1\).

**Stage A verdict.** The scout's energy substitution is correct, and its stated theorem has integer parameter \(gN\). No substantive repair to item 3 is needed. Section 3 supplies the scalar algebra independently for real parameters as well, to make the full quantitative dependence explicit and avoid relying on a new combinatorial set with size parameter \(gN\). This note makes no assertion that the bound improves the current record; that requires the separate status review.

## 2. Energy reduction, with every scale specified

The kernel and its analytic proof are in [COMMON_CAPACITY.md, Lemmas 2–6](COMMON_CAPACITY.md):

\[
 f(t)=\begin{cases}\frac43-2|t|+\frac23|t|^3,&|t|\le1,\\0,&|t|>1.\end{cases}
\]

It is an autocorrelation, even, nonnegative, nonincreasing on \([0,\infty)\), of integral one, with \(a=f(0)=4/3\). For every \(L\ge1\), every positive measure \(\mu\) of mass \(k\) supported on \([0,L]\) satisfies

\[
 k^2\le\left(L+\frac23+200e^{-\alpha L}\right)E_f(\mu,\mu),
 \qquad \alpha=\log(4/3).
 \tag{G2}
\]

The common appendix proves this using a finite signed certificate \(\nu_L\), with \(f*\nu_L=1\) on the whole closed interval and \(E_f(\nu_L,\nu_L)\le L+2/3+200e^{-\alpha L}\). The identity \(E_f(\mu,\nu)=\langle h*\mu,h*\nu\rangle_{L^2}\) justifies Cauchy–Schwarz for signed certificates. Their positivity is neither asserted nor needed.

For every real \(T>0\), monotonicity and mass one give

\[
 2\sum_{d\ge1}f(d/T)
 \le2T\int_0^\infty f(t)\,dt=T.
 \tag{G3}
\]

Each summand is at most \(T\int_{(d-1)/T}^{d/T}f(t)\,dt\); compact support makes the sum finite.

Let \(k=|A|\) and put \(\mu=\sum_{a\in A}\delta_{(a-1)/T}\). For \(0<T\le N\), its support lies in \([0,N/T]\), and the exact ordered-pair expansion is

\[
 E_f(\mu,\mu)=\frac43k+2\sum_{d\ge1}r_A(d)f(d/T)
 \le\frac43k+2g\sum_{d\ge1}f(d/T)
 \le\frac43k+gT.
 \tag{G4}
\]

The diagonal term has coefficient \(4/3\), not \(4g/3\); only nonzero differences are multiplied by \(g\). Nonnegativity of \(f\) is essential to the majorization. Combining \(G2\) and \(G4\), and writing

\[
 S=gT,\qquad X=gN,\qquad L=N/T=X/S,
\]

gives

\[
 k^2\le\left(\frac XS+\frac23+200e^{-\alpha X/S}\right)
               \left(S+\frac43k\right),\qquad0<S\le X.
 \tag{G5}
\]

Every \(S\in(0,X]\) is permitted, since \(T=S/g\in(0,N]\). The same argument, translating by \(-\min A\), proves (G5) with \(X=gD\) when \(D>0\). Empty sets and singletons cause no difficulty in (G4) or (G1); the diameter refinement only concerns positive diameter.

## 3. A real-parameter scalar lemma

**Lemma.** Let \(X\ge120^4\) and \(k\ge0\) be real. Put \(x=X^{1/4}\), \(S=\sqrt2 x^3\). If \(G5\) holds at this \(S\), then

\[
 k<x^2+\gamma x+1,\qquad\gamma=\frac{2\sqrt2}{3}.
 \tag{G6}
\]

**Proof.** Since \(x\ge120>\sqrt2\), \(0<S\le X\) and \(L=X/S=x/\sqrt2\ge1\). Put \(\varepsilon=200e^{-\alpha x/\sqrt2}\). Expansion of \(G5\) gives \(P_\varepsilon(k)\le0\), with

\[
 P_\varepsilon(z)=z^2-\left(\gamma x+\frac89+\frac43\varepsilon\right)z
                   -x^4-\gamma x^3-\sqrt2\,\varepsilon x^3.
 \tag{G7}
\]

The integral representation of the logarithm gives \(\alpha\ge1/4\). Since \(\sqrt2\le3/2\), \(\alpha/\sqrt2\ge1/6\). The function \(x e^{-x/6}\) decreases for \(x\ge6\); hence for every real \(x\ge120\),

\[
 \varepsilon x\le24000e^{-20}<\frac{24000}{2^{20}}<\frac1{32}.
 \tag{G8}
\]

Here \(e>2\) by its positive series and \(24000\cdot32=768000<1048576=2^{20}\). Thus the error bound holds uniformly, not just at integral \(X\).

Set \(y=x^2+\gamma x+1\). Using \(\gamma^2=8/9\), direct expansion gives

\[
 P_0(y)=\frac{10}{9}x^2+\frac\gamma9x+\frac19\ge x^2.
 \tag{G9}
\]

Also \(\gamma<1\) and \(x\ge1\), so \(y\le3x^2\). Therefore

\[
 \varepsilon\left(\frac43y+\sqrt2x^3\right)
 <\frac1{32x}\left(4x^2+\frac32x^3\right)
 =\frac x8+\frac{3x^2}{64}\le\frac{11x^2}{64}.
 \tag{G10}
\]

It follows that \(P_\varepsilon(y)>53x^2/64>0\). This monic quadratic has strictly negative constant term, so it has exactly one positive root. Since \(k\ge0\) and \(P_\varepsilon(k)\le0\), that root is at least \(k\); since \(y>0\) and \(P_\varepsilon(y)>0\), it is less than \(y\). This proves \(G6\). No integrality of \(X,x,S,k\) was used. ∎

Apply the lemma to \(G5\) to prove \(G1\) and the stated diameter refinement.

For an explicit inverse form, if \(k\ge20366\), elementary counting of positive differences gives \(gD\ge k(k-1)/2\ge207376795>120^4\). Thus

\[
 gD>
 \left(\frac{\sqrt{4(k-1)+8/9}-2\sqrt2/3}{2}\right)^4.
 \tag{G11}
\]

This follows by solving \(k-1<y^2+\gamma y\) for \(y=(gD)^{1/4}\ge0\). It entails \(gD\ge k^2-(4\sqrt2/3)k^{3/2}+O(k)\), with an absolute error constant; \(G11\), rather than the asymptotic notation, is the fully explicit statement.

## 4. Verification scope

Run `node check_g_thin.js`. It uses no packages and checks all subsets of \(\{0,\ldots,11\}\) for \(1\le g\le4\), at integral and nonintegral rational scales, using exact BigInt kernel weights. It checks the difference-count and diagonal factors, the lattice majorant, the scale substitution on rational values (including nonintegral \(X\)), and every rational numerical constant in the scalar lemma. A negative control distinguishes difference-thinness from unordered sum multiplicity. These are finite arithmetic/combinatorial tests, not a computational proof of the common analytic lemma or an all-real search. No Lean check or literature-priority conclusion is claimed.

Actual run on 2026-10-02: exit 0, PASS; 4,096 subsets considered, 7,521 admissible set/parameter pairs, 60,168 weighted energy checks, 54 rational parameter substitutions, and all scalar rational certificates passed.
