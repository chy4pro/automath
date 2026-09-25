# Erdős #889: second prior-art pass (2026-09-25, pass B)

Question: has anyone already written that {n : v₁(n) = 1} is finite (equivalently, v₁(n) ≥ 2 for all
large n), in particular as a consequence of Langevin 1981, Ramachandra–Shorey–Tijdeman or Tijdeman?
This pass follows up G2_KILL_GATE_20260925.md and does not repeat what that file already covers.
It is a same-vendor (Claude) literature pass: no proof checking and no cross-vendor review.

Access notes. WebSearch was unavailable because the session budget was spent (200/200), and
Google and Google Books were blocked (JavaScript wall; the Books API has a daily quota of 0). I did
not use a general search engine to get around the budget. Sources came from:
* archive.org full-text search (FTS), both archive-wide and restricted to single items. For
  lending-restricted books this returns only highlighted snippets.
* archive.org downloads of unrestricted OCR text.
* The zbMATH Open API, OpenAlex, Semantic Scholar, OpenCitations and Crossref.
* Numdam item pages (bibliographies), matwbn Acta Arith. scans (images read directly), and arXiv
  e-print sources.
* A RIMS Kôkyûroku PDF (OCR layer), the GitHub API, the erdosproblems.com pages, and the
  StackExchange API (MathOverflow and Math.SE).

Cost: about 1 agent-hour. No paid resources, no new dependencies.

## 0. Verdict

**INCONCLUSIVE, leaning NOT_FOUND.** No source I obtained states the corollary. No source links
Langevin 1981, RST or Tijdeman to the Erdős–Selfridge function v(n,k). Every obtained source that
mentions v₁ still calls it open. That includes one written 23 years after Langevin 1981: Guy,
UPINT 3rd ed. (2004), B27. Two sources on the task list could not be obtained: [Er98], p. 178 and
the Shorey–Tijdeman 1986 book (see §3). So the verdict cannot be NOT_FOUND in the strict sense.

## 1. Sources obtained, with the closest statement (verbatim)

### 1.1 Guy, UPINT, B27 (task item 1). Obtained, full entry.

**3rd edition (2004).** Unrestricted OCR text of the Springer 3rd edition (title page: "Third
Edition"). Source: archive.org item `collection-of-mathematics-books-number-theory`, file
"Unsolved Problems in Number Theory ( PDFDrive )_djvu.txt", p. 126. The entry is below with OCR
errors fixed: "vi/v;/v1" became v₁ or v_l, "n+72/n+7" became n+i, and "u(n;k)" became v(n;k).
One subscript is uncertain: the OCR "define vi(n) … over k > 1" could be v_l with k ≥ l, or v₁
with k ≥ 1. The sentence in bold is clean in the OCR apart from the subscript glyph.

> "B27 The number of prime factors of n+k which don't divide n+i, 0≤i<k.
> Erdős & Selfridge define v(n;k) as the number of prime factors of n+k which do not divide n+i
> for 0 ≤ i < k, and v₀(n) as the maximum of v(n;k) taken over all k ≥ 0. Does v₀(n) → ∞ with n?
> They show that v₀(n) > 1 for all n except 1, 2, 3, 4, 7, 8 and 16. More generally, define v_l(n)
> [OCR: "vi(n)"] as the maximum of v(n;k) taken over k ≥ l [OCR: "k > 1"]. Does v_l(n) → ∞ with n? **They are unable to prove even
> that v₁(n) = 1 has only a finite number of solutions. Probably the greatest n for which v₁(n) = 1
> is 330.** They also denote by V(n;k) … Does V₁(n) = 1 have only a finite number of solutions?
> Perhaps n = 80 is the largest solution. What is the largest n such that V₀(n) = 2? Some further
> problems are given in their paper."
> References: "P. Erdős & J. L. Selfridge, Some problems on the prime factors of consecutive
> integers, Illinois J. Math., 11(1967) 428-430. A. Schinzel, Unsolved problem 31, Elem. Math.,
> 14(1959) 82-83. OEIS: A059756-059757."

Guy cites no Langevin, RST or Tijdeman paper in B27. RST appear only in B32 (Grimm), with
Langevin's SDPP 1976/77 note: "Ramachandra, Shorey & Tijdeman proved, under the hypothesis of
Schinzel mentioned in A2, that there are only finitely many exceptions to Grimm's conjecture."

**2nd edition (1994).** Item `unsolvedproblems0000guyr`, lending-restricted, read through FTS
snippets only. The wording is the same: "They are unable to prove even that v₁(n) = 1 has only a
finite number of solutions. Probably the greatest n for which v₁(n) = 1 is 330."

### 1.2 Langevin, *Acta Arith.* 39 (1981) 241–249 (task item 4). All 9 pages now read.

Pass A read pp. 241–245 and 248–249. This pass also read pp. 246–247, and re-read p. 242 and the
bibliography on p. 249. Source: matwbn scan aa3932.pdf.

* The only Erdős–Selfridge citation is [1], "P. Erdős et J. L. Selfridge, *Some problems on the
  prime factors of consecutive integers, II*, Proc. Washington St. Univ. Conf. on Number Theory,
  Pullman (Wash.), 1971, p. 13–21". It is cited for the Grimm/Hall-type Lemma 1 (p. 242): "Le lemme
  suivant généralise un résultat d'Erdős et Selfridge ([1], s'y reporter pour l'historique du
  problème)". Lemma 1 (p. 243) reads: "Soient des entiers tels qu'aucun d'entre eux ne divise le
  plus petit commun multiple (ppcm) des autres, alors, il existe des nombres premiers distincts les
  divisant respectivement."
* ErSe67 (the v-function paper) is **not** cited. The paper has no v(n,k), v₁, or "two prime
  factors > k" statement.
* On (8), p. 242: "(8) généralise un résultat dérivé par Tijdeman ([14]), quand a = 1, valable dans
  le domaine partiel n ≥ exp(k^{ε'}) …, de travaux de Shorey ([12]) et Ramachandra ([7])". Here
  [14] is "R. Tijdeman, Math. Rev., 54, n° 1, 7/1977, 246", an MR review that I did not obtain
  (§2).

### 1.3 Langevin's own seminar papers (task item 4). Numdam bibliographies obtained.

| Paper | Numdam item | Erdős–Selfridge citations |
|---|---|---|
| "Sur la fonction plus grand facteur premier", SDPP 16 (1974/75) G22, 29 pp. | SDPP_1974-1975__16_2_A18_0 | 68 entries. Only ErSe71 II ([14]) and Ramachandra's "Application of Baker's theory to two problems considered by Erdős and Selfridge" ([41]). Not ErSe67. |
| "Méthodes élémentaires en vue du théorème de Sylvester", SDPP 17 (1975/76) G2 | SDPP_1975-1976__17_2_A9_0 | 8 entries; none by Erdős–Selfridge. |
| "Plus grand facteur premier d'entiers en progression arithmétique", SDPP 18 (1976/77) no. 3 | SDPP_1976-1977__18_1_A3_0 | 13 entries; none by Erdős–Selfridge. |
| "Facteurs premiers d'entiers en progression arithmétique", SDPP 19 (1977/78) no. 4 (announces the 1981 paper) | SDPP_1977-1978__19_1_A3_0 | 15 entries; RST I/II, no Erdős–Selfridge. |
| "Facteurs premiers des coefficients binomiaux", SDPP 20 (1978/79) no. 27 | SDPP_1978-1979__20_2_A4_0 | 11 entries (Erdős ×3, Langevin ×8); no Selfridge. |

The Ramachandra 1973/74 paper, J. Indian Math. Soc. 37, 25–34 (zbMATH review 0326.10038 by
Ramachandra), treats Grimm's g(n) and P((u+1)…(u+k)), not v: "The first problem concerns the maximum
number g=g(n) such that it is possible to select prime factors p₁,…,p_g of (n+1),…,(n+g) … Another
application is to prove that … the greatest prime factor of (u+1)…(u+k) is ≫ …".

### 1.4 Papers citing Langevin 1981 (task item 4)

Citation databases:
* zbMATH `ci:0396.10033`: 1 hit, Shorey–Tijdeman, Acta Arith. 53 (1989/90).
* OpenAlex: 1 citation. Semantic Scholar: 1, Tijdeman, RIMS 1989.
* OpenCitations: 1, the 2011 Springer chapter "The Thirties" by Narkiewicz.
* zbMATH has no review text for the 1981 paper. Google Scholar "cited by" was unavailable.

Further citers found by archive.org FTS: *A Tribute to Paul Erdős* (1990) and the Luminy 1990
proceedings (1992).

| Citer | Access | Closest statement / result |
|---|---|---|
| Shorey–Tijdeman, "On the greatest prime factor of an arithmetical progression (II)", Acta Arith. 53 (1990) 499–504 | matwbn aa5356.pdf; pp. 499–501 and 504 (references) read | Cites Langevin only for P(Δ) bounds: "Also, Langevin [3] obtained results which imply that … P > C₁k loglog a if a > k^r". Five references; no Erdős–Selfridge. |
| Tijdeman, "On the product of the terms of a finite arithmetic progression", RIMS Kôkyûroku 708 (1989) 51–62 | kurims PDF 0708-06, OCR layer, whole text | Cites Langevin 1981 as [5] only in: "Shorey and I improved upon some estimate of Langevin [5]" (P(Δ) ≫ k loglog χ). Its only Erdős–Selfridge item is the 1975 "never a power" paper. No v. |
| Narkiewicz, *Rational Number Theory in the 20th Century* (2012) | FTS snippets only (restricted) | "…given by D. Hanson [2500] and M. Langevin [3709, 3710] (who also dealt with the same problem for products of terms of an arithmetic progression)", about Sylvester's theorem. FTS finds no "Some problems on the prime factors" (ErSe67/71) in the book. |
| Shorey–Tijdeman, *A Tribute to Paul Erdős* (1990) | FTS snippets only | Langevin is cited for Sylvester-type P > k results: "For such results we refer the reader to Langevin [5, 6, 7, 8]". FTS finds no ErSe67 title in the volume. |
| Luminy 1990 proceedings (1992): Langevin, "Partie sans facteur carré d'un produit d'entiers voisins", and ST, "…arithmetical progression III" | FTS snippets only | "Selfridge" has **0** FTS hits anywhere in the volume. |

### 1.5 Shorey–Tijdeman surveys and the Grimm literature (task item 3)

**Shorey–Tijdeman, "Arithmetic properties of blocks of consecutive integers", arXiv:1612.05438**
(in *From Arithmetic to Zeta-Functions*, Springer 2016). Full LaTeX source read.
* §4.2 (number of distinct prime factors): "Ramachandra et al. [rst] proved that there exists a
  constant c₄>0 such that for n > exp(c₄(log k)²), ω(n,k) > k. Shorey and Tijdeman ([st92],
  Theorem 5) showed that there exists a constant c₅>0 such that for k>c₅, n> exp₂(c₅k),
  ω(n,k) > k + π(k)−2."
* Langevin is cited only for P(n,k) and abc results. Langevin 1981 does not appear in its
  bibliography.
* Its Erdős mentions are Erdős–Graham, Erdős–Woods and Erdős's combinatorial argument. There is no
  Erdős–Selfridge v and no smooth-term count.

**Shorey–Tijdeman, "Some Methods of Erdős Applied to Finite Arithmetic Progressions"**, in *The
Mathematics of Paul Erdős I* (2nd ed. 2013; 1st ed. 1997). Unrestricted OCR text (archive.org
`springers-collection-of-books`, "The Mathematics of Paul Erd_s I ( PDFDrive )_djvu.txt").
* Its summary centres on Erdős–Selfridge 1975 ("the product of two or more consecutive positive
  integers is never a perfect power").
* Langevin is cited only for "Langevin [14] proved that P(Δ(a,d,k)) > k for χ > k" (SDPP 1976/77).
* Its bibliography lists no ErSe67 and no Langevin 1981.
* Neither volume I nor volume II of that book contains "v(n,k)", "v(n;k)" or "v₁(n)".

**Shorey–Tijdeman, "On the number of prime factors of a finite arithmetical progression"**, Acta
Arith. 61 (1992) 375–390 (matwbn aa6146.pdf, text layer). It covers d > 1 progressions. Its 11
references include RST I but not Langevin or Erdős–Selfridge.

**Laishram–Murty, "Grimm's conjecture and smooth numbers"**, Michigan Math. J. 2012
(arXiv:1306.0765, source read). It cites ErSe71 only for Grimm consequences ("That this is a
difficult conjecture having several interesting consequences was first pointed out by Erdős and
Selfridge"). No Langevin, no v.

**Laishram–Shorey, IJNT 2 (2006).** zbMATH review only: a computational Grimm check. Not
obtained in full.

### 1.6 Other obtained reference works

**Sándor–Mitrinović–Crstici, *Handbook of Number Theory I*** (full OCR).
* §XII.14.2(c): with f(n,k) = #{n+i with a prime factor > k}, "If n > exp(c(log k)³), then
  f(n,k) = k − π(k)", credited to RST.
* §V.17(b) cites ErSe67 only for "liminf Σ_{i<k} ω(n+i) ≥ k + π(k) − 1".
* There is no v₁ statement and no link to Langevin 1981. Langevin appears only in §§IV.7 and IV.19,
  for P bounds.

***Handbook of Number Theory II*** (full OCR): nothing relevant.

**MathOverflow / Math.SE** (StackExchange API). No hits for Erdős–Selfridge v₁. The only
Langevin hit (MO 262400) concerns Sylvester–Schur smooth-number injections, not v.

**Archive-wide FTS** for "unable to prove even", "v(n;k)", "prime factors of n + k which" and
"greatest n for which": the only relevant hits are Guy (1994, 2004, and a Chinese translation of
Guy).

### 1.7 Kitamura repository and the erdosproblems.com thread (task item 5). Re-checked 2026-09-25 ~14:35Z.

**erdosproblems.com/forum/thread/889.** Still 2 comments and "Proof claims (0)"; the page was last
edited 02 Jan 2026. Kitamura (22 Sep 2026): "It does not solve the main lowercase-v₀(n)→∞ problem
displayed on this page, the lowercase-v₁ finite-exception problem, or the stronger prediction that
80 is the largest capital-V₁ exception." No comment mentions Langevin, RST or Tijdeman.

**KitaKen1/erdos-889-capital-v1-finite.**
* Still 3 commits, all on 2026-09-22 (last 03:15Z).
* README, line 15: "It does **not** prove the main problem `Erdos889.erdos_889`, the lowercase-v₁
  finite-exception variant, or the conjecture that the largest capital-V₁ exception is 80."
* The Lean header reads "This proves finiteness, not the lowercase-v divergence problem …". There
  is no Langevin citation.

**Other GitHub activity.**
* GitHub search for "erdos 889" finds only the three repositories already known.
* vikktorrz/erdos-889-prime-power `paper/main.tex` is about capital V₁ only and contains no
  Langevin, Tijdeman or Shorey.
* formal-conjectures `main`, 889.lean line 87: `erdos_889.variants.v1_eq_1_finite` is still
  `@[category research open]`.
* The FC PR search for "889" shows no lowercase-v₁ PR; #6453 (capital V₁) is open with 0 comments.

## 2. Sources not obtained. I have not guessed at their contents.

| Source | Why it matters | What was tried |
|---|---|---|
| **[Er98] Erdős, "Some of my new and almost new problems and results in combinatorial number theory", *Number theory (Eger, 1996)*, de Gruyter 1998, 169–180, p. 178** (DOI 10.1515/9783110809794.169; MR 1628841) | The only post-1981 Erdős source for #889. | de Gruyter (HTTP 202/405), renyi Erdős archive (no 1990s PDFs), archive.org metadata and FTS (title found only in MR 2000 indexes and bibliographies), Google Books (blocked). Indirect evidence: erdosproblems.com, which cites [Er98, p.178], still presents v₁ as open ("could not even prove that v₁(n) ≥ 2 for all large n"). That is Bloom's summary, not Erdős's text. |
| **Shorey–Tijdeman, *Exponential Diophantine Equations*, Cambridge Tracts 87 (1986)** | The main monograph on the Baker-method consecutive-integer results. | Cambridge Core gives the chapter TOC and only the first page of Ch. 1 "Purely exponential equations" (pp. 40–55; p. 40 read: Tijdeman's S-unit gap theorem, Cassels's corollary). No chapter of the book is devoted to products of consecutive integers. Crossref has no reference list. Not on archive.org. |
| Tijdeman's MR review, "Math. Rev. 54, n° 1, 7/1977, 246" (Langevin's ref. [14]) | Tijdeman derived the a = 1 smooth-count bound here, per Langevin. | MathSciNet is not accessible; archive.org MR issues stop in the 1960s. |
| MR 83f review of Langevin 1981 | A reviewer might have noted the consequence. | Only the MR 1983 index is on archive.org, not the issue itself. zbMATH has no review. |
| Saradha–Shorey, Acta Arith. 99 (2001) 363–388; Laishram PhD thesis (TIFR 2007); Laishram–Shorey IJNT 2006 (full text) | Secondary surveys on consecutive-integer results. | matwbn does not cover AA 99; the thesis was not found without web search; IJNT is paywalled. Their topics are perfect powers and Grimm, so the relevance is low. |
| Full text of Narkiewicz 2012, *A Tribute to Paul Erdős* (1990), and the Luminy 1990 proceedings | Citers of Langevin 1981. | Lending-restricted. Read through targeted FTS snippet probes only; results in §1.4. |
| Google Scholar "cited by" for Langevin 1981 and ErSe67 | Broad citer coverage. | Blocked (JavaScript/CAPTCHA). OpenAlex, Semantic Scholar, OpenCitations and zbMATH were used instead. Each lists at most one citer of Langevin 1981. |

## 3. Assessment

* No obtained source states the corollary, and none connects Langevin's o(π(k)) bound on k-smooth
  terms (1981, Corollaire 1 (8)) with the Erdős–Selfridge function. Every citer and survey I
  obtained uses Langevin 1981 only for lower bounds on P(Δ), the greatest prime factor. Langevin's
  own bibliographies cite Erdős–Selfridge 1971 (Grimm), never ErSe67.
* The latest authoritative problem-book entry, Guy 2004 B27, repeats ErSe67's "unable to prove
  even that v₁(n) = 1 has only a finite number of solutions" and cites no post-1967 work. So Guy did
  not know of the link as of 2004.
* The two unobtained items, [Er98] and the ST 1986 book, are why the verdict is INCONCLUSIVE rather
  than NOT_FOUND. Before any public priority claim, one of them should be checked from a library or
  institutional copy: [Er98] p. 178 first, then the ST book's Ch. 1 notes. It would also help to get
  Tijdeman's MR 54 review, which is cited as the source of the a = 1 smooth-count bound.
