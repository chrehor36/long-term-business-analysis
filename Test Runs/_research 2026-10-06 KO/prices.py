"""Year-end closes and yearly average closes for KO from the price cache tools/run.py wrote (Yahoo chart endpoint;
AGGREGATOR, flagged: used for the retention test's market-value leg and for the prices paid on buybacks only).
`close`, never `adjclose` (operator protocol). Usage: python prices.py"""
import json, os
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
r = json.load(open(os.path.join(ROOT, "tools", "_cache", "px_KO_10y.json")))["chart"]["result"][0]
ts = r["timestamp"]
cl = r["indicators"]["quote"][0]["close"]
by_year = {}
for t, c in zip(ts, cl):
    if c is None:
        continue
    d = datetime.fromtimestamp(t, tz=timezone.utc)
    by_year.setdefault(d.year, []).append((d.strftime("%Y-%m-%d"), c))
print("year  last close (date)        mean close   low     high")
for y in sorted(by_year):
    v = by_year[y]
    cs = [c for _, c in v]
    print(f"{y}  {v[-1][1]:7.2f} ({v[-1][0]})   {sum(cs)/len(cs):7.2f}   {min(cs):6.2f}  {max(cs):6.2f}")
print("splits in window:", r.get("events", {}).get("splits", "none"))
