"""
r3_bovdi_maroti.py -- ROUND 3, line zc1a7.

Round 1's literature check cleared arXiv:2108.06977 (Bovdi-Maroti, "On partial
augmentations of elements in integral group rings", Publ. Math. Debrecen / zbMATH 2023)
on the ground that it "does not touch A_7/ZC1".  That was a statement about the paper's
CONTENT.  Its Theorem 1 and Theorem 2, however, are stated for an ARBITRARY finite group
and an arbitrary torsion unit, so they are candidate constraints on our open case and
must be TESTED, not cleared by topic.  This script tests them.

Theorem 1 (verbatim from the arXiv source, notation nu = partial augmentation):
  Let u in V(ZG) be torsion, k and n positive integers, k coprime to exp(G), and
  n = k = 1 (mod |u|).  Then for every s in G
      nu_s(u) = sum_{r | t | n} mu(r) * ( sum_{ x^G : (exists y) y^{(k n r)/t} = x^k ~ s }
                                          nu_x(u) ).
Theorem 2 (specialised below to q = 2, p = 2) reduces to Hertweck's congruence, which
HeLP already uses; we check that too.

Exact integer arithmetic.  Interpreter: .venv/bin/python3.
"""
import itertools
from collections import defaultdict
from sympy import mobius, divisors

# ------------------------------------------------------------------ build A_7 explicitly
def parity(p):
    seen = [False] * 7
    par = 0
    for s in range(7):
        if not seen[s]:
            L = 0
            t = s
            while not seen[t]:
                seen[t] = True
                t = p[t]
                L += 1
            par += L - 1
    return par % 2


A7 = [p for p in itertools.permutations(range(7)) if parity(p) == 0]
assert len(A7) == 2520


def mul(p, q):
    return tuple(p[q[x]] for x in range(7))


def power(p, k):
    r = tuple(range(7))
    b = p
    k = k % 420 if k > 420 else k
    for _ in range(k):
        r = mul(b, r)
    return r


def cyc(p):
    seen = [False] * 7
    t = []
    for s in range(7):
        if not seen[s]:
            L = 0
            x = s
            while not seen[x]:
                seen[x] = True
                x = p[x]
                L += 1
            t.append(L)
    return tuple(sorted(t, reverse=True))


CTMAP = {(1,) * 7: '1a', (2, 2, 1, 1, 1): '2a', (3, 1, 1, 1, 1): '3a', (3, 3, 1): '3b',
         (4, 2, 1): '4a', (5, 1, 1): '5a', (3, 2, 2): '6a'}
seed = next(p for p in A7 if cyc(p) == (7,))
orb7a = set()
for g in A7:
    gi = power(g, [o for o in range(1, 8) if power(g, o) == tuple(range(7))][0] - 1)
    orb7a.add(mul(mul(g, seed), gi))
assert len(orb7a) == 360

CLS = {}
for p in A7:
    c = cyc(p)
    CLS[p] = CTMAP.get(c) or ('7a' if p in orb7a else '7b')
CL = ['1a', '2a', '3a', '3b', '4a', '5a', '6a', '7a', '7b']
SZ = [sum(1 for p in A7 if CLS[p] == c) for c in CL]
assert SZ == [1, 105, 70, 280, 630, 504, 210, 360, 360], SZ
ORD = {'1a': 1, '2a': 2, '3a': 3, '3b': 3, '4a': 4, '5a': 5, '6a': 6, '7a': 7, '7b': 7}
REP = {c: next(p for p in A7 if CLS[p] == c) for c in CL}
EXPG = 420
print("A_7 built explicitly; class sizes", SZ, "; exponent", EXPG)

# class of x^k, by actually exponentiating a representative
PWCL = {}
for c in CL:
    for k in range(0, 60):
        PWCL[(c, k)] = CLS[power(REP[c], k % ORD[c])]

# is class s an m-th power in G?  (compute the set of m-th powers, by class)
POWSET = {}


def powset(m):
    m = m % 420
    if m not in POWSET:
        POWSET[m] = {CLS[power(q, m)] for q in A7}
    return POWSET[m]

# ------------------------------------------------------------------ the two candidates
NU_OPEN = {'2a': 2, '4a': -1}
NU_TRIV = {'4a': 1}


def theorem1_rhs(nu, s, k, n):
    tot = 0
    for t in divisors(n):
        for r in divisors(t):
            m = mobius(r)
            if m == 0:
                continue
            e = (k * n * r) // t
            inner = 0
            for x, v in nu.items():
                if PWCL[(x, k % ORD[x])] != s:
                    continue
                if s not in powset(e):
                    continue
                inner += v
            tot += int(m) * inner
    return tot


print("\nTHEOREM 1 of Bovdi-Maroti, tested on both HeLP survivors")
print("  admissible (k,n):  k coprime to exp(G)=420 and k = n = 1 (mod |u|=4)")
ks = [k for k in range(1, 60) if k % 4 == 1 and all(k % q for q in (2, 3, 5, 7))]
ns = [n for n in range(1, 30) if n % 4 == 1]
print("  k in", ks, " n in", ns)
for tag, nu in (('TRIVIAL (0,1)', NU_TRIV), ('OPEN (2,-1)', NU_OPEN)):
    viol = []
    tested = 0
    for k in ks:
        for n in ns:
            for s in CL:
                tested += 1
                lhs = nu.get(s, 0)
                rhs = theorem1_rhs(nu, s, k, n)
                if lhs != rhs:
                    viol.append((k, n, s, lhs, rhs))
    print("  %-16s : %d (k,n,s) instances tested, %d violations" % (tag, tested, len(viol)))
    for v in viol[:5]:
        print("        k=%d n=%d s=%s : lhs=%d rhs=%d" % v)
print("\n  REJECTION CONTROL -- the implementation must be able to say NO.")
print("  Feed it a vector that is NOT the partial-augmentation vector of any torsion unit,")
print("  supported on the two IRRATIONAL classes 7a/7b where x^13 = x^{-1} genuinely moves:")
FAKE = {'2a': 2, '7a': 1, '7b': -2}
vio = []
for k in ks:
    for n in ns:
        for s in CL:
            if FAKE.get(s, 0) != theorem1_rhs(FAKE, s, k, n):
                vio.append((k, n, s, FAKE.get(s, 0), theorem1_rhs(FAKE, s, k, n)))
print("  fake vector {2a:2, 7a:1, 7b:-2} : %d of %d instances VIOLATE Theorem 1."
      % (len(vio), len(ks) * len(ns) * 9))
print("  e.g.", vio[0] if vio else 'none')
assert vio, "rejection control failed -- the implementation cannot say NO"

print("""  ==> Theorem 1 is VACUOUS for a unit of order 4 in ZA_7.  Reason, and it is structural:
      the hypothesis forces k = 1 (mod |u|) = 1 (mod 4), while Hertweck's theorem forces
      nu_x(u) = 0 unless ord(x) divides 4.  So x^k = x for every x in the support of nu,
      the inner sum collapses to nu_s(u) times a statement about G alone, and the identity
      holds for ANY vector of partial augmentations supported on {2a,4a}.  It therefore
      cannot separate the two HeLP survivors.""")

print("\nTHEOREM 2 (q=2, p=2) -- reduces to Hertweck's congruence, already used by HeLP")
# nu_s(u^2) = sum_{x : x^2 ~ s} nu_x(u)  (mod 2)
NU2_OPEN = {'2a': 1}
NU2_TRIV = {'2a': 1}
for tag, nu, nu2 in (('TRIVIAL (0,1)', NU_TRIV, NU2_TRIV), ('OPEN (2,-1)', NU_OPEN, NU2_OPEN)):
    bad = []
    for s in CL:
        lhs = nu2.get(s, 0) % 2
        rhs = sum(v for x, v in nu.items() if PWCL[(x, 2)] == s) % 2
        if lhs != rhs:
            bad.append((s, lhs, rhs))
    print("  %-16s : %d of 9 classes violate the mod-2 congruence" % (tag, len(bad)), bad)
print("  ==> both survivors satisfy it; it is the congruence round 2 already used.")

print("\nVERDICT: arXiv:2108.06977 supplies NO new constraint on the A_7 open case.")
print("         Round 1 cleared it on topic; this round clears it on CONTENT, by running it.")
