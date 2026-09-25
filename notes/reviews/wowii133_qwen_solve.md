# WOWII/Graffiti.pc Conjecture 133 — Qwen3.8-Max independent-solver attempt

Date: 2026-08-18 (session start ~03:58 CDT, aborted at wall-clock limit ~04:43 CDT, ≈45 min elapsed).

Model: Qwen3.8-Max (confirmed via the model selector showing "Qwen3.8-Max" with the
checkmark on that option, selected after several flaky-dropdown retries — see notes below),
mode: **Thinking** (confirmed via the mode selector showing a checkmark on "Thinking",
not "Auto"/"Fast"). New tab (tabId 2130629787), new chat (fresh "How can I help you?"
screen navigated from https://chat.qwen.ai/, not a continuation of any prior conversation).
Chat URL after send: `https://chat.qwen.ai/c/371a3550-ac66-4e8f-98bf-adda7a676292`.

**Task role given to Qwen**: independent solver (not reviewer) on the open case of
Conjecture 133 — prove the open `C₄`-free, `⌊l⌋ ≥ 3` branch, or find/strategize a
counterexample, or (failing both) deliver its strongest new rigorously-proved partial
result. Full prompt (structured as: problem statement + definitions, what's already
proven verbatim [Theorem A, Theorem C, Theorem D, Corollary D1, plus E/F for context],
the five named obstacles O1–O5 verbatim, the ask with two suggested attack angles and
the A1/A7 auxiliary claims for reference, and a required final-verdict format) was
composed to a scratch file and pasted into the composer via OS-clipboard `pbcopy` +
`cmd+v` (not typed character-by-character), following the established `notes/web_model_ops.md`
guidance for long multi-paragraph prompts. Verified in the UI: the full ~17.9 KB prompt
landed intact in the blue user-message bubble (spot-checked first/last visible lines
match the source file; no truncation observed).

## Outcome: INCOMPLETE — hit the 50-minute wall-clock budget while Qwen was still thinking

This was **not** a throttling event (no "Capabilities reduced" / rate-limit banner was
ever shown; one transient "Network error, reconnecting..." toast appeared at ~18.5 min
and self-recovered within 30s with no visible loss of progress). Qwen3.8-Max (Thinking)
was still actively generating its internal reasoning trace, with the visible
step-summary line still updating every poll, right up to the last poll before the
task's hard 50-minute wall-clock limit was reached. It never reached the point of
emitting a final answer bubble (the "Thinking completed" collapse + action-icon row that
other captures in this directory use as the completion signal never appeared), so there
is **no answer text to harvest** from this run.

Reasoning-trace step-summary labels observed over the run (collapsed one-line
summaries only — the full reasoning trace itself was not captured, consistent with
prior review captures in this directory), in order, each captured by an independent
poll roughly 90s apart:

1. "I engage deeply with the problem at hand." (send confirmation, ~0 min)
2. "Exploring structural constraints in graphs with limited average degree and cyc..." (~1.5 min)
3. "Refining the boundary conditions for path extensions and vertex counts." (~3 min)
4. "Exploring the structural properties of trees and induced paths within graphs" (~4.5 min)
5. "Exploring the structural limits of C4-free graphs through geometric constructi..." (~6 min)
6. "Analyzing the structural properties of a graph derived from a complete graph's..." (~7.5 min)
7. "Exploring structural lower bounds on induced path length in bipartite graphs w..." (~9 min)
8. "Exploring the relationship between radius and longest path in graph structures" (~10.5 min)
9. "Exploring structural constraints to bound induced path lengths in graphs with li..." (~12 min)
10. "Analyzing the structural constraints and connectivity patterns within the graph." (~13.5 min)
11. "Exploring structural properties of triangle-free and C4-free graphs through de..." (~15 min)
12. [transient network-error toast, self-recovered] (~17.5 min)
13. "Exploring structural relationships between induced paths and potential cycles f..." (~18.5 min)
14. "Exploring structural constraints to extend induced paths in graphs with specifi..." (~20 min)
15. "Exploring the relationship between graph radius and path length through struc..." (~21.5 min)
16. "Exploring the structural properties of STS incidence graphs through distance a..." (~23 min) — notable: exploring Steiner-triple-system incidence graphs as a candidate extremal/counterexample structure
17. "Exploring structural constraints in the graph to identify potential long induced ..." (~24.5 min)
18. "Exploring structural properties of graphs through decomposition and induction." (~26 min)
19. "Exploring structural properties of longest induced paths in graphs" (~28 min)
20. "Exploring deeper structural properties to identify a meaningful and provable re..." (~29.5 min)
21. "Shifting focus to a solid, provable result." (~31 min) — apparent pivot from proof/counterexample search toward a PARTIAL-result deliverable
22. "Exploring structural properties of graphs through degree and path length relati..." (~33 min)
23. "Exploring structural constraints in C4-free graphs with minimum degree at leas..." (~34.5 min)
24. "Exploring the structural constraints of graph radius two through component an..." (~36 min)
25. "Analyzing structural constraints in graph geodesics to identify induced paths." (~45.5 min, last poll before abort)

## My assessment

Nothing rigorous to assess yet — there is no final answer text. Qualitatively, the
trace shows the model working broadly across the territory the prompt mapped out
(degree/radius/path relations, C₄-free structural constraints, geodesics, induction),
touching several of the named obstacle areas (O1's degree/radius framing, O2-adjacent
"complete graph derived" and bipartite-graph explorations, and at step 16 a specific
extremal-design candidate — Steiner triple system incidence graphs — as a possible
sparse/C₄-free counterexample-family candidate, which is a reasonable class to probe
given O1/O2's point that extremal `C₄`-free structures are exactly where any
degree/radius-only argument breaks). Step 21 ("shifting focus to a solid, provable
result") suggests the model itself judged a full proof or counterexample out of reach
within its own budget and pivoted toward assembling a PARTIAL/proved-fragment answer —
consistent with the task's fallback instruction — but that pivot happened only ~19
minutes into a run that was still going at the 45-minute mark, so it is unclear how
far that partial-result synthesis got.

**Given the task's hard ≤50-minute wall-clock limit for the whole session (model
selection took extra time due to a genuinely flaky dropdown — see below — leaving
less runway for the model call itself), I aborted polling without a completed answer.**
No adversarial follow-up turn was possible since there was no first-turn answer to
critique.

## Operational notes for next attempt (flaky-dropdown procedure, confirmed)

- The Qwen3.8-Max model-selector dropdown is genuinely flaky: the trigger button
  requires being clicked, closes/opens inconsistently on the first click, and several
  clicks — both raw-coordinate `computer` clicks and `find`-ref-based clicks — landed on
  the correct visible option (`Qwen3.8-Max`, confirmed via `read_page` returning the
  right accessible name) without the selection actually taking effect (header stayed on
  "Qwen3.7-Plus", checkmark stayed on the old option). The fix that worked: click the
  header trigger, then explicitly **wait ~2s and take a screenshot to confirm the
  dropdown panel is fully opaque/settled (not mid fade-in/out animation)** before
  clicking the target option — a click during the animation transition appears to be
  silently swallowed or misrouted even though the element is visually present and
  `read_page` reports it as interactive. Once opened-and-settled, a plain coordinate
  click on the option row succeeded immediately (header updated to "Qwen3.8-Max",
  checkmark moved). This cost ~6 attempts / several minutes before succeeding — future
  runs should build in the explicit settle-wait from the start rather than discovering
  it by trial and error.
- Thinking mode was already the account default in this session (confirmed via the mode
  selector's checkmark) — no change needed, but it was explicitly verified rather than
  assumed, per the task instructions.
- Clipboard paste (`pbcopy` + `computer` `key` `cmd+v`) worked cleanly on the first try
  for the ~17.9 KB / ~360-line prompt into Qwen's plain `<textarea>` composer — no
  newline/premature-submit issue (that issue is specific to ChatGPT's contenteditable
  editor per `notes/web_model_ops.md`, not observed here on Qwen).
- This run's reasoning time (>45 min and still going) is well beyond the ~12 min median
  noted for Qwen3.8-Max Thinking in prior captures in this directory (see
  `notes/web_model_ops.md`) — this specific prompt (a hard open research-level
  conjecture, not a proof-review task) appears to be substantially harder for the model
  to converge on than the review tasks previously captured, which is plausible given the
  prompt explicitly told it the problem is open and gave it license to run a long,
  exploratory search.

## Status / next steps

- **Tab left open**: tabId **2130629787**, URL
  `https://chat.qwen.ai/c/371a3550-ac66-4e8f-98bf-adda7a676292`, as instructed, so the
  run can be checked on and harvested later without re-sending the prompt.
- To harvest later: reopen this tab (or navigate to the URL above in the existing Chrome
  session), poll until the "Thinking completed" collapse + action-icon row appears (or
  until a "Capabilities reduced"/throttle banner appears, which would instead be an
  abort signal), then capture the final answer bubble verbatim and append it, plus a
  rigor assessment, to this file. If a first answer is captured and claims PROVED, the
  task's adversarial-follow-up step (ask it to re-derive its weakest step in full detail)
  should still be executed as a second turn before treating the result as trustworthy.

---
## 最终回答收割（08-18 05:0x CDT，root 亲自从 tab 2130629787 harvest）

Qwen 自评：PARTIAL。交付内容：

**Lemma 3（双端测地线扩张）**：C4-free 图中，任意长度 d≥2 的测地线 u0…ud，若两端点满足
α(G[N(u0)])≥3 且 α(G[N(ud)])≥3，则存在 d+3 个顶点的诱导路径。
证明骨架：两端各取异分量邻居对 {x1,x2}/{y1,y2}（分量≠含 u1/u(d-1) 的分量）；
端集不相交（d≥3 用捷径矛盾、d=2 用 C4）；四点间非完全二部（否则 x1y1x2y2 成 C4）
→ 存在 x≁y；x 对 P 仅邻 u0（i=2 用 C4、i≥3 用捷径）、y 对称 → x,P,y 诱导。

**Theorem 1**：连通 C4-free 图，path(G) ≥ rad(G) + min{3, μ}，μ := min_v α(G[N(v)])。
（μ=1 用 Thm A；μ=2 先证 rad≥2——支配点存在时所有非支配点 a(v)=1——再用 Thm D；
μ≥3 用 Lemma 3 于中心测地线。）

**Cor 2**：三角形自由+δ≥3 ⟹ path≥rad+3。**Cor 3**：δ≥5（允许三角形）⟹ path≥rad+3
（t(v)≤⌊d/2⌋ ⟹ a(v)≥⌈d/2⌉）。**Cor 4**：⌊l⌋≤3 且 μ≥3 ⟹ C133-b 成立。
**Cor 5**：径向对端点均 μ≥3 ⟹ path≥diam+3。

**root 亲核裁决（逐行）**：Lemma 3 ✅（不相交性、非完全二部、诱导性三步全查，
d=2 特判正确，C4 子图定义（许弦）下论证依然成立）；Theorem 1 ✅（rad≥2 论证含
n≥2 非空性 ✓）；Cor 2/3/4/5 ✅。**全部采纳，Petersen 上紧。**

**残余开放**：⌊l⌋=3 且 μ≤2 且无高-a 径向对；⌊l⌋≥4（仅 n≥14 存在）；A1/A7。
Qwen 会话思考轨迹曾探索 Steiner 三元系入射图作反例候选——未产出但值得记录。

---
## 追击轮收割（08-18 05:5x CDT，root 从 tab 2130629787 亲自 harvest + 亲核）
Qwen 自评：POCKET 1 PARTIAL / POCKET 2 OBSTRUCTED。
交付：Lemma 4（单端扩张 a(u0)≥3 ∧ a(ud)≥2 ⟹ d+3）、Theorem 2（半径版）、
Lemma 5（a=1 分类）、Theorem 3（口袋 1 反例五条结构约束）、
以及口袋 2 的**反例族 T_m 证伪 k 端推广**。
root 裁决：全部成立，已并入 wowii133_draft.md §10（含我对不交性隐含性、
T_m 与猜想不矛盾性的独立验证）。残余唯一缺口=开放平均命题（见 §10 末）。

---
## 三问轮（开放平均命题）（2026-08-18 06:15 CDT，root 从 tab 2130629787 亲自 harvest，逐字未删改）

Follow-up 发送内容：确认 Lemma 4 / Theorem 2 / Theorem 3 / T_m 反驳逐行核验通过，指出
T_m 不与猜想本身矛盾（l→2, ⌊l⌋=2, path=5≥rad+2，只废技术不废命题），并将口袋 1 收窄到
唯一缺口——OPEN AVERAGING STATEMENT（G connected, C4-free, r=rad(G)≥2, l(G)≥3 ⟹
either path(G)≥r+3, or ∃ 距离恰为 r 的一对顶点 a-值为 (≥3,≥2)），附四条攻击结构建议
（(1) 反证+计数不等式界定 H；(2) 高心顶点离心率论证；(3) H 诱导子图半径/直径；
(4) 若命题假则构造见证并声明是否 ⌊l⌋≥3 真反例）。

Qwen 回答逐字如下（从 KaTeX 渲染的 DOM 提取，`$...$`/`$$...$$` 为其原始 LaTeX 源，
非我事后转写）：

> Attack on the Open Averaging Statement
>
> I have not been able to prove the full averaging statement for all $r\ge 2$, but I can prove it completely for $r=2$, and I can prove several strong structural reductions for general $r$. These reductions substantially narrow the possible form of a counterexample.
>
> Throughout, write
>
> $$a(v):=\alpha(G[N(v)]).$$
>
> For $C_4$-free graphs, $G[N(v)]$ is a matching plus isolated vertices, and $a(v)$ is the number of connected components of $G[N(v)]$.
>
> **1. A key structural lemma: high vertices must be centres**
>
> Assume throughout this section that $G$ is connected, $C_4$-free, has radius $r\ge 2$, and satisfies the following "no good pair" condition:
>
> $$(\star)\qquad \text{there is no pair }x,y\text{ with }\operatorname{dist}(x,y)=r \text{ and }\{a(x),a(y)\}\supseteq\{2,3\},$$
>
> i.e. there is no distance-$r$ pair whose $a$-values are $(\ge 3,\ge 2)$ in either order.
>
> **Lemma 6 (high vertices are centres).** Assume $(\star)$. If $h\in V(G)$ satisfies $a(h)\ge 3$, then
>
> $$\operatorname{ecc}(h)=r.$$
>
> In particular, every high vertex is a centre.
>
> *Proof.* Since $r$ is the radius, every vertex has eccentricity at least $r$. Thus $\operatorname{ecc}(h)\ge r$.
> Suppose for contradiction that $\operatorname{ecc}(h)\ge r+1$. Choose a vertex $z$ with $\operatorname{dist}(h,z)=e\ge r+1$, and choose a shortest path $h=p_0,p_1,\ldots,p_e=z$. Consider the vertex $p_r$. It is at distance exactly $r$ from $h$. Because $a(h)\ge 3$ and $(\star)$ holds, we cannot have $a(p_r)\ge 2$. Hence $a(p_r)=1$.
> But $p_r$ has at least the two distinct neighbours $p_{r-1}$ and $p_{r+1}$, because $e\ge r+1$. By Lemma 5, if $a(v)=1$ and $d(v)\ge 2$, then $d(v)=2$ and the two neighbours of $v$ are adjacent. Therefore $p_{r-1}\sim p_{r+1}$.
> But then there is a walk from $h$ to $p_{r+1}$ of length $h=p_0,p_1,\ldots,p_{r-1},p_{r+1}$, which has exactly $r$ edges. This contradicts the fact that the chosen path was a geodesic and therefore $\operatorname{dist}(h,p_{r+1})=r+1$.
> Thus $\operatorname{ecc}(h)\neq r+1,r+2,\ldots$, so $\operatorname{ecc}(h)=r$. ∎
>
> This is a strong restriction: in any counterexample to the averaging statement, every vertex with $a\ge 3$ must be a centre.
>
> **2. Internal vertices on geodesics from high centres are medium**
>
> **Lemma 7.** Assume $(\star)$. Let $h$ be a vertex with $a(h)\ge 3$. By Lemma 6, $h$ is a centre. Let $h=p_0,p_1,\ldots,p_r=z$ be a geodesic from $h$ to an eccentric vertex $z$. Then for every internal vertex $p_i$ with $1\le i\le r-1$,
>
> $$a(p_i)\ge 2.$$
>
> *Proof.* Fix $i\in\{1,\ldots,r-1\}$. The vertex $p_i$ has the two distinct neighbours $p_{i-1}$ and $p_{i+1}$.
> Suppose for contradiction that $a(p_i)=1$. Since $p_i$ has at least two neighbours, Lemma 5 implies that $d(p_i)=2$ and that its two neighbours are adjacent. Hence $p_{i-1}\sim p_{i+1}$.
> But then $h=p_0,p_1,\ldots,p_{i-1},p_{i+1},\ldots,p_r$ would be a $h$-$z$ walk of length $r-1$, contradicting that $p_0\cdots p_r$ is a geodesic of length $r$.
> Therefore $a(p_i)\ge 2$. ∎
>
> Thus in any counterexample, every geodesic from a high centre to its eccentric sphere has the form
>
> $$(\ge 3),\quad \underbrace{(\ge 2),\ldots,(\ge 2)}_{r-1\text{ internal vertices}},\quad (1).$$
>
> This is extremely rigid.
>
> **3. Deleting $a=1$ vertices is distance-preserving**
>
> **Lemma 8.** Let $G$ be $C_4$-free and let $v$ satisfy $a(v)=1$. Then deleting $v$ does not increase distances between remaining vertices. Equivalently, for all $x,y\in V(G)\setminus\{v\}$,
>
> $$\operatorname{dist}_{G-v}(x,y)=\operatorname{dist}_G(x,y).$$
>
> *Proof.* By Lemma 5, either: $d(v)=1$ (leaf); or $d(v)=2$ with the two neighbours of $v$ adjacent (triangle-leaf).
> If $d(v)=1$: no shortest path between two vertices distinct from $v$ can use $v$, since a path entering $v$ must leave through the same neighbour, creating a repeated vertex. Distances among remaining vertices are unchanged.
> If $d(v)=2$, let $N(v)=\{u,w\}$ with $u\sim w$: any walk between remaining vertices using $v$ enters from one of $u,w$ and leaves through the other; the segment $u\text{-}v\text{-}w$ can be replaced by edge $u\text{-}w$, no longer than the original. Distances among remaining vertices are unchanged. ∎
>
> Effect on the average $l$: let $S=\sum_x a(x)$, so $l=S/n$.
> - Leaf case: deleting $v$ removes $a(v)=1$ and also removes one isolated neighbourhood component from its unique neighbour, so $S$ drops by $2$.
> - Triangle-leaf case: deleting $v$ removes $a(v)=1$, but the edge component in each neighbour's neighbourhood becomes an isolated component, so $S$ drops by exactly $1$.
>
> If $l\ge 3$, then after deleting $v$, $l'\ge 3$: leaf case $\frac{S-2}{n-1}\ge 3 \iff S\ge 3n-1$, follows from $S\ge 3n$; triangle-leaf case $\frac{S-1}{n-1}\ge 3 \iff S\ge 3n-2$, again follows from $S\ge 3n$.
>
> Thus $a=1$ vertices can be deleted without destroying $l\ge 3$, and without changing distances among the remaining vertices.
>
> **4. The averaging statement is proved for radius $2$**
>
> **Theorem 4.** Let $G$ be connected, $C_4$-free, with radius $r=2$. If $l(G)\ge 3$, then either $\operatorname{path}(G)\ge 5$ or there exists a pair of vertices at distance exactly $2$ whose $a$-values are $(\ge 3,\ge 2)$ in some order. Equivalently, if $r=2$, the open averaging statement is true.
>
> *Proof.* Assume, for contradiction, that $\operatorname{path}(G)\le 4$ and that there is no distance-$2$ pair of type $(\ge 3,\ge 2)$.
> Since $G$ is connected, $C_4$-free, and has radius $2$, Theorem D gives $\operatorname{path}(G)\ge r+2=4$. Hence $\operatorname{path}(G)=4$.
> We will show that under the no-good-pair assumption one must have $l(G)<3$, contradicting the hypothesis.
> Because $l(G)\ge 3$, there exists at least one vertex $h$ with $a(h)\ge 3$. By Lemma 6, $h$ is a centre. Since $r=2$, its eccentricity is $2$. Let $A:=N(h)$ be the first BFS layer around $h$, and let $B:=V(G)\setminus(\{h\}\cup A)$ be the second BFS layer. Since $h$ has eccentricity $2$, every vertex of $B$ is at distance exactly $2$ from $h$.
> Because there is no distance-$2$ pair of type $(\ge 3,\ge 2)$, and $a(h)\ge 3$, every vertex of $B$ must satisfy $a(b)=1$.
>
> *4.1 Unique parent in $A$.* Let $b\in B$. Since $\operatorname{dist}(h,b)=2$, $b$ has at least one neighbour in $A$. Suppose $b$ had two distinct neighbours $a,a'\in A$. Then $h$ and $b$ would have two common neighbours, namely $a$ and $a'$. In a $C_4$-free graph, two distinct vertices have at most one common neighbour — impossible. Thus every $b\in B$ has a unique parent in $A$, denoted $p(b)$.
>
> *4.2 No edges between different $A$-fibres inside $B$.* For $a\in A$, define its fibre $B_a:=\{b\in B:p(b)=a\}$. Claim: no edges between different fibres. Suppose $b\in B_a$, $b'\in B_{a'}$, $a\ne a'$, and $b\sim b'$. In $N(b)$, we have the two vertices $a$ and $b'$. If $a\sim b'$, then $b'$ would have two parents ($a$ and $a'$), contradicting unique parent. Hence $a\not\sim b'$. Therefore $a$ and $b'$ lie in different connected components of $G[N(b)]$, which implies $a(b)\ge 2$. But every vertex of $B$ has $a=1$ — contradiction. Thus there are no edges between distinct fibres $B_a$ and $B_{a'}$.
>
> *4.3 Structure inside a fibre.* Fix $a\in A$. Since every $b\in B_a$ has $a(b)=1$ and is adjacent to $a$, $N(b)$ has exactly one connected component. If $b$ has a neighbour $b'\in B_a$, then $b'$ is adjacent to $a$, so in $N(b)$ the vertices $a$ and $b'$ are adjacent; since $G[N(b)]$ has max degree $\le 1$, $b$ cannot have two neighbours inside $B_a$. So $G[B_a]$ has max degree $\le 1$: a matching plus isolated vertices. Let $s_a$ = # isolated vertices of $G[B_a]$, $q_a$ = # matching edges inside $B_a$. Then $|B_a|=s_a+2q_a$. Let $S:=\sum_a s_a$, $Q:=\sum_a q_a$, so $|B|=S+2Q$.
>
> *4.4 The matching inside $A$.* Because $G$ is $C_4$-free, $G[A]$ has max degree $\le 1$: a matching plus isolated vertices. Let $m:=|A|$, $p$ = # matching edges in $G[A]$. Then $a(h)=m-p$.
>
> *4.5 Computing $a(a)$ for $a\in A$.* $N(a)$ contains: the centre $h$; possibly one matched neighbour $a'\in A$ (contributing, together with $h\sim a'$, exactly $1$ component either way); the vertices of $B_a$. No edges from $h$ to $B$, none from a matched $a'\in A$ to $B_a$ (else two parents). Therefore $a(a)=1+s_a+q_a$.
>
> *4.6 Summing all $a(v)$.* $\Sigma:=\sum_{v\in V(G)} a(v)$. $a(h)=m-p$. $\sum_{a\in A} a(a)=m+S+Q$. $\sum_{b\in B} a(b)=|B|=S+2Q$. Hence $\Sigma=(m-p)+(m+S+Q)+(S+2Q)=2m-p+2S+3Q$. And $n=1+m+S+2Q$.
> $3n-\Sigma = 3(1+m+S+2Q)-(2m-p+2S+3Q) = 3+m+p+S+3Q \ge 3 > 0$.
> Hence $\Sigma<3n$, so $l(G)=\Sigma/n<3$ — contradicting $l(G)\ge3$.
> Therefore, when $r=2$, if $l(G)\ge 3$, then either $\operatorname{path}(G)\ge 5$ or there is a distance-$2$ pair of type $(\ge 3,\ge 2)$. ∎
>
> **5. Consequence for Pocket 1 at radius $2$**
>
> **Corollary 7.** Let $G$ be connected, $C_4$-free, with $\operatorname{rad}(G)=2$. If $\lfloor l(G)\rfloor=3$, then $\operatorname{path}(G)\ge 5$.
>
> *Proof.* Since $\lfloor l\rfloor=3$, $l\ge 3$. By Theorem 4, either $\operatorname{path}(G)\ge 5$, or a distance-$2$ pair of type $(\ge 3,\ge 2)$ exists; in the second case Lemma 4 gives an induced path on $2+3=5$ vertices. Hence in all cases $\operatorname{path}(G)\ge 5$. ∎
>
> Thus the radius-$2$ part of Pocket 1 is fully closed.
>
> **6. What remains for radius $r\ge 3$**
>
> Assume $G$ is a counterexample: $l(G)\ge 3$, $\operatorname{path}(G)\le r+2$, and no distance-$r$ pair of type $(\ge 3,\ge 2)$. Then: every high vertex is a centre (if $a(h)\ge 3$ then $\operatorname{ecc}(h)=r$); every eccentric sphere of a high vertex consists entirely of $a=1$ vertices; every internal vertex on a geodesic from a high centre to an eccentric vertex has $a\ge 2$; deleting any $a=1$ vertex is distance-preserving and preserves $l\ge 3$, so in a minimal counterexample such deletion must reduce the radius (otherwise minimality would produce a forbidden distance-$r$ pair or a longer induced path). Thus any remaining counterexample must have radius $\ge 3$, built from high centres whose eccentric spheres are entirely leaves/triangle-leaves, all internal geodesic vertices medium, with $l\ge3$ sustained by the high centres without creating a longer induced path or a distance-$r$ $(\ge3,\ge2)$ pair. **"I have not been able to rule out this remaining $r\ge 3$ configuration completely."**
>
> **7. No witness found**
>
> No graph witnessing failure of the averaging statement was constructed. For $r=2$, Theorem 4 proves none exists. For $r\ge 3$ the structural constraints are severe (all high vertices central; all high eccentric spheres only $a=1$; no distance-$r$ contact between high and medium vertices; enough high surplus to keep $l\ge3$ without an induced path of length $r+3$) but **"No construction satisfying all of these is known to me."**
>
> **OPEN AVERAGING STATEMENT: PARTIAL**
>
> Exactly what is established: Lemma 6 proved (under $(\star)$, every $a\ge3$ vertex is a centre); Lemma 7 proved (under $(\star)$, internal geodesic vertices from a high centre have $a\ge2$); Lemma 8 proved (deleting $a=1$ vertex is distance-preserving, preserves $l\ge3$); **Theorem 4 proved: the full averaging statement is true for radius $r=2$**; Corollary 7 proved (the $\lfloor l\rfloor=3$ tier of Conjecture 133-b is closed for radius $2$).
>
> Not established: the averaging statement for arbitrary radius $r\ge 3$; a counterexample to the averaging statement; a complete proof of Pocket 1 for all radii.

**root 待裁决**：Theorem 4（r=2 完整闭合）看起来是本轮最有价值的新增——若逐行核验通过，
口袋 1 的 r=2 层即可完全关闭，与既有 §10 的 Lemma 4/Theorem 2/3 拼接。r≥3 仍开放，
Qwen 自己承认未能排除、也未构造反例。尚未做逐行核验（本轮任务仅为发送追问+收割，
核验留待下一轮）。
