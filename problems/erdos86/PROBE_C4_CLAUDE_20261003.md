CLEAN-ROOM PROBE (Claude Opus, 2026-10-03). The agent could not write this file itself; the coordinator saved its returned text verbatim. Code in ./code (certificate data cert_m2.pkl included; the 8 MB column data res_m2.pkl is not stored — regenerate with q4lp2.py).

STATUS: PARTIAL — proved c = 0.6066083 (computer-assisted, exact-arithmetic certificate). This does NOT beat the published 0.60318. The best fully human-readable bound obtained is c = 0.6258161 (root of θ³+6θ−4), resting on one exhaustively verified Q4 lemma. No HIT.

# Erdős #86 (C4-free subgraphs of Q_n): clean-room probe, 2026-10-03

Notation. G ⊆ Q_n is C4-free. D(v) ⊆ [n] is the set of directions of G-edges at v, d_v = |D(v)| and δ_v = d_v/n. The density is ρ_n(G) = e(G)/(n2^{n−1}) = E_v δ_v. For H ⊆ Q_k, a_m(H) is the number of vertices of degree m in H.

Basic identity. For a k-subcube C = v + span(S): deg_{G∩C}(v) = |D(v) ∩ S|. Hence
  Σ_{k-subcubes C} Σ_{v∈C} f(deg_{G∩C} v) = Σ_v Σ_{|S|=k} f(|D(v)∩S|).
For fixed v the inner average is Hyp(n, d_v, k), which equals Bin(k, δ_v) + O(k²/n) uniformly.

## 1. Results proved

### Theorem 1 (folklore level): ex(Q_n,C4) ≤ (2n+1)·2^{n−1}/3, so π₄ ≤ 2/3.
Proof. Call a pair of G-edges at a common vertex a *cherry*. Each cherry spans a unique square. A square with 3 G-edges has 2 cherries, one with 2 adjacent G-edges has 1, and all others (at most 3 edges) have 0. Let s_t be the number of squares with t G-edges. Then
  Σ_v C(d_v,2) = 2s_3 + s_{2,adj} ≤ (2/3)(3s_3 + 2s_{2,adj}) ≤ (2/3)Σ_t t·s_t = (2/3)(n−1)e(G).
Write d̄ = e(G)/2^{n−1}. Jensen gives Σ_v C(d_v,2) ≥ 2^n d̄(d̄−1)/2, so d̄ ≤ (2n+1)/3. Tight at n = 4 (24 edges). ∎

### Lemma A (Q3): a C4-free H ⊆ Q3 has at most 2 vertices of degree 3.
Proof. Two degree-3 vertices at distance 2 lie on a common face whose 4 edges are all present, a C4. So pairwise distances are in {1,3}. An adjacent pair leaves no room for a third vertex: its distances to two adjacent vertices have different parity. If all distances are 3, each vertex has a unique antipode. ∎ (Confirmed over all 2902 C4-free subgraphs of Q3.)

### Theorem 2: π₄ ≤ 4^{−1/3} = 0.629960…
More precisely, if d̄ ≥ 2 then d̄(d̄−1)(d̄−2) ≤ n(n−1)(n−2)/4.
Proof. Σ_v C(d_v,3) = Σ_{Q3-subcubes} a_3(G∩C) ≤ 2·C(n,3)·2^{n−3} by Lemma A. Then apply Jensen to the convex function f(x) = C(x,3)·1[x≥2]. ∎
This is exactly the optimum of the Q3 degree-histogram/Bin(3)-mixture LP.

### Lemma B (Q4; exhaustive verification): every C4-free H ⊆ Q4 satisfies a_1 + a_2 ≥ 3a_4.
Checked over all 1,226,436,381 C4-free subgraphs of Q4, via their 828 distinct degree histograms. Two independent codes agree (hist.py and check_enum.py).
Equality holds for 14 histograms with a_4 > 0, e.g. (0,0,6,8,2), (0,0,12,0,4), (0,12,0,0,4), (8,6,0,0,2). No hand proof found.

### Theorem 3: π₄ ≤ θ, where θ is the real root of θ³+6θ−4 = 0, θ = ∛(2+2√3) − ∛(2√3−2) = 0.6258161…
Proof. Apply the basic identity with k = 4 and f(m) = 3[m=4] − [m=1] − [m=2]. By Lemma B:
  Σ_v [3C(d_v,4) − d_v C(n−d_v,3) − C(d_v,2)C(n−d_v,2)] ≤ 0.
Divide by 2^n C(n,4) to get E_v g(δ_v) ≤ O(1/n), where
  g(δ) = 3δ⁴ − 4δ(1−δ)³ − 6δ²(1−δ)² = δ⁴ + 6δ² − 4δ = δ(δ³+6δ−4).
g'' > 0, so g(ρ) ≤ O(1/n). Since g < 0 on (0,θ) and g > 0 on (θ,1], ρ ≤ θ + o(1). ∎
This is the exact optimum (0.6258162) of the LP using the full Q4 degree-histogram polytope with Bin(4)-mixture constraints. Lemma B is its dual certificate, with weights (0,−1,−1,0,3). So no better bound comes from degree information in Q4.

### Theorem 4 (computer-assisted; exact rational certificate): π₄ ≤ 0.6066083
Exactly: π₄ ≤ 121321659/200000000 + c₁, with c₁ < 1.85·10⁻⁹ rigorous.

Definitions. Fix a C4-free H ⊆ Q4. Take an edge e of Q4 (present or not) in direction i, with endpoints u (bit i = 0) and v. For another direction j, the square type is
  τ_j(e) = 1[uu+e_j∈H] + 2·1[vv+e_j∈H] + 4·1[(u+e_j)(v+e_j)∈H] ∈ {0..7}.
Let s_e = 1[e∈H]. Let N^s(H) ∈ R^{8×8} be the average, over:
- the 32 edges e,
- the 2 orientations (u↔v swaps bits 0 and 1 of τ),
- the 6 ordered pairs (j,l) of distinct other directions,
of 1[s_e = s]·E_{τ_j(e),τ_l(e)}. Also H_m = a_m/16 and ρ(H) = e(H)/32.

Certificate.
- w = 10⁻⁹·(−2866080, 3829617, −4664328, 5022509, −4929686).
- Y⁰ and Y¹ as in §4, both verified PSD by exact rational LDLᵀ.

Checks.
 (i) For all C4-free H ⊆ Q4: ρ(H) − Σ w_m H_m + Σ_s⟨Y^s, N^s(H)⟩ ≤ c₀ = 121321659/200000000.
     Verified in exact int64 arithmetic over all 13,242,015 representatives, which cover every isomorphism class. The functional is Aut(Q4)-invariant. The maximum is attained by the empty graph.
 (ii) Σ_m w_m C(4,m)δ^m(1−δ)^{4−m} ≤ c₁ on [0,1], by exact rational Bernstein subdivision.

Proof. Average (i) over all Q4-subcubes of Q_n.
- E[ρ(H)] = ρ_n.
- E[H_m] = E_v Bin(4,δ_v)(m) + O(1/n), which is controlled by (ii).
- A random Q4 containing edge e, with a random ordered pair of its other directions, gives a uniform ordered pair of distinct directions ≠ i. So E N^s = E_{e,orient}[1[s_e=s] p_e p_eᵀ] + O(1/n), where p_e is the empirical square-type distribution at e. This is PSD up to O(1/n).
Hence ρ_n ≤ c₀ + c₁ + O(1/n). ∎

(In flag-algebra terms: Q4 consistency plus one Cauchy–Schwarz on edge-rooted square flags. It is a sub-relaxation of a Q4 flag-algebra computation.)

## 2. Exhaustive enumeration results

| k | e(Q_k) | # C4-free subgraphs (labelled) | ex | density | # labelled extremal | structure |
|---|---|---|---|---|---|---|
| 2 | 4 | 15 | 3 | 0.75 | 4 | path P4 |
| 3 | 12 | 2,902 (99 Aut-orbits) | 9 | 0.75 | 8 | Q3 minus 3 edges in 3 distinct directions, one per face. Degrees (3,3,2⁶); the degree-3 vertices are antipodal. |
| 4 | 32 | 1,226,436,381 | 24 | 0.75 | 8 (1 orbit) | 3-regular. The missing perfect matching meets each of the 24 squares exactly once (forced by equality in Thm 1). |
| 5 | 80 | not counted | 56 (no 57; 56 attained) | 0.70 | not counted | — |

Q4 counts by number of edges (labelled): 0:1, 1:32, 2:496, 3:4960, 4:35936, 5:200704, 6:897120, 7:3287328, 8:10029480, 9:25723136, 10:55739072, 11:102159936, 12:157982000, 13:204855968, 14:220449792, 15:193877952, 16:136352716, 17:74390848, 18:30170096, 19:8558976, 20:1553936, 21:158144, 22:7552 (30 orbits), 23:192 (1 orbit), 24:8 (1 orbit).

Method for Q4. Q4 = Q3×K2. A C4-free subgraph is (A, B, M): A and B are C4-free in the two Q3 layers, and M (the vertical edges present) is an independent set of A∩B.

Method for Q5. The same decomposition over Q4 gives max |M| = α(A∩B) = 16 − ν(A∩B), by König.
- 57 edges would need |A|+|B| − ν ≥ 41.
- ν ≥ (|A|+|B|−32)/4, so |A|+|B| ≥ 44 and |A|,|B| ≥ 20.
- All 1,719,832 labelled Q4 graphs with ≥ 20 edges were listed. A ran over orbit representatives of the larger class and B over all labelled graphs; α was computed exactly.
- The maximum is 56. An example pair as Q4 edge masks: (2128557822, 3979135359).
Counting extremal Q5 graphs would need about 1.4·10⁹ more pairs and was not done. Q6 was not attempted.

## 3. Relaxation hierarchy (numerical; only Theorems 1–4 are certified)

| relaxation | value | status |
|---|---|---|
| Q2 degrees + Bin(2) mixture | 2/3 | proved (Thm 1) |
| Q3 degree histograms + Bin(3) | 0.6299605 | proved (Thm 2) |
| Q4 degree histograms + Bin(4) | 0.6258162 | proved (Thm 3) |
| Q3 distribution + Bin(3) + edge-rooted square-type 2nd-moment PSD | 0.606794 | float, not certified. Equals the published 0.6068 to the displayed digits (source not consulted). |
| same + coupled Q4 degree histograms | 0.606794 | no change; the Q4 constraint is not binding |
| Q4 distribution (column generation over all Q4) + Bin(4) + same PSD | LP 0.6066073; certified 0.6066083 | proved (Thm 4) |
| Q4 + vertex-rooted pair flags (18×18) + 3rd-order edge localising + square-rooted prism flags (256 types) | not converged | — |

## 4. Certificate data for Theorem 4 (10⁹·Y^s; τ = b_u + 2b_v + 4b_top)
Y⁰·10⁹:
[  603742215  -426827875  -426827875  -648745732   335302466  -200241688  -200241688    45537936]
[ -426827875  1942745550 -1141725011   494964819  -181209042  1105799294  -725432575  -105624871]
[ -426827875 -1141725011  1942745550   494964819  -181209042  -725432575  1105799294  -105624871]
[ -648745732   494964819   494964819   710542220  -339738576   233049329   233049329   -75941402]
[  335302466  -181209042  -181209042  -339738576   217828159   -83721284   -83721284   -16232625]
[ -200241688  1105799294  -725432575   233049329   -83721284   909974109  -729239818   -51272511]
[ -200241688  -725432575  1105799294   233049329   -83721284  -729239818   909974109   -51272511]
[   45537936  -105624871  -105624871   -75941402   -16232625   -51272511   -51272511    58056151]
Y¹·10⁹:
[ 1797387916   308269851   308269851 -1322352593   174259341   418600442   418600442  0]
[  308269851   938391070  -832545744  -227341958    26372746   350030578  -205853626  0]
[  308269851  -832545744   938391070  -227341958    26372746  -205853626   350030578  0]
[-1322352593  -227341958  -227341958   978771253   -90000042  -311159493  -311159493  0]
[  174259341    26372746    26372746   -90000042   264697436    19917104    19917104  0]
[  418600442   350030578  -205853626  -311159493    19917104   187648337    10783052  0]
[  418600442  -205853626   350030578  -311159493    19917104    10783052   187648337  0]
[          0           0           0           0           0           0           0  0]
(Type 7 with s = 1 would be a C4, so it never occurs.)
Reproduce: `q4lp2.py M2 m2 200 420 12 800`, then `verify.py m2` (about 20 s).

## 5. Routes that failed, with exact obstructions
1. Pure subcube averaging / compatibility of extremal Q_k's. The LP value is exactly ex(Q_k)/e(Q_k): 3/4, 3/4, 7/10 for k = 3, 4, 5, because the symmetrised extremal graph is always feasible. "Compatibility" across overlapping Q_k's is just averaging at level k+1. For example, two parallel extremal Q4 layers allow α(A∩B) ≤ 8, giving 56. So the route is capped near 0.7 for computable k. The Jensen/regularity step is the essential ingredient.
2. Degree information only, k ≤ 4. Exact optima are 2/3, 0.62996 and 0.62582. At k = 4 the optimum is near-regular, with Bin(4, 0.6258) a convex combination of the realisable histograms (0,0,6,8,2), (0,0,12,0,4), (0,8,4,0,4), (1,5,4,3,3), all tight for Lemma B.
3. Q3 edge-rooted Cauchy–Schwarz stalls at 0.606794, the known bound. Adding Q4 degrees has no effect.
4. Adding Q4 consistency (Thm 4) gains only 1.9·10⁻⁴.
5. The full Q4 relaxation (essentially a flag-algebra SDP), done as LP column generation with eigenvector cuts in numpy/scipy, did not converge. It became unstable after column pruning and was stopped at round 6. No SDP solver was available. I make no claim about its value.
6. No hand proof of Lemma B was found. Partial facts: degree-4 vertices are pairwise at distance ≠ 2, and every vertex at distance 2 from a degree-4 vertex has degree ≤ 3.

## 6. Assessment
- Target not reached: no c < 0.60318.
- Human-readable bounds (2/3, 0.62996, 0.62582) are all weaker than the known 0.6068.
- The only bound below 0.6068 is computer-assisted (0.60661, exact certificate) and is weaker than the 2012 result.
- No cross-model check and no formalisation were done.

## 7. Cost
- Single agent, no web, no repository files read.
- numpy/scipy (HiGHS LP) on at most 2 threads; no SAT/ILP.
- About 40–50 CPU-minutes, of which about 30 went to Q4 column-generation attempts (two abandoned). Theorem 4 plus its verification took under 1 minute. Wall time about 1.5 h.

## Appendix: code
Files: cube.py, q4.py, q4counts.py, hist.py, check_enum.py, k3edge.py, k3q4.py, q4enum.py, q4lp2.py, q5.py, verify.py — to be attached verbatim.
