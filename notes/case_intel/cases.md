# AI 解决猜想案例数据库

追加式。字段：日期 | 问题（名气级★1-5）| 系统 | 方法 | 验证 | 来源 | 启示
种子数据来自 2026-08-16 初始调研（21 案例，详版见调研档案）。

## 种子（2026-08-16 初始调研提炼）

- 2023-12 | Cap set 下界改进（★★★★）| FunSearch | LLM+进化搜索可打分构造 | 程序化评估+Nature 评审 | nature.com/articles/s41586-023-06924-6 | 构造+评分函数型问题是 AI 强区
- 2025-05 | 4×4 矩阵乘 48 次（56 年纪录）、kissing number 11维 593 等（★★★★★）| AlphaEvolve | 进化编码 agent | 自动评分 | deepmind 博客 | 同上；问题族可批量复用基础设施
- 2025-08 | 凸优化梯度步长 1.5/L（★★★）| GPT-5 Pro（Bubeck）| 单发长思考 | 人工逐行验证；后发现文献已有 1.75/L | whataifound.org | 解出后必查文献
- 2025-09 | QMA 放大误差下界引理（★★★）| GPT-5 Thinking（Aaronson）| 对话式纠错循环 | 人类秒验的子步骤 | scottaaronson.blog/?p=9183 | 选"人类可即时验证"的子问题；迭代鼓励有效
- 2025-10 | 凸优化 40 年开放问题（★★★★）| GPT-5 Pro（Ernest Ryu 三周迭代）| 多轮迭代 | 逐步人工复核 | Ryu X 线程 | 持续迭代+专家陪跑
- 2025-10~11 | Erdős #848（★★★）| GPT-5（Sawhney&Sellke）| — | 人工严格验证 | arXiv 2511.16072 | —
- 2026-01 | Erdős #728 + 衍生 #729/#401（★★★★，"首个公认 AI 自主非平凡解"）| GPT-5.2 Pro + Aristotle | 竞赛伪装+禁联网；LaTeX→Lean | Lean + Tao 确认 | arXiv 2601.07421 | 伪装 prompt；证明迁移（T7）
- 2026-01~03 | Gemini 半自主 700 题扫射 5 原创；Aletheia 700→63 正确/4-5 自主（★★★★）| DeepMind | Generator-Verifier-Reviser 环 | AI 验证器+人类终审 | arXiv 2601.22401 / 2602.10177 | 命中率思维；大规模扫射+分层验证
- 2026-04 | Erdős #1196（专家投入过的问题）+ 衍生（★★★★★）| GPT-5.4 Pro（Price 运行 80 分钟）| 发明"von Mangoldt 链"新技巧 | 8 人合著论文重构+部分 Lean | arXiv 2605.00301, Tao 博客 | AI 能发明可复用新技术；影响力目标可攻
- 2026-05 | Erdős #90 单位距离猜想证伪 + #92、启发 #52（★★★★★）| OpenAI 内部模型 + Claude Mythos 独立复现 | 代数数域构造+张量幂放大 | 独立复核+人类伴随论文 | arXiv 2605.20695, Bloom 博客 | 著名猜想的"证伪"路线；跨模型独立复现
- 2025-12~2026-06 | Erdős 问题批量 14+ 独立完整解（★★★~★★★★）| GPT-5.4/5.5 Pro、Aristotle、Claude 等 | 各式 | Lean 200+ 形式化、wiki 分级 | teorth/erdosproblems wiki | 社区赛道已拥挤（本项目 08-16 实测）
- 2026-08-16 | Fernandes 猜想（2026 论文 Conjecture 1，★★★）| **本项目**（codex 证明+Fable 审读+双模型审查）| Goursat+阶数障碍；盲解 | 14/14 计算+双审，Lean 施工中 | 本项目 papers/fernandes | 自产案例

## 增量（扫描追加区）

## 增量 2026-08-16 10:30 CDT（著名猜想清单调研带回的 7-8 月浪潮，全文见该调研报告）

- 2026-05-20 | Erdős 单位距离猜想证伪（★★★★★）| OpenAI 内部模型 | 类域塔/代数数论 | Alon+Gowers 验证 | arXiv 2605.20695 | "疑假猜想找反例"模式的样板
- 2026-07-10~14 | Cycle Double Cover 猜想"被证明"（★★★★★，**08-18 状态更新：已强化，非崩塌**）| GPT-5.6 Sol Ultra 64 子代理 | 8-cycle double cover 构造（3维GF(2)向量空间上nowhere-zero flow转化）；5-cycle 强化版仍开放 | **本回合更新**：公开 Lean 4 形式化已存在（finite loopless bridgeless multigraph 覆盖，钉定 commit）；图论专家 Jim Geelen 与 Sang-il Oum 各自独立发布"人类专家阐释版"（Independent Specialist Expositions），Oum 在 IBS 离散数学群研讨会公开报告；仍未走完正式期刊评审，但数学正确性已获实质性专家复核确认 | arXiv 2607.16356；Sang-il Oum 阐释版 arxiv.org+sangil.dimag.kr/2026/cdc/（WebSearch 独立核实，非仅凭 Qwen 转述） | **WATCH 结案：未崩塌反而增强，不再是"抢位机会"——已从存疑声称升级为实质性确认案例，图论头号开放目标应看 5-cycle 强化版而非退回 CDC 本身**
- 2026-07-20~21 | Jacobian 猜想 n≥3 证伪（★★★★★）| Claude Fable 5 + Alpöge | ℂ³ 显式 7 次多项式映射 | Tao 消化验证 | Tao 博客 | 平面情形（n=2）仍开放且信真
- 2026-07-22 | Dinitz–Garg–Goemans 猜想证伪（★★★★）| GPT-5.6 Pro，4 条 prompt 58 词 | 显式有限反例图 | 人工验证 | DataCamp 报道 | 极小成本大成果
- 2026-07-29 | Maxwell 猜想（1873）证伪（★★★★）| GPT-5.6 Sol 提供思路+人类严格化 | 5 电荷 24 临界点构型 | 人工 | arXiv 2607.27197 | AI 出想法+人类严格化分工
- 2026-07 | Grothendieck 有限自由群概形猜想反例（★★★★）| Fable/Sol + Akhil Mathew | 4 阶概形 | ~1000 行 Lean | Xena 博客 | —
- 2026-07 | Erdős–Szemerédi 和积猜想（ℝ 上）证伪（★★★★★）| 人类四人组受 AI 启发 + GPT-5.5 Pro 复现 7/8 | 全实代数数域 | — | arXiv 2605.28781 | 反例技术会连锁扩散
- 2026-08-01 | OpenAI Astra 一批 10 项（★★★★★，部分存疑）| Astra（未发布），$2000 推理成本 | 全部带 Lean 4 证书 | Lean（但"Lean过≠回答了本意问题"警示）| Zvi 汇总 | Alpöge 用 Claude Fable 24h 内复现 5/10
- 2026-02~08 | Hadamard 阶 668 填补（★★★★）| "三人+Claude" | 构造 | Epoch AI 暂认 | epoch.ai | 单点填补型
- 2026-04-03 | Kahn–Kalai "Conjecture 7" 证伪（★★★★）| GPT-5.5 Pro + Diskin/Kreitner（首个 AI+Polymath）| Lean 验证反例 | Lean | Kalai 博客 | 6(a) 仍开放且 Kalai 点名
- 2026-01/03 | Lonely Runner n=7,8,9 相继解决（★★★）| 计算机辅助 | 界定最小反例+验证 | — | Quanta 2026-03-06 | n=10 社区称"小改进即可"
- 2026-07-27 | **Crouzeix 猜想（2004，矩阵分析核心开放问题）证明**（★★★★★）| GPT-5.6 Sol ~16h，Shanmu Jin（协和神外住院医师，数学自学！）| **改编 OpenAI CDC 的多子代理对抗审查 prompt** | 8 天后 Lorist–Schwenninger 独立第二证明（arXiv 2608.03841）+ Crouzeix/Townsend/Greenbaum 逐行审读 SIAM News 认可（未走完期刊评审）| preprints.org + notes/case_intel/crouzeix_check.md | **业余者+公开脚手架即可攻克著名猜想；CDC 脚手架必须纳入我方武器库**

## 增量 2026-08-18（Sweep 4 线索 + planner WebSearch 核实）

- 2026-05-21 | **AlphaProof Nexus**（DeepMind）：Erdős 问题 9/353 自主解决 + OEIS 猜想
  44/492 证明 + Hilbert 函数 15 年悬案 + 凸优化界改进（★★★★，**此前情报漏检 ~3 个月**，
  与已收录的"2026-01~03 Gemini 半自主 700 题扫射/Aletheia"是不同系统，不可合并）|
  AlphaProof Nexus（Gemini 3.1 Pro 生成 + Lean 硬校验循环，George Tsoukalas 等 21 人署名）|
  LLM 提议+Lean 逐步机检拒绝幻觉的生成-校验循环 | 全部 Lean 4 形式证明公开
  （github.com/google-deepmind/alphaproof-nexus-results）+ 单价数百美元 | **主源**：
  arXiv:2605.22763"Advancing Mathematics Research with AI-Driven Formal Proof
  Search"，摘要原文"Our most capable agent **autonomously** resolved 9 of 353 open
  Erdős problems...proved 44/492 OEIS conjectures"（provenance 从句明确，非人类工作）；
  GitHub 仓库 APNOutputs/ErdosProblems/ 实际产出目录核实解决号为
  **{12, 26, 125, 138, 152, 741, 846}**（7 个不同编号，含 2 个拆两部分算 2 个 =9）|
  **对 TARGETS.md 撞车检查**：solved 7 号与本项目候选池（19/97/106/107/114/128/167/
  252/307/475/547/551/556/580/583/617/647/699/743/779/835/855/982/993/1020/1041/
  1082/1135）及排雷号（287/488/458/366/672/506/7/23/64/242/364/375/398/548/628/
  723/742）**零重叠**；但其 `erdos_problems_attempted.txt`（尝试未必成功）中含
  **#307（本池头部#4）与#1082（观察名单）**——即该题已被 DeepMind 顶级系统试过且
  未列入 9 个成功名单，隐含"已试过但未解出"的负面难度信号，非撞车但应作认领前提醒；
  另 OEIS 44 条与本项目 WOWII/677 线无重叠（不同题库）。已发短消息知会 planner
- 2026-08-10 | RH 临界线零点占比下界 41.6%→67.2%（two-thirds distinct+on-line, one-half simple；★★★★★，37 年仅进 0.8pp 的纪录级推进；**明确不证 RH 本身**）| Anthropic 未发布 Claude（Claude Code 编排 60 subagent、31M 输出 token、54h/3 日会话，先有独立的 ~1000-agent 十天前预热会话零产出仅留否定清单）| 组合 Weil 显式公式+Pontryagin 空间负指标路线（一半）与 Montgomery 整数模板+von Neumann 迹不等式（rank–trace lemma，三分之二）；referee 架构=同一 claim 派 2-4 个互相隔离+各配专项攻击任务的敌对 agent | Lean 4 形式化（`sorry`-free，公开仓库）+ 内部数学家 Alpöge/Furman + 外部专家 Conrey/Goldston 复核；社区复核进行中 | **主源全套**：anthropic.com/research/riemann-zeta（论文/informal note/Claude 自述过程 95pp/原始 transcript 116pp 四个 PDF 均公开）；**arXiv:2608.13637**（署名 Alpöge & Furman，摘要明载"discovered autonomously by Claude (Anthropic); verified and communicated by the listed authors"——署名人=人类验证者非独立作者，勿再误判为独立人类工作）；github.com/anthropics/zeta-23-lean；TechSpot/Neowin/MLQ/TechTimes 08-11/12 二手报道 | 编排/预算/verbatim brief 深度考古见 prompts/case_prompt_archaeology.md §8；多 agent+大 token 预算规模上限远高于我方现用；"组合已有文献"是可移植模式；情报漏检 7 天 → 反思 R3；08-18 续场中还发现 Qwen 曾将 arXiv:2608.13637 误判为"无关独立人类工作"（T005 Sweep4 遗留错误，已在 §8 订正）

## 增量 2026-08-22（Deep Research T1 harvest 补漏，对照 cases.md 全文而非 scorecard 窄口径 8 项 key；deepresearch_T1.md 8 行摘要表中 Jacobian/CDC/Dinitz-Garg-Goemans/RH-67.25%/Erdős单位距离 五项已在本文件既有行中，不重复添加；下列 5 项为本文件此前缺失）

- 2026-07-27 | Feige's 1/e 反集中猜想证明（2004，★★★★，六人合著）| ChatGPT 5.6 Pro（Zhengqing Zhou 主导实验，Guanyang Wang 等共著）| 凸几何 Grünbaum 形心定理 + Letwin-Yaskin(2024) 推广，桥接 Vlassis-Thomas Dirichlet 校准定理（该定理同时解决 Gaffke 统计猜想），证明过程本身被记录做 prompt 消融实验 | **VERIFIED**：arXiv API 直查 2607.23980 存在（2026-07-27 发表，math.PR），摘要原文自述"The proof is found by ChatGPT 5.6 Pro"（一手文献自证，非二手转述）| arXiv:2607.23980（Fu, Han, Wang, Yan, Zhang, Zhou, "Sharp small-deviation inequalities..."）；guanyangwang.github.io/blog/feige-conjecture.html（消融实验：单句"先广泛搜文献不限领域"指令使成功率从 0/4 升至 3/4）| prompt 工程强证据——"先地毯式搜文献再证"值得纳入我方 prompt 模板；同窗口内出现独立人类竞争证明（arXiv 2607.24528, Nie & Wei，无 AI），说明该猜想已进入多路竞速期，若我方未碰过此题不必再追（已被抢）
- 2026-08-12 | Zhao's Vanishing Conjecture（齐次四次型 Laplacian 消没猜想）证伪，40 变量反例（★★★，Jacobian 反例技术下游应用）| DR 摘要表标注"Claude Fable 5（经 Thompson/MacFarlane）"，但独立复核发现 arXiv 页面**署名仅人类作者 Thomas Prellberg，无任何 AI credit** | collision-generated compression：将 Jacobian 反例构造中的 collision 子代数手法迁移到齐次 Keller 映射，在 Q(i) 上给出 350-单项式四次型及精确梯度 collision | **事件本身 VERIFIED**（arXiv API 直查 2608.12543 存在，2026-08-12 发表，math.AG）；**AI 归因 UNVERIFIED-CLAIM**——WebFetch 复核摘要页确认无任何 AI 模型提及；"Thompson""MacFarlane" 实为摘要内数学对象名（Thompson 的 24 变量映射、MacFarlane 不变子空间），非人类协作者，DR 摘要表"系统"列疑似把对象名误读成人名/系统名 | arXiv:2608.12543（Prellberg, sole author）| 反例技术级联扩散的又一实证（Jacobian→相邻猜想的脚手架复用模式，同 CDC 脚手架逻辑），但 AI 归因需谨慎——DR 摘要表本身有误读风险，抄录前必须查一手原文，不能只信摘要表列名
- 2026-08-20 | 有理数域椭圆曲线秩下界推进至 rank≥30（★★★★，前纪录 rank≥29, Elkies&Klagsbrun 2024）| Claude（Anthropic team）协助 Levent Alpöge + Ava Howell；**Alpöge 与 07-19 Jacobian 反例通报人为同一人** | 显式构造 30 个线性无关有理点（无条件下界）；上界=30 在 GRH 下经 Bober 方法证得 | **VERIFIED**（社区排行榜级，非期刊级）：ICARM 排行榜 curve #273（elliptic-rank.icarm.cloud）公开挂出，公告日 2026-08-20；两次独立 WebSearch 交叉核实（HN 帖 + Bartosz Naskręcki 祝贺 X 帖 "@__alpoge__ ... team Anthropic"）均确认 Claude/Anthropic 参与 | icarm.io/news/new-record-breaking-elliptic-curve-reported/；elliptic-rank.icarm.cloud/curve/273；news.ycombinator.com/item?id=49374873；x.com/nasqret/status/2090524721360097594 | Alpöge 在 7 月 Jacobian 反例、8 月椭圆曲线秩纪录两个独立事件中都是"人类锚点"角色——同一批 Anthropic 关联数学家在连续认领纪录型问题，是评估"AI+特定人类专家"组合竞争强度时的重点盯防对象
- 2026-08-17 | **FAR（Find-Attempt-Recommend）工业化猜想发现流水线**首个 pilot，组合数学领域（★★★★★，方法论意义 > 单点结果）| GPT-5.5 Pro（xhigh 推理，攻打/评审/评分全阶段）+ gpt-oss-120b（标注）+ gemini-3.5-flash（抽取）+ gemini-3.1-pro（联网核验）| 文献→候选猜想→开放性核验→AI 批量攻打→人工终审 五级漏斗：51,110 论文→5,245 组合数学论文→6,453 候选猜想→4,717 确认开放→598 疑似解决→77 人工复核产出；产出含 Ikenmeyer-Pak-Panova 猜想证明、Erdős-Straus 二项式整除性问题、Davies-Jenssen-Perkins-Roberts 与 Lund-Saraf-Wolf 猜想反例 | **VERIFIED**：arXiv API 直查 2608.16977 存在（2026-08-17 发表），作者含 Jeremy Avigad（Lean/形式化验证权威）、Sean Welleck（LLM+数学权威），可信信号强；DR 摘要表漏斗数字与论文摘要完全吻合 | arXiv:2608.16977 "The Problem Is the Problem: Towards Scalable Mathematical Discovery"（Zheng, Zhang, Avigad, Tetali, Welleck）| **本轮新增中对我方战略最相关**——公开的"literature-to-proof"全自动化管线范本，五级漏斗（挖掘候选→开放性核验→批量攻打→分层人工复核）可直接对标/借鉴到我方流水线设计；竞争风险：若类似工业化管线批量扫过 Erdős/OEIS 题库，会持续蚕食本项目"未被触碰的开放问题"候选池，需要把 TARGETS.md 候选与该类管线可能覆盖领域（目前仅组合数学 pilot，尚未见数论/代数几何 pilot）做撞车监控
- 2026-06-02 | **Leiden Declaration on Artificial Intelligence and Mathematics** 发布，IMU 正式背书（政策/规范事件，非解题事件，★★★★，行业级）| 国际数学家联合声明（起源 2025-09 Lorentz Center 研讨会），Scholze/Buzzard/Goldberg/Tillmann 等联署，07 月 ICM 大会由 Jim Portegies 宣讲 | 要求：AI 使用须透明披露、人类对 AI 生成证明的正确性负最终责任、遵循开放科学原则、反对成果私有化 | **VERIFIED**：多源交叉确认——en.wikipedia.org 词条、Leiden University 官方新闻稿、CACM 博客、mathunion.org 官方 IMU AO Circular Letter 8/2026 PDF（IMU 一手文件）均一致，发布日期 2026-06-02 | leidendeclaration.ai；en.wikipedia.org/wiki/Leiden_Declaration_on_Artificial_Intelligence_and_Mathematics；mathunion.org/fileadmin/documents/2026-06/IMU_AO_CL_8_2026.pdf | 竞争对手/学界"规则环境"变化而非具体解题事件——若我方以后要发表/公开任何自动证明成果，需评估是否要遵循同等披露规范（AI 使用披露、人类担责）以规避"不透明"指控；也说明学界已把"AI solved it"当作严肃议题系统追踪，我方成果保密/公开节奏需相应权衡

## 增量 2026-08-22（续，methodology_far_integration 任务登记，占位不深读）

- 2026-08-22 | **pipeline-math** 猜想发现/证明管线（Peng/Tao/Wang/Yu，2026）（★★★，方法论意义，**NOT YET READ**）| 未知（未读，仅知 GitHub 仓库名）| 未知 | 未知 | **NOT YET READ**——经 FAR 论文（arXiv:2608.16977）related-work 引用带回本仓库地址（far_pipeline.md §3 已摘录原文引用句），本轮据 planner 指示不深读，仅登记占位 | github.com/Pengbinghui/pipeline-math（引用来源：far_pipeline.md §3 "Related competing pipelines"）| 第二个具名竞争管线；下一轮情报扫描应深读评估其架构与撞车风险；已在 orchestration/watch_ledger.md 竞争管线 watch 表登记同名行

## 2026-08-19 — cscK Yau–Tian–Donaldson DISPROVED, AI-obtained (arXiv:2608.19301, Jihao Liu)
Full case: `case_ytd_2608.19301.md` · miss-analysis: `miss_analysis_ytd.md` · recalibration:
`recalibration_ytd.md`. **Top-tier case.** Polarized smooth projective fivefold, K-polystable, no
cscK metric — **cscK version only; Fano/KE (CDS, Tian 2015) unaffected, and a citation dropping
"cscK" is malformed.** Obtained with GPT-5.6-sol + Fable 5 + Danus; appendix with Bin Dong and
Guoxiong Gao documents usage in detail. Headline takeaways: the **two-kinds taxonomy** of
counterexamples (finite certificate vs. "in substance, a proof"); **Claude Code (Fable 5) at max
effort failed this problem**, as did five other systems, and **none of the six could prove it even
when handed the counterexample**; **Danus alone solved it in 5 h 29 min** — architecture beat bare
model. Fact-graph economics: **88 of 616 facts (14%) in the main-theorem closure**.
**We missed it for four days; the cause was structural — every channel was pull-by-target and the
only scheduled watch faced our own output.** Fix built and self-tested: `tools/arxiv_daily_watch.py`.

## 2026-08-23 — S^6 complex structure (Hopf problem) CLAIMED, Levent Alpoge + Claude — NOT on arXiv
**Primary source located 2026-08-24 02:3x CDT: https://alpo.ge/s6.pdf** (1.1MB, pdfTeX; title/author
metadata empty; attribution via alpo.ge domain + X @__alpoge__ post 08-23). Title-page claim verbatim:
"The Delta(3,4,infinity) modular family of 2-tori, completed at its three special points, is a complex
structure on S^6" — triangle group Delta(3,4,inf) acting on rank-4 lattice, family of complex 2-tori
over orbifold P^1, Kodaira logarithmic transforms at the three special points; claims a(X)=1,
very-general fibre non-algebraic. Per X: "short certificates" philosophy + Claude composed a 100+ page
writeup; finite matrix computations verify pi_1/homology. **STATUS: first-party-VERIFIED claim (author-run finite
certificates), one day old, no arXiv, NOT YET INDEPENDENTLY/PEER VERIFIED — do NOT cite as
established (owner correction 08-24: "unverified" is the wrong word for this class; the right
axis is first-party vs independent verification).** Retrospective R6. Channel note: announced ONLY via X +
self-hosted PDF — structurally invisible to the arXiv watch.
Same-author cluster (intake 08-24):
- **2608.19068 (arXiv, 08-19): S. Brendle + P. K. Hung, "A metric on S^2 x S^2 with positive sectional
  curvature" — the HOPF CONJECTURE (curvature), distinct from the S^6 Hopf PROBLEM; abstract is pure
  understatement (no 'conjecture'/'Hopf'/'long-standing' anywhere; MATHEMATICA-assisted, no AI decl.).
  Keyword arms CANNOT catch this class — measured, see R6.**
- X 08-19: Alpoge (+collaborator +Claude) claims Caratheodory AND Loewner conjectures FALSE with
  explicit counterexamples — PENDING verification, no paper located yet.
- X 08-20: Alpoge on Brendle-Hung: he had a candidate construction with only numerical positivity
  checks — top-tier humans+AI now racing the same targets days apart.
Method detail (per his own X posts, 08-23): construction verified via FINITE MATRIX COMPUTATIONS
(pi_1 vanishing + homology of the completed threefold), packaged as "short certificates that people
can use to verify in full with their expertise" + two replication screenshots; **Claude composed the
100+ page detailed writeup** and is credited for "computational and theoretical assistance" —
division of labor beyond that (who proposed the triangle-group ansatz) NOT yet public. PDF is >=68pp
(hyperref anchors); no AI statement extractable from the PDF locally (CM font encoding — do not
assert absence). Context: Alpoge = Anthropic-affiliated mathematician (per Digg cluster reporting),
the same operator as Jacobian counterexample (07-2026, w/ Claude Fable 5) and named human verifier
on Claude's zeta-zeros result (2608.13637). His repeatable pattern: expert + Claude long-session ->
explicit construction + machine-checkable certificate -> same-day X/self-hosted announcement.
Reception (08-24): mixed, treated as FIRST-PARTY CLAIM, not independently verified; the S^6 problem
has a graveyard of failed claims (Etesi etc.) — verification discipline scales with fame.

## 2026-08-29 — daily case scan, window 08-24→08-29 (SOP v5)

- 2026-08-25 (v3 08-27) | **Fröberg's Conjecture — Hilbert series of r general forms of degree
  d in k[x1..x4]**, proved for every r≥1 in the two cases d=5 (quintics) and d=7 (septics),
  extending previously-unproven generator-count ranges 6≤r≤11 (quintics) / 6≤r≤21 (septics);
  paper explicitly scopes out the unrestricted conjecture (★★★, 40-year commutative-algebra
  conjecture, Fröberg 1985) | Qihang Wang & Dongming Zhang, three-model workflow: OpenAI
  GPT-5.6 Sol + Anthropic Claude Fable 5 + Grok 4.6 | disclosure verbatim: "formulation of
  mathematical ideas, generation of conjectures and proof strategies, derivation and checking
  of intermediate steps, construction of examples and exact certificates, comparison of
  literature and candidate proof approaches, organization of arguments, LaTeX drafting, and
  revision of the final text... decomposed the problem into smaller subproblems and used
  repeated self-critique and alternative derivations"; no stated human orchestrator, no
  division-of-labor breakdown between the three models | exact linear algebra (Macaulay
  multiplication-matrix endpoint-rank reductions) via two ancillary Python verifier scripts
  (`froberg_quintics_verifier.py`, `froberg_septics_verifier.py`); no Lean certificate |
  **VERIFIED** via direct WebFetch of arXiv abstract page + full HTML (2608.24797v3,
  math.AC) | arxiv.org/abs/2608.24797 — **method absorption: NONE NEW.** The "multi-model
  cross-check + repeated self-critique + exact-certificate verifier script" pattern this case
  demonstrates is already inside our own VERIFY_CHECKLIST / S-8 counterexample-witness
  discipline and the CDC-style adversarial cross-family review absorbed 08-16; this is a
  confirmation data point, not a new transplant. **Famous-watch / TARGETS touch: NONE** —
  Fröberg's conjecture is absent from `notes/selection/famous_watch.md` and from
  `orchestration/TARGETS.md`'s pool and observation list; no RE-SCORE flag.

Scan coverage note (not a case row): searched arXiv (via `notes/case_intel/arxiv_watch_ledger.md`
resolution/positive/ai-disclosure arms for 08-24..08-27 — **ledger has no 08-28/08-29 entries
yet, i.e. the automated arXiv daily watch is 1-2 days behind; flagged for the arxiv-watch
monitor, not fixed here**), Terence Tao's blog (terrytao.wordpress.com, only new post in window
is a non-AI Kakeya popularization, 08-25), X (Alpöge @__alpoge__ — xcancel.com mirror shut down
08-24 after an X Corp cease-and-desist, could not re-verify recent posts directly; no new
primary source found this window for the previously-PENDING Caratheodory/Loewner claim, so no
row added and the PENDING status from the 08-24 entry stands unchanged), DeepMind/OpenAI blogs
(no new math announcements in window; Astra's 10-result drop remains 08-01), MathOverflow
"AI-assisted" search (nothing new in window). No famous-watch-listed problem (S^6, Kaplansky,
Lonely Runner, Agrawal, Kourovka 20.76, Erdős #699/#982/#617/#779, Zariski Cancellation,
Casas-Alvero, Circulant Hadamard, Jacobian n=2, CDC 5-cycle, Kalai 6(a), Andrews-Curtis, Conway
99-graph, Collatz) had a new development in this window per checks run.

## 2026-09-06 — owner-verbal intel (two WeChat articles), full intake in notes/case_intel/case_colombo_flt_2609.md

- 2026-08 (arXiv 2609.00101, v1 ~09-01) | **Colombo 1928 determinant problem** (det ≠ 0 for even N,
  D ≥ N−1; ★, VibeMathed significance 12/100; concurrent independent proof by Kun Li et al.) |
  Qianli Ma + WuJie AIAGENT team: GPT-5.6 Sol literature, Claude Fable 5 red team, DeepSeek/Qwen/
  Kimi Lean, upper agent scheduling sub-agents, human sets routes and compute | 8 routes each with
  advantage/weakness/obstacle/continue-or-not evaluation; route p=m−1 burned 11h17m / 141 artifacts /
  47k lines "rewarded by local progress" until the human stopped it; lowering to p=m−2 exposed regular
  structure and closed in 2h23m; Pfaffian → integral → spline determinant ≥ 0 → strictly positive region
  | Lean 4.30, ~20k lines, no sorry (repo hkjtsgmc79-boop/colombo-odd-lean); small-circle peer read,
  not refereed | **VERIFIED** (arXiv abstract + disclosure section + Lean README read directly) |
  **absorption: TEMPLATE v2.4 ROUTE PORTFOLIO BLOCK** (route table, 25% budgets, gap-sentence metric,
  judge/worker split, mandatory lower-the-target move). Famous-watch touch: none.
- 2026-08-18 (Anthropic blog + repo anthropics/fermats-last-theorem + Claude log PDF; Prove2Me paper
  2608.28433) | **Fermat's Last Theorem fully formalised in Lean** (formalisation, not a new theorem —
  out of VibeMathed scope; ★★★ as a capability event) | Claude research model ≈ Fable 5.1, dozens of
  parallel agents on the Prove2Me harness (Columbia, Tianyi Peng); humans wrote one line of Lean and a
  few priority remarks | 11 days, 6×10⁹ output tokens, 29,511 theorems / 60,474 files; pre-harness
  phase lost global state (≈7% wasted lines); harness = theorem DAG + statement/proof split cards +
  NL descriptions for search/reuse; agents pre-checked each other's statements | verification: full
  recompilation, single-project build (3 axioms, no sorry, derives Mathlib's FLT statement), Lean FRO
  comparator, nanoda kernel, FinalCheck.lean with #guard_msgs | **VERIFIED** (blog, README, log PDF,
  Prove2Me skill/solver/captain/prove prompt files read verbatim) | **absorption: card workflow
  (local Prove2Me-lite), blind read-back before proof, FinalCheck.lean mandatory, explanation style,
  Lean leaves to cheap tier.** Famous-watch touch: none.
- 2026-07-13/15 (starfleetmath.com; explainx.ai write-up; HN thread) | **Star Fleet Math** — 27 Erdős problems
  "Solution Proposed" incl. 13 claimed full solutions (#123, #254, #267, #320, #321, #336, #394, #450,
  #489, #538 …) and partials (#709 f(n) ≤ 14n^{3/7}, #769 c(n) ≫ n^n disproved, #959, #1186, #1189)
  — community status pending for all (★ each; not on erdosproblems.com) | Colin Snyder (self-funded,
  advised by Mike Kim): Mac app driving 20 parallel "starships" (GPT-5.6 Codex, 60-vCPU each, 2000-vCPU
  bursts, H100), Lean 4 + SAT/SMT/CAS tools, Claude Fable API wrapped as proof-verifier harness,
  iMessage alert for human review, Ton 618 premise graph (gemini-embeddings-2 + Chroma), Firecrawl
  index | harness artefacts visible in the #709 bundle: `verified_math/` ledger (one-line index +
  one folder per fact F-nnn with frontmatter tier lean/gate/census, polarity, depends_on, supersedes,
  exact verifier command; "never edit or delete a fact — supersede it"; negative results first),
  canonical Statement.lean mirrored byte-for-byte in an audited_mirror, verify.sh gate banning
  sorry/admit/axiom | **VERIFIED for #709 by automath**: statement faithful, proof read in full
  (Katz–Tao four-projection transfer), local pinned rebuild — see problems/erdos709/G2.md |
  **absorption: (i) G2 must query VibeMathed + starfleetmath (tools/vm_g2.py, tools/sfm_g2.py);
  (ii) verified-fact ledger pattern (index + per-fact folder + exact re-verify command + supersede
  rule) adopted for our proofs/ folders; (iii) NEW ROUTE for #709: more slices / longer blocks to
  beat exponent 3/7.** Famous-watch touch: none.
