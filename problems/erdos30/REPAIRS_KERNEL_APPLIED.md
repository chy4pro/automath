DONE — referee A's R1/S1/S2 were independently checked and applied to the proof report and manuscript v2; root integration review passed. No TeX compilation was available.

# Referee A repairs applied to the kernel optimality proof

Date: 2026-10-02. Task 033. Status: APPLIED; coordinator review pending.

The complete referee A report, the Task 033 instruction, the optimality
proof, and the Task 031 manuscript were read. Referee A (Claude Opus)
returned PASS-WITH-REPAIRS: the original core capacity theorems were
correct; R1 supplied a missing scope argument, and S1/S2 were optional
strengthenings. All three were independently checked and applied to
KERNEL_OPTIMALITY.md and main_v2.tex.

## R1: fixed-scale expansion → simultaneous all-scale comparison

Old text:

> For a fixed admissible kernel write x=N^(1/4), T=t x^3 with fixed t>0.
> The positive root of this quadratic is
> x^2 + (bt+a/t)x/2 + o(x).

This remains valid but by itself covers only fixed t.

New text (report Section 7.2 and manuscript all-scales lemma):

> Let beta=liminf(C_f(L)-L). For every real theta<sqrt(a beta), where
> beta=infinity permits every finite theta, all sufficiently large N
> have k_N=floor(N^(1/2)+theta N^(1/4)) satisfying
> k_N^2 <= C_f(N/T)[a(k_N-1)+T] for EVERY T>0.
> The threshold in N is independent of T.

Actual verification: choose finite 0<B<beta with sqrt(aB)>theta and
L_0 such that c(L)=C_f(L)-L>=B for L>=L_0. For 0<L<=L_0,

    c(L)/L >= M_1(L)/L >= M_1(L_0)/L_0 = eta >0,

so the scalar right side is at least N(1+eta)>k_N^2 for large N.
For L>=L_0, expansion and AM–GM give, uniformly in L,

    (L+c(L))[N/L+a(k_N-1)]
      >= N+NB/L+a(k_N-1)L
      >= N+2sqrt(aBN(k_N-1))
       = x^4+2sqrt(aB)x^3+O(x^2).

Compare k_N^2=x^4+2theta x^3+O(x^2). The floor contributes only
O(1) to k_N, and k_N-1>=0 for large N. The error constants are
independent of L and hence of T. With finite intercept, beta=b and
theta=sqrt(ab)-epsilon gives the referee's comparison for every
epsilon>0. To refute a putative smaller scalar upper coefficient c,
choose c<theta<sqrt(a beta), also overcoming any fixed additive term.

The texts explicitly identify these as scalar comparison integers,
not constructed Sidon sets.

## S1: finite intercept → unrestricted extended liminf capacity theorem

Old text:

> f is any even, nonnegative member of C_0(R) intersect L1(R),
> integral f=1, a=f(0)>0, and C_f(L)=L+b+o(1) with finite b.
> Then ab>=8/9.

New text:

> Let f be any even, nonnegative member of C_0(R) intersect L1(R),
> with integral f=1 and a=f(0)>0. Define
> beta(f)=liminf_{L->infinity}(C_f(L)-L), allowing infinity.
> Then beta(f)>=8/(9a). No finite intercept, unit-slope hypothesis,
> autocorrelation representation, positive definiteness, or sampling
> assumption is required. A finite intercept gives beta=b and ab>=8/9.

Actual verification: C_f(L)-L>=M_1(L) and M_1(L) increases to m_1.
If m_1=infinity, beta=infinity proves the conclusion. If m_1<infinity,
the existing boundary-energy expansion requires no intercept; take
liminf in the positive variational bound. The exact scaling identities

    C_fell(L)=C_f(ell L)/ell, beta(f_ell)=beta(f)/ell

hold also for extended beta. The same quadratic maximization gives
beta>=8/(9a). The ramp has beta=b=2/3 and a=4/3, so the sharp
infimum of a beta remains 8/9. The renewal certificate and explicit
ramp remainder did not need repair.

The abstract, introduction, theorem, moment dichotomy, scaled certificate,
and equality-condition wording were updated consistently. The original
finite-intercept result remains a corollary.

## S2: upper sampling assumption → separate lower bound from unit slope

Old text:

> For application to Sidon sets also require the sampling bound
> sum_{d>=1} f(d/T) <= T/2+O(1).

The earlier limitation discussion inherited this sufficient hypothesis.

New text:

> Under the separate hypothesis limsup_{L->infinity} C_f(L)/L<=1,
> S_T=sum_{d in Z}f(d/T)>=T for every T>0.
> No upper sampling bound is required for this conclusion.

Actual verification: S_T=infinity is immediate. Otherwise, with
mu_n=n^(-1)sum_{j=0}^{n-1}delta_(j/T),

    E_f(mu_n,mu_n)
      =n^(-2)sum_{|d|<n}(n-|d|)f(d/T) <= S_T/n,
    C_f((n-1)/T) >= n/S_T.

Divide by (n-1)/T and apply the unit-slope upper limsup to obtain
S_T>=T. The exact full-sum majorant is a(k-1)+S_T, which is at least
a(k-1)+T. R1 therefore gives simultaneous scalar non-exclusion for
all T without any upper sampling estimate.

The hypotheses and limitations are separated explicitly:

- The capacity theorem needs neither a finite intercept nor unit slope.
- The full-sum method limitation states unit slope explicitly; a finite
  intercept is one sufficient condition. No additional implication from
  the liminf hypothesis is used or asserted in this proof.
- Upper sampling control remains a sufficient ingredient for producing
  an effective/asymptotic Sidon upper bound.
- The limitation uses the FULL infinite lattice difference sum. It does
  not cover replacing that sum by a truncated sum over d<=N.
- No lattice-restricted capacity extension, unrestricted method barrier,
  N-dependent kernel assertion, uniqueness theorem, or solution of the
  original conjecture was added.

## Provenance: pending placeholder → A applied, B pending

Old manuscript text:

> Cross-vendor referee verdicts on the optimality section:
> PENDING---placeholder for the new reports.

New manuscript text:

> Cross-vendor referee A (Claude Opus): PASS-WITH-REPAIRS,
> repairs applied.
> Cross-vendor referee B: PENDING.

The earlier two Claude PASS reports concern the v1 explicit upper bound
and are not transferred to the new theorem. Referee A's reported
numerical checks were not rerun here and are not certified numerical
proofs. No fresh referee verdict after these edits is claimed.

The root reviewer informed the integration worker that
REFEREE_KERNEL_B_20261002.md is now available. The integration worker
did not read or incorporate it; the root subsequently read its PASS
verdict and qualifications. Task 033 explicitly requires retaining the
B-pending manuscript placeholder, which is left for coordinator update.
B's floating-point experiments were not rerun or certified here. In
particular, sampling the potential on a finer grid does not by itself
certify a lower bound for its minimum on the whole continuum interval.

## Checks actually performed

The three arguments were checked directly, including all inequality
directions, finite/infinite cases, the diagonal convention, uniformity
over T, and the separation of capacity and method hypotheses.
No numerical quadrature, optimizer, solver, or referee scratch script
was run. No new literature or priority check was performed. The v1
onset and bibliography were preserved, not independently re-certified.

- Static comparison: v1 Statement through the end of the constant section is byte-for-byte unchanged (24,299 bytes).
- All 16 v1 theorem/lemma/proof blocks are present verbatim.
- The bibliography is byte-for-byte unchanged.
- LaTeX static checks: no duplicate labels, unresolved references, or unmatched environments. The abstract has 112 whitespace-delimited words (limit 170).
- main.tex SHA-256 remains 168e28b0fcbe8a5ec635aa7f8ee2d091a70010caf6cec615540e7b016ee5df52.
- No TeX compilation was performed.

The root integration review separately checked the strengthened theorem,
the finite/infinite moment split, extended-real scaling, the small-L and
large-L comparison uniformly in T, and the unit-slope lattice argument.
It found no mathematical repair necessary. The report-start status and
the attribution of the notification about referee B were corrected here.

The integration worker wrote only KERNEL_OPTIMALITY.md, main_v2.tex,
and this repair record. The root reviewed those files and records
completion in the protocol STATUS file. main.tex, the bibliography and
the v1 core were not changed. No git, compilation, dependency installation,
publication or external message was performed. No new worker was spawned
for this integration. Token and monetary costs were not exposed.
