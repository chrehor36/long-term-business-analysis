"""Competitor row: FY sales, operating profit, operating cash flow, capex, stock pay from each company's own
10-K XBRL (companyfacts, transcription; accession printed so the filed statement can be checked).
Usage: python -I peers.py   (reads cache/<t>_companyfacts.json)"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
TAGS = {
    "sales": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"],
    "opinc": ["OperatingIncomeLoss"],
    "ocf": ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
    "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
}
def annual(facts, tag, fy_end):
    f = facts["facts"]["us-gaap"].get(tag)
    if not f:
        return None
    best = None
    for u in f["units"].get("USD", []):
        if u.get("form") == "10-K" and u.get("fp") == "FY" and u["end"] == fy_end and u.get("start", "")[:4] == fy_end[:4]:
            if best is None or u["filed"] < best["filed"]:
                best = u
    return best
for t in ["gd", "noc", "rtx"]:
    facts = json.load(open(os.path.join(HERE, "cache", f"{t}_companyfacts.json")))
    for fy in ["2025-12-31", "2024-12-31", "2023-12-31", "2022-12-31", "2021-12-31"]:
        row = {}
        acc = None
        for k, tags in TAGS.items():
            for tag in tags:
                u = annual(facts, tag, fy)
                if u:
                    row[k] = u["val"] / 1e6
                    acc = acc or u["accn"]
                    break
        if not row:
            continue
        s, o = row.get("sales"), row.get("opinc")
        oc = None
        if row.get("ocf") is not None and row.get("capex") is not None:
            oc = row["ocf"] - row.get("sbc", 0) - row["capex"]
        print(f"{t.upper():4} {fy[:4]} sales {s:>9,.0f} opinc {o if o is None else round(o):>7} margin "
              f"{(o / s * 100 if s and o else float('nan')):5.1f}%  ocf {row.get('ocf', float('nan')):>7,.0f} "
              f"sbc {row.get('sbc', float('nan')):>5,.0f} capex {row.get('capex', float('nan')):>6,.0f} owner cash "
              f"{(oc if oc is not None else float('nan')):>7,.0f} ({(oc / s * 100 if oc and s else float('nan')):4.1f}% of sales)  accn {acc}")
