# Q7 arithmetic for STLD (COMPUTATION; inputs from the 10-K/10-Q figures transcribed in the run file)
ocf  = {2016:853,2017:739,2018:1415,2019:1396,2020:987,2021:2204,2022:4460,2023:3520,2024:1845,2025:1450}
sbc  = {2016:32,2017:36,2018:43,2019:48,2020:56,2021:58,2022:59,2023:62,2024:67,2025:69}
capex= {2016:198,2017:165,2018:239,2019:452,2020:1198,2021:1006,2022:909,2023:1658,2024:1868,2025:948}
da   = {2016:296,2017:299,2018:317,2019:321,2020:326,2021:348,2022:384,2023:438,2024:479,2025:551}
acq  = {2016:123,2017:6,2018:434,2019:97,2020:60,2021:0,2022:134+222,2023:0,2024:0,2025:176}
intx = {2021:57,2022:92,2023:76,2024:56,2025:70}
sales= {2016:7607,2017:9364,2018:11802,2019:10451,2020:9588,2021:18409,2022:22261,2023:18795,2024:17540,2025:18177}
TAX=0.21; R=0.056; FLOOR=0.10
SH=143.328088; PRICE=240.63; NETDEBT=4180.810+1.332-567.708
allsp = {y: ocf[y]-sbc[y]-capex[y] for y in ocf}
maint = {y: ocf[y]-sbc[y]-da[y] for y in ocf}
allsp_acq = {y: allsp[y]-acq[y] for y in ocf}
avg = lambda d, ys: sum(d[y] for y in ys)/len(ys)
A = range(2016,2021); B = range(2021,2026)
print("owner cash all-spending by year", allsp)
print("owner cash maintenance (D&A proxy) by year", maint)
print("all-spending less acquisitions", allsp_acq)
print("highest share of sales: all-spending %.1f%% (%d), maintenance %.1f%% (%d)" % (max(100*allsp[y]/sales[y] for y in sales), max(sales, key=lambda y: allsp[y]/sales[y]), max(100*maint[y]/sales[y] for y in sales), max(sales, key=lambda y: maint[y]/sales[y])))
ai = avg(intx, B)*(1-TAX)
print("after-tax interest add-back (all-equity) %.0f" % ai)
cA = {"allsp_acq": avg(allsp_acq, A), "maint": avg(maint, A), "allsp": avg(allsp, A)}
cB = {"allsp_acq": avg(allsp_acq, B), "maint": avg(maint, B), "allsp": avg(allsp, B)}
print("cycle A 2016-20 avg", {k: round(v) for k, v in cA.items()}, " cycle B 2021-25 avg", {k: round(v) for k, v in cB.items()})
for k in cA:
    print("  growth between cycle averages %s: %.1f%%/yr" % (k, 100*((cB[k]/cA[k])**(1/5)-1)))
sA, sB = avg(sales, A), avg(sales, B)
print("sales cycle A %.0f B %.0f growth %.1f%%/yr" % (sA, sB, 100*((sB/sA)**0.2-1)))
for k, d in [("allsp_acq", allsp_acq), ("maint", maint)]:
    print("  literal window end-year growth 2021->2025 %s: %.1f%%/yr" % (k, 100*((d[2025]/d[2021])**0.25-1)))
def val(c, g, r):
    v = sum(c*(1+g)**t/(1+r)**t for t in range(1, 11))
    v += c*(1+g)**10/r/(1+r)**10
    return v
def ps(ev): return (ev-NETDEBT)/SH
ev_price = PRICE*SH + NETDEBT
print("market cap %.0f  net debt %.0f  EV at price %.0f" % (PRICE*SH, NETDEBT, ev_price))
gA = (cB["allsp_acq"]/cA["allsp_acq"])**0.2-1
cases = [
 ("central bottom: growth case, all spending and acquisitions charged, growth cut to discount rate", cB["allsp_acq"]+ai, R),
 ("central top: no-growth case, maintenance only (D&A proxy)", cB["maint"]+ai, 0.0),
 ("beside: no-growth, all spending and acquisitions charged", cB["allsp_acq"]+ai, 0.0),
 ("beside: growth case uncut (cycle-to-cycle, all spending and acquisitions)", cB["allsp_acq"]+ai, gA),
 ("beside: maintenance with growth at discount rate (charges no growth spending; shown only)", cB["maint"]+ai, R),
 ("beside literal window: all spending and acq, end-year decline carried", cB["allsp_acq"]+ai, (allsp_acq[2025]/allsp_acq[2021])**0.25-1),
 ("beside literal window: maintenance, end-year decline carried", cB["maint"]+ai, (maint[2025]/maint[2021])**0.25-1),
]
print()
print("%-95s %8s %7s %9s %9s %9s %9s" % ("case", "cash", "g", "EV@5.6", "$/sh", "EV@10", "$/sh@10"))
res = {}
for name, c, g in cases:
    v, v10 = val(c, g, R), val(c, g, FLOOR)
    res[name] = (v, v10)
    print("%-95s %8.0f %6.1f%% %9.0f %9.2f %9.0f %9.2f" % (name, c, 100*g, v, ps(v), v10, ps(v10)))
bot, top = res[cases[0][0]], res[cases[1][0]]
print("\ncentral range $/sh %.2f to %.2f ; width %.2f" % (ps(bot[0]), ps(top[0]), ps(top[0])/ps(bot[0])))
fair = ((bot[1]+top[1])/2 - NETDEBT)/SH
print("fair price all-equity (each end at 10%%, averaged, less net debt): $%.2f" % fair)
# equity-only: owner cash after interest (no add-back) against market value
eb = val(cB["allsp_acq"], R, FLOOR); et = val(cB["maint"], 0.0, FLOOR)
print("fair price equity-only: $%.2f" % (((eb+et)/2)/SH))
print("equity-only range at 5.6%%: $%.2f to $%.2f" % (val(cB["allsp_acq"], R, R)/SH, val(cB["maint"], 0, R)/SH))
# does any case earn the floor at the price? (EV at 10% >= EV at price)
for name, (v, v10) in res.items():
    print("  floor at price: %-90s %s" % (name[:90], "EARNS" if v10 >= ev_price else "no"))
# implied cash yield
print("owner cash yield on EV at price: all-spending %.2f%%, maintenance %.2f%%" % (100*(cB['allsp_acq']+ai)/ev_price, 100*(cB['maint']+ai)/ev_price))
# what cash earns 10% at price, no growth
print("cash needed for 10%% at price, no growth: %.0f" % (FLOOR*ev_price))
