#!/usr/bin/env python3
"""
R5 at large n (sampled). For random n in [10^e, 2*10^e):

  * block statistics at K = floor(C log n), C in (2,5,10), l = 0, from trial division of n+j by
    the primes <= K and a primality / prime-power test of the K-rough cofactor:
      omK(n+j) in {0, 1, >=2}; t0, t1, t_{>=2}; sigma0 = pi(K) - (2 t0 + t1);
      sigma = pi(K) - sum_{j in J} cap(n+j); Pcount = #{p <= K : ceil(n/p) prime > K}.
    (These need only omK in {0,1,>=2}, so they are exact.)
  * k3_l(n), l = 0, 1: exact when e <= EXACT_E (full sympy factorisation);
    otherwise a certified upper bound: the least k at which a certified LOWER bound for v(n,k)
    reaches 3 (primes in (k, B] found by trial division up to B, plus 1 if the B-rough
    cofactor is a prime power, plus 2 if it is composite and not a prime power).

Usage: python3 r5_bigsample.py --exps 12 15 18 24 30 50 100 --per 40 --seed 7 --out data/bigsample.jsonl
"""
import argparse, json, math, random, time
from sympy import primerange, isprime, perfect_power, factorint

EXACT_E = 18
B = 10000
PB = list(primerange(2, B + 1))

def rough_class(c):
    """0 if c == 1, 1 if c is a prime power, 2 otherwise (c > 1 composite, not a prime power)."""
    if c == 1:
        return 0
    if isprime(c):
        return 1
    pp = perfect_power(c)
    if pp and isprime(pp[0]):
        return 1
    return 2

def block_stats(n, C):
    K = math.floor(C * math.log(n))
    P = [p for p in PB if p <= K] if K <= B else list(primerange(2, K + 1))
    piK = len(P)
    t = [0, 0, 0]; capJ = 0
    for j in range(K + 1):
        m = n + j; inJ = False
        for p in P:
            if m % p == 0:
                if p > j:
                    inJ = True
                while m % p == 0:
                    m //= p
        o = rough_class(m)
        t[o] += 1
        if inJ:
            capJ += 2 - o if o < 2 else 0
    Pc = sum(1 for p in P if -(-n // p) > K and isprime(-(-n // p)))
    return dict(C=C, K=K, piK=piK, t0=t[0], t1=t[1], t2p=t[2], sigma0=piK - (2 * t[0] + t[1]),
                sigma=piK - capJ, Pc=Pc)

def v_lower(n, k):
    assert k < B, 'v_lower assumes k < B (cofactor primes then exceed k)'
    m = n + k; c = 0
    for p in PB:
        if p * p > m:
            break
        if m % p == 0:
            if p > k:
                c += 1
            while m % p == 0:
                m //= p
    if m == 1:
        return c, True
    if m <= B * B or isprime(m):          # m is 1 prime (loop exhausted: m < p^2, or m B-rough and < B^2)
        return c + (1 if m > k else 0), True
    o = rough_class(m)
    return c + o, (o == 1)                # exact unless o == 2 (then >= c+2)

def v_exact(n, k):
    return sum(1 for p in factorint(n + k) if p > k)

def k3(n, l, exact):
    k = l
    while True:
        if exact:
            if v_exact(n, k) >= 3:
                return k
        else:
            lb, _ = v_lower(n, k)
            if lb >= 3:
                return k
        k += 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--exps', type=int, nargs='+', required=True)
    ap.add_argument('--per', type=int, default=30)
    ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    with open(a.out, 'a') as f:
        for e in a.exps:
            t = time.time()
            for _ in range(a.per):
                n = rng.randrange(10 ** e, 2 * 10 ** e)
                exact = e <= EXACT_E
                rec = dict(e=e, n=str(n), logn=math.log(n), exact_k3=exact,
                           k3_l0=k3(n, 0, exact), k3_l1=k3(n, 1, exact),
                           blocks=[block_stats(n, C) for C in (2, 5, 10)])
                f.write(json.dumps(rec) + '\n'); f.flush()
            print(f'e={e}: {a.per} samples in {time.time()-t:.1f}s', flush=True)

if __name__ == '__main__':
    main()
