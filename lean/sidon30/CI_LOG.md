# sidon30 CI — run 37073539830  (completed / failure, commit c29a20c)

## Errors and warnings with context
```
464:✖ [8743/8745] Building Sidon30.SonarWindows (4.3s)
465-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
466:error: Sidon30/SonarWindows.lean:98:76: unsolved goals
467-case e_a
468-m U : ℕ
469-hU : U ≤ m
470-hm : m = U + (m - U)
471-hleft : ∑ k ∈ Finset.range U, ↑(sonarWindow m U k).card ^ 2 = ∑ k ∈ Finset.range U, ↑k ^ 2
472-hmiddle : ∑ k ∈ Finset.range (m - U), ↑(sonarWindow m U (U + k)).card ^ 2 = (↑m - ↑U) * ↑U ^ 2
473-hright : ∑ k ∈ Finset.range U, ↑(sonarWindow m U (m + k)).card ^ 2 = ∑ k ∈ Finset.range U, (↑U - ↑k) ^ 2
474-⊢ ∑ x ∈ Finset.range U, ↑(sonarWindow (U + (m - U)) U x).card ^ 2 +
475-      ∑ x ∈ Finset.range (m - U), ↑(sonarWindow (U + (m - U)) U (U + x)).card ^ 2 =
476-    ∑ k ∈ Finset.range U, ↑(sonarWindow m U k).card ^ 2 +
477-      ∑ k ∈ Finset.range (m - U), ↑(sonarWindow m U (U + k)).card ^ 2
478-warning: Sidon30/SonarWindows.lean:113:13: This simp argument is unused:
479-  Finset.mem_filter
480-
--
508:error: build failed
509-##[error]Process completed with exit code 1.
510-##[group]Run actions/upload-artifact@v4
511-with:
512-  name: build-log
513-  path: lean/sidon30/build.log
514-  if-no-files-found: warn
515-  compression-level: 6
516-  overwrite: false
517-  include-hidden-files: false
518-##[endgroup]
519-(node:3275) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
520-(Use `node --trace-deprecation ...` to show where the warning was created)
521-With the provided path, there will be 1 file uploaded
522-Artifact name is valid!
```
## Summary
```
✖ [8743/8745] Building Sidon30.SonarWindows (4.3s)
error: Sidon30/SonarWindows.lean:98:76: unsolved goals
error: build failed
```
