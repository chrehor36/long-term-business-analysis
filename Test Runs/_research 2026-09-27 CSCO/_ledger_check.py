import csv,sys
ids="E3-03 E3-43 E3-46 E4-04 E4-23 E4-27 E4-29 E4-22 E3-44 E2-09 E4-28 E4-25 E3-31 E4-46 E4-19 E4-18 E4-15 E3-32 E3-27 E4-14 E3-70 E4-44 E2-59 E2-44 E4-37 E4-26 E3-41 E4-52 E2-49 E5-20".split()
rows=list(csv.DictReader(open("principle_ledger.csv",encoding="utf-8")))
print(list(rows[0].keys()))
idk=list(rows[0].keys())[0]
by={r[idk]:r for r in rows}
for i in ids:
    r=by.get(i)
    if not r: print(i,"MISSING"); continue
    txt=" | ".join(str(v)[:230] for k,v in r.items() if k!=idk)
    print(i,"::",txt[:330].replace("\n"," "))
