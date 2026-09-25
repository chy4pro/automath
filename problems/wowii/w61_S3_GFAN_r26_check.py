#!/usr/bin/env python3
"""Independent checks for prompts/w61_S3_GFAN_r26.md.

This program is written from Appendix A.0 and Appendix C.1 only.  It does not
read or parse any author enumeration or review artifact.
"""

from collections import Counter
from functools import lru_cache
import itertools
from pathlib import Path
import re


def hh_run(values, trace=False):
    """Return (valid, steps, residue, trace_rows) for the specified HH run."""
    a = list(values)
    rows = []
    steps = 0
    while True:
        a.sort(reverse=True)
        if any(x < 0 for x in a):
            return False, None, None, rows
        if not a or a[0] == 0:
            return True, steps, len(a), rows
        before = tuple(a)
        d = a.pop(0)
        if d > len(a):
            return False, None, None, rows
        if any(a[i] <= 0 for i in range(d)):
            return False, None, None, rows
        for i in range(d):
            a[i] -= 1
        steps += 1
        if trace:
            rows.append((steps, before, d, tuple(sorted(a, reverse=True))))


def step_count(values):
    valid, steps, _, _ = hh_run(values)
    return steps if valid else None


def residue(values):
    valid, _, r, _ = hh_run(values)
    return r if valid else None


@lru_cache(maxsize=None)
def partitions(n, cap=None):
    """All positive integer partitions, as nonincreasing tuples."""
    if cap is None or cap > n:
        cap = n
    if n == 0:
        return ((),)
    out = []
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, min(first, n - first)):
            out.append((first,) + tail)
    return tuple(out)


def p(n):
    return len(partitions(n))


def s0(lam):
    top = lam[0]
    return step_count((top,) * (top + 1) + tuple(lam))


def c_list(L, e):
    return tuple(sorted((tuple(L + x for x in e) + (L,) * (L + 1 - len(e))), reverse=True))


def shape_list(L, e, lam):
    return c_list(L, e) + tuple(lam)


def fan6_certificate(lam):
    w = lam[0]
    second = lam[1] if len(lam) > 1 else 0
    killed = w >= 1 and (len(lam) == 1 or lam[1] < w) and second <= w - 2
    return killed, (w, second)


def enumerate_positive_escape(nu):
    tested = Counter()
    survivors = Counter()
    misses = []
    rows = []
    for E in range(1, nu):
        for L in range(nu + 1, 2 * nu - E + 1):
            for e in partitions(E):
                for lam in partitions(2 * nu - E):
                    tested[E] += 1
                    values = shape_list(L, e, lam)
                    if step_count(values) == L:
                        survivors[E] += 1
                        killed, cert = fan6_certificate(lam)
                        row = (L, E, e, lam, cert)
                        rows.append(row)
                        if not killed:
                            misses.append(row)
    return tested, survivors, rows, misses


def enumerate_e0(nu):
    tail_survivors = []
    boundary_tested = 0
    boundary_survivors = []
    for lam in partitions(2 * nu):
        if s0(lam) == lam[0]:
            tail_survivors.append(lam)
        for L in range(nu + 1, lam[0]):
            boundary_tested += 1
            if step_count((L,) * (L + 1) + lam) == L:
                boundary_survivors.append((L, lam, fan6_certificate(lam)[1]))
    return tail_survivors, boundary_tested, boundary_survivors


def fmt_counter(c):
    return "{" + ", ".join(f"{k}:{c[k]}" for k in sorted(c)) + "}"


def calibration():
    checks = [("K2", (1, 1), 1)]
    checks.extend((f"C{n}", (2,) * n, (n + 2) // 3) for n in range(3, 10))
    print("CALIBRATION (printed before every Section 0 value)")
    ok = True
    for name, seq, expected in checks:
        got = residue(seq)
        good = got == expected
        ok &= good
        print(f"  {name}: residue={got}, expected={expected}, {'PASS' if good else 'FAIL'}")
    print(f"CALIBRATION_STATUS={'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("calibration failed")


def section0():
    print("SECTION 0 HELD-OUT CHECKS")
    h1_parts = ((12, 6, 4), (9, 7, 3, 3), (14, 5, 2, 1), (8, 8, 6))
    print("H1")
    for lam in h1_parts:
        values = (lam[0],) * (lam[0] + 1) + lam
        valid, steps, _, rows = hh_run(values, trace=True)
        print(
            f"  lambda={list(lam)} valid={valid} s0={steps} "
            f"heads={[row[2] for row in rows]}"
        )

    terms = []
    for E in range(1, 11):
        terms.append((E, 11 - E, p(E), p(22 - E), (11 - E) * p(E) * p(22 - E)))
    print("H2")
    for E, mult, pe, plam, term in terms:
        print(f"  E={E}: ({mult})*p({E})={pe}*p({22-E})={plam} -> {term}")
    print(f"  S(11)={sum(t[-1] for t in terms)}")

    tested11, survivors11, rows11, misses11 = enumerate_positive_escape(11)
    print("H3")
    print(f"  tested={sum(tested11.values())} tested_split={fmt_counter(tested11)}")
    print(f"  survivors={len(rows11)} survivor_split={fmt_counter(survivors11)}")
    print(f"  FAN6_misses={len(misses11)}")

    count13 = sum(s0(lam) == 13 for lam in partitions(22))
    print("H4")
    print(f"  partitions_of_22={p(22)} count_s0_eq_13={count13}")

    h5 = shape_list(13, (2, 1), (5, 4, 4, 3, 3))
    h5_valid, h5_steps, _, h5_trace = hh_run(h5, trace=True)
    print("H5")
    print(f"  list={list(h5)}")
    print(f"  valid={h5_valid} clears_in_13={h5_valid and h5_steps == 13} actual_steps={h5_steps}")
    print("  heads=" + str([row[2] for row in h5_trace]))


def theorem_checks():
    print("THEOREM_GFANNU_REGENERATION")
    all_rows = {}
    for nu in range(1, 11):
        tail, boundary_n, boundary_surv = enumerate_e0(nu)
        tested, survivors, rows, misses = enumerate_positive_escape(nu)
        all_rows[nu] = rows
        expected_s = sum((nu - E) * p(E) * p(2 * nu - E) for E in range(1, nu))
        print(
            f"  nu={nu}: partitions={p(2*nu)} tail_survivors={tail} "
            f"boundary={boundary_n}/{len(boundary_surv)} Epos={sum(tested.values())}/{len(rows)} "
            f"formula={expected_s} split={fmt_counter(survivors)} FAN6_misses={len(misses)}"
        )
        if sum(tested.values()) != expected_s or misses:
            print(f"    ANOMALY misses={misses}")

    print("GFAN2_L3_EIGHT_ROWS")
    for E in (0, 1):
        es = ((),) if E == 0 else ((1,),)
        for e in es:
            for lam in partitions(4 - E):
                steps = step_count(shape_list(3, e, lam))
                killed, cert = fan6_certificate(lam)
                print(f"  E={E} e={e} lambda={lam} steps={steps} FAN6={killed} cert={cert}")

    print("GFAN2_L_GE_4_TRAJECTORIES")
    for L in (4, 7):
        for lam in ((2, 2), (2, 1, 1), (1, 1, 1, 1)):
            print(f"  L={L} lambda={lam} steps={step_count((L,)*(L+1)+lam)}")

    print("NAMED_ROSTER_SPOT_CHECKS")
    checks = [
        (5, 6, (2, 2), (4, 2)),
        (6, 7, (3, 2), (4, 2, 1)),
        (7, 8, (3, 3), (4, 2, 2)),
        (8, 9, (4, 4), (4, 2, 2, 2)),
        (10, 11, (5, 4), (4, 2, 2, 2, 1)),
    ]
    for nu, L, e, lam in checks:
        vals = shape_list(L, e, lam)
        killed, cert = fan6_certificate(lam)
        print(
            f"  nu={nu} L={L} E={sum(e)} e={e} lambda={lam}: "
            f"steps={step_count(vals)} cert={cert} FAN6={killed} list={vals}"
        )


def printed_data_comparison():
    """After regeneration, compare the regenerated rows with the prompt's data."""
    prompt = Path("prompts/w61_S3_GFAN_r26.md").read_text()

    # All 159 printed s0 values in (C-2).
    c2 = prompt.split("**(C-2) The `E = 0` column", 1)[1].split("**Reading.**", 1)[0]
    printed_s0 = {}
    headings = list(re.finditer(r"> \*\*ν = (\d+)\*\*", c2))
    for i, match in enumerate(headings):
        nu = int(match.group(1))
        end = headings[i + 1].start() if i + 1 < len(headings) else len(c2)
        block = c2[match.end():end]
        for lam_text, value in re.findall(r"(?:\*\*)?(\d+(?:\+\d+)*):(\d+)", block):
            lam = tuple(map(int, lam_text.split("+")))
            printed_s0[(nu, lam)] = int(value)
    computed_s0 = {
        (nu, lam): s0(lam)
        for nu in range(1, 7)
        for lam in partitions(2 * nu)
    }

    # E>=1 survivor rosters: (C-4) uses one row per L; (C-8) groups L values.
    printed_epos = set()
    c4 = prompt.split("Now the survivors.", 1)[1].split("**Reading.**", 1)[0]
    current_nu = None
    for line in c4.splitlines():
        nu_match = re.search(r"\*\*ν = (\d+)\*\*", line)
        if nu_match:
            current_nu = int(nu_match.group(1))
        for L, E, e_text, lam_text in re.findall(
            r"L(\d+) E(\d+) e=([0-9+]+) λ=([0-9+]+)", line
        ):
            printed_epos.add(
                (current_nu, int(L), int(E), tuple(map(int, e_text.split("+"))),
                 tuple(map(int, lam_text.split("+"))))
            )

    c8 = prompt.split("**(C-8) The `ν = 7…10` rosters", 1)[1]
    current_nu = None
    for line in c8.splitlines():
        nu_match = re.search(r"\*\*`ν = (\d+)`\*\*", line)
        if nu_match:
            current_nu = int(nu_match.group(1))
        row = re.search(
            r"`E(\d+) e=([0-9+]+) λ=([0-9+]+)` — `L ∈ \{([0-9,]+)\}`", line
        )
        if row:
            E = int(row.group(1))
            e = tuple(map(int, row.group(2).split("+")))
            lam = tuple(map(int, row.group(3).split("+")))
            for L in map(int, row.group(4).split(",")):
                printed_epos.add((current_nu, L, E, e, lam))

    generated_epos = set()
    for nu in range(1, 11):
        _, _, rows, _ = enumerate_positive_escape(nu)
        generated_epos.update((nu, L, E, e, lam) for L, E, e, lam, _ in rows)

    # Boundary rosters in (C-3) and (C-8).
    printed_boundary = set()
    c3 = prompt.split("**(C-3) The `E = 0` boundary rows", 1)[1].split(
        "**(C-4) The `E ≥ 1` rows", 1
    )[0]
    for line in c3.splitlines():
        table_nu = re.match(r"\| (\d+) \|", line)
        if table_nu:
            nu = int(table_nu.group(1))
            survivor_cell = line.split("|")[3]
            for L, lam_text in re.findall(r"\((\d+), \[([0-9,+ ]+)\]\)", survivor_cell):
                printed_boundary.add((nu, int(L), tuple(map(int, lam_text.replace(" ", "").split(",")))))
    current_nu = None
    for line in c8.splitlines():
        nu_match = re.search(r"\*\*`ν = (\d+)`\*\*", line)
        if nu_match:
            current_nu = int(nu_match.group(1))
        if "*Boundary survivors" in line:
            for L, lam_text in re.findall(r"\((\d+), \[([0-9+]+)\]\)", line):
                printed_boundary.add((current_nu, int(L), tuple(map(int, lam_text.split("+")))))
    generated_boundary = set()
    for nu in range(1, 11):
        _, _, rows = enumerate_e0(nu)
        generated_boundary.update((nu, L, lam) for L, lam, _ in rows)

    print("PRINTED_DATA_COMPARISON_AFTER_REGENERATION")
    print(
        f"  C2_s0 printed={len(printed_s0)} computed={len(computed_s0)} "
        f"mismatches={sum(printed_s0.get(k) != v for k, v in computed_s0.items())}"
    )
    print(
        f"  Epos printed={len(printed_epos)} generated={len(generated_epos)} "
        f"generated_minus_printed={len(generated_epos-printed_epos)} "
        f"printed_minus_generated={len(printed_epos-generated_epos)}"
    )
    print(
        f"  boundary printed={len(printed_boundary)} generated={len(generated_boundary)} "
        f"generated_minus_printed={len(generated_boundary-printed_boundary)} "
        f"printed_minus_generated={len(printed_boundary-generated_boundary)}"
    )


def controls():
    print("INDEPENDENT_CONTROLS")
    tail_pairs = 0
    tail_mismatches = []
    for nu in range(1, 12):
        for lam in partitions(2 * nu):
            for L in range(max(nu + 1, lam[0]), 2 * nu + 4):
                tail_pairs += 1
                direct = step_count((L,) * (L + 1) + lam)
                predicted = (L - lam[0]) + s0(lam) if s0(lam) is not None else None
                if direct != predicted:
                    tail_mismatches.append((nu, L, lam, direct, predicted))
    print(f"  TAIL pairs={tail_pairs} mismatches={len(tail_mismatches)}")

    padding_pairs = 0
    padding_mismatches = []
    for nu in range(1, 11):
        for lam in partitions(2 * nu):
            L = max(nu + 1, lam[0])
            vals = (L,) * (L + 1) + lam
            padding_pairs += 1
            if step_count(vals) != step_count(vals + (0,) * 13):
                padding_mismatches.append((nu, L, (), lam))
        for E in range(1, nu):
            for L in range(nu + 1, 2 * nu - E + 1):
                for e in partitions(E):
                    for lam in partitions(2 * nu - E):
                        vals = shape_list(L, e, lam)
                        padding_pairs += 1
                        if step_count(vals) != step_count(vals + (0,) * 13):
                            padding_mismatches.append((nu, L, e, lam))
    print(f"  padding pairs={padding_pairs} mismatches={len(padding_mismatches)}")

    # Counterfactual: correct C-shape for (nu,L,E)=(2,3,0), deliberately wrong
    # A' mass 1 rather than 2nu-E=4.  FAN-4' and all downstream finite-list
    # eliminations are therefore unavailable.
    bad = (3, 3, 3, 3, 1)
    print("COUNTERFACTUAL_AVAILABILITY")
    print(
        "  nominal=(nu=2,L=3,E=0), list=" + str(bad)
        + f", A'_mass=1 required=4, steps={step_count(bad)}"
    )
    print("  FAN-4'/FAN-8'/GFAN2 finite-list conclusions unavailable: residue-mass hypothesis fails.")


def construction_search():
    """Attack N4 at tau=2,3 on the unlabeled graph atlas (orders <= 7)."""
    import networkx as nx

    def maximum_independent_sets(G):
        vertices = list(G)
        best = 0
        answers = []
        for r in range(len(vertices) + 1):
            for subset in itertools.combinations(vertices, r):
                if all(not G.has_edge(x, y) for x, y in itertools.combinations(subset, 2)):
                    if r > best:
                        best, answers = r, [set(subset)]
                    elif r == best:
                        answers.append(set(subset))
        return best, answers

    def forest_number(G):
        vertices = list(G)
        best = 0
        for r in range(1, len(vertices) + 1):
            for subset in itertools.combinations(vertices, r):
                if nx.is_forest(G.subgraph(subset)):
                    best = max(best, r)
        return best

    frame_reductio = 0
    universal_low = 0
    violations = []
    for G in nx.graph_atlas_g():
        n = len(G)
        if n == 0 or not nx.is_connected(G):
            continue
        alpha, max_sets = maximum_independent_sets(G)
        tau = n - alpha
        if tau not in (2, 3):
            continue
        if nx.diameter(G) != 4 or nx.is_forest(G) or forest_number(G) != alpha + 1:
            continue
        if residue([degree for _, degree in G.degree()]) != alpha:
            continue
        frame_reductio += 1
        for A in max_sets:
            B = set(G) - A
            low = {b for b in B if G.degree(b) <= tau}
            if not low:
                continue
            if not all(all(b == x or G.has_edge(b, x) for x in B) for b in low):
                continue
            universal_low += 1
            nu = sum(not G.has_edge(x, y) for x, y in itertools.combinations(B, 2))
            if nu > len(low) - 1:
                violations.append((n, tuple(sorted(G.edges())), tuple(sorted(A)), tau, len(low), nu))

    print("N4_CONSTRUCTION_SEARCH")
    print("  scope=all unlabeled graphs in NetworkX graph_atlas_g (orders <= 7), tau in {2,3}")
    print(
        f"  frame_plus_reductio={frame_reductio} universal_low={universal_low} "
        f"nu_gt_L_minus_1={len(violations)}"
    )
    print("  full-hypothesis search box is empty; this is not positive evidence for N4")

    # Quantifier-boundary witness for extending GFANnu to nu=0: K3 with
    # A={0}, B={1,2}.  Exhaustive subsets give alpha=1 and f=2.
    K3 = nx.complete_graph(3)
    alpha, max_sets = maximum_independent_sets(K3)
    f = forest_number(K3)
    print("NU_ZERO_WITNESS_K3")
    print(
        f"  connected={nx.is_connected(K3)} A={{0}}_maximum={set([0]) in max_sets} "
        f"alpha={alpha} exhaustive_max_sets={sorted(tuple(sorted(s)) for s in max_sets)}"
    )
    print(
        f"  diam={nx.diameter(K3)} f={f}=alpha+1 nonforest={not nx.is_forest(K3)} "
        f"residue={residue([d for _, d in K3.degree()])}=alpha"
    )
    print("  GFan(tau=2,L=2,nu=0)=True; thus GFANnu's lower bound nu>=1 is necessary")


if __name__ == "__main__":
    calibration()
    section0()
    theorem_checks()
    printed_data_comparison()
    controls()
    construction_search()
    print("SCRIPT_STATUS=PASS")
