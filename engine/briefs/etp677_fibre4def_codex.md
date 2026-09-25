# CODEX TICKET (exact search engineering; any tier — verified verdicts only) — FIBRE-4 (and 5, 6)
# gauge-free cores WITH THE E255 DEFECT, on your enlarged universe from DONE-FIBRE4CORE.
# Repo: $HOME/workspace/claudecode/automath. Reuse problems/etp677/simple/fibre_core/fibre4/
# (your 69-name universe, 88 certified products, 34 closed instances / 74 pairs; m = 4 SAT witness)
# and read problems/etp677/simple/fibre_core/core_joint.py (--defect: the defect chain) and registry
# STEP 53 (grep "STEP 53"). Local caps ≤ 600 s per solve, ≤ 2 heavy processes; disk is at 87 % —
# delete DRAT files after drat-trim verification (keep the drat-trim log + sha256 of the proof).
# DONE marker: DONE-FIBRE4DEF.

## Why
A minimal counterexample M to 677 ⟹ 255 has an E255 failure at some m₀; with a = π(m₀) in the
quotient B (E677+E255), the fibre over a carries the DEFECT: for the fibre coordinate s₀ of m₀,
((a,s₀)*(a,s₀))*(a,s₀))*(a,s₀) ≠ (a,s₀). Through the universal chain aa = S(a), S(a)·a = U(a),
U(a)·a = a this is: σ_{u,a}(r₂)(s₀) ≠ s₀ where r₁ = σ_{a,a}(s₀)(s₀), r₂ = σ_{s0,a}(r₁)(s₀).
Our 10-instance joint core + this defect is UNSAT for m = 3 (as it must be) and UNDECIDED at
m = 4 after 600 s (kissat and CP-SAT), whereas without the defect m = 4 is SAT in seconds. Your
34-instance core adds many constraints; with the defect it may become decidable.

## Tasks
1. Add the defect (∃ s₀ selector, chain through the pairs (a,a), (S(a),a), (U(a),a) — all in
   your universe) to the full 34-instance gauge-free core; run m = 4 with kissat and CP-SAT
   (≤ 600 s each); if UNSAT → DRAT, drat-trim, then minimise the instance set (greedy drop,
   re-verify each step) and report the minimal defect core; also try m = 5 and m = 6.
   Controls (mandatory): m = 3 + defect UNSAT (DRAT); m = 5 + defect with σ fixed to the
   order-5 direct product must be UNSAT (E255 holds there); m = 4 WITHOUT the defect stays
   SAT (your witness).
2. If m = 4 + defect is still UNKNOWN at 600 s: package it (and m = 5, 6) as cloud cells under
   problems/etp677/simple/fibre_core/fibre4/cloud_def/ with SHA256SUMS (DIMACS headers exact) —
   do not launch — and report the best partial information (e.g. which single instance, when
   added to the 10-instance joint core + defect, changes the solver behaviour most; conflict
   counts).
3. Report table: core → m → defect? → verdict → time → certificate.
## Deliverables
problems/etp677/simple/fibre_core/fibre4/def/ (encoder, CNFs, logs, drat-trim logs) and
engine/out/codex/etp677_fibre4def_report.md ending with DONE-FIBRE4DEF.
