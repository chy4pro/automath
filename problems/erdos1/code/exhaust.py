"""Exhaustive enumeration of DSS sets with n elements and max <= M (small n).
Reports the minimum max, the number of sets found, and checks for every set found:
  (i)  #{X in (-a_n,a_n)} = 2 #{Y in (-2a_n,0)} <= a_n
  (ii) #{Y in (-2a_{n-1},0)} >= beta(n-1)   (Harper on Q_{n-1})
and the final inequality a_n >= 2 beta(n-1).
"""
import sys, time
from math import comb
from itertools import product

def beta(m):
    return comb(m, m // 2)

def pm_sums(a):
    X = [0]
    for ai in a:
        X = [x - ai for x in X] + [x + ai for x in X]
    return X

def enum(n, M):
    found = []
    need_total = 2 ** n - 1
    def rec(cur, bits, total, start):
        k = len(cur)
        if k == n:
            found.append(tuple(cur))
            return
        rem = n - k
        # remaining elements are distinct and <= M: max possible added sum
        maxadd = sum(range(M - rem + 1, M + 1))
        if total + maxadd < need_total:
            return
        for x in range(start, M - rem + 2):
            if bits & (bits << x):
                continue
            # quick feasibility: total + x + (rem-1 largest) >= need
            cur.append(x)
            rec(cur, bits | (bits << x), total + x, x + 1)
            cur.pop()
    rec([], 1, 0, 1)
    return found

def check(a):
    n = len(a); an = a[-1]
    X = pm_sums(a); Y = pm_sums(a[:-1])
    occ = sum(1 for x in X if -an < x < an)
    yc = sum(1 for y in Y if -2 * an < y < 0)
    yc2 = sum(1 for y in Y if -2 * a[-2] < y < 0) if n >= 2 else 0
    assert occ == 2 * yc <= an, a
    assert yc2 >= beta(n - 1), a
    assert an >= 2 * beta(n - 1), a

if __name__ == "__main__":
    targets = {3: 6, 4: 9, 5: 15, 6: 26, 7: 46}
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    for n in range(3, nmax + 1):
        t = time.time()
        sets = enum(n, targets[n])
        for a in sets:
            check(list(a))
        mn = min(a[-1] for a in sets)
        best = [a for a in sets if a[-1] == mn]
        print(f"n={n} M={targets[n]} #DSS sets={len(sets)} min a_n={mn} (2b(n-1)={2*beta(n-1)}, b(n)={beta(n)}) "
              f"optimal sets={best[:4]} time={time.time()-t:.1f}s")
