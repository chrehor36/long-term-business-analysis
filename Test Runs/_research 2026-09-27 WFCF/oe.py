# Owner earnings, the corpus's way [E2-23]: operating cash as filed (short-term investment purchases that the filer
# classed inside operating activities in FY2015-FY2020 removed), less stock compensation in full INCLUDING common stock
# issued for services, less (c) at two ends, less finance/capital lease principal. $K. No net-income proxy anywhere.
# (c) capex end = "Purchases of property and equipment" / "...and software development costs" plus purchased intangibles,
# accreditation and other long-term assets as filed; (c) D&A end = depreciation as filed (acquired-intangible amortisation
# excluded; FY2020-FY2025 depreciation is filed only as "approximately $0.x million" and tagged at that rounding).
import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
# FY: (OCF as filed, ST-investment line inside OCF, SBC, stock for services, capex, other LT/intangible purchases, depreciation, lease principal, PB dividend, acquisitions+investments cash, source 10-K accession)
D={
2008:(-438.537,0,3.410,0,70.951,0,32.114,0,0,0,'0001104659-09-021739'),
2009:(102.678,0,27.750,0,111.711,0,55.952,0,0,0,'0001104659-10-017623'),
2010:(430.885,0,0.063,14.300,58.337,18.007,77.828,0,0,0,'0001104659-11-013565'),
2011:(720.685,0,13.170,0,12.171,0,69.361,0,0,0,'0001387131-12-000837'),
2012:(334.714,0,29.325,0,73.876,13.664,58.300,8.300,0,214.774,'0001387131-13-000623'),
2013:(216.904,0,70.152,75.000,34.645,0,57.000,5.506,0,565.000,'0001387131-14-000736'),
2014:(589.992,0,88.060,75.000,74.852,65.000,96.200,4.174,0,345.926,'0001387131-15-000597'),
2015:(862.117,-251.717,117.696,0,26.312,0,100.200,4.397,0,0,'0001387131-17-001106 (restated column)'),
2016:(986.056,-481.387,121.871,78.750,445.847,0,112.600,9.047,0,1284.697,'0001387131-17-001106'),
2017:(657.219,-10.102,169.133,25.000,83.757,9.043,317.200,4.889,0,150.000,'0001387131-18-001346'),
2018:(1154.170,-5.390,161.128,0,366.691,8.131,372.300,8.699,100,1850.000,'0001387131-19-002315'),
2019:(2874.931,-12.500,162.405,0,369.200,0,472.600,6.634,120,1000.000,'0001387131-20-002583'),
2020:(2452,258,121,0,464,0,400,8,150,300,'0001493152-21-004235'),
2021:(3020,0,291,0,213,0,400,10,200,0,'0001493152-22-005648'),
2022:(2654,0,154,0,89,0,400,13,250,178,'0001493152-23-005851'),
2023:(2822,0,78,0,148,0,300,13,320,500,'0001493152-24-006846'),
2024:(2730,0,34,0,159,0,300,14,400,0,'0001493152-25-007682'),
2025:(1607,0,23,0,155,0,300,15,100,0,'0001493152-26-008155'),
}
rows={}
print('| FY | OCF as filed | less ST-inv line | SBC + stock for services | capex incl other LT | depreciation | lease principal | OE capex end | OE D&A end | Progressive Beef dividend inside | OE capex end ex PB | OE D&A end ex PB | acquisitions and investments (cash) | 10-K |')
print('|'+'---|'*14)
for y,(ocf,st,sbc,svc,cap,olt,dep,lp,pb,acq,acc) in D.items():
    base=ocf-st
    s=sbc+svc
    oe_c=base-s-(cap+olt)-lp
    oe_d=base-s-dep-lp
    rows[y]=(oe_c,oe_d,oe_c-pb,oe_d-pb,acq)
    print(f'| {y} | {ocf:,.1f} | {-st:,.1f} | {s:,.1f} | {cap+olt:,.1f} | {dep:,.1f} | {lp:,.1f} | {oe_c:,.1f} | {oe_d:,.1f} | {pb:,.0f} | {oe_c-pb:,.1f} | {oe_d-pb:,.1f} | {acq:,.1f} | `{acc}` |')
# TTM to 2026-06-30
ttm_ocf=1607+1460-1813; ttm_sbc=23+94-0; ttm_cap=155+155-63; ttm_lp=15+6-7; ttm_pb=100+0-50
print(f'TTM to 2026-06-30: OCF {ttm_ocf}, SBC {ttm_sbc}, capex {ttm_cap}, lease {ttm_lp}, PB div {ttm_pb}; OE capex end {ttm_ocf-ttm_sbc-ttm_cap-ttm_lp} ; ex PB {ttm_ocf-ttm_sbc-ttm_cap-ttm_lp-ttm_pb}; D&A end (dep ~300+/-) {ttm_ocf-ttm_sbc-300-ttm_lp-ttm_pb}')
cap_m=53730.564
print()
print('| window ending FY2025 | capex end | D&A end | capex end ex PB | D&A end ex PB | yield range on $53.7M (ex PB, both ends) | capex/dep |')
print('|---|---|---|---|---|---|---|')
allv=[]
for n in range(3,19):
    ys=[y for y in range(2025-n+1,2026)]
    a=sum(rows[y][0] for y in ys)/n; b=sum(rows[y][1] for y in ys)/n; c=sum(rows[y][2] for y in ys)/n; d=sum(rows[y][3] for y in ys)/n
    capx=sum(D[y][4]+D[y][5] for y in ys)/sum(D[y][6] for y in ys)
    allv+= [c,d]
    print(f'| {n}y FY{ys[0]}-25 | {a:,.0f} | {b:,.0f} | {c:,.0f} | {d:,.0f} | {min(c,d)/cap_m*100:.2f}% to {max(c,d)/cap_m*100:.2f}% | {capx:.2f} |')
print('combined range ex PB, every window 3-18y, both ends: %.0f to %.0f $K; yield %.2f%% to %.2f%%'%(min(allv),max(allv),min(allv)/cap_m*100,max(allv)/cap_m*100))
