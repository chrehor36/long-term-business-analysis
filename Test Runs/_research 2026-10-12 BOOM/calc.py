"""BOOM run 2026-10-12: arithmetic only (COMPUTATION, NOT A CLEARANCE). USD millions.
Sources: cash-flow statements of the 10-Ks 0000034067-26-000009 (FY2025: 2025, 2024, 2023) and
0000034067-24-000025 (FY2023: 2023, 2022, 2021); segment notes of those and 0000034067-22-000023,
0000034067-21-000015; 10-Q 0000034067-26-000048 (net debt, shares)."""
yrs=[2021,2022,2023,2024,2025]
ocf={2021:-12.812,2022:44.936,2023:65.927,2024:46.596,2025:53.534}
sbc={2021:6.574,2022:10.058,2023:10.270,2024:6.902,2025:5.542}
capex={2021:8.659,2022:18.584,2023:15.974,2024:17.284,2025:16.503}
ppe_sale={2021:1.019,2022:0.062,2023:0.344,2024:0.103,2025:0.047}
intpaid={2021:0.051,2022:6.236,2023:9.188,2024:7.486,2025:4.952}
nci={2021:0.0,2022:12.300,2023:13.515,2024:8.445+2.500,2025:6.400}
acq={2021:261.000+24.902,2022:2.404,2023:0,2024:0,2025:0}
da={2021:12.7,2022:51.2,2023:36.5,2024:35.0,2025:34.0}
sales={2021:260.115,2022:654.086,2023:719.188,2024:642.851,2025:609.840}
T=0.21
oc={y:ocf[y]-sbc[y]-capex[y]+ppe_sale[y] for y in yrs}            # equity basis, after interest
ocu={y:oc[y]+intpaid[y]*(1-T) for y in yrs}                         # all-equity, before interest
ocda={y:ocf[y]-sbc[y]-da[y] for y in yrs}
print("year  OCF   SBC  capex  ownercash(eq) +int(1-t)=unlev  NCIdist  unlev-NCI  eq-NCI  D&Avariant  acq   sales  unlev%sales")
for y in yrs:
    print(y, f"{ocf[y]:7.1f}{sbc[y]:6.1f}{capex[y]:7.1f}{oc[y]:10.1f}{ocu[y]:14.1f}{nci[y]:9.1f}{ocu[y]-nci[y]:10.1f}{oc[y]-nci[y]:8.1f}{ocda[y]:10.1f}{acq[y]:7.1f}{sales[y]:8.1f}{100*ocu[y]/sales[y]:9.1f}")
R=0.056; FL=0.10
def pv(c0,g,r):
    v=0;c=c0
    for t in range(1,11):
        c=c*(1+g); v+=c/(1+r)**t
    return v + c/r/(1+r)**10
sh=20.540949; price=5.66
nd=30.513; put=187.080-24.902
def show(label,c0,g,claims):
    lo_g=min(g,0.0); hi_g=max(g,0.0)
    ends=[(c0,0.0),(c0,g)]
    vals=[pv(c0,gg,R) for _,gg in ends]
    fair=[pv(c0,gg,FL) for _,gg in ends]
    ps=[(v-claims)/sh for v in vals]; fp=(sum(fair)/2-claims)/sh
    print(f"{label}: base {c0:.2f}, g {100*g:.1f}%: whole {min(vals):.1f}-{max(vals):.1f}; per share {min(ps):.2f} to {max(ps):.2f}; width {max(vals)/min(vals) if min(vals)>0 else float('nan'):.2f}; fair/share {fp:.2f}; claims {claims:.1f}")
    return ps,fp
avg=lambda d,ys: sum(d[y] for y in ys)/len(ys)
W5=yrs; W4=[2022,2023,2024,2025]
print()
# Default pair, literal window: acquisitions deducted, total growth credited
d5={y:ocu[y]-nci[y]-acq[y] for y in W5}
print("DEFAULT literal 2021-25 base (unlev, after NCI dist, acquisitions deducted):", round(avg(d5,W5),2))
d5e={y:oc[y]-nci[y]-acq[y] for y in W5}
print("DEFAULT literal equity-only base:", round(avg(d5e,W5),2))
# Combined-company window 2022-25 (merger year 2021 aberrational: Arcadia 8 days, no Arcadia sales recorded)
A={y:ocu[y]-nci[y] for y in W4}; Ae={y:oc[y]-nci[y] for y in W4}
def halves(d):
    h1=(d[2022]+d[2023])/2; h2=(d[2024]+d[2025])/2
    return h1,h2,(h2/h1)**0.5-1
for lab,d,claims in [("A all-equity (NCI dist deducted), net debt",A,nd),("A equity-only",Ae,0.0)]:
    h1,h2,g=halves(d); print(lab,"halves",round(h1,2),round(h2,2),"g",round(100*g,2))
    show(lab,avg(d,W4),g,claims)
# B: put exercised at floor value, net of note: Arcadia 100% to DMC, claim added
B={y:ocu[y] for y in W4}; Be={y:oc[y] for y in W4}
for lab,d,claims in [("B all-equity, put claim + net debt",B,nd+put),("B equity-only, put claim",Be,put)]:
    h1,h2,g=halves(d); print(lab,"halves",round(h1,2),round(h2,2),"g",round(100*g,2))
    show(lab,avg(d,W4),g,claims)
# the default pair inside the combined window (no acquisition after 2022 adj)
dA={y:ocu[y]-nci[y]-acq[y] for y in W4}
h1,h2,g=halves(dA); print("default pair in combined window g",round(100*g,2)); show("A default 2022-25",avg(dA,W4),g,nd)
print("market cap", round(sh*price,1), "EV(A)", round(sh*price+nd,1), "EV(B)", round(sh*price+nd+put,1))
print("max unlev owner cash share of sales", max(ocu[y]/sales[y] for y in W4))

print("\n--- the cap of specific (f): growth carried ten years against the highest share of sales of the same series ---")
sh1=(sales[2022]+sales[2023])/2; sh2=(sales[2024]+sales[2025])/2; gs=(sh2/sh1)**0.5-1
print("sales halves",round(sh1,1),round(sh2,1),"sales growth",round(100*gs,2))
for lab,d,claims in [("A all-equity",A,nd),("A equity-only",Ae,0.0),("B all-equity",B,nd+put),("B equity-only",Be,put),("A default 2022-25",dA,nd)]:
    h1,h2,g=halves(d); c0=avg(d,W4)
    mx=max(d[y]/sales[y] for y in W4)
    yr10=c0*(1+g)**10/sales[2025]
    cut = g>0 and yr10>mx
    gg = gs if cut else g
    print(f"{lab}: shown g {100*g:.1f}%, yr10 share {100*yr10:.1f}% vs max {100*mx:.1f}% -> {'CUT to sales growth' if cut else 'kept'} {100*gg:.1f}%")
    show("   "+lab,c0,gg,claims)

print("\n--- the reporting set (combined window 2022-25; growth after the cap of (f)) ---")
dAe={y:oc[y]-nci[y]-acq[y] for y in W4}; dB={y:ocu[y]-acq[y] for y in W4}; dBe={y:oc[y]-acq[y] for y in W4}
for lab,d,claims in [("A default all-equity (CENTRAL)",dA,nd),("A default equity-only",dAe,0.0),
                     ("A acq left out all-equity",A,nd),("A acq left out equity-only",Ae,0.0),
                     ("B default all-equity",dB,nd+put),("B default equity-only",dBe,put)]:
    h1,h2,g=halves(d); c0=avg(d,W4); mx=max(d[y]/sales[y] for y in W4)
    cut = g>0 and c0*(1+g)**10/sales[2025]>mx
    gg = gs if cut else g
    print(f"{lab}: shown g {100*g:.1f}% {'cut to '+format(100*gg,'.1f')+'%' if cut else 'kept'}")
    show("   ",c0,gg,claims)
print("\nliteral window 2021-25, default pair: all-equity base", round(avg(d5,W5),2), "; per-share value of the no-growth case",
      round((pv(avg(d5,W5),0,R)-nd)/sh,2), "; at 10%", round((pv(avg(d5,W5),0,FL)-nd)/sh,2))
print("depreciation-only variant 2024, 2025:", round(46.596-6.902-13.891,1), round(53.534-5.542-14.904,1), "vs capex basis", round(oc[2024],1), round(oc[2025],1))
print("book equity per share 2025:", round(242.050/sh,2))

print("\n--- beside: the cap read on all filings read (2019 consolidated owner cash 33.3 on sales 397.6 = 8.4%), i.e. A uncut ---")
for lab,d,claims in [("A default all-equity, uncut",dA,nd),("A default equity-only, uncut",dAe,0.0)]:
    h1,h2,g=halves(d); c0=avg(d,W4); print(lab, round(c0*(1+g)**10/sales[2025]*100,1),"% of 2025 sales in year ten")
    show("   ",c0,g,claims)
