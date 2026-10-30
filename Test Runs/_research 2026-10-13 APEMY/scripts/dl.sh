#!/bin/bash
# usage: dl.sh SRCNAME DEST ; resumes until pdftotext can read the file
cd "/c/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-10-13 APEMY/cache"
B=https://www.aperam.com/sites/default/files/documents
for i in $(seq 1 25); do
  curl -s -A "Mozilla/5.0" -C - --max-time 300 -o "$2" "$B/$1"
  if pdftotext -l 1 "$2" - >/dev/null 2>&1 && tail -c 1100 "$2" | grep -q "%%EOF"; then echo "$2 OK $(stat -c %s "$2")"; exit 0; fi
done
echo "$2 FAILED $(stat -c %s "$2")"
