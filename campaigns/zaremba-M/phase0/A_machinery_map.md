# A — Machinery map: Shkredov arXiv:2603.14116v2, from Theorem 8 down to 𝓜 = 2^2000

Agent A, Phase 0, Zaremba campaign (slot 1). Written 2026-09-26.
Scope: the exact logical chain the appendix (§6) uses to get 𝓜 = 2^2000 for large primes q = p, drawn as a dependency tree. For each node I give the statement as printed, its hypotheses, the constants it brings in, the outside results it depends on, and a label: **structural**, or **could be replaced by X** (with a citation). Every number below is either quoted with its location or derived here with the working shown. "Unread" means I could not get the text.

---

## 0. Sources: what I read and what I could not

| Tag | Source | Version read | Status |
|---|---|---|---|
| [S] | Shkredov, *On some results of Korobov and Larcher and Zaremba's conjecture*, arXiv:2603.14116 | **v2** (24 Jun 2026, 41 pp.). arXiv lists only v1 and v2, so there is no v3 as of 2026-09-26. | read in full (§§1–6) |
| [MMS22] | Moshchevitin–Murphy–Shkredov, *On Korobov bound concerning Zaremba's conjecture*, arXiv:2212.14646 (= [S]'s ref [43], "IMRN, accepted 2026") | **v1** only (30 Dec 2022, 25 pp.) | read pp. 1–9 (Lemma 4 sketch and the prime case). **The IMRN journal version, which [S] cites by page ("[43, Page 7]", "[43, Page 9]"), is unread.** The arXiv v1 differs from what [S] quotes (see F2 and F3). |
| [MMS18] | Moshchevitin–Murphy–Shkredov, *Popular products and continued fractions*, arXiv:1808.05845 (= [S] ref [42], Israel J. Math. 238 (2020)) | **v2** (23 Aug 2018) | read §§4–8 and the appendix header. Theorem numbers in arXiv v2 **differ** from the journal numbering [S] cites ("[42, Lemmas 12, 21]", "[42, Prop. 7]"). |
| [Usp] | Shkredov, *Non-commutative methods in additive combinatorics and number theory*, Uspekhi Mat. Nauk 76:6 (2021), 119–180 (= [S] ref [53]); Russian original, mathnet.ru rm10029 | journal PDF (Russian) | read §6, Theorems 47–49 and Corollary 50 (pp. 152–157). It is **not on arXiv** (checked against Shkredov's arXiv author feed). |
| [RS] | Rudnev–Shkredov, arXiv:1812.01671 (= [S] ref [50], Mathematika 68 (2022)) | **v3** | read intro and Thm 2. [S] cites "[50, Theorem 5]", which is the journal numbering; the SL2 statement is arXiv Thm 2. |
| [Mur] | Murphy, *Group action combinatorics*, arXiv:1907.13569 (= [S] ref [48]) | v1 | read §§3–4. Only an "absolute constant C" appears there; the explicit **C1 = 9, C2 = 32 are not in it**. |
| [GF] | Shkredov, *girth-free BG machine*, arXiv:2111.05751 (= [S] ref [55]) | v1 | read Thms 1–3, 7, 9 and the proof of (15)–(18). |
| [Z] | X. Zhang, arXiv:2605.02518 | v2 (8 May 2026) | read §§1–3 (skimmed). |
| — | Helfgott 2008 (Annals); Bourgain–Gamburd 2008 (Annals); Tao–Vu book Thm 2.29 and Lemma 2.13; Tao 2008 Prop 4.5; Kurzweil 1951 Thm VIII; Hensley 1989/1992 | — | **unread**. I know them only through the quotations in [S], [MMS18], [RS] and [Usp]. |

---

## 1. Top of the chain (as printed)

**Theorem 8 [S, p. 6].** There is an absolute constant 𝓜 such that for all M ≥ 𝓜 and any q ∈ Z there are at least q^{2w_M − 1 − o(1)} positive integers a with (a, q) = 1 and a/q = [0; c_1, …, c_s], c_j ≤ 100M.

**Corollary 1 [S, p. 2].** There is an absolute M ≥ 2 such that for every prime (or square-free) p some a coprime to p has all partial quotients ≤ M.

**Appendix claim (158) [S, p. 38].** For sufficiently large q = p (prime) one can take 𝓜 = 2^2000. This covers only the prime case, only one a, and no δ-Assumption (so M̃ = 200). q₀ is not explicit.

**Remark 9 [S, p. 6].** Tang–Zhang/Zhang make Lemma 14 hold for all q, and with that Corollary 1 holds for every q ([Z]). [Z, Remark 1.3] says its M is "effectively computable" but does not compute it.

Note that (22) bounds partial quotients by **100M**, while (158) sets the *threshold* 𝓜 = 2^2000. The appendix does not say whether the Zaremba constant is 𝓜 or 100𝓜. Taken literally it is 100·2^2000 ≈ 2^2006.6 (flag F8).

---

## 2. Dependency tree

```
(158)  M = 2^2000                                   [S §6]
 └─ (157) partial quotients ≤ max{O(M*), M~} ~ max{10(κε)^-1, 100 δ_A^-60}      [S §5.4]
     ├─ M~ = 200 (no δ-Assumption for prime q)                                  [S §6]
     ├─ ε < 1/18 − o(1)            (156) ⇐ (119) N ≤ q^{1/9}/(2^30 M M* M~)       [S Prop 35, §5.2 (151)]
     │    └─ Prop 35 (middle interval) ⇐ Lemma 32 ⇐ Lemmas 25,28–31, Lemma 33/Cor 34 (Dirichlet), Lemma 19, Lemma 10
     ├─ M* ≥ 40M                   ⇐ 1−w_M ≥ 10(1−w_{M*})  ⇐ Thm 38 (Kurzweil)      [S §6]
     │    └─ "10" ⇐ N* = N/H^2 = N^{1/10}, H = N^{9/20}  (155) ε* = ε/10          [S §5.4]
     ├─ |A∩A^{-1}| ≥ |A|^2 φ(q)/(2q^2)  needs  M^{-1} q^{w_M} N^{κ/10} ≫ q^{1+o(1)}   [S §5.4]
     │    ├─ Lemma 21 (Ahlfors–David lower bound (54))  ⇐ Lemma 13 (Moshchevitin)
     │    ├─ Lemma 20 (Möbius; trivial for prime q)
     │    ├─ Lemma 18 (good intervals, loss N*^{-κ/2}) ⇐ Lemma 17 (loss N2^{-κ/4}) ⇐ Cor 16
     │    └─ Cor 16  |A∩B^{-1}| − |A||B|/q ≪ √(|A||B|) N^{-κ}   (proof gives N^{-κ/2})
     │         ├─ Lemma 15 (2-parameter family, girth-free [GF Thm 3])   ← used in the proof of Cor 16
     │         └─ Lemma 14 (1-parameter family, [MMS22 Lemma 4] = [MMS18 Prop 7])  ← the family whose κ the appendix computes
     │              └─ κ = δ/6   ("log N·κ = (6m)^{-1} τ δ log p", m = τ log_N p)     [S §6, citing IMRN [43, p. 9], unread]
     │                   ├─ Stage 1 (free group + girth + Kesten):  G = {v^j u^{-j}}, K(G^m) = p^{τ/6}, τ = 1/4
     │                   │     ⇐ [MMS18 Thm 25 / Cor 31 / Lemmas 26–28], Margulis girth (Thm 29), Kesten
     │                   ├─ Hölder (18) [MMS22]: saving p^{-δ} → p^{-δ/(2l)}, 2^l ≤ 2m
     │                   └─ Stages 2+3 (L2-flattening + quasirandomness):  δ = c/2^{k+4}, k = ⌈1/c⌉ + 1
     │                          └─ c ≥ min{1/3, 1/(8C2), τ/(4C2), 0.5 c_H/(C1+C2)} = 1/1640   [S §6, "following [53, Thm 49]"]
     │                               ├─ quasirandomness d = (p−1)/2 (Frobenius)             [Usp Thm 47]
     │                               ├─ Thm 39 non-commutative BSG (Murphy), C1 = 9, C2 = 32   [S; via Tao–Vu 2.29 + Tao Prop 4.5, unread]
     │                               ├─ Lemma 40 growth |A^3| ≫ min{|SL2|, |A|^{1+c_H}}, c_H = 1/20   [RS Thm 2]
     │                               └─ subgroup non-concentration (Dickson classification; K = p^{τ/6})
     └─ Lemma 10 (x|y| ≥ q/M ⇒ c_j ≤ M; c_j ≤ M ⇒ x|y| ≥ q/(4M))                  [S; Korobov]
```

Everything below "κ" is the **growth-in-SL2 block**. Everything above it is the **Diophantine and Cantor-set block**. The appendix says the losses are "entirely" in κ [S, end of §5.4]. My bookkeeping in §4 agrees: κ-independent overheads add only about 14 bits to log₂ M.

---

## 3. Nodes: exact statement, constants, inputs, replaceability

### N-A. Lemma 10 (Korobov's hyperbola lemma) [S, p. 7]
- **Statement.** Let (a, q) = 1 and a/q = [0; c_1, …, c_s], and consider ax ≡ y (mod q) with 1 ≤ x < q and 1 ≤ |y| < q. If every solution has x|y| ≥ q/M, then c_j ≤ M for all j. Conversely, if c_j ≤ M for all j, every solution has x|y| ≥ q/(4M).
- **Constant.** The factor **4** in 4M.
- **Inputs.** Korobov [33, Lemma 5]; [44 §9]; [43 Lemma 2].
- **Replaceable.** Remark 11 [S] says 4M can become **M + 2** "(see the proof of [43, Lemma])". That saves about 2 bits (route R5).

### N-B. Lemma 13 (Moshchevitin's interval structure) [S, p. 8]
- **Statement.** For t ≤ √q, Z_M(t) = I_1 ⊔ … ⊔ I_T with c₁t^{2w_M} ≤ T ≤ c₂t^{2w_M} and [q/t²] ≤ |I_j| ≤ 8(M+1)q/t² + 1.
- **Constants.** c₁ and c₂ are absolute and unspecified (in [MMS22 Lemma 3], C₅ = C₁/(2C₄ log k)). They are q-independent, so they do not affect the exponent of M.
- **Status.** Structural (it is the Cantor-set model). The constants only change q₀.

### N-C. Theorem 12 (Hensley) and Theorem 38 (Kurzweil) [S, pp. 8, 38]
- **Theorem 12** (Hensley [20]): w_M = 1 − 6/(π²M) − 72 log M/(π⁴M²) + O(1/M²). Here 6/π² = 0.60793.
- **Theorem 38** (Kurzweil [36, Thm VIII]; unread): for M ≥ 1000, 1 − 0.99/M ≤ w_M ≤ 1 − 1/(4M).
- **Use.** To get 1 − w_M ≥ 10(1 − w_{M*}) it is enough that 10·0.99/M* ≤ 1/(4M), that is M* ≥ 39.6M, so **M* ≥ 40M**.
- **Replaceable** by Hensley's asymptotic, or by rigorous interval enclosures of w_M (Pollicott–Vytnova arXiv:2012.07083, unread). Asymptotically the ratio needed is 10(1 + o(1)), so M* ≈ 10M. That saves 2 bits (route R5).

### N-D. Lemma 21 (Ahlfors–David property) [S, p. 14]
- **Statement.** Let M ≥ 2, t ≫ M and I ⊆ Z/qZ an interval. Then |Z_M(t) ∩ I| ≪ M⁴|I|^{w_M}N^{1−w_M}. If also |I| ≥ N and the centre of I lies in Z_M(t), then |Z_M(t) ∩ I| ≫ M^{-1}|I|^{w_M}N^{1−w_M}.
- **Use in §5.4.** |A| ≫ M*^{-1} q^{w_M} N^{1−w_M} H^{2(w_{M*}−1)} for A = Z_M(t) ∩ Z_{M*}(tH).
- **Status.** Structural. The polynomial factors in M are q^{o(1)}.

### N-E. Section 4 (critical denominators): Lemmas 25, 28–32, Lemma 33/Cor 34, Proposition 35 [S, pp. 15–31]
- **Proposition 35.** Let 2 ≤ M ≤ M* ≤ N^{10^{-10}}, M̃ ≤ N^{1/1000}, H = N^{9/20}, and suppose **(119) N ≤ q^{1/9}/(2^{30} M M* M̃)**. Let I ⊆ J_{u/v} ⊆ Z_M(t) ∩ Z_{M*}(tH) with 20N/(δ⁶⁰M̃H²) ≤ |I| ≤ 40N/(δ⁶⁰M̃H²). Then either I fails the δ-Assumption, or some a ∈ I ∩ Z_M^{-1}(t) has a partial quotient ≥ M* at a denominator q(a) ∈ [√q N/H, √q N].
- **Internal constants.** m = 200 (Lemma 31/32). The exponent 60 on δ comes from Lemma 19 with k = 5: exp(−4k log(4k) log(1/δ)) = δ^{20 log 20} ≤ δ^{60}. Also T = √q N^{2/7}, and the 2^{15}, 2^{19}, 2^{26}, 2^{30} factors in (124)–(129).
- **Output that affects M.** Only the range **ε < 1/18** ((119) with N = q^{2ε}, so N^{9/2} ≤ q^{1/2} up to q^{o(1)}), and **M̃** (200 for primes, 100δ^{-60} in general). All the 2^a·M^b factors are q^{o(1)}.
- **Inputs.** Only elementary facts: continuants, the Dirichlet principle and Lemma 10. No growth.
- **Replaceable.** [S, p. 6] says "the constant 1/9 can be improved". Enlarging the admissible ε range would lower M, since M ∝ 1/ε. This is route R5 (re-optimising ε), and the gain is at most a constant factor: ε ≤ 1/2 even in principle, against 1/18 now, so at most log₂ 9 ≈ 3.2 bits. The Diophantine machinery itself is **structural** for this proof, but the argument is untouched by the growth routes.

### N-F. Lemma 14 [S, p. 9] = [MMS22 Lemma 4] = [MMS18 Prop 7]
- **Statement.** Let q ∈ Z, N a positive integer and A, B ⊆ Z/qZ. There is an absolute κ > 0 with
  | #{(a + 2c)(b + 2c) = 1 : a ∈ A, b ∈ B, c ∈ [N]} − N|A||B|/q | ≪ √(|A||B|) N^{1−κ}.
- **Equivalent operator form.** This is the family g_j = (−2j, 1−4j² | 1, 2j) acting on P¹(F_p). Up to a GL₂ multiplier it is G = {(1, −2j | 2j, 1−4j²)} = {v^j u^{-j}}, with u = (1 2 | 0 1) and v = (1 0 | 2 1) [MMS22 (15)–(16); MMS18 Cor 31]. The phase-0 numerics (`zaremba_kappa_numerics.py`) measure exactly this operator.
- **Proof skeleton ([MMS22] pp. 5–6).**
  1. *Stage 1 (girth / free group).* Σ_{x∈gΓ} r_{G,2m}(x) ≤ |G|^{2m}/K(G) for every coset of every proper subgroup Γ (17), with m = (τ/4) log_N p and K(G) = p^{τ/6} in [MMS22] v1. [S §6] instead says "τ = 1/4, m = τ log_N p, K(G^m) = p^{τ/6}" (flag F2).
  2. *Hölder (18).* |Σ_s Σ_{x∈B} f(s)A(sx) − |A||B|Σf/p| ≤ √(|A||B|) · (|B|^{-1} Σ_s r_{f,2^l}(s) Σ_{x∈B} B(sx))^{1/2^l}, for the maximal l with 2^l ≤ 2m.
  3. *Stages 2+3 (19).* Σ_s F(s) Σ_{x∈B} B(sx) ≪ |B| ‖F‖₁ p^{-δ}, with "δ = 1/2^{k+2} and k ≪ log p / log K(f)" [MMS22 p. 6].
  4. The printed conclusion is ≪ √(|A||B|) |G| p^{-δ/24m} ≪ √(|A||B|) N^{1−κ}, with "δ = δ(τ) = exp(−C/τ)" [MMS22 p. 6].
- **External inputs.** Free subgroup ⟨u, v⟩ ≤ SL₂(Z) (Sanov); Margulis's girth bound [MMS18 Thm 29]; Kesten's bound [MMS18 Lemma 27]; Dickson's classification of subgroups [MMS18 Thm 12, Lemma 28]; Bourgain–Gamburd L²-flattening [MMS18 Thm 15]; Frobenius quasirandomness [Usp Thm 47] or the doubly-transitive bound [MMS18 Cor 21]; Helfgott growth [MMS18 Thm 19].
- **Replaceable.**
  - Stage 1 could be replaced by [GF] Lemma 15 (Thm 3), which is girth-free and Kesten-free.
  - Stages 2+3 are the target of route R2 (a BSG-free flattening lemma).
  - The whole node is the target of routes R3 (bilinear Kloosterman / incidence bound) and R4 (automorphic spectral gap).
  - Its composite-q version is [Z, Thm 3.6]. Its κ (η there) is ineffective in print.

### N-G. Lemma 15 [S, p. 9] = [GF Thm 3]
- **Statement.** Let δ ∈ (0, 1], N sufficiently large, N ≤ q^{cδ}, g ∈ SL₂ non-linear, and S ⊆ [N] × [N] with |S| ≥ N^{1+δ}. Then there is κ = κ(δ) > 0 with
  |#{g(α + a) = β + b : (α, β) ∈ S, a ∈ A, b ∈ B} − |S||A||B|/q| ≪_g √(|A||B|) |S|^{1−κ}.
- **Constants ([GF] (15)–(18)).** K = N^{−o_s(1)} min{(|H|/N)^{2s}N^{-1}, |H|^{2s(1−δ*)}N^{-1}, |H|^{2s(1−δ*)}}, with s maximal such that (2N)^{2s+1} < 2^{-5}p^{1/4}, so log K ≫ δ log p. The saving is p^{-ζ/2l} with **ζ = 1/2^{t+2}, t ≪ log p / log K ≪ δ^{-1}**, and the final bound is N^{-exp(−Ω(1/δ))}. The implicit constants are not computed anywhere.
- **Use.** The *proof of Corollary 16* invokes Lemma 15 (with S = [h] × [h], g x = 1/x), not Lemma 14. The appendix computes κ only for the one-parameter family (159) (flag F5).
- **Status.** This is an alternative to Stage 1. It still ends in the same doubly-exponential BG output.

### N-H. Corollary 16 [S, p. 9]
- **Statement.** Let Λ₁, Λ₂ ⊂ Z/qZ, I = [N], A = I ∔ Λ₁ and B = I ∔ Λ₂. Then |A ∩ B^{-1}| − |A||B|/q ≪ √(|A||B|) N^{-κ}.
- **Proof.** Smooth I by an h-interval, h ~ √N. The main term uses Lemma 15 and gives √(|A||B|) N^{-κ/2}; the smoothing error is h|A||B|/(Nq) + √(|A||B|) h^{1−κ}/√N. **The proof yields exponent κ/2**, and the text then says "the constant κ may vary from line to line" (flag F6).
- **Structural?** The reduction from an intersection count to an operator bound is structural. The input can be replaced by any bound of Lemma-14/15 type, which is exactly where routes R3 and R4 plug in: the "gap_indicator" of R3 is this node for N = p^{1/9} at near-full density.

### N-I. Lemma 17 and Lemma 18 [S, pp. 10–11]
- **Lemma 17.** With C = A ∩ B^{-1} and C̄ = C + [−N₂/2, N₂/2] (N₂ ≤ N₁): |A| − O(q √(|A|/|B|) N₂^{-κ/2}) ≤ |C̄| ≤ |A|(1 + 2N₂/N₁). The proof ends with N₂^{-κ/4}, i.e. another halving (h ~ N₂^{1/2}).
- **Lemma 18.** |A \ Ã| ≪ q N*^{-κ/2}.
- **Status.** Structural bookkeeping. Each step costs a factor 2 in κ, so log₂ M gains about 1–2 bits (flag F6).

### N-J. §5.4 assembly [S, pp. 37]
- A = Z_M(t) ∩ Z_{M*}(tH), t = q^{1/2−ε}, N = q^{2ε}, H = N^{9/20}, N* = N/H² = N^{1/10}.
- **Key inequality.** |A ∩ A^{-1}| ≥ |A|²φ(q)/(2q²) holds provided M^{-1} q^{w_M} N^{κ/10} ≫ q^{1+o(1)}, which (from Cor 16 at scale N*) means **2εκ/10 > 1 − w_M**. With Thm 38, it is enough that M > 0.99 · 5/(εκ).
- **Output (157).** Partial quotients ≤ max{O(M*), M̃} ~ max{10(κε)^{-1}, 100δ_A^{-60}}. Here δ_A is the δ-Assumption parameter of Assumption 22, **not** the flattening δ (a name clash in [S]).
- **Status.** Structural. The factors 10 (from N^{1/10}), 40 (M*/M) and 4 (Lemma 10) are replaceable overheads (R5).

### N-K. Growth block, the appendix's formula [S, p. 38] (the heart of 𝓜)
- **As printed.** "log N · κ = (6m)^{-1} τ δ log p = 6^{-1} δ log N, where δ = c/2^{k+4}, k = ⌈c^{-1}⌉ + 1 and c > 0 is an absolute constant." And then "c ≥ min{1/3, (8C₂)^{-1}, τ(4C₂)^{-1}, 0.5 c_H (C₁ + C₂)^{-1}} = 1/1640. It implies that k = 1641. So, κ ≥ 2^{-1656}."
- **Recomputation.** With c = 1/1640 and k = 1641: log₂(1/κ) = k + 4 + log₂ 1640 + log₂ 6 = 1641 + 4 + 10.680 + 2.585 = **1658.26**. So κ = 2^{-1658.26}, not 2^{-1656} (flag F3, the known N2 discrepancy, confirmed).
- **Terms of the minimum** (τ = 1/4, C₁ = 9, C₂ = 32, c_H = 1/20):
  - 1/3
  - 1/(8C₂) = 1/256
  - τ/(4C₂) = 1/512
  - 0.5c_H/(C₁ + C₂) = 1/1640

  The binding term is the BSG + growth term. With τ = 1/5 the third term is 1/640 (still not binding). It becomes binding only for **τ < 4C₂/1640 = 16/205 ≈ 0.078**, for example τ = 1/20 gives 1/2560 (flag F2).
- **Provenance of the minimum.** [S] says "following the argument of the proof of [53, Thm 49]". [Usp] Thm 49 (p. 154) states: let G be d-quasirandom with |X³| ≥ min{|G|, |X|^{1+c*}} for every generating X; let A satisfy max_{g,Γ} |A ∩ gΓ| ≤ |A|/K; put K* = min{d, K}. Then for every h, #{h = a₁⋯a_{2k}} = |A|^{2k}/|G| + O(|A|^{2k}/K*^{ck}). The proof sketch (pp. 155–157) reduces this to **(60): T_{2s}(f) ≪ T_s(f)|A|^{2s}K*^{-c}, "0 < c < 1/4"**. It has four cases, which match the four terms:
  1. Quasirandom case: T_{2s} ≤ T_s² |G|/K*. This gives T_s ≥ K*^{1−c}|A|^{2s}/|G|, and the term **1/3** (d = (p−1)/2 ≈ |G|^{1/3}, [Usp Thm 47]).
  2. BSG + growth case: E(P) ≫ |P|³/K₁ with K₁ = K*^c L⁴. BSG gives |P*| ≫ |P|/K₁^{C₁} and |P*³| ≪ K₁^{C₂}|P*|, and growth then gives K₁ ≫ |P|^{c₁}. This is the term **0.5c_H/(C₁ + C₂)**.
  3. P*³ = G case: |P| ≫ |G|K₁^{-C}. This is the term **1/(8C₂)**.
  4. Subgroup case: P* ⊆ H forces ∆|P|K₁^{-C} ≪ |A|^s/K. This is the term **τ/(4C₂)**, through K = p^{τ/6}.

  The sketch prints no explicit constants. The matching of terms to cases is my reading, not printed (task N1 should confirm it).
- **Dependencies.**
  - Thm 39 (Murphy's BSG, C₁ = 9, C₂ = 32) is **not in [Mur] arXiv**, which only says "C absolute"; [S] derives it from Tao–Vu Thm 2.29 + Lemma 2.13 = Tao 2008 Prop 4.5, which are unread (flag F7).
  - Lemma 40 (c_H = 1/20) comes from [RS] Thm 2, whose hypothesis is "**symmetric** generating set", while Lemma 40 as printed in [S] drops "symmetric" (flag F4).

---

## 4. Constant ledger (the whole of 𝓜 in one line)

All logs are base 2. Every step has a source.

1. **c = 1/1640** = 0.5 · (1/20)/(9 + 32). [S p. 39]
2. **k = ⌈1/c⌉ + 1 = 1641.** [S p. 38]. See flag F1: this step is the one I could not reconcile with the texts I read.
3. **δ = c/2^{k+4}**, so log(1/δ) = 1645 + 10.680 = 1655.68. [S p. 38]
4. **κ = δ/6**, so log(1/κ) = **1658.26**. [S p. 38; the (6m)^{-1}τ formula cites IMRN [43, p. 9], unread]
5. **M ≳ 0.99 · 5/(εκ)** from 2εκ/10 > 1 − w_M (§5.4 condition plus Thm 38). With **ε < 1/18**, 5 · 18 = 90, about 6.5 bits. [S (155)–(156); my derivation above]. [S (157)] prints 10(κε)^{-1}, a factor 2 larger (+1 bit).
6. **M* = 40M** (+5.32 bits); **Lemma 10 factor 4** (+2 bits); the appendix does not specify **(22) 100M** (+6.64 bits if counted, flag F8).

**Total.** log₂ 𝓜 ≈ 1658.3 + [6.5 to 7.5] + 5.3 + 2 (+ 6.6 if 100M is counted) ≈ **1672–1680**. This agrees with the design note (~1680). The κ-independent overhead is C₀ ≈ 2^{14}–2^{21}. Agent B owns the exact-rational version of this ledger. I only list which node every factor comes from.

**Sensitivity.** Over 98% of log₂ 𝓜 is k ≈ 1/c. Per the ledger, log₂ 𝓜 ≈ 1/c + log₂(1/c) + (~20–25). Reaching the announce bar log₂ 𝓜 ≤ 500 needs 1/c ≲ 470. Reaching log₂ 𝓜 ≤ 150 needs 1/c ≲ 120.

---

## 5. Audit flags (for RB1, N1, N2, and every route owner)

**F1 (critical, unresolved): the step count k = ⌈1/c⌉ + 1 has no normalisation in any source text I read.**
Both lineage texts I read count dyadic flattening steps as log|G| / (c · log K):
- [Usp] Cor 50 (p. 157): ‖Â(ρ)‖^{2^{k+1}}/|G| ≪ |A|^{2^{k+1}}/K*^{ck}, "taking k ≫ 1/δ" where K* ≥ |G|^δ. So a saving needs K*^{ck} > |G|, that is, k > 1/(c·δ_K) with δ_K = log K*/log|G|.
- [MMS18] Thm 9 (p. 11/22): k = 3 log p / (c* log K), δ = 2^{-(k+2)}. In Thm 24 (p. 27–28) this becomes k = 12/(c*τ) − 1, i.e. δ = ¼·b₀^{-1/τ} with b₀ = 2^{12/c*}.
- [MMS22] p. 6 likewise writes δ = exp(−C/τ).

In this lineage, K is the Stage-1 non-concentration, K = p^{τ/6} (or p^{τ/4}), so δ_K ≤ τ/3 ≤ 1/12. If c in the minimum of §3 N-K is the per-step exponent on this K-scale (the survey's (60) is written with K*^{-c}), then:

| reading | k | log₂(1/κ) |
|---|---|---|
| appendix as printed (needs a gain of \|G\|^{-c} per step) | 1641 | 1658 |
| p-scale gain p^{-c} per step, from ‖μ‖₂² ≈ p^{-τ} to p^{-3} | ≈ (3 − τ)/c = 4510 | ≈ 4528 |
| K-scale with the loosest cap K ≤ p^τ (δ_K ≤ 1/12) | ≥ 12/c = 19680 | ≥ 19698 |
| K-scale literal, [Usp] Thm 49 with K* = p^{τ/6}, τ = 1/4 | 18/(τc) = 118,080 | ≈ 118,098 |

The appendix's k = ⌈1/c⌉ + 1 is what you get with δ_K = 1 (K* ≈ |G|). In the [Usp] sketch, however, the growth case measures K₁ against |P| (the current level-set size), which grows during the iteration, so a proof with a gain close to |G|-scale may exist. I have **not** found one in print.

The appendix gives the formula with a citation to the IMRN version of [43] (unread). **This is not a claim that [S] is wrong.** It is the first thing RB1/N1 must settle, because it decides whether the baseline is log₂ 𝓜 ≈ 1.7·10³ or ≈ 10⁴–10⁵. It also changes what "log₂ M ≤ 500" requires: a new flattening lemma would have to fix both c and this normalisation.

**F2: τ is inconsistent across versions.**
- [MMS18] v2 Thm 25: d(Cay) ≥ ¼ log_N p for p ≫ 1. The proof gives ≥ ⅓ log_N(p/2), from Margulis with ‖g_j‖ ≤ 5j² ≤ N³ for N ≥ 5. Lemma 27 requires m ≤ γ and Lemma 28 requires m ≤ γ/2, so in Thm 24 τ ≤ τ₀/2 = 1/8, and K^{-1} = |S|^{-m/4} = p^{-τ/4}.
- [MMS22] v1: girth τ log_N p with **τ = 1/5**, m = (τ/4) log_N p = (1/20) log_N p, K(G) = p^{τ/6}.
- [S §6]: **τ = 1/4**, m = τ log_N p, K(G^m) = p^{τ/6}.

As N → ∞, Margulis gives d ≥ log(p/2)/log(5N²) → ½ log_N p, so m ≤ d/2 allows τ up to ¼ − o(1). The appendix's τ = 1/4 is therefore attainable only in the limit, and is fine for the binding term. Because κ = δ/6 is τ-free, τ enters 𝓜 only through the term τ/(4C₂). That term binds iff τ < 0.078, and then 1/c = 512/τ. With [MMS22]'s effective m-coefficient 1/20, c = 1/2560, k = 2561 and log₂(1/κ) ≈ 2579, above 2000. **Which τ is legitimate in the formula decides whether 2^2000 holds.**

**F3: 2^{-1656} vs 2^{-1658.26}.** Recomputed in §3 N-K. The difference is 2.26 bits and is immaterial to (158).

**F4: Lemma 40 drops the symmetry hypothesis.** [RS] Thm 2 assumes a symmetric generating set. The BSG output P* ⊆ p^{-1}P need not be symmetric. Symmetrising with |(A ∪ A^{-1} ∪ {e})³| ≤ (3|A³|/|A|)³|A| (quoted in [MMS18] eq. before (29)) turns K₁^{C₂} into ≈ K₁^{3C₂}. Then the growth term becomes 0.5c_H/(C₁ + 3C₂) = **1/4200** (my arithmetic, assuming the symmetrisation is applied after BSG). An alternative: Tao's approximate-group output may already be symmetric (Tao 2008, unread). RB1 should settle this.

**F5: Cor 16 is proved with Lemma 15, but the appendix computes κ for Lemma 14's family (159).** Lemma 15's constants ([GF] (15)–(18)) are never made explicit. A plausible repair is a reparametrisation i' = i + d that reduces the two-parameter count to the diagonal family with a shifted B. I have not checked it.

**F6: halvings of κ.** Cor 16's proof gives κ/2, Lemma 17 κ/4, Lemma 18 κ/2. §5.4 uses Cor 16 at scale N* with "κ varying". Each halving adds 1 bit to log₂ 𝓜. The appendix's κ is for Lemma 14 itself, so 1–2 bits are unaccounted for (+1 to +2 in log₂ 𝓜).

**F7: C₁ = 9, C₂ = 32 are unverified.** They are not in [Mur] arXiv. [S] derives them from Tao–Vu Thm 2.29 + Lemma 2.13 (= Tao 2008 Prop 4.5), both unread.

**F8: the final constant.** It is unclear whether the final constant is 𝓜 (the threshold) or 100𝓜 ((22)). Also, the "4 max{M, M*, M̃}" of §5.2 and the (157) "max{O(M*), M̃}" are not reconciled with (22)'s 100M, since M* = 40M already exceeds 100M/4.

**F9: numbering.** [S] cites [42], [43] and [50] by journal numbering and pages. The arXiv versions ([MMS18] v2, [MMS22] v1, [RS] v3) use different theorem numbers and, for [MMS22], different formulas (p^{-δ/24m} with m = (τ/4) log_N p, against the appendix's (6m)^{-1}τ). The IMRN text of [43] is unread.

---

## 6. Replaceability summary (the map every route uses)

| Node | Constant(s) it controls | Label | Could be replaced by (citation) | Effect on log₂ 𝓜 |
|---|---|---|---|---|
| Lemma 40 (growth) | c_H = 1/20 | replaceable input | Kowalski 1/1512, Helfgott–Kowalski version 1/3024 ([MMS18] Thm 19; both worse). [RS] footnote: **1/15** if an SL₂ analogue of Szőnyi's direction theorem holds (conditional); "as if 1/12" only for the diameter. Button–Roney-Dougal: δ ≤ 0.3012 is the ceiling for any growth exponent (quoted in [RS] p. 2). | c_H = 1/15 → 1/c = 1230 (−410 bits). c_H = 0.3 with the same BSG gives 1/c ≈ 273. **Constant substitution, not announceable.** |
| Thm 39 (BSG) | C₁ = 9, C₂ = 32 | replaceable input | better non-commutative BSG/tripling exponents (N6, unread). [Mur] Thm 24 (group-action asymmetric BSG, with its own L^{2ε} loss). Removing BSG altogether is route R2. | Without BSG the minimum becomes min{1/3, 0.5c_H} = 1/40, so log₂ 𝓜 ≈ 40 + 5 + 25 ≈ 70 (under the appendix normalisation of F1). |
| Growth-case term algebra | 0.5c_H/(C₁ + C₂) | bookkeeping | My reading of the [Usp] sketch: the growth case needs (1−c)c_H > c(C₂ + C₁c_H) using \|P\| ≫ \|A\|K^{-c} ≥ K^{1−c}, i.e. c < c_H/(C₂ + (C₁+1)c_H) = **1/650**. This is not verified, and it is **bookkeeping** that must not be announced. | 1/c: 1640 → 650 (−990 bits) *if* the [Usp] sketch holds with these constants. RB1 should check. |
| Stage 1 (girth/Kesten) | τ, K = p^{τ/6}, m | replaceable | [GF] Lemma 15 (girth-free); Margulis asymptotic τ → ¼; Kesten exact spectral radius √(2k−1)/k (the numerics show the true operator attains 2√(N−1)/N) | τ is not binding at 1/4 (F2) |
| Stages 2+3 (flattening + quasirandom) | k, δ = c/2^{k+4}: the **2^{-1/c}** | **structural for dyadic BG** (each doubling halves the exponent by the 2^{k+1}-th root in Hölder/Cor 50) | Replacing it needs a non-BG input: R3 (bilinear Kloosterman/incidence for Cor 16 at N = p^{1/9}), R4 (automorphic spectral gap), or R2 (a flattening lemma with c ≥ 1/450 under the appendix normalisation). [Usp] p. 157: "It would be extremely interesting to find a better bound here" (exp(−O(1/δ)) is typical). | This is where all ~1650 bits live |
| Cor 16 / Lemmas 17–18 | κ/2, κ/4 | structural reduction, replaceable input | any L² bound for I-invariant sets at scale N = p^{1/9} (R3). [S] p. 6: "the first stage of BG is not required" for a single a in the prime case. | the input is what matters. The halvings cost 1–2 bits. |
| §5.4 + Thm 38 | 10, 40, ε < 1/18 | overhead | Hensley asymptotic (M* ≈ 10M), Pollicott–Vytnova enclosures, improving 1/9 ([S] p. 6) | at most about 7 bits total |
| Lemma 10 | 4M | overhead | Remark 11: M + 2 | −2 bits |
| Section 4 (Prop 35) | ε < 1/18, M̃ = 200 | structural (Diophantine) | none needed. Its q^{o(1)} constants are irrelevant | only via ε |
| Composite q | ω(q)-terms, Lemma 20 | not in the prime chain | [Z] Thms 2.1/2.2/2.4 (ineffective as printed) | — |

**Bottom line for the routes.**
1. As printed, 𝓜 = 2^{Θ(1/c)} with c = 0.5c_H/(C₁ + C₂). The only lever that changes the order of magnitude is the exponent in the BG flattening (k ≈ 1/c doublings, each costing a square root).
2. Substituting better c_H or BSG constants moves 1/c by constant factors and is bookkeeping.
3. Before any route is scored, RB1/N1 must resolve **F1** (k's normalisation) and **F2** (τ). F1 alone could move the true baseline from ~1.7·10³ bits to ~10⁴–10⁵ bits.
