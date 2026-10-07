# Owner earnings, CAH, from the FILED cash-flow statements ($M). Source vintage per row noted.
# cols: OCF, SBC, DA, capex, finlease_add, AR, INV, AP, other(incl SA units), amort_intang, acq, src
D={
2012:(1176,85,325,260,0,-129,-495,319,-129,79,174,'10-K FY2014'),
2013:(1727,93,397,195,0,216,-370,426,-281,121,2239,'10-K FY2014'),
2014:(2524,96,459,249,0,925,142,-196,-116,188,519,'10-K FY2014'),
2015:(2540,110,451,300,0,-870,-779,1948,153,191,503,'10-K FY2017'),
2016:(2971,111,641,465,0,-866,-1179,2815,-147,355,3614,'10-K FY2017'),
2017:(1184,96,717,387,0,-665,-673,564,-493,395,132,'10-K FY2019'),
2018:(2768,85,1032,384,0,-871,-1211,2574,415,574,6142,'10-K FY2020'),
2019:(2722,82,1000,328,0,-751,-551,1864,193,531,82,'10-K FY2020'),
2020:(1960,90,913,375,40,82,-409,-162,6550,512,0,'10-K FY2020'),
2021:(2429,89,783,400,45,-904,-1584,2325,452,428,3,'10-K FY2023'),
2022:(3175,81,692,387,28,-1405,-1204,3555,264,311,22,'10-K FY2024 (revised)'),
2023:(2844,96,692,481,42,-950,-412,2816,-997,281,10,'10-K FY2024 (revised)'),
2024:(3762,121,710,511,55,-996,1115,1824,-433,264,1190,'10-K FY2026'),
2025:(2397,244,790,547,107,-833,-1816,2732,-606,303,5250,'10-K FY2026'),
2026:(5174,367,956,649,32,-408,-488,3463,-906,361,1991,'10-K FY2026'),
}
rows={}
print('FY   OCF  SBC   D&A capex+FL  tradeWC  other | A_capex A_DA | B_capex B_DA | depr-only')
for y,(o,s,da,cx,fl,ar,inv,ap,oth,am,acq,src) in D.items():
    twc=ar+inv+ap
    c1=cx+fl
    A1=o-s-c1; A2=o-s-da; B1=o-twc-s-c1; B2=o-twc-s-da
    rows[y]=(A1,A2,B1,B2)
    print(f'{y} {o:5d} {s:4d} {da:5d} {c1:5d} {twc:7d} {oth:6d} | {A1:6d} {A2:6d} | {B1:6d} {B2:6d} | c_dep={da-am}  acq={acq}')
def w(a,b):
    ys=[y for y in rows if a<=y<=b]
    m=lambda k: sum(rows[y][k] for y in ys)/len(ys)
    A=(m(1),m(0)); B=(m(3),m(2))
    return len(ys),A,B
print()
for lab,a,b in [('3y FY2024-26',2024,2026),('5y FY2022-26',2022,2026),('7y FY2020-26',2020,2026),('10y FY2017-26',2017,2026),('15y FY2012-26',2012,2026),('FY2026 alone',2026,2026),('5y FY2017-21',2017,2021)]:
    n,A,B=w(a,b)
    print(f'{lab:14s} n={n}  A {A[0]:7.0f} to {A[1]:7.0f}   B {B[0]:7.0f} to {B[1]:7.0f}')
# sensitivity: FY2022 net cash tax refund of 766 (CARES carryback, disputed by IRS NOPA) removed
n,A,B=w(2022,2026)
print('5y with FY2022 tax refund removed: A',round(A[0]-766/5),'to',round(A[1]-766/5),' B',round(B[0]-766/5),'to',round(B[1]-766/5))
# trade working capital sums by window
for a,b in [(2022,2026),(2024,2026),(2012,2026)]:
    print(a,b,'trade WC cumulative',sum(D[y][5]+D[y][6]+D[y][7] for y in D if a<=y<=b),'other cumulative',sum(D[y][8] for y in D if a<=y<=b))
# total WC incl other, per year, sign check for the screen flag
for y in (2024,2025,2026):
    t=D[y][5]+D[y][6]+D[y][7]+D[y][8]; print(y,'total WC incl other',t,'AP',D[y][7],'OCF',D[y][0],'AP/OCF',round(D[y][7]/D[y][0],2))
