#!/bin/sh
# usage: commit.sh "message"
cd "C:/Users/chreh/OneDrive/Documents/BRK" || exit 1
R="Test Runs/2026-10-16 Run - VSEC VSE Corporation.md"; D="Test Runs/_research 2026-10-16 VSEC"
printf '%s\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\n' "$1" > "$D/_commitmsg.txt"
for i in 1 2 3 4 5 6 7 8 9 10; do
  if git add -- "$R" "$D" && git commit -q -F "$D/_commitmsg.txt" -- "$R" "$D"; then git log --oneline -1; exit 0; fi
  echo "retry $i"; sleep 30
done
exit 1
