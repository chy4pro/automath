# Adversarial review of `papers/etp677_structure/main.tex` (round 1)

Date: 2026-08-17  
Role: verifier, not co-author

## Verdict

**INVALID**

The draft contains several sound and well-scoped core results, including the
order-176 model itself, the affine-fibre theorem (source R5-C, Theorem 5.1), the
range-limited 176 minimality proposition, and the explicitly partial 22/87
order-11 census. However, it also contains claims that cross the boundary the
paper itself says must not be crossed: most seriously, it promotes the
affine-fibre `{1,3}` collision to left-injectivity for arbitrary fibre tables,
even though that general-table case is exactly the open R5-A search. It also
states an order-10 exclusion for cycle length 5 that the source says is
unfinished, and calls bounded saturation a proof that whole classes of
arguments are ruled out. Several machine-verification labels exceed what the
cited scripts actually execute.

## CRITICAL ERROR

### C1. The affine `{1,3}` argument is incorrectly generalized to arbitrary fibre operations

- **Location:** lines 1410--1417 (end of Section 4.4), repeated at lines
  2163--2170 (the “general-magma `{1,3}` collision” problem).
- **Problem:** The text infers that whenever the two blueprint positions
  coincide, the general fibre operation `diamond_{y,x}` is left-injective.
  Coincidence of positions 1 and 3 does not imply pointwise left-injectivity
  for a general table. The position-conflict argument uses affine fibres:
  degeneracy is represented by the scalar condition `a_d=0`, which turns a
  point collision into a uniform row collision. This promotion is precisely
  what fails for general tables. If the displayed general claim were true,
  the open general-table TI and pair-indexed searches would already be
  settled.
- **Source of truth:** `problems/etp677/R5A_codex_report.md`, especially the
  E255 column condition and the discussion of general table cells; the
  corrected Round-5 entry in `problems/etp677/campaign_registry.md`, which
  explicitly says R5-C Theorem 5.1 covers **affine fibres only** and that
  general-table TI and shift-ansatz searches remain open; and
  `problems/etp677/R5C_soff_report.md`, Section 5, whose proof is entirely in
  the scalar-affine setting despite its own over-broad concluding prose.
- **Impact:** This breaks a substantive structural claim and contradicts the
  paper's correctly scoped diagonal-protection theorem at lines 1344--1372.

### C2. Cycle length 5 is falsely declared impossible through order 10

- **Location:** lines 2188--2192.
- **Problem:** The draft says both `m(y)=4` and `m(y)=5` are unrealizable for
  `n<=10`. Only the `m(0)=4` order-10 subcase was exhausted. The order-10
  cases `m(0)=5,...,10` were still running. The paper itself states the
  correct status at lines 1916--1921, so this is also an internal
  contradiction.
- **Source of truth:** `problems/etp677/F1_structural_report.md`, Sections 5.1
  and 5.3: all order-10 `m(0)=4` classes are UNSAT, while the 19 remaining
  subproblems, beginning with `m(0)=5`, are unfinished. The same status is
  summarized in `problems/etp677/R3B_parity_report.md`.
- **Impact:** This turns a partial computation into a theorem-strength
  exclusion.

### C3. Bounded saturation is repeatedly promoted from evidence to an impossibility theorem

- **Location:** abstract lines 112--115; introduction lines 149--154 and
  216--220; Proposition B1 and its reading, lines 1491--1518; blocked-routes
  table lines 1824--1827; summary lines 2218--2225.
- **Problem:** Proposition B1 reports depth-bounded and pool-restricted
  saturation experiments. Failure of those searches to derive E255 or `(Q)`
  does not rule out an equational or quasi-equational proof. Lines 1513--1515
  correctly call the result “computational evidence,” but the abstract,
  table, and final summary say the route is “ruled out,” “provably closed,”
  and something a proof “may not be.” Those stronger statements do not
  follow. The free-magma argument rules out an identity proof of E255 from
  E677 alone, but it does not rule out the left-quasigroup/quasi-equational
  setting; the draft acknowledges exactly this limitation at lines
  1465--1468 for the sibling statement.
- **Source of truth:** `problems/etp677/F5_counting_report.md`, Section 4,
  which labels these as computational saturation results; and
  `problems/etp677/R3F_codex_report.md`, “Bounded derivation attempt,” which
  explicitly says bounded non-closure does not prove underivability.
- **Impact:** The paper's advertised “obstruction map” misclassifies a failed
  finite search as a mathematical closure theorem.

### C4. Corollary 4.6 omits the fibre-size hypothesis needed for its iff criterion

- **Location:** lines 1297--1308, Corollary “exact criterion for the failure
  of `(S-off)`.”
- **Problem:** The displayed equivalence
  `S-off holds iff A_0 intersect rho(A_0) is empty` is stated without a fibre
  size hypothesis. The supplied counting argument establishes the reverse
  implication only for `|M|>=3`: at most `2|M|` hit conditions must leave a
  pair among `|M|^2`. At `|M|=2`, that inequality is not strict and the two
  hit conditions can cover every pair. The parenthetical at lines 1306--1308
  does not repair the unqualified theorem statement.
- **Source of truth:** `problems/etp677/R5C_soff_report.md`, Corollary 2.4,
  where the same proof explicitly introduces “for `|M|>=3`.”
- **Impact:** The theorem is stronger than its proof and source support.

### C5. The paper overstates what the order-176 example refutes about isoperimetry

- **Location:** abstract lines 105--111; introduction lines 208--220;
  Corollary 4.2(c), lines 1180--1197; lines 1734--1749; final summary lines
  2222--2225.
- **Problem:** The concrete target refuted by the model is the particular
  threshold `e(O)<=|O||O^c|` uniformly over a fixed size class. The abstract
  says it refutes “every uniform isoperimetric upper bound,” and later prose
  says no uniform upper bound can exist. Those statements are literally much
  broader (trivial and other uniform upper bounds do exist) and do not follow
  from the example. What is closed is the R3-C averaging route using that
  specific threshold, not every conceivable off-diagonal or isoperimetric
  argument.
- **Source of truth:** `problems/etp677/R3C_linking_report.md`, Section 5,
  which identifies the exact threshold; `problems/etp677/R5C_soff_report.md`,
  Section 4.2, which tests/refutes that threshold.
- **Impact:** The advertised scope of a major negative result is false.

## JUSTIFICATION GAP

### J1. “Complete classification” and the exact affine spectrum lack the noncommuting converse

- **Location:** abstract lines 96--103; introduction lines 191--201; Section 3
  title and lines 764--770; Theorems 3.1 and 3.2, especially lines 831--844.
- **Problem:** The general affine criterion allows arbitrary
  `F,G in End(A)` and gives two noncommutative equations. The polynomial
  `P(G)` and `Z[u]/(P)` module description are derived only after assuming
  `F` and `G` commute and setting `F=(G+G^3)^{-1}`. Neither the paper nor the
  cited report proves that every affine E677 solution of the general
  equations must commute or arise from this `R`-module construction.
  Therefore the construction of all `R`-module models is proved, but the
  converse needed for “orders realized exactly” and “complete
  classification” is missing.
- **Source of truth:** `problems/etp677/R3B_parity_report.md`, Theorem 1(a)
  versus Theorem 1(c)/Theorem 1-prime. The latter says every finite
  `R`-module gives a model; it does not supply the missing converse from the
  noncommutative equations. The cited `final_verify.py` only tests scalar,
  hence commuting, models over cyclic groups.

### J2. The isoperimetric extrema have no cited verifier

- **Location:** lines 1172--1187, especially the claimed values of
  `max_{|O|=s}(e(O)-|O||O^c|)` for all size classes.
- **Problem:** The marker cites `verify176.py` and `minimal_scan.py`.
  `verify176.py` constructs the model and checks E677, rows, N margins, E255,
  N values, right cancellation, and `(S-off)` pairs; it never computes
  `e(O)` or any subset extrema. `minimal_scan.py` searches TI fibre families
  and likewise contains no subset/isoperimetric calculation. No repository
  script containing the quoted `+282` extremum or the all-size scan was
  found. The explicit two-point witness `e({0,65})=350>348` is readily
  checkable, but the all-size/extremal claim is not machine-verified by the
  cited artefacts.
- **Source of truth:** the actual source of
  `problems/etp677/R5C_scripts/verify176.py` and
  `problems/etp677/R5C_scripts/minimal_scan.py`; the unsupported claim is
  inherited from `problems/etp677/R5C_soff_report.md`, Section 4.2.

### J3. `term_search.py` checks a sample, not all 111,600 forced pairs

- **Location:** lines 1470--1475 and artefact description lines 2291--2292.
- **Problem:** The prose says the displayed term equals the unique witness
  on **all** 111,600 forced ordered pairs and labels that statement
  machine-verified. The script explicitly draws a deterministic random
  sample, of size 1,200 by default, builds term functions only on that sample,
  and reports agreement “fraction of sample.” It contains no subsequent
  full-domain verification of the found term.
- **Source of truth:** `problems/etp677/R5C_scripts/term_search.py`, especially
  `SAMP`, `random.sample`, and the sampled `target`; archived
  `term_search.out` reports the sample search, not an all-pairs pass.

### J4. The `verify176.py` label is attached to claims the script does not check

- **Location:** Theorem 4.1 lines 1121--1155, especially `r_t=c_v=146`; and
  Proposition 4.3 lines 1199--1210.
- **Problem:** The rerun confirms the core model claims, but the script does
  not calculate row/column support sizes `r_t,c_v`, strong connectivity,
  diameter 2, `Q=sum N^2`, or the complete `F_{pq}` distribution. Therefore
  it does not machine-verify the exact full statements to which its marker is
  attached. These additional claims may be true, but need their actual
  verifier or a proof.
- **Source of truth:** `problems/etp677/R5C_scripts/verify176.py`; comparison
  with `problems/etp677/R5C_soff_report.md`, Sections 1.2 and 4.3.

### J5. The generic near-miss claim is extrapolated from two tested orders

- **Location:** lines 1975--1989, especially lines 1982--1984.
- **Problem:** The explicit order-11 near-miss is supported. The stronger
  sentence says the same row-transposition recipe gives exactly five failures
  “at every order carrying an E677 magma,” while immediately admitting it was
  checked only at `n=5,11`. No uniform proof is supplied, and the source
  report also presents those two computations rather than a theorem over all
  orders/models.
- **Source of truth:** `problems/etp677/F5_counting_report.md`, Section 5.1,
  and its `nearmiss.py` coverage.

### J6. The claimed four-way cross-validation of the complete `n<=9` classification is overstated

- **Location:** abstract lines 118--120; introduction lines 224--229;
  Theorem 6.1 and cross-validation paragraph lines 1863--1900.
- **Problem:** F1's `cp677.c` is the source claiming a complete scan through
  order 9. The other listed implementations have smaller or different exact
  coverage: F5 reports complete classification through 7 and had order 8
  unresolved in its report; R2 is scoped through 6; R3-B's C run confirms
  emptiness/existence through 9 but does not enumerate the order-9
  isomorphism classification. Thus the result may be correct, but the
  *complete classification* was not independently cross-validated four ways.
- **Source of truth:** `problems/etp677/F1_structural_report.md`, Section 5.1;
  `problems/etp677/F5_counting_report.md`, Section 3;
  `problems/etp677/R2_Qprime_codex_report.md`, Section 5; and
  `problems/etp677/R3B_parity_report.md`, exhaustive-search table.

### J7. The `m=2` extension impossibility is asserted inside an unmarked proposition without its proof

- **Location:** Proposition 5.9, lines 1756--1764.
- **Problem:** The proposition has no verification marker despite the paper's
  convention, and its last sentence asserts that fibre size 2 is “provably
  impossible” without proof or a precise reference. The campaign registry
  records the claim, but the cited R5-A report is an encoding audit and m=5/7
  backtracker handoff, not a proof of the m=2 classification.
- **Source of truth:** `problems/etp677/campaign_registry.md`, Round-5 B4
  entry; `problems/etp677/R5A_codex_report.md`.

## EDITORIAL

### E1. The paper promises a marker on every numbered statement, but does not supply one

- **Location:** lines 67--73; examples include Lemma 2.1 at lines 268--271
  (bibliographic attribution but no status marker) and Proposition 5.9 at
  lines 1756--1764 (no marker or citation on the proposition itself).
- **Problem:** This makes the stated verification convention unreliable as a
  mechanical audit device.

### E2. The transport/state-map notation `T` is overloaded incompatibly

- **Location:** `T(t,v,x)` is a three-coordinate state map at lines
  1533--1545; `T(a,t)=(Lambda_t a,v)` is a different two-coordinate transport
  at lines 1615--1619; line 1650 then writes `T(x_k,x_{k-1})` while discussing
  the latter. Elsewhere `T[delta]` denotes fibre operation tables.
- **Problem:** These are not harmless variants of one map; arities and domains
  differ, so later cross-references are ambiguous.
- **Source of truth:** `problems/etp677/R2_Qprime_codex_report.md`, Section 2,
  for the three-coordinate state map; `problems/etp677/R3C_linking_report.md`,
  Section 2, for the transport map.

### E3. Support-size notation is used long before it is defined

- **Location:** `r_t=c_v=146` at line 1154; `r_t` and `c_v` are introduced
  only at lines 2080 and 2089.
- **Problem:** This makes Theorem 4.2 non-self-contained and obscures what the
  146 measures.

### E4. The “complete TI structure theory” wording conflicts with the actual affine-fibre setting

- **Location:** lines 211--214, 1231--1238, and bibliography lines
  2406--2409.
- **Problem:** The section's working setting restricts all fibre operations to
  affine maps, and the scope correction at lines 1365--1372 says general TI
  tables remain open. Calling the section a complete structure theory of the
  TI family without “affine fibres” invites exactly the invalid reading the
  correction warns against.

### E5. The small-order lower bound is needlessly inconsistent with the paper's own theorem

- **Location:** lines 2148--2152.
- **Problem:** It says the least non-right-cancellative order is “at least 8,”
  while Theorem 6.1 claims every model through order 9 is a quasigroup (and
  order 8 is empty). The stronger lower bound supplied by the draft itself is
  at least 10. The stated bound is not logically false, but it makes the
  landscape look less settled than the paper claims elsewhere.

### E6. Compilation has no unresolved citations/references, but does have a duplicate hyperref object

- **Location:** `papers/etp677_structure/compile.log`, final warning
  `Object @equation.2.1 already defined`; numerous large overfull boxes also
  occur in theorem/status lines and the artefact table.
- **Problem:** Cross-references resolve, but the duplicate equation anchor can
  produce an incorrect hyperlink target. This is an internal-numbering issue,
  not a mathematical defect.

## Spot-run verification record

The following cited checks were rerun in this review:

1. `problems/etp677/R5C_scripts/verify176.py` (run from `/tmp` so its generated
   JSON did not overwrite the repository artefact): exit 0; order 176; zero
   E677 violations; all rows permutations; E255 holds; N values `{0,1,16}`;
   2,640 unordered `(S-off)` violations; distribution
   `{0:2640, 2:12584, 32:176}`.
2. `problems/etp677/r5a_audit.py`: exit 0; printed `PASS` for pair
   subscripts, TI quadruples, `d*=25`, and the derangement reduction.
3. `problems/etp677/r3f_enum.py check-named`: exit 0; all five named models
   (orders 5, 7, 7, 9, 16) reported medial, E255, and Latin.
4. `conflict_check.diag_check()` from
   `problems/etp677/R5C_scripts/conflict_check.py`: exit 0; the claimed
   `D1(-c/A)=D3(-c/A)=c/A` coincidence passed for all enumerated TI bases at
   `p in {5,11,31,41,61,71}`.
5. `problems/etp677/R3B_scripts/final_verify.py`: exit 0; zero scalar cyclic
   criterion mismatches for `Z_m`, `m<40`; eight GF(16) roots all gave
   E677/E255/Latin models; the printed affine order lists match the draft.

These reruns support the concrete model and finite computations they actually
perform. They do not repair the scope and coverage gaps listed above.

## Correctly scoped high-risk items

For clarity, the following specifically requested danger points are handled
correctly in their principal numbered statements:

- Theorem 4.8 (lines 1344--1350) explicitly says **affine fibres**, and the
  scope-retraction at lines 1365--1372 is accurate. The error is the later
  unqualified generalization identified in C1.
- Proposition 4.11 (lines 1423--1453) explicitly limits 176 minimality to the
  scanned theta-family with `p in {5,11}`, `q<=32`, and expressly denies
  global minimality.
- Proposition 6.3 (lines 1933--1950) accurately reports 22/87 completed
  order-11 pointed types and 0/174 at order 13; the provisional affine case is
  not counted among the 22.
- The community `n<=10` DRAT result is not silently adopted: lines 2068--2069
  call it unreviewed and make the stronger lower bound conditional on accepting
  it.
