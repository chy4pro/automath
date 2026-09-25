#!/usr/bin/env python3
"""Independent checker for prompts/w61_S3_GFAN_r14.md.

This file is self-contained.  It reads no repository files and implements the
Havel--Hakimi rules, partition generation, finite GFAN shape enumeration, and
small explicit graph checks directly from the review specification.
"""

from __future__ import annotations

from itertools import combinations, product
from math import ceil


def hh(values, trace=False):
    """Return (valid, steps, residue, trajectory) under Appendix A.0/C-1(4)."""
    cur = sorted(values, reverse=True)
    trajectory = [tuple(cur)]
    steps = 0
    while cur and cur[0] > 0:
        d = cur.pop(0)
        if d < 0 or d > len(cur):
            return False, None, None, trajectory
        if any(cur[i] <= 0 for i in range(d)):
            return False, None, None, trajectory
        for i in range(d):
            cur[i] -= 1
        cur.sort(reverse=True)
        steps += 1
        if trace:
            trajectory.append(tuple(cur))
    return True, steps, len(cur), trajectory


def partitions(n, max_part=None):
    """All integer partitions as nonincreasing tuples."""
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def p(n):
    return sum(1 for _ in partitions(n))


def fmt(xs):
    return "+".join(map(str, xs)) if xs else "empty"


def fan6_kills(lam):
    if not lam:
        return False
    w = lam[0]
    second = lam[1] if len(lam) > 1 else 0
    return w >= 1 and lam.count(w) == 1 and second <= w - 2


def shape_list(L, e, lam):
    c_part = [L + x for x in e] + [L] * (L + 1 - len(e))
    return c_part + list(lam)


def run_shape(L, e, lam, trace=False):
    return hh(shape_list(L, e, lam), trace=trace)


def calibrate():
    checks = []
    checks.append(("K2", hh([1, 1])[2], 1))
    for n in range(3, 10):
        checks.append((f"C{n}", hh([2] * n)[2], ceil(n / 3)))
    print("CALIBRATION (printed before all review enumeration)")
    for name, got, expected in checks:
        print(f"  residue({name}) got={got} expected={expected} pass={got == expected}")
    assert all(got == expected for _, got, expected in checks)
    print("CALIBRATION PASS")


def check_gfan2():
    print("\nGFAN2 DIRECT REFUTATION ATTEMPT")
    for L in (4, 5, 8):
        for lam in ((2, 2), (2, 1, 1), (1, 1, 1, 1)):
            valid, steps, residue, _ = run_shape(L, (), lam)
            print(f"  L={L} E=0 lambda={fmt(lam)} valid={valid} steps={steps} target={L}")
    print("  complete L=3 rows")
    rows = []
    for E in (0, 1):
        e_parts = [()] if E == 0 else list(partitions(E))
        for e in e_parts:
            for lam in partitions(4 - E):
                valid, steps, residue, _ = run_shape(3, e, lam)
                rows.append((E, e, lam, valid, steps, fan6_kills(lam)))
                print(
                    f"    E={E} e={fmt(e)} lambda={fmt(lam)} valid={valid} "
                    f"steps={steps} target=3 FAN6={fan6_kills(lam)}"
                )
    assert len(rows) == 8
    survivors = [row for row in rows if row[3] and row[4] == 3]
    assert survivors and all(fan6_kills(row[2]) for row in survivors)
    print(f"  generated_rows={len(rows)} exact-step_survivors={len(survivors)} un-killed=0")


def enumerate_all():
    print("\nGFANnu FINITE ENUMERATION (generated without printed data)")
    all_e_shapes = []
    total_survivors = []
    for nu in range(1, 7):
        s0_rows = []
        tail_survivors = []
        for lam in partitions(2 * nu):
            valid, s0, residue, _ = hh([lam[0]] * (lam[0] + 1) + list(lam))
            assert valid
            s0_rows.append((lam, s0))
            if s0 == lam[0]:
                tail_survivors.append(lam)
        print(
            f"  nu={nu} s0_rows={len(s0_rows)} values="
            + " | ".join(f"{fmt(lam)}:{s0}" for lam, s0 in s0_rows)
        )
        print(
            f"    tail_exact={len(tail_survivors)} "
            f"tail_survivors={','.join(fmt(x) for x in tail_survivors) or 'none'} "
            f"un-killed={sum(not fan6_kills(x) for x in tail_survivors)}"
        )

        boundary_pairs = []
        boundary_survivors = []
        for lam in partitions(2 * nu):
            for L in range(nu + 1, lam[0]):
                valid, steps, residue, _ = run_shape(L, (), lam)
                boundary_pairs.append((L, lam))
                if valid and steps == L:
                    boundary_survivors.append((L, lam))
        print(
            f"    boundary_pairs={len(boundary_pairs)} survivors="
            + (", ".join(f"L{L}/lambda={fmt(lam)}" for L, lam in boundary_survivors) or "none")
        )
        print(
            f"    boundary_survivor_count={len(boundary_survivors)} "
            f"un-killed={sum(not fan6_kills(lam) for _, lam in boundary_survivors)}"
        )

        tested = []
        survivors = []
        per_e = {}
        for E in range(1, nu):
            per_e[E] = 0
            for L in range(nu + 1, 2 * nu - E + 1):
                for e in partitions(E):
                    assert len(e) <= L + 1
                    for lam in partitions(2 * nu - E):
                        row = (nu, L, E, e, lam)
                        tested.append(row)
                        all_e_shapes.append(row)
                        per_e[E] += 1
                        valid, steps, residue, _ = run_shape(L, e, lam)
                        if valid and steps == L:
                            survivors.append(row)
                            total_survivors.append(row)
        closed_terms = [
            (nu - E) * p(E) * p(2 * nu - E) for E in range(1, nu)
        ]
        closed = sum(closed_terms)
        assert closed == len(tested)
        print(
            f"    Epositive tested={len(tested)} closed_form={closed} "
            f"terms={closed_terms or []} per_E={per_e}"
        )
        print(
            f"    Epositive survivors={len(survivors)} "
            f"un-killed={sum(not fan6_kills(row[4]) for row in survivors)}"
        )
        for _, L, E, e, lam in survivors:
            second = lam[1] if len(lam) > 1 else 0
            print(
                f"      L{L} E{E} e={fmt(e)} lambda={fmt(lam)} "
                f"cert=({lam[0]},{second}) kill={fan6_kills(lam)}"
            )
    print(
        f"  TOTAL Epositive tested={len(all_e_shapes)} "
        f"survivors={len(total_survivors)} un-killed="
        f"{sum(not fan6_kills(row[4]) for row in total_survivors)}"
    )
    return all_e_shapes


def controls(all_e_shapes):
    print("\nSPECIFICATION CONTROLS")
    tail_pairs = 0
    tail_mismatches = []
    for nu in range(1, 7):
        for lam in partitions(2 * nu):
            valid0, s0, _, _ = hh([lam[0]] * (lam[0] + 1) + list(lam))
            assert valid0
            for L in range(lam[0], 16):
                tail_pairs += 1
                valid, steps, _, _ = run_shape(L, (), lam)
                predicted = (L - lam[0]) + s0
                if not valid or steps != predicted:
                    tail_mismatches.append((nu, L, lam, valid, steps, predicted))
    print(f"  TAIL direct_pairs={tail_pairs} mismatches={len(tail_mismatches)}")

    bases = []
    for nu in range(1, 7):
        for lam in partitions(2 * nu):
            # The canonical s0 list is a separate E=0 control row.
            bases.append([lam[0]] * (lam[0] + 1) + list(lam))
            for L in range(nu + 1, max(2 * nu, lam[0]) + 1):
                bases.append(shape_list(L, (), lam))
    for _, L, _, e, lam in all_e_shapes:
        bases.append(shape_list(L, e, lam))
    pads = (0, 1, 2, 3, 4, 8, 13)
    padding_mismatches = []
    for base in bases:
        # C-1(2) claims validity/step-count inertness, not equality of the
        # terminal number of zeros (which naturally grows under padding).
        outcomes = [(hh(base + [0] * z)[0:2]) for z in pads]
        if len(set(outcomes)) != 1:
            padding_mismatches.append((base, outcomes))
    print(
        f"  zero-padding base_lists={len(bases)} paddings={len(pads)} "
        f"pairs={len(bases) * len(pads)} mismatches={len(padding_mismatches)}"
    )

    print("  empty-residue boundary")
    for L in range(1, 7):
        valid, steps, residue, _ = run_shape(L, (), ())
        print(f"    L={L} valid={valid} steps={steps} residue={residue}")
    print("  single-part FAN-6 convention")
    for w in range(1, 7):
        print(f"    lambda=[{w}] second=0 kill={fan6_kills((w,))}")


def graph_from_edges(names, edge_pairs):
    index = {name: i for i, name in enumerate(names)}
    adj = [set() for _ in names]
    for x, y in edge_pairs:
        i, j = index[x], index[y]
        assert i != j
        adj[i].add(j)
        adj[j].add(i)
    return adj


def connected(adj):
    if not adj:
        return True
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u] - seen:
            seen.add(v)
            stack.append(v)
    return len(seen) == len(adj)


def independent(adj, subset):
    chosen = set(subset)
    return all(not (adj[u] & chosen) for u in chosen)


def maximum_independent(adj):
    n = len(adj)
    best = ()
    for mask in range(1 << n):
        if bin(mask).count("1") <= len(best):
            continue
        subset = tuple(i for i in range(n) if mask & (1 << i))
        if independent(adj, subset):
            best = subset
    return best


def diameter(adj):
    if not connected(adj):
        return None
    ans = 0
    for root in range(len(adj)):
        dist = {root: 0}
        queue = [root]
        for u in queue:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        ans = max(ans, max(dist.values()))
    return ans


def induced_is_forest(adj, subset):
    chosen = set(subset)
    parent = {u: u for u in chosen}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u in chosen:
        for v in adj[u]:
            if v in chosen and u < v:
                ru, rv = find(u), find(v)
                if ru == rv:
                    return False
                parent[ru] = rv
    return True


def forest_number(adj):
    n = len(adj)
    best = 0
    for mask in range(1 << n):
        if bin(mask).count("1") <= best:
            continue
        subset = tuple(i for i in range(n) if mask & (1 << i))
        if induced_is_forest(adj, subset):
            best = len(subset)
    return best


def edge_list(names, adj):
    return [(names[u], names[v]) for u in range(len(adj)) for v in adj[u] if u < v]


def verify_gfan(names, adj, A_names, low_names, high_names):
    ix = {x: i for i, x in enumerate(names)}
    A = {ix[x] for x in A_names}
    low = {ix[x] for x in low_names}
    high = {ix[x] for x in high_names}
    B = low | high
    tau = len(B)
    a0_candidates = [a for a in A if B <= adj[a]]
    low_universal = all((B - {b}) <= adj[b] for b in low)
    low_dega_one = all(len(adj[b] & A) == 1 for b in low)
    common = len(a0_candidates) == 1 and all((adj[b] & A) == set(a0_candidates) for b in low)
    nonedges = [(u, v) for u, v in combinations(B, 2) if v not in adj[u]]
    nonedges_high = all(u in high and v in high for u, v in nonedges)
    high_condition = all(len(adj[w]) >= tau + 1 for w in high)
    low_condition = all(len(adj[b]) <= tau for b in low)
    no_aprime_low = bool(a0_candidates) and all(
        not (adj[a] & low) for a in A - set(a0_candidates)
    )
    return {
        "tau": tau,
        "L": len(low),
        "nu": len(nonedges),
        "low_universal": low_universal,
        "low_degA_1": low_dega_one,
        "common_a0_allB": common,
        "nonedges_inside_high": nonedges_high,
        "high_condition": high_condition,
        "low_condition": low_condition,
        "no_Aprime_low": no_aprime_low,
        "all": all((low_universal, low_dega_one, common, nonedges_high,
                    high_condition, low_condition, no_aprime_low)),
    }


def print_graph_witness(label, names, adj, A_names, low_names, high_names):
    ix = {x: i for i, x in enumerate(names)}
    A = tuple(ix[x] for x in A_names)
    max_A = maximum_independent(adj)
    alpha = len(max_A)
    f = forest_number(adj)
    degs = [len(x) for x in adj]
    valid, steps, residue, _ = hh(degs)
    print(f"  {label}")
    print(f"    vertices={names}")
    print(f"    edges={edge_list(names, adj)}")
    print(f"    connected={connected(adj)}")
    print(
        f"    A={list(A_names)} independent={independent(adj, A)} "
        f"maximum_by_exhaustive_enumeration={len(A) == alpha} alpha={alpha} "
        f"one_maximum={[names[i] for i in max_A]}"
    )
    print(f"    diameter={diameter(adj)}")
    print(f"    forest_number={f} f_eq_alpha_plus_1={f == alpha + 1}")
    print(f"    nonforest={not induced_is_forest(adj, range(len(adj)))}")
    print(
        f"    degrees={degs} HH_valid={valid} HH_steps={steps} "
        f"residue={residue} residue_eq_alpha={residue == alpha}"
    )
    print(f"    GFan_check={verify_gfan(names, adj, A_names, low_names, high_names)}")


def construct_graphs():
    print("\nCONSTRUCTION AND QUANTIFIER CONTROLS")

    # nu=0 boundary: K5, with B of size four and A={a0}.
    names = ["a0", "b0", "b1", "b2", "b3"]
    edges = list(combinations(names, 2))
    adj = graph_from_edges(names, edges)
    print_graph_witness(
        "nu=0 extension counterexample: K5 as GFan(4,4,0)",
        names, adj, ["a0"], ["b0", "b1", "b2", "b3"], []
    )

    # A genuine GFan-shaped graph at nu=2 which deliberately fails the reductio.
    names = ["a0", "x1", "x2", "x3", "x4", "b0", "b1", "b2", "h0", "h1", "h2"]
    edges = []
    B = ["b0", "b1", "b2", "h0", "h1", "h2"]
    missing = {frozenset(("h0", "h1")), frozenset(("h0", "h2"))}
    for u, v in combinations(B, 2):
        if frozenset((u, v)) not in missing:
            edges.append((u, v))
    edges += [("a0", b) for b in B]
    edges += [("x1", h) for h in ("h0", "h1", "h2")]
    edges += [("x2", h) for h in ("h0", "h2")]
    edges += [("x3", "h0")]
    edges += [("x4", "h1")]
    adj = graph_from_edges(names, edges)
    print_graph_witness(
        "counterfactual GFan(6,3,2) violating residue=alpha",
        names, adj, ["a0", "x1", "x2", "x3", "x4"],
        ["b0", "b1", "b2"], ["h0", "h1", "h2"]
    )

    print("  boundary search for GFan(*,L,2), L in {1,2}")
    for L in (1, 2):
        found = None
        checked = 0
        p_high = 3
        B = [f"b{i}" for i in range(L)] + [f"h{i}" for i in range(p_high)]
        high = [f"h{i}" for i in range(p_high)]
        for missing_pairs in combinations(list(combinations(high, 2)), 2):
            missing = {frozenset(x) for x in missing_pairs}
            for k in (3, 4):
                Aprime = [f"x{i}" for i in range(k)]
                for cols in product(range(1, 1 << p_high), repeat=k):
                    checked += 1
                    row_counts = [sum(bool(mask & (1 << i)) for mask in cols) for i in range(p_high)]
                    miss_counts = [sum(frozenset((high[i], other)) in missing for other in high if other != high[i]) for i in range(p_high)]
                    if any(row_counts[i] < 1 + miss_counts[i] for i in range(p_high)):
                        continue
                    names = ["a0"] + Aprime + B
                    edges = []
                    for u, v in combinations(B, 2):
                        if frozenset((u, v)) not in missing:
                            edges.append((u, v))
                    edges += [("a0", b) for b in B]
                    for j, mask in enumerate(cols):
                        for i, h in enumerate(high):
                            if mask & (1 << i):
                                edges.append((Aprime[j], h))
                    adj = graph_from_edges(names, edges)
                    ix = {x: i for i, x in enumerate(names)}
                    Aidx = tuple(ix[x] for x in ["a0"] + Aprime)
                    maxA = maximum_independent(adj)
                    residue = hh([len(x) for x in adj])[2]
                    gf = verify_gfan(names, adj, ["a0"] + Aprime, B[:L], high)
                    if gf["all"] and len(Aidx) == len(maxA) and residue == len(Aidx):
                        found = (names, adj, ["a0"] + Aprime, B[:L], high)
                        break
                if found:
                    break
            if found:
                break
        print(f"    L={L} candidates_checked={checked} found={found is not None}")
        if found:
            print_graph_witness(f"L={L} boundary witness", *found)
        else:
            print("      no instance found in p=3, |A'| in {3,4} search box")


def main():
    calibrate()
    check_gfan2()
    shapes = enumerate_all()
    controls(shapes)
    construct_graphs()
    print("\nCHECKER VERDICT: finite GFAN2/GFANnu shape searches found no un-killed survivor.")


if __name__ == "__main__":
    main()
