#!/usr/bin/env python3
"""Independent witness checker for Erdos #624 cells.  Written from scratch; imports nothing
from ../src.  It reads a full table of f and checks the *literal* definition:

  L : f : P([n]) -> [n] total;  for EVERY Y subset [n] with |Y| >= m,
      {f(A) : A subset Y} = [n].
  EH: f : P([n]) \\ {[n]} -> [n] total with f(A) not in A;  for EVERY Y with |Y| >= m,
      {f(A) : A subset Y, A != [n]} = [n].

Two independent evaluation methods are used and must agree:
  (1) subset-closure recursion  img(Y) = {f(Y)} u U_{i in Y} img(Y - i)   (all 2^n sets Y)
  (2) direct enumeration of all submasks A of Y for every Y with |Y| = m, and for every Y
      with |Y| >= m when 3^n <= 2e7.
Witness format: '#' comment lines, then 2^n lines; line k holds f(k) where bit i of k means
element i is in the set; '-' marks the undefined value at the full set (EH only).
usage: check_witness.py n m {L,EH} witness_file[.gz]
"""
import sys, gzip


def load(path, n, variant):
    op = gzip.open if path.endswith(".gz") else open
    vals = []
    with op(path, "rt") as fh:
        for line in fh:
            t = line.strip()
            if not t or t.startswith("#"):
                continue
            vals.append(t)
    if len(vals) != 2 ** n:
        raise SystemExit("FAIL: expected %d table entries, got %d" % (2 ** n, len(vals)))
    top = 2 ** n - 1
    f = []
    for k, t in enumerate(vals):
        if variant == "EH" and k == top:
            if t != "-":
                raise SystemExit("FAIL: EH table must have '-' at the full set")
            f.append(None)
            continue
        v = int(t)
        if not 0 <= v < n:
            raise SystemExit("FAIL: value out of range at mask %d" % k)
        if variant == "EH" and (k >> v) & 1:
            raise SystemExit("FAIL: EH condition f(A) not in A violated at mask %d" % k)
        f.append(v)
    return f


def method_closure(f, n):
    """img[Y] as a bitmask of colours, via img(Y) = {f(Y)} u U_i img(Y - i)."""
    img = [0] * (2 ** n)
    for Y in range(2 ** n):           # increasing order: every Y - i < Y already done
        acc = 0 if f[Y] is None else (1 << f[Y])
        rest = Y
        while rest:
            low = rest & -rest
            acc |= img[Y ^ low]
            rest ^= low
        img[Y] = acc
    return img


def method_direct(f, n, Y):
    seen = set()
    A = Y
    while True:
        if f[A] is not None:
            seen.add(f[A])
        if A == 0:
            break
        A = (A - 1) & Y
    return seen


def mutation_selftest(f, n, m, variant, trials=40):
    """Liveness: flip single values of f on sets of size <= m; count how many flips the
    closure method detects (a checker that never fails would detect none)."""
    import random
    rnd = random.Random(624)
    full_colours = (1 << n) - 1
    small = [A for A in range(2 ** n) if bin(A).count("1") <= m and f[A] is not None]
    detected = 0
    for _ in range(trials):
        A = rnd.choice(small)
        choices = [c for c in range(n) if c != f[A] and not (variant == "EH" and (A >> c) & 1)]
        if not choices:
            continue
        g = list(f)
        g[A] = rnd.choice(choices)
        img = method_closure(g, n)
        if any(img[Y] != full_colours for Y in range(2 ** n) if bin(Y).count("1") >= m):
            detected += 1
    return detected, trials


def main():
    n, m, variant, path = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]
    assert variant in ("L", "EH")
    f = load(path, n, variant)
    full_colours = (1 << n) - 1
    img = method_closure(f, n)
    size = [bin(Y).count("1") for Y in range(2 ** n)]
    bad1 = [Y for Y in range(2 ** n) if size[Y] >= m and img[Y] != full_colours]
    exhaustive = 3 ** n <= 2 * 10 ** 7
    targets = [Y for Y in range(2 ** n) if (size[Y] >= m if exhaustive else size[Y] == m)]
    bad2 = [Y for Y in targets if method_direct(f, n, Y) != set(range(n))]
    # agreement between the two methods on the sets checked by both
    for Y in targets:
        assert (img[Y] == full_colours) == (method_direct(f, n, Y) == set(range(n))), Y
    nY = sum(1 for Y in range(2 ** n) if size[Y] >= m)
    print("n=%d m=%d variant=%s : closure method checked %d sets Y (|Y|>=m), failures %d; "
          "direct method checked %d sets (%s), failures %d"
          % (n, m, variant, nY, len(bad1), len(targets),
             "all |Y|>=m" if exhaustive else "|Y|=m", len(bad2)))
    if bad1 or bad2:
        print("RESULT: FAIL")
        sys.exit(1)
    if "--selftest" in sys.argv:
        d, t = mutation_selftest(f, n, m, variant)
        print("mutation self-test: %d of %d single-value mutations detected as failures" % (d, t))
    print("RESULT: PASS  (f witnesses (%d,%d)_%s, hence H_%s(%d) <= %d)" % (n, m, variant, variant, n, m))


if __name__ == "__main__":
    main()
