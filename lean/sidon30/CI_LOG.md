# sidon30 CI — run 37057054792  (completed / failure, commit 91a49ac)

## Errors and warnings with context
```
313:✖ [8713/8729] Building Sidon30.RenewalBlockMatrix (5.3s)
314-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
315-warning: Sidon30/RenewalBlockMatrix.lean:107:6: `if_pos` has been deprecated: Use `ite_eq_left` instead
316-warning: Sidon30/RenewalBlockMatrix.lean:107:40: `if_pos` has been deprecated: Use `ite_eq_left` instead
317-warning: Sidon30/RenewalBlockMatrix.lean:108:6: `if_neg` has been deprecated: Use `ite_eq_right` instead
318-warning: Sidon30/RenewalBlockMatrix.lean:113:6: `if_neg` has been deprecated: Use `ite_eq_right` instead
319-warning: Sidon30/RenewalBlockMatrix.lean:113:42: `if_pos` has been deprecated: Use `ite_eq_left` instead
320-warning: Sidon30/RenewalBlockMatrix.lean:114:6: `if_pos` has been deprecated: Use `ite_eq_left` instead
321-info: Sidon30/RenewalBlockMatrix.lean:117:4: Try this:
322-  [apply] ring_nf
323-  
324-  The `ring` tactic failed to close the goal. Use `ring_nf` to obtain a normal form.
325-    
326-  Note that `ring` works primarily in *commutative* rings. If you have a noncommutative ring, abelian group or module, consider using `noncomm_ring`, `abel` or `module` instead.
327:error: Sidon30/RenewalBlockMatrix.lean:111:2: unsolved goals
328-case inr.inl
329-T i : ℕ
330-hi : 1 ≤ i
331-hexp : i - 1 + 1 = i
332-hpow : (1 + 1 / ↑T) ^ i = (1 + 1 / ↑T) ^ (i - 1) * (1 + 1 / ↑T)
333-hj : 1 ≤ i
334-⊢ -(↑T)⁻¹ + (↑T)⁻¹ * (1 + (↑T)⁻¹) ^ (i - 1) + (↑T)⁻¹ ^ 2 * (1 + (↑T)⁻¹) ^ (i - 1) =
335-    (↑T)⁻¹ * (1 + (↑T)⁻¹) ^ (i - 1) + (↑T)⁻¹ ^ 2 * (1 + (↑T)⁻¹) ^ (i - 1) - if True then (↑T)⁻¹ else 0
336-warning: Sidon30/RenewalBlockMatrix.lean:120:6: `if_neg` has been deprecated: Use `ite_eq_right` instead
337-warning: Sidon30/RenewalBlockMatrix.lean:120:42: `if_neg` has been deprecated: Use `ite_eq_right` instead
338-warning: Sidon30/RenewalBlockMatrix.lean:121:6: `if_neg` has been deprecated: Use `ite_eq_right` instead
339-warning: Sidon30/RenewalBlockMatrix.lean:114:6: This simp argument is unused:
340-  if_pos (show i = i from rfl)
341-
--
361:✖ [8715/8729] Building Sidon30.RenewalFirstBlock (4.8s)
362-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
363-warning: Sidon30/RenewalFirstBlock.lean:20:6: `if_pos` has been deprecated: Use `ite_eq_left` instead
364:error: Sidon30/RenewalFirstBlock.lean:49:8: `simp` made no progress
365:✖ [8716/8729] Building Sidon30.RenewalRampIdentity (5.3s)
366-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
367-warning: Sidon30/RenewalRampIdentity.lean:17:8: `if_pos` has been deprecated: Use `ite_eq_left` instead
368-warning: Sidon30/RenewalRampIdentity.lean:27:8: `if_neg` has been deprecated: Use `ite_eq_right` instead
369-warning: Sidon30/RenewalRampIdentity.lean:29:58: Used `tac1 <;> tac2` where `(tac1; tac2)` would suffice
370-
371-Note: This linter can be disabled with `set_option linter.unnecessarySeqFocus false`
372:error: Sidon30/RenewalRampIdentity.lean:40:4: `simp` made no progress
373-warning: Sidon30/RenewalRampIdentity.lean:63:16: `if_pos` has been deprecated: Use `ite_eq_left` instead
374-warning: Sidon30/RenewalRampIdentity.lean:63:28: `if_pos` has been deprecated: Use `ite_eq_left` instead
375-warning: Sidon30/RenewalRampIdentity.lean:66:16: `if_neg` has been deprecated: Use `ite_eq_right` instead
376-warning: Sidon30/RenewalRampIdentity.lean:66:28: `if_neg` has been deprecated: Use `ite_eq_right` instead
377-warning: Sidon30/RenewalRampIdentity.lean:125:8: `if_pos` has been deprecated: Use `ite_eq_left` instead
378-warning: Sidon30/RenewalRampIdentity.lean:128:8: `if_neg` has been deprecated: Use `ite_eq_right` instead
379-✔ [8717/8729] Built Sidon30.IntegerScaleAndTail (7.9s)
380-✔ [8718/8729] Built Sidon30.ShiftWindow (5.8s)
381:✖ [8719/8729] Building Sidon30.CorrelationFacts (6.0s)
382-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
383-warning: Sidon30/CorrelationFacts.lean:28:8: `if_pos` has been deprecated: Use `ite_eq_left` instead
384-warning: Sidon30/CorrelationFacts.lean:34:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
385-warning: Sidon30/CorrelationFacts.lean:35:16: `if_pos` has been deprecated: Use `ite_eq_left` instead
386-warning: Sidon30/CorrelationFacts.lean:36:8: `if_neg` has been deprecated: Use `ite_eq_right` instead
387-warning: Sidon30/CorrelationFacts.lean:44:15: `if_neg` has been deprecated: Use `ite_eq_right` instead
388-warning: Sidon30/CorrelationFacts.lean:60:15: `if_pos` has been deprecated: Use `ite_eq_left` instead
389-warning: Sidon30/CorrelationFacts.lean:60:41: `if_pos` has been deprecated: Use `ite_eq_left` instead
390-warning: Sidon30/CorrelationFacts.lean:61:8: `if_neg` has been deprecated: Use `ite_eq_right` instead
391-warning: Sidon30/CorrelationFacts.lean:68:15: `if_pos` has been deprecated: Use `ite_eq_left` instead
392-warning: Sidon30/CorrelationFacts.lean:68:41: `if_pos` has been deprecated: Use `ite_eq_left` instead
393-warning: Sidon30/CorrelationFacts.lean:69:8: `if_neg` has been deprecated: Use `ite_eq_right` instead
394-warning: Sidon30/CorrelationFacts.lean:92:15: `if_pos` has been deprecated: Use `ite_eq_left` instead
395-warning: Sidon30/CorrelationFacts.lean:92:29: `if_pos` has been deprecated: Use `ite_eq_left` instead
--
398:error: Sidon30/CorrelationFacts.lean:119:6: Tactic `rewrite` failed: motive is not type correct:
399-  fun _a ↦
400-    (if _a then rampWeight T j * rampWeight T i else 0) = if ↑j - ↑i = d then rampWeight T i * rampWeight T j else 0
401-Error: Application type mismatch: The argument
402-  (↑i - ↑j).instDecidableEq (-d)
403-has type
404-  Decidable (↑i - ↑j = -d)
405-but is expected to have type
406-  Decidable _a
407-in the application
408-  @ite ℝ _a ((↑i - ↑j).instDecidableEq (-d))
409-
410-Explanation: The rewrite tactic rewrites an expression 'e' using an equality 'a = b' by the following process. First, it looks for all 'a' in 'e'. Second, it tries to abstract these occurrences of 'a' to create a function 'm := fun _a => ...', called the *
411-
412-Possible solutions: use rewrite's 'occs' configuration option to limit which occurrences are rewritten, or use 'simp' or 'conv' mode, which have strategies for certain kinds of dependencies (these tactics can handle proofs and 'Decidable' instances whose t
--
423:error: Sidon30/CorrelationFacts.lean:161:10: Tactic `rewrite` failed: motive is not type correct:
424-  fun _a ↦ (if _a then rampWeight T j ^ 2 else 0) = if ↑i = ↑j - d then rampWeight T j ^ 2 else 0
425-Error: Application type mismatch: The argument
426-  (↑j).instDecidableEq (↑i + d)
427-has type
428-  Decidable (↑j = ↑i + d)
429-but is expected to have type
430-  Decidable _a
431-in the application
432-  @ite ℝ _a ((↑j).instDecidableEq (↑i + d))
433-
434-Explanation: The rewrite tactic rewrites an expression 'e' using an equality 'a = b' by the following process. First, it looks for all 'a' in 'e'. Second, it tries to abstract these occurrences of 'a' to create a function 'm := fun _a => ...', called the *
435-
436-Possible solutions: use rewrite's 'occs' configuration option to limit which occurrences are rewritten, or use 'simp' or 'conv' mode, which have strategies for certain kinds of dependencies (these tactics can handle proofs and 'Decidable' instances whose t
437-
--
452:✖ [8726/8729] Building Sidon30.FinalReduction (4.2s)
453-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
454:error: Sidon30/FinalReduction.lean:50:4: not a positivity goal
455-⚠ [8727/8729] Built Sidon30.SidonEnergyUpper (3.3s)
456-warning: Sidon30/SidonEnergyUpper.lean:38:55: `if_true` has been deprecated: Use `ite_true` instead
457-warning: Sidon30/SidonEnergyUpper.lean:38:64: `if_false` has been deprecated: Use `ite_false` instead
458-warning: Sidon30/SidonEnergyUpper.lean:43:55: `if_true` has been deprecated: Use `ite_true` instead
459-warning: Sidon30/SidonEnergyUpper.lean:43:64: `if_false` has been deprecated: Use `ite_false` instead
460-warning: Sidon30/SidonEnergyUpper.lean:59:20: `if_pos` has been deprecated: Use `ite_eq_left` instead
461-warning: Sidon30/SidonEnergyUpper.lean:64:38: `if_false` has been deprecated: Use `ite_false` instead
462-Some required targets logged failures:
463-- Sidon30.RenewalBlockMatrix
464-- Sidon30.RenewalFirstBlock
465-- Sidon30.RenewalRampIdentity
466-- Sidon30.CorrelationFacts
467-- Sidon30.FinalReduction
468:error: build failed
469-##[error]Process completed with exit code 1.
470-##[group]Run actions/upload-artifact@v4
471-with:
472-  name: build-log
473-  path: lean/sidon30/build.log
474-  if-no-files-found: warn
475-  compression-level: 6
476-  overwrite: false
477-  include-hidden-files: false
478-##[endgroup]
479-(node:2799) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
480-(Use `node --trace-deprecation ...` to show where the warning was created)
481-With the provided path, there will be 1 file uploaded
482-Artifact name is valid!
```
## Summary
```
✖ [8713/8729] Building Sidon30.RenewalBlockMatrix (5.3s)
error: Sidon30/RenewalBlockMatrix.lean:111:2: unsolved goals
✖ [8715/8729] Building Sidon30.RenewalFirstBlock (4.8s)
error: Sidon30/RenewalFirstBlock.lean:49:8: `simp` made no progress
✖ [8716/8729] Building Sidon30.RenewalRampIdentity (5.3s)
error: Sidon30/RenewalRampIdentity.lean:40:4: `simp` made no progress
✖ [8719/8729] Building Sidon30.CorrelationFacts (6.0s)
error: Sidon30/CorrelationFacts.lean:119:6: Tactic `rewrite` failed: motive is not type correct:
error: Sidon30/CorrelationFacts.lean:161:10: Tactic `rewrite` failed: motive is not type correct:
✖ [8726/8729] Building Sidon30.FinalReduction (4.2s)
error: Sidon30/FinalReduction.lean:50:4: not a positivity goal
error: build failed
```
