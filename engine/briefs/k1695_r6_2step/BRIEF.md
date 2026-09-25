# K6-2STEP — break or prove the surviving hill-climbing conjecture (2Step) for Kourovka 16.95

## Setting
F a field, B ∈ GL(n,F). Column transpositions act by B ↦ B P_τ (P_τ swaps two columns). For a standard
basis vector e_i let kd(B, i) := rank [e_i, B e_i, B² e_i, …, B^{n−1} e_i] (Krylov dimension). B is
cyclic (nonderogatory: minpoly = charpoly) iff some vector is Krylov-cyclic; kd(B, i) = n says e_i is one.
Kourovka 16.95 (open): for every A ∈ GL(n,F) some A P_σ (σ ∈ S_n) is cyclic. Known: n ≤ 3 all fields;
n = 4 partially; exhaustive on GL(5,2), GL(4,3), GL(4,4).
A pair (B, i) with kd(B, i) < n is a **kd-local maximum** if no transposition τ has kd(BP_τ, i) > kd(B, i).
A transposition τ is **neutral** at (B, i) if kd(BP_τ, i) = kd(B, i).

## What is known (all verified by exhaustive computation with our own code)
* On GL(3,4), GL(4,2), GL(3,5), GL(5,2) and four more small cells, from EVERY kd-local maximum (B, i) some
  neutral τ followed by some τ′ gives kd(BP_τP_τ′, i) > kd(B, i) ("one neutral step, then ascent").
* The potential Φ′ = (kd, −ν) with ν = number of neutral transpositions was conjectured to have no local
  maxima below kd = n ("(Mono)": from every kd-local maximum some neutral step lowers ν). **This is FALSE
  at n = 6 over F₂** (found today by construction): M with rows 000100 / 100000 / 111101 / 001000 /
  101110 / 000001 and i = 1: kd = 5 is a kd-local maximum, ν = 3 (neutral: (1,5), (2,5), (3,5)), and after
  each neutral move ν = 8, 4, 4 — no decrease. But the two-step ascent exists: kd(M P_(15) P_(16), 1) = 6.
* Random sampling over GF(2) at n = 6, 7 finds almost no kd-local maxima at all (1 in 5871 invertible
  matrices at n = 6, none in 1781 at n = 7); local maxima concentrate in structured families
  (rank-one perturbations of permutation matrices, Q + J with J the all-ones matrix, monomial-like).
* Useful tool ("Lemma T", proved): P_τ = I − ddᵀ with d = e_a − e_b, so BP_τ − μI = (B − μI) − (Bd)dᵀ is a
  rank-one update; kd(BP_τ, i) can be analysed through the Krylov space K = span(e_i, Be_i, …) — in the
  top layer kd = n − 1, K is a B-invariant hyperplane and BP_τ = B − (Bd)dᵀ.

## Conjecture (2Step)
For every field F, every B ∈ GL(n,F) and every i with kd(B, i) < n: if (B, i) is a kd-local maximum then
there are transpositions τ (neutral) and τ′ with kd(BP_τP_τ′, i) > kd(B, i).
(2Step) implies by iteration that from any (A, i) a sequence of ≤ 2-step ascents reaches kd = n, i.e.
e_i becomes a Krylov-cyclic vector of some AP_σ — which implies 16.95.

## Tasks (mark every statement PROVED / CONJECTURED / COMPUTED / FAILED; use your sandbox)
1. BREAK IT: search for a kd-local maximum (B, i) with NO neutral-then-ascent path — n ≤ 7 over F₂, F₃,
   F₄ (and n = 8 over F₂ if feasible), exhaustively where possible and otherwise over the structured
   families above plus the neighbourhood of the matrix M (all B P_ρ, ρ ∈ S₆, and all rank-one changes of
   one column). Also test the stronger variants: (2Step′) the ascent must exist after EVERY neutral move
   (false? — check on M), and (kStep) with k = 3 if (2Step) fails. Ship the matrix, the index, the full
   transposition profile, and an exact self-contained verifier (as you did for M).
2. If nothing breaks it: prove (2Step) in the top layer kd = n − 1 over an arbitrary field, or isolate the
   exact obstruction (which configurations of the invariant hyperplane K, the vector d = e_a − e_b and
   Bd make every neutral move a dead end). Partial credit: characteristic 2; or n ≤ 5 by a uniform argument.
3. Is there ANY potential function of (B, i) (computable from kd-profiles of radius ≤ 2) with no local
   maxima below kd = n on all your data? Propose one only with evidence from your own exhaustive runs.
Web use only for literature (cite DOIs). Do not assume 16.95; do not restrict to n-cycles.
