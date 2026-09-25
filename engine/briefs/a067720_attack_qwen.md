# ATTACK BRIEF — OEIS A067720 uniqueness (LLM-first; construct proof, machines only verify)
Step 0 (G2, do first): state what you know about current status of this problem; flag any
solved-after-cutoff risk explicitly. Then attack regardless (your proof attempt is the deliverable).
CONJECTURE (formal-conjectures FormalConjectures/OEIS/A067720): for k a positive integer,
if phi(k^2+1) = k * phi(k+1) and k != 8, then k+1 is prime. (phi = Euler totient.
Known: k=8 is the sole known exception: phi(65)=48=8*phi(9)=8*6.)
TASK: produce a COMPLETE proof or an explicit counterexample.
Proof route hints (yours to improve): compare phi(k^2+1)/(k^2+1) with k*phi(k+1)/(k^2+1);
note k^2+1 = (k+1)^2 - 2(k+1) + 2; gcd(k^2+1, k+1) | 2; if k+1 composite then phi(k+1) <= (k+1)(1-1/p)(...)
forces a sharp deficit; local valuations at 2; bound the totient ratio on both sides.
Requirements: every step elementary and checkable; number all lemmas; end with a
verification plan (which finite computations would confirm each lemma, and what a Lean
formalization would need). If the proof fails, state the EXACT sticking point as a
precise open lemma. No hand-waving; a check that cannot fail counts as no check.
