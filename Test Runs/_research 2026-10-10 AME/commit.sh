#!/bin/bash
# Pathspec commit of this run's two paths only, retrying while another session holds .git/index.lock.
# Usage: bash commit.sh "AME run: <question closed>"
cd "/c/Users/chreh/OneDrive/Documents/BRK" || exit 1
RUN="Test Runs/2026-10-10 Run - AME AMETEK.md"
RES="Test Runs/_research 2026-10-10 AME"
MSG="$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
for i in $(seq 1 120); do
  if [ ! -f .git/index.lock ]; then
    if git add -- "$RUN" "$RES" 2>/dev/null && git commit -q -m "$MSG" -- "$RUN" "$RES" 2>/dev/null; then
      git log --oneline -1 -- "$RUN" > "$RES/cache/last_commit.txt"
      exit 0
    fi
  fi
  sleep 1
done
echo "COMMIT FAILED" > "$RES/cache/last_commit.txt"
exit 1
