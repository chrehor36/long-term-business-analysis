"""GFS annual series from companyfacts (ifrs-full, USD), newest vintage per period, for cross-check against the filed
statements read by hand. Transcription only."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(HERE, "companyfacts.json")))["facts"]["ifrs-full"]
def ann(tag, instant=False):
    if tag not in F: return {}
    out = {}
    for f in F[tag]["units"].get("USD", []):
        if f.get("form") != "20-F": continue
        if instant:
            if f["end"][5:] != "12-31" or "start" in f: continue
        else:
            if "start" not in f or f["start"][5:] != "01-01" or f["end"][5:] != "12-31" or f["start"][:4] != f["end"][:4]: continue
        y = int(f["end"][:4]); prev = out.get(y)
        if prev is None or f["filed"] > prev[1]: out[y] = (f["val"] / 1e6, f["filed"])
    return {k: v[0] for k, v in sorted(out.items())}
tags = {"rev": "Revenue", "gp": "GrossProfit", "opinc": "ProfitLossFromOperatingActivities", "ni": "ProfitLoss",
        "ocf": "CashFlowsFromUsedInOperatingActivities", "da": "DepreciationAndAmortisationExpense",
        "sbc": "AdjustmentsForSharebasedPayments"}
S = {k: ann(v) for k, v in tags.items()}
S["eq_parent"] = ann("EquityAttributableToOwnersOfParent", instant=True)
S["eq"] = ann("Equity", instant=True)
for y in range(2018, 2026):
    row = {k: S[k].get(y) for k in S}
    gm = row["gp"] / row["rev"] * 100 if row["gp"] and row["rev"] else None
    om = row["opinc"] / row["rev"] * 100 if row["opinc"] and row["rev"] else None
    print(y, {k: (round(v, 1) if v is not None else None) for k, v in row.items()}, "GM", gm and round(gm, 1), "OM", om and round(om, 1))
json.dump({k: {str(y): v for y, v in d.items()} for k, d in S.items()}, open(os.path.join(HERE, "series_out.json"), "w"), indent=1)
