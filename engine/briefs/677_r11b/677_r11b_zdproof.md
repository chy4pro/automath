
# Finite-combinatorics research brief (self-contained). Construction task.

## Setting
Fix an integer q >= 2 and n = q^2+q+1.  M is a set of size n carrying a projective
plane Pi of order q (n lines, each of size q+1; two points on a unique line; two
lines meet in a unique point).

A **branch object** is a binary operation * : M x M -> M such that
 (a) every ROW is a permutation: for each x, y |-> x*y is a bijection.  Lam_x is its
     inverse: Lam_x(y) = x\y.
 (b) every COLUMN c is block-structured: there is a line ell_c in Pi and a value
     nu(c) with {a : a*c = nu(c)} = ell_c, every other value occurring at most once
     in column c; c |-> ell_c is a bijection columns -> lines.  So column c omits
     exactly q values:  D_c := M \ {a*c : a in M},  |D_c| = q.
 (c) [PROVED] nu is automatically a bijection.

Derived:
  Xi_t(x) := x\(t\x) = Lam_x(Lam_t(x))            (the n x n "Xi-array")
  E(t,v)  := #{x : Xi_t(x) = v};   N(t,v) := #{a : a*t = v}
  N(t,.) profile: q+1 at nu(t); 1 on M \ (D_t u {nu(t)}); 0 on D_t.
  Row t of the array is PERFECT iff E(t,.) = N(t,.).  P := set of perfect rows.
  pencil(x) := {v : x in ell_v}, of size q+1.
  Z(x) := {v : v not in {Xi_t(x) : t in M}}, the values MISSED by COLUMN x of the
          array;  |Z(x)| = q  (see (F1)).
  g(c) := nu(c)\c;  b(v) := |g^{-1}(v)|;  m(v) := #{x : x in D_{x*v}};
  delta(v) := (Sum_t E(t,v)) - n.

## PROVED toolkit (all q; use freely, do NOT re-prove)
 (F0) Sum_v b(v) = n; Sum_v m(v) = nq; Sum_v delta(v) = 0; for each value x,
      #{c : x in D_c} = q exactly.
 (F1) [vertical profile] #{t : Xi_t(x) = v} = N(x*v, x).  Hence for each x the map
      t |-> Xi_t(x) has fibre profile exactly {q+1 once, 1 x q^2, 0 x q}: the big
      fibre is over v_0(x) = x\nu^{-1}(x) and is carried by the rows of
      ell_{nu^{-1}(x)}; the q empty fibres are Z(x).
 (F2) [deficit] delta(v) = q*b(v) - m(v).
 (F3) [phi-fusion] phi_t(x) := x * Xi_t(x) = Lam_t(x); hence phi_t is a bijection.
      This is the entire content of "the array is realized by a table".
 (F4) [loc] x in ell_v AND Xi_t(x) = v  <=>  x = t*nu(v).
      Corollary |Xi_t^{-1}(v) ^ ell_v| <= 1.
 (F5) [T-count] T_v := {t : some x in ell_v has Xi_t(x) = v} = R_{nu(v)}^{-1}(ell_v),
      so |T_v| = (q+1) + q*[nu^2(v) in ell_v] - |ell_v ^ D_{nu(v)}|.
 (F6) [REAL-1] g(c) = nu^{-1}(c) <=> nu(c) in ell_{nu^{-1}(c)}; hence
      A := #{v : nu^2(v) in ell_v} = #{c : g(c) = nu^{-1}(c)}.
 (F7) [pencil/skeleton] for every column c and every r in ell_c: Xi_r(nu(c)) = g(c).
 (F8) [b-cap] delta(v) <= 0 ==> b(v) <= q.
 (F9) [closure] Read (F3) as a table rule with v := Xi_t(x):
        forward  x*v = u known ==> t*u = x;   backward  Lam_t(x) = c known ==> x*v = c.
      Seeding with the block cells a*c = nu(c) (a in ell_c) and propagating to a
      fixpoint (with "rows are permutations"; and for a perfect row c "column c
      carries exactly M \ ({nu(c)} u D_c) off the block") is SOUND, so a closure
      conflict certifies that the array is realized by no table.
 (F10) [dual] D(a,b) := a\b is again a branch object with nu_D = nu^{-1},
      ell^D_b = ell_{nu^{-1}(b)}, N_D = N^T; delta == 0 is NOT preserved.

## NEW (this is the frontier; it is PROVED, all q)
 (F11) **(ZD)**   v in Z(x)  <=>  x in D_{x*v}   for all x, v.
      Proof: by (F1), #{t : Xi_t(x) = v} = N(x*v, x); the left side is 0 iff
      v in Z(x), the right side is 0 iff x in D_{x*v}.  QED.
      Equivalent forms:  D_c = {x : x\c in Z(x)};   C_x := {c : x in D_c}
      = {x*v : v in Z(x)}  (both of size q).
 (F12) **(ZD-block)** for x in ell_v one has x*v = nu(v), so v in Z(x) <=> x in
      D_{nu(v)}; hence |ell_v ^ D_{nu(v)}| = #{x in ell_v : v in Z(x)} is visible
      from the ARRAY for every v, with no perfectness hypothesis.  Therefore
 (F13) **(T-exact)**  |T_v| + #{x in ell_v : v in Z(x)} = (q+1) + q*[nu^2(v) in ell_v]
      for every v — an unconditional identity between array data and design data.
 (F14) **(ZD-C)** for each value x the q columns missing x are C_x = {x*v : v in Z(x)};
      in particular every v in pencil(x) ^ Z(x) contributes the column nu(v) to C_x,
      and every v in pencil(x) \ Z(x) forbids the column nu(v) from C_x.  If r is a
      perfect row then r in C_x <=> x is missing from row r of the array.

## The situation, exactly
* delta == 0 (the TRACE sub-branch) is necessary for the target property (N)
  ("E = N everywhere", i.e. all n rows perfect).  By (F1)+(F2), delta == 0 is
  EXACTLY the array statement "every value occurs exactly n times in the array".
* PROVED at q = 2 by exhaustion, CONJECTURE in general and THE TARGET:
      delta == 0  ==>  |P| <= q.
* PROVED at q = 2 (full branch) and conjectured in general: |P| <= q+1.
* MEASURED at q = 2 on one realizable design instance: the first-order system
  {(a),(b),(c) + delta==0 + (F4) + (F5) + (F9)} admits |P| = q+1 phantom arrays
  (arrays satisfying everything listed but realized by NO table).  Adding
  (F11)-(F14) kills ALL of them: every 3-subset becomes infeasible, i.e. the
  abstract cap drops from q+1 to q, matching reality.  So (ZD) is the missing
  first-order ingredient — but the q = 2 computation is NOT a proof at general q.

## DEAD ROUTES (proved closed; do not propose)
* Marginal / Gale-Ryser / transportation counting on the (t,x,v) marginals plus the
  column structure: provably closed at every q (capacity tight at P = M).
* "The sets C_r := Fix(L_r R_{nu(r)}) are pairwise disjoint over perfect rows":
  REFUTED; also |C_r ^ C_s| <= 1 is insufficient.
* Any ROW-LOCAL argument (one perfect row at a time): refuted by explicit phantoms.
* Per-cell concentration bounds max E < max N: refuted at every q.
* Translation-invariant tables x*y = x + h(y-x) on Z_n: perfect-row count there is
  0 or n and delta == 0 holds identically; the family carries zero information.
* Assuming b == 1 silently: delta == 0 does NOT force b == 1.  (But note: b(v) >= 1
  for all v would force b == 1, since Sum_v b(v) = n over n values.  So under
  delta == 0 either b == 1, or some b(v) = 0 and then m(v) = 0.)

## RULES FOR YOUR ANSWER (construction-only; strict)
1. You are a CONSTRUCTOR, not a certifier.  Give candidate steps with COMPLETE
   proofs from (a)-(c) and (F0)-(F14).  Anything not fully proved must be labelled
   `CONJECTURE:` with the missing link named in one line.
2. NEVER claim the whole target is solved.  One genuinely new PROVED lemma beats a
   long sketch.  State for each claim whether it is proved for ALL q or only q = 2.
3. No literature, no internet, no external references.
4. Any object you propose (design, array, table) must be given EXPLICITLY and
   checked against (a)-(c) and (F6); unrealizable design data certifies nothing.
5. HARD WORD CAP: 1100 words.  No restatement of this brief, no pleasantries, no
   summary section.  Start directly with your first claim.

## YOUR SPECIFIC ANGLE
Angle 1 (HEAD) -- prove the drop at general q.
Target: delta == 0 ==> |P| <= q, using (F11)-(F14) as the new input.  Concretely:
suppose |P| = q+1 and derive a contradiction.  Suggested skeleton to develop, refute
or replace: for each r in P the set D_r is array-visible; by (F14), r in C_x <=>
x in D_r, so the q+1 perfect rows partition the values x into 2^{q+1} classes by the
pattern (x in D_r)_{r in P}, while |C_x| = q forces at most q of the q+1 patterns to
be "in".  Count Sum_{r in P} |D_r| = (q+1)q two ways and collide it with the pencil
forcing of (F14) (v in pencil(x) ^ Z(x) contributes nu(v) to C_x).  Push until either
a contradiction or a precise obstruction appears; name the obstruction exactly.
