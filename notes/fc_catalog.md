## Arxiv/0912.2382/CurlingNumberConjecture.lean
/-!
# The Curling Number Conjecture

*Reference:* [arxiv/0912.2382](https://arxiv.org/abs/0912.2382)
**The Curling Number Conjecture**
by *Benjamin Chaffin and N. J. A. Sloane*
-/

### curling_number_conjecture
/--
The sequence will eventually reach $1$.
-/
```
theorem curling_number_conjecture (S₀ : List ℤ) (h : S₀ ≠ []) : ∃ m, k (S S₀ m) = 1 := by
```

## Arxiv/1102.4662/AtiyahSutcliffe.lean
/-!
# The first Atiyah--Sutcliffe conjecture

Atiyah and Sutcliffe associate a homogeneous binary polynomial to each point
in a configuration of distinct points in Euclidean three-space. Their first
conjecture says that these polynomials are always linearly independent.

*References:*
- M. F. Atiyah and P. M. Sutcliffe,
  [The Geometry of Point Particles](https://doi.org/10.1098/rspa.2001.0913)
- Marcin Mazur and Bogdan V. Petrenko,
  [On the conjectures of Atiyah and Sutcliffe](https://arxiv.org/abs/1102.4662)
-/

### conjecture_one
/-- [Atiyah–Sutcliffe Conjecture 1](https://doi.org/10.1098/rspa.2001.0913), stated as
Conjecture 1.1 in [Mazur–Petrenko](https://arxiv.org/abs/1102.4662): the configuration
polynomials are linearly independent. -/
```
theorem conjecture_one {n : ℕ} (x : Fin n → Point) (hx : Function.Injective x) :
    LinearIndependent ℂ (pointPolynomial x) := by
```

## Arxiv/1104.1579/CunninghamChain.lean
/-!
# Cunningham chains — Jones's conjecture

A Cunningham chain is a sequence of primes satisfying either $p_{i+1}=2p_i+1$
(first kind) or $p_{i+1}=2p_i-1$ (second kind). It is conjectured that there
are infinitely many chains of every positive exact length, of both kinds.

A chain has **exact length k** when its first $k$ terms are prime and the
$(k+1)$-th generated term is composite.

Lenny Jones conjectures that for every positive integer $k$, infinitely many
primes start a chain of exact length $k$, for each of the two kinds.

*References:*
- Lenny Jones, [Polynomial Cunningham Chains](https://arxiv.org/abs/1104.1579)
- [OEIS A181697](https://oeis.org/A181697), first-kind chain lengths
- [OEIS A181715](https://oeis.org/A181715), second-kind chain lengths
-/

### infinitely_many_firstKind_chains
/--
Jones's conjecture (first kind): for every positive integer $k$, there are
infinitely many primes $p$ that start a first-kind Cunningham chain of
exactly length $k$.
-/
```
theorem infinitely_many_firstKind_chains (k : ℕ) (hk : 0 < k) :
    Set.Infinite {p : ℕ | IsFirstKindChainOfLength p k} := by
```

### infinitely_many_secondKind_chains
/--
Jones's conjecture (second kind): for every positive integer $k$, there are
infinitely many primes $p$ that start a second-kind Cunningham chain of
exactly length $k$.
-/
```
theorem infinitely_many_secondKind_chains (k : ℕ) (hk : 0 < k) :
    Set.Infinite {p : ℕ | IsSecondKindChainOfLength p k} := by
```

## Arxiv/1601.03081/UniqueCrystalComponents.lean
/-!
# Unique Crystal Components

*Reference:* [arxiv/1601.03081](https://arxiv.org/abs/1601.03081)
**The Biharmonic mean**
by *Marco Abrate, Stefano Barbero, Umberto Cerruti, Nadir Murru*
-/

### crystals_components_unique
/--
If $n = ab$ is a crystal, then there are no other pairs of
positive integers $c, d > 1$, different from the couple $a, b$, such that $n = cd$ and
$B(c, d) ∈ ℕ$, i.e., the components of the crystals are unique.
-/
```
theorem crystals_components_unique (n a b c d : ℕ)
    (hab : IsCrystalWithComponents n a b) (hcd : IsCrystalWithComponents n c d) :
    ({a, b} : Finset ℕ) = {c, d} := by
```

## Arxiv/1609.08688/sIncreasingrTuples.lean
/-!
# The length of an $s$-increasing sequence of $r$-tuples

This file contains the formalisation of [GoLo21] up to and
including Conjecture 1.8.

*References:*
- [arxiv/1609.08688](https://arxiv.org/abs/1609.08688)
  **The length of an $s$-increasing sequence of $r$-tuples** by *W. T. Gowers, J. Long*
- [GoLo21](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/length-of-an-sincreasing-sequence-of-rtuples/7301418D47DB1ECD6BE71C20E8A98D0A)
  **The length of an $s$-increasing sequence of $r$-tuples**
  by *W. T. Gowers, J. Long*, Combinatorics, Probability and Computing (2021), 686-721
-/

### maximalLength_le_strong
/-- $F(n) \leq n^{3/2}$. -/
```
theorem maximalLength_le_strong (n : ℕ) : F n ≤ Real.sqrt n ^ 3 := by
```

## Arxiv/2104.00502/BarkerSequence.lean
/-!
# Barker sequences

A Barker sequence is a finite sequence of $\pm 1$ values whose nontrivial aperiodic
autocorrelations all have magnitude at most one. The Barker conjecture says that no such sequence
has length greater than $13$.

*References:*
* J. Willms, [A note on Barker sequences of even length](https://arxiv.org/abs/2104.00502)
* [Barker code](https://en.wikipedia.org/wiki/Barker_code)
* [OEIS A091704](https://oeis.org/A091704)
-/

### barker_conjecture
/-- Every Barker sequence has length at most $13$. -/
```
theorem barker_conjecture (a : List ℤ) (ha : IsBarkerSequence a) : a.length ≤ 13 := by
```

## Arxiv/2107.00295/IndependentDomination.lean
/-!
# Independent Domination of Regular Graphs, Conjecture 1.6

*Reference:* [arxiv/2107.00295](https://arxiv.org/abs/2107.00295)
**On independent domination of regular graphs**
by *Eun-Kyung Cho, Ilkyoo Choi, Boram Park*
-/

### independentDominationEven
/--
**Conjecture 1.6 (Even case).**
For a nonempty isolate-free graph $G$ on $n$ vertices,
if $D$ is even, then $(D + 2)^2 \cdot i(G) \leq (D^2 + 4) \cdot n$.
-/
```
theorem independentDominationEven (hIso : 0 < G.minDegree) (hEven : Even G.maxDegree) :
    let D := G.maxDegree
    let i := G.indepDominationNumber
    let n := Fintype.card V
    (D + 2)^2 * i ≤ (D^2 + 4) * n := by
```

### independentDominationOdd
/--
**Conjecture 1.6 (Odd case).**
For a nonempty isolate-free graph $G$ on $n$ vertices,
if $D$ is odd, then $(D + 1)(D + 3) \cdot i(G) \leq (D^2 + 3) \cdot n$.
-/
```
theorem independentDominationOdd (hIso : 0 < G.minDegree) (hOdd : Odd G.maxDegree) :
    let D := G.maxDegree
    let i := G.indepDominationNumber
    let n := Fintype.card V
    (D + 1) * (D + 3) * i ≤ (D^2 + 3) * n := by
```

## Arxiv/2107.12475/CollatzLike.lean
/-!
# Digit $2$ in base $3$ representation of $2^n$

*References:*
- [Some Unconventional Problems in Number Theory](https://doi.org/10.2307/2689842)
  by *Paul Erdös*, Mathematics Magazine 52, no. 2, p. 67, 1979
- [arxiv/2107.12475](https://arxiv.org/abs/2107.12475)
  **Hardness of busy beaver value BB(15)** by *Tristan Stérin, Damien Woods*
- [Hardness of Busy Beaver Value BB(15)](https://doi.org/10.1007/978-3-031-72621-7_9)
  by *Tristan Stérin, Damien Woods*, Reachability Problems, Lecture Notes in Computer Science
  15050, Springer, Cham (2024)
-/

### CollatzLike
/--
For $n > 8$, $2^n$ is not the the sum of distinct powers of $3$. Expressed here in terms of the base $3$ digits of $n$.

This conjecture is equivalent to the halting of a $15$-state $2$-symbol Turing Machine.

TODO(lezeau): Formalize the Turing Machine version of this problem.

Source: *Hardness of Busy Beaver Value BB(15)*: https://link.springer.com/chapter/10.1007/978-3-031-72621-7_9
This is also https://arxiv.org/abs/2107.12475.
-/
```
theorem CollatzLike (n : ℕ) (hn : 8 < n) : 2 ∈ Nat.digits 3 (2^n) := by
```

## Arxiv/2208.14736/ZariskiCancellation.lean
/-!
# Zariski Cancellation

*Reference:* [arxiv/2208.14736](https://arxiv.org/abs/2208.14736)
**The Zariski Cancellation Problem and related problems in Affine Algebraic Geometry**
by *Neena Gupta*
-/

### zariski_cancellation_problem
/--
The **Zariski Cancellation Problem**: every polynomial ring over a field `k` of characteristic
`0` is cancellative.
-/
```
theorem zariski_cancellation_problem {k : Type*} [Field k]
    [CharZero k] {ι : Type*} [Fintype ι] : IsCancellative k (MvPolynomial ι k) := by
```

## Arxiv/2209.04540/SpectralSetsAndWeakTiling.lean
/-!
# Spectral sets and weak tiling

This file formalizes Problems 7.1 and 7.2 from Kolountzakis, Lev, and Matolcsi.

*References:*
- [KLM2023] Mihail N. Kolountzakis, Nir Lev, and Máté Matolcsi,
  [Spectral sets and weak tiling](https://arxiv.org/abs/2209.04540).
- [GL16] Rachel Greenfeld and Nir Lev, Spectrality and tiling by cylindric domains,
  *Journal of Functional Analysis* 271 (2016), 2808–2821.
- [GL20] Rachel Greenfeld and Nir Lev, Spectrality of product domains and Fuglede's conjecture
  for convex polytopes, *Journal d'Analyse Mathématique* 140 (2020), 409–441.
-/

### exists_nowhereDense_spectralSet
/--
[KLM2023, Problem 7.1] asks whether a bounded, measurable, nowhere dense subset
$\Omega \subset \mathbb{R}^d$ of positive measure can be spectral for every $d \ge 2$.
-/
```
theorem exists_nowhereDense_spectralSet :
    answer(sorry) ↔ ∀ᵉ (d : ℕ) (hd : 2 ≤ d),
      ∃ Ω : Set (Fin d → ℝ), Bornology.IsBounded Ω ∧ MeasurableSet Ω ∧
        IsNowhereDense Ω ∧ 0 < volume Ω ∧ isSpectral Ω := by
```

### isSpectral_right_of_product_three_dimensional
/--
[KLM2023, Problem 7.2] For a three-dimensional convex body $A$ and a bounded,
measurable set $B$, must spectrality of $A \times B$ imply spectrality of $B$?
-/
```
theorem isSpectral_right_of_product_three_dimensional :
    answer(sorry) ↔
      ∀ (m : ℕ), 0 < m → spectralProductImpliesRightSpectral 3 m := by
```

### isSpectral_right_of_product_of_convexBody
/--
[KLM2023, Problem 7.2] For every positive dimension $n$, a convex body $A$ and a bounded,
measurable set $B$, must spectrality of $A \times B$ imply spectrality of $B$?
-/
```
theorem isSpectral_right_of_product_of_convexBody :
    answer(sorry) ↔
      ∀ (n m : ℕ), 0 < n → 0 < m →
        spectralProductImpliesRightSpectral n m := by
```

## Arxiv/2303.01089/FurstenbergTimesPTimesQ.lean
/-!
# Furstenberg's `times p, times q` conjectures

*Reference:* [arxiv/2303.01089](https://arxiv.org/abs/2303.01089)
**Around Furstenberg's times $p$, times $q$ conjecture: times $p$-invariant measures
with some large Fourier coefficients**
by *Catalin Badea, Sophie Grivaux*
-/

### conjecture_1_3
/--
**Conjecture 1.3** (the $\times p, \times q$ conjecture): the only atomless Borel probability
measure on $\mathbb{T}$ which is both $T_p$- and $T_q$-invariant is the Lebesgue measure.
-/
```
theorem conjecture_1_3 {p q : ℕ} (hp : 2 <= p) (hq : 2 <= q) (hpq : MultiplicativelyIndependent p q)
    {μ : Measure 𝕋} [IsProbabilityMeasure μ] [MeasureTheory.IsAtomLess μ]
    (hmup : MeasurePreserving (Tn p) μ μ)
    (hmuq : MeasurePreserving (Tn q) μ μ) :
    μ = volume := by
```

## Arxiv/2402.13202/CirculantHadamard.lean
/-!
# The circulant Hadamard conjecture

A circulant matrix is generated by cyclically shifting one row. The circulant Hadamard conjecture,
also attributed to Ryser, says that no circulant Hadamard matrix has order greater than $4$.

*Reference:*
* S. Steinerberger,
  [A note on approximate Hadamard matrices](https://arxiv.org/abs/2402.13202)
-/

### circulant_hadamard_conjecture
/-- Every circulant Hadamard matrix has order at most four. -/
```
theorem circulant_hadamard_conjecture {n : ℕ} (v : Fin n → ℝ)
    (hv : Hadamard.IsHadamard' (Matrix.circulant v)) : n ≤ 4 := by
```

## Arxiv/2501.03234/ArithmeticSumS.lean
/-!
# An Arithmetic Sum Associated with the Classical Theta Function

*Reference:* [arxiv/2501.03234](https://arxiv.org/abs/2501.03234)
**An Arithmetic Sum Associated with the Classical Theta Function**
by *Bruce C. Berndt, Raghavendra N. Bhat, Jeffrey L. Meyer, Likun Xie, Alexandru Zaharescu*
-/

### conjecture_1_1
/--
**Conjecture 1.1**: For any odd prime $k$, the sum associated with the classical theta function $θ_3$,
$S(k)$ is positive.
-/
```
theorem conjecture_1_1 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) : 0 < S k := by
```

### conjecture_4_1
/--
**Conjecture 4.1**: For any prime $k$ larger than $5$, $S(k) > k$.
-/
```
theorem conjecture_4_1 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) (hgt : k > 5) : k < S k := by
```

### conjecture_4_2
/--
**Conjecture 4.2**: For any prime $k$ larger than $233$, $S(k) > 2k$.
-/
```
theorem conjecture_4_2 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) (hgt : k > 233) : 2 * k < S k := by
```

### conjecture_4_3
/--
**Conjecture 4.3**: For any prime $k$ larger than $3119$, $S(k) > 3k$.
-/
```
theorem conjecture_4_3 (k : ℕ) (hprim : k.Prime) (hodd : Odd k) (hgt : k > 3119) : 3 * k < S k := by
```

### conjecture_4_4
/--
**Conjecture 4.4**: Given a natural number $n ∈ ℕ$, for all large enough odd prime $k$ (depending on $n$),
$nk < S(k)$.
-/
```
theorem conjecture_4_4 (n : ℕ) : ∀ᶠ (k : ℕ) in Filter.atTop, k.Prime → Odd k → n * k < S k := by
```

## Arxiv/2504.17644/Margulis.lean
/-!
# A conjecture by Margulis on matrix groups

*Reference:* [arxiv/2504.17644v3](https://arxiv.org/abs/2504.17644v3)
**Bounded diagonal orbits in homogeneous spaces over function fields**
by *Qianlin Huang, Ronggang Shi*
-/

### conjecture_1_1
/-- Let `D` be the diagonal group of `SL_n(ℝ)` where n ≥ 3.
Then any relatively compact `D`-orbit in `SL_n(ℝ) / SL_n(ℤ)` is closed. -/
```
theorem conjecture_1_1 {n : ℕ} (hn : 3 ≤ n)
    (g : SL(n, ℝ) ⧸ Subgroup.map (map (Int.castRingHom ℝ)) ⊤)
    (hg : IsCompact <| closure (MulAction.orbit (diagonalSubgroup (Fin n) ℝ) g)) :
    IsClosed <| MulAction.orbit (diagonalSubgroup (Fin n) ℝ) g := by
```

## Arxiv/2604.08040/Conjecture5_5.lean
/-!
# Group structure via subgroup counts

*Reference:* [arXiv:2604.08040v1](https://arxiv.org/abs/2604.08040v1)
**Group Structure via Subgroup Counts**
by *Angsuman Das, Hiranya Kishore Dey, Khyati Sharma* (2026)

For a finite group $G$, let $\mathrm{cyc}(G)$ denote the number of cyclic subgroups of $G$,
and let $t = \pi(G)$ denote the number of distinct prime divisors of $|G|$.

The paper establishes several structural results of the form
"if $\mathrm{cyc}(G)$ or $\mathrm{sub}(G)$ is small relative to $2^t$, then $G$
has a strong structural property":

* $\mathrm{cyc}(G) < 5 \cdot 2^{t-2} \implies G$ is nilpotent (Theorem 3.1)
* $\mathrm{cyc}(G) < 2^{t+1} \implies G$ is supersolvable (Theorem 4.2)
* $\mathrm{sub}(G) < 59 \cdot 2^{t-3} \implies G$ is solvable (Theorem 5.3)

**Conjecture 5.5** proposes the analogue for solvability via cyclic subgroup count:
if $\mathrm{cyc}(G) < 2^{t+2}$, then $G$ is solvable.

* **In-Paper Location:** Conjecture 5.5, Section 5 "Solvability of a group from $\mathrm{sub}(G)$"
  ([PDF page 15](https://arxiv.org/pdf/2604.08040v1#page=15))
* **OpenConjecture ID:** 1512
-/

### solvable_of_cyc_lt
/--
**Conjecture 5.5** (Das, Dey, Sharma 2026):
If a finite group `G` satisfies $\mathrm{cyc}(G) < 2^{t+2}$, where $t = \pi(G)$ is the
number of distinct prime divisors of $|G|$, then `G` is solvable.
-/
```
theorem solvable_of_cyc_lt :
    answer(sorry) ↔ ∀ (G : Type) [Group G] [Fintype G],
      cyc G < 2 ^ (numPrimeFactors G + 2) → IsSolvable G := by
```

## Arxiv/2605.02731/DeanCycles.lean
/-!
# Dean's conjecture on cycles of length divisible by `k`

*References:*
- [arxiv/2605.02731](https://arxiv.org/abs/2605.02731)
  **Existence of cycles of length divisible by 3 or 4**
  by *Ilkyoo Choi, Hojin Chu, Ringi Kim, Boram Park*, where this is Conjecture 1.1.
- [De88] Dean, N., Open problem, in Cycles and Rays. (1988).
- [DeLeSa93] Dean, N. and Lesniak, L. and Saito, A., Cycles of length 0 modulo 4 in graphs.
  Discrete Math. (1993), 133--139.
- [ChSa94] Chen, G. and Saito, A., Graphs with a cycle of length divisible by three.
  J. Combin. Theory Ser. B (1994), 277--292.
-/

### dean_conjecture
/--
**Conjecture 1.1 (Dean, 1988).** For every integer $k \geq 3$, every finite simple graph with
minimum degree at least $k$ contains a cycle whose length is divisible by $k$.

A cycle has length at least `3`, so the divisor is never `0` and the statement is not
satisfied for a trivial reason. `SimpleGraph.minDegree` is `0` on a graph with no vertices and
on a graph with no edges, so the hypothesis excludes both.
-/
```
theorem dean_conjecture :
    answer(sorry) ↔ ∀ (k : ℕ), 3 ≤ k → ∀ (V : Type) [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj], k ≤ G.minDegree →
        ∃ m ∈ G.cycleLengths, k ∣ m := by
```

### dean_conjecture
/--
The case $k = 5$. This is the only case of the conjecture that is still open.
-/
```
theorem dean_conjecture.variants.five :
    answer(sorry) ↔ ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj], 5 ≤ G.minDegree → ∃ m ∈ G.cycleLengths, 5 ∣ m := by
```

## Arxiv/2605.12342/Conjecture1.lean
/-!
# Fernandes' conjecture on the 2-generation of even direct product permutation groups

*Reference:* [arxiv/2605.12342](https://arxiv.org/abs/2605.12342)
**Groups of permutations that are even on maximal proper subsets, and related monoids**
by *Vítor H. Fernandes*

For positive integers $m, n \ge 2$, let $\mathrm{S}_m \times \mathrm{S}_n$ be the direct product of
symmetric groups on $[m] = \{1, \dots, m\}$ and $[n'] = \{1', \dots, n'\}$. Define
$$
\Gamma_{m \oplus n} = \{(\sigma_1, \sigma_2) \in \mathrm{S}_m \times \mathrm{S}_n :
  \mathrm{sgn}(\sigma_1) = \mathrm{sgn}(\sigma_2)\}
$$
to be the index-$2$ subgroup of pairs of permutations with equal parity, i.e., those whose
product action on $[m] \cup [n']$ is an even permutation.

It is known that $\mathrm{rank}(\Gamma_{2 \oplus 2}) = 1$, $\mathrm{rank}(\Gamma_{3 \oplus 3}) = 3$,
$\mathrm{rank}(\Gamma_{4 \oplus 3}) = 3$, and $\mathrm{rank}(\Gamma_{4 \oplus 4}) = 3$.

**Conjecture 1 (Fernandes, 2026):** For all integers $m \ge n \ge 2$ such that
$(m, n) \notin \{(2,2), (3,3), (4,3), (4,4)\}$, the group $\Gamma_{m \oplus n}$ has
rank $2$ (i.e., is $2$-generated).
-/

### conjecture_1
/--
**Conjecture 1 (Fernandes, 2026):**
Let $m \ge n \ge 2$ be integers with $(m, n) \notin \{(2,2), (3,3), (4,3), (4,4)\}$.
Then the group
$$
\Gamma_{m \oplus n} = \{(\sigma_1, \sigma_2) \in \mathrm{S}_m \times \mathrm{S}_n :
  \mathrm{sgn}(\sigma_1) = \mathrm{sgn}(\sigma_2)\}
$$
has rank $2$, i.e., minimal generating set of size $2$.

Note: Fernandes states the conjecture for groups of exact rank $2$, which is why $(2,2)$
is in the exception list: $\Gamma_{2 \oplus 2} \cong C_2$ has rank $1$. The formalised
conclusion `∃ g₁ g₂, closure {g₁, g₂} = ⊤` encodes 2-generation (at most $2$ generators),
which $\Gamma_{2 \oplus 2}$ also satisfies. The other three exceptions $(3,3), (4,3), (4,4)$
have rank $3$ and are genuinely not 2-generated.
-/
```
theorem conjecture_1 {m n : ℕ} (hm2 : 2 ≤ m) (hn2 : 2 ≤ n) (hmn : n ≤ m)
    (h_except : (m, n) ∉ ({(2, 2), (3, 3), (4, 3), (4, 4)} : Set (ℕ × ℕ))) :
    ∃ g₁ g₂ : gammaSubgroup m n, Subgroup.closure {g₁, g₂} = ⊤ := by
```

## Arxiv/2606.03696/BondyLongestCycles.lean
/-!
# Bondy's conjecture on longest cycles in highly connected graphs

*References:*
- [arxiv/2606.03696](https://arxiv.org/abs/2606.03696)
  **Longest cycles and Dirac-type results in highly connected graphs**
  by *Jie Ma, Bo Ning, Ziyuan Zhao*, where this is Conjecture 1.
- [Bo80] Bondy, J. A., Longest paths and cycles in graphs of high degree. (1980).

Take a `k`-connected graph with a large minimum degree. Bondy says that the graph outside any
longest cycle holds no long path.

The case `k = 1` is Dirac's theorem and the case `k = 2` is the theorem of Nash-Williams. The
case `k = 3` is proved. The cases `k ≥ 4` are open.
-/

### bondy_conjecture
/--
**Conjecture 1 (Bondy, 1980).** Let $k \geq 1$ and let $G$ be a $k$-connected graph on $n$
vertices. If $\delta(G) \geq \frac{n + k(k-1)}{k+1}$, then for every longest cycle $C$ of $G$,
every path in $G - V(C)$ has at most $k-1$ vertices.

The bound on the number of vertices of a path is written as `+ 1 ≤ k` rather than `≤ k - 1`,
because subtraction on `ℕ` is truncated. The two forms agree for `k ≥ 1`.

A longest cycle is a cycle whose length is the circumference of `G`.
-/
```
theorem bondy_conjecture :
    answer(sorry) ↔ ∀ (k : ℕ), 1 ≤ k → ∀ (V : Type) [Fintype V] [DecidableEq V]
      (G : SimpleGraph V) [DecidableRel G.Adj], IsKConnected G k →
      ((Fintype.card V : ℝ) + k * (k - 1)) / (k + 1) ≤ G.minDegree →
      ∀ (a : V) (C : G.Walk a a), C.IsCycle → C.length = G.circumference →
      ∀ (u v : offWalk C) (P : (G.induce (offWalk C)).Walk u v), P.IsPath →
        P.support.length + 1 ≤ k := by
```

## Arxiv/2607.03582/LpRogersShephard.lean
/-!
# Planar $L_p$-Rogers-Shephard, the equality case

*Reference:* [arxiv/2607.03582](https://arxiv.org/abs/2607.03582)
**$L_p$-Rogers-Shephard type inequalities for $L_p$-zonoids and symmetric bodies**
by *Matthieu Fradelizi, Auttawich Manui, Mark Meyer, Cheikh Saliou Ndiaye*

Corollary 29 bounds $|K \oplus_p -K|$ against $|K|$ for planar convex bodies with a centre of
symmetry containing the origin, and notes that parallelograms with a vertex at the origin
attain it. Conjecture 5 asks whether they are the only bodies that do.
-/

### isParallelogramAtOrigin_of_volume_lpSum_eq
/--
**Conjecture 5 (Fradelizi-Manui-Meyer-Ndiaye, 2026).** Among planar convex bodies with a
centre of symmetry containing the origin, for $p > 1$, equality in Corollary 29 holds only for
parallelograms with a vertex at the origin.
-/
```
theorem isParallelogramAtOrigin_of_volume_lpSum_eq :
    answer(sorry) ↔ ∀ (K : Set ℝ²), Convex ℝ K → IsCompact K → (interior K).Nonempty →
      HasCentreOfSymmetry K → (0 : ℝ²) ∈ K → ∀ p q : ℝ, 1 < p → 1 / p + 1 / q = 1 →
        volume (lpSum p K (-K)) = ENNReal.ofReal (rsConstant q) * volume K →
          IsParallelogramAtOrigin K := by
```

## Arxiv/2607.05349/MicroscopicWeighting.lean
/-!
# The microscopic weighting on a metric space

*Reference:* [arxiv/2607.05349](https://arxiv.org/abs/2607.05349)
**The microscopic weighting on a metric space**
by *Emily Roff, Simon Willerton*
-/

### microscopic_weighting_iff_finite_concentration
/--
**Conjecture 3.3 (Roff-Willerton, 2026).** A finite metric space admits a microscopic weighting
if and only if its distance matrix has finite concentration.

`Nonempty` is needed and not just tidiness. On the empty space every gauging condition fails,
since `∑ i, g i` is `0` rather than `1`, while `X → ℝ` is a subsingleton so the weighting
converges trivially. The equivalence would be false there for reasons that have nothing to do
with the question.
-/
```
theorem microscopic_weighting_iff_finite_concentration :
    answer(sorry) ↔ ∀ (X : Type) [Fintype X] [DecidableEq X] [Nonempty X] [MetricSpace X],
      HasMicroscopicWeighting X ↔ HasFiniteConcentration (distanceMatrix X) := by
```

## Arxiv/2607.05739/TanArctanSum.lean
/-!
# Integer values of $\tan(\arctan 1 + \arctan 2 + \cdots + \arctan n)$

*References:*
- [arxiv/2607.05739](https://arxiv.org/abs/2607.05739)
  **Integer values of $\tan(\arctan 1+\arctan 2+\cdots+\arctan n)$ are rare** by *Ken Ono*
- [AMM08] T. Amdeberhan, L. A. Medina, and V. H. Moll, *Arithmetical properties of a sequence
  arising from an arctangent sum*, J. Number Theory 128 (2008), no. 6, 1807-1846.
- [TanArctan](https://github.com/AxiomMath/TanArctan), a Lean formalisation of the three
  results of [Ono26], MIT licensed. Its `P`, `A`, `B` and `x` are the definitions used
  here.
-/

### tan_arctan_sum_not_integer
/--
**Conjecture (Amdeberhan-Medina-Moll, 2008).** For every integer $n \geq 5$, the value
$$x_n = \tan(\arctan 1 + \arctan 2 + \cdots + \arctan n)$$
is not an integer.
-/
```
theorem tan_arctan_sum_not_integer :
    answer(sorry) ↔ ∀ n : ℕ, 5 ≤ n → ¬ IsIntegerValue n := by
```

## Arxiv/2607.06396/AlonTarsi.lean
/-!
# The Alon-Tarsi short cycle cover conjecture

*References:*
- [AlTa85] Alon, N. and Tarsi, M., Covering multigraphs by simple circuits.
  SIAM J. Algebraic Discrete Methods (1985), 345--350.
- [arxiv/2607.06396](https://arxiv.org/abs/2607.06396)
  **Some new results on Sylvester colorings of cubic graphs**
  by *Luca Ferrarini, Vahan Mkrtchyan*, where this is Conjecture 4.

Every bridgeless graph has a list of cycles covering every edge whose lengths sum to at most
$\frac{7}{5}|E|$.
-/

### alon_tarsi_short_cycle_cover
/--
**Conjecture 4 (Alon-Tarsi, 1985).** Every bridgeless graph has a list of cycles covering
every edge, with $\sum_{C} |E(C)| \leq \frac{7}{5}|E(G)|$.
-/
```
theorem alon_tarsi_short_cycle_cover :
    answer(sorry) ↔ ∀ (V : Type) [Fintype V] [DecidableEq V] (G : SimpleGraph V)
      [DecidableRel G.Adj], G.IsBridgeless →
      ∃ C : Multiset (Cycle G), IsCycleCover G C ∧
        (totalLength C : ℚ) ≤ 7 / 5 * #G.edgeFinset := by
```

## Arxiv/2607.08366/MinModulus.lean
/-!
# Minimum modulus for the unique multiset-sum problem

*References:*
- [arxiv/2607.08366](https://arxiv.org/abs/2607.08366)
  **Minimum modulus for the unique multiset-sum problem**
  by *José A. R. Fonollosa*
- [jarfo/min-modulus](https://github.com/jarfo/min-modulus), the author's Lean development of
  the paper's Main Theorem. Section 7 of the paper describes it.

The paper's Main Theorem fixes the super-increasing set $\{2^k - 1\}$ and pins the least modulus
at which *it* is valid. Conjecture 1 says no other set of $n$ residues does better, and is open.
-/

### min_modulus
/--
**Conjecture 1 (Fonollosa, 2026).** For every $n \geq 2$ and every
$N < 2^n - 2^{\lfloor \log_2 n\rfloor}$, no set of $n$ residues mod $N$ is valid.

Equivalently the super-increasing set $\{2^k - 1 : 0 \leq k \leq n-1\}$ attains the least
valid modulus, which is `minModulus n`.

`0 < N` excludes `N = 0`, where `ZMod 0` is `ℤ` rather than a finite modulus and `{1, 2}` is
valid, which would make the statement false for a reason unrelated to the question.
-/
```
theorem min_modulus :
    answer(sorry) ↔ ∀ n N : ℕ, 2 ≤ n → 0 < N → N < minModulus n →
      ∀ A : Finset (ZMod N), #A = n → ¬ IsValidMod A := by
```

## Arxiv/math.0110202/BanachMazurRotation.lean
/-!
# Banach-Mazur Rotation Problem

*References:*
- [arxiv/math.0110202](https://arxiv.org/abs/math/0110202)
  **A note on Banach--Mazur problem** by *Beata Randrianantoanina*
- [mathoverflow/41211](https://mathoverflow.net/questions/41211/easy-proof-of-the-fact-that-isotropic-spaces-are-euclidean)
  **Easy proof of the fact that isotropic spaces are Euclidean**
-/

### banach_mazur_rotation_problem
/--
The Banach--Mazur rotation problem asks whether every separable Banach space whose group of linear
isometric equivalences acts transitively on the unit sphere is linearly isometric to a Hilbert
space.
-/
```
theorem banach_mazur_rotation_problem : answer(sorry) ↔
    ∀ (E : Type*) [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] [SeparableSpace E]
      [IsPretransitive (E ≃ₗᵢ[ℝ] E) (sphere (0 : E) 1)], ∃ (H : Type*) (_ : NormedAddCommGroup H)
      (_ : InnerProductSpace ℝ H),
      Nonempty (E ≃ₗᵢ[ℝ] H) := by
```

## Mathoverflow/17560.lean
/-! # Mathoverflow 17560


*Reference:* [mathoverflow/17560](https://mathoverflow.net/questions/17560)
asked by user [Alon-Amit](https://mathoverflow.net/users/25/alon-amit)
-/

### mathoverflow_17560
/--
If $2^x$ and $3^x$ are integers, then $x$ must be an integer.
-/
```
theorem mathoverflow_17560 {x : ℝ} (hx : ∃ m : ℕ, (2 : ℝ) ^ x = m) (hx' : ∃ m : ℕ, (3 : ℝ) ^ x = m) :
    ∃ m : ℕ, x = m := by
```

## Mathoverflow/1973.lean
/-!
# Mathoverflow 1973

Does the 6-sphere $S^6$ admit the structure of a complex manifold?

*Reference:* [mathoverflow/1973](https://mathoverflow.net/questions/1973/)
asked by user [*Fetchinson0234*](https://mathoverflow.net/users/41312/victor-ramos)
-/

### mathoverflow_1973
/--
Does the 6-sphere admit a complex structure, i.e. an atlas of holomorphically compatible charts
relating it to `EuclideanSpace ℂ (Fin 3)`?
-/
```
theorem mathoverflow_1973 :
    answer(sorry) ↔ ∃ atlas : ChartedSpace (EuclideanSpace ℂ (Fin 3)) (unitSphere 6),
      IsManifold 𝓘(ℂ, EuclideanSpace ℂ (Fin 3)) 1 (unitSphere 6) := by
```

## Mathoverflow/21003.lean
/-!
# Mathoverflow 21003

Is there any polynomial $f(x, y) \in \mathbb{Q}[x, y]$ such that
$f : \mathbb{Q} \times \mathbb{Q} \rightarrow \mathbb{Q}$ is a bijection?

*Reference:* [mathoverflow/21003](https://mathoverflow.net/questions/21003)
asked by user [*Z.H.*](https://mathoverflow.net/users/5098/z-h)
-/

### mathoverflow_21003
/--
Is there any polynomial $f(x, y) \in \mathbb{Q}[x, y]$ such that
$f : \mathbb{Q} \times \mathbb{Q} \rightarrow \mathbb{Q}$ is a bijection?
-/
```
theorem mathoverflow_21003 :
    answer(sorry) ↔ ∃ f : MvPolynomial (Fin 2) ℚ, Function.Bijective fun x ↦ f.eval x := by
```

## Mathoverflow/235893.lean
/-!
# Mathoverflow 235893

*Reference:* [mathoverflow/235893](https://mathoverflow.net/questions/235893)
asked by user [*Willie Wong*](https://mathoverflow.net/users/3948/willie-wong)
-/

### mathoverflow_235893
/--
Assume for $n>1$, $f:\mathbb{R}^n\to\mathbb{R}^n$ is a bijection, where $\mathbb{R}^n$ is equipped
with the standard topology. Does the connectedness of (the induced power set map) $f$ imply
that of $f^{-1}$?
-/
```
theorem mathoverflow_235893 :
    answer(sorry) ↔ ∀ n > 1, ∀ (f : ℝ^n ≃ ℝ^n), IsConnectedMap f → IsConnectedMap f.symm := by
```

## Mathoverflow/31809.lean
/-!
# Mathoverflow 31809

Source:
[Mathoverflow/31809](https://mathoverflow.net/questions/31809/pre-triangulated-category-that-isnt-triangulated)

-/

### mathoverflow_31809
/-- Does there exist a category that is pretriangulated but not triangulated? -/
```
theorem mathoverflow_31809 : answer(sorry) ↔ (∀ (C : Type*) [Category C] [Preadditive C]
    [HasZeroObject C] [HasShift C ℤ] [∀ (n : ℤ), (shiftFunctor C n).Additive]
    [Pretriangulated C], IsTriangulated C) := by
```

## Mathoverflow/339137.lean
/-!
# Mathoverflow 339137

Why do polynomials with coefficients 0,1
 like to have only factors with 0,1
 coefficients?

*Reference:* [mathoverflow/339137](https://mathoverflow.net/questions/339137)
asked by user [*Sil*](https://mathoverflow.net/users/136794/sil)
-/

### mathoverflow_339137
/--
Let $P(x), Q(x) ∈ ℝ[x]$ be two monic polynomials with non-negative coefficients.
If $R(x) = P(x)Q(x)$ is a $0,1$ polynomial (coefficients only from $\{0,1\}$), then $P(x)$ and $Q(x)$
are also $0, 1$ polynomials.
-/
```
theorem mathoverflow_339137 (P Q R : ℝ[X]) (hP: P.Monic) (hQ : Q.Monic)
    (hp : ∀ c ∈ P.coeffs, 0 ≤ c) (hq : ∀ c ∈ Q.coeffs, 0 ≤ c)
    (h : R = P * Q) (hR : IsZeroOne R) :
    IsZeroOne P ∧ IsZeroOne Q := by
```

## Mathoverflow/34145.lean
/-!
# Mathoverflow 34145

Can the unit square be covered by $1/k$-by-$1/(k+1)$ rectangles (across $1 \le k$ natural)?

I am deliberately not requiring that the rotations can only be $0^\circ, 90^\circ, 180^\circ, \text{ or } 270^\circ$.

Because of indexing, since `n : ℕ` starts at 0, we change the side lengths to $1 / (n + 1)$ and
$1 / (n + 2)$, so that the first rectangle is $1/1$ by $1/2$, the second is $1/2$ by $1/3$, etc.

*Reference:* [mathoverflow/34145](https://mathoverflow.net/q/34145)
asked by user [*Kaveh*](https://mathoverflow.net/users/7507/kaveh)
-/

### rectangles_cover_unit_square
/-- Can a unit square be covered by rectangles of width `1 / (n + 1)` and height `1 / (n + 2)`? -/
```
theorem rectangles_cover_unit_square :
    answer(sorry) ↔ ∃ c : Configuration, ∀ p ∈ unitSquare, ∃ n, p ∈ (c.rect n).toSet := by
```

### rectangles_pack_unit_square
/-- Equivalently, can a unit square be packed with rectangles of width `1 / (n + 1)` and height
`1 / (n + 2)`? -/
```
theorem rectangles_pack_unit_square :
    answer(sorry) ↔ ∃ c : Configuration, (∀ n, (c.rect n).toSet ⊆ unitSquare) ∧ c.IsPacking := by
```

## Mathoverflow/347178.lean
/-!
# Mathoverflow 347178

*Reference:* [mathoverflow/347178](https://mathoverflow.net/questions/347178)
asked by user [*Biagio Ricceri*](https://mathoverflow.net/users/149235/biagio-ricceri)
-/

### mathoverflow_347178
/--
Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Does the equality
$$\sup_{x \in \mathbb R^n}f(x) = \sup_{x\in \mathbb R^n} f(x+\nabla f(x))$$
hold when both suprema are finite?
-/
```
theorem mathoverflow_347178.variants.bounded_only :
    answer(sorry) ↔ ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (hf : ContDiff ℝ 1 f)
        (h : BddAbove (range f)) (h' : BddAbove (range (fun x ↦ f (x + gradient f x)))),
        (⨆ x, f x) = ⨆ x, f (x + gradient f x) := by
```

## Mathoverflow/434111.lean
/-!
# Are prime numbers among sums of prime numbers distributed as $\frac n{2\ln(n)}$?

*Reference:*

[mathoverflow.net/questions/434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn)

[Me18] Meštrović, R., *Curious Conjectures on the Distribution of Primes
Among the Sums of the First `2n` Primes*, [arXiv:1804.04198](https://arxiv.org/abs/1804.04198)
(2018), Conjecture 3.3.
-/

### restricted_prime_number_theorem
/-- The conjecture claims that $\pi_n\sim\frac n{2\ln(n)}$.

In other words, primes are distributed among the much sparser sequence $(S_n)_n$
with essentially the same density as in the positive integers, up to a factor of $2$.

[MathOverflow 434111](https://mathoverflow.net/questions/434111/are-prime-numbers-among-sums-of-prime-numbers-distributed-as-frac-n2-lnn).

[Me18] Meštrović, R., *Curious Conjectures on the Distribution of Primes
Among the Sums of the First `2n` Primes*, [arXiv:1804.04198](https://arxiv.org/abs/1804.04198)
(2018).
-/
```
theorem restricted_prime_number_theorem :
    answer(sorry) ↔ ((fun n : ℕ => (piRestricted n : ℝ)) ~[atTop] (fun n : ℕ => (n : ℝ) / (2 * Real.log n))) := by
```

### restricted_prime_number_theorem
/--
Meštrović's original formulation [Me18, Conjecture 3.3]: the sequence of sums of the
first $2m$ primes satisfies the Restricted Prime Number Theorem, $\pi(m, (S_{2m})) \sim \frac{m}{\ln m}$.
-/
```
theorem restricted_prime_number_theorem.variants.even_subsequence :
    answer(sorry) ↔
      ((fun m : ℕ => (((Finset.Icc 1 m).filter (fun k => Nat.Prime (S (2 * k)))).card : ℝ)) ~[atTop]
        (fun m : ℕ => (m : ℝ) / Real.log m)) := by
```

## Mathoverflow/75792.lean
/-!
# Mathoverflow 75792

Various questions about integer complexity, which is the minimum number of `1`s needed to express a natural number using addition, multiplication, and parentheses.

Let `‖n‖` denote the integer complexity of `n > 0`.
* It is known that `‖3^n‖ = 3n` for `n > 0`.
* Is it true that `‖2^n‖ = 2n` for `n > 0`?
* The corresponding conjecture for `5` is false, because
  `5^6 = 15625 = 1 + 2^3 * 3^2 * (1 + 2^3 * 3^3)`!

We have chosen to formalise this using an inductive type.

*References:*
 - [mathoverflow/75792](https://mathoverflow.net/a/75792) by user [Harry Altman](https://mathoverflow.net/users/5583)
 - http://arxiv.org/abs/1203.6462 by Jānis Iraids, Kaspars Balodis, Juris Čerņenoks, Mārtiņš Opmanis, Rihards Opmanis, Kārlis Podnieks
 - http://arxiv.org/abs/1207.4841 by Harry Altman, Joshua Zelinsky
 - https://oeis.org/A5245 : Mahler-Popken complexity.
-/

### complexity_two_pow
/-- Is `2n` the complexity of `2^n` for `0 < n`? -/
```
theorem complexity_two_pow : answer(sorry) ↔ ∀ n : ℕ, 0 < n → complexity (2 ^ n) = 2 * n := by
```

## OEIS/100434.lean
/-!
# Expansion of g.f. $(1+x)(3+x)/(1+6x^2+x^4)$

This sequence is defined by the linear recurrence relation
$a(n) = -6 a(n-2) - a(n-4)$ for $n \ge 4$,
with initial values $a(0)=3$, $a(1)=4$, $a(2)=-17$, $a(3)=-24$.

*References:*
- [A100434](https://oeis.org/A100434)
-/

### conjecture1
/--
**Conjecture from Creighton Dement (A100434)**:
Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
Then for all $n \ge 0$, $c(n) + d(n) = b(n)$.
-/
```
theorem conjecture1 (n : ℕ) : c n + d n = b n := by
```

### conjecture2
/--
**Conjecture from Creighton Dement (A100434)**:
Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
Then for all $n \ge 0$, $e(n) + f(n) = b(n)$.
-/
```
theorem conjecture2 (n : ℕ) : e n + f n = b n := by
```

### conjecture3
/--
**Conjecture from Creighton Dement (A100434)**:
Let the auxiliary sequences c, d, e, f, g, b be defined as specified.
Then for all $n \ge 0$, $g(n) + a(n) = b(n)$.
-/
```
theorem conjecture3 (n : ℕ) : g n + a n = b n := by
```

## OEIS/100474.lean
/-!
# Conjectures associated with A100474

$a(1) = 1$; $a(n)$ is the smallest integer such that $a(n) + a(n-1)$ has the first $n$ distinct
prime factors not used before in this construction.

*References:*
- [A100474](https://oeis.org/A100474)
-/

### conjecture
/--
After $a(2) = 5$, is there another prime?
-/
```
theorem conjecture : answer(sorry) ↔ ∃ n > 2, (a n).Prime := by
```

## OEIS/100475.lean
/-!
# Prime-th recurrence with reversal at each step

$$a(n) = \operatorname{reversal}(p_{a(n-1)})$$
with $a(0)=1$, where $p_k$ is the $k$-th prime number.

*References:*
- [A100475](https://oeis.org/A100475)
-/

### conjecture
/--
Starting at other than $a(n) = 1$, does this sequence ever go into a loop?
-/
```
theorem conjecture (x : ℕ) (h : x ≠ 1) :
    answer(sorry) = IsUltimatelyPeriodic (aStartAt x) := by
```

## OEIS/100800.lean
/-!
# Conjectures associated with A100800

Let $f(n) = n + \text{sum of the digits of } n$. If $f(n)$ is multiple of $n$ then $a(n)= f(n)$
else $a(n) = f(f(f(n)))\dots$ until one gets a multiple of $n$; $a(n) = 0$ if no such number
exists.

*References:*
- [A100800](https://oeis.org/A100800)
-/

### conjecture
/-- A100800 Conjecture: No term is zero. -/
```
theorem conjecture : ∀ (n : ℕ), n ≠ 0 → a n ≠ 0 := by
```

## OEIS/101779.lean
/-!
# Conjectures associated with A101779

$a(n)$ is the least $k$ such that all of $k, 2k+1, 3k+2, ..., nk+n-1$ are primes,
or $0$ if no such $k$ is found.
It is conjectured $k$ always exists.

*References:*
- [A101779](https://oeis.org/A101779)
-/

### conjecture
/--
It is conjectured k always exists.
-/
```
theorem conjecture : ∀ (n : ℕ), 1 ≤ n → ∃ k : ℕ, Ak n k := by
```

## OEIS/102847.lean
/-!
# $a(0) = 1$, $a(n) = a(n-1)a(n-1) + 2$

*References:*
- [A102847](https://oeis.org/A102847)
-/

### conjecture
/--
Prime for $a(1) = 3$, $a(2) = 11$, $a(4) = 15131$; semiprime for $a(3) = 123 = 3 * 41$,
$a(5) = 228947163 = 3 * 76315721$.
$a(6)$, added by Jonathan Vos Post, has 4 prime factors.
$a(7) = 41 * 811^2 * 106693969 * 317171188688357726699 * 8272236925540996054440172449761$.
When is the next prime in the sequence?
-/
```
theorem conjecture : answer(sorry) = sInf {n : ℕ | 4 < n ∧ (a n).Prime} := by
```

## OEIS/103151.lean
/-!
# Number of decompositions of $2n+1$ into $2p+q$, where $p$ and $q$ are both odd primes

*References:*
- [A103151](https://oeis.org/A103151)
-/

### conjecture
/--
Conjecture: all items for $n \ge 4$ are greater than or equal to $1$. This is a stronger
conjecture than the Goldbach conjecture.
-/
```
theorem conjecture (n : ℕ) (hn : n ≥ 4) : a n ≥ 1 := by
```

## OEIS/103425.lean
/-!
# $a(n) = 3a(n-1) + a(n-2) - 3a(n-3)$

*References:*
- [A103425](https://oeis.org/A103425)
-/

### conjecture
/--
The current sequence contains primes, including $3, 5, 41, 21523361$.
Is there an $(a, b, c)$ weighted tribonacci sequence with $a, b, c$ relatively prime
which is prime-free?
-/
```
theorem conjecture : answer(sorry) ↔
    ∃ (a b c : ℤ) (x : ℕ → ℤ),
      Nat.gcd (Int.gcd a b) c.natAbs = 1 ∧
      IsWeightedTribonacci a b c x ∧
      ∀ n, ¬ (x n).natAbs.Prime := by
```

## OEIS/103662.lean
/-!
# Smallest power with base>1 and exponent $n$ without digit 0

For statistical reasons it is conjectured that the sequence is finite.
Also it is conjectured that $a(40)$ does not exist (i.e. the sequence is empty for $n=40$).

*References:*
- [A103662](https://oeis.org/A103662)
-/

### conjecture
/--
For statistical reasons it is conjectured that the sequence is finite.
This is formalized as the assertion that for large enough $n$, no valid zeroless power exists,
which in our definition results in $a(n) = 0$.
-/
```
theorem conjecture : ∃ N : ℕ, ∀ n : ℕ, n > N → a n = 0 := by
```

### conjecture
/--
$a(40)$, if it exists, is not known.

This claim is rooted in the finiteness conjecture. The most direct mathematical expression
of the open problem concerning $a(40)$ is the negation of the existence of a valid base.
-/
```
theorem conjecture.variants.a_40 :
  ¬ ∃ (b : ℕ), IsValidZerolessPower 40 b := by
```

## OEIS/103885.lean
/-!
# $a(n) = [x^{2n}] \left(\frac{1 + x}{1 - x}\right)^n$

The sequence is given by the combinatorial identity:
$a(n) = \sum_{k = 0}^n \binom{n}{k} \binom{2n+k-1}{n-1}$
with $a(0) = 1$.

*References:*
- [A103885](https://oeis.org/A103885)
-/

### conjecture
/--
The recurrence given below can be rewritten in the form
$$(2n+1)(2n+2)P(2,n)a(n+1) - (2n-1)(2n-2)P(2,-n)a(n-1) = Q(2,n^2)a(n),$$
where the polynomial $Q(2,n) = 4(55n^2 - 34n + 3)$ and the polynomial $P(2,n) = 5n^2 - 5n + 1$
satisfies the symmetry condition $P(2,n) = P(2,1-n)$ and has real zeros.
More generally, for fixed $m = 1,2,3, \ldots$, we conjecture that the sequence $b(n) := a(mn)$
satisfies a recurrence of the form
$$( \prod_{k = 1}^{2m} (2mn + k) )P(2m,n)b(n+1) + (-1)^m( \prod_{k = 1}^{2*m} (2mn - k) )
  P(2m,-n)b(n-1) = Q(2m,n^2)b(n),$$
where the polynomials $P(2m,n)$ and $Q(2m,n)$ have degree $2m$. Conjecturally, the polynomial
$P(2m,n) = P(2m,1-n)$ and has real zeros in the interval [0, 1].
The $4m$ zeros of the polynomial $Q(2m,n^2)$ seem to belong to the interval $[-1, 1]$ and
$4m - 2$ of these zeros appear to be approximated by the rational numbers
$\pm k/(3m)$, where $1 \le k \le 3m - 2$, $k$ not a multiple of $3$.
-/
```
theorem conjecture (m : ℕ) (hm : 1 ≤ m) :
    ∃ (P Q : Polynomial ℝ),
      -- P and Q have degree 2m
      P.degree = (2 * m : ℕ) ∧ Q.degree = (2 * m : ℕ) ∧
      -- The recurrence relation holds for all n >= 1
      (∀ (n : ℕ) (hn : 1 ≤ n),
        (prodFactorPlus m n * P.eval (n : ℝ)) * (aSubsequenceReal m (n + 1)) +

        ((-1 : ℝ) ^ m * prodFactorMinus m n * P.eval (-(n : ℝ))) * (aSubsequenceReal m (n - 1)) =

        (Q.eval ((n : ℝ)^2)) * (aSubsequenceReal m n)) ∧

      -- P symmetry: P(x) = P(1-x)
      (∀ x : ℝ, P.eval x = P.eval (1 - x)) ∧

      -- P has real zeros in [0, 1]: all complex zeros are real and in [0, 1]
      (∀ z : ℂ, (P.map (algebraMap ℝ ℂ)).eval z = 0 → z.im = 0 ∧ z.re ∈ (Set.Icc 0 1)) ∧

      -- Q zero properties: The zeros of Q(x^2) are real and in [-1, 1].
      (∀ z : ℂ, (Q.map (algebraMap ℝ ℂ)).eval (z^2) = 0 → z.im = 0 ∧ z.re ∈ (Set.Icc (-1) 1)) := by
```

## OEIS/104320.lean
/-!
# Number of zeros in ternary representation of $2^n$

*References:*
- [A104320](https://oeis.org/A104320)
-/

### conjecture
/--
Conjecture from N. J. A. Sloane: $a(n) > 0$ for $n > 15$.
-/
```
theorem conjecture : ∀ n : ℕ, 15 < n → a n > 0 := by
```

## OEIS/105020.lean
/-!
# Array read by upward antidiagonals

Array read by upward antidiagonals: row $n$ ($n \ge 0$) contains the numbers
$m^2 - n^2$, $m \ge n+1$.

*References:*
- [A105020](https://oeis.org/A105020)
-/

### conjecture
/--
A "Goldbach Conjecture" for this sequence: when there are $n$ terms between consecutive odd
integers $2n+1$ and $2n+3$ for $n > 0$, at least one will be the product of 2 primes
(not necessarily distinct). Example: $n=3$ for consecutive odd integers $a(7) = 7$ and
$a(11) = 9$ and of the 3 sequence entries $a(8) = 12$, $a(9) = 15$ and $a(10) = 16$ between
them, one is the product of 2 primes $a(9) = 15=3*5$. - _Michael Hiebl_, Jul 15 2007
-/
```
theorem conjecture :
  ∀ (n i j : ℕ), 1 ≤ n →
    a i = 2 * n + 1 →
    a j = 2 * n + 3 →
    j = i + n + 1 →
    ∃ (k : ℕ),
      i < k ∧
      k < j ∧
      (a k).IsSemiprime := by
```

## OEIS/105210.lean
/-!
# Conjectures associated with A105210

$a(1) = 393$; for $n > 1$, $a(n) = a(n-1)$ + 1 + sum of distinct prime factors of $a(n-1)$
that are $< a(n-1)$.

*References:*
- [A105210](https://oeis.org/A105210)
-/

### conjecture_disjoint_starting_values
/--
Cormier and Selfridge found 5 starting values for which the sequences appear to not merge.
The sequences were checked up to 10^8.
-/
```
theorem conjecture_disjoint_starting_values :
    ∀ j k : ℕ,
      j ∈ ({1, 393, 412, 668, 932} : Set ℕ) →
      k ∈ ({1, 393, 412, 668, 932} : Set ℕ) →
      j ≠ k →
      sequenceSet j ∩ sequenceSet k = ∅ := by
```

### conjecture
/--
This suggests that there may be infinitely many different (non-merging) sequences obtained
by choosing different starting values.
-/
```
theorem conjecture :
  ∃ K : Set ℕ,
    Set.Infinite K ∧
    (∀ k ∈ K, 1 ≤ k) ∧
    (∀ j k : ℕ,
      j ∈ K → k ∈ K → j ≠ k →
      sequenceSet j ∩ sequenceSet k = ∅) := by
```

## OEIS/105720.lean
/-!
# Triangular matchstick numbers in the class of prime numbers

$a(n) = \sum_{k = n}^{2n} p_k$, where $p_k$ is the $k$-th prime.

*References:*
- [A105720](https://oeis.org/A105720)
-/

### conjecture
/--
Terms are squares at only(?) three values of $n = 3, 6, 4072$:
corresponding terms are 6^2, 13^2, and 15735^2.
-/
```
theorem conjecture :
    ∀ n : ℕ, 0 < n → (IsSquare (a n) ↔ (n = 3 ∨ n = 6 ∨ n = 4072)) := by
```

## OEIS/105751.lean
/-!
# Imaginary part of $\prod_{k=0}^n (1 + k \cdot i)$, $i = \sqrt{-1}$

*References:*
- [A105751](https://oeis.org/A105751)
-/

### conjecture
/--
Moll's conjecture 5.5 extends to this sequence and takes the form:
(ii) for the other primes of type $2$, the p-adic valuation
$\nu_p(a(n)) \sim n/(p - 1)$ as $n \rightarrow \infty$.

(Type 2 primes consists of primes p == 1 (mod 4))
-/
```
theorem conjecture.variants.moll_p_mod_4_eq_1 {p : ℕ} (hp : p.Prime) (h_mod : p % 4 = 1) :
    Tendsto (fun n ↦ ((p - 1 : ℚ) * (padicValInt p (a n) : ℚ)) / (n : ℚ)) atTop (nhds 1) := by
```

## OEIS/107247.lean
/-!
# Sum of squares of nonacci numbers

Sum of squares of nonacci numbers (Fibonacci 9-step numbers).

*References:*
- [A107247](https://oeis.org/A107247)
-/

### conjecture
/--
Primes in this sequence include: $a(8) = 2$, which is next?
-/
```
theorem conjecture :
    answer(sorry) = a (sInf {n : ℕ | 8 < n ∧ (a n).Prime}) := by
```

## OEIS/108081.lean
/-!
# $a(n) = \sum_{i=0}^n \binom{2n-i}{n+i}$

Alternatively the sequence `a` can be defined as
$a(n) = \sum_{k=0}^n \binom{n+k-1}{k} F(n-k+1)$, where $F(m)$ is the $m$-th Fibonacci number.
We formalize a conjecture about the number of words of length $n$ in a set $X$ being related
to this sequence.

*References:*
- [A108081](https://oeis.org/A108081)
-/

### count_words_in_x_is_a_shifted
/--
"The number of words of length $n$ for $n \le 12$ is given by $a(n+1)$. Is this always true?"

Formalized as $|X_n| = a(n-1)$ for $n \ge 1$, because the sequence values $a(0)=1, a(1)=2, a(2)=7$
match the examples given for word lengths $n=1, 2, 3$ respectively.
-/
```
theorem count_words_in_x_is_a_shifted (n : ℕ) :
    n ≥ 1 → Set.ncard (xN n) = a (n - 1) := by
```

## OEIS/108129.lean
/-!
# Riesel Problem

Riesel problem: let $k=2n-1$; then $a(n)$ is the smallest $m \ge 1$ such that
$k \cdot 2^m-1$ is prime, or $-1$ if no such prime exists.

*References:*
- [A108129](https://oeis.org/A108129)
-/

### conjecture
/--
It is conjectured that the integer $k = 509203$ is the smallest Riesel number,
that is, the first $n$ such that $a(n) = -1$ is $254602$.
-/
```
theorem conjecture :
  a 254602 = -1 ∧ (∀ n : ℕ, 1 ≤ n ∧ n < 254602 → a n ≠ -1) :=
by sorry

end OeisA108129
```

## OEIS/108211.lean
/-!
# $a(n) = 16n^2 + 1$

*References:*
- [A108211](https://oeis.org/A108211)
-/

### conjecture
/--
Conjecture:
$$a(n) = \left\lfloor \frac{1}{\frac{1}{4n} - \log(2) +
  \frac{1}{n+1} + \frac{1}{n+2} + \dots + \frac{1}{2n}} \right\rfloor.$$
-/
```
theorem conjecture (n : ℕ) (hn : n > 0) :
    (a n : ℝ) =
      (⌊ 1 / ((4 * n : ℝ)⁻¹ - log 2 + ∑ k ∈ (Finset.Icc (n + 1) (2 * n)), (k : ℝ)⁻¹) ⌋ : ℝ) := by
```

## OEIS/108301.lean
/-!
# Digital sum of the Fermat number $2^{2^n} + 1$

`a n` is the digital sum of the Fermat number $2^{2^n} + 1$.
The conjecture asks if there are any prime numbers in this sequence beyond $n=11$.

*References:*
- [A108301](https://oeis.org/A108301)
-/

### conjecture
/-- $a(0)$, $a(1)$, $a(5)$, $a(6)$, $a(7)$ and $a(11)$ are primes. Are there any more? -/
```
theorem conjecture : answer(sorry) ↔ ∃ n > 11, (a n).Prime := by
```

## OEIS/108569.lean
/-!
# Numbers $n$ such that $\phi(n) = \phi(n + \phi(n))$

*References:*
- [A108569](https://oeis.org/A108569)
-/

### conjecture
/-- Conjecture: Except for the first term all terms are even. -/
```
theorem conjecture : ∀ n, 0 < n → Even (a n) := by
```

## OEIS/108864.lean
/-!
# Numbers $n$ such that the perfect deficiency of $n$ is $\le 10$.

We formally define the property satisfied by elements of the sequence,
using the sum of divisors function $\sigma_1(n)$.

*References:*
- [A108864](https://oeis.org/A108864)
-/

### conjecture
/--
Is 1155 the last odd number in this sequence?
(1155 is the 59th term starting from 1, corresponding to `a 58 = 1155`).
-/
```
theorem conjecture :
    answer(sorry) ↔ ∀ n > 58, Even (a n) := by
```

## OEIS/108866.lean
/-!
# Numerator of $\sum_{k=1}^n 2^k/k$.

Conjecture: for $n > 3$,
$\textrm{numerator}(-2/n + \sum_{k=1}^{n} \frac{2^k}{k}) == 0 (\textrm{mod} n^2)$
if and only if n is prime.

*References:*
- [A108866](https://oeis.org/A108866)
-/

### conjecture
/--
Conjecture: for $n > 3$,
$\textrm{numerator}(-2/n + \sum_{k=1}^{n} \frac{2^k}{k}) == 0 (\textrm{mod} n^2)$
if and only if n is prime.
-/
```
theorem conjecture {n : ℕ} (hn : n > 3) :
    (ratExpression n).num ≡ 0 [ZMOD (n^2 : ℤ)] ↔ n.Prime := by
```

## OEIS/109074.lean
/-!
# Numerator of $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right)$

Conjecture: $\binom{6n-2}{2n} / \left(2 \binom{4n-1}{2n}\right) = A005156(n+1)/A005156(n)$

*References:*
- [A109074](https://oeis.org/A109074)
-/

### conjecture
/--
It is conjectured that binomial(6*n-2,2*n)/(2 * binomial(4*n-1,2*n)) = A005156(n+1)/A005156(n).
-/
```
theorem conjecture (n : ℕ) (h_pos : n ≥ 1) :
    frac n = (b (n + 1) : ℚ) / (b n : ℚ) := by
```

## OEIS/109227.lean
/-!
# Conjectures associated with A109227

Binary strings that have 1's where primes occur, 0's elsewhere and every term ends
with the $n$-th prime index.

Conjecture: $a(2)$ and $a(121)$ are primes. Are there any more?

*References:*
- [A109227](https://oeis.org/A109227)
-/

### conjecture
/--
Conjecture: $a(2)$ and $a(121)$ are primes. Are there any more?
-/
```
theorem conjecture :
    answer(sorry) ↔ ∃ n > 0, n ≠ 2 ∧ n ≠ 121 ∧ (a n).Prime := by
```

## OEIS/109671.lean
/-!
# Conjectures associated with A109671

$a(1)=1$; thereafter, $a(2n)=a(n)$, $a(2n+1)$ is the smallest positive number
such that $|a(2n+1)-a(2n-1)|=a(n)$.
Conjecture: Does the sequence contain every positive integer?

*References:*
- [A109671](https://oeis.org/A109671)
-/

### conjecture
/--
Does the sequence contain every positive integer (cf. A169741)?
-/
```
theorem conjecture :
    answer(sorry) ↔ ∀ m : ℕ, 0 < m → ∃ n : ℕ, 0 < n ∧ a n = m := by
```

## OEIS/109845.lean
/-!
# Conjectures associated with A109845

$a(1) = 2$; $a(2n)$ = lcm of all previous terms + 1; $a(2n+1)$ = lcm of all previous terms - 1.

*References:*
- [A109845](https://oeis.org/A109845)
-/

### conjecture
/--
Conjecture: There are infinitely many primes in this sequence.
-/
```
theorem conjecture : Set.Infinite {n : ℕ | (a n).Prime} := by
```

## OEIS/109905.lean
/-!
# Conjectures associated with A109905

$a(n)$ is the greatest prime of the form $k(n-k)+1$, where $k$ can take values from
$1$ to $\lfloor n/2 \rfloor$. $a(n)=0$ if no such prime exists.

*References:*
- [A109905](https://oeis.org/A109905)
-/

### conjecture
/--
$a(n) = 0$ for $n = 1$, $6$, $30$ and $54$. Are there any others?
-/
```
theorem conjecture : answer(sorry) ↔ {n : ℕ | n > 0 ∧ a n = 0} = {1, 6, 30, 54} := by
```

## OEIS/109908.lean
/-!
# Conjectures associated with A109908

$a(n)$ = greatest prime of the form $k(n-k)-1$, or $0$ if no such prime exists.

*References:*
- [A109908](https://oeis.org/A109908)
-/

### conjecture
/--
Conjecture: $a(n) > 0$ for $n > 3$.
-/
```
theorem conjecture : ∀ n > 3, a n > 0 := by
```

## OEIS/109909.lean
/-!
# Conjectures associated with A109909

$a(n)$ = number of primes of the form $k(n-k)-1$.

*References:*
- [A109909](https://oeis.org/A109909)
-/

### conjecture
/--
Conjecture: $a(n) > 0$ for $n > 3$.
-/
```
theorem conjecture : ∀ n > 3, a n > 0 := by
```

## OEIS/110475.lean
/-!
# Number of symbols '*' and '^' to write the canonical prime factorization of n

The canonical prime factorization is $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$.
The written form is $p_1^{\wedge} e_1 * p_2^{\wedge} e_2 * \cdots * p_k^{\wedge} e_k$,
where the $\wedge$ appears only if $e_i > 1$.
$a(n) = (\text{number of distinct prime factors}) - 1 +$
$(\text{number of distinct prime factors with exponent } > 1)$.

*References:*
- [A110475](https://oeis.org/A110475)
-/

### conjecture
/--
It is conjectured that $1,2,3,4,5,6,7,9,11$ are the only positive integers
which cannot be represented as the sum of two elements of indices $n$ such that $a(n) = 1$.
-/
```
theorem conjecture :
  ∀ m > 0, m ∉ exceptionalSet ↔ ∃ x y : ℕ, a x = 1 ∧ a y = 1 ∧ m = x + y := by
```

## OEIS/110566.lean
/-!
# $a(n) = \operatorname{lcm}\{1,2,\dots,n\}/\operatorname{denom}(H(n))$

*References:*
- [A110566](https://oeis.org/A110566)
-/

### conjecture
/--
It is conjectured that every odd number occurs in this sequence.
-/
```
theorem conjecture :
  ∀ m : ℕ, Odd m → ∃ n > 0, a n = m := by
```

## OEIS/110835.lean
/-!
# Smallest $m > 0$ such that there are no primes between $nm$ and $n(m+1)$ inclusive.

Sierpinski's conjecture (1958) is precisely that a(n) >= n for all n.

*References:*
- [A110835](https://oeis.org/A110835)
-/

### conjecture
/--
Sierpinski's conjecture (1958) is precisely that $a(n) >= n$ for all $n$.
-/
```
theorem conjecture : ∀ n > 0, a n ≥ n := by
```

## OEIS/110854.lean
/-!
# Conjectures associated with A110854

$a(n) = \mathrm{prime}(2n+2) - \mathrm{prime}(2n+1) - \mathrm{prime}(2n) + \mathrm{prime}(2n-1)$,
where $\mathrm{prime}(k)$ is the $k$-th prime number.

*References:*
- [A110854](https://oeis.org/A110854)
-/

### conjecture
/--
Do the absolute values cover A004275?
A004275 is the set of all differences between two prime numbers.
The conjecture asks whether every possible difference between two prime numbers
occurs as the absolute value of some term $a(n)$.
-/
```
theorem conjecture :
  ∀ d > 0, (∃ p1 p2 : ℕ, p1.Prime ∧ p2.Prime ∧ d = (p1 - p2 : ℤ).natAbs) →
  ∃ n > 0, d = (a n).natAbs := by
```

## OEIS/111114.lean
/-!
# Integer part of $\mathrm{prime}(n)/\pi(n)$

Here $\mathrm{prime}(n)$ is the $n$-th prime number, and $\pi(n)$ is the prime-counting function.

*References:*
- [A111114](https://oeis.org/A111114)
-/

### conjecture
/--
Conjecture: As $n \rightarrow \infty$, there are infinitely many n's such that
$a(n)$ is greater than $a(n+1)$.
-/
```
theorem conjecture : ∃ᶠ n in atTop, a n > a (n + 1) := by
```

## OEIS/111291.lean
/-!
# Number of refactorable numbers (A033950) $\le 10^n$

A number $k$ is refactorable if its number of divisors, $\tau(k)$, divides $k$.

*References:*
- [A111291](https://oeis.org/A111291)
-/

### conjecture
/--
Simon Colton conjectures that the number of refactorables less than x is at least x/(2 log(x)).
-/
```
theorem conjecture : ∀ (x : ℝ), x > 1 →
    (countRefactorable x : ℝ) ≥ x / (2 * Real.log x) := by
```

## OEIS/113010.lean
/-!
# Number of digits of n raised to the power of the sum of the digits of n

*References:*
- [A113010](https://oeis.org/A113010)
-/

### conjecture
/--
$n=1$ and $32$ are two fixed points. Are there any others?
-/
```
theorem conjecture : answer(sorry) ↔ ∀ n : ℕ, a n = n ∧ n > 0 → n = 1 ∨ n = 32 := by
```

## OEIS/113019.lean
/-!
# Number of digits of n raised to the power of the digital root of n

*References:*
- [A113019](https://oeis.org/A113019)
-/

### conjecture
/--
$n=1$ and $32$ are fixed points. Are there any others?
-/
```
theorem conjecture : answer(sorry) ↔ ∀ n : ℕ, a n = n → n = 1 ∨ n = 32 := by
```

## OEIS/113213.lean
/-!
# Smallest number $m$ such that $2^n - m$ and $2^n + m$ are primes


*References:*
- [A113213](https://oeis.org/A113213)
-/

### conjecture
/--
Conjecture: $a(n) = O(n^3)$.
-/
```
theorem conjecture :
    (fun n : ℕ => (a n : ℝ)) =O[Filter.atTop] (fun n : ℕ => (n ^ 3 : ℝ)) := by
```

## OEIS/113257.lean
/-!
# Ascending descending base exponent transform of squares

a n is $\sum_{i=1}^n (i^2)^((n-i+1)^2)$.

*References:*
- [A113257](https://oeis.org/A113257)
-/

### conjecture1
/--
The smallest prime in this sequence is $a(2) = 5$. What is the next prime?
-/
```
theorem conjecture1 :
    answer(sorry) = a (sInf {n : ℕ | 2 < n ∧ (a n).Prime}) := by
```

### conjecture2
/--
What is the first square value after 1?
-/
```
theorem conjecture2 :
    answer(sorry) = a (sInf {n : ℕ | 1 < n ∧ IsSquare (a n)}) := by
```

## OEIS/113258.lean
/-!
# Ascending descending base exponent transform of factorials

*References:*
- [A113258](https://oeis.org/A113258)
-/

### conjecture
/--
Is there a nontrivial power after $a(4) = 5^3$?
-/
```
theorem conjecture :
  answer(sorry) ↔ ∃ n > 4, ∃ b > 1, ∃ e > 1, a n = b ^ e := by
```

## OEIS/113271.lean
/-!
# Ascending descending base exponent transform of $2^n$

*References:*
- [A113271](https://oeis.org/A113271)
-/

### conjecture1
/--
The smallest primes in this (always odd) sequence are $a(1) = 3$, $a(3) = 41$ and $a(5) = 543$.
What is the next prime?
-/
```
theorem conjecture1 :
  answer(sorry) = a (sInf {n : ℕ | 5 < n ∧ (a n).Prime}) := by
```

## OEIS/113609.lean
/-!
# Number of prime powers $q<=n$ such that also $q+2$ is a prime power

*References:*
- [A113609](https://oeis.org/A113609)
-/

### conjecture
/--
(25,27) is the smallest pair of prime powers (q,q+2) such that both q and q+2 are not primes,
conjecture: there are more (but not < 10^6).
-/
```
theorem conjecture :
  answer(sorry) ↔ ∃ q ≥ 1000000,
    IsOeisPrimePower q ∧ IsOeisPrimePower (q + 2) ∧
    ¬ q.Prime ∧ ¬ (q + 2).Prime := by
```

## OEIS/114137.lean
/-!
# Difference between first odd semiprime $> 2^n$ and $2^n$

*References:*
- [A114137](https://oeis.org/A114137)
-/

### conjecture1
/--
In this powers of 2 sequence, does 1 occur infinitely often?
-/
```
theorem conjecture1 :
  answer(sorry) ↔ Set.Infinite {n : ℕ | a n = 1} := by
```

### conjecture2
/--
Does every odd number occur?
-/
```
theorem conjecture2 :
  answer(sorry) ↔ ∀ k : ℕ, Odd k → ∃ n : ℕ, a n = k := by
```

## OEIS/114216.lean
/-!
# Largest odd divisor of $a(n-1) + \textrm{prime}(n)$

$a(0)=0$; thereafter $a(n)$ = largest odd divisor of $a(n-1) + \textrm{prime}(n)$.

*References:*
- [A114216](https://oeis.org/A114216)
-/

### conjecture
/--
Is $a(33900)$ the last term equal to $1$?
-/
```
theorem conjecture :
  answer(sorry) ↔ ∀ n > 33900, a n ≠ 1 := by
```

## OEIS/114362.lean
/-!
# Numerator of $\zeta(4n)/\zeta(2n)^2$ (with $a(0)=2$ instead of $-2$)

The ratio $\zeta(4n)/\zeta(2n)^2$ for $n \ge 1$ is the rational number
$$ Q_n = -2 \frac{B_{4n}}{B_{2n}^2 \binom{4n}{2n}} $$
where $B_k$ is the $k$-th Bernoulli number. The sequence $a(n)$ is the numerator of $Q_n$,
with $a(0)$ defined as $2$.

*References:*
- [A114362](https://oeis.org/A114362)
-/

### conjecture1
/--
Conjecture: if an integer $n > 1$ is odd, then $\zeta(2n)/\zeta(n)^2$ is irrational.
Cf. W. Kohnen (link) and my conjecture in A348829. - Thomas Ordowski, Jan 05 2022
-/
```
theorem conjecture1 (n : ℕ) (hn_gt_one : 1 < n) (hn_odd : Odd n) :
    Irrational ((riemannZeta (2 * n : ℂ) / (riemannZeta (n : ℂ)) ^ 2).re) := by
```

### conjecture2
/--
Conjecture:
$\frac{1 - t(n)}{1 + t(n)} = \frac{1}{2^n} + \frac{1}{3^n} + \frac{1}{5^n} + \frac{1}{7^n} +
  O(\frac{1}{11^n})$,
where $t(n) = \zeta(2n)/\zeta(n)^2$. Cf. A348829. - Thomas Ordowski, Nov 13 2022
-/
```
theorem conjecture2 :
    (fun n : ℕ => (1 - t n) / (1 + t n) -
      (1 / (2:ℝ)^n + 1 / (3:ℝ)^n + 1 / (5:ℝ)^n + 1 / (7:ℝ)^n))
      =O[atTop] (fun n : ℕ => 1 / (11:ℝ)^n) := by
```

## OEIS/1146.lean
/-!
# $a(n) = 2^(2^n)$

*References:*
- [A001146](https://oeis.org/A001146)
-/

### conjecture
/--
I conjecture that { $a(n)$ ; $n>1$ } are the numbers such that $n^4-1$ divides $2^n-1$,
intersection of A247219 and A247165. - M. F. Hasler, Jul 25 2015
This formalizes the reverse direction.
-/
```
theorem conjecture :
  ∀ k : ℕ, ((k^4 - 1) : ℕ) ∣ (2^k - 1 : ℕ) → k > 1 → ∃ n : ℕ, 2 ≤ n ∧ k = a n := by
```

## OEIS/114831.lean
/-!
# Each term is previous term plus floor of harmonic mean of two previous terms.

$a(1) = 1, a(2) = 2$ and
$a(n) = a(n-1) + \lfloor \frac{2 a(n-1) a(n-2)}{a(n-1) + a(n-2)} \rfloor$ for $n \ge 3$.

*References:*
- [A114831](https://oeis.org/A114831)
-/

### conjecture3
/--
Conjecture based on OEIS A114831: What is this sequence, asymptotically?
If the limit exists, the ratio of consecutive terms must tend to $\sqrt{3}$:
$$ \lim_{n \to \infty} \frac{a(n+1)}{a(n)} = \sqrt{3}. $$
That's because $a(n)$ is positive, monotonically increasing ($a(n) > a(n-1)$)
and $a(n+2) \geq a(n+1) + a(n)$.
So $a(n)$ grows exponentially, at least as fast as the Fibonnaci numbers.
Assuming $\frac{a(n+1)}{a(n)}$ tend to a limit L, solving for L in the definition of $a(n)$
gives $L=\sqrt{3}$.
-/
```
theorem conjecture3 :
    Tendsto (fun n ↦ (a (n + 1) : ℝ) / (a n : ℝ)) atTop (nhds (Real.sqrt 3)) := by
```

## OEIS/115257.lean
/-!
# Partial sums of $\binom{2n}{n}^2$

$$a(n) = \sum_{k=0}^n \binom{2k}{k}^2$$

*References:*
- [A115257](https://oeis.org/A115257)
-/

### conjecture
/--
Conjecture: For any positive integer n, the polynomials Sum_{k=0}^n binomial(2k,k)^2*x^k
and Sum_{k=0}^n binomial(2k,k)^2*x^k/(k+1) are irreducible over the field of rational numbers.
- Zhi-Wei Sun, Mar 23 2013
-/
```
theorem conjecture :
  ∀ (n : ℕ), 1 ≤ n → Irreducible (polyP n) ∧ Irreducible (polyQ n) := by
```

## OEIS/115366.lean
/-!
# $a(n)$ = the number of values of $k <= 10^n$ such that $\sqrt{k(k+1)(k+2)(k+3)+1}$ is prime

Since $\sqrt{k(k+1)(k+2)(k+3)+1} = k^2 + 3k + 1$,
$a(n) = \#\{k \in \mathbb{N} \mid 1 \le k \le 10^n \land (k^2 + 3k + 1) \text{ is prime} \}.$

*References:*
- [A115366](https://oeis.org/A115366)
-/

### conjecture
/--
Conjecture: $a(n)/A006880(n) \rightarrow 1.77...$
where A006880(n) is the number of primes $\le 10^n$.
-/
```
theorem conjecture :
    ∃ L : ℝ,
      Tendsto (fun n : ℕ => (a n : ℝ) / (Nat.primeCounting' (10 ^ n) : ℝ)) atTop (nhds L) ∧
      1.77 ≤ L ∧ L ≤ 1.78 := by
```

## OEIS/11545.lean
/-!
# $a(n)$ is the integer whose decimal digits are the first $n+1$ decimal digits of $\pi$

*References:*
- [A011545](https://oeis.org/A011545)
-/

### conjecture1
/--
Wolfgang Haken (1977) conjectured that no term of this sequence is a perfect square,
and estimated the probability that this conjecture is false to be smaller than $10^-9$.
-/
```
theorem conjecture1 : ∀ n, ¬ IsSquare (a n) := by
```

### conjecture2
/--
Number of collisions occurring in a system consisting of an infinitely massive,
rigid wall at the origin, a ball with mass m stationary at position $x_1 > 0$,
and a ball with mass $(10^2n)m$ at position $x_2 > x_1$ and rolling toward the origin,
assuming perfectly elastic collisions and no friction.

Strictly speaking, this property, which is equivalent to the statement that the interval
$(m\pi, \pi/\textrm{arctan}(1/m))$ does not contain an integer for all $m = 10^n$, is not
known to be true for sure. In other words, we do not know for certain that A332045 does not
contain a power of $10$.
-/
```
theorem conjecture2 :
    ∀ n : ℕ, ¬ ∃ (k : ℤ),
      (Real.pi * (10 : ℝ) ^ n.cast < k.cast) ∧
      (k.cast < Real.pi / Real.arctan (1 / (10 : ℝ) ^ n.cast)) := by
```

## OEIS/1157.lean
/-!
# Sum of squares of divisors of $n$

*References:*
- [A001157](https://oeis.org/A001157)
-/

### conjecture
/--
Conjecture: For each k = 2,3,..., all the rational numbers
$\frac{\sigma_k(n)}{n^k} = \sum_{d|n} \frac{1}{d^k}$ (n = 1,2,3,...) have pairwise distinct
fractional parts. - Zhi-Wei Sun, Oct 15 2015
-/
```
theorem conjecture :
  ∀ k : ℕ, 2 ≤ k →
    ∀ n₁ n₂ : ℕ, 0 < n₁ → 0 < n₂ → n₁ ≠ n₂ →
      Int.fract (↑((sigma k) n₁) / (↑n₁ ^ k : ℚ)) ≠
        Int.fract (↑((sigma k) n₂) / (↑n₂ ^ k : ℚ)) := by
```

## OEIS/116150.lean
/-!
# $a(n) = \sum_{j=1}^{n} (3^j + (-2)^j)$

*References:*
- [A116150](https://oeis.org/A116150)
-/

### conjecture
/--
First primes are $a(11) = 264353$ and $a(17) = 193622861$.
Additional primes: $a(71)$, $a(91)$, $a(431)$.
What is the next prime?
-/
```
theorem conjecture : answer(sorry) = a (sInf {n : ℕ | 431 < n ∧ (a n).Prime}) := by
```

## OEIS/117027.lean
/-!
# Determinants of 2 X 2 matrices of non-overlapping blocks of 4 consecutive primes

$a(n) = p_{4n-3}p_{4n} - p_{4n-2}p_{4n-1}$ where $p_k$ is the k-th prime number (1-indexed).

*References:*
- [A117027](https://oeis.org/A117027)
-/

### conjecture
/--
This suggests the ratio is approaching a limit close to 0.87.

Formalized as: The sequence of ratios $P(N)/Neg(N)$ converges to a limit L,
and L is in the interval (0.8, 0.9).
-/
```
theorem conjecture :
  ∃ L : ℝ, Tendsto ratioSeq atTop (nhds L) ∧ 0.8 < L ∧ L < 0.9 :=
by sorry

end OeisA117027
```

## OEIS/167604.lean
/-!
# Chua's Euclidean prime sequence

For a product $n$ of the preceding terms, Chua's sequence chooses the least
prime dividing $d + n / d$ for some divisor $d$ of $n$. The open question is
whether every prime occurs.

*References:*
- [OEIS A167604](https://oeis.org/A167604)
- Andrew R. Booker,
  [A variant of the Euclid--Mullin sequence containing every prime](https://arxiv.org/abs/1605.08929)
-/

### conjecture
/-- Does Chua's sequence contain every prime? -/
```
theorem conjecture :
    answer(sorry) ↔ ∀ p : ℕ, p.Prime → ∃ n ≥ 1, a n = p := by
```

## OEIS/211417.lean
/-!
# Integrality and supercongruences of the factorial ratio $\frac{(6n)! n!}{(3n)! (2n)!^2}$

Integral factorial ratio sequence:
$$a(n) = \frac{(30n)! n!}{(15n)! (10n)! (6n)!}$$

*References:*
- [A211417](https://oeis.org/A211417)
- [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
-/

### general_divisibility
/--
Conjecture: "More generally, for r >= 1, we conjecture that there exists a constant D(r) such that
D(r)*a(n)/Product_{i = 1..r, i coprime to 30} (30*n - i) is integral for all n."
- _Peter Bala_, Aug 28 2025

This generalizes `thirty_mul_sub_one_dvd_a` (the $r = 1$ case where $D(1) = 1$).
-/
```
theorem general_divisibility (r : ℕ) (hr : 1 ≤ r) :
    ∃ D : ℤ, ∀ n : ℕ, (divisorProduct n r) ∣ (D * (a n : ℤ)) := by
```

### supercongruence
/--
Supercongruence: "a(p^k) == a(p^(k-1)) ( mod p^(3*k) ) for any prime p >= 5 and any positive
integer k." - _Peter Bala_, Jan 24 2020

More generally, "the congruences a(n*p^k) == a(n*p^(k-1)) ( mod p^(3*k) ) may hold for any
prime p >= 5 and any positive integers n and k."
-/
```
theorem supercongruence (p k : ℕ) (hp : p.Prime) (hp5 : 5 ≤ p) (hk : 0 < k) :
    (p : ℤ) ^ (3 * k) ∣ ((a (p ^ k) : ℤ) - (a (p ^ (k - 1)) : ℤ)) := by
```

## OEIS/228828.lean
/-!
# Numbers $n$ such that $n^2 + \pi(n)$ is prime

*References:*
- [A228828](https://oeis.org/A228828)
-/

### conjecture
/--
Conjecture: the sequence A228828 is infinite.
-/
```
theorem conjecture : {a n | n}.Infinite := by
```

## OEIS/231201.lean
/-!
# Sum of two numbers with prime conditions

Number of ways to write $n = x+y$, for $x,y > 0$ such that $2^x + y$ is prime.

Zhi-Wei Sun has offered a \$1000 prize for the first proof.

*References:*
- [A231201](https://oeis.org/A231201)
- Zhi-Wei Sun, "Table of n, a(n) for n = 1..10000",
  "Write n = k + m with 2^k + m prime", a message to Number Theory List, Nov. 16, 2013,
  "On a^n+ bn modulo m", arXiv:1312.1166 [math.NT], 2013-2014,
  "Problems on combinatorial properties of primes", arXiv:1402.6641 [math.NT], 2014-2015.
-/

### conjecture
/-- The conjecture for sequence A231201: for any $n > 1$, there exist $x, y > 0$ such that $n = x + y$ and $2^x + y$ is prime. -/
```
theorem conjecture (n : ℕ) (hn : 1 < n) : A n := by
```

## OEIS/232174.lean
/-!
# Representations with prime conditions

Any integer $n > 1$ can be written as $x + y$ with $x, y > 0$ such that both $x + ny$ and
$x^2 + ny^2$ are prime.

Zhi-Wei Sun has offered a \$200 prize for the first proof.

*References:*
- [A232174](https://oeis.org/A232174)
- Z.-W. Sun, "Conjectures on representations involving primes," in: M. Nathanson (ed.),
  Combinatorial and Additive Number Theory II: CANT, Springer Proc. in Math. & Stat.,
  Vol. 220, Springer, 2017, pp. 279-310. https://arxiv.org/abs/1211.1588
- D.A. Cox, "Primes of the Form x² + ny²," John Wiley & Sons, 1989.
-/

### conjecture
/--
**Zhi-Wei Sun's Conjecture (A232174)**: Any integer $n > 1$ can be written as $x + y$ with
$x, y > 0$ such that both $x + ny$ and $x^2 + ny^2$ are prime.
-/
```
theorem conjecture (n : ℕ) (hn : 1 < n) : A n := by
```

## OEIS/237271.lean
/-!
# Number of parts in the symmetric representation of $\sigma(n)$

Number of parts in the symmetric representation of $\sigma(n)$. $a(n)$ is $1$ plus the number of pairs $(d_k, d_{k+1})$ of consecutive divisors of $n$
such that $d_{k+1}$ is odd and $d_{k+1} \ge 2 d_k$.

The formula used is
$1 + |\{(d_k, d_{k+1}) \in \text{consecutive pairs of divisors of } n \mid
d_{k+1} \text{ is odd and } d_{k+1} \ge 2 d_k\}|$,
which is a known characterization of the sequence.

*References:*
- [A237271](https://oeis.org/A237271)
- [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.
-/

### observation_carmichael
/--
Observation: "a(A002997(n)) >= 3, at least for 1 <= n <= 10000."
- _Omar E. Pol_, Oct 21 2025

That is, $a(k) \ge 3$ for every Carmichael number $k$.
A002997 is the sequence of Carmichael numbers: the composite numbers $k$ such that
$b^{k-1} \equiv 1 \pmod k$ for every $b$ coprime to $k$. This is `IsCarmichael`,
which also forces $k$ to be composite.
-/
```
theorem observation_carmichael (k : ℕ) (hk : IsCarmichael k) :
    3 ≤ a k := by
```

## OEIS/239957.lean
/-!
# Primitive roots of the form k² + 1

Every prime $p$ has a primitive root $0 < g < p$ of the form $k^2 + 1$, where $k$ is an integer.

Zhi-Wei Sun has offered a prize of RMB 2,000 for the first proof.

*References:*
- [A239957](https://oeis.org/A239957)
- Z.-W. Sun, "New observations on primitive roots modulo primes," arXiv:1405.0290 [math.NT], 2014.
-/

### conjecture
/--
**Zhi-Wei Sun's Conjecture (A239957)**: Every prime $p$ has a primitive root $0 < g < p$ of the
form $k^2 + 1$, where $k$ is an integer.
-/
```
theorem conjecture (p : ℕ) (hp : p.Prime) : A p := by
```

## OEIS/280831.lean
/-!
# The 1680-Conjecture

Any nonnegative integer can be written as $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative
integers such that $x^4 + 1680 y^3 z$ is a square.

Zhi-Wei Sun has offered a prize of 1,680 RMB for the first proof.

*References:*
- [A280831](https://oeis.org/A280831)
- Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
- Z.-W. Sun, "Refining Lagrange's four-square theorem," arXiv:1604.06723 [math.NT], 2016.
-/

### conjecture
/--
**Zhi-Wei Sun's 1680-Conjecture (A280831)**: Any nonnegative integer can be written as
$x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative integers such that $x^4 + 1680 y^3 z$ is a square.
-/
```
theorem conjecture (n : ℕ) : A n := by
```

## OEIS/281976.lean
/-!
# Sum of four squares with square conditions

Any integer $n \geq 0$ can be written as $x^2 + y^2 + z^2 + w^2$ with $x, y, z, w$ nonnegative
integers and $z \leq w$, such that both $x$ and $x + 24y$ are squares.

Zhi-Wei Sun has offered a \$2,400 prize for the first proof.

*References:*
- [A281976](https://oeis.org/A281976)
- Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
  https://doi.org/10.1016/j.jnt.2016.11.008
- Z.-W. Sun, "Restricted sums of four squares," *arXiv:1701.05868* [math.NT], 2017.
  https://arxiv.org/abs/1701.05868
-/

### conjecture
/--
**Zhi-Wei Sun's Conjecture (A281976)**: Any integer $n \geq 0$ can be written as $x^2 + y^2 + z^2 + w^2$
with $x, y, z, w$ nonnegative integers and $z \leq w$, such that both $x$ and $x + 24y$ are squares.
-/
```
theorem conjecture (n : ℕ) : A n := by
```

## OEIS/287616.lean
/-!
# Sum of a triangular number, a generalized pentagonal number, and a generalized heptagonal number

Any nonnegative integer can be written as $x(x+1)/2 + y(3y+1)/2 + z(5z+1)/2$ with $x, y, z$
nonnegative integers.

Zhi-Wei Sun has offered a USD 135 prize for the first proof of this conjecture.

*References:*
- [A287616](https://oeis.org/A287616)
- Zhi-Wei Sun, "Universal sums of three quadratic polynomials", arXiv:1502.03056 [math.NT]
-/

### conjecture
/--
**Zhi-Wei Sun's Conjecture (A287616)**: Any nonnegative integer can be written as the sum of
a triangular number $x(x+1)/2$, a generalized pentagonal number $y(3y+1)/2$, and a generalized
heptagonal number $z(5z+1)/2$, where $x, y, z$ are nonnegative integers.
-/
```
theorem conjecture (n : ℕ) : A n := by
```

## OEIS/303656.lean
/-!
# Sum of two squares, a power of 3, and a power of 5

Any integer $n > 1$ can be written as $a^2 + b^2 + 3^c + 5^d$ where $a, b, c, d$ are
nonnegative integers.

Zhi-Wei Sun has offered a \$3,500 prize for the first proof.

*References:*
- [A303656](https://oeis.org/A303656)
- Z.-W. Sun, "Restricted sums of four squares," arXiv preprint:
  https://arxiv.org/abs/1701.05868v10
- Z.-W. Sun, "Refining Lagrange's four-square theorem," Journal of Number Theory:
  http://maths.nju.edu.cn/~zwsun/RefineFourSquareTh.pdf
- Z.-W. Sun, "Restricted sums of three or four squares":
  http://maths.nju.edu.cn/~zwsun/Square-sum.pdf
- Zhi-Wei Sun's 1-3-5 conjecture and variations:
  https://www.aimspress.com/aimspress-data/era/2020/2/PDF/1935-9179_2020_2_589.pdf
-/

### conjecture
/--
**Zhi-Wei Sun's Conjecture (A303656)**: Any integer $n > 1$ can be written as the sum of two
squares, a power of 3, and a power of 5.
-/
```
theorem conjecture (n : ℕ) (hn : 1 < n) : A n := by
```

## OEIS/306477.lean
/-!
# The 2-4-6-8 Conjecture

Any integer $n > 0$ can be written as $\binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8}$
with $w, x, y, z$ nonnegative integers.

Zhi-Wei Sun has offered a $2,468 prize for the first proof (or $2,468 RMB for a counterexample).

The conjecture has been verified for all $n$ up to $1.2 \times 10^{12}$ by Yaakov Baruch (March 2019).

*References:*
- [A306477](https://oeis.org/A306477)
- [mathoverflow/323541](https://mathoverflow.net/questions/323541): Z.-W. Sun, "Positive integers written as C(w,2) + C(x,4) + C(y,6) + C(z,8) with w,x,y,z in {2,3,...},", Feb. 19, 2019.
-/

### conjecture
/--
**Zhi-Wei Sun's 2-4-6-8 Conjecture (A306477)**: Any integer $n > 0$ can be written as
$\binom{w+2}{2} + \binom{x+3}{4} + \binom{y+5}{6} + \binom{z+7}{8}$ for nonnegative integers $w, x, y, z$.
-/
```
theorem conjecture (n : ℕ) (hn : 0 < n) : A n := by
```

## OEIS/308734.lean
/-!
# Four-square conjecture with powers of 2, 3, and 5

Any integer $n > 1$ can be written as $(2^a \cdot 3^b)^2 + (2^c \cdot 5^d)^2 + x^2 + y^2$
where $a, b, c, d, x, y$ are nonnegative integers.

Zhi-Wei Sun has offered a \$2,500 prize for the first proof.

*References:*
- [A308734](https://oeis.org/A308734)
- Z.-W. Sun, "Refining Lagrange's four-square theorem," *J. Number Theory* **175** (2017), 167-190.
  https://doi.org/10.1016/j.jnt.2016.11.008
- Z.-W. Sun, "Restricted sums of four squares," *Int. J. Number Theory* **15** (2019), 1863-1893.
- Z.-W. Sun, "Various Refinements of Lagrange's Four-Square Theorem," Westlake Number Theory
  Symposium, Nanjing University, China, 2020.
- S. Banerjee, "On a conjecture of Sun about sums of restricted squares," *J. Number Theory*
  **256** (2024), 253-289.
-/

### conjecture
/--
**Zhi-Wei Sun's Four-Square Conjecture (A308734)**: Any integer $n > 1$ can be written as
$(2^a \cdot 3^b)^2 + (2^c \cdot 5^d)^2 + x^2 + y^2$ for nonnegative integers $a, b, c, d, x, y$.
-/
```
theorem conjecture (n : ℕ) (hn : 1 < n) : A n := by
```

## OEIS/34693.lean
/-!
# Smallest number $k$ such that $kn + 1$ is prime

*References:*
- [A34693](https://oeis.org/A34693)
-/

### exists_k
/-- Conjecture: for every $n > 1$ there exists a number $k < n$ such that $nk + 1$ is a prime. -/
```
theorem exists_k {n : ℕ} (hn : 1 < n) : ∃ k < n, (n * k + 1).Prime := by
```

### exists_k_stronger
/-- A stronger conjecture: for every n there exists a number $k < 1 + n^{0.75}$ such that
$nk + 1$ is a prime. -/
```
theorem exists_k_stronger {n : ℕ} (hn : 0 < n) : ∃ k : ℕ,
    k < 1 + (Real.nthRoot 4 n) ^ 3 ∧ (n * k + 1).Prime := by
```

### a_isBigO
/-- Conjecture: $a(n) = O(\log(n)\log(\log(n)))$. -/
```
theorem a_isBigO : (fun n ↦ (a n : ℝ)) =O[atTop] (fun n ↦ Real.log n * Real.log (Real.log n)) := by
```

### a_unbounded
/-- Counter-conjecture to `a_isBigO`: $a(n) / (\log n \log \log n)$ is unbounded. -/
```
theorem a_unbounded : ¬BddAbove (Set.range fun n ↦ a n / (Real.log n * Real.log (Real.log n))) := by
```

## OEIS/357513.lean
/-!
# Numerator of a sum involving binomial coefficients

$a(n)$ is the numerator of
$\sum_{k = 1}^n \frac{1}{k^3} \binom{n}{k}^2 \binom{n+k}{k}^2$ for $n \ge 1$
with $a(0) = 0$.

*References:*
- [A357513](https://oeis.org/A357513)
-/

### general_supercongruence
/--
We conjecture that $u(p-1) == 0 (mod p^4)$ for all primes $p$,
with a finite number of exceptions that depend on $m$.
-/
```
theorem general_supercongruence (m : ℕ) : ∃ (exceptions : Finset ℕ), ∀ p, p.Prime →
    p ∉ exceptions → u m (p - 1) = (0 : ZMod (p ^ 4)) := by
```

## OEIS/37274.lean
/-!
# Home primes (OEIS A037274)

Starting from an integer $n\geq 2$, list its prime factors in nondecreasing order with
multiplicity, concatenate their decimal representations, and repeat. The home-prime conjecture
says that this process always reaches a prime.

For example,

$$25 \longmapsto 55 \longmapsto 511 \longmapsto 773.$$

*References:*
* [OEIS A037274](https://oeis.org/A037274)
* M. Herman and J. Schiffman, *Investigating home primes and their families*,
  Mathematics Teacher 107 (2014), 606–614
-/

### home_prime_conjecture
/-- Every integer at least two reaches a home prime. -/
```
theorem home_prime_conjecture : ∀ n : ℕ, 2 ≤ n → ReachesPrime n := by
```

## OEIS/41.lean
/-!
# No powers as partition numbers

There are no partition numbers $a(k)$ of the form $x^m$, with $x,m$ integers $>1$.

*Reference:* [A41](https://oeis.org/A41)
-/

### noPowerPartitionNumber
/--
There are no partition numbers $a(k)$ of the form $x^m$, with $x,m$ integers $>1$.
See comment by Zhi-Wei Sun (Dec 02 2013).
-/
```
theorem noPowerPartitionNumber : answer(sorry) ↔ ∀ k, ¬IsPerfectPower (a k) := by
```

## OEIS/56777.lean
/-!
# Divisibility of $2^n + 1$ by $n$

A56777 lists composite numbers $n$ satisfying both $\varphi(n+12) = \varphi(n) + 12$ and
$\sigma(n+12) = \sigma(n) + 12$.

The conjectures state identities connecting A56777 and prime quadruples (A7530), as
well as congruences satisfied by the members of A56777.

*References:*
- [A56777](https://oeis.org/A56777)
-/

### comesFromPrimeQuadruple_of_a
/-- All members of the sequence A56777 come from prime quadruples. -/
```
theorem comesFromPrimeQuadruple_of_a {n : ℕ} (h : A n) : ComesFromPrimeQuadruple n := by
```

## OEIS/63880.lean
/-!
# Conjectures associated with A063880

A063880 lists numbers $n$ such that $\sigma(n) = 2 \cdot \text{usigma}(n)$, where $\sigma(n)$ is the
sum of all divisors and $\text{usigma}(n)$ is the sum of unitary divisors.

Equivalently, these are numbers whose unitary and non-unitary divisors have equal sum.

The conjectures state that all members satisfy $n \equiv 108 \pmod{216}$, and that all
primitive terms (those whose proper divisors aren't in the sequence) are powerful numbers,
with $108$ being the only primitive term.

*References:*
- [A063880](https://oeis.org/A063880)
-/

### mod_216_of_a
/-- All members of the sequence satisfy $n \equiv 108 \pmod{216}$. -/
```
theorem mod_216_of_a {n : ℕ} (h : A n) : n % 216 = 108 := by
```

### unique_primitive_108
/-- $108$ is the only primitive term. -/
```
theorem unique_primitive_108 {n : ℕ} (h : IsPrimitiveTerm n) : n = 108 := by
```

## OEIS/67720.lean
/-!
# Conjectures associated with A067720

A067720 lists numbers $k$ such that $\varphi(k^2 + 1) = k \cdot \varphi(k + 1)$,
where $\varphi$ is Euler's totient function.

The sequence exhibits a strong connection to primes: for almost all terms $k$,
$k + 1$ is prime. The conjecture states that $k = 8$ is the only exception.

*References:*
- [A067720](https://oeis.org/A067720)
-/

### prime_add_one_of_a
/-- For members of the sequence other than $8$, we have $k + 1$ is prime. -/
```
theorem prime_add_one_of_a {k : ℕ} (h : A k) (hne : k ≠ 8) : (k + 1).Prime := by
```

## OEIS/81091.lean
/-!
# Primes of the form 2^n + 2^i + 1

There are infinite primes of the form $2^n + 2^i + 1$, with $0 < i < n$.
See Wagstaff (2001) where this conjecture is posed.

*References:*
- [A81091](https://oeis.org/A81091)
- Samuel S. Wagstaff, Jr., [Prime Numbers with a fixed number of one bits or zero bits in their binary representation](http://projecteuclid.org/euclid.em/999188636), Exp. Math. vol. 10, issue 2 (2001) 267.
-/

### conjectureA81091
/--
**Conjecture (A81091)**: There are infinite primes of the form $2^n + 2^i + 1$,
with $0 < i < n$.
-/
```
theorem conjectureA81091 :
    answer(sorry) ↔ Set.Infinite {p : ℕ | A p} := by
```

## OEIS/945.lean
/-!
# Euclid-Mullin sequence

The Euclid-Mullin sequence starts with $a(1) = 2$. Each subsequent term is the smallest prime
factor of one plus the product of all preceding terms. We extend the sequence by $a(0) = 1$ and
write $b(n)$ for the product of the first $n$ official terms.


*References:*
- [A000945](https://oeis.org/A000945)
- [Mullin63] A. A. Mullin,
  ["Research Problem 8 (ii)"](https://doi.org/10.1090/S0002-9904-1963-11017-4),
  *Bull. Amer. Math. Soc.* **69** (1963), p. 737.
- [Wagstaff93] S. S. Wagstaff, Jr.,
  ["Computing Euclid's primes"](https://oeis.org/A000945/a000945_4.pdf),
  *Bull. Institute Combin. Applications* **8** (1993), pp. 23-32.
- [CrandallPomerance01] R. Crandall and C. Pomerance,
  *Prime Numbers: A Computational Perspective*, Springer (2001), p. 6.
- A. R. Booker, "A variant of the Euclid-Mullin sequence containing every prime,"
  [arXiv:1605.08929](https://arxiv.org/abs/1605.08929), *Journal of Integer Sequences* **19**
  (2016), Article 16.6.4.
-/

### every_prime_occurs
/--
"Does the sequence ... contain every prime? ... [It] was considered by Guy and Nowakowski
and later by Shanks, [Wagstaff93] computed the sequence through the 43rd term. The
computational problem inherent in continuing the sequence further is the enormous size of the
numbers that must be factored. Already the number $a(1) \cdots a(43) + 1$ has 180 digits."
- [CrandallPomerance01]

See also [Mullin63].
-/
```
theorem every_prime_occurs :
    answer(sorry) ↔ ∀ p, p.Prime → ∃ n ≥ 1, a n = p := by
```

## Paper/CardinalityLindelof.lean
/-!
# Conjecture about cardinality of Lindelöf spaces

The conjecture asks for a Lindelöf space where all singletons are G_δ sets
and which has cardinality > 𝔠.

This is Problem 1 in https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf

*Reference:*
* [Selected Old Open Problems in General Topology](https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf)
  by A. V. Arhangel’skii

-/

### HasGδSingletons
/--
Is there a Lindelöf space with singletons as Gδ sets with cardinality greater than the continuum?
-/
```
theorem HasGδSingletons.lindelof_card :
    ∃ (X : Type) (_ : TopologicalSpace X), HasGδSingletons X ∧ LindelofSpace X ∧ 𝔠 < #X := by
```

## Paper/CasasAlvero.lean
/-!
# Casas-Alvero Conjecture

*References:*
* [The Casas-Alvero conjecture for infinitely many degrees](https://arxiv.org/pdf/math/0605090)
* [MathOverflow](https://mathoverflow.net/questions/27851)

The Casas-Alvero conjecture states that if a univariate polynomial `P` of degree `d` over a field
of characteristic zero shares a non-trivial factor with its Hasse derivatives up to order `d-1`,
then `P` must be of the form `(X - α)ᵈ` for some `α` in the field.

The conjecture has been proven for:
* Degrees `d ≤ 8`
* Degrees of the form `p^k` where `p` is prime
* Degrees of the form `2p^k` where `p` is prime

The conjecture is false in positive characteristic `p` for polynomials of degree `p+1`.

The conjecture is now claimed to be proven in this paper:
* [Proof of the Casas-Alvero conjecture: Soham Ghosh)](https://arxiv.org/pdf/2501.09272)

-/

### casas_alvero_conjecture
/--
The Casas-Alvero conjecture states that in characteristic zero, if a monic polynomial `P`
has the Casas-Alvero property, then `P = (X - α)ᵈ` for some `α`.
-/
```
theorem casas_alvero_conjecture (hP' : HasCasasAlveroProp P) :
    ∃ α : K, P = (X - C α) ^ P.natDegree := by
```

## Paper/CatchUpConjecture.lean
/-!
# The Catch-Up game and conjecture

The game **Catch-Up** (Isaksen–Ismail–Brams–Nealen, 2015) is a two-player, perfect-information game
played on a finite nonempty set `S` of positive integers. Each time a player removes a number from
`S`, that number is added to the player’s score.

**Rules.**
* The scores start at `0`. Player `p1` starts by removing **exactly one** number from `S`.
* After the first move, players alternate turns. On a turn, the current player removes **one or more**
  numbers from `S`, one at a time, and must keep removing numbers until their score becomes
  **at least** the opponent’s score; before the final pick they must remain **strictly behind**.
* If the current player cannot catch up (in particular, even taking all remaining numbers would still
  leave them behind), the game ends immediately: the current player receives all remaining numbers.

When `S` is empty, the player with higher score wins; equal scores give a draw.

In this file we define:
* `Player` and `Outcome`,
* the recursive evaluator `value` (optimal play),
* the conjecture `value_of_even_mul_succ_self_div_two`.

## Example
For `S = {1,2,3,4}` one play is: `p1` takes `2`, `p2` takes `1` then `4`, and `p1` takes `3`,
ending with scores `(5,5)`.

## References
A. Isaksen, M. Ismail, S. J. Brams, A. Nealen,
*Catch-Up: A Game in Which the Lead Alternates,* Game & Puzzle Design 1(2), 38–49 (2015).

-/

### value_of_even_mul_succ_self_div_two
/--
Let $T_N = \sum_{k=1}^{N} k = \frac{N(N+1)}{2}$.
If $T_N$ is even (equivalently $N \equiv 0 \pmod 4$ or $N \equiv 3 \pmod 4$),
then under optimal play the game `Catch-Up($\{1, \ldots, N\}$)` ends in a draw.
-/
```
theorem value_of_even_mul_succ_self_div_two
    (N : ℕ) (h_even : Even (N * (N + 1) / 2)) :
    value (.Icc 1 N) = .draw := by
```

## Paper/Chvatal.lean
/-!
# Chvátal's Conjecture

*References:*

* [A Conjecture in Extremal Combinatorics](https://users.encs.concordia.ca/~chvatal/conjecture.html)
* [Chvátal's Conjecture and Correlation Inequalities](https://arxiv.org/abs/1608.08954)
-/

### exists_maximal_star
/--
If F is a decreasing family of sets of some finite type α, then there is some element
x of α such that the family consisting of all members of F containing x is an intersecting
subfamily of F with maximal cardinality.
-/
```
theorem exists_maximal_star :
    ∀ F : Finset (Finset α), Decreasing F →
        ∃ x : α, ∀ G, G ⊆ F → Intersecting G → G.card ≤ { A ∈ F | x ∈ A }.card := by
```

## Paper/ConjugacyClassSizes.lean
/-!
# The $S_3$-conjecture (conjugacy classes of distinct sizes)

*References:*
* W. Zhou, I. Gorshkov, *On $\{2,3,5\}$-groups with conjugacy classes of distinct sizes*,
  [arXiv:2606.22244](https://arxiv.org/abs/2606.22244) (2026).
* F. M. Markel, *Groups with many conjugate elements*, J. Algebra **26** (1973), 69–74.
  (Origin of the $S_3$-conjecture.)
* R. Knörr, W. Lempken, B. Thielcke, *The $S_3$-conjecture for solvable groups*,
  Israel J. Math. **91** (1995), 61–76.
* J. Zhang, *Finite groups with many conjugate elements*, J. Algebra **170** (1994), 608–624.
* Z. Arad, M. Muzychuk, A. Oliver, *On groups with conjugacy classes of distinct sizes*,
  J. Algebra **280** (2004), 537–576.
* [Conjugacy class](https://en.wikipedia.org/wiki/Conjugacy_class)

A finite group in which distinct conjugacy classes have distinct cardinalities is called an
*anti-homogeneous* group (or *ah-group*). The symmetric group $S_3$ is an ah-group: its three
conjugacy classes have sizes $1$, $2$, and $3$. Markel's **$S_3$-conjecture** (1973) asserts that,
up to isomorphism, $S_3$ is the only nontrivial finite ah-group. The conjecture has been proved
for all solvable groups (independently by Zhang and by Knörr–Lempken–Thielcke), but the general
non-solvable case remains open.
-/

### conjClassSizes_iff_sym_three
/--
**Markel's $S_3$-conjecture** (1973): any nontrivial finite ah-group is isomorphic to $S_3$.

The conjecture is open in general; it is known to be true for solvable groups.
-/
```
theorem conjClassSizes_iff_sym_three
    (G : Type) [Group G] [Fintype G] [Nontrivial G]
    (h : HasDistinctConjClassSizes (G := G)) :
    Nonempty (G ≃* Equiv.Perm (Fin 3)) := by
```

## Paper/DeGiorgi.lean
/-!
# De Giorgi's conjecture

This file states a conjecture of De Giorgi about entire solutions to $Δ u + u - u^3 = 0$.
The conjecture is a rigidity theorem: in spatial dimension $n ≤ 8$, the level sets of bounded solutions
which satisfy $∂₁u > 0$ everywhere are hyperplanes. It has been shown that the condition $n ≤ 8$ is sharp.

The main theorems are:
- `DeGiorgi_le_eight`: the conjecture holds in dimension $n ≤ 8$.
- `DeGiorgi_ge_nine`: the conclusion of the conjecture does not hold if $n ≥ 9$.

The cases $1 ≤ n ≤ 8$ are also listed individually to enable partial solutions.
The cases $1 ≤ n ≤ 3$ are solved, while $4 ≤ n ≤ 8$ remains open.

## Existing results
- The case $n = 1$ trivially holds ($u$ is injective since $∂_1 u > 0$).
- The case $n = 2$ was proven by Ghoussoub and Gui.
- The case $n = 3$ was proven by Ambrosio and Cabré.
- The case $4 ≤ n ≤ 8$ was proven under an extra assumption by Savin.
- The counterexample for $n ≥ 9$ was proven by Del Pino, Kowalczyk, and Wei.

## References
* [Ghoussoub, Gui](https://doi.org/10.1007/s002080050196),
  Mathematische Annalen 311 (1998) proves the conjecture for $n = 2$.
* [Ambrosio, Cabré](https://doi.org/10.1090/S0894-0347-00-00345-3),
  Journal of the American Mathematical Society 13 (2000) proves the conjecture for $n = 3$.
* [Savin](https://doi.org/10.4007/annals.2009.169.41),
  Annals of Mathematics 169 (2009) proves the case $4 ≤ n ≤ 8$ under an additional assumption.
* [Del Pino, Kowalczyk, Wei](http://dx.doi.org/10.4007/annals.2011.174.3.3),
  Annals of Mathematics 174 (2011) shows that the condition $n ≤ 8$ is sharp.
-/

### DeGiorgi_le_eight
/--
De Giorgi's conjecture holds in dimension $n ≤ 8$.
-/
```
theorem DeGiorgi_le_eight (hn : n ≤ 8) : (DeGiorgi_conclusion n) := by
```

### DeGiorgi_four
/--
De Giorgi's conjecture holds in dimension $n = 4$.
-/
```
theorem DeGiorgi_four : (DeGiorgi_conclusion 4) := by
```

### DeGiorgi_five
/--
De Giorgi's conjecture holds in dimension $n = 5$.
-/
```
theorem DeGiorgi_five : (DeGiorgi_conclusion 5) := by
```

### DeGiorgi_six
/--
De Giorgi's conjecture holds in dimension $n = 6$.
-/
```
theorem DeGiorgi_six : (DeGiorgi_conclusion 6) := by
```

### DeGiorgi_seven
/--
De Giorgi's conjecture holds in dimension $n = 7$.
-/
```
theorem DeGiorgi_seven : (DeGiorgi_conclusion 7) := by
```

### DeGiorgi_eight
/--
De Giorgi's conjecture holds in dimension $n = 8$.
-/
```
theorem DeGiorgi_eight : (DeGiorgi_conclusion 8) := by
```

## Paper/Dubner.lean
/-!
# Dubner's conjecture

*Reference*: [Every even number greater than 4208 is the sum of two t-primes](https://scispace.com/pdf/twin-prime-conjectures-3icaxy6b0m.pdf)
by *Harvey Dubner*.
-/

### dubner_conjecture
/--
Every even number greater than 4208 is the sum of two twin primes.
-/
```
theorem dubner_conjecture (n : ℕ) (hn : 4208 < n) (h : Even n) :
    ∃ p q : ℕ,
      IsTwinPrime p ∧
      IsTwinPrime q ∧
      p + q = n := by
```

## Paper/FusibleNumber.lean
/-!
# Main conjecture on fusible numbers

*References:*
- [Fusible numbers and Peano Arithmetic](https://arxiv.org/abs/2003.14342),
  by Jeff Erickson, Gabriel Nivasch, and Junyan Xu.
- [Fusible numbers and Peano Arithmetic](https://doi.org/10.46298/lmcs-18%283%3A6%292022),
  Logical Methods in Computer Science, Volume 18, Issue 3 (July 28, 2022).
-/

### conj_7_1
/-- If `x` is a fusible number and `y` is its successor, then the interval `[x + 1, y + 1)` can be
divided into intervals `[ℓₙ, ℓₙ₊₁)`, such that the fusible numbers in `[ℓₙ, ℓₙ₊₁)` are obtained by
fusing the `n + 1`st successor of `x` with a fusible number.
This formalization differs from Conjecture 7.1 in the paper in four ways:
(1) it is obtained from Conjecture 7.1 by plugging in `n + 1` into `n`, which simplifies the expressions
  and removes the need to assume `n ≥ 1`;
(2) the `n + 1`st successor `s^(n+1)(x)` is replaced by the explicit value `x + (2 - 1 / 2 ^ n) * m`;
(3) instead of defining `y` to be the successor of `x`, we assert that there is no fusible number
  strictly between `x` and `y`;
(4) instead of using `∃ z, IsFusible z ∧ q = s^(n+1)(x) ~ z` we use the value of `z` determined by the equality,
  namely `z = 2 * q - 1 - s^(n+1)(x)`, and it is easy to see `z ∈ [x + 1 - m / 2 ^ n, x + 1)` as required. -/
```
theorem conj_7_1 (x y q : ℚ) (n : ℕ) (fus_x : IsFusible x) (fus_y : IsFusible y) (lt : x < y)
    (nmem_Ioo : ∀ z, IsFusible z → z ∉ Set.Ioo x y) :
    let m := y - x
    let ℓ (n : ℕ) := y + 1 - m / 2 ^ n
    IsFusible q → q ∈ Set.Ico (ℓ n) (ℓ (n + 1)) → IsFusible (2 * q - 1 - x - (2 - 1 / 2 ^ n) * m) := by
```

## Paper/HartshorneConjecture.lean
/-! # Hartshorne's conjecture on Vector Bundles

*References:*
* [Har1974] R. Hartshorne, [Varieties of small codimension in projective space](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-80/issue-6/Varieties-of-small-codimension-in-projective-space/bams/1183535999.full).
* [MO2010] [Evidences on Hartshorne's conjecture? References?](https://mathoverflow.net/questions/13990/evidences-on-hartshornes-conjecture-references)
-/

### harthshorne_conjecture
/--
There are no indecomposable vector bundles of rank 2 on $\mathbb{P}^n$ for $n \ge 7$.
This is Conjecture 6.3 in [Har1974].
-/
```
theorem harthshorne_conjecture (n : ℕ) (hn : 7 ≤ n)
    (𝓕 : VectorBundles ℙ(Fin (n + 1); Spec (.of ℂ)))
    (h𝓕 : 𝓕.rank = 2) :
    Nonempty (𝓕.Splitting (Fin 2)) := by
```

## Paper/Homogenous.lean
/-!
# Conjectures around homogeneous topological spaces

This file formalizes the notion of a weakly first countable topological space and some conjectures
around those.

*References:*
* [Ar2013] Arhangeliski, Alexandr. "Selected old open problems in general topology."
  Buletinul Academiei de Ştiinţe a Republicii Moldova. Matematica 73.2-3 (2013): 37-46.
  https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf
-/

### homogeneousSpace_exists_inj_tendsto
/-- Problem 13 in [Ar2013]:
Is it true that every infinite homogeneous compact hausdorff
space contains a non-trivial convergent sequence? -/
```
theorem homogeneousSpace_exists_inj_tendsto :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), ¬ Finite X → T2Space X → CompactSpace X →
      HomogeneousSpace X → ∃ s : ℕ → X, s.Injective ∧ ∃ a : X, Tendsto s atTop (nhds a) := by
```

### homogeneousSpace_exists_surjective
/-- Problem 14 in [Ar2013]:
Is it possible to represent an arbitrary compact hausdorff space as an image
of a homogeneous compact space under a continuous mapping? -/
```
theorem homogeneousSpace_exists_surjective :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      ∃ (Y : Type) (_ : TopologicalSpace Y), T2Space Y ∧ CompactSpace Y ∧ HomogeneousSpace Y ∧
        ∃ f : Y → X, Continuous f ∧ f.Surjective := by
```

### firstCountableTopology_of_countablyMonolithicSpace
/-- Problem 15 in [Ar2013]:
Is every homogeneous ω-monolithic compact hausdorff space first countable? -/
```
theorem firstCountableTopology_of_countablyMonolithicSpace :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      HomogeneousSpace X → CountablyMonolithicSpace X → FirstCountableTopology X := by
```

### countablyMonolithicSpace_card_lt
/-- Problem 16 in [Ar2013]:
Is the cardinality of every homogeneous ω-monolithic compact hausdorff space not greater than 𝔠? -/
```
theorem countablyMonolithicSpace_card_lt :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      HomogeneousSpace X → CountablyMonolithicSpace X → #X ≤ 𝔠 := by
```

### countablyMonolithicSpace_exists_nhds_generated_countable
/-- Problem 17 in [Ar2013]:
Is it true that every nonempty ω-monolithic compact hausdorff space contains a point with a
first countable neighborhood basis?

Note: `Nonempty X` is required since the conclusion asserts the existence of a point.
-/
```
theorem countablyMonolithicSpace_exists_nhds_generated_countable :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T2Space X → CompactSpace X →
      Nonempty X → CountablyMonolithicSpace X → ∃ x : X, (𝓝 x).IsCountablyGenerated := by
```

## Paper/KotzigConjecture.lean
/-!
# Kotzig's Conjecture

*Reference:* A. Kotzig, cited in A. Rosa, *On certain valuations of the vertices of a graph*,
Theory of Graphs (Internat. Sympos., Rome, 1966), Gordon and Breach, 1967, pp. 349–355.

Kotzig conjectured that for every $n$, the complete graph $K_{2n+1}$ decomposes into copies of
any $n$-edge tree via cyclic shifts of a single embedding. This is strictly stronger than
Ringel's conjecture; see `Paper/RingelConjecture.lean`. The large-$n$ case is proved by
Montgomery–Pokrovskiy–Sudakov; see `Arxiv/2001.02665/RingelConjecture.lean`.
-/

### kotzig_conjecture
/--
For any tree $T$ with $n$ edges, the complete graph $K_{2n+1}$ decomposes into
$2n+1$ edge-disjoint copies of $T$ via cyclic shifts of a single embedding.

The $2n+1$ copies are $f_0, f_1, \dots, f_{2n}$ where $f_i(v) = f_0(v) + i$ for all vertices
$v$ — each copy is obtained by adding $i \pmod{2n+1}$ to every vertex of the base copy.
This is strictly stronger than `RingelConjecture.ringel_conjecture`.
-/
```
theorem kotzig_conjecture {V : Type} [Finite V]
    (T : SimpleGraph V) (hT : T.IsTree)
    (n : ℕ) (hn : T.edgeSet.ncard = n) :
    ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
      (∀ i v, f i v = f 0 v + i) ∧
      Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
      ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1))) := by
```

## Paper/Kurepa.lean
/-!
# Kurepa's conjecture

*Reference:* [On the left factorial function !N](https://oeis.org/A3422), by *Đuro Kurepa* Math. Balkanica 1, p. 147-153, 1971

-/

### kurepa_conjecture
/--
## Kurepa's conjecture

For all $n$, $$!n\not\equiv 0 \mod n$$

This appears as B44 "Sums of factorials."
in [Unsolved Problems in Number Theory](https://doi.org/10.1007/978-0-387-26677-0)
by *Richard K. Guy*
-/
```
theorem kurepa_conjecture (n : ℕ) (h_n : 2 < n) : (!n : ℕ) % n ≠ 0 := by
```

### kurepa_conjecture
/--
This statement can be reduced to the prime case only.
-/
```
theorem kurepa_conjecture.variants.prime (p : ℕ) (h_p : 2 < p) :
    p.Prime → (!p : ℕ) % p ≠ 0 := by
```

### kurepa_conjecture
/--
An equivalent formulation in terms of the gcd of $n!$ and $!n$.
-/
```
theorem kurepa_conjecture.variants.gcd (n : ℕ) : 2 < n → (n !).gcd (! n) = 2 := by
```

## Paper/LatinSquare.lean
/-!
# Conjectures about Latin Squares

This file formalizes some conjectures and theorems around latin squares.

*References:*
* [Wa2011] Wanless, Ian. "Transversals in Latin Squares: A Survey."
  Surveys in Combinatorics 2011, R. Chapman, Ed. Cambridge University Press, 2011, pp. 403–437.
  https://users.monash.edu.au/~iwanless/papers/transurveyBCC.pdf
* https://en.wikipedia.org/wiki/Problems_in_Latin_squares
-/

### oddOrderLatinSquareTransversal
/--
Conjecture 3.2 in [Wa2011]:
Each Latin square of odd order has at least one transversal.
-/
```
theorem oddOrderLatinSquareTransversal : answer(sorry) ↔
    Odd n → ∀ (L : LatinSquare n), ∃ σ, IsTransversal L σ := by
```

### latinSquareOrder11Transversal
/--
The smallest odd number for which this conjecture is not known is 11.
-/
```
theorem latinSquareOrder11Transversal : answer(sorry) ↔
    ∀ (L : LatinSquare 11), ∃ σ, IsTransversal L σ := by
```

### latinSquareNearTransversal
/--
Conjecture 5.1 in [Wa2011]:
Every latin square has a near-transversal
-/
```
theorem latinSquareNearTransversal : answer(sorry) ↔
    ∀ (L : LatinSquare n), ∃ ρ σ, IsNearTransversal L ρ σ := by
```

### numTransversalsZn
/--
Conjecture 6.7 in [Wa2011]:
There exist real constants $0 < c_1 < c_2 < 1$ such that
$$
c_1^n n! \leq z_n \leq c_2^n n!
$$
for all odd $n \geq 3$.
-/
```
theorem numTransversalsZn : answer(sorry) ↔
      ∃ᵉ (c₁ > (0 : ℝ)) (c₂ < (1 : ℝ)) (_ : c₁ < c₂),
      ∀ n ≥ 3, Odd n →
        (z n : ℝ) ∈ Set.Icc (c₁ ^ n * n.factorial) (c₂ ^ n * n.factorial) := by
```

### growthRateZn
/--
Conjecture 6.9 in [Wa2011]:
$$
\lim_{\substack{n \to \infty \\ n \text{ odd}}} \frac{1}{n} \log(z_n / n!) = -1
$$
It is not even known if this limit exists. Note that $z_n = 0$ for even $n$ (see `z_even`), so the
limit must be restricted to odd $n$; here we parametrise odd $n$ as $2k + 1$.
-/
```
theorem growthRateZn : answer(sorry) ↔
    Filter.Tendsto (fun k => (1 : ℝ) / (2 * k + 1) *
      Real.log (z (2 * k + 1) / (2 * k + 1).factorial)) Filter.atTop
      (nhds (-1)) := by
```

### molsExistenceProblem
/--
MOLS existence problem: determine exactly which orders `n` admit a complete set of `n - 1`
mutually orthogonal latin squares.

Equivalently, this asks for which orders affine planes of order `n` exist. Complete sets are known
for prime-power orders; the smallest currently unresolved order is `12`.
-/
```
theorem molsExistenceProblem : answer(sorry) = {n : ℕ | HasCompleteMOLS n} := by
```

### molsOrder12
/--
The smallest unresolved case of the MOLS existence problem: whether there are `11` mutually
orthogonal latin squares of order `12`.
-/
```
theorem molsOrder12 : answer(sorry) ↔ HasCompleteMOLS 12 := by
```

## Paper/LatinTableau.lean
/-!
# Latin Tableau Conjecture

The Latin Tableau Conjecture states that the graph associated
to any (finite) Young diagram (i.e., whose vertices are the
cells of the diagram, with edges between cells in the same row
or column) is CDS-colorable, meaning that there exists a proper
coloring of the vertices of the graph such that for all k > 0, the
number of vertices with color < k equals the maximum size of
the union of k independent sets of the graph.

*References:*

* [The Latin Tableau Conjecture](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v32i2p48)
-/

### LatinTableauConjecture
/-- The Latin Tableau Conjecture: If G is the simple graph
  of a Young diagram, then G is CDS-colorable. -/
```
theorem LatinTableauConjecture (μ : YoungDiagram) :
     μ.toSimpleGraph.CDSColorable := by sorry
```

## Paper/MonochromaticQuantumGraph.lean
/-!
# Monochromatic quantum graphs (inherited vertex colorings)

This file studies the existence of *monochromatic quantum graphs*: edge-coloured, edge-weighted
complete graphs whose perfect matchings induce vertex colourings, with the property that

- every **non-monochromatic** inherited vertex colouring has total weight `0`, while
- each of the `D` **monochromatic** colourings has total weight `1`.

In the quantum-optics motivation, such a construction corresponds to generating high-dimensional
multipartite GHZ-type states using probabilistic pair sources and linear optics (without additional
resources), where interference patterns can be expressed as weighted sums over perfect matchings.

## Main questions (informal)

- For `N = 4` and `D ≥ 4`, does there exist such a graph/weighting?
- For even `N ≥ 6` and `D ≥ 3`, does there exist such a graph/weighting?

## Formalisation sketch

A quantum graph with `N` vertices and `D` colours can be encoded by a weight function
`W : EdgeN N D α → α` (for a coefficient domain `α`).

For each assignment of vertex indices `ι : V N → Fin D`, we define a perfect-matching sum
`pmSumN N D W ι` (a sum over perfect matchings, where each matching contributes the product of the
corresponding edge weights determined by `ι`). The equation system `EqSystemN N D W` requires

`pmSumN N D W ι = 1` iff `ι` is constant (all entries equal), and `0` otherwise.

The open conjectures in this file ask for non-existence/existence of such `W` over various
coefficient domains (e.g. `ℂ`, `ℝ`, `ℤ`, and restricted integer weights).

## References

* [Krenn2017] M. Krenn, X. Gu, A. Zeilinger,
  "Quantum Experiments and Graphs: Multiparty States as Coherent Superpositions of Perfect Matchings",
  *Physical Review Letters* 119(24), 240403 (2017).

* [MO2018] [Vertex coloring inherited from perfect matchings (motivated by quantum physics)](https://mathoverflow.net/questions/311325),
  MathOverflow question 311325.

* [Gu2019] X. Gu, M. Erhard, A. Zeilinger, M. Krenn,
  "Quantum experiments and graphs II: Quantum interference, computation, and state generation",
  *PNAS* 116(10), 4147–4155 (2019).

* [Krenn2019] [Questions on the Structure of Perfect Matchings inspired by Quantum Physics](https://arxiv.org/abs/1902.06023)
  by *M. Krenn, X. Gu, U. Soltész*,
  Proc. 2nd Croatian Combinatorial Days, 57–70 (2019).

* [Chandran2022] [Edge-coloured graphs with only monochromatic perfect matchings and their connection to quantum physics](https://arxiv.org/abs/2202.05562)
  by *N. Chandran, S. Gajjala* (2022).

* [Chandran2024] [Krenn–Gu conjecture for sparse graphs](https://arxiv.org/abs/2407.00303)
  by *N. Chandran, S. Gajjala, S. Illickan, M. Krenn*, MFCS 2024.
-/

### eqSystem6_no_solution_d3
/-- For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem6_no_solution_d3 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 3 ℂ, EqSystemN 6 3 W := by
```

### eqSystem6_no_solution_d4
/-- For $N = 6$ and $D = 4$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem6_no_solution_d4 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 4 ℂ, EqSystemN 6 4 W := by
```

### eqSystem6_no_solution_d5
/-- For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem6_no_solution_d5 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 5 ℂ, EqSystemN 6 5 W := by
```

### eqSystem6_no_solution_ge3
/-- For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem6_no_solution_ge3 :
    answer(sorry) ↔
      ∀ D : Nat, D ≥ 3 →
        ¬ ∃ W : WeightsN 6 D ℂ, EqSystemN 6 D W := by
```

### eqSystem8_no_solution_d3
/-- For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem8_no_solution_d3 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 8 3 ℂ, EqSystemN 8 3 W := by
```

### eqSystem10_no_solution_d3
/-- For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d3 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 3 ℂ, EqSystemN 10 3 W := by
```

### eqSystem10_no_solution_d4
/-- For $N = 10$ and $D = 4$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d4 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 4 ℂ, EqSystemN 10 4 W := by
```

### eqSystem10_no_solution_d5
/-- For $N = 10$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d5 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 5 ℂ, EqSystemN 10 5 W := by
```

### eqSystem10_no_solution_d6
/-- For $N = 10$ and $D = 6$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d6 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 6 ℂ, EqSystemN 10 6 W := by
```

### eqSystem10_no_solution_d7
/-- For $N = 10$ and $D = 7$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d7 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 7 ℂ, EqSystemN 10 7 W := by
```

### eqSystem10_no_solution_d8
/-- For $N = 10$ and $D = 8$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d8 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 8 ℂ, EqSystemN 10 8 W := by
```

### eqSystem10_no_solution_d9
/-- For $N = 10$ and $D = 9$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem10_no_solution_d9 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 9 ℂ, EqSystemN 10 9 W := by
```

### eqSystem12_no_solution_d3
/-- For $N = 12$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem12_no_solution_d3 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 12 3 ℂ, EqSystemN 12 3 W := by
```

### eqSystem14_no_solution_d3
/-- For $N = 14$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem14_no_solution_d3 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 14 3 ℂ, EqSystemN 14 3 W := by
```

### eqSystem16_no_solution_d3
/-- For $N = 16$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{C}$? -/
```
theorem eqSystem16_no_solution_d3 :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 16 3 ℂ, EqSystemN 16 3 W := by
```

### eqSystem_no_solution_ge6_ge3
/-- For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
quantum graph equation system over $\mathbb{C}$? -/
```
theorem eqSystem_no_solution_ge6_ge3 :
    answer(sorry) ↔
      ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
        ¬ ∃ W : WeightsN N D ℂ, EqSystemN N D W := by
```

### eqSystem6_no_solution_d3_real
/-- For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{R}$? -/
```
theorem eqSystem6_no_solution_d3_real :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 3 ℝ, EqSystemN 6 3 W := by
```

### eqSystem6_no_solution_d5_real
/-- For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{R}$? -/
```
theorem eqSystem6_no_solution_d5_real :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 5 ℝ, EqSystemN 6 5 W := by
```

### eqSystem6_no_solution_ge3_real
/-- For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{R}$? -/
```
theorem eqSystem6_no_solution_ge3_real :
    answer(sorry) ↔
      ∀ D : Nat, D ≥ 3 →
        ¬ ∃ W : WeightsN 6 D ℝ, EqSystemN 6 D W := by
```

### eqSystem8_no_solution_d3_real
/-- For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{R}$? -/
```
theorem eqSystem8_no_solution_d3_real :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 8 3 ℝ, EqSystemN 8 3 W := by
```

### eqSystem10_no_solution_d3_real
/-- For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{R}$? -/
```
theorem eqSystem10_no_solution_d3_real :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 3 ℝ, EqSystemN 10 3 W := by
```

### eqSystem_no_solution_ge6_ge3_real
/-- For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
quantum graph equation system over $\mathbb{R}$? -/
```
theorem eqSystem_no_solution_ge6_ge3_real :
    answer(sorry) ↔
      ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
        ¬ ∃ W : WeightsN N D ℝ, EqSystemN N D W := by
```

### eqSystem6_no_solution_d3_int
/-- For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$? -/
```
theorem eqSystem6_no_solution_d3_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 3 ℤ, EqSystemN 6 3 W := by
```

### eqSystem6_no_solution_d5_int
/-- For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$? -/
```
theorem eqSystem6_no_solution_d5_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 5 ℤ, EqSystemN 6 5 W := by
```

### eqSystem6_no_solution_ge3_int
/-- For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$? -/
```
theorem eqSystem6_no_solution_ge3_int :
    answer(sorry) ↔
      ∀ D : Nat, D ≥ 3 →
        ¬ ∃ W : WeightsN 6 D ℤ, EqSystemN 6 D W := by
```

### eqSystem8_no_solution_d3_int
/-- For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$? -/
```
theorem eqSystem8_no_solution_d3_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 8 3 ℤ, EqSystemN 8 3 W := by
```

### eqSystem10_no_solution_d3_int
/-- For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$? -/
```
theorem eqSystem10_no_solution_d3_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 3 ℤ, EqSystemN 10 3 W := by
```

### eqSystem_no_solution_ge6_ge3_int
/-- For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
quantum graph equation system over $\mathbb{Z}$? -/
```
theorem eqSystem_no_solution_ge6_ge3_int :
    answer(sorry) ↔
      ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
        ¬ ∃ W : WeightsN N D ℤ, EqSystemN N D W := by
```

### eqSystem6_no_solution_d3_trinary_int
/-- For $N = 6$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$? -/
```
theorem eqSystem6_no_solution_d3_trinary_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 3 ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN 6 3 W := by
```

### eqSystem6_no_solution_d5_trinary_int
/-- For $N = 6$ and $D = 5$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$? -/
```
theorem eqSystem6_no_solution_d5_trinary_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 6 5 ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN 6 5 W := by
```

### eqSystem6_no_solution_ge3_trinary_int
/-- For $N = 6$ and all $D \geq 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$? -/
```
theorem eqSystem6_no_solution_ge3_trinary_int :
    answer(sorry) ↔
      ∀ D : Nat, D ≥ 3 →
        ¬ ∃ W : WeightsN 6 D ℤ,
            (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
              EqSystemN 6 D W := by
```

### eqSystem8_no_solution_d3_trinary_int
/-- For $N = 8$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$? -/
```
theorem eqSystem8_no_solution_d3_trinary_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 8 3 ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN 8 3 W := by
```

### eqSystem10_no_solution_d3_trinary_int
/-- For $N = 10$ and $D = 3$, does there exist no solution to the monochromatic quantum graph
equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$? -/
```
theorem eqSystem10_no_solution_d3_trinary_int :
    answer(sorry) ↔
      ¬ ∃ W : WeightsN 10 3 ℤ,
          (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
            EqSystemN 10 3 W := by
```

### eqSystem_no_solution_ge6_ge3_trinary_int
/-- For all even $N \geq 6$ and $D \geq 3$, does there exist no solution to the monochromatic
quantum graph equation system over $\mathbb{Z}$ with weights in $\{-1, 0, 1\}$? -/
```
theorem eqSystem_no_solution_ge6_ge3_trinary_int :
    answer(sorry) ↔
      ∀ N D : Nat, N ≥ 6 → Even N → D ≥ 3 →
        ¬ ∃ W : WeightsN N D ℤ,
            (∀ e, W e = (-1 : ℤ) ∨ W e = 0 ∨ W e = 1) ∧
              EqSystemN N D W := by
```

## Paper/PrimeTuples.lean
/-!
# Prime Tuples Conjecture

*Reference:* [FLC07] Friedlander, J. B. and Luca, F. and Stoiciu, M., On the irrationality of a
divisor function series. Integers (2007).
-/

### prime_tuples_conjecture
/-- For any `k ≥ 2`, let `a₁,...,aₖ` and `b₁,...,bₖ` be integers with `aᵢ > 0`. Suppose that for
every prime `p` there exists an integer `n` such that `p ∤ ∏ i, (aᵢ n + bᵢ)`. Then there exist
infinitely many `n` such that `aᵢ n + bᵢ` is prime for all `i`. -/
```
theorem prime_tuples_conjecture {k : ℕ} (hk : 2 ≤ k) (a : Fin k → ℕ+) (b : Fin k → ℕ)
    (hab : ∀ p, p.Prime → ∃ n, ¬ p ∣ ∏ i, (a i * n + b i)) :
    Set.Infinite {n | ∀ i : Fin k, (a i * n + b i).Prime} := by sorry
```

## Paper/ReedOmegaDeltaChi.lean
/-!
# Reed's omega, delta, and chi conjecture

*References*:
- [B. Reed,  ω Δ and χ, J. Graph Theory 27 (1998) 177-212.](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0118(199804)27:4%3C177::AID-JGT1%3E3.0.CO;2-K)
- [openproblemgarden](http://www.openproblemgarden.org/op/reeds_omega_delta_and_chi_conjecture)
- [mathoverflow/37923](https://mathoverflow.net/questions/37923) asked by user [Andrew D. King](https://mathoverflow.net/users/4580/andrew-d-king)
-/

### reed_omega_delta_chi_conjecture
/--
For a graph $G$, we define $\Delta(G)$ to be the maximum degree, $\omega(G)$ to be the size of the
largest clique subgraph, and $\chi(G)$ to be the chromatic number. Reed's omega, delta, and chi
conjecture states that $$\chi(G) \leq \lceil \frac{1}{2}(\omega(G) + \Delta(G) + 1) \rceil.$$
-/
```
theorem reed_omega_delta_chi_conjecture :
  ∀ {V : Type} (G : SimpleGraph V),
    let χ := G.chromaticNumber
    let ω := G.ecliqueNum
    let Δ := G.emaxDegree
    2 * χ ≤ ω + Δ + 2 := by
```

### reed_omega_delta_chi_conjecture_for_finite_graphs
/--
For a finite graph $G$, we define $\Delta(G)$ to be the maximum degree, $\omega(G)$ to be the
size of the largest clique subgraph, and $\chi(G)$ to be the chromatic number. Reed's omega,
delta, and chi conjecture states that $$\chi(G) \leq \lceil \frac{1}{2}(\omega(G) + \Delta(G) + 1) \rceil.$$
-/
```
theorem reed_omega_delta_chi_conjecture_for_finite_graphs :
  ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
    let χ := G.chromaticNumber
    let ω := G.cliqueNum
    let Δ := G.maxDegree
    2 * χ ≤ ω + Δ + 2 := by
```

### reed_conjecture_Δ_6_ω_2
/--
The simplest open case is when $\Delta(G) = 6$ and $\omega(G) = 2$.
-/
```
theorem reed_conjecture_Δ_6_ω_2 :
  ∀ {V : Type} (G : SimpleGraph V), G.emaxDegree = 6 ∧ G.cliqueNum = 2 → G.chromaticNumber ≤ 5 := by
```

## Paper/RingelConjecture.lean
/-!
# Ringel's Conjecture

*Reference:* G. Ringel, *Problem 25*, in *Theory of Graphs and its Applications*
(Proc. Sympos. Smolenice, 1963), Academia, Prague, 1964.

Ringel's conjecture (1963): the complete graph $K_{2n+1}$ decomposes into copies of any tree
with $n$ edges. It remains open; the case of all sufficiently large $n$ is proved by
Montgomery–Pokrovskiy–Sudakov, see `Arxiv/2001.02665/RingelConjecture.lean`.
-/

### ringel_conjecture
/--
For any tree $T$ with $n$ edges, the complete graph $K_{2n+1}$ decomposes into
$2n+1$ edge-disjoint copies of $T$.

A "copy" of $T$ is the image $T.\text{map}(f_i)$ of $T$ under a vertex embedding
$f_i : V \hookrightarrow \text{Fin}(2n+1)$; the copies are pairwise edge-disjoint
and together cover every edge of $K_{2n+1}$.
-/
```
theorem ringel_conjecture {V : Type} [Finite V]
    (T : SimpleGraph V) (hT : T.IsTree)
    (n : ℕ) (hn : T.edgeSet.ncard = n) :
    ∃ f : Fin (2 * n + 1) → (V ↪ Fin (2 * n + 1)),
      Pairwise (fun i j => Disjoint (T.map (f i)).edgeSet (T.map (f j)).edgeSet) ∧
      ⨆ i, T.map (f i) = (⊤ : SimpleGraph (Fin (2 * n + 1))) := by
```

## Paper/StrongSensitivityConjecture.lean
/-!
# Strong Sensitivity Conjecture (`bs(f) ≤ s(f)^2`)

This file formalizes the *strong* sensitivity conjecture, asserting:

For every Boolean function `f : {0,1}^n → {0,1}`,
`bs(f) ≤ s(f)^2`,
where bs(f) denotes block sensitivity and s(f) denotes sensitivity.

Huang's theorem proves a *quartic* upper bound, `bs(f) ≤ s(f)^4`, thereby
resolving the most widely known form of the sensitivity conjecture.

We now ask whether a stronger upper bound holds. Interestingly, the original
paper of Nisan and Szegedy, where the sensitivity conjecture first appeared,
already speculated that a *quadratic* upper bound might be the correct
relation. On the lower bound side, Rubinstein
(https://link.springer.com/article/10.1007/BF01200762) constructed Boolean functions
exhibiting the first quadratic separation. The best currently
known gap, due to Ambainis and Sun (https://arxiv.org/abs/1108.3494), is
`bs(f) ≥ (2/3)⋅s(f)^2`.

*References:*
* [Induced Subgraphs of Hypercubes and a Proof of the Sensitivity Conjecture](https://arxiv.org/abs/1907.00847)
  by Hao Huang (see Section 3, Concluding Remarks)
* [Variations on the Sensitivity Conjecture](https://arxiv.org/abs/1011.0354)
  by Pooya Hatami, Raghav Kulkarni, and Denis Pankratov (see Question 3.1)
* [On the Degree of Boolean Functions as Real Polynomials](https://link.springer.com/article/10.1007/BF01263419)
  by Noam Nisan, and Mario Szegedy (see Section 4, Open Problems)
-/

### strong_sensitivity_conjecture
/-- Strong Sensitivity Conjecture,
for every Boolean function `f : {0,1}^n → {0,1}`,
`bs(f) ≤ s(f)^2`.

We call this the *strong* sensitivity conjecture because the original sensitivity
conjecture only asked for a polynomial bound in terms of `s(f)`. Huang's
celebrated result (often called the sensitivity theorem) gives a quartic bound,
`bs(f) ≤ s(f)^4`, thereby settling the original conjecture. -/
```
theorem strong_sensitivity_conjecture {n : ℕ} (f : (Fin n → Bool) → Bool) :
    blockSensitivity f ≤ sensitivity f ^ 2 := by
```

## Paper/VoronovskajaTypeFormula.lean
/-!
# Voronovskaja-type Formula for the Bezier Variant of the Bernstein Operators

The Bézier-type Bernstein operators $B_{n,\alpha}$ for $\alpha > 0$ are defined for
$f : [0,1] \to \mathbb{R}$ by
$$
(B_{n,\alpha} f)(x)
  = \sum_{k=0}^n f\!\left(\frac{k}{n}\right)
    \left( J_{n,k}(x)^{\alpha} - J_{n,k+1}(x)^{\alpha} \right),
$$
where
$$
J_{n,k}(x) = \sum_{j=k}^n p_{n,j}(x),
\qquad
p_{n,j}(x) = \binom{n}{j} x^j(1-x)^{n-j},
$$
and $J_{n,n+1}(x) = 0$.

In the classical case $\alpha = 1$, these operators reduce to the usual Bernstein operators.
For $f$ which are $C^2$ on $[0,1]$, one has the classical Voronovskaja
asymptotic formula
$$
\lim_{n \to \infty} n\bigl( B_{n,1} f(x) - f(x) \bigr)
    = \tfrac{1}{2} x(1-x) f''(x).
$$

## Known Results
* For $\alpha = 1$, the asymptotics are completely understood.
* Numerical experiments indicate that for $\alpha \neq 1$ the quantity
    $$
        \sqrt{n}\,\bigl( B_{n,\alpha} f(x) - f(x) \bigr)
    $$
    may converge to a non-zero limit.

## The Problem
Determine the asymptotic behaviour of the Bézier-type Bernstein operators for $\alpha > 0$,
$\alpha \neq 1$:
\textbf{Existence of the limit:}
    Prove (or disprove) the existence of the limit
    $$
        \lim_{n \to \infty}
        \sqrt{n}\,\bigl( B_{n,\alpha} f(x) - f(x) \bigr),
    $$
    at least for sufficiently smooth functions $f$.
    \textbf{Explicit form of the limit:}
    If the limit exists, determine an explicit expression for it in terms of $f$, $x$, and $\alpha$.

*References:*

* [Voronovskaja-type Formula for the Bézier Variant of the Bernstein Operators](https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2010/files_CTF-2010/Open_problems.pdf),
  by *Ulrich Abel*, in *Constructive Theory of Functions, Sozopol 2010*.
-/

### voronovskaja_theorem
/--
Conjecture: Voronovskaja-type formula for Bézier-Bernstein operators
with shape parameter $\alpha > 0$, $\alpha \neq 1$.

The source asks for sufficiently smooth functions. This concrete version uses
`ContDiffOn ℝ 2 f I` as a readable baseline regularity assumption; since the
domain is the compact interval $[0,1]$, this also explains why no separate
boundedness assumption is included here. The variants below record the unknown
smoothness threshold more explicitly.
-/
```
theorem voronovskaja_theorem.bezier_bernstein_operators
    (α : ℝ) (hα_pos : 0 < α) (hα : α ≠ 1)
    (f : ℝ → ℝ) (x : ℝ) (hx : x ∈ I)
    (hf : ContDiffOn ℝ 2 f I) :
    Tendsto (fun n : ℕ => Real.sqrt n * (bezierBernstein n α f x - f x)) atTop
      (𝓝 answer(sorry)) := by
```

### voronovskaja_theorem
/--
Variant of the Bézier-Bernstein Voronovskaja problem which treats "sufficiently smooth" as an
eventual condition in the smoothness order $m$: for all sufficiently large finite $m$, every
$C^m$ function on $[0,1]$ should have the asserted asymptotic formula.
-/
```
theorem voronovskaja_theorem.bezier_bernstein_operators.variants.eventually_smooth
    (α : ℝ) (hα_pos : 0 < α) (hα : α ≠ 1) :
    let limitFormula : (ℝ → ℝ) → ℝ → ℝ := answer(sorry)
    ∀ᶠ m : ℕ in atTop,
      ∀ (f : ℝ → ℝ) (x : ℝ), x ∈ I → ContDiffOn ℝ m f I →
        Tendsto (fun n : ℕ => Real.sqrt n * (bezierBernstein n α f x - f x)) atTop
          (𝓝 (limitFormula f x)) := by
```

### voronovskaja_theorem
/--
Existence-only version of the eventual-smoothness variant. This separates the first part of the
source problem, proving that the scaled sequence has some limit, from the stronger task of finding
an explicit expression for that limit.
-/
```
theorem voronovskaja_theorem.bezier_bernstein_operators.variants.eventually_smooth.limit_exists
    (α : ℝ) (hα_pos : 0 < α) (hα : α ≠ 1) :
    ∀ᶠ m : ℕ in atTop,
      ∀ (f : ℝ → ℝ) (x : ℝ), x ∈ I → ContDiffOn ℝ m f I →
        ∃ L : ℝ,
          Tendsto (fun n : ℕ => Real.sqrt n * (bezierBernstein n α f x - f x)) atTop
            (𝓝 L) := by
```

### voronovskaja_theorem
/--
Variant of the Bézier-Bernstein Voronovskaja problem with the required smoothness order itself
left as an answer. Replacing `(answer(sorry) : ℕ × ((ℝ → ℝ) → ℝ → ℝ))` by a concrete value lets one
state the conjecture for a chosen regularity threshold.
-/
```
theorem voronovskaja_theorem.bezier_bernstein_operators.variants.answer_smoothness
    (α : ℝ) (hα_pos : 0 < α) (hα : α ≠ 1) :
    let p : ℕ × ((ℝ → ℝ) → ℝ → ℝ) := answer(sorry)
    let m := p.1
    let limitFormula := p.2
    ∀ (f : ℝ → ℝ) (x : ℝ), x ∈ I → ContDiffOn ℝ m f I →
      Tendsto (fun n : ℕ => Real.sqrt n * (bezierBernstein n α f x - f x)) atTop
        (𝓝 (limitFormula f x)) := by
```

## Paper/WeakTiling.lean
/-!
# Weak tiling problems

Problems 4.1, 4.2, and 4.3 from [arxiv/2506.23631](https://arxiv.org/abs/2506.23631).

*Reference:*
* [Geometric implications of weak tiling](https://arxiv.org/abs/2506.23631)

See also `FormalConjectures.Wikipedia.Fuglede` for Fuglede's spectral set conjecture, which
motivates the study of weak tilings.
-/

### problem_4_1
/-- **Problem 4.1.** Let $\Omega \subset \mathbb{R}$ be a finite union of intervals and $\nu$
    a weak tiling measure for $\Omega$. Must $\mathrm{supp}(\nu)$ have bounded density? -/
```
theorem problem_4_1 :
    answer(sorry) ↔ ∀ (Ω : Set ℝ) (_ : IsFiniteUnionOfIntervals Ω)
      (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν), HasBoundedDensity ν.support := by
```

### problem_4_2
/-- **Problem 4.2.** Let $\Omega \subset \mathbb{R}$ be a finite union of three or more
    intervals. If $\Omega$ weakly tiles its complement, must it also tile its complement
    properly? -/
```
theorem problem_4_2 :
    answer(sorry) ↔ ∀ (n : ℕ) (_ : 3 ≤ n) (Ω : Set ℝ)
      (_ : IsUnionOfNIntervals n Ω) (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν),
      ∃ T : Set ℝ, IsProperTiling Ω T := by
```

### problem_4_3
/-- **Problem 4.3.** Let $\Omega \subset \mathbb{R}$ be a finite union of intervals and $\nu$
    a weak tiling measure for $\Omega$. Must $\nu$ be expressible as a convex combination of
    proper tiling measures? -/
```
theorem problem_4_3 :
    answer(sorry) ↔ ∀ (Ω : Set ℝ) (_ : IsFiniteUnionOfIntervals Ω)
      (ν : Measure ℝ) (_ : IsWeakTilingMeasure Ω ν),
      ∃ (T : ℕ → Set ℝ) (c : ℕ → ℝ≥0), (∀ i, IsProperTiling Ω (T i)) ∧ ∑' i : ℕ, c i = 1 ∧
      ν = Measure.sum
        (fun i => (c i : ℝ≥0∞) • Measure.sum (fun t : T i => Measure.dirac (t : ℝ))) := by
```

## Paper/WeaklyFirstCountable.lean
/-!
# Conjectures about Weakly First Countable spaces

This file formalizes the notion of a weakly first countable topological space and some conjectures
around those.

*References:*
* [Ar2013] Arhangeliski, Alexandr. "Selected old open problems in general topology."
  Buletinul Academiei de Ştiinţe a Republicii Moldova. Matematica 73.2-3 (2013): 37-46.
  https://www.math.md/files/basm/y2013-n2-3/y2013-n2-3-(pp37-46).pdf.pdf
* [Ya1976] Yakovlev, N. N. "On the theory of o-metrizable spaces."
  Doklady Akademii Nauk. Vol. 229. No. 6. Russian Academy of Sciences, 1976.
  https://www.mathnet.ru/links/016f74007f9f96fa3aadae05cbd98457/dan40570.pdf (in Russian)
-/

### existsWeaklyFirstCountableCompactBig
/-- Problem 2 in [Ar2013]: Give an example in ZFC of a weakly first-
countable compact Hausdorff space X such that $𝔠 < |X|$.

Note: [Ar2013] uses a blanket convention that all spaces are
Tychonoff and "compact" means compact Hausdorff. -/
```
theorem existsWeaklyFirstCountableCompactBig : answer(sorry) ↔
    ∃ (X : Type) (_ : TopologicalSpace X),
      WeaklyFirstCountableTopology X ∧ CompactSpace X ∧ T2Space X ∧
        𝔠 < #X := by
```

### existsWeaklyFirstCountableCompactNotFirstCountable
/-- Problem 3 in [Ar2013]: Give an example in ZFC of a weakly first-
countable compact Hausdorff space which is not first countable.

Note: [Ar2013] uses a blanket convention that all spaces are
Tychonoff and "compact" means compact Hausdorff. -/
```
theorem existsWeaklyFirstCountableCompactNotFirstCountable :
    ∃ (X : Type) (_ : TopologicalSpace X),
      WeaklyFirstCountableTopology X ∧ CompactSpace X ∧ T2Space X ∧
        ¬ FirstCountableTopology X := by
```

### cardinalMk_le_continuum_of_weaklyFirstCountable_of_countableSouslinNumber
/-- Problem 4 in [Ar2013]: If a Tychonoff weakly first-countable space has countable
Souslin number, then does its cardinality not exceed the continuum? -/
```
theorem cardinalMk_le_continuum_of_weaklyFirstCountable_of_countableSouslinNumber :
    answer(sorry) ↔ ∀ (X : Type) (_ : TopologicalSpace X), T35Space X →
      WeaklyFirstCountableTopology X → HasCountableSouslinNumber X → #X ≤ 𝔠 := by
```

## Paper/ZagierMZV.lean
/-!
# Zagier's Conjecture on Multiple Zeta Values

*References:*
- [Za94] Zagier, Don. "Values of zeta functions and their applications."
  First European Congress of Mathematics Paris, July 6–10, 1992: Vol. II: Invited Lectures (Part 2). Basel: Birkhäuser Basel, 1994.
- [Co18] Combariza, Germán AG. "A few conjectures about the multiple zeta values."
  ACM Communications in Computer Algebra 52.1 (2018): 11-20.
- [Te02] T. Terasoma. Mixed Tate motives and multiple zeta values. Invent. Math., 149(2):339–369, 2002.
- [DG05] P. Deligne and A. Goncharov. Groupes fondamentaux motiviques de Tate mixte. Ann. Sci.
  Ecole Norm. Sup. (4), 38(1):1–56, 2005.
- [OEIS A000931](https://oeis.org/A000931)
-/

### zagier_conjecture
/--
**Zagier's conjecture**

The $\mathbb{Q}$-dimension of the vector space spanned by all multiple zeta values
of weight $n$ equals $d_n$, where $d_n$ is the Zagier dimension sequence
satisfying $d_0 = 1$, $d_1 = 0$, $d_2 = 1$, and $d_n = d_{n-2} + d_{n-3}$ for $n \geq 3$.
-/
```
theorem zagier_conjecture :
    answer(sorry) ↔ ∀ n : ℕ, Module.finrank ℚ (mzvSpanOfWeight n) = zagierDim n := by
```


---
OEIS: 76 files
Arxiv: 24 files
Paper: 23 files
Mathoverflow: 10 files
Total: 133 files
