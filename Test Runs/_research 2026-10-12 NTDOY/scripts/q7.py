# NTDOY run 2026-10-12: owner cash series and the Q7 COMPUTATION, by hand from the annual reports (millions of yen).
# Sources: Annual Reports 2014, 2016, 2018, 2020, 2022, 2024, 2026 (consolidated statements of cash flows, key financial data).
FY = list(range(2013, 2027))
sales = [635422,571726,549780,504459,489095,1055682,1200560,1308519,1758910,1695344,1601677,1671865,1164922,2313051]
op    = [-36410,-46425,24770,32881,29362,177557,249701,352370,640634,592760,504375,528941,282553,360117]
tax   = [.379,.379,.355,.33,.308,.308,.305,.305,.305,.305,.305,.305,.305,.305]  # statutory rate, each report's tax note
dep   = [12637,9918,9011,9139,8366,9064,9564,9557,10798,10527,11040,17856,15361,15854]
capex = [9488,19540,4582,4670,10458,9609,10736,9843,7011,7587,22190,16123,19008,27169]
dAR   = [1691,20374,-24198,15444,-65706,51585,-8416,-55372,-527,8134,31513,37995,27876,-74786]
dInv  = [-83608,35529,88204,34501,-155,-107454,8484,43230,7244,-84563,-45792,123853,-333837,-27591]
dAP   = [20738,-56940,3558,-21556,51528,9368,-51349,20832,22002,25125,9025,-75315,57564,79700]
intinc= [None]*9 + [4525,27369,54271,57626,53145]  # interest and dividend income, CF statement add-back, FY2022-26
oc = {}; ocm = {}
print("FY    sales     op  opAfterTax   dep  capex     dWC  ownerCash  OC/sales  OCmaint")
for i, y in enumerate(FY):
    wc = dAR[i] + dInv[i] + dAP[i]
    oat = op[i] * (1 - tax[i])
    oc[y] = oat + dep[i] - capex[i] + wc
    ocm[y] = oat + wc  # maintenance case: capex replaced by depreciation (dep - dep)
    print(f"{y} {sales[i]:>9,} {op[i]:>8,} {oat:>10,.0f} {dep[i]:>6,} {capex[i]:>6,} {wc:>8,} {oc[y]:>10,.0f} {oc[y]/sales[i]:>8.1%} {ocm[y]:>9,.0f}")
avg = lambda ys, d=oc: sum(d[y] for y in ys) / len(ys)
win = range(2022, 2027); swc = range(2018, 2026); wiiu = range(2013, 2018)
print("literal window FY2022-26 avg owner cash", round(avg(win)))
print("Switch cycle FY2018-25 avg owner cash", round(avg(swc)), " maint", round(avg(swc, ocm)))
print("Wii U cycle FY2013-17 avg owner cash", round(avg(wiiu)))
s_avg = lambda ys: sum(sales[FY.index(y)] for y in ys) / len(ys)
print("sales avg WiiU", round(s_avg(wiiu)), "Switch", round(s_avg(swc)), "growth p.a. (mid FY2015 -> mid FY2021.5)", (s_avg(swc)/s_avg(wiiu))**(1/6.5)-1)
h1, h2 = range(2018, 2022), range(2022, 2026)
print("halves FY2018-21", round(avg(h1)), "FY2022-25", round(avg(h2)), "growth p.a. (4 yrs apart)", (avg(h2)/avg(h1))**(1/4)-1)
print("max OC/sales in filings read", max(oc[y]/sales[FY.index(y)] for y in FY))
# Wii/DS cycle operating profit FY2008-12 (Annual Report 2012 five-year summary), for a peak-to-peak beside
wii_op = [487220,555263,356567,171076,-37320]
print("op profit avg Wii cycle FY2008-12", sum(wii_op)/5, "Switch FY2018-25", sum(op[5:13])/8)

def value(c, g, r, n=10):
    pv = sum(c*(1+g)**t/(1+r)**t for t in range(1, n+1))
    return pv + c*(1+g)**n / r / (1+r)**n
r = 0.04085   # MOF 30-year JGB 2026-10-09
shares = 1287260000 - 134431295   # issued less treasury, 31 Mar 2026
cash = 1791802 + 425054 + (420875 - 278251)  # cash and deposits, securities, investment securities less associates
lease = 7512
netcash = cash - lease
price = 8146
print("shares", shares, "net cash", netcash, "per share", netcash*1e6/shares, "mkt cap", price*shares/1e6)
C = avg(swc); gshown = (avg(h2)/avg(h1))**(1/4)-1
gcap = min(gshown, r)
for label, c in (("cycle base FY2018-25", C), ("literal window FY2022-26", avg(win))):
    for g in (0.0, gcap):
        vb = value(c, g, r); v10 = value(c, g, 0.10)
        print(f"{label} g={g:.4f}: value at sovereign {vb:,.0f} -> per share {(vb+netcash)*1e6/shares:,.0f}; at 10% {v10:,.0f} -> {(v10+netcash)*1e6/shares:,.0f}")
# implied expected return at price on each case: solve r such that value + netcash = mkt cap
def irr(c, g):
    mc = price*shares/1e6 - netcash
    lo, hi = 0.001, 0.5
    for _ in range(100):
        m = (lo+hi)/2
        if value(c, g, m) > mc: lo = m
        else: hi = m
    return m
for g in (0.0, gcap):
    print(f"expected return at price, cycle base, g={g:.4f}: {irr(C, g):.4f}")
# equity-only: add after-tax interest and dividend income (5-yr avg FY2022-26) and drop net cash
ii = sum(intinc[9:14])/5*(1-.305)
for g in (0.0, gcap):
    v10 = value(C+ii, g, 0.10); vb = value(C+ii, g, r)
    print(f"equity-only g={g:.4f}: sovereign per share {vb*1e6/shares:,.0f}; at 10% per share {v10*1e6/shares:,.0f}")
fair_ae = (value(C,0,0.10)+value(C,gcap,0.10))/2 + netcash
fair_eq = (value(C+ii,0,0.10)+value(C+ii,gcap,0.10))/2
print("FAIR all-equity per share", fair_ae*1e6/shares, " equity-only", fair_eq*1e6/shares, " after-tax int income avg", ii)
print("ADS (1/4 share) at JPY/USD 158.06: fair", fair_ae*1e6/shares/4/158.06, fair_eq*1e6/shares/4/158.06)

# Beside (d): FY2025's launch inventory build replaced by the FY2018-24 average working-capital change
wc18_24 = sum(dAR[i]+dInv[i]+dAP[i] for i in range(5, 12)) / 7
oc_alt = dict(oc); oc_alt[2025] = op[12]*(1-tax[12]) + dep[12] - capex[12] + wc18_24
Ca = avg(swc, oc_alt)
print("FY2018-24 avg dWC", round(wc18_24), "alt FY2025 OC", round(oc_alt[2025]), "alt cycle avg", round(Ca))
for g in (0.0, gcap):
    print(f"alt g={g:.4f}: sovereign per share {(value(Ca,g,r)+netcash)*1e6/shares:,.0f}; 10% per share {(value(Ca,g,0.10)+netcash)*1e6/shares:,.0f}; return at price {irr(Ca,g):.4f}")
print("alt fair all-equity", ((value(Ca,0,.1)+value(Ca,gcap,.1))/2+netcash)*1e6/shares)
print("cycle-to-cycle shown growth WiiU->Switch", (avg(swc)/avg(wiiu))**(1/6.5)-1)
print("width", (value(C,gcap,r)+netcash)/(value(C,0,r)+netcash))
print("ten-year OC at shown 81%:", C*(1.81**10)/1e6, "trn yen vs FY2026 sales 2.3trn")
