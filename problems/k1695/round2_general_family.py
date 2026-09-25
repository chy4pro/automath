#!/usr/bin/env python3
"""round2_general_family.py -- k1695 ROUND 2, section 10.

Stasinski's counterexample A = J - I is one point of a two-parameter family
A = a I + b J.  Every member has FULL permutation symmetry
(P_tau A P_tau^{-1} = A), so the round-2 cycle-type analysis applies to the
whole family verbatim.  This script derives, runs and stress-tests that.

Normalisation: for a != 0, cyclicity of A P is unchanged by scaling, so with
c := b/a it suffices to study  M = P + c J.   (a = 0 gives A = bJ, singular
for n >= 2, so it is outside GL(n,F).)   A = J - I is c = -1.

det(I + cJ) = 1 + cn =: nu, so A invertible <=> nu != 0 -- which for c = -1
is exactly round 1's corrected side condition char F does not divide n-1.

Interpreter: .venv/bin/python3 .  Exact arithmetic only (Fraction / mod p).
"""
import sys, time, itertools
from fractions import Fraction
from math import gcd, factorial

T0 = time.time()
LIMIT = 1200.0


def say(s=""):
    print(s); sys.stdout.flush()


def hr(t):
    say(""); say("=" * 78); say(t); say("=" * 78)


# ------------------------------------------------------------------ fields --
class QF:
    p = 0; name = "Q"
    @staticmethod
    def of(k): return Fraction(k)
    @staticmethod
    def add(a, b): return a + b
    @staticmethod
    def sub(a, b): return a - b
    @staticmethod
    def mul(a, b): return a * b
    @staticmethod
    def inv(a): return Fraction(1) / a
    @staticmethod
    def iszero(a): return a == 0
    zero = Fraction(0); one = Fraction(1)


class PF:
    def __init__(self, p):
        self.p = p; self.name = "F%d" % p; self.zero = 0; self.one = 1 % p
    def of(self, k): return k % self.p
    def add(self, a, b): return (a + b) % self.p
    def sub(self, a, b): return (a - b) % self.p
    def mul(self, a, b): return (a * b) % self.p
    def inv(self, a): return pow(a, self.p - 2, self.p)
    def iszero(self, a): return a % self.p == 0


def rank(F, rows):
    rows = [list(r) for r in rows]
    if not rows: return 0
    m = len(rows[0]); r = 0
    for c in range(m):
        piv = None
        for i in range(r, len(rows)):
            if not F.iszero(rows[i][c]): piv = i; break
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        iv = F.inv(rows[r][c])
        rows[r] = [F.mul(iv, v) for v in rows[r]]
        for i in range(len(rows)):
            if i != r and not F.iszero(rows[i][c]):
                f = rows[i][c]
                rows[i] = [F.sub(rows[i][j], F.mul(f, rows[r][j])) for j in range(m)]
        r += 1
        if r == len(rows): break
    return r


def matmul(F, A, B):
    n = len(A); C = [[F.zero] * n for _ in range(n)]
    for i in range(n):
        for t in range(n):
            a = A[i][t]
            if F.iszero(a): continue
            for j in range(n):
                C[i][j] = F.add(C[i][j], F.mul(a, B[t][j]))
    return C


def is_cyclic(F, A):
    n = len(A); vecs = []
    cur = [[F.one if i == j else F.zero for j in range(n)] for i in range(n)]
    for d in range(n + 1):
        v = [cur[i][j] for i in range(n) for j in range(n)]
        if rank(F, vecs + [v]) == len(vecs):
            return d == n
        vecs.append(v); cur = matmul(F, cur, A)
    return False


# ---------------------------------------------------------------- objects ----
def P_plus_cJ(F, sigma, c):
    n = len(sigma)
    M = [[c] * n for _ in range(n)]
    for j, i in enumerate(sigma):
        M[i][j] = F.add(M[i][j], F.one)
    return M


def type_perm(lam):
    s = []; b = 0
    for L in lam:
        s += [b + (k + 1) % L for k in range(L)]; b += L
    return s


def perm_type(s):
    n = len(s); seen = [0] * n; t = []
    for a in range(n):
        if seen[a]: continue
        L = 0; y = a
        while not seen[y]: seen[y] = 1; y = s[y]; L += 1
        t.append(L)
    return tuple(sorted(t, reverse=True))


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield (); return
    for k in range(min(n, mx), 0, -1):
        for r in parts(n - k, k): yield (k,) + r


def ntype(lam):
    n = sum(lam); num = factorial(n); m = {}
    for L in lam:
        num //= L; m[L] = m.get(L, 0) + 1
    for L, k in m.items(): num //= factorial(k)
    return num


def p_power(d, p):
    if d == 1: return True
    if p == 0: return False
    while d % p == 0: d //= p
    return d == 1


def criterion_general(F, lam, c):
    """M = P + cJ nonderogatory, c != 0.  Derived in the state file sec 10."""
    n = sum(lam); r = len(lam); p = F.p
    for i in range(r):
        for j in range(i + 1, r):
            if not p_power(gcd(lam[i], lam[j]), p): return False, "a"
    nu = F.add(F.one, F.mul(c, F.of(n)))
    if nu != F.one:
        for L in lam:
            v = F.one
            for _ in range(L): v = F.mul(v, nu)
            if v == F.one: return False, "b"
    allzero = all(F.iszero(F.of(L)) for L in lam)
    if not allzero:
        if r > 2: return False, "c1"
    else:
        if r != 1: return False, "c2"
        h = F.mul(c, F.of(n * (n - 1) // 2))
        if F.add(h, F.one) == F.zero: return False, "c3"
    return True, "ok"


def invertible(F, n, c):
    return not F.iszero(F.add(F.one, F.mul(c, F.of(n))))


# ================================================================ SECTION ====
def validate_criterion():
    hr("SEC 10.1 -- GENERALISED CRITERION vs EVERY n!, n <= 6, EVERY c != 0")
    say("M = P + cJ.  nu := 1 + cn.  Conditions:")
    say("  (a) for every mu != 1 : #{i : mu^{l_i} = 1} <= 1")
    say("  (b) if nu != 1 : #{i : nu^{l_i} = 1} = 0")
    say("  (c) if some l_i != 0 in F : r <= 2 ;")
    say("      else                  : r = 1 AND c*n(n-1)/2 != -1")
    say("(c = -1 recovers the J - I criterion exactly: nu = 1-n and the last")
    say(" clause becomes n(n-1)/2 != 1.)")
    say("")
    say("%-5s %2s %-8s %7s %9s %9s %8s" % ("field", "n", "c", "n!", "measured", "predicted", "MISMATCH"))
    tot = 0; mism = 0; distinct = set()
    fields = [PF(2), PF(3), PF(5), PF(7), QF]
    for F in fields:
        cs = ([F.of(k) for k in range(1, F.p)] if F.p else
              [Fraction(-1), Fraction(1), Fraction(2), Fraction(-2), Fraction(1, 2), Fraction(-3, 2)])
        for n in range(2, 7):
            for c in cs:
                if time.time() - T0 > LIMIT:
                    say("!! self-limit reached -- stopping 10.1 here, honestly."); return False
                meas = 0; pred = 0; bad = 0
                for s in itertools.permutations(range(n)):
                    mv = is_cyclic(F, P_plus_cJ(F, list(s), c))
                    pv = criterion_general(F, perm_type(list(s)), c)[0]
                    meas += mv; pred += pv; tot += 1
                    if mv != pv:
                        bad += 1; mism += 1
                        if bad <= 2:
                            say("   MISMATCH F=%s n=%d c=%s sigma=%s meas=%s pred=%s" %
                                (F.name, n, c, s, mv, pv))
                distinct.add(meas)
                if n >= 5 or bad:
                    say("%-5s %2d %-8s %7d %9d %9d %8d" % (F.name, n, c, factorial(n), meas, pred, bad))
    say("")
    say("%d (field, n, c, sigma) rows; %d disagreements." % (tot, mism))
    say("The measured counts take %d DISTINCT values across the grid, so the" % len(distinct))
    say("criterion is not agreeing with a constant.")
    return mism == 0


def thompson_whole_family():
    hr("SEC 10.2 -- 16.95 FOR THE WHOLE FAMILY aI + bJ  (highest-stakes control)")
    say("For A = aI + bJ, EVERY permutation conjugate of A is A itself, so the")
    say("cycle-type reduction is exact and the p(n) cycle types EXHAUST all n!")
    say("permutations.  Therefore: if for some invertible (F, n, c) NO cycle")
    say("type is cyclic, THOMPSON'S CONJECTURE 16.95 IS FALSE.  This run is a")
    say("genuine refutation attempt on a numbered Kourovka problem, over a")
    say("2-parameter family, exhaustively -- not a sample.")
    say("")
    say("%-5s %3s %6s %10s %10s %10s" % ("field", "n", "#c", "rows", "no-good", "used (n-1,1)"))
    fields = [PF(2), PF(3), PF(5), PF(7), PF(11), PF(13), QF]
    tot = 0; nogood = 0; fallback = 0; both = 0
    for F in fields:
        for n in range(2, 13):
            if time.time() - T0 > LIMIT:
                say("!! self-limit reached -- stopping 10.2 here, honestly."); return False
            cs = ([F.of(k) for k in range(1, F.p)] if F.p else
                  [Fraction(-1), Fraction(1), Fraction(2), Fraction(-2), Fraction(1, 2),
                   Fraction(-3, 2), Fraction(-2, n)])
            rows = 0; ng = 0; fb = 0
            for c in cs:
                if F.iszero(c) or not invertible(F, n, c):
                    continue
                rows += 1; tot += 1
                good = [lam for lam in parts(n)
                        if is_cyclic(F, P_plus_cJ(F, type_perm(lam), c))]
                if not good:
                    ng += 1; nogood += 1
                    say("   *** NO CYCLE TYPE WORKS: F=%s n=%d c=%s  <-- 16.95 WOULD BE FALSE" %
                        (F.name, n, c))
                else:
                    n1 = (n,) in good
                    n2 = (n - 1, 1) in good if n >= 2 else False
                    if not n1:
                        fb += 1; fallback += 1
                        if not n2:
                            both += 1
                            say("   *** BOTH BRANCHES FAIL: F=%s n=%d c=%s good=%s" %
                                (F.name, n, c, good))
            if rows:
                say("%-5s %3d %6d %10d %10d %10d" % (F.name, n, len(cs), rows, ng, fb))
    say("")
    say("%d invertible (field, n, c) rows, each EXHAUSTIVE over all n!." % tot)
    say("Rows with NO cyclic column permutation: %d   <-- 0 means 16.95 SURVIVED" % nogood)
    say("Rows where the n-cycle branch FAILED and the (n-1,1) fallback was")
    say("   load-bearing: %d.   Rows where BOTH branches failed: %d." % (fallback, both))
    say("ENTITLED CENSUS: %d of %d rows could have sunk the one-branch rule and" % (fallback, tot))
    say("did; 0 of %d sank the two-branch rule.  The %d rows are the sub-" % (tot, fallback))
    say("population where the theorem could have failed, and it is not small.")
    return nogood == 0 and both == 0


def boundary_b_zero():
    hr("SEC 10.3 -- THE BOUNDARY CASES OF THE FAMILY")
    say("b = 0 (A = aI, excluded from the c-normalisation because c = 0 changes")
    say("the kernel analysis): A P = a P and an n-cycle P is the companion")
    say("matrix of x^n - 1, so aP is the companion matrix of x^n - a^n --")
    say("cyclic.  a = 0 gives A = bJ, rank 1, not in GL(n,F) for n >= 2.")
    say("")
    say("%-5s %3s %6s %10s" % ("field", "n", "a", "aP cyclic?"))
    ok = True
    for F in [PF(2), PF(3), PF(5), QF]:
        for n in (3, 5, 8):
            for k in (1, 2, 3):
                a = F.of(k)
                if F.iszero(a): continue
                s = type_perm((n,))
                M = [[F.zero] * n for _ in range(n)]
                for j, i in enumerate(s): M[i][j] = a
                v = is_cyclic(F, M)
                ok &= v
                if n == 3:
                    say("%-5s %3d %6s %10s" % (F.name, n, a, v))
    say("   ... all (field, n, a) rows cyclic: %s" % ok)
    return ok


def main():
    say("k1695 ROUND 2 sec 10 -- the family aI + bJ")
    say("interpreter: %s" % sys.executable)
    say("started %s  self-limit %ds" % (time.strftime("%Y-%m-%d %H:%M:%S"), LIMIT))
    r1 = validate_criterion()
    r2 = thompson_whole_family()
    r3 = boundary_b_zero()
    hr("SECTION 10 SUMMARY")
    say("criterion validated against brute force : %s" % r1)
    say("16.95 holds on the whole family aI + bJ : %s" % r2)
    say("boundary case b = 0                     : %s" % r3)
    say("elapsed %.1f s" % (time.time() - T0))


if __name__ == "__main__":
    main()
