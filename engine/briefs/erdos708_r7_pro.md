# ATTACK — Erdős Problem #708, round 7: COUNTING CERTIFICATES for the hinge inequality (campaign structure, TEMPLATE v2.3, inequality type)

## The statement (the hinge inequality)
Weights z_p ∈ [0,1] on primes (finitely many nonzero), w(n) := Σ_p z_p v_p(n), m ≥ 1, x ≥ 0, I := {x+1,…,x+m}, K := {1,…,m}.
   (TH)   Σ_{k≤m} (w(k)−2)⁺ ≤ Σ_{b∈I} (w(b)−1)⁺.
PROVED consequence: (TH) ⇒ g(n) ≤ 18n for the Erdős–Surányi function (LP duality; only weights supported on the primes dividing
∏a_i are needed). (TH) has no counterexample among 2.1·10⁶ tested instances and on dense windows of length 10⁵–10⁶.

## The certificate principle (PROVED — this is the route; read it carefully)
Every interval of length m satisfies, for every integer d ≥ 1:   ⌊m/d⌋ ≤ N_I(d) := #{b∈I : d | b} ≤ ⌊m/d⌋ + 1.
Let c = (c_d) be real coefficients, finitely many nonzero, indexed by integers d composed of the weighted primes, such that
   (F)   Σ_{d | n} c_d ≤ (w(n)−1)⁺   for every positive integer n (equivalently for every valuation pattern).
Then Σ_{b∈I}(w(b)−1)⁺ ≥ Σ_d c_d N_I(d) ≥ V(c) := Σ_{c_d>0} c_d ⌊m/d⌋ − Σ_{c_d<0} |c_d| (⌊m/d⌋+1).
So (TH) holds for (m, z) and EVERY x as soon as some c satisfies (F) and V(c) ≥ W(m,z) := Σ_{k≤m} (w(k)−2)⁺. No property of x is
used — the Hensley–Richards dense windows (which killed every earlier route) are handled by the UPPER bound N_I(d) ≤ ⌊m/d⌋+1,
which those routes never used. Finding the best c is an LP (dual of: minimise Σ_t n_t (w(t)−1)⁺ over multisets of valuation
types t with ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1 for all d). We solved it:
E1 general weights, types t = capped exponent vectors, m ≤ 200, up to 7 primes, z ∈ {1, 0.7, 0.4, mixed}: LP optimum ≥ W in every
   case (m=100, primes ≤ 17: 114 vs W=64 for z≡1; 63.3 vs 22 for z≡0.7; 16.4 vs 0.8 for z≡0.4). The optimal certificates use only
   d ≤ m: prime powers p^j (c=1), a few pairs pq (c=1), a few triples pqr (c=−1).
E2 0/1 weights (z = 1_P), P = all primes ≤ m, c supported on pairs and triples, constraint generation over all subsets S ⊆ P:
   m=300: 223.5 vs W=59; m=500: 407.4 vs 124; m=1000: ≈907 vs 321. Other P (P∖{2}, P∖{2,3}, random halves, primes in [5,400],
   primes ≤ 20) at m=400: all certified with ≥ 3× margin.

## An explicit family (dual feasibility PROVED)
0/1 weights, prime set P, R := first r primes of P. c_d := (−1)^{|A'|} for d = ∏A', A' ⊆ R, |A'| ≥ 2; c_d := (−1)^{|A'|+1} for
d = q·∏A', q ∈ P∖R, ∅ ≠ A' ⊆ R; c = 0 otherwise; prime powers p^j (j ≥ 2) are handled exactly by Σ_I (Ω−ω) ≥ Σ_K (Ω−ω) and
(Ω−2)⁺ ≤ (Ω−ω) + (ω−2)⁺, (Ω−1)⁺ = (Ω−ω) + (ω−1)⁺. Proof of (F): for n with prime set T = A ∪ Q (A ⊆ R, Q ⊆ P∖R),
Σ_{d|n} c_d = Σ_{A'⊆A,|A'|≥2}(−1)^{|A'|} + Σ_{q∈Q} Σ_{∅≠A'⊆A}(−1)^{|A'|+1} = (|A|−1)⁺ + |Q|·[A≠∅] ≤ (|T|−1)⁺. Dropping any whole
q-block preserves (F). With r = 2 and only q ≤ m/2:
   V_2(m,P) = ⌊m/6⌋ + Σ_{q∈P, 5≤q≤m/2} (⌊m/2q⌋ + ⌊m/3q⌋ − ⌊m/6q⌋ − 1)      (requires 2,3 ∈ P; otherwise use the two smallest primes of P).
Numerics for P = all primes ≤ m: V_2 = 800 vs W = 321 (m=10³); 10605 vs 5582 (10⁴); 125331 vs 76102 (10⁵). Heuristically
V_2 ≈ (2/3)m(ln ln m + 0.26) − π(m/2) and W ≈ m(ln ln m − 1.74), so V_2 ≥ W up to m ≈ 10^48 but not beyond; larger r is worse
(each q costs 2^{r−1}−1 for the negative terms). The LP optimum exceeds V_2 (e.g. 907 vs 800 at m = 1000); whether it stays ≥ W
for ALL m is the question.

## Routes that are DEAD (one line each; all used only the lower bound N_I(d) ≥ ⌊m/d⌋)
D1 weight-free injections k ↦ b with (k/p) | b (Hall fails on dense windows). D2 single-threshold level-set domination (fails at
τ = 1, 1/2). D3 #{n≤L: ω_Q ≥ 2} ≤ #{window: ω_Q ≥ 1} (fails). D4 same-threshold sum domination (fails). D7 the Laplace/exponential
form s Σ_J s^w ≤ Σ_{[1,L]} s^w (fails at L = 10⁶). D8 one global forest serving every k individually (averaging kills it — but note:
a forest as a CERTIFICATE only needs total weight Σ_{pq∈F}⌊m/pq⌋ ≥ W, a much weaker condition; the star from 2 gives ≈ (m/2)ln ln m).

## Targets, in order of value (prove-or-refute, equal rank)
T1 Explicit certificates for ALL weights z ∈ [0,1]^P and all m: c = c(m,z) with (F) and V(c) ≥ W(m,z) (⇒ (TH) ⇒ g(n) ≤ 18n).
   Natural ansatz: c supported on d = p^j and on d = q·∏A' with A' ⊆ {2,3} (or the two heaviest-weight primes), coefficients
   depending on z through the hinge; verify (F) on all valuation patterns; compute V.
T2 Explicit certificates for 0/1 weights, all P and all m (⇒ the 0/1 hinge inequality for all m).
T3 A rigorous proof that V_2(m,P) ≥ W(m,P) for all P ⊆ primes ≤ m and all m ≤ 10^40, with explicit constants (Rosser–Schoenfeld /
   Mertens with error terms), or the exact range where it holds.
T4 Refutation of the counting route: an explicit (m, z) and an explicit abstract multiset of valuation types satisfying all
   ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1 with Σ_t n_t (w(t)−1)⁺ < W(m,z) (this would show counting alone cannot prove (TH) for that (m,z)).
T5 A certificate for (TH_c): Σ_{k≤m}(w(k)−c)⁺ ≤ Σ_I (w(b)−1)⁺ with an explicit absolute c > 2 for all m (⇒ g(n) ≤ (c+16)n) —
   here W is replaced by Σ_K (w−c)⁺, which is much smaller, so C_2-type certificates may already suffice for all m: check.
Rule: no intermediate statement may be used as a lemma or proposed as a target until an adversarial agent has tried to break it —
for certificates that means checking (F) on adversarial valuation patterns (many primes, high powers) and computing V exactly.

## Tools (paste into your sandbox)
# types LP for general weights (m ≤ ~150, ≤ 6 primes) — returns LP minimum and the dual certificate
import itertools, math, numpy as np
from scipy.optimize import linprog
def cert(m, P, Z):
    E=[int(math.log(m,p))+1 for p in P]; types=list(itertools.product(*[range(e+1) for e in E])); T=len(types)
    w=lambda t: sum(z*a for z,a in zip(Z,t)); dval=lambda d: math.prod(p**a for p,a in zip(P,d))
    A=np.array([[1.0 if all(a<=b for a,b in zip(d,t)) else 0.0 for t in types] for d in types]); q=np.array([m//dval(d) for d in types],float)
    i1=types.index(tuple([0]*len(P))); Aub=np.vstack([-A,A]); bub=np.concatenate([-q,q+1]); bub[T+i1]=m
    c=np.array([max(0.0,w(t)-1.0) for t in types]); res=linprog(c,A_ub=Aub,b_ub=bub,bounds=[(0,None)]*T,method='highs')
    duals=-res.ineqlin.marginals; return res.fun, [(types[j],dval(types[j]),duals[j],duals[T+j]) for j in range(T) if duals[j]>1e-9 or duals[T+j]>1e-9]
# W(m,z): sum over k<=m of (w(k)-2)^+ with exact valuations.

## Current task statement
Give a rigorous standalone proof using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; every claimed
lemma carries a status tag PROVED / CONDITIONAL (on what) / CONJECTURED, and the answer ends with a dependency list
"final claim ← lemmas ← unproved items". Partial progress counts only if it implies exactly one of T1–T5.
Use multiagents aggressively and dynamically: (i) certificate construction for fractional z (T1) — start from the 0/1 family and
the LP-found certificates at m ≤ 100, guess the z-dependence, verify (F) by exhaustive checks over valuation patterns;
(ii) T2/T3 with explicit Mertens-type estimates; (iii) T4 — an adversarial team trying to build abstract multisets that beat W
(this is a finite LP; if the LP optimum drops below W for some m, report the instance); (iv) T5. Adversarial agents check (F) on
patterns with many primes and high prime powers, and recompute every V. Budget: about two hours; then return the strongest
rigorously proved derivation with its exact gap (do not fail silently).

## Output contract
Numbered lemmas with status tags; every constant explicit; every finite computation stated so it can be re-run; what a Lean
formalisation needs. A check that cannot fail counts as no check.
