You are a LaTeX-writing mathematician working on a research paper. Your job is a REWRITE PASS,
not a research pass: you are given finished, adjudicated mathematics and you must render it as
a new section of an existing paper, in that paper's exact style and notation. Do not invent
mathematics, do not "improve" statements, do not add results. Your output will be adjudicated
line by line against the source before anything is used; anything you change silently will be
caught and the whole pass rejected.

# 1. The paper

Title: "Partial Results on the WOWII-133 Graffiti Conjecture — The C4-free branch below
floor(l) = 4". It reports partial progress on: a connected graph G satisfies
rad(G) + floor(l(G))^c <= path(G), where path(G) is the order (number of VERTICES) of a longest
induced path, l(G) is the average over v of the independence number a(v) of the open
neighbourhood N(v), and c = 1 if G is C4-free, c = 0 otherwise. The conjecture is OPEN and the
paper does not claim to resolve it.

Notation already defined in the preamble (use these macros, do not redefine them):
  \rad  \ecc  \diam  \pth  \comp  \ball  \gir      (operator names: rad, ecc, diam, path, ...)
Theorem environments already defined: theorem, lemma, proposition, corollary, definition,
problem, question, remark — all numbered in one sequence within a section.
Standing local notation used throughout the paper: a(v) = independence number of N(v);
mu(G) = min_v a(v), written $\mu(G)$; a "usable side-neighbour" x of an end u_0 of a geodesic
u_0...u_d means x in N(u_0) lying outside u_1's component of G[N(u_0)]; "peripherally 3-capped"
means every geodesic of length >= rad has all its usable side-neighbours of a-value <= 3.

Epistemic markers (this paper attaches one to EVERY numbered assertion; they are macros):
  \PRV{scriptnames}  proof given in full here + assertions machine-checked by those scripts
  \PRVn              proof given in full here, nothing machine-checked
  \REV{scriptnames}  as \PRV, and in addition the statement passed TWO adversarial review
                     passes by reviewers from two DISJOINT model families, both returning no
                     surviving defect at any joint classified as mathematics
  \AD{scriptnames}   machine-assisted: originated in a free exploration channel, re-derived
                     here, machine-checked, and passed ONE adversarial review pass
  \MV{scriptnames}   a purely computational statement (an explicit finite graph with its
                     invariants, or a completed bounded sweep) — evidence of exactly the
                     stated scope and nothing more
Script names inside these macros are typeset with escaped underscores, e.g.
\REV{w133\_r11\_g42.py}.

Existing style, verbatim sample from the paper (match this):

```latex
\begin{lemma}[$d = 4$]\label{lem:g36}
\AD{w133\_r10\_adjudicate.py, w133\_r11\_adjudicate.py}
Let $G$ be $C_4$-free with a geodesic $u_0u_1u_2u_3u_4$, $a(u_0)\ge 3$, $a(u_4)\ge 2$, and a
usable side-neighbour $x$ of $u_0$ with $a(x)\ge 4$. Then $\pth(G)\ge 8 = d+4$. No further
hypothesis is needed.
\end{lemma}

\begin{proof}
Choose $y \in N(u_4)$ outside $u_3$'s component, so $y \not\sim u_3$.
...
\end{proof}
```

The marker macro goes on its own line immediately after \begin{...}\label{...}. Proofs are
ordinary LaTeX \begin{proof}...\end{proof}. Prose is British-ish academic English, plain, no
bullet-point mathematics inside theorem statements, em-dashes written as ---.

# 2. What you must produce

ONE new section of LaTeX, to be appended to the paper as a new \section immediately after the
existing \section{The band $\lfloor \ell\rfloor \ge 4$} (whose label is \verb|sec:adopted| and
which contains Lemma~\ref{lem:g36}, Lemma~\ref{lem:g37}, Theorem~\ref{thm:g38},
Corollary~\ref{cor:g38}). Proposed label: \verb|sec:pocket2|. Suggested title: "The band
$\lfloor\ell\rfloor \ge 4$ at large radius". It must contain, IN THIS ORDER:

(A) A short opening paragraph saying what the section does and, explicitly, what tier its
    contents carry (see section 4 below, "STATUS WORDS" — this is mandatory and is graded).

(B) The witness W2 (source S1 below) as a \begin{proposition} with the \MV{} marker, including
    the construction recipe in enough detail that a reader can rebuild the graph, and the
    verified invariants. It is a witness/computational statement, NOT a proof.

(C) Lemma G41 (source S2) with proof — label \verb|lem:g41|.

(D) Theorem G42 (source S3) with proof — label \verb|thm:g42|. Its tightness/non-vacuity
    discussion MUST obey the TWO-NUMBERS RULE in section 4 below.

(E) Lemma G43 and Corollary G44 (source S4) with proofs — labels \verb|lem:g43|,
    \verb|cor:g44|. Immediately after Corollary G44, a \begin{remark} carrying the
    NON-EXHIBITION CAVEAT of section 4 below. This remark is mandatory and is graded.

(F) Theorem G48 and the witness Q32-W (source S5) as a \begin{theorem} with the \MV{} marker
    plus the recipe and invariants, and a short paragraph recording precisely which route the
    witness kills and which it does NOT kill (the scope guard in S5 — reproduce its content,
    it is a limit on what the refutation buys).

(G) A residual-map table (source S6) in booktabs style (\toprule/\midrule/\bottomrule), inside
    a \begin{table}[ht] with \caption and \label{tab:pocket2}, summarising what is closed and
    what is open in this band, and a closing paragraph naming the one surviving open
    configuration.

Length target: 900-1400 words of LaTeX body. Output ONLY the LaTeX for the new section, inside
one fenced ```latex block. No preamble, no \documentclass, no \begin{document}. Nothing else in
your answer except the fenced block and, after it, a short section headed "## Self-audit"
listing (i) every place you were unsure, (ii) every number you copied, and (iii) confirmation
of the three mandatory carries of section 4.

# 3. SOURCE MATERIAL — the adjudicated mathematics, in the project's own working notation.
Reproduce its content faithfully. Where it uses backtick/markdown notation, convert to LaTeX
math. Where it cites a script name, keep it.

## S1 — the witness W2

Theorem (already proved, this is the witness statement): There is a connected C4-free graph G
with l(G) = 6 > 4, rad(G) = diam(G) = 5 (so diam <= rad + 2), and path(G) >= 168 >= rad + 4.

The device, which is the reusable part: a VERTEX-TRANSITIVE graph has rad = diam, so
diam <= rad + 2 automatically; and a TRIANGLE-FREE graph has a(v) = d(v), so a k-regular
triangle-free graph has l = k exactly. Therefore any vertex-transitive C4-free triangle-free
k-regular graph with k >= 5 and diam >= 5 is a witness. Cayley graphs of PSL(2,p) on three
generators supply them.

W2 (the standing hard control): G = Cay(PSL(2,11), S) with
S = {g, g^{-1} : g in {[5 0; 2 9], [1 5; 0 1], [1 6; 10 6]}} over GF(11) (elements of SL(2,11)
taken mod +-I). Machine-verified: n = 660, connected, 6-regular, triangle-free, C4-free, hence
a(v) = 6 for every v and l = 6 > 4; ecc equal from three sampled vertices (transitivity check),
rad = diam = 5; greedy certified induced path of 168 vertices (each certified chord-free), so
path >= 168, far above rad + 4 = 9. Larger members verified the same way: PSL(2,13) (n = 1092,
rad = diam = 6, path >= 239), PSL(2,17) and PSL(2,19) (rad = diam = 7), PSL(2,23) (n = 6072,
rad = diam = 7). Scripts: w133_r11_qradp.py, and independently w133_r15_key.py.

Why it matters: W2 is the campaign's first HARD positive control at large radius. diam + 1 = 6
is strictly below rad + 4 = 9, so the trivial device does not settle it, and the conjecture
nevertheless holds on it with a factor of about 19. A named dead end follows: no counterexample
in this band can be a vertex-transitive C4-free graph of degree >= 5 with an easily-found long
induced path — the expander-like witnesses are all far from tight. Tightness, if it exists,
lives in low-a, triangle-rich, irregular graphs.

## S2 — Lemma G41

Lemma G41 (= the paper's Lemma~\ref{lem:g14} sharpened). G C4-free, geodesic u_0 ... u_d with
d >= 5, a(u_0) >= 2, a(u_d) >= 2, and some usable side-neighbour x of u_0 with a(x) >= 4.
Then path(G) >= d + 4.

Proof: the existing construction of Lemma~\ref{lem:g14}, unchanged: y in N(u_d) outside
u_{d-1}'s component; w in N(x) in a component of G[N(x)] other than u_0's and surviving the
u_2- and u_3-kills (a(x) >= 4 pays for both); then w, x, u_0, ..., u_d, y is induced by exactly
the non-adjacencies that lemma lists. The construction never selects a THIRD component of
G[N(u_0)] — it names only x — so a(u_0) >= 2 (which "some usable side-neighbour x" already
presupposes) is all it consumes. QED.

Scope guard which must be stated: the redundancy is specific to d >= 5. At d = 4
(Lemma~\ref{lem:g36}) and d = 3 (Lemma~\ref{lem:g37}) the proofs pick z in N(u_0) outside BOTH
u_1's and x's components, which genuinely needs a(u_0) >= 3. So G41 does not propagate
downwards.

Machine-checked non-vacuously: on path-joined PG(2,5) chains, 120 frames with a(u_0) = 2
exactly and d >= 5, the construction built and certified chord-free every time.
Script: w133_r11_g14sharp.py.

## S3 — Theorem G42

Theorem G42. Let G be connected, C4-free, with l(G) > 4, rad(G) >= 5, and no vertex of a-value
1 (that is, mu(G) >= 2). Then path(G) >= rad(G) + 4.

Proof (three lines; every ingredient is already in the paper). By the contrapositive of
Theorem~\ref{thm:g38} (i.e. Corollary~\ref{cor:g38}), G is not peripherally 3-capped, so there
is a geodesic u_0 ... u_d with d >= rad(G) >= 5 and a usable side-neighbour x of u_0 with
a(x) >= 4. Since mu(G) >= 2, both a(u_0) >= 2 and a(u_d) >= 2 hold for free — and a(u_0) >= 2
is now all the seed needs, by G41. Apply G41 at d >= 5: path(G) >= d + 4 >= rad(G) + 4. QED.

Machine-checked: script w133_r11_g42.py, exit 0, 0 failures: 50 end-to-end runs of the
mechanism on the two witnesses W1 and W2 — a real cap-break geodesic located on the graph, the
G41 path built by the proof's own recipe, certified induced, and checked against rad + 4.
(W1 is a second witness, a chain of two disjoint copies of the PG(2,5) incidence graph joined
by an internal path; it has mu = 2 and rad = 6. You do not need its details; mention it only as
"a second witness" if you mention it at all.)

TIGHTNESS — this is the sentence the two-numbers rule of section 4 governs. On W2 the path
that the mechanism CONSTRUCTS has exactly 9 vertices, and 9 = rad + 4, so the construction
delivers the bound with no slack to spare; whereas W2's own longest induced path satisfies
path(W2) >= 168. The 9 is a property of the construction, NOT of the graph.

Consequence for the residual: pocket 2's rad >= 5 branch reduces entirely to the a = 1 case.
If G has a leaf or triangle-leaf, peeling reaches mu >= 2 and preserves both C4-freeness and
l > 4, but may LOWER the radius, and path of the peeled graph is only a lower bound for
path(G).

## S4 — Lemma G43 and Corollary G44

Lemma G43. Let G be C4-free with a geodesic u_0 ... u_d, d >= 6, a(u_0) >= 2, and a usable
side-neighbour x of u_0 with a(x) >= 4. Then path(G) >= d + 3 — with NO hypothesis at all on
a(u_d).

Proof. If a(u_d) >= 2, G41 gives d + 4. So let a(u_d) = 1; then N(u_d) is either {u_{d-1}}
(leaf) or {u_{d-1}, q} with q ~ u_{d-1} (triangle-leaf). Truncate to the geodesic u_0 ...
u_{d-1}, of length d - 1 >= 5, and take y := u_d as the far-side vertex. This is legitimate:
u_d in N(u_{d-1}), and u_d lies outside u_{d-2}'s component of G[N(u_{d-1})] — in the leaf case
u_d is isolated there; in the triangle-leaf case its component is {u_d, q}, and u_{d-2} is not
in {u_d, q}, because u_{d-2} != u_d (they are at distance 2) and u_{d-2} = q would force
dist(u_{d-2}, u_d) = 1, contradicting the geodesic. (Note u_{d-2} ~ q is also impossible: q
would then have two neighbours inside G[N(u_{d-1})], which is a matching.) Hence
a(u_{d-1}) >= 2 with y = u_d witnessing it, x is still a usable side-neighbour of u_0 for the
truncated geodesic (same first step u_1), and G41 at d - 1 >= 5 gives
path >= (d-1) + 4 = d + 3. QED.

Machine-checked: script w133_r11_g43.py, exit 0, 0 failures: 24 certified truncation runs on
graphs that DO carry a = 1 vertices (bare-leaf and triangle-leaf variants of the witness W1,
l = 764/133 and 765/134, rad = 8).

Corollary G44. Let G be connected, C4-free, l(G) > 4, rad(G) >= 5. Then path(G) >= rad(G) + 4
UNLESS every geodesic of length >= rad that fails to be 3-capped at an end has length exactly
rad AND a-value 1 at its far end.

Proof. Such a geodesic exists by Corollary~\ref{cor:g38}. If one of them has length
d >= rad + 1 >= 6, G43 gives path >= d + 3 >= rad + 4. If one of them has far end with a >= 2,
G41 gives path >= d + 4 >= rad + 4. QED.

Effect on the residual: combined with G42, the band at rad >= 5 is down to a single
configuration — the cap-break happens only on geodesics of length exactly rad, and every one of
those ends in a leaf or triangle-leaf.

NON-VACUITY, stated exactly: the class {C4-free, l > 4, rad >= 5, some a = 1 vertex} is
inhabited — W1 with a leaf attached, and W1 with a triangle-leaf attached, are members
(l = 764/133 and 765/134, rad = 8). See the caveat in section 4, which is MANDATORY.

## S5 — Theorem G48 and the witness Q32-W

Theorem G48 (machine-verified witness). The following statement, call it (FAR-2), is FALSE:
  "C4-free, l > 4, rad >= 5 implies some geodesic of length >= rad has a usable side-neighbour
   of a-value >= 4 at one end AND a-value >= 2 at the other."

The witness Q32-W: the PG(2,4) point/line incidence graph (42 vertices) with a 2-vertex pendant
hair s — h_s — f_s attached at each of the six vertices arising from S = {[1:0:0], [0:1:0],
[0:0:1]} taken both as points and as lines. All invariants recomputed from the recipe, never
assumed: n = 54, 117 edges, C4-free (strong form, 0 violating pairs), connected, triangle-free,
a-profile {6 vertices of a-value 6, 36 of a-value 5, 6 of a-value 2, 6 of a-value 1},
sum of a = 234, l = 13/3 > 4, rad = 5, diam = 7; and 0 frames over all (u_0, u_1, u_d) with
dist(u_0, u_d) >= rad admit a usable side-neighbour of a-value >= 4 at u_0 together with
a(u_d) >= 2. The configuration is non-vacuous: 480 cap-break frames exist, every one of length
exactly rad = 5 with far-end a-value exactly 1. Script: w133_r13_q32_verify.py, 22/22 checks
pass.

Second thing the same witness kills: peeling the six a = 1 hairs removes exactly 12 vertices
and returns the bare PG(2,4) incidence graph, on which rad drops 5 -> 3 while l stays > 4
(210/42 = 5). So the route "peeling cannot drop the radius" is DEAD in general.

SCOPE GUARD — reproduce this, it is a limit on what the refutation buys. Q32-W does NOT refute
the underlying problem (control the radius drop under a = 1 peeling, or trade it against the
induced path the peeled hairs supply). On Q32-W itself an induced path on at least 14 vertices
exists, found by a depth-first search that does not use the witness's own exhibited path at all
— far above rad + 4 = 9. And what survives as the only live route is the quantitative
hair-exchange trade rad(G) <= rad(G') + h, where G' is the peeled graph and h the hair length;
Q32-W is its named tight control and an EQUALITY instance: h = 2, rad = 5, rad(G') = 3, so
5 <= 3 + 2 holds with equality, and any proof of that trade must execute on this graph.

Also: G42/G43/G44 are unaffected by G48 and are in fact corroborated by it — they govern the
mu >= 2 branch and the reduction to one configuration, whereas Q32-W has mu = 1 and IS an
instance of that one configuration, so it shows the reduction is non-vacuous rather than
threatening it.

## S6 — the residual map (content for the table of (G))

rad >= 5 splits as:
 * mu >= 2 — CLOSED, by Theorem G42.
 * mu = 1 — OPEN, and by G43/G44 it is exactly ONE configuration. Inside it the sub-routes are:
     - the equivalent formulation (FAR-2): DEAD, refuted by Theorem G48;
     - the route "peeling cannot drop the radius": DEAD, same witness;
     - the quantitative hair-exchange trade rad(G) <= rad(G') + h: LIVE, and tight-controlled
       by Q32-W.
Residual for the whole band = this one mu = 1 configuration at rad >= 5, plus the radii 2, 3, 4
(radius 4 additionally wanting the a(u_0) >= 3 upgrade that Lemma~\ref{lem:g36} needs there).

# 4. THE THREE MANDATORY CARRIES — these are graded, and a pass that misses one is rejected

## 4.1 STATUS WORDS
Lemma G41, Theorem G42, Lemma G43 and Corollary G44 have passed TWO adversarial review passes
by reviewers from two disjoint model families, both returning no surviving defect at any joint
classified as mathematics. Therefore:
  * they carry \REV{...}, NOT \AD{...};
  * the section's opening paragraph must say in words that these four carry the two-family
    reviewed tier of \S\ref{sec:conventions}, one tier above the \AD{} results of the previous
    section;
  * it must ALSO say, explicitly, that this is a REVIEW tier and not a claim that the band is
    settled: the band floor(l) >= 4 remains OPEN, no part of the conjecture is closed by this
    section, and nothing here is formally verified.
  * Scripts for the \REV{} markers: G41 -> w133\_r11\_g14sharp.py; G42 ->
    w133\_r11\_g42.py, w133\_r15\_key.py; G43 -> w133\_r11\_g43.py; G44 ->
    w133\_r11\_g43.py. The W2 proposition -> \MV{w133\_r11\_qradp.py, w133\_r15\_key.py}.
    Theorem G48 -> \MV{w133\_r13\_q32\_verify.py}.

## 4.2 THE TWO-NUMBERS RULE (tightness)
Everywhere tightness is discussed, the CONSTRUCTED path length and the GRAPH's own longest
induced path must appear as TWO DISTINCT NUMBERS and must never be merged into a single
"tight" claim. Concretely, for W2 you must print both:
    the constructed path has 9 = rad + 4 vertices   (a fact about the CONSTRUCTION)
    path(W2) >= 168                                 (a fact about the GRAPH)
and say in words that the mechanism is tight while the graph is not, i.e. that the first number
measures the mechanism's slack and the second measures the graph's. Any sentence that reads
"W2 is tight" or "the bound is tight on W2" full stop is WRONG and will fail the pass.

## 4.3 THE NON-EXHIBITION CAVEAT (mandatory remark after Corollary G44)
Corollary G44's EXCEPTIONAL configuration — every non-3-capped geodesic of length exactly rad,
with a-value 1 at its far end — is NOT ITSELF EXHIBITED by any graph the campaign has. What is
exhibited is only the broader class {C4-free, l > 4, rad >= 5, some a = 1 vertex}. Write this
out plainly as a limit on the non-vacuity claim: we know the ambient class is inhabited; we do
NOT know that the exceptional configuration of Corollary~G44 is inhabited, and until a witness
for it exists the corollary's "unless" clause could in principle be vacuous — which would be
good news, but is not knowledge. Do not soften this and do not bury it in a footnote.
(One thing you MAY note, because it is true: Q32-W of Theorem G48 has mu = 1 and every one of
its 480 cap-break frames has length exactly rad with far-end a-value 1 — but Q32-W does not
witness the exceptional configuration, because it has path >= 14 >= rad + 4, so it is not a
graph on which Corollary G44's "unless" clause is doing any work. State this precisely if you
state it at all.)

# 5. Two defects that must NOT propagate into your text
Earlier internal briefs on this material carried two errors. They are listed here so that you
do not reproduce them from any pattern-matching instinct:
 1. A chain-witness family was once quoted with formulas n = 72k - 10 and sum a = 394k - 22
    WITHOUT the qualifier that they hold for one particular parameter value (L = 10) and not
    for the family generally. Do not state any such closed formula at all — the witness W1 is
    not part of your assignment; mention it only as "a second witness" if at all, with no
    numbers except l = 764/133 and 765/134 and rad = 8 where S4 uses them.
 2. Two dangling cross-references to deleted items "H3" and "H4" survived a rebuild. Your
    output must contain NO cross-reference to any label you do not yourself define, EXCEPT the
    following labels which genuinely exist in the paper and which you SHOULD cite:
    sec:conventions, sec:adopted, sec:limits, lem:g14, lem:g36, lem:g37, thm:g38, cor:g38,
    app:artifacts. Any other \ref must point at a label you create in this same section.

Begin. Output the fenced LaTeX block, then the self-audit.
