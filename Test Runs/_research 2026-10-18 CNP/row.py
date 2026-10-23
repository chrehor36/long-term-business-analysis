import csv, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = {r[0]: r for r in csv.reader(open(sys.argv[1], encoding="utf-8"))}
for i in sys.argv[2:]:
    r = rows.get(i)
    print(i, r[3] if r else "", "::", r[2][:700] if r else "MISSING"); print()
