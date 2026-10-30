# Owner earnings, continuing operations FY2015-FY2025, $M, from the filed cash-flow statements
# (k2017 for 2015-2017 continuing; k2019 2018-2019; k2021 2020-2021; k2022 2022; k2025 2023-2025)
# OE = OCF - SBC - (c); (c) capex end = purchases of PP&E + finance-lease principal; D&A end = depreciation and finance-lease amortization (acquired-intangible amortization excluded)
Y=list(range(2015,2026))
OCF=[20.823,-1.793,-5.793,-18.400,42.886,56.087,-5.811,17.540,53.455,55.051,67.283]
SBC=[1.743,1.809,1.200,0.281,1.709,3.088,3.216,3.702,3.672,5.061,5.564]
CAP=[6.831,2.292,2.851,3.797,8.585,14.013,13.262,22.829,18.291,20.799,20.177]
FL =[1.270,0.279,0.327,0.398,0.434,0.420,0.415,0.597,0.826,1.419,1.660]
DEP=[7.332,8.768,6.060,8.767,12.391,12.344,11.482,12.664,11.616,15.038,15.405]
cap=103.11*9637202/1e6
oc=[o-s-c-f for o,s,c,f in zip(OCF,SBC,CAP,FL)]
od=[o-s-d for o,s,d in zip(OCF,SBC,DEP)]
print('cap $M', round(cap,1))
print('FY  OCF  SBC  capex+FL  dep  OE_capex  OE_dep')
for i,y in enumerate(Y): print(y, OCF[i], SBC[i], round(CAP[i]+FL[i],3), DEP[i], round(oc[i],1), round(od[i],1))
def m(a,n): return sum(a[-n:])/n
for n in range(1,12):
    a,b=m(oc,n),m(od,n)
    print(f'{n}y FY{2026-n}-25: capex end {a:.1f} ({100*a/cap:.2f}%)  dep end {b:.1f} ({100*b/cap:.2f}%)')
print('rolling 5y:')
for s in range(0,7):
    a=sum(oc[s:s+5])/5; b=sum(od[s:s+5])/5
    print(f'  FY{Y[s]}-{Y[s+4]}: {a:.1f} / {b:.1f}')
# TTM to 2026-06-30: FY2025 + H1 2026 - H1 2025 (10-Q 0001437749-26-025050)
tocf=67.283+43.340-10.272; tsbc=5.564+3.703-2.692; tcap=20.177+7.688-7.165; tfl=1.660+1.195-0.803; tdep=15.405+8.288-7.278
a=tocf-tsbc-tcap-tfl; b=tocf-tsbc-tdep
print(f'TTM Jun-2026: OCF {tocf:.1f} SBC {tsbc:.1f} capex {tcap:.1f} FL {tfl:.1f} dep {tdep:.1f} -> {a:.1f} ({100*a/cap:.2f}%) / {b:.1f} ({100*b/cap:.2f}%)')
# share of the 5y sum at capex end
s5=sum(oc[-5:]); print('5y sum capex end', round(s5,1), {Y[-5+i]: round(100*oc[-5+i]/s5,1) for i in range(5)})
s5d=sum(od[-5:]); print('5y sum dep end', round(s5d,1), {Y[-5+i]: round(100*od[-5+i]/s5d,1) for i in range(5)})
s3=sum(oc[-3:]); print('3y share capex end', {Y[-3+i]: round(100*oc[-3+i]/s3,1) for i in range(3)})
# floor and sovereign arithmetic, COMPUTATION - NOT A CLEARANCE
sh=9.637202
for lab,(lo,hi) in {'5y':(min(m(oc,5),m(od,5)),max(m(oc,5),m(od,5))),'3y':(min(m(oc,3),m(od,3)),max(m(oc,3),m(od,3))),'11y':(min(m(oc,11),m(od,11)),max(m(oc,11),m(od,11))),'TTM':(min(a,b),max(a,b))}.items():
    print(lab, 'per share at 10%:', round(lo/0.10/sh,1), round(hi/0.10/sh,1), ' at 5.56%:', round(lo/0.0556/sh,1), round(hi/0.0556/sh,1), ' growth to 10% floor:', round(100*(0.10*cap-hi)/(cap+hi),2), round(100*(0.10*cap-lo)/(cap+lo),2), ' yield pts vs 5.56:', round(100*lo/cap-5.56,2), round(100*hi/cap-5.56,2))
