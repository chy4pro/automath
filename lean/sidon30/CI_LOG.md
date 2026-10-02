# sidon30 CI — run 37075703586  (completed / failure, commit 89bb6ee)

## Errors and warnings with context
```
373:✖ [8730/8759] Building Sidon30.DifferenceTriangleScale (11s)
374-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
375:error: Sidon30/DifferenceTriangleScale.lean:154:2: linarith failed to find a contradiction
376-n m : ℕ
377-x : ℝ
378-hn : 1 ≤ n
379-hx : 120 ≤ x
380-hx4m : x ^ 4 * ↑n = ↑m
381-hxpos : 0 < x
382-hsmall : x * (3 / 4) ^ (m / dtsIntegerScale n x) < 1 / 100
383-hT : ↑(dtsIntegerScale n x) / ↑n ≤ 3 / 2 * x ^ 3
384-hp : 0 ≤ (3 / 4) ^ (m / dtsIntegerScale n x)
385-hupper :
386-  ↑(dtsIntegerScale n x) / ↑n * (29 * (3 / 4) ^ (m / dtsIntegerScale n x)) ≤
387-    3 / 2 * x ^ 3 * (29 * (3 / 4) ^ (m / dtsIntegerScale n x))
388-hmul : 87 / 2 * x ^ 2 * (x * (3 / 4) ^ (m / dtsIntegerScale n x)) < 87 / 2 * x ^ 2 * (1 / 100)
389-a✝ : 87 / 200 * x ^ 2 ≤ 29 * ↑(dtsIntegerScale n x) / ↑n * (3 / 4) ^ (m / dtsIntegerScale n x)
--
392:error: Sidon30/DifferenceTriangleScale.lean:194:2: Type mismatch
393-  add_le_add_right hb ?m.268
394-has type
395-  ?m.268 + (↑m + 2 / 3 * (↑(dtsIntegerScale n x) - 1)) / ↑n ≤ ?m.268 + (x ^ 4 + sidonGamma * x ^ 3)
396-but is expected to have type
397-  (↑m + 2 / 3 * (↑(dtsIntegerScale n x) - 1)) / ↑n + dtsScaleError n m x ≤
398-    x ^ 4 + sidonGamma * x ^ 3 + dtsScaleError n m x
399-⚠ [8731/8759] Built Sidon30.RampGramEnergy (11s)
400-warning: Sidon30/RampGramEnergy.lean:164:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
401-warning: Sidon30/RampGramEnergy.lean:167:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
402-warning: Sidon30/RampGramEnergy.lean:205:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
403-warning: Sidon30/RampGramEnergy.lean:211:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
404-⚠ [8732/8759] Built Sidon30.GThinScale (15s)
405-warning: Sidon30/GThinScale.lean:36:8: this tactic is never executed
406-
--
519:error: build failed
520-##[error]Process completed with exit code 1.
521-##[group]Run actions/upload-artifact@v4
522-with:
523-  name: build-log
524-  path: lean/sidon30/build.log
525-  if-no-files-found: warn
526-  compression-level: 6
527-  overwrite: false
528-  include-hidden-files: false
529-##[endgroup]
530-(node:3366) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
531-(Use `node --trace-deprecation ...` to show where the warning was created)
532-With the provided path, there will be 1 file uploaded
533-Artifact name is valid!
```
## Summary
```
✖ [8730/8759] Building Sidon30.DifferenceTriangleScale (11s)
error: Sidon30/DifferenceTriangleScale.lean:154:2: linarith failed to find a contradiction
error: Sidon30/DifferenceTriangleScale.lean:194:2: Type mismatch
error: build failed
```
