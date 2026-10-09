# Standalone replay of the CR-7 claimed counterexample to SID-L (Erdos #30) + Singer dilation-orbit diagnostic.
# Run: python3 -I sidl_30_replay.py   (stdlib only, exact integers)
import math, time
from fractions import Fraction
from itertools import combinations_with_replacement

A68 = [int(x) for x in """0, 14, 134, 207, 220, 417, 493, 527, 538, 580, 587, 662, 823, 916, 925, 962, 1137, 1191, 1215, 1253, 1341, 1353, 1356, 1430, 1499, 1611, 1617, 1800, 1851, 2025, 2060, 2077, 2157, 2205, 2207, 2236, 2262, 2263, 2358, 2510, 2531, 2602, 2646, 2727, 2759, 2825, 2844, 2992, 3075, 3103, 3136, 3243, 3259, 3263, 3302, 3327, 3392, 3584, 3606, 3614, 3624, 3715, 3778, 3814, 3819, 3886, 3933, 3956""".split(',')]

def Tof(N):
    lo, hi = 1, N
    while lo < hi:
        m = (lo + hi) // 2
        if 10000 * m**4 >= 38809 * N**3: hi = m
        else: lo = m + 1
    return lo

def dec(fr, places=6):
    n, d = fr.numerator, fr.denominator
    v = (n * 10**places * 2 + d) // (2*d)
    return "%d.%0*d" % (v // 10**places, places, v % 10**places)

def mask_diffs(A):
    """bitmask of positive differences (bit d set iff d is a positive difference)."""
    N = max(A) + 1
    mk = 0
    for a in A: mk |= 1 << a
    D = 0
    for a in A: D |= mk >> a
    return D & ~1

def S_of(D, T):
    miss = (~D) & ((1 << T) - 1) & ~1
    S = 0; ms = []
    while miss:
        low = miss & -miss; d = low.bit_length() - 1; miss ^= low
        ms.append(d); S += 4*T**3 - 6*d*T*T + 2*d**3
    return S, ms

def rho_of(S, k, T): return Fraction(100*S, 3*k*T**3)

# ---------------- Part 1 ----------------
def part1(out):
    A = A68; k = len(A)
    out.append("## Part 1 - exact replay of the displayed 68-point set\n")
    out.append("| item | value |\n|---|---|")
    row = lambda a, b: out.append("| %s | %s |" % (a, b))
    row("k = |A|", k); row("distinct", len(set(A)) == k); row("sorted", A == sorted(A))
    row("min, max", "%d, %d" % (min(A), max(A))); row("all in [0,4095]", all(0 <= a <= 4095 for a in A))
    row("k^2 = %d >= 4096" % (k*k), k*k >= 4096)
    diffs = [A[j]-A[i] for j in range(k) for i in range(j)]
    row("#positive differences / #distinct", "%d / %d" % (len(diffs), len(set(diffs))))
    sums = [A[i]+A[j] for i in range(k) for j in range(i, k)]
    row("#sums a_i+a_j (i<=j) / #distinct", "%d / %d" % (len(sums), len(set(sums))))
    row("strong Sidon (both conventions)", len(set(diffs)) == len(diffs) == 2278 and len(set(sums)) == len(sums) == 2346)
    N = 4096; T = Tof(N)
    row("T (N=4096)", T)
    row("10000*718^4 < 38809*4096^3 <= 10000*719^4", "%d < %d <= %d : %s" % (10000*718**4, 38809*N**3, 10000*719**4, 10000*718**4 < 38809*N**3 <= 10000*719**4))
    D = mask_diffs(A); S, ms = S_of(D, T)
    # independent plain-set recomputation
    ds = set(diffs); ms2 = [d for d in range(1, T) if d not in ds]
    S2 = sum(4*T**3 - 6*d*T*T + 2*d**3 for d in ms2)
    row("missing differences in {1..T-1}", "%s (count %d); bitmask and set methods agree: %s" % (ms2, len(ms2), ms == ms2 and S == S2))
    row("expected missing {601,615,624,638,671,685}", ms2 == [601, 615, 624, 638, 671, 685])
    row("S", S); row("100*S", 100*S); row("3*k*T^3", 3*k*T**3)
    row("100*S < 3*k*T^3 (counterexample)", 100*S < 3*k*T**3)
    r = rho_of(S, k, T)
    row("rho = M(A)/(k/100) = 100S/(3kT^3)", "%s = %s" % (r, dec(r)))
    Np = max(A) - min(A) + 1
    row("span N' = max-min+1", Np); row("N' >= 4096 ?", Np >= 4096)
    row("hyp at N'=%d: k^2>=N'" % Np, k*k >= Np)
    out.append("")
    out.append("Span convention: N' = %d < 4096, so the hypothesis N >= 4096 is %s under the span convention; the counterexample stands under the interval convention A subset {0..N-1}, N = 4096 (the lemma's own convention)." % (Np, "MET" if Np >= 4096 else "NOT met"))
    out.append("")
    return 100*S < 3*k*T**3 and ms2 == [601, 615, 624, 638, 671, 685] and S == 180279588

# ---------------- Singer generator ----------------
def factor(n):
    f = []; d = 2
    while d*d <= n:
        if n % d == 0:
            f.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: f.append(n)
    return f

def singer_set(p):
    m = p*p + p + 1; q = p**3
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
        for d in (4, 3):
            co = r[d] % p; r[d] = 0
            if co: r[d-1] -= a*co; r[d-2] -= b*co; r[d-3] -= c*co
        return tuple(t % p for t in r[:3])
    one = (1, 0, 0)
    def pw(x, e):
        r = one
        while e:
            if e & 1: r = mul(r, x)
            x = mul(x, x); e >>= 1
        return r
    fs = factor(q - 1); th = None
    for u in range(p):
        for v in range(p):
            for w in range(p):
                g = (u, v, w)
                if g == (0, 0, 0): continue
                if all(pw(g, (q-1)//l) != one for l in fs): th = g; break
            if th: break
        if th: break
    cur = one; Bs = set()
    for i in range(q - 1):
        if cur[2] == 0: Bs.add(i % m)
        cur = mul(cur, th)
    B = sorted(Bs)
    assert len(B) == p + 1
    dd = set((x - y) % m for x in B for y in B if x != y)
    assert len(dd) == m - 1 == (p+1)*p, "not a perfect difference set"
    return m, B

def sweep(p, do4096, t0, budget):
    m, B = singer_set(p); k = len(B)
    res = {}  # conv -> dict(elig, cex, best(rho,u,cut,S,N,T), nu)
    units = [u for u in range(1, m//2 + 1) if math.gcd(u, m) == 1]
    done_all = True; ncex_list = []
    full4096 = None
    for u in units:
        if time.process_time() - t0 > budget: done_all = False; break
        s = sorted((u*b) % m for b in B)
        for i in range(k):
            A = [x - s[i] for x in s[i:]] + [x + m - s[i] for x in s[:i]]
            convs = [('N=m', m)]
            if do4096 and A[-1] <= 4095: convs.append(('N=4096', 4096))
            for conv, N in convs:
                st = res.setdefault(conv, dict(elig=0, cex=0, best=None, units=set(), hit=[]))
                if k*k < N: continue
                T = Tof(N); D = mask_diffs(A)
                if bin(D).count('1') != k*(k-1)//2: raise SystemExit("difference collision p=%d u=%d i=%d" % (p, u, i))
                S, ms = S_of(D, T)
                st['elig'] += 1; st['units'].add(u)
                r = rho_of(S, k, T)
                if 100*S < 3*k*T**3: st['cex'] += 1; st['hit'].append((u, i, N, S))
                if st['best'] is None or r < st['best'][0]: st['best'] = (r, u, i, S, N, T, len(ms), list(A))
                if conv == 'N=4096' and A == A68: st['match'] = (u, i)
    return dict(p=p, m=m, k=k, nunits=len(units), done_all=done_all, res=res, last_u=u)

def main():
    t0 = time.process_time()
    out = ["# SID-L counterexample CR-7: replay report (verifier, AUT-60)", "STATUS_PLACEHOLDER", ""]
    ok = part1(out)
    c1 = time.process_time() - t0
    out.append("Part 1 CPU: %.2f s\n" % c1)
    out.append("## Part 2 - Singer dilation-orbit diagnostic\n")
    out.append("Instances: for each unit u, 1<=u<=m/2, gcd(u,m)=1, dilate the Singer set B (k=p+1) by u mod m, sort, and take all k cyclic cuts translated to min 0. N=m always tested; N=4096 tested iff max A <= 4095 (p=67 only). Counterexample iff 100S < 3kT^3; rho = 100S/(3kT^3).\n")
    out.append("| p | m | k | convention | units covered/total | eligible instances | counterexamples | min rho (exact = decimal) | argmin (u, cut) | S at min | T | #missing at min | CPU s |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    cap = 15*60 - 60
    notes = []; p67 = None
    for p, d4096 in ((67, True), (71, False), (79, False)):
        t1 = time.process_time()
        if t1 - t0 > cap: notes.append("cap reached before p=%d" % p); break
        R = sweep(p, d4096, t1, cap - (t1 - t0))
        cpu = time.process_time() - t1
        if p == 67: p67 = R
        for conv, st in sorted(R['res'].items()):
            b = st['best']
            out.append("| %d | %d | %d | %s | %d/%d%s | %d | %d | %s = %s | (%d, %d) | %d | %d | %d | %.1f |" % (
                p, R['m'], R['k'], conv, len(st['units']), R['nunits'], '' if R['done_all'] else ' (CAP HIT)',
                st['elig'], st['cex'], b[0], dec(b[0]), b[1], b[2], b[3], b[5], b[6], cpu))
        if not R['done_all']: notes.append("cap reached during p=%d" % p); break
    out.append("")
    if p67:
        st = p67['res'].get('N=4096')
        if st:
            b = st['best']
            out.append("p=67, N=4096: counterexamples (u, cut, S): %s" % (st['hit'][:40],))
            out.append("Minimum at N=4096: S=%d (attacker S=180279588): reproduced = %s; minimizing set equals displayed 68-set: %s; displayed set found as orbit instance (u, cut): %s" % (b[3], b[3] == 180279588, b[7] == A68, st.get('match')))
            # also: other instances attaining the same S?
        stm = p67['res']['N=m']
        out.append("p=67, N=m=4557: counterexamples (u, cut, S): %s" % (stm['hit'][:40],))
    out.extend(notes)
    tot = time.process_time() - t0
    out.append("\nTotal CPU time: %.1f s" % tot)
    out[1] = "STATUS: " + ("CONFIRMED" if ok else "NOT CONFIRMED")
    print("\n".join(out))

main()
