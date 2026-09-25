#!/usr/bin/env python3
"""Independent checker for the review specified by prompts/w61_S3_GFAN_sol.md.

This program is self-contained.  It does not read repository files.  Its stdout is
the raw checker record requested by the review brief.
"""

from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import ceil


def hh_run(values, trace=False):
    """Return (steps, residue, valid, trace).

    At each positive step, delete the largest value d and subtract one from the
    next d largest values.  A negative value (including decrementing a zero) or
    too few remaining entries makes the sequence invalid.  For a valid run,
    residue is the number of zero entries left.
    """
    a = list(values)
    history = []
    steps = 0
    while True:
        a.sort(reverse=True)
        if trace:
            history.append(tuple(a))
        if not a or a[0] == 0:
            return steps, len(a), True, history
        d = a.pop(0)
        if d < 0 or d > len(a):
            return None, None, False, history
        for i in range(d):
            a[i] -= 1
            if a[i] < 0:
                return None, None, False, history
        steps += 1


def hh_steps(values):
    steps, _, valid, _ = hh_run(values)
    return steps if valid else None


def hh_residue(values):
    _, residue, valid, _ = hh_run(values)
    return residue if valid else None


def partitions(n, cap=None):
    """All integer partitions of n as nonincreasing positive tuples."""
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def fan6_certificate(lam):
    """Return (killed, maximum, second), with an implicit zero after one part."""
    w = lam[0]
    unique = len(lam) == 1 or lam[1] < w
    second = lam[1] if len(lam) >= 2 else 0
    return unique and w >= 1 and second <= w - 2, w, second


def c_part(L, e):
    return tuple(sorted([L + x for x in e] + [L] * (L + 1 - len(e)), reverse=True))


def fmt(part):
    return "+".join(map(str, part)) if part else "(empty)"


def cycle_degrees(n):
    return [2] * n


def print_calibration():
    print("=== CALIBRATION (printed before all review numbers) ===")
    k2 = hh_residue([1, 1])
    print(f"K2 residue: computed={k2} expected=1 pass={k2 == 1}")
    all_ok = k2 == 1
    for n in range(3, 10):
        got = hh_residue(cycle_degrees(n))
        expected = ceil(n / 3)
        ok = got == expected
        all_ok &= ok
        print(f"C{n} residue: computed={got} expected=ceil({n}/3)={expected} pass={ok}")
    print(f"CALIBRATION PASS={all_ok}")
    if not all_ok:
        raise SystemExit("calibration failed; no theorem numbers computed")


def enumerate_shapes():
    data = {}
    for nu in range(1, 7):
        e0 = []
        boundary = []
        eplus_tested = 0
        eplus_survivors = []
        for lam in partitions(2 * nu):
            lam1 = lam[0]
            s0 = hh_steps((lam1,) * (lam1 + 1) + lam)
            e0.append((lam, s0, s0 == lam1, fan6_certificate(lam)))
            for L in range(nu + 1, lam1):
                steps = hh_steps((L,) * (L + 1) + lam)
                boundary.append((L, lam, steps, steps == L, fan6_certificate(lam)))
        for E in range(1, nu):
            for L in range(nu + 1, 2 * nu - E + 1):
                for e in partitions(E):
                    if len(e) > L + 1:
                        continue
                    cp = c_part(L, e)
                    for lam in partitions(2 * nu - E):
                        eplus_tested += 1
                        steps = hh_steps(cp + lam)
                        if steps == L:
                            eplus_survivors.append(
                                (L, E, e, lam, steps, fan6_certificate(lam))
                            )
        data[nu] = {
            "e0": e0,
            "boundary": boundary,
            "eplus_tested": eplus_tested,
            "eplus_survivors": eplus_survivors,
        }
    return data


def print_enumeration(data):
    print("\n=== REFUTE-FIRST FINITE ENUMERATION (generated, not copied) ===")
    for nu, d in data.items():
        e0_survivors = [r for r in d["e0"] if r[2]]
        boundary_survivors = [r for r in d["boundary"] if r[3]]
        un_killed = [r for r in d["eplus_survivors"] if not r[5][0]]
        print(
            f"nu={nu}: partitions={len(d['e0'])}; "
            f"E0-tail-survivors={len(e0_survivors)}; "
            f"boundary-pairs={len(d['boundary'])}; "
            f"boundary-survivors={len(boundary_survivors)}; "
            f"Eplus-tested={d['eplus_tested']}; "
            f"Eplus-survivors={len(d['eplus_survivors'])}; "
            f"Eplus-not-killed-by-FAN6prime={len(un_killed)}"
        )
        print("  E0 tail:", [fmt(r[0]) for r in e0_survivors])
        print(
            "  boundary:",
            [(r[0], fmt(r[1]), r[4][1:]) for r in boundary_survivors],
        )
        print("  Eplus survivors:")
        for L, E, e, lam, steps, cert in d["eplus_survivors"]:
            print(
                f"    L{L} E{E} e={fmt(e)} lambda={fmt(lam)} "
                f"steps={steps} FAN6prime={cert}"
            )

    # Only now compare against the numbers printed in the reviewed text.
    expected_partition_counts = [2, 5, 11, 22, 42, 77]
    expected_boundary_counts = [0, 1, 3, 7, 14, 26]
    expected_shape_counts = [0, 3, 24, 110, 397, 1211]
    expected_survivor_counts = [0, 1, 4, 9, 20, 38]
    got_partition_counts = [len(data[nu]["e0"]) for nu in range(1, 7)]
    got_boundary_counts = [len(data[nu]["boundary"]) for nu in range(1, 7)]
    got_shape_counts = [data[nu]["eplus_tested"] for nu in range(1, 7)]
    got_survivor_counts = [len(data[nu]["eplus_survivors"]) for nu in range(1, 7)]
    print("\n=== AFTER-THE-FACT COMPARISON WITH PRINTED COUNTS ===")
    for label, got, expected in (
        ("partition counts", got_partition_counts, expected_partition_counts),
        ("boundary counts", got_boundary_counts, expected_boundary_counts),
        ("Eplus shape counts S(nu)", got_shape_counts, expected_shape_counts),
        ("Eplus survivor counts", got_survivor_counts, expected_survivor_counts),
    ):
        print(f"{label}: computed={got} printed={expected} match={got == expected}")


def print_e0_full(data):
    print("\n=== FULL RECOMPUTED s0 TABLE ===")
    for nu, d in data.items():
        print(f"nu={nu}")
        for lam, s0, survives, cert in d["e0"]:
            print(
                f"  lambda={fmt(lam)} s0={s0} lambda1={lam[0]} "
                f"tail-survives={survives} FAN6prime={cert}"
            )


def tail_and_padding_controls(data):
    tail_pairs = 0
    tail_mismatches = []
    for nu in range(1, 7):
        for lam, s0, _, _ in data[nu]["e0"]:
            for L in range(lam[0], 16):
                tail_pairs += 1
                direct = hh_steps((L,) * (L + 1) + lam)
                predicted = (L - lam[0]) + s0
                if direct != predicted:
                    tail_mismatches.append((nu, L, lam, direct, predicted))
    print("\n=== TAIL CONTROL ===")
    print(f"pairs={tail_pairs} mismatches={len(tail_mismatches)}")
    for row in tail_mismatches:
        print("  MISMATCH", row)

    padding_lists = 0
    padding_mismatches = []
    pads = (0, 1, 2, 3, 4, 8)
    for nu in range(1, 5):
        for lam in partitions(2 * nu):
            for L in range(1, 13):
                padding_lists += 1
                results = [hh_steps((L,) * (L + 1) + lam + (0,) * z) for z in pads]
                if len(set(results)) != 1:
                    padding_mismatches.append((nu, L, lam, results))
    print("\n=== ZERO-PADDING CONTROL ===")
    print(f"base-lists={padding_lists} paddings={list(pads)} mismatches={len(padding_mismatches)}")
    for row in padding_mismatches:
        print("  MISMATCH", row)


def gfan2_control(data):
    print("\n=== GFAN2 DIRECT CONTROL ===")
    d = data[2]
    for L in range(3, 13):
        rows = []
        for E in range(0, 2):
            if E and L > 4 - E:
                continue
            es = [()] if E == 0 else list(partitions(E))
            for e in es:
                for lam in partitions(4 - E):
                    steps = hh_steps(c_part(L, e) + lam)
                    if steps == L:
                        rows.append((E, e, lam, fan6_certificate(lam)))
        print(f"L={L}: exact-L rows={[(E, fmt(e), fmt(lam), cert) for E,e,lam,cert in rows]}")
    all_candidates = []
    for lam, s0, survives, cert in d["e0"]:
        if survives:
            all_candidates.append(("tail", lam, cert))
    for L, lam, steps, survives, cert in d["boundary"]:
        if survives:
            all_candidates.append((f"boundary-L{L}", lam, cert))
    for L, E, e, lam, steps, cert in d["eplus_survivors"]:
        all_candidates.append((f"Eplus-L{L}-E{E}-e{fmt(e)}", lam, cert))
    print("finite surviving shapes before FAN6prime:", all_candidates)
    print("un-killed shapes:", [x for x in all_candidates if not x[2][0]])


# ----- Graph controls: no third-party graph package is used. -----


def graph_from_edges(vertices, edges):
    adj = {v: set() for v in vertices}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def connected(adj, subset=None):
    verts = set(adj) if subset is None else set(subset)
    if not verts:
        return True
    seen = set()
    stack = [next(iter(verts))]
    while stack:
        u = stack.pop()
        if u in seen:
            continue
        seen.add(u)
        stack.extend((adj[u] & verts) - seen)
    return seen == verts


def independent(adj, subset):
    s = set(subset)
    return all(not (adj[v] & s) for v in s)


def acyclic(adj, subset):
    s = set(subset)
    seen = set()
    for root in s:
        if root in seen:
            continue
        stack = [(root, None)]
        while stack:
            u, parent = stack.pop()
            if u in seen:
                return False
            seen.add(u)
            for v in adj[u] & s:
                if v != parent:
                    stack.append((v, u))
    return True


def maximum_size(adj, predicate):
    vertices = tuple(adj)
    for size in range(len(vertices), -1, -1):
        for subset in combinations(vertices, size):
            if predicate(adj, subset):
                return size, subset
    raise AssertionError


def diameter(adj):
    if not connected(adj):
        return None
    answer = 0
    for source in adj:
        dist = {source: 0}
        queue = [source]
        for u in queue:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        answer = max(answer, max(dist.values()))
    return answer


def degree_sequence(adj):
    return sorted((len(nbrs) for nbrs in adj.values()), reverse=True)


def find_frame_witness():
    """Search a small constrained GFan frame; return first class-valid graph.

    B={b0,b1,b2,b3}; b0 is low and B-universal.  G[B] is K4-b1b2.
    a0 is B-universal, and each other independent A vertex has a nonempty
    neighbourhood in {b1,b2,b3}.  Candidate A is checked exhaustive-maximum.
    """
    B = ("b0", "b1", "b2", "b3")
    b_edges = [
        ("b0", "b1"), ("b0", "b2"), ("b0", "b3"),
        ("b1", "b3"), ("b2", "b3"),
    ]
    masks = tuple(range(1, 8))
    for alpha_target in range(4, 8):
        aprime = tuple(f"a{i}" for i in range(1, alpha_target))
        A = ("a0",) + aprime
        vertices = A + B
        for choices in combinations_with_replacement(masks, len(aprime)):
            edges = list(b_edges) + [("a0", b) for b in B]
            for a, mask in zip(aprime, choices):
                for i, b in enumerate(B[1:]):
                    if mask & (1 << i):
                        edges.append((a, b))
            adj = graph_from_edges(vertices, edges)
            # Required low/high split for tau=4 and B-universality of b0.
            Blo = tuple(b for b in B if len(adj[b]) <= len(B))
            if not Blo or any((set(B) - {b}) - adj[b] for b in Blo):
                continue
            alpha, alpha_set = maximum_size(adj, independent)
            if alpha != len(A) or not independent(adj, A):
                continue
            if diameter(adj) != 4:
                continue
            f, forest_set = maximum_size(adj, acyclic)
            if f != alpha + 1:
                continue
            if acyclic(adj, vertices):
                continue
            return adj, A, B, Blo, alpha_set, forest_set
    return None


def validate_frame_witness():
    print("\n=== RIG CONSTRUCTION AND CLASS-ORDER WITNESS VALIDATION ===")
    found = find_frame_witness()
    if found is None:
        print("NO full hard-core-frame witness found in the stated constrained search box")
        return None
    adj, A, B, Blo, alpha_set, forest_set = found
    edges = sorted(tuple(sorted((u, v))) for u in adj for v in adj[u] if u < v)
    print("vertices:", list(adj))
    print("edges:", edges)
    # Class predicates in the order mandated by the review brief.
    print("1 connected:", connected(adj))
    alpha, exhaustive_witness = maximum_size(adj, independent)
    print(
        "2 A maximum by exhaustive subset enumeration:",
        independent(adj, A) and len(A) == alpha,
        "A=", A,
        "alpha=", alpha,
        "one maximum set=", exhaustive_witness,
    )
    diam = diameter(adj)
    print("3 diameter:", diam, "equals4=", diam == 4)
    f, fset = maximum_size(adj, acyclic)
    print("4 forest number:", f, "alpha+1=", alpha + 1, "witness=", fset, "pass=", f == alpha + 1)
    nonforest = not acyclic(adj, tuple(adj))
    print("5 non-forest:", nonforest)
    residue = hh_residue(degree_sequence(adj))
    print("6 residue-vs-alpha:", residue, alpha, "equal(reductio)=", residue == alpha)

    tau = len(B)
    Bhi = tuple(b for b in B if len(adj[b]) >= tau + 1)
    nonedges_B = sorted(
        (B[i], B[j]) for i in range(len(B)) for j in range(i + 1, len(B))
        if B[j] not in adj[B[i]]
    )
    unique_A = {b: tuple(a for a in A if a in adj[b]) for b in Blo}
    a0s = set.intersection(*(set(v) for v in unique_A.values())) if unique_A else set()
    a0 = next(iter(a0s)) if a0s else None
    conclusions = {
        "(a) each low deg_A=1": all(len(unique_A[b]) == 1 for b in Blo),
        "(b) common unique a0": len(a0s) == 1,
        "(c) a0 adjacent all B": a0 is not None and set(B) <= adj[a0],
        "(d) all B nonedges in Bhi and nu>=1": bool(nonedges_B) and all(u in Bhi and v in Bhi for u, v in nonedges_B),
        "(e) A-a0 avoids Blo": a0 is not None and all(not (adj[a] & set(Blo)) for a in A if a != a0),
    }
    print("B_lo:", Blo, "B_hi:", Bhi, "B-nonedges:", nonedges_B)
    print("RIG conclusions:", conclusions)
    return adj, A, B


def counterfactual_control():
    print("\n=== COUNTERFACTUAL AVAILABILITY CONTROL ===")
    # It looks like the start-of-tail shape for nu=2,L=3,E=1, but lambda has
    # mass 2 rather than the required 2*nu-E=3.
    nu, L, E = 2, 3, 1
    e = (1,)
    lam = (2,)
    values = c_part(L, e) + lam
    steps, residue, valid, trace = hh_run(values, trace=True)
    print(f"instance: nu={nu} L={L} E={E} e={e} lambda={lam} list={values}")
    print(f"lambda-mass={sum(lam)} required-mass={2*nu-E} mass-hypothesis-pass={sum(lam)==2*nu-E}")
    print(f"HH: valid={valid} steps={steps} residue={residue} trace={trace}")
    print(
        "availability: FAN-4prime unavailable (its exact mass conclusion fails); "
        "FAN-8prime and FAN-6prime unavailable because this shape is not established "
        "to arise from GFan under the reductio."
    )


def literal_nu_zero_counterexample():
    """Validate K5 against the literal hypotheses of Theorem GFANnu."""
    print("\n=== LITERAL nu=0 COUNTEREXAMPLE TO THEOREM GFANnu ===")
    A = ("a0",)
    B = ("b0", "b1", "b2", "b3")
    vertices = A + B
    edges = list(combinations(vertices, 2))
    adj = graph_from_edges(vertices, edges)
    print("graph: K5")
    print("vertices:", vertices)
    print("edges:", edges)
    # The hard-core predicates are printed in their stipulated class order even
    # though the literal theorem statement does not require that class.
    print("1 connected:", connected(adj))
    alpha, alpha_set = maximum_size(adj, independent)
    print(
        "2 A maximum by exhaustive subset enumeration:",
        independent(adj, A) and len(A) == alpha,
        "A=", A,
        "alpha=", alpha,
        "one maximum set=", alpha_set,
    )
    diam = diameter(adj)
    print("3 diameter:", diam, "equals4=", diam == 4)
    f, fset = maximum_size(adj, acyclic)
    print("4 forest number:", f, "alpha+1=", alpha + 1, "witness=", fset, "pass=", f == alpha + 1)
    nonforest = not acyclic(adj, vertices)
    print("5 non-forest:", nonforest)
    degrees = degree_sequence(adj)
    residue = hh_residue(degrees)
    print("6 residue-vs-alpha:", residue, alpha, "equal(reductio)=", residue == alpha, "degree-sequence=", degrees)

    tau = len(B)
    Blo = tuple(b for b in B if len(adj[b]) <= tau)
    Bhi = tuple(b for b in B if len(adj[b]) >= tau + 1)
    nu = sum(
        1 for i in range(len(B)) for j in range(i + 1, len(B))
        if B[j] not in adj[B[i]]
    )
    L = len(Blo)
    gfan_checks = {
        "B_lo nonempty": bool(Blo),
        "all B_lo B-universal": all((set(B) - {b}) <= adj[b] for b in Blo),
        "all B_lo deg_A=1": all(len(adj[b] & set(A)) == 1 for b in Blo),
        "common a0 adjacent all B": set(B) <= adj["a0"],
        "all nu nonedges inside B_hi": all(
            (B[j] in adj[B[i]]) or (B[i] in Bhi and B[j] in Bhi)
            for i in range(len(B)) for j in range(i + 1, len(B))
        ),
        "all B_hi high": all(len(adj[b]) >= tau + 1 for b in Bhi),
        "A-prime avoids B_lo": all(not (adj[a] & set(Blo)) for a in A if a != "a0"),
    }
    print("parameters: tau=", tau, "L=", L, "nu=", nu, "B_lo=", Blo, "B_hi=", Bhi)
    print("GFan clauses:", gfan_checks, "all-pass=", all(gfan_checks.values()))
    theorem_range = nu <= 6 and L >= nu + 1
    print("literal theorem range nu<=6 and L>=nu+1:", theorem_range)
    print(
        "COUNTEREXAMPLE PASS=",
        all(gfan_checks.values()) and theorem_range and residue == alpha,
    )
    print(
        "load-bearing omitted condition: diam=4 would exclude this graph and, via "
        "Observation R1, force nu>=1."
    )


def main():
    print_calibration()
    data = enumerate_shapes()
    print_enumeration(data)
    print_e0_full(data)
    tail_and_padding_controls(data)
    gfan2_control(data)
    validate_frame_witness()
    counterfactual_control()
    literal_nu_zero_counterexample()
    print("\nCHECKER COMPLETED")


if __name__ == "__main__":
    main()
