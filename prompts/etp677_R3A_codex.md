# R3-A: the T3-amplification attack on (Q'), plus structured counterexample search

Read prompts/etp677_R3_common.md first (established toolkit + blocked routes).
Do not read problems/etp677/ reports or campaign_registry.md. No internet.

PRIMARY (R3-A): execute the T3-AMPLIFICATION program — the one live route
nobody has run. T3's proof shows: x ∈ F_{pq} ⟹ Λ_p(x) ∉ F_{pq} (via L4).
Amplify: suppose x, x' ∈ F_{pq} with x ≠ x'. Apply KEY at (p,x), (q,x),
(p,x'), (q,x') simultaneously and hunt for derived exclusions of the form
"φ(x) ∈ F_{pq} is impossible" for MORE maps φ than just Λ_p — each new
independent exclusion roughly halves the ⌊n/2⌋ bound; pushing |F_{pq}| < 1
proves (Q'). Candidate maps to test for exclusion: Λ_q, Λ_pΛ_q, L_p, L_q,
Λ_p², the mixed words in {L_p,L_q,Λ_p,Λ_q} of length ≤ 3, and the maps
x ↦ x*v for v := p*x = q*x. Work the algebra CAREFULLY (this is the core
task); verify every derived exclusion computationally against the known
models (they have F_{pq} patterns since distinct rows DO agree somewhere in
non-Latin... no — known models are Latin so F_{pq} = ∅ there; instead verify
exclusions against random left quasigroups satisfying KEY on subsets, or
verify the derivations symbolically). If amplification stalls, characterize
exactly the algebraic obstruction.

SECONDARY (R3-D): structured counterexample hunt at odd composite orders.
The second linear-branch factor G⁴+G³+2G²+2G+1 and module constructions
over rings: enumerate solutions over Z_15, Z_21, Z_25, Z_27, Z_33, F_25,
F_27, Z_5×Z_5, Z_3×Z_9 etc. (linear gives quasigroups — the POINT is to
then attempt NON-linear perturbations: take a linear model and modify k ≥ 2
cells/rows preserving row-Latin + E677 — use the exact 5-instance violation
anatomy: a would-be counterexample's violated-instance pattern is known, so
search perturbations that REPAIR all 677 instances while keeping column 0
missing value 0; encode as SAT with your own generator if useful, kissat is
at tools/kissat/build/kissat).

Write the complete report to problems/etp677/R3A_codex_report.md: every
derived exclusion with full proof, the amplification ledger (which maps
excluded, current bound on |F_{pq}|), counterexample search coverage, and
the exact remaining gap. Persist per the campaign discipline.
