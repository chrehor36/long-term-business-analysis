import csv, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
rows = {r[0]: r for r in csv.reader(open(sys.argv[1], encoding="utf-8-sig"))}
hdr = rows.pop(next(iter(rows)))
for i in sys.argv[2:]:
    r = rows.get(i)
    if not r: print(i, "MISSING"); continue
    d = dict(zip(hdr, r))
    q = d["quote_verbatim"] + "  [" + d["source_file"] + "]"
    print(f"{i} | {q}\n")
