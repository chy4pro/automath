#!/bin/bash
# Fetch the latest sidon30-lean GitHub Actions run: status + Build-step errors (with context) + failed-step tail → lean/sidon30/CI_LOG.md
export GH_TOKEN=$(cat /wb/creds/github-token/value)
R=chy4pro/automath
id=$(gh run list --repo $R --workflow sidon30-lean --limit 1 --json databaseId -q '.[0].databaseId')
st=$(gh run view $id --repo $R --json status,conclusion,headSha,createdAt -q '"\(.status) \(.conclusion) \(.headSha[0:7]) \(.createdAt)"')
log=$(gh run view $id --repo $R --log 2>/dev/null | grep -P "\t(Build|Axioms)\t" | cut -d$'\t' -f2- | sed -E 's/\t[0-9T:.Z-]+ /\t/')
{ echo "# sidon30 CI — latest run $id"; echo; echo "$st"; echo
  echo "## Build/Axioms errors and warnings (with context)"; echo '```'
  echo "$log" | grep -n -E -A14 "error|✖" | cut -c1-260 | head -220
  echo '```'; echo "## Summary lines"; echo '```'; echo "$log" | grep -E "Build completed|build failed|✖|error:" | cut -c1-200 | head -40; echo '```'; } > /work/lean/sidon30/CI_LOG.md
echo "$id $st"
