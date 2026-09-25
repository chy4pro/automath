#!/usr/bin/env python3
"""Erdős #1188 (irreducible-covering-set reading, cf. Bloom's comment 2026-04-17 and Erdős [Er80]):
G(x) = number of irreducible covering sets with all moduli in [2, x], i.e. sets S of distinct moduli that admit a
covering system (some residues cover Z) while no proper subset of S does.  Coverability is monotone, so minimality
only needs the |S| maximal proper subsets.  Enumeration: DFS over subsets of {2..x} in increasing order with the
necessary conditions sum(1/n) >= 1 and the private-prime-power filter (every p^e || n_i divides another modulus);
coverability by SAT (CaDiCaL via pysat) on Z/lcm.  Usage: python3 count_irreducible_by_max.py XMAX [SECONDS]"""
import sys, math, time
from functools import lru_cache
from pysat.solvers import Cadical153
XMAX = int(sys.argv[1]); CAP = float(sys.argv[2]) if len(sys.argv) > 2 else 1200.0
T0 = time.time()
def ppows(n):
    out = []; d = 2
    while d * d <= n:
        if n % d == 0:
            e = 1
            while n % d == 0: n //= d; e *= d
            out.append(e)
        d += 1
    if n > 1: out.append(n)
    return out
PP = {n: ppows(n) for n in range(2, XMAX + 1)}
def private_ok(mods):
    for i, n in enumerate(mods):
        for q in PP[n]:
            if not any(j != i and m % q == 0 for j, m in enumerate(mods)): return False
    return True
@lru_cache(maxsize=None)
def can_cover(mods):
    L = 1
    for n in mods: L = L * n // math.gcd(L, n)
    var = lambda i, a: 1 + sum(mods[:i]) + a
    s = Cadical153()
    for i, n in enumerate(mods):
        s.add_clause([var(i, a) for a in range(n)])
        for a in range(n):
            for b in range(a + 1, n): s.add_clause([-var(i, a), -var(i, b)])
    s.add_clause([var(0, 0)])
    for t in range(L): s.add_clause([var(i, t % n) for i, n in enumerate(mods)])
    r = s.solve(); s.delete(); return r
def irreducible(mods):
    if not private_ok(mods) or not can_cover(mods): return False
    for i in range(len(mods)):
        sub = mods[:i] + mods[i + 1:]
        if len(sub) >= 2 and can_cover(sub): return False   # coverability only (private_ok is NOT necessary for coverability)
    return True
found = {}   # x -> list of sets whose max modulus is exactly x
count = 0
def dfs(prefix, start, harmonic):
    global count
    if time.time() - T0 > CAP: raise TimeoutError
    if len(prefix) >= 2 and harmonic >= 1 - 1e-12:
        if irreducible(tuple(prefix)):
            found.setdefault(prefix[-1], []).append(tuple(prefix)); count += 1
            return   # supersets of an irreducible covering set are never irreducible
    rem = sum(1.0 / n for n in range(start, XMAX + 1))
    if harmonic + rem < 1 - 1e-12: return
    for n in range(start, XMAX + 1):
        dfs(prefix + [n], n + 1, harmonic + 1.0 / n)
try:
    dfs([], 2, 0.0); done = True
except TimeoutError:
    done = False
print("complete:" if done else "INCOMPLETE (time cap):", f"{time.time()-T0:.0f}s, XMAX={XMAX}")
cum = 0
for x in range(2, XMAX + 1):
    cum += len(found.get(x, []))
    print(f"x={x}: sets with max modulus exactly x: {len(found.get(x, []))}; G(x) (all moduli <= x): {cum}")
for x in sorted(found):
    for s in found[x]: print("  ", s)
