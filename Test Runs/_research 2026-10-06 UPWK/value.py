"""COMPUTATION - NOT A CLEARANCE. UPWK value cases per the v5 Q7 convention and variants (USD millions)."""
r = 0.0566; sh = 124.903; netcash = 476.040 + 138.204 - 360.998  # 2026-06-30, notes at principal
def pv(oc, g, r=r):
    s = sum(oc*(1+g)**t/(1+r)**t for t in range(1, 11))
    return s + oc*(1+g)**10/r/(1+r)**10
oc = {2021: 10.836-53.592-(1.027+5.110), 2022: (6.559+4.9)-75.501-(1.248+7.485),
      2023: 52.708-74.195-(0.692+12.659), 2024: 153.563-68.391-(3.528+10.916), 2025: 248.259-65.390-(5.790+19.349)}
for y,v in oc.items(): print(y, round(v,1))
m5 = sum(oc.values())/5; print("5yr mean", round(m5,1), "3yr mean", round((oc[2023]+oc[2024]+oc[2025])/3,1))
gsv = {2020: 2523.649, 2025: 4028.386, 2022: 4104.891}
g5 = (gsv[2025]/gsv[2020])**(1/5)-1; g3 = (gsv[2025]/gsv[2022])**(1/3)-1
print("GSV cagr 2020-25", round(g5*100,2), "2022-25", round(g3*100,2))
# 2025 adjusted: remove after-tax other income, charge deferred tax at full rate
adj25 = oc[2025] - 18.493 - 23.869*(1-0.246)
print("2025 adjusted owner cash", round(adj25,1), " netcash", round(netcash,1))
h1_26 = 69.893-29.544-(3.341+17.709); h1_25 = 109.479-28.249-(4.853+8.210)
ttm = oc[2025]-h1_25+h1_26; print("H1 26", round(h1_26,1), "H1 25", round(h1_25,1), "TTM Jun26", round(ttm,1))
def ps(ev): return (ev+netcash)/sh
for name, base in [("5yr mean", m5), ("2025 adjusted", adj25), ("TTM Jun-26", ttm)]:
    for g in (-0.04, 0.0, g3, g5):
        print(f"{name:14s} g={g*100:5.1f}%  EV {pv(base,g):8.0f}  $/sh {ps(pv(base,g)):6.2f}")
# fair price: pre-tax owner cash / 10% + net cash, zero growth (expected return = pre-tax yield)
for name, base in [("5yr mean", m5), ("2025 adjusted", adj25), ("TTM Jun-26", ttm)]:
    pre = base/(1-0.246); print("FAIR", name, "pre-tax", round(pre,1), "$/sh", round((pre/0.10+netcash)/sh,2))
print("price 8.36 implies EV", round(8.36*sh-netcash,1))
