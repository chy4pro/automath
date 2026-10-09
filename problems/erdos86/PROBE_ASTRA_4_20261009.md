PARTIAL — A self-contained proof gives π₄ ≤ 4^(-1/3). An independently checked exhaustive 4-cube certificate strengthens this to π₄ ≤ r = 0.625816818958… , where r³ + 6r − 4 = 0, with the explicit finite bound e(G)/(n2^(n−1)) ≤ r + 3/n for every C₄-free G ⊆ Q_n and n ≥ 4. The requested bound below 0.60318 is OPEN.

# Scope and provenance

This is the clean-room deliverable for AUT-23, round 4. No mathematical repository files, other agents' files, papers, or web sources were read. The brief, the supplied continuation comment, standard mathematics, and computations derived here were used. The designated report did not already exist. Paperclip skill documentation was read only for task administration.

The continuation comment's cubic bound was re-derived below; it was not accepted on authority. Both required routes were worked. The stronger partial bound depends on a finite exhaustive certificate, not a hand classification of 4-cubes. It does not improve either numerical bound stated in the brief. No claim of novelty is made.

All graphs are spanning subgraphs, with isolated vertices included. Q_n has vertex set {0,1}^n, adjacency given by a change in exactly one coordinate, and n2^(n−1) edges. Write d(v) for graph degree and p=e(G)/(n2^(n−1)). All limits and error terms below are explicit; no unspecified o(1) is used.

# 1. Averaging and a fully hand-proved bound

A coordinate k-face is obtained by selecting k free coordinates and fixing the others. There are 2^(n−k) binom(n,k) such faces. Each edge belongs to binom(n−1,k−1) of them.

Consequently the average edge density of the restrictions to k-faces equals p. This proves that a_n=ex(Q_n,C₄)/(n2^(n−1)) is nonincreasing: every k-face is C₄-free and hence has density at most a_k. Since a_n≥0, its limit π₄ exists.

Call a vertex of a k-cube full when its degree within the restricted graph is k. Two full vertices at distance two force all four edges of their common square, which is prohibited. In Q₃, any two distinct vertices of the same parity have distance two. Thus at most one full vertex occurs in each parity class, and every C₄-free Q₃ has at most two full vertices.

Counting full-vertex/3-face incidences gives, for n≥3,

    Σ_v binom(d(v),3) ≤ 2·2^(n−3) binom(n,3),

and therefore

    E_v (d(v))_3 ≤ (n)_3/4,

where (a)_k=a(a−1)…(a−k+1), and the expectation is over all 2^n vertices. For an integer d≥0,

    (d)_3 ≥ ((d−2)_+)³.

For d=0,1,2 both sides are zero; for d≥3 every factor on the left is at least d−2. The function x↦((x−2)_+)³ is convex, so Jensen gives

    ((np−2)_+)³ ≤ (n)_3/4.

It follows that

    p ≤ 2/n + ((n)_3/(4n³))^(1/3) ≤ 4^(−1/3)+2/n.

Thus π₄≤4^(−1/3)=0.629960524947… . This part does not rely on enumeration.

# 2. A finite 4-cube certificate

For a C₄-free H⊆Q₄, let n_i be its number of degree-i vertices, e its number of edges, and T_k=Σ_v binom(d_H(v),k).

The exhaustive certificate below establishes

    n_1+n_2 ≥ 3n_4.                                      (1)

Its equivalent forms are

    T_2+T_4 ≤ 2e,                                        (2)
    T_3+n_0 ≤ 16.                                        (3)

Indeed T_2+T_4−2e=−n_1−n_2+3n_4, by evaluating binom(i,2)+binom(i,4)−i for i=0,…,4. Also T_3=n_3+4n_4 and Σ_i n_i=16, so (3) is exactly (1).

There are at most four full vertices: within either parity class, any distinct full pair must be antipodal, since the other possible nonzero distance is two. A parity class therefore contains at most two full vertices.

If there is no full vertex, (1) is immediate. Otherwise translate a full vertex to 0000. Its four incident edges are fixed present. Each of the six weight-two vertices has two possible edges to weight-one vertices; at most one can be present, or a square through 0000 results. Each gives exactly three choices: neither, the first, or the second. The remaining 16 edges are unconstrained at this preliminary stage. We therefore examine exactly

    3^6 · 2^16 = 47,775,744

distinct candidates. Every C₄-free graph with 0000 full occurs once. We reject precisely candidates containing a square, then compute degrees directly.

Every simple 4-cycle of a cube is a coordinate square: every coordinate in a closed walk is flipped an even number of times; a simple walk of length four must use two coordinates twice, alternately. Thus checking the 24 coordinate squares is sufficient.

The exact results were:

| Number f of full vertices | Valid graphs with 0000 full | Minimum n_1+n_2 |
|---:|---:|---:|
| 1 | 19,975,328 | 4 |
| 2 | 4,877,691 | 6 |
| 3 | 147,744 | 9 |
| 4 | 1,296 | 12 |

Total valid graphs: 25,002,059. Violations of (1): zero. This table proves (1) by the exhaustive partition just described. Appendix A is the complete independent verifier, using only exact 32-bit operations and exactly represented integer counts. The table is a computational certificate; no unproved structural classification is being substituted for it.

A separate enumeration of all labelled C₄-free Q₄ subgraphs, using pairs of Q₃ layers and an independent vertical set, also verified (1). Its details and executable code are in Section 6 and Appendix B.

# 3. Averaging the certificate: explicit bound

Fix n≥4 and a C₄-free G⊆Q_n. For a uniform random vertex v define

    T=d(v)/n,
    q_k=E_v [(d(v))_k/(n)_k].

For a uniform random 4-face F, double counting at a uniformly chosen vertex of F gives

    E_F Σ_{v∈F} binom(d_F(v),k) = 16 binom(4,k) q_k.

To see this, at a fixed vertex choose four directions uniformly. Each present k-subset of incident directions is contained in that choice with probability binom(n−k,4−k)/binom(n,4)=binom(4,k)/binom(n,k). Averaging over vertices gives the identity.

Applying (2) to each F yields

    96q_2+16q_4 ≤ 64p,
    6q_2+q_4 ≤ 4p.                                      (4)

Here E_F Σ_v d_F(v)=16·4p=64p.

For k≤n and a fixed degree d, sampling k directions independently with replacement has probability (d/n)^k of all being present. Conditional on all sampled directions being distinct, its probability is (d)_k/(n)_k. The probability of a repetition is at most binom(k,2)/n by the union bound over pairs of draws. Writing the unconditional probability as the mixture of the two conditional probabilities shows

    (d)_k/(n)_k ≥ (d/n)^k − binom(k,2)/n.                 (5)

This also covers d<k; the falling-factorial ratio is then zero.

Using (5) for k=2,4 in (4), and Jensen for the convex functions t² and t⁴ on [0,1], gives

    6E T²+E T⁴ ≤ 4p+12/n,
    p⁴+6p²−4p ≤ 12/n.                                  (6)

Let r be the unique positive zero of r³+6r−4. The cubic is strictly increasing, has value −4 at 0 and positive value at 2/3. Hence 0<r<2/3. Put g(t)=t⁴+6t²−4t. Then g(r)=0,

    g'(r)=4r³+12r−4=12(1−r)>4,
    g''(t)=12t²+12>0.

For p≥r, the fundamental theorem of calculus gives g(p)≥4(p−r). Combining with (6), and treating p<r trivially, proves for every n≥4:

    e(G)/(n2^(n−1)) ≤ r+3/n.                             (7)

Passing to the already established limit yields π₄≤r.

The exact rational bracket, checked with integer arithmetic, is

    625816818958/10^12 < r < 625816818959/10^12.

At these endpoints the numerator of x³+6x−4, after multiplying by 10^36, is respectively

    −3348659416260042279926088,
     3826280656413965615148079.

Also (5/8)³+6(5/8)−4=−3/512, so r>5/8>0.60318. The target was therefore not reached.

# 4. Route (a): degree profiles, Jensen, and the exact obstruction

## 4.1 What overlapping 3-cubes did and did not give

The first attempted improvement was a strict upper bound T_3<16 in Q₄. It is false. All eight 24-edge C₄-free Q₄ graphs found by enumeration are cubic, so T_3=16. More generally the enumeration found T_3=16 at each feasible full-vertex count 0,2,3,4. The maximum at full-vertex count 1 is 15.

The absence of isolated vertices in the T_3=16 cases suggested (3), which led to the certified improvement above.

The next idea was to use all Q₄ degree-profile inequalities, together with regular degrees and Jensen, to approach the requested constant. The following exact feasible mixture obstructs this particular approach.

## 4.2 An exact degree-profile mixture at p=5/8

Label Q₃ vertices by integers 0,…,7, with binary coordinates, and order its edges as

    (0,1),(0,2),(0,4),(1,3),(1,5),(2,3),
    (2,6),(3,7),(4,5),(4,6),(5,7),(6,7).

A triple (a,b,V) specifies a graph in Q₄: a selects these edges in the lower layer 0,…,7, b selects them in the upper layer 8,…,15, and V selects the vertical edges (x,x+8). Bits are numbered from zero; a bit equal to one means the corresponding edge is present.

The five graphs below were checked directly against all 24 squares:

| (a,b,V) | Probability numerator, denominator 512 | (n_0,n_1,n_2,n_3,n_4) | (e,T_2,T_3,T_4) |
|---|---:|---|---|
| (15,3510,171) | 132 | (1,5,4,3,3) | (17,31,15,3) |
| (15,3501,173) | 30 | (1,4,6,2,3) | (17,30,14,3) |
| (2029,3006,231) | 43 | (0,0,0,16,0) | (24,48,16,0) |
| (487,3454,235) | 157 | (0,0,6,8,2) | (22,42,16,2) |
| (95,3501,237) | 150 | (0,2,7,4,3) | (20,37,16,3) |

All weights are nonnegative and sum to 512. The weighted degree-histogram numerators, with denominator 512, are

    (162,1080,2700,3000,1250).

Consequently

    E n_i = 16 binom(4,i)(5/8)^i(3/8)^(4−i),

and equivalently

    (E e,E T_2,E T_3,E T_4)
      = (20,75/2,125/8,625/256).

Thus the degree of a uniform vertex in this random valid Q₄ is exactly Binomial(4,5/8).

Every linear inequality valid for the degree histogram of every C₄-free Q₄ remains valid for this convex mixture. It has exactly the local degree moments of a hypothetical asymptotically regular graph with density 5/8. Hence a relaxation retaining only those averaged histograms and the usual one-vertex moment constraints cannot rule out 5/8, even if it uses all valid Q₄ degree-histogram inequalities. A constant below 0.60318 requires information discarded by this relaxation.

This is not a construction of large C₄-free cubes of density 5/8. No globally consistent extension of the mixture is asserted. Correlations among different roots or overlapping faces could exclude it.

## 4.3 Q₅ checks on the route

Direct edge averaging using the brief's ex(Q₅,C₄)=56 gives only p≤56/80=7/10 for n≥5. That supplied value was not independently re-proved or enumerated here.

Averaging (3) over the ten 4-faces of a C₄-free Q₅ gives the exact inequality

    2T_3+5n_0+n_1 ≤ 160.                                (8)

Each present triple of directions at a vertex lies in two 4-faces. A degree-zero vertex is isolated in five 4-faces; a degree-one vertex is isolated in exactly one; a vertex of degree at least two is isolated in none.

For the regular-density limiting substitution,
T_3=32·10p³, n_0=32(1−p)^5, and n_1=32·5p(1−p)^4, (8) becomes

    4p³+(1−p)^4 ≤ 1,
    p⁴+6p²−4p ≤ 0.

This is exactly the existing inequality, not a new improvement. Its finite-dimensional averages also reproduce the Q₄ average because every 4-face appears equally often.

A separate full-vertex count in Q₅ is weaker. Within a parity class, distinct full vertices must have distance four. Translating one to zero, all others have weight four, and any two distinct weight-four vectors of length five have distance two. Thus at most two full vertices occur per parity class, at most four total. Averaging gives q_5≤1/8. Equation (5) and Jensen for t^5 then give p^5≤1/8+10/n for n≥5, hence only π₄≤(1/8)^(1/5), which exceeds 4^(−1/3).

No exhaustive Q₅ enumeration was attempted: its 80 edge choices were not treated as a tractable extension of the exact Q₄ search. The missing step is a new inequality retaining consistency between overlapping faces or multiple rooted neighborhoods.

## 4.4 Other degree-count attempts and the hand-proof gap

Counting length-two paths gives a weaker preliminary bound. Two vertices at distance two have at most one common graph neighbor, since two would form a square. There are 2^(n−1)binom(n,2) unordered vertex pairs at distance two. Hence

    Σ_v binom(d(v),2) ≤ 2^(n−1)binom(n,2),
    q_2≤1/2.

Equation (5) and Jensen give p²≤1/2+1/n for n≥2, and only π₄≤1/√2.

A weighted neighbor-degree count improves that to 2/3, still insufficient. Fix x, put d=d(x), and let S be its present directions. Among the neighbors x^i for i∈S, the edges back to x contribute d. Directions outside S contribute at most d(n−d). Each pair i,j∈S contributes at most one of the two edges from x^i and x^j to x^{i,j}, because both would complete a square through x. Thus

    Σ_{y∈N_G(x)} d(y) ≤ d+d(n−d)+binom(d,2)
                     = nd−binom(d,2).

Summing over x, the left side is Σ_y d(y)². Rearrangement gives

    3Σ_v d(v)² ≤ (2n+1)Σ_v d(v).

Jensen for t², followed by division by the positive mean degree when it is nonzero, yields p≤2/3+1/(3n). The zero-edge case is immediate. This count discards correlations beyond a pair of directions.

I also attempted to replace the finite certificate by a short hand classification according to the full vertices' parity classes. That proof was not completed. A remaining configuration has one full vertex at 0000 and one at 0111, with no other full vertices. In their common 3-face, the six edges between the two sets of three neighbors must form a matching: two incident such edges together with one of the full corners form a square. However a matched neighbor can acquire a third edge in the fourth direction, so this matching constraint alone does not force the required six degree-one-or-two vertices in Q₄. Controlling those extensions was the unclosed step. The report consequently uses the exhaustive certificate for (1), and does not claim a hand proof of it.

# 5. Route (b): direction entropy and compression

## 5.1 Compression fails to preserve the forbidden configuration

Consider Q₃ with precisely these four edges:

    (0,1),(0,2),(5,7),(6,7).

It is the disjoint union of two two-edge paths and two isolated vertices, so is C₄-free.

Compress all edges parallel to the first two coordinates toward the layer where the third coordinate is zero: for a pair of parallel corresponding edges, replace their lower/upper presence bits (a,b) by (a OR b,a AND b). Leave third-direction edges unchanged.

The resulting four edges are

    (0,1),(0,2),(1,3),(2,3),

which form a square. Edge count is preserved. Thus this natural direction compression cannot be used as a C₄-free reduction. Any replacement compression must prove preservation by an additional mechanism.

## 5.2 Face entropy yields only the face edge bound

For n≥2, randomly translate and permute coordinates of a fixed C₄-free G⊆Q_n, and let Z be its vector of edge indicators. Entropy is measured in bits. Each edge lies in n−1 coordinate squares, so the entropy covering inequality gives

    H(Z) ≤ (1/(n−1)) Σ_F H(Z_F).

For completeness, this inequality follows from the entropy chain rule: order all edge coordinates, expand each H(Z_F) in that induced order, and use that conditioning on fewer earlier coordinates cannot decrease conditional entropy. Each coordinate's full-chain conditional entropy is counted n−1 times.

For λ>1 the allowed edge subsets of a square have weighted partition polynomial

    P(λ)=1+4λ+6λ²+4λ³.

Nonnegativity of relative entropy (a consequence of log x≤x−1), applied against the probability distribution proportional to λ^(number of present edges), gives

    H(Z_F) ≤ log₂ P(λ) − E|Z_F| log₂ λ.

Coordinate symmetrization gives E|Z_F|=4p. There are n(n−1)2^(n−3) squares and M=n2^(n−1) edge coordinates. Since H(Z)≥0,

    p ≤ log₂ P(λ)/(4 log₂ λ).

For every λ>1 this right side exceeds 3/4, because P(λ)>λ³; its limit as λ→∞ is 3/4. The resulting optimized bound is exactly p≤3/4. Replacing squares by the supplied Q₅ family yields only its edge bound 7/10 by the same leading-degree argument.

One cannot repair this by assuming extensive entropy from positive density. The random graph here is chosen from at most 2^n n! translated/permuted copies, so

    H(Z) ≤ n+log₂(n!) ≤ n+n log₂ n,
    H(Z)/M ≤ 2(1+log₂ n)/2^n.

These are explicit bounds. Positive edge density supplies no missing lower bound on the joint entropy in this symmetrization.

## 5.3 Root-direction entropy has an exact feasible obstruction

Choose a graph from the mixture in Section 4.2, uniformly translate it, uniformly permute its four directions, and inspect the four incident-edge bits at a fixed root. Their sum has distribution Binomial(4,5/8). Direction permutation makes all subsets of a given size equiprobable. Therefore each bit pattern S⊆{1,2,3,4} has probability

    (5/8)^|S| (3/8)^(4−|S|).

The four root bits are thus exactly independent Bernoulli(5/8), and their entropy is 4h₂(5/8), where h₂(t)=−t log₂t−(1−t)log₂(1−t). Every sampled whole 4-cube is nevertheless C₄-free.

This demonstrates the precise information loss in an entropy argument using only incident direction bits at one root: even the independent, maximum-entropy root law at p=5/8 is locally realizable. It does not disprove possible entropy inequalities involving different roots or overlap consistency. Those additional correlations were not controlled here.

# 6. Exact checks, algorithms, and cost

## Checks actually run

1. All 2^12=4096 labelled edge subsets of Q₃ were checked. Exactly 2902 were C₄-free. Their counts by edge number 0,…,12 were

       1,12,66,220,489,744,756,468,138,8,0,0,0.

   There were 35 degree histograms. The maximum number of degree-three vertices was two. This also checked ex(Q₃,C₄)=9.

2. All labelled C₄-free Q₄ graphs were enumerated using two valid Q₃ layers. If their edge masks are a and b, the set V of present vertical edges must be an independent vertex set in the Q₃ graph with edge mask a AND b. This condition is necessary and sufficient: the only squares not internal to a layer use two vertical edges and a horizontal edge present in both layers. Ordered unequal layer pairs were counted with multiplicity two.

   Exactly 1,226,436,381 graphs were found, with 828 distinct degree profiles. Equivalently these are 828 distinct (e,T_2,T_3,T_4) vectors, since the histogram is recovered successively from these moments and the vertex count 16.

   Counts by edge number 0,…,24 were

       1,32,496,4960,35936,200704,897120,3287328,
       10029480,25723136,55739072,102159936,157982000,
       204855968,220449792,193877952,136352716,74390848,
       30170096,8558976,1553936,158144,7552,192,8.

   Counts at 25,…,32 were zero. Thus ex(Q₄,C₄)=24 was independently checked. This enumeration was run twice: first for extrema and profile counts, then to retain explicit witnesses. Both runs returned the same counts.

3. The independent full-root enumeration in Appendix A examined all 47,775,744 candidates, retained 25,002,059, and found zero violations of (1).

4. The five mixture witnesses were separately decoded into edge lists, checked against all 24 squares, and their degree histograms recomputed. Weighted histogram totals were exactly (162,1080,2700,3000,1250)/512.

5. The two rational endpoint signs for the cubic were checked using BigInt arithmetic. The compression example was checked before and after: zero squares before and one after.

6. A deterministic exploratory search solved ordinary 5-by-5 real linear systems to locate the five mixture weights. It found them at loop index 592 (zero-based); the displayed final weights were then checked exactly as integers. This was not SAT, ILP, or an optimization solver.

## Cost and limitations

All arithmetic ran in one Node.js process at a time, with --single-threaded --v8-pool-size=1 and UV_THREADPOOL_SIZE=1; no worker threads, subprocess parallelism, SAT/ILP solvers, paid services, or external mathematical sources were used.

Measured process CPU (user+system, microseconds):

| Computation | CPU microseconds |
|---|---:|
| Q₃ enumeration | 24,517 |
| First Q₄ layer enumeration | 14,629,921 |
| Second Q₄ layer enumeration | 14,046,768 |
| Mixture search | 14,179 |
| Independent full-root verifier | 3,864,772 |
| Final witness/root/compression checks | 695 |
| Total | 32,580,852 |

Thus measured mathematical CPU in this resumed run was 32.580852 seconds, well below one CPU-hour. This excludes Node startup, orchestration, and file/control-plane operations. The supplied interrupted-run context had no CPU accounting; no aggregate cost for that earlier execution is asserted. Model-token cost was not available.

The strongest result remains a computationally certified partial bound r≈0.625816819, not the requested human-readable improvement below 0.60318. The exact 5/8 mixture identifies the obstruction to the particular degree/one-root entropy relaxations tried. There is no claimed obstruction to more informative structural or entropy methods.

# Appendix A. Complete independent certificate for (1)

Run with:

    UV_THREADPOOL_SIZE=1 node --single-threaded --v8-pool-size=1

and supply the following JavaScript on standard input. No input files or libraries are needed.

~~~js
const start=process.cpuUsage(),wall=Date.now();
const E=[];for(let x=0;x<16;x++)for(let i=0;i<4;i++)if(!(x>>i&1))E.push([x,x^(1<<i)]);
function pop(x){x=x-((x>>>1)&0x55555555);x=(x&0x33333333)+((x>>>2)&0x33333333);return (((x+(x>>>4))&0x0f0f0f0f)*0x01010101)>>>24;}
const inc=Array(16).fill(0);E.forEach(([x,y],i)=>{inc[x]|=1<<i;inc[y]|=1<<i;});
const squares=[];for(let x=0;x<16;x++)for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)if(!(x>>i&1)&&!(x>>j&1)){let mask=0;const v=[x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)];E.forEach(([a,b],e)=>{if(v.includes(a)&&v.includes(b))mask|=1<<e;});squares.push(mask);}
const pairVertices=Array.from({length:16},(_,i)=>i).filter(x=>pop(x)===2),pairs=pairVertices.map(x=>E.flatMap(([a,b],i)=>(a===x&&pop(b)===1)||(b===x&&pop(a)===1)?[i]:[]));
const fixed=inc[0],free=E.flatMap(([a,b],i)=>pop(a)>=2&&pop(b)>=2?[i]:[]);
if(free.length!==16||pairs.some(p=>p.length!==2))throw Error('partition');
const freeMasks=new Int32Array(65536);for(let s=1;s<65536;s++){const low=s&-s;freeMasks[s]=freeMasks[s^low]|(1<<free[31-Math.clz32(low)]);}
let valid=0,minLow=Array(17).fill(99),witness=Array(17).fill(null),fullCounts=Array(17).fill(0),violations=0;
for(let t=0;t<729;t++){let mask=fixed,q=t;for(const p of pairs){const r=q%3;q=Math.floor(q/3);if(r)mask|=1<<p[r-1];}for(let s=0;s<65536;s++){const m=mask|freeMasks[s];let ok=true;for(const sq of squares)if((m&sq)===sq){ok=false;break;}if(!ok)continue;valid++;let hist=Array(5).fill(0);for(const z of inc)hist[pop(m&z)]++;const low=hist[1]+hist[2],f=hist[4];fullCounts[f]++;if(low<minLow[f]){minLow[f]=low;witness[f]={mask:m>>>0,hist};}if(low<3*f)violations++;}}
console.log(JSON.stringify({attempts:729*65536,valid,minLow,fullCounts,witness,violations,cpu:process.cpuUsage(start),wall_ms:Date.now()-wall}));

~~~

# Appendix B. Complete Q₄ layer/profile enumeration

The following was the second layer enumeration actually run. The returned profile list contains a witness (a,b,V) for each profile. The first enumeration used the same partition and additionally tabulated maxima and the componentwise maximal profiles. Integer counts are below 2^53; bit masks here use only 12 or 8 bits.

~~~js
const start=process.cpuUsage(),wall=Date.now();
let E=[],sq=[];for(let x=0;x<8;x++)for(let i=0;i<3;i++)if(!(x>>i&1))E.push([x,x^(1<<i)]);
for(let x=0;x<8;x++)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(!(x&(1<<i))&&!(x&(1<<j))){const verts=[x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)];sq.push(E.reduce((a,[u,v],e)=>a|(verts.includes(u)&&verts.includes(v)?1<<e:0),0));}
let G=[];for(let m=0;m<4096;m++)if(!sq.some(s=>(s&m)===s)){let d=Array(8).fill(0),e=0;E.forEach(([u,v],i)=>{if(m>>i&1){d[u]++;d[v]++;e++;}});G.push({m,d,e,t2:d.reduce((a,v)=>a+v*(v-1)/2,0),t3:d.filter(v=>v===3).length});}
let IS=Array.from({length:4096},()=>[]),pc=new Uint8Array(256),bit=new Uint8Array(256);for(let v=1;v<256;v++){pc[v]=pc[v&(v-1)]+1;bit[v]=31-Math.clz32(v&-v);}for(let v=0;v<256;v++){let forbidden=0;E.forEach(([x,y],i)=>{if((v>>x&1)&&(v>>y&1))forbidden|=1<<i;});for(let m=0;m<4096;m++)if(!(m&forbidden))IS[m].push(v);}
let profiles=new Map(),counts=Array(33).fill(0),ds2=new Uint8Array(256),ds3=new Uint8Array(256),ds4=new Uint8Array(256),w2=new Uint8Array(8),w3=new Uint8Array(8),w4=new Uint8Array(8);
for(let ai=0;ai<G.length;ai++){let a=G[ai];for(let bi=ai;bi<G.length;bi++){let b=G[bi],mult=ai===bi?1:2;for(let x=0;x<8;x++){w2[x]=a.d[x]+b.d[x];w3[x]=a.d[x]*(a.d[x]-1)/2+b.d[x]*(b.d[x]-1)/2;w4[x]=(a.d[x]===3)+(b.d[x]===3);}for(let v=1;v<256;v++){const rest=v&(v-1),k=bit[v];ds2[v]=ds2[rest]+w2[k];ds3[v]=ds3[rest]+w3[k];ds4[v]=ds4[rest]+w4[k];}for(const v of IS[a.m&b.m]){const e=a.e+b.e+pc[v],t2=a.t2+b.t2+ds2[v],t3=a.t3+b.t3+ds3[v],t4=ds4[v];counts[e]+=mult;const key=e+33*(t2+97*(t3+65*t4));if(!profiles.has(key))profiles.set(key,{p:[e,t2,t3,t4],w:[a.m,b.m,v]});}}
if(process.cpuUsage(start).user+process.cpuUsage(start).system>110e6)throw Error('110-second CPU stop');}
console.log(JSON.stringify({counts,profiles:Array.from(profiles.values()),cpu:process.cpuUsage(start),wall_ms:Date.now()-wall}));
~~~

# Appendix C. Separate exact witness and counterexample checks

This independently reconstructs the five displayed graphs, checks their squares and histograms, checks the weighted histogram, verifies the cubic bracket, and checks the compression example. The exploratory floating-point search is not needed to reproduce any conclusion.

~~~js
const rows=[{"p":[17,31,15,3],"w":[15,3510,171]},{"p":[17,30,14,3],"w":[15,3501,173]},{"p":[24,48,16,0],"w":[2029,3006,231]},{"p":[22,42,16,2],"w":[487,3454,235]},{"p":[20,37,16,3],"w":[95,3501,237]}];
const start=process.cpuUsage();
const E3=[];for(let x=0;x<8;x++)for(let i=0;i<3;i++)if(!(x>>i&1))E3.push([x,x^(1<<i)]);
const weights=[132,30,43,157,150],sumHist=Array(5).fill(0),checked=[];
function sqs(n,E){let out=[];for(let x=0;x<1<<n;x++)for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(!(x>>i&1)&&!(x>>j&1)){const a=[x,x^(1<<i),x^(1<<j),x^(1<<i)^(1<<j)];out.push(E.filter(([u,v])=>a.includes(u)&&a.includes(v)));}return out;}
for(let k=0;k<rows.length;k++){let[a,b,V]=rows[k].w,E=[];for(let i=0;i<12;i++){if(a>>i&1)E.push(E3[i]);if(b>>i&1)E.push(E3[i].map(x=>x+8));}for(let x=0;x<8;x++)if(V>>x&1)E.push([x,x+8]);let d=Array(16).fill(0);for(let [u,v]of E){d[u]++;d[v]++;}let hist=Array(5).fill(0);d.forEach(x=>hist[x]++);let nSquares=sqs(4,E).filter(e=>e.length===4).length;if(nSquares)throw Error('square in witness');hist.forEach((z,j)=>sumHist[j]+=weights[k]*z);checked.push({w:rows[k].w,weight:weights[k],hist,edges:E.length,squares:nSquares});}
const lo=625816818958n,hi=625816818959n,den=1000000000000n;
function cubicNum(x){return x**3n+6n*x*den**2n-4n*den**3n;}
const before=[[0,1],[0,2],[5,7],[6,7]],after=before.map(([a,b])=>[a&3,b&3]);
console.log(JSON.stringify({checked,sumWeights:weights.reduce((a,b)=>a+b,0),sumHist,expectedTwice:[162,1080,2700,3000,1250],rootBracketSigns:[cubicNum(lo).toString(),cubicNum(hi).toString()],compression:{before,after,beforeSquares:sqs(3,before).filter(e=>e.length===4).length,afterSquares:sqs(3,after).filter(e=>e.length===4).length},cpu:process.cpuUsage(start)}));

~~~

Next mathematical action: obtain and prove a constraint on overlapping rooted faces that excludes the displayed 5/8 degree mixture. No follow-up execution is scheduled by this report.
