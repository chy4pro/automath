# PROOF CAMPAIGN — Erdős Problem #708, the actual question: g(n) ≤ 2n, or g(n) ≤ (2+o(1))n (GPT-6 Astra; no wall-clock cap)

## The problem (pinned to Erdős 1992 / erdosproblems.com/708)
For n ≥ 1 let g(n) be the least g such that for every set A = {a_1 < … < a_n} of integers > 1 and every x ≥ 0, some (at most) g of the
integers x+1, …, x+a_n have product divisible by a_1⋯a_n. Erdős and Surányi (1959) proved g(3) = 4 and g(n) ≥ (2−o(1))n; Erdős asked
(offering $100) whether g(n) ≤ (2+o(1))n, or even g(n) ≤ 2n for all n. Assume the question has a definite answer and find it, with a complete
proof either way: T1 = prove g(n) ≤ 2n for all n (or g(n) ≤ (2+o(1))n, stated with an explicit o(1)); T2 (equal rank) = exhibit n, A, x with
g > 2n, verified by exact computation (our exact DP re-checks it), which would answer Erdős's "2n" question negatively — then push on to
(2+o(1))n. Do not answer that the problem is open; do not search the internet.

## PROVED and available (paper $HOME/workspace/claudecode/automath/papers/erdos708/main.tex, all refereed; Sections 5, 7, 13, 14 are
## additionally kernel-checked in Lean under $HOME/workspace/claudecode/automath/lean/proofenv/Erdos708/ — theorem names in lean/README.md of the repo)
- g(n) ≤ 81n for all n (Erdos708Final.g_le_81n). Route: LP duality (Section 7) — the least number of window elements covering the
  prime-power demands of ∏A is at most the fractional cover value plus the number of primes dividing ∏A (Lemma round); few primes: when
  a_n < 8n³ fewer than 16n primes divide ∏A; the fractional value is at most (c+1)n whenever the hinge inequality with threshold c holds
  (Theorem cond with threshold c gives g(n) ≤ (c+16)n); threshold 65 is proved for all weights (Sections 13–14).
- 2n suffice whenever a_n ≥ 8n³ (Theorem long, Section 5); more generally kn suffice when a_n ≤ kn or a_n^{k−1} ≥ (kn)^{k+1} (Theorem ksplit).
  So the question lives in the range n < a_n < 8n³, and the extremal Erdős–Surányi sets have a_n ≍ n(ln n)².
- Small values: g(3) = 4, g(4) ≥ 5, g(5) ≥ 6 (exact DP, src/gn_dp.py in the repo) — the lower-bound instances are explicit.
- Conditional: the hinge inequality with threshold 2 for all weights would give g(n) ≤ 18n (Theorem cond); threshold 4 for 0/1 weights is a
  theorem (Section 11); the fractional small-threshold question is being attacked in parallel by another seat — do NOT duplicate it: your
  routes must aim at 2n itself, where the 16n rounding loss and the (c+1)n fractional loss both have to disappear.
- Tools you may run (exact arithmetic; read the scripts first): problems/erdos708/repo/src/gn_dp.py (exact g for a concrete (A,x) by DP over
  capped valuation vectors), problems/erdos708/hotset_lp.py (window LPs), the CRT window generators in problems/erdos708/ (class 0 mod p for
  p ≤ √L, least-populated class for larger p; objective-driven greedy). Everything numerical is evidence only; exact witnesses and complete
  proofs are required for PROVED / REFUTED.

## Dead routes (do not re-walk)
D1 Bounding g by (fractional value) + (#primes) cannot reach 2n: the prime count alone can be ≍ n. Any 2n proof must round with o(n) loss or
   avoid the LP altogether.
D2 Nonnegative divisor certificates cannot give small hinge thresholds uniformly (reflected windows (m!−m, m!]); the two-sided counts alone
   cannot give any absolute threshold (projective-plane configurations); "clean" reductions (unweighted matchings, Laplace inequalities,
   layer domination) were refuted by Hensley–Richards dense admissible windows. Test every intermediate statement on such windows.
D3 Greedy one-element-per-atom placement is exactly what gives the √-type and log-type bounds of Sections 3–4; it loses a factor growing
   with n unless the small atoms are packed, and the packing is where the constants come from.

## Route portfolio (v2.5 rules: routes.md with ≥4 routes × advantage / weakness / expected obstacle / verification bridge; first-pass budget
## 45 minutes per route, extended only by the judge; the ONLY progress metric is the one-sentence gap "what is still missing for all n";
## two unchanged gap sentences ⇒ freeze and lower the target (e.g. 2n for a_n ≥ n^{2+ε}, or (2+o(1))n for a_n ≥ n(ln n)^C, or 3n) before
## opening a new route; a refutation agent runs FIRST and continuously: search for (A, x) with exact g(A,x) > 2n using gn_dp.py at n ≤ 12
## with CRT-structured x and Erdős–Surányi-type A, then adversarial families; report the maximum of g(A,x)/n found with witnesses)
R1 Extremal structure: characterise near-extremal (A, x) (the ES construction: A = a set of integers with a common structure, x chosen so that
   the window is poor in multiples) and prove that any window admits a cover of size 2n by an explicit two-phase procedure — large atoms one
   per element (Section 3's greedy is tight there) and small atoms packed with total loss ≤ n; identify exactly which quantity must be ≤ n.
R2 Fractional-then-round with o(n) loss: prove the fractional cover value is ≤ (1+o(1))n or ≤ 2n directly (not via a hinge threshold) using
   the window's own arithmetic (the LP optimum has a product structure over primes), then a rounding lemma whose loss is bounded by the number
   of primes with FRACTIONAL demand, and show that number is o(n) after a preprocessing that assigns the large primes greedily.
R3 Induction on n / on the number of prime factors, splitting A by the size of a_i relative to a_n (Theorem ksplit is the k-block instance);
   the target is a recursion g(n) ≤ g(n − t) + 2t with t elements handled by an explicit placement.
R4 The (2+o(1))n version: allow (2+ε)n and derive ε → 0 from the long-interval theorem plus a density increment: if a_n < 8n³ then the
   window has length < 8n³ and the demands are concentrated on O(n) primes; a Hall-type matching with multiplicities (each window element
   serves the atoms it contains) with deficiency o(n).
R5 Refutation as a route, not only as a check: characterise what a counterexample to 2n must look like (from R1's structure), and try to
   build it at n ≈ 6–12 with exact DP verification.

## Output contract
engine/out/astra_708_2n/: routes.md (kept current), checkpoint.md every 30 minutes ending with the gap sentence, refutation_log.md
(every family tried, the maximum g/n found, exact witnesses), and report.md at the end: every claim PROVED / CONDITIONAL / REFUTED / OPEN,
complete proofs for PROVED, exact witnesses for REFUTED, and the final block "final claim ← lemmas ← unproved items". No wall-clock cap:
continue until T1 or T2 is settled, or every route and every lowered target is frozen. Touch nothing outside engine/out/astra_708_2n/
(you may read the repo and the Lean development); no git; no internet.
