OPEN — task 030 in progress. No universal kernel-optimality theorem or improved kernel is claimed.

# Kernel optimality for the scalar Sidon energy inequality

Date: 2026-10-02. This report separates the precise optimization problem,
proved partial statements, clean-room investigations, route analysis, and
literature checks. Independent human review and kernel formalization are
not part of this task. Findings below remain subject to the task's final
adversarial checks.

## 1. The admissible class and the capacity convention

For definiteness take a real function h in L1(R) intersect L2(R), with
integral h = 1. Put h~(t) = h(-t), f = h*h~, and a = f(0) = ||h||_2^2.
Then f is even, continuous, tends to zero at infinity, is positive
definite, has integral 1, and |f| <= a. In addition require f >= 0.
The relevant capacity is

    C_+(L) = 1 / inf E_f(mu,mu),

where the infimum is over NONNEGATIVE Borel probability measures supported
on the CLOSED interval [0,L]. The energy of a finite measure is the double
integral of f(x-y). Require a finite boundary constant

    C_+(L) = L + b + o(1), as L -> infinity.

A second admissibility condition for the discrete application is

    sum_{d>=1} f(d/T) <= T/2 + O(1), as T -> infinity,

with a controlled error if an explicit Sidon bound is wanted. Monotonicity
of f on the positive half-line is sufficient but is not an assumption
forced by the application. Neither nonnegativity of h nor compact support
is logically required by the Sidon difference-counting step.

Minimizing energy over arbitrary finite SIGNED probability measures gives
a different capacity C_s(L), with C_s(L) >= C_+(L). Their boundary constants
must not be identified without proof. A signed comparison measure used
in Cauchy--Schwarz to bound E_f(mu,mu) is also not itself a proof that the
positive-measure capacity has the asserted asymptotic.

## 2. An unconditional lower bound for every kernel in this class

**Proposition (elementary universal partial bound).** The existence of the
finite positive-capacity boundary constant forces

    m1 := integral_R |x| f(x) dx < infinity,
    b >= m1 + 1/(2a),
    a b >= 3/4.

This is weaker than the proposed sharp value 8/9 and is not a resolution
of the optimization problem.

**Proof.** Let

    M(L) = integral_R min(|x|,L) f(x) dx.

The unnormalized Lebesgue measure lambda_L on [0,L] has mass L and energy

    E(lambda_L,lambda_L)
      = integral_R (L-|x|)_+ f(x) dx = L-M(L).

This energy is positive: f is continuous and f(0)=a>0, and hence positive
on a neighborhood of zero. The uniform probability measure therefore gives

    C_+(L) >= L^2/(L-M(L)) >= L+M(L).

Because C_+(L)-L tends to a finite b and M(L) increases to m1, monotone
convergence gives m1 <= b < infinity.

For any fixed c >= 0, use the positive trial measure

    sigma_L = lambda_L + c delta_0 + c delta_L.

Its mass is L+2c. The endpoints are distinct for L>0, and direct expansion
of all ordered cross terms gives

    E(sigma_L,sigma_L)
      = L-M(L) + 4c integral_0^L f(x) dx + 2c^2(a+f(L))
      = L-m1+2c+2ac^2+o(1).

Here integral_0^infinity f = 1/2 and f(L) -> 0. Normalize sigma_L to a
probability measure to obtain

    C_+(L) >= (L+2c)^2 / E(sigma_L,sigma_L)
            = L + m1+2c-2ac^2+o(1).

Taking limits and then c=1/(2a) proves b >= m1+1/(2a).
Finally 0 <= f <= a and integral f=1 imply

    integral_{|x|>r} f(x) dx >= max(1-2ar,0).

Layer-cake integration yields

    m1 >= integral_0^{1/(2a)} (1-2ar) dr = 1/(4a).

Combining the inequalities gives ab >= 3/4. All trial measures are
nonnegative; no signed-capacity assumption or spectral factorization is
used. QED.

## 3. Sufficient lattice regularity and the scalar asymptotic

If f has finite total variation V on [0,infinity), the needed lattice
estimate follows with an explicit error V:

    |sum_{d>=1} f(d/T) - T/2| <= V.

Indeed, on each interval I_d=[(d-1)/T,d/T],

    |f(d/T)-T integral_{I_d} f| <= Var_{I_d}(f).

Sum over finitely many cells, then pass to the limit. Nonnegativity and
integrability ensure convergence of the sums under this bound. Thus a
nonmonotone f is not automatically excluded. If f is nonincreasing, the
one-sided estimate has zero error instead.

For a Sidon set A of cardinality k, the diagonal terms have multiplicity k
and every positive difference has multiplicity at most one. Consequently

    E_f(sum_{u in A} delta_{u/T}) <= ak+T+2V,
    k^2 <= C_+(N/T)(ak+T+2V).

Assuming only C_+(L)=L+b+o(1), set x=N^(1/4), T=t x^3, with fixed t>0.
The monic quadratic in k first gives k=x^2+O(x), and expanding its positive
root then gives

    k <= x^2 + (bt+a/t)x/2 + o(x).

Here b>0 follows from Section 2. Minimizing over t gives t=sqrt(a/b) and
coefficient sqrt(ab). An o(1) capacity remainder alone gives an o(N^(1/4))
Sidon remainder, not a uniform additive O(1). For an additive O(1), a
sufficient quantitative condition is C_+(L)<=L+b+O(1/L). Explicit constants
and onset require explicit bounds on that remainder and on V.

## 4. A sharp moment theorem, with its capacity hypothesis visible

**Proposition.** Let p>=0 on [0,infinity), integral p=1, p in L2, and
0<m=integral t p(t)dt<infinity. Then

    ||p||_2^2 m >= 4/9.

Equality holds precisely, up to null sets, for

    p(t) = 2(R-t)_+/R^2,  R=3m.

**Proof.** For every R>m, positivity and Cauchy--Schwarz give

    R-m = integral_0^infinity (R-t)p(t)dt
        <= integral_0^R (R-t)p(t)dt
        <= ||p||_2 (R^3/3)^(1/2).

Hence ||p||_2^2 >= 3(R-m)^2/R^3. Taking R=3m gives the bound.
Equality in the first inequality requires p=0 almost everywhere on (R,infinity),
and equality in Cauchy--Schwarz requires p proportional to R-t on (0,R).
Normalization fixes the displayed factor; conversely this p attains equality.
QED.

It follows that in any class where the relevant f has a NONNEGATIVE CAUSAL
factor p of mass one and one has separately proved

    b = 2 integral_0^infinity t p(t)dt,

the sharp bound is ab>=8/9, with the ramp as the equality case. The moment
inequality by itself does not establish that capacity identity, and the
identity must use a correctly chosen factor: translation of p changes its
first moment while leaving f unchanged.

## 5. Positivity of f does not force positivity of a given causal factor

Here is an exact example relevant to the scope of Section 4, not a better
Sidon kernel. Set D=91/85 and

    h(t) = D^(-1) exp(-t)(1+(6/5)cos(4t)) 1_{t>=0}.

It is real, integrable, square-integrable, and has integral one. It changes
sign, since its parenthesis equals -1/5 at t=pi/4. Direct integration gives,
for x>=0,

    f(x)=D^(-2) exp(-x) [31/50 + (213/425)cos(4x)
                                      - (138/425)sin(4x)],

and f is extended evenly. The constant term exceeds the amplitude of the
oscillating part, as

    527^2 - 426^2 - 276^2 = 20077 > 0

after using the common denominator 850. Therefore f>0 everywhere. Its
derivative is integrable on the positive half-line, so it satisfies the
lattice estimate of Section 3 with finite variation. It is nonmonotone:
at x=3pi/8, the derivative's bracket equals

    -31/50 + 4(213/425) - 138/425 = 901/850 > 0.

The Laplace transform of the causal factor is the rational function

    H(s) = D^(-1) [ (11/5)(s+1)^2 + 16 ]
                       / [(s+1)((s+1)^2+16)].

Its zeros are -1 +/- 4i sqrt(5/11), and its poles all have real part -1.
Thus merely checking the absence of zeros in the closed right half-plane
also does not imply that h is nonnegative. No capacity asymptotic for this
example is being asserted here, and it does not disprove the target 8/9.
Its role is to show why the nonnegative-factor restriction is substantive.

## 6. Why a zero-free transform does not suffice

The following counterexample concerns a proposed sufficient hypothesis,
not the Sidon theorem or the target value of the optimization. Take

    p(t)=t exp(-t) 1_{t>=0},  H(s)=(1+s)^(-2).

The factor is nonnegative and causal, has mass one and finite first
moment, and H has no zero in the closed right half-plane. Nevertheless

    1/(sH(s)) - 1/s = 2+s.

This cannot be the Laplace transform of a finite signed measure q on the
positive half-line, since such a transform is bounded by ||q||_TV for
every real s>0. In distributional notation the inverse correction is
2 delta_0 + delta'_0. Thus absence of zeros alone does not justify the
finite-measure half-line construction or its total-variation estimates.
The specific ramp proof has a separately constructed renewal measure and
explicit tail estimates, so this caveat does not undermine that proof.

## 7. Bounded literature check

The literature-only worker read the following sources before consulting
any project proof, scan, or referee report. No checked source establishes
the global infimum in Section 1. This is a bounded search conclusion,
not an exhaustive novelty or priority certification.

* **Hou--Zhao, arXiv:2607.01169v3.** The relevant result is **Theorem 2.1**,
  not Lemma 2.1. It uses finite nonnegative symmetric probability kernels,
  mixing weights, and real boundary vectors subject to feasibility
  inequalities, producing a coefficient sqrt(ab). Section 3.1 poses its
  finite parameter optimization. Lemma 3.1 solves the boundary quadratic
  program only with kernels and mixing fixed. Proposition 2.2 assumes
  individually feasible constituent certificates. Section 3.4 expressly
  disclaims global optimality, including for its scalar numerical search.
  Its boundary cost is not identified with our exact continuous positive
  capacity correction. [Theorem 2.1](https://arxiv.org/html/2607.01169v3#S2.Thmtheorem1),
  [optimization](https://arxiv.org/html/2607.01169v3#S3.SS1),
  [limitations](https://arxiv.org/html/2607.01169v3#S3.SS4).

* **Carter--Hunter--O'Bryant, arXiv:2310.20032v1.** Theorem 1.1 is the
  Erdős--Turán Sidon Set Equality, retaining rectangular-window variance
  and weighted missing differences. Lemmas 3.1--3.2 exploit endpoint
  variance and several window lengths; Section 3.2.2 combines piecewise
  affine estimates by linear programming. The parameter search is local.
  No theorem about the infimum of the functional in Section 1 was found.
  Inference: this is related endpoint methodology, not a solution of our
  kernel variational problem.
  [Theorem 1.1](https://arxiv.org/html/2310.20032v1#S1.Thmtheorem1),
  [Section 3.2.2](https://arxiv.org/html/2310.20032v1#S3.SS2.SSS2).

* **Gupta--O'Bryant, arXiv:2605.14229v1, Theorem 13, Section 5.3.** For
  LM rulers, the positive difference d has multiplicity at most d-1.
  Sorting the n-1 consecutive gaps gives s_(i)>sqrt(2i); integration of
  sqrt(2t) then yields diameter at least (2sqrt(2)/3)(n-1)^(3/2).
  There is no autocorrelation, capacity or half-line optimization in
  this argument. Its identical coefficient does not solve, or certify
  an optimum for, the present problem.
  [Section 5.3](https://arxiv.org/html/2605.14229v1#S5.SS3).

* **Alfonsi--Schied, arXiv:1201.2756v4.** Section 1.1 distinguishes positive
  and signed energy minimization. Their explicit results concern
  completely monotone G, with G''(0+)<infinity for the main characterization.
  Corollary 1 describes endpoint atoms and a continuous interior density;
  Theorem 2 and Corollary 2 use Riccati and Volterra equations. Their
  energy includes a factor 1/2, so its reciprocal is twice our capacity
  for the same kernel. These are results for restricted fixed kernels,
  not optimization over all autocorrelations.
  [Primary paper](https://arxiv.org/pdf/1201.2756v4).

* **Leinster--Roff, arXiv:1908.11184.** Theorem 8.1 expresses magnitude
  using signed measures and the exponential metric kernel. Lemma 8.2
  identifies the positive problem when a positive weight measure exists.
  Example 8.4 gives the interval measure (delta_0+delta_l+Leb)/2 and
  magnitude 1+l/2. Lemma 7.7 and Proposition 6.3 concern the positive
  equilibrium potential inequality and its contact set. This supports
  retaining the positivity condition; it supplies no universal optimum
  for the kernels of Section 1.
  [Primary paper, Sections 7--8](https://arxiv.org/html/1908.11184).

* **Gimperlein--Goffeng--Louca, arXiv:2201.11357v2.** Theorems 1.1, 1.3,
  1.4 and Section 5.2 give boundary expansions and Wiener--Hopf analysis
  for exp(-R d(x,y)) on suitable compact manifolds with boundary. The
  inverse is constructed in Sobolev spaces and may be distributional;
  the associated energy formulation permits signed measures. Inference:
  this framework cannot be applied as a ready-made positive-capacity
  theorem for arbitrary f=h*h~.
  [Primary paper](https://arxiv.org/html/2201.11357).

* **Spectral-factor qualification.** Fejér--Riesz factorization does not
  assert nonnegative coefficients of its factor.
  [Dritschel--Rovnyak, p. 2](https://uva.theopenscholar.com/files/james-rovnyak/files/p71.pdf).
  Ewerhart--Serena, Definition 1, Lemma 2 and Section 2.4, discuss the
  stronger probability question of representing a distribution as X-Y
  for iid X,Y, and explain why a nonnegative characteristic function
  alone is insufficient. The older counterexample they cite was not
  independently inspected in this search.
  [Author-hosted paper](https://ewerhart.net/files/2024%20Ewerhart%20Serena%20MathOR%20On%20the%20(Im-)possibility%20of%20Representing%20Probability%20Distributions.pdf).

## 8. Work still in progress

Two fresh-context clean-room probes are investigating the variational
problem independently. The literature-only phase is complete. The platform
rejected both creation of a fourth worker thread and resumption of a
previously completed route worker with `agent thread limit reached`.
The completed literature worker therefore now runs a separately recorded
context-informed route phase. There are three worker identities, not four;
neither clean-room probe receives the literature or route analysis.
The coordinator's prior numerical scan and referee recommendations are
context for informed analysis only, not proof of global optimality.

## 9. Candidate universal dual certificate (under independent audit)

Clean-room probe B produced the following candidate proof. Independently,
probe A has reported the same all-kernel target with a positive renewal
construction; its final derivation is still awaited. This section is not
yet the report's final verdict.

Write C_f(L)=C_+(L). For positive finite measures nu supported on [0,L],
let M(nu) be the mass. Optimizing a scalar multiple of a probability
measure gives the exact variational identity

    C_f(L) = sup_{nu>=0, supp nu subset[0,L]} (2M(nu)-E_f(nu,nu)).

Use the uniform probability distribution W on [0,1] and its renewal
measure U=delta_0+sum_{n>=1} W^{*n}. Let

    v=U/2,  kappa=v-Leb_[0,infinity),  m=kappa(R)=1/3.

The density of U away from its atom is u. Elementary renewal contraction
gives u>=1 almost everywhere and u(t)=2+O(exp(-alpha t)),
alpha=log(4/3). In particular kappa is a finite signed measure with an
atom 1/2 at zero and an exponentially decreasing density k(t)=u(t)/2-1.
Its mass follows either from the elementary renewal proof or the expansion

    Laplace(v)(s)=1/[2(1-(1-exp(-s))/s)]=1/s+1/3+O(s).

For t>0 put T(t)=kappa([t,infinity)). Define an even measure of at most
linear growth

    B = [-|t|+2m+2T(|t|)]dt + 2 kappa*kappa~.

The central identity requiring audit is

    B = (1/2)delta_0 + D(t)dt,
    D(t)=0                       for 0<|t|<1,
    D(t)=-(1/2)R(|t|-1)          for |t|>1,
    R(s)=U([0,s]) for s>=0.

In particular D<=0. Here is the submitted derivation. With transform
convention integral exp(-i omega t), let Q(s)=(1-exp(-s))/s and K=kappa-hat.
For omega!=0,

    B-hat = 2/omega^2 - 4 Im(K)/omega + 2|K|^2
          = 2|K-i/omega|^2
          = 1/[2|1-Q(i omega)|^2].

Multiplication by i omega-1+exp(-i omega) yields, in physical space,

    B' - B + tau_1 B = (v~)',

where tau_1 translates a measure to the right by one. The submitted
Fourier argument says the multiplier's double zero at zero eliminates
the possible origin-supported delta/delta' ambiguity from the transform
of the linear-growth term. This step is being independently checked,
including a possible direct real-space derivation.

On (0,1), evenness gives D'=D-D(1-t), which forces D to be constant, d.
The atom of tau_1 B forces a jump -1/2 at t=1. For t>1, D'=D-D(t-1).
The function R has jump 1 at zero, obeys R'=R-R(t-1) for t>0, and
R(s)=2s+2/3+o(1). Thus D(t)=d-R(t-1)/2 for t>1. Directly from the
definition of B, D(t)=-t+2/3+o(1). Comparing constants gives d=0.

Now truncate the two boundary corrections to the interval and put

    nu_L = Leb_[0,L] + kappa|_[0,L] + reflection(kappa|_[0,L]).

The endpoint atoms are 1/2. Its interior density is
u(x)/2+u(L-x)/2-1>=0, so this is a positive trial measure. Its mass is
L+2/3+o(1). For every f in Section 1, the necessary first moment from
Section 2 justifies expansion of its energy:

    E_f(nu_L,nu_L) = L + integral_R f(t)dB(t) + o(1).

The four contributions to the constant term are, respectively,

    -integral |t|f(t)dt                       (uniform--uniform),
    2m + 4 integral_0^infinity f(t)T(t)dt     (uniform--boundary),
    2 integral f d(kappa*kappa~)             (same-end boundary),
    0                                       (opposite-end boundary).

The last term tends to zero because kappa has finite total variation
and f belongs to C_0. The integral involving R is finite because R grows
at most linearly. The candidate identity for B gives

    E_f(nu_L,nu_L)
      = L+a/2-(1/2)integral_{|t|>1} f(t)R(|t|-1)dt+o(1).

The positive variational formula then implies

    b >= 4/3-a/2+(1/2)integral_{|t|>1} f(t)R(|t|-1)dt
      >= 4/3-a/2.

Rescale the renewal construction by a length ell>0 while preserving
interior density one: kappa_ell=ell times the pushforward of kappa under
t -> ell t. Its mass is ell/3 and its endpoint atom is ell/2. The pair
correction becomes ell^2 times the pushforward of B, hence

    b >= 4ell/3 - a ell^2/2
          + (ell/2) integral_{|t|>ell} f(t)R(|t|/ell-1)dt
      >= 4ell/3-a ell^2/2.

Taking ell=4/(3a) would prove ab>=8/9 for the full class, without any
nonnegative-factor or signed-capacity hypothesis. Ramp attainment still
requires the actual positive-capacity asymptotic, whose proof is being
checked by the route worker.
