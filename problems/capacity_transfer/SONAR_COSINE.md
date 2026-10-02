PROVED — complete analytic derivation, independent OpenAI in-team review PASS, isolated Claude referee A main-theorem PASS, and 16 BigInt rational checks PASS. No novelty claim or Lean formalisation is made.

Revision 2026-10-02 (039c): clarified the scope of the template optimum, stated the logarithm bound and integral domains, and renamed an auxiliary variable. Theorem C1, its coefficient, remainder and onset are unchanged. The referee report calls itself same-vendor; the actual provenance here is an OpenAI derivation reviewed by Claude, as identified in the coordinator's dispatch.

# An explicit cosine-kernel bound for sonar sequences

A sonar sequence with n rows and m columns is a sequence y_0,...,y_(m−1) in {0,...,n−1} for which all ordered displacement vectors (i−j,y_i−y_j), i≠j, are distinct. Equivalently, displacements with positive first coordinate are distinct. Repeated row values are allowed; there is exactly one point per column.

**Theorem.** For every integer n≥160³=4,096,000 and every such sequence,

m ≤ n + 3(π²/36)^(1/3)n^(2/3) + 4n^(1/3).          (C1)

The second coefficient is strictly below 2. For the specific leading-term inequality template C5, with the vertical ramp certificate fixed and horizontal kernels of the form h*h~ with h≥0, KERNEL_FUNCTIONAL.md proves that the best leading coefficient is 3(π²/36)^(1/3), whenever the stated lattice asymptotics apply. This is not a lower bound for arbitrary two-dimensional kernels or other energy inequalities. KERNEL_PERTURBATION.md gives an admissible horizontal kernel outside this nonnegative-factor class and a strictly smaller coefficient; the full-class infimum remains open.

## 1. Analytic inputs and exact marginal identity

The vertical kernel is the ramp autocorrelation f from COMMON_CAPACITY.md, with a₂=4/3, b=2/3 and α=log(4/3). For every L≥1 that appendix constructs a finite signed measure ν_L whose potential is1 on the closed interval[0,L] and whose energy is at most C(L)=L+b+200exp(−αL). All signed-measure Cauchy–Schwarz and Fubini justifications are included there.

For the horizontal kernel let h(x)=(π/2)sin(πx) on[0,1], zero outside, and g=h*h~. Direct integration gives, for0≤s≤1,

g(s)=(π²/8)(1−s)cos(πs)+(π/8)sin(πs),

g(−s)=g(s), and g=0 for|s|≥1. Its value at zero is a=π²/8, its mass is1, and M=∫|s|g(s)ds=1/4, as also proved in KERNEL_FUNCTIONAL.md. It is nonnegative by its autocorrelation integral of two nonnegative functions; g'(s)=−(π³/8)(1−s)sin(πs)≤0.

Choose positive real scales T≤m and U≤n. Let μ be the point measure of the sonar sequence, λ=Σ_{i=0}^{m−1}δ_i, and let ρ be the U-dilate of ν_(n/U). Use the product kernel G(x,y)=g(x/T)f(y/U). The test measure λ⊗ρ has mixed energy with μ equal to

Λ=Σ_{i,j=0}^{m−1}g((i−j)/T),

because every y-coordinate lies in[0,n]. Its self-energy is ΛE_f(ν_(n/U),ν_(n/U)). Also Λ≥am>0 when m>0. Cauchy–Schwarz, followed by division by Λ, gives

Λ ≤ E_G(μ,μ) C(n/U).                              (C2)

No positive-sign assumption on ρ is needed.

## 2. Lattice estimates with bounded error

For any even nonnegative decreasing unit-mass kernel w with w(0)=a_w, comparison of the positive lattice sum with left and right Riemann sums gives

T−a_w ≤ Σ_{d∈Z}w(d/T) ≤ T+a_w.

For g, define p(s)=|s|g(s). On the positive half-line,

∫_(0,∞)|p'|≤∫_(0,∞)g+∫_(0,∞)s|g'|=1;

integration by parts gives the second integral1/2. Thus the total variation of p is at most2. Comparing each lattice sample with the integral over its adjacent cell proves

|Σ_{d∈Z}p(d/T)−T∫p|≤2,

and consequently

Σ_{d∈Z}|d|g(d/T) ≤ MT²+2T.

Since T≤m and g is supported on[−1,1], the exact column identity is

Λ=mΣ_{d∈Z}g(d/T)−Σ_{d∈Z}|d|g(d/T)
 ≥ m(T−a)−MT²−2T.                                (C3)

The off-diagonal displacement vectors of μ are distinct and have nonzero first coordinate. Both kernels are nonnegative, so their weighted sum is bounded by the entire corresponding lattice sum. The horizontal sum over nonzero integers is at most T, and the vertical sum is at most U+a₂. Therefore

E_G(μ,μ) ≤ aa₂m + T(U+a₂).                        (C4)

Combining C2–C4 and dividing by T gives the fully finite inequality

m[1−a/T−aa₂C(n/U)/T] ≤ MT+2+C(n/U)(U+a₂).          (C5)

This is linear in m and supplies the bootstrap; no estimate m=n+O(n^(2/3)) has been assumed.

## 3. Explicit scales, exponential tail and final algebra

Put x=n^(1/3), v=(π²/36)^(1/3), T=4vx² and U=(3/2)vx². Elementary bounds3<π<22/7 give

3/5<v<2/3,  a=(9/2)v³,  M=1/4.

If m<n, C1 is immediate. Otherwise m≥n, and x≥160 ensures T≤n≤m and U≤n. Put ε=200exp(−α n/U). The identity log(4/3)=∫_1^(4/3)dt/t≥(1/3)(3/4)=1/4 proves α≥1/4. Since (3/2)v≤1, ε≤200exp(−x/4). For x≥160,

                         ε≤x^(−4).                         (C6)

Indeed x⁴exp(−x/4) decreases for x≥16, and
200·160⁴=131072000000<1099511627776=2⁴⁰<exp(40).
This proves C6 without a numerical exponential estimate.

Writing d=(17/8)v² and e_tail=(3/2)v²ε, the denominator and right side in C5 become

1−u,  u=v/x+(d+e_tail)/x²,
R=x³+2vx²+[8/(9v)]x+26/9+ε[(3/2)vx²+4/3].

In particular0<u<1/2 for x≥160. Set Y=x³+3vx²+4x. Exact expansion yields

Y(1−u)−R
=[4−(41/8)v²−8/(9v)]x
 −4v−3vd−4d/x−26/9
 −ε[(3/2)v²x+(9/2)v³+6v²/x+(3/2)vx²+4/3].

Using3/5≤v≤2/3 gives the coefficient of x at least13/54. Also d≤17/18, so

4v+3vd+26/9 ≤67/9,  4d/x≤1.

By C6, the last ε-bracket is at most

x^(−2)+(2/3)x^(−3)+(8/3)x^(−4)+(8/3)x^(−5)<1.

Consequently

Y(1−u)−R ≥13x/54−85/9>0  for x≥160.

Equation C5 and1−u>0 imply m<Y, proving C1. Finally3v<2 follows exactly from π²<32/3, itself implied by(22/7)²<32/3. The coefficient is an exact radical involving π, not a fitted decimal.

## Verification scope

The complete capacity proof is local in COMMON_CAPACITY.md. The first-moment optimization and full-class limitation are local in KERNEL_FUNCTIONAL.md. The checker check_sonar_cosine.js verifies the rational parameter envelopes, exponential endpoint arithmetic and positive final margin. It does not replace the analytic proof or certify novelty. The independent exact combinatorial model checks are supplied separately by check_sonar.js.
