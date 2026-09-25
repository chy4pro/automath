# TICKET (codex, engineering + bounded computation; no claims) — portfolio candidate P1:
# does the order-5 law E17260 have a nontrivial FINITE model?  (ETP order-5 chapter, status
# "unknown" as of 2026-08-30: https://teorth.github.io/equational_theories/blueprint/order-5-austin-laws.html)

## The law (verbatim from the chapter page; ◇ is the magma operation, variables x,y,z)
E17260:  x = (y ◇ x) ◇ (z ◇ (x ◇ (z ◇ z)))
Its dual E28740: x = (((y ◇ y) ◇ x) ◇ y) ◇ (x ◇ z)  — a model of one gives a model of the other
(reverse the operation), so search ONLY E17260.
Sanity you must print: the dual computed mechanically from E17260 equals E28740 up to renaming.
Trivial (1-element) models exist; the question is a model of order n ≥ 2.  The chapter notes that
Vampire indicates nontrivial (possibly infinite) models exist.

## Deliverable 1 — encoder `problems/etp_o5/e17260_cnf.py`
Input: n.  One-hot table T[a][b][c] ("a◇b = c"), exactly-one per (a,b).  Ground the law for all
(x,y,z) ∈ [n]^3 with auxiliary one-hot term variables for the five sub-terms, chaining
T-lookups (the standard term-evaluation encoding used in core_joint.py).  Symmetry breaking:
fix 0◇0 = 0 or 0◇0 = 1 as two cubes (one of them holds in any model up to isomorphism); optional
lex-leader row breaking only if it is exact (state the argument) — otherwise none.  Print
vars/clauses and sha256 per CNF.  Also emit `check_table.py`: reads a decoded table, verifies the
law at all n^3 triples, prints PASS/FAIL — no encoder import.

## Deliverable 2 — local probes (allowed: tiny instances only, ≤ 600 s total)
n = 2,3,4,5,6 with kissat --time=60 each (both cubes); decode any SAT model, verify it with
check_table.py, print the table.  Expect UNSAT at small n (the project would have found small
models); report the exact verdicts.  Do NOT run n ≥ 7 locally.

## Deliverable 3 — cloud batch card (not launched by you)
CNFs for n = 7..16 (both cubes each) staged with sha256; a path-launched runner variant of
problems/etp677/ext/startup_proof_min.sh contract (kissat + DRAT + on-VM drat-trim) is fine as
is — inputs in the bucket sub `o5a/in/`; card with --scopes=storage-rw, pd-standard, e2-highcpu-2,
CAP 12 h per CNF.  A SAT verdict must upload the model (`-q` off; keep the `v` lines) so it can be
decoded and re-checked independently; UNSAT gets the proof as usual.

## Deliverable 4 — Lean stub
`lean/etp677_ext/Ext_O5_E17260.lean` skeleton: the law as a Prop over a `Fin n` table and a
`decide`/`bv_decide` theorem template that takes a concrete table (to be filled if a witness
appears).  Build only if the existing project builds in < 5 min (ETP677_MATHLIB_CACHE set!).

## Report
`engine/out/codex/etp_e17260_report.md` ending `DONE-E17260`: verdict table for n=2..6, CNF
sizes/hashes for 7..16, the card.  No claim of any kind about existence; a witness, if found,
is data to be re-verified by line-677 (independent checker + Lean) before any word leaves.
