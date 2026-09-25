#!/usr/bin/env python3
"""Erdos #488 enhanced search.

Two criteria per set A:
  1. order-aware: exists n < m (both >= maxA, m <= M) with f(m) >= 2 f(n)
  2. delta criterion: 2*min_{n in [maxA, M]} f(n) < delta = asymptotic density
     (then a violating m exists far out even beyond M, since f(m) -> delta)
Plus adversarial hill-climbing maximizing violation objective.
Hard internal time cap.
"""
import itertools
import random
import time
from math import gcd

TIME_CAP_SEC = 540
t0 = time.time()
random.seed(487)  # deterministic reproducibility


def lcm(a, b):
    return a // gcd(a, b) * b


def density(A):
    """Exact asymptotic density of the multiple set of A via inclusion-exclusion."""
    d = 0.0
    n = len(A)
    for mask in range(1, 1 << n):
        l = 1
        for i in range(n):
            if mask >> i & 1:
                l = lcm(l, A[i])
                if l > 10**15:
                    break
        d += (-1) ** (bin(mask).count("1") + 1) / l
    return d


def analyze(A, mfactor=80):
    """Return (order_ratio, delta_ratio, details). ratio >= 1.0 means violation."""
    A = sorted(set(A))
    amax = A[-1]
    M = mfactor * amax
    hit = bytearray(M + 1)
    for a in A:
        hit[a::a] = b"\x01" * ((M) // a)
    c = 0
    minf_n, minf_c = amax, None  # argmin of f over n seen so far
    order_worst = 0.0
    order_arg = None
    fmin = None  # (c, n) minimal f over full range
    prefix = []
    for i in range(1, M + 1):
        c += hit[i]
        prefix.append(c)
        if i >= amax:
            if minf_c is None:
                minf_c = c
                minf_n = i
            else:
                r = (c * minf_n) / (2 * minf_c * i)
                if r > order_worst:
                    order_worst, order_arg = r, (minf_n, i)
                if c * minf_n < minf_c * i:
                    minf_n, minf_c = i, c
            if fmin is None or c * fmin[1] < fmin[0] * i:
                fmin = (c, i)
    d = density(A) if len(A) <= 16 else None
    delta_ratio = None
    if d and fmin:
        delta_ratio = d / (2 * fmin[0] / fmin[1])
    return order_worst, order_arg, delta_ratio, fmin


def main():
    worst = []
    tried = 0
    # exhaustive: sizes 1-3 from [2..60], size 4 from [2..30]
    spaces = [(1, range(2, 61)), (2, range(2, 61)), (3, range(2, 41)),
              (4, range(2, 31))]
    for size, rng in spaces:
        for A in itertools.combinations(rng, size):
            if any(b % a == 0 for a, b in itertools.permutations(A, 2)):
                continue
            ow, oa, dr, fm = analyze(A, mfactor=60)
            tried += 1
            score = max(ow, dr or 0)
            worst.append((score, ow, dr, tuple(A), oa))
            if ow >= 1.0 or (dr or 0) >= 1.0:
                print(f"VIOLATION A={A} order={ow:.4f}@{oa} delta_ratio={dr}")
                return
            if time.time() - t0 > TIME_CAP_SEC * 0.6:
                print(f"cap-part1 size={size} tried={tried}")
                break
        else:
            continue
        break
    worst.sort(reverse=True)
    print(f"exhaustive: {tried} sets, no violation. top5:")
    for s, ow, dr, A, oa in worst[:5]:
        print(f"  score={s:.4f} order={ow:.4f} delta={dr and round(dr,4)} A={A} at {oa}")

    # adversarial hill climb from top seeds and random starts
    seeds = [list(w[3]) for w in worst[:6]] + \
            [random.sample(range(2, 120), random.randint(2, 8)) for _ in range(10)]
    best_hc = (0, None)
    for A in seeds:
        cur = analyze(A)[0]
        for _ in range(400):
            if time.time() - t0 > TIME_CAP_SEC:
                break
            B = sorted(set(A))
            op = random.random()
            if op < 0.35 and len(B) > 1:
                B.remove(random.choice(B))
            elif op < 0.7:
                B.append(random.randint(2, 150))
            else:
                B.remove(random.choice(B))
                B.append(random.randint(2, 150))
            B = sorted(set(B))
            if not B or len(B) > 10:
                continue
            if any(y % x == 0 for x, y in itertools.permutations(B, 2)):
                continue
            ow = analyze(B)[0]
            if ow >= 1.0:
                print(f"VIOLATION (hillclimb) A={B} ratio={ow:.4f}")
                return
            if ow > cur:
                A, cur = B, ow
        if cur > best_hc[0]:
            best_hc = (cur, list(A))
        if time.time() - t0 > TIME_CAP_SEC:
            break
    print(f"hillclimb best: ratio={best_hc[0]:.4f} A={best_hc[1]}")
    print(f"RESULT: no violation found. elapsed={time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
