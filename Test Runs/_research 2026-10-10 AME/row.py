"""Print ledger rows by id, or search rows for a phrase.  python row.py ID [ID...] | python row.py -s "phrase" """
import csv, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
rows = {r["id"]: r for r in csv.DictReader(open(os.path.join(ROOT, "principle_ledger_v5.csv"), encoding="utf-8-sig"))}
out = []
if sys.argv[1] == "-s":
    ph = sys.argv[2].lower()
    for k, r in rows.items():
        if ph in r["quote_verbatim"].lower():
            out.append(f"{k}: {r['quote_verbatim'][:300]}")
else:
    for k in sys.argv[1:]:
        out.append(f"{k}: {rows[k]['quote_verbatim']}" if k in rows else f"{k}: MISSING")
open(os.path.join(os.path.dirname(__file__), "cache", "row_out.txt"), "w", encoding="utf-8").write("\n\n".join(out))
