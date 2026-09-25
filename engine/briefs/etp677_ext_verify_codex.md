# CODEX TICKET — INDEPENDENT VERIFICATION of the extension-with-defect instrument (R46)
# Adversarial cross-family check. Repo: $HOME/workspace/claudecode/automath.
# Code in ENGLISH only. Local compute: pure Python + kissat runs of at most 60 s each.
# No cloud action. Do NOT modify files under problems/etp677/ext/ — write your own under
# problems/etp677/ext/verify_codex/.

## What is being claimed (the object under review)
`problems/etp677/ext/ext_cnf.py` emits a CNF that is SATISFIABLE iff there is a
"pair-indexed extension" of a fixed finite 677-magma B (tables in the script: f7a = F_7 with
x<>y = 4x+3y; f7b = F_7 with 4x+y; m9 = F_3^2 with x<>y = x + G y, G = [[0,1],[1,1]]) by an
m-element fibre, i.e. a magma on B x M with (x,s)*(y,t) = (x<>y, s <>_{x,y} t), such that
(a) every fibre op <>_{x,y} has permutation rows (t -> s <>_{x,y} t bijective),
(b) the big magma satisfies E677  x = y*(x*((y*x)*y)),
(c) E255  x = ((x*x)*x)*x  FAILS at some point (a, sigma) with a = 1 in B.
The encoder does NOT encode E677 on the (nb*m)^2 table directly. It uses the blueprint
identity (Equational Theories Project blueprint ch. 13, eq. (4); also registry (R9-A/eq4)):
   E677 on B x M  <=>  for all base pairs (x,y) and all s,t in M:
      s = t <>_{P1} ( s <>_{P2} ( (t <>_{P3} s) <>_{P4} t ) )
      P1 = (y, y\x),  P2 = (x, (y<>x)<>y),  P3 = (y, x),  P4 = (y<>x, y),
and the defect criterion (registry (R7-A Thm 2)/(R7-C/witness)): E255 fails at (a,sigma) iff
no s has s <>_{(x_a,a)} sigma = sigma, where x_a is the unique left unit of a in B.
It also uses two WLOG reductions: the defect level may be taken a = 1 because the base
automorphism group acts transitively on non-zero elements (scaling x -> lambda x on F_7; the
unit group of F_3[G] = F_9 on F_3^2); and a defect cannot sit over the idempotent level 0 when
m < 12 (instance (0,0) is E677 on M itself, and all 677-magmas of order < 12 satisfy E255).
Encoding: X[p][s][t][v] one-hot, p = x*nb + y, var = 1 + ((p*m+s)*m+t)*m+v; rows permutations;
eq. (4) through aux U2/U3 with implication clauses only; defect via selector variables.

## Your tasks (all mandatory; report each with its own verdict)
V1  DERIVATION. From E677 on the product magma, re-derive eq. (4) and the subscript quadruple
    P1..P4 yourself (do not copy). State whether the encoder's quadruple is correct. Then
    re-derive the defect criterion from Lemma 13.1(ii) of the blueprint (y*x = x solvable
    iff E255 at x). State whether the star pair (x_a, a) is right and check the encoder's
    printed star indices (f7a: 22, f7b: 1, m9: 55).
V2  WLOG. Prove or refute: (i) the scaling maps are automorphisms of each base and act
    transitively on non-zero elements; (ii) a defect at level lambda*a transports to level a;
    (iii) "instance (0,0) is E677 on M" for these bases; (iv) all 677-magmas of order m in
    {5,7,9} satisfy E255 (cite how you know — exhaustive check you run yourself is best:
    enumerate all 677-magmas of order 5 and 7 with your own search, bounded to 60 s, or use
    the ETP literature and say so).
V3  INDEPENDENT CHECKER. Write `verify_codex/ext_check.py` that, given a base table and the
    nb^2 fibre-op tables, builds the (nb*m)x(nb*m) table and checks E677 directly on all
    pairs and E255 at every point. Then build BIDIRECTIONAL TESTS of the CNF:
      (a) 20 random gauge-twisted direct products (s <>_{x,y} t := pi_{x<>y}(op(pi_x^-1 s,
          pi_y^-1 t)), random pi_x, op a known 677 op on M, m = 5): your checker must say
          E677 holds; fixing all ops by unit clauses in the encoder's CNF (use its .map
          variable formula) must give SAT (kissat, seconds).
      (b) 20 MIS-WIRED twists (output gauge pi_x instead of pi_{x<>y}) and 20 single-cell
          perturbations of a good twist: your checker must say E677 fails; the fixed CNF
          must be UNSAT. Report the 4 counts (a-SAT, a-E677, b-UNSAT, b-fail) out of 60.
      (c) Decode the encoder's own control model `ext/out/ctl_f7a_m5_product.log` with YOUR
          checker (not with ext_decode_verify.py) and confirm: order 35, E677 holds, E255 holds.
V4  DEFECT CLAUSE. Construct by hand (or by search, 60 s cap) a left-quasigroup op on 5
    elements whose column 0 misses 0; fix the star op to it and all other ops free, m=5,
    base f7a, defect level 1; the CNF must NOT be trivially UNSAT for a reason unrelated to
    eq. (4) — i.e. show that with the defect clause removed and the same star fixed, the
    remaining clauses are satisfiable only if eq. (4) allows it. (Purpose: demonstrate the
    defect clause is doing exactly "column sigma of the star misses sigma" and nothing more.)
    Also verify the selector encoding: for the 35-element product with the star replaced by
    your defective op, decode-and-check with your checker which points fail E255.
V5  ANY OTHER GAP. Look for reasons the free instances (ext_f7a_m5 etc.) could be UNSAT for
    a trivial/encoding reason: at-most-one/at-least-one bugs, aux variable collisions (check
    the numbering: aux blocks start at nb^2*m^3), a missing case in the row-permutation
    constraints, an off-by-one in the map. Grep the CNF for the literal counts you expect.

## Deliverables
`problems/etp677/ext/verify_codex/{ext_check.py, tests.py, results.out}` and
`engine/out/codex/etp677_ext_verify_report.md` with sections V1–V5, each ending in
VERIFIED / DEFECT FOUND (with the concrete defect) / CANNOT DECIDE, ending with the line
DONE-EXTVERIFY. Minimum effort: run every test; do not summarize a test you did not run.
