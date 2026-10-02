# 039 Capacity-method transfers: adversarial referee, then full proofs with explicit statements (slot 2, high-certainty)
priority: high — ahead of 038a if seats are scarce · parallel: yes · clean-room: no (verification and proof-writing; informed seats are fine) · report: /work/problems/capacity_transfer/REPORT.md (proofs in the same directory, one file per item)

Input: /work/notes/selection/transfer_targets_20261002.md — a Claude Opus scout's UNREVIEWED derivations. It claims that the Sidon machinery (ramp kernel, Lemma 6 capacity bound L + 2/3 + 200e^{-αL}) improves five neighbouring records:
 1. sonar sequences (n rows, m columns, one dot per column, distinct difference vectors): m ≤ n + 2n^{2/3} + O(n^{1/3}) — record: Erdős–Graham–Ruzsa–Taylor 1992, proved 5 (4 in the proof), unproved remark 3. New step: Cauchy–Schwarz against λ⊗ρ with λ the exact column marginal (inequality (S), §3.1).
 2. weak Sidon sets: √N + √(8/3)·N^{1/4} + O(1) — record ≈ 1.7232 (Balogh–Füredi–Roy 2023).
 3. g-thin Sidon sets / g-Golomb rulers: √(gN) + (2√2/3)(gN)^{1/4} + 1 for gN ≥ 120⁴.
 4. difference triangle sets: m(n,k) ≥ n(k² − (4√2/3)k^{3/2} + O(k)) — record Kløve 1988 with 2.
 5. Manhattan distinct-difference configurations: r/√2 + 3·2^{-4/3}(8/9)^{2/3} r^{2/3} — record BEMP 2010 with 3·2^{-4/3}.
 (6. Sidon sets in [N]^d: constant ((d+1)/2)(8/9)^{d/(d+1)} — status of the record unknown; include the proof, mark the comparison open.)
The coordinator re-checked the sonar sandwich numerically on quadratic sonar sequences (p = 101, 499, 1009; holds) and the AM–GM arithmetic; nothing else.

Stage A — cross-vendor adversarial referee (you are the other vendor here). For each item: is the combinatorial model stated exactly as in the cited source (quantifiers, ordered/unordered pairs, index ranges, what "diameter"/"scope" means)? Is every inequality valid — especially: positivity of the kernel where missing difference vectors are dropped; positive-definiteness where Cauchy–Schwarz is used; the lattice-sum bounds; the 3-AP accounting for weak Sidon (r(d) ≤ 2, |P| ≤ k−2); the index-2 lattice in item 5; the product test measure? Try to break (S) on small exhaustive cases. Verdict per item: PASS / PASS-WITH-REPAIRS / FAIL, with the exact failing line.

Stage B — for every item that survives: a complete standalone proof in the style of problems/erdos30/SIDON_BOUND_PROOF.md, with a **fully explicit** theorem where reachable (all n ≥ n₀ / N ≥ N₀ with every constant named; the scout's scans suggest "+2, N ≥ 90⁴" for weak Sidon and ≈ +2.62 n^{1/3} for sonar — these are scans, not proofs). Where an explicit onset is not reachable in reasonable effort, state the asymptotic theorem with a bounded error term and say so. A dependency-free exact check script per item (JS/BigInt is acceptable; label it).

Stage C — push the sonar result: the x-direction constant is a·m₁ with m₁ = ∫|t|f(t)dt (triangle 1/3 → coefficient 2; cosine bump π²/32 → ≈ 1.949; trivial floor 1/4 → ≈ 1.817). Determine the true infimum of f(0)·∫|t|f over admissible kernels (even, ≥ 0, positive definite, ∫f = 1) with proof if you can, handle the lattice-sum errors for the optimal kernel, and state the resulting best coefficient and a matching barrier statement for this method. Also ask whether a known marginal can be exploited in any other item.

Do not do literature search for novelty here — the coordinator is running the status check (G2) separately; do read a cited source when you need the exact definition. No external publication. Push back if you think the package is not worth Astra's time, or if a different ordering is better.
