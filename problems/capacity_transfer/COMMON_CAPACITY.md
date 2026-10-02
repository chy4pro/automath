PROVED — shared analytic input for task039, reproduced from the project's Sidon proof. This file supplies the complete ramp-kernel, signed-certificate and finite-interval energy proofs used by the transfer notes. It is an analytic proof, not a new Lean formalisation of the transfer results.

# Shared finite-interval capacity lemma

The following sections are copied from SIDON_BOUND_PROOF.md sections2–4, preserving the original internal equation/lemma numbers. Each use of a scaled kernel means a pushforward of the certificate measure under x↦Tx; its mass and energy in the scaled kernel are unchanged. Products of certificates are finite signed product measures. Fubini applies to their bounded product kernels by finite total variation; the product autocorrelation gives the same Hilbert-space Cauchy–Schwarz inequality.

## 2. An autocorrelation kernel and its energy

Lebesgue measure on the real line is denoted by \(dt\). For an integrable
function \(v\) and a measure \(\mu\), write

\[
(v*\mu)(x)=\int v(x-t)\,d\mu(t)
\]

whenever the integral exists. A finite signed real measure means one with
finite total variation \(\|\mu\|_{\rm TV}=|\mu|(\mathbb R)\).

Set

\[
h(t)=2(1-t)\mathbf1_{[0,1]}(t),\qquad
\widetilde h(t)=h(-t),\qquad f=h*\widetilde h.
\tag{2.1}
\]

The specified value \(h(0)=2\) will be convenient in a pointwise identity.

**Lemma 2 (kernel and Cauchy inequality).** The function \(f\) is even and

\[
f(x)=
\begin{cases}
\displaystyle\frac43-2|x|+\frac23|x|^3,&|x|\le1,\\
0,&|x|>1.
\end{cases}
\tag{2.2}
\]

It is nonnegative, nonincreasing on \([0,\infty)\), and satisfies

\[
f(0)=\|h\|_2^2=\frac43,
\qquad \int_{\mathbb R}h(t)\,dt=1,
\qquad \int_{\mathbb R}f(t)\,dt=1.
\tag{2.3}
\]

For finite signed real measures define

\[
E(\mu,\nu)=\iint f(x-y)\,d\mu(x)\,d\nu(y).
\]

Then

\[
E(\mu,\nu)=\int_{\mathbb R}(h*\mu)(t)(h*\nu)(t)\,dt,
\qquad E(\mu,\mu)\ge0,
\tag{2.4}
\]

and

\[
|E(\mu,\nu)|^2\le E(\mu,\mu)E(\nu,\nu).
\tag{2.5}
\]

*Proof.* The autocorrelation is even by a change of variable. For
\(0\le x\le1\), its value is

\[
4\int_0^{1-x}(1-s-x)(1-s)\,ds
=\frac43-2x+\frac23x^3;
\]

for \(x>1\) the two supports have no overlap of positive length. This proves
(2.2). Nonnegativity also follows directly from the integral of the two
nonnegative factors. On \([0,1]\) the derivative is \(-2+2x^2\le0\), and
outside this interval the function is zero. Integrating \(h\) and \(h^2\)
gives (2.3); the mass of \(f\) is \((\int h)^2=1\) by Tonelli's theorem.

For any finite signed measure, Cauchy–Schwarz with respect to \(|\mu|\)
gives

\[
\int |h*\mu|^2\le
\|\mu\|_{\rm TV}
\int\!\int |h(t-x)|^2\,d|\mu|(x)\,dt
=\|\mu\|_{\rm TV}^2\|h\|_2^2.
\]

Thus \(h*\mu\in L^2\). Moreover,
\(\int |h(t-x)h(t-y)|\,dt\le\|h\|_2^2\), so the corresponding triple
integral against \(|\mu|\) and \(|\nu|\) is finite. Fubini's theorem is
therefore applicable. Its inner integral is \(f(x-y)\), which proves
(2.4). Applying the usual Cauchy–Schwarz inequality in real \(L^2\) proves
(2.5). This argument allows either measure to be signed. ∎

## 3. An exact half-line correction

Let \(U\) be the probability measure with density
\(v_1=\mathbf1_{[0,1)}\), and let \(U^{*0}=\delta_0\). Define

\[
g_+=\frac12\sum_{n=0}^{\infty}U^{*n}.
\tag{3.1}
\]

The following construction proves everything needed about this measure;
no renewal theorem is used.

**Lemma 3 (local finiteness and exact potential).** The measure \(g_+\) is
locally finite, supported on \([0,\infty)\), and

\[
h*g_+=\mathbf1_{[0,\infty)},
\qquad (f*g_+)(x)=1\quad(x\ge0).
\tag{3.2}
\]

*Proof.* For \(n\ge1\), let \(v_n\) be the density of \(U^{*n}\).
Convolution gives representatives satisfying, for \(t\ge0\),

\[
0\le v_n(t)\le\frac{t^{n-1}}{(n-1)!}.
\tag{3.3}
\]

For \(n=1\) this is the bound \(v_1\le1\). If it holds at \(n\), then

\[
v_{n+1}(t)=\int_0^{\min(1,t)}v_n(t-s)\,ds
\le\int_0^t\frac{(t-s)^{n-1}}{(n-1)!}\,ds
=\frac{t^n}{n!}.
\]

For every fixed \(R\ge0\), it follows that
\(U^{*n}([0,R])\le R^n/n!\). The sum in (3.1) consequently has finite mass
on every bounded interval.

For a direct proof of the first identity in (3.2), put
\(H=\mathbf1_{[0,\infty)}\). The definitions give the pointwise identity
\(h/2=H-U*H\). Thus each finite partial sum telescopes:

\[
\frac12\sum_{n=0}^m h*U^{*n}
=H-U^{*(m+1)}*H.
\tag{3.4}
\]

For \(t\ge0\), the last term on the right is between zero and
\(t^{m+1}/(m+1)!\), by (3.3), and this tends to zero. For \(t<0\), both
sides vanish. The nonnegative partial sums on the left converge to
\(h*g_+\), proving the identity. This also fixes its value at \(t=0\).

Tonelli's theorem allows association of the nonnegative convolutions.
For \(x\ge0\),

\[
(f*g_+)(x)
=(\widetilde h*(h*g_+))(x)
=\int_{-1}^0\widetilde h(y)H(x-y)\,dy
=\int_{-1}^0\widetilde h(y)\,dy=1.
\]

All the integrals against \(g_+\) here are locally finite because their
kernels have compact support. ∎

Write

\[
g_+=\frac12\delta_0+\frac12u(t)\mathbf1_{[0,\infty)}(t)\,dt,
\qquad u(t)=\sum_{n=1}^{\infty}v_n(t)\quad(t\ge0).
\tag{3.5}
\]

Use the right-continuous representative of \(u\). In particular,

\[
u(0)=1,\quad u(t)=e^t\ (0\le t<1),\quad u(1)=e-1.
\tag{3.6}
\]

The left limit at 1 is \(e\), and must not be substituted for \(u(1)\) in
the recurrence below. To justify these regularity claims, the series in
(3.5) converges uniformly on compact intervals by (3.3). For \(n\ge2\),
the density \(v_n(t)=\int_{t-1}^t v_{n-1}(s)\,ds\), with densities set
to zero for \(s<0\), is continuous. Only \(v_1\) has a jump at 1. For
\(0\le t<1\), the induction proving (3.3) gives equality. At \(t=1\),
\(v_1(1)=0\) and \(v_n(1)=1/(n-1)!\) for \(n\ge2\). These observations
prove (3.6) and the stated representative convention.

**Lemma 4 (quantitative convergence of the density).** For almost every
\(t\ge0\),

\[
|u(t)-2|\le(e-1)(3/4)^{\lfloor t\rfloor}
<2(3/4)^{\lfloor t\rfloor}.
\tag{3.7}
\]

*Proof.* Summing the convolution recurrence for the densities yields
\(u=v_1+U*u\). Thus

\[
u(t)=\int_{t-1}^t u(s)\,ds\qquad(t\ge1).
\tag{3.8}
\]

This includes \(t=1\) with the right-continuous value in (3.6). On
\((1,\infty)\), this identity makes \(u\) locally absolutely continuous,
and \(u'(t)=u(t)-u(t-1)\) almost everywhere. Fix an integer \(n\ge1\).
Solving this first-order equation on \([n,n+1]\) gives

\[
u(n+x)=e^xu(n)-\int_0^x e^{x-y}u(n-1+y)\,dy
\qquad(0\le x\le1).
\]

Since \(u(n)=\int_0^1u(n-1+y)\,dy\), this becomes

\[
u(n+x)=\int_0^1K_x(y)u(n-1+y)\,dy,
\qquad
K_x(y)=e^x-\mathbf1_{\{y\le x\}}e^{x-y}.
\tag{3.9}
\]

For \(0\le x,y\le1\), the kernel is nonnegative, and

\[
\int_0^1 K_x(y)\,dy=e^x-\int_0^x e^{x-y}\,dy=1.
\]

For \(y\in[1/2,1]\), it also satisfies \(K_x(y)\ge1/2\). Indeed, if
\(y>x\), its value is \(e^x\ge1\). If \(y\le x\), its value is
\(e^{x-y}(e^y-1)\ge e^{1/2}-1>1/2\), using the exponential series.

Let \([m_n,M_n]\) be the smallest closed interval containing the essential
range of \(u\) on \([n,n+1)\). Here essential extrema ignore sets of
Lebesgue measure zero. Initially \([m_0,M_0]=[1,e]\). Equation (3.9) first
implies that these closed intervals are nested. For the width estimate,
every \(K_x(y)\,dy\) contains the common measure

\[
w(y)\,dy=\frac12\mathbf1_{[1/2,1]}(y)\,dy
\]

of mass \(1/4\). Put
\(c_n=\int_0^1w(y)u(n-1+y)\,dy\). The remaining nonnegative measure
has mass \(3/4\), so every value in (3.9) lies between
\(c_n+(3/4)m_{n-1}\) and \(c_n+(3/4)M_{n-1}\). Consequently,

\[
[m_n,M_n]\subseteq[m_{n-1},M_{n-1}],
\qquad M_n-m_n\le\frac34(M_{n-1}-m_{n-1}).
\]

The nested closed intervals therefore meet in a single real number \(c\),
and

\[
|u(t)-c|\le(e-1)(3/4)^{\lfloor t\rfloor}
\tag{3.10}
\]

almost everywhere. This also provides a uniform essential bound and
essential uniform convergence to \(c\) as \(t\to\infty\).

For \(t>1\), the atom in (3.5) contributes nothing to \(h*g_+(t)\), so
Lemma 3 gives

\[
1=\frac12\int_0^1 h(s)u(t-s)\,ds.
\]

Letting \(t\to\infty\) in this integral, (3.10) and \(\int h=1\) imply
\(1=c/2\). Thus \(c=2\). Finally, \(e<3\): in its series
\(e=2+\sum_{j\ge2}1/j!\), the tail is strictly smaller than
\(\sum_{j\ge2}2^{-(j-1)}=1\). This proves (3.7). ∎

**Lemma 5 (size, tail, and mass of the correction).** Define the signed
measure supported on \([0,\infty)\)

\[
q=g_+-\mathbf1_{[0,\infty)}(t)\,dt
=\frac12\delta_0+r(t)\mathbf1_{[0,\infty)}(t)\,dt,
\qquad r(t)=\frac12u(t)-1.
\tag{3.11}
\]

It is a finite signed measure, and, with \(\alpha=\log(4/3)\),

\[
|r(t)|\le(3/4)^{\lfloor t\rfloor}\quad\hbox{almost everywhere},
\qquad \|q\|_{\rm TV}\le\frac92,
\tag{3.12}
\]

\[
|q|((L,\infty))\le6e^{-\alpha L}\qquad(L\ge1),
\tag{3.13}
\]

and

\[
q(\mathbb R)=\frac13.
\tag{3.14}
\]

*Proof.* The first bound follows from Lemma 4. Integration on unit intervals
then gives

\[
\|q\|_{\rm TV}\le\frac12+\sum_{n=0}^\infty(3/4)^n=\frac92.
\]

For \(L\ge1\), the atom at zero is outside \((L,\infty)\), and

\[
|q|((L,\infty))
\le\sum_{n=\lfloor L\rfloor}^\infty(3/4)^n
=4(3/4)^{\lfloor L\rfloor}
\le\frac{16}{3}e^{-\alpha L}
\le6e^{-\alpha L}.
\]

It remains to compute the signed mass, not just its absolute bound. For
\(s>0\), Tonelli's theorem and the product rule for Laplace transforms of
nonnegative convolutions give

\[
\begin{aligned}
\int e^{-st}\,dg_+(t)
&=\frac12\sum_{n=0}^\infty
\left(\int_0^1e^{-st}\,dt\right)^n\\
&=\frac1{2\left(1-(1-e^{-s})/s\right)}.
\end{aligned}
\tag{3.15}
\]

The geometric series converges since \(0<\int_0^1e^{-st}\,dt<1\).
Taylor's formula for the exponential, as \(s\downarrow0\), gives

\[
\phi(s):=1-\frac{1-e^{-s}}s
=\frac s2-\frac{s^2}6+O(s^3).
\]

This use of \(O(s^3)\) concerns only a limit: for \(0<s\le1\), Taylor's
remainder after the cubic term of \(e^{-s}\) has absolute value at most
\(s^4/24\), which supplies the displayed bound directly. Subtracting the
Laplace transform \(1/s\) of half-line Lebesgue measure gives

\[
\int e^{-st}\,dq(t)
=\frac1{2\phi(s)}-\frac1s
=\frac{s-2\phi(s)}{2s\phi(s)}
\longrightarrow\frac13.
\]

Because \(q\) has finite total variation and is supported on the
nonnegative half-line, \(|e^{-st}|\le1\) there. Dominated convergence for
the finite measure \(|q|\) shows that the limit is \(q(\mathbb R)\), proving
(3.14). ∎

## 4. Joining two half-lines

**Lemma 6 (finite-interval energy bound).** Let \(L\ge1\), and let \(\mu\)
be any finite positive measure supported on the closed interval \([0,L]\).
If \(k=\mu(\mathbb R)\), then

\[
E(\mu,\mu)\ge
\frac{k^2}{L+\frac23+200e^{-\alpha L}},
\qquad \alpha=\log(4/3).
\tag{4.1}
\]

*Proof.* Let \(q_L\) be the pushforward of \(q\) by the reflection
\(t\mapsto L-t\), and set

\[
\nu_L=\mathbf1_{[0,L]}(t)\,dt+q+q_L.
\tag{4.2}
\]

This is a finite signed real measure, with

\[
\nu_L(\mathbb R)=L+\frac23.
\tag{4.3}
\]

Let \(g_-^L\) denote the same reflection of \(g_+\). As locally finite
measures,

\[
\nu_L=g_++g_-^L-dt.
\tag{4.4}
\]

Indeed, the two half-line Lebesgue measures sum to full-line Lebesgue
measure plus Lebesgue measure on \([0,L]\); endpoints do not change those
Lebesgue measures. The atoms of \(q\) at 0 and of \(q_L\) at \(L\) remain
included in (4.2). Since \(f\) is compactly supported, (4.4) may be
convolved locally with \(f\). Lemma 3 and evenness of \(f\) give, for
\(0\le x\le L\),

\[
V_L(x):=(f*\nu_L)(x)=1+1-\int f=1.
\tag{4.5}
\]

This holds also at both endpoints. For every real \(x\), nonnegativity
and mass one of \(f\), together with Lemma 5, imply

\[
|V_L(x)|\le1+\|f\|_\infty
(\|q\|_{\rm TV}+\|q_L\|_{\rm TV})
\le1+\frac43\cdot9=13.
\tag{4.6}
\]

Outside \([0,L]\), the only measure in (4.2) on \((L,\infty)\) is the
tail of \(q\); on \(( -\infty,0)\) it is the reflection of the same tail.
In particular there are no excluded endpoint atoms. Thus (3.13) gives

\[
|\nu_L|(\mathbb R\setminus[0,L])\le12e^{-\alpha L}.
\]

By (4.3), (4.5), and (4.6),

\[
\begin{aligned}
\left|E(\nu_L,\nu_L)-\left(L+\frac23\right)\right|
&=\left|\int_{\mathbb R\setminus[0,L]}(V_L(x)-1)\,d\nu_L(x)\right|\\
&\le14\cdot12e^{-\alpha L}
=168e^{-\alpha L}
\le200e^{-\alpha L}.
\end{aligned}
\tag{4.7}
\]

Also \(E(\mu,\nu_L)=\int V_L\,d\mu=k\). Lemma 2 now gives

\[
k^2\le E(\mu,\mu)E(\nu_L,\nu_L)
\le E(\mu,\mu)\left(L+\frac23+200e^{-\alpha L}\right).
\]

The denominator is positive and \(E(\mu,\mu)\ge0\), proving (4.1).
There is no assumption that \(\nu_L\) is positive. ∎

