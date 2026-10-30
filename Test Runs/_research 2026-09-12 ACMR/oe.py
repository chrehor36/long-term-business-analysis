import urllib.request, json, io, time, collections
UA={"User-Agent":"BRK framework run chrehor36@gmail.com","Accept-Encoding":"identity"}
def get(u):
    for i in range(5):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=180).read()
        except Exception as e: print("retry",e); time.sleep(4)
    raise SystemExit("fail")
d=json.loads(get("https://data.sec.gov/api/xbrl/companyfacts/CIK0001680062.json").decode())
io.open("Test Runs/_research 2026-09-12 ACMR/companyfacts.json","w",encoding="utf-8").write(json.dumps(d))
us=d["facts"]["us-gaap"]
def series(tag, unit="USD", annual=True):
    if tag not in us: return None
    out={}
    for f in us[tag]["units"].get(unit,[]):
        if f.get("form") not in ("10-K","10-K/A"): continue
        st=f.get("start"); en=f["end"]
        if annual:
            if not st: continue
            # calendar year, ~365 days
            import datetime
            a=datetime.date.fromisoformat(st); b=datetime.date.fromisoformat(en)
            if not (330 <= (b-a).days <= 400): continue
            key=en
        else:
            if st: continue
            key=en
        # newest vintage wins
        prev=out.get(key)
        if prev is None or f["filed"]>prev[1]:
            out[key]=(f["val"], f["filed"], f.get("accn"))
    return dict(sorted(out.items()))
tags_flow=["NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation",
 "DepreciationDepletionAndAmortization","PaymentsToAcquirePropertyPlantAndEquipment",
 "PaymentsToAcquireIntangibleAssets","Revenues","RevenueFromContractWithCustomerExcludingAssessedTax",
 "NetIncomeLoss","ProfitLoss","NetIncomeLossAttributableToNoncontrollingInterest",
 "IncreaseDecreaseInAccountsPayable","IncreaseDecreaseInAccountsPayableTrade",
 "GrossProfit","CostOfRevenue","StockIssuedDuringPeriodValueNewIssues"]
for t in tags_flow:
    s=series(t)
    if s: print(t); [print("   ",k,f"{v[0]:>15,}", v[1]) for k,v in s.items()]
    else: print(t, "-- NOT RESOLVED (annual)")
