# TICKET LEAN3FID — statement-fidelity audit of `lean/proofenv/K1695/CyclicVectorThree.lean` against Kourovka 16.95 (n = 3)

Self-contained; no internet. Do NOT modify existing files. Write only under `problems/k1695/lean3_fidelity/` and the
report at `engine/out/codex/k1695_lean3_fidelity_report.md` ending with the literal line `DONE-LEAN3FID`. ~60 min.

## Context
`engine/harvest/k1695_r6_lean3/REPORT.md` claims that `K1695.kourovka_16_95_n3_cyclic_vector` (and companions) in
`lean/proofenv/K1695/CyclicVectorThree.lean` prove, over every field, the n = 3 case of Kourovka Notebook problem
16.95 (Thompson): "for every field F and every A ∈ GL(n, F) there is a permutation matrix P such that AP is cyclic
(its minimal polynomial has degree n, equivalently it has a cyclic vector)". The line's own statement of the problem
and its conventions are in `problems/k1695/campaign_registry.md` (§R1–§R3 for the definitions; `P_σ e_j = e_{σ(j)}`,
`A P_σ` = columns of A permuted). The ticket that produced the file is `engine/briefs/k1695_r6_lean3/TICKET.md`.

## Tasks
T1. Rebuild: `cd lean/proofenv && ~/.elan/bin/lake env lean K1695/CyclicVectorThree.lean` (record exit code, warnings,
    any `sorry`), then `#print axioms` for EVERY theorem in the file (write a scratch file that imports it and prints
    them; do not edit the file).
T2. Statement fidelity, theorem by theorem: transcribe the exact Lean statement of `kourovka_16_95_n3_cyclic_vector`,
    `kourovka_16_95_n3_every_coordinate`, `t2_rank_two_matrix`, `t2_six_choices_scalar`, and translate each into plain
    mathematics. Check: (a) the field is arbitrary (`[Field K]`, no `CharZero`/finiteness/decidability that restricts
    generality — note `[DecidableEq K]` is harmless); (b) the matrix is arbitrary in GL(3,K) (invertibility is the ONLY
    hypothesis; no extra hypothesis such as "rank of a sub-block", "some entry nonzero", or a specific column order);
    (c) the conclusion is existence of a permutation of the columns (a genuine permutation matrix — check how P_σ is
    defined and that ALL 6 permutations are admissible, not a fixed subset) such that the product has a cyclic
    vector, AND that "cyclic vector" is defined as linear independence of v, Mv, M²v (Krylov), which is equivalent to
    "M is cyclic" for 3×3 — state whether the file proves that equivalence or only the vector form; (d) the product is
    A·P (columns permuted) and not P·A (rows permuted) — say which, and whether it matters (it does not for existence
    of a cyclic matrix since P A = P (A P^{-1}) P^{-1}... check carefully and state the correct argument);
    (e) definitional hazards: `Matrix.rank`, `Fin 3`, `Matrix.mulVec`, `Function.Injective` for the permutation, any
    `Classical` choice hiding a stronger hypothesis, any `Nontrivial`/`IsDomain` assumption beyond a field.
T3. Vacuity: instantiate the main theorem at three concrete matrices (over ℚ, over ZMod 2, over ZMod 3) with `example`
    in your scratch file to show the hypotheses are satisfiable, and at one NON-invertible matrix to confirm the theorem
    does not apply (it must fail to typecheck or need the invertibility hypothesis).
T4. Verdict: does the file prove Kourovka 16.95 for n = 3 over every field exactly as stated in the registry, YES / NO /
    YES-WITH-CAVEATS (list each caveat with the line number in the .lean file).

## Report
T1–T4, with the exact Lean statements quoted verbatim, then `DONE-LEAN3FID`.
