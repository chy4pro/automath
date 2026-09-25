#!/usr/bin/env python3
"""
Erdos #889, level 3, round 1 -- R5 numerical reconnaissance (segmented, numpy only).

For every n in [lo, hi) (processed in segments of S integers) this computes:

  k3_l(n) = min{ k >= l : v(n,k) >= 3 }   for l in LS = (0, 1, 2),
            v(n,k) = #{ primes p | n+k : p > k }        (Lemma 1.1 of PROOF_THEOREM_A.md).
            The search is EXACT, not windowed: v(n,k) >= 3 forces n+k >= (k+1)(k+2)(k+3),
            so k runs up to the largest k allowed by that bound on the segment; an n with
            no hit is recorded as k3 = -1, meaning v_l(n) <= 2 (no k >= l at all).

  For C in CS = (2, 5, 10) and K = floor(C log n) (natural log), with l = 0:
     omK(m)  = #{ primes p | m : p > K }             ("type" of the term m)
     cap(m)  = max(0, 2 - omK(m))                     (free slots under (H3))
     d_j     = #{ primes p in (j, K] : p | n+j }      (entry primes at position j)
     t_i     = #{ 0 <= j <= K : omK(n+j) = i }, i = 0, 1, 2, and t3 = #{omK >= 3}
     sigma0  = pi(K) - (2 t0 + t1)                    (block-product / R2 certificate)
     sigma   = pi(K) - sum_{j in J} cap(n+j),  J = { j : d_j >= 1 }   (R1 certificate)
     Pcount  = #{ p <= K : ceil(n/p) is a prime > K }  (the configuration (P) of ROUND1.md)
  sigma > 0 (or sigma0 > 0) certifies, by pigeonhole, some j <= K with v(n,j) >= 3.
  (Sum_j d_j = pi(K) at l = 0 because each p <= K enters the block at j = (-n mod p) < p.)

Output: one JSON line per segment (aggregates, records, extremal n) to --out.

Usage:
  export PATH="$HOME/.local/bin:$PATH"
  python3 r5_scan.py --lo 2 --hi 100000000 --seg 1000000 --workers 6 --out data/scan_1e8.jsonl
"""
import argparse, json, math, sys, time
import numpy as np
from multiprocessing import Pool

LS = (0, 1, 2)
CS = (2, 5, 10)
W = 12  # max distinct prime factors stored (product of the 12 smallest primes > 7e12)


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0].astype(np.int64)


def kbound(N):
    """largest k >= 0 with (k+1)(k+2)(k+3) <= N + k  (v(n,k) >= 3 impossible beyond, for n <= N)"""
    k = 0
    while (k + 2) * (k + 3) * (k + 4) <= N + k + 1:
        k += 1
    return k


def factor_table(A, L, primes):
    """distinct prime factors of m in [A, A+L), ascending, zero padded; A >= 1."""
    cof = np.arange(A, A + L, dtype=np.int64)
    F = np.zeros((L, W), dtype=np.int64)
    cnt = np.zeros(L, dtype=np.int64)
    top = A + L - 1
    for p in primes:
        p = int(p)
        if p * p > top:
            break
        idx = np.arange((-A) % p, L, p)
        if idx.size == 0:
            continue
        F[idx, cnt[idx]] = p
        cnt[idx] += 1
        sub = idx
        while sub.size:
            cof[sub] //= p
            sub = sub[cof[sub] % p == 0]
    rem = np.nonzero(cof > 1)[0]
    F[rem, cnt[rem]] = cof[rem]
    cnt[rem] += 1
    return F, cnt


def pi_small(x, plist):
    return int(np.searchsorted(plist, x, side='right'))


def process(args):
    A, S, maxN = args
    tstart = time.time()
    S = min(S, maxN - A)
    kb = kbound(A + S - 1)
    Kmax = max(int(math.floor(c * math.log(A + S - 1))) for c in CS)
    L = S + max(kb, Kmax) + 2
    primes = primes_upto(int(math.isqrt(A + L)) + 2)
    F, cnt = factor_table(A, L, primes)
    out = {'A': A, 'S': S, 'kbound': kb}
    # ---- k3 for each l ----
    for l in LS:
        res = np.full(S, -1, dtype=np.int64)
        unres = np.arange(S)
        k = l
        while unres.size and k <= kb:
            v = (F[unres + k] > k).sum(axis=1)
            hit = v >= 3
            res[unres[hit]] = k
            unres = unres[~hit]
            k += 1
        ok = res >= 0
        hist = np.bincount(res[ok]) if ok.any() else np.array([])
        n_arr = A + np.arange(S)
        ratio = np.where(ok, res / np.log(n_arr.astype(float)), -1.0)
        imax = int(np.argmax(np.where(ok, res, -1)))
        out[f'l{l}'] = {
            'hist': {int(i): int(c) for i, c in enumerate(hist) if c},
            'none': [int(A + i) for i in np.nonzero(~ok)[0]],
            'n_none': int((~ok).sum()),
            'max_k3': int(res[imax]) if ok.any() else None, 'argmax': int(A + imax),
            'max_ratio_logn': float(ratio.max()), 'argmax_ratio': int(A + int(np.argmax(ratio))),
            'top': sorted([[int(A + i), int(res[i])] for i in np.argsort(-np.where(ok, res, -1))[:20]],
                          key=lambda x: -x[1]),
        }
    # ---- block statistics at K = floor(C log n), l = 0 ----
    plist = primes_upto(Kmax + 2)
    n_arr = A + np.arange(S)
    for C in CS:
        Kn = np.floor(C * np.log(n_arr.astype(float))).astype(np.int64)
        stats = {'min_sigma0': None, 'min_sigma': None, 'n_sigma0_le0': 0, 'n_sigma_le0': 0,
                 'sum_t': [0, 0, 0, 0], 'max_t0': [-1, 0], 'max_t1': [-1, 0], 'max_P_frac': [-1.0, 0],
                 'max_2t0t1_over_piK': [-1.0, 0], 'count': 0}
        for K in np.unique(Kn):
            K = int(K)
            grp = np.nonzero(Kn == K)[0]
            i0, i1 = int(grp[0]), int(grp[-1]) + 1  # contiguous
            piK = pi_small(K, plist)
            if piK == 0:
                continue
            m_lo, m_hi = i0, i1 + K  # table rows needed
            Fm = F[m_lo:m_hi]
            omK = (Fm > K).sum(axis=1)
            cap = np.maximum(0, 2 - omK)
            small = np.where((Fm > 0) & (Fm <= K), Fm, 0)
            g = small.max(axis=1)  # largest prime factor <= K (0 if none)
            G = i1 - i0
            # window sums over j = 0..K  (rows r = i - i0 + j)
            def wsum(x):
                c = np.concatenate(([0], np.cumsum(x)))
                return c[K + 1:K + 1 + G] - c[0:G]
            t0 = wsum(omK == 0); t1 = wsum(omK == 1); t2 = wsum(omK == 2); t3 = wsum(omK >= 3)
            sigma0 = piK - (2 * t0 + t1)
            capJ = np.zeros(G, dtype=np.int64)
            for j in range(K + 1):
                capJ += (g[j:j + G] > j) * cap[j:j + G]
            sigma = piK - capJ
            # configuration (P): p <= K with ceil(n/p) a prime > K, i.e. n + ((-n) mod p) = p * q, q prime > K
            Pc = np.zeros(G, dtype=np.int64)
            nn = n_arr[i0:i1]
            for p in plist[plist <= K]:
                p = int(p)
                jp = (-nn) % p
                rows = np.arange(G) + jp  # row index into Fm
                r = Fm[rows]
                m = nn + jp
                c2 = (cnt[m_lo + rows] == 2)
                big = r.max(axis=1)
                Pc += (c2 & (r[:, 0] == p) & (big > K) & (m == p * big)).astype(np.int64)
            # aggregate
            s0 = int(sigma0.min()); s = int(sigma.min())
            if stats['min_sigma0'] is None or s0 < stats['min_sigma0'][0]:
                stats['min_sigma0'] = [s0, int(nn[int(np.argmin(sigma0))]), K, piK]
            if stats['min_sigma'] is None or s < stats['min_sigma'][0]:
                stats['min_sigma'] = [s, int(nn[int(np.argmin(sigma))]), K, piK]
            stats['n_sigma0_le0'] += int((sigma0 <= 0).sum())
            stats['n_sigma_le0'] += int((sigma <= 0).sum())
            for a, t in enumerate((t0, t1, t2, t3)):
                stats['sum_t'][a] += int(t.sum())
            if int(t0.max()) > stats['max_t0'][0]:
                stats['max_t0'] = [int(t0.max()), int(nn[int(np.argmax(t0))])]
            if int(t1.max()) > stats['max_t1'][0]:
                stats['max_t1'] = [int(t1.max()), int(nn[int(np.argmax(t1))]), K, piK]
            fr = Pc / piK
            if float(fr.max()) > stats['max_P_frac'][0]:
                stats['max_P_frac'] = [float(fr.max()), int(nn[int(np.argmax(fr))]), int(Pc.max()), piK]
            q = (2 * t0 + t1) / piK
            if float(q.max()) > stats['max_2t0t1_over_piK'][0]:
                stats['max_2t0t1_over_piK'] = [float(q.max()), int(nn[int(np.argmax(q))])]
            stats['count'] += G
        out[f'C{C}'] = stats
    out['secs'] = round(time.time() - tstart, 2)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lo', type=int, required=True)
    ap.add_argument('--hi', type=int, required=True)
    ap.add_argument('--seg', type=int, default=1_000_000)
    ap.add_argument('--workers', type=int, default=4)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    jobs = [(A, a.seg, a.hi) for A in range(a.lo, a.hi, a.seg)]
    t = time.time()
    with open(a.out, 'a') as f, Pool(a.workers) as pool:
        for r in pool.imap(process, jobs):
            f.write(json.dumps(r) + '\n'); f.flush()
            print(f"[{time.time()-t:7.1f}s] A={r['A']} secs={r['secs']} "
                  f"maxk3(l0)={r['l0']['max_k3']} none0={r['l0']['n_none']} "
                  f"minsig(C10)={r['C10']['min_sigma']}", flush=True)


if __name__ == '__main__':
    main()
