#!/usr/bin/env python3
"""
k1695 ROUND 1 -- exact reproduction of Stasinski's counterexample.

TARGET (primary sources, quoted, not paraphrased):

  Kourovka Notebook v45 (21st ed., 2026-07-03), 21tkt.tex line 8966:
    "16.95.  Conjecture: If F is a field and A is in GL(n,F), then there is a
     permutation matrix P such that AP is cyclic, that is, the minimal
     polynomial of AP is also its characteristic polynomial.  -- J.G.Thompson"

  arXiv:1606.02238v2 (withdrawn) ERRATA, verbatim:
    "I am indebted to Alexander Stasinski (Durham University) for the following
     observations.  Suppose n > 2 and J is the n x n all 1's matrix over a field
     of characteristic not 2. Then A := J - I has the minimal polynomial
     (X + 1)(X - n + 1). Thus A is invertible and not cyclic even though A
     satisfies condition (iv) of the Proposition.  The error lies in the claim
     towards the end of the proof that 'these particular row and column errors
     do not change the determinants ...'."
    Comments: "I am withdrawing this paper since the implication (iv) => (i) in
     the Proposition is false for n > 2. As a consequence the conjecture of
     J.G. Thompson remains open"

  arXiv:1606.02238v1 (CyclicMatrices.tex), the Proposition and its definitions,
  verbatim:
    "We shall use the notation A[i1:i2, j1:j2] to denote the submatrix of A
     consisting of the entries in rows i with i1 <= i <= i2 and columns j with
     j1 <= j <= j2.  We shall call an n x n matrix A strongly invertible if each
     of the submatrices A[1:k,1:k] (k=1,...,n) is invertible."
    "Proposition. Let A be an invertible n x n matrix over a field F.  Then the
     following are equivalent:
       (i)   A is cyclic;
       (ii)  A is similar to a Hessenberg matrix whose subdiagonal entries are
             all nonzero;
       (iii) A is similar to a Hessenberg matrix whose subdiagonal entries are
             all equal to 1;
       (iv)  A is similar to a matrix B such that B[2:n,1:n-1] is strongly
             invertible."
    and, in the ((ii) <=> (iv)) half of the proof, the sentence the erratum
    blames:
       "Neither do these particular row and column operations change the
        determinants of the submatrices B[2:m+1;1:m] (m=1,...,n-1) so
        B'[2:n,1:n-1] is strongly invertible."

Unfolding (iv) with the paper's own definitions: B[2:n,1:n-1] is (n-1)x(n-1),
and it is strongly invertible iff its leading kxk minors are nonzero for
k=1..n-1, i.e. iff  det B[2:k+1, 1:k] != 0  for k = 1,...,n-1.  This matches the
paper's own usage ("B[2:k+1,1:k]", "B[2:m+1;1:m] (m=1,...,n-1)").

EXACT ARITHMETIC ONLY.  Two independent cyclicity oracles (minimal-polynomial
degree by linear dependence of matrix powers; dimension of the commutant) are
run on every matrix and required to agree.  No floating point anywhere.

Interpreter: automath/.venv/bin/python3 (3.9.6, sympy 1.14.0, no networkx).
"""

import sys
import time
import itertools
from fractions import Fraction

START = time.time()
HARD_LIMIT_S = 900.0  # self-limit; see PROTOCOL hard constraint 3


def budget_ok(tag=""):
    if time.time() - START > HARD_LIMIT_S:
        raise SystemExit("HARD SELF-LIMIT %.0fs exceeded at %s" % (HARD_LIMIT_S, tag))


# ---------------------------------------------------------------- fields ----
class QQ:
    name = "QQ"
    char = 0
    zero = Fraction(0)
    one = Fraction(1)

    @staticmethod
    def of(k):
        return Fraction(k)

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def neg(a):
        return -a

    @staticmethod
    def inv(a):
        return Fraction(1) / a

    @staticmethod
    def iszero(a):
        return a == 0


class GFp:
    """Prime field F_p, p prime.  Elements are ints in [0,p)."""

    def __init__(self, p):
        self.p = p
        self.name = "GF(%d)" % p
        self.char = p
        self.zero = 0
        self.one = 1 % p

    def of(self, k):
        return k % self.p

    def add(self, a, b):
        return (a + b) % self.p

    def sub(self, a, b):
        return (a - b) % self.p

    def mul(self, a, b):
        return (a * b) % self.p

    def neg(self, a):
        return (-a) % self.p

    def inv(self, a):
        if a % self.p == 0:
            raise ZeroDivisionError
        return pow(a, self.p - 2, self.p)

    def iszero(self, a):
        return a % self.p == 0


class GF4:
    """F_4 = F_2[a]/(a^2+a+1).  Elements 0,1,2=a,3=a+1 as bit pairs."""

    name = "GF(4)"
    char = 2
    zero = 0
    one = 1

    _MUL = {}

    def __init__(self):
        if not GF4._MUL:
            for x in range(4):
                for y in range(4):
                    GF4._MUL[(x, y)] = GF4._slow_mul(x, y)

    @staticmethod
    def _slow_mul(x, y):
        # carry-less multiply then reduce mod a^2+a+1 (bits 0b111)
        r = 0
        a, b = x, y
        while b:
            if b & 1:
                r ^= a
            a <<= 1
            b >>= 1
        # reduce degree >= 2
        for shift in (2, 1, 0):
            if r & (1 << (shift + 2)):
                r ^= (0b111 << shift)
        return r & 3

    @staticmethod
    def of(k):
        return k % 2  # integers land in the prime subfield

    @staticmethod
    def add(a, b):
        return a ^ b

    @staticmethod
    def sub(a, b):
        return a ^ b

    @staticmethod
    def mul(a, b):
        return GF4._MUL[(a, b)]

    @staticmethod
    def neg(a):
        return a

    @staticmethod
    def inv(a):
        if a == 0:
            raise ZeroDivisionError
        for x in range(1, 4):
            if GF4._MUL[(a, x)] == 1:
                return x
        raise ArithmeticError

    @staticmethod
    def iszero(a):
        return a == 0


# ------------------------------------------------------- exact linear alg ---
def mat_of_int(F, rows):
    return [[F.of(x) for x in r] for r in rows]


def eye(F, n):
    return [[F.one if i == j else F.zero for j in range(n)] for i in range(n)]


def mat_mul(F, A, B):
    n, m, p = len(A), len(B), len(B[0])
    C = [[F.zero] * p for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        Ci = C[i]
        for k in range(m):
            a = Ai[k]
            if F.iszero(a):
                continue
            Bk = B[k]
            for j in range(p):
                Ci[j] = F.add(Ci[j], F.mul(a, Bk[j]))
    return C


def mat_sub(F, A, B):
    return [[F.sub(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def mat_is_zero(F, A):
    return all(F.iszero(x) for r in A for x in r)


def submatrix(A, r0, r1, c0, c1):
    """1-indexed inclusive, matching the paper's A[i1:i2, j1:j2]."""
    return [row[c0 - 1:c1] for row in A[r0 - 1:r1]]


def rank(F, rows):
    """Gaussian elimination on a copy; returns rank."""
    M = [list(r) for r in rows]
    if not M or not M[0]:
        return 0
    nr, nc = len(M), len(M[0])
    r = 0
    for c in range(nc):
        piv = None
        for i in range(r, nr):
            if not F.iszero(M[i][c]):
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = F.inv(M[r][c])
        M[r] = [F.mul(inv, x) for x in M[r]]
        for i in range(nr):
            if i != r and not F.iszero(M[i][c]):
                f = M[i][c]
                M[i] = [F.sub(M[i][j], F.mul(f, M[r][j])) for j in range(nc)]
        r += 1
        if r == nr:
            break
    return r


def det(F, rows):
    n = len(rows)
    if n == 0:
        return F.one
    M = [list(r) for r in rows]
    assert all(len(r) == n for r in M)
    d = F.one
    sign_flip = False
    for c in range(n):
        piv = None
        for i in range(c, n):
            if not F.iszero(M[i][c]):
                piv = i
                break
        if piv is None:
            return F.zero
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            sign_flip = not sign_flip
        d = F.mul(d, M[c][c])
        inv = F.inv(M[c][c])
        for i in range(c + 1, n):
            if not F.iszero(M[i][c]):
                f = F.mul(M[i][c], inv)
                M[i] = [F.sub(M[i][j], F.mul(f, M[c][j])) for j in range(n)]
    return F.neg(d) if sign_flip else d


# ------------------------------------------- two independent cyclic oracles --
def minpoly_degree(F, A):
    """Smallest d >= 1 such that I, A, ..., A^d are linearly dependent over F
    (as vectors in F^{n^2}).  That d is deg(minimal polynomial of A)."""
    n = len(A)
    powers = [eye(F, n)]
    vecs = [[x for row in powers[0] for x in row]]
    for d in range(1, n + 1):
        powers.append(mat_mul(F, powers[-1], A))
        v = [x for row in powers[-1] for x in row]
        if rank(F, vecs + [v]) == len(vecs):
            return d
        vecs.append(v)
    raise AssertionError("minpoly degree exceeded n -- impossible (Cayley-Hamilton)")


def commutant_dim(F, A):
    """dim { X : AX = XA }.  A is cyclic (nonderogatory) iff this equals n.
    Independent of minpoly_degree: it is a nullspace computation on an
    n^2 x n^2 matrix, not a power-dependence computation."""
    n = len(A)
    N = n * n
    rows = []  # each row of the linear map applied to basis matrix E_{ab}
    cols = []
    for a in range(n):
        for b in range(n):
            E = [[F.zero] * n for _ in range(n)]
            E[a][b] = F.one
            C = mat_sub(F, mat_mul(F, A, E), mat_mul(F, E, A))
            cols.append([x for row in C for x in row])
    # matrix whose columns are cols -> nullity = N - rank
    M = [[cols[j][i] for j in range(N)] for i in range(N)]
    return N - rank(F, M)


def is_cyclic(F, A, checked=None):
    n = len(A)
    d = minpoly_degree(F, A)
    c = commutant_dim(F, A)
    cyc_a = (d == n)
    cyc_b = (c == n)
    if cyc_a != cyc_b:
        raise AssertionError(
            "ORACLE DISAGREEMENT over %s: minpoly deg=%d, commutant dim=%d, n=%d"
            % (F.name, d, c, n))
    if checked is not None:
        checked.append((F.name, n, d, c))
    return cyc_a


# --------------------------------------------------- Dixon condition (iv) ---
def cond_iv_minors(F, B):
    """The paper's condition on a single B: det B[2:k+1, 1:k] for k=1..n-1."""
    n = len(B)
    return [det(F, submatrix(B, 2, k + 1, 1, k)) for k in range(1, n)]


def satisfies_iv_via(F, B):
    return all(not F.iszero(x) for x in cond_iv_minors(F, B))


# ------------------------------------------------------------- the family ---
def J_minus_I(F, n):
    return [[F.of(0 if i == j else 1) for j in range(n)] for i in range(n)]


def perm_matrix(F, sigma):
    n = len(sigma)
    P = [[F.zero] * n for _ in range(n)]
    for j, i in enumerate(sigma):
        P[i][j] = F.one
    return P


# --------------------------------------------------------------- reporting --
OUT = []


def say(s=""):
    print(s)
    OUT.append(s)


def hr(t):
    say("")
    say("=" * 78)
    say(t)
    say("=" * 78)


# =========================================================== §0 CONTROLS =====
def controls():
    hr("SECTION 0 -- ORACLE CONTROLS (each one could have come out the other way)")
    F = QQ
    ok = True

    # C0.1 companion matrix of X^n - 1 : cyclic, and Hessenberg with subdiag 1
    for n in (3, 4, 5):
        C = [[F.zero] * n for _ in range(n)]
        for i in range(1, n):
            C[i][i - 1] = F.one
        C[0][n - 1] = F.one
        cyc = is_cyclic(F, C)
        iv = satisfies_iv_via(F, C)
        say("C0.1 n=%d companion(X^n-1) over QQ : cyclic=%s  satisfies(iv) via B=C : %s"
            % (n, cyc, iv))
        ok &= cyc and iv

    # C0.2 scalar matrix 2I : NOT cyclic for n>1, and FAILS (iv) via B=itself
    for n in (3, 4, 5):
        S = [[F.of(2) if i == j else F.zero for j in range(n)] for i in range(n)]
        cyc = is_cyclic(F, S)
        iv = satisfies_iv_via(F, S)
        say("C0.2 n=%d 2*I over QQ : cyclic=%s (want False)  (iv) via B=S : %s (want False)"
            % (n, cyc, iv))
        ok &= (not cyc) and (not iv)

    # C0.3 identity : the (iv)-checker MUST reject it (k=1 minor is the (2,1) entry = 0)
    for n in (3, 4):
        I = eye(F, n)
        say("C0.3 n=%d I over QQ : (iv)-minors via B=I = %s (want a zero)"
            % (n, cond_iv_minors(F, I)))
        ok &= not satisfies_iv_via(F, I)

    # C0.4 a diagonalisable matrix with distinct eigenvalues : cyclic
    for n in (3, 4, 5):
        D = [[F.of(i + 1) if i == j else F.zero for j in range(n)] for i in range(n)]
        cyc = is_cyclic(F, D)
        say("C0.4 n=%d diag(1..n) over QQ : cyclic=%s (want True)" % (n, cyc))
        ok &= cyc

    # C0.5 oracle agreement on a spread of matrices over several fields
    fields = [QQ, GFp(2), GFp(3), GFp(5), GFp(7), GF4()]
    agree = 0
    for Fk in fields:
        for n in (3, 4):
            for seed in range(6):
                vals = [(seed * 7 + 3 * i + 5 * (i * i)) % 11 for i in range(n * n)]
                M = [[Fk.of(vals[i * n + j]) for j in range(n)] for i in range(n)]
                is_cyclic(Fk, M)  # raises on disagreement
                agree += 1
    say("C0.5 minpoly-degree oracle and commutant-dimension oracle agreed on all "
        "%d probe matrices over %s" % (agree, ", ".join(f.name for f in fields)))
    say("C0 VERDICT: %s" % ("all controls pass" if ok else "*** A CONTROL FAILED ***"))
    return ok


# ============================ §1 REPRODUCE THE ERRATUM, CLAUSE BY CLAUSE =====
def repro_table():
    hr("SECTION 1 -- STASINSKI'S COUNTEREXAMPLE, CLAUSE BY CLAUSE")
    say("A := J - I, n x n.  Erratum's four clauses, each checked separately:")
    say("  (a) minpoly(A) = (X+1)(X-n+1)   (b) A invertible")
    say("  (c) A not cyclic                (d) A satisfies condition (iv)")
    say("(d) is checked CONSTRUCTIVELY, by exhibiting a B similar to A with")
    say("B[2:n,1:n-1] strongly invertible.  The witness tried first is B = A")
    say("itself (similarity matrix = identity).")
    say("")
    hdr = ("%-9s %-4s | %-5s %-5s %-5s | %-6s %-8s %-6s | %s"
           % ("field", "n", "(a)", "(b)", "(c)", "det A", "deg mpol", "(d)",
              "counterexample to (iv)=>(i)?"))
    say(hdr)
    say("-" * len(hdr))

    fields = [QQ, GFp(3), GFp(5), GFp(7), GFp(11), GFp(2), GF4()]
    rows = []
    for Fk in fields:
        for n in (2, 3, 4, 5, 6, 7):
            budget_ok("repro n=%d %s" % (n, Fk.name))
            A = J_minus_I(Fk, n)
            # (a) minpoly = (X+1)(X-(n-1)) : the product annihilates A, and
            #     neither linear factor does => minpoly is exactly that product
            I = eye(Fk, n)
            AplusI = [[Fk.add(A[i][j], I[i][j]) for j in range(n)] for i in range(n)]
            AminusN1 = [[Fk.sub(A[i][j], Fk.mul(Fk.of(n - 1), I[i][j]))
                         for j in range(n)] for i in range(n)]
            prod_zero = mat_is_zero(Fk, mat_mul(Fk, AplusI, AminusN1))
            f1_zero = mat_is_zero(Fk, AplusI)
            f2_zero = mat_is_zero(Fk, AminusN1)
            clause_a = prod_zero and not f1_zero and not f2_zero
            # (b) invertible
            dA = det(Fk, A)
            clause_b = not Fk.iszero(dA)
            # (c) not cyclic
            d = minpoly_degree(Fk, A)
            clause_c = not is_cyclic(Fk, A)
            # (d) condition (iv), witnessed by B = A
            clause_d = satisfies_iv_via(Fk, A)
            is_ce = clause_b and clause_c and clause_d
            rows.append((Fk.name, n, clause_a, clause_b, clause_c, dA, d,
                         clause_d, is_ce))
            say("%-9s %-4d | %-5s %-5s %-5s | %-6s %-8d %-6s | %s"
                % (Fk.name, n, clause_a, clause_b, clause_c, str(dA), d,
                   clause_d, is_ce))
    return rows


# ============================= §2 (iv) HOLDS IN EVERY CHARACTERISTIC =========
def iv_minors_are_one():
    hr("SECTION 2 -- WHY (iv) HOLDS: the minors of J-I are identically 1")
    say("For A = J_n - I_n, A[2:k+1,1:k] has (i,j) entry 1 - delta_{j,i+1}.")
    say("Exact determinants, computed over ZZ (integers, no field involved):")
    for n in (3, 4, 5, 6, 7, 8):
        A = J_minus_I(QQ, n)
        ms = cond_iv_minors(QQ, A)
        say("  n=%d : det A[2:k+1,1:k] for k=1..%d  =  %s"
            % (n, n - 1, [int(x) for x in ms]))
    say("")
    say("All these minors equal 1 as INTEGERS, so they are nonzero in every")
    say("field, of every characteristic.  Hence A = J-I satisfies condition")
    say("(iv) over EVERY field, with the identity as the similarity -- the")
    say("witness needs no search.  (Proof: subtracting the last row of")
    say("A[2:k+1,1:k] from each earlier row turns row i into -e_{i+1}^T, so the")
    say("determinant is (-1)^{k-1} times the sign of the k-cycle (1 2 ... k),")
    say("which is (-1)^{k-1}; the product is 1.)")


# ================= §3 WHERE THE ERRATUM'S OWN SIDE CONDITION IS WRONG =======
def side_condition():
    hr("SECTION 3 -- CONTROL: is the erratum's stated hypothesis 'char != 2' right?")
    say("det(J_n - I_n) = (n-1)*(-1)^(n-1).  So A is invertible iff char F does")
    say("NOT divide n-1.  The erratum states the hypothesis as 'char != 2'.")
    say("These differ.  Exact check of det over each field:")
    say("")
    hdr = "%-5s %-9s %-10s %-12s %-12s" % ("n", "field", "det(J-I)", "invertible?",
                                           "erratum says?")
    say(hdr)
    say("-" * len(hdr))
    disagreements = []
    for n in (3, 4, 5, 6, 7):
        for Fk in [GFp(2), GFp(3), GFp(5), GFp(7), QQ]:
            budget_ok("side n=%d" % n)
            A = J_minus_I(Fk, n)
            dA = det(Fk, A)
            inv = not Fk.iszero(dA)
            erratum_covers = (Fk.char != 2)  # erratum's stated hypothesis
            if erratum_covers != inv:
                disagreements.append((n, Fk.name, inv, erratum_covers))
            say("%-5d %-9s %-10s %-12s %-12s"
                % (n, Fk.name, str(dA), inv,
                   "in scope" if erratum_covers else "excluded"))
    say("")
    if disagreements:
        say("DISAGREEMENTS between the erratum's stated hypothesis and the truth:")
        for n, f, inv, cov in disagreements:
            if cov and not inv:
                say("  n=%d over %s : erratum's hypothesis admits it, but A is "
                    "SINGULAR -- so it is NOT a counterexample there." % (n, f))
            else:
                say("  n=%d over %s : erratum excludes it, but A IS invertible, "
                    "not cyclic and satisfies (iv) -- so it IS a counterexample "
                    "there." % (n, f))
    else:
        say("No disagreement found -- the erratum's hypothesis is exactly right.")
    return disagreements


# ============ §4 REPRODUCE THE FAILING STEP INSIDE DIXON'S OWN PROOF ========
def break_point():
    hr("SECTION 4 -- THE BREAK POINT INSIDE THE PROOF, REPRODUCED EXACTLY")
    say("The erratum blames one sentence in the ((ii)<=>(iv)) half of the proof:")
    say('  "Neither do these particular row and column operations change the')
    say('   determinants of the submatrices B[2:m+1;1:m] (m=1,...,n-1)"')
    say("")
    say("Run Dixon's own induction step k=1 on B = J - I over QQ.  The step:")
    say("row_i <- row_i - (b_{i1}/b_{21}) row_2 for i=3..n, then the matching")
    say("column operations, i.e. B' = E B E^{-1} with E = I - sum_i c_i e_i e_2^T.")
    F = QQ
    for n in (3, 4, 5):
        budget_ok("breakpoint n=%d" % n)
        B = J_minus_I(F, n)
        assert satisfies_iv_via(F, B), "B must start in the class Bcal"
        before = cond_iv_minors(F, B)
        c = [F.zero] * n
        inv21 = F.inv(B[1][0])
        E = eye(F, n)
        Einv = eye(F, n)
        for i in range(2, n):
            c[i] = F.mul(B[i][0], inv21)
            E[i][1] = F.neg(c[i])
            Einv[i][1] = c[i]
        Bp = mat_mul(F, mat_mul(F, E, B), Einv)
        assert mat_is_zero(F, mat_sub(F, mat_mul(F, E, Einv), eye(F, n)))
        after = cond_iv_minors(F, Bp)
        say("")
        say("  n=%d" % n)
        say("    B  = %s" % [[int(x) for x in r] for r in B])
        say("    B' = %s" % [[int(x) for x in r] for r in Bp])
        say("    det B[2:m+1,1:m]  m=1..%d : %s" % (n - 1, [int(x) for x in before]))
        say("    det B'[2:m+1,1:m] m=1..%d : %s" % (n - 1, [int(x) for x in after]))
        changed = [m + 1 for m in range(n - 1) if before[m] != after[m]]
        say("    determinants CHANGED at m = %s   -> the quoted sentence is false"
            % changed)
        say("    B' still in the class Bcal? %s (the induction step needs True)"
            % satisfies_iv_via(F, Bp))
        # similarity sanity check: same char poly
        import sympy as sp
        cpB = sp.Matrix([[sp.Rational(x) for x in r] for r in B]).charpoly().as_expr()
        cpBp = sp.Matrix([[sp.Rational(x) for x in r] for r in Bp]).charpoly().as_expr()
        say("    sympy charpoly(B) == charpoly(B') ? %s   (%s)"
            % (sp.simplify(cpB - cpBp) == 0, sp.factor(cpB)))


# ====== §5 DOES J-I REFUTE 16.95 ITSELF?  n! EXACT CHECK -- MUST SAY NO =====
def thompson_check():
    hr("SECTION 5 -- CONTROL: does J-I refute Thompson's conjecture itself?")
    say("Dixon's Proposition is broken.  16.95 is a different statement.  For")
    say("each invertible A = J-I below, check ALL n! products AP for cyclicity.")
    say("If some P works, this family does not touch 16.95.  If NO P worked for")
    say("any single A, that would be a refutation of a Kourovka problem -- so")
    say("this control genuinely could have come out the other way.")
    say("")
    hdr = "%-9s %-4s %-8s %-10s %-28s" % ("field", "n", "n!", "#P cyclic",
                                          "first witness sigma")
    say(hdr)
    say("-" * len(hdr))
    fields = [QQ, GFp(2), GFp(3), GFp(5)]
    all_ok = True
    for Fk in fields:
        for n in (3, 4, 5, 6):
            budget_ok("thompson n=%d %s" % (n, Fk.name))
            A = J_minus_I(Fk, n)
            if Fk.iszero(det(Fk, A)):
                say("%-9s %-4d %-8s %-10s %s"
                    % (Fk.name, n, "-", "-", "A singular -- 16.95 does not apply"))
                continue
            cnt = 0
            first = None
            for sigma in itertools.permutations(range(n)):
                P = perm_matrix(Fk, sigma)
                AP = mat_mul(Fk, A, P)
                if is_cyclic(Fk, AP):
                    cnt += 1
                    if first is None:
                        first = sigma
            say("%-9s %-4d %-8d %-10d %-28s"
                % (Fk.name, n, len(list(itertools.permutations(range(n)))) if n <= 3
                   else __import__("math").factorial(n), cnt, str(first)))
            if cnt == 0:
                all_ok = False
                say("   *** NO PERMUTATION MAKES AP CYCLIC -- THIS WOULD REFUTE "
                    "16.95.  STOP AND ESCALATE. ***")
    say("")
    say("All rows found a witness: %s" % all_ok)
    return all_ok


# =========================== §6 sympy cross-check over QQ ===================
def sympy_crosscheck():
    hr("SECTION 6 -- INDEPENDENT sympy CROSS-CHECK OVER QQ")
    import sympy as sp
    X = sp.symbols("X")
    ok = True
    for n in (3, 4, 5, 6, 7):
        A = sp.Matrix(n, n, lambda i, j: 0 if i == j else 1)
        cp = A.charpoly(X).as_expr()
        claimed = sp.expand((X + 1) * (X - n + 1))
        annih = sp.expand((A + sp.eye(n)) * (A - (n - 1) * sp.eye(n)))
        detA = A.det()
        # sympy's own rank-based cyclicity: dim of commutant
        Xs = sp.Matrix(n, n, lambda i, j: sp.Symbol("x_%d_%d" % (i, j)))
        eqs = list((A * Xs - Xs * A))
        vars_ = list(Xs)
        M = sp.Matrix([[sp.diff(e, v) for v in vars_] for e in eqs])
        comm = len(vars_) - M.rank()
        say("n=%d : sympy det=%s  charpoly=%s" % (n, detA, sp.factor(cp)))
        say("        (A+I)(A-(n-1)I) == 0 ? %s ; claimed minpoly %s"
            % (annih == sp.zeros(n, n), sp.factor(claimed)))
        say("        sympy commutant dim = %d (n=%d) -> cyclic ? %s"
            % (comm, n, comm == n))
        ok &= (annih == sp.zeros(n, n)) and (detA != 0) and (comm != n)
        # agreement with the hand-rolled oracle
        mine = commutant_dim(QQ, J_minus_I(QQ, n))
        say("        hand-rolled commutant dim = %d -> agrees ? %s"
            % (mine, mine == comm))
        ok &= (mine == comm)
    say("")
    say("sympy cross-check consistent with the hand-rolled exact oracles: %s" % ok)
    return ok


# ===== §7 IS DIXON'S COROLLARY ARGUMENT ITSELF STILL VALID? (run, not read) ==
def greedy_corollary(F, A):
    """Dixon's own construction in the Corollary, implemented literally:
    'there exists a permutation matrix P (permuting the columns of A) such that
     AP is in Bcal'.  Base: pick Q with (AQ)[2,1] != 0.  Step k=1..n-2: pick a
    column (leaving the first k fixed) that is independent of the first k inside
    rows 2..k+2.  Returns (P, B=AP) or None if the construction gets stuck."""
    n = len(A)
    cols = list(range(n))  # cols[j] = which original column sits in position j

    def cur():
        return [[A[i][cols[j]] for j in range(n)] for i in range(n)]

    # base: (2,1) entry nonzero, i.e. 0-indexed B[1][0]
    pick = None
    for j in range(n):
        if not F.iszero(A[1][cols[j]]):
            pick = j
            break
    if pick is None:
        return None
    cols[0], cols[pick] = cols[pick], cols[0]
    # steps
    for k in range(1, n - 1):
        B = cur()
        pick = None
        for l in range(k, n):
            trial = list(cols)
            trial[k], trial[l] = trial[l], trial[k]
            T = [[A[i][trial[j]] for j in range(k + 1)] for i in range(1, k + 2)]
            if not F.iszero(det(F, T)):
                pick = l
                break
        if pick is None:
            return None
        cols[k], cols[pick] = cols[pick], cols[k]
    B = cur()
    P = [[F.zero] * n for _ in range(n)]
    for j in range(n):
        P[cols[j]][j] = F.one
    return P, B


def corollary_still_valid():
    hr("SECTION 7 -- IS DIXON'S COROLLARY CONSTRUCTION ITSELF STILL VALID?")
    say("The broken step is inside the PROPOSITION.  The COROLLARY's own")
    say("argument -- greedily permute columns until AP lies in the class Bcal --")
    say("is a separate piece of reasoning.  Run it, do not read it.  For every")
    say("invertible A below the construction must (1) never get stuck and")
    say("(2) deliver AP in Bcal.  Either could fail.  Whether AP is CYCLIC is")
    say("exactly what is no longer guaranteed -- that is the size of the gap.")
    say("")
    hdr = "%-9s %-4s %-22s %-10s %-10s %-10s" % (
        "field", "n", "family", "#tested", "#in Bcal", "#cyclic")
    say(hdr)
    say("-" * len(hdr))
    fields = [QQ, GFp(2), GFp(3), GFp(5)]
    stuck_total = 0
    for Fk in fields:
        for n in (3, 4, 5):
            budget_ok("corollary n=%d %s" % (n, Fk.name))
            # family 1: J - I (the counterexample family)
            fams = {"J-I": []}
            A = J_minus_I(Fk, n)
            if not Fk.iszero(det(Fk, A)):
                fams["J-I"].append(A)
            # family 2: a deterministic spread of invertible matrices
            fams["deterministic spread"] = []
            for seed in range(40):
                vals = [(seed * 13 + 7 * i + 3 * (i * i) + (i % 5)) % 9
                        for i in range(n * n)]
                M = [[Fk.of(vals[i * n + j]) for j in range(n)] for i in range(n)]
                if not Fk.iszero(det(Fk, M)):
                    fams["deterministic spread"].append(M)
            for fname, mats in fams.items():
                if not mats:
                    continue
                nin = ncyc = 0
                for M in mats:
                    r = greedy_corollary(Fk, M)
                    if r is None:
                        stuck_total += 1
                        continue
                    P, B = r
                    # P really is a permutation matrix and B really is A*P
                    assert mat_is_zero(Fk, mat_sub(Fk, mat_mul(Fk, M, P), B))
                    if satisfies_iv_via(Fk, B):
                        nin += 1
                    if is_cyclic(Fk, B):
                        ncyc += 1
                say("%-9s %-4d %-22s %-10d %-10d %-10d"
                    % (Fk.name, n, fname, len(mats), nin, ncyc))
    say("")
    say("construction got stuck on %d matrices -- it MUST be 0 for the "
        "corollary's argument to be valid as written." % stuck_total)
    say("")
    say("READ THE COLUMNS: '#in Bcal' == '#tested' everywhere means Dixon's")
    say("greedy really does land in Bcal, i.e. THAT part of the paper survives.")
    say("'#cyclic' < '#tested' is the gap the erratum opened: membership in Bcal")
    say("no longer buys cyclicity.")
    return stuck_total


def main():
    say("k1695 ROUND 1 -- Stasinski counterexample reproduction")
    say("interpreter: %s" % sys.executable)
    say("started: %s" % time.strftime("%Y-%m-%d %H:%M:%S %Z"))
    c_ok = controls()
    rows = repro_table()
    iv_minors_are_one()
    dis = side_condition()
    break_point()
    t_ok = thompson_check()
    s_ok = sympy_crosscheck()
    stuck = corollary_still_valid()

    hr("VERDICT")
    ce = [r for r in rows if r[8]]
    say("Rows in section 1 that are genuine counterexamples to (iv)=>(i)")
    say("  (invertible AND not cyclic AND satisfy (iv)) : %d" % len(ce))
    say("  of those, over a field of characteristic != 2 with n > 2 (exactly")
    say("  the erratum's stated hypothesis) : %d"
        % len([r for r in ce if r[1] > 2 and not r[0].startswith("GF(2")
               and r[0] != "GF(4)"]))
    say("Controls passed: oracles %s, Thompson-witness %s, sympy %s"
        % (c_ok, t_ok, s_ok))
    say("Erratum-hypothesis disagreements found: %d" % len(dis))
    say("Dixon's corollary construction got stuck on: %d matrices" % stuck)
    say("elapsed: %.1fs" % (time.time() - START))

    with open(sys.argv[1] if len(sys.argv) > 1 else
              "/dev/null", "w") as fh:
        fh.write("\n".join(OUT) + "\n")


if __name__ == "__main__":
    main()
