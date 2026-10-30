from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
rows=[l.split() for l in open("filings_list.txt") if " 8-K " in l and "2.02" in l]
rows=[r for r in rows if r[0]>="2021-01-01"]
for r in rows:
    d,acc=r[0],r[2]
    name=f"EX99_{d}"
    if os.path.exists(name+".txt"): continue
    try:
        items=exhibits(acc)
        ex=[i for i in items if re.search(r"(ex|exhibit)[-_]?9", i, re.I) and i.endswith(".htm")]
        if not ex: print("no ex", d, items); continue
        grab(acc, ex[0], name)
    except Exception as e: print("ERR", d, e)
