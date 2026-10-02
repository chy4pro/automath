PROVED for nonnegative autocorrelation factors, with independent in-team and isolated Claude mathematical reviews PASS. The full-class infimum remains OPEN, but KERNEL_PERTURBATION.md now proves that it is strictly below the restricted optimum. No numerical optimum is promoted to a theorem.

Revision 2026-10-02 (039c): kernels are explicitly continuous; all coefficient-optimality statements below concern the stated leading-term product template. The vertical capacity theorem is linked with its exact hypotheses. The numerical bounds and constructed kernels are unchanged.

# The first-moment functional and its sonar coefficient

Write a=f(0), M=∫|x|f(x)dx. Kernels are continuous, real, even, nonnegative, positive definite and integrable, with ∫f=1. Infinite M is irrelevant to minimization. In the leading-term product template derived from SONAR_COSINE.md (C5), the error to optimize is MT+b_y U+a a_y n²/(TU). Its AM–GM minimum is 3[(aM)(a_y b_y)]^(1/3)n^(2/3). This statement presumes the lattice and certificate errors are lower order at the chosen scales. It is a property of this inequality template. The vertical ramp certificate has a_y b_y=8/9.

## 1. Exact optimum when f=h*h~ with h≥0

Let h≥0 belong to L¹∩L², with ∫h=1, and put F(x)=∫_{−∞}^x h. Then

a=∫h²,
M=∫∫|x−y|h(x)h(y)dxdy=2∫F(x)(1−F(x))dx.

The second identity follows by writing |x−y| as the integral of indicators that a threshold separates x and y, and applying Tonelli. Cauchy–Schwarz gives

(∫h²)(∫F(1−F)) ≥ [∫h sqrt(F(1−F))]²
= [∫_0^1 sqrt(u(1−u))du]² = (π/8)².

The substitution uses the absolutely continuous cumulative distribution F; it remains valid if h vanishes on subintervals. Hence

                         aM ≥ π²/32.                       (K1)

Equality is attained by h(x)=(π/2)sin(πx) on [0,1], zero outside, and by its translates/dilates. Indeed its cumulative distribution on [0,1] is (1−cos(πx))/2, so h=π sqrt(F(1−F)); a=π²/8 and M=1/4. Conversely, equality in Cauchy–Schwarz forces h=c sqrt(F(1−F)) almost everywhere. Where 0<F<1, integration of this differential equation gives the same sine density on one interval, up to translation and dilation. This proves the infimum and its attainment within the stated nonnegative-factor class.

With the vertical ramp certificate fixed, the best leading coefficient of this template over horizontal nonnegative factors, subject to its lattice asymptotics, is

                         3(π²/36)^(1/3).

The fully explicit realization, including lattice errors, is proved in SONAR_COSINE.md. The restriction h≥0 is material: KERNEL_PERTURBATION.md constructs a continuous nonnegative positive-definite unit-mass kernel with aM<π²/32. By K1 it cannot have a nonnegative unit-mass autocorrelation factor in L¹∩L². Thus the distinction between these classes has an explicit example.

If the vertical kernel is also varied, the needed separate capacity result is [KERNEL_OPTIMALITY.md, Theorem 1](../erdos30/KERNEL_OPTIMALITY.md): for every even nonnegative f_y∈C₀(R)∩L¹(R) of mass 1 and a_y=f_y(0)>0, let C_y(L) be the reciprocal minimum energy over nonnegative probability measures supported on the closed interval [0,L]. Then liminf_(L→∞)(C_y(L)−L)≥8/(9a_y). In particular a finite intercept C_y(L)=L+b_y+o(1) obeys a_y b_y≥8/9; the ramp attains equality. Combining this result with K1 only optimizes the above product template for kernels whose sampling and certificate asymptotics justify that template. It makes no assertion about non-product two-dimensional kernels or additional information beyond this inequality.

## 2. A rigorous lower bound for the full class

The elementary bound aM≥1/4 follows from 0≤f≤a and unit mass. Positive definiteness supplies a quantitative improvement:

                    aM ≥ 1/4 + 1/(18π²).                  (K2)

Proof. Normalize g(t)=f(t/a)/a, so g(0)=1, ∫g=1, and its first absolute moment is aM. Positive definiteness gives 0≤g≤1 from each two-by-two principal matrix. Its Fourier transform, with phase exp(−2πiξt), is nonnegative. This standard consequence also follows by applying positive definiteness to finite sums approximating ∫∫g(x−y)φ(x)conj(φ(y))dxdy and then to long truncated exponential test functions.

Let B=1_[−1/2,1/2]. At ξ=3/2, its Fourier transform is −2/(3π). Thus

||g−B||₁ ≥ |g_hat(3/2)−B_hat(3/2)| ≥ 2/(3π).

Put m=∫_{|t|>1/2}g=∫_{|t|≤1/2}(1−g). Then ||g−B||₁=2m and m≥1/(3π). The excess moment is

D=∫|t|g−1/4
 =∫_{|t|>1/2}(|t|−1/2)g
  +∫_{|t|≤1/2}(1/2−|t|)(1−g).

Each last integral is at least m²/4: for a density bounded by1 on two rays measured from their boundary, filling the two nearest strips of width m/2 minimizes this nonnegative distance cost. For the inner strips m≤1, so they fit inside the interval. Equivalently the layer-cake bound integrates (m−2s)_+ over s≥0. Therefore D≥m²/2≥1/(18π²), proving K2.

Combining K1's admissible example with K2 first yields

1/4+1/(18π²) ≤ inf_full_class aM ≤ π²/32.

The explicit admissible perturbation in KERNEL_PERTURBATION.md sharpens the upper endpoint to (π²/32)R, where R=1−129/(8·10⁷)−508/10¹⁴<1. Thus the two classes have strictly different infima. These bounds do not determine the full infimum. In the same leading-term product template, with the ramp vertical certificate fixed (or the finite-intercept vertical class just specified), K2 gives only the following lower bound for its optimized coefficient:

3[(8/9)(1/4+1/(18π²))]^(1/3),

There is no matching full-class attainment claim. This is not a barrier for all two-dimensional kernels or for all sonar arguments. The exact value requested in StageC remains OPEN beyond the nonnegative-factor subclass.

## 3. Bounded exploratory checks and rejected shortcuts

A deterministic floating-point grid checked the explicitly admissible family f_cos(x)(1+λcos(ωx)), normalized to mass1, with 0≤λ≤1. Nonnegativity is pointwise; positive definiteness follows from nonnegative frequency translates. The grid used λ increments1/20, ω increments1/4 through40 and Simpson integration with4000 subintervals. It found no smaller value than π²/32. This does not prove optimality.

A signed-factor family h=(1−e)sin(πx)+3e sin(3πx), supported on [0,1], appeared to reduce the functional but failed nonnegativity of its autocorrelation. At e=−1/5 its autocorrelation at lag1/2 is −3/(50π) before mass normalization. This is an exact rejection, not a rounding issue. A denser grid also found negative values for e=−3/20,−4/25,−17/100,−9/50. None is an admissible improved kernel.

These checks used no solver or installed dependency. They are exploratory only. The exact rational checker check_sonar_cosine.js verifies the coefficient brackets and explicit inequalities used in the proved theorem; the analytic integral identities above are proved in the text.

## 4. Where another known marginal can help

The exact-marginal step is not specific to one point per column. Let μ be a finite positive measure on X×Y with known X-marginal λ. For a product positive-definite kernel φ(x−x')ψ(y−y'), suppose ρ has ψ-potential1 on the allowed Y-region and energy at most C. Put Λ=E_φ(λ,λ)>0. Then the test measure λ⊗ρ has mixed energy Λ and self-energy at most ΛC, so

                         E_(φ⊗ψ)(μ,μ)≥Λ/C.

This follows from Fubini and Cauchy–Schwarz exactly as in sonar. It can exploit any prescribed marginal, including a full grid marginal in higher-dimensional graph-type models. For unrestricted Sidon boxes or Manhattan configurations, however, the projected marginal is not prescribed. Replacing its unknown energy by the usual capacity lower bound gives back the product-capacity argument; a universal extra gain has not been proved. A g-thin or weak Sidon set likewise has no extra fixed spatial marginal in its definition. For difference triangle sets the equal number of marks per row is already used by summing the per-row lower energies; adding cross-row energy would require difference constraints that the DTS definition does not impose. Thus these other models do not inherit the sonar gain solely from their stated definitions.
