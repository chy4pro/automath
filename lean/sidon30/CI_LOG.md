# sidon30 CI — run 37074847215  (completed / failure, commit 7ab3dca)

## Errors and warnings with context
```
345:✖ [8729/8754] Building Sidon30.SonarFinal (7.1s)
346-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
347-warning: Sidon30/SonarFinal.lean:46:2: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
348-
349-Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
350-warning: Sidon30/SonarFinal.lean:55:2: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
351-
352-Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
353:error: Sidon30/SonarFinal.lean:106:35: Invalid field `mp`: The environment does not contain `Function.mp`, so it is not possible to project the field `mp` from an expression
354-  mul_le_mul_right ?m.860
355-of type
356-  ∀ (a : ?m.854), a * ?m.858 ≤ a * ?m.859
357:error: Sidon30/SonarFinal.lean:106:28: Application type mismatch: The argument
358-  hUpos
359-has type
360-  0 < U
361-but is expected to have type
362-  ?m.858 ≤ ?m.859
363-in the application
364-  mul_le_mul_right hUpos
365:error: Sidon30/SonarFinal.lean:112:10: failed to synthesize instance of type class
366-  MulLeftStrictMono ℝ
367-
368-Hint: Type class instance resolution failures can be inspected with the `set_option trace.Meta.synthInstance true` command.
369-✔ [8730/8754] Built Sidon30.FinalReduction (6.7s)
370-⚠ [8731/8754] Built Sidon30.CorrectionFiniteMass (5.4s)
371-warning: Sidon30/CorrectionFiniteMass.lean:22:6: `if_pos` has been deprecated: Use `ite_eq_left` instead
372-warning: Sidon30/CorrectionFiniteMass.lean:42:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
373-warning: Sidon30/CorrectionFiniteMass.lean:42:32: `if_pos` has been deprecated: Use `ite_eq_left` instead
374-warning: Sidon30/CorrectionFiniteMass.lean:44:19: `if_pos` has been deprecated: Use `ite_eq_left` instead
375-warning: Sidon30/CorrectionFiniteMass.lean:44:35: `if_neg` has been deprecated: Use `ite_eq_right` instead
376-warning: Sidon30/CorrectionFiniteMass.lean:55:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
377-warning: Sidon30/CorrectionFiniteMass.lean:60:19: `if_pos` has been deprecated: Use `ite_eq_left` instead
378-⚠ [8732/8754] Built Sidon30.RampGramEnergy (5.9s)
379-warning: Sidon30/RampGramEnergy.lean:164:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
--
486:error: build failed
487-##[error]Process completed with exit code 1.
488-##[group]Run actions/upload-artifact@v4
489-with:
490-  name: build-log
491-  path: lean/sidon30/build.log
492-  if-no-files-found: warn
493-  compression-level: 6
494-  overwrite: false
495-  include-hidden-files: false
496-##[endgroup]
497-(node:3005) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
498-(Use `node --trace-deprecation ...` to show where the warning was created)
499-With the provided path, there will be 1 file uploaded
500-Artifact name is valid!
```
## Summary
```
✖ [8729/8754] Building Sidon30.SonarFinal (7.1s)
error: Sidon30/SonarFinal.lean:106:35: Invalid field `mp`: The environment does not contain `Function.mp`, so it is not possible to project the field `mp` from an expression
error: Sidon30/SonarFinal.lean:106:28: Application type mismatch: The argument
error: Sidon30/SonarFinal.lean:112:10: failed to synthesize instance of type class
error: build failed
```
