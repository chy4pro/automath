# sidon30 CI — run 37058224778  (completed / failure, commit f3e07df)

## Errors and warnings with context
```
409:✖ [8727/8729] Building Sidon30.FiniteBoundaryPotential (5.7s)
410-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
411-warning: Sidon30/FiniteBoundaryPotential.lean:47:6: `if_pos` has been deprecated: Use `ite_eq_left` instead
412-warning: Sidon30/FiniteBoundaryPotential.lean:47:18: `if_pos` has been deprecated: Use `ite_eq_left` instead
413-warning: Sidon30/FiniteBoundaryPotential.lean:60:53: `if_neg` has been deprecated: Use `ite_eq_right` instead
414-warning: Sidon30/FiniteBoundaryPotential.lean:61:4: `if_pos` has been deprecated: Use `ite_eq_left` instead
415-warning: Sidon30/FiniteBoundaryPotential.lean:61:16: `if_neg` has been deprecated: Use `ite_eq_right` instead
416-warning: Sidon30/FiniteBoundaryPotential.lean:71:53: `if_neg` has been deprecated: Use `ite_eq_right` instead
417-warning: Sidon30/FiniteBoundaryPotential.lean:72:4: `if_neg` has been deprecated: Use `ite_eq_right` instead
418-warning: Sidon30/FiniteBoundaryPotential.lean:72:16: `if_pos` has been deprecated: Use `ite_eq_left` instead
419-warning: Sidon30/FiniteBoundaryPotential.lean:117:40: `if_pos` has been deprecated: Use `ite_eq_left` instead
420:error: Sidon30/FiniteBoundaryPotential.lean:132:8: Tactic `rewrite` failed: Did not find an occurrence of the pattern
421-  D - (x + ↑j - ↑i)
422-in the target expression
423-  rampWeight T j * rampWeight T i * (fun y ↦ renewalInt T (D - y)) (x + ↑j - ↑i) =
424-    rampWeight T i * rampWeight T j * renewalInt T (D - x + ↑i - ↑j)
425-
426-T : ℕ
427-hT : 1 ≤ T
428-D x : ℤ
429-hx : x ≤ D
430-i : ℕ
431-_hi : i ∈ Finset.range T
432-j : ℕ
433-_hj : j ∈ Finset.range T
434-harg : D - (x + ↑j - ↑i) = D - x + ↑i - ↑j
--
439:error: build failed
440-##[error]Process completed with exit code 1.
441-##[group]Run actions/upload-artifact@v4
442-with:
443-  name: build-log
444-  path: lean/sidon30/build.log
445-  if-no-files-found: warn
446-  compression-level: 6
447-  overwrite: false
448-  include-hidden-files: false
449-##[endgroup]
450-(node:3027) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
451-(Use `node --trace-deprecation ...` to show where the warning was created)
452-With the provided path, there will be 1 file uploaded
453-Artifact name is valid!
```
## Summary
```
✖ [8727/8729] Building Sidon30.FiniteBoundaryPotential (5.7s)
error: Sidon30/FiniteBoundaryPotential.lean:132:8: Tactic `rewrite` failed: Did not find an occurrence of the pattern
error: build failed
```
