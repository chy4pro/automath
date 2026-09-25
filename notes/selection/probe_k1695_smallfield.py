#!/usr/bin/env python3
"""SELECTION PROBE P-K1 (2026-08-24): Kourovka 16.95 small-case exhaustive scan.

Question: does a counterexample to Thompson's 16.95 (some invertible A over a small
field with NO permutation P making AP cyclic) exist in the fully-checkable range?
  - n=2: F2,F3,F5,F7   - n=3: F2,F3,F5   - n=4: F2
All INVERTIBLE A enumerated (population = |GL(n,q)|, printed and checked against the
known order formula), all n! permutations tried with early exit.

Either outcome materially updates solvability:
  - a hit  => 16.95 REFUTED with a seconds-verifiable Kind-1 certificate (major);
  - no hit => census: 16.95 holds on all of GL(n,q) for these (n,q); the counterexample,
    if any, lives at n>=4,q>=3 or n>=5 — informs the line's search frontier.

Controls:
  POSITIVE (must find witness): companion matrix of x^n-1 has AP cyclic at P=I.
  NEGATIVE (checker must reject): identity matrix I itself is NOT cyclic for n>=2
    (minpoly deg 1), so cyclic() must return False on I.
  ORDER CHECK: enumerated |GL(n,q)| must equal prod_{i}(q^n - q^i).

Hard timeout 600 s wall, single process, checkpoint per (n,q) block to stdout
(line-buffered). Pure stdlib.
"""
import sys, time, itertools
sys.stdout.reconfigure(line_buffering=True)
T0 = time.time()
HARD_LIMIT = 600.0

def check_time():
    if time.time() - T0 > HARD_LIMIT:
        print("HARD TIMEOUT at %.1fs -- partial results above stand as stated" % (time.time()-T0))
        sys.exit(2)

def matmul(A, B, n, q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(n)) % q for j in range(n)) for i in range(n))

def det(A, n, q):
    # Gaussian elimination mod prime q
    M = [list(r) for r in A]
    d = 1
    for c in range(n):
        piv = None
        for r in range(c, n):
            if M[r][c] % q:
                piv = r; break
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]; d = -d
        inv = pow(M[c][c], q-2, q)
        d = d * M[c][c] % q
        for r in range(c+1, n):
            if M[r][c]:
                f = M[r][c] * inv % q
                for k in range(c, n):
                    M[r][k] = (M[r][k] - f*M[c][k]) % q
    return d % q

def cyclic(M, n, q):
    # minpoly degree == n  <=>  I,M,...,M^(n-1) lin indep and M^n dependent (automatic).
    # Row-reduce flattened powers incrementally; cyclic iff rank of first n powers == n.
    rows = []  # reduced rows, each a list len n*n, with pivot index
    P = tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))
    cur = P
    rank = 0
    for _ in range(n):
        v = [cur[i][j] for i in range(n) for j in range(n)]
        for (piv, rw) in rows:
            if v[piv]:
                f = v[piv]
                for k in range(piv, n*n):
                    v[k] = (v[k] - f*rw[k]) % q
        piv = next((i for i, x in enumerate(v) if x), None)
        if piv is None:
            return False  # minpoly degree < n
        inv = pow(v[piv], q-2, q)
        v = [x*inv % q for x in v]
        rows.append((piv, v))
        rank += 1
        cur = matmul(cur, M, n, q)
    return True

def perms_mats(n):
    out = []
    for sigma in itertools.permutations(range(n)):
        out.append((sigma, tuple(tuple(1 if sigma[i]==j else 0 for j in range(n)) for i in range(n))))
    return out

def gl_order(n, q):
    o = 1
    for i in range(n):
        o *= q**n - q**i
    return o

def companion_xn_minus_1(n):
    # C e_j = e_{j+1}, last column from x^n = 1
    M = [[0]*n for _ in range(n)]
    for i in range(1, n):
        M[i][i-1] = 1
    M[0][n-1] = 1
    return tuple(tuple(r) for r in M)

def scan(n, q):
    check_time()
    P_list = perms_mats(n)
    # controls
    I = tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))
    assert not cyclic(I, n, q), "NEGATIVE CONTROL FAILED: I judged cyclic (n=%d,q=%d)" % (n, q)
    C = companion_xn_minus_1(n)
    assert any(cyclic(matmul(C, PM, n, q), n, q) for _, PM in P_list), \
        "POSITIVE CONTROL FAILED: companion x^n-1 has no cyclic AP (n=%d,q=%d)" % (n, q)
    total_inv = 0
    bad = []  # counterexamples
    cells = itertools.product(range(q), repeat=n*n)
    for flat in cells:
        A = tuple(tuple(flat[i*n+j] for j in range(n)) for i in range(n))
        if det(A, n, q) == 0:
            continue
        total_inv += 1
        if total_inv % 200000 == 0:
            check_time()
        ok = False
        for _, PM in P_list:
            if cyclic(matmul(A, PM, n, q), n, q):
                ok = True
                break
        if not ok:
            bad.append(A)
            if len(bad) >= 3:
                break
    expect = gl_order(n, q)
    order_ok = (total_inv == expect) if not bad else "n/a(early-exit)"
    print("n=%d q=%d  |GL| enumerated=%d expected=%d order_ok=%s  counterexamples=%d  elapsed=%.1fs"
          % (n, q, total_inv, expect, order_ok, len(bad), time.time()-T0))
    for A in bad:
        print("  COUNTEREXAMPLE A =", A)
    return bad

print("PROBE P-K1 start; hard limit %ds" % HARD_LIMIT)
any_bad = False
for (n, q) in [(2,2),(2,3),(2,5),(2,7),(3,2),(3,3),(4,2),(3,5)]:
    bad = scan(n, q)
    if bad:
        any_bad = True
print("VERDICT:", "COUNTEREXAMPLE FOUND -- 16.95 refuted in scanned range" if any_bad
      else "NO counterexample in any scanned cell -- 16.95 holds on all of GL(n,q) for the cells above")
print("total elapsed %.1fs" % (time.time()-T0))
