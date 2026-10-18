# COMPUTATION, NOT A CLEARANCE. MTRX Q7 arithmetic. USD millions. FY ends June 30.
# Inputs transcribed from XBRL company facts (10-K filings, accessions in the run file) and checked
# against the FY2026 10-K statements (0000866273-26-000057) for FY2024-FY2026.
OCF  = {2011:22.7,2012:2.9,2013:57.1,2014:77.0,2015:26.2,2016:33.6,2017:-18.7,2018:74.7,2019:41.4,2020:44.1,
        2021:-3.0,2022:-54.2,2023:10.2,2024:72.571,2025:117.471,2026:6.907}
SBC  = {2011:2.4,2012:3.5,2013:3.8,2014:5.7,2015:6.3,2016:6.3,2017:7.5,2018:8.6,2019:11.9,2020:9.9,
        2021:8.2,2022:7.9,2023:6.8,2024:7.745,2025:8.904,2026:7.145}
CAPEX= {2011:10.4,2012:13.5,2013:23.2,2014:23.6,2015:15.8,2016:13.9,2017:11.9,2018:8.7,2019:19.6,2020:18.5,
        2021:4.4,2022:3.3,2023:9.0,2024:6.994,2025:7.685,2026:5.483}
INTINC={2011:0.1,2012:0.0,2013:0.0,2014:0.1,2015:0.5,2016:0.2,2017:0.1,2018:0.4,2019:1.2,2020:1.3,
        2021:0.1,2022:0.1,2023:0.3,2024:1.339,2025:6.652,2026:7.717}
INTEXP={2011:0.8,2012:0.8,2013:0.8,2014:1.4,2015:1.2,2016:0.9,2017:2.2,2018:2.6,2019:1.3,2020:1.6,
        2021:1.6,2022:3.0,2023:2.0,2024:1.130,2025:0.518,2026:0.437}
DBIE = {2011:6.6,2012:-5.2,2013:32.6,2014:3.1,2015:-11.7,2016:-38.4,2017:5.2,2018:45.6,2019:-15.0,2020:-41.7,
        2021:-8.6,2022:11.3,2023:20.3,2024:85.872,2025:152.285,2026:-23.646}
REV  = {2011:628.5,2016:1311.9,2017:1197.5,2021:673.4,2022:707.8,2026:873.632}
r, floor = 0.0543, 0.10
shares = 28.291921
netdebt = -222.966      # borrowings 0, finance leases 0, less unrestricted cash; restricted 25.0 left out
price = 10.02
def oc(y):  return OCF[y]-SBC[y]-CAPEX[y]                  # owner cash after every real cost, after interest
def ocu(y): return oc(y)-INTINC[y]+INTEXP[y]              # before interest (all-equity basis)
def avg(f, ys): return sum(f(y) for y in ys)/len(ys)
def val(B, g, rate):
    v = 0.0
    for t in range(1, 11): v += B*(1+g)**t/(1+rate)**t
    return v + B*(1+g)**10/rate/(1+rate)**10
def ps_allequity(V): return (V - netdebt)/shares
def ps_equity(V):    return V/shares
print("owner cash by year (after interest | before interest | of which BIE change):")
for y in sorted(OCF): print("  FY%d  %7.1f  %7.1f  %7.1f" % (y, oc(y), ocu(y), DBIE[y]))
W  = range(2022, 2027); C1 = range(2011, 2017); C2 = range(2017, 2027)
cases = {}
cases["literal five-year window FY2022-26"] = (avg(ocu, W), avg(oc, W))
cases["cycle base FY2017-26 (ten years)"]    = (avg(ocu, C2), avg(oc, C2))
cases["prior cycle FY2011-16"]                = (avg(ocu, C1), avg(oc, C1))
exadv = lambda f: (lambda y: f(y) - DBIE[y])
cases["cycle base FY2017-26 before customer-advance build"] = (avg(exadv(ocu), C2), avg(exadv(oc), C2))
cases["window FY2022-26 before customer-advance build"]     = (avg(exadv(ocu), W), avg(exadv(oc), W))
for k,(bu,bl) in cases.items(): print("%-55s before interest %6.1f   after interest %6.1f" % (k, bu, bl))
# growth between successive cycle averages (midpoints FY2013.5 and FY2021.5, eight years)
g = (cases["cycle base FY2017-26 (ten years)"][0]/cases["prior cycle FY2011-16"][0])**(1/8)-1
gl= (cases["cycle base FY2017-26 (ten years)"][1]/cases["prior cycle FY2011-16"][1])**(1/8)-1
print("growth between cycle averages: before interest %.2f%%, after interest %.2f%%" % (100*g, 100*gl))
print("sales growth FY2011-16 avg to FY2017-26 avg:", end=" ")
print("(rev FY2016 %.0f, FY2026 %.0f)" % (REV[2016], REV[2026]))
def report(label, bu, bl, gu, glv):
    top_u, bot_u = val(bu, 0, r), val(bu, gu, r)
    top_l, bot_l = val(bl, 0, r), val(bl, glv, r)
    lo_u, hi_u = sorted([ps_allequity(top_u), ps_allequity(bot_u)])
    lo_l, hi_l = sorted([ps_equity(top_l), ps_equity(bot_l)])
    fair_u = (ps_allequity(val(bu,0,floor)) + ps_allequity(val(bu,gu,floor)))/2
    fair_l = (ps_equity(val(bl,0,floor)) + ps_equity(val(bl,glv,floor)))/2
    print("\n%s" % label)
    print("  all-equity range  $%6.2f to $%6.2f a share   fair (10%%) $%6.2f" % (lo_u, hi_u, fair_u))
    print("  equity-only range $%6.2f to $%6.2f a share   fair (10%%) $%6.2f" % (lo_l, hi_l, fair_l))
    for nm, B, G, f in (("no-growth", bu, 0, ps_allequity), ("decline", bu, gu, ps_allequity)):
        # does the case earn the floor at the price? compare the 10% value with the price
        print("  %-9s at 10%%: $%6.2f a share all-equity vs price $%.2f -> %s" % (nm, f(val(B,G,floor)), price,
              "earns the floor" if f(val(B,G,floor)) >= price else "below the floor"))
cb = cases["cycle base FY2017-26 (ten years)"]
report("CENTRAL: cycle base FY2017-26, top no-growth, bottom the decline between cycles", cb[0], cb[1], g, gl)
lw = cases["literal five-year window FY2022-26"]
report("LITERAL WINDOW FY2022-26 (series changes sign: no-growth case alone)", lw[0], lw[1], 0, 0)
ea = cases["cycle base FY2017-26 before customer-advance build"]
print("\nBESIDE, before customer-advance build: base before interest %.1f; no-growth whole-business value %.1f;"
      " cash less net contract liabilities (BIE 299.9 less CIE 29.2) = %.1f" % (ea[0], val(ea[0],0,r), 222.966-(299.947-29.231)))
print("  per share, no-growth value plus cash net of advances: $%.2f" % ((val(ea[0],0,r) + 222.966-(299.947-29.231))/shares))
print("market cap at price: %.1f; enterprise value (all-equity basis): %.1f" % (price*shares, price*shares+netdebt))

# ---- added: the cycle as the text defines it (owner cash defines the cycle; specific (a)) ----
REVALL = {2011:628.5,2012:739.0,2013:892.6,2014:1263.1,2015:1343.1,2016:1311.9,2017:1197.5,2018:1091.6,
          2019:1416.7,2020:1100.9,2021:673.4,2022:707.8,2023:795.0,2024:728.213,2025:769.286,2026:873.632}
ACQ = {2011:3.8,2012:0,2013:9.4,2014:51.6,2015:5.6,2016:13.0,2017:40.8,2018:1.7,2019:-3.9,2020:0,2021:0,
       2022:0,2023:-6.3,2024:0,2025:0,2026:0}   # cash paid for businesses net of businesses sold
print("\n==== the cycle by owner cash (specific (a)) ====")
print("owner-cash peaks FY2014 47.7, FY2018 57.4, FY2025 100.9; troughs FY2012 -14.1, FY2017 -38.1, FY2022 -65.4")
P = range(2019, 2026)      # last full cycle, peak FY2018 to peak FY2025
P0 = range(2015, 2019)     # prior cycle, peak FY2014 to peak FY2018
acqd = lambda f: (lambda y: f(y) - ACQ[y])
bP_u, bP_l = avg(acqd(ocu), P), avg(acqd(oc), P)
bP0_u = avg(acqd(ocu), P0)
print("last full cycle FY2019-25: before interest %.2f, after interest %.2f (acquisitions net of sales deducted)" % (bP_u, bP_l))
print("prior cycle FY2015-18: before interest %.2f (acquisitions deducted) -> sign change between cycles: growth meaningless" % bP0_u)
h1, h2 = range(2019, 2022), range(2023, 2026)
print("halves of the cycle: FY2019-21 %.2f, FY2023-25 %.2f before interest" % (avg(acqd(ocu), h1), avg(acqd(ocu), h2)))
s1, s2 = avg(lambda y: REVALL[y], h1), avg(lambda y: REVALL[y], h2)
gs = (s2/s1)**(1/4)-1
print("sales over the same halves: %.1f -> %.1f, growth %.2f%% a year (midpoints FY2020 to FY2024)" % (s1, s2, 100*gs))
print("owner cash share of sales, highest in the filings read: FY2025 %.1f%%" % (100*oc(2025)/REVALL[2025]))
report("CENTRAL (a): last full cycle FY2019-25, top no-growth, bottom the business's own sales growth (shown owner-cash growth cut, (f))",
       bP_u, bP_l, gs, gs)
print("range width top/bottom (all-equity, whole-business values): %.2f" % (val(bP_u,0,r)/val(bP_u,gs,r)))
print("D&A variant (capex below D&A every year FY2020-26; above in FY2019): base before interest with D&A in place of capex:")
DA = {2019:18.2,2020:19.1,2021:17.9,2022:15.3,2023:13.7,2024:11.023,2025:10.012,2026:8.640}
print("  FY2019-25 %.2f" % avg(lambda y: ocu(y)+CAPEX[y]-DA[y]-ACQ[y], P))
