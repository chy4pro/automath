VERDICT: CLEAN — No mathematical defect was found in Lemma TAIL’s reviewed scope; within its stated hypothesis `L ≥ λ₁` and `λ ≠ []`, direct simulation matches `(L − λ₁) + s₀(λ)` and all stated boundary behaviors are consistent with that hypothesis. No MATHEMATICS defects were found.
TEXT VERSION REVIEWED: w61_S3_TAIL_spark (Q27)

## 1) Refutation log

- Mandatory computation script: [problems/w61/w61_S3_TAIL_spark_check.py]($HOME/workspace/claudecode/automath/problems/w61/w61_S3_TAIL_spark_check.py)
- Output file: [problems/w61/w61_S3_TAIL_spark_check.out]($HOME/workspace/claudecode/automath/problems/w61/w61_S3_TAIL_spark_check.out)

Box searched:
- All partitions `λ` with `|λ| ≤ 12` (including `∅`): `272`.
- All `L ∈ [0, 15]`.

Calibration (from script):
- `residue(K₂) = 1`, `steps(K₂) = 1`.
- Cycle checks: `residue(C_n) = ceil(n/3)` for `n = 3…9`.
  - `n=3: 1`, `n=4: 2`, `n=5: 2`, `n=6: 2`, `n=7: 3`, `n=8: 3`, `n=9: 3`.

Refutation table summary:
- In-hypothesis pairs (`λ ≠ []`, `L ≥ λ₁`): `3125`
- In-hypothesis mismatches: `0`
- Outside-hypothesis pairs (`λ ≠ []`, `L < λ₁`): `1211`
- Outside-hypothesis mismatches: `462`

Boundary samples from script:
- `λ = []` (not admissible in lemma): `L=2`, multiset `[2]^3` takes `2` steps.
- `λ=[2]`: `s₀([2]) = 2`; for `L=2..10`, observed steps are `2,3,4,5,6,7,8,9,10` exactly `L`.
- `L=λ₁` sample: `λ=[3]`, `L=3`, observed `3`, formula `3`.
- `L=λ₁-1` sample: `λ=[3]`, `L=2` (out of scope), observed `1`, formula gives `2`; the statement does not claim this case.

- All outside-hypothesis mismatches are listed in the `.out` file for traceability; no in-hypothesis mismatches were found.

## 2) Joint table

- **J-TAIL-BLOCK**: CLEAN
  - The proof’s tie-break statement is correct on the checked family: starting from `[t]^{t+1} ∪ λ` with `t > λ₁`, every non-head `t` entry is among the top-`t` non-head entries, and all `λ` entries are `< t`; block-update gives `[t-1]^t ∪ λ`.

- **J-TAIL-IND**: CLEAN
  - Loop and arithmetic are consistent: iterating from `t=L` down to `λ₁` takes exactly `L-λ₁` steps and leaves `[λ₁]^{λ₁+1} ∪ λ`. The code check confirms all checked cases.

- **J-TAIL-EQUIV**: CLEAN
  - Under `L ≥ λ₁`, equivalence is algebraic and immediate:
    - `clear in exactly L` iff `(L-λ₁)+s₀(λ) = L` iff `s₀(λ)=λ₁`.
    - `λ`-only dependence is only after substituting the fixed hypothesis.

- **J-TAIL-DEF**: CLEAN
  - `s₀(λ)` definition and `residueAux` spec used in the check are consistent. Script uses the exact HH step with list sorted descending and `d`-truncated decrements.
  - `steps` counted exactly as HH steps (head-`>0` applications); direct runs from `[L]^{L+1}∪λ` are the tested target.

- **J-FAN5**: CLEAN
  - `s₀([2]) = 2` from `steps([2]^3 ∪ [2]) = steps([2,2,2,2])`.
  - For every checked `L ≥ 2`, `steps([L]^{L+1} ∪ [2]) = L`, matching the stated claim.

- **J-SCOPE**: CLEAN
  - The reviewed text is used as a multiset lemma inside graph-theoretic context; the internal use only requires the reduced multiset form and does not introduce extra assumptions in this step.

## 3) Defects

No proof defects found for the reviewed statement under its explicit hypotheses.

- **Quoted statement under stress check:** "If `L ≥ λ₁` then the number of further Havel–Hakimi steps is `(L−λ₁)+s₀(λ)`."
- **Outcome:** verified by exhaustive computation for the required box.
- **Smallest counterexample attempt:** none in-hypothesis.
- **Repair needed:** no.
- **Does the CONCLUSION survive:** yes.
- **Label:** **BOOKKEEPING/MATHEMATICS** — no defect.

## 4) Repair-species probes

1. **Statement riders are separate proof obligations**
   - `consequently` sentence checked as separate obligation.
   - Valid under `L ≥ λ₁`; no extra arithmetic gap found.

2. **Scope-widening contagion**
   - `does not depend on L` is interpreted as `under L ≥ λ₁`, which is consistent with the proof and with the checked code.
   - Boundary checks show off-hypothesis cases do not invalidate the in-hypothesis result.

3. **Box-vs-branch artifact**
   - The script computes all checked finite pairs independently; no `all-L` conclusion is inferred from a smaller non-exhaustive branch.

## 5) T12 controls

1. **Counterfactual availability**
   - Control control checked: `[L]^{L+1} ∪ λ` with `L < λ₁` is not covered by the lemma hypothesis.
   - Direct counterexample on control: `λ=(2,)`, `L=0` gives observed `1` vs formula `0` (outside the scope), confirming boundary sensitivity.

2. **Witness validation**
   - Every simulated witness is of the exact target form `[L]^{L+1} ∪ λ` with nonincreasing integer entries (`λ` a partition), satisfying the multiset setup directly.

3. **Non-vacuity**
   - Non-vacuous instances exist (`λ=[2], L=2`, `λ=[2], L=5`, etc.) and verify the formulas exactly.

## 6) What I could NOT check

- Could not invoke the `global-memory` recall tool in this environment (no usable `recall_presets` endpoint was exposed), so AGENTS-mandated recall confirmation output was not retrievable.
- No non-restricted files were consulted per task restriction.

## 7) Out-of-scope, noticed anyway

- None with confidence from this pass.
