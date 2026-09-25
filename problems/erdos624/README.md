# Erdős #624: certified small values of H(n) (checkpoint 1)

This directory holds a small table of exact values of the Erdős–Hajnal set-mapping function H(n)
for two conventions. Every table entry comes with a machine-checkable artefact. Erdős problem #624
asks whether H(n) − log₂ n → ∞. The problem page states that this cannot be settled by a finite
computation, and nothing here bears on the asymptotic question. The only result is the table.

**Credit.** On 18 Sep 2026 herong posted a comment on the erdosproblems.com #624 forum thread
(forum/thread/624, re-read 2026-09-25). It gave H(2..8) = 1, 2, 3, 3, 3, 4, 4 and N(1), N(2), N(3)
= 2, 3, 6, computed with two independently written exhaustive backtracking solvers. It also
reported an explicit 10-point witness for N(4) ≥ 10 (the witness itself was not posted), a short
proof that H(2^m) ≥ m+1 for m ≥ 2, and the restriction argument showing that H is non-decreasing.
Here N(m) = max{n : H(n) ≤ m}. Lemmas P2 and M below are herong's arguments written out again. The
problem page credits the bound H(2^k) ≥ k+1 to Alon. All of herong's values use the Lean /
erdosproblems convention H_L, and they agree with this table.

## 1. Definitions

Write [n] = {0, …, n−1}. For a variant V ∈ {L, EH}, a cell (n, m)_V is *feasible* if a V-map f
exists with the covering property for m. Then H_V(n) = min{m ≥ 0 : (n, m)_V feasible}.

* **H_L (the Lean / erdosproblems convention).** This matches `FormalConjectures/ErdosProblems/624.lean`:
  `ExistsEventuallySurjective n m := ∃ f : Finset (Fin n) → Fin n, ∀ Y, #Y ≥ m → Y.powerset.image f = univ`.
  Here f is defined on **all** subsets of [n], with no condition on f(A). The covering condition is
  {f(A) : A ⊆ Y} = [n] for **every** Y ⊆ [n] with |Y| ≥ m. The Lean file sets H(0) = 0 and otherwise
  takes the sInf. For n ≥ 1 the cell (n, n)_L is feasible (take f({i}) = i), and feasibility is upward
  closed in m, so the sInf is the minimum defined above.
* **H_EH (Erdős–Hajnal 1968, as restated by Gyárfás, "Problems and memories", §3.2).** Here f is a
  *set mapping*: it is defined on the **proper** subsets A ⊊ [n], with f(A) ∈ [n] ∖ A. The covering
  condition is {f(A) : A ⊆ Y, A ≠ [n]} = [n] for every Y ⊆ [n] with |Y| ≥ m. Y = [n] is allowed
  and then A ranges over the proper subsets. With this reading H_EH(n) ≤ n, because f([n]∖{i}) = i
  already covers [n]. Erdős and Hajnal proved log₂ n < H_EH(n).

## 2. Lemmas used (with proofs)

Throughout, n ≥ 1. "Valid" means that f satisfies the variant's value constraint and the covering
condition for the m in question.

**Lemma R (reduction to small sets).** Let 0 ≤ m ≤ n and let D = {A ⊆ [n] : |A| ≤ m}, with [n]
removed from D for EH. Then (n, m)_V is feasible iff some g : D → [n] (with g(A) ∉ A for EH)
satisfies {g(A) : A ∈ D, A ⊆ Y} = [n] for every Y with |Y| = m.
*Proof.* (⇒) Take g = f|_D. If |Y| = m, every A ⊆ Y has |A| ≤ m. For EH, the sets A ⊆ Y with
A ≠ [n] are exactly the members of D below Y, so the two images coincide. (⇐) Extend g to f by
f(A) = 0 (L) or f(A) = min([n]∖A) (EH, A ≠ [n]) outside D. Given |Y| ≥ m, choose Y' ⊆ Y with
|Y'| = m. Then {f(A) : A ⊆ Y (A ≠ [n])} ⊇ {g(A) : A ∈ D, A ⊆ Y'} = [n]. ∎
The CNF encodings and the "direct" method of the witness checker rely on this lemma. The checker's
closure method does not: it checks every Y with |Y| ≥ m against the full table of f.

**Lemma U (monotone in m).** If (n, m)_V is feasible, then so is (n, m+1)_V, using the same f. ∎

**Lemma M (monotone in n; herong's restriction argument).** If (n+1, m)_V is feasible, then so is
(n, m)_V. Hence H_V(n) ≤ H_V(n+1), and infeasibility of (n, m)_V carries over to every larger n.
*Proof.* Let f be valid on [n+1]. For A ⊆ [n] (A ≠ [n] for EH), set g(A) = f(A) if f(A) < n. Otherwise
set g(A) = 0 (L) or g(A) = min([n]∖A) (EH; this set is nonempty because A ≠ [n]). For EH, every such
A is a proper subset of [n+1], so f(A) is defined and f(A) ∉ A, which gives g(A) ∉ A. Now let
Y ⊆ [n] with |Y| ≥ m, and take v ∈ [n]. Validity of f gives v = f(A) for some A ⊆ Y. If A is in the
domain of g, then g(A) = f(A) = v. The only other case is EH with A = [n]. That case cannot give v,
because f([n]) ∉ [n] forces f([n]) = n ≠ v. ∎

**Lemma E (EH ⇒ L).** An EH-valid f, extended by f([n]) := 0, is L-valid. Hence H_L(n) ≤ H_EH(n). ∎

**Lemma C (counting).** If (n, m)_V is feasible, then n ≤ 2^m. If m ≥ n this holds trivially.
Otherwise pick |Y| = m: the image {f(A) : A ⊆ Y} has at most 2^m elements and equals [n]. Hence
H_V(n) ≥ ⌈log₂ n⌉. ∎

**Lemma P2 (powers of two; herong 18 Sep 2026, bound attributed to Alon).** For k ≥ 2, the cell
(2^k, k)_L is infeasible. By Lemmas E and M, (n, k)_V is then infeasible for every n ≥ 2^k and both V.
*Proof.* Suppose f is valid, and take any Y with |Y| = k. Since |2^Y| = 2^k = n and the image is
[n], A ↦ f(A) is a bijection on 2^Y. For distinct x, y ∈ [n], choose Y ⊇ {x, y} with |Y| = k (this
uses k ≥ 2). Then ∅, {x}, {y} ⊆ Y receive three distinct values. So f is injective on the n+1 sets
∅, {x} (x ∈ [n]), which is impossible in [n]. ∎
(For k = 1 the statement is false in L: (2,1)_L is feasible. In EH, (2,1)_EH is infeasible, see §4.)

**Lemma S1 (relabelling).** Let σ and π be permutations of [n], and write π(A) for the image of a set.
(a) L: σ∘f is valid whenever f is. (b) L: A ↦ f(π⁻¹(A)) is valid whenever f is.
(c) EH: A ↦ π(f(π⁻¹(A))) is valid whenever f is.
*Proof.* (a) σ([n]) = [n]. (b) {f(π⁻¹A) : A ⊆ Y} = {f(B) : B ⊆ π⁻¹Y} = [n], and |π⁻¹Y| = |Y|.
(c) This combines (a) and (b) with σ = π. The value constraint is kept because
π(f(π⁻¹A)) ∈ A ⟺ f(π⁻¹A) ∈ π⁻¹A. The domain is kept because π⁻¹A ≠ [n] ⟺ A ≠ [n]. ∎
*Consequence (level sb=1).* One may assume f(∅) = 0. In L, apply (a) with σ(f(∅)) = 0. In EH, apply
(c) with π(f(∅)) = 0.

**Lemma S2-L (singleton normal form, level sb=2, L only).** Suppose (n, m)_L is feasible with n ≥ 2.
Then there is a valid g with g(∅) = 0 whose singleton sequence s_i = g({i}) satisfies s_0 ∈ {0, 1}
and s_{i+1} − s_i ∈ {0, 1} for 0 ≤ i ≤ n−2.
*Proof (one relabelling, no composition of separate lemmas).* Let f be valid and c* = f(∅). Let
v_1, …, v_r be the distinct values of f on singletons, listed so that v_1 = c* if c* is one of them.
Let B_j = {x : f({x}) = v_j}, and let π be a permutation of [n] sending B_1, B_2, … onto consecutive
intervals of [n] in this order. Put δ = 0 if v_1 = c* and δ = 1 otherwise, and prescribe σ(c*) = 0 and
σ(v_j) = j − 1 + δ. These prescriptions agree on c* when δ = 0. They are injective. They land in [n],
since δ = 1 forces r ≤ n − 1. Extend σ to a permutation. Then g(A) = σ(f(π⁻¹A)) is valid by S1(a,b),
and g(∅) = 0. For i in the image of B_j, g({i}) = j − 1 + δ. Since the blocks are consecutive
intervals, s starts at δ, stays constant inside a block and rises by exactly 1 between blocks. ∎

**Lemma S2-EH (singleton breadth-first form, level sb=2, EH only).** If (n, m)_EH is feasible, there
is a valid g with g(∅) = 0 and, for every i ∈ [n],
g({i}) ≤ 1 + max(i, g({0}), …, g({i−1})).
*Proof (one relabelling).* Build an ordering p_0, …, p_{n−1} of [n] and put π(p_k) = k, so every
point receives a label. Start with p_0 = f(∅). For k = 0, 1, …, n−1 in turn: if p_k is still
undefined, let p_k be any unlabelled point, which gets label k. Then, if q_k = f({p_k}) is unlabelled,
give it the next free label. Labels therefore always form an initial segment {0, …, t}. Let t_k be
the largest label in use just before q_k is handled. By induction, t_k = max(k, g({0}), …, g({k−1})),
where g = π·f is valid by S1(c). Then g({k}) = π(q_k) is either an old label (≤ t_k) or t_k + 1, and
g(∅) = π(p_0) = 0. Induction step: after step k the labels are {0, …, max(t_k, g({k}))}. Step k+1
adds label k+1 exactly when k+1 exceeds this maximum, so t_{k+1} = max(k+1, g({0}), …, g({k})). ∎

Each symmetry-breaking level is the normal form of a **single** relabelling lemma: sb=1 is S1, and
sb=2 is S2-L or S2-EH. The clause x(∅, 0) at sb=2 comes from the same relabelling as the singleton
clauses, so no two independent symmetry-breaking arguments are ever composed. The "colour
precedence + point cubes" combination the pilot used is **not** used here. For the two cells whose
archived certificate uses sb=2, the same cell was also solved and LRAT-checked at sb=1 (and (9,4)_EH
at sb=0). Those proofs were checked but not archived because of their size (§4).

## 3. Encoding (src/encode.py) and independent checks

The boolean x(A, c) means f(A) = c. It exists for A ∈ D (Lemma R) and allowed colours c (any c for
L, c ∉ A for EH). Clauses: ALO(A) = ⋁_c x(A,c). AMO(A) is pairwise. COV(Y, c) = ⋁_{A⊆Y} x(A,c) for
|Y| = m. At sb ≥ 1 add the unit x(∅, 0). At sb = 2 add the S2 clauses: for L, x({0},0) ∨ x({0},1)
and ¬x({i},c) ∨ x({i+1},c) ∨ x({i+1},c+1); for EH, ¬x({i},v) ∨ ⋁_{j<i, w≥v−1} x({j},w) for
v ≥ i+2. Variables are numbered with sets sorted by (size, bitmask) and colours ascending.

* `check/check_witness.py` (no code shared with the encoder) reads the **full** table of f on all
  2^n subsets. It checks the value constraint and then the covering condition by two methods. The
  first is a subset-closure recursion over **all** Y with |Y| ≥ m. The second enumerates every
  submask A ⊆ Y directly: for all |Y| ≥ m when 3^n ≤ 2·10⁷, and for |Y| = m otherwise (n = 16, 17).
  With `--selftest` it also flips 40 random values of f and reports how many flips it detects.
  Negative tests: a changed f(∅) on the (11,4)_L witness, a random table, and an EH-violating
  table were all rejected.
* `check/audit_cnf.py` (no code shared with the encoder) rebuilds the full clause set of each UNSAT
  CNF from the definitions and requires **set equality** with the file. A weakened unit clause was
  rejected.
* UNSAT pipeline (`src/certify_unsat.sh`): audit, then CaDiCaL writes a DRAT proof, then drat-trim
  backward-checks it and emits a trimmed LRAT proof. That LRAT proof is checked by **cake_lpr**
  (CakeML-verified checker, arm8 build) and by **lrat-check** (drat-trim repository). The raw DRAT
  is deleted. A corrupted hint and a weakened CNF were each rejected by both checkers.

## 4. Certified table

Status keys: **W** = witness file checked by the independent checker. **LRAT** = cake_lpr and
lrat-check both verified a trimmed LRAT proof of an audited CNF, and the proof is archived.
**lemma** = proved in §2. No cell in the n-ranges below is solver-only.

### H_L(n), n = 1..11, plus the cells 16 and 17

| n | H_L(n) | upper bound (m = H) | lower bound (m = H−1 infeasible) | status | new vs herong 18 Sep |
|---|---|---|---|---|---|
| 1 | 0 | W (1,0) | trivial | W | (n=1 not listed) |
| 2 | 1 | W (2,1) | Lemma C | W + lemma | agrees |
| 3 | 2 | W (3,2) | Lemma C | W + lemma | agrees |
| 4 | 3 | W (4,3) | Lemma P2 (k=2); also LRAT (4,2)_L at sb=0 | W + lemma + LRAT | agrees |
| 5 | 3 | W (5,3) | Lemma C | W + lemma | agrees |
| 6 | 3 | W (6,3) | Lemma C | W + lemma | agrees |
| 7 | 4 | W (7,4) | **LRAT (7,3)_L, sb=2** (also checked at sb=1, not archived) | W + LRAT | agrees |
| 8 | 4 | W (8,4) | Lemma P2 (k=3); or (7,3)_L + M | W + lemma | agrees |
| 9 | 4 | W (9,4) | (7,3)_L + Lemma M | W + LRAT + lemma | herong's N(4) ≥ 10 already gives it |
| 10 | 4 | W (10,4) | (7,3)_L + Lemma M | W + LRAT + lemma | herong's N(4) ≥ 10 already gives it |
| 11 | 4 | **W (11,4)** | (7,3)_L + Lemma M | W + LRAT + lemma | **new**: N_L(4) ≥ 11 (herong expected, without proof, N(4) = 10) |
| 12–15 | 4 or 5 | W (16,5) + Lemma M | (7,3)_L + Lemma M | **undecided**: (12,4)_L open | — |
| 16 | 5 | **W (16,5)** | Lemma P2 (k=4) | W + lemma | new witness |
| 17 | 5 | **W (17,5)** | Lemma P2 + Lemma M | W + lemma | new witness |

So H_L(2^k) = k+1 for k = 2, 3, 4, while H_L(2) = 1 and H_L(1) = 0. Also N_L(1..3) = 2, 3, 6 and
11 ≤ N_L(4) ≤ 15.

### H_EH(n), n = 2..13

| n | H_EH(n) | upper bound | lower bound | status |
|---|---|---|---|---|
| 2 | 2 | W (2,2) | LRAT (2,1)_EH, sb=0; hand proof below | W + LRAT |
| 3 | 3 | W (3,3) | LRAT (3,2)_EH, sb=0; hand proof below | W + LRAT |
| 4 | 3 | W (4,3) | (3,2)_EH + Lemma M (also P2 via Lemma E) | W + LRAT + lemma |
| 5 | 4 | W (5,4) | LRAT (5,3)_EH, sb=0 | W + LRAT |
| 6 | 4 | W (6,4) | (5,3)_EH + Lemma M | W + LRAT + lemma |
| 7 | 4 | W (7,4) | (5,3)_EH + Lemma M | W + LRAT + lemma |
| 8 | 4 | W (8,4) | (5,3)_EH + Lemma M; also Lemma P2 | W + LRAT + lemma |
| 9 | 5 | W (9,5) | **LRAT (9,4)_EH, sb=2** (also checked at sb=0 and sb=1, not archived) | W + LRAT |
| 10 | 5 | W (10,5) | (9,4)_EH + Lemma M | W + LRAT + lemma |
| 11 | 5 | **W (11,5)** | (9,4)_EH + Lemma M | W + LRAT + lemma |
| 12 | 5 | **W (12,5)** | (9,4)_EH + Lemma M | W + LRAT + lemma |
| 13 | 5 | **W (13,5)** | (9,4)_EH + Lemma M | W + LRAT + lemma |

Writing N_EH(m) = max{n : H_EH(n) ≤ m}, this gives N_EH(2), N_EH(3), N_EH(4) = 2, 4, 8 and
N_EH(5) ≥ 13; Lemma P2 caps N_EH(5) at 31. The skeptic's
concern was justified: the pilot had **not** established (11,5)_EH or (12,5)_EH. Both are now
settled by checked witnesses. At the powers of two the table gives H_EH(2^k) = k+1 for k = 1, 2, 3,
i.e. the Erdős–Hajnal lower bound log₂ n < H(n) is attained at n = 2, 4, 8. That is a statement
about these small n only.

Hand proofs of the two smallest EH lower bounds (these are also LRAT-certified):
(2,1)_EH: f({0}) = 1 and f({1}) = 0 are forced. Y = {0} then needs f(∅) = 0, and Y = {1} needs
f(∅) = 1.
(3,2)_EH: f({a,b}) is forced to be the third point, so each pair Y = {a,b} needs
{f(∅), f({a}), f({b})} ⊇ {a, b}. By S1 assume f(∅) = 0. Y = {1,2} forces f({1}) = 2 and
f({2}) = 1. Y = {0,1} then forces f({0}) = 1, and Y = {0,2} is left without the value 2.

## 5. Checkpoint-2 preparation (probes only, each ≤ 30 CPU-min)

No large runs were made. Every probe below hit its CPU cap without an answer, except the two
ansatz runs, whose UNSAT verdicts concern only the restricted ansatz. Exit -24 in `cpu_ledger.csv`
means the process was stopped by the RLIMIT_CPU cap. All probes ran under a 2 GB address-space cap,
with at most 4 solver processes at a time.

| cell | configuration | CPU cap | outcome |
|---|---|---|---|
| (12,4)_L | sb=2, CaDiCaL default | 30 min | undecided |
| (12,4)_L | sb=0, CaDiCaL `--sat` | 20 min | undecided |
| (12,4)_L | sb=2 plus the cube "singletons injective" (f({i}) = i for all i) | 20 min | undecided |
| (12,4)_L | free-orbit Z₁₂ ansatz, f(A+1) = f(A)+1 (SAT search only) | 15 min | ansatz UNSAT in 43 s: no witness of that form |
| (14,5)_EH | sb=1 | 30 min | undecided |
| (14,5)_EH | sb=2 | 30 min | undecided |
| (14,5)_EH | sb=0, `--sat` | 20 min | undecided |
| (14,5)_EH | free-orbit Z₁₄ ansatz | 15 min | undecided |
| (16,5)_EH | sb=1 | 30 min | undecided |
| (16,5)_EH | free-orbit Z₁₆ ansatz | 15 min | ansatz UNSAT in 178 s: no witness of that form |

The cube probe CNF was the sb=2 CNF plus 12 unit clauses x({i}, i), generated inline and not archived.
The free-orbit ansatz is `src/encode.py --ansatz cyc`. It imposes f(A+1) = f(A)+1 (mod n) only on
sets whose rotation orbit is free. It is used only to search for witnesses.

**Undecided cells after checkpoint 1.** (12,4)_L, and hence H_L(12..15) ∈ {4, 5} with
11 ≤ N_L(4) ≤ 15. Also (14,5)_EH, (15,5)_EH and (16,5)_EH, with 13 ≤ N_EH(5) ≤ 31. There is a
sharp jump in difficulty: (13,5)_EH was solved in 0.8 s, but (14,5)_EH resisted about 95 CPU-min
over four configurations.

**Bisection plan (checkpoint 2, proposed cap about 30 CPU-h in total, gated).**
1. *(12,4)_L first.* If it is UNSAT, then N_L(4) = 11 and H_L(12..17) = 5, using the (16,5)_L
   witness and Lemma M, and the L side of the table is finished. If it is SAT, try (14,4)_L next,
   then 13 or 15.
2. *N_EH(5): start at (14,5)_EH.* If it is UNSAT, N_EH(5) = 13. If it is SAT, go to (16,5)_EH and
   then 15. Only after that would (16,5)_EH, the pilot's former target C2, be attacked directly.
3. *UNSAT methods, in this order.* (a) Cube-and-conquer on the singleton pattern. S2-L leaves the
   non-decreasing 0/1-step sequences. A block-size-sorted variant, which must be proved as one
   relabelling lemma like S2, cuts these to at most 2·p(12) = 154 cubes. Coverage of the cubes is
   itself checked by one small LRAT proof (the S2 clauses plus the negated cube disjunction are
   UNSAT), and each cube gets its own LRAT proof. The injective cube alone did not finish in 20
   CPU-min, so the first step is to time a handful of cubes split one level deeper (pair values)
   before committing any budget. (b) Redundant counting clauses per m-set Y: there are 2^m
   subsets and n values, so at most 2^m − n repeats. These would use auxiliary counter variables
   with definitional clauses. That is a conservative extension, but it must be stated as a written
   lemma and covered by the audit. (c) A pair-level normal form, proved as one lemma.
4. *SAT side.* Try other group ansätze, for example Z₁₁ fixing one point, or Z₃ × Z₄. Only a
   witness that passes the checker counts.
5. *Gates.* Stop a target after 10 CPU-h if no cube-level cost estimate below the remaining
   budget exists. An UNSAT proof whose trimmed LRAT exceeds 2 GB, or that cake_lpr cannot check
   within 2 GB, is to be reported as "UNSAT (solver only, uncertified)".

## 6. Reproduce

Tools:
* SAT solver: CaDiCaL 2.1.2, the binary shipped in the Lean toolchain
  `~/.elan/toolchains/leanprover--lean4---v4.34.0-rc1/bin/cadical`.
* The box has no system C compiler, so the checkers were built with zig cc 0.16.0 (PyPI `ziglang`,
  installed into `/home/agent/tools/venv`):
  * drat-trim.c and lrat-check.c from github.com/marijnheule/drat-trim, master @ 2e3b2dc
    (sha256 d834b649… and bf07c2ac…);
  * cake_lpr from github.com/tanyongkiam/cake_lpr @ a36874a (`cake_lpr_arm8.S`, sha256 95b64883…,
    matching the repository's sha256 file; `basis_ffi.c` sha256 8e30d84f… differs from the value
    in that file, and we used the repository's current `basis_ffi.c`).
  ```
  uv venv /home/agent/tools/venv && uv pip install --python /home/agent/tools/venv/bin/python ziglang
  ZIG="/home/agent/tools/venv/bin/python -m ziglang"
  cd /home/agent/tools/src
  for f in lrat-check.c drat-trim.c; do curl -sO https://raw.githubusercontent.com/marijnheule/drat-trim/master/$f; done
  git clone --depth 1 https://github.com/tanyongkiam/cake_lpr.git
  $ZIG cc -O2 -o ../bin/lrat-check lrat-check.c
  $ZIG cc -O2 -o ../bin/drat-trim drat-trim.c
  (cd cake_lpr && $ZIG cc -O2 -std=c99 -DCML_HEAP_SIZE=1400 -DCML_STACK_SIZE=256 basis_ffi.c cake_lpr_arm8.S -o ../../bin/cake_lpr)
  ```
  cake_lpr is run with `--CML_HEAP_SIZE=1400 --CML_STACK_SIZE=256`, which keeps it under the 2 GB
  address-space cap.
* Python 3.12 (standard library only).

Commands, run from this directory:
```
./verify_all.sh                         # re-check every archived witness and LRAT proof (~1 s)
src/witness_cell.sh 11 4 L 1            # regenerate one witness: encode, solve, decode, check
src/certify_unsat.sh 7 3 L 2            # regenerate one UNSAT certificate: audit, solve, trim, check twice
src/certify_unsat.sh 9 4 EH 2
src/certify_unsat.sh 7 3 L 1            # optional cross-check without Lemma S2 (~6 CPU-min, 1.4 GB, 843 MB LRAT)
src/certify_unsat.sh 9 4 EH 0           # optional cross-check with no symmetry breaking (~2 CPU-min, 428 MB LRAT)
```
Witnesses: `certs/witness_<n>_<m>_<V>.txt.gz`, one value per line for masks 0..2^n−1 (bit i = element
i, `-` = undefined at [n] in EH), with the checker output in `.check.txt`. UNSAT certificates:
`certs/unsat_<n>_<m>_<V>_sb<k>.{cnf.gz,lrat.gz,log.txt}`. The log records the audit, drat-trim core
statistics, both checker verdicts and the sha256 of the uncompressed CNF and LRAT.
`*.NOT_ARCHIVED.log.txt` records proofs that were checked and then deleted for size.

## 7. CPU time

`cpu_ledger.csv` records every solver and checker process: 109 runs, 12,549 CPU-s ≈ **3.5 CPU-h**,
against a budget of 20 CPU-h. The breakdown is:
* checkpoint-2 probes: 200 CPU-min. This is almost all of it: eight capped probes at 15 to 30
  minutes each.
* UNSAT certification: 7.7 CPU-min. This includes the unarchived cross-checks (7,3)_L at sb=1
  (about 5.5 min in total) and (9,4)_EH at sb=0 and sb=1 (about 1.9 min). The archived sb=2
  certificates take under 1 CPU-s each.
* witnesses: 1.1 CPU-min, of which (17,5)_L took 57 s.
Peak resident memory was 1.4 GB (cake_lpr heap, and CaDiCaL on (17,5)_L). Python encoding,
decoding and checking are not in the ledger; they add an estimated few CPU-minutes. Wall time was
about 75 minutes, with at most 4 solver processes at a time.

## 8. What is new, and what is not

The erdosproblems.com page says #624 cannot be resolved by a finite computation, and this directory
does not attempt that. It is a small certified table. Compared with herong's 18 Sep 2026 comment,
the new items are as follows. The witness (11,4)_L gives H_L(11) = 4, and so N_L(4) ≥ 11; herong
had reported N(4) ≥ 10 and said he expected, without proof, N(4) = 10. The witnesses (16,5)_L and
(17,5)_L, combined with herong's proof of P2, give H_L(16) = H_L(17) = 5. The EH-convention values
H_EH(n) for n = 2..13 are the other new item; we did not find these values in the sources our G2
check covered, but that check was not exhaustive. Every cell in the two ranges above now has a
checkable artefact, either a witness or an LRAT proof, together with the written lemmas. The values
H_L(2..8) are a re-verification of herong's numbers. The SAT instances are small: the hardest
archived UNSAT proof took under a second to find with symmetry breaking. The open cells (12,4)_L
and (14..16,5)_EH are left for checkpoint 2.
