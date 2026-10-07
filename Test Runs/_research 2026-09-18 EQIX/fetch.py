import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_core import *
sub = json.load(open(os.path.join(HERE, "submissions.json"), encoding="utf-8"))["filings"]["recent"]
rows = list(zip(sub["form"], sub["filingDate"], sub["reportDate"], sub["accessionNumber"], sub["primaryDocument"], sub["items"]))
which = sys.argv[1]
for f, fd, rd, acc, doc, it in rows:
    if which == "core":
        if f == "10-K" and rd >= "2019-12-31": grab(acc, doc, f"10K_FY{rd[:4]}")
        if f == "10-Q" and fd >= "2025-04-01": grab(acc, doc, f"10Q_{rd}")
        if f == "DEF 14A" and fd >= "2025-01-01": grab(acc, doc, f"DEF14A_{fd[:4]}")
    if which == "8k" and f.startswith("8-K") and fd >= "2024-01-01" and any(x in it for x in ("2.02","8.01","7.01","1.01","2.01","4.02","4.01")):
        if "2.02" in it and fd < "2025-01-01" and fd not in ("2024-02-14",): continue
        try: names = exhibits(acc)
        except Exception as e: print("idx fail", acc, e); continue
        grab(acc, doc, f"8K_{fd}_{acc[-6:]}_main")
        for n in names:
            if re.search(r"ex-?99|ex99|exhibit99|dex99|ex991", n, re.I) and n.lower().endswith((".htm",".html")):
                grab(acc, n, f"EX99_{fd}_{acc[-6:]}_{re.sub(r'[^A-Za-z0-9]','',n)[:30]}")
