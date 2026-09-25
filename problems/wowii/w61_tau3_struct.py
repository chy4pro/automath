#!/usr/bin/env python3
"""
WOWII-61, tau = 3: numerical verification of the STRUCTURAL BACKBONE of the
owner-w61 round-2 case decomposition, checked on every member of the
exhaustive parametric family (Lemma P) inside the multiplicity box.

Structural claims (each is proved by hand in draft sec.7.3; here they are
stress-tested on every tau=3 hard-core graph in the box):

 C0  e_B <= 2                                          (Observation R1)
 C1  e_B = 0  =>  every b in B has deg(b) >= 2
 C2  e_B = 1  =>  every b in B has deg(b) >= 3
 C3  e_B = 2  =>  every b in B has deg(b) >= 3, AND the two endpoints of the
                  path G[B] have deg >= 4  (hence k := #{b : deg b >= 4} >= 2)
 C4  k = 0  (all B-degrees <= 3)  =>  alpha <= 6   (so this case is finite)
 C5  the joint distribution of (e_B, k) -- which cells are non-empty

Also: explicit Havel-Hakimi traces of the one-parameter families that the
case analysis isolates, over a long parameter range.

Usage: python3 w61_tau3_struct.py [MAXMULT]     (default 4)
"""
import sys
from itertools import product
sys.path.insert(0, "$HOME/workspace/claudecode/automath/problems/wowii")
from w61_tau3 import analyse, EB_PATTERNS, hh_trace


def main():
    MAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    fail = {c: 0 for c in ("C0", "C1", "C2", "C3a", "C3b", "C4")}
    wit = {}
    cells = {}
    hard = 0
    for name, eb in EB_PATTERNS:
        # centre / endpoints of G[B] when e_B = 2 (pattern [(0,1),(1,2)])
        for mu in product(range(MAX + 1), repeat=7):
            r = analyse(list(mu), eb)
            if r is None:
                continue
            hard += 1
            d = r["degB_raw"]
            din = r["degB_in"]
            eB = r["eb"]
            k = sum(1 for x in d if x >= 4)
            cells[(eB, k)] = cells.get((eB, k), 0) + 1
            if eB > 2:
                fail["C0"] += 1
                wit.setdefault("C0", r)
            if eB == 0 and min(d) < 2:
                fail["C1"] += 1
                wit.setdefault("C1", r)
            if eB == 1 and min(d) < 3:
                fail["C2"] += 1
                wit.setdefault("C2", r)
            if eB == 2:
                if min(d) < 3:
                    fail["C3a"] += 1
                    wit.setdefault("C3a", r)
                ends = [b for b in range(3) if din[b] == 1]      # path endpoints
                if any(d[b] < 4 for b in ends):
                    fail["C3b"] += 1
                    wit.setdefault("C3b", r)
            if k == 0 and r["alpha"] > 6:
                fail["C4"] += 1
                wit.setdefault("C4", r)
    print(f"[struct] MAXMULT={MAX}  tau=3 hard-core instances checked = {hard}")
    print(f"[struct] failures: {fail}")
    print(f"[struct] (e_B,k) cells occupied: "
          f"{ {k: v for k, v in sorted(cells.items())} }")
    for k, v in wit.items():
        print("  WITNESS", k, v)

    # ---- the one-parameter families isolated by the case analysis ----
    print("\n[families] explicit HH traces (s must be >= 4 in every row)")

    def show(tag, degs, n_expect=None):
        heads, res = hh_trace(degs)
        s = len(heads)
        m = sum(degs) // 2
        ok = "OK" if s >= 4 else "*** s=3 : COUNTEREXAMPLE ***"
        return s, m, sum(heads[:3]), ok

    bad = 0
    # F1 : k=1, e_B=1, sub-case (II)   [X,3,3,3,3,1^(X-2)]
    for X in range(4, 60):
        degs = [X, 3, 3, 3, 3] + [1] * (X - 2)
        s, m, s3, ok = show("F1", degs)
        if s < 4:
            bad += 1
            print("F1", X, degs, s, ok)
    print(f"  F1 (k=1,e_B=1): X=4..59 tested, violations={bad}")

    # F2 : k=1, e_B=0, p=1        [nx+3, 3,3,3, 2,2,2, 1^nx]
    bad = 0
    for nx in range(1, 60):
        degs = [nx + 3, 3, 3, 3, 2, 2, 2] + [1] * nx
        s, m, s3, ok = show("F2", degs)
        if s < 4:
            bad += 1
            print("F2", nx, degs, s, ok)
    print(f"  F2 (k=1,e_B=0,p=1): n_x=1..59 tested, violations={bad}")

    # F2b : k=1, e_B=0, p=2      [X,3,3,3,3,2,1^(X-2)]
    bad = 0
    for X in range(4, 60):
        degs = [X, 3, 3, 3, 3, 2] + [1] * (X - 2)
        s, m, s3, ok = show("F2b", degs)
        if s < 4:
            bad += 1
            print("F2b", X, degs, s, ok)
    print(f"  F2b (k=1,e_B=0,p=2): X=4..59 tested, violations={bad}")

    # F0 : k=0 (unique sequence)
    s, m, s3, ok = show("F0", [3, 3, 3, 3, 3, 2, 1])
    print(f"  F0 (k=0, unique seq [3,3,3,3,3,2,1]): s={s} m={m} D1+D2+D3={s3} {ok}")

    # F3 : k=2, e_B=2, z = centre     [X, Y, 3, 3, 2^c1, 1^(a1+b1)]
    bad = 0
    tot = 0
    for a1 in range(1, 12):
        for b1 in range(1, 12):
            for c1 in range(1, 12):
                X, Y = a1 + c1 + 2, b1 + c1 + 2
                if X < 4 or Y < 4:
                    continue
                degs = sorted([X, Y, 3, 3] + [2] * c1 + [1] * (a1 + b1),
                              reverse=True)
                tot += 1
                s, m, s3, ok = show("F3", degs)
                if s < 4:
                    bad += 1
                    print("F3", a1, b1, c1, degs, s, ok)
    print(f"  F3 (k=2,e_B=2,centre): {tot} parameter triples, violations={bad}")


if __name__ == "__main__":
    main()
