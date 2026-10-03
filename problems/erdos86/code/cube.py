"""Basic hypercube utilities and exhaustive enumeration of C4-free subgraphs of Q3, Q4."""
import itertools, numpy as np

def cube(k):
    edges = []
    for v in range(1 << k):
        for i in range(k):
            if not (v >> i) & 1:
                edges.append((v, v | (1 << i), i))
    eidx = {(a, b): t for t, (a, b, _) in enumerate(edges)}
    sq = []
    for v in range(1 << k):
        for i in range(k):
            for j in range(i + 1, k):
                if not (v >> i) & 1 and not (v >> j) & 1:
                    a, b, c, d = v, v | (1 << i), v | (1 << j), v | (1 << i) | (1 << j)
                    sq.append((eidx[(a, b)], eidx[(a, c)], eidx[(b, d)], eidx[(c, d)]))
    return edges, eidx, sq

def c4free_masks(k):
    """all C4-free edge masks of Q_k (k<=3 brute force)"""
    edges, eidx, sq = cube(k)
    m = len(edges)
    sqm = [sum(1 << e for e in s) for s in sq]
    out = [x for x in range(1 << m) if all((x & s) != s for s in sqm)]
    return out

if __name__ == "__main__":
    for k in (2, 3):
        edges, eidx, sq = cube(k)
        L = c4free_masks(k)
        mx = max(bin(x).count("1") for x in L)
        ext = [x for x in L if bin(x).count("1") == mx]
        print(k, "edges", len(edges), "#C4free", len(L), "max", mx, "#extremal(labelled)", len(ext))
