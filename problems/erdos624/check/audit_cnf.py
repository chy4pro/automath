#!/usr/bin/env python3
"""Independent audit of a CNF used for an UNSAT certificate.  Imports nothing from ../src.

It rebuilds, directly from the definitions in the README, the set of clauses that the CNF for
cell (n, m, variant) with symmetry-breaking level sb must contain, and checks that the file's
clause set is EXACTLY that set (no extra clause, no missing clause, no duplicate).

Variable numbering specification (README, section "CNF"): the boolean x(A, c) means f(A) = c.
Sets A range over subsets of {0..n-1} with |A| <= m (EH: A != full set), listed by increasing
size and, within a size, by increasing bitmask value; for each A the allowed colours c
(L: all of 0..n-1; EH: c not in A) are listed increasingly; variables get ids 1, 2, 3, ... in
this order.

Clause families (all must be consequences of 'f is a valid (n,m) set map in normal form'):
  ALO(A)     OR_{c allowed} x(A,c)
  AMO(A,c,d) -x(A,c) v -x(A,d)                  c < d allowed
  COV(Y,c)   OR_{A subset Y, c allowed at A} x(A,c)      |Y| = m (EH & m = n: A != full)
  sb>=1      x(empty, 0)
  sb>=2, L   x({0},0) v x({0},1);  -x({i},c) v x({i+1},c) [v x({i+1},c+1) if c+1<n]
  sb>=2, EH  -x({i},v) v OR_{j<i, w>=v-1, w allowed at {j}} x({j},w)      for v >= i+2
usage: audit_cnf.py n m variant sb file.cnf[.gz]
"""
import sys, gzip
from itertools import combinations


def main():
    n, m, variant, sb, path = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5]
    top = frozenset(range(n))
    # --- variable ids per specification, using frozensets instead of bitmasks
    ids = {}
    nxt = 1
    for k in range(m + 1):
        layer = [frozenset(t) for t in combinations(range(n), k)]
        layer.sort(key=lambda S: sum(2 ** e for e in S))
        for A in layer:
            if variant == "EH" and A == top:
                continue
            for c in range(n):
                if variant == "EH" and c in A:
                    continue
                ids[(A, c)] = nxt
                nxt += 1
    nvars = nxt - 1
    domain = sorted({A for (A, _) in ids}, key=lambda S: (len(S), sorted(S)))
    X = lambda A, c: ids[(frozenset(A), c)]
    ok = lambda A, c: (frozenset(A), c) in ids
    expected = []
    for A in domain:
        cols = [c for c in range(n) if ok(A, c)]
        expected.append(frozenset(X(A, c) for c in cols))
        for i in range(len(cols)):
            for j in range(i + 1, len(cols)):
                expected.append(frozenset((-X(A, cols[i]), -X(A, cols[j]))))
    for Y in combinations(range(n), m):
        subs = [frozenset(S) for k in range(m + 1) for S in combinations(Y, k)]
        for c in range(n):
            expected.append(frozenset(X(S, c) for S in subs if ok(S, c)))
    if sb >= 1:
        expected.append(frozenset([X((), 0)]))
    if sb >= 2 and variant == "L":
        expected.append(frozenset([X((0,), 0), X((0,), 1)]) if n >= 2 else frozenset([X((0,), 0)]))
        for i in range(n - 1):
            for c in range(n):
                lits = [-X((i,), c), X((i + 1,), c)]
                if c + 1 < n:
                    lits.append(X((i + 1,), c + 1))
                expected.append(frozenset(lits))
    if sb >= 2 and variant == "EH":
        for i in range(n):
            for v in range(i + 2, n):
                if not ok((i,), v):
                    continue
                lits = [-X((i,), v)] + [X((j,), w) for j in range(i) for w in range(v - 1, n) if ok((j,), w)]
                expected.append(frozenset(lits))
    # --- read the file
    op = gzip.open if path.endswith(".gz") else open
    got, header = [], None
    with op(path, "rt") as fh:
        cur = []
        for line in fh:
            if line.startswith("c"):
                continue
            if line.startswith("p"):
                header = tuple(int(t) for t in line.split()[2:4])
                continue
            for t in line.split():
                v = int(t)
                if v == 0:
                    got.append(frozenset(cur)); cur = []
                else:
                    cur.append(v)
    problems = []
    if header != (nvars, len(expected)):
        problems.append("header %s != expected (%d, %d)" % (header, nvars, len(expected)))
    if len(set(expected)) != len(expected):
        problems.append("expected family has duplicate clauses (spec issue)")
    if len(set(got)) != len(got):
        problems.append("file has duplicate clauses")
    extra = set(got) - set(expected)
    missing = set(expected) - set(got)
    if extra:
        problems.append("%d clauses in file not in the specification" % len(extra))
    if missing:
        problems.append("%d specified clauses missing from file" % len(missing))
    print("audit n=%d m=%d variant=%s sb=%d: vars=%d clauses expected=%d file=%d"
          % (n, m, variant, sb, nvars, len(expected), len(got)))
    if problems:
        print("AUDIT: FAIL: " + "; ".join(problems))
        sys.exit(1)
    print("AUDIT: PASS (file clause set == specification clause set)")


if __name__ == "__main__":
    main()
