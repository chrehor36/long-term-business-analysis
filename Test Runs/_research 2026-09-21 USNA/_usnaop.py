import json
from datetime import date
f=json.load(open("Test Runs/_research 2026-09-21 USNA/companyfacts.json"))
def series(tags,dur=True,ns="us-gaap"):
    out={}
    for t in tags:
        d=f["facts"].get(ns,{}).get(t)
        if not d: continue
        for unit,vals in d["units"].items():
            for u in vals:
                if u.get("form") not in ("10-K","10-K/A"): continue
                s,e=u.get("start"),u["end"]
                if dur:
                    if not s: continue
                    n=(date.fromisoformat(e)-date.fromisoformat(s)).days
                    if not (340<=n<=380): continue
                else:
                    if s: continue
                p=out.get(e)
                if p is None or u["filed"]>p[1]: out[e]=(u["val"],u["filed"])
    return out
REV=series(["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","SalesRevenueNet","SalesRevenueGoodsNet"])
OPI=series(["OperatingIncomeLoss"])
EQ=series(["StockholdersEquity"],dur=False)
TAXPAID=series(["IncomeTaxesPaidNet","IncomeTaxesPaid"])
PRETAX=series(["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"])
TAXEXP=series(["IncomeTaxExpenseBenefit"])
NI=series(["NetIncomeLoss"])
print(f"{'FYend':12}{'Rev':>9}{'OpInc':>9}{'margin':>8}{'Pretax':>9}{'TaxExp':>8}{'ETR':>7}{'CashTax':>9}{'cash/ptx':>9}{'NI':>8}{'Equity':>9}{'ROE':>7}")
for k in sorted(REV):
    g=lambda D:(D[k][0]/1e6 if k in D else None)
    r,o,px,te,ct,ni,eq=g(REV),g(OPI),g(PRETAX),g(TAXEXP),g(TAXPAID),g(NI),g(EQ)
    def F(x,w=9,d=1): return (f"{x:{w}.{d}f}" if x is not None else f"{'-':>{w}}")
    m=(100*o/r if o and r else None); etr=(100*te/px if te and px else None)
    cp=(100*ct/px if ct and px else None); roe=(100*ni/eq if ni and eq else None)
    print(f"{k:12}{F(r)}{F(o)}{F(m,8)}{F(px)}{F(te,8)}{F(etr,7)}{F(ct)}{F(cp)}{F(ni,8)}{F(eq)}{F(roe,7)}")
