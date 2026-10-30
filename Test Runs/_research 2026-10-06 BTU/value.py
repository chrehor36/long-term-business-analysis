# COMPUTATION - NOT A CLEARANCE. Arithmetic for the reporting items the owner asked for.
r = 0.0566                     # 30-yr UST par, 2026-10-05 (tools/sources.py)
sh = 121.9                     # millions, 10-Q cover, 2026-08-03
price = 25.50
cash, debt = 526.3, 325.5+13.5 # 10-Q 2026-06-30
netcash = cash - debt
def pv(c, g, r=r, n=10):
    v = 0; ct = c
    for t in range(1, n+1):
        ct = ct*(1+g); v += ct/(1+r)**t
    return v + ct/r/(1+r)**n   # zero nominal growth after year 10
# owner cash, filed: OCF - SBC - capex - NCI distributions (USD M)
yrs = [2021,2022,2023,2024,2025]
ocf = [420.0,1173.6,1035.5,606.5,333.7]; sbc=[10.0,8.4,6.9,7.3,13.8]
capex=[183.1,221.5,348.3,401.3,411.4]; dna=[308.7,317.6,321.4,343.0,384.5]; nci=[4.0,17.5,59.0,34.8,22.9]
oe = [o-s-c-n for o,s,c,n in zip(ocf,sbc,capex,nci)]
oed = [o-s-d-n for o,s,d,n in zip(ocf,sbc,dna,nci)]
print("owner cash capex basis", [round(x,1) for x in oe], "avg", round(sum(oe)/5,1))
print("owner cash D&A basis  ", [round(x,1) for x in oed], "avg", round(sum(oed)/5,1))
# post-emergence 2018-2025
ocf8=[1489.7,677.4,-9.7]+ocf; sbc8=[34.9,38.3,13.5]+sbc; cap8=[301.0,285.4,191.4]+capex
oe8=[o-s-c for o,s,c in zip(ocf8,sbc8,cap8)]
print("2018-2025 owner cash (before NCI)", [round(x,1) for x in oe8], "avg", round(sum(oe8)/8,1))
g_vol = (121.9/229.2)**(1/14)-1   # mining tons sold 2011 -> 2025
print("volume trend 2011-2025", round(g_vol*100,2), "%/yr")
def show(label, c):
    lo = pv(c, g_vol); hi = pv(c, 0.0)
    print(f"{label}: C={c:.0f}  no-growth ${(hi+netcash)/sh:.2f}  decline ${(lo+netcash)/sh:.2f}  width {hi/lo:.2f}x  (equity, incl. net cash {netcash:.0f})")
    return lo, hi
show("Convention window 2021-2025", sum(oe)/5)
# whole-cycle: average segment margins per ton over 2014-16, 2018-25 x 2025 volumes
m = {"ST":[12.59,9.64,10.23,23.68,16.85,8.59,20.45,41.42,37.28,26.17,14.42],
     "SM":[-8.79,-1.16,-1.22,40.09,17.32,-23.11,32.28,117.86,63.48,22.20,6.57],
     "PRB":[3.57,3.48,3.36,2.37,2.05,2.23,1.53,0.83,1.76,1.74,2.08],
     "OUS":[12.29,12.69,11.90,7.69,8.18,9.22,9.71,13.19,12.79,10.34,5.33]}
vol = {"ST":15.4,"SM":8.6,"PRB":84.5,"OUS":13.4}
seg = 0
for k in m:
    a = sum(m[k])/len(m[k]); seg += a*vol[k]; print(k, "avg margin/ton", round(a,2), "x", vol[k], "=", round(a*vol[k],1))
corp = -80.0; capx = 375.0; legacy = 70.0; sbcn = 14.0; ncin = 27.6
aus_ebitda = (sum(m["ST"])/11)*vol["ST"] + (sum(m["SM"])/11)*vol["SM"]; aus_dda = 122.8+123.8
tax = max(0,(aus_ebitda-aus_dda))*0.30
pre = seg + corp - capx - legacy - sbcn - ncin
post = pre - tax
print(f"segment EBITDA {seg:.0f}; pre-tax owner cash {pre:.0f}; Aus tax {tax:.0f}; after-tax owner cash {post:.0f}")
lo, hi = show("Whole-cycle variant", post)
# floor: ~10% pre-tax on equity; central case growth = midpoint of the two ends
gc = g_vol/2
fair_eq = pre/(0.10 - gc)          # Gordon-style: yield + growth = 10%
print(f"central growth {gc*100:.2f}%  fair (equity, pre-tax 10%) ${fair_eq/sh:.2f}  + net cash -> ${(fair_eq+netcash)/sh:.2f}")
fair_flat = pre/0.10
print(f"fair if flat ${ (fair_flat+netcash)/sh:.2f}")
print(f"cheap (half of whole-cycle bottom) ${ (lo+netcash)/sh/2:.2f}")
print("pre-tax yield at price, whole-cycle:", round(pre/(price*sh-netcash)*100,2), "%")
print("market cap", round(price*sh,1), "EV", round(price*sh-netcash,1))
