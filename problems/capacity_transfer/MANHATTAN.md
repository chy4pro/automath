PROVED — isolated Claude two-dimensional referee PASS (2026-10-02). Explicit theorem and all-real remainder unchanged; no Lean formalisation or novelty verdict.

# Manhattan distinct-difference configurations: referee and explicit transfer

Task 039, item 5. Informed OpenAI review of the Claude scout derivation;
not a clean-room attack, an external human review, or Lean certification.
No novelty claim is made. The companion analytic appendix
[COMMON_CAPACITY.md](COMMON_CAPACITY.md) is part of this self-contained package.

## Stage A verdict: PASS-WITH-REPAIRS

The model is the square-grid Manhattan DDC of Blackburn--Etzion--Martin--Paterson,
Definition 1 and the paragraph following it: all pairs are at Manhattan distance
at most r, and no two unoriented segments have the same displacement up to sign.
Equivalently, all nonzero ordered difference vectors are distinct. There is no
one-dot-per-row or one-dot-per-column restriction. Their Theorem 9 explicitly
includes an O(r^(1/3)) remainder. These definitions and that statement were read
in the [primary paper, sections II-B and IV-A](https://arxiv.org/html/0811.3832v2)
on 2026-10-02. This was a definition check, not a
literature or priority search.

The scout's inequality (M) and its second-order coefficient are valid. Repairs:

1. Its displayed two-term final upper bound omits **+O(r^(1/3))**. The derivation
   proves the asymptotic statement with that term, not the bare two-term bound.
   The theorem below replaces it by the explicit term +9r^(1/3).
2. Under independent translations of the two transformed coordinates, the point
   set can lie in either coset of the index-2 lattice. Its *differences* still
   lie in the lattice. Counting points themselves in the wrong coset is unnecessary.
3. The product certificate is a finite **signed** measure. Its validity comes
   from the Gram identity and Cauchy--Schwarz, not from positivity of that measure.
   Nonnegativity of the kernel is separately needed when missing vectors are added.
4. The optimized coefficient simplifies exactly to (4/3)^(1/3).

No fatal model or analytic obstruction was found.

## Explicit theorem

Let A be any finite subset of Z^2 such that the map (p,q) -> p-q is injective on
ordered pairs of distinct elements of A. Suppose

    |p_1-q_1| + |p_2-q_2| <= r   for all p,q in A.

For every real r >= 160^3 = 4,096,000, writing m=|A|, one has

\[
\boxed{m\le \frac r{\sqrt2}+\left(\frac43\right)^{1/3}r^{2/3}
                  +9r^{1/3}.}\tag{M1}
\]

Thus the error term is uniform over all such configurations. The onset and
coefficient 9 are convenient explicit choices, not claimed optimal.

## Kernel, signed certificate, and product energy

Put a=4/3, b=2/3, alpha=log(4/3), and

\[
h(t)=2(1-t)1_{[0,1]}(t),\qquad f=h*\widetilde h.
\]

For 0<=t<=1,

\[
f(t)=\frac43-2t+\frac23t^3;
\]

f is even, nonnegative, decreasing on [0,infinity), zero outside [-1,1],
and has integral one. The proved interval-certificate lemma in
[COMMON_CAPACITY.md, Lemma 6](COMMON_CAPACITY.md) supplies, for every L>=1,
a finite signed real measure nu_L with

\[
f*\nu_L=1\text{ on }[0,L],\qquad
0\le E_f(\nu_L,\nu_L)\le L+b+200e^{-\alpha L}.\tag{M2}
\]

For 0<T<=r, dilate nu_(r/T) by the map s -> Ts, without multiplying its mass;
call the resulting measure rho. For F_T(u,v)=f(u/T)f(v/T), the product
rho tensor rho has potential one on [0,r]^2. Fubini gives its energy as
E_f(nu_(r/T),nu_(r/T))^2.

These product manipulations are legitimate for signed measures: each factor
has finite total variation, and the kernels are bounded. Moreover F_T is the
autocorrelation of T^(-1)h(u/T)h(v/T). The associated energy is an L2 inner
product of convolutions. Hence Cauchy--Schwarz applies to the point measure
and the signed product certificate. If the point measure has mass m in this
box, then, with D=r/T+b+200exp(-alpha r/T),

\[
m^2\le D^2 E_{F_T}(\mu,\mu).\tag{M3}
\]

This argument does not require the certificate to be supported in the box.
Only the point measure must be supported there; potential one holds also
on the closed boundary.

## Geometry and the index-2 lattice sum

Apply the invertible real-linear map

\[
(x,y)\longmapsto(u,v)=(x+y,x-y).
\]

The empty configuration is immediate, so the coordinate minima used below
may be taken for a nonempty configuration.

For every displacement,

\[
|\Delta x|+|\Delta y|=\max\{|\Delta u|,|\Delta v|\}.
\]

Thus each transformed coordinate has range at most r. Translate the two
coordinates independently to enclose the configuration in [0,r]^2. Before
translation the image of Z^2 is precisely

\[
\Lambda=\{(u,v)\in\mathbb Z^2:u\equiv v\pmod2\},
\]

which has index 2; afterwards the points occupy a coset. Every difference
still belongs to Lambda, and the linear map preserves difference uniqueness.

Let

\[
S_e=\sum_{j\in\mathbb Z}f(2j/T),\qquad
S_o=\sum_{j\in\mathbb Z}f((2j+1)/T).
\]

Monotonicity and integral one give S_e<=T/2+a. For the odd sum, put
v=f(1/T). Comparing each positive odd sample after the first with the
preceding interval of length 2/T gives

\[
S_o\le2v+T\int_{1/T}^{\infty}f
\le 2v+T\left(\frac12-\frac vT\right)
\le\frac T2+a.\tag{M4}
\]

This remains valid when T<1, since the samples and relevant tail integral
then vanish. All sums are finite because f is compactly supported.
The complete lattice sum is exactly S_e^2+S_o^2. Its zero-vector contribution
is a^2, whereas the point-set energy has m diagonal contributions. Therefore

\[
\begin{aligned}
E_{F_T}(\mu,\mu)
&\le a^2m+S_e^2+S_o^2-a^2\\
&\le a^2m+T^2/2+2aT+a^2.
\end{aligned}\tag{M5}
\]

The addition of unused differences here uses f>=0. Combining (M3)--(M5)
proves the scout's inequality, now with all hypotheses explicit:

\[
\boxed{m^2\le
\left(r/T+b+200e^{-\alpha r/T}\right)^2
\left(a^2m+T^2/2+2aT+a^2\right),\quad0<T\le r.}\tag{M6}
\]

## Explicit optimization and error bound

Set x=r^(1/3), c=(4/3)^(1/3), and t=sqrt(2)c. Then 1<t<2, c<4/3,
and take T=t x^2. For x>=160, T<=r and L=x/t>=1.
Since alpha>=1/4 and t<2, with epsilon=200exp(-alpha x/t),

\[
\epsilon x\le200xe^{-x/8}
\le32000e^{-20}<\frac{32000}{2^{20}}<\frac1{32}.\tag{M7}
\]

The middle bound holds for every x>=160 because x exp(-x/8) decreases for
x>=8. The final comparison is the integer inequality 1,024,000<1,048,576.
Write beta=b+epsilon<1 and D=x/t+beta<=2x.

For A>=0 and B>0, the positive root of z^2-Az-B=0 is at most

\[
\sqrt B+\frac A2+\frac{A^2}{8\sqrt B};\tag{M8}
\]

this follows from sqrt(B+A^2/4)<=sqrt B+A^2/(8sqrt B), obtained by
squaring the nonnegative right side. Apply (M8) to A=a^2D^2 and
B=D^2 B_0, where B_0=T^2/2+2aT+a^2. Since

\[
T/\sqrt2\le\sqrt{B_0}\le T/\sqrt2+\sqrt2a,
\]

(M6) yields

\[
m\le D(T/\sqrt2+\sqrt2a)+\frac{a^2D^2}{2}
                  +\frac{a^4\sqrt2D^3}{8T}.\tag{M9}
\]

The r term is x^3/sqrt(2), and the x^2 coefficient without epsilon is

\[
\frac{bt}{\sqrt2}+\frac{a^2}{2t^2}=c.\tag{M10}
\]

Indeed the two terms are 2c/3 and c/3, using c^3=4/3. The remaining
terms in (M9) are bounded as follows, with every comparison valid for x>=160:

\[
\begin{array}{rcl}
\epsilon t x^2/\sqrt2&\le&x/24,\\
a^2\beta x/t&\le&(16/9)x,\\
\sqrt2a x/t&\le&2x,\\
a^2\beta^2/2+\sqrt2a\beta&\le&26/9\le(13/720)x,\\
a^4\sqrt2D^3/(8T)&\le&(128/27)x.
\end{array}
\]

Their sum is at most (18529/2160)x<9x. This proves (M1) uniformly.

For reference, the optimized second-order coefficient is

\[
3\,2^{-4/3}(ab)^{2/3}=(4/3)^{1/3}.
\]

The omitted remainder cannot simply be deleted from this derivation.
Even after setting epsilon=0 in (M6), its quadratic evaluated at
y_0=x^3/sqrt(2)+c x^2 has expansion

\[
P_0(y_0)=-(c^2+2a/t)x^4+O(x^3).
\]

It is negative for sufficiently large x, so the scalar inequality still
allows values strictly above that two-term expression. This observation
does not construct counterexample DDCs to a sharper possible theorem.

## Exact checker and verification scope

Run `node check_manhattan.js`. It uses only built-in JavaScript and BigInt
rational arithmetic. It checks the numerical rational margins, the optimized
constant identities, parity-lattice sums, the metric transform, and exhaustive
small-set agreement between unordered-sum and ordered-difference conventions.
For every enumerated DDC it checks the exact kernel energy upper bound.
It does not approximate the infinite signed certificate, prove the analytic
appendix computationally, or turn its finite checks into an all-r proof.

Actual execution in this task (Node.js v22.23.1, exit 0): PASS; 72 rational
lattice parameters, all 4,096 subsets of a 4-by-3 grid, 721 DDC subsets, and
3,605 exact energy checks. Empty and singleton sets are included in these
counts. No local Lean compilation, installation, solver, or external action
was used.
