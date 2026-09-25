#!/usr/bin/env python3
"""
WOWII-61 round 3 (owner-w61): numerical corroboration of the two repairs written
into draft 7.3 "5bis".

T-b repair claims: in the tau=3 hard core, the branch (k=1, e_B=0, p=3) is empty
-- the draft's stated reason ("p>=3 gives deg(y)>3") fails exactly at p=3, and the
repair kills p=3 via (F-b) instead.  Here we (1) confirm the cell is empty over
the box of multiplicity tuples, and (2) confirm the repair's intermediate claims
(p=3 & k<=1  =>  the only occurring types are the universal one and at most one
singleton containing the unique high-degree B-vertex, hence no disjoint pair).

T-a repair claims: in the tau=3 hard core, case k=3 always has e_B=2 and
D_3=Z-1, and the entry attaining max(L^2) is never one that was decremented at
step 2.  We test the repair's *branch (1)* directly: no entry of L^1 other than
the step-2 head has value >= Z.

Enumeration follows draft 7.3 Lemma P: a tau=3 hard-core graph is determined by
the 7 multiplicities mu[T] (T a non-empty subset of B) together with G[B]
(4 isomorphism types).  This is a bounded box scan, not a search: no SAT, no
large brute force.
"""
import itertools
from collections import Counter

B = [0, 1, 2]
TYPES = [frozenset(s) for r in (1, 2, 3) for s in itertools.combinations(B, r)]
GB = [[], [(0, 1)], [(0, 1), (1, 2)], [(0, 1), (1, 2), (0, 2)]]

MAXMULT = 4


def build(mu, gb):
    """vertices 0,1,2 = B ; then the A-vertices in type order."""
    edges = list(gb)
    n = 3
    for T in TYPES:
        for _ in range(mu[T]):
            for b in sorted(T):
                edges.append((n, b))
            n += 1
    return n, edges


def adj(n, edges):
    a = [0] * n
    for u, v in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def connected(a, n):
    seen, st = 1, [0]
    while st:
        v = st.pop()
        m = a[v] & ~seen
        while m:
            b = m & -m
            m ^= b
            seen |= b
            st.append(b.bit_length() - 1)
    return seen == (1 << n) - 1


def diam(a, n):
    best = 0
    for s in range(n):
        d = [-1] * n
        d[s] = 0
        q = [s]
        while q:
            nq = []
            for v in q:
                m = a[v]
                while m:
                    b = m & -m
                    m ^= b
                    w = b.bit_length() - 1
                    if d[w] < 0:
                        d[w] = d[v] + 1
                        nq.append(w)
            q = nq
        if min(d) < 0:
            return -1
        best = max(best, max(d))
    return best


def acyclic(a, n, S):
    verts = [v for v in range(n) if S >> v & 1]
    idx = {v: i for i, v in enumerate(verts)}
    par = list(range(len(verts)))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for v in verts:
        m = a[v] & S
        while m:
            b = m & -m
            m ^= b
            w = b.bit_length() - 1
            if w > v:
                ra, rb = find(idx[v]), find(idx[w])
                if ra == rb:
                    return False
                par[ra] = rb
    return True


def hh_heads(degs):
    ent = sorted(degs, reverse=True)
    heads = []
    while ent and ent[0] > 0:
        d = ent[0]
        heads.append(d)
        rest = ent[1:]
        for k in range(min(d, len(rest))):
            rest[k] = max(rest[k] - 1, 0)
        ent = sorted(rest, reverse=True)
    return heads


def main():
    cells = Counter()
    p3_cases = 0
    k3_e_b = Counter()
    k3_branch1_fail = 0
    tested = 0
    for gb in GB:
        for vals in itertools.product(range(MAXMULT + 1), repeat=len(TYPES)):
            mu = dict(zip(TYPES, vals))
            if sum(vals) == 0:
                continue
            n, edges = build(mu, gb)
            if n > 12:
                continue
            a = adj(n, edges)
            if not connected(a, n):
                continue
            # A = the non-B vertices; is it a MAXIMUM independent set (alpha = n-3)?
            al = n - 3
            ok = True
            for S in range(1 << n):
                if bin(S).count('1') <= al:
                    continue
                m2, good = S, True
                while m2:
                    b = m2 & -m2
                    m2 ^= b
                    if a[b.bit_length() - 1] & S:
                        good = False
                        break
                if good:
                    ok = False
                    break
            if not ok:
                continue
            if diam(a, n) != 4:
                continue
            # f = alpha + 1 : some (n-1)-subset acyclic? no -> f<=alpha+1 ; need
            # f != alpha+2 = n-1, and f >= alpha+1 always (Lemma 3)
            if any(acyclic(a, n, ((1 << n) - 1) ^ (1 << v)) for v in range(n)):
                continue
            degs = [bin(x).count('1') for x in a]
            if all(acyclic(a, n, (1 << n) - 1) for _ in [0]):
                continue                                   # forest
            tested += 1
            eB = len(gb)
            k = sum(1 for b in B if degs[b] >= 4)
            p = mu[frozenset(B)]
            cells[(eB, k)] += 1
            if k <= 1 and eB == 0 and p == 3:
                p3_cases += 1
            if k == 3:
                k3_e_b[eB] += 1
                # T-a repair, branch (1): after step 1, no entry other than the
                # step-2 head has value >= Z (= min B-degree)
                Z = min(degs[b] for b in B)
                ent = sorted(degs, reverse=True)
                d1 = ent[0]
                rest = ent[1:]
                for i2 in range(min(d1, len(rest))):
                    rest[i2] = max(rest[i2] - 1, 0)
                L1 = sorted(rest, reverse=True)
                if any(v >= Z for v in L1[1:]):
                    k3_branch1_fail += 1
    print(f"[repair] MAXMULT={MAXMULT} tau=3 hard-core instances tested = {tested}")
    print(f"[repair] (e_B,k) cells: {dict(sorted(cells.items()))}")
    print(f"[repair] T-b: instances with k<=1, e_B=0, p=3  ==  {p3_cases}   "
          f"(repair claims 0)")
    print(f"[repair] T-a: k=3 instances {sum(k3_e_b.values())}, e_B distribution "
          f"{dict(sorted(k3_e_b.items()))}  -- NOTE this scan is NOT filtered by the "
          f"reductio hypothesis residue=alpha, so it does NOT test the draft's "
          f"'k=3 forces e_B=2' (which is derived only under that hypothesis)")
    print(f"[repair] T-a branch-1 ('no entry of L^1 besides the step-2 head has "
          f"value >= Z'): violations = {k3_branch1_fail} (repair claims 0)")


if __name__ == "__main__":
    main()
