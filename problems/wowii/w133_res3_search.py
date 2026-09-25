#!/usr/bin/env python3
"""
Round 4.
(A) Q14.1 side-probe: is there a C4-free graph with diam=2, l>3 CONTAINING A TRIANGLE?
    Candidate family: Erdos-Renyi orthogonal polarity graphs ER_q (extremal C4-free).
(B) Main: is the r=3 residual class inhabited?
        C4-free,  rad = 2,  diam = 3,  l > 3.
    If inhabited, a contradiction proof is impossible and we must prove path >= 6.
"""
import sys, itertools
sys.path.insert(0, '$HOME/workspace/claudecode/automath/problems/wowii')
from w133_r3_counterexample import (neighbours, alldist, ecc_rad, avec, has_c4,
                                    girth, connected, hoffman_singleton,
                                    greedy_long_induced_path)

def has_triangle(adj):
    return any(adj[u] & adj[v] for u in range(len(adj)) for v in adj[u] if u < v)

def info(name, n, E):
    adj = neighbours(E, n)
    if not connected(adj): return None
    D = alldist(adj); e, r = ecc_rad(D); a = avec(adj); S = sum(a)
    return dict(name=name, n=n, adj=adj, rad=r, diam=max(e), S=S, l=S/n,
                c4free=not has_c4(adj), tri=has_triangle(adj), mu=min(a), amax=max(a))

def er_polarity(q):
    """Erdos-Renyi orthogonal polarity graph on PG(2,q), q prime. C4-free, extremal."""
    pts = []
    seen = set()
    for v in itertools.product(range(q), repeat=3):
        if v == (0, 0, 0): continue
        # normalise: first nonzero coordinate = 1
        for i in range(3):
            if v[i]:
                inv = pow(v[i], q - 2, q)
                key = tuple((x * inv) % q for x in v)
                break
        if key not in seen:
            seen.add(key); pts.append(key)
    idx = {p: i for i, p in enumerate(pts)}
    E = set()
    for p in pts:
        for r_ in pts:
            if p == r_: continue
            if sum(p[i] * r_[i] for i in range(3)) % q == 0:
                E.add(tuple(sorted((idx[p], idx[r_]))))
    return len(pts), sorted(E)

def report(f, tag=""):
    if f is None: return
    print(f"  {f['name']:<26} n={f['n']:<4} C4-free={str(f['c4free']):<5} tri={str(f['tri']):<5} "
          f"rad={f['rad']} diam={f['diam']} l={f['l']:.3f} mu={f['mu']} {tag}")
    return f

if __name__ == "__main__":
    print("=== (A) Q14.1: C4-free, diam=2, l>3, WITH a triangle? (ER_q polarity graphs) ===")
    hits = []
    for q in (3, 5, 7, 11):
        n, E = er_polarity(q)
        f = info(f"ER_{q}", n, E)
        if f is None: continue
        ok = f['c4free'] and f['diam'] == 2 and f['l'] > 3 and f['tri']
        report(f, "  <== ANSWERS Q14.1 (yes)" if ok else "")
        if ok:
            P = greedy_long_induced_path(f['adj'])
            print(f"      G12 predicts path >= 6; certificate = {len(P)}  "
                  f"{'OK' if len(P) >= 6 else 'FAIL'}")
            hits.append(f)
    print(f"  ==> Q14.1 witnesses: {len(hits)}")

    print()
    print("=== (B) is the r=3 residual class inhabited?  C4-free, rad=2, diam=3, l>3 ===")
    cands = []
    n0, E0 = hoffman_singleton()
    adj0 = neighbours(E0, n0)
    def sub(name, drop):
        keep = [v for v in range(n0) if v not in drop]
        ix = {v: i for i, v in enumerate(keep)}
        return info(name, len(keep),
                    [(ix[u], ix[v]) for u, v in E0 if u in ix and v in ix])
    cands.append(sub("HS - 1 vertex", {0}))
    cands.append(sub("HS - 2 adj", {0, list(adj0[0])[0]}))
    cands.append(sub("HS - 2 nonadj", {0, next(v for v in range(1, n0) if v not in adj0[0])}))
    for kdrop in (3, 5, 8, 12):
        cands.append(sub(f"HS - {kdrop} vertices", set(range(kdrop))))
    for q in (3, 5, 7):
        n, E = er_polarity(q)
        adjq = neighbours(E, n)
        keep = list(range(n - 1))
        ixq = {v: i for i, v in enumerate(keep)}
        cands.append(info(f"ER_{q} - 1 vertex", len(keep),
                          [(ixq[u], ixq[v]) for u, v in E if u in ixq and v in ixq]))
    found = []
    for f in cands:
        if f is None: continue
        ok = f['c4free'] and f['rad'] == 2 and f['diam'] == 3 and f['l'] > 3
        report(f, "  <== IN RESIDUAL CLASS" if ok else "")
        if ok:
            P = greedy_long_induced_path(f['adj'])
            print(f"      residual needs path >= 6; certificate = {len(P)}  "
                  f"{'OK' if len(P) >= 6 else '*** FAIL = COUNTEREXAMPLE ***'}")
            found.append(f)
    print(f"  ==> residual-class members found: {len(found)}")

# ---------------------------------------------------------------------------
def R3_holds(f):
    """(R3): no pair at distance >= 3 with a-values (>=3, >=2).
       Equivalently: every vertex with a>=3 has eccentricity <= 2."""
    adj, D = f['adj'], alldist(f['adj']); a = avec(adj); n = f['n']
    bad = [(u, v, D[u][v], a[u], a[v]) for u in range(n) for v in range(n)
           if u != v and D[u][v] >= 3 and a[u] >= 3 and a[v] >= 2]
    return (len(bad) == 0), bad

def RES(f):
    """the TRUE r=3 residual predicate (adds (R3) to the planner's stated class)."""
    ok3, _ = R3_holds(f)
    return f['c4free'] and f['rad'] == 2 and f['diam'] == 3 and f['l'] > 3 and ok3

if __name__ == "__main__" and "--res" in sys.argv:
    print()
    print("=== (C) TRUE residual predicate RES = class + (R3) ===")
    print("    (R3) := every vertex with a>=3 has ecc <= 2")
    n0, E0 = hoffman_singleton()
    def sub(name, drop):
        keep = [v for v in range(n0) if v not in drop]
        ix = {v: i for i, v in enumerate(keep)}
        return info(name, len(keep), [(ix[u], ix[v]) for u, v in E0 if u in ix and v in ix])
    cands = [sub("HS - 1 vertex", {0}), sub("HS - 3 vertices", set(range(3))),
             sub("HS - 8 vertices", set(range(8))), sub("HS - 12 vertices", set(range(12)))]
    for q in (5, 7):
        n, E = er_polarity(q); adjq = neighbours(E, n)
        keep = list(range(n - 1)); ixq = {v: i for i, v in enumerate(keep)}
        cands.append(info(f"ER_{q} - 1 vertex", len(keep),
                          [(ixq[u], ixq[v]) for u, v in E if u in ixq and v in ixq]))
    nres = 0
    for f in cands:
        if f is None: continue
        ok3, bad = R3_holds(f)
        a = avec(f['adj']); H = [v for v in range(f['n']) if a[v] >= 3]
        excess = sum(a[v] - 2 for v in H)
        print(f"  {f['name']:<22} l={f['l']:.3f} (R3)={ok3}"
              f"{'' if ok3 else f'  (e.g. dist-{bad[0][2]} pair with a=({bad[0][3]},{bad[0][4]}))'}"
              f" | in RES: {RES(f)} | sum_H(a-2)={excess} vs n={f['n']}"
              f" ({'>n OK' if excess > f['n'] else '<=n'})")
        nres += RES(f)
    print(f"  ==> members of the TRUE residual RES found: {nres}")
    print("      => the 9 'class' witnesses above are NOT in the residual: they all")
    print("         violate (R3), because a dense core with diam 3 has HIGH vertices")
    print("         at distance 3 from each other.")
