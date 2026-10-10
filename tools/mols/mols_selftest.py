#!/usr/bin/env python3
"""Self-test + baseline order-22 replay. Run: python3 mols_selftest.py"""
import sys, os, json, copy, hashlib, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mols_check import check

def timed(d, k):
    t = time.perf_counter(); r = check(d, k); return r, time.perf_counter() - t

fails = 0
def expect(name, d, k, want_ok, frag=""):
    global fails
    (ok, why), dt = timed(d, k)
    good = ok == want_ok and (want_ok or frag in why)
    fails += not good
    print("%-4s %-46s k=%d -> %s (%s) %.4fs" % ("OK" if good else "BAD", name, k, "ACCEPT" if ok else "REJECT", why, dt))

for p in (5, 7, 11, 13, 23):
    L = [[[(a * i + j) % p for j in range(p)] for i in range(p)] for a in range(1, p)]
    expect("p=%d full" % p, {"n": p, "squares": L}, p - 1, True)
    if p > 5:
        expect("p=%d subset k=4" % p, {"n": p, "squares": L[:4]}, 4, True)
    else:
        expect("p=5 subset k=4 (=full)", {"n": p, "squares": L[:4]}, 4, True)
    base = {"n": p, "squares": L[:4]}
    d = copy.deepcopy(base); r = d["squares"][0][0]; r[0], r[1] = r[1], r[0]
    expect("p=%d swap two cells in a row" % p, d, 4, False, "not Latin")  # columns break
    d = copy.deepcopy(base); d["squares"][1] = copy.deepcopy(d["squares"][0])
    expect("p=%d duplicate square" % p, d, 4, False, "not orthogonal")
    d = copy.deepcopy(base); d["squares"][2][1][1] = p
    expect("p=%d out-of-range symbol" % p, d, 4, False, "out-of-range")
    d = copy.deepcopy(base); d["squares"][2][1][1] = float(d["squares"][2][1][1])
    expect("p=%d float entry" % p, d, 4, False, "non-integer")
    d = copy.deepcopy(base); d["squares"][3][1][1] = True
    expect("p=%d bool entry" % p, d, 4, False, "non-integer")
    d = copy.deepcopy(base); d["squares"][3].pop()
    expect("p=%d wrong shape" % p, d, 4, False, "wrong shape")
    d = copy.deepcopy(base); d["squares"][3][2].pop()
    expect("p=%d ragged row" % p, d, 4, False, "wrong shape")
    expect("p=%d wrong count (k=5 asked)" % p, base, 5, False, "wrong number")
# orthogonality-only failure: Latin but non-orthogonal, distinct squares (L_1 vs L_1 with symbols permuted by a non-... )
p = 7
A = [[(i + j) % p for j in range(p)] for i in range(p)]
B = [[(i + j + 1) % p for j in range(p)] for i in range(p)]  # Latin, different, not orthogonal
expect("p=7 Latin-but-not-orthogonal", {"n": p, "squares": [A, B]}, 2, False, "not orthogonal")

# ---- baseline replay: QDM_21_5_1_1_1 -> OA(5,22) -> 3 Latin squares
M = [[1,13,18,3,16,19,None],[16,19,1,13,18,3,0],[18,3,16,19,1,13,0],
     [6,15,6,15,6,15,0],[12,9,19,16,5,2,0]]
Mb = [[0,7,14,None,0],[0,14,7,0,None]]
for a,b,c,d,e in zip(*M):
    Mb.append([a,b,c,d,e])
    Mb.append([16*c%21, None if a is None else 16*a%21, 16*b%21, (16*d+7)%21, (16*e+14)%21])
    Mb.append([4*b%21, 4*c%21, None if a is None else 4*a%21, (4*d+14)%21, (4*e+7)%21])
assert len(Mb) == 23
for c in range(5): assert sum(r[c] is None for r in Mb) == 1
INF = 21
OA = []
for r in Mb:
    for g in range(21):
        OA.append([INF if x is None else (x + g) % 21 for x in r])
OA.append([INF]*5)
assert len(OA) == 484 and len({tuple(r) for r in OA}) == 484
# OA check: every pair of columns covers all 22^2 pairs
for a in range(5):
    for b in range(a+1, 5):
        assert len({(r[a], r[b]) for r in OA}) == 484, (a, b)
print("OA(5,22): 484 rows, all 10 column pairs cover Z22^2 exactly once")
sq = [[[None]*22 for _ in range(22)] for _ in range(3)]
for r in OA:
    for t in range(3):
        sq[t][r[0]][r[1]] = r[2+t]
d = {"n": 22, "squares": sq}
expect("baseline order 22", d, 3, True)
expect("baseline order 22 asked k=4", d, 4, False, "wrong number")
s = json.dumps(d, separators=(",", ":"))
open("/work/tools/mols/baseline_mols22_k3.json", "w").write(s)
print("sha256(baseline_mols22_k3.json) =", hashlib.sha256(s.encode()).hexdigest())
d2 = copy.deepcopy(d); r = d2["squares"][0][3]; r[0], r[1] = r[1], r[0]
expect("baseline swap two cells", d2, 3, False, "not Latin")
print("FAILS:", fails)
sys.exit(1 if fails else 0)
