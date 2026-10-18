import json, sys
sys.path.insert(0, ".")
from facts import annual
REV = ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueServicesNet","RevenueFromContractWithCustomerIncludingAssessedTax","ContractsRevenue"]
rows = {}
for c in ["0000866273","0001361538","0000700923","0000100591"]:
    name, out = annual("cache/facts_%s.json" % c, REV + ["GrossProfit","OperatingIncomeLoss"])
    print(name)
    for f in sorted(out):
        r = next((out[f][t] for t in REV if t in out[f]), None)
        gp = out[f].get("GrossProfit"); oi = out[f].get("OperatingIncomeLoss")
        if r:
            print("  %s rev %8.1f  GM %6s  OM %6s" % (f, r/1e6, "%.1f%%" % (100*gp/r) if gp is not None else "-", "%.1f%%" % (100*oi/r) if oi is not None else "-"))
