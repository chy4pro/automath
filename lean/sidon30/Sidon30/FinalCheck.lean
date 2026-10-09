import Sidon30

/-!
Axiom gates for the exact theorem and its principal finite proof milestones.
All thirteen exact guards passed in CI run37060176909, commit f8e9766,
with only the standard logical axioms. The global sidon_second_order theorem
discharges the explicit hypotheses of the conditional intermediate reductions.
Unexpected project axioms or sorryAx must fail these exact guards.
-/

/-- info: 'Sidon30.isSidon_iff_uniquePositiveDifferences' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.isSidon_iff_uniquePositiveDifferences

/-- info: 'Sidon30.isSidon_weightedDifferenceCount_le_sum' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.isSidon_weightedDifferenceCount_le_sum

/-- info: 'Sidon30.positivePairs_card_le_pred' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.positivePairs_card_le_pred

/-- info: 'Sidon30.sum_rampWeight' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sum_rampWeight

/-- info: 'Sidon30.finiteGramEnergy_cauchySchwarz' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.finiteGramEnergy_cauchySchwarz

/-- info: 'Sidon30.isSidon_orderedPairEnergy_le_normalized' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.isSidon_orderedPairEnergy_le_normalized

/-- info: 'Sidon30.renewal_ramp_identity' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.renewal_ramp_identity

/-- info: 'Sidon30.boundaryCertificate_potential' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.boundaryCertificate_potential

/-- info: 'Sidon30.sidon_second_order_of_discreteCertificate' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidon_second_order_of_discreteCertificate

/-- info: 'Sidon30.renewalCorrection_bound' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.renewalCorrection_bound

/-- info: 'Sidon30.boundaryCertificate_energy_le' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.boundaryCertificate_energy_le

/-- info: 'Sidon30.discreteSidonCertificate' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.discreteSidonCertificate

/-- info: 'sidon_second_order' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms sidon_second_order

/-- info: 'Sidon30.ramp_card_sq_le_certificate' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.ramp_card_sq_le_certificate

/-- info: 'Sidon30.indexed_ramp_card_sq_le_certificate' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.indexed_ramp_card_sq_le_certificate

/-- info: 'g_thin_second_order' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms g_thin_second_order

/-- info: 'sidon_second_order_from_gThin' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms sidon_second_order_from_gThin

/-- info: 'Sidon30.isWeakSidon_positiveDifferenceCount_le_two' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.isWeakSidon_positiveDifferenceCount_le_two

/-- info: 'Sidon30.isWeakSidon_repeatedDifferences_card_le' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.isWeakSidon_repeatedDifferences_card_le

/-- info: 'Sidon30.weakSidon_second_order' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.weakSidon_second_order

/-- info: 'Sidon30.sonar_finite_sandwich' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sonar_finite_sandwich

/-- info: 'sonar_triangle_bound' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms sonar_triangle_bound

/-- info: 'Sidon30.dts_scope_count' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.dts_scope_count

/-- info: 'Sidon30.dts_finite_certificate' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.dts_finite_certificate

/-- info: 'difference_triangle_scope_bound' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms difference_triangle_scope_bound

/-- info: 'difference_triangle_expanded_bound' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms difference_triangle_expanded_bound

/-! Lower-onset Route B: every new theorem and the scalar compatibility wrapper. -/

/-- info: 'Sidon30.sidonIntegerScale_quotient_bound_sharp' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonIntegerScale_quotient_bound_sharp

/-- info: 'Sidon30.sidonIntegerScale_quotient_ge_thirtytwo' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonIntegerScale_quotient_ge_thirtytwo

/-- info: 'Sidon30.sidonTailEnvelopeSharp_succ_le' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonTailEnvelopeSharp_succ_le

/-- info: 'Sidon30.sidonTailEnvelopeSharp_le_base' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonTailEnvelopeSharp_le_base

/-- info: 'Sidon30.sidonTail_power_thirtytwo_lt' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonTail_power_thirtytwo_lt

/-- info: 'Sidon30.sidonTailEnvelopeSharp_lt' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonTailEnvelopeSharp_lt

/-- info: 'Sidon30.sidonIntegerScale_tail_lt_sharp' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonIntegerScale_tail_lt_sharp

/-- info: 'Sidon30.sidonIntegerScale_tail_lt_half_sharp' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidonIntegerScale_tail_lt_half_sharp

/-- info: 'Sidon30.secondOrder_of_scaled_certificate_one' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.secondOrder_of_scaled_certificate_one

/-- info: 'Sidon30.secondOrder_of_scaled_certificate' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.secondOrder_of_scaled_certificate

/-- info: 'Sidon30.sidon_fourthRoot_gt_of_onset' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidon_fourthRoot_gt_of_onset

/-- info: 'Sidon30.sidon_second_order_of_discreteCertificate'' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms Sidon30.sidon_second_order_of_discreteCertificate'

/-- info: 'sidon_second_order'' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms sidon_second_order'
