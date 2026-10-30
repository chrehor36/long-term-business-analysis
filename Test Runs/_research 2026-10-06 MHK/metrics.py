# Arithmetic only: Mohawk annual series from XBRL companyfacts (facts.json), year-end instants from 10-K filings.
import json
from datetime import date
d = json.load(open("facts.json"))["facts"]["us-gaap"]
def dur(k):
    out = {}
    if k not in d: return out
    for u,arr in d[k]["units"].items():
        for x in arr:
            if x.get("form","").startswith("10-K") and "start" in x:
                s=date.fromisoformat(x["start"]); e=date.fromisoformat(x["end"])
                if 350<(e-s).days<380:
                    out[int(x["end"][:4])] = x["val"]/1e6   # last filed wins (latest restatement)
    return out
def inst(k):
    out = {}
    if k not in d: return out
    for u,arr in d[k]["units"].items():
        for x in arr:
            if x.get("form","").startswith("10-K") and "start" not in x and x["end"][5:]=="12-31":
                out[int(x["end"][:4])] = x["val"]/1e6
    return out
sales = {**dur("SalesRevenueNet"), **dur("SalesRevenueGoodsNet"), **dur("RevenueFromContractWithCustomerExcludingAssessedTax")}
opi = dur("OperatingIncomeLoss")
imp = {**dur("GoodwillAndIntangibleAssetImpairment")}
imp.setdefault(2008, 1543.4); imp.setdefault(2016, 47.9)
ocf = dur("NetCashProvidedByUsedInOperatingActivities"); capex = dur("PaymentsToAcquirePropertyPlantAndEquipment")
da = dur("DepreciationDepletionAndAmortization"); sbc = dur("ShareBasedCompensation")
eq = inst("StockholdersEquity"); gw = inst("Goodwill")
ti = {**inst("IndefiniteLivedTrademarks"), **inst("IndefiniteLivedIntangibleAssetsExcludingGoodwill")}
fi = inst("FiniteLivedIntangibleAssetsNet")
cash = inst("CashAndCashEquivalentsAtCarryingValue")
ltd = inst("LongTermDebtNoncurrent"); std = {**inst("LongTermDebtCurrent"), **inst("ShortTermBorrowingsAndCurrentPortionOfLongTermDebt"), **inst("DebtCurrent")}
print("year  sales   opInc  impair  opExImp  margin%  OCF  capex  D&A  SBC  OCF-SBC-capex  OCF-SBC-D&A  tangCap  preTaxROTC%")
rows=[]
for y in range(2008, 2026):
    s=sales.get(y); o=opi.get(y)
    if s is None or o is None: 
        print(y, "missing", s, o); continue
    i=imp.get(y,0) or 0; ox=o+i
    tc=None
    if y in eq and y in gw:
        tc = eq[y] + ltd.get(y,0) + std.get(y,0) - gw[y] - ti.get(y,0) - fi.get(y,0) - cash.get(y,0)
    roc = 100*ox/tc if tc else None
    a=ocf.get(y,0)-sbc.get(y,0)-capex.get(y,0); b=ocf.get(y,0)-sbc.get(y,0)-da.get(y,0)
    rows.append((y,s,ox,a,b))
    print(y, round(s), round(o), round(i), round(ox), round(100*ox/s,1), round(ocf.get(y,0)), round(capex.get(y,0)), round(da.get(y,0)), round(sbc.get(y,0)), round(a), round(b), round(tc) if tc else None, round(roc,1) if roc else None)
