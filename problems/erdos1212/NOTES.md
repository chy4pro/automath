# Erdős #1212 (strengthened) — dialogue working notes, 09-02

## Machine evidence (C union-find, problems/erdos1212/components.c)
Admissible = gcd(x,y)=1, x,y>1, x or y composite; edges = unit steps; box [2,N]^2.
| N | admissible | density | largest component | share | second | span of largest | min(x+y) | far-edge vertices |
|---|---|---|---|---|---|---|---|---|
| 2000 | 2,337,670 | 0.5850 | 329,016 | 14.1% | 329,016 (mirror) | x[153,1974] y[1064,2000] | 1795 | 150 |
| 4000 | 9,417,254 | 0.5889 | 2,575,251 | 27.3% | mirror | x[2,3990] y[1064,4000] | 1795 | 499 |
| 8000 | 37,882,522 | 0.5921 | 13,386,699 | 35.3% | mirror | x[2,7998] y[1064,8000] | 1795 | 2761 |
Density → 6/π² = 0.6079 > 0.5927 (Z² site threshold). The giant component's share GROWS with N and it always
touches the far edge; the two largest components are mirror images under (x,y)→(y,x). Strong evidence for YES.
The near-origin region {x+y ≤ 21} is a finite component (42 vertices); the giant component never reaches
x+y < 1795 — an infinite path must start far out.

## Lemma A (leaf lemma). For n ≥ 2, (n, n+1) has ≤ 1 admissible neighbour. [proved; in the Pro brief as G2]

## Lemma B (no translation-periodic path, m = m' case). There is no infinite admissible path of the form
P ∪ (P+(m,m)) ∪ (P+2(m,m)) ∪ … for a finite path P and m ≥ 1.
Proof. Along such a path y−x is bounded, so x → ∞ and every column x is visited (x changes by ≤ 1 per step).
Let the values of y−x lie in [−w, w]. Choose x divisible by every prime ≤ w (and by 2). At column x the only
admissible vertices with |y−x| ≤ w are (x, x±1) (any other d has a common prime with x). Both are leaves (Lemma A,
x even), so the path cannot pass through column x. ∎  Consequence: approach family (iv) "periodic pattern" in the
brief cannot work verbatim; any construction must use rails whose least prime factors grow.
(For (m,m') with m ≠ m' the same argument does not apply directly since y−x → ∞; but coprimality forces every
prime factor of D = ym − xm' (constant along translates) to divide gcd(m,m'); left open.)

## Lemma C (rails). Horizontal run on composite row Y over [X,X'] is admissible iff no prime of Y divides any
x in [X,X']; hence X'−X < lpf(Y). Symmetric for columns. Fixed-prime rails impossible (brief G4).

## Structural observations for a proof (heuristic)
- "All-clear rows": if every prime factor of Y exceeds X', the whole row segment x ≤ X' is admissible. Rows with
  lpf(Y) > X must be ≥ X² to be composite. Columns likewise.
- The natural proof is greedy-with-sieve: at each corner choose the next rail among many candidates in a short
  window; bad candidates (a prime of the rail has a multiple inside the run) are a small fraction by a union bound
  Σ_{r | rail} (run+1)/r, provided lpf(rail) ≫ run length. Needs: many composites with large lpf in windows — for
  windows of length L with lpf > L^{1/3} the fundamental lemma of sieve theory gives ≍ L/log L; runs of length
  ≈ log L (typical gap to the next good rail) keep the union bound small. Making this rigorous with explicit
  constants is the whole difficulty; short-interval statements with lpf > L are UNPROVED territory (Jacobsthal).
- Attempts that fail: prime-square rails (rails too sparse vs run bound), unit-step diagonal bands (Lemma A),
  slope-k lines y = kx+1 (column must be coprime to (k+1)!, impossible for consecutive columns).

## Round 2 status (09-03 04:3x)
Q17 (Qwen): Peierls reduction formalised; L4.1 single-prime recurrence (≤ ⌊n/p⌋ per residue class); L5.1 prime-simple
contours ≤ σ₃ⁿ; L6.1 coarse bounded clusters; explicit rail (U,C)~(U+1,C)~(V,C). Gap ML (multi-scale repeated-prime
contour bound). All finite claims verified. P15 (Pro) still running on the same brief.

## 09-03 08:1x — the uniform Peierls bound ML is FALSE (dialogue analysis)
Consider a "square" ∗-contour of perimeter n whose four sides are straight. On a horizontal side the p-closed vertices
are those whose φ_x is ≡ 0 mod p (with φ_y ≡ 0 mod p fixing t_y mod p). Choosing t by CRT, a side of length m is closed
by a set P of primes iff the m consecutive odd integers φ_x can be covered by one residue class mod each p ∈ P — a
Jacobsthal-type covering. Known lower bounds for the Jacobsthal function (Ford–Green–Konyagin–Maynard–Tao 2018) give
coverings of length m using primes whose product is exp(O(m / log m)) (Iwaniec's upper bound j(P#) ≪ k² log² k is
consistent). Hence a square contour of perimeter n admits translates with every vertex closed at density
δ(Γ) ≥ ∏_{p∈P} p^{−2} ≥ exp(−C n / log n): NOT exponentially small in n. So δ(Γ) ≤ qⁿ uniformly in Γ (ML) is false,
and the exponential G5′ (∏p ≥ e^{cn}) is false; the truth for straight-sided contours is ∏p ≥ exp(c n/log n)-ish.
Consequence for the Peierls route: the sum Σ_Γ δ(Γ) must be organised by the number of turns k of Γ: contours with
few turns are rare (≤ n^{O(k)}) but arithmetically cheap; contours with Θ(n) turns are exponentially many but each turn
forces a fresh prime assignment (cost ≤ σ per turn?). Corrected target ML′: δ(Γ) ≤ q^{k(Γ)} · exp(−c (n−k)/log n) or any
F(n,k) with Σ_n Σ_k N_{n,k} F(n,k) < 1 − 8/π², where N_{n,k} = number of length-n contours with k turns.
Machine evidence (torus components): for P ⊆ {3,…,13}, Σ 1/p < 1 and the largest P-closed ∗-component has size
2, 4, 6, 10 (P = {3,5}, {3,5,7}, {3,5,7,11}, {3,…,13}) — no closed P-contour at all, consistent with the necessary
condition Σ_{p∈P} ⌊n/p⌋ ≥ n (each p closes ≤ ⌊n/p⌋ vertices of a length-n contour).


## Round 4 outcome and RETRACTION of G7 as unconditional (2026-09-03 20:4x, dialogue)
- Q19 (Qwen): no proof of ML′; L1–L8 elementary (capacity inequality, mask-DP finite bound, large-prime tail), L9 conditional summability under a chosen F(n,k). Arithmetic machine-checked. No progress on the turn charge.
- P16 (Pro): ML′ REFUTED via the bump family (M=15L+7, 2^{4L} contours with n=4M, k=12L+4, all bumps closed by one class mod 3 / mod 5, one CRT certificate). Geometry independently verified (bump_contours.py). The refutation needs four pairwise-disjoint one-class-per-prime coverings of [0,M] with ∏p = exp(o(M)).
- That input was MY G7 assertion of 09-03 08:1x and is UNPROVEN. Provable: a single covering with ∏p = exp(o(M)) (Westzynthius 1931 / Rankin 1938: j(P#)/P → ∞). Not provable now: r ≥ 2 disjoint coverings at that cost (needs class-choice gain ≥ (log M)^{(r−1)/r} over Mertens; Rankin/FGKMT give (log log)²). True under the conjectural j(P#) ≍ P log² P. Geometry cannot avoid disjointness (rows closer than the primes used need disjoint sets; rows ±1 beside a covered row are open for its primes).
- Status: G7 = conditional. Uniform bound δ(Γ) ≤ qⁿ: neither proved nor refuted unconditionally. ML′: conditionally refuted; even if not, no proof strategy survives (all four rounds could not derive a turn charge).
- New crisp question (unclaimed): 'disjoint Jacobsthal' j_r(x) = max length coverable by r pairwise-disjoint one-class-per-prime systems with primes ≤ x; is j_2(x)/x → ∞? Rankin's method gives nothing for r ≥ 2.
- Decision: #1212 slot-1 line wound down at method limit. Residue for publication (notes repo, no theorem): Lemmas A/B/C, run lemma, parity compression, factorial-shift embedding, periodic criterion, exact block densities, giant-component data, 6151-step path, bump-family construction + conditional obstruction, disjoint-Jacobsthal question.
