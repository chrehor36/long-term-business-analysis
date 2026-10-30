from facts import load, annual
REV = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueServicesNet"]
def first(d, tags):
    out = {}
    for t in tags:
        for k, v in annual(d, t).items():
            out.setdefault(k, v)
    return out
def yr(k): return k[:4] if k[5:7] >= "06" else str(int(k[:4])-1)
for t in ["ACM","J","TTEK"]:
    d = load(t)
    rev = first(d, REV); oi = first(d, ["OperatingIncomeLoss"])
    eq = first(d, ["StockholdersEquity"]); ocf = first(d, ["NetCashProvidedByUsedInOperatingActivities"])
    capex = first(d, ["PaymentsToAcquirePropertyPlantAndEquipment"])
    gw = first(d, ["Goodwill"]); acq = first(d, ["PaymentsToAcquireBusinessesNetOfCashAcquired"])
    print(d["entityName"])
    print("  FYend       rev     opinc  margin   equity  goodwill   OCF   capex  acq")
    for k in sorted(rev):
        if k < "2015-06": continue
        r = rev[k][0]/1e6; o = oi.get(k,(None,))[0]
        o = o/1e6 if o is not None else float('nan')
        def g(x): v = x.get(k,(None,))[0]; return v/1e6 if v is not None else float('nan')
        print(f"  {k} {r:9.0f} {o:8.0f} {100*o/r:6.1f}% {g(eq):8.0f} {g(gw):8.0f} {g(ocf):6.0f} {g(capex):6.0f} {g(acq):6.0f}")
