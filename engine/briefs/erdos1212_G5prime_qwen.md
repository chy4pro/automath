# ATTACK — the exponential-product lemma G5′ for Erdős Problem #1212 (single-shot variant, TEMPLATE v2.2, round 4)

## The problem (one geometric lemma; with the Peierls machinery it resolves Erdős #1212)
Coarse grid Λ = ℤ², φ(i,j) = (2i+1, 2j+1). For an odd prime p, a vertex v is p-CLOSED iff v ≡ a_p (mod p) where
a_p = ((p−1)/2, (p−1)/2), i.e. iff p divides both coordinates of φ(v); the p-closed vertices form the single coset
a_p + pℤ² (one per p×p block). For a finite set P of odd primes, a vertex is P-closed iff it is p-closed for some
p ∈ P. A ∗-contour is a simple closed walk with steps of sup-norm ≤ 1. Prove:
   (G5′) there is an absolute constant c > 0 such that if the set of P-closed vertices contains a simple closed
         ∗-contour of length n, then ∏_{p∈P} p ≥ e^{cn}.
Equivalently: a closed ∗-contour of length n cannot be covered by the cosets a_p + pℤ² of primes whose product is
less than e^{cn}.

## Known givens — all PROVED (machine-checked); use freely
G1 (bounded clusters) With L = ∏_{p∈P} p, the lines i ≡ 0 (mod L) and j ≡ 0 (mod L) contain no P-closed vertex, so every
   ∗-component of P-closed vertices lies in one L×L cell; hence n ≤ L² trivially, i.e. only ∏p ≥ √n is known.
G2 (single-prime recurrence) On a ∗-contour of length n, each residue class of (ℤ/pℤ)² contains ≤ ⌊n/p⌋ vertices
   (≤ 1 if n < p): congruent vertices are ≥ p apart in sup norm.
G3 (density) The density of P-closed vertices is 1 − ∏_{p∈P}(1 − 1/p²) ≤ Σ_{p∈P} 1/p² < 0.2023 — far below the ℤ²
   site-percolation threshold 0.5927 and below the ∗-percolation threshold too; heuristically P-closed clusters
   have exponential tails, which is what G5′ makes rigorous for a FINITE, PERIODIC pattern.
G4 (exact density of a closed pattern) For a finite S, the density of translates t with every vertex of t+S closed by
   primes of P is p^{−2} Σ_c δ_{P∖{p}}(S ∖ S_{p,c}) (prime-layer recursion), and δ_P(S) ≤ Σ over compatible assignments
   f: S → P (vertices sharing a prime congruent mod it) of ∏_{p∈f(S)} p^{−2}.
G5 (Chernoff form) For any λ > 0, δ_P(Γ) ≤ e^{−λn} ∏_{p∈P} p^{−2} Σ_c e^{λ|Γ∩c|}.
G6 (small cases, exact) For a straight block of 2, 3, 4 consecutive vertices the all-closed densities are 0.024129,
   0.002148, 0.000724 (per-vertex roots 0.155, 0.129, 0.164; the 4-block is worse than the 3-block because positions
   0 and 3 coincide mod 3).
G7 (what fails) The bound |Γ∩c| ≤ n/p alone cannot give G5′: a straight segment of length n meets ≈ p classes with
   ≈ n/p points each for every p ≤ n; closedness of the contour is essential.

## Current task statement
Give a rigorous standalone proof of (G5′) — or of the weaker but still sufficient statement ∏_{p∈P} p ≥ n^{K} for every
K with explicit constants, or of the entropy inequality Σ_{p∈P} log(p^{−2} Σ_c e^{λ|Γ∩c|}) ≤ (λ − c)n — using your own
knowledge and reasoning, without searching the public web, connected sources, previous conversations, or project
contexts. Assume for purposes of this task that a complete proof exists. Work iteratively until a correct proof has
been reached. This is a finite, periodic, combinatorial statement; treat every "well-known difficulty" as a claim to
be tested.

Partial progress does not count unless it implies exactly G5′ (or the stated sufficient variants). Restating G1–G7,
bounded computations, and heuristics are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents:
  (i) turning-point argument: a closed ∗-contour of length n has ≥ 4 turns and, since it is closed, at least Ω(n/p)
      "returns" modulo p for each p — quantify how a periodic coset a_p + pℤ² can carry a long straight run (at most p−1
      steps in a row along a coset line? no: a coset is a lattice, so consecutive contour vertices on the same coset are
      ≥ p apart — hence between two p-closed vertices the contour must be closed by OTHER primes for ≥ p−1 steps);
      derive that the primes must "take turns" and count the turns;
  (ii) smallest-prime induction: let p_min be the least prime in P; on any run of p_min − 1 consecutive contour vertices
      at most one is p_min-closed, so the others are closed by P ∖ {p_min}; iterate to get n ≤ f(P) with f growing like
      a product/exponential;
  (iii) counting closed patterns: the number of P-closed vertices in an L×L cell is ≤ L² Σ 1/p² and they are arranged
      as a union of lattices; bound the length of the longest simple closed ∗-walk inside a union of k lattice cosets of
      moduli p_1 < … < p_k;
  (iv) Chernoff with contour geometry: bound Σ_c e^{λ|Γ∩c|} for closed Γ using that a closed contour crossing a coset
      line must cross it again, giving cancellation of concentration;
  (v) potential/discrepancy: assign to the contour the vector (|Γ∩c|)_{p,c} and prove a lower bound on the "entropy"
      Σ_p log(number of classes met) ≥ c·n for closed contours (a straight segment meets few classes for large p but
      a closed curve of length n has diameter ≤ n/2 and area, so it meets many classes for p ≲ diameter);
  (vi) if G5′ is false, find the counterexample family (a P-closed closed contour of length n with ∏p = n^{O(1)})
      and state the sharpest true bound.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at an equal-strength statement is NOT close to completion.
- Use adversarial agents throughout: test every claimed inequality on explicit small P (e.g. {3,5}, {3,5,7}) by exhaustive
  search of P-closed ∗-contours inside one L×L cell; reject any step that treats primes as independent without CRT.
- Require concrete inequalities with explicit constants — not plans.
- Do not stop after the first wave fails.

Return a complete proof if one survives adversarial audit. If none does, return instead: (1) the strongest rigorously
proved derivation you reached, as numbered lemmas — e.g. G5′ for P ⊆ {3,5,7,11} by exhaustion with the exact longest
closed P-contour lengths, a proved polynomial bound ∏p ≥ n^K, or a proved turn-counting inequality; (2) the exact
remaining gap as a precise open statement; (3) every machine-checkable artefact you built (longest P-closed contour
tables for small P, extremal contours, code). Do not return an empty answer, a bare statement of failure, a status
report, or an explanation of why the problem is hard. Do not search the web to determine whether the statement is
open, and do not answer that it is open.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation
stated so it can be re-run; what a Lean formalisation needs. A check that cannot fail counts as no check.
