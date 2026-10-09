import sys, time, itertools, json, numpy as np
sys.path.insert(0, '.')
from b4l_common import *
res = {}
t0 = time.process_time()
# (a) dense: all subsets of {0..31}, 1..4 elements, B4 kept
tot = {}; keep = {}
accs = Acc('dense{0..31}<=4')
nonb4 = 0
for k in range(1, 5):
    rows = np.array(list(itertools.combinations(range(32), k)), dtype=np.int64)
    ok = b4_ok(rows)
    tot[k] = len(rows); nonb4 += int((~ok).sum())
    rows = rows[ok]
    # cross-check b4_ok against brute force on a random subset
    rng = np.random.default_rng(1)
    for i in rng.choice(len(ok), size=min(2000, len(ok)), replace=False):
        assert b4_brute(list(itertools.combinations(range(32), k))[i] if False else tuple(int(v) for v in np.array(list(itertools.islice(itertools.combinations(range(32), k), int(i), int(i) + 1)))[0])) == bool(ok[i])
    norm = rows - rows[:, :1]
    norm = np.unique(norm, axis=0)                       # translation cache: key = shape
    refl = np.unique(norm[:, -1:] - norm[:, ::-1], axis=0); assert np.array_equal(refl, norm)
    keep[k] = (len(rows), len(norm))
    accs.add(norm)
res['dense'] = dict(subsets_total=tot, b4_kept={k: v[0] for k, v in keep.items()}, unique_shapes={k: v[1] for k, v in keep.items()},
                    nonb4=nonb4, invalid_in_eval=accs.invalid, nfail=len(accs.failures), failures=accs.failures[:10], best=accs.best, cover=accs.cover)
print('dense', res['dense'], flush=True)
cpu_a = time.process_time() - t0
# (b) greedy prefixes and dilates
G = [0, 1, 5, 21, 55, 153, 368, 856, 1424, 2603, 4967, 8194]
assert b4_brute(G), 'greedy list itself is not B4'
byk = {}
shapes = 0; raw = 0
for k in range(1, 13):
    acc = Acc('greedy prefix k=%d' % k)
    rows = []
    for d in range(1, 17):
        A = [d * g for g in G[:k]]
        assert b4_brute(A), (k, d)           # fixture validity (brute, independent of b4_ok)
        rows.append(A); raw += 1
    rows = np.array(rows, dtype=np.int64)
    assert b4_ok(rows).all()
    rows = np.unique(rows, axis=0); shapes += len(rows)
    refl = np.unique(rows[:, -1:] - rows[:, ::-1], axis=0)
    acc.add(rows); acc.add(refl)                         # reflections evaluated explicitly
    byk[k] = dict(n=len(rows), nfail=len(acc.failures), failures=acc.failures[:5], best=acc.best, cover=acc.cover, invalid=acc.invalid)
    print('prefix', k, byk[k]['best'], flush=True)
res['greedy'] = byk; res['greedy_raw'] = raw; res['greedy_shapes'] = shapes
res['cpu_dense'] = cpu_a; res['cpu_total'] = time.process_time() - t0
json.dump(res, open('batch2_result.json', 'w'))
print('cpu', res['cpu_dense'], res['cpu_total'])
