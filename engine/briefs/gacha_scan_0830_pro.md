# WIDE BRIEF — CANDIDATE-PROBLEM SCAN for an automated proof pipeline (2026-08-30).
# Label every item PROVED / COMPUTED / CONJECTURED / OPEN as you know it; cite sources by name; say when unsure.

Context. We are an autonomous mathematics pipeline whose decisive strengths are: (1) exhaustive search over
small finite structures (magmas, groups, matrices, designs, graphs) with SAT/CP-SAT and DRAT-certified UNSAT,
symmetry breaking and cube-and-conquer up to ~10^9 conflicts per cell; (2) polynomial-system certificates
(msolve Groebner bases, characteristic p and 0) for algebraic case decompositions; (3) Lean 4 + Mathlib
kernel-checked formalisation of finite lemmas and transport arguments; (4) an LLM construct-and-verify loop
that finds explicit counterexamples to conjectured lemmas. Weaknesses: arguments needing genuinely new
concepts, asymptotic/analytic estimates, anything not reducible to finite or algebraic case analysis.
Recent closed results (for calibration): fibre-size exclusions for a minimal counterexample to the finite
Equational-Theories-Project implication 677 => 255 (structure theorem, DRAT + Lean), and Kourovka 16.95
(Thompson: for A in GL(n,F) some A*P_sigma is cyclic) for n <= 4 over every field.

TASK. Produce a ranked list of 15-25 OPEN problems that fit our strengths, each satisfying all three:
 (a) decidable at small scale by exhaustive/algebraic search, or reducible to finitely many certificate cells;
 (b) recognised as open on a public list or in a recent paper (say which: ETP open implications list,
     Kourovka Notebook, Erdos problems site, OEIS "conjectured" entries, open-problem garden, Guy's UPINT,
     Mathlib/Lean wishlists, MathOverflow "unsolved" tags, recent arXiv "we were unable to decide ...");
 (c) a closed answer (theorem, counterexample, or a decisive small-case result) would be publishable and
     valued by that community, and plausibly reachable in 1-3 days of the resources above.

For EACH candidate give: exact statement; source/list and status as you know it (with the risk that it was
solved after your knowledge cutoff - flag it); why it fits (which of (1)-(4)); the concrete finite/algebraic
reduction you would attempt first (sizes, symmetry, expected cell counts); a difficulty estimate (hours of
compute + human-proof risk); value (who cares, what it unlocks); and the first sanity control to run.
Prioritise: remaining OPEN implications of the Equational Theories Project (list every one you know with its
numbers and the smallest orders already exhausted), computational Kourovka problems (finite groups, small
n), small-case conjectures on Latin squares/quasigroups/loops, finite geometry and designs, graph
conjectures with small extremal cases, and matrix/permutation problems like 16.95 for other matrix classes.
End with a 5-line "do first" recommendation and a 5-line "avoid" list (problems that look finite but hide an
infinite/analytic core).

# APPENDIX (WITH-INTERNET VERSION ONLY) — VERIFY-LIST. Check each against the live source (ETP GitHub
# dashboard / Lean repository and blueprint, Kourovka Notebook latest edition PDF, arXiv, MathSciNet-level
# search) and report: current status (OPEN / SOLVED — by whom, when, link), smallest unexhausted order or
# open parameter, and whether it survives criteria (a)-(c). Do this BEFORE the ranked list; cite URLs.
V1 ETP finite implication 1485 => 151 ("Austin pair" candidate): proved for finite magmas in 2025 or still
   open? If open: what orders are exhausted, what is the known infinite counterexample, and does a
   "no small congruence class in a minimal finite counterexample" reduction apply (left translations
   bijective?).
V2 ETP: is 677 => 255 (finite) the ONLY remaining open finite implication? List any others still open on
   the dashboard, with numbers.
V3 ETP phase-2 / follow-up projects with public open lists (two operations, commutative magmas, laws of
   larger size, single-axiom questions): which have a concrete open small-order question today?
V4 CSPLib quasigroup existence problems QG1-QG7 (idempotent quasigroups with (xy)(yx)=x, (xy)y=x(xy), ...):
   current frontier orders (which orders are open per identity) and the last published SAT results.
V5 Products of two cyclic (nonderogatory) matrices over F_2, F_3 for n <= 4: known? (Sourour-type
   factorisations need |F| large.) Give the exact literature status.
V6 Waring-type tables for M_n(F_q): sums of two k-th powers / two squares / two nilpotents / two
   idempotents, n <= 3, q <= 5, k <= 4 — which tables exist in print (Katre-Garge, Larsen-Shalev-Tiep,
   others) and where are the gaps?
V7 Kourovka Notebook entries decidable with the GAP SmallGroups library ("does there exist a finite group
   with ..." for orders up to a few thousand): list concrete entry numbers still marked open in the
   latest edition, with the order bound where the search would start.
V8 Cayley-graph Hamiltonicity: the largest order for which all connected Cayley graphs are verified
   Hamiltonian, and whether the next order is a recognised open computation.
V9 Any 2024-2026 arXiv paper on finite magmas / quasigroups / small matrix groups that states "we could
   not decide" a specific small case (search phrases: "remains open for n =", "we were unable to
   determine", "open for order").
