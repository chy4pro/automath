# sidon30 CI — run 37057713673  (completed / failure, commit 0ea8672)

## Errors and warnings with context
```
342:✖ [8722/8729] Building Sidon30.RampGramEnergy (5.0s)
343-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
344:error: Sidon30/RampGramEnergy.lean:59:4: omega could not prove the goal:
345-a possible counterexample may satisfy the constraints
346-  b ≥ 0
347-  a ≥ 0
348-  a - b ≥ 1
349-where
350- a := ↑j
351- b := ↑i
352-warning: Sidon30/RampGramEnergy.lean:163:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
353-warning: Sidon30/RampGramEnergy.lean:166:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
354-warning: Sidon30/RampGramEnergy.lean:204:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
355-warning: Sidon30/RampGramEnergy.lean:210:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
356-✔ [8724/8729] Built Sidon30.WeightedCount (5.8s)
357-✔ [8725/8729] Built Sidon30.PairCount (6.3s)
358-✔ [8726/8729] Built Sidon30.FinalReduction (6.0s)
--
368:error: build failed
369-##[error]Process completed with exit code 1.
370-##[group]Run actions/upload-artifact@v4
371-with:
372-  name: build-log
373-  path: lean/sidon30/build.log
374-  if-no-files-found: warn
375-  compression-level: 6
376-  overwrite: false
377-  include-hidden-files: false
378-##[endgroup]
379-(node:2990) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
380-(Use `node --trace-deprecation ...` to show where the warning was created)
381-With the provided path, there will be 1 file uploaded
382-Artifact name is valid!
```
## Summary
```
✖ [8722/8729] Building Sidon30.RampGramEnergy (5.0s)
error: Sidon30/RampGramEnergy.lean:59:4: omega could not prove the goal:
error: build failed
```
