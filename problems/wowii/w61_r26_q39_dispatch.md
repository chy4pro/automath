# Q39 — owner-w61 round 26 dispatch

Read `prompts/w61_S3_GFAN_r26.md` and execute the review it specifies, in full and to its
own report contract. It names its own output paths; use exactly those:

* report  -> `problems/wowii/w61_S3_GFAN_r26.md`
* scripts -> `problems/wowii/w61_S3_GFAN_r26_check.py`
* raw stdout (not a summary) -> `problems/wowii/w61_S3_GFAN_r26_check.out`

Do Section 0 first and print your calibration before any Section 0 value, as the brief
requires. Print the verdict line to the terminal as well.

## One addition to the brief's report contract, and it is the reason this round exists

Appendix A.1 of this brief claims to state, in full, **every** fact the proofs reach
outside themselves for, and it prints an eighteen-name list you are invited to grade us
on. A previous version of that same claim was **false**, and the brief says so in its own
words near the top.

So, as a separate numbered section of your report, headed **IMPORT INTERFACE ROLL CALL**:

1. Walk the eighteen names on that list. For each one, say whether a **statement** — not
   merely the name — is present in this file, and where.
2. For the target, **Corollary GFANν-HC**, list every fact its proof reaches outside
   itself for, and for each say whether its interface is checkable **from this file
   alone**: hypothesis required vs hypothesis supplied, conclusion proved vs conclusion
   used. Name any import whose interface you cannot check, and say what is missing.
3. The bracket after that proof commits to a **count** of the imports it guards. Check
   the count as well as the clauses. If the count is wrong in either direction, that is a
   defect of the bracket and we want it reported as one.

If the answer to any part of this is "still not supplied", say so plainly. A report that
tells us the repair did not work is worth more to us than one that tells us it did.
