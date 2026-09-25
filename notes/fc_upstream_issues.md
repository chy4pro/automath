# formal-conjectures 上游 mis-formalization 发现（2026-08-16）

按"不改上游、发现即上报"原则记录，待用户确认后提 GitHub issue。

## Issue 1: OEIS/109074.lean — b 定义错误 + 移位错误（陈述在 n=1 可反驳）

- 文件把 A005156 定义成 `b n = (3n).choose n / (2n+1)`，这其实是 A001764
  （三叉树数：1,1,3,12,55,...），不是 A005156（垂直对称 ASM 数：1,1,3,26,646,...；
  Robbins 猜想、Kuperberg 证明的乘积公式）。
- 且 OEIS 猜想的正确移位是 frac(n) = A005156(n)/A005156(n-1)（数值验证
  frac(2)=3=A(2)/A(1)、frac(3)=26/3=A(3)/A(2)），而文件写 b(n+1)/b(n)。
- 现陈述可在 n=1 直接反驳：frac(1)=1，b(2)/b(1)=3/1=3。
- 数学注记：给定 Kuperberg 积公式 A(n) = Π_{k≤n} (6k-2)!(2k-1)!/((4k-1)!(4k-2)!)/2^k
  （形式随 OEIS Maple 代码），A(n)/A(n-1) = (6n-2)!(2n-1)!/(2(4n-1)!(4n-2)!) =
  C(6n-2,2n)/(2C(4n-1,2n)) = frac(n) 是平凡阶乘恒等式——原 OEIS 猜想的实质
  即 Kuperberg 定理。

## Issue 2: OEIS/100434.lean — b 定义符号错误（三条猜想在 n=0 全部可反驳）

- 文件定义 `b n = if n%2=0 then c (n+1) else c (n-1)`。按此定义
  conjecture1/2/3 在 n=0 反例：c(0)+d(0)=3 但 b(0)=c(1)=-3。
- 正确定义应为偶数分支取负：b(2n) = -c(2n+1)（与文件内已证的
  textbook 定理 a(2n) = -c(2n+1) 一致）。修正后三条恒等式数值验证
  n<600 全部成立，且可由双步归纳机械证明（我方已在 proofenv 施工）。

## 处理状态
- [ ] 用户确认后提 issue（或直接 PR 修 def + 附证明）
- [x] 修正版三条恒等式 Lean 证明进行中（lean/proofenv/A100434.lean）

## Issue 素材 #3：A211417 general_divisibility 陈述空洞（2026-08-17 发现）
FormalConjectures/OEIS/211417.lean 的 general_divisibility 只要求 ∃ D : ℤ，
未排除 D=0——而任何数整除 0，取 D=0 即字面为真，命题空洞。建议上游改为
∃ D > 0（或 D ≠ 0）。发现自我方一般情形证明的查重工作（notes/proofs/
a211417_v1.md §7.1）；KitaKen1 在 issue #4923 亦有相关观察。待 GitHub 登录后
与 #1(109074)/#2(100434) 一并提交。
