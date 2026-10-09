PARTIAL — proved the conditional lift-repair bound s(HM) ≤ k + H − 1 + u, exact cubic-curve coverage counts, and an explicit second-moment obstruction for independent thinning of perfect difference sets. No bound s(N) ≪ N^(1/3)(log N)^θ with θ < 1/3 is proved.

# Scope and notation

This is a clean-room probe of the two routes in the brief. All mathematical arguments below were derived in this run from the brief and standard finite-field and probability facts; the needed probability inequalities are proved below. No repository material, other agents' files, web pages, or papers were read. The designated output did not exist at the start. Operational Paperclip skill instructions were read outside /work.

Write [N] = {1,...,N}. A Sidon set has distinct sums indexed by unordered pairs, including pairs with repetition. The same definition is used in an abelian group. Translation between {0,...,N−1} and [N] preserves the property and maximality. All logarithms are natural. There are no unspecified o(1) or O(1) terms in the proved statements.

The brief's improved upper-bound target remains OPEN. The results here concern reductions, exact examples, and limitations of particular sampling schemes, not a limitation of all possible constructions.

# 1. Exact blocking criterion and a baseline lower bound

For an integer Sidon set A, put

T(A) = {a+b−c : a,b,c in A},

Q(A) = {(a+b)/2 : a,b in A and a+b is even},

B(A) = A union T(A) union Q(A).

For x not in A, the set A union {x} fails to be Sidon if and only if x belongs to T(A) union Q(A).

Proof. An old-old collision is impossible. A new sum x+a can collide with an old sum b+c precisely when x=b+c−a. The new sum 2x can collide with an old sum b+c precisely when x=(b+c)/2. Distinct sums x+a and x+b cannot coincide, and x+a=2x would imply a=x, excluded here. This exhausts the possibilities. The argument also works in any abelian group when Q is interpreted as the solutions of 2x=a+b. In an odd-order group, division by 2 is unique.

Consequently A is maximal in [N] exactly when [N] is contained in B(A). If |A|=m, then

|B(A)| ≤ m + m²(m−1)/2 + m(m−1)/2 = (m³+m)/2.                 (1)

Indeed, a triple a+b−c with c equal to a or b already gives an element of A. For each of the m choices of c, the number of unordered pairs with repetition from A minus {c} is m(m−1)/2. This bounds all other triple values by m²(m−1)/2. Nontrivial midpoint values are indexed by at most m(m−1)/2 distinct-element pairs. Overlaps only decrease the union's size. Thus every maximal set satisfies the explicit inequality

2N ≤ m³+m.                                                     (2)

This is a lower bound, not progress on the requested upper bound.

For any initial Sidon set, greedy addition yields a maximal extension. All its added elements were initially unblocked: a collision present in A remains present in every superset of A. The general bound is therefore |A| plus the number of initially unblocked points. Section 2 gives a substantially smaller repair certificate for one special class of gaps.

# 2. Route (a): modular sets, lifting, and a cheap fibre repair

## 2.1 A single representative does not block other copies of its residue

Let M≥2, let D be a Sidon subset of Z/MZ, and select exactly one integer a_d congruent to each d in D. Then A={a_d:d in D} is an integer Sidon set: an integer sum equality reduces to a modular sum equality, which identifies the unordered residue pair and hence the two selected integers.

If x≠a_d is another integer congruent to d in D, it can be added to A. To prove this using Section 1, a putative equality x+a_e=a_f+a_g would imply {d,e}={f,g} modulo M. As representatives are unique, the integer equation would reduce to x+a_e=a_d+a_e and force x=a_d. Likewise 2x=a_f+a_g forces f=g=d and then x=a_d. Thus neither blocking mechanism is available.

In particular, if the ambient interval is I={0,...,HM−1}, representatives are chosen from I, and |D|=k, then k(H−1) points in the occupied residue classes are initially unblocked. This obstructs immediate maximality, but does NOT force k(H−1) additions.

## 2.2 Exact criterion for several levels in a modular Sidon support

Choose representatives d in {0,...,M−1}. For each d in D let S_d be a set of integers and form

C = union over d in D of {d+Ms : s in S_d}.

Then C is Sidon if and only if all the positive differences s−t, with s>t in a common S_d, are distinct, counting occurrences across every d.

Proof. Reducing any pair-sum collision modulo M identifies its unordered pair of residue classes. Within a single residue class, pair-sum uniqueness is exactly the Sidon property of S_d. For integers this is equivalent to uniqueness of its positive differences: a repeated positive difference s−t=u−v gives s+v=u+t, and a nontrivial pair-sum collision gives a repeated positive difference after ordering the terms. Between two different residue classes d,e, a nontrivial collision is exactly

s_1+t_1=s_2+t_2,  with s_i in S_d and t_i in S_e,

so s_1−s_2=t_2−t_1 is a nonzero difference shared by the two level sets. Conversely, a common positive difference supplies that collision. These are all possible residue pairs.

If every S_d is contained in {0,...,H−1}, this gives

sum over d of binom(|S_d|,2) ≤ H−1.                            (3)

All counted differences are distinct members of {1,...,H−1}. If every S_d is nonempty and t points have been added beyond one per class, write |S_d|=1+t_d. Since binom(1+t_d,2)≥t_d and sum t_d=t, (3) implies

t ≤ H−1.                                                       (4)

Thus greedy extension using only these residue classes always stops after at most H−1 additions and blocks every remaining point in those classes.

## 2.3 Conditional lift-repair theorem

Let D⊆Z/MZ be modular Sidon of size k, let H≥1 be an integer, and choose one a_d in I={0,...,HM−1} for every d in D. Let u be the number of initially unblocked integers of I whose residues are outside D. Then

s(HM) ≤ k + H − 1 + u.                                         (5)

Proof. First greedily add only points with residue in D. The process adds at most H−1 points by (4), and ends with all such points blocked. Next greedily add arbitrary available points until maximality. Every later addition has residue outside D and was initially unblocked, so there are at most u later additions. Translation by 1 gives the asserted interval theorem.

For example, if H≤c k and u≤C k for specified constants c,C≥0, (5) gives s(HM)≤(1+c+C)k−1. Obtaining such an outside-residue coverage estimate at H proportional to k is the missing step. No such estimate is proved here. Moreover, a construction only on selected lengths HM would still require an argument covering every sufficiently large N; none is silently inferred by truncation.

Repeating an entire modular set in two common layers is not a repair: for distinct d,e,

(d+0M)+(e+M) = (d+M)+(e+0M)

is a nontrivial collision. Condition (3) describes precisely the constraint that this naive repetition violates.

## 2.4 The algebraic perfect-difference family used below

Here is a self-contained construction of the modular family underlying the random probe. For a prime power q, let F be the field with q³ elements, and choose a generator g of its cyclic multiplicative group. The quotient F* / F_q* is cyclic of order

M=q²+q+1.

The nonzero trace-zero elements, modulo scalar multiplication by F_q*, give a subset D of this quotient of size

k=(q²−1)/(q−1)=q+1.

The trace map Tr(z)=z+z^q+z^(q²) is F_q-linear and nonzero: its defining nonzero polynomial has degree q²<q³ and so cannot vanish at every element of F. Its kernel therefore has dimension 2.

For a nontrivial quotient element represented by α not in F_q, the forms Tr(z) and Tr(αz) are independent. Otherwise Tr((α−c)z)=0 for all z for some c in F_q. Multiplication by the nonzero α−c is bijective on F, which would make Tr identically zero. Their common kernel has dimension 1. It contains exactly one nonzero projective point. Thus every nonzero quotient element has exactly one representation d_1−d_2 with d_1,d_2 in D.

Identify this quotient with Z/MZ. We have proved

M=k²−k+1, and every nonzero difference occurs exactly once.     (6)

Such a D is Sidon: a nontrivial equality a+b=c+d would give two representations of the nonzero difference a−c=d−b; difference uniqueness makes the unordered pairs identical. The finite-field existence and cyclicity facts used in this construction are standard algebra, not a cited construction from a paper.

# 3. A direct algebraic three-coordinate attempt: exact failure of the cubic curve

Let p≥5 be prime and work in the additive group F_p³. Consider

C_p = {(t,t²,t³):t in F_p}.

It is Sidon. The first two coordinates of the sum of parameters a,b determine a+b and a²+b², hence ab=((a+b)²−(a²+b²))/2. These determine the unordered roots a,b of their quadratic polynomial.

Write T_p=C_p+C_p−C_p. The exact count is

|T_p| = (p³−p²+2p)/2.                                          (7)

Here is the complete calculation. For a candidate (u,v,w), put δ=v−u². If parameters a,b,c represent it as a+b−c coordinatewise, set S=a+b and P=ab. The first coordinate gives c=S−u; the second gives

P=uS−(u²+v)/2.

The third becomes

w=u³+(3/2)δS.                                                  (8)

If δ=0, equation (8) forces w=u³. Conversely (u,u²,u³) belongs to T_p. Thus only one w works for each u when δ=0.

If δ≠0, equation (8) uniquely gives

S=2(w−u³)/(3δ).

The parameters a,b exist if and only if the discriminant

S²−4P=(S−2u)²+2δ                                               (9)

is a square, with zero permitted. Once it is a square, its two roots and c=S−u supply the representation, so this is both necessary and sufficient.

Let χ be the quadratic character, with χ(0)=0. For c≠0,

sum over y in F_p of χ(y²+c)=−1.

Indeed, the number of solutions of z²−y²=c is p−1: choose z−y to be any nonzero value, set z+y=c/(z−y), and recover z,y by division by 2. Counting instead by y gives p plus the displayed sum. Also y²+c has 1+χ(−c) zeros. The number of y for which y²+c is a square, including zero, is therefore

[p + (−1) + (1+χ(−c))]/2 = (p+χ(−c))/2.

As w runs over F_p, S−2u does too. For fixed δ≠0, (9) succeeds for (p+χ(−2δ))/2 values of w. Summing over δ≠0 cancels the character term: multiplication by −2 permutes the nonzero field, and multiplication by any nonsquare permutes that field while negating χ, so its character sum is zero. Each u contributes p(p−1)/2+1 points, proving (7).

The midpoint contribution can also be computed exactly. For two distinct parameters u+d,u−d, d≠0, their midpoint is

(u, u²+d², u³+3ud²).

Here δ=d² and (8) forces S=2u, so (9) becomes 2d². Thus every nontrivial midpoint is in T_p if χ(2)=1, and none is in T_p if χ(2)=−1. There are p(p−1)/2 distinct nontrivial midpoints, by the Sidon property and invertibility of 2. Hence the exact number of addable group elements is

  p(p−1)(p+2)/2,  if χ(2)=1;
  (p³−p)/2,      if χ(2)=−1.                                   (10)

This candidate is far from maximal even in the group model. The calculation supplies no efficient repair or integer interval cover. Encoding coordinates into integers would additionally require handling carries and actual integer, rather than modular, blocking equations. Equation (10) alone does not rule out every restricted box or every modification of this curve.

# 4. Route (b): independent thinning and a full second-moment calculation

This section proves a quantitative limitation of one precise model. It does not claim that all random or correlated constructions fail.

Let k≥3, M=k²−k+1, and D⊆Z/MZ be a perfect difference set satisfying (6). Independently retain each element of D with probability 0<ρ≤1/2, obtaining A. Every outcome A is Sidon. We study points outside D; the omitted points of D are automatically addable, since adjoining one of them still gives a subset of the Sidon set D.

## 4.1 Witness counts and bounded overlap

Fix x outside D. For each b in D, the nonzero difference x−b has a unique representation a−c. Consequently there are exactly k ordered representations

x=a+b−c,  a,b,c in D.

The negative element c cannot equal either positive element, since that would put x in D. Let t_x be the number of these representations having a=b. The remaining representations pair under interchange of a,b, so the number of distinct three-element witness supports is

h_x=(k−t_x)/2.                                                 (11)

A three-element support cannot supply two different negative choices for the same x: that would give 2(c−c')=0. The group has odd order, so c=c'. Diagonal witnesses have two-element supports, at most t_x of them. There is at most one additional midpoint witness 2x=a+b, since D is Sidon. Its two elements are distinct, as x is outside D.

Every vertex of D occurs in at most two distinct triple-witness supports for fixed x. In a positive role d, the equation x=d+b−c fixes the nonzero difference b−c=x−d and hence fixes b,c. In a negative role d, the equation a+b=x+d fixes the unordered pair a,b. Including the possible midpoint witness, the vertex degree is at most 3.

Every pair (a,c) of distinct elements of D gives 2a−c outside D. Otherwise 2a=x+c with x,c in D would contradict its Sidon property. Therefore

sum over x outside D of t_x = k(k−1).

There are (k−1)² points outside D. Define

G={x outside D:t_x≤4},  g=|G|.

At most k(k−1)/5 points can have t_x≥5, and k(k−1)/5≤(k−1)²/2 for k≥3. Thus

g ≥ (k−1)²/2.                                                  (12)

For x in G, let F_x be its family of distinct blocking supports. It has at most k/2 supports of size 3, at most 5 supports of size 2, and vertex degree at most 3. A support blocks x exactly when all its vertices are retained.

For distinct x,y in G, their families have at most one common three-element support. Indeed, if c_x,c_y are the negative vertices of that support, then

x−y=2(c_y−c_x).

Difference uniqueness determines this ordered pair, since 2 is invertible; the remaining vertex is then determined by x. There are at most five common two-element supports.

## 4.2 Two elementary probability tools, with proofs

First, decreasing events under independent Bernoulli coordinates are positively associated. For completeness, for two decreasing real functions f,g, induct on the number of coordinates. The law of total covariance, conditioning on the last Bernoulli coordinate X, gives

Cov(f,g) = E[Cov(f,g | X)]
           + ρ(1−ρ)(E[f|X=1]−E[f|X=0])
                      (E[g|X=1]−E[g|X=0]) ≥ 0.

The first term is nonnegative by induction and the two last differences are both nonpositive. Apply this to indicator functions and then successively to intersections of decreasing events. In particular, the probability that none of a family of supports is fully selected is at least the product of their individual avoidance probabilities.

Second, let E_1,...,E_n be events determined by independent coordinates, and declare i,j adjacent when their coordinate supports intersect. With p_i=P(E_i),

|P(no E_i) − product_i(1−p_i)|
 ≤ sum over adjacent i<j of [P(E_i intersect E_j)+p_i p_j].     (13)

Proof. At step i, let B be avoidance of the earlier nonneighbors and C avoidance of the earlier neighbors. E_i is independent of B. If q_i is the probability of avoiding the first i events, then

q_i−(1−p_i)q_(i−1)
 = P(E_i intersect B intersect C^c) − p_i P(B intersect C^c).

The absolute value is at most the sum, over earlier neighbors j, of P(E_i intersect E_j)+p_i p_j, by the union bound. Iterating the recurrence, whose multiplier 1−p_i lies in [0,1], proves (13). No Janson or Poisson-approximation theorem is invoked without proof.

## 4.3 A lower bound on the expected number of holes

Put

b = exp(−4kρ³/7 − 20ρ²/3),

ε = 5ρ² + 201ρ³ + 15kρ⁴.                                      (14)

For x in G let I_x indicate that x is unblocked and put U=sum_(x in G) I_x. Write

w_x = product_(e in F_x)(1−ρ^|e|).

Positive association gives P(I_x=1)≥w_x. For 0≤z<1,

log(1−z)=−integral_0^z dt/(1−t) ≥ −z/(1−z).

Since ρ≤1/2, we have 1/(1−ρ³)≤8/7 and 1/(1−ρ²)≤4/3. Using at most k/2 triple supports and five pair supports,

w_x ≥ exp(−(k/2)ρ³/(1−ρ³)−5ρ²/(1−ρ²)) ≥ b.

Thus

E U ≥ g b ≥ (k−1)² b/2.                                        (15)

## 4.4 Pair covariance and an explicit failure probability

Consider the union of the two distinct-support families F_x and F_y. Its vertex degree is at most 6. It has at most k three-element supports and ten two-element supports.

A three-element support intersects at most 3(6−1)=15 others. There are at most 15k/2 pairs of intersecting three-element supports. Distinct such supports have union size at least 4; their contribution per pair in (13) is at most ρ⁴+ρ⁶≤2ρ⁴. Their total contribution is at most 15kρ⁴.

A two-element support intersects at most 2(6−1)=10 others. There are at most 100 intersecting pairs involving a two-element support; counting a pair twice only enlarges this bound. Distinct supports of these types have union size at least 3, and their probability product is at most ρ⁴. The contribution per pair in (13) is at most ρ³+ρ⁴≤2ρ³, and their total contribution is at most 200ρ³.

Let w_xy be the product of the avoidance factors over the union family. Removing duplicate factors from w_x w_y increases it by at most the sum of their event probabilities: 1−product(1−z_i)≤sum z_i for z_i in [0,1]. Section 4.1 therefore gives

w_xy ≤ w_x w_y + 5ρ² + ρ³.

Applying (13) now yields

P(I_x=I_y=1) ≤ w_x w_y + 5ρ² + 201ρ³ + 15kρ⁴
             = w_x w_y + ε.

As P(I_x=1)P(I_y=1)≥w_xw_y, we conclude Cov(I_x,I_y)≤ε. Also Var(I_x)≤1. Hence

Var U ≤ g+g(g−1)ε,

P(U=0) ≤ Var U/(E U)² ≤ (1/g+ε)/b²
        ≤ [2/(k−1)² + 5ρ² + 201ρ³ + 15kρ⁴]
           exp(8kρ³/7 + 40ρ²/3).                              (16)

The first probability inequality is Chebyshev's inequality applied to deviation E U. Blocking every point outside D implies U=0, so (16) also bounds the success probability for outside-residue coverage. The right side may exceed 1 for small parameters; it remains a valid upper bound.

## 4.5 Explicit sublogarithmic specialization

Fix C>0 and 0≤θ<1/3. Set

L_0 = max{128, 6 log(2C), ((96/7)C³)^(1/(1−3θ))},

K(C,θ) = exp(L_0),

J(C) = exp(10/3)(8+5C²+201C³+15C⁴).

For every perfect difference set as above with integer k≥K(C,θ), choose

ρ=C k^(−1/3)(log k)^θ.

Then

E|A| = C k^(2/3)(log k)^θ,

P(all points outside D are blocked) ≤ J(C) k^(−1/6).            (17)

All onsets and constants are explicit. To check them, write L=log k. For L≥1, log L≤L/2: the maximum of log L−L/2 occurs at L=2 and equals log 2−1<0. Consequently

log ρ ≤ log C−L/3+(log L)/3 ≤ log C−L/6 ≤ −log 2.

Thus ρ≤1/2. The last component of L_0 ensures

(8/7)kρ³=(8/7)C³ L^(3θ)≤L/12.

Also (40/3)ρ²≤10/3. For L≥128, log L≤L/16: the difference L/16−log L is positive at 128 and increasing thereafter. Since θ<1/3, this gives

ρ²≤C² k^(−5/8),
ρ³≤C³ k^(−15/16),
kρ⁴≤C⁴ k^(−1/4).

Furthermore 2/(k−1)²≤8/k². Substitution in (16) bounds its bracket by (8+5C²+201C³+15C⁴)k^(−1/4), and its exponential by exp(10/3)k^(1/12), proving (17).

For any specified 0<η<1, the probability in (17) is at most η whenever

k ≥ max{K(C,θ), (J(C)/η)^6}.

This supplies an explicit replacement for a statement that the success probability is o(1). A negative θ can also be bounded by the θ=0 case for k≥e, by coupling the smaller retention probability to the larger one; coverage is an increasing event.

Interpretation. This is a genuine second-moment calculation, but it goes in the obstructive direction: independent thinning at the proposed scale typically leaves unblocked outside points. It does NOT prove there is no exceptional successful subset, nor does it prevent a later efficient repair, conditioning, correlated sampling, or a different host. In particular, the existence problem cannot be rejected merely because an expected number of holes is large.

# 5. Other attempted steps and their exact stopping points

1. One representative per modular Sidon residue: Sidonness lifts for free, but maximality does not. Section 2.1 gives explicit addable points. This obstruction is partly resolved by (5); the remaining unproved estimate is u≤Ck for H proportional to k, with constants and a usable construction.

2. Several complete height layers: the four-term equality in Section 2.3 destroys Sidonness. More selective levels must satisfy the exact common-difference restriction (3). This does not rule out a successful selective repair.

3. Cubic algebraic graph: equations (8)–(10) leave exactly the stated quadratic-character gaps. No repair of size proportional to p was obtained. Group coverage also would not automatically imply interval coverage.

4. Independent thinning of a perfect difference set: Sections 4.1–4.5 show that a second-moment replacement for a union bound does not make this unmodified sampler cover its outside points with substantial probability at the requested sublogarithmic scale. Missing host points are a separate obstruction to maximality. The calculation neither rules out rare samples nor bounds the cost of an intelligent repair.

5. Literal add-one-per-hole repair: the universally valid certificate |A|+number of holes gives no desired improvement when the hole count is large. A lower bound on E U is only an obstruction to this particular expectation-based certificate, not a lower bound on the size of an optimal repair. The fibre repair (5) illustrates why that distinction matters.

6. Independent sampling directly in [N] with a deletion for every additive collision: this has no automatic Sidon guarantee. Here is an exact calculation behind the stopping point. For N≥10, let ℓ=floor(N/5), and choose a in [1,ℓ], b in [ℓ+1,2ℓ], c in [2ℓ+1,3ℓ]. Then d=b+c−a satisfies c<d≤5ℓ−1≤N and a+d=b+c. These are ℓ³ distinct four-element collision supports, since their increasing order determines a,b,c. With independent retention probability r and m=Nr, their expected number is ℓ³r⁴≥m⁴/(1000N), because ℓ≥N/10. If m³>1000N, this expectation already exceeds m. Thus the elementary estimate E(retained size)≥m−E(number of all collisions), obtained by paying one deletion per collision, gives no positive guarantee there. Shared collisions could be repaired more efficiently; this argument proves no lower bound on the necessary deletions. No stronger collision control was derived.

No unproved covering assertion from any of these attempts is used as a theorem.

# 6. Exact finite checks

All computations were written and run in this session using Node, without SAT/ILP solvers, worker threads, external data, or random seeds. Computation supports the derivations; it is not used to extrapolate an asymptotic theorem. The algorithms below specify the checked objects completely.

## 6.1 Every integer Sidon subset for N=1,...,24

A depth-first enumeration appended elements in increasing order. A candidate x was accepted precisely when 2x and every x+a were absent from the existing unordered-pair sum set. Thus it enumerated every Sidon subset once. At every node, a separately generated set of triple values and integer midpoint values was compared, for every outside x in [N], with direct addability via the sum set. At maximal nodes, (2) was checked.

There were 84,274 Sidon subsets across these 24 intervals, 1,436,132 outside-point comparisons, and zero failures.

| N | s(N), exhaustively computed | Sidon subsets | Maximal Sidon subsets |
|---:|---:|---:|---:|
| 1 | 1 | 2 | 1 |
| 2 | 2 | 4 | 1 |
| 3 | 2 | 7 | 3 |
| 4 | 2 | 13 | 3 |
| 5 | 3 | 22 | 6 |
| 6 | 3 | 36 | 14 |
| 7 | 3 | 57 | 20 |
| 8 | 3 | 91 | 24 |
| 9 | 3 | 140 | 36 |
| 10 | 3 | 216 | 64 |
| 11 | 4 | 317 | 110 |
| 12 | 4 | 463 | 176 |
| 13 | 4 | 668 | 238 |
| 14 | 4 | 962 | 294 |
| 15 | 4 | 1,359 | 370 |
| 16 | 4 | 1,919 | 504 |
| 17 | 4 | 2,666 | 736 |
| 18 | 4 | 3,694 | 1,086 |
| 19 | 4 | 5,035 | 1,592 |
| 20 | 4 | 6,845 | 2,240 |
| 21 | 4 | 9,188 | 2,982 |
| 22 | 4 | 12,366 | 3,788 |
| 23 | 5 | 16,417 | 4,700 |
| 24 | 5 | 21,787 | 5,814 |

Examples of attained minima: {2,5,6} in [10], {4,7,12,13} in [22], and {1,2,4,8,20} in [24]. All enumeration and count operations in this check use integers within JavaScript's exact range.

## 6.2 Three explicit perfect difference sets and all their subsets

The sets were

- M=7, D={0,1,3};
- M=13, D={0,1,3,9};
- M=21, D={0,1,4,14,16}.

Each unordered pair sum was checked for uniqueness modulo M; every nonzero ordered difference occurred exactly once. For every x outside D, all witnesses were enumerated. The ordered triple count was k, the total witness-family vertex degree was at most 3, and any two outside points shared at most one three-element support.

For all 8, 16, and 32 subsets respectively, the witness-family criterion was compared against direct modular pair-sum addability at every outside point: 32+144+512=688 comparisons, zero failures.

Let the histogram list “number of outside holes : number of subsets.” The exact histograms were:

- M=7: 0:1, 1:3, 4:4.
- M=13: 0:5, 6:6, 9:5.
- M=21: 0:6, 5:6, 6:3, 12:1, 13:9, 15:1, 16:6.

Weighted enumeration also computed the first two moments of U on G and P(U=0). A subset of size a received exact integer weight (d−1)^(k−a) over denominator d^k for ρ=1/d. These fraction calculations used BigInt. The resulting fractions are intentionally unreduced:

| M | g | ρ | E U | E U² | P(U=0) |
|---:|---:|:---:|:---:|:---:|:---:|
| 7 | 4 | 1/2 | 19/8 | 67/8 | 1/8 |
| 7 | 4 | 1/4 | 225/64 | 873/64 | 1/64 |
| 13 | 9 | 1/2 | 81/16 | 621/16 | 5/16 |
| 13 | 9 | 1/4 | 2025/256 | 17253/256 | 13/256 |
| 21 | 15 | 1/2 | 276/32 | 3348/32 | 6/32 |
| 21 | 15 | 1/4 | 13662/1024 | 192510/1024 | 16/1024 |

For M=21 the point with t_x=5 is omitted from G; thus these moments and the preceding full-outside histogram concern slightly different variables. Floating-point evaluations of the coarse mean/variance bounds were also checked at these six parameters with tolerance 10^(−12), with zero failures. Those evaluations are only numerical checks; the inequalities are proved above.

## 6.3 Every height assignment in two and three layers

For each of the three D above and H=2,3, every map f:D→{0,...,H−1} was enumerated, giving A={d+Mf(d)} in {0,...,HM−1}. There were 407 assignments in total. Every A was integer Sidon. Every other integer with a residue in D was directly tested and was addable: 3,488 such comparisons, zero failures.

| M | k | H | Assignments | Minimum initial holes, all residues | Best ascending-greedy final size |
|---:|---:|---:|---:|---:|---:|
| 7 | 3 | 2 | 8 | 3 | 4 |
| 7 | 3 | 3 | 27 | 8 | 5 |
| 13 | 4 | 2 | 16 | 5 | 5 |
| 13 | 4 | 3 | 81 | 13 | 6 |
| 21 | 5 | 2 | 32 | 7 | 6 |
| 21 | 5 | 3 | 243 | 19 | 7 |

“Best ascending-greedy” means: begin with each lift, scan all ambient integers in increasing order, add when direct sum testing permits, then minimize the final size over those lifts. It is not a minimum over every possible repair.

In a separate pass on all 407 assignments, repair was restricted first to residues in D, then extended to all remaining integers, both scans in increasing order. The largest number of first-phase additions was exactly H−1 in every row. The final set was maximal and its size satisfied (5) in every case. Zero failures.

## 6.4 Cubic curves over nine prime fields

For p=5,7,11,13,17,19,23,29,31, all unordered pair sums, all triple values, and all midpoints of C_p were enumerated. Every element of F_p³ was tested against the discriminant criterion (8)–(9). Pair sums were unique and there were zero criterion mismatches.

| p | Triple-set size | Midpoint-set size, including C_p | Unblocked points |
|---:|---:|---:|---:|
| 5 | 55 | 15 | 60 |
| 7 | 154 | 28 | 189 |
| 11 | 616 | 66 | 660 |
| 13 | 1,027 | 91 | 1,092 |
| 17 | 2,329 | 153 | 2,584 |
| 19 | 3,268 | 190 | 3,420 |
| 23 | 5,842 | 276 | 6,325 |
| 29 | 11,803 | 435 | 12,180 |
| 31 | 14,446 | 496 | 15,345 |

These counts agree with (7) and (10). All field operations were integer modular arithmetic, and square membership was checked by exhaustive enumeration of squares.

# 7. Proof audit, remaining step, and cost

Before reporting, the implications were checked again from the written argument: the blocking criterion includes midpoint collisions; the fibre repair counts positive differences globally, not separately per fibre; the cubic curve includes diagonal sums; the random families use distinct event supports; double-counted intersections only enlarge the error; and the Chebyshev argument bounds sampling success rather than asserting nonexistence. The explicit onset in (17) was substituted into each preceding term separately.

The missing mathematical step remains an effective correlated coverage or repair theorem giving an upper bound for every sufficiently large integer N with logarithmic exponent strictly below 1/3. A concrete next direction is to produce the outside-residue estimate u≤Ck in (5) at H proportional to k, then address all interval lengths. This is a proposed mathematical direction, not a scheduled follow-up or a proved result.

Five mathematical Node invocations used a single JavaScript execution thread, with --single-threaded --v8-pool-size=1; no parallel compute jobs or solver processes were used. Their measured user+system CPU times, in seconds, were 0.226457, 0.021781, 0.254175, 0.025990, and 0.051652, totaling 0.580055 CPU seconds. Their internally measured elapsed times totaled 0.584935536 seconds. File handling and control-plane calls are not included in those mathematical-compute measurements. No paid compute was used. Model-token/monetary usage is not available to this process.

Exactly this one file was written under /work. The final disposition is PARTIAL for the research target and complete for the requested clean-room probe deliverable.
