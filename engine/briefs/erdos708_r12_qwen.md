# MICRO-LEMMA — Erdős Problem #708, round 12 (single-shot): the sparse core at a single scale

## Setting (all proved, use freely)
Atoms: a finite set A of prime powers d = p^j with weights α_d ∈ [0,1] (for fixed p the weights α_{p,j} are non-increasing in j and
Σ_j α_{p,j} ≤ 1). S(n) := Σ_{d∈A} α_d 1[d | n]. m ≥ 1, x ≥ 0, I = {x+1,…,x+m}, K = {1,…,m}. Target with an absolute constant C:
   (TH_C)   Σ_{k∈K} (S(k) − C)⁺ ≤ Σ_{b∈I} (S(b) − 1)⁺.
PROVED (counting certificates): if real numbers (c_D), indexed by positive integers D and finitely many nonzero, satisfy (F) Σ_{D|n} c_D ≤ (S(n)−1)⁺
for every n ≥ 1, then Σ_I (S−1)⁺ ≥ V(c) := Σ_{c_D>0} c_D ⌊m/D⌋ − Σ_{c_D<0} |c_D| (⌊m/D⌋+1).
PROVED (affine): c_1 = −1, c_d = α_d gives Σ_I (S−1)⁺ ≥ Σ_K S − m − 1, so (TH_C) holds whenever Σ_K min(S, C) ≥ m + 1.
PROVED (0/1 single scale): for 0/1 weights on primes in (y, y ln y] the odd-depth alternating certificate proves (TH_2) once y is large.
PROVED (sliding window): order the atoms d₁, d₂, … and lay their weights end to end on [0, Z), Z = Σ α_d; for 0 ≤ t ≤ Z − 1 let A_t be the set of
atoms whose segment meets [t, t+1]; c_B := Leb{t : A_t = B} ≥ 0 for B ⊆ A and c_D := Σ_{B : lcm(B) = D} c_B. Then (F) holds, and for n with
active atom set Q(n) the certificate sum equals Leb{t : [t,t+1] ⊆ ∪_{a∈Q(n)} segment(a)} = Σ over maximal runs of active atoms in the order of
(run length − 1)⁺ ≤ (S(n) − 1)⁺.

## Targets, in order of value
T1 SINGLE SCALE: all atoms are primes p ∈ (y, 2y] (j = 1) with arbitrary weights α_p ∈ [0,1], and m ≥ y³. PROVE (TH_C) for an explicit absolute C
   (any C), by an explicit certificate (sliding window in the natural order of the primes, or a better order, or a hybrid with a bounded
   negative part on moduli D ≤ m/64), with every constant explicit and the value computed with ⌊m/D⌋ ≥ m/D − 1. State exactly which
   inequality between Σ_K (S − C)⁺ and the certificate value you prove and under which condition on (y, m, α).
T2 The same with two scales (y₁, 2y₁] and (y₂, 2y₂], y₂ ≥ y₁²: does the certificate cost add or multiply? Give the explicit constant.
T3 Lower bound: an explicit single-scale instance (y, m, α) and an explicit ordering-independent argument showing that every sliding-window
   certificate (any order) has value ≤ Σ_K (S − c)⁺ for some c ≥ 2 — i.e. the smallest threshold the sliding-window family can reach.

## Task statement
Give a rigorous standalone derivation using your own knowledge, computation and reasoning, without searching the public web or other
sources. Every claimed lemma carries a status tag PROVED / CONDITIONAL / CONJECTURED; every constant explicit; every finite computation
stated so it can be re-run. Do not return a heuristic or an explanation of why the problem is hard.
