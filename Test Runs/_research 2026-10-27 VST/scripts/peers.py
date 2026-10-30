import json, sys
D = sys.argv[1]
names = {"0001692819":"VST","0001013871":"NRG","0001868275":"CEG","0001622536":"TLN"}
tags = {
 "OI":["OperatingIncomeLoss"],
 "NI":["NetIncomeLoss","ProfitLoss"],
 "EQ":["StockholdersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
 "GW":["Goodwill"],
 "INT":["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"],
 "LTD":["LongTermDebtNoncurrent","LongTermDebtAndCapitalLeaseObligations","LongTermDebt"],
 "CUR":["LongTermDebtCurrent","LongTermDebtAndCapitalLeaseObligationsCurrent"],
 "CASH":["CashAndCashEquivalentsAtCarryingValue"],
 "REV":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax"],
 "INTX":["InterestExpense","InterestExpenseNonoperating","InterestAndDebtExpense"],
 "PRETAX":["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"],
}
def annual(f, tag, instant):
    out = {}
    u = f["facts"]["us-gaap"].get(tag, {}).get("units", {}).get("USD", [])
    for x in u:
        if x.get("form") not in ("10-K","10-K/A"): continue
        if instant:
            if "start" in x: continue
            y = x["end"][:4]
            if x["end"][5:] != "12-31": continue
        else:
            if "start" not in x: continue
            s,e = x["start"], x["end"]
            if e[5:] != "12-31" or s[5:] != "01-01" or s[:4] != e[:4]: continue
            y = e[:4]
        # keep first-filed value per year
        if y not in out or x["filed"] < out[y][1]:
            out[y] = (x["val"]/1e6, x["filed"], x["accn"])
    return out
inst = {"EQ","GW","INT","LTD","CUR","CASH"}
for cik,n in names.items():
    f = json.load(open(f"{D}/cache/facts_{cik}.json"))
    data = {}
    for k,ts in tags.items():
        for t in ts:
            a = annual(f,t,k in inst)
            if a:
                for y,v in a.items():
                    data.setdefault(k,{}).setdefault(y,v)
    print("==",n)
    print("year     REV      OI   PRETAX     NI      EQ     GW    INT    LTD    CUR   CASH  INTX")
    for y in range(2014,2026):
        y=str(y)
        row=[data.get(k,{}).get(y,(None,))[0] for k in ["REV","OI","PRETAX","NI","EQ","GW","INT","LTD","CUR","CASH","INTX"]]
        if all(r is None for r in row): continue
        print(y," ".join(f"{(r if r is not None else float('nan')):7.0f}" for r in row))
