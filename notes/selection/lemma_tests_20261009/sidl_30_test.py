import math, time
from fractions import Fraction
T0 = time.process_time()
W0 = time.time()
OUT = []
def P(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)

class GenErr(Exception): pass

# ---------- sanity: A143824 ----------
def Fbrute(N):
    best = 0
    def rec(start, A, diffs):
        nonlocal best
        best = max(best, len(A))
        for x in range(start, N):
            nd = [x - a for a in A]
            if len(set(nd)) == len(nd) and not any(d in diffs for d in nd):
                rec(x + 1, A + [x], diffs | set(nd))
    rec(0, [], frozenset())
    return best
EXPECT = [1,2,2,3,3,3,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,6,6,6]
got = [Fbrute(n) for n in range(1, 26)]
SANITY = (got == EXPECT)
P("SANITY F(1..25) brute force == A143824 expected:", SANITY, got)

# ---------- core test ----------
def Tof(N):
    lo, hi = 1, N
    while lo < hi:
        m = (lo + hi) // 2
        if 10000 * m**4 >= 38809 * N**3: hi = m
        else: lo = m + 1
    assert 10000 * lo**4 >= 38809 * N**3 and (lo == 1 or 10000 * (lo-1)**4 < 38809 * N**3)
    assert lo <= N
    return lo

def test_set(N, A, stats, ctx, witnesses):
    """returns 'skip' / 'ok' / 'cex'"""
    A = sorted(A); k = len(A)
    if N < 4096 or k * k < N: return 'skip'
    seen = bytearray(N); cnt = 0
    for j in range(k):
        aj = A[j]
        for i in range(j):
            d = aj - A[i]
            if seen[d]: raise GenErr("not strong Sidon: repeated difference %d; ctx=%s N=%d A=%s" % (d, ctx, N, A))
            seen[d] = 1; cnt += 1
    if cnt != k*(k-1)//2: raise GenErr("difference count wrong")
    T = Tof(N)
    S = 0; miss = 0
    for d in range(1, T):
        if not seen[d]:
            S += 4*T**3 - 6*d*T*T + 2*d**3; miss += 1
    lhs, rhs = 100*S, 3*k*T**3
    g = math.gcd(lhs, rhs)
    rho = (lhs//g, rhs//g)
    stats['rho'].append((rho, ctx, N, k, T, S))
    stats['miss'].append((miss, ctx, N))
    # rho_rand = 100*R/k, R=(2/15)T^2/N  => 200 T^2 / (15 N k)
    stats['rr'].append(Fraction(200*T*T, 15*N*k))
    if lhs < rhs:
        S2 = sum(4*T**3 - 6*d*T*T + 2*d**3 for d in range(1, T) if all(d != A[j]-A[i] for i in range(0)) and not seen[d])
        missing = [d for d in range(1, T) if not seen[d]]
        S2 = sum(4*T**3 - 6*d*T*T + 2*d**3 for d in missing)
        witnesses.append(dict(ctx=ctx, N=N, A=A, k=k, T=T, S=S, S2=S2, lhs=lhs, rhs=rhs, missing=missing))
        return 'cex'
    return 'ok'

# ---------- main family ----------
def factor(n):
    f = []; q = 2
    while q*q <= n:
        if n % q == 0:
            f.append(q)
            while n % q == 0: n //= q
        q += 1
    if n > 1: f.append(n)
    return f

def bose_set(p):
    M = p*p - 1
    delta = next(d for d in range(2, p) if pow(d, (p-1)//2, p) == p-1)
    one = (1, 0)
    def mul(x, y): return ((x[0]*y[0] + delta*x[1]*y[1]) % p, (x[0]*y[1] + x[1]*y[0]) % p)
    def pw(x, e):
        r = one
        while e:
            if e & 1: r = mul(r, x)
            x = mul(x, x); e >>= 1
        return r
    fs = factor(M)
    z = None
    for a in range(p):
        for b in range(p):
            if (a, b) == (0, 0): continue
            if all(pw((a, b), M//l) != one for l in fs): z = (a, b); break
        if z: break
    if pw(z, M) != one: raise GenErr("z^M != 1")
    pows = []; cur = one
    for i in range(M):
        pows.append(cur); cur = mul(cur, z)
    if len(set(pows)) != M: raise GenErr("powers not distinct")
    B = [i for i in range(M) if pows[i][1] == 1]
    if len(B) != p: raise GenErr("|B| != p")
    return M, z, B

def singer_set(p):
    M = p*p + p + 1; q = p**3
    h = None
    for a in range(p):
        for b in range(p):
            for c in range(p):
                if all((x**3 + a*x*x + b*x + c) % p for x in range(p)): h = (a, b, c); break
            if h: break
        if h: break
    a, b, c = h
    def mul(u, v):
        r = [0]*5
        for i in range(3):
            for j in range(3): r[i+j] += u[i]*v[j]
        for d in (4, 3):  # x^d reduce: x^3 = -(a x^2 + b x + c)
            co = r[d] % p; r[d] = 0
            if co:
                r[d-1] -= a*co; r[d-2] -= b*co; r[d-3] -= c*co
        return tuple(t % p for t in r[:3])
    one = (1, 0, 0)
    def pw(x, e):
        r = one
        while e:
            if e & 1: r = mul(r, x)
            x = mul(x, x); e >>= 1
        return r
    fs = factor(q - 1)
    th = None
    for u in range(p):
        for v in range(p):
            for w in range(p):
                g = (w, v, u)  # coeffs of 1, x, x^2 ordered lexicographically on (c0,c1,c2)
                g = (u, v, w)
                if g == (0, 0, 0): continue
                if all(pw(g, (q-1)//l) != one for l in fs): th = g; break
            if th: break
        if th: break
    if pw(th, q-1) != one: raise GenErr("theta^(q-1) != 1")
    cur = one; Bs = set(); seenp = set()
    for i in range(q - 1):
        seenp.add(cur)
        if cur[2] == 0: Bs.add(i % M)
        cur = mul(cur, th)
    if len(seenp) != q - 1: raise GenErr("theta not primitive")
    B = sorted(Bs)
    if len(B) != p + 1: raise GenErr("|B| != p+1")
    dd = set((x - y) % M for x in B for y in B if x != y)
    if len(dd) != M - 1 or len([1 for x in B for y in B if x != y]) != M - 1: raise GenErr("not perfect difference set")
    return M, (h, th), B

def run_family(name, primes, gen, svals, allc_p, budget, writer):
    t_start = time.process_time()
    res = {}; last = None; timeout = False; eligible = 0; skips = 0; total = 0
    witnesses = []; generr = None
    for p in primes:
        try: M, z, B = gen(p)
        except GenErr as e: generr = "p=%d: %s" % (p, e); break
        for s in svals:
            if math.gcd(s % M, M) != 1: continue
            cs = list(range(M)) if p == allc_p else [(j*M)//32 for j in range(32)]
            for c in cs:
                if time.process_time() - t_start > budget: timeout = True; break
                A0 = [(s*b + c) % M for b in B]
                mn = min(A0)
                for conv, (N, A) in (('N=M', (M, A0)), ('N=span', (max(A0)-mn+1, [a-mn for a in A0]))):
                    total += 1
                    st = res.setdefault((p, conv), dict(rho=[], miss=[], rr=[]))
                    try: r = test_set(N, A, st, (p, z, s, c, conv), witnesses)
                    except GenErr as e: generr = str(e); break
                    if r == 'skip': skips += 1
                    else: eligible += 1
                if generr: break
                last = (p, s, c)
            if timeout or generr: break
        if timeout or generr: break
    return dict(res=res, last=last, timeout=timeout, eligible=eligible, skips=skips, total=total,
                witnesses=witnesses, generr=generr, cpu=time.process_time() - t_start)

def dec(fr, places=4):
    n, d = fr.numerator, fr.denominator
    v = (n * 10**places * 2 + d) // (2*d)
    return "%d.%0*d" % (v // 10**places, places, v % 10**places)

def summarize(R):
    L = []
    allmiss = []
    for (p, conv), st in sorted(R['res'].items()):
        if not st['rho']: continue
        rhos = sorted(st['rho'], key=lambda t: Fraction(*t[0]))
        n = len(rhos)
        mn, mx = rhos[0], rhos[-1]
        fr = lambda t: Fraction(*t[0])
        med = fr(rhos[n//2]) if n % 2 else (fr(rhos[n//2-1]) + fr(rhos[n//2])) / 2
        minrr = min(Fraction(*r[0]) / x for r, x in zip(st['rho'], st['rr']))
        mm = min(st['miss'])
        allmiss.append(mm[0])
        L.append("| %d | %s | %d | %d/%d = %s | %s | %d/%d = %s | %s | min set: s,c=%s,%s N=%d k=%d T=%d S=%d | %d | %s |" % (
            p, conv, n, mn[0][0], mn[0][1], dec(fr(mn)), dec(med), mx[0][0], mx[0][1], dec(fr(mx)), '', mn[1][2], mn[1][3], mn[2], mn[3], mn[4], mn[5], mm[0], dec(minrr)))
    return L, (min(allmiss) if allmiss else None)

def report_family(title, R, f):
    f.append("## " + title)
    f.append("- generator error: %s" % R['generr'])
    f.append("- timeout: %s; last completed (p,s,c): %s" % (R['timeout'], R['last']))
    f.append("- sets generated (both conventions counted): %d; eligible: %d; skipped (N<4096 or k^2<N): %d; CPU %.1f s" % (R['total'], R['eligible'], R['skips'], R['cpu']))
    f.append("- counterexamples: %d" % len(R['witnesses']))
    for w in R['witnesses'][:3]:
        f.append("  - WITNESS ctx(p,(h|z),s,c,conv)=%s N=%d k=%d T=%d S=%d S_recomputed=%d 100S=%d 3kT^3=%d\n    A=%s\n    missing d<T=%s" % (w['ctx'], w['N'], w['k'], w['T'], w['S'], w['S2'], w['lhs'], w['rhs'], w['A'], w['missing']))
    L, mm = summarize(R)
    f.append("- min over family of unweighted missing count (d<T): %s" % mm)
    f.append("")
    f.append("| p | convention | eligible | min rho (exact = decimal) | median rho | max rho | | min-rho set | min missing count | min rho/rho_rand |")
    f.append("|---|---|---|---|---|---|---|---|---|---|")
    f.extend(L)
    f.append("")

main = run_family('main', [67, 71, 79, 97, 127, 191, 257], bose_set, [1, -1, 2, 3, 5, 7], 67, 3300, None)
sup = run_family('supp', [67, 71, 79, 97, 127], singer_set, [1, -1, 2, 3], None, 900, None)

if main['generr'] or sup['generr']: status = "NOT TESTABLE AS STATED (generator error; see report)" if main['generr'] else None
if main['witnesses'] or sup['witnesses']: status = "FALSIFIED"
elif main['generr']: status = "PARTIAL (generator error)"
elif main['timeout']: status = "PARTIAL"
else: status = "SURVIVED"
f = ["STATUS: " + status, "",
     "# SID-L finite test (Erdős #30), Bose + Singer families", "",
     "Sanity check F(1..25) vs A143824: %s." % ("PASS" if SANITY else "FAIL"), "",
     "SURVIVED would cover only these algebraic families (numerical/exact finite evidence, not a proof)."
     " Supplementary-family outcome is reported separately: %s." % ("counterexample" if sup['witnesses'] else ("generator error" if sup['generr'] else ("timeout" if sup['timeout'] else "all eligible passed"))), ""]
report_family("Main family (Bose)", main, f)
report_family("Supplementary family (Singer)", sup, f)
f.append("rho = 100S/(3kT^3) (counterexample iff rho<1); rho_rand = 200T^2/(15Nk). Margins are diagnostics for the algebraic families only.")
f.append("")
f.append("COST: wall %.1f s, CPU %.1f s, no web, no solver." % (time.time()-W0, time.process_time()-T0))
import os
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "SIDL_30_test.md"), "w").write("\n".join(f) + "\n")
print("\n".join(f))
