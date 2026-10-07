import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
f = sources.sec_facts("0000012927")
for tags,label in [ (["StockIssuedDuringPeriodValueEmployeeBenefitPlan"],"401k stock (value $M)"),
                    (["WeightedAverageNumberOfDilutedSharesOutstanding"],"WA diluted shares"),
                    (["WeightedAverageNumberOfSharesOutstandingBasic"],"WA basic shares"),
                    (["StockholdersEquity"],"Shareholders equity $M"),
                    (["StockIssuedDuringPeriodSharesTreasuryStockReissued"],"treasury reissued shares"),
                  ]:
    d,used,unit = sources.annual(f, tags, vintage="newest")
    print(f"\n{label}  ({used}, {unit})")
    for e in sorted(d): print("  ", e, f"{d[e]:,.4f}" if unit!="USD" else f"{d[e]:,.1f}")
# instant facts: equity, debt, shares outstanding
def instant(tag, forms=("10-K","10-Q")):
    out={}
    n=f["facts"].get("us-gaap",{}).get(tag)
    if not n: return out
    for unit,pts in n["units"].items():
        for x in pts:
            if x.get("form") in forms and not x.get("start"):
                k=x["end"]; fl=x.get("filed","")
                if k not in out or fl>out[k][1]: out[k]=(x["val"],fl)
    return {k:v[0] for k,v in out.items()}
for t in ["StockholdersEquity","CommonStockSharesOutstanding","LongTermDebtNoncurrent","LongTermDebt","ContractWithCustomerLiability"]:
    d=instant(t)
    if d:
        print(f"\nINSTANT {t}")
        for k in sorted(d)[-14:]: print("  ",k, f"{d[k]:,.0f}")
