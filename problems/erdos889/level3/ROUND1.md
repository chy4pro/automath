# Erdős #889, level 3: proof campaign, round 1

**Status: OPEN.** There is no proof of (L3) and no counterexample.

**What this round proves.**

1. **Unconditional (Baker step).** Proposition 2.3 and Corollary 2.4 give an effective bound
   O(π(K)·log log log n / log log n) = o(π(K)) on the number of block terms of the form
   (K-smooth) × (1 or one prime power r^b with r > K and r^b ≤ exp((log n)^β)), for any fixed β < 1/2.
   Here K = ⌊C log n⌋ and the block is n + j, 0 ≤ j ≤ K.
2. **Structure (Theorem 2.5).** Suppose v(n,k) ≤ 2 for all k ≤ K. Then at least π(K)·(1 − o(1))
   block terms have the shape n + j = s·p^a·r^b, where:
   * s is j-smooth;
   * p is a prime with j < p ≤ K;
   * r > K is prime and r^b > exp((log n)^β).
3. **Conditional (Theorem C).** (L3) holds with k ≤ C log n under Hypothesis H*(C, β, δ), which says
   that at most (1 − δ)·π(K) block terms have that shape. This covers l = 0, and every
   l < δC/1.3841.
4. **Barrier (Proposition 3.1).** The pigeonhole-and-counting method that closed level 2 fails for
   every n with property (P): ω(n) ≤ 2, and ⌈n/p⌉ is prime for every prime p ≤ K with p ∤ n.
   * (P) occurs: n = 65 855 792 with K = 17, which is 0.94·log n.
   * (P) is heuristically infinitely frequent at K = c log n for any c < 1.
   * For every C, excluding (P) at K = C log n needs an upper bound for the simultaneous
     primality of ≍ log n/log log n integers. We know of no method that gives one.

**Gap indicator.** Put K = ⌊C log n⌋ and Y = exp((log n)^{1/3}). This single inequality would
finish it: there are C, δ > 0 such that for all large n,

    |𝒯(n)| ≤ (1 − δ)·π(K),   where   𝒯(n) := { 0 ≤ j ≤ K : n + j = s·p^a·r^b with P(s) ≤ j < p ≤ K < r, r^b > Y },

where p and r are primes, a, b ≥ 1, and P(s) denotes the largest prime factor of s, with P(1) = 1.
(The exact per-n form is Theorem C′.)

A necessary special case is: for every large n with ω(n) ≤ 2, #{p ≤ K prime : ⌈n/p⌉ is prime}
≤ π(K) − 3.

Scope and checks:
* Same-vendor work (Claude Opus); no referee yet; nothing is kernel-checked.
* External inputs are the same as for Theorem A: Matveev 2000 (E1), Rosser–Schoenfeld 1962 (E2)
  and Robin 1983 (E3), all as quoted in `../PROOF_THEOREM_A.md` §2. Theorem C (ii) also uses E2
  in the form π(K) ≥ K/log K.
* Literature statements quoted from `../G2_LEVEL3_20260925.md` are marked [G2].

Notation:
* log is natural.
* P(m) is the largest prime factor of m, with P(1) = 1. "m is x-smooth" means P(m) ≤ x.
* ω(m) is the number of distinct prime factors of m.
* Π_m(n) := ∏_{0≤i<m}(n+i), with Π_0(n) = 1.

## 0. Verdicts at a glance

| Route | Verdict | One-line reason |
|---|---|---|
| R1: counting type-0 and type-1 terms | **Partly works; needs X** | Baker (Prop. 2.3) removes type-0 terms and type-1 terms whose large prime power is ≤ exp((log n)^{β}), β < 1/2. X is a bound (1 − δ)π(K) on the rest, the set 𝒯(n) of type-1 terms carrying one huge prime. That set is invisible to linear forms (two unknown primes per pair of terms), to pigeonhole on smooth parts, and to sieves (interval shorter than the primes). |
| R2: block product / ω(Δ) | **Needs X′ ⊋ X** (strictly stronger than R1) | Under (H3), R2 is exactly σ₀ > 0, i.e. 2t₀ + t₁ < π(K) over *all* terms. Its natural all-n form X′ implies π(n + K) − π(n) ≤ (1 − δ)π(K), beyond the Brun–Titchmarsh constant 2. Counting with multiplicity cannot help (§3.2). Numerically σ₀ ≤ 0 for almost every n ≤ 10⁹. |
| R3: Luccioli, averaged f(n) | **Dead** (reduces to R2) | Luccioli's identity moves one level *down* per shift. "f(n) > 2" is exactly R2's inequality. The best known averaged bound is liminf f ≥ 10/7 (Pólya, ineffective). No known result turns dense v ≥ 2 into v ≥ 3. |
| R4: conditional | **Delivered** | Theorem C (H* ⇒ L3, effective). Proposition 3.1: the barrier (P). Remark 3.5: abc only raises Y to n^{1/2−ε}, and (P) is abc-compatible. Thue–Mahler does not apply, because the equations are linear. |
| R5: numerics | **Done** | Exhaustive to 10⁹ (l = 0, 1, 2) plus samples to 10²⁰⁰. See §4. The feasible range is pre-asymptotic for the counting quantities. |

## 1. What "v ≤ 2 on the block" forces

Fix integers n ≥ 2 and 0 ≤ l < K. The hypothesis is

  **(H3)_{l,K}:** v(n,k) ≤ 2 for every integer k with l ≤ k ≤ K.

(L3) at level l with range K is the statement that (H3)_{l,K} fails.

### 1.1 Entry positions and a counting identity

For a prime p, let e(p) = e_n(p) := min{i ≥ 0 : p | n + i}, the **entry position** of p. We have
e(p) ≤ p − 1.

**Lemma 1.1.** For every k ≥ 0 and prime p: p is counted in v(n,k) ⟺ p | n + k and p > k ⟺
e(p) = k.

*Proof.* The left-hand equivalence is Lemma 1.1 of `PROOF_THEOREM_A.md` for k ≥ 1. For k = 0 it holds
because the FC definition has an empty range and p > 0 always.

For the second equivalence:
* (⇒) If p | n + k and p > k, then p ∤ n + i for 0 ≤ i < k, since 0 < k − i < p. So e(p) = k.
* (⇐) If e(p) = k and p ≤ k, then p | n + (k − p) with 0 ≤ k − p < k. This contradicts
  minimality. So p > k. ∎

**Identity (I).** For 0 ≤ a ≤ b,

  Σ_{k=a}^{b} v(n,k) = #{p : a ≤ e(p) ≤ b} = ω(Π_{b+1}(n)) − ω(Π_a(n)).

*Proof.* By Lemma 1.1 every prime is counted at exactly one k, namely k = e(p). The primes
dividing Π_{b+1}(n) are exactly those with e(p) ≤ b. ∎

Next split v(n,j) according to the size of the prime. For l ≤ j ≤ K put:

  d_j := #{p prime : j < p ≤ K, p | n + j} = #{p ≤ K : e(p) = j},
  τ_j := #{p prime : p > K, p | n + j}   (the **type** of the term n + j).

**Lemma 1.2.** v(n,j) = d_j + τ_j for l ≤ j ≤ K.

*Proof.* By Lemma 1.1, v(n,j) counts the primes p > j that divide n + j. Such a prime lies either
in (j, K] or above K. For p ≤ K, the condition p > j with p | n + j is equivalent to e(p) = j,
again by Lemma 1.1. ∎

**Lemma 1.3 (demand).** D_l(n) := Σ_{j=l}^{K} d_j = #{p ≤ K : p ∤ Π_l(n)} = π(K) − ω_{≤K}(Π_l(n)).
In particular D_0(n) = π(K).

*Proof.* Every p ≤ K has e(p) ≤ p − 1 ≤ K − 1. So Σ_{j=l}^{K} d_j counts the p ≤ K with
e(p) ≥ l, and these are exactly the p ≤ K that divide none of n, …, n + l − 1. ∎

### 1.2 Absorption, and the two pigeonhole certificates

Put cap_j := max(0, 2 − τ_j) and J := {j ∈ [l, K] : d_j ≥ 1}. Put
t_i := #{j ∈ [l,K] : τ_j = i} for i = 0, 1, 2, and t_i^J := #{j ∈ J : τ_j = i}.

**Lemma 1.4 (absorption).** Assume (H3)_{l,K}. Then, for every j ∈ [l, K]:

* τ_j ≤ 2 and d_j ≤ cap_j;
* t₂^J = 0;
* D_l(n) = Σ_{j∈J} d_j ≤ Σ_{j∈J} cap_j = 2t₀^J + t₁^J ≤ 2t₀ + t₁.

*Proof.* By Lemma 1.2, d_j + τ_j = v(n,j) ≤ 2. This gives τ_j ≤ 2 and d_j ≤ 2 − τ_j = cap_j. If
j ∈ J then d_j ≥ 1, so τ_j ≤ 1. Sum over J. ∎

**Corollary 1.5 (certificates).** For any n, define

  σ(n) := D_l(n) − Σ_{j∈J} cap_j  and  σ₀(n) := D_l(n) − (2t₀ + t₁).

Then σ₀ ≤ σ. If σ(n) > 0 (in particular if σ₀(n) > 0), some k ∈ [l, K] has v(n,k) ≥ 3. This is the
contrapositive of Lemma 1.4.

* σ > 0 is the **R1 certificate**.
* At l = 0, σ₀ > 0 is equivalent (under (H3)) to ω(Π_{K+1}(n)) > 2(K+1). That is the **R2
  certificate**; see §3.2.
* Both lemmas hold with K replaced by any x ∈ [l, K], because (H3)_{l,K} implies (H3)_{l,x}.

### 1.3 The shape of the terms under (H3)

**Proposition 1.6.** Assume (H3)_{l,K}. Every term factors as

  n + j = s_j · ∏_{p ≤ K, e(p) = j} p^{v_p(n+j)} · R_j   (l ≤ j ≤ K),

where:
* s_j is j-smooth (s_j = 1 when j ≤ 1);
* R_j is a product of τ_j prime powers of primes > K;
* d_j + τ_j ≤ 2.

Conversely, (H3)_{l,K} holds if and only if every n + j (l ≤ j ≤ K) is a j-smooth number times at
most two prime powers of primes > j.

*Proof.* A prime q | n + j with q ≤ j goes into s_j. A prime q with j < q ≤ K has e(q) = j by
Lemma 1.1. A prime q > K goes into R_j. The count is Lemma 1.2. ∎

Consequences, and the corrections to the campaign brief:

* **Type-2 terms are not the obstruction.** A term with τ_j = 2 has d_j = 0: it holds no entry
  position and absorbs no demand. It is simply j-smooth times two large prime powers.
* The demand D_l(n) (= π(K) at l = 0) must be carried by the J-terms, and each carries:
  * type 0 (K-smooth): at most 2 units;
  * type 1 (one prime > K): exactly 1 unit.
* So the whole question is whether |J| ≥ D_l/2 terms can be of the form

    (j-smooth) × p^a × (1 or r^b),  j < p ≤ K < r,

  which is the shape of the Lemma R terms plus one free prime r.

### 1.4 Bounded ranges are impossible under Dickson, and the conjectural size of the range

**Remark 1.7 (Dickson; l = 0).** Let x ≥ 2 and M := lcm(1, …, x+1)². Put n = Mt + 1. For
0 ≤ k ≤ x:

  n + k = (k+1)·L_k(t),  L_k(t) := (M/(k+1))·t + 1.

The number M/(k+1) is divisible by every prime ≤ x + 1, so L_k(t) ≡ 1 mod each such prime. The
primes > k dividing n + k are therefore:
* k + 1 itself, when k + 1 is prime;
* the prime factors of L_k(t), all of which are > x + 1.

So v(n,k) = 1[k+1 prime] + ω(L_k(t)).

The system L_0, …, L_x is admissible:
* modulo p ≤ x + 1 every form is ≡ 1;
* for p > x + 1 there are only x + 1 < p forms.

So Dickson's conjecture gives infinitely many t with every L_k(t) prime. Each such n has
v(n,k) ≤ 2 for 0 ≤ k ≤ x. This confirms the G2 remark: a bounded range is impossible at l = 0,
conditionally.

The family has log n ≥ log M ≈ 2(x + 1), so it only reaches x ≲ (log n)/2.

*Heuristic, not a statement.* With the prime-tuple heuristic, the same family should give
k₃(n) ≥ (1 − o(1))·log n/log log n infinitely often. Here k₃(n) is the least k with v(n,k) ≥ 3.
A random-integer model gives the matching upper order: the probability that all K + 1 terms have
v ≤ 2 is exp(−(1 + o(1))·K log log n). So the natural conjecture is max_{m ≤ n} k₃(m) ≍
log n/log log n, and (L3) with k ≤ C log n is heuristically true with room for every C > 0.

## 2. The Baker step (unconditional): type-0 terms and small-prime type-1 terms

**Setting.** Let n ≥ 3, and let l, K be integers with 0 ≤ l < K, 3 ≤ K ≤ n. Let Y ≥ K be real. Put

  𝒮 = 𝒮(n; l, K, Y) := { j ∈ [l, K] : n + j = c_j·R_j, P(c_j) ≤ K,
                             R_j = 1 or R_j = r_j^{b_j} with r_j > K prime, b_j ≥ 1, R_j ≤ Y }.

So 𝒮 contains every K-smooth term (R_j = 1). No hypothesis on v is made in §§2.1–2.4.

### 2.1 The maximal-power device

**Lemma 2.1.** Assume 𝒮 ≠ ∅. For each prime p ≤ K, fix j_p ∈ 𝒮 with
v_p(n + j_p) = max_{j∈𝒮} v_p(n+j). For j ∈ 𝒮 put

  U_j := ∏_{p ≤ K, j_p = j} p^{v_p(n+j)},  W_j := ∏_{p ≤ K, j_p ≠ j} p^{v_p(n+j)}.

Then:
* n + j = U_j·W_j·R_j;
* the prime supports of the U_j are pairwise disjoint subsets of {p ≤ K};
* ∏_{j∈𝒮} W_j ≤ (K − l)!.

*Proof.* This is Lemma R(2) of `PROOF_THEOREM_A.md` with J replaced by 𝒮 and the range
{l, …, Y − 1} replaced by {l, …, K}. Fix a prime p ≤ K and j ∈ 𝒮 with j ≠ j_p. Then p^{v_p(n+j)}
divides both n + j and n + j_p, so it divides j − j_p ≠ 0. Hence

  Σ_{j ≠ j_p} v_p(n+j) ≤ Σ_{i=l, i≠j_p}^{K} v_p(|i − j_p|) = v_p((j_p − l)!·(K − j_p)!) ≤ v_p((K − l)!).

Taking the product over p ≤ K gives the bound. Disjointness holds because each p has one j_p. ∎

### 2.2 Two good terms give a small linear form

Call j ∈ 𝒮 **(t, T)-good** if ω(U_j) ≤ t and log W_j ≤ T. Here t ≥ 0 is an integer and T ≥ 1 is
real.

**Lemma 2.2.** Let C₁(·) = C₁(·, 1) be Matveev's constant (E1). If 𝒮 contains two distinct
(t,T)-good indices, then

  log n − log K < C₁(2t+3) · T · (log K)^{2t} · (log Y)² · (1 + log(log(n+K)/log 2)).   (2.1)

*Proof.* Let i ≠ j be good. Put Λ := log(n+i) − log(n+j).

*Upper bound.* Λ ≠ 0. By the mean value theorem |Λ| = |i − j|/ξ with ξ strictly between n + i and
n + j, so ξ > n. Hence |Λ| < K/n and

  −log|Λ| > log n − log K.

*Rewriting Λ.* By Lemma 2.1,

  Λ = log(W_i/W_j) + Σ_{p | U_i} v_p(n+i) log p − Σ_{p | U_j} v_p(n+j) log p + b_i log r_i − b_j log r_j.

Terms with R = 1 are omitted, and so is the W-term when W_i = W_j. This is a linear form in at
most t′ ≤ 2t + 3 logarithms of positive rationals ≠ 1. There is at least one, because Λ ≠ 0.

*Heights.* Apply E1 with 𝕂 = ℚ, D = 1, ϰ = 1, and take:

* for W_i/W_j: A = T. Its height is ≤ max(log W_i, log W_j) ≤ T, and |log(W_i/W_j)| ≤ T.
* for each p ≤ K: A = log K ≥ log p = h(p). Also log K ≥ 1, since K ≥ 3.
* for r_i and r_j: A = log Y ≥ log r ≥ 1.

*Exponents.* All coefficients have absolute value ≤ log(n+K)/log 2: v_p(n+i) ≤ log(n+K)/log 2,
and b ≤ log(n+K)/log r. So B* ≤ log(n+K)/log 2.

*Matveev.* E1 gives −log|Λ| < C₁(t′)·∏A·(1 + log B*).

Every A that can be absent is ≥ 1. So ∏A ≤ T·(log K)^{2t}·(log Y)², and C₁ is increasing in its
argument, so C₁(t′) ≤ C₁(2t+3). Combining with the lower bound on −log|Λ| gives (2.1). ∎

### 2.3 The bound

**Proposition 2.3.** Let t ≥ 0 and T ≥ 1. Suppose (2.1) fails, that is

  log n − log K ≥ C₁(2t+3)·T·(log K)^{2t}·(log Y)²·(1 + log(log(n+K)/log 2)).

Then

  |𝒮(n; l, K, Y)| ≤ 1 + π(K)/(t+1) + log((K−l)!)/T.

*Proof.* By Lemma 2.2 at most one j ∈ 𝒮 is good. The others fall into two classes:

* ω(U_j) ≥ t + 1. Since the U_j have disjoint supports among the π(K) primes ≤ K, there are at
  most π(K)/(t+1) of these.
* log W_j > T. Since every W_j ≥ 1 and ∏W_j ≤ (K−l)!, there are at most log((K−l)!)/T of these.
  ∎

**Corollary 2.4 (asymptotic form).** Fix C > 0 and 0 < β < 1/2, and put γ := (1 − 2β)/3. Put
K := ⌊C log n⌋ and Y := max(K, exp((log n)^β)). There is an effectively computable n₀(C, β) such
that for all n ≥ n₀ and all 0 ≤ l < K,

  |𝒮(n; l, K, Y)| ≤ (2/γ + o(1)) · π(K) · log log log n / log log n  =  o(π(K)).

*Proof.* Take T := (log n)^γ and t := ⌊γ·log log n / log(4096·(log K)²)⌋.

Since C₁(m) ≤ 2^{6m+20} (the second entry of Matveev's min),

  C₁(2t+3)(log K)^{2t} ≤ 2^{38}·(4096 (log K)²)^t ≤ 2^{38}(log n)^γ.

For large n, log Y = (log n)^β. So the right side of (2.1) is at most

  2^{38}·(log n)^{2γ+2β}·O(log log n) = O((log n)^{(2+2β)/3}·log log n) = o(log n),

since β < 1/2. So (2.1) fails for n ≥ n₀, and Proposition 2.3 applies.

For the three terms of that bound:
* π(K)/(t+1) ≤ π(K)·(8.32 + 2 log log K)/(γ log log n), and log log K = log log log n + o(1).
* log((K−l)!)/T ≤ K log K/(log n)^γ, which is o(π(K)/log log n). ∎

*Remarks.*

1. For the K-smooth terms alone this recovers the shape of Langevin's o(π(k)) bound [La81, (8)],
   as quoted in `PROOF_THEOREM_A.md` §7.1. The addition is the one extra prime power up to
   exp((log n)^β). We make no novelty claim: it is a routine extension of the RST/Langevin
   technique. The rate is useless at feasible n (at n = 10¹⁰⁰ the factor is about 2), so this is
   purely asymptotic.
2. **Why β < 1/2 is the limit.** Every pair of block terms that both carry a large prime gives a
   linear form with *two* unknown primes, whose heights multiply: (log r_i)(log r_j) ≤ (log Y)².
   The form must beat |Λ| < K/n, so (log Y)²·(polylog) < log n. A prime r > K divides at most one
   block term, so no linear form built from block terms can avoid two unknown primes, unless one
   of the two terms is K-smooth.
   * If the block happens to contain a good K-smooth term j₀, pairing each other good term with j₀
     leaves one unknown prime. That lifts the threshold for those terms to
     log r ≤ log n/(polylog n).
   * Nothing forces such a j₀ to exist.

### 2.4 Structure under (H3)

**Theorem 2.5.** Assume (H3)_{l,K} with K ≥ 3 and Y ≥ K. Put

  𝒯 = 𝒯(n; l, K, Y) := { j ∈ [l, K] : n + j = s·p^a·r^b, s j-smooth, p prime with j < p ≤ K, a ≥ 1,
                               r prime > K, b ≥ 1, r^b > Y }.

Then D_l(n) ≤ 2|J ∩ 𝒮| + |J ∩ 𝒯| ≤ 2|𝒮| + |𝒯|.

In particular, for l = 0, K = ⌊C log n⌋ and Y = max(K, exp((log n)^β)) with β < 1/2, and n ≥ n₀:

  |𝒯(n; 0, K, Y)| ≥ π(K)·(1 − (12/(1−2β) + o(1))·log log log n/log log n).

*Proof.* Let j ∈ J. By Lemma 1.4, τ_j ≤ 1 and d_j ≤ cap_j.

* If τ_j = 0, then n + j is K-smooth, so j ∈ 𝒮, and d_j ≤ 2.
* If τ_j = 1, then d_j = 1. By Proposition 1.6, n + j = s_j·p^a·r^b with s_j j-smooth, p the unique
  prime in (j, K] dividing n + j, and r the unique prime > K dividing n + j. Then j ∈ 𝒮 if
  r^b ≤ Y, and j ∈ 𝒯 otherwise.

Summing d_j over J gives D_l(n) ≤ 2|J ∩ 𝒮| + |J ∩ 𝒯|. The second claim uses D_0 = π(K) (Lemma 1.3) and
Corollary 2.4. ∎

So under (H3), almost all of the demand π(K) sits on terms of the form

  (j-smooth) × (one entry prime p ∈ (j, K], to some power) × (one prime power r^b > exp((log n)^β)).

Controlling these terms is the whole remaining problem.

## 3. Routes R1–R4

### 3.1 R1: counting type-0 and type-1 terms

**What works.** Type-0 terms, and type-1 terms whose large part is ≤ exp((log n)^β) with β < 1/2,
number o(π(K)) (Corollary 2.4). This is the full extent to which Lemma R's method carries over.

**What is needed (X).** A bound |𝒯(n)| ≤ (1 − δ)π(K), i.e. Hypothesis H* of Theorem C below.

**Dead ends, with reasons.**

* **(a) Equal smooth parts.** If two type-1 terms n + i = c·r_i^{b_i} and n + j = c·r_j^{b_j} share
  the K-smooth part c, then c | (j − i), so c ≤ K. This says only that j ↦ c_j is injective on the
  terms with c_j > K. It gives no count.
* **(b) Distinct smooth parts: no pigeonhole.** Any product of m distinct primes ≤ K with
  K^m ≤ n/K is a K-smooth number ≤ n/K. So there are at least binom(π(K), m) such numbers, with
  m = ⌊log(n/K)/log K⌋. For K = C log n with C ≥ 3 we have π(K)/m ≥ 2 for large n, so this count
  is at least 2^m = n^{(log 2 + o(1))/log log n}, which is ≫ K. The smooth parts therefore have
  plenty of room to be distinct.
* **(c) Fixing the smooth parts and letting the primes vary.** Two terms give c_i x − c_j y = i − j
  with x = r_i^{b_i} and y = r_j^{b_j}.
  * This equation is **linear**. With g = gcd(c_i, c_j) | (i − j), its solutions are
    (x₀ + (c_j/g)u, y₀ + (c_i/g)u), u ∈ ℤ. Infinitely many have x, y > K. Each defines
    n := c_i x − i with c_i | n + i and c_j | n + j.
  * The remaining shape conditions (x and y K-rough prime powers) are conditions on two linear
    forms in u. No Diophantine finiteness is available for them.
  * Thue–Mahler and S-unit finiteness need degree ≥ 3 or bounded prime support. Neither is
    available: the unknowns x, y are not S-units for any fixed S.
  * Requiring x, y prime turns this into a two-form Dickson problem, which is not provable either
    way.
  * More equations (more terms) only add more linear congruences n ≡ −j (mod c_j), all compatible
    by the Chinese remainder theorem.
  * So Baker/Pólya control exists only when the unknown primes are bounded, and that is
    Corollary 2.4.
* **(d) Sieve.** The block has length K + 1. A prime > K divides at most one term, so a sieve can
  only use primes ≤ K and sees only the K-rough part of each term. It cannot tell a term with one
  large prime from a term with two or more.
  * After the K-smooth parts are fixed, the event "|𝒯| ≥ (1−δ)π(K)" asks ≈ (1−δ)π(K) prescribed
    integers of size ≥ n^{1−o(1)} (namely (n+j)/(s p^a)) to be prime powers.
  * The random-model probability of that is X^{−(1−δ)C + o(1)} for n ≈ X; §3.4 has the
    computation.
  * The available sieve bounds for k simultaneous prime values carry a factor ≍ 2^k·k!, as in the
    Halberstam–Richert k-dimensional upper bound for fixed k, and even that is unproved uniformly
    in k. At k ≍ log X/log log X this factor makes the bound X^{1−o(1)} ≥ 1. No sieve bound known
    to us reaches < 1 in this regime.
* **(e) The barrier configuration (P).** This is Proposition 3.1 below. It shows that R1 in any
  form that uses only the demand/absorption data must exclude (P).

**Proposition 3.1 ((P) defeats the counting certificate).** Let K ≥ 2 and n > K². Say n has
property **(P_K)** if:

* ω(n) ≤ 2, and
* ⌈n/p⌉ is prime for every prime p ≤ K with p ∤ n.

Then σ(n) ≤ 0 at (l, K) = (0, K). That is, the R1 certificate of Corollary 1.5 fails, and a
fortiori so does the R2 certificate.

*Proof.* Let p ≤ K with p ∤ n. Then e(p) = (−n mod p) ∈ [1, p−1], and

  n + e(p) = p·⌈n/p⌉ = p·q_p,  with q_p prime and q_p ≥ n/p > K.

So τ_{e(p)} = 1 and cap_{e(p)} = 1.

The positions e(p) are distinct. Suppose e(p) = e(p′) with p ≠ p′. Then p′ | p·q_p, so p′ = q_p.
But q_p > K ≥ p′, a contradiction.

Now the position j = 0. We have d₀ = ω_{≤K}(n), and cap₀ = 2 − ω_{>K}(n) ≥ ω_{≤K}(n), because
ω(n) ≤ 2.

Hence Σ_{j∈J} cap_j ≥ #{p ≤ K : p ∤ n} + ω_{≤K}(n) = π(K) = D₀(n). ∎

**Remark 3.2 ((P) for fixed K, under Dickson).** Fix K ≥ 2. Let M := ∏_{p≤K} p² and n := Mt + 1.
For each prime p ≤ K we have p ∤ n, e(p) = p − 1, and

  ⌈n/p⌉ = (n + p − 1)/p = (M/p)·t + 1.

These π(K) forms, together with n = Mt + 1 itself, form an admissible system:
* each form is ≡ 1 modulo every prime q ≤ K;
* for q > K there are π(K) + 1 < q forms.

So Dickson's conjecture gives infinitely many t with all of them prime. Such n have ω(n) = 1 and
(P_K). Hence for bounded K, (P_K) cannot be excluded (conditionally). Any exclusion has to be
quantitative in K ≍ log n.

This rigid family has log n ≥ log M ≈ 2K, so it only reaches K ≤ (log n)/2. The examples below
(K/log n ≈ 0.94–1.12) are not of this form.

**Consequence.** Consider any proof of (L3) at range K = ⌊C log n⌋ that derives a contradiction
from (H3) using only the demand D and the per-position capacities. Such a proof must contain a
proof that (P_K) fails for all large n. Here is where things stand:

* **Examples.** (P_K) occurs at every depth we searched. `p_config_search.py` finds, as the
  smallest n > 1000 of each depth:
  * n = 110 661 = 3·36887 with K = 13 (K/log n = 1.12);
  * n = 65 855 792 = 2⁴·4115987 with K = 17 (K/log n = 0.94). This n still has v(n,6) ≥ 3.
  * No n < 10¹¹ has depth 19 (§4.4).
* **Heuristic frequency.** The number of n ≤ X with (P_K), K = C log X, should be
  X^{1 − C + o(1)}. Each of the π(K) values ⌈n/p⌉ is a prime of size about X/p, and
  (log X)^{π(K)} = X^{C(1+o(1))}. The local factors are X^{o(1)}.
  * So for C < 1, (P) should occur infinitely often. The counting route then *cannot* prove (L3)
    at any C < 1, even though (L3) is expected to hold there.
  * For C > 1, (P) should occur only finitely often, but a proof of that is a simultaneous
    primality upper bound of the kind described in (d).
* **Assessment.** We do not know how to prove, for any fixed C, the necessary lemma "for every
  large n with ω(n) ≤ 2, some prime p ≤ C log n with p ∤ n has ⌈n/p⌉ composite."

### 3.2 R2: multiplicity via the block product

* **Exact form.** At l = 0, Identity (I) with a = 0 and b = K gives

    ω(Π_{K+1}(n)) = Σ_{j=0}^{K} v(n,j) = π(K) + t₁ + 2t₂ + Σ_{i≥3} i·t_i.

  Since t₀ + t₁ + t₂ + t_{≥3} = K + 1, it follows that ω(Π_{K+1}(n)) > 2(K+1) if and only if

    π(K) + Σ_{i≥3}(i − 2)·t_i > 2t₀ + t₁.

  Under (H3) the last sum vanishes. So "R2 closes" is exactly the statement that σ₀ > 0 for every
  n satisfying (H3), and σ₀ ≤ σ, so R2 asks for more than R1.
* **The gap, quantified.** R2 needs ω(Π_{K+1}(n)) ≥ 2K + 3, i.e. ω_{>K} ≥ 2K + 3 − π(K) primes
  above K. The known lower bounds are:
  * ω ≥ K + (1 − ε)π(K) when log n ≥ (log K)^{C′} [ST92a, via G2];
  * ω ≥ K for K ≤ exp(c(log n)^{1/2}) [RST76, via G2];
  * ω ≥ k + π(k) − 1 for fixed k and n > c(k), ineffective [Pólya, via ErSe67 and G2].
  * These all give ω_{>K} ≥ (1 − o(1))K, one large prime per term. The gap is K + 3 − (1 − ε)π(K)
    primes, i.e. a factor of 2 in the large-prime count.
  * Equivalently, R2 needs 2t₀ + t₁ < π(K). A counting proof cannot know in advance that n
    satisfies (H3), so it would establish this for all large n, in the form X′: "2t₀ + t₁ ≤
    (1 − δ)π(K) for all large n".
  * Every prime in the block has τ = 1, so X′ implies π(n + K) − π(n − 1) ≤ (1 − δ)π(K) at
    K = C log n. The best unconditional bound at this scale is 2K/log K, about 2π(K)
    (Brun–Titchmarsh in the Montgomery–Vaughan form, π(x + y) − π(x) ≤ 2y/log y). We know of no
    improvement of the constant 2 at y ≍ log x.
* **Multiplicity does not help.** The only multiplicity-sensitive information is size:

    Σ_{j=0}^{K} log(K-rough part of n+j) = (K+1) log n + O(K/n) − log(K-smooth part of Π_{K+1}(n)).

  By the device of Lemma 2.1 applied to all terms, the subtracted term is
  ≤ log K! + π(K) log(n+K). So on average each term has a K-rough part of size n^{1−O(1/log K)}.
  That size is equally compatible with one, two, or ten large primes per term, and under (H3) a
  term may be r^b with b large. No count of distinct large primes follows from size.
* **Numerics (§4).** In every decade up to 10⁹, σ₀ ≤ 0 for 96.8–100% of n (C = 2, 5, 10), while
  σ ≤ 0 for fewer than 10⁻⁶ of n above 10⁸. In the random samples, σ₀ > 0 for every sampled n from
  10³⁰ on at C = 2 (7 of 540 samples still fail at 10²⁴), and from 10⁵⁰ on at C = 10 (377 of 540
  fail at 10³⁰).

**Verdict:** needs X′ = "2t₀ + t₁ ≤ (1 − δ)π(K) over all terms". This is strictly stronger than
R1's X, and it contains a Brun–Titchmarsh improvement at scale log n.

### 3.3 R3: Luccioli's inequality and averaged statements

* **Exact form of Luccioli's inequality.** For n ≥ 1 and k ≥ 0,

    v(n+1, k) = v(n, k+1) + 1[k+1 is prime and (k+1) | n+k+1].

  *Proof.* Both sides count primes dividing m = n + k + 1. The left side counts p > k and v(n,k+1)
  counts p > k + 1; they differ only at p = k + 1. ∎
* **Consequences.**
  * Since v(n+1, k−1) ≥ v(n, k): level M at level l + 1 for all n ≥ N implies level M at level l
    for all n ≥ N + 1, with the range shifted by 1.
  * Level M at level l implies level M − 1 at level l + 1.
  * So Theorem A (level 2 at l = 1) yields only level 2 at l = 0, which ErSe67 already had.
  * No shift gains a level.
* **The averaged function.** ErSe67's f(n) = max_k (1/(k+1)) Σ_{i≤k} v(n,i) equals
  max_k ω(Π_{k+1}(n))/(k+1) by Identity (I). So "f(n) > 2" is exactly R2's inequality at some K.
  * Pólya's bound, in the form quoted from the Shorey–Tijdeman survey [G2, row 4], is
    ω(Π_k(n)) ≥ k + π(k) − 1 for n > c(k), ineffectively. (It is consistent with the "≥ k − 1"
    for primes > k quoted on #890.)
  * With k = 7, which maximises (π(k) − 1)/k, it gives liminf f(n) ≥ 10/7. That is the best
    averaged statement we can extract.
  * 2 + ε would be needed.
* **Dense v ≥ 2.** Under (H3), "v(n,k) = 2 for every k in the block" is consistent with every
  constraint above: by Identity (I) it only says ω(Π) = 2(K+1). One more prime is needed, and that
  is R2 again.
  * Even the weaker statement "a positive proportion of k ≤ C log n have v(n,k) ≥ 2" reduces to
    bounding by (1 − δ)K the terms with at most one prime > k. That is the same unknown-prime
    counting problem, and we cannot prove it either.
  * Theorem A_unif guarantees a witness of v ≥ 2 in each window [l, 10 l log n] with l ≤ log n.
    These windows are nested, so they may all contain the same k, and they give no density.

**Verdict: dead.** Every averaged route reduces to R2, and Luccioli moves the wrong way.

### 3.4 R4: conditional results

**Hypothesis H*(C, β, δ)**, for C > 0, 0 < β < 1/2 and 0 < δ < 1: there is n₀ such that for every
n ≥ n₀, with K = ⌊C log n⌋ and Y = max(K, exp((log n)^β)),

  |𝒯(n; 0, K, Y)| ≤ (1 − δ)·π(K).

**Theorem C.** Assume H*(C, β, δ).

* (i) There is N₁, effectively computable from n₀, C, β and δ, such that every n ≥ N₁ has some k
  with 0 ≤ k ≤ ⌊C log n⌋ and v(n,k) ≥ 3.
* (ii) For every integer l ≥ 1 with 1.3841·l < δC there is N₁(l) such that every n ≥ N₁(l) has some
  k with l ≤ k ≤ ⌊C log n⌋ and v(n,k) ≥ 3.

*Proof.* (i) Let n ≥ n₀ satisfy (H3)_{0,K}. By Theorem 2.5 and H*,

  π(K) = D₀(n) ≤ 2|𝒮| + |𝒯| ≤ 2|𝒮| + (1 − δ)π(K).

So δπ(K) ≤ 2|𝒮(n;0,K,Y)|. By Corollary 2.4 this is false for n ≥ n₀(C, β).

(ii) Here 𝒯(n; l, K, Y) ⊆ 𝒯(n; 0, K, Y), and Corollary 2.4 holds for every l < K. By Lemma 1.3 and
Robin's bound E3, applied to each n + i with i < l (note log(n+i) ≤ log n + 1 once l ≤ n),

  D_l(n) ≥ π(K) − Σ_{i<l} ω(n+i) ≥ π(K) − 1.3841·l·(log n + 1)/log log n.

Hence δπ(K) ≤ 2|𝒮| + 1.3841·l·(log n + 1)/log log n. By E2, π(K) ≥ K/log K ≥
(C log n − 1)/log(C log n). So the right side is (1.3841·l/C + o(1))·π(K), which is < δπ(K) for
large n. ∎

**Theorem C′ (exact per-n form).** For every n, l, K and Y ≥ K with K ≥ 3: if

  |𝒯(n; l, K, Y)| < D_l(n) − 2|𝒮(n; l, K, Y)|,

then some k ∈ [l, K] has v(n,k) ≥ 3. This is immediate from Theorem 2.5. |𝒮| is bounded
unconditionally by Proposition 2.3, so **|𝒯| is the only uncontrolled quantity.** This is the
gap indicator.

**Heuristic status of H*.**

* *Typical n.* For random n, a block term lies in 𝒯 with probability O(log K·log log n/log n). So
  E|𝒯| = O(C·(log log n)²), far below π(K) ≍ C log n/log log n.
* *Adversarial n.* Choose a set of (1 − δ)π(K) positions; there are X^{o(1)} ways. Each position
  has probability O(log K/log n) of being in 𝒯, by summing 1/(c·log(n/c)) over K-smooth c. The
  union bound gives X^{1 − (1−δ)C + o(1)} exceptional n ≤ X.
* So H*(C, β, δ) is heuristically true whenever (1 − δ)C > 1, e.g. C = 10 and δ = 1/2.
* By Proposition 3.1 it is also *necessary* (in this counting framework) to exclude (P), which is
  the p·prime special case of 𝒯.

**Remark 3.5 (abc and Thue–Mahler do not close it).**

* *abc.* Let i < j be two (t,T)-good type-1 terms (U/W decomposition as in Lemma 2.1, over the set
  of all terms with τ ≤ 1). With g = gcd(n+i, n+j) | (j − i), apply abc to

    (n+i)/g + (j−i)/g = (n+j)/g.

  The radical is ≤ K^{2t+1}·e^{2T}·r_i·r_j. So abc gives r_i·r_j ≥ n^{1−ε−o(1)} when
  t = O(log log n) and T = o(log n). Hence all good type-1 terms but one have
  r ≥ n^{1/2−ε}.
  * In Theorem 2.5 this raises Y from exp((log n)^β) to n^{1/2−ε}, and does nothing else.
  * (P) is abc-compatible: its terms are p·q_p with q_p ≈ n/p. Any abc triple built from two block
    terms then has radical ≥ n^{2−o(1)}, so abc is vacuous there.
* *Thue–Mahler.* The equations c_i x − c_j y = i − j are linear (degree 1) in the unknowns, so
  Thue–Mahler finiteness and its effective (Baker) versions have nothing to act on (§3.1 (c)).

**Verdict:** a conditional theorem with a precise hypothesis is delivered (Theorem C, C′). abc and
Thue–Mahler are not enough.

## 4. R5: numerical reconnaissance

All scripts are numpy/sympy only, with no solvers. Their outputs are in `data/`. The notation
is that of §1: k₃_l(n) := min{k ≥ l : v(n,k) ≥ 3}, and t_i, σ₀, σ are as in Corollary 1.5 with
l = 0 and K = ⌊C log n⌋.

* The k₃ search is **exact, not windowed.** v(n,k) ≥ 3 forces n + k ≥ (k+1)(k+2)(k+3), so the
  search runs up to that bound. "none" means v_l(n) ≤ 2, i.e. no k ≥ l at all.
* The block statistics use the exact per-n value of K, grouped within each segment.

### 4.1 Exhaustive scan, 2 ≤ n < 10⁹ (`r5_scan.py`, 1000 segments of 10⁶, about 20 min on 5 cores)

The decades are segment-aligned: "10^d" means [2 + 10^d, 2 + 10^{d+1}), and "10^0" means
[2, 10⁶ + 2).

**k₃_0 (the target, l = 0):**

| decade | #n | mean k3 | max k3 | at n | max k3/log n | at n | #none | largest none |
|---|---|---|---|---|---|---|---|---|
| 10^0 | 1000000 | 0.514 | 70 | 612873 | 5.25 | 612873 | 2053 | 958534 |
| 10^6 | 9000000 | 0.402 | 113 | 4046876 | 7.43 | 4046876 | 56 | 9919351 |
| 10^7 | 90000000 | 0.341 | 86 | 20141151 | 5.11 | 20141151 | 2 | 14433526 |
| 10^8 | 899999998 | 0.299 | 62 | 684689751 | 3.05 | 684689751 | 0 | - |

**k₃_1 and k₃_2 (for comparison; Theorem A's level-2 statement is at l = 1):**

| decade | #n | mean k3 | max k3 | at n | max k3/log n | at n | #none | largest none |
|---|---|---|---|---|---|---|---|---|
| 10^0 | 1000000 | 1.985 | 77 | 892860 | 5.62 | 892860 | 18032 | 999856 |
| 10^6 | 9000000 | 1.709 | 163 | 9112860 | 10.17 | 9112860 | 2824 | 9998100 |
| 10^7 | 90000000 | 1.529 | 259 | 35098932 | 14.91 | 35098932 | 176 | 83689053 |
| 10^8 | 899999998 | 1.431 | 259 | 138740814 | 13.81 | 138740814 | 1 | 100458710 |

| decade | #n | mean k3 | max k3 | at n | max k3/log n | at n | #none | largest none |
|---|---|---|---|---|---|---|---|---|
| 10^0 | 1000000 | 4.227 | 87 | 889112 | 6.35 | 889112 | 61639 | 999950 |
| 10^6 | 9000000 | 3.643 | 164 | 9112859 | 10.23 | 9112859 | 17532 | 9998100 |
| 10^7 | 90000000 | 3.142 | 291 | 32175458 | 16.83 | 32175458 | 1544 | 99484560 |
| 10^8 | 899999998 | 2.890 | 262 | 138740811 | 13.97 | 138740811 | 6 | 168263225 |

**Findings.**

* **v₀(n) ≤ 2.** Below 10⁹ the n with *no* k at all having v(n,k) ≥ 3 number 2053 below 10⁶,
  56 in [10⁶, 10⁷), 2 in [10⁷, 10⁸), and none in [10⁸, 10⁹). The largest is n = 14 433 526.
  * The list contains ErSe67's four values 94491, 94492, 99387, 99741, for which they state
    V₀(n) = 2. That is consistent, since V ≥ v.
  * It also contains other n in (94000, 10⁵), e.g. 94173. Also consistent: V₀(n) > 2 does not
    force v₀(n) > 2.
* **v₁(n) ≤ 2** holds up to n = 100 458 710 (one value in [10⁸, 10⁹)). **v₂(n) ≤ 2** holds up to
  168 263 225.
* **Does k₃ look like O(log n)?** At l = 0 the per-decade maximum of k₃_0/log n *decreases*:
  7.43 (n = 4 046 876, k₃ = 113), 5.11, 3.05. At l = 1 it is flat and noisy: 10.2, 14.9, 13.8,
  with maximum k₃_1 = 259 at n = 35 098 932 and at 138 740 814.
  * So the data are consistent with O(log n), and equally consistent with the heuristic order
    log n/log log n (§1.4). They cannot tell the two apart.
  * As a finite statement: every n with 14 433 527 ≤ n < 10⁹ has some k ≤ 5.12·log n with
    v(n,k) ≥ 3. The maximum ratio is 5.1135, at n = 20 141 151. This follows from the decade maxima and the "none" list.
  * With C = 2 the range fails below 10⁹: k₃_0 = 62 > 2 log n at n = 684 689 751.
* **Why the records are large: a size effect.** At the l = 0 record n = 4 046 876 the run is
  113 consecutive terms with v ≤ 2: 62 terms with v = 1, 50 with v = 2, and one with v = 0. The
  factorisations are listed in `data/summary.md`.
  * Near n ≈ 4·10⁶, the fraction of integers with at least three distinct prime factors > k falls
    fast. Measured on [3.5·10⁶, 4.5·10⁶): 68% at k = 0, 17% at k = 10, 1.2% at k = 50, 0.13% at
    k = 100, 0.03% at k = 113. At k = 113, log n/log k ≈ 3.2.
  * So a block that survives its short initial stretch is rarely broken later. That is why the
    records sit at small n, and why k₃/log n declines as n grows.
  * The fraction of n with k₃_0 ≥ 11 (or none) is 2.1·10⁻⁴ on [3·10⁶, 5·10⁶), 1.2·10⁻⁴ on
    [9·10⁶, 1.1·10⁷), and 2.4·10⁻⁵ on [10⁸, 2·10⁸).
  * A naive independence model overestimates such long runs by orders of magnitude, so we do not
    claim a quantitative fit. The record blocks show no Dickson-type structure: the terms are
    generic numbers with one or two large prime factors.
  * The effect fades as log n/log k → ∞. In the sampled range (§4.3), the largest k₃_0 in 1040
    samples was 4 at 10¹² and 2 at 10¹⁸.

### 4.2 Block statistics and the two pigeonhole certificates (same scan)

Here t_i = #{0 ≤ j ≤ K : n + j has exactly i prime factors > K} (t3+ means ≥ 3), averaged over n.
The "frac" columns give the fraction of n in the decade with σ₀ ≤ 0 or σ ≤ 0.

K = ⌊2 log n⌋:

| decade | mean t0 | mean t1 | mean t2 | mean t3+ | frac sigma0<=0 | frac sigma<=0 | min sigma (n, K, pi(K)) | max (2t0+t1)/pi(K) | max t1 (n) | max P-frac (n) |
|---|---|---|---|---|---|---|---|---|---|---|
| 10^0 | 0.25 | 16.47 | 9.05 | 0.377 | 1.0000 | 7.17e-03 | -3 (16, 5, 3) | 4.00 (3) | 25 (381513) | 1.00 (33) |
| 10^6 | 0.08 | 17.03 | 13.03 | 1.109 | 0.9987 | 1.24e-04 | -1 (1030382, 27, 9) | 2.89 (1360996) | 29 (7559619) | 0.89 (1246141) |
| 10^7 | 0.03 | 16.80 | 16.49 | 2.522 | 0.9924 | 6.37e-06 | -1 (10551277, 32, 11) | 2.82 (55950573) | 31 (55950573) | 0.73 (62600161) |
| 10^8 | 0.01 | 16.94 | 19.36 | 4.178 | 0.9680 | 3.92e-07 | -1 (172456671, 37, 12) | 2.83 (743559420) | 34 (743559420) | 0.67 (197706601) |

K = ⌊5 log n⌋:

| decade | mean t0 | mean t1 | mean t2 | mean t3+ | frac sigma0<=0 | frac sigma<=0 | min sigma (n, K, pi(K)) | max (2t0+t1)/pi(K) | max t1 (n) | max P-frac (n) |
|---|---|---|---|---|---|---|---|---|---|---|
| 10^0 | 2.62 | 49.90 | 12.03 | 0.020 | 1.0000 | 5.13e-02 | -7 (46, 19, 8) | 4.75 (8) | 64 (678611) | 0.64 (1345) |
| 10^6 | 1.20 | 54.10 | 21.75 | 0.323 | 1.0000 | 4.55e-04 | -3 (2969445, 74, 21) | 3.48 (4626816) | 70 (9126467) | 0.48 (2860915) |
| 10^7 | 0.55 | 55.30 | 31.70 | 1.320 | 1.0000 | 3.29e-06 | -2 (11519996, 81, 22) | 3.32 (15591526) | 76 (85140998) | 0.48 (30122461) |
| 10^8 | 0.23 | 55.27 | 41.55 | 3.354 | 1.0000 | 1.11e-08 | 0 (119138048, 92, 24) | 3.21 (147867642) | 79 (655778821) | 0.46 (618049113) |

K = ⌊10 log n⌋:

| decade | mean t0 | mean t1 | mean t2 | mean t3+ | frac sigma0<=0 | frac sigma<=0 | min sigma (n, K, pi(K)) | max (2t0+t1)/pi(K) | max t1 (n) | max P-frac (n) |
|---|---|---|---|---|---|---|---|---|---|---|
| 10^0 | 11.58 | 105.27 | 11.80 | 0.000 | 1.0000 | 4.00e-01 | -15 (1654, 74, 21) | 5.92 (55) | 127 (832899) | 0.44 (18805) |
| 10^6 | 6.02 | 120.65 | 27.55 | 0.017 | 1.0000 | 1.91e-02 | -7 (1070152, 138, 33) | 4.36 (1023891) | 142 (8468666) | 0.38 (2666319) |
| 10^7 | 3.21 | 127.50 | 46.11 | 0.441 | 1.0000 | 9.15e-05 | -5 (12906393, 163, 38) | 4.05 (10671191) | 154 (74328537) | 0.37 (12102097) |
| 10^8 | 1.64 | 130.65 | 66.09 | 1.909 | 1.0000 | 6.22e-08 | -2 (127184379, 186, 42) | 3.79 (150103978) | 165 (524527756) | 0.36 (184770301) |

**Findings.**

* **This range is pre-asymptotic.** Near 10⁸–10⁹ a typical term has τ ≤ 1 at K = 10 log n: about
  130 of the ≈ 200 terms are type 1, against π(K) ≈ 45. So:
  * the R2 certificate σ₀ fails for essentially every n (96.8–100%, depending on C);
  * the R1 certificate σ fails for a fraction below 10⁻⁶ in the top decade (4·10⁻⁷, 1·10⁻⁸ and
    6·10⁻⁸ for C = 2, 5, 10), with min σ ∈ {−1, 0, −2}.
  * A failed certificate does not mean (H3) holds. At the worst n below, v(n,0) = 3 already. It
    only shows that the counting is lossy.
* **Anatomy of the worst R1 failure** (C = 10, top decade): n = 127 184 379 = 3·7·6056399,
  K = 186, π(K) = 42. The J-terms are listed below. The certificate fails (Σ cap = 44 ≥ 42),
  although v(n,0) = 3 already.
  * The mechanism: six K-smooth J-terms (τ = 0) each have capacity 2 but carry demand 1. That
    spare capacity covers the overflow at j = 0, 1, 3.
  * The other J-terms have exactly the Theorem 2.5 shape (j-smooth)·p·(one prime > K).

| j | d_j (entry primes in (j,K]) | tau_j (#primes > K) | cap_j | v(n,j) | n+j factorised |
|---|---|---|---|---|---|
| 0 | 2 [3, 7] | 1 | 1 | 3 | 3·7·6056399 |
| 1 | 2 [2, 5] | 1 | 1 | 3 | 2^2·5·6359219 |
| 3 | 3 [13, 31, 89] | 1 | 1 | 4 | 2·3^2·13·31·89·197 |
| 6 | 1 [19] | 1 | 1 | 2 | 3·5·19·446261 |
| 7 | 1 [83] | 1 | 1 | 2 | 2·7·83·109453 |
| 8 | 1 [11] | 1 | 1 | 2 | 11·11562217 |
| 9 | 1 [23] | 1 | 1 | 2 | 2^2·3·23·460813 |
| 11 | 1 [61] | 1 | 1 | 2 | 2·5·61·208499 |
| 12 | 1 [79] | 1 | 1 | 2 | 3^3·79·59627 |
| 13 | 1 [37] | 1 | 1 | 2 | 2^3·37·429677 |
| 16 | 1 [17] | 1 | 1 | 2 | 5·13·17·115099 |
| 17 | 1 [73] | 1 | 1 | 2 | 2^2·73·435563 |
| 18 | 1 [47] | 1 | 1 | 2 | 3·47·902017 |
| 21 | 1 [103] | 0 | 2 | 1 | 2^4·3^2·5^2·7^3·103 |
| 22 | 1 [29] | 1 | 1 | 2 | 29·4385669 |
| 25 | 1 [127] | 1 | 1 | 2 | 2^2·19·127·13177 |
| 31 | 1 [173] | 1 | 1 | 2 | 2·5·173·73517 |
| 32 | 1 [43] | 1 | 1 | 2 | 23·43·128599 |
| 33 | 1 [59] | 1 | 1 | 2 | 2^2·3·17·59·10567 |
| 39 | 1 [53] | 1 | 1 | 2 | 2·3^4·53·14813 |
| 40 | 1 [41] | 1 | 1 | 2 | 41·3102059 |
| 46 | 1 [67] | 1 | 1 | 2 | 5^2·67·75931 |
| 51 | 1 [71] | 0 | 2 | 1 | 2·3·5·29^2·71^2 |
| 52 | 1 [151] | 1 | 1 | 2 | 11^2·151·6961 |
| 59 | 1 [113] | 1 | 1 | 2 | 2·113·562763 |
| 65 | 2 [139, 157] | 0 | 2 | 2 | 2^2·31·47·139·157 |
| 73 | 1 [101] | 1 | 1 | 2 | 2^2·101·314813 |
| 81 | 1 [97] | 0 | 2 | 1 | 2^2·3·5·13·41^2·97 |
| 84 | 1 [149] | 1 | 1 | 2 | 3^2·7·17·149·797 |
| 91 | 1 [109] | 1 | 1 | 2 | 2·5·7·79·109·211 |
| 101 | 1 [107] | 0 | 2 | 1 | 2^5·5·17·19·23·107 |
| 115 | 1 [131] | 1 | 1 | 2 | 2·131·485437 |
| 119 | 1 [137] | 1 | 1 | 2 | 2·7^2·137·9473 |
| 120 | 1 [163] | 0 | 2 | 1 | 3^5·13^2·19·163 |
| 133 | 1 [179] | 0 | 2 | 1 | 2^7·7·13·61·179 |
| 149 | 1 [167] | 1 | 1 | 2 | 2^4·167·47599 |
| 158 | 1 [181] | 1 | 1 | 2 | 19·31·181·1193 |

### 4.3 Sampled large n (`r5_bigsample.py`)

k₃ is exact for e ≤ 18 (full factorisation). For larger e it is a certified upper bound: primes
up to 10⁴ are found by trial division, and the cofactor is classified as prime, prime power or
composite-non-prime-power. The block statistics need only τ ∈ {0, 1, ≥ 2}, so they are exact
for every e.

| e | #n | k3_0: mean / max | k3_1: mean / max | C | K | pi(K) | mean t0 | mean t1 | mean t2+ | mean t1/pi(K) | #sigma0<=0 | min sigma0 | #sigma<=0 | min sigma | mean Pcount |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 | 1040 | 0.22 / 4 | 1.26 / 6 | 2 | 55-56 | 16-16 | 0.00 | 17.2 | 39.4 | 1.076 | 718 | -14 | 0 | 6 | 0.64 |
| 12 | 1040 | 0.22 / 4 | 1.26 / 6 | 5 | 138-141 | 33-34 | 0.01 | 55.1 | 85.5 | 1.629 | 1040 | -39 | 0 | 12 | 1.41 |
| 12 | 1040 | 0.22 / 4 | 1.26 / 6 | 10 | 276-283 | 58-61 | 0.10 | 129.7 | 150.9 | 2.185 | 1040 | -97 | 0 | 21 | 2.51 |
| 15 | 1040 | 0.16 / 2 | 1.22 / 6 | 2 | 69-70 | 19-19 | 0.00 | 17.5 | 52.9 | 0.922 | 391 | -15 | 0 | 8 | 0.61 |
| 15 | 1040 | 0.16 / 2 | 1.22 / 6 | 5 | 172-176 | 39-40 | 0.00 | 54.8 | 120.3 | 1.372 | 1035 | -34 | 0 | 18 | 1.33 |
| 15 | 1040 | 0.16 / 2 | 1.22 / 6 | 10 | 345-352 | 68-70 | 0.01 | 126.6 | 223.1 | 1.825 | 1040 | -88 | 0 | 35 | 2.30 |
| 18 | 1040 | 0.13 / 2 | 1.17 / 5 | 2 | 82-84 | 22-23 | 0.00 | 18.3 | 66.0 | 0.795 | 131 | -10 | 0 | 13 | 0.63 |
| 18 | 1040 | 0.13 / 2 | 1.17 / 5 | 5 | 207-210 | 46-46 | 0.00 | 55.2 | 154.5 | 1.201 | 991 | -32 | 0 | 25 | 1.27 |
| 18 | 1040 | 0.13 / 2 | 1.17 / 5 | 10 | 414-421 | 80-82 | 0.00 | 126.7 | 292.2 | 1.573 | 1040 | -82 | 0 | 47 | 2.20 |
| 24 | 540 | 0.12 / 2 | 1.19 / 4 | 2 | 110-111 | 29-29 | 0.00 | 18.8 | 92.9 | 0.648 | 7 | -5 | 0 | 18 | 0.55 |
| 24 | 540 | 0.12 / 2 | 1.19 / 4 | 5 | 276-279 | 58-59 | 0.00 | 56.7 | 222.1 | 0.963 | 210 | -19 | 0 | 39 | 1.15 |
| 24 | 540 | 0.12 / 2 | 1.19 / 4 | 10 | 552-559 | 101-102 | 0.00 | 127.2 | 430.0 | 1.253 | 538 | -63 | 0 | 70 | 2.04 |
| 30 | 540 | 0.11 / 2 | 1.14 / 4 | 2 | 138-139 | 33-34 | 0.00 | 19.5 | 120.0 | 0.583 | 0 | 1 | 0 | 23 | 0.52 |
| 30 | 540 | 0.11 / 2 | 1.14 / 4 | 5 | 345-348 | 68-69 | 0.00 | 57.1 | 290.7 | 0.832 | 30 | -11 | 0 | 51 | 1.08 |
| 30 | 540 | 0.11 / 2 | 1.14 / 4 | 10 | 690-697 | 124-125 | 0.00 | 129.5 | 565.5 | 1.036 | 377 | -35 | 0 | 91 | 2.00 |
| 50 | 220 | 0.13 / 2 | 1.09 / 3 | 2 | 230-231 | 50-50 | 0.00 | 20.3 | 211.3 | 0.405 | 0 | 17 | 0 | 42 | 0.48 |
| 50 | 220 | 0.13 / 2 | 1.09 / 3 | 5 | 575-579 | 105-106 | 0.00 | 59.7 | 518.4 | 0.564 | 0 | 27 | 0 | 87 | 0.94 |
| 50 | 220 | 0.13 / 2 | 1.09 / 3 | 10 | 1151-1158 | 190-191 | 0.00 | 133.4 | 1022.4 | 0.699 | 0 | 28 | 0 | 159 | 1.74 |
| 100 | 80 | 0.10 / 1 | 1.09 / 3 | 2 | 460-461 | 88-89 | 0.00 | 23.4 | 438.3 | 0.264 | 0 | 54 | 0 | 81 | 0.45 |
| 100 | 80 | 0.10 / 1 | 1.09 / 3 | 5 | 1151-1154 | 190-191 | 0.00 | 66.1 | 1087.5 | 0.347 | 0 | 108 | 0 | 174 | 0.91 |
| 100 | 80 | 0.10 / 1 | 1.09 / 3 | 10 | 2302-2309 | 342-343 | 0.00 | 146.9 | 2159.7 | 0.429 | 0 | 169 | 0 | 314 | 1.75 |
| 200 | 10 | 0.00 / 0 | 1.10 / 2 | 2 | 921-922 | 157-157 | 0.00 | 23.9 | 898.6 | 0.152 | 0 | 123 | 0 | 149 | 0.90 |
| 200 | 10 | 0.00 / 0 | 1.10 / 2 | 5 | 2303-2305 | 342-342 | 0.00 | 71.5 | 2233.9 | 0.209 | 0 | 258 | 0 | 327 | 1.50 |
| 200 | 10 | 0.00 / 0 | 1.10 / 2 | 10 | 4607-4611 | 623-623 | 0.00 | 160.3 | 4450.1 | 0.257 | 0 | 439 | 0 | 596 | 2.40 |

**Findings.**

* t₁/π(K) falls steadily: at C = 10 it is 2.19 (10¹²), 1.57 (10¹⁸), 1.04 (10³⁰), 0.70 (10⁵⁰),
  0.43 (10¹⁰⁰), 0.26 (10²⁰⁰). The mean of t₁ itself grows only slowly (≈ 127 → 160), as the
  heuristic E t₁ ≍ C·(log log n)^{O(1)} predicts.
* σ₀ > 0 in every sample from 10⁵⁰ on (and from 10³⁰ at C = 2). σ > 0 in every sample from 10¹²
  on.
* The mean of Pcount = #{p ≤ K : ⌈n/p⌉ prime} stays near C/log K·O(1), about 2 at C = 10, and
  does not grow with n.
* So for *typical* n the counting certificates hold with room once n is astronomically large, as
  the heuristics say. The difficulty is entirely about exceptional n, which sampling cannot probe.

### 4.4 The barrier configuration (P) (`p_config_search.py`)

For each prime Q, the table gives the smallest n > 1000 with (P_Q): ω(n) ≤ 2, and ⌈n/p⌉ is prime
for every prime p ≤ Q with p ∤ n. By Proposition 3.1 the counting certificate fails at K = Q for
these n.

| Q | smallest n > 1000 with (P_Q) | factorisation | log n | Q/log n | π(Q) | k₃_0(n) |
|---|---|---|---|---|---|---|
| 5 | 1 125 | 3²·5³ | 7.03 | 0.71 | 3 | none (v₀(n) ≤ 2) |
| 7 | 1 225 | 5²·7² | 7.11 | 0.98 | 4 | none |
| 11 | 1 893 | 3·631 | 7.55 | 1.46 | 5 | none |
| 13 | 110 661 | 3·36887 | 11.61 | 1.12 | 6 | none |
| 17 | 65 855 792 | 2⁴·4115987 | 18.00 | 0.94 | 7 | 6 |
| 19 | none below 10¹¹ | – | – | < 0.76 would be needed | 8 | – |

* Rows Q ≤ 11 come from the v1 search (`data/p_config_partial_v1.log`). Rows Q ≥ 13 were
  reproduced by the v2 search (`data/p_config_1e11.log`), which covered all n < 10¹¹ in 41 min.
* Direct check at n = 110 661 (K = 13) and n = 65 855 792 (K = 17): σ = 0 at l = 0, as
  Proposition 3.1 predicts. Every J-term is (entry prime)·(one prime > K).
  * For n = 65 855 792 the values ⌈n/p⌉ for p = 3, 5, …, 17 are all prime: 21951931, 13171159,
    9407971, 5986891, 5065831, 3873871.
  * p = 2 divides n and is absorbed at j = 0.

**Reading.**

* In the searchable range, (P) is realised with K/log n between 0.94 and 1.12, near the heuristic
  threshold C = 1 of §3.1.
* Depth 19 does not occur below 10¹¹. Any example would have Q/log n < 0.76.
* So (P) is a real, not merely hypothetical, obstruction to the counting route at C ≈ 1. Whether
  it persists at every fixed C < 1 (the heuristic says yes) or dies out is not decided by this
  data.
* For n > 10⁶ in the table, level 3 still holds, at k = 6. The small n (≤ 1.1·10⁵) are among the
  v₀(n) ≤ 2 exceptions anyway.

### 4.5 Independent re-check (`r5_recheck.py`)

The re-check uses a different code path. It factorises with sympy and evaluates v(n,k) from the
Formal Conjectures definition (p | n + k and p ∤ n + i for all i < k), not from Lemma 1.1. It
recomputes:

* k₃_0, k₃_1, k₃_2 exactly, with a search to the cube-root bound;
* for C = 2, 5, 10: K, π(K), t₀…t₃, σ₀, σ and Pcount.

It compares these with the scan code on a sample. The sample consists of the per-segment record
holders, every extremal n stored by the scan, random "none" n for each l, random n, and random
large-n rows with e ≤ 18 from §4.3.

Result (`data/recheck.log`): **PASS**.

* 19 012 values of n up to 10⁹ were checked, giving 57 036 k₃ comparisons (three values of l) and
  57 036 block-statistic comparisons (three values of C, each covering K, π(K), t₀…t₃, σ₀, σ and
  Pcount). There were 0 mismatches.
* 40 sampled rows with n ∈ [10¹², 2·10¹⁸] were re-derived from full factorisations, with
  0 mismatches.
* The k₃ = −1 ("none") values were re-checked all the way to the cube-root bound, so the v_l(n) ≤ 2
  lists are independently confirmed on the sample.

Separately, the four ErSe67 values with V₀(n) = 2 appear in our v₀(n) ≤ 2 list, as they must.

## 5. The gap, stated once

* **Needed (sufficient).** For some C, δ > 0 and all large n, |𝒯(n; 0, ⌊C log n⌋, exp((log n)^{1/3}))|
  ≤ (1 − δ)π(⌊C log n⌋). This is H*(C, 1/3, δ), and it gives (L3) by Theorem C.
  * Per n, the requirement is exactly |𝒯| < π(K) − 2|𝒮| (Theorem C′). The Baker step has already
    made |𝒮| = o(π(K)).
* **Necessary for the counting method.** ¬(P_K) for all large n (Proposition 3.1). This requires
  showing that the ≈ π(K) numbers ⌈n/p⌉ (p ≤ K) are not all prime.
* **What would not help.**
  * Longer linear forms (more logarithms): the obstruction is two unknown primes per pair of
    terms, not the number of known ones.
  * Sharper Matveev constants, and abc (Remark 3.5): these only move Y.
  * Larger k-ranges: heuristically, for K ≥ exp(c√log n) even typical n have t₁ ≫ π(K), because
    t₁/π(K) ≈ (log K)²·log(log n/log K)/log n. So the counting inequality fails outright.
  * The sieve/short-interval route with K = n^θ: it needs integers with three prime factors
    > n^θ in *every* interval of length n^θ ≤ n^{1/3}, and all-interval Type II estimates stop at
    lengths ≈ n^{1/2}. This is our assessment, consistent with G2 §5(c).
* **Where a new idea would have to enter.** Some input that sees primality of ≈ log n/log log n
  unrelated integers of size ≈ n, or a way to use the type-2 terms (which carry no demand, but
  whose shape "(j-smooth)·(two prime powers > j)" is itself restrictive). This round found no
  handle on either.

## 6. Files, reproduction and cost

All paths are relative to `problems/erdos889/level3/`. Python 3.12 with numpy 2.5.3, sympy 1.14.0 and
mpmath 1.3.0; run with `export PATH="$HOME/.local/bin:$PATH"`. No SAT/ILP or other solvers.

| File | Role |
|---|---|
| `ROUND1.md` | this report |
| `r5_scan.py` | exhaustive segmented scan (k₃ for l = 0, 1, 2; block statistics for C = 2, 5, 10) |
| `r5_bigsample.py` | sampled large n, 10¹²–10²⁰⁰ |
| `r5_recheck.py` | independent re-check (sympy, FC definition of v) |
| `p_config_search.py` | search for the barrier configuration (P_Q) |
| `summarize.py` | builds `data/summary.md` from the raw outputs |
| `data/scan_2_1e9.jsonl`, `.log` | raw scan output, one JSON line per 10⁶-segment |
| `data/bigsample.jsonl`, `data/bigsample_B.jsonl`, `.log` | raw large-n samples (seeds 7–10 and 17–20) |
| `data/p_config_1e11.log` | (P) search output, v2 (depths ≥ 13), n < 10¹¹ |
| `data/p_config_partial_v1.log` | (P) search v1 (all depths ≥ 5), stopped at about 10⁹ because it was too slow; superseded by v2 |
| `data/recheck.log` | re-check output (PASS) |
| `data/summary.md` | all tables, including full factorisation listings for the record holders |

Reproduction:

```
python3 r5_scan.py --lo 2 --hi 1000000000 --seg 1000000 --workers 5 --out data/scan_2_1e9.jsonl
python3 r5_bigsample.py --exps 12 15 18 --per 40 --seed 7 --out data/bigsample.jsonl      # and the other runs listed in data/*.log
python3 r5_bigsample.py --exps 12 15 18 --per 1000 --seed 17 --out data/bigsample_B.jsonl
python3 p_config_search.py --lo 1000 --hi 100000000000 --seg 10000000
python3 r5_recheck.py data/scan_2_1e9.jsonl --nrand 400 --nnone 40 --seed 2026 --big data/bigsample.jsonl data/bigsample_B.jsonl --nbig 40
python3 summarize.py data/scan_2_1e9.jsonl --big data/bigsample.jsonl data/bigsample_B.jsonl --out data/summary.md
```

The exact large-n runs were:
* `--exps 12 15 18 --per 40 --seed 7`, `--exps 24 30 --per 40 --seed 8`, `--exps 50 100 --per 20 --seed 9`
  and `--exps 200 --per 10 --seed 10`, all into `bigsample.jsonl`;
* `--exps 12 15 18 --per 1000 --seed 17`, `--exps 24 30 --per 500 --seed 18`, `--exps 50 --per 200 --seed 19`
  and `--exps 100 --per 60 --seed 20`, all into `bigsample_B.jsonl`.

**Cost.**
* About 1 hour of wall time for the analysis and write-up.
* About 3 CPU-hours of computation on this container:
  * scan: 20 min × 5 cores;
  * (P) search: about 20 min (v1) plus about 45 min (v2) on one core;
  * re-check: 8 min;
  * samples: 5 min.
* No paid resources.
* Peak memory about 2.5 GB (5 scan workers).

SHA-256 of the scripts as used for the final data. (`r5_scan.py` differs from the version
that produced segments ≥ 10⁷ + 2 only in no longer truncating the stored "none" lists; the
ten lowest segments were regenerated with it, and the shared fields were checked identical.)

```
7b96a321940b0d12c9b953b8e45ceddd65cf0012789c018735b8f4388429d567  r5_scan.py
8f95f584ad6617c569cbfddef366b8119d9776ed559877086a02f20bb0156606  r5_bigsample.py
4852c8eb4468960616f94f986875850d4eb4b17aea642df44582a2fb599b70e8  r5_recheck.py
8b1f8f27d6f04808fc7682cf0af2b0650aed761b0b34a72d51109c5ccd717089  p_config_search.py
630c4ad1f52cb8b1b12319ed0adfcc5a4382ed1ab5cb5db65e3aea65f020a7d1  summarize.py
```
