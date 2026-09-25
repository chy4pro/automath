# Lean/mathlib API notes (accumulated from formalization runs)

From A108211 run (opus agent, 2026-08-17, mathlib v4.34.0-rc1 era):

- mathlib has NO alternating-harmonic-equals-log-2 lemma. Workaround that
  avoids Abel/integrals entirely: paired series f m = 1/((2m+1)(2m+2)) has
  partial sums exactly H_{2n} - H_n (induction); squeeze via
  log x <= x - 1 (Real.log_le_sub_one_of_pos) telescoped:
  log(2n+1) - log(n+1) <= H_{2n} - H_n <= log 2; then
  summable_of_sum_range_le + hasSum_iff_tendsto_nat_of_nonneg.
- Renames: div_lt_div_iff -> div_lt_div_iff₀ (same for le/lt variants).
- Nat.Ico_succ_right gone; convert Icc/Ico via ext + simp.
- positivity reads context hypotheses (have 0 < 4x+1 etc. lets it close
  big products in one call).
- Polynomial positivity certificates: after obtain ⟨t, ht, rfl⟩ (x = 1 + t),
  `linarith [pow_nonneg ht 2, ..., pow_nonneg ht 16]` handles degree-16
  coefficient-nonneg certificates without hand-written expansions.
- Telescoping series: avoid HasSum for the telescope; use partial-sum
  inequalities + le_of_tendsto' / squeeze_zero.
- Useful combo: Summable.sum_add_tsum_nat_add, summable_nat_add_iff,
  Finset.sum_range_sub / sum_range_sub'.
- linarith [cert] beats exact cert for goals from div_lt_div_iff₀
  (immune to assoc differences).
- import Mathlib: ~33 s cold, 3-5 s warm. maxHeartbeats 2000000 set but not
  needed in practice.

From A100434 run (sonnet, 2026-08-16):
- if_pos/if_neg deprecated -> ite_eq_left/ite_eq_right (this mathlib).
- omega natively handles Int /, %, ∣ by literal 2 — prefer over manual
  Int.mul_ediv_cancel lemmas: provide dvd facts + sum/diff identities and
  let omega close.
- Nat.twoStepInduction for 2-periodic recurrences; rewrite LARGER index
  pattern first when two rewrites share subterms.

From A114362 conjecture2 run (opus, 2026-08-16, mathlib v4.34.0-rc1):

## Euler product → real limit (the "hard bridge", solved without tprod)

- `riemannZeta_eulerProduct (hs : 1 < s.re) : Tendsto (fun n : ℕ ↦ ∏ p ∈ Nat.primesBelow n,
  (1 - (p:ℂ)^(-s))⁻¹) atTop (𝓝 (riemannZeta s))` is FAR easier to use than
  `riemannZeta_eulerProduct_tprod` / `_hasProd` (which are indexed by the subtype
  `Nat.Primes`). Working with the `primesBelow` finite-partial-product version means
  ALL infinite-product machinery (Multipliable, tprod over subtypes, tail products)
  can be avoided: everything becomes finite `Finset.prod` + `le_of_tendsto`.
- Transport ℂ → ℝ: for `s = (m:ℕ)` the partial products are real. Recipe that works:
  ```
  have key : ∀ N, ((realProd N : ℝ) : ℂ) = ∏ p ∈ Nat.primesBelow N, (1 - (p:ℂ)^(-(m:ℂ)))⁻¹ := by
    intro N; rw [ofReal_prod]           -- `Complex.ofReal_prod`, needs `open Complex`
    refine Finset.prod_congr rfl fun p _ ↦ ?_
    rw [Complex.cpow_neg, Complex.cpow_natCast]; push_cast; ring
  have h2 : Tendsto (fun N ↦ ((realProd N : ℝ) : ℂ)) atTop (𝓝 (riemannZeta (m:ℂ))) := by
    simpa only [key] using riemannZeta_eulerProduct hs
  have h3 : Tendsto (fun N ↦ (((realProd N : ℝ):ℂ)).re) atTop (𝓝 (riemannZeta (m:ℂ)).re) :=
    (Complex.continuous_re.tendsto _).comp h2
  simpa only [Complex.ofReal_re] using h3
  ```
  Two traps: (a) state `h3` with an explicit `have : Tendsto (fun N ↦ ...re) ...` type
  ascription, otherwise you get `re ∘ f` and `simpa` chokes; (b) finish with
  `simpa only [Complex.ofReal_re]`, NOT plain `simpa` — plain simp rewrites
  `(↑x)⁻¹.re` into `re/normSq` form and breaks the match.
- Corollary trick: `ζ(m).re ≥ 1` for `m ≥ 2` follows from `ge_of_tendsto'` applied to
  the real partial products (each ≥ 1). No need to know ζ is real-valued at all —
  taking `.re` of the (real) partial-product limit is exactly FC's `t n` definition
  `(ζ(2n)).re / ((ζ(n)).re)^2`.
- `ζ(2n)/ζ(n)^2 = ∏_p (1-p^-n)/(1+p^-n)` then comes from
  `Filter.Tendsto.div h2 (h1.pow 2) hne` plus the pointwise identity
  `EP(2n) N / (EP n N)^2 = ∏ q_p`, proved by
  `rw [← Finset.prod_pow, ← Finset.prod_div_distrib]; Finset.prod_congr` + `field_simp`.

## Peeling a finite set of primes out of the limit

- `Finset.prod_sdiff (h : s₁ ⊆ s₂) : (∏ x ∈ s₂ \ s₁, f x) * ∏ x ∈ s₁, f x = ∏ x ∈ s₂, f x`
  is the clean way to split off `{2,3,5,7}`; then `le_of_tendsto` / `ge_of_tendsto`
  with `filter_upwards [eventually_ge_atTop 8]`.
- "prime and ∉ {2,3,5,7} ⇒ ≥ 11": `by_contra; rw [Nat.not_le] at h; interval_cases p <;>
  revert hprime hnotmem <;> decide` — `decide` kills all 11 cases at once.
- `∏ p ∈ ({2,3,5,7} : Finset ℕ), f p`: unfold with
  `rw [show ({2,3,5,7} : Finset ℕ) = insert 2 (insert 3 (insert 5 {7})) from rfl,
      Finset.prod_insert (by decide), ..., Finset.prod_singleton]`.

## Missing-from-mathlib lemmas I had to prove

- `1 - ∑ (1 - f i) ≤ ∏ f i` for `0 ≤ f i ≤ 1` (no mathlib version found).
  `induction s using Finset.cons_induction` with the two hypotheses left as
  arrows in the goal (`(∀ i ∈ s, ...) → ... → ...`) so the motive generalizes;
  step closed by `nlinarith [mul_le_mul_of_nonneg_left ih' hfa0,
  mul_nonneg hs (sub_nonneg.2 hfa1)]`.
- Tail comparison `∑_{k=11}^{N-1} k^{-n} ≤ 12·11^{-n}` (n ≥ 2), FINITE version only —
  no Summable/tsum needed since the index set is always a `Finset.Ico`.
  Route: `∑_{Ico 12 N} k^{-2} ≤ 1/11 - 1/(N-1)` by `Nat.le_induction` +
  `Finset.sum_Ico_succ_top`; then for `n = m+2` and `k ≥ 12`,
  `k^{-(m+2)} ≤ (121/11^(m+2))·k^{-2}` via `pow_le_pow_left₀ : 11^m ≤ k^m`.
  Split the `k = 11` term with `Finset.sum_eq_sum_Ico_succ_bot`.

## Renames / gotchas hit this run (mathlib v4.34.0-rc1)

- `div_le_div_iff` → `div_le_div_iff₀ (0 < b) (0 < d) : a/b ≤ c/d ↔ a*d ≤ c*b`.
- `one_lt_pow` → `one_lt_pow₀ (h : 1 < a) (hn : n ≠ 0)`.
- `pow_le_pow_left` → `pow_le_pow_left₀ (0 ≤ a) (a ≤ b) (n)`.
- `le_inv_comm₀ (0 < a) (0 < b) : a ≤ b⁻¹ ↔ b ≤ a⁻¹` (for `1 ≤ (1-x)⁻¹`).
- `div_div_div_cancel_right₀ (hc : c ≠ 0) (a b) : a/c/(b/c) = a/b` — pass the
  `≠ 0` proof explicitly or `rw` leaves a stray `case hc` goal.
- `push_neg` is deprecated (warning) → `rw [Nat.not_le] at h` or `push Not at h`.
- `rw [e12, e30, e420] at h` ORDER MATTERS when one LHS is a subterm of another:
  rewrite the LARGEST pattern first (`e420` before `e12`) — same lesson as
  A100434's "rewrite the larger index pattern first".
- `1/u^n * (1/v^n) = 1/(u*v)^n` is a pure identity: `rw [mul_pow, div_mul_div_comm, one_mul]`
  (no positivity hypotheses). Much more robust than chains of `← mul_pow`, which
  fail on `(u^n)^2`; insert `pow_two` first if a square is present.
- `Complex.ofReal_prod` is available as `ofReal_prod` under `open Complex`;
  `RCLike.ofReal_prod` does NOT rewrite (K stays a metavariable).
- Sanity anchor for zeta values: `riemannZeta_two : riemannZeta 2 = (π:ℂ)^2/6`,
  `riemannZeta_four : riemannZeta 4 = (π:ℂ)^4/90`; take `.re` via
  `rw [riemannZeta_two, show ((π:ℂ))^2/6 = ((π^2/6 : ℝ) : ℂ) by push_cast; ring,
  Complex.ofReal_re]`. Gives `t 2 = 2/5` as a non-vacuity check.

From Fernandes conjecture_1 run (opus, 2026-08-16, mathlib v4.34.0-rc1):
`lean/proofenv/Fernandes.lean`, 490 lines, 5 s warm, 0 warnings,
axioms = [propext, Classical.choice, Quot.sound] only.

## Group-theory entry points that carried the whole proof

- **Goursat is in mathlib**: `Mathlib/GroupTheory/Goursat.lean`.
  `I.goursatFst : Subgroup G` = `{g | (g,1) ∈ I}` with
  `Subgroup.mem_goursatFst : g ∈ I.goursatFst ↔ (g, 1) ∈ I` (and `…Snd`),
  `Subgroup.normal_goursatFst (hI₁ : Surjective (Prod.fst ∘ ⇑I.subtype)) : I.goursatFst.Normal`.
  The *isomorphism* part (`goursat_surjective`) was NOT needed: everything the paper does
  with "the common quotient Q" can be done with the two kernels alone.
- **`Equiv.Perm.alternatingGroup_le_of_normal (hα : 5 ≤ Nat.card α) {N : Subgroup (Perm α)}
  [N.Normal] (ntN : Nontrivial N) : alternatingGroup α ≤ N`**
  (`Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.lean`) — this single lemma replaces
  the paper's Lemma 4.1 (centraliser of A_r trivial) + Prop 4.3 (classification of normal
  subgroups of S_r). Also there: `alternatingGroup.isSimpleGroup (5 ≤ Nat.card α)` (general n,
  not just A₅) and `alternatingGroup.normal_subgroup_eq_bot_or_eq_top`.
  `Nontrivial ↥N` from `N ≠ ⊥`: `(Subgroup.nontrivial_iff_ne_bot _).2` — H is EXPLICIT, so
  `Subgroup.nontrivial_iff_ne_bot.2` fails with "invalid projection".
- **`Equiv.Perm.closure_cycle_adjacent_swap (h1 : IsCycle σ) (h2 : σ.support = univ) (x) :
  closure {σ, swap x (σ x)} = ⊤`** (`Mathlib/GroupTheory/Perm/Closure.lean`).
- `finRotate` toolkit (`Mathlib/GroupTheory/Perm/Fin.lean`, `Mathlib/Logic/Equiv/Fin/Rotate.lean`):
  `isCycle_finRotate` / `_of_le`, `support_finRotate : support (finRotate (n+2)) = univ`,
  `sign_finRotate (n) : sign (finRotate n) = (-1)^(n-1)` (ROOT namespace — `_root_.sign_finRotate`,
  `Equiv.Perm.sign_finRotate` does not exist), `finRotate_apply : finRotate n i = i + 1`,
  `finRotate_apply_zero`, `coe_finRotate_of_ne_last`.
- `MonoidHom.map_closure (f) (s) : (closure s).map f = closure (f '' s)` — namespace is
  **MonoidHom**, not Subgroup.

## Design tricks that cut the work by ~5x vs. the paper's route

- Rather than the paper's parity-dependent `a_r`/`b_r`, use ONE pair for every degree
  `r+2`: `c = finRotate (r+2)` (full cycle) and `t = swap 0 1 = swap 0 (c 0)`, then
  `t*c` is the `(r+1)`-cycle. `sign c = (-1)^(r+1)`, so `{a, {b,d}} = {c, {t, t*c}}` with the
  roles of `c` and `t*c` swapped by the parity of `r`. All three generating sets
  `{c,t}`, `{c,t*c}`, `{t*c,t}`, `{t*c,c}` follow from `closure_cycle_adjacent_swap` plus
  `closure_top_of_mem : closure S = ⊤ → (∀ x ∈ S, x ∈ closure T) → closure T = ⊤`.
- Package the generators as ONE existential lemma
  `exists_gens (r) : ∃ a b d, sign a = 1 ∧ sign b = -1 ∧ sign d = -1 ∧ closure {a,b} = ⊤ ∧
  closure {a,d} = ⊤ ∧ b*b = 1 ∧ (3 ≤ r → d*d ≠ 1)`; the main theorem then never mentions
  cycles at all.
- **Never construct the Goursat isomorphism.** The two facts
  `H ≤ Γ ∧ (π₂ H onto) ∧ A_m ≤ H.goursatFst ⟹ H = Γ` (and its mirror) are 8-line proofs:
  for `(σ,τ) ∈ Γ` pick `(σ',τ) ∈ H`, then `sign (σσ'⁻¹) = 1`, so `(σσ'⁻¹,1) ∈ H` and
  `(σ,τ) = (σσ'⁻¹,1)·(σ',τ)`. This kills Prop 4.4(ii) and all index/cardinality bookkeeping.
- The order obstruction only needs `d*d ≠ 1` (not `orderOf d = r` or `r-1`): `(b,d)² = (1,d²)`
  puts `d²` in `goursatSnd`, so `goursatSnd ≠ ⊥` and mathlib's classification finishes.
  `d*d ≠ 1` for `d = finRotate` via `IsCycle.orderOf` + `orderOf_dvd_of_pow_eq_one`; for
  `d = t*c` by evaluating at `⟨1,_⟩ ↦ ⟨2,_⟩ ↦ ⟨3,_⟩`.
- `n = 2` needs NO classification: `alternatingGroup (Fin 2) = ⊥`
  (`∀ τ : Perm (Fin 2), sign τ = 1 → τ = 1` by `revert; decide`), so the mirror lemma applies
  with a vacuous hypothesis. Only `m ≥ 5` cases ever touch `alternatingGroup_le_of_normal`
  (m > n ≥ 3 forces m ≥ 5 once (4,3) is excluded).
- `goursatFst = ⊥` in the unequal case ⟹ `π₂|_H` is bijective ⟹ `m! ≤ n!`:
  `MonoidHom.ker_eq_bot_iff`, `Nat.card_eq_of_bijective`, `Nat.card_le_card_of_surjective`,
  `Nat.card_perm : Nat.card (Perm α) = (Nat.card α)!`, `Nat.factorial_lt (0 < n) : n! < m! ↔ n < m`
  (needs `0 < n` — pass it as a hypothesis!).

## Gotchas hit this run

- `sign x.1 * (sign x.2)⁻¹ = 1`: plain `simp` rewrites `u⁻¹ → u` in `ℤˣ`, so `mul_inv_eq_one`
  never fires. Prove `∀ a b : ℤˣ, a*b = 1 ↔ a = b` first by
  `rcases Int.units_eq_one_or a with rfl|rfl <;> rcases … <;> decide`.
- `rw [← h]` where `h : closure {x,y} = Γ` and the goal mentions `⟨x, hx : x ∈ Γ⟩` fails with
  "motive is not type correct" (the subtype proof depends on Γ). Fix: prove the statement
  with `closure {x,y}` first and then `rw [h] at hstatement`.
- `n !` needs `open Nat`; write `Nat.factorial n` otherwise (error is a confusing
  "unexpected token '<'").
- `MonoidHom.snd_apply` does not exist; `hx : x ∈ ((MonoidHom.snd ..).comp H.subtype).ker`
  is *defeq* to `(↑x).2 = 1`, so just `have hx' : (↑x : _ × _).2 = 1 := hx` after
  `rw [MonoidHom.mem_ker]`.
- Working with a variable degree: parametrise as `Fin (r + 2)` (obtained by
  `obtain ⟨M, rfl⟩ : ∃ M, m = M + 2 := ⟨m - 2, by omega⟩`). This gives `NeZero`, makes
  `Fin.val_one : (1 : Fin (n+2)).val = 1` match syntactically, and `(0 : Fin (r+2)) ≠ 1`
  is then just `by simp`.
- Fin numerals with a variable modulus: `finRotate (r+2) ⟨k,_⟩ = ⟨k+1,_⟩` by
  `rw [finRotate_apply]; apply Fin.ext; rw [Fin.val_add]; simp only [Fin.val_one];
  exact Nat.mod_eq_of_lt hk1`. Use `Fin.mk` everywhere, never bare numerals ≥ 2.
- `congrArg (fun p => p x) hsq` + `simp only [Perm.mul_apply]` over-unfolds
  (`t (c (t (c x)))`), destroying the rewrite targets. Instead state
  `have : (f * f) x = x := by rw [hsq]; rfl` and `rw [Equiv.Perm.mul_apply, e1, e2] at this`.
- Subgroup-of-subtype bridge: `∃ g₁ g₂ : Γ, closure {g₁,g₂} = ⊤` from
  `closure {x,y} = Γ` — show `Γ ≤ (closure {⟨x,_⟩,⟨y,_⟩}).map Γ.subtype`, then for `z : Γ`
  pull back and use `Subtype.ext`. (`Subgroup.map_injective` also works but needs
  `map ⊤ = range`.)
- `decide` DOES evaluate `Equiv.Perm.sign` on `Perm (Fin 2)` / `Perm (Fin 3)`
  (`∀ τ : Perm (Fin 2), sign τ = 1 → τ = 1` closes instantly), even though `signDiffHom`
  must be declared `noncomputable`.
