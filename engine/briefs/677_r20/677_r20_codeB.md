# Finite-combinatorics research brief (self-contained). Construction task.
# BRIEF VERSION: r20 brief v1 (2026-08-22, owner-677)

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
      with b == 1 AND objects carrying a fibre of size 2 (registry (R9-K): bmax
      histogram {1: 10634, 2: 6561} over 17195 delta == 0 tables).**
      **HOW V2 APPLIES THIS ROUND — SCOPED, NOT SUSPENDED.**  Your angle ASSUMES the
      restriction b == 1 as an explicit scope hypothesis (below), and on that stratum g
      IS a bijection.  So V2 is not waived and not free: every step that reads a value
      back to a column must carry, in brackets on the same line, the words
      `[licensed by the scope hypothesis b == 1]` AND one clause saying what the step
      becomes when some fibre has b(v) = 2 or b(v) = 0 — the primed witness above is
      printed precisely so that the scope stays a RESTRICTION and does not silently
      become a habit.  A g-inversion with no such bracket is a void, exactly as before.
      For the PRINTED INSTANCE, whether it lies in the stratum is a HELD-OUT question:
      derive b from the instance (rows H2a/H2b), never from the scope hypothesis.
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
Seven quantities, all fully determined by data printed in this brief, none of them
printed anywhere in it.  Answer all seven in a table before your first claim, each with
a one-line derivation.  **All seven are about the PRINTED INSTANCE (the table W below),
never about the b-witness.**  Rows are tiered and the tiers are graded differently:
  * `[H]` = hand-derivable in at most ~25 lookups.  A confident WRONG value on an `[H]`
    row VOIDS THE ROUND regardless of the mathematics after it.
  * `[C]` = genuinely computational.  `CANNOT COMPUTE` on a `[C]` row is a CLEAN answer
    and costs you nothing.  A confident wrong value on a `[C]` row does not by itself
    void the round, but it downgrades every un-derived numeric claim in your body to
    CONJECTURE — so use the hatch rather than guess.
**ONE ROW, ONE QUANTITY FAMILY.**  The rows are deliberately split so that a single slip
costs one row and not the round: a verdict gets a row of its own, never a row shared with
the data it is computed from.  Answer each row independently; do not derive one row's
answer from another row's answer if you can derive it from the table.
**AND A DISCLOSURE ABOUT HOW THIS TABLE WAS BUILT, WHICH YOU SHOULD USE.**  A previous
return passed EVERY row of a held-out table and was nevertheless wrong on the one
quantity the round actually turned on — because the rows had been chosen for what was
convenient to compute.  The rows below are chosen AGAINST the argument instead: rows
H4/H5/H6 hold out precisely the quantity your load-bearing step manipulates.  If your
argument and those rows disagree, the rows are right and the argument is wrong.
  H1  `[H]`  From the table W: the sets `D_0`, `D_3` and `D_6` (the values missing from
      columns 0, 3 and 6 of W).  Give each as an explicit set and state its size.
  H2  `[H]`  From the table W: `g(c) = nu(c)\c` for all seven columns c = 0..6.  Seven
      values, nothing else on this row.
  H3  `[C]`  From the table W: the set `Z(x)` for every x = 0..6.  State which route you
      used ((F1)/(F11) is far cheaper than building the whole Xi-array).
  H4  `[C]`  **The set `P` of PERFECT rows of this instance** — the rows t with
      `E(t,.) = N(t,.)`.  Give it as an explicit subset of {0,...,6} and state `|P|`.
      Do NOT infer it from any general claim you intend to make; derive it from W.
  H5  `[C]`  **The seven integers `k_c := |P ^ ell_c|`, c = 0..6, in column order.**
      Seven integers, not a verdict, not a summary.  (This is the vector your angle is
      about.  It is held out deliberately.)
  H6  `[C]`  **The single VERDICT: is `k_c mod 2` the SAME for all seven columns c?**
      Yes or no, with one line of reason.  Scored on its own: a wrong H5 does not
      double-count here, and a right H6 does not rescue a wrong H5.
  H7  `[C]`  For the value x = 4: the set `C_4 := {c : 4 in D_c}` of columns missing the
      value 4, given as an explicit set, together with `|C_4|`.  (H7 is deliberately
      independent of H4-H6: one slip must not cost you two rows.)

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

## REFUSED AT DISPATCH — SIX CLOSED ROUTES, BY NAME AND CITATION ONLY
These six are CLOSED.  They are listed by NAME and REGISTRY CITATION and their content is
deliberately NOT reprinted: restating a closed route's data in a brief has, in this
campaign, handed answers to questions the brief was holding out.  If your load-bearing
step is one of these, your answer is REFUSED WITHOUT READING — so check the list first.
  (1) the global double count of `I = {(x,c) : x in D_c}`      — (R12/DEGEN), PROVED, all q
  (2) the g-fibre LINE-UNION exclusion                          — retired empirically, all q
  (3) the plane's PAIR COUNT / any per-line cap `k_c <= K`      — (R14/PAIRCAP), PROVED, all q
  (4) the ZERO-FIBRE route on the `b >= 2` branch               — closed, all q
  (5) the (F15)(ii) fibre-collision route on `b >= 2`           — closed, all q
  (6) the SEPARATOR / pair-uniqueness route                     — closed r18-r19, all q

**THE PATTERN, AND IT IS NOW A THEOREM RATHER THAN A TALLY — read this before choosing
your route.**  Write `k_c := |P ^ ell_c|`.  The two incidence identities this line keeps
aggregating through,
        `Sum_c k_c = (q+1)|P|`      and      `Sum_c C(k_c,2) = C(|P|,2)`,
are exactly the first two BINOMIAL MOMENTS of `k`, and both are functions of `|P|` ALONE.
They therefore hold for EVERY point set and retain, after aggregation, **ZERO information
about the CONFIGURATION of P**.  Concretely: a LINE and a `(q+1)`-ARC have IDENTICAL
moments 1 and 2 and first differ at moment 3 (`C(q+1,3)` versus `0`).  All six routes
above die of this one fact, and so does every spectral/eigenvalue argument, since the
plane axioms give `A A^T = qI + J` and hence `||A^T 1_P||^2 = q|P| + |P|^2`, again
`|P|`-determined.
**Consequence, and it is the whole reason for your angle: no conjunction of single-row and
pair-row conditions can distinguish "P is a line" from "P is an arc".  Any ingredient that
still aggregates through those two identities is not a new ingredient.**
**Therefore: before you submit any bound, evaluate it at q = 2 and q = 3 (V4).  If it
comes out at or above q^2 (>= 4 at q = 2, >= 9 at q = 3) it is a KNOWN result of this
line and is NOT a deliverable — say so plainly and do not present it as progress.**

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

## YOUR ANGLE — THE p-ARY CODE OF THE PLANE, IN THE ONLY FORM THAT CAN BE TRUE

### THE IMPORT (use freely, do NOT re-prove; it is classical)
**(AK) Assmus-Key.**  For a projective plane `Pi` of order `q = p^h` (`p` prime), let
`C_p(Pi) <= GF(p)^M` be the span of the incidence vectors of the n lines.  Then
`C_p(Pi)` has MINIMUM WEIGHT `q+1`, and its weight-`(q+1)` codewords are EXACTLY the
scalar multiples of the incidence vectors of LINES.
**DECLARED NARROWING, carried on every claim you make from it: (AK) needs `q = p^h`, so
this route can prove the target only for planes of PRIME-POWER order.**  State that
narrowing in your own conclusion; an unqualified conclusion is scored as overreach.

### THE BRIDGE, PROVED — ADD IT TO THE TOOLKIT AS (F16)
 (F16) [PROVED, every plane of order `q = p^h`, EVERY point set S]
       `1_S in C_p(Pi)`  ==>  `k_c := |S ^ ell_c| == |S| (mod p)` for EVERY line c.
       Proof, three lines: `<1_S, 1_ell_c> = k_c` in `GF(p)`; two lines meet in exactly
       one point and `|ell| = q+1 == 1 (mod p)` since `p | q`, so `<1_ell, 1_ell'> == 1`
       for ALL pairs equal or not; writing `1_S = Sum_ell lam_ell 1_ell` gives
       `k_c == Sum_ell lam_ell`, independent of c; summing over the n lines,
       `Sum_c k_c = (q+1)|S| == |S|` and `== n * (Sum lam) == Sum lam` since
       `n = q^2+q+1 == 1 (mod p)`.  QED
       **MEASURED, at q = 2, 3, 4, 5, by exhaustion over ALL `(q+1)`-subsets of the
       plane: among sets of size exactly `q+1`, "the `k`-profile is constant mod p" holds
       for exactly n sets, and those n sets are exactly the n LINES.**  So at the weight
       that matters the mod-p `k`-profile CHARACTERISES lines.  That is a measurement on
       four planes, NOT a theorem at general q; treat it as evidence, and if your argument
       needs it at general q, say so and label the step CONJECTURE.

### THE TRAP, DECLARED BEFORE YOU START — TWO OF THEM
**T1.  "`k` is in the code" is a SELF-SATISFIED INVARIANT.**  `k = A^T 1_P` lies in the
image of `A^T` BY CONSTRUCTION, for every point set whatsoever.  Any step whose content
is "`k` is in the row space" has proved nothing and will be scored as ABSENT.  The content
is the REVERSE reading: forcing `1_P` ITSELF into `C_p(Pi)`.
**T2.  AND THE UNCONDITIONAL REVERSE READING IS FALSE.  Do not try to prove it.**
The target `|P| <= q` is TIGHT at `q = 2`: `delta == 0` objects with `|P| = q` exist
(exhaustive, registry).  A nonzero codeword has weight at least `q+1 = 3`, so on such an
object `1_P` is NOT a codeword.  Hence
        "`delta == 0  ==>  1_P in C_p(Pi)`"   is FALSE,
and by (F16) so is "`delta == 0 ==> k` is constant mod p".  **A proof of either is a proof
of something false; if your derivation reaches one of them, you have an error, and finding
it is worth more than the rest of your answer.**

### THE EQUIVALENCE DISCLOSURE — READ IT BEFORE YOU CHOOSE A ROUTE
**(F19) [PROVED for `q = p` prime; MEASURED at q = 4]  For `|S| = q+1`:
`k` constant mod p  <==>  `1_S in C_p(Pi)`  <==>  `S` is a LINE.**
(At prime order `dim C_p = (n+1)/2` exactly, so the mod-p `k`-profile IS membership;
(AK) then identifies the weight-`(q+1)` codewords with the lines.)
**So the statement you are asked for below is LOGICALLY IDENTICAL to "`|P| = q+1` implies
P is a line".  The code does not give you a stepping stone toward the line case — it
RENAMES it.**  Two consequences, and they decide whether your answer is worth anything:
  * **WORTHLESS, and scored as ABSENT:** derive "P is a line" from the geometry and then
    observe that `k` is constant mod p.  That is circular at the level of the whole route.
  * **THE ONLY PAYING ROUTE:** derive the membership `1_P in C_p(Pi)` ALGEBRAICALLY — from
    `delta == 0` and the mod-p vanishings it manufactures ((F2) gives `m(v) = q*b(v) == 0
    (mod p)` at every value; (F17) is its row-side twin) — **WITHOUT first knowing the
    configuration of P.**  (AK) then returns "P is a line" for free, and THAT is a genuine
    arity-n step that no conjunction of pair conditions can supply.
**If you conclude that no such algebraic route exists, say so and say why: that verdict is
this round's most valuable possible outcome, and it is ranked above a partial proof.**

### WHAT YOU ARE ASKED TO PROVE — THE CONDITIONAL FORM, AND ONLY IT
 (COND)  `delta == 0`  AND  `|P| = q+1`   ==>   `k_c == 1 (mod p)` for every column c.
         (`|P| = q+1 == 1 (mod p)`, so by (F16) this is exactly `1_P in C_p(Pi)`.)
Then, by (AK) at weight `q+1`, `P` would be a LINE, and the remaining task is to refute
the line case.
**THE VOID TEST, PRE-REGISTERED, AND IT IS MECHANICAL.**  Your proof of (COND) MUST
CONSUME the hypothesis `|P| = q+1`.  Point at the line where it is used and say what
breaks without it.  A derivation that never uses it has proved the unconditional form,
which T2 says is FALSE — so such an answer is VOID regardless of how it reads.
**AND A VACUITY WARNING, ALSO PRE-REGISTERED.**  At `q = 2`, `|P| = q+1 = 3` is NOT
realizable on `delta == 0` (exhaustive, registry: the maximum there is 2).  So (COND) is
VACUOUSLY TRUE at `q = 2` and NO `q = 2` object can test it.  An answer that "verifies
(COND) at q = 2" has verified nothing and must say so; the first testable order is q = 3.

### THE ARRAY-SIDE DICTIONARY YOU ARE GIVEN
Two identities, both derived from (F0)-(F15), both machine-checked.  They are the material
a proof of (COND) has to work with; you are not required to use them.
 (F17) [derived from the N-profile of (b) + (F11)/(F14); all q; ANY set P, no perfectness]
       `Sum_{r in P} N(r,v) = |P| + q*[nu^{-1}(v) in P] - |P ^ C_v|` for every value v,
       where `C_v = {c : v in D_c} = {v*w : w in Z(v)}` has size q.  Mod p, since `p | q`:
       `Sum_{r in P} N(r,v) == |P| - |P ^ C_v| (mod p)`.
       Note what this is NOT: it uses no perfectness, so it is an identity and not a
       constraint.  It is listed because it is the ROW-side twin of the column-side
       vanishing `m(v) = q*b(v) == 0 (mod p)` that `delta == 0` supplies through (F2).
 (F18) [from (F15)(i); all q]  for every column c:
       `k_c <= (q+1) - |ell_c ^ C_{g(c)}|`, because a perfect `r in ell_c` has
       `g(c) not in D_r`, i.e. `r not in C_{g(c)}`.
       This is the ONLY per-line upper bound on `k` the toolkit supplies — and note it is
       a per-line CAP, so by refused route (3) it can never on its own deliver the target.
       Use it as a local ingredient, never as your aggregation.

### SUB-TASKS, IN ORDER
 1. **(COND), or its refutation.**  Prove (COND), or exhibit the obstruction.  Either
    outcome is a deliverable.  For every step, state PROVED-all-q / PROVED-at-q=2 /
    CONJECTURE.  Discharge the VOID TEST explicitly: name the line where `|P| = q+1` is
    consumed.
 2. **THE LINE CASE.**  Independently of whether you prove (COND): assume `P = ell_{c*}`
    is a full line of `q+1` perfect rows and try to derive a contradiction from
    (F0)-(F15) + (F17) + (F18).  A complete refutation of the line case is worth as much
    as (COND) itself, and the two together close `|P| = q+1`.
 3. **MANDATORY SELF-TEST, V7 FORM, WITH TEETH.**  For every necessary condition you
    propose, state in one line what value or configuration would REFUTE it, then TEST IT
    ON THE PRINTED INSTANCE and name the rows or columns that pass and that fail.  A
    condition satisfied by every row/column of the instance is a SELF-SATISFIED INVARIANT
    and is worth nothing — say so plainly rather than reporting it as a confirmation.  A
    self-check with no stated refuter scores as ABSENT (V6/V7) and voids what rests on it.
 4. **THE HONEST EXIT.**  If (COND) resists, do not manufacture it.  Name, in at most five
    lines, the exact ADDITIONAL INGREDIENT a proof of (COND) needs — a property of the
    array, of the plane, or of the pair `(D, Pi)` — and say why nothing in (F0)-(F18)
    supplies it.  A precise statement of the missing ingredient is ranked EQUAL with a
    proved lemma this round, and far above a bound that lands at `q^2`.
Deliver in this order: sub-task 1 with its void-test discharge; sub-task 2; the sub-task 3
self-tests with refuters and instance rows named; and sub-task 4 if it applies.

## HARD WORD CAP: 1500 words.  Exceeding it is a defect, not a bonus.

