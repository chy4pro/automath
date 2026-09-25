# Structure Theory of Finite 677 Magmas

*A working paper: verified by-products of an unfinished campaign*

**v7.2 · working paper · 2026-08-18**

**AutoMath Collaboration** (Claude Fable 5, OpenAI GPT-5.6 via `codex`, GPT-5.6 "Pro" via web, operated autonomously)

**Disclosure of the production pipeline.** This paper reports by-products of an autonomous, still-running attack on the last open finite implication of the Equational Theories Project, namely whether every finite magma satisfying $E677$ satisfies $E255$. *That question is not resolved here, and this paper does not claim to resolve it.* Every mathematical statement below was produced by automated systems: an orchestrating agent (Claude Fable 5) that designed the attack families, audited the returning reports, and drafted this document; subordinate exploration agents (Claude Fable 5 instances, OpenAI GPT-5.6 driven through the `codex` command-line interface, and GPT-5.6 at "Pro" effort through the web interface) that carried out the individual lines of attack; and machine checkers (`kissat`, purpose-written C and Python enumerators, and independent from-scratch Python re-verifiers). No human supplied a definition, a lemma, a proof idea, or a correction. Every numbered *assertion* — theorem, lemma, proposition, corollary — carries an explicit verification marker; numbered definitions, problems and the single conjecture assert nothing and carry none.

🖥️ MACHINE-VERIFIED (path) means a script at that path in the campaign repository checks the statement (usually on explicit models, exhaustively over the stated finite range); ✅ PROVED (X) means a human-readable proof exists in the cited internal report and the orchestrating agent independently re-derived or spot-checked it; 🧮 COMPUTATIONAL, PARTIAL (…) means an incomplete search whose exact coverage is stated and which must *not* be read as a classification; and 🧮 COMPUTATIONAL (…) means a completed computation of exactly the stated scope, which — when the computation is a *failed* search — is evidence and not a proof of impossibility.

Several of the campaign's own working conjectures were refuted by its own later rounds (Sections 3 and 4); those self-refutations are recorded rather than quietly deleted. Responsibility for what follows rests with the reader who re-runs the scripts.

*(17 August 2026)*

## Abstract

Let $E677$ denote the law $x = y \mathbin{*} (x \mathbin{*} ((y \mathbin{*} x) \mathbin{*} y))$ and $E255$ the law
$x = ((x\mathbin{*} x)\mathbin{*} x)\mathbin{*} x$. Whether every *finite* $E677$ magma satisfies $E255$ is the
last open finite implication of the Equational Theories Project. We do not settle it. We do
develop the structure theory of finite $E677$ magmas far enough to record a coherent body of
results, all of them either proved here or machine-verified, and all of them by-products of
an ongoing automated campaign.
We prove a pointwise criterion identifying $E255$ at $y$ with the existence of a left unit
for $y$, and derive from it a cluster of equivalent witness criteria, a cycle-length
obstruction $m(y)\notin\{2,3\}$, a row-code minimum-distance bound $\ge \lceil n/2\rceil$,
and the unconditional counting identity $\sum_{y,w}|\operatorname{Fix}(L_y R_w)| = n^2$.
We classify the affine models with commuting coefficients completely: for $F,G$ commuting,
$x\mathbin{*} y = Fx+Gy+c$ on an abelian group $A$
satisfies $E677$ iff $F(G+G^3)=1$, $P(G)=\Phi_{10}(G)\cdot(G^4+G^3+2G^2+2G+1)=0$ and
$(G^2F+G^2+G+1)c=0$, so the affine orders
realizable with commuting coefficients are exactly the orders of finite
$\mathbb{Z}[u]/(P(u))$-modules; the
$\Phi_{10}$ branch consists precisely of the Alexander quandles. (For general $F,G$ the
criterion is a pair of noncommutative equations, and whether every affine model has
commuting coefficients is open.) In particular $2$ is inert
of residue degree $4$ in $\mathbb{Z}[\zeta_5]$, whence such an affine model of even order forces
$16 \mid n$, and $16$ is attained by an $\mathbb{F}_{16}$ quandle. This refutes an odd-order
conjecture that an earlier round of the campaign had proposed: since models of even order
exist, no argument can conclude that $n$ is odd, which removes the parity, sign and $2$-adic
routes the campaign had been pursuing.
We then exhibit and machine-verify a finite $E677$ magma of order $176 = 11\times 16$ which is
*not* right-cancellative; it is smaller than the order-$496$ example of the project
blueprint, which is the only such magma our literature reconnaissance could find recorded
anywhere. It satisfies $E255$, so it is
not a counterexample; what it does refute is a family of proposed proof routes,
including every constraint of the form $N(t,v)+N(v,t)\ge 1$ off the diagonal and the
uniform isoperimetric bound $e(O)\le |O||O^c|$ on which the averaging route of §5.7 rests.
Finally we map the obstructions. Equational and quasi-equational derivations of $E255$ from
$E677$ plus left cancellation resisted every saturation experiment we could run — which is
computational evidence, not a proof of underivability; the natural state map
is provably circular; local amplification of the row-distance bound is capped at
$\lfloor n/2\rfloor$; the transport tree has branching factor $1$; affine fibre extensions
are forced to satisfy $E255$ by a $\{1,3\}$ subscript collision; and idempotent bases in the
extension framework are circular, leaving exactly one habitat for a counterexample built that
way. We give the complete classification of $E677$ magmas of order $\le 9$ (orders
$2,3,4,6,8$ are empty; orders $5,7,9$ carry only affine quasigroups), a deliberately partial
order-$11$ census, and a list of open problems and closed routes.
A final section reports a sixth round: the general-magma analogue of the $\{1,3\}$
collision is identified and turns out to be the problem itself one level down; two $E677$
magmas of order $77$ are constructed — the first non-idempotent non-right-cancellative
example, certified in **Lean** 4, and the first extension that is not
translation-invariant; a new counting identity gives the upper-bound criterion
$\sum_xN(x\backslash x,x)\le\sum_xN(x,x)\Rightarrow E255$, which no term witness can
prove; every idempotent-free *affine* model is shown to have order in $31\cdot S$,
where $31 = \operatorname{Res}(\Phi_{10},Q)$; and a conjecture of that same round is
refuted twice over, which exposes a systematic bias in the campaign's own benchmark set
that we document as a result in its own right.
Two further sections report Rounds 7 and 8: the local configuration that decides $E255$ is
shown to be the same over every base (idempotent levels are circular, non-idempotent levels
carry a three-instance pattern), a cocycle theorem protects the entire separable family, and
two structure theorems say that a minimal counterexample must be simple and can have no
idempotent quotient. Congruences are then identified with block systems of the
left-multiplication group satisfying a kernel condition, which reduces “simple $\Rightarrow$
right-cancellative” to three exhaustively verified finite statements, one of which — a
transport law — would close the last surviving construction route. None of the three is
first-order derivable, and we prove two independent barriers explaining why: one for
existential statements and one, new, for injectivity statements.
A final section refutes that programme. The object its own failure analysis had specified
— a magma whose fibre operation degenerates at one fibre point and is injective at
another — is constructed, twice and independently, at orders $77$ and $385$; it satisfies
$E677$, $E255$ and every genuine first-order consequence of $E677$, and it refutes the
transport law and six further statements, including two we discovered in the course of
writing this. We carry out the retraction in full, marking rather than deleting the voided
results, since the record of which hypotheses died — all of them supported by a model set
whose members shared one accidental property — is the most transferable thing the campaign
produced.

## 1. Introduction

### 1.1 The problem

The Equational Theories Project [1] determined, for a list of $4694$ magma laws, all
$4694^2$ implications between them, in the process producing a very large formalized corpus.
A single *finite* implication survived the effort. Writing $\mathbin{*}$ for the magma
operation, the two laws in question are

$$
\begin{aligned}
  (E677) \qquad x &= y \mathbin{*} \bigl(x \mathbin{*} ((y\mathbin{*} x)\mathbin{*} y)\bigr), \\
  (E255) \qquad x &= ((x\mathbin{*} x)\mathbin{*} x)\mathbin{*} x .
\end{aligned}
$$

$E677$ does not imply $E255$ in general: the free one-generated $677$ magma violates $E255$,
and there is an infinite greedy counterexample [2, Ch. 13]. The question is
whether the implication holds when the carrier is finite. The project's own paper
tentatively conjectures that it does *not* [1], and the DeepMind
`formal-conjectures` corpus [3] carries the same expectation as
a marginal note; but no finite counterexample is known, and every concrete finite model on
record satisfies $E255$ [4].

**Problem 1.1 (the open implication).** 
Does every finite magma satisfying $E677$ satisfy $E255$?

**This paper does not answer Problem 1.1.** What it does is report the part
of the structure theory that has been established and independently checked in the course of
an automated attack on it, together with an explicit map of which attack routes are now
closed — some by proof, some by an explicit counterexample, and some only in the weaker
sense that they were exhausted under a stated computational budget. The three strengths are
kept apart throughout and never conflated. Negative results are a substantial fraction of the
content, and they are stated as results rather than as apologies: several of them refute
proposals that looked, from inside the campaign, like the natural next step.

### 1.2 Why the finite case is delicate

The single structural consequence of $E677$ is that every left translation is surjective:
$E677$ exhibits $x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y)$ as an $L_y$-preimage of $x$. On a finite carrier
surjectivity upgrades to bijectivity, so a finite $E677$ magma is a *left quasigroup*,
and this — as far as anything we have found goes — is the only thing finiteness gives
directly. Everything in this paper is a consequence of $E677$ together with the injectivity
of every $L_y$.

The delicacy is that the corresponding right-hand statement is exactly what is missing.
Theorem 2.7 below shows that $E255$ at $y$ is equivalent to $y$ possessing a
*left unit*, i.e. to the value $y$ appearing in column $y$ of the Cayley table; and the
sets $\operatorname{Fix}(L_w)$ are always pairwise disjoint (Lemma 2.6), so
$\sum_w |\operatorname{Fix}(L_w)| \le n$ always, with $E255$ equivalent to equality. The whole problem is
therefore a covering statement: $n$ pairwise disjoint sets, and one must show they exhaust.
By contrast the mirror statement — that the sets $\operatorname{Fix}(R_u)$ partition $M$ — is
unconditionally true (Proposition 2.11). That asymmetry is the problem.

### 1.3 What is proved here

1.  **Section 2: the basic lemma package.** The $\mathrm{KEY}$
identity $(y\mathbin{*} x)\mathbin{*} y = x\backslash(y\backslash x)$, which is equivalent to $E677$ over a
left quasigroup and is the working form throughout; the left-unit criterion
(Theorem 2.7), which coincides with [2, Lemma 13.1(ii)] and was
rediscovered independently by three of the campaign's attack families; a cluster of
equivalent witness criteria with unique candidate witnesses
(Theorem 2.14); the cycle-length obstruction $m(y)\notin\{2,3\}$
(Theorem 2.15); the row-code bound $|\{x: p\mathbin{*} x = q\mathbin{*} x\}| \le \lfloor
n/2\rfloor$ (Theorem 2.17); the counting identity $\sum_{y,w}|\operatorname{Fix}(L_yR_w)| = n^2$
(Theorem 2.20); and the two single-variable bijectivity reductions
(Proposition 2.21). We also record two genuine linking constraints on the
multiplicity matrix $N$: its support digraph is strongly connected (Theorem 2.22) and
satisfies an edge-expansion bound (Theorem 2.23).

1.  **Section 3: the affine criterion and the commuting spectrum.** The
general criterion, a pair of noncommutative equations in $F,G\in\operatorname{End}(A)$, and its commuting
form $F(G+G^3)=1$, $P(G) = \Phi_{10}(G)\,Q(G) = 0$ with
$Q(u) = u^4+u^3+2u^2+2u+1$ (Theorem 3.1); the module-theoretic spectrum of
the commuting family (Theorem 3.2); the identification of the $\Phi_{10}$
branch with the Alexander
quandles (Proposition 3.3); the *even-order spectrum theorem*
(Theorem 3.4): a commuting affine model of even order forces $16\mid n$, because
$2$ is inert of residue degree $4$ in $\mathbb{Q}(\zeta_5)$, and $16$ is realized by an $\mathbb{F}_{16}$
quandle. Whether an affine $E677$ magma can have $F,G$ non-commuting is
**open** (Problem 11.3), so “complete classification” below always
means *complete within the commuting/$R$-module family*.
This refutes the campaign's own working parity conjecture; since $E677$ magmas of even order
exist, no parity, sign, $2$-adic or Sylow-$2$ argument can conclude that $n$ is odd
(Section 5.6). We also record that all
commuting-coefficient affine models are medial, and that affine models and *affine*
fibre extensions are forced to satisfy $E255$.

1.  **Section 4: an order-$176$ model.** A finite $E677$ magma on
$\mathbb{F}_{11}\times\mathbb{F}_{16}$ that is not right-cancellative (Theorem 4.1), verified by an
independent from-scratch re-implementation. At order $176$ it is smaller than the order-$496$
example of [2, §13.1], which was the only non-right-cancellative finite $E677$
magma previously recorded anywhere (Section 7 brings this down to $77$). It
satisfies $E255$. As a witness it refutes
(Corollary 4.2) the statement $(\mathrm{S\text{-}off})$: $N(t,v)+N(v,t)\ge 1$ for
$t\ne v$, and — for every size class $2\le s\le n-2$ — the specific uniform isoperimetric
upper bound $e(O)\le |O|\,|O^{c}|$ on which the R3-C averaging route rests
(§5.7). Section 4.3 gives
the structure theory of the translation-invariant extension family with *affine fibres*
in which it lives, including the exact criterion for the failure, and the exact reason
(Theorem 4.8) why the same mechanism can never produce a failure *on the
diagonal*, i.e. can never break $E255$, when the fibre operations are affine. General
(non-affine) fibre tables are not covered and remain open.

1.  **Section 5: the obstruction map.** Seven routes are mapped, each
with its exact strength: equational/quasi-equational derivation
(*computational evidence only* — bounded saturation did not collapse, which does not
prove underivability); surjectivity of the state map (provably circular);
pure marginal counting on $N$ (explicit certificate); local amplification of the row-distance
bound (exhausted for words of length $\le 3$); the transport
tree and the pair rotation (proved); parity and sign (refuted by an explicit model); and the
off-diagonal/isoperimetric programme in the form in which it was proposed (refuted by an
explicit model). In the extension framework we record the *idempotent-base circularity*,
which leaves the exceptional base $x\mathbin{*} y = 5x-4y+c$ on $\mathbb{F}_{31}$ as the only
translation-invariant habitat for a counterexample built that way.

1.  **Section 6: the small-order landscape.** A complete
classification for $n\le 9$ (Theorem 6.1), due to a single implementation and
corroborated over smaller ranges by three others (§6.1):
orders $2,3,4,6,8$ carry no $E677$ magma at all; orders $1,5,7,9$ carry only
affine quasigroups, and hence only models satisfying $E255$. A deliberately partial order-$11$
census ($22$ of $87$ pointed cycle types, all UNSAT; four affine models found, the exclusion
of a fifth unfinished) and the near-miss data.

1.  **Section 7: Round 6.** The general-magma analogue of the
$\{1,3\}$ collision, identified exactly — it is Problem 1.1 one level down
(Corollary 7.8); a new family of counting identities yielding the
*upper*-bound criterion $\sum_xN(x\backslash x,x)\le\sum_xN(x,x)\Rightarrow E255$
(Corollary 7.14), together with a proof that no term witness for it exists
(Theorem 7.15); two $E677$ magmas of order $77$
(Theorems 7.18, 7.20) — the first non-idempotent
non-right-cancellative example, certified in **Lean** 4, and the first extension that
is not translation-invariant; the refutation, twice over, of the round's own conjecture that
$e(x) = x\backslash x$ is an automorphism (§7.4); and the spectrum theorem
$S_0^{\mathrm{aff}} = 31\cdot S$ for idempotent-free affine magmas
(Theorem 7.34), resting on $\operatorname{Res}(\Phi_{10},Q) = 31$. The round
also produced a methodological finding, §7.6: four separate conjectures
in this campaign were supported only by an artefact of the model set they were tested on.

1.  **Section 8: Round 7.** The occurrence trichotomy
(Theorem 8.1): at an idempotent level the extension equation collapses
four-fold and is circular, at every non-idempotent level the $E255$-deciding operation occurs
in exactly three instances with a $\{1,3\}$ collision — and this is *independent of the
base*, so changing the base cannot help. On the last surviving base, $\mathbb{F}_7(4x+3y)$: a
strengthening of [2, Lemma 13.4] needing only *one* separable operation over
*any* group (Corollary 8.6), a rigidity theorem needing only three affine
neighbours (Theorem 8.8), and the proof that the $\{1,3\}$ collision is
*not* a protection there. A cocycle protection theorem
(Theorem 8.9) kills the entire separable family. Two structure theorems about
minimal counterexamples: every quotient is a blueprint extension, so “a minimal counterexample
is simple” is equivalent to the extension statement (Theorem 8.12); and no
minimal counterexample has an idempotent quotient (Theorem 8.13).

1.  **Section 9: Round 8.** A dictionary putting congruences of an
$E677$ magma inside permutation group theory — $\theta$ is a congruence iff it is an
$\langle L\rangle$-block system satisfying a kernel condition, whence
$\langle L\rangle$ primitive $\Rightarrow$ $M$ simple
(Theorem 9.1). An exact reduction of “simple $\Rightarrow$ right-cancellative”
to three finite statements, of which one is a *transport law* $(\mathrm{T})$ verified on
$17.3$ million instances (Theorem 9.7); conditionally on it, a dichotomy
(Theorem 9.12) that appeared to kill the last surviving base of Round 7.
And two
independent proofs that the remaining statements are out of reach of first-order reasoning
(§9.7) — the second of which shows that even plain *injectivity*
statements about the collapse structure require finiteness.

1.  **Section 10: Round 9, and a retraction.** The object those
blueprints specified exists: an order-$77$ magma $M_{77}^{\mathrm{D}}$ with a non-affine
fibre operation whose degeneracy depends on the fibre point (Theorem 10.5). It
refutes $(\mathrm{T})$, $(\mathrm{T}^{*})$, $(\mathrm{W})$, $(\mathrm{D})$,
$(\mathrm{A})$, $(\mathrm{S}')$, both falsification filters, the closure of $\operatorname{Idem}$, and
“$\theta_\kappa$ is a congruence” — while satisfying $E677$, $E255$ and every genuine
first-order consequence of $E677$. A second, independent object of order $385$ separates
four strata (Theorem 10.8) and shows the filters have a blind spot and that
$(\mathrm{A})$ and $(\mathrm{T})$ are decoupled. §10.4 carries out the
resulting retraction chain in full — nothing is deleted, everything is marked — and
§10.5 states the corrected skeleton
$(\mathrm{P})\Leftarrow[\text{(NTS)}]+[(\mathrm{B})]+[(\mathrm{Prop})]+[(\mathrm{Q})\Rightarrow E255]$,
in which $(\mathrm{B})$ has newly lost its proof. The positive residue is the machinery
(Theorems 10.1–10.3) that makes non-affine models constructible
at will.

### 1.4 Verification conventions

Because this is an automated campaign's output, the epistemic status of each statement is
recorded explicitly and is not uniform. Four markers are used.

-  🖥️ MACHINE-VERIFIED (path) — a script at that path in the campaign repository checks the statement.
For statements about specific models this is exhaustive over the model; for statements about
ranges it is exhaustive over the stated range and over nothing else.

-  ✅ PROVED (report) — a human-readable proof appears in the cited internal report, and
the orchestrating agent re-derived or spot-checked it independently. Where the proof is short
it is reproduced here in full.

-  🧮 COMPUTATIONAL, PARTIAL (scope) — an *incomplete* computation. The stated scope is the exact
coverage. Such a statement is never a classification, and we flag the two places
(the order-$11$ census in §6.3, and the minimality range of the order-$176$
model in §4.5) where it would be easiest, and most wrong, to read one as
if it were.

-  🧮 COMPUTATIONAL (scope) — a completed computation of the stated scope which is not a
re-runnable single script in the repository (typically a solver run whose log is archived).
It is evidence of exactly the stated scope and of nothing beyond it; in particular a
*failed* bounded search is never a proof of impossibility, and where one appears
(Proposition 5.1) the text says so explicitly.

Markers are attached to every numbered assertion; definitions, open problems and the single
conjecture carry none, since they assert nothing. Where a marker names a script, that script
checks the statement it is attached to and *only* that statement: after the round-1
adversarial review, three markers whose scripts did not in fact compute the quantities
claimed were replaced by new verifiers written for the purpose
(`isoperim_check.py`, `struct_check.py`, `term_full_check.py`).

Where a statement is due to the project blueprint [2] rather than to this
campaign we say so at the statement. Several results below were obtained independently here
and only afterwards matched against the blueprint; we record both, since the independent
derivations are what the campaign actually used, and the coincidence is evidence that the
transcription is faithful.

## 2. Preliminaries: the basic lemma package

### 2.1 Notation

Throughout, $(M,\mathbin{*})$ is a finite magma of order $n = |M|$ satisfying $E677$, unless the text
says otherwise. We write

$$

  L_y(z) := y \mathbin{*} z, \qquad R_y(z) := z\mathbin{*} y, \qquad
  S(y) := y\mathbin{*} y, \qquad \delta(y) := (y\mathbin{*} y)\mathbin{*} y .

$$

**Lemma 2.1 (left quasigroup; known, {[2, Lemma 13.1(i)]}).** 
✅ PROVED ([2, Lemma 13.1(i)]; proof reproduced below)
In any magma satisfying $E677$, every $L_y$ is surjective, with
$L_y^{-1}(x) = x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y)$. If $M$ is finite, every $L_y$ is a bijection.

*Proof.* 
$E677$ reads $L_y\bigl(x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y)\bigr) = x$, which exhibits a preimage of an
arbitrary $x$; finiteness turns surjectivity into bijectivity, and then the displayed formula
computes the inverse.
 ∎

Accordingly we write $\Lambda_y := L_y^{-1}$ and $y\backslash z := \Lambda_y(z)$, so that
$y \mathbin{*} (y\backslash z) = z$. We also write

$$

  y_k := \Lambda_y^{\,k}(y) \quad (k\in\mathbb{Z}), \qquad
  m(y) := \min\{k>0 : y_k = y\},

$$

so $L_y(y_k) = y_{k-1}$, $y\mathbin{*} y = y_{-1}$, and $m(y)$ is the length of the $L_y$-cycle
through $y$. Finally $e(y) := y_1 = \Lambda_y(y)$ is the unique *right* unit of $y$
(indeed $y\mathbin{*} e(y) = y$, and $e(y)$ is unique because $L_y$ is injective).

*Finiteness enters this paper only through the injectivity of the maps $L_y$.* Every
statement below that does not explicitly invoke a counting argument therefore holds in every
$E677$ left quasigroup, finite or not; we flag this where it matters, because it delimits
exactly what a proof of Problem 1.1 may not do.

### 2.2 The $\mathrm{KEY}$ identity

**Lemma 2.2 ($\mathrm{KEY}$).** 
✅ PROVED (F5, §1 and R2)
In a left quasigroup, $E677$ is equivalent to

$$\tag{$\mathrm{KEY}$}
  (y\mathbin{*} x)\mathbin{*} y \;=\; x\backslash(y\backslash x) \;=\; \Lambda_x\Lambda_y(x)
  \qquad \text{for all } x,y .
$$

Equivalently, writing $\Theta_t := R_t\circ L_t$, one has
$\Theta_t(x) = (t\mathbin{*} x)\mathbin{*} t = \Lambda_x(\Lambda_t(x))$.

*Proof.* 
$E677$ says $L_yL_x\bigl((y\mathbin{*} x)\mathbin{*} y\bigr) = x$; apply $\Lambda_y$ and then $\Lambda_x$.
Every step is reversible in a left quasigroup.
 ∎

$\mathrm{KEY}$ is the working form used throughout. It makes visible that $E677$ carries
exactly $n^2$ bits of information and that the right translation $R$ is a *derived*
operation, determined by the left division:

**Lemma 2.3 ($R$ is determined by $\backslash$).** 
✅ PROVED (F1, Lemma B$'$)
For all $v,y$,

$$v\mathbin{*} y \;=\; \Lambda_{\Lambda_y(v)}\bigl(\Lambda_y^2(v)\bigr)
        \;=\; (y\backslash v)\backslash\bigl(y\backslash(y\backslash v)\bigr). \tag{2.1}
$$

Consequently a finite $E677$ magma is completely determined by its left-division left
quasigroup $(M,\backslash)$, and $E677$ is equivalent to the single law
$u\backslash\bigl((y\backslash u)\backslash(y\backslash(y\backslash u))\bigr) = y$
in $(M,\backslash)$.

*Proof.* 
Substituting $x := y\backslash u$ into $\mathrm{KEY}$ (so that $y\mathbin{*} x = u$) gives the
*master form*

$$(y\backslash u)\mathbin{*}(u\mathbin{*} y) \;=\; \Lambda_y^2(u) \qquad\text{for all } u,y, \tag{2.2}
$$

i.e. $L_{\Lambda_y(u)}(R_y(u)) = \Lambda_y^2(u)$. Solving (2.2) for $u\mathbin{*} y$
using injectivity of $L_{\Lambda_y(u)}$ gives (2.1).
 ∎

Identity (2.2) is used so often below — it is the source of every “transport”
argument in the campaign — that we give it a name: the *master identity*. In the form

$$(\Lambda_t x)\mathbin{*}(x\mathbin{*} t) \;=\; \Lambda_t^2(x) \tag{2.3}
$$

it is the *transport identity*; (2.3) is equivalent to
$\mathrm{KEY}$, hence to $E677$.

**Lemma 2.4 (diagonal).** 
✅ PROVED (F1 Lemma D; F4 (4a); F5 Lemma B; R3-B L-a)
$\delta(y) = (y\mathbin{*} y)\mathbin{*} y = \Lambda_y^2(y) = y_2$, equivalently $L_y^2(\delta(y)) = y$.

*Proof.* 
$E677$ at $x=y$ reads $L_y^2\bigl((y\mathbin{*} y)\mathbin{*} y\bigr) = y$.
 ∎

So the first three points of the $R_y$-orbit of $y$ are $y_0, y_{-1}, y_2$, and $E255$ at
$y$ is precisely $R_y^3(y) = y$, i.e. $R_y(y_2) = y$.

### 2.3 Left units: the pointwise criterion

**Lemma 2.5.** 
✅ PROVED (F1 Lemma F)
If $y\mathbin{*} v = v$ then $v\mathbin{*} y = e(v)$; in particular $v\mathbin{*} y$ does not depend on $y$.

*Proof.* 
$y\mathbin{*} v = v$ says $\Lambda_y(v) = v$, hence also $\Lambda_y^2(v) = v$. Then (2.1)
gives $v\mathbin{*} y = \Lambda_{\Lambda_y(v)}(\Lambda_y^2(v)) = \Lambda_v(v) = e(v)$.
 ∎

**Lemma 2.6 (uniqueness of left units).** 
✅ PROVED (F1 Lemma G; F5 L2; R3-B L-b)
For every $v\in M$ there is at most one $y$ with $y\mathbin{*} v = v$. Equivalently, the fixed-point
sets $\operatorname{Fix}(L_w)$, $w\in M$, are pairwise disjoint.

*Proof.* 
By Lemma 2.5 every such $y$ satisfies $L_v(y) = e(v)$, and $L_v$ is injective.
 ∎

**Theorem 2.7 (left-unit criterion).** 
✅ PROVED (F1 Thm 1; F4 Lemma 2; F5 T1; blueprint Lemma 13.1(ii))
Let $M$ be a finite $E677$ magma and $y\in M$. The following are equivalent.

1.  $((y\mathbin{*} y)\mathbin{*} y)\mathbin{*} y = y$, i.e. $E255$ holds at $y$;

1.  there exists $w$ with $w\mathbin{*} y = y$ (“$y$ has a left unit”);

1.  $y \in \operatorname{Im}(R_y)$, i.e. the value $y$ occurs in column $y$ of the Cayley table.

Moreover the $w$ of (2) is unique and equals $\delta(y) = (y\mathbin{*} y)\mathbin{*} y$.

*Proof.* 
(1)$\Rightarrow$(2): take $w = \delta(y)$. (2)$\Rightarrow$(1): given $w\mathbin{*} y = y$,
Lemma 2.5 gives $y\mathbin{*} w = e(y) = \Lambda_y(y)$; but also
$y\mathbin{*} \delta(y) = y\mathbin{*} \Lambda_y^2(y) = \Lambda_y(y) = e(y)$ by Lemma 2.4.
Injectivity of $L_y$ forces $w = \delta(y)$, whence $\delta(y)\mathbin{*} y = y$, which is $E255$ at
$y$. (2)$\Leftrightarrow$(3) is a restatement.
 ∎

**Remark.** 
Theorem 2.7 was obtained independently by three of the campaign's attack
families before the blueprint was consulted; it is [2, Lemma 13.1(ii)]. Its
proof uses finiteness *only* to upgrade surjectivity of $L_y$ to injectivity, so it
holds in every $E677$ left quasigroup, infinite ones included. This locates the entire
finite/infinite gap precisely:

$$

  y\notin\operatorname{Im}(R_y) \implies R_y \text{ not surjective}
  \implies_{\text{finite}} R_y \text{ not injective}
  \implies \exists\, a\ne b: a\mathbin{*} y = b\mathbin{*} y .

$$

So a finite counterexample must have two distinct rows of its Cayley table agreeing in some
column, and Lemma 2.6 says they may not agree at a diagonal position. Only the
off-diagonal case is open.

**Corollary 2.8.** 
✅ PROVED (F1 Cor 1.1; F5 T2)
Every finite $E677$ magma which is a quasigroup — equivalently, whose Cayley table is a
Latin square, equivalently for which every $R_y$ is injective — satisfies $E255$.

**Corollary 2.9 (partition criterion).** 
✅ PROVED (F1 Cor 1.3; F5 T1)
$\#\{y: E255 \text{ holds at } y\} = \sum_{w\in M}|\operatorname{Fix}(L_w)| \le n$, with equality iff
$E255$ holds. Thus $E255$ holds iff the sets $\operatorname{Fix}(L_w)$ *partition* $M$. In particular,
if every $L_w$ has a fixed point then $E255$ holds.

**Corollary 2.10 (dichotomy).** 
✅ PROVED (F1 Cor 1.2)
For every $y$: either $R_y^3(y) = y$, so $y$ lies on an $R_y$-cycle of length dividing $3$,
or $y$ has no $R_y$-preimage at all. There is no intermediate behaviour — $y$ can never
sit on a longer $R_y$-cycle, nor on a tail at positive distance from a cycle.

**Proposition 2.11 (the right-hand dual, unconditional).** 
✅ PROVED (F1 Prop 2)
$\operatorname{Fix}(R_u) = e^{-1}(u)$, because $x\mathbin{*} u = x \iff L_x(u) = x \iff u = \Lambda_x(x) = e(x)$.
Hence the sets $\operatorname{Fix}(R_u)$, $u\in M$, *always* partition $M$, and
$\sum_u |\operatorname{Fix}(R_u)| = n$ exactly.

The contrast between Corollary 2.9 and Proposition 2.11 is
the whole problem: the right translations' fixed-point sets always partition $M$; the left
translations' fixed-point sets are always disjoint, and $E255$ says exactly that they also
cover.

### 2.4 The reformulations (P) and (Q)

**Definition 2.12.** 
For finite $E677$ magmas consider

$$
\begin{aligned}
  (\mathrm{P}) &\quad \text{every $y$ satisfies } y\in\operatorname{Im}(R_y)
                \quad\text{(equivalently: every element has a left unit);}\\
  (\mathrm{Q}) &\quad \text{every $R_t$ is injective: } a\mathbin{*} t = b\mathbin{*} t \implies a = b .
\end{aligned}
$$

By Theorem 2.7, $(\mathrm{P})$ *is* Problem 1.1: it is a
reformulation, not a strengthening. By Corollary 2.8,
$(\mathrm{Q})\Rightarrow(\mathrm{P})$. During Rounds 1–3 the campaign pursued $(\mathrm{Q})$
as the target, on the evidence that every model then known was a quasigroup. That was a
mistake, and it is worth recording as such:

**Proposition 2.13 ($(\mathrm{Q})$ is false).** 
🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/verify176.py (order $176$),
m496.py (order $496$))
$(\mathrm{Q})$ fails: there are finite $E677$ magmas that are not right-cancellative. The
blueprint's order-$496$ example [2, §13.1] is one; the order-$176$ magma of
Theorem 4.1 is a smaller one. Both satisfy $E255$.

So $(\mathrm{Q})$ is strictly stronger than $(\mathrm{P})$ and is *false*, while
$(\mathrm{P})$ remains open. Any future work must target $(\mathrm{P})$, or one of the seven
equivalent pointwise conditions of [2, Lemma 13.2], and not $(\mathrm{Q})$.

### 2.5 Witness criteria with unique candidate witnesses

**Theorem 2.14 ($E255$ criteria).** 
✅ PROVED (F1 Thm 3)
For $y$ in a finite $E677$ magma the following are equivalent, and in each case the witness
is *unique* and is the displayed element.

1.  $E255$ holds at $y$;

1.  $\exists w: w \mathbin{*} y = y\backslash w$, i.e. $\operatorname{Fix}(L_yR_y)\ne\emptyset$ — the only
possible $w$ is $y_3 = \Lambda_y^3(y)$;

1.  $\exists c: c\mathbin{*} c = y\backslash c$ — the only possible $c$ is
$y_4 = \Lambda_y^4(y)$;

1.  $\exists c: y\mathbin{*}(c\mathbin{*} c) = c$, i.e. $c\mapsto y\mathbin{*}(c\mathbin{*} c)$ has a fixed point;

1.  $y_4 \mathbin{*} y_4 = y_5$.

*Proof.* 
(1)$\Leftrightarrow$(2): if $v\mathbin{*} y = y$, put $w := \Lambda_y(v)$; (2.2) gives
$w\mathbin{*}(v\mathbin{*} y) = \Lambda_y(w)$, i.e. $w\mathbin{*} y = \Lambda_y(w)$. Conversely from
$w\mathbin{*} y = \Lambda_y(w)$ put $v := L_y(w)$; (2.2) gives
$w\mathbin{*}(v\mathbin{*} y) = \Lambda_y(w) = w\mathbin{*} y$, so $v\mathbin{*} y = y$ by injectivity of $L_w$. Uniqueness
of $v = \delta(y) = y_2$ (Theorem 2.7) gives $w = \Lambda_y(y_2) = y_3$.
(2)$\Leftrightarrow$(3): by (2.1), $w\mathbin{*} y = \Lambda_{\Lambda_y(w)}(\Lambda_y^2(w))$;
with $c := \Lambda_y(w)$ the condition $w\mathbin{*} y = \Lambda_y(w)$ becomes
$\Lambda_c(\Lambda_y(c)) = c$, i.e. $c\mathbin{*} c = \Lambda_y(c)$; and
$c = \Lambda_y(y_3) = y_4$. (3)$\Leftrightarrow$(4) is
$\Lambda_y(c) = c\mathbin{*} c \iff y\mathbin{*}(c\mathbin{*} c) = c$. (3)$\Leftrightarrow$(5) since
$\Lambda_y(y_4) = y_5$.
 ∎

Criterion (5) is worth isolating: *$E255$ at $y$ is equivalent to a single equation
about the fourth and fifth iterates of $\Lambda_y$ at $y$.* Criterion (3) is the global
version: $E255$ holds iff, for every $y$, the squaring map $S(c) = c\mathbin{*} c$ agrees with the
permutation $\Lambda_y$ somewhere. Equivalently, in a counterexample the squaring map must
avoid the entire graph of $\Lambda_y$ — $n$ simultaneous disequalities, and the sharpest
single pointwise obstruction available.

**Theorem 2.15 (cycle-length obstruction).** 
✅ PROVED (F1 Thm 2; independent proof R3-B L-c)
For every $y$ in a finite $E677$ magma:

- **(a)**  $m(y)\notin\{2,3\}$;

- **(b)**  if $E255$ holds at $y$ then $m(y)\notin\{2,3,4\}$; equivalently,
$m(y) = 4$ forces $E255$ to fail at $y$;

- **(c)**  $m(y) = 1$ (i.e. $y$ idempotent) implies $E255$ at $y$.

*Proof.* 
(c) $y\mathbin{*} y = y$ gives $((y\mathbin{*} y)\mathbin{*} y)\mathbin{*} y = y$.

(a) If $m(y)=2$: write $y\mathbin{*} y = a \ne y$, $y\mathbin{*} a = y$, so $y_2 = y$. Lemma 2.4
gives $(y\mathbin{*} y)\mathbin{*} y = y_2 = y$, i.e. $a\mathbin{*} y = y$, so $a$ is a left unit of $y$; by
Theorem 2.7, $a = \delta(y) = y_2 = y$, a contradiction.

If $m(y)=3$: write $y\mathbin{*} y = a$, $y\mathbin{*} a = b$, $y\mathbin{*} b = y$ with $y,a,b$ distinct; then
$y_1 = b$ and $y_2 = a$. Lemma 2.4 gives $a\mathbin{*} y = a$. Applying (2.2)
with $u := y_1$, $y := y$ gives $y_1\mathbin{*}(y\mathbin{*} y) = y_2$, i.e. $b\mathbin{*} a = a$. Now $\mathrm{KEY}$
with $y := a$, $x := y$ reads $y\mathbin{*}((a\mathbin{*} y)\mathbin{*} a) = \Lambda_a(y)$; since $a\mathbin{*} y = a$ this
is $y\mathbin{*}(a\mathbin{*} a) = \Lambda_a(y)$. From $b\mathbin{*} a = a$ and Theorem 2.7, $b$ is
*the* left unit of $a$, so $a\mathbin{*} b = e(a)$ by Lemma 2.5; independently
$a\mathbin{*} y = a$ says $y = e(a)$, so $a\mathbin{*} b = y$, i.e. $\Lambda_a(y) = b$. Hence
$y\mathbin{*}(a\mathbin{*} a) = b = y\mathbin{*} a$, so $a\mathbin{*} a = a$ by injectivity of $L_y$. But then $e(a) = a$,
contradicting $e(a) = y \ne a$.

(b) Assume $E255$ at $y$, i.e. $y_2\mathbin{*} y = y$. Applying (2.2) with $u := y_3$,
$y := y$ gives $y_3\mathbin{*}(y_2\mathbin{*} y) = y_4$, hence $y_3\mathbin{*} y = y_4$. If $m \mid 4$ then
$y_4 = y$, so $y_3\mathbin{*} y = y$, making $y_3$ a left unit of $y$; Theorem 2.7
forces $y_3 = \delta(y) = y_2$, i.e. $m\mid 1$, so $m = 1$. If $m\mid 3$ then
$y_{-1} = y_2$, and Lemma 2.4 ($y_{-1}\mathbin{*} y = y_2$) reads $y_2\mathbin{*} y = y_2$; with
$y_2\mathbin{*} y = y$ this gives $y_2 = y$, i.e. $m\mid 2$, so together $m = 1$.
 ∎

**Remark.** 
An earlier report [8, L3] recorded the weaker statement “$m(y)\in\{2,3\}\Rightarrow
E255$ fails at $y$”. Theorem 2.15(a) shows those cycle lengths do not occur at
all, so that statement, while true, is vacuous. Empirically the observed values of $m$ across
all models the campaign enumerated are $1,6,7,8,9,12,15,18,36,42$; $m\in\{4,5\}$ has never
been observed, and is open. 🧮 COMPUTATIONAL (F1 §5, R3-B `mvals.py`)

### 2.6 The row code and the multiplicity matrix

**Lemma 2.16.** 
✅ PROVED (F5 L1, L4)
In a finite $E677$ magma:

- **(L1)**  $z\mapsto L_z$ is injective; hence $M$ embeds in $\operatorname{Sym}(M)$ as a set $\Lambda$ of
$n$ distinct permutations.

- **(L4)**  $p\mathbin{*} x = q\mathbin{*} x$ *and* $p\backslash x = q\backslash x$ together imply
$p = q$.

*Proof.* 
(L4): $\mathrm{KEY}$ at $(p,x)$ and $(q,x)$ gives, with $u := p\mathbin{*} x = q\mathbin{*} x$,
$u\mathbin{*} p = \Lambda_x(\Lambda_p(x))$ and $u\mathbin{*} q = \Lambda_x(\Lambda_q(x))$. If
$\Lambda_p(x) = \Lambda_q(x)$ the right sides agree, so $L_u(p) = L_u(q)$ and $p=q$.

(L1): assume $L_p = L_q$ and put $u := p\mathbin{*} x = q\mathbin{*} x$ for arbitrary $x$. $E677$ at $(p,x)$
and at $(q,x)$ gives, after applying $\Lambda_p = \Lambda_q$, that
$x\mathbin{*}(u\mathbin{*} p) = p\backslash x$ and $x\mathbin{*}(u\mathbin{*} q) = q\backslash x = p\backslash x$. Cancel
$L_x$ to get $u\mathbin{*} p = u\mathbin{*} q$, then cancel $L_u$.
 ∎

**Theorem 2.17 (row-code distance).** 
✅ PROVED (F5 T3; two-line proof R3-B L-d)
Let $p\ne q$ and $F_{pq} := \{x : p\mathbin{*} x = q\mathbin{*} x\} = \operatorname{Fix}(L_p^{-1}L_q)$. Then
$x\in F_{pq} \Rightarrow L_p^{-1}(x)\notin F_{pq}$; consequently $F_{pq}$ meets every
$L_p$-cycle $C$ in at most $\lfloor |C|/2\rfloor$ points, so

$$

  |F_{pq}| \;\le\; \lfloor n/2\rfloor .

$$

Equivalently, the $n$ rows of the Cayley table form an $n$-ary code of length $n$ with
minimum Hamming distance $\ge \lceil n/2\rceil$.

*Proof.* 
Let $x\in F_{pq}$ and $f := L_p^{-1}(x)$, so $p\mathbin{*} f = x$. If also $f\in F_{pq}$ then
$q\mathbin{*} f = p\mathbin{*} f = x$, i.e. $p\backslash x = f = q\backslash x$; with $p\mathbin{*} x = q\mathbin{*} x$,
(L4) gives $p = q$.
 ∎

Theorem 2.17 is a genuine counting obstruction of the right type, and it is
quantitatively insufficient: the Latin property needs minimum distance $n$, and no
Plotkin- or Singleton-type bound bites at distance $n/2$ with only $n$ codewords. Closing
that gap was the campaign's route R3-A; §5.5 records that it is capped.

**Definition 2.18 (the multiplicity matrix and its support sizes).** 
$N(t,v) := \#\{a : a\mathbin{*} t = v\}$, the multiplicity of the value $v$ in column $t$. We also fix
here, once and for all, the two support sizes used from §4 onwards:

$$

  r_t := |\operatorname{Im}(R_t)| = \#\{v : N(t,v)>0\}, \qquad
  c_v := \#\{t : v\in\operatorname{Im}(R_t)\} = \#\{t : N(t,v)>0\},

$$

i.e. $r_t$ is the number of *distinct values* occurring in column $t$, and $c_v$ is the
number of *columns* in which the value $v$ occurs at all. Both equal $n$ exactly when
$(\mathrm{Q})$ holds; Lemma 6.8 records the two inequalities they satisfy in general.

**Lemma 2.19 ($N$ counts fixed points).** 
✅ PROVED (R2 (13); R3-C Lemma 1.1)
For all $t,v$ the map $a\mapsto \Lambda_t(a)$ is a bijection
$\{a: a\mathbin{*} t = v\} \to \operatorname{Fix}(L_t R_v) = \{x : t\mathbin{*}(x\mathbin{*} v) = x\}$. Hence
$N(t,v) = |\operatorname{Fix}(L_tR_v)|$, and also $N(t,v) = |\Theta_t^{-1}(v)|$ where
$\Theta_t = R_t\circ L_t$.

*Proof.* 
Put $x := \Lambda_t(a)$, so $a = t\mathbin{*} x$. By $\mathrm{KEY}$,
$a\mathbin{*} t = (t\mathbin{*} x)\mathbin{*} t = \Lambda_x(\Lambda_t x)$. Hence
$a\mathbin{*} t = v \iff \Lambda_x(\Lambda_t x) = v \iff \Lambda_t x = x\mathbin{*} v \iff t\mathbin{*}(x\mathbin{*} v) = x$,
and $\Lambda_t$ is a bijection.
 ∎

**Theorem 2.20 (the counting identity).** 
✅ PROVED (orchestrating agent, R2; equivalent form R2 (12)+(14))
In every finite $E677$ magma, all row sums and all column sums of $N$ equal $n$. Hence,
unconditionally,

$$\sum_{y,w\in M} \bigl|\operatorname{Fix}(L_y R_w)\bigr| \;=\; n^2 . \tag{2.4}
$$

Moreover $N(v,v)\le 1$ for all $v$ (Lemma 2.6), and

$$

  \begin{aligned}
    E255 &\iff \operatorname{tr} N = n \iff \text{every } \Theta_t \text{ has a fixed point},\\
    (\mathrm{Q}) &\iff N\equiv 1 \iff \text{every } L_vR_u \text{ has a fixed point}.
  \end{aligned}

$$

*Proof.* 
For fixed $t$, every $x$ lies in exactly one fibre $\Theta_t^{-1}(v)$, so
$\sum_v N(t,v) = n$. For fixed $v$, every row of the Cayley table contains $v$ exactly once
(rows are permutations), so $\sum_t N(t,v) = n$. Summing either way gives (2.4)
through Lemma 2.19. The diagonal statement is Lemma 2.6 restated, and
$E255 \iff \operatorname{tr} N = n$ is Theorem 2.7 restated. For $(\mathrm{Q})$: if every
$L_tR_v$ has a fixed point then $N(t,v)\ge1$ for all $t,v$, and each row of $N$ has $n$
entries summing to $n$, so every entry equals $1$; conversely $N\equiv1$ trivially gives
fixed points. Thus mere *existence* already forces uniqueness.
 ∎

Identity (2.4) is the reason $E255$ can be described as a *diagonal slice* of
$(\mathrm{Q})$: the total mass is fixed at $n^2$ unconditionally, the diagonal is capped at
$1$ per entry, and $E255$ asks that the diagonal be saturated.

**Proposition 2.21 (single-variable reductions).** 
✅ PROVED (R3-B L-g, L-h)
Fix $t,x\in M$.

- **(L-g)**  Column $t$ of the Cayley table is a permutation $\iff$ the map
$\Theta_t: z\mapsto \Lambda_z(\Lambda_t(z))$ is a bijection of $M$. Hence
$(\mathrm{Q}) \iff \Theta_t$ is bijective for every $t$.

- **(L-h)**  $\beta_x(y) := (y\mathbin{*} x)\mathbin{*} y$ is a bijection $\iff$ $N(t,x) = 1$ for every $t$
$\iff$ the value $x$ occurs exactly once in every column.

*Proof.* 
(L-g) $\Theta_t = R_t\circ L_t$ with $L_t$ a permutation, so $\Theta_t$ is bijective iff
$R_t$ is; and $\Theta_t(z) = \Lambda_z\Lambda_t(z)$ by $\mathrm{KEY}$.
(L-h) By $\mathrm{KEY}$, $\beta_x(y) = \Theta_y(x) = \Lambda_x(\Lambda_y(x)) =
\Lambda_x(\alpha_x(y))$ with $\alpha_x(y) := \Lambda_y(x)$; since $\Lambda_x$ is a bijection,
$\beta_x$ is injective iff $\alpha_x$ is. And $\alpha_x(y) = \alpha_x(y') = z$ means
$y\mathbin{*} z = x = y'\mathbin{*} z$, so $\alpha_x$ is injective iff $N(z,x)\le 1$ for all $z$; the column
sums $\sum_t N(t,x) = n$ then force $N(\cdot,x)\equiv 1$.
 ∎

(L-g) and (L-h) are the two “orthogonal” halves of $(\mathrm{Q})$ — columns versus values
— each expressed as bijectivity of an explicit *single-variable* map built from
$\mathrm{KEY}$, rather than as a condition on the $n\times n$ matrix $N$.

### 2.7 Two linking constraints on $N$

Pure marginal information about $N$ (row sums, column sums, diagonal cap, support bound) is
provably insufficient: §5.3 exhibits a numerical matrix satisfying all
of it with $N\not\equiv 1$. The following two theorems are constraints that genuinely
*link* entries of $N$, and they are not implied by the marginal package: a
block-diagonal $N$ with row and column sums $n$ and diagonal $\le 1$ satisfies the marginals
and violates Theorem 2.22.

**Theorem 2.22 (strong connectivity).** 
✅ PROVED (R3-C Thm A)
Let $D_N$ be the digraph on $M$ with an arc $a\to b$ iff $N(a,b)>0$ (equivalently
$b\in\operatorname{Im}(R_a)$). Then $D_N$ is strongly connected. Equivalently, there is no
$\emptyset \ne O \subsetneq M$ with $M\mathbin{*} O \subseteq O$, and $\langle L_y : y\in M\rangle$
acts transitively on $M$.

*Proof.* 
Let $O$ be the set reachable from some $a\in M$ in $D_N$ (so $a\in O$). Then $O$ is forward
closed: $L_y(O)\subseteq O$ for every $y$, hence $L_y(O) = O$ and $\Lambda_y(O) = O$ by
finiteness and injectivity.

*Step 1 ($O$ is right closed).* Let $x\in O$ and $t\in M$. Then $\Lambda_t x\in O$ and
therefore $\Lambda_x(\Lambda_t x)\in O$. By $\mathrm{KEY}$,
$(t\mathbin{*} x)\mathbin{*} t = \Lambda_x(\Lambda_t x)\in O$. As $x$ runs over $O$, $u := t\mathbin{*} x$ runs over
$L_t(O) = O$. Hence

$$u \mathbin{*} t \in O \qquad \text{for every } u\in O \text{ and every } t\in M . \tag{2.5}
$$

*Step 2 (counting).* For $a\in O$, all $n$ products $y\mathbin{*} a$ lie in $O$, so
$\sum_{b\in O} N(a,b) = n$; summing over $a\in O$ gives $\sum_{a,b\in O} N(a,b) = n|O|$. On
the other hand each $b\in O$ has full column sum $n$, so
$\sum_{b\in O}\sum_{a\in M} N(a,b) = n|O|$. Subtracting,

$$\sum_{a\notin O,\, b\in O} N(a,b) = 0, \quad\text{i.e.}\quad
  u\mathbin{*} t\notin O \text{ whenever } t\notin O . \tag{2.6}
$$

*Step 3.* If $O\ne M$ pick $t\notin O$ and $u\in O$; then (2.5) gives
$u\mathbin{*} t\in O$ and (2.6) gives $u\mathbin{*} t\notin O$. Hence $O = M$; as $a$ was
arbitrary, $D_N$ is strongly connected.
 ∎

Implication (2.5) — *any set closed under all left translations is
closed under all right translations* — is the only place in the whole campaign where
$\mathrm{KEY}$ produced genuinely global, non-tautological information. A localized or
weighted version of it remains the most promising unexplored mechanism.

**Theorem 2.23 (edge expansion).** 
✅ PROVED (R3-C Thm B)
For $\emptyset\ne O\subsetneq M$ put
$e(O) := \sum_{a\in O, b\notin O} N(a,b) = \#\{(y,a) : a\in O, y\mathbin{*} a\notin O\}$ and
$m := \min(|O|,|O^{c}|)$. Then

$$

  m \;\le\; e(O) + \sqrt{e(O)}, \qquad\text{i.e.}\qquad
  e(O) \;\ge\; m + \tfrac12 - \sqrt{m+\tfrac14}.

$$

*Proof.* 
Write $\varepsilon := e(O)$, $s := |O|$. Step 2 of Theorem 2.22 generalizes to the
flow balance $\sum_{a\notin O, b\in O} N(a,b) = ns - \sum_{a,b\in O} N(a,b) = \varepsilon$,
since $\sum_{a\in O, b\in M} N(a,b) = ns = \sum_{b\in O, a\in M} N(a,b)$. In particular
$\#\{(u,t) : t\notin O, u\in M, u\mathbin{*} t\in O\} = \varepsilon$.

Let $\delta_y := |L_y(O)\setminus O|$; then $\sum_y\delta_y = \varepsilon$, so
$Y := \{y : L_y(O) = O\}$ has $|Y|\ge n-\varepsilon$, and for $y\in Y$ also
$\Lambda_y(O) = O$. Fix $t\in Y\setminus O$ and $x\in O\cap Y$. Then $\Lambda_t x\in O$ and,
since $\Lambda_x(O) = O$, also $\Lambda_x(\Lambda_t x)\in O$; by $\mathrm{KEY}$,
$(t\mathbin{*} x)\mathbin{*} t\in O$, while $u := t\mathbin{*} x \in L_t(O) = O$. Each such pair $(x,t)$ therefore
produces a pair $(u,t)$ with $u\in O$, $t\notin O$, $u\mathbin{*} t\in O$, and $x\mapsto t\mathbin{*} x$ is
injective for fixed $t$. Hence
$\varepsilon \ge |Y\setminus O|\cdot|O\cap Y| \ge (|O^{c}|-\varepsilon)(|O|-\varepsilon)$.
If $\varepsilon\ge m$ the claim is immediate; otherwise both factors are $\ge m-\varepsilon>0$,
so $\varepsilon\ge(m-\varepsilon)^2$, i.e. $m-\varepsilon\le\sqrt\varepsilon$.
 ∎

Theorem 2.22 is the case $m\ge 1$ of Theorem 2.23 ($\varepsilon = 0$ would give
$1\le 0$). Both are *lower* bounds on $e(O)$. Section 5.7 explains why
this direction is the wrong one, and Section 4 shows that the right one is
unavailable.

## 3. The affine models: criterion and commuting spectrum

Every finite $E677$ magma known to us — to the campaign, to the blueprint, and to the
public model database [4] — is affine over an abelian group, or a fibred extension
of one. This section gives the exact criterion for an affine magma to satisfy $E677$, and
classifies completely those affine models whose two coefficients *commute*; every known
affine model is of that kind. *The converse — that an affine $E677$ magma must have
commuting coefficients — is not proved here and is open* (Problem 11.3),
so “the affine spectrum” below always means the spectrum of the commuting family. The
classification is the source of the campaign's most useful pieces of information and of one
of its most instructive mistakes.

### 3.1 The affine criterion

**Theorem 3.1 (affine criterion).** 
✅ PROVED (R3-B Thm 1) 🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/final_verify.py, constc.py
(scalar, hence commuting, models over cyclic groups only))
Let $A$ be an abelian group and $F,G\in\operatorname{End}(A)$, and define $x\mathbin{*} y := Fx+Gy$.

- **(a)**  $(A,\mathbin{*})$ satisfies $E677$ iff

$$

  \text{(i)}  GF + G^2FG = \mathrm{id}_A
  \qquad\text{and}\qquad
  \text{(ii)}  F + G^2F^2 + G^3 = 0 .

$$

- **(b)**  If $F$ and $G$ commute, (i)–(ii) read $F(G+G^3) = 1$ and $F+F^2G^2+G^3 = 0$.

- **(c)**  Suppose $G+G^3\in\operatorname{Aut}(A)$ and put $F := (G+G^3)^{-1}$ (so $F,G$ commute). Then
(i)–(ii) hold iff

$$

  P(G) = 0, \qquad\text{where}\qquad
  P(u) := u^8+2u^6+u^4+u^2+u+1 = \Phi_{10}(u)\cdot Q(u),

$$

with $\Phi_{10}(u) = u^4-u^3+u^2-u+1$ and $Q(u) = u^4+u^3+2u^2+2u+1$.

- **(d)**  Any such $(A,\mathbin{*})$ is a *quasigroup* (both $F$ and $G$ are units), hence
satisfies $(\mathrm{Q})$ and therefore $E255$.

- **(e)**  With a constant, $x\mathbin{*} y = Fx+Gy+c$ satisfies $E677$ iff (i), (ii) hold and
$(G^2F+G^2+G+1)c = 0$.

*Proof.* 
(a) Expanding, and keeping the order of composition,

$$

\begin{aligned}
  y\mathbin{*} x &= Fy+Gx, \\
  (y\mathbin{*} x)\mathbin{*} y &= F^2y + FGx + Gy, \\
  x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y) &= Fx + GF^2y + GFGx + G^2y, \\
  y\mathbin{*}\bigl(x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y)\bigr) &= (GF+G^2FG)\,x + (F+G^2F^2+G^3)\,y .
\end{aligned}

$$

Setting this equal to $x$ for all $x,y$ gives exactly (i)–(ii) (take $y=0$ and $x=0$
respectively); conversely (i)–(ii) plainly suffice. (b) is immediate.

(c) From (i), $G+G^3 = G(1+G^2)$ is invertible, hence so is $G$. Multiplying (ii) by
$(G+G^3)^2$ and using $F(G+G^3)=1$,

$$

  F(G+G^3)^2 + F^2G^2(G+G^3)^2 + G^3(G+G^3)^2
  = (G+G^3) + G^2 + G^3(G^2+2G^4+G^6)
  = G\cdot P(G).

$$

Since $G$ and $(G+G^3)^2$ are units, (ii) $\iff P(G)=0$. Conversely if $P(G)=0$ and $G+G^3$
is invertible, set $F := (G+G^3)^{-1}$; the displayed identity gives
$(F+F^2G^2+G^3)(G+G^3)^2 = G\,P(G) = 0$, hence (ii).

(d) $F = (G+G^3)^{-1}$ is a unit, so $a\mapsto a\mathbin{*} t = Fa+Gt$ is injective: the table is a
Latin square, so $(\mathrm{Q})$ holds and Corollary 2.8 applies.

(e) The same expansion with the constant produces the extra term $(G^2F+G^2+G+1)c$.
 ∎

Note that (i) already forces $F$ and $G$ to commute *once one assumes*
$F = (G+G^3)^{-1}$, and conversely commuting $F,G$ satisfying (i) must equal $(G+G^3)^{-1}$;
so parts (b),(c) describe exactly the commuting solutions. Nothing below rules out a
noncommuting solution of (i)–(ii), and we know of none; see
Problem 11.3.

The side condition in (c) is in fact automatic:

**Theorem 3.2 (module description of the commuting affine spectrum).** 
✅ PROVED (R3-B Thm 1$'$)
Let $R := \mathbb{Z}[u]/(P(u))$. In $R$ the element $u$ is a unit (from $P(u)=0$ one has
$u\cdot(u^7+2u^5+u^3+u+1) = -1$) and $1+u^2$ is a unit (since $P(u)\equiv u \bmod (1+u^2)$),
so $u+u^3 = u(1+u^2)$ is automatically a unit of $R$. Consequently, for every finite
$R$-module $A$, letting $G$ be the action of $u$ and $F := (G+G^3)^{-1}$, the magma
$(A, x\mathbin{*} y = Fx+Gy)$ is an $E677$ magma of order $|A|$, and it is a quasigroup satisfying
$E255$ and $(\mathrm{Q})$.

Hence: *the orders realized by affine $E677$ magmas with commuting $F,G$ are exactly the
orders of finite $\mathbb{Z}[u]/(P(u))$-modules.* Concretely, for a prime $p$ let $d(p)$ be the
multiset of degrees of
the distinct irreducible factors of $P$ mod $p$; the achievable exponents of $p$ form the
numerical semigroup generated by $d(p)$.

**Remark (exactly what is and is not classified).** 
The “$\supseteq$” half — every finite $R$-module yields a model of its own order — is
proved above. The “$\subseteq$” half is proved only for solutions with $F,G$ commuting,
equivalently with $F = (G+G^3)^{-1}$, since only then does $P(G)=0$ follow. A hypothetical
affine model with noncommuting $F,G$ would satisfy neither hypothesis and could in principle
realize an order outside the $R$-module spectrum. Every affine model exhibited anywhere in
this paper, in the campaign, in [2] or in [4] is commuting (indeed
scalar or a matrix power series in $G$), and the verifier
`R3B_scripts/final_verify.py` tests scalar models over cyclic groups; so the
noncommuting case is unexplored rather than excluded.

**Proposition 3.3 (the $\Phi_{10}$ branch is exactly the Alexander quandles).** 
✅ PROVED (R3-B Prop 2)
For commuting $F,G\in\operatorname{End}(A)$ the following are equivalent:

1.  $\Phi_{10}(G) = 0$ and $F = 1-G$;

1.  $F = 1-G$ and $(A, x\mathbin{*} y = Fx+Gy)$ satisfies $E677$;

1.  $(A, x\mathbin{*} y = Fx+Gy)$ satisfies $E677$ and is *idempotent*.

In that case $(A,\mathbin{*})$ is a *quandle*: idempotent, left-distributive, with all $L_x$
bijective; i.e. it is the Alexander quandle $x\mathbin{*} y = (1-G)x+Gy$ with $G$ a primitive $10$th
root of unity in $\operatorname{End}(A)$.

*Proof.* 
If $\Phi_{10}(G)=0$, i.e. $G^4-G^3+G^2-G = -1$, then
$(1-G)(G+G^3) = G+G^3-G^2-G^4 = -(G^4-G^3+G^2-G) = 1$, so $F := 1-G = (G+G^3)^{-1}$, and
$P(G) = \Phi_{10}(G)Q(G) = 0$, so Theorem 3.1(c) gives $E677$. Conversely if
$F=1-G$ and $E677$ holds, then $F(G+G^3)=1$ forces $(1-G)(G+G^3)=1$, which unwinds to
$\Phi_{10}(G)=0$. Idempotency: $x\mathbin{*} x = (F+G)x$, so $x\mathbin{*} x = x$ for all $x$ iff $F+G=1$.
Left distributivity for an affine magma: $x\mathbin{*}(y\mathbin{*} z) = Fx+GFy+G^2z$ while
$(x\mathbin{*} y)\mathbin{*}(x\mathbin{*} z) = (F^2+GF)x + FGy + G^2z$; with commuting $F,G$ these agree for all
$x,y,z$ iff $F = F(F+G)$, i.e. iff $F+G=1$ ($F$ being a unit).
 ∎

The order-$5$ dihedral (Takasaki) quandle $x\mathbin{*} y = 2x-y$ over $\mathbb{Z}_5$ is the case $A=\mathbb{Z}_5$,
$G=-1$ (since $\Phi_{10}(-1)=5\equiv 0$). The $Q$-branch is not idempotent in general: the
two order-$7$ models $x\mathbin{*} y = 4x+y$ ($G=1$, $Q(1)=7$) and $x\mathbin{*} y = 4x+3y$ ($G=3$,
$Q(3)=133=7\cdot 19$) are $Q$-branch, and the first has a left identity. In particular
*$E677$ does not force idempotency, even finitely.*

**Remark.** 
Theorem 3.1 was derived independently by two of the campaign's families —
first as the cyclic-modulus statement $P(G)\equiv 0 \pmod m$, $F = (G+G^3)^{-1}$,
$c\cdot(G^2F+G^2+G+1)=0$ over $\mathbb{Z}/m$ [8], then in the endomorphism form above
[11] — and it matches the blueprint's Type 1/Type 2 dichotomy exactly: Type 1 is the
$\Phi_{10}$ factor, Type 2 the quartic factor $Q$. This is a cross-check of a transcription,
not an independent theorem.

### 3.2 The even-order spectrum theorem

The following was the campaign's sharpest self-correction. Rounds 1–2 had recorded, on the
strength of the cyclic case plus the exhaustive emptiness of orders $2,4,6,8$, a working
*parity conjecture*: every finite $E677$ magma has odd order. It is false.

**Theorem 3.4 (even-order spectrum, commuting case).** 
✅ PROVED (R3-B Thm 3, Thm 4) 🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/final_verify.py, extra.py, paranoia.py)
Throughout, “affine” means $x\mathbin{*} y = Fx+Gy+c$ with $F,G$ *commuting*, equivalently
$F = (G+G^3)^{-1}$ (Theorem 3.1(c)); this is what makes $P(G)=0$ available.

- **(a)**  *(the cyclic case, which is all the earlier claim covered)* If $A\cong \mathbb{Z}_m$
is cyclic then no affine $E677$ magma of even order exists on $A$: indeed
$P(G)\equiv G^8+G^4+G^2+G+1\equiv 1 \pmod 2$ for every integer $G$, so $P(G)$ is always odd
and $P(G)\equiv 0 \pmod m$ is unsolvable for even $m$.

- **(b)**  *(general abelian $A$)* If $A$ carries an affine $E677$ magma structure and
$|A|$ is even, then $16 \mid |A|$; more precisely the $2$-primary part $A_2$ satisfies
$|A_2| = 16^{k}$ for some $k\ge 1$.

- **(c)**  $16$ is attained. Let $\mathbb{F}_{16} = \mathbb{F}_2[z]/(z^4+z^3+z^2+z+1)$, so $z^5=1$ and
$z\ne 1$, and define on $M = \mathbb{F}_{16}$

$$

  x \mathbin{*} y \;=\; (1+z)\,x + z\,y .

$$

Then $(M,\mathbin{*})$ is an $E677$ magma of order $16$; it satisfies $E255$, its table is a Latin
square (so $(\mathrm{Q})$ holds in it), and it is a quandle.

Hence the minimal even order of a commuting affine model is exactly $16$.

*Proof.* 
(a) is the displayed congruence.

(b) $P$ mod $2$ factors over $\mathbb{F}_2$ as
$P \equiv (u^4+u^3+u^2+u+1)(u^4+u^3+1) = \Phi_5\cdot f$, a product of two *distinct*
irreducible quartics. Let $A_2\ne 0$ be the $2$-primary part (which is $G$-invariant). For
each $i$, $V_i := 2^iA_2/2^{i+1}A_2$ is an $\mathbb{F}_2$-vector space carrying an induced
$\bar G$ with $P(\bar G) = 0$, i.e. $V_i$ is a module over
$\mathbb{F}_2[u]/(\Phi_5 f) \cong \mathbb{F}_2[u]/(\Phi_5)\times \mathbb{F}_2[u]/(f) \cong \mathbb{F}_{16}\times\mathbb{F}_{16}$ by
CRT. A module over a product of fields is a direct sum of vector spaces over each factor, so
$\dim_{\mathbb{F}_2}V_i \equiv 0 \pmod 4$ and $|V_i| = 16^{k_i}$. Multiplying over the filtration,
$|A_2| = 16^{\sum k_i}$, and $A_2\ne 0$ forces some $k_i\ge 1$.

(c) In characteristic $2$, $\Phi_{10}(u) = u^4+u^3+u^2+u+1 = \Phi_5(u)$, and $z$ is a
primitive $5$th root of unity, so $\Phi_{10}(z) = 0$; also $1-z = 1+z$. Now apply
Proposition 3.3 with $G = $ multiplication by $z$ and $F = 1+z$, and
Theorem 3.1(d). Finally $\Phi_5$ is irreducible over $\mathbb{F}_2$ (the order of
$2$ mod $5$ is $4$), so $\mathbb{F}_2[z]$ really is a field of $16$ elements, and $z$ exists there
because $5\mid 15 = |\mathbb{F}_{16}^{\times}|$.
 ∎

The Cayley table of the order-$16$ quandle was re-parsed from printed text and the raw $E677$
term $y\mathbin{*}(x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y))$ evaluated on all $256$ pairs: $0$ violations; $E255$: $0$
violations 🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/paranoia.py). There is a second family at order
$16$: taking $G\in\mathbb{F}_{16}$ a root of the other factor $u^4+u^3+1$ (a primitive $15$th root of
unity) and $F = (G+G^3)^{-1}$ gives a Latin, $E255$, *non*-idempotent model. Scanning all
$G\in\mathbb{F}_{16}$ with $P(G)=0$ gives exactly $8$ values, splitting into two Frobenius orbits, and
a backtracking isomorphism search shows these $8$ magmas form exactly *two* isomorphism
classes 🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/extra.py):

| $G$ (multiplicative order) | $F$ | quandle? | # idempotents | cycle type of every $L_y$ |
|---|---|---|---|---|
| $5$ (the $\Phi_{10}$ branch) | $1+G$ | yes | $16$ | $(5,5,5,1)$ |
| $15$ (the $Q$ branch) | $(G+G^3)^{-1}$ | no | $1$ | $(15,1)$ |

**Corollary 3.5 (the structural reason there is no parity obstruction).** 
✅ PROVED (R3-B §6.3)
The only “mod $2$” phenomenon in this problem is that $P \bmod 2 = \Phi_5\cdot(u^4+u^3+1)$
has no root in $\mathbb{F}_2$ — which is exactly why $\mathbb{Z}_m$-linear even-order models do not exist.
But both factors are irreducible of degree $4$, so they do have roots in $\mathbb{F}_{16}$. The
would-be parity obstruction is really a *residue-degree* statement: the prime $2$ has
residue degree $4$ in $\mathbb{Z}[u]/(P)$, i.e. $2$ is inert in $\mathbb{Q}(\zeta_5)$ (because $2$ has order
$4$ mod $5$). That is an arithmetic fact about the number $5$, not a parity fact about $n$;
it forces $16\mid n$, never $n$ odd. *Any future global mechanism for
Problem 1.1 must be insensitive to the parity of $n$.*

### 3.3 The affine spectrum

Computing the factorizations of $P$ modulo small primes 🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/final_verify.py):

| $p$ | irreducible factors of $P$ mod $p$ | minimal $p$-part |
|---|---|---|
| $2$ | $u^4+u^3+1$, $u^4+u^3+u^2+u+1$ | $2^4 = 16$ |
| $3$ | $(u^2-u-1)^2$, $u^4-u^3+u^2-u+1$ | $3^2 = 9$ |
| $5$ | $(u+1)^4$, $Q$ | $5$ |
| $7$ | $u-1$, $u-3$, $u^2-2u-2$, $\Phi_{10}$ | $7$ |
| $11,13,19,31,37,41,43$ | have a linear factor | $p$ |
| $17,23,29,53,59$ | minimal degree $2$ | $p^2$ |
| $47$ | irreducible quartics only | $p^4$ |

The orders $\le 200$ achievable by a commuting affine model are

$$

\begin{aligned}
&1, 5, 7, 9, 11, 13, \mathbf{16}, 19, 25, 31, 35, 37, 41, 43, 45, 49, 55, 61, 63, 65, 67, 71, 73,\\
&77, \mathbf{80}, 81, 91, 95, 97, 99, 101, 103, 109, \mathbf{112}, 117, 121, 125, 131, 133, 139,\\
&143, \mathbf{144}, 151, 155, 157, 163, 169, 171, 175, \mathbf{176}, 181, 185, 191, 193 .
\end{aligned}

$$

The even orders $\le 1000$ are $16, 80, 112, 144, 176, 208, 256, 304, 400, 496, 560, 592,
656, 688, 720, 784, 880, 976$ — all divisible by $16$, as Theorem 3.4(b)
requires. Since $E677$ is an identity, the class of $E677$ magmas is closed under direct
products, so $16m$ is realizable for every realizable odd $m$; there are infinitely many even
orders.

**Remark (a superseded list).** 
An earlier round recorded the model orders as “$1,5,7,9,11,13,19,31,35,37,41,43$”, obtained
by scanning $x\mathbin{*} y = ax+by \bmod n$ for $n\le 39$. That list is *not* exhaustive even
among affine models: e.g. $25$ is realizable by $A = (\mathbb{Z}/5)^2$,
$G = \left(\begin{smallmatrix}4&1\\0&4\end{smallmatrix}\right) = -I+N$ with $N^2=0$
(then $\Phi_{10}(u)\equiv(u+1)^4 \bmod 5$, so $\Phi_{10}(G) = N^4 = 0$, and $G+G^3 = -2I+4N$
is invertible). The correct statement is
Theorem 3.2.
🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/extra.py)

### 3.4 Mediality, and why affine models cannot be counterexamples

**Proposition 3.6 (commuting affine models are medial).** 
✅ PROVED (R3-F) 🖥️ MACHINE-VERIFIED (problems/etp677/r3f_enum.py)
Every affine $E677$ model with commuting coefficients ($FG=GF$) is medial:
$(x\mathbin{*} y)\mathbin{*}(z\mathbin{*} w) = (x\mathbin{*} z)\mathbin{*}(y\mathbin{*} w)$. Conversely, direct expansion shows an affine
operation is medial *iff* $FG=GF$, so mediality of all affine models is equivalent to
the open commutation problem (Problem 11.3).

*Proof.* 
Expanding both sides of mediality for $x\mathbin{*} y = Fx+Gy+c$ shows they differ only by
interchanging $FGb+GFc$ with $FGc+GFb$; under $FG=GF$ the two sides agree. In the commuting
setting $F=(G+G^3)^{-1}$ automatically commutes with $G$.
 ∎

Mediality was verified exhaustively over all quadruples for the named models
$(\mathbb{Z}_5, 2x+4y)$, $(\mathbb{Z}_7, 4x+y)$, $(\mathbb{Z}_7, 4x+3y)$, $(\mathbb{F}_9, x+(t+2)y)$ with $t^2+1=0$, and
$(\mathbb{F}_{16}, (1+z)x+zy)$ — all medial, all $E255$, all Latin.

Three separate obstructions say that no counterexample can be affine, or even affinely
fibred:

**Proposition 3.7 (no affine counterexamples).** 
[markers are attached to the individual items (a)–(d)]

- **(a)**  *✅ PROVED (Theorem 3.1(d); [2, Lemma 13.3])* Any finite
$E677$ magma of the form $x\mathbin{*} y = \alpha x + \beta y + c$ on an abelian group satisfies
$E255$.

- **(b)**  *✅ PROVED (F4 Prop 5)* Let $A$ be any abelian group (finite or not),
$h : A\to A$ *arbitrary* — not assumed linear — and $y\mathbin{*} x := x + h(y)$. If this
satisfies $E677$ then it satisfies $E255$.

- **(c)**  *✅ PROVED (F4 Prop 6)* For every $n\ge 1$ and every
$(\alpha,\beta,\gamma)\in(\mathbb{Z}/n)^3$, the $E677$ conditions for
$y\mathbin{*} x = \alpha y + \beta x + \gamma$ imply the $E255$ conditions.

- **(d)**  *✅ PROVED ([2, Lemma 13.4], external)* If $G\times M$ satisfies $E677$, where $G$ is
an $E677$ magma satisfying $E255$, $M$ is an abelian group, and
$(x,s)\mathbin{*}(y,t) = (x\mathbin{*} y, \alpha_{x,y}s+\beta_{x,y}t+c_{x,y})$ with $\alpha,\beta$
endomorphisms, then $G\times M$ satisfies $E255$.

*Proof of (b).* 
Every row of $y\mathbin{*} x = x+h(y)$ is a translation, hence a permutation. Direct expansion shows
$E677$ holds exactly when

$$h\bigl(x+h(y)\bigr) + h(x) + h(y) + y = x \qquad (x,y\in A). \tag{3.1}
$$

Put $y=x$ in (3.1): $h(x+h(x)) = -2h(x)$. Now put $y = x+h(x)$ in (3.1) and use
the previous display; the remaining terms cancel to $h(x-2h(x)) = 0$. The three right
multiplications by $x$ are therefore

$$

  x\mathbin{*} x = x+h(x), \quad (x\mathbin{*} x)\mathbin{*} x = x+h(x+h(x)) = x-2h(x), \quad
  ((x\mathbin{*} x)\mathbin{*} x)\mathbin{*} x = x + h(x-2h(x)) = x .

$$

 ∎

*Proof of (c).* 
Expansion of $E677$ for $y\mathbin{*} x = \alpha y+\beta x+\gamma$ gives the exact necessary and
sufficient congruences mod $n$

$$

  \text{(A1)} \alpha\beta(1+\beta^2)=1, \qquad
  \text{(A2)} \alpha+\alpha^2\beta^2+\beta^3=0, \qquad
  \text{(A3)} \bigl(\beta^2(\alpha+1)+\beta+1\bigr)\gamma=0,

$$

while $E255$ is exactly

$$

  \text{(B1)} \alpha^3+\alpha^2\beta+\alpha\beta+\beta=1, \qquad
  \text{(B2)} (\alpha^2+\alpha+1)\gamma = 0 .

$$

Set $u := 1+\beta^2$. By (A1), $\alpha,\beta,u$ are units and $\alpha = (\beta u)^{-1}$.
Multiplying (A2) by the unit $\beta u^2$ turns it into $F := u+\beta+\beta^4u^2 = 0$.
Multiplying the left side of (B1) minus $1$ by the unit $\beta^3u^3$ gives
$N = 1+\beta^2u+\beta^3u^2+\beta^4u^3-\beta^3u^3$, and using only $u = 1+\beta^2$, direct
expansion gives the polynomial identity $N = (1-\beta+\beta^2)F$; thus (A2) implies (B1).
For the constant term put $H := \beta+u(\beta^2+\beta+1)$ and $J := 1+\beta u+\beta^2u^2$;
the coefficient in (A3) is $H/u$, while $\alpha^2+\alpha+1 = J/(\beta^2u^2)$, and direct
expansion gives $J = (1-\beta+\beta^2)H$. Hence
$(\alpha^2+\alpha+1)\gamma = \frac{1-\beta+\beta^2}{\beta^2u}\bigl(\beta^2(\alpha+1)+\beta+1\bigr)\gamma = 0$,
which is (B2).
 ∎

Part (b) is worth emphasizing, since it goes beyond the blueprint's linear obstruction: the
row-shift function $h$ is completely arbitrary, so *no* choice of nonlinear row shifts
and no modulus can turn the natural periodic-successor construction into a counterexample.
The obstruction is the two-step use of (3.1), not a failed parameter search. As an
independent check, exhaustive enumeration of all $(\alpha,\beta,\gamma)$ modulo every
$n = 11,\dots,40$ found affine $E677$ models exactly at
$n\in\{11,13,19,31,35,37\}$ (with $4,13,38,65,14,74$ solutions respectively) and zero
violations of (B1)–(B2) in every one; and exhaustive enumeration of all functions
$h : \mathbb{Z}/n\to\mathbb{Z}/n$ for $n\le 7$ found no violation in the family (3.1)
🧮 COMPUTATIONAL ([7], §3–§4).

## 4. An $E677$ magma of order $176$ that is not right-cancellative

### 4.1 Context

Until this campaign, exactly one finite $E677$ magma failing right cancellation was recorded
anywhere: the order-$496$ example of [2, §13.1], built as a fibred extension of
an $\mathbb{F}_{31}$ base by three $\mathbb{F}_{16}$ fibre operations. It satisfies $E255$. Its existence is
what makes $(\mathrm{Q})$ of Definition 2.12 false, and hence what forced the campaign
to abandon the route it had been pursuing for two rounds.

The natural next target, proposed at the end of Round 3 as “the smallest currently
unclaimed step in the right direction”, was the following weakening of $(\mathrm{Q})$:

$$

  (\mathrm{S\text{-}off}) \qquad N(t,v) + N(v,t) \;\ge\; 1 \qquad \text{for all } t\ne v .

$$

Its appeal is that setting $t=v$ turns it into $N(v,v)\ge 1$, which is exactly $E255$; so
$(\mathrm{S\text{-}off})$ is the “weaker off-diagonal sibling” of the target, and whatever
technique proved it would have been informative about the diagonal. It is false, and the rest
of this section is an expanded and re-checked account of [16].

### 4.2 The model

**Theorem 4.1.** 
🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/verify176.py, m176.json)
Let $M := \mathbb{F}_{11}\times\mathbb{F}_{16}$ with $\mathbb{F}_{16} = \mathbb{F}_2[z]/(z^4+z^3+1)$ (elements encoded as
integers $0..15$, bit $i$ the coefficient of $z^i$). Define, for $x,y\in\mathbb{F}_{11}$ and
$s,t\in\mathbb{F}_{16}$,

$$

  (x,s) \mathbin{*} (y,t) \;:=\; \bigl(\,4x+8y \bmod 11,  a_{y-x}\,s + b_{y-x}\,t\,\bigr),

$$

where the fibre coefficients $(a_d,b_d)\in\mathbb{F}_{16}^2$, indexed by $d = (y-x)\bmod 11$, are

| $d$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $(a_d,b_d)$ | $(14,15)$ | $(0,1)$ | $(11,10)$ | $(10,11)$ | $(10,11)$ | $(11,10)$ | $(10,11)$ | $(11,10)$ | $(11,10)$ | $(10,11)$ | $(0,1)$ |

Then $|M| = 176$ and:

- **(a)**  $(M,\mathbin{*})$ satisfies $E677$ (zero violations over all $176^2$ pairs);

- **(b)**  every $L_y$ is a bijection; all row sums and all column sums of $N$ equal $176$;

- **(c)**  $(M,\mathbin{*})$ satisfies $E255$: $N(v,v) = 1$ for every $v$;

- **(d)**  $(M,\mathbin{*})$ is *not* right-cancellative: the entries of $N$ take the values
$\{0,1,16\}$;

- **(e)**  there are $2640$ unordered pairs $\{t,v\}$ with $t\ne v$ and
$N(t,v) = N(v,t) = 0$. An explicit witness is $t = (0,0)$, $v = (4,1)$: there is no $a$ with
$a\mathbin{*} t = v$ and no $b$ with $b\mathbin{*} v = t$.

The off-diagonal distribution of $N(t,v)+N(v,t)$ over the $\binom{176}{2} = 15400$ unordered
pairs is $\{0 : 2640, 2: 12584, 32: 176\}$. Moreover, writing
$r_t$ and $c_v$ for the support sizes of Definition 2.18,
$N$ has $5280$ zero entries and
$r_t = c_v = 146$ for all $t,v$
🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/struct_check.py).

The key feature is $a_1 = a_{10} = 0$: the fibre operations at offsets $d = \pm 1$ are the
projections $s\diamond t = t$, which are not injective in their left argument.

*Verification.* 
The script `R5C_scripts/verify176.py` rebuilds $\mathrm{GF}(16)$, the base
$x\diamond y = 4x+8y$ on $\mathbb{F}_{11}$, and the whole $176\times176$ Cayley table from scratch,
importing nothing from the search code, and evaluates the raw $E677$ term on all $176^2$
pairs together with all the counts quoted above; its archived output
`verify176.out` reports $0$ violations. The table itself is stored as
`R5C_scripts/m176.json`. The construction was found by SAT
(`R5C_scripts/bp_sat.py`, log `bp_theta_sat.out`) inside the extension
framework of §4.3, and verified twice — once through the extension
equation (4.1), once by brute force on the product magma.
 ∎

**Corollary 4.2.** 
🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/verify176.py for (a)–(b);
isoperim_check.py for (c))

- **(a)**  $(\mathrm{S\text{-}off})$ is false. A fortiori so are $N+N^{\mathsf T} = 2J$ and
$N+N^{\mathsf T}\ge 2J-I$.

- **(b)**  The order-$176$ magma is a non-right-cancellative finite $E677$ magma of order
smaller than $496$. As far as the campaign's literature reconnaissance [14] could
determine, no smaller one had been recorded at the time. (Round 6 later produced one of
order $77$, Theorem 7.18; it satisfies $(\mathrm{S\text{-}off})$ and so does not
replace the order-$176$ witness for (a) and (c).)

- **(c)**  With $e(O)$ as in Theorem 2.23, write
$\mathrm{exc}(O) := e(O)-|O|\,|O^{c}|$; since all row sums of $N$ equal $n$ one has
identically $\mathrm{exc}(O) = |O|^2 - \sum_{a,b\in O}N(a,b)$. In the order-$176$ magma
$\mathrm{exc}(O)>0$ for at least one $O$ of *every* size $2\le s\le n-2$: the script
`isoperim_check.py` exhibits such an $O$ for each of the $173$ size classes and
evaluates $e(O)$ on the stored Cayley table. In particular for the
$(\mathrm{S\text{-}off})$-violating
pair $O = \{(0,0),(4,1)\}$ one has $e(O) = 350 > 348 = |O||O^c|$. Full enumeration gives the
exact maxima $\max_{|O|=s}\mathrm{exc}(O) = 0,\,+2,\,+4$ at $s=1,2,3$; for the middle size
classes only lower bounds are established here, and they are large (e.g. an explicit $O$
with $|O|=88$ has $\mathrm{exc}(O) = 1152$).

**Remark (a corrected number).** 
[16], §4.2 printed a table of purported extremal excesses
($+20$ at $s=8$, $+282$ at $s=88$, $+264$ at $s=120$, \dots). Those values are *not*
maxima: `isoperim_check.py` exhibits sets with $\mathrm{exc} = +32$, $+1152$ and
$+768$ at those sizes. Exact maxima are verified only at $s\in\{1,2,3\}$ (and, by
complementation, $s\in\{173,174,175\}$); at $s=4,5$ the witness family reproduces the
reported values without an exactness proof. Nothing in the paper depends on the extremal values —
only on the sign of $\mathrm{exc}$ — but the table should not be quoted.

Part (c) closes the programme it was aimed at, and needs to be read carefully. Round 3 had
proved
[12] that if $e(O)\le|O||O^c|$ holds for all $O$ of one *single* size $s$, then
$E255$ follows — an averaging argument, since
$\sum_{|O|=s}e(O) = (n^2-\operatorname{tr} N)\binom{n-2}{s-1}$ and
$s(n-s)\binom ns = (n^2-n)\binom{n-2}{s-1}$. The implication is correct. What
Corollary 4.2(c) shows is that its *premise* is false for every size class
$s$ that is not already equivalent to $E255$ — and false in a magma
that *does* satisfy $E255$. So that premise cannot be proved, and this particular route
is closed, not merely unproven. Any proof of $E255$ along these lines must bound $e(O)$ for a
*restricted* family of sets
$O$ (for instance only $|O|=1$, which is $E255$ itself), not uniformly over a size class.
This says nothing about other conceivable off-diagonal or isoperimetric quantities; what is
refuted is the specific threshold $e(O)\le|O||O^c|$.

**Proposition 4.3 (what survives in the order-$176$ magma).** 
🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/struct_check.py, verify176.py)
The following all hold in the order-$176$ magma, and are therefore *consistent* with the
failure of the Latin property and cannot by themselves give $E255$: Theorem 2.22
(strong connectivity of $\operatorname{supp} N$); the diameter-$2$ property (for all $t,z$ there is $u$
with $N(t,u)>0$ and $N(u,z)>0$, namely $u = f_t(z) = (t\mathbin{*}(t\mathbin{*} z))\mathbin{*} t$); row and column
sums $=n$; $\operatorname{tr} N = n$; and the counting condition
$\#\mathrm{zeros}(N) = 5280 \le \binom{176}{2} = 15400$ that $(\mathrm{S\text{-}off})$
necessarily implies. In addition $Q := \sum_{t,v}N(t,v)^2 = 115456$, so
$Q-n^2 = \sum_{p\ne q}|F_{pq}| = 84480$; here $F_{pq}\ne\emptyset$ exactly for the $2640$
ordered pairs $p = (x,s)$, $q = (x,s')$ with $s\ne s'$, and then $|F_{pq}| = 32$.

**Remark.** 
For comparison, in the order-$496$ magma the same count gives $|F_{pq}| = 240$ against the
bound $\lfloor n/2\rfloor = 248$ of Theorem 2.17 — i.e. the row-code bound is
essentially *tight* there. That is why the Cauchy–Schwarz route to a lower bound on
$\sum_t r_t$ is hopeless: it gives $\sum_t r_t \ge n^4/Q = 29\,772$ against the required
$123\,256$ 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/m496.py).

### 4.3 The translation-invariant extension family with affine fibres

The order-$176$ magma is an instance of the extension framework of
[2, Ch. 13]: given an $E677$ magma $G$, an abelian group $M$, and a family
$\diamond_{x,y}$ of operations on $M$ satisfying

$$s \;=\; t \diamond_{y,\,L_y^{-1}x}\Bigl( s \diamond_{x,\,(y\diamond x)\diamond y}
          \bigl( (t\diamond_{y,x}s)\diamond_{y\diamond x,\,y} t \bigr)\Bigr)
  \qquad \text{for all } x,y\in G, \tag{4.1}
$$

the product $(x,s)\mathbin{*}(y,t) := (x\diamond y, s\diamond_{x,y}t)$ satisfies $E677$. This
subsection gives the complete structure theory of the *translation-invariant* (TI)
sub-family *with affine fibre operations*, in which $\diamond_{x,y}$ depends only on
$y-x$ and each $\diamond_d$ is affine. **Both restrictions are in force throughout
§4.3 and §4.4**; “complete” always means complete for that
sub-family, and general (non-affine) fibre tables are *not* covered by anything below
(see the scope remark after Theorem 4.8 and
Problem 11.8). The restriction is what made the search
tractable and what makes the diagonal analysis in §4.4 sharp.

*Setting.* Base $x\diamond y = Ax+By+c$ on $\mathbb{F}_p$ with $A+B=1$ and $A,B\ne 0$ (so the
base is translation-invariant and Latin; $E677$ for it is checked directly). Fibre operations
$s\diamond_d t = a_d s + b_d t + c_d$ are $M$-linear with $b_d$ invertible (needed so that
rows are permutations), and the operation attached to the pair $(x,y)$ is $\diamond_{y-x}$.

**Lemma 4.4 ((4.1) in coordinates).** 
✅ PROVED (R5-C Lemma 2.1; adversarially re-derived in R5-A) 🖥️ MACHINE-VERIFIED (problems/etp677/r5a_search.py `selftest`, R5C_scripts/blueprint_search.py)
Put

$$

  D_1 = -\frac{d+c}{B},\qquad
  D_2 = (A^2+B)d + (A+1)c,\qquad
  D_3 = -d,\qquad
  D_4 = Bd-c .

$$

Then (4.1) at parameter $d = y-x$ is equivalent to the three scalar equations in the
operations at indices $D_1,\dots,D_4$:

$$

  \text{(E1)}  b_1\bigl(a_2+b_2a_4b_3\bigr) = 1, \qquad
  \text{(E2)}  a_1 + b_1b_2\bigl(a_4a_3+b_4\bigr) = 0, \qquad
  \text{(E3)}  b_1\bigl(b_2(a_4c_3+c_4)+c_2\bigr)+c_1 = 0,

$$

where index $j$ abbreviates index $D_j$.

*Proof.* 
Expand $t\diamond_{D_1}\bigl(s\diamond_{D_2}((t\diamond_{D_3}s)\diamond_{D_4}t)\bigr)$ as an
affine function of $(s,t)$ and equate to $s$; the coefficients of $s$, of $t$, and the
constant give (E1), (E2), (E3). The index formulas are obtained by specializing the four base
pairs of (4.1): solving $y\diamond z = x$ gives $z-y = -(d+c)/B$;
$(y\diamond x)\diamond y = ABx+(A^2+B)y+(A+1)c$, whose difference from $x$ is
$(A^2+B)d+(A+1)c$ using $A+B=1$; and the last two differences are $x-y = -d$ and
$y-(y\diamond x) = Bd - c$.
 ∎

**Remark.** 
The index formulas were subjected to an adversarial re-derivation by an independent agent,
which confirmed them together with the general (non-TI) pair subscripts and the reduction of
the $E255$-violation constraint; a self-test reconstructs the blueprint order-$496$ model with
zero violations of (4.1), zero $E677$ violations on the full order-$496$ magma, and
zero $E255$ failures 🖥️ MACHINE-VERIFIED (problems/etp677/r5a_search.py `selftest`,
r5a_audit.py).

**Lemma 4.5 (the $N$-matrix of a TI extension).** 
✅ PROVED (R5-C Lemma 2.3)
Let the base be Latin. For $T = (y,t)$ and $V = (v_1,v_2)$ put $\delta := (y-v_1+c)/A$. Then

$$

  N(T,V) \;=\;
  \begin{cases}
    1 & \text{if } a_\delta \ne 0,\\
    |M| & \text{if } a_\delta = 0 \text{ and } b_\delta t + c_\delta = v_2,\\
    0 & \text{if } a_\delta = 0 \text{ and } b_\delta t + c_\delta \ne v_2 .
  \end{cases}

$$

*Proof.* 
$x$ is uniquely determined by $Ax+By+c = v_1$, and then
$y-x = (y-v_1+c)/A = \delta$; the remaining equation is $a_\delta s + b_\delta t + c_\delta = v_2$,
which is affine in $s$.
 ∎

**Corollary 4.6 (exact criterion for the failure of $(\mathrm{S\text{-}off})$).** 
✅ PROVED (R5-C Cor 2.4)
For $T = (y,t)$ and $V = (v_1,v_2)$ the reverse pair has offset
$\delta' = (v_1-y+c)/A = \rho(\delta)$ where $\rho(\delta) := 2c/A - \delta$. Writing
$A_0 := \{d : a_d = 0\}$ for the *degenerate set*, in this family:

- **(a)**  if $(\mathrm{S\text{-}off})$ fails then $A_0\cap\rho(A_0)\ne\emptyset$ (no
hypothesis on $|M|$);

- **(b)**  *provided $|M|\ge 3$*, the converse holds as well, so

$$

  (\mathrm{S\text{-}off})  \text{holds} \iff A_0\cap\rho(A_0) = \emptyset .

$$

For $c=0$ this reads $A_0\cap(-A_0) = \emptyset$: the degenerate set must be antisymmetric.

*Proof.* 
(a) A failure at the pair $(T,V)$ needs $N(T,V) = N(V,T) = 0$, and by Lemma 4.5
each vanishing forces the corresponding offset to lie in $A_0$; those offsets are $\delta$
and $\rho(\delta)$.
(b) Given $\delta\in A_0\cap\rho(A_0)$, fix base coordinates $y,v_1$ realizing $\delta$;
these satisfy $y\ne v_1$ unless $\delta = d^{*} := c/A$, and $d^{*}\notin A_0$ by
Theorem 4.8 below, so $y\ne v_1$ and hence $T\ne V$. By
Lemma 4.5 the pair $(t,v_2)\in M^2$ fails to give a violation only if
$b_\delta t + c_\delta = v_2$ or $b_{\rho(\delta)}v_2 + c_{\rho(\delta)} = t$; each condition
excludes exactly $|M|$ of the $|M|^2$ pairs, so at most $2|M|$ are excluded, and
$|M|^2 > 2|M|$ exactly when $|M|\ge 3$.
 ∎

*The hypothesis $|M|\ge3$ in (b) is necessary as stated*: at $|M|=2$ one has
$|M|^2 = 2|M|$ and the two hit conditions can cover all four pairs, so the index condition
need not produce a violating pair. The order-$176$ magma has $|M| = 16$, and the whole
discussion below is for $|M|\ge 3$; see also Proposition 5.9, where
$|M|=2$ is disposed of on other grounds.

**Lemma 4.7 (position conflicts).** 
✅ PROVED (R5-C Lemma 2.5) 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/conflict_check.py)
In (E1)–(E2) with all $b_j\ne 0$:

$$

  a_1 = 0 \implies a_3\ne 0 \text{ and } a_4\ne 0, \qquad
  a_2 = 0 \implies a_4 \ne 0,

$$

and no other implication holds: exactly the eight degeneracy patterns

$$

  \emptyset, \{1\}, \{2\}, \{3\}, \{4\}, \{1,2\}, \{2,3\}, \{3,4\}

$$

are realizable. Equivalently, the
*forbidden* position pairs are $\{1,3\}$, $\{1,4\}$, $\{2,4\}$.

*Proof.* 
If $a_1=0$, (E2) gives $a_4a_3 = -b_4 \ne 0$, so $a_3,a_4\ne 0$. If $a_2=0$, (E1) gives
$b_1b_2a_4b_3 = 1$, so $a_4\ne 0$. Realizability of the remaining patterns is exhibited by
direct solution; exhaustive enumeration over $\mathrm{GF}(3),\mathrm{GF}(4),\mathrm{GF}(5),
\mathrm{GF}(8)$ prints exactly those eight patterns and no conflict violation.
 ∎

### 4.4 Why the diagonal survives: the $\{1,3\}$ subscript collision

This is the sharpest structural statement the campaign produced, and it is a complete answer
for the family in which the counterexample lives. Setting $t=v$ in $(\mathrm{S\text{-}off})$
gives $N(v,v)\ge1$, i.e. $E255$. Both cases are governed by the *same* criterion of
Corollary 4.6, but at *different* indices:

-  *off-diagonal* (base coordinates $y\ne v_1$): the two offsets are $\delta$ and
$\rho(\delta) = 2c/A-\delta$, two *distinct* indices; both must be degenerate for a
failure;

-  *diagonal* ($y=v_1$): here $\delta = \rho(\delta) = c/A$, and a failure would need
the *single* index $d^{*} := c/A$ to be degenerate.

**Theorem 4.8 (diagonal protection).** 
✅ PROVED (R5-C Thm 5.1) 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/conflict_check.py `diag_check`)
For every translation-invariant base ($A+B=1$, $A,B\ne 0$, any $c$) and every field of fibre
scalars, if the fibre operations are *affine* $s\diamond_d t = a_ds+b_dt+c_d$ then
$a_{c/A}\ne 0$. Consequently $E255$ holds in the entire translation-invariant blueprint
family *with affine fibres*, however those fibre operations are chosen.

*Proof.* 
Take the instance of (4.1) at parameter $d = -c/A$. Then

$$

  D_3(-c/A) = c/A = d^{*}, \qquad
  D_1(-c/A) = -\frac{-c/A + c}{B} = -\frac{c(A-1)}{AB} = \frac{c}{A} = d^{*}
  \quad(\text{using } A-1 = -B).

$$

So positions $1$ and $3$ carry the *same* index $d^{*}$. If $a_{d^{*}} = 0$ then
$a_1 = a_3 = 0$, contradicting the forbidden pair $\{1,3\}$ of Lemma 4.7.
The index coincidence was machine-checked for every TI base with
$p\in\{5,11,31,41,61,71\}$.
 ∎

**Remark (scope — an internal correction).** 
An intermediate report summary claimed that “the entire TI blueprint family satisfies
$E255$” without qualification. That is *not* what is proved: Theorem 4.8
assumes affine fibre operations (§4.3, Lemma 4.4 is stated
for affine fibres). A general-table TI fibre assignment, or a shift ansatz
$T_\delta(s,t) = s+g_\delta(t-s)$ with arbitrary $g_\delta$, is *not* covered by
Theorem 4.8. Searches over those remain open (§5.8). The
unqualified reading is recorded here only to be retracted.

**Theorem 4.9 (the exact off-diagonal gap).** 
✅ PROVED (R5-C Thm 5.2)
For an off-diagonal pair the relevant index pair is $(\delta,\rho(\delta))$ with
$\rho(\delta) = 2c/A-\delta$, and (4.1) forbids simultaneous degeneracy *only*
when $\rho$ coincides with one of the three conflict maps

$$

  \sigma_1(e) = \frac{e-c}{B}, \qquad
  \sigma_2(f) = -\frac{f+c(1+B)}{B^2}, \qquad
  \sigma_3(f) = \frac{(A^2+B)(f+c)}{B}+(A+1)c

$$

(arising from the forbidden pairs $\{1,3\},\{1,4\},\{2,4\}$ respectively), or with one of
their inverses. For $c=0$ this happens iff
$-1 \in \{1/B, -1/B^2, (A^2+B)/B\}^{\pm 1}$.

**Corollary 4.10 (why $496$ works and $176$ does not).** 
✅ PROVED (R5-C §2.4) 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/m496.py)
For the blueprint base $A = 1+\beta$, $B = -\beta$, $c = 0$ on $\mathbb{F}_{31}$ with $\beta = 2$ a
primitive $5$th root of unity, one has $A_0 = \{\text{nonzero squares}\}$ and
$\rho(\delta) = -\delta$; the blueprint's own hypothesis “$-1$ is a non-square mod $31$” is
*precisely* $A_0\cap(-A_0)=\emptyset$. So $(\mathrm{S\text{-}off})$ holds in the
order-$496$ magma for a number-theoretic accident of $\mathbb{F}_{31}$, not for a structural reason.
For the base $A=4$, $B=8$, $c=0$ on $\mathbb{F}_{11}$ the three conflict maps of
Lemma 4.7 become multiplication by $7,6,3$ (with inverses $8,2,4$), and
$-1 = 10$ is not among them; so the two-element degenerate set
$A_0 = \{1,-1\} = \{1,10\}$ is admissible, and a SAT search produced a consistent operation
family realizing exactly that $A_0$ — the order-$176$ magma.

**Summary of the $t=v$ mechanism.** The diagonal is protected by an *index
collision* ($D_1 = D_3$ at one specific parameter) which forces the $\{1,3\}$ conflict to
bite; the off-diagonal case involves two generically distinct indices and is protected only by
an arithmetic accident of the base field. So the technique does not “fail at $t=v$”: it
works there and *only* there. In this family the diagonal is strictly *easier* than
the off-diagonal — the opposite of the working hypothesis that motivated the search.

*What generalizes, and what does not.* In the general (non-translation-invariant,
general-table) framework the *subscript* half of the argument survives verbatim:
positions $1$ and $3$ of (4.1)
carry the pairs $(y,\Lambda_yx)$ and $(y,x)$, and they coincide exactly when $y\diamond x = x$,
i.e. exactly at the pair that would have to be degenerate for $E255$ to fail at $x$. The
*conclusion* does not. Lemma 4.7 is a statement about the scalars $a_j$
of *affine* fibre operations: there degeneracy is the single scalar condition $a_d=0$,
which promotes a one-point collision to a collision of whole rows, and it is whole-row
collisions that (E1)–(E2) forbid at positions $\{1,3\}$. For a general fibre table, breaking
$E255$ requires only a *one-point* collision, and no analogue of the $\{1,3\}$ conflict
lemma is known. In particular the statement

*for every $y,x$ with $y\diamond x = x$, the fibre operation $\diamond_{y,x}$ is
left-injective*

is proved here only for affine fibre operations (where it is the mechanism behind
[2, Lemma 13.4]); for general tables it was the open R5-A question
(Problem 11.8). **Note added:** Round 6 settled that question
negatively — see Corollary 7.8. The general-table statement is false, and
the correctly generalized mechanism (Theorems 7.3–7.6) is
Problem 1.1 itself for a smaller magma. The recommendation that stood here in
earlier drafts — “look for the general-magma analogue of this self-referential instance,
not for counting bounds” — is therefore withdrawn in its literal form; what remains of it
is Problem 11.8(b).

### 4.5 Minimality: exactly what was searched

**Proposition 4.11.** 
🧮 COMPUTATIONAL, PARTIAL ($\theta$-family TI extensions with $p\in\{5,11\}$, $q\le 32$) 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/minimal_scan.py)
Within the translation-invariant blueprint family with $\theta$-form fibre operations
$s\diamond t = s-\theta(t-s)$, base prime $p\in\{5,11\}$ and fibre field size $q\le 32$, the
smallest order at which non-right-cancellativity occurs is $176$, and the smallest order at
which $(\mathrm{S\text{-}off})$ fails is $176$. Representative rows of the scan:

| order | $p$ | base $(A,B,c)$ | $q$ | non-cancellative | $(\mathrm{S\text{-}off})$ violation |
|---|---|---|---|---|---|
| $80$ | $5$ | $(2,4,0)$ | $16$ | no | none |
| $125$ | $5$ | $(2,4,0)$ | $25$ | no | none |
| $176$ | $11$ | $(4,8,0)$ | $16$ | **yes** | $(1,10)$ |
| $176$ | $11$ | $(5,7,0)$ | $16$ | no | none |
| $176$ | $11$ | $(6,6,0)$ | $16$ | yes | none |
| $176$ | $11$ | $(10,2,0)$ | $16$ | yes | none |
| $275$ | $11$ | $(4,8,0)$ | $25$ | no | none |

**This is not a minimality theorem.** It states minimality *within the scanned
range and within one ansatz*. Whether a smaller non-right-cancellative finite $E677$ magma
exists at all is open. In particular a *non*-translation-invariant fibre assignment over
$\mathbb{F}_5$ would give order $80$, and was not searched. Independently, a direct small-order SAT
search for any $E677$ magma of order $n$ carrying an $(\mathrm{S\text{-}off})$-violating pair
returned UNSAT for $n = 3,4,5,6,7$; $n=8$ ran $39$ minutes without a verdict and was stopped;
$n = 9,10,11$ were never run 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/soff_sat.py).

**Proposition 4.12 (no equational witness for $(\mathrm{S\text{-}off})$ was ever possible).** 
✅ PROVED (R5-C §4.4) 🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/freemagma.py)
In the free $677$ magma of [2, §13.2], let $t\ne v$ be two distinct generators.
Since $t$ is not a pair, the collapsing clause can never fire with right argument $t$, so
$a\diamond t = (a,t)$ for every $a$, which is a pair and hence never equal to the generator
$v$. Thus $N(t,v) = 0$, and symmetrically $N(v,t) = 0$. Hence $(\mathrm{S\text{-}off})$ fails
in the free $677$ magma already, and no derivation of it from the $E677$ identities alone can
exist; any proof had to use finiteness.

*Honest caveat.* The free $677$ magma has $L_y$ surjective but not necessarily injective,
so it is a $677$ magma but need not be a left quasigroup. Proposition 4.12
therefore excludes proofs in the language $\{\mathbin{*}\}$; it does not by itself exclude proofs in
$\{\mathbin{*},\backslash\}$. The order-$176$ magma excludes those too.

**Remark (a single-model coincidence, recorded so that nobody chases it).** 
In the order-$496$ magma, on *all* $111\,600$ ordered pairs where the direction is forced
($N(v,t)=0$, so $(t,v)$ must carry the witness, and there $N(t,v)=1$), the unique witness
equals $w(t,v) = \bigl((t\backslash v)\mathbin{*}(t\mathbin{*} v)\bigr)\mathbin{*} v$
🖥️ MACHINE-VERIFIED (problems/etp677/R5C_scripts/term_full_check.py). (The term was *found* by
`term_search.py`, which searches on a deterministic random sample of $1200$ of those
pairs; the all-pairs statement is the separate full-domain check
`term_full_check.py`, which also reports that the predicate
$w(t,v)\mathbin{*} t = v$ is false on all $111\,600$ pairs forced in the other direction.)
This is a single-model coincidence;
Proposition 4.12 shows no term identity of this kind can be a theorem. And had
the *conditional* form “$N(t,v)=0 \Rightarrow w(v,t)\mathbin{*} v = t$” been a theorem, at
$t=v$ it would read “$N(v,v)=0 \Rightarrow N(v,v)\ge1$”, i.e. $E255$ — so the
conditional-witness route is not easier than the main problem.

## 5. The obstruction map: routes that are closed

A campaign of this kind produces more closed routes than open theorems, and the closed routes
are the more reusable output: each one is a statement about what a proof of
Problem 1.1 may not do. This section collects them. They are stated with their
exact strength — “provably circular”, “refuted by an explicit model”, and “exhausted
under a stated computational budget” are three different things and are not conflated.

### 5.1 Equational and quasi-equational derivations

**Proposition 5.1 (the equational meta-theorem).** 
🧮 COMPUTATIONAL (F5 §4, scripts `saturate.py`, `saturate2.py`, `saturate3.py`)
Consider the theory $T := \{\text{left quasigroup}\} + E677$ in the signature
$\{\mathbin{*},\backslash\}$, with congruence closure under sound merges only, so that any derived
equality is a theorem of $T$.

- **(a)**  Depth-bounded *full* saturation — all instances, all terms up to depth $d$
— is complete for $d\le 4$ ($1693$ classes, $27$ merges) and derives neither
$c(a) = a$ nor $a\mathbin{*} a = a$. At $d = 5,6$ the closure passes $400\,000$ classes without
deriving anything.

- **(b)**  Pool-restricted saturation with *unbounded* term depth, instantiating $E677$
and $\mathrm{KEY}$ at all pairs from
$\{\Lambda_a^{-k}(a) : |k|\le K\}\cup\{S,\delta,c\}$ for $K\le 6$ and iterated to a fixed
point, leaves the pool at $2K+1$ distinct classes (no collapse) and does not derive
$c(a)=a$.

Since the free $677$ magma violates $E255$ [2, §13.2], any proof must use
finiteness, and the only first-order consequence finiteness supplies is left cancellation.
Item (b) is significant because the empirically minimal set of $E677$-instances whose failure
destroys $E255$ (§6.4) lies *inside* the saturated pool.

**Reading — and what this does *not* say.** Proposition 5.1 reports
depth-bounded and pool-restricted saturation experiments. Failure of a bounded search to
derive $E255$ or $(\mathrm{Q})$ is *not* a proof that no equational or quasi-equational
derivation exists; unbounded saturation is not a decision procedure here, and no
underivability certificate was produced. What the experiments support is the weaker,
heuristic statement that the natural first-order strengthening does not collapse under the
strongest saturation we could run, which is evidence — not proof — that a proof of
Problem 1.1 will have to use a global counting or finiteness argument rather than
an equational manipulation. A genuine theorem of this shape does exist for the
*sibling* statement, but only in the language $\{\mathbin{*}\}$: Proposition 4.12
proves that $(\mathrm{S\text{-}off})$ has no derivation from the $E677$ identities alone, and
even that argument does not reach the left-quasigroup (quasi-equational) setting, as the
caveat after it records.

A separate bounded search for an equational derivation of *mediality* from $E677$ plus
the left-division equations reached $168\,182$ distinct terms per side with at most $9$
operation nodes and rewrite depth $\le 3$, without the two closures meeting; a larger run with
at most $17$ operation nodes hit an explicit cap of $250\,000$ states per side, and is
truncated evidence only 🧮 COMPUTATIONAL, PARTIAL (R3-F, `r3f_saturation.py`). This does not show
mediality is underivable.

### 5.2 The state map is circular

Iterating the master identity (2.2) produces a canonical dynamical system on the
witness set, and it is the most natural finite-pumping mechanism available. It was pursued as
the campaign's Round-2 main line [9], and it is provably circular.

**Theorem 5.2 (circularity of the state map).** 
✅ PROVED (R2 §2, (10); recoordinatized in R3-C)
Let $\mathcal E := \{(t,v,x) : x\in\operatorname{Fix}(L_tR_v)\}$, so $|\mathcal E| = n^2$ by
Theorem 2.20. Then

$$

  T(t,v,x) := \bigl(v, \Lambda_t x, \Lambda_v x\bigr)

$$

is a well-defined self-map of $\mathcal E$, and

$$

  T \text{ is injective on } \mathcal E
  \iff T \text{ is surjective on } \mathcal E
  \iff (\mathrm{Q}) .

$$

*Proof.* 
Well-definedness: let $x\in F(t,v)$ and set $p := \Lambda_tx = x\mathbin{*} v$, $c := \Lambda_v x$;
(2.2) with $y=v$, $u=x$ yields $c\mathbin{*} p = \Lambda_v c = \Lambda_v^2 x$, so
$c\in F(v,p)$. For the equivalence: given a target $(v,p,c)$, set $x := L_vc$; the target
equation and (2.2) imply $p = x\mathbin{*} v$, and a preimage under $T$ is obtained by
choosing $t$ with $\Lambda_t x = p$, equivalently $t\mathbin{*} p = x$. So the number of preimages of
$(v,p,c)$ is exactly $|\{t : t\mathbin{*} p = x\}| = N(p,x)$, and $T$ is bijective iff all such fibres
are singletons, which is $(\mathrm{Q})$.
 ∎

Writing the iteration as $t_{k+1} = v_k$, $v_{k+1} = \Lambda_{t_k}x_k$,
$x_{k+1} = \Lambda_{v_k}x_k$ makes the failure mode explicit: finiteness guarantees that every
forward orbit is eventually periodic, but not that the *initial point* is periodic. A
non-injective $T$ can have tails feeding cycles, and excluding those tails is exactly the
injectivity assertion. Moreover the subscripts of successive $\Lambda$'s change along the
orbit, so the finite order of any single permutation $\Lambda_y$ does not close it.

The same circularity afflicts a variant proposed as an “easier foothold”: with
$P := \{(t,v,A) : A\mathbin{*} v = \Lambda_t(A)\}$ (of size $n^2$) and
$\Xi(t,v,A) := (v,\Lambda_t A,\Lambda_v A)$, one has $\Xi$ injective $\iff (\mathrm{Q})$,
while surjectivity of $\Xi$ would suffice; but surjectivity is Theorem 5.2 again.

### 5.3 Pure marginal counting on $N$

**Proposition 5.3 (marginal insufficiency).** 
✅ PROVED (R2 §3, (17))
The constraints available on $N$ from margins alone — all row sums and all column sums equal
$n$, diagonal entries $\le 1$, and the support bound $N(t,v)\le s(v) := |\{p : N(v,p)>0\}|$
— do not force $N\equiv 1$. The matrix

$$

  \begin{pmatrix} 0&1&2\ 1&1&1\ 2&1&0 \end{pmatrix}

$$

has all row and column sums $3$, diagonal entries $\le 1$, and satisfies the support bound
(the row support sizes are $2,3,2$), yet is not all-ones. *A constraint linking distinct
entries of $N$ is required.*

The matrix above is not asserted to arise from an $E677$ magma; it demonstrates only that the
current counting inequalities are insufficient. Theorems 2.22 and 2.23 are
genuine linking constraints of the required kind — and they are still not enough:

**Proposition 5.4 (A + B + the transport are still insufficient).** 
🧮 COMPUTATIONAL (R3-C §2.4, machine-checked certificate)
There is a $5\times5$ nonnegative integer matrix $N$ with row and column sums $5$, diagonal
$\equiv 1$ (so $E255$ “holds”), strongly connected support (Theorem 2.22 holds, with
minimal Theorem 2.23 slack $4.0$ over all $30$ proper subsets), realizable transport
data, and $N\not\equiv 1$:

$$

  N = \begin{pmatrix}
    1&0&2&2&0\ 0&1&2&2&0\ 2&1&1&0&1\ 0&1&0&1&3\ 2&2&0&0&1
  \end{pmatrix},
  \qquad
  \begin{aligned}
    f_0 &= (2,2,0,3,3), & f_1 &= (2,1,2,3,3), & f_2 &= (2,1,0,0,4),\\
    f_3 &= (4,4,1,3,4), & f_4 &= (0,1,1,0,4). &&
  \end{aligned}

$$

Machine-checked: $|f_t^{-1}(v)| = N(t,v)$ for all $t,v$; $N(f_t(u),u)>0$ for all $t,u$; row
and column sums; $\operatorname{tr} N = n$; strong connectivity.

### 5.4 The transport tree and the pair rotation

Two mechanisms were proposed in Round 3 for producing the missing linking constraint. Both are
dead, and the reasons are worth recording because they are the kind of error that looks like
progress.

**Proposition 5.5 (the transport tree has branching factor $1$).** 
✅ PROVED (R3-C §2)
Write $\tau(a,t) := (\Lambda_ta, a\mathbin{*} t)$ for the *transport map* on $M^2$; it is a
two-coordinate map and must not be confused with the three-coordinate state map $T$ of
Theorem 5.2.
Let $a\in F(t,v)$ (i.e. $a\mathbin{*} t = v$). Then $\tau(a,t) = (\Lambda_ta, v)$ is a witness of the
fibre $(v,\Lambda_t^2(a))$, so the map $F(t,v)\to \operatorname{supp}(\text{row } v\text{ of }N)$,
$a\mapsto\Lambda_t^2(a)$, is injective and $N(t,v)\le r_v$ (Definition 2.18). But the
iteration
adds nothing further:

- **(a)**  Each *point* $(a,t)\in M^2$ has exactly one image $\tau(a,t)$: the transport
is a
function, not a correspondence. “A fibre of size $k$ spawns $k$ children” means the $k$
points have $k$ images which lie in $k$ distinct fibres. It is the same $k$ objects,
redistributed. The “tree” is simply the functional graph of $\tau$, with out-degree $1$ at
every
node and total mass exactly $n^2$ at every depth. *Mass is conserved identically at every
level*, so no pigeonhole on $n^2$ and no forced row-sum overflow can ever arise.

- **(b)**  Distinctness survives to depth $2$ and no further: at depth $1$ the images lie in
$k$ distinct fibres, at depth $2$ they lie in $k$ distinct *rows* of $N$, and at depth
$\ge 3$ two paths merge exactly when a $\tau$-collision occurs — which is a right-collision,
i.e. the failure of $(\mathrm{Q})$ itself.

- **(c)**  The full combinatorial content of the transport is: for each $t$ there is a
function $f_t : M\to M$ (explicitly $f_t = R_tL_t^2$, i.e. $f_t(u) = (t\mathbin{*}(t\mathbin{*} u))\mathbin{*} t$) with fibre sizes $|f_t^{-1}(v)| = N(t,v)$ and
$N(f_t(u),u)>0$ for every $u$. The last condition is a *tautology*: for any $s,u$ one has
$s\mathbin{*}(\Lambda_su) = u$, so $N(\Lambda_su,u)\ge1$ automatically, with no algebra used.

**Proposition 5.6 (the pair rotation carries no $E677$ information).** 
✅ PROVED (R3-C §3) 🧮 COMPUTATIONAL (cycle data on ten affine models)
$P(r,s) := (r\mathbin{*} s, r)$ is a bijection of $M^2$ for *every* left quasigroup, with
$P^{-1}(u,r) = (r,\Lambda_ru)$; $E677$ is nowhere used. Its iterates satisfy
$x_{k+1} = x_k\mathbin{*} x_{k-1}$, and the $E677$ side condition
$x_{k-1} = x_k\mathbin{*}(x_{k-1}\mathbin{*} x_{k+2})$ is *literally* the transport identity
(2.3) again. Moreover $P$'s cycle type is wildly model-dependent — two affine
models of the same order $11$ have identical $P$-type but different $\tau$-type, and two
others
have $\tau$-type equal to $P$-type — so there is no cycle-type invariant to count two ways,
and
$\tau$ is never a power of $P$. The dictionary is
$\tau(x_k,x_{k-1}) = (x_{k-2},x_{k+1})$: the transport is one $P$-step backwards in the first
coordinate and one $P$-step forwards in the second, which is exactly why it mixes distinct
$P$-orbits and why $P$-orbit bookkeeping cannot see it. (Here $\tau$ is the transport map of
Proposition 5.5, not the state map $T$ of Theorem 5.2.)

### 5.5 Local amplification of the row-distance bound is capped

Theorem 2.17 gives $|F_{pq}|\le\lfloor n/2\rfloor$; the Latin property needs $0$. The
obvious plan is to amplify by finding more maps that move $F_{pq}$ off itself. It amplifies
cleanly and does not amplify numerically [10].

**Theorem 5.7 (amplification cap).** 
✅ PROVED (R3-A) 🖥️ MACHINE-VERIFIED (problems/etp677/r3a_search.py)
Fix $p\ne q$ and let $F := F_{pq}$.

- **(a)**  For every $x\in F$ all four immediate neighbours $L_px$, $L_qx$, $\Lambda_px$,
$\Lambda_qx$ lie outside $F$.

- **(b)**  But $L_px = L_qx$ on $F$, so the three image sets are $B := L_p(F) = L_q(F)$,
$C := \Lambda_p(F)$, $D := \Lambda_q(F)$, each of size $|F|$, and the proved disjointness is
only $A\cap B = A\cap C = A\cap D = \emptyset$ where $A := F$. Explicit five-element
partial-$\mathrm{KEY}$ tables satisfying global (L4) realize each of
$B\cap C$, $B\cap D$, $C\cap D$, $C\cap C'$ nonempty. Hence $n\ge|A\cup B| = 2|F|$ and one
cannot replace $2|F|$ by $3|F|$ or $4|F|$.

- **(c)**  All $84$ nonempty words of length $\le 3$ in $\{L_p,L_q,\Lambda_p,\Lambda_q\}$ were
tested against a local SAT model (five distinct elements, every row a permutation, global
(L4), $x,x'\in F$ distinct, the four $\mathrm{KEY}$ instances at $(p,x),(q,x),(p,x'),(q,x')$,
and $x' = w(x)$). Exactly $50$ are UNSAT and $34$ are SAT; and *every* UNSAT case is
either a one-step exclusion from (a) or a reduction to $x$ or to a one-step exclusion. The
$34$ locally feasible words include $\Lambda_p\Lambda_q$, $\Lambda_p^2$, $L_p^2$, $L_pL_q$ and
their mixed analogues. The nonlinear candidate $x\mapsto x\mathbin{*} v$ (with $v := p\mathbin{*} x = q\mathbin{*} x$)
is also locally feasible, and its injectivity would already require $(\mathrm{Q})$.

Consequently the bound remains $|F_{pq}|\le\lfloor n/2\rfloor$: *the four-instance
$\mathrm{KEY}$ package is exhausted.*

*Proof of (a).* 
Let $a := \Lambda_px$. If $a\in F$ then $p\mathbin{*} a = x = q\mathbin{*} a$, hence
$\Lambda_px = a = \Lambda_qx$; combined with $p\mathbin{*} x = q\mathbin{*} x$, (L4) gives $p=q$. Same for
$\Lambda_qx$. For $L_px = L_qx = v$: if $v\in F$ then $p\mathbin{*} v = q\mathbin{*} v$, while
$p\mathbin{*} x = q\mathbin{*} x = v$ gives $\Lambda_pv = x = \Lambda_qv$, so (L4) at $v$ gives $p=q$.
(As a degenerate subcase, $v=x$ is impossible for the same reason.)
 ∎

**Exact remaining obstruction.** The four $\mathrm{KEY}$ instances keep the $x$- and
$x'$-packages separated unless a proposed word identifies an immediate
predecessor/successor, and those identifications are precisely the (L4) proofs above. Longer
words introduce fresh table entries rather than a second product-and-division equality at a
common point. Any continuation must propagate $\mathrm{KEY}$ to those fresh entries and use
finiteness to make two chains meet; listing more short words provably cannot improve the
bound.

### 5.6 Parity, sign, $2$-adic and Sylow-$2$ routes

**Proposition 5.8 (the sign identity is true and empty).** 
✅ PROVED (R3-B Prop 5) 🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/analysis.py)
For any finite left quasigroup $(M,\mathbin{*})$ of order $n$, the bijection $P(r,s) = (r\mathbin{*} s, r)$
satisfies

$$

  \mathrm{sign}(P) \;=\; (-1)^{n(n-1)/2}\cdot\prod_{y\in M}\mathrm{sign}(L_y).

$$

But it carries no parity information: on genuine $E677$ models both $\mathrm{sign}(P)$ and
$\prod_y\mathrm{sign}(L_y)$ take both values already at $n = 7$. Hence no identity of the
shape “$\mathrm{sign}(P) = \varepsilon(n)$” or “$\prod_y\mathrm{sign}(L_y) = \varepsilon(n)$”
can hold, and no sign invariant of $P$ can force $n$ odd.

*Proof.* 
Let $D(r,s) := (r,r\mathbin{*} s)$, which acts on each fibre $\{r\}\times M$ by $L_r$, so
$\mathrm{sign}(D) = \prod_r\mathrm{sign}(L_r)$. Let $\mathrm{sw}(a,b) := (b,a)$ (the
coordinate swap — unrelated to the transport map $\tau$ of
Proposition 5.5); $\mathrm{sw}$ fixes the $n$
diagonal points and swaps the $n(n-1)/2$ unordered off-diagonal pairs, so
$\mathrm{sign}(\mathrm{sw}) = (-1)^{n(n-1)/2}$. Finally $P = \mathrm{sw}\circ D$.
 ∎

Combined with Theorem 3.4 and Corollary 3.5, this closes the whole
family: fixed-point parity and odd-cycle counting fail because the two order-$16$ models have
completely different cycle data ($L_y$ of type $(5,5,5,1)$ for all $y$ versus $(15,1)$ for all
$y$) at the same even order; the cycle-length obstruction $m(y)\notin\{2,3\}$ is genuine but
does not interact with parity; and even order forces nothing about idempotents ($16$
idempotents in one order-$16$ model, $1$ in the other). **Any global mechanism for
Problem 1.1 must be insensitive to the parity of $n$.**

### 5.7 The off-diagonal and isoperimetric programme

This is Section 4 restated as a closure. The order-$176$ magma refutes:

-  any constraint of the form $N(t,v)+N(v,t)\ge k$ for $t\ne v$ with $k\ge1$;

-  $N+N^{\mathsf T} = 2J$ and $N+N^{\mathsf T}\ge 2J-I$;

-  the isoperimetric threshold $e(O)\le|O||O^c|$, uniformly over any one size class
$2\le s\le n-2$ — which is precisely the premise of the R3-C averaging implication.

$N$'s off-diagonal support carries no usable information: it can be arbitrarily holey in both
directions simultaneously while $E255$ holds.

*Scope.* The third item refutes one specific threshold, not “every isoperimetric upper
bound”. Uniform upper bounds on $e(O)$ certainly exist — $e(O)\le n|O|$ is trivial —
and the order-$176$ magma says nothing about thresholds other than $|O||O^c|$, nor about
bounds restricted to a family of sets that is not a full size class. What is closed is the
R3-C averaging route in the form in which it was proposed.

The diagnosis is a *direction mismatch*, and it was visible before the counterexample.
Theorems 2.22 and 2.23 are *lower* bounds on $e(O)$, obtained by
propagating $\mathrm{KEY}$ through an invariant set; the transport gives only support
information ($N(t,v)\le r_v$ is an “enough room” statement); $E255$ needs an *upper*
bound on $e(O)$ at the threshold $|O||O^c|$. No mechanism in the campaign produced such an
upper bound, and Corollary 4.2(c) shows that no bound at that threshold can hold
uniformly over a size class.

### 5.8 The extension framework: where a counterexample could still live

Within the blueprint extension framework of §4.3, three obstructions carve out
the remaining habitat.

**Proposition 5.9 (affine fibres are blocked; and $m=2$ is always affine).** 
✅ PROVED ([2, Lemma 13.4] and Theorem 4.8; the $m=2$ statement is
proved below)
Theorem 4.8 (equivalently [2, Lemma 13.4]) forces $E255$ for every
affine fibre extension of a base satisfying $E255$. The mechanism is exactly the $\{1,3\}$
subscript collision of §4.4: affinity turns a would-be single-point collision into
a whole-row collision, and [2, Lemma 13.4] only excludes whole-row collisions,
whereas violating $E255$ needs only a single point. A general (non-affine) fibre table does
not force the promotion. Consequently *fibre size $m=2$ cannot produce a counterexample,
and $m\ge3$ is the survival region.*

*Proof of the $m=2$ statement.* 
For the product $(x,s)\mathbin{*}(y,t) = (x\diamond y, s\diamond_{x,y}t)$ to have all rows
permutations, each fibre operation $\diamond_{x,y}$ must have all its rows permutations:
$t\mapsto s\diamond_{x,y}t$ is a bijection of $M$ for every $s$. If $|M| = 2$, say
$M = \mathbb{F}_2$, the only bijections of $M$ are $t\mapsto t$ and $t\mapsto t+1$, so
$s\diamond_{x,y}t = t + \varepsilon(s)$ for some function $\varepsilon:\mathbb{F}_2\to\mathbb{F}_2$; and
*every* function $\mathbb{F}_2\to\mathbb{F}_2$ is affine, $\varepsilon(s) = \alpha s+\gamma$ with
$\alpha = \varepsilon(1)+\varepsilon(0)$, $\gamma = \varepsilon(0)$. Hence every admissible
two-element fibre operation is of the affine shape $\alpha s+\beta t+\gamma$ with
$\beta = 1$, and [2, Lemma 13.4] (Proposition 3.7(d)) applies:
the extension satisfies $E255$. There is no genuinely non-affine two-element fibre.
 ∎

**Proposition 5.10 (idempotent-base circularity).** 
✅ PROVED (orchestrating agent, Round 5; recorded in the campaign registry)
Let the base $G$ be a translation-invariant $E677$ model possessing an idempotent, and build
an extension by fibres of size $m$. Then the base's idempotent forces $\delta^{*} = 0$, and
the $d=0$ instance of (4.1) forces the fibre operation $\diamond_0$ to be *itself* an
$m$-element $E677$ magma, while the $E255$-violation clause demands that $\diamond_0$ violate
$E255$. This is circular: a counterexample of order $|G|\cdot m$ built this way requires a
counterexample of order $m$. The same argument applies to non-translation-invariant fibre
assignments: at an instance $(a,a)$ the operation $\mathrm{op}_{(a,a)}$ is forced to be an
$m$-element $E677$ magma required to violate $E255$.

Consequently, within the translation-invariant blueprint framework, a counterexample can only
be built over a base with *no* idempotent at all. The unique such translation-invariant
base is the blueprint's exceptional Type 2 model $x\mathbin{*} y = 5x-4y+c$ on $\mathbb{F}_{31}$ with $c\ne0$,
for which $\delta^{*} = c/5 \ne 0$. (Theorem 7.27 later shows it is the unique
such base over *any* field.)

Note the direction: what forces $\diamond_0$ to satisfy $E677$ here is the *hypothesis*
(4.1) imposed on the fibre family, read at its $d = 0$ instance — not the assumption
that the product magma satisfies $E677$. The distinction is the subject of
Remark (logical status of the collapse; §7.1), and it is what makes this proposition a genuine obstruction
rather than a circular one: the circularity it exhibits is a property of the construction
being attempted, not of the argument.

**Proposition 5.11 (no class-partition ansatz over the exceptional base).** 
✅ PROVED (orchestrating agent, Round 5; recorded in the campaign registry)
For the exceptional base $x\mathbin{*} y = 5x-4y+1$ on $\mathbb{F}_{31}$, the four subscript maps
$d\mapsto D_1,\dots,D_4$ of Lemma 4.4 generate the full affine group
$\mathrm{AGL}(1,31)$ ($21$ is a primitive root of $\mathbb{F}_{31}$, and the maps have no common fixed
point). Since $31$ is prime, this action is primitive and admits no nontrivial block system.
Hence the blueprint's $\{0,\mathrm{QR},\mathrm{QNR}\}$ trichotomy, available for the $c=0$
base, has no analogue at $c\ne 0$: a translation-invariant search over the exceptional base
has no shortcut, and a non-constant solution, if it exists, must be genuinely inhomogeneous.

The associated SAT searches were discontinued on 2026-08-17 (compute-budget decision); only
the runs that terminated are reported, each with its exact status 🧮 COMPUTATIONAL, PARTIAL (R5-A, discontinued):
translation-invariant fibre size $m=3$ over the exceptional base: UNSAT, and (crucially)
UNSAT *also without* the violation clause, so the $m=3$ result says the extension does
not exist at all, not that it satisfies $E255$; non-translation-invariant $m=3$: UNSAT both
with and without the violation clause, giving the machine theorem *the exceptional base
admits no $3$-element fibre extension whatsoever*; for $m=4$: the translation-invariant
search *with* the violation clause is UNSAT (kissat, $\approx 30$ CPU-minutes), while
the two existence questions (translation-invariant without violation, and pair-indexed)
remain open at the time of writing; and $m=5$
is the smallest fibre size *known* to have a nonempty solution space — the constant
family $\diamond_\delta\equiv 2x-y$ over $\mathbb{F}_5$ was verified to give zero violations of
(4.1), hence an order-$155$ product model. At $m=8$ a nonlinear five-operation
partial assignment (“gadget”) on $\mathbb{F}_2^3$, proposed by an independent reasoning model and
re-verified in our parametrization, satisfies both fully determined instances ($d=0$ and
$d=6$) while destroying every left unit in $\diamond_{25}$; however, fixing this particular gadget
(one concrete choice of its parameters $(S,h)$) and searching the remaining $26$ operations
is UNSAT (kissat, under one minute), so that instantiation does not extend. The $m=4$,
$m=5$, $m=7$ and $m=8$ classifications are *not* complete, and no claim is made about
them. A dedicated
backtracking solver and an independent adversarial re-derivation of the encoding are recorded
in [15].

### 5.9 Summary table: the routes and their exact status

| route | status | why |
|---|---|---|
| Equational / quasi-equational derivation of $E255$ or $(\mathrm{Q})$ from $E677$ + left cancellation | *not* closed: computational evidence only | bounded saturation does not collapse (Proposition 5.1); this does not prove underivability. The free-magma argument (Proposition 4.12) is a genuine theorem, but only for the sibling statement $(\mathrm{S\text{-}off})$ and only in the language $\{\mathbin{*}\}$ |
| Injectivity/surjectivity of the state map $T$ on $\mathcal{E}$ | closed (proved circular) | Theorem 5.2 |
| Pure marginal counting on $N$ | closed (counterexample matrix) | Proposition 5.3, Proposition 5.4 |
| Iterated transport tree; pair rotation $P$ | closed (proved) | branching factor $1$ (Proposition 5.5); $P$ is $E677$-free (Proposition 5.6) |
| Local amplification of $\lvert F_{pq}\rvert\le\lfloor n/2\rfloor$ | closed (exhausted, local) | Theorem 5.7: all words of length $\le3$ |
| Parity / sign / $2$-adic / Sylow-$2$ | closed (refuted) | Theorem 3.4, Proposition 5.8 |
| Off-diagonal strengthenings $N(t,v)+N(v,t)\ge k$; the uniform threshold $e(O)\le\lvert O\rvert\lvert O^c\rvert$ over a size class | closed (refuted) | Corollary 4.2, order-$176$ magma. Only this threshold is refuted; other isoperimetric quantities are untouched |
| Affine (linear) models and affine fibre extensions as counterexamples | closed (proved) | Proposition 3.7, Theorem 4.8 |
| Extension over an idempotent-bearing base | closed (proved circular) | Proposition 5.10 |
| $677$-quasigroup $\Rightarrow$ medial $\Rightarrow$ Toyoda | *moot* | requires $(\mathrm{Q})$, which is false (Proposition 2.13) |

**Remark (third-party corroboration).** 
An independent project on the same problem [5], working in purely
combinatorial/graph-theoretic language rather than the quandle/affine framework used here,
independently established that all rows of a finite $E677$ magma are permutations and is
likewise stalled at localized obstructions. That two methodologically disjoint efforts both
report “local mechanisms are systematically insufficient” is the strongest evidence
available that the remaining step is global.

## 6. The small-order landscape

### 6.1 Complete classification up to order $9$

**Theorem 6.1 (classification for $n\le 9$).** 
🧮 COMPUTATIONAL (F1 §5.1 (`cp677.c`) for the full range $n\le9$; corroborated over smaller
ranges by F5 §5.3 ($n\le7$), R2 §5 ($n\le6$) and R3-B `search.c`
(emptiness/nonemptiness only, $n\le9$) — see §6.1)
The finite $E677$ magmas of order $\le 9$ are exactly the following.

| $n$ | # labelled | up to iso. | $E255$? | quasigroup? | description |
|---|---|---|---|---|---|
| $1$ | $1$ | $1$ | yes | yes | trivial |
| $2$ | $0$ | — | — | — | *no model* |
| $3$ | $0$ | — | — | — | *no model* |
| $4$ | $0$ | — | — | — | *no model* |
| $5$ | $6$ | $1$ | yes | yes | dihedral (Takasaki) quandle $x\mathbin{*} y = 2x-y$ over $\mathbb{Z}_5$; $\lvert\operatorname{Aut}\rvert = 20$ |
| $6$ | $0$ | — | — | — | *no model* |
| $7$ | $1680$ | $2$ | yes | yes | $x\mathbin{*} y = 4x+y$ (has a left identity, not idempotent) and $x\mathbin{*} y = 4x+3y$, both over $\mathbb{Z}_7$ |
| $8$ | $0$ | — | — | — | *no model* ($45$ canonical row-$0$ classes, all UNSAT) |
| $9$ | — | $1$ | yes | yes | affine over $\mathbb{F}_9 = \mathbb{F}_3[t]/(t^2+1)$, *not* over $\mathbb{Z}/9$ |

In particular every $E677$ magma of order $\le 9$ is an affine quasigroup and satisfies
$E255$, so there is no counterexample to Problem 1.1 of order $\le 9$.

*Cross-validation, and its exact extent.*
The *complete* classification through order $9$ — counts of labelled models,
isomorphism classes, and the identification of the order-$9$ model — rests on
implementation (i) alone. The other three implementations agree with it, but over
strictly smaller or weaker ranges; we spell this out because “cross-validated four ways”
would overstate it.

- **(i)**  A constraint-propagation
DFS over Cayley-table cells with row `alldifferent` and the derived lemmas as
propagators 🖥️ MACHINE-VERIFIED (problems/etp677/F1_tools/cp677.c), cross-checked at $n\le6$ against naive
brute force and at $n=5,7$ with and without the derived-lemma propagators. *This is the
source of the complete statement through $n = 9$*, including the $45$ canonical row-$0$
classes at $n=8$ and the $67$ at $n=9$.

- **(ii)**  A propagating
backtracking enumerator plus `kissat` encodings 🖥️ MACHINE-VERIFIED (problems/etp677/F5_scripts/enum677.py, sat677.py):
complete classification through $n = 7$ (orders $2,3,4,6$ empty; one class at $5$; two at
$7$). In the report of [8] order $8$ was still undecided and orders $9,10$ were not
reached.

- **(iii)**  A division-row CSP with arc consistency, complete for orders $\le6$ only,
cross-checked by direct
enumeration of all $n$-tuples of row permutations at $n\le4$ ✅ PROVED (R2 §5). Its order-$7$
run was started but not finished, and [9] makes no order-$7$ claim.

- **(iv)**  A C
enumerator with $\mathrm{KEY}$ propagation and the proved prunes of
Lemmas 2.6, 2.15, 2.17 plus isomorphism reduction on row $0$
🖥️ MACHINE-VERIFIED (problems/etp677/R3B_scripts/search.c): independently confirms that
$n = 2,3,4,6,8$ are *empty* and that $n = 5,7,9$ are *nonempty*, with the models
re-verified in Python. It does not report the order-$9$ isomorphism count.

So emptiness at $2,3,4,6,8$ is confirmed twice independently (i)+(iv), the orders $\le 7$
three or four times, and the order-$9$ enumeration *once*.

*On the order-$9$ entry.* The search finds exactly $2$ of the $67$ canonical row-$0$
classes satisfiable, one solution each; these are the same magma relabelled, affine over
$\mathbb{F}_9$ with $(a,b) = (1,t+2)$ and $(1,2t+2)$ — the two parameters are Frobenius conjugates.
We record this as *one* isomorphism class, following [6]; a separate script
[11] refers to “two $\mathbb{F}_9$ models”, meaning the two parameter pairs. *This is
flagged as a point where the two internal reports use “model” with different scopes; the
mathematics is not in dispute.*

### 6.2 Orders $10$ and beyond: exactly what is settled

**Proposition 6.2.** 
🧮 COMPUTATIONAL, PARTIAL (see below)

- **(a)**  There is no *commuting affine* $E677$ magma of order $10$, $12$ or $14$: their
$2$-parts are $2,4,2$, all smaller than $16$ (Theorem 3.4(b)).

- **(b)**  At order $10$, the sub-case $m(0) = 4$ is fully exhausted (all $11$ canonical
row-$0$ classes, $\approx 4\cdot10^8$ nodes, UNSAT). Since $m(y) = 4$ *forces* $E255$ to
fail at $y$ (Theorem 2.15(b)), that sub-case is thereby settled at order $10$. The
remaining classes $m(0) = 5,\dots,10$ ($19$ subproblems) were still running when the
underlying report was written, as was an independent C search
($>1.9\cdot10^8$ nodes, no model found); **all of these were subsequently discontinued
without a verdict** (compute-budget decision, 2026-08-17), so *nothing* is claimed about
$m(0)\ge5$ at order $10$, and in particular $m(y)=5$ is *not* excluded at order $10$.

- **(c)**  Whether a *non-affine* $E677$ magma exists at order $10$, $12$ or $14$ is
**open**. All known models of all orders are affine, so the expected answer is “no”,
making $16$ the expected smallest even order — but this is an expectation, not a theorem.

### 6.3 A deliberately partial order-$11$ census

The following is the campaign's Round-3 census attempt [13], reported with its exact
coverage.

**Proposition 6.3.** 
🧮 COMPUTATIONAL, PARTIAL ($22$ of $87$ pointed cycle types at order $11$; $0$ of $174$ at order $13$) 🖥️ MACHINE-VERIFIED (problems/etp677/r3f_enum.py, r3f_n11_merged.json)
Relabelling an arbitrary element to $0$ and conjugating the left-division row $P_0$ to its
standard pointed cycle representative, and using $m(0)\notin\{2,3\}$
(Theorem 2.15(a)), the order-$11$ classification splits into

$$

  p(10)+p(7)+p(6)+p(5)+p(4)+p(3)+p(2)+p(1)+p(0) = 42+15+11+7+5+3+2+1+1 = 87

$$

pointed cycle types, which cover every isomorphism class at least once. **$22$ of these
$87$ cases have been exhaustively decided, and all $22$ are UNSAT.** The completed cases are
those with $m(0)=1$ and remainder cycle type among
$1^{10}$; $1^{8}2$; $1^{7}3$; $1^{6}2^2$; $1^{6}4$; $1^{5}23$; $1^{5}5$; $1^{4}2^3$;
$1^{4}24$; $1^{4}3^2$; $1^{4}6$; $1^{2}2^{2}3$; $1^{3}25$; $1^{3}34$; $1^{3}7$;
$1^{2}2^4$; $1^{2}2^{2}4$; $1^{2}23^2$; $1^{2}26$; $1\,2^{3}3$; $1\,2^{2}5$; $2^5$,
totalling $6\,592.116$ durable solver-seconds with `kissat` 4.0.4.

**This is not a classification of order $11$.** $65$ of the $87$ cases are undecided.

**Proposition 6.4 (the affine benchmark at orders $11$ and $13$).** 
🖥️ MACHINE-VERIFIED (problems/etp677/r3f_enum.py)
Over $\mathbb{Z}_{11}$ the affine equations have exactly the four roots
$(F,G) = (10,2), (6,6), (5,7), (4,8)$; the constant multipliers $G^2(F+1)+G+1$ are
respectively $3,6,5,10$, all units, so $c=0$ in every case. Since $F+G=1$ in all four, all
four are idempotent. Their canonical hashes are distinct, so these are four pairwise
non-isomorphic affine isomorphism types: Latin, idempotent Alexander quandles, medial,
satisfying $E255$, each with automorphism group of order $110$. At order $13$ the affine
equations have the single root $G=11$ with $F=9$; here $F+G\ne1$, so translation normalizes
$c$ to $0$, and the affine benchmark is one class.

**Remark (provisional case).** 
The pointed cycle type $1\mid(10)$ at order $11$ — the case in which the four affine models
live — was run far enough to *find* all four, with blocking clauses installed, but the
final UNSAT proof excluding a fifth model did not finish. So “exactly four models of type
$1\mid(10)$” is **provisional** and this case is *not* counted among the $22$
completed cases. Regression censuses at orders $5$ and $7$ with the same enumerator returned
one class and two classes respectively, matching Theorem 6.1.

### 6.4 Near-misses and how thin the implication is

**Proposition 6.5 (an order-$11$ near-miss).** 
🧮 COMPUTATIONAL (F5 §5.1, `nearmiss.py`)
Take the affine $E677$ quandle of order $11$, $x\mathbin{*} y = -x+2y \bmod 11$, and swap the entries
$0\mathbin{*}0$ and $0\mathbin{*}1$ in row $0$. The result is still a left quasigroup, satisfies $E677$ at
$116$ of the $121$ instances — failing exactly at
$(y,x)\in\{(0,0),(0,1),(0,2),(1,6),(4,0)\}$ — and violates $E255$ exactly at $x=0$, where
$c(0)=2$. Columns $0$ and $1$ are the only non-permutation columns, as
Theorem 2.7 requires. The same recipe (one transposition in one row of an exact
model) was checked at the two orders $n=5$ and $n=11$, and yielded exactly $5$ violated
instances at both; *no proof for general orders is available, and the pattern is
recorded as an observation on those two orders only.* In both cases the five violated pairs
are

$$

  (x_0,x_0),\quad (x_0, x_0\backslash x_0),\quad (x_0, x_0\mathbin{*} x_0),\quad
  (x_0\backslash x_0, x_0\backslash(x_0\backslash x_0)),\quad (x_0\mathbin{*}(x_0\mathbin{*} x_0), x_0).

$$

**Proposition 6.6 (exact robustness profile).** 
🧮 COMPUTATIONAL (F5 §5.2, `robust.py` + `kissat`)
Encoding “left quasigroup of order $n$ $+$ $E255$ fails at $0$ $+$ at most $k$ instances of
$E677$ violated” with a sequential-counter cardinality constraint:

| $n$ | minimum number of violated $E677$ instances when $E255$ fails |
|---|---|
| $4$ | **4** ($k\le3$ UNSAT, $k=4$ SAT; violated set $\{(0,3),(1,2),(2,1),(3,0)\}$) |
| $5$ | **5** ($k\le4$ UNSAT, $k=5$ SAT; violated set $\{(0,0),(0,2),(0,3),(1,0),(2,1)\}$) |
| $6$ | $\ge 4$ ($k\le3$ UNSAT; $k=4$ hit the $600$s limit) |
| $11$ | $\le 5$ (explicit witness, Proposition 6.5) |

Note that $k=0$ UNSAT is precisely “no counterexample of order $n$”, so this re-derives the
non-existence results from scratch. The implication is *thin*: it is destroyed by $5$
broken instances out of $n^2$.

**Proposition 6.7 (local repair around the order-$25$ model is excluded to radius $15$).** 
🖥️ MACHINE-VERIFIED (problems/etp677/r3a_search.py)
Take the first-branch model $x\mathbin{*} y = 2x-y$ on the additive group $\mathbb{F}_5^2$ (order $25$; Latin,
$E677$, $E255$; simultaneously a model on the additive groups of $\mathbb{F}_{25}$ and $\mathbb{Z}_5\times\mathbb{Z}_5$).

- **(a)**  Of the $7\,500$ single-row transpositions, exactly $24$ make column $0$ omit $0$,
and every one of those violates exactly five $E677$ instances. Of the $115\,000$ three-cell
single-row derangements, exactly $552$ make column $0$ omit $0$, with violation histogram
$\{7\!:\!24, 8\!:\!48, 9\!:\!480\}$ — so a third changed cell does not repair the
near-miss.

- **(b)**  A SAT encoding (one-hot cells, row-Latin, all $625$ $E677$ instances with one-hot
intermediates, $\neg X[r,0,0]$ for every $r$ (where $X[r,u,v]$ is the cell variable “$r\mathbin{*} u = v$”), and a Sinz sequential counter bounding the
Hamming distance from the model) returns UNSAT for radius $2,3,4,5,6,8,10,12$ and $15$; the
radius-$15$ instance had $56\,235$ variables and $1\,568\,729$ clauses, and subsumes all
smaller radii. **Radius $20$ timed out after $180$ seconds and is recorded as UNKNOWN,
not UNSAT.** No DRAT certificate was requested; these are reproducible solver results, not
proof-assistant-certified exclusions.

**Remark (the second linear branch has no small seed).** 
For $Q(T) = T^4+T^3+2T^2+2T+1$, requiring $Q(G)=0$ with $G+G^3$ invertible, an exhaustive
enumeration found *no* solution in any of: scalar $\mathbb{Z}_{15}, \mathbb{Z}_{21}, \mathbb{Z}_{25}, \mathbb{Z}_{27},
\mathbb{Z}_{33}$, the fields $\mathbb{F}_{25} = \mathbb{F}_5[u]/(u^2+2)$ and $\mathbb{F}_{27} = \mathbb{F}_3[u]/(u^3+2u+1)$, the full
endomorphism ring $\operatorname{End}(\mathbb{Z}_5\times\mathbb{Z}_5) = M_2(\mathbb{F}_5)$ ($625$ candidates), and all $243$
endomorphisms of $\mathbb{Z}_3\times\mathbb{Z}_9$ 🖥️ MACHINE-VERIFIED (problems/etp677/r3a_search.py). Consistently,
$Q \equiv (T^2+2T+2)^2 \bmod 3$ with the quadratic irreducible, and $Q$ is irreducible of
degree $4$ mod $5$. So there is no second-branch seed to perturb at those orders.

### 6.5 The profile a finite counterexample must match

Collecting the pointwise constraints, we record the target profile. Let $M$ be a finite $E677$
magma violating $E255$, of minimum order $n$, and let $y$ be a violating element.

1.  $M$ is $1$-generated as a left quasigroup: the subset generated by $y$ under $\mathbin{*}$ and
$\backslash$ is closed, is again a finite $E677$ magma, and $E255$ still fails at $y$ there;
minimality forces it to be all of $M$.

1.  Column $y$ does not contain the value $y$ (Theorem 2.7); hence $R_y$ is
not surjective, hence not injective, so $M$ is not a quasigroup and some value occurs at least
twice in column $y$.

1.  $y$ has no left unit, while it does have the always-existing unique right unit
$e(y) = \Lambda_y(y)$.

1.  $m(y)\ge 4$ (Theorem 2.15); and $m(y)=4$ automatically violates.

1.  $(y\mathbin{*} y)\mathbin{*} y = \Lambda_y^2(y)$ always, but the $R_y$-orbit of $y$ is a pure tail that
never returns, and $y$ has no $R_y$-preimage at all (Corollary 2.10).

1.  $\Lambda_y^3(y)\mathbin{*} y \ne \Lambda_y^4(y)$; $\Lambda_y^4(y)\mathbin{*}\Lambda_y^4(y)\ne\Lambda_y^5(y)$;
and for *every* $c\in M$, $c\mathbin{*} c\ne y\backslash c$ — the squaring map must avoid the
entire graph of the permutation $\Lambda_y$ (Theorem 2.14). These are $n$
simultaneous disequalities and constitute the sharpest single obstruction available.

1.  $\sum_w|\operatorname{Fix}(L_w)| < n$: the disjoint sets $\operatorname{Fix}(L_w)$ fail to cover $M$, and
$y\notin\bigcup_w\operatorname{Fix}(L_w)$.

1.  $M$ is not affine over any abelian group (Proposition 3.7), and not an
affine fibre extension of an $E255$ base (Theorem 4.8).

1.  $n\ge 10$ (Theorem 6.1); $n\ge11$ if the community's unreviewed DRAT results
for $n\le10$ are accepted. Also $n\ne 8$ since no $E677$ magma of order $8$ exists at all.

1.  Every $L_y$ and every $\Lambda_y$ is still a permutation — that is forced; what must
fail is only the column structure. Concretely $N$ has all row and column sums $n$, $0/1$
diagonal, $N(t,v)\le|\operatorname{Im}(R_v)|$, $\sum_t|\operatorname{Im}(R_t)|\ge n^{3/2}$, strongly connected support
(Theorem 2.22), and at least one diagonal entry $0$.

Item 10 uses two further counting facts we record for completeness.

**Lemma 6.8.** 
✅ PROVED (F1 Lemma H, Cor H2)
With $r_t,c_v$ as in Definition 2.18: $N(t,v)\le r_v$ for all $t,v$, and
$\sum_{t\in M} r_t \ge n^{3/2}$.

*Proof.* 
Let $a\mathbin{*} t = v$. Identity (2.2) with $u:=a$, $y:=t$ gives
$\Lambda_t(a)\mathbin{*}(a\mathbin{*} t) = \Lambda_t^2(a)$, i.e. $\Lambda_t^2(a) = R_v(\Lambda_t(a))\in\operatorname{Im}(R_v)$.
As $a$ ranges over the $N(t,v)$ solutions of $a\mathbin{*} t = v$, the values $\Lambda_t^2(a)$ are
$N(t,v)$ distinct elements of $\operatorname{Im}(R_v)$. For the second claim, let
$\rho := \sum_t r_t = \sum_v c_v$. From
$n = \sum_t N(t,v)\le c_vr_v$ we get $c_v\ge n/r_v$, so $\rho\ge n\sum_v 1/r_v \ge n\cdot n^2/\rho$
by AM–HM, i.e. $\rho^2\ge n^3$.
 ∎

So a finite $E677$ magma cannot be very far from a quasigroup: its columns carry on average at
least $\sqrt n$ distinct values. (Not enough to force $r_t = n$; and the order-$176$ magma has
$r_t = 146$ against $n^{1/2} = 13.3$, so this bound is far from binding in practice.)

### 6.6 Sublemmas that are false

Recorded to save re-derivation. All are refuted by explicit models
🧮 COMPUTATIONAL (F1 §8, R3-B §6).

-  *“Finite $E677$ magmas are idempotent.”* False: in $x\mathbin{*} y = 4x+y$ over $\mathbb{Z}_7$
only $0$ is idempotent.

-  *“Every left translation of a finite $E677$ magma has a fixed point.”* False:
same model, $L_w$ is fixed-point-free for $w\ne0$. So Corollary 2.9's
sufficient condition is strictly sufficient.

-  *“The squaring map $S(c) = c\mathbin{*} c$ is bijective.”* False: for $x\mathbin{*} y = 4x+3y$
over $\mathbb{Z}_7$, $S(c) = 7c = 0$ is constant. So Theorem 2.14(3) cannot be
closed by invoking bijectivity of $S$.

-  *“$\delta(y) = (y\mathbin{*} y)\mathbin{*} y$ is injective.”* False: $\delta\equiv0$ in
$x\mathbin{*} y = 4x+y$ over $\mathbb{Z}_7$.

-  *“$E677$ forces $(y\mathbin{*} y)\mathbin{*} y = y\mathbin{*}(y\mathbin{*} y)$.”* False whenever $m(y)\nmid4$.

-  *“$m(y)\in\{2,3\}$ is a cheap counterexample generator.”* False: those cycle
lengths are impossible (Theorem 2.15(a)). $m(y)=4$ *is* a valid target since
it forces failure, but it is unrealisable for $n\le10$.

-  *“Every finite $E677$ magma has odd order.”* False (Theorem 3.4).

-  *“Every finite $E677$ magma is right-cancellative” ($(\mathrm{Q})$).* False
(Proposition 2.13).

-  *“$N+N^{\mathsf T} = 2J$” and “$N(t,v)+N(v,t)\ge1$ for $t\ne v$”.* Both false
(Corollary 4.2).

-  *“The right-unit map $e(x) = x\backslash x$ is an endomorphism.”* False:
$1050$ of $5929$ violations in $M_{77}^{\mathrm{NT}}$ (Theorem 7.24).

-  *“$e$ is injective.”* False already at order $9$, in the unique $E677$ magma of
that order, where $0$ is a right identity and $e$ is constant
(Theorem 7.25). The two failures are independent: $e$ is bijective in
$M_{77}^{\mathrm{NT}}$ and is an endomorphism in $M_9$.

-  *“Every non-right-cancellative finite $E677$ magma is idempotent.”* True in
every model known before Round 6, and false: $M_{77}$ has $11$ idempotents out of $77$
(Theorem 7.18).

-  *“The blueprint compatibility equations force translation invariance.”* False:
$M_{77}^{\mathrm{NT}}$ (Theorem 7.20), by the diagonal-decoupling
Lemma 7.19.

## 7. Round 6: self-reference, the order-$77$ models, and idempotent-free spectra

The sections above report the campaign as it stood when this draft entered
adversarial review. A sixth round ran afterwards, in five parallel sub-campaigns
[17,18,19,20,21], and its results are collected here rather than woven
into the earlier text, so that a reader can see exactly which statements are new
and what each of them cost. Four of them change the earlier text materially.

1.  The general-magma analogue of the $\{1,3\}$ subscript collision is now
identified exactly. It is a *self-reduction*: it says that
Problem 1.1 holds one level down. In particular
Problem 11.8(a) is answered, and the answer is **no**
(§7.1).

1.  The smallest known non-right-cancellative order drops from $176$ to $77$,
and the order-$77$ model is the first that is *not* idempotent
(§7.3). A second order-$77$ model is the campaign's first extension
that is not translation-invariant.

1.  A new family of counting identities produces an *upper*-bound
criterion for $E255$ of exactly the shape Section 5.7 says is
missing (§7.2) — together with a proof that no term-level witness for
it can exist.

1.  A conjecture that Round 6 itself proposed, “$e(x) = x\backslash x$ is an
automorphism”, was refuted twice over, by two independent mechanisms
(§7.4). The evidence that had supported it was an artefact of the
campaign's benchmark set, which is the third occurrence of one and the same trap;
§7.6 records the pattern as a methodological finding in its own
right, and §7.7 gives the resulting model zoo.

### 7.1 The general-magma $\{1,3\}$ collision is a self-reduction

Write the $E677$ instance at $(y,x)$ as $x = y\mathbin{*}(x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y))$. Its four
multiplication nodes carry the argument pairs

$$

  P_1 = (y, \Lambda_yx), \qquad P_2 = (x, (y\mathbin{*} x)\mathbin{*} y), \qquad
  P_3 = (y, x), \qquad P_4 = (y\mathbin{*} x, y),

$$

which are exactly the indices $D_1,\dots,D_4$ of Lemma 4.4 in the
translation-invariant coordinates. Solving the collision equations gives

$$

\begin{aligned}
  P_1 = P_3 &\iff y\mathbin{*} x = x, &\qquad
  P_2 = P_4 &\iff y\mathbin{*} x = x \text{ and } x\mathbin{*} y = y,\\
  P_1 = P_4 &\iff y\mathbin{*} x = y \text{ and } y\mathbin{*} y = x, &\qquad
  P_2 = P_3 &\iff y = x \text{ and } \delta(x) = x .
\end{aligned}

$$

**Lemma 7.1 (the $\{1,4\}$ and $\{2,4\}$ configurations collapse).** 
✅ PROVED (R6-A Lemmas 1.5 and 1.5b) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
In a finite $E677$ magma: if $y\mathbin{*} x = x$ and $x\mathbin{*} y = y$ then $x = y$ and $x$ is
idempotent; if $y\mathbin{*} x = y$ and $y\mathbin{*} y = x$ then $x = y$ and $x$ is idempotent.

*Proof.* 
First statement: $E677$ at $(y,x)$ reads
$x = y\mathbin{*}(x\mathbin{*}((y\mathbin{*} x)\mathbin{*} y)) = y\mathbin{*}(x\mathbin{*}(x\mathbin{*} y)) = y\mathbin{*}(x\mathbin{*} y) = y\mathbin{*} y$, and
symmetrically $y = x\mathbin{*} x$. Hence $\delta(x) = (x\mathbin{*} x)\mathbin{*} x = y\mathbin{*} x = x$, so $y$
is a left unit of $x$; left units are unique (Theorem 2.7), so
$y = \delta(x) = x$ and then $x\mathbin{*} x = y = x$.
Second statement: $y\mathbin{*} x = y$ says $x = \Lambda_y(y) = y_1$ and $y\mathbin{*} y = x$ says
$x = y_{-1}$; so $\Lambda_y^2(y) = y$, i.e. $m(y)\mid 2$. By
Theorem 2.15(a) $m(y)\ne 2$, so $m(y) = 1$.
 ∎

So of the three forbidden position pairs $\{1,3\}$, $\{1,4\}$, $\{2,4\}$ of
Lemma 4.7, only $\{1,3\}$ — i.e. $y\mathbin{*} x = x$, “$y$ is a left
unit of $x$” — is realisable outside the totally degenerate idempotent case,
where all four positions coincide. That is the configuration to generalize.

**Theorem 7.2 (congruence classes have equal size).** 
✅ PROVED (R6-A Thm 1.1) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
All classes of a congruence $\theta$ on a finite $E677$ magma $M$ have the same
size.

*Proof.* 
$G := M/\theta$ is a finite $E677$ magma. For a class $B$ and $y\in M$ we have
$L_y(B)\subseteq [y]\cdot B$, and $B\mapsto[y]\cdot B$ is the bijection $L_{[y]}$
of the class set. Since $L_y$ is injective, $|L_y(B)| = |B|$, and
$\bigsqcup_BL_y(B)\subseteq\bigsqcup_B[y]\cdot B = M$ with both sides of size $n$;
so $L_y(B) = [y]\cdot B$ and $|B| = |[y]\cdot B|$ for every $B$. By
Theorem 2.22 applied to $G$, the group generated by the $L_{[y]}$ acts
transitively on the classes.
 ∎

**Theorem 7.3 (the total collision: a class is a smaller $E677$ magma).** 
✅ PROVED (R6-A Thm 1.2) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
Let $\theta$ be a congruence on a finite $E677$ magma $M$ and let $X$ be a class
with $X\mathbin{*} X = X$ (i.e. $[X]$ is idempotent in $M/\theta$). Then

- **(a)**  $X$ is closed under $\mathbin{*}$, and $(X,\mathbin{*})$ is itself a finite $E677$
magma;

- **(b)**  for $s\in X$: *$E255$ holds at $s$ in $M$ if and only if $E255$
holds at $s$ in $X$*;

- **(c)**  for all $t,s\in X$ the four positions $P_1,\dots,P_4$ of the $E677$
instance at $(t,s)$ all carry the class pair $(X,X)$ — the *total*
$\{1,2,3,4\}$ collision.

*Proof.* 
(a) Closure is the hypothesis read elementwise; $E677$ is an identity, hence
inherited, and $L_t|_X$ is an injective self-map of the finite set $X$.
(b) If $a\mathbin{*} s = s$ in $M$ then $[a][s] = [s]$ and $[s][s] = [s]$ in $M/\theta$, so
uniqueness of left units in $M/\theta$ (Theorem 2.7) gives
$[a] = [s]$, i.e. $a\in X$; the converse is trivial.
(c) $X\mathbin{*} X = X$ gives $\Lambda_XX = X$, hence $P_1 = (X,X)$; $(X\mathbin{*} X)\mathbin{*} X = X$
gives $P_2 = (X,X)$; $P_3 = (X,X)$; and $P_4 = (X\mathbin{*} X,X) = (X,X)$.
 ∎

**Remark (logical status of the collapse: an observation, never a construction premise).** 
The statement “at a diagonal instance all four positions carry the same subscript, so the
fibre operation there is itself an $E677$ magma” appears twice below, and the two readings
must be kept apart, because one of them would be circular. This paragraph fixes the logical
direction once and for all.

*What it is.* The collapse is a *consequence of idempotency of the base point*: if
$q\diamond q = q$, then the four subscripts $P_1,\dots,P_4$ of the instance at $(q,q)$ are
all equal to $(q,q)$ (Theorem 7.3(c), applied in the quotient). It is thus
an observation about the *structure of one instance* of the system (4.1) —
about which subscripts occur in which positions — derived from idempotency, and on its own
it asserts nothing about any magma.

*The two directions, and where each is used.*

- **(i)**  *Restriction.* If a finite $E677$ magma is *given* and $X$ is a
congruence class with $X\mathbin{*} X = X$, then $(X,\mathbin{*})$ inherits $E677$
(Theorem 7.3(a)). Hypothesis: the large magma; conclusion: the block. This
direction is what Corollary 7.8, §7.6 and
Theorem 7.28 (hence $\mathrm{FiberSpec}(0)\subseteq S$) use, always with the
large magma already in hand.

- **(ii)**  *Construction.* Equation (4.1) is a *hypothesis* imposed on a
fibre family, not a consequence of anything; its diagonal instance, written out, is literally
the $E677$ identity for the single operation $\diamond_{q,q}$. That is an identity between
two explicitly given finite systems of equations, and it may be read in either direction
without any magma being assumed. It is used in the construction direction — exhibit a
$\diamond_{q,q}$, check that it satisfies $E677$, and the diagonal instance of
(4.1) is thereby discharged — in Theorems 7.18 and 7.20, and
nowhere else.

*The circular reading, explicitly disclaimed.* It *would* be circular to infer
“$\diamond_{q,q}$ satisfies $E677$” from “the product magma satisfies $E677$” and then to
use that inference as a step towards proving that the product satisfies $E677$. No argument
in this paper does so: in (i) the product is a hypothesis and the block is the conclusion; in
(ii) neither the product nor the block is assumed — an explicit operation is exhibited and
its equations are verified, by hand and by machine. In particular *no theorem in this
paper takes the collapse as a premise of its proof*; §7.1 draws from it a
*negative* conclusion (Corollary 7.8: the mechanism is a self-reduction,
hence cannot be an engine), which is the opposite of using it as one.

*The non-idempotent branch, for contrast.* If $q$ is *not* idempotent, write $x_q$
for its unique left unit (Theorem 2.7). Then the operation attached to the
pair $(x_q,q)$ occurs in exactly three instances of the system: once at positions $1$ and $3$
simultaneously — the $\{1,3\}$ collision, which holds because $x_q\diamond q = q$ forces
$L_{x_q}^{-1}(q) = q$ — and once each at positions $2$ and $4$ of two further instances. It
is therefore *not* forced to satisfy $E677$, and that is exactly the gap which
Theorem 7.5 measures and which Theorem 4.8 closes only under
affineness. A later round verified that this three-occurrence picture is independent of the
base, on seven different bases ✅ PROVED ([22], Thm R7-B.0); it is stated in full as
Theorem 8.1.

**Corollary 7.4 (what Theorem 4.8 really is).** 
✅ PROVED (R6-A Cor 1.2$'$)
In the translation-invariant family with $c = 0$ the index maps of (4.1)
are linear, so all four vanish at $d = 0$ and the $d=0$ instance of
(4.1) reads

$$

  s \;=\; t \diamond_0\bigl(s\diamond_0((t\diamond_0 s)\diamond_0 t)\bigr)
  \qquad\text{for all } s,t,

$$

i.e. *$(M,\diamond_0)$ is itself an $E677$ magma*. Consequently $a_0\ne0$ is
forced (a left-constant operation cannot satisfy $E677$ on a set of size $\ge2$),
which is Theorem 4.8 at $c = 0$; and $E255$ for the extension at
$(x,s)$ is *equivalent* to $E255$ for $(M,\diamond_0)$ at $s$, which holds
because $\diamond_0$ is affine and affine $E677$ magmas are Latin
(Theorem 3.1(d)). For $c\ne0$ the base is not idempotent, the
classes satisfy $X\mathbin{*} X\ne X$, and only the partial $\{1,3\}$ collision survives.

For the partial collision the conclusion is strictly weaker, and this is the whole
story.

**Theorem 7.5 (the partial $\{1,3\}$ collision gives only non-constancy).** 
✅ PROVED (R6-A Thm 1.3) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
Let $Y,X$ be congruence classes with $Y\mathbin{*} X = X$ and $m := |X| = |Y| \ge 2$. Then
the block map $Y\times X\to X$, $(t,s)\mapsto t\mathbin{*} s$, is *not independent of
$t$*.

*Proof.* 
$Y\mathbin{*} X = X$ gives $\Lambda_YX = X$, and $E677$ in $M/\theta$ gives
$X\mathbin{*}(X\mathbin{*} Y) = \Lambda_YX = X$. Suppose $t\mathbin{*} s = \mu(s)$ for all $t\in Y$,
$s\in X$; then $\mu = L_t|_X$ is a bijection of $X$. $E677$ at $(t,s)$ reads
$s = t\mathbin{*}(s\mathbin{*}(\mu(s)\mathbin{*} t))$ with $s\mathbin{*}(\mu(s)\mathbin{*} t)\in X$, so
$s = \mu(s\mathbin{*}(\mu(s)\mathbin{*} t))$. As $\mu$ is bijective, $s\mathbin{*}(\mu(s)\mathbin{*} t)$ is
independent of $t$; as $L_s$ is injective, $\mu(s)\mathbin{*} t$ is independent of $t$;
but $t\mapsto\mu(s)\mathbin{*} t$ is injective on $Y$. Hence $|Y| = 1$.
 ∎

**Theorem 7.6 (the block problem is Problem 1.1 verbatim).** 
✅ PROVED (R6-A Thm 1.4)
With $Y,X,m$ as above put $\nu(s,s') := \#\{t\in Y : t\mathbin{*} s = s'\}$ for
$s,s'\in X$. Then all row sums and all column sums of the $m\times m$ matrix $\nu$
equal $m$, and $\nu(s,s) = N(s,s)\le 1$. Consequently

-  $E255$ holds at every point of $X$ $\iff$ $\operatorname{diag}\nu\equiv1$
— literally $(\mathrm{P})$ for the block;

-  the block map is left-injective $\iff$ $\nu\equiv1$ — literally
$(\mathrm{Q})$ for the block.

*Proof.* 
Rows: for fixed $s$, $t\mapsto t\mathbin{*} s$ maps $Y$ into $X$. Columns: for fixed $s'$
and each $t\in Y$ there is exactly one $s\in X$ with $t\mathbin{*} s = s'$, because
$L_t|_X$ is a bijection of $X$. Diagonal: $\nu(s,s)\le N(s,s)\le1$ by
Lemma 2.6.
 ∎

**Proposition 7.7 (blocks are arbitrary).** 
✅ PROVED (R6-A Prop 1.6) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_blocks.py)
Let $X$ be *any* finite $E677$ magma and $G$ any finite $E677$ magma with an
idempotent $g$. In $X\times G$ the sets $X\times\{h\}$ form a congruence, the class
over $g$ satisfies $(X\times\{g\})^2 = X\times\{g\}$, and its block operation is
the operation of $X$. So the block at a total-collision pair can be an arbitrary
finite $E677$ magma.

**Corollary 7.8 (answer to Problem 11.8(a)).** 
✅ PROVED (R6-A §1.4–1.6)
The affine conclusion does **not** generalize: there are blueprint extensions
and pairs $y,x$ with $y\diamond x = x$ at which the fibre operation
$\diamond_{y,x}$ is *not* left-injective. Take the direct product
$M_{176}\times G$ with $G$ any $E677$ magma carrying an idempotent $g$
(Proposition 7.7); the block over $g$ is the order-$176$
magma, which is not right-cancellative. What does generalize is
Theorem 7.5 (non-constancy) — and, by
Theorems 7.3 and 7.6, upgrading non-constancy to
left-injectivity *is* $(\mathrm{Q})$ for the block, while the $E255$
statement for the block *is* $(\mathrm{P})$ for the block.

**Remark (why Theorem 4.8 escapes, and what this costs).** 
Theorem 4.8 is true for exactly one reason: in its setting the block is
*affine*, and a non-constant affine map over a field is automatically
injective. Corollary 7.8 says that this is the only reason.
Therefore *the general-magma analogue of the $\{1,3\}$ self-referential
collision is Problem 1.1 itself, one level down*: the mechanism is a
fixed point of the problem and cannot resolve it. This is consistent with the
other half of the same self-reference, already recorded in §6.5:
a minimal counterexample is $1$-generated. The campaign's “single best
recommendation for a continuation” of §4.4 is hereby withdrawn in its
literal form; what survives of it is Problem 11.8(b), the search
for a mechanism that does *not* pass through the block.

### 7.2 The $\Psi$ identities: an upper-bound criterion, and why it has no term witness

Section 5.7 diagnosed the gap as a direction mismatch: every
mechanism in the campaign produces *lower* bounds on the relevant curve mass,
while $E255$ needs an *upper* bound. Round 6 produced a statement of exactly
that shape.

**Theorem 7.9 (column-transport identity).** 
✅ PROVED (R6-A Thm 2.1) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
In every finite $E677$ magma, for every $x\in M$,

$$

  \sum_{z\in M} N(z\mathbin{*} x, z) \;=\; n .

$$

*Proof.* 
$\#\{(a,z) : a\mathbin{*}(z\mathbin{*} x) = z\} = \sum_a|\operatorname{Fix}(L_aR_x)| = \sum_aN(a,x) = n$, using
Lemma 2.19 and the column-sum identity of Theorem 2.20.
 ∎

**Corollary 7.10.** 
✅ PROVED (R6-A Cor 2.1$'$)
Put $A(x,z) := N(z\mathbin{*} x,z)$. Then all row sums and all column sums of $A$ equal
$n$ (rows by Theorem 7.9, columns because $x\mapsto z\mathbin{*} x$ is
a bijection), and $\operatorname{tr} A = \operatorname{tr} N$ (Theorem 7.12 below). Hence

$$

  E255 \iff \operatorname{tr} A \ge n

$$

for an $n\times n$ non-negative integer matrix all of whose line sums are $n$.
This is a genuine constraint linking $N$ to the Cayley table, and it is not inside
the marginal package refuted by Proposition 5.3.

**Definition 7.11 (the curve masses).** 
For $k\in\mathbb{Z}$ put $\Psi_k := \sum_{x\in M} N(x_k,\,x)$, where $x_k = \Lambda_x^k(x)$
as in §2. Thus $\Psi_0 = \operatorname{tr} N$, $\Psi_{-1} = \sum_xN(x\mathbin{*} x,x)$
and $\Psi_1 = \sum_xN(x\backslash x,\,x) = \sum_xN(e(x),x)$.

**Theorem 7.12 (the one shift that is proved).** 
✅ PROVED (R6-A Thm 2.2) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
$\Psi_{-1} = \Psi_0 = \operatorname{tr} N$, via the explicit bijection

$$

  \{(t,x) : t\mathbin{*}(x\mathbin{*} x) = x\} \longrightarrow \{(a,t) : a\mathbin{*} t = t\},
  \qquad (t,x)\mapsto\bigl(t\mathbin{*}(t\mathbin{*} x), t\bigr).

$$

*Proof.* 
By $\mathrm{KEY}$, $\operatorname{Fix}\Theta_t = \{x : (t\mathbin{*} x)\mathbin{*} t = x\} = \{x : t\mathbin{*}(x\mathbin{*} x) = x\}$,
and $|\operatorname{Fix}\Theta_t| = |\operatorname{Fix}(L_tR_t)| = N(t,t)$ by Lemma 2.19. Composing
the two bijections gives the displayed map.
 ∎

**Theorem 7.13.** 
✅ PROVED (R6-A Thm 2.3)
$\Psi_1 \ge n$, because $x\mathbin{*}(x\backslash x) = x$ supplies the witness $a = x$ for
every $x$.

**Corollary 7.14 (the missing upper bound).** 
✅ PROVED (R6-A Cor 2.4)
$\Psi_{-1} = \Psi_0 = \operatorname{tr} N\le n$ and $\Psi_1\ge n$. Hence

$$

  \Psi_1 \le \Psi_0, \text{ i.e. } \sum_x N(x\backslash x,\,x) \le \sum_x N(x,x)
  \quad\Longrightarrow\quad E255 ,

$$

and pointwise $N(x\backslash x,x)\le N(x,x)$ for a single $x$ already gives $E255$
at $x$. More generally, if $v\mapsto N(v,x)$ is constant on the $L_x$-orbit of $x$
— call this $(\mathrm{ORB})$ — then $E255$ holds.

Corollary 7.14 is an *upper* bound on a curve mass, it is
strictly weaker than $(\mathrm{Q})$ (which implies it), and — unlike the
off-diagonal statement $(\mathrm{S\text{-}off})$ — it is *not* refuted by
the order-$176$ magma. Three warnings come with it.

**Remark (logic correction).** 
✅ PROVED (R6-A §7.2)
$\Psi_1 = n$ alone does **not** imply $(\mathrm{P})$: it says only that each
$N(x\backslash x,x) = 1$, which constrains an off-diagonal curve of $N$ and says
nothing about $\operatorname{tr} N$. What implies $(\mathrm{P})$ is $\Psi_1\le\operatorname{tr} N$. In terms
of the sets

$$

  S_1 := \{(a,x) : a\mathbin{*}(x\backslash x) = x\},\qquad
  S_0 := \{(b,t) : b\mathbin{*} t = t\},

$$

with $|S_1| = \Psi_1\ge n$ and $|S_0| = \operatorname{tr} N\le n$, the prize is an
*injection* $S_1\hookrightarrow S_0$, not a bijection $S_1\to M$.

**Theorem 7.15 (no term-definable injection).** 
✅ PROVED (R6-A Thm 7.4, modulo Proposition 5.1)
There is no pair of terms $(\beta,\tau)$ in $\{\mathbin{*},\backslash\}$ such that
$(a,x)\mapsto(\beta(a,x),\tau(a,x))$ maps $S_1$ into $S_0$ injectively in every
finite $E677$ magma.

*Proof.* 
$S_1$ always contains the free diagonal $\{(x,x)\}$, since $x\mathbin{*}(x\backslash x) = x$.
On it the map is $x\mapsto(b(x),t(x))$ with $b,t$ unary terms, and
$b(x)\mathbin{*} t(x) = t(x)$ would be an unconditional identity of the variety. By
Theorem 2.7, $E255$ holds at $t(x)$ for every $x$; injectivity on
the diagonal makes $t$ injective, hence surjective, so $E255$ holds everywhere —
an equational derivation of $E255$ from $E677$ plus the left-quasigroup axioms,
which is what the saturation experiments of Proposition 5.1 failed to
find and what Proposition 4.12 rules out for the sibling statement.
 ∎

Theorem 7.12 does not contradict this: $S_{-1} = \{(t,x) : t\mathbin{*}(x\mathbin{*} x) = x\}$
has *no* unconditional elements, so its bijection to $S_0$ carries no free
diagonal. The pattern — *whenever a candidate mapping has an
unconditionally non-empty source, it cannot be a term map* — recurs below.

**Proposition 7.16 (reformulations).** 
✅ PROVED (R6-A §7.3) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_psi.py)
$\Psi_0 = \#\{(a,p) : R_p(a) = p\}$ and $\Psi_1 = \#\{(a,p) : R_p(a)\in\operatorname{Fix}(R_p)\}$.
Since $\operatorname{Fix}(R_p) = e^{-1}(p)$ and $\sum_p|\operatorname{Fix} R_p| = n$
(Proposition 2.11),

$$

  \Psi_1 = n \iff \text{for every $p$, every fixed point of $R_p$ is its own only
  $R_p$-preimage,}

$$

i.e. $a\mathbin{*}(x\backslash x) = x \Rightarrow a = x$: right cancellation restricted to
the pairs $(x,e(x))$.

**Theorem 7.17 (no term-level up-step).** 
✅ PROVED (R6-A §3.1–3.3) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py)
Full $L_x$-invariance of column $x$ of $N$ — $N(x\mathbin{*} v,x) = N(v,x)$ for all $v$
— is false: $11264$ of $30976$ pairs violate it in the order-$176$ magma and
$238080$ of $246016$ in the order-$496$ magma. Even the support-level statement
fails: the number of columns whose support is $L_x$-invariant is $0$ of $176$ and
$0$ of $496$ respectively. Consequently there is *no* term $T(x,a,v)$ in
$\{\mathbin{*},\backslash\}$ with

$$

  a\mathbin{*}(x\mathbin{*} v) = x \implies T(x,a,v)\mathbin{*} v = x

$$

in every finite $E677$ magma.

*Proof of the last statement.* 
If $T(x,\cdot,v)$ is injective for all $x,v$, the implication injects
$R_{x\mathbin{*} v}^{-1}(x)$ into $R_v^{-1}(x)$, i.e. $N(x\mathbin{*} v,x)\le N(v,x)$; summing
over $v$ gives $n\le n$ with equality forced termwise, i.e. full
$L_x$-invariance. If it is not injective, the implication still gives
$N(x\mathbin{*} v,x)>0\Rightarrow N(v,x)>0$, i.e. support $L_x$-invariance. Both are
refuted by the displayed counts.
 ∎

So the natural route to $(\mathrm{ORB})$ — start from the free fact
$N(x_1,x)\ge1$ and propagate along the $L_x$-cycle back to $x_0$, a genuinely
finite argument not blocked by Proposition 5.1 — is dead at the level
of uniform witnesses. Any proof of $\Psi_1\le\operatorname{tr} N$ must be non-uniform.

**Remark (what the numerics are worth).** 
🧮 COMPUTATIONAL (R6-A Obs. 2.5 on $13$ models; R6-C §6 on the order-$77$ model; root-verified)
$\Psi_k = n$ for all $-6\le k\le6$ on all models the campaign owns, and the
order-$77$ model of §7.3 gives $\Psi_1 = \operatorname{tr} N = 77$ with equality on
its first genuinely non-idempotent test. This looks overwhelming and means very
little: §7.6 explains why, and §7.5 records that
the one explicit design able to falsify $\Psi_1 = \operatorname{tr} N$ — a fibre family with
$a_{-c/B} = 0$ over the exceptional base — provably does not exist for fibre
fields of size $q\le7$.

### 7.3 Two $E677$ magmas of order $77$

Section 5.8 left the extension framework with the record that
*every* known non-right-cancellative model was idempotent, so that every
orbit-type conjecture of §7.2 held vacuously in the entire test bed
(§7.6). The remedy was to put a *non-idempotent* affine
$E677$ magma — the $Q$-branch of Theorem 3.1 — at the
zero-offset fibre, where Corollary 7.4 says the compatibility
equation is literally $E677$ for that one operation.

**Theorem 7.18 (the order-$77$ model $M_{77}$).** 
✅ PROVED (R6-C §§1–4) 🖥️ MACHINE-VERIFIED (problems/etp677/R6C_scripts/r6c_verify.py;
Lean 4 kernel certificate lean/proofenv/M77.lean)
Let the base be $\mathbb{F}_{11}$ with $x\diamond y = 6x+6y$ (translation-invariant, since
$6+6 = 1$), let the fibre be $\mathbb{F}_7$, and put $s\diamond_dt = a_ds+b_dt$ with

$$

  (a_d,b_d) =
  \begin{cases}
    (4,1) & d = 0,\\
    (0,1) & d \in\{1,3,4,5,9\} \text{(nonzero squares)},\\
    (3,5) & d \in\{2,6,7,8,10\} \text{(non-squares)} .
  \end{cases}

$$

Then $M_{77} := (\mathbb{F}_{11}\times\mathbb{F}_7, (x,s)\mathbin{*}(y,t) = (6x+6y, a_{y-x}s+b_{y-x}t))$
has order $77$ and:

- **(a)**  it satisfies $E677$ (zero violations over all $5929$ pairs) and every
$L_Y$ is a bijection;

- **(b)**  it satisfies $E255$ at every element, although it is *not*
idempotent: $X\mathbin{*} X = (x,5s)$, so exactly the $11$ elements $(x,0)$ are
idempotent and the other $66$ are not;

- **(c)**  it is *not* right-cancellative — indeed all $77$ right
translations are non-injective; each row of $N$ has $30$ zeros, $42$ ones and $5$
entries equal to $7$, so every column carries exactly $47$ distinct values and the
global distribution of $N$ is $\{0\!:\!2310, 1\!:\!3234, 7\!:\!385\}$;

- **(d)**  $(\mathrm{S\text{-}off})$ nevertheless *holds* in it (zero
violating pairs);

- **(e)**  $\operatorname{tr} N = \Psi_1 = 77$, so Corollary 7.14 holds with
equality on the first non-idempotent test available.

*Proof sketch.* 
$(F,G) = (4,1)$ over $\mathbb{F}_7$ satisfies the affine criterion
($1\cdot4+1\cdot4\cdot1 = 8 = 1$ and $4+16+1 = 21 = 0$), so $\diamond_0$ is a
non-idempotent affine $E677$ magma ($s\diamond_0s = 5s$); $(F,G) = (6,6)$ over
$\mathbb{F}_{11}$ likewise satisfies it, so the base is a Latin $E677$ magma. With
$A = B = 6$ and $c = 0$ the index maps of Lemma 4.4 are
$D_1 = D_2 = 9d$, $D_3 = 10d$, $D_4 = 6d$; $9$ is a square and $10,6$ are
non-squares mod $11$, so the operation pattern at the four positions is
$(U,U,V,V)$ for square $d$ and $(V,V,U,U)$ for non-square $d$, where $U = (0,1)$
and $V = (r,r^{-1})$. In both cases (E1) is automatic and (E2) reduces to
$r^3 = -1$, whose solutions in $\mathbb{F}_7$ are $r\in\{3,5,6\}$; $r = 3$ gives the
displayed $(3,5)$. At $d = 0$ all four positions carry $\diamond_0$ and the two
equations are exactly the affine $E677$ conditions for $(4,1)$
(Corollary 7.4). Non-idempotency, $E255$ and the failure of
right cancellation are then read off: repeated multiplication by the same element
stays at offset $0$, so $X\mathbin{*} X = (x,5s)$, $(X\mathbin{*} X)\mathbin{*} X = (x,0)$ and
$((X\mathbin{*} X)\mathbin{*} X)\mathbin{*} X = X$; and at any nonzero square offset the fibre output
$0\cdot s+1\cdot t = t$ is independent of $s$, so seven distinct rows collide in
every column.
 ∎

**Remark (three records, and one thing it does not do).** 
$77 < 176 < 496$: $M_{77}$ is the smallest non-right-cancellative finite $E677$
magma known to the campaign or to [14], the first that is not idempotent, and
the first non-constant non-idempotent translation-invariant coefficient
assignment. It lies outside the $\theta$-family scanned in
Proposition 4.11 — its zero-offset fibre has $a_0+b_0 = 5\ne1$
— so the range-limited minimality statement there is unaffected; but the problem
of the least non-right-cancellative order now reads “between $10$ and $77$”.
$M_{77}$ satisfies $E255$ and is *not* a counterexample to
Problem 1.1.

**Remark (machine certificate).** 
🖥️ MACHINE-VERIFIED (lean/proofenv/M77.lean)
All four properties of Theorem 7.18(a)–(c) are certified in **Lean** 4
by kernel-level `decide` — *not* `native_decide` — on the
carrier `Fin 77` with the pair $(x,s)$ encoded as $7x+s$. The file carries
bridging lemmas (`mulN_enc`, `offs_sub`) certifying that the
encoded operation is literally the displayed formula on pairs and that the
truncated-subtraction offset is the genuine difference mod $11$, so the encoding
is not load-bearing. The axiom audit reports {`propext`, `Quot.sound`} — strictly inside the permitted set, with no
`Classical.choice`.

The second order-$77$ model answers a question the framework had never been
pushed on: does the compatibility system force translation invariance?

**Lemma 7.19 (diagonal decoupling).** 
✅ PROVED (R6-E §2) 🖥️ MACHINE-VERIFIED (problems/etp677/R6E_scripts/r6e_verify.py)
Work with pair-indexed fibre operations $s\diamond_{x,y}t = a_{x,y}s+b_{x,y}t$, so
that (4.1) becomes, for every ordered base pair,

$$

  \text{(E1-pair)}  b_1(a_2+b_2a_4b_3) = 1, \qquad
  \text{(E2-pair)}  a_1+b_1b_2(a_4a_3+b_4) = 0,

$$

with subscripts $P_1 = (y,z_2)$, $P_2 = (x,z_4)$, $P_3 = (y,x)$, $P_4 = (z_3,y)$
where $z_3 = y\diamond x$, $z_4 = z_3\diamond y$, $z_2 = x\diamond z_4$. Over the
base $x\diamond y = 6x+6y$ on $\mathbb{F}_{11}$ the four subscripts have offsets
$9d,9d,10d,6d$ with $d = y-x$; all four multipliers are nonzero. Hence for
$x\ne y$ all four $P_i$ are off-diagonal pairs, while for $x = y$ idempotency of
the base gives $P_1 = P_2 = P_3 = P_4 = (x,x)$. *The eleven diagonal fibre
operations may therefore be chosen independently of each other and of the
off-diagonal ones*, subject only to each being an affine $E677$ magma.

The collapse at $x = y$ is used here purely in the construction direction of
Remark (logical status of the collapse; §7.1)(ii): two explicit affine operations are exhibited and their
$E677$ equations are checked, so that the corresponding instances of (4.1) are
discharged. Nothing about the product magma is assumed in order to obtain them.

**Theorem 7.20 (the non-translation-invariant order-$77$ model $M_{77}^{\mathrm{NT}}$).** 
✅ PROVED (R6-E §§3–5) 🖥️ MACHINE-VERIFIED (problems/etp677/R6E_scripts/r6e_verify.py;
independently rebuilt from the written specification in
R6D_scripts/r6d_m77nt.py)
Keep the base $6x+6y$ on $\mathbb{F}_{11}$ and the fibre $\mathbb{F}_7$, and set

$$

  (a_{x,y},b_{x,y}) =
  \begin{cases}
    (4,3) & x = y = 0,\\
    (4,1) & x = y \ne 0,\\
    (0,1) & x\ne y, y-x \text{ a nonzero square},\\
    (3,5) & x\ne y, y-x \text{ a non-square}.
  \end{cases}

$$

Then the resulting order-$77$ magma satisfies $E677$ (zero violations over all
$5929$ pairs), all $77$ left translations are permutations, it satisfies $E255$,
has $11$ idempotents and $77$ non-injective columns — and it is *not*
translation-invariant: the pairs $(0,0)$ and $(1,1)$ have the same offset $0$ but
different coefficients. It is not a coordinate-gauge artefact either: rescaling a
translation-invariant assignment by nonzero fibre scalars $\mu_x$ sends
$(a_{x,y},b_{x,y})$ to $(a_{y-x}\mu_x/\mu_{x\diamond y}, b_{y-x}\mu_y/\mu_{x\diamond y})$,
and on an idempotent base $x = y$ cancels the scale, leaving every diagonal
coefficient unchanged.

*Proof sketch.* 
$(4,3)$ over $\mathbb{F}_7$ satisfies the affine $E677$ equations
($4\cdot3\cdot(1+9) = 120 = 1$ and $4+9\cdot16+27 = 175 = 0$), as does $(4,1)$; by
Lemma 7.19 the eleven diagonal instances ask for nothing else. The
off-diagonal instances are those of Theorem 7.18 verbatim. All $121$
pair-indexed instances therefore hold, and the blueprint extension theorem gives
$E677$.
 ∎

### 7.4 The right-unit map $e(x) = x\backslash x$: a conjecture refuted twice

Recall from §2 that every $x$ has a unique right unit
$e(x) = \Lambda_x(x) = x\backslash x$. (This $e$ takes an *element*; the
isoperimetric $e(O)$ of Theorem 2.23 takes a *set*. The two are
unrelated.) Round 6 began by observing that $e$ is a term operation and that it
was an automorphism in every model then available.

**Lemma 7.21.** 
✅ PROVED (R6-A §8.1, R6-B §15, R6-D §1) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_e.py, R6D_scripts/r6d_check1.py)
$e(w) = w\backslash w = w\mathbin{*}((w\mathbin{*} w)\mathbin{*} w)$, so $e$ is a term of the language
$\{\mathbin{*}\}$ alone. Consequently “$e$ is an endomorphism” is the pure
$\{\mathbin{*}\}$-identity $(x\mathbin{*} y)\mathbin{*}\bigl((x\backslash x)\mathbin{*}(y\backslash y)\bigr) = x\mathbin{*} y$,
equivalently: *the graph of $e$ is a subalgebra of $M\times M$*. Moreover
$\operatorname{Fix}(e) = \{x : x\mathbin{*} x = x\}$ and $\sum_p|\operatorname{Fix}(R_p)| = n$
(Proposition 2.11), so

$$

  e \text{ injective} \iff e \text{ surjective} \iff e \text{ bijective}
  \iff \text{every } R_p \text{ has exactly one fixed point.}

$$

**Conjecture (R6-B-2, proposed and then refuted).** 
In every finite $E677$ magma, $e$ is an automorphism.

It held in $10$ of $10$ models when proposed, including $M_{77}$, $M_{176}$ and
$M_{496}$. Both halves are false, for different reasons, and the two refutations
are independent: in $M_{77}^{\mathrm{NT}}$ the map $e$ is bijective but not a
homomorphism, while in the order-$9$ model below $e$ is a homomorphism (it is
constant) but not injective. Both are needed.

**Proposition 7.22 (why the evidence was worthless).** 
✅ PROVED (R6-A Prop 8.4) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_e.py)
Let $M = \mathbb{F}_p\times\mathbb{F}_q$ be any translation-invariant blueprint extension with base
$x\diamond y = Ax+By+c$, $A+B = 1$, and homogeneous linear fibres
$s\diamond_dt = a_ds+b_dt$, $b_d\ne0$. Put $d_0 := -c/B$ and
$\lambda := (1-a_{d_0})/b_{d_0}$. Then

$$

  e\bigl((x,s)\bigr) \;=\; \bigl(x - c/B, \lambda s\bigr),

$$

and $e$ is an endomorphism — an automorphism iff $\lambda\ne0$ — for every $c$
and every admissible fibre family.

*Proof.* 
Base: $Ax+Bw+c = x \iff w = x-c/B$, so the offset from $x$ to its base right unit
is the constant $d_0$, independent of $x$. Fibre:
$a_{d_0}s+b_{d_0}\sigma = s\iff\sigma = \lambda s$. Endomorphism: $e(X)$ and
$e(Y)$ have base offset $(y-c/B)-(x-c/B) = y-x$, the same offset as $X,Y$, so
$e(X)\mathbin{*} e(Y) = (x\diamond y - c/B, \lambda(a_ds+b_dt)) = e(X\mathbin{*} Y)$, using
$A+B = 1$.
 ∎

So the entire translation-invariant family — which is every model the campaign
owned — satisfies the conjecture for a two-line reason with no $E677$ content.
On $M_{77}$ the prediction is $e((x,s)) = (x,4s)$, exact on all $77$ elements, and
$M_{77}$ is neither medial nor left-distributive, so the reason is not mediality
but fibre-constancy.

**Proposition 7.23 (not an equational consequence).** 
✅ PROVED (R6-A §8.2) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_e.py)
In the free $677$ magma of [2, §13.2] — where $E677$ holds with
zero violations and $w\mathbin{*} e(w) = w$ holds with zero violations, so $e(w)$ really
is a right unit — the identity $e(x\mathbin{*} y) = e(x)\mathbin{*} e(y)$ fails at *all*
$4356$ of $4356$ instances of terms of size $\le3$, the smallest being $x = y = a$.
Hence no derivation of the conjecture from the $E677$ identity in the language
$\{\mathbin{*}\}$ exists. As in Proposition 4.12, the caveat is that this
free magma is not a left quasigroup ($L_a$ is not injective there, with an
explicit witness), so this closes the equational route only.

**Theorem 7.24 (first refutation: $e$ need not be a homomorphism).** 
✅ PROVED (R6-E §5) 🖥️ MACHINE-VERIFIED (problems/etp677/R6E_scripts/r6e_verify.py;
independently R6D_scripts/r6d_m77nt.py)
In $M_{77}^{\mathrm{NT}}$ (Theorem 7.20) the right-unit map is
$e((x,s)) = (x,\lambda_xs)$ with $\lambda_0 = 6$ and $\lambda_x = 4$ for $x\ne0$;
both scalars are nonzero, so $e$ is a bijection. It is not a homomorphism: it
fails at $1050$ of the $5929$ ordered pairs. An explicit witness is

$$

  X = (1,0),\quad Y = (0,1): \qquad e(X\mathbin{*} Y) = (6,6) \ne (6,2) = e(X)\mathbin{*} e(Y).

$$

*Proof.* 
The base is idempotent, so its right-unit map is the identity, and solving
$4s+3t = s$ at base point $0$ gives $t = 6s$, while $4s+t = s$ elsewhere gives
$t = 4s$. By the criterion of Proposition 7.22 extended to
pair-indexed coefficients, $e$ is a homomorphism exactly when
$\lambda_{x\diamond y}a_{x,y} = a_{x,y}\lambda_x$ and
$\lambda_{x\diamond y}b_{x,y} = b_{x,y}\lambda_y$ for all $x,y$. At $x = 1$,
$y = 0$ one has $x\diamond y = 6$, $(a_{1,0},b_{1,0}) = (3,5)$, and the second
equation would require $4\cdot5 = 5\cdot6$ in $\mathbb{F}_7$, i.e. $6 = 2$. The
coefficient obstruction occurs at $25$ of the $121$ base pairs, and at each the
homomorphism defect is a nonzero linear form in the two fibre variables, hence
fails on $42$ of their $49$ values: $25\times42 = 1050$.
 ∎

**Theorem 7.25 (second refutation: $e$ need not even be injective).** 
✅ PROVED (R6-D §3) 🖥️ MACHINE-VERIFIED (problems/etp677/R6D_scripts/r6d_min9.py, r6d_m9.py)
Let $M_9 := (\mathbb{F}_3^2, x\mathbin{*} y = x+Gy)$ with
$G = \left(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\right)$ over $\mathbb{F}_3$, which
satisfies $G+G^3 = I$. Then $M_9$ is an $E677$ magma of order $9$ (zero violations
over all $81$ pairs), it is a quasigroup, it satisfies $E255$, and it has exactly
one idempotent. Its coefficient $F$ is $I$, so $0$ is a *right identity* and
$e\equiv0$ is constant: $e$ is not injective. Moreover $9$ is the least order at
which this happens.

*Proof.* 
$F = I$ is forced by $F = (G+G^3)^{-1} = I$, and $x\mathbin{*}0 = x$ makes $0$ a right
identity, so $x\backslash x = 0$ for every $x$. Minimality: orders $2,3,4,6,8$
carry no $E677$ magma at all and at orders $5,7$ the map $e$ is bijective
(Theorem 6.1 and Table 1), so no smaller example exists.
Independently, a **Mace4** search over “left quasigroup $+$ $\mathrm{KEY}$
$+$ $\exists a\ne b,c: a\mathbin{*} c = a\wedge b\mathbin{*} c = b$” terminated with
`exit(exhausted)` and zero models at $n = 5,7$ and returned exactly this
model at $n = 9$.
 ∎

**Remark (the counterexample was in Theorem 6.1 all along).** 
🖥️ MACHINE-VERIFIED (problems/etp677/R6_zoo.py)
$M_9$ is not a new magma. By Theorem 6.1 there is exactly one $E677$
magma of order $9$ up to isomorphism, the affine model over
$\mathbb{F}_9 = \mathbb{F}_3[t]/(t^2+1)$ with $(F,G) = (1,t+2)$, and an explicit isomorphism
$M_9\to(\mathbb{F}_9, x+(t+2)y)$ is exhibited by `R6_zoo.py` (both have $F = 1$,
so both have $0$ as a right identity). **Mace4** rediscovered it because the
campaign's working benchmark set — cyclic affine models, $\mathbb{F}_{16}$, and
translation-invariant extensions — contained no odd-order *non-cyclic*
model, $\mathbb{Z}/9$ carrying no affine $E677$ structure at all. *The refutation of
half of a Round-6 conjecture was sitting inside this paper's own classification
table, unused, because the object used for testing conjectures was not the
classification but the benchmark set.* See §7.6.

**Corollary 7.26 (the affine criterion for bijectivity).** 
✅ PROVED (R6-D §6)
For an affine model $x\mathbin{*} y = Fx+Gy+c$ one has $e(x) = G^{-1}((1-F)x-c)$, so

$$

  e \text{ is bijective} \iff 1-F \text{ is invertible} \iff G^3+G-1 \text{ is
  invertible},

$$

using $F = (G+G^3)^{-1}$. $M_9$ realizes the extreme case $G^3+G-1 = 0$.

**Remark (what survives, and the new target).** 
✅ PROVED (R6-D §5) 🧮 COMPUTATIONAL ($13$ models; root-verified)
$\operatorname{Fix}(e) = \operatorname{Idem}(M)$ is a definitional identity and is untouched. What dies is the
route “$e\in\operatorname{Aut}$ $\Rightarrow$ $\operatorname{Idem}(M) = \operatorname{Fix}(e)$ is a subalgebra
$\Rightarrow$ $\langle e\rangle$-orbit lengths are divisible by $31$
$\Rightarrow$ $31\mid n$” (Conjecture R6-B-3 of §7.5): the orbit
partition needs $e$ to be a permutation, and in $M_9$ it is constant. The
statement “$\operatorname{Idem}(M)$ is a subalgebra” is *not* refuted — it holds in all
$13$ models, including $M_{77}^{\mathrm{NT}}$ and $M_9$ — and it now has a clean
equivalent reduction: since $a^2 = a$ and $b^2 = b$ for idempotents,

$$

  \operatorname{Idem}(M) \text{ is closed} \iff (a\mathbin{*} b)\mathbin{*}(a\mathbin{*} b) = a\mathbin{*} b
  \text{ for all idempotent } a,b,

$$

i.e. the square identity $(a\mathbin{*} b)^2 = a^2\mathbin{*} b^2$ restricted to idempotent
pairs. In $M_{77}^{\mathrm{NT}}$ that identity has $1050$ violations globally but
none on idempotent pairs, which is exactly why $\operatorname{Idem}$ is still closed there. This
strictly weaker statement is the recommended successor target.

### 7.5 Idempotent-free magmas and the fibre spectrum

Proposition 5.10 left the extension programme with exactly one
habitat: the base $x\diamond y = 5x-4y+c$ on $\mathbb{F}_{31}$ with $c\ne0$, the only
translation-invariant $E677$ base with no idempotent. Round 6 asked what the fibre
sizes over that base can be. Write

$$

  S := \{\,|M| : M \text{ a finite } E677 \text{ magma}\,\}, \qquad
  S_0 := \{\,|M| \in S : M \text{ has no idempotent}\,\},

$$

and $\mathrm{FiberSpec}(c) :=$ the set of fibre sizes $m$ for which the base
$5x-4y+c$ admits a translation-invariant fibre family. The *fibre spectrum
conjecture* is $\mathrm{FiberSpec}(1) = S$.

**Theorem 7.27 (uniqueness of the exceptional base).** 
✅ PROVED (R6-B Thm 3) 🖥️ MACHINE-VERIFIED (problems/etp677/R6B_tools.py)
Over a commutative ring, $x\diamond y = ax+by+c$ satisfies $E677$ iff
$ab(1+b^2) = 1$, $a+a^2b^2+b^3 = 0$ and $c(ab^2+b^2+b+1) = 0$; the first two are
equivalent to $a = (b+b^3)^{-1}$ and $P(b) = \Phi_{10}(b)\,Q(b) = 0$;
translation invariance $a+b = 1$ is equivalent to $\Phi_{10}(b) = 0$; and, when
$c$ is a non-zero-divisor, the third is equivalent to $Q(b) = 0$. Hence a
*non-idempotent translation-invariant affine base* requires
$\Phi_{10}(b) = Q(b) = 0$, which forces $248 = 8\cdot31 = 0$. Over a field
characteristic $2$ is excluded, so the characteristic is $31$, and then
$b = -5/9 = -4$, $a = 5$, with $c$ any nonzero constant (normalizable to $1$).

So the exceptional base is not *a* special base: it is the unique
non-idempotent translation-invariant affine $E677$ base over any field. The whole
extension-based counterexample programme rests on that one arithmetic fact.

**Theorem 7.28 (fibres over an idempotent are submagmas).** 
✅ PROVED (R6-B Thm 2)
Let $B$ satisfy $E677$, let $\pi : B\to C$ be a magma homomorphism and let $e\in C$
be idempotent. Then $\pi^{-1}(e)$ is closed in $B$, hence is itself an $E677$
magma when nonempty. Consequently $\mathrm{FiberSpec}(0) = S$: over any $c = 0$
translation-invariant base the fibre spectrum *is* the order spectrum, and
the fibre spectrum conjecture is a theorem there.

This is Theorem 7.3 again, and it explains structurally why
$c\ne0$ is the only escape: $E_c$ has no idempotent because $x\diamond x = x+c$.
In the other direction, sufficiency is free and holds over every base.

**Theorem 7.29 (sufficiency).** 
✅ PROVED (R6-B Thm 1) 🖥️ MACHINE-VERIFIED (problems/etp677/R6B_tools.py)
If $(M,\circ)$ is any finite $E677$ magma then the constant family
$\diamond_\delta\equiv\circ$ satisfies all $31$ instances of (4.1) over
any base $E_c$, so $S\subseteq\mathrm{FiberSpec}(c)$ for every $c$. Verified for
$m = 5$ (order $155$) and $m = 16$ (order $496$), with a negative control (the
$\omega$-quandle, which is not $E677$) producing $7440$ violations.

**Remark (constant is not the same as rigid).** 
✅ PROVED (R6-B Prop 1.1) 🧮 COMPUTATIONAL (on the order-$496$ magma)
“All translation-invariant solutions over the exceptional base are constant” is
*false*. If $\gamma\in\operatorname{Aut}(M,\circ)$ with $\gamma^{31} = \mathrm{id}$, then
$\diamond_\delta(s,t) := \gamma^{4\delta-1}(s)\circ\gamma^{5\delta-1}(t)$ is again
a solution (it is the constant solution transported by
$\psi(x,s) = (x,\gamma^x(s))$). Taking $(M,\circ)$ to be the order-$496$ magma and
$\gamma$ a base translation gives a solution whose $\diamond_0$ and $\diamond_1$
differ at all $246016$ points. The correct rigidity statement can only be
“every solution is gauge-equivalent to a constant one”.

**Theorem 7.30 (structural equivalence and the free $\mathbb{Z}_{31}$-action).** 
✅ PROVED (R6-B Thm 4 and Cors. 4.1–4.5)
$m\in\mathrm{FiberSpec}(c)$ if and only if there is a finite $E677$ magma $B$, a
surjective homomorphism $\pi : B\to E_c$ with all fibres of size $m$, and
$\theta\in\operatorname{Aut}(B)$ with $\pi(\theta X) = \pi(X)+1$; such a $\theta$ has order $31$
and acts freely. Consequently, for $c\ne0$:

- **(a)**  $B$ has no idempotent, so $S\subseteq\mathrm{FiberSpec}(1)\subseteq\{m : 31m\in S_0\}$;

- **(b)**  either of “$31n\in S\Rightarrow n\in S$” and “$S_0\subseteq31\cdot S$”
implies the necessity half of the fibre spectrum conjecture;

- **(c)**  $8\in\mathrm{FiberSpec}(1)$ iff there is an $E677$ magma of order
$248$ with no idempotent carrying a free $\mathbb{Z}_{31}$ of automorphisms;

- **(d)**  every automorphism-invariant subset of $B$ has size divisible by $31$;
in particular the set of elements at which $E255$ fails has size $\equiv0\pmod{31}$,
so a translation-invariant counterexample cannot break at a single point — it
must break on at least one full $\mathbb{Z}_{31}$-orbit;

- **(e)**  (single-orbit reduction) if a solution violates $E255$ at $(0,\sigma_0)$
then its restriction to the closure of $\{\sigma_0\}$ under the $31$ operations
$\diamond_\delta$ is again a solution violating $E255$ at the same point. So one
may assume without loss that the fibre is generated by the violating point.

**Theorem 7.31 (the exceptional base blocks every local mechanism).** 
✅ PROVED (R6-B Thm 5) 🖥️ MACHINE-VERIFIED (problems/etp677/R6B_tools.py)
For $E_1 = (\mathbb{F}_{31},\,5x-4y+1)$:

- **(a)**  $E_1$ has no proper subalgebra and no nontrivial congruence. (Any
nonempty subalgebra is closed under $x\mapsto x\diamond x = x+1$, hence is
everything; for congruences, $x\mathrel\theta y$ forces $5x+k\mathrel\theta5y+k$
for all $k$, and $5^3\equiv1\pmod{31}$ gives translation invariance of $\theta$,
so the classes are cosets of a subgroup $H$ with $5H = H$, and $\mathbb{Z}_{31}$ has no
proper subgroup.) So constructions by subalgebra, quotient or preimage produce
nothing.

- **(b)**  For $c\ne0$ no instance of (4.1) degenerates to $E677$: the
most collapsed instance, $d = -c/A$, still involves three distinct operations
(for $c=1$: $d = 6$ with subscripts $(25,8,25,6)$). For $c = 0$ the unique
coincident instance is $d = 0$, where all four subscripts agree.

- **(c)**  No $\theta$-twist $X*Y := \theta^a(X\diamond\theta^jY)$ carries the
$c = 1$ system onto a $c' = 0$ system, so Theorem 7.28 cannot be
imported.

- **(d)**  The affine symmetry group of the subscript system collapses from
$\mathbb{F}_{31}^\times$ (order $30$, at $c = 0$) to the trivial group (at $c\ne0$). The
blueprint's own $\{0,\mathrm{QR},\mathrm{QNR}\}$ class-function ansatz is a
$\mathbb{F}_{31}^\times$-class function and therefore has no analogue at $c\ne0$.

Together these say that the necessity half cannot be obtained by any subalgebra,
quotient, twist or symmetry argument: it needs a global theorem about $S$ or $S_0$.
Round 6 obtained that theorem for affine magmas.

**Theorem 7.32 ($S_0$ is an ideal).** 
✅ PROVED (R6-B Thm 8) 🖥️ MACHINE-VERIFIED (problems/etp677/R6B_S0.py)
$A\times B$ has an idempotent iff both $A$ and $B$ do. Hence $S_0\cdot S\subseteq S_0$:
$S_0$ is an ideal of the multiplicative monoid $S$. Since $31\in S_0$ (the
exceptional model itself), $31\cdot S\subseteq S_0$. Machine check:
$E_{31}\times\{1,\mathbb{F}_5,\mathbb{F}_7,E_{31}\}$ gives orders $31,155,217,961$, all with zero
idempotents and zero $E677$ violations.

**Theorem 7.33 (the elimination constant is exactly $31$).** 
✅ PROVED (R6-B Thm 9; Bézout identity re-verified coefficientwise)
In $\mathbb{Z}[b]$, with $\Phi_{10}(b) = b^4-b^3+b^2-b+1$ and $Q(b) = b^4+b^3+2b^2+2b+1$
the two factors of $P$,

$$

  \operatorname{Res}(\Phi_{10},Q) = 31, \qquad
  (18+16b+b^2+10b^3)\,\Phi_{10}(b) + (13-24b+19b^2-10b^3)\,Q(b) = 31 .

$$

So for any commutative ring $R$ and any $b\in R$ the ideal
$(\Phi_{10}(b),Q(b))$ contains $31$. This is sharper than the “$248 = 8\cdot31 = 0$”
of Theorem 7.27: the factor $2$ is eliminated entirely, because
$\Phi_{10}$ and $Q$ are coprime mod $2$.

**Theorem 7.34 (idempotent-free affine orders are exactly $31\cdot S$).** 
✅ PROVED (R6-B Thm 10) 🖥️ MACHINE-VERIFIED (problems/etp677/R6B_S0.py)
Let $M$ be a finite abelian group, $a,b\in\operatorname{End}(M)$ commuting with $b$ invertible,
$c\in M$, and suppose $B = (M, x\mathbin{*} y = ax+by+c)$ satisfies $E677$ and has no
idempotent. Then $31\mid|M|$ and $|M|/31\in S$. Combining with
Theorem 7.32, $S_0^{\mathrm{aff}} = 31\cdot S^{\mathrm{aff}}$.

*Proof sketch.* 
From $ab(1+b^2) = 1$, $b$ and $1+b^2$ are units and $a = (b+b^3)^{-1}$; then
$u := a+b-1 = \Phi_{10}(b)\,(b+b^3)^{-1}$, so $\operatorname{Im}(u) = \operatorname{Im}(\Phi_{10}(b))$, and
$(1+b^2)(ab^2+b^2+b+1) = Q(b)$, so the constant condition gives $Q(b)c = 0$. Now
$x\mathbin{*} x = x\iff(a+b-1)x = -c$, so *$B$ has no idempotent iff
$c\notin\operatorname{Im}(\Phi_{10}(b))$*. Evaluating the Bézout identity of
Theorem 7.33 at $b$ and applying it to $c$ gives
$31c = \Phi_{10}(b)(A(b)c)\in\operatorname{Im}(\Phi_{10}(b))$. If $31\nmid|M|$ then
multiplication by $31$ is an automorphism whose inverse is multiplication by an
integer, hence commutes with $\Phi_{10}(b)$, giving $c\in\operatorname{Im}(\Phi_{10}(b))$ —
a contradiction. So $31\mid|M|$. Finally decompose $M = \bigoplus_pM_p$ into
primary components (each is characteristic, hence $a,b$-invariant); $B$ is the
product of the $B_p$, each a quotient of $B$ and hence an $E677$ magma, so
$|M_p|\in S$; $B$ has no idempotent iff some $B_p$ has none, and that forces
$p = 31$; then $|M|/31 = 31^{k-1}\prod_{p\ne31}|M_p|$ with every factor in $S$
and $S$ closed under multiplication.
 ∎

**Corollary 7.35.** 
✅ PROVED (R6-B Cors. 10.1–10.2)
(a) If $m\in\mathrm{FiberSpec}(1)$ and the resulting order-$31m$ magma is affine,
then $m\in S$: the fibre spectrum conjecture holds for all extensions whose total
magma is affine. (b) There is no idempotent-free *affine* $E677$ magma of
order $248$, because $248/31 = 8\notin S$ (Theorem 6.1).

A scan over all $(a,b,c)$ on $22$ small rings finds idempotent-free affine models
at exactly the orders $31,155,217,961 = 31\cdot\{1,5,7,31\}$, matching
Theorem 7.34 exactly 🖥️ MACHINE-VERIFIED (problems/etp677/R6B_S0.py). The
general case is open and is the campaign's cleanest remaining sub-goal:

**Conjecture (R6-B).** 
Every idempotent-free finite $E677$ magma has order divisible by $31$; more
strongly, $S_0 = 31\cdot S$. Either this or “$31n\in S\Rightarrow n\in S$” makes
the fibre spectrum conjecture a theorem and empties the $m = 8$ search space
(Theorem 7.30(b),(c)).

**The affine fibre classes, computed.** Theorem 7 of [18] reduces a
translation-invariant affine fibre family to a system in the ring generated by the
coefficients: with $\diamond_\delta(s,t) = a_\delta s+b_\delta t+e_\delta$,
(4.1) at $d$ is equivalent to

$$

\begin{aligned}
  \text{(I)} & b_1a_2+b_1b_2a_4b_3 = 1, &\qquad
  \text{(II)} & a_1+b_1b_2a_4a_3+b_1b_2b_4 = 0,\\
  \text{(III)} & b_1b_2a_4e_3+b_1b_2e_4+b_1e_2+e_1 = 0, &&
\end{aligned}

$$

and (III) is homogeneous linear in $e$, so $e\equiv0$ is always a solution and
*existence is decided by (I)–(II) alone*. Since (I)–(II) live in the ring
generated by the $a_\delta,b_\delta$, one solves once per coefficient ring. A
complete depth-first solver
🧮 COMPUTATIONAL (R6-B §8; complete over the stated rings, no SAT)
gives: no solution for $m\in\{2,3,4,6\}$ over every possible coefficient ring;
exactly one solution for $m = 5$, the constant family $(a,b)\equiv(2,4)$; and for
$m = 8$, no solution over $\mathbb{Z}_8$, $\mathbb{Z}_4\times\mathbb{Z}_2$ (including the full
noncommutative $\operatorname{End}$), or any commutative coefficient ring on $\mathbb{Z}_2^3$ except
$\mathbb{F}_8$. *Honest gaps:* $R = \mathbb{F}_8$ (search space $56$, terminated by the
round's compute budget) and $M = \mathbb{Z}_2^3$ with noncommuting coefficients
($M_3(\mathbb{F}_2)$, search space $86\,016$, not attempted); and the whole computation
covers *affine* fibres only, so it says nothing about the nonlinear
five-operation gadget of §5.8.

**Theorem 7.36 (the exceptional base over small fibre fields).** 
🧮 COMPUTATIONAL (R6-B §§17–19, complete solution; $1296$ algebraic shards,
$5.66\cdot10^{10}$ nodes)
For homogeneous affine fibre families over the exceptional base
$5x-4y+1$ on $\mathbb{F}_{31}$: there is no solution for $q\in\{2,3,4,6\}$ (and for every
coefficient ring of those orders); exactly one for $q = 5$, the constant family
$(2,4)$; and exactly two for $q = 7$, the constant families $(4,1)$ and $(4,3)$.
The solution space is therefore *exactly* the set of constant families, one
for each affine $E677$ structure on the fibre — one at $q=5$, two at $q=7$.
In particular there is no family with $a_{8} = 0$, where $8 = -c/B$.

The last clause matters for §7.2. [17], §7.5–7.6 designed an
explicit potential counterexample to $\Psi_1 = \operatorname{tr} N$: over a base *without*
idempotents, $E255$ is protected at the fibre pair $(\delta(x),x)$ while the
$x$-term of $\Psi_1$ is decided at the pair $(x,e(x))$, and these two coincide
*only at idempotent base points*; on $E_c$ the corresponding offsets are
$c/A$ and $-c/B$, always distinct, and $-c/B$ avoids all three conflict indices
of Lemma 4.7. Any fibre family with $a_{-c/B} = 0$ would give a
magma satisfying $E255$ with $\Psi_1 = nq > n = \operatorname{tr} N$, refuting both
$\Psi_1 = \operatorname{tr} N$ and $(\mathrm{ORB})$. Theorem 7.36 shows that no such
*affine* family exists for $q\le7$; a constant family always has
$a = (b+b^3)^{-1}$, a unit, so the design necessarily requires a non-constant —
hence, in this range, a non-affine — family. The design and the range limitation
are both recorded rather than resolved.

### 7.6 Methodology: the evolution of the benchmark set

Four times in this campaign a statement was believed on the strength of holding in
every available model, and four times the belief was an artefact of what those
models had in common. The pattern is worth recording as a result.

1.  **Phase 1 — cyclic affine models.** Orders $\le9$ plus a scan of
$ax+by\bmod n$: every model odd, every model a quasigroup. Outcome: the
*parity conjecture* (Section 3.2), refuted by the $\mathbb{F}_{16}$
quandle, which is not cyclic; and the pursuit of $(\mathrm{Q})$ for two rounds
(§5.2), refuted by the order-$496$ magma.

1.  **Phase 2 — adding $M_{176}$ and $M_{496}$.** These are
non-right-cancellative, and they immediately killed the term
$b = (x\mathbin{*} x)\backslash a$, which is a perfect “up-step” in *every* Latin
model tested (orders $5,7,7,11,11,11,11,13,16,19,19$) and fails in $21120$ of
$30976$ instances in $M_{176}$ 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_verify.py).
Had they not been in the set, that term would have looked like a proof of
Problem 1.1. The same filter caught, on the day it was installed, a
claimed complete proof of Problem 1.1 produced by one of the
campaign's own third-party reasoning models: its key identity $N^2 = nN$ holds
automatically in every Latin model and fails on $5390$ of $5929$ pairs in
$M_{77}$ and on $14080$ of $30976$ in $M_{176}$
🖥️ MACHINE-VERIFIED (problems/etp677/R6_zoo.py) — i.e. the argument had silently
assumed $(\mathrm{Q})$, which is false.

1.  **Phase 3 — adding $M_{77}$.** Both $M_{176}$ and $M_{496}$ are
*idempotent*, so $\delta = e = \mathrm{id}$ and $x_k = x$ for all $k$ in
them: the entire $\Psi$/orbit programme of §7.2 is
*vacuously* true there, and direct products do not help because all these
curve masses are multiplicative
✅ PROVED (R6-A §4.4) 🖥️ MACHINE-VERIFIED (problems/etp677/R6A_scripts/r6a_blocks.py).
$M_{77}$ was built (§7.3) precisely to be non-idempotent and
non-right-cancellative. It still does not discriminate: by
Theorem 7.3 the $L_x$-orbit of $x$ stays inside its congruence
class, and that class is a Latin block. Within the $c = 0$ translation-invariant
family this is unavoidable, and it is the same self-similarity as
§7.1.

1.  **Phase 4 — adding $M_{77}^{\mathrm{NT}}$ and $M_9$.** Every model up
to that point was translation-invariant, and Proposition 7.22 shows
that in *every* such model the right-unit map is automatically an
endomorphism for a two-line linear reason. The conjecture “$e\in\operatorname{Aut}$” was
therefore supported by $10$ models with zero discriminating power, and fell to the
first non-translation-invariant model (Theorem 7.24) and to the
order-$9$ model that the benchmark set had never included
(Theorem 7.25).

Two rules were adopted as a result, and are recommended to anyone continuing this
work.

-  **Filter set.** Every term or identity search must be run against
$\{M_9,\,M_{77},\,M_{77}^{\mathrm{NT}},\,M_{176},\,M_{496}\}$ at minimum: a
non-cyclic odd-order model with a right identity, a non-idempotent
non-right-cancellative model, a non-translation-invariant one, and two
idempotent non-right-cancellative ones. One measured consequence: of $595$
unary terms that are endomorphisms in all $11$ Phase-2 models, only $32$ survive
the addition of $M_{77}^{\mathrm{NT}}$, and those $32$ are all equal to the
identity map 🖥️ MACHINE-VERIFIED (problems/etp677/R6D_scripts/r6d_survive.py).

-  **The $E255$ blind spot.** *Every* finite $E677$ magma known to
anyone satisfies $E255$. Therefore “holds in all known models” carries
**zero** information about whether a statement is a consequence of $E677$ or
only of $E677+E255$; a term-mining run on the model set will happily rediscover
$E255$ itself as a “law”. No identity obtained by model filtering may be used on
the main line before it has been derived from $E677$ independently. This is the
exact sense in which the campaign's numerical evidence for $\Psi_1 = \operatorname{tr} N$
(§7.2) must be discounted.

**Remark (a retracted conjecture, recorded).** 
🧮 COMPUTATIONAL (R6-D §4.3)
The $595\to32$ collapse above was itself preceded by a Round-6 conjecture — that
*every* unary term is an endomorphism — proposed on the Phase-2 set and
withdrawn within the round. It is recorded here for the same reason as the parity
conjecture and $(\mathrm{Q})$: the failure mode is the interesting datum.

**Remark (what automated theorem provers did and did not do).** 
🧮 COMPUTATIONAL (R6-D §4.2, Prover9/Mace4 and E 3.1, each run under $300$\,s and $3$\,GB)
Bounded runs proved the division formula, $\mathrm{KEY}\Rightarrow E677$,
$e(y)\mathbin{*}(y\mathbin{*} y) = (y\mathbin{*} y)\mathbin{*} y$ and $\delta(x) = x\backslash e(x)$ in seconds
(five calibration targets, all discharged). The same configuration failed to prove
“$e$ is an endomorphism” and the square identity $(x\mathbin{*} y)^2 = x^2\mathbin{*} y^2$ from
$E677$, with and without $E255$. *Those failures are not evidence of
underivability* — see the reading of Proposition 5.1 — but the first
of them is now known to be a failure for the right reason
(Theorem 7.24).

### 7.7 The model zoo

Table 1 lists every finite $E677$ magma the campaign can construct,
with the properties that decide what each one can test. All columns are recomputed
from the models themselves.

**Table 1 (the model zoo).**

| model | $n$ | $\lvert\operatorname{Idem}\rvert$ | $(\mathrm{Q})$ | TI | affine | $e$ bij. | what it is good for |
|---|---|---|---|---|---|---|---|
| $\mathbb{Z}_5$, $2x-y$ | 5 | 5 | yes | — | yes | yes | the unique order-5 model; Takasaki quandle |
| $\mathbb{Z}_7$, $4x+y$ | 7 | 1 | yes | — | yes | yes | first non-idempotent model; has a left identity |
| $\mathbb{Z}_7$, $4x+3y$ | 7 | 1 | yes | — | yes | yes | $Q$-branch; squaring map constant |
| $\mathbb{F}_9$, $x+(t+2)y$ | 9 | 1 | yes | — | yes | **no** | $=M_9$; unique order-9 model; *0 is a right identity, $e\equiv0$*; kills "$e$ injective" |
| $\mathbb{Z}_{11}$, $4x+8y$ | 11 | 11 | yes | — | yes | yes | one of four order-11 classes |
| $\mathbb{Z}_{13}$, $9x+11y$ | 13 | 1 | yes | — | yes | yes | unique order-13 affine class |
| $\mathbb{F}_{16}$, $(1+z)x+zy$ | 16 | 16 | yes | — | yes | yes | smallest even order; killed the parity conjecture |
| $E_{31}$, $5x-4y+1$ | 31 | **0** | yes | — | yes | yes | *the* exceptional base: the only idempotent-free translation-invariant affine base (Theorem 7.27) |
| $M_{77}$ | 77 | 11 | **no** | yes | fibres | yes | smallest known non-right-cancellative; first non-idempotent such; first non-idempotent test of $\Psi_1\le\operatorname{tr} N$ |
| $M_{77}^{\mathrm{NT}}$ | 77 | 11 | **no** | **no** | fibres | yes | first non-translation-invariant extension; *$e$ not a homomorphism* ($1050/5929$) |
| $M_{176}$ | 176 | 176 | **no** | yes | fibres | yes | refutes $(\mathrm{S\text{-}off})$ and the isoperimetric threshold; kills term-level up-steps |
| $M_{496}$ | 496 | 496 | **no** | yes | fibres | yes | the blueprint example; $\lvert F_{pq}\rvert$ nearly attains the row-code bound |
| $E_{31}\times\mathbb{Z}_5$ | 155 | **0** | yes | — | yes | yes | idempotent-free, order $31\cdot5$ |
| $E_{31}\times\mathbb{Z}_7$ | 217 | **0** | yes | — | yes | yes | idempotent-free, order $31\cdot7$ |
| $E_{31}\times E_{31}$ | 961 | **0** | yes | — | yes | yes | idempotent-free, order $31^2$; $S_0$ is an ideal (Theorem 7.32) |

*"TI" applies only to blueprint extensions; "affine" means affine over an abelian group, and "fibres" means the fibre operations are affine while the magma itself is an extension, not affine. Every entry satisfies $E677$ and $E255$ with zero violations, has all rows permutations, and has $\Psi_1 = \operatorname{tr} N = n$. $\operatorname{Idem}$ is closed in every entry except $M_{77}^{\mathrm{D}}$, and the three Round-9 models have genuinely non-affine fibre operations, which is what makes them decisive (Lemma 10.4). The columns $\lvert\operatorname{Idem}\rvert$, $(\mathrm{Q})$, $e$ bijective, $e$ homomorphism, $\operatorname{Idem}$ closed, $\operatorname{tr} N$ and $\Psi_1$ are recomputed by `problems/etp677/R6_zoo.py`, which also exhibits the isomorphism $M_9\cong(\mathbb{F}_9,\,x+(t+2)y)$.*

Three features of the table are the campaign's current position in compressed
form. Every entry satisfies $E255$ — that is the blind spot of
§7.6. Every entry has $\Psi_1 = \operatorname{tr} N$ — that is the strongest
unrefuted criterion (Corollary 7.14), supported by evidence that
§7.6 says must be discounted. And exactly one structural feature
separates the idempotent-free entries from the rest: they all have order divisible
by $31$, which is Conjecture R6-B and, if proved, closes the extension programme.

## 8. Round 7: the mixed-idempotent base, the cocycle protection theorem, and the quotient theorems

Round 6 ended with one route still open. Corollary 7.8 had shown
that the $\{1,3\}$ collision cannot be upgraded in general, and
Proposition 5.10 had shown that an *idempotent* base
makes the construction circular. That leaves bases with *some* idempotent
element but not all — the “mixed” case — of which the smallest is
$\mathbb{F}_7$ with $x\diamond y = 4x+3y$. Round 7 attacked it [22]. It did not
produce a counterexample and it did not prove protection; what it produced is
(i) an exact, base-independent description of the local configuration
(§8.1), (ii) three strictly stronger no-go theorems, one of
which subsumes [2, Lemma 13.4] (§8.2), (iii) a
protection theorem for the whole separable/cocycle family
(§8.3), and (iv) two structure theorems about *minimal*
counterexamples that convert the Round-5 obstacle into a statement about
quotients (§8.4).

### 8.1 The occurrence trichotomy

Remark (logical status of the collapse; §7.1) quoted the following statement in passing; here
it is with its proof, since the rest of the section is organized around it. For
a base $E677$ magma $B$ and $a\in B$ satisfying $E255$, write $x_a$ for the
unique left unit of $a$ (Theorem 2.7) and
$\star := \diamond_{x_a,a}$ for the fibre operation attached to that pair — the
operation that decides $E255$ at level $a$.

**Theorem 8.1 (occurrence trichotomy; base-independent).** 
✅ PROVED (R7-B.0) 🧮 COMPUTATIONAL (verified on seven bases,
problems/etp677/R7A_scripts/r7b_baseindep.py; root-verified)
Let $B$ be any finite $E677$ magma satisfying $E255$ and $a\in B$.

- **(a)**  If $a$ is *idempotent* (equivalently $x_a = a$), the instance of
(4.1) at $(a,a)$ has $P_1 = P_2 = P_3 = P_4 = (a,a)$: $\star$ is forced
to be an $E677$ magma and $E255$ for $\star$ is the original problem. This is the
Round-5 circularity (Proposition 5.10,
Theorem 7.3).

- **(b)**  If $a$ is *not* idempotent, then $\star$ occurs in exactly
*three* instances of (4.1): in the instance at $(a,x_a)$ it occupies
positions $1$ and $3$ simultaneously — the $\{1,3\}$ collision — and it
occupies position $2$ of one further instance and position $4$ of one more.

*Proof.* 
$P_3 = (y,x) = (x_a,a)$ forces $(x,y) = (a,x_a)$. $P_1 = (y,\Lambda_yx) = (x_a,a)$
forces $y = x_a$ and $x = L_{x_a}(a) = x_a\diamond a = a$, the same instance; the
coincidence is exactly $L_{x_a}(a) = a$, i.e. the definition of a left unit. For
(a), $a\diamond a = a$ collapses all four subscripts.
 ∎

| base | idempotents | non-idempotent levels with the $3$-occurrence pattern |
|---|---|---|
| $\mathbb{F}_5(2x-y)$, $\mathbb{F}_{11}(6x+6y)$, $\mathbb{F}_{31}(5x-4y)$ | all | — (all collapse $4$-fold) |
| $\mathbb{F}_{31}(5x-4y+1)$ | none | $31/31$ |
| $\mathbb{F}_7(4x+3y)$, $\mathbb{F}_7(4x+y)$, $\mathbb{F}_{13}(9x+11y)$ | exactly $1$ | $6/6$, $6/6$, $12/12$ |

**Corollary 8.2 (changing the base does not help).** 
✅ PROVED (R7-B.0)
The local configuration around the $E255$-deciding operation is the same for
every base: at every non-idempotent level it is the three-instance picture with
the $\{1,3\}$ collision, and at every idempotent level it is the circular
four-fold collapse. In particular the idempotent-free $\mathbb{F}_{31}$ route of
§5.8 and the mixed $\mathbb{F}_7$ route of this section are
*locally identical*; only all-idempotent bases are genuinely different, and
those are circular.

### 8.2 The mixed-idempotent base $\mathbb{F}_7$, $x\diamond y = 4x+3y$

This base has $x\diamond x = 0$ for every $x$, hence the unique idempotent $0$;
for $a\ne0$ the left unit of $a$ is $3a\ne a$; and $4+3 = 0\ne1$, so it is
*not* translation-invariant. The pair-indexed system (4.1) has
$P_1 = (y,5x+y)$, $P_2 = (x,5x+5y)$, $P_3 = (y,x)$, $P_4 = (3x+4y,y)$; all four
are invertible $\mathbb{F}_7$-linear maps of $\mathbb{F}_7^2$, so each of the $49$ pairs occurs
exactly once in each position and the system is *square*: $49$ operations,
$49$ equations 🧮 COMPUTATIONAL (R7-A §2, r7a_struct.py). The instance at $(0,0)$ collapses
four-fold, so $|M|$ must lie in the $E677$ spectrum.

**Theorem 8.3 (occurrence theorem at this base).** 
✅ PROVED (R7-A Thm 1) 🧮 COMPUTATIONAL (problems/etp677/R7A_scripts/r7a_base.py)
For $a\ne0$ the operation $\star = \diamond_{3a,a}$ occurs in exactly the three
instances

$$

\begin{array}{llll}
  I_1 = (a,3a) & \text{positions } 1\text{ and }3, &\quad
  I_2 = (3a,0) & \text{position } 2,\\
  I_3 = (2a,a) & \text{position } 4. &&
\end{array}

$$

**Theorem 8.4 ($E255$ criterion in two operations).** 
✅ PROVED (R7-A Thm 2) 🧮 COMPUTATIONAL ($4000$ random systems, r7a_criterion.py)
For any pair-indexed extension $N = B\times M$, any $a\in\mathbb{F}_7$ and
$\sigma\in M$:

$$

  E255 \text{ holds at } (a,\sigma) \iff
  \exists s: \sigma\diamond_{a,4a}(s\diamond_{2a,a}\sigma) = s
  \iff \text{some left row of } \star \text{ fixes } \sigma .

$$

*Proof.* 
$E255$ at $Y$ in $N$ means some $X$ has $X\mathbin{*} Y = Y$
(Theorem 2.7); in the base $x\diamond y = y$ has the unique
solution $x = 3y$, so $E255$ at $(a,\sigma)$ says $s\diamond_{3a,a}\sigma = \sigma$
is solvable. Substituting into the instance $I_3$, whose $P_4$ is $(3a,a)$, and
using that $s\mapsto\sigma\diamond_{a,2a}s$ is a bijection gives the displayed
equivalence.
 ∎

The next theorem is the round's most reusable output: it strengthens
[2, Lemma 13.4] in three directions at once.

**Theorem 8.5 (row separation).** 
✅ PROVED (R7-A Thm 3)
Fix $a$ and put $\star = \diamond_{3a,a}$. If $s\mathbin{*} t = s'\mathbin{*} t$ for *all*
$t\in M$ then $s = s'$: the $|M|$ left rows of $\star$ are pairwise distinct
permutations.

*Proof.* 
Put $x = 3a$, $y = a$, so $x\diamond y = y$ and $y\diamond(y\diamond x) = y$. Row
equality says $L_{(x,s)}$ and $L_{(x,s')}$ agree on the whole fibre over $y$. The
$E677$ instance gives $(y,t) = L_{(x,s)}L_{(y,t)}L_{L_{(x,s)}(y,t)}(x,s)$, and
$L_{(x,s)}(y,t) = (y,s\star t) = (y,s'\star t) = L_{(x,s')}(y,t)$, so the same
identity for $s'$ has the same inner word. Both inner words lie in the fibre over
$y$, where $L_{(x,s)} = L_{(x,s')}$; cancelling $L_{(x,s)}$ and then twice more
gives $(x,s) = (x,s')$.
 ∎

**Corollary 8.6 (separability rigidity, strictly stronger than blueprint Lemma 13.4).** 
✅ PROVED (R7-A Cor 3a)
Let $M$ carry *any* group structure, abelian or not. If the *single*
operation $\star = \diamond_{3a,a}$ has the separable form
$s\star t = \alpha(s)\cdot\beta(t)\cdot c$ for *arbitrary maps*
$\alpha,\beta : M\to M$ and a constant $c$ — no homomorphism assumption — then
$\alpha$ is injective, hence every column map of $\star$ is a bijection, and
$E255$ holds at $(a,\sigma)$ for every $\sigma$.

Blueprint Lemma 13.4 is the special case “$M$ abelian, $\alpha,\beta$
endomorphisms, and *all $49$* operations of that shape”; the corollary
needs one operation, no abelianness and no homomorphism property. Two further
consequences are worth isolating.

**Corollary 8.7.** 
✅ PROVED (R7-A Cor 3b–3d)
(a) $E255$ fails at $(a,\sigma)$ only if $\star$ is genuinely two-variable at
$\sigma$: there are $s\ne s'$ with $s\star\sigma = s'\star\sigma$ but
$s\star t\ne s'\star t$ for some $t$. Every additive, group-affine,
Frobenius-twisted or endomorphism-coefficient fibre system is therefore dead.
(b) (fibre-$T3$) For $s\ne s'$ the set $\{t : \lambda_s(t) = \lambda_{s'}(t)\}$,
$\lambda_s := L^\star_s$, contains no two $\lambda_s$-consecutive points —
Theorem 2.17 applied inside the fibre.
(c) For each $\sigma$ at most one $s$ has $\lambda_s(\sigma) = \sigma$; hence
$E255$ holds in $N$ iff $\sum_{a}\sum_s|\operatorname{Fix}(\lambda^{(a)}_s)| = 7|M|$.

**Theorem 8.8 (three-neighbour affine rigidity).** 
✅ PROVED (R7-A Thm 4) 🧮 COMPUTATIONAL (all $8000$ coefficient triples over $\mathbb{F}_5$,
r7a_verify.py V5)
If the three operations $\diamond_{a,4a}$, $\diamond_{2a,a}$, $\diamond_{a,2a}$
are affine over an abelian group, then $\star = \diamond_{3a,a}$ is affine and, by
Theorem 8.5, its left coefficient is invertible; hence $E255$ holds
at level $a$. *It suffices that $3$ of the $49$ operations be affine, not all
$49$.*

**Remark (the $\{1,3\}$ collision is *not* a protection here).** 
🧮 COMPUTATIONAL (R7-A §§6–7, r7a_local.py, r7a_local3.py, r7a_global.py)
This is the essential difference from Round 5. At an idempotent level the
collapse is four-fold and forces the block to be an $E677$ magma
(Theorem 8.1(a)) — genuinely circular. Here only positions $1$
and $3$ collide, and the entire content of that collision is (i) a determination
of $\diamond_{a,3a}$ from $\star$ and $\diamond_{a,6a}$, and (ii) the fibre
analogue of Theorem 2.17 (Corollary 8.7(b)) — verified to
be exactly the same condition, $0$ mismatches in $4000$ trials. Defective
operations can satisfy it: over $|M| = 5$ there is an explicit
*ten-operation* assignment solving $I_1,I_2,I_3$ simultaneously, with all ten
operations left-invertible and $\star$ missing two values, so that $E255$ would
fail at two points; and all $20$ single-transposition defective perturbations of
the direct-product star extend to solutions of $\{I_1,I_2,I_3\}$. *There is
no local protection at this base; any protection theorem must be global.*

**Remark (the global wall).** 
🧮 COMPUTATIONAL (R7-A §8, R7-B §B.6; time-boxed randomised search, no SAT)
The $49$-operation system is square, with propagation rules determining the
operation at $P_4$ (always) or at $P_1$ (when the derived map is bijective) from
the other three; the minimal propagation seed is $19$ operations ($P_4$ only) or
$16$ ($P_4$ and $P_1$), so blind enumeration is out of reach. An annealer seeded
at the direct product with a forced defect reaches $7$ violated cells out of
$1225$ at $|M|=5$, $6$ out of $2401$ at $|M|=7$, and $7$ out of $3969$ resp. $12544$ at $|M| = 9,16$; the control (same annealer, no defect required) returns
to $0$ immediately. *In every best state the residual violations are exactly
the three star-instances* $I_1,I_2,I_3$: the other $46$ instances are perfectly
satisfiable around a defective star. §8.3 explains why.

### 8.3 The cocycle protection theorem

Corollary 8.6 kills every $\star$ that is separable over a
*group*. The natural escape is to let the fibre be a magma: take $(M,\circ)$
to be itself a finite $E677$ magma — for instance one of the
non-right-cancellative models of §7.7, where right translations need
not be surjective and a defect looks available — and put

$$

  s\diamond_{x,y}t \;:=\; \theta_{x,y}(s)\circ\psi_{x,y}(t),
  \qquad \theta,\psi\in\operatorname{Aut}(M,\circ).

$$

Matching (4.1) term by term against $E677$ for $(M,\circ)$ gives the
*sufficient* cocycle conditions

$$

  \text{(R1)} \psi_i\theta_j = 1,\quad
  \text{(R2)} \psi_j\theta_l\psi_k = \theta_j,\quad
  \text{(R3)} \psi_l = \theta_l\theta_k,\quad
  \text{(R4)} \psi_i\psi_j\theta_l\theta_k = \theta_i,

$$

with $i,j,k,l$ the four positions. The constant solution builds an order-$35$
extension with zero violations 🧮 COMPUTATIONAL (r7b_verify2.py S1).

**Theorem 8.9 (cocycle protection).** 
✅ PROVED (R7-B.1; arbitrary, possibly non-abelian, automorphism group; arbitrary base)
For a term-matched cocycle assignment, (R1)–(R4) force
$\psi_{P_3} = \theta_{P_3}\theta_{P_1}^{-1}$. At the collision instance
$P_1 = P_3 = \star$ (Theorem 8.1(b)), so $\psi_\star = \mathrm{id}$
and hence $R^\star_\sigma(s) = \theta_\star(s)\circ\sigma$, whose image is
$\operatorname{Im}(R^\circ_\sigma)$. Since $(M,\circ)$ satisfies $E255$ we have
$\sigma\in\operatorname{Im}(R^\circ_\sigma)$, so $E255$ holds in the extension at every point
of every non-idempotent level: *the construction can produce a counterexample
only if the fibre already is one*.

*Proof.* 
From (R1), $\theta_j = \psi_i^{-1}$; substituting into (R2) gives
$\psi_i\psi_j\theta_l = \psi_k^{-1}$, and putting that into (R4) gives
$\psi_k^{-1}\theta_k = \theta_i$, i.e. $\psi_{P_3} = \theta_{P_3}\theta_{P_1}^{-1}$.
 ∎

**Theorem 8.10 (thinness criterion).** 
✅ PROVED (R7-B.2)
Let $\star(s,t) = \theta(s)\circ\psi(t)$ with $\theta,\psi$ *any* bijections
of a set $M$ carrying a binary operation $\circ$, and let
$N_\circ(c,v) := \#\{r : r\circ c = v\}$. Then
$\#\{s : s\star\sigma = \sigma\} = N_\circ(\psi\sigma,\sigma)$.
Theorem 2.7 applied to the big magma forces this to be $\le1$, and
$E255$ fails at $(a,\sigma)$ exactly when it is $0$. Consequently:

- **(a)**  if the fibre is right-cancellative then no defect is possible — this
re-proves Corollary 8.6 and extends it to *every quasigroup
fibre* with $\theta,\psi$ arbitrary bijections;

- **(b)**  🧮 COMPUTATIONAL (r7b_thin.py, bipartite matching) “$N$-thin with a hole”
permutations do exist for all four non-right-cancellative models, so
Theorem 2.7 alone does not close the route;

- **(c)**  🧮 COMPUTATIONAL ($0/330$) but *none* of the $330$ affine automorphisms of
$M_{77}$ is thin with a hole, so even ignoring Theorem 8.9 the
automorphism-separable route over $M_{77}$ is closed.

**Remark (honest scope).** 
🧮 COMPUTATIONAL (R7-B §B.5)
The cocycle conditions are sufficient, not necessary. Over the quasigroup fibre
$\mathbb{F}_5(2s+4t)$ there are “accidental” solutions of (4.1) violating
(R1)–(R4) — $2048$ of $2304$ at a generic instance, and $84000$ of $90000$
separable solutions of the *collision* instance have $\psi_\star\ne\mathrm{id}$.
They are harmless there (Theorem 8.10(a) kills any defect anyway). Over
$M_{77}$, where a defect is conceivable, the accidental solutions vanish: of the
$36$ separable solutions of the collision instance, $0$ have
$\psi_\star\ne\mathrm{id}$. That last statement is 🧮 COMPUTATIONAL ($M_{77}$ only), not proved
in general. This is why every global search of §8.2 failed near
the direct product: the seed and all its neighbours lie inside this family, which
is now proved defect-free.

### 8.4 Quotient theorems: what a minimal counterexample cannot be

Round 7 closed by asking for the theorem “every blueprint extension satisfies
$E255$”. The first thing that had to be settled was the statement.

**Proposition 8.11.** 
✅ PROVED (R7-C C.1)
The one-element magma is a finite $E677$ magma satisfying $E255$, and a
pair-indexed extension of it by a fibre $M$ is a single operation on $M$ whose
instance of (4.1) is exactly $E677$. Hence “every blueprint extension
over every base satisfies $E255$” *is* Problem 1.1. The
statement must be restricted to non-trivial bases.

**Theorem 8.12 (every quotient is a blueprint extension).** 
✅ PROVED (R7-C C.2) 🧮 COMPUTATIONAL (r7c_quotient.py on five models)
In every $E677$ magma, $E677$ in the form $x = L_yL_xL_{L_yx}(y)$ exhibits $x$ in
the $\langle L\rangle$-orbit of $y$, so $\langle L_b : b\in M\rangle$ is
transitive. Consequently, if $\pi : N\to B$ is a surjective homomorphism of finite
$E677$ magmas then $L_Y$ maps $\pi^{-1}(x)$ bijectively onto
$\pi^{-1}(\pi(Y)\diamond x)$, so all fibres are equinumerous, and choosing
bijections realises $N$ as a pair-indexed extension of $B$ satisfying
(4.1). Therefore

$$

\begin{aligned}
  &\text{“every blueprint extension over a base with } 1<|B|<|N|
  \text{ satisfies } E255\text{”}\\
  &\qquad\iff \text{“a minimal counterexample is \textit{simple}”.}
\end{aligned}

$$

**Theorem 8.13 (no idempotent quotient).** 
✅ PROVED (R7-C C.3)
Let $N$ be a counterexample to Problem 1.1 of minimal order and
$\pi : N\to B$ a proper quotient. If $a\in B$ is idempotent then, by
Theorem 8.1(a), $\diamond_{a,a}$ is an $E677$ magma on the fibre
and, by Theorem 8.4 specialised to $x_a = a$, $E255$ at $(a,\sigma)$
in $N$ is literally $E255$ for $\diamond_{a,a}$ at $\sigma$; minimality forces
that to hold. Hence $E255$ holds at every point of $\pi^{-1}(a)$, and:

-  the $E255$-failure set of a minimal counterexample lies over the
*non-idempotent* part of every quotient;

-  *no quotient of a minimal counterexample is an idempotent magma*. This
kills every Alexander-quandle / translation-invariant-with-$c=0$ quotient
outright, and in particular the *base shape* of $M_{77}$, $M_{77}^{\mathrm{NT}}$
(whose only proper quotient is the fully idempotent $\mathbb{F}_{11}(6x+6y)$
🧮 COMPUTATIONAL (root-verified)) and of $M_{176}$, $M_{496}$ (base $\mathbb{F}_{31}(5x-4y)$, fully
idempotent). Those models remain legal as *fibres*.

-  The $\mathbb{F}_7(4x+3y)$ route is *not* killed: that base has exactly one
idempotent, so only the level $a = 0$ is protected — precisely the level
§8.2 had already excluded.

This upgrades the Round-5 obstacle (Proposition 5.10) from
“this construction fails” to a structure theorem about minimal counterexamples.
Combined with Corollary 8.2, the entire remaining extension-type
search space is the single uniform three-instance configuration dissected in
§8.2.

**Proposition 8.14 (unique witness and the $\Phi$-swap).** 
✅ PROVED (R7-C C.4) 🧮 COMPUTATIONAL ($200$ resp. $50$ gauge-twisted extensions, r7c_witness.py)
At a non-idempotent level, write $F := \diamond_{P_2(I_1)}$ and
$G := \diamond_{P_4(I_1)}$. Then the instance $I_1$ forces the *unique*
candidate

$$

  t(\sigma) := (L^G_\sigma)^{-1}\bigl((L^F_\sigma)^{-1}(\sigma)\bigr),
  \qquad E255 \text{ at } (a,\sigma) \iff t(\sigma)\star\sigma = \sigma .

$$

Moreover, with $\tau := t(\sigma)\star\sigma$ and
$\Phi := L^\star_{t(\sigma)}\circ L^F_\sigma\circ R^G_{t(\sigma)}$, substituting
$s = \sigma$, $t = t(\sigma)$ into $I_1$ gives $\Phi(\sigma) = \tau$ and
$\Phi(\tau) = \sigma$: *a defect at $\sigma$ forces $\Phi$ to be a
transposition on $\{\sigma,\tau\}$*.

**Remark (the residual is not an equational invariant).** 
🧮 COMPUTATIONAL (R7-C C.5, prover9 saturation)
The annealing residual of §8.2 is always exactly three
instances, which suggests a conservation law. The natural candidate is

$$

  (\mathrm{INV})\quad \text{the } E255\text{-failure set } D \text{ is }
  \langle L\rangle\text{-invariant},

$$

which would be decisive: with transitivity (Theorem 8.12) it
gives $D = \emptyset$ or $D = M$, and $D = M$ is impossible once $M$ has an
idempotent. Prover9 was run on both translates (“$E255$ at $x$ $\Rightarrow$
$E255$ at $z\mathbin{*} x$” and at $x\mathbin{*} z$) and *saturated* in both cases
(`exit (sos_empty)`), so $(\mathrm{INV})$ is not a first-order consequence
of $E677$; any such conservation law must use finiteness, exactly as
Proposition 5.1 predicts. The residual is instead explained by
Theorem 8.9.

**Remark (what Round 7 leaves).** 
The named obstacle is (NTS): a *non-separable* star, or an accidental
(non-term-matched) separable star over a non-right-cancellative fibre, whose
column defect survives the other $46$ instances — with the extra requirement of
Proposition 8.14 that $\Phi$ be a transposition. Everything
separable and term-matched is dead (Theorem 8.9); every quasigroup
fibre is dead (Theorem 8.10(a)); every group-affine fibre system is dead
(Corollary 8.6); every system with three affine neighbours is dead
(Theorem 8.8); and the $M_{77}/M_{176}/M_{496}$ *base*
shape is dead (Theorem 8.13). Round 8 appeared to close (NTS) as
well, conditionally on one verified but unproved law
(Corollary 9.13); **Round 9 refuted that law and reopened
(NTS)**, and indeed proved that non-separable fibre operations exist
(§10).

## 9. Round 8: simplicity, the transport law, and two barriers to first-order proof

Theorem 8.12 reduced one half of the programme to a single
statement: *a minimal counterexample is simple*. Round 8 [23,24,25]
attacked the contrapositive,

$$

  (\mathrm{S})\qquad \text{a \textit{simple} finite } E677 \text{ magma is
  right-cancellative,}

$$

which together with the already-proved $(\mathrm{Q})\Rightarrow E255$
(Corollary 2.8) and a closure of (NTS) would give
Problem 1.1. $(\mathrm{S})$ is **not** proved. What Round 8
delivered is a dictionary that moves the whole question into permutation group
theory, an exact reduction of $(\mathrm{S})$ to three finite statements, a
transport law that implies two of them and has a decisive structural consequence,
and — the most durable output — *two independent proofs that the
remaining statements cannot be reached by first-order reasoning at all*.

Throughout, $F_{ab} = \{t : a\mathbin{*} t = b\mathbin{*} t\} = \operatorname{Fix}(L_b^{-1}L_a)$ as in
Theorem 2.17, $\ker R_t$ is the partition of $M$ by $a\mapsto a\mathbin{*} t$,
and the *collapse relation* is

$$

  a \mathrel{\varrho} b  :\iff a\ne b \text{ and } F_{ab}\ne\emptyset .

$$

($\varrho$ here is a relation on $M$; it is unrelated to the offset reflection
$\rho$ of Corollary 4.6.) Thus $(\mathrm{Q})$ says
$\varrho = \emptyset$. Write $\varrho^{*}$ for the transitive closure,
$G := \langle L_y : y\in M\rangle\le\operatorname{Sym}(M)$, and recall that $G$ is transitive
(Theorem 8.12).

### 9.1 The congruence/block dictionary

**Theorem 9.1 (dictionary).** 
✅ PROVED (R8-A Thm 1) 🖥️ MACHINE-VERIFIED (problems/etp677/R8A_scripts/r8a_verify.py)
For an equivalence $\theta$ on a finite $E677$ magma let $K_\theta\le G$ be the
kernel of the action of $G$ on $M/\theta$. Then $\theta$ is a congruence if and
only if

- **(i)**  $\theta$ is $G$-invariant — a *block system* of $\langle L\rangle$ — and

- **(ii)**  $L_b^{-1}L_a \in K_\theta$ for every $a\mathrel\theta b$.

*Proof.* 
If $\theta$ is a congruence then every $L_c$ preserves it, hence so does
$L_c^{-1} = L_c^{\,r-1}$, giving (i); and right compatibility gives
$(a\mathbin{*} c)\mathrel\theta(b\mathbin{*} c)$, so applying the $\theta$-preserving bijection
$L_b^{-1}$ yields $L_b^{-1}L_a(c)\mathrel\theta c$ for every $c$, which is (ii).
Conversely (i) is left compatibility, and from (ii)
$L_b^{-1}(a\mathbin{*} c)\mathrel\theta c$; applying $L_b$ gives
$(a\mathbin{*} c)\mathrel\theta(b\mathbin{*} c)$.
 ∎

**Corollary 9.2.** 
✅ PROVED (R8-A C1.1–C1.4)
(a) Every congruence class is an $\langle L\rangle$-block, and since $G$ is
transitive all classes are equinumerous (a one-line sharpening of
Theorem 8.12).
(b) $\mathrm{Con}(M)$ embeds as a lattice into the block lattice of the transitive
group $G$, i.e. into the subgroup interval $[G_x,G]$.
(c) **$\langle L\rangle$ primitive $\Rightarrow$ $M$ simple.**
(d) $M$ has no congruence with $k$ classes unless an $E677$ magma of order $k$
exists; in particular none with $2$, $3$ or $4$ classes
(Theorem 6.1).

Part (c) is unconditional and is what makes the counterexample side concrete:
*to refute $(\mathrm{S})$ it suffices to exhibit a non-right-cancellative
finite $E677$ magma whose left-multiplication group is primitive* — a property
decidable from the Cayley table in $O(n^3)$. All four known non-right-cancellative
models are imprimitive with a unique minimal block system
(Table 2).

**Theorem 9.3 (column-kernel intersection).** 
✅ PROVED (R8-A Thm 2)
In every finite $E677$ magma $\bigcap_t\ker R_t = \Delta$. Consequently, if $M$ is
not a quasigroup then $t\mapsto\ker R_t$ is *not* constant, i.e. the
column-kernel relation $\theta_\kappa := \{(t,t') : \ker R_t = \ker R_{t'}\}$ is a
proper equivalence.

*Proof.* 
$a\mathrel{\ker R_t}b$ for every $t$ says $L_a = L_b$, whence $a = b$ by
Lemma 2.16(L1). If all $\ker R_t$ were equal to a common $K$ then
$K = \Delta$ and every column is injective.
 ∎

This kills unconditionally one half of the escape “every pair collapses
*and* all columns look alike”; it is what supplies *properness* in the
reduction below.

### 9.2 The master reduction, and the collapse-count identity

**Theorem 9.4 (master reduction).** 
✅ PROVED (R8-A Thm 4) [implication intact; *leg $(\mathrm{A})$
refuted* by $M_{77}^{\mathrm{D}}$, so this route is dead — it is replaced by
Theorem 10.10]
Consider

$$

  (\mathrm{A})\quad t\mathrel\varrho t' \implies \ker R_t = \ker R_{t'},
  \qquad\qquad
  (\mathrm{B})\quad \varrho^{*} \text{ is a congruence.}

$$

If $M$ is a finite $E677$ magma with $|M|>1$ satisfying $(\mathrm{A})$ and
$(\mathrm{B})$ and $M$ is not right-cancellative, then $M$ is not simple. Hence
$(\mathrm{A})+(\mathrm{B})\Rightarrow(\mathrm{S})$.

*Proof.* 
Non-Latin gives $\varrho\ne\emptyset$. $(\mathrm{A})$ says
$\varrho\subseteq\theta_\kappa$, and $\theta_\kappa$ is an equivalence, so
$\varrho^{*}\subseteq\theta_\kappa\ne\nabla$ by Theorem 9.3. By
$(\mathrm{B})$, $\varrho^{*}$ is a congruence, and it is neither $\Delta$ nor
$\nabla$.
 ∎

So $(\mathrm{A})$ supplies properness and $(\mathrm{B})$ compatibility. The second
half has a purely numerical sufficient condition. Let
$W(a,b) := |F_{ab}| = |\operatorname{Fix}(L_b^{-1}L_a)|$ be the *collapse-count matrix*.

**Proposition 9.5.** 
✅ PROVED (R8-A Prop 4.1) [implication intact; $(\mathrm{W})$
**REFUTED** by $M_{77}^{\mathrm{D}}$ ($2112/17\,787$), having previously
passed $\sim38\,000$ random triples on $10$ models with $0$ mismatches]
Consider

$$

  (\mathrm{W})\quad W(c\mathbin{*} a,\,c\mathbin{*} b) = W(a,b)
   \text{ and } W(c\backslash a,\,c\backslash b) = W(a,b)
   \text{ for all } a,b,c,

$$

i.e. $W$ is constant on the orbitals of the diagonal $\langle L\rangle$-action.
Then $(\mathrm{W})\Rightarrow(\mathrm{B})$: $\varrho$ becomes a compatible
reflexive symmetric relation (a tolerance), and the transitive closure of a
tolerance is a congruence.

**Remark (the symmetry explanation of $(\mathrm{W})$ is false).** 
🧮 COMPUTATIONAL (R8-A §4.3; refuted)
One would expect $(\mathrm{W})$ to come from a conjugacy
$L_{c\mathbin{*} b}^{-1}L_{c\mathbin{*} a}\sim L_b^{-1}L_a$ or an isotopy
$L_{c\mathbin{*} a} = A_cL_aB_c$. Both are *refuted*: the two displacements need not
even have the same cycle type ($871/3949$ random triples differ on $M_{77}$,
$1636/3952$ on $M_{77}^{\mathrm{NT}}$, $2795/3976$ on $M_{176}$; they do agree on
$M_{496}$). In $M_{77}$ the two fixed-point sets are the $\mathrm{QR}$- and the
$\mathrm{QNR}$-halves of the fibration, equal in size only because
$|\mathrm{QR}_{11}| = |\mathrm{QNR}_{11}|$. $(\mathrm{W})$ is a genuine
*counting* coincidence, not a symmetry — which already tells us that its
proof cannot be structural.

### 9.3 The transport law $(\mathrm{T})$ and the twisted diagonal

**Definition 9.6.** 

$$

  (\mathrm{T})\qquad a\mathbin{*} t = b\mathbin{*} t \implies
  (c\mathbin{*} a)\backslash(c\mathbin{*} t) = (c\mathbin{*} b)\backslash(c\mathbin{*} t)
  \qquad\text{for all } c,

$$

equivalently $L_c(F_{ab})\subseteq E_{c\mathbin{*} a,\,c\mathbin{*} b}$, where
$E_{xy} := \{v : x\backslash v = y\backslash v\} = L_x(F_{xy})$ is the value-side
collapse set. (The label $(\mathrm{T})$ is a statement, not the state map $T$ of
Theorem 5.2.)

**Theorem 9.7.** 
[**REFUTED** 2026-08-17 by $M_{77}^{\mathrm{D}}$ and
$M_{385}^{\mathrm{canon}}$ — see Theorem 10.6. The verification
record below stands as recorded and is what made the conjecture look safe]
**$(\mathrm{T})$ is false in general** (Theorem 10.6); the
statement and its consequences are kept because the implications they carry are
intact and because the shape of the error is the point (§10.4).
As recorded before Round 9:
$(\mathrm{T})$ held in every finite $E677$ magma the campaign could then
construct — exhaustively on $M_{77}$, $M_{77}^{\mathrm{NT}}$ ($1\,245\,090$
instances each) and $M_{176}$ ($14\,868\,480$), plus $200\,000$ random on
$M_{496}$ and exhaustively on $M_{77}\times\mathbb{Z}_5$: $0$ violations in $17.3$M
instances. It
is *not* a triviality of finite left quasigroups: on uniformly random left
quasigroups it fails on $75.3\%$ ($n=5$), $80.5\%$ ($n=6$), $84.2\%$ ($n=7$) and
$86.2\%$ ($n=8$) of collapse instances 🧮 COMPUTATIONAL ($200\,000$ instances each).

**Proposition 9.8.** 
✅ PROVED (R8-B Prop B.1) [implication intact; *hypothesis
$(\mathrm{T})$ refuted*, §10.4]
$(\mathrm{T})$ implies the *exact* transport
$F_{c\mathbin{*} a,\,c\mathbin{*} b} = \Lambda_{c\mathbin{*} a}L_c(F_{ab})$ and
$E_{c\mathbin{*} a,\,c\mathbin{*} b} = L_c(F_{ab})$; hence $(\mathrm{W})$, hence $(\mathrm{B})$
via Proposition 9.5. It also implies the disjointness law
$F_{c\mathbin{*} a,c\mathbin{*} b}\cap L_c(F_{ab}) = \emptyset$, which is therefore not an
independent conjecture but Theorem 2.17 transported.

*Proof.* 
$\Lambda_{c\mathbin{*} a}L_c$ is a bijection of $M$ carrying $F_{ab}$ into
$F_{c\mathbin{*} a,c\mathbin{*} b}$, so $|F_{ab}|\le|F_{c\mathbin{*} a,c\mathbin{*} b}|$; for fixed $c$ the map
$(a,b)\mapsto(c\mathbin{*} a,c\mathbin{*} b)$ is a bijection of $M^2$, so summing over all pairs
turns the inequality into an equality pointwise, and the inclusion into an
equality. Disjointness is then Theorem 2.17 ($F_{xy}\cap L_x(F_{xy}) = \emptyset$)
applied to the pair $(c\mathbin{*} a,c\mathbin{*} b)$.
 ∎

**Proposition 9.9.** 
✅ PROVED (R8-B Prop B.2, from a prover9 saturation)
$(\mathrm{T})$ is not first-order derivable from $E677$ plus the left-division
axioms: it implies the goal
“$a\mathbin{*} t = b\mathbin{*} t \to \exists s\,((c\mathbin{*} a)\mathbin{*} s = (c\mathbin{*} b)\mathbin{*} s)$”, which
saturates (`exit (sos_empty)`), and $(\mathrm{T})$ itself saturates
directly in $0.7$\,s. So $(\mathrm{T})$ is a *finite-only* law.

**Remark (the positive control that makes the saturations meaningful).** 
🧮 COMPUTATIONAL (R8-A §6, prover9)
Six further goals — transitivity of $\varrho$, its left and right
compatibility, $(\mathrm{A})$, the disjointness law, and $(\mathrm{Q})$ itself —
all saturate in the same axiomatisation. That this is genuine negative
information and not a broken encoding is established by the *positive
control*: Theorem 2.17 *is* first-order, and prover9 proves it in
$13$ steps in exactly the same setting.

For $c\in M$ define the *twisted diagonal* map

$$

  \Delta_c(a,t) \;:=\; \bigl(c\mathbin{*} a, (c\mathbin{*} a)\backslash(c\mathbin{*} t)\bigr),

$$

a bijection of $M\times M$, and let
$K := \{(a,t) : N(t,a\mathbin{*} t)\ge2\}$ be the *collapse locus*.

**Proposition 9.10 (flat form).** 
✅ PROVED (R8-B, from $(\mathrm{T})$) [implication intact;
*hypothesis refuted*] 🧮 COMPUTATIONAL (verified directly on $4$ models)
$(\mathrm{T})$ implies that $K$ is invariant under every $\Delta_c$, hence a union
of orbits of $G_\Delta := \langle\Delta_c : c\in M\rangle$ acting on $M\times M$.

**Theorem 9.11 (affine $\Delta$-dichotomy).** 
✅ PROVED (R8-B Thm B.3) 🧮 COMPUTATIONAL ($9$ parameter combinations, r8b_delta.py)
Let $x\diamond y = Ax+By+c$ over a field, with $A,B$ invertible. Then $G_\Delta$
is *transitive* on $F\times F$ unless $\diamond$ is idempotent
($A+B = 1$ *and* $c = 0$), in which case the orbits are exactly the $|F|$
difference classes $\{(x,y) : y-x = \text{const}\}$.

*Proof.* 
Solving $A(z\diamond x)+B\xi+c = z\diamond y$ gives $\Delta_z = L+T_z$ with the
$z$-free linear part $L(x,y) = (Bx, y-Ax)$ and
$T_z = (Az+c, B^{-1}A(1-A)z - B^{-1}Ac)$. Hence $G_\Delta$ contains every
$\Delta_z\Delta_{z'}^{-1}$, i.e. all translations along $d := (1,B^{-1}(1-A))$,
and conjugation by $\Delta_z$ turns a translation by $v$ into one by $Lv$. Now
$Ld$ is parallel to $d$ iff $A+B = 1$. If $A+B\ne1$ then $d,Ld$ are independent
and $G_\Delta$ contains all translations, so it is transitive. If $A+B = 1$ then
$d = (1,1)$ and every $\Delta_z$ shifts the difference $y-x$ by the same constant
$-cB^{-1}$: for $c = 0$ the orbits are the difference classes, and for $c\ne0$ the
shift generates the additive group, so $G_\Delta$ is transitive again.
 ∎

**Theorem 9.12 (the dichotomy).** 
✅ PROVED (R8-B Thm B.4, root-verified; conditional on $(\mathrm{T})$) ⛔ VOIDED (2026-08-17 by $M_{77}^{\mathrm{D}}$): the implication below is intact, its hypothesis is false — see §10.4
*Void in general.* [v7.2 correction:] a previous version of this note added
“true for extensions with clean fibre operations
(Lemma 10.4), which is where $(\mathrm{T})$ does hold”. That
addition was unproved and its second half is *false*:
$M_{385}^{\mathrm{canon}}$ is an extension over a Latin base all of whose fibre
operations are clean, and it refutes $(\mathrm{T})$
(Proposition 10.9(c)). The hypothesis of this theorem is
available only on the models where it has been checked
(§10.4).
Let $M$ be a finite $E677$ magma whose $\Delta$-action is transitive on
$M\times M$, and assume $(\mathrm{T})$. Then *either $M$ is a quasigroup, or
$E255$ fails at every element of $M$* ($\operatorname{tr} N = 0$). In the second case $M$ has no
idempotent, and if $M$ is a minimal counterexample it has no proper subalgebra at
all.

*Proof.* 
By Proposition 9.10, $K$ is a union of $\Delta$-orbits, so
transitivity gives $K = \emptyset$ or $K = M\times M$. In the first case every
column is injective. In the second, $N(t,v)\ge2$ for every $v\in\operatorname{Im}(R_t)$, while
$N(t,t)\le1$ by Lemma 2.6; hence $N(t,t) = 0$ for every $t$, i.e. no $t$
has a left unit. An idempotent would give $N(x,x)\ge1$. Finally a proper
subalgebra of a minimal counterexample is a smaller $E677$ magma, hence satisfies
$E255$, and $E255$ at a point is the same statement there and in $M$.
 ∎

**Corollary 9.13.** 
✅ PROVED (R8-B Cors. B.4.1–B.4.3, root-verified; conditional on $(\mathrm{T})$) ⛔ VOIDED (2026-08-17 by $M_{77}^{\mathrm{D}}$): the implication below is intact, its hypothesis is false — see §10.4
**Retracted: the $\mathbb{F}_7(4x+3y)$ base is alive again, and (NTS) is reopened.**
What survives is the implication itself, on any class where $(\mathrm{T})$ is
available; [v7.2:] the earlier claim that “extensions with clean fibre
operations” is such a class is withdrawn, since $M_{385}^{\mathrm{canon}}$ is
clean and refutes $(\mathrm{T})$ (Proposition 10.9(c)).
(a) A finite $E677$ magma with transitive $\Delta$ and at least one idempotent is
a quasigroup.
(b) **The $\mathbb{F}_7(4x+3y)$ base dies.** It is non-idempotent, so $\Delta$ is
transitive on it (Theorem 9.11, and $1$ orbit of $49$
🧮 COMPUTATIONAL ()), and it has an idempotent; the collapse pattern of any pair-indexed
extension projects to a $\Delta$-invariant subset of $B\times B$, which is
therefore empty (the extension is a quasigroup) or everything (making the diagonal
fibre operation over the idempotent a smaller non-Latin $E677$ magma, impossible
for the smallest such, and $E255$-protected by Theorem 8.13 for a
minimal counterexample). This closes exactly the hole (NTS) that Round 7 left
open — conditionally on $(\mathrm{T})$.
(c) What a base may still be: combining with Theorem 8.13, every
*affine* proper quotient of a non-simple minimal counterexample must be
idempotent-free, i.e. of the exceptional $\mathbb{F}_{31}(5x-4y+1)$ shape whose orders
are pinned to $31\cdot S$ by Theorem 7.34; and those are
$\Delta$-transitive, so Theorem 9.12 then forces $E255$ to fail
*everywhere*, not merely somewhere.

**Remark (the decisive fork — resolved in §10).** 
Either no non-Latin pair-indexed extension over $\mathbb{F}_7(4x+3y)$ — or over any
$\Delta$-transitive base with an idempotent — exists, which closes (NTS); or such
an extension exists and *refutes* $(\mathrm{T})$, killing the
$(\mathrm{W})/(\mathrm{B})$ route. Both outcomes are decisive, and the object to be
searched is the one Round 7 already spent a round on.
**Note added: the second branch is the true one** —
Theorem 10.6. Consistency check: the bases
of all four known non-Latin models are idempotent, hence $\Delta$-imprimitive with
the difference classes as orbits — which is exactly what allows their collapse
patterns (the $\mathrm{QR}$-classes of $M_{77}$, the $\{\pm1\}$-classes of
$M_{176}$) to exist. Had any known model possessed a $\Delta$-transitive base with
an idempotent, $(\mathrm{T})$ would already be refuted.

### 9.4 The shear decomposition and the counting shadows

**Theorem 9.14 (shear decomposition).** 
✅ PROVED (R8-D Thm D.1) 🧮 COMPUTATIONAL ($0$ violations on $10$ models, r8d_shear.py)
Let $\Omega(x,y) := (x, x\backslash y)$ and $\Pi(r,s) := (r\mathbin{*} s, r)$, both
bijections of $M\times M$ ($\Pi$ is the pair rotation of
Proposition 5.6). Then for every $c$

$$

  \Delta_c = \Omega\circ(L_c\times L_c),
  \qquad
  \Pi\circ\Delta_c = (L_c\times L_c)\circ\mathrm{sw} .

$$

Unconditionally, $\Delta_c$ carries the column fibre $\{(a,t) : a\in M\}$ onto the
value fibre $\{(A,s) : A\mathbin{*} s = c\mathbin{*} t\}$.

So the twisted diagonal action is nothing but the plain diagonal action followed
by one *fixed*, $c$-independent shear. That single observation determines the
shape of everything below.

**Definition 9.15.** 
Put $\nu(a,t) := N(t,a\mathbin{*} t)$ and $A(x,y) := N(x\backslash y,\,y)$. The
*cardinality shadow* of $(\mathrm{T})$ is

$$

  (\mathrm{T}^{*})\qquad \nu \text{ is } \Delta\text{-invariant},
  \quad\text{equivalently}\quad A(c\mathbin{*} a,\,c\mathbin{*} t) = \nu(a,t)
   \text{ for all } a,t,c .

$$

**Proposition 9.16.** 
✅ PROVED (R8-D Prop D.4) [implication intact; $(\mathrm{T}^{*})$ itself
**REFUTED** by $M_{77}^{\mathrm{D}}$, having previously been exhaustive for
every model of order $\le77$ ($456\,533$ instances each) and $300\,000$ random on
$M_{176}$, $M_{496}$ with $0$ violations]
$(\mathrm{T})\Rightarrow(\mathrm{T}^{*})$, and in fact
$L_c(S(a,t)) = S(\Delta_c(a,t))$ exactly, where $S(a,t) := \{b : b\mathbin{*} t = a\mathbin{*} t\}$.
Conversely $(\mathrm{T})\iff(\mathrm{T}^{*})$ plus the single inclusion
$L_c(S(a,t))\subseteq S(\Delta_c(a,t))$; so $(\mathrm{T}^{*})$ is strictly the
cardinality half, and it is the half a counting proof could reach.

**Remark (no invariance explanation exists).** 
🧮 COMPUTATIONAL (R8-D §D.3; refuted)
One might hope that $\nu$ (or $A$) is invariant under the *plain* diagonal
action and that $\Omega$ preserves it. Both fail massively:
$\nu(c\mathbin{*} a,c\mathbin{*} t) = \nu(a,t)$ fails in $53\,820$ of $59\,319$ triples on
$M_{77}$, $16\,920/46\,656$ on $M_{176}$, $28\,830/29\,791$ on $M_{496}$, and $A$
behaves identically. So $(\mathrm{T}^{*})$ is a *shear-compensation*
identity: the plain diagonal action moves $\nu$ a great deal and the fixed shear
$\Omega$ moves it back exactly. Together with the refutation of conjugacy and
isotopy (§9.2), this closes every invariance-style explanation of
$(\mathrm{T})$.

**Corollary 9.17 (the two marginals).** 
✅ PROVED (R8-D Cors. D.6, D.6.1, D.7, root-verified; conditional on $(\mathrm{T})$) ⛔ VOIDED (2026-08-17 by $M_{77}^{\mathrm{D}}$,
in which $S_a\in\{247,257\}$ and $\Sigma/n\notin\mathbb{Z}$): the implication below is intact, its hypothesis is false — see §10.4
*In particular “a left identity forces a quasigroup” loses its proof.*
Write $S_a := \sum_tN(t,a\mathbin{*} t) = \sum_b|F_{ab}|$, $H(t) := \sum_vN(t,v)^2$,
$G(u) := \sum_wN(w,u)^2$ and $\Sigma := \sum_{t,v}N(t,v)^2$. Assuming
$(\mathrm{T})$:

- **(a)**  $S_a$ is constant in $a$ (the $t$-marginal, plus transitivity of
$\langle L\rangle$);

- **(b)**  *all or nothing*: $S_a\ge n$ always, with equality iff row $a$
collides with no other row, so either every row is collision-free — $M$ is a
quasigroup — or no row is. In particular a finite $E677$ magma with a
*left identity* $e$ has $S_e = \operatorname{tr} N\le n$, hence $\Sigma\le n^2$, hence
(Cauchy–Schwarz, $\Sigma\ge n^2$ always) it is a *quasigroup*;

- **(c)**  $G(c\mathbin{*} t) = H(t)$, and since $\operatorname{supp} N$ is strongly connected
(Theorem 2.22) this forces $H\equiv G\equiv\Sigma/n$ constant.

**Proposition 9.18 (the global count is exactly circular).** 
✅ PROVED (R8-D Prop D.8) [unconditional: neither the statement nor the
proof uses $(\mathrm{T})$ or Corollary 9.17]
Let $\Xi(c) := |\Delta_c(K)\cap K|$. Then $\Xi(c)\le|K|$ with equality iff $K$ is
$\Delta_c$-invariant, so “$K$ is $\Delta$-invariant for all $c$” is equivalent to
$\sum_c\Xi(c) = n|K|$. But
$\sum_c\Xi(c) = n|K| - \#\{(c,a,t) : (a,t)\notin K, \Delta_c(a,t)\in K\}$, so that
identity is *literally* the statement being proved. Global double counting on
$K$ therefore carries no information beyond the pointwise statement.

**Remark (the marginal comparison, restated without the voided corollary — v7.2).** 
The last clause of this proposition previously read “\dots and the two
marginals of Corollary 9.17 are strictly weaker”, which compares
against a corollary Round 9 has since voided. The comparison is restated here so
that it stands on its own. The two objects being compared are the
*statistics*

$$

  \mathbf{(M1)} a\mapsto S_a \text{ is constant},
  \qquad
  \mathbf{(M2)} H\equiv G\equiv\Sigma/n ,

$$

which are defined in every finite magma, whatever the status of $(\mathrm{T})$.
Unconditionally, (M1) and (M2) fix only the $t$-sum and the $a$-sum of
$\nu\circ\Delta_c$ and say nothing about its distribution, so neither can imply
$\Delta$-invariance of $K$. That they are *strictly* weaker than
$(\mathrm{T})$ was in v7 an expectation; it is now a fact witnessed by a model:
$M_{385}^{\mathrm{canon}}$ satisfies (M1) and (M2) exactly
($S_a\equiv H\equiv G\equiv\Sigma/n = 595$) and refutes $(\mathrm{T})$
(Theorem 10.8, stratum 3). What Corollary 9.17
supplied — and no longer does — is the converse direction, that
$(\mathrm{T})$ implies (M1) and (M2); the two filters of the remark below are
therefore *necessary conditions for $(\mathrm{T})$ in the class where the
corollary's hypothesis holds*, and not a test for $(\mathrm{T})$ anywhere.

**Remark (two cheap falsification filters — and their blind spot).** 
✅ PROVED (R8-D §D.6, root-verified; conditional on $(\mathrm{T})$) ⛔ VOIDED (2026-08-17 by $M_{385}^{\mathrm{canon}}$, which
refutes $(\mathrm{T})$ while passing both filters exactly): the implication below is intact, its hypothesis is false — see §10.4
Corollary 9.17 converts into two $O(n^2)$ table statistics that any
candidate model must pass:

$$

  \mathbf{Filter\ 1:\ } S_a = \sum_tN(t,a\mathbin{*} t) \text{ independent of } a;
  \qquad
  \mathbf{Filter\ 2:\ } H(t) = G(u) = \Sigma/n \text{ for all } t,u .

$$

A candidate violating either *refutes $(\mathrm{T})$ outright*, hence the
whole $(\mathrm{W})/(\mathrm{B})$ route, without any inspection of collapse sets.
Both filters are part of Table 2.

### 9.5 Blocks versus congruences: the statement C1

Corollary 9.2(c) gives “primitive $\Rightarrow$ simple”. The
converse needs the extra statement

$$

  (\mathrm{C1})\qquad \text{every } \langle L\rangle\text{-block system of a
  finite } E677 \text{ magma is a congruence,}

$$

which would upgrade “a minimal counterexample is simple”
(Theorem 8.12) to “$\langle L\rangle$ is primitive” and hand
the problem to O'Nan–Scott. Round 8 did not settle $(\mathrm{C1})$ but made it
decidable, proved it for two large classes, and found no counterexample
[24].

**Proposition 9.19 (decidability).** 
✅ PROVED (R8-C §1) 🖥️ MACHINE-VERIFIED (problems/etp677/R8C_scripts/r8c_blocks.py)
A partition is an $\langle L\rangle$-block system iff it is closed under
$x\sim y\Rightarrow c\mathbin{*} x\sim c\mathbin{*} y$, and a congruence iff it is closed under
that and under $x\sim y\Rightarrow x\mathbin{*} c\sim y\mathbin{*} c$. Every block system is the
join of the principal ones $\beta(0,b)$ (using transitivity), and joins of
congruences are congruences. Hence $(\mathrm{C1})$ holds for $M$ iff
$\mathrm{leftclosure}(0,b) = \mathrm{fullclosure}(0,b)$ for every $b$ — a test
costing $O(n^3)$.

**Theorem 9.20 ($(\mathrm{C1})$ for affine models).** 
✅ PROVED (R8-C T-A)
Let $x\diamond y = Fx+Gy+c$ be an affine $E677$ magma on a finite abelian group
$A$. Then every $\langle L\rangle$-block system is a congruence.

*Proof.* 
$L_yL_0^{-1}$ is translation by $Fy$, and $F$ is onto, so $\langle L\rangle$
contains all translations and $\langle L\rangle = A\rtimes\langle G\rangle$ with
$A$ regular; the blocks through $0$ are the $G$-invariant subgroups $S$, and the
coset partition by $S$ is a congruence iff $FS\subseteq S$ and $GS\subseteq S$.
Now $F = (G+G^3)^{-1}$ and $u := G+G^3$ lies in the finite commutative ring
$\mathbb{Z}[G]\le\operatorname{End}(A)$; $u$ acts invertibly, so it is not a zero divisor of $\mathbb{Z}[G]$,
and a non-zero-divisor of a finite commutative ring is a unit. Hence
$F = u^{-1}\in\mathbb{Z}[G]$ and every $G$-invariant subgroup is $F$-invariant.
 ∎

**Theorem 9.21 (no $2$-block system).** 
✅ PROVED (R8-C T-B) 🖥️ MACHINE-VERIFIED (problems/etp677/R8C_scripts/r8c_proofs.py)
No finite $E677$ magma has an $\langle L\rangle$-block system with exactly two
blocks.

*Proof.* 
Let $\pi : M\to\mathbb{Z}_2$ be the block map and $f(c)\in\mathbb{Z}_2$ the indicator of “$L_c$
swaps the blocks”, so $\pi(c\mathbin{*} x) = \pi(x)+f(c)$. Applying $\pi$ to
$\mathrm{KEY}$ in the form $L_{y\mathbin{*} x}(y) = \Lambda_x\Lambda_y(x)$ gives
$f(y\mathbin{*} x) = \pi(x)+\pi(y)+f(x)+f(y)$. Hence $\lambda(x) := (\pi(x),f(x))$ is a
magma homomorphism onto its image in $(\mathbb{Z}_2^2,\,\bullet)$ with
$(p,q)\bullet(r,s) = (r+q, p+q+r+s)$, and the image has at least two elements
because $\pi$ is onto. But $(\mathbb{Z}_2^2,\bullet)$ has no subalgebra of order $\ge2$
satisfying $E677$ — by direct enumeration of all $15$ subsets its only proper
subalgebras are two singletons, and the whole $4$-element algebra fails $E677$.
 ∎

This is self-contained: it needs only the $4$-element label table, not the
exhaustive small-order searches, and it strengthens
Corollary 9.2(d), which only said that a $2$-block system could not
be a *congruence*.

**Theorem 9.22 (refinement is a congruence).** 
✅ PROVED (R8-A Thm 5 and R8-C T-C)
Project $\mathrm{KEY}$ through a block system $\theta$ with block set $B$,
$k = |B|$, and put $\Phi(x) := \bar L_x\in\bar G := G/K_\theta$. Then
$\Phi(y\mathbin{*} x)(\bar y) = \Phi(x)^{-1}\Phi(y)^{-1}(\bar x)$, and $\theta$ is a
congruence iff $\Phi$ is constant on blocks. If $\bar G$ acts *regularly* on
$B$, then $\lambda(x) := (\bar x,\Phi(x))$ is a magma homomorphism, so
$\ker\lambda$ is a *congruence* with at most $k^2$ classes; hence either
$\theta$ is a congruence or it is strictly refined by a congruence with $\le k^2$
classes.

For general $\bar G$ the method stalls for a precise reason: the projected
identity pins $\Phi(y\mathbin{*} x)$ down at the *single* point $\bar y$, and a
permutation of $k>2$ points is not determined by one value.

**Theorem 9.23 (exact reformulation, and where it becomes circular).** 
✅ PROVED (R8-C T-D)
$(\mathrm{C1})$ is equivalent to “every left-compatible equivalence of a finite
$E677$ magma is right-compatible”. Moreover, for any left-compatible $\theta$ and
any $a\mathrel\theta b$,

$$

  L_b^{-1}L_a\in K_\theta
  \iff \Theta_a(x)\mathrel\theta\Theta_b(x) \forall x
  \iff \Lambda_a(x)\mathrel\theta\Lambda_b(x) \forall x
  \iff L_bL_a^{-1}\in K_\theta,

$$

and the first and last are equivalent for free because $K_\theta\trianglelefteq G$.
So the natural term-level attack — rewrite $L_b^{-1}L_a$ through $\mathrm{KEY}$
and push it through $\theta$ — *provably closes into a tautology*:
$\mathrm{KEY}$ carries the kernel condition onto its own $\Lambda$-mirror.

**Remark (status of $(\mathrm{C1})$).** 
🧮 COMPUTATIONAL (R8-C §§2, 7; $31$ models, orders $5$–$496$, $0$ separations)
$(\mathrm{C1})$ was verified on $31$ models — the zoo, several direct products,
$M_{77}\times\mathbb{Z}_5$ of order $385$, $M_{496}$, and ten *new* non-affine
translation-invariant gadget extensions built for the purpose — with no
separation between the block lattice and the congruence lattice. Every observed
block count lies in the $E677$ spectrum, as $(\mathrm{C1})$ requires. A bounded
first-order search timed out rather than saturating, with a passing positive
control, so $(\mathrm{C1})$ is recorded as **conjectured true**, not as
shown-underivable: the honest statement is that the natural term route is
provably circular (Theorem 9.23) and no derivation was found within
the budget.

### 9.6 The two legs, and why there are only two

*Status note (added in v7.2).* Every statement in this subsection is made
under $(\mathrm{T})$, or under $(\mathrm{T})+(\mathrm{A})$, and Round 9 refuted
both (Theorem 10.6). The implications proved here are intact and
are used below only as implications; *no conclusion of this subsection may be
read as an unconditional fact about finite $E677$ magmas*, and each statement
now carries that qualification locally as well as in the retraction table of
§10.4. The one statement of the subsection that is not known to
be false is $(\mathrm{R})$ itself, which remains unrefuted.

Under $(\mathrm{T})$ — false in general, see the status note —
$(\mathrm{W})$ holds, hence $\varrho^{*}$ is an
$\langle L\rangle$-block system. By Theorem 9.1 it is a congruence iff

$$

  (\mathrm{R})\qquad a\mathrel\varrho b  \text{ and }  a\mathbin{*} u = b\mathbin{*} w
  \implies u\mathrel{\varrho^{*}}w ,

$$

verified exhaustively with $0$ violations in $2.1$M instances over the four
non-Latin models then known ❓ CONJECTURE (exhaustive $4/4$ at the time; [v7.2] $(\mathrm{R})$
was re-verified in Round 9 on the three new models as well, $0/17\,787$ in
$M_{77}^{\mathrm{D}}$ and $0/444\,675$ in each order-$385$ object, so the count
is now $7/7$). Round 8 then showed that
$(\mathrm{R})$ is not an independent third leg [25].

**Theorem 9.24 (mirror forms).** 
✅ PROVED (R8-E E1, E5) 🧮 COMPUTATIONAL (identical instance counts on three models)
$(\mathrm{R})$ is equivalent to each of
$(\mathrm{R}^\Lambda)$: $a\mathrel\varrho b\Rightarrow a\backslash v\mathrel{\varrho^{*}}b\backslash v$
for every $v$, and
$(\mathrm{R}^\Theta)$: $\Theta_a(v)\mathrel{\varrho^{*}}\Theta_b(v)$ for every $v$.
Moreover $\varrho$ is self-mirror: $E_{ab} = L_a(F_{ab}) = L_b(F_{ab})$, so
$a\mathrel\varrho b$ iff $a\backslash u = b\backslash u$ for some $u$.

**Theorem 9.25 ($(\mathrm{R})$ is the $(\mathrm{C1})$-instance at $\varrho^{*}$).** 
✅ PROVED (R8-E E2) ⚠️ implication intact, hypothesis refuted in Round 9 (the hypothesis $(\mathrm{T})$ is refuted, and so is
$(\mathrm{A})$ in the displayed critical lemma): see §10.4. Nothing below may be read as an unconditional statement about finite $E677$ magmas
$(\mathrm{T})+(\mathrm{C1})\Rightarrow(\mathrm{R})$. Conversely $(\mathrm{R})$
*is* the kernel condition at the single partition $\varrho^{*}$, so it
inherits every $(\mathrm{C1})$ result — in particular it holds in every affine
model (Theorem 9.20), and $\varrho^{*}$ never has exactly two
classes (Theorem 9.21). *Under those hypotheses the critical
lemma therefore reads*

$$

  (\mathrm{A}) + (\mathrm{T}) + (\mathrm{C1}) \implies (\mathrm{S}).

$$

[v7.2:] two of the three hypotheses are now known false, so the display is an
implication with no available antecedent; it is superseded by
Theorem 10.10, which reaches $(\mathrm{S})$ from
$(\mathrm{B})+(\mathrm{Prop})$ instead. What survives here unconditionally is the
second sentence: $(\mathrm{R})$ is an instance of $(\mathrm{C1})$, and every
$(\mathrm{C1})$ theorem applies to it.

**Theorem 9.26 (separation criterion).** 
✅ PROVED (R8-E E3) 🧮 COMPUTATIONAL ($4/4$ models, r8e_sep.py) ⚠️ implication intact, hypothesis refuted in Round 9 (both hypotheses,
$(\mathrm{T})$ and $(\mathrm{A})$, are refuted): see §10.4. Nothing below may be read as an unconditional statement about finite $E677$ magmas
Assume $(\mathrm{T})$ and $(\mathrm{A})$, so $\varrho^{*}$ is a block system with
$k$ blocks of size $m$ and induced group $\bar G\le\operatorname{Sym}(B)$. If
$\mathrm{fix}(\bar G) := \max\{|\operatorname{Fix}(h)| : 1\ne h\in\bar G\} < |F_{ab}|/m$ for
every $\varrho$-pair, then $(\mathrm{R})$ holds. In $M_{77}$,
$M_{77}^{\mathrm{NT}}$, $M_{176}$ and $M_{496}$ the group $\bar G$ is
$\mathrm{AGL}(1,11)$ resp. $31\!:\!\mathbb{Z}_{10}$ — *Frobenius*, so
$\mathrm{fix}(\bar G) = 1$ — while $|F_{ab}|/m = 5,5,2,15$. Hence
*in those four models, whose hypotheses were checked one by one,
$(\mathrm{R})$ is a theorem and not an assumption.*
[v7.2 scope correction:] this was stated in v7 as “in every known non-Latin
model”. It is not: the criterion needs $(\mathrm{T})$ and $(\mathrm{A})$, which
$M_{77}^{\mathrm{D}}$ refutes, and $(\mathrm{T})$, which
$M_{385}^{\mathrm{canon}}$ refutes, so it says nothing about the three models
added in Round 9. $(\mathrm{R})$ nevertheless still *holds* in all of them
— $0/17\,787$ in $M_{77}^{\mathrm{D}}$ and $0/444\,675$ in each order-$385$
object 🖥️ MACHINE-VERIFIED (problems/etp677/R9_audit.py) — but there by
verification, not by this criterion.

*Proof.* 
For $t\in F_{ab}$ we have $\Phi(a)(\bar t) = \Phi(b)(\bar t)$. By $(\mathrm{A})$,
$F_{ab}$ is $\varrho^{*}$-saturated, hence a union of $|F_{ab}|/m$ blocks, so
$\Phi(b)^{-1}\Phi(a)$ fixes at least that many blocks; the hypothesis forces it to
be the identity, which is $(\mathrm{R})$ via Theorem 9.1.
 ∎

**Theorem 9.27 (the mechanism behind $(\mathrm{A})$).** 
✅ PROVED (R8-E E4) 🧮 COMPUTATIONAL ($0/2541$ and $0/14520$ partial fixed sets) ⚠️ implication intact, hypothesis refuted in Round 9 (the hypothesis $(\mathrm{T})$ is refuted, and the subject
$(\mathrm{A})$ is false in general as well): see §10.4. Nothing below may be read as an unconditional statement about finite $E677$ magmas
Under $(\mathrm{T})+(\mathrm{R})$: $(\mathrm{A})$ holds iff every displacement
$L_b^{-1}L_a$ restricted to every $\varrho^{*}$-block is the identity or
fixed-point-free; it suffices that $K_{\varrho^{*}}$ act *semiregularly* on
each block. In the known models that inner group is the translation group of the
fibre, regular of order $m$ — which is exactly why $(\mathrm{A})$ costs nothing
there. Slogan: *$(\mathrm{R})$ is about the outer action on the blocks
(Frobenius); $(\mathrm{A})$ is about the inner action inside a block
(semiregular)*. [v7.2:] read as an implication only. Its hypothesis
$(\mathrm{T})$ and its subject $(\mathrm{A})$ are both refuted in general
(Theorem 10.6); what the theorem still does is explain why
$(\mathrm{A})$ costs nothing in the models where it does hold, which
Proposition 10.9(a) now upgrades to a proof for the whole clean
class.

**Remark (failure blueprints: $(\mathrm{A})$ and $(\mathrm{T})$ need the same object).** 
✅ PROVED (R8-E §7, R8-B §B.6)
Let the base of a non-simple $M$ be Latin, so $\varrho\subseteq\varrho^{*}\subseteq$
the fibration. When $\varrho^{*}$ equals the fibration — as in all four known
models — $(\mathrm{A})$ says exactly: *every fibre operation must have all
of its columns with the same kernel*. For affine fibres the column kernel is
$\ker\alpha_{x,y}$, independent of the column, so $(\mathrm{A})$ is free. A
refutation therefore needs a *non-affine* fibre operation, degenerate at one
fibre point and injective at another — which is *verbatim* the requirement
for refuting $(\mathrm{T})$. So the two open legs share one minimal failure
structure, and one search object decides both. $(\mathrm{R})$, by contrast, can
fail only if $\varrho^{*}$ is strictly finer than the fibration and
$\mathrm{fix}(\bar G)\ge|F_{ab}|/m$ — the opposite of the Frobenius behaviour
every known quotient has.

**Corrected in Round 9** (v7.1 local marker): Theorem 10.8(ii)
shows this remark is only *half* right — the shared failure structure
kills $(\mathrm{T})$, but only its *unbalanced* version also kills
$(\mathrm{A})$: the canonical order-$385$ object refutes $(\mathrm{T})$ while
satisfying $(\mathrm{A})$ exactly. “One search object decides both” is
retracted; the two laws are decoupled.

**Remark (the zoo has almost no discriminating power here).** 
🧮 COMPUTATIONAL (R8-A §7; WARN-2 discipline of §7.6)
All four known non-Latin models are pair-indexed extensions with *affine*
fibre operations, in which a column collapses iff $\alpha_{x,y} = 0$ — a
condition depending only on the base coordinates, which is $(\mathrm{A})$ for
free. So $(\mathrm{A})$, $(\mathrm{B})$ and $(\mathrm{W})$ holding on the zoo is
close to *zero* evidence. The same applies to the prior “all known non-Latin
models are non-simple”: they are non-simple *by construction*, and by
Theorem 8.12 every non-simple magma is an extension. The one
genuinely unconditional fact in support of $(\mathrm{S})$ is
Theorem 9.3. This is the fifth occurrence of the trap catalogued
in §7.6.

### 9.7 Two barriers: existential and injective

Corollary 9.17(a) suggests proving $S_a$ constant
*unconditionally*, which would make the “all or nothing” dichotomy and
“a left identity forces a quasigroup” unconditional. Round 8 mapped that route
completely, and found two distinct reasons why the campaign's proof technique
cannot reach it.

**Theorem 9.28 (the existential barrier).** 
✅ PROVED (R8-F Thm F.2) 🧮 COMPUTATIONAL (exhaustive over $6\,739\,216$ depth-$\le2$ term
pairs)
Let $X_a := \{(u,t) : u\mathbin{*} t = a\mathbin{*} t\}$, so $|X_a| = S_a$. Exactly *eight*
pairs of depth-$\le2$ terms define a bijection $X_a\to X_{c\mathbin{*} a}$, all of the form
$(u,t)\mapsto(c\mathbin{*} u, \gamma)$ with

$$

\begin{aligned}
  \gamma\in\{\,&c\mathbin{*}(a\backslash t), c\mathbin{*}(u\backslash t), (c\mathbin{*} a)\backslash(c\mathbin{*} t), (c\mathbin{*} u)\backslash(c\mathbin{*} t),\\
  &(c\mathbin{*} c)\mathbin{*}(a\backslash t), (c\mathbin{*} c)\mathbin{*}(u\backslash t), (c\backslash c)\mathbin{*}(a\backslash t), (c\backslash c)\mathbin{*}(u\backslash t)\,\},
\end{aligned}

$$

the third being $(\mathrm{T})$ itself. But for *any* term $\gamma$ the
implication $u\mathbin{*} t = a\mathbin{*} t\Rightarrow(c\mathbin{*} u)\mathbin{*}\gamma = (c\mathbin{*} a)\mathbin{*}\gamma$
supplies a witness for the saturating goal of Proposition 9.9, so
*every* such statement is finite-only. Hence the technique of
Theorems 7.9 and 7.12 — a term-defined
bijection whose correctness is a first-order consequence — cannot prove
$S$-constancy through any of them, and at depth $\le2$ there is no bijection with
a different first component.

**Remark (honest nuance).** 
$S$-constancy is a *cardinality* statement and does not itself imply that
goal, so the target is not logically blocked — only this route to it is. A proof
must be a global counting argument that never exhibits a pointwise
correspondence. Consistently, the group-like explanation is refuted: if the
displacement multiset $\{L_b^{-1}L_a : b\}$ were independent of $a$ then $S$ would
be constant ✅ PROVED (R8-F §F.3), but that hypothesis 🧮 COMPUTATIONAL (holds in all six Latin
benchmarks and) *fails in all four non-Latin models*.

The companion identity is sharper and cleaner.

**Theorem 9.29 (the $Q$-matrix).** 
✅ PROVED (R8-G Thm G.1) 🖥️ MACHINE-VERIFIED (problems/etp677/R8_invariants.py)
Let $Q(a,x) := \#\{z : a\mathbin{*} z = z\mathbin{*} x\} = |\operatorname{Fix}(L_a^{-1}R_x)|$. Then all row sums
of $Q$ equal $n$ — for each $z$ the equation $a\mathbin{*} z = z\mathbin{*} x$ determines
$x = z\backslash(a\mathbin{*} z)$ uniquely — so $Q$ has total $n^2$, and

$$

  (\mathrm{S}')\qquad S'_x := \sum_zN(z,\,z\mathbin{*} x) = \sum_aQ(a,x) = n
  \quad\text{for every } x

$$

is exactly the statement that $Q$ has constant column sums. Equivalently,
$(\mathrm{S}')$ is Theorem 7.9 with $L_a$ replaced by
$L_a^{-1}$.

**Theorem 9.30 (the injectivity barrier).** 
[the barrier is **[computed]** and stands; $(\mathrm{S}')$ itself is
**REFUTED** 2026-08-17 by $M_{77}^{\mathrm{D}}$, where
$S'_x\in\{42,77,112,147\}$ — it had been exact, value $n$, in $10/10$ models,
with $\approx100\%$ failure on random left quasigroups]
🧮 COMPUTATIONAL (R8-G §§ G.2–G.4; $12$ prover9 saturations)
The proof of Theorem 7.9 does not transpose: the identity
$|\operatorname{Fix}(L_aR_x)| = N(a,x)$ has no analogue for $Q$ (on $M_{77}$ the entries of $N$
lie in $\{0,1,7\}$ and those of $Q$ in $\{0,11\}$); the uniqueness mechanism
“exactly one $z$ with $b\mathbin{*} z = z\mathbin{*} x$” is *refuted*
($M_{77}$: $\{0\!:\!5390, 11\!:\!539\}$; $M_{176}$:
$\{0\!:\!5280, 1\!:\!25344, 16\!:\!352\}$; it survives in the Latin models and,
curiously, in $M_{496}$); and the opposite magma is not an $E677$ magma, so there
is no duality. Since $\sum_xS'_x = n^2$ unconditionally, $(\mathrm{S}')$ follows
from an *injection* $\Psi_x := \{(a,z) : a\mathbin{*} z = z\mathbin{*} x\}\to M$, and exactly
$21$ depth-$\le2$ terms are injective on every $\Psi_x$ of every one of the ten
models. **None of those injectivity statements is first-order derivable**:
twelve of them were put to prover9 and all twelve saturated.

**Remark (what this upgrades).** 
Injectivity has no existential in its conclusion, so the barrier of
Theorem 9.28 does not apply to these statements — yet they are
finite-only too. This is an *independent* second barrier, and it upgrades the
campaign's reading of Proposition 5.1: it is not only
witness/existential statements about the collapse structure that need finiteness,
*plain injectivity statements do as well*. Every known route to an exact
$E677$ counting identity beyond Theorems 7.9 and
7.12 now passes through a non-first-order step.

**Proposition 9.31 (where $(\mathrm{S}')$ would inject).** 
✅ PROVED (R8-G Prop G.5, root-verified; conditional on $(\mathrm{S}')$) ⛔ VOIDED (2026-08-17 by $M_{77}^{\mathrm{D}}$): the implication below is intact, its hypothesis is false — see §10.4
$(\mathrm{S}')$ implies that *every finite $E677$ magma with a right identity
satisfies $E255$*: if $z\mathbin{*} x_0 = z$ for all $z$ then
$S'_{x_0} = \sum_zN(z,z) = \operatorname{tr} N$, so $(\mathrm{S}')$ gives $\operatorname{tr} N = n$, which is
$E255$ by Theorem 2.7. $M_9$ is such a magma
(Theorem 7.25), with $\operatorname{tr} N = 9$. This is the companion of
Corollary 9.17(b), “a left identity forces a quasigroup”: the two
shadows of $(\mathrm{T})$ each kill one identity type. Beyond this,
$(\mathrm{S}')$ does not inject into $(\mathrm{A})$, $(\mathrm{T})$ or
$(\mathrm{S})$; it is a *technique* target.

### 9.8 Status, the decisive object, and the Round-9 outlook

| statement | status (as of the end of Round 8; see §10.4) |
|---|---|
| $(\mathrm{S})$ | **open** |
| $(\mathrm{A})+(\mathrm{T})+(\mathrm{C1})\Rightarrow(\mathrm{S})$ | proved (Theorems 9.4, 9.25); *route dead in Round 9* |
| $(\mathrm{T})\Rightarrow(\mathrm{W})\Rightarrow(\mathrm{B})$, $(\mathrm{T})\Rightarrow(\mathrm{T}^{*})$ | proved (implications intact) |
| $(\mathrm{T})$, $(\mathrm{T}^{*})$, $(\mathrm{A})$, $(\mathrm{S}')$ | **refuted in Round 9** (Theorem 10.6); each had been exhaustively verified on every model then available, and none is first-order |
| $(\mathrm{R})$ | conjectured, exhaustively verified, not first-order; survives, and is redundant in every known model (Theorem 9.26) |
| $(\mathrm{C1})$ | conjectured true; proved for affine models; survives |

**Remark (the decisive object).** 
Three independent lines — the (NTS) hole of Round 7, the failure blueprint for
$(\mathrm{T})$ (§9.3), and the failure blueprint for
$(\mathrm{A})$ (§9.6) — converge on *one* object:

> a finite $E677$ magma given as a pair-indexed extension whose fibre operation at
> some base pair is **non-affine and genuinely two-variable**, degenerate at
> one fibre point and injective at another, over a base whose $\Delta$-orbit
> structure permits a partial collapse pattern.

Such an object refutes $(\mathrm{T})$ and $(\mathrm{A})$ simultaneously, or —
if it provably does not exist — closes (NTS) and, with $(\mathrm{C1})$, gives
$(\mathrm{S})$. **Note added: it exists** (Theorem 10.5), and
Theorem 10.8 shows that the two halves of the prediction come apart:
a $\tau$-dependent object always refutes $(\mathrm{T})$, but only an
*unbalanced* one also refutes $(\mathrm{A})$. The advice to pre-screen
candidates with Filters 1 and 2 was *wrong* — $M_{385}^{\mathrm{canon}}$
passes both and still refutes $(\mathrm{T})$. What survives of this paragraph is
the last clause: by Corollary 9.2(c) the strongest form of the
search is for a non-Latin model with *primitive* $\langle L\rangle$.

**Remark (cross-vendor result, not independently verified).** 
[claimed in [26]; source: an external reasoning model; *not*
re-derived or machine-checked by this campaign]
A parallel line of the campaign put the same target to a third-party reasoning
model. It reports (i) two near-misses — an order-$13$ table failing $E677$ at
$6$ of $169$ instances, and an order-$23$ construction
$a\mathbin{*} b = a+p(b-a)$ with $p$ a derangement (so that *no* element has a left
unit) failing at $46$ of $529$ pairs — and (ii) an impossibility argument for
the narrowed route above: if the other fibre operations are held at a fixed
cocycle completion, then one of the three star-instances determines the
left-unit-pair operation $\star$ *uniquely*, and the unique solution is the
original, separable one; hence no transposition $\Phi$ can be implemented and a
single-operation defect cannot exist. If correct, this is consistent with, and
sharper than, Theorem 8.9: it says a counterexample must perturb at
least one *other* fibre operation away from the cocycle family at the same
time. **We record it as a claim.** It has not been re-derived here, its
machine check has not been run in our pipeline, and nothing in
§§8–9.8 depends on it.
**Note added:** Round 9 proved it, in the stronger form
Theorem 10.3, and the same source went on to produce one of the two
decisive objects (§10.3); both are now verified here.

**Table 2 (Round-7/8 invariants).**

| model | $n$ | $(\mathrm{Q})$ | $\varrho^{*}$ | prim. | $(\mathrm{C1})$ | $\#\Delta$-orb. | $\lvert K\rvert$ | $S_a$ | $\Sigma$ | $H\!=\!G$ | $(\mathrm{T})$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| $\mathbb{Z}_5$, $2x-y$ | 5 | yes | 5 | yes | yes | 5 | 0 | 5 | 25 | 5 | 0 |
| $\mathbb{Z}_7$, $4x+y$ | 7 | yes | 7 | yes | yes | 1 | 0 | 7 | 49 | 7 | 0 |
| $\mathbb{Z}_7$, $4x+3y$ | 7 | yes | 7 | yes | yes | 1 | 0 | 7 | 49 | 7 | 0 |
| $\mathbb{F}_9 = M_9$ | 9 | yes | 9 | yes | yes | 1 | 0 | 9 | 81 | 9 | 0 |
| $\mathbb{Z}_{11}$, $4x+8y$ | 11 | yes | 11 | yes | yes | 11 | 0 | 11 | 121 | 11 | 0 |
| $\mathbb{F}_{16}$ quandle | 16 | yes | 16 | yes | yes | 16 | 0 | 16 | 256 | 16 | 0 |
| $E_{31}$ | 31 | yes | 31 | yes | yes | 1 | 0 | 31 | 961 | 31 | 0 |
| $M_{77}$ | 77 | **no** | 11 | no | yes | 11 | 2695 | 287 | 22099 | 287 | 0 |
| $M_{77}^{\mathrm{NT}}$ | 77 | **no** | 11 | no | yes | 11 | 2695 | 287 | 22099 | 287 | 0 |
| $M_{176}$ | 176 | **no** | 11 | no | yes | 12 | 5632 | 656 | 115456 | 656 | 0 |
| $M_{77}\times\mathbb{Z}_5$ | 385 | **no** | 55 | no | yes | 55 | 67375 | 1435 | 552475 | 1435 | 0 |

*Recomputed by `problems/etp677/R8_invariants.py`. $\varrho^{*}$ = number of classes of the transitive closure of the collapse relation; "prim." = $\langle L\rangle$ primitive; $\#\Delta$-orb. = orbits of the twisted diagonal action; $K$ = collapse locus; $S_a$ and $H\!=\!G$ are the two filters of §9.4 (a single value means constant, as $(\mathrm{T})$ predicts); $(\mathrm{T})$ = violations of the transport law, exhaustive for $n\le77$ and $200{,}000$ random above.*

*__Note added:__ $(\mathrm{T})$ is false in general (Theorem 10.6); a zero in that column means only that the law holds in that model. Every model here does have clean fibre operations (Lemma 10.4), which is a common feature of the rows and not an explanation of them: [v7.2] cleanness does not imply $(\mathrm{T})$ (Proposition 10.9(c)). The $Q$-matrix row sums (Theorem 9.29) and $S'_x = n$ were verified for every row. $M_{496}$ is omitted — its $\Delta$-orbit computation is $O(n^3) = 1.2\cdot10^8$ — and its figures (31 $\varrho^{*}$-classes, $\Sigma = 2{,}031{,}616$, $S_a = 4096$, $(\mathrm{T})$ verified on $200{,}000$ random instances) are quoted from [23].*

Table 2 is the Round-7/8 companion of Table 1, and it is
consistent with it: $M_9$ appears in both, in Table 1 as the model
that refutes injectivity of $e$ and here as a primitive quasigroup with a single
$\Delta$-orbit. The two filters are constant in every row, as they must be if
$(\mathrm{T})$ is true; the only genuinely new row is $M_{77}\times\mathbb{Z}_5$, whose
values are the multiplicative products of those of its factors — another
instance of the multiplicativity that makes direct products useless as tests
(§7.6).

## 10. Round 9: the decisive object, and a retraction chain

Section 9.8 ended with a specification rather than a theorem: three
independent lines converged on one hypothetical object — a pair-indexed
extension with a *non-affine* fibre operation whose degeneracy depends on
the fibre point — and the fork was that such an object either does not exist,
closing (NTS), or exists and refutes the transport law $(\mathrm{T})$.

**It exists.** Round 9 [27] constructed two of them independently, and
the second branch of the fork is the true one. This section reports the objects,
the theorems that made them constructible, and — at equal length, because it is
the more useful half — the resulting *retraction chain*: every statement of
Sections 8 and 9 that rested on $(\mathrm{T})$ is
now void in general. Following the convention of this paper, nothing is deleted:
the voided statements are kept, with their proofs, and marked. A retracted
conditional theorem still records what *is* true — the implication — and
the record of which hypotheses died is the campaign's most transferable output.

### 10.1 The general extension equation and three structural theorems

Everything below drops the affine ansatz. Let $(B,\diamond)$ be a *Latin*
finite $E677$ magma (by Theorem 8.12 a non-simple $E677$ magma is
such an extension, and a non-Latin base would be a smaller counterexample), let
$V$ be a $q$-set, and for each ordered pair $(x,y)\in B^2$ let $\diamond_{x,y}$ be
a left quasigroup operation on $V$ — its *rows*
$\lambda^{x,y}_s : t\mapsto s\diamond_{x,y}t$ are permutations, its *columns*
$\rho^{x,y}_t : s\mapsto s\diamond_{x,y}t$ are arbitrary maps. Put
$(x,s)\mathbin{*}(y,t) := (x\diamond y, s\diamond_{x,y}t)$, and with
$z_3 = y\diamond x$, $z_4 = z_3\diamond y$, $z_2 = x\diamond z_4$ set
$P_1 = (y,z_2)$, $P_2 = (x,z_4)$, $P_3 = (y,x)$, $P_4 = (z_3,y)$ as before.

**Theorem 10.1 (the general extension equation).** 
✅ PROVED (R9-A Thm 1) 🧮 COMPUTATIONAL (agrees with the full-table $E677$ check on every model)
$N = B\times V$ satisfies $E677$ if and only if for all $x,y\in B$ and all
$s,t\in V$

$$

  t \diamond_{P_1}\Bigl(s\diamond_{P_2}\bigl((t\diamond_{P_3}s)\diamond_{P_4}t\bigr)\Bigr) = s .

$$

The two scalar equations of Lemma 7.19 are its affine specialisation.
Moreover (*the collapse dictionary*) the extension fails right cancellation
iff some column $\rho^{x,y}_\tau$ is non-injective, and all of $F_{ab}$,
$\ker R_t$, the multiplicity matrix, $S_a$, $H$ and $G$ are assembled fibrewise
from the column-kernel data of the $\diamond_{x,y}$, by the formulas displayed in
the proof.

*Proof.* 
Write $X = (x,s)$ and $Y = (y,t)$. Then

$$

  Y\mathbin{*} X = (z_3, t\diamond_{P_3}s),\quad
  (Y\mathbin{*} X)\mathbin{*} Y = \bigl(z_4, (t\diamond_{P_3}s)\diamond_{P_4}t\bigr),\quad
  X\mathbin{*}\bigl((Y\mathbin{*} X)\mathbin{*} Y\bigr) = \bigl(z_2, s\diamond_{P_2}(\cdots)\bigr),

$$

using at each step that the fibre operation used in a product is indexed by the
ordered pair of base coordinates of its two factors: those pairs are $(y,x)$,
$(z_3,y)$ and $(x,z_4)$, that is, $P_3$, $P_4$ and $P_2$. One more product gives
$Y\mathbin{*}\bigl(X\mathbin{*}((Y\mathbin{*} X)\mathbin{*} Y)\bigr)
 = \bigl(y\diamond z_2, t\diamond_{P_1}(\cdots)\bigr)$ with index $P_1 = (y,z_2)$.
The base coordinate is $y\diamond z_2 = y\diamond(x\diamond z_4) = x$, since
$(B,\diamond)$ itself satisfies $E677$. So the $E677$ instance at $(X,Y)$ holds
iff its fibre coordinate equals $s$, which is the displayed equation; quantifying
over $x,y\in B$ and $s,t\in V$ gives the equivalence. (Every ordered pair
$(x,y)$ arises, so no instance is missed.)

For the dictionary, note first that
$(x,s)\mathbin{*}(y,\tau) = (x',s')\mathbin{*}(y,\tau)$ forces $x\diamond y = x'\diamond y$,
hence $x = x'$ because $B$ is Latin, and then
$\rho^{x,y}_\tau(s) = \rho^{x,y}_\tau(s')$. Consequently, writing elements of
$N$ as pairs:

$$

  \ker R_{(y,\tau)} = \bigsqcup_{x\in B} \{x\}\times\ker\rho^{x,y}_\tau ,
  \qquad
  F_{(x,s)(x',s')} =
  \begin{cases}
    \{(y,\tau) : \rho^{x,y}_\tau(s) = \rho^{x,y}_\tau(s')\}, & x = x',\\[2pt]
    \emptyset, & x\ne x',
  \end{cases}

$$

and, for the multiplicity matrix of the extension,
$N\bigl((y,\tau),(w,v)\bigr) = \bigl|(\rho^{x,y}_\tau)^{-1}(v)\bigr|$ where $x$ is
the unique base element with $x\diamond y = w$. In particular a column of the
Cayley table of $N$ is non-injective iff one of the $\rho^{x,y}_\tau$ is, which
is the right-cancellation statement. Since $S_a = \sum_tN(t,a\mathbin{*} t)$,
$H(t) = \sum_vN(t,v)^2$, $G(u) = \sum_wN(w,u)^2$ and $\Sigma = \sum_{t,v}N(t,v)^2$
are sums of these entries, each of them is a sum over $x\in B$ of a quantity
depending only on the column kernels of $\diamond_{x,y}$; the explicit weighted
form, for translation-invariant extensions, is
Definition 10.7(iii).
 ∎

**Theorem 10.2 (degeneracy transfer).** 
✅ PROVED (R9-A Thm 2)
Under the equation of Theorem 10.1, for every $t$

$$

  \rho^{P_4}_t\circ\lambda^{P_3}_t \;=\; \Theta_t,
  \qquad \Theta_t(s) := s\backslash_{P_2}\bigl(t\backslash_{P_1}s\bigr).

$$

Hence $\ker\rho^{P_4}_t = \lambda^{P_3}_t(\ker\Theta_t)$: *the entire
column-collapse structure of the fibre operation at $P_4$ — including how it
depends on the fibre point $t$ — is determined by $\diamond_{P_1}$ and
$\diamond_{P_2}$ alone; $\diamond_{P_3}$ only relabels.* Consequently, writing
$N_{Q}(t,w) := |\{u\in V : u\diamond_{Q}t = w\}|$ for the multiplicity matrix of
a single fibre operation,

$$

  N_{P_4}(t,w) = \bigl|\operatorname{Fix}\bigl(\lambda^{P_1}_t\circ\rho^{P_2}_w\bigr)\bigr| .

$$

This is the pair-indexed *analogue* of Lemma 2.19, derived below
from the extension equation; [v7.2:] it is *not* an instance of that lemma,
which is a statement about a whole $E677$ magma and about the operation's own
left division, and the fibre operations $\diamond_{Q}$ are not $E677$ magmas.

*Proof.* 
Read the equation as
$\lambda^{P_1}_t\lambda^{P_2}_s\rho^{P_4}_t\lambda^{P_3}_t(s) = s$; since
$\lambda^{P_1}_t$ and $\lambda^{P_2}_s$ are permutations,
$\rho^{P_4}_t\lambda^{P_3}_t(s) = s\backslash_{P_2}(t\backslash_{P_1}s)$, which
is the displayed identity, and applying it to kernels gives
$\ker\rho^{P_4}_t = \lambda^{P_3}_t(\ker\Theta_t)$ because $\lambda^{P_3}_t$ is a
bijection.

[v7.2, the step the review found missing.] Fix $t$ and $w$. Substituting
$u = \lambda^{P_3}_t(s)$ — legitimate because $\lambda^{P_3}_t$ is a
permutation of $V$ — turns $\{u : u\diamond_{P_4}t = w\}$ into
$\{s : \rho^{P_4}_t\lambda^{P_3}_t(s) = w\} = \{s : \Theta_t(s) = w\}$, so
$N_{P_4}(t,w) = |\Theta_t^{-1}(w)|$. Now unfold $\Theta_t$: by definition of
left division,

$$

  \Theta_t(s) = w
  \iff s\diamond_{P_2}w = t\backslash_{P_1}s
  \iff \rho^{P_2}_w(s) = \bigl(\lambda^{P_1}_t\bigr)^{-1}(s)
  \iff \lambda^{P_1}_t\bigl(\rho^{P_2}_w(s)\bigr) = s ,

$$

the last step because $\lambda^{P_1}_t$ is a permutation. Hence
$\Theta_t^{-1}(w) = \operatorname{Fix}(\lambda^{P_1}_t\circ\rho^{P_2}_w)$, which is the claim.
 ∎

**Theorem 10.3 (rigidity).** 
✅ PROVED (R9-A Thm 3)
If the base is Latin then $(x,y)\mapsto P_4(x,y) = ((y\diamond x)\diamond y, y)$
is a *bijection* of $B^2$. Hence every fibre operation is the $P_4$ of exactly
one base pair and satisfies, at that pair,

$$

  u\diamond_{P_4}t = \sigma\backslash_{P_2}\bigl(t\backslash_{P_1}\sigma\bigr),
  \qquad \sigma = t\backslash_{P_3}u .

$$

[v7.1 scope correction:] when $P_4\notin\{P_1,P_2,P_3\}$ this display
*uniquely determines* $\diamond_{P_4}$ from the three partner operations,
and such a fibre operation cannot be perturbed in isolation. When the pair is
*self-referential* — $P_4\in\{P_1,P_2,P_3\}$, as happens for diagonal
pairs over idempotent base points, where all four coincide — the display
involves left divisions in $\diamond_{P_4}$ itself and is a *self-consistency
constraint*, not an explicit determination; uniqueness is *not* claimed
there, and an isolated perturbation is constrained but not excluded by this
theorem alone.

**Remark (the cross-vendor claim of §9.8, now verified and generalized).** 
The remark closing §9.8 recorded a third-party impossibility argument
[26] — “once the other $48$ fibre operations are fixed, one instance
forces the left-unit-pair operation to equal the original one, hence separable”
— explicitly as an unverified claim. Theorem 10.3 *proves
it for every non-self-referential pair*, over every Latin base and every fibre
simultaneously — not a peculiarity of order $77$ or of the two order-$7$ bases.
[v7.1:] for self-referential (e.g. idempotent-diagonal) pairs the theorem yields
only a self-consistency constraint, so the third-party instance is subsumed
exactly when its pair is non-self-referential. Its corollary — that a defect
must be spread over several fibre operations — is exactly how the object below
was found: *both* the square-offset and the non-square-offset operations
differ from those of $M_{77}$. The claim is upgraded from “recorded” to
“confirmed for non-self-referential pairs and generalized”.

**Lemma 10.4 (dichotomy, and constant-column absorption).** 
✅ PROVED (R9-A §4 and Thm 4) 🧮 COMPUTATIONAL (all fibre operations of $M_{77}$,
$M_{77}^{\mathrm{NT}}$, $M_{176}$, $M_{496}$ are clean)
Call a fibre operation *clean* if every column is either injective or
constant. Then $\diamond_Q$ is clean iff it is Latin or *constant-column*
($s\diamond_Qt = c(t)$ with $c$ a permutation). Anything else is a
*decisive* fibre operation: either some column is injective and another is
not ($\tau$-dependent degeneracy), or some column has image size strictly between
$1$ and $q$. Moreover, if $\diamond_{P_2}$ is constant-column then
$\diamond_{P_4}$ is Latin, and if $\diamond_{P_1}$ is constant-column then
$\Theta_t$ is independent of $t$, so $\diamond_{P_4}$ has no $\tau$-dependence:
*a $\tau$-dependent operation requires both $\diamond_{P_1}$ and
$\diamond_{P_2}$ to be non-constant-column.*

Affine fibre operations $s\diamond t = \alpha s+\beta t$ over a field are Latin
when $\alpha\ne0$ and constant-column when $\alpha = 0$ — always clean.
*That is why $(\mathrm{A})$ cost the old zoo nothing* — on the clean class
$(\mathrm{A})$ is a theorem, Proposition 10.9(a) — and it is
the fifth and sharpest confirmation of the benchmark trap of
§7.6. [v7.2:] v7 said the same of $(\mathrm{T})$ and
$(\mathrm{W})$. For $(\mathrm{W})$ cleanness reduces the law to a counting
condition on the base but does not settle it, and for $(\mathrm{T})$ the
explanation is simply wrong: a clean extension can refute $(\mathrm{T})$
(Proposition 10.9(c)). What the zoo's affine fibres do
guarantee is $(\mathrm{A})$; that $(\mathrm{T})$ also held in all of them
remains, on the present evidence, unexplained.

### 10.2 The decisive object $M_{77}^{\mathrm{D}}$

**Theorem 10.5.** 
✅ PROVED (R9-A §6) 🖥️ MACHINE-VERIFIED (problems/etp677/R9_audit.py, an independent audit written for
this paper reading only the archived table
R9A_scripts/r9a_DO_table.txt)
Let the base be $\mathbb{F}_{11}$ with $x\diamond y = 6x+6y$ and the fibre
$V = \{0,\dots,6\}$, and take $\diamond_{x,y}$ to be $D : s\diamond t = 4s+t$ at
offset $d = y-x = 0$, the table $U$ at nonzero quadratic-residue offsets and the
table $W$ at non-residue offsets, where

$$

\begin{array}{c|ccccccc}
U & 0&1&2&3&4&5&6\\\hline
0 & 0&1&2&3&4&5&6\\
1 & 0&1&2&3&4&6&5\\
2 & 0&1&2&3&4&5&6\\
3 & 0&1&2&3&4&5&6\\
4 & 0&1&2&3&4&5&6\\
5 & 0&6&2&3&4&5&1\\
6 & 0&5&2&3&4&1&6
\end{array}
\qquad
\begin{array}{c|ccccccc}
W & 0&1&2&3&4&5&6\\\hline
0 & 5&3&4&1&6&0&2\\
1 & 3&1&2&0&4&5&6\\
2 & 6&2&1&5&0&4&3\\
3 & 1&0&6&3&5&2&4\\
4 & 2&4&5&6&1&3&0\\
5 & 0&1&3&4&2&5&6\\
6 & 4&1&0&2&3&5&6
\end{array}

$$

Then $M_{77}^{\mathrm{D}} := (\mathbb{F}_{11}\times V,\mathbin{*})$ is a finite $E677$ magma of
order $77$: zero $E677$ violations over all $5929$ pairs, all left translations
bijective, $E255$ holds everywhere, and it is not right-cancellative. Its column
profiles are

$$

  U: (7)\,(5,1,1)\,(7)\,(7)\,(7)\,(5,1,1)\,(5,1,1),
  \qquad
  W: (1^7)\,(3,1^4)\,(1^7)\,(1^7)\,(1^7)\,(3,1^4)\,(3,1^4),

$$

so $W$ is injective at $t\in\{0,2,3,4\}$ and degenerate at $t\in\{1,5,6\}$:
*$\tau$-dependent degeneracy*, and $U$ has partial degeneracy. Neither $U$
nor $W$ is affine, and by Lemma 10.4 neither is separable.

**Remark (verification protocol).** 
The construction was verified through four mutually independent code paths — the
pair equation of Theorem 10.1, a self-contained **Python**
re-implementation, the *previous round's* checker `r8a_lib.py`, and a
standalone **C** program reading only the stored table — plus a
**negative control** (swapping two table cells produces $8$ $E677$ failures).
For this paper the table was audited once more, by code written from the
definitions alone (`R9_audit.py`), reproducing every figure below.
*The decisive control is that $M_{77}^{\mathrm{D}}$ satisfies every statement
that is a genuine first-order consequence of $E677$*: Theorem 2.17 and its
refinement, $N(v,v)\le1$, the right-unit count of
Proposition 2.11, and the column-transport identity
$\sum_zN(z\mathbin{*} x,z) = n$ of Theorem 7.9 — all with zero
violations. It fails exactly the statements that were only ever conjectured from
the affine zoo.

**Theorem 10.6 (what $M_{77}^{\mathrm{D}}$ refutes).** 
🖥️ MACHINE-VERIFIED (problems/etp677/R9_audit.py)
In $M_{77}^{\mathrm{D}}$:

| statement | where | violations |
|---|---|---|
| $(\mathrm{T})$ transport law | Definition 9.6 | $174{,}900/1{,}041{,}810$ (exhaustive) |
| $(\mathrm{T}^{*})$, $(\mathrm{T}\text{-flat})$ | Definition 9.15, Proposition 9.10 | fail |
| $(\mathrm{W})$ collapse-count invariance | Proposition 9.5 | $2112/17{,}787$ |
| $(\mathrm{D})$ disjointness of the transported collapse | Proposition 9.8 | $528/2541$ |
| $(\mathrm{A})$ $t\mathrel\varrho t'\Rightarrow\ker R_t = \ker R_{t'}$ | Theorem 9.4 | $165/231$ |
| Filter 1: $S_a$ constant | §9.4 | $S_a\in\{247,257\}$ |
| Filter 2: $H\equiv G\equiv\Sigma/n$ | §9.4 | $H,G\in\{207,287\}$, $\Sigma/n = 19459/77\notin\mathbb{Z}$ |
| $(\mathrm{S}')$ $\sum_zN(z,z\mathbin{*} x) = n$ | Theorem 9.29 | $S'_x\in\{42,77,112,147\}$ |
| $\operatorname{Idem}(M)$ is a subalgebra | Problem 11.6 | $55/121$ idempotent pairs |
| $\theta_\kappa$ is a congruence | Theorem 9.3 | $44$ classes, not a congruence |

Surviving in it: $E255$, $(\mathrm{R})$ ($0/17\,787$), $(\mathrm{B})$ ($\varrho^{*}$
is a congruence with $11$ classes), $(\mathrm{C1})$, $\theta_\kappa\ne\nabla$
($44$ distinct column kernels, as Theorem 9.3 requires),
$\Psi_1 = \operatorname{tr} N = 77$ (Corollary 7.14 is untouched), and every
first-order item. It is *not* simple, so $(\mathrm{S})$ is not refuted.

*Status of this table, and of Theorem 10.5 (v7.2).* Both are
statements about one explicit $77\times77$ Cayley table, and *nothing in
either is proved in-text*. What is proved in-text is only that the data
displayed in Theorem 10.5 — base, fibre, three $7\times7$ tables and
the offset rule — determine that Cayley table, and that $E677$ for it is
equivalent to the finitely many instances of the equation of
Theorem 10.1. Everything else is a finite computation: the $E677$,
$E255$ and cancellation status, the column profiles, and every row of the table
above were computed by `R9_audit.py`, written from the definitions for
this paper and reading only the archived table
`R9A_scripts/r9a_DO_table.txt`, and independently by the round's own
`r9a_verify.c` (a standalone C program), by `r8a_lib.py` (the
*previous* round's checker, which knows nothing of Round 9) and by a
self-contained **Python** re-implementation; the negative control is in the
remark above. Three entries are hand-checkable and are checked in full here: the
$(\mathrm{T})$ witness in the remark below, and the $(\mathrm{S}')$ and
$\operatorname{Idem}$-closure witnesses in the paragraph after it. The reader who wants a
proof rather than an audit should re-run the scripts; the paper claims no more
than that.

The last two rows are new here: the reports of [27] did not test
$(\mathrm{S}')$ or the closure of $\operatorname{Idem}$, and the audit written for this paper
found that the same object refutes both. Two hand-checkable witnesses:
$\sum_zN(z,z\mathbin{*} x)$ already differs from $77$ at $x = 0$; and $(0,0)$ and $(2,0)$
are both idempotent while $(0,0)\mathbin{*}(2,0) = (1,5)$ is not.

**Remark (a hand-checkable refutation of $(\mathrm{T})$).** 
Take $a = (2,0)$, $b = (2,1)$, $t = (0,0)$, $c = (0,2)$. Both $a\mathbin{*} t$ and
$b\mathbin{*} t$ have base coordinate $6\cdot2+6\cdot0 = 1$ and offset $0-2 = 9\in QR_{11}$,
so both use $U$, and $U[0][0] = U[1][0] = 0$: the columns collapse,
$a\mathbin{*} t = b\mathbin{*} t = (1,0)$. Now $c\mathbin{*} a = (1,W[2][0]) = (1,6)$ and
$c\mathbin{*} b = (1,W[2][1]) = (1,2)$, while $c\mathbin{*} t = (0,D[2][0]) = (0,1)$. Solving
$(1,6)\mathbin{*}(y,\tau) = (0,1)$ gives $y = 10$, offset $9\in QR$, $U[6][\tau] = 1$,
i.e. $\tau = 5$; solving $(1,2)\mathbin{*}(y,\tau) = (0,1)$ gives $U[2][\tau] = 1$, i.e. $\tau = 1$. So $(c\mathbin{*} a)\backslash(c\mathbin{*} t) = (10,5)\ne(10,1) = (c\mathbin{*} b)\backslash(c\mathbin{*} t)$.

**Remark (the family, and where the object first appears).** 
🧮 COMPUTATIONAL (R9-A §8; complete DFS validated against the known counts $6$ at $n=5$ and
$1680$ at $n=7$)
Twenty-two distinct decisive objects were harvested at order $77$; all satisfy
$E677$ and $E255$, all fail both filters and $(\mathrm{A})$, and all have
$\varrho^{*}$ equal to the $11$-class fibration. Exhaustive searches show none
exists in the analogous families at order $25$ (exactly $30$ solutions, all with
Latin fibre operations) or at order $55$ (no $\tau$-dependent object, four
conjugacy cases). *Within the searched families the decisive object first
appears at order $77$*; no minimality claim is made outside them.

### 10.3 The order-$385$ objects and the four-stratum theorem

A second decisive object arrived the same evening from an independent source: a
third-party reasoning model produced an order-$385$ magma [28], which was
rebuilt inside the framework above and verified here. It is a pair-indexed
extension with base $\mathbb{F}_{11}\times\mathbb{F}_5$ (order $55$, Latin, idempotent) and fibre
$\mathbb{F}_7$, in which the sign of the selector is flipped on the $\mathbb{F}_5$-diagonal at one
coordinate; because that coordinate is part of $\tau$, the coarse column kernel
again depends on $\tau$. A deliberate variant $M_{385}^{\mathrm{R}}$ flips the
sign on the *offset* instead, which is $\tau$-independent. Both are genuine
$E677$ magmas satisfying $E255$, and they separate the strata.

The four strata are named by properties of the fibre operations. Those names
were used in v7 without definitions — a gap the adversarial review was right to
flag — so they are fixed here, in the form they have in [27, §B.2].

**Definition 10.7 (the vocabulary of the strata).** 
Let $N = B\times V$ be a pair-indexed extension as in §10.1, with
$|V| = q$, and let $\diamond_Q$ be one of its fibre operations, with columns
$\rho^Q_\tau$.

- **(i)**  $\diamond_Q$ is *separable* if there is a group structure on $V$,
maps $\alpha,\beta : V\to V$ and a constant $c$ with
$s\diamond_Qt = \alpha(s)\,\beta(t)\,c$ — the hypothesis of
Corollary 8.6, and the notion whose negation appears in (NTS).
It is *clean* if every column is injective or every column is constant,
equivalently (Lemma 10.4) if it is Latin or constant-column.
*Non-separable* in the table below means: not of that form. An affine
operation $s\diamond_Qt = \alpha s+\beta t$ over a field is separable and clean;
a separable operation has $\ker\rho^Q_\tau = \ker\alpha$ for *every* $\tau$,
so it is clean exactly when $\alpha$ is injective or constant, and in the
Round-7 setting of Corollary 8.6 the equation forces the first
alternative. The non-separability of the specific operations named below is
taken from [27], not re-derived here.

- **(ii)**  $\diamond_Q$ has *$\tau$-independent kernel* if the partition
$\ker\rho^Q_\tau$ of $V$ is one and the same for every $\tau\in V$, and
*$\tau$-dependent kernel* otherwise. Clean $\Rightarrow$ $\tau$-independent
(all kernels discrete, resp. all full), and separable $\Rightarrow$
$\tau$-independent; the converse of the first implication fails, since an
operation whose columns all have one and the same kernel with image size
strictly between $1$ and $q$ is $\tau$-independent and not clean. That is what
stratum 2 below exhibits.

- **(iii)**  Suppose $N$ is *translation-invariant* over an affine base
$x\diamond y = Fx+Gy$: the operation $\diamond_{x,y}$ depends only on the
difference $y-x$. Group the differences into the classes $O$ carrying one and
the same fibre operation $\diamond_O$, let $w_O$ be the size of the class, and
put

$$

  N_O(\tau,v) := \bigl|(\rho^O_\tau)^{-1}(v)\bigr| ,\qquad
  f_O(s) := \sum_{\tau\in V}N_O\bigl(\tau, s\diamond_O\tau\bigr) ,\qquad
  H_O(\tau) := \sum_{v\in V}N_O(\tau,v)^2 .

$$

The extension is *balanced* if the two weighted sums
$\sum_Ow_Of_O(s)$ and $\sum_Ow_OH_O(\tau)$ are constant — independent of $s$,
resp. of $\tau$ — and *unbalanced* otherwise.

- **(iv)**  All four notions are relative to a chosen presentation of the model
as an extension. The same magma can be clean over one base and decisive over
another: $M_{385}^{\mathrm{canon}}$ is clean over its order-$55$ base
(Proposition 10.9(c)) and $\tau$-dependent over its order-$11$
base, which is the presentation used in the table.

**Remark (why those are the right weighted sums, and what balance means).** 
🖥️ MACHINE-VERIFIED (problems/etp677/R9_clean_check.py, step 7)
By the collapse dictionary in the proof of Theorem 10.1, the two
sums of Definition 10.7(iii) are the two filter statistics
themselves:

$$

  S_a = \sum_O w_O\,f_O(s)\quad\text{for } a = (\cdot,s),
  \qquad
  H(t) = \sum_O w_O\,H_O(\tau)\quad\text{for } t = (\cdot,\tau) .

$$

So Filter 1 is exactly the constancy of the first and Filter 2 that of the
second, and inside the translation-invariant family “balanced” and “passes
both filters” are the *same* statement — which is why the informative
columns of the table below are the $(\mathrm{T})$ and $(\mathrm{A})$ ones. On
$M_{77}^{\mathrm{D}}$, where $w_D = 1$ and $w_U = w_W = 5$, the two sums
evaluate to $\{247,257\}$ and $\{207,287\}$: the numbers quoted in
Theorem 10.6, recovered from the three $7\times7$ tables alone.

**Theorem 10.8 (four strata).** 
🧮 COMPUTATIONAL (R9-B §B.2.1: four witness models, instance counts as recorded
there) 🖥️ MACHINE-VERIFIED (problems/etp677/R9_audit.py; every row re-derived here
from the archived tables)

|  | fibre operation | $(\mathrm{T})$ | $(\mathrm{A})$ | Filters 1, 2 | witness |
|---|---|---|---|---|---|
| 1 | affine (clean) | holds | holds | pass | $M_{77}$, $M_{77}^{\mathrm{NT}}$, $M_{176}$, $M_{496}$ |
| 2 | non-separable, $\tau$-*independent* kernel | holds | holds | pass ($1435$) | $M_{385}^{\mathrm{R}}$ |
| 3 | $\tau$-dependent, *balanced* | **FAILS** | holds | **pass** ($595$) | $M_{385}^{\mathrm{canon}}$ |
| 4 | $\tau$-dependent, *unbalanced* | **FAILS** | **FAILS** | **fail** | $M_{77}^{\mathrm{D}}$ |

*What this table is, and what it is not* (v7.2). Every entry is a finite
computation on an archived Cayley table — re-derived for this paper by
`R9_audit.py` and, for the two order-$385$ objects, by the independent C
checker `r9b_verify.c` — and the marker has been corrected from
“proved” to “computational” accordingly. Three consequences of that:

- **(a)**  *No row is an implication.* The table does not assert “fibre
operations of type $X$ $\Rightarrow$ $(\mathrm{T})$”; it records what holds in
four named models. The only implication of that shape proved anywhere in this
paper is Proposition 10.9(a), for $(\mathrm{A})$ on the clean
class — and stratum 3 shows that no such implication is available for
$(\mathrm{T})$ from cleanness, since $M_{385}^{\mathrm{canon}}$ is clean over its
own base.

- **(b)**  *The four rows are not a partition.* They are the four types
realized so far by the nine benchmark models of §10.6. A clean but
non-affine extension, or a separable $\tau$-dependent one, matches no row, and
nothing here excludes further strata; *no exhaustiveness is claimed, and
none is proved in [27]*. Read the table as a separation result — the
four cells it does occupy are pairwise distinguished by the columns — not as a
classification theorem.

- **(c)**  *The filter columns for strata 3 and 4 are definitional*,
by Definition 10.7(iii) — whose labels presuppose the
translation-invariant presentation, which both witnesses do have, over $\mathbb{F}_{11}$
with fibres of size $7$ resp. $35$. The content of those two rows is that a
model exists in each cell, and in particular that a $(\mathrm{T})$-counterexample
can be balanced.

Three corrections follow, each overturning a statement made earlier in this paper.

- **(i)**  **The two filters have a genuine blind spot.** Stratum 3 refutes
$(\mathrm{T})$ while passing Filter 1 and Filter 2 *exactly*
($S_a\equiv H\equiv G\equiv\Sigma/n = 595$). The filters are strictly weaker than
$(\mathrm{T})$, precisely as Proposition 9.18 predicted for
marginals. *A candidate that passes both filters proves nothing.*

- **(ii)**  **$(\mathrm{A})$ and $(\mathrm{T})$ are decoupled.** Stratum 3
refutes $(\mathrm{T})$ but satisfies $(\mathrm{A})$ ($0/1155$). The claim of
§9.6 that the two legs share their minimal failure structure is
therefore only half right: the shared structure kills $(\mathrm{T})$, and only the
*unbalanced* version also kills $(\mathrm{A})$. $M_{77}^{\mathrm{D}}$ remains
the unique known refutation of $(\mathrm{A})$.

- **(iii)**  **Non-separability is not the operative property.** Stratum 2 is
non-separable — its coarse column images have sizes $11$ and $29$, neither
dividing $35$ — and every conjecture still holds in it.
*$\tau$-dependence of $\ker\rho_\tau$ is the operative property*, exactly as
Theorem 10.2 predicts.

### 10.4 The retraction chain

Every statement below is *kept* in this paper, with its proof, and marked
**voided**. In each case the implication proved there remains true; what has
died is a hypothesis.

| statement | status after Round 9 |
|---|---|
| $(\mathrm{T})$, Theorem 9.7 | **REFUTED** by $M_{77}^{\mathrm{D}}$ and $M_{385}^{\mathrm{canon}}$ |
| $(\mathrm{T}^{*})$, $(\mathrm{T}\text{-flat})$, $(\mathrm{W})$, $(\mathrm{D})$, $(\mathrm{A})$ | **REFUTED** by $M_{77}^{\mathrm{D}}$ |
| Propositions 9.8, 9.10, 9.16 | implications intact, *hypothesis false* |
| Theorem 9.12 (the dichotomy) and Corollary 9.13 | **VOID in general.** In particular "the $\mathbb{F}_7(4x+3y)$ base is dead" is retracted — that base is alive again, and (NTS) is reopened |
| Corollary 9.17 and the two filters | **VOID in general.** In particular "a left identity forces a quasigroup" loses its proof |
| Theorem 9.4, route $(\mathrm{A})+(\mathrm{B})\Rightarrow(\mathrm{S})$ | implication intact, *leg $(\mathrm{A})$ false*, so this route is dead |
| Theorems 9.25, 9.26, 9.27 | implications intact, *hypotheses unavailable* |
| $(\mathrm{S}')$, Theorem 9.29; Proposition 9.31 | **REFUTED** by $M_{77}^{\mathrm{D}}$ (new here); the row-sum half of Theorem 9.29 is unconditional and survives |
| $\operatorname{Idem}(M)$ a subalgebra (Problem 11.6) | **REFUTED** by $M_{77}^{\mathrm{D}}$ (new here) |
| $\theta_\kappa$ a congruence | **REFUTED** by $M_{77}^{\mathrm{D}}$ |
| $(\mathrm{B})$, $(\mathrm{R})$, $(\mathrm{C1})$, $(\mathrm{S})$, Theorem 9.3, all first-order items | **survive** |
| The benchmark warning of §7.6 | **vindicated in full** |

*Restricted survivors — rewritten in v7.2.* None of the voided results is
worthless: each holds verbatim on the class where its hypothesis is verified.
The question is which class that is, and v7 answered it wrongly. It asserted
that, since every fibre operation of a separable or affine extension is clean
(Lemma 10.4), $(\mathrm{T})$, $(\mathrm{W})$, $(\mathrm{A})$ and
both filters hold throughout strata 1 and 2, so that
Theorem 9.12 and Corollaries 9.13,
9.17 become true statements about extensions with clean fibre
operations. **No such implication was ever proved — neither in
[27] nor here — and for $(\mathrm{T})$ it is false.** The following
proposition, which is the one piece of new mathematics in this revision,
separates what cleanness gives from what it does not.

**Proposition 10.9 (what cleanness does and does not give).** 
✅ PROVED (this revision (v7.2)) 🖥️ MACHINE-VERIFIED (problems/etp677/R9_clean_check.py, steps 1–6)
Let $N = B\times V$ be a pair-indexed extension over a *Latin* base, with
$|V| = q$, all of whose fibre operations are *clean*, and put
$C_x := \{y\in B : \diamond_{x,y} \text{is constant-column}\}$. Then:

- **(a)**  $\ker R_{(y,\tau)}$ depends only on $y$ and not on $\tau$; hence
$(\mathrm{A})$ *holds* in $N$.

- **(b)**  $F_{ab} = \emptyset$ unless $a = (x,s)$ and $b = (x,s')$ lie in one
fibre, in which case $F_{ab} = C_x\times V$. So $|F_{ab}| = |C_x|\,q$ depends
only on the base coordinate, and $(\mathrm{W})$ holds in $N$ if and only if
$x\mapsto|C_x|$ is constant on $B$.

- **(c)**  $(\mathrm{T})$ does **not** follow. $M_{385}^{\mathrm{canon}}$
is such an extension — base $\mathbb{F}_{11}\times\mathbb{F}_5$ with
$(c,a)\diamond(d,b) = (6c+6d, 2a+4b)$, Latin of order $55$; fibre $\mathbb{F}_7$; and
each of its $55^2$ fibre operations is one of $s\diamond t = 4s+t$,
$s\diamond t = t$, $s\diamond t = 3s+5t$, hence Latin or constant-column — and
it refutes $(\mathrm{T})$, with the explicit witness
$(a,b,t,c) = (70,71,0,14)$ in the labelling
$(c,a,s)\mapsto(5c+a)\cdot7+s$. In it $|C_x| = 5$ for every $x$, so
$|F_{ab}|\equiv35$ and both $(\mathrm{A})$ and $(\mathrm{W})$ do hold, exactly as
(a) and (b) predict.

*Proof.* 
By the collapse dictionary in the proof of Theorem 10.1, two elements
are identified by $R_{(y,\tau)}$ iff they lie in one fibre, over some $x$, and
are identified by $\rho^{x,y}_\tau$. A clean $\diamond_{x,y}$ is Latin or
constant-column (Lemma 10.4), so $\ker\rho^{x,y}_\tau$ is the
discrete partition for every $\tau$, or the full partition for every $\tau$; in
both cases it does not depend on $\tau$, and neither does
$\ker R_{(y,\tau)} = \bigsqcup_x\{x\}\times\ker\rho^{x,y}_\tau$. For
$(\mathrm{A})$, note that $t\mathrel\varrho t'$ means $t\mathbin{*} u = t'\mathbin{*} u$ for some
$u$, which forces $t$ and $t'$ into one fibre by the same dictionary; their
$\ker R$ then agree by what was just proved. That is (a). The same case
distinction gives
$F_{(x,s)(x,s')} = \{(y,\tau) : \rho^{x,y}_\tau(s) = \rho^{x,y}_\tau(s')\}
 = C_x\times V$ for $s\ne s'$, and $\emptyset$ across fibres, which is the first
half of (b). For the second half: $c\mathbin{*} a$ and $c\mathbin{*} b$ lie in the fibre over
$\gamma\diamond x$ when $c$ lies over $\gamma$ and $a,b$ over $x$, so
$(\mathrm{W})$ reads $|C_{\gamma\diamond x}| = |C_x|$ for all $\gamma,x$; since
the base is Latin, $\gamma\mapsto\gamma\diamond x$ is onto $B$, so this holds for
all $\gamma,x$ iff $|C_{\cdot}|$ is constant. The left-division half of
$(\mathrm{W})$ is the same computation with $\gamma\backslash x$. Part (c) is a
finite verification, performed independently of the Round-9 scripts by
`R9_clean_check.py`: it rebuilds the order-$385$ table from the
selector rule, confirms $0$ $E677$ violations in $148\,225$ instances, that the
base is Latin, that all $3025$ fibre operations are clean, that the displayed
witness violates $(\mathrm{T})$ — with $711\,480$ violations over a $1$-in-$7$
stride in $c$ — and that $(\mathrm{A})$ holds ($0/1155$) with
$|F_{ab}|\equiv35$.
 ∎

Consequently the honest restriction is the following, and no more.

- **(1)**  On the clean class, $(\mathrm{A})$ is a *theorem*
(Proposition 10.9(a)), and $(\mathrm{W})$ reduces to a counting
condition on the base. This is the mechanism Theorem 9.27 was
pointing at, now proved rather than observed.

- **(2)**  On the clean class, $(\mathrm{T})$, $(\mathrm{T}^{*})$,
$(\mathrm{T}$-flat$)$ and the two filters have exactly the status they had
before Round 9: *computational observations on named models*. They are
verified in $M_{77}$, $M_{77}^{\mathrm{NT}}$, $M_{176}$ and $M_{496}$
(exhaustively for $n\le77$, $200\,000$ random instances on $M_{496}$;
`R8_invariants.py`) and in $M_{385}^{\mathrm{R}}$ (`R9_audit.py`,
`r9b_verify.c`) — and $(\mathrm{T})$ is *refuted* in the clean
object $M_{385}^{\mathrm{canon}}$. Theorem 9.12 and
Corollaries 9.13, 9.17 therefore survive as statements
about the models in which their hypothesis has been checked, and not about any
structurally delimited class. The sharpest form of the point: over the
*same* Latin base of order $55$ and with the *same* three clean fibre
operations $4s+t$, $t$, $3s+5t$, the two order-$385$ objects differ only in
*which pair gets which operation* — and one satisfies $(\mathrm{T})$
while the other refutes it. Whatever governs $(\mathrm{T})$ is a property of the
assignment $(x,y)\mapsto\diamond_{x,y}$, not of the individual operations.

- **(3)**  Cleanness is in any case relative to a presentation
(Definition 10.7(iv)): $M_{385}^{\mathrm{canon}}$ is clean over its
order-$55$ base and $\tau$-dependent over its order-$11$ base. Any future
“restricted survival” claim must name the presentation.

- **(4)**  The current candidate for a structural class on which the transport
law holds is $\tau$-independence of the coarse column kernels, in the sense of
Theorem 10.8(iii) — a property of the assignment, which is what
(2) says is needed. ❓ CONJECTURE (unproved in either direction; the evidence is the five
models $M_{77}$, $M_{77}^{\mathrm{NT}}$, $M_{176}$, $M_{496}$,
$M_{385}^{\mathrm{R}}$ on one side and the two objects
$M_{77}^{\mathrm{D}}$, $M_{385}^{\mathrm{canon}}$ on the other)

What is lost is exactly the extrapolation from the checked models to all finite
$E677$ magmas — the extrapolation §7.6 had already flagged as
unsupported. The v7 wording of this paragraph is itself the sixth occurrence of
that trap, and the first to be caught by an adversarial review rather than by a
model.

### 10.5 The corrected skeleton, and the state of $(\mathrm{S})$

**Theorem 10.10 (the chain has two legs, not three).** 
✅ PROVED (R9-B B.1.1)
Let $M$ be a finite $E677$ magma, $|M|>1$, non-Latin. If $(\mathrm{B})$
$\varrho^{*}$ is a congruence and

$$

  (\mathrm{Prop})\qquad \varrho^{*}\ne\nabla ,

$$

then $M$ is not simple. Hence $(\mathrm{B})+(\mathrm{Prop})\Rightarrow(\mathrm{S})$.

*Proof.* 
Non-Latin means some column is non-injective, so $\varrho\supsetneq\Delta$ and a
fortiori $\varrho^{*}\supsetneq\Delta$; with $(\mathrm{B})$ and
$\varrho^{*}\ne\nabla$ the closure is a congruence strictly between $\Delta$ and
$\nabla$.
 ∎

**Remark (the existential weakening $(\mathrm{Prop}_{\exists})$; v7.1 correction).** 
Write

$$

  (\mathrm{Prop}_{\exists})\qquad \exists\, a\ne b: F_{ab}=\emptyset,
  \text{ i.e. some } L_b^{-1}L_a \text{ is fixed-point-free.}

$$

Then $(\mathrm{Prop})\Rightarrow(\mathrm{Prop}_{\exists})$: if
$\varrho^{*}\ne\nabla$, pick $a,b$ in different $\varrho^{*}$-classes; a direct
collapse witness $t\in F_{ab}$ would put them in one class. *The converse
fails in general*: $\varrho^{*}=\nabla$ needs only *connectivity* of the
collapse graph, while $\neg(\mathrm{Prop}_{\exists})$ is its
*completeness*. A previous version of this theorem glossed the two as
equivalent; the gloss was wrong and is hereby retracted (the theorem itself is
unaffected, since its hypothesis is $\varrho^{*}\ne\nabla$). Consequences:
$(\mathrm{Prop}_{\exists})$ is a *necessary* condition, so refuting it —
proving every pair collapses directly, $\varrho=\nabla$ — refutes
$(\mathrm{Prop})$; but establishing $(\mathrm{Prop}_{\exists})$ does *not*
establish $(\mathrm{Prop})$. Theorem 10.13 and the design-theoretic
reading below are statements about $(\mathrm{Prop}_{\exists})$ and about
$\varrho=\nabla$, and are re-anchored accordingly.

$(\mathrm{R})$ is *not* a third leg: it entered only as the kernel half of
the dictionary criterion (Theorem 9.1), whose other half — that
$\varrho^{*}$ is a block system — came from $(\mathrm{T})$. And $(\mathrm{A})$
is gone, its role having been to supply properness, which $(\mathrm{Prop})$ now
names directly.

**Remark ($(\mathrm{B})$ has lost its proof).** 
$(\mathrm{B})$ had exactly two derivations: $(\mathrm{W})\Rightarrow(\mathrm{B})$
(Proposition 9.5) and
$(\mathrm{T})+(\mathrm{R})\Rightarrow(\mathrm{B})$ (§9.6), with a
third, $(\mathrm{T})+(\mathrm{C1})\Rightarrow(\mathrm{R})$, feeding the second.
All three hypotheses are refuted. *$(\mathrm{B})$ is therefore an open
conjecture with no surviving proof route*, and its model evidence is the same trap
once more: in every known non-Latin model — $M_{77}$, $M_{77}^{\mathrm{NT}}$,
$M_{176}$, $M_{496}$, $M_{77}^{\mathrm{D}}$, the twenty-two-member family, both
order-$385$ objects — the magma is a pair-indexed extension over a Latin base,
so $\varrho$ is contained in the fibration and $\varrho^{*}$ *is* the
fibration by construction, hence a congruence for free. The evidence for
$(\mathrm{B})$ is close to zero.

**Proposition 10.11 ($(\mathrm{Prop})$ is automatic for extensions).** 
✅ PROVED (R9-B B.3.2)
In any pair-indexed extension over a Latin base, $(x,s)\mathbin{*}(y,t) = (x',s')\mathbin{*}(y,t)$
forces $x = x'$, so $\varrho$ is contained in the fibration, hence so is its
transitive closure, and $\varrho^{*}\ne\nabla$. Hence no pair-indexed extension
over a Latin base violates $(\mathrm{Prop})$, and *no extension-based model
can supply evidence for or against it*. [v7.1 scope correction:] a violator of
$(\mathrm{Prop})$ must lie *outside* this extension class; the further step
— that it may be taken *simple* non-Latin, the counterexample target of
Corollary 9.2(c) — is available only under the
minimal-counterexample reduction, i.e. conditional on the quotient theorem's
hypotheses (NTS/extension-closure), not unconditionally.

**Theorem 10.12 (refined $T3$).** 
✅ PROVED (R9-B B.3.1) 🖥️ MACHINE-VERIFIED (problems/etp677/R9_audit.py)
For $a\ne b$, $|F_{ab}|\le\bigl(n-\mathrm{odd}(L_a)\bigr)/2$ where
$\mathrm{odd}(L_a)$ is the number of odd-length cycles of $L_a$; in particular
$F_{ab}\cap\operatorname{Fix}(L_a) = \emptyset$, and $|F_{ab}|\le(n-1)/2$ for odd $n$.

*Proof.* 
Theorem 2.17 says $F_{ab}$ is an independent set in the functional digraph
of $L_a$, a disjoint union of cycles of lengths $\ell_i$; a cycle of length $\ell$
has independence number $\lfloor\ell/2\rfloor$ and
$\sum_i\lfloor\ell_i/2\rfloor = (n-\mathrm{odd}(L_a))/2$. A fixed point is a
$1$-cycle.
 ∎

**Theorem 10.13 (why the primitive-group route is silent).** 
✅ PROVED (R9-B B.4.1–B.4.2)
Put $D := \{L_b^{-1}L_a : a\ne b\} = S^{-1}S\setminus\{1\}$, where
$S=\{L_a:a\in M\}$. Then $(\mathrm{Prop}_{\exists})$ — the necessary condition
of $(\mathrm{Prop})$, see the v7.1 remark after Theorem 10.10 —
holds iff $D$ contains a derangement, iff $D$ is not contained in the union of
point stabilisers. Jordan's theorem and the Fein–Kantor–Schacher theorem produce
derangements in the *group* $\langle L\rangle$, not in the *subset* $D$,
which is not a subgroup. Worse, by Theorem 10.12 every element of
$D$ with a fixed point moves at least $n/2$ points, so $D$ lies exactly in the
large-support regime where Jordan-type “small support $\Rightarrow$ contains
$A_n$” theorems are silent. [v7.2:] the first two sentences are proved; the
last is a *methodological* observation about the reach of those theorems —
it says that the hypotheses of the Jordan-type results are provably unavailable
here, not that no group-theoretic argument can exist. 🧮 COMPUTATIONAL (on $M_{77}^{\mathrm{D}}$ the fixed-point
distribution over $a\ne b$ is $\{0\!:\!5390, 25\!:\!264, 35\!:\!198\}$)

**Remark (the recommended replacement: design theory).** 
✅ PROVED (R9-B B.4)
$\varrho = \nabla$ says the $n$ partitions $\{\ker R_t\}_{t\in M}$ cover every
pair of points: a *resolvable pairwise covering design* on $n$ points with
exactly $n$ parallel classes. Immediately $\Sigma\ge2n^2-n$; and if moreover every
$|F_{ab}| = 1$ the design is a resolvable linear space with $S_a = 2n-1$ for every
$a$. A linear space on $n$ points whose lines split into $n$ parallel classes is a
very rigid object, so de Bruijn–Erdős and Fisher-type inequalities — with
$N(v,v)\le1$, Proposition 2.11 and Theorem 10.12 as
side conditions — are the natural tool, in place of O'Nan–Scott. Note that
$(\mathrm{Prop})$ is *existential*, so no ATP can be run on it at all,
consistent with §9.7.

> **Corrected skeleton.**
> 

$$

>   (\mathrm{P})  \Longleftarrow [\text{(NTS) closed}] \;+\; [(\mathrm{B})] \;+\; [(\mathrm{Prop})]
>   \;+\; [(\mathrm{Q})\Rightarrow E255 \checkmark]
> 
$$

> Three open legs. $(\mathrm{Q})\Rightarrow E255$ is Corollary 2.8;
> $(\mathrm{B})$ newly lost its proof; $(\mathrm{Prop})$ is untestable on any
> extension; and (NTS) moved *away*, because non-separable fibre operations are
> now known to exist. The Round-7 reassessment that the extension class was turning
> towards $(\mathrm{P})$ must be down-weighted accordingly.

### 10.6 The nine-model benchmark set

**Remark (test order matters).** 
The filter set of §7.6 is superseded. It is now the nine models

$$

  \{M_5, M_9, M_{77}, M_{77}^{\mathrm{NT}}, M_{176}, M_{496}, M_{77}^{\mathrm{D}}, M_{385}^{\mathrm{canon}}, M_{385}^{\mathrm{R}}\},

$$

*tested in this order*: $M_{77}^{\mathrm{D}}$ first, since it alone kills
$(\mathrm{T})$, $(\mathrm{T}^{*})$, $(\mathrm{W})$, $(\mathrm{D})$,
$(\mathrm{A})$, $(\mathrm{S}')$, $\operatorname{Idem}$-closure and both filters; then
$M_{385}^{\mathrm{canon}}$, which kills $(\mathrm{T})$ while *passing* both
filters and $(\mathrm{A})$ — without it one would wrongly conclude that the
filters detect $(\mathrm{T})$-failure; then $M_{385}^{\mathrm{R}}$, the
$\tau$-independent non-separable control, which must *not* be killed. Any
claim verified on the other six carries no evidence at all. Table 1
has been extended with the three new models, and Table 2 must be read
with the $(\mathrm{T})$ column understood as “holds in this model”, never as
evidence for the law.

**Remark (what Round 9 did not do).** 
$M_{77}^{\mathrm{D}}$ and both order-$385$ objects satisfy $E255$. They are not
counterexamples to Problem 1.1, and they do not refute
$(\mathrm{S})$ — all of them are extensions, hence non-simple. What they refute
is a family of conjectures the campaign had erected *about* the route to
$(\mathrm{P})$. The genuinely new positive knowledge of this round is
Theorems 10.1–10.3 and Lemma 10.4,
which for the first time make non-affine models constructible at will: “build a
finite $E677$ magma with prescribed collapse behaviour” is now a small constraint
problem on $|B|^2$ fibre tables. That machinery, not the refutations, is what
should be pointed at $(\mathrm{Prop})$, at $(\mathrm{C1})$ and at the search for a
non-Latin magma with primitive $\langle L\rangle$.

## 11. Open problems and the state of the routes

### 11.1 The main problem

**Conjecture 11.1 ($(\mathrm{P})$; = Problem 1.1).** 
Every element of a finite $E677$ magma has a left unit; equivalently
$\sum_{w}|\operatorname{Fix}(L_w)| = n$; equivalently $\operatorname{tr} N = n$; equivalently every $\Theta_t = R_tL_t$
has a fixed point; equivalently every finite $E677$ magma satisfies $E255$.

The campaign's own view of this shifted twice and is recorded honestly. After Rounds 1–2,
with every known model an affine quasigroup and orders $\le9$ exhausted, the orchestrating
agent judged the evidence to point strongly to “true” — against the community's
expectation [1,3] that a counterexample exists. That judgement was
based on a biased sample (small orders, all affine). The discovery that $(\mathrm{Q})$ is
false — the blueprint's own order-$496$ example, then our order-$176$ one — corrected it:
the escape mechanism in those models is idempotency of the base, which routes $E255$ through
a trivial channel, and it is not obviously unavoidable. The current assessment is
*balanced, with a slight tilt toward a counterexample existing*, consistent with the
community's. We state this because a paper that reported only the final assessment would be
concealing how the evidence moved.

### 11.2 Specific open questions

**Problem 11.2 (smallest non-right-cancellative order).** 
What is the least order of a finite $E677$ magma that is not right-cancellative? It is at most
$77$ (Theorem 7.18; it was $176$ before Round 6) and at least $10$: every $E677$ magma of order $\le 9$ is a
quasigroup (Theorem 6.1), and orders $2,3,4,6,8$ carry no model at all. (The
targeted small-order SAT search of `soff_sat.py` independently returns UNSAT for
$n\le7$.) A
non-translation-invariant fibre assignment over $\mathbb{F}_5$ would give order $80$ and was never
searched; Lemma 7.19 now makes such assignments routine to construct,
so that is the cheapest available test.

**Problem 11.3 (must affine coefficients commute?).** 
Theorem 3.1(a) is a pair of *noncommutative* equations
$GF+G^2FG = 1$, $F+G^2F^2+G^3 = 0$ for $F,G\in\operatorname{End}(A)$. Every solution known to us — here,
in [2], and in [4] — has $FG = GF$, equivalently
$F = (G+G^3)^{-1}$, and only for those does $P(G)=0$ and hence the $R$-module spectrum of
Theorem 3.2 apply. Does a solution with $FG\ne GF$ exist? If not, the
classification of affine models and the even-order spectrum become unconditional; if one
exists, it could realize an order outside the $\mathbb{Z}[u]/(P)$-module spectrum, and
Theorem 3.4(b) would not apply to it. The cheapest test is a search over
$\operatorname{End}(A)$ for small non-cyclic $A$ (e.g. $M_2(\mathbb{F}_p)$, $M_3(\mathbb{F}_2)$).

**Problem 11.4 (the exceptional base).** 
Does the exceptional translation-invariant base $x\mathbin{*} y = 5x-4y+c$ on $\mathbb{F}_{31}$ ($c\ne0$)
— which by Theorem 7.27 is the unique non-idempotent
translation-invariant affine $E677$ base over any field — carry a fibre extension
violating $E255$? Fibre size
$m=3$ is impossible even as an extension; $m=5$ is the first size with a nonempty solution
space; $m=5$ and $m=7$ are unclassified for general fibre tables. For *affine* fibres
the answer is now complete for $m\le7$ (Theorem 7.36): the solution space is exactly
the set of constant families. By Theorem 7.30(d) any counterexample built
here must fail $E255$ on at least $31$ elements, and by (e) one may assume the fibre is
generated by a single violating point.

**Problem 11.5 (the fibre spectrum, and idempotent-free orders).** 
Is $S_0 = 31\cdot S$ — equivalently, does every idempotent-free finite $E677$ magma have
order divisible by $31$ (Conjecture R6-B)? Or, weaker in a different direction, is
$31n\in S\Rightarrow n\in S$? Either statement makes the fibre spectrum conjecture
$\mathrm{FiberSpec}(1) = S$ a theorem and empties the fibre size $m = 8$
(Theorem 7.30(b),(c)). Theorem 7.34 settles the affine case;
the open part is a hypothetical idempotent-free magma that is neither affine nor an
extension of the exceptional base.

**Problem 11.6 (is $\operatorname{Idem}(M)$ a subalgebra? — **answered: no**).** 
**Refuted** by $M_{77}^{\mathrm{D}}$: $(0,0)$ and $(2,0)$ are idempotent while
$(0,0)\mathbin{*}(2,0) = (1,5)$ is not, and closure fails at $55$ of the $121$ idempotent
pairs (Theorem 10.6). Equivalently the square identity fails on
idempotent pairs. This was the surviving fragment of the route through
Conjecture R6-B-2 (§7.4) and the successor target recommended there;
it is now closed, and with it the last carrier of Conjecture R6-B-3.
$\operatorname{Fix}(e) = \operatorname{Idem}(M)$ (Lemma 7.21) is unaffected — it is a
definitional identity.

**Problem 11.7 ($\Psi_1\le\operatorname{tr} N$).** 
Is $\sum_xN(x\backslash x,x)\le\sum_xN(x,x)$ in every finite $E677$ magma? By
Corollary 7.14 this implies Conjecture 11.1; it is implied by
$(\mathrm{Q})$, hence strictly weaker; it holds with equality in all $16$ models of
Table 1; and by Theorem 7.15 no proof of it can be witnessed by
a term map, so any proof must be a counting argument. Its strongest available
falsification design — a fibre family with $a_{-c/B} = 0$ over the exceptional base —
provably does not exist for affine fibres with $q\le7$ (Theorem 7.36), so the
search must be non-affine.

**Problem 11.8 (the general-table $\{1,3\}$ collision).** 
Theorem 4.8 protects the diagonal by a subscript collision $D_1 = D_3$: positions
$1$ and $3$ of (4.1) are the pairs $(y,\Lambda_yx)$ and $(y,x)$, and these coincide
precisely at a left unit. The subscript coincidence is general; the conclusion drawn from it
is not. Two questions, in increasing generality.

- **(a)**  **Answered in Round 6, negatively.** For a *general* fibre table
$\diamond_{y,x}$ — not assumed affine — does $y\diamond x = x$ force $\diamond_{y,x}$ to
be left-injective? **No**: Corollary 7.8. What survives is
non-constancy (Theorem 7.5), and upgrading it to left-injectivity is
$(\mathrm{Q})$ for a block that can be an arbitrary finite $E677$ magma
(Proposition 7.7). The question is therefore not merely open, it is
a restatement of the problem one level down.

- **(b)**  Find the analogue of this self-referential instance of $E677$ at a left unit for a
general finite magma, *without* passing through a congruence block — since by
§7.1 every route through the block is circular. Rounds 7 and 8 have since
mapped this precisely: Theorem 8.1 shows the local picture is the same over
every base, Theorem 8.9 closes the entire separable family, and
Corollary 9.13 appeared to close the last surviving base conditionally on
$(\mathrm{T})$ — but $(\mathrm{T})$ is false (Theorem 10.6), so
**that base is alive again** and this problem is fully open. The decisive
object of §9.8 exists (§10.2) and the machinery of
§10.1 is the tool to point at it.

**Problem 11.9 (the transport law — **answered: false**).** 
$(\mathrm{T})$ was the campaign's single recommended target at the end of Round 8.
It is **refuted** (Theorem 10.6). The question it leaves is
the one that replaced it: *what actually protects $E255$?* Both decisive
objects satisfy $E255$ although every conjecture erected to explain that has now
failed, so the protection mechanism in the $\tau$-dependent stratum is unknown.
The three-instance analysis of §8.2 is independent of
$(\mathrm{T})$ and remains the best available handle.

**Problem 11.10 (blocks versus congruences).** 
Prove or refute $(\mathrm{C1})$: every $\langle L\rangle$-block system of a finite $E677$
magma is a congruence. It holds for all affine models (Theorem 9.20) and on
$31$ tested models; it would upgrade “a minimal counterexample is simple”
(Theorem 8.12) to “$\langle L\rangle$ is primitive” and hand the problem
to the O'Nan–Scott classification. A separating model must be non-affine, have at least $5$
blocks (Theorem 9.21) and a non-regular induced action
(Theorem 9.22).

**Problem 11.11 (the critical lemma).** 
Is a simple finite $E677$ magma right-cancellative? Equivalently
(Theorem 8.12), is a minimal counterexample to
Problem 1.1 simple? The Round-8 route
$(\mathrm{A})+(\mathrm{T})+(\mathrm{C1})$ is dead (§10.4); the
current reduction is $(\mathrm{B})+(\mathrm{Prop})$, Theorem 10.10. To
*refute* $(\mathrm{S})$ it suffices to exhibit a non-right-cancellative finite
$E677$ magma whose left-multiplication group is primitive
(Corollary 9.2(c)) — an $O(n^3)$-checkable property, and one the
construction machinery of §10.1 can now be aimed at.

**Problem 11.12 (properness).** 
$(\mathrm{Prop})$: in a finite $E677$ magma with $|M|>1$, is
$\varrho^{*}\ne\nabla$ — does the direct-collapse graph fail to be
*connected*? With $(\mathrm{B})$ this gives $(\mathrm{S})$
(Theorem 10.10). [v7.1:] its existential weakening
$(\mathrm{Prop}_{\exists})$ — some displacement $L_b^{-1}L_a$ ($a\ne b$)
fixed-point-free, i.e. the collapse graph fails to be *complete* — is
necessary but not sufficient. Both are automatic for every extension
(Proposition 10.11), so no model in the zoo carries any evidence;
under the minimal-counterexample reduction (conditional on NTS) a violator may be
taken simple non-Latin. The permutation-group route is provably silent already
for $(\mathrm{Prop}_{\exists})$ (Theorem 10.13). The design-theoretic
reading of §10.5 addresses the *refutation* side: exhibiting
a resolvable pairwise covering design of $M$ by its $n$ column kernels proves
$\varrho=\nabla$, killing both readings; ruling the design out establishes only
$(\mathrm{Prop}_{\exists})$, and closing the gap from completeness to
connectivity is part of the problem. Note both readings are existential over
finite structure, so no ATP applies.

**Problem 11.13 ($(\mathrm{B})$, now without a proof route).** 
Is $\varrho^{*}$ — the transitive closure of the collapse relation — always a
congruence? Both derivations died in Round 9
(§10.5), and its model evidence is worthless: in every known
non-Latin magma $\varrho^{*}$ is the fibration *by construction*. This is now
the weakest-supported hypothesis in the whole programme, and the first thing the
machinery of §10.1 should be pointed at — a $\tau$-dependent object
whose $\varrho^{*}$ is strictly finer than its fibration would refute it.

**Problem 11.14 (the transposed counting identity — **answered: false**).** 
$(\mathrm{S}')$ $\sum_zN(z,z\mathbin{*} x) = n$ is **refuted**: in
$M_{77}^{\mathrm{D}}$ the sum takes the values $\{42,77,112,147\}$
(Theorem 10.6). Its proved companion, the row-sum half of
Theorem 9.29, is unconditional and survives, as does
Theorem 7.9. What remains open is the question behind the
target: *is there any exact $E677$ counting identity of the
global-cancellation type beyond Theorems 7.9 and
7.12?* Both barriers of §9.7 still stand, and the
refutation of $(\mathrm{S}')$ shows the campaign had no way to tell a true one
from a false one on the evidence it had.

**Problem 11.15 (localized ideal propagation).** 
Implication (2.5) — any set closed under all left translations is closed
under all right translations — is the only genuinely global, non-tautological consequence of
$\mathrm{KEY}$ found. Is there a localized or weighted version, e.g. one applying to a
weighting rather than to a set, which would produce an *upper* bound on $e(O)$ for a
restricted family of $O$? By Corollary 4.2(c) it cannot be uniform over a size
class.

**Problem 11.16 (order $10$, $12$, $14$; the small even orders).** 
Does a non-affine $E677$ magma of order $10$, $12$ or $14$ exist? Theorem 3.4
excludes commuting-coefficient affine ones (a hypothetical noncommuting affine model is not
covered; none was found in the spot search over $M_2(\mathbb{F}_2)$, $M_2(\mathbb{F}_3)$, $M_2(\mathbb{F}_5)$,
$M_3(\mathbb{F}_2)$). Order $10$ is within reach of the symmetry-broken decomposition of
§6.3.

**Problem 11.17 (cycle lengths $4$ and $5$).** 
Is $m(y)\in\{4,5\}$ realizable in some finite $E677$ magma? $m(y)\in\{2,3\}$ is impossible
(Theorem 2.15(a)); $m(y)=4$ forces $E255$ to fail, so a realization at $m=4$ would
be a counterexample; $m=5$ has never been observed. The exclusions have *different*
ranges: $m(y)=4$ is excluded for $n\le 10$ (orders $\le9$ by Theorem 6.1, and the
order-$10$ sub-case $m(0)=4$ was exhausted, Proposition 6.2(b)), whereas $m(y)=5$
is excluded only for $n\le 9$ — the order-$10$ sub-cases $m(0)=5,\dots,10$ never finished
and were discontinued.

**Problem 11.18 (mediality without $(\mathrm{Q})$).** 
Every commuting-coefficient affine $E677$ model is medial (Proposition 3.6),
and a medial $E677$ quasigroup is affine by Toyoda's theorem, hence satisfies $E255$. Since $(\mathrm{Q})$ is
false, that route cannot be completed as originally planned. Is mediality derivable from
$E677$ plus left cancellation? A bounded rewrite saturation reaching $168\,182$ terms per side
did not close it 🧮 COMPUTATIONAL, PARTIAL (R3-F).

**Problem 11.19 (quantitative robustness).** 
Is it true that in any finite left quasigroup of order $n\ge5$, if $E255$ fails then at least
$5$ instances of $E677$ fail, and $5$ is attained (Proposition 6.6)? A proof of
the “$\ge1$” case is Conjecture 11.1 itself; a proof of “$\ge5$” would presumably
expose the mechanism.

**Problem 11.20 (an infinite left-cancellative counterexample).** 
Proposition 5.1 predicts that $E677$ plus left cancellation does not imply $E255$,
which would be witnessed by an *infinite left-cancellative* counterexample. The known
infinite counterexamples (greedy, free) are not left quasigroups. Constructing one would
pin down exactly what finiteness contributes.

### 11.3 Closed routes

Section 5.9 tabulates them, with their exact strengths. In summary, a
proof of Conjecture 11.1 may **not** be: a surjectivity/injectivity argument for
the state map; a marginal count on $N$; a local
amplification of the row-code distance bound; a transport-tree or pair-rotation pigeonhole; a
parity, sign, $2$-adic or Sylow-$2$ argument; an off-diagonal constraint
$N(t,v)+N(v,t)\ge k$; a uniform bound $e(O)\le|O||O^c|$ over a size class;
or a reduction through $(\mathrm{Q})$, which is false. Each of those is closed by a proof or
by an explicit model. Separately, and *on weaker grounds*, an equational or
quasi-equational derivation from $E677$ plus left cancellation resisted every saturation
experiment we ran, but is not proved impossible. The experiments therefore *suggest*
— without proving — that a proof will be global and insensitive to the parity of $n$,
and that it will bound $e(O)$ from above on a family of sets that is not a full size class.
The route that earlier drafts recommended in the same breath — “find the general-magma
analogue of the $\{1,3\}$ collision” — is now known to be circular
(Corollary 7.8), and the criterion of Corollary 7.14 has taken
its place as the campaign's best-shaped unrefuted target. (Round 9 left
Corollary 7.14 untouched — $\Psi_1 = \operatorname{tr} N$ holds in all three
decisive objects — while refuting the $(\mathrm{T})$ programme that had
overtaken it; see §10.4.)

**Remark (superseded in Round 6).** 
The record “$176$ is the smallest known non-right-cancellative order” stood only until
Round 6: Theorem 7.18 exhibits one of order $77$, which is moreover the first
non-idempotent example and is certified in **Lean** 4. It lies outside the
$\theta$-family scanned in §4.5 (its zero-offset fibre has
$a_0+b_0\ne1$), so the scoped minimality statement there is unaffected, and the order-$176$
magma remains the witness for everything in §4: the order-$77$ model
satisfies $(\mathrm{S\text{-}off})$ and therefore does not replace it.

## 12. Verification artefacts

All paths are relative to the campaign repository root. Python was run with a project
virtualenv; SAT solving used `kissat` 4.0.4 [30] unless noted.

**Table 3 (verification artefacts).**

| artefact | what it establishes |
|---|---|
| `problems/etp677/F1_tools/cp677.c` | constraint-propagation enumerator; complete classification $n\le9$ (Theorem 6.1) |
| `problems/etp677/F1_tools/verify.py`,<br>`verify2.py`, `an9.py`, `gen2.py` | verification of Lemmas 2.4, 2.5, 2.6, Theorems 2.7, 2.14 and Proposition 2.11 on 18 concrete models of orders $5,7,7,11,13,19,31,37,35,49,55$ including direct products; no violations |
| `problems/etp677/F5_scripts/enum677.py` | propagating backtracking enumerator |
| `problems/etp677/F5_scripts/sat677.py`,<br>`sat_queries.py`, `sat2.py`, `sat3.py` | `kissat` encodings: existence; `not255`; `notlatin`; `nocol0` with symmetry breaking; with the proved $\mathrm{KEY}$ and Lemma 2.6 clauses as redundant constraints |
| `problems/etp677/F5_scripts/enum_iso.py` | SAT enumeration up to isomorphism (blocking whole isomorphism orbits) plus per-model structure report |
| `problems/etp677/F5_scripts/saturate*.py` | congruence closure for the free left quasigroup $+$ $E677$ (Proposition 5.1) |
| `problems/etp677/F5_scripts/nearmiss.py`,<br>`robust.py` | Propositions 6.5, 6.6 |
| `problems/etp677/R3B_scripts/final_verify.py`,<br>`constc.py` | affine criterion versus brute force: $20{,}539$ cases over $\mathbb{Z}_m$, $m<40$, all $(F,G)$; $105{,}624$ cases over $\mathbb{Z}_m$, $m<26$, all $(F,G,c)$ — **0 mismatches** (Theorem 3.1) |
| `problems/etp677/R3B_scripts/paranoia.py` | re-parses the *printed* order-$16$ Cayley table and evaluates the raw $E677$ term on all $256$ pairs: $0$ violations (Theorem 3.4(c)) |
| `problems/etp677/R3B_scripts/extra.py` | order-$25$ model on $(\mathbb{Z}/5)^2$; the $\mathbb{F}_9$ order-$9$ models; exactly $2$ isomorphism classes at order $16$ |
| `problems/etp677/R3B_scripts/analysis.py`,<br>`mvals.py` | sign identity (Proposition 5.8), cycle types, idempotent counts, $m$-multisets, $\sum_z\lvert\operatorname{Fix}(L_z)\rvert$ |
| `problems/etp677/R3B_scripts/search.c` | independent C enumerator with $\mathrm{KEY}$ propagation; re-confirms $n=2,3,4,6,8$ empty and $n=5,7,9$ nonempty |
| `problems/etp677/r3a_search.py` | Theorem 5.7 (all $84$ words of length $\le3$); second-branch enumeration; Proposition 6.7 |
| `problems/etp677/r3f_enum.py`,<br>`r3f_n11_merged.json` | order-$11$ partial census ledger (Proposition 6.3); affine catalogue; mediality checks |
| `problems/etp677/r3f_saturation.py` | bounded mediality rewrite saturation |
| `problems/etp677/R5C_scripts/verify176.py`,<br>`m176.json` | **independent from-scratch verification** of Theorem 4.1(a)–(e) and the full Cayley table: order, $E677$ over all $176^2$ pairs, rows permutations, $N$ margins, $E255$, the value set of $N$, the $(\mathrm{S\text{-}off})$ pairs and the off-diagonal $N(t,v)+N(v,t)$ distribution. It computes *no* subset, support-size or connectivity quantity — for those see `struct_check.py` and `isoperim_check.py` |
| `problems/etp677/R5C_scripts/blueprint_search.py` | $\mathrm{GF}(p^k)$, translation-invariant base enumeration, the index formulas `quads` of Lemma 4.4, magma builder and checkers |
| `problems/etp677/R5C_scripts/bp_sat.py` | the SAT search that found the order-$176$ magma |
| `problems/etp677/R5C_scripts/minimal_scan.py` | Proposition 4.11 (the *range-limited* minimality scan) |
| `problems/etp677/R5C_scripts/conflict_check.py` | Lemma 4.7 over $\mathrm{GF}(3),\mathrm{GF}(4),\mathrm{GF}(5),\mathrm{GF}(8)$; the index coincidence $D_1(-c/A) = D_3(-c/A) = c/A$ of Theorem 4.8 for $p\in\{5,11,31,41,61,71\}$ |
| `problems/etp677/R5C_scripts/m496.py` | rebuild and $N$-analysis of the blueprint order-$496$ model (Corollary 4.10) |
| `problems/etp677/R5C_scripts/term_search.py` | *search* for the term witness in the order-$496$ magma, on a deterministic random sample (default $1200$) of the forced pairs; it does not verify the winner on the full domain |
| `problems/etp677/R5C_scripts/term_full_check.py` | full-domain verification of the term witness on all $111{,}600$ forced ordered pairs of the order-$496$ magma, plus the complete truth table of $w(t,v)\mathbin{*} t = v$ by pair class |
| `problems/etp677/R5C_scripts/isoperim_check.py` | Corollary 4.2(c): $e(O)$ recomputed from `m176.json`; exact maxima of $e(O)-\lvert O\rvert\lvert O^c\rvert$ at $\lvert O\rvert=1,2,3$; explicit witnesses with $e(O)>\lvert O\rvert\lvert O^c\rvert$ for every size $2\le s\le 174$ |
| `problems/etp677/R5C_scripts/struct_check.py` | the order-$176$ statistics that `verify176.py` does not compute: $r_t = c_v = 146$, strong connectivity of $\operatorname{supp} N$, diameter $2$, $Q = \sum N^2 = 115456$, the $\lvert F_{pq}\rvert$ distribution, $\#\mathrm{zeros}(N)$ |
| `problems/etp677/R5C_scripts/soff_sat.py` | small-order falsification search for $(\mathrm{S\text{-}off})$: UNSAT for $n=3,4,5,6,7$ |
| `problems/etp677/R5C_scripts/freemagma.py` | free $677$ magma: $E677$ check and the failure of $(\mathrm{S\text{-}off})$ at distinct generators (Proposition 4.12) |
| `problems/etp677/r5a_search.py` | the extension encoder; `selftest` rebuilds the order-$496$ model with zero violations of (4.1) and zero $E255$ failures |
| `problems/etp677/r5a_audit.py` | independent adversarial audit of the index formulas, the $E255$-violation reduction and the derangement reduction; reported `PASS` |
| `problems/etp677/r5a_bt.c` | specialized backtracking solver for the extension search (searches discontinued; no classification claimed) |
| **Round 6** | |
| `problems/etp677/R6A_scripts/r6a_verify.py` | the whole of §7.1 and §7.2 on $13$ models (orders $5,7,7,11,11,11,11,13,16,19,19,176,496$): Theorems 7.2, 7.3, 7.5, Lemma 7.1, Theorems 7.9, 7.12, 7.13, the $\Psi_k$ and $\mathrm{BIRT}_k$ tables, and the refutations of Theorem 7.17 |
| `problems/etp677/R6A_scripts/r6a_blocks.py` | Proposition 7.7 (blocks are arbitrary) and multiplicativity of the curve masses over direct products |
| `problems/etp677/R6A_scripts/r6a_psi.py` | Proposition 7.16; the $\Psi$ battery on the order-$77$ model; the $c\ne0$ offset analysis behind Theorem 7.36 |
| `problems/etp677/R6A_scripts/r6a_e.py` | Propositions 7.22 and 7.23: the closed form of $e$ in the translation-invariant family, and the free-magma refutation ($4356/4356$) |
| `problems/etp677/R6B_tools.py`,<br>`R6B_qsystem.py`, `R6B_affine.c` | Theorems 7.27, 7.29, 7.31; the fibre-ansatz reductions; the complete affine-fibre solver (deterministic DFS, no SAT) |
| `problems/etp677/R6B_S0.py` | Theorems 7.32, 7.33 (Bézout identity, coefficientwise) and 7.34; the scan producing idempotent-free affine orders $31\cdot\{1,5,7,31\}$ |
| `problems/etp677/R6B_z7_driver.py` | Theorem 7.36: the $1296$-shard complete solution over $\mathbb{F}_7$ ($5.66\cdot10^{10}$ nodes) |
| `problems/etp677/R6C_scripts/r6c_verify.py` | Theorem 7.18: the order-$77$ model, built from the closed formulas and checked exhaustively (no solver, no search) |
| `lean/proofenv/M77.lean` | **kernel-checked Lean 4 certificate** for Theorem 7.18(a)–(c): `decide` only, axiom footprint {`propext`, `Quot.sound`}, with bridging lemmas certifying the encoding |
| `problems/etp677/R6E_scripts/r6e_verify.py` | Lemma 7.19, Theorems 7.20 and 7.24: the $121$ pair-indexed instances, the full table, and the $1050$ homomorphism failures |
| `problems/etp677/R6D_scripts/r6d_m77nt.py`,<br>`r6d_min9.py`, `r6d_survive.py` | independent rebuild of $M_{77}^{\mathrm{NT}}$ from its written specification (no code reuse); Theorem 7.25; the $595\to32$ unary-term collapse of §7.6 |
| `problems/etp677/R6D_scripts/c*.p`, `cm*.in` | Prover9/Mace4 and E 3.1 inputs: five discharged calibration targets, the exhausted **Mace4** searches at $n = 5,7,9$, and the (inconclusive) failed proof attempts |
| `problems/etp677/R6_zoo.py` | Table 1: every column recomputed for all $16$ models, plus the isomorphism $M_9\cong(\mathbb{F}_9,\,x+(t+2)y)$ |
| **Rounds 7 and 8** | |
| `problems/etp677/R7A_scripts/r7a_*.py` | the $\mathbb{F}_7(4x+3y)$ instance system; Theorems 8.3, 8.4, 8.8; the ten-operation defective local solution and the $20/20$ extensions; the global annealer and its residual diagnosis (time-boxed randomised search, no SAT) |
| `problems/etp677/R7A_scripts/r7b_baseindep.py`,<br>`r7b_cocycle.py`, `r7b_thin.py` | Theorem 8.1 on seven bases; the $196\times98$ cocycle system ($B_\star\equiv0$ mod seven primes); Theorem 8.10(b),(c) |
| `problems/etp677/R7A_scripts/r7c_quotient.py`,<br>`r7c_witness.py` | $\langle L\rangle$-transitivity and the quotient structure (Theorem 8.12); the unique-witness formula and the $\Phi$-swap (Proposition 8.14) |
| `problems/etp677/R8A_scripts/r8a_*.py` | Theorems 9.1, 9.3, 9.4, the $(\mathrm{W})$ scan and the refuted conjugacy explanation; the term-witness scan |
| `problems/etp677/R8A_scripts/r8b_transport.py`,<br>`r8b_delta.py`, `r8d_shear.py` | $(\mathrm{T})$ exhaustively to $n=176$ plus the random-left-quasigroup control; $\Delta$-orbits and the affine dichotomy; the shear decomposition, $(\mathrm{T}^{*})$ and the two marginals |
| `problems/etp677/R8A_scripts/r8f_bijsearch.py`,<br>`r8f_shadow.py`, `r8g_sprime.py` | the exhaustive depth-$\le2$ term-pair search ($6{,}739{,}216$ pairs, exactly $8$ bijections); $(\mathrm{DS})$; the $Q$-matrix, the refutation of the uniqueness mechanism, and the $21$ injective terms |
| `problems/etp677/R8A_scripts/atp/g*.in`,<br>`h1..h12.in` | the prover9 inputs: six saturations for the collapse statements, one for $(\mathrm{T})$, twelve for the injectivity goals — and `g7`, the **positive control**, in which Theorem 2.17 is proved in $13$ steps |
| `problems/etp677/R8C_scripts/r8c_*.py` | Proposition 9.19 and the $31$-model sweep (including ten new non-affine gadget extensions); machine checks for Theorems 9.20, 9.21, 9.23 |
| `problems/etp677/R8E_scripts/r8e_*.py` | Theorems 9.24, 9.26, 9.27 and the verification table of $(\mathrm{A})$, $(\mathrm{R})$, $(\mathrm{R}^\Lambda)$, $(\mathrm{R}^\Theta)$, $(\mathrm{T})$ |
| `problems/etp677/R8_invariants.py` | Table 2: collapse classes, primitivity, $(\mathrm{C1})$, $\Delta$-orbits, $\lvert K\rvert$, both filters, $Q$-row sums and $(\mathrm{T})$, recomputed for eleven models |
| **Round 9** | |
| `problems/etp677/R9A_scripts/r9a_DO.py`,<br>`r9a_DO_table.txt`, `r9a_verify.c` | the decisive object $M_{77}^{\mathrm{D}}$ (Theorem 10.5): self-contained build, the stored $77\times77$ table, an independent C verifier reading only that table, and the negative control |
| `problems/etp677/R9A_scripts/r9a_dfs.c`,<br>`r9a_anneal.c`, `r9a_family.py` | the exhaustive DFS at orders $25$ and $55$ (validated against the known counts $6$ and $1680$), the directed annealer that found the object, and the battery over the $22$-member family |
| `problems/etp677/R9A_scripts/r9b_canon.py`,<br>`r9b_m385R.py`, `r9b_verify.c` | the two order-$385$ objects and a general table checker; `R9A_scripts_gpt/magma677_order385.py` is the third-party generator |
| `problems/etp677/R9A_scripts/r9b_prop.py`,<br>`r9b_strat.py` | refined $T3$, $(\mathrm{Prop})$ probes, $\theta_\kappa$, and the filter-weight stratification |
| `problems/etp677/R9_audit.py` | **independent audit written for this paper**: reads only the three archived tables and re-derives $E677$, $E255$, every first-order item, and every refutation of Theorem 10.6 — including the two ($(\mathrm{S}')$ and $\operatorname{Idem}$-closure) that the reports had not tested |
| `problems/etp677/R9_clean_check.py`,<br>`R9_clean_check.out` | **written for the v7.2 revision**: Proposition 10.9 — that $M_{385}^{\mathrm{canon}}$ is a clean extension over a Latin order-$55$ base which nevertheless refutes $(\mathrm{T})$, while satisfying $(\mathrm{A})$ and $\lvert F_{ab}\rvert\equiv\lvert C_x\rvert q$ — together with the weighted-statistic identities of Definition 10.7(iii) on $M_{77}^{\mathrm{D}}$ |

## Acknowledgements and division of labour

The attack was organized as a set of independent “approach families” launched in parallel
rounds, with the orchestrating agent forbidden to disclose one family's content to another
within a round, so that convergent discoveries would constitute cross-validation rather than
contamination. Theorem 2.7 was found independently by three families before
being matched against [2, Lemma 13.1(ii)]; the affine spectrum
$P = \Phi_{10}\cdot Q$ was found independently and then matched against the blueprint's
Type 1/Type 2 dichotomy. The order-$176$ magma (Theorem 4.1) was found by a Claude
Fable 5 agent using a SAT search inside the extension framework, and verified by a
from-scratch re-implementation. Theorem 5.7 and
Propositions 6.3, 6.4 were produced by GPT-5.6 through
`codex`. Theorem 2.20 and Propositions 5.10,
5.11 were produced by the orchestrating agent. The refutation of the parity
conjecture (Theorem 3.4) was produced by a Claude Fable 5 agent that had been
tasked with *proving* it. One GPT-5.6 “Pro” web session ran for $89$ minutes on
$(\mathrm{Q})$ without producing usable output and was terminated; this is recorded because
the cost of unproductive runs is part of an honest account of the method.

## References

[1] J. Bolan, J. Breitner, F. Carlini, T. Tao, et al., *The Equational Theories Project: Advancing Collaborative Mathematical Research at Scale*, arXiv:2512.07087, 2025. <https://arxiv.org/abs/2512.07087>. The finite implication $E677\Rightarrow E255$ is recorded there as the single remaining open finite implication, with the authors tentatively conjecturing it to be false.

[2] Equational Theories Project, *Blueprint, Chapter 13: Equation 677*. <https://teorth.github.io/equational_theories/blueprint/677-chapter.html>. Lemma 13.1 (basic properties, including the left-unit criterion), Lemma 13.2 (seven equivalent pointwise conditions for $E255$ at $x$), Lemma 13.3 (no linear counterexamples), Lemma 13.4 (no counterexamples via linear extension), §13.1 (the order-$496$ non-right-cancellative example), §13.2 (the free $677$ magma and its violation of $E255$).

[3] Google DeepMind, *formal-conjectures*, file `FormalConjectures/Other/EquationalTheories_677_255.lean`. <https://github.com/google-deepmind/formal-conjectures>. The file states both directions with marginal notes indicating that the existence of a finite counterexample is expected.

[4] NSF Institute for Computer-Aided Reasoning in Mathematics, *eq677 model database*. <https://eq677.icarm.cloud>. Built on the model searcher of <https://github.com/memoryleak47/eq677>. As of consultation: every known example also satisfies Equation 255.

[5] G. Pochuev, *finite-magma-e677-to-e255*. <https://github.com/Grisha-Pochuev/finite-magma-e677-to-e255>. An independent project on the same problem in combinatorial language; it likewise establishes that all rows are permutations and is stalled at localized obstructions.

[6] AutoMath campaign, internal report `problems/etp677/F1_structural_report.md` (structural algebra of finite $677$ magmas).

[7] AutoMath campaign, internal report `problems/etp677/F4_finitization_report.md` (finitization of the greedy counterexample; Propositions 5 and 6).

[8] AutoMath campaign, internal report `problems/etp677/F5_counting_report.md` (counting, parity and orbit obstructions; the linear spectrum; the saturation experiments).

[9] AutoMath campaign, internal report `problems/etp677/R2_Qprime_codex_report.md` (the state map and its circularity; the doubly-stochastic formulation).

[10] AutoMath campaign, internal report `problems/etp677/R3A_codex_report.md` (amplification of the row-distance bound; second-branch enumeration; perturbation search).

[11] AutoMath campaign, internal report `problems/etp677/R3B_parity_report.md` (refutation of the parity conjecture; the affine criterion in endomorphism form; the even-order spectrum; eight auxiliary lemmas).

[12] AutoMath campaign, internal report `problems/etp677/R3C_linking_report.md` (transport tree and pair rotation; Theorems A and B; the isoperimetric reformulation).

[13] AutoMath campaign, internal report `problems/etp677/R3F_codex_report.md` (partial order-$11$ census; affine benchmark; mediality).

[14] AutoMath campaign, internal report `problems/etp677/R4_literature_recon.md` (literature reconnaissance).

[15] AutoMath campaign, internal report `problems/etp677/R5A_codex_report.md` (adversarial audit of the extension encoder; specialized backtracking solver).

[16] AutoMath campaign, internal report `problems/etp677/R5C_soff_report.md` (the order-$176$ magma; structure theory of the translation-invariant extension family with affine fibres; diagonal protection). *Note:* the extremal isoperimetric table of its §4.2 does not list maxima (Corollary 4.2 and the remark following it), and its §5 concluding prose omits the affine-fibre hypothesis under which Theorem 5.1 there is proved.

[17] AutoMath campaign, internal report `problems/etp677/R6A_selfref_report.md` (the general-magma analogue of the $\{1,3\}$ collision; the $\Psi$ identities; the $\Psi_1$ addendum; the $e$-endomorphism addendum).

[18] AutoMath campaign, internal report `problems/etp677/R6B_spectrum_report.md` (the fibre spectrum conjecture; uniqueness of the exceptional base; the blocking theorem; $S_0$ as an ideal, $\operatorname{Res}(\Phi_{10},Q) = 31$ and $S_0^{\mathrm{aff}} = 31\cdot S$; the complete $\mathbb{F}_7$ solution).

[19] AutoMath campaign, internal report `problems/etp677/R6C_codex_report.md` (the order-$77$ non-idempotent non-right-cancellative model).

[20] AutoMath campaign, internal report `problems/etp677/R6D_eaut_report.md` (refutation of both halves of “$e$ is an automorphism”; the order-$9$ counterexample; the benchmark-set warning).

[21] AutoMath campaign, internal report `problems/etp677/R6E_codex_report.md` (the diagonal-decoupling lemma; the first non-translation-invariant extension; refutation of the $e$-homomorphism half).

[22] AutoMath campaign, internal report `problems/etp677/R7A_report.md` (three chapters: the mixed-idempotent base $\mathbb{F}_7$, $x\diamond y = 4x+3y$, its occurrence theorem and the generalized Lemma 13.4; the base-independent occurrence trichotomy and the cocycle protection theorem; the quotient theorems and the non-first-order status of the conservation law).

[23] AutoMath campaign, internal report `problems/etp677/R8A_simple_report.md` (five chapters: the congruence/block dictionary and the master reduction; the transport law $(\mathrm{T})$ and the twisted-diagonal dichotomy; the shear decomposition, the cardinality shadow and the two falsification filters; the existential barrier; the $Q$-matrix and the injectivity barrier).

[24] AutoMath campaign, internal report `problems/etp677/R8C_blocks_report.md` ($(\mathrm{C1})$: decidability, the affine case, the non-existence of $2$-block systems, and the exact circularity of the term-level route).

[25] AutoMath campaign, internal report `problems/etp677/R8E_AR_report.md` (the legs $(\mathrm{A})$ and $(\mathrm{R})$: mirror forms, the merger of $(\mathrm{R})$ into $(\mathrm{C1})$, the Frobenius separation criterion, and the shared failure blueprint).

[26] AutoMath campaign, harvested transcript `problems/etp677/R6_gpt_counterexample.md` (a third-party reasoning model's counterexample search: two near-misses and a claimed impossibility argument for the single-operation defect route). *Not independently verified by this campaign*; see the remark in §9.8.

[27] AutoMath campaign, internal report `problems/etp677/R9A_DO_report.md` (two chapters: the general extension equation, the degeneracy-transfer and rigidity theorems, and the decisive object $M_{77}^{\mathrm{D}}$; the audit of the repaired chain, the four-stratum theorem, refined $T3$ and the group-theoretic anatomy of $(\mathrm{Prop})$).

[28] AutoMath campaign, harvested artefact `problems/etp677/R9_gpt_DO.md` and generator `R9A_scripts_gpt/magma677_order385.py` (a third-party reasoning model's order-$385$ object, rebuilt and verified inside the framework of §10.1).

[29] AutoMath campaign, **Lean** 4 certificate `lean/proofenv/M77.lean` ($E677$, $E255$, non-idempotency and failure of right cancellation for the order-$77$ model, by kernel `decide`; axiom footprint {`propext`, `Quot.sound`}).

[30] A. Biere et al., *Kissat SAT solver*, version 4.0.4. <https://github.com/arminbiere/kissat>.


## Revision history

- **v1** (2026-08-17) — First complete draft, compiled from the campaign reports F1, F4, F5, F7, R2, R3-A, R3-B, R3-C, R3-F, R4, R5-A, R5-C and the campaign registry.
- **v2** (2026-08-17) — Repairs after adversarial review round 1 (verdict INVALID): six content corrections (C1–C6, e.g. the {1,3} collision scoped to affine fibres, bounded saturation demoted to computational evidence, the (S-off) criterion split into unconditional/conditional directions) and six editorial corrections (E1–E6, e.g. the verification-marker convention stated, notation collisions renamed), all following "weaker rather than stronger."
- **v3** (2026-08-17) — Second adversarial review (verdict VALID-WITH-GAPS): mediality scoped to commuting coefficients, an overclaim ("a proof must be global") downgraded to "suggests," extremal wording made exact, markers completed.
- **v4** (2026-08-17) — Note added on the order-77 model and its Lean certificate.
- **v5** (2026-08-17) — New "Round 6" section from reports R6-A–R6-E (all root-verified): the general-magma {1,3} analogue and its negative answer to the general-table collision problem; uniqueness of the exceptional base and the main theorem $S_0^{\mathrm{aff}} = 31\cdot S$; the order-77 model with a Lean 4 kernel certificate; the diagonal-decoupling lemma and the first non-translation-invariant extension; an independent rebuild of that extension and a second, independent refutation of "$e$ is injective."
- **v5.1** (2026-08-17) — Qwen review of the Round 6 chapter: 3 of 4 items confirmed independently; one potentially-critical gap on the logical status of the diagonal "occurrence collapse" fixed with a new Remark separating the restriction and construction directions, plus an audit of every use.
- **v6** (2026-08-17) — New "Round 7" and "Round 8" sections from reports R7A, R8A, R8C, R8E: the base-independent occurrence trichotomy and cocycle protection theorem; quotient theorems constraining a minimal counterexample; the congruence/block dictionary, master reduction, and the conjectured transport law (T); three distinct verification markers introduced, including the new conditional marker `\PROVEDC`.
- **v7** (2026-08-17) — New "Round 9" section plus a paper-wide retraction chain, from R9A and a third-party report: the decisive objects $M_{77}^{\mathrm{D}}$ and $M_{385}^{\mathrm{canon}}$ refute (T), (T*), (W), (D), (A) and more; new `\VOID` macro marks every affected statement (implication kept, hypothesis flagged false); new proved results including the rigidity and degeneracy-transfer theorems and the clean/decisive dichotomy.
- **v7.1** (2026-08-18) — Repairs after adversarial review (Qwen3.8-Max, verdict INVALID: 4 CRITICAL + 8 GAP): all four criticals fixed (QC1–QC4, e.g. a false gloss in the rigidity theorem retracted, a claim rescoped to the minimal-counterexample reduction); new `\HYPDEAD` macro for statements whose hypothesis Round 9 refuted.
- **v7.2** (2026-08-18) — Second repair pass on the same review, closing the six remaining justification gaps (G5, G6, G8, G9, G11, G12; G7 done in v7.1): one restriction claim demoted and half of it refuted outright (with a new Proposition "cleansurv" and machine-checked artefact `R9_clean_check.py`); conditional-status markers added throughout the "legs" section; proofs supplied for the fibrewise-assembly theorem; missing definitions supplied for the four-stratum theorem; the unconditional part of the marginal-counting proposition isolated; the transfer-identity derivation completed.
