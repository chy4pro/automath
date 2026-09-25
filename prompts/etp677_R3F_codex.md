# R3-F: the all-affine conjecture — full classification at order 11 (and 13)

Read prompts/etp677_R3_common.md first (toolkit incl. 08-16 14:10 corrections
+ blocked routes). No internet. Do not read problems/etp677/ reports.

MOTIVATION: every finite 677-magma found so far is AFFINE over an abelian
group (x*y = Fx+Gy+c with P(G)=0, F=(G+G³)^{-1}). If ALL finite 677-magmas
are affine, the finite implication 677⟹255 follows immediately (affine
models provably satisfy E255). So the "all-affine conjecture" is a
completion route independent of the blocked ones.

TASKS:
1. FULL enumeration of 677-magmas of order 11 up to isomorphism. Engineering:
   left-division representation (each row a permutation), KEY as the row
   constraint P_u(P_p(q)) = y for p=P_y(u), q=P_y(p); symmetry-break by
   canonicalizing row 0 (its cycle type + relabeling; the toolkit's m(y)
   cycle facts prune). Compare the census against the affine count (expect:
   only affine classes if the conjecture holds). Write an efficient C or
   optimized python solver; run with checkpoints; report exact coverage
   honestly if time runs short (order 11 full may be big — prioritize
   completeness of the search-space accounting over reaching 13).
2. MEDIALITY test: check whether (a*b)*(c*d) = (a*c)*(b*d) holds in all
   known models (construct: Z5 dihedral, both order-7, F9 model a=1,b=t+2,
   F16 model (1+z)x+zy) — if all medial, attempt an equational derivation
   of mediality from E677 + left-quasigroup (bounded saturation; note
   B1 blocks E255-derivation but mediality might be derivable!). If E677 ⟹
   medial (even just finitely), the classification literature for medial
   left quasigroups could finish everything.
3. If a NON-AFFINE model appears at order 11: analyze it completely
   (E255 status, Latin?, quandle?, automorphisms) — top priority finding.

Report to problems/etp677/R3F_codex_report.md with full search-space
accounting. This is a long compute task — use background terminals with
checkpoints, poll them, stay honest about coverage.
