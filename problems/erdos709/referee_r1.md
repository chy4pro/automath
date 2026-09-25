# Referee report — Erdős #709, engine transcript `engine/harvest/erdos709_pro_r1_raw.md`

Referee: Opus (strict mode). Date 2026-09-04.
Convention used throughout (as in the transcript): `f(n)` is the least **positive integer** k such
that for every A ⊆ [2,∞)∩ℕ with |A| = n and every interval I of exactly k·max(A) consecutive
integers there is an SDR (distinct x_a ∈ I with a | x_a). Monotonicity in k is automatic (a longer
window contains a shorter one), so "f(n) ≤ k" ⟺ "the property holds at k".

Notation: m = max(A); I = {x+1,…,x+km}; J_j = {x+(j−1)m+1,…,x+jm} (1 ≤ j ≤ k);
for B ⊆ A, U_j = {y ∈ J_j : ∃a∈B, a|y}, s_j = |U_j|, r = |B|, N_I(B) = Σ_j s_j.

---

## 0. Summary table

| Claim | Verdict | Severity of defect |
|---|---|---|
| Lemma 1 (up-closure) | PASS | — |
| Lemma 2 (fractional = integral, A2 refuted) | PASS (standard) | — |
| **Lemma 3** (boundary injection r ≤ s_j s_{j+1}) | **PASS** | — (boundary case a\|c_j checked) |
| **Lemma 4** (even k) | **PASS**, and sharp | — |
| **Lemma 5** (odd k) | **PASS** | GAP-minor: inequality (1) is a proof *sketch*; full induction supplied below |
| **Theorem 6** (f(n) ≤ K(n) ≤ ⌈√n⌉) | **PASS** | GAP-trivial: k = 1 not covered by L4/L5 |
| Lemma 7 (layered-line CRT embedding) | PASS | — (all four boundary inequalities check out) |
| Corollary 8 (sharpness of L3) | PASS | — |
| **Lemma 9** (monotonicity) | **PASS** | — (needs "d large enough"; the transcript says so) |
| **Lemma 10** (f(n) ≥ 2) | **PASS** | — |
| **Lemma 11** (f(6) > 2) | **PASS** | — (verified two independent ways) |
| **Theorem 12** (f(1)=1, f(2..5)=2, f(6..9)=3) | **PASS** | — |
| **Lemma 13** (f(19) ≥ 4) | **PASS** | — (fully re-derived and re-verified) |
| Lemma 14 (crossing barrier t−1 < (32r)^{1/3}) | PASS | — |
| Prop 16 / 17 (conditional) | PASS (trivial arithmetic) | — |

**Overall: PASS.** No mathematical error was found in any claim. Two write-up gaps (both
repairable in a few lines, neither affecting truth) are recorded. The main reservation is
**novelty, not correctness** — see §4.

---

## 1. Detailed verification of the proofs

### Lemma 3 (r ≤ s_j s_{j+1}) — PASS
c_j = x + jm is the *right endpoint* of J_j and the *left neighbour* of J_{j+1}.
ℓ_j(a) = a⌊c_j/a⌋, r_j(a) = ℓ_j(a) + a.

* **ℓ_j(a) ∈ J_j.** Upper: ℓ_j(a) ≤ c_j = x+jm ✔ (J_j contains its right endpoint c_j).
  Lower: ℓ_j(a) > c_j − a ≥ c_j − m = x+(j−1)m, so ℓ_j(a) ≥ x+(j−1)m+1 ✔. Uses a ≤ m, true for
  all a ∈ B ⊆ A.
* **Boundary case a | c_j** (explicitly requested): then ℓ_j(a) = c_j ∈ J_j ✔ (right endpoint,
  included), and r_j(a) = c_j + a ≥ c_j + 1 ∈ J_{j+1} ✔. No off-by-one.
* **r_j(a) ∈ J_{j+1}.** Lower: r_j(a) = ℓ_j(a)+a > c_j so ≥ x+jm+1 ✔. Upper: r_j(a) ≤ c_j + a ≤
  c_j + m = x+(j+1)m ✔.
* Both are multiples of a ∈ B, hence ℓ_j(a) ∈ U_j and r_j(a) ∈ U_{j+1}.
* Injectivity: a = r_j(a) − ℓ_j(a) recovers a ✔.

Hence r ≤ s_j s_{j+1} for every 1 ≤ j < k. The proof is valid for arbitrary integer x (also
negative windows, where 0 may be a common multiple — the floor-based definitions still work).
Nothing is assumed about gcd's, lcm's, or the size of a beyond a ≤ m. **Correct.**

### Lemma 4 (k = 2h even) — PASS, and provably sharp
Disjoint boundary pairs (s_1,s_2),(s_3,s_4),…,(s_{2h−1},s_{2h}) use boundaries j = 1,3,…,2h−1,
all < k ✔. Each gives s_{2i−1}s_{2i} ≥ r, hence s_{2i−1}+s_{2i} ≥ 2√r, and by integrality
≥ ⌈2√r⌉ ✔. Summing: Σ s_j ≥ h⌈2√r⌉.
* r ≤ 4h²: h⌈2√r⌉ ≥ 2h√r ≥ √r·√r = r ✔ (2h ≥ √r).
* 4h² < r ≤ 4h²+h: 2√r > 4h and 4h ∈ ℤ ⟹ ⌈2√r⌉ ≥ 4h+1, and h(4h+1) = 4h²+h ≥ r ✔.
Note s_j ≥ 1 is needed and follows from r ≥ 1 with r ≤ s_j s_{j+1}. R(2h) = 4h²+h = k²+k/2 ✔.
**Numerically confirmed sharp** (see §2, CHECK D): for k = 2,4,6,8 the exact threshold of the
path relaxation is *exactly* k²+k/2.

### Lemma 5 (k = 2h+1 odd, h ≥ 1) — PASS; inequality (1) is a sketch
Substitution x_i = s_{2i+1} (0≤i≤h), y_i = s_{2i} (1≤i≤h) is consistent: y_i is adjacent to
x_{i−1} and x_i via boundaries j = 2i−1 and j = 2i, and 2i ≤ 2h = k−1 ✔. So
y_i ≥ r/min(x_{i−1},x_i) ✔.

**Inequality (1): Σ_{i=1}^h min(x_{i−1},x_i) ≤ (h/(h+1))·Σ_{i=0}^h x_i.**
The transcript's argument is correct but compressed; here is the full induction (on the number of
vertices of the path), which I verified line by line:
1. *Shift invariance.* Let μ = min_i x_i and x_i ← x_i − μ. LHS drops by exactly hμ (each of the h
   min-terms drops by μ since both arguments are ≥ μ). RHS drops by (h/(h+1))·(h+1)μ = hμ.
   So the inequality is **invariant**, not merely weakened — this is the crux and it is exact.
2. After shifting, some x_p = 0, so both min-terms incident to index p vanish. The path splits
   into the sub-path on {0,…,p−1} (p vertices, p−1 edges) and on {p+1,…,h} (h−p vertices,
   h−p−1 edges); edge count (p−1)+(h−p−1)+2 = h ✔ (with the obvious degeneration when p = 0 or h).
3. Induction gives each part ≤ (q/(q+1))·(part sum) with q ≤ h−1 < h, and q/(q+1) ≤ h/(h+1);
   the part sums add up to the total (x_p = 0). Base case: one vertex, no edges, 0 ≤ 0 ✔.
**Severity: minor / editorial.** The claim is true (exhaustively and randomly verified, §2 CHECK C);
a Lean formalisation would need the above spelled out, exactly as §15 of the transcript says.

Remaining chain: AM–HM (Cauchy–Schwarz) Σ 1/min ≥ h²/M_x ≥ h(h+1)/O (needs M_x > 0, true since
s_j ≥ 1) ✔; E ≥ r·h(h+1)/O ✔; O + rh(h+1)/O ≥ 2√(rh(h+1)) = √(4h(h+1)r) = √((k²−1)r) ✔.

**Case r = k² (explicitly requested).** For r ≤ k²−1, √((k²−1)r) ≥ √(r·r) = r ✔. For r = k²:
Σ s_j ≥ k√(k²−1), and k²(k²−1) − (k²−1)² = k²−1 > 0 gives k√(k²−1) > k²−1; Σ s_j is an integer,
hence ≥ k² = r ✔. **Correct, including the integrality step.**

### Theorem 6 — PASS with one trivial gap
For k = K(n) and any B ⊆ A: r = |B| ≤ n ≤ R(k); Lemma 3 supplies all path constraints; Lemma 4/5
give Σ_j s_j ≥ r, i.e. |N_I(B)| ≥ |B|; Hall ⟹ SDR ✔. The blocks J_j are disjoint so
N_I(B) = Σ s_j *exactly* ✔.
* **GAP (trivial):** Lemma 4 needs k ≥ 2 and Lemma 5 needs k = 2h+1 ≥ 3, so **k = 1 is not covered**
  by the quoted lemmas. K(n) = 1 only for n = 1, where the statement is immediate (a window of
  length a contains exactly one multiple of a). One sentence fixes this. Severity: trivial.
* K(n) ≤ ⌈√n⌉: with k = ⌈√n⌉, R(k) ≥ k² ≥ n in both parities ✔. R(1..6) = 1,5,9,18,25,39 ✔
  (transcript's list is correct); R is increasing.

### Lemma 9 (f nondecreasing) — PASS
Scaling: I = {x+1,…,x+km} ↦ I′ = {dx+1,…,dx+kdm}, A ↦ dA. |I′| = kdm = k·max(dA) ✔ — the window
length is exactly k times the *new* maximum, as required. dz ∈ I′ ⟺ x+1 ≤ z ≤ x+km ⟺ z ∈ I
(z ∈ ℤ) ✔, and every multiple of da is a multiple of d, so N_{I′}(dB) = d·N_I(B), same
cardinality ✔ — deficiency is preserved exactly.
**Padding (explicitly requested):** one needs N−n further integers in [2, dm] \ dA — they exist
because |[2,dm]| − n = dm − 1 − n ≥ N − n once dm ≥ N+1, and d is free ("选足够大的 d" in the
transcript covers this, though the explicit inequality dm ≥ N+1 is not written out). New elements
are ≤ dm so max(A′) = dm is unchanged, and adding elements to A cannot shrink N_{I′}(dB), so dB
stays deficient ✔. **Correct.** (Independently reproduced on the f(6) instance, §2 CHECK H.)

### Lemma 10 (f(n) ≥ 2 for n ≥ 2) — PASS
A = {n+1,…,2n}, |A| = n, max = 2n = m, I = {C−n+1,…,C+n} of length 2n = 1·max(A) ✔. Every a ∈ A
satisfies a > n, so consecutive multiples are > n apart while I has radius n around C; C ∈ I is a
multiple of every a, and C±a ∉ I ✔. So N_I(A) = {C}, |N| = 1 < n ⟹ Hall fails at k = 1 ✔.
Verified numerically for n = 2..8.

### Lemma 11 (f(6) > 2) — PASS
A = {71,80,83,91,92,100}, m = 100, c = 2 436 242 840, I = {c−99,…,c+100}: exactly 200 = 2·max(A)
consecutive integers ✔. Brute force over all 200 integers (my own code, §2 CHECK A) gives
neighbourhood offsets exactly {−40,−31,+40,+52,+60}, |N_I(A)| = 5 < 6, and the maximum bipartite
matching is 5. The residues in the transcript's table (31,40,31,31,40,40) are correct, and for
each a the *next* multiple on either side is outside the window (offsets −102,−120,−114,−122,−132,
−140 and +111,+120,+135,+151,+144,+160). Hall fails for B = A ⟹ f(6) > 2 ✔.

### Theorem 12 — PASS
f(1) = 1 (K(1)=1, and f ≥ 1 by definition); f(n) = 2 for 2 ≤ n ≤ 5 (T6 with R(2)=5, plus L10);
f(n) = 3 for 6 ≤ n ≤ 9 (T6 with R(3)=9, plus L11 + L9 monotonicity) ✔. All arithmetic checked.

### Lemma 13 (f(19) ≥ 4) — PASS, fully re-derived
I rebuilt the construction from the printed data (§2 CHECK F) and verified:
* 19 rows, 19 **distinct** slopes d; each row is a genuine 3-term AP (d = y−ℓ, r = 2y−ℓ) ✔.
* every ℓ ∈ L, y ∈ Y, r ∈ R with |L| = |Y| = |R| = 6, total **18 designated points** ✔.
* max|d_i − d_j| = 97 exactly, matching Q = lcm(1,…,97); the printed value of Q is correct ✔.
* a_d = (431+d)Q+1 = M + Q(d−32); moduli distinct, all ≥ 2, **pairwise coprime** (any common
  factor g divides Q(d−e) and is coprime to Q since a_d ≡ 1 mod Q, so g | |d−e| ≤ 97 | Q, g = 1) ✔.
* max(A) = M is attained at d = 32, so the window length 3M is **exactly 3·max(A)** ✔ (requested).
* u,v,w are consecutive multiples: v−u = w−v = a_d ✔; layers separated mod Q (u ≡ 0, v ≡ 1,
  w ≡ 2 mod Q), so the 18 points really are 18 distinct integers ✔.
* **No fourth multiple in the window** (requested). Since a_d ≥ 366Q+1 and |I| = 3M = 1389Q+3, a
  window *could* a priori hold 4 multiples (1389/366 ≈ 3.79). The proof rules this out correctly:
  multiples form an AP, so it suffices that u−a ≤ 0 and w+a > 3M. I checked both with margins:
  (u−a)/Q ≤ −73 (comfortable) and (w+a−3M)/Q ≥ **1**, i.e. the right-hand inequality holds with
  slack exactly one Q — it needs min(r+d) = −134 > −136 and is therefore **tight but valid**. My
  direct enumeration of the multiples of every a_d inside {x+1,…,x+3M} returns exactly 3 per
  modulus and exactly {u,v,w}. Union = 18 < 19 ⟹ f(19) ≥ 4 ✔.
* CRT is legitimate (pairwise coprime moduli), x ≥ 0 chosen, so the window is inside ℕ ✔.

### Lemma 7 / Corollary 8 / Lemma 14 (contextual, checked anyway) — PASS
* **L7.** I implemented the construction from the statement alone and ran it (§2 CHECK E). All four
  required inequalities hold with the transcript's constants: block membership needs
  C − R ≥ 1 and Q(C+R) < m (uses C = R+D+1, N = 2R+2D+2); predecessor outside needs
  C+b−N−d′ ≤ −1 ✔; successor outside needs C + b_λ + t·d′_λ > 0, which holds because
  b_λ + (t−1)d′_λ ≥ −R and d′_λ ≥ −D, i.e. exactly the reason C was set to R+D+1 ✔ (this is the
  one step that is *not* covered by "b+jd′ ∈ X′_j" and the transcript's constants handle it).
  Coprimality and max(A) = m ✔.
* **Cor 8.** Slopes 2^{u+j}+2^i are distinct by binary representation (i < u ≤ u+j) ✔; r = uv,
  s_1 = u, s_2 = v gives r = s_1s_2 exactly, so Lemma 3 is sharp at every scale ✔. Executed for
  (u,v) = (2,3),(3,3),(2,4),(3,4): real divisibility instances with |N_I(A)| = u+v are produced,
  giving f(6)>2, f(9)>2, f(8)>2, f(12)>2 — an **independent second proof of Lemma 11's conclusion**.
* **L14.** E ≥ r(t−1) (edges determine their line, so no multi-edges); crossings ≤ C(r,2) < r²/2
  (two lines meet at most once); crossing lemma cr ≥ E³/(64S²) valid for E ≥ 4S. Combining gives
  r(t−1)³ ≤ 32S² ✔, and with S < r, t ≥ 5 ⟹ t−1 < (32r)^{1/3} ✔. Standard and correct; it only
  rules out the *one-point-per-layer straight-line* template, as the transcript honestly states.

---

## 2. Computation

### 2a. Transcript's script `check709_r1.py` (run with python3, exit 0)
```
f6 example neighborhood offsets: [-40, -31, 40, 52, 60] size 5 <6 -> True
  a=71 c mod a=31 / a=80 40 / a=83 31 / a=91 31 / a=92 40 / a=100 40
f19: distinct points 18
f19: union of multiples in the 3M-window has size 18 <19 -> True
ALL CHECKS PASSED
```

### 2b. My independent script `ref709_indep.py` (written from the statements, not their code)
* **CHECK A (Lemma 11, requested brute force).** Direct scan of all 200 integers of the window:
  neighbourhood = {c−40,c−31,c+40,c+52,c+60}, size 5 < 6; max matching = 5. Per-modulus multiple
  lists and the two just-outside multiples printed and confirmed. **PASS.**
* **CHECK B (Lemma 10).** n = 2..8: |N| = 1 < n in every case. **PASS.**
* **CHECK C (path inequality (1)).** Exhaustive for h ≤ 5, x_i ∈ [0,6] (117 649 vectors at h=5)
  plus 200 000 random real vectors with h ≤ 8: **0 violations.**
* **CHECK D (are Lemmas 4/5 valid and sharp?).** Exact DP for
  T(k) := max{ r : min{Σs_j : s_j ∈ ℤ_{≥1}, s_j s_{j+1} ≥ r} ≥ r }:

  | k | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
  |---|---|---|---|---|---|---|---|---|
  | R(k) claimed | 1 | 5 | 9 | 18 | 25 | 39 | 49 | 68 |
  | true T(k) | 1 | 5 | 9 | 18 | **26** | 39 | **51** | 68 |

  R(k) ≤ T(k) always ⟹ **Lemmas 4 and 5 are valid**; Lemma 4 (even k) is **exactly sharp**;
  Lemma 5 (odd k ≥ 5) is slightly lossy (also T(9) = 83 > 81). This is an *improvement
  opportunity*, not an error: using T(k) would give e.g. f(26) ≤ 5 instead of 6. It does not change
  K(n) ≤ ⌈√n⌉ nor any n ≤ 9 value (T(3) = R(3) = 9).
* **CHECK E (Lemma 7 + Cor 8).** Re-implemented; real instances built and their multiples counted
  directly — every modulus has exactly t multiples, |N_I(A)| = |X_0|+|X_1| in all four cases.
* **CHECK F (Lemma 13).** Rebuilt from the rows; all structural, coprimality, CRT and
  multiple-count assertions confirmed independently (details in §1). **PASS.**
* **CHECK G (falsification attempt on Theorem 6).** 12 500 random (A, window) pairs with
  n = 5,6,9 and max(A) ≤ 60/120, window = K(n)·max(A), maximum bipartite matching computed:
  **0 counterexamples.**
* **CHECK H (Lemma 9).** The f(6)>2 instance scaled by d = 2 and padded to n = 7,…,12 with fresh
  moduli ≤ 200: window length stays 2·max(A′) = 400 and the deficient set keeps |N| = 5 < 6.
  So f(n) > 2 for 7 ≤ n ≤ 12 concretely, exactly as Lemma 9 asserts.

### 2c. Brute force `problems/erdos709/f_small.py` (exhaustive, all A ⊆ [2,M], all windows mod lcm A)
```
python3 f_small.py 5 12  ->  f_12(5) = 2 attained at (2,3,4,5,6)      [1.7 s]
python3 f_small.py 9 12  ->  f_12(9) = 2 attained at (2,3,4,5,6,7,8,9,10)  [4.3 s]
```
plus the pre-existing logs f_16(4)=f_24(4)=2, f_12(6)=f_13(6)=2, f_12(7)=2.
**Consistency:** f_M(n) is a lower bound for f(n) restricted to max(A) ≤ M. f_12(5) = 2 is
consistent with (and confirms) f(5) = 2. f_12(9) = 2 is consistent with f(9) ≤ 3 and does *not*
contradict f(9) = 3, because the extremal instances need large max(A) — the transcript's own
f(6) > 2 witness has max(A) = 100, and Corollary 8's f(9) > 2 witness has astronomically large
moduli. No brute-force result contradicts anything in the transcript.

### 2d. Extra probe: is n = 19 the best this 3-layer template can do?
A line of Lemma 13 is (ℓ,y,2y−ℓ) with distinct differences, so the number of lines equals
#{d : Y ∩ (L+d) ∩ (R−d) ≠ ∅}, and f(#lines) ≥ 4 needs #lines > |L|+|Y|+|R|. Annealing search:
sizes (4,4,4)→10, (5,5,5)→14, (5,6,5)→15, (6,5,6)→17, (6,6,6)→**20**, (7,7,7)→25 lines. So
S ≤ 17 never beat S, while S = 18 admits 20 lines (an alternative witness, and dropping one line
re-proves f(19) ≥ 4). Heuristic, not exhaustive, but it suggests **n = 19 is essentially optimal
for this template** — the transcript did not over- or under-claim here.

---

## 3. Gaps, ranked

1. **GAP-minor (write-up), Lemma 5:** inequality (1) is given as a three-line hint. It is *true*
   (proof supplied in §1, verified in §2), but as printed it is not a proof. Must be expanded
   before publication/formalisation.
2. **GAP-trivial, Theorem 6:** k = 1 is outside the range of Lemmas 4 and 5; needs one sentence.
3. **GAP-trivial, Lemma 9:** the explicit smallness condition on the padding (dm ≥ N+1) is implicit
   in "choose d large enough".
4. **Not a gap, but a missed improvement:** R(k) is not the optimal threshold of the transcript's
   own path relaxation for odd k ≥ 5 (T(5)=26, T(7)=51, T(9)=83 vs 25,49,81).
5. **Presentation:** Lemma 13's right-boundary inequality holds with slack exactly 1·Q. Correct,
   but any future edit of the row table must re-check min(r+d) > −136.

No claim in the transcript is false. No claim is over-stated relative to its proof; the document is
explicit that T1 and T3 are unresolved and that Prop 16/17 are conditional. This is a low-hype,
self-consistent write-up.

---

## 4. Novelty assessment (what I actually know; nothing fabricated)

**What is definitely known before this transcript.**
* erdosproblems.com/709 (local copy `scratchpad/ep_709.html`, last edited 23 Mar 2026) states the
  problem is **open**, credits (log n)^c ≪ f(n) ≪ n^{1/2} to Erdős–Surányi **[ErSu59]**, and records
  the improved lower bounds log n/log log n (via van Doorn [vD26] and #711) and √(log n/log log n)
  (via [ErPo80]). Terence Tao's forum comment there also records that the Erdős–Surányi lower-bound
  exponent is c = 1 − (1+log log 2)/log 2 ≈ 0.086.
* **Per the coordinator: arXiv:2603.28636 (van Doorn, Li, Tang, 30 Mar 2026) settles Erdős #650**:
  for windows of length 2·max(A) the guaranteed matching number is exactly min(m, ⌈2√m⌉); their
  lower bound is Hall + two-block boundary injection, their upper bound is f(st) ≤ s+t by CRT.
  I have not read that paper (offline); I take the coordinator's description as given.

**Consequences for this transcript.**
* **Lemma 3 with k = 2 is known** — it is exactly their lower-bound step.
* **Corollary 8 is (the k = 2 case of) their upper-bound construction**: r = uv lines on two layers
  with u+v points is precisely "f(st) ≤ s+t". Lemma 7 is the t-layer generalisation of the same CRT
  packing; the generalisation is routine, and I would not claim it as new without a literature check.
* **Theorem 12's k = 2 content is known.** min(m,⌈2√m⌉) = m ⟺ m ≤ 5, so "f(n) = 2 exactly for
  2 ≤ n ≤ 5" and "f(6) > 2" are immediate corollaries of the March 2026 paper. **Lemma 11 is
  therefore a new small *witness* (max(A) = 100, human-checkable) for an already-known fact.**
  Corollary 8 with (u,v) = (2,3) reproves it inside the transcript itself.
* **What may be new:** the **k-block extension** — Lemmas 4/5, the threshold R(k), Theorem 6 in the
  form f(n) ≤ K(n), the explicit constant 1 in f(n) ≤ ⌈√n⌉, the exact values f(6..9) = 3, and
  f(19) ≥ 4 (a 3-layer construction; #650's paper is about 2 layers).
* **Is f(n) ≤ ⌈√n⌉ what Erdős–Surányi proved?** I do not know and cannot check: [ErSu59] is not in
  this workspace and I have no network access to it. The honest statement is: *the exponent 1/2 is
  theirs (1959); the implied constant they obtained is unknown to me.* Given that the k = 2 case of
  the identical argument is the published state of the art as of March 2026, and given that the
  boundary-injection step is described in the transcript itself as "the real core of the classical
  square-root bound", **I would assume the method is classical and only the explicit bookkeeping
  (R(k), K(n), constant 1, the values at n ≤ 9 and n = 19) is potentially new.** A literature check
  of [ErSu59] and of arXiv:2603.28636 (does it remark on k ≥ 3?) is **mandatory before any
  publication claim.** The transcript itself never claims a new theorem — it says "重建 √n 上界"
  ("reconstruct the √n upper bound") and "this does not change the n^{1/2} exponent".
* **Nothing here touches the actual open problem** (improving the exponent or proving a polylog
  upper bound). T1 and T3 remain open; the transcript says so.

---

## 5. Verdict

* Lemma 3 — **PASS**. Lemma 4 — **PASS (sharp)**. Lemma 5 — **PASS** (one minor write-up gap).
  Theorem 6 — **PASS** (trivial k=1 gap). Lemma 9 — **PASS**. Lemma 10 — **PASS**.
  Lemma 11 — **PASS** (independently brute-forced). Theorem 12 — **PASS**. Lemma 13 — **PASS**
  (independently rebuilt). Lemmas 1, 2, 7, 14, Cor 8, Prop 16/17 — **PASS**.
* **Overall: PASS — mathematically sound, computationally reproducible, honestly scoped.**
* **Publication recommendation: HOLD pending literature check.** The mathematics is correct, but
  the k = 2 slice (Lemma 3, Corollary 8, f(2..5) = 2, f(6) > 2) is already published
  (arXiv:2603.28636, Mar 2026), and the constant in Erdős–Surányi's n^{1/2} is unverified here.
  If [ErSu59] already gives f(n) ≤ ⌈√n⌉ (or better), the only surviving new items are f(6..9) = 3,
  f(19) ≥ 4, and the R(k) bookkeeping — a short note at best, and the R(k) table should first be
  replaced by the exact thresholds T(k) computed in §2 CHECK D.
