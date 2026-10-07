import sys, os, json, datetime
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
r = sources._chart("DLR", rng="1mo", max_age_h=0)
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
print("meta regularMarketPrice", r["meta"].get("regularMarketPrice"), datetime.datetime.utcfromtimestamp(r["meta"]["regularMarketTime"]))
for t, o, h, l, c, v in zip(ts, q["open"], q["high"], q["low"], q["close"], q["volume"]):
    print(datetime.datetime.utcfromtimestamp(t).date(), o and round(o,2), h and round(h,2), l and round(l,2), c and round(c,4), v)
ev = r.get("events", {})
print("events", json.dumps(ev)[:600])
print("split after 2026-07-01:", sources.split_factor_after("DLR", "2026-07-01"))
