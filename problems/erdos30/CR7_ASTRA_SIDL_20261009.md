STATUS: DISPROVED — SID-L is false: the 68-element strong Sidon set listed below lies in {0,...,4095}, has 68² = 4624 ≥ 4096, and for T = 719 satisfies 100S = 18,027,958,800 < 75,825,771,636 = 3·68·719³.

# Exact counterexample and proof

Take N = 4096 and the following set A, listed in full in increasing order:

```text
0, 14, 134, 207, 220, 417, 493, 527, 538, 580, 587, 662,
823, 916, 925, 962, 1137, 1191, 1215, 1253, 1341, 1353,
1356, 1430, 1499, 1611, 1617, 1800, 1851, 2025, 2060,
2077, 2157, 2205, 2207, 2236, 2262, 2263, 2358, 2510,
2531, 2602, 2646, 2727, 2759, 2825, 2844, 2992, 3075,
3103, 3136, 3243, 3259, 3263, 3302, 3327, 3392, 3584,
3606, 3614, 3624, 3715, 3778, 3814, 3819, 3886, 3933, 3956.
```

There are k = 68 entries, all between 0 and 3956 inclusive. Thus A is contained in {0,...,4095}, N meets the required onset, and k² = 4624 ≥ 4096.

Direct enumeration of the 68·67/2 = 2278 positive differences gives 2278 distinct integers, each with multiplicity one. Independently, direct enumeration of the 68·69/2 = 2346 sums with the first index at most the second gives 2346 distinct integers. An exhaustive integer verifier for both assertions appears below; it stops with an error at the first collision. Consequently A is strong Sidon under either definition in the brief. Neither the construction method nor any theorem about finite fields is needed for this verification.

The exact calculation of T is certified by

\[
10000\cdot718^4=2,657,649,945,760,000
 < 2,666,934,172,647,424=38809\cdot4096^3
 \le 2,672,486,755,210,000=10000\cdot719^4.
\]

The fourth power is strictly increasing on the positive integers, so T = 719 is the least positive integer required by the definition.

The complete list of missing differences in {1,...,718} is

\[
\{601,615,624,638,671,685\}.
\]

For these six differences the exact integer summands are:

| d | 4T³ − 6dT² + 2d³ |
|---:|---:|
| 601 | 56,782,072 |
| 615 | 44,410,496 |
| 624 | 37,219,100 |
| 638 | 27,241,272 |
| 671 | 9,718,272 |
| 685 | 4,908,376 |
| **Sum S** | **180,279,588** |

The identity

\[
4T^3-6dT^2+2d^3=2(T-d)^2(2T+d)
\]

follows by expansion, and division by 3T³ gives exactly f(d/T). Therefore

\[
M(A)=\frac{180,279,588}{1,115,084,877}
       \mathrel{\approx}0.1616734221030961.
\]

The decimal is descriptive only. The decisive exact comparison is

\[
100S=18,027,958,800
 <75,825,771,636=3kT^3.
\]

Since 100 and 3T³ are positive, this is equivalent to M(A) < k/100 = 0.68. This supplies a counterexample at the first permitted value of N and disproves SID-L exactly as stated. No limiting argument, error term, or unproved asymptotic assertion is used.

## Exhaustive proof certificate

The following standalone JavaScript enumerates every difference and every allowed sum. All quantities affecting the target comparison use BigInt. The array entries, indices, and multiplicities are integers of magnitude below 10,000 and are represented exactly as JavaScript Numbers. The window moments are accumulated as BigInts too. The code uses no library, external file, random choice, solver, or algebraic construction.

```javascript
// BEGIN EXACT CERTIFICATE
function check(condition, message) {
  if (!condition) throw new Error(message);
}
const A = [
  0,14,134,207,220,417,493,527,538,580,587,662,
  823,916,925,962,1137,1191,1215,1253,1341,1353,
  1356,1430,1499,1611,1617,1800,1851,2025,2060,
  2077,2157,2205,2207,2236,2262,2263,2358,2510,
  2531,2602,2646,2727,2759,2825,2844,2992,3075,
  3103,3136,3243,3259,3263,3302,3327,3392,3584,
  3606,3614,3624,3715,3778,3814,3819,3886,3933,3956
];
const N = 4096, k = A.length;
check(k === 68 && N >= 4096 && k*k >= N, 'parameters');
for (let i = 0; i < k; ++i) {
  check(Number.isInteger(A[i]) && 0 <= A[i] && A[i] < N,
        'entry outside the interval');
  if (i > 0) check(A[i-1] < A[i], 'not a strictly increasing set');
}

const differences = new Uint8Array(N);
const sums = new Uint8Array(2*N-1);
let pairCount = 0, sumCount = 0;
for (let i = 0; i < k; ++i) {
  for (let j = 0; j < i; ++j) {
    const d = A[i]-A[j];
    check(differences[d] === 0, 'repeated positive difference '+d);
    differences[d] = 1;
    ++pairCount;
  }
  for (let j = i; j < k; ++j) {
    const s = A[i]+A[j];
    check(sums[s] === 0, 'repeated unordered sum '+s);
    sums[s] = 1;
    ++sumCount;
  }
}
check(pairCount === 2278 && sumCount === 2346, 'enumeration sizes');
check(differences.reduce((a,b) => a+b, 0) === 2278,
      'difference support size');
check(sums.reduce((a,b) => a+b, 0) === 2346, 'sum support size');

const threshold = 38809n*BigInt(N)**3n;
let low = 0n, high = BigInt(N);
check(10000n*high**4n >= threshold, 'binary-search upper bound');
while (high-low > 1n) {
  const mid = (low+high)/2n;
  if (10000n*mid**4n >= threshold) high = mid;
  else low = mid;
}
const t = high, T = Number(t);
check(T === 719, 'T');
check(10000n*(t-1n)**4n === 2657649945760000n, 'lower bracket');
check(threshold === 2666934172647424n, 'threshold');
check(10000n*t**4n === 2672486755210000n, 'upper bracket');
check(10000n*(t-1n)**4n < threshold && threshold <= 10000n*t**4n,
      'least integer T');

let S = 0n, P = 0n, missingTent = 0n;
const missing = [], weights = [];
for (let d = 1; d < T; ++d) {
  const b = BigInt(d);
  if (differences[d] === 0) {
    const w = 4n*t**3n-6n*b*t*t+2n*b**3n;
    check(w === 2n*(t-b)**2n*(2n*t+b), 'factorization');
    missing.push(d);
    weights.push(w.toString());
    S += w;
    missingTent += t-b;
  } else {
    P += t-b;
  }
}
check(missing.join(',') === '601,615,624,638,671,685', 'missing list');
check(weights.join(',') ===
      '56782072,44410496,37219100,27241272,9718272,4908376',
      'individual summands');
check(S === 180279588n && missingTent === 480n && P === 257641n,
      'weighted totals');
const left = 100n*S, right = 3n*BigInt(k)*t**3n;
check(left === 18027958800n && right === 75825771636n, 'target sides');
check(left < right, 'not a counterexample');

// Independently evaluate the window and third-order diagnostics.
const r = new Uint8Array(N+T-1);
for (const a of A) for (let x = a; x < a+T; ++x) ++r[x];
const moments = [0n,0n,0n];
const histogram = new Array(k+1).fill(0);
let endSquare = 0n, bulkSquare = 0n;
for (let x = 0; x < r.length; ++x) {
  const b = BigInt(r[x]);
  moments[0] += b;
  moments[1] += b*b;
  moments[2] += b*b*b;
  ++histogram[r[x]];
  if (x < T-1 || x >= N) endSquare += b*b;
  else bulkSquare += b*b;
}
let U = 0n;
for (let i = 0; i < k; ++i)
  for (let j = i+1; j < k; ++j)
    for (let h = j+1; h < k; ++h)
      if (A[h]-A[i] < T) U += t-BigInt(A[h]-A[i]);
check(U === 869739n, 'triple term');
check(moments.map(String).join(',') === '48892,564174,6813172',
      'window moments');
check(moments[0] === BigInt(k)*t, 'first-moment identity');
check(moments[1] === BigInt(k)*t+2n*P, 'second-moment identity');
check(moments[2] === BigInt(k)*t+6n*P+6n*U, 'third-moment identity');
check(endSquare === 70032n && bulkSquare === 494142n, 'end/bulk split');
check(histogram.slice(0,18).join(',') ===
      '139,37,167,140,18,233,139,125,31,271,461,992,894,396,549,174,42,6',
      'window histogram');
check(histogram.slice(18).every(v => v === 0), 'maximum window count');

const bins = [0,0,0,0,0,0];
let largeDifferenceCount = 0;
for (let d = 1; d < N; ++d) if (differences[d]) {
  ++bins[Math.floor(d/T)];
  if (d > N-T) ++largeDifferenceCount;
}
check(bins.join(',') === '712,594,451,320,167,34', 'position bins');
check(A.filter(a => a < T).length === 12, 'left end size');
check(A.filter(a => a >= N-T).length === 12, 'right end size');
check(largeDifferenceCount === 67, 'large differences');
check(8192n*(BigInt(k*k)+2n*BigInt(pairCount)) === 75202560n,
      'fourth Fourier moment');

console.log(JSON.stringify({
  status: 'DISPROVED', N, k, T, pairs: pairCount,
  unorderedSums: sumCount, missing, weights, S: S.toString(),
  left: left.toString(), right: right.toString(),
  windowMoments: moments.map(String), tripleTerm: U.toString()
}));
// END EXACT CERTIFICATE
```

Why this is an exhaustive certificate: the two nested difference loops visit each ordered index pair i > j exactly once; the independent sum loops visit each pair i ≤ j exactly once. Each value is tested before marking its slot. The missing-difference loop visits every integer in the required range, using precisely those marked slots. The binary search maintains one infeasible lower endpoint and one feasible upper endpoint until they are consecutive. Finally all arithmetic in the kernel sum and the strict comparison is integer arithmetic. Thus successful execution verifies each finite assertion used in the disproof, without sampling.

# Routes worked and exact obstructions

## (a) Positivity at all scales and the exact fourth moment

For this same A define, for every real u,

\[
F(u)=\sum_{a\in A}e^{iua},\qquad
|F(u)|^2=k+2\sum_{d\in D_+(A)}\cos(du).
\]

The second identity follows by multiplying the sum by its complex conjugate and grouping the pairs a > b and b > a. It is nonnegative at every real u. Also |F(u)| ≤ k: each summand has modulus one, and repeated application of the triangle inequality bounds the modulus of their sum by the sum of their moduli. For completeness, the triangle inequality for two complex numbers follows by squaring and using Re(z·conjugate(w)) ≤ |z||w|, which follows from Re(v) ≤ |v|.

Embed in the cyclic group of order L = 8192 = 2N. All integer differences are in [−3956,3956], so reducing them modulo L identifies no two different integer differences. Write c(d) for the cyclic autocorrelation. Then c(0) = 68, and all other nonzero values of c are one, at exactly 4556 residues. For u_j = 2πj/L,

\[
\sum_{j=0}^{L-1}|F(u_j)|^4
=L\sum_{d=0}^{L-1}c(d)^2
=8192(68^2+4556)
=75,202,560.
\]

Here is the complete orthogonality argument: for an integer h, the sum of e^{2πijh/L} over j = 0,...,L−1 is L if L divides h and zero otherwise. In the latter case the geometric-series ratio is not one and its L-th power is one, giving sum zero. Expanding the square of the Fourier transform of c and using this identity leaves exactly L times the sum of squares of its coefficients. This proves the displayed fourth moment directly, including its normalization.

The near/far decomposition can be made exact at a negative Dirichlet lobe. Put

\[
u_* = \frac{3\pi}{2T},\quad
E=\{601,615,624,638,671,685\},\quad
R(u)=2\sum_{\substack{d\in D_+(A)\\d\ge T}}\cos(du).
\]

Summing the finite geometric series gives

\[
1+2\sum_{d=1}^{T-1}\cos(du)
=\frac{\sin((T-\tfrac12)u)}{\sin(u/2)}
\]

whenever the denominator is nonzero. At u = u_* the quotient is −cot(3π/(4T)). Consequently

\[
R(u_*)=|F(u_*)|^2-(k-1)+\cot\frac{3\pi}{4T}
        +2\sum_{d\in E}\cos(du_*)
\ge -(k-1)+\cot\frac{3\pi}{4T}
        +2\sum_{d\in E}\cos(du_*).
\]

This is the exact compensation inequality on the tested frequency. More generally positivity gives, at every u, R(u) ≥ −k − 2Σ_{d<T, d∈D₊(A)} cos(du); it holds throughout any selected arc. There are exactly 1566 realized far differences, all with coefficient one. Orthogonality as above gives their exact separate budget

\[
\sum_{j=0}^{8191}R(u_j)^2=2\cdot8192\cdot1566=25,657,344.
\]

For diagnostic purposes only, ordinary floating point evaluation gave a fully realized near contribution of approximately −238.1519852061462, an actual near contribution of approximately −232.25494344513177, R(u_*) approximately 265.60373324365855, and |F(u_*)|² approximately 33.34878979852662. These decimals are not used as inequalities in the proof.

**Exact obstruction to this route proving SID-L:** the explicit polynomial F above has the required nonnegative square at every scale, the 0/1 far-difference structure, the exact fourth moment, the required support, and the bound |F| ≤ k, yet its missing mass is strictly less than k/100. Thus those true constraints cannot imply the proposed numerical target. The separate, stronger question whether a profile with every d < T realized can obey all those constraints was not settled; a profile with only the six stated omissions already disproves the requested lemma.

Two preliminary relaxations also failed to answer the full-realization question:

* The coefficients q_d = 1−|d|/N for 0 < |d| < N give the nonnegative polynomial k−1 + N⁻¹|Σ_{a=0}^{N−1}e^{iua}|². Expansion proves that formula. They are fractional, and at u = 0 this polynomial is k−1+N = 4163, whereas an actual 68-point set requires k² = 4624. This is an explicit wrong-normalization/wrong-coefficient obstruction, not a compatible Sidon profile.
* On a group of order m = k²−k+1, the formal autocorrelation c(0)=k and c(d)=1 otherwise has Fourier values k² at zero and k−1 elsewhere. The same geometric-series identity proves this, and its squared-coefficient sum is 2k²−k. However, with k=68 it lives on m=4557 < 2·4096 and has no required integer-interval support. It therefore cannot settle the requested embedded full-realization problem either.

## (b) Window counts, the third moment, and the ends

There is an indexing defect in the stated seed: with a possible element 0, summing r(x)=|A∩[x−T+1,x]| over x=1,...,N+T−1 drops one occurrence of that element. Use x=0,...,N+T−2 instead. This gives N+T−1 = 4814 windows and the intended identities exactly.

Let

\[
P=\sum_{\substack{d<T\\d\in D_+(A)}}(T-d),\qquad
U=\sum_{\substack{a<b<c\\a,b,c\in A}}\max(0,T-(c-a)).
\]

An element belongs to T windows, a pair at distance d belongs to max(0,T−d) windows, and a triple with extreme points a,c belongs to max(0,T−(c−a)) windows. Expanding r² = r+2·binom(r,2) and r³ = r+6·binom(r,2)+6·binom(r,3) proves

\[
\sum r=kT,\quad \sum r^2=kT+2P,\quad
\sum r^3=kT+6P+6U.
\]

For the counterexample, direct enumeration yields

\[
P=257641,\quad U=869739,\quad
(\sum r,\sum r^2,\sum r^3)=(48892,564174,6813172).
\]

The histogram of the window counts, which supplies another exact check of all three moments, is:

| r | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| windows | 139 | 37 | 167 | 140 | 18 | 233 | 139 | 125 | 31 |

| r | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| windows | 271 | 461 | 992 | 894 | 396 | 549 | 174 | 42 | 6 |

Full realization would give P = T(T−1)/2 = 258121. The actual missing triangular mass is only 480, so the second moment is only 960 below the full-realization value 565134. Cauchy–Schwarz does not exclude it: its cross-multiplied form reads

\[
48892^2=2,390,427,664
\le4814\cdot564174=2,715,933,636.
\]

This version of Cauchy–Schwarz follows immediately by expanding Σ(r−mean(r))² ≥ 0. Substituting Σr² = kT+2P into it gives a lower bound on P, hence an upper bound on missing triangular mass, the opposite direction from the desired proof.

The two end clusters are explicitly

```text
A ∩ [0,719):
0,14,134,207,220,417,493,527,538,580,587,662

A ∩ [3377,4096):
3392,3584,3606,3614,3624,3715,3778,3814,3819,3886,3933,3956
```

They each have twelve points. There are exactly 67 realized differences greater than N−T=3377. Each such pair necessarily joins the two displayed clusters: b−a>N−T and b≤N−1 imply a<T, and a≥0 implies b>N−T. Enumeration considers these pairs together with every interior pair. In addition, the actual boundary windows x<718 or x≥4096 contribute 70032 to Σr², and the bulk windows 718≤x<4096 contribute 494142. Their sum is 564174. The value of U above enumerates all triples, including those meeting either end.

**Exact obstruction:** this actual 0/1 point set, its displayed window histogram, the full triple sum, and the boundary/bulk contributions coexist. An additional upper bound deduced from these structures cannot force SID-L because this very object violates its conclusion. I found no valid extra upper bound excluding this profile; no such bound can hold for all of the sets in the brief.

## (c) Pair budget by position: limited check

The positions of the same set give the following exact pair counts:

| Difference range | Realized differences |
|---|---:|
| 1,...,718 | 712 |
| 719,...,1437 | 594 |
| 1438,...,2156 | 451 |
| 2157,...,2875 | 320 |
| 2876,...,3594 | 167 |
| 3595,...,4095 | 34 |
| Total | 2278 |

Every counted difference comes from actual displayed positions a and a+d≤3956≤N−1, and every multiplicity is one. This exact position array defeats an attempted proof based just on allocating near/far pair budgets. The suggested general interval bound was not used or claimed proved; once an actual counterexample was found there was no reason to pursue it as a route to SID-L.

## (d) Cyclic lifts: successful disproof search

The construction was used only to find candidate lists. Every final claim of strong Sidonicity was checked by enumerating differences, independently of that construction.

Here is an exact specification of the finite search objects. For each row below, calculations were performed on triples representing the quotient ring (Z/qZ)[X]/(X³−X−c), with g = a+X. Multiplication expands the product and replaces X³ by X+c; exponentiation is repeated squaring. For 0≤i<m=q²+q+1, include i in B if all three coefficients of

\[
g^i+(g^i)^q+(g^i)^{q^2}
\]

vanish. For each computed B the program directly checked |B|=q+1 and that the ordered differences between distinct elements hit every nonzero residue modulo m exactly once. This finite verification, not an assertion about a named algebraic family, was the condition for retaining B.

| q | c | a in g=a+X | m | k | units u tested, 1≤u≤⌊m/2⌋ | cuts tested at N=m |
|---:|---:|---:|---:|---:|---:|---:|
| 67 | 3 | 4 | 4557 | 68 | 1260 | 85680 |
| 83 | 3 | 6 | 6973 | 84 | 3294 | 276696 |
| 127 | 1 | 2 | 16257 | 128 | 5418 | 693504 |

For each listed u coprime to m, sort C=uB modulo m and consider each cut C_i, giving A_i={c−C_i modulo m:c∈C}, represented in [0,m). These are the k distinct circular-cut configurations; other shifts inside an empty gap merely translate the resulting integer set. Negating u reflects such configurations and does not change the positive-difference multiset, which explains the restriction u≤m/2.

For an exact fast calculation at fixed T, a pair C_i<C_j with d=C_j−C_i<T contributes its integer weight to the missing mass for precisely the cuts with indices i+1,...,j. If m−d<T, the complementary directed arc contributes to precisely the complementary cuts. This follows because a modular difference is absent as an integer difference exactly when the cut crosses that directed arc. Range additions over cut indices therefore evaluate all cut masses. All intermediates in this three-row search were below 2⁵³: each weight is at most 4·2021³ and there are fewer than 2021 eligible directed differences, so even 4·2021⁴ < 2⁵³ bounds the total absolute eligible weight. A candidate minimum was then verified with a fresh difference set and BigInt summation.

The minima from these N=m searches were:

| q | u | zero-based cut index | N | T | exact S | 100M/k, approximately |
|---:|---:|---:|---:|---:|---:|---:|
| 67 | 353 | 66 | 4557 | 779 | 567713840 | 0.5886903833 |
| 83 | 18 | 18 | 6973 | 1072 | 1850037520 | 0.5959305357 |
| 127 | 971 | 115 | 16257 | 2021 | 34834245740 | 1.0989457312 |

The q=67 minimum is exactly the 68-entry A in the proof. It already disproves SID-L at N=4557. Its maximum is only 3956, so the same set can be placed at N=4096, producing the stronger counterexample proved above.

The first 32 dilations ordered by their best fixed-N mass in each row were also examined at every cut using the shortest admissible interval length N=max(A_i)−min(A_i)+1. This gave at most 2176, 2688, and 4096 candidate cuts respectively; cuts with N<4096 were excluded from that particular test. The respective best retained results were:

| q | u | cut | N | T | S | 100M/k, approximately |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 67 | 1111 | 62 | 4147 | 726 | 902392420 | 1.1559935452 |
| 83 | 18 | 18 | 6160 | 976 | 488998176 | 0.2087167220 |
| 127 | 971 | 115 | 15216 | 1923 | 21487110140 | 0.7868807715 |

These tables describe exactly the finite searches performed, not an exhaustive search over all strong Sidon sets. The shortest interval convention must include the +1: an integer set of diameter L fits {0,...,L}, which has length L+1. The final proof avoids any convention ambiguity by using N=4096 directly.

**Obstruction to the stronger full-realization attempt:** the selected q=67 configuration still misses 601,615,624,638,671,685 below its final T. Thus this work does not produce M=0. It does produce the strict inequality necessary to disprove SID-L. No family with a proved asymptotic trend was obtained or is needed.

# Verification record and cost

The discovery computation, a separate direct verifier on the displayed list, and the exact verifier embedded above were run independently. The direct verifier checked both positive differences and unordered sums; the embedded verifier additionally rechecked every table entry used for the final counterexample's window, third-moment, endpoint, and pair-budget calculations. After writing this report, I replayed its embedded certificate and independently re-derived the counterexample from the report's displayed set: for every d=1,...,4095, I summed 1_A(x)1_A(x+d) over all x with 0≤x<x+d<4096. Every such sum was zero or one, their total was 2278, and the same six missing small differences gave S=180279588 using the factored weight. Both strict-comparison sides matched those in the first line. The Fourier identities were re-derived from the geometric-series calculation written above; no numerical Fourier transform is needed for their proof. All proof arithmetic is exact. The diagnostic trigonometric decimals are expressly excluded from the proof.

No repository, paper, web page, or other agent's work was consulted. The only non-brief reading was the Paperclip operational skill and its artifact instructions, outside /work. No sub-agent, SAT/ILP solver, random search, paid service, or outward publication was used. This is the only file written. Computation used Node with --single-threaded --v8-pool-size=1, one computation process at a time.

Cost: research and report verification ran from 2026-10-09 16:48:26 through 16:58:55 UTC, a wall time of 629 seconds (10 minutes 29 seconds). The discovery process used 1.714730 CPU seconds; the initial independent verifier used 0.031011; the Fourier diagnostic used 0.017807; the boundary-window diagnostic used 0.025561; and the final written-certificate replay plus independent correlation verification used 0.045505. Total measured mathematical-computation CPU: 1.834614 seconds, summing user and system CPU from Node's process.cpuUsage(). File editing and control-plane attachment/status operations are outside this computation measurement. No CPU-hour limit was approached.

Disposition: the requested lemma is false. The deliverable task is complete. The next mathematical action, if the coordinator chooses to continue, is to revise the statement in light of this explicit counterexample; no follow-up task or ongoing computation is claimed here.
