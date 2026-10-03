DONE — core theorems PASS; overall PASS-WITH-REPAIRS. Novelty PARTIALLY KNOWN. Recommend a repository note, with the general two-ring admissibility claim left OPEN.

# Erdős #1082: adversarial referee and bounded G2 check

Date: 2026-10-03 UTC. Task 046. Input: PROBE_DISTANCES_CLAUDE_20261003.md. Two informed reused workers divided the geometric proofs and the two-ring construction; the root rederived the main count and performed exact finite checks. These reviewers are one vendor, different from the Claude probe; no kernel formalization or independent-vendor replay of the numerical checks occurred.

## Decisions

Throughout, P is a set of n>=3 distinct planar points with no three collinear, h is its number of hull vertices, M(p) counts positive distances from p to P\{p}, and M=max_p M(p). Theorem 4 separately extends to n=2. No claim below extends the ceiling bound to n=1.

| Statement | Referee verdict | Bounded novelty verdict |
|---|---|---|
| Lemma 1 and exact defect identity, Proposition 2 | PASS | PARTIALLY KNOWN: algebraic repackaging of the classical double count; exact presentation not located |
| Lemma 3: enclosing disks through >=3 points, count <=h-2 | PASS | KNOWN: classical farthest-point Delaunay face count |
| Lemma 3': exact-two-boundary pairs <=2h-3 | PASS, specify proper crossings | KNOWN geometric ingredient; center-count application elementary |
| Theorem 4's hull-sensitive average bound | PASS | PARTIALLY KNOWN: follows from old geometric/counting ingredients; exact formula not located |
| Theorem 4: M>=ceil(n/3), n>=2 | PASS | PARTIALLY KNOWN: immediate consequence of the old equality count plus diameter-graph theorem; explicit earlier pinned ceiling statement not unambiguously located |
| Corollary 5: n divisible by 3, h<(n+16)/10 implies M>=n/3+1 | PASS | PARTIALLY KNOWN: exact statement not located |
| Two-ring distance merges for every 4 divides k | PASS | PARTIALLY KNOWN construction method; k=4 is KNOWN |
| No three collinear for every 4 divides k | FAIL as a completed proof; mathematically OPEN here | Floating tests do not establish the universal claim |
| Restricted two-ring family k=2^s, s>=2 | PASS after adding the proof below | Exact norm argument not located; no priority certification |
| Broad obstruction/equivalence claims in §§2,5 | PASS-WITH-REPAIRS only after the listed deletions | Finite examples do not establish the claimed general barriers |

No positive coefficient improvement beyond 1/3 has been proved. No item receives a certified NEW verdict from this bounded search.

## Defect identity and hull bounds

Let the distance-class sizes at p be a_i(p), let V_p=sum_i(a_i(p)-3)^2, and let A(p)=sum_i binom(a_i(p),2). Bases and apexes use unordered pairs; a base has at most two apexes because its perpendicular bisector contains at most two points of P. Let Z_j count bases with j apexes.

Expanding each square gives
\[
 2A(p)=5(n-1)-9M(p)+V_p.
\]
The independent apex/base count is
\[
 \sum_p A(p)=Z_1+2Z_2=n(n-1)-Z_1-2Z_0.
\]
Therefore, exactly,
\[
 9\sum_pM(p)=3n(n-1)+D(P),\qquad
 D(P)=\sum_pV_p+2Z_1+4Z_0.
\]
All terms are nonnegative. In particular D>=9 delta n^2 is sufficient for the stated average bound. Conversely M<=(1/3+epsilon)n implies D<=9epsilon n^2+3n. This latter implication is a necessary structural condition, not an equivalent formulation of the original coefficient target.

**Lemma 3.** Every point of P on the boundary of an enclosing disk is an exposed hull vertex: the tangent supporting line to a strictly convex disk meets it in one point. Every relevant disk is determined by a noncollinear triple, so there are finitely many.

For distinct enclosing disks, subtraction of their power functions is a nonconstant affine function; coincident centers with different radii are impossible when each disk has boundary points in P. The affine function is nonnegative on the first boundary polygon and nonpositive on the second. Their interiors are disjoint. At each hull vertex their interior angle sectors are disjoint and lie inside the hull angle. Thus the stronger inequality holds:
\[
 \sum_D(|\partial D\cap P|-2)\le h-2.
\]
It implies the claimed count. This proof permits four or more cocircular points; no perturbation is used.

**Lemma 3'.** For two exact-two-boundary disks the same affine separation prevents proper crossings of the corresponding chords. A proper crossing would force both chords onto the radical axis, contradicting no three collinear points. The graph is therefore noncrossing on h vertices in convex position and has at most 2h-3 edges. Shared endpoints are allowed. A pair is the farthest class of at most two centers in P, again by the perpendicular-bisector condition.

**Theorem 4.** Distinct centers p give distinct enclosing disks D(p,R(p)). At most h-2 centers can have a farthest class of size three. Every other center contributes at least one to V_p. Consequently
\[
 D(P)\ge n-h+2,\qquad
 \frac1n\sum_pM(p)\ge\frac{n-1}{3}+\frac{n-h+2}{9n}.
\]
Since n-h+2>=2, M>(n-1)/3 and M>=ceil(n/3). For n=2, M(p)=1 and the displayed average inequality holds directly.

**Corollary 5.** Put m=n/3 and assume M<=m. Define W_p=V_p+9(m-M(p)). The identity gives
\[
 \sum_pW_p+2Z_1+4Z_0=3n.
\]
If M(p)<m then W_p>=9. If M(p)=m then the class deviations sum to -1, so V_p>=1; a singleton farthest class contributes 4 and forces other deviations summing to +1, hence V_p>=5. Therefore
\[
 W_p\ge1+4\mathbf1_{\{|F(p)|=1\}}.
\]
Lemmas 3 and 3' give at least n-5h+8 singleton farthest classes, whence 3n>=n+4(n-5h+8). This is exactly h>=(n+16)/10, proving the corollary.

## Two concentric polygons: what is proved

Let theta=pi/k, 4 divide k, c=cos(theta), rho=sqrt(1+c^2)-c, and take outer vertices exp(2ij theta) and inner vertices rho exp(i(2j+1)theta). Then rho^2+2c rho=1 and 0<rho<1.

There are k/2 same-ring and k/2 cross-ring distances before overlaps. The outer squared chord of index k/4 equals 2, and its cross-ring value at angle pi-theta is 1+rho^2+2rho c=2. The inner squared chord is 2rho^2 and matches the cross-ring value at angle theta. Thus M<=k-1. This proves an upper bound, not equality; additional merges have not been excluded.

**Exact collinearity criterion.** A line through outer vertices with indices a,b has equation
\[
 \operatorname{Re}(z e^{-i(a+b)\theta})=\cos((a-b)\theta).
\]
An inner vertex lies on it precisely when
\[
 \rho\cos((2j+1-a-b)\theta)=\cos((a-b)\theta).
\]
The cosine indices have opposite parity. The analogous inner-inner-outer equation has the same property. They cannot both vanish, since a zero index is congruent to the even number k/2 modulo k. Taking absolute values and reducing indices preserves parity. Hence a collinear mixed triple exists if and only if
\[
 \rho=\frac{\cos(u\pi/k)}{\cos(v\pi/k)},\qquad
 0\le v<u<k/2,\quad u-v\ {\rm odd}.
\]
For sufficiency take a=u,b=0,j=(u+v-1)/2 modulo k. Triples on one circle cannot be collinear.

**Complete proof for k=2^s, s>=2.** Put zeta=exp(i pi/k), K=Q(zeta), and alpha_j=zeta^j+zeta^(-j). The field degree is k. A collinearity would put rho=alpha_u/alpha_v in K. Its monic equation rho^2+alpha_1 rho-1=0 makes it integral; rho^(-1)=rho+alpha_1 is also integral. Thus rho is a unit, with absolute norm 1.

On the other hand alpha_j=zeta^(-j)(1+zeta^(2j)). For odd j its absolute norm in K is 4, since Phi_k(-1)=2 and [K:Q(zeta^(2j))]=2. For nonzero even j<k/2, writing t=v_2(j)<=s-2 gives
\[
 |N_K(\alpha_j)|=2^{2^{t+1}}\ge16.
\]
For j=0 the norm is 2^k>=16. Opposite-parity indices therefore have unequal absolute norms, contradicting that their ratio is a unit. This proves the admissible infinite family
\[
 n=2^{s+1},\quad M\le n/2-1,\qquad s\ge2.
\]

For k with odd factors, this norm distinction no longer excludes all ratios. We found neither a universal proof nor a counterexample. The all-4-divides-k admissibility claim remains OPEN. Do not infer M=n/2-1 or D~1.5n^2 merely from the proved upper bound.

## Necessary repairs elsewhere in the probe

1. Restrict the status-line ceiling statement to n>=2. At n=1 it is false.
2. The reciprocal inequality bounds the harmonic mean from below: H>=(n-1)/3.
3. “Equality in Szemerédi's bound” must mean equality in the unrounded real bound (n-1)/3. Equality in its rounded integer version occurs in other residue classes.
4. At K=ceil(n/3), the slack 9nK-3n(n-1) is 3n,9n,6n for residues 0,1,2, respectively. The post-Corollary values 2n and 3n are wrong; delete the accompanying unsupported “one extra unit” obstruction.
5. Saturation at n=8 does not rule out a deficient-base bound valid for all sufficiently large n. Neither of the examples establishes V=o(n^2): both suppress the base deficit, and the polygon-plus-center example has V=Theta(n^2).
6. Few exceptional classes do not imply small sum(a_i-3)^2: one large class may contribute Theta(n^2). Remove the final “equivalently” and retain the weighted sufficient condition and necessary near-extremal condition.
7. The origin-centered example in §2.4 verifies only its local class/bisector statements, not all the preceding link and circumcenter consistency conditions. “Locally consistent at every single point” is too broad.
8. “Any weighting is subsumed,” “any inequality that P_k satisfies,” and a general circle-depth barrier inferred from finite tests are unsupported. The valid harmonic-mean statement only precludes improving its own leading constant using that scalar bound.
9. The no-four-cocircular qualifications cannot be silently imposed on the original problem. Numerical circle-depth observations remain empirical.
10. Small-n entries n=6 and n=9 are stale: published locally-few-distance classifications give exact pinned minima 3 and 4, respectively. Do not spend an algebraic-elimination campaign re-proving those cells.

## Literature and publication decision

The established isosceles double count and integer balancing appear in [Erdős 1975, pp.100–101](https://users.renyi.hu/~p_erdos/1975-25.pdf), [Nivasch–Pach–Pinchasi–Zerbib, §2](https://arxiv.org/pdf/1207.1266v2), and [Sheffer, Lemma 3.1](https://arxiv.org/pdf/1406.1949). The exact defect presentation was not located. The old paper's rounded notation is not used here as an unambiguous citation of the precise pinned ceiling statement.

The enclosing-circle geometry is classical: [Eppstein's primary report, §§1–2](https://ics.uci.edu/~eppstein/pubs/Epp-TR-90-45.pdf) describes farthest-point diagrams on hull vertices, enclosing-circle faces, and polygonal faces when points are cocircular. The two counts follow by elementary planar counting. We located no explicit prior source for this exact hull-average inequality or Corollary 5; this does not establish priority.

There is also a shorter derivation of pinned rounding from classical facts. If M=(n-1)/3, equality forces every local class to have size three. Let Q be the nonisolated support of the global diameter graph. Every vertex in Q has exactly three diameter neighbors, all in Q. Its diameter graph thus has 3|Q|/2 edges, contradicting the planar diameter-edge bound e<=|Q| recorded in [Erdős 1975, p.102](https://users.renyi.hu/~p_erdos/1975-25.pdf). This is our direct consequence, not an identified earlier explicit statement.

The [day report](https://erdosproblemaday.com/report/1082) gives a related GLOBAL-distance rounding argument and says it does not improve the pinned bound. Restricting to the active diameter support repairs that limitation. The complete [live forum thread](https://www.erdosproblems.com/forum/discuss/1082) was read during the immediately preceding dossier045; its December 2025 construction has 42 points on two concentric 21-gons with M=20. No relevant source was inferred from empty proof-claim counts.

The eight-point configuration is KNOWN: [Fishburn 2002](https://doi.org/10.1016/S0012-365X(01)00134-0), following the earlier counterexample. The exact current power-of-two construction proof was not located. [Nozaki–Shinohara, Propositions 4.16 and 4.18](https://arxiv.org/html/0906.0199) supplies the locally-few-distance cardinality bounds underlying the corrected small-n cells; the known typographical indexing issue in Proposition 4.18 is recorded in dossier045.

Recommendation: keep a corrected repository note containing the exact defect bookkeeping, hull refinements, and proved restricted family. Do not issue a Zenodo record-improvement note now: the geometric ingredients are classical, the headline rounding is a short consequence of them, and the exact hull refinements lack targeted priority clearance. The main coefficient target remains OPEN. No external posting is authorized by this report.

## Actual exact checks and reproducibility

The root ran two sequential dependency-free Node processes with BigInt arithmetic; no numerical tolerance, external solver, files, or dependencies were used.

- Checked 4639 admissible subsets of four fixed pools: the probe's eight coordinates after scaling by 2 in Z[sqrt(3)]; the 3x3 integer grid; {(j,j^2):0<=j<=7}; and the twelve integer points on x^2+y^2=25. Every subset of cardinality >=3 was enumerated and rejected if a cross product vanished.
- Accepted counts for sizes 3 through 12: 408,713,932,982,808,497,220,66,12,1. Overlap between pools was not deduplicated; these are test instances, not distinct similarity classes.
- Every accepted instance satisfied the exact identity, D>=n-h+2, M>=ceil(n/3), farthest-class counts, and Corollary 5 whenever its hypothesis applied.
- The eight-point witness has h=4, M(p)=3 with sizes (4,2,1) at all points, V=48, Z=(0,0,28), D=48. This independently reproduces its stated exact claims.
- In a separate check over all 4420 accepted subsets of the three integer pools, every circumcircle through a triple was represented by primitive integer coefficients of A(x^2+y^2)+Bx+Cy+D=0 with A>0. Containment was checked exactly and duplicate circles removed.
- Across those instances: 4817 distinct-per-instance enclosing circles, 26465 exact-two-boundary pairs, and maximum boundary multiplicity 12. Both count bounds and sum_D(|boundary|-2)<=h-2 passed, including degeneracies.
- For an exact-two-boundary pair a,b, centers are (a+b)/2+t perp(b-a). Strict containment of each other q is the rational open half-line inequality (q-a) dot (q-b) < 2t cross(b-a,q-a). The intersection is nonempty exactly when its rational lower endpoint is smaller than its upper endpoint. This checks existence of such a disk without numerical optimization.
- For quadratic coordinates, multiplication is (a,b)(c,d)=(ac+3bd,ad+bc). Exact signs follow by comparing a^2 and 3b^2 when the terms have opposite signs. Final RSS was 75,558,912 bytes for the first process and 62,345,216 for the second; peak RSS and billing were not measured.

Finite checks support implementation and edge-case confidence; the universal conclusions above rest on the written proofs.

