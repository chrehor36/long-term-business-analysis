import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_core import *
sub = json.load(open(os.path.join(HERE, "submissions.json"), encoding="utf-8"))["filings"]["recent"]
for f, fd, acc, doc, it in zip(sub["form"], sub["filingDate"], sub["accessionNumber"], sub["primaryDocument"], sub["items"]):
    if f.startswith("8-K") and "5.02" in it and fd >= "2024-01-01":
        grab(acc, doc, f"8K502_{fd}_{acc[-6:]}")
        t = open(os.path.join(HERE, f"8K502_{fd}_{acc[-6:]}.txt"), encoding="utf-8").read()
        i = t.find("Item 5.02")
        print("=====", fd, acc, re.sub(r"\s+", " ", t[i:i+1100]))
