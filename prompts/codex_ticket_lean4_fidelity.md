# TICKET LEAN4FID — statement-fidelity audit of `lean/proofenv/K1695/TranspositionLemmaFull.lean` (+ TranspositionLemma.lean) against Lemma T as stated in the k1695 registry

Self-contained; no internet. Do NOT modify existing files. Write only under `problems/k1695/lean4_fidelity/` and the
report at `engine/out/codex/k1695_lean4_fidelity_report.md` ending with `DONE-LEAN4FID`. ~60 min.
Model: `engine/out/codex/k1695_lean3_fidelity_report.md` (same format: rebuild, axioms, verbatim statements, plain-math
translation, vacuity examples, verdict YES / NO / YES-WITH-CAVEATS with line numbers).

## Object
Lemma T ("transposition = rank-one update") as stated in `problems/k1695/campaign_registry.md` §R6.1 with the §R6.6 repair
(T1/T2 require μ ≠ 0) and the §R6.14/§R6.20 wording: T0 (derogatory only at an eigenvalue of A), T1, T2 (nullity-two
criterion, both directions), T3 (nullity ≥ 3 ⟹ AP_τ derogatory), T4 (rationality over a subfield; general degree vs the
quadratic case vs the "cubic fallback"). The Lean claims are in `engine/harvest/k1695_r6_lean/REPORT.md`,
`engine/harvest/k1695_r6_lean2/REPORT.md`, `engine/harvest/k1695_r6_lean4/REPORT.md` (files `K1695/TranspositionLemma.lean`,
`K1695/TranspositionLemmaFull.lean`).

## Tasks
T1. Rebuild both files with `cd lean/proofenv && ~/.elan/bin/lake env lean <file>`; `#print axioms` for every theorem
    (scratch file importing them; list any declaration whose axiom set is NOT exactly [propext, Classical.choice, Quot.sound]).
T2. For each of T0, T1, T2 (both directions), T3, T4: quote the Lean theorem(s) verbatim, translate to plain mathematics,
    and compare hypothesis-by-hypothesis with the registry statement: field generality; n-range (n ≥ 3? n = 4 only?);
    μ ≠ 0 where required; the permutation is a genuine transposition of two DISTINCT indices; "rank" = Matrix.rank over
    the field; "derogatory" encoded how; for T4: which degree of the minimal polynomial is covered (quadratic only /
    cubic fallback / general), and whether the "power-basis decomposition" is a hypothesis (weaker) or derived.
T3. Vacuity: instantiate T2-iff and T4 at concrete n=4 matrices over ℚ and ZMod 3 with `example`.
T4. Verdict: is the sentence "Lemma T is fully kernel-checked except general-degree T4" EXACT, OVERSTATED, or
    UNDERSTATED? Give the exact replacement sentence you would put in the registry.

## Report
T1–T4, verbatim Lean statements, then `DONE-LEAN4FID`.
