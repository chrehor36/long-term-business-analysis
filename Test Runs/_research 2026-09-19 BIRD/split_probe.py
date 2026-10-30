# BIRD run 2026-09-19: every share-count fact companyfacts carries for CIK 1653909, with the filing that carried it,
# to test whether pre- and post-split (1-for-20, effective 2024-09-04) counts sit side by side.
import json, os
here = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(here, "companyfacts.json")))
g = f["facts"].get("us-gaap", {})
for t in ("CommonStockSharesOutstanding", "CommonStockSharesIssued", "WeightedAverageNumberOfSharesOutstandingBasic",
          "WeightedAverageNumberOfDilutedSharesOutstanding", "StockIssuedDuringPeriodSharesNewIssues"):
    L = g.get(t, {}).get("units", {}).get("shares", [])
    print("==", t, len(L))
    for x in sorted(L, key=lambda x: (x.get("end"), x.get("filed"))):
        print("  ", x.get("start", ""), x.get("end"), f'{x["val"]:>14,}', x["form"], x["filed"], x["accn"], x.get("frame", ""))
