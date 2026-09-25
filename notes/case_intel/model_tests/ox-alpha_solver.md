## Setting Up

I need to find all $n$ with $1 \le n \le 1000$ such that
$$n^2 + 1 \equiv 0 \pmod{101}, \quad \text{i.e., } n^2 \equiv -1 \pmod{101}.$$

## Finding All Solutions Modulo 101

**Key observation:** Since $10^2 = 100 \equiv -1 \pmod{101}$, the value $n = 10$ is a solution.

**Claim:** The only solutions modulo 101 are $n \equiv 10$ and $n \equiv -10 \equiv 91 \pmod{101}$.

*Proof:* If $n^2 \equiv -1 \pmod{101}$, then
$$n^2 - 100 \equiv -1 - 100 \equiv -101 \equiv 0 \pmod{101},$$
so
$$(n-10)(n+10) \equiv 0 \pmod{101}.$$
Since 101 is **prime**, it divides one of the factors (if a prime divides a product, it divides at least one factor). Hence:
$$n \equiv 10 \pmod{101} \quad \text{or} \quad n \equiv -10 \equiv 91 \pmod{101}.$$

These two classes are distinct since $10 \not\equiv 91 \pmod{101}$ (their difference is $81$, not divisible by 101). Conversely, both classes are solutions since $10^2 \equiv 91^2 \equiv (-10)^2 \equiv 100 \equiv -1 \pmod{101}$. $\blacksquare$

So there are exactly **two residue classes** of solutions mod 101.

## Counting in Range $[1, 1000]$

Since $1000 = 9 \cdot 101 + 91$, each residue class appears either 9 or 10 times among $1, \dots, 1000$.

**Class $n \equiv 10 \pmod{101}$:** elements are $10 + 101k$ for $k = 0, 1, \dots$:
$$10,\ 111,\ 212,\ 313,\ 414,\ 515,\ 616,\ 717,\ 818,\ 919.$$
The next term is $1020 > 1000$, so this gives **10 values**.

**Class $n \equiv 91 \pmod{101}$:** elements are $91 + 101k$ for $k = 0, 1, \dots$:
$$91,\ 192,\ 293,\ 394,\ 495,\ 596,\ 697,\ 798,\ 899,\ 1000.$$
The next term is $1101 > 1000$, so this also gives **10 values**. (Note $1000 = 91 + 9\cdot 101$ qualifies; indeed $1000^2 + 1 = 1000001 = 101 \cdot 9901$.)

## Total

$$10 + 10 = 20.$$

ANSWER: 20
