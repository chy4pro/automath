PASS

# Referee report: PROBE_ASTRA_6_20261009 (Erdős #1066, T5), round 4

Referee: referee-1 (isolated, adversarial). File reviewed: `PROBE_ASTRA_6_20261009.md` only, plus the target brief in the task. No other material read; no web.

Verdict: PASS. Every statement the report labels as proved is correct; I re-derived each step before reading the author's justification and found no gap, no circularity and no silently assumed lemma. The STATUS line is honest (PARTIAL, with the 13n/48 statement clearly conditional). All reported finite checks were reproduced exactly with independent code. Minor non-blocking remarks are listed in §4 below; none requires a repair.

## 1. Claim-by-claim verdicts

**Definitions.** Penny graph: pairwise distances ≥ 1, edges at distance exactly 1. Matches the brief. S = degree-6 vertices, T = rest, α_w weighted independence number. Consistent throughout.

**§1 (elementary facts, four-colour baseline).** VALID.
- |u−v|² = 2−2cos θ ≥ 1 ⇒ θ ≥ π/3; gaps sum to 2π ⇒ d ≤ 6; d = 6 ⇒ all gaps π/3 ⇒ regular unit hexagon. Re-derived.
- 3-degeneracy: a generic linear functional has a unique minimiser x; all neighbour directions lie in an open arc of length π; four neighbours would need three gaps ≥ π/3 totalling ≥ π, impossible in an open arc of length π. Re-derived. (This is the standard "penny graphs are 3-degenerate" fact; correctly not claimed as new.)
- Hence greedy 4-colouring of every induced subgraph; α_w ≥ w(P)/4. VALID.

**§2 (rigidity of degree-6 vertices, lattice components).** VALID.
- L_a = a + Zu + ZRu independent of the chosen neighbour: (u,Ru) ↦ (Ru, Ru−u) is unimodular. Re-derived.
- Adjacent degree-6 a,b: b ∈ L_a and both stars have the same six directions ⇒ L_a = L_b. Re-derived.
- Common neighbour x with d(x) ≤ 5: the identity x + R(a−x) − a = R⁻¹(x−a) was verified in complex notation (e^{iπ/3}−1 = e^{2πi/3} = −e^{−iπ/3}). So a's star forces the three points x + R^i(a−x), i ∈ {−1,0,1}, into N(x); same for b. Two 3-subsets of a set of size ≤ 5 meet ⇒ b−x = R^k(a−x) ⇒ same six directions, both lattices contain x ⇒ L_a = L_b. The case d(x) = 6 is handled by applying the adjacency case twice. Re-derived, no gap.
- Graph H on S (G-distance ≤ 2): each component C has one lattice L_C containing C and all G-neighbours of C (induction along H-paths). No G-edge between different H-components (distance 1 ≤ 2). All S-neighbours of a T-vertex lie in one H-component (they share x). All VALID; the remark that components of G[S] would be insufficient is correct.

**§3 (three-colouring, partition T₀/T₁/T₂, inequality (1)).** VALID.
- χ_C(au+bv) = a+2b mod 3. Unit vectors of the lattice are exactly the six listed ((a+b/2)²+3b²/4 = 1 ⇒ |b| ≤ 1); their increments of a+2b are ±1, ±2, −1, +1, all nonzero mod 3. Proper colouring. Re-derived.
- Well-definedness of q(x): origin change adds a constant; basis rotation u ↦ Ru gives (a,b) = (−b′, a′+b′) and χ = 2a′+b′ ≡ −(a′+2b′) mod 3, i.e. negation. Both permute the colour classes, so the number of distinct colours among S-neighbours is invariant. Every x ∈ T has a unique H-component of S-neighbours (or none), so q(x) ∈ {0,1,2} is a function on T and T₀, T₁, T₂ partition T. q(x) ≠ 3 because x ∈ L_C and neighbours of x in L_C avoid χ_C(x). VALID.
- Random colouring: independent uniform k_C per component; I is independent (same-colour lattice points are never at unit distance; no edges across components). Pr(v ∈ I) = 1/3 for v ∈ S. Survival of x ∈ T: T₀ always; otherwise iff k_C avoids the q(x) colours present, probability 1−q(x)/3 exactly. (5) holds for every outcome since U ⊆ T is disjoint from I and has no I-neighbours, and G[U] is an induced penny graph. Averaging (linearity only) gives (1). Re-derived: w(S)/3 + (1/4)Σ w(x)(1−q(x)/3) = w(S)/3 + w(T₀)/4 + w(T₁)/6 + w(T₂)/12. VALID.
- (2): 3t₀+2t₁+t₂ ≥ n−s ⇒ (4s+n−s)/12 = (n+3s)/12. Ceilings are legitimate since α is an integer. (6) re-derived: (4s+3t₀+2t₁+t₂)/12 = n/4 + (s−t₁−2t₂)/12. VALID.
- Conditional statement: s ≥ 3n/4 ⇒ (n+3s)/12 ≥ 13n/48; 13/48−6/23 = 11/1104 > 0. Thresholds "69s > 49n" and "s ≤ 2n/3 ⇒ max is n/4" re-derived. All VALID and the conditional nature is stated in the STATUS line, in the preamble ("The conditional statement is not a solution of the target") and in §6.

**§4 (family F_(W,H)).** VALID.
- Band distances: triangular (k−i+½)²+¾ (equality iff k ∈ {i, i−1}), square (k−i)²+1 (equality iff k = i); rows ≥ 2 apart separated by ≥ 1+√3/2; same row integer spacing. Packing condition and contact list re-derived.
- Degree formula (7) re-derived by hand (interior 2+2+1 = 5; each interior row has one endpoint of degree 3 and one of degree 4; top/bottom non-corners 4; corners 2,3,3,2) and verified by exhaustive computation for W = 2..9, H = 2,4,...,10 (see §3 below). Edge count (5WH−2W−3H)/2 verified. (8) follows.
- 3-colouring (row 2k: 2i, row 2k+1: 2i+1 mod 3): increments 2, ±1, −1. VALID. Triangle partition when 3 | W: in the interleaved order edges join positions 1 or 2 apart and every three consecutive positions are pairwise adjacent (checked all three pair types). So α = WH/3 (9). VALID and computationally confirmed.
- Curvature 1−5/2+3/3+2/4 = 0 and the 3-triangle/2-square face pattern around an interior vertex re-derived. VALID.

**§5 (weighted Caro–Wei).** VALID.
- Exponential-clock formula λ_v/(λ_v+Σλ_u) is standard; (10) correct.
- (11) re-derived symbolically and verified exactly for all W,H above. 53/240 at M = 4, monotone in M. VALID.
- (12): K = (W−4)(H−4) interior vertices with all-degree-5 closed neighbourhoods; term exactly 1/6 for any degree-only f; others ≤ 1. WH−K = 4(W+H−4) ⇒ (10/3)(W+H−4). VALID. At M = 72 the bound equals 1/6+5/54−(small) < 7/27 < 6/23; at M ≥ 80 it is < 1/4. Both onsets are correct as sufficient conditions (see remark in §4 below).
- Unrestricted rates give sup = α(G): VALID (rate M on a maximum, hence maximal, independent set).

**§6 (routes and obstructions).** All statements checked. Item 3's cross-star example (centres 0 and 3u; halo vertices u, 2u adjacent; selected together with probability 1/9 under per-star halo colouring) is correct; u and 2u are both present and at distance 1. Item 4's pentagon: 2 sin(π/5) ≈ 1.1756 > 1, valid penny graph, degree-5 centre, no triangle. Items 5–8 are correctly scoped (obstruction to the specific certificates, not to the conjecture).

**§7–§8 (finite checks, cost).** All table entries reproduced exactly (§3 below).

## 2. Errors found

None. No step uses a hypothesis before it is available; the only probabilistic step uses linearity of expectation only, as stated; the four-colour repair is applied to an induced penny graph, which is legitimate.

## 3. Independent re-checks (what I ran, what it gave)

Own python3 code (exact integer arithmetic; points as (X,A,B) meaning (X/2,(A+B√3)/2), contact iff U = 4, V = 0; distance ≥ 1 decided by sign of (U−4)+V√3 with the integer comparison (U−4)² vs 3V²; α by include/exclude recursion with memoisation). Total CPU about 7 s.

1. Rhombi R_1..R_6 and hexagonal patches B_0..B_2: n, edge count, s and exact α all agree with the report's first table (e.g. R_6: 36, 85, 16, 12; B_2: 19, 42, 7, 7). Degree histograms also recorded (R_m: two degree-2, two degree-3, 4(m−2) degree-4, (m−2)² degree-6).
2. Strips F_(W,H), W = 1..6, H ∈ {2,4,6}: all 18 triples (n, edges, α) agree exactly with the second table. 4α ≥ n and 12α ≥ n+3s hold in all cases.
3. Degree formula (7), edge count, and Caro–Wei sum (11): exhaustively verified for W = 2..9, H = 2..10 even: 0 mismatches. F_(3,4) has (n₂..n₅) = (2,4,4,2) and F_(6,6) has (2,6,12,16), as reported.
4. (9): α(F_(W,H)) = WH/3 confirmed for W ∈ {3,6}, H ∈ {2,4,6,8}.
5. Star unions (second table): I rebuilt H-components (G-distance ≤ 2 among degree-6 vertices), q(x) and (t₀,t₁,t₂):
   - (0,0),(1,0): n 10, s 2, 1 component, (0,6,2), numerator 22, α 4.
   - (0,0),(1,1): 12, 2, 1, (0,10,0), 28, 5.
   - (1,0),(0,1),(−1,1): 13, 3, 1, (0,7,3), 29, 5.
   - (0,0),(3,0): 14, 2, 2 components, (0,12,0), 32, 6.
   Exact agreement on every entry; 12α ≥ numerator in all four.
6. Random tests of (1) and (2) not in the report: 400 random subsets (8–30 points) of a 7×7 triangular rhombus, each with unit weights and with independent random integer weights in {0,...,5}; and 60 dense subsets of the radius-3 hexagonal patch (37 points minus 0–4 random points, s up to 19, t₂ up to 12). Asserted that all S-neighbours of a T-vertex lie in one H-component and no G-edge joins distinct components. 0 violations of (1), (2) or 4α ≥ n. Minimum ratio 12α/(4s+3t₀+2t₁+t₂) observed: 11/7.
7. Constants: 13/48−6/23 = 11/1104; 6/23−7/27 = 1/621; 6/23−8/31 = 2/713; 6/23−1/4 = 1/92; 53/240 < 1/4. Bound (12) divided by M²: 0.2618 at M = 68, 0.2592 at M = 70, 0.2567 at M = 72, 0.2521 at M = 76, 0.24994 at M = 78, 0.2479 at M = 80.
8. Nonvacuity of the hypothesis s ≥ 3n/4 (not addressed in the report): R_m has s/n = (1−2/m)², which is ≥ 3/4 for m ≥ 15 (R_15: 0.7511).

What I could not check: nothing substantive. The geometric lemmas of §2 were verified algebraically, not by exhaustive computation over non-lattice configurations (exact arithmetic over rotated lattices was not attempted); the hand derivation is complete.

## 4. Minor remarks (no repair required)

- §5: the stated onsets M ≥ 72 (below 6/23) and M ≥ 80 (below 1/4) are sufficient, not sharp; the bound (12) itself already falls below 6/23 at M = 70 and below 1/4 at M = 78. The report never claims sharpness, so this is not an error.
- The conditional theorem improves the brief's known 8n/31 only when s > 65n/93 ≈ 0.699n and beats 6n/23 only when s > 49n/69 ≈ 0.710n (hence the cleaner sufficient condition s ≥ 3n/4). The report states the 49/69 threshold; it could also state explicitly that the hypothesis excludes exactly the degree-5-dense regime that its own §4 identifies as the hard case.
- The report could note that the hypothesis s ≥ 3n/4 is nonvacuous (lattice rhombi with m ≥ 15).

## 5. Honest status

PARTIAL is correct and not dressed up. What is proved for all penny graphs is only α ≥ ⌈n/4⌉ (a known fact, correctly not claimed as new) and the lemma α ≥ ⌈(n+3s)/12⌉, which is a genuine, elementary, probably not new, but correctly proved statement. The 13n/48 bound is presented as conditional on s ≥ 3n/4 everywhere it appears. The obstructions in §4–§5 are explicitly scoped to the certificates examined. Nothing conditional is presented as unconditional and no bound weaker than 8/31 is presented as progress. The status is far from HIT: the proved regime (s ≥ 49n/69) is the easy, lattice-dominated regime.

## 6. Value

Usable lemmas: (i) the rigidity lemma of §2, that degree-6 vertices at G-distance ≤ 2 share one triangular lattice which also contains all their neighbours, is a clean, reusable ingredient for any discharging argument; (ii) inequality (1) with its explicit loss term (6), which quantifies exactly how much the lattice part contributes. Usable negative results: the triangle–square strip family F_(W,H) (s = 0, α = n/3, zero combinatorial curvature at every interior vertex, only 4M−4 vertices of degree ≤ 4) shows that degree-only Caro–Wei certificates cap at about n/6 and that discharging cannot force a positive density of non-degree-5 vertices from the packing hypothesis alone. The exact remaining obstruction is the degree-5-dense regime (s = o(n)) where no Euclidean rigidity is available: there the report's certificates give exactly n/4, and a selection or reducible-configuration argument giving c > 6/23 on such graphs is entirely missing.
