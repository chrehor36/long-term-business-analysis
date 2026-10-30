import csv, sys
sys_ = __import__("sys"); sys_.stdout.reconfigure(encoding="utf-8", errors="replace")
rows = {r[0]: r for r in csv.reader(open(sys.argv[1], encoding="utf-8"))}
hdr = None
for i in sys.argv[2:]:
    r = rows.get(i)
    print(i, "=>", r[2][:1200] if r else "MISSING")
    print()
