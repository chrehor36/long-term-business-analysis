"""Print ledger rows by id: python q.py ID [ID ...]"""
import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"C:\Users\chreh\OneDrive\Documents\BRK\principle_ledger_v5.csv"
rows = {r['id']: r for r in csv.DictReader(open(p, encoding='utf-8-sig'))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(f"[{i}]", (r['quote_verbatim'] if r else 'MISSING'), "\n")
