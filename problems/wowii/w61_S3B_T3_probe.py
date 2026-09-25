#!/usr/bin/env python3
# Independent adversarial referee (round B) probe for Theorem T3 (tau=3).
# Written from scratch; no repo scripts consulted.
import itertools, sys
from collections import deque

# ---------------- Havel-Hakimi / residue (literal residueAux transcription) -------------
def hh(deg):
    """residueAux: [] -> 0 ; (0::s) -> 1+|s| ; else one HH step.
    Returns (residue, heads, lists) where lists[i] = sorted list before step i+1."""
    L = sorted(deg, reverse=True)
    heads = []; lists = [list(L)]
    while L and L[0] != 0:
        D = L[0]; rest = L[1:]
        for i in range(min(D, len(rest))):
            rest[i] = max(rest[i]-1, 0)
        L = sorted(rest, reverse=True)
        heads.append(D); lists.append(list(L))
    return (len(L), heads, lists)

def hh_labelled(deg_by_v, order_key):
    """Labelled HH with adversarial tie-break. order_key(v,val)->tuple used as
    secondary sort key (ascending) among equal values.  Returns list of
    (head_vertex, head_val, decremented_set, state_after) per step."""
    state = dict(deg_by_v)
    trace = []
    while state and max(state.values()) != 0:
        items = sorted(state.items(), key=lambda kv: (-kv[1], order_key(kv[0], kv[1])))
        hv, D = items[0]
        rest = items[1:]
        dec = set(v for v, _ in rest[:D])
        new = {}
        for i, (v, val) in enumerate(rest):
            new[v] = max(val-1, 0) if i < D else val
        trace.append((hv, D, dec, dict(new)))
        state = new
    return trace

# ---------------- graph helpers -------------------------------------------------
def diam(n, adj):
    best = 0
    for s in range(n):
        dist = [-1]*n; dist[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if dist[w] < 0:
                    dist[w] = dist[u]+1; q.append(w)
        if min(dist) < 0: return None   # disconnected
        best = max(best, max(dist))
    return best

def acyclic(vs, adj):
    """is the induced subgraph on the vertex set vs a forest?"""
    vs = set(vs)
    par = {v: v for v in vs}
    def find(a):
        while par[a] != a:
            par[a] = par[par[a]]; a = par[a]
        return a
    for u in vs:
        for w in adj[u]:
            if w in vs and w > u:
                ru, rw = find(u), find(w)
                if ru == rw: return False
                par[ru] = rw
    return True

# ---------------- tau = 3 parametrisation --------------------------------------
SUBS = [1,2,3,4,5,6,7]   # non-empty subsets of B = {0,1,2} as bitmasks
GB_TYPES = {
    'empty':  [],
    'edge01': [(0,1)],
    'path':   [(0,1),(1,2)],          # centre = 1
    'tri':    [(0,1),(1,2),(0,2)],
}

def build(mu, gbe):
    """mu: dict mask->multiplicity.  Returns (n, adj, Aidx, reps)."""
    n = 3 + sum(mu.values())
    adj = [set() for _ in range(n)]
    for (a,b) in gbe:
        adj[a].add(b); adj[b].add(a)
    idx = 3; reps = {}
    for mask in SUBS:
        for j in range(mu[mask]):
            if j == 0: reps[mask] = idx
            for b in range(3):
                if mask >> b & 1:
                    adj[idx].add(b); adj[b].add(idx)
            idx += 1
    return n, [sorted(s) for s in adj], list(range(3, n)), reps

def alpha_is_n3(mu, gbe):
    """A (the alpha=n-3 candidate) is maximum  <=>  for every G[B]-independent
    S subseteq B : |N_A(S)| >= |S|   (proved in the report)."""
    ebset = set(map(frozenset, [set(e) for e in gbe]))
    for r in range(1, 4):
        for S in itertools.combinations(range(3), r):
            ok = True
            for u, v in itertools.combinations(S, 2):
                if frozenset({u,v}) in ebset: ok = False
            if not ok: continue
            NA = sum(mu[mask] for mask in SUBS if any(mask >> b & 1 for b in S))
            if NA < len(S): return False
    return True

def scan(MAX, want_hardcore=True, collect=None):
    out = []
    rng = range(MAX+1)
    for name, gbe in GB_TYPES.items():
        for vec in itertools.product(rng, repeat=7):
            mu = dict(zip(SUBS, vec))
            if sum(vec) == 0: continue
            # connectivity of B under (G[B] edges) U (pairs sharing an occurring type)
            par = list(range(3))
            def find(a):
                while par[a] != a: par[a] = par[par[a]]; a = par[a]
                return a
            def uni(a,b):
                ra, rb = find(a), find(b)
                if ra != rb: par[ra] = rb
            for (a,b) in gbe: uni(a,b)
            for mask in SUBS:
                if mu[mask]:
                    bs = [b for b in range(3) if mask >> b & 1]
                    for i in range(1, len(bs)): uni(bs[0], bs[i])
            if len({find(0), find(1), find(2)}) != 1: continue
            if not all(any(mu[mask] for mask in SUBS if mask >> b & 1) or
                       any(b in e for e in gbe) for b in range(3)): continue
            if not alpha_is_n3(mu, gbe): continue
            n, adj, A, reps = build(mu, gbe)
            d = diam(n, adj)
            if d != 4: continue
            alpha = n - 3
            # f = alpha+1  <=>  no vertex removal leaves a forest
            testv = list(range(3)) + [reps[mask] for mask in SUBS if mu[mask]]
            f_ge_a2 = any(acyclic([v for v in range(n) if v != x], adj) for x in testv)
            if want_hardcore and f_ge_a2: continue
            deg = [len(adj[v]) for v in range(n)]
            res, heads, lists = hh(deg)
            rec = dict(gb=name, mu=dict(mu), n=n, m=sum(deg)//2, alpha=alpha,
                       deg=deg, res=res, heads=heads, lists=lists,
                       eB=len(gbe), Bdeg=sorted(deg[:3], reverse=True),
                       Bdeg_lab=deg[:3], f_ge_a2=f_ge_a2)
            rec['k'] = sum(1 for x in rec['Bdeg'] if x >= 4)
            rec['p'] = mu[7]; rec['q'] = mu[3]+mu[5]+mu[6]
            rec['r'] = mu[1]+mu[2]+mu[4]
            if collect is None or collect(rec): out.append(rec)
    return out

if __name__ == '__main__':
    pass
