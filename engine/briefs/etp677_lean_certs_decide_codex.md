# CODEX TICKET — upgrade the q=3 Lean certificates from `native_decide` to kernel `decide`
# Repo: $HOME/workspace/claudecode/automath. Project: lean/etp677_certs/ (Lean
# v4.27.0, stdlib only). Code/comments in ENGLISH. Local compute: lake build only (cap the
# attempt: if a single `decide` does not finish within 20 minutes, stop and report).

## Why
`#print axioms` on the four object theorems shows [propext, Lean.ofReduceBool,
Lean.trustCompiler] — the `native_decide` tier trusts the compiled evaluator. The campaign's
banking rule wants certificates whose axioms are only propext / Classical.choice / Quot.sound.
For the two q=3 objects (13×13 tables) a kernel-reduction proof should be feasible.

## Tasks
1. In new modules `R45L02Decide.lean` and `L03Decide.lean` (keep the existing ones), prove
   the SAME `Certificate object rows` statements with `decide` (or `by decide` after
   `simp only`/`unfold` as needed), NOT `native_decide`. If the kernel is too slow on the
   current `Core.lean` definitions (List-based `countN`/`allN` over `List.range`), you may
   add a second, kernel-friendlier formulation (e.g. `Nat.all`/`Nat.fold`-style loops, or
   `Array`-based checks, or a `Decidable` instance built from `Nat.decEq` chains) PROVIDED
   you also prove, or make definitionally obvious, that the new Boolean checker equals the
   existing `branchObjectB`/`perfectB`/`deltaZeroB` on the object (a lemma
   `checkerNew object = checkerOld object := by rfl` or a proved general equality).
2. `#print axioms` for the new theorems must show ONLY propext (and possibly
   Classical.choice / Quot.sound); record the output in `AXIOMS_DECIDE.txt`.
3. Also try the q=4 object (21×21) under the 20-minute cap; report feasibility either way.
4. Report timings (wall, per theorem) and the maximum recursion/heartbeat settings used
   (`set_option maxRecDepth`/`maxHeartbeats` are fine; say so).

## Deliverables
New modules + `AXIOMS_DECIDE.txt` + `engine/out/codex/etp677_lean_certs_decide_report.md`
ending with DONE-LEANDECIDE. If kernel `decide` is infeasible even at q=3, say so with the
measured evidence — that is a valid outcome.

## ADDENDUM (added after dispatch; finding F5 of etp677_checker_adversarial_report.md)
The current `Certificate o rows` proves only that every LISTED row is perfect (positive
inclusion). Add, for each object, a theorem `..._exact` stating that the listed rows are
EXACTLY the perfect rows: `∀ r < n, perfectB o r = true ↔ r ∈ rows` (with `decide` where
feasible, else `native_decide` and say so), so that the certified perfect-row set is exact.
