# CODEX TICKET (engineering + exact search; for the Sep-3 codex window or a Pro/Qwen seat with
# code) — WIDE direction D1: a finite 677-counterexample search inside a PRIMITIVE DIAGONAL
# action. Repo: $HOME/workspace/claudecode/automath. English. OR-tools CP-SAT is in
# engine/venv_item3 (python); kissat in tools/. Local caps: any solve ≤ 600 s; the long run
# is a cloud item (runner file committed, not executed here).

## The template (registry R46 STEP 33; from engine/harvest/etp677_wide_r46_pro.md D1)
S = A5 (60 elements; build it as even permutations of 5 points, with multiplication and
inverse tables). K = S × S acts on S by (a,b)·z = a z b⁻¹ — a primitive action (stabiliser
of 1 = the diagonal ΔS, maximal). A magma on S whose rows are elements of K:
   x * y := a_x · y · b_x⁻¹        (a_x, b_x ∈ S unknown; 120 unknowns)
is automatically a left quasigroup. E677 for (x,y): with p := y*x = a_y x b_y⁻¹,
   a_y · a_x · a_p · y · (b_y · b_x · b_p)⁻¹ = x      (3600 equations; p is a dynamic index).
E255 fails at 1 iff, with p₀ = a_1 b_1⁻¹ (= 1*1), q₀ = a_{p₀} b_{p₀}⁻¹ ... — compute
((1*1)*1)*1 through the rows and require ≠ 1 (WLOG the defect at 1 by transitivity of K
acting by conjugation on the whole section).
Generation: ⟨(a_x,b_x) : x⟩ = K is checked AFTER a solution is found (if it fails, the
left-multiplication group is a proper subgroup; the magma is still a counterexample!).

## Tasks
1. `diag_cpsat.py`: CP-SAT model — IntVar a[x], b[x] ∈ 0..59; group multiplication via
   AddElement over a flattened 3600-entry table (index = 60·g + h) or AddAllowedAssignments;
   the dynamic index p via AddElement(p, a_list, a_p) and AddElement(p, b_list, b_p);
   staged products with intermediate IntVars; the defect constraint at 1; symmetry: fix
   a_1 = 1 WLOG? (justify: conjugating the section by (g,g) ∈ ΔS fixes the point 1 and
   maps a_x ↦ g a_{g⁻¹ x g} g⁻¹ … — state exactly what may be fixed, or fix nothing.)
   Also a plain SAT encoding `diag_cnf.py` for kissat + BreakID if CP-SAT is slow.
2. CONTROLS (mandatory): (a) drop the defect and require E255 everywhere → the model must
   admit the trivial solutions? (Which sections give E677 magmas on A5 at all? e.g. is
   x*y = y (a_x = b_x = 1) E677? No — check; find by solver at least one E677 section on A5
   or prove none exists without the defect: if NONE exists even without the defect, report
   that as the answer "no 677-magma of this form" — still informative.) (b) a smaller
   template as a warm-up: S = A4 (12 points; not primitive but tests the machinery) and
   S = Z/7 with K = Z/7 × Z/7 acting by (a,b)·z = a + z − b (this recovers translation-
   invariant magmas x*y = y + c_x — compare with known affine models as a positive control).
3. Run the A5 model with the defect for ≤ 600 s locally; report status; commit a cloud
   runner `problems/etp677/diag/startup_diag.sh` (installs ortools in a venv on the VM,
   runs the model with 8 workers, no time limit, checkpoints the solver log every 10 min,
   uploads a solution immediately if found). Decode + verify any solution with an
   INDEPENDENT checker (build the 60×60 table, check rows, E677 on all 3600 pairs, E255 at
   every point) before reporting.

## Deliverables
`problems/etp677/diag/{a5.py, diag_cpsat.py, diag_cnf.py, check.py, controls.out, startup_diag.sh}`
and `engine/out/codex/etp677_D1_diag_report.md` ending with DONE-D1DIAG.
