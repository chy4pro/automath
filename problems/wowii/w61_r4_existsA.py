#!/usr/bin/env python3
"""
WOWII-61 round 4, side check for task (1): the *exists-A* reading of the hoped
bound  hs <= e_B + c*t.  For every trajectory of every reductio graph
(residue = alpha), test whether SOME maximum independent set A satisfies
hs <= e_B + c*t  (t = |A cap K|), for c = 1 and c = 2.

Result (archived in w61_r4_existsA.out): c=1 fails on 106 / 52 000
trajectories, c=2 fails on 4 / 52 000 (min slack -1).  So even the
choose-your-A version of task (1)'s bound is false for c <= 2.

Run: python3 w61_r4_existsA.py    (~5 s)
"""
import random
import sys

sys.path.insert(0, "$HOME/workspace/claudecode/automath/problems/wowii")
from w61_cstar import adj_masks, is_connected            # noqa: E402
from w61_r4_probe import hh_full, alpha_sets             # noqa: E402

rng = random.Random(99)
fail1 = fail2 = tested = 0
wit1 = wit2 = None
minslack2 = 10 ** 9


def test(n, edges):
    global fail1, fail2, tested, wit1, wit2, minslack2
    a = adj_masks(n, edges)
    if not is_connected(a, n):
        return
    degs = [bin(x).count('1') for x in a]
    al, isets = alpha_sets(a, n)
    tau = n - al
    trajs = [hh_full(degs)] + [hh_full(degs, rng) for _ in range(3)]
    if n - len(trajs[0][0]) != al:
        return
    for heads, surv, snaps, beta, blocks in trajs:
        tested += 1
        K = set(h[0] for h in heads)
        hs = sum(g - D for (_, g, D, _) in heads)
        b1 = b2 = -10 ** 9
        for S in isets:
            eB = sum(1 for u, v in edges if not (S >> u & 1) and not (S >> v & 1))
            t = sum(1 for v in K if S >> v & 1)
            b1 = max(b1, eB + t - hs)
            b2 = max(b2, eB + 2 * t - hs)
        if b1 < 0:
            fail1 += 1
            if wit1 is None:
                wit1 = (n, edges, degs, tau, hs, b1)
        if b2 < 0:
            fail2 += 1
            if wit2 is None:
                wit2 = (n, edges, degs, tau, hs, b2)
        minslack2 = min(minslack2, b2)


def main():
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    small = []
    for G in graph_atlas_g():
        if G.number_of_nodes() < 2 or not nx.is_connected(G):
            continue
        small.append((G.number_of_nodes(), [(u, v) for u, v in G.edges()]))
    for n, e in small:
        test(n, e)
    print(f"[existsA n<=7] traj={tested} fail(c=1)={fail1} fail(c=2)={fail2}")
    for n, edges in small:
        if n != 7:
            continue
        for mask in range(1, 1 << 7, 3):
            test(8, list(edges) + [(7, v) for v in range(7) if mask >> v & 1])
    print(f"[existsA +n8/3] traj={tested} fail(c=1)={fail1} fail(c=2)={fail2}")
    for n in range(9, 13):
        for _ in range(400):
            p = rng.choice([0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
            test(n, [(u, v) for u in range(n) for v in range(u + 1, n)
                     if rng.random() < p])
    print(f"[existsA +rand] traj={tested} fail(c=1)={fail1} fail(c=2)={fail2} "
          f"minslack(c=2)={minslack2}")
    print("wit1:", wit1)
    print("wit2:", wit2)


if __name__ == "__main__":
    main()
