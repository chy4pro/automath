#!/usr/bin/env python3
"""Independent checks for prompts/w61_S3_GFAN_r24.md.

Written from the specification printed in that brief.  This program does not read
the prompt, the draft, archived scripts, reviews, or any other project artifact.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations


def popcount(x):
    return bin(x).count("1")


def hh_run(values, keep_trace=False):
    """Return (valid step sequence, steps, residue, trace)."""
    a = list(values)
    if any((not isinstance(x, int)) or x < 0 for x in a):
        return False, 0, None, []
    steps = 0
    trace = []
    while any(a):
        a.sort(reverse=True)
        before = tuple(a)
        d = a.pop(0)
        if d > len(a) or any(x == 0 for x in a[:d]):
            if keep_trace:
                trace.append((before, d, "INVALID"))
            return False, steps, None, trace
        for i in range(d):
            a[i] -= 1
        steps += 1
        if keep_trace:
            trace.append((before, d, tuple(sorted(a, reverse=True))))
    return True, steps, len(a), trace


def partitions(n, cap=None):
    """Yield integer partitions as nonincreasing tuples."""
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def p(n):
    return sum(1 for _ in partitions(n))


def value_list(L, escape_partition, lam):
    e = tuple(escape_partition)
    assert len(e) <= L + 1
    return [L + x for x in e] + [L] * (L + 1 - len(e)) + list(lam)


def certificate(lam):
    vals = list(lam)
    if not vals:
        return None
    w = vals[0]
    second = vals[1] if len(vals) >= 2 else 0
    unique = len(vals) == 1 or vals[1] < w
    return w, second, unique and w >= 1 and second <= w - 2


def enumerate_positive_E(nu):
    counts = Counter()
    survivors = []
    misses = []
    tested = 0
    for E in range(1, nu):
        eparts = list(partitions(E))
        lparts = list(partitions(2 * nu - E))
        for L in range(nu + 1, 2 * nu - E + 1):
            for e in eparts:
                assert len(e) <= L + 1
                for lam in lparts:
                    tested += 1
                    ok, steps, _, _ = hh_run(value_list(L, e, lam))
                    if ok and steps == L:
                        row = (nu, L, E, e, lam, certificate(lam))
                        survivors.append(row)
                        counts[E] += 1
                        if not row[-1][-1]:
                            misses.append(row)
    expected = sum((nu - E) * p(E) * p(2 * nu - E) for E in range(1, nu))
    assert tested == expected
    return tested, counts, survivors, misses


def enumerate_E0(nu):
    tail = []
    boundary_tested = 0
    boundary_survivors = []
    s0eq = []
    for lam in partitions(2 * nu):
        m = lam[0]
        ok, s0, _, _ = hh_run([m] * (m + 1) + list(lam))
        if ok and s0 == m:
            s0eq.append(lam)
        for L in range(nu + 1, m):
            boundary_tested += 1
            ok2, steps, _, _ = hh_run(value_list(L, (), lam))
            if ok2 and steps == L:
                boundary_survivors.append((L, lam, certificate(lam)))
    return s0eq, boundary_tested, boundary_survivors


def print_trace(label, values):
    ok, steps, residue, trace = hh_run(values, keep_trace=True)
    heads = [row[1] for row in trace]
    print(f"{label}: valid={ok} steps={steps} residue={residue} heads={heads}")


def calibration():
    print("=== CALIBRATION (printed before held-out computations) ===")
    ok, steps, residue, _ = hh_run([1, 1])
    print(f"K2 degrees [1,1]: valid={ok}, steps={steps}, residue={residue}, expected=1")
    assert ok and residue == 1
    for n in range(3, 10):
        ok, steps, residue, _ = hh_run([2] * n)
        expected = (n + 2) // 3
        print(f"C{n} degrees {[2] * n}: valid={ok}, steps={steps}, residue={residue}, expected={expected}")
        assert ok and residue == expected


def held_out():
    print("\n=== SECTION 0 HELD-OUT COMPUTATIONS ===")
    h1parts = [(12, 6, 4), (9, 7, 3, 3), (14, 5, 2, 1), (8, 8, 6)]
    for lam in h1parts:
        values = [lam[0]] * (lam[0] + 1) + list(lam)
        print_trace(f"H1 lambda={list(lam)}", values)

    terms = []
    for E in range(1, 11):
        term = (11 - E) * p(E) * p(22 - E)
        terms.append(term)
    print(f"H2 terms={terms}; S(11)={sum(terms)}")

    tested, counts, survivors, misses = enumerate_positive_E(11)
    split = [counts[E] for E in range(1, 11)]
    print(f"H3 tested={tested}; survivors={len(survivors)}; per-E E=1..10={split}; FAN6-misses={len(misses)}")

    s0_13 = []
    for lam in partitions(22):
        values = [lam[0]] * (lam[0] + 1) + list(lam)
        ok, steps, _, _ = hh_run(values)
        if ok and steps == 13:
            s0_13.append(lam)
    print(f"H4 partitions(22)={p(22)}; count s0=13 is {len(s0_13)}")
    print("H4 matching partitions:", [list(x) for x in s0_13])

    h5 = value_list(13, (2, 1), (5, 4, 4, 3, 3))
    print_trace("H5 L=13 E=3 e=[2,1] lambda=[5,4,4,3,3]", h5)
    return survivors


def gfannu_checks():
    print("\n=== GFANnu INDEPENDENT ENUMERATION ===")
    expected_tested = {1: 0, 2: 3, 3: 24, 4: 110, 5: 397, 6: 1211,
                       7: 3340, 8: 8457, 9: 20126, 10: 45450}
    expected_survivors = {1: 0, 2: 1, 3: 4, 4: 9, 5: 20, 6: 38,
                          7: 75, 8: 137, 9: 251, 10: 447}
    expected_boundary_pairs = {1: 0, 2: 1, 3: 3, 4: 7, 5: 14, 6: 26,
                               7: 45, 8: 75, 9: 120, 10: 187}
    expected_boundary_survivors = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3,
                                   7: 3, 8: 4, 9: 4, 10: 5}
    all_agree = True
    for nu in range(1, 12):
        tested, counts, surv, misses = enumerate_positive_E(nu)
        s0eq, btested, bsurv = enumerate_E0(nu)
        print(f"nu={nu}: E+ tested={tested}, split={dict(sorted(counts.items()))}, survivors={len(surv)}, misses={len(misses)}; "
              f"E0 s0=lambda1={len(s0eq)} {s0eq}; boundary tested={btested}, survivors={len(bsurv)}")
        if nu <= 10:
            agrees = (tested == expected_tested[nu] and len(surv) == expected_survivors[nu]
                      and btested == expected_boundary_pairs[nu]
                      and len(bsurv) == expected_boundary_survivors[nu]
                      and misses == [] and s0eq == [(2 * nu,)])
            print(f"  comparison with printed aggregate data: {'AGREE' if agrees else 'DISAGREE'}")
            all_agree &= agrees
        if misses:
            print("  UNKILLED SURVIVORS:", misses)
    print(f"GFANnu nu<=10 aggregate comparison: {'ALL AGREE' if all_agree else 'DISAGREEMENT FOUND'}")


def gfan2_checks():
    print("\n=== GFAN2 DIRECT TRAJECTORIES ===")
    parts4 = list(partitions(4))
    for L in (4, 5, 8):
        for lam in parts4:
            ok, steps, _, _ = hh_run(value_list(L, (), lam))
            print(f"L={L} E=0 lambda={lam}: valid={ok}, steps={steps}, cert={certificate(lam)}")
    for E in (0, 1):
        for e in partitions(E):
            for lam in partitions(4 - E):
                ok, steps, _, _ = hh_run(value_list(3, e, lam))
                print(f"L=3 E={E} e={e} lambda={lam}: valid={ok}, steps={steps}, cert={certificate(lam)}")


def spot_checks():
    print("\n=== NAMED ROSTER SPOT CHECKS ===")
    rows = [
        (5, 6, (2, 2), (4, 2)),
        (6, 7, (3, 2), (4, 2, 1)),
        (7, 8, (2, 2, 2), (5, 3)),
        (8, 10, (2,), (12, 2)),
        (10, 11, (4, 4, 1), (5, 2, 2, 2)),
    ]
    for nu, L, e, lam in rows:
        E = sum(e)
        assert sum(lam) == 2 * nu - E
        vals = value_list(L, e, lam)
        ok, steps, _, _ = hh_run(vals)
        print(f"nu={nu} L={L} E={E} e={e} lambda={lam}: valid={ok}, steps={steps}, cert={certificate(lam)}, list={vals}")


def padding_and_tail_controls():
    print("\n=== SPECIFICATION CONTROLS ===")
    padding_mismatch = 0
    checked = 0
    for nu in range(1, 12):
        for E in range(0, nu):
            Ls = range(nu + 1, 2 * nu - E + 1) if E else (nu + 1, 2 * nu)
            for L in Ls:
                eparts = partitions(E)
                for e in eparts:
                    for lam in partitions(2 * nu - E):
                        base = hh_run(value_list(L, e, lam))[:2]
                        for z in (1, 2, 7, 13):
                            checked += 1
                            if hh_run(value_list(L, e, lam) + [0] * z)[:2] != base:
                                padding_mismatch += 1
    print(f"zero-padding checks={checked}, mismatches={padding_mismatch}")

    tail_checked = 0
    tail_mismatch = 0
    for nu in range(1, 12):
        for lam in partitions(2 * nu):
            m = lam[0]
            ok0, s0, _, _ = hh_run([m] * (m + 1) + list(lam))
            for L in range(max(nu + 1, m), 2 * nu + 4):
                ok, steps, _, _ = hh_run(value_list(L, (), lam))
                predicted = (L - m) + s0
                tail_checked += 1
                if ok != ok0 or (ok and steps != predicted):
                    tail_mismatch += 1
    print(f"TAIL direct-vs-formula checks={tail_checked}, mismatches={tail_mismatch}")

    cf = value_list(4, (1,), (4,))  # nu=3 would require lambda mass 5, not 4.
    ok, steps, _, _ = hh_run(cf)
    print(f"counterfactual shape nu=3 L=4 E=1 e=(1) lambda=(4): list={cf}, valid={ok}, steps={steps}; required lambda mass=5, actual=4")


# Minimal graph utilities for a construction search.  No external graph package is used.
def graph_from_bits(n, bits):
    adj = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (bits >> k) & 1:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
            k += 1
    return adj


def connected(adj):
    n = len(adj)
    seen = 1
    frontier = 1
    while frontier:
        ubit = frontier & -frontier
        frontier ^= ubit
        u = ubit.bit_length() - 1
        new = adj[u] & ~seen
        seen |= new
        frontier |= new
    return seen == (1 << n) - 1


def independent(adj, mask):
    x = mask
    while x:
        bit = x & -x
        x ^= bit
        u = bit.bit_length() - 1
        if adj[u] & x:
            return False
    return True


def maximum_independent_masks(adj):
    n = len(adj)
    best = 0
    masks = []
    for mask in range(1 << n):
        size = popcount(mask)
        if size < best:
            continue
        if independent(adj, mask):
            if size > best:
                best, masks = size, [mask]
            else:
                masks.append(mask)
    return best, masks


def diameter(adj):
    n = len(adj)
    ans = 0
    for src in range(n):
        dist = [-1] * n
        dist[src] = 0
        q = [src]
        for u in q:
            x = adj[u]
            while x:
                bit = x & -x
                x ^= bit
                v = bit.bit_length() - 1
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    q.append(v)
        if -1 in dist:
            return None
        ans = max(ans, max(dist))
    return ans


def induced_forest(adj, mask):
    # A graph is a forest iff every component has edges = vertices-1.
    unseen = mask
    while unseen:
        root = unseen & -unseen
        seen = root
        frontier = root
        edges2 = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            u = bit.bit_length() - 1
            nbr = adj[u] & mask
            edges2 += popcount(nbr)
            new = nbr & ~seen
            seen |= new
            frontier |= new
        verts = popcount(seen)
        if edges2 // 2 != verts - 1:
            return False
        unseen &= ~seen
    return True


def forest_number(adj):
    n = len(adj)
    return max(popcount(mask) for mask in range(1 << n) if induced_forest(adj, mask))


def graph_residue(adj):
    return hh_run([popcount(x) for x in adj])[2]


def target_for_A(adj, A):
    n = len(adj)
    allmask = (1 << n) - 1
    B = allmask ^ A
    tau = popcount(B)
    low = []
    x = B
    while x:
        bit = x & -x
        x ^= bit
        u = bit.bit_length() - 1
        if popcount(adj[u]) <= tau:
            low.append(u)
    all_low_universal = all(((adj[u] & (B ^ (1 << u))) == (B ^ (1 << u))) for u in low)
    nu = 0
    verts = [i for i in range(n) if (B >> i) & 1]
    for i, j in combinations(verts, 2):
        if not ((adj[i] >> j) & 1):
            nu += 1
    return tau, low, all_low_universal, nu


def inspect_candidate(adj):
    # Predicate order mandated by the brief.
    if not connected(adj):
        return None
    alpha, As = maximum_independent_masks(adj)
    if diameter(adj) != 4:
        return None
    f = forest_number(adj)
    if f != alpha + 1:
        return None
    full = (1 << len(adj)) - 1
    if induced_forest(adj, full):
        return None
    if graph_residue(adj) != alpha:
        return None
    for A in As:
        tau, low, universal, nu = target_for_A(adj, A)
        if tau >= 4 and universal:
            return (alpha, A, 4, f, False, graph_residue(adj), tau, low, nu)
    return None


def construction_search():
    print("\n=== CONSTRUCTION / QUANTIFIER SEARCH ===")
    found = []
    n = 6
    total = 1 << (n * (n - 1) // 2)
    for bits in range(total):
        adj = graph_from_bits(n, bits)
        hit = inspect_candidate(adj)
        if hit:
            found.append((n, bits, hit))
            break
    print(f"exhaustive labeled n=6 graphs tested={total}; full hard-core/all-low-universal hits={len(found)}")

    # Fixed LCG sampling, so this exploratory construction search is reproducible.
    state = 0x61_53_24
    sampled = 0
    for n in range(7, 11):
        width = n * (n - 1) // 2
        mask = (1 << width) - 1
        for _ in range(3000):
            state = (6364136223846793005 * state + 1442695040888963407) & ((1 << 64) - 1)
            bits = state & mask
            sampled += 1
            hit = inspect_candidate(graph_from_bits(n, bits))
            if hit:
                found.append((n, bits, hit))
                break
    print(f"fixed-seed sampled n=7..10 graphs tested={sampled}; cumulative hits={len(found)}")
    if found:
        for n, bits, hit in found:
            print(f"WITNESS n={n} edge_bits={bits} ordered predicates=(connected=True, alpha/A={hit[0:2]}, diam={hit[2]}, f={hit[3]}, nonforest={not hit[4]}, residue={hit[5]}); tau={hit[6]} low={hit[7]} nu={hit[8]}")
    else:
        print("Vacuity honesty: this bounded search contained no instance satisfying all composite hypotheses; this is not positive evidence for the theorem.")


def main():
    calibration()
    held_out()
    gfannu_checks()
    gfan2_checks()
    spot_checks()
    padding_and_tail_controls()
    construction_search()
    print("\nVERDICT: GAP")


if __name__ == "__main__":
    main()
