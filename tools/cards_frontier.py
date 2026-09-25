#!/usr/bin/env python3
"""Local Prove2Me-lite: list the open frontier of a card directory.

A card directory holds one Lean file per statement ("card"). Conventions (see
notes/case_intel/case_colombo_flt_2609.md section 4.2):
  * the file's leading doc comment (/-! ... -/ or /-- ... -/) is the natural-language
    description of the statement and names its source;
  * a card is OPEN while its main declaration ends in `:= by sorry` (or contains `sorry`);
  * a card DEPENDS on another card when it `import`s it (module path under the cards root);
  * a card is a LEAF when it is open and every card it imports is proved.

Usage:
  python3 tools/cards_frontier.py lean/cards/<line>          # frontier + DAG summary
  python3 tools/cards_frontier.py lean/cards/<line> --dot    # Graphviz DOT of the DAG

Exit code 0 always; the report is the product. No Lean is invoked here; proving and
kernel checks stay with `lake build` and the FinalCheck.lean of the line.
"""
import os, re, sys

DOC_RX = re.compile(r"/-[!-]?\s*(.*?)-/", re.S)
IMPORT_RX = re.compile(r"^\s*(?:public\s+)?import\s+([A-Za-z0-9_.]+)", re.M)
DECL_RX = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:public\s+)?(theorem|lemma)\s+([A-Za-z0-9_.']+)", re.M)


def read_cards(root):
    cards = {}
    for dp, _, fns in os.walk(root):
        for fn in fns:
            if not fn.endswith(".lean"):
                continue
            path = os.path.join(dp, fn)
            rel = os.path.relpath(path, root)[:-5].replace(os.sep, ".")
            src = open(path, encoding="utf-8").read()
            doc = DOC_RX.search(src)
            decls = DECL_RX.findall(src)
            cards[rel] = {
                "path": path,
                "desc": (doc.group(1).strip().split("\n")[0][:100] if doc else "(no description)"),
                "imports": IMPORT_RX.findall(src),
                "open": "sorry" in src,
                "decls": [d[1] for d in decls],
            }
    return cards


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    root = sys.argv[1]
    cards = read_cards(root)
    if not cards:
        print("no .lean cards under", root)
        return
    names = set(cards)

    def local_deps(c):
        deps = []
        for imp in cards[c]["imports"]:
            for n in names:
                if imp == n or imp.endswith("." + n):
                    deps.append(n)
        return deps

    if "--dot" in sys.argv:
        print("digraph cards {")
        for c in sorted(cards):
            print('  "%s" [shape=box,style=%s];' % (c, "dashed" if cards[c]["open"] else "solid"))
            for d in local_deps(c):
                print('  "%s" -> "%s";' % (c, d))
        print("}")
        return

    n_open = sum(1 for c in cards.values() if c["open"])
    print("cards: %d  proved: %d  open: %d" % (len(cards), len(cards) - n_open, n_open))
    leaves = [c for c in cards if cards[c]["open"] and all(not cards[d]["open"] for d in local_deps(c))]
    print("open leaves (attack these first): %d" % len(leaves))
    for c in sorted(leaves):
        print("  - %s :: %s [%s]" % (c, cards[c]["desc"], ", ".join(cards[c]["decls"]) or "no decl"))
    blocked = [c for c in cards if cards[c]["open"] and c not in leaves]
    if blocked:
        print("open but blocked on open children: %d" % len(blocked))
        for c in sorted(blocked):
            print("  - %s <- %s" % (c, ", ".join(d for d in local_deps(c) if cards[d]["open"])))
    # priority hint: number of open cards that (transitively) depend on each open leaf
    rev = {c: [] for c in cards}
    for c in cards:
        for d in local_deps(c):
            rev[d].append(c)

    def dependants(c, seen=None):
        seen = seen or set()
        for p in rev[c]:
            if p not in seen:
                seen.add(p)
                dependants(p, seen)
        return seen

    if leaves:
        print("priority (open dependants count, higher first):")
        for c in sorted(leaves, key=lambda x: -len(dependants(x))):
            print("  %3d  %s" % (len(dependants(c)), c))


if __name__ == "__main__":
    main()
