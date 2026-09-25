"""owner-w61 round 4 — focused probe of the decisive open step of draft §7.6:

    (SL)   under the reductio hypothesis residue(G) = alpha(G),
           L >= 1  ==>  slack >= 1,
    where  slack := L*(tau+1) - ( Sum_{b in B_lo} deg(b) + nu ).

Corollary L1' (draft §7.6 B) shows the residual hard-core L = 1 configuration has
slack exactly 0, so (SL) at L = 1 closes L = 1 outright.  Equivalent sharp form
at L = 1 (derived in the round-4 report):

    (SL1)  L = 1  ==>  deg_A(b0) + mbar <= 1,
           i.e. deg_A(b0) = 1 AND B_hi is a clique.

This script tests (SL) and (SL1) on a much larger and denser corpus than
`w61_r4_low.py`, because the Conditional Theorem of §7.6 B rests on them.
Independent labelled-HH implementation (same as w61_r4_low.py, owner-written).
"""
import random
from itertools import combinations
from collections import Counter

import networkx as nx
from networkx.generators.atlas import graph_atlas_g


def hh(deg, rng=None):
    cur = dict(deg)
    heads, hvals = [], []
    while cur and max(cur.values()) > 0:
        items = list(cur.items())
        if rng is not None:
            rng.shuffle(items)
        items.sort(key=lambda kv: -kv[1])
        h, D = items[0]
        del cur[h]
        for lab, _ in items[1:][:D]:
            cur[lab] -= 1
        heads.append(h)
        hvals.append(D)
    return heads, hvals


def max_ind_sets(G, cap=200):
    nodes = list(G.nodes())
    for r in range(len(nodes), 0, -1):
        out = [set(S) for S in combinations(nodes, r)
               if all(not G.has_edge(u, v) for u, v in combinations(S, 2))]
        if out:
            return r, out[:cap]
    return 0, []


def run(G, R, rng):
    n = G.number_of_nodes()
    if n < 2 or not nx.is_connected(G):
        return
    deg = dict(G.degree())
    alpha, isets = max_ind_sets(G)
    tau = n - alpha
    trajs = [hh(deg)] + [hh(deg, rng) for _ in range(4)]
    trajs = [t for t in trajs if n - len(t[0]) == alpha]
    if not trajs:
        return
    R['graphs'] += 1
    for A in isets:
        B = [v for v in G.nodes() if v not in A]
        eB = G.subgraph(B).number_of_edges()
        nu = tau * (tau - 1) // 2 - eB
        Blo = [b for b in B if deg[b] <= tau]
        Bhi = [b for b in B if deg[b] >= tau + 1]
        L = len(Blo)
        mbar = len(Bhi) * (len(Bhi) - 1) // 2 - G.subgraph(Bhi).number_of_edges()
        slack = L * (tau + 1) - (sum(deg[b] for b in Blo) + nu)
        R['checks'] += 1
        R['minslack'][L] = min(R['minslack'].get(L, 10 ** 9), slack)
        if L >= 1 and slack <= 0:
            R['SL_fail'] += 1
            R.setdefault('SL_wit', (n, sorted(G.edges()), sorted(A), tau, L, slack))
        if L == 1:
            b0 = Blo[0]
            degA0 = sum(1 for w in G[b0] if w in A)
            R['L1'] += 1
            if degA0 + mbar > 1:
                R['SL1_fail'] += 1
                R.setdefault('SL1_wit', (n, sorted(G.edges()), sorted(A), tau,
                                         degA0, mbar))
            R['L1_profile'][(degA0, mbar)] += 1


def main():
    rng = random.Random(4242)
    R = {'graphs': 0, 'checks': 0, 'SL_fail': 0, 'SL1_fail': 0, 'L1': 0,
         'minslack': {}, 'L1_profile': Counter()}

    for G in graph_atlas_g():
        run(G, R, rng)
    print(f"[atlas n<=7] graphs={R['graphs']} checks={R['checks']} "
          f"SL_fail={R['SL_fail']} SL1_fail={R['SL1_fail']} L1={R['L1']}")

    for n in range(8, 15):
        for _ in range(2500):
            p = rng.uniform(0.25, 0.85)
            G = nx.gnp_random_graph(n, p, seed=rng.randrange(1 << 30))
            run(G, R, rng)
    print(f"[+random n=8..14 dense] graphs={R['graphs']} checks={R['checks']} "
          f"SL_fail={R['SL_fail']} SL1_fail={R['SL1_fail']} L1={R['L1']}")

    # split graphs and near-split graphs: these are where L is small and B is dense,
    # i.e. exactly the regime Proposition L1 lives in
    for _ in range(6000):
        tau = rng.randint(3, 7)
        al = rng.randint(2, 7)
        G = nx.Graph()
        Bv = [('b', i) for i in range(tau)]
        for u, v in combinations(Bv, 2):          # B a clique minus a few edges
            if rng.random() > 0.12:
                G.add_edge(u, v)
        G.add_nodes_from(Bv)
        for j in range(al):
            k = rng.randint(1, tau)
            for b in rng.sample(Bv, k):
                G.add_edge(('a', j), b)
        if G.number_of_nodes() == tau + al:
            run(G, R, rng)
    print(f"[+near-split] graphs={R['graphs']} checks={R['checks']} "
          f"SL_fail={R['SL_fail']} SL1_fail={R['SL1_fail']} L1={R['L1']}")

    print(f"[minslack per L] {dict(sorted(R['minslack'].items()))}")
    print(f"[L=1 profile (deg_A(b0), mbar)] {dict(sorted(R['L1_profile'].items()))}")
    for k in ('SL_wit', 'SL1_wit'):
        if k in R:
            print(f"WITNESS {k}: {R[k]}")


if __name__ == '__main__':
    main()
