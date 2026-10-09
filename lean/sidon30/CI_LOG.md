# sidon30 CI — run 37977887526  (completed / failure, commit 940f621)

## Errors and warnings with context
```
361:✖ [8719/8759] Building Sidon30.IntegerScaleAndTail (16s)
362-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
363:error: Sidon30/IntegerScaleAndTail.lean:332:2: linarith failed to find a contradiction
364-r : ℕ
365-hr : 32 ≤ r
366-hpower : (3 / 4) ^ 32 < 1 / 9900
367-hbase : (2 * ↑r + 5) * (3 / 4) ^ r ≤ 127858393030777029 / 18446744073709551616
368-a✝ : 667 / 3300 ≤ 29 * sidonTailEnvelopeSharp r
369-⊢ False
370-failed
371-✔ [8720/8759] Built Sidon30.DifferenceTriangleStatement (6.5s)
372-✔ [8721/8759] Built Sidon30.TransferStatement (6.7s)
373-⚠ [8722/8759] Built Sidon30.CorrelationFacts (8.5s)
374-warning: Sidon30/CorrelationFacts.lean:28:8: `if_pos` has been deprecated: Use `ite_eq_left` instead
375-warning: Sidon30/CorrelationFacts.lean:34:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
376-warning: Sidon30/CorrelationFacts.lean:35:16: `if_pos` has been deprecated: Use `ite_eq_left` instead
377-warning: Sidon30/CorrelationFacts.lean:36:8: `if_neg` has been deprecated: Use `ite_eq_right` instead
--
507:error: build failed
508-##[error]Process completed with exit code 1.
509-##[group]Run actions/upload-artifact@v4
510-with:
511-  name: build-log
512-  path: lean/sidon30/build.log
513-  if-no-files-found: warn
514-  compression-level: 6
515-  overwrite: false
516-  include-hidden-files: false
517-##[endgroup]
518-(node:3331) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
519-(Use `node --trace-deprecation ...` to show where the warning was created)
520-With the provided path, there will be 1 file uploaded
521-Artifact name is valid!
```
## Summary
```
✖ [8719/8759] Building Sidon30.IntegerScaleAndTail (16s)
error: Sidon30/IntegerScaleAndTail.lean:332:2: linarith failed to find a contradiction
error: build failed
```

## AUT-78 run history

| Run | Commit | Result | Evidence / repair |
| --- | --- | --- | --- |
| [37977887526](https://github.com/chy4pro/automath/actions/runs/37977887526) | `940f621cad8811eec09122f6b082b0459e2625c3` | failure | Build: one opaque-envelope goal in IntegerScaleAndTail; Axioms skipped. Repair: unfold sidonTailEnvelopeSharp before nlinarith. |
