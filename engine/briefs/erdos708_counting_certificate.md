# COUNTING CERTIFICATES for the hinge inequality — dialogue's finding (09-04 12:xx CDT), to be handed to the engines

## The principle (PROVED)
Every interval I of length m satisfies, for every integer d ≥ 1,  ⌊m/d⌋ ≤ N_I(d) := #{b ∈ I : d | b} ≤ ⌊m/d⌋ + 1.
Suppose real coefficients c_d (finitely many nonzero, d ranging over products of prime powers of the weighted primes) satisfy
   (F)  Σ_{d | t} c_d ≤ (w(t) − 1)⁺   for every "type" t (every possible valuation pattern; in particular every integer).
Then Σ_{b∈I} (w(b)−1)⁺ ≥ Σ_d c_d N_I(d) ≥ Σ_{c_d>0} c_d ⌊m/d⌋ − Σ_{c_d<0} |c_d| (⌊m/d⌋+1) =: V(c).
Hence (TH) holds for (m, z) and EVERY x as soon as V(c) ≥ Σ_{k≤m} (w(k)−2)⁺.  Only counting is used; no arithmetic of x.
Finding the best c is a linear programme (dual of the "abstract interval" LP: minimise Σ_t n_t (w(t)−1)⁺ over multisets of types
with ⌊m/d⌋ ≤ N(d) ≤ ⌊m/d⌋+1).  Scripts: problems/erdos708/abstract_count_lp2.py (general weights, types = capped exponent vectors),
graph_cert.py (0/1 weights, pairs/triples with constraint generation), cert_family.py (explicit family below).

## Evidence
- General weights (types LP): m ≤ 200, |P| ≤ 7, z ∈ {1, 0.7, 0.4, mixed}: LP min ≥ K-side in every case, e.g. m=100, P ≤ 17:
  114 vs 64 (z ≡ 1), 63.3 vs 22 (z ≡ 0.7), 16.4 vs 0.8 (z ≡ 0.4). So for these (m, P, z) the hinge inequality is PROVED for all x.
- 0/1 weights, P = all primes ≤ m (graph LP, pairs + triples, constraint generation converged): m=300: V* = 223.5 vs W = 59;
  m=500: 407.4 vs 124; m=1000: 907 vs 321 (iteration cap hit — being re-verified). Optimal certificates use edges 2–q, 3–q, 5–q
  with weight 1 and triangle corrections 2·3·q, 2·5·q; typically ≥ 3× margin.

## An explicit certificate family (dual feasibility PROVED)
0/1 weights, prime set P, R := the first r primes of P.  Put c_d = (−1)^{|A'|} for d = ∏A', A' ⊆ R, |A'| ≥ 2, and
c_d = (−1)^{|A'|+1} for d = q·∏A' with q ∈ P∖R and ∅ ≠ A' ⊆ R;  all other c_d = 0.  (Prime powers p^j, j ≥ 2, are handled
exactly by Σ_I (Ω−ω) ≥ Σ_K (Ω−ω).)  For T = A ∪ Q (A ⊆ R, Q ⊆ P∖R) the sum Σ_{d | ∏T} c_d equals (|A|−1)⁺ + |Q|·[A ≠ ∅] ≤ |T| − 1,
so (F) holds; dropping any whole q-block keeps (F).  With r = 2 (R = {2,3}) and only q ≤ m/2:
   V_2 = ⌊m/6⌋ + Σ_{q∈P, 5≤q≤m/2} ( ⌊m/2q⌋ + ⌊m/3q⌋ − ⌊m/6q⌋ − 1 ).
For P = all primes ≤ m: V_2 = 800 vs W = 321 (m = 10^3); 10605 vs 5582 (10^4); 125331 vs 76102 (10^5).  Asymptotically
V_2 ≈ (2/3) m (ln ln m + 0.26) − π(m/2) and W ≈ m (ln ln m − 1.74), so this single certificate proves the 0/1 hinge inequality
(P = all primes ≤ m) for all m up to about e^{110} ≈ 10^{48}; beyond that a better certificate is needed (the LP optimum is
larger than V_2 — the question is whether it stays above W for all m).  Larger r does NOT help (each q costs 2^{r−1}−1 extra).

## What this changes
- The three refutations (weight-free matching, single-threshold level sets, Laplace form) all used only LOWER bounds N_I(d) ≥ ⌊m/d⌋
  (Hall-type transport).  The UPPER bounds N_I(d) ≤ ⌊m/d⌋+1 — which is what defeats the dense Hensley–Richards windows — were
  never used.  With both bounds, LP duality does the "transport" and the hinge inequality follows from pure counting.
- Open combinatorial problems (no sieve theory needed): (a) 0/1: for every prime set P and every m, is max_c V(c) ≥ W(P,m)?
  (b) fractional z: find explicit certificates c_d (the types-LP finds them for small m); a natural ansatz is c supported on
  d = q·∏A' with A' ⊆ {2,3} and coefficient depending on the weights z_2, z_3, z_q through the hinge (w−1)⁺.
