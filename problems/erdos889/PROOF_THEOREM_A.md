# Erdős #889: an explicit threshold for the lowercase v₁ problem (Theorem A)

Cross-vendor refereed 2026-09-26 (OpenAI Codex, GPT-6 Astra): PASS-WITH-REPAIRS, N0 unchanged; repairs applied — see REFEREE_ASTRA_20260926.md.

**Published 2026-09-25:** Zenodo DOI [10.5281/zenodo.22962744](https://doi.org/10.5281/zenodo.22962744) (concept DOI 10.5281/zenodo.22962743). Source of the note: publish/automath-papers/erdos889/.

Historical status (2026-09-25): refereed same-vendor (Claude Opus, adversarial, fresh context) —
PASS-WITH-REPAIRS, repairs R1–R6 applied; see REFEREE_CLAUDE_20260925.md.

Written by a Claude (Opus) worker for the automath project. The same-vendor report was followed
by a Codex cross-vendor review on 2026-09-26 (`REFEREE_ASTRA_20260926.md`, PASS-WITH-REPAIRS).
No human referee or Lean verification is claimed; nothing here is kernel-checked.
All numerical constants come from `n0_compute.py` in this directory, which uses mpmath interval
arithmetic. Its full output is reproduced in Appendix A. External theorems and attack points are
listed in `CHECKS.md`.

Notation. `log` is the natural logarithm. p and q denote primes. P(m) is the largest prime factor
of an integer m ≥ 2, and P(1) = 1. ω(m) is the number of distinct prime factors of m, v_p is the
p-adic valuation, and π(x) = #{p ≤ x} for real x.

## 0. Statements

**Theorem A.** Put ℓ₁ := 45.28 and N0 := exp(exp(ℓ₁)). Then

  log N0 = e^45.28 ≈ 4.62 × 10¹⁹ (4.6223 × 10¹⁹ to five figures).

For every integer n ≥ N0 there is an integer k with 1 ≤ k ≤ 10 log n and v(n,k) ≥ 2. In words,
n + k has at least two distinct prime factors greater than k.

*Where the number comes from.* Section 5.1 defines an explicit constant for l = 1 and C₀ = 10:

  K = C₁(3)·κ₁²κ₂κ₃ + κ₁/ℓ₁⁴ = 2.41092… × 10¹¹.

Here C₁(3) = (3e/2)·30⁶·3^3.5 = 1.390073… × 10¹¹ is Matveev's constant for three logarithms over ℚ,
κ₁ = 1.05085…, κ₂ = 1.03018… and κ₃ = 1.52458…. Suppose some n with log log n ≥ ℓ₁ had
v(n,k) ≤ 1 for every 1 ≤ k ≤ 10 log n. Then log n < K·(log log n)⁵ (Proposition 5.2). But
ℓ ↦ ℓ − 5 log ℓ is increasing for ℓ > 5, and at ℓ = 45.28 the value ℓ − 5 log ℓ − log K is
0.00722… > 0, certified by interval arithmetic. So log n ≥ K·(log log n)⁵ whenever
log log n ≥ 45.28, and no such n exists. The value 45.28 is the least multiple of 0.01 for which
this certificate holds; 45.27 fails.

**Corollary A1.** Every n with v₁(n) = 1 satisfies n < N0, so {n : v₁(n) = 1} is finite. In
Formal Conjectures terms (`FormalConjectures/ErdosProblems/889.lean`), this is a paper proof,
not a Lean proof, that `Erdos889.erdos_889.variants.v1_eq_1_finite` holds with answer `True`. It
depends on the published results E1–E3 (§2). The qualitative finiteness also follows from
Langevin 1981 together with Lemma R(1) (§7.1).

**Theorem A_l (fixed l).** Let l ≥ 1 be an integer and C₀ = 10. Compute the constants (5.1) for
this l. If ℓ₁ passes the certificate of Proposition 5.2, then every n with log log n ≥ ℓ₁ and
log n ≥ l has a k with l ≤ k ≤ 10·l·log n and v(n,k) ≥ 2. The certified values are ℓ₁(1) = 45.28,
ℓ₁(2) = 45.35, …, ℓ₁(20) = 45.58; the full table for l ≤ 20 is in §5.3.

**Theorem A_unif (uniform in l).** Let l ≥ 1 and n be integers with log log n ≥ 48.82 and
log n ≥ l. Then there is an integer k with l ≤ k ≤ 10·l·log n and v(n,k) ≥ 2. Equivalently, the
statement holds for C₀ = 10 and every n ≥ N(l), where

  N(l) := max(exp(e^48.82), ⌈e^l⌉),  e^48.82 ≈ 1.593 × 10²¹.

**Corollary A_l.** For every l ≥ 1 and every n ≥ N(l), v_l(n) ≥ 2. This is the level-2 case of
`erdos_889.variants.general`. That variant asks for v_l(n) → ∞, which is not proved here.

**Not claimed.**

* The main problem v₀(n) → ∞.
* v₀(n) ≥ 3 for all large n, or v_l(n) ≥ 3 for all large n.
* The conjectures that 330 is the largest n with v₁(n) = 1 and that 80 is the largest n with
  V₁(n) = 1.

N0 is far beyond any computation, so the exception set of v₁ is still not determined. The proof
uses Matveev's theorem, which is not in Mathlib. No Lean statement is claimed.

## 1. The definitions pinned

The FC definitions, verbatim from `889.lean`:

```lean
def v (n k : ℕ) : ℕ :=
  ((n + k).primeFactors.filter (fun p =>
    ∀ i ∈ range k, ¬ p ∣ n + i)).card

noncomputable def v_l (l n : ℕ) : ℕ∞ :=
  ⨆ k ≥ l, (v n k : ℕ∞)

theorem erdos_889.variants.v1_eq_1_finite :
    answer(sorry) ↔ {n | v_l 1 n = 1}.Finite
```

So v(n,k) counts the primes p dividing n + k with p ∤ n + i for every 0 ≤ i ≤ k − 1. For k ≥ 1 we
have n + k ≥ 1, so `primeFactors` is the usual set of prime divisors. Also
v_l(n) = sup_{k ≥ l} v(n,k), taken in ℕ ∪ {∞}.

**Lemma 1.1.** For integers n ≥ 0 and k ≥ 1, v(n,k) = #{p : p | n + k and p > k}.

*Proof.* Let p | n + k.

* If p ≤ k, then i := k − p satisfies 0 ≤ i ≤ k − 1 and p | (n + k) − p = n + i. So p is not
  counted.
* If p > k, take any 0 ≤ i ≤ k − 1. The difference (n + k) − (n + i) = k − i lies in [1, k], so
  p does not divide it, and hence p ∤ n + i. So p is counted. ∎

Thus v(n,k) ≥ 2 means that n + k has two distinct prime factors greater than k. And v(n,k) ≤ 1
means that n + k has at most one prime factor greater than k.

*Proof of Corollary A1 from Theorem A.* Let n ≥ N0. Theorem A gives some k ≥ 1 with v(n,k) ≥ 2.
Then v_l 1 n ≥ 2, so v_l 1 n ≠ 1. Hence {n | v_l 1 n = 1} ⊆ {n ∈ ℕ : n < N0}, which is finite. ∎

Corollary A_l follows from Theorem A_unif in the same way.

## 2. External results used

The proof uses three published results. Each was read from a scan of the original publication;
`CHECKS.md` gives the access details and says where each result is applied.

**E1 (Matveev 2000, Corollary 2.3).** E. M. Matveev, "An explicit lower bound for a homogeneous
rational linear form in the logarithms of algebraic numbers. II", Izv. Ross. Akad. Nauk Ser. Mat.
64 (2000), no. 6, 125–180; English translation in Izv. Math. 64 (2000), 1217–1269. We read the
Russian original, pp. 125–127.

The setting (§1 and §2, pp. 125–127):

* 𝕂 is an algebraic number field of degree D over ℚ, embedded in ℂ.
* ϰ = 1 if 𝕂 ⊆ ℝ, and ϰ = 2 otherwise.
* α₁, …, α_n ∈ 𝕂* have absolute logarithmic heights h(α_j).
* ln α₁, …, ln α_n are arbitrary fixed **nonzero** values of the logarithms ("произвольные
  фиксированные ненулевые значения логарифмов").
* b₁, …, b_n ∈ ℤ, and the following are defined:

```
(1.1)  Λ  = b₁ ln α₁ + ⋯ + b_n ln α_n,
(1.3)  B  = max{1, max{|b_j| A_j / A_n : 1 ≤ j ≤ n}},
(1.4)  B* = max{|b₁|, …, |b_n|},
(2.4)  A_j ≥ max{D h(α_j), |ln α_j|, 0.16},
       Ω  = A₁ ⋯ A_n.
```

The original statement of Corollary 2.3: «Следствие 2.3. Если Λ ≠ 0, A_j из (2.4), B из (1.3), то
ln|Λ| > −C₁(n)D²Ω ln(eD) ln(eB), C₁(n) = C₁(n,ϰ) = min{(1/ϰ)((1/2)en)^ϰ 30^{n+3} n^{3.5},
2^{6n+20}}, при этом B может быть заменено на B* из (1.4).»

In English: *If Λ ≠ 0, the A_j satisfy (2.4) and B is given by (1.3), then*

  ln|Λ| > −C₁(n) D² Ω ln(eD) ln(eB),  C₁(n) = C₁(n,ϰ) = min{ (1/ϰ)(en/2)^ϰ · 30^(n+3) · n^3.5 , 2^(6n+20) },

*and B may be replaced by B\* from (1.4).*

We use it only with 𝕂 = ℚ ⊂ ℝ. Then D = 1, ϰ = 1 and ln(eD) = 1. We need n = 2 or 3; below this
count of logarithms is called t, to avoid a clash with our n. The constants are:

  C₁(3) := C₁(3,1) = min{(3e/2)·30⁶·3^3.5, 2³⁸} = (3e/2)·30⁶·3^3.5 = 1.390073… × 10¹¹,
  C₁(2) := C₁(2,1) = min{e·30⁵·2^3.5, 2³²} = e·30⁵·2^3.5 = 7.47318… × 10⁸.

A simplified form is widely quoted: 1.4·30^(t+3)·t^4.5·D²(1 + log D)(1 + log B)A₁⋯A_t. It is
weaker, since 1.4·30⁶·3^4.5 = 1.4319 × 10¹¹ ≥ C₁(3). Using it instead gives ℓ₁ = 45.31 and
log N0 = 4.76 × 10¹⁹ (Appendix A).

For a rational number a/b in lowest terms, h(a/b) = log max(|a|, |b|).

**E2 (Rosser–Schoenfeld 1962).** J. B. Rosser and L. Schoenfeld, "Approximate formulas for some
functions of prime numbers", Illinois J. Math. 6 (1962), 64–94. Page 69, Corollary 1, (3.5):

  x/log x < π(x) for 17 ≤ x.

Here x is real. Theorem 2, (3.3), on the same page gives x/(log x − 1/2) < π(x) for 67 ≤ x; it is
used only in Remark 7.2.

**E3 (Robin 1983).** G. Robin, "Estimation de la fonction de Tchebychef θ sur le k-ième nombre
premier et grandes valeurs de la fonction ω(n) nombre de diviseurs premiers de n", Acta Arith. 42
(1983), 367–389. Page 369, Théorème 11:

  ω(n) ≤ 1,3841 · log n / log log n pour n ≥ 3.

Théorème 13 on the same page gives ω(n) ≤ log n/(log log n − 1,1714) for n ≥ 26; it is used only
in Remark 7.2.

Everything else below is elementary and is proved in full. We write R := 1.3841.

## 3. The reduction (Lemma R)

**Setting.** Fix integers l ≥ 1 and n ≥ 2 and a real number y with Y := ⌊y⌋ ≥ l + 2. Put
Π_l(n) := n(n+1)⋯(n+l−1) and

  ω_{l,y}(n) := #{p ≤ y : p | Π_l(n)},  𝒫 := {p ≤ y : p ∤ Π_l(n)},  so |𝒫| = π(y) − ω_{l,y}(n).

The hypothesis is:

  **(H)** v(n,k) ≤ 1 for every integer k with l ≤ k ≤ y.

Define

  A := π(y) − 2·ω_{l,y}(n) − 2·log((Y−l−1)!)/log n,  and, when A > 1,  T := log((Y−l−1)!)/(A − 1).

**Lemma R.** Assume (H).

1. For p ∈ 𝒫 let k₀(p) := min{k ≥ l : p | n + k}. Then l ≤ k₀(p) ≤ p − 1 ≤ Y − 1 and
   P(n + k₀(p)) = p. The map p ↦ k₀(p) is injective. Hence J := k₀(𝒫) ⊆ {l, l+1, …, Y−1} has
   |J| = π(y) − ω_{l,y}(n), and for j ∈ J every prime factor of n + j is at most Y.
2. Assume J ≠ ∅. For every prime p ≤ Y fix j_p ∈ J with v_p(n + j_p) = max_{j∈J} v_p(n + j). For
   j ∈ J let

     U_j := ∏_{p ≤ Y, j_p = j} p^{v_p(n+j)},  W_j := ∏_{p ≤ Y, j_p ≠ j} p^{v_p(n+j)}.

   Then n + j = U_j·W_j for each j ∈ J, and ∏_{j∈J} W_j ≤ (Y − l − 1)!.
3. Let s(j) := ω(U_j), J₀ := {j ∈ J : s(j) = 0} and J₁ := {j ∈ J : s(j) = 1}. Then
   |J₀| ≤ log((Y−l−1)!)/log n, and |J₁| ≥ π(y) − 2ω_{l,y}(n) − 2|J₀| ≥ A.
4. For j ∈ J₁, U_j = q_j^{e_j} with q_j a prime ≤ Y and e_j ≥ 1. So n + j = W_j·q_j^{e_j} with
   q_j ∤ W_j. The map j ↦ q_j is injective on J₁.
5. If A > 1, then J ≠ ∅, and there are j₁ ≠ j₂ in J₁ with log W_{j₁} ≤ T and log W_{j₂} ≤ T.

*Proof of (1).* Let p ∈ 𝒫. Among the p consecutive integers n, n+1, …, n+p−1 there is a multiple
n + i of p, with 0 ≤ i ≤ p − 1.

* If p ≤ l, this n + i is a factor of Π_l(n), contradicting p ∤ Π_l(n). So p ≥ l + 1.
* Since p ∤ n + i for i < l, the multiple has l ≤ i ≤ p − 1. Hence l ≤ k₀(p) ≤ p − 1.
* Since p ≤ y and p is an integer, p ≤ Y. So k₀(p) ≤ Y − 1 < y, and (H) gives v(n, k₀(p)) ≤ 1.
* By Lemma 1.1 (note k₀(p) ≥ 1), n + k₀(p) has at most one prime factor greater than k₀(p). The
  prime p is such a factor. So every other prime factor of n + k₀(p) is ≤ k₀(p) < p, and
  P(n + k₀(p)) = p ≤ Y.
* If k₀(p) = k₀(p′), then p = P(n + k₀(p)) = p′. So the map is injective, and |J| = |𝒫|. ∎

*Proof of (2).* By (1), n + j = ∏_{p≤Y} p^{v_p(n+j)} for j ∈ J. Split the primes p ≤ Y into those
with j_p = j and those with j_p ≠ j; this gives n + j = U_j·W_j.

Fix a prime p ≤ Y and some j ∈ J with j ≠ j_p. Since v_p(n+j) ≤ v_p(n+j_p), the power
p^{v_p(n+j)} divides both n + j and n + j_p. Hence it divides their difference j − j_p ≠ 0, and
v_p(n+j) ≤ v_p(|j − j_p|). Sum over j ∈ J∖{j_p}, which is a subset of {l, …, Y−1}∖{j_p}; all terms
are ≥ 0, so

  Σ_{j∈J, j≠j_p} v_p(n+j) ≤ Σ_{i=l, i≠j_p}^{Y−1} v_p(|i − j_p|) = v_p((j_p − l)!·(Y − 1 − j_p)!) ≤ v_p((Y−l−1)!).

The last step holds because a!·b! divides (a+b)! (binomial coefficients are integers), with
a + b = Y − l − 1. Therefore

  ∏_{j∈J} W_j = ∏_{p≤Y} p^{Σ_{j∈J, j≠j_p} v_p(n+j)} ≤ ∏_{p≤Y} p^{v_p((Y−l−1)!)} = (Y−l−1)!.

The final equality holds because every prime factor of (Y−l−1)! is ≤ Y. ∎

*Proof of (3).* The bound on J₀:

* For j ∈ J₀ we have U_j = 1, so W_j = n + j > n and log W_j > log n.
* All W_j ≥ 1, so by (2):
  |J₀|·log n ≤ Σ_{j∈J₀} log W_j ≤ Σ_{j∈J} log W_j ≤ log((Y−l−1)!).

The bound on J₁:

* s(j) = #{p ≤ Y : j_p = j and v_p(n+j) ≥ 1}.
* Every prime p ≤ Y has exactly one j_p. So these sets, for j ∈ J, are pairwise disjoint subsets
  of the primes ≤ Y, and Σ_{j∈J} s(j) ≤ π(Y) = π(y).
* Put J_{≥2} := J ∖ (J₀ ∪ J₁). Then
  |J₁| + 2|J_{≥2}| ≤ π(y)  and  |J₀| + |J₁| + |J_{≥2}| = |J| = π(y) − ω_{l,y}(n).
* Substituting |J_{≥2}| = π(y) − ω_{l,y}(n) − |J₀| − |J₁| into the first inequality gives
  |J₁| ≥ π(y) − 2ω_{l,y}(n) − 2|J₀|.
* With the bound on |J₀|, this is ≥ A. ∎

*Proof of (4).* If s(j) = 1, there is exactly one prime q = q_j ≤ Y with j_q = j and
v_q(n+j) ≥ 1. The other primes p with j_p = j contribute p⁰ = 1. So U_j = q_j^{e_j} with
e_j := v_{q_j}(n+j) ≥ 1. Also q_j ∤ W_j, because W_j contains only primes p with j_p ≠ j. Finally
q_j determines j = j_{q_j}, so j ↦ q_j is injective. ∎

*Proof of (5).* If J = ∅, then π(y) = ω_{l,y}(n) and A ≤ −π(y) < 1. So A > 1 forces J ≠ ∅.

By (3), |J₁| ≥ A > 1, so the integer m := |J₁| is at least 2. List the numbers log W_j (j ∈ J₁) as
w₁ ≤ w₂ ≤ ⋯ ≤ w_m, and let j₁, j₂ be indices giving w₁ and w₂. All w_i are ≥ 0, so by (2)

  (m − 1)·w₂ ≤ w₂ + ⋯ + w_m ≤ Σ_{j∈J} log W_j ≤ log((Y−l−1)!).

Since m − 1 ≥ A − 1 > 0, we get w₁ ≤ w₂ ≤ log((Y−l−1)!)/(A − 1) = T. ∎

*Remark.* Parts (2) and (3) use a standard device: for each prime, discard the term in which it
occurs to the highest power. This device appears in the Sylvester–Erdős arguments on products of
consecutive integers. The proof above is complete, so nothing depends on this attribution.

## 4. The linear form in three logarithms

**Proposition B.** Work in the setting of §3. Assume (H), A > 1 and Y ≤ n, and put L := log n.
Then

  **(4.1)** L − log Y < C₁(3)·(log Y)²·max(T, 0.16)·(1 + log B̄),  where B̄ := log(n + Y)/log 2.

*Proof.* Take j₁ ≠ j₂ from Lemma R(5), and write W_i := W_{j_i}, q_i := q_{j_i} and e_i := e_{j_i}.
Then, for i = 1, 2:

* n + j_i = W_i·q_i^{e_i};
* q₁ ≠ q₂ (Lemma R(4)), q_i ≤ Y and e_i ≥ 1;
* log W_i ≤ T.

Define, with real logarithms,

  Λ := log(n + j₁) − log(n + j₂) = e₁ log q₁ − e₂ log q₂ + log(W₁/W₂).

*Nonvanishing.* Λ ≠ 0, because j₁ ≠ j₂ and log is injective on (0, ∞).

*Upper bound.* By the mean value theorem, |Λ| = |j₁ − j₂|/ξ for some ξ between n + j₁ and
n + j₂, so ξ > n. Since j₁, j₂ ∈ {l, …, Y−1}, we have |j₁ − j₂| ≤ Y − 1 − l < Y. Hence
|Λ| < Y/n, that is,

  **(4.2)** −log|Λ| > L − log Y.

*Exponents.* q_i^{e_i} ≤ n + j_i < n + Y, so e_i ≤ log(n+Y)/log q_i ≤ log(n+Y)/log 2 = B̄. Hence
B* := max(|e₁|, |−e₂|, 1) ≤ B̄; note that B̄ ≥ 1.

*Case 1: W₁ ≠ W₂.* Apply E1 with 𝕂 = ℚ (so D = 1 and ϰ = 1) and t = 3:

  α₁ = q₁, α₂ = q₂, α₃ = W₁/W₂;  b₁ = e₁, b₂ = −e₂, b₃ = 1;

with ln α_j the real logarithms.

* The logarithms are nonzero: q_i ≥ 2 and W₁/W₂ ≠ 1.
* Heights: h(q_i) = log q_i. Write W₁/W₂ = a/b in lowest terms; then a | W₁ and b | W₂, so
  h(W₁/W₂) = log max(a, b) ≤ log max(W₁, W₂) ≤ T.
* Also |ln(W₁/W₂)| = |log W₁ − log W₂| ≤ max(log W₁, log W₂) ≤ T, because both logarithms are ≥ 0.

Take A₁ := log q₁, A₂ := log q₂ and A₃ := max(T, 0.16). Then (2.4) holds:

* max{h(q_i), |ln q_i|, 0.16} = log q_i, because log q_i ≥ log 2 > 0.16;
* A₃ ≥ max{h(α₃), |ln α₃|, 0.16}.

Since Λ ≠ 0, Corollary 2.3 applies. Replacing B by B* gives

  −log|Λ| < C₁(3)·log q₁·log q₂·max(T, 0.16)·(1 + log B*) ≤ C₁(3)·(log Y)²·max(T, 0.16)·(1 + log B̄).

*Case 2: W₁ = W₂.* Now Λ = e₁ log q₁ − e₂ log q₂ ≠ 0. Apply E1 with t = 2, α₁ = q₁, α₂ = q₂ and
A_i = log q_i:

  −log|Λ| < C₁(2)·log q₁·log q₂·(1 + log B*) ≤ 0.16·C₁(3)·(log Y)²·(1 + log B̄).

This uses C₁(2) = 7.47 × 10⁸ ≤ 0.16·C₁(3) = 2.22 × 10¹⁰, which the script certifies. So the Case 2
bound is at most the Case 1 bound.

In both cases, combining with (4.2) gives (4.1). ∎

## 5. Numerical closure for fixed l

### 5.1 Constants

Fix an integer l ≥ 1 and put c := C₀ = 10 and R := 1.3841. For real ℓ₁ define:

```
(5.1)  m   := log(c·l),
       κ₁  := 1 + m/ℓ₁,
       κ₂  := 1 + (1 − log log 2 + e^(−ℓ₁))/ℓ₁,            (−log log 2 = +0.36651…)
       μ   := 2Rm/(c − 2R),
       ρ   := (ℓ₁ + m − 1)/(ℓ₁ − μ),
       ε₁  := 3·e^(−ℓ₁) / (c(ℓ₁ + m − 1)),
       e₁  := 2c + (2c(m − 1) + 2R/ℓ₁ + 6e^(−ℓ₁) + 1)/ℓ₁,
       ε₂  := e₁·κ₁·ℓ₁²·e^(−ℓ₁) / ((c − 2R)(1 − μ/ℓ₁)),
       κ₃  := (c/(c − 2R))·ρ·κ₁·(1 + ε₁)/(1 − ε₂),
       K   := C₁(3)·κ₁²·κ₂·κ₃ + κ₁/ℓ₁⁴,
       φ(ℓ₁) := ℓ₁ − 5 log ℓ₁ − log K.
```

**Proposition 5.2.** Let l ≥ 1, and let ℓ₁ ≥ 10 satisfy ℓ₁ > μ, ε₂ < 1 and φ(ℓ₁) ≥ 0. Then every
integer n with log log n ≥ ℓ₁ and log n ≥ l has an integer k with l ≤ k ≤ 10·l·log n and
v(n,k) ≥ 2.

Two more side conditions are needed: m > 1 and κ₃ℓ₁² ≥ 0.16. They hold automatically, because
m ≥ log 10 and κ₃ ≥ 1, and the script checks them anyway.

*Proof.* Let L := log n, ℓ := log L ≥ ℓ₁ ≥ 10, y := c·l·L and Y := ⌊y⌋. Suppose, for
contradiction, that v(n,k) ≤ 1 for every integer k ∈ [l, y]; this is (H).

Preliminary facts:

* L ≥ e¹⁰, so y ≥ 10L ≥ 67.
* Y > y − 1 ≥ l + 2, since y ≥ 10·l·L.
* Y ≤ y ≤ cL² < e^L = n, since l ≤ L and L ≥ e¹⁰.
* n ≥ 26 and l − 1 < n.
* log y = ℓ + m.

*S1 (primes).* By E2 (3.5) with x = y ≥ 17:

  π(y) > y/log y = c·l·L/(ℓ + m).

*S2 (ω).* Every prime dividing Π_l(n) divides some n + i with 0 ≤ i ≤ l − 1. Each n + i ≥ 3, so
by E3

  ω_{l,y}(n) ≤ Σ_{i=0}^{l−1} ω(n+i) ≤ Σ_{i=0}^{l−1} R·log(n+i)/log log(n+i) ≤ l·R·(L + 1)/ℓ.

The last step uses log(n+i) ≤ log(n+l−1) ≤ L + (l−1)/n ≤ L + 1 and log log(n+i) ≥ log log n = ℓ > 0.

*S3 (factorial).* Define G(x) := (x + 1) log x − x + 1. For integers M ≥ 1,

  log M! = Σ_{i=1}^{M−1} log i + log M ≤ ∫_1^M log t dt + log M = G(M),

because log i ≤ ∫_i^{i+1} log t dt. G is increasing on [1, ∞), since G′(x) = log x + 1/x > 0. With
M = Y − l − 1 ∈ [1, y − l − 1]:

  log((Y−l−1)!) ≤ G(y − l − 1) = (y − l)·log(y − l − 1) − (y − l − 1) + 1 ≤ y log y − y + l + 2 = l·L·c(ℓ + m − 1) + l + 2.

*S4 (A).* By S1–S3 and the definition of A in §3 (with log n = L):

  A − 1 ≥ c·l·L/(ℓ + m) − 2lRL/ℓ − 2lR/ℓ − 2cl(ℓ + m − 1) − 2(l + 2)/L − 1 = l·L·a(ℓ) − E(ℓ),

where

  a(ℓ) := c/(ℓ + m) − 2R/ℓ = (c − 2R)(ℓ − μ)/(ℓ(ℓ + m)),
  E(ℓ) := 2lR/ℓ + 2cl(ℓ + m − 1) + 2(l + 2)/L + 1.

Since ℓ ≥ ℓ₁ > μ, a(ℓ) > 0. For all ℓ ≥ ℓ₁ we have 1/l ≤ 1, (l+2)/l ≤ 3, 1/L = e^(−ℓ) ≤ e^(−ℓ₁),
1/ℓ ≤ 1/ℓ₁ and m − 1 > 0. These give:

  E(ℓ)/l ≤ 2cℓ + (2c(m − 1) + 2R/ℓ₁ + 6e^(−ℓ₁) + 1) ≤ e₁·ℓ,
  1/a(ℓ) = ℓ(ℓ + m)/((c − 2R)(ℓ − μ)) ≤ κ₁ℓ/((c − 2R)(1 − μ/ℓ₁)).

Hence E(ℓ)/(l·L·a(ℓ)) ≤ [e₁κ₁/((c − 2R)(1 − μ/ℓ₁))]·ℓ²e^(−ℓ) ≤ ε₂, because ℓ²e^(−ℓ) is decreasing
for ℓ ≥ 2. Therefore

  A − 1 ≥ l·L·a(ℓ)·(1 − ε₂) > 0.

*S5 (T).* By S3, log((Y−l−1)!) ≤ l·L·c(ℓ + m − 1)·(1 + ε₁), since

  (l + 2)/(l·L·c(ℓ + m − 1)) ≤ 3e^(−ℓ₁)/(c(ℓ₁ + m − 1)) = ε₁.

Combining with S4:

  T ≤ c(ℓ + m − 1)(1 + ε₁)/(a(ℓ)(1 − ε₂)) = (c/(c − 2R))·((ℓ + m − 1)/(ℓ − μ))·ℓ(ℓ + m)·(1 + ε₁)/(1 − ε₂) ≤ κ₃ℓ².

Two facts give the last step:

* (ℓ + m − 1)/(ℓ − μ) is decreasing in ℓ, since its derivative has the sign of −(m − 1 + μ) < 0.
  So it is ≤ ρ.
* ℓ + m ≤ κ₁ℓ.

Also 0.16 ≤ κ₃ℓ², so max(T, 0.16) ≤ κ₃ℓ².

*S6 (B̄ and log Y).* We have log(n + Y) ≤ L + Y/n ≤ L + 1 and log(L + 1) ≤ ℓ + 1/L. So

  1 + log B̄ ≤ 1 + ℓ + e^(−ℓ₁) − log log 2 ≤ κ₂ℓ,  and  log Y ≤ log y = ℓ + m ≤ κ₁ℓ.

*S7 (conclusion).* All hypotheses of Proposition B hold: A > 1 by S4, and Y ≤ n. By (4.1) and
S5–S6,

  L < κ₁ℓ + C₁(3)·κ₁²ℓ²·κ₃ℓ²·κ₂ℓ ≤ K·ℓ⁵,

using κ₁ℓ ≤ (κ₁/ℓ₁⁴)·ℓ⁵. That is, **log n < K·(log log n)⁵**.

But ψ(ℓ) := ℓ − 5 log ℓ has ψ′(ℓ) = 1 − 5/ℓ > 0 for ℓ > 5. So ψ(ℓ) ≥ ψ(ℓ₁) ≥ log K, which means
L = e^ℓ ≥ K·ℓ⁵. This is a contradiction. ∎

### 5.2 Proof of Theorem A

For l = 1 the script takes ℓ₁ = 45.28 and certifies the following with interval arithmetic
(60 digits, outward rounding; values rounded for display):

| quantity | value |
|---|---|
| m = log 10 | 2.30258509299 |
| κ₁ | 1.05085214428 |
| κ₂ | 1.03017917227 |
| μ | 0.881387214031 |
| ρ | 1.04919010235 |
| ε₁ | 1.39329644231 × 10⁻²² |
| e₁ | 20.5987817363 |
| ε₂ | 1.35404300089 × 10⁻¹⁶ |
| κ₃ | 1.52457710226 |
| C₁(3) | 1.39007316922 × 10¹¹ |
| K | 2.41092138023 × 10¹¹ |
| φ(45.28) | 0.00722781770539 > 0 |

All side conditions are certified: ℓ₁ ≥ 10, ℓ₁ > μ, ε₂ < 1, κ₃ℓ₁² ≥ 0.16, m > 1 and y ≥ 67.
Proposition 5.2 therefore applies with l = 1. The condition log n ≥ l = 1 is automatic. So every
n with log log n ≥ 45.28, that is every n ≥ N0 = exp(e^45.28), has some k with
1 ≤ k ≤ 10 log n and v(n,k) ≥ 2. This proves Theorem A. ∎

*How much S1–S7 lose.* The script also evaluates the right side of (4.1) directly, using only the
bounds S1–S3 and S6. That right side first drops below L near ℓ ≈ 45.272, but no monotonicity is
claimed there. So the κ-simplifications cost less than 0.01 in ℓ₁. The script also checks that the
direct right side is ≤ Kℓ⁵ at ℓ ∈ {45.28, 46, 50, 60, 100, 1000}. This checks the algebra in S4–S7.

### 5.3 Theorem A_l for l ≤ 20 (C₀ = 10)

| l | ℓ₁(l) | log N(l) = e^ℓ₁(l) | K(l) |
|---|---|---|---|
| 1 | 45.28 | 4.622 × 10¹⁹ | 2.411 × 10¹¹ |
| 2 | 45.35 | 4.957 × 10¹⁹ | 2.570 × 10¹¹ |
| 3 | 45.39 | 5.160 × 10¹⁹ | 2.666 × 10¹¹ |
| 4 | 45.42 | 5.317 × 10¹⁹ | 2.736 × 10¹¹ |
| 5 | 45.44 | 5.424 × 10¹⁹ | 2.791 × 10¹¹ |
| 10 | 45.51 | 5.818 × 10¹⁹ | 2.968 × 10¹¹ |
| 15 | 45.55 | 6.055 × 10¹⁹ | 3.076 × 10¹¹ |
| 20 | 45.58 | 6.239 × 10¹⁹ | 3.154 × 10¹¹ |

All l from 1 to 20 are in Appendix A. The per-l threshold depends on l only through
m = log(10l), and it grows slowly: the same certificate gives ℓ₁(l) = 45.95 at l = 10³, 46.53 at
l = 10⁶ and 47.54 at l = 10¹². For every l with 1 ≤ l ≤ log n, §6 gives the single threshold
log log n ≥ 48.82.

## 6. Uniform in l

Put c = 10 and R = 1.3841 as before, and define:

```
(6.1)  κ₁ᵘ := 2 + log c/ℓ₁,
       μᵘ  := 2R·log c/(c − 4R),
       ρᵘ  := (2ℓ₁ + log c − 1)/(ℓ₁ − μᵘ),
       ε₁ᵘ := 3e^(−ℓ₁)/(c(ℓ₁ + log c − 1)),
       e₁ᵘ := 4c + (2c(log c − 1) + 2R/ℓ₁ + 6e^(−ℓ₁) + 1)/ℓ₁,
       ε₂ᵘ := e₁ᵘ·κ₁ᵘ·ℓ₁²·e^(−ℓ₁) / ((c − 4R)(1 − μᵘ/ℓ₁)),
       κ₃ᵘ := (c/(c − 4R))·ρᵘ·κ₁ᵘ·(1 + ε₁ᵘ)/(1 − ε₂ᵘ),
       Kᵘ  := C₁(3)·(κ₁ᵘ)²·κ₂·κ₃ᵘ + κ₁ᵘ/ℓ₁⁴,
       φᵘ(ℓ₁) := ℓ₁ − 5 log ℓ₁ − log Kᵘ.
```

Here κ₂ is as in (5.1).

**Proposition 6.1.** Suppose c > 4R, ℓ₁ ≥ 10, ℓ₁ > μᵘ, ε₂ᵘ < 1 and φᵘ(ℓ₁) ≥ 0. Then for every
integer l ≥ 1 and every integer n with log log n ≥ ℓ₁ and log n ≥ l, some k with
l ≤ k ≤ c·l·log n has v(n,k) ≥ 2.

*Proof.* Repeat the proof of Proposition 5.2. Now m = log(cl) is no longer fixed; from
1 ≤ l ≤ L we only know log c ≤ m ≤ ℓ + log c. S1–S3 are unchanged. The later steps change as
follows.

* **S4.** a(ℓ) = c/(ℓ + m) − 2R/ℓ is decreasing in m. So
  a(ℓ) ≥ aᵘ(ℓ) := c/(2ℓ + log c) − 2R/ℓ = (c − 4R)(ℓ − μᵘ)/(ℓ(2ℓ + log c)) > 0.
  Using m ≤ ℓ + log c:
  E(ℓ)/l ≤ 2R/ℓ₁ + 2c(2ℓ + log c − 1) + 6e^(−ℓ₁) + 1 ≤ e₁ᵘℓ.
  Also 1/aᵘ(ℓ) ≤ κ₁ᵘℓ/((c − 4R)(1 − μᵘ/ℓ₁)). Hence E/(l·L·a) ≤ E/(l·L·aᵘ) ≤ ε₂ᵘ, and
  A − 1 ≥ l·L·a(ℓ)·(1 − ε₂ᵘ) > 0.
* **S5.** Since m ≥ log c, (l + 2)/(l·L·c(ℓ + m − 1)) ≤ ε₁ᵘ. Also
  c(ℓ + m − 1)/a(ℓ) ≤ c(2ℓ + log c − 1)/aᵘ(ℓ) ≤ (c/(c − 4R))·ρᵘ·κ₁ᵘ·ℓ².
  Here (2ℓ + log c − 1)/(ℓ − μᵘ) is decreasing, since its derivative has the sign of
  −(2μᵘ + log c − 1) < 0. So T ≤ κ₃ᵘℓ².
* **S6.** log Y ≤ ℓ + m ≤ 2ℓ + log c ≤ κ₁ᵘℓ. The bound on 1 + log B̄ is unchanged; it uses
  Y ≤ cL² < n.
* **S7.** L < Kᵘℓ⁵, which contradicts φᵘ(ℓ₁) ≥ 0 as before. ∎

With c = 10 (and 4R = 5.5364 < 10), the script certifies ℓ₁ = 48.82. The values are κ₁ᵘ = 2.0472,
μᵘ = 1.4280, ρᵘ = 2.0877, ε₂ᵘ = 2.87 × 10⁻¹⁷, κ₃ᵘ = 9.5752, Kᵘ = 5.734 × 10¹² and
φᵘ = 0.00182 > 0. This proves Theorem A_unif; the threshold is e^48.82 ≈ 1.593 × 10²¹ for log n.

## 7. Remarks

### 7.1 The Langevin route: qualitative

Lemma R(1) alone reduces Theorem A to a statement about smooth numbers in short intervals. Take
l = 1 and y = K := ⌊10 log n⌋. Under (H), the set 𝒴 := {1 ≤ i ≤ K : P(n + i) ≤ K} has at least
π(K) − ω(n) elements.

Langevin [La81, Corollaire 1, (8)], read from the scan, states: "Soit ε un réel positif, soit
r(ε) = sup(C·C^{c/ε}, exp exp(c+ε)^{−1}) (resp. sup(C·C^{(1+c)/ε}, exp exp(1+c+ε)^{−1})). Pour
tout triplet (n,k,a) d'entiers vérifiant (1), on a, si log n/log k ≥ r(ε), [(7)] (respectivement
(8) card Y < sup(2, (1+c+ε) π(k) log₂(log n/(log k)²) (log(log n/(log k)²))^{−1}), où Y désigne la
partie formée des éléments vérifiant P(n+ia) ≤ k)." In this statement:

* condition (1) is "n > 1, a ≥ 1, (n,a) = 1, k ≥ 2, a < n^{t₁}";
* log₂ means log log;
* C and c are effectively computable constants depending on the parameters t₁, …, t₆ of his
  Théorème 1.

Take a = 1 and k = K. Then (8) bounds |𝒴| by o(π(K)). On the other hand, by E3 and S1 the lower
bound π(K) − ω(n) is at least (1 − 0.139 − o(1))·π(K). These contradict each other for large n.
So the qualitative Corollary A1 follows from [La81] together with Lemma R(1). The l-version of
Lemma R(1) gives Corollary A_l qualitatively as well.

This route was found in the G2 gate (`G2_KILL_GATE_20260925.md` §3). We have not refereed
Langevin's proof. His Théorème 1 allows any real t₁ < 1, and C and c depend on t₁, …, t₆. His
Exemple (p. 242) takes t₁ = 1/2, t₂ = 1, t₃ = 1/3, t₄ = 3 and t₅ = t₆ = 6. With t₁ = 1/2, the
condition a = 1 < n^{t₁} holds for every n > 1.

Langevin's constants are effective. We have not computed a certified numerical onset for this alternative route and use it only to establish the qualitative consequence.

RST II [RST76, Theorem 2] bounds the number of k-smooth terms among u+1, …, u+k by π(k). That bound
is exactly borderline: it does not contradict π(K) − ω(n), so it does not suffice.

### 7.2 Refined constants: log N0′ = 3.36 × 10¹⁹

The same proof with three sharper inputs gives a smaller threshold.

1. **S1 with E2 (3.3).** π(y) > y/(log y − 1/2), valid for y ≥ 67.
2. **S2 with E3 Théorème 13.** For n + i ≥ 26,
   ω(n + i) ≤ log(n+i)/(log log(n+i) − ρ₀) ≤ (L + 1)/(ℓ − ρ₀), with ρ₀ := 1.1714.
3. **Case 1 of Proposition B with B from (1.3) in place of B\*.** Order the numbers with
   α₃ = W₁/W₂ last and take A₃ := τ := κ₃′ℓ². This is allowed because τ ≥ T ≥ h(α₃), τ ≥ |ln α₃|
   and τ ≥ 0.16. Then B = max{1, e₁ log q₁/τ, e₂ log q₂/τ, 1} ≤ max{1, (L + 1)/τ}.

Define:

```
a′(ℓ) := c/(ℓ + m − 1/2) − 2/(ℓ − ρ₀) = (c − 2)(ℓ − μ′)/((ℓ + m − 1/2)(ℓ − ρ₀)),
μ′    := (cρ₀ + 2m − 1)/(c − 2),
g     := 1 + (m − 1/2)/ℓ₁,
ρ′    := (ℓ₁ + m − 1)/(ℓ₁ − μ′),
e₁′   := 2c + (2c(m − 1) + 2/(ℓ₁ − ρ₀) + 6e^(−ℓ₁) + 1)/ℓ₁,
ε₂′   := e₁′·g·ℓ₁²·e^(−ℓ₁) / ((c − 2)(1 − μ′/ℓ₁)),
κ₃′   := (c/(c − 2))·ρ′·g·(1 + ε₁)/(1 − ε₂′).
```

With these, S4–S5 give T ≤ κ₃′ℓ². Put d′ := 2 log ℓ₁ + log κ₃′ − 1 − e^(−ℓ₁); we need
ℓ₁ − d′ ≥ 1. Then

  1 + log B ≤ max{1, 1 + ℓ + e^(−ℓ) − log κ₃′ − 2 log ℓ} ≤ ℓ − d′,

and so L < κ₁ℓ + C₁(3)·κ₁²·κ₃′·ℓ⁴·(ℓ − d′).

Case 2 is dominated when κ₃′ℓ₁ ≥ C₁(2)κ₂/C₁(3). Put

  Q(ℓ) := (κ₁ℓ + C₁(3)κ₁²κ₃′ℓ⁴(ℓ − d′))·e^(−ℓ).

Q is non-increasing for ℓ ≥ ℓ₁ when ℓ₁ ≥ 10 and ℓ₁ − d′ ≥ 3, because its log-derivative is
≤ 4/ℓ + 1/(ℓ − d′) − 1 < 0. The script certifies ℓ₁ = 44.96, Q(44.96) = 0.99329 < 1 and all side
conditions. So the conclusion of Theorem A holds for all n with log log n ≥ 44.96, that is with
log N0′ = e^44.96 ≈ 3.356 × 10¹⁹.

Theorem A is stated with the simpler 45.28. The refinement changes log N0 only by a factor 0.73.

### 7.3 The constant 10

For fixed l the argument works with any C₀ = c > 2R = 2.7682. Then a(ℓ) > 0 for large ℓ, but the
threshold grows as c decreases towards 2R. With Robin's Théorème 13, any c > 2 works. The uniform
version as written needs c > 4R. We did not try to optimise c or the thresholds.

### 7.4 Finite check (evidence only)

`python3 n0_compute.py --check` checks every conclusion of Lemma R(1)–(5) on every triple
(n, l, Y) with 3 ≤ n ≤ 10⁶, l ∈ {1, 2, 3}, l + 2 ≤ Y ≤ 150 and v(n,k) ≤ 1 for all l ≤ k ≤ Y. There
are 91,709 such triples, 40,312 of them with |J₁| ≥ 2, and none fails.

It also lists the n ≤ 10⁶ for which no k ≤ 10 log n has v(n,k) ≥ 2. There are exactly 28:

  2, 3, 4, 6, 7, 8, 10, 12, 15, 16, 18, 22, 24, 26, 30, 36, 42, 46, 48, 60, 70, 78, 80, 96, 120, 190, 222, 330.

These are the values n ≥ 2 in Erdős–Selfridge's list of n with v₁(n) = 1 [ErSe67]. This is a
consistency check of the code and of the statements. It is not part of the proof.

## 8. What this adds and what it does not

What is proved here, relative to the sources checked in the G2 gate and in prior-art pass B
(`PRIOR_ART_20260925_B.md`):

1. An explicit threshold, log N0 = e^45.28 ≈ 4.62 × 10¹⁹, for Theorem A. This gives an explicit
   bound for the finiteness of {n : v₁(n) = 1}.
2. An explicit uniform-in-l statement with C0=10 and N(l)=max(exp(exp(48.82)), ceil(exp(l))), plus sharper per-l values for l<=20. Here exp(48.82) is approximately 1.59315 × 10^21.

What is not new:

* The qualitative finiteness, and its uniform-in-l analogue. Both follow from Langevin 1981 and
  Lemma R(1) (§7.1), as the G2 gate observed. We did not find that connection recorded in the
  sources we read.
* The tools. Baker-type lower bounds applied to smooth terms in blocks of consecutive integers go
  back to Ramachandra–Shorey–Tijdeman [RST75, RST76], Tijdeman [Ti73] and Langevin [La81]. The
  assignment of maximal prime powers is classical. The numerical inputs are Matveev, Rosser–
  Schoenfeld and Robin.

N0 is nowhere near the conjectured largest exception, 330.

The novelty check has limits. It consists of the G2 gate and prior-art pass B. Both were single
same-vendor passes without general web search. Pass B obtained Guy, *Unsolved Problems in Number
Theory*, 3rd ed. (2004), B27, which still says Erdős and Selfridge "are unable to prove even
that v₁(n) = 1 has only a finite number of solutions" and cites no later work on it. The
following were not obtained and have not been checked:

* Erdős 1998, p. 178;
* Shorey–Tijdeman, *Exponential Diophantine Equations* (1986);
* Erdős, Publ. Math. Debrecen 23 (1976);
* the Tijdeman result that Langevin cites (MR 54, 1977, p. 246);
* the MR review of Langevin 1981.

Any of these may already contain Theorem A or its qualitative form.

## 9. References

- [ErSe67] P. Erdős, J. L. Selfridge, Some problems on the prime factors of consecutive integers,
  Illinois J. Math. 11 (1967), 428–430.
- [La81] M. Langevin, Facteurs premiers d'entiers en progression arithmétique, Acta Arith. 39
  (1981), 241–249.
- [Ma00] E. M. Matveev, An explicit lower bound for a homogeneous rational linear form in the
  logarithms of algebraic numbers. II, Izv. Ross. Akad. Nauk Ser. Mat. 64 (2000), no. 6, 125–180;
  English translation in Izv. Math. 64 (2000), no. 6, 1217–1269.
- [RST75] K. Ramachandra, T. N. Shorey, R. Tijdeman, On Grimm's problem relating to factorisation
  of a block of consecutive integers, J. reine angew. Math. 273 (1975), 109–124.
- [RST76] K. Ramachandra, T. N. Shorey, R. Tijdeman, On Grimm's problem relating to factorisation
  of a block of consecutive integers. II, J. reine angew. Math. 288 (1976), 192–201.
- [Ro83] G. Robin, Estimation de la fonction de Tchebychef θ sur le k-ième nombre premier et grandes
  valeurs de la fonction ω(n) nombre de diviseurs premiers de n, Acta Arith. 42 (1983), 367–389.
- [RS62] J. B. Rosser, L. Schoenfeld, Approximate formulas for some functions of prime numbers,
  Illinois J. Math. 6 (1962), 64–94.
- [Ti73] R. Tijdeman, On integers with many small prime factors, Compositio Math. 26 (1973),
  319–330. This 1973 paper is the only Tijdeman
  paper on the topic that has been checked. Its Theorem 1 does not give Theorem A; see the G2 gate,
  row 2.
- [FC] google-deepmind/formal-conjectures, `FormalConjectures/ErdosProblems/889.lean`.

## Appendix A. Output of `n0_compute.py --check`

This is the historical output before the 2026-09-26 R1 side-check correction, not a new execution.
The script's historical sha256 is recorded in `CHECKS.md`. The run used Python 3.12 and mpmath 1.3.0, and took
about 6 s on one core. The corrected side condition was independently checked in the cross-vendor report;
Python is unavailable in the repair environment, so this transcript has not been regenerated.

```
Erdos #889 -- threshold computation (mpmath 1.3.0 , iv.dps = 60 )

== Matveev constants (Cor. 2.3, kappa = 1, D = 1) ==
  C1(3): (3e/2)*30^6*3^3.5 = 139007316922.0 ; 2^38 = 274877906944.0 ; min = 139007316922.0
  C1(2): e*30^5*2^3.5      = 747318511.874 ; 2^32 = 4294967296.0 ; min = 747318511.874
  comparison: 1.4*30^6*3^4.5 = 143186215391.0
    [OK] C1(2) <= 0.16 * C1(3)  (case W1 = W2 is dominated)
  -log log 2 = 0.366512920582

== Theorem A  (l = 1, C0 = 10; RS (3.5), Robin Thm 11, Matveev B*) ==
  ell1 = 45.28   (grid 0.01; ell1 - 0.01 = 45.27 fails the certificate)
  m         = 2.30258509299
  kappa1    = 1.05085214428
  kappa2    = 1.03017917227
  mu        = 0.881387214031
  ratio     = 1.04919010235
  eps1      = 1.39329644231e-22
  e1        = 20.5987817363
  eps2      = 1.35404300089e-16
  kappa3    = 1.52457710226
  K         = 241092138023.0
  phi(ell1) = 0.00722781770539
    [OK] phi(ell1) >= 0
    [OK] ell1 >= 10 (phi increasing, ell^2 e^-ell decreasing)
    [OK] ell1 > mu
    [OK] eps2 < 1 (so A - 1 > 0)
    [OK] kappa3 * ell1^2 >= 0.16
    [OK] m > 1 (monotonicity of ratio, sign of e1 bracket)
    [OK] y = c l L >= 67 (so >= 17)
  log N = exp(ell1) = 4.62225755084e+19
  => Theorem A holds for all n with log log n >= 45.28,
     i.e. log n >= 4.62226e+19, and on that range log n < K (log log n)^5 fails.
  => N0 := exp(exp(45.28)),  log N0 = 4.622e+19
  (variant) with the simplified constant 1.4*30^6*3^4.5 in place of C1(3): ell1 = 45.31, log N0 = 4.763e+19

== Sanity: unsimplified RHS of (4.1) vs K*ell^5 and vs L (direct evaluation) ==
  ell=  45.28: A=6.88835e+18 T=3125.81 RHS=4.58897e+19 K ell^5=4.58897e+19 L=4.62226e+19
    [OK] RHS <= K ell^5 at ell = 45.28
    [OK] RHS < L at ell = 45.28
  ell=     46: A=1.39451e+19 T=3221.15 RHS=4.94835e+19 K ell^5=4.96561e+19 L=9.49612e+19
    [OK] RHS <= K ell^5 at ell = 46
    [OK] RHS < L at ell = 46
  ell=     50: A=7.04244e+20 T=3776.94 RHS=7.37741e+19 K ell^5=7.53413e+19 L=5.18471e+21
    [OK] RHS <= K ell^5 at ell = 50
    [OK] RHS < L at ell = 50
  ell=     60: A=1.30612e+25 T=5360.01 RHS=1.77479e+20 K ell^5=1.87473e+20 L=1.14201e+26
    [OK] RHS <= K ell^5 at ell = 60
    [OK] RHS < L at ell = 60
  ell=    100: A=1.88349e+42 T=14457.9 RHS=2.13212e+21 K ell^5=2.41092e+21 L=2.68812e+43
    [OK] RHS <= K ell^5 at ell = 100
    [OK] RHS < L at ell = 100
  ell=   1000: A=1.42019e+432 T=1.389e+6 RHS=1.94236e+26 K ell^5=2.41092e+26 L=1.97007e+434
    [OK] RHS <= K ell^5 at ell = 1000
    [OK] RHS < L at ell = 1000
  (info) the unsimplified bound first falls below L near ell = 45.2719 (no monotonicity claimed there; the theorem uses ell1 = 45.28)

== Theorem A_l, C0 = 10, per l (same method, fixed l) ==
   l   ell1(l)   log N(l) = exp(ell1)       K(l)
   1   45.28   4.622e+19                    2.411e+11  OK
   2   45.35   4.957e+19                    2.57e+11  OK
   3   45.39   5.16e+19                     2.666e+11  OK
   4   45.42   5.317e+19                    2.736e+11  OK
   5   45.44   5.424e+19                    2.791e+11  OK
   6   45.46   5.534e+19                    2.837e+11  OK
   7   45.48   5.646e+19                    2.876e+11  OK
   8   45.49   5.702e+19                    2.91e+11  OK
   9   45.50   5.76e+19                     2.941e+11  OK
  10   45.51   5.818e+19                    2.968e+11  OK
  11   45.52   5.876e+19                    2.993e+11  OK
  12   45.53   5.935e+19                    3.016e+11  OK
  13   45.54   5.995e+19                    3.037e+11  OK
  14   45.54   5.995e+19                    3.057e+11  OK
  15   45.55   6.055e+19                    3.076e+11  OK
  16   45.56   6.116e+19                    3.093e+11  OK
  17   45.56   6.116e+19                    3.109e+11  OK
  18   45.57   6.177e+19                    3.125e+11  OK
  19   45.57   6.177e+19                    3.14e+11  OK
  20   45.58   6.239e+19                    3.154e+11  OK

== Theorem A_unif (all 1 <= l <= log n, C0 = 10) ==
  ell1 = 48.82   (grid 0.01; ell1 - 0.01 = 48.81 fails the certificate)
  kappa1u   = 2.04716479093
  kappa2    = 1.02799084229
  muu       = 1.42799893683
  ratiou    = 2.08774862579
  eps1u     = 3.75691341781e-24
  e1u       = 40.5552725119
  eps2u     = 2.866464257e-17
  kappa3u   = 9.57515341656
  Ku        = 5.73427154249e+12
  phi(ell1) = 0.00181783635267
    [OK] phi(ell1) >= 0
    [OK] ell1 >= 10
    [OK] c > 4*1.3841
    [OK] ell1 > mu_u
    [OK] eps2_u < 1
    [OK] kappa3_u * ell1^2 >= 0.16
    [OK] log c > 1
  log N = exp(ell1) = 1.59314977484e+21
  => for every l >= 1 and every n with log n >= max(exp(48.82), l):
     some k in [l, 10 l log n] has v(n,k) >= 2.   exp(48.82) = 1.593e+21

== Remark 7.2: refined inputs, l = 1 (RS (3.3), Robin Thm 13, Matveev B of (1.3)) ==
  ell1 = 44.96   (grid 0.01; ell1 - 0.01 = 44.95 fails the certificate)
  m         = 2.30258509299
  kappa1    = 1.05121408125
  mu_r      = 1.91489627325
  ratio_r   = 1.07474674441
  g         = 1.04009308481
  eps1      = 1.93201925961e-22
  e1_r      = 20.6026996407
  eps2_r    = 1.68492896332e-16
  kappa3_r  = 1.39729582097
  dprime    = 6.94608522348
  Q         = 0.993290452437
  phi(ell1) = 0.00673215777013
    [OK] phi(ell1) >= 0
    [OK] ell1 >= 10
    [OK] ell1 > mu_r
    [OK] eps2_r < 1
    [OK] ell1 - d' >= 3 (Q non-increasing; 1 <= ell - d')
    [OK] case W1 = W2 dominated: kappa3*ell1 >= C1(2) kappa2 / C1(3)
    [OK] m - 1 + mu_r > 0
  log N = exp(ell1) = 3.35644786965e+19
  => log N0' = exp(44.96) = 3.356e+19

== Summary ==
  Theorem A:        log log N0 = 45.28, log N0 = 4.622e+19
  Theorem A_unif:   log log N* = 48.82, log N* = 1.593e+21
  Remark (refined): log log N0' = 44.96, log N0' = 3.356e+19
  ALL CHECKS PASSED

== Finite check of Lemma R, 3 <= n <= 1000000, l in (1, 2, 3), all admissible Y <= 150 ==
  instances (n,l,Y) with v(n,k) <= 1 for all l <= k <= Y and Y >= l+2: 91709
  of which |J1| >= 2: 40312;  failures: 0
  n in [2,1000000] with no k <= 10 log n and v(n,k) >= 2: 28 values, max 330
  [2, 3, 4, 6, 7, 8, 10, 12, 15, 16, 18, 22, 24, 26, 30, 36, 42, 46, 48, 60, 70, 78, 80, 96, 120, 190, 222, 330]
```
