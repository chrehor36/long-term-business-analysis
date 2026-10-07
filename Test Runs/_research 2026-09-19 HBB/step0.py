import sys, os, json, datetime
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
print("now", datetime.datetime.now().isoformat())
print("sovereign", sources.sovereign("USD"))
print("price()", sources.price("HBB"))
c = sources._chart("HBB", rng="1mo", max_age_h=0)
r = c["chart"]["result"][0] if "chart" in c else c
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
for i, t in enumerate(ts):
    print(datetime.datetime.utcfromtimestamp(t).date(), q["open"][i], q["high"][i], q["low"][i], q["close"][i], q["volume"][i])
print("meta", {k: r["meta"].get(k) for k in ("regularMarketPrice","regularMarketTime","currency","exchangeName")})
print("split after 2026-08-04", sources.split_factor_after("HBB", "2026-08-01"))
print("deal", sources.deal_filings("0001709164"))
print("deal_note", sources.deal_note("0001709164"))
