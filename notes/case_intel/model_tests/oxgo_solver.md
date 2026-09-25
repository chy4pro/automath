## Setting Up

We need $n^2 + 1 \equiv 0 \pmod{101}$, i.e., $n^2 \equiv -1 \equiv 100 \pmod{101}$.

**Finding solutions:** Since $10^2 = 100 \equiv -1 \pmod{101}$, we have $n \equiv 10$ works, and clearly $n \equiv -10 \equiv 91 \pmod{101}$ also works.

**These are the only solutions:** Work in the field $\mathbb{Z}/101\mathbb{Z}$ (valid since 101 is prime). The congruence $x^2 + 1 \equiv 0$ is a polynomial equation of degree 2 over a field, which has at most 2 roots. Since $10$ and $91$ are two distinct roots modulo 101, they are *all* the roots.

Therefore:
$$101 \mid n^2 + 1 \iff n \equiv 10 \text{ or } n \equiv 91 \pmod{101}.$$

## Counting

**Class 1: $n = 10 + 101k$, $k \ge 0$.**
$$10 + 101k \le 1000 \iff 101k \le 990 \iff k \le 9.9,$$
so $k \in \{0, 1, \dots, 9\}$: **10 values** ($n = 10, 111, \dots, 919$).

**Class 2: $n = 91 + 101k$, $k \ge 0$.**
$$91 + 101k \le 1000 \iff 101k \le 909 \iff k \le 9,$$
so $k \in \{0, 1, \dots, 9\}$: **10 values** ($n = 91, 192, \dots, 1000$; note $91 + 101 \cdot 9 = 1000$ exactly).

The two classes are disjoint since $10 \not\equiv 91 \pmod{101}$.

**Total:** $10 + 10 = 20$.

## Verification Spot-Checks

- $n = 10$: $10^2 + 1 = 101$. ✓
- $n = 91$: $91^2 + 1 = 8282 = 82 \cdot 101$. ✓
- $n = 1000$: $1000 \equiv -10 \pmod{101}$, so $1000^2 + 1 \equiv 100 + 1 \equiv 0 \pmod{101}$. ✓
- Boundary check: next values would be $n = 1020$ and $n = 1101$, both exceeding 1000, confirming no values are missed or double-counted at the upper endpoint.

ANSWER: 20
