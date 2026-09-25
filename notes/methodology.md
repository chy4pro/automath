# AutoMath 方法论 v1.2（2026-08-16）

目标：尽可能多 × 尽可能有价值 × 尽可能高效地解决开放数学问题。

## 选题策略 v3（用户指令 08-16：影响力优先）

- **有名有姓的著名猜想优先**：命名猜想、有文献引用、业界关注的目标排在前面。名气不再是排除理由——2026 年案例证明有影响力目标恰恰在被 AI 批量突破（Erdős #90 证伪、#1196、AlphaEvolve 破 56 年纪录）
- 评分 = 影响力（命名/引用/年龄/领域关注）× AI 可解性（初等陈述、反例可搜、有限结构、"缺的是技术组合而非新理论"的信号）
- 不要只挑简单的做；相信能力，多轮多角度坚持后再下"部分结果"结论（案例显示持续迭代+鼓励显著提高产出）；solver prompt 应鼓励穷尽多条进攻路线
- **终极命题原则（用户指令 08-16，08-16 修正表述）**：每次攻坚的目标 = 完整证明或证伪最终命题本身，绝不以"边界推进/改进常数/推进特例"为目标立项。边界成果只作为全力攻坚后的副产品记录（副产品可以且应该写论文），攻坚计划书必须写明通向完整解决的路线，目标一定要远大。
  **注意：不存在"只能推边界的题"**（这种分类=能力低估）。命题结构三型及其合规立项方式：
  ① 单发终结型（反例/构造一发定乾坤）→ 直接立项；
  ② 精确值型（R(5,5)、Hadwiger–Nelson）→ 以"定出精确值"立项，收窄不算完成；
  ③ ∀型深猜想 → 按"证伪反例路线"（若有疑假信号）或"通用证明新思路"立项，绝不按参数阶梯立项。
  例：Lonely Runner 两个强化版新近被证伪=疑假信号 → 按直攻反例路线重新入池（而非逐 n 推进）。
- 但**验证纪律与名气同步加严**：越有名，越必须三方独立审查 + 文献查重 + Lean，绝不因兴奋降低门槛
- 猎场：FC 库 Wikipedia/（131 条命名开放猜想已形式化）、GreensOpenProblems/（Ben Green 列表 50 条）、Kourovka/（群论名家问题集——刚验证过群论战力）、WrittenOnTheWallII/、各领域 named conjecture 清单

## 每题流水线（7 阶段）

| 阶段 | 内容 | 执行者 | 通过条件 |
|---|---|---|---|
| S0 分诊 | 读题（FC Lean 陈述 + erdosproblems 页面缓存）；名气/难度过滤（奖金≥$1000、文献厚、著名 → 弃）；OEIS 小案例数值侦察 | Claude（廉价） | 长尾 + 初等方法可及 + 终点可验 |
| S1 文献前查 | T4 prompt，确认仍 open（wiki 停更于 2026-06-30，必须查活状态与 2026 下半年 arXiv） | Claude + WebSearch | 无已解证据 |
| S2 攻坚 | T1 竞赛伪装 prompt，禁联网；falsifiable 题优先做反例数值搜索；多路独立尝试 | Claude 主力；难题加 codex 第二路 | 得到完整证明或反例 |
| S3 对抗审查 | T3 验证器 prompt，Critical/Gap 二分类，连续 ≥2 轮干净 + 1 轮跨模型（codex） | codex（稀缺额度花在这） | 连续干净 |
| S4 文献后查 | T5 prompt，"是否已知"（最高频翻车点） | Claude + WebSearch | NEW |
| S5 Lean 形式化 | 填 FC 现成陈述的 sorry（免自动形式化风险）；lake build；#print axioms ⊆ {propext, Classical.choice, Quot.sound}；T6 陈述保真检查 | Claude 写，编译器裁决 | 编译通过 + 公理干净 + 保真 |
| S6 论文 | LaTeX 写定（papers/）；注明 AI 生成 + 验证链条 | Claude | 完整可读 |
| S7 报告 | 更新 artifact 战报、pipeline-state 记忆、事件日志 | Claude | — |

**问题生命周期（用户指示 2026-08-17：不恋战但不轻易放弃）**：
- active：正在攻坚
- **parked**：暂无进展或额度紧张时挂起，保留完整档案（进展、思路、卡点写入 problems/parked/<题号>.md），有额度/有新想法/新模型上线时重新拾起，绝不一刀切放弃
- retired：仅限"已被他人解决"或"发现根本性障碍（如等价于著名难题）"
S2 卡住 → park（记录卡点）；S3 Critical → 回 S2 修复，3 轮未过 → park。

**多方证明者（用户指示）**：不只 Claude 主证明——codex、ChatGPT 5.6 pro（网页）、qwen3.8-max（网页）都可担任独立求解者；同题多路独立攻坚后交叉比对是高价值模式。

## 模型/额度分工（用户明确要求优化 Fable 用量）

- **Fable 5 主循环（最贵，省着用）**：仅限编排决策、S2 核心证明推理、S3 裁决、关键判断
- **subagent 分层**：文献扫描/网页调研/机械提取 → `model: sonnet`；批量文件操作 → `model: haiku`；数学性强的复核 → `model: opus`。Agent 调用必须显式指定 model，不许默认继承 Fable
- **数值侦察/搜索**：纯 Python/Bash，零 LLM 成本，优先于让模型"想"
- codex 模型阶梯（/model 切换）：sol/5.5=前沿（S3 终审+独立攻坚）；terra/5.4=中档；luna/5.4-mini=廉价机械；**spark=独立周额度**，早轮验证/机械检查优先走它（不耗主额度）
- **免费网页模型（无额度，用尽为止，已登录）**：qwen3.8-max（chat.qwen.ai）、ChatGPT 5.6 pro（chatgpt.com，据称高于 5.6-sol 最高档）——经 Chrome 浏览器自动化驱动，适合大量审查/独立求解；没额度时页面会提示
- 模型多样性原则：S3 验证模型 ≠ 求解模型（跨供应商独立性）；重大成果目标三方独立验证（codex + qwen + gpt-web 任二 + Lean）
- **同源不自审硬化细则（08-18 用户定）**：Qwen 产出的证明不得由 Qwen 审（送 codex Spark/sol 或 opus）；codex/Claude 产出可送 Qwen 审。ChatGPT Pro 节流期（至 08-20）Qwen 为网页主力求解器+审稿人，注意短板：超长单跑自主攻坚无证据、会话易停在生成中途需催、有限流
- **S3 裁判协议三条加固（08-18 采纳自 Anthropic RH 案考古 §8.4）**：①每个裁判分派**具名的特定关节/断言**，不是"审整篇"；②裁判间**禁止互读报告**（独立性而非仅多元性）；③每个关键断言至少一名裁判持**预写好的攻击计划**（"按此路径找错"而非"找找错"）。派发验证前先声明错误先验+两个最可能失败模式；部分结果交付带防火墙语句（模板 T13）
- **Leader 纪律（用户指示）**：Fable 只做编排、证明策略设计、终审裁决；调研/浏览器驱动/Lean 打磨/审查执行全部分派给 subagent 或外部模型
- 额度检查节律：每个工作周期边界看一次（codex /status；claude.ai/settings/usage 看 Claude 侧含 Fable 单独额度条）

## 防假证明三红线

1. 任何"已解决"宣称必须同时有：对抗审查干净 + 文献后查 NEW + Lean 编译通过
2. Lean 通过 ≠ 完成：必须人工核对最终定理陈述与原题一致（防"证了别的东西"）
3. 战报只写已验证事实；未出结果一律 PENDING（不写占位猜测）

## S1/S4 查重源清单 v2（08-18 血泪修订：A114831/Fernandes 双撞车后）

S1 前查与 S4 后查必查以下**全部**渠道（此前只查 arXiv/OEIS/网页，漏掉了主战场）：
1. **FC 仓库 PR（含未合并）**：`gh pr list -R google-deepmind/formal-conjectures --state all --search "<题号/关键词>"`——未合并 PR 也是公开优先权（Fernandes 教训：对方 PR 挂了 5 天，我们全程没看）
2. **FC 仓库 issue**：同上 `gh issue list --search`
3. **竞争者仓库清单**：`gh repo list KitaKen1 --limit 50`（工业化对手，日产多题，模型栈=ChatGPT 5.6 sol + Codex；仓库名即题号，扫一眼即知他碰过什么）；发现新的高产账号随时加入此清单
4. 上游文件当前状态：`git show origin/main:<file> | grep "category research"`（open/solved 直读）
5. arXiv / OEIS 页面 / 网页搜索（原有渠道保留）
选题阶段同理：FC 里 category research open ≠ 无人在做——**必须查该题有无 open PR 与竞争者仓库**再立项。

## 上游贡献纪律（08-18 CLA 实战教训）

- Google CLA 仓库的 commit **不得带 `Co-Authored-By: Claude …` trailer**（[email] 永远签不了 CLA，check 必死；PR #5023 曾因此卡死，amend 掉 trailer 后立即转绿）。AI 披露一律写在 PR 正文/commit 正文散文里（"AI Usage Disclosure: …"，上游惯例）
- commit 作者/committer 一律 chy4pro <[email]>（CLA 匹配+隐私红线）
- 提交后必须确认 CLA check 转绿才算派发完成，不许"提了就走"
- **对外 URL/permalink 必须程序生成+推送前验证（08-18 #5028 事故，用户定为 class fix）**：
  40-hex SHA 与 permalink 一律 `git rev-parse`+脚本拼装，绝不手工拼接（多 PR 批量、相似
  SHA 场景尤其危险）；推送前 `curl` 该 URL 确认 200 且锚定行存在。**CI 全绿不检查链接
  有效性——这正是本次的验证真空**。同种病灶：w133 (R3) 转写事故——手工转写无验证

## 案例情报体系（用户指令 08-16，详见 notes/case_intel/README.md）

- 持续收录全网 AI 解决猜想案例（GitHub/arXiv/X/自媒体/新闻/Zulip），扫描主力=免费网页模型（零额度），每工作日 ≥1 次增量
- **源清单硬性条款（08-18 R3 修订）**：每次扫描必须显式检索**厂商官方研究频道**（anthropic.com/research、openai.com/research、DeepMind 博客）与主流科技媒体聚合——头条级成果最易漏检（Anthropic RH 67.2% 案漏 7 天教训）
- **双检索线条款（08-18 R5 修订）**：每次扫描必须跑两条**独立**检索意图：(a) 发现全新系统名——"过去 90 天各厂商研究页/GitHub 组织有无我们完全未收录的新系统/新论文"（开放式）；(b) 追踪已知系统新动态（关键词复查）。(b) 的高命中率不得挤占 (a) 的检索预算——批量解题类案例的"审美疲劳"漏检教训（AlphaProof Nexus 漏 89 天）
- **已知假信息源排除清单（08-18 intel 发现）**："AI Village News"（gitlab.io）＝自我声明的
  虚构多智能体沙盒，批量生成带逼真模型名/commit hash 的假"猜想解决"报道——扫描命中一律
  排除；同类"AI 生成的虚构成果新闻"源发现即加入本清单（cases.md 收录前必查源性质）
- **陈述-证明作用域双向相等（08-18 双线互证）**：陈述**窄于**证明 ⟹ 漏掉免费的一般性
  （w61 general-s 物种）；陈述**宽于**证明 ⟹ 陈述为假（w133 G32 漏 C4-free——证明的
  "距离-2 对撞 C4"步隐用了该假设，planner 抽核亦隐性中招）。亲核与裁判都必须做
  **statement-hypothesis audit**：逐一核对陈述携带的假设集合恰等于论证实际使用的集合
- **修复文本三物种（08-18 w61 S3 循环实录，供裁判 brief 直接引用）**：①scope-widening
  contagion——加宽一段的适用范围会静默加宽其后每个承接句（K1：k≤1 加宽让下一句在 k=0
  变假，恰复活已撤回断言）；②box-vs-branch——在有界盒上量化的断言被表述成对整个分支
  量化（K2："恰 10 个构型"实为无穷族的盒内切片；F5 物种第三形态）；③ex falso 附句
  ——见下条。裁判 brief 的簿记关节应把这三种列为具名检查
- **陈述附句是独立证明义务（08-18 w61 FAN-F1 教训，planner 亲核同漏）**：定理陈述里的
  "equivalently / in particular / exactly / 恰为" 附句各是**独立的**证明义务——主链矛盾式
  证明只支撑主句；附句若其论证在被反驳的假设下推导（ex falso）即未被证明。亲核与 S3 都
  必须逐句核对定理陈述，不得把附句当主句的搭载品。实例：Theorem FAN 第二句"恰 residue=α−1"
  在 s=τ 反设下推导，被独立裁判抓出，降级为数值观察（280 万序列支持但未证）
- **多 tab 相关性失效（08-18 677 R9-J 教训）**：共享同一 brief 的"独立"tab 会犯**同一个
  静默错误**（实例：三 tab 同时无声采用假的 "WLOG ν=id" 规范化，519/530 反驳）——多 tab
  并行提供的是覆盖多样性而非假设独立性。裁决纪律：对多 tab 收割件必须显式列出并逐条核查
  **所有 tab 共享的隐含假设**；需要真独立性时须变换 brief 框架（不同记号/不同切入面）。
  **补条（w133 G25 教训）**：brief 自带的"已知事实"若非最紧（如"≤1"实为 0），该松弛会无声
  传播进每个 tab——派发前对 brief 事实断言做紧性检查；收割裁决时把"brief 自带假设"列入
  共享假设清单
- **顶级实验室 attempted-未成功 = S0 常设负面难度信号（08-18 R5）**：区别于"已被解决"的排雷——认领目标前查各大系统公开的 attempted 清单（如 AlphaProof Nexus erdos_problems_attempted.txt），命中即在 S0 复核中下调可解性先验（警示非阻断）
- 每次扫描后做**未命中比对**：著名成果我们既没收录也没攻击 → retrospectives.md 强制反思（漏于情报源/选题过滤/能力误判/速度）+ 至少一条方法论修正

## Null-model discipline for empirical gaps (08-18, from 677 R9-F→R9-G lesson)

Before selecting a target (or declaring an obstruction "quantitative / structural") on the
strength of an empirical statistic — e.g. "observed max 6–7 vs required 10" — test the same
statistic against a NULL MODEL (random tables / random assignments of matched size). R9-F
read max|Fix| = 6–7 over 8281 cells as a structural gap; it was the expected maximum of
~Poisson(1) cells at that sample size, and the "gap" vanished at q=2,3 where targeted
search broke the bound immediately (R9-G). Small-max statistics over many cells are
sample-size artifacts until a null comparison says otherwise. Sampler coverage must also
match the claimed branch (R9-F's sampler was narrower than the branch it spoke for).

## 访问纪律

erdosproblems.com：带 UA、低频、页面缓存到 problems/cache/；优先用本地克隆的
problems.yaml 与 formal-conjectures。OEIS 用 JSON 接口低频查询。

## 立项模板二分（08-17 补注，防漂移）
- T1 竞赛伪装+禁联网：适用于单题单发攻坚（防模型识破开放问题拒答）
- CDC 式公开多子代理战役：适用于大型命名目标的持续攻坚（模型知情、多轮迭代、
  工具箱共享）——战役 #1 用此模板，属有意选择而非违反 S2
## 方案文件重读纪律（08-17 用户指令）
每 ~4 个心跳 tick（约 2 小时）或每次上下文压缩/会话重启后，必须重读本文件 +
automath-mission 记忆 + campaign_registry.md 开头目标段，做漂移自检（对照：选题
原则、终极命题、七阶段、模型分工、parked 拾起、案例情报节律），发现漂移当场纠正。

## READY-row freeze discipline (2026-08-22, from the Q32 dispatch race)
A queue row marked READY is a HANDOFF: from that moment the brief file is frozen and
belongs to the driver. Owners must finish all edits BEFORE flipping a row to READY; any
post-READY edit requires first flipping the row back to REVISING (so no driver picks it
up) and bumping a version note in the row. Rationale: qwen-driver-r13 dispatched Q32
twice (v1 13.7KB, v2 15.7KB) and both were stale within minutes because owner-w133 kept
rewriting Problem A and adding facts while the row said READY — two burned conversations
answering superseded statements (correctly flagged NOT-for-harvest). Driver-side rule
stays: byte-diff the source before closing books; stop after one re-send, never chase a
moving target.

## Design-level realizability gate for phantom/abstract instances (2026-08-22, 677 R10-A)
Before ANY fine structure of an abstract/phantom instance is trusted (obstruction sets,
feasibility landscapes, extremal counts), the instance's DESIGN DATA must pass every
proved realizability constraint — in 677's case (R10/REAL-1): g is determined by nu and
the design, not free. R9-K's entire landscape fine structure (max |P|=6, the unique
{1,2,5,6} obstruction) was an artifact of design data no real object carries (nu=id,
g=id forces 7 absolute points; a polarity has exactly q+1=3). This is the design-level
analogue of the model-zoo benchmark filter: "holds on the abstract instance" is zero
evidence until the instance passes the realizability gates. Corollary discipline: every
new PROVED structural lemma should immediately be re-run as a gate over all standing
phantom instances.

## Held-out checks for no-execution API judges (2026-08-22, from the muse-spark Q34 echo report)
New failure species: the FLUENT ECHO REPORT — a well-formed CLEAN verdict whose numbers
are recited from the brief rather than computed. Diagnostic signature (muse-spark Q34):
every brief-printed value correct, every value the judge had to compute wrong (5/7 HH
step counts false while the adjacent brief-printed residues were all "OK"; a padding
scope that fails its own multiplication, mixing a pre-repair 480 with a post-repair
18963). Planner hand-verified the C5/C6 step counts (3,4) against the report's (2,3).
The fuller the brief, the easier this failure hides — import-completeness widens the
echo surface. STANDING RULE: every brief sent to a judge that cannot execute code MUST
(a) demand an explicit execution-environment declaration up front, and (b) carry
HELD-OUT CHECKS — a few values the reviewed text implies but the brief deliberately
does not print, demanded in a mandatory table. Echo-vs-compute then becomes decidable
at adjudication. A report that fails its held-outs is VOID as a round regardless of
verdict quality elsewhere.

## Name-the-map-you-invert clause (2026-08-22, 677 r11b post-mortem)
Six of eight volume-engine attack briefs died of ONE error family: silently inverting a
branch map that is not a bijection (R_{nu(v)} as a table column; row-vs-column confusion
in D). STANDING brief-design rule for attack briefs (all engines): any step that inverts
or transports along a map must NAME the map and JUSTIFY bijectivity (or restrict to the
fiber actually used). Adjudication shortcut: check the inversions first — they are the
cheapest kill.

## Cycle-to-path counting clause (2026-08-22, w133 D3 sweep post-mortem)
Second engine error family (distinct from map-inversion): walking all k vertices of an
induced C_k as if they formed an induced path — forgetting the closing edge. An induced
C_k yields a longest induced path on k-1 VERTICES. STANDING RULES: (a) any brief that
carries a "this induces a C_k" fact must print the k-1 sentence verbatim; (b) on such
briefs adjudication checks cycle->path steps FIRST (D3_A and D3_C both died there,
zero compute needed).

## Unswept-citation partial repair (2026-08-22, WOWII-61 round 15 pre-dispatch catch,
notes/proofs/wowii61_draft.md §7.30 — OUR species, observed in our own line, not
FAR-derived)
New failure species, distinct from the three "repair text" species above and from the
fluent-echo-report species: a repair that fixes the SITE where a defect was found but
leaves other citations of the same repaired object untouched elsewhere in the same
document. WOWII-61 round 15's "Repair AC1b" removed a mismatched import at one citation
site, but two further citations of that same import survived (§7.22 (c-1) item 5, and
the honest-demarcation bracket at §7.13 D / (c-6)) and both would have reached the
outgoing brief unchanged — dispatching as-was would have handed a cross-family judge the
identical mathematics defect at a second site, burning a scarce judge round. The same
class-vs-instance confusion (logged there as AC3) had already recurred in the same
document one round earlier — twice in two consecutive rounds, not a one-off. STANDING
RULE: a repair is not complete until the WHOLE document has been swept for every other
citation of the repaired object, and the sweep result is recorded explicitly — including
when it is clean, because a clean sweep is cheap evidence. Fixing the site where the
defect was found is the start of the repair, not the end of it. Any brief that reports a
repair must include this sweep as a mandatory line item, alongside the existing named
species (scope-widening contagion, box-vs-branch, ex falso appended clauses,
map-you-invert-not-named, cycle-to-path-off-by-one, fluent-echo-report), so a brief
author can point at it by name.

## Competitor case intel: FAR pipeline (2026-08-22, arXiv:2608.16977; full read in
notes/case_intel/far_pipeline.md)
(a) FAR ("Find-Attempt-Recommend") is a literature-mined, industrial-scale
conjecture-discovery pipeline (Zheng, Zhang, Avigad, Tetali, Welleck). Its funnel on an
unscreened, single-direction ("combinatorics") arXiv pool: 51,110 papers → 5,245
in-domain → 6,453 candidate conjectures → 4,717 confirmed open → 1,050 claimed NEW → 598
judged PASS → **77 publishable (1.6% of the open pool)**.
(b) FAR runs Solve, Judge, AND Grade all on the same model (gpt-5.5 at xhigh reasoning
effort) — this is precisely what our **同源不自审** rule (08-18) forbids. Name this as
the concrete critique if we ever cite or compare against FAR publicly, and treat it as a
standing reminder to keep enforcing our own cross-provider requirement ourselves.
(c) FAR has **zero formal/compiled verification anywhere** in its pipeline — every gate
(Solve self-audit, Judge unanimity, Grade lit-recheck, final human read) is
natural-language judgment; its strongest objective check is "authors hand-reviewed
15/77, found 0 errors," a sample, not a mechanized guarantee. Our S5 hard-gate (Lean
compile + `#print axioms ⊆ {propext, Classical.choice, Quot.sound}` + statement-fidelity
check) is our clearest quality moat versus FAR's approach and should be defended, not
traded away for throughput.
(d) FAR allocates exactly **one attempt per conjecture** ("the initialization step of a
bandit algorithm"); multi-pull is explicitly named as future work. Our multi-tab/
multi-model escalation on hard targets (S2) is already standing practice, not a
future-work item.

NOT adopted in this slice (planner handling separately, see
orchestration/tasks/methodology_far_integration.md §4 items 1/2): FAR's corpus-scale
literature-mining sourcing pipeline (Label→Extract→Check) as an alternate target source,
and AUC-style post-hoc calibration of our own TARGETS.md 影响力×可解性 scores against
realized outcomes.

Watch registrations for FAR and a second named competitor (pipeline-math): see
orchestration/watch_ledger.md competitor-watch section and notes/case_intel/cases.md.


## ⭐ VERIFICATION DOCTRINE — consolidated 2026-08-22/23, see `notes/verification_doctrine.md`
That file is the durable home for the rule set this project earned in one night across three
mathematical lines and eight target-selection gates. It is organised by theme, and **every rule
carries the failure that bought it** — a rule whose cost is remembered survives a handover; one that
arrives as received wisdom gets quietly dropped. Read it before writing any brief, held-out table,
verification script, or ledger entry. One-sentence version: **arithmetic goes under machine check,
not under reading.** Full reasoning per rule: `orchestration/planner_msgs/`.

## 上游贡献纪律补条（2026-08-24，用户批准后立）
**Requested-changes 完成后 24 小时内必须触发复审通知**：回复里写 "Done" 不进 reviewer 的
通知队列。顺序：①API re-request review（fork 作者常无权限，404 即放弃）→ ②一句礼貌
@-mention 评论（本次实操模板见 PR #5023/#5027/#5029 2026-08-24 评论）。此后每次 ping 间隔
≥5 天，最多两次；两次无响应改为等待并在 watch 台账降级关注频率。背景教训：三个 PR 改完
惯例后静默 5 天掉出注意力队列，而仓库同期在活跃合并快审类 PR。
