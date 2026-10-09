PARTIAL — For every finite penny graph G with n vertices and s vertices of degree 6, proved α(G) ≥ max{⌈n/4⌉, ⌈(n+3s)/12⌉}. For n>0, s ≥ 3n/4 implies α(G) ≥ 13n/48 > 6n/23. No constant c > 6/23 has been proved for all penny graphs.

Clean-room probe, AUT-25, 2026-10-09. Author: attacker-2.

This report treats both requested routes: local geometric rigidity and boundary accounting, and weighted greedy/Caro–Wei certificates. The conditional statement is not a solution of the target. No novelty claim is made for the partial lemmas.

The prescribed report was absent at the start of this continuation. The supplied history mentioned the conditional bound 13n/48 but contained no proof. The argument below was reconstructed and checked directly. No other file in /work, repository material, papers, web pages, or other agents' files was read. Only the prescribed report is written under /work. Control-plane skill instructions were read outside /work for task administration.

**Definitions and exact statement.**

Let P be a finite set of n distinct points in the Euclidean plane with |x−y| ≥ 1 whenever x ≠ y. Its penny graph G has vertex set P, with xy an edge exactly when |x−y| = 1. Let d(v) be its degree, S = {v : d(v)=6}, s = |S|, and T = P \ S. The independence number α(G) is the maximum cardinality of a set containing no adjacent pair.

For nonnegative vertex weights w(v), write w(A) = ∑_{v∈A} w(v), and let α_w(G) be the maximum weight of an independent set.

There are canonically determined sets T_0,T_1,T_2 partitioning T, defined below using the rigid lattice components of S, for which

    α_w(G) ≥ w(S)/3 + w(T_0)/4 + w(T_1)/6 + w(T_2)/12.       (1)

In particular, writing t_i = |T_i|,

    α(G) ≥ ⌈(4s+3t_0+2t_1+t_2)/12⌉
         ≥ ⌈(n+3s)/12⌉.                                    (2)

Also α_w(G) ≥ w(P)/4. All these assertions hold for every n ≥ 0; no asymptotic qualification is involved.

If n>0 and s ≥ 3n/4, then

    (n+3s)/12 ≥ (n+9n/4)/12 = 13n/48,

and

    13/48 − 6/23 = (299−288)/1104 = 11/1104 > 0.             (3)

More generally the unrounded expression (n+3s)/12 exceeds 6n/23 exactly when 69s > 49n. The unrounded maximum of the two bounds in the status line is just n/4 when s ≤ 2n/3. Integer rounding supplies no uniform linear improvement as n grows.

**1. Elementary geometric facts and the four-color baseline.**

If u and v are unit neighbors of x, and their smaller angular separation at x is θ ∈ [0,π], then

    |u−v|² = 2−2 cos θ.

Since |u−v| ≥ 1, cos θ ≤ 1/2, hence θ ≥ π/3. In particular each cyclic gap between successive unit neighbors is at least π/3. Summing the gaps gives d(x) ≤ 6. If d(x)=6, all six gaps equal π/3: the neighbors form a regular unit hexagon.

Every nonempty induced subgraph of G has a vertex of degree at most 3. To see this, choose a linear functional whose values on its vertex set are all different; only finitely many directions are forbidden. At its unique minimum vertex x all other vertices lie in one strict half-plane through x. Thus all directions toward unit neighbors of x lie in an open angular interval of length π. Four such neighbors would have three successive angular gaps, each at least π/3, whose sum is at least π. Their directions cannot fit in this open interval. Therefore there are at most three neighbors.

Repeatedly remove such a vertex and put vertices back in reverse order. A vertex being put back has at most three already colored neighbors, so one of four colors is available. This proves four-colorability directly, without invoking the Four Color Theorem. Each color class is independent, and their weights sum to w(P). At least one has weight at least w(P)/4. The same conclusion holds for every induced subgraph, including an empty one.

**2. Degree-6 vertices linked through a common neighbor have the same lattice.**

Let R be rotation through π/3. A degree-6 vertex a lies at the center of a regular hexagon. Its star determines a triangular lattice

    L_a = a + Z u + Z R u,

where u is any vector from a to a neighbor. Choosing another of the six neighbors gives the same lattice: rotation R takes the basis (u,Ru) to (Ru,Ru−u), and translations by lattice vectors preserve the lattice.

If degree-6 vertices a,b are adjacent, their unit vector b−a fixes the same six directions for both stars, and b ∈ L_a. Hence L_a=L_b.

Now suppose distinct degree-6 vertices a,b have a common neighbor x. If x has degree 6, apply the preceding adjacency argument twice. Otherwise d(x)≤5.

The star centered at a forces three neighbors of x with vectors, measured from x,

    a−x, R(a−x), R^−1(a−x).                                 (4)

For example the point x+R(a−x) is a neighbor of a because

    x+R(a−x)−a = R^−1(x−a).

The vector on the right is one of a's six unit neighbor vectors. The analogous identity gives the other point. All three points in (4) are at distance 1 from x, so they really belong to N(x).

The star centered at b likewise forces the triple with vectors b−x, R(b−x), R^−1(b−x). Two three-element subsets of the at-most-five-element set N(x) must intersect. Thus for some integers i,j ∈ {−1,0,1},

    R^i(a−x) = R^j(b−x).

Consequently b−x is obtained from a−x by a multiple of π/3. Both lattices contain x and have the same six directions, so L_a=L_b.

Define an auxiliary graph H on S by joining two distinct vertices whenever their distance in the graph G is at most 2. The preceding arguments imply that each connected component C of H has a single triangular lattice L_C containing C and every neighbor in G of every vertex in C.

There are no G-edges between different components of H. Moreover, if x∈T has any neighbor in S, then all its neighbors in S belong to one component of H, since any two share the neighbor x. This explains why using just the connected components of G[S] would miss a necessary compatibility condition.

**3. Three-coloring each rigid lattice and proving (1).**

Take a unit vector u and v=Ru as a basis of L_C, with any lattice point as origin. For integer coordinates (a,b), define

    χ_C(a u+b v) = a+2b mod 3.

The squared length of a u+b v is a²+ab+b². This equals 1 only for

    (a,b) ∈ {(1,0),(−1,0),(0,1),(0,−1),(1,−1),(−1,1)}.

Indeed a²+ab+b² = (a+b/2)²+3b²/4 implies |b|≤1, after which these possibilities follow by substitution. The six corresponding changes in a+2b are nonzero modulo 3. Thus χ_C is a proper three-coloring of all unit edges of L_C.

For x∈T with neighbors in S, let q(x) be the number of different χ_C colors among those neighbors, using their unique component C. Because x itself lies in L_C, no neighbor has color χ_C(x). Therefore q(x)∈{1,2}. If x has no S-neighbor, set q(x)=0. Changing the origin adds a constant to χ_C; rotating the permitted basis once through π/3 negates χ_C modulo 3. Repeating these operations only permutes the three color classes, so q(x) is unchanged. Define T_i={x∈T:q(x)=i}.

Independently for each component C, choose a uniform color k_C∈{0,1,2}. Select

    I = ⋃_C {v∈C : χ_C(v)=k_C}.

There is no edge inside a selected color class or between distinct components, so I is independent. Each vertex of S is selected with probability 1/3.

Let U={x∈T : N(x)∩I=∅}. Every independent set in G[U] can be joined to I. By the four-color argument,

    α_w(G) ≥ w(I) + w(U)/4                                 (5)

for every choice of the colors. A vertex x∈T_0 always survives. A vertex x∈T with an S-neighbor survives precisely when the chosen color of its S-component is not one of the q(x) forbidden colors. Thus

    Pr(x∈U)=1−q(x)/3.

No independence between different survival events is needed; linearity of expectation suffices. Averaging (5) gives

    α_w(G)
      ≥ w(S)/3 + (1/4) ∑_{x∈T} w(x)(1−q(x)/3)
      = w(S)/3 + w(T_0)/4 + w(T_1)/6 + w(T_2)/12,

which proves (1). For unit weights this is the first inequality of (2). Since 3t_0+2t_1+t_2 ≥ t_0+t_1+t_2 = n−s, the second follows. Together with the baseline in paragraph 1 this proves the status-line theorem.

This calculation also identifies the boundary loss exactly. Before rounding, (1) with unit weights is

    n/4 + [s−t_1−2t_2]/12.                                  (6)

Replacing t_1+2t_2 by its upper bound 2(n−s) gives (n+3s)/12. No unquantified boundary or o(1) term is hidden in this step.

**4. An explicit family with no degree-6 vertices and almost all degrees 5.**

Fix integers W≥2 and even H≥2. For 0≤i<W and 0≤j<H let

    a_j=⌈j/2⌉,       b_j=⌊j/2⌋,
    p_(i,j)=(i+a_j/2, b_j+(√3/2)a_j).

Call its penny graph F_(W,H). There are WH points.

Rows have horizontal spacing 1. From row j to j+1:

- if j is even, the horizontal displacement is 1/2 and vertical displacement is √3/2;
- if j is odd, the horizontal displacement is 0 and vertical displacement is 1.

For a triangular band the squared distance between indices i below and k above is (k−i+1/2)²+3/4, which is at least 1, with equality precisely when k=i or k=i−1. For a square band it is (k−i)²+1, with equality precisely when k=i.

Any two rows separated by at least two steps have vertical separation at least 1+√3/2>1. Within one row, distinct points have integer distance at least 1. These cases exhaust all pairs and prove the packing condition and the claimed contact list.

Each interior row has one triangular band on one side and one square band on the other. For 1≤i≤W−2 and 1≤j≤H−2, the degree is therefore

    2 horizontal + 2 triangular-band + 1 square-band = 5.

An endpoint of an interior row has degree 3 or 4. On the top or bottom row, non-corner vertices have degree 4; the four corners comprise two of degree 2 and two of degree 3. Hence, exactly,

    n_2=2,
    n_3=H,
    n_4=2W+H−6,
    n_5=(W−2)(H−2),
    n_6=0,                                                  (7)
    |E(F_(W,H))|=(5WH−2W−3H)/2.

These formulas include W=2 or H=2. The sum of the degree counts is WH and the displayed edge count is half their degree sum.

In particular, for even M≥2,

    n=M²,   n_6=0,
    n_5/n=1−4/M+4/M²,
    #{v:d(v)≤4}=4M−4.                                      (8)

Thus no positive universal fraction of degree-6 vertices, or of vertices of degree at most 4 in their absence, can be inferred from the packing hypothesis.

The example is not close to disproving the target. Color row 2k by 2i mod 3 and row 2k+1 by 2i+1 mod 3. Horizontal edges change color by 2; the two triangular contacts change it by 1 or −1; square contacts change it by −1. This is a proper three-coloring, so α(F_(W,H))≥WH/3.

If W is divisible by 3, each two-row triangular band, ordered

    p_(0,2k), p_(0,2k+1), p_(1,2k), p_(1,2k+1), …,

has all edges between positions one or two apart. Every three consecutive positions form a triangle. Since 2W is divisible by 3, partitioning this sequence into triples partitions that band into triangles. The H/2 bands are vertex-disjoint and cover all vertices. Any independent set therefore contains at most WH/3 vertices. Consequently

    α(F_(W,H))=WH/3 whenever 3 divides W and H is even.       (9)

The degree-5 interior has three incident triangular faces and two incident squares. Its usual combinatorial curvature is exactly

    1−5/2+3(1/3)+2(1/4)=0.

This supplies a local zero-curvature pattern for the discharging route: triangles, squares, contact angles, and degree 5 alone do not force positive-density exceptional vertices. Formula (8) gives the precise finite boundary count instead of an asymptotic assertion.

**5. Weighted Caro–Wei route, and the scope of its obstruction.**

For any finite graph, assign independent exponential random clocks with positive rates λ_v. Select v if its clock is earlier than every neighbor's clock. Adjacent vertices cannot both be selected. The probability that v is selected is

    ∫_0^∞ λ_v exp(−λ_v t) ∏_{u∈N(v)} exp(−λ_u t) dt
      = λ_v/[λ_v+∑_{u∈N(v)} λ_u].

Thus, for all nonnegative weights w,

    α_w(G) ≥ ∑_v w(v) λ_v/[λ_v+∑_{u∈N(v)} λ_u].             (10)

With all rates equal, the right side is ∑_v w(v)/(d(v)+1), the usual weighted Caro–Wei certificate. This is a one-pass local-minimum argument. A sequential greedy algorithm may select additional vertices, so failure of this certificate is not a claimed failure of every greedy algorithm.

For F_(W,H), unit weights and the exact degree counts (7) give

    ∑_v 1/(d(v)+1)
      = 2/3 + H/4 + (2W+H−6)/5 + (W−2)(H−2)/6
      = WH/6 + W/15 + 7H/60 + 2/15.                         (11)

For W=H=M its ratio to n is exactly

    1/6 + 11/(60M) + 2/(15M²).

For every even M≥4 this is at most its value at M=4,

    1/6+11/240+2/240 = 53/240 < 1/4.

The two correction terms decrease because M and M² increase. This explicitly rules out extracting the target from the uniform-rate certificate on this family.

A stronger obstruction allows arbitrary positive degree-only rates, λ_v=f(d(v)). The seven positive values of f may depend on W,H. Assume W,H≥4, with H even. There are at least

    K=(W−4)(H−4)

vertices with 2≤i≤W−3 and 2≤j≤H−3. Every such vertex and all five of its neighbors have degree 5, by the contact list above. Its term in (10) with unit weights is exactly

    f(5)/(6f(5))=1/6,

regardless of f. Every other term is at most 1 because all rates are positive. Therefore the entire degree-only certificate C_f satisfies

    C_f ≤ K/6+(WH−K)
        = WH/6 + (5/6)[WH−(W−4)(H−4)]
        = WH/6 + (10/3)(W+H−4).                            (12)

For even M≥72,

    C_f/M² ≤ 1/6 + 20/(3M) − 40/(3M²)
             < 1/6 + 20/(3·72)
             = 7/27 < 6/23,

where 6/23−7/27=(162−161)/621=1/621. For even M≥80, the same estimate gives C_f/M²<1/4 because 20/(3M)≤1/12 and the final correction is strictly negative.

These bounds are uniform over all positive degree-only choices, including choices depending on the size of the graph. Any averaging of such certificates obeys the same upper bound.

For M divisible by 6 and M≥84, the strip has actual independence number n/3 by (9), while s=0 and t_0=n. Consequently the geometric certificate (1) gives exactly n/4, its simplified version gives n/12, the four-color baseline gives n/4, and every certificate in (12) is below n/4. Taking the maximum or convex combinations of these certificates cannot establish the requested c>6/23. This is an obstruction to the explored estimates, not a counterexample to the conjectured inequality.

There is deliberately no claim that arbitrary vertex-dependent rates cannot work. In fact, for any graph let A be a maximum independent set, use rate M on A and rate 1 outside A, and let M tend to infinity. A vertex of A has selection probability M/(M+d(v)), tending to 1. Since a maximum independent set is maximal, every vertex outside A has a neighbor in A; its selection probability is at most 1/(M+1), tending to 0. The sum in (10) tends to |A|. Each sum is at most α(G), since it is the expected size of an independent set. Thus the supremum of (10) over unrestricted rates is exactly α(G). The missing ingredient is a justified geometric choice of rates or a stronger iterative selection argument, not an impossibility theorem about all weights.

**6. Routes attempted and their exact limitations.**

1. Extreme-vertex deletion and four-coloring. This gives α≥n/4. On its own its coefficient is below 6/23, since 6/23−1/4=1/92.

2. Use the triangular structure of degree-6 vertices. This succeeds only in the quantitative form (1). Discarding the rest gives merely α≥s/3, which cannot give a universal bound when s=0. The improved boundary accounting gives the status-line partial theorem, but (8) shows its high-s hypothesis is not universal.

3. Choose a random lattice color on the complete degree-6 stars, including their neighboring vertices, and unite the choices across components. This proposed improvement has a concrete conflict. Take the union of the seven-point hexagonal stars with centers 0 and 3u, where u is a unit lattice vector. Their two degree-6 centers lie in different components of H. The halo vertices u and 2u are adjacent, and suitable independent color choices in the two stars select both, with probability 1/9. The union is then not independent. The residual four-color step in (5) repairs this issue, at the explicit cost appearing in (6).

4. Treat degree 5 as imposing the same local rigidity as degree 6. This is false even locally: the origin and five points on the unit circle at angles 2πk/5 form a penny graph whose center has degree 5 and no triangular face. Its neighbors' consecutive distances are 2 sin(π/5)>1, since π/5>π/6 and sine is increasing on [0,π/2]. All other neighbor distances are larger. Hence degree 5 does not even force a triangle or the π/3 directions. The separate dense degree-5 obstruction is the exact triangle-square family in paragraph 4.

5. Force many low-degree or rigid vertices by angle/face discharging alone. The interior configuration with degree 5, three triangles, and two squares has curvature zero. Equations (7)–(8) realize arbitrarily large finite packings with that interior and only 4M−4 non-degree-5 vertices. This rules out the positive-density exceptional-vertex assertion needed by that attempted route. It does not rule out a more sophisticated discharging proof using reducible configurations.

6. Uniform-rate weighted Caro–Wei. Formula (11) gives a certificate tending to n/6 on the same dense degree-5 family; the error is exactly W/15+7H/60+2/15.

7. Optimize positive rates using only the degree. The quantitative upper bound (12) defeats all these choices on the strip family, with the explicit onsets M≥72 for falling below 6n/23 and M≥80 for falling below n/4.

8. Use unrestricted geometric weights, a sequential greedy improvement, or sharper coloring of the surviving boundary. No valid universal inequality completing these steps was obtained. Unrestricted-rate optimization can already encode a maximum independent set, as proved above, so asserting that suitable weights exist without constructing and estimating them would be circular. The cross-star example in item 3 prevents the simplest boundary-color shortcut.

The report does not reprove or invoke the brief's known 8n/31 theorem or its unrefereed numerical claims. Even accepting 8n/31 as an input would not close the missing universal case: 6/23−8/31=2/713>0. No attempted calculation yielded a universal coefficient above 6/23.

**7. Exact small checks performed.**

Two Node.js v22.23.1 scripts performed exact finite calculations. Neither sampled random point sets nor used tolerance-based contact decisions. No SAT/ILP solver or library solver was used.

For the first script, points were represented by integer triples (X,A,B), meaning

    (x,y)=(X/2,(A+B√3)/2).

For a pair, four times its squared distance is the exact expression

    U+V√3,
    U=(ΔX)²+(ΔA)²+3(ΔB)²,    V=2ΔAΔB.

Contact is exactly U=4,V=0. To test distance at least 1, the sign of (U−4)+V√3 was determined by signs first and, for opposite signs, by comparing (U−4)² with 3V². Irrationality of √3 excludes a nonzero integer equality in the latter comparison. All integer intermediates were far below 2^53, so the integer operations in JavaScript Number were exact.

The first script checked every pair in each of these 27 configurations:

- Triangular-lattice rhombi R_m, 1≤m≤6: points (i+j/2,√3 j/2), 0≤i,j<m.
- Hexagonal lattice patches B_r, r=0,1,2: points i u+j v with max{|i|,|j|,|i+j|}≤r, where v=Ru.
- The 18 strip graphs F_(W,H) with 1≤W≤6 and H∈{2,4,6}. For W=1 the same coordinate definition applies and gives a path; the degree-count formula (7) was only claimed for W≥2.

It asserted that no pair distance was below 1, constructed every contact edge, computed all degrees, and computed α exactly by the recurrence

    A(∅)=0,
    A(U)=max{A(U\{v}), 1+A(U\N[v])}.

For efficiency, v was chosen with maximum degree in the current induced graph, results were memoized, and an edgeless U returned |U|. Vertex sets were BigInt masks, and N[v] was intersected with U by the mask operations. The recurrence exhausts the two possibilities that an independent set excludes or includes v, so it is exact. Every computed result was checked against 4α≥n and 12α≥n+3s.

Results for the rhombi and hexagonal patches:

| Object | n | Edges | s=n_6 | Exact α |
|---|---:|---:|---:|---:|
| R_1 | 1 | 0 | 0 | 1 |
| R_2 | 4 | 5 | 0 | 2 |
| R_3 | 9 | 16 | 1 | 4 |
| R_4 | 16 | 33 | 4 | 6 |
| R_5 | 25 | 56 | 9 | 9 |
| R_6 | 36 | 85 | 16 | 12 |
| B_0 | 1 | 0 | 0 | 1 |
| B_1 | 7 | 12 | 1 | 3 |
| B_2 | 19 | 42 | 7 | 7 |

For the strips, each cell contains (n, number of edges, exact α); all have s=0:

| W | H=2 | H=4 | H=6 |
|---|---|---|---|
| 1 | (2,1,1) | (4,3,2) | (6,5,3) |
| 2 | (4,5,2) | (8,12,4) | (12,19,6) |
| 3 | (6,9,2) | (12,21,4) | (18,33,6) |
| 4 | (8,13,3) | (16,30,6) | (24,47,9) |
| 5 | (10,17,4) | (20,39,8) | (30,61,12) |
| 6 | (12,21,4) | (24,48,8) | (36,75,12) |

For additional degree-count audit examples, F_(3,4) had (n_2,n_3,n_4,n_5)=(2,4,4,2), and F_(6,6) had (2,6,12,16), in agreement with (7). The first script made 70,111 recursive calls in total; its largest individual memo table had 15,740 states.

The second script checked four star unions. Here centers are specified by integer coordinates in the basis (u,v), and each center contributes itself and its six lattice neighbors. Duplicate vertices are merged. The contact test was the exact quadratic form a²+ab+b²=1. The script rebuilt degrees, the components of H, the color counts q(x), and the exact independence number using the same include/exclude recurrence (with the first available vertex). It asserted 12α≥4s+3t_0+2t_1+t_2.

| Centers | n | s | H components | (t_0,t_1,t_2) | Numerator 4s+3t_0+2t_1+t_2 | Exact α |
|---|---:|---:|---:|---|---:|---:|
| (0,0),(1,0) | 10 | 2 | 1 | (0,6,2) | 22 | 4 |
| (0,0),(1,1) | 12 | 2 | 1 | (0,10,0) | 28 | 5 |
| (1,0),(0,1),(−1,1) | 13 | 3 | 1 | (0,7,3) | 29 | 5 |
| (0,0),(3,0) | 14 | 2 | 2 | (0,12,0) | 32 | 6 |

The second row specifically tests two nonadjacent degree-6 vertices coupled through common neighbors. The last row is the failed halo-union example from paragraph 6. These checks support the bookkeeping on the stated finite objects; they are not an exhaustive classification of penny graphs or a replacement for the proof.

**8. Cost, audit, and remaining mathematical step.**

The two arithmetic scripts used one JavaScript computation thread, were run sequentially, and used Node's V8 worker pool size 1; no computational worker threads or solvers were launched. Their measured process CPU use during the checking routines was:

- First script: 55,319 microseconds user + 2,022 microseconds system.
- Second script: 448 microseconds user + 0 microseconds system.
- Total measured checking CPU: 57,789 microseconds = 0.057789 seconds.

This excludes interpreter startup, file writing, model reasoning, and control-plane administration. The tool reported each checking command complete in about 0.1 seconds. No sustained computation or paid resource was used. The interrupted earlier run's total cost is not available in the supplied history; no claim about its exact usage is made. The current continuation uses far less than the one-CPU-hour allowance.

The proof was independently rechecked from its written chain: common-neighbor triple intersection establishes lattice compatibility; all S-neighbors of a T-vertex are in one component and use at most two colors; the survivor probability is exactly 1−q/3; the residual induced penny graph is four-colorable; averaging gives (1); minimizing the T coefficients gives (2); substitution gives (3). All inequalities and asymptotic-looking boundary effects in this report have explicit finite formulas. No o(·) terms are used.

Remaining target: prove α(G)≥c n for every finite penny graph with an explicit fixed c>6/23. The missing step is a selection or reducibility estimate that also handles extensive degree-5 regions and interactions between rigid patches. Equations (8) and (12) explain why the two simplest density/degree-weight closures do not supply that step. This bounded probe is complete as PARTIAL; it does not claim the universal target or schedule further work.
