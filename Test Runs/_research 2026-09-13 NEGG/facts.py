import json, os, sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\Screens")
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
HERE = os.path.dirname(os.path.abspath(__file__))
facts = json.load(open(os.path.join(HERE, "companyfacts.json")))
g = facts["facts"].get("us-gaap", {})

TAGS = ["NetCashProvidedByUsedInOperatingActivities",
        "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
        "DepreciationDepletionAndAmortization", "DepreciationAndAmortization",
        "DepreciationAmortizationAndAccretionNet", "Depreciation",
        "ShareBasedCompensation", "AllocatedShareBasedCompensationExpense",
        "PaymentsToAcquirePropertyPlantAndEquipment", "IncreaseDecreaseInAccountsPayable",
        "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "NetIncomeLoss",
        "PaymentsToAcquireProductiveAssets"]

for t in TAGS:
    if t not in g:
        continue
    rows = {}
    for unit, arr in g[t]["units"].items():
        for r in arr:
            if r.get("form") not in ("20-F", "20-F/A", "10-K", "10-K/A"):
                continue
            if "start" in r:
                from datetime import date
                d = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
                if not (340 <= d <= 380):
                    continue
            rows.setdefault(r["end"], []).append((r["filed"], r["form"], r["accn"], r["val"]))
    print("\n==", t)
    for end in sorted(rows):
        vs = sorted(set(rows[end]))
        print(" ", end, " | ".join(f"{v[3]/1e6:,.2f} ({v[1]} {v[2]} filed {v[0]})" for v in vs))

if len(sys.argv) > 1:
    import floor_screen as F
    ocf = F.annual(facts, F.OCF_TAGS)
    print("\nOCF annual() used by screen:", {k: round(v / 1e6, 2) for k, v in sorted(ocf.items())})
    series = [ocf[y] for y in sorted(ocf)[-9:]]
    print("last 9:", [round(s / 1e6, 2) for s in series], "mean", sum(series) / len(series) / 1e6)
    print("best_year_dependence", F.best_year_dependence(series))
    print("level_shift", F.level_shift(series))
    da = F.da_annual(facts)
    print("da_annual", {k: round(v / 1e6, 2) for k, v in sorted(da.items())})
    print("da flag", F.da_discontinuity_flag(facts))
    print("wc flag", F.working_capital_flag(facts) if hasattr(F, "working_capital_flag") else None)
    oe = F.owner_earnings(facts)
    print("owner_earnings", oe)
    print("oe_annual capex", {k: round(v / 1e6, 2) for k, v in sorted(F.oe_annual(facts, "capex").items())})
    print("oe_annual da", {k: round(v / 1e6, 2) for k, v in sorted(F.oe_annual(facts, "da").items())})
