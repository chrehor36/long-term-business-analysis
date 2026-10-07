import sys, os, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_core import *
cache = os.path.join(sources.CACHE, "sov_USD_treasury.csv")
if os.path.exists(cache): os.remove(cache)
print("SOV", sources.sovereign("USD"))
print("CIK", sources.cik_for("SMCI"))
open(os.path.join(HERE, "submissions.json"), "w", encoding="utf-8").write(get("https://data.sec.gov/submissions/CIK0001375365.json")); print("got submissions")
print("PRICE(intraday, not struck)", sources.price("SMCI"))
print("DEALS", sources.deal_filings("0001375365"))
print("DEALNOTE", sources.deal_note("0001375365"))
r = sources._chart("SMCI", rng="1mo", max_age_h=0)
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
print("meta regularMarketPrice", r["meta"].get("regularMarketPrice"), datetime.datetime.utcfromtimestamp(r["meta"]["regularMarketTime"]))
for t, o, h, l, c, v in zip(ts, q["open"], q["high"], q["low"], q["close"], q["volume"]):
    print(datetime.datetime.utcfromtimestamp(t).date(), o and round(o,2), h and round(h,2), l and round(l,2), c and round(c,4), v)
rm = sources._chart("SMCI", rng="max", max_age_h=0)
print("splits", json.dumps((rm.get("events") or {}).get("splits")))
print("split after 2026-07-31:", sources.split_factor_after("SMCI", "2026-07-31"))
