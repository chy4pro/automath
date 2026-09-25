EXECUTION ENVIRONMENT: I ran code. Python 3.9 with NetworkX 3.2.1.
Corollary GFANν-HC: GAP
VERDICT: GAP — MATHEMATICS defects were found in the required N4 scope claim and in two omissions from the target's guard bracket; no counterexample to Corollary GFANν-HC itself was found.
TEXT VERSION REVIEWED: w61_S3_GFAN_r26

## 0. HELD-OUT CHECKS

Calibration was printed before every Section 0 value:

```text
K2: 1/1 PASS
C3..C9: 1/1, 2/2, 2/2, 2/2, 3/3, 3/3, 3/3 — all PASS
CALIBRATION_STATUS=PASS
```

| row | result | derivation (at most two lines) |
|---|---|---|
| H1 | `[12,6,4]:14`; `[9,7,3,3]:12`; `[14,5,2,1]:16`; `[8,8,6]:10`. All are valid step sequences. | Direct HH head lists have respectively 14, 12, 16, 10 entries; the complete lists are in the raw stdout. |
| H2 | `S(11)=98,384` | Terms for `E=1..10`: `7920+11286+11760+13475+12474+12705+10560+8910+6060+3234`. |
| H3 | `791`; per-`E`: `{1:6,2:14,3:21,4:35,5:47,6:85,7:110,8:155,9:170,10:148}` | Exhaustively ran all `98,384` C.1 shapes. Every one of the 791 survivors also has a FAN-6′ certificate. |
| H4 | `131` | Generated all `p(22)=1002` partitions and directly counted those for which `steps([λ₁]^(λ₁+1)+λ)=13`. |
| H5 | **NO; actual step count `16`.** | Built list `[15,14,13^12,5,4,4,3,3]`; heads were `15,13,11,10,9,8,7,6,5,4,4,3,2,2,2,1`. |

## 1. Joint table

| joint | verdict | justification |
|---|---|---|
| J-FAN4P | CLEAN | Degree sums give `pτ−2ν+R`; recipient accounting gives `R−2ν+E` decrements and residue `2ν−E`. At `E=0` the formula remains active. At `p=0`, a genuine configuration forces `ν=E=0`. |
| J-FAN8P | CLEAN | Remaining-high and nonescaping-C sets are disjoint block subsets. Prefix comparison is tie-safe. `E≥1` is load-bearing: without an escape step the proof starts nowhere and no `L≤2ν` conclusion follows. |
| J-FAN6P | CLEAN | DICH(b), block-prefix selection, and backward uniqueness/gap propagation match. Zero convention is explicit and applied consistently. Smallest killed residues `[2]`, `[3,1]`, `[4,2]` satisfy the certificate; listed nonexamples do not. |
| J-GFAN2 | CLEAN | Regenerated all eight `L=3` rows. For `L≥4`, the three surviving partition types take `L+1,L+1,L+2` steps. The escape bound makes the case split exhaustive. |
| J-RIG1 | PARTIAL | Clause L2(b) alone gives `B_lo+=∅`; citing (a) too is redundant bookkeeping. RIG then supplies (c), the configuration, and `ν=m̄=1` without the tightness re-run. |
| J-CORHC | CLEAN | Both corollary arithmetics check. RIG's `1≤ν≤L−1` excludes `L=1`; L1-short is unused in Appendix B. GFAN2-L3 is the direct contrapositive of GFAN2-HC's `L≥4`. |
| J-FIN | CLEAN | The three cases are disjoint/exhaustive; `λ₁≤2ν`, and `E≤ν−1` follows from the two L-bounds. `ν≥1` is necessary: `K3` realizes `GFan(2,2,0)` with residue=alpha. |
| J-SPEC | CLEAN | The multiset reduction preserves HH trajectories; padding was inert on 80,655 generated lists. Omitting feasibility/graphicality filters enlarges the search, which is the safe direction. All actual FAN-4′ shapes are included. |
| J-DATA | CLEAN | Independently regenerated all rows. All 159 printed `s0` values, all 982 positive-E survivors, and all 25 boundary survivors matched both directions. Counts and closed form also matched. |
| J-KILL | CLEAN | Every generated survivor for `ν≤10` had a unique top with the required gap; zero misses. Explicit `(4,2)` and `(3,1)` boundary certificates were included in checks. |
| J-IMPORT | GAP | Ordinary interfaces match, but N4 invokes MB/MB1 below their printed `τ≥4` scope without a supplied weakening proof. This is an import-interface gap in Appendix B's broadened RIG sentence. |
| J-SCOPE | GAP | At interface level the target does not consume `τ≥4`; however N4 does not prove the broadened RIG bound without it. In the actual hard-core target, `τ≥4` is available, so the target implication remains supported. |
| J-NEWTEXT | GAP | N1–N3 are true, needed, and effective. N4's `τ≥2` weakening of Theorem MB is not supplied by this file; the printed MB statement requires the hard core, hence `τ≥4`. |
| J-AZGUARD | GAP | The bracket counts the correct four imports, but omits RIG's universal-low hypothesis and GFANν's residue-equality guard from its claimed complete roll call. Both are actually supplied by the corollary. |

## 2. J-IMPORT table

| Appendix A.1 fact actually used | caller(s) | hypothesis and conclusion match (≤30 words) |
|---|---|---|
| Lemma 4 | RIG | Frame is supplied; adjacent B-pairs are supplied. Only a common A-neighbour is used. Match. |
| Observation R1 | RIG, GFAN2-HC, GFANν-HC | Frame/diameter four is supplied. `B` nonclique and `ν≥1` are exactly the used conclusions. Match. |
| Lemma DICH | FAN-1 extension, FAN-4′, FAN-8′, FAN-6′ | Reductio gives `s=τ`; high vertices have `g≥τ+1`. Exact earlier-block occupancy/value is used. Match. |
| Lemma FAN-1 | FAN-4′, FAN-8′, GFAN2/GFANν chain | GFan extension proves identical degree categories and tie handling. Only “first p heads are B_hi” is used. Match. |
| Proposition L2 | RIG-1 | Hard core and `L=2` are supplied. Clause (b) suffices for universality; clause (a) is cited but unnecessary. Conclusion use is valid. |
| Corollary MB1 | RIG final bound/N4 | Matches in the hard core. The broadened frame+reductio sentence drops printed `τ≥4`; N4 does not establish that weakening. Mismatch there. |
| Theorem K | GFAN2-HC, GFANν-HC | Reductio and `L=0`, hence every B-degree at least `τ+1`, are supplied. Only clique conclusion is used. Match. |
| Theorem MB | N4 scope chain | Printed hypothesis is hard core plus `L≥1`. N4 claims availability at `τ≥2` without the printed `τ≥4`; no proof is supplied. Mismatch. |
| Theorem SL | N4 scope chain | Reductio, `τ≥2`, and `L≥1` are the printed guards and the claimed guards. LOW3 is the named conclusion. Match. |
| Theorem FAN | RIG-2, GFAN2-HC | `Fan(τ,L)` and `L≥2` are supplied before eliminating `ν=1`. Only the no-equality conclusion is used. Match. |
| Lemma TAIL (listed import, located in C) | GFANν | `E=0`, nonempty λ, and `L≥λ₁` are supplied in its branch. Formula/equivalence are used exactly. Match. |

The A.1 facts S, Z+, F3′, C*, (F-b), L1-short, and Favaron–Maheo–Saclé are not directly imported by Appendix B/C proofs under review; some support statements inside A.1 itself. L1-short is explicitly unused in Appendix B.

## 3. IMPORT INTERFACE ROLL CALL

### 3.1 Eighteen-name statement check

| # | name | statement present? | where |
|---|---|---|---|
| 1 | Lemma FAN-1 | YES | Appendix A.1, “Lemma FAN-1 (high phase first)” plus its GFan extension paragraph. |
| 2 | Lemma DICH (a)–(c) | YES | Appendix A.1, “Lemma DICH (head dichotomy)”; all three clauses are explicit. |
| 3 | Proposition L2 | YES | Appendix A.1, “Proposition L2”; clauses (a)–(e) are explicit. |
| 4 | Corollary L1-short | YES | Appendix A.1, its named block. |
| 5 | Corollary MB1 | YES | Appendix A.1, “a floor on L.” |
| 6 | Lemma TAIL | YES | Appendix C, immediately before Theorem GFANν. |
| 7 | Lemma 4 | YES | Appendix A.1 opening statement. |
| 8 | Observation R1 | YES | Appendix A.1 opening statement. |
| 9 | Lemma C* | YES | Appendix A.1 combined C*/(F-b) paragraph: type vertices have `deg_A≥3`. |
| 10 | (F-b) | YES | Same combined paragraph: every `T1×T2` cross pair is nonadjacent. |
| 11 | Lemma S | YES | Appendix A.1, survivor degree bound. |
| 12 | Lemma Z+ | YES | Appendix A.1, block occupancy. |
| 13 | Lemma F3′ | YES | Appendix A.1, survivor decay. |
| 14 | Theorem K | YES | Appendix A.1, with both hypotheses and all three conclusions. |
| 15 | Theorem MB | YES | Appendix A.1, master-budget inequality and scope. |
| 16 | Theorem SL | YES | Appendix A.1, slack and LOW3 forms. |
| 17 | Theorem FAN | YES | Appendix A.1, no-Fan equality statement and consequence. |
| 18 | Favaron–Maheo–Saclé | YES | Appendix A.1, `residue(G)≤alpha(G)` for every graph. |

Result: all eighteen names have substantive statements. C* and (F-b) share one physical paragraph, but each named interface is stated. Nothing on the eighteen-name list is still unsupplied.

### 3.2 Corollary GFANν-HC: complete outside-fact interface

| import | hypothesis required | hypothesis supplied | conclusion proved | conclusion used | file-alone check? |
|---|---|---|---|---|---|
| Theorem K | residue=alpha; every `b∈B` has degree `≥τ+1` | hard core supplies equality; `L=0` means no degree-`≤τ` B-vertex | `K=B`, full B edge count, hence B clique | B clique | YES |
| Observation R1 | hard-core frame, in particular `diam=4` | target is in hard core | B nonclique, hence `ν≥1` | contradiction to K; lower bound `ν≥1` | YES |
| Theorem RIG | frame; `B_lo≠∅`; every low vertex B-universal; reductio for `ν≤L−1` | hard core; K/R1 step gives nonempty; target assumption gives universality | GFan configuration and `1≤ν≤L−1` | exactly that configuration/range | YES at statement interface; N4 leaves its broadened proof scope unresolved |
| Theorem GFANν | GFan; residue=alpha; `1≤ν≤10`; `L≥ν+1` | RIG; hard core; eliminated case range; RIG inequality | no such graph | eliminates every available `ν≤10` | YES |

No direct target import has an interface that is absent from this file. The conclusion of Theorem GFANν is consumed verbatim: same `τ`, `1≤ν≤10`, `L≥ν+1`, GFan configuration, and residue equality.

### 3.3 Bracket count

The proof explicitly reaches four named outside facts: K, RIG, R1, and GFANν. All four are used, and I found no fifth named theorem/lemma import. Thus **the bracket's count “FOUR” is correct in both directions**. Its count is repaired; its clause completeness is not, because two required guards are omitted as recorded below.

## 4. Defect list

### D1 — MATHEMATICS — N4 does not establish Theorem RIG's weakened scope

Theorem RIG claims `ν≤L−1` in frame+reductio without the canonical hard core's `τ≥4`. Its proof imports Corollary MB1. MB1 is literally stated only “in the hard core,” and its proof imports Theorem MB, also literally stated in the hard core; Appendix A defines that scope to include `τ≥4`. N4 asserts that the chain only consumes `τ≥2`, but the MB proof is not supplied, and A.1 expressly says whether MB consumes the rider is unanswered. Thus N4 is an assertion, not a supplied weakening proof. Restricting RIG's final bound back to the hard core, or printing a proof of the weakened MB interface, would settle it. The target corollary itself is filed in the hard core, so this gap does not furnish a counterexample to its implication.

### D2 — MATHEMATICS — AZ bracket omits one RIG guard

RIG's statement requires “every low vertex is B-universal.” The target supplies it as its own hypothesis, so the mathematical invocation is sound and file-alone checkable. But bracket clause (ii), under a claim to list every required guard locally, names the frame and `B_lo≠∅` and omits universality. Under J-AZGUARD's predeclared classification, a needed-but-not-claimed guard is a MATHEMATICS defect of the bracket.

### D3 — MATHEMATICS — AZ bracket omits GFANν's residue-equality guard

Theorem GFANν eliminates GFan configurations **satisfying `residue=alpha`**. The target supplies equality because “in the hard core” includes the reductio. Bracket clause (iv) lists the configuration, ν-range, and L-bound, but not residue equality, despite claiming to enumerate all guards. The proof is checkable and the guard is present; the bracket's completeness claim is false. J-AZGUARD requires this omission to be classified MATHEMATICS.

### D4 — BOOKKEEPING — RIG-1 over-cites Proposition L2(a)

RIG-1 says L2(a),(b) force `B_lo+=∅`. Clause (b), “both are B-universal,” alone gives that conclusion; adjacency clause (a) contributes nothing. This is harmless over-citation and does not reintroduce the removed tightness argument.

### D5 — BOOKKEEPING — independence provenance is not established inline

The pasted diff establishes agreement of outputs, but it cannot establish that the programs were independently written; doing that requires source/provenance files this brief prohibits reading. I therefore treat “independently written” as unverified provenance. This does not affect the enumeration here: my own specification-first regeneration matched all printed data both directions.

### J-NEWTEXT sub-list

- N1 — CLEAN: true; needed to make MB's `L≥1` interface available; K plus R1 supplies it. Universal quantification over an empty low set would not.
- N2 — CLEAN: true and needed at GFAN2-HC before RIG; it supplies nonemptiness using K/R1.
- N3 — CLEAN: the same sentence is true and needed at GFANν-HC for the same local reason. The different downstream eliminator does not alter this interface.
- N4 — GAP/MATHEMATICS: `τ≥2` follows correctly from connectedness, `diam=4`, and `τ=|B|`; SL has that scope. Theorem MB does not: its printed interface retains hard core/`τ≥4`, and no weakening proof is supplied.

### J-AZGUARD sub-list

- K-a — CLEAN: hard core supplies residue equality.
- K-b — CLEAN: `L=0` is exactly the absence of B-degrees `≤τ`, hence every B-degree is at least `τ+1`; universality is correctly identified as vacuous and unused.
- K conclusion — CLEAN: clique is proved and is the only K conclusion used.
- RIG frame — CLEAN: hard core supplies it.
- RIG nonempty-low guard — CLEAN: K plus R1 supplies `L≥1` first.
- RIG universal-low guard — DEFECT: required and actually supplied by the corollary hypothesis, but not claimed in bracket clause (ii).
- RIG reductio guard for the upper bound — CLEAN as availability: hard core supplies it; N4 separately fails to prove the claimed reduced scope.
- RIG conclusion — CLEAN at interface: GFan and `1≤ν≤L−1` are exactly stated and used.
- R1 — CLEAN: frame/diameter four is available; nonclique/`ν≥1` is exactly used.
- GFANν configuration/range/L guards — CLEAN: all three are named and supplied.
- GFANν residue-equality guard — DEFECT: required and supplied by hard core, but omitted from clause (iv)'s claimed roll call.
- GFANν conclusion — CLEAN: the theorem's complete `1≤ν≤10` elimination is used verbatim.
- `τ≥4` negative claim — interface-clean against the four printed target imports; proof-level confidence is limited by D1's unsupported RIG scope weakening.
- Import count — CLEAN: exactly four, no omitted fifth and no unused listed import.

## 5. Refutation log

I implemented HH directly from A.0, generated integer partitions recursively, and generated every C.1 multiset without consulting printed survivor values. Only after generation did a separate comparison parse the printed data.

Raw regeneration summary:

```text
nu=1:  boundary=0/0   Epos=0/0       FAN6_misses=0
nu=2:  boundary=1/1   Epos=3/1       FAN6_misses=0
nu=3:  boundary=3/1   Epos=24/4      FAN6_misses=0
nu=4:  boundary=7/2   Epos=110/9     FAN6_misses=0
nu=5:  boundary=14/2  Epos=397/20    FAN6_misses=0
nu=6:  boundary=26/3  Epos=1211/38   FAN6_misses=0
nu=7:  boundary=45/3  Epos=3340/75   FAN6_misses=0
nu=8:  boundary=75/4  Epos=8457/137  FAN6_misses=0
nu=9:  boundary=120/4 Epos=20126/251 FAN6_misses=0
nu=10: boundary=187/5 Epos=45450/447 FAN6_misses=0
C2_s0 printed=159 computed=159 mismatches=0
Epos printed=982 generated=982 generated_minus_printed=0 printed_minus_generated=0
boundary printed=25 generated=25 generated_minus_printed=0 printed_minus_generated=0
```

GFAN2 was attacked separately. Its eight `L=3` step counts regenerated as `3,4,4,4,5,3,4,4`; exactly the two three-step rows have single-part residues and FAN-6′ kills both. At `L=4` the three remaining E=0 types take `5,5,6` steps; at `L=7` they take `8,8,9`, confirming the claimed uniform excess.

Named roster rows checked by rebuilt list and certificate included:

- C-5: `ν=5,L=6,E=4,e=(2,2),λ=(4,2)` gives list `(8,8,6,6,6,6,6,4,2)`, six steps, certificate `(4,2)`.
- C-5: `ν=6,L=7,E=5,e=(3,2),λ=(4,2,1)` gives seven steps, certificate `(4,2)`.
- C-8: `ν=7,L=8,E=6,e=(3,3),λ=(4,2,2)` gives eight steps, certificate `(4,2)`.
- C-8: `ν=8,L=9,E=8,e=(4,4),λ=(4,2,2,2)` gives nine steps, certificate `(4,2)`.
- C-8: `ν=10,L=11,E=9,e=(5,4),λ=(4,2,2,2,1)` gives eleven steps, certificate `(4,2)`.

Construction attacks:

- Removing GFANν's lower bound succeeds: `K3` with `A={a0}`, `B={b1,b2}` is `GFan(2,2,0)` and has residue=alpha=1. Thus `ν=0` would refute the extended statement.
- For N4 I exhaustively searched all unlabeled graphs of order at most seven in NetworkX's graph atlas with `τ∈{2,3}`. There were zero frame+reductio graphs, hence no universal-low instance and no bound violation. This empty box is not evidence for N4.
- No counterexample appeared in the complete C.1 shape search for `1≤ν≤10`; every survivor was killed by FAN-6′.

The complete unedited stdout is in `problems/wowii/w61_S3_GFAN_r26_check.out`.

## 6. Mandatory control section

### 6.1 Counterfactual availability

Take the nominal shape parameters `(ν,L,E)=(2,3,0)` and list `[3,3,3,3,1]`. Its C-part is of the required form, but its A′ mass is 1 rather than `2ν−E=4`; the HH run is not a step sequence. FAN-4′'s conclusion fails, so FAN-8′ and the GFAN2 finite-list elimination are unavailable. This confirms that the mass identity is load-bearing.

### 6.2 Witness validation in class-definition order

For the only graph witness, `K3` with `A={0}`, `B={1,2}`:

1. Connected: yes.
2. A maximum: exhaustive independent sets have maximum size 1, namely `{0}`, `{1}`, `{2}`; hence `alpha=1`.
3. Diameter: `1`, so it is not a hard-core frame (not needed by GFANν).
4. Forest number: `f=2=alpha+1`; every two-vertex induced subgraph is a forest, while all three vertices induce a cycle.
5. Non-forest: yes.
6. Residue versus alpha: HH on `[2,2,2]` leaves one zero, so `residue=1=alpha`.

Also, B is a clique, both B-vertices are low of degree `τ=2`, each has unique A-neighbour `0`, `B_hi=A′=∅`, and `ν=0`; hence every GFan clause holds.

### 6.3 Vacuity honesty

The N4 graph-atlas search box contained no graph satisfying frame+reductio at `τ=2,3`, so it gave no full-hypothesis test and is not positive evidence. The value-list enumeration is a necessary-condition superset, not an existence search for hard-core graphs; absence of an un-killed list supports the elimination proof, not existence/nonexistence of other graph classes.

## 7. What I could not check

- N4's claim that Theorem MB's proof does not consume `τ≥4`: MB's proof is absent. This is the substantive GAP; a weakened theorem statement with proof would settle it.
- The asserted historical independence of the author's two programs and restricted dispatch/log provenance. The pasted output cannot establish authorship independence, and the brief forbids checking those files.
- I did not referee proofs of Appendix A.1 imported facts beyond their interfaces, as explicitly instructed.
- The graph-atlas construction search stops at seven vertices; it cannot refute or prove N4 beyond that finite box.
- Nothing is missing from the target's four direct import interfaces: each required statement, hypothesis, and conclusion is present and checkable from this file alone.
