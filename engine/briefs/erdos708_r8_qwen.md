# MICRO-LEMMA — Erdős Problem #708, round 8 (single-shot): a two-layer sieve lemma for intervals, with explicit constants

## Setting (all proved, use freely)
For a finite set of primes Q and an integer i let ω_Q(i) be the number of primes of Q dividing i. Any set J of L consecutive
integers satisfies L/d − 1 < N_J(d) < L/d + 1 for the number N_J(d) of multiples of d in J. Known (proved): for L ≥ 64 and
s(L) := max(2, ⌈2e² ln(1 + ln L/6)⌉),  #{i ≤ L : ω_Q(i) ≥ s(L)+5} ≤ #{i ∈ J : ω_Q(i) ≥ 1}  for every Q and every such J
(proof: y = L^{1/6}, R = {q ∈ Q : q ≤ y}, H = Σ_R 1/q ≤ e ln(1 + ln y); at most 5 prime factors > y; #{i ≤ L : ω_R ≥ s} ≤ L H^s/s! ≤ L/4;
two-term Bonferroni on a subfamily R′ with 1/2 ≤ H′ ≤ 1 gives #{i ∈ J : ω_{R′} ≥ 1} ≥ L(H′ − H′²/2) − (3/4)y² ≥ L/4, and if H < 1/2
then ≥ (3/4)LH − (3/4)y² ≥ LH/4 ≥ L H²/2). This one-layer lemma gives a hinge inequality for 0/1 weights; the two-layer version below
is what the case of weights equal to 1/2 needs.

## The statement to prove (two-layer sieve lemma)
Find an explicit function t(L) = O(ln ln L) such that for every finite prime set Q, every L ≥ L₀ (explicit) and every set J of L
consecutive integers:
   (TL)   #{i ≤ L : ω_Q(i) ≥ t(L)} ≤ #{i ∈ J : ω_Q(i) ≥ 2}.
Warning (proved false): the single-threshold version #{i ≤ L : ω_Q(i) ≥ 2} ≤ #{i ∈ J : ω_Q(i) ≥ 1} FAILS for L = 10^5 (windows with
more integers free of small primes than [1,L]); so the left threshold must grow, as in the known lemma.

## Targets, in order of value
T1 Prove (TL) with explicit t(L) and L₀, by the method of the known lemma: bound the left side by moments (e_s ≤ H^s/s!), and bound
   #{i ∈ J : ω_Q(i) ≥ 2} from below by a second-order Bonferroni inequality on a suitable subfamily R′ of small primes with the
   interval bounds L/d − 1 < N_J(d) < L/d + 1 (count pairs, subtract triples; or count "at least two hits" via
   Σ_{q<q′} N_J(qq′) − 2 Σ_{q<q′<q″} N_J(qq′q″) ≤ #{i : ω ≥ 2}·C(ω,2)…; state exactly which identity is used).
T2 The weighted version: for weights u_q ∈ [0,1] on Q and U(i) := Σ_{q∈Q, q|i} min(u_q·v_q(i), 1)… (or simply Σ_{q|i} u_q), prove
   #{i ≤ L : U(i) ≥ t(L)} ≤ #{i ∈ J : U(i) ≥ 1} with explicit t(L) = O(ln ln L), for all u; state precisely the lower bound on the
   right side that you can prove (e.g. split Q into heavy primes u_q ≥ 1/2 and light primes and use the better of the two).
T3 A counterexample to (TL) for every t(L) ≤ 20 ln ln L, i.e. an explicit Q, L, J (we re-check it).

## Task statement
Give a rigorous standalone proof using your own knowledge, computation and reasoning, without searching the public web or other
sources. Work until a proof survives your own adversarial audit, or deliver the strongest of T2–T3. Every claimed lemma carries a
status tag PROVED / CONDITIONAL / CONJECTURED. Every constant explicit. Do not return a bounded verification alone, a heuristic,
or an explanation of why the problem is hard.

## Output contract
Numbered lemmas, every constant explicit, every finite computation stated so it can be re-run.
