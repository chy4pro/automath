# ATTACK — Erdős Problem #708, round 8: the hinge inequality for FRACTIONAL weights with a ln ln m threshold (TEMPLATE v2.3, inequality type)

## The statement to prove
Weights z_p ∈ [0,1] on primes (finitely many nonzero), w(n) := Σ_p z_p v_p(n), m ≥ 1, x ≥ 0, I := {x+1,…,x+m}, K := {1,…,m}.
   (TH_c)   Σ_{k≤m} (w(k)−c)⁺ ≤ Σ_{b∈I} (w(b)−1)⁺.
PROVED consequences: (TH_2) ⇒ g(n) ≤ 18n; more generally (TH_c) for all weights supported on the primes dividing ∏a_i ⇒
g(n) ≤ (c+16)n whenever a_n < 8n³ (and 2n suffice for a_n ≥ 8n³). Hence (TH_c) with c = C ln ln m for all m gives
g(n) ≤ (C ln ln(8n³) + 17) n = O(n ln ln n), which beats the best published bound (2+o(1)) n √(ln n / ln ln n).

## What is PROVED (use freely)
P1 THEOREM A (0/1 weights, all m, x, P): Σ_{n≤m}(Ω_P(n) − c*(m))⁺ ≤ Σ_{b∈I}(Ω_P(b) − 1)⁺ with c*(m) = 5 + max(2, ⌈2e² ln(1 + ln m/6)⌉) ≤ 20 ln ln m.
   Proof structure (every step elementary; keep it as the template):
   (a) Σ_{p≤y} 1/p ≤ e ln(1 + ln y) (σ = 1 + 1/ln y, p^{σ−1} ≤ e, Σ p^{−σ} ≤ ln ζ(σ) ≤ ln(1 + ln y)).
   (b) SIEVE LEMMA: L ≥ 64, Q any finite prime set, J any L consecutive integers, s(L) := max(2, ⌈2e² ln(1 + ln L/6)⌉):
       #{n ≤ L : ω_Q(n) ≥ s(L)+5} ≤ #{n ∈ J : ω_Q(n) ≥ 1}.  Proof: y = L^{1/6}, R = {q ∈ Q : q ≤ y}, H = Σ_R 1/q; n ≤ L has ≤ 5 prime
       factors > y; #{n ≤ L : ω_R ≥ s} ≤ L H^s/s! ≤ L(eH/s)^s ≤ L 2^{−s} ≤ L/4; for the interval, two-term Bonferroni with
       L/d − 1 < N_J(d) < L/d + 1 on a subfamily R′ with 1/2 ≤ H′ ≤ 1 gives #{n ∈ J : ω_{R′} ≥ 1} ≥ L(H′ − H′²/2) − (3/4)y² ≥ L/4;
       if H < 1/2 use R itself: ≥ (3/4)LH − (3/4)y² ≥ LH/4 ≥ L H²/2 ≥ #{ω_R ≥ s}.
   (c) ORDERING IDENTITY: (ω_P(n) − c)⁺ = Σ_{p∈P, p|n} [ω_{<p}(n) ≥ c] (ω_{<p} counts the P-primes below p dividing n).
   (d) per prime p: n = pi ≤ m ⇒ i ≤ L := ⌊m/p⌋ and ω_{<p}(pi) = ω_{<p}(i); the multiples of p in I are p·J_p with J_p a run of L or
       L+1 consecutive integers; apply (b) with Q = {q ∈ P : q < p} (L ≥ 64; for L < 64, ω ≤ 3 < 7 ≤ c*); sum over p.
   (e) prime powers peel off: (Ω−1)⁺ = E + (ω−1)⁺, (Ω−c)⁺ ≤ E + (ω−c)⁺, Σ_I E ≥ Σ_K E, E := Ω − ω.
P2 LOSSLESS PEEL for fractional weights: with S(n) := Σ_p min(z_p v_p(n), 1) and E(n) := Σ_p (z_p v_p(n) − 1)⁺ one has w = E + S,
   (w−1)⁺ = E + (S−1)⁺, (w−c)⁺ ≤ E + (S−c)⁺, Σ_I E ≥ Σ_K E (nonnegative increments Δ_{p,j} = (z_p j−1)⁺ − (z_p(j−1)−1)⁺ on p^j).
   So (TH_c) for all weights follows from   (S_c):  Σ_{k≤m} (S(k) − c)⁺ ≤ Σ_{b∈I} (S(b) − 1)⁺.
   Rational weights z_p = a_p/N: multiply by N: R(n) := Σ_p r_p(n), r_p(n) := min(a_p v_p(n), N) ∈ [0, N]; (S_c) ⟺ Σ_K (R − cN)⁺ ≤ Σ_I (R − N)⁺.
P3 WEIGHTED ORDERING IDENTITY (dialogue, proved): order the primes dividing n as p_1 < … < p_k, prefix sums R_{<p}(n) := Σ_{q<p, q|n} r_q(n).
   For every threshold T ≥ 0:   (R(n) − T − N)⁺ ≤ Σ_{p|n} r_p(n)·[R_{<p}(n) ≥ T] ≤ (R(n) − T)⁺.
   (Proof: let j* be the first index with R_{≤p_{j*}} ≥ T; the sum equals R(n) − R_{≤p_{j*}}, and T ≤ R_{≤p_{j*}} < T + N.)
   Consequently (S_c) ⟸  for every prime p:  Σ_{k≤m, p|k} r_p(k)[R_{<p}(k) ≥ (c−1)N] ≤ Σ_{b∈I, p|b} r_p(b)[R_{<p}(b) ≥ N].
   Writing r_p(k) = Σ_{j≥1} Δ_{p,j}[p^j | k] with Δ_{p,j} = min(a_p j, N) − min(a_p(j−1), N) ≥ 0, and R_{<p}(p^j i) = R_{<p}(i), it suffices that
   for every p, every j ≥ 1, L := ⌊m/p^j⌋ and every run J of L consecutive integers (the quotient set of the multiples of p^j in I has L or L+1):
   (WSL)   #{i ≤ L : R_Q(i) ≥ (c−1)N} ≤ #{i ∈ J : R_Q(i) ≥ N},   Q := {q : q < p, a_q > 0},  R_Q(i) := Σ_{q∈Q} min(a_q v_q(i), N).
   For 0/1 weights (a_q ∈ {0,N}) (WSL) is exactly the sieve lemma (b). So (WSL) with c − 1 = C ln ln L is the whole remaining task.
P4 COUNTING CERTIFICATES (proved principle): if Σ_{d|n} c_d ≤ (w(n)−1)⁺ for all n then Σ_I (w−1)⁺ ≥ Σ_{c_d>0} c_d⌊m/d⌋ − Σ_{c_d<0}|c_d|(⌊m/d⌋+1);
   LP-verified certificates exist for fractional weights at m ≤ 200 (types LP) and for 0/1 weights at m ≤ 1000 (all primes). Two useful
   feasible certificates for any weights: the AFFINE one c_1 = −1, c_{p^j} = z_p (value Σ_K w − m − 1, enough when Σ_K min(w,2) ≥ m+1), and
   for a single prime the increment certificate c_{p^j} = (z_p j − 1)⁺ − (z_p(j−1) − 1)⁺ (value Σ_K (w−1)⁺).

## Machine facts
M1 (TH_2): 2.1·10⁶ instances, no counterexample; ≥ 0.18m slack on dense windows of length 10⁵. Theorem A: 5·10⁴ tests, min slack 0.
M2 Dense windows (Hensley–Richards) exist; any argument using only lower bounds N_I(d) ≥ ⌊m/d⌋ at a single threshold fails on them
   (D1–D4, D7 of earlier rounds); the sieve lemma survives because it uses the UPPER bound on pairs (Bonferroni).

## Targets, in order of value (prove-or-refute, equal rank)
T1 Prove (WSL) — equivalently (S_c) — with c = C ln ln m for an explicit absolute C, all weights (⇒ g(n) = O(n ln ln n), improving the
   published √-bound). Route: generalise the sieve lemma. On the left, R_Q(i) ≥ (c−1)N forces many Q-primes with large a_q or very many
   with small a_q; bound by moments of the weighted sum Σ_{q|i} u_q (u_q = a_q/N ∈ [0,1]) as in (b) (e_s bounds with weights u_q/q).
   On the right, #{i ∈ J : Σ_{q|i} u_q ≥ 1} needs a lower bound in an arbitrary interval: split Q by weight (u_q ≥ 1/2 primes give
   "one hit suffices" — Bonferroni as in (b); light primes need ≥ 2 hits — second-order Bonferroni with the interval bounds, or the
   weighted second moment); take the better of the two families. Every constant explicit.
T2 Prove (S_2) — the exact fractional hinge inequality — by an explicit counting certificate for all m (⇒ g(n) ≤ 18n).
T3 Refute: an explicit instance (m, weights) and an explicit abstract multiset of valuation patterns satisfying ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1
   for all d with Σ_t n_t (w(t)−1)⁺ < Σ_K (w−2)⁺, or an explicit counterexample to (WSL) for some c (we re-check everything).
T4 (TH_c) for fractional weights with c = C·(ln ln m)² or c = C ln m, if T1 resists (still explicit; state the resulting bound on g).
Rule: no intermediate statement is used before an adversarial agent has tried to break it on the dense-window structure and on
weight patterns with many light primes; every lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; the answer ends
with a dependency list "final claim ← lemmas ← unproved items".

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; partial progress
counts only if it implies exactly one of T1–T4. Use multiagents aggressively and dynamically: (i) the weighted sieve lemma with
explicit constants (several agents, different splits of Q by weight); (ii) counting certificates for fractional weights (T2) built
from the affine and increment certificates plus anchor stars; (iii) an adversarial team building abstract multisets and dense windows
against every candidate; (iv) T4 as the fallback with explicit constants. Budget: about two hours; then return the strongest
rigorously proved derivation with its exact gap (do not fail silently).

## Output contract
Numbered lemmas with status tags; every constant explicit; every finite computation stated so it can be re-run; what a Lean
formalisation needs. A check that cannot fail counts as no check.
