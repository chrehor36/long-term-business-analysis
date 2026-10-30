# GAAP operating margin and (OCF - SBC - capex)/revenue by fiscal year, from each filer's own 10-K XBRL. Transcription and arithmetic only.
from xbrl_annual import load, annual
R = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"]
for t in ["AVGO","MRVL","NVDA","QCOM","MSFT","ORCL","VMW"]:
    f = load(t)
    rev = annual(f, R); op = annual(f, ["OperatingIncomeLoss"]); ocf = annual(f, ["NetCashProvidedByUsedInOperatingActivities"])
    sbc = annual(f, ["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"]); cx = annual(f, ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"])
    print(t, "accn of latest:", list(rev.values())[-1][3] if rev else "")
    line1, line2 = [], []
    for k in sorted(rev):
        if k < "2016": continue
        r = rev[k][0]
        if k in op: line1.append(f"{k[:7]} {100*op[k][0]/r:5.1f}%")
        if k in ocf and k in sbc and k in cx: line2.append(f"{k[:7]} {100*(ocf[k][0]-sbc[k][0]-cx[k][0])/r:5.1f}%")
    print("  op margin :", " | ".join(line1)); print("  OC margin :", " | ".join(line2))
    print("  revenue $M:", " | ".join(f"{k[:7]} {v[0]/1e6:,.0f}" for k, v in rev.items() if k >= "2016"))
