# ATTACK — A067720 Open Lemma, round 2 (TEMPLATE v2.1 campaign structure)

## The problem
Let phi be Euler's totient. For an integer n > 1 write x = n - 1 and M = x^2 + 1, and consider
        (E)   phi(M) = x * phi(n).
Prove: if n is composite, n != 9, and n is not an odd prime square, then (E) FAILS.
(Equivalently: the only composite n satisfying (E) is n = 9.)

## Known givens — all PROVED, several machine-verified here; use freely, re-derive if you prefer
delta(t) := t - phi(t).
G1  gcd(x, M) = 1; gcd(n, M) | 2, equal to 1 for n odd and 2 for n even (since M ≡ 2 mod n).
G2  every odd prime q | M satisfies q ≡ 1 (mod 4).
G3  M prime => n prime. Hence a composite solution needs M composite.
G4  (deficit identity) (E) <=> M - phi(M) = x*(delta(n) - 1) + 1. Write Delta_M for the right side.
G5  every odd prime q | M satisfies q >= M / Delta_M.
G6  N composite and NOT a prime square => delta(N) >= sqrt(2N), with equality iff N = 8.
    [machine-verified for all such N <= 120000: no violation, equality set exactly {8}]
    Corollary: in any counterexample, delta(n) > sqrt(x) + 1.
G7  n = 2^a (a >= 2) is impossible; n = 2p is impossible; and for x > 1 with Q = (x^2+1)/2 prime, impossible.
G8  if p is an odd prime with p^2 | n then some q | M has q ≡ 1 (mod p), hence (with G2) q ≡ 1 (mod 4p).
G9  if q is an odd prime with q^2 | M then some odd p | n has p ≡ 1 (mod q), hence p >= 2q + 1.
    Consequently the largest odd prime factor of n*M occurs to the first power.
G10 (odd n) M cannot be a squarefree semiprime. Proof sketch: q + r = S := x(delta(n)-1) + 2 and qr = x^2+1;
    mod x gives (q-1)^2 ≡ 0 so q >= sqrt(x) + 1; f(t) = t(S-t) is increasing on [0, S/2] and
    f(sqrt(x)+1) > M = f(q), contradiction. Also M cannot have two distinct repeated prime factors.
    Hence omega(M) = 2 forces M = q^b * r exactly, with b >= 2.
G11 (odd prime powers) if n = p^a with p odd and a >= 3 then: M is squarefree; every q | M satisfies q > p;
    sum over q|M of v_p(q-1) equals a-1 with at least one term zero; 2*omega(M) <= v2(p^a - 1) + v2(p - 1);
    and omega(M) = 2 and omega(M) = 3 are both IMPOSSIBLE. So omega(M) >= 4 there.
    [the identity M - p*D = (p-1)(p^a - 2) used in that proof is machine-verified exact]
G12 (even n) write n = 2^a*m with m odd > 1, u = 2^(a-1), h = u*m, x = 2h-1, N = M/2 = 2h^2-2h+1,
    e = h - phi(n) = u*delta(m). Then (E) <=> phi(N) = x*phi(n) and delta(N) = x*e - (h-1);
    2*omega(N) <= (a-1) + sum over p|m of v2(p-1). If N is a squarefree semiprime then e < sqrt(x/2) + 1,
    which excludes every composite odd part m; the surviving branch is m prime with a >= 4, where the
    semiprime case reduces to Y^2 - C z^2 = 4(2u^2 - 2u + 1) with C = 4u^2 - 4u - 7.
G13 [machine-verified] an independent search over k <= 3000 finds 75 solutions of (E) with n = k+1, and
    the ONLY one with composite n is n = 9.

## Current task statement
Give a rigorous standalone proof of the statement above using your own knowledge, computation, and
reasoning, without searching the public web, connected sources, previous conversations, or project
contexts. Assume for purposes of this task that a complete affirmative proof exists. Work iteratively
until a correct proof has been reached.

Partial progress does not count unless it implies exactly the resolution of the entire statement. In
particular, reductions to other unproved statements, verification for bounded n, and heuristic density
arguments are insufficient. G1-G13 are already ours; restating them is not progress.

Use multiagents aggressively and dynamically. Do not use a fixed assignment such as "N agents for
strategy X." Instead:
- Begin with a genuinely diverse portfolio. Distinct families worth separate agents: (i) the
  factor-allocation/resultant route — write M = prod q_i, allocate x = prod d_i with d_i | q_i - 1,
  q_i = d_i h_i + 1, and exploit q_i | y_i^2 + h_i^2 where y_i = x/d_i; (ii) 2-adic budget accounting —
  every q ≡ 1 mod 4 spends at least 2 from v2(phi(M)) = v2(x) + v2(phi(n)); (iii) size/counting —
  omega(M) <= log M / log(min q) combined with G5; (iv) smallest-counterexample descent; (v) the even
  branch Pell equation of G12 with the primality and congruence side conditions; (vi) a route that
  treats n and M symmetrically via the Gaussian integers (M = x^2+1 = (x+i)(x-i)) and reads the
  constraints as conditions on Gaussian prime factors of x + i.
- Do not tell most agents the currently favored route; preserve independence in early rounds.
- Maintain an explicit registry of approach families grouped by mathematical idea; redirect agents out
  of overcrowded families.
- A route that ends at a statement of the same strength (e.g. "no such factorisation of M exists") is
  NOT close to completion unless it supplies a genuinely new mechanism.
- Use adversarial agents throughout: every candidate proof is checked for gaps, hidden conditionals,
  handwaving, circularity, and for silently assuming n odd or M squarefree. Reject status reports and
  claims that a step is "routine".
- Require concrete lemmas, inequalities, and explicit constants — not plans.
- The root agent repeatedly synthesizes, challenges, redirects, and launches new rounds. Do not stop
  after the first wave fails. Do not return because approaches fail or agents report equal-strength gaps.
  Produce a complete proof if one survives audit; otherwise report only the strongest rigorously proved
  derivation and its exact remaining gap — never return an empty answer.

Return only when a complete proof has been found and survives adversarial audit, or (failing that) with
the strongest rigorously proved derivation and its exact remaining gap. Do not return a bounded
verification, a heuristic, or an explanation of why the problem is hard. Do not search the web to
determine whether the statement is open, and do not answer that it is open.

## Output contract (applied after the audit passes)
Numbered lemmas, each step elementary and independently checkable; then (1) what a Lean formalisation
needs, module by module; (2) every finite computation you relied on, stated so it can be re-run.
A check that cannot fail counts as no check.
