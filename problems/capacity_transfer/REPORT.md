PROVED — all six mathematical transfers survive adversarial review, with the repairs below and explicit remainders. The all-N square supplement is complete. StageC also yields a rigorously admissible kernel strictly below the nonnegative-factor optimum. The exact infimum over the full kernel class remains OPEN.

# Capacity-method transfers: final proofs and verification record

This is informed OpenAI review of the Claude scout, followed by full proof writing. Three isolated Claude reports now pass the cosine sonar theorem, the three one-dimensional transfers, triangular sonar, Manhattan, general boxes and the kernel functional/admissibility claims. The perturbed sonar consequence passes with editorial repairs applied. This is cross-vendor review of the OpenAI proofs and repairs; the scout's initial ideas and the Claude referees share a vendor. The all-N square supplement has in-team review but was outside the Claude reading lists. No new Lean formalisation, human referee, novelty certification or publication is claimed. The earlier Lean theorem for the ordinary Sidon bound remains a separate verified result.

## 1. Exact results and referee verdicts

In all size bounds, the combinatorial variables are integers; all roots and powers are positive real ones. The Manhattan diameter parameter may be real. Sidon sums include diagonals except in the explicitly weak model. Every theorem is uniform over the stated finite sets/configurations.

Put θ=1/10000000,

R=1−(129/8)θ−508θ²,
vθ=[(π²/36)R]^(1/3),
γ=2sqrt2/3,
Φ(k)=(sqrt(4k+8/9)−γ)/2.

| Item | StageA verdict | Proved explicit statement | Proof |
|---|---|---|---|
| Sonar: n rows, m columns, exactly one point per column, unique nonzero displacement vectors | PASS-WITH-REPAIRS | m≤n+2n^(2/3)+3n^(1/3) for n≥48³; refined to m≤n+3vθ n^(2/3)+8n^(1/3) for n≥160³ | [Base](SONAR.md), [cosine](SONAR_COSINE.md), [strict perturbation](KERNEL_PERTURBATION.md) |
| Weak Sidon: off-diagonal unordered sums unique | PASS-WITH-REPAIRS | k<√N+sqrt(8/3)N^(1/4)+2 for N≥90⁴ | [Weak Sidon](WEAK_SIDON.md) |
| g-thin: every nonzero ordered difference has at most g representations | PASS | k<√(gN)+γ(gN)^(1/4)+1 for gN≥120⁴, every integer g≥1 | [g-thin](G_THIN.md) |
| Difference triangle sets: n rows of k+1 marks, globally unique positive within-row differences | PASS-WITH-REPAIRS | m(n,k)>nΦ(k)⁴ for all n≥1,k≥20365; also m≥n[k²−(4sqrt2/3)k^(3/2)+(16/9)k−2√k] | [DTS](DIFFERENCE_TRIANGLES.md) |
| Manhattan DDC: unique ordered nonzero vectors, pairwise Manhattan distance≤r | PASS-WITH-REPAIRS | m≤r/sqrt2+(4/3)^(1/3)r^(2/3)+9r^(1/3) for r≥160³ | [Manhattan](MANHATTAN.md) |
| Strong Sidon in [N]^d, d≥2 | PASS-WITH-REPAIRS | k≤N^(d/2)+c_d N^(d²/(2d+2))+2d²N^(d(d−1)/(2d+2)), where c_d=((d+1)/2)(8/9)^(d/(d+1)), if N^(d/(2d+2))≥max(120,4d) | [Boxes](BOXES.md) |

The sonar cosine theorem without the perturbation has coefficient3(π²/36)^(1/3), smaller remainder4n^(1/3), and the same onset160³. The perturbation improves the asymptotic coefficient strictly; its displayed remainder is larger. Neither is described as pointwise superior at every finite n.

For d=2, [BOXES_ALL_N.md](BOXES_ALL_N.md) also proves k≤N+(8/3)^(1/3)N^(2/3)+18N^(1/3) for every integer N≥1. An exact square-window argument gives k≤N+(3/2)N^(2/3)+(7/2)N^(1/3) at every N; a rational splice with the capacity theorem at N=120³ gives the displayed all-N result.

All analytic dependencies are included locally in [COMMON_CAPACITY.md](COMMON_CAPACITY.md): the full ramp autocorrelation proof, signed half-line correction, exponential tail, exact potential and interval-energy certificate. The individual notes prove their own counting, scaling, algebra and errors. Real interval parameters are justified directly, rather than applying an integer theorem outside its domain.

## 2. Substantive repairs to the scout

- **Sonar:** the exact-marginal inequality(S) is valid. One must establish its horizontal energy Λ>0 before cancellation, push the signed certificate forward without multiplying its mass, and solve the inequality linearly in m. Assuming m=n+O(n^(2/3)) in order to derive it would be circular. The numerical +2.62 remainder is replaced by proved constants.
- **Weak Sidon:** the cross-sum pair can be diagonal in the allowed three-term progression case. Splitting that case proves r(d)≤2, with each repeated difference arising from one progression. Its middle point is unique across different progression differences, giving |P|≤k−2 only for k≥2. Empty and singleton sets are handled separately. The +2 and90⁴ onset are now supported by an exact exponential certificate and a uniform positive quadratic margin.
- **g-thin:** the scout's scaling is valid. This is a difference-multiplicity theorem, not the different B₂[g] sum-representation problem. The diagonal contribution is not multiplied by g. The new note spells out all scales and a real-parameter scalar lemma; no substantive failure was found.
- **DTS:** the scope quotient m/n need not be integral. The scalar proof is now valid for real parameters. Using the actual closed interval[0,m] removes the scout's unnecessary final−1. Cross-row differences are never inserted into the energy sum. The onset20365 is verified by exact integer comparisons.
- **Manhattan:** the scout's final two-term display omitted its O(r^(1/3)) error. A +9r^(1/3) term is now proved. The coordinate transform puts differences in the index-2 lattice even if translated points lie in its other coset. The exact second coefficient simplifies to(4/3)^(1/3).
- **Boxes:** the asymptotic claim needs fixed-d quantifiers and a dimension-dependent error. The note supplies both, and proves the sharper lattice bound Σ_j f(j/T)≤T+1/(2T) for T≥1 by an exact polynomial identity.

All products use finite signed certificates. Their energies are nonnegative because the kernels are positive definite, so product inequalities and signed Cauchy–Schwarz are valid. Separately, pointwise nonnegativity justifies adding missing difference vectors.

## 3. Kernel functional: what is actually optimized

[KERNEL_FUNCTIONAL.md](KERNEL_FUNCTIONAL.md) proves

inf_{h≥0, ∫h=1, f=h*h~} f(0)∫|t|f(t)dt = π²/32,

attained by h(t)=(π/2)sin(πt) on[0,1], up to translations/dilations. The proof uses the exact identity∫∫|x−y|h(x)h(y)=2∫F(1−F) and Cauchy–Schwarz with∫_0^1 sqrt(u(1−u))du=π/8. It does not infer global minimality from a stationarity equation.

This optimum is restricted to nonnegative factors. The coordinator's039a tail-perturbation suggestion led to the concrete construction in [KERNEL_PERTURBATION.md](KERNEL_PERTURBATION.md). With δ=1/16, bδ(x)=δ^−1f₀(x/δ),

fθ=f₀+θ[bδ(x−2)+bδ(x+2)−2bδ(x)]

has mass1 and is pointwise nonnegative. Its Fourier transform is nonnegative because the ratio of its subtracted Fourier term to f₀_hat is uniformly at most4210704, and θ times that constant is less than1. Its functional value is exactly(π²/32)R<π²/32. A complete bounded-variation lattice estimate and all-real tail/algebra calculation give the stated refined sonar theorem.

For the full class of even nonnegative positive-definite unit-mass kernels, the proved bounds are

1/4+1/(18π²) ≤ inf f(0)∫|t|f(t)dt ≤ (π²/32)R < π²/32.

The lower bound uses the negative Fourier coefficient of the mass-one box and an exact moment-distance estimate. The exact full-class infimum and a matching optimizer remain OPEN. The coefficient optimization proved here is specifically for the leading expression MT+b_y U+a a_y n²/(TU), with the stated horizontal class and the vertical ramp (or the finite-intercept class in the linked one-dimensional capacity theorem). It does not cover non-product two-dimensional kernels, arbitrary sampling errors or additional information beyond this inequality. This scope incorporates referee A's required wording repair R2.

A known marginal can be exploited more generally: if μ on X×Y has X-marginal λ, and a signed ψ-certificate on Y has energy≤C and unit potential, then the product test measure gives E_(φ⊗ψ)(μ,μ)≥E_φ(λ,λ)/C. For the other unrestricted models their spatial marginals are not prescribed. Replacing the unknown marginal energy by its capacity bound returns the original product estimate. Equal row masses in DTS are already exploited by summing separate row energies; cross-row constraints cannot be invented.

## 4. Executed exact checks

The root independently executed each completed checker and inspected the corresponding proof. All runs below exited0/PASS. They use dependency-free JavaScript/BigInt; no solver, local Lean build or installed dependency was used.

| Checker | Actual checked scope |
|---|---|
| [check_sonar.js](check_sonar.js) | 820 marginal identities,60 lattice checks,1070 small sonar prefixes,41856 energy/certificate cases,20 exact power enclosures; non-sonar negative control rejected |
| [check_weak_sidon.js](check_weak_sidon.js) | all16384 subsets of14 positions,2048 weak Sidon sets,16384 energies,1558 repeated-difference instances; exact exponential/onset certificate |
| [check_g_thin.js](check_g_thin.js) | all4096 subsets of12 positions,7521 admissible set/g pairs,60168 energies,54 rational substitutions |
| [check_difference_triangles.js](check_difference_triangles.js) | 687 compatible row families,4122 energies,72 substitutions including54 nonintegral interval parameters; exact20365 onset |
| [check_manhattan.js](check_manhattan.js) | 72 rational lattice cases,4096 subsets of a4×3 grid,721 DDCs,3605 energies |
| [check_boxes.js](check_boxes.js) | exact symbolic lattice identity,292 rational lattice cases,21 dimension/error cases,768 subsets,341 Sidon sets,1705 energies |
| [check_sonar_cosine.js](check_sonar_cosine.js) | 16 exact rational checks, including certified π brackets and uniform tail/denominator/margin bounds |
| [check_kernel_perturbation.js](check_kernel_perturbation.js) | 29 exact rational checks of the admissibility constants, strict product decrease and all-real sonar envelopes |
| [check_boxes_all_n.js](check_boxes_all_n.js) | 530 square-grid subsets,199 strong Sidon subsets,3180 exact window energy identities,1194 Sidon energy inequalities,1004 exact ceiling checks,2 polynomial identities and rational splice margins |

The six combinatorial checkers cover127840 finite configuration/scale energy-accounting cases in total. They are not evidence for the capacity step: the Manhattan and box scripts never evaluate that certificate, and the small-parameter sonar sandwich checks have a tail allowance too large to stress it. Their useful scope is exact identities, lattice sums, combinatorial accounting and scalar algebra. The analytic and uniform proofs supply the theorems. The first-moment exploratory grids are explicitly separated from these exact checks in KERNEL_FUNCTIONAL.md. Model-token usage and monetary cost are not exposed, so no cost estimate is asserted.

## 5. Source comparisons and remaining external gates

The coordinator's [bounded G2 report](G2_TRANSFER_20261002.md) is separate from this proof audit. Its corrections in039b are accepted as source-status findings with that provenance; no new novelty search was performed here.

- Sonar comparisons should name Osorio–Ruiz–Trujillo–Urbano2014, Theorem2.1 (located coefficient3.78), and distinguish the EGRT1992 coefficient3 remark from a printed proof. The unread main pages of Chen–Kløve1996, the sonar part of Robinson1985 and the Caicedo thesis remain access gaps in that report. We do not write “best known” or claim priority.
- The weak-Sidon comparison is to BFR arXiv2103.15850v2, Theorem5.1; the Monthly version is not substituted for that source.
- The g-thin statement is a direct corollary of the improved scalar bound and should not be packaged as an independent mechanism.
- DTS and Manhattan comparisons must retain the named-source/theorem and access qualifications in G2.
- For d=2, coefficients3/2 and1.9 were located in secondary reports of Robinson1985 and Caicedo2016. For d≥3, the status of earlier explicit constants remains unresolved. The proof above is independent of that record question.

The isolated [Claude referee A report](REFEREE_SONAR_CLAUDE_A_20261002.md) passes the cosine sonar theorem C1, the capacity input, K1 and K2. Its required R2 scope repair and optional logarithm, continuity, factor-class example and notation repairs have been applied with dated revision notes. The report's same-vendor label conflicts with the actual OpenAI-author/Claude-reviewer provenance confirmed in039c and040; its source text is preserved. The [one-dimensional report](REFEREE_1D_CLAUDE_20261002.md) passes weak Sidon, g-thin and DTS. The [two-dimensional report](REFEREE_2D_CLAUDE_20261002.md) passes triangular sonar, Manhattan, general boxes, the kernel functional and the perturbation's admissibility; the perturbed sonar theorem passes with editorial repairs now applied in KERNEL_PERTURBATION.md. The repairs inline the variation bound, exact marginal cancellation and all-real exponential estimate. Numerical experiments in these reports are referee-reported evidence, not root reruns or interval certificates. No external publication or community message was performed by this task.

Task039 proof delivery is complete with StageC's exact full-class infimum explicitly open. The coordinator's proposed presentation is mathematically sound: use the clean cosine coefficient as the main sonar statement, and present the perturbation as a proposition disproving full-class optimality of π²/32, with its refined sonar bound as a secondary consequence.
