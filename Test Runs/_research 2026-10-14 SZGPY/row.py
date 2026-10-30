"""Print principle_ledger_v5.csv rows by id, or search quotes for a phrase.
Usage: python row.py ID [ID ...]      |  python row.py -s "phrase"  """
import csv
import sys

LEDGER = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r["id"]: r for r in csv.DictReader(open(LEDGER, encoding="utf-8-sig"))}
args = sys.argv[1:]
if args and args[0] == "-s":
    ph = args[1].lower()
    for i, r in rows.items():
        if ph in r["quote_verbatim"].lower():
            print(f"{i}: {r['quote_verbatim'][:300]}")
else:
    for i in args:
        r = rows.get(i)
        print(f"== {i}: {r['quote_verbatim'] if r else 'MISSING'}\n")
