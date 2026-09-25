# 竞争对手档案：KitaKen1（Kenta Kitamura / "Intellectual Moonshine"）

建档 2026-08-18（三路并行调研：GitHub API 数据挖掘 / 四代表仓库精读 / 全网足迹）。
完整文章（用户可读版）：https://claude.ai/code/artifact/c6772741-7bcf-476d-a5b9-dfc5d8008bcd
原始数据：本会话 scratchpad profile.json/repos.json/prs.json/commits_*.txt（易失）。

## 速览
- 日本独立研究者（时区推断 JST），单人+人在回路 AI，无机构、无 arXiv、无博客、无媒体报道
- 时间线：2026-02-05 首触 FC（PR 被退：不会本地编译）→ 05-06 首合并（等 89 天）→
  **08-10 起工业化**：9 天 31 仓库（08-15 单日 12 个）、43 PR 中 29 个、合并中位 275h→9.2h
- 模型栈演化（披露原文）：ChatGPT-5.2 → ChatGPT/Codex 5.6 sol xhigh → Codex →
  **"OpenAI Codex, Fable5, and Claude Code"（08-17 最新）**——已用我方同款工具
- 自述工作流（lean-eval 提交 JSON）：人定策略、AI 出证明、人审中间断言、本地+EC2 编译

## 产线要点
1. 靶场=FC 预制陈述（category research open + sorry）；>25-50 行证明必须外置=官方规则
2. 一题一抛弃式仓库，模板骨架 README+lean/+lean4web/；commit 原子倾倒（过程全黑箱）
3. lean4web 技巧：自包含单文件+live.lean-lang.org URL 参数=零安装浏览器内核复验
4. 质检：#print axioms 全覆盖（旗舰 60+ 次增量）；sorry 仅 1 处且公开声明；旗舰有
   audit.sh（curl 钉 commit 逐字符串比对上游陈述）——其余仓库只有手动 grep
5. **结构缺环：无独立对抗审查阶段**（审稿人=自己+内核）→ 难离开预制陈述轨道
6. 选题谱：速食渐近题 → 打包 OEIS 整除 → 形式化他人反例（零数学风险）→ 旗舰
   Erdős 979 k=3（18,640 行/52 文件/复用 PNT+ 库）→ 真常数改进（Erdős 425: 2.95→3.499）
7. 讲规矩：拒绝空洞陈述记分（A211417 D=0）、给 FC 提 ~7 个错误形式化审计 issue、
   每次披露 AI；社区实名认可（Woett/Nat Sothanaphan/Chai Wah Wu engage；OEIS A397205 署名）

## 与我方五次相撞
A113019（他反例击杀我方候选）/ A114831（他先证）/ Fernandes（他先证，PR 挂 5 天我们没查）/
A211417（他解四具体+弃权一般情形，我们拿下一般情形，双方诚实互引）/ FC 审计 issue 生态位重叠

## 应对（已入 methodology 或待执行）
- ✅ S1/S4 查重清单 v2：FC 未合并 PR + `gh repo list KitaKen1` 必查
- **预警雷达**：他仓库先建、PR 后发（差小时~天）——每 tick 监控 repo list=看到他在攻什么
- 错位竞争：避开 FC 速食题正赛，主攻一般参数定理/战役型结构理论/需对抗审查的原创数学
- 抄作业：audit.sh 式陈述比对脚本、lean4web URL 复验、第三方专业库复用意识
- ✅ 速度纪律：证完→公开小时级

## 快照 2026-08-18（owner-intel 接手首次基线，`gh repo list KitaKen1 --limit 100`）
- 全量 69 仓库（含 2 个 2024 年无关旧仓 BrainOrganoid*，可忽略）；最新活动：
  `formal-conjectures`（fork，08-18 09:47 push）、`oeis-a129365-conjectures`（08-18 03:13，
  scan_log Sweep3 已记）——**上次快照后无新增原创攻坚仓库**
- `formal-conjectures` fork 今日活动 = 常规 FC 审计工作流，非新战线：PR #5030（VCDimConvex
  n=0 退化情形修复，08-18 09:50 已合并，对应既有仓库 `vcdim-convex-counterexample`）；同批
  近期 fork 提交（08-16）均为陈述-源文核对类修复（Erdős 477 index-set 偏差、Green's 40
  filter 类型错、Erdős 1055 class 定义遗漏排除条款）——延续"讲规矩"人设，非数学攻坚
- 公开 FC PR 检索（`gh pr list --author KitaKen1 --state all`）：近期含 1 条 OPEN 未合并
  （#5011，arXiv 2607.03582 Conjecture 5，08-16 发起，非我方在攻线）
- **撞车检查**：677（Tao Equational Theories 677→255，magma）、WOWII-133、WOWII-61 —— 三线
  在其仓库名/PR 标题中**均无命中**（`wowii-graph-conjecture-*` 系列仅覆盖 2/31/217/316 号，
  与我方 133/61 不重叠）。**本次快照零撞车信号**，无需即时上报
- 下次快照建议直接 diff 本节仓库名清单，而非重新审阅历史仓库

## Diff 2026-08-18（owner-intel 回合2，`gh repo list`+`gh pr list` 直查，非网页模型）
- 最新 15 仓库时间戳核对：与今晨 planner 基线（`oeis-a129365-conjectures` 08-18 03:13 /
  `erdos-979-k3` 08-17 05:43）比对，**无新仓库产出**（`formal-conjectures` fork 08-18
  09:47 push 是同一枚 PR #5030 的常规审计修复，非新战线）
- FC PR 列表（`gh pr list --author KitaKen1 --state all --limit 20`）核对：最新 PR
  #5030（VCDimConvex n=0 退化修复，08-18 09:50 已合并）之外，无新增 PR；#5011（arXiv
  2607.03582 Conjecture 5）仍 OPEN 未合并，非我方在攻线
- **撞车检查**：677/WOWII-133/WOWII-61 关键词在最新 15 仓库名与最新 20 条 PR 标题中
  均无命中——**本次 diff 零撞车信号**，无需即时上报
- 附带发现（顺带，非本次 diff 目的）：本回合案例情报考古确认 KitaKen1 与 DeepMind
  官方 AlphaProof Nexus（arXiv:2605.22763，见 cases.md）是完全不同量级的两类竞争者——
  KitaKen1 是个人+FC 生态位竞争，AlphaProof Nexus 是厂商级系统，两者暂无重叠攻击面
