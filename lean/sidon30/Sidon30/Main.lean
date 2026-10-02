import Sidon30.FiniteCertificateAssembly
import Sidon30.FiniteBoundaryCost
import Sidon30.RenewalErrorBound

/-!
The complete dependency chain for the exact Sidon bound.
The finite-certificate and boundary-cost hypotheses of the intermediate
reduction lemmas are discharged here using the proved renewal error bound.
-/

namespace Sidon30

/-- The finite Sidon certificate with its explicit uniform error term. -/
theorem discreteSidonCertificate : DiscreteSidonCertificateBound := by
  apply discreteSidonCertificate_of_boundaryCost
  intro N T hN hT
  simpa only [boundaryEnergy, boundarySupport] using
    (boundaryCertificate_energy_le (N := N) (T := T) hN hT
      (fun n hn => renewalCorrection_bound hT hn))

end Sidon30

/-- For every strong Sidon subset of {1,...,N}, with N at least 120^4,
the exact second-order coefficient is 2*sqrt(2)/3 and the additive constant is 1.
The specification includes diagonal sums and places no fourth-power restriction on N. -/
theorem sidon_second_order : SidonSecondOrderBound :=
  Sidon30.sidon_second_order_of_discreteCertificate Sidon30.discreteSidonCertificate
