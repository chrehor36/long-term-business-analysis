# COMPUTATION, NOT A CLEARANCE. VELO, run of 2026-10-13. USD thousands. Figures from the filed cash-flow statements (latest filing for each year).
ocf={2020:-26446,2021:-56404,2022:-123962,2023:-105636,2024:-32677,2025:-27327}
sbc={2020:1455,2021:4368,2022:20148,2023:24931,2024:11810,2025:9509}   # 2024 as revised in the FY2025 10-K (15,363 as first filed)
capex={2020:401,2021:9619,2022:13822,2023:1046,2024:9,2025:2715}
intp={2020:461,2021:1417,2022:372,2023:9722,2024:1183,2025:1125}
rev={2020:18975,2021:27439,2022:78706,2023:77443,2024:41003,2025:45973}
yrs=range(2021,2026)
oe={y:ocf[y]-sbc[y]-capex[y] for y in ocf}            # equity-only: after interest paid
oeu={y:oe[y]+intp[y] for y in ocf}                    # all-equity: before interest
for y in sorted(ocf): print(y, 'owner cash (after int)',oe[y],' before int',oeu[y],' rev',rev[y], ' share of sales %.0f%%'%(100*oe[y]/rev[y]))
m=sum(oe[y] for y in yrs)/5; mu=sum(oeu[y] for y in yrs)/5
m3=sum(oe[y] for y in (2023,2024,2025))/3; mu3=sum(oeu[y] for y in (2023,2024,2025))/3
print('5y mean equity-only',round(m),'all-equity',round(mu)); print('3y mean',round(m3),round(mu3))
fh=(oe[2021]+oe[2022])/2; sh=(oe[2024]+oe[2025])/2; print('halves',fh,sh)
r=0.056; shares=32149.118  # thousands of shares, cover of 10-Q, 2026-08-07
cash=91144; debt=3197+4973; netdebt=debt-cash   # 2026-06-30 10-Q; operating leases left out (Livermore lease commenced 2026-07-01, not on the balance sheet)
price=7.99; mcap=price*shares
print('mcap',round(mcap),'net debt',netdebt)
def pv(c,rate): return c/rate   # no growth, zero nominal growth after year ten = perpetuity
for lab,base,b in (('all-equity 5y',mu,'ae'),('equity-only 5y',m,'eo'),('all-equity literal last year 2025',oeu[2025],'ae'),('all-equity 3y',mu3,'ae')):
    v=pv(base,r); ps=(v-netdebt)/shares if b=='ae' else v/shares
    f=pv(base,0.10); fps=(f-netdebt)/shares if b=='ae' else f/shares
    print(f'{lab}: value at sovereign {v/1000:.1f}M -> {ps:.2f}/sh ; at 10%: {f/1000:.1f}M -> {fps:.2f}/sh')
print('expected return at price on 5y all-equity base: %.1f%%'%(100*mu/(mcap+netdebt)))
print('expected return at price on 2025 alone: %.1f%%'%(100*oeu[2025]/(mcap+netdebt)))
