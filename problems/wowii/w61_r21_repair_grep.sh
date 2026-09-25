#!/bin/zsh
# owner-w61 ROUND 21 CLOSING GREP -- run AFTER 7.36 is appended (RW61-4 as amended)
cd $HOME/workspace/claudecode/automath
D=notes/proofs/wowii61_draft.md
B=prompts/w61_S3_GFAN_r20.md
P=problems/wowii/w61_r20_q37_dispatch.md
echo "=== owner-w61 ROUND 21 CLOSING GREP -- run AFTER 7.36 was appended (RW61-4 as amended) ==="
date
echo
printf 'draft: %-40s %8s bytes / %8s lines\n' "$D" "$(wc -c < $D | tr -d ' ')" "$(wc -l < $D | tr -d ' ')"
printf 'brief: %-40s %8s bytes   md5=%s\n' "$B" "$(wc -c < $B | tr -d ' ')" "$(md5 -q $B)"
printf '       sha256=%s\n' "$(shasum -a 256 $B | awk '{print $1}')"
echo
echo "--- [1] dispatched brief IDENTITY is unchanged by this round (md5 and sha must match r20) ---"
echo "  md5 must be 6fc6cc062028496e36661fbef66907d3 : $(md5 -q $B)"
echo "  sha must be 1dde17a46a1c855798c9bbfaab207962d102987eb4c7176568016ade432cdbe3"
echo "           is $(shasum -a 256 $B | awk '{print $1}')"
echo
echo "--- [2] r18 base brief UNTOUCHED (family-1 lineage; md5 must be 3a2c17cb1a3a45cd741ae63cad35de3f) ---"
echo "  r18 md5 : $(md5 -q prompts/w61_S3_GFAN_r18.md)"
echo
echo "--- [3] the STALE dispatch identity table is repaired (each must be as annotated) ---"
echo "  '95 414' bare, unannotated, in dispatch record : $(grep -c '95 414' $P)  (expect 1, inside the CORRECTED cell)"
echo "  '6fc6cc06' present in dispatch identity table  : $(grep -c '6fc6cc062028496e36661fbef66907d3' $P)"
echo "  'CORRECTED r21' markers                        : $(grep -c 'CORRECTED r21' $P)"
echo "  dispatch record self-consistent on bytes       : $(grep -c '102 422' $P)"
echo
echo "--- [4] held-out answers still absent from the dispatched brief (each must be ZERO) ---"
for v in 98384 "98 384" 791 131 1002 "1 002" "s0(\[12+6+4\])"; do
  printf '  %-12s : %s\n' "$v" "$(grep -c -- "$v" $B)"
done
echo
echo "--- [5] the EXECUTION-ENVIRONMENT template lines are OURS, not a judge claim (both must be >=1 in the BRIEF) ---"
grep -n 'EXECUTION ENVIRONMENT: I ran code' $B | head -3
grep -n 'EXECUTION ENVIRONMENT: I did NOT run code' $B | head -3
echo "  'Python 3' anywhere in the brief (must be ZERO -- the runtime token in the r20 title signal is NOT ours) : $(grep -c 'Python 3' $B)"
echo
echo "--- [6] 7.36 present and last section of the draft ---"
grep -n '^## §7\.3[4-9]' $D
echo
echo "--- [7] AC4 class sweep: '480' in the DISPATCHED brief (must be ZERO) ---"
grep -c '480' $B
echo
echo "--- [8] duplicated '(C-8)' heading in the dispatched brief (must be 1) ---"
grep -c '^\*\*(C-8)' $B
echo
echo "--- [9] no per-message attribution claim is written anywhere in the draft (must be ZERO) ---"
echo "  'per-message attribution established' : $(grep -c 'per-message attribution established' $D)"
echo "  'Gemini has no A/B'                   : $(grep -c 'Gemini has no A/B' $D)"
echo "  'no A/B feature'                      : $(grep -c 'no A/B feature' $D)"
echo
echo "--- [10] the RULING AC strength sentence is present VERBATIM in 7.36 (must be >=1) ---"
grep -c 'single response observed; session-level mode verified at both ends; per-message' $D
echo
echo "--- [11] the harvest artifact exists and carries its provenance digest ---"
H=problems/wowii/w61_S3_GFAN_r20_gemini_Q37.md
echo "  bytes : $(wc -c < $H | tr -d ' ')"
echo "  in-page sha recorded in the file : $(grep -c 'f4965d68053fce5d6b6f2c10d4010a035bcc925e4cc90c3820e78f71a1795916' $H)"
echo "  same sha recorded in the draft    : $(grep -c 'f4965d68053fce5d6b6f2c10d4010a035bcc925e4cc90c3820e78f71a1795916' $D)"
echo "  fidelity caveat present (NOT byte-verified) : $(grep -c 'Byte-identity against the page was NOT' $H)"
echo
echo "--- [12] the judge's non-held-out figures ARE in the brief (each must be >=1) ---"
echo "  '77 373' in brief : $(grep -c '77 373' $B)"
echo "  '427'    in brief : $(grep -c '427' $B)"
echo
echo "--- [13] no held-out ANSWER leaked into the brief, re-checked after the harvest (each ZERO) ---"
for v in 98384 791 131; do printf '  %-8s : %s\n' "$v" "$(grep -c -- "$v" $B)"; done
echo
echo "--- [14] 7.36 does NOT claim the r20 title signal was a hit (must be >=1 for the retirement wording) ---"
echo "  'is not being scored as a hit' : $(grep -c 'not being scored as a hit' $D)"
echo
echo "--- [15] OPS-11 is registered once and does not collide ---"
echo "  OPS-11 headings in web_model_ops : $(grep -c '^## OPS-11' notes/web_model_ops.md)"
echo "  OPS-10 headings in web_model_ops : $(grep -c '^## OPS-10' notes/web_model_ops.md)"
