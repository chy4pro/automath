#!/usr/bin/env python3
"""
Independent re-check of r5_scan.py (different code path: sympy factorisation, and v(n,k)
evaluated from the Formal Conjectures definition, not from Lemma 1.1):

  v_FC(n,k) = #{ p prime : p | n+k  and  p does not divide n+i for every 0 <= i < k }.

Checks, for a sample of n:
  (1) k3_l(n) for l = 0, 1, 2 (exact: search up to the cube-root bound);
  (2) for C in (2,5,10), K = floor(C log n): t0..t3, sigma0, sigma, Pcount,
      computed from sympy factorisations of n..n+K;
and compares with the scan code evaluated on the one-element segment [n, n+1).
The sample = all record holders ('top' lists) and extremal n stored in the scan output,
up to --nnone of the n with k3 = -1 per l, and --nrand uniformly random n per file.

Usage: python3 r5_recheck.py data/scan_*.jsonl --nrand 200 --nnone 50 --seed 1
"""
import sys, json, math, random, argparse
from sympy import factorint, primerange, isprime
sys.path.insert(0, __file__.rsplit('/', 1)[0] if '/' in __file__ else '.')
import r5_scan

def v_fc(n, k):
    c = 0
    for p in factorint(n + k):
        if all((n + i) % p for i in range(k)):
            c += 1
    return c

def kbound_n(n):
    k = 0
    while (k + 2) * (k + 3) * (k + 4) <= n + k + 1:
        k += 1
    return k

def k3(n, l):
    for k in range(l, kbound_n(n) + 1):
        if v_fc(n, k) >= 3:
            return k
    return -1

def block(n, C):
    K = math.floor(C * math.log(n))
    P = list(primerange(2, K + 1))
    piK = len(P)
    if piK == 0:
        return None
    fac = [factorint(n + j) for j in range(K + 1)]
    omK = [sum(1 for p in f if p > K) for f in fac]
    cap = [max(0, 2 - o) for o in omK]
    t = [sum(1 for o in omK if o == i) for i in (0, 1, 2)] + [sum(1 for o in omK if o >= 3)]
    sigma0 = piK - (2 * t[0] + t[1])
    # J = positions j carrying some prime p in (j, K]
    capJ = sum(cap[j] for j in range(K + 1) if any(j < p <= K for p in fac[j]))
    sigma = piK - capJ
    # (P): ceil(n/p) prime > K
    Pc = sum(1 for p in P if (-(-n // p)) > K and isprime(-(-n // p)))
    return dict(K=K, piK=piK, t=t, sigma0=sigma0, sigma=sigma, Pc=Pc)

def scan_one(n):
    return r5_scan.process((n, 1, n + 1))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--nrand', type=int, default=100)
    ap.add_argument('--nnone', type=int, default=30)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--skip-block-above', type=float, default=1e13)
    ap.add_argument('--big', nargs='*', default=[], help='r5_bigsample output to re-check (rows with e <= 18)')
    ap.add_argument('--nbig', type=int, default=20)
    a = ap.parse_args()
    bad_big = 0
    if a.big:
        rng0 = random.Random(a.seed + 1)
        rows = [json.loads(x) for fn in a.big for x in open(fn)]
        rows = [r for r in rows if r['e'] <= 18]
        pick = rng0.sample(rows, min(a.nbig, len(rows)))
        for r in pick:
            n = int(r['n'])
            for l, key in ((0, 'k3_l0'), (1, 'k3_l1')):
                got = k3(n, l)
                if got != r[key]:
                    bad_big += 1; print('MISMATCH big k3', n, l, got, r[key])
            for b in r['blocks']:
                g = block(n, b['C'])
                for k1, k2 in (('K', 'K'), ('piK', 'piK'), ('sigma0', 'sigma0'), ('sigma', 'sigma'), ('Pc', 'Pc')):
                    if g[k1] != b[k2]:
                        bad_big += 1; print('MISMATCH big block', n, b['C'], k1, g[k1], b[k2])
                if [g['t'][0], g['t'][1], g['t'][2] + g['t'][3]] != [b['t0'], b['t1'], b['t2p']]:
                    bad_big += 1; print('MISMATCH big t', n, b['C'], g['t'], b)
        print(f'# big-n re-check: {len(pick)} rows (e <= 18), mismatches = {bad_big}')
    rng = random.Random(a.seed)
    sample = set()
    for fn in a.files:
        rows = [json.loads(x) for x in open(fn)]
        lo = min(r['A'] for r in rows); hi = max(r['A'] + r['S'] for r in rows)
        for r in rows:
            for l in (0, 1, 2):
                for n, _ in r[f'l{l}']['top'][:3]:
                    sample.add(n)
            for C in (2, 5, 10):
                st = r[f'C{C}']
                for key in ('min_sigma0', 'min_sigma', 'max_t1', 'max_P_frac'):
                    if st.get(key):
                        sample.add(st[key][1])
        nones = {l: sorted({n for r in rows for n in r[f'l{l}']['none']}) for l in (0, 1, 2)}
        for l in (0, 1, 2):
            sample.update(rng.sample(nones[l], min(a.nnone, len(nones[l]))))
        for _ in range(a.nrand):
            sample.add(rng.randrange(lo, hi))
    sample = sorted(sample)
    print(f'# re-checking {len(sample)} values of n')
    bad = 0; nblock = 0
    for n in sample:
        s = scan_one(n)
        for l in (0, 1, 2):
            ref = s[f'l{l}']['max_k3']; ref = -1 if ref is None else ref
            got = k3(n, l)
            if got != ref:
                bad += 1; print('MISMATCH k3', n, l, got, ref)
        if n <= a.skip_block_above:
            for C in (2, 5, 10):
                b = block(n, C)
                st = s[f'C{C}']
                if b is None:
                    continue
                nblock += 1
                ref = dict(sigma0=st['min_sigma0'][0], sigma=st['min_sigma'][0], K=st['min_sigma'][2],
                           piK=st['min_sigma'][3], t=[x for x in st['sum_t']], Pc=st['max_P_frac'][2])
                for key in ('K', 'piK', 'sigma0', 'sigma', 't', 'Pc'):
                    if b[key] != ref[key]:
                        bad += 1; print('MISMATCH block', n, C, key, b[key], ref[key])
    print(f'# done: {len(sample)} n, k3 checks = {3*len(sample)}, block checks = {nblock}, mismatches = {bad}')
    bad += bad_big
    print('RECHECK', 'PASS' if bad == 0 else 'FAIL')

if __name__ == '__main__':
    main()
