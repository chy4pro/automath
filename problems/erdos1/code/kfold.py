# Check the general k-fold bound: for S subset of [n-1] (0-based indices < n-1), R = complement in [n-1] nonempty,
# c = max a_R, k = |S|+1:
#   #{X in (-a_n,a_n)} >= 2*beta(n-k) * #{eps_S : |W| <= 2(a_n - c)} - 1   (and <= a_n)
import random, itertools
import numpy as np
from windows import all_pm_sums, is_dss, beta
from exhaust import enum

def check(a, max_subsets=300, rng=None):
    a = sorted(a); n = len(a); an = a[-1]
    X = all_pm_sums(a)
    occ = int(np.count_nonzero((X > -an) & (X < an)))
    assert occ <= an
    idx = list(range(n - 1))
    subsets = []
    for r in range(0, n - 1):
        for S in itertools.combinations(idx, r):
            subsets.append(S)
    if rng is not None and len(subsets) > max_subsets:
        subsets = rng.sample(subsets, max_subsets)
    best = 0
    for S in subsets:
        R = [i for i in idx if i not in S]
        c = max(a[i] for i in R)
        k = len(S) + 1
        W = all_pm_sums([a[i] for i in S])
        cnt = int(np.count_nonzero(np.abs(W) <= 2 * (an - c)))
        b = 2 * beta(n - k) * cnt - 1 if cnt else 0
        assert occ >= b, (a, S, occ, b)
        best = max(best, b)
    return best

rng = random.Random(7)
tot = 0; improved = 0
for n, M in [(4, 12), (5, 20), (6, 30), (7, 48)]:
    for a in enum(n, M):
        b = check(list(a)); tot += 1
        improved += b > 2 * beta(n - 1)
for trial in range(1500):
    n = rng.randint(5, 13)
    a = sorted({max(1, int(2**i * rng.uniform(0.55, 1.0))) for i in range(n)})
    if len(a) == n and is_dss(a):
        b = check(a, rng=rng); tot += 1
        improved += b > 2 * beta(n - 1)
print("sets checked:", tot, "; sets where some k-fold choice beats 2*beta(n-1):", improved)
