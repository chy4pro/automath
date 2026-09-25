# ATTACK BRIEF — CLOSE THE A067720 OPEN LEMMA (LLM-first: you construct the proof; machines only verify)
Step 0 (G2): state current status as you know it + solved-after-cutoff risk. Then attack regardless.

CONTEXT (already PROVED by our pipeline, treat as given but re-derive anything you rely on):
Notation n = k+1, x = n-1, M = x^2+1, delta(t) = t - phi(t). Equation (E): phi(M) = x*phi(n).
L1 gcd(x,M)=1; gcd(n,M)|2 (=1 for n odd, =2 for n even).
L2 every odd prime q | M satisfies q = 1 (mod 4).
L3 M prime  =>  n prime.
L4 (deficit identity) (E)  <=>  M - phi(M) = x*(delta(n) - 1) + 1.
L5 n composite => delta(n) >= sqrt(n), equality iff n = p^2.
L6 every odd prime q | M satisfies q >= M / Delta_M, where Delta_M = x*(delta(n)-1)+1.
L7 n = 2^a (a>=2) impossible; also x>1 with Q=(x^2+1)/2 prime impossible.
L8 if p odd prime with p^2 | n then some q | M has q = 1 (mod p).
THEOREM A (proved): if n = p^2 (prime square) and (E) holds then p = 3, i.e. k = 8.

YOUR TARGET — the OPEN LEMMA, the single remaining gap:
Let n > 1 be composite, n != 9, and NOT an odd prime square. Prove phi((n-1)^2+1) != (n-1)*phi(n).
Equivalently (ratio form): with A = distinct primes of n, B = distinct odd primes of M,
   prod_{q in B} (1 - 1/q)  =  (1 + (x-1)/(x^2+1)) * prod_{p in A} (1 - 1/p)
is impossible, subject to: every q in B is 1 mod 4; no odd q in B divides n; if p^2 | n then some
q in B is 1 mod p; and the L6 lower bound.
Sub-cases to cover: (a) even composite n not a power of 2; (b) odd squarefree composite with >= 2
prime factors; (c) odd prime powers p^a, a >= 3; (d) mixed composites.

STRATEGY HINTS (improve on them): the RHS exceeds prod(1-1/p) by a factor 1 + (x-1)/(x^2+1) ~ 1 + 1/x,
so B's totient ratio must exceed A's by a hair — but B's primes are all 1 mod 4 and disjoint from n,
which forces them large (L6) while the deficit identity pins their total size; try (i) counting: the
number of prime factors of M is bounded by log M / log(smallest allowed q); (ii) 2-adic valuation
bookkeeping in the even case; (iii) for case (c) push the Theorem A machinery (resultant restriction
q | H(h), discriminant squeeze) to p^a; (iv) a smallest-counterexample descent.
REQUIREMENTS: number every lemma; each step elementary and independently checkable; end with
(1) a verification plan (finite computations + what Lean would need), (2) if you cannot close it,
the EXACT residual statement as a precise open lemma — no hand-waving. A check that cannot fail is no check.
