from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
L=[l.split() for l in open("filings_list.txt")]
for x in L:
    if x[1]=="8-K" and x[0].startswith("2021-04"):
        names = exhibits(x[2]); print(x[0], x[2], names)
        ex=[n for n in names if "3" in n and ("ex3" in n.lower() or "exhibit31" in n.lower() or "ex-3" in n.lower())]
        for i,n in enumerate(ex): grab(x[2], n, f"CHARTER_{x[0]}_{i}", cik=1734722)
