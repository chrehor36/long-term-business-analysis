import json, sys
from datetime import date
def load(path):
    return json.load(open(path))["facts"].get("us-gaap", {})
def series(g, tags, flow=True):
    out = {}
    for t in tags:
        node = g.get(t)
        if not node: continue
        for unit, vals in node["units"].items():
            if unit != "USD": continue
            for v in vals:
                if v.get("form") not in ("10-K","20-F","10-K/A","20-F/A"): continue
                if flow:
                    if "start" not in v: continue
                    d = (date.fromisoformat(v["end"]) - date.fromisoformat(v["start"])).days
                    if not (350 <= d <= 380): continue
                else:
                    if "start" in v: continue
                    if v["end"][5:] not in ("12-31",): continue
                fy = int(v["end"][:4])
                # prefer the first tag in list that has the year; within a tag prefer latest filed
                prev = out.get(fy)
                if prev and prev[2] != t and tags.index(prev[2]) < tags.index(t): continue
                if prev and prev[2] == t and prev[1] >= v["filed"]: continue
                out[fy] = (v["val"]/1e6, v["filed"], t)
    return {k: v[0] for k, v in out.items()}
REV = ["Revenues","RevenueFromContractWithCustomerIncludingAssessedTax","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueServicesNet"]
PTI = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest","IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]
INT = ["InterestExpense","InterestExpenseNonoperating","InterestExpenseDebt","InterestPaidNet"]
EQ = ["StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest","StockholdersEquity"]
GW = ["Goodwill"]; IA = ["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"]
CASH = ["CashAndCashEquivalentsAtCarryingValue"]; STI = ["ShortTermInvestments","MarketableSecuritiesCurrent"]
LTD = ["LongTermDebtNoncurrent","LongTermDebtAndCapitalLeaseObligations"]; CUR = ["LongTermDebtCurrent","DebtCurrent","ShortTermBorrowings","LongTermDebtAndCapitalLeaseObligationsCurrent","ShortTermBorrowingsAndCurrentPortionOfLongTermDebt"]
for name in sys.argv[1:]:
    g = load(name)
    rev, pti, it = series(g, REV), series(g, PTI), series(g, INT); oi = series(g, ["OperatingIncomeLoss"])
    eq, gw, ia, ca, st, ltd = [series(g, x, flow=False) for x in (EQ, GW, IA, CASH, STI, LTD)]
    cur = {}
    for t in CUR:
        s = series(g,[t],flow=False)
        for k,v in s.items(): cur.setdefault(k,{})[t]=v
    print("==", name)
    tot_e = tot_c = tot_r = 0
    for y in range(2017, 2026):
        if y not in rev or y not in pti: continue
        ebit = oi[y] if y in oi else pti[y] + it.get(y, 0)
        c = cur.get(y, {}); curd = c.get("DebtCurrent", c.get("ShortTermBorrowingsAndCurrentPortionOfLongTermDebt", c.get("LongTermDebtCurrent",0)+c.get("ShortTermBorrowings",0)))
        cap = eq.get(y,0) + ltd.get(y,0) + curd - ca.get(y,0) - st.get(y,0) - gw.get(y,0) - ia.get(y,0)
        print(f"{y} rev {rev[y]:9,.0f} pti {pti[y]:8,.0f} int {it.get(y,0):6,.0f} ebit {ebit:8,.0f} m {100*ebit/rev[y]:5.1f}% tangcap {cap:8,.0f} ret {100*ebit/cap if cap>0 else float('nan'):6.1f}%  eq {eq.get(y,0):,.0f} gw {gw.get(y,0):,.0f} ia {ia.get(y,0):,.0f} ltd {ltd.get(y,0):,.0f} curd {curd:,.0f} cash {ca.get(y,0)+st.get(y,0):,.0f}")
