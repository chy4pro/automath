# Finite-combinatorics research brief (self-contained). Construction task.
# BRIEF VERSION: r15 brief v2 (2026-08-22, owner-677)

## PART 0 — EXECUTION ENVIRONMENT DECLARATION (mandatory first line of your answer)
You have NO execution environment.  Your answer MUST open with the literal line
`EXECUTION: none — all claims derived in text.` (or an honest statement of what you did
run, if that is false).  Then the INVERSIONS USED list (0.2), then the DATA ECHO (0.25),
then the HELD-OUT table (0.3), then your first claim.  A missing Part 0 line voids the
answer.

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
      **b-WITNESS — DESIGN DATA ONLY.  THIS IS NOT THE PRINTED INSTANCE BELOW.**  It is a
      DIFFERENT design on the SAME line set, from an exhaustive check over all 5040
      permutations nu.  Its symbols are primed throughout so you cannot confuse them with
      the instance's:
          nu'(0)=1  nu'(1)=2  nu'(2)=3  nu'(3)=0  nu'(4)=5  nu'(5)=6  nu'(6)=4
          g'(0)=0   g'(1)=2   g'(2)=0   g'(3)=3   g'(4)=1   g'(5)=0   g'(6)=1
          b'(0)=3   b'(1)=2   b'(2)=1   b'(3)=1   b'(4)=0   b'(5)=0   b'(6)=0
          fibres:  g'^{-1}(0) = {0, 2, 5}   g'^{-1}(1) = {4, 6}   g'^{-1}(2) = {1}
                   g'^{-1}(3) = {3}         g'^{-1}(4) = g'^{-1}(5) = g'^{-1}(6) = {}
      so g' has a fibre of size 3, a fibre of size 2, and three EMPTY fibres.
      Two standing traps this witness kills (both cost a previous round):
        * image-of-intersection vs intersection-of-images:
          `g(S ^ S') = g(S) ^ g(S')` is FALSE for non-injective g;
        * union-as-sum: `|S ^ (union of the lines over a g-fibre)| = Sum over the fibre
          of |S ^ ell_c|` is FALSE as soon as two lines of one fibre share a point —
          and in a projective plane ANY two distinct lines share exactly one point.
      NOTE ON delta == 0: this witness is NOT a delta == 0 object (it has b'(0) = 3 > q,
      which (F8) forbids when delta <= 0).  On the delta == 0 sub-branch the sharpest
      PROVED statement is (F8): b(v) <= q for every v.  **b == 1 is NOT FORCED there:
      an exhaustive q = 2 check over every delta == 0 object found both kinds — objects
      with b == 1 AND objects carrying a fibre of size 2.  So on the delta == 0
      sub-branch b is genuinely variable, subject only to Sum_v b(v) = n and b(v) <= q.
      Do not assume b == 1 and do not assume its negation; for the PRINTED INSTANCE,
      derive b from the instance (held-out row H2).**
V3. **STATE THE ARGUMENT OF EVERY TRANSPORT.**  Naming the map is no longer enough.
    Every time you apply a map (phi_t, Lam_t, nu, a row, a column, `x |-> x*v`), you must
    write, in brackets, the map AND the exact element you are feeding it AND the slot that
    element occupies.  A previous submission named `phi_t = Lam_t` correctly, proved it
    bijective correctly, and then evaluated `phi_t(x) = x * Xi_t(x)` with the ROW INDEX t
    in the argument slot where the POINT x belongs; the resulting general identity was
    refuted on 70135 of 89208 instances.  Missing argument = void for that step.
V4. **ARITHMETIC RE-CHECK — every closed form is re-evaluated in-text at TWO concrete
    parameter values, and EVERY DIVISION IS SHOWN.**  Any formula, bound or identity you
    state in general q must be immediately re-evaluated at `q = 2` (`n = 7`) AND at
    `q = 3` (`n = 13`), with both numeric results printed on the spot and every division
    written out as an exact fraction before it is rounded or floored.  A general formula
    with no two numeric evaluations beside it is scored as UNSTATED.
    Why this rule exists — the two best answers of the previous round both died here, in
    one line each, and both would have been caught by one substitution:
      * one wrote `q*n/(q+1) = q + q^2/(q+1)`.  With `n = q^2+q+1` the true value is
        `q*n/(q+1) = q^2 + q/(q+1)`.  At q = 2 that is 14/3 = 4.67 (floor 4), not 10/3
        = 3.33 (floor 3).  Its headline conclusion `|P| <= q for all q` was FALSE; the
        route in fact caps at `q^2`.
      * another wrote a union size as `3(q+1) - 2 = 3q - 2`.  `3(q+1) - 2 = 3q + 1`.
    So: print `q = 2:` and `q = 3:` lines under every displayed formula, and show
    numerator, denominator and quotient separately for every division.
V5. **STATE THE CARDINALITY AND THE TYPE OF EVERY SET YOU EQUATE.**  Whenever you write
    `S = S'` or `S subset S'` for sets, you must give, in brackets, for BOTH sides: its
    size (as a formula in q) and its AMBIENT TYPE — VALUES, COLUMNS, POINTS, or ROWS.
    Why this rule exists: a previous answer, with every V3 bracket correct, wrote
    `C_r = {x : r in C_x} = {x : x in D_r} = M \ D_r` and called `M \ D_r` "a set of size
    q".  Three faults in one line, all caught by V5: `{x : x in D_r}` IS `D_r`, written
    as its own complement; `|M \ D_r| = n - q = q^2+1`, not q; and `C_r` was typed as a
    set of VALUES where (F14) types `C_x` as a set of COLUMNS.  V3 does not catch this.
V6. **A SELF-CHECK MUST PRINT ITS DERIVATION, NOT ITS VERDICT.**  Wherever this brief
    mandates a self-check, write out the derivation you performed and then the verdict.
    **A bare `PASS` / `checks out` / `as expected` with no derivation beside it is scored
    as ABSENT, not as passed** — and a self-check scored ABSENT voids every claim that
    rests on it.  (A previous answer returned `PASS` on a mandated recovery whose second
    half was contradicted by its own preceding line.)
V0. **A COMPLIANCE DECLARATION WITH NO SUBJECT MATTER IS NOT COMPLIANCE.**  Declaring
    "V2 respected: no g-fibre is inverted" in an answer that uses no g-fibre anywhere
    scores as ABSENT, not as PASS.  Declare a rule only where you actually exercised it,
    and point at the line where you did.  Likewise `CANNOT COMPUTE` / `CANNOT DERIVE` is
    a hatch you are EXPECTED to use when it applies — but its presence somewhere in your
    answer excuses nothing elsewhere: a previous answer carried a prominent hatch and
    then asserted a wrong constant anyway.

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

## PART 0.25 — DATA ECHO (mandatory, immediately after the INVERSIONS list)
Before you use any printed number, reprint the data you are going to use, in labelled
form, one value per entry, and TAG ITS SOURCE as either `[INSTANCE]` (the table W and its
nu, lines, pencils, printed below) or `[b-WITNESS]` (the primed nu', g', b' of V2).  The
two objects are DIFFERENT and share only the line set.  Minimum echo: the row of W you
read most, `nu` and `nu^{-1}` in full, and the pencil you use.
Why this rule exists: the previous round's best-scoped angle was voided outright because
its answer read `g(1) = 1` off a printed list whose first entry was labelled `g(0)`.  One
misread index, three wrong held-out rows, whole round lost.  Echo first, then compute.

## PART 0.3 — HELD-OUT TABLE (mandatory, graded; anti-echo + anti-arithmetic harness)
Four quantities, all fully determined by data printed in this brief, none of them printed
anywhere in it.  Answer all four in a table before your first claim, each with a one-line
derivation.  **All four are about the PRINTED INSTANCE (the table W below), not about the
b-witness.**  Rows are tiered, and the tiers are graded differently:
  * `[H]` = hand-derivable in at most ~25 lookups.  A confident WRONG value on an `[H]`
    row VOIDS THE ROUND regardless of the mathematics after it.
  * `[C]` = genuinely computational.  `CANNOT COMPUTE` on a `[C]` row is a CLEAN answer
    and costs you nothing.  A confident wrong value on a `[C]` row does not by itself
    void the round, but it downgrades every un-derived numeric claim in your body to
    CONJECTURE — so use the hatch rather than guess.
  H1 `[H]`  From the table W: the sets `D_0`, `D_3` and `D_6` (the values missing from
      columns 0, 3 and 6 of W).  Give each as an explicit set and state its size.
  H2 `[H]`  From the table W: `g(c) = nu(c)\c` for all seven columns c = 0..6, and the
      resulting fibre-size profile `b(v)` for all seven values v = 0..6.  (These are
      WITHHELD on purpose: derive them, do not look for them printed.)
  H3 `[C]`  From the table W: the set `Z(x)` for every x = 0..6; the number
      `m(v) = #{x : v in Z(x)}` for every v = 0..6; and whether this instance satisfies
      `delta == 0`.  State which route you used ((F1)/(F11) is far cheaper than building
      the whole Xi-array).
  H4 `[C]`  Over ALL 5040 permutations nu' of the seven points, on the fixed line set
      printed below (the table W plays no role in this row): how many nu' satisfy
      `A(nu') = #{v : nu'(nu'(v)) in ell_v} = 0`?
      (H4 is deliberately independent of H1-H3: one slip must not cost you two rows.)

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

## THE PRINTED INSTANCE — one explicit branch object at q = 2, n = 7
Source tag for everything in this section: `[INSTANCE]`.  Entry in row a, column c is
the product `a*c`.  Rows are permutations; columns are block-structured.
          c=0   c=1   c=2   c=3   c=4   c=5   c=6 
   a=0 |   4     3     0     1     2     6     5  
   a=1 |   3     1     6     4     0     2     5  
   a=2 |   2     3     5     6     0     1     4  
   a=3 |   0     6     4     2     3     1     5  
   a=4 |   4     5     1     2     0     3     6  
   a=5 |   4     0     6     3     5     1     2  
   a=6 |   5     3     6     2     1     4     0  
Its design data, one value per entry:
   nu(0) = 4   nu(1) = 3   nu(2) = 6   nu(3) = 2   nu(4) = 0   nu(5) = 1   nu(6) = 5
   nu^{-1}(0) = 4   nu^{-1}(1) = 5   nu^{-1}(2) = 3   nu^{-1}(3) = 1   nu^{-1}(4) = 0   nu^{-1}(5) = 6   nu^{-1}(6) = 2
   ell_0 = {0, 4, 5}
   ell_1 = {0, 2, 6}
   ell_2 = {1, 5, 6}
   ell_3 = {3, 4, 6}
   ell_4 = {1, 2, 4}
   ell_5 = {2, 3, 5}
   ell_6 = {0, 1, 3}
   pencil(0) = {c : 0 in ell_c} = {0, 1, 6}
   pencil(1) = {c : 1 in ell_c} = {2, 4, 6}
   pencil(2) = {c : 2 in ell_c} = {1, 4, 5}
   pencil(3) = {c : 3 in ell_c} = {3, 5, 6}
   pencil(4) = {c : 4 in ell_c} = {0, 3, 4}
   pencil(5) = {c : 5 in ell_c} = {0, 2, 5}
   pencil(6) = {c : 6 in ell_c} = {1, 2, 3}
**READ THIS INSTANCE AS AN INSTANCE, NEVER AS A GENERIC OBJECT.**  It has special
features which (R11C/A-free) forbids you to assume in general — you must NOT transport
any of them into a general-q argument, and if your argument needs one, carry it as a
symbol and say what your conclusion becomes without it.  Its `g`, `b`, `D`, `Z`, `m`,
`delta` and `P` are deliberately NOT printed: derive what you need (H1-H3).

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
   by (F8).  Empty fibres (b(v) = 0) are normal — the printed b-witness has three.

## The situation, exactly
* delta == 0 (the TRACE sub-branch) is necessary for the target property (N)
  ("E = N everywhere", i.e. all n rows perfect).  By (F1)+(F2), delta == 0 is
  EXACTLY the array statement "every value occurs exactly n times in the array".
* PROVED at q = 2 by exhaustion, CONJECTURE in general and THE NAMED TARGET:
      **derive  delta == 0 ==> |P| <= q  from (F11)-(F15) + the phi-fusion closure (F9).**
  The bound is TIGHT at q = 2: delta == 0 objects with |P| = q exist.
* MEASURED at q = 2 on one realizable design instance: the first-order system
  {(a),(b),(c) + delta==0 + (F4) + (F5) + (F9)} admits |P| = q+1 phantom arrays
  (arrays satisfying everything listed but realized by NO table).  Adding
  (F11)-(F14) kills ALL of them.  That computation is NOT a proof at general q.

## REFUSED AT DISPATCH — three retired routes and the PATTERN THEY MAKE
**(1) The global double count of I  ((R12/DEGEN), PROVED, all q).**  Let
I := {(x,c) : x in D_c}.  Splitting I by whether the column is perfect gives the GROUND
IDENTITY  q|P| = Sum_x #{v in Z(x) : x*v in P} = Sum_x |P ^ C_x|.  This identity is FREE,
unconditional, and CARRIES NO INFORMATION ABOUT |P|: writing k = |P|, its exact
pencil/off-pencil refinement reads `qk = k(q+1) + q*A_P - Sum_s |T_s| + F`, in which the
k terms CANCEL identically (0 violations on 4248 branch objects, observed difference
identically 0).  Any submission whose load-bearing step is a re-expression of
`Sum_x |P ^ C_x|` is REFUSED WITHOUT READING.  Also retired with it: the "competition"
variant bounding q|P| <= nq - W_Pbar.
**(2) The g-fibre LINE-UNION exclusion  (retired, empirically, all q).**  With
U_x := union of ell_c over the g-fibre {c : g(c) = x}, (F15)(i) says
`P ^ C_x ^ U_x = empty` for every value x.  The term U_x is genuinely NEW (it is built
from ell and g only, with no D/C/Z input) and the exclusion is correctly proved — and it
STILL has zero bite, because the only way to aggregate it is through the ground identity
of (1), which then yields `q|P| <= nq`, i.e. `|P| <= n`.  Bolting a new geometric term
onto the ground identity is ADMISSIBLE and does not help.  Do not re-walk it.
**(3) The plane's pair count  ((R14/PAIRCAP), PROVED, all q).**  With
k_c := |P ^ ell_c| the two incidence identities `Sum_c k_c = (q+1)|P|` and
`Sum_c C(k_c,2) = C(|P|,2)` are pure plane geometry.  From ANY per-line cap of the form
`k_c <= K` they give `|P| <= (K-1)(q+1) + 1`; at the best cap the pencil route supplies,
K = q, that is `|P| <= q^2 - 1 + 1 = q^2`, tight at q^2 for q = 2,3,4,5,7.  Since any two
points of a projective plane lie on a common line, `K = 1` forces `|P| <= 1` and is
unavailable.  **So the pair-count route can NEVER deliver q.**
**THE PATTERN — read it before choosing your route.**  Three independent routes, plus the
T-sum route of dead route 6(iii), all cap at ORDER q^2, not q.  They share one shape:
*sum a local constraint of strength ~q over the n lines/columns/values, then divide by the
q+1 incidences each perfect row has*.  That shape yields `n*q/(q+1) = q^2 + q/(q+1)` and
cannot do better, because the target `|P| <= q` is one BELOW the size q+1 of a line, and
per-incidence averaging cannot separate `|P| = q+1` from `|P| = q`.
**Therefore: before you submit any bound, evaluate it at q = 2 and q = 3 (V4).  If it
comes out at or above q^2 (>= 4 at q = 2, >= 9 at q = 3) it is a KNOWN result of this
line and is NOT a deliverable — say so plainly and do not present it as progress.**
The conclusion the line draws from the pattern, and the reason for your angle: the
missing ingredient is not another incidence count.  It is a constraint on the
NON-PERFECT rows, which is the only place every would-be conflict is currently absorbed.

## DEAD ROUTES — located errors from previous fan-outs.  DO NOT RE-WALK.
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
    silently needs F_x ^ P = empty, which is FALSE.  An EXACT accounting carrying the
    overlap |F_x ^ P| as a term is still open; assuming it empty is dead on arrival.
 6. ZERO-BITE restatements (true but content-free; do not submit them):
    (i) "r in P ==> D_r = {x : x\r in Z(x)}" — (F11) gives this unconditionally;
    (ii) any chain using only |D_c| = q, e.g. "z = e+1" for a (q+1)-set of columns;
    (iii) re-deriving (F13) summed over v with A symbolic — that is this brief's own
    arithmetic, and the resulting T-sum bound caps |P| at order q^2 (it evaluates to
    8.75 against a target of 2 at q = 2), so the whole T-SUM ROUTE is exhausted.
 7. ARGUMENT/INDEX SWAP (see V3): transporting along `phi_a = Lam_{nu(c)}` or feeding a
    row index into the point slot of phi.  The general form `nu(c)*(a*g(c)) = a` is
    REFUTED 70135/89208.  `nu(c)*g(c) = c` is DEFINITIONAL (g(c) := nu(c)\c) — not a
    finding, and transported CORRECTLY it is vacuous: feeding phi_r the point nu(c)
    returns the seed cell you started from.
 8. FIBRE-COLLAPSE (see V2), two refuted instances, both smuggling b == 1:
    (i) `|g(pencil r) ^ g(pencil r')| <= 1` — REFUTED 3084/89208 row pairs.
    (ii) `Sum_x theta(x) = (q+1)^2` for theta(x) = |S ^ U_x| — REFUTED 9782/148680.
    Correct relation is `<=`.
 9. PHANTOM MEASUREMENT: declaring `EXECUTION: none` and then asserting a measured fact.
    Automatic void (V1).
 Also long closed: marginal / Gale-Ryser / transportation counting on the (t,x,v)
 marginals (capacity TIGHT at P = M, so no bound |P| < n is derivable from marginals at
 any q); "the sets Fix(L_r R_{nu(r)}) are pairwise disjoint over perfect rows"; any
 ROW-LOCAL argument (one perfect row at a time); per-cell concentration bounds
 max E < max N; translation-invariant tables on Z_n (DEAD at q = 3, do not propose);
 the COLLINEAR pair-count angle (see REFUSED (3)).

## RULES FOR YOUR ANSWER (construction-only; strict)
1. You are a CONSTRUCTOR, not a certifier.  Give candidate steps with COMPLETE proofs
   from (a)-(c) and (F0)-(F15).  Anything not fully proved must be labelled
   `CONJECTURE:` with the missing link named in one line.
2. NEVER claim the whole target is solved.  One genuinely new PROVED lemma beats a long
   sketch.  State for each claim whether it is proved for ALL q or only q = 2.
3. No literature, no internet, no external references.
4. Any object you propose (design, array, table) must be given EXPLICITLY and checked
   against (a)-(c) and (F6); unrealizable design data certifies nothing.
5. Answer order is fixed: Part 0 line, `INVERSIONS USED` list, DATA ECHO, HELD-OUT table,
   then your first claim.  No restatement of this brief, no pleasantries, no summary.

## YOUR ANGLE — the POINTWISE law m(v) = q*b(v), aimed at the NON-PERFECT rows
This is the one angle of the previous fan-out that was never examined: its carrier
misread a printed constant and was voided before its mathematics was read.  The angle
itself is untested, not refuted.  Everything above tells you where it must bite.

Under delta == 0, (F2) is not an inequality but an EXACT POINTWISE law:
      for every value v:   m(v) = #{x : v in Z(x)} = q * b(v).
Every retired route uses only its TOTAL, `Sum_v m(v) = nq`.  Your new term is the
per-value law.  Say so in your opening line.

**THE GAP YOU ARE AIMED AT** (located and registered last round, and it is the reason
every conflict so far has evaporated): `delta == 0 constrains only the GLOBAL column sums
of the array — Sum_t E(t,v) = n for each v — while the NON-PERFECT rows' Xi-profiles stay
free, so every conflict a perfect row generates is absorbed by them.`  Concretely, with
p := |P|, e(v) := [nu^{-1}(v) in P] and a(v) := #{r in P : v in D_r}:
      Sum_{r in P} E(r,v) = p + q*e(v) - a(v),
so the n - p non-perfect rows must carry R(v) := n - p - q*e(v) + a(v) at each value v.
Non-negativity of R(v) alone gives only `p <= n - q = q^2 + 1` — a FOURTH route capped at
order q^2 (check it at q = 2 and q = 3 under V4 and confirm this for yourself before you
go further).  **The deliverable is a constraint on non-perfect rows BEYOND
`Sum_v E(t,v) = n`.**

Sub-tasks, in order.
 1. Prove the displayed law from (F2) + (F11), argument slots explicit (V3), types and
    cardinalities on every set equation (V5).  State what it says at b(v) = 0 (then NO
    array column misses v) and at b(v) = q.
 2. **A second, independent derivation of the same law, which identifies b GEOMETRICALLY
    inside the ARRAY.**  By (F1) each array column x has exactly one big fibre, sitting
    at the value v_0(x) = x\nu^{-1}(x) and carried by the points of the line
    ell_{nu^{-1}(x)}.  Put beta_0(v) := #{x : v_0(x) = v}.  Prove
    `Sum_t E(t,v) = n + q*beta_0(v) - m(v)` directly from (F1), hence
    `delta(v) = q*beta_0(v) - m(v)`; then prove `beta_0 = b` by identifying the map
    v_0 in terms of g and nu (one line; state the argument you feed each map, V3).
    Report this as a MANDATED SELF-CHECK under V6: print the derivation, then the
    verdict — a bare PASS scores as absent.  If beta_0 != b, your (F1) reading is wrong
    and everything below it is void, so say which.
    The payoff you must then state explicitly: `b(v)` counts the array columns whose BIG
    FIBRE sits at v, and those big fibres are carried by LINES — so under delta == 0 the
    number of columns MISSING v is exactly q times the number of LINES carrying v's big
    fibres.  That is a statement about the array's geometry, not a counting total.
 3. Now use it on the non-perfect rows.  Fix a value v.  The q*b(v) columns x with
    v in Z(x) can host v in NO row at all; the remaining n - q*b(v) columns host v with
    total multiplicity n, of which b(v) columns host it (q+1) times and the rest once
    (prove this decomposition; it is (F1) plus step 2).  A row t therefore realizes v
    only at columns outside the Z-set of v, and a PERFECT row r with v in D_r realizes v
    nowhere.  Derive an upper bound on E(t,v) for an ARBITRARY row t, in terms of q and
    b(v), with proof — or show none better than the trivial one exists and say so.
    Then re-derive R(v) with that bound in place and evaluate the resulting cap on p at
    q = 2 and q = 3 (V4).  If it is still order q^2, SAY SO and go to 4 rather than
    presenting it.
 4. **The joint step, where the angle either bites or dies.**  For each value v put
    A_v := {r in P : v in D_r}.  Then |A_v| <= q for every v by (F0) (only q columns miss
    v at all), and Sum_v |A_v| = q*p.  By (F15)(i) every r in A_v lies OUTSIDE the union
    of the b(v) lines {ell_c : g(c) = v}.  Now feed in the pointwise law: those same b(v)
    lines are the carriers of v's big fibres (step 2), and exactly q*b(v) columns miss v.
    Ask whether p = q+1 is compatible with all of this simultaneously — and be exact
    about which values v can have A_v = empty, since values with b(v) = 0 impose no line
    exclusion at all.  Carry beta := #{v : b(v) >= 1} as a symbol; (F0)+(F8) give
    beta >= n/q.  Deliver the sharpest PROVED inequality relating p, beta and q, both
    numerically evaluated (V4), and state in one line the exact extra fact that would
    close it to p <= q.
 5. **The ZERO-FIBRE consequence — the one place the pointwise law constrains a row that
    need NOT be perfect, and therefore the most promising part of this angle.**
    Since b is NOT constant 1 on this sub-branch (V2), put
    `z := #{v : b(v) = 0}`; from (F0) `Sum_v b(v) = n` one gets
    `z = Sum_v max(b(v) - 1, 0)`, so z > 0 exactly when some fibre has b(v) >= 2.
    (a) For a value v with b(v) = 0 the pointwise law gives `m(v) = 0`, i.e. NO array
        column misses v.  By (F11) that says `x not in D_{x*v}` for EVERY x.  Unfold it
        with argument slots explicit (V3): for every value r in the image of the column
        map R_v — that is, every r outside `D_v` — the unique x with `x*v = r` satisfies
        `x not in D_r`; and taking r = nu(v), `ell_v ^ D_{nu(v)} = empty`.
    (b) Fix a row r and let v range over the zero-fibre values.  Prove that the points
        `x_v := R_v^{-1}(r)` obtained in (a) are PAIRWISE DISTINCT as v varies (one
        line: rows are bijections).  Hence there is a set `X_r` of forbidden values with
        `D_r ^ X_r = empty` and `|X_r| >= z - q - 1` (state where the `- q` and the `- 1`
        come from; (F0) and the bijectivity of nu).  Note carefully: this holds for
        EVERY row r, PERFECT OR NOT — that is the point.  Give its cardinality and type
        on both sides (V5).
    (c) Now add perfectness.  For r in P, (F15)(i) additionally forces
        `D_r ^ g(pencil(r)) = empty`, and nu(r) is never in D_r.  So for a perfect row
        the q values of D_r must fit inside `M \ (X_r u g(pencil(r)) u {nu(r)})`.  Turn
        that feasibility condition into a bound: how many rows r can satisfy it at once?
        Evaluate whatever you get at q = 2 and q = 3 (V4) and compare against q^2.
    (d) State the DICHOTOMY honestly, because it decides the angle's worth: when b == 1
        one has z = 0 and (b)-(c) are vacuous, the law degenerating to `m(v) = q` for
        every v.  Say explicitly what the b == 1 case leaves you, and whether any
        constraint on the non-perfect rows survives there.
Deliver, in this order: the law with both derivations and the step-2 self-check printed
in full; the E(t,v) bound of step 3 with its q = 2 and q = 3 evaluations; the step-4
inequality; and steps 5(a)-(d) in full.  A single PROVED all-q lemma from step 2, 3 or 5
is worth more than a sketch of the whole target.

## HARD WORD CAP: 1500 words.  Exceeding it is a defect, not a bonus.
