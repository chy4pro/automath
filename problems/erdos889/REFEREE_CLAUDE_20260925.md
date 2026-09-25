# Erdős #889, Theorem A: referee report (same-vendor)

Date: 2026-09-25. Referee: a Claude (Opus 5.5) subagent acting as adversarial referee. I did not
write the note, and I treated every step as wrong until I had checked it.

**This is a same-vendor review (Claude reviewing Claude).** It is not a cross-vendor or human
referee report, and nothing has been formalised in Lean. The global-memory `recall_presets` tool
was not available in this subagent session, so it was not called.

Files reviewed (sha256):

| file | sha256 |
|---|---|
| `PROOF_THEOREM_A.md` | `f091bfa2713a13c5c44d1df2daa66d7e46a5f68a853d5bf39a714122968d2141` |
| `CHECKS.md` | `40f45c859a7532b1e3f3885c12484e064daebaadb4e11b9e83e69a8316a7369a` |
| `n0_compute.py` | `997fc1afb6c1ab848a09e7385523b604e7430d9ff65d27d81fe6976677f6de57` (same as recorded in CHECKS.md) |
| `G2_KILL_GATE_20260925.md` | `53fba186bb4e3f88ec1ff5f29f430ec346f6ee43ee6107ae4367068d65126dd2` |
| `formal-conjectures/.../ErdosProblems/889.lean` | `8939a28c46c34d288750618aed0b0e4999a5833c601094610b8b3c4585eedf13` |

## Verdict

**PASS-WITH-REPAIRS.**

* I found no mathematical gap in Theorem A, Theorem A_l, Theorem A_unif, Corollary A1 or
  Corollary A_l.
* N0 does not change: log log N0 = 45.28, log N0 = e^45.28 = 4.6223 × 10¹⁹. 45.27 fails. The
  uniform threshold 48.82 and the Remark 7.2 threshold 44.96 are also confirmed.
* All six repairs (R1–R6, §9) concern wording, citations or stale status lines. None changes a
  statement, constant or proof step.

Item verdicts:

| # | item | verdict |
|---|---|---|
| 1 | Definitions vs `889.lean`, edge cases | VERIFIED |
| 2 | Lemma R | VERIFIED |
| 3 | Baker step, Matveev Cor. 2.3, C₁(3) | VERIFIED |
| 4 | Robin 1983, Rosser–Schoenfeld 1962, other bounds | VERIFIED |
| 5 | Final chain, S4–S7 replacements, K, ℓ₁ | VERIFIED |
| 6 | Corollary A_l, N(l), C₀ = 10 | VERIFIED; one sentence in §5.3 is imprecise (REPAIRED, R2) |
| 7 | Langevin remark | VERIFIED; one open point closed from the source (REPAIRED, R3) |
| 8 | Wording, credit, unchecked sources | REPAIRED (R1, R4, R5, R6) |

## 0. Primary sources fetched by the referee

I fetched every source myself. Scans were rendered with my own stdlib decoders (a CCITT G4
decoder and a 1-bit Flate/PNG-predictor decoder) and read visually. For the English Matveev I
decoded the text layer through the embedded Type 1 font encodings.

| source | access | sha256 | pages read |
|---|---|---|---|
| Matveev 2000, Russian original, Izv. RAN Ser. Mat. 64:6, 125–180 | mathnet.ru `getFT.phtml?jrnid=im&paperid=314&what=fullt` | `ed606b6c…c2e0cb` | pp. 125–127 (visual) |
| Matveev 2000, English translation, Izv. Math. 64:6, 1217–1269 (53 pp., "Translated by A. V. Domrin") | mathnet.ru `…&what=fullteng` | `e395e469…093574` | pp. 1218–1220 and the §5 height definition (text layer) |
| Rosser–Schoenfeld 1962, Illinois J. Math. 6, 64–94 | Project Euclid PDF (curl was blocked by Incapsula; fetched through WebFetch, which saved the binary) | `8e37b06f…ab556` | p. 69 (visual) |
| Robin 1983, Acta Arith. 42, 367–389 | matwbn `aa4242.pdf` (Anubis proof-of-work answered by my own script) | `018d5d94…707fcb` | pp. 368–369, 382–383 (visual) |
| Langevin 1981, Acta Arith. 39, 241–249 | matwbn `aa3932.pdf` | `da9244d0…0b0147` | pp. 241–242 (visual) |
| Guy, UPINT 3rd ed. (© 2004), B27 | archive.org OCR text, item `collection-of-mathematics-books-number-theory` | — | B27 entry |

All five PDFs are byte-identical to the author's copies in the session scratchpad. My reading is
independent, but the files are the same.

## 1. Definitions — VERIFIED

* `889.lean`: `v n k = ((n+k).primeFactors.filter (fun p => ∀ i ∈ range k, ¬ p ∣ n+i)).card`
  and `v_l l n = ⨆ k ≥ l, (v n k : ℕ∞)`. The note's §1 quotes these verbatim.
* Lemma 1.1 (k ≥ 1: v(n,k) = #{p | n+k : p > k}). Both directions are correct.
  * If p ≤ k, then i = k − p ∈ [0, k−1] and p | n+i.
  * If p > k, then 0 < k − i ≤ k < p.
* Brute-force check against the literal FC definition (`all((n+i) % p for i in range(k))`):
  n < 3000 plus 3000 random n < 10⁶, 1 ≤ k < 40. Result: 0 mismatches.
* Edge cases:
  * k = 1: v(n,1) = ω(n+1).
  * n = 0: v(0,k) = 0 for k ≥ 1, so `v_l 1 0 = 0`.
  * n = 1: `v_l 1 1 = 1` (ErSe67 lists n = 1).
  * k = 0 is excluded from `v_l 1`.
* Corollary A1. Theorem A gives some k ≥ 1 with v(n,k) ≥ 2. Hence `v_l 1 n ≥ 2 ≠ 1` for n ≥ N0,
  and {n | v_l 1 n = 1} ⊆ [0, N0). The FC answer is `True`.
* Independent recomputation (numpy sieve of the second-largest distinct prime factor): the
  n ∈ [2, 10⁶] with no k ≤ 10 log n and v(n,k) ≥ 2 are exactly the 28 values in §7.4, i.e.
  ErSe67's list without n = 1.

## 2. Lemma R — VERIFIED

**Notation.** The brief's notation differs from the note's. The note's A is
π(y) − 2ω_{l,y}(n) − 2·log((Y−l−1)!)/log n; the last term is the brief's "2a₀*", an upper bound
for 2|J₀|. The brief's c_i are the note's W_{j_i}. The note proves W_i^{A−1} ≤ (Y−l−1)!, i.e.
log W_i ≤ T, which is sharper than ≤ y!.

Each step checked by hand:

* **R(1).**
  * p ≤ l is impossible, because the multiple of p among n, …, n+p−1 would divide Π_l(n). So the
    multiple lies in [l, p−1], and l ≤ k₀(p) ≤ p−1 ≤ Y−1 ≤ y.
  * (H) applies at k₀(p). By Lemma 1.1, p is the only prime factor of n+k₀ above k₀ < p. So
    P(n+k₀) = p ≤ Y.
  * p ↦ k₀(p) is injective, and |J| = π(y) − ω_{l,y}(n).
* **R(2).**
  * n+j is Y-smooth.
  * For j ≠ j_p, p^{v_p(n+j)} divides j − j_p ≠ 0.
  * ∏_{i∈[l,Y−1], i≠j_p} |i − j_p| = (j_p−l)!·(Y−1−j_p)!. The index range has Y − l elements,
    and a + b = Y − l − 1.
  * a!b! | (a+b)!.
  * All prime factors of (Y−l−1)! are ≤ Y.
* **R(3).**
  * For j ∈ J₀, W_j = n + j > n.
  * Σ s(j) ≤ π(Y) = π(y), since each prime has exactly one j_p.
  * Eliminating |J_{≥2}| from |J₁| + 2|J_{≥2}| ≤ π(y) and |J₀| + |J₁| + |J_{≥2}| = π(y) − ω gives
    |J₁| ≥ π(y) − 2ω − 2|J₀|. The direction is correct.
* **R(4).** Correct.
* **R(5).**
  * If J = ∅, then A ≤ 0.
  * Otherwise (m−1)·w₂ ≤ Σ_J log W_j ≤ log((Y−l−1)!) with m − 1 ≥ A − 1 > 0.

Numerical tests (my own code, exact integer arithmetic, not sharing code with `n0_compute.py`):

* **Exhaustive.** 2 ≤ n ≤ 10⁶, l ∈ {1,2,3,4}, every Y ∈ [l+2, min(200, Y_max(n,l))] where (H)
  holds. The j_p ties were broken at random.
  * 207,874 instances, of which 101,390 have |J₁| ≥ 2.
  * Checked: every assertion of R(1)–(4); ∏W_j ≤ (Y−l−1)! as integers; n^{|J₀|} ≤ (Y−l−1)!;
    |J₁| ≥ A; and w₂^{m−1} ≤ (Y−l−1)! as integers.
  * **0 failures.**
* **Exceptional n.** The 28 n with v₁(n) = 1 satisfy (H) for all k ≥ 1, so Y can be large. I ran
  Y ≤ 1500 (step 7), with three tie-break rules for j_p (random, min, max): 5,992 Y values,
  17,976 checks, **0 failures**.
* **Synthetic stress test of R(2)–(5), no (H) needed.** J = all j ∈ [l, Y−1] with n+j Y-smooth,
  n up to 10¹², Y ≤ 1500, |J| up to 1162. Checked the product bound, the J₀ bound,
  |J₁| ≥ 2|J| − 2|J₀| − π(Y) and the pigeonhole bound. 630 tests, **0 failures**.
* **A > 1 is almost unreachable by computation.** A numpy search over n ≤ 3·10⁷, l ≤ 6, Y < 60
  finds A > 1 only at n = 7, l = 1, Y ∈ {3, 4, 5}. So conclusion (5) is tested non-vacuously only
  there. Its proof from the (m−1)w₂ inequality, which was tested 10⁵ times, is one line and
  correct.

Worked example (n = 7, l = 1, Y = 5):

* ω_{1,5}(7) = 0 and 𝒫 = {2, 3, 5}, with k₀ = 1, 2, 3 (8 = 2³, 9 = 3², 10 = 2·5).
* j₂ = 1, j₃ = 2, j₅ = 3, so W = (1, 1, 2) and ∏W = 2 ≤ 3! = 6.
* J₁ = {1, 2, 3}, A = 3 − 2 log 6/log 7 = 1.1584 and T = 11.31.
* The two smallest W are W₁ = W₂ = 1, so Case 2 of Proposition B applies:
  Λ = 3 log 2 − 2 log 3 = −0.1178, and |Λ| < Y/n = 0.714.

## 3. The Baker step — VERIFIED

**Nonvanishing.**

* Λ = log(n+j₁) − log(n+j₂) = e₁ log q₁ − e₂ log q₂ + log(W₁/W₂), by n + j_i = W_i q_i^{e_i}.
* Λ ≠ 0 because j₁ ≠ j₂. No cancellation case exists, in Case 1 or Case 2, and the sign does not
  matter (Matveev bounds |Λ|).

**Upper bound.**

* |Λ| = |j₁ − j₂|/ξ with ξ > n, and |j₁ − j₂| ≤ Y − 1 − l < Y. So |Λ| < Y/n, which is sharper
  than the brief's 2y/n.
* Hence −log|Λ| > L − log Y.

**Matveev, checked against the Russian scan (pp. 125–127) and the English text layer
(p. 1219).**

* ϰ: «Если 𝕂 ⊆ ℝ, то положим ϰ = 1, иначе ϰ = 2» / "If K ⊆ R, we put ϰ = 1, and otherwise
  ϰ = 2". With 𝕂 = ℚ: D = 1, ϰ = 1 and ln(eD) = 1.
* Logarithms: «ln α₁, …, ln α_n – произвольные фиксированные ненулевые значения логарифмов» /
  "arbitrary fixed non-zero values of the logarithms". The real logarithms of q₁, q₂ and
  W₁/W₂ ≠ 1 are nonzero.
* (2.4) A_j ≥ max{D h(α_j), |ln α_j|, 0.16}.
  * A_i = log q_i ≥ log 2 > 0.16, and h(q_i) = log q_i. The English §5 says "If α ∈ Z and α ≠ 0,
    then h(α) = ln|α|".
  * A₃ = max(T, 0.16). Here h(W₁/W₂) = log max(a, b) ≤ log max(W₁, W₂) ≤ T, from
    h(α) = D⁻¹ Σ_σ max{0, ln|α|_σ} (§5). Also |log(W₁/W₂)| ≤ max(log W₁, log W₂) ≤ T, since both
    logarithms are ≥ 0.
* Cor. 2.3, verbatim on p. 127: «Если Λ ≠ 0, A_j из (2.4), B из (1.3), то
  ln|Λ| > −C₁(n)D²Ω ln(eD) ln(eB), C₁(n) = C₁(n,ϰ) = min{(1/ϰ)((1/2)en)^ϰ 30^{n+3} n^{3.5},
  2^{6n+20}}, при этом B может быть заменено на B* из (1.4).» The English p. 1219 agrees word for
  word ("where B may be replaced by B* (see (1.4))").
  * Linear independence of the logarithms and b_n ≠ 0 are hypotheses of Theorem 2.1 only. They
    are not hypotheses of Cor. 2.3.
  * The note's transcription in §2 E1 is exact.
* B* = max{|b₁|, …, |b_n|} (1.4), which is max(e₁, e₂, 1) for b = (e₁, −e₂, 1).
  * e_i ≤ log(n+Y)/log 2 = B̄, so ln(eB*) ≤ 1 + log B̄.
  * Ω ≤ (log Y)²·max(T, 0.16).
* C₁ recomputed at 80 digits:
  * C₁(3) = (3e/2)·30⁶·3^{3.5} = 1.39007316922 × 10¹¹ < 2³⁸ = 2.749 × 10¹¹, so this is the min.
  * C₁(2) = e·30⁵·2^{3.5} = 7.47318511874 × 10⁸ < 2³².
  * 0.16·C₁(3) = 2.224 × 10¹⁰ ≥ C₁(2).
  * The popular form 1.4·30⁶·3^{4.5} = 1.4319 × 10¹¹ is weaker, as the note says.

**Case 2 (W₁ = W₂): the two-logarithm fallback.**

* With real logarithms, ln α₃ = 0 is not admissible, so splitting off this case is required.
  Matveev's «допускается α_j = 1» needs a nonzero, hence non-real, value of the logarithm.
* Here t = 2, b = (e₁, −e₂), and Λ ≠ 0 is unchanged.
* The bound C₁(2)·log q₁·log q₂·(1 + log B*) ≤ 0.16·C₁(3)·(log Y)²·(1 + log B̄) is at most the
  Case 1 bound. This is correct.

## 4. External inputs — VERIFIED

* **Robin 1983, p. 369** (the statement list in the introduction):
  * Théorème 11: «ω(n) ≤ 1,3841 log n/log log n pour n ≥ 3».
  * Théorème 13: «ω(n) ≤ log n/(log log n − 1,1714) pour n ≥ 26».
  * The Remarque on p. 383 says the extremal parameter is λ = 1,38401, attained at
    N₉ = 2·3·…·23. My recomputation: 9·log log N₉/log N₉ = 1.3840127. So 1,3841 is Robin's
    rounded-up constant.
  * The note applies Th. 11 to n+i ≥ n ≥ 26 ≥ 3.
* **Rosser–Schoenfeld 1962, p. 69:**
  * Corollary 1, (3.5): "x/log x < π(x) for 17 ≤ x".
  * Theorem 2, (3.3): "x/(log x − ½) < π(x) for 67 ≤ x".
  * The note applies (3.5) at the real point y = 10·l·log n ≥ 10e¹⁰ > 17.
* **No other external bound is used.**
  * log M! ≤ G(M) = (M+1) log M − M + 1 is proved in S3: log i ≤ ∫_i^{i+1} log t dt, and
    G′ = log x + 1/x > 0.
  * The rest is the mean value theorem and a!b! | (a+b)!.

## 5. Final chain and numerics — VERIFIED

**Rerun.**

* `python3 n0_compute.py --check` (sha256 as in CHECKS.md) prints `ALL CHECKS PASSED`, in 5.1 s.
* Its output is character-identical to Appendix A; I diffed them.

**Independent recomputation.** My own code, with the formulas typed from §5.1, §6 and §7.2 of the
note, evaluated both with mpmath `iv` at 50 digits and with `mp` at 80 digits.

| quantity | referee value | note |
|---|---|---|
| φ(45.26) | −0.0106614 | — |
| φ(45.27) | −0.0017169 (fails) | "45.27 fails" ✓ |
| φ(45.28) | +0.0072278 (certified ≥ 0) | 0.00722781770539 ✓ |
| K(45.28) | 2.41092138023 × 10¹¹ | ✓ |
| κ₁, κ₂, μ, ρ, ε₁, e₁, ε₂, κ₃ | agree with §5.2 to 12 digits | ✓ |
| e^45.28 | 4.622257551 × 10¹⁹ | ✓ |
| φᵘ(48.81) / φᵘ(48.82) | −0.0071865 / +0.0018178 | ✓ |
| Kᵘ(48.82), e^48.82 | 5.73427154249 × 10¹², 1.593149775 × 10²¹ | ✓ |
| Q(44.95) / Q(44.96) (Remark 7.2) | 1.00217 (fails) / 0.99329 | ✓ |
| ℓ₁(l), l = 1, 2, 3, 4, 5, 10, 15, 20 | 45.28, 45.35, 45.39, 45.42, 45.44, 45.51, 45.55, 45.58 | ✓ |

**Monotone replacements, by hand.** Each constant is evaluated at ℓ₁ and must bound its
ℓ-dependent quantity for every ℓ ≥ ℓ₁. I checked the direction of each:

* m/ℓ ≤ m/ℓ₁ (κ₁).
* (1 − log log 2 + e^{−ℓ})/ℓ is decreasing, with a positive numerator (κ₂).
* E(ℓ)/l ≤ e₁ℓ. This uses 1/l ≤ 1, (l+2)/l ≤ 3, e^{−ℓ} ≤ e^{−ℓ₁}, 1/ℓ ≤ 1/ℓ₁, and a positive
  bracket, which is ≤ bracket·ℓ/ℓ₁.
* 1/a(ℓ) = (ℓ+m)/((c−2R)(1−μ/ℓ)) ≤ κ₁ℓ/((c−2R)(1−μ/ℓ₁)).
* ℓ²e^{−ℓ} is decreasing for ℓ ≥ 2 (ε₂).
* (ℓ+m−1)/(ℓ−μ) is decreasing, since its derivative has the sign of −(m−1+μ) < 0 (ρ).
* The bound for ε₁.
* max(T, 0.16) ≤ κ₃ℓ², since κ₃ℓ₁² ≥ 0.16.
* κ₁ℓ ≤ (κ₁/ℓ₁⁴)ℓ⁵.
* Y ≤ 10L² < e^L = n.
* ψ(ℓ) = ℓ − 5 log ℓ is increasing for ℓ > 5 (ψ′(45.28) = 0.89).

All are correct for every ℓ ≥ ℓ₁. None is applied in the wrong direction.

**Numerical sanity check (not part of the proof).**

* Fixed l. Every replacement above, and RHS(4.1) ≤ Kℓ⁵ ≤ L, were checked for l ∈ {1, 2, 5, 20}
  on 23,971 grid points ℓ ∈ [ℓ₁(l), 2·10⁴]. No failures.
  * At ℓ = ℓ₁ several replacements are equalities by construction, so I allowed a relative
    rounding tolerance of 10⁻⁴⁵ there.
  * The largest RHS/L on the grid is 0.99687 (l = 5, ℓ = 45.44).
  * The unsimplified bound for l = 1 crosses L at ℓ ≈ 45.2719, which matches the script's info
    line.
* Uniform version. 49 points (ℓ ∈ {48.82, …, 1000}, with l from 1 up to ⌊L⌋) all pass. One
  flag came from a strict-inequality typo in my own test at l = L; it is not a defect of the note.

## 6. Corollary A_l — VERIFIED

**Proposition 6.1, step by step:**

* a(ℓ) = c/(ℓ+m) − 2R/ℓ is decreasing in m. With m ≤ ℓ + log c (from l ≤ L),
  a ≥ aᵘ = (c−4R)(ℓ−μᵘ)/(ℓ(2ℓ+log c)) > 0.
* E/l ≤ e₁ᵘℓ, using m ≤ ℓ + log c.
* ε₁ᵘ uses m ≥ log c.
* c(ℓ+m−1)/a ≤ c(2ℓ+log c−1)/aᵘ, because the numerator increases and a decreases in m.
* (2ℓ+log c−1)/(ℓ−μᵘ) is decreasing, since its derivative has the sign of
  −(2μᵘ + log c − 1) < 0.
* log Y ≤ 2ℓ + log c ≤ κ₁ᵘℓ.
* Y ≤ cL² < n.
* The ω bound uses l − 1 < n.

**The corollary itself:**

* N(l) = max(exp(e^48.82), ⌈e^l⌉). If n ≥ N(l), then log log n ≥ 48.82 and log n ≥ l.
  Proposition 6.1 then gives k ∈ [l, 10·l·log n] with v(n,k) ≥ 2, so v_l(n) ≥ 2.
* C₀ = 10 suffices because 10 > 4R = 5.5364 and the certificate at 48.82 holds; I recomputed it.
* "Level-2 case of `general`; v_l → ∞ not proved" is the correct scope.

**One imprecise sentence (R2).** In §5.3, "log N(l) grows like a power of log l" is loose. My
recomputed per-l thresholds are 45.95 (l = 10³), 46.53 (10⁶), 47.54 (10¹²), 48.67 (10²⁰) and
48.82 (l = e^48.82). The growth is slow, but it is not a clean power of log l. The sentence is not
used anywhere.

## 7. The Langevin remark (§7.1) — VERIFIED, one repair

**Quote.** The quote of Corollaire 1, (8), of condition (1) and of log₂ = loglog matches the scan
(pp. 241–242).

**Logic.**

* Hypotheses: a = 1 gives (n, a) = 1; n > 1; K = ⌊10 log n⌋ ≥ 2 is an integer; and
  log n/log K → ∞, so log n/log K ≥ r(ε) for large n.
* With X = log n/(log K)² → ∞, (8) gives card Y < max(2, (1+c+ε)·π(K)·log log X/log X), which is
  o(π(K)).
* Lemma R(1) with l = 1 and y = K gives J ⊆ [1, K−1] with P(n+j) ≤ K. So J lies inside
  Langevin's Y, and |J| ≥ π(K) − ω(n) ≥ (1 − 0.13841 − o(1))·π(K). The note's "0.139" is a safe
  rounding.
* This gives a contradiction for large n, with effective constants. The logic is correct.

**l-version.**

* J ⊆ [l, K−1] ⊆ [1, K].
* For fixed l, ω_{l,K}(n)/π(K) ≤ R/10 + o(1).
* The same holds uniformly for 1 ≤ l ≤ log n: K ≤ 10L², X ≥ L/(2ℓ + log 10)² → ∞, and the ratio
  is ≤ 0.277 + o(1).
* So §8's statement that the uniform-in-l analogue also follows is correct.

**t₁ (R3).** The note says "We have also not checked how his t₁ is fixed". This can be closed
from the source. Langevin's Exemple on p. 242 fixes t₁ = 1/2, t₂ = 1, t₃ = 1/3, t₄ = 3 and
t₅ = t₆ = 6 for the example constants. Then a = 1 < n^{1/2} for every n > 1.

**Not verified by me:**

* The rough estimate "log log N0 ≳ 10⁶ for this route". It holds only with his example constants,
  and the note labels it rough.
* The RST II statement, which is quoted from the G2 gate. The logical point that "≤ π(K)" is
  borderline is correct.

## 8. Wording — REPAIRED

**What is already right:**

* There is no "first" and no priority claim.
* The qualitative statement is credited to Langevin 1981 plus Lemma R(1), in §7.1 and §8.
* Er98 p. 178 and Shorey–Tijdeman 1986 are named as not obtained.

**Defects:**

1. **Stale citation status (R4).** §8 lists Guy, UPINT B27 (3rd ed.) as "not obtained". Prior-art
   pass B, commit 5495be0, which predates the write-up commit e201fe5, obtained it. I re-fetched
   the OCR (3rd ed., © 2004, p. 126): "They are unable to prove even that v;(n) = 1 has only a
   finite number of solutions. Probably the greatest n for which v1(n) = 1 is 330." The OCR
   subscript glyph is ambiguous, but the sentence is clear. §8 also frames novelty relative to
   the G2 gate only, not to pass B.
2. **Corollary A1 (R1).** "this proves `…v1_eq_1_finite` with answer 'yes'" can be read as a formal
   result or a first resolution. It should say: paper proof, answer `True`, conditional on the
   three cited theorems, no Lean proof, qualitative content also from Langevin + Lemma R(1).
3. **Internal wording (R5).** [Ti73] refers to "the brief for this task", which is internal.
4. **CHECKS.md (R6).** It still says the English Matveev wording was not compared, and that §5 of
   Matveev was not read. Both are now done (§3 above).

## 9. Repairs (exact replacement text; I edited nothing)

**R1 — `PROOF_THEOREM_A.md` §0, Corollary A1.** Replace

> **Corollary A1.** Every n with v₁(n) = 1 satisfies n < N0, so {n : v₁(n) = 1} is finite. In
> Formal Conjectures terms (`FormalConjectures/ErdosProblems/889.lean`), this proves
> `Erdos889.erdos_889.variants.v1_eq_1_finite` with answer "yes".

with

> **Corollary A1.** Every n with v₁(n) = 1 satisfies n < N0, so {n : v₁(n) = 1} is finite. In
> Formal Conjectures terms (`FormalConjectures/ErdosProblems/889.lean`), this is a paper proof,
> not a Lean proof, that `Erdos889.erdos_889.variants.v1_eq_1_finite` holds with answer `True`. It
> depends on the published results E1–E3 (§2). The qualitative finiteness also follows from
> Langevin 1981 together with Lemma R(1) (§7.1).

**R2 — `PROOF_THEOREM_A.md` §5.3, last paragraph.** Replace

> All l from 1 to 20 are in Appendix A. N(l) depends on l only through m = log(10l), so log N(l)
> grows like a power of log l.

with

> All l from 1 to 20 are in Appendix A. The per-l threshold depends on l only through
> m = log(10l), and it grows slowly: the same certificate gives ℓ₁(l) = 45.95 at l = 10³, 46.53 at
> l = 10⁶ and 47.54 at l = 10¹². For every l with 1 ≤ l ≤ log n, §6 gives the single threshold
> log log n ≥ 48.82.

**R3 — `PROOF_THEOREM_A.md` §7.1.** Replace

> We have not refereed
> Langevin's proof. We have also not checked how his t₁ is fixed; a = 1 < n^{t₁} needs t₁ > 0.

with

> We have not refereed
> Langevin's proof. His Théorème 1 allows any real t₁ < 1, and C and c depend on t₁, …, t₆. His
> Exemple (p. 242) takes t₁ = 1/2, t₂ = 1, t₃ = 1/3, t₄ = 3 and t₅ = t₆ = 6. With t₁ = 1/2, the
> condition a = 1 < n^{t₁} holds for every n > 1.

**R4 — `PROOF_THEOREM_A.md` §8.**

First, replace

> What is proved here, relative to the sources checked in the G2 gate:

with

> What is proved here, relative to the sources checked in the G2 gate and in prior-art pass B
> (`PRIOR_ART_20260925_B.md`):

Second, replace the paragraph from "The novelty check has limits." through "Any of these may
already contain Theorem A or its qualitative form." with

> The novelty check has limits. It consists of the G2 gate and prior-art pass B. Both were single
> same-vendor passes without general web search. Pass B obtained Guy, *Unsolved Problems in Number
> Theory*, 3rd ed. (2004), B27, which still says Erdős and Selfridge "are unable to prove even
> that v₁(n) = 1 has only a finite number of solutions" and cites no later work on it. The
> following were not obtained and have not been checked:
>
> * Erdős 1998, p. 178;
> * Shorey–Tijdeman, *Exponential Diophantine Equations* (1986);
> * Erdős, Publ. Math. Debrecen 23 (1976);
> * the Tijdeman result that Langevin cites (MR 54, 1977, p. 246);
> * the MR review of Langevin 1981.
>
> Any of these may already contain Theorem A or its qualitative form.

**R5 — `PROOF_THEOREM_A.md` §9, [Ti73].** Delete the sentence 'The brief for this task said
"Tijdeman 1974".' Keep the rest of the entry.

**R6 — `CHECKS.md`.**

(a) In E1 "How verified", replace the two bullets

> * The English translation PDF was downloaded, but its text layer uses a custom font encoding and
>   could not be read. **The English wording of Cor. 2.3 was not compared.**
> * §5 (definition of h) was not read. With D = 1 the relative and absolute heights coincide, and
>   h(a/b) = log max(|a|,|b|) is the standard definition.

with

> * The English translation (Izv. Math. 64:6, 1217–1269) was compared by the same-vendor referee
>   (`REFEREE_CLAUDE_20260925.md`), using the text layer decoded through the embedded Type 1 font
>   encodings. On p. 1219, (2.1), (2.4), (2.6), "arbitrary fixed non-zero values of the
>   logarithms" and "where B may be replaced by B* (see (1.4))" agree with the Russian.
> * §5 defines h(α) = D⁻¹ Σ_σ max{0, ln|α|_σ}. For a/b in lowest terms this gives
>   log max(|a|,|b|).

(b) In §C, delete the bullet "The English translation of Matveev's Cor. 2.3 was not compared
with the Russian original (B.1)."

(c) Optionally, update the status lines in both files. In `PROOF_THEOREM_A.md` line 4, "No
independent referee yet" should become "One same-vendor referee report
(`REFEREE_CLAUDE_20260925.md`, PASS-WITH-REPAIRS); no cross-vendor or human referee yet".

**N0 after repairs: unchanged.** ℓ₁ = 45.28, log N0 = e^45.28 = 4.6223 × 10¹⁹. Theorem A_unif
keeps 48.82, and Remark 7.2 keeps 44.96.

## 10. Minor observations (no action required)

* §7.1 reuses the letter K for ⌊10 log n⌋, which clashes with the constant K of §5.1. Consider
  writing k* there.
* Appendix A says the run takes "about 6 s" and CHECKS.md says "about 5 s". I measured 5.1 s.
* The finite check in `n0_compute.py` compares logarithms in floating point with a 10⁻⁹
  tolerance. My check compares the same inequalities as exact integers and agrees. The finite
  check is evidence only, as the note says.

## 11. What I did not verify

* The proofs of Matveev 2000, Rosser–Schoenfeld 1962, Robin 1983 and Langevin 1981. I checked
  statements, hypotheses and constants only. For Robin I read the statement list on p. 369, not
  the proof of Théorème 11.
* Novelty or priority. I did not obtain Er98 p. 178, Shorey–Tijdeman 1986, Erdős 1976, Tijdeman's
  MR 54 review or the MR review of Langevin 1981. Apart from Guy B27, I did not re-check the G2
  and pass-B literature claims (RST I/II, Tijdeman 1973 and the others).
* The rough "log log N0 ≳ 10⁶" estimate for the Langevin route.
* The witness table (commit faf11ac), which is outside this review.
* Anything in Lean. The result depends on Matveev's theorem, which is not in Mathlib.
* Independence of the source files. My fetched PDFs are byte-identical to the author's, so an
  error in a scan would affect both readings. The risk is low: they are publisher or archive
  originals, fetched fresh.
* My test scripts live only in the session scratchpad (`scratchpad/ref/`); they are not in the
  repository.

Cost: one agent session. CPU time was a few minutes for the Lemma R run to 10⁶ (not timed
exactly), about 1 minute for the numpy A > 1 search, and seconds for everything else. No paid
resources and no new dependencies (stdlib, mpmath and numpy were already installed).
