# 开放性集中复核 — 2026-08-17（S1/S4 文献核查，sonnet）

核查人：sonnet freshness-audit agent。方法：WebSearch + WebFetch + GitHub REST API（curl，
不占 WebSearch 预算）+ 直接抓取 formal-conjectures 仓库源文件/commit 历史。
WebSearch 实际用量 ≈14 次（预算 20）。

---

## 1. A211417 / Bala D(r) 整除猜想 —— 判定：**CONFIRMED-OPEN，但发现高优先级竞速警报**

**图书馆状态（一手核实，非转述）**：直接拉取
`google-deepmind/formal-conjectures` 主分支当前
`FormalConjectures/OEIS/211417.lean`（curl raw file，2026-08-17 现状）：

```
@[category research open, AMS 11]
theorem general_divisibility (r : ℕ) (hr : 1 ≤ r) :
    ∃ D : ℤ, ∀ n : ℕ, (divisorProduct n r) ∣ (D * (a n : ℤ)) := by
  sorry
```

`general_divisibility`（对一切 r≥1 的一般情形）确认仍是 `research open`，未被任何人标记
solved。同文件里已被标 solved 的只有 5 条 **r=1 专属**子命题：`(30n-1)|a(n)`
（AlphaProof Nexus，2605.22763）+ 4 条 k=2,3,5 的 r=1 特例（2026-08-16 由 PR #5010 合并，
证明作者 KitaKen1）。OEIS A211417 页面 Ralf Stephan 2026-06-30 评论同样只认领 r=1
（"The conjecture that (30*n-1) divides a(n) was proved..."）。**这部分与出发前提完全一致。**

**新发现（关键警报）**：formal-conjectures issue **#4923**（"Possible misformalizations
II"，作者 KitaKen1，created 2026-08-13，body 最后编辑于 2026-08-16T00:46:41Z，即在我方
2026-08-17 定稿**之前**）在 `general_divisibility` 条目下写道：

> **Update:** the intended version appears true with the explicit positive witness
> `D(r) = lcm(1,...,r)^|{1 ≤ i ≤ r : gcd(i,30)=1}|`. **The general proof is
> paper-complete but not yet Lean-checked**; the four fixed statements are separate
> in #5010.

即：**KitaKen1（同一位、几天内高产刷了几十个 formal-conjectures 目标的贡献者）声称自己
已经有一般 r 情形的"paper-complete"证明**，只是尚未 Lean 形式化，日期早于我方定稿。
但深挖未发现任何可公开核验的正文：
- KitaKen1/oeis-a211417 仓库（唯一相关代码仓，2026-08-15 建，README 逐字核对）**明确写
  `general_divisibility` "intentionally out of scope"**，理由是当前 FC 陈述因 D 可取 0
  而空洞，并声明"This repository does not count that statement as a solution and does
  not include it as a target"——即该仓库本身**没有**包含一般 r 证明。
- 搜索该用户全部 ~45 个仓库、gists、formal-conjectures fork 的全部分支（含
  `mark-oeis-a211417-divisibility-solved`），均只对应 PR #5010 的 4 条 r=1 特例，无
  "general" 或 "211417-general" 类分支。
- PR #5010（已合并，2026-08-16T08:39:43Z）本身也只标记了 4 条 r=1 特例为 solved，
  不含一般情形。
- 全网 WebSearch 未命中任何公开可读的"KitaKen1 A211417 general divisibility paper"
  文本、预印本或 gist。

**结论**：一般 r 情形在**任何公开可核验来源**中都不构成 ALREADY-KNOWN——KitaKen1 目前只是
在一个 GitHub issue 的自由文本里做了口头声明（witness 公式 `D(r)=lcm(1..r)^m` 看似过于
粗糙/未必正确，我方 v1.1 §3 用的是逐素数分层论证，给出的是更精细的显式 D(r)），且没有
随附任何可审查的证明文本。但这是一个**真实存在、日期早于我方、由同一活跃个人/AI管线
提出**的竞争声明，若其在未来数天内被 Lean 形式化并合并，会直接冲击我方"率先证明一般
情形"的优先权主张。**建议**：论文定稿前务必在正文/查重节明确引用并讨论 issue #4923
（承认存在此并行声明、说明我方方法独立性与更强的显式性），并考虑加速向 arXiv/FC 提交
以锁定时间戳；同时用我方 §3 的方法核实 KitaKen1 的 witness 公式
`D(r)=lcm(1,...,r)^|L_r|` 是否真的对所有 r 成立（这本身是一个几分钟可验证的数值/逻辑
检验，值得立刻做，以防对方证明是对的但比我方弱/或反而比我方更简洁）。

置信度：高（GitHub 一手数据直接核实，非转述）。

---

## 2. WOWII Graffiti 猜想 61 / 133 / 291 —— 判定：**CONFIRMED-OPEN（3/3）**

- formal-conjectures 主分支当前源码逐条核实：`GraphConjecture61.lean`、`133.lean`、
  `291.lean` 均仍是 `@[category research open]`，`:= by sorry`。
- GitHub issue/PR 增量扫描（区别于"08-17 上午"已查过的一次）：61 只出现在 #4688
  （"chore: modulize FormalConjectures/"，纯重构性 chore PR，覆盖全仓库文件，非证明）；
  133 只关联 #4423（misformalization 报告，已 closed，与"χ_{C4}"另一条 WOWII 猜想
  #160 有关，非 133 本身的证明）和 #3820（六月批量新增 22 条 WOWII 猜想的 PR，历史添加
  记录）；291 关联 #4510（"fix: remove extra order hypothesis"，只是修正命题的
  hypothesis 措辞，仍标 open，非证明）。**三者均无新认领/新 PR/新 issue 声称已解决。**
- 同期文献扫描确认 Graffiti.pc/WOWII 生态**确实存在"机器猜想被人类事后单独证明"的活跃
  现象**（如 arXiv:2608.01396 证明 Conjecture 141/142/143；arXiv:2608.04040 证明
  Erdős–Staton 加强的 residue 猜想 [Fajtlowicz 原 WOTW Conjecture 448]；KitaKen1 仓库
  证过 WOWII Conjecture 2/31/217/316），说明这类"文献里可能已证但 FC 不知道"的风险模式
  是真实存在的——但针对 61/133/291 本身，多轮 WebSearch（含
  `"Conjecture 61" residue forest proof`、`"Conjecture 133" OR "Conjecture 291"
  Graffiti.pc proof 2026`）均未命中任何论文/预印本。
- **证据缺口**：DeLaVina 官方状态页
  `http://cms.uhd.edu/faculty/delavinae/research/wowII/open.html`（及备用域名
  `cms.dt.uh.edu`）本次核查中**服务器不可达**（DNS 解析到 216.145.162.15，TCP 443
  connection timeout/refused，WebFetch 与 curl 均失败；wayback machine 也因限流/工具
  限制未能取得存档快照）。这是本次审计**唯一未能一手核实的信源**，之前 formal-conjectures
  文件本身注明"Last update 7/23/26"字样（来自搜索引擎摘要，非本次直接抓取），若该页面
  实际把 61/133/291 标记为已证明，本次核查会漏检。

置信度：中高（GitHub/arXiv 一手核实充分；官方权威页面本次不可达，留一个待复核缺口）。

---

## 3. A63880（powerful core 缺口）—— 判定：**CONFIRMED-OPEN**

- OEIS A063880 页面全量 COMMENTS 一手抓取：最新相关评论仍是 Amiram Eldar 2024-08-31，
  条件式表述"If there are no other primitive terms, then a(n) = 108 * A276378(n)"——
  即"是否存在 108 之外的其它 primitive powerful 项"仍是悬而未决的核心缺口，无任何
  2025/2026 新评论声称已解决。
- 检索到的近期"AI 批量证 OEIS 猜想"论文（Sela Fried 系列第四篇 arXiv:2607.24832，
  57 页，覆盖初等数论/斐波那契/丢番图方程等主题）abstract 未提及 A063880；
  AlphaProof Nexus（44 条 OEIS 猜想已证名单）与本序列无匹配信号。

置信度：高。

---

## 4. ETP finite 677→255 / 命题 (P) —— 判定：**CONFIRMED-OPEN（增量核实：无新变化）**

在今晨已有 `notes/case_intel/etp677_freshness_0817.md` 完整核查的基础上，本次仅做增量：

- `teorth/equational_theories` 最新 commit 仍是 2026-08-14 的 Law43 相关工作；新发现
  **PR #1440**（"Dedicated 677"，作者 Timeroot，2026-05-19 创建，仍为 **draft**，
  2026-08-13 有一次更新但**零评论**，无实质内容变化）——非解决信号，只是长期挂起的草稿
  分支被动 rebase。
- Issue #1464（SAT/DRAT order-10 排除下界，非维护者投稿）状态与今晨扫描一致，无新活动。
- `Grisha-Pochuev/finite-magma-e677-to-e255` 仓库 `pushed_at` 仍是 2026-07-17，**一个月
  无新 push**，与今晨记录一致。
- arXiv 检索（"equational theories" magma finite implication）未见任何新论文，命中的
  权威信源仍是 arXiv:2512.07087（ETP 项目论文本身，"tentatively conjecture false"）。

**无任何一手/二手来源显示命题 (P) 已被解决。** 与今晨 Qwen 扫描、今晨 sonnet freshness
核查结论一致，属于三重独立确认。

置信度：高。

---

## 5. 我方 677 论文两条头牌副产品 —— 判定：**(a) CONFIRMED-OPEN / 无直接重合；
(b) 需要修正措辞——"存在性"部分本身 ALREADY-KNOWN（且我方自己的 R4 侦察已发现并
正确处理），"最小阶=77"部分 CONFIRMED-NOVEL（待续追踪）**

### (a) "偶阶 677-magma ⟹ 16 | n"（2 在 Q(ζ₅) 惯性论证）

- 未找到任何文献把 **677 恒等式本身**（KEY 恒等式，ETP 内部编号，非历史命名公理）的
  偶数阶谱问题作为研究对象——这符合预期，677 是 ETP 随机枚举 magma 律库里的一条，非
  经典对象。
- 唯一在**结构上**平行的文献，是我方团队自己在 `R4_literature_recon.md`（2026-08-16，
  同 campaign 内部产出，本次未重新独立复核但内容详实可信）里已经找到并明确讨论过的：
  Tomáš Nagy, "Non-affine latin quandles of order 2^k"（arXiv:1909.08683）——Latin
  quandle（左自结合+拟群）在 2^k 阶存在非仿射结构当且仅当 k=6 或 k≥8；**677-magma 不是
  Latin quandle**（KEY 恒等式≠左自结合律），R4 报告本身已明确指出这只是"高度平行的启发"
  而非同一定理，不能直接套用。本次外部 WebSearch（"Alexander quandle spectrum even
  order 2 inert cyclotomic Z[zeta_5]"）未命中任何直接匹配文献，确认这条"16|n"的具体
  论证路径（2 在 Q(ζ₅) 中惯性次数导出的谱约束）**目前看不到已发表的对应结果**。
- 判定：CONFIRMED-OPEN / 无重合证据。风险主要在于"结构平行但非同一命题"的边界判断，
  建议论文正文明确注明与 Nagy (2019) 结果的关系（承认平行现象，划清不是同一定理），
  以防审稿人误认为是重新发现。

### (b) 非右消去 677-magma 的存在性 + 最小阶（我方 77）

**重要澄清（非新发现，但需要在论文措辞里显式确认）**：非右消去有限 677-magma 的
**存在性本身早已是"已知"事实** —— ETP 官方 blueprint 第 13 章（
`teorth.github.io/equational_theories/blueprint/677-chapter.html`）**§13.1 标题就是
"A finite non-right-cancellative example"**，显式构造了一个阶 31×16=496 的例子（我方
`R4_literature_recon.md` §0.1 已逐字核对、亲自验证其数论细节无误，日期 2026-08-16）。
**如果论文措辞是"我们首次证明存在非右消去 677-magma"，这是 ALREADY-KNOWN 且需立即改写
——正确的措辞只能是"最小阶记录"。**

好消息是：我方内部记录显示这一点**已经被自己正确处理**，非本次审计新发现的漏洞：
- `R5C_soff_report.md`（2026-08-17）明确写"the blueprint's §13.1 example, order 496,
  was recorded... as 'the only one known anywhere'"，把自己的 order-176 构造定位为
  "new **smallest known**"，而非"首次存在性"。
- `campaign_registry.md` 记录进一步推进到 **order 77**（"77/77 列非单射...三项纪录：
  最小非右消（77<176）..."），同样是"最小阶"框架，且 77<176<496 的链条内部自洽、可核验
  （R5C→R6C 递进关系有 mtime 佐证）。

本次外部核实：多轮 WebSearch（"non-right-cancellative quandle rack left quasigroup
smallest example"）未发现任何 ETP 生态之外的文献给出比 496 更小的例子，也未发现有人
公开给出比我方 77 更小的例子；"左拟群不必右消去"这一**结构事实**本身在 rack/quandle
文献里是标准常识（左拟群定义只要求左可除），不构成任何具体阶数结果的抵触。

判定：(b)-存在性 = ALREADY-KNOWN（但我方已知晓且正确改用"最小阶"措辞，非漏洞，仅提醒
定稿前再次核对全文没有退化回"首次存在性"的表述）；(b)-最小阶 77 = 目前无外部文献能
证伪或抢先，CONFIRMED-OPEN-NOVEL，但因缺乏"77 是否真最小"的独立证明（大概率只是"目前
搜索到的最小"，非最小性证明），论文应明确标注为"目前已知最小构造"而非"最小阶定理"，
除非另有独立的最小性证明。

置信度：高（一手核对了我方自己的内部文档链条，且外部检索一致）。

---

## 汇总表

| # | 目标 | 判定 | 关键证据 |
|---|---|---|---|
| 1 | A211417 general_divisibility (r≥1) | CONFIRMED-OPEN + **竞速警报** | FC 主分支 `research open`；KitaKen1 issue #4923 声称"paper-complete"但无公开文本，日期早于我方 |
| 2 | WOWII 61/133/291 | CONFIRMED-OPEN（3/3） | FC 源码仍 `research open`；无新 PR/issue/arXiv；官方状态页本次不可达（缺口） |
| 3 | A63880 powerful core | CONFIRMED-OPEN | OEIS 评论最新仍是条件式表述，无解决声明 |
| 4 | ETP (P) 677→255 | CONFIRMED-OPEN | 三重独立确认（今晨 Qwen + 今晨 sonnet + 本次增量），PR #1440 仍是零评论 draft |
| 5a | 偶阶⟹16\|n | CONFIRMED-OPEN | 仅与 Nagy(2019) Latin quandle 结果结构平行，非同一命题 |
| 5b | 非右消去存在性 | **ALREADY-KNOWN**（我方已知晓并正确改述为"最小阶"，非漏洞） | ETP blueprint §13.1，order 496，早于本 campaign |
| 5b | 非右消去最小阶=77 | CONFIRMED-OPEN-NOVEL | 无外部文献给出更小例子；建议措辞为"已知最小"而非"证明最小" |
