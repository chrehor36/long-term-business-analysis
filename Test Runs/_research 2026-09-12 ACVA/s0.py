import urllib.request, json, io, csv, time, datetime
UA = {"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
OUT = "C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-09-12 ACVA/"
def get(u, h=UA):
    for i in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=90).read()
        except Exception as e: print("retry", i, e); time.sleep(3)
tk = json.loads(get("https://www.sec.gov/files/company_tickers.json").decode())
for v in tk.values():
    if v["ticker"].upper() in ("ACVA","KAR","OPLN","CPRT","RBA","KMX","CVNA","CRMT"):
        print(v["ticker"], str(v["cik_str"]).zfill(10), v["title"])
cik=[str(v["cik_str"]).zfill(10) for v in tk.values() if v["ticker"]=="ACVA"][0]
sub = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik}.json").decode())
open(OUT+"submissions.json","w").write(json.dumps(sub))
r = sub["filings"]["recent"]
rows = list(zip(r["form"], r["filingDate"], r["reportDate"], r["accessionNumber"], r["primaryDocument"], r["items"]))
for x in rows[:120]:
    if x[0] in ("10-K","10-Q","DEF 14A","8-K","10-K/A","S-1","8-K/A","SC 13D","SC 13D/A","424B4","S-3","S-3ASR","S-8"): print(" | ".join(str(y) for y in x))
cf = get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json")
open(OUT+"companyfacts.json","wb").write(cf)
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv"
d = get(url).decode("utf-8-sig")
rows = list(csv.DictReader(io.StringIO(d)))
for q in rows[:5]: print("TSY", q.get("Date"), "30Y", q.get("30 Yr"), "10Y", q.get("10 Yr"))
h={"User-Agent":"Mozilla/5.0","Accept-Encoding":"identity"}
for t in ["ACVA","KAR","OPLN","CPRT","RBA","KMX","CVNA"]:
    try:
        u=f"https://query1.finance.yahoo.com/v8/finance/chart/{t}?range=5d&interval=1d"
        dd=json.loads(get(u,h)); rr=dd["chart"]["result"][0]
        print("PX",t,[(datetime.datetime.utcfromtimestamp(a).strftime("%Y-%m-%d"), b) for a,b in zip(rr["timestamp"],rr["indicators"]["quote"][0]["close"])][-3:])
    except Exception as e: print("PX",t,"ERR",e)
u="https://query1.finance.yahoo.com/v8/finance/chart/ACVA?range=2y&interval=1d"
open(OUT+"px_history_2y.json","wb").write(get(u,h))
