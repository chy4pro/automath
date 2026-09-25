# Erdős #889, Theorem A: external inputs and referee attack points

This is the companion to `PROOF_THEOREM_A.md`, dated 2026-09-25. Same-vendor work, not yet
refereed.

Script: `n0_compute.py`, sha256 `997fc1afb6c1ab848a09e7385523b604e7430d9ff65d27d81fe6976677f6de57`.

Reproduce with:

```
export PATH="$HOME/.local/bin:$PATH"
python3 n0_compute.py --check
```

Tested with Python 3.12.14 and mpmath 1.3.0. It takes about 5 s on one core, and two runs gave
identical output.

## A. External theorems used

Only E1–E3 are used in the proof. E4 appears only in Remark 7.1.

### E1. Matveev 2000, Corollary 2.3

**Source.** E. M. Matveev, Izv. Ross. Akad. Nauk Ser. Mat. 64:6 (2000) 125–180; English
translation in Izv. Math. 64:6 (2000) 1217–1269. mathnet.ru id `im314`.

**Setting (§2).**

* 𝕂 ⊂ ℂ is a number field of degree D.
* ϰ = 1 if 𝕂 ⊆ ℝ, and ϰ = 2 otherwise.
* α_j ∈ 𝕂*, with absolute logarithmic height h.
* ln α_j are arbitrary fixed **nonzero** values of the logarithm.
* b_j ∈ ℤ, and Λ = Σ b_j ln α_j (1.1).
* B = max{1, max_j |b_j| A_j/A_n} (1.3), and B* = max_j |b_j| (1.4).
* A_j ≥ max{D h(α_j), |ln α_j|, 0.16} (2.4), and Ω = ∏ A_j.

**Statement.** If Λ ≠ 0, the A_j satisfy (2.4) and B is given by (1.3), then

  ln|Λ| > −C₁(n) D² Ω ln(eD) ln(eB),  C₁(n,ϰ) = min{(1/ϰ)(en/2)^ϰ 30^{n+3} n^{3.5}, 2^{6n+20}}.

Moreover, B may be replaced by B*.

**Where applied.**

* Proposition B, Case 1: t = 3, α = (q₁, q₂, W₁/W₂), b = (e₁, −e₂, 1), with B*.
* Proposition B, Case 2: t = 2, used when W₁ = W₂, because then ln α₃ = 0 is not an admissible
  "nonzero value".
* Remark 7.2: with B from (1.3), with α₃ ordered last.
* In all cases 𝕂 = ℚ, D = 1 and ϰ = 1.

**How verified.**

* The Russian original PDF (`getFT.phtml?jrnid=im&paperid=314&what=fullt`, 56 scanned pages) was
  rendered locally.
* Pages 125, 126 and 127 were read visually: (1.1)–(1.4), the first paragraph of §2, (2.1)–(2.6),
  Theorems 2.1–2.2, Corollary 2.3 and Remark 2.1.
* The English translation (Izv. Math. 64:6, 1217–1269) was compared by the same-vendor referee
  (`REFEREE_CLAUDE_20260925.md`), using the text layer decoded through the embedded Type 1 font
  encodings. On p. 1219, (2.1), (2.4), (2.6), "arbitrary fixed non-zero values of the
  logarithms" and "where B may be replaced by B* (see (1.4))" agree with the Russian.
* §5 defines h(α) = D⁻¹ Σ_σ max{0, ln|α|_σ}. For a/b in lowest terms this gives
  log max(|a|,|b|).

### E2. Rosser–Schoenfeld 1962

**Source.** Illinois J. Math. 6 (1962) 64–94, p. 69.

**Statements.**

* Corollary 1, (3.5): x/log x < π(x) for 17 ≤ x. Here x is real.
* Theorem 2, (3.3): x/(log x − 1/2) < π(x) for 67 ≤ x.

**Where applied.** (3.5) in §5 S1 with x = y = 10·l·log n ≥ 67. (3.3) only in Remark 7.2.

**How verified.** Project Euclid scan, p. 69 read visually.

### E3. Robin 1983

**Source.** Acta Arith. 42 (1983) 367–389, p. 369.

**Statements.**

* Théorème 11: ω(n) ≤ 1,3841 log n/log log n for n ≥ 3.
* Théorème 13: ω(n) ≤ log n/(log log n − 1,1714) for n ≥ 26.

**Where applied.** Théorème 11 in §5 S2 and §6, to each n + i with 0 ≤ i < l. Théorème 13 only in
Remark 7.2.

**How verified.** matwbn.icm.edu.pl scan `aa4242.pdf`, p. 369 read visually.

### E4. Langevin 1981, Corollaire 1 (8): remark only

**Source.** Acta Arith. 39 (1981) 241–249.

**Where applied.** Remark 7.1 only, as the alternative qualitative route.

**How verified.** The statement was read from the G2 gate's crop of the matwbn scan
(`scratchpad/g2/aa/crop_cor1.png`, `crop_th1.png`). Langevin's proof and the dependence of C and c
on t₁, …, t₆ were **not** checked.

### Elementary facts used without citation

* The mean value theorem.
* a!·b! divides (a+b)!.
* log M! ≤ (M+1) log M − M + 1, proved in S3.
* Monotonicity of the explicit one-variable functions listed in B.9.

## B. Points a referee should attack

They are ordered by our estimate of risk.

**B.1 Matveev transcription and use.**

* Check (2.6) against the English translation. In particular check (en/2)^ϰ/ϰ with ϰ = 1, and
  n^{3.5} rather than n^{4.5}.
* Check the replacement clause "B may be replaced by B*".
* Check the standing requirement that the ln α_j be nonzero (the reason for the Case 2 split).
* The simplified 1.4·30^{t+3}t^{4.5} form is weaker, so it is safe. Using it gives ℓ₁ = 45.31
  instead of 45.28 (Appendix A).

**B.2 Lemma R(2), the product bound.**

* For j ≠ j_p, p^{v_p(n+j)} | (j − j_p) because v_p(n+j) ≤ v_p(n+j_p).
* The summation runs over a subset of {l, …, Y−1}∖{j_p}.
* The identity ∏_{i≠j_p}|i − j_p| = (j_p − l)!(Y−1−j_p)!, which divides (Y−l−1)!.
* Check the exact factorial: the index range has Y − l elements.

**B.3 Lemma R(3), the counting.**

* The direction of the elimination giving |J₁| ≥ π(y) − 2ω_{l,y}(n) − 2|J₀|.
* That Σ s(j) ≤ π(Y) needs each prime to have exactly one j_p.

**B.4 Lemma R(1).**

* A prime p ≤ l always divides Π_l(n), so it is excluded.
* k₀(p) ≤ p − 1 ≤ Y − 1 < y, so (H) applies at k₀(p).
* Lemma 1.1 needs k₀(p) ≥ 1, which holds since l ≥ 1.

**B.5 Lemma R(5), the pigeonhole.** It uses Σ over all of J (including J₀) as the budget, and
m − 1 ≥ A − 1 > 0.

**B.6 Proposition B.**

* |j₁ − j₂| ≤ Y − 1 − l, and ξ > n.
* The height of W₁/W₂ is bounded by log max(W₁, W₂), and |log(W₁/W₂)| by the same quantity.
* A₁ = log q_i is ≥ 0.16 because q_i ≥ 2.
* The case W₁ = W₂.
* The claim C₁(2) ≤ 0.16·C₁(3), which is certified.

**B.7 §5 S2.**

* The ω bound for n + i uses only log(n+i) ≤ L + 1 and log log(n+i) ≥ ℓ. No monotonicity of
  log x/log log x is needed.
* ω_{l,y}(n) ≤ Σ_{i<l} ω(n+i).

**B.8 §5 S3.** The bound G(M) ≥ log M!, G increasing, and M = Y − l − 1 ≤ y − l − 1.

**B.9 §5 S4–S6, monotone replacements.** Each constant in (5.1) is evaluated at ℓ₁ and must bound
the ℓ-dependent quantity for **every** ℓ ≥ ℓ₁. The quantities are:

* m/ℓ;
* (1 − log log 2 + e^{−ℓ})/ℓ;
* (ℓ + m − 1)/(ℓ − μ), decreasing because m − 1 + μ > 0;
* ℓ²e^{−ℓ}, decreasing for ℓ ≥ 2;
* ℓ/(ℓ − μ) ≤ 1/(1 − μ/ℓ₁);
* 3e^{−ℓ}/(c(ℓ + m − 1)).

The same list applies to (6.1) and to Remark 7.2.

**B.10 §5 S7.** ψ(ℓ) = ℓ − 5 log ℓ is increasing for ℓ > 5. The final certificate is
φ(45.28) = 0.0072 > 0.

**B.11 The script.**

* Check that every inequality used in the proof is either certified by the script or proved by
  hand. The script's side-condition lists are in `fixed_l`, `uniform` and `refined`.
* Decimal constants ('1.3841', '1.1714', '45.28') enter as intervals that enclose them.
* The min in C₁ is formed from endpoints.
* `search` only finds the least grid point. The proof needs only the certificate at the stated ℓ₁.
* `direct_R` is a consistency check, not part of the proof.

**B.12 Uniform version (§6).**

* a(ℓ) is decreasing in m, and m ranges over [log c, ℓ + log c] when 1 ≤ l ≤ log n.
* Each worst case is taken in the correct direction.
* Y ≤ c(log n)² < n.

**B.13 Pinning.**

* FC `v` uses `range k` (0 ≤ i < k) and `primeFactors`; Lemma 1.1 converts this.
* `v_l 1 n` is a sup in ℕ∞.
* Theorem A uses the natural log, and n ≥ N0 is equivalent to log log n ≥ 45.28.
* Corollary A1 gives `v1_eq_1_finite` with answer "yes". Nothing about `erdos_889`,
  `V1_eq_1_finite` or `v0_gt_1` is claimed.

**B.14 Novelty and priority.**

* The qualitative statement follows from Langevin 1981 and Lemma R(1) (§7.1).
* The G2 search was single-pass and same-vendor, without web search. Guy B27, Er98 p. 178,
  Shorey–Tijdeman 1986, Erdős 1976 (Publ. Math. Debrecen 23) and the Tijdeman result cited by
  Langevin (MR 54, 1977) were not obtained.
* The brief's "Tijdeman 1974" could not be matched to a checked paper. The proof cites Tijdeman,
  Compositio 26 (1973) 319–330, which is the paper the G2 gate read.

## C. Not justified, or open

* Langevin's hypotheses and constants (Remark 7.1) were not refereed. The estimate
  "log log N0 at least of order 10⁶" for that route is ours and rough.
* Novelty, as in B.14.
* No independent (cross-vendor or human) review, and no formalisation. A Lean proof would need
  Matveev's theorem as a hypothesis. Lemma R and §5 are elementary and could be formalised
  unconditionally.
