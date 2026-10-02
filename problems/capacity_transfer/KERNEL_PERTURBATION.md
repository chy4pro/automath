PROVED — derivation and independent in-team adversarial review PASS. The BigInt rational checker passed. The full-class infimum is still OPEN; no new cross-vendor review or Lean formalisation of this perturbation is claimed.

# An explicit admissible kernel below the nonnegative-factor optimum

Let f₀ be the cosine autocorrelation in SONAR_COSINE.md, with a₀=π²/8, mass1, first absolute moment1/4, support[−1,1], and Fourier convention exp(−2πiξx). Put

δ=1/16,  θ=1/10000000,  bδ(x)=δ^−1 f₀(x/δ),
fθ(x)=f₀(x)+θ[bδ(x−2)+bδ(x+2)−2bδ(x)].             (P1)

This is a continuous, compactly supported, even, nonnegative positive-definite kernel of mass1. Its support is contained in[−33/16,33/16]. The exact values are

a=fθ(0)=a₀(1−32θ),
M=∫|x|fθ(x)dx=1/4+(127/32)θ,
aM=(π²/32)R,  R=1−(129/8)θ−508θ²,  0<R<1.       (P2)

Consequently π²/32 is NOT the full-class infimum. It remains the attained optimum for autocorrelations of nonnegative factors, as proved separately in KERNEL_FUNCTIONAL.md.

## 1. Pointwise nonnegativity and exact moments

The two added tails have supports disjoint from[−1,1]. Their signs are positive. On the only region where a negative correction occurs, |x|≤δ, the explicit formula for f₀ gives

f₀(x)≥a₀(1−δ)cos(πδ)≥a₀/2.

Indeed πδ<1/4 and cos u≥1−u²/2 give(1−δ)cos(πδ)≥465/512>1/2. Since bδ≤a₀/δ=16a₀, the subtracted quantity is at most32θa₀<a₀/2. Elsewhere the original f₀ and any added tails are nonnegative. Thus fθ≥0 everywhere.

Mass is unchanged because1+1−2=0. At zero only the central subtraction contributes. Because bδ is even, of mass1 and support[−δ,δ], each translate by±2 has first absolute moment2. The central bδ has first moment δ/4. This proves P2 by direct expansion; no numerical optimization is involved.

## 2. Positive definiteness with a uniform Fourier bound

For h(x)=(π/2)sin(πx) on[0,1],

h_hat(ξ)=exp(−πiξ)cos(πξ)/(1−4ξ²),
f₀_hat(ξ)=cos²(πξ)/(1−4ξ²)²,

with removable values at ξ=±1/2. Also

|h_hat(ξ)|≤min(1,1/(2ξ²)).                         (P3)

The first bound uses ||h||₁=1. For the second, the distributional second derivative of the zero extension of h has total variation2π²: the two endpoint jumps of h' contributeπ², and its ordinary second derivative contributesπ². Two integrations by parts divide this variation by(2π|ξ|)². Thus f₀_hat(t)≤min(1,1/(4t⁴)).

Taking Fourier transforms in P1 gives

fθ_hat(ξ)=f₀_hat(ξ)−4θsin²(2πξ)f₀_hat(δξ).

Where f₀_hat is nonzero, the ratio of the subtracted term before θ to f₀_hat is exactly

16sin²(πξ)(1−4ξ²)²f₀_hat(δξ).

Using P3, and splitting at ξ²=1/(2δ²), gives

(1−4ξ²)²f₀_hat(δξ)≤(1+2/δ²)².

For ξ² below the split, bound the first factor by(1+4ξ²)² and f₀_hat by1. Above it, use f₀_hat(δξ)≤1/(4δ⁴ξ⁴); the resulting expression is at most(1+2/δ²)² again. Therefore the ratio is at most

K=16(1+2/δ²)²=4210704.

Since θK<1, fθ_hat≥(1−θK)f₀_hat≥0. At the zeros of f₀_hat the subtracted sine factor also vanishes; continuity extends the inequality there and across the removable points. Fourier inversion is justified by the integrable fourth-power decay. A nonnegative integrable Fourier transform proves positive definiteness, completing the admissibility proof.

## 3. Explicit sonar consequence

Energy Cauchy–Schwarz for this new kernel follows directly by Fourier inversion: its nonnegative integrable Fourier transform represents energy as the weighted inner product of the transforms of two finite signed measures. Finite total variation and integrability justify Fubini. The product with the vertical ramp kernel has the same representation. No nonnegative autocorrelation factor for fθ is assumed.

Define

v=[(π²/36)R]^(1/3).

For every sonar sequence with n≥160³ rows and m columns,

m≤n+3v n^(2/3)+8n^(1/3).                           (P4)

Thus its second-order coefficient is strictly smaller than the nonnegative-factor value3(π²/36)^(1/3). The larger stated remainder means this is an asymptotic coefficient improvement; no claim of a better numerical bound at every n is made.

Here are complete lattice and error bounds. We have1≤a≤4/3 and1/4≤M≤1/3. The total variation of fθ is at most

2a₀+128θa₀<3.

For p(x)=|x|fθ(x), the unperturbed variation is at most2. Each shifted |x|bδ(x∓2) has variation at most1+(2+δ)·2a₀/δ, while |x|bδ(x) has variation at most2. Hence

Var(p)≤2+θ(6+132a₀)<3.

Lattice Riemann sums therefore satisfy

|Σ_d fθ(d/T)−T|≤3,
Σ_d |d|fθ(d/T)≤MT²+3T.

When(33/16)T≤m, the exact horizontal marginal energy is at least m(T−3)−MT²−3T. The off-diagonal horizontal lattice sum is at most T+3−a≤T+2. The vertical ramp lattice sum is at most U+4/3. The same signed-product-certificate argument as in SONAR_COSINE.md gives, with C=n/U+2/3+ε and ε=200exp(−αn/U),

m[1−3/T−(4a/3)C/T]≤MT+3+C(1+2/T)(U+4/3).          (P5)

Put x=n^(1/3), t₁=v/M, t₂=(3/2)v, T=t₁x², U=t₂x². The identity v³=(8/9)aM gives

(4a/3)/(t₁t₂)=v,  Mt₁=(2/3)t₂=v.

Here R>9/10 by its explicit rational formula, so π>3 gives v³>(1/4)(9/10)=9/40>27/125=(3/5)³. Also R<1 and π<22/7 give v<2/3. Thus9/5≤t₁≤8/3 and9/10≤t₂≤1. If m<n, P4 is immediate. Otherwise x≥160 gives(33/16)T≤(11/2)x²≤n≤m and U≤n. The same uniform tail proof as C6 gives ε≤x^−4.

Write the denominator in P5 as1−u, with

u=v/x+d/x²+eε/x²,
d=[3+(8/9)a]/t₁≤565/243<3,
e=(4a/3)/t₁≤80/81<1.

Then0<u<1/2 for x≥160. Expanding the right side of P5 and using a₂/t₂=8/(9v),2/t₁≤10/9 and M≤1/3 shows it is at most

R_upper=x³+2vx²+(70/27)x+8.                        (P6)

For completeness, after these first three terms the remaining positive quantities are bounded by

35/9+2M≤41/9,
[16/(9v)]/(t₁x)<1,
16/(9t₁x²)<1,
ε(t₂x²+4/3)(1+2/(t₁x²))<1,

whose sum is smaller than8. These estimates hold for all x≥160, not only integer x.

For Y=x³+3vx²+8x, direct multiplication gives

Y(1−u)−R_upper
≥[8−4/3−3−70/27]x−(16/3+6+1+8+1)
≥(29/27)x−22>0.

The terms bounded by1 here are8d/x and eε(x+3v+8/x), respectively. Equation P5 and1−u>0 now imply m<Y, proving P4 with a fully explicit error and onset.

## 4. Scope and remaining optimization question

This exact perturbation supplies an admissible full-class upper value(π²/32)R strictly belowπ²/32. Combining it with the general Fourier lower bound in KERNEL_FUNCTIONAL.md gives

1/4+1/(18π²)≤inf_full aM≤(π²/32)R<π²/32.

The exact infimum and a matching full-class optimizer/barrier remain OPEN. No LP grid, conjectured dual certificate, or unattained infimum is used to establish P1–P5.
