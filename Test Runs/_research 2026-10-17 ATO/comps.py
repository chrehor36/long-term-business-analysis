import json, sys
def annual(f, tags, forms=("10-K",)):
    g = f["facts"].get("us-gaap", {})
    for t in tags:
        if t not in g: continue
        out = {}
        for unit, vals in g[t]["units"].items():
            for v in vals:
                if v.get("form") not in forms: continue
                if "start" in v:
                    from datetime import date
                    s = date.fromisoformat(v["start"]); e = date.fromisoformat(v["end"])
                    if not (350 <= (e - s).days <= 380): continue
                # keep first-filed (earliest filed) value per period end
                k = v["end"]
                if k not in out or v["filed"] < out[k][1]:
                    out[k] = (v["val"], v["filed"], v["accn"])
        if out: return t, out
    return None, {}
names = {"0000731802":"ATO","0001587732":"OGS","0001126956":"SR","0001193311":"Oncor"}
for cik, nm in names.items():
    f = json.load(open(f"cache/facts_{cik}.json"))
    tn, ni = annual(f, ["NetIncomeLoss","ProfitLoss","NetIncomeLossAvailableToCommonStockholdersBasic"])
    te, eq = annual(f, ["StockholdersEquity","MembersEquity","StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest","PartnersCapital"])
    to, ocf = annual(f, ["NetCashProvidedByUsedInOperatingActivities"])
    tc, cap = annual(f, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets","PaymentsForCapitalImprovements"])
    print(f"== {nm}  NI:{tn} EQ:{te} OCF:{to} CAPEX:{tc}")
    ends = sorted(ni)[-11:]
    prev = None
    for e in ends:
        n = ni[e][0]/1e6; q = eq.get(e,(None,))[0]
        qv = q/1e6 if q else None
        roe = n/((qv+prev)/2)*100 if (qv and prev) else None
        o = ocf.get(e,(None,))[0]; c = cap.get(e,(None,))[0]
        print(e, f"NI {n:8.1f}", f"EQ {qv:9.1f}" if qv else "EQ -", f"ROE(avg) {roe:5.1f}%" if roe else "", f"OCF {o/1e6:8.1f}" if o else "", f"CAPEX {c/1e6:8.1f}" if c else "", ni[e][2])
        prev = qv
