# Finite-combinatorics research brief (self-contained). Construction task.
# BRIEF VERSION: r13 brief v1 (2026-08-22, owner-677)

## PART 0 — EXECUTION ENVIRONMENT DECLARATION (mandatory first line of your answer)
You have NO execution environment.  Your answer MUST open with the literal line
`EXECUTION: none — all claims derived in text.` (or an honest statement of what you did
run, if that is false).  Then the INVERSIONS USED list (Part 0.2), then the HELD-OUT
table (Part 0.3), then your first claim.  A missing Part 0 line voids the answer.

## PART 0.1 — AUTOMATIC VOID RULES (read before writing anything)
V1. **Every number you state must be derived in the text you write, or quoted from this
    brief with its label.**  Any number that is neither — a "measured", "computed",
    "verified by search", "one checks that ... = 17" value with no derivation — is an
    AUTOMATIC VOID of the whole answer, not of the sentence.  (A previous submission
    declared `EXECUTION: none` and then asserted a measurement; it was fabricated and
    refuted on 3967 of 4248 objects.)  If you need a number you cannot derive, write
    `CANNOT DERIVE` and carry the quantity as a symbol.
V2. **g IS NOT INJECTIVE.**  `g(c) := nu(c)\c` is a map columns -> values with NO
    injectivity property.  Every single occurrence of `g^{-1}`, "the c with g(c) = x",
    "the line of the g-fibre", "by g-injectivity", or any step that reads a value back to
    a unique column, MUST be accompanied, in brackets on the same line, by the printed
    b-witness below and by an explicit statement of what your step does when the fibre
    has size b(x) != 1 — including the empty case b(x) = 0.  Missing bracket = void.
      PRINTED b-WITNESS (a real branch object at q = 2, from an exhaustive check over all
      5040 nu on the fixed line set below):
          nu = [1,2,3,0,5,6,4]   gives   g = [0,2,0,3,1,0,1],   b = [3,2,1,1,0,0,0]
      so g has a fibre of size 3, a fibre of size 2, and three EMPTY fibres.
      Two standing traps this witness kills (both cost a previous round):
        * image-of-intersection vs intersection-of-images:
          `g(S ^ S') = g(S) ^ g(S')` is FALSE for non-injective g;
        * union-as-sum: `|S ^ (union of the lines over a g-fibre)| = Sum over the fibre
          of |S ^ ell_c|` is FALSE as soon as two lines of one fibre share a point —
          and in a projective plane ANY two distinct lines share exactly one point.
      NOTE ON delta == 0: this witness is NOT a delta == 0 object (it has b(0) = 3 > q,
      which (F8) forbids when delta <= 0).  On the delta == 0 sub-branch the sharpest
      PROVED statement is (F8): b(v) <= q for every v.  b == 1 is NOT forced there, so
      you may not assume it; you may use b <= q.
V3. **STATE THE ARGUMENT OF EVERY TRANSPORT.**  Naming the map is no longer enough.
    Every time you apply a map (phi_t, Lam_t, nu, a row, a column, `x |-> x*v`), you must
    write, in brackets, the map AND the exact element you are feeding it AND the slot that
    element occupies.  A previous submission named `phi_t = Lam_t` correctly, proved it
    bijective correctly, and then evaluated `phi_t(x) = x * Xi_t(x)` with the ROW INDEX t
    in the argument slot where the POINT x belongs; the resulting general identity was
    refuted on 70135 of 89208 instances.  "Used a bijection at the wrong argument" is as
    fatal as inverting a non-bijection and is caught the same way: by reading your
    brackets first.  Missing argument = void for that step.

## PART 0.2 — HARD RULE, NAME THE MAP YOU INVERT (standing, verbatim)
> "Any step that inverts or transports along a map must NAME the map and JUSTIFY
> bijectivity (or restrict to the fiber actually used).  Adjudication shortcut:
> check the inversions first — they are the cheapest kill."
Open with an `INVERSIONS USED` list: one line per map you invert or transport along,
giving its domain, codomain, the ARGUMENT you feed it (V3), and either a proof it is a
bijection or the exact fibre you restrict to.  A missing or false entry voids the answer.
The only maps PROVED bijective here are: rows y |-> x*y (a), nu (c), phi_t = Lam_t (F3),
and c |-> ell_c (b).  COLUMNS R_c are NOT bijections; g is NOT injective;
D-membership is NOT symmetric.

## PART 0.3 — HELD-OUT TABLE (mandatory, graded; this is an anti-echo harness)
The four quantities below are fully determined by data printed in this brief, and their
values are deliberately NOT printed anywhere in it.  Answer all four in a table before
your first claim, each with a one-line derivation.  `CANNOT COMPUTE` is an accepted
answer for a row; a confident wrong value is not.  Failing the table voids the round
regardless of the quality of the mathematics after it.
  H1. The value of A = #{v : nu^2(v) in ell_v} for the printed b-witness nu above, on the
      printed line set — computed BOTH ways, directly and via (F6).
  H2. For every unordered pair of distinct columns c != c' with g(c) = g(c') in that
      witness: the point ell_c ^ ell_{c'}.  (There are exactly as many such pairs as the
      printed b forces; say how many and list them.)
  H3. For the point r = 0 of that witness: the set pencil(0) = {c : 0 in ell_c}, the
      multiset {g(c) : c in pencil(0)}, and whether it has a repeat.
  H4. In that witness, how many of the 7 points r have a REPEATED g-value in
      {g(c) : c in pencil(r)}?

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

THE FIXED q = 2 LINE SET used by the printed b-witness (points and columns are both
0..6; ell_c is the line of column c):
  ell_0 = {0,4,5}  ell_1 = {0,2,6}  ell_2 = {1,5,6}  ell_3 = {3,4,6}
  ell_4 = {1,2,4}  ell_5 = {2,3,5}  ell_6 = {0,1,3}

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
      ARGUMENT WARNING (V3): the argument slot of phi_t is the POINT x, never the row
      index t; the identity is between the two maps x |-> x*Xi_t(x) and x |-> t\x.
 (F4) [loc] x in ell_v AND Xi_t(x) = v  <=>  x = t*nu(v).
      Corollary |Xi_t^{-1}(v) ^ ell_v| <= 1.
 (F5) [T-count] T_v := {t : some x in ell_v has Xi_t(x) = v} = R_{nu(v)}^{-1}(ell_v),
      so |T_v| = (q+1) + q*[nu^2(v) in ell_v] - |ell_v ^ D_{nu(v)}|.
      R_c denotes the map x |-> x*c (a COLUMN of the table).  R_c is NOT a
      bijection: its fibre profile is (q+1) over nu(c), 1 elsewhere, 0 on D_c.
 (F6) [REAL-1] g(c) = nu^{-1}(c) <=> nu(c) in ell_{nu^{-1}(c)}; hence
      A := #{v : nu^2(v) in ell_v} = #{c : g(c) = nu^{-1}(c)}.
 (F7) [skeleton] for every column c and every r in ell_c, PERFECT OR NOT:
      Xi_r(nu(c)) = g(c).  CONSEQUENCE, and a standing warning: the POSITIONAL clause
      "nu(c) is the place where Xi_r takes the value g(c)" is therefore automatic and
      carries NO information.  Any contradiction derived from the positional clause
      alone is VACUOUS.
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
      perfect row then r in C_x <=> x in D_r; this equivalence is DEFINITIONAL (it is
      NOT a symmetry of D — see dead route 4).
 (F15) **(pencil)** For a PERFECT row r: (i) g(c) not in D_r for every c in pencil(r);
      (ii) g is injective on pencil(r) EXCEPT that repeats with value nu(r) are allowed.
      For perfect r != s with joining column c0 (the unique column with r, s in
      ell_{c0}): g(c0) not in D_r u D_s, and if g(c0) not in {nu(r), nu(s)} then nu(c0)
      is the unique Xi_r- and the unique Xi_s-preimage of g(c0).
      Arc form: for q+2 perfect rows with no 3 collinear, from each row the pencil
      g-values are distinct-or-nu(r).
      (F15) is PROVED at all q and is the main structural fact you are given that is NOT
      a counting identity.  Note (ii) has bite exactly on the part where b > 1.

## GIVEN — A, g, b ARE FREE DESIGN DATA  ((R11C/A-free), exhaustive check at q = 2)
On the fixed line set above, ALL 5040 permutations nu are realizable by at least one
branch table, and A attains EVERY value 0,1,...,7 = n.  Consequences you must respect:
 * `A = n` is FALSE in general; `g == nu^{-1}` is FALSE in general.  You may NOT assume
   g(c) = nu^{-1}(c), nor that nu^2(v) in ell_v, for any particular v.
 * If your argument needs a value of A, carry A as a SYMBOL and say what your conclusion
   becomes for each A.  An argument valid only at A = n is worth nothing.
 * b is free subject to Sum_v b(v) = n, and to b(v) <= q on the delta == 0 sub-branch
   by (F8).  Empty fibres (b(v) = 0) are normal — the printed witness has three.

## The situation, exactly
* delta == 0 (the TRACE sub-branch) is necessary for the target property (N)
  ("E = N everywhere", i.e. all n rows perfect).  By (F1)+(F2), delta == 0 is
  EXACTLY the array statement "every value occurs exactly n times in the array".
* PROVED at q = 2 by exhaustion, CONJECTURE in general and THE NAMED TARGET:
      **derive  delta == 0 ==> |P| <= q  from (F11)-(F15) + the phi-fusion closure (F9).**
* MEASURED at q = 2 on one realizable design instance: the first-order system
  {(a),(b),(c) + delta==0 + (F4) + (F5) + (F9)} admits |P| = q+1 phantom arrays
  (arrays satisfying everything listed but realized by NO table).  Adding
  (F11)-(F14) kills ALL of them.  That computation is NOT a proof at general q.

## REFUSED AT DISPATCH — the retired global double count  ((R12/DEGEN), PROVED, all q)
Let I := {(x,c) : x in D_c}.  Splitting I by whether the column is perfect gives the
GROUND IDENTITY  q|P| = Sum_x #{v in Z(x) : x*v in P} = Sum_x |P ^ C_x|.
This identity is FREE, unconditional, and CARRIES NO INFORMATION ABOUT |P|: writing
k = |P|, the exact pencil/off-pencil refinement of it reads
`qk = k(q+1) + q*A_P - Sum_s |T_s| + F`, in which the k terms CANCEL identically, leaving
a statement true for every k (0 violations on 4248 branch objects, observed difference
identically 0).  Consequently:
  **Any submission whose load-bearing step is the double count of I against P — through
  the pencil/off-pencil split, through T-data, or through any re-expression of
  Sum_x |P ^ C_x| — is REFUSED WITHOUT READING.**  This is a dispatch-time refusal, not
  an adjudication-time one: do not spend your budget there.  A route through I is
  admissible ONLY if it introduces a term that is not a re-expression of Sum_x |P ^ C_x|,
  and you must say IN ONE LINE, up front, which term that is and why it is new.
Also retired with it: the "competition" variant that bounds q|P| <= nq - W_Pbar; it is
the same identity with f_off(x) <= q - s_x.

## DEAD ROUTES — located errors from the previous two fan-outs.  DO NOT RE-WALK.
 1. "A = n for every branch object" (g == nu^{-1} identically) — REFUTED exhaustively.
 2. "delta(v) = q - m(v) identically", hence "b == 1 unconditionally" — REFUTED.
    ERROR: "x |-> x*v is a bijection by the row-permutation property" varies the ROW
    index at fixed column, i.e. it is a COLUMN R_v, and columns are not permutations.
 3. "For perfect r, EVERY x in ell_{nu(r)} has Xi_r(x) = nu(r)" — REFUTED by (F4),
    whose corollary caps that count at 1 (measured 1 in 57/57 perfect rows).
 4. "r perfect ==> C_r = D_r" (and any `Phi = n - |P|` functional resting on it) —
    REFUTED 57/57.  ERROR: "r in C_x <=> x in D_r" is DEFINITIONAL, not a symmetry of D.
    D is a bipartite relation between VALUES and COLUMNS; it has no symmetry.
 5. "|P ^ C_x| <= q - |F_x|" with F_x the pencil-forced set — REFUTED as stated: it
    silently needs F_x ^ P = empty, which is FALSE.  Its downstream gap
    "delta == 0 ==> Sum_v s_v >= q(q^2+1)" is REFUTED.  An EXACT accounting that carries
    the overlap |F_x ^ P| as a term is still open; assuming it empty is dead on arrival.
 6. ZERO-BITE restatements (true but content-free; do not submit them):
    (i) "r in P ==> D_r = {x : x\r in Z(x)}" — (F11) gives this unconditionally;
    (ii) any chain using only |D_c| = q, e.g. "z = e+1" for a (q+1)-set of columns;
    (iii) re-deriving (F13) summed over v with A symbolic — that is this brief's own
    arithmetic, and the resulting T-sum bound caps |P| at order q^2 (it evaluates to
    8.75 against a target of 2 at q = 2), so the whole T-SUM ROUTE is exhausted.
 7. ARGUMENT/INDEX SWAP (see V3): transporting along `phi_a = Lam_{nu(c)}` or feeding a
    row index into the point slot of phi.  The general form `nu(c)*(a*g(c)) = a` is
    REFUTED 70135/89208.  `nu(c)*g(c) = c` is DEFINITIONAL (g(c) := nu(c)\c) — not a
    finding.  Any step needing the incidence `nu(c) in ell_c` is unjustified (REFUTED
    21060/29736).
 8. FIBRE-COLLAPSE (see V2), two refuted instances, both smuggling b == 1:
    (i) `|g(pencil r) ^ g(pencil r')| <= 1` — REFUTED 3084/89208 row pairs.  ERROR:
    the proof gets `pencil(r) ^ pencil(r') = {c}` and then reads off the IMAGES.
    (ii) `Sum_x theta(x) = (q+1)^2` where theta(x) = |S ^ (union of the lines of the
    g-fibre over x)| — REFUTED 9782/148680 subsets.  ERROR: the proof sums |S ^ ell_c|
    over the fibre; union != sum once two lines of one fibre meet inside S, and the
    b(x) = 0 fibres are empty.  The correct relation is `<=`.
 9. PHANTOM MEASUREMENT: declaring `EXECUTION: none` and then asserting a measured fact.
    Automatic void (V1).
 Also long closed: marginal / Gale-Ryser / transportation counting on the (t,x,v)
 marginals (capacity TIGHT at P = M, so no bound |P| < n is derivable from marginals at
 any q); "the sets Fix(L_r R_{nu(r)}) are pairwise disjoint over perfect rows"; any
 ROW-LOCAL argument (one perfect row at a time); per-cell concentration bounds
 max E < max N; translation-invariant tables on Z_n (DEAD at q = 3, do not propose).
 RE-OPENED, for the record: the "collinear 4-set" kill of an earlier round failed only
 because it used the vacuous positional clause of (F7); the collinear configuration
 question itself is OPEN.

## RULES FOR YOUR ANSWER (construction-only; strict)
1. You are a CONSTRUCTOR, not a certifier.  Give candidate steps with COMPLETE proofs
   from (a)-(c) and (F0)-(F15).  Anything not fully proved must be labelled
   `CONJECTURE:` with the missing link named in one line.
2. NEVER claim the whole target is solved.  One genuinely new PROVED lemma beats a long
   sketch.  State for each claim whether it is proved for ALL q or only q = 2.
3. No literature, no internet, no external references.
4. Any object you propose (design, array, table) must be given EXPLICITLY and checked
   against (a)-(c) and (F6); unrealizable design data certifies nothing.
5. Answer order is fixed: Part 0 line, `INVERSIONS USED` list, HELD-OUT table, then your
   first claim.  No restatement of this brief, no pleasantries, no summary section.

## YOUR SPECIFIC ANGLE — D: the Z-profile law  m(v) = q*b(v)  under delta == 0
Under delta == 0, (F2) is not an inequality but an EXACT pointwise law:
      for every value v:   m(v) = #{x : v in Z(x)} = q * b(v).
(The middle expression is the (F11) reading of m: v in Z(x) <=> x in D_{x*v}.)  So the
Z-side profile is DETERMINED by the g-fibre sizes, value by value, and by (F8) every
fibre has b(v) <= q while Sum_v b(v) = n.  Nothing in the retired global double count
uses this pointwise law — it uses only its total Sum_v m(v) = nq.  Say so in your
opening line: your new term is the per-value law, not the total.
Sub-tasks, in order:
 1. Prove the displayed law from (F2) + (F11) with argument slots explicit, and state
    what it says at b(v) = 0 (then NO column of the array misses v) and at b(v) = q.
 2. Fix a perfect row r.  Perfectness makes D_r exactly the set of values missing from
    row r of the array, and (F14) makes C_x the columns missing x.  Express |D_r| = q in
    terms of the Z-sets: which x have r in C_x?  Then count the incidences
    {(x, r) : r in P, v in Z(x)} for a FIXED v — this is a per-value count of size
    q*b(v), and it is NOT the total incidence count of the retired route.
 3. Combine with (F15)(i) in the form "g(c) not in D_r for c in pencil(r)": the values
    that CAN be missing from a perfect row are constrained to avoid the g-image of the
    pencil.  Since g's image has size #{v : b(v) >= 1} <= n and the fibres are capped at
    q by (F8), derive a counting relation between |P|, the number of nonempty fibres, and
    q.  Carry the number of nonempty fibres as a symbol beta := #{v : b(v) >= 1}; note
    (F0)+(F8) give beta >= n/q.
 4. Push for a contradiction at |P| = q+1: with q+1 perfect rows, the q+1 sets D_r are
    each of size q and each avoids the g-values of its own pencil.  Ask whether the
    per-value law m(v) = q*b(v) can be satisfied simultaneously — i.e. whether the total
    Z-mass qn can be distributed as required while every perfect row's D-set dodges its
    pencil's g-image.
Deliver: the per-value law proved cleanly, the beta-parametrised counting relation, and
either a contradiction at |P| = q+1 or the sharpest inequality relating |P|, beta and q
that you can PROVE, with a one-line statement of the missing fact.

## HARD WORD CAP: 1000 words.  Exceeding it is a defect, not a bonus.
