import json, urllib.request, datetime, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for t in ["2330.TW", "TSM", "TWD=X", "2303.TW", "UMC"]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1mo&interval=1d"
    r = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read())["chart"]["result"][0]
    ts = r["timestamp"]; c = r["indicators"]["quote"][0]["close"]
    rows = [(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d %H:%M"), b) for a, b in zip(ts, c)]
    out[t] = {"meta": {k: r["meta"].get(k) for k in ("currency", "regularMarketPrice", "regularMarketTime", "exchangeName", "timezone")}, "rows": rows[-8:]}
    print(t, out[t]["meta"]); [print("  ", x) for x in rows[-6:]]
json.dump(out, open(os.path.join(HERE, "prices_2026-09-13.json"), "w"), indent=1)
