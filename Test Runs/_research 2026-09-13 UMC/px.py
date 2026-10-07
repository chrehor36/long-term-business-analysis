import json, urllib.request, datetime, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for t in ["2303.TW", "UMC", "2363.TW", "3035.TW", "3037.TW", "3034.TW", "6147.TWO", "3014.TW", "6202.TW", "8021.TW", "3227.TWO", "2330.TW", "TSM", "GFS", "TSEM", "5347.TWO"]:
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=3mo&interval=1d"
        r = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=45).read())["chart"]["result"][0]
        ts = r["timestamp"]; c = r["indicators"]["quote"][0]["close"]
        rows = [(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d %H:%M"), b) for a, b in zip(ts, c)]
        out[t] = {"meta": {k: r["meta"].get(k) for k in ("currency", "regularMarketPrice", "regularMarketTime", "exchangeName", "longName", "shortName")}, "rows": rows}
        print(t, out[t]["meta"]["shortName"], out[t]["meta"]["currency"], rows[-3:])
    except Exception as e:
        print(t, "ERR", e)
json.dump(out, open(os.path.join(HERE, "prices_2026-09-13.json"), "w"), indent=1)
