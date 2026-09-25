#!/usr/bin/env python3
"""ROUND 6-AA: tests of the K6-GC3 answer (registry R6.69) on the rank-one stratum A = I + u w^T, own code.
For each invertible A (1 + w.u != 0): good set; then
  * g >= 6 ?  (Theorem 1)
  * identity + all transpositions bad ? (Prop. 2)
  * b_T + b_F <= 8 ?  (face lemma conclusion; b_T bad 3-cycles, b_F bad 4-cycles)
  * every bad 4-cycle has >= 2 good faces ? (local claim); Hall/SDR: bad 4-cycles inject into good faces ?
  * equality cases g = 6 with u, w != 0: list patterns (Theorem 2 / char 2,3 classification).
Exhaustive over F_2, F_3, F_4 (all (u,w)); samples over F_5, F_7."""
import sys, itertools, time, random
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
src = open("problems/k1695/round6_controllable.py").read()
G = {}
exec(compile(src[:src.index('print("ROUND 6-B')], "r6b", "exec"), G)
GF, rank_rows, cyclic = G['GF'], G['rank_rows'], G['cyclic']
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
P_id = tuple(range(n))
trans = [s for s in perms if ctype(s) == (2, 1, 1)]
three = [s for s in perms if ctype(s) == (3, 1)]
four = [s for s in perms if ctype(s) == (4,)]
def compose(s, t):  # (s o t)(j) = s[t[j]]; P_s P_t = P_{s o t}
    return tuple(s[t[j]] for j in range(n))
# faces of a 4-cycle rho: rho o tau for tau a transposition of two points adjacent in the cycle (gives 3-cycles)
def faces(rho):
    out = set()
    for a in range(n):
        b = rho[a]
        tau = list(range(n)); tau[a] = b; tau[b] = a
        f = compose(rho, tuple(tau))
        if ctype(f) == (3, 1): out.add(f)
    return out
FACES = {rho: faces(rho) for rho in four}
assert all(len(FACES[r]) == 4 for r in four), [len(FACES[r]) for r in four]
assert all(sum(1 for r in four if t in FACES[r]) == 3 for t in three)

def has_sdr(bad4, goodT):
    # brute-force matching: try to assign distinct good faces to all bad 4-cycles
    bad4 = list(bad4)
    def rec(i, used):
        if i == len(bad4): return True
        for f in FACES[bad4[i]]:
            if f in goodT and f not in used:
                used.add(f)
                if rec(i + 1, used): return True
                used.discard(f)
        return False
    return rec(0, set())

def run(q, sample=None):
    F = GF(q); ADD, MUL = F.ADD, F.MUL
    rng = random.Random(1695 + q)
    if sample is None:
        it = itertools.product(range(q), repeat=8)
    else:
        it = (tuple(rng.randrange(q) for _ in range(8)) for _ in range(sample))
    tot = 0; ming = None; bad_g6 = []; viol_prop2 = 0; max_bTbF = 0; viol_local = 0; viol_hall = 0; hist = {}
    for e in it:
        u, w = e[:4], e[4:]
        A = [[(1 if i == j else 0) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                A[i][j] = ADD[A[i][j]][MUL[u[i]][w[j]]]
        if rank_rows([r[:] for r in A], n, F) < n: continue
        tot += 1
        good = set(s for s in perms if cyclic(tuple(A[i][s[j]] for i in range(n) for j in range(n)), n, F))
        g = len(good); hist[g] = hist.get(g, 0) + 1
        if ming is None or g < ming: ming = g
        if P_id in good or any(t in good for t in trans): viol_prop2 += 1
        bT = sum(1 for t in three if t not in good); bF = sum(1 for r in four if r not in good)
        max_bTbF = max(max_bTbF, bT + bF)
        bad4 = [r for r in four if r not in good]
        goodT = set(t for t in three if t in good)
        if any(len(FACES[r] & goodT) < 2 for r in bad4): viol_local += 1
        if not has_sdr(bad4, goodT): viol_hall += 1
        if g == 6 and any(u) and any(w): bad_g6.append((u, w))
    print("F_%d%s: invertible A=I+uw^T: %d; min g=%d; Prop2 violations=%d; max(b_T+b_F)=%d (lemma: <=8); local '>=2 good faces' violations=%d; Hall/SDR violations=%d; g=6 with u,w!=0: %d; hist low %s  [%.0fs]"
          % (q, "" if sample is None else " sample %d" % sample, tot, ming, viol_prop2, max_bTbF, viol_local, viol_hall, len(bad_g6), sorted(hist.items())[:4], time.time()-T0))
    return bad_g6

def canon(u, w, q):
    # orbit representative under simultaneous coordinate permutation (u_i, w_i) -> (u_pi(i), w_pi(i)) and scaling u->cu, w->c^-1 w
    F = GF(q); MUL = F.MUL; INV = {a: b for a in range(1, q) for b in range(1, q) if MUL[a][b] == 1}
    best = None
    for s in perms:
        for c in range(1, q):
            uu = tuple(MUL[c][u[s[i]]] for i in range(n)); ww = tuple(MUL[INV[c]][w[s[i]]] for i in range(n))
            key = (uu, ww)
            if best is None or key < best: best = key
    return best

for q in (2, 3, 4):
    m = run(q)
    reps = sorted(set(canon(u, w, q) for u, w in m))
    print("   F_%d nontrivial minimizers: %d pairs, %d orbits under (simultaneous permutation, reciprocal scaling): %s" % (q, len(m), len(reps), reps[:8]))
for q in (5, 7):
    m = run(q, sample=30000)
    if m: print("   F_%d nontrivial minimizers found in sample: %s" % (q, m[:5]))
print("done %.0fs" % (time.time()-T0))
