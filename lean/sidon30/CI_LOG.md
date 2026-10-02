# sidon30 CI — run 37052888598  (completed / failure, commit 2d672bd)

## Errors and warnings with context
```
203:✖ [8709/8713] Building Sidon30.Differences (3.2s)
204-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
205:error: Sidon30/Differences.lean:54:59: unsolved goals
206-A : Finset ℕ
207-p : ℕ × ℕ
208-⊢ p ∈ A.product A ∧ p.2 < p.1 ↔ p.1 ∈ A ∧ p.2 ∈ A ∧ p.2 < p.1
209-warning: Sidon30/Differences.lean:55:47: This simp argument is unused:
210-  Finset.mem_product
211-
212-Hint: Omit it from the simp argument list.
213-  [apply] simp only [positivePairs, Finset.mem_filter, and_assoc]
214-
215-Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
216-warning: Sidon30/Differences.lean:55:67: This simp argument is unused:
217-  and_assoc
218-
219-Hint: Omit it from the simp argument list.
--
225:error: build failed
226-##[error]Process completed with exit code 1.
227-##[group]Run actions/upload-artifact@v4
228-with:
229-  name: build-log
230-  path: lean/sidon30/build.log
231-  if-no-files-found: warn
232-  compression-level: 6
233-  overwrite: false
234-  include-hidden-files: false
235-##[endgroup]
236-(node:2623) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
237-(Use `node --trace-deprecation ...` to show where the warning was created)
238-With the provided path, there will be 1 file uploaded
239-Artifact name is valid!
```
## Summary
```
✖ [8709/8713] Building Sidon30.Differences (3.2s)
error: Sidon30/Differences.lean:54:59: unsolved goals
error: build failed
```
