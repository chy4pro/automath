# CODEX TICKET (engineering + exact computation; any tier — tables and verified facts only, no
# conjectural claims) — STRUCTURE CENSUS of every finite E677 magma we have: congruence
# lattice, quotients, and whether each model is an iterated extension of AFFINE pieces.
# Repo: $HOME/workspace/claudecode/automath. Python 3 / numpy. Local caps: ≤ 600 s per
# table, ≤ 2 heavy processes, sequential (the box is memory-constrained: keep RSS < 1 GB).
# DONE marker: DONE-STRUCT.

## Inputs
- problems/etp677/ext/db/*.txt — 161 tables (row i = products i*j, 2-digit ints), orders 5–49;
  problems/etp677/ext/db/pro217_idemfree.json ({"table": [[...]]}, order 217).
- problems/etp677/eprime/survivors_p31.json — 6,900 laws of the switching-type family F7×F31
  (fields documented in enum_family.py / profile.py); rebuild each table from its law.
- The explicit models: T7 = 4x+y+6 mod 7; 4x+3y mod 7; F13 affine (find (α,β,γ) by the
  E677 conditions αβ(1+β²)=1, α+α²β²+β³=0 over F13); F31 5x−4y+1; M49ε (4x+y, 4s+t+[x=y=0]);
  M217ε, R217 (4q+3r, 5s−4t+[q=r=0]).
Every table: first verify E677 on all pairs and record E255 and the idempotent count
(all must be E677; report any that is not).

## Tasks
1. Congruences: for each table compute ALL congruences (for n ≤ 49: closure of every pair
   (x,y) under products by all z, union-find; then joins; report the lattice size, the
   minimal non-trivial congruences and the maximal proper ones with class-size multisets).
   For order 217 compute at least the principal congruences and their joins (feasible).
2. Quotients: for each maximal proper congruence, build the quotient table, canonicalise
   (isomorphism test by row-invariant hashing + backtracking), and identify it against the
   catalogue: affine over F_p (fit x*y = αx+βy+γ by solving on three points and verifying),
   or a db table, or "new". Record the FIBRE STRUCTURE: for each quotient class pair (X,Y),
   the map (s,t) ↦ product's fibre coordinate — is it affine in (s,t) with coefficients
   depending only on (X,Y)? on the product class? on [hub]? (i.e. which of the eprime
   parametrisations F1/F2/F3 or a more general pair-indexed rule it obeys).
3. Decomposition tree: iterate on each quotient until simple; output for every model a tree
   whose leaves are simple magmas with their identification (affine over F_p / other), and a
   flag "all leaves affine and all fibre rules affine-in-(s,t) with pair-dependent constants"
   (call this SWITCHING-TYPE). Report the list of models that are NOT switching-type, with
   the first non-affine fibre rule exhibited explicitly (a small table).
4. Simple models: list every simple E677 magma in the catalogue (no non-trivial congruence)
   with order, idempotent count, |Im U|, left-multiplication-group order and primitivity
   (compute ⟨L_x⟩ as a permutation group via a simple Schreier–Sims or sympy's
   PermutationGroup; report whether it is affine, i.e. has a regular normal elementary
   abelian subgroup — sympy can give order and is_primitive; for the abelian normal
   subgroup test use the structure: order p^k · (group of affine maps) and check that the
   translations x ↦ x+c (if the table is affine) are in the group).
5. Report: one table per model (order, #idem, lattice size, decomposition tree in one
   line, switching-type flag) + the summary: how many models are switching-type; the full
   list of exceptions with evidence; the list of simple models and their groups.

## Deliverables
problems/etp677/structure/{census.py, iso.py, results.json, report.md} and
engine/out/codex/etp677_structure_report.md ending with DONE-STRUCT.
