PROVED — liminf(C_f(L)-L) >= 8/(9f(0)); the ramp attains equality. Same-vendor reviews PASS; cross-vendor referee A (Claude Opus): PASS-WITH-REPAIRS, repairs applied. Referee B manuscript status awaits coordinator update; human and kernel reviews remain outstanding.

# The optimal kernel constant for the scalar Sidon capacity method

Date: 2026-10-02. Task 030, strengthened by Task 033.

**Main result.** For the kernel class in Theorem 1, set
beta(f)=liminf_{L->infinity}(C_f(L)-L), allowing infinity. Then

\[
\boxed{\beta(f)\ge\frac8{9f(0)},\qquad
       \inf_f f(0)\beta(f)=\frac89.}
\]

The finite-intercept subclass still has inf_f f(0)b(f)=8/9.

The ramp h(t)=2(1-t)1_[0,1](t) attains the infimum, with a=4/3 and b=2/3.
The lower bound permits signed h, nonmonotone f and unbounded support.
Its proof uses only NONNEGATIVE trial measures in the capacity problem.
It does not identify positive and signed capacities or assume a
nonnegative spectral factor.

The consequent barrier is for the **fixed-kernel scalar capacity and
nonnegative difference-majorization method**, under the separate unit-slope
hypothesis in Section 7 and using the full infinite lattice difference
sum. The capacity theorem itself needs no slope hypothesis. It is not
a barrier for all
weighted Erdős--Turán arguments, additional variance/missing-difference
information, or the original Erdős #30 conjecture. The existing explicit
Sidon bound and its onset are not changed by this report.

## 1. Definitions, hypotheses, and exact theorem

Let h be real, in L1(R) intersect L2(R), with integral h=1. Set

    h~(t)=h(-t),  f=h*h~,  a=f(0)=||h||_2^2.

Assume f>=0. Such f is even, continuous, tends to zero at infinity,
has integral one, is positive definite, and satisfies |f|<=a.
For a finite measure mu write

    E_f(mu,nu)=integral integral f(x-y) dmu(x)dnu(y).

The capacity in this report is

    C_f(L)=1/min{ E_f(mu,mu): mu is a NONNEGATIVE Borel probability
                              measure supported on the CLOSED [0,L] }.

The minimum exists by compactness and continuity. It is positive: f>=a/2
on some neighborhood of zero, and partitioning [0,L] into finitely many
intervals of smaller diameter gives a uniform positive lower energy
bound using the sum of squared interval masses.

The capacity theorem below requires no finite intercept. When one exists,
write C_f(L)=L+b+o(1); then beta=b. For obtaining an asymptotic Sidon
upper bound the upper sampling estimate

    sum_{d>=1} f(d/T) <= T/2+O(1), as T tends to infinity,

is useful, with a controlled error when explicit constants are requested.
Section 7 separates that sufficient upper-bound condition from the
weaker unit-slope assumption used in the barrier direction. No
monotonicity or support restriction is imposed.

**Theorem 1 (universal capacity lower bound).** Let f be any even,
nonnegative member of C_0(R) intersect L1(R), with integral f=1 and
a=f(0)>0. Define the extended real number

    beta(f)=liminf_{L->infinity}(C_f(L)-L).

Then

\[
 \boxed{\beta(f)\ge\frac8{9a}.}
\]

No finite intercept, unit-slope hypothesis, autocorrelation
representation, positive definiteness, or sampling assumption is
required. In particular, if C_f(L)=L+b+o(1) with finite b, then
beta=b and ab>=8/9. The separate slope assumption used for the
method barrier is stated in Section 7.

**Theorem 2 (attainment).** For the ramp autocorrelation

\[
f_0(t)=
\begin{cases}
4/3-2|t|+(2/3)|t|^3,& |t|\le1,\\
0,& |t|>1,
\end{cases}
\]

one has a=4/3 and, with alpha=log(4/3), for every real L>=1,

\[
L+\frac23-168e^{-\alpha L}-192e^{-2\alpha L}
\ \le C_{f_0}(L)\le\
L+\frac23+168e^{-\alpha L}.
\]

In particular |C_f0(L)-L-2/3|<=360e^(-alpha L), b=2/3,
and the exact sampling bound sum_{d>=1} f_0(d/T)<=T/2 holds for every T>0.
These theorems establish the stated infimum for the admissible Sidon class.

## 2. Positive capacity and the first-moment dichotomy

For positive finite measures nu supported on [0,L], write M(nu)=nu(R).
Scaling a probability measure and maximizing 2c-c^2 E_f(mu,mu) over c>=0
gives the exact formula

\[
C_f(L)=\sup_{\nu\ge0,\ \operatorname{supp}\nu\subseteq[0,L]}
          \{2M(\nu)-E_f(\nu,\nu)\}.
\tag{2.1}
\]

Here the zero measure can harmlessly be included. Taking nu to be
Lebesgue measure lambda_L on [0,L] yields

    E_f(lambda_L,lambda_L)=L-M_1(L),
    M_1(L)=integral_R min(|t|,L)f(t)dt,
    C_f(L)>=L+M_1(L).

Because M_1(L) increases to the possibly infinite first moment,

\[
 m_1:=\int_{\mathbb R}|t|f(t)\,dt
 \le \beta:=\liminf_{L\to\infty}(C_f(L)-L).
\tag{2.2}
\]

If m_1=infinity, the uniform trial already gives beta=infinity and
proves Theorem 1. If m_1<infinity, the boundary expansion in Section 5
applies directly, without requiring beta to be finite or a limit to
exist. A finite intercept b is the special case beta=b and forces
m_1<=b<infinity.

## 3. An elementary renewal measure

Let W have density w=1_[0,1), and set

    U=delta_0+sum_{n>=1} W^{*n},  v=U/2,
    H_+(t)=1_[0,infinity)(t), H_-(t)=H_+(-t).

Functions such as H_+ also denote their associated Lebesgue-density
measures when used in measure convolutions. The densities of W^{*n}
are bounded by t^(n-1)/(n-1)! for t>=0, so the sum is locally finite
and converges locally for its density. Write

    U=delta_0+u(t)dt, with u=0 for t<0.

The right-continuous representative obeys

    u(t)=exp(t) for 0<=t<1,  u(1)=e-1,
    u(t)=integral_(t-1)^t u(s)ds for t>=1.

The atom and the jump at one must both be retained. In particular the
left limit e is not the value substituted into the recurrence at one.

Let h_0(t)=2(1-t)1_[0,1](t). The identity h_0/2=H_+-W*H_+
and telescoping the renewal series give

\[
 h_0*v=H_+.
\tag{3.1}
\]

The remainder tends to zero locally, bounded on [0,R] by R^(n+1)/(n+1)!.

Here is a quantitative renewal proof without a quoted renewal theorem.
For integers n>=1 and 0<=x<=1, differentiating the recurrence and using
an integrating factor gives

\[
u(n+x)=\int_0^1 K_x(y)u(n-1+y)\,dy,
\qquad K_x(y)=e^x-\mathbf1_{\{y\le x\}}e^{x-y}.
\tag{3.2}
\]

The kernel is nonnegative and has integral one. For y in [1/2,1]
it is at least 1/2: if y>x it is e^x>=1; otherwise it equals
e^(x-y)(e^y-1)>=e^(1/2)-1>1/2. Every averaging measure thus contains
(1/2)1_[1/2,1](y)dy, of mass 1/4. The essential ranges of u on successive
unit intervals are nested inside the initial interval [1,e], and their
widths contract by 3/4. They meet in a single number c, with

    u>=1 almost everywhere,
    |u(t)-c| <= (e-1)(3/4)^floor(t).

For t>1, (3.1) becomes 1=(1/2)integral_0^1 h_0(s)u(t-s)ds.
Taking the limit gives c=2. Since e<3,

\[
 |u(t)-2|<2(3/4)^{\lfloor t\rfloor}\quad\text{almost everywhere}.
\tag{3.3}
\]

Define the FINITE signed measure

    kappa=v-H_+ = (1/2)delta_0+k(t)dt,  k(t)=u(t)/2-1 for t>=0.

It has no other atom and satisfies

\[
 \|\kappa\|_{\rm TV}\le\frac92,
 \qquad |\kappa|((L,\infty))\le6e^{-\alpha L}\quad(L\ge1),
 \qquad \alpha=\log(4/3).
\tag{3.4}
\]

Indeed, integrate |k(t)|<=(3/4)^floor(t) on unit intervals;
the tail is at most 4(3/4)^floor(L)<=(16/3)e^(-alpha L)<6e^(-alpha L).
Its total mass is obtained without a transform: (3.1) gives
h_0*kappa=H_+-h_0*H_+, whose right side vanishes outside [0,1].
Fubini and integral h_0=1 imply

\[
 m:=\kappa(\mathbb R)
 =\int_0^1\left(1-\int_0^t h_0(s)ds\right)dt
 =\int_0^1 t h_0(t)dt=\frac13.
\tag{3.5}
\]

Finally put R(s)=U([0,s]) for s>=0 and R(s)=0 for s<0.
It is nonnegative, R(s)>=1 for s>=0, has jump 1 at zero, and obeys

    R'(s)=R(s)-R(s-1) for s>0, almost everywhere,
    R(s)=2s+2/3+O(exp(-alpha s)) as s tends to infinity.

The last assertion follows immediately from U=2H_++2kappa and (3.4).

## 4. The exact boundary-correlation identity

For t>0 let T(t)=kappa([t,infinity)). The value assigned at t=0 will
not matter for a density. Define the even measure, with at most linear
growth of its density,

\[
 B=[-|t|+2m+2T(|t|)]dt+2\kappa*\widetilde\kappa.
\tag{4.1}
\]

**Lemma.** As measures,

\[
\boxed{B=\frac12\delta_0
       -\frac12\mathbf1_{\{|t|>1\}}R(|t|-1)\,dt.}
\tag{4.2}
\]

Values of the displayed density at t=+/-1 are immaterial. In particular
its density away from the zero atom is nonpositive everywhere a.e.

**Proof.** The proof uses only elementary weak derivatives: derivatives
are interpreted against compactly supported smooth test functions.
Write D for differentiation, tau_1 for translation to the right by one,
and A=D-I+tau_1. The renewal equation (delta_0-W)*v=(1/2)delta_0,
after differentiation using W'=delta_0-delta_1, gives

    Av=(1/2)delta'_0,
    AH_+=delta_0-W,
    A kappa=W-delta_0+(1/2)delta'_0.

All subsequent convolutions are well defined: kappa is a finite signed
measure with an exponentially decreasing density and one atom; the
operator A has compact support; convolution with a half-line indicator
is bounded. The derivative identity also expresses kappa' as a finite
signed measure plus one derivative of an atom, which justifies commuting
the weak derivatives below.

Since H_-*kappa+H_+*kappa~=m+T(|t|) almost everywhere,

    B=-|t|dt+2H_-*kappa+2H_+*kappa~+2kappa*kappa~.

Apply A, placing it on kappa in the second and fourth terms and on H_+
in the third. The terms convolved against kappa~ cancel except for its
derivative. Also H_-*delta'_0=-delta_0. Therefore

    AB=A(-|t|)+2(H_-*W-H_-)-delta_0+(kappa~)'.

The two ordinary functions cancel exactly: on (0,1) they are 2(t-1)
and 2(1-t), respectively, and both vanish elsewhere. Consequently

\[
 B'-B+\tau_1B=(\widetilde v)'.
\tag{4.3}
\]

No Fourier transform or ambiguity at zero frequency enters this identity.

The only atom of B is (1/2)delta_0. Write B=(1/2)delta_0+D_0(t)dt,
where D_0 is even. For t>0 its locally integrable density is explicitly

    D_0(t)=-t+2m+2T(t)+k(t)
                       +2 integral_0^infinity k(s)k(s+t)ds.

In particular D_0(t)=-t+2m+O(exp(-alpha t)) as t tends to infinity.
The right side of (4.3) is supported on the nonpositive half-line.
Thus on 0<t<1 it gives

    D_0'(t)=D_0(t)-D_0(1-t).

This equality first ensures local absolute continuity. The derivative
of D_0(t)-D_0(1-t) is zero, and this difference changes sign under
reflection about 1/2. It is therefore zero, and D_0 is a constant d
on (0,1). At t=1 the translated atom gives a jump -1/2. For t>1,
D_0'=D_0-D_0(t-1). The renewal function R has exactly the required
jump and delay equation, so uniqueness on successive unit intervals gives

    D_0(t)=d-(1/2)R(t-1), t>1.

Its asymptotic constant from this formula is d+2/3, while from its
definition it is 2m=2/3. Hence d=0, proving (4.2). QED.

## 5. Positive trials for every kernel and proof of Theorem 1

If m_1=infinity, Section 2 already proves the theorem. Throughout the
rest of this proof assume m_1<infinity; beta may still be infinite.

Truncate the two boundary corrections and set

    nu_L=lambda_L+kappa|_[0,L]+reflection(kappa|_[0,L]).

The endpoint atoms have mass 1/2. The interior density is

    1+k(x)+k(L-x)=u(x)/2+u(L-x)/2-1>=0.

Thus nu_L is a NONNEGATIVE measure for every L>0, not just a formal signed
boundary ansatz. Its mass is L+2m+o(1)=L+2/3+o(1).

In this finite-first-moment case, expansion of the energy gives

\[
 E_f(\nu_L,\nu_L)=L+\int_{\mathbb R} f(t)\,dB(t)+o(1).
\tag{5.1}
\]

Here are all four terms and their justifications.

1. Uniform--uniform contributes L-m_1+o(1), by (2.2).
2. For a left correction, the uniform potential at y>=0 tends to
   integral_(-y)^infinity f=1/2+integral_0^y f, and is bounded by one.
   Dominated convergence against |kappa|, followed by Fubini, shows
   that both ends and both ordered cross terms together contribute
   2m+4 integral_0^infinity f(t)T(t)dt.
3. The two same-end self-energies tend to 2 integral f d(kappa*kappa~),
   by boundedness of f and finiteness of |kappa|.
4. The opposite-end cross term tends to zero: for fixed x,y>=0,
   f(x+y-L) tends to zero, and dominated convergence applies against
   |kappa| times |kappa|. Truncation introduces no additional term.

These are exactly the terms defining B. The integral of f against its
linear-growth density converges by (2.2). By the certificate (4.2),

    E_f(nu_L,nu_L)
      = L+a/2-(1/2)integral_{|t|>1} f(t)R(|t|-1)dt+o(1).

Use nu_L in the POSITIVE variational formula (2.1). After subtracting L
and taking the lower limit,

\[
 \beta\ge\frac43-\frac a2
       +\frac12\int_{|t|>1} f(t)R(|t|-1)dt
 \ge\frac43-\frac a2.
\tag{5.2}
\]

For any ell>0 apply this statement to f_ell(t)=ell f(ell t).
Its integral is one, its value at zero is ell a, and changing variables
in the positive measure problem gives the exact relation

    C_fell(L)=C_f(ell L)/ell,
    beta(f_ell)=beta(f)/ell.

The latter holds in the extended real numbers. Thus the scaled certificate is

\[
 \beta\ge\frac{4\ell}{3}-\frac{a\ell^2}{2}
       +\frac\ell2\int_{|t|>\ell}f(t)R(|t|/\ell-1)dt
 \ge\frac{4\ell}{3}-\frac{a\ell^2}{2}.
\tag{5.3}
\]

Set ell=4/(3a), maximizing the final quadratic. This proves

\[
\boxed{\liminf_{L\to\infty}(C_f(L)-L)
       =\beta\ge\frac8{9a}.}
\]

When a finite intercept exists, beta=b and ab>=8/9 follows.
Neither an upper sampling estimate nor positive definiteness was used.
As a necessary equality condition, a beta=8/9 forces
f(t)=0 for |t|>4/(3a), since R>=1 there in (5.3).
This is NOT a uniqueness theorem for all equality kernels.

## 6. Actual positive-capacity attainment and explicit remainder

Direct integration gives the stated formula for f_0=h_0*h_0~, with
f_0(0)=4/3, integral f_0=1 and f_0 nonnegative and nonincreasing on
[0,infinity). For any finite signed measures mu,nu, Fubini gives

    E_f0(mu,nu)=integral (h_0*mu)(t)(h_0*nu)(t)dt.

The integrals converge because h_0 is in L2 and the measures have finite
total variation. The energy therefore obeys Cauchy--Schwarz, also for
signed comparison measures.

Convolve (3.1) with h_0~. Since h_0~ is supported on [-1,0] and has mass
one, f_0*v=1 on the CLOSED positive half-line. For L>=1 let kappa_L be
reflection of kappa under t -> L-t, and put

    eta_L=lambda_L+kappa+kappa_L,
    d_L=L+2/3, V_L=f_0*eta_L.

This is a finite signed measure of mass d_L. Equivalently it is the sum
of v and its reflection minus full-line Lebesgue measure, so

    V_L=1 on [0,L],  |V_L(x)|<=1+2(4/3)(9/2)=13 everywhere.

Let sigma_L be its restriction to [0,L], and tau_L the omitted exterior
part. The former is exactly nu_L from Section 5, hence nonnegative.
The latter satisfies, with q_L=exp(-alpha L),

    ||tau_L||TV<=12q_L,
    |E_f0(eta_L,eta_L)-d_L|
      =|integral_outside (V_L-1)deta_L|<=168q_L.

For any probability measure mu on [0,L], E_f0(mu,eta_L)=1.
Cauchy--Schwarz then yields C_f0(L)<=E_f0(eta_L,eta_L)<=d_L+168q_L.

For the lower bound use sigma_L in (2.1). Since V_L=1 on its support,
E_f0(eta_L,sigma_L)=M(sigma_L). Expanding eta_L=sigma_L+tau_L gives the
EXACT identity

    2M(sigma_L)-E_f0(sigma_L,sigma_L)
      =E_f0(eta_L,eta_L)-E_f0(tau_L,tau_L).

The last energy is at most (4/3)||tau_L||TV^2<=192q_L^2. Therefore

    C_f0(L)>=d_L-168q_L-192q_L^2>=d_L-360q_L.

This proves Theorem 2 for the positive capacity itself; no equality
with a signed-measure capacity was assumed.

## 7. Sampling and the exact scope of the Sidon consequence

Monotonicity of f_0 gives, for every T>0,

    f_0(d/T)<=T integral_((d-1)/T)^(d/T) f_0(s)ds,
    sum_{d>=1} f_0(d/T)<=T/2.

Monotonicity is sufficient but unnecessary for this upper sampling bound.
For example, if f has total variation V<infinity on the positive
half-line, summing the cellwise variation bound gives

    |sum_{d>=1} f(d/T)-T/2|<=V.

This upper bound is useful for obtaining an effective Sidon estimate.
It is not an assumption of the capacity theorem, and is not needed
for the barrier direction below.

### 7.1. A sampling lower bound from unit capacity slope

For this subsection impose the separate hypothesis

    limsup_{L->infinity} C_f(L)/L <= 1.                         (7.1)

It holds whenever C_f(L)=L+b+o(1) with finite b. It is NOT an
assumption of Theorem 1; it is stated explicitly as a hypothesis
of the method limitation. Set

    S_T=sum_{d in Z} f(d/T), in (0,infinity].

Then, for every T>0,

    S_T >= T.                                                (7.2)

If S_T is infinite this is immediate. Otherwise take the probability
measure mu_n=(1/n)sum_{j=0}^{n-1}delta_(j/T). Nonnegativity gives

    E_f(mu_n,mu_n)
      =(1/n^2)sum_{|d|<n}(n-|d|)f(d/T) <= S_T/n,
    C_f((n-1)/T) >= n/S_T.

Divide by (n-1)/T and let n tend to infinity. Hypothesis (7.1)
gives 1>=T/S_T, proving (7.2). No upper sampling estimate was used.

The Sidon convention is injectivity of unordered pair sums INCLUDING
diagonal pairs. Equivalently, each positive difference has at most
one representation. For a Sidon set A subset {1,...,N}, |A|=k,
nonnegative difference majorization therefore yields the exact scalar
inequality

    k^2 <= C_f(N/T)[ak+2 sum_{d>=1}f(d/T)]
        = C_f(N/T)[a(k-1)+S_T].                              (7.3)

An infinite lattice sum makes this inequality uninformative. By (7.2),
its right side is at least C_f(N/T)[a(k-1)+T]. Thus exceptionally
small lattice sums cannot evade the barrier.

### 7.2. A single scalar comparison works for every T

Let beta=liminf_{L->infinity}(C_f(L)-L), as in Theorem 1. For every
real theta<sqrt(a beta), where beta=infinity permits every finite
theta, all sufficiently large N have the following property:

    x=N^(1/4), k_N=floor(x^2+theta x)
    ==> k_N^2 <= C_f(N/T)[a(k_N-1)+T] for EVERY T>0.           (7.4)

These are scalar comparison integers, NOT constructed Sidon sets.
The threshold in N is independent of T.

Proof: choose a finite B with 0<B<beta and sqrt(aB)>theta, possible
by Theorem 1. Write L=N/T and c(L)=C_f(L)-L. By the definition of
liminf choose L_0>0 such that c(L)>=B whenever L>=L_0.
The uniform trial gives c(L)>=M_1(L)>0 for every L>0, and

    M_1(L)/L = integral min(|t|/L,1)f(t)dt
              >= M_1(L_0)/L_0 =: eta >0   (0<L<=L_0).

In particular this ratio tends to one as L decreases to zero, by
dominated convergence. For 0<L<=L_0 and large N, k_N>=1, so

    C_f(L)[N/L+a(k_N-1)] >= N(1+eta) > k_N^2.

For L>=L_0, expansion and AM--GM give, uniformly in L,

    (L+c(L))[N/L+a(k_N-1)]
      >= N + NB/L + a(k_N-1)L
      >= N + 2 sqrt(aBN(k_N-1))
       = x^4 + 2 sqrt(aB) x^3 + O(x^2).

But k_N^2=x^4+2 theta x^3+O(x^2), so sqrt(aB)>theta proves (7.4)
for all large N, simultaneously over the entire range of L. QED.

Under the separate slope hypothesis (7.1), (7.2)--(7.4) show that
k_N satisfies all exact majorized scalar inequalities simultaneously.
Thus no choice T=T(N), nor simultaneous use of all such T, excludes
every scalar comparison with coefficient below sqrt(a beta).
Equivalently, a purported bound with coefficient c<sqrt(a beta) and
a fixed additive constant is contradicted by choosing
c<theta<sqrt(a beta) in (7.4). Since a beta>=8/9, the universal floor
is 2sqrt(2)/3. For a finite intercept b, beta=b; the referee's
comparison floor(x^2+(sqrt(ab)-epsilon)x) follows for every epsilon>0.
The argument also covers a nonconvergent capacity excess when (7.1)
holds. If beta=infinity, every finite comparison coefficient survives.

### 7.3. Producing an upper bound and preserving the scope

If in addition C_f(L)=L+b+o(1) with finite b and the upper sampling
bound holds, then

    k^2<=C_f(N/T)(ak+T+O(1)).

For x=N^(1/4) and T=t x^3 with fixed t>0, the positive root is

    x^2 + (bt+a/t)x/2 + o(x).

This is an upper bound on k, not an assertion about sparse Sidon sets.
Optimizing t gives sqrt(ab). The all-T argument above, rather than
this fixed-t expansion alone, establishes the method limitation.

An o(1) capacity remainder yields an o(N^(1/4)) Sidon remainder,
not a uniform additive O(1). The sufficient assumptions
C_f(L)<=L+b+O(1/L) and a bounded sampling error give an additive O(1).
The ramp's explicit exponential remainder is stronger. The existing
effective theorem remains

    |A|<=sqrt(N)+(2sqrt(2)/3)N^(1/4)+1, N>=120^4=207360000.

No onset is lowered or declared minimal here. The barrier concerns
fixed kernels, the scalar positive-capacity inequality, nonnegative
majorization by the FULL infinite lattice difference sum, and the stated
unit-slope hypothesis. It does not cover replacing that sum by a
truncated sum restricted to d<=N.
The capacity lower bound itself needs no slope hypothesis. This is
not a barrier for other weighted Erdős--Turán arguments, extra
variance or missing-difference information, other counting majorants,
or arbitrary N-dependent kernels without uniform control. It neither
solves the original conjecture nor proves uniqueness of the optimizer.
No lattice-restricted capacity extension is asserted.

## 8. Why the proof must retain positivity and not assume a factor theorem

Allowing arbitrary finite signed probability measures gives a capacity
C_s(L)>=C_f(L), possibly infinite. Its intercept cannot automatically
replace the positive intercept. Signed measures eta_L enter only as
Cauchy--Schwarz comparison certificates; all lower-bound trials in the
capacity optimization are nonnegative.

A tempting restricted approach minimizes ||p||_2^2 times integral tp
for a nonnegative causal factor p. That moment optimization does attain
4/9 at a ramp, but it would not alone prove this report's all-kernel
result. In particular zero-free Laplace transforms do not guarantee a
finite signed half-line correction: p(t)=t exp(-t)1_[0,infinity) has
H(s)=(1+s)^(-2), while

    1/(sH(s))-1/s=2+s,

which cannot be the Laplace transform of a finite signed measure,
because such transforms are bounded for real s>0. No such factor
assumption is used in Sections 2--5.

## 9. Independent derivations, audit, and work actually performed

* Clean-room A and B each began with fresh context containing only the
  precise variational problem and Sidon convention. Both independently
  produced the same universal positive renewal certificate. Neither read
  project files, searched the web, or communicated with other workers.
* B's completed clean-room result was followed by a separately requested
  self-audit, which replaced its Fourier derivation by the exact real-space
  cancellation in Section 4. Root independently checked that cancellation.
* A supplied a separate transform derivation and a faster renewal estimate.
  The report uses the elementary contraction above instead; A's optional
  contour-integral numerical constants are not relied on here.
* A literature-only phase was completed before that worker read any
  project proof, scan or referee report. The platform then rejected both
  a new fourth worker thread and resumption of the earlier route worker
  with an agent-thread limit. The completed literature worker was reused
  for a separately identified informed route/audit phase. There were
  THREE worker identities covering the four requested roles, not four
  simultaneously running agents. The two clean-room contexts stayed isolated.
* The informed route audit independently checked the trial positivity,
  every boundary cross term, the weak-derivative cancellation, scaling,
  the capacity identity, and the explicit ramp remainder. Its reported
  verdict on these derivations is PASS. A sparse-set wording error in
  an earlier draft was repaired in Section 7.

After completion of their clean-room phases, both A and B separately read
the complete integrated report and returned PASS with no mathematical
repairs. These final reads are informed integration reviews, not additional
clean-room probes. Neither final reader independently repeated the literature
search or the earlier explicit Sidon onset proof.

The original derivation and integration reviews above are same-vendor
(OpenAI). A subsequent cross-vendor referee A report by Claude Opus,
[REFEREE_KERNEL_A_20261002.md](REFEREE_KERNEL_A_20261002.md), returned
**PASS-WITH-REPAIRS**: the two core theorems were correct, but the
all-T scope needed the short argument R1. Task 033 independently checked
and applied R1 and the proposed strengthenings S1 (liminf without an
intercept) and S2 (sampling lower bound from unit slope).
The old and new text and the integration checks are recorded in
[REPAIRS_KERNEL_APPLIED.md](REPAIRS_KERNEL_APPLIED.md).
Referee A's reported numerical checks were not independently rerun in
this integration and are not certified numerical proofs.

The root reviewer has read the newly available referee B report, which
records PASS. The integration worker did not read or incorporate that
report; the manuscript's B placeholder remains pending under the explicit
Task 033 instruction, for coordinator update. B's floating-point
experiments were not rerun or certified in this integration. The earlier
two Claude reports concern the v1 explicit Sidon bound and are not
transferred to the optimality theorem. No human or Lean/kernel
verification of the new theorem is claimed.

No git operation, publication, forum message, solver run, dependency
installation, or cloud task was performed. No numerical optimization
establishes any claim above. Token and monetary costs were not exposed
by the tools.

## 10. Bounded literature check

The literature-only worker read the following sources before consulting
any project proof, scan, or referee report. No checked source establishes
the global infimum in Section 1. This is a bounded search conclusion,
not an exhaustive novelty or priority certification.

* **Hou--Zhao, arXiv:2607.01169v3.** The relevant result is **Theorem 2.1**,
  not Lemma 2.1. It uses finite nonnegative symmetric probability kernels,
  mixing weights, and real boundary vectors subject to feasibility
  inequalities, producing a coefficient sqrt(ab). Section 3.1 poses its
  finite parameter optimization. Lemma 3.1 solves the boundary quadratic
  program only with kernels and mixing fixed. Proposition 2.2 assumes
  individually feasible constituent certificates. Section 3.4 expressly
  disclaims global optimality, including for its scalar numerical search.
  Its boundary cost is not identified with our exact continuous positive
  capacity correction. [Theorem 2.1](https://arxiv.org/html/2607.01169v3#S2.Thmtheorem1),
  [optimization](https://arxiv.org/html/2607.01169v3#S3.SS1),
  [limitations](https://arxiv.org/html/2607.01169v3#S3.SS4).

* **Carter--Hunter--O'Bryant, arXiv:2310.20032v1.** Theorem 1.1 is the
  Erdős--Turán Sidon Set Equality, retaining rectangular-window variance
  and weighted missing differences. Lemmas 3.1--3.2 exploit endpoint
  variance and several window lengths; Section 3.2.2 combines piecewise
  affine estimates by linear programming. The parameter search is local.
  No theorem about the infimum of the functional in Section 1 was found.
  Inference: this is related endpoint methodology, not a solution of our
  kernel variational problem.
  [Theorem 1.1](https://arxiv.org/html/2310.20032v1#S1.Thmtheorem1),
  [Section 3.2.2](https://arxiv.org/html/2310.20032v1#S3.SS2.SSS2).

* **Gupta--O'Bryant, arXiv:2605.14229v1, Theorem 13, Section 5.3.** For
  LM rulers, the positive difference d has multiplicity at most d-1.
  Sorting the n-1 consecutive gaps gives s_(i)>sqrt(2i); integration of
  sqrt(2t) then yields diameter at least (2sqrt(2)/3)(n-1)^(3/2).
  There is no autocorrelation, capacity or half-line optimization in
  this argument. Its identical coefficient does not solve, or certify
  an optimum for, the present problem.
  [Section 5.3](https://arxiv.org/html/2605.14229v1#S5.SS3).

* **Alfonsi--Schied, arXiv:1201.2756v4.** Section 1.1 distinguishes positive
  and signed energy minimization. Their explicit results concern
  completely monotone G, with G''(0+)<infinity for the main characterization.
  Corollary 1 describes endpoint atoms and a continuous interior density;
  Theorem 2 and Corollary 2 use Riccati and Volterra equations. Their
  energy includes a factor 1/2, so its reciprocal is twice our capacity
  for the same kernel. These are results for restricted fixed kernels,
  not optimization over all autocorrelations.
  [Primary paper](https://arxiv.org/pdf/1201.2756v4).

* **Leinster--Roff, arXiv:1908.11184.** Theorem 8.1 expresses magnitude
  using signed measures and the exponential metric kernel. Lemma 8.2
  identifies the positive problem when a positive weight measure exists.
  Example 8.4 gives the interval measure (delta_0+delta_l+Leb)/2 and
  magnitude 1+l/2. Lemma 7.7 and Proposition 6.3 concern the positive
  equilibrium potential inequality and its contact set. This supports
  retaining the positivity condition; it supplies no universal optimum
  for the kernels of Section 1.
  [Primary paper, Sections 7--8](https://arxiv.org/html/1908.11184).

* **Gimperlein--Goffeng--Louca, arXiv:2201.11357v2.** Theorems 1.1, 1.3,
  1.4 and Section 5.2 give boundary expansions and Wiener--Hopf analysis
  for exp(-R d(x,y)) on suitable compact manifolds with boundary. The
  inverse is constructed in Sobolev spaces and may be distributional;
  the associated energy formulation permits signed measures. Inference:
  this framework cannot be applied as a ready-made positive-capacity
  theorem for arbitrary f=h*h~.
  [Primary paper](https://arxiv.org/html/2201.11357).

* **Spectral-factor qualification.** Fejér--Riesz factorization does not
  assert nonnegative coefficients of its factor.
  [Dritschel--Rovnyak, p. 2](https://uva.theopenscholar.com/files/james-rovnyak/files/p71.pdf).
  Ewerhart--Serena, Definition 1, Lemma 2 and Section 2.4, discuss the
  stronger probability question of representing a distribution as X-Y
  for iid X,Y, and explain why a nonnegative characteristic function
  alone is insufficient. The older counterexample they cite was not
  independently inspected in this search.
  [Author-hosted paper](https://ewerhart.net/files/2024%20Ewerhart%20Serena%20MathOR%20On%20the%20(Im-)possibility%20of%20Representing%20Probability%20Distributions.pdf).
