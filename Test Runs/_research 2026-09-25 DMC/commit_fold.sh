#!/bin/bash
# Commit the fold through a temporary index: HEAD tree plus exactly these blobs. The shared index is not used,
# so nothing another session has staged can enter this commit; afterwards the shared index is reset for these
# paths only, so the CRM hunks stay unstaged in the working tree.
set -e
cd "/c/Users/chreh/OneDrive/Documents/BRK"
R="Test Runs/_research 2026-09-25 DMC"
Q="Screens/WATCHLIST RUN QUEUE.md"; RL="Screens/2026-08-31 PREPPED READING LIST (operator lists).md"; DONE="Screens/_daily/_wave7_done.txt"
OLD=$(git rev-parse HEAD)
export GIT_INDEX_FILE="$R/_tmp_index"
rm -f "$GIT_INDEX_FILE"
git read-tree "$OLD"
bq=$(git hash-object -w --no-filters "$R/q_staged.md")
bd=$(git hash-object -w --no-filters "$R/done_staged.txt")
br=$(git hash-object -w --no-filters "$R/rl_staged.md")
git update-index --cacheinfo "100644,$bq,$Q"
git update-index --cacheinfo "100644,$bd,$DONE"
git update-index --cacheinfo "100644,$br,$RL"
for f in fold_insert.py register_entry.md reading_fold.md check_out.txt check_out2.txt msg_fold.txt commit_fold.sh; do
  b=$(git hash-object -w --path="$R/$f" "$R/$f")
  git update-index --add --cacheinfo "100644,$b,$R/$f"
done
T=$(git write-tree)
C=$(git commit-tree "$T" -p "$OLD" -F "$R/msg_fold.txt")
unset GIT_INDEX_FILE
rm -f "$R/_tmp_index"
git update-ref -m "commit: DMC fold" refs/heads/master "$C" "$OLD"
git reset -q -- "$Q" "$DONE" "$RL" "$R/fold_insert.py" "$R/register_entry.md" "$R/reading_fold.md" "$R/check_out.txt" "$R/check_out2.txt" "$R/msg_fold.txt" "$R/commit_fold.sh"
git log --oneline -1
git show --stat HEAD | tail -12
