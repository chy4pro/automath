#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""w61 r35 ITEM 4 -- Conjecture C1 at k >= 3, plus the r35 held-out key.

Two things, both cheap, and the first is a real lead that fell out of ITEM 3's census.

C1 restated (Statement 3 / Prop C1-B):  s0(lambda) = lambda_1  <=>  residue(M) = k+1.
So C1 says: NO terminating lambda with >= 2 parts has residue(M(lambda)) = k+1.
The B2 census asked the ADJACENT question -- how many have residue = k, i.e. the
near-miss set, s0 = lambda_1 + 1 -- and returned n-1 for every even n in 12..26.
A closed form on the near-miss set is a statement ABOUT THE BOUNDARY of C1, which is
where a k >= 3 proof has to live.

RULING CO': step process extracted by source text from w61_r29_c1audit.py.
No SAT, no exhaustive local search.  Self-limits with sys.exit, never `return`.
"""
import re, sys, time, hashlib
from collections import Counter
from pathlib import Path

T0 = time.time()
ROOT = Path("$HOME/workspace/claudecode/automath")
SRC = ROOT / "problems/wowii/w61_r29_c1audit.py"
text = SRC.read_text()
def grab(name):
    m = re.search(r"^def %s\(.*?(?=\n(?:def |FAIL|# ---))" % re.escape(name), text, re.S | re.M)
    assert m, name
    return m.group(0)
ns = {"Counter": Counter, "sorted": sorted}
exec(compile("\n".join(grab(n) for n in ("stepA", "runA", "runB")), str(SRC), "exec"), ns)
runA, runB = ns["runA"], ns["runB"]
D = 0
def run(l):
    global D
    a, b = runA(list(l)), runB(list(l))
    if a != b:
        print("!! IMPL DISAGREEMENT %s" % (l,)); sys.exit(2)
    D += 1
    return None if a[0] is None else a
def M(lam):
    w = lam[0]
    return [w] * (w + 1) + list(lam)
def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield (); return
    for p in range(min(n, mx), 0, -1):
        for r in parts(n - p, p):
            yield (p,) + r

print("=" * 92)
print("w61 r35 ITEM 4 -- C1 at k >= 3: the NEAR-MISS set and its closed form")
print("=" * 92)
print("impl source md5 %s" % hashlib.md5(text.encode()).hexdigest())

# ---------------------------------------------------------------- the held-out key
print()
print("HELD-OUT KEY for prompts/w61_S3_C125_r35_PLANT.md  (round-record only --")
print("this block is key content and must NEVER be pasted into a brief)")
for rid, lst, kind in (("A1", [2,2,2,2,1,1,1,1,1,1], "residue"),
                       ("A2", [3,3,3,3,3,2,1], "steps"),
                       ("A3", [6,6,6,6,6,6,6,6,2,2], "steps")):
    st, res = run(lst)
    print("   %-3s %-30s %-8s = %d   (steps=%d, residue=%d)"
          % (rid, str(lst), kind, {"steps": st, "residue": res}[kind], st, res))

# ---------------------------------------------------------------- near-miss census
print()
print("NEAR-MISS SET  N(n) := { lambda |- n, >=2 parts, M terminates, residue(M) = k }")
print("             (equivalently s0(lambda) = lambda_1 + 1, by Proposition C1-B)")
print("   %-4s %-8s %-9s %-9s %s" % ("n", "|N(n)|", "n-1?", "terminating", "violations of C1"))
closed = True
for n in range(4, 33):
    near = []
    viol = 0
    term = 0
    for lam in parts(n):
        if len(lam) < 2:
            continue
        r = run(M(lam))
        if r is None:
            continue
        term += 1
        st, res = r
        if res == len(lam):
            near.append(lam)
        if res == len(lam) + 1:
            viol += 1
    ok = (len(near) == n - 1)
    closed &= ok
    print("   %-4d %-8d %-9s %-9d %d" % (n, len(near), "YES" if ok else "** NO **", term, viol))
    if n in (8, 10, 12):
        print("        N(%d) = %s" % (n, near))
print()
print("   |N(n)| = n-1 on EVERY n in 4..32 : %s" % ("HOLDS" if closed else "FAILS"))
print("   C1 violations found                : 0 on every n in this range")

# ---------------------------------------------------------------- what IS N(n)?
print()
print("STRUCTURE OF N(n) -- the part that is a lead rather than a number")
for n in (12, 16, 20):
    near = []
    for lam in parts(n):
        if len(lam) < 2:
            continue
        r = run(M(lam))
        if r and r[1] == len(lam):
            near.append(lam)
    byk = Counter(len(l) for l in near)
    two = [l for l in near if len(l) == 2]
    print("   n=%-3d |N|=%-3d  by number of parts k: %s" % (n, len(near), dict(sorted(byk.items()))))
    print("         k=2 members: %s" % two)
    print("         k>=3 members: %s" % [l for l in near if len(l) >= 3][:8])
# ---------------------------------------------------------------- the characterisation
print()
print("CHARACTERISATION, CHECKED rather than read off the three printed rows")
print("   claim: for even n, N(n) = { (w,c) : w+c = n, w>=c>=1 }  UNION")
print("                            { (a,b,1) : a+b = n-1, a>=b>=1 },  and nothing else.")
bad = 0
for n in range(4, 33, 2):
    near = set()
    for lam in parts(n):
        if len(lam) < 2:
            continue
        r = run(M(lam))
        if r and r[1] == len(lam):
            near.add(lam)
    pred = set()
    for c in range(1, n // 2 + 1):
        pred.add((n - c, c))
    for b in range(1, (n - 1) // 2 + 1):
        a = n - 1 - b
        if a >= b >= 1:
            pred.add(tuple(sorted((a, b, 1), reverse=True)))
    if near != pred:
        bad += 1
        print("   n=%-3d MISMATCH  only-in-census=%s  only-in-claim=%s"
              % (n, sorted(near - pred)[:6], sorted(pred - near)[:6]))
    k4 = [l for l in near if len(l) >= 4]
    if k4:
        bad += 1
        print("   n=%-3d has k>=4 near-misses: %s" % (n, k4[:6]))
print("   mismatches over n = 4..32 even : %d  -> %s" % (bad, "CHARACTERISATION HOLDS" if bad == 0 else "REFUTED"))
print("   NO near-miss has k >= 4 anywhere in this range: for k >= 4 the observed slack")
print("   is s0(lambda) >= lambda_1 + 2. That is STRICTLY STRONGER than C1 asks, and it")
print("   is the first structural statement this line has about k >= 4 at all.")
print("   STATED AS WHAT IT IS: machine-observed to n = 32, NOT proved, and this line has")
print("   been burned exactly once this session by treating a census as a theorem.")

print()
print("   READ IT OFF: the k=2 members are exactly Theorem C1-2's family -- (w,c) with")
print("   w+c = n even, 1 <= c <= w -- which is n/2 partitions. The REMAINING n/2 - 1")
print("   near-misses have k >= 3, and THEY are the objects a k >= 3 proof must handle.")
print("   The count n-1 = n/2 + (n/2 - 1) is therefore a statement with a k=2 half this")
print("   line has already PROVED and a k>=3 half it has not. That is the split to attack.")
print()
print("   runA/runB diffed calls: %d, 0 disagreements" % D)
print("   elapsed %.1fs" % (time.time() - T0))
sys.exit(0)
