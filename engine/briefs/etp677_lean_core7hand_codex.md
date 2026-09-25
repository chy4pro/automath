# CODEX TICKET (Lean 4; sol tier) — CLEAN-TIER fibre-3 exclusion: formalise the human proof of
# problems/etp677/simple/fibre_core/handproof/proof.md (registry R46 STEP 58) and re-derive
# `fibre3_exclusion` WITHOUT bv_decide / native_decide / any certificate axiom.
# Repo: $HOME/workspace/claudecode/automath; project lean/etp677_ext. Existing pieces to
# REUSE: Ext677Core7Free.lean — `Core7Pair`, `core7Chains` (the seven lifted chains as a Prop on
# σ : Core7Pair → Fin3 → Equiv.Perm Fin3), `core7_pattern_chains` (the semantic bridge, clean),
# and the transport/lifting proof of `fibre3_exclusion` (only its call to
# `core7_free_three_no_semantic` must be replaced). 0 sorry; `#print axioms` for the new
# `core7_chains_no_solution` and the new `fibre3_exclusion_clean` must be exactly
# [propext, Classical.choice, Quot.sound]; append to AXIOMS.txt. Heavy ≤ 2 (lake build).
# DONE marker: DONE-LEANC7H.

## The proof to formalise (all verified by line-677; notation of proof.md)
Operations A..N as in proof.md §1 (fourteen `Fin3 → Perm Fin3`); chain E(P,Q,R,Z) :=
∀ s t, P t (Q s (Z (R t s) t)) = s. The seven chains: E(A,B,C,D), E(E,F,G,H), E(I,J,K,L),
E(D,M,D,N), E(F,K,F,I), E(H,L,A,B), E(K,I,L,E). Prove False from all seven:
1. Lemma (5): from E(X,Y,X,Z): ∀ s t, Z (X t s) t = (Y s)⁻¹ ((X t)⁻¹ s)   [two `Equiv` cancels].
2. BRIDGE LEMMA (the only finite part): from E(F,K,F,I), E(I,J,K,L), E(K,I,L,E), E(E,F,G,H)
   derive ∃ ℓ, (∀ s, L s = ℓ) ∧ (∀ s, H s = ℓ⁻¹). Recommended formalisation: prove it as a
   decidable statement over the FINITE data — the collision E(F,K,F,I) has exactly 252
   solutions (X,Y,Z) ∈ (Fin3 → Perm Fin3)³ (Perm Fin3 has 6 elements, so 6^9 raw triples; use
   lemma (5) to make Z a function of (X,Y): 6^6 = 46,656 pairs — `decide` over 46,656 cases
   with the row-permutation check is likely too slow for the kernel; instead FIRST normalise
   by the gauge (7): prove that any solution is conjugate (by three permutations τ_v, τ_b, τ_c
   acting as in proof.md (7)) to one of the FIVE representatives (types 0–4), then prove the
   bridge conclusion for each representative by `decide`/`fin_cases` over the remaining free
   operations (≤ 6³ each; the statement per type is "for all L E G with the three chains,
   L const ∧ H = L⁻¹" or "no such L,E" for types 0,1,3,4). The gauge lemma itself: the map
   (X,Y,Z) ↦ (τ_b⁻¹ ∘ X_{τ_v s} ∘ τ_b, τ_b⁻¹ ∘ Y_{τ_b s} ∘ τ_c, τ_c⁻¹ ∘ Z_{τ_b s} ∘ τ_v) preserves
   E(X,Y,X,Z) (symbolic), and orbit-representative selection is a `decide` over 46,656 (X,Y)
   pairs computing a canonical form — if that is too heavy, the fallback is the unnormalised
   `decide` over all (X,Y) with Z computed by (5) (46,656 cases, each with ~3 chain checks);
   try `decide` with `Decidable` instances on `Fin 3 → Equiv.Perm (Fin 3)` via
   `Fintype`/`DecidableEq` — measure and report the elaboration time; if the kernel cannot do
   it, use `Nat.rec`-style computation with `by decide` on a Bool-valued function over
   `List (Fin 3 → Fin 3 → Fin 3)` (216 × 216 = 46,656 pairs is small for `Nat`-level
   evaluation in the kernel if written as a tail-recursive Bool fold — `decide` on
   `bridgeCheck = true` where `bridgeCheck` iterates over all pairs; avoid `native_decide`).
3. Cancellation endgame (symbolic): E(H,L,A,B) + bridge ⟹ ∀ s t, B (A t s) t = s ⟹ B s t =
   (A t)⁻¹ s; E(A,B,C,D) ⟹ D (C t s) t = t ⟹ ∀ r t, D r t = t (surjectivity of C t);
   E(D,M,D,N) ⟹ ∀ s t, M s (N s t) = s ⟹ False (t ↦ M s (N s t) is injective, Fin 3 has ≥ 2
   elements).
4. Wire it: `core7_chains_no_solution : ¬ ∃ σ, core7Chains σ` (matching Ext677Core7Free's
   `core7Chains`), then `fibre3_exclusion_clean` by the existing transport proof, and
   `fibre_two_or_three_exclusion_clean`; leave the bv_decide versions in place (do not delete).

## Deliverables
lean/etp677_ext/Ext677Core7Hand.lean, AXIOMS.txt appended (the two new theorems must be clean),
engine/out/codex/etp677_lean_core7hand_report.md (elaboration times of the finite lemma, which
route worked) ending with DONE-LEANC7H.
