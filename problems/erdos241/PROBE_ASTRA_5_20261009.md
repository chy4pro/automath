PARTIAL — proved exact hole/representation identities, a shared-endpoint matching constraint, and |A|^3 <= 4N + 32N^(5/6) for every B_3 set A in {1,...,N}. The requested strict improvement below 1.5154 remains OPEN.

# Clean-room probe of Erdős #241

This report is in English as required for internal research notes. It uses the supplied brief and elementary mathematics only. The designated report did not exist at the start of this recovery run. No other file under `/work`, repository source, paper, web result, or other agent's file was read. Paperclip operational skill files were read only for task administration.

The bound proved here has limiting constant 4^(1/3), which is weaker than 1.5154. No improvement on the bound supplied in the brief is claimed. Both requested seeds were investigated: holes in A+A-A, and moments/shared endpoints of representation counts.

## 1. Definitions and a precise summary of the missing estimate

Let N be a positive integer, and let A be a B_3 subset of {1,...,N}. Thus equality between sums of two three-element multisets from A implies equality of those multisets. Write m=|A|. Empty sets will be handled separately whenever division by m occurs.

All representation functions below count ordered tuples, with repetitions allowed:

\[
\begin{aligned}
 f(x)&=\mathbf 1_A(x),\\
 p(x)&=\#\{(a,b)\in A^2:a+b=x\},\\
 r(x)&=\#\{(a,b,c)\in A^3:a+b-c=x\},\\
 d(h)&=\#\{(a,b)\in A^2:a-b=h\},\\
 C(h)&=\#\{(a,b,c,e)\in A^4:a+b-c-e=h\}.
\end{aligned}
\]

Define the finite sets

\[
 S=A+A-A,\qquad T=\{2a-b:a,b\in A,\ a\ne b\},\qquad D=A-A.
\]

For any integer h define

\[
 H(h)=\#\{a\in A:a+h\notin S\},\qquad
 B(h)=\#\{a\in A:a+h\in T\}.
\]

For a positive integer L put

\[
 w_L(h)=\max(0,L-|h|),\qquad
 W_L=\sum_h w_L(h)H(h),\quad
 V_L=\sum_h w_L(h)d(h),\quad
 U_L=\sum_h w_L(h)B(h).
\]

The sums are finite. Since the sum of the weights is L^2, the quantity

\[
 \theta_L(A)=\frac{W_L}{mL^2}\quad (m>0)
\]

belongs to [0,1]. It is a weighted fraction of holes sampled at translates of the actual elements of A, rather than a fraction over the whole ambient interval.

The main exact coupling proved below is

\[
 C(h)=2m-2H(h)+(2m-3)d(h)-B(h).                 \tag{1}
\]

For m>=2 and L=ceil(N^(5/6)), it yields the effective estimate

\[
 \frac{m^3}{N}\le 4(1-\theta_L(A))+32N^{-1/6}. \tag{2}
\]

The unproved assertion that would suffice for the target is the following:

> There is an explicit N_* such that every B_3 set A in {1,...,N}, with N>=N_* and m>=(3/2)N^(1/3), satisfies theta_{ceil(N^(5/6))}(A)>=13/100.

This assertion is NOT established in this report. Section 6 explains exactly how it would imply a constant below 1.5154, including a finite onset. Global holes, the exact one-point moments, and the first-moment shared-endpoint constraint derived here do not establish it.

## 2. Exact representation counts

### 2.1. Cancellation and uniqueness

If m>0, B_3 implies B_2: append any fixed element of A to an equality of two pair sums, apply B_3, and cancel the appended element as a multiset. Consequently d(0)=m and d(h) is either 0 or 1 for h!=0. Indeed, if a-b=c-e!=0, then a+e=c+b. The B_2 alternatives are the identical ordered difference or a=b and c=e; the latter is incompatible with a nonzero difference.

Consider a representation a+b-c=x, with the positive pair regarded as unordered. Call it noncancelling if c is neither a nor b. Two such representations of the same value satisfy

\[
 a+b+c'=a'+b'+c.
\]

B_3 identifies the corresponding three-element multisets. The element c on the right cannot equal a or b, so it must equal c'. Cancelling it identifies the two positive pairs. Thus every noncancelling representation is unique in this convention.

If x is in A, then a+b=c+x and B_2 forces {a,b}={c,x}; hence a representation of x necessarily cancels. Conversely, for a fixed x in A, each c different from x gives two ordered representations, and c=x gives one. Therefore r(x)=2m-1 on A.

Outside A, all representations are noncancelling. A representation with a!=b contributes exactly two ordered tuples; a representation with a=b contributes exactly one. In particular T is disjoint from A, its elements are all distinct as (a,b) with a!=b varies, and

\[
 |T|=m(m-1).
\]

For a positive pair of distinct elements there are m-2 allowed negative elements. There are binom(m,2) such pairs. For a doubled positive element there are m-1 allowed negative elements. These cases, together with A itself, give

\[
 |S|=m+\binom m2(m-2)+m(m-1)
     =m+\frac{m^2(m-1)}2.                     \tag{3}
\]

The counting argument also covers m=0,1,2; the term binom(m,2)(m-2) is zero when m<3.

Pointwise on the whole integer line,

\[
 r(x)=2\mathbf 1_S(x)+(2m-3)\mathbf 1_A(x)-\mathbf 1_T(x). \tag{4}
\]

To check (4), the four disjoint cases are x in A, x in T, x in S\(A union T), and x outside S. Their values are respectively 2m-1, 1, 2, and 0. For m=0 the identity is also zero on both sides.

### 2.2. Every one-point moment is explicit

For every integer k>=1,

\[
 \sum_x r(x)^k
 =m(2m-1)^k
  +2^k\frac{m(m-1)(m-2)}2+m(m-1).            \tag{5}
\]

This is simply the sum of the powers of the four values just enumerated, so there is no omitted diagonal correction. For example,

\[
 \sum_x r(x)^2=6m^3-9m^2+4m.                 \tag{6}
\]

Thus varying k produces no new scalar parameter of A. The moments could still be useful in a position-sensitive inequality, but an argument seeking an extra strict defect in one of these unshifted moments has no such defect to exploit.

## 3. Shared endpoints and the exact hole coupling

Summing (4) over x=a+h with a in A gives (1), because

\[
 C(h)=\sum_{a\in A}r(a+h),\qquad
 \sum_{a\in A}\mathbf 1_S(a+h)=m-H(h).
\]

This proves the coupling without an inequality or an asymptotic error.

At h=0, B_2 directly gives

\[
 C(0)=2m^2-m.                                \tag{7}
\]

For h in D, H(h)=0: if h=u-v with u,v in A, then a+h=a+u-v is in S for every a in A.

If h=u-v!=0, the ordered pair (u,v) is unique. A quadruple counted by C(h) satisfies

\[
 a+b+v=c+e+u.
\]

Multiset uniqueness implies that {a,b}={u,z} and {c,e}={v,z} for one z in A. Each z outside {u,v} contributes four ordered quadruples; z=u and z=v each contribute two. Hence

\[
 C(h)=4m-4\quad(h\in D\setminus\{0\}).     \tag{8}
\]

Substitution in (1), using d(h)=1 and H(h)=0, gives B(h)=1 on D\{0}. If h is outside D, then d(h)=0 and

\[
 C(h)=2m-2H(h)-B(h)\le2m.                    \tag{9}
\]

There is also a matching interpretation, which is a genuine shared-endpoint restriction. Fix h outside D and consider ordered pairs (P,Q) of unordered two-element multisets from A satisfying sum(P)-sum(Q)=h. Then P and Q have disjoint supports: cancelling a shared element would put h in D.

Two distinct representations cannot share an element on their positive sides. If P={a,b}, P'={a,b'}, then the equality of differences gives

\[
 \{b\}\uplus Q'=\{b'\}\uplus Q
\]

by B_3. Since b is not in Q, it must equal b'; cancellation then gives Q'=Q and P'=P. The same argument applies to the negative sides. Thus the positive pairs form a matching on their supports, as do the negative pairs; doubled elements are allowed as singleton supports. This argument does not restrict a positive endpoint in one representation from being a negative endpoint in a different representation.

## 4. Smoothing: a fully effective bound

Let q_L(n)=sum_{j=0}^{L-1}p(n-j). All its values are nonnegative and

\[
 \sum_n q_L(n)=Lm^2.
\]

Its support lies in the integer interval [2,2N+L-1], which has 2N+L-2 elements. Cauchy-Schwarz, applied after filling any unused positions with zeros, gives

\[
 \sum_n q_L(n)^2\ge\frac{m^4L^2}{2N+L-2}.  \tag{10}
\]

Expanding the square, the number of pairs of indices j,k in {0,...,L-1} with a specified difference h is w_L(h). Also sum_n p(n)p(n+h)=C(h), since C is symmetric. Therefore

\[
 \sum_n q_L(n)^2=\sum_h w_L(h)C(h)
 =2mL^2-2W_L+(2m-3)V_L-U_L.                 \tag{11}
\]

For completeness, sum_h w_L(h)=L+2 sum_{h=1}^{L-1}(L-h)=L^2. Moreover

\[
 0\le V_L\le L\sum_h d(h)=Lm^2,\qquad U_L\ge0, \tag{12}
\]

because 0<=w_L(h)<=L and sum_h d(h)=m^2. If m>=2, then 2m-3>=0, so (10)--(12), divided by mL^2, give

\[
 \frac{m^3}{2N+L-2}
 \le 2-\frac{2W_L}{mL^2}+\frac{(2m-3)m}{L}
 \le 2(1-\theta_L(A))+\frac{2m^2}{L}.        \tag{13}
\]

We next justify a uniform elementary preliminary bound needed to choose L. Since S is contained in [2-N,2N-1], (3) implies

\[
 m^3-m^2+2m\le6N-4.                         \tag{14}
\]

If m>=3, then m^3-m^2>=(2/3)m^3, whence m^3<=9N. Consequently m^2<=9^(2/3)N^(2/3)<5N^(2/3), where the last inequality follows from 81<125. If m<=2, then m^2<=4<=5N^(2/3). In all cases,

\[
 m^2\le5N^{2/3}.                            \tag{15}
\]

Set L=ceil(N^(5/6)). Then N^(5/6)<=L<=N^(5/6)+1, and hence

\[
 2N+L-2\le2N+N^{5/6},\qquad
 \frac{2m^2}{L}\le10N^{-1/6}.                \tag{16}
\]

Both factors in the right-hand side of (13) are nonnegative. Multiplying the upper bounds (16) and expanding gives, for m>=2,

\[
\begin{aligned}
 m^3
 &\le (2N+N^{5/6})\bigl(2(1-\theta_L)+10N^{-1/6}\bigr)\\
 &=4(1-\theta_L)N
   +\bigl(2(1-\theta_L)+20\bigr)N^{5/6}
   +10N^{2/3}\\
 &\le4(1-\theta_L)N+32N^{5/6}.               \tag{17}
\end{aligned}
\]

The last step uses 0<=theta_L<=1 and N^(2/3)<=N^(5/6) for N>=1. This proves (2). Dropping theta_L proves

\[
 \boxed{\ m^3\le4N+32N^{5/6}\ }              \tag{18}
\]

for m>=2, and the same assertion is immediate for m=0,1. Every step is valid for every integer N>=1; no large-N exception is hidden.

Equivalently,

\[
 \frac{R_3(N)}{N^{1/3}}\le(4+32N^{-1/6})^{1/3}.
\]

This gives limsup R_3(N)/N^(1/3)<=4^(1/3), with the displayed finite error, and does not reach the target.

## 5. What the hole route proves, and what endpoint balance adds

### 5.1. Global holes

Define the global hole count within the full possible support interval by

\[
 G_N=\#\bigl([2-N,2N-1]\cap\mathbb Z\setminus S\bigr).
\]

Equation (3) gives the exact formula

\[
 G_N=3N-2-m-\frac{m^2(m-1)}2.                \tag{19}
\]

By (18), and by m^2/2-m=((m-1)^2-1)/2>=-1/2,

\[
 G_N\ge N-16N^{5/6}-\frac52
      \ge N-16N^{5/6}-3.                     \tag{20}
\]

Together with nonnegativity this gives, for every N>=1,

\[
 \frac{G_N}{3N-2}
 \ge\frac{\max(0,N-16N^{5/6}-3)}{3N-2}.     \tag{21}
\]

In particular, the liminf of this global fraction along any sequence of such sets with N tending to infinity is at least 1/3. This applies also under the requested density hypothesis m>=(3/2)N^(1/3). Formula (21), rather than an unspecified error term, is the finite version.

The local weight in (2) is substantially different. Since L=ceil(N^(5/6))<=N, all points a+h with |h|<L are inside [2-N,2N-1]. Thus W_L counts genuine ambient holes, but preferentially those near A. A global count does not say that enough holes receive this weight.

One exact obstruction to a cardinality-only inference is visible in the relaxed problem where S is an arbitrary set. For any integers N,L with 2L<N, take A contained in [L+1,N-L] and take an artificial set S_tilde containing [1,N], enlarged to any prescribed cardinality between N and 3N-2 inside [2-N,2N-1]. Then every a+h with a in A and |h|<L lies in S_tilde, so its weighted hole fraction is zero, despite all the holes outside S_tilde. This is not claimed to realize S=A+A-A or a dense B_3 set. It identifies exactly why the scalar information |S| and global holes cannot by itself supply the required conclusion; additional realizability information must be used.

### 5.2. A first-moment constraint from shared endpoints

For every integer h there is a further exact identity

\[
 \sum_{a\in A}a\bigl(r(a-h)-r(a+h)\bigr)
 =\frac{hC(h)}2.                            \tag{22}
\]

To verify it, consider all ordered quadruples (u,v,s,t) with u+v-s-t=h. The sum of their first positive coordinates is sum_a a r(a-h); the sum of their first negative coordinates is sum_a a r(a+h). Interchanging the two positive coordinates, and separately the two negative coordinates, shows that twice their difference equals the sum of u+v-s-t over all quadruples, namely hC(h). This proves (22), including repeated-coordinate cases.

Suppose N>1 and h is outside D. Then r(a+h) and r(a-h) both lie in {0,1,2}. Define e_+(a)=2-r(a+h) and e_-(a)=2-r(a-h). These are nonnegative, and, since C(h)=C(-h), their total masses are both

\[
 \Delta_h=2m-C(h)=2H(h)+B(h).                \tag{23}
\]

For h>0, equations (22)--(23) and 1<=a<=N give

\[
 \frac{hC(h)}2
 =\sum_a a(e_+(a)-e_-(a))
 \le N\Delta_h-\Delta_h=(N-1)\Delta_h.
\]

For h<0 apply the same reasoning to -h. Rearrangement gives

\[
 C(h)\le\frac{4m(N-1)}{2(N-1)+|h|},\qquad
 2H(h)+B(h)\ge\frac{2m|h|}{2(N-1)+|h|}
 \quad(h\notin D).                          \tag{24}
\]

The denominator is positive under N>1. The N=1 case consists only of sets of size at most one and is irrelevant to the density regime; (18)--(21) already cover it.

For L>=1 one also has the exact total and its immediate weighted upper bound

\[
 \sum_h B(h)=m|T|=m^2(m-1),\qquad
 U_L\le Lm^2(m-1).                          \tag{25}
\]

Indeed, each ordered choice a in A, t in T contributes exactly once, at h=t-a.

Equations (24)--(25) show why this particular endpoint balance does not close the gap. Even if the B term and the exceptional shifts in D were discarded in the most favorable way, the proposed lower bound on H(h)/m from (24), for |h|<L, is at most

\[
 \frac{L-1}{2(N-1)}\quad(N>1).              \tag{26}
\]

For L=ceil(N^(5/6)), this is at most N^(5/6)/(2(N-1)), which tends to zero. Thus this lower-bound calculation cannot certify a fixed positive hole fraction. This is a limitation of (24), not an assertion that the actual holes tend to zero.

The size of the diagonal correction in this scale is also explicit: by (15) and (25),

\[
 0\le\frac{U_L}{mL^2}\le\frac{m(m-1)}L
 \le5N^{-1/6}.                              \tag{27}
\]

The needed gain is therefore a fixed positive weighted hole fraction, not a gain obtainable merely by retaining this vanishing diagonal correction.

## 6. Exact threshold for a conditional improvement

Direct integer arithmetic gives

\[
 (1.5154)^3=\frac{3480020872264}{10^{12}}
           =3.480020872264.
\]

Consequently the threshold suggested by (2) is

\[
 \theta_*:=1-\frac{(1.5154)^3}{4}
 =\frac{64997390967}{500000000000}
 =0.129994781934.                            \tag{28}
\]

A proved uniform lower bound theta_L>=theta_0>theta_* on all sufficiently large sets in the density regime would give a strict improvement via (2). Equality theta_0=theta_* would not itself give a strict improvement.

Here is a fully explicit conditional version using theta_0=13/100. If the unproved assertion in Section 1 holds with onset N_*, then (17) gives, in that regime,

\[
 \frac{m^3}{N}\le\frac{87}{25}+32N^{-1/6}.
\]

For every integer

\[
 N\ge\max\{N_*,(3200000)^6\},               \tag{29}
\]

the last error is at most 1/100000. Therefore

\[
 m\le\left(\frac{348001}{100000}\right)^{1/3}N^{1/3}.
\]

The same bound holds for sets below the density regime, since (3/2)^3=27/8<348001/100000. The cube of this conditional constant is 3.48001<3.480020872264, so it is strictly below 1.5154. The integer in (29) is exactly

\[
 (3200000)^6=1073741824000000000000000000000000000000.
\]

This is a reduction to a concrete missing estimate, NOT a proof of that estimate or of the target. No value of N_* has been obtained.

## 7. Routes attempted and their precise obstructions

1. **Direct packing of A+A-A.** Noncancelling uniqueness proves (3). Packing it in an interval of length 3N-2 gives only (14), whose cubic leading coefficient is 6. The obstruction is that this counts all available positions with equal weight and makes no use of where the representations lie.

2. **Higher one-point moments of r.** All of them are exactly (5). For example, ordinary Cauchy-Schwarz on r and its support gives
   \[
   m^6\le(3N-2)(6m^3-9m^2+4m),
   \]
   since sum_x r(x)=m^3 and the support has at most 3N-2 positions. This is much weaker than needed. The obstruction to an extra-moment-defect argument is the rigid value distribution, not an unestimated lower-order term.

3. **Shared endpoints, pointwise four-variable caps, and smoothing.** Equations (7)--(13) retain the exceptional shifts exactly. Discarding W_L and U_L yields (18), with limiting cubic coefficient 4. The precise missing improvement in this route is the uniform weighted hole bound quantified in (28), rather than a sharper treatment of the exceptional d(h) term, whose upper contribution in (13) is at most 10N^(-1/6) at the chosen scale.

4. **Transfer from global holes to holes near A.** Equations (19)--(21) prove a substantial global hole fraction, including for m>=(3/2)N^(1/3). No lower bound of 0.13 on theta_L follows. The artificial-set example in Section 5.1 shows why the cardinality relaxation permits theta_L=0; proving that B_3 realizability excludes this behavior is the unresolved part.

5. **First moments of the shared-endpoint matching.** The exact balance identity (22) yields (24), but at |h|<ceil(N^(5/6)) the lower-bound mechanism has size bounded by (26), which tends to zero. It does not produce the required fixed positive deficit. Enlarging the smoothing scale to a fixed fraction of N also enlarges the support denominator 2N+L-2 in (13); no improvement below 4 was derived this way.

6. **An unsmoothed higher mixed energy.** Let E_4=sum_h C(h)^2, equivalently the number of equalities of two ordered four-term sums. Its support has at most 4N-3 positions and sum_h C(h)=m^4, so
   \[
   E_4\ge\frac{m^8}{4N-3}.
   \]
   Outside D, C(h)^2<=2mC(h) by (9). On D use (7)--(8), and |D\{0}|=m(m-1). Adding these inequalities gives
   \[
   \begin{aligned}
   E_4&\le 2m^5+(2m^2-m)(2m^2-3m)\\
      &\qquad+m(m-1)(4m-4)(2m-4)\\
      &=2m^5+12m^4-40m^3+43m^2-16m.
   \end{aligned}
   \]
   For m>0 the resulting exact consequence is
   \[
   \frac{m^3}{4N-3}
    \le2+\frac{12}{m}-\frac{40}{m^2}
           +\frac{43}{m^3}-\frac{16}{m^4}.
   \]
   Along m tending to infinity this has cubic leading coefficient 8 relative to N, weaker even than (18). The obstruction is the crude upper bound on mixed shifts outside D. B_3 does not identify two arbitrary four-term multisets, so treating E_4 as a diagonal-only energy would be invalid.

These are all the mathematical routes attempted in this recovery. No density variational problem was solved, no numerical optimizer was used, and no positive uniform hole bound was assumed in an unconditional conclusion.

## 8. Exact finite checks

The checks are diagnostics, not substitutes for the proofs. All subset enumeration used integer arithmetic, with no SAT/ILP solver, floating-point optimization, or sampling of subsets.

### 8.1. Exhaustive subsets of {1,...,20}

A single Node.js v22.23.1 process enumerated all 2^20=1,048,576 subsets. A subset was accepted exactly when its unordered triple sums, generated by indices i<=j<=k, were all distinct. There were 2,089 accepted sets, including the empty set, distributed by size as follows:

| Size m | Number of B_3 subsets of {1,...,20} |
|---:|---:|
| 0 | 1 |
| 1 | 20 |
| 2 | 190 |
| 3 | 936 |
| 4 | 942 |

The first encountered set of size four was {1,2,8,12}. No set of size five or larger was accepted. This is only a statement about this exhaustive range.

The cumulative counts for ambient N=1,...,20 were respectively

```text
2, 4, 7, 11, 18, 30, 45, 67, 96, 132,
177, 237, 314, 420, 559, 737, 968, 1270, 1631, 2089.
```

Each accepted nonempty set was checked using N=max(A); for the empty set the checks used N=1. Direct loops independently formed r, d, p, T and C (the latter from the pair-sum correlations). The following checks all passed:

- Exact cardinalities (3) and |T|=m(m-1), and pointwise formula (4) throughout [2-N,2N-1].
- 12,534 moment comparisons: (5) for k=1,...,6 on every accepted set.
- 150,665 shift comparisons: (1), and (7)--(9) where applicable, for every integer h from -2N-2 through 2N+2.
- 150,665 independent first-moment checks of (22); also the cross-multiplied bound (24) wherever N>1 and h is outside D.
- 51,176 pair-of-pair representations checked while asserting that distinct positive pairs, and distinct negative pairs, never reused an endpoint at a shift outside D.
- 10,430 smoothing comparisons for the distinct values in {1,2,ceil(N/2),N,2N+1}: direct construction of q_L, equality (11), and Cauchy-Schwarz (10). The bound using V_L<=Lm^2 was checked whenever m>=2.

All values used for the integer equality and Cauchy-Schwarz checks in this exhaustive range are below 2^53. An initial auxiliary check of the bound from (13) used Number arithmetic with division by m; division by three need not be exact. That auxiliary comparison was therefore rerun in a fully multiplied, BigInt form as recorded in Section 8.4. No claim of exactness relies on the initial division.

Failures: zero. Measured process CPU for the enumeration and its checks: 0.615040 user seconds + 0.008127 system seconds = 0.623167 seconds. Measured script wall time: 0.591426515 seconds.

### 8.2. Larger cardinalities and repeated-coordinate cases

To test beyond m=4, a second process checked 36 explicitly described sets. For each m=1,...,12, let P_m={4^j:0<=j<m}, Q_m=5P_m+3, and n_m=max(Q_m)+7. The three sets checked were

\[
 P_m,\qquad Q_m,\qquad \{n_m+1-a:a\in Q_m\}.
\]

Base-four digit uniqueness with digits at most three proves that P_m is B_3; translation, dilation by a nonzero integer, and reflection preserve B_3. Unordered triple-sum uniqueness was also checked directly. The largest ambient endpoint used was 20,971,523.

These sets passed 360 exact moment comparisons for k=1,...,10 (using BigInt), 39,576 shift comparisons of (1), (7)--(9), (22), and (24), and 177 smoothing identity/Cauchy-Schwarz comparisons. The shift set was supp(C) together with -2N-1 and 2N+1. The distinct smoothing lengths were {1,2,ceil(N^(5/6)),N,2N+1}. All energy and weighted-mass arithmetic in these smoothing comparisons used BigInt.

For large L, the weighted hole count was computed exactly as

\[
 W_L=mL^2-\sum_{a\in A}\sum_{s\in S}w_L(s-a),
\]

and the energy as sum_h w_L(h)C(h); no array with N or L entries was needed. The value ceil(N^(5/6)) was selected numerically for these auxiliary checks, but each selected positive integer L was checked with exact integer arithmetic. The proof of (17) uses the mathematical ceiling and is independent of that selection.

Failures: zero. Measured process CPU for this check: 0.312243 user seconds + 0.009072 system seconds = 0.321315 seconds. Measured script wall time: 0.181587190 seconds.

### 8.3. Arithmetic check of the target threshold

Separate BigInt arithmetic verified the cube numerator 3,480,020,872,264 with denominator 10^12, the reduced fraction in (28), the positive cube gap 20,872,264/10^12 above 3.48, and the integer (3200000)^6 displayed in (29). These calculations concern the conditional reduction only.

### 8.4. Focused integer audit of two derived inequalities

A further enumeration of the same 2^20 subsets selected the 2,088 nonempty B_3 sets. For every one, BigInt arithmetic checked both bounds for E_4 in route 6 against the directly computed sum_h C(h)^2. This gave 2,088 successful energy comparisons. For each set with m>=2 and each of the same distinct lengths {1,2,ceil(N/2),N,2N+1}, it also checked

\[
 m^4L^2\le(2N+L-2)\bigl(2mL^2-2W_L+(2m-3)m^2L\bigr).
\]

This is the first inequality in (13) with all denominators cleared. All 10,333 of these BigInt comparisons passed. Thus the auxiliary floating-point division mentioned in Section 8.1 is unnecessary to the checked result. Measured process CPU: 0.381361 user seconds + 0.001001 system seconds = 0.382362 seconds. Measured script wall time: 0.369749307 seconds.

## 9. Proof audit, cost, and next mathematical action

The proof was re-derived from the written identities in the following dependency order: B_3 cancellation -> (3)--(5) -> (1), (7)--(9) -> exact smoothing (11) -> (13)--(17). The signs of the hole and diagonal corrections, the exceptional h=0 and h in D\{0} cases, the integer support length 2N+L-2, and the ceiling error in L were checked separately. The first-moment identity (22) was re-derived by summing the two positive and the two negative coordinates of each quadruple. The report makes no HIT claim.

Every asymptotic conclusion above has a displayed finite inequality behind it. There are no unspecified o(1) or O(1) terms in any claimed theorem. In particular, N>=1 is the onset of (18), and (29) is the exact onset of the explicitly conditional conclusion, conditional also on the as-yet-unproved N_*.

Compute used no worker jobs or parallel mathematical processes; Node was invoked with UV_THREADPOOL_SIZE=1 and --v8-pool-size=1. The three substantive checking sections used 1.326844 measured process CPU seconds in total. Including the two tiny arithmetic invocations and interpreter startup, mathematical compute was below 5 CPU seconds, well below one CPU-hour. No SAT/ILP solver, network mathematical lookup, paid compute, or sub-agent was used. Operational Paperclip I/O is separate from mathematical compute. The supplied record does not contain a reliable compute total for earlier interrupted runs, so no aggregate cost for those runs is asserted.

Exactly one deliverable file was created under /work: this report. The remaining mathematical action is to prove, or replace with another quantitatively sufficient realizability constraint, the uniform weighted-hole assertion in Section 1. The present probe is complete as a PARTIAL result; the target remains open.
