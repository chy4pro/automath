# Adversarial review of `papers/etp677_structure/main.tex` (round 2)

Date: 2026-08-17  
Role: verifier, not co-author  
Audited snapshot: 2,759 lines, SHA-256
`d3e94e9000fd922d4b3b45cffee99a46d25d185919bf58d2e9d30f1abef52079`

## Verdict

**VALID-WITH-GAPS**

Version 2 repairs the central scope errors of version 1. In particular, the
general-table `{1,3}` question is again open, the order-10 cycle-length ranges
are honest, the order-176 isoperimetric conclusion is restricted to the exact
threshold it refutes, and the three new numerical verifiers reproduce their
principal advertised results.

The repair is not complete. The manuscript still draws a theorem-strength
conclusion from bounded saturation in one final sentence, and its purported
scope correction for affine models is contradicted by the unqualified claim
that every affine E677 model is medial. For an affine operation, mediality is
equivalent to `FG=GF`; thus that proposition assumes the answer to the paper's
own open noncommuting-coefficient problem. The isoperimetric repair also adds
an unsupported assertion about exact maxima at sizes 4 and 5. These are real
gaps, but they do not invalidate the order-176 construction or the manuscript's
other principal corrected conclusions.

## Round-1 finding audit

### Critical errors

#### C1 — FIXED

The affine `{1,3}` collision is no longer generalized to arbitrary fibre
tables. Lines 1407--1414 impose both the translation-invariant and affine-fibre
restrictions; Theorem 4.8 at lines 1549--1568 is expressly affine; and lines
1618--1638 distinguish the general subscript coincidence from the unavailable
general-table injectivity conclusion. The general-table collision problem at
lines 2472--2489 correctly states the R5-A question as open. This is a
substantive repair, not a change of
terminology.

#### C2 — FIXED

The exclusions now have their correct different ranges. Proposition 6.2(b),
lines 2205--2212, reports only the completed `m(0)=4` order-10 subcase and says
that `m(0)=5,...,10` were discontinued without a verdict. The open problem at
lines 2506--2513 says `m=4` is excluded through order 10 and `m=5` only through
order 9. This agrees with F1 and R3-B.

#### C3 — PARTIALLY-FIXED

The abstract (lines 198--200), introduction (lines 313--320), the reading after
Proposition B1 (lines 1737--1757), and the closed-routes table (lines
2088--2092) all now say correctly that bounded saturation is evidence rather
than an underivability proof. The free-magma result is also correctly limited
to the `{*}` language.

One theorem-strength conclusion remains. After expressly saying that an
equational or quasi-equational derivation "is not proved impossible," lines
2547--2551 conclude, "So a proof must be global." A still-possible unbounded
equational derivation need not be global in the intended counting sense. This
should remain a heuristic expectation (`the experiments suggest...`), not a
necessary profile of every proof.

#### C4 — FIXED

Corollary 4.6 is now split correctly: failure of S-off implies a collision in
the degenerate-index set without a fibre-size assumption, while the converse
and the displayed iff are explicitly restricted to `|M|>=3` (lines
1481--1492). The proof at lines 1494--1505 uses the strict inequality
`|M|^2>2|M|`, and the following paragraph isolates the `|M|=2` exception.

#### C5 — FIXED

The abstract, Corollary 4.2(c), Section 5.7, the closed-routes table, and the
final summary consistently identify the refuted bound as the particular
threshold

`e(O) <= |O||O^c|`

uniform over a size class. Lines 1372--1376 and 1986--1990 expressly deny any
claim about all conceivable isoperimetric bounds. This matches the R3-C route
actually refuted by the model.

### Justification gaps

#### J1 — PARTIALLY-FIXED

The classification and spectrum statements themselves are now properly
restricted to commuting coefficients: see the abstract (lines 177--184), the
introduction (lines 280--291), the Section 3 opening (lines 889--900), Theorems
3.1--3.3, and the explicit noncommuting problem at lines 2452--2462. The
missing converse is no longer silently assumed in those results.

The correction is nevertheless contradicted elsewhere:

- Proposition 3.6, lines 1166--1174, says **every** affine E677 model is medial.
  Its proof simply asserts `F=(G+G^3)^{-1}`, which is available only after
  assuming `FG=GF`. Direct expansion shows that an affine operation is medial
  iff `FG=GF`, so this proposition is equivalent to answering the explicitly
  open problem at lines 2452--2462.
- The same unqualified claim occurs in the introduction at lines 294--296 and
  in the mediality problem at lines 2516--2521.
- Lines 2500--2503 say the commuting even-order theorem excludes all affine
  models of orders 10, 12, and 14. That theorem excludes only **commuting** affine models, as its
  title and hypotheses say. A hypothetical noncommuting affine model is not
  covered.

The small matrix spot search performed in this review found no noncommuting
solution over `M_2(F_2)`, `M_2(F_3)`, `M_2(F_5)`, or `M_3(F_2)`, but a finite
sample is not the missing proof. Proposition 3.6 and its downstream prose must
be scoped to commuting coefficients unless commutation is proved.

#### J2 — FIX-INTRODUCED-NEW-ERROR

The original all-size extremum claim has been repaired well. Corollary
4.2(c), lines 1340--1350, claims exact maxima only for sizes 1, 2, and 3; it
labels the middle-size values as lower bounds and cites the new
`isoperim_check.py`. The script really does enumerate all 176 singletons, all
15,400 pairs, and all 893,200 triples, and it constructs and evaluates a
positive-excess witness for every size 2 through 174.

The new remark at lines 1354--1360 then goes beyond that evidence: it says the
old report's values "agree with the true maxima" for `s<=5` and `s>=174`,
"which we verified." The new script proves exactness only at `s=1,2,3` (and,
by complementation, the corresponding sizes 175, 174, 173). At `s=4,5` it
constructs witnesses of `+8,+12`; it neither enumerates all subsets nor gives
an upper-bound proof. The sentence should say that the values are reproduced
by the witness family, or supply the missing exact verifier/proof. The main
`+1152` correction and the route-closing sign claim remain valid.

#### J3 — FIXED

Lines 1690--1698 now separate discovery from verification: `term_search.py`
is accurately described as a deterministic 1,200-pair sampled search, and the
new `term_full_check.py` is cited for the all-111,600-pair statement. The new
script was rerun and checks every claimed forced pair.

#### J4 — FIXED

The support sizes, zero count, strong connectivity, diameter two, `Q`, and the
`F_pq` distribution now cite `struct_check.py` (lines 1308--1313 and
1378--1386), while the artefact table accurately says that `verify176.py`
does not compute them. Rerunning `struct_check.py` reproduced every stated
number.

There is one stale editorial sentence at lines 1319--1324: it says
`verify176.py` computes "all the counts quoted above," although `r_t=c_v=146`
and the zero count immediately precede it and are computed by
`struct_check.py`. The evidence is now present, so this is no longer J4's
substantive gap, but the verifier description should be narrowed to items
(a)--(e) and the off-diagonal distribution.

#### J5 — FIXED

Proposition 6.5 now says the transposition recipe was checked only at orders 5
and 11 and explicitly states that no general-order proof is available (lines
2273--2276). No universal extrapolation remains.

#### J6 — FIXED

Theorem 6.1 and lines 2158--2188 now credit the complete classification
through order 9 to F1's implementation alone. The exact smaller/weaker
coverage of F5, R2, and R3-B is stated separately, including that the R3-B run
checks existence/emptiness rather than the order-9 isomorphism count. The
summary correctly says the order-9 enumeration was performed once.

#### J7 — FIXED

Proposition 5.9 now has a proof marker and a self-contained proof of the
two-element-fibre reduction (lines 2006--2029). With a two-element fibre,
every row permutation has the form `t -> t+epsilon(s)`, and every function
`epsilon:F_2->F_2` is affine; the blueprint's affine-extension lemma then
applies when the base satisfies E255. This supplies the missing argument and
states the relevant base hypothesis.

### Editorial findings

#### E1 — PARTIALLY-FIXED

The convention now sensibly applies to numbered assertions, not to
definitions, problems, or the conjecture, and the two round-1 examples now
carry proof markers. One exception prevents the convention from being a fully
mechanical audit rule: Proposition 3.7 at lines 1184--1201 carries the custom
placeholder "markers are attached to the individual items," but items (a)
and (d) contain ordinary citations rather than any of the four defined status
markers. Either give the proposition one real status marker or mark all four
items consistently.

#### E2 — FIXED

The maps are now disjointly named: `T(t,v,x)` is the three-coordinate state
map, `tau(a,t)` is the two-coordinate transport, and `sw` is the coordinate
swap. No incompatible reuse of `T` remains.

#### E3 — FIXED

The multiplicity-matrix definition introduces `r_t` and `c_v` at lines
718--728, before their
first use in the order-176 theorem. The theorem now refers back to that
definition.

#### E4 — FIXED

The TI structure-theory claim consistently carries both the
translation-invariant and affine-fibre restrictions (notably lines
1407--1414 and the R5-C bibliography note). The general-table scope is
explicitly open.

#### E5 — FIXED

The least non-right-cancellative order is now bounded below by 10, not 8
(lines 2442--2447), exactly as the paper's own `n<=9` theorem permits.

#### E6 — PARTIALLY-FIXED

The duplicate hyperref object is gone: `compile_v2.log` contains no duplicate
anchor, unresolved-reference, or unresolved-citation warning. The typesetting
cleanup is incomplete. The log still contains four distinct overfull-box
sites (reported once per pass), including boxes approximately 42 pt and 69 pt
too wide near lines 1134--1150. This is editorial only and does not affect the
mathematics.

## Fresh-sweep findings

No new explicit counterexample to a corrected principal theorem was found.
The material fresh issues are already recorded above:

1. the unqualified affine-mediality proposition and the order-10/12/14 affine
   exclusion, under J1;
2. the unsupported exact-maxima statement for sizes 4 and 5, introduced by
   the J2 repair;
3. the stale `verify176.py` description under J4;
4. the remaining marker exception and overfull boxes under E1 and E6.

No repaired statement was found to have been weakened below a stronger result
that its cited source actually proves, aside from harmless choices to report
only the exact ranges independently supported in the repository.

## Spot-run verification record

The following changed claims were rerun against the current repository.

1. `R5C_scripts/isoperim_check.py`: exit 0. It reproduced exact maximum
   excesses `0,+2,+4` for sizes `1,2,3`; exhibited positive excess in every
   size class `2<=s<=174`; and reproduced the changed witnesses `+32` at
   `s=8`, `+1152` at `s=88`, and `+768` at `s=120`.
2. `R5C_scripts/struct_check.py`: exit 0. It reproduced
   `r_t=c_v=146`, 5,280 zeros, strong connectivity, diameter 2,
   `Q=115456`, `Q-n^2=84480`, and `|F_pq|=32` on exactly 2,640 ordered
   pairs (zero on the other 28,160).
3. `R5C_scripts/term_full_check.py`: exit 0. It rebuilt the order-496 model,
   found 111,600 forced ordered pairs, confirmed `N(t,v)=1` on all of them,
   and verified the displayed term witness on all 111,600.
4. A direct finite-matrix search of the noncommutative affine equations over
   `M_2(F_2)`, `M_2(F_3)`, `M_2(F_5)`, and `M_3(F_2)` found no
   noncommuting solution. This is only a spot check and is not used as a proof
   of Proposition 3.6.

The three new repository verifiers therefore repair the central numerical
evidence labels. The remaining defects are scope/proof and editorial defects,
not failures of those computations.

## Final verdict

**VALID-WITH-GAPS**
