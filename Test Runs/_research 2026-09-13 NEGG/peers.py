import json, os, sys, time
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
HERE = os.path.dirname(os.path.abspath(__file__))
PEERS = {"AMZN": "0001018724", "BBY": "0000764478", "WMT": "0000104169", "EBAY": "0001065088",
         "NEGG": "0001474627"}
T = {
 "rev": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
 "cogs": ["CostOfGoodsAndServicesSold", "CostOfRevenue", "CostOfGoodsSold"],
 "gp": ["GrossProfit"],
 "opinc": ["OperatingIncomeLoss"],
 "ocf": ["NetCashProvidedByUsedInOperatingActivities"],
 "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"],
 "sbc": ["ShareBasedCompensation"],
}
out = {}
for tk, cik in PEERS.items():
    f = S.sec_facts(cik)
    row = {}
    for k, tags in T.items():
        try:
            vals, used, unit = S.annual(f, tags, vintage="newest")
        except TypeError:
            vals, used, unit = S.annual(f, tags)
        row[k] = {str(e): v for e, v in vals.items()}
    out[tk] = row
    print("\n==", tk)
    ends = sorted(set(row["rev"]))[-6:]
    for e in ends:
        rev = row["rev"].get(e); gp = row["gp"].get(e)
        if gp is None and row["cogs"].get(e) is not None and rev:
            gp = rev - row["cogs"][e]
        op = row["opinc"].get(e); ocf = row["ocf"].get(e); cx = row["capex"].get(e); sbc = row["sbc"].get(e)
        def pct(a): return f"{100*a/rev:.1f}%" if (a is not None and rev) else "n/a"
        print(e, f"rev {rev:,.0f}" if rev else "rev n/a", "GM", pct(gp), "OM", pct(op),
              "OCF", ocf, "capex", cx, "SBC", sbc,
              "OE(capex)/rev", pct((ocf - sbc - cx) if None not in (ocf, sbc, cx) else None))
json.dump(out, open(os.path.join(HERE, "peers_xbrl.json"), "w"), indent=1)
