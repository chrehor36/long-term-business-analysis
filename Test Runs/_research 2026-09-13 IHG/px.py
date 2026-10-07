"""Live quotes (Yahoo chart API; AGGREGATOR, flagged) for GFS; price history for context. Transcription only."""
import sys, os, json, datetime
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
import sources as S
out = {}
r = S._chart("IHG", rng="max", max_age_h=0)
ts = r["timestamp"]; q = r["indicators"]["quote"][0]
rows = [(datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"), c) for t, c in zip(ts, q["close"]) if c]
out["meta"] = {k: r["meta"].get(k) for k in ("currency", "exchangeName", "regularMarketPrice", "regularMarketTime")}
out["last10"] = rows[-10:]
out["splits"] = (r.get("events") or {}).get("splits")
# year-end closes and key dates
ye = {}
for d, c in rows:
    ye[d[:4]] = (d, c)
out["year_end"] = ye
look = ["2019-12-31","2020-03-18","2020-12-31","2026-01-02","2026-02-17","2026-08-11","2026-09-03"]
out["key"] = {k: [x for x in rows if x[0] >= k][:1] for k in look}
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "prices_ADR_2026-09-13.json"), "w"), indent=1)
print(json.dumps(out, indent=1))
