"""Print v5 ledger rows by id: python row.py ID [ID ...]"""
import csv, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "..", "..", "principle_ledger_v5.csv")
want = set(sys.argv[1:])
for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig")):
    if r["id"] in want:
        print(f"[{r['id']}] ({r['year']}, {r['speaker']}, {r['source_file']})\n{r['quote_verbatim']}\n")
