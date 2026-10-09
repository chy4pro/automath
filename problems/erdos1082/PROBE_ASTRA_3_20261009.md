PARTIAL — For every n ≥ 2, re-proved M > (n−1)/3 and hence M ≥ ⌈n/3⌉; proved exact defect and stability identities and explicit obstructions to both proposed counting routes. No δ > 0 in the requested linear improvement is proved.

# Scope and outcome

Target: for all finite sets S of n points in the Euclidean plane with no three collinear, prove M ≥ (1/3+δ)n−B with explicit absolute δ>0 and B, where M is the largest number of distinct positive distances seen from a point of S.

This report does not establish that target. Both specified route seeds were worked. All mathematical claims below were derived from the brief and elementary mathematics; no repository, paper, web source, or other agent's file was consulted. The designated output file did not exist at the beginning of this continuation. The earlier continuation comment was treated as a lead, and its mathematical claims were re-derived.

The useful exact sufficient condition is as follows. With the nonnegative quantities D and C defined below, for every n≥2,
\[
 M\ \ge\ {n-1\over3}+{D+C\over3n}.                     \tag{1}
\]
Consequently D+C≥c n² would imply
\[
 M\ge(1/3+c/3)n-1/3.
\]
No uniform positive c has been proved here. This sufficient condition is stronger than merely proving the target for the maximum M; it is not asserted to be necessary.

There are no unspecified asymptotic error terms in the proved statements.

# 1. Exact accounting

For p∈S let t_p be its number of distinct positive distances, and let
A_{p,1},…,A_{p,t_p} be its distance classes, of positive integer sizes
a_{p,1},…,a_{p,t_p}. Thus
\[
 \sum_i a_{p,i}=n-1,\qquad T:=\sum_p t_p,\qquad M=\max_p t_p.
\]
Write N=n(n−1). An isosceles incidence is an apex p and an unordered base
b={x,y}⊂S\{p} with |p−x|=|p−y|. Let k_b be the number of its apexes.
Every apex lies on the perpendicular bisector of xy. That line contains
at most two points of S, so 0≤k_b≤2. Put
\[
 I:=\sum_{p,i}\binom{a_{p,i}}2=\sum_b k_b,\qquad
 D:=\sum_b(2-k_b)=N-I,
\]
\[
 C:=\sum_{p,i}{(a_{p,i}-2)(a_{p,i}-3)\over2},\qquad
 E:=\sum_{p,i}(a_{p,i}-3)^2.
\]
Both D and E are nonnegative. C is nonnegative because, for positive
integer a, its summand equals 1 at a=1, 0 at a=2 or 3, and is positive
at a≥4.

For every integer a,
\[
 \binom a2=2a-3+{(a-2)(a-3)\over2}.
\]
Summing and using Σa=N gives I=2N−3T+C. Substitution of I=N−D proves
\[
 \boxed{3T=N+D+C}.                                      \tag{2}
\]
Since T≤nM, this proves (1).

A separate expansion gives
\[
 (a-3)^2-3{(a-2)(a-3)\over2}={a(3-a)\over2}.
\]
Its sum equals (3N−Σa²)/2=N−I=D, because Σa²=2I+N. Hence
\[
 \boxed{E=D+3C},\qquad
 \boxed{9T=3N+2D+E}.                                    \tag{3}
\]
These equalities show precisely what is, and is not, gained by the
unweighted class-size second moment.

One can pad every row to M classes by allowing a=0. If
\[
 V:=\sum_{p}\sum_{i=1}^{M}(a_{p,i}-3)^2
   =E+9(nM-T),
\]
then
\[
 \boxed{9nM=3N+2D+V}.                                   \tag{4}
\]
In particular every term in this formula is explicit.

# 2. A self-contained strictness argument

Here n≥2. Form the diameter graph: two points are adjacent if their
distance is the diameter d>0 of S.

First, every endpoint u of a diameter uv is an exposed vertex of the
convex hull. For x∈S\{u}, the inequality |x−v|²≤|u−v|² implies
\[
 2(x-u)\cdot(v-u)\ge |x-u|^2>0.
\]
Thus u uniquely minimizes the linear functional x↦x·(v−u).

Second, any two diameter edges with disjoint endpoints cross in their
interiors. Otherwise their four endpoints, being convex-hull vertices,
occur as A,B,C,D in cyclic order with AB and CD opposite sides. Let O
be the intersection of diagonals AC and BD. Strict triangle inequalities
give
\[
 |AB|+|CD|
 <(|AO|+|OB|)+(|CO|+|OD|)
 =|AC|+|BD|\le2d.
\]
The left side is 2d, a contradiction. Strictness follows because the
vertices form a nondegenerate convex quadrilateral.

Third, the diameter graph has a nonisolated vertex of degree at most 2.
Indeed, if a vertex a has at least three neighbors, choose three of
them b,c,e in that order along the convex-hull boundary with a removed.
The middle neighbor c can have no diameter neighbor other than a:
a further edge cx would have to cross both ab and ae. For x distinct
from a,b,e, crossing ab requires x on the open boundary arc from a to b
that avoids c, while crossing ae requires x on the disjoint open arc
from e to a that avoids c. If x=b, the edge cb fails to cross ae;
if x=e, ce fails to cross ab. All possibilities contradict the preceding
crossing property. Therefore c has degree 1. If no vertex has degree
at least 3, any endpoint of any diameter edge already has degree at
most 2. This proves the assertion in every case.

Now (2) gives M≥(n−1)/3. Suppose equality held. Then T≤nM=N/3,
so (2) forces T=N/3 and D=C=0. By (3), E=0, and therefore every
distance class has size exactly 3. In particular every nonisolated
diameter-graph vertex would have degree exactly 3. This contradicts
the preceding paragraph. Hence
\[
 M>{n-1\over3},\qquad M\ge\left\lceil{n\over3}\right\rceil
 \quad(n\ge2).                                          \tag{5}
\]
The integer conclusion follows by considering n modulo 3.
For n=1, M=0; that degenerate case is excluded from (5).

This is only a strictness result. The argument supplies a small
exceptional class, not a positive fraction of the approximately n²
incidences required for the target.

# 3. Route (a): exact stability and kite structure

Let R=D+C. Equations (2)–(3) give
\[
 R=3T-N\le3nM-N,\qquad E=D+3C\le3R.                     \tag{6}
\]
For example, for every ε,B≥0 and every n≥2,
\[
 M\le(1/3+\varepsilon)n+B
 \quad\Longrightarrow\quad
 R\le3\varepsilon n^2+(3B+1)n,\quad
 E\le9\varepsilon n^2+(9B+3)n.                         \tag{7}
\]
Alternatively M≤(n−1)/3+ηn implies R≤3ηn² and E≤9ηn²
for every η≥0.

Call a class bad when its size is not 3. There are at most E bad
classes because each contributes at least 1 to E. Let U be the number
of ordered pairs (p,x), x≠p, belonging to bad classes at p, and J the
number of isosceles incidences whose apex class is bad. Then
\[
 U=\sum_{a\ne3}a\le4E,\qquad
 J=\sum_{a\ne3}\binom a2\le6E.                          \tag{8}
\]
Here the cases a=1,2 can be checked directly. For a≥4 write b=a−3≥1.
The remaining inequalities follow respectively from
\[
 4b^2-(b+3)=(b-1)(4b+3)\ge0,
\]
\[
 6b^2-\frac{(b+3)(b+2)}2
   =\frac{(b-1)(11b+6)}2\ge0.
\]
Thus no bounded-class-size hypothesis was silently used.

At most D bases have k_b<2, since each contributes at least 1 to D.
At most J further bases have a bad class at an apex. Consequently
all but at most
\[
 D+6E=7D+18C\le18R                                     \tag{9}
\]
of the N/2 bases have exactly two apexes, with class size 3 at both.
For ε=B=0 in (7), the explicit bounds are U≤12n and at most 18n
exceptional bases; for general ε,B substitute (7) into (8)–(9).
These are rigorous stability reductions, not a contradiction.

For such a good base {x,y} with apexes p,q, its perpendicular bisector
is the line pq, and reflection in pq exchanges x,y. Thus it determines
a kite with two specified three-point distance circles.

One can package the structure into a graph H. Its vertices are the
distance classes of size 3, represented by their circles. Each good
base gives an edge between its two apex circles. This graph is simple:
two different circles have at most two intersection points, and thus
cannot determine two different common unordered bases. To justify
the intersection statement, subtract the two circle equations to get
a line if the centers differ; a line meets a circle in at most two
points. Concentric distinct circles are disjoint. Each vertex of H
has degree at most 3, one for each pair in its class.

If A₃ is its number of vertices and e(H) its number of edges, then
\[
 3A_3=N-U,\qquad
 0\le3A_3-2e(H)\le D+J\le18R.                         \tag{10}
\]
For the upper bound, a missing half-edge at a size-3 class either has
no second apex (charged to a base with k_b=1), or its second apex
class is bad (charged to that bad isosceles incidence). These charges
are injective within each type. The former type numbers at most D,
and the latter at most J.

The unresolved step is quantitative geometry: (10) gives a graph
that is almost 3-regular when R is small, but does not show that such
a graph, with the additional center/point relations, must have a
positive fraction of missing half-edges or bad classes.

## 3.1 A fully saturated local component really can occur in the plane

The following eight integer points have no three collinear:
\[
\begin{array}{c|rr}
i&x_i&y_i\\\hline
0&0&0\\
1&1008&0\\
2&252&756\\
3&1260&1512\\
4&504&252\\
5&504&861\\
6&1722&-154\\
7&1026&774
\end{array}
\]
Point 4 has a distance class exactly {0,1,2}; point 5 exactly {0,1,3};
point 6 exactly {0,2,3}; and point 7 exactly {1,2,3}. These are the
circumcenters of the indicated triples. All other classes are singletons.
All six pairs among 0,1,2,3 have exactly the following two apexes:
\[
 01:45,\quad02:46,\quad03:56,\quad12:47,\quad13:57,\quad23:67.
\]
Therefore H is exactly K₄, with all four degrees equal to 3.
In particular, a claim that every component of H must meet a deficient
base or a non-size-3 class is false.

These are exact finite assertions, checked by integer squared distances
and all 56 integer determinants. The smallest absolute determinant is
76734, so no determinant vanishes. Reproduction code is below.
The complete set has
\[
 n=8,\quad T=48,\quad M=7,\quad I=12,\quad
 D=C=44,\quad E=176.
\]
It is not a near-extremal configuration for the requested theorem:
its purpose is to refute this specific local propagation argument.

## 3.2 Missing apexes alone cannot have a universal quadratic lower bound

Let m≥3 be odd. Take the m vertices of a regular polygon on the unit
circle together with its center O, so n=m+1. No three polygon vertices
are collinear because a line meets a circle in at most two points.
A line through O would contain two polygon vertices only if they were
antipodal, impossible for odd m. Thus the whole set has no three
collinear.

For two polygon vertices indexed i,j modulo m, their perpendicular
bisector contains O and the polygon vertex indexed
k=(i+j)/2 modulo m, using the inverse of 2 modulo odd m.
The latter vertex is distinct from i,j. These are exactly two apexes
by the no-three-collinear hypothesis.

For a base {O,v}, an apex would be another polygon vertex w with
|w−v|=|w−O|=1. A chord of the unit circle has length 1 exactly when
its smaller central angle is π/3. The possible smaller angles here are
2πr/m, 1≤r≤(m−1)/2; equality would require m=6r, impossible for odd m.
Thus these m bases have zero apexes, and
\[
 D=2m.                                                 \tag{11}
\]

At O the sole class has size m. At each polygon vertex there are
(m−1)/2 classes of size 2, and the singleton {O}. Indeed the chord
lengths 2sin(πr/m) strictly increase for the indicated r, and none
equals 1 by the preceding argument. Direct substitution gives
\[
 T=1+\frac{m(m+1)}2,\quad M=\frac{m+1}2,\quad I=m(m-1),
\]
\[
 C=\frac{m^2-3m+6}{2},\quad
 R=\frac{m^2+m+6}{2},\quad
 E=\frac{3m^2-5m+18}{2}.                               \tag{12}
\]
For any fixed c>0, choosing an odd m>2/c gives
D/(m+1)²=2m/(m+1)²<2/m<c.
Thus D≥cn² is false as a universal assertion. This family does not
refute a bound for D+C, and does not refute the target for M.

## 3.3 Subsampling does not amplify the strictness argument by itself

Retain every point independently with probability q∈[0,1], obtaining S′.
Define D(S′) by the same base count even when |S′|<2. A base survives
with probability q², and a specified apex together with that base
survives with probability q³. Linearity of expectation therefore gives
\[
 \mathbb E D(S')=q^2N-q^3I
               =q^2((1-q)N+qD).                      \tag{13}
\]
Even hypothetical data with D=0 have the positive term q²(1−q)N
when 0<q<1. Thus the weak subset strictness supplied by the diameter
argument is compatible with zero parent defect. No stronger
subset inequality yielding a parent quadratic defect was obtained.

# 4. Route (b): weights and second moments

For any real weight w(a) on integers a≥2, put
\[
 X_b:=\sum_{p\ {\rm apex\ of}\ b} w(a_{p,b}),
\]
where a_{p,b} is the size of the class containing the two endpoints.
Interchanging finite sums gives the exact identities
\[
 \sum_b X_b=\sum_{p,i}\binom{a_{p,i}}2w(a_{p,i}),        \tag{14}
\]
\[
 \sum_bX_b^2=
 \sum_{p,i}\binom{a_{p,i}}2w(a_{p,i})^2+
 2\sum_{b:k_b=2}w(a_{p,b})w(a_{q,b}).                  \tag{15}
\]
Size-1 classes contribute zero and require no defined weight.
The second term of (15) couples the two apex class sizes of a kite.
It is not determined by the class-size histogram alone.

As a natural normalized choice, take w(a)=2/(a−1). Then a class of
size a≥2 contributes exactly a to (14), so
\[
 \sum_bX_b=N-s_1,
\]
where s₁ is the number of singleton classes. When a=3, w(a)=1.

In hypothetical homogeneous data with every class of size 3 and
every base having two apexes, necessarily T=N/3. For an arbitrary
w, all N/2 values X_b equal 2w(3). Thus
\[
 \sum_bX_b=Nw(3),\quad
 \sum_bX_b^2=2Nw(3)^2
 =\frac{(\sum_bX_b)^2}{N/2}.                            \tag{16}
\]
The Cauchy–Schwarz second-moment inequality is an equality. Hence
these weights and this second moment, without a further geometric
restriction, provide no strict gain.

The unweighted base-deficit second moment has the same limitation.
If b_j is the number of bases with k_b=j, then
\[
 D=2b_0+b_1,\qquad
 \sum_b(2-k_b)^2=4b_0+b_1,\qquad
 D\le\sum_b(2-k_b)^2\le2D.                             \tag{17}
\]
Both inequalities follow by subtracting D or the middle expression
from 2D; their differences are respectively 2b₀ and b₁.

A third class-count bound from circle uniqueness is also too weak:
\[
 \sum_{p,i}\binom{a_{p,i}}3\le\binom n3.               \tag{18}
\]
Every noncollinear triple determines a unique circle and center, so
is counted at most once. At the homogeneous values the left side
is N/3, whereas the right side is N(n−2)/6. For n≥4, (18) permits
the homogeneous data, with ratio 2/(n−2). Thus it gives no contradiction.

## 4.1 A symmetric metric model saturates all these accounting bounds

This is an abstract metric model, not a planar configuration and not
a counterexample to the target.

For any integer d≥1, let the point set be the vector space F₄ᵈ,
with n=4ᵈ. There are K=(n−1)/3 one-dimensional F₄ subspaces:
their nonzero vectors partition the n−1 nonzero vectors into triples.
Enumerate them L₁,…,L_K. For distinct x,y define the distance
\[
 \rho(x,y)=1+\frac{j}{K+1}
 \quad\hbox{when }y-x\in L_j,
 \qquad \rho(x,x)=0.
\]
It is symmetric because −1=1 in F₄. All positive distances lie
strictly between 1 and 2, so the triangle inequality is strict when
the three points are distinct: one distance is <2 and the sum of
the other two is >2. Cases with repeated points are immediate.

At x each distance class is (x+L_j)\{x}, of size 3; thus every
point sees exactly K distances.

For a base {a,b}, equality ρ(p,a)=ρ(p,b) holds exactly when
a−p and b−p lie in one common one-dimensional subspace. Subtracting
shows that this must be the subspace spanned by b−a, and p must lie
on the affine line a+F₄(b−a). Conversely either of the two points
of this four-point line other than a,b is an apex. Hence k_b=2
for every base. Consequently
\[
 T=N/3,\quad I=N,\quad D=C=E=0,\quad M=(n-1)/3.         \tag{19}
\]
Distinct abstract class sets also have intersections of size at most
2: if their underlying affine lines agree, they omit different
centers and share two points; different affine lines intersect in
at most one point. A triple occurs in at most one class, since it
would determine the affine line and its missing fourth point.

It follows that a proof using only the symmetric metric axioms,
these class-size counts, the two-apex bound, these class intersection
bounds, and the resulting weighted moments cannot force a positive
linear improvement. This statement is about this listed collection
of hypotheses; it does not rule out using additional Euclidean facts.

The model fails a basic planar constraint: every affine line has
four pairwise equidistant points. Four such points cannot occur in
the plane. To see this, place the first two at (−r/2,0),(r/2,0).
The only two other points at distance r from both are
(0,√3 r/2),(0,−√3 r/2), whose mutual distance is √3 r≠r.
This identifies a concrete geometric fact omitted by the model.
The diameter-graph proof also detects its failure, but only at the
strictness level used above.

## 4.2 A failed attempt to remove that local model obstruction

I also tried a ten-point model built by partitioning K₁₀ into three
Petersen graphs, giving each graph its own distance in (1,2).
Represent a Petersen graph on the ten two-element subsets of
{0,1,2,3,4}, with edges between disjoint subsets. It has degree 3.
An adjacent pair has no common neighbor; a nonadjacent distinct pair
has exactly one common neighbor, namely the complement of its
three-element union.

If three edge-disjoint copies partitioned K₁₀, every base would be
adjacent in one color and nonadjacent in two colors. It would
therefore have 0+1+1=2 same-color apexes, and every class would have
size 3, without a monochromatic K₄.

The exact backtracking check described below found no such partition:
13,810 partial search nodes, 288 complete second-copy embeddings
edge-disjoint from the first, and zero with a Petersen residual graph.
Fixing the image of vertex 0 to 0 loses no possible second-copy
graph, because the source Petersen graph is vertex-transitive
(the permutations of the underlying five symbols act transitively).
This is an obstruction to this particular attempted ten-point model,
not a nonexistence claim for all abstract models without equidistant
four-tuples.

# 5. Failed routes and precise remaining obstruction

1. A universal quadratic lower bound for missing apexes D alone:
   false by (11)–(12).
2. Propagating a defect through every component of the size-3 kite
   graph: false by the eight-point planar K₄ example.
3. Diameter/radius extremality: proves that exact equality at
   M=(n−1)/3 is impossible, but the established statement only forces
   a class of size at most 2. It supplies no quadratic defect estimate.
4. Applying this strictness to randomly sampled subsets: (13)
   exhibits quadratic subset defects even when the parent defect is
   zero, so the available subset statement does not amplify.
5. Class-size weights, Cauchy–Schwarz, and the unweighted second
   moments: equality is possible in the explicit abstract metric
   model (19). The unknown extra input is geometric control of the
   cross term in (15), or an independent geometric lower bound on R.
6. Triple uniqueness and pairwise circle intersection counting:
   (18) and the intersection bound permit the abstract homogeneous
   model. They do not express all plane geometry.
7. Replacing the four-point affine blocks by three Petersen color
   graphs on ten vertices: the complete finite search failed as
   recorded in §4.2. This candidate was abandoned.

8. Reflection-direction multiplicities were also considered. If r_{pq}
   counts bases whose two apexes are p,q, then in the homogeneous
   situation its row sum at p is n−1 and its total over unordered
   {p,q} is N/2. Thus the mean over possible axes is 1, which does
   not by itself bound the variance or force many missing bases. No
   further geometric estimate for these multiplicities was obtained.
9. The squared-distance matrix has rank at most 4, since it equals
   u1ᵀ+1uᵀ−2xxᵀ−2yyᵀ with u_i=x_i²+y_i². This additional planar
   constraint was considered, but no inequality converting that rank
   bound and the equality pattern into a lower bound on R was found.

The unproved geometric step is to exclude, quantitatively and
uniformly in n, sets satisfying simultaneously the bounds (7)–(10)
with arbitrarily small ε and bounded B. In particular, a proof of
R≥c n² for some explicit c>0 and explicit onset would finish the
stronger average-based route through (1). No such lemma is claimed.

# 6. Exact checks and their limits

All computation used Node with UV_THREADPOOL_SIZE=1 and
--single-threaded. No SAT/ILP solver, numerical optimization,
floating-point geometry, external data, or probabilistic search was
used. The larger integer-grid and polygon checks were given a
30-second process CPU limit; they completed in milliseconds.
At most two checking processes ran concurrently.

## 6.1 Exhaustive subsets of the 4×4 integer grid

Enumerated all 65,536 subsets of {0,1,2,3}². There are 44 collinear
triples in that grid. Retained exactly the 4,795 subsets of size at
least two avoiding every collinear triple. For each retained subset,
computed all squared distances, class sizes, and apex counts
independently; checked k_b≤2, (2), (3), I=N−D, and (5).
There were zero failures.

| n | retained subsets | minimum M | minimum D+C |
|---|---:|---:|---:|
| 2 | 120 | 1 | 4 |
| 3 | 516 | 2 | 9 |
| 4 | 1278 | 2 | 12 |
| 5 | 1668 | 3 | 22 |
| 6 | 998 | 4 | 30 |
| 7 | 204 | 5 | 45 |
| 8 | 11 | 6 | 58 |

These minima concern only this finite grid, not all planar sets.
All integers in this check are exactly representable by JavaScript
Number; in particular squared distances are at most 18.

## 6.2 Abstract field models

Checked every class and every base for d=1,2,3, using exact F₄
arithmetic represented by binary polynomials modulo x²+x+1.

| d | n | bases | T | M | I | D=C=E |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 6 | 4 | 1 | 12 | 0 |
| 2 | 16 | 120 | 80 | 5 | 240 | 0 |
| 3 | 64 | 2016 | 1344 | 21 | 4032 | 0 |

Every class had size 3 and every base exactly two apexes. These
are checks of the nonplanar model, not Euclidean examples.

## 6.3 Exact polygon incidence checks

For every odd m∈{3,5,…,31}, used the exact class labels: center
distance label 0; between vertices i,j, label min(r,m−r) where
r=j−i modulo m. Section 3.2 proves that these labels express exactly
the equalities of the actual Euclidean distances, without a
floating-point tolerance. Checked all apexes and every formula in
(11)–(12). Zero failures. For example:

| m | n | T | M | D | C | E |
|---|---:|---:|---:|---:|---:|---:|
| 3 | 4 | 7 | 2 | 6 | 3 | 15 |
| 5 | 6 | 16 | 3 | 10 | 8 | 34 |
| 9 | 10 | 46 | 5 | 18 | 30 | 108 |
| 31 | 32 | 497 | 16 | 62 | 437 | 1373 |

## 6.4 Eight-point and Petersen checks

The eight-point example was checked with BigInt coordinates and
squared distances, including all 56 collinearity determinants, the
four exact classes, the six specified apex pairs, and full counts.
A separate determinant pass gave minimum absolute determinant 76734.

The Petersen search was exhaustive over the partial permutations
described in §4.2, with no randomized choices. Zero residual graphs
passed the common-neighbor characterization required of a Petersen
graph.

# 7. Reproduction code

The following code specifies the checks. It can be fed directly to
Node through a quoted shell heredoc; no scratch files are needed.
The geometric examples and identities above have independent proofs;
the exhaustive finite checks are validation and route diagnostics.

~~~javascript
const assert = (ok, msg) => { if (!ok) throw Error(msg); };

function stats(labels) {
  const n = labels.length, N = n*(n-1);
  let T=0, M=0, I=0, D=0, C=0, E=0;
  for (let p=0;p<n;p++) {
    const cls=new Map();
    for(let q=0;q<n;q++) if(q!==p) {
      const key=String(labels[p][q]);
      cls.set(key,(cls.get(key)||0)+1);
    }
    T+=cls.size; M=Math.max(M,cls.size);
    for(const a of cls.values()) {
      I+=a*(a-1)/2;
      C+=(a-2)*(a-3)/2;
      E+=(a-3)**2;
    }
  }
  for(let a=0;a<n;a++) for(let b=a+1;b<n;b++) {
    let k=0;
    for(let p=0;p<n;p++)
      if(p!==a&&p!==b&&labels[p][a]===labels[p][b]) k++;
    assert(k<=2,"apex bound");
    D+=2-k;
  }
  assert(I===N-D && 3*T===N+D+C && E===D+3*C,"identities");
  return {n,T,M,I,D,C,E};
}

// Grid: all subsets; exact Number arithmetic at these magnitudes.
const grid=[];
for(let x=0;x<4;x++) for(let y=0;y<4;y++) grid.push([x,y]);
const gd=grid.map(a=>grid.map(b=>(a[0]-b[0])**2+(a[1]-b[1])**2));
const forbidden=[];
for(let a=0;a<16;a++) for(let b=a+1;b<16;b++)
for(let c=b+1;c<16;c++)
  if((grid[b][0]-grid[a][0])*(grid[c][1]-grid[a][1])===
     (grid[b][1]-grid[a][1])*(grid[c][0]-grid[a][0]))
    forbidden.push((1<<a)|(1<<b)|(1<<c));
assert(forbidden.length===44,"grid collinear triples");
const rows={};
let total=0;
for(let mask=0;mask<65536;mask++) {
  const ids=[];
  for(let i=0;i<16;i++) if(mask&(1<<i)) ids.push(i);
  if(ids.length<2||forbidden.some(b=>(mask&b)===b)) continue;
  const s=stats(ids.map(i=>ids.map(j=>gd[i][j])));
  assert(s.M>=Math.ceil(s.n/3),"planar lower bound");
  rows[s.n]??={count:0,minM:Infinity,minR:Infinity};
  rows[s.n].count++;
  rows[s.n].minM=Math.min(rows[s.n].minM,s.M);
  rows[s.n].minR=Math.min(rows[s.n].minR,s.D+s.C);
  total++;
}
assert(total===4795,"grid count");
console.log("grid",rows);

// F4 arithmetic: elements 0,1,x,x+1 encoded by 0,1,2,3.
function mul4(a,b) {
  let z=0;
  for(let k=0;k<2;k++) if((b>>k)&1) z^=a<<k;
  if(z&4) z^=7;
  return z;
}
function scale4(v,c,d) {
  let z=0;
  for(let i=0;i<d;i++)
    z|=mul4((v>>(2*i))&3,c)<<(2*i);
  return z;
}
for(let d=1;d<=3;d++) {
  const n=4**d, dir=Array(n).fill(-1);
  for(let v=1;v<n;v++)
    dir[v]=Math.min(v,scale4(v,2,d),scale4(v,3,d));
  const s=stats(Array.from({length:n},(_,p)=>
    Array.from({length:n},(_,q)=>dir[p^q])));
  assert(s.D===0&&s.C===0&&s.E===0,"field homogeneous");
  assert(s.M===(n-1)/3&&s.T===n*(n-1)/3,"field counts");
  console.log("field",d,s);
}

// Odd polygon plus center: labels justified analytically in §3.2.
for(let m=3;m<=31;m+=2) {
  const n=m+1, inv2=(m+1)/2;
  const label=(p,q)=>{
    if(p===q) return -1;
    if(p===m||q===m) return 0;
    const r=(q-p+m)%m;
    return Math.min(r,m-r);
  };
  const lab=Array.from({length:n},(_,p)=>
    Array.from({length:n},(_,q)=>label(p,q)));
  const s=stats(lab);
  for(let a=0;a<n;a++) for(let b=a+1;b<n;b++) {
    const actual=[];
    for(let p=0;p<n;p++)
      if(p!==a&&p!==b&&lab[p][a]===lab[p][b]) actual.push(p);
    const expected=b===m?[]:[inv2*(a+b)%m,m];
    assert(actual.length===expected.length&&
      expected.every(p=>actual.includes(p)),"polygon apexes");
  }
  assert(s.T===1+m*(m+1)/2&&s.I===m*(m-1),"polygon T,I");
  assert(s.M===(m+1)/2&&s.D===2*m,"polygon M,D");
  assert(s.C===(m*m-3*m+6)/2,"polygon C");
  assert(s.E===(3*m*m-5*m+18)/2,"polygon E");
  console.log("polygon",m,s);
}

// All geometry in this example is BigInt arithmetic.
const pts=[
  [0n,0n],[1008n,0n],[252n,756n],[1260n,1512n],
  [504n,252n],[504n,861n],[1722n,-154n],[1026n,774n]
];
const ed=pts.map(a=>pts.map(b=>
  (a[0]-b[0])**2n+(a[1]-b[1])**2n));
let minimum=null, detCount=0;
for(let i=0;i<8;i++) for(let j=i+1;j<8;j++)
for(let k=j+1;k<8;k++) {
  let z=(pts[j][0]-pts[i][0])*(pts[k][1]-pts[i][1])-
        (pts[j][1]-pts[i][1])*(pts[k][0]-pts[i][0]);
  if(z<0n) z=-z;
  assert(z>0n,"no three collinear");
  if(minimum===null||z<minimum) minimum=z;
  detCount++;
}
assert(detCount===56&&minimum===76734n,"determinants");
const faces=[[0,1,2],[0,1,3],[0,2,3],[1,2,3]];
for(let i=0;i<4;i++) {
  const actual=[];
  for(let j=0;j<8;j++)
    if(ed[i+4][j]===ed[i+4][faces[i][0]]) actual.push(j);
  assert(String(actual)===String(faces[i]),"circumcenter class");
}
const es=stats(ed);
assert(es.T===48&&es.M===7&&es.I===12&&
       es.D===44&&es.C===44&&es.E===176,"eight-point counts");
console.log("eight-point",es,String(minimum));

// Failed Petersen decomposition search.
const pairs=[];
for(let i=0;i<5;i++) for(let j=i+1;j<5;j++) pairs.push([i,j]);
const A=pairs.map((p,i)=>pairs.map((q,j)=>
  i!==j&&!p.some(x=>q.includes(x))?1:0));
let leaves=0,nodes=0,found=null;
const perm=Array(10).fill(-1),used=Array(10).fill(false);
perm[0]=0;used[0]=true;
function dfs(k) {
  nodes++;
  if(found) return;
  if(k===10) {
    leaves++;
    const B=Array.from({length:10},()=>Array(10).fill(0));
    for(let i=0;i<10;i++) for(let j=0;j<10;j++)
      B[perm[i]][perm[j]]=A[i][j];
    const C=A.map((row,i)=>row.map((v,j)=>
      i===j?0:1-v-B[i][j]));
    for(let i=0;i<10;i++) for(let j=i+1;j<10;j++) {
      let cn=0;
      for(let t=0;t<10;t++) cn+=C[i][t]*C[j][t];
      if(cn!==(C[i][j]?0:1)) return;
    }
    found=[...perm];
    return;
  }
  for(let x=0;x<10;x++) {
    if(used[x]) continue;
    let ok=true;
    for(let i=0;i<k;i++)
      if(A[k][i]&&A[x][perm[i]]) {ok=false;break;}
    if(!ok) continue;
    perm[k]=x;used[x]=true;
    dfs(k+1);
    used[x]=false;perm[k]=-1;
  }
}
dfs(1);
assert(nodes===13810&&leaves===288&&found===null,"Petersen search");
console.log("Petersen",{nodes,leaves,found});
~~~

# 8. Cost and verification record

The five original checking processes reported the following CPU usage
from process.cpuUsage(), including both user and system CPU:

| Check | CPU seconds |
|---|---:|
| Petersen search | 0.009590 |
| F₄ models | 0.024194 |
| 4×4 grid subsets | 0.019110 |
| eight-point coordinates and classes | 0.000305 |
| polygon labels and separate determinant pass | 0.023945 |
| Total original mathematical checks | 0.077144 |

These are measured CPU costs, not wall-time estimates. No solver was
used and no expensive search was run. The continuation's wall-clock
start was 2026-10-09 14:18 UTC. Prior interrupted runs' compute costs
were not available from the supplied history; they are not fabricated
or included in this measured total. Coordination and file-writing
process CPU is not included in the mathematical-check total.

The full reproduction block was extracted from this report and run
independently after writing it. All assertions passed, reproducing all
21 output groups. The rerun used 0.074134 CPU seconds (0.072206 user,
0.001928 system), with measured wall time 74 milliseconds. The combined
measured mathematical-check CPU cost was therefore 0.151278 seconds.
The rerun completed at 2026-10-09 14:34 UTC, approximately 16 minutes
after this continuation began. The written algebra and geometric
arguments were rechecked against their definitions before submission.
The proofs of (2)–(5), the explicit stability constants in (8)–(10),
and the two obstruction constructions are the substantive deliverable.
No target HIT is claimed.

Next mathematical action, if a further probe is commissioned: obtain
a genuinely quantitative Euclidean restriction on the coupled apex
classes in (15), or on the center/point relations in the almost
3-regular graph (10). This probe itself is complete with a PARTIAL
outcome.
