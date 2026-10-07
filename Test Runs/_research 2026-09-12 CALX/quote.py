import json, urllib.request, ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
for t in ["CALX","ADTN","CIEN","HLIT","UI","NOK"]:
    u = f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d"
    try:
        r = urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0"})
        d = json.load(urllib.request.urlopen(r, timeout=30, context=ctx))
        res = d["chart"]["result"][0]
        import datetime
        ts = res["timestamp"]; cl = res["indicators"]["quote"][0]["close"]
        print(t, [(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d"), round(b,2) if b else None) for a,b in zip(ts,cl)])
        print("   meta regularMarketPrice", res["meta"].get("regularMarketPrice"))
    except Exception as e:
        print(t, "FAILED", e)
