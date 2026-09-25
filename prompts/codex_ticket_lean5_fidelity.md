# TICKET LEAN5FID — statement-fidelity audit of `lean/proofenv/K1695/CyclicToMinpoly.lean` against the Kourovka Notebook wording of Problem 16.95 (n = 3)

Self-contained; no internet. Do NOT modify existing files. Write only under `problems/k1695/lean5_fidelity/` and the
report at `engine/out/codex/k1695_lean5_fidelity_report.md` ending with `DONE-LEAN5FID`. ~45 min.
Model: `engine/out/codex/k1695_lean3_fidelity_report.md` (same format).

## Object
`engine/harvest/k1695_r6_lean5/REPORT.md` claims `K1695.kourovka_16_95_n3 (A) (hA : IsUnit A.det) :
∃ σ, minpoly K (A * σ.permMatrix K) = (A * σ.permMatrix K).charpoly` is proved, together with
`minpoly_eq_charpoly_of_krylov_linearIndependent` (Krylov-cyclic ⟹ minpoly = charpoly) and the general-n deflation
`cyclic_standardBasis_of_principalBlock`. The Kourovka Notebook problem 16.95 (J. G. Thompson), as recorded by line-k1695 in
`problems/k1695/campaign_registry.md` (§R1, quote it from there — do not search the internet), asks: for every field F and
every A ∈ GL(n, F), does there exist a permutation matrix P such that AP is cyclic, i.e. its minimal polynomial equals its
characteristic polynomial?

## Tasks
T1. Rebuild `cd lean/proofenv && ~/.elan/bin/lake env lean K1695/CyclicToMinpoly.lean`; `#print axioms` for every theorem
    (scratch file); report any declaration whose axioms are not exactly [propext, Classical.choice, Quot.sound].
T2. Quote verbatim the statements of `kourovka_16_95_n3`, `minpoly_eq_charpoly_of_krylov_linearIndependent`,
    `cyclic_standardBasis_of_principalBlock`; translate to plain mathematics; check: (a) field arbitrary (`[Field K]`) and no
    hidden `CharZero`/`Fintype`/`IsAlgClosed`; (b) A arbitrary 3×3 with `IsUnit A.det` as the ONLY hypothesis (is `IsUnit A.det`
    equivalent to A ∈ GL(3,K) over a field? state why); (c) σ ranges over ALL of `Equiv.Perm (Fin 3)` and `σ.permMatrix K` is a
    genuine permutation matrix — note Mathlib's convention (column j of A·P_σ is column σ.symm j of A) and confirm this yields
    "AP for some permutation matrix P" in the notebook's sense; (d) `minpoly K M = M.charpoly` is Mathlib's `minpoly` over K and
    `Matrix.charpoly` — both monic, so equality is the notebook's "minimal polynomial equals characteristic polynomial"; confirm
    no degree-only weakening; (e) does the general-n theorem `cyclic_standardBasis_of_principalBlock` state exactly
    "(S′)_n ⟸ (T_{n−1})" as in the registry (§R6.8 / §R6.29), with which hypotheses on the principal block?
T3. Vacuity: `example`s instantiating `kourovka_16_95_n3` at concrete matrices over ℚ, ZMod 2, ZMod 3 (typecheck only), and one
    non-invertible matrix showing the hypothesis is needed.
T4. Verdict YES / NO / YES-WITH-CAVEATS on: "Kourovka 16.95 for n = 3, in the notebook's own formulation, is kernel-checked in
    Lean 4/Mathlib over every field", with line numbers for each caveat and the exact sentence you would put in the registry.

## Report
T1–T4, verbatim Lean statements, then `DONE-LEAN5FID`.
