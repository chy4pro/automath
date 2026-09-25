# WOWII-133 · Qwen 会话收割（口袋1 r≥3 攻击线）

- 收割时间：2026-08-18 07:00 CDT
- 会话 URL：https://chat.qwen.ai/c/371a3550-ac66-4e8f-98bf-adda7a676292
- 模型：Qwen3.8-Max（页面顶部确认）
- 生成是否已完成：**是**（截图确认：回答末尾操作图标行 copy/thumbs-up/thumbs-down/share/regenerate 已出现，composer 发送按钮为闲置态，非停止方块；任务卡记录的"仍在生成"状态已在本次收割时结束）
- 内容是否完整：**是**（提取自 DOM 的最后一轮用户提示 + 最后一轮助手回答，assistant 回答共 4 轮中的第 4 轮/最新一轮，`.qwen-chat-message-assistant` 计数=4，本文为最后一条；KaTeX 公式已按下方方法从 DOM 提取 LaTeX 源，非纯渲染文本）
- KaTeX 提取方法：页面 KaTeX 构建未使用标准 `<annotation encoding="application/x-tex">`；实测其 `.katex-mathml math` 元素的最后一个子节点是纯文本节点，内容即原始 LaTeX 源（如 `<math>...<mrow>...</mrow>"r\ge 3"</math>`）。用该文本节点替换整个 `.katex` 元素（display 公式替换为 `$$...$$`，inline 替换为 `$...$`），避免了 MathML/HTML 双树重复及阅读顺序错乱问题（对照 notes/web_model_ops.md 中记录的 ChatGPT KaTeX 顺序坑）。
- 裁决声明：**本文件只做收割，不做数学正确性裁决**，Qwen 自评为 PARTIAL（见文末），是否可信/是否可作为下一轮攻击起点由 planner 核定。

---

## 最后一轮 · 用户提示（TASK 指令，四条攻击线原文）

Lemma 6, Lemma 7, Lemma 8, Theorem 4 and Corollary 7 were all verified line by line and accepted. Theorem 4 is the strongest result of this line of work.

One observation from my verification you should exploit: your proof of Theorem 4 never uses the assumption path(G)=4. The contradiction comes purely from (star) + r=2 + existence of a high vertex. So you actually proved the cleaner, stronger THEOREM 4': if G is connected, C4-free, rad(G)=2 and l(G)>=3, then there EXISTS a distance-2 pair with a-values (>=3,>=2) — no path disjunct needed.

Pocket 1 is now reduced to r >= 3. Your Lemmas 6-8 already force any counterexample to be very rigid: every high vertex is a centre; the distance-r sphere around a high vertex is entirely a=1 vertices (leaves or triangle-leaves); internal vertices of geodesics from a high centre have a>=2; and deleting an a=1 vertex preserves distances and preserves l>=3.

TASK: settle r >= 3, in this priority order.

(1) Generalize the counting proof of Theorem 4 to arbitrary r. Layer as L_0={h}, L_1, ..., L_r around a high centre h; you know L_r is all a=1. Try to prove 3n - Sigma > 0 by bounding each layer's contribution. Note the r=2 proof used "unique parent" (two parents would give a C4 with h) — for general r two vertices still share at most one common neighbour, but a vertex of L_i may have several neighbours in L_{i-1}. Work out exactly what C4-freeness gives between consecutive layers and whether the fibre decomposition survives in a weakened form.

(2) Minimal-counterexample reduction via Lemma 8. Take a counterexample minimizing n and delete an a=1 vertex v. Distances among the rest are preserved and l>=3 survives, so G-v is not a counterexample: either path(G-v) >= rad(G-v)+3 or G-v has a distance-rad(G-v) pair of type (>=3,>=2). A long induced path in G-v lifts back to G, so the deletion must lower the radius. Analyse exactly how deleting a leaf or a triangle-leaf can change the radius, and how many times that can happen before the graph runs out of a=1 vertices. This looks like the most promising route.

(3) Note that a counterexample MUST contain a=1 vertices: l>=3 forces a high vertex, and its distance-r sphere is entirely a=1. Make this precise and combine with (2).

(4) If you cannot close it, construct a candidate: C4-free, r>=3, l>=3, all high vertices central, their distance-r spheres all leaves/triangle-leaves, no induced path on r+3 vertices. Even a near-miss with a precise account of which condition fails is valuable.

Full rigor. End with PROVED / DISPROVED / PARTIAL and state exactly what is established.

---

## 最后一轮 · 助手完整回答（原样，LaTeX 已还原为源码）

Thinking completed

Status of the request

I have not been able to prove the full averaging statement for all $r\ge 3$, nor have I found a counterexample. What I can give is a rigorous strengthening of the structural picture for $r\ge 3$, plus a precise minimal-counterexample obstruction coming from deletion of $a=1$ vertices. The radius-$2$ case is completely closed by Theorem $4'$.

I will first restate Theorem $4'$ in its strengthened form, then prove three new structural lemmas for hypothetical counterexamples with $r\ge 3$.

### 1. The radius-$2$ theorem in its strongest form

Theorem 4'. Let $G$ be connected, $C_4$-free, and suppose
$$\operatorname{rad}(G)=2.$$
If
$$l(G)\ge 3,$$
then there exists a pair of vertices at distance exactly $2$ whose $a$-values are $(\ge 3,\ge 2)$ in some order.

This is exactly the theorem already verified. In particular, no path disjunct is needed for $r=2$.

### 2. Assumptions for the remaining $r\ge 3$ analysis

For the rest of this note, suppose for contradiction that $G$ is a counterexample to the averaging statement with radius
$$r\ge 3.$$
Thus: $G$ is connected and $C_4$-free; $\operatorname{rad}(G)=r\ge 3$; $l(G)\ge 3$; there is no pair of vertices at distance exactly $r$ with $a$-values $(\ge 3,\ge 2)$; by Theorem D, $\operatorname{path}(G)\ge r+2$, and since the desired conclusion fails, we must have
$$\operatorname{path}(G)=r+2.$$

We continue to use the lemmas already established: Lemma 6: every vertex with $a\ge 3$ is a centre; Lemma 7: on a geodesic from a high centre to an eccentric vertex, all internal vertices have $a\ge 2$; Lemma 8: deleting an $a=1$ vertex preserves distances among the remaining vertices and preserves $l\ge 3$.

### 3. A high centre has only one deep component

Let $h$ be a high vertex, so $a(h)\ge 3$. By Lemma 6, $h$ is a centre. Consider the graph $G-h$. Its connected components are the branches around $h$.

Lemma 9. In a hypothetical counterexample, for every high centre $h$, all vertices at distance exactly $r$ from $h$ lie in a single connected component of $G-h$.

Proof. Suppose not. Then there are two vertices $x,y$ with
$$\operatorname{dist}(h,x)=\operatorname{dist}(h,y)=r$$
such that $x$ and $y$ lie in distinct connected components of $G-h$. Choose shortest paths
$$P_x=h,x_1,x_2,\ldots,x_r=x$$
and
$$P_y=h,y_1,y_2,\ldots,y_r=y.$$
Because $P_x$ and $P_y$ are geodesics, they are induced paths by Lemma 2. Since $x$ and $y$ lie in different components of $G-h$, there are no edges between
$$\{x_1,\ldots,x_r\}$$
and
$$\{y_1,\ldots,y_r\}.$$
Also, $x_1$ and $y_1$ are not adjacent, because otherwise they would lie in the same component of $G-h$. Therefore the concatenated path
$$x=x_r,x_{r-1},\ldots,x_1,h,y_1,\ldots,y_r=y$$
is induced. It has
$$r+1+r=2r+1$$
vertices. Since $r\ge 3$,
$$2r+1\ge r+3.$$
Thus
$$\operatorname{path}(G)\ge 2r+1\ge r+3,$$
contradicting $\operatorname{path}(G)=r+2$. $\blacksquare$

We call the unique component of $G-h$ containing the distance-$r$ sphere of $h$ the deep component of $h$.

### 4. No high vertex can live in a shallow component

Lemma 10. Let $h$ be a high centre, and let $D$ be the unique deep component of $G-h$ from Lemma 9. If $C$ is any other component of $G-h$, then $C$ contains no vertex $v$ with $a(v)\ge 3$.

Proof. Choose a vertex
$$z\in S_r(h),$$
so $\operatorname{dist}(h,z)=r$. By Lemma 9, $z\in D$. Let $C\ne D$ be another component of $G-h$, and let $v\in C$. Since $C$ and $D$ are distinct components of $G-h$, every path from $v$ to $z$ must pass through $h$. Therefore
$$\operatorname{dist}(v,z)=\operatorname{dist}(v,h)+\operatorname{dist}(h,z).$$
Now $v\ne h$, so $\operatorname{dist}(v,h)\ge 1$. Hence
$$\operatorname{dist}(v,z)\ge 1+r=r+1.$$
If $a(v)\ge 3$, then by Lemma 6, $v$ is a centre, so $\operatorname{ecc}(v)=r$. But then no vertex can be at distance $r+1$ from $v$. This contradicts the inequality above. Thus no vertex in $C$ has $a\ge 3$. $\blacksquare$

So, in any counterexample, all high vertices are confined to the union of a high centre $h$ and its unique deep component.

Corollary 8. If $h$ is a high centre, then every component of $G-h$ other than the deep component contains only vertices with $a\le 2$.

This is a strong restriction. It says that any "extra" neighbourhood components of $h$ which do not lead to the deep branch must be supported entirely by medium and low vertices.

### 5. Why the $r=2$ fibre counting does not immediately generalize

In the proof of Theorem $4'$, with $r=2$, every vertex $b\in L_2$ had a unique parent in $L_1$. This came from the fact that two parents in $L_1=N(h)$ would give two common neighbours of $h$ and $b$, hence a $4$-cycle.

For $r\ge 3$, a vertex $v\in L_i$ may have several neighbours in $L_{i-1}$. Two parents in $L_{i-1}$ no longer automatically share the centre $h$ as a common neighbour, so the unique-parent argument breaks down.

What remains true is the following. If $v\in L_i$ has two distinct parents $u,w\in L_{i-1}$, then $u$ and $w$ have the common neighbour $v$. Since $G$ is $C_4$-free, $u$ and $w$ can have at most one common neighbour. In particular, they cannot also share a parent in $L_{i-2}$. Moreover, if $a(v)=1$ and $v$ has two neighbours $u,w$, then by Lemma 5, those two neighbours must be adjacent. Thus an $a=1$ vertex in the far sphere is either: a leaf, or a triangle-leaf whose two neighbours are adjacent. This is exactly the structure used by Lemma 8.

However, this weaker parent control is not enough to reproduce the exact fibre sum from the $r=2$ case. The fibres over $L_{r-1}$ can overlap through adjacent pairs, and the clean inequality
$$3n-\Sigma=3+m+p+S+3Q>0$$
does not directly generalize.

### 6. Minimal-counterexample deletion analysis

Now suppose $G$ is a counterexample with the minimum possible number of vertices. Because $l(G)\ge 3$, there is a high vertex $h$. By Lemma 6, $h$ is a centre. By Lemma 9 and the fact that $\operatorname{ecc}(h)=r$, there exists a vertex
$$z\in S_r(h)$$
with $a(z)=1$. By Lemma 5, $z$ is either a leaf or a triangle-leaf.

Delete $z$, and write
$$G'=G-z.$$
By Lemma 8: distances between vertices of $G'$ are the same as in $G$; $l(G')\ge 3$; $G'$ is connected.

Let
$$r'=\operatorname{rad}(G').$$
Because distances among old vertices do not increase, we have
$$r'\le r.$$
Also, deleting one $a=1$ vertex can lower the radius by at most one. For completeness, here is the proof.

Lemma 11. Let $z$ be an $a=1$ vertex. Then
$$\operatorname{rad}(G-z)\ge \operatorname{rad}(G)-1.$$

Proof. Let $r=\operatorname{rad}(G)$, and let $G'=G-z$. Suppose $c$ is a centre of $G'$, so
$$\operatorname{ecc}_{G'}(c)=r'.$$
If $z$ is a leaf with neighbour $w$, then
$$\operatorname{dist}_G(c,z)=\operatorname{dist}_{G'}(c,w)+1\le r'+1.$$
Therefore
$$\operatorname{ecc}_G(c)\le r'+1.$$
Hence
$$r\le r'+1,$$
so $r'\ge r-1$.

If $z$ is a triangle-leaf with adjacent neighbours $u,w$, then
$$\operatorname{dist}_G(c,z)=\min\{\operatorname{dist}_{G'}(c,u),\operatorname{dist}_{G'}(c,w)\}+1\le r'+1.$$
Again,
$$\operatorname{ecc}_G(c)\le r'+1,$$
so $r'\ge r-1$. $\blacksquare$

Thus in the minimal counterexample,
$$r'\in\{r-1,r\}.$$
If $r'=r$, then $G'$ is a smaller connected $C_4$-free graph with radius $r$, with $l(G')\ge 3$, and with no distance-$r$ pair of type $(\ge 3,\ge 2)$, because distances among remaining vertices are unchanged. Also
$$\operatorname{path}(G')\le \operatorname{path}(G)=r+2.$$
Thus $G'$ would also be a counterexample, contradicting minimality.

Therefore, in a minimal counterexample, deleting any such far $a=1$ vertex must lower the radius:
$$r'=r-1.$$
This is a severe restriction.

### 7. Exact radius-increase condition for adding an $a=1$ vertex

The previous paragraph can be rephrased positively: adding the deleted vertex $z$ to $G'$ raises the radius by exactly one. We can characterize when that happens.

Lemma 12. Let $G'$ be connected with radius $\rho$. Form $G$ by adding an $a=1$ vertex $z$.

Case 1: $z$ is a leaf adjacent to $w$. Then
$$\operatorname{rad}(G)=\rho+1$$
if and only if every centre $c$ of $G'$ satisfies
$$\operatorname{dist}_{G'}(c,w)=\rho.$$

Case 2: $z$ is a triangle-leaf with adjacent neighbours $u,w$. Then
$$\operatorname{rad}(G)=\rho+1$$
if and only if every centre $c$ of $G'$ satisfies
$$\min\{\operatorname{dist}_{G'}(c,u),\operatorname{dist}_{G'}(c,w)\}=\rho.$$

Proof. Leaf case. Let $z$ be a leaf adjacent to $w$. For any vertex $x\in V(G')$,
$$\operatorname{ecc}_G(x)=\max\left(\operatorname{ecc}_{G'}(x),\operatorname{dist}_{G'}(x,w)+1\right).$$
Also,
$$\operatorname{ecc}_G(z)=\operatorname{ecc}_{G'}(w)+1.$$
Suppose some centre $c$ of $G'$ satisfies
$$\operatorname{dist}_{G'}(c,w)\le \rho-1.$$
Then
$$\operatorname{ecc}_G(c)=\max(\rho,\operatorname{dist}_{G'}(c,w)+1)\le \rho.$$
Since adding a leaf cannot create a vertex of eccentricity below $\rho$, this gives
$$\operatorname{rad}(G)=\rho.$$
Conversely, suppose every centre $c$ of $G'$ satisfies
$$\operatorname{dist}_{G'}(c,w)=\rho.$$
Then for every centre $c$,
$$\operatorname{ecc}_G(c)=\rho+1.$$
If $x$ is not a centre of $G'$, then
$$\operatorname{ecc}_{G'}(x)\ge \rho+1,$$
so also
$$\operatorname{ecc}_G(x)\ge \rho+1.$$
Finally,
$$\operatorname{ecc}_G(z)=\operatorname{ecc}_{G'}(w)+1\ge \rho+1.$$
Thus every vertex of $G$ has eccentricity at least $\rho+1$, and some vertex has eccentricity exactly $\rho+1$. Hence
$$\operatorname{rad}(G)=\rho+1.$$

Triangle-leaf case. Now suppose $z$ has adjacent neighbours $u,w$. For $x\in V(G')$,
$$\operatorname{dist}_G(x,z)=\min\{\operatorname{dist}_{G'}(x,u),\operatorname{dist}_{G'}(x,w)\}+1.$$
Thus
$$\operatorname{ecc}_G(x)=\max\left(\operatorname{ecc}_{G'}(x),\min\{\operatorname{dist}_{G'}(x,u),\operatorname{dist}_{G'}(x,w)\}+1\right).$$
If some centre $c$ of $G'$ satisfies
$$\min\{\operatorname{dist}_{G'}(c,u),\operatorname{dist}_{G'}(c,w)\}\le \rho-1,$$
then
$$\operatorname{ecc}_G(c)\le \rho,$$
so $\operatorname{rad}(G)=\rho$. Conversely, if every centre $c$ of $G'$ satisfies
$$\min\{\operatorname{dist}_{G'}(c,u),\operatorname{dist}_{G'}(c,w)\}=\rho,$$
then every centre of $G'$ has eccentricity $\rho+1$ in $G$. Non-centres of $G'$ already have eccentricity at least $\rho+1$ in $G'$, and $z$ itself has eccentricity at least $\rho+1$ because it is at distance $\rho+1$ from any centre of $G'$. Therefore
$$\operatorname{rad}(G)=\rho+1.$$
$\blacksquare$

### 8. Consequence for a minimal counterexample

Combine Lemmas 8, 11, and 12. Let $G$ be a minimal counterexample with radius $r\ge 3$. Choose a high centre $h$, and choose
$$z\in S_r(h)$$
with $a(z)=1$. Let $G'=G-z$. Then: $\operatorname{rad}(G')=r-1$; $l(G')\ge 3$; distances among vertices of $G'$ are the same as in $G$; adding $z$ raises the radius from $r-1$ to $r$.

Therefore, by Lemma 12: if $z$ is a leaf with neighbour $w$, then every centre of $G'$ is at distance $r-1$ from $w$; if $z$ is a triangle-leaf with adjacent neighbours $u,w$, then every centre of $G'$ is at distance $r-1$ from both $u$ and $w$.

In particular, the support vertex or vertices of every such far $a=1$ vertex are peripheral for every centre of the smaller graph $G'$. This is the exact obstruction that any minimal counterexample must satisfy.

### 9. What remains open for $r\ge 3$

The above results reduce a hypothetical counterexample to the following rigid situation. There exists a high centre $h$. Around $h$: all vertices at distance $r$ from $h$ have $a=1$; all those vertices lie in a single deep component of $G-h$; every other component of $G-h$ contains only vertices with $a\le 2$; every geodesic from $h$ to a vertex in its distance-$r$ sphere has internal vertices with $a\ge 2$; deleting any such distance-$r$ $a=1$ vertex lowers the radius by exactly one; the support of that deleted vertex is peripheral for every centre of the smaller graph.

What I have not been able to prove is that this configuration necessarily forces
$$\sum_v a(v)<3n,$$
or produces an induced path on $r+3$ vertices.

The difficulty is that, for $r\ge 3$, the clean unique-parent fibre decomposition from the $r=2$ case fails. Vertices in intermediate layers may have several parents, and the deep component may contain enough medium/high structure to keep $l\ge 3$ without obviously creating a distance-$r$ $(\ge 3,\ge 2)$ pair.

### 10. No counterexample constructed

I did not construct a graph satisfying all of the above conditions. In particular: for $r=2$, Theorem $4'$ proves that no counterexample exists; for $r\ge 3$, any counterexample must satisfy the very restrictive structural and deletion conditions above.

A candidate counterexample would need: a high central core with enough surplus $\sum(a-2)$ to keep $l\ge 3$; all high vertices central; all distance-$r$ spheres of high vertices consisting only of leaves or triangle-leaves; no induced path on $r+3$ vertices; and every far $a=1$ vertex radius-critical in the precise sense of Lemma 12. I do not currently have such a construction.

### OPEN AVERAGING STATEMENT FOR $r\ge 3$: PARTIAL

Exactly what is established:
- Theorem 4' remains the complete radius-$2$ result. If $\operatorname{rad}(G)=2$ and $l(G)\ge 3$, then a distance-$2$ pair of type $(\ge 3,\ge 2)$ exists.
- Lemma 9 proved. In any hypothetical counterexample with $r\ge 3$, for every high centre $h$, all vertices at distance $r$ from $h$ lie in a single component of $G-h$.
- Lemma 10 proved. In any hypothetical counterexample, every component of $G-h$ other than that unique deep component contains only vertices with $a\le 2$. In particular, no high vertex can lie in a shallow component.
- Lemma 11 proved. Deleting an $a=1$ vertex can reduce the radius by at most one.
- Lemma 12 proved. The exact condition under which adding a leaf or triangle-leaf raises the radius by one is characterized.
- Minimal-counterexample obstruction proved. In a minimal counterexample, deleting any far $a=1$ vertex from the sphere of a high centre must reduce the radius from $r$ to $r-1$, and its support vertex/vertices must be peripheral for every centre of the smaller graph.

Not established:
- The full averaging statement for $r\ge 3$.
- A counterexample for $r\ge 3$.
- A generalized fibre-counting proof for arbitrary $r$.

---
## owner-w133 核验戳（2026-08-18，opus）

逐行核验完成。**Lemma 9 / 10 / 11 / 12 与 §6 极小反例推理全部 VALID，无假证明。**
Theorem 4′ 为 draft §11 Theorem G7 的 root 补注之重述，非新增。
所有新条目均为条件性结构结论（前提含"反例且 path=r+2"），不关闭任何缺口；
Qwen 自评 PARTIAL 属实。已采纳入 `notes/proofs/wowii133_draft.md` §12.0 表格。

**但主攻方向已被证伪**：本任务书攻击线 (1)（把 Theorem 4′ 的纤维计数推广到 r ≥ 3，
即证 "(★) ∧ r≥3 ∧ 存在高顶点 ⟹ 3n−Σ>0"）为**假**——反例见 draft §12.4
（Hoffman–Singleton 每点挂 2 片叶：C4-free、rad=3、⌊l⌋=3、0 个好对、3n−Σ=−100）。
后续对 Qwen 续问务必避开该路线。按"同源不自审"，§12 结论不得送回 Qwen 审。
