# Task R6-E: build the FIRST non-translation-invariant blueprint extension
#            (and thereby test conjecture R6-B-2 "e is an automorphism")

Read first: problems/etp677/R6A_selfref_report.md Section 8 (especially 8.5's
constraint shape), problems/etp677/R6C_codex_report.md (your own order-77
construction — the method to imitate), problems/etp677/r5a_search.py
(pair_subs gives the pair-indexed compatibility instances for general bases).

Motivation: ALL known finite 677 models are translation-invariant blueprint
extensions; on that family e(x)=x\x is automatically an automorphism
(base translation x fibre scalar), so conjecture R6-B-2 has zero discriminating
power there. A NON-TI extension would be (a) the first model outside the TI
family, (b) the decisive test: R6-A section 8.5 shows e is a homomorphism iff
lambda_{x<>y} a_{x,y} = a_{eps(x),eps(y)} lambda_x and the b-analogue hold for
all pairs — 2p^2 constraints with no reason to hold.

Job:
1. Take a small idempotent TI base (e.g. F_5 with 2x-y, or F_11 with 6x+6y)
   and AFFINE pair-indexed fibre ops s |-> a_{x,y} s + b_{x,y} t on a small
   field fibre. Derive the eq-(4) compatibility equations for PAIR-indexed
   coefficients (the analogue of your R6-C derivation, without the TI
   restriction a_{x,y} = a_{y-x}). Solve ALGEBRAICALLY for a genuinely non-TI
   solution: one where (a_{x,y}, b_{x,y}) is NOT a function of y-x alone.
   Light targeted computation allowed (small linear-algebra solves, seconds);
   NO SAT, NO brute-force enumeration of full assignment spaces.
2. If a non-TI solution exists: build the full Cayley table in Python, verify
   E677 exhaustively, then test e(x*y) = e(x)*e(y) on all pairs. Either
   outcome is a major result: violation => R6-B-2 falsified; holds => strong
   evidence for R6-B-2 beyond the TI family.
3. If the compatibility equations FORCE translation-invariance for affine
   fibres over these bases, prove it — that is a new rigidity theorem
   (explains why no non-TI model was ever found) and redirects the R6-B-2
   test to non-affine fibres.
Report: problems/etp677/R6E_codex_report.md, PROVED/computed/conjectured
markers, honest about which of the three outcomes occurred.
