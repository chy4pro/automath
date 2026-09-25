# ATTACK — Erdős Problem #708, round 12: the sparse core needs ARITHMETIC — use the residue structure of the window (TEMPLATE v2.3, prove-or-refute)

## The statement (only the sparse core is left)
Atoms: prime powers d = p^j with weights α_{p,j} ≥ 0, Σ_j α_{p,j} ≤ 1, supported on p^j ≤ m/64; S₀(n) := Σ α_{p,j} 1[p^j | n]; m > 4096;
mean H := Σ α_{p,j}/p^j < 17/16. Window I = {x+1,…,x+m}, K = {1,…,m}.
   (SC_64)   Σ_{k≤m} (S₀(k) − 64)⁺ ≤ Σ_{b∈I} (S₀(b) − 1)⁺   for every x ≥ 0.
PROVED (this week, refereed, published as v9): (SC_64) ⇒ fractional (TH_65) ⇒ g(n) ≤ 81n for the Erdős–Surányi function (the first linear
bound). Dense branch H ≥ 17/16 is done. So (SC_64) is exactly what stands between us and a linear bound.

## What is PROVED about the sparse core (use freely)
S1 Vacuity: S₀ ≤ ω, so the left side is 0 unless some k ≤ m has ω(k) ≥ 65, i.e. unless m ≥ P₆₅ := ∏_{i≤65} p_i ≈ 6.1·10^127.
S2 Left side is tiny: Σ_{k≤m} e_ℓ((a_p(k))_p) ≤ m e_ℓ((h_p)_p) ≤ mH^ℓ/ℓ! (a_p = per-prime atom mass at k, h_p = per-prime harmonic mass), and
   (t − C)⁺ ≤ e_{C+1} of summands in [0,1]; hence L := Σ_K (S₀ − 64)⁺ ≤ mH^65/65! < 6.24·10^−90 m.
S3 One high point forces the right side: if S₀(k) > 64 for some k ≤ m then I contains a multiple b of k with S₀(b) ≥ S₀(k), so R := Σ_I(S₀−1)⁺ > 63.
S4 Two-sided counting alone is insufficient: projective-plane configurations (order q, m = q(q²+q+1)+1) satisfy 0 ≤ N_ν(A) − N_μ(A) ≤ 1 for all
   nonempty atom sets A yet beat every threshold ≤ q (q = 67 beats 64). They are excluded by the true table only at first order (at most q−1
   moduli have ⌊m/d⌋ = q+1, but q²+q+1 atoms with that count would be needed). So a proof MUST use the values ⌊m/d⌋ and/or the residue structure.
S5 Counting certificates (F) Σ_{d|n} c_d ≤ (S₀(n)−1)⁺ with value Σ_{c>0} c_d⌊m/d⌋ − Σ_{c<0}|c_d|(⌊m/d⌋+1) remain valid tools; the affine one gives
   R ≥ Σ_K S₀ − m (negative in the sparse core); the sliding-window one (nonnegative, feasible) gives R ≥ Σ_K Σ_runs(ℓ−1)⁺ for any fixed atom order.
S6 Hinge sums are NOT monotone under N_I(d) ≥ N_K(d) (m = 11021, P = {101,103,107}: Σ_K(ω_P−1)⁺ = 3 > 2 = Σ_I(ω_P−1)⁺ for I centred at 101·103·107).
S7 Dead: positive-coefficient level-set combinations; '0/1 vertices ⇒ cube'; Bernoulli rounding; positive pair terms at low mass; fixed-degree
   pointwise polynomial certificates; the random-partition condition (RP_64); Hall-type transport as a 'reduction' (it is a strengthening).

## Coordinator's analysis — the arithmetic input that is available and unused
A1 The window is determined by ONE integer x: N_I(d) = ⌊m/d⌋ + [x mod d ∈ some set of (m mod d) residues]. The abstract adversary of S4 chooses
   the ±1 deficits independently for every modulus; a real window cannot — the deficits are functions of the single residue vector (x mod d)_d,
   coupled by CRT. Quantify this: for pairwise coprime moduli the residues are independent only when d ranges over a set whose product is ≤ m;
   for products > m they are constrained (there are only m windows of length m in each block of length lcm).
A2 By S2–S3 a counterexample needs L > R > 63 with L ≤ 6.24·10^−90 m, i.e. m ≥ 10^91 and a window that is simultaneously deficient (by 1) on
   astronomically many moduli in a way that suppresses every integer of large S₀. Turn S3 into a counting argument: each k ≤ m with S₀(k) > 64
   has ⌊m/k⌋ ≥ 1 multiples in I, each with S₀ ≥ S₀(k); different k's can share a multiple b, but then b is divisible by lcm of them, and the
   number of k ≤ m with S₀(k) > 64 dividing a given b is bounded by the number of divisors of b that are ≤ m and have ≥ 65 prime factors — relate
   this to (S₀(b) − 1)⁺ (which is ≥ S₀(b) − 1 ≥ 64·(something)). Goal: R ≥ Σ_{k: S₀(k)>64} (S₀(k) − 64)⁺ / M where M bounds the multiplicity, then
   show M ≤ 1 + (S₀(b) − 65)·(…): i.e. prove a 'multiplicity-weighted' version of S3: Σ_{b∈I} (S₀(b)−1)⁺ ≥ Σ_{k≤m} (S₀(k)−64)⁺ by charging each k to
   its multiples in I with weights ⌊m/k⌋^{-1} and bounding the total charge received by b by (S₀(b) − 1)⁺. This is a purely arithmetic
   double-counting: prove it or find where it fails.
A3 Alternative: the 0/1-style cube-root split inside the sparse core. Atoms with p ≤ m^{1/3} vs larger: at most 2 large distinct primes divide
   any k ≤ m (peel costs 2 in the threshold); for the small ones use the sliding-window certificate ordered by p, whose runs are long exactly
   when many consecutive small primes divide n — and n ≤ m with ≥ 65 small prime factors are astronomically rare; compare run structure on I
   vs K using that consecutive small primes' residues are CRT-independent while their product is ≤ m.

## Targets (equal rank; prove-or-refute)
T1 PROVE (SC_64) (or (SC_r) for any absolute r, with the matching dense branch) — a linear bound follows. Route A2 first: the multiplicity-weighted
   charging argument is elementary; if it works it is a two-page proof.
T2 PROVE the charging inequality of A2 in the 0/1 case (all α = 1 on a prime set), i.e. Σ_I (ω_P(b)−1)⁺ ≥ Σ_K (ω_P(k) − C)⁺ by charging for some
   absolute C — even though the 0/1 case is known, a proof by charging would immediately generalise.
T3 REFUTE: an explicit window x (residue conditions) for which the charging argument of A2 fails by an unbounded factor — i.e. many k with
   S₀(k) > 64 all mapping to few b's — and, if possible, an actual counterexample to (SC_64) for some astronomically large m given by congruence
   conditions on x (we cannot compute at that size, so give a proof, not numbers).
T4 A different arithmetic argument (CRT independence of residues for moduli with product ≤ m; Hensley–Richards-type constructions as the extremal
   windows; the Erdős–Surányi original argument for g(3) = 4) that proves (SC_r) for some absolute r.
Rule: no intermediate statement is used before an adversarial agent has tried to break it on abstract multisets AND on residue-defined windows;
status tags PROVED / CONDITIONAL / CONJECTURED; end with 'final claim ← lemmas ← unproved items'. Do NOT re-derive S1–S7.

## Current task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; use multiagents
aggressively: (i) charging team (A2); (ii) CRT/residue team (A1, A3, T4); (iii) adversary team (T3); (iv) referee team. Budget: about two
hours; then return the strongest rigorously proved statement with its exact gap.

## Output contract
Numbered lemmas with status tags; every constant explicit; every construction explicit enough to be re-run; what a Lean formalisation needs.
A check that cannot fail counts as no check.
