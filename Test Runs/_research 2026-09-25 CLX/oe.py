"""Owner earnings for CLX, by hand from the filed cash-flow statements. ARITHMETIC ONLY, no verdict.
Sources (Consolidated Statements of Cash Flows, each 10-K's Exhibit 99.1): FY2013 10-K 0001206774-13-003034 (FY2011-13),
FY2016 10-K 0001206774-16-006893 (FY2014-16), FY2019 10-K 0000021076-19-000012 (FY2017-19), FY2022 10-K
0000021076-22-000026 (FY2020-22), FY2025 10-K 0000021076-25-000039 (FY2023), FY2026 10-K 0000021076-26-000034 (FY2024-26).
OCF = net cash provided by CONTINUING operations where the filing separates it (FY2011-17), else total.
Construction (the framework's CONVENTION): OE = OCF - SBC - (c). (c) at two ends: D&A (the [E3-44] default) and total capex.
FY2026 OCF carries a one-time $476M payment to buy P&G's 20% of Glad ('Venture agreement payment'); shown both ways."""
rows={ # fy: (ocf, sbc, da, capex, acquisitions, divestiture proceeds)
2011:(690,32,173,228,0,747),2012:(620,27,178,192,93,0),2013:(777,35,182,194,0,0),2014:(786,36,177,137,0,0),
2015:(858,32,169,125,0,0),2016:(768,45,165,172,290,0),2017:(868,51,163,231,0,0),2018:(976,53,166,194,681,0),
2019:(992,43,180,206,0,0),2020:(1546,50,180,254,0,0),2021:(1276,50,211,331,85,0),2022:(786,52,224,251,0,0),
2023:(1158,73,236,228,0,0),2024:(695,74,235,212,0,17),2025:(981,81,219,220,0,128),2026:(612,48,247,207,2104,0)}
VENT={2026:476}
print('| FY | OCF | SBC | D&A | capex | OE (c)=D&A | OE (c)=capex | OE (c)=max(D&A,capex) | acquisitions | note |')
print('|---|---|---|---|---|---|---|---|---|---|')
oe={}
for y,(o,s,d,c,a,p) in rows.items():
    lo=o-s-max(d,c); da=o-s-d; cx=o-s-c
    oe[y]=(da,cx,lo)
    note='incl. -476 Glad buyout; ex it: %d / %d / %d'%(da+476,cx+476,lo+476) if y in VENT else ''
    print(f'| {y} | {o:,} | {s} | {d} | {c} | {da:,} | {cx:,} | {lo:,} | {a:,} | {note} |')
def win(a,b,adj=0):
    ys=range(a,b+1); n=len(ys)
    m=lambda k: sum(oe[y][k]+(VENT.get(y,0) if adj else 0) for y in ys)/n
    return m(0),m(1),m(2)
print()
print('| window | (c)=D&A | (c)=capex | (c)=max | same, Glad buyout added back |')
print('|---|---|---|---|---|')
for a,b,l in [(2024,2026,'3y FY2024-26'),(2022,2026,'5y FY2022-26'),(2017,2026,'10y FY2017-26'),(2011,2026,'16y FY2011-26'),(2020,2026,'7y FY2020-26'),(2015,2019,'5y FY2015-19 (pre-pandemic)')]:
    x=win(a,b); z=win(a,b,1)
    print(f'| {l} | {x[0]:,.0f} | {x[1]:,.0f} | {x[2]:,.0f} | {z[0]:,.0f} / {z[1]:,.0f} / {z[2]:,.0f} |')
acq=lambda a,b: sum(rows[y][4]-rows[y][5] for y in range(a,b+1))/(b-a+1)
print()
for a,b in [(2017,2026),(2011,2026),(2017,2025),(2011,2025)]:
    print(f'net acquisitions per year FY{a}-{b}: {acq(a,b):,.0f}')
