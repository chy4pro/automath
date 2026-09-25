# Independent solve task (elementary number theory)

This is a research-style number theory problem. Solve it and give a rigorous
proof. Do not search the internet. Do not read files outside this task file.
If you cannot fully solve it, present only rigorously proven partial results.

Let sigma(n) denote the sum of all divisors of n, and usigma(n) the sum of
unitary divisors (d | n with gcd(d, n/d) = 1). Consider the set
  A = { n >= 1 : sigma(n) = 2 * usigma(n) }
(equivalently: the sum of non-unitary divisors of n equals the sum of
unitary divisors). Known members: 108, 540, 756, 972, 1188, 1620, ...

Prove or disprove:
(a) every n in A satisfies n ≡ 108 (mod 216);
(b) 108 is the only "primitive" member of A (one having no proper divisor
    in A).

Analyze the multiplicative structure: for n = 2^a * 3^b * m with
gcd(m,6)=1, express the condition via sigma and usigma multiplicativity,
and derive constraints on a and b (2-adic and 3-adic). You may use python3
for exploration, but the final write-up must be a proof; mark any
computational lemmas clearly. Write your complete solution to
notes/reviews/a63880_codex_solve.md.
