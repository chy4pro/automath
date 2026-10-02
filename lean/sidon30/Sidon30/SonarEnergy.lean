import Sidon30.SonarWindows

/-! Exact finite triangle/ramp energy accounting for sonar sequences.
Only the displacement map is injective; repeated row values are allowed. -/

noncomputable section
open scoped BigOperators

namespace Sidon30

private def sonarPositivePairs (m : ℕ) : Finset (Fin m × Fin m) :=
  (Finset.univ.product Finset.univ).filter (fun p => p.2.val < p.1.val)

private theorem sum_fin_symmetric_eq {m : ℕ} (K : Fin m → Fin m → ℝ) (a : ℝ)
    (hsymm : ∀ i j, K j i = K i j) (hdiag : ∀ i, K i i = a) :
    (∑ i : Fin m, ∑ j : Fin m, K i j) =
      (m : ℝ) * a + 2 * ∑ p ∈ sonarPositivePairs m, K p.1 p.2 := by
  have hpos : (∑ p ∈ sonarPositivePairs m, K p.1 p.2) =
      ∑ i : Fin m, ∑ j : Fin m, if j.val < i.val then K i j else 0 := by
    unfold sonarPositivePairs
    rw [Finset.sum_filter, Finset.product_eq_sprod, Finset.sum_product]
  have hneg : (∑ i : Fin m, ∑ j : Fin m,
      if i.val < j.val then K j i else 0) =
      ∑ p ∈ sonarPositivePairs m, K p.1 p.2 := by
    rw [hpos]
    exact Finset.sum_comm
  have hd : (∑ i : Fin m, ∑ j : Fin m, if i = j then a else 0) =
      (m : ℝ) * a := by simp
  have hsplit : ∀ i j : Fin m,
      K i j = (if i = j then a else 0) +
        (if j.val < i.val then K i j else 0) +
        (if i.val < j.val then K j i else 0) := by
    intro i j
    rcases lt_trichotomy i.val j.val with hij | hij | hji
    · have hne : i ≠ j := by
        intro h
        exact (ne_of_lt hij) (congrArg Fin.val h)
      simp only [hne, if_false, hij, if_true, not_lt_of_ge hij.le, zero_add]
      exact (hsymm i j).symm
    · have heq : i = j := Fin.ext hij
      subst j
      simp only [hdiag, if_true, lt_self_iff_false, if_false, add_zero]
    · have hne : i ≠ j := by
        intro h
        exact (ne_of_gt hji) (congrArg Fin.val h)
      simp only [hne, if_false, hji, if_true, not_lt_of_ge hji.le, zero_add, add_zero]
  calc
    (∑ i : Fin m, ∑ j : Fin m, K i j) =
        ∑ i : Fin m, ∑ j : Fin m,
          ((if i = j then a else 0) +
            (if j.val < i.val then K i j else 0) +
            (if i.val < j.val then K j i else 0)) := by
      apply Finset.sum_congr rfl
      intro i _hi
      apply Finset.sum_congr rfl
      intro j _hj
      exact hsplit i j
    _ = (∑ i : Fin m, ∑ j : Fin m, if i = j then a else 0) +
        (∑ i : Fin m, ∑ j : Fin m, if j.val < i.val then K i j else 0) +
        (∑ i : Fin m, ∑ j : Fin m, if i.val < j.val then K j i else 0) := by
      simp_rw [Finset.sum_add_distrib]
    _ = _ := by rw [hd, ← hpos, hneg]; ring

private theorem sum_le_sum_of_injective_support {α β : Type*}
    [DecidableEq α] [DecidableEq β] (P : Finset α) (D : Finset β)
    (δ : α → β) (w : β → ℝ) (hinj : Set.InjOn δ (↑P : Set α))
    (hcover : ∀ p ∈ P, w (δ p) ≠ 0 → δ p ∈ D)
    (hnonneg : ∀ d ∈ D, 0 ≤ w d) :
    (∑ p ∈ P, w (δ p)) ≤ ∑ d ∈ D, w d := by
  let Q := P.filter (fun p => δ p ∈ D)
  have hfilter : (∑ p ∈ Q, w (δ p)) = ∑ p ∈ P, w (δ p) := by
    dsimp [Q]
    exact Finset.sum_filter_of_ne hcover
  have hQinj : Set.InjOn δ (↑Q : Set α) := by
    intro p hp q hq hpq
    exact hinj (Finset.mem_filter.mp hp).1 (Finset.mem_filter.mp hq).1 hpq
  have hsub : Q.image δ ⊆ D := by
    intro d hd
    obtain ⟨p, hp, rfl⟩ := Finset.mem_image.mp hd
    exact (Finset.mem_filter.mp hp).2
  calc
    (∑ p ∈ P, w (δ p)) = ∑ p ∈ Q, w (δ p) := hfilter.symm
    _ = ∑ d ∈ Q.image δ, w d := (Finset.sum_image hQinj).symm
    _ ≤ ∑ d ∈ D, w d :=
      Finset.sum_le_sum_of_subset_of_nonneg hsub (fun d hd _ => hnonneg d hd)

private theorem sum_positive_triangle {U : ℕ} (hU : 1 ≤ U) :
    (∑ d ∈ Finset.Icc 1 (U - 1), ((U - d : ℕ) : ℝ)) =
      (U : ℝ) * ((U : ℝ) - 1) / 2 := by
  have hrev : (∑ d ∈ Finset.Icc 1 (U - 1), ((U - d : ℕ) : ℝ)) =
      ∑ d ∈ Finset.Icc 1 (U - 1), (d : ℝ) := by
    refine Finset.sum_bij (fun d _ => U - d) ?_ ?_ ?_ ?_
    · intro d hd
      have hd' := Finset.mem_Icc.mp hd
      apply Finset.mem_Icc.mpr
      constructor <;> omega
    · intro d hd e he hde
      have hd' := Finset.mem_Icc.mp hd
      have he' := Finset.mem_Icc.mp he
      omega
    · intro e he
      have he' := Finset.mem_Icc.mp he
      refine ⟨U - e, ?_, ?_⟩
      · apply Finset.mem_Icc.mpr
        constructor <;> omega
      · omega
    · intro d _hd
      rfl
  have hsub : Finset.Icc 1 (U - 1) ⊆ Finset.range U := by
    intro d hd
    have hd' := Finset.mem_Icc.mp hd
    apply Finset.mem_range.mpr
    omega
  have hsum : (∑ d ∈ Finset.Icc 1 (U - 1), (d : ℝ)) =
      ∑ d ∈ Finset.range U, (d : ℝ) := by
    apply Finset.sum_subset hsub
    intro d hd hn
    have hdU := Finset.mem_range.mp hd
    have hz : d = 0 := by
      by_contra h
      apply hn
      apply Finset.mem_Icc.mpr
      constructor <;> omega
    simp only [hz, Nat.cast_zero]
  rw [hrev, hsum, sum_range_id_real]

/-- The exact triangle weight on column differences, with the full normalized
row-correlation mass. The diagonal contribution is m U a_V. -/
theorem isSonar_triangleRampEnergy_le {m n U V : ℕ}
    (y : Fin m → Fin n) (hA : IsSonar y) (hU : 1 ≤ U) (hV : 1 ≤ V) :
    (∑ i : Fin m, ∑ j : Fin m,
      ((U - (max i.val j.val - min i.val j.val) : ℕ) : ℝ) *
        rampCorrelation V (((y i).val : ℤ) - ((y j).val : ℤ))) ≤
      (m : ℝ) * (U : ℝ) * rampDiagonal V + (U : ℝ) * ((U : ℝ) - 1) := by
  let K : Fin m → Fin m → ℝ := fun i j =>
    ((U - (max i.val j.val - min i.val j.val) : ℕ) : ℝ) *
      rampCorrelation V (((y i).val : ℤ) - ((y j).val : ℤ))
  let δ : Fin m × Fin m → ℕ × ℤ := fun p =>
    (p.1.val - p.2.val, ((y p.1).val : ℤ) - ((y p.2).val : ℤ))
  let w : ℕ × ℤ → ℝ := fun d => ((U - d.1 : ℕ) : ℝ) * rampCorrelation V d.2
  let D := (Finset.Icc 1 (U - 1)).product (Finset.Icc (1 - (V : ℤ)) ((V : ℤ) - 1))
  have hsymm : ∀ i j, K j i = K i j := by
    intro i j
    dsimp [K]
    rw [max_comm j.val i.val, min_comm j.val i.val]
    have hneg : ((y j).val : ℤ) - ((y i).val : ℤ) =
        -(((y i).val : ℤ) - ((y j).val : ℤ)) := by ring
    rw [hneg, rampCorrelation_neg]
  have hdiag : ∀ i, K i i = (U : ℝ) * rampDiagonal V := by
    intro i
    simp only [K, max_self, min_self, Nat.sub_self, Nat.sub_zero, sub_self,
      rampCorrelation_zero hV]
  have hinj : Set.InjOn δ (↑(sonarPositivePairs m) : Set (Fin m × Fin m)) := by
    intro p hp q hq hpq
    have hplt := (Finset.mem_filter.mp hp).2
    have hqlt := (Finset.mem_filter.mp hq).2
    have hfst := congrArg Prod.fst hpq
    have hsnd := congrArg Prod.snd hpq
    dsimp [δ] at hfst hsnd
    have hpne : p.1 ≠ p.2 := by
      intro h
      have := congrArg Fin.val h
      omega
    have hqne : q.1 ≠ q.2 := by
      intro h
      have := congrArg Fin.val h
      omega
    have hvec :
        ((p.1.val : ℤ) - (p.2.val : ℤ), ((y p.1).val : ℤ) - ((y p.2).val : ℤ)) =
        ((q.1.val : ℤ) - (q.2.val : ℤ), ((y q.1).val : ℤ) - ((y q.2).val : ℤ)) := by
      apply Prod.ext
      · omega
      · exact hsnd
    obtain ⟨h1, h2⟩ := hA p.1 p.2 q.1 q.2 hpne hqne hvec
    exact Prod.ext h1 h2
  have hcover : ∀ p ∈ sonarPositivePairs m, w (δ p) ≠ 0 → δ p ∈ D := by
    intro p hp hnz
    have hplt := (Finset.mem_filter.mp hp).2
    have hcol : p.1.val - p.2.val < U := by
      by_contra h
      have hz : U - (p.1.val - p.2.val) = 0 := by omega
      apply hnz
      simp only [w, δ, hz, Nat.cast_zero, zero_mul]
    have hrow : rampCorrelation V (((y p.1).val : ℤ) - ((y p.2).val : ℤ)) ≠ 0 := by
      intro hz
      apply hnz
      simp only [w, δ, hz, mul_zero]
    apply Finset.mem_product.mpr
    constructor
    · apply Finset.mem_Icc.mpr
      constructor <;> dsimp [δ] <;> omega
    · apply Finset.mem_Icc.mpr
      constructor
      · by_contra h
        have he : ((y p.1).val : ℤ) - ((y p.2).val : ℤ) ≤ 0 := by
          dsimp [δ] at h
          omega
        apply hrow
        apply rampCorrelation_eq_zero_of_abs_le
        rw [abs_of_nonpos he]
        dsimp [δ] at h
        omega
      · by_contra h
        have he : 0 ≤ ((y p.1).val : ℤ) - ((y p.2).val : ℤ) := by
          dsimp [δ] at h
          omega
        apply hrow
        apply rampCorrelation_eq_zero_of_abs_le
        rw [abs_of_nonneg he]
        dsimp [δ] at h
        omega
  have hnonneg : ∀ d ∈ D, 0 ≤ w d := by
    intro d _hd
    exact mul_nonneg (by positivity) (rampCorrelation_nonneg V d.2)
  have hsum : (∑ d ∈ D, w d) = (U : ℝ) * ((U : ℝ) - 1) / 2 := by
    dsimp [D, w]
    rw [Finset.product_eq_sprod, Finset.sum_product]
    simp_rw [← Finset.mul_sum, sum_rampCorrelation hV, mul_one]
    exact sum_positive_triangle hU
  have hpositive : (∑ p ∈ sonarPositivePairs m, K p.1 p.2) ≤
      (U : ℝ) * ((U : ℝ) - 1) / 2 := by
    calc
      _ = ∑ p ∈ sonarPositivePairs m, w (δ p) := by
        apply Finset.sum_congr rfl
        intro p hp
        have hplt := (Finset.mem_filter.mp hp).2
        dsimp [K, w, δ]
        rw [max_eq_left hplt.le, min_eq_right hplt.le]
      _ ≤ ∑ d ∈ D, w d :=
        sum_le_sum_of_injective_support (sonarPositivePairs m) D δ w hinj hcover hnonneg
      _ = _ := hsum
  change (∑ i : Fin m, ∑ j : Fin m, K i j) ≤ _
  rw [sum_fin_symmetric_eq K ((U : ℝ) * rampDiagonal V) hsymm hdiag]
  nlinarith only [hpositive]

end Sidon30

end
