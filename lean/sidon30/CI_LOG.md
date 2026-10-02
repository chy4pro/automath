# sidon30 CI — run 37055538640  (completed / failure, commit 1de2678)

## Errors and warnings with context
```
267:✖ [8707/8719] Building Sidon30.RenewalRecurrence (6.8s)
268-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
269:error: Sidon30/RenewalRecurrence.lean:33:2: `simp` made no progress
270-warning: Sidon30/RenewalRecurrence.lean:45:25: `if_neg` has been deprecated: Use `ite_eq_right` instead
271-warning: Sidon30/RenewalRecurrence.lean:91:29: `if_neg` has been deprecated: Use `ite_eq_right` instead
272-warning: Sidon30/RenewalRecurrence.lean:106:25: `if_pos` has been deprecated: Use `ite_eq_left` instead
273-✔ [8708/8719] Built Sidon30.FiniteEnergyCS (7.3s)
274-⚠ [8709/8719] Built Sidon30.RampWeights (8.1s)
275-warning: Sidon30/RampWeights.lean:32:25: `if_pos` has been deprecated: Use `ite_eq_left` instead
276-warning: Sidon30/RampWeights.lean:36:25: `if_neg` has been deprecated: Use `ite_eq_right` instead
277-warning: Sidon30/RampWeights.lean:126:35: this tactic is never executed
278-
279-Note: This linter can be disabled with `set_option linter.unreachableTactic false`
280-warning: Sidon30/RampWeights.lean:126:35: Unused tactic linter: `ring` does nothing
281-
282-Note: This linter can be disabled with `set_option linter.unusedTactic false`
283-warning: Sidon30/RampWeights.lean:147:31: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
--
317:error: build failed
318-##[error]Process completed with exit code 1.
319-##[group]Run actions/upload-artifact@v4
320-with:
321-  name: build-log
322-  path: lean/sidon30/build.log
323-  if-no-files-found: warn
324-  compression-level: 6
325-  overwrite: false
326-  include-hidden-files: false
327-##[endgroup]
328-(node:3021) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
329-(Use `node --trace-deprecation ...` to show where the warning was created)
330-With the provided path, there will be 1 file uploaded
331-Artifact name is valid!
```
## Summary
```
✖ [8707/8719] Building Sidon30.RenewalRecurrence (6.8s)
error: Sidon30/RenewalRecurrence.lean:33:2: `simp` made no progress
error: build failed
```
