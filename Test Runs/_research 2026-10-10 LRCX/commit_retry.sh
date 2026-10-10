#!/bin/sh
# Pathspec commit with lock retry (brief: wait 30s, retry up to ten times, never delete a lock).
# usage: sh commit_retry.sh "<message>"
RUN="Test Runs/2026-10-10 Run - LRCX Lam Research.md"; RES="Test Runs/_research 2026-10-10 LRCX"
for i in 1 2 3 4 5 6 7 8 9 10; do
  if git add -- "$RUN" "$RES" && git commit -q -m "$1" -- "$RUN" "$RES"; then
    echo "COMMITTED on try $i: $(git log --oneline -1 -- "$RUN")"; exit 0
  fi
  echo "try $i failed (lock?), waiting 30s"; sleep 30
done
echo "GAVE UP after 10 tries"; exit 1
