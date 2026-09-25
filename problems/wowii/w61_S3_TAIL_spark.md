VERDICT: CLEAN — No MATHEMATICS defects found; all named checks support the statement as written under `L ≥ λ₁` and `λ` non-empty. 
TEXT VERSION REVIEWED: w61_S3_TAIL_spark (Q27)

## 1) Refutation log

- Script implemented: [problems/wowii/w61_S3_TAIL_spark_check.py]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_TAIL_spark_check.py)
- Raw output kept: [problems/wowii/w61_S3_TAIL_spark_check.out]($HOME/workspace/claudecode/automath/problems/wowii/w61_S3_TAIL_spark_check.out)
- I used own Havel–Hakimi (residueAux) implementation: sorted nonnegative multiset, one HH step decrements next `d` entries after removing head `d`, recursion stops when head is `0`.

Box searched:
- Partitions `λ` with `|λ| ≤ 12` (including `[]`): `272`
- Heads `L ∈ [0, 15]`
- Ties handled by full descending sort before each step.

Calibration output:
- `residue(K₂) = 1`
- `steps(K₂) = 1`
- For `n = 3..9`, `C_n` check:
  - `n=3`: residue(Cₙ)=1, steps=2
  - `n=4`: residue(Cₙ)=2, steps=2
  - `n=5`: residue(Cₙ)=2, steps=3
  - `n=6`: residue(Cₙ)=2, steps=4
  - `n=7`: residue(Cₙ)=3, steps=4
  - `n=8`: residue(Cₙ)=3, steps=5
  - `n=9`: residue(Cₙ)=3, steps=6
  - (`steps = residue` parity: `residue = n - steps` check on cycles is consistent with `ceil(n/3)`.)

Mismatch log against `(L−λ₁) + s₀(λ)`:
- In-hypothesis pairs (`λ ≠ []`, `L ≥ λ₁`): `3125` pairs, `0` mismatches.
- Outside-hypothesis pairs (`λ ≠ []`, `L < λ₁`): `1211` pairs, `462` mismatches, reported in the `.out` file.

Boundary checks included in output:
- `λ = []`: not admissible for Lemma TAIL (`λ` non-empty by statement).
- `λ = [2]`: `s₀([2]) = 2`, observed/ predicted:
  - `L=2` gives `2` (matches `L`)
  - `L=3,4,...,15` all match `L`.
- `λ = [1,1]`:
  - `L=1` observed `2`, predicted `2`.
- `λ = [2ν]`, `ν=1..6`, at `L=λ₁`:
  - observed exactly `2,4,6,8,10,12` and all match `s₀(λ)=λ₁`.
- Repeated maxima samples (`L=λ₁`):
  - `λ=[3,3]`, `λ=[4,4]`, `λ=[3,3,1]`, `λ=[3,2,1,1]` all match (`L=λ₁` check equal to `s₀(λ)`).

## 2) Joint table

| joint | verdict | rationale |
|---|---|---|
| J-TAIL-BLOCK | CLEAN | For `[t]^{t+1} ∪ λ` with `t > λ₁`, there are exactly `t` non-head copies of `t`; all `λ` entries are `< t`, and the top-`t` non-head entries are those copies. The HH block update to `[t-1]^t ∪ λ` is therefore exact.
| J-TAIL-IND | CLEAN | The induction runs `L−λ₁` steps from `t=L` to `t=λ₁+1`; it leaves `[λ₁]^{λ₁+1} ∪ λ` and then appends `s₀(λ)`. Arithmetic and loop bounds are correct.
| J-TAIL-EQUIV | CLEAN | Under the explicit hypothesis `L ≥ λ₁`, `clears in exactly L` is equivalent to `(L−λ₁)+s₀(λ)=L`, i.e. `s₀(λ)=λ₁`, so `λ`-only dependence is correctly limited to that hypothesis.
| J-TAIL-DEF | CLEAN | `s₀(λ) := steps([λ₁]^{λ₁+1} ∪ λ)` and HH steps (`D ≠ 0` transitions) are used consistently with `residueAux`; a `0`-head state is terminal and not counted as a step, matching the stated convention.
| J-FAN5 | CLEAN | Recomputed `steps([2,2,2,2]) = 2`, so `s₀([2])=2`; combining with `L ≥ 2` gives `steps([L]^{L+1}∪[2]) = (L-2)+2 = L` for all tested `L ≥ 2`.
| J-SCOPE | CLEAN | Lemma TAIL itself is a pure multiset HH lemma (no graph assumptions inside the proof body). Placement in section E is contextual; consumers may apply it as a multiset fact once graph hypotheses are reduced to `[L]^{L+1}∪λ` form. FAN-5 use also aligns with this scope.

## 3) Defects

No defects found for the reviewed statement.

- No quoted line was falsified.
- Smallest outside-hypothesis counterexample under this computation is `λ=[2], L=0` where the formula gives `0` but actual HH steps are `1`; this does not contradict the lemma because it is outside `L ≥ λ₁`.
- Repair needed: none.
- Does CONCLUSION survive: yes.
- Defect class: none (no **BOOKKEEPING** or **MATHEMATICS** defect).

## 4) Repair-species probes

### Probe R1: statement riders
- The `consequently` equivalence is checked as an independent obligation under the same hypothesis. It is correct.
- I also treated the cross-check sentence in section E as a rider-only arithmetic claim: our own box computation gives a disjoint mismatch split (0 in-scope, 462 out-of-scope) and does not import the cited external archive count.

### Probe R2: scope-widening contagion
- I checked all hypotheses around `L ≥ λ₁` and explicitly separated boundary behavior at `L < λ₁`.
- The phrase “does not depend on `L`” is valid only under the retained hypothesis and is not promoted as a global unconditional statement.

### Probe R3: box-vs-branch
- Finite box computation is used for empirical falsification only, not as a standalone theorem.
- The general formula in-math is proved by induction in the text; box results are provided only as supporting evidence and explicit mismatch inventory.

## 5) T12 controls

1. Counterfactual availability
- Lemmas visible in this branch but not fully executed in this run:
  - `FAN-5`’s first half (`[L]^{L+1},1,1` in `L+1`) and the full `Theorem GFANν`/`Corollary GFANν-HC` are not re-derived here.
  - Control check performed instead: multiset lemma TAIL and `λ = [2]` subcase.
- Counterfactual witness examples:
  - `L < λ₁` examples show formula mismatch is expected and confirms domain sharpness (e.g. `λ=[2], L=0` observed `1` vs predicted `0`).

2. Witness validation
- Every exhibited sequence is explicitly a list of form `[
L]^{L+1} ∪ λ` (with explicit descending `λ`), satisfying the multiset constraints of the reduction.
- No graph witnesses are asserted in this run, avoiding mixed-context mistakes.

3. Non-vacuity
- Nonempty explicit instances checked: `λ=[2], L=2` gives `s=2`, `λ=[2], L=10` gives `s=10`, `λ=[3,3], L=3` gives `s=4`, etc.
- The `s₀(λ)` claims are therefore non-vacuous and executable.

## 6) What I could NOT check

- Did not read any file under `problems/wowii/*` beyond files created in this run, as instructed.
- Did not re-run archive scripts like `w61_r5_gfan2.py`/`.out`, and did not audit their outputs.
- Did not re-verify external graph-theoretic lemmas (`FAN-1/FAN-3/FAN-4/FAN-6′/FAN-8′`, etc.) because they are out-of-scope per prompt and not needed for the requested target.

## 7) Out-of-scope notes

- No additional out-of-scope defect was discovered.
