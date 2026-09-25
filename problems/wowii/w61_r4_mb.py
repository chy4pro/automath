"""owner-w61 round 4 — verification of the INGREDIENTS of Theorem MB (draft §7.6 G).

Important firewall.  Theorem MB and Proposition L2 are statements about the
*hard core with the reductio* (connected, non-forest, diam 4, f = alpha+1,
residue = alpha), which is conjecturally EMPTY.  They therefore cannot be
falsified numerically as composite statements -- any test would pass vacuously.
What CAN be tested is each ingredient separately:

  (a) the degree count of Theorem MB's proof, which needs only
      diam 4 + f = alpha+1 (Lemma 4, Lemma C*, maximality of A) and NOT the
      reductio:
        Sum_{b in B_lo} deg_A(b)  >=  (L - |B_lo^+|) + 2(|B_lo^+| - c) + 3c
                                  =   L + |B_lo^+| + c
      together with the sub-claims
        (a1) every b in B has an A-neighbour,
        (a2) every b in B_lo with a non-neighbour in B has deg_A(b) >= 2,
        (a3) every b in B_lo cap (T1 cup T2) has deg_A(b) >= 3 and lies in B_lo^+;
  (b) Theorem SL itself, which needs only the reductio -- already verified in
      w61_r4_thmSL.py.

MB = (a) + (b), so verifying both is the strongest available check.

Hard-core instances are generated two ways: the exhaustive connected atlas
n <= 7, and a bounded parameter scan in the style of Lemma P (§7.2 D) --
choose G[B] and the type multiplicities mu[T], which determines G up to
isomorphism -- for tau = 3..6.  This is a scan of a box, not a blind search.
"""
import random
from itertools import combinations, chain
from collections import Counter

import networkx as nx
from networkx.generators.atlas import graph_atlas_g


def max_ind_sets(G):
    nodes = list(G.nodes())
    for r in range(len(nodes), 0, -1):
        out = [set(S) for S in combinations(nodes, r)
               if all(not G.has_edge(u, v) for u, v in combinations(S, 2))]
        if out:
            return r, out
    return 0, []


def forest_number(G):
    nodes = list(G.nodes())
    for r in range(len(nodes), 0, -1):
        for S in combinations(nodes, r):
            H = G.subgraph(S)
            if H.number_of_edges() == H.number_of_nodes() - nx.number_connected_components(H):
                return r
    return 0


def fb_pairs(G, A, B):
    """(F-b): occurring types T1,T2 subset of B, disjoint, no G[B]-edge between."""
    types = {}
    for a in A:
        T = frozenset(w for w in G[a])
        if T:
            types.setdefault(T, []).append(a)
    out = []
    ts = list(types)
    for i in range(len(ts)):
        for j in range(i + 1, len(ts)):
            T1, T2 = ts[i], ts[j]
            if T1 & T2:
                continue
            if any(G.has_edge(u, v) for u in T1 for v in T2):
                continue
            out.append((T1, T2))
    return out


def check(G, R):
    n = G.number_of_nodes()
    if n < 3 or not nx.is_connected(G):
        return
    if nx.diameter(G) != 4:
        return
    deg = dict(G.degree())
    alpha, isets = max_ind_sets(G)
    if forest_number(G) != alpha + 1:
        return
    if G.number_of_edges() < n:                      # non-forest
        return
    tau = n - alpha
    R['hard'] += 1
    for A in isets:
        B = [v for v in G.nodes() if v not in A]
        pairs = fb_pairs(G, A, B)
        if not pairs:
            R['no_fb'] += 1
            continue
        Blo = [b for b in B if deg[b] <= tau]
        L = len(Blo)
        degA = {b: sum(1 for w in G[b] if w in A) for b in B}
        R['inst'] += 1
        R['Lhist'][(tau, L)] += 1

        for b in B:                                                     # (a1)
            if degA[b] < 1:
                R['a1'] += 1
        Bloplus = [b for b in Blo
                   if any(not G.has_edge(b, w) for w in B if w != b)]
        for b in Bloplus:                                               # (a2)
            if degA[b] < 2:
                R['a2'] += 1
        # (a3) + the MB count must hold for EVERY admissible (F-b) pair
        for T1, T2 in pairs:
            TT = set(T1) | set(T2)
            for b in Blo:
                if b in TT:
                    if degA[b] < 3:
                        R['a3deg'] += 1
                    if b not in Bloplus:
                        R['a3plus'] += 1
            c = len([b for b in Blo if b in TT])
            lhs = sum(degA[b] for b in Blo)
            if lhs < L + len(Bloplus) + c:                              # (a)
                R['MBcount'] += 1
                R.setdefault('wit', (n, sorted(G.edges()), sorted(A), tau, L,
                                     len(Bloplus), c, lhs))
            if L >= 1:
                R['MBc_slackhist'][lhs - (L + len(Bloplus) + c)] += 1


def scan_types(tau, rng, trials, R):
    """Lemma-P style bounded scan: choose G[B] and a SMALL set of occurring types.

    The A-side is kept small on purpose (at most 6 occurring types, multiplicity
    at most 2, so n <= tau + 12): the hard-core conditions are about the type
    pattern, not about how many copies of each type occur, and large n makes the
    exact alpha / f computations blow up.
    """
    Bv = list(range(tau))
    subsets = [frozenset(S) for k in range(1, tau + 1)
               for S in combinations(Bv, k)]
    for _ in range(trials):
        G = nx.Graph()
        G.add_nodes_from(Bv)
        for u, v in combinations(Bv, 2):
            if rng.random() < 0.55:
                G.add_edge(u, v)
        nxt = tau
        chosen = rng.sample(subsets, min(len(subsets), rng.randint(2, 6)))
        for T in chosen:
            for _ in range(rng.randint(1, 2)):
                for b in T:
                    G.add_edge(nxt, b)
                nxt += 1
        if G.number_of_nodes() > tau:
            check(G, R)


def main():
    rng = random.Random(31337)
    R = Counter()
    R['Lhist'] = Counter()
    R['MBc_slackhist'] = Counter()

    for G in graph_atlas_g():
        check(G, R)
    print(f"[atlas n<=7] hard-core graphs={R['hard']} (graph,A) instances={R['inst']} "
          f"fails: a1={R['a1']} a2={R['a2']} a3deg={R['a3deg']} "
          f"a3plus={R['a3plus']} MBcount={R['MBcount']}")

    for tau in range(3, 7):
        scan_types(tau, rng, 4000, R)
    print(f"[+Lemma-P type scan tau=3..6] hard-core graphs={R['hard']} "
          f"(graph,A) instances={R['inst']} fails: a1={R['a1']} a2={R['a2']} "
          f"a3deg={R['a3deg']} a3plus={R['a3plus']} MBcount={R['MBcount']}")
    print(f"[hard core (no reductio) (tau,L) histogram] "
          f"{dict(sorted(R['Lhist'].items()))}")
    print(f"[MB degree-count slack histogram] "
          f"{dict(sorted(R['MBc_slackhist'].items()))}")
    if 'wit' in R:
        print(f"WITNESS MBcount: {R['wit']}")


if __name__ == '__main__':
    main()
