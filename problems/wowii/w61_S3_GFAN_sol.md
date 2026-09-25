VERDICT: REFUTED — a MATHEMATICS defect was found: literal Theorem GFANν includes ν = 0, and `K5` is an explicit counterexample.

TEXT VERSION REVIEWED: w61_S3_GFAN_sol (Q33)

## Joint verdicts

| Joint | Verdict | Result |
|---|---|---|
| **J-CAP** | **PARTIAL** | The inequalities are correct, including at `n_b=0` and `n_b=tau-1`. The lower bound needs only that `A` is maximal independent, not maximum; this is an over-hypothesis/bookkeeping issue. The upper bound uses only `b in B_lo` and the definitions. No frame or reductio hypothesis is used. |
| **J-RIG** | **CLEAN** for the stated frame theorem | Clauses (a)–(e) follow in order. `diam=4` enters only through Observation R1 to obtain `nu>=1`; placement of the non-edges uses B-universality. Lemma 4 is used exactly for adjacent pairs in `B`. The trailing `nu<=L-1` is correctly separated from the frame conclusions and attributed to Corollary MB1 in the hard core. An independently found frame graph satisfies all five conclusions. |
| **J-RIG-EQ** | **CLEAN** | Given the Appendix A definition, the word “exactly” is justified: the hypothesis supplies nonempty `B_lo`; (a)–(c), (d), and (e) are the substantive `GFan` clauses; “all `B_hi` is high” is definitional. The asserted converse adds no graph property. |
| **J-RIG12** | **GAP** in one import, otherwise clean | RIG-2's chain is earned: RIG gives `1<=nu<=L-1`, Theorem FAN removes `nu=1`, so `2<=nu<=L-1`; this makes `L=2` empty and leaves only `nu=2` at `L=3`. RIG-1's new CAP/RIG route does avoid the quoted tightness re-run. I could not verify that Proposition L2(a),(b) have exactly the claimed conclusion because their statements are not supplied. |
| **J-FAN4P** | **GAP** in imports; algebra clean | The degree sum and recipient bookkeeping recompute to `dec_A' = R-2nu+E`, hence terminal `A'` mass `2nu-E`; each `C` entry is `L+e_c`. The `p` terms cancel exactly. The uses of FAN-1 and DICH(b) cannot be import-checked from the supplied text because their statements are absent. |
| **J-FAN8P** | **GAP** in imports; argument clean conditional on them | Remaining high vertices and nonescaping `C` vertices are disjoint (`B_hi` versus `C`) and, assuming DICH(b)/the escape definition, lie in the block. Prefix comparison is tie-safe: an in-prefix `x` has value at least an escaping out-of-prefix `c`. The inequality gives `L<=2nu-E`. At `E=0` the lemma says nothing. FAN-1/DICH(b) import matching is not checkable from the supplied text. |
| **J-FAN6P** | **GAP** in imports; induction clean conditional on them | The multiplicity split `a_j<mu` versus `a_j>=mu` is valid, and the unique-top/gap property propagates back to an impossible `A'` degree above `p`. Zero entries are treated consistently: a one-positive-part residue has second entry zero, so `[w]` is killed exactly for `w>=2`; `[1]` is not. The listed smallest examples and nonexamples are correct. Again, FAN-1/DICH(b) import matching is unavailable. |
| **J-GFAN2** | **GAP** only because of the preceding import gap; finite analysis clean | The independent simulator reproduces the escape budget, all three displayed `L>=4` trajectories, and all eight `L=3` rows. The row list is complete. The only exact-`L` shapes are the stated single-part residues, all satisfying FAN-6′. No computational refutation was found. |
| **J-CORHC** | **PARTIAL** | All three corollaries' arithmetic is correct. GFAN2-HC's citation of “Corollary L1-short” is neither supplied nor needed: RIG already gives `1<=nu<=L-1`, excluding `L=1`. GFAN2-L3 and GFANν-HC follow. The latter only uses the valid positive-`nu` portion of GFANν, so the `nu=0` counterexample does not refute the hard-core corollary. |
| **J-FIN** | **CLEAN** for `1<=nu<=6` | The split is disjoint and exhaustive for positive `nu`: `E=0,L>=lambda_1`; `E=0,nu+1<=L<lambda_1`; and `E>=1`. Since `lambda` partitions `2nu`, `lambda_1<=2nu`. Combining `nu+1<=L<=2nu-E` gives `E<=nu-1`. FAN-4′, FAN-8′, MB1, and TAIL have the conclusions used. The proof omits the separate `nu=0` case even though the theorem statement includes it. |
| **J-SPEC** | **CLEAN** | The five conventions determine the multiset superset exactly. Havel–Hakimi depends only on the multiset, so unlabelled partitions are legitimate. Zero padding is inert (independently tested). Omitting graphicality is valid because the enumeration is a superset elimination; filtering could only remove rows. Invalid runs are rejected in the correct direction. |
| **J-DATA** | **CLEAN** | Every `s0(lambda)` for all 159 partitions was recomputed. Partition counts, boundary-pair counts, `S(nu)`, survivor counts, boundary survivors, and the full 72-row `E>=1` roster agree with the printed data. There is no missing printed survivor and no spurious printed survivor. |
| **J-KILL** | **CLEAN** | Every tail, boundary, and `E>=1` survivor has a unique maximum with second entry at most two below it. The boundary certificates `(4,2)` and `(3,1)` pass with equality. No survivor escapes FAN-6′. |
| **J-SCOPE** | **REFUTED** | Theorem GFANν is false as written because it says `nu<=6`, not `1<=nu<=6`, and does not impose the frame that would force `nu>=1`. `K5` supplies `GFan(4,4,0)` with `residue=alpha=1`. Also, RIG's scope gloss “Lemma 4, i.e. `f=alpha+1`” is not licensed by the supplied import, which states Lemma 4 only in the frame. Other scope findings are recorded below. |

## Defects

1. **MATHEMATICS — Theorem GFANν is false under its literal quantifiers.**

   The statement quantifies over “every `nu<=6`” and `L>=nu+1`. Since `nu` counts non-edges, `nu=0` is a legitimate value. Let `G=K5`, take `A={a0}`, and `B={b0,b1,b2,b3}`. Then `tau=4`, every `b` has degree `4=tau`, so `B_lo=B`, `L=4`, and every low vertex is B-universal with its unique A-neighbour `a0`. The vertex `a0` is adjacent to all of `B`; `A'` is empty; `B_hi` is empty; and all zero non-edges of `B` lie inside `B_hi` vacuously. Thus this is exactly `GFan(4,4,0)`. Its degree sequence is `[4,4,4,4,4]`, whose Havel–Hakimi residue is `1=alpha`. Finally, `0<=6` and `4>=0+1`. This contradicts the theorem.

   A minimal repair is to state **`1<=nu<=6`**. Alternatively, adding the hard-core frame hypothesis would invoke Observation R1 and force `nu>=1`, but that is a stronger repair than the proof's positive-`nu` enumeration appears to need. The hard-core corollary remains intact because RIG already supplies `nu>=1` there.

2. **MATHEMATICS — the reduced-scope gloss for RIG is not supported by the supplied Lemma 4 import.**

   The scope paragraph says that (a)–(c),(e) need maximum independence “plus Lemma 4, i.e. `f=alpha+1`.” The supplied certified statement is only: “in the frame, any two adjacent vertices of `B` have a common A-neighbour.” Nothing supplied establishes that `f=alpha+1` alone implies this adjacency property after connectedness, non-forest, or other frame conditions are removed. The theorem itself is safely stated in the frame, so its proof is unaffected; the defect is the affirmative reduced-hypothesis statement. To certify that sentence, supply the actual more general statement of Lemma 4 or retain the full frame hypotheses.

3. **BOOKKEEPING — Lemma CAP is over-hypothesized.**

   The proof of `deg_A(b)>=1` uses maximality, not maximum cardinality: if `b` has no A-neighbour, `A union {b}` is independent. The upper bound does not use maximality at all. The stated lemma remains true, but “only that `A` is maximum” is not the minimal scope requested in the audit.

4. **BOOKKEEPING — GFAN2-HC cites an unavailable and redundant `L=1` result.**

   “`L=1` is Corollary L1-short” cannot be checked from the supplied text. It is unnecessary because Theorem RIG already yields `1<=nu<=L-1` on this layer, immediately giving `L>=2`.

## Refutation log

The checker is [w61_S3_GFAN_sol_check.py]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_GFAN_sol_check.py). Its complete unedited stdout is archived at [w61_S3_GFAN_sol_check.out]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_GFAN_sol_check.out). No archived author script or restricted file was read or reused.

### Calibration first

The very first stdout block is the required calibration. It gives residue `1` for `K2` and `ceil(n/3)` for every cycle `C_n`, `3<=n<=9`, with all checks passing. No theorem-search number is printed before this block.

```text
=== CALIBRATION (printed before all review numbers) ===
K2 residue: computed=1 expected=1 pass=True
C3 residue: computed=1 expected=ceil(3/3)=1 pass=True
...
C9 residue: computed=3 expected=ceil(9/3)=3 pass=True
CALIBRATION PASS=True
```

### Refute-first search for GFANν

I generated partitions recursively and independently enumerated every allowed `(nu,L,E,e,lambda)` shape. Only after generation did the checker compare its counts with the printed ones. For `nu=1,...,6`, respectively, it found:

- partition counts: `2,5,11,22,42,77`;
- boundary pair counts: `0,1,3,7,14,26`;
- `E>=1` shape counts: `0,3,24,110,397,1211`;
- `E>=1` survivor counts: `0,1,4,9,20,38`.

The full recomputed `s0` table is in raw stdout. In each positive-`nu` tail range the only survivor is `[2nu]`. The independently generated boundary survivors and all 72 positive-escape survivors match the printed roster entry for entry (order is immaterial). Every survivor is killed by the independently evaluated FAN-6′ predicate; none has a nonunique top or a top gap below two.

The closed form was also independently recovered from the loops: for fixed `E`, there are `nu-E` choices of `L`, `p(E)` escape multisets (the length cap is inactive because `L+1>E`), and `p(2nu-E)` residues. Hence

`S(nu) = sum_{E=1}^{nu-1} (nu-E) p(E) p(2nu-E)`.

The tail formula was compared with direct simulation on 1,817 generated pairs and had zero mismatches. Zero padding was tested on 480 base lists with `0,1,2,3,4,8` appended zeros and had zero mismatches.

This positive-`nu` search did not refute the intended theorem. The refutation instead arose from the omitted `nu=0` scope, which the positive-partition generator correctly does not cover.

### Refute-first search for GFAN2

Direct simulation reproduces the complete eight-row `L=3` table. Exactly two rows clear in three steps: `(E=0,lambda=[4])` and `(E=1,e=[1],lambda=[3])`; both have FAN-6′ certificates. For every tested `L>=4`, the exact-`L` tail shape is only `lambda=[4]`, again killed. Lemma TAIL makes this latter conclusion uniform beyond the direct test range. The three displayed nonsingleton trajectories have the claimed lengths. No GFAN2 counterexample shape survived.

### Construction attack on RIG

The checker searched a constrained family rather than assuming RIG's conclusion. It found the following frame graph:

```text
A = {a0,a1,a2,a3}
B = {b0,b1,b2,b3}
E = {a0-b0,a0-b1,a0-b2,a0-b3,
     a1-b1,a2-b2,a3-b1,a3-b2,
     b0-b1,b0-b2,b0-b3,b1-b3,b2-b3}.
```

Exhaustive subset enumeration gives `alpha=4` with the displayed `A`, `diam=4`, and forest number `5=alpha+1`; the graph is connected and non-forest. Here `B_lo={b0,b3}`, both low vertices are B-universal, `B_hi={b1,b2}`, and the only `B` non-edge is `b1-b2`. All five RIG conclusions are true. Its degree-sequence residue is `3`, not `alpha=4`, so it is a frame witness rather than a hard-core witness; this is also a useful reductio-availability control.

### Explicit refutation of literal GFANν

The relevant raw checker excerpt is:

```text
=== LITERAL nu=0 COUNTEREXAMPLE TO THEOREM GFANnu ===
graph: K5
1 connected: True
2 A maximum by exhaustive subset enumeration: True ... alpha= 1
3 diameter: 1 equals4= False
4 forest number: 2 alpha+1= 2 ... pass= True
5 non-forest: True
6 residue-vs-alpha: 1 1 equal(reductio)= True degree-sequence= [4, 4, 4, 4, 4]
parameters: tau= 4 L= 4 nu= 0 ...
GFan clauses: ... all-pass= True
literal theorem range nu<=6 and L>=nu+1: True
COUNTEREXAMPLE PASS= True
```

This witness is printed in full in raw stdout, including its ten edges and every `GFan` clause.

## Mandatory controls

### 1. Counterfactual availability

Two controls show that the standing hypotheses are load-bearing.

First, the RIG construction above satisfies the full hard-core frame and all `GFan` structural conclusions but has `residue=3<alpha=4`. Therefore FAN-4′, FAN-8′, FAN-6′, and the hard-core MB1 conclusion are unavailable on it: each requires the reductio/hard core, which this graph fails. The graph is not presented as evidence for those lemmas.

Second, the checker prints a deliberately malformed tail-shaped list with `nu=2,L=3,E=1,e=[1],lambda=[2]`. Its `lambda` mass is `2`, whereas FAN-4′ requires `2nu-E=3`. The Havel–Hakimi run is invalid and the shape is outside FAN-4′; consequently the reductio-derived FAN-8′ and FAN-6′ machinery is not invoked on it. This confirms that the residue-mass identity is not decorative.

Finally, `K5` satisfies connectedness, `A` maximum, `f=alpha+1`, non-forest, the reductio, `tau>=4`, and all literal `GFan(4,4,0)` clauses, but has diameter one. Observation R1 is unavailable, so `nu>=1` cannot be inferred. This pinpoints the omitted frame/lower-bound hypothesis behind the refutation.

### 2. Witness validation in class-definition order

Both named graph witnesses were checked and printed in the mandated order: connected; `A` maximum by exhaustive enumeration of all vertex subsets; diameter; forest number by exhaustive enumeration; non-forest; then Havel–Hakimi residue versus `alpha`. The RIG construction passes the frame predicates and fails only the reductio. `K5` passes every literal GFANν hypothesis and the reductio but fails `diam=4`, which the literal theorem does not state.

### 3. Vacuity honesty

The positive-`nu` GFAN2/GFANν computation enumerates necessary tail **shapes**, not realized graphs. I did not find or enumerate a graph satisfying every full composite hypothesis for positive `nu`; therefore the absence of an un-killed shape is not presented as empirical positive evidence that such graphs do not exist. It is only a verification of the stated superset-elimination argument, conditional on the imported structural lemmas. The ingredients were attacked separately by full multiset enumeration, tail testing, zero-inertness testing, and a genuine frame construction.

The RIG construction box was nonvacuous: it produced a graph satisfying the full frame hypotheses. The literal GFANν scope was also nonvacuous: `K5` is a full counterexample to the written statement.

### 4. Scope audit

- CAP: maximum independence is sufficient but stronger than necessary; maximality suffices for the lower bound, and the upper bound is purely definitional.
- RIG: the stated frame supplies all proof hypotheses. Only `nu>=1` uses diameter. Only the final `nu<=L-1` uses the reductio/hard core. The attempted reduction of the remaining hypotheses to `f=alpha+1` alone is not certified by the supplied form of Lemma 4.
- RIG-1/RIG-2: both are filed in the hard core, which is sufficient. RIG-1's precise Proposition L2 import is unavailable. RIG-2 uses no hidden extra condition.
- FAN-4′/8′/6′: all are stated under `GFan` plus reductio, which is what their users supply. Their internal counting also uses FAN-1 and DICH(b), whose exact scopes are absent from the brief.
- GFAN2: `nu=2` and `L>=3` avoid the zero case. Its proof is scope-valid conditional on FAN-1/DICH(b) having exactly the needed `GFan`+reductio hypotheses.
- TAIL: this is a pure multiset statement. Nonempty `lambda` and `L>=lambda_1` are explicitly stated and used.
- GFANν: under-hypothesized/over-quantified at `nu=0`; the proof and data cover only `nu=1,...,6`.
- GFAN2-HC: true; its L1-short citation is redundant. GFAN2-L3 and GFANν-HC have the hard-core hypotheses needed, and GFANν-HC supplies positive `nu` through RIG.
- Appendix C's data and conventions are proof support, not extra graph hypotheses. The no-graphicality choice enlarges the search box and is safe.
- The two all-`nu` statements C1 and C2 are explicitly labelled conjectures and are not used as proved facts.

## What I could not check

1. **FAN-1 and DICH(b) import matching.** Their statements and hypotheses are not in the supplied text, although FAN-4′, FAN-8′, FAN-6′, and GFAN2 use them. I verified every downstream calculation conditional on the properties quoted in the proofs, but I cannot verify that those properties are available under exactly `GFan` plus reductio. Settling this requires the certified statements of FAN-1 and DICH(b), not their proofs.

2. **Proposition L2(a),(b) import matching in RIG-1.** Proposition L2 is named as certified, but its clauses are not stated. I cannot independently confirm that (a),(b) force `B_lo^+=empty`. Supplying those clauses would settle the joint.

3. **The “L1-short” citation.** No such statement is supplied. It is harmless here because it is redundant, but its citation cannot be checked.

4. **The claimed reduced form of Lemma 4.** Only the frame version is supplied, so I could not determine whether the author has a separately certified theorem assuming merely maximum independence and `f=alpha+1`. The current brief does not license that reduction.

5. **Graph realizability of positive-`nu` tail shapes.** I deliberately did not treat a degree-list simulation as a graph construction. Realizability is unnecessary for the superset elimination, but it means the computational search itself supplies no full positive-`nu` graph witness. This is the vacuity limitation stated above.

Per the hard read restriction, I did not inspect any author notes, previous review, archived enumeration, restricted prompt, orchestration file, or web source. No conclusion above relies on such material.
