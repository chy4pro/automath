PROVED — informed transfer proof. Stage A: PASS-WITH-REPAIRS (real scope parameter justified, and an unnecessary additive loss removed). No novelty verdict or new Lean formalisation is asserted.

# Difference triangle sets: an explicit scope lower bound

## 1. Model and theorem

Let \(n,k\ge1\) be integers. A normalized \((n,k)\) difference triangle set consists of \(n\) rows

\[
 X_i=\{0=a_{i0}<a_{i1}<\cdots<a_{ik}\}\subset\mathbb Z,
 \qquad1\le i\le n,
\]

such that all differences \(a_{ij}-a_{ij'}\), over all rows \(i\) and all \(j\ne j'\), are nonzero and mutually distinct. Equivalently all positive within-row differences, over all rows, are distinct. There is no condition on differences formed between marks from different rows. The scope is \(m=\max_i a_{ik}\); \(m(n,k)\) is the smallest possible scope. These are the conventions of [Chee–Colbourn, Introduction](https://arxiv.org/pdf/0712.2553). They are ordinary integer differences, not differences modulo a code length.

**Theorem.** For every integer \(n\ge1\) and \(k\ge20365\),

\[
 \boxed{
 m(n,k)>
 n\left(\frac{\sqrt{4k+8/9}-2\sqrt2/3}{2}\right)^4.
 }
 \tag{D1}
\]

The non-strict version also holds. This improves the scout's proposed right side by removing its unnecessary \(-1\). In particular,

\[
 m(n,k)\ge n\left(k^2-\frac{4\sqrt2}{3}k^{3/2}
                           +\frac{16}{9}k-2\sqrt k\right)
 \qquad(k\ge20365).
 \tag{D2}
\]

Thus the claimed \(k^{3/2}\) coefficient is obtained with an explicit lower-order term, uniform in \(n\).

**Stage A verdict.** The summed energy reduction is valid. However, applying a theorem stated only for integer interval parameters to \(X=(m+1)/n\) is not justified without redoing the scalar proof for real \(X\). Section 3 does that explicitly. Also, the actual interval \([0,m]\) already supports the analytic lemma, so \(X=m/n\) can be used and the scout's final \(-1\) is dispensable. The exact onset \(20365\) is checked in Section 4. This does not assert any new result for cyclic optical codes without a separate equivalence proof, or compare against a current literature record.

## 2. Summing row energies without introducing cross-row differences

Let \(K=k+1\). The shared analytic input, proved completely in [COMMON_CAPACITY.md, Lemmas 2–6](COMMON_CAPACITY.md), uses

\[
 f(t)=\begin{cases}\frac43-2|t|+\frac23|t|^3,&|t|\le1,\\0,&|t|>1,\end{cases}
 \qquad \alpha=\log(4/3),\qquad
 C(L)=L+\frac23+200e^{-\alpha L}.
\]

The kernel is even, nonnegative, nonincreasing on \([0,\infty)\), of integral one, and is an autocorrelation with \(f(0)=4/3\). For any positive measure \(\mu\) of mass \(K\), supported on \([0,L]\), \(L\ge1\), the common lemma gives

\[
 K^2\le C(L)E_f(\mu,\mu).
 \tag{D3}
\]

The proof uses a finite signed measure of potential one on the closed interval; the autocorrelation inner product gives Cauchy–Schwarz for that signed measure. It does not require a positive equilibrium measure.

Fix any real \(T\in(0,m]\), set \(L=m/T\ge1\), and define separate measures

\[
 \mu_i=\sum_{j=0}^k\delta_{a_{ij}/T}\qquad(1\le i\le n).
\]

Each row has mass \(K\) and support in \([0,L]\). Summing \(D3\) over rows gives

\[
 nK^2\le C(L)\sum_{i=1}^n E_f(\mu_i,\mu_i).
 \tag{D4}
\]

Each row contributes exactly \(K\) diagonal ordered pairs. By global uniqueness of positive within-row differences and nonnegativity of \(f\),

\[
 \sum_i E_f(\mu_i,\mu_i)
 \le\frac43 nK+2\sum_{d\ge1}f(d/T)
 \le\frac43 nK+T.
 \tag{D5}
\]

The last estimate holds for every real \(T>0\): sum the inequalities \(f(d/T)\le T\int_{(d-1)/T}^{d/T}f(t)\,dt\) and use evenness and mass one. Compact support makes the sum finite. In particular there is just one lattice-sum budget \(T\), because differences are unique across all rows. We never replace the sum of row energies by the energy of the union; doing so would introduce uncontrolled cross-row terms. Marks such as the \(n\) copies of zero are also kept in their respective row measures.

Write

\[
 S=T/n,\qquad X=m/n,\qquad L=X/S.
\]

Divide \(D4\)–\(D5\) by \(n\). For every real \(0<S\le X\),

\[
 K^2\le\left(\frac XS+\frac23+200e^{-\alpha X/S}\right)
              \left(S+\frac43K\right).
 \tag{D6}
\]

The variable \(X=m/n\) is generally nonintegral. All scales remain valid: \(T=nS\le nX=m\).

## 3. Scalar algebra for arbitrary real \(X\ge120^4\)

Put \(x=X^{1/4}\), \(S=\sqrt2x^3\), \(\gamma=2\sqrt2/3\), and \(\varepsilon=200e^{-\alpha x/\sqrt2}\). If \(x\ge120\), then \(S\le X\) and \(L=x/\sqrt2\ge1\). Expansion of \(D6\) says \(P_\varepsilon(K)\le0\), with

\[
 P_\varepsilon(z)=z^2-\left(\gamma x+\frac89+\frac43\varepsilon\right)z
                   -x^4-\gamma x^3-\sqrt2\,\varepsilon x^3.
 \tag{D7}
\]

We have \(\alpha\ge1/4\) by integrating \(1/t\ge3/4\) on \([1,4/3]\), and \(\sqrt2\le3/2\). Thus \(\varepsilon x\le200x e^{-x/6}\). The right side decreases for \(x\ge6\), so, for all real \(x\ge120\),

\[
 \varepsilon x\le24000e^{-20}<24000/2^{20}<1/32.
 \tag{D8}
\]

The last step is the exact integer comparison \(24000\cdot32=768000<1048576\); \(e>2\) follows from its series.

Set \(y=x^2+\gamma x+1\). Since \(\gamma^2=8/9\),

\[
 P_0(y)=\frac{10}{9}x^2+\frac\gamma9x+\frac19\ge x^2.
\]

Since \(\gamma<1\), we also have \(y\le3x^2\) for \(x\ge1\). Hence

\[
 \varepsilon\left(\frac43y+\sqrt2x^3\right)
 <\frac1{32x}\left(4x^2+\frac32x^3\right)
 \le\frac{11x^2}{64}.
\]

Consequently \(P_\varepsilon(y)>53x^2/64>0\). The quadratic is monic and its constant term is strictly negative; it has one positive root. From \(K\ge0\), \(P_\varepsilon(K)\le0\), and \(y>0\), \(P_\varepsilon(y)>0\), we conclude

\[
 K<\sqrt X+\gamma X^{1/4}+1.
 \tag{D9}
\]

This proof uses no integrality of \(X\) or \(K\).

## 4. Onset, inversion, and an explicit remainder

There are exactly \(n\binom{k+1}{2}\) positive within-row differences. They are distinct integers in \(\{1,\ldots,m\}\), so

\[
 X=m/n\ge\frac{k(k+1)}2.
 \tag{D10}
\]

The onset calculations are

\[
 \frac{20364\cdot20365}{2}=207356430<207360000=120^4,
\]
\[
 \frac{20365\cdot20366}{2}=207376795>207360000.
\]

Since \(k(k+1)/2\) is increasing for \(k\ge0\), every \(k\ge20365\), independently of \(n\ge1\), satisfies \(X\ge120^4\). The preceding integer \(20364\) does not ensure this from counting alone; this is an exact audit of this sufficient onset, not a minimal-onset claim for the theorem.

Using \(K=k+1\), \(D9\) gives \(k<x^2+\gamma x\). This function is strictly increasing for \(x\ge0\), so

\[
 x>z:=\frac{\sqrt{4k+\gamma^2}-\gamma}{2}>0.
\]

Raise to the fourth power and multiply by \(n\): \(m=nx^4>nz^4\). This proves \(D1\) for each configuration and hence for the minimum scope. In particular the scout's weaker \(-1\) version is valid.

Here is a bound on the remainder that uses no unspecified asymptotic constants. The relation \(z^2+\gamma z=k\) gives

\[
 z^4=k^2+\gamma^2 k-\gamma(2k+\gamma^2)z.
\]

Concavity of the square root, or squaring its nonnegative right side, gives

\[
 z=\sqrt{k+\gamma^2/4}-\gamma/2
 \le\sqrt k-\gamma/2+\frac{\gamma^2}{8\sqrt k}.
\]

Substitute this upper bound into the preceding identity (its coefficient is negative). For \(k\ge1\),

\[
\begin{aligned}
 z^4
 &\ge k^2-2\gamma k^{3/2}+2\gamma^2 k
       -\frac{5\gamma^3}{4}\sqrt k+\frac{\gamma^4}{2}
       -\frac{\gamma^5}{8\sqrt k}\\
 &\ge k^2-2\gamma k^{3/2}+2\gamma^2 k-2\sqrt k.
\end{aligned}
\tag{D11}
\]

For the final step, \(0<\gamma<1\) and \(1/\sqrt k\le\sqrt k\), so the two negative remainder terms have magnitude at most \((5/4+1/8)\sqrt k<2\sqrt k\), while \(\gamma^4/2\ge0\). Using \(2\gamma=4\sqrt2/3\), \(2\gamma^2=16/9\) proves \(D2\). All constants and quantifiers are explicit. ∎

## 5. Verification scope

Run `node check_difference_triangles.js`. It uses dependency-free BigInt arithmetic for the exact onset, real-parameter substitution on nonintegral rational examples, and scalar numerical certificates. It exhaustively checks normalized rows of up to four marks in scopes \(m\le9\), and compatible families of at most three such rows: positive-difference counting, all diagonal contributions, and the summed energy majorant at integral and nonintegral rational scales. Negative controls distinguish internally Golomb rows from families with globally disjoint differences. The finite tests do not certify all parameter values; the analytic lemma, monotonic estimates and algebra above provide that proof. No new Lean check, cyclic-code transfer, or current-record claim is made.

Actual run on 2026-10-02: exit 0, PASS; 687 compatible family instances (including 210 with three rows), 4,122 weighted energy checks, 72 rational substitutions (54 with nonintegral \(m/n\)), and both exact onset comparisons passed.
