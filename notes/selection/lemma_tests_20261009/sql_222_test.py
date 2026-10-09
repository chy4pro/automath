import math, time, sys, os
from math import isqrt
T0W = time.time(); C0 = time.process_time()
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SQL_222_test.md")
def cpu(): return time.process_time() - C0
def Jof(u):
    J = isqrt(isqrt(u))
    while J**4 < u: J += 1
    while J > 1 and (J-1)**4 >= u: J -= 1
    return J
def Tof(u): return isqrt(196*u//25)   # max e with 25e^2<=196u
def ej_list(u, r, J):
    L = []
    for j in range(J+1):
        x = r + 2*u*j - j*j; s = isqrt(x); q = s+1 if s*s < x else s
        L.append(q*q - x)
    return L
class St:
    def __init__(s, name):
        s.name=name; s.n=0; s.bpass=0; s.j0=0; s.hist={}; s.maxj=-1; s.maxjat=None
        s.nontriv=0; s.minslack=None; s.minslack_at=None; s.wit=[]; s.nwit=0; s.cpu=0.0; s.note=""
def witness(u, r, st):
    J = Jof(u); L = ej_list(u, r, J); b = 2*u+1-r
    e = min([b]+L)   # second independent loop, no early exit
    if 25*e*e > 196*u:
        st.nwit += 1
        if len(st.wit) < 20:
            st.wit.append(dict(u=u, r=r, n=u*u+r, J=J, ej=L, b=b, e=e, lhs=25*e*e, rhs=196*u))
    else:
        raise RuntimeError("witness not reproduced %d %d" % (u, r))
def run_range(u, r0, r1, J, T, st):
    """test r in [r0,r1)"""
    twou = 2*u; hist = st.hist
    for r in range(r0, r1):
        st.n += 1
        e = twou + 1 - r
        if e <= T:
            st.bpass += 1; continue
        x = r; passed = False
        for j in range(J+1):
            x = r + twou*j - j*j
            s = isqrt(x)
            if s*s < x: s += 1
            ej = s*s - x
            if ej < e: e = ej
            if e <= T:
                passed = True; break
        if not passed:
            witness(u, r, st); continue
        if j == 0: st.j0 += 1
        else:
            hist[j] = hist.get(j, 0) + 1
        if j > st.maxj: st.maxj = j; st.maxjat = (u, r)
        if j > 0:   # nontrivial: boundary and e_0 both exceed T
            st.nontriv += 1
            es = min([twou+1-r] + ej_list(u, r, J))
            sl = 196*u - 25*es*es
            if st.minslack is None or sl < st.minslack:
                st.minslack = sl; st.minslack_at = (u, r)
def run_chunked(u, r0, r1, st, limit):
    J = Jof(u); T = Tof(u)
    a = r0
    while a < r1:
        b = min(a+1000, r1)
        run_range(u, a, b, J, T, st)
        a = b
        if cpu() > limit: return False
    return True
def run_pairs(pairs, st, limit):
    for k, (u, r) in enumerate(pairs):
        run_range(u, r, r+1, Jof(u), Tof(u), st)
        if k % 1000 == 0 and cpu() > limit: return False
    return True

# ---- sanity
def sos(n):
    a = 0
    while 2*a*a <= n:
        b2 = n - a*a; b = isqrt(b2)
        if b*b == b2: return True
        a += 1
    return False
def g(n):
    d = 0
    while not sos(n+d): d += 1
    return d
A001481 = [0,1,2,4,5,8,9,10,13,16,17,18,20,25,26,29]
san_ok1 = all(g(n) == 0 for n in A001481)
san_cnt = 0; san_ok2 = True
for u in range(1024, 1031):
    J = Jof(u)
    for r in range(0, 2*u+1):
        es = min([2*u+1-r] + ej_list(u, r, J)); san_cnt += 1
        if es < g(u*u+r): san_ok2 = False
sanity = "g(n)=0 on the 16 listed A001481 values: %s; e_*(u,r)>=g(u^2+r) for u=1024..1030, all r (%d instances): %s." % (san_ok1, san_cnt, san_ok2)

LIM123 = 3300.0
stats = []
# ---- batch 1
b1 = St("Batch 1"); c = cpu(); done = True; last = None
for u in range(1024, 4097):
    if not run_chunked(u, 0, 2*u+1, b1, LIM123): done = False; last = u; break
b1.cpu = cpu()-c
b1.note = "complete" if done and b1.n == 15736833 else "STOPPED at u=%s, n=%d" % (last, b1.n)
stats.append(b1)
# ---- batch 2
b2 = St("Batch 2"); c = cpu(); fixture = None
pairs = []
if done:
    for m in range(2, 100001, 2):
        u = m*(m+2)//2; r = m*m+1
        if u >= 1024 and r <= 2*u: pairs.append((u, r))
    done2 = run_pairs(pairs, b2, LIM123)
    J = Jof(4098384); L = ej_list(4098384, 2862**2+1, J)
    T = Tof(4098384); fj = None; e = 2*4098384+1-(2862**2+1)
    for j, v in enumerate(L):
        e = min(e, v)
        if e <= T: fj = j; break
    fixture = dict(u=4098384, r=2862**2+1, n=4098384**2+2862**2+1, J=J, ej=L, b=2*4098384+1-(2862**2+1), T=T, fj=fj)
    b2.note = "complete (%d instances)" % b2.n if done2 else "STOPPED at n=%d" % b2.n
    done = done2
else: b2.note = "not run"
b2.cpu = cpu()-c; stats.append(b2)
# ---- batch 3
b3 = St("Batch 3"); c = cpu()
if done:
    pairs = []
    for b in range(10, 41):
        for t in range(32):
            u = (1 << b) + t; M = isqrt(2*u)
            S = {0, u, 2*u}
            for m in range(max(0, M-16), M+1):
                if m*m+1 <= 2*u: S.add(m*m+1)
            for r in sorted(S): pairs.append((u, r))
    done = run_pairs(pairs, b3, LIM123)
    b3.note = "complete (%d instances)" % b3.n if done else "STOPPED at n=%d" % b3.n
else: b3.note = "not run"
b3.cpu = cpu()-c; stats.append(b3)
cpu123 = cpu()
# ---- batch 4
LIM4 = cpu123 + 1200.0
def window(u, st, limit):
    T = Tof(u); J = Jof(u); m = 0
    while m*m <= 2*u:
        lo = m*m+1; hi = min((m+1)**2 - T - 1, 2*u - T)
        if lo <= hi:
            run_range(u, lo, hi+1, J, T, st)
            if cpu() > limit: return False
        m += 1
    return True
b4i = St("Batch 4(i) u=4097..20000"); b4ii = St("Batch 4(ii) u=2^b+t"); c = cpu(); stopi = None
if done:
    ok = True
    for u in range(4097, 20001):
        if not window(u, b4i, LIM4): ok = False; stopi = u; break
        if cpu() > LIM4: ok = False; stopi = u+1; break
    b4i.note = "complete" if ok else "STOPPED during/after u=%s (u<%s fully done)" % (stopi, stopi)
    b4i.cpu = cpu()-c; c = cpu()
    if ok:
        stop = False
        for b in range(15, 41):
            for t in range(1000):
                if not window((1<<b)+t, b4ii, LIM4): stop = True; b4ii.note = "STOPPED at b=%d t=%d" % (b, t); break
                b4ii.n  # no-op
            if stop: break
        if not stop: b4ii.note = "complete"
    else: b4ii.note = "not run (clock)"
    b4ii.cpu = cpu()-c
else:
    b4i.note = b4ii.note = "not run"
stats += [b4i, b4ii]

# ---- report
nw123 = sum(s.nwit for s in stats[:3]); nw4 = b4i.nwit + b4ii.nwit
if not (b1.note == "complete" and b2.note.startswith("complete") and b3.note.startswith("complete")):
    status = "PARTIAL" if nw123 == 0 and nw4 == 0 else "FALSIFIED"
elif nw123 or nw4: status = "FALSIFIED"
else: status = "SURVIVED"
o = []
o.append("STATUS: %s\n" % status)
o.append("Finite falsification test of SQ-L (Erdos #222). Numerical/exact finite evidence only; says nothing universal. Batch 4 reported separately.\n")
o.append("Sanity: " + sanity + "\n")
for s in stats:
    o.append("## %s — %s" % (s.name, s.note))
    o.append("- instances tested: %d; violations (witnesses): %d" % (s.n, s.nwit))
    o.append("- passed at boundary candidate: %d; passed at j=0: %d" % (s.bpass, s.j0))
    o.append("- first-passing j histogram (j>=1): %s" % dict(sorted(s.hist.items())))
    o.append("- max first-passing j: %d at %s" % (s.maxj, s.maxjat))
    o.append("- non-trivial instances (boundary and e_0 both > threshold): %d; min slack 196u-25e*^2 = %s at (u,r)=%s" % (s.nontriv, s.minslack, s.minslack_at))
    o.append("- CPU seconds: %.1f\n" % s.cpu)
    for w in s.wit:
        o.append("WITNESS: " + repr(w))
if fixture:
    o.append("## Regression fixture m=2862\n- " + repr(fixture) + "\n- first passing j = %s (threshold T=%d, i.e. 25e^2<=196u iff e<=T)\n" % (fixture['fj'], fixture['T']))
o.append("Note: 'non-trivial' slack uses the full e_* = min over boundary and all j=0..J (no early exit).")
o.append("\nCOST: wall %.1f s, CPU %.1f s (batches1-3 CPU %.1f s), no web, no solver." % (time.time()-T0W, cpu(), cpu123))
open(OUT, "w").write("\n".join(o)+"\n")
print("\n".join(o))
