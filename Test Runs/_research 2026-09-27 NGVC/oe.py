# NGVC owner earnings, arithmetic only. $M. Sources: companyfacts tags checked against filed statements (Step 0);
# lease-financed additions from each 10-K's supplemental non-cash disclosure (not tagged for 2011-2019, 2024-2025).
CAP=684.692
Y=list(range(2011,2026))
ocf={2011:16.74,2012:25.2,2013:25.72,2014:31.75,2015:41.0,2016:28.83,2017:40.85,2018:42.86,2019:37.38,2020:66.5,2021:53.88,2022:39.69,2023:64.61,2024:73.76,2025:55.304}
sbc={2011:0.0,2012:0.78,2013:0.6,2014:0.53,2015:0.57,2016:0.88,2017:0.76,2018:0.81,2019:1.19,2020:1.13,2021:0.88,2022:1.19,2023:1.36,2024:2.829,2025:3.96}
capex={2011:20.446,2012:25.259,2013:39.708,2014:36.51,2015:36.75,2016:53.759,2017:41.14,2018:23.69,2019:30.03,2020:26.75,2021:26.35,2022:28.04,2023:36.568,2024:37.541,2025:31.201}
intang={y:0 for y in Y}; intang.update({2017:0.09,2018:0.03,2019:2.7,2020:2.83,2021:1.94,2022:3.41,2023:1.525,2024:1.139,2025:0.178})
lease={2011:0,2012:5.526,2013:14.372,2014:2.300,2015:5.772,2016:4.438,2017:1.499,2018:8.285,2019:12.156,2020:11.625,2021:3.025,2022:9.625,2023:5.724,2024:-0.045,2025:7.419}
da={2011:7.69,2012:9.95,2013:13.5,2014:17.21,2015:21.34,2016:25.53,2017:29.51,2018:29.43,2019:28.98,2020:31.19,2021:29.63,2022:27.91,2023:28.91,2024:30.93,2025:31.81}
oc={y:ocf[y]-sbc[y]-capex[y]-intang[y]-lease[y] for y in Y}   # capex end, lease-financed additions included (the 2026-09-01 addendum)
ocx={y:ocf[y]-sbc[y]-capex[y]-intang[y] for y in Y}           # capex end, cash only (what the screen sees)
od={y:ocf[y]-sbc[y]-da[y] for y in Y}                          # D&A end
print('| FY | OCF | SBC | capex (PP&E) | intangibles | lease-financed additions | D&A | OE capex end (incl. leases) | OE capex end (cash only) | OE D&A end | capex+leases / D&A |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for y in Y:
    print(f'| {y} | {ocf[y]:.1f} | {sbc[y]:.2f} | {capex[y]:.1f} | {intang[y]:.2f} | {lease[y]:.1f} | {da[y]:.1f} | {oc[y]:.1f} | {ocx[y]:.1f} | {od[y]:.1f} | {(capex[y]+intang[y]+lease[y])/da[y]:.2f} |')
m=lambda d,ys: sum(d[y] for y in ys)/len(ys)
print('\nTrailing windows ending FY2025 (mean $M, and yield on cap $%.1fM):'%CAP)
lo=hi=None; allv=[]
for n in range(3,16):
    ys=Y[-n:]; a,b,c=m(oc,ys),m(ocx,ys),m(od,ys)
    allv+= [a,c]
    print(f'  {n:2d}y {ys[0]}-{ys[-1]}: capex end {a:6.1f} ({a/CAP*100:.2f}%) | cash-only {b:6.1f} | D&A end {c:6.1f} ({c/CAP*100:.2f}%)')
print(f'  RANGE over every trailing window 3-15y, both ends (leases included at capex end): {min(allv):.1f} to {max(allv):.1f} = {min(allv)/CAP*100:.2f}% to {max(allv)/CAP*100:.2f}%')
print('\nEvery rolling 5-year window (capex end incl. leases | D&A end):')
r=[]
for s in range(0,len(Y)-4):
    ys=Y[s:s+5]; a,c=m(oc,ys),m(od,ys); r+=[a,c]
    print(f'  {ys[0]}-{ys[-1]}: {a:6.1f} | {c:6.1f}')
print(f'  rolling-5y range, both ends: {min(r):.1f} to {max(r):.1f}')
print('\nEvery rolling 3-year window (capex end incl. leases | D&A end):')
for s in range(0,len(Y)-2):
    ys=Y[s:s+3]; print(f'  {ys[0]}-{ys[-1]}: {m(oc,ys):6.1f} | {m(od,ys):6.1f}')
# screen reproduction
for n in (3,5):
    ys=Y[-n:]
    print(f'screen check {n}y: cash capex end (PP&E only, no intangibles, no leases) {m({y:ocf[y]-sbc[y]-capex[y] for y in Y},ys):.1f}; D&A end {m(od,ys):.1f}')
# growth required at 5.49% for yields (no-growth perpetuity: value = OE / r) -- reported, not used for entry
