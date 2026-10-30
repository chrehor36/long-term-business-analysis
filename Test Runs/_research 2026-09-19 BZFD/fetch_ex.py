from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
L=[l.split() for l in open("filings_list.txt")]
for x in L:
    if x[1]=="8-K" and "2.02" in x[4] and x[0] >= "2022-01-01":
        acc=x[2]
        try: names=exhibits(acc)
        except Exception as e: print("ERR idx",acc,e); continue
        ex=[n for n in names if n.endswith(".htm") and re.search(r"ex[-_]?99[-_.]?1|ex991|exhibit991|99-?1|pressrelease|earnings", n.lower())]
        print(x[0],acc,ex)
        if ex:
            try: grab(acc, ex[0], "EX991_"+x[0])
            except Exception as e: print("ERR", e)
        time.sleep(0.3)
