"""Finite fields F_{p^n} by log tables; theta = class of x, modulus = first (lex by low->high coefficient tuple) monic poly for which x is primitive."""
import itertools

def build(p, n):
    Q = p**n
    for coeffs in itertools.product(range(p), repeat=n):   # x^n = -(c_{n-1}x^{n-1}+...+c_0)
        if coeffs[0] == 0: continue
        cur = [0]*n; cur[0] = 1
        exp = []; seen = set(); ok = True
        for i in range(Q - 1):
            t = tuple(cur)
            if t in seen: ok = False; break
            seen.add(t); exp.append(t)
            top = cur[-1]
            cur = [0] + cur[:-1]
            if top:
                cur = [(cur[j] - top*coeffs[j]) % p for j in range(n)]
        if ok and tuple(cur) == exp[0]:
            enc = lambda t: sum(d * p**j for j, d in enumerate(t))
            E = [enc(t) for t in exp]
            L = {e: i for i, e in enumerate(E)}
            return p, n, coeffs, E, L
    raise RuntimeError

def add(p, n, a, b):
    r = 0; m = 1
    for _ in range(n):
        r += ((a % p + b % p) % p) * m; a //= p; b //= p; m *= p
    return r

def families(p, e):
    """q = p^e. Returns {'Bose-Chowla': (M, [(b, sorted set mod M)]), 'Singer': (M, [...])}"""
    q = p**e
    out = {}
    P, n, co, E, L = build(p, 4*e); Q = q**4; M = Q - 1
    Fq = [0] + [E[i*(M//(q-1))] for i in range(q-1)]
    bc = []
    for b in range(M):
        if (b*q*q) % M == b: continue                       # theta^b in F_{q^2}: degree <4 over F_q
        z = E[b]; S = set()
        for v in Fq:
            w = add(P, n, z, v); assert w != 0
            S.add(L[w] % M)
        assert len(S) == q
        bc.append((b, sorted(S)))
    out['Bose-Chowla'] = (M, bc)
    P, n, co, E, L = build(p, 5*e); Q = q**5; M2 = (Q - 1)//(q - 1)
    Fq = [0] + [E[i*((Q-1)//(q-1))] for i in range(q-1)]
    def mul(a, b):
        return 0 if a == 0 or b == 0 else E[(L[a]+L[b]) % (Q-1)]
    sg = []
    for b in range(1, M2):                                   # b=0 gives theta^b in F_q (degree 1)
        z = E[b]; S = set()
        for u in Fq:
            for v in Fq:
                if u == 0 and v == 0: continue
                w = add(P, n, mul(u, z), v); assert w != 0
                S.add(L[w] % M2)
        assert len(S) == q + 1, (q, b, len(S))
        sg.append((b, sorted(S)))
    out['Singer'] = (M2, sg)
    return out
