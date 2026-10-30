import sys, json
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

RES = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK"
cik = "0000093556"
facts = sources.sec_facts(cik)

TAGS = {
    "ocf": ("NetCashProvidedByUsedInOperatingActivities",
            "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"),
    "capex": ("PaymentsToAcquirePropertyPlantAndEquipment",
              "PaymentsToAcquireProductiveAssets"),
    "dep": ("DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
            "DepreciationAndAmortization"),
    "sbc": ("ShareBasedCompensation", "AllocatedShareBasedCompensationExpense"),
    "ni":  ("NetIncomeLoss",),
    "rev": ("RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues",
            "RevenueFromContractWithCustomerIncludingAssessedTax", "SalesRevenueNet"),
    "acq": ("PaymentsToAcquireBusinessesNetOfCashAcquired",),
    "ap":  ("IncreaseDecreaseInAccountsPayable",),
    "inv": ("IncreaseDecreaseInInventories",),
    "ar":  ("IncreaseDecreaseInAccountsReceivable",),
    "div": ("PaymentsOfDividendsCommonStock", "PaymentsOfDividends"),
    "amort": ("AmortizationOfIntangibleAssets",),
    "deponly": ("Depreciation",),
    "intexp": ("InterestExpense", "InterestIncomeExpenseNet"),
    "restr": ("RestructuringCharges",),
    "taxpaid": ("IncomeTaxesPaidNet", "IncomeTaxesPaid"),
    "pretax": ("IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
               "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"),
    "opinc": ("OperatingIncomeLoss",),
    "gross": ("GrossProfit",),
}

for vintage in ("earliest", "newest"):
    print("=" * 108)
    print("VINTAGE:", vintage)
    out, tagsused = {}, {}
    for k, tags in TAGS.items():
        d, t, u = sources.annual(facts, tags, vintage=vintage)
        out[k], tagsused[k] = d, t
    years = sorted(set(out["ocf"]))
    hdr = ["FY", "ocf", "capex", "dep", "sbc", "ni", "rev", "acq", "dAP", "dInv", "dAR", "div", "restr"]
    print("  ".join(f"{h:>9}" for h in hdr))
    for y in years:
        row = [y]
        for k in hdr[1:]:
            key = {"dAP": "ap", "dInv": "inv", "dAR": "ar"}.get(k, k)
            v = out[key].get(y)
            row.append(f"{v:,.1f}" if v is not None else "-")
        print("  ".join(f"{str(x):>9}" for x in row))
    print()
    for k in TAGS:
        print(f"   {k:10s} <- {tagsused[k]}")
    json.dump(out, open(rf"{RES}\annual_{vintage}.json", "w"), indent=1)
