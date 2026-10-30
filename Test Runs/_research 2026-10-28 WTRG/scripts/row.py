import csv, sys
ids = set(sys.argv[2:])
with open(sys.argv[1], encoding="utf-8-sig") as f:
    r = csv.reader(f); h = next(r)
    for row in r:
        if row[0] in ids:
            print(row[0], row[3], "|", row[2][:1100] if len(row)>2 else "")
            print()
