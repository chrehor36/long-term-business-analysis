import json, os, sys
from datetime import date
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import get as G
out = {}
for tk, cik in {"TSEM": 928876, "GFS": 1709048}.items():
    fn = os.path.join(HERE, "peers", f"{tk}_companyfacts.json")
    if not os.path.exists(fn):
        open(fn, "wb").write(G.get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"))
    f = json.load(open(fn))["facts"]
    ns = "us-gaap" if "us-gaap" in f else "ifrs-full"
    def ann(tags):
        r = {}
        for t in tags:
            if t not in f.get(ns, {}): continue
            for u, rows in f[ns][t]["units"].items():
                for x in rows:
                    if x.get("form") not in ("20-F", "10-K") or "start" not in x or "segment" in x: continue
                    d = (date.fromisoformat(x["end"]) - date.fromisoformat(x["start"])).days
                    if not 340 <= d <= 380: continue
                    y = x["end"][:4]
                    if y not in r or x["filed"] > r[y][1]:
                        r[y] = (x["val"] / 1e6, x["filed"], x["accn"], t)
            if r: break
        return r
    rev = ann(["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "Revenue"])
    gp = ann(["GrossProfit"])
    oi = ann(["OperatingIncomeLoss", "ProfitLossFromOperatingActivities"])
    capex = ann(["PaymentsToAcquirePropertyPlantAndEquipment", "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"])
    out[tk] = {"ns": ns}
    for y in sorted(rev):
        if y < "2014": continue
        g = gp.get(y); o = oi.get(y); c = capex.get(y)
        row = dict(rev=rev[y][0], gm=100*g[0]/rev[y][0] if g else None, om=100*o[0]/rev[y][0] if o else None,
                   capex_rev=100*c[0]/rev[y][0] if c else None, src=rev[y][2])
        out[tk][y] = row
        print(tk, y, {k: (round(v, 1) if isinstance(v, float) else v) for k, v in row.items()})
json.dump(out, open(os.path.join(HERE, "peers", "peers_out.json"), "w"), indent=1)
