# 核实：Crouzeix 猜想是否已被 AI 解决（2026-08-16 核实）

**来源线索**：sweep1 扫描带回的待核实条目"Crouzeix 猜想 AI 证明（Jin 2026）"（见 scan_log.md 2026-08-16 上午条）。

## 结论（Verdict）

**RESOLVED（强证据支持，尚未走完期刊同行评审）**——不是谣言，"Jin" 确有其人：**Shanmu Jin（金善木音译，北京协和医院神经外科住院医师/博士后）**，用 ChatGPT（GPT-5.6 Sol）自主跑了约16小时给出证明思路，2026-07-27 发预印本；8天后 Lorist & Schwenninger 用完全不同方法独立给出第二个证明（2026-08-04，arXiv）。原猜想提出者 Michel Crouzeix 本人已亲自核对并认可 Jin 的证明正确。距今仅约2.5周，尚无期刊发表/形式化同行评审，但已有双重独立证明+领域权威背书，可信度很高。

## 时间线

| 日期 | 事件 |
|---|---|
| 2004 | Crouzeix 提出猜想；同年证明 ‖p(A)‖≤11.08·sup\|p(W(A))\| |
| 2007 | Crouzeix 证明常数可到某界（论文列出11.08版本） |
| 2017 | Crouzeix–Palencia 证明常数 1+√2≈2.414（SIAM J. Matrix Anal.） |
| 2017-07-31~08-04 | AIM（美国数学研究所）在 San Jose 办 Crouzeix 猜想专题工作坊（Embree/Overton/Greenbaum 组织） |
| **2026-07-27** | **Shanmu Jin 发预印本《The Numerical Range Is a 2-Spectral Set》**，preprints.org/manuscript/202607.1919（后出到 v4，2026-08-07） |
| 2026-07-30 | Alex Townsend（康奈尔）例行用 ChatGPT 5.6 问该猜想，AI 主动链接到 Jin 的预印本 |
| **2026-08-04** | **Emiel Lorist & Felix Schwenninger 独立发表第二个证明**，arXiv:2608.03841《A solution to Crouzeix's conjecture》，方法不同（双层势表示+2-dilation 扰动引理），5页，同样披露用 GPT-5.6 探索过证明策略 |
| 2026-08-14 | Townsend & Greenbaum 联名发表 SIAM News 文章《The Neurosurgery Resident Who Proved Crouzeix's Conjecture》，确认"两位作者本人及 Michel Crouzeix 本人都已仔细核对，认为 Jin 的手稿是对的" |

## 关键信息核实

- **AI 角色**：Jin 用了改编自 OpenAI 攻克 Cycle Double Cover 猜想（见本项目 cases.md 2026-07-10~14 条，当时标注"未经同行评审/未Lean，WATCH"）的同款 prompt 风格——禁网络访问、多子agent分支探索、禁止过早收敛、对抗式审查、不许在证明扛住检验前放弃。GPT-5.6 Sol 在 ChatGPT Work 模式下自主运行约16小时产出关键定理（其预印本 Theorem 2）的证明思路。
- **验证方式**：非正式但重量级——猜想原提出者 Michel Crouzeix 本人核实 + Townsend/Greenbaum 核实 + 独立第二证明（Lorist & Schwenninger）殊途同归。Jin 的 GitHub 仓库（github.com/jinshanmu/CrouzeixConjecture）公开了手稿、Lean 4 形式化 + axiom audit、prompt 原文、AI 对话记录，"多轮独立计算/对抗审计未发现具体数学错误"，但**正式同行评审尚未完成**。
- **与背景信息比对**：用户给出的背景（1+√2 常数来自 Crouzeix–Palencia 2017，猜想常数为2）与 SIAM News 原文引用一致，无误。
- **未被收录之处**：whataifound.org（AI解题登记站）截至核实时**尚未收录此案例**（该站70条记录中无 Crouzeix 条目）——说明这是非常新鲜、可能还未进入主流跟踪列表的进展，而非该站已判定不成立。
- **Wikipedia 现状**："Crouzeix's conjecture" 词条已更新提及"2026年7月神经外科医生 Shanmu Jin 发预印本声称证明"，但词条口径仍保守，标注"尚未经数学界验证"（这是 Wikipedia 一贯的滞后/保守措辞，与 SIAM News 一手信源的"两位专家+原作者已核实无误"并不矛盾，只是标准不同：前者要等期刊发表，后者是专家私下审读结论）。

## 是否符合"AI攻击画像"

高度符合。这是一个纯分析类猜想，此前的部分进展本来就有"小矩阵反例数值搜索"传统（Greenbaum 等对 3×3/4×4 情形的数值探索），但本次并非反例搜索路线，而是 LLM 自主长程推理直接产出解析证明思路（正向证明，非计算机搜索反例）。属于本项目 cases.md 中"长程自主多子agent+对抗审查"这一 2026-07~08 波次的典型案例（与 Cycle Double Cover、Jacobian 猜想证伪、Maxwell 猜想证伪等同期，同样用 GPT-5.6 系列模型）。

## 来源（Sources）

1. arXiv:2608.03841 — Lorist & Schwenninger, "A solution to Crouzeix's conjecture" (2026-08-04) — https://arxiv.org/abs/2608.03841 （已直接核对摘要原文，引用 [12]=Jin 预印本）
2. SIAM News 文章原文 PDF — Townsend & Greenbaum, "The Neurosurgery Resident Who Proved Crouzeix's Conjecture" (2026-08-14) — https://alextownsend.net/essays/SIAMNews_CrouzeixConjecture.pdf （已完整读取全文4页）
3. Jin 预印本 — "The numerical range is a 2-spectral set", preprints.org/manuscript/202607.1919, v4 2026-08-07
4. Jin 的公开仓库 — https://github.com/jinshanmu/CrouzeixConjecture （手稿、Lean 形式化、prompt、AI对话记录）
5. Wikipedia — https://en.wikipedia.org/wiki/Crouzeix%27s_conjecture （已更新提及2026年7月声称证明，标注未正式验证）
6. 新闻报道（未直接读全文，仅搜索结果标题命中）：gadgetsnow.indiatimes.com、nationpress.com、remio.ai 均报道"北京神经外科医生用GPT解出20年猜想"
7. 交叉参考：Michel Crouzeix 本人近期 arXiv 活跃度佐证其仍在该领域——arXiv:2512.11813（2025-11-26）、arXiv:2509.19792（2025-09-24）、arXiv:2508.12768（与 Greenbaum 合著，2025-08-18）

## 建议

- 该条目建议正式录入 `cases.md`（★★★★★ 级，著名开放猜想+双独立证明+原作者背书），并从 scan_log.md 的"待核实"移除。
- 后续需跟踪：Jin/Lorist-Schwenninger 论文是否被期刊接收、Lean 形式化是否完整过 kernel、是否有人挑出漏洞（截至核实时未搜到任何质疑/勘误报道，但样本时间太短，需持续关注）。
