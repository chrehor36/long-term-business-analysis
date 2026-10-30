# PEG Q7 arithmetic. All figures USD millions from the filed statements (accessions in the run file).
yrs = [2021, 2022, 2023, 2024, 2025]
peg_ocf  = [1736, 1503, 3806, 2133, 3298]
peg_cx   = [2719, 2888, 3325, 3380, 3272]
peg_da   = [1216, 1100, 1135, 1182, 1257]
nfuel    = [187, 183, 189, 191, 202]
sbc      = [28, 29, 18, 40, 43]
int_paid = [547, 602, 683, 799, 932]
rev      = [9722, 9800, 11237, 10290, 12168]
coll     = [-790+81, -677+111, 1408-201, -131+4, 22+13]
g_ocf = [1724, 2028, 1540, 1725, 2368]
g_cx  = [2447, 2590, 2998, 2921, 2731]
g_ee  = [117, 286, 466, 544, 552]
g_da  = [928, 935, 980, 1025, 1116]
g_rev = [7122, 7935, 7807, 8449, 9558]
avg = lambda v: sum(v)/len(v)
print("year  PEG_OC_all  PSEG_OCm  PSEG_G  P&O_OC  collateral")
po_ocf = [a-b for a,b in zip(peg_ocf, g_ocf)]
po_cx  = [a-b for a,b in zip(peg_cx, g_cx)]
for i,y in enumerate(yrs):
    oc_all = peg_ocf[i]-peg_cx[i]-sbc[i]
    ocm = g_ocf[i]+g_ee[i]-g_da[i]
    G = g_cx[i]+g_ee[i]-g_da[i]
    print(y, oc_all, ocm, G, po_ocf[i]-po_cx[i], coll[i])
OC_all = avg(peg_ocf)-avg(peg_cx)-avg(sbc)
P_ocm = avg(g_ocf)+avg(g_ee)-avg(g_da)
P_G   = avg(g_cx)+avg(g_ee)-avg(g_da)
PO    = avg(po_ocf)-avg(po_cx)
PO_maint = avg([a for a in [x for x in []]] or [0])
print("PEG owner cash, all spending, 5y avg:", round(OC_all,1))
print("PSE&G OC after maintenance (D&A) avg:", round(P_ocm,1), " PSE&G growth spending avg:", round(P_G,1))
print("P&O OCF avg", avg(po_ocf), "capex avg", avg(po_cx), "D&A+fuel avg", avg([a-b for a,b in zip(peg_da,g_da)])+avg(nfuel), "P&O OC", PO)
print("SBC avg", avg(sbc), " collateral sum", sum(coll))
flat = PO - avg(sbc)
OCm_total = P_ocm + flat
print("Total OC after maintenance (equity-only, no-growth stream):", round(OCm_total,1))
# growth: PSE&G OCm end-years and halves; sales
cagr = (( g_ocf[4]+g_ee[4]-g_da[4])/(g_ocf[0]+g_ee[0]-g_da[0]))**(1/4)-1
h1 = avg([g_ocf[i]+g_ee[i]-g_da[i] for i in (0,1)]); h2 = avg([g_ocf[i]+g_ee[i]-g_da[i] for i in (3,4)])
print("PSE&G OCm CAGR end years %.2f%%, halves %.2f%%/yr" % (100*cagr, 100*((h2/h1)**(1/3)-1)))
print("PSE&G OCm share of sales by year:", [round((g_ocf[i]+g_ee[i]-g_da[i])/g_rev[i]*100,1) for i in range(5)])
print("PSE&G sales CAGR %.2f%%; PEG sales CAGR %.2f%%" % (100*((g_rev[4]/g_rev[0])**0.25-1), 100*((rev[4]/rev[0])**0.25-1)))
sov = 0.0533
g = min((g_rev[4]/g_rev[0])**0.25-1, sov)
print("growth carried (cut to sales growth, capped at sovereign): %.4f" % g)
# debt credit
ltd_2020 = 14496+1684; ltd_2025 = 21670+875
inc = (ltd_2025-ltd_2020)/5
own_share = (22741+850)/(22741+850+17329)
cap_own = own_share*P_G; cap_45 = 0.45*P_G
C = min(inc, cap_own); C45 = min(inc, cap_45)
print("LT debt YE2020 %d YE2025 %d increase/yr %.1f; own LT debt share %.4f; cap %.1f; credit %.1f; (45%% cap: %.1f)" % (ltd_2020, ltd_2025, inc, own_share, cap_own, C, C45))
shares = 498.420030
price = 72.18
def value(r, g, ocm_p, G, C, flat, years=10):
    v = 0.0
    for t in range(1, years+1):
        v += ((ocm_p - G + C)*(1+g)**t + flat)/(1+r)**t
    term = (ocm_p*(1+g)**years + flat)/r/(1+r)**years
    return v + term
def nogrowth(r, ocm_p, flat): return (ocm_p+flat)/r
for label, CC in (("own-share cap (central)", C), ("45% cap", C45)):
    ng = nogrowth(sov, P_ocm, flat); gr = value(sov, g, P_ocm, P_G, CC, flat)
    ng10 = nogrowth(0.10, P_ocm, flat); gr10 = value(0.10, g, P_ocm, P_G, CC, flat)
    print(label, "EQUITY-ONLY range per share: no-growth %.2f, growth %.2f | at 10%%: %.2f, %.2f fair %.2f" % (ng/shares, gr/shares, ng10/shares, gr10/shares, (ng10+gr10)/2/shares))
# growth year 1 and year 10 spending
print("growth spending yr1 %.0f yr10 %.0f; credit yr1 %.0f yr10 %.0f" % (P_G*(1+g), P_G*(1+g)**10, C*(1+g), C*(1+g)**10))
# expected return at price on no-growth stream
print("no-growth owner cash yield at price: %.2f%%" % (OCm_total/(price*shares)*100))
# all-equity beside: add after-tax interest, no debt credit, less net debt at 2026-06-30
t = 0.21 + 0.115*(1-0.21)
ati = avg(int_paid)*(1-t)
netdebt = 22741+850+950-192
# allocate interest: add to flat (no growth) as conservative simplification
ng_ae = nogrowth(sov, P_ocm, flat+ati) - netdebt
gr_ae = value(sov, g, P_ocm, P_G, 0, flat+ati) - netdebt
ng_ae10 = nogrowth(0.10, P_ocm, flat+ati) - netdebt
gr_ae10 = value(0.10, g, P_ocm, P_G, 0, flat+ati) - netdebt
print("statutory rate %.4f after-tax interest %.1f net debt %d" % (t, ati, netdebt))
print("ALL-EQUITY beside: no-growth %.2f growth %.2f | fair %.2f" % (ng_ae/shares, gr_ae/shares, (ng_ae10+gr_ae10)/2/shares))
# literal window all spending (no maintenance split)
print("literal all-spending owner cash avg %.1f -> perpetuity per share %.2f" % (OC_all, OC_all/sov/shares))
# PTC variant (section E): remove 2024 PTC 350 from the base
ng_ptc = nogrowth(sov, P_ocm, flat-70)/shares; gr_ptc = value(sov, g, P_ocm, P_G, C, flat-70)/shares
print("PTC removed (-70/yr): no-growth %.2f growth %.2f" % (ng_ptc, gr_ptc))
# 2022-2025 variant (2021 dropped) rejected, shown
i4 = slice(1,5)
P_ocm4 = avg(g_ocf[i4])+avg(g_ee[i4])-avg(g_da[i4]); P_G4 = avg(g_cx[i4])+avg(g_ee[i4])-avg(g_da[i4])
flat4 = avg(po_ocf[i4])-avg(po_cx[i4])-avg(sbc[i4])
inc4 = (ltd_2025-(15219+700))/4; C4 = min(inc4, own_share*P_G4)
print("2022-2025 variant: no-growth %.2f growth %.2f" % (nogrowth(sov,P_ocm4,flat4)/shares, value(sov,g,P_ocm4,P_G4,C4,flat4)/shares))
print("market cap %.0f" % (price*shares))
