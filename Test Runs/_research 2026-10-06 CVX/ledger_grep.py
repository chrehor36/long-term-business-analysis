"""Grep principle_ledger_v5.csv by regex; print id, speaker and the quote (truncated).
Usage: python ledger_grep.py REGEX [maxchars]"""
import csv, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
rows = list(csv.DictReader(open(root / 'principle_ledger_v5.csv', encoding='utf-8-sig')))
pat = re.compile(sys.argv[1], re.I)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 400
for r in rows:
    if pat.search(r['quote_verbatim']):
        print(r['id'], r['speaker'], '|', r['quote_verbatim'][:n].replace('\n', ' '))
