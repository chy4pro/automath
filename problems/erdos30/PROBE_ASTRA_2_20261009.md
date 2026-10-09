PARTIAL — proved exact second/third window-moment identities, an explicit limitation of the tested third-moment relaxation, and an infinite family of Sidon sets realizing both proposed endpoint clusters. No bound with c < 2sqrt(2)/3 is proved.

# Scope and conventions

This is a clean-room report for AUT-13, using only its supplied brief and elementary mathematics. I did not read the repository, other agents' files, papers, or the web. The only non-brief instructions read were the Paperclip workflow skill outside /work. There was no existing file at this report's assigned path.

A Sidon set means a finite set A of integers whose positive differences a-b, a>b, are all distinct. This is equivalent to uniqueness of unordered sums, including repeated summands: an equality of two positive differences gives an equality of two unordered sums, and conversely a nontrivial equality of sums can be rearranged to equal positive differences. Write m=|A| and A subset {1,...,N}.

The known bound and kernel barrier in the brief are taken as premises, not re-proved here. The brief does not specify f or C(N,T), or give an exact quantified theorem forcing its approximate endpoint profile. Consequently the window energy defined below is an explicitly chosen test of seed (a); it is not asserted to be the brief's optimized residual energy. The endpoint construction tests a necessary part of seed (b), not the simultaneous dense-bulk/saturation profile.

There are no unspecified asymptotic error terms in the proved statements below.

# 1. Seed (a): exact identities and available third-order inequalities

Let N,T be positive integers with 1<=T<=N. Put W=N+T-1 and, for 1<=x<=W, define

    r(x) = |A intersect [x-T+1,x]|.
    S = mT,  mu = S/W.
    D(d) = |{(a,b) in A^2: a<b, b-a=d}|.
    P = sum_{d=1}^{T-1} (T-d) D(d).
    H = sum_{a<b<c in A} max(0,T-(c-a)).
    Q = sum_{x=1}^W (r(x)-mu)^2.
    R = sum_{x=1}^W (r(x)-mu)^3.

For a Sidon set, D(d) is either 0 or 1.

## 1.1 Exact moment formulas

The following hold, including for the empty set:

    sum r(x)   = S;
    sum r(x)^2 = S+2P;
    sum r(x)^3 = S+6P+6H.                              (1)

Proof. A point a belongs to exactly the T windows with a<=x<=a+T-1. A pair a<b belongs to exactly max(0,T-(b-a)) common windows. A triple a<b<c belongs to exactly max(0,T-(c-a)) common windows. Apply the integer identities

    u^2 = u+2 binom(u,2),
    u^3 = u+6 binom(u,2)+6 binom(u,3)

and sum over the windows. This proves all three formulas.

The Sidon condition and the arithmetic-series identity give

    sum r(x)^2 <= mT+2 sum_{d=1}^{T-1}(T-d)
               = mT+T(T-1).                           (2)

For the triangular kernel g(u)=max(0,1-|u|), define the auxiliary energy

    V_tri(A) = sum_{a,b in A} g((a-b)/T) - m^2 T/W.

Formula (1) gives

    V_tri(A) = Q/T >= 0.                               (3)

Indeed the first term is (sum r(x)^2)/T, and
Q=sum r(x)^2-S^2/W. Nonnegativity follows by summing squares. This kernel is positive definite because its unnormalized values T g((a-b)/T) are the inner products of the indicator vectors of [a,a+T-1] and [b,b+T-1]. Here W/T is just the normalization from this elementary window calculation; no optimal-capacity assertion is made.

Expanding the centered cube, substituting (1), and using sum r^2=W mu^2+Q gives the exact third-order identity

    6H = W mu(mu-1)(mu-2) + 3(mu-1)Q + R.             (4)

In detail,
R=sum r^3-3mu sum r^2+2Wmu^3,
while sum r^3=3 sum r^2-2S+6H. Substitution yields
R=6H+3(1-mu)Q-Wmu(mu-1)(mu-2), which is (4).

Thus a proposed lower bound for H cannot by itself be substituted for a lower bound for Q: R must also be controlled.

## 1.2 The integrality contribution is too small at this scale

Let q=floor(mu), theta=mu-q. For every integer u,

    (u-q)(u-q-1) >= 0.

Summing this inequality with u=r(x), and using S=W(q+theta), gives

    Q >= W theta(1-theta).                            (5)

Equality holds precisely when every r(x) belongs to {q,q+1}. Such integer arrays with total S always exist, since Wtheta=S-qW is an integer between 0 and W-1.

The right side in (5), after division by T, is at most W/(4T), since
theta(1-theta)=1/4-(theta-1/2)^2<=1/4. If T=floor(N^(3/4)), then T>=N^(3/4)/2 and W<=2N, so

    W/(4T) <= N^(1/4).
    [W theta(1-theta)/T]/m <= 2 N^(-1/4)
        whenever m >= sqrt(N)/2.                      (6)

The floor inequality used here follows from floor(y)>=y/2 for y>=1. Formula (6) bounds the contribution guaranteed by (5); it is not an upper bound on the actual energy of a Sidon set.

A basic cubic nonnegativity inequality is also available:

    sum r(x)^3 >= (2q+1) sum r(x)^2 - q(q+1)S.        (7)

This follows because u(u-q)(u-q-1)>=0 for nonnegative integers u. Cauchy-Schwarz gives, for S>0,

    sum r(x)^3 >= (sum r(x)^2)^2/S,                  (8)

by applying it to r(x)^(3/2) and r(x)^(1/2). Neither adds a positive constant times m to (3) in the relaxation tested below.

## 1.3 Bounds from unique third-order correlations

For integers 0<u<v, let

    C_3(u,v) = |{a: a,a+u,a+v all belong to A}|.

Then C_3(u,v)<=1: two different starting points would repeat the positive difference u. Also

    H = sum_{0<u<v<T} (T-v) C_3(u,v)
      <= sum_{v=2}^{T-1} (v-1)(T-v)
       = binom(T,3).                                 (9)

The last sum counts triples of distinct integers from {1,...,T} by their largest-minus-smallest span, or follows by expanding the quadratic summand.

There is a stronger elementary bound. Define

    k_d = floor((sqrt(1+8d)-3)/2),   d>=1;
    U_T = sum_{d=1}^{T-1} (T-d) k_d.

Then

    H <= U_T <= sqrt(2T) T(T-1)/2.                    (10)

To prove the first inequality, fix endpoints a<c of difference d<T. If q0=|A intersect [a,c]|, its binom(q0,2) distinct positive differences all lie in {1,...,d}. Hence q0(q0-1)<=2d, so the number of intermediate points is q0-2<=k_d. There is at most one endpoint pair of each difference d. Summing its contribution proves H<=U_T. Finally k_d<=sqrt(2d)<=sqrt(2T), and sum_{d=1}^{T-1}(T-d)=T(T-1)/2. For example, the first of these inequalities follows already from k_d(k_d+1)<=2d, which is weaker than (k_d+2)(k_d+1)<=2d.

For use in comparing the strength of this bound, there is also an explicit lower bound on its numerical right side:

    U_T >= T^(5/2)/64,  for every integer T>=64.      (11)

For ceil(T/4)<=d<=floor(T/2), there are at least T/4-1>=T/8 integer choices, and T-d>=T/2. The floor formula gives

    k_d >= sqrt(2d)-5/2
        >= sqrt(T/2)-5/2
        >= sqrt(T)/4.

For the last inequality, use 1/sqrt(2)>=5/8 and sqrt(T)>=8; then
sqrt(T)(1/sqrt(2)-1/4)>=3sqrt(T)/8>=3>=5/2.
Multiplying these three lower bounds proves (11).

## 1.4 A rigorous limitation of this particular moment relaxation

Proposition. For every integer s>=65536 and every integer m with

    s^2 <= m <= s^2+s,

put N=s^4, T=s^3, W=N+T-1. There exist nonnegative integer arrays r(1),...,r(W), and binary numbers D(1),...,D(T-1), with the following properties:

* The mass identity and pair identity in (1), and the Sidon pair upper bound (2), hold.
* With H=sum_x binom(r(x),3), the third identity in (1), the centered identity (4), integrality inequality (5), and inequalities (7),(8) hold.
* The numerical third-order upper bounds H<=U_T and H<=binom(T,3) both hold.
* Nevertheless

      Q/(Tm) <= 1/(2s).                              (12)

These arrays are not asserted to come from a set A. In particular this proposition is about the explicitly listed scalar constraints, not about all third-order correlation consistency conditions.

Proof. Let S=mT, q=floor(S/W), and k=S-qW. Take k entries equal to q+1 and the remaining W-k entries equal to q. They have total S and

    Q = k(W-k)/W <= W/4.

The largest permitted mass is

    S_max=(s^2+s)s^3=s(W+1).

At this mass, q=s and k=s, so every entry is at most s+1. The minimum value of sum r(r-1) at a given integer mass is attained by a balanced array: replacing entries u,v with u-1,v+1 when u>=v+2 decreases that sum by 2(u-v-1)>0. This minimum is nondecreasing with mass, since increasing the mass of a balanced array by one increases the minimum by 2q>=0. Therefore at every permitted m,

    sum r(r-1) <= W s(s-1)+2s^2
                = s^6-s^4+s^2+s
                <= s^6-s^3 = T(T-1).

The last inequality is equivalent to s^4-s^3-s^2-s>=0. For s>=2 it follows from
s^3-s^2-s-1>=s^2-s-1>=1.

Set P=(sum r(r-1))/2. It is an integer between 0 and T(T-1)/2. Every integer in this range is a sum of a subset of {1,...,T-1}. One proof is induction: the attainable ranges without and with the largest weight j are [0,j(j-1)/2] and [j,j+j(j-1)/2], which are adjacent or overlap for j>=2; j=1 is immediate. Choose D(d) in {0,1} so that sum (T-d)D(d)=P. This proves the required mass and pair identities and inequality.

The third identity holds by the polynomial identity for cubes, and (4),(5),(7),(8) hold for this actual integer array. Because r(x)<=s+1 and W<=2s^4,

    H <= W(s+1)^3/6
      <= (8/3)s^7
      < 4s^7
      <= s^(15/2)/64
      <= U_T.

Here s+1<=2s gives the second inequality; sqrt(s)>=256 gives the penultimate inequality; and (11) gives the last one.

The other third-order upper bound holds as well. For T>=4,

    binom(T,3)=T(T-1)(T-2)/6 >= T^3/24.

Indeed T-1>=T/2 and T-2>=T/2. Thus binom(T,3)>=s^9/24>=(8/3)s^7 for s>=8.

Finally,

    Q/(Tm) <= W/(4Tm)
             <= (s+1)/(4s^2)
             <= 1/(2s),

using W=s^4+s^3-1, T=s^3, m>=s^2 and s>=1. This proves the proposition.

Its exact obstruction is that these mass, pair, integrality, and scalar third-order conditions admit arbitrarily small Q/(Tm), even for cardinalities throughout the second-order range in question. Any successful route must add a condition excluding these arrays. Window boundary conditions and compatibility of the individual C_3(u,v) with a single set are not enforced here.

## 1.5 An actual Sidon example separating pair and third-order data

Consider

    A = {1,2,5,11,13,18},
    B = {1,2,9,12,14,18}.

Each has the following fifteen positive differences, each exactly once:

    {1,2,3,4,5,6,7,8,9,10,11,12,13,16,17}.

This verifies directly that both are Sidon and have identical pair statistics. For N=18 and T=5,

    W=22, S=30, P=10,
    H(A)=1, H(B)=0,
    sum r_A^2=sum r_B^2=50,
    sum r_A^3=96, sum r_B^3=90,
    Q(A)=Q(B)=100/11,
    V_tri(A)=V_tri(B)=20/11.

The only triple of span less than 5 in A is {1,2,5}, of span 4; there is none in B. The displayed moments then follow from (1).

More generally, these two sets give identical sum_{a,b} f((a-b)/T) for every function f and positive T, since all ordered difference multiplicities agree. With the same N,m,C(N,T), their residual energies also agree. Their third moments differ because R changes by exactly 6 in (4). This does not refute a universal residual-energy theorem; it identifies why using H without simultaneous control of R is insufficient.

# 2. Seed (b): both proposed endpoint clusters are realizable

The following infinite construction is unconditional.

Proposition. For every odd prime p>=61, set

    m=(p-1)/2,
    N=ceil((100m/69)^4),
    L=floor(N^(3/4)/10).

There is a Sidon set A subset {1,...,N} of size 2m with exactly m points in each of [1,L] and [N-L+1,N]. Moreover

    0 <= (69/100) N^(1/4)-m <= 1/(4m^3),             (13)
    0 <= N^(3/4)/10-L < 1.                           (14)

The clusters can in fact both be confined to windows of length 8m^2+3.

Proof. For 0<=i<=p-2 let r_i be the least nonnegative residue of i^2 modulo p, and set

    b_i=2pi+r_i.

The sequence is strictly increasing because b_{i+1}-b_i>=2p-(p-1)=p+1.

First prove that the set of b_i is Sidon. Suppose, with j>i and l>k,

    b_j-b_i=b_l-b_k.

Then

    2p[(j-i)-(l-k)] = (r_l-r_k)-(r_j-r_i).

The right side has absolute value at most 2(p-1)<2p. Thus j-i=l-k=h. Reducing the equality of residue differences modulo p gives

    h(j+i) = h(l+k) (mod p).

Since 1<=h<p, h is invertible modulo p. Substituting j=i+h and l=k+h gives 2i=2k modulo p. The prime is odd, so i=k modulo p. Both indices lie between 0 and p-2, hence i=k and j=l. This proves uniqueness of positive differences.

Put

    B0=b_{p-2}=2p(p-2)+4=8m^2+2.

The residue is 4 because p>=61. Split the 2m marks into their first and last m marks, and define

    A_left  = {1+b_i: 0<=i<m},
    A_right = {N-B0+b_i: m<=i<=2m-1},
    A=A_left union A_right.

All internal differences within either block are distinct, including across the two blocks, since they are differences of distinct pairs of the original Sidon set. Every difference from the right block to the left block is

    N-B0-1 + (b_j-b_i),  i<m<=j.

They too are distinct, by the same Sidon property. They exceed B0 as soon as N>2B0+1, so they cannot equal an internal difference, all of which are at most B0.

That required inequality holds: (100/69)^4>4, so N>4m^4>16m^2+5=2B0+1 for m>=30. For the strict middle inequality, 4m^4-16m^2=4m^2(m^2-4)>5 already for m>=3. Thus A is Sidon.

Now verify the endpoint locations with an explicit onset. Since m>=30,

    L >= (100000/328509)m^3-1
      > (3/10)m^3-1
      >= 9m^2-1
      >= 8m^2+8m+2
       = 2p^2.

Here 100000/328509>3/10 follows by cross multiplication; (3/10)m>=9; and
m^2-8m-3>0 for m>=30, since m(m-8)-3>=30*22-3>0.
As B0+1<2p^2, the left block lies in [1,L], and the right block lies in [N-L+1,N]. Both actually lie in the endpoint windows of length B0+1=8m^2+3. The two L-windows are disjoint because 2L<=N^(3/4)/5<=N/5<N. This also verifies that the counts in those windows are exactly m.

For (13), put x=100m/69. Then 0<=N-x^4<1. The function t^(1/4) has decreasing derivative (1/4)t^(-3/4), so integration over [x^4,N] gives

    0 <= N^(1/4)-x <= 1/(4x^3).

After multiplication by 69/100, the error is at most
(69/100)^4/(4m^3)<1/(4m^3). Formula (14) is the defining floor inequality. This completes the proof.

There are infinitely many such primes: if there were only finitely many primes, their product plus one would have a prime divisor absent from the list. Only finitely many are below 61. Hence the proposition is an infinite family with the endpoint constants 0.69 and 0.1 specified in the brief, with explicit rounding bounds.

Limitation. This construction has only 2m points in total, not approximately sqrt(N). It does not saturate the short differences: in particular difference 1 is absent, since internal positive differences are at least p+1 and cross differences are larger still. It neither realizes nor disproves the complete extremal profile. It proves that the two endpoint clusters alone, even taken together, are not contradictory.

## 2.1 Elementary endpoint difference budgets

If a Sidon set has q points in each of [1,L] and [N-L+1,N], with the two windows disjoint, uniqueness implies

    q(q-1) <= L-1,          from the two internal difference sets;
    q^2 <= 2L-1,           from the cross differences.               (15)

The first uses 2 binom(q,2) distinct differences in {1,...,L-1}. The second uses q^2 distinct differences in [N-2L+1,N-1], an interval of 2L-1 integers.

For q=floor((69/100)N^(1/4)), L=floor(N^(3/4)/10), and N>=256, their demand-to-capacity ratios satisfy

    q(q-1)/(L-1) <= (4761/500) N^(-1/4);
    q^2/(2L-1) <= (4761/1000) N^(-1/4).              (16)

Indeed q^2<=4761 N^(1/2)/10000,
L-1>=N^(3/4)/10-2>=N^(3/4)/20, and
2L-1>=N^(3/4)/5-3>=N^(3/4)/10.
Both last inequalities hold at N=256 and thereafter because N^(3/4)>=64.
For N>=10000 both ratios are below 1. Thus the most direct counting inequalities have substantial slack at the proposed endpoint parameters.

# 3. Other attempted closures and their exact obstructions

The following were considered in addition to the detailed moment and endpoint routes. None gives the target.

1. Third-correlation uniqueness alone. This gives (9). The sharper span-capacity argument gives (10). Proposition 1.4 shows that even the stronger scalar upper bound, together with the tested moment and integrality conditions, permits Q/(Tm)<=1/(2s). What is missing is compatibility of individual third correlations, window positions, and the full family of pair constraints.

2. Integrality or jump-size fluctuations. Integrality gives only (5), with its explicitly vanishing normalized contribution (6). For the jump calculation, extend r by zero and write
   r(x)-r(x-1)=1_A(x)-1_A(x-T). Therefore

       sum_x (r(x)-r(x-1))^2 = 2m-2D(T).

   This identity alone does not yield order m for V_tri. Since (u-v)^2<=2u^2+2v^2, the elementary full-line estimate only gives sum r^2>=(m-D(T))/2; after division by T it is at scale m/T and does not even subtract the large mean component needed for Q. A strengthened estimate involving positions of jumps was not proved. Sparse endpoint transitions are not themselves impossible, as Section 2 illustrates.

3. Rank-gap telescoping. If A={a_1<...<a_m} and 1<=h<=m-1, consider the
   M=hm-h(h+1)/2 distinct positive differences a_{i+j}-a_i with 1<=j<=h. Their sum is at least M(M+1)/2. For each j, telescoping bounds the sum by j(N-1), because only the first and last j terms remain and each paired difference is at most N-1. Thus

       M(M+1) <= h(h+1)(N-1).

   At N=s^4, h=s, this implies
   m <= (s+1)/2 + sqrt((s+1)(s^4-1)/s)
     <= s^2+s+1/2,
   whenever h<=m-1. The last step uses sqrt(1+1/s)<=1+1/(2s), obtained by squaring the nonnegative right side. If h>m-1 then m<=s and the same final bound is immediate. This standard telescoping choice gives coefficient 1, and no extra inequality improving it was obtained.

4. Fourth Fourier moment. For F(t)=sum_{a in A} exp(2 pi i a t), orthogonality of integer exponentials gives

       integral_0^1 |F(t)|^4 dt
          = m^2+2 sum_{d>=1} D(d)^2
          = 2m^2-m.

   The last equality uses D(d)^2=D(d) and sum D(d)=binom(m,2).
   Thus this identity is already determined by the pair data. I did not obtain an additional localization inequality giving the requested residual gap from it. No claimed Fourier improvement is hidden here.

5. Counting representations as three distinct summands. Distinct unordered triples with the same sum cannot share a point: cancelling a shared point would violate uniqueness of the remaining pair sum. Therefore at most floor(m/3) such triples have any one sum. There are at most 3N possible sums, giving

       binom(m,3) <= 3N floor(m/3) <= Nm.

   For m>0 this gives only (m-1)(m-2)<=6N, much weaker even in the leading constant. It does not constrain the proposed endpoint clusters at the relevant scale.

6. Endpoint gluing and local difference packing. Equations (15)-(16) are too weak, and Section 2 supplies actual simultaneous endpoint clusters. The missing condition is their coexistence with a bulk of size approximately sqrt(N) and near saturation of every short difference. No quantitative contradiction from those simultaneous conditions was established.

The unresolved target is exactly the one in the brief: an effective argument giving a fixed c<2sqrt(2)/3 and a quantified remainder for all sufficiently large N. In particular, no positive kappa for the brief's optimized V_T(A) has been established. The missing f and C specifications would be needed for an exact residual calculation, but merely specifying them would not close the mathematical gaps above.

# 4. Exact computational checks

All computations were local Node.js v22.23.1, with one computational thread, V8's single-threaded flag, V8 pool size 1, and UV_THREADPOOL_SIZE=1. No SAT/ILP solver, numerical optimizer, external package, network research, or paper was used.

## 4.1 Exhaustive Sidon subsets

I enumerated every Sidon subset of {1,...,N} for each 1<=N<=24, including the empty set and all translates. The recursion visits the current increasing set A and then tries every a>max(A). It accepts an extension precisely when none of the differences a-b, b in A, is already used. New differences are mutually distinct automatically. This proves the recursion is exhaustive and introduces no non-Sidon sets.

For N<=16, I checked (1), (2), (5), (7), H<=U_T, and (4) for every T=1,...,N. The final verification used integer arithmetic exclusively: k_d was found by incrementing the maximum q0 with q0(q0-1)<=2d, rather than by floating-point square roots. The identity (4) was checked after multiplication by W^2. All numbers in those checks were below 2^53, so JavaScript integer-valued Number operations were exact.

There were 6,276 checked set instances and 87,240 checked (N,A,T) instances in that final pass. No check failed.

The exhaustive counts and maxima were:

| N | Number of Sidon subsets | F(N) | Largest D with every difference 1,...,D present |
|---:|---:|---:|---:|
| 1 | 2 | 1 | 0 |
| 2 | 4 | 2 | 1 |
| 3 | 7 | 2 | 1 |
| 4 | 13 | 3 | 3 |
| 5 | 22 | 3 | 3 |
| 6 | 36 | 3 | 3 |
| 7 | 57 | 4 | 6 |
| 8 | 91 | 4 | 6 |
| 9 | 140 | 4 | 6 |
| 10 | 216 | 4 | 6 |
| 11 | 317 | 4 | 6 |
| 12 | 463 | 5 | 9 |
| 13 | 668 | 5 | 9 |
| 14 | 962 | 5 | 9 |
| 15 | 1359 | 5 | 9 |
| 16 | 1919 | 5 | 9 |
| 17 | 2666 | 5 | 9 |
| 18 | 3694 | 6 | 13 |
| 19 | 5035 | 6 | 13 |
| 20 | 6845 | 6 | 13 |
| 21 | 9188 | 6 | 13 |
| 22 | 12366 | 6 | 13 |
| 23 | 16417 | 6 | 13 |
| 24 | 21787 | 6 | 13 |

Examples attaining the changes in the last column are:
{1,2}, {1,2,4}, {1,2,5,7}, {1,3,8,9,12}, and {1,2,5,11,13,18}.
The last two have initial saturated intervals through 9 and 13 respectively. These are finite checks, not evidence claimed as an asymptotic obstruction.

The two six-point sets in Section 1.5 were independently checked by listing and sorting all fifteen positive differences and computing the windows at T=5. The results were exactly the values recorded there.

## 4.2 Explicit endpoint family

For p=61,101,257,1009, trial division verified primality. I built the sets in Section 2 and checked every positive difference for positivity and uniqueness, and counted the points in both prescribed windows. N, L, endpoints, and differences used BigInt. L was computed as floor(root_4(N^3))/10 with integer division, using an exact binary-search fourth root; this equals floor(N^(3/4)/10).

| p | m per endpoint | N | L | B0 | Checked positive differences |
|---:|---:|---:|---:|---:|---:|
| 61 | 30 | 3573458 | 8218 | 7202 | 1770 |
| 101 | 50 | 27572977 | 38050 | 20002 | 4950 |
| 257 | 128 | 1184250334 | 638384 | 131074 | 32640 |
| 1009 | 504 | 284659565968 | 38971250 | 2032130 | 507528 |

Every check passed. The smallest positive differences were respectively 69,111,273,1041, confirming in these examples that short-difference saturation is absent.

## 4.3 Large exact aggregate checks of the moment relaxation

Using BigInt aggregate formulas, without allocating W entries, I checked Proposition 1.4 at s=65536 and s=100000, each for

    m=s^2,  m=s^2+floor(94s/100),  m=s^2+s.

The checked m values were respectively

    4294967296, 4295028899, 4295032832;
    10000000000, 10000094000, 10000100000.

For each, I checked
sum r(r-1)<=T(T-1),
(64H)^2<=T^5,
and 2s k(W-k)<=WTm.
These imply the tested upper bound H<=T^(5/2)/64<=U_T and (12). All six checks passed.

## 4.4 Cost and delivery

Measured CPU usage inside the three mathematical Node runs was:

* Enumeration through N=24 and first moment checks: 0.028292 CPU seconds.
* Four endpoint constructions and all their differences: 0.253654 CPU seconds.
* Final integer-only moment checks, the six-point example, and aggregate checks: 0.027712 CPU seconds.

Total measured mathematical-process CPU: 0.309658 seconds. This excludes interpreter startup and control-plane/file I/O overhead; no long-running compute process was used. All calculations were synchronous on one computational thread, well within the one CPU-hour cap. No monetary-cost measurement was available.

The only file written under /work is this report. No follow-up research has been scheduled. The completed deliverable is a partial-result/obstruction report; the requested improvement of the Sidon bound remains open.

