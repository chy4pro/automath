#!/usr/bin/env python3
"""
w133 round-8 judge, part 4: falsification test of the judge's own repair lemma

  G15(d)  [proposed]  G C4-free with NO induced P6, Z an induced C6.
                      Then every vertex outside Z has 0 or 2 neighbours on Z,
                      and if 2 they are ANTIPODAL (cyclic distance exactly 3).
                      (G15(b) allowed cyclic distance 1 or 3; (C6) kills 1.)

Proof: if S ~ v_i, v_{i+1} then (S, v_i, v_{i-1}, v_{i-2}, v_{i-3}, v_{i-4}) is an
induced P6 -- Z minus v_{i+1} is an induced P5 with endpoint v_i and S has no
other Z-neighbour.

Tested on: every connected C4-free graph n<=10 (exhaustive, by augmentation)
plus structured C4-free graphs, restricted to the P6-free ones.
"""
import itertools, sys
import networkx as nx

def c4free(G):
    V = list(G)
    for i, a in enumerate(V):
        for b in V[i+1:]:
            if len(set(G[a]) & set(G[b])) >= 2:
                return False
    return True

def induced_paths(G, k):
    adj = {v: set(G[v]) for v in G}
    def ext(path, pset):
        if len(path) == k:
            yield tuple(path); return
        for w in adj[path[-1]]:
            if w in pset: continue
            if any(w in adj[z] for z in path[:-1]): continue
            path.append(w); pset.add(w)
            yield from ext(path, pset)
            path.pop(); pset.discard(w)
    for v in G:
        yield from ext([v], {v})

def has_P6(G):
    for _ in induced_paths(G, 6):
        return True
    return False

def induced_C6s(G):
    """all induced 6-cycles, as cyclic vertex tuples (each up to rotation/reflection)"""
    seen = set()
    for S in itertools.combinations(G, 6):
        H = G.subgraph(S)
        if H.number_of_edges() != 6: continue
        if any(H.degree(v) != 2 for v in S): continue
        if not nx.is_connected(H): continue
        key = frozenset(S)
        if key in seen: continue
        seen.add(key)
        # order it
        start = S[0]; order = [start]; prev = None; cur = start
        for _ in range(5):
            nxt = [w for w in H[cur] if w != prev][0]
            order.append(nxt); prev, cur = cur, nxt
        yield tuple(order)

def atlas_pool():
    return [nx.convert_node_labels_to_integers(G) for G in nx.graph_atlas_g()
            if G.number_of_nodes() >= 3 and nx.is_connected(G) and c4free(G)]

def augment(graphs, n):
    seen, out = {}, []
    for G in graphs:
        V = list(G); adj = {v: set(G[v]) for v in V}
        conflict = {v: set() for v in V}
        for i, a in enumerate(V):
            for b in V[i+1:]:
                if adj[a] & adj[b]:
                    conflict[a].add(b); conflict[b].add(a)
        for r in range(1, len(V) + 1):
            for T in itertools.combinations(V, r):
                if any(T[j] in conflict[T[i]] for i in range(r) for j in range(i+1, r)):
                    continue
                H = G.copy(); H.add_node(n-1)
                for t in T: H.add_edge(n-1, t)
                h = nx.weisfeiler_lehman_graph_hash(H, iterations=3)
                b = seen.setdefault(h, [])
                if any(nx.is_isomorphic(H, K) for K in b): continue
                b.append(H); out.append(H)
    return out

def main():
    A = atlas_pool()
    pool = list(A)
    lvl = [G for G in A if G.number_of_nodes() == 7]
    for n in (8, 9, 10):
        lvl = augment(lvl, n)
        print("exhaustive C4-free connected n=%d: %d classes" % (n, len(lvl)))
        pool += lvl
    print("pool size:", len(pool))

    ncand = nC6 = nout = nfail = 0
    dist_hist = {0: 0, 1: 0, 2: 0, 3: 0}
    fails = []
    for G in pool:
        if has_P6(G):
            continue
        ncand += 1
        for Z in induced_C6s(G):
            nC6 += 1
            pos = {v: i for i, v in enumerate(Z)}
            for v in G:
                if v in pos: continue
                nb = [pos[w] for w in G[v] if w in pos]
                nout += 1
                if len(nb) == 0:
                    dist_hist[0] += 1
                    continue
                if len(nb) != 2:
                    nfail += 1
                    fails.append(("G15(a) violated", v, nb, sorted(G.edges())))
                    continue
                d = min((nb[0]-nb[1]) % 6, (nb[1]-nb[0]) % 6)
                dist_hist[d] += 1
                if d != 3:
                    nfail += 1
                    fails.append(("G15(d) violated: cyclic distance %d" % d,
                                  v, nb, sorted(G.edges())))
    print("\nP6-free C4-free graphs in pool : %d" % ncand)
    print("induced C6 instances           : %d" % nC6)
    print("outside vertices tested        : %d" % nout)
    print("Z-neighbour-count / cyclic-distance histogram (0 nbrs / d=1 / d=2 / d=3):",
          dist_hist)
    print("FAILURES of proposed G15(d)    : %d" % nfail)
    for f in fails[:5]:
        print("  ", f[:3])
    return 0 if nfail == 0 else 2

if __name__ == "__main__":
    sys.exit(main())
