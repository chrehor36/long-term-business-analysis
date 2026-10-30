from fetch_core import *
import sys, re
sys.stdout.reconfigure(encoding="utf-8")
L=[l.split() for l in open("filings_list.txt")]
out=open("13d_2026.txt","w",encoding="utf-8")
for x in L:
    if x[1].startswith("SCHEDULE_13") and x[0] >= "2026-01-01":
        acc=x[2]; a=acc.replace("-","")
        cik=int(acc.split("-")[0])
        for c in (cik, 1828972):
            try:
                t=get(f"https://www.sec.gov/Archives/edgar/data/{c}/{a}/primary_doc.xml"); break
            except Exception as e: t=None
        if not t: print("ERR", acc); continue
        tx=re.sub(r"<[^>]+>"," | ",t); tx=re.sub(r"(\s*\|\s*)+"," | ",tx)
        out.write(f"\n######## {x[0]} {x[1]} {acc}\n{tx[:6000]}\n"); print(x[0],x[1],acc,len(tx))
        time.sleep(0.3)
