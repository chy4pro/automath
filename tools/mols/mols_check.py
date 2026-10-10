#!/usr/bin/env python3
"""Exact checker for k mutually orthogonal Latin squares of order n.
Usage: mols_check.py FILE.json [k]   (k default 4)
Input JSON: {"n": N, "squares": [ [[...],...], ... ]}
Exit 0 on accept, 1 on reject, 2 on usage/IO error. Standard library only."""
import sys, json, hashlib, time


def check(data, k):
    """Return (ok, reason)."""
    if not isinstance(data, dict) or "n" not in data or "squares" not in data:
        return False, "malformed: need keys n, squares"
    n = data["n"]
    if type(n) is not int or n < 1:
        return False, "n is not a positive integer"
    sq = data["squares"]
    if not isinstance(sq, list) or len(sq) != k:
        return False, "wrong number of squares: expected %d" % k
    for s, A in enumerate(sq):
        if not isinstance(A, list) or len(A) != n:
            return False, "square %d: wrong shape (not n rows)" % s
        for i, row in enumerate(A):
            if not isinstance(row, list) or len(row) != n:
                return False, "square %d row %d: wrong shape" % (s, i)
            for j, v in enumerate(row):
                if type(v) is not int:
                    return False, "square %d cell (%d,%d): non-integer entry %r" % (s, i, j, v)
                if v < 0 or v >= n:
                    return False, "square %d cell (%d,%d): out-of-range symbol %d" % (s, i, j, v)
    for s, A in enumerate(sq):
        for i in range(n):
            if len(set(A[i])) != n:
                return False, "square %d row %d: repeated symbol (not Latin)" % (s, i)
        for j in range(n):
            if len({A[i][j] for i in range(n)}) != n:
                return False, "square %d column %d: repeated symbol (not Latin)" % (s, j)
    for a in range(k):
        for b in range(a + 1, k):
            seen = [False] * (n * n)
            A, B = sq[a], sq[b]
            for i in range(n):
                for j in range(n):
                    p = n * A[i][j] + B[i][j]
                    if seen[p]:
                        return False, "squares %d,%d: not orthogonal (repeated pair (%d,%d))" % (a, b, A[i][j], B[i][j])
                    seen[p] = True
    return True, "ok"


def main(argv):
    if len(argv) < 2:
        print("usage: mols_check.py FILE.json [k]", file=sys.stderr)
        return 2
    try:
        k = int(argv[2]) if len(argv) > 2 else 4
        raw = open(argv[1], "rb").read()
        h = hashlib.sha256(raw).hexdigest()
        data = json.loads(raw)
    except Exception as e:
        print("REJECT (unreadable input: %s)" % e)
        return 2
    t = time.perf_counter()
    ok, why = check(data, k)
    dt = time.perf_counter() - t
    n = data.get("n") if isinstance(data, dict) else None
    print("%s k=%d n=%s: %s  sha256=%s  time=%.3fs" % ("ACCEPT" if ok else "REJECT", k, n, why, h, dt))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
