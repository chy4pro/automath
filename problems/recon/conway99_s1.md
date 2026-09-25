# S1 文献侦察：Conway's 99-Graph Problem

日期 2026-08-17。检索手段：WebSearch + WebFetch（arXiv abs/html 页、Wikipedia、Epoch AI、straylight 博客、GitHub、CAISc 官网均已直接抓取核实）。目标问题：是否存在 srg(99,14,1,2)（99 顶点强正则图，λ=1,μ=2）；Conway 2014 年在 DIMACS 会议悬赏 $1000。

---

## 0. 结论先行

**截至 2026-08-17，问题仍然 OPEN**（未见任何存在性构造或不存在性证明，2026 全年多篇新文献均只是缩小范围/给出计算下界，无一声称解决）。

**建议：PARK-WATCH**（不主攻，定期扫描）。理由见 §5。

---

## 1. 问题现状

- Wikipedia 词条（<https://en.wikipedia.org/wiki/Conway%27s_99-graph_problem>，最后更新 2026-01-30）仍标注"remains open and unsolved"。1969 Biggs 首提可能性，1975 Conway 研究，2014 Conway 在 DIMACS 悬赏 $1000。
- 满足 λ=1,μ=2 可行性条件的参数集仅 5 组：(9,4)、(99,14)、(243,22)、(6273,112)、(494019,994)（Keramatipour 2026，见 §2）。前两个已构造出图——(9,4,1,2) 即 Paley(9)，(243,22,1,2) 即 Berlekamp–van Lint–Seidel 图；**99 是"最小的未知情形"**，(6273,112) 和 (494019,994) 更是完全未触及。

---

## 2. 2026 年新文献（确认此前情报"两篇 SAT/结构约减论文"）

### 2.1 arXiv:2604.23037 "Approaching the Conway-99 problem using SAT solvers"（Ali Keramatipour，v1 2026-04-24 / v2 2026-04-28）
- 把强正则图搜索编码为 SAT 实例，实测结论：**"we shall see the incapability of SAT solvers facing this problem in a reasonable time"**——即标准 SAT 求解器在合理时间内无法处理，并进一步分析了导致这一困难的数学原因。
- 对称性削减：固定一个顶点，把搜索规约到 142−7=84 个未匹配"顶点对"之间的边——这是后文 Thakkar 论文"84 顶点约化"的先声/同构思路。
- 理论结果：证明 (99,14,1,2) 图不可能遵循 Paley(9) 的模式（Thm 3.4.2）。
- 结论明确：SAT 路线已被专业作者自己判定为当前算力下不可行，不是"没试过"，是"试过且写文章说明为什么不行"。

### 2.2 arXiv:2608.11211 "A Forced-Structure Reduction and Verifiable Bounds for Conway's 99-Graph"（Aalok Thakkar，2026-07-13，投稿至 **CAISc 2026** "Verifiable Problems" track，partial-credit 评分）
- **明确是一个自主 AI 研究 agent 的产出**（论文自述"an autonomous AI research agent"，先用 SMT 后转 CP-SAT 求量级加速）。
- 结构约减（forced-structure reduction）：λ=1 迫使每个顶点的 14-邻域分解为 7 对不相交边（"7-bladed fan"，与 2020 年 straylight 博客独立给出的观察一致）；μ=2 进一步把非邻居顶点与未匹配邻居对建立双射，把问题坍缩为一个 **84 顶点的 12-正则图**子问题——仍然 open。
- 计算结果：①**穷尽证明**ℤ/99 上任何循环图（circulant graph）满足的约束比例不超过 3366/4950=**68.0%**；②CP-SAT 搜索得到的**最佳验证结果 69.43%**（14 种方法中最优）；③框架在小案例 srg(9,4,1,2) 与 Paley/srg(13,6,2,3) 上做了验证。
- 论文原话："any provable bound below 4950 is a non-existence proof"——即若能证明任意图都不能满足全部 4950 个顶点对约束，即完成不存在性证明；但目前只在**受限图类（循环图）**上做到穷尽排除，一般情形仍完全开放。
- **该论文明确"re-scope 到 verifiable bounds，对存在性不做声称（explicit non-claim on existence）"**——没有宣称接近解决。

---

## 3. 自同构群已排除范围（多篇文献叠加，结论收窄很紧）

1. Makhnev & Minakova (2004)：|Aut(Γ)| 整除 2·3³·7·11 = 4158；若 2 | |Aut|，则 |Aut| 整除 42。
2. 2009 年论文"On the (99,14,1,2) strongly regular graph"（经 straylight 博客 <https://maths.straylight.co.uk/archives/1315> 转引核实）：**不存在 11 阶自同构**——由 Cauchy 定理，这直接排除 11 整除 |Aut|。
3. **arXiv:2308.02978**"On the automorphism group of a putative Conway 99-graph"（Cesarz & Woldar，2023-08-06）：精化上述结果，证明**若 7 | |Aut|，则 Aut ≅ ℤ₇（恰好，不与其他因子组合）**；作为推论，**若 2 | |Aut|，则 |Aut| 整除 6，即 Aut ∈ {ℤ₂, ℤ₆, S₃}**。
4. **arXiv:2606.29183**"No involutions in the missing Moore graph"（Yawara Ishida，2026-06-28 提交/2026-07-09 修订）——**注意：此文主题是另一个不同的著名开放问题（Hoffman-Singleton 分类最后情形，度 57 的 Moore 图 srg(3250,57,0,1)，"missing Moore graph"），不是 Conway 99-图本身**。主定理：该 57-度 Moore 图（如果存在）无对合（无 2 阶自同构）。方法是一个新的"trace-rank identity"（源自 p-置换格的 Brauer 商），把素数阶自同构的经典特征标同余关系升级为**精确的秩等式**。摘要明确写"it sharpens known automorphism analyses of **other hypothetical strongly regular graphs**"——即该技术工具**可能**（论文未在摘要给出 99-图的具体新结论，需读正文确认）被用于进一步收紧 99-图的自同构分析,但这**不是**一篇以 99-图为主角的论文，转引时需谨慎，不能算作"99-图自同构再突破"的确证文献。

**净效果**：叠加 1-3（不含存疑的 4），99-图（如果存在）的自同构群阶 **只能是 1、2、3、6、9、27 之一，或恰好等于 7（即 Aut≅ℤ₇）**——已排除 11 及大部分复合阶。**这意味着该图几乎肯定不是顶点传递的**，任何依赖大对称群（循环图、传递设计）的构造搜索从理论上就注定受限——与 §2.1 的循环图上限 68% 实测吻合，是理论结果与计算实验相互印证的一个漂亮例子，但对"找到图"本身没有直接帮助（甚至说明"找钥匙不能靠路灯下"）。

---

## 4. 竞争密度评估

**高，且已建制化**——不是冷门题：

- **Epoch AI FrontierMath "Open Problems" 基准**（<https://epoch.ai/frontiermath/open-problems/conway-99-graph>）把本题正式收录为 AI 模型评测题，给出标准化提交格式（99 顶点、1386 有向边/693 无向边列表）与自动验证器。
- **CAISc 2026**（"Conference For AI Scientists"，Lossfunk + BITS Pilani 联合主办，2026 年 7 月，<https://caisc2026.github.io/>）——一个**专门给"AI 自主科研 agent"投稿的新会议**，设有"Verifiable Problems"赛道、自动验证 + partial-credit 打分。Conway 99-图是其精选题目之一，Thakkar 2026 论文正是投给这个赛道，当前公开最佳分数 69.43%。这意味着**本题已经是一个有排行榜、有标准打分、被多个 AI agent/团队盯着刷分的正式基准**。
- 学界专精代数/群论一侧：Cesarz & Woldar（2023）、Ishida（2026，用到相当深的 p-置换格/Brauer 商工具）持续产出，是窄而专的赛道，非我们这类通才 agent 一两次推理能追上的深度。
- 业余/爱好者一侧：GitHub `caitlin-hutnyk/conway-99`（"hybrid evolutionary algorithm"，附一份课程报告 `drp_final.pdf`，26 commits、2 stars，看起来是学生课程项目，无确认的实质突破，活跃度低）。
- **无"接近解决"信号**：目前最好结果仍停留在"69.43% 约束满足"与"84 顶点子问题仍未解"，没有任何文献声称已逼近存在性或不存在性证明的最后一步。

---

## 5. AI 可解性评估（无本地大规模 SAT 前提下）

**反例侧（构造一个满足全部 4950 个顶点对约束的 99 阶图）**：
- 可验证性完美（Python/Lean 秒级核验度数=14、λ=1、μ=2 对所有 C(99,2)=4851 对成立）。
- 但搜索空间是当前专业 CP-SAT 团队投入后仍只能做到 69.43% 的空间——纯推理/云端 LLM 猜构造，没有现实路径去弥补"专业 SAT/CP-SAT 团队都卡在 30 个百分点缺口"这件事。自同构群已被证明极小（§3），意味着**没有对称性捷径可用**，唯一现实路线仍是大规模计算搜索——恰好是我方已明确停用的本机大算力，云端调用外部 SAT/CP-SAT 服务本质上是在同一个赛道上和已发表论文拼资源，没有信息差优势。

**证明侧（不存在性证明）**：
- 需要①穷尽算力排除（Keramatipour 论文已自证目前 SAT 求解器做不到），或②新的代数障碍把自同构群逼到平凡并延伸为全局不存在性论证。②这条线专业门槛很高（Brauer 商、p-置换格、特征标理论），已有专职有限群论学者在做，即便我们能贡献，大概率也只是渐进式收紧自同构群阶（已经从 4158 收窄到 ≤27 或=7），而非一次性终结存在性——不符合 automath"终结型立项"的选题原则（禁止以边界推进为立项目标）。

**净判断**：本题当前是"算力密集 + 已建制竞争"的组合，恰好踩在我方两个弱项上（无本地 SAT、通才 agent 难以在几周内追上窄专代数赛道两年的深耕）。没有看到任何一条对我方有比较优势的攻击面。

---

## 6. 攻坚建议：**PARK-WATCH**

理由汇总：
1. 非冷门空当——已是 Epoch AI FrontierMath + CAISc 2026 双基准挂钩的正式 AI 竞赛题，有公开排行榜（69.43%），首发/信息差优势为零。
2. 结构约减已经把问题精确卡在计算密集区（84 顶点 12-正则子问题、循环图 68% 上限、CP-SAT 69.43%），这正是我方"退役本地大规模 SAT"新规下最缺资源的战场；云端调用同类求解器没有比较优势，纯推理路线目前看不到能补上 30 个百分点缺口的机制。
3. 剩下的"纯推理"空当（自同构群代数收窄）已有专职群论学者持续产出（Cesarz-Woldar 2023、Ishida 2026），工具专深（p-置换格/Brauer 商），且即便贡献成功也只是边界推进而非终结存在性，不符合选题红线。
4. 无"即将解决"信号，无需抢跑；但也不建议 NO-GO 彻底放弃——若后续出现"CP-SAT 突破至接近 100%约束满足"或"自同构群被证明为平凡群 + 完整不存在性论证"的强信号,应立即重新评估。

**下次重访触发条件**：①arXiv 出现新的 Conway-99 论文声称约束满足率 >90% 或给出完整不存在性论证；②CAISc/Epoch AI 排行榜分数显著跃升；③Ishida 一类的代数工具被明确应用于 99-图本身（而非仅"missing Moore graph"）并给出新的自同构排除结果。建议扫描周期：每 2-4 周一次轻量 WebSearch 复查，不投入主力资源。

---

## 附：核心文献清单（均已直接抓取核实，含 arXiv 号）

| 文献 | arXiv/来源 | 日期 | 一句话贡献 |
|---|---|---|---|
| Wikipedia "Conway's 99-graph problem" | en.wikipedia.org | 最后更新 2026-01-30 | 现状总览，标注仍 open |
| Approaching the Conway-99 problem using SAT solvers | arXiv:2604.23037 (Keramatipour) | 2026-04-24/28 | SAT 求解器实测"无法在合理时间内解决"；证明不遵循 Paley(9) 模式；仅 5 组可行参数 |
| A Forced-Structure Reduction and Verifiable Bounds for Conway's 99-Graph | arXiv:2608.11211 (Thakkar) | 2026-07-13 | AI agent 产出，CAISc2026 投稿；循环图穷尽上限 68.0%；84 顶点结构约减；CP-SAT 最佳 69.43% |
| On the automorphism group of a putative Conway 99-graph | arXiv:2308.02978 (Cesarz & Woldar) | 2023-08-06 | 7\|\|Aut\|⟹Aut≅ℤ₇；2\|\|Aut\|⟹\|Aut\|整除6（∈{ℤ₂,ℤ₆,S₃}） |
| No involutions in the missing Moore graph | arXiv:2606.29183 (Ishida) | 2026-06-28/07-09 | **主题是度 57 Moore 图（不同问题）**；摘要称方法"sharpens"其他假想 SRG 的自同构分析，含 99-图的可能延伸需读正文核实 |
| Constraints on Conway's 99-graph (and its subgraphs) | maths.straylight.co.uk/archives/1315 | 2020-07-08 | 7-bladed fan 结构、特征值 14/3(×54)/-4(×44)、无 11 阶自同构（引 2009 文献） |
| Conway's 99-Graph Problem (FrontierMath Open Problems) | epoch.ai | — | AI 基准题，标准化验证格式（1386 边列表） |
| CAISc 2026 | caisc2026.github.io | 2026-07 | "AI 科学家"专属会议，Verifiable Problems 赛道，本题在其精选题库中 |
| conway-99 (hybrid evolutionary algorithm) | github.com/caitlin-hutnyk/conway-99 | — | 学生/爱好者项目，低活跃度，无确认突破 |
| ON THE STRONGLY REGULAR GRAPH OF PARAMETERS (99, 14, 1, 2) | math.mit.edu/research/highschool/primes (Lou & Murin) | — | PRIMES 高中项目，背景资料（未深入核实） |
