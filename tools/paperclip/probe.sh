#!/bin/sh
echo "PROBE id=$(id) arch=$(uname -m) home=$HOME user=$(whoami 2>/dev/null)"
echo "PROBE os=$(cat /etc/os-release | head -1)"
echo "PROBE node=$(command -v node) $(node -v 2>/dev/null) npm=$(command -v npm) python3=$(command -v python3) git=$(command -v git) curl=$(command -v curl)"
echo "PROBE mem=$(free -m | awk '/Mem/ {print $2" total "$7" avail"}') cpus=$(nproc)"
echo "PROBE work=$(ls -d /work/.tools 2>&1) writable=$(touch /work/.tools/.probe && echo yes || echo no)"
echo "PROBE claude=$(command -v claude) codex=$(command -v codex)"
echo "PROBE env PATH=$PATH"
exec sleep infinity
