PROVED — version 2 (2026-10-09): onset lowered from 120^4 to 4,600,000. Kernel-checked in Lean (lean/sidon30, theorem `sidon_second_order'`, CI run 37978411704, 39 exact axiom guards); two independent cross-vendor referees PASS on the new Section 6 (notes/review/REF_CR9_referee1_20261010.md, REF_CR9_referee2_20261010.md); exact replay by check_sidon_bound_v2.py (exit 0). No human referee. Version 1 (onset 120^4, Zenodo 10.5281/zenodo.23103980) remains valid as a special case.

# An explicit upper bound for finite Sidon sets

**Status 2026-10-02:** same-vendor review PASS; two isolated cross-vendor referees (Claude Opus) PASS, no repair required (REFEREE_CLAUDE_A_20261002.md, REFEREE_CLAUDE_B_20261002.md); python checker run by the coordinator (exit 0). Published: Zenodo DOI 10.5281/zenodo.23103980. No human referee; no Lean.

**Status: same-vendor reviewed only.** This is a standalone expansion of the
SID-B argument and its ordinary adversarial review. No cross-vendor review,
independent human verification, or kernel formalization is asserted here. No
novelty or priority claim is made. This bound does not settle the original
Erdős #30 conjecture.

## 1. Statement and conventions

A finite set of integers \(A\) is a **Sidon set** if the map

\[
\{(a,b)\in A^2:a\le b\}\longrightarrow\mathbb Z,
\qquad (a,b)\longmapsto a+b
\]

is injective. In particular, the pairs \((a,a)\) are included: equality
\(a+b=c+d\), with \(a\le b\) and \(c\le d\), requires \(a=c\) and \(b=d\).

**Theorem.** For every integer \(N\ge4\,600\,000\) and every Sidon set
\(A\subseteq\{1,\ldots,N\}\),

\[
\boxed{|A|\le\sqrt N+\frac{2\sqrt2}{3}N^{1/4}+1.}
\tag{1.1}
\]

All powers and square roots in this document are positive real ones. In
particular, there is no requirement that \(N\) be a fourth power. The onset is
\(4\,600\,000\) (version 2; version 1 used the convenience onset \(207\,360\,000=120^4\)).

**Lemma 1 (equivalent difference convention).** The Sidon condition is
equivalent to

\[
a-b=c-d\ne0,\qquad a,b,c,d\in A
\quad\Longrightarrow\quad (a,b)=(c,d).
\tag{1.2}
\]

Here the differences are indexed by ordered pairs, and zero differences are
excluded. Equivalently, each positive integer is the difference \(a-b\), with
\(a,b\in A\) and \(a>b\), at most once.

*Proof.* Suppose first that pair sums, including diagonal sums, are unique.
The equality \(a-b=c-d\ne0\) gives \(a+d=c+b\). Equality of the two unordered
pairs with multiplicities gives either \(a=c,d=b\), as required, or
\(a=b,d=c\). The latter possibility contradicts the nonzero difference.

Conversely, suppose (1.2) holds, and let \(a+b=c+d\). If \(a=c\), then
\(b=d\). Otherwise \(a-c=d-b\ne0\), so (1.2), applied to the ordered pairs
\((a,c)\) and \((d,b)\), gives \(a=d,c=b\). Thus the unordered pairs with
multiplicities agree. Restricting both pairs to increasing order proves the
stated Sidon condition, including when a pair is diagonal. Finally, a
negative difference becomes a positive one on reversing both ordered pairs;
hence uniqueness of positive differences is equivalent to (1.2). ∎

Translation preserves these conditions. We may consequently replace \(A\)
by \(A-1\subseteq\{0,\ldots,N-1\}\) when proving (1.1).

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

## 5. The discrete inequality for every interval length

**Lemma 7 (Sidon energy upper bound).** For every integer \(N\ge1\),
every Sidon set \(A\subseteq\{0,\ldots,N-1\}\), and every real
\(0<T\le N\), writing \(k=|A|\) gives

\[
\boxed{
k^2\le
\left(\frac NT+\frac23+200e^{-\alpha N/T}\right)
\left(T+\frac43k\right).
}
\tag{5.1}
\]

*Proof.* Put \(L=N/T\ge1\) and
\(\mu=\sum_{a\in A}\delta_{a/T}\). Its mass is \(k\), and its support
lies in \([0,L]\). In fact its right endpoint is at most \((N-1)/T\);
using the larger interval of length \(N/T\) is permitted in Lemma 6.

Let \(D_+(A)\) denote the set of positive differences of elements of
\(A\). Lemma 1 says that each such difference occurs for exactly one
ordered pair. The zero differences are precisely the \(k\) diagonal
ordered pairs. Evenness of \(f\) therefore gives the exact identity

\[
E(\mu,\mu)=\frac43k+2\sum_{d\in D_+(A)}f(d/T)
\le\frac43k+2\sum_{d=1}^{\infty}f(d/T).
\tag{5.2}
\]

The inequality uses nonnegativity of \(f\). For every integer \(d\ge1\),
monotonicity on the positive half-line implies

\[
f(d/T)\le T\int_{(d-1)/T}^{d/T}f(s)\,ds.
\]

Summing, and using evenness and \(\int f=1\), yields

\[
\sum_{d=1}^{\infty}f(d/T)
\le T\int_0^\infty f(s)\,ds=\frac T2.
\]

Only finitely many summands can be nonzero. It follows that
\(E(\mu,\mu)\le T+4k/3\). Combining this with (4.1) proves (5.1).
This proof applies also to the empty set and to singleton sets. ∎

## 6. The explicit additive constant and onset

Put \(N_1=4\,600\,000\) and \(x_1=N_1^{1/4}\). Let \(N\ge N_1\) be an integer and let \(A\subseteq\{0,\ldots,N-1\}\) be a Sidon set. Write \(k=|A|\). Set

\[
x=N^{1/4},\qquad T=\sqrt2\,x^3,\qquad
\gamma=\frac{2\sqrt2}{3},\qquad
\alpha=\log(4/3),\qquad
\varepsilon=200e^{-\alpha x/\sqrt2}.
\tag{6.1}
\]

The estimates below hold, in fact, for every real \(x\ge x_1\), regardless of whether \(x^4\) is integral. Put \(s=\sqrt2\), \(\beta=\alpha/s\), and \(u=463/10\). Since \(463^4=45\,954\,068\,161<46\,000\,000\,000=10^4N_1\), we have \(x\ge x_1>u>46>2>s>0\). Here \(u>46\) follows from \(463>460\), and \(2>s\) follows from \(2<4=2^2\). Consequently
\(L=N/T=x/s>1\) and \(0<T<N\). Thus the interval parameter in Lemma 7 is admissible.

Expanding Lemma 7 gives \(P_\varepsilon(k)\le0\), where, exactly as before,

\[
P_\varepsilon(z)=
z^2-\left(\gamma x+\frac89+\frac43\varepsilon\right)z
-x^4-\gamma x^3-\sqrt2\,\varepsilon x^3.
\tag{6.2}
\]

Indeed, \((4/3)(x/s+2/3+\varepsilon)=\gamma x+8/9+(4/3)\varepsilon\), and \((x/s+2/3+\varepsilon)sx^3=x^4+\gamma x^3+s\varepsilon x^3\).

Here are exact elementary bounds for the exponential. Substitution in the logarithm integral gives

\[
\alpha=2\int_0^{1/7}\frac{dt}{1-t^2}
>2\left(\frac17+\frac{1}{3\cdot7^3}\right)
=\frac{296}{1029}>\frac{719}{2500}.
\]

The first strict inequality follows from \(1/(1-t^2)>1+t^2\) for \(0<t\le1/7\). The last comparison is \(740000>739851\). Also \(s<99/70\), since \(99^2=9801>9800=2\cdot70^2\). Therefore

\[
\beta u>
\frac{719}{2500}\frac{463}{10}\frac{70}{99}
>\frac{941}{100}>1.
\tag{6.3}
\]

The middle comparison is exactly
\(2\,330\,279\,000>2\,328\,975\,000\), obtained by multiplying the positive denominators; the last is \(941>100\).

The positive-term exponential series yields

\[
e^3>\sum_{j=0}^{9}\frac{3^j}{j!}
=\frac{22471}{1120}>\frac{1003}{50},
\qquad
e^{41/100}>
\sum_{j=0}^{3}\frac{(41/100)^j}{j!}
=\frac{9033221}{6000000}>\frac32.
\]

The rational comparisons are \(1\,123\,550>1\,123\,360\) and \(9\,033\,221>9\,000\,000\). Hence

\[
e^{\beta u}>e^{941/100}
=(e^3)^3e^{41/100}
>\frac{3\cdot1003^3}{2\cdot50^3}>12100,
\qquad
200e^{-\beta u}<\frac{2}{121}.
\tag{6.4}
\]

The penultimate comparison is exactly
\(3\,027\,081\,081>3\,025\,000\,000\).

Put \(y=x^2+\gamma x+1\). Since \(\gamma^2=8/9\), the unchanged polynomial identity is

\[
P_0(y)=\frac{10}{9}x^2+\frac{\gamma}{9}x+\frac19\ge x^2.
\tag{6.5}
\]

We retain the full leading term \((10/9)x^2\) in what follows. In particular \(P_0(y)\ge(10/9)x^2\). Also \(0<\gamma<1\), because \(0<\gamma^2=8/9<1\).

Normalize the error by \(x^2\):

\[
F(x):=\frac{\varepsilon((4/3)y+sx^3)}{x^2}
=200e^{-\beta x}
\left(sx+\frac43+\frac{4\gamma}{3x}+\frac{4}{3x^2}\right).
\]

This function is strictly decreasing on \([u,\infty)\). To see this without any estimate on an unspecified remainder, its four summands are positive constant multiples of \(xe^{-\beta x}\), \(e^{-\beta x}\), \(x^{-1}e^{-\beta x}\), and \(x^{-2}e^{-\beta x}\). The first derivative is \(e^{-\beta x}(1-\beta x)<0\), by (6.3). For \(j=0,1,2\), the derivative of \(x^{-j}e^{-\beta x}\) is
\(-e^{-\beta x}(j x^{-j-1}+\beta x^{-j})<0\).

At the rational endpoint \(u\),

\[
su<\frac{99}{70}\frac{463}{10}
=\frac{45837}{700}<\frac{131}{2},
\qquad
\frac43\left(1+\frac\gamma u+\frac1{u^2}\right)
<\frac43\left(1+\frac1{46}+\frac1{46^2}\right)
=\frac{721}{529}<\frac32.
\]

These comparisons are \(45837<45850\), \(463>460\), and \(1442<1587\). Combining them with (6.4) gives, uniformly for \(x\ge x_1>u\),

\[
F(x)\le F(u)
<\frac{2}{121}\left(\frac{131}{2}+\frac32\right)
=\frac{134}{121}.
\tag{6.6}
\]

Finally, (6.2), (6.5), and (6.6) give

\[
\begin{aligned}
P_\varepsilon(y)
&=P_0(y)-\varepsilon\left(\frac43y+sx^3\right)\\
&>\left(\frac{10}{9}-\frac{134}{121}\right)x^2
=\frac4{1089}x^2>0.
\end{aligned}
\tag{6.7}
\]

Here \(10\cdot121-134\cdot9=1210-1206=4>0\). This proves the requested real-variable assertion for every real \(x\ge x_1\).

The quadratic \(P_\varepsilon\) has leading coefficient 1 and strictly negative constant term. Its discriminant is positive, and its two roots have negative product, so precisely one root is positive. Since \(k\ge0\) and \(P_\varepsilon(k)\le0\), \(k\) is at most that positive root. Since \(y>0\) and \(P_\varepsilon(y)>0\), the positive root is strictly smaller than \(y\). Consequently

\[
k<x^2+\gamma x+1
=\sqrt N+\frac{2\sqrt2}{3}N^{1/4}+1.
\]

Translation from \(A\subseteq\{1,\ldots,N\}\) to \(A-1\subseteq\{0,\ldots,N-1\}\) preserves the given Sidon condition. This proves the stated non-strict theorem, and indeed its strict version, for every integer \(N\ge4\,600\,000\). The root argument also includes \(k=0\). ∎

**Remark (version history).** Version 1 of this document (2026-10-02) proved
the theorem with the convenience onset \(N_0=120^4=207\,360\,000\): it
replaced \(\alpha/\sqrt2\) by \(1/6\) and absorbed the error through the
envelope \(\varepsilon x<1/32\), which needs \(x\ge120\). The present
section (version 2, 2026-10-09) keeps Lemma 7 and the identities (6.2), (6.5)
unchanged and replaces only the numerical absorption; the earlier argument
remains valid on its own range and is a special case of this one. The onset
\(4\,600\,000\) is not claimed minimal: the real-variable inequality
\(P_\varepsilon(y)>0\) with the fixed scale \(T=\sqrt2x^3\) first holds
near \(N\approx4.54\cdot10^6\) (numerical observation, not part of the proof).

## 7. Where the constant \(2\sqrt2/3\) comes from

Two exact constants determine this coefficient in the retained scalar
energy inequality:

\[
a=f(0)=\frac43,
\qquad b=2q(\mathbb R)=\frac23.
\tag{7.1}
\]

The first is the diagonal cost per point in (5.2). The second is the sum
of the two half-line excess masses in (4.3). Apart from the explicitly
controlled exponential error, (5.1) has right side

\[
\left(\frac NT+b\right)(T+ak)
=N+bT+\frac{aNk}{T}+abk.
\tag{7.2}
\]

To read its second-order scale, put \(N=x^4\),
\(T=t x^3\) for a fixed \(t>0\), and \(k=x^2+cx+O(1)\). The terms of
order \(x^3\) in the two sides of the inequality are respectively
\(2cx^3\) and \((bt+a/t)x^3\). The resulting upper coefficient is

\[
c(t)=\frac12\left(bt+\frac at\right)
=\frac t3+\frac{2}{3t}.
\tag{7.3}
\]

For \(t>0\),

\[
bt+\frac at-2\sqrt{ab}
=\left(\sqrt{bt}-\sqrt{a/t}\right)^2\ge0.
\]

Thus the minimum in (7.3) is
\(\sqrt{ab}=2\sqrt2/3\), attained precisely at
\(t=\sqrt{a/b}=\sqrt2\). This gives the scale chosen in (6.1).
For fixed \(t\), the exponential term has argument \(-\alpha x/t\), so
it contributes no term at this order; Section 6 supplies its fully
effective treatment for the selected \(t\).

A precise limitation statement is also possible. It concerns **only the
scalar inequalities (5.1), with this kernel and these retained energy
estimates**. It does not concern all arguments using this kernel, all
boundary corrections, or all Sidon methods.

To prove this limited statement, for each \(N>0\) let \(\kappa_N>0\) be
the solution of

\[
\kappa_N=\sqrt N+\sqrt{ab\,\kappa_N}.
\tag{7.4}
\]

Writing \(x=N^{1/4}\) and \(\gamma=\sqrt{ab}\) gives explicitly

\[
\kappa_N
=\left(\frac{\gamma+\sqrt{\gamma^2+4x^2}}2\right)^2
=x^2+\gamma\sqrt{x^2+\gamma^2/4}+\frac{\gamma^2}{2}.
\tag{7.5}
\]

For every \(T>0\), the elementary square inequality gives

\[
bT+\frac{aN\kappa_N}{T}\ge2\sqrt{abN\kappa_N}.
\]

Consequently,

\[
\begin{aligned}
\left(\frac NT+b\right)(T+a\kappa_N)
&\ge N+2\sqrt{abN\kappa_N}+ab\kappa_N\\
&=\left(\sqrt N+\sqrt{ab\kappa_N}\right)^2
=\kappa_N^2.
\end{aligned}
\tag{7.6}
\]

Equality occurs at \(T=\sqrt{aN\kappa_N/b}\). In particular,
\(\kappa_N\) satisfies the entire collection of these scalar
inequalities simultaneously, even if one allows every \(T>0\) and removes
the nonnegative exponential error. It therefore also satisfies (5.1) for
every allowed \(0<T\le N\).

Formula (7.5) gives the exact remainder identity

\[
\kappa_N-x^2-\gamma x
=\frac{\gamma^2}{2}
+\frac{\gamma^3}{4\bigl(\sqrt{x^2+\gamma^2/4}+x\bigr)}.
\tag{7.7}
\]

Thus \(\kappa_N=x^2+\gamma x+O(1)\). Even imposing integrality on a scalar
\(k\) does not change this leading limitation: for each fixed \(T\),
the inequality in \(k\) is a monic quadratic inequality with negative
constant term, so it holds on the full interval from zero to its positive
root. It therefore holds at \(\lfloor\kappa_N\rfloor\), simultaneously
for all \(T\), including with the exponential error restored. These
integers still equal \(x^2+\gamma x+O(1)\). For large \(N\) they also lie
between 0 and \(N\).

It follows that these scalar inequalities alone cannot imply
\(k\le\sqrt N+cN^{1/4}+C\) for any fixed \(c<\gamma\) and fixed \(C\):
the admissible scalar values \(\lfloor\kappa_N\rfloor\) eventually
violate that conclusion. These are scalar comparison values, **not
constructed Sidon sets**. Improving an earlier estimate, retaining more
information about the differences, or choosing another kernel lies outside
this limitation statement. No general method barrier is claimed.

## 8. External facts and verification scope

The proof uses no external theorem about Sidon sets, renewal processes,
or extremal constants. Its foundational analytic facts are the following;
each is stated with the scope in which it was used.

1. Lebesgue integration for positive and finite signed measures, including
   Tonelli's theorem for nonnegative integrands and Fubini's theorem for
   absolutely integrable integrands. The needed finiteness and absolute
   integrability are verified above. The convolution product rule in
   (3.15) is a direct application of Tonelli and a change of variables.
2. Monotone convergence for the nonnegative measure and function series,
   and dominated convergence when an integrand is bounded by an integrable
   function. For the signed limit in Lemma 5 the dominating finite measure
   is \(|q|\). Compact uniform convergence of the density series follows
   directly from the summable factorial bound (3.3).
3. Cauchy–Schwarz for real square-integrable functions. It is applied both
   to finite positive measures and to Lebesgue measure in Lemma 2.
4. The fundamental theorem for integrals of locally integrable functions:
   their indefinite integrals are locally absolutely continuous, with the
   integrand as derivative almost everywhere. The integrating-factor
   solution of \(w'=w-v\) on a compact interval follows by integrating
   \((e^{-x}w)'=-e^{-x}v\).
5. Completeness of the real numbers: a nested sequence of nonempty compact
   intervals whose lengths tend to zero has a unique common point.
6. Elementary real calculus and algebra: the power series and derivative
   of the exponential, its Taylor formula with remainder, the integral
   formula for the natural logarithm, differentiation of positive real
   powers, geometric series, and the quadratic formula. All problem-specific
   evaluations, error constants, and optimization steps are derived above.

None of these facts needs a specialized literature reference. In
particular, neither an asymptotic renewal theorem nor a quoted numerical
bound supplies any step of the argument.

The accompanying `check_sidon_bound.py` is a computational audit aid. Finite
numerical grids or searches over small sets do not prove Lemma 7 for every
\(N\), nor do they replace the monotonicity argument (6.3)–(6.7). Conversely,
the theorem above does not depend on completion of any exhaustive finite
search. The source argument and this standalone expansion have both received
informed same-vendor adversarial mathematical review. The expansion review
checked the telescoping identity, endpoints, signed measures, all-N monotonicity,
and the restricted scalar optimality argument, without identifying a gap.
This is not cross-vendor, independent human, or kernel certification.

**Version 2 record (2026-10-09).** The new Section 6 was written in a
literature-free clean room from Lemma 7 alone (problems/erdos30/CR9_ASTRA_ONSET_20261010.md),
independently reviewed by two referees of the other vendor (both PASS, no
repair), replayed numerically (notes/review/VER_onset30_20261010.md) and
kernel-checked: `sidon_second_order' : SidonSecondOrderBound'` in
lean/sidon30 compiles with only `propext`, `Classical.choice`, `Quot.sound`.
The formalisation uses the finite certificate of lean/sidon30/PLAN.md rather
than the real-variable Lemma 7; its tail chain at the new onset is the Route B
argument of the same report. Still no human referee.


## 9. Verification script and actual checks

**Version 2.** [check_sidon_bound_v2.py](check_sidon_bound_v2.py) (Python 3,
standard library, exact integers and fractions) replays every integer and
rational comparison of the new Section 6 and of the formalisation's tail chain,
checks the algebraic identities in \(\mathbb Q[\sqrt2,x]\), runs a rational
interval sanity layer for \(P_\varepsilon(y)>0\) on a grid from \(x_1\) to
\(10^6\), tests the finite-certificate tail inequality exactly for every integer
\(N\in[4.6\cdot10^6,5.6\cdot10^6]\) and at every \((T,r)\) block start up to
\(1.2\cdot10^7\), and repeats the small-\(N\) enumeration below. Run by the
verifier on 2026-10-09: exit 0, 2.3 s. The original script below audits
version 1 and is unchanged.

The accompanying [check_sidon_bound.py](check_sidon_bound.py) uses Python3.8+
and the standard library, principally exact fractions and integer square
roots. It requires no package installation. Its default invocation is:

```text
python3 check_sidon_bound.py
```

This checks rational enclosures of the final inequalities at ten default
grid points, including the onset and points through 10^24, then independently enumerates all
subsets for N≤12 and runs complete branch-and-bound to obtain maxima for
every 1≤N≤60. The default exact-search budget is five million nodes and
120seconds. If interrupted, it reports rigorous bounds, marks unresolved
entries INCOMPLETE and exits2; it does not promote a witness to a maximum.
To remove both exact-search budgets explicitly, use:

```text
python3 check_sidon_bound.py --max-n 60 --node-budget 0 --seconds 0
```

The exponential error is enclosed by a proved rational majorant derived
from Section6, rather than floating-point evaluation of exp/log. The
script also checks the polynomial identity symbolically in Q[sqrt(2)].
Small-set checks cover both sum/difference conventions, the diagonal
identity, monotone kernel sum, and stronger rational sufficient versions
of Lemmas6–7 for their tested parameters. Grid tests do not replace the
all-N proof.

Python was absent from this execution environment, so **the Python
deliverable has not been run here**. As explicitly requested in task026,
the coordinator is to run it. The following distinct checks actually
occurred:

- The checker producer ran an equivalent JavaScript branch-and-bound:
  91,104 nodes completed the entire N≤60 search. The derived minimum
  spans for cardinalities1 through10 were
  (0,1,3,6,11,17,25,34,44,55). Eleven marks were excluded by the proved
  index-band lower bound64>59. These values were derived by search, not
  imported as a table.
- An independent literal enumeration of all262,144 subsets of
  {0,…,17} agreed with the translated search's maxima for every N≤18.
  Candidate-mask invariants were also checked on the small search.
- Exact-rational JavaScript mirrors passed all ten default numerical
  grid points. After a reviewer identified a false-abort risk at huge
  optional grid points, all radical enclosures were changed to adaptive
  precision; the N=2^400 regression passed at433bits.
- After adding the finite lower-energy checks, exact-rational JavaScript
  mirrors passed them on all1,368 Sidon subsets among8,190 subsets across
  N≤12 and on all60 displayed maximum witnesses:8,524 rational-parameter
  checks in total.
- An informed adversarial reviewer read this complete proof and the
  Python code, checked every pruning rule and the rational interval
  operations, and returned PASS after the precision repair. The reviewer
  did not execute Python or consult the isolated novelty report.

These are same-vendor code/mathematical checks and an executed JavaScript
translation, not a Python execution, cross-vendor review, or kernel proof.
The finite calculations are sanity checks below the theorem's onset.
No monetary or model-token cost total is available.
