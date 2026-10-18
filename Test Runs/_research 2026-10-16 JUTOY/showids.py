import csv, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
rows = {r["id"]: r for r in csv.DictReader(open(sys.argv[1], encoding="utf-8-sig"))}
for i in sys.argv[2:]:
    r = rows.get(i)
    print(f"== {i}: " + ("MISSING" if r is None else r["quote_verbatim"][:700]))
