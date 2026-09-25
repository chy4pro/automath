# Parked problems（挂起非放弃 — 用户指示 2026-08-17）

有额度/有新思路/新模型上线时重新评估。每题一个文件记录：陈述、已做工作、卡点、重启条件。

| 题 | 卡点 | 重启条件 |
|---|---|---|
| erdos-287 | 社区证书链已推到 n1>3.99e19；完整证明疑需好素数无穷性 | 有新的结构性思路，或社区停滞后我们有富余前沿额度 |
| erdos-488 | Tao 卡在筛法振荡不等式；特例已被他人证完 | MalekZ 的 slab 归约有新进展可切入；或想到绕过振荡的新途径 |
| fernandes-2gen | Γ_{m⊕n} 2-生成（arXiv 2605.12342 Conj 1）；未开工 | 下一个主攻窗口即可启动（群论构造，正适合 5.6-pro/qwen 独立多路） |
| a63880-mod216 | σ(n)=2σ*(n) ⇒ n≡108 (mod 216)；未开工 | 快赢批清空后 |
| crystals-unique | 双调和平均"晶体"分解唯一性（arXiv 1601.03081）；未开工 | 快赢批清空后 |
| ~~a211417-bala~~ | **已证（2026-08-17）→ notes/proofs/a211417_v1.md** | RETIRED |
| a103425-tribonacci | 无素数加权 tribonacci 是否存在（Graham 1964 技术可能可迁移） | 覆盖同余系构造的专注窗口 |
| krenn-gu-n6d3 | 量子图 N=6,D=3 非存在性；Gröbner 计算量大 | 计算资源充裕的窗口 |

## conway99（2026-08-17 PARK-WATCH）
srg(99,14,1,2) 存在性。侦察报告 problems/recon/conway99_s1.md。park 理由：SAT 密集
+建制化竞争+边界推进型。复查节律 2-4 周；若 CDC 崩塌或我方获得新构造思路再评估。

## 记账更正（2026-08-17 重访）
- fernandes-2gen：**移出 parked → DONE**（08-16 已全链路定案：Lean 0 sorry + 论文发布；
  此前误标未开工——见 revisit_0817.md）
- REACTIVATED（2026-08-17）：a211417-bala（AlphaProof Nexus 竞争压力+p-adic 技巧可推广）、
  a63880-mod216（卡点已收窄至 powerful core 情形）——攻坚 agent 已派

## a63880-mod216 攻坚结果（2026-08-17，S2 opus）——仍 OPEN，但显著推进

产出：`notes/proofs/a63880_v2.md` + `notes/proofs/a63880_v2_verify.py`（33/33 检查通过，~103s）。

**新增无条件结果**（均为初等完整证明，非计算断言）：
1. ω(powerful core) ≤ 2 ⇒ core = 108（任意素数、任意指数；严格强于 v1 的平方自由定理）。
   关键步骤：两素数情形下把方程写成 q(q^{f-1}-1)(2·2^a-1) = 3(q-1)(q^f+1)，模 q 得 q | 3 ⇒ q=3。
2. **OEIS 猜想 (a) ⟺ (b)**，且两者都等价于「108 是 A 的唯一 powerful 元」。（v1 只有 (a)⇒(b)。）
   ⇒ Lean 文件里两个 `research open` 目标等价，证一个即可。
3. 6 | n（n powerful ∈ A）⇒ v₂(n)=2 且 v₃(n)∈{2,3}；v₃=3 ⟺ n=108；v₃=2 ⇒ n=36M，
   M 与 6 互素且 ∏ρ = 100/91（M 的素因子全 ≥ 11）。即 6|n 时猜想 (a) 的「4‖n」一半已证。
4. 6 | n 且 ω(n) ≤ 4 ⇒ n = 108。

**新增判定程序**（指数上完全精确、末位素数无需筛表）：无 108 以外的 powerful 解满足
ω(n) ≤ 3 且 v₂(n) ≤ 21——n 本身、奇素数、其余指数全部无界。（v1 只穷举到 10¹²。）

**具名障碍**（重启需要新工具，不是算力）：
- O1：v₂(n)=a 无法用不等式定界（奇部残余目标 1+3/(2^{a+1}-1) → 1）。破法需 Mersenne
  数 2^{a+1}-1 的素因子必整除 ∏(p^e+1) 这类 factor-chain / Zsygmondy 论证。
- O2：ω(n) 也无界（∑1/p ≲ log τ 与 ∑1/(p−1) ≳ log τ 仅差 ∑1/p²，大素数集可同时满足）。
- O3：前缀已能耗尽目标时支撑枚举失效（τ=2 时首次出现在支撑 {3,5,7}）。

**最锐利的子问题**（等价于 6|n 情形的整个猜想）：是否存在与 6 互素的 powerful 数 M 使
∏ρ(p,e) = 100/91？（素因子全 ≥ 11，某个指数 ≡ 3 mod 4，ω(M) ≥ 3。）
重启条件：有人给出 factor-chain 型的 v₂ 上界，或对 100/91 子问题有新思路。
- **a211417-bala：RETIRE（2026-08-17，已证）**。一般 D(r) 猜想（r≥1 全体）已完整证明，
  并附带证明同批的 C(k,r) 姊妹族（k=2,3,5），给出显式常数。证明见
  `notes/proofs/a211417_v1.md`（现为 v1.2），验证脚本 `notes/proofs/a211417_verify.py`。
  **双跨厂商审查均确认核心有效**：codex（`notes/reviews/a211417_review1.md`）+ Qwen
  （`notes/reviews/a211417_qwen_review.md`）独立复核 Legendre 约化/引理 A/B/C，
  均判无 critical error、主定理 3 VALID；两家缺口全在旁支，已于 v1.1/v1.2 逐条处理。
  v1.2：补全定理 4 证明（显式引理 C′）、重排 D(r) 表并加跳变注解（数值自始正确）。
  v1.3：撤回一处过度声称——混合积 42a/((2n+1)(3n+1)(5n+1)) **不被定理 4 覆盖**
  （三因子来自不同 k 且非两两互素，n=1 时 gcd(3,6)=3），改标 numerically verified,
  not covered；另补条件性命题 7（由三条外部最优结果 + gcd 结构导出混合积）。
  **Lean 已闭环**：`lean/proofenv/A211417.lean` 607 行 0 sorry，证出
  general_divisibility_strong（含 0<D）与字面版，并回收 r=1；FC 补丁两条无 sorry
  （残留 3 处 sorry 系上游自带的 r=1 姊妹条目）。Lean witness 用粗的 (r!)^{r²}，
  最优 D(r) 的形式化仍待办。
  v1.1 已修两处旁支：错误的 O(r log log r) 推论改正为 Θ(r log r)（上下界均证），
  "完全分类"措辞收窄为充分方向 + 对 30n+i 补上真正的不可行性证明（命题 5）。
  **优先权（§7.1）**：KitaKen1 于 2026-08-16（早我方一天）在 formal-conjectures issue
  #4923 声称一般情形 "paper-complete but not yet Lean-checked"，witness=lcm(1..r)^|L_r|；
  但无公开证明正文（issue 零评论、其仓库明写该题 out of scope、无 arXiv）。我方定位改为
  **independently obtained，不主张首证**；我方常数远小（r=7：7 vs 176400）且整除其 witness，
  另有 C(k,r) 族与命题 5 为其未涉及。
  下一步：Lean 形式化（可复用 AlphaProof Nexus r=1 文件的 `f_nat` 骨架）+ 论文。

## [08-18 05:45] a63880 REACTIVATED（第四条战线）
攻坚目标锁定 v2 §8 Obstacle 2 的最锐利子问题：是否存在与 6 互素的 powerful M
使 ∏ρ(p,e)=100/91（素因子全 ≥11、某指数 ≡3 mod 4、≥3 个素因子）——否定回答
= 猜想在 6|n 情形成立。副攻 Obstacle 1 点名但从未尝试的路线：Zsygmondy/因子链
（2^{a+1}−1 的素因子 ℓ>3 必整除 ∏(p^e+1)）以界住 v₂(n)。opus agent 已派，
产出 notes/proofs/a63880_v3.md。

### [08-18 06:30] a63880 v3 定案（root 亲跑验证器确认 30/30、0.19s）
- **Theorem F（COMPUTATIONAL，精确有理，gaps=0）**：不存在与 6 互素的 powerful M 使
  ∏ρ=100/91 且 ω(M)≤3 ⟹ **Cor F1：6|n 的 powerful 成员 ω(n)≤5 ⟹ n=108**（v2 只到 ω≤4）。
  两处关键改进：①把 v2 的浮点+余量素数指标界换成精确 Fraction 比较（Part 4 全程无浮点）；
  ②v2 只跑了引擎 1（τ=100/91 在 ω=3 卡住留 2973 支），v3 用精确残量引擎 2 全闭合。
  正对照：同引擎跑 τ=2 返回恰好 108 ✓
- 新 PROVED：Lemma V（D_ℓ 对任意 ℓ 的闭式，LTE，48734 例机检）、Cor V2/V3、Thm G7/G5、
  Rmk13（ℓ=13 已在 e=2 失效）、Lemma H（11|M ⟹ v₁₁=2 且其余素数 ≥127，余量仅 2/10101）、
  Lemma W（两素数情形对精确 t 恒可判定）
- **Zsygmondy 路线正式退役（Prop Z5，honest negative）**：Z1 修正 v2 表述（a 偶时
  2^{a+1}−1 整除 ∏(p^e+1)，a 奇时只保证 1/3）；新 Lemma Z4（初等两行）已强于 Zsygmondy
  的素数下界，Z5 量化证明不可能产生计数矛盾（a=20：p-窗口约 49400 素数 vs 3 个素因子）
- **新墙**：ρ(p,e)ρ(q,f)ρ(r,g) 仅落在区间时无法界住 r 或 f；同余工具无能为力。
  所需输入=界住 ω(M) 或 |91∏σ(p^e)−100∏(p^e+1)| 的非零下界（abc/线性型味道）
