#!/usr/bin/env python3
"""CNF encoder for the Erdos #624 set-mapping cells (n, m, variant).

Variant L  (Lean / erdosproblems convention): f is defined on every subset of [n] = {0..n-1},
           no restriction on f(A); need {f(A) : A subset of Y} = [n] for every |Y| >= m.
Variant EH (Erdos-Hajnal 1968 as restated by Gyarfas): f is defined on proper subsets of [n],
           f(A) in [n] \\ A; need {f(A) : A subset of Y, A proper} = [n] for every |Y| >= m.

By the reduction lemma (README, Lemma R) it suffices, for 0 <= m <= n, to encode f on the sets
of size <= m (proper ones for EH) and the covering condition for |Y| = m.

Variables x(A, c) <-> f(A) = c.  Clauses:
  ALO(A): OR_c x(A,c)                  (c ranges over allowed colours: all for L, c not in A for EH)
  AMO(A): -x(A,c) v -x(A,d)            for allowed c < d
  COV(Y,c): OR_{A subset Y, c allowed for A} x(A,c)     for |Y| = m, c in [n]
Symmetry breaking (optional, see README Lemmas S1/S2):
  --sb 1 : unit clause x(emptyset, 0).               (L: colour relabelling; EH: joint relabelling)
  --sb 2 : sb1 plus a singleton normal form: Lemma S2 (L) or Lemma S2-EH (EH).

usage: encode.py n m {L,EH} [--sb K] > out.cnf
       encode.py --decode n m {L,EH} model.txt > witness.txt   (full table of f, one value per mask)
"""
import sys, itertools, argparse


def popcount(x):
    return bin(x).count("1")


def build(n, m, variant, sb, ansatz=None):
    assert variant in ("L", "EH") and 0 <= m <= n and n >= 1
    full = (1 << n) - 1
    sets = [A for A in range(1 << n) if popcount(A) <= m and not (variant == "EH" and A == full)]
    sets.sort(key=lambda A: (popcount(A), A))
    allowed = {A: [c for c in range(n) if not (variant == "EH" and (A >> c) & 1)] for A in sets}
    var = {}
    for A in sets:
        for c in allowed[A]:
            var[(A, c)] = len(var) + 1
    cls = []
    for A in sets:
        cls.append([var[(A, c)] for c in allowed[A]])
        for c, d in itertools.combinations(allowed[A], 2):
            cls.append([-var[(A, c)], -var[(A, d)]])
    setset = set(sets)
    for Ybits in itertools.combinations(range(n), m):
        Y = sum(1 << i for i in Ybits)
        subs = [A for A in sets if A & ~Y == 0]
        for c in range(n):
            cls.append([var[(A, c)] for A in subs if (A, c) in var])
    if ansatz == "cyc":
        # SAT-search heuristic only (never used for UNSAT claims): f(A+1) = f(A)+1 (mod n) for
        # every set A whose rotation orbit is free (A+k != A for 0<k<n); sets with a nontrivial
        # rotation stabiliser (e.g. the empty set) are left unconstrained, since equivariance
        # would force f(A) = f(A)+k there.  Compatible with both variants.
        rot = lambda A: ((A << 1) | (A >> (n - 1))) & full
        def free(A):
            B = A
            for _ in range(n - 1):
                B = rot(B)
                if B == A:
                    return False
            return True
        for (A, c), v in list(var.items()):
            if free(A):
                cls.append([-v, var[(rot(A), (c + 1) % n)]])
    if sb >= 1:
        cls.append([var[(0, 0)]])
    if sb >= 2:
        cls.extend(singleton_normal_form(n, var) if variant == "L" else singleton_bfs_form(n, var))
    return sets, var, cls


def singleton_normal_form(n, var):
    """Lemma S2 (L variant): WLOG f(empty)=0 and the singleton colour sequence
    s_i = f({i}) satisfies s_0 in {0,1}, s_{i+1} in {s_i, s_i + 1}  (i.e. non-decreasing,
    colours introduced in order without gaps).  Encoded as clauses over x({i}, c)."""
    cls = []
    S = lambda i, c: var[(1 << i, c)]
    # s_0 in {0,1}
    cls.append([S(0, 0), S(0, 1)] if n >= 2 else [S(0, 0)])
    for i in range(n - 1):
        for c in range(n):
            nxt = [S(i + 1, c)] + ([S(i + 1, c + 1)] if c + 1 < n else [])
            cls.append([-S(i, c)] + nxt)
    return cls


def singleton_bfs_form(n, var):
    """Lemma S2-EH (EH variant): WLOG f(empty)=0 and, for every i,
    f({i}) <= 1 + max(i, f({0}), ..., f({i-1}))   (with max over the empty list = i).
    Clause for each i and each colour v >= i+2 allowed at {i}:
        -x({i},v)  v  OR_{j<i, w >= v-1, w allowed at {j}} x({j},w)."""
    cls = []
    for i in range(n):
        for v in range(i + 2, n):
            if ((1 << i), v) not in var:
                continue
            cl = [-var[(1 << i, v)]]
            for j in range(i):
                for w in range(v - 1, n):
                    if ((1 << j), w) in var:
                        cl.append(var[(1 << j, w)])
            cls.append(cl)
    return cls


def write_cnf(nvars, cls, out):
    out.write("p cnf %d %d\n" % (nvars, len(cls)))
    for c in cls:
        out.write(" ".join(map(str, c)) + " 0\n")


def decode(n, m, variant, model_path, sb):
    sets, var, cls = build(n, m, variant, sb)
    true = set()
    for line in open(model_path):
        if line.startswith("v"):
            true.update(int(t) for t in line.split()[1:] if int(t) > 0)
    inv = {v: k for k, v in var.items()}
    f = {}
    for v in true:
        if v in inv:
            A, c = inv[v]
            assert A not in f, "AMO violated in model"
            f[A] = c
    full = (1 << n) - 1
    rows = []
    for A in range(1 << n):
        if variant == "EH" and A == full:
            rows.append("-")           # f undefined on the full set
        elif A in f:
            rows.append(str(f[A]))
        else:                          # sets larger than m: any legal value (Lemma R)
            assert popcount(A) > m
            rows.append(str(0 if variant == "L" else min(c for c in range(n) if not (A >> c) & 1)))
    sys.stdout.write("# erdos624 witness n=%d m=%d variant=%s ; line k (k=0..2^n-1) = f(mask k), "
                     "bit i of k <-> element i ; '-' = undefined\n" % (n, m, variant))
    sys.stdout.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--decode", action="store_true")
    ap.add_argument("--sb", type=int, default=0)
    ap.add_argument("--ansatz", default=None, help="'cyc': cyclic-equivariance ansatz (SAT search only)")
    ap.add_argument("n", type=int)
    ap.add_argument("m", type=int)
    ap.add_argument("variant")
    ap.add_argument("model", nargs="?")
    a = ap.parse_args()
    if a.decode:
        decode(a.n, a.m, a.variant, a.model, a.sb)
    else:
        sets, var, cls = build(a.n, a.m, a.variant, a.sb, a.ansatz)
        write_cnf(len(var), cls, sys.stdout)
