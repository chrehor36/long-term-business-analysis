import json, urllib.request, sys, datetime
for t in sys.argv[1:]:
    try:
        url=f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=1mo&interval=1d"
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        r=json.loads(urllib.request.urlopen(req,timeout=30).read())["chart"]["result"][0]
        m=r["meta"]; ts=r["timestamp"]; c=r["indicators"]["quote"][0]["close"]
        print(t, m.get("currency"), m.get("regularMarketPrice"), datetime.datetime.utcfromtimestamp(m["regularMarketTime"]).strftime("%Y-%m-%d"), [(datetime.datetime.utcfromtimestamp(a).strftime("%m-%d"), round(b,2) if b else None) for a,b in zip(ts[-5:],c[-5:])])
    except Exception as e:
        print(t, "ERR", e)
