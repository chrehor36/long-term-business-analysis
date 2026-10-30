import json, urllib.request, datetime, os
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for t in ["TM", "7203.T", "JPY=X", "HMC", "7267.T"]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1mo&interval=1d"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    d = json.loads(urllib.request.urlopen(req, timeout=60).read())
    r = d["chart"]["result"][0]
    ts = r["timestamp"]; cl = r["indicators"]["quote"][0]["close"]
    rows = [(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d"), c) for a, c in zip(ts, cl)]
    out[t] = {"meta_currency": r["meta"].get("currency"), "exchange": r["meta"].get("exchangeName"), "last": rows[-8:]}
    print(t, r["meta"].get("currency"), r["meta"].get("exchangeName"), rows[-6:])
json.dump(out, open(os.path.join(HERE, "prices_2026-09-13.json"), "w"), indent=1)
