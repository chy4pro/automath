# S4 文献查重：WOWII Conjecture 61 / 133 / 291

日期 2026-08-17。目标：核实这三条 Graffiti.pc "Written on the Wall II" 猜想是否真的仍未解决——
不满足于 formal-conjectures 库 `research open` 标签（该标签只反映库维护者认知，可能滞后于
DeLaVina 本人维护的官方状态页）。

## 方法与关键突破

DeLaVina 官方状态页 `cms.dt.uh.edu/faculty/delavinae/research/wowII/all.html` 在本环境中
**HTTPS 端口物理不可达**（TCP 连接超时，非 DNS/证书问题；HTTP 端口正常但 301 重定向到坏掉的
HTTPS），WebFetch 与直连 curl 均失败。绕过方案：Wayback Machine CDX API + 直接下载归档快照
（`web.archive.org` 对该站点有持续抓取历史，包括 **2026-07-26 的近乎实时快照**，比 formal-conjectures
本地克隆的日期还新）。用 `id_` 原始模式绕过 Wayback 回放层的 500 错误，服务器返回 gzip 压缩体，
本地 `gunzip` 解压后得到可读 HTML。

页面格式：每条猜想前有单字符状态标记，紧跟其后的题号是**该标记所属的题号**（如 "O 61." 表示
61 号状态为 O）。通过多个上下文明确的例子（如 289/292/293 号后面直接跟着 "see counterexample"
或写出的反例计算）确认字母含义：
- **T** = Theorem（已证明为真，页面内嵌完整证明）
- **O** = Open（未解决，无任何后续记录）
- **F** = False（已被反例证伪，页面内嵌反例说明）

交叉验证：用 2010-07-17 Wayback 快照（`cms.uhd.edu` 域名下的旧版 all.html/resolvedT.htm）确认
三条猜想在 2010 年时的状态与 2026-07-26 快照对照，看是否有变化。

## 逐条结论

### Conjecture 61 — `f(G) ≥ residue(G) + ⌈diam(G)/3⌉`

- 官方页面原文（2026-07-26 快照）：
  > O
  > 61. If G is a simple connected graph, then f(G) >= res(G)+ CEIL[diam(G)/3]
  > ... Mar 25, 2004.
- 状态 **O（Open）**，自 2004-03-25 登记以来**无任何后续记录**（无反例、无证明引用），
  2010 年快照与 2026-07-26 快照完全一致（逐字比对无变化）。
- 广泛文献检索（"induced forest" + diameter/residue 组合、Favaron-Mahéo-Saclé 1991 引用链、
  近期 arXiv 论文如 2608.01396「三条 Graffiti.pc 归纳树猜想的证明」、TxGraffiti/Optimist 相关综述）
  均未发现任何论文直接证明或证伪此不等式的直径追加项。
- **VERDICT: 确认 OPEN，干净，可以安全攻坚。**

### Conjecture 133 — `path(G) ≥ rad(G) + ⌊l(G)⌋^cC4(G)`

- 官方页面原文（2026-07-26 快照）：
  > O
  > 133. If G is a simple connected graph, then path(G) >= rad(G)+ [average of l (v)]^ c C4
  > ... July 12, 2005.
- 状态 **O（Open）**，自 2005-07-12 登记以来**无任何后续记录**，2010 年与 2026-07-26 快照完全一致。
- 文献检索（"average independence number of neighborhoods" + radius + C4-free 组合）未发现
  相关证明/证伪论文。
- **VERDICT: 确认 OPEN，干净，可以安全攻坚。**

### Conjecture 291 — `γ_t(G) ≤ k + freq(t_min(v))`（n > 2）

- 官方页面原文（2026-07-26 快照，**关键发现**）：
  > F
  > 291. If G is a simple connected graph such that n(G)> 2, then
  > g t (G) <= k + frequency t min (v), where k is the first step in which a zero appears
  > in the Havil-Hakimi process.
  > ... Mar. 1, 2007, **July 23, 2026 Zyad Tamimi, sent a 12-vertex counterexample,
  > g_t(G) = 4, frequency t_min(v) = 1 and k = 2.**
- 状态已从 2010 年的 **O（Open）** 变为 **F（False，已被证伪）**——这个反例是 **2026-07-23**
  才提交给 DeLaVina 并登记的，距今仅 25 天，比 formal-conjectures 本地库快照更新、也比 S1 阶段
  GitHub PR/issue 查重（该查重只覆盖 formal-conjectures 仓库内部活动，覆盖不到直接投给
  DeLaVina 本人的反例投稿）更新。
- 反例数值验证：k + freq(t_min) = 2 + 1 = 3 < 4 = γ_t(G)，严格违反猜想的上界，是有效反例。
  该反例的假设（n>2 的连通图）与本地 Lean 形式化（`hn : 2 < Fintype.card α`）的假设条件完全一致，
  **直接适用**，不存在假设不匹配的空子。
- 提交者 "Zyad Tamimi" 未检索到公开论文/预印本（可能是直接投稿到 DeLaVina 站点的私人交流，
  未经期刊发表），但作为该猜想编号体系的**权威维护者本人**登记的反例，可信度视为高——
  这类站内"送反例"记录是 Graffiti.pc/WOWII 生态的标准更新机制（页面上其余数十条 F 状态
  条目均以同样格式记录）。
- **VERDICT: 已被证伪（disproved），非 OPEN。formal-conjectures 库的 `research open` 标签已过期
  （滞后于官方状态页约 3-4 周）。不应作为证明目标攻坚**——除非改为「形式化这个已知反例」
  的低价值收尾任务（且此反例本身可能很快被移植进 formal-conjectures 库产生冲突 PR）。

## 证据链接

- Wayback CDX API 查询（确认最新可用快照时间线）：
  `http://web.archive.org/cdx/search/cdx?url=cms.dt.uh.edu/faculty/delavinae/research/wowII/all.html&matchType=prefix`
- 2026-07-26 快照（本次核查主证据）：
  https://web.archive.org/web/20260726061534id_/http://cms.dt.uh.edu/faculty/delavinae/research/wowII/all.html
- 2026-07-23 快照存在但 Wayback 回放层报 500（服务器端记录確有更新，内容与 07-26 一致，07-26
  快照文本中已包含 "July 23, 2026 Zyad Tamimi" 的记录，故 07-23 的更新已被 07-26 快照完整捕获）：
  https://web.archive.org/web/20260723161837/http://cms.dt.uh.edu/faculty/delavinae/research/wowII/all.html
- 2010-07-17 基线快照（用于确认 61/133 二十年来无变化）：
  https://web.archive.org/web/20100717162629/http://cms.uhd.edu/faculty/delavinae/research/wowII/all.html
- 佐证：Average Local Independence and the Spanning-Tree Leaf Number（arXiv 2607.24020，
  证明 WOWII Conjecture 2）一文明确提到该论文写作时 DeLaVina 页面 "Last update 7/23/26"，
  与本次发现的 291 号更新日期吻合，独立佐证该页面确实处于活跃维护、且 7/23/26 附近有过一次更新：
  https://arxiv.org/html/2607.24020
- formal-conjectures 本地库对应文件（当前仍标 `research open`，属过期状态）：
  `FormalConjecture61.lean`、`GraphConjecture133.lean`、`GraphConjecture291.lean`

## 对 S1 分诊结论（wowii_triage.md）的修正

原推荐排序「61 > 133 > 291」——**61、133 排序维持不变（两者查重均确认干净）**，但 **291 应从
候选列表中整体剔除**（已证伪，非"干净的开放猜想"），不再是"第三选"，而是"死亡"。
