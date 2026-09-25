## Sweep 1 · 2026-08-16 上午
- 渠道：Qwen3.8-Max 网页（搜索开）完整报告 → sweep1_qwenweb.md；GPT-5.6 Pro 网页（搜索开）70min 未收敛 → sweep1_gptweb.md（PARTIAL，检索轨迹含线索）
- 新条目：确认 Astra/单位距离/Tao ICM 五阶段论；**待核实线索：Crouzeix 猜想 AI 证明（Jin 2026）**、Umans–Wang、thin-shell
- 运维教训：GPT-Pro+search 的开放式大请求会陷入检索循环——拆成小请求；Qwen 是全谱扫描更可靠的执行者

## Sweep 2 · 2026-08-17 上午（补记 08-18）
- 渠道：sonnet WebSearch 全谱扫描 → 独立报告 scan_0817.md（当时未按体系归档进本流水账，08-18 补记）
- 要点：见 scan_0817.md；本次补记同时修复"扫描后必须当日入 scan_log"的流程漏洞

## Sweep 3 · 2026-08-18 深夜（GitHub 直查，非网页模型）
- 渠道：gh CLI 直查 FC 仓库 PR/issue/竞争者仓库（复盘会话顺带完成，属 S4 深查而非全谱扫描）
- 新条目：KitaKen1 工业化流水线全景（30+ 仓库：OEIS 系列、Erdős 319/357/361/692/979、Green 37/52、Kahn-Kalai C7 反例、weak-tiling 反例等；深夜仍活跃，最新 oeis-a129365）
- 触发未命中反思 R2（双撞车）；查重清单 v2 已入 methodology

## Sweep 4 · 2026-08-18（T005 例行增量扫描，PARTIAL/RESUMABLE）
- 渠道：chat.qwen.ai qwen3.8-max（thinking+search，切模型已截图确认）；Q1 遇 2 次
  "high demand" 报错，第 3 次重试成功；planner 因 Zenodo 发布任务收回 Chrome 租约，
  Q2/Q3 未发送即收尾。详见 orchestration/results/T005_case_intel_scan.md（状态
  RESUMABLE，Q2/Q3 问题原文已留档可直接续用同一 Qwen 会话）。
- Q1（arXiv+GitHub，08-17 后）结论：未检索到新增案例。
- 新线索（未验证）：Qwen 提及 2026-08-10 Anthropic Claude 研究版本经 Agent 架构将黎曼猜想
  临界线零点占比下界从 41.6% 提升至 67.2%，cases.md 未收录、来源不完整——留给续场核验真伪。

## Sweep 5 · 2026-08-18（owner-intel 首回合：RH 案深度考古 + KitaKen1 基线接手，WebSearch/WebFetch/gh，无 Chrome）
- RH 案考古：直读 anthropic.com/research 官方页 + 四份 PDF 原文全套（论文/informal note/
  Claude 自述过程 95pp/transcript 116pp）+ arXiv:2608.13637 摘要 + github.com/anthropics/
  zeta-23-lean README。产出写入 prompts/case_prompt_archaeology.md §8（编排结构/60 subagent
  角色分布/verbatim 研究 brief/referee 架构/预算数字）；cases.md 08-18 条目已订正+补全主源；
  另发现并订正 T005 Sweep4 遗留错误（Qwen 误判 arXiv:2608.13637 为无关人类工作）——已起草
  retrospectives.md R4（待 planner 背书）
- KitaKen1 基线：`gh repo list KitaKen1 --limit 100` 全量 69 仓库 + PR/commit 抽查，见
  competitor_kitaken1.md「快照 2026-08-18」——零撞车信号（677/WOWII-133/WOWII-61 均未命中）
- Chrome 全程 LEASED→T008（Zenodo 发布），本回合未占用；T005 Q2/Q3（X/新闻+Zulip+KitaKen1
  逐日 diff，需 Qwen 网页）轮询未空出，留次回合续场，会话 URL 与问题原文仍在
  T005_case_intel_scan.md

## Sweep 6 · 2026-08-18（owner-intel 回合 2：WebSearch 例行扫描 + 20 候选重建 + Chrome 到手续 T005）
- 例行 WebSearch 扫描（厂商研究频道+主流科技媒体，R3 硬性条款）：Anthropic/OpenAI/DeepMind
  近期动态均已收录（RH、Astra、Jacobian），**新发现 DeepMind AlphaProof Nexus
  （arXiv:2605.22763，05-21 发布，此前漏检 ~3 个月）**——已订正入 cases.md，
  provenance 核实（摘要"autonomously resolved"）+ GitHub 实际解决号核对
  （{12,26,125,138,152,741,846}，与本项目候选池/排雷号零重叠；但其"attempted"清单含
  我方 #307/#1082，非撞车但为难度先验警示）；已起草 retrospectives.md R5（待背书）
- 20 候选评分表重建（T009 已确认原表 MISSING）：4 个锚点条目（Conway99/Andrews-Curtis/
  Lonely Runner/2nd Hardy-Littlewood）现状快照见
  orchestration/results/intel_20cand_rebuild.md；关键更新——Lonely Runner n=10 已被
  证明（arXiv:2511.22427，Trakulthongchai，Oxford 本科生，2026-04 修订），n≤12 全部
  解决，Autumn 2026 有专题 workshop，比 08-16 快照更拥挤
- KitaKen1 diff（`gh repo list`+`gh pr list` 直查）：与今晨基线比对**无新增仓库/PR**，
  677/WOWII-133/WOWII-61 零命中，零撞车
- Chrome 08:0x 见 FREE，即刻接手（登记 RESOURCES.md）；首个动作=双表配速截图法首测
  （All 60% used/剩40%，Fable 51% used/剩49%，Weekly Sat 00:00 重置，已短消息报
  planner，planner 裁决=Fable 相对未用满触发 upshift 温和档）
- T005 Q2/Q3 续场（同一 Qwen 会话）**已完成**：CDC 猜想状态由 WATCH 升级为实质确认
  （Geelen/Oum 独立阐释版+Lean 4 形式化，独立 WebSearch 交叉核实）；Crouzeix 两份证明
  均未撤稿，08-14 GitHub 反例仅伤及 Lorist–Schwenninger 一个辅助 Remark、主定理不受
  影响；Zulip/MathOverflow/erdosproblems wiki 08-17 后无新 AI 解题动态；**新发现扫描
  风险源"AI Village News"**（gitlab.io，DeepSeek-V4-Pro 撰写的虚构多智能体沙盒"战报"，
  含逼真假冒猜想解决案例+假 commit hash，WebFetch 独立核实其自我披露为模拟）——已提交
  planner 裁决是否入 methodology.md 排除清单。详见 T005_case_intel_scan.md（状态
  COMPLETE）
- **planner 08-18 中途下达 Qwen 饱和使用政策（新标准职责）**：owner-intel 兼任
  qwen_capability_profile.md 维护者 + 持 Chrome 时兼 qwen_queue.md driver。本回合执行：
  发现队列 Q1（w61 S3 Theorem N + T3 跨模型第二轮）已有 owner-w61 备好的官方
  ready-to-paste brief（`prompts/w61_S3_qwen_R2.md`），按其"两个独立会话"规范用 sed
  拆分 verbatim 附录（非手抄）分别派发（Theorem N 会话
  718f2032-2cf7-444c-bbb0-c6b2a8eb0fcb；Theorem T3 会话
  5b9c1698-f879-41cb-bc1f-36dee1c56af0，中途遇一次"high demand"报错已重试）；另有
  owner-intel 本人在得知官方 brief 存在前先行派发的一版手写对抗审查 prompt（会话
  0ccceb5b-73da-40bc-9ec8-836b0e9e4fd6，非官方版本，作补充数据点）。三个会话在本回合
  结束时**均仍在生成中**（复杂密集证明审查，预计远超单次轮询窗口），已在
  qwen_queue.md 登记完整交接说明供下任 driver 收割，未强行等待完成——回合时间纪律
  优先于任务饱和度


## Sweep 7 · 2026-08-22 晚（scout-retriage-r1：TARGETS 头部再分诊，`orchestration/
tasks/targets_retriage_r1.md`，Part 1 zero-quota + Part 2 Google AI Mode，无 Deep
Research）
- 渠道：Part 1 = `gh` CLI 直查 google-deepmind/formal-conjectures（merged+unmerged PR/
  issue）+ `gh repo list KitaKen1`（80 仓库）+ arXiv 前端 `arxiv.org/search`（export API
  遭遇持续 rate-limit，改走网页前端）+ OEIS + `google-deepmind/alphaproof-nexus-results`
  attempted 清单直读；Part 2 = Chrome Google AI Mode（`google.com/search?...&udm=50`，单
  tab 串行，租约见 RESOURCES.md scout-retriage-r1 行）。
- **#2 Kaplansky 零因子猜想**：CONFIRMED OPEN。FC 仅格式化 PR（#117/#173/#3532/#3538）；
  两个自称"solved"的 PR #2615/#3139 均 CLOSED 未合并且针对的是已解决的 unit 变体非
  zero-divisor；KitaKen1 零命中；arXiv 160 条泛化噪声无专题解决论文。AI Mode 报出未核实
  线索：MathOverflow 2026-07-29 帖"Checking one group for torsion"（用户 Maximka123）
  构造候选反例群测 torsion-free，未独立核实，记为 lead。
- **#9 Kourovka 20.76**：CONFIRMED OPEN，本轮置信度最高——直读 FC 主分支当前源码
  `FormalConjectures/Kourovka/20_76.lean`，确认仍为 `category research open` + `sorry`。
  唯一相关 PR #1906（MERGED，纯格式化）。交叉核对 arXiv:2607.17477（Aristotle/Harmonic
  一次解决 8 题的论文，含本池 #1）摘要全文，确认 20.76 不在其列（最后一条"p-group
  extension rank inequality"与 20.76 精确陈述不是同一命题）。
- **#5 Agrawal 猜想**：CONFIRMED OPEN，零竞争。唯一 PR #3610（MERGED，仅加陈述无证明，
  issue #3606 因 formalize 关闭）；KitaKen1/arXiv 均零命中；AI Mode 复述既有
  Lenstra–Pomerance 启发式（非新证据）。
- **#4 Erdős 307**：CONFIRMED OPEN 但**订正为更挤**——PR #4260（MERGED 06-22，barrier，
  ElVec1o，外部 Zenodo DOI）→ #4403（OPEN 07-06，同作者加强到 60 素数）；#4429（CLOSED
  07-14）→ #4479（OPEN 07-20，SNAPKITTYWEST，明确修正 #4260 一个已合并的错误定理并加
  11-素数 barrier）。两个独立贡献者近 6-10 周内正面竞速同一开放命题，不挤度 2.5→1.5，
  总分 131→≈79。
- **#6 Erdős 617**：CONFIRMED OPEN，零新信号（唯一 PR #1845 MERGED 纯格式化）。
- **#7 Erdős 699**：CONFIRMED OPEN——PR #3984（MERGED）明确注明只连接已解决子引理
  Sylvester-Schur，未碰开放的 gcd 主命题。
- **#8 Erdős 779**：CONFIRMED OPEN（实际落在 `Wikipedia/` 路径，PR #3714 MERGED 纯
  格式化 + 一条被判重的 #4381 CLOSED）。**R5 新命中**：`erdos_problems_attempted.txt`
  直读确认 `erdos_779` 在列——v1 未记录，本轮新增。
- **#10 Erdős 982**：CONFIRMED OPEN——主命题未动；一条 OPEN 未合并 PR #4694 只加了一个
  更弱的 concyclic 变体。**R5 新命中**：`erdos_982` 同样在 attempted 清单——v1 未记录，
  本轮新增。
- **R5 复核**：`google-deepmind/alphaproof-nexus-results` 最后 commit 2026-06-05，since
  08-18 无变化；attempted 清单本轮新确认命中 #779/#982（此前只记录 #307/#1082），solved
  清单 {12,26,125,138,152,741,846} 与本池仍零重叠。
- 产出：`orchestration/TARGETS.md` v2（#1 归档存证，头部改为 A/B 双序，推荐 #2 为下一条
  owner 线）；`orchestration/RESOURCES.md` Chrome 租约记录（取用+释放）。

## Radar tick — 2026-08-22 21:1x CDT (planner v4, routine per-cycle check)
`gh repo list KitaKen1` top-5 by recency: **four repos updated TODAY (08-22)** —
`formal-conjectures`, `green-29-counterexample`, `opg-melnikov-valency-variety-lean`,
`erdos-367-higher-full-parts`; plus `oeis-a076141-binary-word` (08-21).
**Collision check against our active lines (WOWII-61 / WOWII-133 / ETP 677) and the TARGETS head
(Agrawal, Kaplansky, Kourovka 20.76/20.75, Erdős #307/#617/#699/#779/#982, Lonely Runner):
NO MATCH.** Erdős #367 is not in our pool.
**Pace datum, not a collision:** four repos in one day sustains the industrialised-competitor
profile on file. Our exposure is unchanged because our three active lines are all bespoke
(WOWII / ETP) rather than drawn from the shared benchmark lists this competitor works from —
worth stating, since that structural separation, not luck, is what keeps the collision surface
small. The pool candidates are where we ARE exposed, which is a further argument for gating them
before committing rather than after.
