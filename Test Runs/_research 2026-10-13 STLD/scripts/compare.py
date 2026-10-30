import sys; sys.path.insert(0, "scripts")
from annual import pick, ITEMS
REV = ["RevenueFromContractWithCustomerExcludingAssessedTax", "RevenueFromContractWithCustomerIncludingAssessedTax", "Revenues", "SalesRevenueNet", "SalesRevenueGoodsNet"]
def g(tk):
    d = {k: {y: v[0] / 1e6 for y, v in pick(tk, tags, dur).items()} for k, tags, dur in ITEMS}
    d["rev"] = {y: v[0] / 1e6 for y, v in pick(tk, REV).items()}
    return d
out = []
for tk in ["STLD", "NUE", "CLF", "CMC"]:
    d = g(tk)
    print(f"\n{tk}: pretax margin % | (pretax+interest)/(equity+debt-cash-goodwill) at year end %")
    rows = []
    for y in range(2015, 2026):
        try:
            rev = d["rev"][y]; pt = d["pretax"][y]; it = d["int"].get(y, 0)
            cap = d["equity"][y] + d["ltd"].get(y, 0) + d["ltdc"].get(y, 0) - d["cash"].get(y, 0) - d["gw"].get(y, 0)
            rows.append((y, rev, pt, it, cap))
            print(f"  {y}  rev {rev:8.0f}  pretax {pt:7.0f}  margin {100*pt/rev:6.1f}  RoTC {100*(pt+it)/cap:6.1f}  cap {cap:7.0f}")
        except KeyError as e:
            print("  ", y, "missing", e)
    for a, b in [(2016, 2025), (2021, 2025), (2016, 2020)]:
        rr = [r for r in rows if a <= r[0] <= b]
        if rr:
            print(f"  {a}-{b}: sum pretax/sum rev {100*sum(r[2] for r in rr)/sum(r[1] for r in rr):.1f}%  mean RoTC {sum(100*(r[2]+r[3])/r[4] for r in rr)/len(rr):.1f}%  (n={len(rr)})")
