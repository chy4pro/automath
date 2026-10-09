"""Batch 3: adversarial search over B4 sets A in {0..N-1} maximising W = sum_{0<|x|<u} T(x)(u-|x|)  (min D).
Maximal-set hill climbing with random restarts; W is monotone in A so only maximal B4 sets matter."""
import sys, time, random, itertools, json, numpy as np
sys.path.insert(0, '.')
from b4l_common import *

def valid_adders(A, cand, N):
    """boolean mask over cand: adding c keeps B4. new sums = k*c + (multiset sums of size 4-k of A), k=1..4."""
    A = list(A)
    sums = {j: [sum(c) for c in itertools.combinations_with_replacement(A, j)] for j in range(4)}
    S4 = np.array([sum(c) for c in itertools.combinations_with_replacement(A, 4)], dtype=np.int64) if A else np.zeros(0, np.int64)
    parts = [np.array(sums[3], dtype=np.int64), np.array(sums[2], dtype=np.int64), np.array(sums[1], dtype=np.int64), np.array(sums[0], dtype=np.int64)]
    cols = [np.add.outer(cand * (1 + i), p) for i, p in enumerate(parts) if len(p)]
    # k = 1 + i copies of c with 3-i-th... parts[i] has multisets of size 3-i, new sums (i+1)*c + part
    new = np.concatenate(cols, axis=1)
    new_sorted = np.sort(new, axis=1)
    dup = (new_sorted[:, 1:] == new_sorted[:, :-1]).any(axis=1)
    inS4 = np.isin(new, S4).any(axis=1) if len(S4) else np.zeros(len(cand), bool)
    return ~(dup | inS4)

def Wval(A, u):
    r = np.array([sorted(A)], dtype=np.int64)
    return int(W_rows(r, np.array([u], dtype=np.int64))[0])

def fill(A, N, rng):
    A = set(A)
    cand = np.array([c for c in range(N) if c not in A], dtype=np.int64)
    while len(cand):
        ok = valid_adders(sorted(A), cand, N)
        cand = cand[ok]
        if len(cand) == 0: break
        c = int(cand[rng.randrange(len(cand))]); A.add(c)
        cand = cand[cand != c]
    return A

def search(N, budget, seed):
    rng = random.Random(seed); u = u_of(N)
    t0 = time.process_time(); best = (-1, None); evals = 0
    cur = fill(set(), N, rng); curW = Wval(cur, u)
    while time.process_time() - t0 < budget:
        B = set(cur)
        for e in rng.sample(sorted(B), min(len(B), rng.choice([1, 1, 2, 2, 3]))): B.discard(e)
        B = fill(B, N, rng); w = Wval(B, u); evals += 1
        if w >= curW: cur, curW = B, w
        if curW > best[0]: best = (curW, sorted(cur))
        if rng.random() < 0.02:                              # random restart
            cur = fill(set(), N, rng); curW = Wval(cur, u)
            if curW > best[0]: best = (curW, sorted(cur))
    W, A = best
    return N, u, W, A, evals

if __name__ == '__main__':
    budget = float(sys.argv[1]); out = {}
    for N in (256, 512, 1024):
        N, u, W, A, ev = search(N, budget, seed=N)
        assert b4_brute(A)
        D, u2 = brute_D(A, N)                                 # independent recomputation
        assert u2 == u and D == 4 * u * (u - 1) - W, (D, u, W)
        out[N] = dict(N=N, u=u, A=A, W=W, D=D, rho=100 * D / (u * (u - 1)), F=W / (4 * u * (u - 1)), m=len(A), evals=ev, fail=100 * D < u * (u - 1))
        print(out[N], flush=True)
        json.dump(out, open('batch3_result.json', 'w'))
