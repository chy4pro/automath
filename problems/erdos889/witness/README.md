# Erdos #889 — mechanical witness computation up to 10^7

This directory contains a self-contained, independently checked, numpy-only
computation in support of the Erdos #889 line. It is **not** a proof of any
part of the conjecture; it is finite verification / exception-list data,
scoped and bounded exactly as specified for this task (N = 10^7, single
process, <= 1 GB RAM, <= 2 CPU-hours). See `../G2_KILL_GATE_20260925.md`
for the proof-side status of the problem (the analytic "Theorem A" line was
found subsumed by Langevin 1981 and the Baker/Matveev proof campaign was
killed); this witness computation is independent of that and was requested
separately as exception-list/finiteness data.

## Definitions (exact, natural log throughout)

For integers `n >= 1`, `k >= 1`:

```
v(n,k) = #{ primes p : p | (n+k), p > k }
v_l(n) = sup_{k >= l} v(n,k)                for l >= 1
```

`log` / `ln` below always means the natural logarithm.

## Tasks and truncations

**Task 1.** For every `n` with `1 <= n <= 10^7`: find the smallest `k >= 1`
such that `v(n,k) >= 2`, searching only `k <= floor(30*ln(n+2)+30)`. This
search bound is the literal cutoff used (no padding); it is large enough
that in practice it is never actually the limiting factor (see Results).

From this we also derive, using the *same* found witnesses (the 30 ln(n+2)+30
search bound comfortably covers `10*ln(n)` for all n in range):

* the maximal smallest-`k` over all `n <= 10^7`;
* the list of all `n` with **no** `k <= 10*ln(n)` giving `v(n,k) >= 2`
  (expected: exactly the classical Erdos-Selfridge exceptional set, largest
  expected 330);
* the count of `n` with smallest `k > 20`.

`witness.csv` lists `(n, k, p1, p2)` — `k` and the two smallest witnessing
primes `p1 < p2` — **only** for the `n` whose smallest such `k` exceeds 10,
to keep the file small (as specified). This is 2 rows for `N = 10^7`
(see Results); every other `n <= 10^7` has smallest `k` in `{1,...,10}` and
is not listed.

**Task 2.** For each `l` in `{1, 2, 3, 5, 8, 13, 20}`: list every `n <= 10^7`
with `v_l(n) <= 1` when `v_l` is truncated to `k` in
`[l, floor(40*ln(n+2)+40)]`, i.e. **no** `k` in that window reaches
`v(n,k) >= 2`.

**Caveat (explicit, as required):** this is a truncation of the true
`sup_{k>=l}`. `v(n,k) >= 2` becomes overwhelmingly likely for `k` much
larger than `l` (a positive-density heuristic / Langevin's smooth-number
bound), so a window of `40*ln(n+2)+40` is generous, but an `n` listed here
as an "exception" is only known to have no witness *inside the window*; if
its true `v_l(n)` were achieved by some `k` beyond the window, it would be
wrongly listed here. This is exactly the caveat the task asked to state.
No independent proof that the window is sufficient is claimed; only the
`l=1` finite list (330 and below) is independently corroborated by the
published Erdos-Selfridge 1967 exceptional-set claim (`v_1(n)=1` for those
n, unrestricted `k`), which our windowed check reproduces exactly.

## Method (no sympy, no factordb, single process, bounded memory)

`gen_witness.py`:

1. Builds a segmented smallest-prime-factor (SPF) sieve over
   `[0, 10^7 + buffer]` (buffer ~694, covers the largest `n+k` used by
   either task) using plain Sieve-of-Eratosthenes-style numpy slicing —
   phase 1 finds primes up to `sqrt(MAXV)`, phase 2 marks multiples in
   chunks, phase 3 fills any still-zero entry as a self-prime. Result: one
   `int32` array of ~40 MB, `spf[m]` = smallest prime factor of `m`.
2. For each task, processes `n = 1..10^7` in independent **blocks** of
   `--block-size` (default 1,000,000) n-values — v(n,k) depends only on n
   itself, so blocks don't interact. Within a block, an outer loop over
   `k = k_start, k_start+1, ...` maintains the shrinking set of n not yet
   resolved; for the still-open n at each k, `m = n+k` is factored by
   repeatedly peeling `spf[m]` (in non-decreasing prime order, vectorized
   over the batch) until two *distinct* primes exceeding k have been seen
   or the number is exhausted. This is what bounds memory: peak working-set
   size is `O(block_size)`, not `O(N)`, independent of how large N is.
3. `witness.csv` rows and the task-2 exception lists are streamed out
   per-block rather than being accumulated as full N-sized arrays.

No sympy is imported (factorization is exclusively via the SPF array), and
the whole generator runs as one OS process (no multiprocessing/fork).

## Commands

```
export PATH="$HOME/.local/bin:$PATH"
cd /work/problems/erdos889/witness
ulimit -v 1200000   # ~1.144 GiB address-space cap, per the task's <=1GB limit
python3 gen_witness.py --N 10000000 --block-size 1000000
python3 check_witness.py witness.csv
```

`python3` here is python3.12 with numpy 2.5.3 (`$HOME/.local/bin/python3` /
uv-managed cpython-3.12.14). Both scripts are stdlib+numpy only
(`check_witness.py` is pure stdlib, no numpy).

## Runtime and memory (measured, this run)

* Total wall-clock: **19.9 s** (`run.log`: SPF sieve 0.07 s, task 1 1.5 s,
  task 2 summed over all 7 `l` values (each timed independently, `l=1`
  through `l=20`: 1.4, 2.0, 2.2, 2.5, 2.8, 3.5, 3.8 s) ~18.2 s) — measured
  directly by the script's own timers; independently confirmed by
  wall-clock timing of the whole process (20 s) from outside. Two
  back-to-back full runs reproduced byte-identical output files (see
  `witness.csv` SHA-256 below), confirming determinism.
* CPU budget: <= 2 CPU-hours (7200 s) allowed; actual usage is **~20 s**,
  about 0.3% of budget.
* Peak memory, measured via `/proc/<pid>/status` under `ulimit -v 1200000`:
  **VmPeak (virtual/address space) = 588,244 KB (~588 MB)**, comfortably
  under the 1,200,000 KB cap; **VmHWM (actual resident memory) = 148,264 KB
  (~148 MB)**. A bare `import numpy` alone already reserves ~472 MB of
  address space on this platform (BLAS/threading arena reservations, not
  our data), which is why VmPeak looks large relative to the small
  resident-memory footprint of the actual arrays — see `run.log` for the
  per-phase `[mem]` checkpoints. This did not grow materially between
  `N=2*10^6` and `N=10^7` runs with the same `--block-size`, confirming
  peak memory is governed by `block_size`, not `N`.
* Single process throughout (verified: no subprocess/multiprocessing calls
  in `gen_witness.py`).

Correctness of the vectorized numpy implementation was cross-checked before
the full run against an independent pure-Python trial-division brute force
(different code path, not shipped in this directory) at N=3,000 and
N=200,000/2,000,000: all reported quantities (max smallest-k, the 10*ln(n)
exceptional list, count>20, witness.csv rows including p1/p2, and all seven
task-2 exception lists/counts/largest values) matched exactly.

## Results (N = 10^7)

### Task 1

| Quantity | Value |
|---|---|
| Max smallest-k over all n <= 10^7 | **11** (achieved at n = 210) |
| n with no k <= 30*ln(n+2)+30 giving a witness at all | **29** (list below) |
| n with smallest k > 20 | **29** (same 29 n as above — no n in (330, 10^7] needs k>20) |
| n with no k <= 10*ln(n) (classical Erdos-Selfridge threshold) | **29**, largest = **330** |

The 29 exceptional n (identical for all three rows above, i.e. every n that
fails the tight `10*ln(n)` check also fails the far more generous
`30*ln(n+2)+30` search, and no *new* exceptions appear anywhere in
`(330, 10^7]`):

```
1, 2, 3, 4, 6, 7, 8, 10, 12, 15, 16, 18, 22, 24, 26, 30, 36, 42, 46, 48,
60, 70, 78, 80, 96, 120, 190, 222, 330
```

This reproduces Erdos-Selfridge (Illinois J. Math. 11 (1967), 428-430)
exactly: "v_1(n) = 1 for n = 1-4, 6-8, 10, 12, 15, 16, 18, 22, 24, 26, 30,
36, 42, 46, 48, 60, 70, 78, 80, 96, 120, 190, 222, 330, and for no other
values of n < 2500" — confirmed and extended here to n <= 10^7 with no
further exceptions found.

`witness.csv` (n with smallest k > 10; k and the two smallest witnessing
primes p1 < p2 of n+k that exceed k):

| n | k | p1 | p2 |
|---|---|----|----|
| 210 | 11 | 13 | 17 |
| 840 | 11 | 23 | 37 |

SHA-256 of `witness.csv`:
`6d752388a9fbae07ae83257360c66d9ad61b027646b3af93bfdd96e92631cb1c`

### Task 2 — exception lists for v_l(n) <= 1, truncated to k in [l, 40*ln(n+2)+40]

| l | count (n<=10^7) | largest n | selection-report value (n<=10^6) | match |
|---|---|---|---|---|
| 1 | 29 | 330 | 330 | yes |
| 2 | 103 | 1365 | 1365 | yes |
| 3 | 187 | 1365 | 1365 | yes |
| 5 | 383 | 2415 | 2415 | yes |
| 8 | 722 | 4895 | 4895 | yes |
| 13 | 1531 | 11655 | 11655 | yes |
| 20 | 2817 | 27714 | 27714 | yes |

All seven values from the selection report are **confirmed**, and extending
the search from 10^6 to 10^7 finds **no new exceptions** for any of the
seven l values — the largest exceptional n is unchanged in every case. Full
per-l exception lists are in `exceptions_l{1,2,3,5,8,13,20}.csv`
(count, largest and SHA-256 of each list are also in `task2_summary.json`).

## Independent checker (`check_witness.py`)

A second script, written independently (plain Python trial division, no
numpy, no SPF sieve, no shared code/imports with `gen_witness.py`), re-derives
from scratch for every row of `witness.csv`:

(A) that `p1 < p2` are genuinely primes, both `> k`, both dividing `n+k`,
    and that trial division of `n+k` finds at least 2 distinct prime factors
    exceeding `k` (i.e. the witness itself is valid), and

(B) **minimality** — that no smaller `k' < k` already has
    `v(n,k') >= 2` (re-factoring `n+k'` by trial division for every
    `k' = 1..k-1`), i.e. that `k` really is the smallest such k, not merely
    *a* valid k.

Run:
```
python3 check_witness.py witness.csv
```
Result on the real `witness.csv`:
```
check_witness.py: checked 2 rows from witness.csv
PASS=2 FAIL=0
elapsed=0.000s
```
Exit code 0. (The checker's discriminating power was separately verified
during development against deliberately-corrupted rows — wrong divisibility
and a deliberately non-minimal k — both of which it correctly flagged as
FAIL with the specific reason; that scratch test is not part of this
directory.)

## Files

| File | Contents |
|---|---|
| `gen_witness.py` | Generator (numpy, segmented SPF sieve, blocked/streamed). |
| `check_witness.py` | Independent trial-division checker for `witness.csv`. |
| `witness.csv` | n with smallest task-1 k > 10 (2 rows), with k, p1, p2. |
| `task1_summary.json` | Full task-1 summary (all fields in the table above, plus the full 29-n exceptional list). |
| `task2_summary.json` | Full task-2 summary for all 7 l values, incl. per-list SHA-256. |
| `exceptions_l1.csv` ... `exceptions_l20.csv` | Full exception list of n for each l (v_l(n)<=1 under the truncation). |
| `run.log` | Per-block/per-l progress log plus `[mem]` VmRSS/VmHWM/VmPeak checkpoints. |

## Discrepancies with expected values

**None.** Every value that had a stated expectation (the Erdos-Selfridge
largest exception 330; the selection report's seven largest-n values for
l = 1,2,3,5,8,13,20) matched exactly, both at intermediate scales (N=3,000
brute-force cross-check; N=200,000/2,000,000 against the selection report's
values, which are all <= 10^6) and at the full N=10^7 scale. No new
exceptions appeared anywhere between 10^6 and 10^7 for any of the 8
quantities checked (1 task-1 list + 7 task-2 lists).
