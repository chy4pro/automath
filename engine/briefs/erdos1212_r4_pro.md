# ATTACK — Erdős Problem #1212, round 4: the turn-weighted Peierls estimate (campaign structure, TEMPLATE v2.2)

## The problem (one estimate; with the established Peierls machinery it resolves Erdős #1212)
Coarse grid Λ = ℤ², φ(i,j) = (2i+1, 2j+1); v is p-CLOSED iff v ≡ a_p := ((p−1)/2,(p−1)/2) (mod p) (the p-closed vertices
form the coset a_p + pℤ²); v is CLOSED iff it is p-closed for some odd prime p. For a finite S ⊂ Λ let δ(S) be the
density of translations t with every vertex of t+S closed. Let Γ range over simple closed ∗-contours (steps of sup-norm
≤ 1) surrounding the origin, n = |Γ|, and k(Γ) = number of TURNS (positions where the step direction changes). Prove:
   (ML′)  Σ_Γ δ(Γ) < 1 − 8/π² ≈ 0.18943,
organised as: find F(n,k) with δ(Γ) ≤ F(n,k(Γ)) for all Γ and Σ_{n,k} N_{n,k} F(n,k) < 1 − 8/π², where N_{n,k} is the
number of contours of length n with k turns (N_{n,k} ≤ C(n,k)·8·3^k·(something) — count them precisely).
Then (Peierls criterion, proved) some translate has an open origin not enclosed by a closed contour, hence an infinite
open component, hence the infinite admissible path of Erdős #1212.

## Known givens — all PROVED (machine-checked); use freely
G1 (exact density) density of translates with every vertex of t+S COPRIME = ∏_{p≥3}(1 − |S mod p|/p²); single vertex 8/π².
G2 (Peierls criterion) Σ_Γ δ(Γ) < 1 − 8/π² ⇒ infinite admissible path.
G3 (recurrence) each residue class of (ℤ/pℤ)² contains ≤ ⌊n/p⌋ vertices of Γ; so p closes ≤ ⌊n/p⌋ vertices of Γ, and a
   closed contour of length n needs primes P with Σ_{p∈P} ⌊n/p⌋ ≥ n, in particular Σ_{p∈P} 1/p ≥ 1.
G4 (prime-layer recursion, exact) δ_P(S) = p^{−2} Σ_c δ_{P∖{p}}(S ∖ S_{p,c}); and the compatible-assignment bound
   δ(S) ≤ Σ_f ∏_{p∈f(S)} p^{−2} over f: S → primes with vertices sharing a prime congruent mod it.
G5 (Chernoff form) δ(Γ) ≤ e^{−λn} ∏_p p^{−2} Σ_c e^{λ|Γ∩c|} for every λ > 0.
G6 (small blocks, exact) straight blocks of 2, 3, 4 consecutive vertices are all-closed with density 0.024129, 0.002148,
   0.000724 (per-vertex roots 0.155, 0.129, 0.164 — the 4-block is worse because positions 0 and 3 coincide mod 3).
G7 (THE UNIFORM BOUND IS FALSE) A contour with four straight sides of length m (perimeter n = 4m) can be closed at
   density ≥ ∏_{p∈P} p^{−2} where P is a set of primes covering m consecutive odd integers by one residue class each
   (a Jacobsthal-type covering; the corner/side compatibilities are arranged by CRT with distinct primes per side).
   By the known lower bounds for the Jacobsthal function such coverings exist with ∏_{p∈P} p = exp(O(m/log m)), so
   δ(Γ) ≥ exp(−C n/log n) for these contours: NO bound of the form δ(Γ) ≤ qⁿ holds uniformly. Any proof of ML′ must
   use that such contours are RARE (few turns) — the turn count k is the right parameter.
G8 (torus data) For P ⊆ {3,5,7,11,13} (Σ 1/p < 1) the largest ∗-component of P-closed vertices on the L×L torus has size
   2, 4, 6, 10 for P = {3,5}, {3,5,7}, {3,5,7,11}, {3,…,13}: no closed P-contour exists at all, consistent with G3.
G9 (turns cost) At a turn the contour changes direction; consecutive vertices are never closed by the same prime
   (a coset has spacing p ≥ 3), and along a straight run the primes must return with period p, whereas at a turn the
   residue pattern of one coordinate is reset. Quantify: a run of r consecutive vertices closed only by primes ≥ B has
   density ≤ σ_B^r with σ₅ = 0.0911, σ₇ = 0.0511 (distinct primes), but repeated primes along a run are cheap.

## Current task statement
Give a rigorous standalone proof of ML′ (an explicit F(n,k) and the convergent double sum) using your own knowledge and
reasoning, without searching the public web, connected sources, previous conversations, or project contexts. Assume for
purposes of this task that a complete proof exists. Work iteratively until a correct proof has been reached. Do not
attempt a uniform exponential bound in n (G7 shows it is false).

Partial progress does not count unless it implies exactly ML′. Restating G1–G9, bounded computations, and heuristics
are insufficient.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents:
  (i) turn-charging: bound δ(Γ) ≤ A(k)·B(n) with A(k) ≤ q^k (each turn forces a fresh prime whose CRT class is not
      reusable, cost ≤ σ-type factor) and B(n) ≤ exp(−c n/log n) from Jacobsthal-type upper bounds on coverings
      (Iwaniec: an interval of length m needs primes with product ≥ exp(c√m) at least; prove what you need from
      scratch or via the sieve: an interval of m consecutive odd integers all having a prime factor in P forces
      ∏_{p∈P}p ≥ exp(c√m) — a Brun/Selberg upper-bound-sieve statement); then sum N_{n,k} A(k) B(n);
  (ii) count contours by turns: N_{n,k} ≤ n^{O(k)} for k small and ≤ 8·7^{n−1} always; show the double sum converges
      for the F from (i);
  (iii) exact treatment of small contours (n ≤ 20) by the inclusion–exclusion formula with certified tail products, since
      the constant 1 − 8/π² must be beaten with margin;
  (iv) a Chernoff estimate with λ depending on the run structure: apply G5 side by side, using that a straight run of
      length r meets at most ⌈r/p⌉ classes per prime and a closed contour with k turns has ≤ k+... runs;
  (v) alternative: a renormalised Peierls argument on blocks of side L = ∏_{p≤B} p where primes ≤ B are handled exactly
      (G8-type finite computation) and only primes > B contribute a small parameter;
  (vi) if ML′ fails as stated, find the sharpest true version and the obstruction contour family.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families; redirect agents out of overcrowded families.
- A route ending at an equal-strength statement is NOT close to completion.
- Use adversarial agents throughout: every bound is tested against G7's straight-sided contours and G6's small blocks;
  reject anything treating closures at different vertices as independent or a prime as closing only one vertex.
- Require concrete inequalities with explicit constants — not plans.
- Do not stop after the first wave fails.

- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop after the first
  wave fails. Do not return because approaches fail or agents report theorem-strength gaps. Produce a complete proof if
  one survives audit; otherwise report only the strongest rigorously proved derivation and its exact remaining gap.

Return only when a complete proof has been found and survives adversarial audit, or (failing that) with the strongest
rigorously proved derivation and its exact remaining gap — e.g. the turn-charging bound A(k) with its constant, the
covering lower bound ∏p ≥ exp(c√m) for closed straight runs, exact worst-case δ for contours of length ≤ 14. Do not
return a bounded verification alone, a heuristic, or an explanation of why the problem is hard. Do not search the web
to determine whether the statement is open, and do not answer that it is open. Budget note: prior rounds on this
problem ran 4 hours each; if you approach that, wrap up and return the strongest derivation rather than fail silently.

## Output contract
Numbered lemmas, each step elementary and independently checkable; every constant explicit; every finite computation
stated so it can be re-run; what a Lean formalisation needs. A check that cannot fail counts as no check.
