#!/usr/bin/env python3
"""ROUND 6-S: the (S')_4 ideal (WIDE direction B2).  Variables a_{ij} (16), generators
K_{i,sigma}(A) = det[e_i, M e_i, M^2 e_i, M^3 e_i], M = A P_sigma (columns permuted), for all i and all
sigma in S_4 (96 sextics), plus the Rabinowitsch generator 1 - t*det(A).  Unit ideal over GF(p)
<=> (S')_4 holds over every field of characteristic p <=> Kourovka 16.95 at n = 4 there, all at once.
Writes msolve input files for the requested characteristics; runs msolve under a wall cap.
Usage: round6_sprime4_ideal.py <p> [cap_seconds]"""
import sys, os, itertools, time, subprocess
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()
p = int(sys.argv[1]); cap = int(sys.argv[2]) if len(sys.argv) > 2 else 1800
OUT = "$HOME/workspace/claudecode/automath/engine/harvest/k1695_r6_sprime4"
os.makedirs(OUT, exist_ok=True)
n = 4
syms = sp.symbols(" ".join("a%d%d" % (i, j) for i in range(n) for j in range(n)))
A = sp.Matrix(n, n, syms)
t = sp.Symbol("t")
gens = []
cache = OUT + "/gens_Z.txt"
if os.path.exists(cache):
    gens = [sp.sympify(l, locals=dict(zip([str(s) for s in syms], syms))) for l in open(cache) if l.strip()]
    print("loaded %d cached generators" % len(gens))
else:
    for s in itertools.permutations(range(n)):
        P = sp.Matrix(n, n, lambda i, j: 1 if s[j] == i else 0)
        M = A * P
        for i in range(n):
            e = sp.zeros(n, 1); e[i] = 1
            cols = [e]; v = e
            for _ in range(n-1):
                v = M * v; cols.append(v)
            K = sp.expand(sp.Matrix.hstack(*cols).det())
            gens.append(K)
    with open(cache, "w") as f:
        for g in gens: f.write(str(g) + "\n")
    print("generated %d Krylov determinants over Z  [%.0fs]" % (len(gens), time.time()-T0))
gens_nz = [g for g in gens if g != 0]
print("nonzero: %d; degrees: %s" % (len(gens_nz), sorted({sp.Poly(g, *syms).total_degree() for g in gens_nz})))
detA = sp.expand(A.det())
rab = sp.expand(1 - t*detA)
VARS = list(syms) + [t]
def reduce_mod(expr, p):
    if p == 0: return expr
    P = sp.Poly(expr, *VARS)
    terms = {m: (int(c) % p) for m, c in P.terms() if int(c) % p}
    return sp.Poly(terms, *VARS).as_expr() if terms else sp.Integer(0)
body = []
for g in gens_nz + [rab]:
    r = reduce_mod(g, p)
    if r != 0: body.append(str(r).replace("**", "^"))
path = OUT + "/sprime4_p%d.ms" % p
open(path, "w").write(",".join(str(v) for v in VARS) + "\n" + str(p) + "\n" + ",\n".join(body) + "\n")
print("wrote %s: %d generators in %d variables  [%.0fs]" % (path, len(body), len(VARS), time.time()-T0))
if cap == 0:
    print("cap 0: input written only (for the GCP runner); done %.0fs" % (time.time()-T0)); sys.exit(0)
MS = os.path.expanduser("~/.local/bin/msolve")
env = dict(os.environ, DYLD_LIBRARY_PATH=os.path.expanduser("~/.local/lib"))
out = path + ".gb"
t1 = time.time()
try:
    r = subprocess.run([MS, "-g", "2", "-v", "1", "-t", "1", "-f", path, "-o", out], env=env, capture_output=True, text=True, timeout=cap)
    basis = "".join(l for l in open(out) if not l.startswith("#")).replace("\n", "").replace(" ", "")
    print("msolve char %d: %s  (basis starts %s)  [%.0fs]" % (p, "UNIT IDEAL [1]" if basis.startswith("[1]") else "NOT unit (%d chars)" % len(basis), basis[:30], time.time()-t1))
    open(OUT + "/sprime4_p%d.log" % p, "w").write(r.stdout[-4000:] + "\n" + r.stderr[-2000:])
except subprocess.TimeoutExpired:
    print("msolve char %d: CAPPED at %d s" % (p, cap))
print("done %.0fs" % (time.time()-T0))
