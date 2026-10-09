import sys, time, itertools, json, numpy as np
from math import gcd
sys.path.insert(0, '.')
from fields import families
from b4l_common import *

def run(fam, q, M, blist, brute_t):
    t0 = time.process_time()
    units = np.array([a for a in range(1, M) if gcd(a, M) == 1], dtype=np.int64)
    phi = len(units); nb = len(blist)
    raw = nb * phi * M
    keys = []
    k = len(blist[0][1])
    for b, D in blist:
        D = np.array(D, dtype=np.int64)
        assert (len(D) == k)
        A = np.sort((units[:, None] * D[None, :]) % M, axis=1)        # aD mod M
        if brute_t:                                                    # literal enumeration of every t
            T = np.arange(M, dtype=np.int64)
            for ai in range(phi):
                L = np.sort((A[ai][None, :] + T[:, None]) % M, axis=1)
                rows = L - L[:, :1]
                keys.append(np.unique(rows, axis=0))
        else:                                                          # every t falls in one of k cut classes (rotation r)
            rots = [np.concatenate([A[:, r:], A[:, :r] + M], axis=1) - A[:, r:r+1] for r in range(k)]
            keys.append(np.concatenate(rots, axis=0))
    rows = np.concatenate(keys, axis=0)
    # unique normalised full sets
    rows = np.unique(rows, axis=0)
    return raw, phi, nb, rows, time.process_time() - t0

def subsets_unique(full):
    """all nonempty subsets of each row, normalised by min, grouped by size, unique."""
    n, k = full.shape
    out = {}
    for mask in range(1, 1 << k):
        cols = [i for i in range(k) if mask >> i & 1]
        sub = full[:, cols] - full[:, cols[:1]]
        out.setdefault(len(cols), []).append(np.unique(sub, axis=0))
    return {s: np.unique(np.concatenate(v, axis=0), axis=0) for s, v in out.items()}

if __name__ == '__main__':
    qs = [(2, 1), (3, 1), (2, 2), (5, 1)]
    brute_upto = int(sys.argv[1]) if len(sys.argv) > 1 else 0   # q <= brute_upto uses literal t-loop
    res = {}
    for p, e in qs:
        q = p**e
        fams = families(p, e)
        for fam in ('Bose-Chowla', 'Singer'):
            M, bl = fams[fam]
            c0 = time.process_time()
            raw, phi, nb, full, tfull = run(fam, q, M, bl, q <= brute_upto)
            # reflection closure of the unique full-set family
            refl = np.unique(full[:, -1:] - full[:, ::-1], axis=0)
            assert np.array_equal(refl, full), 'reflection closure fails'
            subs = subsets_unique(full)
            acc = Acc((fam, q))
            for s in sorted(subs): acc.add(subs[s])
            cpu = time.process_time() - c0
            res[f'{fam}|{q}'] = dict(M=M, nb=nb, phi=phi, raw=raw, uniq_full=len(full), uniq_sub={s: len(v) for s, v in subs.items()},
                    invalid=acc.invalid, failures=acc.failures[:20], nfail=len(acc.failures), best=acc.best, cover=acc.cover, cpu=cpu, brute_t=q <= brute_upto)
            print(fam, q, 'M', M, 'b', nb, 'phi', phi, 'raw', raw, 'full', len(full), 'subs', {s: len(v) for s, v in subs.items()},
                  'invalid', acc.invalid, 'fail', len(acc.failures), 'cpu %.1f' % cpu, flush=True)
            for b in BASES: print('   ', b, acc.best[b], flush=True)
            json.dump(res, open('batch1_result_%s.json' % ('brute%d' % brute_upto), 'w'))
