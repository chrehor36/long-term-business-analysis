import sys, os, json, datetime
sys.path.insert(0, os.path.join("..", "..", "tools"))
import sources as S
out = {}
for t in ("IHG", "IHG.L", "MAR", "HLT", "H", "WH", "CHH", "AC.PA", "GBPUSD=X"):
    r = S._chart(t, rng="1mo", max_age_h=0)
    ts = r["timestamp"]; q = r["indicators"]["quote"][0]
    rows = [(datetime.datetime.utcfromtimestamp(x).strftime("%Y-%m-%d"), c) for x, c in zip(ts, q["close"]) if c]
    m = r["meta"]
    out[t] = {"currency": m.get("currency"), "exchange": m.get("exchangeName"), "regularMarketPrice": m.get("regularMarketPrice"),
              "regularMarketTime": datetime.datetime.utcfromtimestamp(m.get("regularMarketTime")).isoformat(), "last5": rows[-5:],
              "splits": (r.get("events") or {}).get("splits")}
    print(t, out[t])
json.dump(out, open("prices_daily_2026-09-13.json", "w"), indent=1)
