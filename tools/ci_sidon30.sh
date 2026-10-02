#!/bin/bash
# Fetch the latest sidon30-lean GitHub Actions run status and the failing log tail into lean/sidon30/CI_LOG.md
export GH_TOKEN=$(cat /wb/creds/github-token/value)
R=chy4pro/automath
id=$(gh run list --repo $R --workflow sidon30-lean --limit 1 --json databaseId -q '.[0].databaseId')
st=$(gh run view $id --repo $R --json status,conclusion,headSha,createdAt -q '"\(.status) \(.conclusion) \(.headSha[0:7]) \(.createdAt)"')
{ echo "# sidon30 CI — latest run $id"; echo; echo "$st"; echo; echo '```'; gh run view $id --repo $R --log-failed 2>/dev/null | tail -150 | cut -c1-240; echo '```'; } > /work/lean/sidon30/CI_LOG.md
echo "$id $st"
