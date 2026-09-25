# TICKET K6AUDIT — adversarial audit of the round-6 claims for Kourovka 16.95 (line-k1695 registry §R6.*)

Self-contained. Do NOT modify existing files. Write only under `problems/k1695/r6_audit/` and the report at
`engine/out/codex/k1695_r6_audit_report.md` ending with the literal line `DONE-K6AUDIT`. Time budget ~90 min.
Model this audit on `engine/out/codex/etp677_r46_audit_report.md` (a sibling audit that found two consequential
overstatements): a claim-by-claim table with the evidence artifact, what the evidence ACTUALLY shows, and a verdict
from {EXACT, OVERSTATED, UNVERIFIABLE, WRONG}, plus a "bottom line" section listing every consequential overstatement
with replacement wording.

## Object of audit
The registry file: `problems/k1695/campaign_registry.md` — sections §R6.1 through the latest §R6.x (round 6: Lemma T = "transposition is a
rank-one update", the n=4 stratum-(b) theorem, the (S)/(S′)/(T_m) conjectures and scans, the Lean formalisations,
K6-N4/N4b/N4c, K6-T/T2, K6-S/S2). Evidence artifacts live under `engine/harvest/k1695_r6_*/` (REPORT.md, C sources,
logs, Lean files), `lean/proofenv/K1695/`, `problems/k1695/`, `engine/briefs/k1695_r6_*/TICKET.md`.

## What to check, claim by claim
1. Every "PROVED", "THEOREM", "BANKED", "kernel-checked" in §R6: locate the artifact; for Lean claims rebuild
   (`cd lean/proofenv && ~/.elan/bin/lake env lean K1695/<file>.lean`) and run `#print axioms` yourself; for C/Python
   exhaustive claims re-run the stated command when it takes < 10 min, otherwise re-run a documented prefix and
   check the population formula (|GL(n,q)| = ∏(q^n − q^i)); compare the statement in the registry with the statement
   in the artifact word by word (hypotheses such as μ ≠ 0, n ≥ 3, "every transposition", "every field").
2. Every equivalence claimed between conjectures ((T_{n−1}) ⟹ (S) ⟹ 16.95; (S′)_n ⟺ (T_{n−1}); "(T_2) ⟺ every
   A ∈ GL(3,F), every i, some AP_σ has e_i cyclic"): find where it is proved; if only asserted, say so.
3. Every "0 failures / exhaustive" count: does the log show the population equals the formula? Were VOID cells
   (K6-S cells 4–5) removed from all downstream statements?
4. Status words: is anything called "closed", "theorem", "banked" that the evidence only supports as "provisional",
   "computed on finite fields", or "conjectured"? Is the n=4 status stated consistently everywhere (stratum (b)
   theorem vs stratum (a) open)?
5. Novelty/attribution: does §R6 claim novelty for anything that the artifacts themselves cite as classical
   (e.g. rank-one update inequalities)? Flag, do not search the internet.

## Report
Bottom line (≤ 6 bullets, consequential items only) → claim table → list of artifacts you re-ran with commands and
outcomes → `DONE-K6AUDIT`. Never soften: if a claim is exact, say EXACT; if it is overstated, give the replacement
sentence.
