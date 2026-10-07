from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
L=[l.split() for l in open("filings_list.txt")]
for x in L:
    if x[1] in ("8-K","8-K/A") and "2.02" in x[4] and x[0] >= "2022-05-01":
        acc=x[2]
        try: names=exhibits(acc)
        except Exception as e: print("ERR idx",acc,e); continue
        ex=[n for n in names if n.endswith(".htm") and n != x[3] and "index" not in n and ("99" in n or "ex" in n.lower())]
        print(x[0],acc,ex)
        for n in ex[:1]:
            try: grab(acc, n, "EX99_"+x[0])
            except Exception as e: print("ERR", e)
        time.sleep(0.3)
