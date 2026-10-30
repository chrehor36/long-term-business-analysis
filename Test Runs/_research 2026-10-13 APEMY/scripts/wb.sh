#!/bin/bash
# wb.sh SRCNAME DEST : fetch raw archived copy of an aperam.com document from the Wayback Machine
cd "/c/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-10-13 APEMY/cache"
j=$(curl -s --max-time 60 "https://archive.org/wayback/available?url=www.aperam.com/sites/default/files/documents/$1")
u=$(echo "$j" | python -I -c "import sys,json;d=json.load(sys.stdin);c=d['archived_snapshots'].get('closest');print(c['url'] if c else '')")
[ -z "$u" ] && { echo "$2 NOARCHIVE"; exit; }
raw=$(echo "$u" | sed -E 's#/web/([0-9]+)/#/web/\1id_/#; s#^http:#https:#')
for i in 1 2 3 4 5; do
  curl -sL --max-time 900 -C - -o "$2" "$raw"
  if pdftotext -l 1 "$2" - >/dev/null 2>&1; then echo "$2 OK $(stat -c %s "$2") $raw"; exit; fi
done; echo "$2 FAIL $raw"
