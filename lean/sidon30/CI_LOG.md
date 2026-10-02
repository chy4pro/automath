# sidon30 CI — run 37054355993  (completed / failure, commit 1df3d1c)

## Errors and warnings with context
```
243:✖ [8709/8713] Building Sidon30.Differences (3.8s)
244-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
245:error: Sidon30/Differences.lean:54:59: unsolved goals
246-A : Finset ℕ
247-a b : ℕ
248-⊢ (a, b) ∈ A.product A ∧ b < a ↔ a ∈ A ∧ b ∈ A ∧ b < a
249-warning: Sidon30/Differences.lean:56:47: This simp argument is unused:
250-  Finset.mem_product
251-
252-Hint: Omit it from the simp argument list.
253-  [apply] simp only [positivePairs, Finset.mem_filter, and_assoc]
254-
255-Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
256-warning: Sidon30/Differences.lean:56:67: This simp argument is unused:
257-  and_assoc
258-
259-Hint: Omit it from the simp argument list.
--
265:error: build failed
266-##[error]Process completed with exit code 1.
267-##[group]Run actions/upload-artifact@v4
268-with:
269-  name: build-log
270-  path: lean/sidon30/build.log
271-  if-no-files-found: warn
272-  compression-level: 6
273-  overwrite: false
274-  include-hidden-files: false
275-##[endgroup]
276-(node:3294) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
277-(Use `node --trace-deprecation ...` to show where the warning was created)
278-With the provided path, there will be 1 file uploaded
279-Artifact name is valid!
```
## Summary
```
✖ [8709/8713] Building Sidon30.Differences (3.8s)
error: Sidon30/Differences.lean:54:59: unsolved goals
error: build failed
```
