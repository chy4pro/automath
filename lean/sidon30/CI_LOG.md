# sidon30 CI — run 37059252632  (completed / failure, commit fbc8b92)

## Errors and warnings with context
```
328:✖ [8722/8737] Building Sidon30.RenewalBlockContraction (6.5s)
329-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
330-warning: Sidon30/RenewalBlockContraction.lean:36:28: `if_pos` has been deprecated: Use `ite_eq_left` instead
331-warning: Sidon30/RenewalBlockContraction.lean:53:28: `if_neg` has been deprecated: Use `ite_eq_right` instead
332-warning: Sidon30/RenewalBlockContraction.lean:34:26: this tactic is never executed
333-
334-Note: This linter can be disabled with `set_option linter.unreachableTactic false`
335-warning: Sidon30/RenewalBlockContraction.lean:34:26: Unused tactic linter: `ring` does nothing
336-
337-Note: This linter can be disabled with `set_option linter.unusedTactic false`
338:error: Sidon30/RenewalBlockContraction.lean:128:79: Unknown identifier `j`
339:error: Sidon30/RenewalBlockContraction.lean:130:84: Unknown identifier `j`
340:error: Sidon30/RenewalBlockContraction.lean:146:83: Unknown identifier `j`
341-✔ [8723/8737] Built Sidon30.CorrectionFiniteL1 (5.8s)
342-⚠ [8725/8737] Built Sidon30.CorrectionFiniteMass (5.8s)
343-warning: Sidon30/CorrectionFiniteMass.lean:22:6: `if_pos` has been deprecated: Use `ite_eq_left` instead
344-warning: Sidon30/CorrectionFiniteMass.lean:42:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
345-warning: Sidon30/CorrectionFiniteMass.lean:42:32: `if_pos` has been deprecated: Use `ite_eq_left` instead
346-warning: Sidon30/CorrectionFiniteMass.lean:44:19: `if_pos` has been deprecated: Use `ite_eq_left` instead
347-warning: Sidon30/CorrectionFiniteMass.lean:44:35: `if_neg` has been deprecated: Use `ite_eq_right` instead
348-warning: Sidon30/CorrectionFiniteMass.lean:55:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
349-warning: Sidon30/CorrectionFiniteMass.lean:60:19: `if_pos` has been deprecated: Use `ite_eq_left` instead
350-⚠ [8726/8737] Built Sidon30.RampGramEnergy (5.6s)
351-warning: Sidon30/RampGramEnergy.lean:164:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
352-warning: Sidon30/RampGramEnergy.lean:167:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
353-warning: Sidon30/RampGramEnergy.lean:205:21: `if_neg` has been deprecated: Use `ite_eq_right` instead
354-warning: Sidon30/RampGramEnergy.lean:211:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
--
375:✖ [8732/8737] Building Sidon30.FiniteBoundaryCost (4.2s)
376-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
377-warning: Sidon30/FiniteBoundaryCost.lean:72:34: `if_neg` has been deprecated: Use `ite_eq_right` instead
378-warning: Sidon30/FiniteBoundaryCost.lean:82:30: `if_pos` has been deprecated: Use `ite_eq_left` instead
379-warning: Sidon30/FiniteBoundaryCost.lean:150:34: `if_pos` has been deprecated: Use `ite_eq_left` instead
380-warning: Sidon30/FiniteBoundaryCost.lean:150:70: `if_pos` has been deprecated: Use `ite_eq_left` instead
381-warning: Sidon30/FiniteBoundaryCost.lean:193:19: `if_neg` has been deprecated: Use `ite_eq_right` instead
382-warning: Sidon30/FiniteBoundaryCost.lean:197:14: `if_pos` has been deprecated: Use `ite_eq_left` instead
383:error: Sidon30/FiniteBoundaryCost.lean:330:10: Tactic `split_ifs` failed: no if-then-else conditions to split
384-
385-N T : ℕ
386-hT : 1 ≤ T
387-x : ℤ
388-i : ℕ
389-_hi : i ∈ Finset.range T
390-j : ℕ
391-_hj : j ∈ Finset.range T
392-⊢ 0 ≤ (fun y ↦ if 0 ≤ y ∧ y ≤ ↑N - 1 then 1 else 0) (x + ↑i - ↑j)
393:error: Sidon30/FiniteBoundaryCost.lean:341:6: Tactic `split_ifs` failed: no if-then-else conditions to split
394-
395-N T : ℕ
396-hT : 1 ≤ T
397-x : ℤ
398-hnonneg : 0 ≤ rampDoublePotential T (fun y ↦ if 0 ≤ y ∧ y ≤ ↑N - 1 then 1 else 0) x
399-i : ℕ
400-_hi : i ∈ Finset.range T
401-j : ℕ
402-_hj : j ∈ Finset.range T
403-⊢ (fun y ↦ if 0 ≤ y ∧ y ≤ ↑N - 1 then 1 else 0) (x + ↑i - ↑j) ≤ (fun x ↦ 1) (x + ↑i - ↑j)
404-warning: Sidon30/FiniteBoundaryCost.lean:378:6: `if_neg` has been deprecated: Use `ite_eq_right` instead
405:error: Sidon30/FiniteBoundaryCost.lean:457:8: linarith failed to find a contradiction
406-N T : ℕ
407-hN : 1 ≤ N
408-hT : 1 ≤ T
409-hq : ∀ (n : ℕ), 1 ≤ n → |renewalCorrection T n| ≤ (3 / 4) ^ ((n - 1) / T)
410-herr :
411-  boundaryEnergy N T - ∑ x ∈ boundarySupport N T, boundaryCertificate N T x =
412-    ∑ x ∈ boundarySupport N T \ boundaryWindow N,
413-      boundaryCertificate N T x * (rampDoublePotential T (boundaryCertificate N T) x - 1)
414-x : ℤ
415-_hx : x ∈ boundarySupport N T \ boundaryWindow N
416-hp : |rampDoublePotential T (boundaryCertificate N T) x| ≤ 13
417-ha : |rampDoublePotential T (boundaryCertificate N T) x + -1| ≤ |rampDoublePotential T (boundaryCertificate N T) x| + 1
418-a✝ : 14 < |rampDoublePotential T (boundaryCertificate N T) x - 1|
419-⊢ False
--
421:✖ [8733/8737] Building Sidon30.SidonRampEnergy (3.4s)
422-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
423:error: Sidon30/SidonRampEnergy.lean:62:48: Application type mismatch: The argument
424-  A
425-has type
426-  Finset ℕ
427-but is expected to have type
428-  Finset ℤ
429-in the application
430-  Finset.image (fun a ↦ a) A
431:error: Sidon30/SidonRampEnergy.lean:66:51: unsolved goals
432-A : Finset ℕ
433-x : ℤ
434:⊢ (∃ a ∈ sorry, a = x) ↔ ∃ a ∈ A, ↑a = x
435:warning: Sidon30/SidonRampEnergy.lean:67:13: declaration uses `sorry`
436:warning: Sidon30/SidonRampEnergy.lean:70:8: declaration uses `sorry`
437-warning: Sidon30/SidonRampEnergy.lean:73:2: this tactic is never executed
438-
439-Note: This linter can be disabled with `set_option linter.unreachableTactic false`
440-warning: Sidon30/SidonRampEnergy.lean:74:2: this tactic is never executed
441-
442-Note: This linter can be disabled with `set_option linter.unreachableTactic false`
443-warning: Sidon30/SidonRampEnergy.lean:75:2: this tactic is never executed
444-
445-Note: This linter can be disabled with `set_option linter.unreachableTactic false`
446-warning: Sidon30/SidonRampEnergy.lean:72:2: Unused tactic linter: `apply Finset.card_image_of_injOn` does nothing
447-
448-Note: This linter can be disabled with `set_option linter.unusedTactic false`
449-warning: Sidon30/SidonRampEnergy.lean:73:2: Unused tactic linter: `intro a _ha b _hb hab` does nothing
450-
--
458:error: Sidon30/SidonRampEnergy.lean:89:10: typeclass instance problem is stuck
459-  AddCommMonoid ?m.31
460-
461-Note: Lean will not try to resolve this typeclass instance problem because the type argument to `AddCommMonoid` is a metavariable. This argument must be fully determined before Lean will try to resolve the typeclass.
462-
463-Hint: Adding type annotations and supplying implicit arguments to functions can give Lean more information for typeclass resolution. For example, if you have a variable `x` that you intend to be a `Nat`, but Lean reports it as having an unresolved type lik
464-Some required targets logged failures:
465-- Sidon30.RenewalBlockContraction
466-- Sidon30.FiniteBoundaryCost
467-- Sidon30.SidonRampEnergy
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
479-(node:2975) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
480-(Use `node --trace-deprecation ...` to show where the warning was created)
481-With the provided path, there will be 1 file uploaded
482-Artifact name is valid!
```
## Summary
```
✖ [8722/8737] Building Sidon30.RenewalBlockContraction (6.5s)
error: Sidon30/RenewalBlockContraction.lean:128:79: Unknown identifier `j`
error: Sidon30/RenewalBlockContraction.lean:130:84: Unknown identifier `j`
error: Sidon30/RenewalBlockContraction.lean:146:83: Unknown identifier `j`
✖ [8732/8737] Building Sidon30.FiniteBoundaryCost (4.2s)
error: Sidon30/FiniteBoundaryCost.lean:330:10: Tactic `split_ifs` failed: no if-then-else conditions to split
error: Sidon30/FiniteBoundaryCost.lean:341:6: Tactic `split_ifs` failed: no if-then-else conditions to split
error: Sidon30/FiniteBoundaryCost.lean:457:8: linarith failed to find a contradiction
✖ [8733/8737] Building Sidon30.SidonRampEnergy (3.4s)
error: Sidon30/SidonRampEnergy.lean:62:48: Application type mismatch: The argument
error: Sidon30/SidonRampEnergy.lean:66:51: unsolved goals
error: Sidon30/SidonRampEnergy.lean:89:10: typeclass instance problem is stuck
error: build failed
```
