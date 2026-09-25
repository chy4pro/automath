#!/usr/bin/env python3
"""Erdos #488 counterexample search.

A finite set A (elements >= 2), B = {n >= 1 : some a in A divides n}.
Conjecture: for every m > n >= max(A),  |B cap [1,m]|/m < 2 |B cap [1,n]|/n.
A counterexample is (A, n, m) with f(m) >= 2 f(n).

Strategy: enumerate small A exhaustively + structured families; for each A,
sieve B up to M, then check max over m of f(m) / min over n<m of f(n).
Exact rational comparison: f(m) >= 2 f(n)  <=>  c_m * n >= 2 * c_n * m.
Hard internal time cap; prints best (worst-case) ratios found.
"""
import itertools
import time

TIME_CAP_SEC = 420
M_FACTOR = 60          # sieve up to M_FACTOR * max(A)
BASE_RANGE = range(2, 26)
MAX_SIZE = 4

t0 = time.time()
best = []  # (ratio, A, n, m)


def check(A):
    amax = max(A)
    M = M_FACTOR * amax
    hit = bytearray(M + 1)
    for a in A:
        hit[a::a] = b"\x01" * len(hit[a::a])
    # prefix counts
    c = [0] * (M + 1)
    s = 0
    for i in range(1, M + 1):
        s += hit[i]
        c[i] = s
    # min over n >= amax of f(n) tracked as we scan m upward:
    # violation iff exists n in [amax, m) with c[m]*n >= 2*c[n]*m
    # track candidate n minimizing c[n]/n exactly via pairwise compare
    bn, bcn = amax, c[amax]  # best (minimal f) n so far
    worst = (0.0, None, None)
    for m in range(amax + 1, M + 1):
        # compare f(m) vs 2 f(bn)
        lhs = c[m] * bn
        rhs = 2 * bcn * m
        r = lhs / rhs if rhs else 99.0
        if r > worst[0]:
            worst = (r, bn, m)
        if lhs >= rhs:
            print(f"COUNTEREXAMPLE A={sorted(A)} n={bn} m={m} "
                  f"f(n)={bcn}/{bn} f(m)={c[m]}/{m}")
            return True
        # update minimal f(n) candidate with n = m
        if c[m] * bn < bcn * m:  # f(m) < f(bn)
            bn, bcn = m, c[m]
    best.append((worst[0], tuple(sorted(A)), worst[1], worst[2]))
    return False


def main():
    tried = 0
    # exhaustive small sets
    for size in range(1, MAX_SIZE + 1):
        for A in itertools.combinations(BASE_RANGE, size):
            if any(b % a == 0 for a, b in itertools.permutations(A, 2)):
                continue  # nested divisors are redundant
            if check(A):
                return
            tried += 1
            if time.time() - t0 > TIME_CAP_SEC:
                print(f"TIME CAP at size={size}, tried={tried}")
                break
        else:
            continue
        break
    # structured families: primes blocks, near-half blocks
    fams = []
    primes = [p for p in range(2, 200)
              if all(p % q for q in range(2, int(p ** 0.5) + 1))]
    for k in (3, 5, 8):
        fams.append(tuple(primes[:k]))
        fams.append(tuple(primes[2:2 + k]))
    for a in (10, 20, 30):
        fams.append(tuple(range(a, 2 * a, 2)))
    for A in fams:
        if time.time() - t0 > TIME_CAP_SEC:
            break
        if check(A):
            return
        tried += 1
    best.sort(reverse=True)
    print(f"RESULT: no counterexample in {tried} sets, elapsed={time.time()-t0:.1f}s")
    print("closest ratios (f(m) / 2f(n), 1.0 would violate):")
    for r, A, n, m in best[:10]:
        print(f"  ratio={r:.4f} A={A} n={n} m={m}")


if __name__ == "__main__":
    main()
