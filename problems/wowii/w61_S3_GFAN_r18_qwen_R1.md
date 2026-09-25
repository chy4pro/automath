EXECUTION ENVIRONMENT: I did NOT run code. Everything below is hand-derived.

VERDICT: GAP — no MATHEMATICS defect found in the two target statements; the full finite enumeration/completeness was not independently verified without code.

TEXT VERSION REVIEWED: w61_S3_GFAN_r18

TARGET VERDICT (Theorem GFANnu): GAP  
TARGET VERDICT (Corollary GFANnu-HC): GAP  

## 0. Held-out checks

| # | value | derivation |
|---|---|---|
| **H1** | `[12,6,4]: 14`; `[9,7,3,3]: 12`; `[14,5,2,1]: 16`; `[8,8,6]: 10` | Hand Havel–Hakimi from (C-1)(4); all four lists are valid step sequences. Counts obtained by repeated head-delete/prefix-subtract until all remaining entries are zero. |
| **H2** | `S(11) = 98,384` | `S(11)=Σ_{E=1}^{10}(11-E)p(E)p(22-E) = 10·1·792 + 9·2·627 + 8·3·490 + 7·5·385 + 6·7·297 + 5·11·231 + 4·15·176 + 3·22·135 + 2·30·101 + 1·42·77 = 98,384.` |
| **H3** | `CANNOT COMPUTE` | Requires enumerating and simulating all `98,384` `E≥1` shapes at `ν=11`, then splitting survivors by `E`; beyond honest hand computation. |
| **H4** | `CANNOT COMPUTE` | Requires computing `s0(λ)` for all `p(22)=1002` partitions of `22`; beyond honest hand computation. No closed form is supplied or extrapolated. |
| **H5** | `NO`; actual step count `16` | List is `15, 14, 13^12, 5, 4, 4, 3, 3` (zero padding inert). Hand run clears in 16 steps, not 13. |

## 1. Joint table

| joint | verdict | justification |
|---|---|---|
| **J-FAN4P** *(context)* | CLEAN | Re-derived; `p` cancels via `τ=p+L`. `E=0` gives `A′` mass `2ν` and `C`-part `L`. `p=0` is impossible for `ν≥1` since non-edges must lie in `B_hi`. |
| **J-FAN8P** *(context)* | CLEAN | Escape step exists only if `E≥1`. Subtracted sets are disjoint and inside the block; prefix inequality is tie-safe. `E=0` is not covered; hypothesis is load-bearing. |
| **J-FAN6P** *(context)* | CLEAN | Backward induction checks. Zero convention only encodes absence of a `w−1` entry. Bracket list is correct at `[w]`, `[3,1]`, `[4,2]`, etc. |
| **J-GFAN2** *(context)* | CLEAN | Hand-simulated the eight `L=3` rows; `L≥4` tail matches. Escape budget gives `E=0` for `L≥4`, `E≤1` for `L=3`, so the row list is complete. |
| **J-RIG1** *(context)* | CLEAN | Uses L2(a),(b) only to force `B_lo+ = ∅`; Theorem RIG then supplies the rest. The tightness re-run is genuinely removed, not secretly reused. |
| **J-CORHC** *(target for GFANnu-HC)* | CLEAN | Arithmetic/dependency correct: RIG gives `1≤ν≤L−1`; GFANν kills `ν≤10`; hence `ν≥11`, `L≥12`. Corollary L1-short is unused in Appendix B. |
| **J-FIN** *(TARGET)* | CLEAN | Split `E=0/L≥λ1`, `E=0/L<λ1`, `E≥1` is disjoint/exhaustive. `λ1≤2ν`; `E≤ν−1`. Lower bound `ν≥1` is needed; `ν=1` is covered. |
| **J-SPEC** *(TARGET)* | CLEAN | Conventions specify a superset of actual GFan step-`p+1` multisets. Unlabelled reduction legitimate; zero-inertness true; no graphicality filter is monotone in needed direction. |
| **J-DATA** *(TARGET)* | GAP | Boundary counts, closed form `S(ν)`, and selected rows verified by hand. Full `s0` columns and roster completeness were not verified without code. |
| **J-KILL** *(TARGET)* | GAP | Printed certificates satisfy `2nd ≤ w−2`; spot-checked `(4,2)`, `(3,1)` and others. I did not individually re-run every printed survivor row. |
| **J-IMPORT** *(TARGET)* | PARTIAL | All checked imports match hypotheses/conclusions. FAN-1 is stated for `Fan` but the printed GFan-availability note proves the needed extension; bookkeeping ambiguity only. |
| **J-SCOPE** *(TARGET)* | CLEAN | Theorem consumes GFan + reductio + `L≥ν+1`; corollary consumes RIG. No under-hypothesis found; no imported hypothesis is weakened in passing. |

## 2. Import table for J-IMPORT

| imported fact | caller(s) | hypothesis match / conclusion match |
|---|---|---|
| Lemma 4 | Theorem RIG(b),(c) | Adjacent `B` pairs in frame supplied; common A-neighbour conclusion used. Match. |
| Observation R1 | RIG(d); MB1; L2 | `diam=4` frame supplied; conclusion `ν≥1` used. Match. |
| Corollary MB1 | Theorem RIG final bound | Hard core + all low B-universal supplied; conclusion `ν≤L−1` used. Match. |
| Lemma DICH(b) | FAN-1, FAN-4′, FAN-8′, FAN-6′ | High original degree `≥s+1` supplied; exact block membership / `h_i=i−1` used. Match. |
| Lemma DICH(c) | FAN-1 proof | Head degree `≤s` supplied; upper bound used for tie-break. Match. |
| Lemma FAN-1 | FAN-4′, FAN-8′, FAN-6′, GFAN2 | GFan degree conditions in availability note supply hypothesis; first `p` heads high used. Match; wording only Fan-stated. |
| Theorem MB | Proposition L2; Corollary MB1 | Hard-core hypotheses supplied; inequality on `|B_lo+|+c+mbar` used. Match. |
| Theorem SL (LOW3) | Proposition L2(e) | Hard-core `L=2` data supplied; upper bound on `Σ deg_A(b)` used. Match. |
| Lemma C\* | Proposition L2(d) | Type vertex supplied; conclusion `deg_A≥3` used. Match. |
| (F-b) | Proposition L2(a) | Frame type classes supplied; cross non-adjacency used. “Occurring” non-empty implicit; wording note only. |
| Theorem FAN | RIG-2; GFAN2-HC | `Fan(τ,L≥2)` in hard core supplied; elimination of `ν=1` used. Match. |
| Proposition L2 | Corollary RIG-1 | Hard core `L=2` supplied; clauses (a),(b) used to get `B_lo+=∅`. Match. |
| Corollary L1-short | none in Appendix B/C | Unused; no import to check. |

## 3. Defect list

### 3.1 BOOKKEEPING — FAN-1 statement versus GFan callers

Lemma FAN-1 is stated for `Fan(τ,L)`, while FAN-4′, FAN-8′, FAN-6′ and Theorem GFAN2 call it inside `GFan(τ,L,ν)`. The printed “Why FAN-1 is available on GFan” note supplies the needed extension by checking the degree conditions. I regard this as a presentational/import-wording issue, not a mathematics defect: the proof of FAN-1 uses exactly the degree separation that GFan supplies. An explicit GFan corollary would remove the ambiguity.

### 3.2 BOOKKEEPING — duplicated `(C-8)` heading and lower-case cross-reference

Appendix C contains two adjacent headings beginning “(C-8) The ν = 7…10 rosters …”, and Theorem GFANν’s proof refers to “certified toolkit (c-3)” in lower case. These are cross-reference/formatting defects only; they do not alter the mathematical content.

### 3.3 BOOKKEEPING — non-emptiness of `T_1`, `T_2` in (F-b) import

Proposition L2’s proof uses that `T_1` and `T_2` are non-empty when it derives a contradiction from an adjacent `T_1 × T_2` pair. Appendix A.1 says “occurring types”, which strongly suggests non-emptiness, but does not state it as an explicit clause. This is a wording/bookkeeping issue in a context proof, not a target mathematics defect.

### 3.4 No MATHEMATICS defect found in the two target statements

Within the scope I could verify by hand — finiteness split, specification conventions, boundary counts, closed form `S(ν)`, selected survivor rows, selected certificates, imports, and the corollary arithmetic — I found no false claim, no mismatched import, and no counterexample. The remaining gap is the complete machine enumeration, which I did not rerun.

## 4. Refutation log

### 4.1 Hand calibration of Havel–Hakimi

No code was run. I hand-ran the Havel–Hakimi rule from Appendix A.0.

- `K2`: degree list `[1,1]`. Step 1 deletes `1`, subtracts from the other `1`, leaves `[0]`. Residue `1`.
- Cycles `C_n`, degree list `[2^n]`:

| graph | hand HH residue | expected `ceil(n/3)` | result |
|---|---:|---:|---|
| `C3` | 1 | 1 | ok |
| `C4` | 2 | 2 | ok |
| `C5` | 2 | 2 | ok |
| `C6` | 2 | 2 | ok |
| `C7` | 3 | 3 | ok |
| `C8` | 3 | 3 | ok |
| `C9` | 3 | 3 | ok |

This calibration was done before relying on hand HH counts below.

### 4.2 Attempt to refute Theorem GFANnu at small `ν`

I did not regenerate the full `ν=3…10` finite lists by hand; that would be unreasonable without code. I did hand-check the smallest cases.

- `ν=1`: `E≥1` is impossible because `L≥2` and `L≤2−E` would force `E≤0`. For `E=0`, partitions of `2` are `[2]` and `[1,1]`. `[2]` is killed by FAN-6′; `[1,1]` has `s0=2≠λ1=1`, so it does not clear in exactly `L`. No counterexample.
- `ν=2`: `E=1`, only `L=3`, `e=1`, and partitions of `3`: `[3]`, `[2,1]`, `[1,1,1]`. Hand runs give exactly one survivor, `λ=[3]`, with list `4,3,3,3,3`, clearing in 3 steps and killed by certificate `(3,0)`. The other two clear in 4 steps. No counterexample.

### 4.3 Spot-checked printed survivor rows from (C-5) and (C-8)

Rows I rebuilt from (C-1) and hand-ran:

1. **ν=2, `L3 E1 e=1 λ=3`**, certificate `(3,0)`.  
   List: `4, 3^4`. Hand run: `4,3^4 → 2^4 → 2,1,1 → zeros`, exactly 3 steps. Certificate valid: unique max `3`, second `0 ≤ 1`.

2. **ν=3, `L4 E2 e=2 λ=3+1`**, certificate `(3,1)`.  
   List: `6, 4^4, 3, 1`. Hand run clears in exactly 4 steps. Certificate valid: unique max `3`, second `1 ≤ 1`.

3. **ν=5, `L6 E4 e=2+2 λ=4+2`**, certificate `(4,2)`.  
   List: `8,8, 6^5, 4, 2`. Hand run clears in exactly 6 steps. Certificate valid: unique max `4`, second `2 ≤ 2`.

4. **ν=6 boundary `(L,λ)=(7,[10,1,1])`**, certificate `(10,1)`.  
   List: `10, 7^8, 1, 1`. Hand run clears in exactly 7 steps. Certificate valid: unique max `10`, second `1 ≤ 8`.

5. **ν=7, `E1 e=1 λ=13`, `L=12` and `L=13`**, certificate `(13,0)`.  
   For `L=12`: list `13,13,12^12`. Hand run: step 1 gives `12,11^12`; step 2 gives `10^12`; `[10]^12` clears in 10 further steps, total 12.  
   For `L=13`: list `14,13^14`. Step 1 gives `12^14`; `[12]^14` clears in 12 further steps, total 13. Certificate valid: unique max `13`, second `0`.

No printed row I spot-checked failed to be a survivor, and no certificate I checked violated FAN-6′.

### 4.4 Boundary-pair counts verified by hand

For `E=0`, boundary pairs are `(L,λ)` with `ν+1 ≤ L < λ1`. For each partition of `2ν`, the number of such `L` is `max(0, λ1−ν−1)`.

Using partitions by largest part, I obtained:

- `ν=1`: `0`
- `ν=2`: `1`
- `ν=3`: `3`
- `ν=4`: `7`
- `ν=5`: `14`
- `ν=6`: `26`
- `ν=7`: `45`
- `ν=8`: `75`
- `ν=9`: `120`
- `ν=10`: `187`

These agree with the printed boundary-pair counts.

### 4.5 Closed form `S(ν)` verified by hand

Using standard partition numbers up to `p(20)=627`, I evaluated

`S(ν)=Σ_{E=1}^{ν−1}(ν−E)p(E)p(2ν−E)`

and obtained:

`ν=1: 0`  
`ν=2: 3`  
`ν=3: 24`  
`ν=4: 110`  
`ν=5: 397`  
`ν=6: 1211`  
`ν=7: 3340`  
`ν=8: 8457`  
`ν=9: 20126`  
`ν=10: 45450`

These agree with the printed values.

### 4.6 What I did not do

I did not run code, did not regenerate the full `ν=3…10` rosters, and did not independently verify completeness of the survivor lists. I also did not read any author files or restricted material.

## 5. Mandatory control section

### 5.1 Counterfactual availability

A concrete GFan-shaped step-`p+1` value list violating the reductio mass invariant:

`ν=2`, `E=0`, `L=3`: take `C`-part `[3]^4` and `A′`-part `[1]`.

This has the shape of an `E=0` GFan list, but the `A′` total is `1`, whereas Lemma FAN-4′ under the reductio requires total `2ν−E=4`. Therefore FAN-4′, and the downstream reductio-only lemmas FAN-8′/FAN-6′ as used in the theorem, are unavailable on this object. The reductio hypothesis is load-bearing.

### 5.2 Witness validation in class-definition order

I did not name a graph as a theorem-refuting witness. The counterfactual above is a value list, not a graph witness. Thus no graph class-predicate validation is required.

### 5.3 Vacuity honesty

I performed no exhaustive search over graphs and no exhaustive regeneration of the full finite shape space for `ν=3…10`. The absence of a counterexample in my spot checks is not positive evidence of completeness. I attacked ingredients separately: calibration, boundary counts, closed form `S(ν)`, selected `s0` runs, and selected survivor rows.

### 5.4 What I could NOT check

See Section 6 below.

## 6. What I could not check

1. **Held-out H3 and H4.** I could not enumerate `ν=11` survivors or all `s0(λ)` values for partitions of `22` by hand.
2. **Full `E=0` `s0` column.** I did not recompute `s0(λ)` for all 159 partitions with `ν≤6`, nor for the much larger `ν=7…10` partition sets. I spot-checked several.
3. **Completeness of survivor rosters.** Without code, I did not verify that the printed boundary and `E≥1` survivor rows are complete inside the specified finite sets.
4. **Every printed survivor row.** I spot-checked named rows above and checked the certificate condition on samples, but I did not individually re-run all 985+ survivor rows.
5. **Author’s machine controls.** I did not verify the claimed `1,817`, `17,959`, or `18,963` control pairs, nor the independent recomputation diffs.
6. **Context proofs.** As instructed, I did not referee the proofs of Appendix A.1 imported facts; I only checked import matching.

VERDICT: GAP