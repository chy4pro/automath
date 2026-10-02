#!/bin/bash
# Self-service CI fetch (curl only): waits for the latest sidon30-lean run to finish (optional), writes lean/sidon30/CI_LOG.md.
# Usage: tools/sidon30_ci.sh [--wait]
set -uo pipefail
TOK=$(cat /wb/creds/github-token/value) || exit 2
API=https://api.github.com/repos/chy4pro/automath
H=(-s -H "Authorization: Bearer $TOK" -H "Accept: application/vnd.github+json")
get(){ curl "${H[@]}" "$1"; }
field(){ grep -o "\"$1\": *[^,}]*" | head -1 | sed -E 's/^"[^"]*": *//; s/^"//; s/"$//'; }
while :; do
  run=$(get "$API/actions/workflows/sidon30-lean.yml/runs?per_page=1")
  id=$(echo "$run" | grep -o '"id": *[0-9]*' | head -1 | grep -o '[0-9]*$')
  status=$(echo "$run" | field status); concl=$(echo "$run" | field conclusion); sha=$(echo "$run" | field head_sha | cut -c1-7)
  [ "${1:-}" = "--wait" ] && [ "$status" != "completed" ] && { sleep 30; continue; }
  break
done
job=$(get "$API/actions/runs/$id/jobs" | grep -o '"id": *[0-9]*' | head -1 | grep -o '[0-9]*$')
log=$(curl "${H[@]}" -L "$API/actions/jobs/$job/logs" | sed -E 's/^[0-9T:.Z-]+ //')
{ echo "# sidon30 CI — run $id  ($status / $concl, commit $sha)"; echo
  echo "## Errors and warnings with context"; echo '```'
  echo "$log" | grep -n -E -A14 "error:|✖|sorry|declaration uses" | cut -c1-260 | head -260
  echo '```'; echo "## Summary"; echo '```'
  echo "$log" | grep -E "Build completed|build failed|✖|error:|depends on axioms|does not depend on any axioms" | cut -c1-220 | head -60; echo '```'; } > /work/lean/sidon30/CI_LOG.md
echo "$id $status $concl $sha"
