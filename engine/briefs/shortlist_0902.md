# SHORTLIST 09-02 (Plan A reselection, Fable 5.1) — for the owner to pick TWO (one per slot)
Rule applied: source read + statement pinned verbatim → attention evidence → G2 before any engine hour.
Source of truth: teorth/erdosproblems data/problems.yaml (1217 problems) + erdosproblems.com pages + the cited notes.

## SLOT 1 candidates (high value, uncertain)

### S1-A  Erdős #835 — chromatic number of the Johnson graph J(2k,k), residual k+1 prime
STATEMENT (verbatim, Ma–Tang Problem 1.3 / erdosproblems.com/835): does there exist k > 2 such that
χ(J(2k,k)) = k+1?  Equivalently: can the k-subsets of [2k] be (k+1)-coloured so that every (k+1)-subset
contains all k+1 colours?
KNOWN: false for 3 ≤ k ≤ 8 (computed chromatic numbers); Ma–Tang (note, 2025, 4 pp.) prove χ > k+1 whenever k+1
is composite, by a pure counting/packing argument (each colour class must be a maximum independent set of size
C(2k,k)/(k+1) = Catalan(k), forcing t | C(k+t, t−1) for all t ≤ k; Lucas kills composite k+1). They show the same
divisibilities all HOLD when k+1 is prime, so counting cannot decide the residual.
RESIDUAL: k ∈ {10, 12, 16, 18, 22, …}. First open case k = 10: J(20,10), 184,756 vertices, an 11-colouring would be
11 disjoint "perfect" families of size 16,796 each hitting every 11-subset exactly once.
ATTACK SURFACE (LLM): (i) construct such a colouring for k = p−1 using the F_p structure (each class = a set of
k-subsets meeting every (k+1)-subset exactly once — a design-like object); (ii) or prove a new necessary condition
beyond counting (eigenvalue/LP/design-theoretic) that kills k+1 prime. Both directions are legitimate progress.
VERIFICATION: any claimed colouring is checked by a trivial script; any impossibility proof is elementary
combinatorics, Lean-formalisable (statement already in formal-conjectures as erdos_835).
ATTENTION: Erdős 1974; site activity 2025 (Ma–Tang, Bhavik Mehta); G2 (arXiv, 09-02): nothing on the residual.
PRACTICALITY: low (extremal set theory). Honest odds: a construction for k=10 is a real gamble; a sharper necessary
condition is more likely and still publishable as "Erdős #835: the prime case".

### S1-B  Erdős #1212 — infinite path in the visible-lattice-point graph with a composite coordinate at every vertex
STATEMENT (verbatim, erdosproblems.com/1212): G has vertex set {(x,y) ∈ N² : gcd(x,y)=1}, edges join pairs differing
by ±1 in one coordinate. Is there a path going to infinity all of whose vertices (x,y) have min(x,y) > 1 and at
least one of x, y composite?  (Follow-up on the page: can the path be monotone with bounded runs?)
KNOWN: only the weak version (min(x,y) > 1) is settled — Stewart's path through consecutive-prime pairs, valid for
k ≥ 4 by p_{k+2} < 2p_k. Those vertices are prime–prime, i.e. FORBIDDEN in the strengthened version. No recorded
progress on the strengthened question (added April 2026).
MY MACHINE EVIDENCE (09-02): restricted graph in an N×N box — N=600: largest component 3,444 vertices, none
touching the far edge; N=2000: a giant component of 329,016 vertices (39% of valid vertices) touching the far edge
and spanning x∈[153,1974], y∈[1064,2000]. Valid-vertex density 0.5742 → 0.5850 → limit 6/π² ≈ 0.608, which is
ABOVE the Z² site-percolation threshold 0.5927. Heuristic answer: YES, an infinite path exists; the near-origin region
is enclosed (component of 42 vertices), so the path must start far out.
ATTACK SURFACE (LLM): explicit constructive proof — a staircase of short horizontal/vertical runs at composite
"rails" chosen by CRT so that compositeness comes from the other coordinate and coprimality from residue choice;
only elementary facts needed (no unproved prime-gap input). Machine search for the giant component's corridor
structure feeds the construction.
VERIFICATION: the construction is an explicit infinite family; every finite prefix is machine-checked; the invariant is
a short lemma, Lean-formalisable.
ATTENTION: Erdős 1980 (he paid $25 for the weak version); fresh database entry; G2 (arXiv): nothing.
PRACTICALITY: low. Honest odds: the best of the three — likely solvable; risk is that it is "too easy" and counts as
a minor entry; still a recorded Erdős-problem resolution.

### S1-C (reserve)  Erdős #1109 / #1103 — sets with A+A squarefree
f(N) = max |A ⊆ [N]| with A+A squarefree: Konyagin (log N)² loglog N ≪ f(N) ≪ N^{11/15+o(1)}; Tao is active on the
infinite analogue (#1103, van Doorn–Tao 2025). Attack = new constructions (lower bound) with machine-verified finite
instances. Highest attention of the three, hardest; kept as reserve.

## SLOT 2 candidates (high certainty)

### S2-A  Erdős–OEIS linkage programme (certain, verifiable, practical, modest)
The database flags 324 problems as "possibly related to an OEIS sequence not yet listed". Example with NO OEIS entry
at all (checked 09-02): #1189 irreducible covering sets — I(k) = number of irreducible covering sets of size k,
min/max n_k, max Σ1/n_i. Deliverable per problem: exhaustive computation with certificates, OEIS submission,
PR to teorth/erdosproblems. Value: upstream-visible in Tao's project, OEIS is infrastructure (practical), zero risk.
Not a theorem. Recommended as the slot-2 baseline: 3–5 problems in the first batch.

### S2-B (rejected after reading) the 16 "reduced to a finite computation" problems
All are "proved for sufficiently large n" with non-explicit thresholds or search problems without feasibility evidence
(details in selection_scan_0902.md). Not certain, not selected.

## Recommendation
Slot 1: S1-B (#1212) first — highest probability of a clean, recorded Erdős-problem resolution within days; S1-A
(#835) as the second slot-1 line if S1-B closes quickly. Slot 2: S2-A batch starting with #1189.
Cost estimate before any engine hour: S1-B = 1 Pro campaign + my own construction work; S1-A = 1 Pro campaign
+ a Qwen single-shot; S2-A = machine time only.
