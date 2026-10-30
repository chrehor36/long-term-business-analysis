import json, sys
from fetch_core import *
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
tk = json.loads(get("https://www.sec.gov/files/company_tickers.json"))
want = ["META","PINS","SNAP","RDDT","RUM","DJT"]
cik = {v["ticker"]: v["cik_str"] for v in tk.values() if v["ticker"] in want}
REV = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax"]
out = []
for t in want:
    c = cik[t]; f = json.loads(get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c:010d}.json"))
    g = f["facts"]["us-gaap"]
    def ann(tag):
        r = {}
        for u, obs in g.get(tag, {}).get("units", {}).items():
            for o in obs:
                if o.get("form","").startswith("10-K") and o.get("start") and o["end"][:4] in ("2023","2024","2025"):
                    from datetime import date
                    d = (date.fromisoformat(o["end"]) - date.fromisoformat(o["start"])).days
                    if 350 < d < 380: r[o["end"][:4]] = (o["val"], o["accn"])
        return r
    rev = {}
    for tg in REV:
        for k, v in ann(tg).items(): rev.setdefault(k, v)
    oi = ann("OperatingIncomeLoss"); ocf = ann("NetCashProvidedByUsedInOperatingActivities"); sbc = ann("ShareBasedCompensation")
    for y in ("2023","2024","2025"):
        R = rev.get(y, (None,None)); O = oi.get(y, (None,None)); C = ocf.get(y,(None,None)); S = sbc.get(y,(None,None))
        m = (O[0]/R[0]*100) if R[0] and O[0] is not None else None
        out.append(f"{t} CIK {c} FY{y} revenue {R[0]} op income {O[0]} margin {m if m is None else round(m,1)} OCF {C[0]} SBC {S[0]} accn {R[1]}")
open(os.path.join(HERE,"peers_out.txt"),"w").write("\n".join(out)); print("\n".join(out))
