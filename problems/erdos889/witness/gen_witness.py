#!/usr/bin/env python3
"""
Erdos #889 mechanical witness generator.

Definitions (natural log throughout):
  v(n,k)   = #{ primes p : p | n+k, p > k }                      (n>=1, k>=1)
  v_l(n)   = sup_{k >= l} v(n,k)                                  (l>=1)

Task 1 (per n in 1..N):
  smallest k >= 1 with v(n,k) >= 2, searched over k <= 30*ln(n+2)+30.
Task 2 (per l in {1,2,3,5,8,13,20}, per n in 1..N):
  is v_l(n) <= 1 when v_l is truncated to k in [l, 40*ln(n+2)+40]?
  (i.e. does NO k in that window reach v(n,k) >= 2?)

Method: a single-process, numpy, segmented smallest-prime-factor (SPF) sieve
over [0, MAXV], MAXV = N + small buffer covering the largest k used by either
task. No sympy, no factordb, no multiprocessing. All arithmetic on the
sieve/factoring side is exact integer arithmetic (numpy int64), so there is
no floating point in the number-theoretic test itself -- floating point
(python's math.log / numpy's np.log, IEEE double) is used only to compute the
*search bounds* 30*ln(n+2)+30 and 40*ln(n+2)+40, which are then floored
(exactly as specified) to get the integer k cutoff for each n.

For a fixed k, factoring m = n+k against the SPF array and peeling off
prime factors in non-decreasing order lets us stop as soon as two *distinct*
primes exceeding k have been seen (or the number is exhausted) -- this is
what batch_two_smallest_big_primes() does, vectorized over the current batch of still-open
n values at that k.

Outer loop is over k = 1, 2, 3, ... ; inner state is the shrinking set of n
that have not yet found a witness. This is efficient in practice because the
overwhelming majority of n resolve at very small k (Erdos-Selfridge already
observed this), so only a small, shrinking tail of n pay for the larger-k
iterations.
"""
import argparse
import csv
import gc
import hashlib
import json
import math
import os
import time

import numpy as np

# Search bounds are exactly floor(30*ln(n+2)+30) / floor(40*ln(n+2)+40) as
# specified by the task, computed with IEEE-754 double precision (numpy
# float64 / python's math.log, both correctly-rounded on this platform).
# No padding is added: the task's cutoff is the literal search limit.


def build_spf(maxv, segment_size=2_000_000):
    """Segmented smallest-prime-factor sieve on [0, maxv] (inclusive).

    Phase 1: ordinary sieve of Eratosthenes for primes up to sqrt(maxv)
    ("base primes"). Phase 2: sweep [0, maxv] in chunks of segment_size,
    and for each chunk mark spf[j] = p for the smallest base prime p | j
    that has not already been set by a smaller prime; leftover unmarked
    entries >= 2 in the chunk are primes themselves (no base prime <=
    sqrt(maxv) divides them), so spf[j] = j for those.

    Peak extra memory during construction is O(segment_size + #base_primes),
    not O(maxv); the only O(maxv)-sized array retained afterwards is spf
    itself (int32, 4 bytes/entry).
    """
    r = int(math.isqrt(maxv)) + 1
    base_sieve = np.ones(r + 1, dtype=bool)
    base_sieve[:2] = False
    for i in range(2, int(math.isqrt(r)) + 1):
        if base_sieve[i]:
            base_sieve[i * i:: i] = False
    base_primes = np.nonzero(base_sieve)[0].astype(np.int64)

    spf = np.zeros(maxv + 1, dtype=np.int32)
    for seg_start in range(0, maxv + 1, segment_size):
        seg_end = min(seg_start + segment_size - 1, maxv)
        seg = spf[seg_start:seg_end + 1]
        for p in base_primes:
            pp = p * p
            if pp > seg_end:
                break
            start = pp if pp >= seg_start else ((seg_start + p - 1) // p) * p
            if start > seg_end:
                continue
            off = start - seg_start
            sl = seg[off::p]
            unset = sl == 0
            if unset.any():
                sl[unset] = p
        zero_idx = np.nonzero(seg == 0)[0]
        vals = zero_idx + seg_start
        is_self_prime = vals >= 2
        seg[zero_idx[is_self_prime]] = vals[is_self_prime]
    spf[0] = 0
    if maxv >= 1:
        spf[1] = 0
    return spf


def batch_two_smallest_big_primes(m, k, spf, want_primes=True, max_iter=30):
    """For each entry of int32 array m, decide whether m has >=2 DISTINCT
    prime factors > k, peeling factors of m in non-decreasing order via the
    SPF array. k is a python int (same threshold for the whole batch).
    int32 is exact and sufficient here: m <= N + a few hundred, always well
    under 2^31, so there is no overflow risk while roughly halving the
    memory of the int64 alternative.

    Returns (success_bool_array, p1_array_or_None, p2_array_or_None) with
    p1 < p2 the two smallest such primes when want_primes is True.
    """
    n_items = m.shape[0]
    r = m.copy()
    last_p = np.zeros(n_items, dtype=np.int32)
    cnt = np.zeros(n_items, dtype=np.int8)
    if want_primes:
        p1 = np.zeros(n_items, dtype=np.int32)
        p2 = np.zeros(n_items, dtype=np.int32)
    else:
        p1 = p2 = None
    active = r > 1
    for _ in range(max_iter):
        if not active.any():
            break
        p_val = np.zeros(n_items, dtype=np.int32)
        p_val[active] = spf[r[active]]
        is_new = active & (p_val != last_p)
        is_new_big = is_new & (p_val > k)
        if is_new_big.any():
            take1 = is_new_big & (cnt == 0)
            if want_primes and take1.any():
                p1[take1] = p_val[take1]
            take2 = is_new_big & (cnt == 1)
            if want_primes and take2.any():
                p2[take2] = p_val[take2]
            cnt[is_new_big] += 1
        last_p[active] = p_val[active]
        r[active] //= p_val[active]
        active = (r > 1) & (cnt < 2)
    success = cnt >= 2
    return success, p1, p2


def sweep_block(n_block, kmax_block, k_start, spf, want_primes):
    """Core outer-k sweep, scoped to one block of n values (a numpy int32
    array n_block) with per-n cutoff kmax_block (same length, int32).
    k_start is the first k tried (1 for task 1, l for task 2).

    All working arrays here are sized to len(n_block), not to the global N,
    which is what bounds peak memory: the caller picks a block size so that
    these arrays (persistent + the batch_two_smallest_big_primes temporaries)
    comfortably fit the memory budget regardless of how large N is.

    Returns (found_k, found_p1_or_None, found_p2_or_None, never_found_mask)
    where found_k[i]==0 and never_found_mask[i]==True means no k in
    [k_start, kmax_block[i]] gave v(n_block[i], k) >= 2.
    """
    L = n_block.shape[0]
    found_k = np.zeros(L, dtype=np.int32)
    found_p1 = np.zeros(L, dtype=np.int32) if want_primes else None
    found_p2 = np.zeros(L, dtype=np.int32) if want_primes else None
    active = np.ones(L, dtype=bool)
    remaining = L
    global_kmax = int(kmax_block.max()) if L > 0 else k_start - 1
    k = k_start
    while remaining > 0 and k <= global_kmax:
        cur_mask = active & (kmax_block >= k)
        cnt_cur = int(cur_mask.sum())
        if cnt_cur == 0:
            k += 1
            continue
        cur_pos = np.flatnonzero(cur_mask)
        n_cur = n_block[cur_pos]
        m = n_cur + k
        success, p1, p2 = batch_two_smallest_big_primes(m, k, spf, want_primes=want_primes)
        if success.any():
            sel = cur_pos[success]
            found_k[sel] = k
            if want_primes:
                found_p1[sel] = p1[success]
                found_p2[sel] = p2[success]
            active[sel] = False
            remaining -= int(success.sum())
        k += 1
    return found_k, found_p1, found_p2, active


def task1(N, spf, log_path, outdir, block_size):
    """Smallest k with v(n,k)>=2 for each n in 1..N, k<=30*ln(n+2)+30.

    Processed in blocks of `block_size` n-values (each block independent,
    since v(n,k) depends only on n itself) to bound peak memory; results are
    streamed to witness.csv (rows with k>10) and aggregated into a summary
    dict as we go, rather than keeping full-N-sized found_k/p1/p2 arrays.
    """
    t0 = time.time()
    csv_path = os.path.join(outdir, "witness.csv")
    csv_rows = 0
    max_smallest_k = 0
    n_at_max = None
    count_gt20 = 0
    never_found_all = []
    exceptional_10logn_all = []

    with open(csv_path, "w", newline="") as cf:
        w = csv.writer(cf)
        w.writerow(["n", "k", "p1", "p2"])
        for blk_start in range(1, N + 1, block_size):
            blk_end = min(blk_start + block_size - 1, N)
            n_block = np.arange(blk_start, blk_end + 1, dtype=np.int32)
            bound_f = 30.0 * np.log(n_block.astype(np.float64) + 2.0) + 30.0
            kmax_block = np.floor(bound_f).astype(np.int32)
            del bound_f

            found_k, found_p1, found_p2, never_mask = sweep_block(
                n_block, kmax_block, 1, spf, want_primes=True)

            fk_pos = found_k > 0
            if fk_pos.any():
                blk_max = int(found_k[fk_pos].max())
                if blk_max > max_smallest_k:
                    max_smallest_k = blk_max
                    n_at_max = int(n_block[fk_pos][found_k[fk_pos] == blk_max][0])

            count_gt20 += int((found_k > 20).sum()) + int(never_mask.sum())

            thresh10 = 10.0 * np.log(n_block.astype(np.float64))
            fk_f = found_k.astype(np.float64)
            exc10_mask = never_mask | ((found_k > 0) & (fk_f > thresh10))
            if exc10_mask.any():
                exceptional_10logn_all.extend(int(x) for x in n_block[exc10_mask].tolist())

            if never_mask.any():
                never_found_all.extend(int(x) for x in n_block[never_mask].tolist())

            rows_mask = found_k > 10
            if rows_mask.any():
                ns = n_block[rows_mask]
                ks = found_k[rows_mask]
                p1s = found_p1[rows_mask]
                p2s = found_p2[rows_mask]
                for i in range(len(ns)):
                    w.writerow([int(ns[i]), int(ks[i]), int(p1s[i]), int(p2s[i])])
                csv_rows += int(rows_mask.sum())

            with open(log_path, "a") as lf:
                lf.write(f"[task1] block [{blk_start},{blk_end}] done, "
                         f"never_in_block={int(never_mask.sum())} "
                         f"elapsed={time.time()-t0:.1f}s\n")
            del n_block, kmax_block, found_k, found_p1, found_p2, never_mask
            del fk_pos, thresh10, fk_f, exc10_mask, rows_mask

    never_found_all.sort()
    exceptional_10logn_all.sort()
    with open(log_path, "a") as lf:
        lf.write(f"[task1] done. remaining_without_witness={len(never_found_all)}, "
                  f"elapsed={time.time()-t0:.1f}s\n")
    return {
        "max_smallest_k": max_smallest_k,
        "n_at_max": n_at_max,
        "count_gt20": count_gt20,
        "never_found_all": never_found_all,
        "exceptional_10logn_all": exceptional_10logn_all,
        "csv_rows": csv_rows,
        "csv_path": csv_path,
        "runtime": time.time() - t0,
    }


def task2_exceptions(N, spf, l, log_path, block_size):
    """All n in 1..N with v_l(n) <= 1 under truncation k in [l, 40*ln(n+2)+40].
    Block-processed for the same memory reason as task1; boolean-only (no
    p1/p2 tracking needed), so this is cheaper per element than task1.
    """
    t0 = time.time()
    exceptions = []
    for blk_start in range(1, N + 1, block_size):
        blk_end = min(blk_start + block_size - 1, N)
        n_block = np.arange(blk_start, blk_end + 1, dtype=np.int32)
        bound_f = 40.0 * np.log(n_block.astype(np.float64) + 2.0) + 40.0
        kmax_block = np.floor(bound_f).astype(np.int32)
        del bound_f

        _, _, _, never_mask = sweep_block(n_block, kmax_block, l, spf, want_primes=False)
        if never_mask.any():
            exceptions.extend(int(x) for x in n_block[never_mask].tolist())
        del n_block, kmax_block, never_mask

    exceptions.sort()
    with open(log_path, "a") as lf:
        lf.write(f"[task2 l={l}] done. exceptions={len(exceptions)}, "
                  f"elapsed={time.time()-t0:.1f}s\n")
    return exceptions, time.time() - t0


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def mem_checkpoint(log_path, label):
    """Append current VmRSS/VmPeak (KiB, from /proc/self/status) to the log,
    for the runtime/memory section of README.md."""
    try:
        with open("/proc/self/status") as f:
            status = f.read()
        rss = next((l.split()[1] for l in status.splitlines() if l.startswith("VmRSS:")), "?")
        peak = next((l.split()[1] for l in status.splitlines() if l.startswith("VmPeak:")), "?")
        hwm = next((l.split()[1] for l in status.splitlines() if l.startswith("VmHWM:")), "?")
    except OSError:
        rss = peak = hwm = "?"
    with open(log_path, "a") as lf:
        lf.write(f"[mem] {label}: VmRSS={rss}KB VmHWM={hwm}KB VmPeak={peak}KB\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=10_000_000)
    ap.add_argument("--outdir", type=str, default=os.path.dirname(os.path.abspath(__file__)))
    ap.add_argument("--skip-task2", action="store_true")
    ap.add_argument("--block-size", type=int, default=1_000_000,
                     help="n-values processed per block, to bound peak memory")
    args = ap.parse_args()

    N = args.N
    outdir = args.outdir
    block_size = args.block_size
    os.makedirs(outdir, exist_ok=True)
    log_path = os.path.join(outdir, "run.log")
    with open(log_path, "a") as lf:
        lf.write(f"\n=== gen_witness.py run start N={N} block_size={block_size} pid={os.getpid()} "
                  f"time={time.strftime('%Y-%m-%d %H:%M:%S')} ===\n")

    t_start = time.time()

    # Buffer must cover the largest m = n + k used by EITHER task, at n=N.
    task1_kmax_at_N = math.floor(30.0 * math.log(N + 2) + 30.0)
    task2_kmax_at_N = math.floor(40.0 * math.log(N + 2) + 40.0)
    buffer = max(task1_kmax_at_N, task2_kmax_at_N) + 10
    MAXV = N + buffer

    with open(log_path, "a") as lf:
        lf.write(f"MAXV={MAXV} (buffer={buffer}) building SPF sieve...\n")
    t_sieve0 = time.time()
    spf = build_spf(MAXV)
    t_sieve = time.time() - t_sieve0
    with open(log_path, "a") as lf:
        lf.write(f"SPF sieve built in {t_sieve:.2f}s, array bytes={spf.nbytes}\n")
    mem_checkpoint(log_path, "after SPF sieve")

    # ---- Task 1 ----
    r1 = task1(N, spf, log_path, outdir, block_size)
    mem_checkpoint(log_path, "after task1")

    csv_hash = sha256_of(r1["csv_path"])
    never_found_all = r1["never_found_all"]
    exceptional_10logn_all = r1["exceptional_10logn_all"]

    task1_summary = {
        "N": N,
        "search_bound_formula": "k <= floor(30*ln(n+2)+30)",
        "max_smallest_k_over_all_n": r1["max_smallest_k"],
        "n_achieving_max_smallest_k": r1["n_at_max"],
        "count_n_with_no_witness_within_search_bound": len(never_found_all),
        "n_with_no_witness_within_search_bound": never_found_all[:50],
        "count_n_with_smallest_k_gt_20": r1["count_gt20"],
        "exceptional_under_10logn_threshold": {
            "definition": "n such that no k with 1<=k<=10*ln(n) has v(n,k)>=2, "
                           "checked within the (larger) 30*ln(n+2)+30 search bound",
            "count": len(exceptional_10logn_all),
            "largest": exceptional_10logn_all[-1] if exceptional_10logn_all else None,
            "all": exceptional_10logn_all,
        },
        "witness_csv_rows_k_gt_10": r1["csv_rows"],
        "witness_csv_sha256": csv_hash,
        "runtime_seconds": r1["runtime"],
    }
    with open(os.path.join(outdir, "task1_summary.json"), "w") as f:
        json.dump(task1_summary, f, indent=2)

    del r1, never_found_all, exceptional_10logn_all
    gc.collect()
    mem_checkpoint(log_path, "after task1 cleanup, before task2")

    # ---- Task 2 ----
    ls = [1, 2, 3, 5, 8, 13, 20]
    task2_summary = {
        "N": N,
        "window_formula": "k in [l, floor(40*ln(n+2)+40)]",
        "note": "v(n,k) >= 2 becomes overwhelmingly likely for larger k; this is a "
                "truncation, so 'v_l(n) <= 1' below really means 'no witness k in "
                "the stated window', a caveat that matters only if the true sup is "
                "achieved at some k beyond the window for an n not listed here.",
        "by_l": {},
    }
    expected_from_selection_report = {1: 330, 2: 1365, 3: 1365, 5: 2415, 8: 4895, 13: 11655, 20: 27714}

    if not args.skip_task2:
        for l in ls:
            exc_sorted, tl = task2_exceptions(N, spf, l, log_path, block_size)
            largest = exc_sorted[-1] if exc_sorted else None
            task2_summary["by_l"][str(l)] = {
                "count": len(exc_sorted),
                "largest": largest,
                "expected_largest_up_to_1e6_from_selection_report": expected_from_selection_report[l],
                "matches_expected": (largest == expected_from_selection_report[l]) if N >= 10**6 else None,
                "runtime_seconds": tl,
            }
            list_path = os.path.join(outdir, f"exceptions_l{l}.csv")
            with open(list_path, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["n"])
                for x in exc_sorted:
                    w.writerow([x])
            task2_summary["by_l"][str(l)]["list_file"] = os.path.basename(list_path)
            task2_summary["by_l"][str(l)]["list_sha256"] = sha256_of(list_path)
            del exc_sorted
            gc.collect()
            mem_checkpoint(log_path, f"after task2 l={l}")

    with open(os.path.join(outdir, "task2_summary.json"), "w") as f:
        json.dump(task2_summary, f, indent=2)

    t_total = time.time() - t_start
    with open(log_path, "a") as lf:
        lf.write(f"=== gen_witness.py run end. total_elapsed={t_total:.1f}s ===\n")

    print(json.dumps({"task1": task1_summary, "task2": task2_summary, "total_runtime_seconds": t_total},
                      indent=2, default=str))


if __name__ == "__main__":
    main()
