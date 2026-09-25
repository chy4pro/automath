#!/usr/bin/env python3
"""ROUND 3-D (line k1695, 2026-08-24): MACHINE-CHECK OF THE n=3 THEOREM.

THEOREM (proved this round; full proof in problems/k1695/campaign_registry.md R3.6).
  For every field F and every A in GL(3,F) there is a permutation matrix P with AP cyclic.
  I.e. Kourovka 16.95 holds for n <= 3, over EVERY field.

The proof is CONSTRUCTIVE -- it names the witness -- so it can be machine-checked directly:
this script implements the proof's decision rule and then verifies, with an oracle that
shares no logic with the rule, that the named permutation really does give a cyclic product.

THE RULE (verbatim from the proof).
  Step 1  If A is cyclic, take P = I.
  Step 2  Otherwise A is derogatory, hence A = lam*(I + u v^T) with lam in F^*, u,v in F^3:
          geometric multiplicity >= 2 forces m_lam^2 to divide the characteristic polynomial
          (invariant-factor argument, valid in every characteristic -- a conjugate-counting
          argument would be WRONG over an imperfect field), so 2*deg m_lam <= 3 and lam in F.  If u = 0 or v = 0 then A is scalar: take a 3-cycle.
  Step 3  Otherwise, for a transposition pi = (i j) with fixed point k, A P_pi FAILS to be
          cyclic only if
            (T1)  [S_v = 0 and v_k = 0]  or  [S_u = 0 and u_k = 0]        (failure at lam=1)
            (T2)  char != 2, u_i = u_j, v_i = v_j, u_i v_i + u_k v_k / 2 = -1  (at lam=-1)
          Take the first k for which neither holds.
  Step 4  If every transposition fails, the proof shows u = a*1, v = b*1 with 3ab/2 = -1
          (so char is neither 2 nor 3); then any 3-cycle works.

CONTROLS (each asserted; a failure aborts):
  NEG-1  the rule "always return P = I" must FAIL on these A (they are all derogatory) --
         if it passed, the whole test would be vacuous.
  NEG-2  the rule with clause (T2) DELETED must FAIL somewhere -- this is what proves the
         lam=-1 clause is load-bearing and not decoration.
  NEG-3  the rule with clause (T1) DELETED must FAIL somewhere.
  POS-1  the oracle judges I non-cyclic and the companion of x^3-1 cyclic.
  RED-1  (reduction step of the proof, checked exhaustively, q <= 5): every non-cyclic
         A in GL(3,q) really is of the form lam*(I+u v^T) with lam in F -- if this failed,
         Step 2 would be unsound.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()

IRRED = {(2,2):[1,1,1], (2,3):[1,1,0,1], (3,2):[1,0,1]}
def prime_power(q):
    p = 2
    while p*p <= q and q % p:
        p += 1
    if q % p:
        p = q
    k, t = 0, q
    while t % p == 0:
        t //= p; k += 1
    assert t == 1
    return p, k

class GF(object):
    def __init__(self, q):
        p, k = prime_power(q); self.q, self.p, self.k = q, p, k
        if k == 1:
            self.ADD = [[(a+b) % p for b in range(q)] for a in range(q)]
            self.MUL = [[(a*b) % p for b in range(q)] for a in range(q)]
        else:
            f = IRRED[(p,k)]
            def dg(a):
                d = []
                for _ in range(k):
                    d.append(a % p); a //= p
                return d
            def ud(d):
                v = 0
                for i in reversed(range(k)):
                    v = v*p + d[i]
                return v
            def pm(a, b):
                da, db = dg(a), dg(b); c = [0]*(2*k-1)
                for i in range(k):
                    if da[i]:
                        for j in range(k):
                            c[i+j] = (c[i+j] + da[i]*db[j]) % p
                for i in reversed(range(k, 2*k-1)):
                    if c[i]:
                        co = c[i]; c[i] = 0
                        for j in range(k):
                            c[i-k+j] = (c[i-k+j] - co*f[j]) % p
                return ud(c[:k])
            self.ADD = [[ud([(x+y) % p for x, y in zip(dg(a), dg(b))]) for b in range(q)] for a in range(q)]
            self.MUL = [[pm(a, b) for b in range(q)] for a in range(q)]
        self.NEG = [next(b for b in range(q) if self.ADD[a][b] == 0) for a in range(q)]
        self.INV = [0]*q
        for a in range(1, q):
            self.INV[a] = next(b for b in range(1, q) if self.MUL[a][b] == 1)
    def add(self, *xs):
        r = 0
        for x in xs:
            r = self.ADD[r][x]
        return r

N = 3
def matmul(A, B, F):
    MUL, ADD = F.MUL, F.ADD
    C = [0]*9
    for i in range(3):
        for k in range(3):
            a = A[i*3+k]
            if a:
                Ma = MUL[a]
                for j in range(3):
                    b = B[k*3+j]
                    if b:
                        C[i*3+j] = ADD[C[i*3+j]][Ma[b]]
    return tuple(C)

def cyclic(M, F):
    """ORACLE: minpoly degree == 3.  Shares no logic with the proof's rule."""
    MUL, ADD, NEG, INV = F.MUL, F.ADD, F.NEG, F.INV
    rows = []
    cur = (1,0,0,0,1,0,0,0,1)
    for _ in range(3):
        v = list(cur)
        for (piv, rw) in rows:
            f = v[piv]
            if f:
                Mnf = MUL[NEG[f]]
                for t in range(piv, 9):
                    if rw[t]:
                        v[t] = ADD[v[t]][Mnf[rw[t]]]
        piv = next((i for i, x in enumerate(v) if x), None)
        if piv is None:
            return False
        Miv = MUL[INV[v[piv]]]
        rows.append((piv, [Miv[x] for x in v]))
        cur = matmul(cur, M, F)
    return True

def perm_matrix(s):
    return tuple(1 if s[j] == i else 0 for i in range(3) for j in range(3))

PERMS = {s: perm_matrix(s) for s in itertools.permutations(range(3))}
THREECYCLE = (1, 2, 0)
def transposition(k):
    i, j = [t for t in range(3) if t != k]
    s = list(range(3)); s[i], s[j] = j, i
    return tuple(s)

def rule(u, v, F, use_T1=True, use_T2=True, always_identity=False):
    """The proof's decision rule -> the permutation it names."""
    if always_identity:
        return (0, 1, 2)
    if all(x == 0 for x in u) or all(x == 0 for x in v):
        return THREECYCLE
    Su, Sv = F.add(*u), F.add(*v)
    for k in range(3):
        i, j = [t for t in range(3) if t != k]
        T1 = ((Sv == 0 and v[k] == 0) or (Su == 0 and u[k] == 0)) if use_T1 else False
        T2 = False
        if use_T2 and F.p != 2:
            if u[i] == u[j] and v[i] == v[j]:
                half = F.INV[F.ADD[1][1]]                       # 1/2
                lhs = F.ADD[F.MUL[u[i]][v[i]]][F.MUL[F.MUL[u[k]][v[k]]][half]]
                T2 = (lhs == F.NEG[1])
        if not T1 and not T2:
            return transposition(k)
    return THREECYCLE

def build_A(u, v, F):
    """A = I + u v^T."""
    ADD, MUL = F.ADD, F.MUL
    return tuple(ADD[1 if i == j else 0][MUL[u[i]][v[j]]] for i in range(3) for j in range(3))

def run_cell(q, mode):
    F = GF(q)
    tested = 0; failures = []
    for u in itertools.product(range(q), repeat=3):
        for v in itertools.product(range(q), repeat=3):
            c0 = F.add(*[F.MUL[u[i]][v[i]] for i in range(3)])
            if F.ADD[1][c0] == 0:
                continue                                        # A singular: 16.95 says nothing
            A = build_A(u, v, F)
            tested += 1
            s = rule(u, v, F, **mode)
            if not cyclic(matmul(A, PERMS[s], F), F):
                failures.append((u, v, s))
    return tested, failures

print("ROUND 3-D: machine-check of the n=3 theorem")
# POS-1
for q in [2,3,4,5,7,8,9]:
    F = GF(q)
    assert not cyclic((1,0,0,0,1,0,0,0,1), F), "POS-1 FAILED (identity judged cyclic) q=%d" % q
    assert cyclic((0,0,1,1,0,0,0,1,0), F), "POS-1 FAILED (companion judged non-cyclic) q=%d" % q
print("POS-1 oracle controls pass (I non-cyclic, companion of x^3-1 cyclic), q in {2,3,4,5,7,8,9}")

# RED-1: the proof's Step-2 reduction, checked exhaustively over all of GL(3,q)
for q in [2,3,4,5]:
    F = GF(q)
    tot = 0; noncyc = 0; bad = 0
    for flat in itertools.product(range(q), repeat=9):
        A = tuple(flat)
        # invertible?
        M = [list(A[i*3:(i+1)*3]) for i in range(3)]; ok = True
        for c in range(3):
            piv = next((r for r in range(c,3) if M[r][c]), None)
            if piv is None:
                ok = False; break
            if piv != c: M[c], M[piv] = M[piv], M[c]
            iv = F.INV[M[c][c]]
            for r in range(c+1,3):
                if M[r][c]:
                    f = F.MUL[M[r][c]][iv]; Mnf = F.MUL[F.NEG[f]]
                    for t in range(c,3):
                        if M[c][t]: M[r][t] = F.ADD[M[r][t]][Mnf[M[c][t]]]
        if not ok:
            continue
        tot += 1
        if cyclic(A, F):
            continue
        noncyc += 1
        # must be lam*(I + u v^T): i.e. exists lam in F with rank(A - lam I) <= 1
        found = False
        for lam in range(1, q):
            B = [[F.ADD[A[i*3+j]][F.NEG[F.MUL[lam][1 if i == j else 0]]] for j in range(3)] for i in range(3)]
            # rank <= 1 ?
            nz = [r for r in B if any(r)]
            if not nz:
                found = True; break
            r0 = nz[0]; piv = next(i for i, x in enumerate(r0) if x)
            r1 = True
            for r in nz[1:]:
                c = F.MUL[r[piv]][F.INV[r0[piv]]]
                if any(F.ADD[r[t]][F.NEG[F.MUL[c][r0[t]]]] for t in range(3)):
                    r1 = False; break
            if r1:
                found = True; break
        if not found:
            bad += 1
    assert bad == 0, "RED-1 FAILED q=%d: %d non-cyclic A are NOT lam*(I+uv^T)" % (q, bad)
    assert noncyc > 0, "RED-1 VACUOUS q=%d: no non-cyclic A in GL(3,q) at all" % q
    print("RED-1 q=%d: |GL(3,q)|=%d, non-cyclic=%d, all of them of the form lam*(I+uv^T)  [Step 2 sound]" % (q, tot, noncyc))

# main check + negative controls
print("--- the rule, and the controls that show each clause is load-bearing ---")
MODES = [("PROOF RULE", {}),
         ("NEG-1 always P=I", {"always_identity": True}),
         ("NEG-2 clause T2 deleted", {"use_T2": False}),
         ("NEG-3 clause T1 deleted", {"use_T1": False})]
for q in [2,3,4,5,7,8,9]:
    line = []
    for (name, mode) in MODES:
        tested, fails = run_cell(q, mode)
        line.append("%s: %d/%d ok" % (name, tested-len(fails), tested))
        if name == "PROOF RULE":
            assert not fails, "THEOREM FALSIFIED q=%d first witness %s" % (q, fails[0])
        elif q > 2 or name != "NEG-2 clause T2 deleted":
            # T2 is vacuous in characteristic 2 by construction, so it cannot fail there
            if name == "NEG-2 clause T2 deleted" and GF(q).p == 2:
                continue
            assert fails, "CONTROL %s DID NOT FAIL at q=%d -- that clause is not load-bearing" % (name, q)
    print("q=%d  " % q + " | ".join(line))
print("VERDICT: n=3 theorem's constructive rule verified on every invertible I+uv^T over "
      "GF(q), q in {2,3,4,5,7,8,9}; all negative controls failed as they must. %.1fs" % (time.time()-T0))
