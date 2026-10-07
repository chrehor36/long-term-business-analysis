import urllib.request, json
UA={"User-Agent":"Mozilla/5.0","Accept-Encoding":"identity"}
for t in ["ACMR","LRCX","AMAT","KLAC","ACLS","VECO","ONTO"]:
    try:
        u=f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d"
        d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
        r=d["chart"]["result"][0]
        import datetime
        ts=r["timestamp"]; cl=r["indicators"]["quote"][0]["close"]
        print(t, [(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d"), b) for a,b in zip(ts,cl)][-3:], "| mktprice:", r["meta"].get("regularMarketPrice"), r["meta"].get("regularMarketTime"))
    except Exception as e:
        print(t,"ERR",e)
