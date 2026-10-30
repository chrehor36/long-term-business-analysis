import sys, os, json
sys.path.insert(0, os.path.join(os.getcwd(), "tools"))
import sources
OUT = "Test Runs/_research 2026-09-13 RGTI/peers"
T = ["RevenueFromContractWithCustomerExcludingAssessedTax","Revenues","RevenueFromContractWithCustomerIncludingAssessedTax",
     "NetCashProvidedByUsedInOperatingActivities","ShareBasedCompensation","PaymentsToAcquirePropertyPlantAndEquipment",
     "CostOfRevenue","CostOfGoodsAndServicesSold","OperatingExpenses","OperatingIncomeLoss","RevenueRemainingPerformanceObligation",
     "DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","InvestmentIncomeInterest","ResearchAndDevelopmentExpense"]
for tk in sys.argv[1:]:
    try:
        cik, name = sources.cik_for(tk)
    except Exception as e:
        print(tk, "no cik", e); continue
    cik = str(cik).zfill(10)
    p = os.path.join(OUT, tk + "_companyfacts.json")
    if not os.path.exists(p):
        f = sources.sec_facts(cik); json.dump(f, open(p, "w"))
    f = json.load(open(p)); g = f["facts"].get("us-gaap", {})
    print("=====", tk, cik, name)
    for t in T:
        if t not in g: continue
        rows = []
        for u, rs in g[t]["units"].items():
            for r in rs:
                if r.get("form") not in ("10-K","10-Q"): continue
                s = r.get("start"); e = r["end"]
                if s:
                    from datetime import date
                    d = (date.fromisoformat(e) - date.fromisoformat(s)).days
                    if not (330 <= d <= 380 or (170 <= d <= 190 and e >= "2025-06-01")): continue
                if e < "2021-12-01": continue
                rows.append((s, e, r["val"], r["filed"]))
        best = {}
        for s, e, v, fl in rows:
            k = (s, e)
            if k not in best or fl > best[k][1]: best[k] = (v, fl)
        print(" ", t, [(k[1] if k[0] is None else k[0][:7]+".."+k[1], round(v[0]/1e6,1)) for k, v in sorted(best.items(), key=lambda x: x[0][1])])
