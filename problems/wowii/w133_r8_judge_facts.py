#!/usr/bin/env python3
"""
w133 round-8 INDEPENDENT (non-Qwen) adversarial judge of Lemma G25 / Theorem G26 (draft §18).

Everything here is written from scratch by the S3 judge; no Qwen material consulted.
Tests only the *unconditional* sub-claims (the RES(b)-internal steps cannot be sampled,
they are audited by hand in the report).

Pool:
  P1  every connected C4-free graph on n <= 7   (networkx atlas)
  P2  every connected C4-free graph on n = 8,9  (augmentation + WL/VF2 isomorph rejection)
  P3  structured: Petersen, Hoffman-Singleton, ER_q polarity graphs, +pendant/subdivision
  P4  random maximal C4-free graphs n = 12..40
"""
import itertools, random, sys
import networkx as nx

# ---------------------------------------------------------------- basic utils
def c4free(G):
    """no two distinct vertices have >= 2 common neighbours (== no C4 subgraph)"""
    nodes = list(G)
    adj = {v: set(G[v]) for v in nodes}
    for i, x in enumerate(nodes):
        for y in nodes[i + 1:]:
            if len(adj[x] & adj[y]) >= 2:
                return False
    return True

def indep(G, S):
    """exact independence number of G[S]"""
    S = set(S)
    if not S:
        return 0
    adj = {v: set(G[v]) & S for v in S}
    best = [0]
    def bb(cand, cur):
        if cur + len(cand) <= best[0]:
            return
        if not cand:
            best[0] = max(best[0], cur)
            return
        v = max(cand, key=lambda x: len(adj[x] & cand))
        bb(cand - adj[v] - {v}, cur + 1)
        bb(cand - {v}, cur)
    bb(set(S), 0)
    return best[0]

def avalue(G, v):
    return indep(G, set(G[v]))

def induced_paths(G, k):
    """yield vertex tuples of induced paths on exactly k vertices"""
    adj = {v: set(G[v]) for v in G}
    def ext(path, pset):
        if len(path) == k:
            yield tuple(path)
            return
        last = path[-1]
        for w in adj[last]:
            if w in pset:
                continue
            # induced: w adjacent to none of path[:-1]
            if any(w in adj[z] for z in path[:-1]):
                continue
            path.append(w); pset.add(w)
            yield from ext(path, pset)
            path.pop(); pset.discard(w)
    for v in G:
        yield from ext([v], {v})

def has_induced_P(G, k):
    for _ in induced_paths(G, k):
        return True
    return False

# ---------------------------------------------------------------- pool builders
def atlas_pool():
    out = []
    for G in nx.graph_atlas_g():
        if G.number_of_nodes() < 3:
            continue
        if not nx.is_connected(G):
            continue
        if not c4free(G):
            continue
        out.append(nx.convert_node_labels_to_integers(G))
    return out

def augment_c4free(graphs, n):
    """all connected C4-free graphs on n vertices from those on n-1, with iso rejection"""
    seen = {}
    out = []
    for G in graphs:
        V = list(G)
        adj = {v: set(G[v]) for v in V}
        # conflict graph: u~v iff they already share a neighbour -> cannot both be
        # neighbours of the new vertex; also u~v if u,v adjacent? no: adjacent pair
        # sharing new vertex creates a triangle, which is fine (C4-free allows triangles)
        conflict = {v: set() for v in V}
        for i, x in enumerate(V):
            for y in V[i + 1:]:
                if adj[x] & adj[y]:
                    conflict[x].add(y); conflict[y].add(x)
        # enumerate independent sets of `conflict`, non-empty
        for r in range(1, len(V) + 1):
            for T in itertools.combinations(V, r):
                ok = True
                for i in range(r):
                    for j in range(i + 1, r):
                        if T[j] in conflict[T[i]]:
                            ok = False; break
                    if not ok: break
                if not ok:
                    continue
                H = G.copy()
                new = n - 1
                H.add_node(new)
                for t in T:
                    H.add_edge(new, t)
                assert c4free(H)
                h = nx.weisfeiler_lehman_graph_hash(H, iterations=3)
                bucket = seen.setdefault(h, [])
                if any(nx.is_isomorphic(H, K) for K in bucket):
                    continue
                bucket.append(H)
                out.append(H)
    return out

def petersen():
    return nx.petersen_graph()

def hoffman_singleton():
    # standard construction: 5 pentagons P_h, 5 pentagrams Q_i, P_h[j] ~ Q_i[i*h+j mod 5]
    G = nx.Graph()
    for h in range(5):
        for j in range(5):
            G.add_edge(('P', h, j), ('P', h, (j + 1) % 5))
            G.add_edge(('Q', h, j), ('Q', h, (j + 2) % 5))
    for h in range(5):
        for i in range(5):
            for j in range(5):
                G.add_edge(('P', h, j), ('Q', i, (i * h + j) % 5))
    return nx.convert_node_labels_to_integers(G)

def er_polarity(q):
    """Erdos-Renyi orthogonal polarity graph over GF(q), q prime"""
    pts = []
    for a in range(q):
        for b in range(q):
            pts.append((a, b, 1))
    for a in range(q):
        pts.append((a, 1, 0))
    pts.append((1, 0, 0))
    G = nx.Graph()
    G.add_nodes_from(range(len(pts)))
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            x, y = pts[i], pts[j]
            if sum(x[k] * y[k] for k in range(3)) % q == 0:
                G.add_edge(i, j)
    return G

def random_maximal_c4free(n, seed):
    rnd = random.Random(seed)
    G = nx.Graph(); G.add_nodes_from(range(n))
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    rnd.shuffle(pairs)
    for (i, j) in pairs:
        G.add_edge(i, j)
        # local C4 check
        bad = False
        for x in (i, j):
            for y in G:
                if y == x: continue
                if len(set(G[x]) & set(G[y])) >= 2:
                    bad = True; break
            if bad: break
        if bad:
            G.remove_edge(i, j)
    return G

def add_leaf(G):
    H = G.copy(); v = max(H) + 1
    H.add_edge(v, min(H))
    return H

def add_triangle_leaf(G):
    """attach a new vertex u to two adjacent vertices? that would make a=1 with p~q"""
    H = G.copy()
    for x in G:
        for y in G[x]:
            v = max(H) + 1
            H.add_edge(v, x); H.add_edge(v, y)
            if c4free(H):
                return H
            H.remove_node(v)
    return None

def subdivide_one_edge(G):
    H = G.copy(); e = next(iter(H.edges()))
    v = max(H) + 1
    H.remove_edge(*e); H.add_edge(e[0], v); H.add_edge(v, e[1])
    return H

# ---------------------------------------------------------------- the tests
FAIL = []
CNT = {}
def bump(k, m=1): CNT[k] = CNT.get(k, 0) + m
def check(cond, tag, info):
    bump(tag)
    if not cond:
        FAIL.append((tag, info))

def test_general(G, name):
    """U1: C[N(v)] is a matching+isolated;  a(v)=d-t;  a(v) >= ceil(d/2)."""
    for v in G:
        N = set(G[v])
        sub = G.subgraph(N)
        maxdeg = max((sub.degree(x) for x in N), default=0)
        check(maxdeg <= 1, "U1 nbhd is matching", (name, v, maxdeg))
        t = sub.number_of_edges()
        a = indep(G, N)
        check(a == len(N) - t, "U1 a(v)=d(v)-t(v)", (name, v, a, len(N), t))
        check(a >= -(-len(N) // 2), "U1 a(v)>=ceil(d/2)", (name, v, a, len(N)))

def test_G22(G, name):
    """U2: C4-free + no induced P6  =>  every induced-P5 endpoint has degree <= 5"""
    if has_induced_P(G, 6):
        return
    bump("U2 P6-free graphs seen")
    for P in induced_paths(G, 5):
        bump("U2 induced-P5 endpoints")
        if G.degree(P[0]) > 5:
            FAIL.append(("U2 G22(5)", (name, P, G.degree(P[0]))))

def test_config(G, name):
    """G23 / G25(a)(b)(c) / the G25(d) induced-P5, on every triangular endpoint u."""
    sp = dict(nx.all_pairs_shortest_path_length(G))
    for u in G:
        if G.degree(u) != 2:
            continue
        p, q = list(G[u])
        if not G.has_edge(p, q):
            continue                       # a(u)=1 needs N(u) a clique
        if max(sp[u].values()) != 3:
            continue
        bump("carriers (a=1,d=2,ecc=3)")
        Bp = set(G[p]) - {u, q}
        Bq = set(G[q]) - {u, p}
        D = {y for y in G if sp[u][y] == 3}
        # ---- G23(a)
        check(set(G[p]) & set(G[q]) == {u}, "G23(a) N(p)^N(q)={u}", (name, u))
        check(Bp.isdisjoint(Bq), "G23 Bp,Bq disjoint", (name, u))
        check(G.number_of_nodes() == 3 + len(Bp) + len(Bq) + len(D),
              "layer count n=3+bp+bq+|D|", (name, u))
        check(not (set(G[p]) & D) and not (set(G[q]) & D),
              "p,q have no D-neighbour", (name, u))
        # ---- G25(a)  NO edge between B_p and B_q
        for b in Bp:
            for c in Bq:
                check(not G.has_edge(b, c), "G25(a) no Bp-Bq edge", (name, u, b, c))
        # ---- <=1 parent per side
        for y in D:
            check(len(set(G[y]) & Bp) <= 1, "<=1 Bp-parent", (name, u, y))
            check(len(set(G[y]) & Bq) <= 1, "<=1 Bq-parent", (name, u, y))
        # ---- a(p) = beta_p + 1 - e_p   (J5)
        ep = G.subgraph(Bp).number_of_edges()
        eq = G.subgraph(Bq).number_of_edges()
        check(indep(G, set(G[p])) == len(Bp) + 1 - ep, "J5 a(p)=beta_p+1-e_p",
              (name, u, indep(G, set(G[p])), len(Bp), ep))
        check(indep(G, set(G[q])) == len(Bq) + 1 - eq, "J5 a(q)=beta_q+1-e_q",
              (name, u, indep(G, set(G[q])), len(Bq), eq))
        check(ep <= len(Bp) // 2 and eq <= len(Bq) // 2, "J5 e_x is a matching",
              (name, u, ep, len(Bp), eq, len(Bq)))
        # ---- G25(b)
        for h in Bp | Bq:
            dh = len(set(G[h]) & D)
            check(avalue(G, h) <= 1 + dh, "G25(b) a(h)<=1+delta_h", (name, u, h))
        # ---- G25(c)   ecc(b)=2  =>  beta_q <= delta_b
        for b in Bp:
            if max(sp[b].values()) == 2:
                check(len(Bq) <= len(set(G[b]) & D), "G25(c) p-side",
                      (name, u, b, len(Bq), len(set(G[b]) & D)))
        for c in Bq:
            if max(sp[c].values()) == 2:
                check(len(Bp) <= len(set(G[c]) & D), "G25(c) q-side",
                      (name, u, c, len(Bp), len(set(G[c]) & D)))
        # ---- G25(d): the 5-tuple (h,y,c,q,u) is an induced P5 whenever
        #      h in Bp, y in N(h)^D, c in Bq^N(y)
        for h in Bp:
            for y in set(G[h]) & D:
                for c in set(G[y]) & Bq:
                    T = [h, y, c, q, u]
                    ok = (len(set(T)) == 5
                          and G.has_edge(h, y) and G.has_edge(y, c)
                          and G.has_edge(c, q) and G.has_edge(q, u)
                          and not G.has_edge(h, c) and not G.has_edge(h, q)
                          and not G.has_edge(h, u) and not G.has_edge(y, q)
                          and not G.has_edge(y, u) and not G.has_edge(c, u))
                    check(ok, "G25(d) (h,y,c,q,u) induced P5", (name, u, T))
        # ---- G25(d) FULL statement, testable outside RES(b):
        #      ecc(h)=2  and  beta_q>=1  and  P6-free  =>  d(h) <= 5
        if len(Bq) >= 1 and len(Bp) >= 1 and not has_induced_P(G, 6):
            for h in Bp:
                if max(sp[h].values()) == 2:
                    check(G.degree(h) <= 5, "G25(d) full: deg<=5", (name, u, h, G.degree(h)))
        # ---- G24(d) injectivity of the two-parent map
        seenpair = {}
        for y in D:
            pb = set(G[y]) & Bp; qb = set(G[y]) & Bq
            if pb and qb:
                key = (next(iter(pb)), next(iter(qb)))
                check(key not in seenpair, "G24(d) two-parent injective",
                      (name, u, y, seenpair.get(key), key))
                seenpair[key] = y

# ---------------------------------------------------------------- run
def main():
    pool = []
    A = atlas_pool()
    pool += [(G, "atlas%d_%d" % (G.number_of_nodes(), i)) for i, G in enumerate(A)]
    print("atlas C4-free connected (n<=7):", len(A))

    # exhaustive C4-free n=8,9 by augmentation
    lvl = [G for G in A if G.number_of_nodes() == 7]
    for n in (8, 9, 10):
        lvl = augment_c4free(lvl, n)
        print("exhaustive C4-free connected n=%d classes: %d" % (n, len(lvl)))
        pool += [(G, "ex%d_%d" % (n, i)) for i, G in enumerate(lvl)]

    struct = []
    P = petersen(); struct.append((P, "Petersen"))
    HS = hoffman_singleton(); struct.append((HS, "HS"))
    for q in (3, 5, 7, 11):
        E = er_polarity(q); struct.append((E, "ER_%d" % q))
    base = [g for g, _ in struct]
    for G, nm in list(struct):
        struct.append((add_leaf(G), nm + "+leaf"))
        t = add_triangle_leaf(G)
        if t is not None:
            struct.append((t, nm + "+trileaf"))
        s2 = subdivide_one_edge(G)
        if c4free(s2):
            struct.append((s2, nm + "+subdiv"))
    for s in range(24):
        n = 12 + s
        struct.append((random_maximal_c4free(n, 1000 + s), "rndmax%d_%d" % (n, s)))
    struct = [(G, nm) for (G, nm) in struct if c4free(G)]
    pool += struct
    print("structured graphs:", len(struct), " total pool:", len(pool))

    for G, nm in pool:
        if not nx.is_connected(G):
            continue
        test_general(G, nm)
        if G.number_of_nodes() <= 14:
            test_G22(G, nm)
        test_config(G, nm)

    print("\n--- counts ---")
    for k in sorted(CNT):
        print("  %-40s %d" % (k, CNT[k]))
    print("\n--- failures: %d ---" % len(FAIL))
    for f in FAIL[:40]:
        print("   ", f)
    return 0 if not FAIL else 2

if __name__ == "__main__":
    sys.exit(main())
