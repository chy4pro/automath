# ATTACK BRIEF — ERDOS PROBLEM #203 (LLM-first: you design the object; machines only verify a finite table)
Step 0 (G2): state status as you know it + solved-after-cutoff risk. Then attack regardless.
TARGET: find an integer m with gcd(m,6)=1 such that 2^k * 3^l * m + 1 is COMPOSITE for all k,l >= 0.
(Erdos problem 203; listed open. A single explicit m with a finite covering certificate settles it.)
METHOD (LLM constructs, machine verifies): design a COVERING SYSTEM on the exponent lattice (k,l):
for each residue class (k = a mod A, l = b mod B) choose a prime p with a fixed multiplicative order
pattern so that p | 2^k 3^l m + 1 identically on that class; then solve the resulting congruences on m
by CRT to produce ONE explicit integer m.
Concretely: pick primes p with ord_p(2) = A_p and ord_p(3) = B_p; on the class k = a (mod A_p),
l = b (mod B_p) we need m = -2^{-a} 3^{-b} (mod p). Choose a finite family of primes whose classes
COVER the whole lattice Z_{>=0}^2, check the CRT system is consistent (distinct primes, compatible
conditions), and output m (any positive solution, plus gcd(m,6)=1 and m+1 composite handled).
DELIVERABLES: (1) the explicit covering family: list of (p, A_p, B_p, a, b) rows with proof that the
classes cover the lattice; (2) the CRT solution m as an explicit integer (or the exact congruence
system if the number is huge); (3) a verification recipe: for each row, the finite check
"2^a 3^b m + 1 = 0 (mod p)" plus the order computations, and a covering check on the finite grid
[0,lcm A) x [0,lcm B); (4) an argument that each such value is composite, not merely divisible
(i.e. 2^k 3^l m + 1 > p). If you cannot cover the full lattice, state the exact uncovered classes
and the obstruction. Number every lemma. Machines verify only finite tables; the design must be yours.
