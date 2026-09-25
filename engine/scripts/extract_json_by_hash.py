#!/usr/bin/env python3
"""Find, in the clipboard (whole ChatGPT page + open file viewer), the JSON object whose
SHA-256 (with or without trailing newline) equals the expected hash; save it in the matching form."""
import hashlib, json, subprocess, sys
exp, out = sys.argv[1], sys.argv[2]
raw = subprocess.run(['pbpaste'], capture_output=True, text=True).stdout
def balanced(s, j):
    d = 0
    for k in range(j, len(s)):
        if s[k] == '{': d += 1
        elif s[k] == '}':
            d -= 1
            if d == 0: return s[j:k+1]
starts = [i for i in range(len(raw)) if raw.startswith('{"table"', i)]
for j in starts:
    src = balanced(raw, j)
    if not src: continue
    for v in (src, src + "\n"):
        if hashlib.sha256(v.encode()).hexdigest() == exp:
            open(out, "w").write(v); print("MATCH ->", out, "| bytes", len(v)); sys.exit(0)
print("NO MATCH among", len(starts), "candidates"); sys.exit(1)
