"""Print the verbatim quote of each v5 ledger id given."""
import csv, sys
rows = {r[0]: r for r in csv.reader(open("principle_ledger_v5.csv", encoding="utf-8-sig"))}
for i in sys.argv[1:]:
    r = rows.get(i)
    print(i, "MISSING" if not r else f"[{r[3]} {r[8]}] " + r[2].replace("\n", " "))
    print()
