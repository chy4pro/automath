# ETP 677 -- ARITY-3 COUPLING, ROUND 27.  A DERIVATION IS ASKED FOR, NOT A VERDICT.

## PART 0.0 -- FIREWALL.  READ THIS BEFORE ANYTHING ELSE.
Everything below lives inside ONE branch of ONE sub-problem: the EXTREMAL branch of the
(N)/(N-Prop) rowcap sub-branch.  Nothing here is about ETP 677 -> 255, and no return may
claim otherwise.  All measurements cited are on DESARGUESIAN planes at q = 2, 3, 5.
Narrowings N1 (prime-power order), N2 (prime order for the code certificate) and N3
stand and are not relaxed by anything in this brief.

## PART 0.1 -- WHAT IS ASKED FOR, AND IT IS NOT THE LEMMA.
You are NOT asked to decide the target statement.  You are asked for A DERIVATION:
a chain of steps from the NAMED STOCK FACTS in PART 1 to the TARGET in PART 2, in which
**EVERY STEP CITES THE STOCK FACT IT CONSUMES BY ITS TAG**.  A step that cites nothing
is not a step; it is an assertion, and it will be scored as one.
If you cannot reach the target, say so and hand back THE LONGEST STOCK-CITED PREFIX YOU
CAN JUSTIFY, together with the precise sentence at which the citations run out.  That
return is worth more here than a complete argument with an uncited step, and it is
scored higher.  This is not politeness: an uncited step is the exact defect that has
cost this line seven of its eight closed routes.

## PART 0.2 -- HOW YOU ARE GRADED, INCLUDING WHAT THE GRADING CANNOT SEE.
Three axes, and you are told all three because a scoring rule that hides what it cannot
detect is worse than the defect it prevents.
  * **PROVENANCE.**  Every load-bearing step is checked against the stock and against a
    list of CLOSED ROUTES (PART 3).  A step that re-enters a closed route is refused at
    adjudication whatever its merits.
  * **EXECUTION.**  The held-out table in PART 0.3 is scored AS A CONJUNCTION -- all
    rows together, never one row cited on its own.  Its purpose is to establish that you
    can compute, on a concrete object, the quantities your derivation manipulates in the
    abstract.  Rows are not trivia; each holds out a quantity some step of the intended
    derivation must handle.
  * **TRUTH ON WITNESSES.**  THIS AXIS IS EMPTY, AND YOU ARE TOLD SO.  We hold no object
    satisfying the target's antecedent, at any order we can reach, and this is proved
    rather than merely unobserved.  So NOTHING in this brief or in its grading confirms
    the target statement.  A derivation that passes every check here is a CANDIDATE, not
    a theorem.  Write it that way.  Any sentence in your return asserting that the
    target is established, or that passing the checks establishes it, is struck.

## PART 0.3 -- HELD-OUT TABLE (mandatory; scored as a conjunction).
One instance, printed in PART 4 as `W` together with its column-kernel line set.  Six
quantities, every one of them determined by `W` alone, none of them printed anywhere in
this document.  Answer all six BEFORE your first claim, each with a one-line derivation.
`CANNOT COMPUTE` is a CLEAN answer on any row and costs you nothing; a confident wrong
value costs the row and downgrades every un-derived numeric claim in your body.
**ONE ROW, ONE QUANTITY FAMILY.**  Do not derive one row from another row's answer if
you can derive it from `W`.  **THERE IS NO VERDICT ROW IN THIS TABLE, AND THAT IS
DELIBERATE**: a yes/no row is a coin flip and this campaign has cited two of them.
  R1  From `W`: the set of PERFECT rows -- the rows t whose left-division multiset
      equals its right-division multiset -- as an explicit subset of {0,...,6}, with its
      size.  Derive it from `W`; do not infer it from any general claim you intend to make.
  R2  From `W`: the seven integers `Delta(v)`, v = 0..6, defined in PART 4.  Seven
      integers in order.  Not a summary, not a verdict, not "they are all equal".
  R3  From `W`: the seven integers `k_c := |{perfect rows} ^ ell_c|`, c = 0..6, in column
      order.  This is the vector your PART 2 target is about; it is held out deliberately.
  R4  From `W`: the seven sets `D_c` (the values missing from column c), all seven, each
      with its size.
  R5  From `W`: the seven integers `d_r := |D_r ^ L_r|`, r = 0..6, where `L_r` is the
      transported pencil defined in PART 4.
  R6  From `W`: the set `C_4 := {c : 4 in D_c}`, explicitly, with its size.
**A DISCLOSURE YOU SHOULD USE.**  An earlier return on this line passed every row of a
held-out table and was still wrong on the quantity the round turned on, because the rows
had been chosen for what was convenient to compute.  Rows R1/R2/R3 above are chosen
AGAINST the intended argument instead: they hold out precisely what its load-bearing
step manipulates.  If your argument and those rows disagree, THE ROWS ARE RIGHT.

## PART 1 -- THE STOCK.  These are the only facts you may consume, by tag.
(F1)  Lam(x,.) is a bijection for every x; the array is a left quasigroup on M = {0..6}.
(F2)  Delta = q*b - m, valid pointwise, and it is a LIVE identity of the branch: it is
      refuted by arbitrary permutation-row tables and so is not an identity of the shape.
(F6)  g(c) = nu^{-1}(c) for all c IFF A = n, where A = #{v : nu^2(v) in ell_v}.
(F11) Z(x) may be obtained without building the whole Xi-array.
(N)   the branch's row condition; (N-Prop) its proposition form.  Both as given upstream.
(RC)  ROWCAP AT q=2, A THEOREM AND TIGHT: on the sub-branch where Delta vanishes
      identically, the number of perfect rows is AT MOST 2, and 2 is attained.
      [(R9-K/trace-attain), exhaustive over 589,521,888 representative tables.]
(NZ)  sum_v Delta(v) = 0 identically; consequently exactly one nonzero coordinate is
      impossible.  [(R25/NZ2), one line, all q.]
(TI)  For any table of the form tab[a][t] = a + h(t-a) on Z_n with h a permutation,
      Delta vanishes identically -- using NONE of the branch conditions.  So a scan
      reporting "Delta == 0" on such a family reports the family, not the object.
      [(R26/TRANS-DELTA0).]
(VD)  There exist REAL q=2 tables of the branch carrying q+1 perfect rows in NON-LINE
      position.  Hence the target below is FALSE without its Delta hypothesis, and any
      candidate that does not CONSUME that hypothesis is a proof of something false.
      [(R24/VOID3), 16 of 20 real q=2 design classes.]
(CL)  If a stock's entire content about the perfect-row set is "it is a subset of F"
      plus an m-ary clause, its models at size q+1 are exactly the (q+1)-cliques of the
      m-uniform hypergraph of that clause.  [(R24/CLIQUE3), all q, all m.]

## PART 2 -- THE TARGET.
Let P denote the set of perfect rows.  Show, or fail explicitly and hand back the prefix:
    IF  Delta(t) = 0 for every t in P,  AND  |P| = q+1,   THEN  P is a line.
Consume (VD): a derivation that never uses the Delta hypothesis is refuted before it is
read.  Consume (CL): your clause's arity is the thing that decides whether it can bind a
(q+1)-set at all, and arity <= 2 is proved insufficient.

## PART 3 -- REFUSED AT DISPATCH.  Eight closed routes, by name and citation only.
Any derivation whose load-bearing step re-enters one of these is refused at adjudication
regardless of the mathematics around it.  They are listed so you do not spend on them;
the citations are the authority and the reasons are NOT restated here.
  (1) I-double-count (R12/DEGEN)          (2) gunion (r15)
  (3) collinear (R14/PAIRCAP)             (4) texact / T-SUM (r12, route 6(iii))
  (5) residual non-negativity (r15)       (6) separator / pair-uniqueness (r18-r19)
  (7) linecap-agg (R20/LINECAP summed, r21)
  (8) valid-plane-import (R23/IMPORT-VOID) -- and note its live rider: a SUPPORT-valued
      functional of the k-profile is a COORDINATE ONLY and is a REFUSED TARGET
      ((R24/SECANT-THRESHOLD): bounding it is logically identical to the conclusion).

## PART 4 -- THE INSTANCE, AND THE DEFINITIONS THE HELD-OUT ROWS USE.
`W` is a 7x7 array over M = {0..6}; row a, column t entry is W[a][t].
  W = [[4, 3, 0, 1, 2, 6, 5], [3, 1, 6, 4, 0, 2, 5], [2, 3, 5, 6, 0, 1, 4], [0, 6, 4, 2, 3, 1, 5], [4, 5, 1, 2, 0, 3, 6], [4, 0, 6, 3, 5, 1, 2], [5, 3, 6, 2, 1, 4, 0]]
  nu   = a permutation of M, printed with W in the dispatched copy.
  ell  = the seven column kernels of W, printed with W in the dispatched copy; they
         form the line set of a projective plane of order q = 2.
  pencil(r) = the three lines through r.   L_r = g(pencil(r)) with g as in (F6).
  N(t,.) counts the entries of column t of W; E(t,.) counts the values of Xi_t, where
  Xi_t(x) = Lam(x, Lam(t,x)).  A row t is PERFECT when E(t,.) = N(t,.) as multisets.
  Delta(v) := (sum_t E(t,v)) - n.
  D_c := M \ {W[a][c] : a in M}.

## PART 5 -- SCREENS THIS BRIEF CITES, EACH WITH ITS CHANCE RATE (RULING BR).
No screen is cited here without the rate at which it passes by chance, because a screen
that cannot fail is not evidence.

  * (VD) / (R24/VOID3) against a P-FREE candidate         chance: 16/16 expected violations       
      POWER: HIGH -- a false P-free candidate is violated by every counterexample.
  * (VD) / (R24/VOID3) against a P-RESTRICTED candidate   chance: 11.37 expected vs 12 observed   
      POWER: NONE ((R25/POWER)).  IT IS NOT CITED AS A SCREEN IN THIS BRIEF; it is cited only as the REFUTATION it is, in (VD).
  * a control set of objects satisfying the antecedent    chance: n/a                             
      POWER: EMPTY.  q=2 unsatisfiable (RC); q=3 the only exhaustion we own has |P| = 0 on all 1,070,784 objects, so it passes 100% by construction.
  * the held-out table of PART 0.3, AS A CONJUNCTION      chance: see the computed conjunction rate below
      POWER: COMPUTED THIS ROUND on 677 rows, not imported.  Cited only as a conjunction; there is no verdict row and no row is cited alone.
  * any `Delta == 0` scan on a translation-invariant fam  chance: 100% PASS                       
      POWER: ZERO -- (TI) makes it a self-satisfied invariant.  NOT CITED as evidence anywhere.