#!/usr/bin/env python3
"""Create the private Prove2Me mission proposal for the Erdős 708 sparse-core theorem.
Idempotent-ish: stores ids in engine/out/astra_708_r16/p2m_proposal.json; rerun to re-PATCH items."""
import json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEAN = os.path.join(ROOT, "lean/proofenv/Erdos708/SparseCore.lean")
DESC = os.path.join(ROOT, "engine/out/astra_708_r16/p2m_description.md")
STATE = os.path.join(ROOT, "engine/out/astra_708_r16/p2m_proposal.json")
FIELDS = ["e76e77ab-38dd-426d-a533-0b37fb6dbabc", "55eec41b-ff24-45ad-96b6-49d7a6869286"]  # number-theory, combinatorics
SRC = "H. Chen, Explicit upper bounds for the Erdős–Surányi function g(n), v11 (2026-09-07), https://doi.org/10.5281/zenodo.22636084, Section 14, "

def api(method, path, body=None):
    args = ["python3", os.path.join(ROOT, "tools/p2m.py"), method, path]
    if body is not None:
        args += ["--json", json.dumps(body, ensure_ascii=False)]
    out = subprocess.run(args, capture_output=True, text=True).stdout
    status = int(out.split("\n", 1)[0].split()[1])
    try:
        return status, json.loads(out.split("\n", 1)[1])
    except Exception:
        return status, {"raw": out[:500]}

src = open(LEAN, encoding="utf-8").read()
def block(start_marker, end_marker):
    i = src.index(start_marker); j = src.index(end_marker, i)
    return src[i:j].rstrip()

NS = "Erdos708SparseCore"
defs_code = ("import Mathlib\n\nnamespace " + NS + "\n\nopen Finset BigOperators\n\n"
             + block("/-- A finitely supported system", "/-- **Theorem 14.1") + "\n\nend " + NS + "\n")
def thm_code(name, start, end):
    body = block(start, end)
    return "namespace " + NS + "\n\n" + body + "\n\nend " + NS
PRE = "import Mathlib\nimport Definitions.Def_" + NS + "_defs\nopen Finset BigOperators"
PRE_PLAIN = "import Mathlib\nopen Finset BigOperators"

items = [
 {"kind": "definition", "definition_name": NS + "_defs",
  "definition_title": "Atom systems, $S_0$, the mean $H$ and the hinge sums $L$, $R$ (Erdős 708)",
  "definition": defs_code,
  "natural_language_statement": ("An **atom system** is a finite set of pairs $(p,j)$ with $p$ prime and $j \\ge 1$, each carrying a real weight $\\alpha_{p,j} \\ge 0$, with $\\sum_j \\alpha_{p,j} \\le 1$ for every prime $p$. It defines\n\n$$S_0(n) = \\sum_{(p,j):\\,p^j \\mid n} \\alpha_{p,j},\\qquad H = \\sum_{(p,j)} \\frac{\\alpha_{p,j}}{p^j},$$\n\nand, for an integer $m$ and a window $\\{x+1,\\dots,x+m\\}$ of $m$ consecutive positive integers, the hinge sums\n\n$$L = \\sum_{k=1}^{m}\\bigl(S_0(k)-64\\bigr)^+,\\qquad R = \\sum_{b=x+1}^{x+m}\\bigl(S_0(b)-1\\bigr)^+ .$$\n\nThese are the objects of the sparse-core inequality of Erdős Problem 708 (Section 13–14 of the source); the definitions are reusable for any weighted prime-factor count on intervals.\n\n**Formalization Note** `AtomSystem` bundles the finite set `atoms : Finset (ℕ × ℕ)`, the weight function, primality and $j \\ge 1$ on the atoms, nonnegativity on the atoms, and the per-prime bound. `S0`, `mean`, `L`, `R` are real-valued finite sums; the window is `Finset.Icc (x+1) (x+m)`."),
  "source": SRC + "first display of Section 14 and Corollary 13.3 (atoms defined in Section 13)", "tags": ["number-theory", "combinatorics"]},
 {"kind": "theorem", "theorem_name": NS + ".sparse_core",
  "theorem_title": "Sparse-core inequality with constant $141/128$ (Erdős 708, Theorem 14.1)",
  "formal_statement": thm_code("sparse_core", "/-- **Theorem 14.1", "/-- **Lemma 14.3"),
  "natural_language_statement": ("Let $\\alpha$ be an atom system: finitely many prime powers $p^j$ ($j\\ge1$) with real weights $\\alpha_{p,j}\\ge0$ and $\\sum_j\\alpha_{p,j}\\le1$ for every prime $p$, and let $S_0(n)=\\sum_{p^j\\mid n}\\alpha_{p,j}$ and $H=\\sum\\alpha_{p,j}/p^j$. Suppose $H<17/16$. Then for every integer $m>4096$ and every $x\\ge0$,\n\n$$\\frac{141}{128}\\sum_{k=1}^{m}\\bigl(S_0(k)-64\\bigr)^+\\ \\le\\ \\sum_{b=x+1}^{x+m}\\bigl(S_0(b)-1\\bigr)^+ .$$\n\nThis is the sparse-core inequality of Erdős Problem 708 in the strengthened form of the source; with the reduction already in the source it yields the threshold-65 hinge inequality for all weights and the linear bound $g(n)\\le81n$ for all $n$.\n\n**Formalization Note** The support restriction $p^j\\le m/64$ of the source's Corollary 13.3 is not imposed, since the source proves the statement without it. The window consists of positive integers because $x\\in\\mathbb N$."),
  "preamble": PRE, "source": SRC + "Theorem 14.1 (signed certificate)", "tags": ["number-theory", "combinatorics"]},
 {"kind": "theorem", "theorem_name": NS + ".hinge_le_esymm",
  "theorem_title": "Hinge inequality: $(\\sum x_i - C)^+ \\le e_{C+1}(x)$ on $[0,1]^N$ (Lemma 14.3)",
  "formal_statement": thm_code("hinge_le_esymm", "/-- **Lemma 14.3", "/-- **Lemma 14.4"),
  "natural_language_statement": ("Let $s$ be a finite index set, $x_i\\in[0,1]$ for $i\\in s$, and $C\\ge0$ an integer. Then\n\n$$\\Bigl(\\sum_{i\\in s}x_i - C\\Bigr)^+\\ \\le\\ e_{C+1}(x) := \\sum_{T\\subseteq s,\\ |T|=C+1}\\ \\prod_{i\\in T}x_i .$$\n\nThe elementary symmetric polynomial bounds the positive part of the excess of the sum over $C$. It is the hinge-moment inequality used to charge the excess mass of a hot integer to products of its atoms.\n\n**Formalization Note** $e_{C+1}$ is written as a sum over `s.powersetCard (C+1)`; for $|s|<C+1$ the right side is $0$ and the left side is $0$ as well."),
  "preamble": PRE_PLAIN, "source": SRC + "Lemma 14.3 (hinge)", "tags": ["combinatorics", "inequalities"]},
 {"kind": "theorem", "theorem_name": NS + ".moment_bound",
  "theorem_title": "Factorial-moment bound $\\sum_{j\\le N} e_r(b(j)) \\le N H^r/r!$ (Lemma 14.4)",
  "formal_statement": thm_code("moment_bound", "/-- **Lemma 14.4", "/-- **Lemma 14.8"),
  "natural_language_statement": ("Let $P$ be a finite set of primes. For each $p\\in P$ let a finite set of **levels** $(q,\\mathrm{inc})$ be given, where $q=p^e$ with $e\\ge1$ and $\\mathrm{inc}\\ge0$ is a real increment, and put\n\n$$b_p(j)=\\sum_{(q,\\mathrm{inc})\\text{ at }p,\\ q\\mid j}\\mathrm{inc},\\qquad H_B=\\sum_{p\\in P}\\ \\sum_{(q,\\mathrm{inc})\\text{ at }p}\\frac{\\mathrm{inc}}{q}.$$\n\nThen for all integers $N,r\\ge1$,\n\n$$\\sum_{j=1}^{N} e_r\\bigl((b_p(j))_{p\\in P}\\bigr)\\ \\le\\ N\\,\\frac{H_B^{\\,r}}{r!},$$\n\nwhere $e_r$ is the $r$-th elementary symmetric polynomial of the $|P|$ numbers $b_p(j)$. The proof expands $e_r$ into one level per prime and uses that powers of distinct primes are coprime, so that the number of $j\\le N$ divisible by their product is at most $N$ divided by the product.\n\n**Formalization Note** Levels at a prime are a `Finset (ℕ × ℝ)`; $e_r$ is a sum over `P.powersetCard r` of products."),
  "preamble": PRE_PLAIN, "source": SRC + "Lemma 14.4 (moment bound)", "tags": ["number-theory", "combinatorics"]},
 {"kind": "theorem", "theorem_name": NS + ".numerical_bound",
  "theorem_title": "Uniform numerical bound $t^{12t}H^{12t+1}2^{23t}/(12t+1)! \\le 17/416$ (Lemma 14.8)",
  "formal_statement": thm_code("numerical_bound", "/-- **Lemma 14.8", "end " + NS),
  "natural_language_statement": ("For every integer $t\\ge1$ and every real $H$ with $0\\le H\\le17/16$,\n\n$$\\frac{t^{12t}\\,H^{12t+1}\\,2^{23t}}{(12t+1)!}\\ \\le\\ \\frac{17}{416}.$$\n\nThis is the constant that makes the pointwise feasibility of the signed certificate close: it bounds $\\varepsilon(\\theta)2^{23/\\theta}/\\theta$ with $\\theta=1/t$ uniformly in $t$. The source proves it from $(12t)!\\ge(12t/e)^{12t}$, $e<11/4$ and the exact inequality $2^{23}(187/768)^{12}<1/2$.\n\n**Formalization Note** All quantities are real numbers; the factorial is `Nat.factorial (12*t+1)` cast to $\\mathbb R$."),
  "preamble": PRE_PLAIN, "source": SRC + "Lemma 14.8 (a uniform numerical bound)", "tags": ["number-theory", "inequalities"]},
]

state = json.load(open(STATE)) if os.path.exists(STATE) else {}
if "proposal_id" not in state:
    st, r = api("post", "/mission-proposals", {"name": "Erdős 708: the sparse-core inequality (signed clipped-prefix certificate)",
        "description": open(DESC, encoding="utf-8").read(), "mission_type": "ResearchPaper", "field_ids": FIELDS, "visibility": "private"})
    print("create proposal:", st, (r.get("id") or r)); 
    if st != 201: sys.exit(1)
    state["proposal_id"] = r["id"]; state["items"] = {}
    json.dump(state, open(STATE, "w"), indent=1)
pid = state["proposal_id"]
for it in items:
    key = it.get("theorem_name") or it.get("definition_name")
    if key in state["items"]:
        st, r = api("patch", f"/mission-proposals/{pid}/items/{state['items'][key]}", {k: v for k, v in it.items() if k != "kind"})
        print("patch", key, st, r.get("id") or str(r)[:200])
    else:
        st, r = api("post", f"/mission-proposals/{pid}/items", it)
        print("post", key, st, r.get("id") or str(r)[:300])
        if st == 201: state["items"][key] = r["id"]; json.dump(state, open(STATE, "w"), indent=1)
order = [state["items"][k] for k in [NS + "_defs", NS + ".hinge_le_esymm", NS + ".moment_bound", NS + ".numerical_bound", NS + ".sparse_core"] if k in state["items"]]
st, r = api("patch", f"/mission-proposals/{pid}", {"main_item_id": state["items"].get(NS + ".sparse_core"), "item_order": order})
print("metadata:", st, r.get("status") or str(r)[:200])
ms = [(NS + ".hinge_le_esymm", "Lemma 14.3 — hinge inequality for elementary symmetric polynomials", "Self-contained: for $x_i\\in[0,1]$ and an integer $C\\ge0$, $(\\sum x_i-C)^+\\le e_{C+1}(x)$. Needed to charge the excess of a hot integer to products of its atoms (Lemma 14.5 of the source). No number theory involved; a finite pair-compression argument or induction on the number of fractional coordinates."),
      (NS + ".moment_bound", "Lemma 14.4 — factorial-moment bound for coprime prime-power levels", "Self-contained: $\\sum_{j\\le N}e_r((b_p(j))_p)\\le N H_B^r/r!$. Expand $e_r$ into one level per prime, use coprimality of powers of distinct primes and $\\lfloor N/d\\rfloor\\le N/d$, then $r!\\,e_r(h)\\le(\\sum h)^r$."),
      (NS + ".numerical_bound", "Lemma 14.8 — the uniform constant $17/416$", "Pure real arithmetic: $(12t)!\\ge(12t/e)^{12t}$, $e<11/4$, and the exact rational inequality $2^{23}(187/768)^{12}<1/2$ give $G\\le 17/(16(12t+1)2^t)\\le17/416$.")]
for key, title, desc in ms:
    if key in state["items"]:
        st, r = api("post", f"/mission-proposals/{pid}/milestones", {"item_id": state["items"][key], "milestone_title": title, "milestone_description": desc})
        print("milestone", key, st, r.get("sort_order") if isinstance(r, dict) else r)
print("PROPOSAL", pid)
