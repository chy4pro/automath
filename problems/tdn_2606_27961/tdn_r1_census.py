#!/usr/bin/env python3
"""owner-tdn round 1 -- INDEPENDENT census of the weakened rigidity question.

QUESTION (charter clause (3), arXiv:2606.27961 Sec.6):
  Sec.6 proves |A_w| >= 4 for mixed w = lam*u + mu*v (lam*mu != 0) only under
  |A_u| = |A_v| = 2.  Does the conclusion survive weakening that to <= 3 ?

Definitions re-implemented FROM THE PAPER'S OWN, not imported from probe_t1.py
(quarantine discipline: nothing enters the ledger that this file did not derive):
    G  = (Z/p^2 Z)^2 ,  T_f = { [x] + p[f(x)] : x in F_p^2 } , f(0) = 0
    c_u(x)   = ([x+u] - [x] - [u]) / p          (each coord 0 or -1)
    d_u f(x) = f(x+u) - f(x) + c_u(x)
    A_u(f)   = { d_u f(x) : x in F_p^2 }
    |T_f - T_f| = sum_u |A_u(f)|

TWO INDEPENDENT PATHS, deliberately sharing no counting logic:

  PATH 1 (p=3 only) -- BRUTE.  Every one of the p^(2p^2-2) functions with
    f(0)=0 is visited, as an ordered triple of rows, with the horizontal and
    vertical image sets carried as 9-bit masks.  Population = the entire space.

  PATH 2 (any p) -- STRUCTURED.  f <-> (row base b_j, row word w_j) where
    w_j[i] = d_e1 f(i,j) and sum_i w_j[i] = -e1 (the cycle identity, which the
    parametrisation ABSORBS rather than tests).  Depth-first over rows carrying
    the vertical image set, pruned at |B| > 3.  Reduced by the free p^4 action
    f -> f + lam*[x_1] + mu*[x_2], which shifts A_e1 by lam and A_e2 by mu and
    every A_w by lam*w_1 + mu*w_2 -- so it preserves EVERY |A_w| and the
    reduction is lossless for the rigidity question.

PATH 1 and PATH 2 must agree on R2(3) and on min |A_w|.  Neither is allowed to
be checked against 18225 before both have printed; the comparison is made by
this file, at the end, and printed as PASS/FAIL.

Run:  .venv/bin/python3 problems/tdn_2606_27961/tdn_r1_census.py [--p5]
"""
import itertools
import sys
import time

T_START = time.time()
HARD_TIMEOUT_S = 1000          # self-limit, PROTOCOL hard constraint 3
try:
    sys.stdout.reconfigure(line_buffering=True)
except AttributeError:
    pass


def elapsed():
    return time.time() - T_START


def out_of_time():
    return elapsed() > HARD_TIMEOUT_S


# ------------------------------------------------------------------ algebra
class Fp2(object):
    """F_p^2 with points encoded as ints 0..p^2-1 ; idx = a*p + b."""

    def __init__(self, p):
        self.p = p
        self.n = p * p
        self.pts = [(a, b) for a in range(p) for b in range(p)]
        self.idx = dict((q, i) for i, q in enumerate(self.pts))
        n = self.n
        self.ADD = [[0] * n for _ in range(n)]
        self.SUB = [[0] * n for _ in range(n)]
        for i, (a, b) in enumerate(self.pts):
            for j, (c, d) in enumerate(self.pts):
                self.ADD[i][j] = self.idx[((a + c) % p, (b + d) % p)]
                self.SUB[i][j] = self.idx[((a - c) % p, (b - d) % p)]

    def e(self, a, b):
        return self.idx[(a % self.p, b % self.p)]


def carry(u, x, p):
    """c_u(x) = ([x+u] - [x] - [u]) / p ; each coordinate is 0 or -1."""
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def d_u_val(f, u, x, F):
    """d_u f(x) as an F_p^2 index. f is a dict point->index."""
    p = F.p
    y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
    c = F.idx[carry(u, x, p)]
    return F.ADD[F.SUB[f[y]][f[x]]][c]


def A_size(f, u, F):
    return len(set(d_u_val(f, u, x, F) for x in F.pts))


def dir_table(F, u):
    """[(x_index, (x+u)_index, carry_index)] for one direction u -- lets the
    inner measurement loop touch no dicts."""
    p = F.p
    tab = []
    for x in F.pts:
        y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
        tab.append((F.idx[x], F.idx[y], F.idx[carry(u, x, p)]))
    return tab


def A_size_capped(fv, tab, ADD, SUB, cap):
    """|A_u(f)| computed from a FLAT value list, stopping as soon as `cap`
    distinct values are seen (returns exactly `cap` in that case).  cap=5 keeps
    every value <= 4 exact, which is all the rigidity question needs, and is
    ~5x cheaper than the full set build."""
    s = set()
    add = s.add
    for xi, yi, ci in tab:
        add(ADD[SUB[fv[yi]][fv[xi]]][ci])
        if len(s) >= cap:
            return cap
    return len(s)


def diffset_direct(f, F):
    """|T_f - T_f| computed literally inside (Z/p^2 Z)^2 -- no Sec.6 input."""
    p = F.p
    pp = p * p
    T = []
    for x in F.pts:
        fa, fb = F.pts[f[x]]
        T.append(((x[0] + p * fa) % pp, (x[1] + p * fb) % pp))
    D = set()
    for a in T:
        for b in T:
            D.add(((a[0] - b[0]) % pp, (a[1] - b[1]) % pp))
    return len(D)


# --------------------------------------------------------------- CONTROLS
def controls(primes):
    """Controls that CAN fail.  The published box (2p-1)^2 is 25 at p=3 and 81
    at p=5 in the paper; both are recomputed here from the definitions and
    compared, and the fibre-decomposition identity is checked against a literal
    difference-set computation that uses no Sec.6 machinery at all."""
    print("=" * 78)
    print("CONTROLS (each could fail; population stated beside each)")
    allok = True
    for p in primes:
        F = Fp2(p)
        f0 = dict((x, F.e(0, 0)) for x in F.pts)
        direct = diffset_direct(f0, F)
        fibre = sum(A_size(f0, u, F) for u in F.pts)
        box = (2 * p - 1) ** 2
        ok = (direct == fibre == box)
        allok = allok and ok
        print("  C-A p=%d  f==0 : |T-T| direct=%d  fibre-sum=%d  (2p-1)^2=%d  "
              "MATCH=%s   [population: 1 function]"
              % (p, direct, fibre, box, ok))
    # C-B: the cycle identity, on which PATH 2's parametrisation rests.
    p = 3
    F = Fp2(p)
    import random
    random.seed(20260823)
    bad = 0
    N = 300
    for _ in range(N):
        f = dict((x, random.randrange(F.n)) for x in F.pts)
        f[(0, 0)] = F.e(0, 0)
        for u in F.pts[1:]:
            for x in F.pts:
                s = F.e(0, 0)
                y = x
                for _i in range(p):
                    s = F.ADD[s][d_u_val(f, u, y, F)]
                    y = ((y[0] + u[0]) % p, (y[1] + u[1]) % p)
                if s != F.SUB[F.e(0, 0)][F.idx[(u[0] % p, u[1] % p)]]:
                    bad += 1
    print("  C-B p=3  cycle identity  sum_i d_u f(x+iu) == -u : violations=%d  "
          "[population: %d random f x %d directions x %d basepoints = %d checks]"
          % (bad, N, F.n - 1, F.n, N * (F.n - 1) * F.n))
    allok = allok and (bad == 0)
    # C-C: |A_w| is invariant under f -> f + lam*[x1] + mu*[x2]  (PATH 2's
    # reduction is lossless only if this holds).
    bad2 = 0
    M = 60
    for _ in range(M):
        f = dict((x, random.randrange(F.n)) for x in F.pts)
        f[(0, 0)] = F.e(0, 0)
        lam = random.randrange(F.n)
        mu = random.randrange(F.n)
        la, lb = F.pts[lam]
        ma, mb = F.pts[mu]
        g = {}
        for x in F.pts:
            fa, fb = F.pts[f[x]]
            g[x] = F.e(fa + la * x[0] + ma * x[1], fb + lb * x[0] + mb * x[1])
        for u in F.pts[1:]:
            if A_size(f, u, F) != A_size(g, u, F):
                bad2 += 1
    print("  C-C p=3  |A_u| invariant under f -> f+lam[x1]+mu[x2] : violations=%d "
          " [population: %d (f,lam,mu) x %d directions = %d checks]"
          % (bad2, M, F.n - 1, M * (F.n - 1)))
    allok = allok and (bad2 == 0)
    print("  CONTROLS ALL PASS = %s" % allok)
    return allok


# ------------------------------------------------------- PATH 1 : brute p=3
def path1_brute_p3():
    """Visit EVERY f: F_3^2 -> F_3^2 with f(0)=0.  Rows are triples of values;
    horizontal / vertical image sets are carried as 9-bit masks."""
    p = 3
    F = Fp2(p)
    n = F.n
    rows = list(itertools.product(range(n), repeat=p))       # f(0,j),f(1,j),f(2,j)
    nrows = len(rows)
    POP = nrows ** p // n                                    # f(0,0) pinned
    # horizontal derivative mask of a row (row index j is irrelevant: c_e1 does
    # not depend on x_2), plus the raw list of the p derivative values
    hmask = [0] * nrows
    for r, row in enumerate(rows):
        m = 0
        for i in range(p):
            c = F.idx[carry((1, 0), (i, 0), p)]
            m |= 1 << F.ADD[F.SUB[row[(i + 1) % p]][row[i]]][c]
        hmask[r] = m
    # vertical derivative mask between ordered rows, non-wrap and wrap
    vmask = [[0] * nrows for _ in range(nrows)]
    wmask = [[0] * nrows for _ in range(nrows)]
    c_mid = F.idx[carry((0, 1), (0, 0), p)]                  # x_2 + 1 < p
    c_wrp = F.idx[carry((0, 1), (0, p - 1), p)]              # x_2 + 1 == p
    for a in range(nrows):
        ra = rows[a]
        for b in range(nrows):
            rb = rows[b]
            mm = 0
            mw = 0
            for i in range(p):
                dd = F.SUB[rb[i]][ra[i]]
                mm |= 1 << F.ADD[dd][c_mid]
                mw |= 1 << F.ADD[dd][c_wrp]
            vmask[a][b] = mm
            wmask[a][b] = mw
    pc = [bin(k).count("1") for k in range(1 << n)]
    zero_rows = [r for r in range(nrows) if rows[r][0] == F.e(0, 0)]
    mixed = [(l, m) for l in range(1, p) for m in range(1, p)]
    survivors = 0
    minAw = dict((w, 99) for w in mixed)
    ctr = [0, 0]                                             # visited, pruned
    for r0 in zero_rows:
        if out_of_time():
            print("  PATH1 HARD TIMEOUT")
            return None
        h0 = hmask[r0]
        for r1 in range(nrows):
            h1 = h0 | hmask[r1]
            if pc[h1] > 3:
                ctr[1] += nrows
                continue
            v01 = vmask[r0][r1]
            if pc[v01] > 3:
                ctr[1] += nrows
                continue
            for r2 in range(nrows):
                ctr[0] += 1
                if pc[h1 | hmask[r2]] > 3:
                    continue
                vv = v01 | vmask[r1][r2] | wmask[r2][r0]
                if pc[vv] > 3:
                    continue
                survivors += 1
                f = {}
                for j, rr in enumerate((rows[r0], rows[r1], rows[r2])):
                    for i in range(p):
                        f[(i, j)] = rr[i]
                for w in mixed:
                    s = A_size(f, w, F)
                    if s < minAw[w]:
                        minAw[w] = s
    return dict(pop=POP, visited=ctr[0] + ctr[1], survivors=survivors,
                minAw=minAw, mixed=mixed, nrows=nrows)


# --------------------------------------------- PATH 2 : structured, any p
def build_words(F, A):
    """All length-p words over the index set A whose sum is -e1."""
    p = F.p
    tgt = F.SUB[F.e(0, 0)][F.e(1, 0)]
    out = []
    for w in itertools.product(A, repeat=p):
        s = F.e(0, 0)
        for a in w:
            s = F.ADD[s][a]
        if s == tgt:
            out.append(w)
    return out


def prefixes(F, w):
    P = [F.e(0, 0)]
    for i in range(len(w) - 1):
        P.append(F.ADD[P[-1]][w[i]])
    return P


def canonical_sets(F, k):
    """One representative per orbit of k-subsets under translation, together
    with the orbit size (= p^2 / |stabiliser|).  Stabilisers are trivial for
    k in {2,3} once p >= 5; at p=3 a 3-set can be a coset of a line and this
    routine finds that automatically."""
    n = F.n
    seen = set()
    reps = []
    for S in itertools.combinations(range(n), k):
        if S in seen:
            continue
        orb = set()
        for t in range(n):
            orb.add(tuple(sorted(F.ADD[s][t] for s in S)))
        seen |= orb
        reps.append((S, len(orb)))
    return reps


def path2(F, kmax=3, verbose_every=0, want_count=True):
    """DFS over (row word, row base).  Normalisations used, both from the free
    p^4 action f -> f + lam[x1] + mu[x2]:
        (i)  im d_e1 f is a CANONICAL representative of its translation orbit
        (ii) beta_0 := b_1 - b_0 = 0        (b_0 = 0 is forced by f(0)=0)
    Every f in the stratum is equivalent to exactly one such normal form per
    (lam,mu), and |A_w| is invariant, so the rigidity verdict is exact."""
    p = F.p
    n = F.n
    pc = [bin(k).count("1") for k in range(1 << n)]
    c_j = [F.idx[carry((0, 1), (0, j), p)] for j in range(p)]
    mixed = [(l, m) for l in range(1, p) for m in range(1, p)]
    nmixed = len(mixed)
    TABS = [dir_table(F, w) for w in mixed]
    ADDL = F.ADD
    SUBL = F.SUB
    FIDX = F.idx
    fv = [0] * n
    minAwL = [99] * nmixed
    reps = []
    for k in range(2, kmax + 1):
        reps.extend(canonical_sets(F, k))
    reps.sort(key=lambda t: (len(t[0]), t[0]))
    total_norm = 0
    total_full = 0
    ce = []
    done = 0
    for (A, orbsz) in reps:
        if out_of_time():
            break
        Aset = set(A)
        Amask = 0
        for a in A:
            Amask |= 1 << a
        W = build_words(F, A)
        done += 1
        if not W:
            continue
        P = [prefixes(F, w) for w in W]
        wm = []
        for w in W:
            m = 0
            for a in w:
                m |= 1 << a
            wm.append(m)
        nW = len(W)
        # Qset[i][j] = { P_j[x] - P_i[x] : x } ; pair is dead if |Qset| > 3
        Q = [[None] * nW for _ in range(nW)]
        for i in range(nW):
            for j in range(nW):
                qs = set(F.SUB[P[j][x]][P[i][x]] for x in range(p))
                Q[i][j] = tuple(sorted(qs)) if len(qs) <= kmax else None
        norm_here = 0

        def rec(j, wi, b, Bmask, Bcnt, hm, seq):
            """rows 0..j chosen; wi = word index of row j; b = b_j."""
            nonlocal norm_here
            if out_of_time():
                return
            if j == p - 1:
                # wrap transition j -> 0, base b_0 = 0
                q = Q[wi][seq[0][0]]
                if q is None:
                    return
                beta = F.ADD[F.SUB[F.e(0, 0)][b]][c_j[p - 1]]
                nb = Bmask
                for t in q:
                    nb |= 1 << F.ADD[beta][t]
                if pc[nb] > kmax:
                    return
                if hm != Amask:                      # EXACT image, not subset
                    return
                norm_here += 1
                # reconstruct f as a flat value list and measure every mixed w
                for jj in range(p):
                    bb = seq[jj][1]
                    PP = P[seq[jj][0]]
                    row = ADDL[bb]
                    for i in range(p):
                        fv[FIDX[(i, jj)]] = row[PP[i]]
                for wk in range(nmixed):
                    s = A_size_capped(fv, TABS[wk], ADDL, SUBL, 5)
                    if s < minAwL[wk]:
                        minAwL[wk] = s
                    if s <= 3 and len(ce) < 5:
                        ce.append((A, tuple(seq), mixed[wk], s))
                return
            for nj in range(nW):
                q = Q[wi][nj]
                if q is None:
                    continue
                nhm = hm | wm[nj]
                if pc[nhm] > kmax:
                    continue
                if j == 0:
                    betas = [F.e(0, 0)]              # normalisation (ii)
                else:
                    if Bcnt >= kmax:
                        cand = set()
                        for bb in range(n):
                            if (Bmask >> bb) & 1:
                                cand.add(F.SUB[bb][q[0]])
                        betas = sorted(cand)
                    else:
                        betas = range(n)
                for beta in betas:
                    nb = Bmask
                    for t in q:
                        nb |= 1 << F.ADD[beta][t]
                    if pc[nb] > kmax:
                        continue
                    nbase = F.SUB[F.ADD[b][beta]][c_j[j]]
                    seq.append((nj, nbase))
                    rec(j + 1, nj, nbase, nb, pc[nb], nhm, seq)
                    seq.pop()

        for i0 in range(nW):
            if out_of_time():
                break
            rec(0, i0, F.e(0, 0), 0, 0, wm[i0], [(i0, F.e(0, 0))])
        total_norm += norm_here
        total_full += norm_here * orbsz * n          # orbit of A, times mu
        if verbose_every and done % verbose_every == 0:
            print("    ... A-class %d/%d  cum normal-form f = %d  cum full = %d"
                  "  t=%.0fs" % (done, len(reps), total_norm, total_full,
                                 elapsed()))
    minAw = dict((mixed[k], minAwL[k]) for k in range(nmixed))
    return dict(reps=len(reps), done=done, norm=total_norm, full=total_full,
                minAw=minAw, mixed=mixed, ce=ce, complete=(done == len(reps)),
                cap=5)


# ------------------------------------------------------------------- main
def main():
    do_p5 = "--p5" in sys.argv
    ok = controls([3, 5])
    print("=" * 78)
    print("PATH 1 -- BRUTE, p=3, the ENTIRE function space")
    r1 = path1_brute_p3()
    if r1:
        print("  population (all f with f(0)=0) = %d = 3^(2*3^2-2)" % r1["pop"])
        print("  row alphabet = %d rows; triples enumerated/pruned = %d"
              % (r1["nrows"], r1["visited"]))
        print("  R2(3) [ |A_e1| <= 3 AND |A_e2| <= 3 ] = %d" % r1["survivors"])
        for w in r1["mixed"]:
            print("    min |A_w| over the WHOLE stratum, w=%s : %d"
                  % (str(w), r1["minAw"][w]))
        print("  t=%.1fs" % elapsed())
    print("=" * 78)
    print("PATH 2 -- STRUCTURED, p=3 (same question, disjoint counting logic)")
    F3 = Fp2(3)
    r2 = path2(F3)
    print("  A-classes (translation orbits of image sets, |A| in {2,3}) = %d"
          " ; completed = %d ; complete=%s"
          % (r2["reps"], r2["done"], r2["complete"]))
    print("  normal-form f found = %d ; de-normalised R2(3) = %d"
          % (r2["norm"], r2["full"]))
    for w in r2["mixed"]:
        print("    min |A_w| over the WHOLE stratum, w=%s : %d"
              % (str(w), r2["minAw"][w]))
    print("  counterexamples (|A_w| <= 3) recorded: %d" % len(r2["ce"]))
    print("  t=%.1fs" % elapsed())

    print("=" * 78)
    print("CROSS-CHECK p=3")
    if r1:
        agree = (r1["survivors"] == r2["full"])
        print("  PATH1 R2(3)=%d   PATH2 R2(3)=%d   AGREE=%s"
              % (r1["survivors"], r2["full"], agree))
        mm = all(r1["minAw"][w] == r2["minAw"][w] for w in r1["mixed"])
        print("  min|A_w| tables agree across the two paths: %s" % mm)
        allmin = min(r1["minAw"].values())
        print("  VERDICT p=3: min over ALL mixed w and ALL stratum members = %d"
              "  (rigidity |A_w| >= 4 holds: %s)" % (allmin, allmin >= 4))

    if do_p5:
        print("=" * 78)
        print("PATH 2 -- STRUCTURED, p=5.  Partial coverage is reported as"
              " partial: each A-class is a COMPLETE sub-population, so a"
              " prefix of the class list is a rigorous statement about that"
              " prefix and about nothing else.")
        F5 = Fp2(5)
        r5 = path2(F5, verbose_every=1)
        print("  A-classes total = %d ; COMPLETED = %d ; complete=%s"
              % (r5["reps"], r5["done"], r5["complete"]))
        print("  normal-form f found in the completed classes = %d"
              % r5["norm"])
        print("  de-normalised stratum count over completed classes = %d"
              % r5["full"])
        worst = min(r5["minAw"].values()) if r5["minAw"] else None
        print("  min |A_w| over completed classes, all %d mixed w = %s"
              % (len(r5["mixed"]), worst))
        print("  counterexamples (|A_w| <= 3) recorded: %d" % len(r5["ce"]))
        for c in r5["ce"]:
            print("    CE  A=%s  w=%s  |A_w|=%d" % (str(c[0]), str(c[2]), c[3]))
    print("=" * 78)
    print("elapsed_s = %.1f  ; controls_ok = %s" % (elapsed(), ok))


if __name__ == "__main__":
    main()
