#!/bin/bash
# Commit the PG fold through a temporary index: HEAD tree plus exactly these blobs; the shared index is not used.
set -e
cd "/c/Users/chreh/OneDrive/Documents/BRK"
R="Test Runs/_research 2026-09-25 PG"
Q="Screens/WATCHLIST RUN QUEUE.md"; RL="Screens/2026-08-31 PREPPED READING LIST (operator lists).md"; DONE="Screens/_daily/_wave7_done.txt"; AL="tools/alerts.json"; PF="PORTFOLIO.md"
OLD=$(git rev-parse HEAD)
export GIT_INDEX_FILE="$R/_tmp_index"
rm -f "$GIT_INDEX_FILE"
git read-tree "$OLD"
for pair in "$Q|q_staged.md" "$DONE|done_staged.txt" "$RL|rl_staged.md" "$AL|alerts_staged.json" "$PF|pf_staged.md"; do
  f="${pair%%|*}"; s="${pair##*|}"
  b=$(git hash-object -w --no-filters "$R/$s"); git update-index --cacheinfo "100644,$b,$f"
done
for f in fold_insert.py register_entry.md reading_fold.md portfolio_row.md check_out2.txt msg_fold.txt commit_fold.sh; do
  b=$(git hash-object -w --path="$R/$f" "$R/$f"); git update-index --add --cacheinfo "100644,$b,$R/$f"
done
T=$(git write-tree)
C=$(git commit-tree "$T" -p "$OLD" -F "$R/msg_fold.txt")
unset GIT_INDEX_FILE
rm -f "$R/_tmp_index"
git update-ref -m "commit: PG fold" refs/heads/master "$C" "$OLD"
git reset -q -- "$Q" "$DONE" "$RL" "$AL" "$PF" "$R/fold_insert.py" "$R/register_entry.md" "$R/reading_fold.md" "$R/portfolio_row.md" "$R/check_out2.txt" "$R/msg_fold.txt" "$R/commit_fold.sh"
git log --oneline -1
git show --stat HEAD | tail -14
