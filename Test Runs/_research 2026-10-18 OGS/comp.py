import json, sys
def series(d, tag, form="10-K"):
    try: units = d["facts"]["us-gaap"][tag]["units"]
    except KeyError: return {}
    out = {}
    for u, rows in units.items():
        for r in rows:
            if r.get("form") != form: continue
            if "start" in r:
                from datetime import date
                s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
                if not (350 <= (e-s).days <= 380): continue
            y = r["end"][:7]
            if y not in out or r["filed"] < out[y][1]: out[y] = (r["val"], r["filed"], r["accn"])
    return out
for f in sys.argv[1:]:
    d = json.load(open(f)); print("==", d["entityName"])
    ni = series(d, "NetIncomeLoss"); eq = series(d, "StockholdersEquity")
    oi = series(d, "OperatingIncomeLoss"); cap = series(d, "PaymentsToAcquirePropertyPlantAndEquipment")
    da = series(d, "DepreciationDepletionAndAmortization") or series(d, "DepreciationAndAmortization") or series(d,"UtilitiesOperatingExpenseDepreciationAndAmortization")
    keys = sorted(k for k in ni if k >= "2015-09")
    for k in keys:
        prev = [p for p in eq if p < k]; 
        pk = max(prev) if prev else None
        roe = ni[k][0] / ((eq[k][0] + eq[pk][0]) / 2) if (k in eq and pk) else None
        print(k, f"NI {ni[k][0]/1e6:8.1f}", f"Eq {eq.get(k,(0,))[0]/1e6:8.1f}", f"ROE {roe*100:5.2f}%" if roe else "", f"capex {cap.get(k,(0,))[0]/1e6:8.1f}", f"D&A {da.get(k,(0,))[0]/1e6:7.1f}", ni[k][2])
