# TICKET LEAN-CERT — machine-checked Lean 4 certificates for the four refutation objects

Goal: turn today's counterexample objects into Lean-checked facts, so the refutations of
(L0), (ROWCAP), (ROWCAP-FULL) and (ROWCAP-D0) rest on a kernel-checked certificate rather
than on Python checkers.

Objects (JSON with "table", "lines", "nu"):
- problems/etp677/R45_L02_q3_3perf_delta0.json  (q=3: 3 perfect rows {4,6,10}, delta==0)
- problems/etp677/L03_q3_four_perfect_delta0.json (q=3: 4 perfect rows {4,5,6,10}, delta==0)
- problems/etp677/L05/L05_q4_P6_delta0.json (q=4: 6 perfect rows {0,1,2,5,15,17}, delta==0)
- problems/etp677/L06/L06_q7_P14_delta0_best.json (q=7: 14 perfect rows, delta==0)

Definitions (all finite; n = q^2+q+1; T : Fin n -> Fin n -> Fin n):
 (B1) every row of T is a permutation of Fin n;
 (B2) for every column c the value nu c is attained exactly q+1 times, on exactly the set
      lines c; every other value at most once; exactly q values are absent;
 (B3) the sets lines c (c : Fin n) form a projective plane of order q on Fin n: every pair of
      distinct points lies on exactly one line;
 (B4) nu is a bijection.
 ldiv a v := the unique w with T a w = v;  Xi t x := ldiv x (ldiv t x);
 E t v := #{x | Xi t x = v};  N t v := #{a | T a t = v};  delta v := (sum_t E t v) - n;
 row r is PERFECT iff for all v, E r v = N r v.

Deliverable: a Lean 4 project under lean/etp677_certs/ (use the toolchain in ~/.elan/bin; a
lakefile with Mathlib is fine if it builds within reasonable time — otherwise stdlib only and
your own Fin-based definitions). For each object: a file that embeds the table as a literal,
defines the predicates above computably, and proves by `decide` / `native_decide` (state which)
the theorem "this table is a branch object AND rows R are perfect AND delta == 0" with R the
stated row set. Then a NEGATIVE CONTROL: the same statement for a two-cell perturbation of the
q=3 object must FAIL to typecheck (show the error) or, better, prove its negation.
Report: engine/out/codex/etp677_lean_certs_report.md — build command, per-object theorem name,
elapsed times, which decision procedure, the negative-control evidence; end with DONE-LEANCERT.
Rules: no system-wide installs (Mathlib cache into the project dir is fine); no network beyond
lake dependencies; keep everything under lean/etp677_certs/ and engine/out/codex/.
