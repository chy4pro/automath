#!/usr/bin/env python3
"""
WOWII-61: does the hard-core frame force an *occurring singleton type*?

Fact F-b as drafted read:

    "In the hard-core frame there exist occurring types T1, T2 that are disjoint
     and have no G[B]-edge between them.  In particular a singleton type occurs."

The first sentence is what the displayed proof establishes (diam = 4 is realised
by a pair a, a' in A with N(a) cap N(a') = empty and no G[B]-edge between them).
The second sentence does not follow, and this script measures how often it fails.

  frame:  G connected, non-forest, diam(G) = 4, f(G) = alpha(G) + 1.
  A a maximum independent set, B = V \\ A,
  occurring type: T = N(a) subset of B for some a in A.

Part 1 re-checks the explicit 8-vertex instance reported by the cross-family
verifier.  Part 2 scans the same corpus w61_cstar.py uses -- the exhaustive
n <= 7 atlas plus the n = 8 cover -- and reports, with its population:

  * frame graphs seen                                   (population)
  * (graph, A) pairs seen                               (population)
  * (graph, A) pairs with NO occurring singleton type   (clause counterexamples)
  * frame graphs for which NO choice of maximum independent set A yields an
    occurring singleton type                            (strong counterexamples)

Run: python3 w61_fb_singleton.py     (needs networkx for the n <= 7 atlas)
"""
import itertools
from collections import Counter

from w61_cstar import (adj_masks, is_connected, diameter, alpha_sets,
                       largest_forest)

# The instance reported by the cross-family verifier, as an edge list.
NOTE_EDGES = [(0, 1), (0, 5), (0, 6), (1, 2), (1, 4), (2, 3), (2, 5),
              (3, 4), (4, 5), (7, 0), (7, 1), (7, 5), (7, 6)]
NOTE_N = 8
NOTE_A = frozenset({1, 3, 5, 6})


def types_of(a, n, S):
    """occurring types (with multiplicity) for independent set S; B = complement."""
    B = [v for v in range(n) if not (S >> v & 1)]
    mu = Counter()
    for v in range(n):
        if S >> v & 1:
            mu[frozenset(w for w in B if a[v] >> w & 1)] += 1
    return B, mu


def fb_pairs(a, mu):
    """disjoint occurring type pairs with no G[B]-edge between them."""
    out = []
    for T1, T2 in itertools.combinations([T for T in mu if mu[T] > 0], 2):
        if T1 & T2:
            continue
        if any(a[u] >> w & 1 for u in T1 for w in T2):
            continue
        out.append((T1, T2))
    return out


def part1():
    a = adj_masks(NOTE_N, NOTE_EDGES)
    n = NOTE_N
    conn = is_connected(a, n)
    d = diameter(a, n)
    al, isets = alpha_sets(a, n)
    f = largest_forest(a, n)
    print("[F-b/1] reported instance E =", sorted(NOTE_EDGES))
    print(f"[F-b/1] n={n} connected={conn} diam={d} alpha={al} f={f} "
          f"forest={f == n} tau={n - al}")
    in_frame = conn and d == 4 and f == al + 1 and f != n
    print(f"[F-b/1] in hard-core frame: {in_frame}")
    S = 0
    for v in NOTE_A:
        S |= 1 << v
    print(f"[F-b/1] A={sorted(NOTE_A)} is a maximum independent set: "
          f"{S in isets} (|A|={bin(S).count('1')}, alpha={al})")
    B, mu = types_of(a, n, S)
    print(f"[F-b/1] B={B}")
    print("[F-b/1] occurring types (with multiplicity):",
          sorted((sorted(T), m) for T, m in mu.items()))
    pairs = fb_pairs(a, mu)
    print("[F-b/1] disjoint no-G[B]-edge type pairs:",
          [(sorted(T1), sorted(T2)) for T1, T2 in pairs])
    singles = [sorted(T) for T in mu if len(T) == 1 and mu[T] > 0]
    print(f"[F-b/1] occurring singleton types: {singles}")
    print(f"[F-b/1] VERDICT: F-b main clause holds ({len(pairs)} witness pair(s)); "
          f"'in particular a singleton type occurs' is "
          f"{'TRUE' if singles else 'FALSE'} here.")
    return in_frame and bool(pairs) and not singles


class Acc:
    def __init__(self):
        self.frames = 0
        self.ga_pairs = 0
        self.ga_no_singleton = 0
        self.frames_no_singleton_any_A = 0
        self.first_witness = None


def scan(n, edges, acc):
    a = adj_masks(n, edges)
    if not is_connected(a, n):
        return
    if diameter(a, n) != 4:
        return
    al, isets = alpha_sets(a, n)
    f = largest_forest(a, n)
    if f != al + 1 or f == n:
        return
    acc.frames += 1
    any_A_has_singleton = False
    for S in isets:
        acc.ga_pairs += 1
        _, mu = types_of(a, n, S)
        has_singleton = any(len(T) == 1 and mu[T] > 0 for T in mu)
        if has_singleton:
            any_A_has_singleton = True
        else:
            acc.ga_no_singleton += 1
            if acc.first_witness is None and fb_pairs(a, mu):
                acc.first_witness = (
                    n, sorted(edges), sorted(v for v in range(n) if S >> v & 1),
                    sorted((sorted(T), m) for T, m in mu.items()))
    if not any_A_has_singleton:
        acc.frames_no_singleton_any_A += 1


def part2():
    import networkx as nx
    from networkx.generators.atlas import graph_atlas_g
    acc = Acc()
    small = []
    for G in graph_atlas_g():
        if G.number_of_nodes() < 2 or not nx.is_connected(G):
            continue
        small.append((G.number_of_nodes(), [(u, v) for u, v in G.edges()]))
    for n, e in small:
        scan(n, e, acc)
    print(f"[F-b/2 n<=7 exhaustive] frame graphs={acc.frames} "
          f"(graph,A) pairs={acc.ga_pairs} "
          f"(graph,A) with no occurring singleton type={acc.ga_no_singleton} "
          f"frame graphs with no singleton for ANY A={acc.frames_no_singleton_any_A}")
    for n, edges in small:
        if n != 7:
            continue
        for mask in range(1, 1 << 7):
            e2 = list(edges) + [(7, v) for v in range(7) if mask >> v & 1]
            scan(8, e2, acc)
    print(f"[F-b/2 +n=8 cover]      frame graphs={acc.frames} "
          f"(graph,A) pairs={acc.ga_pairs} "
          f"(graph,A) with no occurring singleton type={acc.ga_no_singleton} "
          f"frame graphs with no singleton for ANY A={acc.frames_no_singleton_any_A}")
    if acc.first_witness:
        print("[F-b/2] first witness (n, edges, A, types):", acc.first_witness)


def main():
    ok = part1()
    print()
    part2()
    print()
    print(f"[F-b] singleton clause refuted by the reported instance: {ok}")


if __name__ == "__main__":
    main()
