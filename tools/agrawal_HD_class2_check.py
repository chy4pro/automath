#!/usr/bin/env python3
"""Independent execution check that Hegde-Devaraj 2021 CLASS 2 implies the LP kernel.

Class 2 (Hegde, slide 8; n = prod p_i^{a_i}, m_i = n / p_i^{a_i}):
  (2) a_i == 1 (mod 4)
  (4) exists t_i == 2 (mod 4) with (p_i^{t_i} - 1) | (m_i - 1)
Claim: (2)+(4) => (p_i - 1) | (n-1) AND (p_i + 1) | (n+1)   [the Carmichael ^ Lucas-Carmichael kernel]
Negative control: replacing (2) by a_i EVEN must break the (p_i+1)|(n+1) half.
"""
import random


def sieve(n):
    s = [True] * (n + 1); s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(n + 1) if s[i]]


PRIMES = [p for p in sieve(200) if p > 2]


def kernel(ps, aa):
    n = 1
    for p, a in zip(ps, aa):
        n *= p ** a
    return (all((n - 1) % (p - 1) == 0 for p in ps),
            all((n + 1) % (p + 1) == 0 for p in ps))


def trial(exps, ks, trials, seed):
    random.seed(seed)
    tested = fails_c = fails_lc = nonsq = 0
    for _ in range(trials):
        ps = random.sample(PRIMES, random.choice(ks))
        aa = [random.choice(exps) for _ in ps]
        n = 1
        for p, a in zip(ps, aa):
            n *= p ** a
        if not all(any((n // p ** a - 1) % (p ** t - 1) == 0 for t in (2, 6, 10, 14))
                   for p, a in zip(ps, aa)):
            continue                                  # condition (4) not met
        tested += 1
        nonsq += any(a > 1 for a in aa)
        c, lc = kernel(ps, aa)
        fails_c += not c
        fails_lc += not lc
    return tested, nonsq, fails_c, fails_lc


t, nsq, fc, flc = trial([1, 1, 1, 5], [1, 3, 5], 400000, 7)
print("HD (2)+(4)  : %d configs (%d non-squarefree) -> Carmichael-half failures %d, "
      "Lucas-Carmichael-half failures %d" % (t, nsq, fc, flc))
t2, _, fc2, flc2 = trial([2, 4, 6], [1, 3], 400000, 7)
print("CONTROL a_i even (violates HD cond 2): %d configs -> Carmichael-half failures %d, "
      "Lucas-Carmichael-half failures %d" % (t2, fc2, flc2))
print("\nHD cond (4) at t=2 vs the LP pair ((p^2-1)/2 | m-1):")
for p, m in [(7, 25), (11, 61), (13, 85), (19, 181)]:
    print("  p=%-3d m=%-4d  LP: %-5s  HD: %s"
          % (p, m, (m - 1) % ((p * p - 1) // 2) == 0, (m - 1) % (p * p - 1) == 0))
