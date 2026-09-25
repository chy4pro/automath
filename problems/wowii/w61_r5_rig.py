#!/usr/bin/env python3
"""owner-w61 round 5 — numerical backing for Theorem RIG (the B-universal layer).

Written from scratch this round; does NOT reuse any earlier w61_* script.

Claims tested
  RIG-a : A a MAXIMUM independent set, B = V\\A, tau = |B|, b in B with
          deg(b) <= tau (i.e. b in B_lo) and deg_B(b) = tau-1 (b is B-universal)
          ==> deg_A(b) = 1.                        [no frame, no reductio needed]
  RIG-b : hard-core frame (connected, non-forest, diam 4, f = alpha+1) with
          B_lo nonempty and B_lo^+ = empty  ==>  the GFan(tau,L,nu) package:
          (i) every b in B_lo has deg_A(b) = 1;
          (ii) all those A-neighbours coincide in one a0;
          (iii) a0 is adjacent to ALL of B;
          (iv) every non-edge of B lies inside B_hi (nu = mbar);
          (v) every a in A\\{a0} has N(a) cap B_lo = empty;
          (vi) nu >= 1.
  RIG-c : the same instances that additionally satisfy the reductio residue = alpha
          (the hard core) must have nu <= L-1  [Corollary MB1's bound].
Also reports how often the hypothesis B_lo^+ = empty actually occurs (non-vacuity).
"""
import itertools
import random
import sys
from itertools import combinations


def residue_seq(seq):
    """Literal transcription of Lean residueAux (splitAt truncation, nat-trunc -1)."""
    s = sorted(seq, reverse=True)
    while True:
        if not s:
            return 0
        if s[0] == 0:
            return len(s)
        d = s[0]
        rest = s[1:]
        head, tail = rest[:d], rest[d:]
        head = [max(0, x - 1) for x in head]
        s = sorted(head + tail, reverse=True)


class G:
    def __init__(self, n, edges):
        self.n = n
        self.adj = [set() for _ in range(n)]
        for u, v in edges:
            if u != v:
                self.adj[u].add(v)
                self.adj[v].add(u)

    def deg(self, v):
        return len(self.adj[v])

    def degseq(self):
        return [self.deg(v) for v in range(self.n)]

    def connected(self):
        seen = {0}
        st = [0]
        while st:
            x = st.pop()
            for y in self.adj[x]:
                if y not in seen:
                    seen.add(y)
                    st.append(y)
        return len(seen) == self.n

    def diam(self):
        best = 0
        for s in range(self.n):
            dist = {s: 0}
            q = [s]
            while q:
                nq = []
                for x in q:
                    for y in self.adj[x]:
                        if y not in dist:
                            dist[y] = dist[x] + 1
                            nq.append(y)
                q = nq
            if len(dist) < self.n:
                return None
            best = max(best, max(dist.values()))
        return best

    def is_acyclic(self, S):
        S = set(S)
        e = sum(1 for u, v in combinations(sorted(S), 2) if v in self.adj[u])
        # forest iff |E| = |S| - #components
        seen, comp = set(), 0
        for s in S:
            if s in seen:
                continue
            comp += 1
            st = [s]
            seen.add(s)
            while st:
                x = st.pop()
                for y in self.adj[x] & S:
                    if y not in seen:
                        seen.add(y)
                        st.append(y)
        return e == len(S) - comp

    def f(self):
        for k in range(self.n, 0, -1):
            for S in combinations(range(self.n), k):
                if self.is_acyclic(S):
                    return k
        return 0

    def independent_sets_max(self):
        """all maximum independent sets"""
        best, out = 0, []
        for k in range(self.n, 0, -1):
            if k < best:
                break
            for S in combinations(range(self.n), k):
                ok = all(v not in self.adj[u] for u, v in combinations(S, 2))
                if ok:
                    if k > best:
                        best, out = k, [S]
                    elif k == best:
                        out.append(S)
            if out:
                break
        return best, out


def atlas_graphs(nmax):
    try:
        import networkx as nx
    except ImportError:
        return None
    out = []
    for g in nx.graph_atlas_g():
        if 2 <= g.number_of_nodes() <= nmax:
            gg = G(g.number_of_nodes(), list(g.edges()))
            if gg.connected():
                out.append(gg)
    return out


def random_graphs(count, nlo, nhi, seed=20260818):
    rnd = random.Random(seed)
    out = []
    while len(out) < count:
        n = rnd.randint(nlo, nhi)
        p = rnd.uniform(0.2, 0.75)
        edges = [(u, v) for u, v in combinations(range(n), 2) if rnd.random() < p]
        g = G(n, edges)
        if g.connected():
            out.append(g)
    return out


def run(graphs, label, do_frame=True):
    stats = dict(pairs=0, riga_tests=0, riga_fail=0,
                 frame=0, frame_L=0, hyp=0, rigb_fail=0,
                 hardcore=0, hc_hyp=0, rigc_fail=0, nu_hist={})
    fails = []
    for g in graphs:
        alpha, mis = g.independent_sets_max()
        tau = g.n - alpha
        if tau < 1:
            continue
        fval = g.f() if do_frame else None
        d = g.diam()
        res = residue_seq(g.degseq())
        acyclic_all = g.is_acyclic(range(g.n))
        for A in mis:
            Aset = set(A)
            B = [v for v in range(g.n) if v not in Aset]
            assert len(B) == tau
            stats['pairs'] += 1
            degA = {b: len(g.adj[b] - Aset ^ (g.adj[b] - Aset)) for b in B}  # placeholder
            degA = {b: len(g.adj[b] & Aset) for b in B}
            degB = {b: len(g.adj[b]) - degA[b] for b in B}
            B_hi = [b for b in B if g.deg(b) >= tau + 1]
            B_lo = [b for b in B if g.deg(b) <= tau]
            # ---- RIG-a
            for b in B_lo:
                if degB[b] == tau - 1:
                    stats['riga_tests'] += 1
                    if degA[b] != 1:
                        stats['riga_fail'] += 1
                        fails.append(('RIG-a', g.n, sorted(g.degseq(), reverse=True), b, degA[b]))
            if not do_frame:
                continue
            in_frame = (fval == alpha + 1) and d == 4 and not acyclic_all
            if not in_frame:
                continue
            stats['frame'] += 1
            L = len(B_lo)
            if L == 0:
                continue
            stats['frame_L'] += 1
            Bset = set(B)
            B_lo_plus = [b for b in B_lo if degB[b] < tau - 1]
            if B_lo_plus:
                continue
            stats['hyp'] += 1
            # ---- RIG-b package
            bad = []
            if any(degA[b] != 1 for b in B_lo):
                bad.append('i')
            nbrs = set()
            for b in B_lo:
                nbrs |= (g.adj[b] & Aset)
            if len(nbrs) != 1:
                bad.append('ii')
            a0 = next(iter(nbrs)) if len(nbrs) == 1 else None
            if a0 is not None and not Bset <= g.adj[a0]:
                bad.append('iii')
            nonedges = [(u, v) for u, v in combinations(sorted(B), 2) if v not in g.adj[u]]
            nu = len(nonedges)
            hi = set(B_hi)
            if any(not (u in hi and v in hi) for u, v in nonedges):
                bad.append('iv')
            if a0 is not None and any((g.adj[a] & set(B_lo)) for a in Aset if a != a0):
                bad.append('v')
            if nu < 1:
                bad.append('vi')
            if bad:
                stats['rigb_fail'] += 1
                fails.append(('RIG-b' + ''.join(bad), g.n, sorted(g.degseq(), reverse=True), L, nu))
            stats['nu_hist'][(L, nu)] = stats['nu_hist'].get((L, nu), 0) + 1
            # ---- RIG-c (reductio)
            if res == alpha:
                stats['hardcore'] += 1
                stats['hc_hyp'] += 1
                if nu > L - 1:
                    stats['rigc_fail'] += 1
                    fails.append(('RIG-c', g.n, sorted(g.degseq(), reverse=True), L, nu))
    print(f"[{label}] graphs={len(graphs)} (graph,A) pairs={stats['pairs']}")
    print(f"  RIG-a: tested {stats['riga_tests']} B-universal low vertices, "
          f"failures = {stats['riga_fail']}")
    if do_frame:
        print(f"  hard-core FRAME instances: {stats['frame']} (of which L>=1: {stats['frame_L']}); "
              f"hypothesis B_lo^+ = empty holds in {stats['hyp']}")
        print(f"  RIG-b package failures = {stats['rigb_fail']}")
        print(f"  of those, reductio residue=alpha (true hard core): {stats['hardcore']}; "
              f"RIG-c (nu <= L-1) failures = {stats['rigc_fail']}")
        print(f"  (L,nu) histogram on the hypothesis set: "
              f"{dict(sorted(stats['nu_hist'].items()))}")
    for f in fails[:12]:
        print("   FAIL:", f)
    return stats


def constructed_graphs(count, seed=61061):
    """Targeted generator: build B (size tau) with a chosen non-edge set, attach A
    vertices with random non-empty B-types, keep only hard-core-FRAME instances.
    This is how a thick sample of the frame is reached; uniform random graphs
    almost never land there."""
    rnd = random.Random(seed)
    out = []
    tries = 0
    while len(out) < count and tries < 400 * count:
        tries += 1
        tau = rnd.randint(3, 5)
        na = rnd.randint(3, 6)
        n = tau + na
        B = list(range(tau))
        A = list(range(tau, n))
        pairs = list(combinations(B, 2))
        nu = rnd.randint(1, max(1, len(pairs) - 1))
        missing = set(rnd.sample(pairs, min(nu, len(pairs))))
        edges = [e for e in pairs if e not in missing]
        for a in A:
            k = rnd.randint(1, tau)
            for b in rnd.sample(B, k):
                edges.append((b, a))
        g = G(n, edges)
        if not g.connected():
            continue
        if g.diam() != 4:
            continue
        alpha, _ = g.independent_sets_max()
        if alpha != na:
            continue          # A must be A MAXIMUM independent set
        if g.is_acyclic(range(n)):
            continue
        if g.f() != alpha + 1:
            continue
        out.append(g)
    return out


if __name__ == '__main__':
    tot = 0
    ga = atlas_graphs(7)
    if ga is None:
        print("networkx unavailable — atlas skipped")
    else:
        run(ga, "exhaustive connected n<=7 (atlas)")
    rg = random_graphs(1200, 8, 10)
    run(rg, "random connected n=8..10")
    rg2 = random_graphs(400, 11, 12)
    run(rg2, "random connected n=11..12", do_frame=False)
    cg = constructed_graphs(600)
    run(cg, "TARGETED hard-core-FRAME construction")
    print("done")
