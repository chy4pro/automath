#!/usr/bin/env python3
"""Independent re-check of P16's bump-contour family (Erdős #1212 round 4).
For M = 15L+7, square with corners (0,0),(M,0),(M,M),(0,M); on each side L centres u_a = 11+15a
are replaced by an outward (bit 0) or inward (bit 1) point. Checks, without shapely:
  n = 4M, all vertices distinct, every step has sup-norm 1, no two edges cross (diagonal crossings),
  turns = 12L+4, winding number about (M/2,M/2) is +-1, outward pts == (2,2) mod 3, inward == (1,1) mod 5.
Usage: python3 bump_contours.py [LMAX]   (default 4 -> 69904 patterns)"""
import sys
from itertools import product

def make_contour(L, bits):
    M = 15 * L + 7
    centres = [11 + 15 * a for a in range(L)]
    ch = [dict(zip(centres, bits[s * L:(s + 1) * L])) for s in range(4)]
    bottom = [(x, (-1 if ch[0][x] == 0 else 1) if x in ch[0] else 0) for x in range(M + 1)]
    right = [((M + 1 if ch[1][y] == 0 else M - 1) if y in ch[1] else M, y) for y in range(M + 1)]
    top = [(x, (M + 1 if ch[2][x] == 0 else M - 1) if x in ch[2] else M) for x in range(M, -1, -1)]
    left = [((-1 if ch[3][y] == 0 else 1) if y in ch[3] else 0, y) for y in range(M, -1, -1)]
    return M, bottom[:-1] + right[:-1] + top[:-1] + left[:-1]

def winding(v, px, py):
    # signed crossing count of the horizontal ray from (px,py) to the right
    w = 0
    n = len(v)
    for i in range(n):
        x1, y1 = v[i]; x2, y2 = v[(i + 1) % n]
        if (y1 <= py) != (y2 <= py):
            xi = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if xi > px:
                w += 1 if y2 > y1 else -1
    return w

def audit(L, bits):
    M, v = make_contour(L, bits)
    n = len(v)
    assert n == 4 * M, "length"
    assert len(set(v)) == n, "distinct"
    dirs = []
    for i in range(n):
        x1, y1 = v[i]; x2, y2 = v[(i + 1) % n]
        d = (x2 - x1, y2 - y1)
        assert max(abs(d[0]), abs(d[1])) == 1, "step"
        dirs.append(d)
    # diagonal-edge crossing check: two diagonal unit edges cross iff they are the two diagonals of one unit square
    diag = {}
    for i in range(n):
        x1, y1 = v[i]; x2, y2 = v[(i + 1) % n]
        if x1 != x2 and y1 != y2:
            sq = (min(x1, x2), min(y1, y2))
            kind = (x2 - x1) * (y2 - y1)  # +1 main diagonal, -1 anti-diagonal
            assert diag.get(sq, kind) == kind, "crossing"
            diag[sq] = kind
    assert sum(dirs[i] != dirs[i - 1] for i in range(n)) == 12 * L + 4, "turns"
    assert abs(winding(v, M / 2 + 0.25, M / 2 + 0.25)) == 1, "winding"
    bumps = [(x, y) for x, y in v if not ((x in (0, M) and 0 <= y <= M) or (y in (0, M) and 0 <= x <= M))]
    assert len(bumps) == 4 * L, "bumps"
    for x, y in bumps:
        if x < 0 or x > M or y < 0 or y > M:
            assert (x % 3, y % 3) == (2, 2), "mod3"
        else:
            assert (x % 5, y % 5) == (1, 1), "mod5"
    return M

if __name__ == "__main__":
    LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    total = 0
    for L in range(1, LMAX + 1):
        M = None
        for bits in product((0, 1), repeat=4 * L):
            M = audit(L, bits); total += 1
        print(f"L={L} M={M} n={4*M} k={12*L+4}: {2**(4*L)} patterns OK")
    print(f"{total} patterns: OK")
