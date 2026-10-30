#!/usr/bin/env bash
# ping_at.sh -- local timer. Sleeps until a target epoch, then exits, which
# re-invokes the Claude Code session (launch with Bash run_in_background:true).
#
# Usage:  ping_at.sh <target_epoch_seconds> ["reason string"]
# Example: ping_at.sh $(date -d "+3 hours" +%s) "resume BT-15 pipeline"
#
# Preferred over cloud/remote schedulers: all project data (SEC XBRL facts
# cache, price cache, dgs30.csv, screen outputs) is local-only and the repo
# has no git remote, so remote runners cannot do this work.

TARGET="${1:?usage: ping_at.sh <target_epoch> [reason]}"
REASON="${2:-scheduled resume}"

NOW=$(date +%s)
WAIT=$(( TARGET - NOW ))

if [ "$WAIT" -lt 0 ]; then
  echo "TIMER ERROR: target $(date -d "@$TARGET" '+%Y-%m-%d %H:%M:%S %Z') is in the past."
  exit 1
fi

echo "TIMER ARMED: will fire at $(date -d "@$TARGET" '+%Y-%m-%d %H:%M:%S %Z') (${WAIT}s from now)"
echo "REASON: $REASON"

sleep "$WAIT"

echo "=========================================================="
echo "TIMER FIRED at $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo "REASON: $REASON"
echo "Resume the task described above. Full state is in memory:"
echo "  MEMORY.md -> brk-backtest-program.md (BT-15 resume steps)"
echo "=========================================================="
