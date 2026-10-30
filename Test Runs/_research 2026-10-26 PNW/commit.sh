#!/bin/sh
# usage: sh commit.sh "<question closed>"   (pathspec of this run's two paths only; waits on a lock, never deletes it)
cd /c/Projects/BRK || exit 1
R="Test Runs/2026-10-26 Run - PNW Pinnacle West.md"; F="Test Runs/_research 2026-10-26 PNW"
for i in 1 2 3 4 5 6 7 8 9 10; do
  if git add -- "$R" "$F" && git commit -q -m "PNW run: $1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- "$R" "$F"; then git log --oneline -1; exit 0; fi
  echo "commit failed (attempt $i), waiting 30s"; sleep 30
done
echo "LOCK OUTLIVED TEN TRIES"; exit 1
