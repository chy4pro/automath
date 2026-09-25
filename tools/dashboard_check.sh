#!/bin/sh
# dashboard_check.sh -- pre-publish check for the war-report artifact.
#
# Bought by committing the SAME defect twice in the same place: the decide-section
# header said "4 项" while the section held 5 asks, and before that "2 项" while it
# held 4. Both were caught on review, neither by a check. Doctrine 63: a named
# defect recurs until a machine enforces it -- so this is the machine.
#
# Checks: (1) the stated ask count equals the actual ask count;
#         (2) tags balance (the artifact is published as a fragment, so an unclosed
#             tag silently swallows the rest of the page);
#         (3) no stale masthead date left from a previous publish.
# Exit 1 on any failure. Run before every Artifact publish.
F="${1:-$HOME/workspace/claudecode/automath/notes/automath-dashboard-src.html}"
[ -f "$F" ] || { echo "dashboard_check: missing $F"; exit 1; }

python3 - "$F" <<'PY'
import re, sys
f = sys.argv[1]
s = open(f, encoding='utf-8').read()
bad = 0

m = re.search(r'<div class="eyebrow">需要你拍板 · (\d+) 项</div>', s)
if m:
    start = s.index('<section class="decide">')
    end = s.index('</section>', start)
    actual = s[start:end].count('<div class="ask">')
    stated = int(m.group(1))
    if stated != actual:
        print("  FAIL  ask count: header says %d, section holds %d" % (stated, actual)); bad = 1
    else:
        print("  ok    ask count: %d" % actual)
else:
    print("  ok    no decide-section header found")

for tag in ('section', 'div', 'ul', 'li', 'table', 'main'):
    o = len(re.findall(r'<%s[ >]' % tag, s)); c = len(re.findall(r'</%s>' % tag, s))
    if o != c:
        print("  FAIL  <%s> open=%d close=%d" % (tag, o, c)); bad = 1
print("  ok    tag balance" if not bad else "")

dates = re.findall(r'最后更新 ([^<]+)', s)
print("  info  masthead date: %s" % (dates[0] if dates else "NONE FOUND"))
if len(dates) > 1:
    print("  FAIL  %d masthead dates present" % len(dates)); bad = 1

sys.exit(bad)
PY
