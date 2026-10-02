# PROBE A — clean-room attempt to beat c = 2√2/3 in k ≤ √N + c·N^{1/4}

Clean-room: no web, no papers, no project files read. Only the statement in the brief plus standard
mathematics (Bochner positivity, Fejér–Riesz, Poisson summation, LP duality). Numerics: python3 +
numpy/scipy (HiGHS LP), ≤ 2 threads. Scripts are in the session scratchpad `probeA/` (not in the repo);
the load-bearing formulas are reproduced below so everything can be re-derived without them.

**STATUS: PARTIAL — no c < 2√2/3 is proved.** What is proved: a general certificate inequality (1.1)
that contains the scalar argument; a finite-N certificate that beats the ramp bound by ≈ 0.1 at
N = 10⁴ (not an integer improvement); and that ideas (3), (4), (5) and 3-point counting are slack or lossy
at order N^{1/4}. What is numerical evidence only: everything that uses positivity of |μ̂|² plus
0 ≤ R(d) ≤ 1 (this covers ideas (1)-linear and (2)) is capped at c_LP ≈ 0.937–0.939 (bracket
[0.934, 0.9428]), so that whole family can gain at most ≈ 1% over 2√2/3. A real improvement needs non-LP
input; the candidate is the fluctuation bound (8.1).

---------------------------------------------------------------------------------------------------

## 0. Notation

A ⊆ {1,…,N} Sidon, k = |A|, μ = Σ_{a∈A} δ_a. Autocorrelation (ordered pairs, diagonal included)

  R(d) = #{(a,a′) ∈ A² : a − a′ = d},  so R(0) = k, R(d) ∈ {0,1} for d ≠ 0, R(d) = 0 for |d| ≥ N,
  Σ_d R(d) = k²,  R̂(ξ) := Σ_d R(d) e(dξ) = |μ̂(ξ)|² ≥ 0 for every real ξ.        (0.1)

The brief's scalar argument: for f = h*h̃ ≥ 0, ∫f = 1, E = Σ_{a,a′} f((a−a′)/T) satisfies
(i) E ≤ k f(0) + T and (ii) E ≥ k²/(N/T + b_f); optimising T gives c = √(f(0) b_f) ≥ √(8/9).

---------------------------------------------------------------------------------------------------

## 1. The LP that contains every scalar argument (Delsarte-type relaxation)

**LP(N).** Variables R(d) (d ∈ ℤ, |d| < N, R even). Constraints: R(0) = k; 0 ≤ R(d) ≤ 1 (d ≠ 0);
R̂(ξ) ≥ 0 for all ξ; Σ_d R(d) = k². Let k_LP(N) be the largest feasible k. Every Sidon set gives a
feasible point, so k ≤ k_LP(N).

Remarks (proved, standard):
* By Fejér–Riesz, a nonnegative trigonometric polynomial of degree N−1 is |p|² with p a real polynomial
  of degree N−1. So LP(N) is exactly: "real (signed) weights g on {1,…,N} with Σg = Σg² = k and
  autocorrelation in [0,1] off the diagonal". The relaxation forgets (a) g ∈ {0,1}, (b) g ≥ 0,
  (c) everything about sums a+a′ beyond what |μ̂|² sees.
* The scalar argument is a feasible dual certificate of LP(N): both (i) (uses only 0 ≤ R(d) ≤ 1 and f ≥ 0)
  and (ii) (energy of a signed measure on an interval; for the ramp the equilibrium measure is positive —
  checked numerically, min density ≈ 0.48× the mean, so signed and positive capacities agree) hold for
  every LP-feasible R. Hence **k_LP(N) ≤ scalar bound**, and the question "does LP(N) beat 2√2/3?" is
  exactly "is there a better certificate that still uses only (0.1)?".

**General dual certificate (proved, elementary).** Let G(x) = Σ_m ν_m cos(2π η_m x) with ν_m ≥ 0
(finitely many atoms, any real η_m). Then by (0.1), Σ_d R(d) G(d/N) = Σ_m ν_m R̂(η_m/N) ≥ 0, so

  k² − k = Σ_{d≠0} R(d) = Σ_{d≠0} R(d)(1 + G(d/N)) − Σ_{d≠0} R(d) G(d/N)
         ≤ Σ_{0<|d|<N} (1 + G(d/N))₊ + k·G(0).                                        (1.1)

(1.1) is exact for every N and every such G (it uses only R(d) ∈ [0,1] and R̂ ≥ 0). The scalar
argument is the special case G = (F/c) − 1 on [−1,1] with F(x) = f(Nx/T) and c = 1/capacity, where G is
a positive-definite extension of F/c − 1 from [−1,1] (exists by LP duality for the capacity problem).

---------------------------------------------------------------------------------------------------

## 2. Scaling limit of LP(N): a one-parameter Turán-type problem

Put R(d) = φ(d/N) with φ: [−1,1] → [0,1] even, and ε := (k−1)/N ≈ N^{−1/2}. Using Σ_{d≠0} φ(d/N) e(dξ)
= N φ̂(Nξ) − φ(0) + (aliasing), the constraint R̂ ≥ 0 becomes φ̂(η) ≥ −ε, and Σ_{d≠0}R(d) = N∫φ − 1.
So the continuum problem is

  P(ε):  1 + Δ(ε) := max ∫_{−1}^{1} φ  s.t. 0 ≤ φ ≤ 1 on [−1,1], φ = 0 outside, φ̂ ≥ −ε,       (2.1)

  dual:  1 + Δ(ε) = inf_{G pos.-def.} [ ∫_{−1}^{1} (1 + G(x))₊ dx + ε G(0) ],                  (2.2)

and k² − k + 1 = N(1 + Δ(ε)). If Δ(ε) = C√ε (1+o(1)) then k = √N + (C/2) N^{1/4} + O(1).
**c_LP = C/2.** For an upper bound only the dual side matters, and (1.1) turns any G into a rigorous
finite-N inequality (the Riemann-sum error in Σ(1+G(d/N))₊ vs N∫(1+G)₊ is O(total variation of
(1+G)₊) = O(G(0)) = O(N^{1/4}), harmless at the N^{3/4} scale).

Scalar argument in this language: G = F/c − 1 with F = f(x/τ), τ = T/N, c = 1/(1/τ + b):
∫(1+G)₊ = τ·cap = 1 + bτ, εG(0) = ε(f(0)(1/τ + b) − 1), so Δ ≤ bτ + εf(0)/τ + ε(f(0)b − 1);
optimum Δ_scalar(ε) = 2√(f(0)b ε) + ε(f(0)b − 1) = 1.88562√ε − ε/9 for the ramp. C_scalar = 4√2/3.

Primal sanity check (proved by direct computation): φ = min(1, 1+δ−|x|)·1_{|x|≤1} has
φ̂(m/(1+δ)) ≈ −δ²(1 + cos 2πmδ) ≥ −2δ², so δ = √(ε/2) is feasible to leading order and
Δ ≥ 2δ = √2·√ε (a leading-order computation; the reduced problem of §5 reproduces β ≤ 1/√2 for this
shape). Hence, to leading order, **C_LP ∈ [√2, 4√2/3] = [1.414, 1.886]**, i.e. c_LP ∈ [0.707, 0.943].

---------------------------------------------------------------------------------------------------

## 3. What the scalar argument's equality case looks like (structure that any improvement must attack)

Equality in (ii) needs μ ≈ k·(equilibrium measure of [0,N] for f(·/T)); equality in (i) needs R(d) = 1 for
all 0 < |d| < T. Numerically (discrete equilibrium, linear solve K w = 1, N = 2000–3000, T = 100–300):

* ramp capacity − N/T = 0.640, 0.644, 0.656, 0.663 (→ 2/3 as T→∞, from below); equilibrium is positive;
* **the ramp equilibrium has an atom at each endpoint of mass ≈ 0.49·T × (mean density)** (0.4865T,
  0.4701T, 0.4918T in the three runs), then density ≈ 0.49 of the mean on (0,T), a peak ≈ 1.3 at T,
  ≈ 0.83 after T, … (decaying oscillation of period T); flat-window kernel: atoms at all multiples of T.

So a set attaining the scalar bound would have, at the optimal T = √2·N^{3/4}, a cluster of
≈ 0.49·√2·N^{1/4} ≈ 0.69·N^{1/4} elements within o(T) of each endpoint, a density dip/peak profile at
scale T, and every difference < T realised. A Sidon cluster of m elements needs length ≳ m² ≈ 0.48√N ≪ T,
so none of these is excluded by a local density count. (Singer-type sets with uniform density only reach
the "uniform capacity" N/T + M_f, M_f = ∫|t|f = 4/15 for the ramp, i.e. k ≤ √N + √(f(0)·4/15)·N^{1/4}
= √N + 0.596·N^{1/4} for uniform-profile sets — the endpoint clusters are what the 0.94 bound "pays for".)

Fluctuation bookkeeping (proved identity): with γ_n = μ − k·μ_eq and potential constant on [0,N],
E = k²/cap + E_f(γ_n). Near-extremality needs E_f(γ_n) = o(k): the smoothed counting function must be
hyperuniform at scale T (a Poisson-like set has E_f(γ_n) ≈ k f(0), which wipes out the N^{1/4} term
entirely). This is consistent with (i) being tight, so it gives no contradiction by itself.

---------------------------------------------------------------------------------------------------

## 4. Numerical solution of the continuum LP P(ε) (finite ε)

Primal: φ piecewise linear on a non-uniform grid (step √ε/8 on [0,4√ε], √ε/2 in the bulk, √ε/16 on
[1−2√ε,1]), constraint φ̂ ≥ −ε imposed on η ∈ [0, 12/√ε] (step 0.05) plus cutting planes from a check grid
(step 0.01, up to 6/h_min); final violation ≤ 0.1% of ε. Feasible points ⇒ lower bounds for P(ε).
Dual: G = ν₀ + Σ ν_m cos(2πη_m x), ν ≥ 0, η adaptively refined up to 7/√ε; bound (2.2) re-evaluated on a
4·10⁵-point grid (this is the certified number, valid for every feasible φ).

| ε | primal Δ (feasible) | C ≥ | dual Δ (certified) | C ≤ | scalar C(ε)=4√2/3−√ε/9 |
|---|---|---|---|---|---|
| 1e-2 | 0.184362 | 1.8436 | 0.184983 | 1.8498 | 1.8745 |
| 3e-3 | 0.102059 | 1.8633 | 0.102270 | 1.8672 | 1.8795 |
| 1e-3 | 0.059014 | 1.8662 | (run killed: memory) | — | 1.8821 |
| 3e-4 | 0.032362 | 1.8684 | — | — | 1.8837 |

(The scalar column uses b = 2/3; at these τ the exact continuum b is ≈ 0.66, which lowers the scalar
value slightly — at ε = 1e-2 to Δ ≈ 0.1872, still above the certified LP dual 0.18498.)
Caution recorded: my first runs on a coarse η-grid (step 1/8) were wrong by a lot (they reported
C ≈ 2.27, above the scalar bound) because φ̂ dipped below −ε between grid points; only cutting-plane
runs with explicit a-posteriori checks are reported above.

**Shape of the optimum (both sides agree).**
* Primal: φ ≡ 1 on |x| ≤ 1.5√ε, then a downward jump, then φ ≈ (1 − |x|) + β√ε with β ≈ 0.90–0.98 in the
  whole bulk (a dilated, truncated triangle), plus fine structure in a layer of width O(√ε) at x = ±1
  (a jump of size ≈ β√ε at |x| = 1 and a thin spike at the endpoint).
* Dual: 1 + G > 0 only on |x| ≲ 1.46√ε (the "kernel") and on a thin layer at |x| → 1 (width ≈ 0.007
  at ε = 0.01); |1 + G| ≤ 5·10⁻⁵ on the rest. The spectral atoms sit near η ≈ m − t_m (t_m drifting from
  ≈ 0.05m to ≈ 1/2). Forcing 1 + G ≤ 0 on [0.5, 1] (no endpoint layer) gives C ≤ 1.8772 at ε = 1e-2,
  i.e. back to the scalar value: **the whole LP gain comes from putting positive weight on lags
  d ≈ N** (pairs with one element near each end), which penalises the endpoint atoms of the
  equilibrium measure (§3).

**Rigorous finite-N consequence (proved, via (1.1), exact floating-point sum).** With the ε = 1e-2
certificate (121 atoms): N = 10⁴ gives k ≤ 109.71 versus k ≤ 109.84 from the ramp scalar bound
(b = 2/3, best T). N = 2·10⁴: 153.03 vs 153.05. N = 5·10³ and 4·10⁴: the fixed certificate is worse than
the scalar (it is tuned to k/N ≈ 0.01). Both give k ≤ 109 at N = 10⁴, so **no integer improvement**.

---------------------------------------------------------------------------------------------------

## 5. The ε → 0 limit of the LP: a boundary-layer problem (derivation + numerics)

Ansatz (from §4): φ = Λ + s·π(x/s) + s·ω((1−|x|)/s), s = √ε, Λ(x) = (1 + βs − |x|)₊ restricted to
[−1,1]. Then ∫φ − 1 = 2βs + O(s²), so **C_LP = 2β\***. Writing η = θ/s, Λ̂(η) = sin²(πLη)/(π²η²),
e(η) = e^{2iψ}e^{−2πiβθ}(1+o(1)) with ψ = πLη, and minimising over the fast phase ψ:

  φ̂ ≥ −s² for all η  ⇔ (to leading order)  |2W(θ) − a(θ)| ≤ 1 + a(θ) + π̂(θ)  ∀θ > 0,         (5.1)

  a(θ) = 1/(2π²θ²),  W(θ) = e^{−2πiβθ} ω̂(θ),  π even with π(u) ≤ |u| − β (this is φ ≤ 1 near 0),
  ω(v) = −(β + v) on (−β, 0) (φ = 0 beyond |x| = 1), ω(v) ≥ −(β + v) on v > 0 (φ ≥ 0 near ±1).

(Derivation: min_ψ [sin²ψ/(π²θ²) + 2Re(e^{2iψ}W)] = a − |2W − a|.) Sanity check: π = min(0,|u|−β),
ω = forced part only gives β ≤ 1/√2 (the trapezoid of §2) — reproduced numerically.
A further O(s) global mode (φ += cs(1−|x|), whose transform vanishes at the integers) decouples the
inner level from the end level: objective β_in + β_end with π ≤ |u| − β_in and (5.1) using β = β_end.

Numerics (LP feasibility + bisection; PL profiles on [0,6] step 0.05, θ ∈ [0.002, 12], 24-gon outer
approximation of the modulus): with β_in = β_end = β, **β\* ≈ 0.9369** (feasible at 0.93694,
infeasible at 0.93700), i.e. C ≈ 1.874, c ≈ 0.937.
Two-level version, max of β_in + β_end at fixed β_end (same discretisation):

| β_end | 0.70 | 0.85 | 0.90 | 0.92 | 0.937 | 0.95 | 1.02 | 1.20 |
|---|---|---|---|---|---|---|---|---|
| β_in max | 1.1702 | 1.0281 | 0.9746 | 0.9539 | 0.9370 | 0.9244 | 0.8581 | 0.6645 |
| C = sum | 1.8702 | 1.8781 | 1.8746 | 1.8739 | 1.8740 | 1.8744 | 1.8781 | 1.8645 |

The profile in β_end is bumpy (two maxima ≈ 1.878 with a dip between), which I read as discretisation
noise of a few 10⁻³ (a refined run h = 0.025, U = 8, Θ = 14 did not finish in 10 min). All values stay
below 4√2/3 = 1.8856, as they must. Best estimate of the limit: **C_LP ≈ 1.874–1.878, c_LP ≈ 0.937–0.939.**
The finite-ε primal values of §4 (C ≥ 1.8684 at ε = 3e-4, increasing as ε ↓) are consistent with this.

**Conclusion of §§1–5 (numerical, not a proof):** every argument that uses only
"R(d) ∈ [0,1] off the diagonal, R(0) = k, supp R ⊂ (−N,N), R̂ ≥ 0" — this includes any single kernel,
any positive combination of kernels at several scales (idea 2), signed positive-definite kernels,
and capacity/equilibrium arguments — is capped at **c_LP ∈ [≈0.934, 0.9428]**, with the ε→0 boundary-
layer computation pointing to c_LP ≈ 0.937–0.939. So the scalar ramp argument is within ≈ 0.5% (at most ≈ 1%)
of everything positive-definiteness can give. Whether c_LP < 2√2/3 strictly is supported by the finite-ε
certified duals (§4) and the reduced problem (5.1), but I have **not** produced an ε-uniform certificate
family, so no asymptotic improvement is proved.

---------------------------------------------------------------------------------------------------

## 6. The five suggested ideas, one by one

**(1) Step (i) is lossy / count small differences against local density.**
Any inequality that is linear in R (counts of pairs at given distances, windowed second moments
Σ_x n_x(D)² = kD + 2Σ_{d<D}(D−d)R(d), variance ≥ 0 statements) is an LP(N) certificate, hence capped by §5.
Going to third moments does not help, because 3-point Sidon constraints are vacuous at this density:
for windows of length D, Σ_x n_x³ = kD + 6Σ_{d<D}(D−d)R(d) + 6Σ_{a<b<c}(D−(c−a))₊, and a triple
a<b<c is determined by its two gaps (b−a, c−b) (each difference occurs once), so
Σ_x n_x³ ≤ kD + 3D² + D³ (proved). A set of density 1/√N has Σ_x n_x³ ≈ N·(D/√N)³ = D³/√N, a factor √N
below the cap — no constraint. Real near-optimal sets (§7) have step (i) essentially tight (all
differences < T present), so (i) is *not* where they lose. → nothing beyond the LP.

**(2) Several scales at once.** Σ_j λ_j E_{f_j}(T_j) with λ_j ≥ 0 is the energy of the single kernel
F = Σ λ_j f_j(·/T_j); signed combinations that stay positive definite are also LP certificates; so all
of this is inside LP(N) and capped at c_LP ≈ 0.937 (§5) — gain ≤ ≈ 0.006 over 2√2/3, and the LP optimum
does not look multi-scale in the bulk: its only new feature is the endpoint layer at lags ≈ N.

**(3) Sums.** S(s) = #{(a,a′): a+a′ = s} ∈ {0,1,2}. In the scalar-extremal configuration (bulk density
1/√N plus endpoint clusters of 0.69 N^{1/4} points) S(s) ≈ ρ²·min(s, 2N−s) + O(N^{−1/4}) ≤ 1 + O(N^{−1/4}),
i.e. the sum constraint is slack by a factor 2 everywhere, including at the clusters (m points of a
Sidon cluster in a window W ≳ m²/2 have sum density ≤ ½ of the cap). The Fourier coupling Ŝ = μ̂² only
gives |Ŝ| = R̂ (an identity, no new lower bound on R̂), and the energy identity Σ S² = Σ R² = 2k² − k is
automatic for 0/1-valued R. → nothing at order N^{1/4}.

**(4) Position-dependent kernel.** E_w = Σ w(a)w(a′)f((a−a′)/T). Lower bound: substituting ν′ = wν
shows the weighted capacity equals the unweighted one, E_w ≥ (Σ_a w(a))²/cap. Upper bound: the unique
pair at difference d has unknown position, so one must use max_x w(x)w(x+d). With w = 1 + β on the
end windows: gain on the left ≈ 2β·(cluster size)·k ≈ 2.8β N^{3/4}, loss on the right ≈ cap·β·T ≈ βN.
Fails by a factor N^{1/4} (proved for this family; the obstruction is generic: weights only help if
one knows *where* the small differences sit, which is exactly the missing information).

**(5) Integrality.** Window counts are integers: Σ_x (n_x − n̄)² ≥ (N+T)·θ(1−θ) = O(N), but the bound
needs precision O(kT) = O(N^{5/4}) in Σ n_x² — negligible. R(d) ∈ {0,1} versus [0,1] is invisible in the
scaling limit (only local averages of R matter at order N^{1/4}); the only integrality that survives is
R(0) = k = Σg² = Σg, which the LP already has. → nothing at leading order.

Small non-LP fact that *is* usable (proved): pairs at distance ≥ N − t are pairs (x, y) of distances
from the left/right end with x + y ≤ t; their sums are distinct and each end set is Sidon, so
#{pairs at distance ≥ N−t} ≤ Σ_{x≤t} |Y ∩ [0, t−x]| ≤ ∫_0^t √(t−s) d√s + O(t^{3/4}) = (π/4)t + O(t^{3/4}).
So on the endpoint layer that carries the whole LP gain, the true occupation is ≤ π/4 < 1. This can only
sharpen the (already ≤ 1%) LP gain; it does not open a large improvement.

---------------------------------------------------------------------------------------------------

## 7. Real Sidon sets: which inequality is slack? (finite checks, exact discrete capacity)

Golomb rulers k = 10…20 (mark sets from memory, believed optimal; Sidon property verified in code,
optimality not re-verified), placed in
[1, N], N = length+1; ramp kernel at the T minimising the scalar bound; slack(i) = k f(0) + Σ_{d≠0} f(d/T) − E,
slack(ii) = V = E − k²/cap(N,T):

| k | N | c_obs | scalar k ≤ | T | slack(i) | V = slack(ii) | V/(k f(0)) | end/middle density |
|---|---|---|---|---|---|---|---|---|
| 10 | 56 | 0.920 | 10.29 | 32 | 0.00 | 2.11 | 0.16 | 3.00 |
| 11 | 73 | 0.840 | 11.55 | 38 | 2.34 | 1.77 | 0.12 | 3.60 |
| 12 | 86 | 0.895 | 12.40 | 43 | 0.00 | 3.19 | 0.20 | 3.00 |
| 13 | 107 | 0.826 | 13.65 | 51 | 1.54 | 3.89 | 0.22 | 2.57 |
| 14 | 128 | 0.799 | 14.77 | 59 | 0.01 | 6.78 | 0.36 | 1.67 |
| 15 | 152 | 0.761 | 15.93 | 68 | 3.20 | 5.52 | 0.28 | 2.00 |
| 16 | 178 | 0.728 | 17.08 | 76 | 4.45 | 6.09 | 0.29 | 2.33 |
| 17 | 200 | 0.760 | 17.99 | 83 | 3.35 | 6.67 | 0.29 | 1.64 |
| 18 | 217 | 0.852 | 18.66 | 88 | 0.00 | 6.87 | 0.29 | 1.91 |
| 19 | 247 | 0.828 | 19.77 | 96 | 2.33 | 5.89 | 0.23 | 2.18 |
| 20 | 284 | 0.767 | 21.04 | 106 | 0.04 | 11.42 | 0.43 | 1.62 |
| greedy 20 | 475 | −0.38 | 26.54 | 157 | 26.79 | 47.01 | 1.76 | 2.45 |

(end/middle = density in the outer eighths vs the middle three quarters.) Observations: for optimal
rulers step (i) is (nearly) exactly tight — every difference below T occurs — and the loss is in step
(ii), the fluctuation energy V ≈ 0.12–0.43·k f(0). The ends are 1.6–3.6× denser than the middle, as the
endpoint atoms of the ramp equilibrium predict (§3). Caveat: here T ≈ N/2, far from the asymptotic
regime T ≈ √2·N^{3/4} ≪ N; these are finite checks only.

---------------------------------------------------------------------------------------------------

## 8. The single most promising inequality for a follow-up

Fluctuation lower bound (non-LP; conjectural):

  V_T(A) := Σ_{a,a′∈A} f((a−a′)/T) − k²/cap(N,T) ≥ κ·k   for Sidon A ⊆ [1,N], k ≥ √N, T ≍ N^{3/4}.   (8.1)

With (i) unchanged this gives k² ≤ cap·(k(f(0) − κ) + T), i.e. c ≤ √((f(0) − κ)·b_f) = √((4/3 − κ)·2/3)
(κ = 0.1 → 0.906; κ = 0.2 → 0.869). Why this is the right target: (a) the LP optimum — hence every
positivity argument — sits within ≈ 0.5% of the scalar bound in c, which forces V ≲ 0.01·k there, so
(8.1) is exactly the missing non-LP content; (b) on all optimal
rulers the scalar argument loses only in V, with V/(k f(0)) between 0.12 and 0.43; (c) V ≈ 0 forces the
smoothed counting function to be hyperuniform at scale T while all differences below T are realised and
0.69·N^{1/4}-point clusters sit at both ends — a combination for which I found no construction. A proof of
(8.1) has to use 0/1 structure beyond the 2-point function (e.g. that R is a sum of k translates of 1_A,
or a Lasserre/moment-type positivity on pairs); I did not find one.

---------------------------------------------------------------------------------------------------

## 9. Status, proved vs heuristic, cost

**Status: PARTIAL.** No coefficient below 2√2/3 = 0.9428 is proved.

Proved (elementary, checkable by hand):
1. Inequality (1.1) for every finite cosine sum G with nonnegative weights. It contains the scalar
   argument (G = F/c − 1 extended) and every multi-scale or signed positive-definite variant.
2. Fejér–Riesz reformulation of LP(N) (§1): the LP relaxation is the Sidon problem for real weights
   with Σg = Σg² = k.
3. Finite-N certificate (§4): at N = 10⁴, k ≤ 109.71 from (1.1) versus 109.84 from the ramp argument.
   This is a real but tiny gain, and it does not change the integer bound.
4. Negative statements: 3-point window moments are slack by a factor √N (§6(1)). The sum constraint is
   slack by a factor 2 in the extremal configuration (§6(3)). Position weights of the form 1 + β·(end
   windows) lose by a factor N^{1/4} (§6(4)). Window-count integrality is worth O(N) against a needed
   O(N^{5/4}) (§6(5)). Pairs at distance ≥ N − t number ≤ (π/4)t + O(t^{3/4}).

Numerical evidence only (not proofs):
5. The continuum LP P(ε) has, at ε = 1e-2 and 3e-3, certified duals below the scalar value (C ≤ 1.8498
   versus 1.8745; C ≤ 1.8672 versus 1.8795). Feasible primals give C ≥ 1.8436, 1.8633, 1.8662, 1.8684 at
   ε = 1e-2, 3e-3, 1e-3, 3e-4.
6. The ε → 0 boundary-layer problem (5.1) gives C_LP ≈ 1.874–1.878, so c_LP ≈ 0.937–0.939. The
   reduction is a leading-order ansatz, not a theorem, and the discretisation noise is a few 10⁻³.
7. Structure: the ramp equilibrium has endpoint atoms of mass ≈ 0.49T × density. Optimal rulers have
   denser ends (×1.6–3.6), step (i) tight, and step (ii) slack.

Heuristic / open:
8. Whether c_LP < 2√2/3 strictly in the limit. An ε-uniform certificate family G_ε built from the
   dual structure would settle it: spectral atoms near η ≈ m − t(m√ε), plus a positive layer at lags
   ≈ N. Even if it exists, the gain is ≲ 0.006 in c.
9. The fluctuation bound (8.1). This is the only lever I found that could move c substantially.

Cost: about 2.5 CPU-hours of LP solves (HiGHS, ≤ 2 threads), all local. One dual run at ε = 1e-3 and
one refined reduced run were killed (memory/time) and are not used. No web access and no paper
lookup. The shared scratchpad also holds other agents' files, including downloaded papers; I did not
open any of them.

## Appendix: scripts (session scratchpad `probeA/`, not committed)

* `cap_ramp.py`: discrete capacities and equilibrium atoms (§3).
* `primal_nu.py`: feasible primal for P(ε) with a non-uniform PL grid and cutting planes (§4).
* `dual_lp2.py`: dual certificate with adaptive η refinement and fine-grid a-posteriori evaluation (§4).
* `noend.py`: dual with 1 + G ≤ 0 forced on [0.5, 1], which isolates the endpoint-layer gain (§4).
* `finiteN.py`: rigorous finite-N bound (1.1) versus the ramp scalar bound (§4).
* `reduced.py`: boundary-layer problem (5.1), symmetric bisection and two-level version (§5).
* `rulers.py`: slack decomposition on Golomb rulers and a greedy set (§7).

Superseded and not used: `lp_relax.py`, `cont_lp.py`, `cont_lp2.py`, `cont_lp4.py` (coarse η-grids
gave infeasible "optima"), and `dual_lp.py` (fixed grid, weaker).
