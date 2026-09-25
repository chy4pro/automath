#!/usr/bin/env python3
"""
Independent verification of the generating pairs in the Fernandes 2-generation proof.

Conventions: permutations act on {1,...,r}; composition is right-to-left,
(p*q)(x) = p(q(x)).  A permutation of degree r is stored as a tuple
(p(1),...,p(r)).  Pure Python, no third-party dependencies.
"""
import itertools, time
from array import array
from math import factorial
from collections import Counter


# ---------- basic permutation machinery ----------------------------------
def ident(r):
    return tuple(range(1, r + 1))


def mul(p, q):
    """right-to-left: (p*q)(x) = p(q(x))"""
    return tuple(p[x - 1] for x in q)


def inv(p):
    r = len(p)
    out = [0] * r
    for x in range(1, r + 1):
        out[p[x - 1] - 1] = x
    return tuple(out)


def from_cycle(cyc, r):
    p = list(range(1, r + 1))
    for i, x in enumerate(cyc):
        p[x - 1] = cyc[(i + 1) % len(cyc)]
    return tuple(p)


def cycles(p):
    r = len(p)
    seen = [False] * (r + 1)
    out = []
    for s in range(1, r + 1):
        if seen[s]:
            continue
        c, x = [], s
        while not seen[x]:
            seen[x] = True
            c.append(x)
            x = p[x - 1]
        if len(c) > 1:
            out.append(tuple(c))
    return out


def sign(p):
    s = 1
    for c in cycles(p):
        if len(c) % 2 == 0:
            s = -s
    return s


def order(p):
    e, q, k = ident(len(p)), p, 1
    while q != e:
        q = mul(q, p)
        k += 1
    return k


# ---------- the generators of the paper ----------------------------------
def a(r):
    return from_cycle(list(range(1, r + 1)), r) if r % 2 else from_cycle(list(range(1, r)), r)


def b(r):
    return from_cycle([1, 2], r) if r % 2 else from_cycle([r - 1, r], r)


def d(r):
    return mul(b(r), a(r))                        # d_r = b_r a_r


def d_claimed(r):
    if r % 2:
        return from_cycle(list(range(2, r + 1)), r)           # (2 3 ... r)
    return from_cycle(list(range(1, r - 1)) + [r, r - 1], r)  # (1 2 ... r-2 r r-1)


# ---------- indexed symmetric groups -------------------------------------
_cache = {}


def sym(r):
    if r not in _cache:
        perms = sorted(itertools.permutations(range(1, r + 1)))
        idx = {p: i for i, p in enumerate(perms)}
        _cache[r] = (perms, idx)
    return _cache[r]


def leftmul_map(r, g):
    """array L with L[i] = index of g * perms[i]"""
    perms, idx = sym(r)
    return array('i', [idx[mul(g, p)] for p in perms])


def closure_pair(m, n, gens):
    """BFS closure of <gens> inside S_m x S_n."""
    _, im = sym(m)
    _, inn = sym(n)
    Nn = factorial(n)
    maps = [(leftmul_map(m, g1), leftmul_map(n, g2)) for (g1, g2) in gens]
    start = im[ident(m)] * Nn + inn[ident(n)]
    visited = bytearray(factorial(m) * Nn)
    visited[start] = 1
    frontier = array('l', [start])
    total = 1
    while frontier:
        nxt = array('l')
        ap = nxt.append
        for s in frontier:
            i, j = divmod(s, Nn)
            for Lm, Ln in maps:
                t = Lm[i] * Nn + Ln[j]
                if not visited[t]:
                    visited[t] = 1
                    ap(t)
                    total += 1
        frontier = nxt
    return total


def gamma_size(m, n):
    return factorial(m) * factorial(n) // 2


# =========================================================================
print("=" * 78)
print("PART A.  cycle form, parity and order of a_r, b_r, d_r  (2 <= r <= 12)")
print("=" * 78)
ok = True
for r in range(2, 13):
    ar, br, dr = a(r), b(r), d(r)
    dc = d_claimed(r) if r >= 3 else None
    c_ok = (dr == dc) if r >= 3 else "n/a"
    exp_ord = (r - 1) if r % 2 else r
    print(f"r={r:2d} | sgn a={sign(ar):+d} sgn b={sign(br):+d} sgn d={sign(dr):+d} | "
          f"|b|={order(br)} |d|={order(dr)} (claimed {exp_ord}) | "
          f"d = {cycles(dr)} | closed form OK: {c_ok}")
    ok &= sign(ar) == 1 and sign(br) == -1 and sign(dr) == -1
    ok &= order(br) == 2 and order(dr) == exp_ord
    if r >= 3:
        ok &= dr == dc
    ok &= mul(dr, inv(ar)) == br          # b_r = d_r a_r^{-1}
print("PART A: all assertions hold:", ok)

print()
print("=" * 78)
print("PART B.  <a_r, b_r> = S_r  and  <a_r, d_r> = S_r  (2 <= r <= 8)")
print("=" * 78)
for r in range(2, 9):
    row = []
    for name, gens in (("a,b", [a(r), b(r)]), ("a,d", [a(r), d(r)])):
        seen = {ident(r)}
        frontier = [ident(r)]
        while frontier:
            nxt = []
            for p in frontier:
                for g in gens:
                    q = mul(g, p)
                    if q not in seen:
                        seen.add(q)
                        nxt.append(q)
            frontier = nxt
        assert len(seen) == factorial(r), (r, name, len(seen))
        row.append(f"|<{name}>|={len(seen)}")
    print(f"  r={r:2d}  " + "  ".join(row) + f"   = {r}! = {factorial(r)}  OK")

print()
print("=" * 78)
print("PART C.  closure of the paper's generating pairs (14 cases)")
print("=" * 78)
unequal = [(3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (6, 4),
           (6, 5), (7, 3), (7, 6)]
equal = [(5, 5), (6, 6), (7, 7)]
allok = True
for (m, n) in unequal:
    gens = [(a(m), a(n)), (b(m), b(n))]
    for g in gens:
        assert sign(g[0]) == sign(g[1])
    t0 = time.time()
    sz = closure_pair(m, n, gens)
    tgt = gamma_size(m, n)
    allok &= sz == tgt
    print(f"  ({m},{n})  unequal recipe  |<S>| = {sz:>10,}   |Gamma| = {tgt:>10,}   "
          f"{'EQUAL' if sz == tgt else 'FAIL'}   [{time.time()-t0:.1f}s]")
for (m, n) in equal:
    r = m
    gens = [(a(r), a(r)), (b(r), d(r))]
    for g in gens:
        assert sign(g[0]) == sign(g[1])
    t0 = time.time()
    sz = closure_pair(m, n, gens)
    tgt = gamma_size(m, n)
    allok &= sz == tgt
    print(f"  ({m},{n})  equal   recipe  |<S>| = {sz:>10,}   |Gamma| = {tgt:>10,}   "
          f"{'EQUAL' if sz == tgt else 'FAIL'}   [{time.time()-t0:.1f}s]")
print("PART C: all 14 closures equal Gamma:", allok)

print()
print("=" * 78)
print("PART D.  the recipes provably FAIL on the excluded pairs")
print("=" * 78)
for (m, n, kind) in [(4, 3, "unequal"), (3, 3, "equal"), (4, 4, "equal")]:
    gens = ([(a(m), a(n)), (b(m), b(n))] if kind == "unequal"
            else [(a(m), a(m)), (b(m), d(m))])
    sz = closure_pair(m, n, gens)
    tgt = gamma_size(m, n)
    idx = tgt // sz if tgt % sz == 0 else "?"
    print(f"  ({m},{n})  {kind:7s} recipe  |<S>| = {sz:>6,}  |Gamma| = {tgt:>6,}  "
          f"index {idx}   {'PROPER (fails, as expected)' if sz < tgt else 'GENERATES'}")

print()
print("=" * 78)
print("PART E.  exact ranks of the four exceptional groups (exhaustive sweep)")
print("=" * 78)


def gamma_elements(m, n):
    pm, _ = sym(m)
    pn, _ = sym(n)
    return [(p, q) for p in pm for q in pn if sign(p) == sign(q)]


for (m, n) in [(2, 2), (3, 3), (4, 3), (4, 4)]:
    G = gamma_elements(m, n)
    N = len(G)
    assert N == gamma_size(m, n)
    gi = {g: i for i, g in enumerate(G)}
    T = [[gi[(mul(p[0], q[0]), mul(p[1], q[1]))] for q in G] for p in G]
    e = gi[(ident(m), ident(n))]

    def gen_count(gens):
        seen = bytearray(N)
        seen[e] = 1
        fr = [e]
        c = 1
        while fr:
            nx = []
            for s in fr:
                for g in gens:
                    t = T[g][s]
                    if not seen[t]:
                        seen[t] = 1
                        nx.append(t)
                        c += 1
            fr = nx
        return c

    t0 = time.time()
    r1 = any(gen_count([i]) == N for i in range(N))
    if r1:
        print(f"  Gamma_{{{m},{n}}}: order {N:4d}  ->  cyclic, rank 1")
        continue
    found = None
    for i in range(N):
        for j in range(i, N):
            if gen_count([i, j]) == N:
                found = (i, j)
                break
        if found:
            break
    verdict = "2" if found else ">= 3  (matches the literature value 3)"
    print(f"  Gamma_{{{m},{n}}}: order {N:4d}  cyclic: False  2-generated: "
          f"{found is not None}  ->  rank {verdict}   [{time.time()-t0:.1f}s]")

print()
print("=" * 78)
print("PART F.  structural checks used in the write-up")
print("=" * 78)
G32 = gamma_elements(3, 2)
print(f"  |Gamma_{{3,2}}| = {len(G32)}; first projection injective: "
      f"{len({g[0] for g in G32}) == len(G32)}  =>  Gamma_{{3,2}} = S_3 (nonabelian)")
p4, _ = sym(4)
cc = Counter(tuple(sorted(len(c) for c in cycles(p))) for p in p4)
print("  S_4 conjugacy-class sizes by cycle type:",
      {("id" if k == () else k): v for k, v in sorted(cc.items())})
parts = [frozenset([frozenset([1, 2]), frozenset([3, 4])]),
         frozenset([frozenset([1, 3]), frozenset([2, 4])]),
         frozenset([frozenset([1, 4]), frozenset([2, 3])])]
img, ker = set(), []
for p in p4:
    perm = tuple(parts.index(frozenset(frozenset(p[x - 1] for x in S) for S in P))
                 for P in parts)
    img.add(perm)
    if perm == (0, 1, 2):
        ker.append(p)
print(f"  S_4 -> Sym(3 pair-partitions): image order {len(img)}, kernel order {len(ker)} "
      f"= {[cycles(p) for p in ker]}")
img1 = {tuple(v + 1 for v in perm) for perm in img}
print(f"  image is nonabelian: "
      f"{any(mul(x, y) != mul(y, x) for x in img1 for y in img1)}")
for r in range(3, 7):
    pr, _ = sym(r)
    A = [p for p in pr if sign(p) == 1]
    C = [p for p in pr if all(mul(p, x) == mul(x, p) for x in A)]
    print(f"  centralizer of A_{r} in S_{r}: order {len(C)}   {[cycles(p) for p in C]}")
print()
print("ALL PARTS DONE.")
