# PROBE_B — beyond the single-kernel bound for Sidon sets in [1,N] (clean-room probe)

Date: 2026-10-02. Clean-room: no web, no papers, no other project files were consulted. Inputs were the task
statement and standard mathematics only. Computation: about 15 minutes of single-core numpy/scipy in total.

## Status

**NO GAIN.** None of the proposed extra constraints, alone or combined, beats `2*sqrt(2)/3`:
(a) boundary-layer versus bulk difference counting, (b) sub-interval caps `|A∩I| <= F(|I|)` with an LP over
density profiles, and (c) window-variance or second-moment inequalities.

* **Proved (finite N, rigorous):** the kernel method is closed under combination (minimax closure, §2).
  Imposing *all* nonnegative positive-definite (p.d.) convolution kernels at once, at all scales, certifies
  exactly the same `k` as the best *single* such kernel. This also holds after adding any family of convex
  (e.g. linear) constraints on the density profile, such as the sub-interval caps, provided the saddle-point
  profile satisfies them. Every window-variance inequality `Σ_x (n_x − mean)^2 >= 0` is one p.d. kernel, so
  (c) is a special case.
* **Computed (second-order scaling model, §1 and §6):** the combined max–min programme uses 108 kernel
  constraints (9 kernel shapes × 12 scales). Its value is **0.94286** at grid size h = 0.025 (0.94297 at
  h = 0.05). Here `2*sqrt(2)/3 = 0.942809`, and the best single kernel tried gives 0.94318. No combination went
  below `2*sqrt(2)/3`. This independently corroborates the claimed limit of the method to about 5e-5.
* **The profile that defeats the constraints** is the max–min (saddle) profile σ*, in units of
  `N^{3/4}` × bulk density, at each end:
  * an end cluster of ≈ 0.77·N^{1/4} points inside the first 0.1·N^{3/4};
  * total boundary excess s ≈ 0.47·N^{1/4} points per end;
  * cumulative excess `σ_cum(x) >= 0.43` (in units of N^{1/4} points) everywhere.

  This profile comes with `r(d) = 1` for all `d` in the kernel support (`d ≲ 1.5 N^{3/4}`), and with a
  fluctuation spectrum that vanishes at frequencies `|ξ| ≲ N^{-3/4}` (bulk hyperuniform at scale `N^{3/4}`).
  It satisfies:
  * every sub-interval cap, with margin 0.71·N^{1/4} (§3);
  * every local Sidon cap, with first-order slack (§4).
* **Conditional statement (trivial to prove, not useful unconditionally):** suppose that at the relevant scale
  the energy of `A` above equilibrium is at least `θ` times the Poisson level (§5). Then
  `c <= sqrt(1−θ)·c_kernel`. Pair statistics cannot supply θ > 0, because the relaxation is feasible with θ = 0.
  Any gain needs information beyond the 2-point function. This is the realisability of the saddle
  configuration by an actual 0/1 set, which is essentially the original problem.

---

## 0. Conventions

* `A ⊆ {1..N}` is Sidon with `|A| = k`. Write `r(d) = #{(a,b) ∈ A², a − b = d}`. Sidon ⇔ `r(d) ∈ {0,1}` for
  every `d ≠ 0`, and `r(0) = k`. Since Sidon is exactly the 2-point condition `r ≤ 1`, all of the information is
  in: the multiset of positions, `r ∈ {0,1}`, and the realisability of `r` as the autocorrelation of a 0/1 set.
* Kernel method: take `g ≥ 0`, even, p.d., `G = ∫g`, and scale `T`. Then
  `k² I_T(N) <= Σ_{a,b} g((a−b)/T) = k g(0) + Σ_{d≠0} g(d/T) r(d) <= k g(0) + Σ_{d≠0} g(d/T)`.
  Here `I_T(N)` is the minimum of `∫∫ g((x−y)/T) dν dν` over probability measures `ν` on `[0,N]`.
* Ansatz: `k = sqrt(N) + c N^{1/4}` and `T = τ N^{3/4}`. All second-order quantities are of size `sqrt(N)`.

## 1. Second-order reduction (derivation)

**Half-line profile.** Measure lengths in units of `N^{3/4}`. Normalise the bulk density to 1, so 1 unit of
mass means `N^{1/4}` points. Near the left end the smoothed counting measure is
`ν = 1_{[0,∞)} dx + σ`, where σ is a finite signed measure with `ν ≥ 0` (σ is the boundary layer). The right
end is the mirror image.

**Energy expansion.** Take `μ = (1_{[0,L]} + σ(x) + σ(L−x))/Z` with `Z = L + 2s`, `s = ∫dσ` and `L = N^{1/4}`.
Expanding to order `1/L²`, with layers decaying and no end–end interaction:

    E_g(μ) = G/L − b_σ(g)/L² + O(L^{-3}),
    b_σ(g) = m1(g) + 4 ∫ t_g dσ − 2 ∫∫ g(x−y) dσ(x) dσ(y),          (1.1)

where `m1(g) = ∫|u| g(u) du` and `t_g(x) = ∫_x^∞ g`. The derivation uses
`∫∫_{[0,L]²} g = LG − m1`, and that the potential of `1_{[0,∞)}` at `x ≥ 0` is `G − t_g(x)`; the
`4 sG/L²` terms cancel.

**Constraint.** Insert (1.1) into the kernel inequality and expand `k² = N + 2cN^{3/4} + …`:

    2 c ∫g  <=  g(0) + b_σ(g)       for every nonnegative p.d. g (any scale, in units N^{3/4}).    (1.2)

The scale is absorbed into `g`. (1.2) is **linear in g** and **concave in σ**, because the quadratic term is
`−2×` a p.d. form.

**Single-kernel value.** `max_σ b_σ(g) = β(g)`, attained by the half-line equilibrium. Its potential is
constant, and `β = 2 s_eq G`. Scaling `g → g(·/τ)` gives `β → τ² β` and `∫g → τ G`, so optimising over τ gives

    c(g) = sqrt( g(0) β(g) ) / G ,   τ* = sqrt( g(0)/β(g) ).        (1.3)

**Checks.**
* Triangle `(1−|x|)_+`: the equilibrium is the integer lattice, so `s = 1/2`, `β = 1` and `c = 1`. This is
  Lindström / Erdős–Turán.
* Exponential `e^{−|x|}`: the equilibrium is exactly `1 + δ_0` at each end. Then (1.1) gives
  `b = 2 + 4·1 − 2·1 = 4 = 2sG`, so `c = 1` exactly.
* Askey kernels `(1−|x|)_+^ν` give c = 0.94666 (ν=1.25), **0.94318 (ν=1.5)**, 0.94376 (ν=1.75) and 0.94546 (ν=2).
  These are h → 0 values with O(h²) convergence; see §6. They come close to `2√2/3` from above, which is
  consistent with the stated optimum of the method.

## 2. Minimax closure (rigorous; answers "combine the constraints" in general)

**Proposition.** Fix `N, k`. Let `𝒦` be the convex cone of even, nonnegative, p.d., finitely supported
`g: Z → R`. Let `𝒫` be the probability vectors on `{1..N}`, optionally intersected with any closed convex set
`C`, for example the caps `ν(I) <= F(|I|)/k` for every interval `I`. Define

    h(ν, g) = k² Σ_{x,y} g(x−y) ν(x) ν(y) − k g(0) − Σ_{0<|d|<N} g(d).

Every Sidon `A` with `|A| = k` (and `μ_A ∈ C`) satisfies `h(μ_A, g) <= 0` for all `g ∈ 𝒦`. Then

    min_{ν∈𝒫∩C} sup_{g∈𝒦} h(ν,g)  =  sup_{g∈𝒦} min_{ν∈𝒫∩C} h(ν,g).

**Proof.** `𝒫∩C` is compact and convex. `h(·,g)` is continuous and convex because `g` is p.d. `h(ν,·)` is
linear on the convex set `𝒦`. Sion's minimax theorem applies. ∎

**Consequences.**

1. *All kernels at once, all scales, all window-variance inequalities.* Each
   `Σ_x (|A∩[x,x+u)| − mean)² >= 0`, combined with `r <= 1`, is implied by `h(μ_A, g) <= 0` with
   `g = 1_{[0,u)} * 1_{(-u,0]}`. Cauchy–Schwarz over the windows gives a lower bound `<= k² I` for this `g`, so
   the variance form is never stronger. The same holds for weighted windows `w`, with `g = w * w̃`. Together
   these constraints certify exactly
   what one single kernel certifies, and that kernel is a positive combination of the family. The constant
   `2√2/3` is stated to be optimal over single kernels, so no family of second-moment or window-variance
   inequalities beats it. The same argument with `−max_x K(x,x+d)` in place of `Σ g(d)` covers
   non-convolution p.d. kernels: they form a convex family and `h` is concave in `K`. Whether one such
   non-convolution kernel beats `2√2/3` was **not** examined.
2. *Profile constraints.* With caps `C`, the combined method equals "kernel method with the equilibrium problem
   restricted to `C`". In the limit (1.2), the value is `max_{σ∈C} min_g Φ(σ,g)`, where
   `Φ = (g(0) + b_σ(g)) / (2∫g)`. It is unchanged whenever a saddle profile σ* lies in `C`. Sections 3 and 6
   show that σ* satisfies all caps with margin, so the caps are inactive.

## 3. (b) Sub-interval caps `|A∩I| <= F(|I|)`: derivation and LP

Use the bound being tested for sub-intervals, `F(M) <= sqrt(M) + c M^{1/4} + O(1)`. This is the
self-consistent "bootstrap" choice.

* **Interior intervals of length `M = θN`, θ < 1.** The content is `≈ θ sqrt(N)` and the cap is
  `sqrt(θ) sqrt(N)`. There is first-order slack `(sqrt θ − θ) sqrt N`, so these caps are inactive.
* **Intervals at the ends.** Take `I = [1, N−m]` with `m = μ N^{3/4}`, which removes a stretch of length `m`
  at the right end. Its content is `k − N^{1/4}(μ + σ_cum(μ))`. Its cap is
  `sqrt(N) − (μ/2) N^{1/4} + c N^{1/4} + o(N^{1/4})`. The cap therefore reads

      σ_cum(μ) >= −μ/2          for all μ > 0 (and the same at the left end),          (3.1)

  where `σ_cum(μ) = σ([0,μ])`. Removing both ends gives the sum of two copies of (3.1). Removing a length `m`
  loses `m/sqrt N` points, but the cap only drops by `m/(2 sqrt N)`. So the caps only forbid an end segment
  thinner than **half** the bulk density.
* **The LP and its value.** Over profiles σ, maximise `c` subject to (1.2) for all kernels and (3.1) for all
  μ. The optimum σ* has `min_μ (σ_cum + μ/2) = 0.713` and `min σ_cum = 0.434` (h = 0.025). It is strictly
  feasible for (3.1), so the LP value equals the kernel value: **0.94286** with the 108-kernel family, which is
  `2√2/3` within the discretisation error. The equilibrium of the best single kernel (Askey ν = 1.5 at τ*) has
  `min σ_cum ≈ 0.31`, so it is also strictly feasible.
* **Why.** The equilibrium profiles are *denser* at the ends. The caps can only punish *depleted* ends.

## 4. (a) Boundary layers versus bulk differences

* **Scale bookkeeping.** At the saddle, a layer of width `~N^{3/4}` holds `O(N^{1/4})` extra points. The
  points in the layer form `O(sqrt N)` pairs with difference `<= T`, out of `T ≈ 1.3 N^{3/4}` available
  differences. That is a fraction `N^{-1/4}`, exactly second order, and it is already inside the kernel
  identity. The kernel identity sums all pairs, layer–layer, layer–bulk and bulk–bulk, against one global
  budget `Σ g`. The Sidon property never localises: any split of the differences between bulk and layer that
  keeps `r <= 1` is admissible.
* **Local Sidon caps.** For a window of length `λN^{3/4}` at an end, the content is
  `<= (λ + 0.77) N^{1/4}` and the cap is `≈ sqrt(λ) N^{3/8}`. The ratio tends to 0, so these caps are inactive.
* **The end cluster is realisable.** About `m ≈ 0.67 N^{1/4}` excess points sit inside `0.1 N^{3/4}` at each
  end. As a Sidon set they need length `>= m² ≈ 0.45 sqrt N`, which is far below `0.1 N^{3/4}`.
* **The local constraint that does bind is already a kernel constraint.** A kernel at a small scale
  `τ → 0`, but still above the cluster diameter, turns (1.2) into
  `g(0)(1 − 2a²) >= 2cτ∫g + O(τ)`, where `a` is the cluster mass in units of `N^{1/4}` points per end. So the
  total number of internal pairs in the two clusters must fit inside the diagonal budget `k`, which gives
  `2a² <= 1`. This is exactly the "local density near the ends versus the global difference budget" trade-off
  the task asks about.
* **It is active at the saddle.** Among the tightest constraints of the combined programme are the small-scale
  kernels (τ = 0.2–0.45), alongside the scale-1–1.4 kernels (§6). The optimal kernel is therefore genuinely
  multi-scale, and this trade-off is already priced into `2√2/3`.

## 5. (c) Variance / second-moment inequality

**Exact identity.** Take windows `[x, x+u)` for `x = 2−u..N`; there are `X = N+u−1` of them. Then

    Σ_x (n_x − n̄)² = k u + Σ_{0<|d|<u} (u−|d|) r(d) − (k u)²/X ,   n̄ = ku/X.

* With `r <= 1` and only a nonnegative left-hand side this gives `c <= 1` (Erdős–Turán).
* With the boundary ramps of a uniform profile counted, it gives `c <= 1/√3`. That bound is *not valid* for
  general `A`, because `A` may have heavier ends. Optimising over profiles brings it back to `c = 1` for this
  kernel, and the lattice equilibrium attains it.

**Fluctuation decomposition (any kernel).** Let `ν_eq` be the equilibrium for `g_T`. Its potential is `>= I`
on `[0,N]` and equals `I` on its support. Then

    k g(0) + Σ_{d≠0} g_T(d) − k² I  =  M + F,   M = Σ_{d≠0} g_T(d)(1 − r(d)) >= 0,
                                                F = k²(E(μ_A) − I) >= k² E(μ_A − ν_eq) = ∫ |Â − kν̂_eq|² ĝ_T >= 0.

**Conditional proposition (proved; the hypothesis is not).** If `F >= θ k g(0)` with θ ∈ [0,1], then
`c <= sqrt(1−θ) · sqrt(g(0)β)/G`.

* *Proof:* replace `g(0)` by `(1−θ) g(0)` in §1.
* *Meaning:* θ = 1 is a Poisson-like fluctuation level at scale `T`, and gives `c <= 0`. The kernel extremal
  needs `θ = o(1)`, i.e. `A` must be **hyperuniform at scale `N^{3/4}`**, with fluctuation spectrum
  `≈ 0` on `|ξ| ≲ N^{-3/4}`, while still being Poisson-like below that scale (`r ≡ 1` on `[1, T]`).

**Why the hypothesis cannot come from pair data.**
* By §2 the relaxation "profile ν plus a p.d. fluctuation `Q`, with `k²ν*ν̃ + Q = kδ_0 + r'` and `r' <= 1`" is
  exactly dual to the kernel method, and θ = 0 is feasible in it.
* Integrality of the window counts gives only `Var >= {n̄}(1−{n̄}) = O(1)` per window. That is `O(N)` in
  total, against the `N^{5/4}` needed.
* There is no first-moment obstruction to hyperuniform Sidon structure. A one-point-per-block "perturbed
  lattice" has the right expected difference density, `r ≈ 1` for `d >= s`. However, it *misses* differences
  below the block length `s ≈ sqrt N`. That costs `M ≈ s g(0) ≈ k g(0)`, so small-scale hyperuniformity is
  paid for through `M`. The extremal needs hyperuniformity *only above* scale `N^{3/4}`, and nothing at the
  pair level forbids that.

**Real Sidon sets (illustration, exact computation).** The table uses Singer perfect difference sets of order
`q`, viewed as subsets of `[0, q²+q]`, with the Askey ν = 1.5 kernel at `T = 1.325 N^{3/4}`. All values are in
units of `k g(0)`. The identity `slack = M + F` was checked to 1e-13.

| q | N | (k−√N)/N^{1/4} | slack | M (missing d) | F (energy above eq.) |
|---|---|---|---|---|---|
| 31 | 993 | +0.087 | 1.64 | 0.83 | 0.81 |
| 61 | 3783 | +0.063 | 1.73 | 0.29 | 1.44 |
| 101 | 10303 | +0.049 | 1.80 | 0.87 | 0.93 |
| 151 | 22953 | +0.040 | 1.83 | 0.68 | 1.15 |

* The total slack ≈ `g(0) + τ*²β − 2cτ*G ≈ 1.9`, as (1.2) predicts for `c ≈ 0`.
* About 0.6 of `F` is the profile mismatch, since the set is uniform with no boundary layers:
  `τ*²(β − m1) ≈ 0.60`. The rest is fluctuation.
* `M` is large because a cyclic difference `d` is realised in `Z` as either `+d` or `d − n`.
* So the known algebraic sets are nowhere near the kernel extremal. They spend the whole second-order budget
  on missing differences plus fluctuation and flat ends.

## 6. Numerical set-up and output

**Programme.** Discretise σ on a grid `x_i = ih` of `[0, R)`, R = 5, with a trapezoid background (mass `h/2` at
0 and `h` elsewhere) and `ν_i = background_i + σ_i >= 0`. Use the discrete form of (1.1):

    b_σ(g) = m1_h + 4 Σ σ_i t_h(x_i) − 2 σᵀ G σ,   m1_h = h² Σ_m |m| g(mh) + h² g(0)/2,
    t_h(x_i) = h( Σ_{m>=i+1} g(mh) + g(ih)/2 ),    G_ij = g(x_i − x_j),   ∫g -> G_h = h Σ_m g(mh).

* Single kernel: maximise `b_σ` with `ν >= 0` (a nonnegative-least-squares QP), then apply (1.3).
* All kernels: maximise `z` subject to `z <= (g_j(0) + b_σ(g_j)) / (2 G_{h,j})` for all `j`, which is concave
  in σ, solved with SLSQP and analytic gradients.
* Family: Askey ν ∈ {1, 1.25, 1.5, 2, 3}, Gaussian `e^{−πx²}`, `e^{−|x|}`, the cubic B-spline (`tri*tri`) and
  Bohman, each at τ ∈ {0.2, 0.3, 0.45, 0.6, 0.8, 1.0, 1.2, 1.4, 1.7, 2.0, 2.5, 3.0}. That is 108 constraints.

**Cross-check.** A finite-interval QP minimises `wᵀGw − 2Σw` with `w >= 0` on `[0,L]`, so `I = 1/Σw` and
`s = (Σw·G_h − L)/2`. It gives the same single-kernel values and is L-independent for L >= 8.

**Single kernels** (h = 0.05 → 0.025 → 0.0125; the convergence is O(h²)):

| kernel | s per end | c |
|---|---|---|
| triangle (L integer) | 0.5 | 1.00000 |
| exp `e^{-|x|}` | 1.0 | 1.00000 |
| Gaussian | 0.4785 | 0.97831 |
| B-spline | 0.7283 | 0.98541 |
| Bohman | 0.398 | 0.99091 |
| Askey 3 | 0.2282 | 0.95421 |
| Askey 2 | 0.2980 | 0.94546 |
| Askey 1.75 | 0.3239 | 0.94376 |
| **Askey 1.5** | 0.3559 | **0.94318** |
| Askey 1.25 | 0.3983 | 0.94666 |

**Combined max–min:**

| | h = 0.05 | h = 0.025 |
|---|---|---|
| value | 0.94297 | **0.94286** |
| tight constraints | | Askey3 τ = 0.2, 0.3; Bohman τ = 0.2, 0.3, 0.45; Askey2 τ = 0.3, 1.4; triangle τ = 1.0; Askey1.5 τ = 1.4 |
| cluster mass in `[0, 0.1]` | | 0.766 |
| s | | 0.472 |
| `min σ_cum` | | 0.434 |
| cap margin `min(σ_cum + x/2)` | | 0.713 |

**Equilibrium of Askey 1.5 at τ = 1** (bulk-density units; for comparison): atom 0.52 at x = 0, density
0.64–0.95 on (0, 0.75), a concentration at x = 1 (the support edge), and ≈ 1 beyond 1.5. `σ_cum ∈ [0.31, 0.51]`.

**Caveat.** Taking this equilibrium at τ* as a *fixed* profile and testing it against kernels at τ ≈ 0.2–0.4
gives smaller Φ (≈ 0.90 in a first, h-inconsistent run). So a single-kernel equilibrium is **not** a saddle:
small-scale kernels penalise its end atom, `2a² ≈ 0.98`. The true saddle is the max–min profile above. This
does not change the conclusion. It only shows that the optimal kernel is a multi-scale combination.

**Resolution limit.** The family stops at τ >= 0.2. The max–min profile can therefore keep its end cluster
(mass 0.766, `2a² ≈ 1.17`) spread over ≈ 0.1, below the smallest kernel scale. Adding kernels at τ < 0.2 adds
constraints, so it can only *raise* the max–min value. It cannot push it below `2√2/3`. The cluster mass quoted
for σ* is therefore resolution-dependent, but the "no gain" conclusion is not.

## 7. Honest assessment

* **What is solid.**
  * Minimax closure (§2) is a short rigorous argument (Sion). Second-moment, window-variance and
    multi-kernel constraints, together with any convex profile constraints that the saddle satisfies, cannot
    improve on the best single kernel.
  * The sub-interval caps (b) are provably inactive in the second-order model: (3.1) needs `σ_cum >= −μ/2`,
    and the saddle has `σ_cum >= 0.43`.
* **What is numerical only.**
  * The saddle profile and the value 0.94286 come from a discretised half-line model (h = 0.025, R = 5,
    a finite kernel family with τ >= 0.2).
  * I did not reconstruct the exact kernel that attains `2√2/3`. The family above comes within 5e-5 from
    above, which supports the stated optimum. That optimality claim was taken from the task statement, not
    re-proved here.
  * The finite-N second-order expansion (1.1)/(1.2) is a formal asymptotic, checked against exact closed forms
    (triangle, exponential) and against the finite-interval QP. It was not proved with error terms.
* **What would be needed for a gain.** Information that is not a linear functional of the pair function and
  the profile. The Sidon property is purely 2-point (`r <= 1`), so the only remaining information is
  *realisability*: is the saddle configuration the autocorrelation of an actual 0/1 set? The saddle needs:
  1. the profile σ*, with an end cluster of `≈ 0.77 N^{1/4}` points inside `0.1 N^{3/4}`;
  2. every difference `d ≲ 1.5 N^{3/4}` used exactly once;
  3. a fluctuation spectrum that vanishes on `|ξ| ≲ N^{-3/4}` (hyperuniform above scale `N^{3/4}`) but is
     Poisson-like below it.

  A theorem of the form "a Sidon set using all differences up to `D` has window-count variance at least
  `θ·mean` at scale `D`" would give `c <= sqrt(1−θ)·2√2/3` by §5. I see no route to such a statement:
  * the relaxation is feasible with θ = 0;
  * integrality gives only `O(1)` per window;
  * no Sidon set close to the bound (`c > 0`) is known that could be examined for its fluctuation structure.
  The known algebraic sets (Singer) are Poisson-like and lose the whole second-order budget (§5 table).
* **Not attempted:** 3-point or higher realisability constraints for 0/1 sequences, non-convolution
  kernels, and any formal proof of the asymptotic expansion.

**Conclusion.** No candidate theorem with `c < 2√2/3` came out of (a), (b) or (c). The original problem, the
second-order term of F(N), remains open, and nothing here bears on it beyond showing where a new idea would
have to come from.
