import urllib.request, json, datetime
UA={"User-Agent":"Mozilla/5.0","Accept-Encoding":"identity"}
u="https://query1.finance.yahoo.com/v8/finance/chart/ALKT?range=2y&interval=1d"
d=json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read())
r=d["chart"]["result"][0]; ts=r["timestamp"]; cl=r["indicators"]["quote"][0]["close"]; vol=r["indicators"]["quote"][0]["volume"]
rows=[(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d"),b,v) for a,b,v in zip(ts,cl,vol)]
json.dump(rows,open("px_history_2y.json","w"))
for dd,c,v in rows:
    if dd in ("2025-06-30","2025-06-27","2025-12-31","2026-03-31","2026-06-30","2026-03-25","2026-06-22") or dd>="2026-08-25": print(dd, round(c,2) if c else c, v)
print("split events:", r.get("events"))
