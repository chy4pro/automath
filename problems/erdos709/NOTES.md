# Erdős #709 — working notes (started 2026-09-05; no repo/paper until the line is finished)

Statement (erdosproblems.com/709, verbatim): f(n) minimal such that for any A = {a_1,…,a_n} ⊆ [2,∞) ∩ ℕ of size n, in any interval I of
f(n)·max(A) consecutive integers there exist distinct x_1,…,x_n ∈ I with a_i | x_i. "Obtain good bounds for f(n), or even an asymptotic formula."
Known: Erdős–Surányi (1959) (log n)^c ≪ f(n) ≪ n^{1/2}. Site comments (2026): f(n) ≫ log n/log log n via van Doorn's F(n,m) ≫ n log n/log log n
and F(n,m) ≤ f(n)·n with A = {2,…,n+1}; f(n) ≫ √(log n/log log n) via #711. G2 (09-05): arXiv 2607.10431 (Kominers) is about F(n)−f(n,n);
the upper bound n^{1/2} is untouched since 1959.

## Machine facts (brute force, f_small.py: all n-subsets A ⊆ [2,M], all windows mod lcm(A), Hall via augmenting paths)
- f_20(2) = 2 (extremal {2,3}); f_20(3) = 2 ({2,3,4}); f_16(4) = 2 ({2,3,4,5}); f_12(5) = 2 ({2,3,4,5,6}).
  (Subscript = bound on max(A); these are lower bounds for f(n) and exact within the range.)

## Engine rounds
- Q34 (Qwen3.8-Max, 09-05): claims f(n) ≤ 2√n for n ≥ 4 (classical argument reconstructed; unverified), f(1)=1, f(2)=f(3)=f(4)=2 (agrees with
  brute force), T3 'polynomial deficiency for A_k = {m/2,…,m/k}' — SUSPECT (contradicts the polylog state; likely wrong).
- P30 (Pro GPT-5.6 Sol, 09-05 07:39–): brief erdos709_r1_pro.md; progress note: 'consecutive-multiple edges prove length 2m suffices for n ≤ 5'.
- 08:59: f_12(6) = 2 ({2,3,4,5,6,7}); f_24(4) = 2 ({2,3,4,5}). So far every extremal set is {2,…,n+1} and f = 2 for 2 ≤ n ≤ 6 in range.
  Next capped runs: f(7) with M = 12; f(6) with M = 13.
- 09:28: f_12(7) = 2 ({2..8}); f_13(6) = 2 ({2..7}). Pattern: f_M(n) = 2 for 2 ≤ n ≤ 7 in the ranges tested, extremal set always {2,…,n+1}.
- 09:35 P30 DONE (89 min): f(n) ≤ K(n) ≤ ⌈√n⌉ (boundary injection + path inequalities); f(1)=1, f(2..5)=2, f(6..9)=3; f(19) ≥ 4 (CRT, verified);
  f(6) > 2 example A={71,80,83,91,92,100} verified (max A = 100 — explains why our small-M brute force saw only f = 2). Referee (Opus) running.
  Index: engine/harvest/erdos709_pro_r1.md.
- 09:5x G2 UPDATE: arXiv:2603.28636 (van Doorn–Li–Tang, Mar 2026) solved #650 with exactly the 2-block boundary-injection argument of P30 (matching number in 2·max(A) = min(m,⌈2√m⌉)). P30's Theorem 6 is its k-block extension; novelty of round 1 is limited to exact small values and f(19) ≥ 4. Decision: #709 demoted to the Qwen seat (constructions), Pro seat back on #708 (P31). See G2.md.
- 10:0x REFEREE P30: all claims PASS (details engine/harvest/erdos709_pro_r1.md, full report referee_r1.md). Extra: exact odd-k thresholds T(5)=26, T(7)=51, T(9)=83 by DP. Status of #709: k-block extension + small values only; HOLD, no paper.
- 11:25 Q35 DONE: f(10) = 3 (Lemma 2: shape (2,5,2) excluded by a degree/bijectivity argument — checked by me; enumeration confirms it is the only shape); f(6) ≥ 3 certificate A = {16,17,18,19,22,23}, C = 2756168, window [C−22, C+23] — VERIFIED (5 points). Exact f(n) for n ≤ 10: 1,2,2,2,2,3,3,3,3,3. Next: r = 11 (shapes (2,6,2), (3,4,3)) → Q36 follow-up. Still HOLD (no paper).
- 11:5x Q36 DONE: f(11) = 3 (shapes (2,6,2),(3,4,3) excluded via loop/midpoint counting; checked line by line). Exact f(1..11) known; first n with f(n) ≥ 4 in [12,19]. Started local 3-layer line-system search (layer3_search.py, logs layer3_N40.log / N80.log, 9 min cap).
- 12:5x Q37 DONE (r = 12): three doubly-bijective shapes excluded (checked); six asymmetric shapes OPEN; r = 13 shapes enumerated. f(12) undetermined. Q38 = six open shapes; S1 (ChatGPT sub-Pro) = exact search, running.
- 13:2x Q38 DONE: no all-loop 12-line system (checked); six shapes still open; f(12) undetermined. Theory at diminishing returns → Q39 = write an exact bounded MILP decision program (general model, max(A) ≤ m, window 3m) which I run locally; S1 (ChatGPT) still searching loops-only systems.
- 13:3x My exact MILP (hall3.py: r moduli, max A = m forced, k blocks, minimise |covered set|; HiGHS) — test: r=6, m=23, k=2 gives min|S| = 5 (new witness moduli {17,19,20,21,22,23}, residues (13,13,10,9,10,9)), reproducing f(6) ≥ 3. Sweep r = 12, k = 3: m=14→26, m=16→23, m=18→21 (need ≤ 11): far from failure at small m (log hall3_r12.log, continuing to m = 40). Sweep r = 6, k = 2, m = 14..22 to find the minimal max A for f(6) ≥ 3 (log hall3_r6k2.log).
- 13:4x EXACT (MILP, k = 2, r = 6): min |S| = 6 for m = 14, 15 and 5 for m = 16..22 ⇒ the smallest max(A) admitting an f(6) ≥ 3 witness is 16: A = {11,…,16}, window [0,32), residues (10,10,8,8,6,6), covered {6,8,10,21,22} (verified directly). Answers Q35's open item 5 (brute force had said ≥ 14).
- 13:5x S1 DONE (ChatGPT sub-Pro search, 67 min): 3-layer 17/16 system and 4-layer 62/61 and 79/76 systems — ALL VERIFIED by verify_s1.py including CRT embedding ⇒ f(17) ≥ 4 (hence f(17) = f(18) = 4 via R(4) = 18) and f(62) ≥ 5. Engine's exhaustive claim (loops-only r_min = 17) not independently verified and does not settle f(12..16). Table: f(1..11) = 1,2,2,2,2,3,3,3,3,3,3; f(12..16) ∈ {3,4}; f(17)=f(18)=4; f(19..25) ∈ {4,5}; f(62) ≥ 5.
- Site thread 708: my 03-Sep comment (v5 DOI) no longer appears even when logged in (was 'awaiting approval') — presumably rejected. Post one comment with the concept DOI at the next milestone only.

## 2026-09-07 — external claim found (see G2.md same date): f(n) ≤ 7(⌊n^{3/7}⌋+1), Lean-verified by Star Fleet Math (2026-07-14). Our ⌈√n⌉ is superseded asymptotically pending our own kernel re-check; exact small values unaffected. Route idea: multi-slice projection inequalities on longer blocks to beat 3/7.
