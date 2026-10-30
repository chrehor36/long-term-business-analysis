# COMPUTATION - NOT A CLEARANCE. Q7 convention arithmetic for MTCH, USD millions.
ocf ={2021:912.5,2022:525.7,2023:896.8,2024:932.7,2025:1080.4}
sbc ={2021:146.8,2022:203.9,2023:232.1,2024:267.4,2025:258.2}
cap ={2021:80.0,2022:49.1,2023:67.4,2024:50.6,2025:56.8}
dep ={2021:41.4,2022:43.6,2023:61.8,2024:87.5,2025:67.1}
tax ={2021:40.9,2022:46.4,2023:102.0,2024:145.5,2025:99.5}   # cash taxes paid net of refunds
oc={y:ocf[y]-sbc[y]-cap[y] for y in ocf}
ocd={y:ocf[y]-sbc[y]-dep[y] for y in ocf}
r=0.0566; sh=229.551; price=40.33; netdebt=3551.9-580.6-3.2
avg=sum(oc.values())/5; avgd=sum(ocd.values())/5; avgtax=sum(tax.values())/5
g=(oc[2025]/oc[2021])**0.25-1
oc_ws=dict(oc); oc_ws[2022]+=441.0; avg_ws=sum(oc_ws.values())/5
g_ws=(oc_ws[2025]/oc_ws[2021])**0.25-1
def pv(base,g,r=r,n=10):
    v=0;c=base
    for t in range(1,n+1):
        c=c*(1+g); v+=c/(1+r)**t
    return v + (c/r)/(1+r)**n
print('owner cash by year (capex):',{y:round(v,1) for y,v in oc.items()})
print('owner cash by year (D&A):',{y:round(v,1) for y,v in ocd.items()})
print(f'5yr avg capex basis {avg:.1f}  D&A basis {avgd:.1f}  avg cash tax {avgtax:.1f}  pretax {avg+avgtax:.1f}')
print(f'shown growth 2021->2025 aggregate {g*100:.2f}%')
for lab,b,gg in [('central',avg,g),('whole-cycle (2022 settlement added back)',avg_ws,g_ws),('D&A variant',avgd,(ocd[2025]/ocd[2021])**0.25-1)]:
    lo=b/r; hi=pv(b,gg)
    print(f'{lab}: base {b:.1f} g {gg*100:.2f}%  equity value {lo:.0f}..{hi:.0f}  per share {lo/sh:.2f}..{hi/sh:.2f}  width {hi/lo:.2f}x')
# equity plus net debt: add back after-tax interest (interest expense 2021-25 avg) at 21%
ie={2021:130.5,2022:145.5,2023:159.9,2024:160.1,2025:147.6}; aie=sum(ie.values())/5
unlev=avg+aie*(1-0.21)
print(f'net debt {netdebt:.0f}; avg interest {aie:.1f}; unlevered owner cash {unlev:.1f}; EV(no growth) {unlev/r:.0f} -> equity {unlev/r-netdebt:.0f} = {(unlev/r-netdebt)/sh:.2f}/sh')
# expected pre-tax return at price, equity basis
mc=price*sh
print(f'market cap {mc:.0f}; after-tax owner cash yield {avg/mc*100:.2f}%; pre-tax yield {(avg+avgtax)/mc*100:.2f}%; +g = {((avg+avgtax)/mc+g)*100:.2f}%')
# fair price: pretax yield + g = 10%
for lab,gg in [('shown growth',g),('no growth',0.0)]:
    P=(avg+avgtax)/(0.10-gg)/sh
    print(f'fair price ({lab}) where pre-tax owner cash yield + g = 10%: ${P:.2f}')
# EV basis fair: pretax unlevered = avg+avgtax+aie ; EV=that/(0.10-g) ; minus net debt
for lab,gg in [('shown growth',g),('no growth',0.0)]:
    EV=(avg+avgtax+aie)/(0.10-gg); print(f'fair price EV basis ({lab}): ${(EV-netdebt)/sh:.2f}')
lo=avg/r/sh
print(f'cheap (half of range bottom): ${lo/2:.2f}')
# implied growth at price (perpetual, equity, after tax)
print(f'perpetual growth implied at price: {(r-avg/mc)*100:.2f}%')
