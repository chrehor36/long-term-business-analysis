import json, urllib.request, datetime, os, ssl
HERE = os.path.dirname(os.path.abspath(__file__))
out = {}
for sym in ["STLAM.MI", "STLAP.PA", "STLA"]:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range=1mo&interval=1d"
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read()
    d = json.loads(raw)
    r = d["chart"]["result"][0]
    ts = r["timestamp"]
    cl = r["indicators"]["quote"][0]["close"]
    rows = [(datetime.datetime.utcfromtimestamp(t).strftime("%Y-%m-%d"), c) for t, c in zip(ts, cl)]
    out[sym] = {"currency": r["meta"].get("currency"), "exchange": r["meta"].get("exchangeName"), "rows": rows[-8:]}
    print(sym, r["meta"].get("currency"), r["meta"].get("exchangeName"), rows[-6:])
# ECB reference rate USD per EUR
url = "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=6&format=csvdata"
try:
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60).read().decode()
except Exception as e:
    import certifi
    ctx = ssl.create_default_context(cafile=certifi.where())
    raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=60, context=ctx).read().decode()
lines = raw.strip().splitlines()
hdr = lines[0].split(",")
i_t, i_v = hdr.index("TIME_PERIOD"), hdr.index("OBS_VALUE")
fx = [(l.split(",")[i_t], l.split(",")[i_v]) for l in lines[1:]]
print("ECB USD/EUR", fx)
out["ECB_USD_per_EUR"] = fx
json.dump(out, open(os.path.join(HERE, "prices_2026-09-13.json"), "w"), indent=1)
