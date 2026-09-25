#!/usr/bin/env python3
"""
WOWII-61 residual hard core, tau = 3: COMPLETE parametric exploration.

Residual hard core (draft sec.7.1): connected, non-forest, diam = 4,
f = alpha + 1, residue = alpha, tau = n - alpha >= 3.

For tau = 3 the hard core is a FINITE-PARAMETER family, not a search space:
let A be a maximum independent set, B = V \ A = {x,y,z}.  Every a in A has
a nonempty neighbourhood N(a) subseteq B, so G is determined up to
isomorphism by
    mu[T] = #{a in A : N(a) = T}   for the 7 nonempty T subseteq {x,y,z}
together with the graph G[B] (4 isomorphism types: 0,1,2,3 edges).
Hence enumerating mu over a box is an EXHAUSTIVE cover of every tau = 3
hard-core graph whose type multiplicities are inside the box -- no
isomorphism rejection, no SAT, no exponential search.

All predicates are evaluated in closed form on (mu, E_B):

  deg_A(b)      = sum of mu[T] over T containing b
  codeg(u,v)    = sum of mu[T] over T containing both u and v
  m             = sum |T| mu[T] + e_B,      n = 3 + sum mu[T]
  alpha = n-3   <=>  |N_A(S)| >= |S| for every E_B-independent S subseteq B
  f = alpha+1   <=>  G-v has a cycle for every vertex v
  diam          = diameter of the "type quotient" graph (multiplicities do
                  not change distances; two A-vertices of one type are at
                  distance 2)

Usage:  python3 w61_tau3.py [MAXMULT]      (default 5)
"""
import sys
from itertools import product, combinations

TYPES = [(0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]
EB_PATTERNS = [                      # G[B] up to isomorphism
    ("e_B=0", []),
    ("e_B=1", [(0, 1)]),
    ("e_B=2", [(0, 1), (1, 2)]),
    ("e_B=3", [(0, 1), (1, 2), (0, 2)]),
]


# --------------------------------------------------------------- Havel-Hakimi
def hh_trace(degs):
    """returns (heads D_1..D_s, residue).  Mirrors Lean residueAux exactly."""
    s = sorted(degs, reverse=True)
    heads = []
    while True:
        if not s:
            return heads, 0
        if s[0] == 0:
            return heads, len(s)
        d = s[0]
        rest = s[1:]
        s = sorted([max(x - 1, 0) for x in rest[:d]] + rest[d:], reverse=True)
        heads.append(d)


# --------------------------------------------------------------- small unions
class DSU:
    def __init__(self, k):
        self.p = list(range(k))

    def find(self, a):
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb
            return True
        return False


def comps_and_forest(mu, eb):
    """(#components, is_forest) of the graph given by multiplicities mu."""
    present = [i for i, t in enumerate(TYPES) if mu[i] > 0]
    # vertices: 0,1,2 = B ; then for each present type, mu[i] copies
    nv = 3 + sum(mu)
    dsu = DSU(nv)
    m = len(eb)
    for (u, v) in eb:
        dsu.union(u, v)
    idx = 3
    for i in present:
        for _ in range(mu[i]):
            for b in TYPES[i]:
                dsu.union(idx, b)
                m += 1
            idx += 1
    c = len({dsu.find(v) for v in range(nv)})
    return c, (m == nv - c)


def quotient_diam(mu, eb):
    """diameter of G (multiplicities do not affect distances beyond 2)."""
    present = [i for i, t in enumerate(TYPES) if mu[i] > 0]
    nodes = [0, 1, 2] + [3 + k for k in range(len(present))]
    adj = {v: set() for v in nodes}
    for (u, v) in eb:
        adj[u].add(v)
        adj[v].add(u)
    for k, i in enumerate(present):
        for b in TYPES[i]:
            adj[3 + k].add(b)
            adj[b].add(3 + k)
    best = 0
    for s in nodes:
        dist = {s: 0}
        q = [s]
        while q:
            nq = []
            for v in q:
                for w in adj[v]:
                    if w not in dist:
                        dist[w] = dist[v] + 1
                        nq.append(w)
            q = nq
        if len(dist) != len(nodes):
            return None                      # disconnected
        best = max(best, max(dist.values()))
    if any(mu[i] >= 2 for i in present):
        best = max(best, 2)
    return best


# --------------------------------------------------------------- the analysis
def analyse(mu, eb):
    """returns None if (mu,E_B) is not in the tau=3 hard-core-minus-residue,
       else a dict of invariants."""
    al = sum(mu)
    if al == 0:
        return None
    n = 3 + al
    degA = [0, 0, 0]
    for i, t in enumerate(TYPES):
        for b in t:
            degA[b] += mu[i]
    if min(degA) == 0:                       # A maximal: every b has an A-nbr
        return None
    degB = [0, 0, 0]
    for (u, v) in eb:
        degB[u] += 1
        degB[v] += 1
    m = sum(len(TYPES[i]) * mu[i] for i in range(7)) + len(eb)
    if m < n:                                # forest / disconnected
        return None
    c, isforest = comps_and_forest(mu, eb)
    if c != 1 or isforest:
        return None
    # alpha = n - 3 ?
    ebset = {frozenset(e) for e in eb}
    for k in range(1, 4):
        for S in combinations(range(3), k):
            if any(frozenset(pr) in ebset for pr in combinations(S, 2)):
                continue                     # S not independent
            NA = sum(mu[i] for i, t in enumerate(TYPES) if set(t) & set(S))
            if NA < k:
                return None                  # alpha > n-3
    # diam = 4 ?
    if quotient_diam(mu, eb) != 4:
        return None
    # f = alpha + 1 ?  <=>  G - v has a cycle for every v
    def codeg(u, v):
        return sum(mu[i] for i, t in enumerate(TYPES) if u in t and v in t)
    for b in range(3):
        u, w = [t for t in range(3) if t != b]
        cyc = (codeg(u, w) >= 2) or (frozenset((u, w)) in ebset and codeg(u, w) >= 1)
        if not cyc:
            return None
    for i in range(7):
        if mu[i] == 0:
            continue
        mu2 = list(mu)
        mu2[i] -= 1
        _, isf = comps_and_forest(mu2, eb)
        if isf:
            return None                      # G - a is a forest => f >= alpha+2
    degs = [degA[b] + degB[b] for b in range(3)] + \
           [len(TYPES[i])] * 0
    for i in range(7):
        degs += [len(TYPES[i])] * mu[i]
    heads, res = hh_trace(degs)
    return dict(mu=tuple(mu), eb=len(eb), n=n, m=m, alpha=al, tau=3,
                degB_raw=[degA[b] + degB[b] for b in range(3)],
                degB_in=list(degB),
                degB=sorted((degA[b] + degB[b] for b in range(3)), reverse=True),
                p=mu[6], q=mu[3] + mu[4] + mu[5], r=mu[0] + mu[1] + mu[2],
                heads=heads, s=len(heads), residue=res,
                slack3=m - sum(heads[:3]))


def main():
    MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    tot = 0
    hard = 0
    viol = []
    minslack = None
    by_eb = {}
    shape = {}
    for name, eb in EB_PATTERNS:
        for mu in product(range(MAX + 1), repeat=7):
            tot += 1
            r = analyse(list(mu), eb)
            if r is None:
                continue
            hard += 1
            by_eb[name] = by_eb.get(name, 0) + 1
            if r["residue"] >= r["alpha"]:
                viol.append(r)
            k = (r["slack3"],)
            shape[k] = shape.get(k, 0) + 1
            if minslack is None or r["slack3"] < minslack["slack3"]:
                minslack = r
    print(f"[tau=3] MAXMULT={MAX}  parameter tuples scanned = {tot}")
    print(f"[tau=3] graphs in hard-core-minus-residue (connected, non-forest,")
    print(f"        diam=4, f=alpha+1, tau=3): {hard}")
    print(f"[tau=3] by e_B: {by_eb}")
    print(f"[tau=3] residue >= alpha (would be COUNTEREXAMPLES): {len(viol)}")
    print(f"[tau=3] distribution of slack3 = m - (D1+D2+D3): "
          f"{ {k[0]: v for k, v in sorted(shape.items())} }")
    if minslack:
        print(f"[tau=3] minimal-slack witness: {minslack}")
    for v in viol[:5]:
        print("  VIOLATION:", v)


if __name__ == "__main__":
    main()
