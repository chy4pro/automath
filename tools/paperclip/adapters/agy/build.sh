#!/bin/sh
# Build the external agy_local adapter (Antigravity CLI) for Paperclip from source and stage it where Paperclip
# loads it. Source: github.com/evgemar/agy-paperclip-adapter (MIT) at a pinned commit, plus remote-bridge.patch
# (workspace sync + Paperclip callback bridge on ssh targets, ported from claude_local and community PR #14938;
# the session codec keeps remoteExecution, cf. upstream #12930).
# Compiled against the installed, patched @paperclipai/adapter-utils (symlinked, so our ssh patches apply).
# Then: first time  POST /api/adapters/install {"packageName": "$T", "isLocalPath": true}
#       afterwards  POST /api/adapters/agy_local/reload
set -e
COMMIT=d18cae49a6c7d22ca2f31fc41243fc3af2c1d935
T=/work/.paperclip/adapters/agy-paperclip-adapter
AU=/work/.tools/npm/lib/node_modules/paperclipai/node_modules/@paperclipai/adapter-utils
W=$(mktemp -d)
git clone -q https://github.com/evgemar/agy-paperclip-adapter.git "$W/src" && cd "$W/src" && git checkout -q "$COMMIT"
git apply "$(dirname "$(readlink -f "$0")")/remote-bridge.patch"
npm install --no-save --ignore-scripts --no-audit --no-fund typescript@5 @types/node@24 >/dev/null
rm -rf node_modules/@paperclipai && mkdir -p node_modules/@paperclipai && ln -s "$AU" node_modules/@paperclipai/adapter-utils
npx tsc -p . || true   # two known type-only errors (modelProfiles) against adapter-utils 2026.1005.0; JS is emitted
node --test "test/**/*.test.js"
rm -rf "$T"; mkdir -p "$T/node_modules/@paperclipai"
cp -r package.json dist ui-parser.cjs README.md LICENSE "$T/"; ln -s "$AU" "$T/node_modules/@paperclipai/adapter-utils"
echo "$COMMIT + remote-bridge.patch" > "$T/SOURCE_COMMIT"; echo https://github.com/evgemar/agy-paperclip-adapter > "$T/SOURCE_REPO"
rm -rf "$W"; echo "staged $T"
