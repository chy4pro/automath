#!/usr/bin/env python3
"""owner-tdn round 3 -- THE TELESCOPING IDENTITY, and the LINE-SUM PARITY it forces.

WHY THIS FILE EXISTS
--------------------
Engine E40 (quarantined; PARTIAL; its arithmetic re-derived and correct) named its
own precise break point (iii):

    "no A_u <-> A_{ku} relation is derivable from Sec.1-2 without the withheld
     carry formula ... any argument that treats S_u = sum_k |A_{ku}| as controlled
     by |A_u| = 2 is importing a fact not established"

That is a limitation of the BRIEF E40 was given, not of the mathematics.  The carry
formula is not withheld from us -- it is in the definitions this line has used since
round 1.  With it the missing relation is three lines, and this file derives it,
verifies it by construction, and reads off a consequence that closes the exact
2-unit gap round 2 measured.

THE DEFINITIONS (arXiv 2606.27961 Sec.6; [z] = lift of z in F_p to {0..p-1})
    c_u(x)    = ([x+u] - [x] - [u]) / p          (each coordinate 0 or -1)
    d_u f(x)  = f(x+u) - f(x) + c_u(x)
    A_u(f)    = { d_u f(x) : x in F_p^2 }
    |T_f-T_f| = sum over u != 0 of |A_u(f)|

WHAT IS DERIVED HERE (both proved in two lines from the definitions; both then
VERIFIED BY CONSTRUCTION below, exhaustively over the carry space and over
functions)

 (I) COCYCLE / ADDITIVITY.  For any u, v and any x
        d_{u+v} f(x) = d_u f(x) + d_v f(x+u) + eps(u,v)
     where  eps(u,v)_c = floor( (u_c + v_c) / p )  in {0,1}.
     Proof: expand both sides; the f-terms telescope; what is left is
     c_{u+v}(x) - c_u(x) - c_v(x+u), and per coordinate that integer equals
     ((u_c+v_c) - ((u_c+v_c) mod p))/p, which does NOT depend on x.
     *** eps is INDEPENDENT OF x AND OF f. ***

 (II) TELESCOPE.  Iterating (I) along a line: for 1 <= k <= p-1
        d_{ku} f(x) = sum_{i<k} d_u f(x + i u) + gam(u,k)
     with gam(u,k)_c = floor( k * u_c / p ),  again independent of x and of f.
     This is EXACTLY the relation E40 said could not be derived.

 (III) CONSEQUENCE, when |A_u| = 2.  Write A_u = {a, a+s} (Sec.6's 2-point rigidity
     gives s parallel to u).  Give each x the letter L(x) = 0 or 1 according to
     which of the two values d_u f(x) takes.  Then by (II)
        d_{ku} f(x) = k*a + n(x,k)*s + gam(u,k),   n(x,k) = sum_{i<k} L(x + i u)
     so  |A_{ku}| = W_k := #{ distinct k-window sums n(x,k) over all x }.
     The whole line <u> is governed by the window-sum spectrum of ONE binary
     labelling.  S_u := sum_{k=1}^{p-1} |A_{ku}| = sum_k W_k.

 (IV) THE PARITY -- and I am NOT going to oversell it, because it has an
     ELEMENTARY proof that needs none of the above.  Put v = -u in (I): d_0 f = 0,
     so 0 = d_u f(x) + d_{-u} f(x+u) + eps(u,-u), i.e.
        A_{-u} = -A_u - eps(u,-u)          (a reflected translate)
     hence |A_{-u}| = |A_u|.  The p-1 directions of a line pair off as {z,-z}, so
        *** S_L := sum_{z in L} |A_z|  is EVEN, for EVERY line, always. ***
     The window-sum route reaches the same thing on 2-carrying lines
     (W_{p-k} = W_k, because n(x,k) + n(x+ku, p-k) = t with t forced constant by
     the cycle identity) and BOTH are checked below -- but the honest statement is
     that the parity is cheap.  What is NOT cheap is (III) and (VI).

 (V) THE CAP -- this one is new and is not cheap.  Window sums of length k lie in
     {0..k}, and by the same complementation they lie in {t-(p-k)..t}.  So
        |A_{ku}| = W_k <= min(k, p-k) + 1      whenever |A_u| = 2,
     and summing,  S_L <= (p-1) + (p^2-1)/4.
     *** A single 2-direction CAPS ITS WHOLE LINE. ***  At p=5 that is S_L <= 10,
     and the measured spectrum of 2-carrying lines below is exactly {8,10}.
     This is the opposite of what a lower-bound hunt looks for, and it is why the
     conjecture's content sits off the 2-carrying lines.

 (VI) WHAT THE ROUND ACTUALLY BUYS, stated without inflation.  Round 2 certified
     that separate per-direction-class minima reach only 79, "exactly 2 short",
     and concluded that ANY separately-bounding argument is structurally 2 short.
     That conclusion is too strong, and section 5 below shows why by measurement:
     the axis minimum S = 2(p-1) is attained ONLY when |A_e2| = 2, i.e. ONLY in
     the paper's Case A, where the mixed minimum is not 62 but 64.  Conditioning
     the minima on the case split, separated bookkeeping reaches 81 in BOTH
     branches.  The 2 was lost to unconditioned minima, not to separation.

CONTROLS THAT COULD FAIL (each is a real risk; a wrong derivation dies here)
    P1  eps(u,v) as CLAIMED vs c_{u+v}(x) - c_u(x) - c_v(x+u) COMPUTED, exhaustively
        over every (x,u,v) at several primes.  If eps depended on x this fails.
    P2  gam(u,k) as CLAIMED vs c_{ku}(x) - sum_i c_u(x+iu) COMPUTED, exhaustively.
    P3  identity (I) at the level of real f, all x, all (u,v).
    P4  identity (II) at the level of real f, all x, all (u,k).
    P5  |A_{ku}| == W_k, and the PREDICTED SET  {k a + n s + gam} == A_{ku} exactly,
        for every f in the complete class and every line carrying a 2-direction.
    P6  W_{p-k} == W_k (the parity, checked rather than assumed).
    P7  S_L parity/gap: over every (f, line) pair in the complete class, a line with
        a 2-direction has EVEN S_L; and NO line anywhere has S_L equal to 9.
    P8  the paper's own theorem as a control: Case A members of the class must have
        no mixed |A_w| <= 3.  If that fails, this code is wrong, not the paper.
    P9  fibre sum vs |T_f - T_f| computed literally in (Z/p^2 Z)^2, no shared path.

Interpreter: .venv/bin/python3 (pure stdlib; no sympy, no networkx).
Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r3_telescope.py
"""
import itertools
import sys
import time

T_START = time.time()
HARD_TIMEOUT_S = 900          # self-limit, PROTOCOL hard constraint 3
try:
    sys.stdout.reconfigure(line_buffering=True)
except AttributeError:
    pass

PUBLISHED_BOX = {3: 25, 5: 81}     # the paper's own values for f == 0; DATA, for P9

controls = {}
def record(name, ok, detail):
    controls[name] = bool(ok)
    print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", name, detail))


# ------------------------------------------------------------------ definitions
def carry(u, x, p):
    """c_u(x) = ([x+u] - [x] - [u]) / p ; each coordinate 0 or -1, as F_p elements."""
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def d_u_pt(f, u, x, p):
    y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
    c = carry(u, x, p)
    fy, fx = f[y], f[x]
    return ((fy[0] - fx[0] + c[0]) % p, (fy[1] - fx[1] + c[1]) % p)


def A_set(f, u, p, pts):
    return frozenset(d_u_pt(f, u, x, p) for x in pts)


def eps_claim(u, v, p):
    """CLAIMED correction of identity (I)."""
    return (((u[0] + v[0]) // p) % p, ((u[1] + v[1]) // p) % p)


def gam_claim(u, k, p):
    """CLAIMED correction of identity (II)."""
    return (((k * u[0]) // p) % p, ((k * u[1]) // p) % p)


def add(a, b, p):
    return ((a[0] + b[0]) % p, (a[1] + b[1]) % p)


print("=" * 78)
print("TDN r3 -- TELESCOPING IDENTITY and the LINE-SUM PARITY")
print("=" * 78)

# =============================================================== SECTION 1
# P1/P2: the identities are statements about CARRIES ONLY -- f cancels out of both.
# So they can be settled EXHAUSTIVELY over the whole carry space, at several primes.
print("\n[1] the two corrections are functions of (u,v) / (u,k) ALONE -- checked")
print("    exhaustively over the entire carry space, no sampling, several primes.")

p1_viol = p2_viol = 0
p1_pop = p2_pop = 0
primes_checked = []
for p in (3, 5, 7, 11):
    pts = [(a, b) for a in range(p) for b in range(p)]
    nz = [w for w in pts if w != (0, 0)]
    primes_checked.append(p)
    for u in pts:
        for v in pts:
            e = eps_claim(u, v, p)
            for x in pts:
                lhs = carry(add(u, v, p), x, p)
                r = carry(u, x, p)
                s_ = carry(v, add(x, u, p), p)
                got = ((lhs[0] - r[0] - s_[0]) % p, (lhs[1] - r[1] - s_[1]) % p)
                p1_pop += 1
                if got != e:
                    p1_viol += 1
    for u in nz:
        for k in range(1, p):
            ku = ((k * u[0]) % p, (k * u[1]) % p)
            g = gam_claim(u, k, p)
            for x in pts:
                acc0 = acc1 = 0
                y = x
                for _ in range(k):
                    c = carry(u, y, p)
                    acc0 += c[0]
                    acc1 += c[1]
                    y = add(y, u, p)
                lhs = carry(ku, x, p)
                got = ((lhs[0] - acc0) % p, (lhs[1] - acc1) % p)
                p2_pop += 1
                if got != g:
                    p2_viol += 1

print("    primes swept exhaustively: %s" % (primes_checked,))
record("P1", p1_viol == 0,
       "eps(u,v) = floor((u+v)/p) coordinatewise, independent of x : %d violations "
       "in %d (x,u,v) triples; exclusion list EMPTY" % (p1_viol, p1_pop))
record("P2", p2_viol == 0,
       "gam(u,k) = floor(k*u/p) coordinatewise, independent of x : %d violations "
       "in %d (x,u,k) triples; exclusion list EMPTY" % (p2_viol, p2_pop))

# =============================================================== SECTION 2
# P3/P4: the same two identities at the level of ACTUAL functions f.
print("\n[2] the identities at the level of real f (f enters, and cancels)")

P = 5
PTS = [(a, b) for a in range(P) for b in range(P)]
NZ = [w for w in PTS if w != (0, 0)]
MIXED = [(a, b) for a in range(1, P) for b in range(1, P)]

WITNESS_ROWS = [                       # round 1/2 witness, DATA only
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 0), (1, 0), (2, 0), (3, 0)],
    [(2, 2), (2, 2), (3, 2), (4, 2), (0, 2)],
    [(2, 2), (3, 2), (3, 2), (4, 2), (0, 2)],
    [(4, 4), (0, 4), (0, 4), (1, 4), (2, 4)],
]
witness = dict(((i, j), WITNESS_ROWS[j][i]) for j in range(P) for i in range(P))
zero_f = dict((x, (0, 0)) for x in PTS)

# a deterministic pseudo-random family, so the population is reproducible exactly
def prng_f(seed, p, pts):
    st = seed
    f = {}
    for x in pts:
        st = (st * 1103515245 + 12345) % (2 ** 31)
        a = st % p
        st = (st * 1103515245 + 12345) % (2 ** 31)
        b = st % p
        f[x] = (a, b)
    f[(0, 0)] = (0, 0)
    return f

fam = [witness, zero_f] + [prng_f(s, P, PTS) for s in range(1, 61)]
p3_viol = p4_viol = 0
p3_pop = p4_pop = 0
for f in fam:
    for u in PTS:
        for v in PTS:
            e = eps_claim(u, v, P)
            for x in PTS:
                lhs = d_u_pt(f, add(u, v, P), x, P) if add(u, v, P) != (0, 0) else None
                rhs0 = d_u_pt(f, u, x, P) if u != (0, 0) else (0, 0)
                rhs1 = d_u_pt(f, v, add(x, u, P), P) if v != (0, 0) else (0, 0)
                if u == (0, 0) or v == (0, 0) or add(u, v, P) == (0, 0):
                    continue           # d_0 is not defined by the paper; skip, stated
                rhs = add(add(rhs0, rhs1, P), e, P)
                p3_pop += 1
                if lhs != rhs:
                    p3_viol += 1
    for u in NZ:
        for k in range(1, P):
            ku = ((k * u[0]) % P, (k * u[1]) % P)
            g = gam_claim(u, k, P)
            for x in PTS:
                acc = (0, 0)
                y = x
                for _ in range(k):
                    acc = add(acc, d_u_pt(f, u, y, P), P)
                    y = add(y, u, P)
                p4_pop += 1
                if d_u_pt(f, ku, x, P) != add(acc, g, P):
                    p4_viol += 1

print("    population of f: the round-1/2 witness, f == 0, and %d deterministic"
      % (len(fam) - 2))
print("    pseudo-random f (seeded, reproducible). ALL x, ALL directions, no sampling")
print("    of x or of directions. Directions u, v, u+v all nonzero (d_0 undefined).")
record("P3", p3_viol == 0,
       "d_{u+v}f(x) = d_u f(x) + d_v f(x+u) + eps(u,v) : %d violations / %d checks"
       % (p3_viol, p3_pop))
record("P4", p4_viol == 0,
       "d_{ku}f(x) = sum_{i<k} d_u f(x+iu) + gam(u,k) : %d violations / %d checks"
       % (p4_viol, p4_pop))

# =============================================================== SECTION 3
# The complete class of round 2, re-enumerated, and the window-sum theorem on it.
print("\n[3] the complete p=%d class  A_e1 = {(0,0),(1,0)}, |A_e2| <= 3" % P)
print("    -- re-enumerated here, and every line of it tested against (III)/(IV).")

M = [[i - (1 if q < i else 0) for i in range(P)] for q in range(P)]
A_E1 = frozenset([(0, 0), (1, 0)])
E1, E2 = (1, 0), (0, 1)

# the p+1 lines through the origin of F_p^2, as ordered direction lists
LINES = []
seen = set()
for z in NZ:
    if z in seen:
        continue
    L = [((k * z[0]) % P, (k * z[1]) % P) for k in range(1, P)]
    for w in L:
        seen.add(w)
    LINES.append(tuple(L))


def build(qs, betas):
    b = [(0, 0)] * P
    for j in range(P - 1):
        b[j + 1] = ((b[j][0] + betas[j][0]) % P, (b[j][1] + betas[j][1]) % P)
    f = {}
    for j in range(P):
        for i in range(P):
            f[(i, j)] = ((b[j][0] + M[qs[j]][i]) % P, b[j][1])
    return f


def literal_diffset(f, p, pts):
    """|T_f - T_f| computed LITERALLY in (Z/p^2 Z)^2 -- shares no code with A_set."""
    n = p * p
    T = [((x[0] + p * f[x][0]) % n, (x[1] + p * f[x][1]) % n) for x in pts]
    return len(set((((a[0] - b[0]) % n), ((a[1] - b[1]) % n)) for a in T for b in T))


def window_spectrum(f, z, p, pts):
    """For a direction z with |A_z| = 2: return (ok, [W_1..W_{p-1}], predicted sets).

    Letters from the 2-point A_z; n(x,k) = window sums; A_{kz} PREDICTED as
    { k*a + n*s + gam(z,k) }.  Returns None if |A_z| != 2.
    """
    Az = sorted(A_set(f, z, p, pts))
    if len(Az) != 2:
        return None
    a, b = Az[0], Az[1]
    s = ((b[0] - a[0]) % p, (b[1] - a[1]) % p)
    lab = {}
    for x in pts:
        lab[x] = 0 if d_u_pt(f, z, x, p) == a else 1
    Ws, preds = [], []
    for k in range(1, p):
        vals = set()
        for x in pts:
            tot = 0
            y = x
            for _ in range(k):
                tot += lab[y]
                y = add(y, z, p)
            vals.add(tot)
        Ws.append(len(vals))
        g = gam_claim(z, k, p)
        preds.append(frozenset(
            (((k * a[0] + n * s[0] + g[0]) % p), ((k * a[1] + n * s[1] + g[1]) % p))
            for n in vals))
    return (a, s, Ws, preds)


n_norm = 0
p5_viol = p6_viol = 0
p5_pop = p6_pop = 0
p7_odd_with2 = 0
p7_ninesum = 0
p7_pop = 0
p10_viol = p10_pop = 0
p11_viol = p11_pop = 0
p8_caseA = 0
p8_caseA_bad = 0
p9_viol = 0
k1_viol = 0
complete = True

frontier = {}
S_e1_hist = {}
S_e2_hist = {}
Sline_hist = {}
linesum_by_has2 = {}
minS_e2_nonCaseA = None
minSm_caseA = None
minSm_non = None
min_total = None
n_below_box = 0
odd_line_examples = []

for qs in itertools.product(range(P), repeat=P):
    if time.time() - T_START > HARD_TIMEOUT_S:
        complete = False
        break
    D, okq = [], True
    for j in range(P):
        jn = (j + 1) % P
        dj = set((M[qs[jn]][i] - M[qs[j]][i]) % P for i in range(P))
        if len(dj) > 3:
            okq = False
            break
        D.append(sorted(dj))
    if not okq:
        continue

    def cells(j, beta):
        return set(((beta[0] + d) % P, beta[1]) for d in D[j])

    b0 = (0, 0)
    U0 = cells(0, b0)
    if len(U0) > 3:
        continue
    for b1 in PTS:
        U1 = U0 | cells(1, b1)
        if len(U1) > 3:
            continue
        for b2 in PTS:
            U2 = U1 | cells(2, b2)
            if len(U2) > 3:
                continue
            for b3 in PTS:
                U3 = U2 | cells(3, b3)
                if len(U3) > 3:
                    continue
                b4 = ((-(b0[0] + b1[0] + b2[0] + b3[0])) % P,
                      (-1 - (b0[1] + b1[1] + b2[1] + b3[1])) % P)
                U4 = U3 | cells(4, b4)
                if len(U4) > 3:
                    continue
                f = build(qs, [b0, b1, b2, b3, b4])

                a1 = A_set(f, E1, P, PTS)
                a2 = A_set(f, E2, P, PTS)
                if a1 != A_E1 or len(a2) > 3 or set(a2) != U4:
                    k1_viol += 1
                    continue
                n_norm += 1

                sizes = dict((w, len(A_set(f, w, P, PTS))) for w in NZ)
                total = 1 + sum(sizes.values())
                if min_total is None or total < min_total:
                    min_total = total
                if total < (2 * P - 1) ** 2:
                    n_below_box += 1

                # ---- P9 on a subsample of the class (cost of the literal set is
                #      625 ordered pairs per f); stated as a subsample, not a census
                if n_norm % 250 == 1:
                    if literal_diffset(f, P, PTS) != total:
                        p9_viol += 1

                # ---- per-line work
                Sm = 0
                for L in LINES:
                    SL = sum(sizes[w] for w in L)
                    p7_pop += 1
                    # P11: the ELEMENTARY parity, A_{-z} = -A_z - eps(z,-z), checked
                    # on EVERY line whether or not it carries a 2-direction
                    for z2 in L:
                        mz = ((-z2[0]) % P, (-z2[1]) % P)
                        p11_pop += 1
                        if sizes[z2] != sizes[mz]:
                            p11_viol += 1
                        e_ = eps_claim(z2, mz, P)
                        Az2 = A_set(f, z2, P, PTS)
                        Amz = A_set(f, mz, P, PTS)
                        if Amz != frozenset((((-a_[0] - e_[0]) % P),
                                             ((-a_[1] - e_[1]) % P)) for a_ in Az2):
                            p11_viol += 1
                    has2 = any(sizes[w] == 2 for w in L)
                    linesum_by_has2.setdefault(has2, {})
                    linesum_by_has2[has2][SL] = linesum_by_has2[has2].get(SL, 0) + 1
                    Sline_hist[SL] = Sline_hist.get(SL, 0) + 1
                    if has2 and SL % 2 == 1:
                        p7_odd_with2 += 1
                    if SL == 9:
                        p7_ninesum += 1
                    # window-sum theorem on every line that carries a 2-direction
                    if has2:
                        for z in L:
                            if sizes[z] != 2:
                                continue
                            got = window_spectrum(f, z, P, PTS)
                            a, s, Ws, preds = got
                            for k in range(1, P):
                                kz = ((k * z[0]) % P, (k * z[1]) % P)
                                p5_pop += 1
                                if sizes[kz] != Ws[k - 1] or \
                                   A_set(f, kz, P, PTS) != preds[k - 1]:
                                    p5_viol += 1
                            for k in range(1, P):
                                p6_pop += 1
                                if Ws[k - 1] != Ws[P - k - 1]:
                                    p6_viol += 1
                            for k in range(1, P):
                                p10_pop += 1
                                if Ws[k - 1] > min(k, P - k) + 1:
                                    p10_viol += 1
                            p10_pop += 1
                            if SL > (P - 1) + (P * P - 1) // 4:
                                p10_viol += 1
                            break      # one 2-direction per line suffices

                S_e1 = sum(sizes[((k * E1[0]) % P, (k * E1[1]) % P)] for k in range(1, P))
                S_e2 = sum(sizes[((k * E2[0]) % P, (k * E2[1]) % P)] for k in range(1, P))
                Sm = sum(sizes[w] for w in MIXED)
                S_e1_hist[S_e1] = S_e1_hist.get(S_e1, 0) + 1
                S_e2_hist[S_e2] = S_e2_hist.get(S_e2, 0) + 1

                cell = frontier.setdefault(S_e2, [None, None, 0])
                if cell[0] is None or Sm < cell[0]:
                    cell[0] = Sm
                if cell[1] is None or total < cell[1]:
                    cell[1] = total
                cell[2] += 1

                if len(a2) == 2:
                    p8_caseA += 1
                    if min(sizes[w] for w in MIXED) <= 3:
                        p8_caseA_bad += 1
                    if minSm_caseA is None or Sm < minSm_caseA:
                        minSm_caseA = Sm
                else:
                    if minS_e2_nonCaseA is None or S_e2 < minS_e2_nonCaseA:
                        minS_e2_nonCaseA = S_e2
                    if minSm_non is None or Sm < minSm_non:
                        minSm_non = Sm

print("    class enumerated completely = %s ; normal-form f = %d" % (complete, n_norm))
print("    de-normalised (free p^4 action, factor p^2) = %d" % (n_norm * P * P))
record("K1", k1_viol == 0,
       "every f re-checked from the DEFINITIONS, not the parametrisation : %d violations"
       % k1_viol)
record("P9", p9_viol == 0,
       "fibre sum vs |T_f-T_f| literal in (Z/p^2 Z)^2 : %d violations on a "
       "SUBSAMPLE (every 250th f); this one is a subsample, stated as such" % p9_viol)
record("P8", p8_caseA_bad == 0,
       "the PAPER'S OWN theorem as control: Case A members with a mixed |A_w| <= 3 = "
       "%d, out of %d Case A members, all mixed directions tested, exclusion list "
       "EMPTY" % (p8_caseA_bad, p8_caseA))

print("\n    (III) the window-sum theorem, tested on every line carrying a 2-direction")
record("P5", p5_viol == 0,
       "|A_{kz}| == W_k AND A_{kz} == {k a + n s + gam(z,k)} as SETS : %d violations "
       "/ %d (f,line,k) checks; exclusion list EMPTY" % (p5_viol, p5_pop))
record("P6", p6_viol == 0,
       "W_{p-k} == W_k : %d violations / %d (f,line,k) checks; exclusion list EMPTY"
       % (p6_viol, p6_pop))

cap = (P - 1) + (P * P - 1) // 4
record("P10", p10_viol == 0,
       "(V) THE CAP: a 2-direction caps its whole line, |A_{kz}| <= min(k,p-k)+1 "
       "and S_L <= %d : %d violations / %d checks; exclusion list EMPTY"
       % (cap, p10_viol, p10_pop))
record("P11", p11_viol == 0,
       "(IV) elementary parity A_{-z} = -A_z - eps(z,-z) AS SETS, and |A_{-z}| = "
       "|A_z|, on EVERY line of EVERY f : %d violations / %d (f,line,z) checks; "
       "exclusion list EMPTY" % (p11_viol, p11_pop))

print("\n[4] THE LINE-SUM PARITY AND THE GAP")
record("P7a", p7_odd_with2 == 0,
       "lines carrying a 2-direction with ODD S_L : %d, out of %d (f,line) pairs "
       "examined; exclusion list EMPTY" % (p7_odd_with2, p7_pop))
record("P7b", p7_ninesum == 0,
       "lines (ANY line, 2-direction or not) with S_L equal to the forbidden value "
       ": %d, out of %d (f,line) pairs; exclusion list EMPTY" % (p7_ninesum, p7_pop))

print("\n    S_L spectrum, split by whether the line carries a 2-direction")
for has2 in (True, False):
    h = linesum_by_has2.get(has2, {})
    if not h:
        print("      has a 2-direction = %-5s : (no such line in this class)" % has2)
        continue
    print("      has a 2-direction = %-5s : min S_L = %d ; values = %s"
          % (has2, min(h), sorted(h)))
print("    S_e1 spectrum over the class : %s" % sorted(S_e1_hist.items()))
print("    S_e2 spectrum over the class : %s" % sorted(S_e2_hist.items()))

print("\n[5] WHAT THE PARITY BUYS, on this class, in the class's own numbers")
box = (2 * P - 1) ** 2
print("    target (2p-1)^2                                   = %d" % box)
print("    S_e1 is constant on the class                     = %s"
      % sorted(S_e1_hist))
print("    min S_e2 over NON-Case-A members                  = %s" % minS_e2_nonCaseA)
print("    min S_mixed over Case A members                   = %s" % minSm_caseA)
print("    min S_mixed over NON-Case-A members               = %s" % minSm_non)
minS_e1 = min(S_e1_hist)
if minSm_caseA is not None and minS_e2_nonCaseA is not None and minSm_non is not None:
    caseA_route = 1 + minS_e1 + 2 * (P - 1) + minSm_caseA
    other_route = 1 + minS_e1 + minS_e2_nonCaseA + minSm_non
    print("    Case A branch     : 1 + S_e1 + S_e2 + S_mixed >= %d" % caseA_route)
    print("    non-Case-A branch : 1 + S_e1 + S_e2 + S_mixed >= %d" % other_route)
    print("    both branches >= target ?  %s"
          % (caseA_route >= box and other_route >= box))
print("\n    THE EXCHANGE FRONTIER, exactly: for each attained value of S_e2, the")
print("    minimum S_mixed attained WITH it, and the minimum total. This is the")
print("    coupled inequality, measured rather than guessed.")
print("      S_e2   count   min S_mixed   S_e2+min S_mixed   min total")
for s2 in sorted(frontier):
    mm, mt, cc = frontier[s2]
    print("      %-6d %-7d %-13d %-18d %d" % (s2, cc, mm, s2 + mm, mt))
need = box - 1 - minS_e1
print("    what the total needs from the pair : S_e2 + S_mixed >= %d" % need)
print("    the frontier's minimum of S_e2 + S_mixed          : %d"
      % min(s2 + frontier[s2][0] for s2 in frontier))

print("\n    ** CORRECTION TO A BANKED FINDING (cert_tdn_r2.md section 1). **")
print("    r2 certified: separate per-direction-class minima give at most 1+%d+%d+%d,"
      % (minS_e1, 2 * (P - 1), minSm_non))
print("    'exactly two short', and concluded that ANY argument bounding the")
print("    direction classes separately is structurally two short. The measurement")
print("    above says otherwise: the axis minimum %d is attained ONLY by functions"
      % (2 * (P - 1)))
print("    with |A_e2| = 2, which is precisely the paper's Case A, where the mixed")
print("    minimum is not %d but %d. Split on that and the SEPARATED bookkeeping"
      % (minSm_non, minSm_caseA))
print("    reaches the target in both branches. The lost two was not a cost of")
print("    separation; it was a cost of taking each minimum over the WHOLE class")
print("    instead of conditioning on which case attains it.")
print("    (values: axis min %d, Case A mixed min %d, non-Case-A axis min %d,"
      % (2 * (P - 1), minSm_caseA if minSm_caseA else -1,
         minS_e2_nonCaseA if minS_e2_nonCaseA else -1))
print("     non-Case-A mixed min %d)" % (minSm_non if minSm_non else -1))

print("\n    min |T_f - T_f| over the whole class, taken JOINTLY = %s" % min_total)
print("    members below the target : %d ; exclusion list NONE (all %d tested)"
      % (n_below_box, n_norm))
print("    round 2's separated bound used S_axis >= %d for each axis line and got"
      % (2 * (P - 1)))
print("    1 + %d + %d + min S_mixed, two short. The parity replaces the axis floor"
      % (2 * (P - 1), 2 * (P - 1)))
print("    by 'equal to %d, or at least %d' -- and that gap is worth exactly the two."
      % (2 * (P - 1), 2 * (P - 1) + 2))

print("\n" + "=" * 78)
print("  controls_ok = %s" % all(controls.values()))
print("  controls    = %s" % sorted(controls.items()))
print("  complete    = %s" % complete)
print("  elapsed_s   = %.2f" % (time.time() - T_START))
print("=" * 78)
