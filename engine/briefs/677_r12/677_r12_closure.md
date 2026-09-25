
# Finite-combinatorics research brief (self-contained). Construction task.

You have NO execution environment.  Do not report any number as "measured",
"computed" or "verified by search"; every number you state must be derived in the
text you write, or quoted from this brief with its label.  State in one line at the
top: `EXECUTION: none — all claims derived in text.`

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
      R_c denotes the map x |-> x*c (a COLUMN of the table).  R_c is NOT a
      bijection: its fibre profile is (q+1) over nu(c), 1 elsewhere, 0 on D_c.
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
      perfect row then r in C_x <=> x is missing from row r of the array, i.e.
      r in C_x <=> x in D_r (this equivalence is DEFINITIONAL, see error 4 below).

## GIVEN — A IS FREE DESIGN DATA  ((R11C/A-free), established by exhaustive check)
On a fixed line set at q = 2, ALL 5040 permutations nu are realizable by at least one
branch table, and A = #{v : nu^2(v) in ell_v} attains EVERY value 0,1,...,7 = n.
CONSEQUENCES YOU MUST RESPECT AS HYPOTHESES OF THE PROBLEM:
 * `A = n` is FALSE in general.  `g == nu^{-1}` is FALSE in general.  You may NOT
   assume g(c) = nu^{-1}(c), nor that nu^2(v) in ell_v, for any particular v.
 * `b == 1` is NOT automatic, even under delta == 0 (witness at q = 2:
   nu = [1,2,3,0,5,6,4] gives g = [0,2,0,3,1,0,1], b = [3,2,1,1,0,0,0]).
 * Therefore A, g and b are FREE PARAMETERS.  If your argument needs a value of A,
   carry A as a symbol and say what your conclusion becomes for each A; an argument
   valid only at A = n is worth nothing.

## The situation, exactly
* delta == 0 (the TRACE sub-branch) is necessary for the target property (N)
  ("E = N everywhere", i.e. all n rows perfect).  By (F1)+(F2), delta == 0 is
  EXACTLY the array statement "every value occurs exactly n times in the array".
* PROVED at q = 2 by exhaustion, CONJECTURE in general and THE NAMED TARGET:
      **derive  delta == 0 ==> |P| <= q  from (F11)-(F14) + the phi-fusion closure (F9).**
* MEASURED at q = 2 on one realizable design instance: the first-order system
  {(a),(b),(c) + delta==0 + (F4) + (F5) + (F9)} admits |P| = q+1 phantom arrays
  (arrays satisfying everything listed but realized by NO table).  Adding
  (F11)-(F14) kills ALL of them: every (q+1)-subset becomes infeasible.  So (ZD) is
  the missing first-order ingredient — but that computation is NOT a proof at general q.

## HARD RULE — NAME THE MAP YOU INVERT (verbatim standing rule; violation voids your answer)
> "Any step that inverts or transports along a map must NAME the map and JUSTIFY
> bijectivity (or restrict to the fiber actually used).  Adjudication shortcut:
> check the inversions first — they are the cheapest kill."

Operationally: every time you write `R_c^{-1}`, `Lam`, `x |-> x*v`, "by symmetry",
"relabelling", "the same count from the other side", or move an index from row to
column, you MUST insert a bracketed note naming the map, its domain and codomain, and
either a proof it is a bijection or the exact fibre you are restricting to.  The only
maps PROVED bijective here are: rows y |-> x*y (a), nu (c), phi_t = Lam_t (F3), and
c |-> ell_c (b).  COLUMNS R_c are NOT bijections; D-membership is NOT symmetric.
Your answer will be adjudicated by checking the inversions FIRST.

## DEAD ROUTES — six located errors from the previous fan-out.  DO NOT RE-WALK.
 1. "A = n for every branch object" (i.e. g == nu^{-1} identically) — REFUTED
    exhaustively; see the A-free block above.
 2. "delta(v) = q - m(v) identically", hence "b == 1 unconditionally" — REFUTED.
    ERROR: the step "x |-> x*v is a bijection by the row-permutation property"
    varies the ROW index at fixed column, i.e. it is a COLUMN R_v of the table, and
    columns of a branch table are NOT permutations (profile q+1,1,...,1,0,...,0).
    The heavy-term count is #{x : x*v = nu^{-1}(x)}, not 1.
 3. "For perfect r, EVERY x in ell_{nu(r)} has Xi_r(x) = nu(r)" — REFUTED by (F4),
    whose corollary caps that count at 1 (measured = 1 in 57/57 perfect rows, never
    q+1).  Same bijection-abuse family as errors 2 and 6.
 4. "r perfect ==> C_r = D_r" (and any `Phi = n - |P|` functional resting on it) —
    REFUTED on 57/57 perfect rows (e.g. C_3 = {0,4} vs D_3 = {0,5}).  ERROR: with
    C_x := {c : x in D_c}, the statement "r in C_x <=> x in D_r" is DEFINITIONAL; it
    is NOT the symmetry "r in D_c <=> c in D_r" that C_r = D_r asserts.  D is a
    bipartite relation between VALUES and COLUMNS; it has no symmetry.
 5. "|P ^ C_x| <= q - |F_x|" where F_x is the pencil-forced set — REFUTED as stated:
    it silently needs F_x ^ P = empty, which is FALSE.  Also its downstream gap
    "delta == 0 ==> Sum_v s_v >= q(q^2+1)" is REFUTED (real delta == 0 objects carry
    2,4,7,8 at q = 2, and the |P| = q object carries 7).  An EXACT accounting that
    carries the overlap |F_x ^ P| as a term is still open; an argument that assumes
    the overlap empty is dead on arrival.
 6. ZERO-BITE restatements (true but content-free; do not submit them):
    (i) "r in P ==> D_r = {x : x\r in Z(x)}" — (F11) already gives this
    UNCONDITIONALLY for every column, so the "r in P" hypothesis is redundant;
    (ii) any chain using only |D_c| = q, e.g. "z = e+1" for a (q+1)-set of columns —
    such identities hold for EVERY (q+1)-set of columns, perfect or not, and
    constrain perfect rows not at all.
 Also long closed: marginal / Gale-Ryser / transportation counting on the (t,x,v)
 marginals (capacity tight at P = M); "the sets Fix(L_r R_{nu(r)}) are pairwise
 disjoint over perfect rows"; any ROW-LOCAL argument (one perfect row at a time);
 per-cell concentration bounds max E < max N; translation-invariant tables on Z_n.

## RULES FOR YOUR ANSWER (construction-only; strict)
1. You are a CONSTRUCTOR, not a certifier.  Give candidate steps with COMPLETE
   proofs from (a)-(c) and (F0)-(F14).  Anything not fully proved must be labelled
   `CONJECTURE:` with the missing link named in one line.
2. NEVER claim the whole target is solved.  One genuinely new PROVED lemma beats a
   long sketch.  State for each claim whether it is proved for ALL q or only q = 2.
3. No literature, no internet, no external references.
4. Any object you propose (design, array, table) must be given EXPLICITLY and
   checked against (a)-(c) and (F6); unrealizable design data certifies nothing.
5. Open with the line `EXECUTION: none — all claims derived in text.`, then an
   `INVERSIONS USED` list: one line per map you invert, with its bijectivity
   justification or the fibre you restrict to.  A missing or false entry voids the
   answer.  Then start directly with your first claim.  No restatement of this
   brief, no pleasantries, no summary section.

## YOUR SPECIFIC ANGLE — E: run the phi-fusion CLOSURE as a general-q proof device
(F9) is the only tool in the kit that is a PROCEDURE rather than an identity, and
(F3) — phi_t = Lam_t is a bijection — is the only inversion in this problem that is
proved outright.  At q = 2 the closure plus (F11)-(F14) kills every (q+1)-set of
perfect rows by search.  Your job is to run that same propagation SYMBOLICALLY at
general q, from q+1 perfect rows, and reach a conflict by hand.
 1. Set up.  Assume delta == 0 and r_0, ..., r_q perfect.  For a perfect row r,
    column r of the table carries exactly M \ ({nu(r)} u D_r) off the block, and the
    block cells are a*r = nu(r) for a in ell_r.  Write down the closure seeds these
    q+1 rows give you, and the two propagation rules of (F9) in the exact form you
    will use, with phi_t named as the inverted map each time.
 2. Find the cycle.  The forward rule x*v = u ==> t*u = x and the backward rule
    Lam_t(x) = c ==> x*v = c chain cells together; a conflict arises when two chains
    reach the same cell with different values, or when a row is forced to repeat a
    value.  With q+1 perfect rows and (F11) telling you exactly which cells are
    FORBIDDEN (x in D_c <=> x\c in Z(x)), locate a chain that must close on itself in
    at most a bounded number of steps and whose closure forces a repeat in some row.
    Give the chain explicitly as a sequence of cells with the rule used at each step.
 3. The q vs q+1 discrimination.  Your conflict MUST use the (q+1)-st perfect row.
    Show precisely where: exhibit the step that has q+1 objects competing for q slots
    (the natural candidates are C_x with |C_x| = q, or D_r with |D_r| = q, against a
    pencil of size q+1).  If your chain closes with only q perfect rows, it is WRONG —
    real objects with |P| = q exist.  Say which step fails at |P| = q.
 4. If the full conflict does not come out, deliver instead a PROVED "closure lemma":
    a statement of the form "if r and r' are both perfect then the closure forces
    <explicit cell value>", with complete proof.  Several such lemmas, each proved,
    are a better round than one unproved conflict.
Carry A, g, b symbolically throughout (A-free block); no step may assume
g = nu^{-1}, nu^2(v) in ell_v, or b == 1.  Do not re-derive (F11) with a redundant
"r in P" hypothesis (dead route 6(i)).  Every use of Lam or of a column inverse gets
a bracketed bijectivity note (hard rule above).

## HARD WORD CAP: 1100 words.
