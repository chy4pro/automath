PROVED — informed transfer proof, with explicit onset. Stage A: PASS-WITH-REPAIRS. This is a mathematical proof with finite exact checks, not a Lean formalisation or a novelty verdict.

# Weak Sidon sets: an explicit capacity bound

## 1. Statement, convention, and adversarial verdict

A finite set of integers is **weak Sidon** if the sums of its unordered pairs of distinct elements are all different. Diagonal sums are excluded from this definition. This is the convention in [Balogh–Füredi–Roy, Section 5](https://arxiv.org/html/2103.15850v2#S5).

**Theorem.** For every integer \(N\ge90^4=65\,610\,000\) and every weak Sidon set \(A\subseteq\{1,\ldots,N\}\),

\[
 |A|<\sqrt N+\sqrt{\frac83}\,N^{1/4}+2.
 \tag{W1}
\]

In particular the non-strict version holds, uniformly over all such sets. No assertion about an optimal coefficient or a current literature record is made here.

The scout's main coefficient survives. Three repairs are needed:

1. The sentence in scout Section 3.2 claiming that both cross-sum pairs consist of distinct elements is false precisely in the allowed three-term progression case. The proof below splits off that diagonal case before applying weak sum uniqueness.
2. The bound \(|P|\le k-2\) is used only for \(k\ge2\). Empty sets and singletons are treated separately.
3. The claimed onset \(90^4\) was only scanned. Section 4 proves it for every real \(N^{1/4}\ge90\), using monotonicity and an exact rational exponential certificate.

## 2. Analytic input and lattice estimate

Use

\[
 h(t)=2(1-t)\mathbf1_{[0,1]}(t),\qquad
 f=h*\widetilde h,
 \qquad
 f(t)=\begin{cases}\frac43-2|t|+\frac23|t|^3,&|t|\le1,\\0,&|t|>1.\end{cases}
\]

The complete proof of the following input, including the signed certificate, is in [COMMON_CAPACITY.md, Lemmas 2–6](COMMON_CAPACITY.md). The kernel is even, nonnegative, decreasing on the positive half-line, has mass one and \(a=f(0)=4/3\). If \(L\ge1\) and a finite positive measure \(\mu\) of mass \(k\) is supported on the closed interval \([0,L]\), then

\[
 k^2\le C(L)E_f(\mu,\mu),\qquad
 C(L)=L+\frac23+200e^{-\alpha L},\quad \alpha=\log(4/3).
 \tag{W2}
\]

Here \(E_f(\mu,\nu)=\iint f(x-y)\,d\mu(x)d\nu(y)\). This follows from an explicitly constructed finite **signed** measure \(\nu_L\) with \(f*\nu_L=1\) on \([0,L]\) and \(E_f(\nu_L,\nu_L)\le C(L)\). Autocorrelation gives \(E_f(\mu,\nu)=\langle h*\mu,h*\nu\rangle_{L^2}\), so Hilbert-space Cauchy–Schwarz applies to that signed certificate. No positivity of \(\nu_L\), or identification with a positive equilibrium measure, is assumed.

For every real \(T>0\), monotonicity gives

\[
 2\sum_{d=1}^{\infty}f(d/T)
 \le 2T\int_0^\infty f(t)\,dt=T.
 \tag{W3}
\]

Indeed \(f(d/T)\le T\int_{(d-1)/T}^{d/T}f(t)\,dt\), and the sum is finite because \(f\) is compactly supported.

## 3. Repeated differences and the exact diagonal cost

Write \(k=|A|\) and

\[
 r(d)=\#\{(x,y)\in A^2:x-y=d\}\qquad(d>0).
\]

Suppose \(r(d)\ge2\). Choose two different lower endpoints \(p<q\), so \(p,p+d,q,q+d\in A\). The identity

\[
 (p+d)+q=(q+d)+p
\]

has a right-hand pair of distinct elements. Unless \(q=p+d\), its left-hand pair also has distinct elements. These two unordered pairs cannot agree: \(q+d\) is strictly larger than both \(p+d\) and \(q\). Thus weak Sidon uniqueness forces \(q=p+d\). The two representations are exactly the adjacent edges of the progression \(p,p+d,p+2d\).

Three distinct lower endpoints \(p<q<r\) are impossible: applying the same argument to \((p,q)\) and \((p,r)\) would give both \(q=p+d\) and \(r=p+d\). Hence \(r(d)\le2\).

Let \(P=\{d>0:r(d)=2\}\). Each \(d\in P\) determines a unique progression and its middle element. Distinct \(d,e\in P\) cannot have the same middle element \(z\), since the distinct off-diagonal pairs \(\{z-d,z+d\}\) and \(\{z-e,z+e\}\) would have the same sum \(2z\). Each middle element is different from both the minimum and maximum of \(A\). Consequently,

\[
 |P|\le k-2\qquad(k\ge2).
 \tag{W4}
\]

Translate \(A\) by \(-1\), and put \(\mu=\sum_{a\in A}\delta_{(a-1)/T}\), where \(0<T\le N\). Its support lies in \([0,N/T]\). All \(k\) diagonal ordered pairs remain in its energy, even though diagonal sums were excluded from the combinatorial definition. Therefore

\[
\begin{aligned}
 E_f(\mu,\mu)
 &=\frac43 k+2\sum_{d\ge1}r(d)f(d/T)\\
 &\le\frac43 k+2\sum_{d\ge1}f(d/T)
          +2\sum_{d\in P}f(d/T)\\
 &\le\frac43 k+T+\frac83(k-2)
 =T+4k-\frac{16}{3}\le T+4k\qquad(k\ge2).
\end{aligned}
\tag{W5}
\]

Nonnegativity of \(f\) justifies filling missing differences, and \(f\le f(0)=4/3\) bounds each repeated difference. When \(k=0\) or \(1\), the energy is \(4k/3\le T+4k\) directly. Thus \(W2\) yields, in every case,

\[
 k^2\le\left(\frac NT+\frac23+200e^{-\alpha N/T}\right)(T+4k).
 \tag{W6}
\]

The effective diagonal coefficient is \(4=3f(0)\), not \(f(0)\) or \(2f(0)\).

## 4. Exact proof of the additive constant and onset

Set

\[
 x=N^{1/4},\quad T=\sqrt6\,x^3,\quad
 \gamma=\sqrt{\frac83}=\frac{2\sqrt6}{3},\quad
 \varepsilon=200e^{-\alpha x/\sqrt6}.
\]

For \(x\ge90\), \(L=N/T=x/\sqrt6\ge1\). Expanding \(W6\) gives \(P_\varepsilon(k)\le0\), where

\[
 P_\varepsilon(z)=z^2-(\gamma x+\gamma^2+4\varepsilon)z
                 -x^4-\gamma x^3-\sqrt6\,\varepsilon x^3.
 \tag{W7}
\]

We first prove the uniform bound

\[
 \varepsilon x<\frac12\qquad(x\ge90).
 \tag{W8}
\]

For \(u\ge1\), the derivative of \(\log u-2(u-1)/(u+1)\) is \((u-1)^2/(u(u+1)^2)\ge0\). Hence \(\alpha\ge2/7\). Also \(\sqrt6<49/20\), because \(2400<2401\). Consequently \(\alpha/\sqrt6\ge40/343\). The function \(x e^{-40x/343}\) decreases for \(x\ge343/40\), so

\[
 \varepsilon x\le18000e^{-3600/343}<\frac12.
\]

For completeness the last strict inequality has the following rational certificate. Let

\[
 Q=\sum_{j=0}^{4}\frac{(170/343)^j}{j!}.
\]

The positive exponential series gives \(e>1957/720\) and \(e^{170/343}>Q\). Since \(3600/343=10+170/343\), it is enough that

\[
 (1957/720)^{10}Q>36000.
 \tag{W9}
\]

On multiplication by \(720^{10}\cdot24\cdot343^4\), this is exactly

\[
449233538381596942864443106714320805345633416
>
447728960659239231243811144335360000000000000.
\]

No numerical logarithm or exponential evaluation is used.

Put \(y=x^2+\gamma x+2\). Direct expansion using \(\gamma^2=8/3\) gives

\[
 P_0(y)=\frac43x^2-\frac23\gamma x-\frac43.
 \tag{W10}
\]

Since \(\gamma<5/3\), for \(x\ge90\),

\[
 \frac{P_0(y)}{x^2}
 \ge\frac43-\frac{10}{9\cdot90}-\frac4{3\cdot90^2}
 =\frac{8024}{6075}>\frac{13}{10}.
 \tag{W11}
\]

Using \(W8\) and \(y\le x^2+(5/3)x+2\), we have

\[
\begin{aligned}
 \frac{\varepsilon(4y+\sqrt6 x^3)}{x^2}
 &<\frac{49}{40}+\frac2x+\frac{10}{3x^2}+\frac4{x^3}\\
 &\le\frac{49}{40}+\frac1{45}+\frac1{2430}+\frac1{182250}
 <\frac54.
\end{aligned}
\tag{W12}
\]

All comparisons in \(W11\)–\(W12\) are rational. Therefore

\[
 P_\varepsilon(y)>\left(\frac{13}{10}-\frac54\right)x^2
 =\frac{x^2}{20}>0.
\]

The monic quadratic \(P_\varepsilon\) has negative constant term and thus exactly one positive root. Since \(k\ge0\) and \(P_\varepsilon(k)\le0\), while \(y>0\) and \(P_\varepsilon(y)>0\), we obtain \(k<y\). This proves \(W1\). The monotonic estimates above cover every real \(x\ge90\), not merely integer fourth powers or sampled values. ∎

## 5. Verification scope

Run `node check_weak_sidon.js` in this directory. The dependency-free script uses exact BigInt arithmetic for the exponential and rational-margin certificates, and exhaustively checks weak Sidon subsets of \(\{0,\ldots,13\}\), the repeated-difference lemma, diagonal counts and weighted energy majorants at integral and nonintegral rational window scales. It includes the allowed progression \(\{0,1,2\}\) and forbidden four-term progression as negative controls. These finite tests check bookkeeping; the analytic input and the all-\(N\) monotonicity argument are proved above and in the common appendix. No Lean check, novelty search, or external publication was performed for this transfer.

Actual run on 2026-10-02: exit 0, PASS; 16,384 subsets considered, 2,048 weak Sidon sets, 16,384 weighted energy checks, 1,558 repeated-difference instances, and all exact rational certificates passed.
