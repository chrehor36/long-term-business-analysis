#!/bin/bash
# usage: commit.sh msgfile path...
cd "/c/Users/chreh/OneDrive/Documents/BRK"
msg="$1"; shift
git add -- "$@" 2>&1 | grep -v "^warning" 
git commit -q -F "$msg" -- "$@" && git log --oneline -1
