# FSTR 2026-10-13 run: Q7 COMPUTATION, NOT A CLEARANCE (the file closed at Q2).
# Every input is a filed figure (USD thousands) recorded in the run file with its accession.
OE = {  # operating cash (continuing) - stock pay - capex
 2017: 39372-1696-6149, 2018: 26536-3836-3658, 2019: 26242-3155-6026, 2020: 20549-1136-9179,
 2021: -810-1945-4620, 2022: -10576-2380-7633, 2023: 36956-4179-4513, 2024: 22632-3834-9791,
 2025: 35619-5056-10424}
CAPEX = {2018:3658,2019:6026,2020:9179,2021:4620,2022:7633,2023:4513,2024:9791,2025:10424}
DEP = {2018:8066,2019:7944,2020:7850,2021:8051,2022:8635,2023:9949,2024:9452,2025:9143}
INT = {2018:6134,2019:4911,2020:3761,2021:2956,2022:3340,2023:5528,2024:4992,2025:4889}  # interest expense, net
NETBUY = {2018:0,2019:0,2020:1156,2021:229-22707,2022:57852-8800,2023:1246,2024:416,2025:782}
SETTLE = {2018:0,2019:10000,2020:8000,2021:8000,2022:8000,2023:8000,2024:8000,2025:0}
T = 0.21            # federal statutory rate, used to put interest and the settlement after tax
SOV = 0.056         # 30-year Treasury par yield, 2026-10-09
FLOOR = 0.10        # Q7 floor CONVENTION
NETDEBT = 47993-5783   # 10-Q 2026-06-30: revolver 47,478 + finance leases 515, less cash 5,783
SHARES = 10519.763  # thousands, cover 2026-08-03
PRICE = 35.54
# Shelter: federal NOL 76,546 at 21% (80% limit, no expiry) and state NOL benefit 9,121 less allowance 1,997;
# used at about 3,400 + 1,500 a year of tax saved, so it runs out in about five years (inside ten).
def shelter(rate):
    fed, st = 76546*T, 9121-1997
    pv, yr = 0.0, 1
    while fed > 1e-6 or st > 1e-6:
        use_f = min(fed, 3400); use_s = min(st, 1500)
        pv += (use_f+use_s)/(1+rate)**yr; fed -= use_f; st -= use_s; yr += 1
    return pv
avg = lambda d, ys: sum(d[y] for y in ys)/len(ys)
def case(name, oe_eq, oe_all):
    out = {}
    for lbl, r in (('sov', SOV), ('floor', FLOOR)):
        ev = oe_all / r
        out[lbl+'_all'] = (ev - NETDEBT + shelter(r)) / SHARES
        out[lbl+'_eq'] = (oe_eq / r + shelter(r)) / SHARES
    eff_ev = PRICE*SHARES + NETDEBT - shelter(SOV)
    out['ret_at_price_all'] = oe_all / eff_ev
    print(f"{name:58s} OE eq {oe_eq:8.0f}  OE all {oe_all:8.0f} | value@5.6% all {out['sov_all']:6.2f} eq {out['sov_eq']:6.2f}"
          f" | @10% all {out['floor_all']:6.2f} eq {out['floor_eq']:6.2f} | yield at price {100*out['ret_at_price_all']:.1f}%")
    return out
cyc = range(2018, 2024); win = range(2021, 2026); last3 = range(2023, 2026)
print('shelter PV at 5.6%', round(shelter(SOV)), 'at 10%', round(shelter(FLOOR)))
print('cycle 2018-2023: OE', round(avg(OE,cyc)), 'interest', round(avg(INT,cyc)), 'netbuy sum', sum(NETBUY[y] for y in cyc),
      'OE sum', sum(OE[y] for y in cyc))
print('window 2021-2025: OE', round(avg(OE,win)), 'interest', round(avg(INT,win)), 'netbuy sum', sum(NETBUY[y] for y in win),
      'OE sum', sum(OE[y] for y in win))
print('halves of window:', (OE[2021]+OE[2022])/2, (OE[2024]+OE[2025])/2)
c = avg(OE,cyc); i = avg(INT,cyc)*(1-T)
central = case('CENTRAL: cycle 2018-23, organic pair, all spending, no growth', c, c+i)
w = avg(OE,win); iw = avg(INT,win)*(1-T)
case('beside: literal window 2021-25, organic pair', w, w+iw)
case('beside: window, default pair (net purchases deducted)', w-avg(NETBUY,win), w-avg(NETBUY,win)+iw)
case('beside: cycle, default pair (net purchases deducted)', c-avg(NETBUY,cyc), c-avg(NETBUY,cyc)+i)
dv = c-(avg(DEP,cyc)-avg(CAPEX,cyc))
case('beside: cycle, depreciation in place of capex', dv, dv+i)
st = c+avg(SETTLE,cyc)*(1-T)
case('beside: cycle, UPRR settlement added back after tax', st, st+i)
l3 = avg(OE,last3); i3 = avg(INT,last3)*(1-T)
case('beside: last three years 2023-25 (not a Q7 base)', l3, l3+i3)
need = FLOOR*(PRICE*SHARES+NETDEBT-shelter(FLOOR))
print('all-equity owner cash needed at no growth to earn 10% at the price:', round(need))
# Beside, not a Q7 case: the most favourable base carried at the company's own sales growth over the window
# (net sales 513,620 in 2021 to 540,009 in 2025), ten years, then flat, to show the floor test does not turn on growth.
g = (540009/513620)**(1/4)-1
def grow_val(c0, r, g, yrs=10):
    pv = sum(c0*(1+g)**t/(1+r)**t for t in range(1, yrs+1))
    return pv + c0*(1+g)**yrs/r/(1+r)**yrs
for r in (SOV, FLOOR):
    ev = grow_val(l3+i3, r, g)
    print(f'beside: last three years at sales growth {100*g:.2f}% for ten years, rate {r}: per share', round((ev-NETDEBT+shelter(r))/SHARES,2))
lo, hi = 0.0, 0.5
for _ in range(60):
    mid=(lo+hi)/2
    if grow_val(l3+i3, mid, g) > PRICE*SHARES+NETDEBT-shelter(mid): lo=mid
    else: hi=mid
print('expected return at the price on that most favourable case:', round(100*lo,2), '%')
