"""owner-w61 round 4 — proof-internal check of Theorem SL (draft §7.6 F).

Theorem SL: under the reductio residue(G)=alpha(G) (s=tau>=2), L >= 1 implies
    slack := L(tau+1) - (Sum_{b in B_lo} deg b + nu) >= 1.

The proof runs: assume slack = 0, so every low head i has D_i = s-i+2.  Let
i0 = max I_lo and let j = max{k < i0 : x not in block_k} (the last escape step of
the head x deleted at i0).  The proof asserts, in order:

  (P1) |E| = s+1-g >= 1, so j exists, and v_j = s-j+1 exactly;
  (P2) every entry of block_j has value >= v_j (block is a prefix);
  (P3) survivors in block_j have value exactly s-j+1, hence lie in block_k for
       every k in [j, s];
  (P4) every high head (original degree >= s+1) lies in every earlier block;
  (P5) D_{i0} >= s_j + (s - i0), hence s_j <= 2;
  (P6) D_j = (s-j-l_j) + lam_j + s_j <= s-j+1  with lam_j <= l_j - 1;
  (P7) but D_j >= s-j+2 (high head via DICH(b), or low head via slack=0)  --> contra.

Since slack = 0 with L >= 1 should never occur, (P1)-(P7) are checked in a
*counterfactual* way: we check (P2)-(P4) unconditionally on every trajectory, and
we check the conditional chain on the nearest realisable configurations, namely
every low head that attains DICH(c) with equality (D_i = s-i+2) even when the
global slack is positive.  Additionally we record whether the sharper
unconditional claim "D_{max I_lo} <= s - max I_lo + 1" ever fails.
"""
import random
from itertools import combinations
from collections import Counter

import networkx as nx
from networkx.generators.atlas import graph_atlas_g


def hh(deg, rng=None):
    cur = dict(deg)
    heads, hvals, blocks, snaps = [], [], [], []
    while cur and max(cur.values()) > 0:
        items = list(cur.items())
        if rng is not None:
            rng.shuffle(items)
        items.sort(key=lambda kv: -kv[1])
        snaps.append(dict(cur))
        h, D = items[0]
        del cur[h]
        blk = {lab for lab, _ in items[1:][:D]}
        for lab in blk:
            cur[lab] -= 1
        heads.append(h)
        hvals.append(D)
        blocks.append(blk)
    return heads, hvals, blocks, snaps


def max_ind_sets(G):
    nodes = list(G.nodes())
    for r in range(len(nodes), 0, -1):
        out = [set(S) for S in combinations(nodes, r)
               if all(not G.has_edge(u, v) for u, v in combinations(S, 2))]
        if out:
            return r, out
    return 0, []


def run(G, R, rng):
    n = G.number_of_nodes()
    if n < 2 or not nx.is_connected(G):
        return
    deg = dict(G.degree())
    alpha, isets = max_ind_sets(G)
    tau = n - alpha
    for heads, hvals, blocks, snaps in [hh(deg)] + [hh(deg, rng) for _ in range(4)]:
        s = len(heads)
        if n - s != alpha or s < 2:
            continue
        survivors = set(deg) - set(heads)
        pos = {lab: i + 1 for i, lab in enumerate(heads)}
        Ilo = [i + 1 for i, lab in enumerate(heads) if deg[lab] <= s]
        Ihi = [i + 1 for i, lab in enumerate(heads) if deg[lab] >= s + 1]
        R['traj'] += 1

        # (P4) every high head lies in every earlier block
        for i in Ihi:
            for k in range(1, i):
                if heads[i - 1] not in blocks[k - 1]:
                    R['P4'] += 1

        # (P3)+F3: survivors' values are <= s-j+1 at the start of step j
        for j in range(1, s + 1):
            for v in survivors:
                if snaps[j - 1].get(v, 0) > s - j + 1:
                    R['F3'] += 1

        for A in isets:
            B = [v for v in G.nodes() if v not in A]
            eB = G.subgraph(B).number_of_edges()
            nu = tau * (tau - 1) // 2 - eB
            Blo = [b for b in B if deg[b] <= tau]
            L = len(Blo)
            slack = L * (tau + 1) - (sum(deg[b] for b in Blo) + nu)
            if L >= 1:
                R['L>=1'] += 1
                if slack <= 0:
                    R['SL_fail'] += 1
                i0 = max(Ilo)
                if hvals[i0 - 1] > s - i0 + 1:
                    R['sharp_fail'] += 1          # sharper unconditional variant
            break                                  # slack/L are A-dependent only

        # counterfactual chain on every low head attaining DICH(c) with equality
        for i in Ilo:
            x, g, D = heads[i - 1], deg[heads[i - 1]], hvals[i - 1]
            if D != s - i + 2:
                continue
            R['eqhead'] += 1
            Esc = [k for k in range(1, i) if x not in blocks[k - 1]]
            if len(Esc) != s + 1 - g:                                   # (P1a)
                R['P1a'] += 1
            if not Esc:
                R['P1b'] += 1
                continue
            j = max(Esc)
            if snaps[j - 1][x] != s - j + 1:                            # (P1c)
                R['P1c'] += 1
            vj = snaps[j - 1][x]
            if any(snaps[j - 1][lab] < vj for lab in blocks[j - 1]):    # (P2)
                R['P2'] += 1
            sj = [lab for lab in blocks[j - 1] if lab in survivors]
            if any(snaps[j - 1][lab] != s - j + 1 for lab in sj):       # (P3a)
                R['P3a'] += 1
            for k in range(j, s + 1):                                   # (P3b)
                for lab in sj:
                    if lab not in blocks[k - 1]:
                        R['P3b'] += 1
            if hvals[i - 1] < len(sj) + (s - i):                        # (P5)
                R['P5'] += 1
            R['sj'][len(sj)] += 1
            lj = len([k for k in Ilo if k > j])
            lamj = len([k for k in Ilo if k > j and heads[k - 1] in blocks[j - 1]])
            if lamj > lj - 1:                                           # (P6a)
                R['P6a'] += 1
            if hvals[j - 1] != (s - j - lj) + lamj + len(sj):            # (P6b)
                R['P6b'] += 1
            if i == max(Ilo) and hvals[j - 1] > s - j + 1:               # (P6c)
                R['P6c'] += 1


def main():
    rng = random.Random(777)
    R = Counter()
    R['sj'] = Counter()
    for G in graph_atlas_g():
        run(G, R, rng)
    print(f"[atlas n<=7]  {dict((k, v) for k, v in R.items() if k != 'sj')}")
    for n in range(8, 14):
        for _ in range(1500):
            G = nx.gnp_random_graph(n, rng.uniform(0.25, 0.85),
                                    seed=rng.randrange(1 << 30))
            run(G, R, rng)
    for _ in range(4000):
        tau, al = rng.randint(3, 7), rng.randint(2, 7)
        G = nx.Graph()
        Bv = [('b', i) for i in range(tau)]
        for u, v in combinations(Bv, 2):
            if rng.random() > 0.12:
                G.add_edge(u, v)
        G.add_nodes_from(Bv)
        for j in range(al):
            for b in rng.sample(Bv, rng.randint(1, tau)):
                G.add_edge(('a', j), b)
        run(G, R, rng)
    print(f"[+random+near-split]  {dict((k, v) for k, v in R.items() if k != 'sj')}")
    print(f"[s_j histogram at equality heads] {dict(sorted(R['sj'].items()))}")


if __name__ == '__main__':
    main()
