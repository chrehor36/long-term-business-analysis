import json, sys
from datetime import date
sys.stdout.reconfigure(encoding="utf-8")
exec(open("peer.py").read().split("for f in sys.argv")[0])
for f in sys.argv[1:]:
    d = json.load(open(f))["facts"]["us-gaap"]
    rev = series(d, ["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","SalesRevenueNet","SalesRevenueGoodsNet"])
    oi = series(d, ["OperatingIncomeLoss"]); assets = series(d, ["Assets"], flow=False)
    ys = [y for y in range(2016, 2026) if y in rev and y in oi and y in assets]
    m = [oi[y][0]/rev[y][0] for y in ys]; ra = [oi[y][0]/assets[y][0] for y in ys]
    print(f, ys[0], "-", ys[-1], f"mean op margin {sum(m)/len(m)*100:.1f}%", f"min {min(m)*100:.1f}% max {max(m)*100:.1f}%", f"mean opinc/assets {sum(ra)/len(ra)*100:.1f}%", f"sum opinc / sum rev {sum(oi[y][0] for y in ys)/sum(rev[y][0] for y in ys)*100:.1f}%")
