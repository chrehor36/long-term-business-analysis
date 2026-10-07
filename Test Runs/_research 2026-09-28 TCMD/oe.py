# Owner earnings, TCMD, from the FILED consolidated statements of cash flows (thousands; newest vintage).
# OE = operating cash - SBC - (c). Capex end: purchases of property and equipment + recurring patent/intangible
# costs (the 2018 $5,350K Sun Scientific licence/asset purchase and the 2026 $3,000K distribution-rights payment and
# LymphaTech are acquisitions, excluded and recorded). Depreciation end: filed depreciation of property and equipment
# only (excludes amortization of patents and acquired intangibles).
import sys
sys.stdout.reconfigure(encoding='utf-8')
D={ # year: OCF, SBC, PPE capex, patent/intangible costs (recurring), depreciation (filed/tag), total D&A, AR non-current change, earn-out FV change
2014:(-991,148,353,0,400,706,-381,0),
2015:(2399,316,592,23,500,827,-737,0),
2016:(7033,1889,775,58,600,799,-784,0),
2017:(4192,4235,3746,74,1500,1800,105,0),
2018:(9007,7974,4196,0,3300,3737,834,0),
2019:(2510,9824,5446,542,3000,3538,-2300,0),
2020:(2794,10689,2059,232,2400,2794,-5249,0),
2021:(2631,10173,2103,252,2300,3681,-3414,-200),
2022:(5209,9600,1780,140,2500,6268,-10214,11850),
2023:(35855,7547,2324,157,2700,6539,12125,-2475),
2024:(40655,7819,2392,117,3000,6792,10936,0),
2025:(42811,8357,2380,155,2900,6643,0,0),
}
H1_26=(2915,4040,2102,52); H1_25=(15174,4005,748,56)
CAP=22.73*22652286/1e3  # $K
rows={}
print('year   OCF    SBC   capex+pat  dep   OE_capex  OE_dep   ARnc')
for y,(o,s,c,p,d,da,ar,eo) in D.items():
    a=o-s-(c+p); b=o-s-d; rows[y]=(a,b)
    print(y, f'{o/1e3:7.1f} {s/1e3:6.1f} {(c+p)/1e3:7.1f} {d/1e3:5.1f} {a/1e3:8.1f} {b/1e3:8.1f} {ar/1e3:7.1f}')
ttm=[D[2025][i]+H1_26[i]-H1_25[i] for i in range(4)]
ttm_oe_c=ttm[0]-ttm[1]-(ttm[2]+ttm[3]); ttm_dep=2900+ (1.5*0)  # depreciation H1 not split; use FY2025 depreciation
print('TTM to 2026-06-30: OCF %.1f SBC %.1f capex+pat %.1f  OE capex end %.1f  OE dep end (FY25 dep 2.9) %.1f'%(ttm[0]/1e3,ttm[1]/1e3,(ttm[2]+ttm[3])/1e3,ttm_oe_c/1e3,(ttm[0]-ttm[1]-2900)/1e3))
print('cap $M %.1f'%(CAP/1e3))
ys=sorted(D)
print('\nTrailing windows ending 2025 (mean $M, yield on cap):')
for n in (1,2,3,4,5,7,10,12):
    w=ys[-n:]; a=sum(rows[y][0] for y in w)/n; b=sum(rows[y][1] for y in w)/n
    print(f' {n:2d}y {w[0]}-{w[-1]}: {a/1e3:6.1f} to {b/1e3:6.1f}  ({100*a/CAP:5.2f}% to {100*b/CAP:5.2f}%)')
# ex the non-current AR swing (the Medicare appeal backlog): add back the build, remove the release
print('\nSame, removing the non-current AR (Medicare appeals) swing from OCF:')
for n in (1,3,5,12):
    w=ys[-n:]; a=sum(rows[y][0]-D[y][6] for y in w)/n; b=sum(rows[y][1]-D[y][6] for y in w)/n
    print(f' {n:2d}y: {a/1e3:6.1f} to {b/1e3:6.1f}  ({100*a/CAP:5.2f}% to {100*b/CAP:5.2f}%)')
print('\nSums: 2014-2022 OE capex end %.1f; 2023-2025 %.1f; share of 12y sum carried by 2023-2025 %.0f%%'%(sum(rows[y][0] for y in ys if y<=2022)/1e3,sum(rows[y][0] for y in ys if y>=2023)/1e3,100*sum(rows[y][0] for y in ys if y>=2023)/sum(rows[y][0] for y in ys)))
print('SBC / OCF: '+', '.join(f'{y} {100*D[y][1]/D[y][0]:.0f}%' for y in ys if D[y][0]>0))
