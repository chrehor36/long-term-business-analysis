#!/bin/sh
# usage: sh commit_paths.sh <msgfile> ; commits the run file, this folder's scripts, drafts and outputs, plus any extra paths given
cd "C:/Users/chreh/OneDrive/Documents/BRK"
R="Test Runs/_research 2026-09-19 BIRD"
MSG="$1"; shift
P="Test Runs/2026-09-19 Run - BIRD Allbirds.md"
FILES=$(ls "$R"/*.py "$R"/_*.md "$R"/*_out.txt "$R"/_probe_screen_output.txt "$R"/filings_list.txt "$R"/commit_paths.sh 2>/dev/null)
IFS='
'
git add -- "$P" $FILES "$@"
git commit -q -F "$MSG" -- "$P" $FILES "$@" && git log --oneline -1 && git show --stat --format= HEAD | tail -3
