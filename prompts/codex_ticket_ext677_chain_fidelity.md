# TICKET CHAINFID — end-to-end fidelity audit of the Lean-certified reduction chain for ETP 677 (Ext677 L1–L9, Collision C1–C5)

Self-contained; no internet. Do NOT modify existing files. Write only under `problems/etp677/chain_fidelity/` and the
report at `engine/out/codex/etp677_chain_fidelity_report.md` ending with `DONE-CHAINFID`. ~75 min.

## Object
line-677 claims (registry `problems/etp677/campaign_registry.md`, R46 STEP 8–15, wording corrected at STEP 12) that the
interpretation of every extension-instance solver verdict is Lean-certified: `lean/etp677_ext/Ext677.lean` (L1–L6),
`Ext677Quot.lean` (L7 coordinatization, L8 minimal-counterexample dichotomy), `Ext677Glue.lean` (L9), `Ext677Collision.lean`
(C1–C5). The human reduction argument is in `problems/etp677/ext/` (R7A_report.md, REGISTER_A.md) and the encoder is
`problems/etp677/ext/ext_cnf.py` (independently verified: engine/out/codex/etp677_ext_verify_report.md). The audit
`engine/out/codex/etp677_r46_audit_report.md` (STEP 9 finding) said the Lean theorems certified "links, not the whole".

## Tasks
T1. Rebuild: `cd lean/etp677_ext && ~/.elan/bin/lake build`; `#print axioms` on every theorem of the four modules; list
    any sorry/axiom anomaly.
T2. Chain reconstruction: write down, as a numbered list of mathematical statements S1…Sk, the COMPLETE argument from
    "a minimal finite counterexample N to E677⟹E255 exists" to "then for some base B in the enumerated list and some
    fibre size m, the CNF ext_<B>_m is satisfiable" (i.e. UNSAT of all enumerated instances for (B,m) closes exactly the
    cell the registry now says it closes). For each S_i say: Lean theorem name (verbatim statement quoted) / human proof
    location / computational check location / NOT COVERED. Be precise about: quotient existence, choice of B up to
    isomorphism (which bases are enumerated and why that list is exhaustive for the claimed cell — automorphism orbits,
    level protection, m=9 conditional on the order-9 classification), the encoder's faithfulness (ext_verify), and the
    outcome map (SAT decode, UNSAT+DRAT, timeout = no verdict).
T3. Wording check: quote the registry's current sentence(s) describing what an ext UNSAT proves and what is "Lean-certified";
    verdict EXACT / OVERSTATED / UNDERSTATED with replacement wording.
T4. List the remaining human-only links in order of risk.

## Report
T1–T4 (the S1…Sk table is the core), then `DONE-CHAINFID`.
