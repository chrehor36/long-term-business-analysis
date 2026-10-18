import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from facts import series
REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax"]
PT = ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]
def pick(t, tags):
    out = {}
    for tag in tags:
        for k, v in series(t, tag).items():
            if k[5:] in ("12-31", "09-30", "10-02","09-27","09-29","09-28","10-01","10-03","09-30") or True:
                if k not in out: out[k] = (v[0], tag, v[2])
    return out
for t in sys.argv[1:]:
    rev = pick(t, REV); oi = pick(t, ["OperatingIncomeLoss"]); pt = pick(t, PT)
    ni = pick(t, ["NetIncomeLoss"]); eq = pick(t, ["StockholdersEquity"]); gw = pick(t, ["Goodwill"])
    print(t, "FYend  revenue  opinc  opm%  pretax  ptm%  NI  equity  goodwill  accn")
    for k in sorted(rev):
        if k < "2015" or k[5:7] not in ("12","09","10","01"): continue
        r = rev[k][0]/1e6
        o = oi.get(k, (None,))[0]; p = pt.get(k, (None,))[0]
        f = lambda x: "" if x is None else f"{x/1e6:9.0f}"
        g = lambda x: "" if x is None else f"{100*x/1e6/r:5.1f}"
        print(f"  {k} {r:9.0f} {f(o)} {g(o)} {f(p)} {g(p)} {f(ni.get(k,(None,))[0])} {f(eq.get(k,(None,))[0])} {f(gw.get(k,(None,))[0])} {rev[k][2]}")
