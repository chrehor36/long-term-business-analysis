"""HAS run 2026-10-07: owner cash and the Q7 computation. Inputs transcribed from the filed statements
(companyfacts cross-checked against the 10-K cash-flow statements, accessions in the run file). USD millions."""
OCF  = {2016:817.3,2017:724.4,2018:646.0,2019:653.1,2020:976.3,2021:817.9,2022:372.9,2023:725.6,2024:847.4,2025:893.2}
SBC  = {2016:61.6,2017:56.0,2018:27.9,2019:28.0,2020:49.7,2021:97.8,2022:83.4,2023:72.4,2024:50.8,2025:80.4}
PPE  = {2016:154.9,2017:134.9,2018:140.4,2019:133.6,2020:125.8,2021:132.7,2022:128.2,2023:135.5,2024:87.2,2025:63.3}
SOFT = {2022:46.0,2023:73.8,2024:110.3,2025:135.0}   # additions to software development (tagged from 2022)
INT_PAID = {2017:89.3,2018:82.3,2019:82.2,2020:182.9,2021:171.9,2022:161.7,2023:179.0,2024:162.2,2025:158.4}
INT_INC  = {2017:22.2,2018:22.4,2019:30.1,2020:7.4,2021:5.4,2022:11.8,2023:23.0,2024:47.3,2025:28.6}
BUS_PAID = {2020:4412.9,2021:0.0,2022:146.3,2023:0.0,2024:0.0,2025:0.0}
BUS_SOLD = {2021:378.5,2022:0.0,2023:329.6,2024:-12.0,2025:0.0}
TAX = 0.21   # CONVENTION of this run: US federal statutory rate for the interest add-back; the filer's 2024 effective rate was 20.7%
W = range(2021,2026)
oc  = {y: OCF[y]-SBC[y]-PPE[y]-SOFT.get(y,0.0) for y in OCF}
unl = {y: oc[y] + (INT_PAID[y]-INT_INC[y])*(1-TAX) for y in W}
mnt_l = {y: oc[y] + SOFT.get(y,0.0) for y in W}          # maintenance-only: software for unreleased games treated as growth spending
mnt_u = {y: unl[y] + SOFT.get(y,0.0) for y in W}
avg = lambda d: sum(d[y] for y in W)/5
print("owner cash (OCF-SBC-all capex):", {y:round(oc[y],1) for y in sorted(oc)})
print("5-yr levered avg %.1f; unlevered avg %.1f; maint-only levered %.1f; maint-only unlevered %.1f" % (avg(oc),avg(unl),avg(mnt_l),avg(mnt_u)))
print("unlevered by year", {y:round(unl[y],1) for y in W})
g_l = (oc[2025]/oc[2021])**0.25-1; g_u=(unl[2025]/unl[2021])**0.25-1
print("growth end-to-end levered %.2f%% unlevered %.2f%%" % (g_l*100,g_u*100))
SOV=0.0564; FLOOR=0.10
SH=141.044467; PRICE=90.60
DEBT=497.0+3041.2; CASH=880.5+497.7; ND=DEBT-CASH
print("net debt at 2026-06-28: %.1f (debt %.1f, cash+securities %.1f)" % (ND,DEBT,CASH))
def val(c, r, g=0.0, years=10):
    # c grown at g for ten years then held flat (zero nominal growth), discounted at r
    pv=0; x=c
    for t in range(1,years+1):
        x*= (1+g); pv+= x/(1+r)**t
    pv+= x/r/(1+r)**years
    return pv
for name,c,g in [("all-spending, growth shown (unl)",avg(unl),g_u),("all-spending, no growth (unl)",avg(unl),0.0),("maint-only, no growth (unl)",avg(mnt_u),0.0)]:
    ev=val(c,SOV,g); print("%-36s EV %.0f  per share %.2f" % (name,ev,(ev-ND)/SH))
lo=(val(avg(unl),SOV)-ND)/SH; hi=(val(avg(mnt_u),SOV)-ND)/SH
print("RANGE all-equity: %.2f to %.2f ; midpoint %.2f ; width %.2f to 1" % (lo,hi,(lo+hi)/2,hi/lo))
# equity-only
elo=val(avg(oc),SOV)/SH; ehi=val(avg(mnt_l),SOV)/SH
print("RANGE equity-only: %.2f to %.2f" % (elo,ehi))
# fair price: the price at which the midpoint case earns the floor
mid_u=(avg(unl)+avg(mnt_u))/2; mid_l=(avg(oc)+avg(mnt_l))/2
fp_u=(val(mid_u,FLOOR)-ND)/SH; fp_l=val(mid_l,FLOOR)/SH
print("FAIR PRICE all-equity %.2f ; equity-only %.2f" % (fp_u,fp_l))
# literal rule (c): businesses bought net of sold inside the window as capital spending
net_sold=sum(BUS_SOLD[y]-BUS_PAID[y] for y in W)
print("net businesses sold in window %.1f -> +%.1f a year" % (net_sold,net_sold/5))
llo=(val(avg(unl)+net_sold/5,SOV)-ND)/SH; lhi=(val(avg(mnt_u)+net_sold/5,SOV)-ND)/SH
print("LITERAL (c) range all-equity %.2f to %.2f" % (llo,lhi))
# post-sale years only (2024-2025), shown beside: the business that remains
ps=(unl[2024]+unl[2025])/2; psm=(mnt_u[2024]+mnt_u[2025])/2
print("POST-SALE 2024-25 unlevered avg %.1f (maint %.1f) -> %.2f to %.2f" % (ps,psm,(val(ps,SOV)-ND)/SH,(val(psm,SOV)-ND)/SH))
# implied yield at the price
ev_mkt=PRICE*SH+ND
print("market cap %.0f, EV %.0f; unlevered 5-yr avg yield %.2f%%; maint-only %.2f%%" % (PRICE*SH,ev_mkt,avg(unl)/ev_mkt*100,avg(mnt_u)/ev_mkt*100))
# dividend cover
DIV={2021:374.5,2022:385.3,2023:388.0,2024:389.9,2025:392.5}
print("dividend cover by owner cash", {y: round(oc[y]/DIV[y],2) for y in W})

print("\n--- refined: both ends of each basis, and the fair price on each end at the floor ---")
for basis, base_all, base_mnt, g, debt in [("all-equity", avg(unl), avg(mnt_u), g_u, ND), ("equity-only", avg(oc), avg(mnt_l), g_l, 0.0)]:
    bottom_case = (base_all, g)        # all spending, growth shown (the growth bought is worth less than its cost: bottom, rule (e))
    top_case = (base_mnt, 0.0)         # maintenance only, no growth (top, rule (e))
    lo_v = (val(bottom_case[0], SOV, bottom_case[1]) - debt) / SH
    hi_v = (val(top_case[0], SOV, top_case[1]) - debt) / SH
    lo_v, hi_v = min(lo_v, hi_v), max(lo_v, hi_v)
    fp = ((val(bottom_case[0], FLOOR, bottom_case[1]) - debt) / SH + (val(top_case[0], FLOOR, top_case[1]) - debt) / SH) / 2
    print("%-12s range %.2f to %.2f (mid %.2f, width %.2f:1); fair price at the floor %.2f" % (basis, lo_v, hi_v, (lo_v+hi_v)/2, hi_v/lo_v, fp))

print("\n--- default pair of rule (c): businesses bought net of sold inside the window as capital spending, total growth credited ---")
add = net_sold/5
unl_c = {y: unl[y] + (BUS_SOLD.get(y,0)-BUS_PAID.get(y,0)) for y in W}
oc_c = {y: oc[y] + (BUS_SOLD.get(y,0)-BUS_PAID.get(y,0)) for y in W}
gu_c = (unl_c[2025]/unl_c[2021])**0.25-1; gl_c=(oc_c[2025]/oc_c[2021])**0.25-1
print("by year unlevered with business flows", {y:round(unl_c[y],1) for y in W}, "growth %.2f%%" % (gu_c*100))
for basis, base_all, base_mnt, g, debt in [("all-equity", avg(unl)+add, avg(mnt_u)+add, gu_c, ND), ("equity-only", avg(oc)+add, avg(mnt_l)+add, gl_c, 0.0)]:
    a=(val(base_all,SOV,g)-debt)/SH; b=(val(base_mnt,SOV,0.0)-debt)/SH; c=(val(base_all,SOV,0.0)-debt)/SH
    lo_v,hi_v=min(a,b,c),max(a,b,c)
    fp=((val(base_all,FLOOR,g)-debt)/SH+(val(base_mnt,FLOOR,0.0)-debt)/SH)/2
    print("%-12s range %.2f to %.2f ; fair price %.2f" % (basis, lo_v, hi_v, fp))
