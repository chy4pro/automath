OPEN — required T1–T3 kernel-checked; optional T4 CI pending, statement audit passed.

# Rational-kernel transfer formalization

The exact targets are defined in `Sidon30/TransferStatement.lean`, importing
only `Sidon30.Basic` (and hence Mathlib). T1, T2 and T3 are now proved.
The existing Sidon theorem and its thirteen axiom guards remain unchanged.

## Work cards

1. **T1: g-thin — PROVED.** Exact nonzero ordered integer-difference multiplicity.
   Reuse the finite ramp certificate with energy `g + a_T (k-g)`.
   The integer scale is rounded from `sqrt(2) (gN)^(3/4) / g`.
2. **T2: weak Sidon — PROVED.** Strictly off-diagonal unordered sums. Proved the
   repeated-difference structure and an exact finite energy bound, then
   use scale `ceil(sqrt(6) N^(3/4))` and the original onset `90^4`.
3. **T3: triangle sonar — PROVED.** `Fin m → Fin n`; ordered nondiagonal vector
   injectivity. State the original powers by `Real.rpow`, with onset `48^3`.
4. **T4 (optional) — CI pending; statement audit passed:** difference triangle
   sets. The exact D1 and D2 targets are in the separate definitions-only
   `DifferenceTriangleStatement.lean`. A normalized configuration consists
   of `n` rows of `k+1` marks including zero, all at most `m`, with globally
   unique positive within-row differences. There is no cross-row constraint.
   The strict D1 and expanded D2 candidates keep `n>=1`, `k>=20365`.

The original finite signed certificate already has an explicit geometric
remainder. Reusing it avoids any need to formalize continuous integration.
Any new finite comparison must be proved at its stated onset; the paper's
continuous certificate estimates are not assumed as axioms.

## Validation and ownership

Only remote CI, via the prescribed scoped push and CI scripts. No local
Lean build or installation. Root owns integration, CI, and appended axiom
guards. Existing completed worker seats were inspected before reuse.
All new headline theorems must pass `#guard_msgs` axiom checks before a
PROVED milestone. Statement audit is requested first through the inbox.

## Evidence ledger

- 2026-10-02: exact definitions passed CI `37072461005` / `f6bdf41`.
  The coordinator read the statement module and approved all three
  definitions and target propositions through the inbox. They are frozen.
- CI `37073205929` / `044351c` passed the arbitrary-set and indexed-row
  capacity certificates, g-thin difference counting and scale estimates,
  and the initial sliding-window identities. The indexed certificate
  explicitly allows repeated row values.
- CI `37073917922` / `3523813` passed **8749 build jobs and the Axioms step**.
  The job-step conclusions were independently read from the Actions API.
  This checks `g_thin_second_order : GThinSecondOrderBound`, its `g=1`
  recovery `sidon_second_order_from_gThin`, and
  `Sidon30.weakSidon_second_order : WeakSidonSecondOrderBound`.
  Each headline guard allows exactly `[propext, Classical.choice, Quot.sound]`.
  Additional guards check the weak-Sidon multiplicity-two theorem and the
  repeated-difference count `<= k-2`. All original thirteen guards passed
  unchanged; the old Sidon main theorem and specification are unchanged.
- The sonar finite route sums the indexed capacity inequality over every
  horizontal window. Its exact squared column count is
  `m U^2 - (U^3-U)/3`; uniqueness of displacement vectors bounds the summed
  row energy by `m U a_V + U(U-1)`. This yields the discrete triangle/ramp
  sandwich without continuous integration. At `x=n^(1/3) >= 48`, use
  `U=ceil(2x^2)`, `V=ceil(x^2)` and the explicit geometric tail `< 1`.
  CI `37075227591` / `ca96407` passed **8755 build jobs and all 22 axiom
  guards**, including `sonar_triangle_bound : SonarTriangleBound` and the
  actual finite sandwich. Build and Axioms step outcomes were separately
  verified through the Actions API. The statement uses exact `Real.rpow`
  exponents and allows repeated rows, with no unstated restriction on `m`.
  A separate informed source review found no convention or algebra error.
  The review seat also reported exact finite checks (231 marginal identities,
  60270 pair counts, 21400 energy/window tests). These were not rerun by the
  integrating seat and are not the evidence for the kernel milestone.
- T4 reuses the real scope parameter `x^4=m/n` with the actual finite
  window `N=m+1`. The additional `1/n` belongs to the explicit error term;
  it is not discarded. A strict scalar comparison is retained so that D1
  has no extra `-1`. Counting, scale, strict inversion and expanded remainder
  candidates are assembled, awaiting CI. The coordinator read and approved
  the exact T4 configuration definition and both scope statements through
  the inbox. No further Lean targets are authorized for this package after T4.

Only actual CI outcomes are listed as checked. Mathematical review and
source inspection of a candidate are not substitutes for compilation and
the headline axiom guards. No local Lean build has been run.
