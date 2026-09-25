# The equation \(\sigma(n)=2\sigma^*(n)\)

Here \(\sigma^*\) denotes the sum of unitary divisors.  I will first point
out an error in the data in the question.  Directly from the definitions,

\[
\begin{array}{c|c|c|c}
n&\sigma(n)&\sigma^*(n)&\sigma(n)-2\sigma^*(n)\\ \hline
972=2^2 3^5&7\cdot364=2548&5\cdot244=1220&108,\\
1620=2^2 3^4 5&7\cdot121\cdot6=5082&5\cdot82\cdot6=2460&162.
\end{array}
\]

Thus 972 and 1620 are not members of the set defined in the question.
This does not by itself disprove either conjecture, since both numbers are
nevertheless congruent to 108 modulo 216.

I was not able to prove or disprove the two global conjectures.  What
follows is a rigorous reduction, exact 2-adic and 3-adic constraints, a
proof of the conjectures when the part coprime to 6 is squarefree, and a
clearly marked exhaustive computational lemma.  In particular, none of
the finite computation below is being presented as a proof of an
unbounded assertion.

## 1. Multiplicative reduction

For a prime power,

\[
 \sigma(p^e)=1+p+\cdots+p^e,
 \qquad \sigma^*(p^e)=1+p^e.
\]

Both functions are multiplicative.  Put

\[
 \rho(p,e)=\frac{1+p+\cdots+p^e}{1+p^e}.
\]

Then

\[
 n\in A\quad\Longleftrightarrow\quad
 \prod_{p^e\parallel n}\rho(p,e)=2.                 \tag{1}
\]

Notice that \(\rho(p,1)=1\), while \(\rho(p,e)>1\) for
\(e\geq2\).  Also

\[
 \rho(p,e)<\frac p{p-1}.                            \tag{2}
\]

Indeed, the numerator is less than \(p^{e+1}/(p-1)\),
and the denominator is greater than \(p^e\).

Write

\[
 n=2^a3^b m,\qquad (m,6)=1.
\]

For \(c\geq0\), define

\[
 U_2(c)=\begin{cases}1,&c=0,\\2^c+1,&c>0,
 \end{cases}
 \qquad
 U_3(c)=\begin{cases}1,&c=0,\\3^c+1,&c>0.
 \end{cases}
\]

Multiplicativity gives the exact equation

\[
 (2^{a+1}-1)\frac{3^{b+1}-1}{2}\,\sigma(m)
   =2U_2(a)U_3(b)\sigma^*(m).                       \tag{3}
\]

When \(a,b>0\), this can equivalently be written

\[
 (2^{a+1}-1)(3^{b+1}-1)\sigma(m)
 =4(2^a+1)(3^b+1)\sigma^*(m).                       \tag{4}
\]

There is an important immediate consequence of (1).

**Lemma 1.** If \(n\in A\) and \(p\parallel n\), then \(n/p\in A\).
Consequently every primitive member of \(A\) is powerful: every prime
which divides it occurs to exponent at least 2.

**Proof.** Removing \(p\) removes the factor \(\rho(p,1)=1\) from
(1), and hence does not change the product. \(\square\)

## 2. The exact 2-adic constraint

For an odd prime \(p\), set

\[
 D_2(e)=v_2(\sigma(p^e))-v_2(1+p^e).
\]

The value is independent of the odd prime \(p\), and is

\[
 D_2(e)=
 \begin{cases}
 -1,&e\text{ even},\\
 v_2(e+1)-1,&e\text{ odd}.
 \end{cases}                                        \tag{5}
\]

For even \(e\), \(\sigma(p^e)\) is a sum of an odd number of odd
terms, so it is odd; moreover \(p^e\equiv1\pmod8\), and hence
\(v_2(1+p^e)=1\).  For odd \(e\), the standard 2-adic LTE formula
gives

\[
\begin{aligned}
 v_2(\sigma(p^e))
 &=v_2(p^{e+1}-1)-v_2(p-1)\\
 &=v_2(p+1)+v_2(e+1)-1,
\end{aligned}
\]

while the odd-exponent LTE formula gives
\(v_2(p^e+1)=v_2(p+1)\).  This proves (5).

The factors belonging to 2 in both \(\sigma(n)\) and
\(\sigma^*(n)\) are odd.  Taking 2-adic valuations in the defining
equation therefore gives

\[
 \boxed{\ \sum_{\substack{p^e\parallel n\\p\ {m odd}}}D_2(e)=1.\ }
                                                               \tag{6}
\]

Equivalently, in the notation \(n=2^a3^bm\), the term \(D_2(b)\)
is included if \(b>0\), followed by the corresponding terms for the
prime powers in \(m\).

Some useful consequences are:

* at least one odd prime occurs to an exponent congruent to 3 modulo 4;
* every even exponent at an odd prime contributes \(-1\);
* an odd exponent contributes positively precisely when it is congruent
  to 3 modulo 4, and its contribution is \(v_2(e+1)-1\).

Thus (6) is a substantial restriction, but by itself it does not identify
the odd prime carrying the positive contribution as 3.

## 3. The exact 3-adic constraint

For \(p\ne3\), put

\[
 D_3(p,e)=v_3(\sigma(p^e))-v_3(1+p^e).
\]

One has

\[
 D_3(p,e)=
 \begin{cases}
 v_3(e+1),&p\equiv1\pmod3,\\
 0,&p\equiv-1\pmod3\text{ and }e\text{ even},\\
 v_3(e+1)-v_3(e),&p\equiv-1\pmod3\text{ and }e\text{ odd}.
 \end{cases}                                        \tag{7}
\]

For \(p\equiv1\pmod3\), LTE applied to
\((p^{e+1}-1)/(p-1)\) gives the first line, and \(1+p^e\) is not
divisible by 3.  If \(p\equiv-1\pmod3\) and \(e\) is even, neither
quantity is divisible by 3.  If \(e\) is odd, LTE gives

\[
 v_3(1+p^e)=v_3(p+1)+v_3(e)
\]

and, since \(e+1\) is even,

\[
 v_3(\sigma(p^e))=v_3(p+1)+v_3(e+1),
\]

which proves the last line.  The prime-power factors belonging to 3
itself have 3-adic valuation zero on both sides.  Hence

\[
 \boxed{\ \sum_{\substack{p^e\parallel n\\p\ne3}}D_3(p,e)=0.\ }
                                                               \tag{8}
\]

In terms of \(2^a3^bm\), (8) contains the contribution of \(2^a\)
when \(a>0\), and those of the prime powers in \(m\); the exponent
\(b\) makes no contribution.  In particular, the contribution of
\(2^a\) is zero when \(a\) is even.  When \(a\) is odd it is

\[
 v_3(a+1)-v_3(a).                                   \tag{9}
\]

Equations (6) and (8) are the requested exact 2-adic and 3-adic
constraints on \(a,b\) and the remaining prime-power exponents.

## 4. Complete result when \(m\) is squarefree

**Theorem 2.** Suppose \(n=2^a3^bm\), where \((m,6)=1\) and \(m\)
is squarefree.  Then

\[
 n\in A\quad\Longleftrightarrow\quad a=2,quad b=3.
                                                               \tag{10}
\]

Thus all such solutions are exactly

\[
 n=108m,\qquad m\text{ squarefree and }(m,6)=1.       \tag{11}
\]

**Proof.** Since \(m\) is squarefree,
\(\sigma(m)=\sigma^*(m)\), so its factor cancels from (3).  If
\(a=0\) or 1, the 2-part has ratio 1, while the 3-part has ratio
strictly less than \(3/2\) by (2); the product cannot be 2.  If
\(b=0\) or 1, the 3-part has ratio 1, while the 2-part has ratio
strictly less than 2.  Hence \(a,b\geq2\).

Set \(A=2^a\) and \(B=3^b\).  After cancellation, (4) becomes

\[
 (2A-1)(3B-1)=4(A+1)(B+1),
\]

or

\[
 2AB=6A+7B+3.                                       \tag{12}
\]

A useful factorization of (12) is

\[
 (2A-7)(2B-6)=48.                                   \tag{13}
\]

Both factors are now positive.  The first factor is an odd positive
divisor of 48, so it is 1 or 3.  The value 3 would give
\(2^{a+1}=10\), which is impossible.  Therefore it is 1, giving
\(a=2\).  Equation (13) then gives \(2\cdot3^b-6=48\), hence
\(b=3\).  Conversely,

\[
 \rho(2,2)\rho(3,3)=\frac75\frac{10}{7}=2,
\]

and every prime occurring once in \(m\) contributes a factor 1.
This proves both directions. \(\square\)

In particular all the numbers in (11) satisfy

\[
 n=108m\equiv108\pmod{216},
\]

because \(m\) is odd.  Lemma 1 and Theorem 2 also show that 108 is
the only primitive solution whose part coprime to 6 is squarefree.

Any counterexample to part (a), therefore, must contain a prime
\(p\geq5\) to exponent at least 2.  Any second primitive solution must
be powerful and must have such a prime divisor.

## 5. Relation between the two conjectures

The congruence in (a) is equivalent to

\[
 v_2(n)=2\quad\text{and}\quad v_3(n)\geq3.           \tag{14}
\]

Indeed, \(n\equiv108\pmod{216}\) says exactly that
\(n=108(2k+1)\).

Consequently, if (a) is true, then (b) follows immediately.  Every
member of \(A\) would be divisible by 108; since \(108\in A\), every
larger member would have a proper divisor in \(A\).  The same statement
would also show that no proper divisor of 108 belongs to \(A\), so 108
would itself be primitive.

## 6. Computational lemma (finite, exhaustive)

**Computational Lemma.** The only powerful integer \(N\leq10^{12}\)
satisfying \(\sigma(N)=2\sigma^*(N)\) is \(108\).  Consequently every
member of \(A\) up to \(10^{12}\) is of the form (11), and 108 is the
only primitive member up to that bound.

Here is the complete Python 3 computation used for the lemma.  It tests
2,158,390 canonical representations and returns `[(108, ((2, 2),
(3, 3)))]`.

```python
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
```

For completeness, the exhaustion rests on the following standard unique
parametrization.  Every powerful integer has a unique representation

\[
 N=x^2y^3,\qquad y\text{ squarefree}.                \tag{15}
\]

For a prime exponent \(e\geq2\), put the prime in \(y\) precisely when
\(e\) is odd.  If \(e\) is even, its exponent in \(x\) is \(e/2\);
if \(e\) is odd, its exponent in \(x\) is \((e-3)/2\).  This proves
existence and uniqueness of (15).  The bounds in the loops are exactly
\(y\leq X^{1/3}\) and \(x\leq\sqrt{X/y^3}\), so every powerful integer
up to the stated bound is tested once.

Finally, removing all exponent-one prime factors from any member of
\(A\) preserves (1) and leaves a powerful member of \(A\).  The
computational result therefore implies that, below the bound, this core
is 108.  The removed primes form a squarefree number coprime to 6,
which proves the stated finite classification.

## Conclusion

The prompt's displayed list contains two nonmembers.  Unconditionally,
the multiplicative equation is (3), its exact valuation restrictions are
(6) and (8), and the conjectured classification is proved whenever the
part coprime to 6 is squarefree.  A counterexample to either the expected
classification or primitivity statement must introduce a genuinely new
powerful core containing the square of a prime at least 5; exhaustive
search shows that no such core exists through \(10^{12}\).  The arguments
above do not exclude one beyond that bound, so they do not settle (a) or
(b) in full.
