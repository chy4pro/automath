# Parked 问题例行重访（2026-08-17）

方法：读 problems/parked/README.md + 各题在仓库内的既有记录（notes/fc_catalog.md、notes/reviews/、
lean/proofenv/、problems/recon/）交叉核对；每题 1-2 次 WebSearch/WebFetch 做 S1 现状刷新，
重点核查"我们 park 期间是否被他人（尤其 DeepMind AlphaProof Nexus）解决或蚕食"。纯评估，未攻坚。

## 重大发现（先说）

1. **fernandes-2gen 实为记账错误——题目已经解决，不是未开工。** `lean/proofenv/Fernandes.lean`
   开头逐字写明"Formalisation of Conjecture 1 of arXiv:2605.12342"，`conjecture_1` 定理签名
   与 formal-conjectures 原文逐字节一致，`grep sorry` 零命中，`#print axioms` 干净；
   pipeline-state 记忆 2026-08-16 已记为"🏆 旗舰定案"且论文/Lean 全部完成。这与
   parked/README.md（2026-08-17 建档）里"fernandes-2gen…未开工"矛盾——建档时漏查了前一天
   刚完成的旗舰成果。**应从 parked 列表移除并标记 DONE，不是重启候选。**
2. **DeepMind AlphaProof Nexus（arXiv:2605.22763，2026-05）是活跃头号竞争者**，已解 9/353
   Erdős 题、44/492 OEIS 猜想，且其结果仓库 `google-deepmind/alphaproof-nexus-results` 直接
   碰过我们两个 parked 题的同一 Lean 落点：
   - `a211417-bala`：`APNOutputs/OEIS/oeis_a211417_conjecture_specific.lean` 证的是 **r=1
     特例**（D(1)=1，即 30n−1 | a(n)），formal-conjectures 里的一般化定理
     `general_divisibility`（对所有 r 的 D(r)）**仍是 sorry，仍开放**——但已被同一竞争者
     摸过同一文件，存在被扩展到一般 r 的时间压力。
   - `krenn-gu-n6d3`：2026-07-23 AlphaProof Nexus 在 Lean 里证明了 **D≥N 区制**下无解
     （如 N=6,D=6），但这是与我方目标不同、且更容易的渐近区制；`eqSystem6_no_solution_d3`
     （我方目标 N=6,D=3，D<N 的 Gröbner 密集区）**仍是 sorry，仍开放**。同样是同一文件族被
     竞争者持续耕作的信号。
   - erdos_problems_attempted.txt 核查：287、488 均**未出现**在 AlphaProof Nexus 已攻列表中，
     无直接冲突。
3. **a63880-mod216 也存在"未开工"记账偏差**：`notes/reviews/a63880_codex_solve.md`（08-16，
   codex 产出）已完整证明"m 无平方因子情形 ⟺ n=108m"（因式分解 (2A−7)(2B−6)=48 的证书式论证）、
   给出精确 2-adic/3-adic 约束（式 6、8）、且穷举验证到 10¹²（2,158,390 例，见
   `problems/recon/a63880_verify.log`）。真实卡点是"非平方自由 powerful core（含 ≥5² 因子）
   情形是否存在第二个本原解"，而非"未开工"。README 描述需更正为"部分结果"。

## 逐题表

| 题 | 卡点（原档案） | S1 新情报（2026-08-17） | 解卡评估（新资产能否用上） | 建议 |
|---|---|---|---|---|
| erdos-287 | 社区证书链 n1>3.99e19；完整证明疑需好素数无穷性 | WebSearch：erdosproblems 论坛显示仍 open，无新解出信号；无 287 专属 2026 新文献命中 | 新资产（77/176 磁盘模型、shift-ansatz、star-forest 引理）均为 ETP 磁群专用，与解析数论"好素数无穷性"无关；不解卡 | KEEP-PARKED |
| erdos-488 | Tao 卡在筛法振荡不等式；特例已被他人证完 | WebSearch：确认 Aristotle+Cambie（2025-11）已给出反例并推动题面被 erdosproblems 修改；2026 年内无新进展迹象 | 振荡不等式瓶颈需解析数论/筛法专精，新资产不适配；且题面已改版，重启前须重读最新陈述避免打旧靶 | KEEP-PARKED |
| fernandes-2gen | Γ_{m⊕n} 2-生成（arXiv 2605.12342 Conj 1）；未开工 | （非 S1 议题）本地交叉核实：**08-16 已全链路解决**（Lean 507 行 0 sorry + 论文），parked 建档滞后一天漏记 | 不适用——已解决 | **RETIRE**（移出 parked，标记 DONE，非重启候选；建议顺手修 README 记账） |
| a63880-mod216 | σ(n)=2σ*(n)⇒n≡108(mod216)；未开工 | WebSearch：OEIS 页仅确认社区旧观察（Wilson v. 2003，10⁷内），无人给出一般证明或反例 | 本地已有部分定理（squarefree 情形完全证明+2/3-adic精确约束+10¹²穷举），卡点收窄为"非平方自由 powerful core 情形"——ETP 专用新资产不适配，但这是有界的 p-adic 案例分析，正合 GPT-5.6 Pro 多会话 + T9-T11 prompt 模式的专注窗口打法；且"快赢批清空后"重启条件已于 08-17 满足（batch1 首批全定案） | **REACTIVATE-now** |
| crystals-unique | 双调和平均"晶体"分解唯一性；未开工 | WebSearch：仅命中 2016 原论文，无后续进展或解出报道 | 初等数论代数问题，新资产不直接相关；无竞争/时效压力信号 | KEEP-PARKED |
| a211417-bala | Bala D(r) 整除性猜想；未开工，需 p-adic 专注窗口 | WebSearch+仓库核查：**DeepMind AlphaProof Nexus 已碰同一 OEIS 条目**，但只证了 r=1 平凡特例，一般 D(r) 猜想仍 sorry；同期另有独立论文证 Bala 另一序列 A028342 的同类猜想（arXiv:2607.18313, 2026-07），显示 Bala 猜想族正被多方活跃攻克 | 卡点本身就是"p-adic 细算专注窗口"——不需要 ETP 专用新资产，用 GPT-5.6 Pro/opus 把 r=1 的 (2A−7)(2B−6)=48 式论证套路推广到一般 r 是自然延伸；**竞争窗口正在收窄，建议尽快占位** | **REACTIVATE-now**（最高优先级——直接竞争信号最强） |
| a103425-tribonacci | 无素数加权 tribonacci 是否存在；需覆盖同余系构造窗口 | WebSearch 无命中；AlphaProof Nexus OEIS 产出列表核查（37 个文件）**不含 A103425** | Graham 1964 覆盖同余系技巧是专用构造技能，与新资产（ETP/graph 系）不重叠；无竞争压力 | KEEP-PARKED |
| krenn-gu-n6d3 | 量子图 N=6,D=3 非存在性；Gröbner 计算量大 | WebSearch+仓库核查：AlphaProof Nexus 2026-07-23 已用 Lean 攻克 Krenn-Gu 同族问题，但只证了 D≥N（易）区制（如 N=6,D=6），我方目标 D=3(<N=6) 的 Gröbner 密集区仍 sorry、未被触及 | 卡点是重 Gröbner 基计算，与我方"退役本地大规模计算"新规直接冲突；star-forest 引理等新资产表面图论相关但机制（自指幺半群表 vs 完美匹配权系统）不同构，迁移性存疑；"计算资源充裕的窗口"条件仍未满足 | KEEP-PARKED（watch：同题族被同一竞争者持续耕作，若其转攻小 D 区制需立即重估） |
| conway99 | srg(99,14,1,2) 存在性；SAT 密集+建制化竞争 | 本题当日（08-17）已有独立新鲜 S1（problems/recon/conway99_s1.md）；本次补充 WebSearch/WebFetch 核实无新进展——Thakkar arXiv:2608.11211（CAISc2026 排行榜 69.43%）仍是 SOTA，未见存在性/不存在性声称 | 无变化，PARK-WATCH 理由仍成立 | KEEP-PARKED（维持 2-4 周复查节律） |

## 建议行动摘要

- **立即修正记账**：fernandes-2gen 从 parked 列表移除（已解决）；a63880-mod216 描述从"未开工"
  改为"部分结果+精确卡点"。
- **REACTIVATE-now ×2**：a211417-bala（竞争信号最强，DeepMind 已碰同一文件）、a63880-mod216
  （已有强部分定理+重启条件已满足）。两者都适合"p-adic/数论专注窗口"打法，不依赖 ETP 专用新资产。
- **KEEP-PARKED**：erdos-287、erdos-488、crystals-unique、a103425-tribonacci、krenn-gu-n6d3、
  conway99——均无解卡新信息或新资产不适配；krenn-gu-n6d3 需额外标注竞争耕作 watch。
- **RETIRE**：fernandes-2gen（已解决，非放弃）。
