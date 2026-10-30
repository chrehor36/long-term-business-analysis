import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

TAGS = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax",
        "RevenueFromContractWithCustomerIncludingAssessedTax","GrossProfit",
        "CostOfRevenue","CostOfGoodsAndServicesSold","OperatingIncomeLoss",
        "NetIncomeLoss","NetCashProvidedByUsedInOperatingActivities",
        "ShareBasedCompensation","CashAndCashEquivalentsAtCarryingValue",
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "DepreciationDepletionAndAmortization"]

def dump(tkr, cik, want_fy):
    f = sources.sec_facts(cik)
    us = f["facts"].get("us-gaap", {})
    out = {}
    for tag in TAGS:
        if tag not in us: continue
        for unit, items in us[tag]["units"].items():
            for it in items:
                if it.get("form") not in ("10-K",): continue
                if it.get("fp") != "FY": continue
                st, en = it.get("start"), it.get("end")
                if st:
                    from datetime import date
                    d0 = date.fromisoformat(st); d1 = date.fromisoformat(en)
                    if not (340 <= (d1-d0).days <= 380): continue
                key = (tag, en)
                prev = out.get(key)
                if prev is None or it["accn"] > prev["accn"]:
                    out[key] = {"v": it["val"], "accn": it["accn"], "fy": it.get("fy"), "filed": it.get("filed"), "frame": it.get("frame","")}
    print("=== " + tkr + " cik " + cik)
    for (tag, en) in sorted(out, key=lambda k: (k[1], k[0])):
        if en[:4] not in want_fy: continue
        r = out[(tag, en)]
        print("%-58s end=%s  %18.1fM  accn=%s filed=%s" % (tag, en, r["v"]/1e6, r["accn"], r["filed"]))

for t, fys in [("AMZN",{"2025"}),("GOOGL",{"2025"}),("AAPL",{"2025"}),("NFLX",{"2025"}),
               ("TTD",{"2025"}),("CMCSA",{"2025"}),("CHTR",{"2025"}),("WMT",{"2026"}),("ROKU",{"2025"})]:
    try:
        cik = sources.cik_for(t)[0]
        dump(t, cik, fys)
    except Exception as e:
        print(t, "ERR", repr(e))
