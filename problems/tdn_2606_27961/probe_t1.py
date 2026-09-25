#!/usr/bin/env python3
"""PROBE T-1 -- arXiv:2606.27961 (Barcau-Pasol-Turcas, transversal difference numbers).

Question: do the Sec.6 cycle/curl constraints leave a SUB-EXPONENTIAL residual
search space at p=7?

Everything here is either (a) a positive control against the paper's PUBLISHED
numbers, or (b) an exact count / explicit construction.  NO exhaustive search
over the full function space is performed at any p.  Every population is printed
beside every count.

Objects (Sec.6 of the source, subsec:carry-corrected-derivatives):
  G_p = (Z/p^2 Z)^2, H_p = p G_p,  G_p/H_p = F_p^2
  [x]           = coordinatewise standard lift into {0..p-1}^2
  T_f           = { [x] + p [f(x)] : x in F_p^2 },  f(0)=0
  c_u(x)        = ([x+u] - [x] - [u]) / p        (coords 0 or -1 mod p)
  d_u f(x)      = f(x+u) - f(x) + c_u(x)
  A_u(f)        = { d_u f(x) : x in F_p^2 }
  |T_f - T_f|   = sum_u |A_u(f)|                 (Lemma fibre decomposition)

Run:  .venv/bin/python3 problems/tdn_2606_27961/probe_t1.py
      (no third-party imports; either interpreter works)
"""
import itertools
import random
import sys
import time
from math import comb

T_START = time.time()
HARD_TIMEOUT_S = 900          # self-limit, hard constraint 3
SEED = 20260823
random.seed(SEED)


def budget_left():
    return HARD_TIMEOUT_S - (time.time() - T_START)


def check_clock(tag):
    if budget_left() <= 0:
        print("HARD TIMEOUT hit at stage %s -- aborting" % tag)
        sys.exit(2)


# ---------------------------------------------------------------- primitives
def points(p):
    return [(a, b) for a in range(p) for b in range(p)]


def carry(u, x, p):
    """c_u(x) in F_p^2; coordinates 0 or -1."""
    return ((0 if x[0] + u[0] < p else -1) % p,
            (0 if x[1] + u[1] < p else -1) % p)


def d_u(f, u, x, p):
    y = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
    c = carry(u, x, p)
    return ((f[y][0] - f[x][0] + c[0]) % p,
            (f[y][1] - f[x][1] + c[1]) % p)


def A_of(f, u, p, pts):
    return set(d_u(f, u, x, p) for x in pts)


def profile(f, p, pts):
    """dict u -> |A_u(f)|"""
    return dict((u, len(A_of(f, u, p, pts))) for u in pts)


def diffset_size_direct(f, p, pts):
    """|T_f - T_f| computed literally in (Z/p^2 Z)^2, independent of Sec.6."""
    pp = p * p
    T = [((x[0] + p * f[x][0]) % pp, (x[1] + p * f[x][1]) % pp) for x in pts]
    D = set()
    for a in T:
        for b in T:
            D.add(((a[0] - b[0]) % pp, (a[1] - b[1]) % pp))
    return len(D)


def diffset_size_fibre(f, p, pts):
    return sum(len(A_of(f, u, p, pts)) for u in pts)


def zero_f(p, pts):
    return dict((x, (0, 0)) for x in pts)


def random_f(p, pts):
    f = dict((x, (random.randrange(p), random.randrange(p))) for x in pts)
    f[(0, 0)] = (0, 0)
    return f


# ------------------------------------------------- CONTROL A : published box
# Values printed in subsec:small-prime-certificates of arXiv:2606.27961 for the
# coordinate box (delta at p=3 and p=5).  Transcribed from the LaTeX source; the
# run below must reproduce them from scratch.
PUBLISHED_BOX = {3: 25, 5: 81}
PUBLISHED_EXCLUDED_AT_MOST = {3: 23, 5: 79}


def control_A(primes):
    print("=" * 78)
    print("CONTROL A -- coordinate box f == 0, against the paper's PUBLISHED delta values.")
    print("population: 1 function per prime (f == 0); two independent computations each.")
    ok = True
    for p in primes:
        pts = points(p)
        f = zero_f(p, pts)
        direct = diffset_size_direct(f, p, pts)
        fibre = diffset_size_fibre(f, p, pts)
        expect = (2 * p - 1) ** 2
        pub = PUBLISHED_BOX.get(p)
        agree = (direct == fibre == expect) and (pub is None or direct == pub)
        ok = ok and agree
        print("  p=%d  |T-T| direct=%d  fibre-sum=%d  (2p-1)^2=%d  paper=%s  MATCH=%s"
              % (p, direct, fibre, expect, pub, agree))
    print("CONTROL A verdict:", "PASS" if ok else "FAIL")
    return ok


# ------------------------------------------- CONTROL B : Sec.6 lemmas on random f
def control_B(primes, n_samples):
    print("=" * 78)
    print("CONTROL B -- Sec.6 identities/lemmas tested on uniform random f (f(0)=0).")
    allok = True
    for p in primes:
        pts = points(p)
        lo_thm = 3 * p * p - p - 1
        n_fib = n_odd = n_lb = n_ge2 = n_line = n_curl = n_cyc = 0
        n_line_pop = 0
        for _ in range(n_samples):
            check_clock("B p=%d" % p)
            f = random_f(p, pts)
            direct = diffset_size_direct(f, p, pts)
            fibre = diffset_size_fibre(f, p, pts)
            n_fib += (direct == fibre)
            n_odd += (direct % 2 == 1)
            n_lb += (direct >= lo_thm)
            prof = profile(f, p, pts)
            n_ge2 += all(prof[u] >= 2 for u in pts if u != (0, 0))
            # 2-point images lie on a line parallel to <u>
            good_line = True
            for u in pts:
                if u == (0, 0) or prof[u] != 2:
                    continue
                n_line_pop += 1
                a, b = sorted(A_of(f, u, p, pts))
                dd = ((a[0] - b[0]) % p, (a[1] - b[1]) % p)
                # dd in <u>  <=>  dd[0]*u[1] - dd[1]*u[0] == 0 mod p
                if (dd[0] * u[1] - dd[1] * u[0]) % p != 0:
                    good_line = False
            n_line += good_line
            # curl identity, random u,v,x
            cu = True
            for _t in range(5):
                u = random.choice(pts)
                v = random.choice(pts)
                x = random.choice(pts)
                xv = ((x[0] + v[0]) % p, (x[1] + v[1]) % p)
                xu = ((x[0] + u[0]) % p, (x[1] + u[1]) % p)
                lhs = tuple((d_u(f, u, xv, p)[i] - d_u(f, u, x, p)[i]) % p for i in range(2))
                rhs = tuple((d_u(f, v, xu, p)[i] - d_u(f, v, x, p)[i]) % p for i in range(2))
                cu = cu and (lhs == rhs)
            n_curl += cu
            # cycle identity, random nonzero u and base x
            cy = True
            for _t in range(5):
                u = random.choice(pts)
                if u == (0, 0):
                    continue
                x = random.choice(pts)
                s = [0, 0]
                for i in range(p):
                    y = ((x[0] + i * u[0]) % p, (x[1] + i * u[1]) % p)
                    dv = d_u(f, u, y, p)
                    s[0] = (s[0] + dv[0]) % p
                    s[1] = (s[1] + dv[1]) % p
                cy = cy and (tuple(s) == ((-u[0]) % p, (-u[1]) % p))
            n_cyc += cy
        print("  p=%d  population=%d random f" % (p, n_samples))
        print("     fibre-sum == direct           : %d/%d" % (n_fib, n_samples))
        print("     |T-T| odd                     : %d/%d" % (n_odd, n_samples))
        print("     |T-T| >= 3p^2-p-1 = %-5d     : %d/%d" % (lo_thm, n_lb, n_samples))
        print("     |A_u| >= 2 for all u != 0     : %d/%d" % (n_ge2, n_samples))
        print("     2-pt A_u parallel to <u>      : %d/%d  (2-pt directions seen: %d)"
              % (n_line, n_samples, n_line_pop))
        print("     curl identity                 : %d/%d" % (n_curl, n_samples))
        print("     cycle identity                : %d/%d" % (n_cyc, n_samples))
        allok = allok and (n_fib == n_odd == n_lb == n_ge2 == n_line == n_curl == n_cyc == n_samples)
    print("CONTROL B verdict:", "PASS" if allok else "FAIL")
    return allok


# ----------------------------------- CONTROL C : GL2 is a symmetry of |T-T|
def gl2_mod_p2_random(p):
    pp = p * p
    while True:
        m = [[random.randrange(pp) for _ in range(2)] for _ in range(2)]
        det = (m[0][0] * m[1][1] - m[0][1] * m[1][0]) % pp
        if det % p != 0:
            return m


def apply_M_to_T(M, f, p, pts):
    pp = p * p
    T = [((x[0] + p * f[x][0]) % pp, (x[1] + p * f[x][1]) % pp) for x in pts]
    return [((M[0][0] * t[0] + M[0][1] * t[1]) % pp,
             (M[1][0] * t[0] + M[1][1] * t[1]) % pp) for t in T]


def dsize_of_set(T, p):
    pp = p * p
    D = set()
    for a in T:
        for b in T:
            D.add(((a[0] - b[0]) % pp, (a[1] - b[1]) % pp))
    return len(D)


def control_C(p, n_samples):
    print("=" * 78)
    print("CONTROL C -- GL_2(Z/p^2 Z) preserves |T-T| (the WLOG used below).")
    pts = points(p)
    ok = 0
    for _ in range(n_samples):
        check_clock("C")
        f = random_f(p, pts)
        base = diffset_size_direct(f, p, pts)
        M = gl2_mod_p2_random(p)
        MT = apply_M_to_T(M, f, p, pts)
        ok += (len(set(MT)) == p * p and dsize_of_set(MT, p) == base)
    print("  p=%d  population=%d (random f, random M in GL_2(Z/p^2Z))" % (p, n_samples))
    print("     M(T) is a transversal AND |M(T)-M(T)| == |T-T| : %d/%d" % (ok, n_samples))
    print("CONTROL C verdict:", "PASS" if ok == n_samples else "FAIL")
    return ok == n_samples


# ---------------------------- profile arithmetic forced by Sec.6 + the target
def forced_profile(p):
    """What Sec.6 + '|T_f-T_f| <= box-2' force on the multiset {|A_u| : u != 0}."""
    box = (2 * p - 1) ** 2
    target = box - 2                      # largest odd value below the box
    sum_nonzero = target - 1              # A_0 = {0}
    ndirs = p * p - 1
    n2_max = p - 1                        # Case B: S inside one line
    # sum_{k>=4}(k-3) n_k <= sum_nonzero - 3*ndirs + n2
    excess_max = sum_nonzero - 3 * ndirs + n2_max
    n3_min = ndirs - n2_max - excess_max
    return dict(box=box, target=target, sum_nonzero=sum_nonzero, ndirs=ndirs,
                n2_max=n2_max, excess_max=excess_max, n3_min=n3_min)


def report_profiles(primes):
    print("=" * 78)
    print("SEC.6 FORCED PROFILE  (Case A lemma + Thm 3p^2-p-1 + the objective)")
    print("  columns: box=(2p-1)^2, target=largest odd < box, n2_max=p-1,")
    print("           n3_min = #directions forced to have |A_u| EXACTLY 3")
    for p in primes:
        d = forced_profile(p)
        print("  p=%2d  box=%-5d target<=%-5d dirs=%-4d n2<=%-3d excess<=%-4d n3>=%-3d  "
              "two-independent-3-dirs forced: %s"
              % (p, d["box"], d["target"], d["ndirs"], d["n2_max"], d["excess_max"],
                 d["n3_min"], d["n3_min"] > p - 1))


# ------------------- exact count of words with prescribed alphabet and sum
def words_with_sum(A, p, target):
    """#(length-p words over alphabet A subset F_p^2) whose sum is target."""
    cur = {(0, 0): 1}
    for _ in range(p):
        nxt = {}
        for s, c in cur.items():
            for a in A:
                t = ((s[0] + a[0]) % p, (s[1] + a[1]) % p)
                nxt[t] = nxt.get(t, 0) + c
        cur = nxt
    return cur.get(target, 0)


def count_g_with_image_in(A, p, target):
    """#{g : F_p^2 -> F_p^2, im g subset A, every u-line sums to target}
       = words_with_sum(A)^p   (p independent lines of p points)."""
    return words_with_sum(A, p, target) ** p


def exact_R1(p, kmax=3):
    """EXACT #{f : F_p^2->F_p^2, f(0)=0, |A_{e1}(f)| <= kmax}.

    Bijection (proved in the write-up): f <-> (g = d_{e1}f, one base value per
    e1-line), where g ranges over functions with every e1-line summing to -e1
    (this IS the cycle identity), and the base values contribute p^(2p-2) after
    normalising f(0)=0.  Inclusion-exclusion over the image alphabet.
    Translation invariance: words_with_sum(A+t) == words_with_sum(A) because the
    p symbols shift the sum by p*t == 0, so only translation classes are needed.
    """
    pts = points(p)
    target = ((-1) % p, 0)                       # -e1
    # M(A) = #g with im g subset A, for |A| <= kmax ; sum with Mobius weights
    # #{|im g| <= kmax} = sum_{|A|<=kmax} sum_{B subset A} (-1)^(|A|-|B|) M(B)
    #                  = sum_{|B|<=kmax} M(B) * sum_{j=0}^{kmax-|B|} (-1)^j C(N-|B|, j)
    N = p * p
    total = 0
    per_size = {}
    for k in range(0, kmax + 1):
        weight = sum((-1) ** j * comb(N - k, j) for j in range(0, kmax - k + 1))
        if k == 0:
            sub = 1 if target == (0, 0) else 0          # empty alphabet: no g
            sub = 0
            per_size[k] = 0
            continue
        acc = 0
        # enumerate translation classes: fix A to contain (0,0), then multiply by N/k
        seen = 0
        for rest in itertools.combinations([q for q in pts if q != (0, 0)], k - 1):
            check_clock("R1 p=%d k=%d" % (p, k))
            A = ((0, 0),) + rest
            w = words_with_sum(A, p, target)
            acc += w ** p
            seen += 1
        # each unordered k-set has exactly k translates containing (0,0)?  No:
        # the translation class of A has N members (t ranges over F_p^2), of
        # which exactly k contain (0,0).  Enumerating all A that contain (0,0)
        # therefore counts every class exactly k times, and each class member
        # has the same w.  So sum over ALL k-sets = (N/k) * acc.
        acc_all = acc * N // k
        per_size[k] = acc_all
        total += weight * acc_all
    base_free = p ** (2 * p - 2)
    return total * base_free, per_size, base_free


# ---------------- two-direction residual: exact at p=3, bounds at p=5,7
def exact_R_two_dirs(p, kmax=3):
    """EXACT #{f : f(0)=0, |A_{e1}(f)| <= kmax and |A_{e2}(f)| <= kmax}.
    Enumerates only the |A_{e1}|<=kmax stratum (never the full space)."""
    pts = points(p)
    e1, e2 = (1, 0), (0, 1)
    target1 = ((-1) % p, 0)
    N = p * p
    # all g with |im g| <= kmax and every e1-line summing to -e1
    alphabets = []
    for k in range(2, kmax + 1):
        for A in itertools.combinations(pts, k):
            alphabets.append(A)
    rows = list(range(p))
    total = 0
    seen_g = 0
    seen_f = 0
    gset = set()
    for A in alphabets:
        check_clock("R2 p=%d" % p)
        wlist = [w for w in itertools.product(A, repeat=p)
                 if (sum(a[0] for a in w) % p, sum(a[1] for a in w) % p) == target1]
        if not wlist:
            continue
        for choice in itertools.product(wlist, repeat=p):
            # g(x1, x2) = choice[x2][x1]
            g = {}
            for x2 in rows:
                for x1 in range(p):
                    g[(x1, x2)] = choice[x2][x1]
            key = tuple(g[x] for x in pts)
            if key in gset:
                continue
            gset.add(key)
            seen_g += 1
            # rebuild f for every choice of base values (one per e1-line, f(0,0)=0)
            for bases in itertools.product(pts, repeat=p - 1):
                base = ((0, 0),) + bases
                f = {}
                for x2 in rows:
                    cur = base[x2]
                    f[(0, x2)] = cur
                    for x1 in range(p - 1):
                        c = carry(e1, (x1, x2), p)
                        cur = ((cur[0] + g[(x1, x2)][0] - c[0]) % p,
                               (cur[1] + g[(x1, x2)][1] - c[1]) % p)
                        f[(x1 + 1, x2)] = cur
                seen_f += 1
                if len(A_of(f, e2, p, pts)) <= kmax:
                    total += 1
    return total, seen_g, seen_f


# ------------- p=3 decisive control: reproduce "no |T_f-T_f| <= 23" from Sec.6
def control_D_p3():
    """At p=3, Sec.6 forces a counterexample to have n2 = p-1 = 2, i.e. S is the
    full nonzero part of ONE line; GL_2(F_3) is transitive on lines, so WLOG
    |A_{e1}(f)| = 2.  Enumerating that stratum is a few 10^5 functions instead of
    9^8 = 43 million, and it must contain no f with |T_f-T_f| <= 23."""
    p = 3
    pts = points(p)
    e1 = (1, 0)
    target1 = ((-1) % p, 0)
    box = (2 * p - 1) ** 2
    tgt = box - 2
    best = None
    pop = 0
    for A in itertools.combinations(pts, 2):
        wlist = [w for w in itertools.product(A, repeat=p)
                 if (sum(a[0] for a in w) % p, sum(a[1] for a in w) % p) == target1]
        if not wlist:
            continue
        for choice in itertools.product(wlist, repeat=p):
            g = {}
            for x2 in range(p):
                for x1 in range(p):
                    g[(x1, x2)] = choice[x2][x1]
            for bases in itertools.product(pts, repeat=p - 1):
                check_clock("D")
                base = ((0, 0),) + bases
                f = {}
                for x2 in range(p):
                    cur = base[x2]
                    f[(0, x2)] = cur
                    for x1 in range(p - 1):
                        c = carry(e1, (x1, x2), p)
                        cur = ((cur[0] + g[(x1, x2)][0] - c[0]) % p,
                               (cur[1] + g[(x1, x2)][1] - c[1]) % p)
                        f[(x1 + 1, x2)] = cur
                if len(A_of(f, e1, p, pts)) > 2:
                    continue
                pop += 1
                v = diffset_size_fibre(f, p, pts)
                if best is None or v < best:
                    best = v
    print("=" * 78)
    print("CONTROL D -- p=3, Sec.6-restricted stratum |A_{e1}(f)| <= 2 (WLOG by GL_2).")
    print("  population enumerated: %d functions f with f(0)=0 and |A_{e1}(f)|<=2" % pop)
    print("  full space for comparison: %d" % (p ** (2 * p * p - 2)))
    print("  minimum |T_f-T_f| over that stratum: %s   (largest odd below box = %d, box = %d)"
          % (best, tgt, box))
    print("  paper's published p=3 exclusion threshold: %d" % PUBLISHED_EXCLUDED_AT_MOST[p])
    passed = (best is not None and best >= box and best > PUBLISHED_EXCLUDED_AT_MOST[p])
    print("CONTROL D verdict:", "PASS -- reproduces the paper's p=3 exclusion" if passed else "FAIL")
    return passed, pop, best


# ---------------- explicit exponential family inside the two-direction residual
def height_family_members(p, n_samples):
    """f(x) = (x1 + x2 + eta(x) mod p, 0) with eta: F_p^2 -> {0,1} constrained by
    eta(0,.) = eta(p-1,.) and eta(.,0) = eta(.,p-1).  Claim: every such f has
    |A_{e1}(f)| <= 3 and |A_{e2}(f)| <= 3, so the whole family sits inside the
    Sec.6 two-direction residual.  Family size printed below; here we VERIFY the
    claim on random members."""
    pts = points(p)
    e1, e2 = (1, 0), (0, 1)
    ok1 = ok2 = 0
    prof_ok = 0
    for _ in range(n_samples):
        check_clock("H")
        eta = {}
        for x1 in range(p):
            for x2 in range(p):
                eta[(x1, x2)] = random.randrange(2)
        for x2 in range(p):
            eta[(p - 1, x2)] = eta[(0, x2)]
        for x1 in range(p):
            eta[(x1, p - 1)] = eta[(x1, 0)]
        eta[(p - 1, p - 1)] = eta[(0, 0)]
        f = dict(((x1, x2), ((x1 + x2 + eta[(x1, x2)]) % p, 0))
                 for x1 in range(p) for x2 in range(p))
        c0 = f[(0, 0)]
        f = dict((x, ((f[x][0] - c0[0]) % p, (f[x][1] - c0[1]) % p)) for x in pts)
        ok1 += (len(A_of(f, e1, p, pts)) <= 3)
        ok2 += (len(A_of(f, e2, p, pts)) <= 3)
    # eta is free on the (p-1)^2 cells with x1<p-1 and x2<p-1; the last row and
    # last column are forced by the two wrap conditions.  f depends on eta only
    # through eta(x)-eta(0,0), so the map eta -> f is exactly 2-to-1; fixing
    # eta(0,0)=0 leaves (p-1)^2 - 1 free bits, all giving DISTINCT f.
    free_bits = (p - 1) ** 2 - 1
    size = 2 ** free_bits
    return ok1, ok2, n_samples, free_bits, size


def main():
    primes_small = [3, 5]
    a = control_A([3, 5, 7])
    b = control_B(primes_small, 200)
    c = control_C(3, 60)
    report_profiles([3, 5, 7, 11])
    d_ok, d_pop, d_best = control_D_p3()

    print("=" * 78)
    print("RESIDUAL SIZE 1 -- EXACT count of the ONE-direction Sec.6 stratum")
    print("  R1(p) = #{f : f(0)=0, |A_{e1}(f)| <= 3};  full space = p^(2p^2-2)")
    for p in [3, 5, 7]:
        check_clock("R1 loop")
        r1, per_size, base_free = exact_R1(p, kmax=3)
        full = p ** (2 * p * p - 2)
        print("  p=%d  R1 = %d   (~%.3e)   full = %d  (~%.3e)   ratio = %.3e"
              % (p, r1, float(r1), full, float(full), float(r1) / float(full)))
        print("        base-value factor p^(2p-2) = %d ; alphabet strata sizes: %s"
              % (base_free, dict((k, "%.3e" % float(v)) for k, v in per_size.items())))

    print("=" * 78)
    print("RESIDUAL SIZE 2 -- TWO-direction stratum (every counterexample is")
    print("  GL_2-equivalent to one of these, because n3_min > p-1 forces two")
    print("  INDEPENDENT directions with |A_u| = 3, and GL_2 is simply transitive")
    print("  on ordered bases).")
    p = 3
    r2, seen_g, seen_f = exact_R_two_dirs(p, kmax=3)
    full3 = p ** (2 * p * p - 2)
    print("  p=3 EXACT R2 = %d   (population scanned: %d distinct g, %d f)  full = %d"
          % (r2, seen_g, seen_f, full3))

    print("=" * 78)
    print("RESIDUAL SIZE 3 -- explicit EXPONENTIAL family inside the two-direction")
    print("  residual (rigorous LOWER bound on R2).")
    for p in [3, 5, 7, 11]:
        ok1, ok2, n, bits, size = height_family_members(p, 60)
        print("  p=%2d  verified |A_e1|<=3 : %d/%d ; |A_e2|<=3 : %d/%d ; "
              "free bits = %d ; family size = 2^%d = %d (~%.3e)"
              % (p, ok1, n, ok2, n, bits, bits, size, float(size)))

    print("=" * 78)
    print("elapsed_s = %.1f ; controls A/B/C/D = %s/%s/%s/%s"
          % (time.time() - T_START, a, b, c, d_ok))


if __name__ == "__main__":
    main()
