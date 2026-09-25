#!/usr/bin/env python3
"""
WOWII-61: the Qwen tau=3 "Family I / Family II" generalised to arbitrary tau,
and the check that the new Theorem N settles them uniformly.

Family I(tau,c):  B = {b_1..b_tau} independent;  A = U (c vertices adjacent to
                  every b_i) + one leaf on b_1 + one leaf on b_2.
Family II(tau,c): same but with the single edge b_1 b_2 inside B, leaves on
                  b_1 and b_3 (so that diam is still 4).

For each we verify by direct computation: connected, non-forest, diam = 4,
alpha = n - tau, f = alpha + 1 (hard core!), then residue vs alpha, and
whether Theorem N's hypothesis (all B-degrees >= max(tau+1, 2 e_B + 3),
e_B <= tau-2) applies.
"""
import itertools, sys
sys.path.insert(0, "$HOME/workspace/claudecode/automath/problems/wowii")
from w61_lemH import adj_masks, is_connected, alpha_and_covers, hh_labelled


def diameter(a, n):
    best = 0
    for s in range(n):
        dist = [-1] * n
        dist[s] = 0
        q = [s]
        while q:
            nq = []
            for v in q:
                m = a[v]
                while m:
                    b = m & -m
                    m ^= b
                    w = b.bit_length() - 1
                    if dist[w] < 0:
                        dist[w] = dist[v] + 1
                        nq.append(w)
            q = nq
        if min(dist) < 0:
            return None
        best = max(best, max(dist))
    return best


def has_cycle(a, n, mask):
    """does the induced subgraph on `mask` contain a cycle?"""
    verts = [v for v in range(n) if mask >> v & 1]
    seen = 0
    for v in verts:
        if seen >> v & 1:
            continue
        stack = [(v, -1)]
        seen |= 1 << v
        cnt, edges = 0, 0
        comp = []
        while stack:
            x, par = stack.pop()
            comp.append(x)
            m = a[x] & mask
            while m:
                b = m & -m
                m ^= b
                w = b.bit_length() - 1
                edges += 1
                if not (seen >> w & 1):
                    seen |= 1 << w
                    stack.append((w, x))
        if edges // 2 > len(comp) - 1:
            return True
    return False


def f_is_alpha_plus_1(a, n, al):
    """f(G) = alpha+1  <=>  no induced forest on alpha+2 vertices."""
    full = (1 << n) - 1
    for S in itertools.combinations(range(n), al + 2):
        mask = 0
        for v in S:
            mask |= 1 << v
        if not has_cycle(a, n, mask):
            return False
    return True


def build_I(tau, c):
    # 0..tau-1 = B ; tau..tau+c-1 = U ; tau+c, tau+c+1 = leaves on b0, b1
    n = tau + c + 2
    e = [(b, tau + i) for b in range(tau) for i in range(c)]
    e += [(0, tau + c), (1, tau + c + 1)]
    return n, e


def build_II(tau, c):
    if tau < 3:
        return None
    n = tau + c + 2
    e = [(b, tau + i) for b in range(tau) for i in range(c)]
    e += [(0, 1)]                      # the single edge inside B
    e += [(0, tau + c), (2, tau + c + 1)]
    return n, e


def report(name, builder, taus, cs):
    print(f"=== {name} ===")
    print("tau   c    n   m  alpha  residue  hardcore  ThmN-applies")
    bad = 0
    for tau in taus:
        for c in cs:
            r = builder(tau, c)
            if r is None:
                continue
            n, edges = r
            a = adj_masks(n, edges)
            if not is_connected(a, n):
                continue
            degs = [bin(x).count('1') for x in a]
            al, isets = alpha_and_covers(a, n)
            if n - al != tau:
                continue
            heads, _, _ = hh_labelled(degs)
            res = n - len(heads)
            m = sum(degs) // 2
            hard = (m >= n) and (diameter(a, n) == 4) and f_is_alpha_plus_1(a, n, al)
            B = list(range(tau))
            eB = sum(1 for u, v in edges if u < tau and v < tau)
            thmN = (eB <= tau - 2) and min(degs[b] for b in B) >= max(tau + 1, 2 * eB + 3)
            if hard:
                flag = "HARD-CORE" if hard else ""
                print(f"{tau:3d} {c:3d} {n:4d} {m:3d} {al:5d} {res:8d}  {flag:9s} {thmN}")
                if res >= al:
                    print("   *** COUNTEREXAMPLE ***")
                    bad += 1
    print(f"  violations: {bad}")


if __name__ == "__main__":
    report("Family I  (B independent, 2 private leaves)", build_I,
           range(3, 8), range(2, 11))
    report("Family II (one edge inside B, 2 private leaves)", build_II,
           range(3, 8), range(2, 11))
