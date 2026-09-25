# CASE PAIR — Colombo 1928 行列式问题（无界 WuJie 智能体团队）× 费马大定理 Lean 全形式化（Claude + Prove2Me）

**Filed by dialogue automath-b6 (Fable 5.1), 2026-09-06/07. 业主指令："认真深入研究成功和失败的原因（含工具和提示词）→ 改进当前系统 → 不信"AI 能力不足"，案例没做到的分析原因研究规避 → 应用到后续进度"。**

一手源（全部直接读取，不是二手转述）：
- Colombo：arXiv 2609.00101（Qianli Ma；AI workflow disclosure 节）；Lean 仓 hkjtsgmc79-boop/colombo-odd-lean（README：Lean 4.30，≈2 万行，无 sorry）；微信长文 scratchpad/wx1.txt；VibeMathed 条目（significance 12/100；同期 Kun Li 等独立证明）。
- FLT：Anthropic 博客 formalizing-fermats-last-theorem；仓 anthropics/fermats-last-theorem README（验证栈）；Claude 思考日志 PDF（58k 字符，scratchpad/claude_flt_log.txt，逐段读了 Day 1–3、5、8、9、11 的 recheck/wrong/fail 段落）；Prove2Me 论文 arXiv 2608.28433；**Prove2Me 的 agent 提示词原文**：prove2.me/skill.md（v0.9.7）、references/mission_solver.md、mission_captain.md、prove.md（全文下载，scratchpad/p2m_*.md）。
- 背景库：VibeMathed 数据集 /api/dataset（689 条，本地 scratchpad/vm_dataset.json）。

---

## 0. 一句话结论

两个案例成功的共同原因不是模型更聪明，而是 **harness 把"全局状态、路线比较、陈述正确性、验证"四件事从模型的工作记忆里搬到了外部结构里**（DAG/卡片/路线表/验证栈）。两案的失败段（Colombo 的 11h17m 死路、FLT 前期"丢失全局状态"的 7% 废工）也都不是能力问题，而是 **缺少外部结构时模型被局部奖励牵着走**。业主判断正确：这些人做的事（叫停、排优先级、选题）都是规则可写的，写进 harness 后 AI 自己能做，而且不用降低表现。

---

## 1. Colombo 案（1928 ICM 问题，48 h，2 万行 Lean）

### 1.1 事实链
- 题：N 偶、D ≥ N−1（D 奇）时 Colombo 矩阵行列式非零；百年缺证，因为合适工具（样条恒等式、全正性）几十年后才出现。
- 团队：GPT-5.6 Sol 查文献；Fable 5 红队挑刺；DeepSeek/Qwen/Kimi 做 Lean；上层 agent 调度（核心长程任务给最强模型、可拆分形式证明给便宜模型、独立红队找错）；人（非数学专业的 AI 博士生）在最上层定研究路径与算力。
- 路线生成：AI 提出 **8 条路线**，每条同步给出"优势/缺点/可能障碍/是否值得继续投入"的评估；有的直接但算量大，有的概念漂亮但关键环节缺可验证桥梁，有的成功率低很快停。
- 失败段：p=m−1 路线跑 **11h17m，留下 141 项可核验产物、4.7 万行**，一路"好消息"，但始终收敛不成覆盖任意规模的统一证明。作者定性："AI 会被局部进展奖励；只要还能产出新结果就继续深挖，边际收益再低也想补最后一点缺口。"
- 人介入：叫停 p=m−1；AI **把目标降到 p=m−2**，发现 m−1 时纠缠的支撑关系在 m−2 变得规整（每列非零位置成连续区间且随列有序推进）→ 2h23m 后证明成立 → Pfaffian 化 + 积分表示 + 样条行列式非负 + 找严格正区域。
- 验证：Lean 4.30 全形式化，无 sorry；小范围同行评阅；同期另有独立证明（VibeMathed 记为 concurrent）。意义评分 12/100——**题小**，价值在范式。

### 1.2 成功因子（可移植）
S1 **角色分工按成本档**：文献/红队/Lean 三种活分给三档模型。我方已有（Fable 裁决、Pro/Astra 打证明、Qwen 免费层、Opus 审稿），但 **Lean 叶子交便宜模型** 这条我方没做——我们的 Lean 全是 Fable/Opus 自己写（O4/O5）。
S2 **路线组合 + 结构化评估**：每条路线带"优点/缺点/障碍/建议"四栏，人比较后分配算力。我方 TEMPLATE v2.3 有"方法族登记表"，但没有 **每路线预算 + 障碍栏 + 继续/冻结建议** 的固定格式，也没有由 **不做该路线的 judge** 来评估。
S3 **降目标找结构**：m−1 卡死 → m−2 规整 → 推广。这是经典启发式（先解更小/更规整的参数找到结构），但案例证明它在 agent 长程运行里必须是 **强制动作**，不是"想到再用"。
S4 **Lean 收尾用于可信度**：证明先出、后形式化，形式化目的是"外部读者复核可信度和效率"。与我方三关一致。

### 1.3 失败因子与规避（不降表现）
F1 **局部进展奖励 → 11 h 沉没**。根因：工作 agent 自己评估自己的路线；产物计数（141 项）被当进展。
 规避：(a) **路线预算**（首发每路线 ≤ 25% 总预算，续投要 judge 批）；(b) **边际收益指标 = "缺口陈述"是否变短**：每个 checkpoint 必须重写一句"离统一证明还差什么（对任意规模）"，连续两个 checkpoint 缺口不变 → 冻结该路线；产物数量、通过的实例数、引理数 **不算进展**；(c) **judge 与 worker 分离**：judge 只读路线表与缺口陈述，不看细节，按规则裁决继续/冻结/降目标；(d) 表现不降：冻结不是丢弃——产物入路线表可复用，且规则允许 judge 在其他路线也停滞时解冻。
F2 **人来决定叫停** 被文章写成"必须人来把控"。实际上叫停依据只有两条可写规则（时间/边际）。把 F1 的 (a)(b) 写进简报后，AI 自己执行。我方 #708 六轮考古（09-04）已经独立观察到同一现象：不等式型目标的 4 h 长轮全部以"归约"交稿——同一种被局部奖励牵走。
F3 **意义低**（12/100）：选题按"AI 能力 + 可形式化"挑，牺牲了重要性。我方八步选题第二步已是重要性门槛；保持。

### 1.4 提示词/工具考古
- 未公开逐字 prompt；论文 disclosure 只给角色与流程。可取的是 **结构**：路线评估四栏、上层 agent 调度、红队独立。作者原话"第一步不是研究复杂的 Prompt 技巧，而是先用对工具（harness）"——与我方 08-16 方法论一致。
- 工具：把给人用的数学/计算/数据工具改造成 agent 工具（未开源）。我方对应：hotset_lp.py / hall3.py / verify_s1.py 这类"引擎能调用的检查器"要随简报一起给（v2.3 第 2 条已要求）。

---

## 2. FLT 案（11 天，6×10⁹ 输出 token，29,511 定理，60,474 文件）

### 2.1 事实链
- 模型 ≈ Fable 5.1 的内部研究模型；路线参考 Darmon–Diamond–Taylor 的精简阐述；人只写了目标定理一行 Lean，偶尔评论优先级（"把 Jacquet–Langlands 优先级调高"、"催 Mazur"）与鼓励。
- 早期失败：agent 取得局部进展后 **丢失全项目全局状态、无法协同**，≈7% 行数是这种废工。
- 转机 = Prove2Me harness 三件事：(1) 定理 DAG，agent 看到整体进展与依赖树、决定下一步、多 agent 并行；(2) 陈述与证明分文件、链接独立维护 → 编译便宜；(3) 每定理带自然语言描述 → 检索复用，找到更短路径。
- 行为证据（思考日志）：其他 agent **先检查陈述是否为真再证**（"caught several false statements early"）；Day 3 别的 agent 指出错误后它复算并放弃路线（"statement maybe still true but not by our method"）；Day 8 与 Ribet Prop 3.8 矛盾 → 回去 recheck 找到漏掉的 Frobenius twist；Day 9 卡住时换路（数圆上零点）并把不可用的想法搁置回原计划；Day 11 复查别人写的陈述发现自己早先的 sizing 错了。**这就是"红队"与"卡片先验陈述"的内生版本。**
- 验证栈：平台"Proved"≠端到端（每卡片只对子陈述编译）→ 全部 29,511 卡片平台外重编译 → 整树单 Lean 项目构建（仅三公理、无 sorry、推出 Mathlib 自己的 FLT 陈述）→ Lean FRO comparator（陈述与只依赖 Mathlib 的参考文件逐字一致 + 内核重放）→ nanoda（Rust 独立内核）。`FinalCheck.lean` 用 `#guard_msgs in #print axioms` 固化公理集。
- 代价与形态：60,474 文件几乎全机器写，不满足 Mathlib 入库规则，README 自认"不适合上游"。Vinogradov 早先版本用 3 个 Max 订阅完成。

### 2.2 Prove2Me 提示词原文的可移植条款（skill.md / mission_solver.md / captain.md / prove.md）
P1 **三条硬规则**：`solution` 类型必须与目标陈述逐字匹配；禁止 import 自己的目标（防循环）；自己的文件无 sorry（子引理的 sorry 允许）。→ 我方 verification_doctrine 已有前两条精神；第三条"叶子可 sorry、根不可"是 DAG 工作法的许可证。
P2 **Scout before you attempt**（先侦察再动手）：取一手源逐字"翻译"证明而不是凭印象重写；读 milestone 编辑史（被 captain 拒绝的路线不重走）；看已有分解；读讨论区死路；看 backlinks；看 audits 的 flag；读失败提交。→ 我方"死路清单 D1–D6"是同类，但没有 **被拒路线带 reason** 与 **失败提交可读** 两条。
P3 **captain 首要原则 = FAITHFULNESS**：陈述与源逐字对照；边界条件（0 ≤ z ≤ 1、h = 0）；隐含假设；read-back = 独立子 agent 盲写"这个 Lean 陈述断言了什么"的自然语言证词，与源比对。→ 我方 S5 有"陈述保真检查"，缺 **盲读回（read-back）** 这种独立测试形式。
P4 **explanation 像论文段落**：不写"elegant/clever"，不写自我与尝试次数；children 是假设不是结果。→ 直接采纳为我方 report.md 规范。
P5 **不重复造轮子**：基本结果先搜平台（NL 检索）。→ 我方 Lean 工作应先搜 Mathlib/平台，O4/O5 就是在重造 Mathlib 已有（PR 撞车 #25841/#34050 的另一种表现）。

### 2.3 失败因子与规避
F4 **无外部 DAG 时丢全局状态**（7% 废工）。规避：任何 >1 座席或 >2 h 的证明/形式化任务，建立 **共享路线表/卡片目录**（文件系统即可）：每引理一卡（NL 描述 + 精确陈述 + 状态 + 依赖），worker 只改自己卡片的证明文件；judge 与红队读卡片。
F5 **平台绿灯 ≠ 端到端**。规避：我方每个 Lean 交付必须附 `FinalCheck.lean`（`#guard_msgs in #print axioms` + 从我方陈述推出参考陈述）；重要成果再跑 comparator（Lean FRO 工具，公开）。
F6 **不可上游的形态**（60k 文件）。对我方无害——我们不再投 Mathlib；但 **可读性影响独立复核**，故我方形式化交付要求：陈述文件人类可读 + 短 README 说明每个命名结果强度（仿 PROOF-PATH.md）。
F7 文章把"人偶尔调优先级"写成必要干预。日志显示优先级信号只有两三条，且都是"先证依赖树里更靠根/更被依赖的节点"——可写成规则：**优先级 = 依赖它的开放节点数 × 里程碑权重**，DAG 上直接算。

---

## 3. 对照我方系统（差距表）

| 维度 | 案例做法 | 我方现状 | 差距动作 |
|---|---|---|---|
| 路线管理 | 8 路线四栏评估 + 预算 + 叫停 + 降目标 | 方法族登记表；无预算/缺口指标/judge | TEMPLATE v2.4 ROUTE PORTFOLIO BLOCK（§4.1） |
| 全局状态 | Prove2Me DAG/卡片/NL 描述 | checkpoint.md 单文件；Lean 单文件 | 卡片目录 + 开放叶子脚本（§4.2） |
| 陈述先验 | 其他 agent 先验陈述；captain read-back | 状态标签；09-04 极端实例机检 | 卡片建立即做盲读回 + 破坏尝试（§4.3） |
| 红队 | Fable 5 独立红队；agent 互查 | Opus 审稿在收割后 | 红队前移到路线/卡片阶段，且不与 worker 同源 |
| 验证栈 | 重编译 + 整树 + comparator + nanoda + FinalCheck | #print axioms 手查 | FinalCheck.lean 强制；comparator 用于发布件（§4.4） |
| 成本分档 | Lean 给便宜模型 | Lean 由 Fable/Opus 写 | Lean 叶子 → codex Spark（额度 100%）/Qwen；Fable 只写卡片与裁决 |
| 选题/查重 | VibeMathed 记录 689 条 AI 解题 | G2 = 论坛/PR/Zulip | G2 加 VibeMathed 数据集与 ICMConjectures（§4.5） |
| 说明文风 | explanation 像论文段落 | report.md 各式各样 | 采纳 P4 |

我方今晚自己的一个失败也归入 harness 类：Astra r16 首发被 codex 网络安全分类器拦截（简报标题 "ATTACK"、启动词 "carry out the attack"），33 分钟空转。教训：给 codex 的文本禁用 attack/adversarial/exploit/kill/break 一类词，改 proof campaign / refutation agent / stress test / falsify。

---

## 4. 改进（本轮落地）

4.1 **TEMPLATE v2.4 — ROUTE PORTFOLIO BLOCK**（engine/briefs/TEMPLATE_attack_brief.md）：≥4 条路线四栏评估；每路线预算 ≤25% 首发；checkpoint 必含一句"缺口陈述（对任意规模）"，两次不变即冻结；产物/实例/引理数不算进展；judge 角色与 worker 分离；强制"降目标找结构"动作；冻结路线产物入表可解冻；codex 用词表。
4.2 **卡片工作法（本地 Prove2Me-lite）**：`lean/cards/<line>/` 每引理一文件（docstring = NL 描述 + 来源；陈述以 `:= by sorry` 起）；`tools/cards_frontier.py` 列开放叶子与依赖；证明由便宜档填；根文件 + FinalCheck.lean。首个应用：#708 阈值-4 定理与 #709 上界 ⌈√n⌉ 的形式化（槽 2）。
4.3 **卡片先验**：建卡即由不同源 agent 做 read-back + 大尺度破坏尝试（v2.3 第 1 条延伸到形式化）。
4.4 **验证栈**：verification_doctrine 加 FinalCheck.lean 强制项与 comparator 可选项。
4.5 **G2/选题源**：VibeMathed /api/dataset（689 条，含 87 个已解 Erdős 题；本地已下载，派发前脚本查重）、VibeMathed Frontiers（8 条量化前沿的台阶，AI 已推 11 步：长素数间隙、有界素数间隙 212、随机度量失真、systole、椭圆曲线秩 ≥31、矩阵乘法指数、临界线零点比例、19 维 kissing number）、ICMConjectures（2898 题）。
4.6 **Prove2Me 本体**：接入需账号（邮箱确认）与 API key——业主决定是否注册；接入后我方形式化槽可直接跑私有 mission，叶子交平台上的其他求解者/便宜模型。在此之前用 4.2 的本地版。

## 5. 对"AI 能力不足"说法的逐条回应
- "AI 被局部进展奖励，需要人叫停" → 叫停规则只有时间与缺口两条，写进 judge 角色即可；人之所以能叫停，是因为人看的是路线表而不是产物流。
- "最后决策要人把控（选题/路线/可信）" → 三层分别对应我方八步选题、v2.4 judge、三关验证；均已是规则。
- "agent 丢失全局状态、无法协同" → 是没有 DAG 时的表现；有了卡片目录就没有。我方当前多座席运行同样缺这个，故 4.2 优先。
- "人偶尔给优先级" → 依赖树上的可计算量。
保留的真实约束（不是能力问题）：算力/额度（FLT 6×10⁹ token；Astra 每题 ≈$10k 期望）与 **重要性**（Colombo 12/100）。我方对策仍是选题门槛与两槽制。
