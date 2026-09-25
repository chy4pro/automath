# 未命中反思录

## R1 · 2026-08-16 · 情报滞后 6 周（体系建立当日即触发）
**事实**：初始案例调研依赖 erdosproblems wiki（2026-06-30 停更）等来源，完全漏掉 2026 年 7-8 月的著名猜想浪潮（Jacobian n≥3、Maxwell、DGG、Astra 批次、CDC 声称、和积猜想 ℝ）。今日建立情报体系后首次全谱扫描才补齐。
**定位**：情报源盲区（依赖单一停更源）+ 无定期扫描机制（今日已建）+ **prompt 缺陷**（回补 2026-08-16）：
- 初始调研 prompt 写的是"Survey real, verifiable cases from 2023-2026"，未强制"最近数周优先、显式检索 2026-07/08、多源三角验证、注明各来源的数据截止日"——agent 顺势锚定在 6-30 停更的 wiki，属提示词诱导的锚定偏差；
- 同日另一例：A63880 任务书含我凭印象写的错误"已知成员"（972/1620），被 codex 抓出——prompt 中的"事实"必须先经程序验证再写入。
**修正**：①情报扫描必须多源（arXiv 最新 + X/博客 + Epoch AI + whataifound + Zulip），不得依赖任何单一聚合页；②每工作日增量扫描已入循环；③"WATCH 清单"机制：存疑声称（如 CDC）定期复查，崩塌即抢位；④ **prompt 规范**（新增）：调研类 prompt 必须含"最近 N 周优先+多源+标注来源截止日"条款；任务书中的一切事实断言必须先程序验证或标注 UNVERIFIED；失败反思必须回读原 prompt 逐句审计。
**教益**：AI 数学正以周为单位演进，选题窗口期极短；"别人能不能做"的判断必须基于本周情报而非上月。

## R2 · 2026-08-18 · 双撞车：A114831 与 Fernandes 均被 KitaKen1 抢先（查重盲区=FC 未合并 PR）
**事实**：核查 GitHub 时发现 KitaKen1（Kenta Kitamura）早已解决我方两项"定案成果"：A114831（FC PR #4969，08-15 建、08-16 合入上游标 solved——比我方 batch1 论文编译仅早 26 分钟，但其 PR 早我方项目启动一整天）；Fernandes 猜想（FC PR #4868，08-11 建，kernel-checked 证明公开至今，早我方项目启动 5 天）。我方 08-17 的 openness audit 还把 Fernandes 记为已定案旗舰、对 A211417 只查到 issue #4923 口头声称。
**定位**：查重源盲区——S1/S4 只扫 arXiv/OEIS/网页/FC 已合并状态，**从未查 FC 仓库的未合并 PR**，而这正是 AI 形式化竞赛的主战场；且未建立"竞争者仓库监控"（KitaKen1 有 30+ 专题仓库、仓库名即题号、日产多题，扫一眼即知其战场覆盖）。次因：选题时把"FC category research open"误当"无人在做"。
**修正**：①methodology.md 已加"S1/S4 查重源清单 v2"：`gh pr list --state all --search <题号>`（未合并 PR=公开优先权）+ `gh repo list KitaKen1` 竞争者清单 + 上游文件 category 直读，立项前与定案前各查一遍；②两篇论文已改"独立证明、不主张首证"并重编译；③剩余无人认领成果（A108211/A114362/A100434）立即冲刺上游 PR，天级窗口。
**教益**：竞技场里"合并状态"是滞后指标，"PR 提交时间"才是优先权时钟；对手与我们用同款模型栈（ChatGPT 5.6 sol+Codex），选题重合度会持续走高——快过对手的唯一方式是把"证完→公开"的延迟压到小时级。

## R3 · 2026-08-18 · Anthropic RH 里程碑漏检 7 天（情报源盲区=厂商官方研究频道+主流科技媒体）
**事实**：Anthropic 08-10 研究发布：未发布版 Claude 在 Claude Code 内用 60 subagent、3100 万输出 token、约 36 小时，把 Riemann 临界线零点比例下界从 41.6% 推到 67.2%（此下界 37 年仅前进 0.8pp），并产出 Lean 形式化；明确不宣称证明 RH 本身（技术路线预期不通向完整 RH）。主流科技媒体 08-11/08-12 广泛报道（TechSpot/Neowin/MLQ/TechTimes/theaiinsider）。我方情报体系 08-16 建立、08-17 两度扫描（Sweep2/3），至 08-18 才经 Qwen 扫描附带线索 + planner WebSearch 核实——**漏检 7 天，漏的还是我方主循环模型自家厂商的旗舰数学成果**。
**定位**：①情报源盲区：扫描源清单（arXiv/GitHub/X/Zulip/erdosproblems）缺**厂商官方研究频道**（anthropic.com/research、openai.com/research、DeepMind 博客）与主流科技媒体；②扫描 prompt 锚定"数学社区渠道"，未强制通用新闻检索——prompt 审计维度成立；③对自家厂商动态零监控。
**修正**：①methodology.md 案例情报体系加源清单硬性条款（厂商研究频道+科技媒体每次必查）；②扫描 prompt 模板（T005 系列任务卡）加"vendor research blogs 显式检索"条款；③本案入 cases.md；④立 prompt/编排考古任务——60 subagent+31M token+36h 与我方 CDC 脚手架同族，细节价值极高。
**教益**：漏检频率最高处不在冷门角落而在头条——扫描必须覆盖"最大声的频道"。厂商级编排（60 subagent/31M token）同时证明：我方多 agent 攻坚方向正确，且规模上限远未触及。

## R4 · 2026-08-18（owner-intel 起草，待 planner 背书）· Qwen 背景线索误判：几乎斩断 R3 案例的主源引用链
**事实**：R3 反思已补记 Anthropic RH 案，但 T005 Sweep4（Qwen 驱动）在附带背景线索时误判
arXiv:2608.13637（正是该案的正式论文，署名 Alpöge & Furman，摘要明载"discovered
autonomously by Claude (Anthropic); verified and communicated by the listed authors"）为
"人类数学家独立工作，非 AI 自主解决，不计入案例库"。本回合 owner-intel 做 RH 案深度考古
（直读 anthropic.com/research 四份 PDF 原文：论文/informal note/Claude 自述过程 95pp/
transcript 116pp）时才发现并订正（cases.md 已更新，见 §8 correction note）。因 cases.md
当时已凭二手报道记录该案（R3 之功），本次未造成漏检，但若此线索被采信，会把本案的
唯一 arXiv/GitHub 主源引用链错误标记为"不相关"而永久掐断。
**定位**：Qwen 对"背景参考/顺带提及"类线索的把关明显松于对"声称证明"类内容——R1 教益
（Qwen 假证明需先验证）目前只覆盖数学正确性，未覆盖"这是不是同一个案例"这类元数据/
归属判断；Qwen 似乎只做了"作者是人名"→"独立人类工作"的表面模式匹配，未读摘要的
provenance 从句。
**修正**：①T005/后续扫描 prompt 增加"若判定某新增数据点与已知案例无关，必须给出排除
理由（读摘要 provenance 从句/AI disclosure 段），而非仅凭作者列表"；②案例库归属类判断
（是否为 AI 自主解决 vs 人类工作）与数学正确性判断同等对待，同样需要独立验证而非采信
单一网页模型的一句话结论；③本条待 planner 裁决是否正式采纳（无新增漏检，价值在于流程
补强而非纠错，可视 planner 时间预算决定是否背书或降级为运维笔记）。
**教益**：网页模型的"顺带背景信息"和"核心结论"应受同等怀疑——一次表面模式匹配几乎让
我们弄丢自己案例的主源引用链，纯属复核链条更长这次才被抓住。

> **[planner 背书 08-18]** R4 正式采纳。修正落地：①溯源判断规则已写入 charters/intel.md
> （排除判定必须给出基于摘要 provenance 从句/AI disclosure 段的理由，不得凭作者列表）；
> ②归属类判断与数学正确性判断同等对待、需独立验证——并入同一条款。

## R5 · 2026-08-18（owner-intel 起草，待 planner 背书）· DeepMind AlphaProof Nexus 漏检 ~3 个月

**事实**：DeepMind 官方论文 arXiv:2605.22763（2026-05-21，"Advancing Mathematics Research
with AI-Driven Formal Proof Search"，21 人署名含 George Tsoukalas 等）发布 AlphaProof
Nexus 系统，摘要明确"our most capable agent autonomously resolved 9 of 353 open Erdős
problems...proved 44/492 OEIS conjectures"，另解决 15 年 Hilbert 函数悬案+改进凸优化界，
全部 Lean 4 形式证明公开（github.com/google-deepmind/alphaproof-nexus-results）。这是与
本项目已收录的"2026-01~03 Gemini 半自主 700 题扫射/Aletheia"完全不同的独立系统与事件，
但 cases.md 直到今日（08-18，即发布后 89 天）才首次收录，本回合常规 WebSearch 扫描
（非专项深查，仅例行"DeepMind blog conjecture proof 2026"检索）即命中，说明该案例
早已是搜索引擎易发现的公开信息，此前扫描完全绕过。
**定位**：①源清单缺口——R3 已加"厂商官方研究频道"硬性条款，但历次扫描 prompt 对
DeepMind 一侧的检索词偏窄（多用"Erdős 问题批量""AlphaEvolve"等已知关键词复查，未
对"DeepMind + 新系统名/新论文"做开放式扫描）；②可能存在"批量解题类案例"的分类疲劳——
cases.md 已有多条"批量解决 Erdős/OEIS"记录（Astra 10 项、Erdős 批量 14+、Gemini 700
题扫射），扫描时可能对"又一个批量解题系统"类新闻的搜索优先级隐性降低，属于**认知锚定
而非源清单硬缺口**，与 R1/R3 的"单一源盲区"性质不同，需要新的修正方向。
**修正提案**（供 planner 裁决）：①在 methodology.md 的例行扫描 prompt 中加一条独立子
问题："过去 90 天内，各大厂商研究页/GitHub 组织下是否发布过我们完全未收录的新系统名"
（而非只复查已知系统的后续动态）——把"发现全新系统"与"追踪已知系统新动态"拆成两个
独立检索意图，避免后者挤占前者的检索预算；②本案已顺带发现的信息价值：其
`erdos_problems_attempted.txt`（尝试未必成功）显示 DeepMind 曾尝试我方 TARGETS.md
候选池 #307/#1082 而未列入其 9 个成功案例——建议将"顶级实验室已尝试未列入成功名单"
作为认领 S0 分诊的一个新增负面信号维度（不同于"已被解决"的排雷，是"已被试过但未解出"
的难度先验校准信号），已在本回合报告中一并提交 planner。
**教益**：批量解题类新闻会让扫描产生"审美疲劳"，同类事件的第二、第三个实例更容易被
潜意识过滤掉——扫描纪律需要"新系统名发现"与"已知系统追踪"两条独立检索线，不能让
后者的高命中率掩盖前者的漏检。

> **[planner v3 背书 08-18]** R5 正式采纳（89 天核算无误；定位含 prompt 审计维度，合规）。
> 修正落地：①双检索线条款写入 notes/methodology.md 案例情报体系节 + charters/intel.md §1
> （"发现全新系统名"与"追踪已知系统"两条独立检索意图，后者命中率不得挤占前者）；
> ②"顶级实验室 attempted-未成功"立为 S0 分诊常设负面难度信号（区别于"已解决"排雷），
> 写入 methodology.md 与 TARGETS.md 认领门槛；#307/#1082 实例已注记。

## R6 · 2026-08-24 (dialogue v5) · S^6 complex-structure resolution: owner-reported, never intaken

**Fact (repo state audited 2026-08-24 02:0x CDT):** the owner verbally reported, in a prior
session (~08-23), that the construction of a complex structure on S^6 (the Hopf problem) had
just been resolved with AI. As of this audit the ONLY trace in the entire repo is one prior
citation in SELECTION.md:16 ("construction-type: YTD, S^6"). There is NO cases.md entry, NO
miss-analysis, NO retrospective, NO scan_log entry, NO arxiv_watch_ledger flag. The same-week
YTD disproof (2608.19301) got the full three-piece treatment (case / miss-analysis /
recalibration). The mandatory-reflection rule ("famous result neither recorded nor attacked
=> forced retrospective") fired for YTD and silently skipped S^6.

**Diagnosis:**
1. *Classification fatigue, second instance* (same mode as R5): the second major AI-resolution
   of the week was absorbed as a one-line prior in a planning doc instead of going through
   case intake. The channel that failed is new: OWNER-VERBAL intel, which had no intake rule.
2. *Primary source not yet verifiable:* arXiv API sweeps (title arm: six-sphere/6-sphere/S^6
   x complex structure; abstract arm; Hopf-problem phrasing) show nothing after 2606.03379
   (June 2026). If submitted 08-22/23 the paper sits in announcement lag and becomes visible
   Sun-Thu 20:00 ET. Case file is therefore PENDING-source, but the process reflection is due
   now — waiting for the source does not excuse skipping intake.
3. *Tool blind spot found while reflecting:* the daily watch's resolution arm carried only
   negative-resolution vocabulary (disproof/disprove/counterexample) plus "resolution of"/
   "proof of the" — a positive CONSTRUCTION title like "A complex structure on the six-sphere"
   matches nothing. Fixed same day: ARM_POSITIVE added to tools/arxiv_daily_watch.py
   (affirmative / long-standing / answering-a-question / open-problem / settles; measured
   ~14 extra flags/day on the 20260820 window).

**New rule (intake):** anything the owner names as a solved/major case is an intel EVENT, not
color commentary — it must get a cases.md entry (PENDING-source stub if the primary source is
not yet visible) within the same session, plus the standard miss-comparison once the source
lands. A citation inside a planning document is not intake.

**Follow-up owed:** when the S^6 paper announces (watch should now flag it), complete the case
file + miss analysis, and re-run the selection prior update (construction-type problems).

> **[R6 ADDENDUM, same day 02:3x]** Source hunt concluded. The paper is NOT in announcement
> lag — it is not on arXiv at all: X @__alpoge__ (08-23) + self-hosted https://alpo.ge/s6.pdf
> (fetched, title-page claim confirmed). So the deeper channel gap is: **major claims now
> announce via X + personal-site PDFs with machine-checkable certificates; an arXiv-only watch
> is structurally blind to them.** Complement = the case-intel web-scan line (X/blogs), not
> more arXiv arms. Second finding (measured): Brendle-Hung 2608.19068 (Hopf conjecture,
> S^2 x S^2, 08-19) is caught by NO keyword arm — its abstract contains no conjecture-genre
> vocabulary at all ("We construct a metric..."). Tested abs:"conjecture" = 40 hits/day AND
> still misses it (the control that must pass, fails) — rejected. Understatement-class results
> are a proven limit of keyword watching; they are exactly what author-level and community
> channels are for. Positive arm re-scan of 08-17..21 ledger days done (three-arm entries).
