"""Year-end closes (raw close, not adjclose) from the aggregator chart that tools/sources.py uses. AGGREGATOR, FLAGGED:
used only for the market-value leg of the Q6 retention test. Run from the repo root."""
import sys, datetime
sys.path.insert(0, "tools")
import sources
r = sources._chart(sys.argv[1] if len(sys.argv) > 1 else "AXP", rng="10y")
ts, closes = r["timestamp"], r["indicators"]["quote"][0]["close"]
last = {}
for t, c in zip(ts, closes):
    if c is None: continue
    d = datetime.datetime.utcfromtimestamp(t).date()
    last[d.year] = (d.isoformat(), round(c, 2))
for y in sorted(last): print(y, *last[y])
