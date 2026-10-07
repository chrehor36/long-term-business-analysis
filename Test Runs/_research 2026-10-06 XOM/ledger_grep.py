"""Search principle_ledger_v5.csv by regex on the quote; print id, year, quote (truncated). Usage: ledger_grep.py REGEX [maxlen]"""
import csv, re, sys
pat = re.compile(sys.argv[1], re.I)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 500
with open('principle_ledger_v5.csv', encoding='utf-8-sig') as f:
    for x in csv.DictReader(f):
        q = x['quote_verbatim']
        if pat.search(q):
            print(x['id'], '|', q[:n].replace('\n', ' '), '\n')
