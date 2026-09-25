EXECUTION ENVIRONMENT: I ran code. Python 3.9.6.
Corollary GFANν-HC: GAP — a MATHEMATICS defect was found in its guard/import audit.
VERDICT: GAP — MATHEMATICS defect found.
TEXT VERSION REVIEWED: w61_S3_GFAN_r24

## 0. Section 0 held-out checks

| row | result | derivation (at most two lines) |
|---|---|---|
| H1 | `[12,6,4]→14`; `[9,7,3,3]→12`; `[14,5,2,1]→16`; `[8,8,6]→10` | The four head sequences are respectively `12,12,10,10,8,8,6,6,5,4,3,2,2,1`; `9,9,7,7,6,5,4,3,2,2,1,1`; `14,14,12,12,10,10,8,8,6,6,5,4,3,2,1,1`; `8,8,7,6,5,4,3,3,2,1`. All are valid step sequences. |
| H2 | `S(11)=98,384` | Terms for `E=1,…,10`: `7,920+11,286+11,760+13,475+12,474+12,705+10,560+8,910+6,060+3,234`. These are `(11-E)p(E)p(22-E)`. |
| H3 | `791`; per-`E` split `[6,14,21,35,47,85,110,155,170,148]` | Generated every partition `e⊢E`, every `λ⊢(22−E)`, and every `12≤L≤22−E`: `98,384` shapes. Direct HH simulation retained exactly the displayed split. |
| H4 | `131` | Generated all `p(22)=1,002` nonincreasing partitions recursively and ran `[λ₁]^(λ₁+1)∪λ`; exactly 131 valid runs had 13 steps. The full matching list is in the raw stdout. |
| H5 | **NO; actual step count `16`** | The list is `[15,14,13^12,5,4,4,3,3]`; its heads are `15,13,11,10,9,8,7,6,5,4,4,3,2,2,2,1`, so it does not clear in 13 steps. |

Calibration printed before those computations:

```text
K2 degrees [1,1]: valid=True, steps=1, residue=1, expected=1
C3..C9 residues: 1,2,2,2,3,3,3; expected ceil(n/3): 1,2,2,2,3,3,3
```

## 1. Joint table

| joint | verdict | justification (≤40 words) |
|---|---|---|
| J-FAN4P | CLEAN | Degree sums give `pτ−2ν+R`; subtracting later-high and C decrements cancels all `p` terms and leaves `2ν−E`. `E=0` and `p=0` remain meaningful. FAN-1/DICH(b) interfaces match. |
| J-FAN8P | CLEAN | Remaining-high and nonescaping-C sets are disjoint block subsets. Prefix comparison is tie-safe. The conclusion genuinely needs an escape; at `E=0` there is no escape step to select. |
| J-FAN6P | CLEAN | Backward induction and the zero convention match the operative “no `w−1` entry” condition. The listed smallest killed and surviving residues satisfy, or fail, the unique-top gap exactly as stated. |
| J-GFAN2 | CLEAN | Independent simulation reproduced all eight `L=3` rows and all five partition trajectories for several `L≥4`; the escape bound makes the eight-row list exhaustive. Only `[4]` and `[3]` clear in three steps, both certified. |
| J-RIG1 | CLEAN | L2(a),(b) give adjacency and B-universality, hence `B_lo⁺=∅`. RIG supplies unit A-degrees/common neighbour/configuration; its bound and R1 give `ν=m̄=1`. No tightness step is reused. |
| J-CORHC | GAP | The arithmetic and GFANν conclusion match are correct, and L1-short is unused in Appendix B. But both hard-core corollaries rely on the unstated Theorem K interface to establish `L≥1`. |
| J-FIN | CLEAN | The three cases are disjoint and exhaustive. `λ₁≤2ν`; for `E≥1`, the two L-bounds imply `E≤ν−1`. `ν≥1` makes the E=0 residue nonempty. No ν=0 extension is claimed. |
| J-SPEC | CLEAN | Multiset reduction and zero inertness hold; my 730,320 padding comparisons had zero mismatches. Omitted graphicality, `p`-feasibility, and `e_c≤p` constraints only enlarge the tested set, which is safe for elimination. |
| J-DATA | PARTIAL CHECK | All aggregate counts, survivor counts, boundary counts, and unique TAIL survivors through ν=10 were independently regenerated and agreed. Five named rows were rebuilt. I did not transcribe and compare every printed row/value individually. |
| J-KILL | PARTIAL CHECK | Every independently generated survivor through ν=11 satisfied FAN-6′, with zero misses. Five printed rows and certificates were checked directly; I did not parse all 910 printed rows for row-by-row identity. |
| J-IMPORT | GAP | All inspectable interfaces match, but Theorem K's statement is absent. Theorem MB/SL inequalities are printed without complete hypothesis scopes, so N4's scope assertion also cannot be checked. |
| J-SCOPE | GAP | The proof consumes frame, reductio, all-low B-universality, and `L≥1`; it claims not to consume `τ≥4`. That last claim is unverifiable because the Theorem K import supplying `L≥1` has no printed hypotheses. |
| J-NEWTEXT | GAP | N1–N3 depend on an unstated Theorem K interface; N4's MB/SL scope claim lacks printed interfaces. The elementary vacuity and `τ≥2` subclaims are correct. |
| J-AZGUARD | GAP | The bracket correctly checks RIG, R1, and GFANν, but falsely calls them the proof's three imports: Theorem K is a fourth import. Its guard is neither listed nor checkable. |

## 2. J-IMPORT table

| imported Appendix A.1 fact | caller(s) | hypothesis and conclusion match (≤30 words) |
|---|---|---|
| Lemma 4 | RIG(b),(c) | MATCH. The hard-core frame is supplied; adjacent B-pairs are established. Only a common A-neighbour is used. |
| Observation R1 | RIG(d), N1–N3, GFANν-HC | MATCH where reached. The frame supplies `diam=4`; “B not clique,” hence `ν≥1`, is exactly used. The preceding K premise remains unresolved. |
| Lemma DICH(b) | FAN-1 extension, FAN-4′, FAN-8′, FAN-6′ | MATCH. Under reductio `s=τ`; high degrees are at least `τ+1`, yielding every-earlier-block membership and the exact deletion value used. |
| Lemma DICH(c) | FAN-1 and its GFan extension | MATCH. Non-high entries have original degree at most `τ=s`; callers use only the unconditional head-value upper bound. |
| Lemma FAN-1 plus printed GFan extension | FAN-4′, FAN-8′, GFAN2 | MATCH. Configuration and reductio supply the degree split and `s=τ`; callers use only that the first `p` heads are `B_hi`. |
| Proposition L2(a),(b) | RIG-1 | MATCH. Hard core and `L=2` are supplied; adjacency/B-universality imply `B_lo⁺=∅`, exactly as used. |
| Corollary MB1 | RIG final bound | MATCH at the stated interface. Hard core and all-low B-universality are supplied; only `ν=m̄≤L−1` and its floor are used. |
| Theorem FAN | RIG-2, GFAN2-HC, GFANν's ν=1 note | MATCH. Callers have hard core, identify `ν=1` with `Fan(τ,L)`, and establish `L≥2`; the printed elimination conclusion is exact. |
| Theorem K | N1, N2, N3; thus GFANν-HC | UNRESOLVED. A.1 names K but prints neither hypotheses nor conclusion. The callers need `L=0 ⇒ B` clique, and its guards cannot be checked. |
| Theorem MB | N4 scope claim | UNRESOLVED. Its inequality is printed, but its complete hypotheses are not; “uses only `τ≥2`” cannot be interface-checked. |
| Theorem SL | N4 scope claim | UNRESOLVED. LOW3 is printed, but its complete hypotheses are not; “uses only `τ≥2`” cannot be interface-checked. |
| Corollary L1-short | none in Appendix B | UNUSED, as claimed. It is mentioned but never invoked in an Appendix B inference. |

## 3. Defect list

1. **MATHEMATICS — target proof import/guard gap.** GFANν-HC must prove `B_lo≠∅` before invoking RIG, because “every low vertex is B-universal” is vacuous at `L=0`. It does so by asserting that Theorem K makes B a clique at `L=0`, then invokes R1. But Appendix A.1 does not state Theorem K's hypotheses or conclusion. Thus neither that implication nor its availability can be checked. The on-site bracket worsens the defect: it says the proof has three imports and audits RIG, R1, and GFANν, omitting K altogether. This is precisely J-AZGUARD's “guard needed and not claimed.” It also prevents verification of the claim that `τ≥4` is unconsumed: K may require it. Printing K's exact interface, and adding its guard to the bracket, would settle this obligation.

2. **MATHEMATICS — N4 import-scope gap.** N4 affirmatively claims that the chain Corollary MB1 → Theorem MB → Theorem SL uses only `τ≥2`. The brief prints MB and LOW3 inequalities but not the complete hypotheses of Theorems MB and SL. Consequently the claimed weakening from canonical hard core cannot be verified from the mandated source. This does not affect the target's numerical implication, because GFANν-HC is filed under the canonical hard core with `τ≥4`; it does affect the separately targeted new sentence N4.

### J-NEWTEXT

- **N1 — GAP:** needed to license MB at `L≥1`; vacuity observation is true, but K's missing interface leaves truth/supply unresolved.
- **N2 — GAP:** needed for RIG in GFAN2-HC; same valid vacuity observation, same missing K interface.
- **N3 — GAP:** needed for RIG in the target; same words and same guard role as N2, but this site reaches the target verdict.
- **N4 — GAP:** `diam=4 ⇒τ≥2` is correctly proved; the claimed MB/SL `τ`-scope is needed only for RIG's broadened statement and is uncheckable from their incomplete interfaces.

N2 and N3 are interchangeable as guard sentences: both sites start in the hard core with the same vacuous all-low hypothesis and next invoke RIG. Their downstream conclusions differ, not the guard obligation.

### J-AZGUARD

- **RIG clause — CLEAN:** hard core supplies frame and reductio; the proof separately asserts `B_lo≠∅`, subject to the K gap.
- **R1 clause — CLEAN:** `diam=4` is in the supplied frame; only non-cliqueness/`ν≥1` is used.
- **GFANν clause — CLEAN:** RIG supplies the configuration and `1≤ν≤L−1`; hence every eliminated case supplies `1≤ν≤10` and `L≥ν+1`.
- **Theorem K clause — MATHEMATICS defect:** absent from the bracket despite direct use; its hypotheses and conclusion are also absent from A.1.
- **“τ≥4 not consumed” — GAP:** verified for RIG/R1/GFANν, but not for K, whose scope is not printed.

## 4. Refutation log

I wrote the independent checker [w61_S3_GFAN_r24_check.py]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_GFAN_r24_check.py). Its complete unedited stdout is [w61_S3_GFAN_r24_check.out]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_GFAN_r24_check.out). Critical raw excerpts follow.

```text
nu=1: E+ tested=0, split={}, survivors=0, misses=0; E0 s0=lambda1=1 [(2,)]; boundary tested=0, survivors=0
  comparison with printed aggregate data: AGREE
nu=2: E+ tested=3, split={1: 1}, survivors=1, misses=0; E0 s0=lambda1=1 [(4,)]; boundary tested=1, survivors=1
  comparison with printed aggregate data: AGREE
nu=3: E+ tested=24, split={1: 2, 2: 2}, survivors=4, misses=0; E0 s0=lambda1=1 [(6,)]; boundary tested=3, survivors=1
  comparison with printed aggregate data: AGREE
nu=4: E+ tested=110, split={1: 2, 2: 4, 3: 3}, survivors=9, misses=0; E0 s0=lambda1=1 [(8,)]; boundary tested=7, survivors=2
  comparison with printed aggregate data: AGREE
nu=10: E+ tested=45450, split={1: 5, 2: 12, 3: 17, 4: 31, 5: 40, 6: 70, 7: 83, 8: 104, 9: 85}, survivors=447, misses=0; E0 s0=lambda1=1 [(20,)]; boundary tested=187, survivors=5
  comparison with printed aggregate data: AGREE
GFANnu nu<=10 aggregate comparison: ALL AGREE
```

No generated `ν≤10` survivor escaped FAN-6′. At ν=11 the run produced:

```text
H3 tested=98384; survivors=791; per-E E=1..10=[6, 14, 21, 35, 47, 85, 110, 155, 170, 148]; FAN6-misses=0
```

GFAN2 was attacked independently. The eight `L=3` step counts were `3,4,4,4,5,3,4,4`; the two three-step cases had certificates `(4,0)` and `(3,0)`. At `L=4,5,8`, the three non-killed partition types took respectively `L+1,L+1,L+2` steps.

Five roster rows checked by rebuilding their complete lists were:

```text
nu=5 L=6 E=4 e=(2, 2) lambda=(4, 2): valid=True, steps=6, cert=(4, 2, True)
nu=6 L=7 E=5 e=(3, 2) lambda=(4, 2, 1): valid=True, steps=7, cert=(4, 2, True)
nu=7 L=8 E=6 e=(2, 2, 2) lambda=(5, 3): valid=True, steps=8, cert=(5, 3, True)
nu=8 L=10 E=2 e=(2,) lambda=(12, 2): valid=True, steps=10, cert=(12, 2, True)
nu=10 L=11 E=9 e=(4, 4, 1) lambda=(5, 2, 2, 2): valid=True, steps=11, cert=(5, 2, True)
```

Construction search: exhaustive over all 32,768 labelled six-vertex graphs, then 12,000 fixed-seed sampled graphs on 7–10 vertices. It found no graph satisfying the full hard-core/all-low-universal composite hypotheses. This bounded absence is not evidence that the composite statement is true.

## 5. Mandatory controls

### Counterfactual availability

At `ν=3,L=4,E=1,e=[1]`, choose the deliberately wrong residue `λ=[4]`. Its list is `[5,4,4,4,4,4]`, and the run is invalid after four deletions. FAN-4′ requires residue mass `2ν−E=5`, whereas this has mass 4. Therefore it is not an output licensed by FAN-4′, and FAN-8′/FAN-6′ cannot turn it into an admissible GFan reductio case. This confirms that the mass/configuration hypotheses are load-bearing.

### Witness validation in class-definition order

No graph is named as a witness. The construction search tested candidates in the required order: connected; maximum independent sets by exhaustive subset enumeration; diameter; forest number; non-forest; residue versus alpha. It found no full-hypothesis instance, so there is no witness for which predicate results could honestly be printed.

### Vacuity honesty

The bounded graph search contained no instance satisfying all hypotheses of the composite target. I do not treat that absence as positive evidence. The finite sequence ingredients were attacked separately; their agreement does not repair the missing Theorem K interface.

Computational controls produced raw:

```text
zero-padding checks=730320, mismatches=0
TAIL direct-vs-formula checks=31210, mismatches=0
counterfactual shape nu=3 L=4 E=1 e=(1) lambda=(4): list=[5, 4, 4, 4, 4, 4], valid=False, steps=4; required lambda mass=5, actual=4
```

## 6. What I could not check

- Theorem K's interface, so I could not certify `L=0 ⇒ B` clique, K's availability at N1–N3, or the target's assertion that `τ≥4` is unconsumed. The exact K statement would settle all three.
- The complete hypotheses of Theorems MB and SL, so I could not certify N4's claim that their chain uses only `τ≥2`.
- The cited provenance/dispatch files and companion section, because the brief expressly forbids reading them. I treated that provenance as unverified and did not use it.
- I did not parse all 910 printed C-8 survivor rows or all 159 printed `s₀` values for literal row-by-row comparison. I regenerated the finite set and aggregate controls independently and directly checked the five named rows above.
- The exhaustive graph construction search was limited to `n=6`; `n=7…10` was deterministic sampling. It found no full-hypothesis graph, and therefore supplies no positive theorem evidence.
- I did not establish the historical claim that the two prior programs were independently written; the inline diff supports output agreement, not authorship independence. This does not undermine my separate implementation's agreement.
