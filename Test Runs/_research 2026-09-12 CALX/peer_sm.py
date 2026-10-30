import json, urllib.request, time
H={"User-Agent":"Chris Hrehor chrehor36@gmail.com","Accept-Encoding":"identity"}
peers={"CALX":1406666,"ADTN":926282,"CIEN":936395,"HLIT":851310,"CMBM":1738177,"UI":1511737,"CLFD":796505,"CSCO":858877}
tags=["SellingAndMarketingExpense","SellingGeneralAndAdministrativeExpense","GeneralAndAdministrativeExpense","OperatingExpenses","StockholdersEquity","Goodwill","Liabilities","Assets","LongTermDebtNoncurrent","CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]
out={}
for t,c in peers.items():
    try:
        d=json.loads(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json",headers=H),timeout=120).read())
    except Exception as e:
        print(t,"ERR",e); continue
    us=d["facts"].get("us-gaap",{})
    print("\n==",t)
    for tag in tags:
        if tag not in us: continue
        best={}
        for u,rows in us[tag]["units"].items():
            for r in rows:
                if r.get("form")!="10-K": continue
                if "start" in r:
                    from datetime import date
                    s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
                    if not (330<=(e-s).days<=380): continue
                y=r["end"][:4]
                if y not in best or r["filed"]>best[y][1]: best[y]=(r["val"],r["filed"])
        yrs=sorted(best)[-3:]
        print(f"  {tag:52s} " + "  ".join(f"{y}:{best[y][0]/1e6:.0f}" for y in yrs))
    time.sleep(0.4)
