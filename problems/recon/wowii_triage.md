# S0/S1 分诊：formal-conjectures 库中 WOWII 已形式化开放条目

日期 2026-08-17。来源：本地克隆 `problems/formal-conjectures/FormalConjectures/WrittenOnTheWallII/`（50 个 .lean 文件，
`@[category research open]` vs `research solved` 标签精确区分状态）+ GitHub `google-deepmind/formal-conjectures`
Search API 查重（commit 历史 + 全部 open PR/issue 标题体检索，非 WebSearch，因为该库本身在 GitHub 上、直接查 API 比搜索引擎更准）。

---

## 0. 结论先行

本地标记 `research open` 的 WOWII 条目恰好 **10 条**（与情报吻合），文件列表：
`GraphConjecture{19,40,61,100,133,141,160,198a,291,314}.lean`。

**关键发现（查重）：GitHub 上游已有 6 条存在"标记为已解决"的 open PR，尚未合并到本地快照，但数学上基本已死**：
19、100、141、160、198a、314。继续攻这些条目 = 大概率重复造轮子。真正"干净"（无任何 solve
尝试痕迹）的只剩 **61、133、291** 三条；**40** 有第三方 40% 进度的预印本（归约到 2 条待证引理 + 穷举验证到
n≤11），处于"半死不活、可捡漏但要读别人的证明"状态。

**推荐首攻：Conjecture 61 > Conjecture 133 > Conjecture 291**（理由见 §3）。

---

## 1. 逐条表格

| 编号 | 陈述（翻译） | 类型 | 攻击路线 | 难度预估 | 查重状态 |
|---|---|---|---|---|---|
| **19** | 连通图 `G`：最大诱导二部子图规模 `b(G) ≥ ⌊avg_v ecc(v) + max_v l(v)⌋`（`ecc`=离心率，`l(v)`=顶点邻域独立数） | 不等式型（下界，∀图） | — | 中 | **已死**：PR [#4559](https://github.com/google-deepmind/formal-conjectures/pull/4559)（akakabrian，7-23）声称完整证明（因过长而外链托管），等待合并 |
| **40** | 非平凡连通图：最大诱导森林规模 `f(G) ≥ ⌈(p(G)+b(G)+1)/2⌉`（`p`=路覆盖数，`b`=最大诱导二部子图规模） | 不等式型（下界，∀图） | 第三方预印本（cozuya，DOI 10.5281/zenodo.21778700）已证明等价于 `ℓ+o ≥ 2τ+1`（脱圈数/奇圈横贯数/生成线性森林边数的重述），二部情形归约为 2 条待证引理（"广义 Hall 判据"结构已证完），并穷举验证 n≤11（10 亿+图，0 反例）。若接手需先形式化读通预印本 §4 的 2 条引理 | 高（数学上大概率真，但剩余 2 条引理是别人卡住的部分，非平凡） | **半死**：issue [#4702](https://github.com/google-deepmind/formal-conjectures/pull/4702)（cozuya，8-3）留了进度通报，未见后续 solve PR，两条引理仍无人闭合 |
| **61** | 连通图：最大诱导森林规模 `f(G) ≥ residue(G) + ⌈diam(G)/3⌉`（`residue`=Havel-Hakimi 剩余度序列零头数，`diam`=直径） | 不等式型（下界，∀图） | **核心项几乎白给**：Favaron–Mahéo–Saclé (1991) 经典定理 `residue(G) ≤ α(G)`（独立数），而独立集本身就是诱导森林，故 `α(G) ≤ f(G)`——即 `residue(G) ≤ f(G)` 已是文献已知结果；只需再证直径项 `⌈diam/3⌉` 的追加量，可尝试沿最短路径分层构造诱导森林（BFS 层 + 独立集拼接）。小图穷举（n≤10, `#eval`/`decide`）先查是否有反例 | **低-中**（核心项有现成定理打底，最有希望） | **干净**：GitHub 全文/标题检索零命中，无任何 PR/issue 提及 |
| **100** | 连通图：独立数上界 `α(G) ≤ ⌈(max_v l(v) + 0.5·degreeL2Norm(Gᶜ))/2⌉`（`degreeL2Norm`=度序列欧氏范数） | 不等式型（**上界**，∀图，唯一非下界式条目） | — | 中 | **已死**：PR [#4515](https://github.com/google-deepmind/formal-conjectures/pull/4515)（DomTheDeveloper，7-21～8-15 持续更新）已挂完整证明，等待合并 |
| **133** | 连通图：诱导路径规模 `path(G) ≥ rad(G) + ⌊l(G)⌋^{cC4(G)}`（`cC4`=1 当且仅当 `G` 无 C4，指数式古怪写法） | 不等式型（下界，∀图，含条件指数） | **C4 存在时（指数=0）RHS 退化为 `rad(G)+1`**——由圆心到偏心顶点的最短路径本身就是长度 `rad+1` 的诱导路径（最短路无弦），这一半**几乎是免费的**；难点集中在 **C4-free 情形**（RHS=`rad(G)+⌊l(G)⌋`），需要更多结构论证。已用 `Read` 确认 Lean 里 `path G` 语义正确（= 最大诱导路径顶点数，非早期版本误用的"平均距离下取整"那个同名函数，314 文件里的免责声明是历史遗留，当前定义已核实正确） | 中（一半近乎平凡，另一半待攻） | **干净**：仅有历史统计口径修正 PR #4282（已合并，不是证明尝试）；无 solve 痕迹 |
| **141** | 连通图：诱导树规模 `tree(G) ≥ ⌊girth(G)/2⌋ - 1 + max_v l(v)`（`girth`=最短圈长，树为空图取 0） | 不等式型（下界，∀图） | — | 中 | **已死**：PR [#4454](https://github.com/google-deepmind/formal-conjectures/pull/4454)（AlperTheKing，7-18～8-11）声称 141 与 143 均已给出库内完整证明（无 sorry），等待合并 |
| **160** | 连通图：`Ls(G) ≥ max_v l(v) + max_v T(v)·χ_C4(G)`（`Ls`=生成树最大叶子数，`T(v)`=过 v 的三角形数，`χ_C4`=1 当且仅当无 4-圈） | 不等式型（下界，∀图） | — | 中 | **已死**：PR [#4576](https://github.com/google-deepmind/formal-conjectures/pull/4576)（anagnorisis2peripeteia + @vulnix0x4 合作，issue #4569 → PR），已挂完整证明 |
| **198a** | 连通图：若 `b(G) ≤ 2 + avg_ecc(G)`，则 `G` 存在哈密顿路径 | **蕴含型**（充分条件→存在型，非纯不等式） | — | 中（原本适合小图穷举反证：条件可判定 + 哈密顿路径 n≤10 内可判定） | **已死**：PR [#4597](https://github.com/google-deepmind/formal-conjectures/pull/4597)（lukekabbash，7-23）附外部仓库论文 PDF + 完整 Lean 证明链接，等待合并 |
| **291** | `n>2`（本地版本；**上游真实条件仅要求 `Nontrivial`，即 n≥2**，见下）连通图：全支配数 `γ_t(G) ≤ k + freq(t_min(v))`（`k`=Havel-Hakimi 迭代中首次出现零的步数，`freq(t_min)`=达到最小三角形数的顶点数） | 不等式型（**上界**，∀图） | 上界式，适合小图穷举找反例（n≤10：全支配数需要小规模支配集搜索，三角形计数、Havel-Hakimi 模拟均 O(n) 级，可行）；证明路线需理解 `k` 与图连通稀疏度的关系，novel，无现成定理可套，纯 combinatorial | 中-高（无已知定理打底，但可判定，反例搜索性价比高） | **干净**（solve 意义上）：仅有 PR [#4510](https://github.com/google-deepmind/formal-conjectures/pull/4510)（anagnorisis2peripeteia，7-21）指出本地实现的假设过强——本地写的是 `2 < Fintype.card α`，但 WOWII 原文只要求"连通图"，`[Nontrivial α]` 已排除单点图，不该有 `n>2` 限制；该 PR 是**陈述修正**而非解答，**若攻此题应以修正后的 `Nontrivial`（n≥2）版本为目标**，而非本地当前偏弱的 `n>2` 版本，否则即使证出也只是证明了一个比原始猜想弱的命题 |
| **314** | `n>1`、无三角形、且诱导路径规模 `≤4` 的连通图 ⟹ 良好全支配（`IsWellTotallyDominated`） | **蕴含型**（结构条件→性质型） | — | 中（三角形free + 无诱导 P5 的图有已知结构分类文献可能可用） | **已死**：PR [#4455](https://github.com/google-deepmind/formal-conjectures/pull/4455)（glyaea，7-18），标题直接是"标记为已解决"，等待合并 |

---

## 2. 已死清单汇总（不要碰，除非确认上述 PR 被拒绝/撤回）

| 编号 | PR | 作者 | 状态 |
|---|---|---|---|
| 19 | [#4559](https://github.com/google-deepmind/formal-conjectures/pull/4559) | akakabrian | open，外链完整证明 |
| 100 | [#4515](https://github.com/google-deepmind/formal-conjectures/pull/4515) | DomTheDeveloper | open，库内完整证明 |
| 141 | [#4454](https://github.com/google-deepmind/formal-conjectures/pull/4454) | AlperTheKing | open，库内完整证明（连带 143） |
| 160 | [#4576](https://github.com/google-deepmind/formal-conjectures/pull/4576) | anagnorisis2peripeteia | open，库内完整证明 |
| 198a | [#4597](https://github.com/google-deepmind/formal-conjectures/pull/4597) | lukekabbash | open，外链论文+证明 |
| 314 | [#4455](https://github.com/google-deepmind/formal-conjectures/pull/4455) | glyaea | open，标记已解决 |

以上 6 条即使我们独立证出，也只是重复已有工作，不产生增量价值（除非目标是"抢在这些 PR 合并前拿到形式化证明本身"这种时间赛跑，但这不符合终结型立项原则——目标是猜想本身被解决，而不是抢当前 repo 的 PR 归属）。

---

## 3. 推荐首攻 2-3 条及理由

### 首选：Conjecture 61 (`f(G) ≥ residue(G) + ⌈diam(G)/3⌉`)
- **唯一一条核心不等式已有强文献支撑**：`residue(G) ≤ α(G) ≤ f(G)`（Favaron–Mahéo–Saclé 1991 + 独立集⊆诱导森林的平凡观察）。攻坚只需补"直径项"的追加论证，风险面窄、路径清晰。
- 查重完全干净（GitHub 零命中）。
- 类型是纯 ∀图不等式，小图穷举（n≤10）可先几秒验证有无反例，S1 阶段可直接跑一版排除法再转 S2 证明。

### 次选：Conjecture 133 (`path(G) ≥ rad(G) + ⌊l(G)⌋^cC4(G)`)
- **条件分支使问题天然一分为二**：含 C4 时 RHS 退化为 `rad(G)+1`，由"圆心到偏心点最短路即诱导路径"这一初等事实几乎白给；只需专注 C4-free 分支（`RHS=rad(G)+⌊l(G)⌋`）。
- 已核实 Lean 库中 `path` 定义语义正确（最大诱导路径顶点数），排除了 314 文件旁注引发的语义误用担忧，可直接按文档字符串攻。
- 查重干净，唯一历史 PR 是纯陈述修正（已合并入本地版本）。

### 第三选：Conjecture 291（`γ_t(G) ≤ k + freq(t_min(v))`，上界式）
- 是上界型陈述，比下界型更适合"小图反例优先"策略——用 n≤10 暴力穷举全支配数/Havel-Hakimi/三角形计数（均多项式可判定）快速排查是否存在反例，性价比高，废案成本低。
- 无任何文献定理可直接套用（k 与全支配数关系是 ad hoc 组合恒等式），证明路线需要原创构造，难度中高，但正因如此几乎不可能被"抢跑"。
- **重要修正**：攻坚目标应采用 PR #4510 指出的修正版假设（仅 `Nontrivial`/n≥2，去掉本地多余的 `2 < Fintype.card α`），否则证出的是弱化版本，价值打折。

### 备注：Conjecture 40 暂不建议作为首攻
第三方（cozuya）已给出实质性归约（等价形式 + 二部情形归约到 2 条引理 + n≤11 穷举 0 反例），数学上强烈暗示为真，但要"完整解决"仍需啃下预印本 §4 的 2 条开放引理——这是别人已经卡住的部分，非我们从零推导，风险和阅读成本都高于 61/133/291。可作为 S2 阶段的候补/并行观察对象（若后续无人认领这两条引理，可考虑单独立项攻这 2 条引理本身）。

---

## 4. 方法论备注（供 S2 交接）

- 本地 `formal_conjectures` 克隆是 shallow clone（`git log` 仅 1 条 commit），无法用本地 git history 做查重，本次查重全部依赖 GitHub Search API（`api.github.com/search/issues`），注意其**未认证限速 10 req/min**，批量查询需加 sleep。
- 6 条"已死"判定依据 PR **标题**直接含"mark ... solved"或"Prove ... resolves"字样 + body 描述完整证明/外链，均为 `state: open`（未合并），存在极小概率被 maintainer 拒绝（如证明有误）——若后续真要捡漏这 6 条中的某一条，第一步应先查 PR 是否被 close/reject 而非因为 merge 静默消失（其 review 记录、CI 状态需要重新拉取确认）。
- 独立数-诱导森林-residue 三者的链式不等式（`residue ≤ α ≤ f`）对 WOWII 中其他"`f(G) ≥ ...`"形式的条目（例如已解决的 34、40 相关不等式）可能也是通用引理，建议 S2 阶段在 `FormalConjecturesForMathlib` 里检查是否已有 `residue_le_indepNum` 之类的现成引理可直接复用（若没有，证明 61 的过程中产出的这条引理本身也有复用价值）。

## S4 深查重更正（2026-08-17，见 wowii_s4_check.md）
- **291 已死**：DeLaVina 官方状态页 2026-07-26 快照标 "F"——Zyad Tamimi 2026-07-23
  提交 12 顶点反例（γ_t=4 > k+freq=3），直投 DeLaVina、仓库 PR 查重覆盖不到。
  从候选剔除。教训：Graffiti 类猜想查重必须查官方状态页（Wayback 近实时快照），
  不能只查 formal-conjectures 仓库活动。
- 61/133 确认 OPEN（官方页 2004/2005 登记以来无记录，2010 与 2026 快照一致）。
