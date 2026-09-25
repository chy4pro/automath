
# Finite-combinatorics research brief (self-contained). Construction task.

## Setting
Fix an integer q >= 2 and n = q^2+q+1.  M is a set of size n carrying a projective
plane Pi of order q (points = M, n lines each of size q+1, two points on a unique
line, two lines meet in a unique point).

A **branch object** is a binary operation * : M x M -> M (write the table with rows
indexed by the left argument) such that

 (a) every ROW is a permutation: for each x, the map y |-> x*y is a bijection of M.
     Write Lam_x for its inverse:  Lam_x(y) = x\y.
 (b) every COLUMN c is "block-structured": there is a line ell_c in Pi and a value
     nu(c) in M with  {a : a*c = nu(c)} = ell_c, and every other value occurs at most
     once in column c.  The map c |-> ell_c is a bijection columns -> lines.
     Hence column c omits exactly q values;  D_c := M \ {a*c : a in M},  |D_c| = q.
 (c) [PROVED, do not re-derive] nu : M -> M is automatically a bijection.

Derived objects:
  Xi_t(x) := x\(t\x) = Lam_x(Lam_t(x))            ("the Xi-array", an n x n array)
  E(t,v)  := #{x : Xi_t(x) = v}
  N(t,v)  := #{a : a*t = v}  = multiplicity of v in column t.
  Profile of N(t,.):  q+1 at v = nu(t);  1 on M \ (D_t u {nu(t)});  0 on D_t.
  Row t of the Xi-array is **PERFECT** iff E(t,.) = N(t,.), i.e. Xi_t takes the value
  nu(t) exactly q+1 times, omits exactly D_t, and is injective on the rest.
  P := set of perfect rows.
  g(c)   := nu(c)\c   (equivalently nu(c)*g(c) = c);   b(v) := |g^{-1}(v)|
  m(v)   := #{x : x in D_{x*v}}
  delta(v) := (Sum_t E(t,v)) - n .

## PROVED toolkit (use freely; all proved for all q; do NOT re-prove)
 (F0)  Sum_v b(v) = n;  Sum_v m(v) = nq;  Sum_v delta(v) = 0.
       For each value x, #{c : x in D_c} = q exactly.
 (F1) [deficit]  delta(v) = q*b(v) - m(v).
 (F2) [phi-fusion]  phi_t(x) := x * Xi_t(x) = Lam_t(x) for all t,x.  Hence phi_t is a
       bijection.  This is the whole content of "the Xi-array is realized by a table".
 (F3) [loc]  x in ell_v AND Xi_t(x) = v   <=>   x = t*nu(v).
       Corollary: |Xi_t^{-1}(v) ^ ell_v| <= 1 for all t,v.
 (F4) [T-count]  T_v := {t : some x in ell_v has Xi_t(x) = v} = R_{nu(v)}^{-1}(ell_v)
       where R_c(t) := t*c.  Hence EXACTLY
          |T_v| = (q+1) + q*[nu^2(v) in ell_v] - |ell_v ^ D_{nu(v)}| .
       When row nu(v) is PERFECT, D_{nu(v)} is readable off the Xi-array (it is the
       omitted set of Xi_{nu(v)}), so |T_v| is then pinned exactly by the array.
 (F5) [REAL-1]  For every c:  g(c) = nu^{-1}(c)  <=>  nu(c) in ell_{nu^{-1}(c)}.
       Consequently  A := #{v : nu^2(v) in ell_v} = #{c : g(c) = nu^{-1}(c)}.
 (F6) [pencil]  For every column c and every r in ell_c (perfect or not):
          Xi_r(nu(c)) = g(c).
 (F7) [b-cap]  delta(v) <= 0  ==>  b(v) <= q.
 (F8) [block-hit form]  x in ell_{Xi_t(x)}  <=>  Xi_t(x) = nu^{-1}(Lam_t(x)).
       With h_t := #{x : x in ell_{Xi_t(x)}} one has h_t = #{v : t*nu(v) in ell_v}
       and  Sum_t h_t = Sum_v |T_v| = n(q+1) + qA - Sum_v |ell_v ^ D_{nu(v)}|.
 (F9) [closure]  Read (F2) as a table-completion rule with v := Xi_t(x):
          forward:   x*v = u known  ==>  t*u = x
          backward:  Lam_t(x) = c known  ==>  x*v = c
       Seeding with the block cells a*c = nu(c) (a in ell_c) and propagating to a
       fixpoint (with "rows are permutations", and for a perfect row c "column c
       carries exactly M \ ({nu(c)} u D_c) off the block") is sound: every genuine
       table satisfies it, so a closure CONFLICT certifies that the Xi-array is not
       realized by any table.
 (F10) [dual]  D(a,b) := a\b is again a branch object, with nu_D = nu^{-1},
       ell^D_b = ell_{nu^{-1}(b)}, N_D = N^T, and double dual = primal.  delta == 0 is
       NOT preserved by this duality.

## The situation, exactly
* "delta == 0" (the TRACE sub-branch) is a necessary condition for the target
  property (N): "E(t,v) = N(t,v) for all t,v", i.e. ALL n rows perfect.
* KNOWN [theorem at q=2, conjecture in general, the FULL-branch bound]:  |P| <= q+1.
* KNOWN [theorem at q=2 by exhaustion; THE TARGET in general]: on the delta == 0
  sub-branch,  |P| <= q.
* KNOWN [measured exactly, q=2, one realizable design]: the first-order system
  {(a),(b),(c) + delta == 0 + F3 + F4 + F9-closure} admits |P| = q+1 PHANTOM arrays
  (arrays satisfying every listed constraint but realized by no table).  So the
  residual one-row gap CANNOT be closed by re-imposing the constraints above; a NEW
  proved consequence is required.

## TARGET OF THIS BRIEF
Produce candidate PROOF STEPS toward:  delta == 0  ==>  |P| <= q.
The designated mechanism to develop is the FUSION of (F4)'s exact form with the
deficit law delta(v) = q*b(v) - m(v) = 0.  A useful elementary observation you may
build on (proved): m(v) >= |ell_v ^ D_{nu(v)}| always, because x in ell_v implies
x*v = nu(v); so under delta == 0,  |ell_v ^ D_{nu(v)}| <= q*b(v).  Also, since
b(v) >= 1 for all v would force b == 1 (as Sum_v b(v) = n over n values), under
delta == 0 exactly one of the following holds:
   (i)  b == 1, i.e. g is a bijection, equivalently m == q;  or
   (ii) b(v) = 0 for some v, and then m(v) = 0, i.e. NO x at all has x in D_{x*v}.

## DEAD ROUTES (do not propose; they are proved closed)
* Pure marginal / Gale-Ryser / transportation counting on the (t,x,v) marginals plus
  column structure: PROVED closed at every q (the capacity is tight at P = M).
* "The sets C_r := Fix(L_r R_{nu(r)}) are pairwise disjoint over perfect rows r":
  REFUTED (a real delta==0 witness at q=2 has C_2 ^ C_3 = {5}).  Also |C_r ^ C_s|<=1
  is insufficient.
* Any ROW-LOCAL argument (constraints involving one perfect row at a time):
  refuted by explicit phantoms; the needed constraint must be CROSS-ROW.
* Per-cell concentration bounds max E < max N: REFUTED at every q.
* Translation-invariant tables x*y = x + h(y-x) on Z_n: there the perfect-row count
  is 0 or n and delta == 0 holds identically, so the family carries zero information;
  it is also empty of perfect rows at q=3.  Do not use it.
* Assuming b == 1 without saying so: delta == 0 does NOT force b == 1 (at q=2,
  6561 of 17195 delta==0 tables have max b = 2).

## RULES FOR YOUR ANSWER (construction-only; strict)
1. You are a CONSTRUCTOR, not a certifier.  Output candidate steps with COMPLETE
   self-contained proofs from (F0)-(F10) and (a)-(c).  Every step you cannot fully
   prove must be labelled `CONJECTURE:` with the exact missing link named in one line.
2. NEVER claim the whole target is solved.  Partial, provable, NEW steps are the
   deliverable.  A single genuinely new proved lemma is worth more than a long sketch.
3. No literature, no external references, no internet.  Everything from the above.
4. State clearly for each claim whether it is proved for ALL q or only q = 2.
5. If your line needs an object (a design, an array, a table), give it EXPLICITLY and
   check it against every constraint (a)-(c), (F5) included -- unrealizable design
   data certifies nothing.
6. HARD WORD CAP: 1100 words.  No restatement of this brief, no pleasantries,
   no summary section.  Start directly with your first claim.

## YOUR SPECIFIC ANGLE
Angle H -- the block-hit profile of a PERFECT row.
h_t = #{x : x in ell_{Xi_t(x)}} = #{v : t in T_v} = #{v : t*nu(v) in ell_v} (F8).
Question 1: for a PERFECT row r, is h_r pinned or bounded by design data?  Use (F6)
(Xi_r(nu(c)) = g(c) for r in ell_c, so r contributes a block hit at x = nu(c) exactly
when g(c) = nu^{-1}(c), i.e. exactly on the set A of (F5)), plus perfectness
(Xi_r omits exactly D_r, hits nu(r) exactly q+1 times).
Question 2: combine Sum_t h_t = n(q+1) + qA - Sum_v |ell_v ^ D_{nu(v)}| with
delta == 0 (via |ell_v ^ D_{nu(v)}| <= m(v) = q b(v)) to bound Sum_{r in P} h_r from
BOTH sides, and derive a contradiction for |P| = q+1.  Give exact constants at general
q; verify your inequality is not vacuous by instantiating at q = 2, n = 7.
