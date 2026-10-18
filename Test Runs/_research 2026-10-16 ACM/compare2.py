from facts import load, annual
def first(d, tags):
    out = {}
    for t in tags:
        for k, v in annual(d, t).items(): out.setdefault(k, v[0]/1e6)
    return out
REV = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueServicesNet"]
DEBT = {"ACM":["LongTermDebtAndCapitalLeaseObligations","LongTermDebtAndCapitalLeaseObligationsCurrent","ShortTermBorrowings"],
        "J":["LongTermDebtNoncurrent","LongTermDebt","DebtCurrent","ShortTermBorrowings","LongTermDebtCurrent"],
        "TTEK":["LongTermDebtNoncurrent","LongTermDebtCurrent","LongTermLineOfCredit"]}
for t in ["ACM","J","TTEK"]:
    d = load(t); rev = first(d, REV); oi = first(d, ["OperatingIncomeLoss"])
    eq = first(d, ["StockholdersEquity"]); gw = first(d, ["Goodwill"]); ia = first(d, ["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"])
    cash = first(d, ["CashAndCashEquivalentsAtCarryingValue","CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"])
    dsum = {}
    for tag in DEBT[t]:
        a = annual(d, tag)
        for k,v in a.items(): dsum.setdefault(k, {}).setdefault(tag, v[0]/1e6)
    print(d["entityName"], "  FY  margin  OI/(eq+netdebt)  OI/(tangible eq+netdebt)")
    ms=[]; rs=[]; rts=[]
    for k in sorted(rev):
        if k < "2016-06" or k not in oi: continue
        dd = dsum.get(k, {})
        if t=="J": debt = dd.get("LongTermDebtNoncurrent", dd.get("LongTermDebt",0)) + dd.get("DebtCurrent", dd.get("LongTermDebtCurrent",0)) + dd.get("ShortTermBorrowings",0)
        else: debt = sum(dd.values())
        cap = eq.get(k,0)+debt-cash.get(k,0); tcap = cap-gw.get(k,0)-ia.get(k,0)
        m = 100*oi[k]/rev[k]; r = 100*oi[k]/cap if cap>0 else float('nan'); rt = 100*oi[k]/tcap if tcap>0 else float('nan')
        ms.append(m); rs.append(r)
        print(f"   {k[:4]}  {m:5.1f}%   {r:6.1f}%   {('%6.1f%%'%rt) if tcap>0 else '  neg tangible'}   (debt {debt:.0f} cash {cash.get(k,0):.0f})")
    print(f"   avg margin {sum(ms)/len(ms):.1f}%  avg OI/capital {sum(rs)/len(rs):.1f}%")
