VERDICT: GAP — MATHEMATICS defects were found: one mismatched import, plus uncheckable supplementary claims labelled PROVED; no stated target theorem was refuted by the independent computation.
TEXT VERSION REVIEWED: w61_S3_GFAN_r14

## Joint table

| Joint | Verdict | Justification |
|---|---|---|
| J-FAN4P | PASS | Independent degree sums give the asserted residue mass and C-values; the p-terms cancel. The formulas remain coherent when there are no escapes and when the high phase is empty. |
| J-FAN8P | PASS | Remaining high vertices, nonescaping C-vertices, and A′ recipients are disjoint. Prefix comparison is tie-safe. The positive-escape hypothesis supplies the escape step; at zero escapes the lemma asserts nothing. |
| J-FAN6P | PASS | Backward induction is valid: each block contains a positive number of largest A′ entries. The zero convention and the kill list agree, including the smallest single-part and boundary-gap cases. |
| J-GFAN2 | PASS | Independent simulation reproduced the uniform three tails and the complete short-layer list. Exactly the single-part rows hit the target step count, and FAN-6′ excludes both. |
| J-RIG1 | BOOKKEEPING | The tightness removal is real: CAP1 supplies L2(c). RIG supplies the configuration and numerical part of L2(d), but not literally its additional T-class assertions; “L2(d) directly” overstates the route. |
| J-CORHC | PASS | All three corollaries have correct arithmetic and dependencies. RIG’s own interval excludes the smallest layer. L1-short is unused in Appendix B. |
| J-FIN | MATHEMATICS | The three cases are disjoint and exhaustive, and the finite bounds are sound. But GFANν invokes MB1 without a hard-core hypothesis; its lower bound is already a theorem hypothesis, so deleting that citation repairs the proof. |
| J-SPEC | PASS | The five conventions determine a superset containing every realizable shape. Multiset reduction is legitimate, padding is inert for validity/step count, and omitting graphicality or p-feasibility filters is monotone in the required direction. |
| J-DATA | PASS | Independent generation reproduced every partition step count, boundary count, closed-form count, and every survivor. The generated positive-escape roster equals the printed roster in both directions. |
| J-KILL | PASS | Every generated survivor has a unique maximum with the required gap. The tight certificates with second entry two and with second entry one both satisfy the weak inequality exactly as used. |
| J-IMPORT | MATHEMATICS | All target-proof imports match except GFANν→MB1. Appendix C’s Favaron use matches, but the surrounding C1 claims themselves are not printed or proved. See the per-call table. |
| J-SCOPE | GAP | Target statement scopes otherwise match their proofs, and the excluded zero-nonedge range is genuinely necessary. The supplementary C1 claims labelled PROVED are neither Appendix A imports nor proved in place and remain unresolved. |

## J-IMPORT table

| Imported fact | Caller | Hypothesis match | Conclusion match | Verdict |
|---|---|---|---|---|
| Lemma 4 | RIG(b),(c) | RIG is in the hard-core frame, including maximum A and all frame conditions. | Only common A-neighbours of adjacent B-pairs are used. | MATCH |
| Observation R1 | RIG(d) | The frame supplies diameter four. | Used only to infer that B is not a clique and ν is positive. | MATCH |
| Proposition L2(a),(b) | RIG-1 | Caller is a hard core with the specified low-layer size. | Adjacency and B-universality are used; clause (b) alone already empties B_lo⁺. | MATCH |
| Corollary MB1 | RIG final bound | The final paragraph explicitly adds the reductio, hence is in the hard core; all low vertices are B-universal. | Used exactly for ν≤L−1 and the positive lower bound. | MATCH |
| Corollary MB1 | GFANν finiteness | GFANν assumes a GFan configuration and reductio, not the hard-core frame; MB1’s hard-core hypothesis is absent. | The lower bound used is exactly MB1’s conclusion but is independently an explicit theorem hypothesis. | MISMATCH |
| Theorem FAN | RIG-2 | Caller is in the hard core, has a Fan configuration, and explicitly assumes the required lower layer size. | Used only to eliminate the ν-one family. | MATCH |
| Theorem FAN | GFAN2-HC | RIG supplies a hard-core Fan instance; its interval forces the required lower layer size. | Used only to eliminate ν one. | MATCH |
| FAN-1, including its printed GFan extension | FAN-4′, FAN-8′, FAN-6′, GFAN2 | Each caller has GFan plus reductio; the extension verifies degree classes and tie-breaking. | Used only to identify the high-phase heads. | MATCH |
| DICH(b) | FAN-4′, FAN-8′, FAN-6′ | High heads have original degree at least τ+1 and reductio gives s=τ. | Exact earlier-block membership and deletion value are the conclusions used. | MATCH |
| Lemma TAIL | GFANν | Used only at zero escapes with nonempty λ; positivity follows from ν≥1, and the caller separately restricts to L≥λ₁. | Used exactly to replace the tail count by its λ-only criterion. | MATCH |
| Favaron–Mahéo–Saclé | Supplementary C1-C paragraph | A claimed graph realization would be a finite simple graph and supplies α≤k. | residue≤α would give residue≤k, the contradiction required by the stated reduction. | MATCH, CONDITIONAL |

Corollary L1-short is not used anywhere in Appendix B. Theorem MB and Theorem SL occur only behind the separately certified MB1/L2 imports, not as direct calls by a target proof.

## Defect list

### D1 — MATHEMATICS: GFANν calls MB1 outside MB1’s scope

Theorem GFANν lists Corollary MB1 among the four proved bounds that make its enumeration finite. MB1 is stated only “in the hard core.” GFANν assumes a `GFan(τ,L,ν)` configuration, the reductio, its ν range, and `L≥ν+1`; it does not assume connectedness, diameter four, the forest-number equality, non-forest, or the hard-core lower bound on τ. Thus the import’s supplied hypotheses do not match its required hypotheses. The briefing expressly classifies a mismatched import as MATHEMATICS.

This does not refute GFANν: the only imported conclusion used there, `L≥ν+1`, is already an explicit hypothesis of GFANν. Delete “Corollary MB1” from the four-bound sentence and say “the theorem hypothesis `L≥ν+1`”; the split, enumeration, and elimination then remain valid. I found no counterexample to the stated theorem.

### D2 — MATHEMATICS: supplementary claims labelled PROVED are unavailable

The “Progress” paragraph asserts Lemma C1-A, Proposition C1-B, Corollary C1-C, and Theorem C1-2 as proved mathematical results. None is stated in Appendix A.1 or proved in place. Their alleged “certified toolkit” is not supplied, and the review restriction forbids consulting author files that might contain it. The paragraph also reports a larger verification without a complete generation specification for that run.

These claims are not dependencies of GFANν for the stated finite range, so the target theorem does not inherit this gap. They remain affirmative statements inside the reviewed file, however, and the brief says every such statement is under review. Printing their full statements and proofs—or moving them outside the reviewed assertions and marking them unverified context—would settle the gap.

### D3 — BOOKKEEPING: RIG-1 overstates what RIG supplies

RIG-1 says Theorem RIG gives Proposition L2(c) and L2(d) “directly.” RIG does give L2(c), `ν=m̄≥1`, and—after its hard-core bound—`ν=m̄=1`, which is all RIG-1 needs to identify `Fan(τ,2)`. But L2(d) as printed also identifies `T₁={u}`, `T₂={v}` and gives lower bounds on the two endpoints’ A-degrees. Those assertions are not conclusions of RIG.

The advertised removal of the tightness argument is still genuine: CAP1 proves L2(c) without it, and the corollary’s Fan conclusion is sound. Replace “L2(c) and (d) directly” by “L2(c) and the configuration/numerical part of L2(d)” (or separately re-add the type argument).

## Refutation log

The checker was written from Appendix A.0/C.1 and reads no repository input. The complete archived stdout is [w61_S3_GFAN_r14_check.out]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_GFAN_r14_check.out); the source is [w61_S3_GFAN_r14_check.py]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_GFAN_r14_check.py). The archive is byte-for-byte the checker’s stdout.

Calibration was printed before any enumeration:

```text
CALIBRATION (printed before all review enumeration)
  residue(K2) got=1 expected=1 pass=True
  residue(C3) got=1 expected=1 pass=True
  residue(C4) got=2 expected=2 pass=True
  residue(C5) got=2 expected=2 pass=True
  residue(C6) got=2 expected=2 pass=True
  residue(C7) got=3 expected=3 pass=True
  residue(C8) got=3 expected=3 pass=True
  residue(C9) got=3 expected=3 pass=True
CALIBRATION PASS
```

### Part 2 refutation attempt first

I regenerated integer partitions, escape partitions, C-parts, and A′ residues directly. For each shape I ran head-deletion until zero or invalidity, retained exact-step rows, and only then applied FAN-6′. I did not seed the generator with any printed totals or survivors.

Raw summary:

```text
  nu=1 s0_rows=2 values=2:2 | 1+1:2
    boundary_pairs=0 survivors=none
    Epositive tested=0 closed_form=0 terms=[] per_E={}
    Epositive survivors=0 un-killed=0
  nu=2 s0_rows=5 values=4:4 | 3+1:4 | 2+2:3 | 2+1+1:3 | 1+1+1+1:3
    boundary_pairs=1 survivors=L3/lambda=4
    Epositive tested=3 closed_form=3 terms=[3] per_E={1: 3}
    Epositive survivors=1 un-killed=0
  nu=3 s0_rows=11 values=6:6 | 5+1:6 | 4+2:5 | 4+1+1:5 | 3+3:4 | 3+2+1:4 | 3+1+1+1:5 | 2+2+2:4 | 2+2+1+1:4 | 2+1+1+1+1:4 | 1+1+1+1+1+1:4
    boundary_pairs=3 survivors=L5/lambda=6
    Epositive tested=24 closed_form=24 terms=[14, 10] per_E={1: 14, 2: 10}
    Epositive survivors=4 un-killed=0
  nu=4 s0_rows=22 values=8:8 | 7+1:8 | 6+2:7 | 6+1+1:7 | 5+3:6 | 5+2+1:6 | 5+1+1+1:7 | 4+4:5 | 4+3+1:5 | 4+2+2:6 | 4+2+1+1:6 | 4+1+1+1+1:6 | 3+3+2:5 | 3+3+1+1:5 | 3+2+2+1:5 | 3+2+1+1+1:5 | 3+1+1+1+1+1:6 | 2+2+2+2:4 | 2+2+2+1+1:5 | 2+2+1+1+1+1:5 | 2+1+1+1+1+1+1:5 | 1+1+1+1+1+1+1+1:5
    boundary_pairs=7 survivors=L7/lambda=8, L5/lambda=7+1
    Epositive tested=110 closed_form=110 terms=[45, 44, 21] per_E={1: 45, 2: 44, 3: 21}
    Epositive survivors=9 un-killed=0
  nu=5 s0_rows=42
    boundary_pairs=14 survivors=L9/lambda=10, L7/lambda=9+1
    Epositive tested=397 closed_form=397 terms=[120, 132, 90, 55] per_E={1: 120, 2: 132, 3: 90, 4: 55}
    Epositive survivors=20 un-killed=0
  nu=6 s0_rows=77
    boundary_pairs=26 survivors=L11/lambda=12, L9/lambda=11+1, L7/lambda=10+1+1
    Epositive tested=1211 closed_form=1211 terms=[280, 336, 270, 220, 105] per_E={1: 280, 2: 336, 3: 270, 4: 220, 5: 105}
    Epositive survivors=38 un-killed=0
  TOTAL Epositive tested=1745 survivors=72 un-killed=0
```

The full stdout prints every `s₀` value and every positive-escape survivor. A row-by-row comparison after generation found no missing printed survivor and no extra/invalid printed survivor. Boundary survivor totals are respectively absent, one, one, two, two, and three; all are FAN-6′-killed. The derived closed form is

`S(ν)=Σ_{E=1}^{ν−1}(ν−E)p(E)p(2ν−E)`.

Its terms arise independently from the number of allowed layer sizes, all partitions of the escape mass (the part-count bound is vacuous because `L+1>E`), and all partitions of the A′ mass.

### GFAN2 refutation attempt

The three uniform tails were run at several layer sizes; each missed the target by the asserted amount. The short-layer list was generated as all partitions for the two permitted escape totals, not copied as eight rows.

```text
  complete L=3 rows
    E=0 e=empty lambda=4 valid=True steps=3 target=3 FAN6=True
    E=0 e=empty lambda=3+1 valid=True steps=4 target=3 FAN6=True
    E=0 e=empty lambda=2+2 valid=True steps=4 target=3 FAN6=False
    E=0 e=empty lambda=2+1+1 valid=True steps=4 target=3 FAN6=False
    E=0 e=empty lambda=1+1+1+1 valid=True steps=5 target=3 FAN6=False
    E=1 e=1 lambda=3 valid=True steps=3 target=3 FAN6=True
    E=1 e=1 lambda=2+1 valid=True steps=4 target=3 FAN6=False
    E=1 e=1 lambda=1+1+1 valid=True steps=4 target=3 FAN6=False
  generated_rows=8 exact-step_survivors=2 un-killed=0
```

No GFAN2 or GFANν finite shape cleared in the target number of steps without also satisfying FAN-6′’s forbidden-gap hypothesis.

### Construction attempts and boundary quantifiers

The lower bound on ν is necessary. The complete graph below is literally `GFan(4,4,0)`, has residue equal to alpha, and satisfies `L≥ν+1`; it would refute GFANν if zero were admitted. Its class checks are printed in definition order in the control section.

For GFAN2’s excluded layer sizes, I searched the concrete box `p=3`, exactly two high-part nonedges, and three or four A′ vertices, exhaustively testing maximum independence and residue. No instance was found after 8,232 candidates for either layer size. This is not a proof outside the theorem’s range.

For the empty A′ residue boundary, `[L]^(L+1)` clears in exactly `L` steps. In the theorem’s positive-escape branch an empty residue would require `E=2ν`, whereas the escape inequality with positive `L` excludes it. A single positive part is killed exactly from weight two upward; weight one is correctly outside FAN-6′.

## Mandatory control section

### 1–2. Counterfactual availability and witness validation in class order

This graph satisfies the entire hard-core frame and the literal `GFan(6,3,2)` configuration but deliberately violates the reductio. Thus FAN-4′, FAN-8′, FAN-6′, and all enumeration conclusions requiring `s=τ` are unavailable on it; the reductio is load-bearing.

```text
vertices=['a0', 'x1', 'x2', 'x3', 'x4', 'b0', 'b1', 'b2', 'h0', 'h1', 'h2']
edges=[('a0', 'b0'), ('a0', 'b1'), ('a0', 'b2'), ('a0', 'h0'), ('a0', 'h1'), ('a0', 'h2'), ('x1', 'h0'), ('x1', 'h1'), ('x1', 'h2'), ('x2', 'h0'), ('x2', 'h2'), ('x3', 'h0'), ('x4', 'h1'), ('b0', 'b1'), ('b0', 'b2'), ('b0', 'h0'), ('b0', 'h1'), ('b0', 'h2'), ('b1', 'b2'), ('b1', 'h0'), ('b1', 'h1'), ('b1', 'h2'), ('b2', 'h0'), ('b2', 'h1'), ('b2', 'h2'), ('h1', 'h2')]
connected=True
A=['a0', 'x1', 'x2', 'x3', 'x4'] independent=True maximum_by_exhaustive_enumeration=True alpha=5 one_maximum=['a0', 'x1', 'x2', 'x3', 'x4']
diameter=4
forest_number=6 f_eq_alpha_plus_1=True
nonforest=True
degrees=[6, 3, 2, 1, 1, 6, 6, 6, 7, 7, 7] HH_valid=True HH_steps=8 residue=3 residue_eq_alpha=False
GFan_check={'tau': 6, 'L': 3, 'nu': 2, 'low_universal': True, 'low_degA_1': True, 'common_a0_allB': True, 'nonedges_inside_high': True, 'high_condition': True, 'low_condition': True, 'no_Aprime_low': True, 'all': True}
```

The quantifier-boundary witness `K5=GFan(4,4,0)` was checked in the same order:

```text
vertices=['a0', 'b0', 'b1', 'b2', 'b3']
edges=[('a0', 'b0'), ('a0', 'b1'), ('a0', 'b2'), ('a0', 'b3'), ('b0', 'b1'), ('b0', 'b2'), ('b0', 'b3'), ('b1', 'b2'), ('b1', 'b3'), ('b2', 'b3')]
connected=True
A=['a0'] independent=True maximum_by_exhaustive_enumeration=True alpha=1 one_maximum=['a0']
diameter=1
forest_number=2 f_eq_alpha_plus_1=True
nonforest=True
degrees=[4, 4, 4, 4, 4] HH_valid=True HH_steps=4 residue=1 residue_eq_alpha=True
GFan_check={'tau': 4, 'L': 4, 'nu': 0, 'low_universal': True, 'low_degA_1': True, 'common_a0_allB': True, 'nonedges_inside_high': True, 'high_condition': True, 'low_condition': True, 'no_Aprime_low': True, 'all': True}
```

The latter is not a hard-core-frame witness because its diameter is one; it is solely a counterexample to extending GFANν’s literal quantifier to zero.

### 3. Vacuity honesty

I did not construct a graph satisfying all hypotheses of GFAN2 or GFANν; the explicit frame witness above intentionally fails `residue=alpha`. Therefore the absence of a graph counterexample in my limited construction boxes is not positive evidence.

The theorem checks instead attack the ingredients: the proofs map any hypothetical graph to a listed value-multiset shape, my enumeration is a superset of all such shapes, every exact-step shape was independently regenerated, and FAN-6′ eliminates each. That is evidence for the finite implication, not evidence that the composite graph class is nonempty.

### 4. Independent specification controls

```text
SPECIFICATION CONTROLS
  TAIL direct_pairs=1817 mismatches=0
  zero-padding base_lists=2709 paddings=7 pairs=18963 mismatches=0
```

The multiset/unlabelled reduction follows directly from sorting after every deletion. No graphicality filter was used; because the checked set is a superset, any such filter can only delete rows. Escape-part feasibility restrictions involving `p` likewise can only delete generated rows.

## What I could not check

- I could not check the proofs or even complete formal statements of C1-A, C1-B, C1-C, or C1-2. They are absent from Appendix A.1 and Appendix C and their referenced toolkit is unavailable under the read restriction.
- I could not authenticate the historical claims that the author ran two independent enumeration passes or the larger auxiliary C1 verification. I independently reproduced the finite target data, TAIL comparison, and padding control, but not the provenance of prior runs.
- I did not settle a hypothetical `E=0` extension of FAN-8′. Its proof needs an actual escape step, and the stated lemma deliberately makes no zero-escape claim.
- The searches outside GFAN2’s stated `L≥3` range were limited to the printed construction box (`p=3` and three or four A′ vertices). No instance was found, but wider boxes were not exhausted and no general claim is made.
- The dispatch-file historical quotation and the unsupplied companion-section witness were not checked. Neither is used to prove a target statement.

