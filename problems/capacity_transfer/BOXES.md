PROVED — isolated Claude two-dimensional referee PASS (2026-10-02). Explicit all-d theorem and remainder unchanged; no Lean formalisation or novelty verdict.

# Sidon sets in integer boxes: referee and explicit product-capacity transfer

Task 039, item 6. Informed OpenAI review of the Claude scout derivation;
not a clean-room attack, an external human review, or Lean certification.
No comparison with the best published constant is claimed; that question
remains with the coordinator's separate source/status check.
The analytic appendix [COMMON_CAPACITY.md](COMMON_CAPACITY.md) is part of
this self-contained proof package.

## Stage A verdict: PASS-WITH-REPAIRS

Use [N]^d={0,...,N-1}^d with ordinary addition in Z^d, and require all
unordered sums of two elements, **including repeated elements**, to be unique.
This is the convention in the abstract and section 1 of
[On Sidon sets in a random set of vectors](https://arxiv.org/html/1405.4227),
read as a primary definition source on 2026-10-02.
Translation gives the identical theorem for {1,...,N}^d. This is not a
modular group problem or the weaker condition omitting diagonal sums.

The scout's product inequality and coefficient are correct. Its asymptotic
claim needs a stated remainder and fixed-d quantifier. The proof below gives
an explicit d-dependent remainder and onset, and improves the coarse lattice
error by evaluating the one-dimensional lattice sum. Product certificates
are signed; their Gram energies are nonnegative, which is essential when
multiplying their upper bounds. No factor 2^d is lost in the difference count:
every *ordered* nonzero difference vector is used at most once.

## Explicit theorem

Let d>=2 and N>=1 be integers. Set

\[
x=N^{d/(2d+2)},\qquad
s_d=(8/9)^{d/(d+1)},\qquad c_d=\frac{d+1}{2}s_d.
\]

If x>=max{120,4d}, then every strong Sidon set A in [N]^d satisfies

\[
\boxed{|A|\le N^{d/2}+c_dN^{d^2/(2d+2)}
                +2d^2N^{d(d-1)/(2d+2)}.}\tag{B1}
\]

Equivalently, one sufficient integer onset is
N>=ceil(max{120,4d}^((2d+2)/d)). All constants are displayed, and the
inequality is uniform over A. In particular, for each **fixed** d,

\[
|A|\le N^{d/2}+c_dN^{d^2/(2d+2)}
       +O_d\bigl(N^{d(d-1)/(2d+2)}\bigr),
\]

where the upper-error term may be chosen to be the nonnegative function
2d^2 N^(d(d-1)/(2d+2)) beyond the displayed onset. The asymptotic notation is not asserted uniform in
growing d; the explicit inequality (B1) states exactly what remains uniform.

## Difference convention

If p-q=r-s is nonzero, then p+s=r+q. Strong Sidonicity implies equality
of the unordered pairs {p,s} and {r,q}. The alternative p=q would make
the difference zero; hence p=r and q=s. Conversely, a nontrivial equality
of unordered sums gives two distinct ordered representations of a nonzero
difference. This argument includes cases where a sum uses the same point
twice, since Z^d has no 2-torsion. Thus the two conventions agree here.

## Kernel and a sharp enough lattice sum

Let a=4/3, b=2/3, alpha=log(4/3), and use the ramp autocorrelation

\[
f(t)=\begin{cases}
4/3-2|t|+(2/3)|t|^3,& |t|\le1,\\
0,&|t|>1.
\end{cases}
\]

As proved in [COMMON_CAPACITY.md](COMMON_CAPACITY.md), f is nonnegative,
even, positive definite, has integral one, and f(0)=a. Monotonicity alone
gives S(T):=sum_(j in Z)f(j/T)<=T+a for every T>0.
For the explicit remainder we use, for T>=1, the stronger bound

\[
S(T)\le T+\frac1{2T}.\tag{B2}
\]

Here is an elementary proof without Poisson summation. Put n=floor(T) and
theta=T-n. The finite sums sum j=n(n+1)/2 and sum j^3=n^2(n+1)^2/4 give

\[
\begin{aligned}
S(T)&=\frac43+\frac83n-\frac{2n(n+1)}T
                  +\frac{n^2(n+1)^2}{3T^3}\\
&=T+\frac1{3T}
 -\frac{2\theta(1-\theta)(1-2\theta)}{3T^2}
 +\frac{\theta^2(1-\theta)^2}{3T^3}.\tag{B3}
\end{aligned}
\]

The endpoint term when T is integral is zero, so it causes no exception.
For theta in [0,1], theta(1-theta)<=1/4 and
theta(1-theta)|1-2theta|<=1/8. To check the latter, set u=|1-2theta|;
the expression is u(1-u^2)/4<=u(1-u)/2<=1/8.
Since T>=1, (B3) is at most

\[
T+\left(\frac13+\frac1{12}+\frac1{48}\right)T^{-1}
=T+\frac7{16T}\le T+\frac1{2T}.
\]

## Product certificate and scalar inequality

For 0<T<=N put L=N/T, and let nu_L be the finite signed measure from
Lemma 6 of [COMMON_CAPACITY.md](COMMON_CAPACITY.md). Its f-potential is
one on the closed interval [0,L], and its nonnegative self-energy is at
most D=L+b+200exp(-alpha L). Let rho be its pushforward under s->Ts,
with no extra multiplication of its mass, and take rho^(tensor d).

For

\[
F_T(z)=\prod_{i=1}^d f(z_i/T),
\]

the product certificate has potential one on [0,N]^d and self-energy
E_f(nu_L,nu_L)^d<=D^d. All product integrals are absolutely integrable:
the measures have finite total variation and F_T is bounded. Furthermore,
F_T is the autocorrelation of T^(-d/2)product_i h(z_i/T), so its signed
energy is an L2 Gram form. Cauchy--Schwarz against the point measure gives
k^2<=D^d E_(F_T)(mu,mu), where k=|A|.

The k diagonal ordered pairs contribute a^d k. Each other vector is
represented at most once. Nonnegativity permits adding the missing vectors,
and the full integer-lattice sum factors as S(T)^d. Consequently

\[
\boxed{k^2\le D^d\bigl(a^dk+S(T)^d-a^d\bigr).}\tag{B4}
\]

Using S(T)<=T+a gives exactly the scout's scalar inequality. If T>=1,
(B2) also gives the slightly looser but convenient quadratic

\[
k^2\le a^dD^d k+D^d(T+1/(2T))^d.\tag{B5}
\]

Dropping -a^d is in the safe direction. No positivity of rho is presumed.

## Optimization and uniform error calculation

Put

\[
t=(a^d/b)^{1/(d+1)},\quad s=bt=(ab)^{d/(d+1)}=s_d,
\quad q=x^{-1},\quad K=N^{d/2},\quad T=tN/x.
\]

Then 1<t<3/2, 0<s<1, and a^d/t^d=s. Also T>=x because
T/x=t N^(1/(d+1))>=1, and T<=N when x>=120.
For epsilon=200exp(-alpha x/t), alpha>=1/4 and t<3/2 imply

\[
\epsilon x\le200xe^{-x/6}\le24000e^{-20}
<24000/2^{20}<1/32\qquad(x\ge120).\tag{B6}
\]

The bound is uniform because x exp(-x/6) decreases for x>=6, and
24000*32=768000<1048576=2^20.
Define

\[
w=(b+\epsilon)tq,\quad z=1/(2T^2),\quad v=(1+w)(1+z)-1.
\]

The assumptions give q<=1/120 and dq<=1/4. In particular,

\[
0\le w\le s q+(3/64)q^2\le q+q^2,
\quad 0\le z\le q^2/2,
\quad 0\le v\le s q+q^2\le q+q^2.\tag{B7}
\]

For the v estimate, the coefficient beyond s q is at most
3/64+1/2+(q+q^2)/2<=45/64<1, already for q<=1/4.
Therefore dw,dv<=5/16<1/3. For any u>=0 with du<1, the binomial theorem
and binomial(d,j)<=d^j show (1+u)^d<=1/(1-du). Thus

\[
(1+w)^d\le3/2,\quad
(1+w)^d-1\le\frac{dw}{1-dw}\le2dq,\quad
(1+v)^d\le3/2.\tag{B8}
\]

Divide (B5) by K^2. The linear coefficient of U=k/K is
s q(1+w)^d; this uses x^(d+1)=N^(d/2). The constant term is (1+v)^d.
For A>=0,B>0, the root bound
U<=sqrt(B)+A/2+A^2/(8sqrt(B)) follows by completing the square.
Hence

\[
U\le(1+v)^{d/2}+\frac{s q}{2}(1+w)^d
                 +\frac{s^2q^2(1+w)^{2d}}{8(1+v)^{d/2}}.\tag{B9}
\]

The last term is at most (9/32)q^2. The middle term is at most
(s/2)q+dq^2. For the first, put p=d/2>=1. Taylor's theorem on [0,v]
and (B8) bound its second derivative by (3/2)p(p-1). This is valid also
for 1<=p<2, when (1+u)^(p-2)<=1. It follows, since v<=s q+q^2<=2q,
that

\[
(1+v)^{d/2}
\le1+\frac d2s q+\left(\frac d2+\frac{3d^2}{4}\right)q^2.
\]

Putting these bounds in (B9),

\[
U\le1+\frac{d+1}{2}s q+
       \left(\frac{3d^2}{4}+\frac{3d}{2}+\frac9{32}\right)q^2
\le1+c_d q+2d^2q^2.
\]

The last inequality holds for every integer d>=2: the difference is
(5/4)d^2-(3/2)d-9/32, positive at d=2 and increasing afterwards.
Multiplying by K proves (B1).

The optimal scale used above is not guessed: before optimization the
second-order coefficient is (d b t+a^d t^(-d))/2. AM--GM on the d+1
positive terms gives the minimum c_d at t^(d+1)=a^d/b. Allowing different
scales in the coordinate directions gives the same minimum by AM--GM.
This is optimization of the retained product inequality, not optimality
over all kernels, all non-product certificates, or all Sidon arguments.

## Exact checker and verification scope

Run `node check_boxes.js`. This dependency-free checker uses BigInt rational
arithmetic. It verifies (B3) both symbolically and at rational scales, (B2),
the rational margins in the uniform error argument, and exact energy upper
bounds for exhaustively enumerated small strong Sidon sets in dimensions
2 and 3. It tests the inclusion of repeated-element sums explicitly by
comparing against ordered nonzero difference uniqueness. These checks
supplement the proof; they do not certify the analytic appendix or an
unbounded family by finite enumeration.

Actual execution in this task (Node.js v22.23.1, exit 0): PASS; the symbolic
identity after multiplication by 3T^3, 292 rational lattice parameters,
21 dimension/error-margin cases, and all 768 subsets of [3]^2 and [2]^3.
There were 182 and 159 Sidon subsets respectively, for 341 total and 1,705
exact energy checks. The proof of the all-d remainder uses the displayed
polynomial and its positive increment, not the finite dimension scan.
No local Lean compilation, installation, solver, or external action was used.
