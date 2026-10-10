# print v5 ledger rows by id (quote only), or search quotes by regex: python row.py ID [ID...] | python row.py -s REGEX
import csv, sys, re, os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "principle_ledger_v5.csv")
rows = {r["id"]: r for r in csv.DictReader(open(P, encoding="utf-8-sig"))}
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
if sys.argv[1] == "-s":
    rx = re.compile(sys.argv[2], re.I)
    for i, r in rows.items():
        if rx.search(r["quote_verbatim"]):
            print(i, "|", r["quote_verbatim"][:400].replace("\n", " "))
else:
    for i in sys.argv[1:]:
        r = rows.get(i)
        print(i, "|", r["quote_verbatim"].replace("\n", " ") if r else "MISSING")
        print()
