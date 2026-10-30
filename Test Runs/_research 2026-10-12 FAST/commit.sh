#!/bin/sh
# usage: commit.sh "message"   (pathspec commit of the run file and research folder only; retries on a git lock)
cd "/c/Users/chreh/OneDrive/Documents/BRK" || exit 1
F="Test Runs/2026-10-12 Run - FAST Fastenal.md"; R="Test Runs/_research 2026-10-12 FAST"
i=0
while [ $i -lt 10 ]; do
  if git add -- "$F" "$R" 2>/tmp/fastgit.err && git commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- "$F" "$R" 2>>/tmp/fastgit.err; then git log --oneline -1; exit 0; fi
  if grep -q "\.lock" /tmp/fastgit.err; then echo "lock, retry $i"; sleep 30; i=$((i+1)); else cat /tmp/fastgit.err; exit 1; fi
done
echo "LOCK OUTLIVED TEN TRIES"; exit 2
