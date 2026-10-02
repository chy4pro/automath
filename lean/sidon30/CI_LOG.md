# sidon30 CI — latest run 37052528691

completed failure 7485d4d 2026-10-02T19:11:58Z

## Build/Axioms errors and warnings (with context)
```
7:Build	✖ [8709/8713] Building Sidon30.Differences (4.4s)
8-Build	trace: .> LEAN_PATH=/home/runner/work/automath/automath/lean/sidon30/.lake/packages/Cli/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30/.lake/packages/batteries/.lake/build/lib/lean:/home/runner/work/automath/automath/lean/sidon30
9:Build	error: Sidon30/Differences.lean:54:59: unsolved goals
10-Build	A : Finset ℕ
11-Build	p : ℕ × ℕ
12-Build	⊢ p ∈ A.product A ∧ p.2 < p.1 ↔ p.1 ∈ A ∧ p.2 ∈ A ∧ p.2 < p.1
13-Build	warning: Sidon30/Differences.lean:55:47: This simp argument is unused:
14-Build	  Finset.mem_product
15-Build	
16-Build	Hint: Omit it from the simp argument list.
17-Build	  [apply] simp only [positivePairs, Finset.mem_filter, and_assoc]
18-Build	
19-Build	Note: This linter can be disabled with `set_option linter.unusedSimpArgs false`
20-Build	warning: Sidon30/Differences.lean:55:67: This simp argument is unused:
21-Build	  and_assoc
22-Build	
23-Build	Hint: Omit it from the simp argument list.
--
29:Build	error: build failed
30-Axioms	﻿2026-10-02T19:14:17.6141635Z ##[group]Run if [ -f Sidon30/FinalCheck.lean ]; then lake env lean Sidon30/FinalCheck.lean; else echo "no FinalCheck yet"; fi
31-Axioms	^[[36;1mif [ -f Sidon30/FinalCheck.lean ]; then lake env lean Sidon30/FinalCheck.lean; else echo "no FinalCheck yet"; fi^[[0m
32-Axioms	shell: /usr/bin/bash -e {0}
33-Axioms	##[endgroup]
34:Axioms	Sidon30/FinalCheck.lean:1:0: error: object file '/home/runner/work/automath/automath/lean/sidon30/.lake/build/lib/lean/Sidon30.olean' of module Sidon30 does not exist
35:Axioms	##[error]Process completed with exit code 1.
```
## Summary lines
```
Build	✖ [8709/8713] Building Sidon30.Differences (4.4s)
Build	error: Sidon30/Differences.lean:54:59: unsolved goals
Build	error: build failed
Axioms	Sidon30/FinalCheck.lean:1:0: error: object file '/home/runner/work/automath/automath/lean/sidon30/.lake/build/lib/lean/Sidon30.olean' of module Sidon30 does not exist
```
