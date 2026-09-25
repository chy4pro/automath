#!/usr/bin/env python3
"""ROUND 6-AE: the RANK-TWO ideal for Kourovka 16.95 at n = 4 (registry R6.77), own encoder.
Every A in GL(4,F) with ALL 24 A P_sigma non-cyclic normalises (scale by an eigenvalue of geometric
multiplicity >= 2, which exists since A itself is non-cyclic) to A = I + U W^T with U, W in F^{4x2}.
A P_sigma = P_sigma + U (P_sigma^T W)^T is non-cyclic iff for some t in the algebraic closure
rank(A P_sigma - t I) <= 2 iff all sixteen 3x3 minors of (A P_sigma - t I) vanish; t is a FREE variable
t_sigma (a rank-two update can lower rank(P_sigma - tI) from 4 to 2, so t need not be an eigenvalue).
Ideal J = < c*z - 1, minors(A P_sigma - t_sigma I) for the 23 non-identity sigma > in
GF(p)[u11..u42, w11..w42, z, t_1..t_23]; J unit  <=>  16.95 holds for n = 4 over every field of char p.
Controls: (i) rank-one specialisation (second columns of U, W set to 0) restricted to a permutation set
known to be simultaneously bad for some rank-one A (identity + six transpositions + the bad set of
P_(24)) must be NON-unit; (ii) the rank-one full 23-permutation ideal must be UNIT (rank one is
certified for 16.95, registry R6.42).  Usage: round6_r2_ideal.py <p> <cap_seconds> [--controls-only] [--write-only]"""
import sys, os, itertools, time, subprocess
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()
p = int(sys.argv[1]); cap = int(sys.argv[2]) if len(sys.argv) > 2 else 3600
controls_only = "--controls-only" in sys.argv; write_only = "--write-only" in sys.argv
# --chart: WLOG rank W = 2 (rank <= 1 is the rank-one stratum, certified separately); conjugating by a
# permutation moves an invertible 2x2 minor of W to rows 1,2 and R = U W^T = (U G)(W G^-T)^T lets us take
# that block = I_2.  So W = [[1,0],[0,1],[w31,w32],[w41,w42]]: 36 variables instead of 40.
chart = "--chart" in sys.argv
OUT = "$HOME/workspace/claudecode/automath/engine/harvest/k1695_r6_r2ideal"
os.makedirs(OUT, exist_ok=True)
MS = os.path.expanduser("~/.local/bin/msolve"); ENV = dict(os.environ, DYLD_LIBRARY_PATH=os.path.expanduser("~/.local/lib"))
n = 4
perms = [s for s in itertools.permutations(range(n)) if s != tuple(range(n))]
U = sp.Matrix(n, 2, sp.symbols("u11 u12 u21 u22 u31 u32 u41 u42"))
W = sp.Matrix(n, 2, sp.symbols("w11 w12 w21 w22 w31 w32 w41 w42"))
z = sp.Symbol("z")
CHART = {W[0, 0]: 1, W[0, 1]: 0, W[1, 0]: 0, W[1, 1]: 1} if chart else {}
def perm_matrix(s): return sp.Matrix(n, n, lambda i, j: 1 if s[j] == i else 0)
A = sp.eye(n) + U * W.T
c = sp.expand((sp.eye(2) + W.T * U).det())       # det(I + U W^T) = det(I_2 + W^T U)
def minors_for(s, t, rank1=False):
    P = perm_matrix(s)
    M = A * P - t * sp.eye(n)
    if rank1: M = M.subs({U[i, 1]: 0 for i in range(n)}).subs({W[i, 1]: 0 for i in range(n)})
    elif chart: M = M.subs(CHART)
    out = []
    for rows in itertools.combinations(range(n), 3):
        for cols in itertools.combinations(range(n), 3):
            m = sp.expand(M.extract(list(rows), list(cols)).det())
            if m != 0: out.append(m)
    return out
def reduce_mod(expr, VARS):
    if p == 0: return expr
    P = sp.Poly(expr, *VARS)
    terms = {m: (int(cf) % p) for m, cf in P.terms() if int(cf) % p}
    return sp.Poly(terms, *VARS).as_expr() if terms else sp.Integer(0)
def run_ideal(tag, subset, rank1, cap_s):
    ts = {s: sp.Symbol("t%d" % k) for k, s in enumerate(perms)}
    VARS = [v for v in U] + [v for v in W] + [z] + [ts[s] for s in subset]
    if rank1: VARS = [U[i, 0] for i in range(n)] + [W[i, 0] for i in range(n)] + [z] + [ts[s] for s in subset]
    cc = c.subs({U[i, 1]: 0 for i in range(n)}).subs({W[i, 1]: 0 for i in range(n)}) if rank1 else c
    if chart and not rank1:
        cc = cc.subs(CHART); VARS = [v for v in VARS if v not in CHART]
    body = [sp.expand(cc * z - 1)]
    for s in subset: body += minors_for(s, ts[s], rank1)
    lines = []
    for g in body:
        r = reduce_mod(g, VARS)
        if r != 0: lines.append(str(r).replace("**", "^"))
    path = OUT + "/r2_%s%s_p%d.ms" % (tag, "_chart" if (chart and not rank1) else "", p)
    open(path, "w").write(",".join(str(v) for v in VARS) + "\n" + str(p) + "\n" + ",\n".join(lines) + "\n")
    print("  wrote %s: %d generators, %d variables, %d bytes  [%.0fs]" % (path, len(lines), len(VARS), os.path.getsize(path), time.time()-T0))
    if write_only: return None
    out = path + ".gb"
    try:
        subprocess.run([MS, "-g", "2", "-v", "1", "-t", "1", "-f", path, "-o", out], env=ENV, capture_output=True, text=True, timeout=cap_s)
    except subprocess.TimeoutExpired:
        print("  %s: CAPPED at %d s" % (tag, cap_s)); return None
    basis = "".join(l for l in open(out) if not l.startswith("#")).replace("\n", "").replace(" ", "")
    un = basis.startswith("[1]")
    print("  %s: %s  (basis starts %s)  [%.0fs]" % (tag, "UNIT IDEAL [1]" if un else "NOT unit (%d chars)" % len(basis), basis[:50], time.time()-T0))
    return un
def ctype(s):
    seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))
def compose(s, t): return tuple(s[t[j]] for j in range(n))
tau = (0, 3, 2, 1)
bad_tau = [s for s in perms if ctype(compose(tau, s)) != (4,)]   # bad set of A = P_tau (rank-one, 17 non-identity permutations)
print("controls (rank-one specialisation):")
r1 = run_ideal("ctrl_rank1_badPtau", bad_tau, True, 600)
print("  expected NON-unit (P_(24) realises this bad set):", "OK" if r1 is False else "MISMATCH/none")
r2 = run_ideal("ctrl_rank1_all23", perms, True, 1800)
print("  expected UNIT (rank one certified for 16.95):", "OK" if r2 is True else "MISMATCH/none")
if controls_only: sys.exit(0)
print("main rank-two ideal, characteristic %d:" % p)
res = run_ideal("main", perms, False, cap)
print("RESULT char %d: %s" % (p, "UNIT => 16.95 at n=4 in characteristic %d (pending re-run)" % p if res else ("NOT UNIT => candidate counterexample point (solve with -P 1)" if res is False else "CAPPED/UNRESOLVED")))
print("done %.0fs" % (time.time()-T0))
