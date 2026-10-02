OPEN — the exact Sidon theorem now has a complete source dependency chain, awaiting CI for its newly integrated final cards. The middle chain passed run37058690156 / 346252d, including unit potential and the conditional final reduction. No complete target kernel verification is claimed until Main and its guarded axiom audit pass.

# Sidon30 formalisation plan and finite certificate

Task 035, 2026-10-02. Lean v4.34.0-rc1, Mathlib de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11, as pinned in this project. The existing continuous proof is [SIDON_BOUND_PROOF.md](../../problems/erdos30/SIDON_BOUND_PROOF.md). Kernel optimality is outside this task.

## 1. Exact target and current deliverables

The target remains, for every natural N and finite A contained in {1,...,N},

\[
 N\ge120^4=207360000,\quad A\text{ Sidon}
 \quad\Longrightarrow\quad
 |A|\le\sqrt N+\frac{2\sqrt2}{3}\sqrt{\sqrt N}+1.
\]

The Sidon definition includes diagonal sums and requires equality of the two sorted pairs, not just equality as sets. N need not be a fourth power.

Current files:

| File | What exists now |
|---|---|
| Sidon30/Basic.lean | Existing global IsSidon and empty-set lemma; previously compiled smoke test. |
| Sidon30/Statement.lean | SidonSecondOrderBound, a Prop defining the exact target, with no proof. |
| Sidon30/Differences.lean | Strong Sidon iff uniqueness of positive natural differences; positive-pair definition and difference injectivity. |
| Sidon30/WeightedCount.lean | Actual representation counts, zero-difference exclusion, count at most one, and weighted finite-sum majorization. |
| Sidon30/PairCount.lean | Positive ordered pairs inject into the N−1 possible positive differences. |
| Sidon30/FinalCheck.lean | Preliminary axiom reports for those three cards only; no final theorem audit. |
| Sidon30.lean | Imports the current definition, statement and three cards. |

The three new proof cards contain nine theorem declarations and no sorry, admit or new axiom declarations. Their source has been reviewed. CI runs 37052528691 (7485d4d) and 37052888598 (2d672bd) failed at the membership simp lemma in Differences; The destructuring-only repair also failed in run 37054355993 / 1df3d1c. Inspection of the pinned Prod.lean now identifies the exact missing bridge: Finset.product_eq_sprod before Finset.mem_product; that repair is submitted in the next batch. The downstream cards have not yet been validated. Cards 04, 05, 07, 08 and 21 now have source, awaiting CI; card07 is a generic finite Gram interface whose convolution specialization remains pending. Cards09–10 are in progress; the other later cards remain unimplemented rather than hidden behind placeholders. In particular, sidon_second_order does not yet exist.

The first complete formal milestone can be the **original +1 and 120⁴ statement**. The finite route below includes explicit error estimates that preserve both; a larger constant or onset is not presently needed. Before that, the finite certificate inequality (S) is a useful independent milestone. This is a mathematical plan supported by hand derivations, not an already formalized theorem.

## 2. Representation choices

Use integer indices for kernels and shifts, natural indices for the recurrence, and finite sums throughout. The kernel and boundary arrays are rational before their final embedding in the reals. Every denominator is formed in ℚ or ℝ after casting T; never use natural-number division for a weight.

For the first implementation, use explicit finite integer intervals and zero outside the stated support. This avoids setting up a generic convolution library or invoking measure theory. Finite-support functions can later be refactored to Finsupp if that demonstrably shortens the indexing proofs. All displayed sums over ℤ below have an explicit finite support, except that a finitely supported kernel may be applied pointwise to the recursively defined array g; each such evaluation is still a finite sum.

Translate A to B={a−1:a∈A} contained in {0,...,N−1}. The ShiftWindow card must prove membership, cardinality preservation and Sidon preservation using a≥1. Do not silently use natural subtraction without that lower bound. Equivalently, a later implementation may shift the certificate by one and retain A; either convention must keep exactly N window points.

Write k=|B| as a real number in energy formulas. The expression k−1 there is real subtraction. Handle k=0 separately before replacing coefficients using k−1≥0.

## 3. The finite mathematical proof

### 3.1. Weights, correlation and finite energy

For an integer T≥1, extend the following array by zero outside 0≤j<T:

\[
 h_j=\frac{2(T-j)}{T(T+1)},\quad
 f_d=\sum_jh_jh_{j+d},\quad
 a_T=\frac{2(2T+1)}{3T(T+1)},\quad
 m_T=\frac{T-1}{3},\quad \rho=\frac34.
\]

The suggested unnormalized weights 2(T−j)/T² instead have mass 1+1/T. The exact denominator T(T+1) is essential here.

**RampWeights.** Finite first- and second-power summation gives

\[
 h_j\ge0,\quad \sum_jh_j=1,\quad
 \sum_jh_j^2=a_T\le\frac4{3T},\quad
 \sum_jjh_j=m_T.
\]

Proof sketch: substitute j↦T−j, evaluate the finite sums of j and j², clear the positive denominator, and use ring arithmetic.

**CorrelationFacts.** Finite reindexing and Cauchy–Schwarz give

\[
 f_{-d}=f_d,\quad 0\le f_d\le a_T,\quad
 |d|\ge T\Longrightarrow f_d=0,\quad
 \sum_df_d=1,\quad 2\sum_{d=1}^{T-1}f_d=1-a_T.
\]

The mass identity is the product of the two weight masses. The bound f_d≤a_T follows from Cauchy–Schwarz and shift invariance of the square sum. No monotonicity or Riemann-sum approximation is needed.

**FiniteEnergyCS.** For finitely supported real arrays μ,ν, with possibly signed coefficients, put

\[
 E(\mu,\nu)=\sum_{x,y}\mu_x\nu_yf_{x-y}.
\]

Then

\[
 E(\mu,\nu)=\sum_z(h*\mu)_z(h*\nu)_z,\quad
 E(\mu,\mu)\ge0,\quad
 E(\mu,\nu)^2\le E(\mu,\mu)E(\nu,\nu).
\]

Proof sketch: expand the finite triple sum, reindex the h factors, then use finite Cauchy–Schwarz. Enlarge the summation interval to contain both convolved supports before applying the common-index inequality. No positivity of ν is assumed.

**SidonEnergyUpper.** With μ=1_B and r_B(d) counting ordered pairs of difference d>0,

\[
 E(\mu,\mu)
 =a_Tk+2\sum_{d=1}^{T-1}r_B(d)f_d
 \le1+a_T(k-1).                                      \tag{U}
\]

Proof sketch: the zero difference has precisely k diagonal pairs. Swapping coordinates pairs positive and negative differences. Strong Sidon implies r_B(d)≤1. Apply the already written weighted-count card, then the correlation mass identity. Keep the term k−1 through the final algebra.

### 3.2. A recurrence replacing the analytic half-line measure

**RenewalRecurrence.** Define, using only earlier natural indices,

\[
 g_0=\frac{T+1}{2},\qquad
 g_n=\frac1T\sum_{i=1}^{\min(T,n)}g_{n-i}\quad(n\ge1).
\]

Set g_n=0 on negative integer indices. Strong induction gives g_n≥0. The recurrence can be implemented over ℚ; only a finite prefix is ever used in the certificate.

**RenewalRampIdentity.** Let H_n=1 when n≥0 and zero otherwise. For every integer n,

\[
 (h*g)_n=H_n.                                       \tag{H}
\]

Proof sketch: the finite difference of h is

\[
 h_n-h_{n-1}
 =\frac2{T+1}\left(1_{\{n=0\}}-\frac1T1_{\{1\le n\le T\}}\right).
\]

Consequently the difference of h*g is one at zero and zero elsewhere, by the recurrence. It vanishes on negative indices. Finite telescoping proves (H), including the endpoint zero.

**RenewalFirstBlock.** For 1≤n≤T,

\[
 g_n=\frac12(1+1/T)^n,\qquad \frac12\le g_n\le\frac32.
\]

The formula is an induction in the recurrence. For the upper bound, the finite binomial theorem gives (1+1/T)^T≤3: bound its i-th term by 1/i!, use i!≥2^{i−1} for i≥1, and sum a finite geometric series. There is no need for exponential functions or an infinite series.

**RenewalBlockMatrix.** For block number b≥0 and 1≤i,j≤T, write

\[
 v_j=g_{bT+j},\quad w_i=g_{(b+1)T+i},\quad c=1+1/T.
\]

Then w_i=Σ_jK_ij v_j, where

\[
 K_{ij}=
 \begin{cases}
 T^{-1}c^{i-1},&j\ge i,\\
 T^{-1}c^{i-j-1}(c^j-1),&j<i.
 \end{cases}                                       \tag{K}
\]

Each row is nonnegative and sums to one. Prove the formula by induction from
w_i=T⁻¹(Σ_{j=i}^T v_j+Σ_{j=1}^{i−1}w_j). Row sums follow by applying that finite recurrence to the constant input vector. The branches prevent negative natural exponents.

**RenewalBlockContraction.** Every row has

\[
 K_{ij}\ge(2T)^{-1}\quad\text{when }j\ge\lceil T/2\rceil.
\]

For j<i, use the finite Bernoulli inequality c^j−1≥j/T; the other branch is immediate. Put ω_j=(2T)⁻¹ on those columns and zero elsewhere. Its mass β is at least 1/4 and at most one. If all v_j lie in [ℓ,u], every w_i lies in

\[
 [C+(1-\beta)\ell,\ C+(1-\beta)u],\qquad C=\sum_j\omega_jv_j.
\]

Thus the enclosing interval width contracts by at least a factor 3/4. Explicit recursively defined enclosing endpoints suffice; minima, maxima and completeness are unnecessary.

**RenewalErrorBound.** Set q_n=g_n−1 for n≥0, extending q by zero on negative integers. Then

\[
 q_0=(T-1)/2,\qquad
 |q_n|\le\rho^{\lfloor(n-1)/T\rfloor}\quad(n\ge1).     \tag{Q}
\]

Proof sketch: the first block lies in an interval of width one; iterate the contraction. To locate the center, (H) at the right endpoint of block b gives

\[
 1=\sum_{j=0}^{T-1}h_jg_{(b+1)T-j}.
\]

This is a convex combination of values in that block. Hence 1 belongs to its enclosing interval and each value is within its width of 1. Contraction alone would not identify this center; this additional identity is required.

### 3.3. Finite mass identities and the certificate

**CorrectionFiniteL1.** For every finite M≥0,

\[
 \sum_{n=0}^M|q_n|
 \le(T-1)/2+4T\le9T/2.                              \tag{L1}
\]

Group (Q) into blocks of at most T indices and bound the finite geometric sum by 4. Do not introduce an infinite sum of q.

**CorrectionFiniteMass.** Write Q_M=Σ_{n=0}^M q_n. For M≥T−1,

\[
 Q_M-m_T=\sum_{j=0}^{T-1}h_j
                 \sum_{n=M-j+1}^{M}q_n.             \tag{FM}
\]

Proof sketch: h*q=H−h*H. At n≥0 the right side is Σ_{j>n}h_j. Summing n=0,...,M gives m_T, while finite reordering on the left gives Σ_jh_jQ_{M−j}. Subtract this from Q_MΣ_jh_j=Q_M. Empty inner intervals contribute zero. All prefix indices are nonnegative because M≥T−1.

**FiniteBoundaryPotential.** Take N,T≥1 and put

\[
 D=N-1,\quad M=D+T-1,\quad
 q^{[M]}_n=q_n1_{\{0\le n\le M\}},\quad
 \nu_n=1_{\{0\le n\le D\}}+q^{[M]}_n+q^{[M]}_{D-n}.
                                                               \tag{C}
\]

This is a finite rational certificate supported on [1−T,D+T−1]. It may have negative entries. Its exact potential satisfies

\[
 (f*\nu)_x=1\quad(0\le x\le D).                    \tag{P}
\]

Proof sketch: finite associativity and (H) give (f*g)_x=Σ_{s=0}^{T−1}h_s H_{x+s}=1 for x≥0. For x in the window only y in [1−T,D+T−1] matter. There the truncated certificate agrees with g_y+g_{D−y}−1, using
H_y+H_{D−y}=1+1_{0≤y≤D}. Each half-line potential is one on the appropriate side and the constant array has potential Σf=1. Both window endpoints are included.

**FiniteBoundaryCost.** For r=⌊D/T⌋,

\[
 E(\nu,\nu)\le N+\frac23(T-1)+29T\rho^r.             \tag{B}
\]

The constants are fully accounted for:

1. In (FM) all relevant tail indices are at least D+1, so |Q_M−m_T|≤m_Tρ^r. The mass Σν=N+2Q_M differs from N+2m_T by at most 2m_Tρ^r.
2. By (L1), f≤a_T and Σf=1, the potential has absolute value at most 1+2a_T(9T/2)≤13 everywhere.
3. Outside [0,D], ν consists of just two collars, each of T−1 entries bounded in absolute value by ρ^r. Thus their total absolute mass is at most 2(T−1)ρ^r.
4. On the window the potential equals one. Therefore |E(ν,ν)−Σν|≤14·2(T−1)ρ^r.
5. Add the errors: 2m_T+28(T−1)=(86/3)(T−1)≤29T.

Every estimate concerns finite arrays. In particular, the proof neither asserts a positive certificate nor invokes a signed-measure capacity.

**DiscreteSidonCertificate.** Combining finite Cauchy–Schwarz, E(1_B,ν)=k, (U) and (B) gives

\[
 \boxed{
 k^2\le
 \left(N+\frac23(T-1)+29T(3/4)^{\lfloor(N-1)/T\rfloor}\right)
 \left(1+a_T(k-1)\right).
 }                                                     \tag{S}
\]

This holds for all integers N,T≥1 and the stated Sidon sets. When multiplying bounds, supply nonnegativity of the self-energies and their majorants explicitly. The final theorem may handle the empty set separately.

### 3.4. Exact integer scale and the original additive constant

**IntegerScaleAndTail.** Let

\[
 x=\sqrt{\sqrt N}\ge120,\quad \gamma=2\sqrt2/3,\quad
 T=\lceil\sqrt2\,x^3\rceil,\quad
 r=\lfloor(N-1)/T\rfloor.
\]

Then x⁴=N, γ²=8/9, 0<γ<1, and

\[
 a_T\le\gamma/x^3,\quad
 N+\frac23(T-1)\le x^4+\gamma x^3,\quad
 T\le\frac32x^3.
\]

The middle inequality uses T−1≤√2 x³; discarding the minus one would introduce an unnecessary scale error. For the last inequality use T<√2 x³+1, √2≤17/12 and x³≥12.

The division remainder bound (or the equivalent floor inequalities) gives

\[
 r\ge x/2-2\ge58,\qquad x\le2(r+2).
\]

For instance (N−1)/T≥2x/3−2/(3x³)≥x/2−1, and taking the floor loses less than one. If implemented using natural division, derive the corresponding cast inequalities from N−1=rT+(N−1)%T and remainder<T.

The sequence 2(r+2)ρ^r decreases for integers r≥1, because 3(r+3)≤4(r+2). Consequently

\[
 x\rho^r\le120\rho^{58}<1/100.
\]

The rational endpoint needs no numerical approximation:
ρ⁵=243/1024<1/4, hence 120ρ⁵⁸<120/4¹¹<1/100.
Thus, for η=29Tρ^r,

\[
 0\le\eta<\frac{87}{200}x^2<\frac12x^2.              \tag{R}
\]

**SecondOrderFinal.** For k≥1 put C=x⁴+γx³, b=γ/x³ and y=x²+γx+1. Inequality (S) implies

\[
 k^2\le(C+\eta)(1+b(k-1)).
\]

Using γ²=8/9, the exact polynomial identity is

\[
 y^2-C(1+b(y-1))
 =\frac{10}{9}x^2+\frac{10\gamma}{9}x+1.              \tag{A}
\]

Also 1+b(y−1)=1+γ/x+γ²/x²<2. By (R), the added error term η(1+b(y−1)) is less than x², so P(y)>0 for
P(z)=z²−(C+η)(1+b(z−1)).

To exclude k≥y without the quadratic formula, note 0<b<1 and C+η>0. From P(y)>0 and y>0 one gets y>b(C+η). Then

\[
 P(k)-P(y)=(k-y)(k+y-b(C+\eta))\ge0
\]

would contradict P(k)≤0. Therefore k<y, which implies the requested non-strict bound. Handle k=0 directly and transfer from B back to A.

The γ coefficient, +1 and onset are thus justified by explicit inequalities; they are not inferred from an unspecified discretization error. No smaller onset is claimed.

## 4. Card DAG and proposed file boundaries

Each row is one intended Lean file. Rows 01–03 have source now; other proof rows are planned. Statement.lean is the specification and is not counted as a proved card. The optional first counting result 03 is useful for auditing the convention but is not needed by the final route.

| ID / file under Sidon30 | Precise target above / dependencies | Mathlib ingredients |
|---|---|---|
| 01 Differences | Strong Sidon iff positive-difference uniqueness; Basic | Finset product/filter, natural ordered subtraction, omega, Prod.ext |
| 02 WeightedCount | r(0)=0, r(d)≤1 and weighted majorization; 01 | Finset.card_le_one, sum_le_sum, real casts, ordered multiplication |
| 03 PairCount | Positive-pair cardinality≤N−1; 01 | card_le_card_of_injOn, card_range, Icc membership, omega |
| 04 ShiftWindow | a↦a−1 preserves cardinality/Sidon and maps [1,N] to [0,N−1]; 01 | Finset.image, injectivity, interval membership, omega |
| 05 RampWeights | The four mass/moment/square identities; independent of Sidon | Finite first/second power sums, casts, field_simp, ring |
| 06 CorrelationFacts | Symmetry, support, nonnegativity, maximum and mass of f; 05 | sum_product, sum_comm, sum_mul_sum, finite CS, finite reindexing |
| 07 FiniteEnergyCS | Gram identity, nonnegative self-energy and CS; 06 | Finset.sum_mul_sq_le_sq_mul_sq, double/triple finite sums |
| 08 SidonEnergyUpper | Exact diagonal split and (U); 01,02,06 | Product/filter partition, coordinate swap, finite image sums |
| 09 RenewalRecurrence | g definition, recurrence and nonnegativity | Natural strong recursion/induction, finite sum nonnegativity |
| 10 RenewalRampIdentity | (H) by finite differences; 05,09 | Finite convolution expansion, telescoping, induction |
| 11 RenewalFirstBlock | Closed first-block formula and [1/2,3/2]; 09 | Binomial theorem, factorial inequalities, finite geometric sums |
| 12 RenewalBlockMatrix | Formula (K), row nonnegativity and row sum; 09 | Induction, geometric sums, ring/field arithmetic |
| 13 RenewalBlockContraction | Common row mass≥1/4 and width contraction; 12 | Finite Bernoulli inequality, sum inequalities, interval counts |
| 14 RenewalErrorBound | (Q), using (H) to pin the center; 05,10,11,13 | Finite convex combinations, induction over blocks, Nat division |
| 15 CorrectionFiniteL1 | (L1) for each finite prefix; 14 | Finite block reindexing, finite geometric bound, absolute sums |
| 16 CorrectionFiniteMass | (FM); 05,10 | Finite convolution identity and prefix-sum reordering |
| 17 FiniteBoundaryPotential | Certificate (C), support and exact (P); 06,10,16 | Integer intervals, reflection/reindexing, finite convolution |
| 18 FiniteBoundaryCost | (B) with coefficient 29; 05,06,14–17 | abs_sum_le_sum_abs, nonnegative sum comparison, ring arithmetic |
| 19 DiscreteSidonCertificate | Core finite inequality (S); 07,08,17,18 | Ordered multiplication, energy CS, cardinality/indicator sums |
| 20 IntegerScaleAndTail | All ceiling/division and tail estimates (R); 05 | Real.sqrt, Nat.ceil, natural division, power induction, norm_num |
| 21 SecondOrderFinal | Scalar polynomial exclusion (A); 19,20 | Real.sqrt identities, field_simp, ring, explicit positivity, nlinarith |
| 22 Main | sidon_second_order : SidonSecondOrderBound; 04,21,Statement | Unfold specification, transfer/cardinality equalities |
| 23 FinalCheck | Actual final theorem's guarded axiom check; 22 | #print axioms and #guard_msgs |

Attack order: first compile 01–03 and the specification; then 05–08 to close the exact energy upper bound. Prioritize 09–14 next, since the block matrix and its center are the largest proof-engineering risks. Finish 15–19 before root/ceiling algebra. Card 20 and the scalar portion of 21 can be developed independently once their interfaces are frozen. Only combine them in 22 after all hypotheses have been discharged.

## 5. Checked Mathlib interfaces

These names/signatures were read in the official repository at the pinned commit, not tested in this container. Variables and typeclasses below are specialized or abbreviated where appropriate; check inference in CI.

- Finset.sum_mul_sq_le_sq_mul_sq (s : Finset ι) (f g : ι → ℝ):
  (Σ i∈s, f i*g i)² ≤ (Σ i∈s, (f i)²)*(Σ i∈s, (g i)²).
- Finset.sum_sq_le_sum_mul_sum_of_sq_le_mul takes nonnegativity of f,g and pointwise (r i)²≤f i*g i; it yields the corresponding finite summed inequality. It is available if a weighted formulation helps. The older equality-only name is deprecated.
  [Finite Cauchy–Schwarz source](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/Order/BigOperators/Ring/Finset.lean#L126).
- Finset.sum_mul_sum expands a product of sums; [source](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/BigOperators/Ring/Finset.lean#L56).
- Finset.sum_product and Finset.sum_comm reorder finite double sums; their additive versions are generated by the source's to_additive declarations. [Source](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/BigOperators/Group/Finset/Sigma.lean#L78).
- Finset.sum_image uses Set.InjOn of the map on the source finset. [Source](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/BigOperators/Group/Finset/Basic.lean#L92).
- For real-valued weights, Finset.sum_le_sum_of_subset_of_nonneg needs nonnegativity on the newly added indices. Do not substitute the more restrictive sum_le_sum_of_subset. [Source](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/Order/BigOperators/Group/Finset.lean#L159).
- The initial card interfaces card_le_one, card_le_card_of_injOn and card_range were checked in [Finset/Card.lean](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Data/Finset/Card.lean).
- Real.sqrt_nonneg, Real.sq_sqrt (h : 0≤x), Real.sqrt_sq (h : 0≤x), Real.sqrt_le_sqrt, Real.le_sqrt and Real.sqrt_mul (hx : 0≤x) y are present in [Analysis/Real/Sqrt.lean](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Analysis/Real/Sqrt.lean#L144). Give both square-root square identities to nlinarith explicitly; it will not infer them itself.
- Nat.le_ceil, Nat.ceil_lt_add_one with nonnegativity, Nat.floor_le with nonnegativity, Nat.lt_floor_add_one, Nat.le_floor and Nat.le_floor_iff were checked in [Floor/Semiring.lean](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/Order/Floor/Semiring.lean#L47) and [Floor/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11/Mathlib/Algebra/Order/Floor/Defs.lean#L140). Prefer natural division for r if it reduces floor coercions.

Exact helper names for power sums, factorial estimates, block reindexing and geometric bounds still need to be selected from the pinned library when those cards are implemented. They are mathematical dependencies, not claimed completed API checks. All imports may initially remain import Mathlib through the Basic dependency; narrow imports only after successful compilation.

## 6. Statement and final audit design

Statement.lean imports Sidon30.Basic, which itself imports only Mathlib. A literal import Mathlib alone cannot reuse the project's already defined IsSidon. Reusing Basic preserves a single definition and keeps the specification independent of all proof cards.

The actual specification is:

~~~lean
def SidonSecondOrderBound : Prop :=
  ∀ (N : ℕ) (A : Finset ℕ),
    120 ^ 4 ≤ N →
    A ⊆ Finset.Icc 1 N →
    IsSidon A →
    (A.card : ℝ) ≤
      Real.sqrt (N : ℝ) +
        (2 * Real.sqrt 2 / 3) * Real.sqrt (Real.sqrt (N : ℝ)) + 1
~~~

The future Main file must prove the global theorem

~~~lean
theorem sidon_second_order : SidonSecondOrderBound := ...
~~~

The ellipsis is documentation of an unimplemented proof, not a Lean placeholder added to the project.

Once that theorem exists, FinalCheck must import it and guard the actual diagnostic, for example if all three standard logical axioms occur:

~~~lean
/-- info: 'sidon_second_order' depends on axioms: [propext, Classical.choice, Quot.sound] -/
#guard_msgs in
#print axioms sidon_second_order
~~~

Use the exact reviewed output of that theorem; a smaller subset of those standard axioms is acceptable. Do not silently regenerate expected output when an unexpected axiom appears. sorryAx or any project axiom is a failure. Printing axioms of the Prop definition instead would not audit a proof and is expressly insufficient.

The current FinalCheck guards the three initial core theorem diagnostics against the actual standard-axiom output from run37056219882. It also reports later milestones, including the explicitly conditional final reduction. It does **not** contain or claim a final-theorem gate.

## 7. CI protocol, risks and honest status

- Baseline: CI_LOG.md records run 37050942706, commit 6da7197, completed success at 2026-10-02T18:57:41Z. That run predates this batch and checks only the Basic smoke test.
- Tasks 036 and 037 supersede the initial READY-only handoff. The protocol now authorizes only tools/sidon30_push.sh for scoped commits/pushes and tools/sidon30_ci.sh --wait for CI retrieval. The token mount is present and git/curl are available; its contents have not been printed. Root owns this loop, inspects the actual run commit before accepting a result, and continues cards after green batches. No local Lean build or installation is authorized.
- A green build alone does not establish the final theorem, particularly if later scaffolds contain sorry. Completion requires the exact statement, a fully discharged dependency chain and the guarded final axiom output.
- Task 036 reports the workflow failure-propagation fix. The current workflow explicitly selects shell: bash, whose GitHub Actions invocation includes pipefail; run 37052888598 correctly failed the Build step and skipped Axioms. This task does not edit the workflow.
- Highest mathematical/implementation risks: natural-subtraction truncation, casting weights before division, support endpoints, the exact N-point window, finite convolution reindexing, identifying the center 1 in the block bound, and retaining both T−1 and k−1. The proof above supplies the quantitative tail rather than assuming discretization preserves the coefficient.
- Keep functions with explicit support and denominator-positivity lemmas. Keep recursive termination arguments separate from the recurrence identities. Under relaxedAutoImplicit=false, declare all parameters explicitly.
- The final algebra is polynomial after introducing x and γ with their square identities. Supply positivity and denominator facts before field_simp or nlinarith; avoid a large tactic call spanning all previous cards.
- No finite numerical enumeration proves this parameterized certificate. No numerical experiment was run for this plan. The finite route was derived by one worker and independently checked by the root; another worker checked the normalization and pinned APIs but did not audit every detail of the tail constant 29. These are same-vendor mathematical reviews, not cross-vendor, human or Lean verification of the new discrete proof.
- The source cards were written on a separate informed worker and read by the root. No clean-room claim is made for this formalisation planning task. Token and monetary costs are not exposed and are not estimated.

Unfinished proof inventory: cards06,09–20,22, plus the finite-convolution specialization of card07, remain unimplemented or in progress. Cards04,05,07,08,21 have source but are not yet CI validated. The final theorem is absent. No optimality theorem is part of this inventory. CI result for the first new batch: **run37054355993 failed at mem_positivePairs; product_eq_sprod repair and next source cards await CI**.

### CI implementation ledger

- Run 37055051049 / fead917: the product bridge removed the Differences failure. Build still failed in ShiftWindow and PairCount where omega treated unapplied lambdas as opaque, and in SidonEnergyUpper on conditional simplification and addition-side API orientation. The next source repair makes the arithmetic expressions explicit with change, includes ite_true, and uses add_le_add le_rfl. Axioms did not run because the build failed.
- Card09 RenewalRecurrence now has complete source, with a well-founded natural recurrence and zero extension, awaiting CI. Card10 remains in progress.

- Run37055538640 / 1de2678: only RenewalRecurrence failed (sum_coe_sort simp matching); explicit term application is the repair. All earlier reported card errors disappeared, but no complete-batch or axiom PASS is claimed yet. The next commit also stores source-ready cards06,10,11,20 and FinalReduction without importing them until this baseline is green.
- Card11 implementation choice: the first-block power bound uses the pinned Mathlib Real.one_add_inv_pow_le_exp and Real.exp_lt_two_add_div_two_sub at x=1. This is an exact library proof of the scalar bound3, replacing the planned explicit binomial/factorial derivation. No measure theory, infinite convolution or renewal limit is used by this card, but its library dependency does include the exponential function.
- FinalReduction explicitly states DiscreteSidonCertificateBound as a Prop and proves only the implication from that finite inequality to SidonSecondOrderBound. It is not an axiom and does not close sidon_second_order.

- **Baseline green:** run37056219882, commitf8e0beb, Build completed8719jobs and Axioms succeeded. Imported proof cards01–05,07–09,21 compiled. The first three diagnostic theorems each depend only on [propext, Classical.choice, Quot.sound]; their exact outputs are now guarded. The main theorem remains absent.
- Next batch imports source cards06,10–12,20, the generic Gram/certificate bridges, CorrectionBasic, actual finite BoundaryPotential and the conditional FinalReduction. They are not yet claimed compiled. Cards13–16,18–19 actual certificate closure and Main remain unfinished.

- Run37057054792 / 91a49ac: IntegerScaleAndTail compiled; batch failed in first-block/ramp base-index simplification, matrix equal-index ite_true, dependent conditional rewrites in CorrelationFacts, and the empty-set cast in FinalReduction. Repairs normalize the indices/cast and use simp for proposition rewrites. Next commit keeps the same imported chain while storing ready13/15/16 source without yet importing it.

- Run37057713673 / 0ea8672: only RampGramEnergy failed, on a lambda-wrapped shift injection supplied to omega. The explicit change repair matches the already successful earlier pattern. FinalReduction compiled, but remains conditional on the unproved finite certificate. No main-theorem PASS is inferred.

- **Middle chain green:** run37058690156 / 346252d, 8729jobs; six additional printed axiom diagnostics all contained exactly [propext, Classical.choice, Quot.sound]. The reflected renewal beta-reduction repair closed the last failure in this batch.
- Main.lean now supplies the actual renewal pointwise bound to boundaryCertificate_energy_le, supplies the resulting concrete double-sum bound to discreteSidonCertificate_of_boundaryCost, and applies the exact final reduction. Every previously explicit mathematical hypothesis is supplied by a theorem; no new axiom or sorry is used. The complete imported source and exact final axiom guards are **pending CI**, not yet a kernel result.
