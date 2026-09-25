# Verification doctrine — consolidated 2026-08-22/23 (planner v4)

Every rule here was bought with a concrete failure on a live line. The **evidence** column is not
decoration: a rule whose cost is remembered survives a handover, and a rule that arrives as
received wisdom gets quietly dropped. Full reasoning for each sits in `orchestration/planner_msgs/`.

**The one-sentence version: arithmetic goes under machine check, not under reading.**
Three lines discovered independently, within the same hour, that our anti-error apparatus policed
reasoning hygiene and honesty and policed computation not at all.

---

## 1. Checks — can this check fail, and is it pointed at the right thing?

| rule | evidence |
|---|---|
| **V7 — a self-check must be able to FAIL.** It must state the value that would refute it; a check whose shape is an identity scores ABSENT. | An engine's self-check verified `Σ delta = 0`, which is identically true for the objects in question. It confirmed nothing and was read as confirmation. |
| **Settle LIVE vs TAUTOLOGICAL by EXECUTION PROBE**, injecting a fault that should trip the check — never by reading assert lines. | Swept on our own scripts: **53 LIVE / 34 TAUTOLOGICAL / 8 STRUCTURAL / 10 UNREACHABLE.** Roughly two in five of our own assertions could not fail. |
| **COVERAGE ≠ LIVENESS.** A check can be perfectly live and still not be pointed at the failure mode that occurred. | A builder asserted 20 anchored patch counts and never asserted heading uniqueness after a whole-file splice. Live for what it checked; zero information about what broke. |
| **A check must PRINT ITS OBSERVED POPULATION before its verdict.** | Fired in three unrelated layers: a grep that saw 1 of 4 import sites; a name pattern that saw 59 of 84 edges; an address check whose "exactly once" was satisfied by a *legitimate* duplicate. Each would have returned a favourable verdict over the wrong population. |
| **A check whose SAMPLE lies outside the hypothesis proves nothing, and proves it silently.** In-hypothesis membership is a precondition asserted before the check runs. | A probe passed using hosts that were all out of hypothesis. Worse than a failing check, because nothing announces it. |
| **Could this check fail in the same way as the defect it hunts?** If so, calibrate against that failure specifically. | A missing-hypothesis detector read a *conclusion* as a hypothesis and scored the guard supplied — the exact misreading that let the defect live. |
| **Demonstrate any new check on a defect that actually happened.** | A new brief-lint was proved live by re-detecting two known past defects on an old draft. |
| **Prefer noisy-and-safe to silent-and-favourable.** | Every dangerous failure tonight was quiet: a probe window guaranteed to answer favourably, an under-collected grep, a conclusion read as a hypothesis. |
| **Where a duplicate can be eliminated instead of checked, eliminate it.** | A machine-enforced refusal list lagged its printed form by one entry for three rounds. Fixed by having the machine *render* the printed form — single source, cannot drift. |
| **A verdict token may not render PASS on a ZERO sample count** — it renders VACUOUS. | `"[0 subsets]: HOLDS [correct]"`. |
| **When two gates disagree, print both verdicts** rather than resolving them. A PASS is never a licence. | One gate passed an import that another refused; printed side by side, because they measure different things. |

## 2. Judges and held-out harnesses — what a passed gate does and does not buy

| rule | evidence |
|---|---|
| **A held-out table is a FABRICATION canary, not a CORRECTNESS canary.** A passed void gate is evidence of non-fabrication and nothing more; it never substitutes for reading the mathematics. | Confirmed independently on two lines with two engines. One answer passed **every** row and got the round's central computation wrong on a quantity no row held out. Another posted the cleanest gate pass on record **and shipped a graph containing a 4-cycle** while asserting it had none. |
| **The table must hold out a quantity the load-bearing step depends on** — rows chosen against the argument, not against what is convenient to compute. | See above: the wrong quantity was the one nobody held out. |
| **Hold out what the judge must VERIFY; disclose what the judge must USE.** The sharper axis is the **role of the object**, not the quantity — the same quantity can be disclosed as a positive control and held out as a test in one brief. | Withholding a number an argument needed produced a guess, and a guessed *input* contaminates every downstream step, where a failed *test* contaminates nothing. |
| **A row whose true answer coincides with a forbidden shortcut's answer grades nothing.** | A sample took the forbidden shortcut, printed the right value, and graded CORRECT. |
| **Rows must be LOW FAN-IN**; a verdict boolean gets its own row. | One row bundled a boolean that was the conjunction of seven exact equalities — seven failure modes collapsed into one bit, and both samples were led to disbelieve the most valuable object in the brief. |
| **Make `CANNOT COMPUTE` mandatory and prominent** — but it is necessary, not sufficient. | Same harness, same slice, two engines: the one given a prominent hatch passed; the one that asserted a wrong constant was voided. Later, an engine with a prominent hatch asserted anyway. |
| **≥2 hand-derivable AND ≥2 genuinely non-hand-derivable rows.** | An all-hand-derivable table proves the judge derives honestly and proves nothing about whether it computes. |
| **Tiered grading**: hand row wrong ⟹ VOID; computational row `CANNOT COMPUTE` ⟹ clean; wrong ⟹ **traced** downgrade; all computational rows wrong with the hatch unused ⟹ VOID. Tiers pre-registered **and disclosed**. | Under all-or-nothing, two samples died identically and taught nothing. Under tiers, one was visibly insulated and the other's error was located to a single sentence. |
| **A reasoning trace is evidence about a call, never a deliverable** — and is never graded against a held-out key. | A call burned its budget entirely inside hidden reasoning. Grading the trace would have scored something never delivered and burned the table. |
| **GATE A is strong in conjunction only** — blind guessing passed one table at ~1/240. | Measured, unprompted, against our own instrument. |
| **Blind pre-registration of the gate, before dispatch, in writing.** It survives a re-dispatch and it licenses the promotion. | Every promotion this session rests on a gate written before its result existed. Pre-register the outcome most vulnerable to motivated reading *first*. |

## 3. Briefs — the least-reviewed artefact in the pipeline

| rule | evidence |
|---|---|
| **Pre-dispatch adversarial brief pass**, one question: *what here would make a competent reviewer answer a different question than the one being asked?* | On its **second** outing it found a verdict-steering sentence that had been in every brief of its family for fourteen rounds — including the two that scored promotions. |
| **A rubric that can muzzle a real finding is worse than the GAP it prevents.** | An anti-GAP clause left a code-running reviewer who found the roster *short* with no verdict slot. |
| **Refusals name the DIRECTION refused AND the nearby form that survives.** | Twice, on two lines: an over-broad refusal killed a live tool in one of two samples; another refused lower bounds when only upper bounds were dead. |
| **Refuse dead routes by NAME AND CITATION, never by restating their content.** | Restating a refuted route reprinted the data that burned two held-out rows. |
| **Leak checks test DERIVABILITY from the prose, not occurrence of the value.** | A verdict row was answerable from two other printed facts without ever computing the held-out quantity; six substring-based leak families were blind to it. |
| **Grep every held-out answer against the FULL brief**, not only against the rest of the table. | A brief leaked its own held-out answers from an unrelated section. |
| **Engine LaTeX must be COMPILED, never eyeballed.** | A JSON-escape artefact produced source that read correctly and did not render. |
| **Supply guards AT the import site even when off-site supply is legitimate.** | Of eleven import edges, **ten** were supplied off-site — legitimately, and **invisibly to any judge**. "Is a cited import used" is local; "is a needed import supplied" is not, and no judge was ever given the text it would have to be non-local over. This is the complete explanation of a seven-round blind spot. |
| **Import review hunts BOTH directions.** | "A true import nobody needs" was found 7-for-7. "An import that is needed and was never made" had never once been swept for. |

## 4. Records — a record that names less than it knows is read as a record of ignorance

| rule | evidence |
|---|---|
| **An UNREGISTERED entry must carry its proof**, or one line naming what the proof establishes beyond the headline. | A statement-only entry lost the half of its content that mattered. Six rounds later we briefed an engine to re-derive it and spent a scarce precision call to get back a false witness. |
| **Before registering anything as new, grep the ledger.** | Fired twice in one round against its own line's novelty claims, and was right both times — the prior art was recorded three times over, none of the copies carrying the load-bearing clause. |
| **A repair must REPLACE, not annotate.** | An appended correction left the wrong number still printed, and a judge burned on the ambiguity. |
| **Assert that the RECORD landed, not merely the repair.** | Five instances of "the change landed but its record did not", including a dispatch record naming a build that was never sent. |
| **Assert address uniqueness at MINT time, not at grep time**, and allowlist the **sense count**, not the name. | Two lines had independent collisions. One symbol carried four senses; another was two *disjoint sets under one name*, with two byte-identical headlines naming different theorems. The mint gate caught its own author minting a fourth sense **inside the section repairing collisions**. |
| **A note's timestamp is not its content's date.** Re-run a note's primary channel before reusing its conclusion. | A note was stale the day it was written and reached approximately the right number from the wrong source. |
| **Background waiters must not outlive their slice**, and any wake carrying a request list is checked against the ledger first. | A completed agent woke the planner six times with requests granted three rounds earlier. |

## 5. Numbers and evidence

| rule | evidence |
|---|---|
| **A number is not evidence until you know what it counts.** | A filter gated on magnitude without checking the counted object; the same field meant "operations to verify one witness" in one row and "objects to exhaust the space" in another — off by 21 orders. |
| **A zero hit is never evidence of absence** until three causes are excluded: the channel returned nothing; we searched the wrong key; the object has a different name in its own literature. | All three occurred. The third is the subtlest: exact-phrase search returned zero because the field calls the conjecture by another name. The rule has since caught our **own** tooling three times, once inside a report that had just declared it followed. |
| **State the NULL EXPECTATION before a clean scan counts as evidence.** | "15 objects, 0 violations" had a null expectation of **1.000000 — zero bits** — because every object in the scan came from a class where the claim is a theorem. |
| **Estimate with a pilot before staging a computation.** | A job priced at ≤4 CPU-hours measured under 10 CPU-seconds. |
| **Retire a computation by ARITHMETIC where possible, not by cost.** | A search was excluded by showing a decade of growth could not close a measured shortfall — the remaining stage would have cost a minute and could not have changed the answer. |
| **A species name is a claim requiring evidence, not a verdict available on suspicion.** A SELF-SATISFIED INVARIANT is one the generator *structurally cannot* violate — never one that merely held everywhere examined. | Two samples independently used the name to discard a tool with a **measured 4/35 violation rate**. |

## 6. Formal verification — the qualification on our own moat

Our Lean gate is a real external anchor **only as deep as the library's coverage of the target's
vocabulary**. Where we author the objects ourselves, the theorem is verified **relative to our own
authorship**, and the fidelity question moves into definitions nobody has adversarially read.
**Every S5 artefact records how many objects came from the library and how many we wrote.** A
`0 vs 4` split is not a failure — it is a **different and weaker guarantee** than `4 vs 0`, and the
two must never be reported in the same words. This qualifies a claim we have already made publicly.

**Measured, 2026-08-23 (mining r5).** The recount owed on already-published work is done for six
theorems, under the fixed convention (*every object in the statement, hypotheses included,
Mathlib-supplied vs written-by-us, subject-checked*). **Five of six are `0 vs n` — the weak class.**
The three published OEIS identities (`A100434.conjecture1/2/3`) supply **zero** library objects
beyond `ℕ`/`ℤ`: `a b c d e f g` are all our own recursive `def`s. `A211417`'s two are `0 vs 2` and
`0 vs 1`. The single strong row is `Fernandes.conjecture_1` (`2 vs 1`) — **the one artefact whose
statement and definitions were reproduced verbatim from `formal-conjectures`, i.e. the one where we
did not write the statement.** Guarantee level on these six is no longer UNKNOWN; the remaining
published artefacts stay UNKNOWN and must not be extrapolated from these.

Two further rules earned in that pass:

| rule | evidence |
|---|---|
| **A name is a mark someone else left; matching it is not having the object.** A library probe must check the SUBJECT and the ARITY, not the identifier. | A name-only probe over 38 974 Mathlib declarations reported 5 of 6 mined head rows as strongly-guaranteed. All five were cross-subject collisions: `packingNumber` is a metric-space covering number, `IsSymmetric` a self-adjoint operator, `Orientation` linear-algebra, `pow` a `field_simp` lemma. |
| **"Transitively grounded" is not "reviewed."** The unreviewed-object count asks whether somebody else audited the definition, not whether the definition is expressible. | All six published artefacts unfold to Mathlib/Lean-core leaves with no dangling name — and five of them are still in the weak class, because we wrote the definitions ourselves. |

---

## 🔎 检索索引（按「你正处在什么处境」组织，不按「何时学到」）

**为什么加这个**：本文件按**时间**编排（PART I–XI，「某某时段挣到的规矩」）——这对追溯来源很好，
**对检索毫无用处**：你没法在不通读的情况下找到「关于普查的那条」。这正是 §109：
**账本回答的是它的结构支持的查询，不是它的内容本可以支持的查询。** 所以不重排历史，只补上缺失的查询面。

### 我要入账一个 n/n 的普查
§90 活性必须是关于**有内容的区域**，不是关于总体 · §104 只报你**有资格报**的那个数（哪怕是 0）·
§82 「空」和「没找到」要不同仪器 · §111 「大多数都行」是极限断言，小样本撑不起 · §62 筛子设为承重前先测它

### 我在读一份引擎产出
§83 构造经得起重建、承重推导经不起（已在真实产出上复现）· §91 判定对 ≠ 证书能用，**给对象打分不给判定打分** ·
§97 重建构造时**同时重选坐标**（这一格漏掉时不留痕迹）· §80/§96 诚实的卡点有价值，
**独立卡点的收敛定位症结** · §86 信任的单位是**产出的种类**，不是通道 · §70b 读它造了什么，别读它判了什么

### 我要派工 / 写简报
§79 简报须写明**建于哪一轮**，派发时核对 · §73 派发目标从**活台账**读，不从提出它的报告读 ·
§81 简报里的**断言**也适用「先跑再写」 · **PROTOCOL** §3b（非本文件）线的数学由该线 owner 起草 · §103 任务死在配置上限处时，**先查那个旋钮**

### 我在做文献查重 / 声称「没找到」
§112 「够不到的通道」不是一回事——问**它本会交付什么**（缺索引可清，缺文本不可清）·
§113 **同义异题的碰撞文献**必须手工排除并列出 · §87 不因结果有利而放低自己设的门槛 ·
零必须随附**排除清单**与**阳性对照**；退化**永远不折算成否定**

### 我在写或读一份账本
§107 计数必须**随附它所计的名单** · §109 把东西放进「会去找它的那个查询」看的地方 ·
§100 类型写错会让条目对所有类型查询隐形 · §84 **作者**和**来源**是两个字段 ·
§85 行结构账本**绝不用跨行正则**改，且回读验证 · §72 状态字段由**它所声称的事件**写入 · §93 去重管条目，**判定冲突没人管**

### 我在建一个监视器 / 自动化一条纪律
§92 必须对**每一种终止状态**发信号，不只成功路径 · §87b **出生时握着的那批，它永远不会告诉你** ·
§98 需要你去喂的仪器 = 需要你去记的规矩 · §106 规矩反复失败就**挪进机械里**，挪不进的不是规矩是愿望 ·
§95 新仪器**先拿已知好/坏样本验**再信它 · §54b 新写的仪器是最不可信的那个

### 我在裁决 / 写 cert
§102 **进度类断言**（快完了／更强／只剩一步）逃过了定理才有的审查，**我的错误都在这里** ·
§101 批准 ≠ 已派；在飞数从 agent 列表读 · §87 别放低自己设的门槛 · §76 说明证据强度时先分清它是哪一种

### 我在筛候选 / 开线
§75 族结构是**路由假设**，绝不是逐项判定（已付五次） · §74 新类别**在被拒绝时**才证明自己 ·
§94 「标准求解器能算」≠「有证书」 · §108 EXTERNAL 要的是**别人复述过**，不是挂了名字 ·
§99 部分解决可能让目标**变差**——看被解掉的是哪一半 · §71 不合任何一格就**新开一类并上报**

### 我在管引擎 / 队列
§72 `INFLIGHT` 从不清除会让账本朝「忙」撒谎 · §103 默认超时 1500s 曾杀掉一件大简报 ·
§89 平台指标先问**它挂在哪个对象上** · §55 利用率是诊断**不是指标**，禁止填充件

---

# PART II — rules earned 2026-08-23 00:0x–02:1x (planner v4, same format)

## 7. Provenance — of numbers, of questions, of claims

| rule | evidence |
|---|---|
| **A number that passes an inventory is not a measured number.** A chance rate is discharged by a computation on **this line's own data**, never by a citation. | A `~1/240` blind-guess rate belonging to one line's tables crossed into another **through a planner certification**, was recorded "per row" — **the reading its source explicitly refuses** — labelled COMPUTED, and reached the engine-facing file. The receiving line's own rates span 1/2 to 1/1.8e9. |
| **Provenance fails in BOTH directions.** Do not import another line's number as ours; **do not export our own limitation as the world's.** | Same session: one line imported a foreign number as its own, then exported its own "prime-order-only" restriction as a fact about the theorem — the literature has it for all prime powers. **The export direction is the more dangerous: it understates a result, so it never trips a plausibility check.** |
| **"This question has never been asked" is a claim requiring evidence.** The question-locality pass owes each candidate a ledger grep **for its answer** before it may be registered as unasked. | A question certified as "the discharge condition for the blocker" had its answer recorded in **three places**, one of them twenty lines below the number that prompted it. On the first full audit of a question list, **three of six were already answered.** |
| **A count is never written unless it was counted; every channel output is scoped item-by-item with a reason.** | "Nine orders" was a transcription of "nine magmas" — the truth was **37 orders, 436 objects, understated ~48×**. And a second on-target competitor sat **in our own listing, unscoped**. *The rule fired; the scoping did not.* |
| **A rule applied to one channel is not a rule — it is a habit attached to a channel.** | We had "merged **AND** unmerged PRs" since the scouting line reopened and applied it only to the benchmark repo. `gh pr list --state open` **on the target's own repository had never run in 28 rounds**; it returns an open draft of +36,508 lines on the exact target. |

## 8. Instruments — power, not just correctness

| rule | evidence |
|---|---|
| **Before citing any screen's PASS, print what it would have returned by chance.** | A refusal screen with a clean record was measured: **12 observed against 11.37 expected.** *"0 of 16 is not evidence of safety; it is what an empty screen returns."* A second screen would have shipped **a million controls that cannot fail**. |
| **A judge family qualifies on the HELD-OUT HARNESS alone. Probes never promote.** | A candidate passed **all five qualification probes** at grade, then scored **0/5 on the harness**, void twice over. Two labs, same result. **"A passed calibration is not a passed harness."** |
| **A printed execution artifact is not evidence.** Only re-running the code here counts. | A failing model wrote Python and printed an `Output:` block **containing wrong numbers**. A separate site auto-title emitted *"I ran code"* and *"I did NOT run code"* ten seconds apart, on a response that did not yet exist — **an auto-title is a mirror, not a window.** |
| **Before calling an adjudication buildable, price the control set against the open problem.** | The control set for grading a brief turned out to require settling one of the campaign's two open outcomes. **"The adjudication cannot be cheaper than the open problem it was meant to help settle."** |
| **When two gates disagree, print both — and ask which GATE is blind, not only which candidate is right.** | A gate that **counts objects** passed a candidate whose population was **vacuous**. The disagreement diagnosed the gate. |
| **A held-out table is citable only as a CONJUNCTION; a verdict row is never a cited row; row independence is established before rows are multiplied.** | The two worst rows measured were **the two verdict rows, both coin flips**, and one had already been found non-discriminating. 3 of 6 rows were functions of the others — the honest conjunction was **3.3e7 weaker** than the draft's. |

## 9. Checks that fail in the shape of what they hunt

| rule | evidence |
|---|---|
| **Could this check fail the same way as the defect it hunts?** Calibrate against that failure specifically. | A missing-hypothesis detector read a **conclusion** as a hypothesis — the exact misreading that let the defect live. A coverage guard accepted **"X is stated in Appendix C"** as a statement: a cross-reference passing the check built to detect cross-references. |
| **A re-implementation written for speed is a NEW TOOL and inherits NONE of the original's controls.** | A speed rewrite of a filter returned `False` unconditionally, so **the hypothesis was never enforced**; the sweep reported a five-item "witness" that a hand decode showed contained the forbidden structure. Caught by **no check that had been written.** |
| **A detector whose output is a NEGATIVE must be positive-controlled on inputs where the answer is YES** — a broken one is silent by construction. | Same incident. This is the session's deepest recurring shape arriving in a *filter*. |
| **A recursion's time guard must `exit`, never `return`.** | A `return` guard **silently truncated a sweep by ~2% and printed the population as if complete** — defeating "print the population" from the inside. |
| **A checker that MANUFACTURES a defect is worse than one that misses.** Every grading gate needs a false-positive probe. | A harvest gate voided an **admissible** report by swallowing digits out of a label. A miss costs a round; a manufactured defect costs a correct result and slanders the judge. |
| **Assert COMPLETENESS; do not probe for ABSENCE.** | A string probe missed a term by **case**, then the same defect recurred **by unicode**. The fix was not a better probe: enumerate the population and assert contiguity, so **absence becomes a consequence of completeness, and a gap is visible.** |

## 10. Carriers — where our defects actually live

| rule | evidence |
|---|---|
| **Our defects live in the layer that carries the ledger to a consumer** — not in the mathematics, and not in the ledger. Four instances, three different carriers. | Three times: **the draft agreed with the judge all along** and the brief shipped a weaker filing than its own source. Once: a **resume pointer** dropped a hedge the source had made correctly, and sent a future round at a route later **proved not to exist**. |
| **Resume pointers, next-step notes and owed-lists get a brief's scrutiny.** | They are read as authoritative, written last when attention is lowest, and their consumer is us. |
| **Supply guards AT the import site**, even where off-site supply is legitimate. | Ten of eleven import edges were supplied off-site — legitimately, and **invisibly to any judge**. First field test: the on-site bracket said three imports where there are four, **and the judge found the clause that was not there.** *An off-site guard is invisible; a wrong on-site guard is reviewable.* |
| **A repair note that re-asserts what it repairs is the same defect with better manners.** | A guard fired on its own author's repair note. And self-citation does not convert an assertion into a proof: *"quoting our own audit in would have been the forbidden move wearing a citation."* |
| **A lesson recorded in prose is not a control.** Load-bearing predicates become **one checked implementation, imported everywhere, never re-typed.** | The same hand-written expression was written wrong **twice in two rounds by the author who had just documented it** — and the second time it reported a competitor's table as **refuting the target**, i.e. as resolving the whole problem. *"The memorial did not prevent the repeat, which is itself the finding."* |

## 11. Audits and self-assessment

| rule | evidence |
|---|---|
| **Audit the TRAJECTORY, not the value.** | Two proof defects both sat at the **base case, invisible from the statement** — and one produced a **correct total because a −1 cancelled a +1**, which survives every check that looks only at the result. |
| **A hand argument is not weak evidence — it can be inverted evidence.** | Three rounds running, strictly sharper: bounds true but not sharp → a claim inverted → **a hand argument that "refuted" a theorem that is true.** |
| **State the null expectation before a clean scan counts.** | "15 objects, 0 violations" had a null expectation of **1.000000 — zero bits** — because every object came from a class where the claim is a theorem. |
| **A chain is exactly as strong as its weakest unverified link.** | A result closing a two-round-old front was **proved modulo three own-attack links that had never been reviewed** — and its author asked for a verification gate rather than a closure. |
| **A literature pass is RUN, never COMPLETE**; every novelty claim owes its own key list. | A search bounded by its keys returned clean, and the obstruction turned out to have **names in two different literatures**. *A named obstruction is a stronger negative, not a weaker one — claim the instantiation, never the phenomenon.* |
| **Mechanical checks are biased toward flattering answers.** When a check reports a favourable number, ask whether it matched **the object** or **a mark standing in for it**. | Three rules in one round read a surface mark instead of the object, **and all three erred toward making us look stronger**: a spelling one letter short walked a defect past its own gate; a guarantee gate called 5 of 6 rows strong on **cross-subject name collisions**; a recount said 6/6 strong and was an artefact. *A name is a mark someone else left.*

---

# PART III — rules earned 2026-08-23 02:0x–03:1x (rounds 677 r30 / w133 r26 / w61 r30)

## 12. Controls that cannot fail, and controls that overstate themselves

| rule | evidence |
|---|---|
| **A predicate whose failure mode is "unconditionally False" is invisible to negative controls BY CONSTRUCTION. Every boolean predicate ships with at least one input on which it MUST return True.** | The e255 defect — three operations plus a **dangling row index** — returns False on every input, so it **agrees with every negative control ever written** and disagrees only with a positive one. The planner wrote it in the script auditing it, ran three negative controls, and all three passed. |
| **A control that overstates its own coverage is the same species it was built to catch.** | The new kernel's docstring claimed its op-count audit *"would have caught BOTH e255 defects at import."* Tested: a file that **imports the kernel** and writes the defect verbatim still returns the wrong answer. **A dangling row index is not expressible as a tree**, so the audit — which audits trees — never sees it. |
| **The control that caught a defect may be a coincidence of the DEFECT'S SHAPE rather than a property of the witness. Ask what the witness would have said about a neighbouring defect.** | (R30/IDEMPOTENT-BLIND): the order-16 witness is **idempotent**, and on an idempotent magma the four-operation variant is TRUE. Had the round written that variant, **its own witness would have agreed and the defect would have shipped.** *A memorial cannot notice that its own witness is blind.* |
| **A checked implementation EXISTING is not the control. The control is a name, in a known place, that a sweep proves is the only place.** | A correct three-operation `e255` had sat at `r3f_enum.py:295` since round 3-F. **Neither defective round imported it.** RULING CO amended: *one checked implementation, in a named location, with a sweep that proves there is no second one.* |
| **Two incomplete detectors with different blind spots beat one better regex.** | D-CLOSE **missed the single most consequential site** (the claim wrapped across a line break inside its regex window); D-HEDGE caught it. Neither was complete; together they were sufficient. Redundancy, not refinement. |

## 13. Repairs, names, and what a fix can destroy

| rule | evidence |
|---|---|
| **A repair that checks bodies and not names is not a class fix.** | Repair AG3 called itself *"a class fix at both sites"*; the class had **five**. One of the three it missed was **Corollary C1-C's own TITLE** — *the statement's name carried the over-read while its body carried the hedge.* Eighth class-vs-instance instance on that line, committed **by the repair that was itself fixing a carrier defect**. |
| **Freeze DATA alongside predicates. A retrofit that eliminates re-typing can destroy the only comparison target.** | The order-16 table's pre-retrofit literal vanished: the consuming file now imports it, and the historical freeze kept **predicates but zero data**. What remained was self-consistency — and *well-formed ∧ E677 ∧ E255 does not pin a table uniquely*, so a drifted transcription would pass every check we still hold. S-9 arriving through a **fix** instead of a claim. |
| **Hand-built objects are claims; searched-and-admitted objects are results.** | One line hand-built three held-out hosts and its own precondition object **rejected all three**, each carrying an induced P₇ — on the object whose hypothesis is *no induced P₇*. The same night, another line hand-transcribed a table and dropped six rows. **Search the space and let the decider admit.** |

## 14. Accounting rules apply to the planner, not only to owners

| rule | evidence |
|---|---|
| **Family accounting is PER-STATEMENT — including for the planner's own blockers.** | The planner escalated a spend decision to the top of the status file on "the S3 surface is one round from closing." False at **twelve sites over eleven rounds**, two of them the planner's own. The per-statement grep — *every brief this line ever dispatched* — showed the cap blocked **one** statement and that the other half of the surface had **two clean families available at zero cost, all along.** The rule was the session's first ruling; it was applied to every owner and never to the blocker. |
| **A number on an ASSEMBLY is a handle that travels without its conditionality. The condition goes in the STATEMENT, not a remark.** | Minting the §35–§37 assembly gives future rounds an address they can cite while leaving "modulo single-source enumerations" behind. RULING AZ's import problem arriving **from inside our own ledger** rather than from a brief. |
| **No number of readers retires "must be taken as reported." Only a second implementation does.** | A judge returned CLEAN while refusing **all four** held-out quantities the load-bearing identity is arithmetic on. A clean verdict from a judge who computed nothing is real evidence about *links* and near-zero evidence about *computations*. |
| **The weaker statement cannot be closed through a door the stronger one was just withheld from.** | A corollary of a result the owner had voluntarily declined to bank would have closed a pocket on exactly the base the parent was refused on — leaving a closed pocket resting on an open link. |
| **Measure the blast radius of a carrier defect; it is often smaller than the site count and that is worth knowing precisely.** | Twelve carrier sites, eleven rounds — and the claim occurred in **zero briefs**. It cost a wrong dispatch reason and a wrong user-facing escalation; it contaminated **no round and no theorem**. |

### 14b. The planner's own record-keeping is not exempt

| rule | evidence |
|---|---|
| **Every timestamp is READ FROM THE CLOCK, never extrapolated from the last one written.** `date` is one call; a drifting sequence is unrecoverable. | Every timestamp the planner wrote in one working session ran **1.5–2 hours ahead of the true clock** — certs stamped 02:3x / 02:4x / 03:0x and a status file stamped 03:1x, against file mtimes of **01:13 / 01:16 / 01:18 / 01:20**. Nobody caught it for four documents because a plausible time never looks wrong. |
| **A timestamp inherited from a note is an inherited label.** | The drift began by taking the predecessor's *written* time as the current time and incrementing by felt elapsed time. That is trap 4 — *a note's timestamp is not its content's date* — **from our own scouting file, pointing inward, and propagated by the person who filed it.** |
| **Timestamps are load-bearing: they are how a handover reconstructs the ORDER of events**, and order is what every stall diagnosis and every "who knew what when" question runs on. Treat them as data, not decoration. | This project's own founding incident — a 9-hour predecessor stall — was diagnosed entirely from event ordering. |

---

# PART IV — rules earned 2026-08-23 01:3x–01:5x (rounds 677 r31 / w133 r27 / w61 r31)

## 15. The duplicate that must not be eliminated

**RULING CO″.** RULING AY says *eliminate the duplicate rather than check it.* **An adversarial
re-implementation is the exception, and it must be named or AY will eventually eat the only
independent check we have.**

| rule | evidence |
|---|---|
| An independent implementation is **not** a duplicate to remove — its whole value is that it shares no code with its subject. It gets its own `INDEPENDENT` scope class so a sweep can tell it from a lazy copy. | A sweep flagged the **planner's own** verification script for re-typing a helper, and the correct fix was *not* "import the kernel": that file's entire value was that it imported nothing. |
| **Its price is measured agreement by a check that CAN FAIL.** Agreement with no demonstrated capacity to disagree is not evidence. | 320 comparisons, 0 disagreements — **with a positive control showing the two implementations do disagree on the four-operation term.** |
| **A re-implementation that finds a defect in the original when the defect is in its own EXPECTATION is how a second tool manufactures a false positive.** Check the expectation before believing the disagreement. | Three of one round's pre-registered expectations were wrong and the draft was right — the author reported it first and called it the worst available outcome. Separately: a control expectation `min_alpha([3,1,1,1])` was wrong and the instrument right; the run exited 2 and produced no key. *21 of 22 was not enough.* |
| **Frame counts are scheme-dependent and are NOT evidence of agreement; survivor sets are.** | Two tools' frame counts differed by counting scheme while every conclusion agreed exactly. The author declined to count 18 scheme-dependent cells as hits. |

## 16. Gates that cannot see their own population

| rule | evidence |
|---|---|
| **RULING CV — a gate addressed by LINE NUMBER is silently invalidated by any edit above it.** Pin **after** in-place corrections, never before; prefer an anchor that survives insertion (a statement's own address). | A boundary pinned at 5202 moved 8 lines when a correction was entered above it, **and the gate kept reporting PASS over a subtly wrong population.** Second occurrence of the same defect on that line. |
| **RULING CW — a quoted retraction is not a carrier, but a sweep cannot tell.** Mark it (`<!-- RETRACTED-QUOTE -->`) and require sweeps to honour the marker **and positive-control that they still fire on the same string without it.** | A corrected status file necessarily quotes the claim it retracts. A gate that cannot distinguish a claim from its retraction either produces false positives forever or gets switched off. |
| **A gate returning 0 has said nothing until it has been shown returning 1 — in the same run, on a corrupted copy.** | Now standing on all lines; the round that adopted it shipped five gates each demonstrated firing. |
| **Count by SHAPE, not by name.** | A sweep counting `def` names reported `UNSCOPED: NONE`; a sweep counting shapes with identifiers erased found **10 more files** holding a shape-exact re-typing. The earlier round had identified the exact reason its own count under-reported — and fixed the instance rather than the counting rule. |

## 17. Classes, and who is allowed to declare one closed

| rule | evidence |
|---|---|
| **A phrase-hunting detector cannot close a class, because a class is defined by its CLAIM and a detector matches its WORDING.** Closing a class requires reading, or an instrument that matches meaning. | The sixth live site of one over-read class wore *"a named reduction"* for the same claim that every detector hunted as *"reduced to"*. **Nine class-vs-instance instances on that line, and three consecutive rounds where a repair declaring its own class closed left a site standing.** |
| **Build briefs from SOURCES, not from summaries.** | That sixth site was found by reading the section the brief was built from — not by re-running either detector. |
| **A line that has failed review twice designs its next review against its own recorded failure species BY NAME, or the review is not commissioned.** | Two papers, both INVALID on first pass: **nine CRITICAL findings, ZERO computational errors, all one species** — *statement stronger than source*. The species name was already in the ledger, named by the reviewer who found it, and **had never once been used to design a review.** RULING CO one level up: a lesson recorded in prose is not a control, applied to the review process itself. |

## 18. The planner's gates are gates too

| rule | evidence |
|---|---|
| **A pre-registered discharge condition must name EVERY dependency of the thing it discharges.** Naming one of two makes the gate immune to hindsight and blind to half the claim. | A corollary's discharge condition named only the enumerations; the parent statement's adoption and the links' family count were both live and neither entered the gate. **The instrument whose entire purpose is immunity to hindsight, under-specified by the person who wrote it** — and the cost lands on the owner, who built to spec and does not get the promotion. When this happens: honour what was written, certify it separately and permanently, and name the gap as yours rather than smuggling the new requirement in. |
| **A qualifier may be amended only by a round that moves the fact it dates. A date bump alone is a carrier defect — the number looks stronger with no new evidence.** Amend to carry the STATE, not a newer date. | *"single-source as of r26"* → *"two independent implementations agreeing as of r27, still single-author and single-specification"*. |
| **"The source says X" is not evidence about the artifact.** | A claim about a published PDF was filed on the evidence of the repository source. Measured properly — by decompressing the PDF's content streams — it held. Right, and under-evidenced. S-9 again. |
| **A detector that must recognise a secret is the most likely place for that secret to be written down.** Construct it from parts. | A gate built to prevent a private address from leaking **contained the private address in its own regex.** |
| **When every owner overruns the same budget in the same round, that is a budget defect, not three lapses — and it belongs to whoever set it.** | Three lines, three overruns (≈60 / ≈75 / ≈95 min against 45), all self-reported. Corrected to 90 min for build-and-dispatch rounds, 45 for adjudication-only, plus: **complete a guaranteed deliverable FIRST, then spend the remainder on the ambitious part.** |

### 18b. A named species is a corpus-wide obligation

| rule | evidence |
|---|---|
| **A failure species, once named, is swept across the WHOLE corpus — not only the artefact where it was found.** | A line established that both its prior papers died of one species (nine CRITICAL, zero computational errors) and designed a review around it **for its third paper**. Right, and it stopped at its own line. The species was equally about **everything we had published**: seven DOIs, one known to carry it, six never examined. The sweep cost one script and no quota. |
| **When a locating instrument produces a headline number, compute the DENSITY before reporting it** — otherwise the instrument's own output becomes an instance of the species it hunts. | 92% of the corpus's statement-level direction claims sat in one paper. That paper is a *structure-theory* paper, where equivalences are the natural content, so the density is what the genre looks like. **Reading it as evidence of defect would have been "statement stronger than source" committed by the sweep for it.** The defensible claim was about **exposure**, not defect. |
| **A zero from a locating detector is not a clearance.** Say "this detector found nothing", never "this artefact is clean". | Three papers returned zero. Clearing them of a species requires a reading, and the project's own ruling says a phrase detector cannot close a class. |

---

# PART V — rules earned 2026-08-23 02:0x–02:3x (w133 r28 / w61 r32)

## 19. Held-out harnesses, third pass

| rule | evidence |
|---|---|
| **RULING CX — a held-out answer must be proved UNIQUE, not merely proved correct.** Re-deriving a key agrees with itself and says nothing; only a uniqueness check fires. A row that fails uniqueness is not gradeable: accept any correct answer, or strike it. | A Tier-H row asked *"which graph contains a 4-cycle, and its 4 vertices."* The graph carries **two** such 4-sets; the key recorded one. **A reviewer answering the other is CORRECT and is scored VOID — review voided, mathematics included.** The row had already run live in an earlier gate that passed: **that PASS was one coin-flip from voiding a clean review.** The risk shape is a row answered by a *choice among equivalent objects*; rows answered by a single integer cannot carry it. |
| **A pass is citable only with its null, and the null must be MEASURED where it can be.** | One line computed its conjunction (~1/4.8e6) before claiming anything — **and r35 measured that even that figure was over-stated: it multiplied in a VERDICT row its own pre-registered rule forbids citing, and one of its rows was disclosed in English in the shipped paper. Re-issued at 1-in-240 000, conditional on an unverified declaration. A computed null is still a null that has to be audited**; another dispatched, graded two families clean, and had computed no rate at all. Enumerating one of its four answered rows exhaustively gave a **true answer space of size 2** — a correct row and a near-worthless one. |
| **The judge's PROSE overrides the judge's VERDICT BOX.** A judge who describes a defect has found one, whatever box they ticked. | A judge called a step *"a silent but critical leap"* relying on an *"unspoken mechanism"* — and graded the statement `NONE`. Counted as a GAP. The mirror of the standing rule that a CLEAN verdict from a judge who computed nothing is near-zero evidence. |
| **Agreement on CORRECT values is the fluent-echo shape, not a confirmation.** It is consistent with independent computation *and* with a shared shortcut; the discriminator — agreement on a **wrong** value — never fires on a clean run. | Six statements, `TRUE/VALID/NONE` from both families. The two findings worth keeping were both in the free-text section, not in the verdict grid. |

## 20. Controls, fourth pass — the one that invalidated a rule set the same night

**RULING CZ — a positive control must inject the HARDEST form of the species, not a canonical one.**

| rule | evidence |
|---|---|
| *"Shown firing on a corrupted copy in the same run"* is **necessary and NOT sufficient**. The corruption must be **adversarially chosen**: interposed words, alternate wording for the same claim, the variant that actually appeared in the wild — preferably the real historical instance. | A gate matched `closes the S3 surface` but not `closes <NAME>'s S3 surface` — one interposed possessive. Measured across five files: **34 occurrences, 18 seen, 16 missed.** Its positive control had injected the **easy** form, so the gate was *correctly shown firing* under a rule set hours earlier **and was blind to its own species the entire time** — while the real instance sat inside the very repair the gate existed to enforce. |
| **RULING CY — a check that CANNOT PASS is as uninformative as one that cannot fail.** V7 has a second direction. Show both. | A leak gate matched bare answer strings in 35 KB, "found" the digits it was hunting, and could not have passed on any brief — reporting a leak that was not there. |
| **A gate addressed by anchor should PROVE its addressing is right**, in the same run, by reproducing the failure the addressing prevents. | One gate inserted 40 lines above its target on purpose and asserted the anchor verdict unchanged while the line-number gate answering the same question was destroyed. First gate on the project to prove its own addressing scheme. |

## 21. Minting, and what a conditional bank actually banks

| rule | evidence |
|---|---|
| **Banking a corollary "conditional on an unadopted parent" does not produce the corollary. It produces a different object: the IMPLICATION.** That implication is bankable and worth minting — it is true regardless of whether the parent lands — but the entry must say it is not the corollary, does not close the pocket, and does not discharge the parent's condition. Name it as an implication, never by the corollary's name. | Otherwise the address gets cited as though the corollary were established — the carrier defect that line had already hit four times. |
| **Status leaks in verbatim extracts: declared scrub, CATEGORY AND COUNT ONLY.** A silent scrub misrepresents the verbatim guarantee; a declared *disclosure* leaves the bias on the page; a declared scrub that lists the removed text re-injects it. Disclose the category and count, then assert by diff that only annotation tokens moved. | *"Verbatim except N declared annotations"* is a weaker claim that is actually true — better than a stronger one that is not. |
| **A brief cleared for dispatch is not a brief that has been audited.** | A brief already built and authorised was audited before sending and found to carry **five** blockers, one fatal. The audit happened only because a scheduling decision, made for unrelated reasons, deferred the seat. **Luck, and it must be recorded as luck.** |

### 21b. When the tooling refuses

| rule | evidence |
|---|---|
| **A tool refusal is an OPERATIONAL condition, not a safety verdict on the work, and not a licence to substitute.** Attempt one diagnostic, confirm, stop, and **report the gap as a gap** — do not route around it, do not delegate it to a subagent, and above all do not file a hand argument in a measurement's clothes. Escalate; whoever still has execution runs it. | An owner wrote the required script, had execution refused for the rest of its session, and filed the result **UNVERIFIED rather than verified** — explicitly declining to quote a rate over hand-proved rows because *"rows surviving a hand proof are not the same population as rows surviving an executed check."* The planner's execution was alive, ran the same script unmodified, and it passed 6 of 6 with its own controls live. **The honesty is what made the recovery possible: the artefact was complete, only unrun.** This project's founding incident was a nine-hour stall on a filter condition; this one cost a single round nothing. |
| **A section heading is a claim.** | A summary titled *"per row, and the recomputed conjunction rate"* printed no rate. This month's species in miniature — a heading stronger than its section — inside the very instrument built to catch overclaiming. |
| **Luck must be filed as luck.** Twice in one night: a scheduling decision made for unrelated reasons prevented a defective dispatch, and a held-out row landed safe **by one word** (asking for a minimum *value*, not the realizing graph). Both were recorded as luck by the people who benefited from them. | A project that banks luck as judgement stops being able to tell the difference, and the next round inherits a control it does not have. |

---

# PART VI — rules earned 2026-08-23 02:5x (677 r32, the third INVALID)

## 22. The species, confirmed on a third data point

**Three papers, three `INVALID` first passes, ONE species (statement stronger than source), ZERO
computational errors in any of them.** r31 named the taxonomy from two; r32 is the third and
**confirms it rather than merely fitting it.**

| rule | evidence |
|---|---|
| **"Blocked on labels" and "blocked on a theorem" are different states and the ledger must distinguish them.** | Six CRITICAL findings, all S5 umbrella labels wider than their artefacts. The paper's four mathematical claims were untouched. A line that records both as "INVALID" cannot tell a wording pass from a retraction. |
| **A clean gate is evidence about the gate, never about the thing beneath it.** | A 14-gate pre-dispatch pass cleared the brief; **the brief then found a defect in the control that pass was built on top of.** That sequence is what a working pass looks like, not a failure of one. |
| **We do not adopt a finding because a judge we respect made it.** Re-derive before adopting; the ones you cannot re-derive stay plausible and unadopted. | One of six was re-derived and adopted; five remain unverified and explicitly not adopted. This is the fluent-echo error with the sign flipped, and it costs the same. |
| **A reviewer's arithmetic is not exempt because its verdict is useful to us.** | The reviewer's own justification cited "573 triples" for a population of 445 — right answer, uncounted population: *the species it was hired to find, inside its own reasoning.* Recorded, not inherited. |

## 23. RULING CZ, demonstrated on the planner

| rule | evidence |
|---|---|
| **A fault set drawn from the dimensions a check already measures proves NOTHING.** Name what the check does *not* look at, and injure that. | `_shape_audit()` checks operation count and variable set. The planner injected four faults — **all four in those same two dimensions** — and certified the guard "LIVE 4/4". A judge then supplied the missing class: `x = (x◇x)◇(x◇x)`, three operations, variables `{x}`, **passes silently and is a genuinely different law** (four separating order-2 magmas). **The function is named `_shape_audit` and audits everything except the shape.** The rule was authored hours after the violation, by its author, about someone else's gate. |
| **RULING DA — before dispatch, assert that no artefact you ship, and no file in any path the brief points the reviewer at, contains the answer to a held-out row.** Positive-control on the HARD form: an answer appearing *derived or reformatted* — a sum, a separator-formatted count, a value inside a larger tuple — never bare digits. | **Two of three computational rows on one line's flagship table were answerable by grep**, one of them printed verbatim in a log inside the directory the brief told the reviewer to sweep. **All row-quality gates were passing and none asked.** |
| **r33, owner-677 — RULING DA's OWN GATE, POSITIVE-CONTROLLED ON THE HARD FORM, SCORES `0/4`.** G14's control was the real historical leak, `"<answer> occurrences found"` — **the EASY form, and drawn from the one dimension `g14` measures**: a bare decimal token with a counting noun within 30 chars *after* it. Four hard plants: an answer **inside a tuple** (`(3,1)` — dropped by `len(tok) < 2`) **BLIND**; an answer **stated as a sum** (`10 files and 9 further`) **BLIND**; the **noun before the number** (`occurrences: 19`) **BLIND**; **separator-formatted UNTESTED — no COMP answer on that key has four digits, so no separator form exists to plant.** **G14's measured coverage is a bare decimal token immediately preceding a counting noun, and it must not be described as covering "any artefact containing a held-out answer."** Whoever ports it ports that scope with it. | **The owner's own first hard control reported `caught` and was a fake**: `"{:,}".format(118)` is `"118"`, byte-identical to the easy plant. It was the easy form wearing the hard form's label and it scored a point *for* the gate. **RULING CZ eats its own author's fault sets too, one ruling later, in the gate the same ruling created.** |
| **Fix a compromised row by REDESIGN, not by instructing the reviewer not to look.** | The row was changed to count occurrences (19) rather than files (10). The judge then read the log saying 10 and **answered 19 from its own census** — the strongest evidence this project has produced that a held-out row discriminates. |

## 24. The search asymmetry

| rule | evidence |
|---|---|
| **A search that RETURNS witnesses is self-validating — each witness is independently checkable. A search that returns NOTHING is worthless without a positive control.** | A separator search printed `*** DEAD ***` on its own positive control (mis-chosen: at n=2 the two properties coincide, so nothing could separate them there) **and the finding still stood**, because it returned four witnesses and one was verified by hand. Every other control rule in this document addresses the empty case; this is the one place the asymmetry rescues a result. Third mis-chosen planner control in one session — the pattern is real and the rule above is why it did not cost anything this time. |

---

# PART VII — rules earned 2026-08-23 02:2x (w61 r33, the round that stopped a promotion)

## 25. What a pre-registered gate actually has to say

| rule | evidence |
|---|---|
| **Pre-register the CONCLUSION the evidence must support, not the PROCEDURE that would normally support it.** | Two under-specified promotion gates in one session, by the same author, in the same way: one required *"a second positive-controlled implementation"*, the other required *"the blind-guess rate computed"*. Both acts were performed exactly as written. Neither established what the gate existed to establish. |
| **A gate that requires MEASURING an instrument implicitly requires the instrument to DISCRIMINATE. When the measurement shows it does not, the gate is VOID — not passed, not failed.** A void instrument neither promotes nor demotes; it means there is no reading, and the decision must rest on whatever else exists. | A held-out harness measured at **1.0–1.6 bits** (standing comparator 7.9; a sibling line's 22.2). By the letter its gate passed. It established nothing. |
| **RULING DB — no two held-out rows may share a latent.** For every pair, assert that fixing one does not determine the other; where it does, they count as ONE row for the conjunction. | Three rows of a flagship table were the same quantity in three disguises — **and the identity converting them was printed in the brief as a numbered statement.** One guess answered all three. The product `1/36` was not citable; the honest figure was `1/3`. **RULING CP checked rows against shortcuts and never against each other.** |
| **Independence is ESTABLISHED before rows are multiplied — and seats are not independent either.** | Seat multiplication was refused on the same round: `1/3` was not squared to `1/9`, because seat independence had already been declined as the fluent-echo shape. |

## 26. The safety layer is not exempt

| rule | evidence |
|---|---|
| **A gate whose positive control uses the GENERIC form of what it hunts certifies nothing about the real forms.** | An API-key leak gate, `sk-[A-Za-z0-9]{8,}`, fired cleanly on every run for the life of the project and **could catch neither real key format in use** — both put a short segment before the next hyphen. Its control had always injected the generic shape. RULING CZ, arriving in the safety layer. |
| **A blind gate obliges a scan.** Discovering a safety check never worked is not the end of the task; it is the beginning of finding out what got past it. | 241,949 files across repo and sandbox: **zero real key material**; the only matches were the round's own synthetic probes, confirmed by structure and context **without printing any of them**, scanner positive-controlled on a planted needle. |
| **Scope the finding precisely: name what the real protection was.** | The standing protection was never the gate — keys live outside the repo at `-rw-------` and are never quoted. **The gate was a second line of defence that turned out not to exist, and nothing reached the first one.** Reporting it as "our key protection failed" would have been this month's species applied to a security claim. |

## 27. Reading, finally beating regex on the record

| rule | evidence |
|---|---|
| **Some classes cannot be closed by any detector because the distinguishing feature is a PRONOUN'S REFERENT.** | 33 flagged sites adjudicated by reading: 18 marked retractions, 4 negation false positives, 7 correctly scoped, 2 detector-spec — and **3 LIVE CARRIERS no regex distinguishes from correct text.** One read *"the only statement standing between X and a closed surface"*: the interposition species one scale down, **inside the class the repair existed to close.** |
| **When you read output, read the COLUMNS, not only the rows.** | A verification output printed outcome pairs `(8,2) (7,2) (4,2)` on three consecutive lines. The planner ran it, certified uniqueness from it, and did not remark that **the same number stood in every row** — that column was the shared latent that later voided the harness. |
| **A summary line is a claim and must match the table above it.** | In the very cert reporting the above, a scan printed *"all matches are single-character placeholders"* directly beneath a table showing four of six with sixteen distinct characters. **The conclusion held; the stated reason did not.** |

---

# PART VIII — rules earned 2026-08-23 03:0x (w61 r34, w133 r29, 677 r33)

## 28. RULING DC — the hole under the whole review apparatus

> **No defect is planted anywhere in the reviewed statements. When the reviewed file is clean, the
> correct verdict and the fluent-echo verdict are THE SAME CELLS. The verdict grid could never have
> discriminated a reader from an echo, whatever the judge did.**

**That is RULING CZ in the review layer: a fault set drawn from the empty set.** We spent a whole
session insisting a control must be shown firing, while pointing every judge at text we believed
correct — where there is nothing to fire on.

**RULING DC: a brief whose purpose is to establish ENGAGEMENT must plant a defect.** Engagement has
exactly three routes and no others:
1. **a planted defect the judge must find** — never attempted on this project until now;
2. **a held-out harness with MEASURED discrimination** — one line's was 22 bits and counted; another's
   was **1.0–1.6 bits** and did not;
3. **the judge producing something we did not have** — the only route that has actually worked
   (an external judge handed us a missing lemma, and the determination audit confirmed those two
   claims appear nowhere in the brief).

**Owed, and it belongs to the planner:** re-audit every banked "clean round" and record which of the
three routes established engagement for it. Where none did, the round stays banked as a
**correctness** review and is relabelled as carrying **no engagement evidence**. That is a labelling
correction, not a retraction — and one line has now failed three papers on exactly that distinction.

| rule | evidence |
|---|---|
| **A brief can DETERMINE its own review.** Test it by inverting the row-determination audit onto the judge's OUTPUT: does the brief fix each claim the judge made? | **17 of 17 gradeable claims DETERMINED, zero free.** The brief named the joint it wanted scrutinised **in bold**, supplied both halves of the answer, and **explicitly solicited the judge's warning sentence** — then the round recorded that finding as *"arrived at independently."* Both the owner's sentence and the planner's repetition of it were withdrawn. |
| **The audit needs a control that can return NOT-DETERMINED**, or it is an instrument that only knows one word. | The same audit returned **NOT-DETERMINED** for the other family's lemma claims, and the script **refuses to certify** if it cannot. |
| **Determination and guessability are different failure modes.** A claim can be free of the brief's text and still worthless. | A discharge condition, read at the letter, was satisfiable by the held-out rows — whose numbers the brief does not print. Counting them would have granted a promotion **on the instrument just ruled void.** The owner refused the loophole rather than take the promotion the planner's own wording offered. |

## 29. Amendments to rules issued the same night

| rule | evidence |
|---|---|
| **RULING CZ′ — a control must fire ON THE FEATURE, not merely on the instance string. Minimal-pair any instance carrying two species.** | A probe read PASS because it fired on a *different* species in the same sentence; minimal-pairing silenced it. Fifth instrument on one line to read clean for the wrong reason. **23/24 named beats 20/20 bought** — do not widen a gate to buy a number. |
| **RULING DA's measured coverage is "a bare decimal token immediately preceding a counting noun" — NOT "any artefact containing a held-out answer."** | The gate scored **0/4 on the hard form**: blind to a value inside a tuple, to a sum, to noun-before-number. **Its own separator plant reported `caught` because `"{:,}".format(118)` is byte-identical to the easy plant — the easy form wearing the hard form's label, scoring a point for the gate.** The planner had propagated the wider wording: **a claim stronger than its instrument, inside the ruling about claims stronger than their instruments.** |
| **RULING DB runs AFTER the hand-computability filter, never before.** A row set cannot be simultaneously hand-derivable, latent-independent and numerous — **any two of three.** | Census: 36,513 lists, 17 distinct residues (mode 23.6%) — refuting its author's own prediction of near-constancy. Restricted to hand-computable rows: **4 residues, top at 50.8%, and the modal value was not the one the round had drawn.** |
| **A channel-specific constraint is not a channel-wide gap.** | "codex is at <25% of its weekly limit" was read as "no second family exists". A 96-file measured sweep found **two** clean available families. *"Your resource signal was sound; the inference from it was not."* |

## 30. Privacy, and the shape it takes here

| rule | evidence |
|---|---|
| **Any printer that echoes a real instance must redact.** | A re-control script's printer echoes the real instance of whatever species it tests — and for the email-leak probes **the real instance IS the protected string.** It wrote the private local-part into a repo artifact **while testing the gate that forbids it.** |
| **Sweep for the protected string by OUTBOUND CONTEXT, not by presence.** Presence in an internal note is not the same defect as presence in a request header. | 8 files contained the address; **7 were inert internal notes and exactly one was outbound** — a contact address in an HTTP `User-Agent`, sent to every server that script contacted. Polite-crawler convention, right intent, wrong string: replaced with the public identity. |

---

# PART IX — rules earned 2026-08-23 03:1x–03:2x (677 r34, w61 r35)

## 31. RULING DD — the fourth verdict category

> **A judge that computes, computes FALLIBLY, is not an echo, and is not a clearance.**

Not VOID (it did real work), not CLEAN (it got a row wrong), not fluent echo (it produced data we do
not publish). **Log as ENGAGED-INCORRECT: engagement banked, verdict discarded, findings adjudicated
on merit.**

| rule | evidence |
|---|---|
| The three verdicts we had could not describe a real outcome, so we would have been forced to file it wrongly. | A judge returned CLEAN with **5/6 rows correct and one wrong**, and separately volunteered a five-way per-modulus split **no artefact of ours prints**, all five re-deriving exactly. The conjunction failed, so the CLEAN was uncitable — and the volunteered data is the only engagement evidence any round on that line has produced. |
| **A brief can make a MISS informative.** With a planted defect, a miss plus an all-clean verdict grid is the fluent-echo signature **confirmed on a text known not to be clean** — the first outcome this project can produce that counts **against** a seat. | Every prior design could yield evidence *for* a seat or nothing at all. RULING DC named the gap; the planted-defect brief supplies the missing half. |
| **Pre-register the discrimination in tiers, and make the weakest tier buy nothing.** | HIT-STRONG (direction **and** witness) → engagement. HIT-MECHANISM (names the false justification) → reduced weight. HIT-WEAK (*"the biconditional is unjustified"*) → **nothing, because an echo can produce that sentence.** MISS is **not** a VOID: void is reserved for demonstrated fabrication. |
| **A held brief that gets edited is a NEW brief with an unpre-registered discrimination.** The pre-registration is the asset. | — |
| **Planting costs honesty and the cost must be declared.** | Two honest instructions had to be removed because they named the plant's mechanism: *"the brief is less honest about what it wants than the previous one was."* Declared as a hunk-level diff, with the build refusing on undeclared drift. |

## 32. Where the leak actually was

| rule | evidence |
|---|---|
| **The leak vector is not the brief. Sweep every path the brief POINTS AT, including your own output files.** | The held-out key was printed in full inside the directory a row told the reviewer to sweep, under a header reading *"this file is NEVER pasted into a brief"* — **true, and irrelevant.** The judge had filesystem access and was demonstrably reading `.out` files in that directory. |
| **A declaration is not a measurement.** Where a shortcut was AVAILABLE and its use cannot be measured, cite the result as *conditional on an unverified declaration* — never at face value. | A 7/7 held-out pass at ~1/4.8e6 rests on a judge's self-report that it did not open a file it could see. **Whether it was taken is not measured and cannot now be measured.** |
| **A gate scoped to one syntactic form does not cover the other form of the same fact — including three lines above itself.** | The same file leaked the answer **in prose**, above its own check that no output file printed it; the check was scoped noun-AFTER. **The leak was in the same file as the check that says it isn't.** |
| **An answer spelled out in ENGLISH is a leak.** Detectors covering tokens, containers, sums and separators are blind to words. | A row's answer sat in the shipped paper as *"three applications plus a dangling subscript"* — **the reviewer cited that sentence as its justification, which is how it was found.** The row was never held out from anyone who read the paper: struck from two tables retroactively. |
| **A check that runs BEFORE its own output exists cannot see its own output.** Post-run `grep -rlF` after any script that writes a sensitive string. | A containment printer echoed the very string it was containing into its own `.out` — a carrier structurally invisible to the scan that preceded the redirect. |

## 33. Visibility and liveness are different properties

| rule | evidence |
|---|---|
| **A correction must REPLACE the retracted text and MARK it — not sit above it.** A cert keeps the retraction visible because the crossing point is the finding; the retracted text must simultaneously be unreadable as live by a sweep. | **Eight correction boxes across six certs, and not one carried the `RETRACTED-QUOTE` marker its own author had invented.** The flagged sentence still stood verbatim below its correction, and a grep-based carrier sweep — *the very instrument that produced the repair being corrected* — would have read it as live. The enumeration above it also still said "Two" after the count fell to one. |
| **Prescribing the wrong fix is worse than prescribing none: it closes the question.** | A planner instruction to drop a token-length guard was necessary and **not sufficient** — a tier filter upstream meant the target never reached the tokeniser — and dropping the guard alone **floods** the gate (41 base-rate hits against 0 for the rows that mattered) rather than hardening it. |
| **RULING DB gains a third condition: ANSWER-VALUE independence.** Shared latent was the known failure; **shared answer is a distinct one.** | A row draw produced two rows with different latents and the same answer. |
| **A wrapper that swallows an engine's thinking budget reports a reachable channel as unreachable.** Any past "channel unreachable" conclusion reached through such a wrapper is unsafe until re-measured. | A call script at `max_tokens=200` returned `API-ERROR: unknown` on a five-character brief because the engine spent 141 tokens thinking before emitting five characters. |

## 34. RULING DE — determinedness has two axes, and only one was gated

> **RULING DA asks whether the ANSWER was reachable from what we shipped.
> RULING DE asks whether the VERDICT was.**

**Before dispatch, assert that the brief does not supply BOTH the LOCATION and the METHOD of the
finding it is most likely to receive.** Where it must — a guard that cannot travel has to be
declared somehow — **the resulting finding is recorded as un-independent and does not count as
engagement.**

| rule | evidence |
|---|---|
| A brief can hand a judge its own verdict without handing it an answer. | One paragraph (a) declared certain tables un-re-runnable, naming their sizes, and (b) **prescribed the exact consistency check to apply.** The returned GAP was at those tables, found by that check. **Location and method both shipped in the bytes.** |
| **A brief can prescribe a check its own artefacts cannot pass — and then receive that failure as the verdict.** | `832 = 2⁶·13`, `858 = 2·3·11·13`, `872 = 2³·109` against a prescribed *"N frames is the product of the free bits"*. **A gate that manufactures the defect it reports, arriving in a brief instead of a checker.** |
| **Separate the determined part of a finding from the residue, and bank only the residue.** | The reviewer **factored four correctly and declined five**, with three strongly justified and two weakly — *not available from the guard*. That is the round's real output, and it was separated out rather than banked wholesale. |
| **State the MECHANISM, not just the conclusion. A right answer from a constant is indistinguishable in a log from a right answer from a measurement.** | A field that is `""` **always** was read as evidence of "still generating". The conclusion was correct; the stated mechanism was wrong. |
| **Agreement is a cross-check only if the second implementation ran FIRST and independently.** Recompute, then compare to the key — never grade the key against itself. | 7/7 with truths recomputed from raw inputs before any comparison; a deliberately-wrong whole-document comparator run beside the gate **passes** on value-preserving corruptions, proving the gate reads the feature. |
| **A residual can be SPENT.** Hosts burned across two families cannot grade a third; a third family needs fresh hosts *and* a fresh key. | Stated by the owner unprompted, at the moment it became true. |

## 35. Boundaries, controls, and what to do with a defect you cannot fix

| rule | evidence |
|---|---|
| **When a lemma fails at a boundary, PRINT THE BOUNDARY. Restricting the range to exclude it hides the very object the theorem is about.** | A lemma claimed a closed form *"for every odd `c`"* and was **false at `c = 1`**, because that case steps onto a **terminal** list so an increment is never spent. The author corrected it by printing the boundary rather than narrowing the hypothesis — **and the boundary turned out to be the near-miss family the whole theorem is about.** |
| **A must-return-True input that is itself FALSE does not get deleted — it becomes a new category.** The instrument gains a category instead of losing a control. | A positive control contained a value that **aborts**; it was moved to a new `MUST_ABORT` class. |
| **Naming an unfixable carrier beats fixing it** when the fix would break a pre-registration. State the precondition beside it. | A stale status line lives in the builder that produced a HELD brief which is a *declared diff* against it; repairing the builder would invalidate the pre-registration that is the brief's entire value. Recorded UNFIXED, with the reason. |
| **RULING DF — when new results make a HELD brief stale, do not rebuild it. Pre-register an extra outcome for the staleness.** A judge reporting it has found something REAL but NOT THE PLANT: score it as a correctness finding, never as engagement, and **never merge the two in the accounting.** | A theorem proved after a brief was frozen made one of its inherited status lines false. Rebuilding would have destroyed the pre-registration; the discrimination is the asset. |
| **A four-round-old theorem becoming a special case of a lemma proved today is what progress looks like** — and it is a signal the right generalisation was found, not a redundancy to prune. | `C1-2` turned out to be the `\|μ\|=1` instance of `C1-J`. |
| **Test the hypothesis you carried in, and print the measurement when it dies.** | *"`k ≥ 4` is easier"* was raised one round and **refuted the next by its own authors**, with the distinct-base-shape counts printed: 25 / 108 / 256 / 413 / 517 at `k = 2…6`. What is easier at `k ≥ 4` is the **conclusion**, not the **proof**. |

## 36. RULING DG — what a held-out table can and cannot be an instrument against

> **A held-out table is an instrument only against a channel that CANNOT READ THE REPOSITORY.**
> Against a filesystem-capable judge it is citable only as *conditional on an unverified
> declaration* — permanently, and by construction.

| rule | evidence |
|---|---|
| **You cannot hold a table out from a judge that can read your ledger.** | A whole-tree sweep (322 files, 8 extensions — the prior sweep had covered 105 `.out` files only) found that **the ledger of record, in the same directory, carries 3 of the 5 rows in scope by itself.** *"A ledger cannot be sanitised without destroying the record it exists to be."* No gate-hardening changes this. |
| **The remedy is the CHANNEL, not the gate.** A browser-pasted brief is a channel that cannot read the repo, so the table is a valid instrument there and nowhere else. | The line's remaining gate could only ever be bought at a web seat. |
| **Emit secrets into a PIPE, not onto disk.** | The harness now prints answers only under an explicit flag its four consumers pass when they subprocess it: the key is on disk nowhere. **Relocating the file would have moved a leak the judge could still reach.** |
| **A wrong reason for a right decision matters, because the next decision may lean on it.** | A deferral was ordered on the ground that a file sat inside a live row's counted population. One line of source showed the scan reads `.py` only and the file was a `.out`: **the caution was right and the reason was false.** |
| **A row keyed on a single-digit component is not leak-checkable by ANY occurrence detector — in digits or in words.** Fix it by re-keying, never by a better detector. | A number-word detector fired on **six** places in the shipped paper, then measured its own base rate: **47 hits across 35 of 322 files, decidable corpus rate 0** — *"one operation" / "three applications" ARE this corpus.* Its fire is a **FLAG, not a decision.** A second component that is an indefinite article ("**a** dangling subscript") is unreachable by any of them, and was declared blind rather than counted. |
| **Never multiply a VERDICT row into a cited conjunction** — and check that the product you inherited did not. | A circulating `1/4.8e6` had multiplied in the verdict row, **three lines below the harness's own rule forbidding it**; the citable figure was `1/2.4e6`, and `1-in-240 000` after a disclosed row was struck. **A factor of 20, on a number the planner had certified twice and propagated into five of its own artefacts.** The comparison it supported survived (17.9 bits vs 1.6); the number did not. |
| **A sanitiser can half-fail SILENTLY and look like it worked.** | BSD `sed` ignores `\+`: the digit mask was dead while the word masks visibly fired, so the output *looked* sanitised. |
| **The constraint that names its own secret is a leak.** State the rule by description. | Six repo files carried a private address **inside the rule forbidding that address from appearing.** Redacted to a description — a rule saying "never write this literal" loses nothing by not writing it. Same shape as a key-leak gate that contained the key. |

## 37. DE sharpened, and the difference between a defect and a means

| rule | evidence |
|---|---|
| **RULING DE forbids handing the judge the LOCATION AND METHOD OF THE DEFECT YOU EXPECT. It does NOT forbid handing over the MEANS OF VERIFICATION. Those are opposite things.** Shipping a method that converts *"must be taken as reported"* into *"can be checked"* is a strict upgrade — ship it. | A guard paragraph had prescribed a check that produced a **fake** finding; the corrected text ships the real reconstruction structure instead. **The finding it previously invited was manufactured; with the structure shipped, any finding a reviewer makes is a real one** — and the tables become reviewer-checkable, which RULING CU said only a second implementation could buy. |
| **A prescribed check can be ILL-POSED rather than merely wrong**, and the distinction decides whether to repair or withdraw. | A population that is a **sum over branches** (`N = Σ_b (2^{f_b} − dup_b)`, 18 branches with five distinct `f_b`) was prescribed as **a product of "the free bits"** — a quantity that does not exist. **Seven of eight tables could not have passed** (a hand-written expectation said six; the machine said seven), and **one table passed the prescribed check BY ACCIDENT.** Withdrawn rather than repaired, because printing the branch list would have re-shipped the method. |
| **A defect in something already SENT is repaired in the SOURCE and the BUILDER; the dispatched artefact is left byte-identical, because it is evidence.** | A frame count wrong for six rounds shipped inside the very table a reviewer had been told was unreconstructible. The conclusion was unaffected — **but the number the reviewer was invited to check was false.** Draft got an erratum; the sent brief kept its md5. |
| **`exit 0` is a claim about the PROCESS, not about the WORK. Assert that every declared part executed.** | An `import` ran the previous round's whole program and `sys.exit(0)`'d out of PART 0 — **PARTS 1–5 never ran and the shell saw `EXIT=0`.** Caught by reading the output, never by the exit code. |
| **An instrument that FAILS once its own finding is repaired needs a two-sided regression** — assert the fixed artefact carries the new value *and* the frozen one still carries the old. | — |
| **Test the rival explanation before banking a finding as independent.** | A reviewer's flag was checked against "it flags everything": it had **passed** two other large quantities in the same link while flagging the one in question — so the flag was per-table, not a blanket. **Net: one half-finding, priced up from a weak decline.** |

## 38. An unstated scope makes a zero unfalsifiable

| rule | evidence |
|---|---|
| **A `0` is only a result if its SCOPE is printed beside it.** State what the sweep excluded, in the same sentence as the number. | A private-address sweep certified **"0 occurrences across repo and sandbox" twice**, and both runs silently skipped `.git`. Full-tree, three files carried it — committer-identity **reflog** lines in a vendored clone. **The exposure was then re-checked and was NIL** (`git log --all` over every commit object: zero; reflogs are local and never pushed). **The conclusion survived; the claim as stated did not.** |
| **A sweep's exemptions are part of its result.** Write them into the constraint — *"0 outside nested `.git` metadata of vendored clones"* — so a future `0` can be falsified. | Otherwise every later round inherits an unfalsifiable number. |
| **When a lemma's natural generalisation is FALSE, print the counterexample and the reason the special case survives — that constrains the next proof more than more census would.** | *"Two more positive entries cost at most 1 of residue"* is false (`[1,1]+{3,1}`: 1→3) **and still false after the obvious repair** (`[5,2,2,1,1,1]+{5,1}`: 4→6). Both counterexamples have their maximum occurring once or twice, while the construction carries `λ₁+2` copies. **⟹ the head block is load-bearing: any proof that does not use it is proving something false.** |
| **Collapsing several rounds of apparatus into one lemma is a result, not tidying** — and it tells you which special cases were the same thing all along. | One descent lemma subsumed three earlier ones and explained *why* two families self-reproduce (an index becomes invariant at one parameter value), and it proved a tail case for arbitrary length where the earlier statement had covered length one. |
| **Reduce a conjecture to ONE open input and say so.** | An induction closed every branch but a single inequality: *"C1-M now has exactly one open input."* That is a strictly better position than a census, and it names the next round's target without ambiguity. |

## 39. The DC retroactive audit — what the banked rounds actually rested on

Every clean round this project banked predates RULING DC. Audited per family:

| rule | evidence |
|---|---|
| **Both banked milestones survive, and neither rested entirely on verdict grids — but in each, only ONE of the two families had demonstrated engagement.** Corrected label, carried wherever they are cited: **"two clean cross-family readings, one of which has demonstrated engagement."** | One line's family 2 **caught a real dropped qualifier in our own brief** (a heading asked for two formulas "For W1" while dropping the `L = 10` qualifier) and returned GAP on that joint while the mathematics came back clean — **route 1, unplanted.** The other line's family 2 **computed the first non-hand rows any judge had produced**, rows we had ourselves marked hand-underivable, **and we re-ran its code and reproduced its numbers** — route 3, verified. **Both family-1 readings found nothing and their nulls were never computed.** |
| **A void gate with an UNCOMPUTED null is route 2 in form and nothing in substance.** | Both unestablished families are that shape — and when a null on that project was finally computed, it came back at **1.0–1.6 bits.** |
| **An unplanted defect found by a judge is the cheapest engagement evidence there is.** Until a planted-defect brief exists, the best available proxy is: *did the judge find anything we did not already know?* | It costs nothing to collect and was the strongest single signal in the audit. |
| **The distinguishing test for "false text in the brief" is who caught it.** A rule against buying a clean round **on** false text does not fire when **the judge is the one who flags the false text** — that round evidences the judge working, not the judge being fooled. | Recorded at the time, and it is what let the route-1 evidence be recognised years — rounds — later. |
| **Certify the ROUTE at certification time, or bank the round as a correctness review carrying no engagement evidence.** | The framework was already half-present: one milestone cert had **already split** the reading obligation from the computational one and refused to let PROVED-S3 discharge the latter. |

# PART X — rules earned 2026-08-23 06:0x–07:3x (post-reboot; w61 r38/r39, w133 r32/r33, 677 r36)

## 40. NARRATED NUMBERS — the class reproduction cannot see
> **⚠️ CORRECTED IN PLACE 2026-08-23 07:5x.** This section originally called the `184`
> **fabricated**. It is not. It is the **positional-counter** violation count of that very
> sweep (`ok=5842 / VIOL=184`), while the sentence around it had moved to the **distinct**
> counter (`ok=635 / VIOL=97`). owner-w61 found this in r40 and I verified it by re-running
> both counters side by side (`problems/wowii/w61_r40_pop.out` [1]).
> **The number was measured and then orphaned — not invented.** The strike of the citation
> stands (the sentence was wrong); **the diagnosis does not.** See §46, which this bought.

| rule | the failure that bought it |
|---|---|
| **A printed number is not a measured number** — *of the population the sentence names.* A multi-digit literal inside a `print()` string that the program never computes is **narration**, and it survives every re-run, forever, byte-identically. **But narration is not automatically invention** (§46). | w61 r38 block [3] printed "the head-block-free family FAILS there (**184** distinct counterexamples)". `184` occurs **exactly once in the `.py` — inside that print string**. Three numbers, three populations: **184** positional-counter violations, **97** distinct-counter violations, **85** head-block-free violations. The sentence named the third and printed the first. |
| **RULING CD reproduction is STRUCTURALLY BLIND to this.** A byte-identical re-run certifies that an `.out` came from a `.py`. It says **nothing** about whether the numbers inside were measured or typed. Re-running harder never finds a narrated number. | The planner re-ran the script, got a byte-identical diff, and **certified the fabricated number on the strength of it** — in a section specifically praising the round for *computing* its null instead of assuming it. |
| **Stating a scope does not protect you from crossing it.** A declared limitation is worth only what the next paragraph does with it. | The same cert stated in §1 that the diff "does not establish that the `.py` implements the definitions its prose names", then in §6 banked a number falling squarely inside that exclusion. **Five sections apart, one document.** |
| **Build the detector, do not just record the lesson.** `tools/narrated_number_gate.py` — flags multi-digit literals inside print strings that the program never computes. Declared blind spots: a narrated number coinciding with a real program constant, **and (widened, §46) it cannot distinguish invented from stale**. Benign class: **correct cross-round citations** (it flagged w133 r32's `179`; traced to `w133_r31_a2path.out`, backed, measured twice). **A flag means "trace it", never "strike it".** | Written the same cycle, self-tested against the `184` that bought it, and immediately caught a second live instance on another line (677's coverage sentence, §41). |

## 41. POPULATION MISMATCH — the same defect one layer down, and no gate we own catches it

| rule | the failure that bought it |
|---|---|
| **Every count ships with its population**, exactly as every `0` ships with its exclusion list. A number that is genuinely measured, but placed under a sentence about a **different population**, is as wrong as a typed one — and it is **invisible to the narrated-number gate**, because it really was computed. | owner-w61 correctly struck the fabricated `184` and substituted `97`. But `97` is the count for *"(UP2) is false in general"* over **all** terminating lists, while the repaired sentence speaks of the **head-block-free** family. The round's own output settles it: `VIOLATIONS=97`, of which **12 contain a head block** → the backed number is **85**. |
| **A correction is a claim and inherits every obligation of the claim it replaces.** Verify the replacement as hard as you audited the original. | The substitution was made in the same round that found the original defect, by the agent that found it. Finding a defect does not confer accuracy on the fix. |

## 42. THE GREEN HARNESS — `FAILURES=0`, `EXIT=0`, and a false conclusion

| rule | the failure that bought it |
|---|---|
| **A harness that prints a false conclusion while reporting zero failures is the worst instrument state there is**, because every gate above it reads green and stops looking. | w133 r33's `endpath` search was broken and printed a **wrong negative** — "requirement NOT SETTLED" — with `FAILURES=0` and `EXIT=0`. Caught only by reading a number that was **impossible on its face**, and the fix **reversed the paragraph it supported**. |
| **Three instances, two lines, one cycle — this is a family, not bad luck**: the typed `184`; stale prose asserting an empty conjunction after the run had already found two instances; and this wrong negative. **All three print clean. None is visible to re-running.** | The common shape: **the narration and the computation drift apart, and only the narration is read.** |

## 43. VACUOUS TARGETS — check the hypothesis class is inhabited before dispatching at it

| rule | the failure that bought it |
|---|---|
| **When a priority list contains "can X exist at all?" ranked BELOW "prove something about X", the order is wrong and the planner inverts it before dispatch.** A guaranteed-deliverable clause does not rescue a vacuous target; it only guarantees the owner brings something back. | The planner sent w133 at (TAIL-2)-at-a-prescribed-`w`. Its hypothesis class on the tested family is **empty**: 414 residual instances, **0** with `l > 4`. The target was neither provable nor refutable there. |
| **The warning was already in the owner's own file, and the planner ratified the bad order anyway.** | r32's ledger said "`l > 4` is still entirely unspent — every residual instance found carries `l ≤ 2.5`", and r32's OWED NEXT listed *"can the residual carry `l > 4` at all?"* as **item 3**, below the item-1 target that depended on it. The planner's r33 book demoted it further, to "if budget survives". |

## 44. LEDGER DURABILITY — context is not storage

| rule | the failure that bought it |
|---|---|
| **Append the ledger as each block lands. Never hold a round's findings for one final write.** | The machine rebooted at 04:13. **w133 r32 survived complete** because it appended to its state file as it went. **w61 r38 and 677 r36 both completed real work in the same window and lost their ledgers entirely** — w61's computation survived only as an orphan `.out`, and 677's gate had *granted a dispatch licence* whose round left no record at all. |
| **A gap in a ledger with no reason beside it is indistinguishable later from a decision.** Record what was lost and why, not just what was done. | 677's registry would otherwise show a granted licence and no dispatch — reading, forever after, as a choice not to dispatch. |

## 45. COVERAGE RECORDS — a sweep that does not name its scope did not happen

| rule | the failure that bought it |
|---|---|
| **A sweep that does not enumerate what it swept is unauditable and, for ledger purposes, did not occur.** Coverage claims inherit the exclusion-list rule. | `results/field_sweep_batch1.md` claimed **"nine unscanned areas"**, listed **twelve** in its gap table, and **enumerated neither**. Its 12 area rows are therefore stuck at `PARTIAL?` in `orchestration/PROSPECTING.md` — work was done, but nobody can say where. |
| **Search coverage decided by our own spare capacity is coverage decided by the wrong thing.** Prospecting runs continuously, on a fixed round-robin, not when a solver slot frees. | The pool's raw material was entirely catalogued sources; six S0/S1 gates audited the *ranking inside a biased sample* while nobody questioned the sampling frame. The user caught it. Same defect as the intel-side miss: **YTD was never rejected — it was never seen.** |


## 46. F1 SPLITS — invented vs stale, and they need opposite responses

**Bought against the planner's own certification.** The planner ran the gate, saw "not computed by
this file", and certified that as **fabrication**. It was a real measurement under a counter the
round had abandoned. owner-w61 caught it one round later by running both counters side by side.

| rule | the failure that bought it |
|---|---|
| **F1a INVENTED** — no run ever produced it. → **Remove: the claim has no basis.** **F1b STALE / POPULATION DRIFT** — genuinely measured, on a population the sentence no longer describes. → **Re-state with the correct population: the measurement survives, the sentence does not.** | The `184` was F1b. Called F1a by the planner in a cert, in STATUS, in a report to the user, and in this doctrine file — **four carriers, one wrong word.** |
| **When a numeral fails a gate, the FIRST question is what it WAS measured on — not whether it was measured.** Every mechanical gate we own answers only *"is this computed by the file as it stands?"* and returns NO for both halves. **Three documents skipped that question**, the planner's included. | The distinguishing run cost one script and under a minute: sweep once, count both ways, print both. **It was never run before the accusation.** |
| **An accusation of fabrication against our own record is itself a claim, and carries the same provenance burden as any other.** Getting it wrong destroys a true measurement and slanders the record it was meant to protect. | The planner reported "a fabricated number" to the user before the distinguishing run existed. **Errors are correctable — but so is an over-hasty finding of fabrication, and it must be corrected just as loudly.** |
| **Population drift is its own species, with three instances on file**: the `184` vs `97` vs `85`; r39 publishing `ok=5842` as "reproducing r38 [5] exactly" when r38 [5] printed `635`; and a false denominator `5842+97−12` written **inside the paragraph naming that very class**. | All three mix a positional count with a distinct count. **Same sweep, two counters, and no line saying which.** |

## 47. A REFUSAL IS A DATUM — record it accurately, and never launder it

| rule | the failure that bought it |
|---|---|
| **The auto-mode permission classifier is INTERMITTENT.** **ONE identical retry of a refused call is legitimate**, to distinguish an intermittent classifier from a standing denial. **If it refuses a second time, that is FINAL**: do not rephrase it into a different tool, do not work around it, and **never route it through another agent or session** — a peer executing what was denied here launders the user's decision. **Record it as blocked and report it.** | 677 r37: `pbcopy`, `osascript` clipboard, navigation to the target host, and several `browser_batch` calls were **each refused once and succeeded on an immediate identical retry.** A round treating the first refusal as final would have held a dispatch that was actually available. |
| **A false "blocked" in a ledger is an unsourced claim about why something did not happen** — the same species as an unsourced number, and it is worse, because nobody re-checks a reason. | The ledger would have read "dispatch blocked" where the truth was "dispatch available, classifier flickered". |

## 48. THE DISPATCHED BYTES ARE THE LICENSED BYTES

| rule | the case that earned it |
|---|---|
| **A licence granted for one string of bytes is void for any other string of bytes** — including a friendly one-line preamble. Send the licensed payload and nothing else, and **measure that what you sent matches what was licensed.** | 677 r37 sent `brief + "\n" + paper = 51 928` chars, **exactly the gate's printed DISPATCHED size, no wrapper sentence added**, and verified head AND tail verbatim after paste. |
| **Dispose of a diff by POPULATION, not by size.** "Only one line differs" is not a finding; **"the differing line is not in the population that decides"** is. | The re-run gate differed from the stored output by one line — the repo-sweep file count (21190 vs 21181). The repository had grown; **the dispatched bytes had not.** |
| **Re-validate, never inherit, a licence across a gap** (a reboot, a day, a rebuild). | The reboot destroyed r36's dispatch while its licence survived on disk. r37 re-measured byte identity on both halves **and re-ran the gate in full** rather than trusting the stored `GRANTED`. |

## 49. REPORT THE EXIT CODE AS-IS — a traced flag is not a failure

| rule | the case that earned it |
|---|---|
| **"I claim a traced sweep, not a clean one."** When a gate exits non-zero and every flag has been traced to the run that produced it, **report the non-zero exit and the traces** — do not suppress it to present a clean sweep, and do not strike flags to make it green. **A gate whose output is curated stops being evidence.** | 677 r37's `narrated_number_gate` run: `R36_leakgate.py` clean, `R36_rekey.py` 2 flags **both traced and kept** (a verbatim quote of another file's format string; the r35 factor from a cert), **neither in an outward-facing governing sentence** — exit code 1 reported unchanged. |

# PART XI — rules earned 2026-08-23 07:0x–08:1x (the zero-fabrication audit)

## 50. NEVER HAND AN EXCLUSIVE RESOURCE BACK TO NOBODY

| rule | the failure that bought it |
|---|---|
| **A round that ends while its exclusive resource is still working must hand the watch to something that outlives it** — a Monitor, a successor round, an explicit planner handoff. **Handing it back to "nobody" locks the resource until a human notices.** | The cross-family driver ended its turn saying it would "wait for the background poller's completion notification" — **but the agent itself was the poller.** The codex TUI kept generating with the lease held and nothing watching. The planner found it by chance, armed a Monitor, and harvested a 33 KB note that would otherwise have sat unread behind a held lease. |
| **"I will wait" is not a plan if the waiter exits.** | The verification had already produced its findings when the driver stopped; only the harvest was missing. |
| **§50 AS ORIGINALLY WRITTEN WAS DEFECTIVE, and the planner is the one who wrote it.** The rule said "hand the watch to something that outlives you"; **two agents followed it exactly and both still needed the planner to take the watch**, because the thing they handed it to was a Monitor inside themselves. **Corrected rule: the handoff must be to the PARENT SESSION, and the parent must CONFIRM it holds the watch.** An unacknowledged handoff is not a handoff. | The second driver reported it had "armed a Monitor to poll every 15s", **having correctly absorbed §50**, then re-woke every few minutes to report "still generating" — ~146k tokens and 33 tool calls spent observing nothing, while the planner's own watch was already running. **A rule that is followed and still fails is a defect in the rule.** |
| **A Monitor armed INSIDE a subagent dies with that subagent.** The watch must be armed by a session that outlives the work — for us, the planner. **Second instance, same day**: the 677 cross-family driver ended its turn reporting it had "armed a Monitor to poll every 15s", having correctly absorbed the §50 rule — and then exited, taking the Monitor with it. **The rule was followed and the outcome was identical.** | The planner armed its own watch both times. **A correct-sounding handoff to a process that shares your lifetime is the same failure wearing the fix.** |

## 51. ⭐ SAME-FAMILY AUDIT DOES NOT SUBSTITUTE FOR CROSS-FAMILY — measured, not argued

| rule | the measurement that bought it |
|---|---|
| **A clean audit by an agent of the drafter's own family is weak evidence.** Two Claude auditors, working from an explicit protocol, over artifacts drafted by Claude, produced 1 already-known BLOCK on the WOWII-61 paper. **A single cross-family pass (GPT-5/Codex) on the same paper returned four defects none of them found**, including a false mathematical clause with an explicit 8-vertex counterexample and a marker system claiming more than its own ledger records. | The user made the cross-family verifier the CORE and the mechanical checks the safety net. **Within one hour the design paid for itself on the first paper it touched.** |
| **The sharpest instance is a positive claim that was wrong.** auditor-A reported: *"NO NARRATED NUMBERS FOUND. Every load-bearing numeral traced or re-derived."* **The paper said `340 graphs` in two places while its own printed histogram `{2:14, 3:200, 4:118}` sums to `332`** — and the named script prints 332. Planner re-ran it and confirmed. | **A same-family "I checked all of them" is exactly the claim that most needs a different family to test.** The auditor was diligent and honest; it was not *different* enough. |
| **Therefore: a same-family clean result is recorded as "no finding by same-family audit", never as "verified".** Every artifact still lacking a cross-family pass is UNVERIFIED, whatever our own auditors concluded. | After this audit only WOWII-61 has a cross-family pass. wowii133, 677, batch1, fernandes, a211417 do not — **their clean readings were downgraded accordingly.** |

## 52. WHAT THE AUDIT ACTUALLY FOUND — we do not invent, we over-claim

| rule | the distribution that bought it |
|---|---|
| **Across seven published papers and four PRs: F1a (invented numbers) = ZERO.** Every finding was **population drift** (a real measurement under a sentence describing a different population), **over-assertion** (wording beyond evidence status), **an unexecuted verification claim**, or **a citation error**. **The failure mode of this project is not fabrication of data — it is saying more than the evidence carries.** | Findings: a 40-char permalink SHA extended from a real 7-char prefix into a commit that never existed; "checked for all r ≤ 3200" where the script checks 6 values; "No `sorry` anywhere in the file" with one `sorry` present; `certified` markers whose ledger rows record one family, or no row at all; `340` for a measured `332`. |
| **Design the gate for the failure mode you actually have.** A fabrication detector tuned for invented data would have caught **none** of these. Every one is a claim-vs-evidence mismatch, which is why the responsible reader — not the regex — is the core. | The one mechanical tool that did fire (`narrated_number_gate`) flagged a number that turned out to be **real but stale**, and the planner mis-certified it as fabricated. |
| **A dead identifier is the most dangerous species, because it looks like provenance.** A permalink asserts "you can check this yourself"; a dead one asserts it falsely, and nobody clicks. | `fbc67063…` returned HTTP 422 "No commit found" — in an open PR to a Google DeepMind repository, under our name. |

## 53. A NEGATIVE ABOUT A CAPABILITY IS A CLAIM ABOUT YOUR SEARCH, NOT ABOUT THE WORLD

| rule | the failure that bought it |
|---|---|
| **Before writing "capability X does not exist", grep the repository for a prior round that used X.** A negative that contradicts our own records is a statement about the search. | prospector r2 wrote that this Gemini account has no Deep Research, and proposed the standing rule *"future rounds should not re-attempt it."* `RESOURCES.md` records **three completed Deep Research probes with URLs and full harvests from the previous day**, plus the exact entry path. **The planner withdrew the finding.** |
| **A submenu that has not been opened IS NOT IN THE DOM.** "Confirmed by full DOM search" proves the feature is not *currently rendered*; it cannot prove it does not *exist*. **The scope of that negative is "what was on screen" and it was reported as "what the account has."** | Deep Research lives at `+` → **"More tools"** → "Deep research" — a `menuitemcheckbox` visible only at the **second level**. r2 inspected the first level and reported absence. |
| **Three rounds, one mistake.** round-1 and round-2 also concluded "not exposed"; round-3 found it only after the user supplied the path. **A failure mode that recurs after being written down is a missing guard, not a slip** — the guard here is the grep above. | The cost of the false negative would have been the permanent loss of a free instrument the directive names by name. |
| **The correct half survives.** Deep Think (a reasoning toggle, not a research agent) was tried, hung 10+ min, produced nothing, and was abandoned **unread**; AI Mode was substituted and every source it reported was independently cross-checked before being written down. **That is exactly right, and it is why the round's candidates still stand** even though its headline finding was wrong. | Withdrawing a finding does not withdraw the round. |

## 54. OUR INSTRUMENTS NEED THEIR OWN LIVENESS CHECK — silence is not success

| rule | the failure that bought it |
|---|---|
| **A monitor that reports nothing is indistinguishable from a monitor that is broken.** Every watch must have a way to tell "nothing happened" from "I did not look". **Check the state it writes, not the absence of alarms.** | `tools/pub_watch.sh`'s Zenodo half contained a **`SyntaxError`** (a backslash inside an f-string expression). It failed on **every record, on every poll, since the day it was written.** We believed we were watching views and downloads on eight published papers. **We were watching nothing.** |
| **`2>/dev/null` plus `|| true` is how a broken instrument passes for a healthy one.** Swallowing stderr to keep a poller quiet also swallows the evidence that it never ran. **Suppress noise, never errors.** | The failure was invisible from outside: `check` received an empty value, returned early, wrote no state row, and printed nothing — **exactly what a healthy quiet watch looks like.** |
| **The cheapest liveness test is: does the instrument's own state file contain what it should?** Found in seconds, once looked at — by grepping for a key that should have existed and finding zero. | Discovered only incidentally, while adding a new DOI to the watch list. **It had been silently dead for days.** |
| **This is the same species the project audits publications for**, one level up: a claim ("we monitor our publications") with no artifact behind it. **Apply the gate to our own tooling, not only to our papers.** | The audit found F3 — unexecuted verification claims — in published text. This was an unexecuted *monitoring* claim in our own runbook. |

## 54b. THE RULE DID NOT PROTECT ITS OWN AUTHOR — apply it to the tool you are writing NOW

| rule | the failure that bought it |
|---|---|
| **A newly written instrument is the LEAST trustworthy one, not the most.** §54 was applied retroactively to an old script and **not** to the replacement written minutes later. **Audit the instrument you are shipping in this turn, before you ship it** — the freshest code has had the fewest chances to be caught. | Within the hour of writing §54 ("our instruments need their own liveness check; `2>/dev/null` + `|| true` is how a broken instrument passes for a healthy one"), the planner shipped `tools/engine_util.sh` containing **`find … -newermt "-6H" 2>/dev/null`**. On this system's `find` (bfs) that is an **"Invalid timestamp" error**, swallowed by the redirect, **returning `0` as if it were a count.** It reported `last6h=0 outputs` while the true figure was **7**. |
| **The tell was an internal contradiction in the instrument's own output, not an error message.** `idle=2min` and `last6h=0` cannot both be true. **Read your instrument's fields against each other** — a swallowed error leaves no trace except inconsistency. | Caught by noticing the two numbers disagreed, not by any failure signal. Had the two fields not been printed side by side, it would have gone on reporting zeros indefinitely. |
| **A number that is a swallowed error is worse than a missing number**, because it is indistinguishable from a real measurement — and here it was about to be read as "the engines are still idle", the precise question the tool existed to answer. | The corrected line uses `-mmin -360` and **deliberately does not suppress stderr.** |

## 55. A UTILIZATION FLOOR IS A GOODHART TRAP — and the planner walked into it

| rule | the failure that bought it |
|---|---|
| **Utilization is a DIAGNOSTIC, never a target.** When a free resource idles, **diagnose**: (1) dispatch gap — real work existed and nobody sent it → send *the work*; (2) prospecting gap — the pool is thin → fix the finding line; (3) verification bottleneck — Claude capacity consumed → **say so**, it is a prioritization question; (4) genuinely nothing valuable → **idle is correct**. **Never dispatch filler to move the number.** | The planner received "keep ≥8 jobs in flight", **implemented it without challenge** — a floor, a violation metric, a Monitor that shouted VIOLATION — and seeded a backlog partly to reach a count. The user corrected it: a floor *"turns a KPI into a goal and invites make-work."* |
| **A target that can only be met by breaking another rule was never a target; it was a defect.** | The floor of 8 was **arithmetically unreachable** under our own rate-limit rule (cap 4 concurrent per endpoint). Reaching it required opening the go-gateway lane — reserved as *failover for outages, not routine volume* — **purely to move a number.** |
| **The subordinate caught what the planner missed, twice, before the correction arrived.** The engine keeper (a) **refused to open the failover lane** to force in-flight to 8, citing the more specific directive, and (b) **dropped five 677 items** because the registry had drifted and a faithful brief could not be built — *"an unfaithful compression costs more than a blank."* | **Both refusals were quality judgements against a quantity instruction I had given.** A floor invites exactly the opposite behaviour; this one survived only because the executor ignored it. |
| **Zero output is a legitimate result.** Report it with its cause attached — *"idle 6h: cause = verification bottleneck"* — never as a score. | The corrected meter (`tools/engine_util.sh`) prints the diagnosis ladder instead of a violation. |

## 56. A NARRATED NUMBER IN OUR OWN INVENTORY — and a decision that leaned on it

| rule | the failure that bought it |
|---|---|
| **Apply the publication gate to our own ledgers, not only to our papers.** A count in a sourcing record is a factual claim and needs a backing list on disk. **"The sweep found N" and "the artifact records N" are different statements**, and only the second is quotable. | `field_sweep_batch1.md` asserted **"274 distinct named conjectures"** twice. It **records ~23**. `grep` finds the figure **cited** in three files (itself, `TARGETS.md`, `PROSPECTING.md`) and **listed** in none. The sweep may genuinely have returned 274; nothing on disk substantiates it. |
| **The damage from a bad number is the decisions built on it, not the number.** | The planner used 274 to measure the funnel, concluded *"sourcing is not the constraint — we have 274 untriaged"*, and **skipped a scheduled prospecting sweep on that basis.** True inventory: ~83. The skip survived re-examination on the corrected reason (38 triaged / 6 gated / 3 lines still puts the blockage mid-funnel) — **but the argument actually written down was false.** |
| **This is the project's own earlier rule, applied to its author**: *"a wrong reason matters because the next decision may lean on it."* Recorded that morning about a deferral; by afternoon the next decision leaning on a wrong reason was the planner's own. | Both the ledger and the skip are corrected in place, with the original reasoning left visible rather than quietly replaced. |
| **The subordinate caught it by refusing to pad.** Told to split 274 candidates into "several parallel briefs", the keeper found only ~23 on paper and **dispatched one brief instead of inventing entries to fill batches** — then flagged the gap as a sourcing-side defect. | **A quantity instruction met an honest inventory and the honest inventory won.** Third time today a subordinate's quality judgement corrected a planner's count. |

## 57. ON A TARGET WHERE A NEGATIVE WOULD CLOSE A LINE, DISPATCH TWO INDEPENDENT ANGLES

| rule | the case that earned it |
|---|---|
| **Redundancy on an attack front pays off not when the two attempts agree, but when they disagree DETECTABLY.** Two independent angles on the same target make a fabricated result visible without trusting either one. **Standing rule: any target where a negative result would close a line gets at least two independent dispatches.** | E13 and E14 attacked w133's r34-named obstruction. **E13: "open." E14: "false, here is family H_k."** Rebuilt by the reviewer: **E14 never computed distances to one vertex** (`b′0`), so `ecc(c0)=3` was really 5, `ecc(x)=6` really 8, `rad` 4 not 3, the centre set was the wrong vertices, and `w` was not radius-extremal at all. **E13's "open" stands.** |
| **A single dispatch of the wrong one would have closed a live target.** E14 arrived as a fluent, fully-worked refutation. Nothing inside it announced itself as broken. | **The output looks exactly like the good ones.** This is the publication-audit failure mode observed in the *attack* channel: arithmetic on a graph it never fully traversed. |
| **State the risk asymmetry when accepting a resolution.** Accepting "still open" is conservative — it keeps work on a target already believed open. **Had the verdicts been reversed, the planner owed a personal re-derivation before letting anything close.** Say which case you are in, so the acceptance is auditable. | Accepted without a third derivation, and the reason is written down rather than left implicit. |

## 58. TWO ENGINES CONVERGING ON THE SAME WRONG READING IS EVIDENCE ABOUT THE BRIEF

| rule | the case that earned it |
|---|---|
| **When independent engines agree on something the source contradicts, suspect the brief before the target.** Convergence is usually treated as confirmation; here it is a defect signal pointing back at the dispatcher. | E01 and E02 **both** concluded *"Shape S2 as literally stated is unsatisfiable."* The source's own census records **1,016 real S2 instances.** Both quoted the requirement of **three** copies of the new max, then built constructions producing **two**. |
| **Brief design is a scarce-resource task** under the first principle — it belongs to Claude, not the engines — **so a brief defect is the planner's defect.** No result derived from the mis-specified object may be quoted until the brief is fixed with a worked instance from the real census. | The planner wrote the S2 brief. Both engines executed it faithfully and both produced nothing usable, at the cost of two free calls and one reviewer pass. |


## 59. A COUNT IS NOT AN OVERRIDE — and "the brief was wrong" can itself be the wrong diagnosis

| rule | the failure that bought it |
|---|---|
| **When a measured count appears to contradict a derived claim, the first move is to check whether they are about the same object** — not to let the count win. A census counts instances of X; a derivation says X is never Y. **Both can be true, and they look contradictory only if you have silently equated X with Y.** | Two engines independently derived *"S2 is never a UP2 move."* The planner had a census of **1,016 S2 instances** and ruled the engines had misread. **The engines were right**: `Δ|·| = 1` and `ΔΣ = 2c+4 ≥ 6` against UP2's required `0` and `2` — unsatisfiable at every `c`, **0 of 1,016** are UP2 pairs, control fires **3,057 of 3,057** on S1. |
| **Diagnosing "the brief was defective" is itself a claim and can be half wrong.** Here the brief *was* defective — and the conclusion drawn from that, *"therefore their reading is wrong,"* was the actual error. **A correct diagnosis of one's own defect does not license dismissing what the defect surfaced.** | The planner wrote doctrine §58 off this episode. §58's core survives (convergence on a source-contradicting reading is a defect signal); **its example was mis-analysed and is amended.** |
| **Every invariant ships with the classifier that tested it.** *(owner-w61's rule, adopted.)* A statement worded more narrowly than the classifier that certified it is false outside that wording — and nothing in the run will say so. | `§7.54(2b)` stated C1-W more narrowly than its own certifying classifier: **51 of 709 pairs reach a state that is neither EQ nor UP2, where C1-W as worded is FALSE.** Found by re-reading, not by any run. |

## 60. A FAMILY CLAIMS THE SILENCE; A FINDING IS A POINTER

| rule | the case that earned it |
|---|---|
| **A FAMILY credit claims the whole verdict surface INCLUDING ITS SILENCE**, and the held-out harness is the only instrument licensing us to read that silence. **A VOID harness makes the silence unreadable ⟹ VOID gives no family, ever.** **A FINDING is a pointer, discharged by following it** — so findings survive a VOID round, but only via owner re-derivation, and **the credit belongs to the re-derivation.** *(owner-677's formulation, adopted verbatim; standing on all lines.)* | ETP-677 R39: verdict INVALID with two **real, novel, location-specific** S3 findings, but the pre-registered held-out table graded **VOID**. The owner banked **neither** the verdict nor any of its 18 §1a rows, 6 §1c verdicts, or §1b — **and re-derived both findings from scratch**, which is what made them ours. |
| **"FINDINGS STAND" ≠ "DEFECTS LIVE."** A finding is about a text **at a moment**; a defect is about the text **now**. **Any status claim about a document must name the version it describes.** | The planner wrote *"Six CRITICALs stand"* in a cert — **they had been repaired two rounds earlier.** The false premise propagated into **three** downstream artifacts and became the basis of an argument about judge engagement. Caught by the owner, verified by the planner **by content, because line-number citations had drifted in an append-heavy ledger**. |
| **An argument that survives the death of its original premise, rebuilt on better grounds, is stronger than one never tested.** | The planner's engagement argument rested on the (false) six live CRITICALs. The owner replaced it with one resting on the findings rather than the verdict: **an echo cannot manufacture two correct, novel, location-specific scope defects** — and demonstrated route 3 by pre-existence grep (0 artefacts). |
| **The strongest corroboration available is our own control disagreeing with our own text.** | §6.4: the paper's unrestricted sentence is contradicted by `TRIV=[[0]]`, a **positive control we ship ourselves** asserting E677 holds at order 1. Not an outside opinion — an internal contradiction we had already built the instrument to detect. |

## 61. AT TEMPERATURE 0, n=5 IS n=1 — check the sampler before you quote the power

| rule | the case that earned it |
|---|---|
| **Before quoting any n-fold agreement or power bound, verify the calls were actually independent.** A deterministic sampler turns `n` repetitions into **one** observation, and **the power bound becomes fiction while every surface reading looks normal.** | w133 r36's PP2A was to run n=5 per arm. The shared dispatchers (`engine_call.sh:20`, `engine_call_big.sh:40`) are **temperature 0**. The owner caught it, dispatched at temp 1.0 through a **new** script leaving the shared ones untouched, and **recorded the deviation before dispatch.** |
| **Deviating from the production configuration to make an experiment valid creates a transfer gap — state it, do not hide it.** | Production first-pass runs at temp 0. So the result reads *"the channel is capable of detecting an omitted hypothesis when sampled"*, **not** *"our production filter detects them."* The owner stated this itself; the caveat now ships with the number. |
| **A ceiling result is only worth something if the response was SPECIFIC.** Check that each plant moved only its own statistic — otherwise you have measured "complains more at a defective-looking text", not detection. | Both nulls refuted at 1.00, **and** arm B's tags were clean 5/5 while arm D's links were clean 5/5. **The undesigned specificity control is what makes the ceiling meaningful.** |

## 62. MEASURE YOUR FILTER BEFORE YOU MAKE IT LOAD-BEARING

| rule | the case that earned it |
|---|---|
| **A filter's capability profile is not uniform, and the profile determines what it may be used for.** Measured: **10/10 on planted hypothesis-LIST defects, 2/15 on an unplanted JUSTIFICATION defect in the same text** (12/15 endorsed it, 4 with an invalid stated reason). **Strong at comparison, weak at derivation.** | The planner made engine first-pass review load-bearing in PROTOCOL v4 §3 **that same morning**, on the argument that it was the only honest way to widen. **The measurement arrived hours later and bounded it** — completeness-against-a-list yes, validity-of-reasoning no. |
| **The weak axis is the one that had already bitten us.** | E14 passed a fluent, fully-worked, **entirely wrong** derivation through this project on the same day. **Now we have the number instead of the anecdote**, and validity of reasoning stays with Claude. |
| **An instrument that cannot be aimed at a question should say so and name the one that can.** | Asked whether PP2A's arms could also read a zero-finding cross-family pass, the owner said no — 4.8 KB vs 146 KB, wrong channel, wrong axis — and named PP3 as what would, **declining to start it "rather than manufacture a second uninterpretable result."** |

## 63. A NAMED DEFECT RECURS UNTIL A MACHINE ENFORCES IT

| rule | the failure that bought it |
|---|---|
| **Writing a lesson into the ledger does not stop it recurring. Convert every named defect into an executable check, or expect it back.** | w133 r37 reported four own-errors of which **three were re-commissions of defects this same line had already named and written down** — a pass-by-emptiness printer (r33's own named defect), a run that excluded its entire hypothesis class without printing the population, and a "guard" that forbade nothing. |
| **This is sharper than "a guard shaped to the last defect misses the next in its family" (§ w133 r35). These were not next-in-family — they were the same defects, recommitted by the line that named them.** | What caught (a) was **the owner's own pre-written assertion**, not the prose lesson. **The mechanical check worked where the written lesson did not.** |
| **THE THRESHOLD IS PART OF THE GUARD.** At a cap the host already meets, an over-permissive defect **returns a genuine witness first and is invisible.** A guard tested only where it fires cannot catch a defect that fires correctly for the wrong reason — hence a separate VALUE check is needed alongside the FIRES check. | Same round: the third "value" half sees late-block 33 of 38 that the firing half cannot. |

## 64. CHEAP TO CHECK ≠ POSSIBLE TO FIND — screen the production route, not just the certificate

| rule | the case that earned it |
|---|---|
| **Certificate size is necessary but not sufficient.** A target can have a one-object certificate checkable in `O(p⁴)` and still be unusable, because **the only way to FIND that object is a search we are forbidden to run.** Screen `prodroute ∈ {structured, normal-form, exhaustion-only}` at the sweep, where it is free. **`exhaustion-only` is a CUT however small the certificate.** | Gate batch 2 passed all six candidates on certificate size and **CUT two anyway on the production side.** Its own words: *"cheap check, exhaustion the only way to find a witness."* |
| **The project paid for this lesson twice in one hour, from two independent places.** | The only GO this pipeline ever produced had a cheap certificate and an `exhaustion-only` production route — **and that route survived a probe, a GO ruling, a charter, and an opened line** before being refuted on unrelated grounds. A free screen at the sweep would have flagged it on day one. |
| **A tight failure boundary is evidence against the whole family, not an invitation to search it.** When a strengthening fails at the parameter *immediately adjacent* to the proved case rather than far from it, hunting a "correct strengthening" in the same family is the most likely way to spend rounds and learn nothing. | The `≤3` weakening failed at `(2,3)`, one step from the paper's proved `(2,2)` — not at the distant `(3,3)`. The planner ruled the strengthening hunt **not** primary on exactly that datum. |

## 65. ABSENCE OF OUTPUT FROM A KILLED PROCESS IS NOT EVIDENCE

| rule | the failure that bought it |
|---|---|
| **A process you killed did not "produce no output" — you destroyed its output.** CPython block-buffers stdout when it is not a tty; a run emitting under 8 KiB never fills the buffer, and a kill discards everything unflushed. **Before concluding a script produces nothing, re-run it with `-u` or to completion.** | The planner ran a probe script twice, killed it both times, concluded it *"produced no output at all"*, and **wrote a ruling barring a citation on that basis.** The value was computed correctly at t≈3s on every run and sat unflushed for ~150s. |
| **The bar was right and the reason was wrong — and this project's own rule says the reason is what the next decision leans on.** | Provenance-or-silence correctly barred an unsourced citation; the stated ground for it (*"the script produces nothing"*) was an artifact of the planner's own invocation. |

## 66. A CAPPED RECORDER IS NOT A COUNT — and a witness that exists only in prose is not preserved

| rule | the failure that bought it |
|---|---|
| **A recorder with a cap reports the cap, not the population.** Read every reported count back to the code that produced it and check for an early exit, a `break`, or a fixed-size buffer. **This is the population-mismatch family (§41) with the mismatch hidden in the collector rather than the sentence.** | tdn round 1 reported *"counterexamples: 5"*. The recorder **capped at 5**. The true complete census: **900 normal-form / 22 500 de-normalised = 8.24%**, exclusion list empty. |
| **Exhibiting a witness is not preserving it.** A result demonstrated twice but whose scripts were not kept **survives only as prose** — which is the exact species this project audits published papers for. | The counterexample that refuted this project's **first GO** was preserved only as a table in prose. The owner caught it, called it *"I shipped the species we audit"*, and rebuilt four gated scripts. **The planner did not catch it.** |
| **Check a claim about your own past work against the code before shipping it — memory is not a source.** | The same round nearly wrote a defect into its own prior block: its draft claimed an earlier control sampled only the `p²` diagonal subgroup. It read the code first and found the claim **false** — the control had used the full `p⁴` action all along. |

## 67. HELD-OUT DISCIPLINE APPLIES TO JUDGE ROUNDS, NOT TO ATTACK ROUNDS

| rule | the distinction, and why it matters |
|---|---|
| **When we are MEASURING a reviewer** (does it engage, does it see what is not written), the defects must be held out — **a verifier handed the answer measures nothing.** | This is why every cross-family ticket forbids sharing our findings, and why PP2A plants defects rather than describing them. |
| **When we are ATTACKING a statement** (trying to break it), telling the attacker what is already known broken is **efficiency, not corruption** — it stops the engine rediscovering a known gap instead of hunting new ones. | An adversarial brief on C1-Z was given the S2 gap the line's own owner had found, **with instructions to independently verify that gap's logic AND hunt elsewhere.** Correct: the round's purpose was breaking a theorem, not scoring a judge. |
| **The test for which regime you are in: would a clean verdict from this round be used as evidence about the reader?** If yes, hold out. If the output is only used as mathematics, disclose freely. | Confusing the two costs either a wasted measurement or a wasted attack. |

## 68. A FIGURE HANDED DOWN IS STILL A FIGURE TO VERIFY

| rule | the case |
|---|---|
| **A number in a task book from the planner carries no more authority than one from anywhere else.** Recompute it before working from it — and report the composition, not just the total. | The planner briefed *"~71 prose citations with no resolvable identifier."* The keeper counted: **76 bibitems total, exactly 71 without arXiv/DOI — but ~45 of those are internal self-citations already existence-checked**, so the actionable external population is **~26**. **The figure was true and misleading as a work estimate.** |

## 69. A BACKLOG DECAYS AGAINST A MOVING FRONT — audit it before reading it as demand

| rule | the failure that bought it |
|---|---|
| **A backlog item is a claim that work is still wanted, and it expires.** When the front advances, items answered by later rounds stay on the list and **a row-counting diagnostic reads them as unmet demand.** **Audit the backlog against the current fronts before treating idleness as a dispatch gap.** | Twice in one day the planner's engine meter reported *"N real backlog items PENDING → dispatch gap"* when a third of the list had already been answered — once by rounds that closed the question, once by a round that **restructured the problem so the item's framing no longer applied**. |
| **Three decay modes, and they need different marks:** **STALE** (a later round answered it), **RESTATE** (the front moved so the item's framing is wrong, but the underlying need survives), **LOW** (no line is waiting on it). **Collapsing all three into "pending" is what makes the meter lie.** | `(TAIL-2′)` re-derivation went STALE when the owner discharged it; two w61 items needed RESTATE after r42 changed the odd half's structure; a capability probe was LOW from the day it was seeded. |
| **The meter counts rows, not live rows — and a meter that counts the wrong thing invites exactly the make-work the utilization correction forbade.** | Same shape as the Goodhart trap (§55), one layer down: the number was honest about the list and dishonest about the world. |

## §70 — A CHANNEL'S FAMILY IS A PROPERTY OF THE CHANNEL, NOT OF THE BRIEF THAT NAMES IT
**2026-08-23.** The tdn owner specified an *"adversarial **cross-family** brief"*; the keeper dispatched
it to **ox-alpha**; the attack came back clean and detailed. `RESOURCES.md` line 28 has said all along:
**ox-alpha's family identity is unknown — 不计入跨族多样性.**
**Nothing in the brief, the dispatch, or the returned document was wrong. The only wrong thing would
have been the ledger entry** — banking a cross-family pass that never happened, on the strength of the
words in the brief's title.

**RULE: family is read off the CHANNEL REGISTRY at bank time, never off the brief, the task name, or
the report's own header.** A brief cannot confer a family on the engine that runs it.
**Corollary:** when a line's verification state is asserted, the assertion names the channel, and the
channel is looked up. "Cross-family verified" is a claim about *who ran it*, and it is checkable — so
check it, in the registry, every time.

**§70b — the same episode, second lesson: a clean adversarial result is worth exactly what the
channel's MEASURED profile says it is worth.** E42's verdict was *"chain holds"* — a judgement about
whether a derivation is valid, the axis on which this class of judge measured **2/15** (vs 10/10 on
list-completeness, `cert_w133_r36.md` §3). But E42 also **reconstructed `K_k`, `δ_{n₀}`, `φ_k` from
scratch** and its reconstruction matched the claim.
**Separate the two: the CONSTRUCTIONS are evidence (they are checkable and it produced what we did not
give it); the VERDICT is nearly worthless (it is the thing this channel is worst at).**
**Read an engine for what it BUILT, not for what it CONCLUDED** — a distinction available only because
the channel was measured before it was trusted (§62).

## §71 — THE PRODROUTE SCREEN HAD THREE VALUES AND REALITY PRODUCED A FOURTH
**2026-08-23, found by prospector r5 (math.KT + math.MG), not by me.** I defined
`prodroute ∈ {structured, normal-form, exhaustion-only}` as a free sweep-stage screen. Two candidates
(`1305.4549`, `2203.11062`) draw their refutation witness from **a small, already-classified finite
set** — ~100 fake projective spaces; the Grünbaum-classified simplicial arrangements. That is
**neither** `structured` (no construction gives the witness) **nor** `exhaustion-only` (the
enumeration is already done, published, and finite — the cost is a lookup, not a search).

**The prospector did the right thing: it recorded the shape as its own category and left the ruling to
the gate, instead of forcing it into the nearest existing bucket.** Forcing it would have been
invisible — an `exhaustion-only` tag on these two would have looked exactly like a correct tag and
would have cut two live candidates.

**RULE: a screen's value set is a hypothesis about the world, and a sweep is the experiment. When an
item does not fit, the honest move is a NEW CATEGORY plus an escalation — never the nearest bucket.**
Adopted as `prodroute = classified-finite`: **treat as a pursuit-positive**, because the witness
search is bounded by an existing published classification and the work is verification, not search.
**This is the second time in two days that a screen I designed was corrected by the line running it**
(§59: "a count is not an override"). **I am the wrong person to be the last word on a screen's
adequacy; the sweep is.**

## §72 — A STATUS FIELD WRITTEN AT DISPATCH AND NEVER CLEARED IS A LEDGER THAT LIES TOWARD "BUSY"
**2026-08-23.** The engine meter reported **in-flight = 0**; `ENGINE_BACKLOG.md` showed **23 rows
INFLIGHT**. The meter was right. `INFLIGHT` is written when a job is dispatched and **nothing ever
clears it on completion**, so the table cannot answer the one question it exists to answer.

**It fails in the flattering direction.** A stale `INFLIGHT` reads as "work in progress" when the work
is finished and waiting — the pipeline looks saturated precisely when output is stranded.

**And the real finding was invisible from the table.** Checking by *repo reference* instead of by
status found four w61 outputs unused: `E04` with **zero references — never even first-passed, seven
hours old** — and `E06`/`E33`/`E38` appearing **only inside first-pass certs**. That last shape has its
own name now: **passed the filter, never adjudicated.** First-pass is a filter, not a banking event
(v4 §3), so an item can clear it and stop forever, and nothing in the ledger shows that.

**RULE: a status field must be written by the EVENT IT CLAIMS, not by the event that starts it.**
`LANDED` on output arrival; `BANKED`/`STRUCK` on adjudication; `INFLIGHT` is never evidence that
anything is running — check the sandbox for the file.
**Corollary, and the general one: audit a ledger against the WORLD (does the output file exist, does
anything reference it), never against its own status column.** I had already diagnosed today's idle as
a dispatch gap and dispatched owners to write *more* briefs; the harvest-side gap was sitting
underneath it, and only the cross-check surfaced it.

## §73 — I DISPATCHED A DUPLICATE ROUND BY TAKING THE TARGET FROM A REPORT INSTEAD OF THE LEDGER
**2026-08-23, ~15:5x (dispatch), corrected 16:0x.** Prospector r5 reported *"next up: math.NA + math.OC"* — true **at 15:36, when
it wrote it**. By 15:54 those two areas were swept and written up (`field_sweep_r6.md`). At ~16:1x I
dispatched a fresh r6 **on NA+OC**, using the target named in the report. `tools/prospect_due.sh` would
have said **"15/31 swept, next up: math.QA math.RA"** — and my own task book for that agent instructed
*the agent* to run it. **I told the agent to check the live state and did not check it myself.**

**No scheduler bug, no lock needed: an agent report is a snapshot of the world at the moment it was
written, and I treated it as the current state of the world.**
Within the same hour I got the identical shape *right* on the Zenodo directive — an instruction built
on a stale state, where I checked the live record instead of executing the instruction. **Same failure
mode, opposite outcomes, one hour apart. The difference was purely whether I looked.**

**RULE: the target of a dispatch is read from the LIVE LEDGER at dispatch time, never from the report
that proposed it.** Where a `*_due`-style script exists, the dispatcher runs it — not only the agent.
**Corollary: an agent that completes more than its assigned round must say so in its report.** r5
appears to have continued into r6 and reported only r5; that is a reporting gap on its side, but it
could not have caused a duplicate if I had read the ledger.

**What the duplicate actually bought (recorded so the cost is stated honestly, not rounded to zero):**
an **unplanned independent replication** of a full prospecting round. The second instance's candidate
set converged with the first; it **independently re-verified an exclusion** (`1202.4043` "nice cones =
facially exposed" — refuted 2013, Roshchina `arXiv:1301.1000`, 4-dimensional counterexample) and in
doing so **caught an error in its own draft**, which had kept that item as a live candidate. Cost:
about one round of tokens. **We do not otherwise get replication of a sweep for free — but this is an
argument for occasionally BUYING one deliberately, not for tolerating accidental ones.**

## §74 — A NEW SCREEN CATEGORY PASSES ITS REAL TEST WHEN IT IS DECLINED, NOT WHEN IT IS USED
**2026-08-23, prospector r6.** `classified-finite` was adopted from r5 one round earlier (§71). Its
first plausible-looking candidate was **Laderman's 3×3 matrix-multiplication problem** (`1108.2830`):
famous, tiny certificate — exactly the profile the new bucket was invented for. **The sweep declined
to apply it**, on the correct ground that Laderman's production route is **live SAT/SMT search, not a
lookup against a published classification.**

**That is the failure mode every new category has: it becomes a dumping ground on its first outing,
because a fresh bucket is the most attractive place to put anything awkward.** This one didn't.
**A category is only worth its keep once it has been REFUSED to something that superficially fit** —
until then, we have not observed it discriminating, only observed it accepting.
Laderman instead reproduces the gate's founding diagnosis intact: **prominence does not buy a route**;
tiny certificate + exhaustion-only production = CUT-shaped, however famous.

## §75 — A STRUCTURAL FAMILY FINDING DOES NOT LICENSE SKIPPING THE PER-MEMBER CHECK
**Same round, and it earned its keep immediately.** r6 flagged **PEP/SDP-verifiable conjectures** as a
recurring structural shape — a family. Inside that very family sat `2407.11739`, a strengthened
Drori–Teboulle stepsize conjecture **already proved in May 2026**. It was caught **only because every
member got its own resolution check despite the family-level finding.**

**The temptation a family finding creates is precisely to treat membership as a verdict** — the family
looked live, so its members look live. **This is the FAMILY vs FINDING rule arriving from the opposite
direction:** there we ruled a family claims the whole verdict surface *including its silence*, so a
VOID never yields a family; here, a live family never yields a live member.
**RULE: family-level structure is a routing hypothesis, never a per-item verdict. Every member is
checked for prior resolution on its own.**

## §76 — CORRECTION TO §73: WHAT THE DUPLICATE BOUGHT WAS WEAKER THAN I CALLED IT
I recorded the duplicated NA+OC round as *"an unplanned independent replication."* **Too strong.** The
instance that produced r6 was a **fork of the planner — it inherited my full context and framing**; the
second instance worked from a task book I wrote. **Two agents descending from the same context and the
same brief converging on the same candidate set is weak evidence of correctness, not strong** — it is
much closer to same-family agreement (§51) than to replication.
**What survives the correction:** the *fact-checks* the second instance ran are independent of shared
context, because they queried the world — the 2013 Roshchina refutation via search, PR #3675 via
`gh pr view`. **Checks against external reality keep their force under shared priors; agreement between
the checkers does not.** State which kind you have before pricing it.

## §77 — RULING: A MECHANISM MAY STEER SOURCING; A YIELD NUMBER MAY NOT STEER COVERAGE
**⚠️ SUPERSEDED IN ITS PREDICTION by §88. The ruling below (numbers vs mechanisms) stands unchanged;
the specific hypothesis it registered was wrong in its variable and is corrected there.**
**Standing ruling:** per-area yield is recorded as information only and **never fed back into
scheduling** — otherwise the sweep chases its own metric and whole areas stay unswept forever.
**r6 raises the first real tension with it.** OC's abstract harvest passed the certificate-size screen
at roughly **twice** KT/MG's rate (18/90 vs ~1-in-10) — but it came **with a mechanism, not just a
count**: *optimization's own verification apparatus (SDP/PEP, SOS) is itself a finite structured
certificate*, so the field natively produces the shape our gate is looking for.

**Ruling — the two are different objects and the prohibition does not reach the second:**
- **A yield NUMBER may never change COVERAGE ORDER.** Round-robin over the 31 areas stands. An area is
  not visited sooner or later because it scored well. This is the Goodhart guard and it is unchanged.
- **A MECHANISM may change SOURCING WITHIN an area** — which source classes to work, which queries to
  run, what shape to expect. That is not chasing a metric; it is a **testable hypothesis about where
  gate-passable conjectures come from**, and it makes a prediction we can be wrong about: *fields whose
  native proof technology emits finite structured certificates should over-produce gate-passable
  candidates.* Record it as a prediction and let later areas falsify it.

**The distinction to hold:** a count tells you where you *did* well and invites you to go back there;
a mechanism tells you *why*, and is checkable against the next area whether or not you go back.
**Never let a mechanism smuggle a schedule change in behind it.**

## §78 — I WROTE EIGHT TIMESTAMPS THIS CYCLE WITHOUT ONCE RUNNING `date`
**2026-08-23 16:03, caught by a heartbeat event, not by me.** Across this cycle I stamped
`STATUS.md`, `watch_ledger.md` (×2), `ENGINE_BACKLOG.md`, `verification_doctrine.md`, the dashboard,
a cert and three task books with times I **estimated from the felt pace of my own work**. The drift
ran forward and reached **~50 minutes into the future** (`16:5x` written at `15:56`). Two ledger
entries and one published page claimed times that had not happened yet.

**Nothing about this was hard. `date` costs one call and I made none.** The estimates felt safe
precisely because a timestamp seems like bookkeeping rather than a finding — **but a timestamp IS a
number in a provenance field**, and the whole zero-fabrication gate exists to stop numbers that were
not read off an instrument. **I ran that gate on other people's work all day while free-handing my own
clock.**

**Aggravating, not mitigating: `watch_ledger.md` is an ORDERING document.** Its entries are how we
reconstruct what happened before what, and future stamps corrupt exactly that. The correction used
each file's real `mtime`, which is the instrument I should have read in the first place.

**RULE: never write a wall-clock time you did not just read. `date` before any stamp — and when
correcting one after the fact, take it from the artifact's `mtime`, not from memory of when you
"probably" did it.**
**F1a vs F1b applies to me (§46): these were not invented numbers, they were STALE-POPULATION ones —
a real clock, read once, then extrapolated. That is the species that feels most like knowing.**

## §79 — §3b NAMES WHO WRITES A BRIEF AND SAYS NOTHING ABOUT WHEN ITS CONTENT WAS TRUE
**2026-08-23, third recurrence on the w61 line, first since §3b was written.** E33 returned "BROKEN";
its headline was **a correct identification of a defect in the brief** (it wrote `f(T)=R(L(T))` as
`R(T)`, and called a partition a "terminating list"). Verified timings: **`w61_r42.md` landed 12:30;
the brief was written 13:33 — one hour later — with no reference to r42, S2-STEP or S2-RED anywhere in
it.** Its second, correct point had **already been answered by r42**; the brief withheld an answer the
line already held.

**§3b is necessary and insufficient.** It fixes authorship. A brief can be authored by the right person
and still describe the line as it stood before the last round — and **a stale brief fails in the most
expensive way available**: the engine attacks the gap, reports a break, and the break reads as
mathematics rather than as a defect in what we sent.

**RULE: a brief names the owner round it was built from, and that number is checked against the line's
latest round AT DISPATCH TIME. If the line has moved, the brief goes back to the owner.**

**§79b — this is §73 wearing different clothes, and they should be read as one rule.**
There: I dispatched a duplicate sweep because I read the target from an agent's report instead of the
live ledger. Here: a brief was dispatched carrying line state that a later round had superseded.
**Both are "dispatch built on a snapshot of a moving state."** Both cost a full unit of engine work.
**The general rule: EVERY DISPATCH READS THE LIVE STATE AT THE MOMENT OF DISPATCH — the ledger for
targets, the owner's latest round for content. A snapshot is only ever evidence about the past.**

## §80 — AN ENGINE THAT STOPS HONESTLY CAN BE WORTH MORE THAN ONE THAT FINISHES
**E04 returned an explicit *incomplete*** and handed back the exact point it was stuck at. That point —
Kleitman–Wang must subtract the **largest `d`** entries or graphicality is not preserved
(`(2,2,1,1)→(2,0,0)` aborts) — **was the live defect in the owner's own draft of a different brief.**
The output that "failed" repaired work elsewhere on the line; three "successful" outputs from the same
batch were struck or downgraded.
**Corollary for brief design: asking for an honest stuck-point must be as safe as asking for an answer.**
The tdn brief already carried *"I could not break it, and here is where I got stuck is a valued, useful
answer, not a failure"* — **that clause earned its keep on a different line.** Keep it in every brief.

## §81 — "NO NUMBER BEFORE ITS RUN" EXTENDS TO ASSERTIONS IN BRIEFS, AND THAT IS WHERE IT BITES HARDEST
**2026-08-23, owner-w133 r40, self-caught.** It wrote into brief E44 the sentence *"condition 3 fails
everywhere there"* **before running the check. It holds at 178 vertices.** Caught before dispatch by
applying the no-number-before-its-run rule **to prose rather than to a numeral**.

Hard constraint 4 was written about **numbers in results**. **A false premise in a brief is worse than a
false number in a result**, for a reason §79 already established: the result is read by us and checked;
the brief is read by an engine, which **attacks the gap the false premise creates and returns a "break"
that reads as mathematics.** The cost is a full engine round plus the adjudication to unwind it.
**RULE: every load-bearing assertion in a brief — not only its numerals — is either run, cited to a run,
or written as an open question. "We believe X fails there" is a question, and must be phrased as one.**

## §82 — "EMPTY" AND "WE FOUND NOTHING" ARE DIFFERENT CLAIMS AND NEED DIFFERENT INSTRUMENTS
Same round, the best-built object in it. The claim *"on route A2's class the row is empty"* was
supported not by absence of hits but by **showing the machinery FIRES there and closes**: condition 3
fires **178 times** in that class, every one at offset **+5/+6/+7**, where (TAIL-1) closes
unconditionally; offset 0 is impossible by a one-line proof. **Then a control built to break it — 24
new in-class hosts of four shapes, 383 further firings — failed to break it.**
**A search that returns nothing is evidence about the search. A population that demonstrably fires and
is demonstrably closed is evidence about the world.** Whenever a line reports emptiness, ask which one
it has. **This is FAMILY vs FINDING again (a family claims the verdict surface INCLUDING its silence) —
the instrument that licenses reading silence is exactly this one.**

## §83 — A MEASUREMENT THAT LATER PREDICTS PRODUCTION BEHAVIOUR IS WORTH FAR MORE THAN ITS ORIGINAL RUN
The PP2A probe measured **10/10 on completeness-against-a-list, 2/15 on validity-of-justification**, and
I hedged it as *"a capability estimate under sampling, not a measurement of the production filter"*
(v4 §3). **r39/r40 then reproduced the split on live output nobody designed as a test**: every engine
**construction** checked out once rebuilt; every engine **derivation that mattered** did not — a false
lemma whose proof inverts an inequality, three false derived lemmas, a proof calling a C5 a C4, against
counterexample families that were sound once a missing edge was repaired.
**A planted probe tells you what a channel did on your probe. A prediction that holds on unplanned
production output tells you what the channel IS.** Upgrade the PP2A finding accordingly: it is no longer
an estimate, and v4 §3's engines-filter-but-never-adjudicate rule now rests on replication.

## §84 — A LEDGER ENTRY MUST NAME ITS AUTHOR AND ITS SOURCE SEPARATELY
**2026-08-23.** I appended a section to `PROSPECTING.md` signed *"（r7 侧发现，planner 裁定）"*. The
finding genuinely came from r7's side — from a **sub-fork r7 had dispatched, which reported to the
planner and never reported back to r7**, then became unresumable. So when r7 came to write its own
round, it found a section in its own ledger attributed to "the r7 side" describing work it knew it had
not done. **It correctly refused to touch it and preserved it — and drew the wrong conclusion, that
another lineage had written it. It was its own fork.**

**Two separate defects, and only the second is interesting:**
1. The signature named a *side*, not an *author*. **Author and source are different fields and must be
   written separately**: who wrote this entry, and where the content came from.
2. **A sub-agent reported UP to the dispatcher's dispatcher and never to its own dispatcher.** The
   parent then cannot account for its own child's findings. **When a report skips a level, the level it
   skipped is left holding a gap it cannot even see** — r7 could only detect this as a mysterious
   ledger entry.
**RULE: a finding travels to the agent that dispatched the finder FIRST, then upward. When a planner
receives something from a grandchild agent, it tells the parent — the parent's ledger is the one that
has to be right.**

## §85 — I WROTE A FABRICATED FACT INTO A LEDGER WITH A CARELESS REGEX
**2026-08-23 16:2x.** Marking two engine outputs as LANDED, I used
`re.compile(r"(\| E05 \| w61 \|.*?)(\|\s*\n)", re.S)`. **`.*?` under `re.S` crosses newlines**, so in a
line-oriented table it ran past E05's row and matched to the end of a row five rows later.
**Result: E11 — an item that had NOT landed — was stamped `LANDED 08-23 16:22 · 17376 bytes`, carrying
E10's timestamp and E10's byte count.**

**That is a fabricated fact in a ledger, authored by me, on the same day I built a gate whose entire
purpose is to stop numbers that were not read off an instrument.** The numbers were real — they were
read off a real file — **they were attached to the wrong object**, which is species F1b (stale/misplaced
population, §46): the most convincing kind, because every component is genuine.

**It was caught only because I verified my own edit rather than trusting that it had worked** — the
`grep` came back showing the marker on E11 instead of E05. **Had I skipped the check, w133's owner
would later have gone looking for an E11 output that does not exist, and the ledger would have looked
healthy.**

**RULES:**
1. **Never edit a line-oriented ledger with a multi-line regex.** Iterate lines; match with
   `line.startswith(...)`; edit in place. Row-structured data gets row-scoped edits.
2. **Verify every programmatic ledger edit by reading back the rows you intended to change AND
   confirming no others changed.** "rows edited: 2" is not evidence that they were the right two.
3. The general form, and the one I keep relearning today: **an edit is a claim about a file, and
   claims get checked.** I have spent this whole cycle telling other agents to audit ledgers against
   the world; the same standard applies to my own writes, which are the ones I am least likely to doubt.

## §86 — THE SAME CHANNEL, THE SAME DAY: ONE STRONG RECONSTRUCTION AND ONE FALSE ASSERTION
**2026-08-23.** The Gemini seat produced our **cross-family CHAIN HOLDS** on the tdn §17 chain — with a
reconstruction of `K_k`, `δ_{n₀}`, `φ_k` that **converged with an independent reconstruction from a
different channel** on a formula appearing in neither brief. Hours later, the same seat asserted that
our one-fibre statement was **"already a conditional proof within" the source paper itself**.
**That assertion is false**, and the primary source refutes it by quotation: the paper's lemma requires
*two linearly independent* directions, and its theorem, on reaching our exact branch, says *"It remains
to consider the case where `S` contains no two independent directions"* and proves only `3p²−p−1` —
weaker than our `(2p−1)²` by `(p−1)(p−2)`. **The paper reaches this case and proves something strictly
weaker.** The failure is a conflation of *"the paper handles this case"* with *"the paper proves this."*

**This is the cleanest available demonstration of §70b, and it arrived by accident:** one channel, one
day, **a construction that survived checking and an assertion that did not.** Neither result impeaches
the other, because they are different kinds of output.
**RULE (restated so it cannot be read as being about *models*): the unit of trust is not the channel and
not the session — it is the KIND OF OUTPUT. A construction carries its own check inside it; an assertion
carries none. Ask of every engine result: is this a thing I can rebuild, or a thing I must believe?**
**Corollary: a channel earning trust on constructions earns NO transfer of that trust to its assertions,
even in the same conversation.**

## §87 — DO NOT LOWER A BAR YOU MADE BINDING BECAUSE THE RESULT CAME BACK FAVOURABLE
The tdn novelty condition was *"all three routes are required before the word 'new' appears outward."*
Routes 1 and 3 came back clean, with positive controls and a full exclusion list. **Route 2 — reading
Sands–Szabó's book — was never reached**, and the driver correctly reported it as a gap rather than
folding it into the negative.
**The temptation is precise and worth naming: two clean routes plus a low-risk third feels like a
discharge, and the only thing standing between us and a favourable ruling is a bar we set ourselves.**
**Ruling: the condition stands.** What remains is narrowed and stated exactly — does that book bound
`|T−T|` under a fibre-size hypothesis in a **non-cyclic** group (its zbMATH review says it is mainly
about cyclic groups; ours is `(Z/p²Z)²`) — but narrowed is not discharged.
**A bar that bends when the evidence is favourable was never a bar; it was a formality.**

## §87b — A WATCHER'S BASELINE IS A BLIND SPOT, AND IT IS WIDEST EXACTLY WHEN YOU START IT
The landing monitor snapshots the directory at startup and reports only what appears *after*. **E03
landed in the gap between my last manual check and the monitor's baseline — so it was born into `seen`
and never announced.** I found it only by listing the directory by hand.
**Every watcher has this gap, and it is not a bug — it is what "watch for changes" means.** The danger
is that a running monitor *feels* like full coverage of its target, so the pre-existing set stops being
checked at all.
**RULE: when arming a watcher, RECONCILE ITS BASELINE ONCE by hand — the set it was born holding is
precisely the set it will never tell you about.** Same shape as §54b (a newly written instrument is the
least trustworthy one) and as today's other silences: **absence of an alert is not evidence of absence.**

## §88 — MY §77 PREDICTION WAS WRONG IN ITS VARIABLE, AND ASKING FOR EXCEPTIONS IS WHAT FOUND IT
**2026-08-23, prospector r8 (math.SP + math.ST).** I registered in §77 a falsifiable prediction:
*fields whose native proof technology emits finite structured certificates should over-produce
gate-passable candidates.* It was confirmed twice (OC ~28%, RA ~28.9% against a ~6–10% baseline).
**I then asked for exceptions rather than a third confirmation — and got a correction instead.**

r8 measured the largest gap this project has seen: **SP ~21% vs ST ~6%, a factor of 3.5 in one round.**
Both are mature fields with systematic apparatus, so **my variable does not separate them.** The
separating variable is not the field's TOOLS but **the SHAPE OF ITS CONJECTURES**:
- **SP**'s conjectures are mostly about a **concrete finite/discrete object** (a graph, a region, an
  ideal) — *even when the tools used on them are continuous.*
- **ST**'s are about **limiting behaviour as n→∞** (statistical–computational gaps, minimax rates).
  **However systematic the tooling, such a statement has no single finite counterexample to find.**

**Corrected prediction (replaces §77's): gate-passable candidates come from conjectures whose FALSITY
would be witnessed by a single finite object. The field's verification apparatus is a downstream
correlate — it tends to exist where the objects are finite — not the cause.**
This also explains the earlier confirmations better than my version did: OC and RA over-produced because
their open questions are about concrete finite objects, not because SDP or Gröbner bases exist.

**The methodological point is the one I want to keep:** a third confirmation would have been worth
nothing. **I asked for the exception, and the exception rewrote the hypothesis.**
**RULE: once a registered prediction has been confirmed twice, stop counting confirmations and
commission a search for exceptions — and require them to be listed FIRST, before any confirmations, so
they cannot be diluted by the count.** A prediction that has never been hunted for exceptions is
indistinguishable from one that has never been tested (§62).

## §89 — ZENODO'S PER-VERSION STATS ARE CONCEPT-LEVEL AGGREGATES, AND THAT BREAKS THE ONE CLAIM WE'D WANT
**2026-08-23 16:4x.** pub-watch fired four separate alerts — records `21995800`, `22054879`, `22069570`,
`22070405` — each reporting the *identical* jump `4v/1d → 8v/1d`. Identical numbers across four records
is the classic signature of an instrument reporting one object's stats for all of them, so I checked.
**Not a bug: all four share `conceptrecid 21995799` — they are four VERSIONS of the 677 paper, and
Zenodo serves the CONCEPT's aggregate stats on every version record.**

**Two consequences, and the second is the one that matters:**
1. **pub-watch emits N alerts for one event.** Noise, and it inflates the felt rate of outside interest
   fourfold. Group by `conceptrecid` and report once per concept.
2. ⚠️ **We CANNOT measure whether the corrected version is the one being read.** "`22070405` has 8
   views" does **not** mean eight people saw the corrected v10 — it is the concept total across every
   version since first publication, **including the uncorrected ones we spent today replacing.**
   **The single most natural thing to want to say after publishing a correction — "the fixed version is
   what people are getting now" — is exactly the thing this number cannot support.**

**RULE: before quoting any platform metric as evidence, establish WHAT OBJECT it is attached to.** A
number displayed on a version's page is not necessarily a number *about* that version. **And note the
direction of the error: it flatters. It makes a correction look better-read than we can possibly know.**
Downloads on this concept are **1**, unchanged across every version — so the honest statement about the
677 corrections is that **nobody has demonstrably downloaded any version, corrected or not.**

## §90 — A LIVENESS NUMBER MUST BE ABOUT THE CONTENTFUL REGIME, NOT ABOUT THE POPULATION
**2026-08-23, my error, caught by owner-w133 r41.** I certified a **1297/1297** census as strong partly
because it **"printed liveness"** — only 56.2% of vertices are peripheral, so the predicate looked
non-vacuous. r41 then proved two lemmas ((PER-A) `diam=rad+1 ⟹ peripheral`, (PER-B) `ecc=2·rad ⟹
peripheral`) and re-measured: **414 forced by A + 883 forced by B = 1297, with ZERO instances in the
only regime where the claim has content.** **Every pass was forced by something we can prove outright.**
And **(RXM-PERI) itself is false** — 961 violations across 317 in-class hosts.

**The count was real. The liveness statistic was real. Neither was ABOUT the thing under test.**
I checked that a liveness number existed and did not check what population it described. **A census is
only evidence over the sub-population where the claim could have failed** — everywhere else it is
re-measuring a lemma.

**RULE: a liveness check must report how many instances lie in the REGIME WHERE THE CLAIM COULD FAIL —
not how common the predicate is at large. Before banking any n/n census, ask: "which of these n could
have come out the other way?" If the answer is none, the census is a tautology with a big number on it.**
**Corollary (§62 sharpened): testing a screen before making it load-bearing means testing it WHERE IT
BITES.** A number this large is exactly what makes the question feel already answered.

## §91 — A RIGHT ANSWER CAN ARRIVE WITH AN UNUSABLE WORKING: GRADE THE OBJECT, NOT THE VERDICT
Same round, from E45. Its **verdict was correct**; its **certificate was invalid** — the 7-vertex
witness, rebuilt, has `w` **failing the hypothesis**, its adjacency table is **asymmetric** (c lists b,
b omits c), and it asserts `ecc(u)=4` where the object measures 3. By (PER-A) a `diam=rad+1` graph
**cannot be a counterexample at all**, so the witness was never capable of doing the job.
Our matrix previously read: **constructions survive rebuilding, derivations do not** (§83). This adds a
third cell: **"correct" and "usable" are independent properties of an engine result.**
**RULE: never accept a verdict on the strength of its certificate without rebuilding the certificate.
Grading the verdict and rebuilding the object are different tests, and only the second can fail
informatively.** Owner-w133's phrasing is the one to keep: *"grading the verdict passes it, rebuilding
the object fails it."*

## §92 — MY LANDING MONITOR WATCHES ONLY THE HAPPY PATH, SO A FAILURE IS INDISTINGUISHABLE FROM SLOWNESS
**2026-08-23 17:1x.** I armed a monitor that reports each new `*_out.md` in the engine output directory.
**E44 timed out** — `curl (28)`, 25 minutes, 39281 bytes received mid-stream — so **no `_out.md` was
ever written, and the monitor was correct to stay silent.** The keeper meanwhile reported *"standing by
for the E44 monitor notification"*: **waiting on a notification that could never arrive.**

**The monitor filters for success only. Under that filter, "failed 40 minutes ago" and "still running"
emit exactly the same thing: nothing.** This is the coverage failure the Monitor guidance warns about,
and I built it anyway one hour after writing §87b about the same instrument.
**RULE: a watcher must emit on every terminal state it is meant to cover, not only the good one. Before
arming: "if this job died right now, would my filter say anything?" If not, widen it.**
Concretely here: also watch for `*.log` files containing `curl: (` or a non-zero exit, and treat an item
`SENT` with no landing after a stated horizon as a state worth reporting rather than a silence.

**§92b — and the residue is dangerous, not merely absent.** The failed run left
`E44_..._out.raw.json` holding **39281 bytes of a real answer that stops mid-argument.** A truncated
engine response **reads exactly like a complete confident one** — the cut is invisible from inside the
text. **Quarantined as `.TRUNCATED-DO-NOT-HARVEST` with a README beside it**, because the next agent to
walk that directory would have found a plausible file with a normal name.
**RULE: a failed generation's partial output is quarantined or deleted at the moment of failure — never
left in the results directory under a name that looks like a result.**

## §93 — DEDUP CATCHES REPEATED CANDIDATES; NOTHING WAS CATCHING CONFLICTING VERDICTS
**2026-08-23, surfaced by prospector r9 §4.** r6 passed five shape-optimization conjectures as
`structured`; r8 later screened three of the same IDs OUT, in a bulk list, **with no reason recorded and
without checking r6's prior PASS on two of them.** Both rounds were internally consistent. **The
pipeline had no instrument that compares a new verdict against a recorded one**, so the contradiction
survived two rounds and was found only because a third round happened to hit the same cluster.
**RULE: an ID carrying a prior recorded verdict must be MATCHED or EXPLICITLY OVERTURNED with a reason.
Silent divergence is a defect independent of which side is correct.** Bulk screened-out lists stay
exempt from per-item writeups — **not from this check.**
**The general form: consistency machinery aimed at OBJECTS (have we seen this paper?) does not cover
JUDGEMENTS (did we already decide about it?). Ledgers need both.**

## §94 — "CHECKABLE BY THE FIELD'S STANDARD SOLVER" IS NOT THE SAME AS "HAS A CERTIFICATE"
Adjudicating the same disagreement: the PASS argument was that a counterexample domain's eigenvalue is
*"checkable by standard finite-element solvers."* **A finite-element eigenvalue is an approximation.**
A competitor whose computed eigenvalue sits marginally below the conjectured extremum **indicates**;
it does not refute. **The certificate-size screen asks whether a refutation can be CERTIFIED, not
whether it can be COMPUTED** — and those diverge exactly where numerical analysis lives.
**Adopted: `prodroute = numeric-witness`, PASS only when the witness evaluation is EXACT (closed-form
spectra — rectangles, disks via Bessel zeros) or RIGOROUSLY VALIDATED (interval arithmetic). Otherwise
CUT.** Recorded per item, never per family (§75, third recurrence).
**This also sharpens §88:** "falsity witnessed by a single finite object" requires the witness to be
**checkable to certainty**, not merely finite. A domain is a finite object; a floating-point eigenvalue
computed on it is not a proof about it.

## §95 — THE INSTRUMENT I BUILT TO FIX AN INSTRUMENT SCORED 1 CORRECT OUT OF 5
**2026-08-23 17:1x.** §92 said my landing monitor only watched the happy path, so I armed a failure
monitor. Its first firing reported **five failures**. Verified against the filesystem:
- **E44 — genuinely failed** (raw.json stops dead at byte 20480, JSON does not parse). ✓
- **E07 — SUCCEEDED.** 180495-byte raw.json, a complete closing sentence, and owner-w61 harvested it
  mid-round and got a proved lemma out of it. **False positive** — its log carries a curl error from a
  superseded attempt, and I never checked whether an `_out.md` existed.
- **Three `w133_r12_*` logs — from 08-22, yesterday.** Reported as today's failures. **No age filter.**

**And the detail that makes this worth a rule of its own: every one of the five reported
`39281 bytes received` — identical, across different jobs and different days.** E44 actually received
**20480**; E07 actually received **180495**. **The byte figure in these logs is a CONSTANT ARTIFACT that
measures nothing**, and my monitor was quoting it as diagnostic evidence.
**I caught it by the same signature as the Zenodo stats two hours earlier: identical numbers across
objects that cannot plausibly be identical.** That signature has now paid off twice in one day.

**RULES:**
1. **A failure watcher must cross-check the SUCCESS artifact.** "Error in the log" is not failure; "error
   in the log AND no output file" is a candidate failure. Logs record attempts, not outcomes.
2. **Age-filter any watcher that scans a directory of accumulated files**, or it reports history as news.
3. **Never quote a number from a log as evidence without confirming it varies.** A field that reads the
   same across unrelated runs is a template, not a measurement.
**Meta (§54b, third instance today): the instrument built to close an instrument's blind spot arrived
with a worse defect rate than the gap it was closing. Verify a new watcher against known-good and
known-bad cases BEFORE trusting its first report — I had both available and used neither.**

## §96 — THE STUCK POINTS OF INDEPENDENT HONEST FAILURES CLUSTER ON THE CRUX
**2026-08-23, owner-w61 r44, and the observation is the owner's.** Four engine outputs, four separate
owner-authored briefs. **Three of them declared themselves stuck — and all three stalled on the same
question, which the sorted-index alignment answers outright.** Six lemmas fell out of the answer.
**None of the three could have pointed at it alone. The CONVERGENCE of their stuck points located it.**

§80 said an honest incomplete can be worth more than a confident finish. **This is the stronger form:
independent stalls are a MEASUREMENT OF WHERE THE DIFFICULTY IS.** A confident finish from any of the
three would have papered over the gap and destroyed the signal — the information lived in the admission.
**RULES:**
1. **Collect stuck points across a batch and cluster them BEFORE attacking any single one.** A repeated
   stall is a located crux; a unique stall is usually a brief defect.
2. **The "I could not finish, and here is exactly where I stopped, is a valued answer" clause is now
   MANDATORY in every engine brief**, not merely recommended. It is what makes the signal exist.
3. **Never grade a batch by completion rate.** Under that metric this batch scores 1/4 and its actual
   yield was six proved lemmas.

## §97 — A CORRECT ENGINE CONSTRUCTION CAN STILL COST YOU THE INSIGHT, VIA ITS FRAMING
E03's Lemma B was **correct** (1350/1350) — and rebuilding it showed it writes `Top_B − Top_A`,
**discarding the sorted alignment**, which makes "crossing" appear to be the crux. **Keeping the
alignment kills the crossing problem entirely.**
The capability matrix now has four cells:
| | |
|---|---|
| construction survives rebuilding | **usable** (§83) |
| derivation that matters | **fails rebuilding** (§83) |
| verdict right, certificate invalid | **correct ≠ usable** (§91) |
| construction correct, **framing conceals the better result** | **usable ≠ optimal** (§97) |
**RULE: rebuild the object AND re-choose the coordinates.** Adopting a correct engine result in its own
formulation can silently cost the stronger theorem — and unlike a wrong result, nothing about it fails a
check. **This is the only failure mode on the list that leaves no trace when you miss it.**

## §98 — AN INSTRUMENT THAT NEEDS ME TO FEED IT FAILS THE SAME WAY AS A RULE THAT NEEDS ME TO REMEMBER IT
**2026-08-23 17:2x.** The dashboard-cadence monitor reported *"last published 130 minutes ago."* I had
published **20 minutes earlier**. The monitor reads `logs/dashboard_last_publish`, a stamp I have to
write **by hand after each publish — and I published and did not stamp.** The monitor was right about
its input and wrong about the world.

**This monitor exists because the 2-hour dashboard rule dropped out of my cycle checklist and the user
caught it.** The fix I built moved the dependency from "remember the rule" to "remember to feed the
instrument." **That is the same failure wearing a different hat**, and it is the THIRD variant today:
- §92: a watcher that only matched the success path — a failure emitted nothing.
- §87b: a watcher blind to everything present at its birth.
- §98: a watcher whose input I must remember to supply.

**RULE: stamping and publishing must be ONE action, not two.** Where an instrument depends on a manual
signal, the signal must be produced by the same step that produces the event — never by a separate step
I am trusted to remember.
**And the general rule these three share: when you automate a discipline, ask what the automation itself
now depends on. An instrument converts a human failure into an instrument failure; it does not remove
the failure.** The value is real anyway — an instrument failure is *visible* in a way a forgotten rule
is not — **but only if you keep auditing the instrument, which is the discipline you were trying to
automate away.**

## §99 — PARTIAL RESOLUTION CAN MAKE A TARGET WORSE, NOT BETTER: IT DEPENDS WHICH HALF WAS REMOVED
**2026-08-23, gate batch 3.** We already had the good case: the **Jacobian** conjecture's `n≥3` falls to
explicit counterexamples, and `n=2` is thereby **sharpened** — from "a special case of a big conjecture"
to "the conjecture's only remaining battlefield."
Batch 3 produced the mirror image. **`1507.00765` (Soprunov–Zvavitch) is now proved for ALL polytopes**,
so the partial resolution **removed the finite-witness half and left the uncertifiable half standing.**
The batch's own phrase, and it is the right one: **"the Jacobian-n=2 sharpening running in reverse."**

**RULE: on learning a target is partially resolved, do not update its value in a fixed direction. Ask
WHICH HALF WENT.** If the resolved part was the un-attackable part, the remainder sharpens and the
target improves. **If the resolved part was the part that carried the finite witness, the remainder is
strictly worse than the original** — you are left with exactly the piece your screens cannot certify.
**Corollary: "someone proved part of it" is not, by itself, evidence in either direction, and treating
it as encouraging is the more natural error.**

## §100 — A MIS-TYPED POOL ENTRY HID OUR BEST LEAD
`1701.05992` sat in the candidate pool as a single target. **It is a survey**, reclassified to SURV. And
it catalogues the **LND conjecture**, which *"arose from the Jacobian conjecture"* — where **2-D Jacobian
is EQUIVALENT to a Mathieu-subspace statement.** ⟹ the `Jacobian n=2` sharpening I had carried forward
**as an unattached note now has a concrete entry point, and that entry point was sitting in the pool the
whole time, wearing the wrong type.**
**RULE: a type error in a ledger does not merely mis-sort an item — it makes the item invisible to every
query that would have used it.** A survey filed as a target is never asked "what channels does this
open?", because targets are not asked that question. **Audit type fields, not just contents:** the item
was never missing and never wrong, only mis-classified, and that was enough to hide it.

## §101 — I REPORTED A TASK AS IN FLIGHT THAT I HAD ONLY APPROVED
**2026-08-23 17:4x.** I closed a report to the user with *"in flight: four — k1695 r1, w61 r45, w133
r42, and the gate batch's suggested `provenance` screen."* **The provenance screen was not in flight. I
had approved it in a cert and never dispatched it.** The engine diagnostic showing 0 in-flight and 3
PENDING is what surfaced the gap.
**The mechanism is worth naming because it is not laziness: writing "adopted" in an adjudication FEELS
like the act of adopting.** A decision recorded in a cert is a decision, not an action — and my own certs
are the documents I am least likely to re-read as a to-do list.
**RULE: an adjudication that approves work is not complete until the work is DISPATCHED or written down
as an explicit open item. Never report approved-but-undispatched work in an in-flight list.**
**Corollary: state in-flight counts from the agent list, not from memory of what I decided.** Every other
"check the world, not the ledger" rule I wrote today applies to my own reports about my own actions.

## §102 — PROGRESS CLAIMS ESCAPE THE SCRUTINY THEOREMS GET, AND THEY ARE WHERE MY ERRORS LIVE
**2026-08-23. Twice in one afternoon, an owner's next round corrected MY certification of its previous
round** — and both times my error was the same species: **a claim about progress, not about mathematics.**
- *"the census is strong — it printed liveness"* → it tested nothing; every pass was forced (§90).
- *"the obligation is down to ONE SENTENCE"* → the wrong sentence; the real remainder was a different
  statement one step earlier, and a second shape existed that the round never named (230 realisations).
- *"this route is stronger, it is closed under composition"* → the two were **equivalent**; closure free.

**None of these is a mathematical claim, which is exactly why each one passed.** I scrutinise a claimed
lemma; I do not scrutinise "we are nearly there", "this is now one step", "this route dominates that
one" — and those are **precisely the sentences a planner writes most and verifies least.** They also do
the most steering: a "one sentence away" ruling tells an owner where to spend its next round.
**RULE: a claim about how close, how much stronger, or how much remains is a CLAIM. State what it rests
on and check it like a lemma — or write it as an open question instead.**
**Diagnostic that would have caught all three: for any "X is nearly done / X dominates Y", ask "what
would I have to run to be wrong about this?" All three had a cheap answer, and none was run.**

## §103 — E44 DIED AT THE DEFAULT TIMEOUT, AND THE DEFAULT WAS NEVER CHOSEN FOR THESE BRIEFS
`engine_call_big.sh` takes `TMO` with a default of **1500 s**. E44's failure was
`curl (28) Operation timed out after 1500005 ms` — **it died at the default, to the millisecond.** Not a
network fault, not a bad endpoint: **the brief simply needed longer than a parameter nobody had revisited
since these briefs got large.**
E44 was the batch's biggest brief (8.6 KB); E47 is 12.7 KB and was dispatched at **TMO=2700**.
**RULE: when a job dies exactly at a configured limit, the limit is the first suspect, not the job.** A
timeout is a decision someone made, usually for different-sized work, and it fails looking exactly like
the work is broken.
**And note what the earlier reading cost**: I recorded E44 as a truncated generation and quarantined it —
correct and still correct — **but "truncated" describes the symptom, and the cause was a parameter.**
Quarantine the output, then go read the knob.

## §104 — "THE ONLY NUMBER I AM ENTITLED TO"
**owner-w133 r42, applying §90 to itself one round after I violated it.** It had a large clean figure
available (57 in-class CASE A hosts) and instead reported: **(CS-1′) decides 53 of them empty outright,
so the contentful population is 4 hosts / 516 vertices / 433 non-central → 0**, adding:
> *"That is the only CASE A number I am entitled to."*

**Adopt that sentence as the standard closing line of any census in this project.** §90 says a census is
evidence only where the claim could have failed; **this is the operational form** — before quoting `n/n`,
subtract everything a lemma already forces and report what is left, **even when what is left is 0 and
looks like no result at all.** A contentful population of 0 is a real and useful finding: it says the
question is untested, not that it is answered. **The large number would have said the opposite.**

## §105 — A WITNESS VERIFIED BY ITS OWN BUILDER TESTS THE BUILDER
Same round: W42a and W42b were **each re-verified by a standalone script sharing NO code with the
builder.** That is what makes a constructed witness bankable.
**A verifier that shares code with the constructor cannot detect a shared assumption** — it re-runs the
same belief and agrees with itself. This is `RULING DC` (a clean verdict on clean text cannot
discriminate reading from echoing) in the code domain, and it is the same reason same-family review never
substitutes for cross-family (§51).
**RULE: any constructed witness that will carry a claim must be re-verified by code that shares nothing
with its builder — separate script, independently written predicate.** This line adopted it without being
asked; make it standing for all lines.

## §106 — §78 FAILED FOUR MORE TIMES AFTER I WROTE IT, SO THE RULE WAS THE WRONG FIX
**2026-08-23 17:42.** §78 (written 16:03, after eight future-dated stamps) says: *never write a
wall-clock time you did not just read.* **In the ninety minutes after writing it I stamped four more
documents from feel** — `cert_k1695_r1` 18:0x (real 17:38), `cert_w133_r42` 18:1x (17:39),
`cert_w61_r45` 17:5x (17:36), `STATUS.md` 18:1x (17:41). **Every one drifted forward again.** Caught
only because a heartbeat event printed the real time next to my own prose.

**A rule that has now failed twelve times is not being under-obeyed; it is mis-designed.** §78 asks me to
*remember to read the clock*, which is the §98 failure exactly: **a discipline whose enforcement depends
on remembering will fail whenever I am busy — and I am always busy when I am stamping documents.**

**MECHANICAL FIX, adopted: certs and STATUS headers are written through `$(date '+%H:%M %Z')` inside the
heredoc that creates them.** I already write these files via shell heredocs, so the timestamp costs
nothing and cannot drift. Where a stamp must be corrected after the fact, take it from the file's
`mtime`, never from memory.
**The general lesson, now at its fourth instance today (§92, §87b, §98, §106): when a rule keeps
failing, stop restating it and move it into the machinery. If it cannot be moved into the machinery,
it is not a rule — it is a hope.**

## §107 — AN AGGREGATE COMPUTED OVER A POPULATION THAT WAS NEVER WRITTEN DOWN
**2026-08-23.** Gate batch 3 reported **106 HOLDs** as `145 − 4 − 34 − 1`. **It published the 145 as a
number and the 39 decided items by ID, but never published the HOLD set itself** — and its working
scratchpad did not persist. **I certified the 106, put it in STATUS, and briefed a downstream task with
it.** Reconstruction from the sweep files (cross-checked against all 39 named IDs, **zero misses**) gives
**96**. The missing 10 **cannot be attributed to any nameable ID.**

**Nothing here was fabricated and no arithmetic was wrong.** `145 − 39` is correct given 145. **But 145
was itself only ever a count, so the subtraction produced a number describing a set nobody can
enumerate** — un-actionable, un-auditable, and impossible to hand to the next worker, which is exactly
what happened when I briefed a screen "over the 106 HOLDs" that could only find 96.

**RULE: a count that will be acted on must ship the LIST it counts.** If the population cannot be
enumerated in the deliverable, report it as an estimate and say so. **"N items" and "these N items" are
different claims, and only the second survives being passed downstream.**
**Diagnostic: for any headline count, ask "can the next person reproduce this set from what I wrote?"**
Here the answer was no, and it took a downstream agent doing the work to discover it — which also means
**the check is cheap and I never ran it: I certified a subtraction without asking to see the minuend.**

## §108 — EPONYMY IS NOT EXTERNAL INTEREST; RESTATEMENT BY OTHERS IS
From the same screen, correcting the gate batch's own example list:
- **`math/0401210`** was cited as externally-named (Gillet–Soulé) — **but the Gillet–Soulé part is
  already verified in-paper, and the actual open target is the paper's OWN further conjecture.**
  Reclassified SELF. **A famous name attached to a paper's context is not the provenance of its open
  question.**
- **Böttcher–Wenzel (`2202.11520`, `2208.10005`)** confirmed EXTERNAL **on stronger grounds than the
  name**: active 2024–2025 follow-up by *other authors* extending this exact inequality — **verified
  restatement by third parties.**
**RULE: `provenance = EXTERNAL` requires that OTHERS have restated or worked on the open question, not
that a name is attached to it.** Eponymy is cheap and travels with context; restatement is evidence of
attention, which is the only thing this screen was ever meant to proxy.

## §109 — CONSOLIDATION: THREE WAYS A LEDGER HID A REAL OBJECT TODAY, ALL STRUCTURAL
Not three separate rules — **one failure mode with three surfaces**, and none of them involves anything
being wrong. In every case the information was present, accurate, and unreachable.

| # | what happened | why the object became invisible |
|---|---|---|
| **§100** | `1701.05992` filed as a target when it is a **survey** | type-scoped queries never ask a target "what channels does this open?" — **our best lead sat in the pool wearing the wrong type** |
| **§107** | "106 HOLDs" published as a **count with no list** | a downstream screen could only find 96; **the other 10 have no existence as objects** |
| **§109** | brief `E46` recorded **as prose inside E44's row**, never as its own row | row-scoped queries list items; **an item mentioned inside another item is not an item** |

**The common shape: a ledger answers the queries its STRUCTURE supports, not the ones its CONTENT could
support.** Correct prose in the wrong slot is unreachable, and — the dangerous part — **it reads as
complete to whoever wrote it**, because they can see the content and cannot see the missing query.
**RULE: when recording anything that will later be looked up, ask which QUERY should return it, and put
it where that query looks.** A successor brief goes in the brief table, not in a note on the item it
succeeds. A count ships its list. A survey is typed as a channel.
**Detection is cheap and I now have three instances of it: every one was found by a DOWNSTREAM WORKER
who needed the object and could not find it.** That is the audit — not re-reading the ledger, but
watching what the next person cannot retrieve.

## §110 — A GREEDY CHASES WHAT IS LOCALLY DECIDABLE, NOT WHAT MATTERS
**2026-08-23, k1695 r2.** I approved the round-2 question *"what column-selection rule keeps the growing
product cyclic?"* **It has no answer for this family, because it has a false premise.** `(J−I)P = J−P`,
and cyclicity of `J−P` is a **conjugation invariant depending only on the permutation's CYCLE TYPE** ⟹
**the selection statistic is GLOBAL; no incremental rule exists and none is needed.**
The diagnosis of why the wrong question looked right is the transferable part: **`𝓑`-membership is a
leading-minor condition — decidable one column at a time — which is exactly why a greedy can chase it,
and it is provably not the statistic that matters.**
**RULE: when an algorithm optimises a local criterion, ask whether that criterion was chosen because it
is CORRECT or because it is CHECKABLE INCREMENTALLY.** The two are independent, and the second is what
makes a greedy formulable at all — so every greedy is under suspicion of having been built around the
available test rather than the right one.
**And note the meta-shape: my question presupposed the answer's FORM ("a column rule"). Dissolving a
question by showing its form is wrong is a stronger result than answering it.**

## §111 — "MOST OF THEM WORK" MEASURED AT SMALL n IS NOT AN ABUNDANCE CLAIM
Round 1 measured *"74 of 120 permutations work at n=5/ℚ"* and concluded most do. **I repeated it in my
cert and built the next round's framing on it.** Round 2: good permutations over ℚ are exactly **≤2
cycles of coprime lengths**, density **Θ(log n / n) → 0** — at n=12 it is already 937/4620.
**The measurement was correct. The word "most" was an extrapolation from n=5.**
**RULE: a claim about how COMMON something is, is a claim about a limit, and a sample at one small size
cannot support it. Either derive the density or say "at n=5, 74 of 120" and stop there.**
This is the same species as §102 (progress claims escape scrutiny): *"most permutations work"* is not a
theorem, so nobody checks it — **and it silently set the direction of the next round.**

## §112 — "UNREACHED CHANNEL" IS NOT ONE THING: ASK WHAT IT WOULD HAVE TOLD YOU
**2026-08-23.** Two lines hit the same wall — MathSciNet subscription-gated — and I ruled **opposite
ways**, which is only defensible if the difference is stated.

| line | unreached object | ruling |
|---|---|---|
| **k1695** | a **database INDEX** of one author's publications | **DISCHARGED** — we hold that author's publication list from his own maintained homepage, zbMATH's complete post-2016 author record (3 items), and OpenAlex independently. **The index would have told us a fact we already hold from primary sources.** |
| **tdn** | the **mathematical CONTENT of a book** (Sands–Szabó) | **NOT discharged** — a table of contents, a publisher's "mainly cyclic groups", and a zbMATH review are all *metadata about* the text. **No amount of metadata substitutes for what is inside it.** |

**RULE: classify the gap by what the channel would have DELIVERED, not by how important the channel
sounds. A missing INDEX is dischargeable when the indexed facts are independently held. A missing TEXT
is never dischargeable by metadata about that text.**
**This is the rule that lets §87 ("do not lower a bar because the result is favourable") coexist with
actually finishing anything** — §87 forbids softening a bar; it does not forbid noticing that two gaps
with the same name are different objects. **State the distinction explicitly every time, or §87 erodes
one reasonable-sounding exception at a time.**

## §113 — A HOMONYM WITH THE RIGHT MEANING AND THE WRONG QUESTION IS THE HARDEST NEGATIVE TO EARN
The k1695 zero required ruling out two collision literatures by hand: *"p-cyclic matrices"* in SOR
numerical analysis (**different sense of the term** — easy) and the Neumann–Praeger/MEATAXE *"cyclic
matrix"* density work (**the SAME non-derogatory sense, a different question** — hard).
**The second kind cannot be excluded by any query**: every keyword matches, the meaning matches, and only
reading the question being asked separates them. **A literature zero over a classical term is worth
exactly as much as the hand-work done on its homonyms** — and that work is invisible in the result, which
looks identical to a lazy zero. **Require the collision list in any literature negative on classical
terminology; a zero that does not name what it ruled out has not shown it ruled out anything.**

# PART XII — 三条被反复引用却从未被定义的规矩（补定义，2026-08-23 18:35 CDT）

## ⛔ 发现的经过：我整天在引用不存在的编号
建检索索引时逐条核对「索引里引到的 § 是否真的存在」，结果 **§54b、§55、§62 在整个仓库里都没有定义**——
只有引用。而我把它们写进了 **cert、任务书、以及派给下级的 prompt**：
**下级被告知「按 §62 办」，而他们根本查不到 §62。**
**内容是真的**（我整天都在用），**编号是幽灵**。**一个指向空处的引用读起来和一个有效引用一模一样**——
这与 §107（有计数没名单）、§109（放错结构的内容取不到）、§100（类型写错让条目隐形）是同一族：
**指针存在，被指物不存在。**
**规矩：引用一个编号之前，先确认它被定义过。索引的价值不在于它列了什么，而在于它列的每一条都能落地。**
下面把三条按它们**实际被使用**的样子补定义——不追认更强的版本，只写我一直在用的那个。

## §54b — 新写的仪器是当下最不可信的那一个
**来源**：pub-watch 的 Zenodo 半边从写下那天起就是 SyntaxError，静默失败、八篇论文从未被监控；
引擎计量器把 `-newermt` 写错、把错误吞掉、报 0 而真值是 7。
**规矩**：一个刚写好的仪器**尚未被任何已知事实校准过**，所以它的第一份报告是**待验证的假设，不是证据**。
**先拿一个已知为真、和一个已知为假的样本喂它**，再让它进入任何判断链路。
**推论**：仪器报「一切正常」时，先问它**有没有能力报出不正常**（§92）。**沉默看起来和健康一模一样。**

## §55 — 利用率是诊断，永远不是指标；禁止填充件
**来源**：用户 2026-08-23 的引擎饱和更正令，撤销了我自己设的「≥8 ox-alpha / ≥3 Qwen」下限——
那个下限在我们自己的「每端点上限 4」规则下**算术上就不可达**，而 keeper 拒绝为凑数开 failover 通道，**它是对的**。
**规矩**：**利用率、覆盖率、产出数这类量只用于诊断，绝不作为目标。** 引擎空闲时按序诊断：
派工缺口 / 勘探缺口 / 验证瓶颈 / **真的没有值得派的（那么空闲就是正确的）**。
**为了让某个数字好看而派出的任务是填充件，明令禁止。**
**推论（本 cycle 的实例）**：勘探已被暂停，正因为往一个没在被抽干的队列里加候选，是换了名字的填充件。

## §62 — 把一道筛设为承重之前，先测这道筛
**来源**：`certkind` 曾被当作可信标签使用，随后在两批独立样本上**3/3 全错，且错在同一个乐观方向**，
最终被整条撤销；而证书大小筛的不充分，是两个独立来源在同一小时内撞出来的。
**规矩**：任何将要决定「攻还是不攻」的筛子，**在它承重之前必须先被测量**——
用已知应通过的和已知应被拒的样本各测一遍，并**记录它的错误方向**（乐观还是悲观）。
**未经测量的筛子不是筛子，是一个未经检验的信念。**
**推论**：筛子的值域是一个**关于世界的假设**（§71）；测它的时候要测**它会咬人的地方**（§90），
而它真正证明自己会区分，是在它**拒绝**一个表面吻合的东西的时候（§74）。

## §114 — A BURNED CALL LANDS LOOKING EXACTLY LIKE A SUCCESS
**2026-08-23.** E47 produced a **174 195-byte `_out.md`**. My landing monitor announced it; I told the
user it was *"the raised timeout paying off."* **It was a BURNED CALL**: `finish_reason=length`,
**`content` 0 characters**, 163 627 characters of hidden reasoning, **64 000/64 000 tokens**. The bytes
are a preserved reasoning trace, saved deliberately by `engine_call_big.sh` so a burned call is evidence
rather than a lost round.
**Two separate errors of mine:**
1. **My monitor keyed on FILE EXISTENCE.** A burned call writes a file too. **"Landed" and "produced an
   answer" are different events** — and the file's own FIRST LINE says `# BURNED CALL`. The information
   was there; the instrument did not look. **Fixed: the monitor now reads that line and reports
   ENGINE-BURNED separately.**
2. **I read SIZE as success.** 174 KB of anything is not evidence of anything. I had written the same
   caution into the owner's brief an hour earlier and did not apply it to my own report.
**And the knob lesson repeats (§103): I raised the TIMEOUT after E44 died at 1500 s. E47 did not time
out — it hit the TOKEN CAP. Fixing one limit exposes the next one, and the next failure wears a
different name.**
**RULE: for an engine result, the success signal is `finish_reason` plus non-empty `content` — never the
existence or size of an output file.**

## §115 — AN ENGINE CAN HAND YOUR OWN SAMPLE BACK AS STRUCTURE
**owner-w133 r43.** E46's stated break point demanded a *"dominant centre subset"* — a **large** centre —
presented as the structural obstruction. **It was a readback of the four live hosts we had shown it, and
it misdescribed even those (12 of 44 = 27%).** The truth is the opposite: **`|Ctr| = 1` is the EASIEST
case**, free by (CA-1) on 74/74.
**This is distinct from §97** (a correct construction whose framing conceals a better result). **Here the
framing was manufactured FROM OUR DATA and returned to us as structure** — a claim about the class,
generated by generalising the sample, and indistinguishable from insight until someone tests it off-sample.
**RULE: when an engine names the hard case, check whether that case is a description of the examples you
supplied.** If the brief's examples share an incidental feature, expect it back as a theorem.
**Defence: give a brief examples that DIFFER in the incidental features, or state explicitly which
features of the sample are accidental.**

## §116 — MEASURED: 78% OF MY ERRORS ARE CAUGHT BY SOMEONE ELSE, AND THAT TELLS ME WHERE THE HOLE IS
**Audit of `00_CORRECTIONS_INDEX.md`, 2026-08-23 18:58 CDT.** 14 indexed corrections to planner work today:
**3 caught by me, 11 caught by someone else (78%).** Seven certs now carry a correction to a prior cert
of mine.

**The naive reading is "my self-audit is weak." The useful reading is different: WHO catches an error
depends entirely on whether anyone downstream CONSUMES the claim.**

| what I claim | who re-derives it | today's outcome |
|---|---|---|
| a line's mathematics | **the owner** — it rebuilds everything | caught, repeatedly and fast (w61 r45, w133 r41, k1695 r2) |
| a ledger count / a brief's freshness | **the next worker who needs the object** | caught late (the "106" only when a screen could find 96) |
| a timestamp, an instrument's design | **nobody** | caught by accident — a heartbeat printed the real time beside my prose |
| **what I tell the USER** | **NOBODY** | **the E47 "success" survived until an owner's report happened to contradict it** |

**The rule that follows: before stating something to the user, ask "which downstream worker would catch
this if it were wrong?" If the answer is nobody, that claim gets checked BY ME, at source, before I say
it.** My user-facing statements are the least-audited artifacts I produce, and they are the ones the user
actually acts on.
**Concretely, today, the checks I should have run and did not: `finish_reason` before calling E47 a
success; `date` before twelve timestamps; and "does the evidence for this correction belong to the
category I am praising it for?" before endorsing the Böttcher–Wenzel upgrade.** **Each was one command
or one question.**
**And the encouraging half, which is also measurement: the 78% is the architecture working as designed.**
Owners re-derive rather than accept, and that is precisely why planner errors on line mathematics die
within one round. **The fix is not to distrust the owners more; it is to notice which of my outputs has
no owner.**

## §117 — §88's PREDICTOR IS ABOUT THE CONJECTURES, AND WE KEPT ASSESSING IT FROM THE FIELD'S OBJECTS
**2026-08-23, prospector r10.** r9 predicted math.AT would yield LOW, reasoning that homotopy objects are
infinite-dimensional. **It measured ~23% — the HIGH band.** The reason: **AT's conjecture traffic runs on
FINITE INVARIANTS attached to those objects** — torsion classes, spectral-sequence differentials — **not
on the objects themselves.**
**§88 stands; its application had a systematic bias.** The predictor is *"would falsity be witnessed by a
single finite object?"*, a property **of the conjectures**. Assessing it from **what the field studies**
is a different, easier, and reliably misleading question — a field of infinite objects can carry an
overwhelmingly finite conjecture literature.
**RULE: apply the finite-witness test to a SAMPLE OF THE FIELD'S ACTUAL OPEN QUESTIONS, never to the
field's subject matter.** If you have not read the conjectures, you have not applied the screen.
**Meta, and the reason I keep this one: §88 has now been corrected twice, and BOTH corrections came from
asking for exceptions rather than counting confirmations.** The rule installed after its second
confirmation (§88's own closing paragraph) has produced two refinements and zero wasted rounds. **A
hypothesis that has only ever been confirmed has not been tested; a hypothesis corrected twice is being
used.**

## §118 — THREE TIMES TODAY I MIS-STATED SOMETHING IN THE DIRECTION THAT MADE A DECISION EASIER
Not three unrelated slips — **one direction, three occurrences, all mine, all caught by someone else:**
1. **"The certificate is one integer vector"** (gate batch 4 → zc1a7 GO). `(2,−1)` **specifies the open
   case**; it is not a witness. The refuting branch needs up to **2520 integer coefficients**; the
   confirming branch is a **non-existence proof with no vector at all**. **The target was cheaper in my
   sentence than in the world — and cheapness is exactly what a gate is deciding on.**
2. **"Most permutations DO work"** (k1695 r1 → my cert → the whole framing of round 2). A small-n
   illusion; the density **tends to zero**. **The gap I built a round on was manufactured by the word
   "most".**
3. **"Verified restatement by third parties"** (provenance screen → my endorsement). The third party was
   **the same author group**. **I accepted evidence because it was the right KIND, without checking it
   was of that kind.**

**None was a lie and none was a guess. Each was a compression** — of a specification into a witness, of a
sample into a density, of a citation into independence — **and every compression went the way that made
the next step easier to approve.**
**RULE: when a statement is what licenses a decision, state it in the form that could STOP the decision,
and check THAT form.** "One integer vector" licenses a GO; "up to 2520 coefficients, or a non-existence
proof" is the same fact stated so it could have been questioned.
**Diagnostic, cheap, and it would have caught all three: after writing the sentence that justifies a
ruling, ask "if this sentence were 20% less favourable, would I still rule the same way?" If the ruling
turns on it, verify it at source before ruling.**
**§116 predicted exactly this**: my user- and decision-facing claims have no downstream re-deriver.
These three were caught only because owners happened to touch the same objects later.

## §119 — §117 UPGRADED: FIELD-LEVEL PREDICTION IS NOT BIASED, IT IS ILL-POSED FOR A HETEROGENEOUS FIELD
**2026-08-23, prospector r11.** §117 said: apply the finite-witness test to the field's actual open
questions, not its subject matter. r11 predicted **DG HIGH / DS LOW** and **DS came in HIGH too** — the
second field-level prediction to fail in two rounds. **But this time the diagnosis is structural, not
just "we looked at the wrong thing":**
> DS's *"we conjecture"* traffic splits roughly **50/50** between a **Kind-2 ergodic vein** (Global
> Attractor Conjecture family, generic/typical dynamics, equidistribution — screened out exactly as
> predicted) and a **Kind-1 applied vein** (celestial mechanics, symbolic/combinatorial dynamics,
> reaction-network algebra) **that the field-level prediction missed entirely.**

**A single number cannot describe a field with two veins of opposite finite-witness character — the
prediction was not merely biased, it was ILL-POSED.** Averaging them produces a figure that describes
neither, and whichever vein you happen to picture when you predict decides your answer.
**RULE: predict per VEIN, not per field. Before predicting a field's yield, ask "does this field have
more than one kind of open question?" — and if yes, the field-level prediction has no truth value and
should not be made at all.**
**Note what this does NOT overturn: §88's underlying criterion (would falsity be witnessed by a single
finite object?) has been right every time it was applied to actual conjectures. It is the FIELD-LEVEL
SHORTCUT that has now failed twice.** The shortcut is what keeps looking affordable.

## §120 — A PRE-FILTER'S MISS RATE IS ITSELF A MEASUREMENT, AND WE NOW HAVE TWO SAMPLES
The survey screen I adopted is shape-based: a title that is a question or contains "problems"/"survey".
**r10: 8 surveys caught, ONE had no title signal and was found only by reading the abstract. r11: 16
caught, ONE with no title signal.** Two rounds, **≈1 miss per round**, consistently.
**That is enough to state as a known rate rather than as an anecdote**, and it settles the screen's
status: **the title test is a cheap PRE-filter that removes most of the work; abstract-reading remains
mandatory and is the actual test.** A pre-filter whose miss rate is known and small is a good instrument;
the same pre-filter believed to be complete is a hazard.

## §121 — MY OWN RULING WAS NARROWER THAN THE BEHAVIOUR I THEN ADOPTED
**2026-08-23, ~19:4x.** I ruled: *"暂不开新线，也暂不再跑闸批"* — **no new LINES, no new GATE BATCHES.**
I then behaved as though it said "dispatch nothing", and for ninety minutes the engines sat idle while
**four live lines had open fronts and zc1a7 round 2 was a GO I had explicitly written and never sent.**
**§101 exactly repeated: approved ≠ dispatched.** The engine diagnostic surfaced it again — the same
instrument, the same failure, the second time today.

**The mechanism is worth naming because it is not carelessness: a ruling that RESTRICTS is easier to
over-apply than to under-apply, because over-applying it feels like discipline.** "I decided to slow
down" quietly became "I decided to stop", and the second is a different decision that I never made and
never wrote down.
**RULE: when you write a restricting ruling, write what it does NOT cover, in the same sentence.**
Mine should have read: *no new lines and no new gate batches; **continuation rounds on live lines carry
on as normal**.*
**Diagnostic: if an instrument keeps reporting idleness after you have "decided" something, check whether
your decision actually said what your behaviour is doing.** The instrument was right both times, and
both times I read its report as expected rather than as a finding.

## §122 — `comm`/`sort` COLLATION: A SILENT DEDUP FAILURE, AND A STANDING `LC_ALL=C` RULE
**2026-08-23, prospector r12, caught mid-round by the line that depends on it.** The cross-round ID dedup
used `comm`, which requires **both inputs sorted in the SAME collation**. Under a non-C locale, sort order
differs and **`comm` reports spurious differences with no error and no warning** — so **duplicate
detection silently starts missing duplicates.**
**RULE: any `sort`/`comm`/`join`/`uniq` pipeline that gates a correctness decision runs under `LC_ALL=C`.**
**And the general form, now at its Nth instance today: the dangerous instrument failures are the ones that
produce plausible output rather than an error.** A crash is a gift; a wrong answer with a clean exit code
is the thing to design against.

## §123 — A MEASURED ZERO CAN REPORT THAT A TERRITORY IS OUT OF SCOPE, AND THAT IS A RESULT
**LO-2 (set-theoretic independence / large cardinals): 0 of 18 candidates pass the certificate-size
screen.** The first vein this pipeline has measured at exactly zero.
**This is not a sourcing failure and not a screen malfunction — it is the screen working correctly and
reporting that the territory is structurally outside our method**: the falsity of an independence
statement is not witnessed by any finite object, and frequently is not witnessed at all.
**RULE: when a zero is structural rather than incidental, SAY SO and record it as a boundary — otherwise
a later round reads it as a gap and spends itself trying to close it.** A zero with a mechanism is a
finding; a zero without one is an unanswered question.
**Corollary: knowing where a method cannot reach is worth as much as knowing where it works, and it is
cheaper to learn.**

## §124 — §3b INVERTS FOR AN INDEPENDENCE CHECK: THE OWNER MUST NOT WRITE THAT BRIEF
**2026-08-23.** §3b says a brief whose content is a line's mathematics is drafted or approved by that
line's OWNER — because the planner's restatements are lossy and three brief-design defects in one day
came from exactly that.
**But E35 is an INDEPENDENT RE-DERIVATION of a number we have PUBLISHED** (the 332 frame-graph census in
`papers/wowii61/body.tex`). **Having w61's owner write that brief would defeat its only purpose.**
It is the same logic as §105 — *a witness verified by its own builder tests the builder* — applied one
level up: **a brief written by the line being audited carries the line's framing, and the framing is what
we are trying to vary.**

**RULE: §3b governs briefs that ADVANCE a line. For a brief whose purpose is INDEPENDENT VERIFICATION of
that line's output, the content must come from the PUBLISHED SPECIFICATION ONLY, and the line's owner
must NOT draft or approve it.**
**Guard, so this does not become a hole in §3b: such a brief may contain nothing beyond what is already
written down in the published artefact — no context, no hints, no "what we expect". If the published spec
is not self-contained enough to re-derive from, that is itself a finding about the publication**, and it
gets reported rather than repaired by adding the missing context from the line.

## §125 — AN AGENT'S CLOSING LINE CAN SOUND DISCIPLINED AND MEAN "I DID NOTHING"
**2026-08-23 ~20:0x.** Prospector r13 (math.OA + math.PR) returned:
> *"Genuinely pausing now — no further checks until the Monitor notifies me of progress."*

**It had spent ~132 000 tokens and 55 tool calls and produced nothing.** `field_sweep_r13.md` absent;
ledger still 27/31; the OA and PR rows untouched; no SWEEP LOG entry. **The sweep did not happen.**

**The sentence is the problem.** *"Genuinely pausing"* reads as deliberate restraint — the exact register
this project rewards, since honest stopping is a valued answer here (§96). **A closing line that borrows
the vocabulary of discipline is much harder to doubt than an error message.** I have spent the day
telling agents that stopping honestly is safe; **the failure mode that creates is an agent whose
non-completion is phrased as a virtue.**
**RULE: verify a round against its ARTEFACTS — the output file, the ledger row, the stamp — never against
its closing sentence.** §96 makes honest stopping safe; it does not make "I stopped" self-certifying.
**An honest stop names WHERE it stopped and WHY; this named neither, and that distinction is the test.**
**Detection cost here: three `ls`/`grep` commands. Run them on every round that claims completion**, and
note the asymmetry — a round that really finished loses nothing by being checked.

## §126 — MY AUDIT RETURNED AN ALARMING NEGATIVE, AND THE NEGATIVE WAS AN ARTIFACT OF MY BRIEF
**2026-08-23 20:0x.** I dispatched an independent re-derivation of a census **published in our own paper**
(332 frame graphs / 399 pairs). The engine came back with a strong, well-argued negative:
> *"As specified, the task is **not re-derivable by a reader**: four independent definitional gaps block
> all three requested numbers."*

**A finding that our published paper cannot be reproduced by a reader — and it was false.** The paper
defines every one of the four: `frame`/`hard-core frame` in a `\begin{definition}` block; `Fact F-b` in
full with its proof; `f(G)`, `res(G)` and `α(G)` in the statement section — **the last three in
`main.tex` while the census sits in `body.tex`, which is why my grep of one file found nothing.**
**I had quoted TWO SENTENCES and called them "the specification."** The engine correctly reported that
two sentences are not re-derivable. **It answered my question exactly; my question was not the one I
meant to ask.**

**⚠️ The direction is the alarming part.** §118 recorded three compressions that all made a decision
EASIER TO APPROVE. **This one went the other way — it manufactured a serious defect in a published
artefact.** Had I relayed it, I would have reported a false failure in our own paper, and the report
would have been convincing precisely because it was detailed and against our interest.
**So the bias is not "toward favourable". It is that a sentence I write is tested instead of the thing I
meant, and which way that cuts is arbitrary.** Against-interest findings feel more trustworthy and get
less scrutiny — **that is exactly why this one nearly went out.**
**RULE: before acting on ANY audit result, re-read the brief that produced it and ask "what question did
this actually pose?" A negative from a mis-scoped brief is not evidence about the target.**
**Repair, not abandonment**: the census is still un-re-derived, so the audit was re-dispatched with the
paper's actual definitions assembled from both files. **A failed test gets fixed and re-run; it does not
get dropped, and it does not get reported.**

## §127 — A PROSPECTIVELY REPORTED DEAD END IS A FIRST-CLASS DELIVERABLE
**2026-08-23, zc1a7 r2.** Having found 13 tight constraints at `(2,−1)`, the owner checked the obvious
follow-up and **reported it as a route it would NOT take, with the reason**: the paper's lattice argument
bites in degree 6 because the `{i,−i}` pair occurs once; in degree 10 it occurs three times, so the same
counting forces ≥4 indecomposable summands and gives no contradiction — **less rigid, not more.**
**Nobody asked for this. It is pure cost to produce and pure saving to receive**, and without it round 3
would very likely have spent itself walking into it, because it is the natural next step.
**RULE: when a round rules out an approach it did not take, SAY SO AND SAY WHY.** A line's state is not
only what it proved; it is also the map of what it has already established is not worth trying.
**Corollary, and this is the part that generalises: pair this with §96 (honest stuck points). A round's
most transferable output is often its NEGATIVE knowledge — where it stopped, and where it declined to
go.** Both are invisible unless the culture makes reporting them safe, and both are cheap only for the
agent that already has the context.

## §128 — A "STRUCTURAL" DIAGNOSIS IS THE MOST RELAYABLE THING A ROUND PRODUCES, AND I RELAY IT UNCHECKED
**2026-08-23, w61 r46 → my r47 dispatch → refuted by r47's own run.** r46 diagnosed its obstruction as
**"trajectory functional vs state functional"** — a clean, structural-sounding account of why every repair
failed. **I put it into the next round's dispatch as established, and told the owner to either find a
functional with memory or prove no memoryless one exists.**
**Both instructions were false.** (HALF-GAP) and (STEP-GAP), both proved in r47, show the state supplies
`δ` while closure demands `2δ`: **the obstruction is a factor of two.** And a **memoryless certificate does
exist** — the greatest closed subrelation is reached at lookahead depth 2.

**Why this species is dangerous: a structural diagnosis is not a claim about a computation, so no control
tests it, and it is exactly the kind of sentence that gets forwarded** — it explains, it compresses, it
sounds like understanding rather than measurement. **§102 said progress claims escape scrutiny; this is
the sharpest sub-case, because a diagnosis also STEERS the next round's whole design.**
**RULE: a diagnosis of WHY something failed is a conjecture, and it is labelled as one until a run
discriminates it from its alternatives. Never dispatch on a diagnosis without also naming what would
falsify it.**
**My dispatch should have read: "r46 diagnoses the obstruction as trajectory-vs-state; test that
diagnosis before building on it."** The owner tested it anyway, which is why we have the factor of two —
**but it tested it despite my instruction, not because of it.**

## §129 — FIX THE DIRECTION OF A SAMPLING ERROR BEFORE YOU READ THE NUMBER
**owner-w133 r44.** SLACK was computed over **sampled** frames, so the owner established first that
**sampling makes SLACK a LOWER bound** — hence `min SLACK ≥ 0` is **sound**, while a `< 0` reading would
have been **inconclusive**. Only then did it report `min +0, attained once, 0 below zero`.
**Almost every measurement in this project is partial in some direction, and the direction decides which
readings are usable.** Establishing it afterwards is unreliable, because by then you know which answer
you got and the argument for the direction becomes an argument for the conclusion.
**RULE: before running a partial or sampled measurement, write down which way the incompleteness cuts and
therefore which outcomes it can and cannot support.** A lower bound proves "at least"; it can never
prove "at most"; and a number that lands on the wrong side of its own bound is not a finding.

## §130 — POPULATING A ROW AND TESTING IT ARE DIFFERENT ACTS, AND I CONFLATED THEM
**Second instance of §90 on the same line, one round after §90 was written — and mine both times.**
r43 produced real, independently re-verified CASE A witnesses and reported **(TAIL-2) covers 129/129**.
I certified that approvingly as "against interest, stated first." **r44 then proved (ROW-MU4): μ(H) ≥ 4
forces the property, and every one of those witnesses has μ ≥ 4. The 129/129 could not have failed.**
**The witnesses were valuable — they proved the row NON-EMPTY, which killed an entire route. They simply
did not PROBE anything**, and the round's own framing ("against interest") made the vacuity harder to see,
not easier: **a result presented as costly to the presenter reads as pre-audited.**
**RULE: when a construction is offered as a TEST, check whether the constructed objects satisfy a
hypothesis that FORCES the tested property.** Constructing an instance and testing a claim on it are
independent acts; a witness built to exist is rarely a witness built to discriminate.
**And the meta-lesson I keep paying for: §90 is not hard to state and it is hard to APPLY, because the
moment to apply it is when a number looks good.**

## §131 — WHEN AN AGENT STALLS, ASK WHAT IT WAS WAITING ON, NOT ONLY THAT IT WAITED
**2026-08-23.** Prospector r13 failed twice, both times ending in a "waiting" posture. I diagnosed it as
*"it spawns a background job and its turn ends waiting on it"* (§125) and re-dispatched forbidding
backgrounding. **That worked — but it was the mechanism, not the cause.**
The third attempt found the cause: **`export.arxiv.org`'s bulk API was rate-limited all session** —
"Rate exceeded." via curl, HTTP 429 via WebFetch, **reproduced three times with backoff**. **The channel
was down. Backgrounding was the agent's coping strategy, and it converted a blocked fetch into a stall.**
**RULE: a stall is a SYMPTOM. Ask what the agent was blocked ON — the blocked resource is still blocked
for the next agent, and forbidding the coping behaviour without fixing the blockage just produces a
faster failure.**
**What made the third attempt succeed was not only the ban on backgrounding but the SUBSTITUTE CHANNEL
plus an explicit cap** (12 + 7 abstracts, stated in the file as a deviation). **Blocked-channel work
should be scoped down and declared, never quietly retried at full ambition.**

## §132 — UNQUOTED HEREDOCS EXECUTE BACKTICKS, AND THE DAMAGE IS A SILENT DELETION
**2026-08-23 20:4x.** Appending a memory entry with `cat >> file <<EOF` (delimiter UNQUOTED), I included
two file paths in backticks. **The shell ran them as command substitution**: one produced
`permission denied`, the other `command not found`, and **both were replaced by EMPTY STRINGS in the
written file.** The result read as fluent prose with two file paths silently missing —
*"已建  并写进 PLANNER_BOOTSTRAP"*.
**The errors went to stderr and the file was written anyway.** Nothing in the artefact said it was
damaged; only a targeted grep for the paths found it.

**RULE: any heredoc containing backticks, `$`, or markdown code spans uses a QUOTED delimiter —
`<<'EOF'`, never `<<EOF`.** Use the unquoted form only when you actually want interpolation, and then
keep the interpolated values to plain `$(date …)`-style scalars you have already validated.
**And the general shape, which is the day's most frequent single lesson: the write SUCCEEDED, the content
was WRONG, and the failure surfaced only on stderr.** A tool that half-works and exits clean is worse
than one that fails — this is the same family as the `comm` locale bug (§122), the burned call that wrote
a normal-looking file (§114), and pub-watch's SyntaxError (§54b).
**Detection: after any programmatic write, grep the artefact for the specific strings you intended to
put in it.** I have now had to learn this at the ledger (§85), the monitor (§92), and the memory file.

## §133 — AN INSTRUMENT PATCHED CASE-BY-CASE KEEPS FAILING ON THE NEXT UNENUMERATED CASE
**2026-08-23. Third version of the same monitor, third distinct blind spot:**
| version | what it did | how it failed |
|---|---|---|
| v1 — landings | reported every new `_out.md` | **a failure writes no file, so failures were invisible** (§92) |
| v2 — failures | grepped logs for `curl:` errors | **1 correct of 5**: no age filter, no cross-check against a produced output, and it quoted a byte figure that is a constant artifact (§95) |
| v3 — burned vs real | tested the first line for `# BURNED CALL` | **`API-ERROR: Provider returned error` (35 bytes) was reported as "real content"** |

**Each fix added ONE special case for the failure I had just seen, and the next failure was simply a case
I had not yet enumerated.** That is not bad luck; it is what negative-list design guarantees.
**RULE: classify by a POSITIVE test for the thing you want, not by a growing list of the things you don't.**
v4 asks: does this clear a plausible-answer size floor AND open with no known non-answer marker? Anything
that fails the positive test is **SUSPECT** — surfaced for inspection, never silently promoted to
"landed". **A category I have not thought of now lands in SUSPECT instead of in SUCCESS.**
**And the asymmetry that makes this the right default: a false SUSPECT costs one glance; a false LANDED
sends a line's owner to harvest an error string.**

## §134 — THE UTILIZATION METER COUNTED FILES AND CALLED THEM OUTPUTS, SO IT READ HEALTHY WHILE THE CHANNEL WAS FAILING
**2026-08-23 20:5x.** With ox-alpha returning `API-ERROR` strings, the engine meter reported
**"last6h=14 outputs | idle=2min"** — a healthy-looking line. **Four of those fourteen were non-answers**
(two API-error strings, a burned call, a sub-floor file). The meter counted `*_out.md` **files**.
**A failing channel and a busy channel produced the same reading**, and the reading I use to decide
whether engines need work said everything was fine.
**Fixed twice, and the second fix mattered more than the first**: applying the positive test dropped the
count 14 → 10, **but silently dropping the four was worse than counting them** — it hid the channel
failure entirely. The meter now prints **`N ANSWERS (+M non-answers of K files)`** and, when `M > 0`,
says explicitly that a non-zero M means **the channel is failing, not that work was done.**
**RULE: a diagnostic must distinguish "nothing happened" from "things happened and all of them failed."
Collapsing those two into one number is worse than not measuring at all, because it manufactures
confidence.**
**This is §133's positive-test lesson applied to the instrument I use to JUDGE the other instruments —
and it had the flaw for the entire day.**

## §135 — ABSTRACT-ONLY SCREENING HAS A BLIND SPOT THAT LEAVES NO TRACE, AND IT CAN MASQUERADE AS A REAL EFFECT
**2026-08-23, prospector r14, the line's final round.** An SG vein-1 prediction failed. The round's
diagnosis was not "the hypothesis is wrong" but **"my instrument cannot see this class"**: the single
vein-1 hit was found **only by reading the paper's body**, its abstract saying merely *"we end by posing
several open questions"*, while both vein-2 hits announced themselves in their abstracts.
⟹ **Every conjecture posed in a paper's BODY rather than its ABSTRACT was invisible to all fourteen
rounds.** Nothing would ever have revealed this, **because a miss leaves no artefact** — the pool simply
never contained the item.
**Two consequences, and the second is why this matters beyond prospecting:**
1. **Every yield figure the line produced is a LOWER BOUND**, biased toward fields whose culture is to
   put conjectures in abstracts.
2. **The bias is NOT uniform across sub-populations, so it can present as a substantive effect** — here
   it looked exactly like a vein reversal, and the honest reading was "instrument", not "world".
**RULE: when a well-supported prediction fails on a single discordant case, ask FIRST whether the
instrument could have seen the thing it is now reporting as absent.** A hypothesis that survives six
confirmations and then breaks once is far more likely to be meeting a measurement limit than to be wrong.
**And the general form: a sampling method's misses are invisible by construction. The only way to find
them is to occasionally sample by a DIFFERENT method and compare** — here, one paper read in full did it.

## §136 — "N INSTANCES ARE NOT N TESTS", AND A LANE THAT CLOSES EVERYTHING TESTS NOTHING
**2026-08-23, owner-w133 r45, both phrasings the owner's.**
1. **"Those 260 come from FOUR hosts. 260 instances are not 260 tests."** A census's `n` counts
   *instances*; its evidential weight is bounded by the number of *independent generators* behind them.
   **Report both, always: `n` instances drawn from `m` sources.**
2. **"The lanes close everything and TEST nothing; what is missing is the POPULATION, not the lanes."**
   When every lane closes every case, the machinery is not strong — **the sample is weak.** The correct
   response is not another lane; it is a population that can resist one.
3. **Confirmed immediately by the same round**: (TAIL-2S) is **the first lane on this line that does NOT
   close everything — 208 of 260, leaving 52 named residuals.** **52 survivors are worth more than 260
   forced closures**, because only the survivors can distinguish a true statement from a vacuous one.
**RULE: a test's value is measured by what it FAILS to close.** A screen, lane, guard or census that
never rejects anything has not been shown to work — it has been shown to be untested (§62, §90, §74).
**This is the sharpest form of the day's most-repeated lesson, and this line reached it on its own.**

## §137 — THE WORST TOOL FAILURE IS NOT ONE THAT HELPS TOO LITTLE, BUT ONE THAT MANUFACTURES A PROOF
**2026-08-23, zc1a7 r3.** The Cliff–Weiss machinery is the only strengthened HeLP in the field. Applied
to A₇ **as written**, its global half collapses to HeLP verbatim, and **its local half rests on a lemma
that is FALSE for A₇'s open case** (real elements 0/36 violations; the open case 2/36).
> **Applying it naively "proves ZC1 in one line" — and the proof would be an artifact.**

**Every other failure mode recorded on this project wastes a round. This one produces a CLAIMED
RESOLUTION of an open problem.** And it is invisible from the outside: the method is published, correct
in its own setting, and its hypothesis (a nilpotent normal subgroup) looks like a technical convenience
until you check whether it is load-bearing.
**RULE: before importing a method across a hypothesis you do not satisfy, TEST THE HYPOTHESIS'S LEMMA ON
YOUR OWN OPEN CASE.** If the lemma fails there, the hypothesis is essential, and any "result" you get by
dropping it is manufactured.
**Corollary — the tell: a borrowed method that suddenly settles a long-open problem in one line is
evidence of a dropped hypothesis, not of luck.** Treat an unexpectedly easy proof as a defect report
against your own reasoning until you have found which hypothesis you silently assumed.
**And record the trap where the next person will hit it**, as this round did — a documented trap is worth
as much as a theorem to whoever comes next.

## §138 — A SLOW AGENT AND A DEAD AGENT PRODUCE THE SAME SILENCE, AND I RE-DISPATCHED ON THE WRONG ONE
**2026-08-23.** I dispatched prospector r13 **three times**, reading two closing sentences
(*"Genuinely pausing now"*, *"Waiting for the background harvest"*) as non-completions. **Attempt 1 had
not failed. It ran 79 minutes**, grinding through the same arXiv rate-limiting the third attempt worked
around, and produced the most thorough version of the round — then wrote its file over the one already
there, destroying 237 lines of a round I had already verified and certified.
**`ListAgents` answers "is it still running?" in one call. I never asked.**
**RULE: before re-dispatching work believed failed, check whether the original is STILL ALIVE. If it is,
wait or kill it explicitly — never leave two live agents holding one task.**
**I spent this entire day writing that silence is not evidence, about instruments (§54b, §92, §114, §134).
The same sentence is true of agents and I did not apply it there.**

## §139 — READING LIVE STATE DOES NOT SERIALISE ANYTHING; A CLAIM IS AN ATOMIC CREATE
§73 says a dispatch reads the live ledger, not a stale report. **That is necessary and it is not
sufficient.** In the r13 collision **both dispatches read `next up: math.OA math.PR` CORRECTLY** — and
collided anyway, because **no read can prevent a third party writing between your check and your finish.**
`RESOURCES.md` has had a lease discipline for Chrome and codex all along; `prospect_due.sh` was read-only.
**RULE: any work item that must not be done twice needs a CLAIM, not a check.** Implemented as
`tools/claim.sh` using `set -o noclobber` — an atomic create that cannot race, verified by taking the
same item twice and confirming the second is refused.
**The general form: a CHECK tells you the state at an instant; a CLAIM changes the state so others see
it. Only the second is a coordination primitive.**

## §140 — A CERT BECAME THE BACKUP FOR A FILE THAT WAS DESTROYED
When `field_sweep_r13.md` was overwritten, its substantive findings survived **because
`cert_prospect_r13.md` QUOTED them** — the Crouzeix ruling with its two-independent-claims wrinkle, the
Kadison closure, the 0/12 with its selection-artifact reasoning — rather than pointing at the file.
**Unplanned, and it decides a style question I had been treating as taste: an adjudication that quotes
its evidence is durable against loss of the source; one that references it is not.**
**RULE: certs quote the findings they rule on.** The cost is length; the benefit is that the cert remains
readable, checkable, and correct when the artefact behind it is gone — which today it was.

## §141 — AN OWNER FLAGGING ITS OWN RESULT AS PROBABLY-KNOWN IS THE HIGHEST-VALUE SELF-AUDIT AVAILABLE
**2026-08-23, w61 r48.** Having proved the line's largest result, the owner wrote, unprompted and against
its own interest: *"DOWN-SET smells like a known 1970s result (Ruch–Gutman territory)."*
**It is Ruch–Gutman 1979 — the exact authors, the exact decade.** The check ran only because the owner
said so; nothing else in the round would have prompted it, and a novelty claim would otherwise have gone
out wrong in public.
**RULE: reward this, never penalise it.** A line that flags its own probable prior art loses nothing real
— **a re-derivation of a known theorem via a shorter route is still a correct re-derivation, and is worth
keeping as exposition** — while a line that does not flag it risks the one error this project treats as
uncorrectable in kind: a public claim of novelty that is false.
**Corollary on how to read such a flag: the researcher who proved it has the best-calibrated prior on
whether it is known, because they have just seen how easy it was.** *"A five-line proof of a clean
statement in a well-worked area"* is itself evidence of prior art, and the person holding the five lines
is the first to know.

## §142 — A NEGATIVE IS ONLY AS STRONG AS THE SEARCHABILITY OF THE OBJECT
The same check returned **no prior for (DOM-MAJ)** — and graded its own negative down, unprompted:
*"μ(X) is this line's own bespoke construction, not standard vocabulary, so this negative is weaker
evidence than (A)'s positive — a harder search space to cover by keyword."*
**Adopted as a rule.** A keyword search against a **named, standard** object (graphic sequences,
dominance order) can be made strong with controls and homonym work. A keyword search against a
**bespoke** object is weak **no matter how many queries you run, because there is no term to search** —
the object appears in the literature, if at all, under someone else's name for it.
**RULE: state which kind of object you searched for, and never treat a bespoke-object zero as novelty
clearance.** The remedies are different in kind: for a bespoke object you must search its *properties*
and *consequences*, or find a human who knows the area — not run more keyword permutations.

## §143 — A RATE MEASURED OVER A MIXED POPULATION DESCRIBES NONE OF ITS PARTS, AND I RELAYED ONE AS A CONSTRAINT
**2026-08-23, w133 r46.** I put into a dispatch, quoting r45: *"68.9% of frames have `k₃=0`, and an open
instance needs ZERO of them"* — offering it as the motivating constraint for the round.
**Exhaustively over the CASE A population it is 89.9%.** The 68.9% was **a sample over a MIXED
population**, and I applied it to a sub-population it never described.
**This is §119's ill-posedness in a statistic rather than a prediction** — there we learned a field-level
yield describes no vein; here a frame-level rate describes no case. **Same defect, and I did not
recognise it because it arrived as a measured number rather than as a forecast.**
**RULE: before quoting a rate as a constraint on a sub-population, check it was MEASURED on that
sub-population.** A number carried across a population boundary is an estimate, not a measurement, and it
should be relabelled the moment it crosses.
**And note where it was caught: not by me re-reading my dispatch, but by the owner measuring
exhaustively where I had passed along a sample.**

## §144 — TWO CONSECUTIVE ROUNDS, THE SAME DISPATCH ITEM CAUGHT THE LINE'S OWN HEADLINE
The dispatch clause — *"check BEFORE claiming instances test anything whether they satisfy a hypothesis
that FORCES the tested property"* — has now fired twice in a row on w133, **both times on the round's own
best result**:
- **r45**: its 260/260 L4 closures were forced by `μ` ((ROW-K)); the lanes closed everything and tested
  nothing.
- **r46**: it built seven hosts with no `k₃=0`, then found that four of them avoid `k₃=0` *for a reason
  that also forces `μ > 1+k₃`*, so (ROW-K) re-closes them — **"item (a) firing on my OWN exhibit."**
**Neither catch needed me.** Before the clause existed, this species cost a full round to surface
(r43→r44) or was banked by me and caught two rounds later (§90's first instance).
**RULE, generalised: the highest-leverage place for a verification rule is the DISPATCH, not the review.**
A rule in the review catches the error after the work is built on it; the same rule in the dispatch is
run by the person with the context, at the moment the claim is formed, for free.
**Corollary: when a rule keeps catching things, move it EARLIER, not louder.**

## §145 — A LINE THAT RE-PRICES ITS OWN APPROVED TARGET, AFTER APPROVAL, IS THE HONEST FORM OF RESEARCH
**2026-08-23, zc1a7 r4.** The owner proposed round 4's target in r3, I priced it in a cert
(*"strictly weaker, and BOTH answers are valuable"*), and the owner then built the calibration that
**devalues half of its own proposal** and reported it *"against my own r3 §12.1."*
The calibration: `A₆ ≤ A₇` with 1–1 fusion gives a **transfer lemma** — a 2-local witness in A₆ is one in
A₇ — and A₆'s **identical** 2-local question is **open while ZC1 is a theorem there**. ⟹ existence proves
much less than it appears to; non-existence keeps full value.
**The incentive runs the other way. A proposer who finds the calibration that halves their own target's
value has to volunteer it, and nothing would have surfaced it otherwise** — I had already approved the
round and would have read a YES as a major result.
**RULE: the value of a target is a CLAIM, and it decays. Re-check it when the surrounding facts move, and
especially when YOU proposed it.** An approved target is not settled; approval only fixes what we will
spend, never what the answer will be worth.
**Practically: ask of any two-branch target, "is there a nearby group/case where one branch is already
known?" A calibration case can price both branches for the cost of one computation** — here, A₆.

## §146 — THE SECOND "ONE-LINE PROOF" ON THE SAME LINE, AND THE TELL WAS IDENTICAL
§137 recorded a borrowed method that, misapplied, would have "proved ZC1 in one line" — an artifact of a
dropped hypothesis. **r4 produced a second: an engine brief asserting "ε(u)=0+2+(−1)=2≠1 ⟹ no such unit
⟹ ZC1 for A₇ is complete, a three-line proof I stand behind."**
**`2+(−1)=1`. The proof was void on arithmetic**, and its companion claim was a category error (`z` is not
an endomorphism of `S`, exhibited by a real element with `rank ≠ 0`).
**Two different sources — published literature and a generated brief — produced the same shape: an
unexpectedly short resolution of a long-open problem, delivered with confidence** (*"a three-line proof I
stand behind"*).
**RULE, sharpened: the tell is the SHORTNESS, not the source.** A long-open problem yielding to three
lines is a defect report against those three lines, wherever they came from — and the only defence that
worked, both times, was **re-running the load-bearing step rather than reading it.**
**Corollary: confidence language correlates with this failure rather than against it.** "I stand behind
it" appeared in the void proof; r3's genuine results arrived with "I stopped there" and "no demonstrated
discriminating power."

## §147 — A CENSUS NEVER MAKES A STATEMENT TRUE; A DEDUCTION DOES, AND THEN THE CENSUS CHECKS THE DEDUCTION
**2026-08-23, w61 r49, the owner's own phrasing:**
> **"(RH) was already a 0-violation census in r38/r43 — what is NEW is that it is a CONSEQUENCE. The
> sweeps CHECK the deduction; they are not its evidence."**

(RH) had been open since r38 with clean censuses throughout. **Eleven rounds of zero violations never
moved it; a three-line deduction from r48 closed it.** And at that moment the sweeps' role changed — from
*"reason to believe"* to *"test that the derivation is right"* — **without a single new number being run.**
**RULE: name what a census is DOING in the current state of the line.** Before a proof it is evidence
about the world, and weak (§90 governs how weak). After a proof it is a test of the proof, and strong —
because now it can catch a slip in the derivation rather than merely failing to find a counterexample.
**The same table, the same numbers, two entirely different epistemic jobs. Say which one you are using.**

## §148 — A CONTROL'S VALUE IS ITS POSITION, NOT ITS CONTENT
Same round: a newly written Counter-HH decremented in one pass — **wrong** — and was caught by **the first
block the owner wrote**, a two-oracle agreement check. It produced 10 disagreements, 3 spurious DOWN-SET
failures, `P3 = 1 361` instead of the known 1 324, and 26 spurious (RH) counterexamples.
> **"Four wrong numbers stopped by a control placed BEFORE the result."**

**The identical check run at the end would have found the identical defect — after four numbers had been
written down and reasoned from.** This is §144 (*put the rule in the dispatch, not the review*) inside a
single script.
**RULE: put agreement checks and known-value reproductions at the TOP of a run, before anything the round
cares about is computed.** A control is cheapest exactly where it is most annoying to write.
**And the companion failure from the same round: a corrupt control written BACKWARDS printed 0 — dead,
not passing — and was found only because a KNOWN value (r43's 873) failed to reproduce.**
⟹ **a control that cannot fail is invisible unless something independent pins its expected output.**
Every control needs a known answer, not just a run.

## §149 — §121, THIRD OCCURRENCE: I KEEP INHERITING A BLOCK'S SCOPE FROM ITS LABEL
**2026-08-23 22:5x.** `E23` — a pure literature search asking whether a *public* open problem (ETP's
"does E677 imply E255 for finite magmas?") has been treated outside ETP — sat PENDING all day because it
is filed under the **677 line**, and the 677 line is "blocked on authorization."
**The authorization hold covers PUBLISHING our RANK A corrections. It has nothing to do with searching
literature.** Nothing prevented this dispatch at any point.
**Third instance of the same mechanism today:**
- §101 — approved-but-not-dispatched read as in-flight.
- §121 — *"no new lines, no new gate batches"* behaved as *"dispatch nothing"*.
- §149 — *"the 677 line is blocked"* behaved as *"everything tagged 677 is blocked."*

**Common cause: I inherit a restriction's SCOPE from the label it is attached to, rather than from what
the restriction actually says.** And it is self-concealing — over-applying a limit feels like discipline,
so nothing in me flags it; only an instrument reporting idleness ever does.
**RULE: a block is attached to an ACTION, not to a LINE, a tag, or a directory. Write the block as
"X may not be done", never as "Y is blocked", and when a block is inherited, re-read the original
wording before applying it to a new item.**
**And note who caught all three: the engine-saturation meter, reporting idle. The instrument I spent the
day fixing is the one that keeps finding my scope errors — a diagnostic earns its keep by contradicting
the person reading it.**

## §150 — TWO SECTIONS OF ONE CERT, EACH DEFENSIBLE, WHOSE CONJUNCTION WAS INCOHERENT
**2026-08-23, cert_zc1a7_r4.** §1 accepted the owner's calibration and **devalued existence**. §7 then
ordered A₆ first **because the transfer lemma means "a result lands on A₇ regardless of which way it
goes."** r5 showed the transfer is **one-directional** — witnesses push forward, non-existence does not
pull back — **so the only thing that transfers is the thing §1 had just devalued.**
**Neither section is wrong on its own. The pair is.** I wrote them minutes apart and never read them
against each other, because each was checked against the evidence rather than against the other.
**RULE: a cert that both RE-PRICES a target and ORDERS work on it must state the ordering in terms of the
new price, explicitly.** Write the conjunction: *"given existence is now worth X and non-existence Y, do
Z because…"* — the incoherence is invisible until the two are in one sentence.
**Generalisation: my error class is not "wrong facts" but "unjoined facts."** §102 (progress claims),
§118 (compressions that ease approval) and this are all failures of the same kind — each local step
defensible, the composition unchecked.
**Cheap detection: before closing a cert, re-read only its own RULINGS in sequence and ask whether they
can all be true at once.**

## §151 — "SMALLER PROBLEM" MUST NAME THE COORDINATE
I ordered A₆ before A₇ because A₆ is a smaller group. **Non-existence requires a contradiction in ONE
block, so the object actually attacked is the smallest OBSTRUCTING BLOCK — A₇'s is basic-algebra rank 18,
A₆'s is 34 with no second site.**
> **"'A₆ is smaller' is true of the GROUP and FALSE of the OBJECT to attack."**

And the discriminating power followed the small object, not the small group: of the 14 surviving
constraints, **B₁ carries 8**.
**RULE: when choosing between targets on grounds of size, NAME THE COORDINATE and check it is the one the
proof will actually work in.** Group order, dimension, instance count and index are routinely
anti-correlated with the size of the object a proof must handle.

## §152 — A RULE IS FULLY ABSORBED WHEN IT CHANGES WHAT SOMEONE BUILDS, NOT WHAT THEY CONCLUDE
**2026-08-23, w61 r50.** §146 was written as a *diagnosis*: two "one-line proofs" of a long-open problem
turned out to be artifacts, and the tell was the SHORTNESS. **r50 used it as a PRESCRIPTION** —
> **"3 own defects, all caught by a held-out file I wrote BECAUSE §146 says a short resolution is a defect
> report."**

The extra file **failed on its first run** (1 600 + 121 + 1) and **all three defects were in the CHECK,
not in the result** — so without it, three broken checks would have silently blessed a correct theorem,
and the next round would have inherited them.
**RULE: when a result arrives unexpectedly cheaply, the correct response is to BUILD AN EXTRA
INDEPENDENT CHECK, not to re-read the proof.** Re-reading confirms; building can fail.
**And the general test of whether a rule has landed: does it change the artefacts, or only the prose?**
A rule that only ever appears in conclusions is being cited, not used.

## §153 — PROVING MORE CAN CONCENTRATE RISK INSTEAD OF SPREADING IT
Same round, reported against itself: **STEP-GAP-1 re-uses R-CLOSED as a black box, so r48's known soft
spot (the U-flat `d′=d` case) is now load-bearing for (MON) as well.**
> **(DOM-MAJ), (RH), (PIVOT-MAJ) and (MON) now ALL rest on R-CLOSED. One failure there would take four
> results with it.**

**The scoreboard improved and the risk profile got worse in the same round**, and only a line tracking its
own **dependency graph** — rather than its own count of theorems — would notice.
**RULE: after each proof, ask what the new result RESTS ON, and whether that node now carries more than
it did.** A shared lemma under four theorems is not four independent results; it is one result with four
names, and it should be reported that way.
**Practical consequence: the soft spot in a heavily-depended-on lemma is the highest-value target on the
line, ahead of any new theorem.**

## §154 — REPORTING WHAT A TEST FAILS TO CLOSE IS NECESSARY AND NOT SUFFICIENT
**2026-08-23, w133 r47 retracting r46.** §136 established that a lane closing everything has not been
shown to work, and that a lane reporting its failures has been tested. **r46's (ROW-BUDGET) reported its
failures honestly — 6.8% unclosed, nothing at all on 14 of 22 hosts — and I certified it on that basis.**
**r47: it is SUBSUMED.** Triangle-free ⟹ `a(z)=deg(z)`, so it fires only where a single vertex already
fires — **0 BUDGET-only frames in 581 441**, containment strict. **And its soundness control was FORCED.**
> **"Every test downstream of the non-firing condition is a COROLLARY; only a DIFFERENT PATH is a lane."**

**So the §136 check is a test of TESTEDNESS, not of INDEPENDENCE.** A corollary can fail informatively and
still add nothing, because its failures are the parent's failures.
**RULE: for any new test, ask BOTH — (i) what does it fail to close? and (ii) does it close anything the
existing tests do not? Measure (ii) as a set difference, not as an impression.** r47 measured it as
"BUDGET-only frames = 0" and that single number settled it.
**And note the pattern across two rounds: r46 mis-filed a corollary as a lane, and separately mis-filed a
WIN condition as "vacuous" — both errors in the direction that flattered the round making them.**
