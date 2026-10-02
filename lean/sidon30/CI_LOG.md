# sidon30 CI — run 37055051049  (completed / failure, commit fead917)

## Errors and warnings with context
```
277:✖ [8712/8718] Building Sidon30.ShiftWindow (5.9s)
278-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
279:error: Sidon30/ShiftWindow.lean:27:2: omega could not prove the goal:
280-a possible counterexample may satisfy the constraints
281-  e ≥ 1
282-  d ≥ 1
283-  d - e ≤ -1
284-  c ≥ 0
285-where
286- c := ↑((fun a ↦ a - 1) b)
287- d := ↑a
288- e := ↑b
289-✔ [8713/8718] Built Sidon30.Statement (5.1s)
290:✖ [8714/8718] Building Sidon30.PairCount (3.8s)
291-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
292:error: Sidon30/PairCount.lean:24:4: omega could not prove the goal:
293-a possible counterexample may satisfy the constraints
294-  d ≥ 0
295-  c ≥ 0
296-  c - d ≥ 0
297-  b ≥ 1
298-  a ≥ 0
299-  a - b ≥ 1
300-  a - d ≤ 1
301-where
302- a := ↑p.1
303- b := ↑p.2
304- c := ↑((fun p ↦ p.1 - p.2 - 1) p)
305- d := ↑(N - 1)
306:error: Sidon30/PairCount.lean:32:4: omega could not prove the goal:
307-a possible counterexample may satisfy the constraints
308-  g ≥ 0
309-  f ≥ 0
310-  f - g ≥ 1
311-  e ≥ 0
312-  d ≥ 0
313-  d - e ≥ 1
314-  c ≥ 0
315-  b ≥ 0
316-  b - c ≥ 1
317-  a ≥ 0
318-where
319- a := ↑((fun p ↦ p.1 - p.2 - 1) q)
320- b := ↑p.1
--
327:✖ [8716/8718] Building Sidon30.SidonEnergyUpper (3.6s)
328-trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.la
329-warning: Sidon30/SidonEnergyUpper.lean:38:55: `if_true` has been deprecated: Use `ite_true` instead
330-warning: Sidon30/SidonEnergyUpper.lean:38:64: `if_false` has been deprecated: Use `ite_false` instead
331-warning: Sidon30/SidonEnergyUpper.lean:43:55: `if_true` has been deprecated: Use `ite_true` instead
332-warning: Sidon30/SidonEnergyUpper.lean:43:64: `if_false` has been deprecated: Use `ite_false` instead
333-warning: Sidon30/SidonEnergyUpper.lean:59:20: `if_pos` has been deprecated: Use `ite_eq_left` instead
334-warning: Sidon30/SidonEnergyUpper.lean:64:38: `if_false` has been deprecated: Use `ite_false` instead
335:error: Sidon30/SidonEnergyUpper.lean:59:8: Type mismatch: After simplification, term
336-  Finset.sum_eq_single_of_mem a ha fun b _hb hba ↦
337-    of_eq_true
338-      (Eq.trans
339-        (congrFun'
340-          (congrArg Eq
341-            (Eq.trans (ite_congr (eq_false (Ne.symm hba)) (fun a ↦ Eq.refl (f 0)) fun a ↦ Eq.refl 0)
342-              (if_false (f 0) 0)))
343-          0)
344-        (eq_self 0))
345- has type
346-  @Eq ℝ (∑ x ∈ A, if a = x then f 0 else 0) (if True then f 0 else 0)
347-but is expected to have type
348-  @Eq ℝ (∑ b ∈ A, if a = b then f 0 else 0) (f 0)
349:error: Sidon30/SidonEnergyUpper.lean:135:2: Tactic `apply` failed: could not unify the conclusion of `@add_le_add_left`
350-  ?b + ?a ≤ ?c + ?a
351-with the goal
352-  ↑A.card * f 0 + 2 * ∑ p ∈ positivePairs A, f ↑(p.1 - p.2) ≤ ↑A.card * f 0 + 2 * ∑ d ∈ D, f ↑d
353-
354-Note: The full type of `@add_le_add_left` is
355-  ∀ {α : Type ?u.76} [inst : Add α] [inst_1 : LE α] [i : AddRightMono α] {b c : α}, b ≤ c → ∀ (a : α), b + a ≤ c + a
356-
357-A D : Finset ℕ
358-hA : IsSidon A
359-f : ℤ → ℝ
360-heven : ∀ (d : ℤ), f (-d) = f d
361-hcover : ∀ p ∈ positivePairs A, f ↑(p.1 - p.2) ≠ 0 → p.1 - p.2 ∈ D
362-hnonneg : ∀ d ∈ D, 0 ≤ f ↑d
363-⊢ ↑A.card * f 0 + 2 * ∑ p ∈ positivePairs A, f ↑(p.1 - p.2) ≤ ↑A.card * f 0 + 2 * ∑ d ∈ D, f ↑d
--
368:error: build failed
369-##[error]Process completed with exit code 1.
370-##[group]Run actions/upload-artifact@v4
371-with:
372-  name: build-log
373-  path: lean/sidon30/build.log
374-  if-no-files-found: warn
375-  compression-level: 6
376-  overwrite: false
377-  include-hidden-files: false
378-##[endgroup]
379-(node:2689) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
380-(Use `node --trace-deprecation ...` to show where the warning was created)
381-With the provided path, there will be 1 file uploaded
382-Artifact name is valid!
```
## Summary
```
✖ [8712/8718] Building Sidon30.ShiftWindow (5.9s)
error: Sidon30/ShiftWindow.lean:27:2: omega could not prove the goal:
✖ [8714/8718] Building Sidon30.PairCount (3.8s)
error: Sidon30/PairCount.lean:24:4: omega could not prove the goal:
error: Sidon30/PairCount.lean:32:4: omega could not prove the goal:
✖ [8716/8718] Building Sidon30.SidonEnergyUpper (3.6s)
error: Sidon30/SidonEnergyUpper.lean:59:8: Type mismatch: After simplification, term
error: Sidon30/SidonEnergyUpper.lean:135:2: Tactic `apply` failed: could not unify the conclusion of `@add_le_add_left`
error: build failed
```
