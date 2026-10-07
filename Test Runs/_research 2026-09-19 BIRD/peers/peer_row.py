# BIRD run 2026-09-19, Q2 competitor row (recorded, not governing). Latest two fiscal years from each filer's
# companyfacts (transcription of the filed statements; operator rule 4 cross-check done on one figure by hand).
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
here = os.path.dirname(os.path.abspath(__file__))
TAGS = {"rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "RevenueFromContractWithCustomerIncludingAssessedTax"],
        "opinc": ["OperatingIncomeLoss"],
        "ocf": ["NetCashProvidedByUsedInOperatingActivities", "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
        "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets", "PaymentsForProceedsFromProductiveAssets"],
        "sbc": ["ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"],
        "debt": ["LongTermDebt", "LongTermDebtNoncurrent", "DebtInstrumentCarryingAmount", "LongTermDebtAndCapitalLeaseObligations"]}
def fyvals(f, tags, instant=False):
    out = {}
    for t in tags:
        for ns in ("us-gaap",):
            for x in f["facts"].get(ns, {}).get(t, {}).get("units", {}).get("USD", []):
                if not x["form"].startswith(("10-K", "20-F")) or x.get("fp") != "FY": continue
                if not instant:
                    s = x.get("start")
                    if not s: continue
                    days = (int(x["end"][:4]) - int(s[:4])) * 365 + (int(x["end"][5:7]) - int(s[5:7])) * 30
                    if days < 330 or days > 380: continue
                out.setdefault(x["end"], x["val"])
        if out: break
    return out
for t in ["CRWV", "NBIS", "APLD", "IREN", "QMLS"]:
    f = json.load(open(os.path.join(here, f"{t}_companyfacts.json")))
    d = {k: fyvals(f, v, instant=(k == "debt")) for k, v in TAGS.items()}
    ends = sorted(d["rev"])[-2:]
    print("==", t, f.get("entityName"))
    for e in ends:
        g = lambda k: d[k].get(e)
        r, o, c, cx, s = g("rev"), g("opinc"), g("ocf"), g("capex"), g("sbc")
        fmt = lambda v: "n/a" if v is None else f"{v/1e6:,.1f}"
        oc = None if None in (c, cx, s) else (c - s - cx)
        print(f"  FY end {e}: revenue {fmt(r)}  op income {fmt(o)} ({'' if None in (o,r) else f'{o/r:.1%}'})  OCF {fmt(c)}  capex {fmt(cx)}  SBC {fmt(s)}  OCF-SBC-capex {fmt(oc)} ({'' if None in (oc,r) else f'{oc/r:.1%}'} of revenue)")
