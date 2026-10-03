# Check the conditional 2-fold bound: if a_{n-1} <= 2(a_n - a_{n-2}) then a_n >= 4 beta(n-2) - 2,
# via the exact count identity #{X in (-a,a)} = N(-2a-b,-b)+N(-2a+b,b)+N(-b,2a-b)+N(b,2a+b).
import random
import numpy as np
from math import comb
from windows import all_pm_sums, is_dss, beta
from exhaust import enum

def N(Z, lo, hi):
    return int(np.count_nonzero((Z > lo) & (Z < hi)))

def check(a):
    a = sorted(a); n = len(a); A, B, C = a[-1], a[-2], a[-3]
    X = all_pm_sums(a); Z = all_pm_sums(a[:-2])
    lhs = N(X, -A, A)
    rhs = N(Z, -2*A-B, -B) + N(Z, -2*A+B, B) + N(Z, -B, 2*A-B) + N(Z, B, 2*A+B)
    assert lhs == rhs, a
    assert lhs <= A
    cond = B <= 2*(A - C)
    if cond:
        hm = N(Z, -2*C, 0)
        assert hm >= beta(n-2)
        assert A >= 4*beta(n-2) - 2, a
    return cond

cnt = 0; cc = 0
for n, M in [(4, 12), (5, 20), (6, 30), (7, 48)]:
    for a in enum(n, M):
        cnt += 1; cc += check(list(a))
for n in range(4, 18):
    cc += check([2**i for i in range(n)]); cnt += 1
# random DSS sets: perturbed powers of two
rng = random.Random(1)
for trial in range(3000):
    n = rng.randint(5, 14)
    a = sorted({max(1, int(2**i * rng.uniform(0.6, 1.0))) for i in range(n)})
    if len(a) == n and is_dss(a):
        cnt += 1; cc += check(a)
print("sets checked:", cnt, " satisfying 2-fold hypothesis:", cc)
