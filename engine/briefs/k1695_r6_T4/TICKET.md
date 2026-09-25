# TICKET K6-T4 — (T_3): finish the Case-A support-3 stratum and attack Case B; build a real Gröbner engine

Continue `engine/harvest/k1695_r6_T3/` (read its REPORT.md, ideals/, sympy_groebner.py, run_capped.py).
Output to `engine/harvest/k1695_r6_T4/` (create): `REPORT.md` ending with `DONE-K6T4`, every ideal,
basis, log. Exact arithmetic. Caps per computation: 40 min wall, 8 GB (the T3 watchdog); sequential.

## Tooling (allowed this time)
You MAY download and build, INTO `~/.local` only (never system dirs, no Homebrew): autoconf/automake/
libtool (from ftp.gnu.org), GMP, MPFR, FLINT (flintlib.org / GitHub releases), then msolve
(https://github.com/algebraic-solving/msolve). Log every command and every failure verbatim. If the
toolchain build fails, try the alternative: `pip install --target ~/.local/pyflint python-flint` is
NOT a Gröbner engine — do not waste time on it; instead reduce the problem (below) so that sympy
finishes. Verify any engine on the two toy ideals (⟨x²,y²,1−txy⟩ → [1]; ⟨xy,1−tx⟩ → not [1]).

## Mathematics to reduce the size
1. Case A, support 3: β = (b₁, b₂, 0), b₁b₂ ≠ 0, C ∈ GL₃ (12 vars incl. t). Symmetries that preserve
   the STATEMENT (not the individual generators): row permutations of R (act on C by row permutation),
   permutations among the columns e₁, e₂ (with β's coordinates), and — check this carefully — scaling?
   (No: scaling changes the problem.) Use them to fix a normal form for C (e.g. a nonzero entry in a
   fixed position after row permutation is not enough; think about what can be normalised by the
   permutations alone). Alternatively split the stratum by the support pattern of C's first column,
   giving several smaller ideals. Run each over GF(2) first (the hard one), then ℚ, GF(3), GF(5), GF(7).
2. Case B: all κ_j ≠ 0. Do NOT normalise β₁ = 1 (T3 §2 showed it is illegitimate). Consider instead the
   equivalent formulation "for every C ∈ GL₃ and every β with all b_j ≠ 0, one of the 24 cubics
   det[v_j, B C v_j, B C B C v_j] is nonzero" and try to find a SMALL sufficient sub-family of the 24
   (e.g. the six with j = 4, which are det[β, P C β, P C P C β] for P ∈ S₃) whose ideal is already the
   unit ideal after saturation — test by Gröbner with fewer generators first (cheaper to compute and
   if [1] it proves the full statement); if not [1], describe the variety it leaves and add generators.
3. Report the exact certified (stratum, characteristic) table like T3's, with the new tool's name
   and version; state what remains uncovered. End with `DONE-K6T4`.
