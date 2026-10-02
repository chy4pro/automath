# sidon30 CI — run 37074337091  (completed / failure, commit 1298b13)

## Errors and warnings with context
```
286:✖ [8720/8754] Building Sidon30.SonarScale (6.8s)
287-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
288:error: Sidon30/SonarScale.lean:163:27: Tactic `rewrite` failed: Did not find an occurrence of the pattern
289-  (↑n ^ ?y) ^ ?z
290-in the target expression
291-  (↑n).rpow (1 / 3) ^ ↑3 = ↑n
292-
293-n : ℕ
294-⊢ (↑n).rpow (1 / 3) ^ ↑3 = ↑n
295:error: Sidon30/SonarScale.lean:169:27: Tactic `rewrite` failed: Did not find an occurrence of the pattern
296-  (↑n ^ ?y) ^ ?z
297-in the target expression
298-  (↑n).rpow (1 / 3) ^ ↑2 = (↑n).rpow (2 / 3)
299-
300-n : ℕ
301-⊢ (↑n).rpow (1 / 3) ^ ↑2 = (↑n).rpow (2 / 3)
302-⚠ [8721/8754] Built Sidon30.WeakSidonScale (8.3s)
303-warning: Sidon30/WeakSidonScale.lean:101:10: this tactic is never executed
304-
305-Note: This linter can be disabled with `set_option linter.unreachableTactic false`
306-warning: Sidon30/WeakSidonScale.lean:101:10: Unused tactic linter: `ring` does nothing
307-
308-Note: This linter can be disabled with `set_option linter.unusedTactic false`
309-⚠ [8723/8754] Built Sidon30.RenewalRampIdentity (6.9s)
--
467:✖ [8750/8754] Building Sidon30.SonarEnergy (3.3s)
468-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
469-warning: Sidon30/SonarEnergy.lean:38:22: `if_false` has been deprecated: Use `ite_false` instead
470-warning: Sidon30/SonarEnergy.lean:38:37: `if_true` has been deprecated: Use `ite_true` instead
471-warning: Sidon30/SonarEnergy.lean:42:24: `if_true` has been deprecated: Use `ite_true` instead
472-warning: Sidon30/SonarEnergy.lean:42:52: `if_false` has been deprecated: Use `ite_false` instead
473-warning: Sidon30/SonarEnergy.lean:46:22: `if_false` has been deprecated: Use `ite_false` instead
474-warning: Sidon30/SonarEnergy.lean:46:37: `if_true` has been deprecated: Use `ite_true` instead
475:error: Sidon30/SonarEnergy.lean:217:8: Tactic `rewrite` failed: Did not find an occurrence of the pattern
476-  Finset.product ?m.702 ?m.703
477-in the target expression
478-  ∑ d ∈ Finset.Icc 1 (U - 1) ×ˢ Finset.Icc (1 - ↑V) (↑V - 1), ↑(U - d.1) * rampCorrelation V d.2 = ↑U * (↑U - 1) / 2
479-
480-m n U V : ℕ
481-y : Fin m → Fin n
482-hA : IsSonar y
483-hU : 1 ≤ U
484-hV : 1 ≤ V
485-K : Fin m → Fin m → ℝ := fun i j ↦ ↑(U - (max ↑i ↑j - min ↑i ↑j)) * rampCorrelation V (↑↑(y i) - ↑↑(y j))
486-δ : Fin m × Fin m → ℕ × ℤ := fun p ↦ (↑p.1 - ↑p.2, ↑↑(y p.1) - ↑↑(y p.2))
487-w : ℕ × ℤ → ℝ := fun d ↦ ↑(U - d.1) * rampCorrelation V d.2
488-D : Finset (ℕ × ℤ) := (Finset.Icc 1 (U - 1)).product (Finset.Icc (1 - ↑V) (↑V - 1))
489-hsymm : ∀ (i j : Fin m), K j i = K i j
--
498:error: build failed
499-##[error]Process completed with exit code 1.
500-##[group]Run actions/upload-artifact@v4
501-with:
502-  name: build-log
503-  path: lean/sidon30/build.log
504-  if-no-files-found: warn
505-  compression-level: 6
506-  overwrite: false
507-  include-hidden-files: false
508-##[endgroup]
509-(node:3009) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
510-(Use `node --trace-deprecation ...` to show where the warning was created)
511-With the provided path, there will be 1 file uploaded
512-Artifact name is valid!
```
## Summary
```
✖ [8720/8754] Building Sidon30.SonarScale (6.8s)
error: Sidon30/SonarScale.lean:163:27: Tactic `rewrite` failed: Did not find an occurrence of the pattern
error: Sidon30/SonarScale.lean:169:27: Tactic `rewrite` failed: Did not find an occurrence of the pattern
✖ [8750/8754] Building Sidon30.SonarEnergy (3.3s)
error: Sidon30/SonarEnergy.lean:217:8: Tactic `rewrite` failed: Did not find an occurrence of the pattern
error: build failed
```
