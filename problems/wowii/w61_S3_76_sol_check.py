#!/usr/bin/env python3
"""Independent checks for prompts/w61_S3_76_sol.md.

This file intentionally does not import or read any project verification artifact.
"""

from __future__ import annotations

import itertools
import json
import math
import random
from collections import Counter, defaultdict

import networkx as nx


SEED = 0x6176
RNG = random.Random(SEED)


def residue_seq(seq):
    """Literal residueAux-style recursion: sort, splitAt truncation, Nat subtraction."""
    work = sorted((int(x) for x in seq), reverse=True)
    steps = []
    while work:
        if work[0] == 0:
            return len(work), steps
        d, tail = work[0], work[1:]
        left, right = tail[:d], tail[d:]
        work = sorted([max(0, x - 1) for x in left] + right, reverse=True)
        steps.append(d)
    return 0, steps


def labelled_hh(G, tie_seed=None):
    """Labelled HH, with a fresh random tie order at every step when seeded."""
    values = {v: G.degree(v) for v in G.nodes()}
    rng = random.Random(tie_seed) if tie_seed is not None else None
    heads, D, blocks, starts = [], [], [], []
    while values and max(values.values()) > 0:
        groups = defaultdict(list)
        for v, x in values.items():
            groups[x].append(v)
        order = []
        for x in sorted(groups, reverse=True):
            group = sorted(groups[x], key=repr)
            if rng is not None:
                rng.shuffle(group)
            order.extend(group)
        head = order[0]
        d = values[head]
        assert d <= len(order) - 1, ("nongraphical labelled state", values, order)
        block = order[1 : 1 + d]
        starts.append(dict(values))
        heads.append(head)
        D.append(d)
        blocks.append(tuple(block))
        del values[head]
        for v in block:
            values[v] -= 1
            assert values[v] >= 0
    return {"heads": heads, "D": D, "blocks": blocks, "starts": starts,
            "survivors": set(values)}


def adjacency_masks(G):
    nodes = tuple(sorted(G.nodes(), key=repr))
    idx = {v: i for i, v in enumerate(nodes)}
    masks = [0] * len(nodes)
    for u, v in G.edges():
        i, j = idx[u], idx[v]
        masks[i] |= 1 << j
        masks[j] |= 1 << i
    return nodes, masks


def maximum_independent_sets(G):
    nodes, adj = adjacency_masks(G)
    n = len(nodes)
    best, answers = -1, []
    for mask in range(1 << n):
        size = bin(mask).count("1")
        if size < best:
            continue
        ok = True
        for i in range(n):
            if mask >> i & 1 and adj[i] & mask:
                ok = False
                break
        if ok:
            chosen = frozenset(nodes[i] for i in range(n) if mask >> i & 1)
            if size > best:
                best, answers = size, [chosen]
            else:
                answers.append(chosen)
    return best, answers


def forest_number(G):
    nodes = tuple(G.nodes())
    for size in range(len(nodes), -1, -1):
        for S in itertools.combinations(nodes, size):
            if nx.is_forest(G.subgraph(S)):
                return size
    raise AssertionError


def edge_list(G):
    return sorted((min(u, v), max(u, v)) for u, v in G.edges())


def diameter_if_connected(G):
    return nx.diameter(G) if len(G) and nx.is_connected(G) else None


def type_pairs(G, A, B):
    types = sorted({frozenset(set(G.neighbors(a)) & B) for a in A},
                   key=lambda T: (len(T), tuple(sorted(T, key=repr))))
    pairs = []
    for i, T1 in enumerate(types):
        for T2 in types[i + 1:]:
            if not T1 or not T2 or T1 & T2:
                continue
            if all(not G.has_edge(u, v) for u in T1 for v in T2):
                pairs.append((T1, T2))
    return types, pairs


def choose_ties(G):
    # Canonical plus five independent, deterministic randomised adversarial orders.
    signature = sum((u + 1) * (v + 3) for u, v in edge_list(G)) + 1009 * len(G)
    return [None] + [SEED + signature + 7919 * k for k in range(5)]


stats = Counter()
failures = []
boundaries = {}
controls = {}
frame_examples = []
hardcore_examples = []


def remember(name, payload):
    boundaries.setdefault(name, payload)


def fail(label, payload):
    failures.append({"label": label, **payload})


def check_graph(G, source):
    G = nx.convert_node_labels_to_integers(G, ordering="sorted")
    n = len(G)
    if n < 2:
        return
    stats["graphs"] += 1
    connected = nx.is_connected(G)
    if connected:
        stats["connected"] += 1
    alpha, As = maximum_independent_sets(G)
    f = forest_number(G) if connected else None
    diam = diameter_if_connected(G)
    residue, seq_heads = residue_seq([G.degree(v) for v in G])
    if residue != n - len(seq_heads):
        fail("residue=n-s", {"source": source, "edges": edge_list(G)})
    frame = connected and not nx.is_forest(G) and diam == 4 and f == alpha + 1
    if frame:
        stats["frame_graphs"] += 1
    reductio = residue == alpha
    if reductio:
        stats["reductio_graphs"] += 1
    if frame and reductio:
        stats["hardcore_graphs"] += 1
        hardcore_examples.append((G.copy(), alpha, f, residue))

    for A in As:
        stats["maximum_independent_sets"] += 1
        B = set(G) - set(A)
        tau = len(B)
        eB = G.subgraph(B).number_of_edges()
        nu = math.comb(tau, 2) - eB
        types, pairs = type_pairs(G, A, B) if connected else ([], [])

        # Structural controls for the hard-core frame, independent of reductio.
        if frame:
            stats["frame_A"] += 1
            # Lemma 4 at its stated call form.
            for u, v in itertools.combinations(B, 2):
                common = (set(G.neighbors(u)) & set(G.neighbors(v)) & set(A))
                floor = 1 if G.has_edge(u, v) else 2
                if len(common) < floor:
                    fail("Lemma4-call", {"edges": edge_list(G), "A": sorted(A),
                                          "pair": [u, v], "common": len(common)})
            if nu < 1:
                fail("R1", {"edges": edge_list(G), "A": sorted(A)})
            if not pairs:
                fail("F-b", {"edges": edge_list(G), "A": sorted(A)})
            for T1, T2 in pairs:
                for b in T1 | T2:
                    degA = len(set(G.neighbors(b)) & set(A))
                    if degA < 3:
                        fail("Cstar", {"edges": edge_list(G), "A": sorted(A),
                                       "T1": sorted(T1), "T2": sorted(T2), "b": b})

                Blo = {b for b in B if G.degree(b) <= tau}
                Bhi = B - Blo
                L = len(Blo)
                plus = {b for b in Blo if any(c != b and not G.has_edge(b, c) for c in B)}
                c = len(Blo & (set(T1) | set(T2)))
                degree_sum = sum(len(set(G.neighbors(b)) & set(A)) for b in Blo)
                if degree_sum < L + len(plus) + c:
                    fail("MB-degree-count", {"edges": edge_list(G), "A": sorted(A),
                                               "T1": sorted(T1), "T2": sorted(T2)})
                stats["MB_degree_count_instances"] += 1
                stats[f"MB_degree_slack_{degree_sum - L - len(plus) - c}"] += 1

            if not frame_examples:
                frame_examples.append((G.copy(), A, f, residue, types, pairs))

        if not reductio:
            continue

        stats["reductio_A"] += 1
        for tie in choose_ties(G):
            tr = labelled_hh(G, tie)
            stats["trajectories"] += 1
            if len(tr["heads"]) != tau:
                fail("s=tau", {"edges": edge_list(G), "A": sorted(A), "tie": tie,
                                "s": len(tr["heads"]), "tau": tau})
                continue
            if sum(tr["D"]) != G.number_of_edges():
                fail("sumD=m", {"edges": edge_list(G), "tie": tie})

            Bhi = {b for b in B if G.degree(b) >= tau + 1}
            Blo = B - Bhi
            L, p = len(Blo), len(Bhi)
            Ihi = {i for i, h in enumerate(tr["heads"], start=1)
                   if G.degree(h) >= tau + 1}
            actual_hi = {tr["heads"][i - 1] for i in Ihi}
            if actual_hi != Bhi or len(Ihi) != p or tau - len(Ihi) != L:
                fail("HI", {"edges": edge_list(G), "A": sorted(A), "tie": tie,
                             "Bhi": sorted(Bhi), "actual_hi": sorted(actual_hi)})

            sumdeglo = sum(G.degree(b) for b in Blo)
            nulo = sum(1 for u, v in itertools.combinations(Blo, 2) if not G.has_edge(u, v))
            mbar = sum(1 for u, v in itertools.combinations(Bhi, 2) if not G.has_edge(u, v))
            elo = G.subgraph(Blo).number_of_edges()
            degAlo = sum(len(set(G.neighbors(b)) & set(A)) for b in Blo)
            low1_lhs, low1_rhs = sumdeglo + nu, L * (tau + 1)
            if low1_lhs > low1_rhs:
                fail("LOW1", {"edges": edge_list(G), "A": sorted(A), "tie": tie})
            if degAlo + elo + mbar > L * (L + 3) // 2:
                fail("LOW2", {"edges": edge_list(G), "A": sorted(A), "tie": tie})
            if degAlo + mbar > 2 * L + nulo:
                fail("LOW3", {"edges": edge_list(G), "A": sorted(A), "tie": tie})
            pos_rhs = (-sum(range(tau)) + L * (tau + 1))
            calc_rhs = (-sum(i - 1 for i in Ihi)
                        + sum(tau - i + 2 for i in range(1, tau + 1) if i not in Ihi))
            if calc_rhs != pos_rhs:
                fail("LOW-position-collapse", {"tau": tau, "Ihi": sorted(Ihi)})

            slack = low1_rhs - low1_lhs
            stats[f"slack_L{L}_{slack}"] += 1
            if tau >= 2 and L >= 1 and slack < 1:
                fail("SL", {"edges": edge_list(G), "A": sorted(A), "tie": tie,
                             "tau": tau, "L": L, "slack": slack})

            plus = {b for b in Blo if any(c != b and not G.has_edge(b, c) for c in B)}
            payload = {"source": source, "n": n, "edges": edge_list(G),
                       "A": sorted(A), "tie": tie, "tau": tau,
                       "L": L, "p": p, "nu": nu, "slack": slack,
                       "Delta": max(dict(G.degree()).values())}
            remember(f"L={L}", payload)
            if L == 0 and tau >= 1:
                remember("L=0_positive_tau", payload)
            if L == 1 and tau >= 2:
                remember("L=1_tau_ge_2", payload)
            if L == tau and tau >= 2:
                remember("p=0", payload)
            if nu in (0, 1):
                remember(f"nu={nu}", payload)
            if max(dict(G.degree()).values()) == tau:
                remember("Delta=tau", payload)
            if max(dict(G.degree()).values()) == tau + 1:
                remember("Delta=tau+1", payload)
            remember("B_lo_plus=empty" if not plus else "B_lo_plus=nonempty",
                     payload)
            if tau in (2, 3, 4):
                remember(f"tau={tau}", payload)
            low_positions = [i for i in range(1, tau + 1) if i not in Ihi]
            if low_positions:
                i0 = max(low_positions)
                if i0 in (1, tau):
                    remember(f"i0={i0}" if i0 == 1 else "i0=tau", payload)

            if frame:
                # All composite hard-core claims, for every admissible F-b pair.
                for T1, T2 in pairs:
                    c = len(Blo & (set(T1) | set(T2)))
                    mb_lhs = len(plus) + c + mbar
                    mb_rhs = L + nulo - 1
                    if L >= 1 and mb_lhs > mb_rhs:
                        fail("MB", {"edges": edge_list(G), "A": sorted(A), "tie": tie})
                    if L == 1:
                        fail("L1-short/SL-HC", {"edges": edge_list(G), "A": sorted(A)})
                    if all(b not in plus for b in Blo):
                        if not (nu == mbar <= L - 1 and L >= nu + 1 >= 2):
                            fail("MB1", {"edges": edge_list(G), "A": sorted(A)})
                    if L == 2:
                        b1, b2 = sorted(Blo)
                        commonA = set(G.neighbors(b1)) & set(G.neighbors(b2)) & set(A)
                        conclusions = [
                            G.has_edge(b1, b2), not plus,
                            len(set(G.neighbors(b1)) & set(A)) == 1,
                            len(set(G.neighbors(b2)) & set(A)) == 1,
                            len(commonA) == 1,
                            nu == mbar == 1,
                            slack == 1,
                        ]
                        if not all(conclusions):
                            fail("L2", {"edges": edge_list(G), "A": sorted(A),
                                        "checks": conclusions})


def add_random_graphs():
    for n in (8, 9, 10):
        for p in (0.18, 0.35, 0.55, 0.78):
            for k in range(18):
                seed = SEED + n * 10000 + int(p * 1000) * 10 + k
                G = nx.gnp_random_graph(n, p, seed=seed)
                check_graph(G, f"Gnp(n={n},p={p},k={k})")


def calibrate():
    rows = []
    K2 = nx.complete_graph(2)
    rows.append(("K2", residue_seq([d for _, d in K2.degree()])[0], 1))
    for n in range(3, 10):
        C = nx.cycle_graph(n)
        rows.append((f"C{n}", residue_seq([d for _, d in C.degree()])[0], math.ceil(n / 3)))
    assert all(got == want for _, got, want in rows)
    return rows


def process_controls():
    cases = {
        "disconnected_2K2": nx.disjoint_union(nx.path_graph(2), nx.path_graph(2)),
        "edgeless4": nx.empty_graph(4),
    }
    out = {}
    for name, G in cases.items():
        r, heads = residue_seq([d for _, d in G.degree()])
        out[name] = {"degrees": sorted((d for _, d in G.degree()), reverse=True),
                     "residue": r, "heads": heads}
    for seq in ([3, 3, 1], [5, 1], [4, 4, 1, 0]):
        r, heads = residue_seq(seq)
        out[f"nongraphical_{seq}"] = {"residue": r, "heads": heads}
    return out


def main():
    calibration = calibrate()
    # Complete unlabeled atlas box: every graph on 2..7 vertices, connected or not.
    for i, G in enumerate(nx.graph_atlas_g()):
        if 2 <= len(G) <= 7:
            check_graph(G, f"atlas[{i}]")
    add_random_graphs()

    # Ensure requested L=tau boundary appears explicitly via cycles and cliques.
    for n in range(3, 10):
        check_graph(nx.cycle_graph(n), f"cycle{n}")
    for n in range(2, 8):
        check_graph(nx.complete_graph(n), f"clique{n}")

    if frame_examples:
        G, A, f, residue, types, pairs = frame_examples[0]
        controls["hard_core_frame"] = {
            "edges": edge_list(G), "A": sorted(A), "alpha": len(A), "f": f,
            "residue": residue, "diameter": nx.diameter(G),
            "nonforest": not nx.is_forest(G),
            "F_b_pairs": [[sorted(x), sorted(y)] for x, y in pairs],
        }
    # C5 is the advertised reductio-only control.
    C5 = nx.cycle_graph(5)
    a5, A5s = maximum_independent_sets(C5)
    controls["reductio_only_C5"] = {
        "edges": edge_list(C5), "A_examples": [sorted(A) for A in A5s],
        "alpha": a5, "residue": residue_seq([2] * 5)[0],
        "diameter": nx.diameter(C5), "f": forest_number(C5),
    }

    print("CALIBRATION")
    for name, got, want in calibration:
        print(f"  {name}: residue={got}, expected={want}, ok={got == want}")
    print("SEARCH BOX")
    print("  atlas: every unlabeled graph on 2..7 vertices (connected and disconnected)")
    print("  random: n=8..10, p in {0.18,0.35,0.55,0.78}, 18 seeds each")
    print("  A: every maximum independent set; ties: canonical + five random orders")
    print("COUNTS")
    print(json.dumps(dict(sorted(stats.items())), indent=2, sort_keys=True))
    print("BOUNDARIES")
    print(json.dumps(boundaries, indent=2, sort_keys=True))
    print("CONTROLS")
    print(json.dumps(controls, indent=2, sort_keys=True))
    print("PROCESS EDGE CASES")
    print(json.dumps(process_controls(), indent=2, sort_keys=True))
    print("FAILURES")
    print(json.dumps(failures[:25], indent=2, sort_keys=True))
    print(f"FAILURE_COUNT={len(failures)}")


if __name__ == "__main__":
    main()
