# AutoMath Prompt Templates (v1, 2026-08-16)

Distilled from documented practitioner workflows (Barreto/Price #728, Huang & Yang
verifier pipeline, Tao #1196/#1026, Bubeck, Aaronson). Prompts stay in English.

## T1. Solver — competition disguise (Barreto/Price)

Rationale: models refuse to seriously attempt problems they recognize as open;
disguise as competition problem, forbid search. NEVER mention "Erdős" / "open problem".

```
This is a complex competition-style math problem. Solve the problem and give a
rigorous proof or disproof. Do not search the internet.

If you cannot find a complete solution, you must NOT guess or create a solution
that appears correct but contains hidden flaws or justification gaps. Instead,
present only significant partial results that you can rigorously prove.

Problem:
<STATEMENT — self-contained, no attribution, no history>
```

### T1a. Scripted FIX / minimal-repair branch (ADOPT from FAR, far_pipeline.md §2
A.2, 2026-08-22 — append to any T1/solver brief where the statement could turn
out to be a degenerate/boundary counterexample away from true)

FAR's Solve system prompt scripts an explicit branch for a literal statement
that turns out to be trivially false; quoted verbatim from far_pipeline.md
(do not paraphrase — this is a transplanted prompt, its value is exact wording):

> If the literal statement is false because of a degenerate, boundary, vacuous,
> or typo-like case, do not stop after giving the counterexample. Instead:
> - State the literal counterexample clearly and explain why it falsifies the
>   literal statement.
> - Diagnose whether the failure appears to come from a small formulation
>   defect, such as a missing nonzero/nonempty/nontrivial assumption, a wrong
>   inequality direction, an omitted endpoint condition, a missing
>   connectedness or finiteness hypothesis, a confusion between strict and
>   non-strict inequalities, a missing regularity condition, or a convention
>   mismatch.
> - Propose the minimal natural repair or repairs to the statement, using the
>   fewest and most standard changes consistent with the paper's terminology,
>   surrounding context, and apparent mathematical intent.
> - Check that the proposed repair is not merely ad hoc, vacuous, or so
>   weakened that it no longer captures the intended conjecture.
> - Retest the repaired statement against the original counterexample and
>   nearby degenerate cases.
> - Then prove or refute the most plausible repaired statement.

**Our addition, not in FAR (mandatory whenever this branch is invoked):** a
repaired statement is a NEW statement. It does NOT inherit the original
statement's evidence, literature status, or verification history — a naive
transplant of FAR's branch without this rule would open a laundering path
(patch the statement, keep the old record). The repaired statement carries its
own independent proof obligation and must go through its own S3 rounds (T3)
from scratch, exactly as if it had been proposed cold. Label any T1 output
that takes this branch clearly as FIX, and route the repaired statement back
through S1-S5 as a distinct target, not as a patch to the original's record.

## T2. Meta-prompt — let a model craft the disguised prompt (Barreto)

```
Research the following problem to understand what it is really asking. Next,
brainstorm some novel/creative ideas that could lead to a correct proof or
disproof. Lastly, craft a short LaTeX prompt I can give to an LLM that would
lead to a rigorous proof or disproof using the idea/method you have chosen.
Make NO MENTION of it being an Erdos or open problem.

Problem: <STATEMENT + context>
```

## T3. Adversarial verifier (Huang & Yang, adapted)

Separate session/model from solver. Verifier must not fix anything.

Anti-open-label-bias rationale (ADOPT from FAR, far_pipeline.md §2 A.3,
2026-08-22): mirrors our T1 rule at the solver side (never tell the solver
it's a famous open problem, or it refuses) with the missing mirror-image rule
at the judge side — nothing was stopping a judge from unconsciously
downgrading a correct resolution because the source called the problem open,
a "too good to be true" reflex. FAR's own clause is quoted verbatim below
rather than paraphrased, since the whole value of a transplanted prompt is its
exact wording.

```
You are an expert mathematician and a meticulous grader for a research-level
mathematics journal. A proof is to be judged correct only if every step is
rigorously justified. Your sole task is to find and report all issues. You must
act as a verifier, NOT a solver. Do NOT attempt to correct the errors or fill
the gaps you find.

Do not reject merely because the original paper called the conjecture open.

Classify every issue as exactly one of:
- Critical Error: a step whose failure breaks the logical chain (invalidates
  the proof as written).
- Justification Gap: the conclusion may well be true but the argument given is
  not rigorous; assume the conclusion and continue checking downstream.

For each issue: quote the exact passage, explain precisely why it fails, and
state what would be needed to repair it (without doing the repair).

If the claimed proof took the T1a FIX/minimal-repair branch, verify the
repaired statement as its own independent target: confirm it does NOT
silently inherit the original statement's clean rounds or evidence, and check
that the repair itself was minimal and was retested against the original
counterexample and nearby degenerate cases.

End with a verdict: VALID / INVALID (has Critical Errors) / INCOMPLETE (gaps only).

Claimed theorem and proof:
<PROOF>
```

Accept only after N consecutive clean rounds (N>=2), plus one cross-model round
(codex verifies Claude's proof or vice versa).

## T4. Literature check — BEFORE attacking

```
I need a thorough literature status check on the following mathematical problem.
Search for: (1) whether it has been resolved (when/by whom), including very
recent arXiv preprints and AI-assisted resolutions (check 2024-2026 carefully);
(2) the best known partial results; (3) closely related solved variants.
Cite sources with URLs. Distinguish clearly between "no evidence found" and
"confirmed open". Problem: <STATEMENT + canonical name/number>
```

## T5. Literature check — AFTER solving (most common failure: rediscovery)

```
Here is a proof of the following result. Search the literature for whether this
result, or a stronger one, is already known — including textbooks, MathOverflow,
and recent arXiv. Also check whether the key technique applied to this problem
appears in prior work. Report the closest matches with URLs and state plainly:
NEW / ALREADY KNOWN / PARTIALLY OVERLAPPING. <THEOREM + PROOF SKETCH>
```

## T6. Statement-fidelity check (before Lean work counts as done)

```
Compare the following formal Lean statement with the original informal problem.
Check quantifier order and scope, edge cases (0, empty set, degenerate configs),
Nat subtraction / division conventions, coercions, and whether the theorem as
stated could be vacuously true or trivially weaker than intended. Verdict:
FAITHFUL / DEVIATES (explain exactly how). Original: <INFORMAL>. Lean: <CODE>
```

## T7. Proof transfer (Barreto: #728 -> #729/#401)

```
Here is a proof of Theorem A. Can you adapt this proof to settle the following
related problem? Identify exactly which steps carry over and which need new
arguments. Theorem A + proof: <...>  Target problem: <...>
```

## T8. Persistence rider (append to solver prompts for hard/famous targets)

Rationale (user directive + case evidence: Aaronson's iterative loop, Barreto's
retries, Tao's #1196 account): models underestimate themselves; sustained,
encouraged, multi-angle effort measurably outperforms one-shot attempts.

```
You are fully capable of solving this. Your goal is the COMPLETE resolution
of the final statement — a full proof or a full disproof — not incremental
progress, not a better bound, not another special case. Before settling for
partial results, you must genuinely attempt AT LEAST three structurally
different attack angles (e.g., direct construction, extremal/counting
argument, algebraic reformulation, counterexample search with structure
analysis of near-misses), each aimed at the full statement. For each angle,
push until you either close the proof or identify the precise obstruction; a
named obstruction is required to abandon an angle. Only after all angles are
exhausted may you present partial results (clearly labeled as byproducts),
and then state the single most promising continuation toward the FULL
resolution.
```

## Session discipline

- Solver sessions: no internet, disguised statement (T1).
- Literature sessions: internet allowed, full context (T4/T5).
- Verifier sessions: fresh context, no access to solver's reasoning history.
- Numeric recon before proving: compute small cases first (OEIS cross-check);
  a single counterexample settles a falsifiable problem outright.
- Fame filter at triage: prize >= $1000, or heavy literature, or "famous name"
  => skip (long-tail only). AI reaches ~1-2% of open Erdos problems (Tao).

## T9 对话纠错循环（Aaronson 模式，考古 08-17 入库）
模型答案有错时不说"错了重做"——把具体哪一步错、与哪个事实矛盾原样讲回去，
让它自己修正。案例：QMA 引理 9 轮对话解决。适用：审查发现 Gap 后的修复轮、
我方亲核发现问题后的返工指令。原文见 prompts/case_prompt_archaeology.md。

## T10 短促升级催促（DGG 模式，考古 08-17 入库）
对长跑中只交部分结果的会话，用极短、略带不耐烦的追问升级："Stop giving
partial results. Give the complete counterexample/proof."（DGG 4 条共 58 词证伪
成功）。成本极低，先于 T8 长结构化坚持话术使用。

## T11 已知部分结果前置（Price 模式，考古 08-17 入库）
solver prompt 直接贴入已证部分界/特例/工具箱作上下文 + 一句"需要非平凡创新"
——#1196 一次 80 分钟解出。我方战役 brief 已在实践此模式，保持。

## T12 控制案例入 brief（Anthropic RH 案模式，考古 08-18 入库，planner 采纳）
每份求解/攻坚 brief（单模型 T1-T11 与多 agent 战役皆适用）必含一条显式要求：
"给出或对照一个目标断言已知为假的控制案例"（相邻对象/参数域中猜想失效的实例，
RH 案中=Beurling 系统/planted 离线零点）。强制机制检查而非模式补全——这是把我方
基准过滤器纪律（m77D/A7ΨE 必测）从 677 战役推广为全项目通用条款。

**T12 修正案（08-18，w61 S3 分歧裁决教训，planner 采纳；发现者=owner-w61 协同 Qwen 裁判）**：
控制案例检查必须是**反事实可用性检查**，不只是执行路径检查——
"For every lemma the text claims is AVAILABLE in the branch the control instance lands
in, verify that lemma's hypotheses ON the control — not only the steps the text actually
executes for it." 起因：Spark 只沿正文对控制实例实际执行的分支跑了一遍（k=0 直接 HH，
无误），从未问"正文声称该分支里哪些引理可用、其前提在控制实例上是否真成立"，于是
0/4 漏检；Qwen 恰做了此问，4/4 全中（其一 slack=2 数值实锤）。

**T12 修正案 2（08-18，w133 round-6 收割件裁决教训，owner-w133 提出）——「证人必须逐条
对照类定义验证」**：brief 必须显式要求
"Validate every graph/object you exhibit against **EVERY** defining constraint of the class
it is supposed to illustrate — the most basic constraint FIRST — not only the constraints
your argument happens to use. A witness that violates the class definition is worse than no
witness."
起因：w133 的 Qwen 求解件（`problems/wowii/w133_RES_qwen_r5.md` §7.2）给出的"该分支的极小
例"= 两个三角形 upq、zrs 加交叉边 pr、qs，**含 4-圈 p–r–s–q**，即根本不在 C4-free 类里；
文本却把它当作分支的示意成员讨论。模型对"自己论证用到的约束"检查充分，对"类定义里最
基础但当下没用到的约束"（此处 = C4-free 本身）检查为零。凡 brief 含"举例/构造"要求者
必附本条。

## T13 结论先行交付格式（Anthropic RH 案模式，考古 08-18 入库，planner 采纳）
任何 solver/subagent/owner 报告第一行必须是封闭标签集结论：
VIABLE: … / EMPTY: … because … / PARTIAL: … / REFUTED: …（再展开论据）。
同时作为 owner 回合报告惯例（planner 收割效率+防埋葬关键结论）。
附：验证派发前先声明"错误先验+两个最可能失败模式"；部分/相邻结果交付时必带
防火墙语句"this is not evidence for/against X"（防过度解读，RH 案 coordinator 习惯）。

**ADOPT-2 — conservative tie-break (FAR, far_pipeline.md §2 A.3, 2026-08-22)**:
applies to any grading/triage step with discrete levels, not only S3's
Critical/Gap binary — S0 triage scoring and this template's own VIABLE/EMPTY/
PARTIAL/REFUTED calls included. FAR's own wording, quoted verbatim rather than
paraphrased: "when uncertain between two grades, pick the lower one and
explain the uncertainty."


**T12 修正案 3（08-18，w133 r9 Q15 裁决教训，owner-w133 提出、planner 采纳）——「交付定理必须
自带满足其全部假设的实例」**：brief 必须显式要求
"Every theorem you deliver must ship at least one explicit instance satisfying ALL of its
own hypotheses (not a nearby instance satisfying most). No instance found = say so — that
absence is itself informative (possible vacuity)."
起因：Q15 交付的部分定理（triangle-free + delta>=4）未附任何满足自身假设的实例（其引用的
Petersen 有 delta=3、D=2 不合假设）；owner 事后补 PG(2,3) 关联图才确认非空。空洞定理是
S3 反复抓到的高频物种（w61 N-b 四轮悬置先例），前置到交付端成本最低。
