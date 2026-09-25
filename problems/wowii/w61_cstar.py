#!/usr/bin/env python3
"""
WOWII-61 round 3 (owner-w61): numerical test of Lemma C* , the tau-uniform
analogue of the C1/C2/C3 B-degree lower bounds of draft 7.3.1.

  Hard core:  G connected, non-forest, diam(G) = 4, f(G) = alpha(G) + 1.
  A a maximum independent set, B = V \\ A, types  T = N(a) subset of B  for a in A,
  mu[T] = #{a in A : N(a) = T}.
  (F-b):  there are two OCCURRING types T1, T2, disjoint, with no G[B]-edge
          between them  (this is what diam = 4 forces).

  LEMMA C*  : for every such pair (T1,T2) and every b in T1 union T2,
              deg_A(b) >= 3   (hence deg(b) >= 3 + deg_B(b)).
  CONTROL C0: for b outside T1 union T2 only deg_A(b) >= 2 is claimed when b has a
              non-neighbour in B (this is the *weak* side; measured, not claimed).

Also measured: how often ALL of B has degree >= tau+1 (Theorem N hypothesis (i))
inside the hard core, per tau -- the quantity that decides whether the
Theorem N / N' line can ever be tau-uniform on its own.

Run: python3 w61_cstar.py        (exhaustive n<=7 and the n=8 cover)
"""
import itertools
from collections import Counter


def adj_masks(n, edges):
    a = [0] * n
    for (u, v) in edges:
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def is_connected(a, n):
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
            return -1
        best = max(best, max(dist))
    return best


def is_forest_subset(a, n, S):
    """G[S] acyclic?  edges(S) == |S| - #components(S)"""
    verts = [v for v in range(n) if S >> v & 1]
    idx = {v: i for i, v in enumerate(verts)}
    par = list(range(len(verts)))

    def find(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    ne = 0
    for i, v in enumerate(verts):
        m = a[v] & S
        while m:
            b = m & -m
            m ^= b
            w = b.bit_length() - 1
            if w > v:
                ne += 1
                ra, rb = find(idx[v]), find(idx[w])
                if ra == rb:
                    return False
                par[ra] = rb
    return True


def alpha_sets(a, n):
    best, sets = 0, []
    for S in range(1 << n):
        ok, m = True, S
        while m:
            b = m & -m
            m ^= b
            if a[b.bit_length() - 1] & S:
                ok = False
                break
        if not ok:
            continue
        c = bin(S).count('1')
        if c > best:
            best, sets = c, [S]
        elif c == best:
            sets.append(S)
    return best, sets


def largest_forest(a, n):
    for k in range(n, 0, -1):
        for S in range(1 << n):
            if bin(S).count('1') == k and is_forest_subset(a, n, S):
                return k
    return 0


class R:
    def __init__(self):
        self.hard = 0
        self.pairs = 0
        self.failCstar = 0
        self.wit = None
        self.tau_hist = Counter()
        self.tau_allhigh = Counter()      # hard-core cases with min_B deg >= tau+1
        self.outside_deg2_fail = 0


def test(n, edges, R_):
    a = adj_masks(n, edges)
    if not is_connected(a, n):
        return
    if diameter(a, n) != 4:
        return
    al, isets = alpha_sets(a, n)
    f = largest_forest(a, n)
    if f != al + 1:
        return
    if f == n:                                   # forest
        return
    degs = [bin(x).count('1') for x in a]
    tau = n - al
    R_.hard += 1
    R_.tau_hist[tau] += 1
    for S in isets:
        B = [v for v in range(n) if not (S >> v & 1)]
        Bset = set(B)
        if min(degs[b] for b in B) >= tau + 1:
            R_.tau_allhigh[tau] += 1
        # types
        mu = {}
        for v in range(n):
            if S >> v & 1:
                T = frozenset(w for w in B if a[v] >> w & 1)
                mu[T] = mu.get(T, 0) + 1
        degA = {b: sum(1 for v in range(n) if (S >> v & 1) and (a[v] >> b & 1))
                for b in B}
        occ = [T for T in mu if mu[T] > 0]
        for T1, T2 in itertools.combinations(occ, 2):
            if T1 & T2:
                continue
            if any(a[u] >> w & 1 for u in T1 for w in T2):
                continue
            R_.pairs += 1
            for b in T1 | T2:
                if degA[b] < 3:
                    R_.failCstar += 1
                    if R_.wit is None:
                        R_.wit = (n, edges, sorted(degs), tau,
                                  sorted(T1), sorted(T2), b, degA[b])
            for b in Bset - (T1 | T2):
                nonnb = any((not (a[b] >> c & 1)) and c != b for c in B)
                if nonnb and degA[b] < 2:
                    R_.outside_deg2_fail += 1


def main():
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    R_ = R()
    small = []
    for G in graph_atlas_g():
        if G.number_of_nodes() < 2 or not nx.is_connected(G):
            continue
        small.append((G.number_of_nodes(), [(u, v) for u, v in G.edges()]))
    for n, e in small:
        test(n, e, R_)
    print(f"[C* n<=7 exhaustive] hard-core graphs={R_.hard} (F-b) pairs={R_.pairs} "
          f"C* failures={R_.failCstar} outside-deg>=2 failures={R_.outside_deg2_fail}")
    for n, edges in small:
        if n != 7:
            continue
        for mask in range(1, 1 << 7):
            e2 = list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            test(8, e2, R_)
    print(f"[C* +n=8 cover]      hard-core graphs={R_.hard} (F-b) pairs={R_.pairs} "
          f"C* failures={R_.failCstar} outside-deg>=2 failures={R_.outside_deg2_fail}")
    print(f"[C*] hard-core tau histogram: {dict(sorted(R_.tau_hist.items()))}")
    print(f"[C*] hard-core cases with min_B deg >= tau+1 (Theorem N hyp (i)), "
          f"per tau: {dict(sorted(R_.tau_allhigh.items()))}")
    if R_.wit:
        print("  WITNESS C*", R_.wit)


if __name__ == "__main__":
    main()
