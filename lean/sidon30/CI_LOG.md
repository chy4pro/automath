# sidon30 CI — run 37072782780  (completed / failure, commit 4fd7b16)

## Errors and warnings with context
```
375:✖ [8736/8739] Building Sidon30.TransferCertificate (2.9s)
376-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
377:error: Sidon30/TransferCertificate.lean:74:4: No goals to be solved
378-✔ [8737/8739] Built Sidon30.Main (2.9s)
379-Some required targets logged failures:
380-- Sidon30.TransferCertificate
381:error: build failed
382-##[error]Process completed with exit code 1.
383-##[group]Run actions/upload-artifact@v4
384-with:
385-  name: build-log
386-  path: lean/sidon30/build.log
387-  if-no-files-found: warn
388-  compression-level: 6
389-  overwrite: false
390-  include-hidden-files: false
391-##[endgroup]
392-(node:2941) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
393-(Use `node --trace-deprecation ...` to show where the warning was created)
394-With the provided path, there will be 1 file uploaded
395-Artifact name is valid!
```
## Summary
```
✖ [8736/8739] Building Sidon30.TransferCertificate (2.9s)
error: Sidon30/TransferCertificate.lean:74:4: No goals to be solved
error: build failed
```
