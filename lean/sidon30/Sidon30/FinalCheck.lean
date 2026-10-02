import Sidon30

/-!
# Preliminary axiom diagnostics -- the final theorem does not exist yet

`SidonSecondOrderBound` is only the target proposition. These reports concern
the first proved cards, not a proof of that proposition. A successful run of
this file must not be reported as a verification of the final Sidon bound.

When `sidon_second_order : SidonSecondOrderBound` is actually proved, add its
`#print axioms` under `#guard_msgs` with the reviewed exact output. The final
gate must reject `sorryAx` and all axioms other than the standard logical
axioms. See PLAN.md for the complete gate and dependency requirements.
-/

#print axioms Sidon30.isSidon_iff_uniquePositiveDifferences
#print axioms Sidon30.isSidon_weightedDifferenceCount_le_sum
#print axioms Sidon30.positivePairs_card_le_pred
