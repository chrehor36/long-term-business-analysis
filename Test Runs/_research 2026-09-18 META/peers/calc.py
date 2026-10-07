import json, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
T = {"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax"],
     "oi":["OperatingIncomeLoss"],
     "ocf":["NetCashProvidedByUsedInOperatingActivities"],
     "sbc":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
     "capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
     "flp":["FinanceLeasePrincipalPayments","RepaymentsOfLongTermCapitalLeaseObligations"]}
def ann(f, tags):
    out = {}
    g = f["facts"].get("us-gaap", {})
    for tg in tags:
        if tg not in g: continue
        for u in g[tg]["units"].get("USD", []):
            if u.get("form") != "10-K" or "start" not in u: continue
            s, e = date.fromisoformat(u["start"]), date.fromisoformat(u["end"])
            if not 350 <= (e - s).days <= 380: continue
            y = e.year
            if y < 2021 or y > 2025: continue
            if y not in out or u["filed"] > out[y][1]:
                if y in out and out[y][2] != tg: continue
                out[y] = (u["val"], u["filed"], tg)
    return {y: v[0]/1e6 for y, v in out.items()}
rows = []
for t in ["META","GOOGL","AMZN","SNAP","PINS","RDDT"]:
    f = json.load(open(f"{t}_companyfacts.json", encoding="utf-8"))
    d = {k: ann(f, v) for k, v in T.items()}
    print("==", t)
    for k in d: print("  ", k, {y: round(d[k][y],1) for y in sorted(d[k])})
    Y = [y for y in [2021,2022,2023,2024,2025] if y in d["rev"]]
    y0=Y[0]
    g = lambda k, y: d[k].get(y, 0.0)
    r5 = sum(g("rev",y) for y in Y); oi5 = sum(g("oi",y) for y in Y)
    oe5 = sum(g("ocf",y)-g("sbc",y)-g("capex",y)-g("flp",y) for y in Y)
    print(f"  5y rev {r5:,.0f}  oi margin {oi5/r5*100:.1f}%  FY25 oi margin {g('oi',2025)/g('rev',2025)*100:.1f}%  rev growth {y0}->25 {(g('rev',2025)/g('rev',y0))**(1/(2025-y0))*100-100:.1f}%/yr  FY25 growth {(g('rev',2025)/g('rev',2024)-1)*100:.1f}%")
    print(f"  5y OE(ocf-sbc-capex-flp) {oe5:,.0f} = {oe5/r5*100:.1f}% of rev; SBC/OCF 5y {sum(g('sbc',y) for y in Y)/sum(g('ocf',y) for y in Y)*100:.1f}%; capex/rev FY{y0} {g('capex',y0)/g('rev',y0)*100:.1f}% FY25 {g('capex',2025)/g('rev',2025)*100:.1f}%")
