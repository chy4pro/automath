# Sonar sequences: exact-marginal capacity transfer

Status: **INFORMED; Stage A PASS-WITH-REPAIRS; Stage B proved analytically.**
This is a verification and proof report, not a novelty or priority claim.
No Lean verification of this transfer is claimed.

## 1. Model, source check, and referee verdict

For integers n,m >= 1, an n-row, m-column sonar sequence is a sequence

    y_0,...,y_(m-1) in {0,...,n-1}

such that, for every d in {1,...,m-1}, the m-d integers

    y_(j+d) - y_j,  0 <= j < m-d,

are distinct. Equivalently, all vectors (j-i,y_j-y_i), 0 <= i < j < m,
are distinct. There is exactly one point in every column; repeated row
values are allowed. Reversing each ordered pair changes the sign of the
first coordinate, so all nonzero ordered difference vectors are distinct
as well. There is no modular reduction and no restriction of one point
per row.

This agrees with the authors' model in the primary publisher abstract of
Erdos--Graham--Ruzsa--Taylor, *Bounds for arrays of dots with distinct
slopes or lengths*, Combinatorica 12 (March 1992), 39--44:
[publisher abstract](https://link.springer.com/article/10.1007/BF01191203).
The [UCSD author-hosted scan](https://mathweb.ucsd.edu/~ronspubs/92_02_distinct_slopes.pdf)
was reachable by HTTP and the web PDF reader, but contained no extracted
text; the screenshot interface returned no visible image in this session.
Thus the definition check uses the primary publisher abstract; no claim
is made here to have inspected the scan's theorem/proof pages. Access was
on 2026-10-02, approximately 20:51--20:55 UTC. The publication date and
the access date are distinct. No bounded literature search for later
bounds was performed.

**Verdict on the scout's sandwich (S): PASS-WITH-REPAIRS.** The exact
column-marginal step is valid, including with a signed capacity witness.
The repairs needed for a complete proof are:

1. Require 1 <= T1 <= m with T1 integral, and 0 < T2 <= n.
2. Prove Lambda > 0 before cancelling it from signed-energy
   Cauchy--Schwarz. In fact Lambda >= m > 0.
3. Dilate the signed measure by pushforward, without multiplying its mass
   by T2. Its energy is unchanged under the corresponding kernel dilation.
4. Do not assume m = n + O(n^(2/3)) to derive that same estimate: solve the
   resulting linear inequality in m, with a positive coefficient.
5. If the chosen T1 exceeds m, handle that case separately.
6. Replace the numerical '+2.62 n^(1/3)' scan by proved error estimates.

## 2. Explicit theorem

**Theorem.** Every n-row, m-column sonar sequence satisfies

    m <= n + 2 n^(2/3) + 3 n^(1/3)                 (1)

for every integer n >= 48^3 = 110592. In particular

    m <= n + 2 n^(2/3) + O(n^(1/3)),

where the remainder is bounded by 3 n^(1/3), uniformly over all sonar
sequences with the given number of rows.

The constants and onset in (1) are conservative proof constants. The
coefficient 2 is the triangle-in-x/ramp-in-y coefficient, not a claim of
optimality among x-kernels.

## 3. Analytic input, including signed-measure conventions

Write

    f1(t) = (1-|t|)_+,
    h(t) = 2(1-t) 1_[0,1](t),
    f2(t) = (h * reverse(h))(t)
          = 4/3 - 2|t| + (2/3)|t|^3  for |t| <= 1,
          = 0                         otherwise.

Both kernels are even, nonnegative, continuous autocorrelations of real
L1 intersection L2 functions; their integrals are one. Set

    a = f2(0) = 4/3,   b = 2/3,   alpha = log(4/3).

The complete elementary construction and proof of the following signed
witness lemma are included in [COMMON_CAPACITY.md](COMMON_CAPACITY.md),
the common appendix to this transfer package (original Lemmas 2--6):

For every real L >= 1 there is a finite signed real Borel measure nu_L
on R, of finite total variation, such that

    integral f2(t-s) dnu_L(s) = 1     for every t in the CLOSED [0,L],
    0 <= C_L := integral integral f2(s-t) dnu_L(s)dnu_L(t)
       <= L + 2/3 + 200 exp(-alpha L).                  (2)

The measure nu_L need not be positive or supported on [0,L]. Neither
property is used here. In the appendix it is

    nu_L = 1_[0,L] dt + q + reflect_L(q),
    q = (1/2) sum_(r>=0) U^(*r) - 1_[0,infinity) dt,

where U is uniform on [0,1). The quantitative inputs are

    q(R)=1/3,  ||q||_TV <= 9/2,
    |q|((L,infinity)) <= 6 exp(-alpha L).

The exact half-line convolution identity gives potential one, its global
absolute value is at most 13, and the energy-minus-mass error is at most
14*12 exp(-alpha L) <= 200 exp(-alpha L). This explains the constants
in (2), rather than treating (2) as a numerical capacity estimate.

For completeness concerning products, put

    H(x,y) = (T1*T2)^(-1/2) 1_[0,T1](x) h(y/T2).

Its autocorrelation is

    F(x,y) = f1(x/T1) f2(y/T2).

For any finite signed real measures sigma,tau on R^2, Fubini and ordinary
L2 Cauchy--Schwarz give

    E_F(sigma,tau) = integral (H*sigma)(z)(H*tau)(z) dz,
    |E_F(sigma,tau)|^2 <= E_F(sigma,sigma) E_F(tau,tau).  (3)

Absolute integrability follows, for example, from

    integral |H(z-u)H(z-v)| dz <= ||H||_2^2

and the finite total variations of sigma and tau. Thus (3) permits the
signed witness used below. No positive/signed capacity interchange is
being made.

## 4. Exact finite sandwich

Let T1 be an integer with 1 <= T1 <= m and let 0 < T2 <= n. Define

    mu = sum_(j=0)^(m-1) delta_(j,y_j),
    lambda = sum_(j=0)^(m-1) delta_j,
    L = n/T2,
    rho = pushforward_(t -> T2*t)(nu_L),
    nu = lambda tensor rho.

The row coordinates lie in [0,n-1], which is contained in [0,n]; hence
(2) gives

    integral f2((y_j-s)/T2) drho(s) = 1.

The pushforward has no additional factor of T2. Its energy for the
scaled y-kernel is exactly C_L. Let

    Lambda = sum_(i,j=0)^(m-1) f1((i-j)/T1).

Since lambda is the EXACT column marginal,

    E_F(mu,nu) = Lambda,
    E_F(nu,nu) = Lambda C_L.                            (4)

Here Lambda >= m > 0, because all its terms are nonnegative and each
diagonal term is one. In fact C_L > 0 as well: apply one-dimensional
(3) to delta_t and nu_L for any t in [0,L], obtaining 1 <= a C_L.
From (3)--(4), cancelling only the positive quantity Lambda, we obtain

    Lambda <= E_F(mu,mu) C_L
           <= E_F(mu,mu) (n/T2 + 2/3 + 200(3/4)^(n/T2)). (5)

Every off-diagonal ordered difference of mu is different and has nonzero
first coordinate. Since F >= 0, dropping the requirement that a difference
is actually realized gives

    E_F(mu,mu)
      <= (4/3)m + (sum_(d != 0) f1(d/T1))
                         (sum_(e in Z) f2(e/T2))
      <= (4/3)m + (T1-1)(T2+4/3).                      (6)

The first lattice sum is exactly T1-1. For the second, f2 is decreasing
and nonnegative on [0,infinity), so comparison of each right Riemann
rectangle with its integral gives

    sum_(e>=1) f2(e/T2) <= T2 integral_0^infinity f2 = T2/2.

The diagonal contribution to (6) is (4/3)m, not m and not (4/3)m^2.
The factor two for reversed ordered differences is already included in
the lattice sum over d != 0.

Finally, direct finite summation, using T1 <= m, gives

    Lambda = m + 2 sum_(d=1)^(T1-1) (m-d)(1-d/T1)
           = m T1 - (T1^2-1)/3.                       (7)

Equations (5)--(7) prove exactly

    m T1 - (T1^2-1)/3
      <= (n/T2 + 2/3 + 200(3/4)^(n/T2))
           ((4/3)m + (T1-1)(T2+4/3)).                 (S)

This establishes the scout's new step without an assumption about the
size of m.

## 5. Explicit all-n algebra after the onset

Put x=n^(1/3) >= 48, and choose

    T2 = x^2,      U=T1=ceil(2x^2).

Then 2x^2 <= U < 2x^2+1 <= n and T2 <= n. If m < U, then m < n and
(1) is immediate. Hence assume U <= m, so (S) applies.

First control the exponential without a decimal estimate. Since

    alpha = integral_1^(4/3) dt/t >= 1/4,

the function x^2(3/4)^x is decreasing for x >= 8. Moreover

    (3/4)^8 = 6561/65536 < 1/9,
    200*48^2 = 460800 < 9^6 = 531441.

Consequently, for every real x >= 48,

    epsilon := 200(3/4)^x < x^(-2).                    (8)

Set C=x+2/3+epsilon and C0=x+2/3+x^(-2). Solving (S) linearly in m,
after dividing by U, yields

    m (1-aC/U)
       <= U/3 - 1/(3U) + C(1-1/U)(x^2+a),   a=4/3.    (9)

Define

    q = 2/(3x) + 4/(9x^2) + 2/(3x^4).

Then aC/U <= q < 1/2; the latter follows already for x >= 2 by bounding
the three terms by 1/3, 1/9, 1/24, whose sum is 35/72 < 1/2. Thus the
coefficient of m in (9) is positive. No asymptotic bootstrap is assumed.

Because C >= x and 2x^2 <= U <= 2x^2+1, the right side of (9) is at most

    (2x^2+1)/3 + C0(x^2+4/3) - x^3/(2x^2+1).

Use the elementary inequality

    x^3/(2x^2+1) >= x/2 - 1/(4x)

to bound this expression by

    B(x) = x^3 + (4/3)x^2 + (5/6)x + 20/9
                   + 1/(4x) + 4/(3x^2).              (10)

It follows from m>0 and (9) that m(1-q) <= B(x). Put

    Y(x)=x^3+2x^2+3x.

An exact polynomial identity is

    36x^3 [Y(x)(1-q)-B(x)]
       = 14x^4 - 184x^3 - 81x^2 - 96x - 72
       = 14t^4 + 712t^3 + 12591t^2 + 85376t + 141496,
                                                        t=x-16.

All coefficients in the last expression are positive. Hence
Y(x)(1-q)>B(x) for every x>=16, in particular for x>=48. Since 1-q>0,

    m <= B(x)/(1-q) < Y(x),

which proves (1), with a strict inequality available at this onset.
Every estimate is uniform over the sonar sequence.

## 6. Exact checks and their limits

[check_sonar.js](check_sonar.js) is a dependency-free Node.js/BigInt checker.
It uses rational arithmetic and exact integer comparisons, never a
floating-point tolerance. Its tasks are:

* verify (7) for every 1 <= T1 <= m <= 40;
* exhaust all sonar prefixes for 1 <= n <= 4 and 1 <= m <= 2n, permitting
  repeated row values, and check (5), (6), and (S) for every integer
  1 <= T1 <= m and every T2 in {1/2,1,...,n};
* enclose (3/4)^(n/T2) by exact rational lower/upper bounds, obtained by
  integer power comparisons, so the small checks of (5) imply the stated
  real inequality rather than merely checking a looser floor-exponent
  version;
* reject a repeated-row non-sonar negative control through (6);
* verify the rational exponential base inequalities, the Laurent
  polynomial identity in Section 5, and its positive-coefficient shift.

The bound m<=2n used only to delimit the small enumeration is immediate
from column gap one: its m-1 vertical differences are distinct elements
of {-(n-1),...,n-1}, which has 2n-1 members. Every shorter sonar sequence
occurs as a prefix in this enumeration. These finite checks are an
independent error check, not the proof of the theorem for all n.

Actual run on 2026-10-02 UTC: `node check_sonar.js` exited 0 with PASS.
It checked 820 marginal identities, 60 lattice identities/inequalities,
1070 sonar sequences/prefixes, and 41856 scale-specific energy sandwiches.
Twenty exact power enclosures were reused. The negative control had
energy 76/9 greater than its invalid purported upper bound 23/3 and was
correctly rejected. The polynomial identity and all coefficients of its
shift by 16 checked exactly. The complete analytic proof is Sections
3--5 together with the full signed-witness appendix linked in Section 3.
