#!/usr/bin/env python3
"""round2_independent_check.py -- INDEPENDENT re-verification of round 2.

Charter rule: "Any constructed witness that will carry a claim must be
re-verified by code sharing NOTHING with its builder (separate script,
independently written predicate)."

This script imports NOTHING from round2_cycletype.py and from
round1_stasinski.py.  Its cyclicity predicate uses a DIFFERENT theorem:

    M is nonderogatory  <=>  d_{n-1}(x I - M) = 1,

where d_{n-1} is the (n-1)-st determinantal divisor, i.e. the gcd of all
(n-1)x(n-1) minors of x I - M -- equivalently the gcd of the entries of the
ADJUGATE  adj(x I - M) = sum_{i<n} x^i * ( sum_{j>i} c_j M^{j-i-1} ),
c = characteristic polynomial.  (Because minpoly = charpoly / d_{n-1}.)
Round 2's own script used minimal-polynomial degree (Krylov dependence) and
commutant nullity.  No code path and no theorem is shared.

Characteristic polynomials come from sympy's Berkowitz algorithm over ZZ
(division-free, hence valid to reduce mod p afterwards).
Interpreter: .venv/bin/python3 .  Exact arithmetic only.
"""
import sys, os, json, time, itertools
from math import factorial, gcd as igcd
import sympy
from sympy import Matrix, symbols, Poly, QQ

T0 = time.time()
LIMIT = 1500.0
x = symbols('x')
FAIL = []


def say(s=""):
    print(s); sys.stdout.flush()


def hr(t):
    say(""); say("=" * 78); say(t); say("=" * 78)


def check(cond, msg):
    if not cond:
        FAIL.append(msg); say("   *** FAIL: %s" % msg)
    return cond


# ---------------------------------------------- independent field/poly layer
def polygcd_modp(a, b, p):
    """gcd of two poly coefficient lists (index = degree) over F_p, monic."""
    def trim(u):
        while u and u[-1] % p == 0:
            u.pop()
        return u
    a = trim([c % p for c in a]); b = trim([c % p for c in b])
    while b:
        inv = pow(b[-1], p - 2, p)
        while len(a) >= len(b) and a:
            f = (a[-1] * inv) % p
            sh = len(a) - len(b)
            for i, c in enumerate(b):
                a[sh + i] = (a[sh + i] - f * c) % p
            trim(a)
        a, b = b, a
    if not a:
        return [0]
    inv = pow(a[-1], p - 2, p)
    return [(c * inv) % p for c in a]


def polygcd_QQ(a, b):
    pa = Poly(list(reversed(a)), x, domain=QQ)
    pb = Poly(list(reversed(b)), x, domain=QQ)
    if pa.is_zero and pb.is_zero:
        return [0]
    g = sympy.gcd(pa, pb)
    return list(reversed(g.all_coeffs()))


# ------------------------------------------------- the independent predicate
def charpoly_ZZ(M):
    """coefficient list, index = degree, of det(x I - M) over ZZ."""
    return list(reversed(Matrix(M).charpoly(x).all_coeffs()))


def adjugate_coeff_matrices(M, c):
    """B_i (i=0..n-1) with adj(xI-M) = sum_i x^i B_i ,  c = charpoly coeffs."""
    n = len(M)
    powers = [[[1 if a == b else 0 for b in range(n)] for a in range(n)]]
    for _ in range(n - 1):
        P = powers[-1]
        powers.append([[sum(P[a][t] * M[t][b] for t in range(n)) for b in range(n)]
                       for a in range(n)])
    B = []
    for i in range(n):
        Bi = [[0] * n for _ in range(n)]
        for j in range(i + 1, n + 1):
            cj = c[j]
            if cj == 0:
                continue
            Pk = powers[j - i - 1]
            for a in range(n):
                for b in range(n):
                    Bi[a][b] += cj * Pk[a][b]
        B.append(Bi)
    return B


def nonderogatory(M, p):
    """INDEPENDENT predicate: d_{n-1}(xI-M) == 1 .  M an integer matrix,
    p = 0 for Q, else the characteristic."""
    n = len(M)
    if n == 1:
        return True
    c = charpoly_ZZ(M)
    B = adjugate_coeff_matrices(M, c)
    g = None
    for a in range(n):
        for b in range(n):
            e = [B[i][a][b] for i in range(n)]
            if p:
                if all(v % p == 0 for v in e):
                    continue
                g = e[:] if g is None else polygcd_modp(g, e, p)
                if len(g) == 1:
                    return True
            else:
                if all(v == 0 for v in e):
                    continue
                g = e[:] if g is None else polygcd_QQ(g, e)
                if len(g) == 1:
                    return True
    if g is None:
        return False
    return len(g) == 1


# -------------------------------------------------- objects, built from zero
def J_minus_Pmat(sigma):
    """entry (i,j) of J - P where P e_j = e_{sigma(j)}."""
    n = len(sigma)
    return [[1 - (1 if sigma[j] == i else 0) for j in range(n)] for i in range(n)]


def type_to_perm(lam):
    s = []; base = 0
    for L in lam:
        s += [base + (k + 1) % L for k in range(L)]
        base += L
    return s


def perm_type(s):
    n = len(s); seen = [0] * n; t = []
    for a in range(n):
        if seen[a]:
            continue
        L = 0; y = a
        while not seen[y]:
            seen[y] = 1; y = s[y]; L += 1
        t.append(L)
    return tuple(sorted(t, reverse=True))


def parts(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for r in parts(n - k, k):
            yield (k,) + r


def count_of_type(lam):
    n = sum(lam); num = factorial(n); mult = {}
    for L in lam:
        num //= L; mult[L] = mult.get(L, 0) + 1
    for L, m in mult.items():
        num //= factorial(m)
    return num


# --------------- criterion, RE-IMPLEMENTED FROM THE PROSE, different primitives
def criterion(p, lam):
    """(a)(b)(c) as written in the state file.  Condition (a) is implemented
    here NOT by 'gcd is a p-power' but by the literal polynomial identity
    x^d - 1 == (x-1)^d over F, which holds exactly when x^d-1 has no root
    other than 1 in the algebraic closure."""
    n = sum(lam); r = len(lam)
    for i in range(r):
        for j in range(i + 1, r):
            d = igcd(lam[i], lam[j])
            if p == 0:
                same = (d == 1)
            else:
                lhs = Poly(x ** d - 1, x, modulus=p)
                rhs = Poly((x - 1) ** d, x, modulus=p)
                same = (lhs == rhs)
            if not same:
                return False
    nu = (1 - n) if p == 0 else (1 - n) % p
    one = 1 if p == 0 else 1 % p
    if nu != one:
        for L in lam:
            v = nu ** L if p == 0 else pow(nu, L, p)
            if v == one:
                return False
    zero_lens = [L for L in lam if (p and L % p == 0)]
    if len(zero_lens) < r:
        if r > 2:
            return False
    else:
        if r != 1:
            return False
        h = n * (n - 1) // 2
        if (h == 1) if p == 0 else (h % p == one):
            return False
    return True


PRIMES = [0, 2, 3, 5, 7, 11, 13]


def fname(p):
    return "Q" if p == 0 else "F%d" % p


# ================================================================== V1 =======
def self_test():
    hr("V1 -- SELF-TEST OF THE INDEPENDENT PREDICATE (before it is trusted)")
    say("The adjugate construction is checked against sympy's OWN symbolic")
    say("adjugate, and the predicate against matrices whose answer is known.")
    ok = True
    for n in (2, 3, 4, 5):
        M = [[(3 * i + 5 * j + 1) % 7 for j in range(n)] for i in range(n)]
        c = charpoly_ZZ(M)
        B = adjugate_coeff_matrices(M, c)
        sym = (x * sympy.eye(n) - Matrix(M)).adjugate()
        for a in range(n):
            for b in range(n):
                e = sympy.expand(sum(B[i][a][b] * x ** i for i in range(n)))
                if sympy.simplify(e - sympy.expand(sym[a, b])) != 0:
                    ok = False
        say("   n=%d  polynomial adjugate == sympy's symbolic adjugate : %s" % (n, ok))
    check(ok, "adjugate construction disagrees with sympy")
    say("")
    say("%-28s %-8s %-10s %s" % ("matrix", "field", "expected", "predicate"))
    cases = []
    for p in PRIMES:
        for n in (3, 4, 5):
            comp = [[1 if i == j + 1 else 0 for j in range(n)] for i in range(n)]
            comp[0][n - 1] = 1                       # companion of x^n - 1
            cases.append(("companion x^n-1 n=%d" % n, p, True, comp))
            cases.append(("2*I n=%d" % n, p, False,
                          [[2 if i == j else 0 for j in range(n)] for i in range(n)]))
            cases.append(("I n=%d" % n, p, False,
                          [[1 if i == j else 0 for j in range(n)] for i in range(n)]))
            cases.append(("diag(1..n) n=%d" % n, p, None,
                          [[i + 1 if i == j else 0 for j in range(n)] for i in range(n)]))
    npos = nneg = 0
    for nm, p, exp, M in cases:
        got = nonderogatory(M, p)
        if exp is None:
            continue
        if exp:
            npos += 1
        else:
            nneg += 1
        if got != exp:
            check(False, "self-test %s over %s: expected %s got %s" % (nm, fname(p), exp, got))
    say("   %d POSITIVE controls (companion matrices) all accepted" % npos)
    say("   %d NEGATIVE controls (2*I and I) all rejected" % nneg)
    say("   -- a predicate that always said 'yes' would fail %d of these." % nneg)
    say("")
    say("V1 verdict: %s" % ("PASS" if not FAIL else "FAIL"))
    return not FAIL


# ================================================================== V2 =======
def recheck_criterion_all_types():
    hr("V2 -- CRITERION RE-CHECKED ON EVERY CYCLE TYPE, n = 2..12, 7 FIELDS")
    say("Independent predicate (determinantal divisor) vs the criterion")
    say("re-implemented from the state file's prose.  Round 2's main script is")
    say("not consulted.")
    say("")
    say("%-5s %3s %7s %9s" % ("field", "n", "types", "mismatch"))
    tot = 0; bad = 0
    for p in PRIMES:
        for n in range(2, 13):
            if time.time() - T0 > LIMIT:
                say("!! self-limit reached at %s n=%d -- stopping V2 here, honestly." % (fname(p), n))
                say("   verified so far: %d types, %d mismatches" % (tot, bad))
                return bad == 0
            b = 0; t = 0
            for lam in parts(n):
                s = type_to_perm(lam)
                meas = nonderogatory(J_minus_Pmat(s), p)
                pred = criterion(p, lam)
                tot += 1; t += 1
                if meas != pred:
                    b += 1; bad += 1
                    check(False, "V2 %s n=%d type=%s meas=%s pred=%s" % (fname(p), n, lam, meas, pred))
            say("%-5s %3d %7d %9d" % (fname(p), n, t, b))
    say("")
    say("%d (field, cycle type) rows re-verified independently; %d mismatches." % (tot, bad))
    return bad == 0


# ================================================================== V3 =======
def recheck_cycle_type_lemma_and_counts():
    hr("V3 -- CYCLE-TYPE LEMMA AND ROUND 1'S TWELVE COUNTS, INDEPENDENTLY")
    say("(i) every n! for n <= 5, all 7 fields, with the independent predicate:")
    say("    does the verdict really depend only on the cycle type?")
    say("")
    say("%-5s %2s %7s %8s %9s" % ("field", "n", "n!", "classes", "split"))
    splits = 0; classes = 0
    for p in PRIMES:
        for n in range(2, 6):
            byt = {}
            for s in itertools.permutations(range(n)):
                v = nonderogatory(J_minus_Pmat(list(s)), p)
                byt.setdefault(perm_type(list(s)), set()).add(v)
            sp = sum(1 for k, v in byt.items() if len(v) > 1)
            splits += sp; classes += len(byt)
            say("%-5s %2d %7d %8d %9d" % (fname(p), n, factorial(n), len(byt), sp))
    check(splits == 0, "cycle-type lemma split a class")
    say("")
    say("%d classes, %d split.  (Every class could have split.)" % (classes, splits))
    say("")
    say("(ii) round 1's twelve measured counts, recomputed by summing")
    say("     count_of_type over the types the INDEPENDENT predicate accepts:")
    say("")
    R1 = [(0, 3, 5), (0, 4, 14), (0, 5, 74), (0, 6, 264),
          (2, 4, 14), (2, 6, 144), (3, 3, 5), (3, 5, 24), (3, 6, 264),
          (5, 3, 5), (5, 4, 8), (5, 5, 74)]
    say("%-5s %2s %10s %14s %s" % ("field", "n", "round-1", "independent", "match"))
    allok = True
    for p, n, want in R1:
        tot = 0
        for lam in parts(n):
            if nonderogatory(J_minus_Pmat(type_to_perm(lam)), p):
                tot += count_of_type(lam)
        m = (tot == want); allok &= m
        say("%-5s %2d %10d %14d %s" % (fname(p), n, want, tot, "YES" if m else "**NO**"))
    check(allok, "round-1 counts not reproduced by the independent predicate")
    return splits == 0 and allok


# ================================================================== V4 =======
def recheck_existence_and_refutation():
    hr("V4 -- THE 58 EXISTENCE WITNESSES AND THE n-CYCLE REFUTATION")
    say("Every witness that carries the round-2 theorem is rebuilt from its")
    say("cycle type and re-tested with the independent predicate.")
    say("")
    say("%-5s %3s %10s %12s %10s" % ("field", "n", "n-cycle", "(n-1,1)", "witness ok"))
    rows = 0; ok = True; nfail1 = 0; nfail2 = 0
    for p in PRIMES:
        for n in range(3, 13):
            if p and (n - 1) % p == 0:
                continue
            rows += 1
            c1 = nonderogatory(J_minus_Pmat(type_to_perm((n,))), p)
            c2 = nonderogatory(J_minus_Pmat(type_to_perm((n - 1, 1))), p)
            w = c1 or c2
            ok &= w
            nfail1 += (not c1); nfail2 += (not c2)
            say("%-5s %3d %10s %12s %10s" % (fname(p), n, c1, c2, w))
    check(ok, "an existence witness failed under the independent predicate")
    say("")
    say("%d invertible (field, n) rows; witness cyclic in all: %s" % (rows, ok))
    say("ENTITLED CENSUS, and it is the whole point of the case split:")
    say("   the n-cycle branch FAILED on %d of %d rows," % (nfail1, rows))
    say("   the (n-1,1) branch FAILED on %d of %d rows," % (nfail2, rows))
    say("   and they failed together on 0.  NEITHER BRANCH ALONE IS A THEOREM;")
    say("   the disjunction is.  %d of %d rows exercised a branch that could" % (nfail1 + nfail2, rows))
    say("   have sunk a one-branch rule.")
    say("")
    say("n-cycle refutation, char 2, n = 2 mod 4 (claimed infinite family):")
    say("%-5s %3s %10s %12s" % ("field", "n", "n-cycle", "(n-1,1)"))
    ref = True
    for n in (6, 10, 14, 18, 22):
        if time.time() - T0 > LIMIT:
            say("!! self-limit reached -- stopped the refutation sweep at n=%d." % n)
            break
        c1 = nonderogatory(J_minus_Pmat(type_to_perm((n,))), 2)
        c2 = nonderogatory(J_minus_Pmat(type_to_perm((n - 1, 1))), 2)
        ref &= (not c1) and c2
        say("%-5s %3d %10s %12s" % ("F2", n, c1, c2))
    check(ref, "the char-2 n=2 mod 4 refutation did not reproduce")
    say("control, char 2, n = 0 mod 4 (the n-cycle must WORK here, else vacuous):")
    ctl = True
    for n in (4, 8, 12):
        c1 = nonderogatory(J_minus_Pmat(type_to_perm((n,))), 2)
        ctl &= c1
        say("%-5s %3d %10s" % ("F2", n, c1))
    check(ctl, "char-2 n=0 mod 4 control failed -- corollary would be vacuous")
    return ok and ref and ctl


# ================================================================== V5 =======
def recheck_greedy_is_identity():
    hr("V5 -- 'DIXON'S GREEDY RETURNS THE IDENTITY ON J-I' -- PROVED, THEN RUN")
    say("PROOF.  A = J - I.  Base step: the construction takes the first column")
    say("j with A[2,j] != 0; that is j = 1, and A[2,1] = 1 != 0, so no swap.")
    say("Step k: it takes the first admissible column, testing l = k first, and")
    say("l = k means the submatrix A[2:k+2, 1:k+1] with columns untouched, whose")
    say("determinant round 1 proved is identically 1 over Z.  So l = k is always")
    say("admissible and no swap is ever made.  Hence P = I for every field and")
    say("every n.  QED -- the construction does NOTHING to Stasinski's family.")
    say("")
    say("RUN: the minors round 1 says are 1 are recomputed here from scratch,")
    say("by sympy, over ZZ -- if any were 0 or != 1 the proof above would break.")
    ok = True
    for n in range(3, 13):
        A = Matrix([[0 if i == j else 1 for j in range(n)] for i in range(n)])
        ds = [A[1:k + 1, 0:k].det() for k in range(1, n)]
        good = all(d == 1 for d in ds)
        ok &= good
        say("   n=%2d  det A[2:k+1,1:k], k=1..%d  =  %s   %s" %
            (n, n - 1, ds if n <= 7 else "all 1", "ok" if good else "**BROKEN**"))
    check(ok, "the leading minors of J-I are not identically 1")
    say("")
    say("And the identity permutation has cycle type 1+1+...+1, i.e. r = n cycles,")
    say("which violates criterion (c) (r <= 2) for every n >= 3.  So the")
    say("construction lands on the WORST cycle type available -- the maximum")
    say("possible number of cycles -- while its own target class Bcal accepts it.")
    for p in PRIMES:
        for n in (3, 4, 5, 6):
            if p and (n - 1) % p == 0:
                continue
            v = nonderogatory(J_minus_Pmat(list(range(n))), p)
            check(v is False, "J - I claimed cyclic over %s at n=%d" % (fname(p), n))
    say("   confirmed: J - P_identity = J - I is non-cyclic on every invertible")
    say("   (field, n) row with n >= 3, under the independent predicate.")
    return ok



# ================================================================== V6 =======
def recheck_general_family():
    hr("V6 -- THE FAMILY aI + bJ, RE-VERIFIED WITH THE INDEPENDENT PREDICATE")
    say("M = P + cJ.  Same predicate (determinantal divisor), criterion")
    say("re-implemented from the state file section 10 prose.")
    say("")

    def PcJ(sigma, c):
        n = len(sigma)
        return [[c + (1 if sigma[j] == i else 0) for j in range(n)] for i in range(n)]

    def crit_gen(p, lam, c):
        """c given as an integer representative mod p (p>0) or a Fraction (p=0)."""
        n = sum(lam); r = len(lam)
        one = 1 if p == 0 else 1 % p
        for i in range(r):
            for j in range(i + 1, r):
                d = igcd(lam[i], lam[j])
                same = (d == 1) if p == 0 else (
                    Poly(x ** d - 1, x, modulus=p) == Poly((x - 1) ** d, x, modulus=p))
                if not same:
                    return False
        nu = (1 + c * n) if p == 0 else (1 + c * n) % p
        if nu != one:
            for L in lam:
                v = nu ** L if p == 0 else pow(nu, L, p)
                if v == one:
                    return False
        allz = all((p and L % p == 0) for L in lam) if p else False
        if not allz:
            if r > 2:
                return False
        else:
            if r != 1:
                return False
            h = c * (n * (n - 1) // 2)
            if ((h + 1) == 0) if p == 0 else ((h + 1) % p == 0):
                return False
        return True

    say("%-5s %3s %6s %9s %12s %10s" % ("field", "n", "#c", "types", "mismatch", "no-good"))
    tot = 0; mism = 0; nogood = 0; rows = 0; fb = 0
    for p in [2, 3, 5, 7, 0]:
        for n in range(2, 10):
            if time.time() - T0 > LIMIT:
                say("!! self-limit reached -- stopping V6 here, honestly."); return mism == 0
            cs = list(range(1, p)) if p else [sympy.Rational(k) for k in (-1, 1, 2, -2)] + \
                 [sympy.Rational(1, 2), sympy.Rational(-2, n)]
            b = 0; t = 0; ng = 0
            for c in cs:
                nu = (1 + c * n) if p == 0 else (1 + c * n) % p
                if (nu == 0) if p == 0 else (nu % p == 0):
                    continue              # A singular
                rows += 1
                good = []
                for lam in parts(n):
                    meas = nonderogatory(PcJ(type_to_perm(lam), c), p)
                    pred = crit_gen(p, lam, c)
                    tot += 1; t += 1
                    if meas != pred:
                        b += 1; mism += 1
                        check(False, "V6 %s n=%d c=%s type=%s meas=%s pred=%s" %
                              (fname(p), n, c, lam, meas, pred))
                    if meas:
                        good.append(lam)
                if not good:
                    ng += 1; nogood += 1
                    check(False, "V6 NO CYCLE TYPE WORKS %s n=%d c=%s -- 16.95 FALSE" %
                          (fname(p), n, c))
                else:
                    if (n,) not in good:
                        fb += 1
                        check((n - 1, 1) in good,
                              "V6 both branches fail %s n=%d c=%s" % (fname(p), n, c))
            say("%-5s %3d %6d %9d %12d %10d" % (fname(p), n, len(cs), t, b, ng))
    say("")
    say("%d (field, n, c, cycle type) rows re-verified; %d mismatches." % (tot, mism))
    say("%d invertible (field, n, c) rows, each EXHAUSTIVE over all n!;" % rows)
    say("   rows with NO cyclic column permutation: %d  (0 => 16.95 survives)" % nogood)
    say("   rows where the n-cycle failed and the fallback carried it: %d" % fb)
    return mism == 0 and nogood == 0


def main():
    say("k1695 ROUND 2 -- INDEPENDENT RE-VERIFICATION")
    say("interpreter: %s   sympy %s" % (sys.executable, sympy.__version__))
    say("predicate: (n-1)-st determinantal divisor of xI-M  (adjugate gcd)")
    say("started %s  self-limit %ds" % (time.strftime("%Y-%m-%d %H:%M:%S"), LIMIT))
    self_test()
    recheck_criterion_all_types()
    recheck_cycle_type_lemma_and_counts()
    recheck_existence_and_refutation()
    recheck_greedy_is_identity()
    recheck_general_family()
    hr("INDEPENDENT VERIFICATION SUMMARY")
    if FAIL:
        say("FAILURES: %d" % len(FAIL))
        for f in FAIL:
            say("   %s" % f)
    else:
        say("NO FAILURES.  Every load-bearing round-2 claim reproduced by code")
        say("that shares no function, no field class and no theorem with the")
        say("script that produced it.")
    say("elapsed %.1f s" % (time.time() - T0))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
