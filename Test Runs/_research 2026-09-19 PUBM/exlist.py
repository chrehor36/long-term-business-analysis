from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
L=[l.split() for l in open("filings_list.txt")]
for x in L:
    if x[1]=="8-K" and "2.02" in x[4] and x[0] >= "2021-02-01":
        try: print(x[0], x[2], exhibits(x[2], cik=1422930 if x[2].startswith("00014") else 1422930))
        except Exception as e: print("ERR", x[0], e)
        time.sleep(0.3)
