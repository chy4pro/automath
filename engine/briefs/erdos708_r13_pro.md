# ATTACK — Erdős Problem #708, round 13: charge ALL high points — the sparse core for every m (TEMPLATE v2.3, prove-or-refute)

## The statement (the last gap to a linear bound for all n)
Atoms p^j ≤ m/64 with weights α_{p,j} ≥ 0, Σ_j α_{p,j} ≤ 1; S₀(n) = Σ α_{p,j} 1[p^j | n]; m > 4096; mean H = Σ α_{p,j}/p^j < 17/16.
K = {1,…,m}, I = {x+1,…,x+m}; L := Σ_{k≤m}(S₀(k) − 64)⁺, R := Σ_{b∈I}(S₀(b) − 1)⁺.
   (SC_64)   L ≤ R for every x ≥ 0.
PROVED (refereed, published v10): (SC_64) for 4096 < m ≤ 10^2887 ⇒ g(n) ≤ 81n for all n ≤ 10^962. (SC_64) for ALL m would give g(n) ≤ 81n for all n.

## What is PROVED (use freely)
S1 Counting certificates: (F) Σ_{d|n} c_d ≤ (S₀(n)−1)⁺ ∀n ⇒ R ≥ Σ_{c>0} c_d ⌊m/d⌋ − Σ_{c<0}|c_d|(⌊m/d⌋+1). Nonnegative certificates pay nothing extra.
S2 Moment bound: L ≤ Σ_K e₆₅((a_p(k))_p) ≤ mH^65/65! < 6.24·10^−90 m, where a_p(k) = Σ_{p^j|k} α_{p,j} ∈ [0,1]; more generally Σ_K e_ℓ ≤ mH^ℓ/ℓ!.
S3 Vacuity: L = 0 unless m ≥ P₆₅ = ∏_{i≤65} p_i = 6.108·10^127.
S4 SHADOW THEOREM (round 12): if S₀(k) > 64, pack the a_p(k) into 32 groups of mass in (4/3, 2] (packing lemma: pair items > 2/3, greedy for the
   rest), D_r := ∏_{p∈G_r} q_p with q_p the largest active power of p at k; the D_r are pairwise coprime, ∏ D_r | k, D_r ≥ 6; the certificate
   c_{D_r} = 1/3 is (F)-feasible (t of the D_r divide n ⇒ S₀(n) > 4t/3 ⇒ (S₀(n)−1)⁺ > t/3); hence R ≥ (1/3)Σ_r ⌊m/D_r⌋ ≥ (32/3)(1−6^−31) m/k^{1/32}.
   With S2 this gives (SC_64) for m ≤ 10^2887.45 (exact). The referee's ceiling analysis: level-ℓ subset certificates over N groups of mass > β
   (coefficient (Nβ−1)/C(N,ℓ)) have value ≥ (Nβ−1) m k^{−ℓ/N}; the exponent ℓ/N is minimised at N/ℓ ≈ 32.5 (65 equal masses, all C(65,2) pairs with
   coefficient 2/65 give R ≥ 64(1−ε) m k^{−2/65}); so ONE high point can never give more than R ≳ 64 m^{1−2/65}, i.e. (SC_64) up to ≈ 10^2958.
   Since L can be of order 10^−90 m, single-high-point charging cannot reach all m.
S5 Multiples-only charging fails: charging each high point k only to the multiples of k in I overloads a single b ∈ I by an unbounded factor on
   an explicit residue-defined window (all high points k_t = a·t, t ≤ M, share the unique multiple B; S₀(B) = 65); that window is NOT an (SC_64)
   counterexample (its R/L ≥ 64(M+1)^63) — the shadows of the D_r (divisors of k, not k itself) are what must be charged.
S6 Abstract two-sided counting alone cannot give any absolute threshold (projective-plane configurations); the arithmetic of ⌊m/d⌋ must be used.
S7 A single ordering sliding-window certificate is nonnegative and (F)-feasible (runs of active atoms); dead routes: positive level-set combos,
   Bernoulli rounding, fixed-degree pointwise polynomials, (RP_64), Hall-type 'transport' (a strengthening, not a reduction).

## Coordinator's analysis — what a proof for all m must do
A1 L counts (with weight) the high points k; R must be bounded below by a certificate built from ALL of them. The natural object: the family
   𝒟 of all 'shadow moduli' D (products of active prime powers of some high point with group mass > 4/3, or more generally any modulus D with
   Σ_{p^j | D} α_{p,j} > 4/3 built from atoms). The certificate c_D = 1/3 on a SUBFAMILY of 𝒟 is feasible iff for every n the number t(n) of
   chosen D dividing n satisfies t(n)/3 ≤ (S₀(n) − 1)⁺ — true when the chosen D's dividing n use disjoint primes (then S₀(n) > 4t/3), FALSE
   when they overlap (two D's sharing primes can divide n with S₀(n) < 4t/3 + …). So the problem is a packing problem: choose a subfamily of
   shadow moduli, pairwise coprime OR with overlaps paid for by smaller coefficients, whose value Σ c_D ⌊m/D⌋ dominates L. This is an
   LP: maximise Σ_D c_D ⌊m/D⌋ subject to (F). Its optimum is at least the single-point value; the question is whether it is ≥ L for all m.
A2 Averaging idea: for each high point k choose the 32 groups RANDOMLY (many valid packings), and average the certificates over k and over
   packings with weight (S₀(k) − 64)⁺/L; the averaged certificate is still feasible (convexity of feasibility) and its value is the average
   of the single-point values, each ≥ C_* m/k^{1/32} ≥ C_* m^{31/32}. That gives R ≥ C_* m^{31/32} again — no gain, because averaging
   certificates averages values. To gain, one must SUM (not average) over high points, which requires the shadows of different high points to
   be 'almost disjoint' as divisor systems — quantify: two high points k, k' with S₀ > 64 share at most how many groups? If the atoms at k and
   k' overlap in mass < 4/3 per group... Try: choose the groups by a fixed global rule (e.g. by prime size bands), so that the D_r of different
   high points are either equal or coprime; then the certificate c_D = 1/3 on the SET of distinct shadow moduli is feasible as long as
   distinct moduli dividing the same n use disjoint prime bands — which a band rule guarantees. The value is then (1/3) Σ_{distinct D} ⌊m/D⌋, and
   L ≤ Σ_{high k} S₀(k) ≤ Σ over bands … — compare the number of distinct shadow moduli with the number of high points weighted by their mass.
A3 Alternatively raise the threshold: (TH_C) for all m with C = C(m) = o(ln ln m) would already improve the published O(n ln ln n) bound
   (C ≈ √(ln m/ln ln m) is known from S4 with general C). Any C = (ln ln m)^{1−δ} is progress.

## Targets (equal rank; prove-or-refute)
T1 PROVE (SC_64) (or (SC_r) for some absolute r) for ALL m by a certificate built from all high points (band rule of A2, or an LP argument
   with an explicit dual solution), hence g(n) ≤ 81n for all n. Full proof, every constant.
T2 PROVE the fractional analogue of the all-pairs certificate (65 groups of mass in (64/65, 1], all C(65,2) pair products, coefficient 2/65)
   for UNEQUAL masses, giving R ≥ 64(1−ε) m/k^{2/65} and (SC_64) up to 10^2957 (a concrete, checkable improvement).
T3 REFUTE: an explicit family of atom systems and residue-defined windows, one for each m in an infinite sequence beyond 10^2958, for which EVERY
   nonnegative certificate supported on divisors of high points has value ≤ L − 1 (this would show the shadow method cannot close (SC_64)
   and identify what else is needed); or an actual counterexample to (SC_64) (proof, not numbers).
T4 PROVE (TH_C) for all m with C(m) = o(ln ln m) (e.g. (ln ln m)^{1/2}) by combining S4 with the moment bound at a growing threshold, with all
   constants explicit — this improves the published O(n ln ln n) to O(n·C(8n³)).
Rule: no intermediate statement is used before an adversarial agent has tried to break it on residue-defined windows AND on abstract
multisets; status tags PROVED / CONDITIONAL / CONJECTURED; end with 'final claim ← lemmas ← unproved items'. Do NOT re-derive S1–S7.

## Current task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web, connected
sources, previous conversations or project contexts. Do not answer that the statement is open. Work iteratively; use multiagents
aggressively: (i) band-rule / multi-point certificate team (A2, T1); (ii) unequal-mass pair certificate team (T2); (iii) adversary team (T3);
(iv) threshold-growth team (T4); (v) referee team checking every constant. Budget: about two hours; then return the strongest rigorously
proved statement with its exact gap.

## Output contract
Numbered lemmas with status tags; every constant explicit; every construction explicit enough to be re-run; what a Lean formalisation needs.
A check that cannot fail counts as no check.
