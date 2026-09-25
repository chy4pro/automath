#!/usr/bin/env python3
"""ROUND 6-AB: computational certificate for (GC_4) on the rank-one stratum (registry R6.71).
Claim: for every field of characteristic p and all u, w in F^4 with c = 1 + w.u != 0, at most 11 of the 17
permutations of types (2,2), (3,1), (4) make A P_sigma non-cyclic, A = I + u w^T (then g >= 6).
Encoding (Qwen K6-GC4 section 8, own implementation): for a subset S of the 17 permutations the ideal
   I_S = < c*z - 1,  chi_{P_sigma}(t_sigma),  all 3x3 minors of (P_sigma + u w_sigma^T - t_sigma I)  : sigma in S >
in variables u1..u4, w1..w4, z, t_sigma (sigma in S).  I_S is the unit ideal over GF(p) iff no (u, w) over
the algebraic closure of GF(p) makes every sigma in S bad (a 4x4 matrix is non-cyclic iff for some
eigenvalue t the rank of B - tI is <= 2 iff all 3x3 minors vanish; t must be an eigenvalue of P_sigma,
otherwise the rank-one update cannot reach rank <= 2).  We test every 12-subset up to the symmetry
S_4-conjugation x inversion.  Controls: known consistent bad sets must be NON-unit.
Usage: round6_gc4_cert.py <p> [--controls-only] [--limit N]"""
import sys, os, itertools, time, subprocess
sys.stdout.reconfigure(line_buffering=True)
import sympy as sp
T0 = time.time()
p = int(sys.argv[1]); controls_only = "--controls-only" in sys.argv
limit = None
if "--limit" in sys.argv: limit = int(sys.argv[sys.argv.index("--limit") + 1])
OUT = "$HOME/workspace/claudecode/automath/engine/harvest/k1695_r6_gc4cert"
os.makedirs(OUT, exist_ok=True)
MS = os.path.expanduser("~/.local/bin/msolve")
ENV = dict(os.environ, DYLD_LIBRARY_PATH=os.path.expanduser("~/.local/lib"))
n = 4
perms = list(itertools.permutations(range(n)))
def ctype(s):
    seen = [False]*n; t = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]: seen[j] = True; j = s[j]; L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))
def compose(s, t): return tuple(s[t[j]] for j in range(n))
def inverse(s):
    r = [0]*n
    for j in range(n): r[s[j]] = j
    return tuple(r)
SEVENTEEN = [s for s in perms if ctype(s) in ((2, 2), (3, 1), (4,))]
assert len(SEVENTEEN) == 17
idx = {s: k for k, s in enumerate(SEVENTEEN)}
# symmetry group on the 17: conjugation by pi (sigma -> pi sigma pi^-1) and inversion
def conj(pi, s): return compose(compose(pi, s), inverse(pi))
sym_maps = []
for pi in perms:
    for inv in (False, True):
        m = tuple(idx[inverse(conj(pi, s)) if inv else conj(pi, s)] for s in SEVENTEEN)
        sym_maps.append(m)
sym_maps = list(set(sym_maps))
def canon(subset):
    fs = frozenset(subset)
    best = None
    for m in sym_maps:
        img = tuple(sorted(m[k] for k in fs))
        if best is None or img < best: best = img
    return best

u = sp.symbols("u1:5"); w = sp.symbols("w1:5"); z = sp.Symbol("z")
def perm_matrix(s):  # P_s e_j = e_{s(j)}
    return sp.Matrix(n, n, lambda i, j: 1 if s[j] == i else 0)
def gens_for(s, t):
    P = perm_matrix(s)
    wsig = sp.Matrix([w[s[j]] for j in range(n)])  # (w_sigma)_j = w_{sigma(j)}
    M = P + sp.Matrix(u) * wsig.T - t * sp.eye(n)
    chi = sp.expand((P - t * sp.eye(n)).det())
    minors = []
    for rows in itertools.combinations(range(n), 3):
        for cols in itertools.combinations(range(n), 3):
            minors.append(sp.expand(M.extract(list(rows), list(cols)).det()))
    return [chi] + [m for m in minors if m != 0]
c = 1 + sum(w[i]*u[i] for i in range(n))
GENS = {}
for s in SEVENTEEN:
    t = sp.Symbol("t%d" % idx[s])
    GENS[s] = (t, gens_for(s, t))
print("generators prepared for 17 permutations; symmetry maps %d  [%.0fs]" % (len(sym_maps), time.time()-T0))

def reduce_mod(expr, VARS):
    if p == 0: return expr
    P = sp.Poly(expr, *VARS)
    terms = {m: (int(cf) % p) for m, cf in P.terms() if int(cf) % p}
    return sp.Poly(terms, *VARS).as_expr() if terms else sp.Integer(0)

def is_unit(subset, tag):
    VARS = list(u) + list(w) + [z] + [GENS[s][0] for s in subset]
    body = [sp.expand(c*z - 1)]
    for s in subset: body += GENS[s][1]
    lines = []
    for g in body:
        r = reduce_mod(g, VARS)
        if r != 0: lines.append(str(r).replace("**", "^"))
    path = OUT + "/gc4_%s_p%d.ms" % (tag, p)
    open(path, "w").write(",".join(str(v) for v in VARS) + "\n" + str(p) + "\n" + ",\n".join(lines) + "\n")
    out = path + ".gb"
    r = subprocess.run([MS, "-g", "2", "-t", "1", "-f", path, "-o", out], env=ENV, capture_output=True, text=True, timeout=600)
    basis = "".join(l for l in open(out) if not l.startswith("#")).replace("\n", "").replace(" ", "")
    return basis.startswith("[1]"), basis[:60]

# ---- controls ----
DT = [s for s in SEVENTEEN if ctype(s) == (2, 2)]; TC = [s for s in SEVENTEEN if ctype(s) == (3, 1)]; FC = [s for s in SEVENTEEN if ctype(s) == (4,)]
ctrl1 = DT + TC                      # bad set of I + gamma J (char != 2,3): 11 elements -> must be consistent
tau = (0, 3, 2, 1)                   # transposition (2 4) in 0-based (1 3)
bad_tau = [s for s in SEVENTEEN if ctype(compose(tau, s)) != (4,)]  # bad set of A = P_tau: sigma bad iff tau*sigma not a 4-cycle
ctrl2 = bad_tau
print("control sets: |ctrl1|=%d |ctrl2|=%d" % (len(ctrl1), len(ctrl2)))
for name, S in (("single_sigma", [SEVENTEEN[0]]), ("ctrl1_IgJ", ctrl1), ("ctrl2_Ptau", ctrl2)):
    un, b = is_unit(S, name)
    print("control %s (%d perms): unit=%s (expected False)  basis starts %s  [%.0fs]" % (name, len(S), un, b, time.time()-T0))
if controls_only: sys.exit(0)

# ---- all 12-subsets up to symmetry ----
orbits = {}
for sub in itertools.combinations(range(17), 12):
    k = canon(sub)
    if k not in orbits: orbits[k] = sub
print("12-subsets: %d, orbits: %d  [%.0fs]" % (6188, len(orbits), time.time()-T0))
nonunit = []
items = sorted(orbits.items())
if limit: items = items[:limit]
for i, (k, sub) in enumerate(items):
    S = [SEVENTEEN[j] for j in sub]
    un, b = is_unit(S, "orb%03d" % i)
    if not un: nonunit.append((k, b)); print("  NON-UNIT orbit %d: %s  basis starts %s" % (i, k, b))
    if i % 25 == 0: print("  ... %d/%d done, non-unit so far %d  [%.0fs]" % (i+1, len(items), len(nonunit), time.time()-T0))
print("RESULT char %d: orbits tested %d, NON-UNIT (candidate counterexamples) %d  [%.0fs]" % (p, len(items), len(nonunit), time.time()-T0))
print("done")
