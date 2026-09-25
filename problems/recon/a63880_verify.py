
from math import isqrt

X = 10**12
M = isqrt(X)

# Smallest-prime-factor table, sufficient to factor every x and y below.
spf = list(range(M + 1))
for i in range(2, isqrt(M) + 1):
    if spf[i] == i:
        for j in range(i*i, M + 1, i):
            if spf[j] == j:
                spf[j] = i

def factor(t):
    ans = {}
    while t > 1:
        p = spf[t]
        e = 0
        while t % p == 0:
            t //= p
            e += 1
        ans[p] = e
    return ans

squarefree_y = []
for y in range(1, 10000 + 1):       # 10000 = floor(X^(1/3))
    fy = factor(y)
    if all(e == 1 for e in fy.values()):
        squarefree_y.append((y, set(fy)))

solutions = []
tested = 0
for y, primes_y in squarefree_y:
    for x in range(1, isqrt(X // y**3) + 1):
        if x == y == 1:
            continue
        fx = factor(x)
        exponents = {
            p: 2*fx.get(p, 0) + (3 if p in primes_y else 0)
            for p in set(fx) | primes_y
        }
        s = u = 1
        for p, e in exponents.items():
            s *= (p**(e+1) - 1) // (p - 1)
            u *= p**e + 1
        if s == 2*u:
            solutions.append((x*x*y**3, tuple(sorted(exponents.items()))))
        tested += 1

print(tested)
print(sorted(solutions))
