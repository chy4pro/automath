# WOWII Graffiti.pc Conjecture 61 — Qwen3.8-Max solve attempt on the diameter-4 reduction

**Date:** Tue Aug 18 06:10:12 CDT 2026
**Model:** Qwen3.8-Max (thinking mode ON), via chat.qwen.ai
**Tab ID:** 2130629790
**Conversation URL:** https://chat.qwen.ai/c/d8b1e4ed-58fc-487d-9022-1ba31b64f7aa
**Wall-clock generation time:** ~27–28 minutes (thinking + answer), well inside the 40-minute poll budget.

**Prompt given to Qwen:** the full solver prompt (conjecture statement, definitions, Fact 2 /
Lemma 1 / Lemma 3 / Corollary B1 with proof / Theorem C statement, all four named obstacles
O1–O4 from `notes/proofs/wowii61_draft.md` §6, the false-SC1 counterexample note, and the boxed
diameter-4 dichotomy) — reproduced verbatim as sent at
`/private/tmp/claude-501/-Users-user-workspace-claudecode-automath/af393f24-af91-41e1-860b-6357fcc741d7/scratchpad/qwen_prompt.txt`.
Target statement: for every connected `G` with `diam(G) = 4`, either `f(G) ≥ α(G) + 2` or
`residue(G) ≤ α(G) − 1`.

**Outcome class: PARTIAL.** No full proof, no counterexample. Qwen produced a genuine new
partial result: a clean reduction plus two fully-proved sub-cases (vertex-cover number ≤ 2, and
all forests), with the exact remaining hard core stated precisely.

---

## Verbatim response (harvested via the in-page "copy" button → clipboard → file, so LaTeX
source is preserved exactly as Qwen produced it; math delimiters are `\[ \]` / `\( \)`)

I have not found a complete proof of the full diameter-4 dichotomy, nor a counterexample. What I can give is a rigorous reduction that closes several nontrivial subclasses and isolates the exact remaining hard core. The proof below is fully checkable for the subclasses it claims; the remaining case is explicitly identified.

---

## 1. Notation and the hard case

Write

\[
\tau(G):=|V(G)|-\alpha(G)
\]

for the minimum vertex-cover number. Since Fact 2 gives

\[
\operatorname{residue}(G)\le \alpha(G),
\]

the boxed dichotomy at diameter \(4\) is equivalent to:

> If \(G\) is connected, \(\operatorname{diam}(G)=4\), and
> \[
> f(G)=\alpha(G)+1,
> \]
> then
> \[
> \operatorname{residue}(G)\le \alpha(G)-1.
> \]

Indeed, if \(f(G)\ge \alpha(G)+2\), the first disjunct holds. So the only possible danger is the "tight forest" case \(f=\alpha+1\). In that case

\[
\nabla(G)=|V|-f(G)=|V|-\alpha(G)-1=\tau(G)-1.
\]

Thus a graph in the hard case has decycling number exactly one less than its vertex-cover number.

---

## 2. A local obstruction lemma for the tight forest case

### Lemma 4 (pair obstruction when \(f=\alpha+1\))

Let \(G\) be any graph, let \(A\) be a maximum independent set, and put \(B=V(G)\setminus A\). If

\[
f(G)=\alpha(G)+1,
\]

then for every two distinct vertices \(u,v\in B\):

1. if \(uv\in E(G)\), then
   \[
   N_A(u)\cap N_A(v)\neq\varnothing;
   \]

2. if \(uv\notin E(G)\), then
   \[
   |N_A(u)\cap N_A(v)|\ge 2.
   \]

Here \(N_A(x)=N(x)\cap A\).

#### Proof

Consider the induced subgraph

\[
H:=G[A\cup\{u,v\}].
\]

Since \(A\) is independent, every edge of \(H\) is incident with \(u\) or \(v\).

- If \(uv\notin E(H)\), then the only possible cycle in \(H\) is a 4-cycle

  \[
  u-a-v-b-u
  \]

  with distinct \(a,b\in A\), i.e. two distinct common neighbours of \(u\) and \(v\) in \(A\). Hence \(H\) is a forest iff

  \[
  |N_A(u)\cap N_A(v)|\le 1.
  \]

- If \(uv\in E(H)\), then the only possible cycle is a triangle

  \[
  u-v-a-u
  \]

  with \(a\in A\) a common neighbour of \(u\) and \(v\). Hence \(H\) is a forest iff

  \[
  N_A(u)\cap N_A(v)=\varnothing.
  \]

If either of the claimed conditions failed, then \(H\) would be an induced forest on

\[
|A|+2=\alpha(G)+2
\]

vertices, contradicting \(f(G)=\alpha(G)+1\). ∎

---

## 3. Structure of a diametral path in the hard case

### Lemma 5 (forced pattern on every diametral path)

Assume

- \(G\) is connected,
- \(\operatorname{diam}(G)=4\),
- \(f(G)=\alpha(G)+1\).

Let

\[
P=v_0v_1v_2v_3v_4
\]

be any shortest path of length \(4\), and let \(A\) be any maximum independent set. Put \(B=V(G)\setminus A\). Then:

1. \(v_0,v_4\in A\);
2. \(v_1,v_3\in B\);
3. \(v_2\in A\) or \(v_2\in B\), and accordingly
   \[
   A\cap V(P)=\{v_0,v_2,v_4\}
   \quad\text{or}\quad
   A\cap V(P)=\{v_0,v_4\};
   \]
4. \(v_1\) and \(v_3\) are nonadjacent and have at least two common neighbours in \(A\).

#### Proof

Because \(P\) is a shortest \(v_0\)-\(v_4\) path, for all \(i<j\),

\[
\operatorname{dist}_G(v_i,v_j)=j-i.
\]

In particular, any two vertices of \(P\) whose indices differ by at least \(3\) are nonadjacent and have no common neighbour in \(G\).

Let

\[
I:=\{i\in\{0,1,2,3,4\}: v_i\in B\}.
\]

Since \(A\) is independent, \(I\) must meet every edge of the path \(P\). Therefore \(I\) contains an index in \(\{0,1\}\) and an index in \(\{3,4\}\).

Now suppose there exist \(i,j\in I\) with \(j-i\ge 3\). Then \(v_i,v_j\in B\), they are nonadjacent, and they have no common neighbour in \(A\). By Lemma 4, this is impossible in the tight forest case \(f=\alpha+1\), because then \(G[A\cup\{v_i,v_j\}]\) would be an induced forest on \(\alpha+2\) vertices.

Thus all elements of \(I\) lie in an interval of length at most \(2\). Since \(I\) must meet both \(\{0,1\}\) and \(\{3,4\}\), the only possibility is

\[
1,3\in I,
\]

and

\[
0,4\notin I.
\]

Thus

\[
v_1,v_3\in B,\qquad v_0,v_4\in A.
\]

The middle vertex \(v_2\) may lie in \(A\) or in \(B\), giving exactly the two stated possibilities.

Finally, \(v_1\) and \(v_3\) are nonadjacent: if \(v_1v_3\) were an edge, then

\[
v_0v_1v_3v_4
\]

would be a \(v_0\)-\(v_4\) path of length \(3\), contradicting that \(P\) is diametral of length \(4\). Since \(v_1,v_3\in B\) are nonadjacent, Lemma 4 gives

\[
|N_A(v_1)\cap N_A(v_3)|\ge 2.
\]

∎

This lemma is the precise form of the "central obstruction" in the hard case: every diametral path must look like

\[
A\;-\;B\;-\;(A\text{ or }B)\;-\;B\;-\;A,
\]

and the two \(B\)-vertices at distance \(2\) along the path must be blocked from being added to \(A\) by at least two common neighbours in \(A\).

---

## 4. The dichotomy is true when \(\tau(G)\le 2\)

### Theorem 6 (vertex-cover number at most \(2\))

Let \(G\) be connected with \(\operatorname{diam}(G)=4\). If

\[
\tau(G)\le 2,
\]

then the diameter-4 dichotomy holds:

\[
f(G)\ge \alpha(G)+2
\quad\text{or}\quad
\operatorname{residue}(G)\le \alpha(G)-1.
\]

#### Proof

If \(f(G)\ge \alpha(G)+2\), there is nothing to prove. Assume therefore that

\[
f(G)=\alpha(G)+1.
\]

We must show

\[
\operatorname{residue}(G)\le \alpha(G)-1.
\]

The case \(\tau=1\) is impossible. Indeed, a connected graph with vertex-cover number \(1\) is a star \(K_{1,t}\), whose diameter is at most \(2\).

So assume \(\tau=2\). Let \(A\) be a maximum independent set and let

\[
B=V(G)\setminus A=\{x,y\}.
\]

Thus \(|A|=\alpha\) and \(n=\alpha+2\).

Because \(B\) is a vertex cover, every edge is incident with \(x\) or \(y\). First, \(xy\notin E(G)\). If \(xy\in E(G)\), then every vertex of \(A\) is adjacent to some subset of \(\{x,y\}\), and any two vertices of the graph are at distance at most \(3\): two vertices of \(A\) with disjoint neighbourhoods in \(\{x,y\}\) are connected by a path of length \(3\) through the edge \(xy\), and all other pairs are at distance at most \(2\). Hence \(\operatorname{diam}(G)\le 3\), contradiction. Thus

\[
xy\notin E(G).
\]

Partition \(A\) as follows:

- \(A_x\): vertices adjacent to \(x\) but not to \(y\);
- \(A_y\): vertices adjacent to \(y\) but not to \(x\);
- \(A_c\): vertices adjacent to both \(x\) and \(y\).

Connectedness and diameter \(4\) force

\[
|A_x|\ge 1,\qquad |A_y|\ge 1.
\]

Indeed, a distance-4 path between two vertices of \(A\) in a graph whose vertex cover is \(\{x,y\}\) and in which \(xy\notin E\) must have the form

\[
a-x-c-y-b
\]

with \(a\in A_x\), \(b\in A_y\), and \(c\in A_c\).

Also, by Lemma 4 applied to the nonedge \(xy\), we have

\[
|A_c|=|N_A(x)\cap N_A(y)|\ge 2.
\]

Write

\[
a:=|A_x|,\qquad b:=|A_y|,\qquad c:=|A_c|.
\]

Then

\[
a\ge 1,\qquad b\ge 1,\qquad c\ge 2,
\]

and

\[
\alpha=a+b+c.
\]

The degree sequence is explicit:

- \(\deg(x)=a+c\);
- \(\deg(y)=b+c\);
- each vertex of \(A_c\) has degree \(2\);
- each vertex of \(A_x\cup A_y\) has degree \(1\).

The number of edges is

\[
m=a+b+2c.
\]

Assume for contradiction that

\[
\operatorname{residue}(G)=\alpha.
\]

Since \(n=\alpha+2\), Lemma 1 implies that the Havel–Hakimi process would terminate in exactly

\[
s=n-\operatorname{residue}(G)=2
\]

steps.

Let the two Havel–Hakimi heads be \(D_1,D_2\). By Lemma 1,

\[
D_1+D_2=m=a+b+2c.
\]

Without loss of generality, suppose

\[
a+c\ge b+c.
\]

Then the maximum degree is

\[
D_1=\Delta=a+c.
\]

In the first Havel–Hakimi step, we remove one entry of degree \(a+c\) and decrement the next \(a+c\) entries. The other vertex of degree \(b+c\) is certainly among those decremented, because it is the largest remaining entry and \(D_1\ge 1\). Hence after the first step, the largest possible remaining degree is at most

\[
b+c-1.
\]

Therefore

\[
D_2\le b+c-1.
\]

Consequently,

\[
D_1+D_2\le (a+c)+(b+c-1)=a+b+2c-1=m-1,
\]

contradicting Lemma 1, which requires \(D_1+D_2=m\).

Thus the Havel–Hakimi process cannot terminate in \(2\) steps. Hence

\[
s\ge 3,
\]

and therefore

\[
\operatorname{residue}(G)=n-s\le (\alpha+2)-3=\alpha-1.
\]

This proves the dichotomy for \(\tau=2\). ∎

---

## 5. The dichotomy is true for forests

### Theorem 7 (forest case)

If \(G\) is a connected forest with \(\operatorname{diam}(G)=4\), then

\[
f(G)\ge \alpha(G)+2.
\]

#### Proof

For a forest,

\[
f(G)=|V(G)|=n.
\]

A connected forest has vertex-cover number \(1\) exactly when it is a star \(K_{1,t}\), whose diameter is at most \(2\). Since \(\operatorname{diam}(G)=4\), we have

\[
\tau(G)\ge 2.
\]

Thus

\[
\alpha(G)=n-\tau(G)\le n-2,
\]

and therefore

\[
f(G)=n\ge \alpha(G)+2.
\]

∎

---

## 6. Exact remaining hard core

Combining the previous results, the only graphs not yet covered by the diameter-4 dichotomy are those satisfying all of the following:

1. \(G\) is connected;
2. \(\operatorname{diam}(G)=4\);
3. \(f(G)=\alpha(G)+1\);
4. \(\operatorname{residue}(G)=\alpha(G)\);
5. \(\tau(G)=|V(G)|-\alpha(G)\ge 3\);
6. \(G\) is not a forest.

For every such graph, Lemma 5 applies. In particular, for every maximum independent set \(A\) and every diametral path

\[
v_0v_1v_2v_3v_4,
\]

we have

\[
v_0,v_4\in A,\qquad v_1,v_3\in B:=V\setminus A,
\]

and \(v_1,v_3\) are nonadjacent with at least two common neighbours in \(A\).

Equivalently, the remaining problem is:

> Prove that no connected non-forest graph with \(\tau\ge 3\), diameter \(4\), and \(f=\alpha+1\) can have \(\operatorname{residue}=\alpha\).

The mechanism that proves the \(\tau=2\) case is that diameter \(4\) forces a nonedge pair in the vertex cover with private neighbours, and that makes two-step Havel–Hakimi termination impossible. For \(\tau\ge 3\), the analogous obstruction appears to require controlling how the Havel–Hakimi heads interact with several simultaneous common-neighbour obstructions among pairs in \(B\). I have not been able to turn this into a complete proof.

---

## 7. Why this does not yet settle the full dichotomy

The unresolved case is genuinely joint in the sense of Obstacle O1:

- One cannot simply prove \(f\ge \alpha+2\) for all diameter-4 graphs, because witnesses such as W1 have \(f=\alpha+1\).
- One cannot simply prove \(\operatorname{residue}\le \alpha-1\) for all diameter-4 graphs, because trees such as W2 have \(\operatorname{residue}=\alpha\) but compensate with \(f\) much larger than \(\alpha+1\).

The remaining hard case is exactly the intersection:

\[
f=\alpha+1
\quad\text{and}\quad
\operatorname{residue}=\alpha.
\]

The structural path lemma above shows what such a graph must look like locally on every diametral path, but it does not yet force the extra Havel–Hakimi step when \(\tau\ge 3\).

VERDICT: PARTIAL

- **Rigorously proved:** Lemma 4 (pair obstruction when \(f=\alpha+1\)).
- **Rigorously proved:** Lemma 5 (forced structure of every diametral path in the hard case \(f=\alpha+1\), \(\operatorname{diam}=4\)).
- **Rigorously proved:** The diameter-4 dichotomy for all graphs with vertex-cover number \(\tau\le 2\).
- **Rigorously proved:** The diameter-4 dichotomy for all forests.
- **Not proved:** The full diameter-4 dichotomy for non-forest graphs with \(\tau\ge 3\), \(f=\alpha+1\), and \(\operatorname{residue}=\alpha\).
- **No counterexample found:** All explicit families I constructed in the remaining regime satisfy \(\operatorname{residue}\le \alpha-1\), but I do not have a general proof that this must always happen.

---

## Operator assessment (mine, not Qwen's)

### What checks out as rigorous

- **Lemma 4** is correct and cleanly proved. I re-derived both cases by hand (adjacent `u,v`
  → triangle obstruction; nonadjacent `u,v` → 4-cycle obstruction) and the case analysis is
  exhaustive and airtight: `G[A∪{u,v}]` has edges only incident to `u` or `v` (since `A` is
  independent), so its only possible cycles are the triangle/4-cycle described, and the
  forest-iff conditions follow immediately. Solid.

- **Lemma 5** correctly builds on Lemma 4. I checked the index-gap argument (`I` cannot contain
  two indices differing by ≥3, since that would produce a Lemma-4-violating nonadjacent pair
  with zero common neighbours in `A`) and the forced-interval deduction (`I` must hit `{0,1}`
  and `{3,4}` while having diameter ≤2 as a set, forcing `1,3 ∈ I` and `0,4 ∉ I`) — this is
  correct integer arithmetic, no gaps. The final nonadjacency-of-`v1,v3` argument (an edge
  would create a length-3 `v0`–`v4` walk, contradicting `dist(v0,v4)=4`) is also correct.

- **Theorem 6 (τ ≤ 2 case) is the most valuable new result and I verified it in full.** The
  τ=1 case (star, diam ≤ 2) is trivial and correct. The τ=2 case's degree-counting argument is
  genuinely clever: assuming `residue(G)=α` forces the Havel–Hakimi process to terminate in
  exactly `s=2` steps (via Lemma 1, `residue = n − s`, `n = α+2`), which forces `D1+D2 = m`
  exactly (Lemma 1 part 2). But since `y`'s degree `b+c` is *strictly* the largest of the
  `n−1` remaining entries after removing `x` (because `b≥1, c≥2 ⟹ b+c≥3 > 2` = the next-largest
  possible degree, that of an `A_c` vertex), it is certainly decremented in step 1, giving
  `D2 ≤ b+c−1`, hence `D1+D2 ≤ m−1 < m` — a contradiction. This forces `s≥3`, hence
  `residue ≤ α−1`. I re-derived every inequality in this chain independently and it holds.
  One minor exposition gap: the claim "`|Ax|≥1, |Ay|≥1` forced by diam=4" is asserted via a
  single sentence about the shape of a diametral path without ruling out other diametral-pair
  placements; I independently verified the conclusion by direct case computation (if `Ax=∅`,
  the graph's diameter is at most 3, contradiction) — the claim is correct, just under-argued
  in the transcript.

  **Cross-validation against the draft's own witnesses is strong evidence of correctness:**
  witness W1 (`n=8, α=6, f=7, residue=5`) has `τ=n−α=2` and `f=α+1` — exactly Theorem 6's
  hypothesis — and indeed `residue=5=α−1`, matching the theorem's conclusion exactly (not just
  the inequality direction, the *exact* boundary value). Witness W4 (`n=6, α=4, f=5,
  residue=3`) likewise has `τ=2`, `f=α+1`, and `residue=3=α−1` — again an exact match. Both
  witnesses from the original draft sit precisely on the boundary Theorem 6 predicts, which is
  a strong (though not exhaustive) sanity check that the theorem is correctly stated and proved.

- **Theorem 7 (forest case)** is a two-line correct argument (`f=n` for a forest;
  `τ(forest)≥2` whenever diam>2 since only stars have τ=1; `α=n−τ≤n−2` gives `f=n≥α+2`). Note
  this is not subsumed by Theorem 6 — it covers forests of *any* τ≥2, not just τ≤2, so it is a
  genuine independent extension, not a redundant special case.

### What is NOT established (the honest gap)

- The hard core — non-forest, `τ≥3`, `f=α+1`, `residue=α` — is left completely open. Qwen is
  explicit and honest about this; it did not attempt to paper over the gap with hand-waving.
  No example in this regime was exhibited (proved-covered or otherwise), so it is unclear from
  this transcript alone whether the "no counterexample found in my constructed families" claim
  reflects genuine search effort or just an absence of explicit attempts in the visible answer
  (the intermediate search process was in the "thinking" trace, not reproduced in the final
  answer, so this claim is unverified/unverifiable from the transcript).

### Net verdict on the harvest

This is a legitimate, checkable, non-trivial partial result — worth keeping. It does not close
Conjecture 61, but it strictly shrinks the residual diameter-4 case from "everything" down to
"connected, non-forest, τ(G)≥3, f=α+1, residue=α," and supplies two new reusable lemmas
(Lemma 4's pair-obstruction, Lemma 5's forced diametral-path pattern `A-B-(A|B)-B-A`) that look
like exactly the right tools to attack the τ≥3 case next (the natural next step being to run
the same "Havel–Hakimi must take ≥3 steps" counting argument with 3+ vertices in `B` instead of
2, controlling pairwise common-neighbour obstructions from Lemma 4 among all pairs in `B`, not
just one pair). I recommend feeding Theorem 6 + Theorem 7 + Lemma 4/5 back into
`notes/proofs/wowii61_draft.md` as a genuine update to the state of the art, and using them as
the starting point for a follow-up attack on the τ≥3 hard core.
