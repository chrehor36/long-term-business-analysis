# Owner cash and Q7 range for WTRG, from the filed cash-flow statements (USD millions).
# Sources: 10-K FY2025 0000078128-26-000050 (2023-2025), 10-K FY2023 0001562762-24-000047 (2021-2022),
# 10-K FY2021 0001562762-22-000068 (capitalization at 2020-12-31), 10-Q 0000078128-26-000077 (2026-06-30).
yrs = [2021, 2022, 2023, 2024, 2025]
ocf   = [644.679, 600.306, 933.587, 770.343, 1010.459]
sbc   = [10.078, 12.206, 11.323, 9.785, 12.855]
da    = [297.952, 321.177, 343.695, 369.552, 417.471]   # depreciation and amortization, cash-flow statement
capex = [1020.519, 1062.763, 1199.103, 1329.747, 1429.980]
acq   = [36.326, 116.891, 45.303, 0.665, 57.004]
sale  = [1.819, 1.081, 41.758, 167.470, 1.548]
ciac  = [15.264-7.725, 11.714-5.006, 23.982-8.471, 19.563-8.564, 28.255-8.073]  # advances and contributions, net of repayments
intpaid=[201.792, 225.820, 272.532, 275.898, 310.921]   # cash paid for interest, net of capitalized
wc    = [-109.605+5.190, -223.335+53.761, 189.989-14.559, -103.335+26.963, -85.432+14.299]
rev   = [1878.144, 2288.032, 2053.824, 2086.113, 2474.615]
n=5
avg=lambda x: sum(x)/len(x)
netacq=[a-s for a,s in zip(acq,sale)]
oc_all=[o-s-c-na+ci for o,s,c,na,ci in zip(ocf,sbc,capex,netacq,ciac)]
oc_maint=[o-s-d for o,s,d in zip(ocf,sbc,da)]
growth_sp=[c-d+na-ci for c,d,na,ci in zip(capex,da,netacq,ciac)]
print("year  OCF   SBC   D&A  capex netacq  CIAC  OC_all  OC_maint growthsp  WC  OCmaint/rev")
for i in range(n):
    print(yrs[i], *("%7.1f"%v for v in [ocf[i],sbc[i],da[i],capex[i],netacq[i],ciac[i],oc_all[i],oc_maint[i],growth_sp[i],wc[i]]), "%.1f%%"%(oc_maint[i]/rev[i]*100))
print("avg  ", *("%7.1f"%avg(v) for v in [ocf,sbc,da,capex,netacq,ciac,oc_all,oc_maint,growth_sp,wc]))
OCm=avg(oc_maint); GS=avg(growth_sp); OCall=avg(oc_all); INT=avg(intpaid)
# growth shown, aggregate, on the maintenance-basis owner cash
cagr=(oc_maint[-1]/oc_maint[0])**(1/4)-1
h1=avg(oc_maint[:2]); h2=avg(oc_maint[3:])
halves=(h2/h1)**(1/3)-1
sales_g=(rev[-1]/rev[0])**(1/4)-1
print("\nOC_maint avg %.1f  end-year CAGR %.2f%%  halves (2021-22 vs 2024-25, 3 yrs apart) %.2f%%  sales CAGR %.2f%%" % (OCm, cagr*100, halves*100, sales_g*100))
maxshare=max(o/r for o,r in zip(oc_maint,rev))
print("highest OC_maint/sales %.1f%%" % (maxshare*100))
# cap test (f): OC_maint carried 10y at halves rate vs highest share x sales carried at sales growth
for g in [halves, cagr]:
    oc10=OCm*(1+g)**10; s10=avg(rev)*(1+sales_g)**10
    print(" g %.2f%%: OC yr10 %.0f vs highest share x sales yr10 %.0f -> %s" % (g*100, oc10, maxshare*s10, "CUT to sales growth" if oc10>maxshare*s10 else "ok"))
# debt credit
ltd2020=5630.243   # total long-term debt incl. current portion and revolver, no CP (statement of capitalization, 10-K FY2021)
ltd2025=8181.848-568.000  # total long-term debt incl current, less commercial paper (statement of capitalization, 10-K FY2025)
ltd2020_norev=ltd2020-385.0
credit=(ltd2025-ltd2020)/5; credit_alt=(ltd2025-ltd2020_norev)/5
# own LT debt share of LT capital at 2026-06-30
ltd_q2=8473.855+42.312-385.178  # LT excl current (gross) + current portion - CP gross (384.723 net + 0.455 discount)
eq_q2=7018.256
cap=ltd_q2/(ltd_q2+eq_q2)
print("\nLT debt 2020 %.1f 2025(ex CP) %.1f credit/yr %.1f (revolver excluded at 2020: %.1f)" % (ltd2020, ltd2025, credit, credit_alt))
print("own LT debt share of LT capital 2026-06-30: %.1f / (%.1f + %.1f) = %.2f%%" % (ltd_q2, ltd_q2, eq_q2, cap*100))
print("growth spending avg %.1f x cap = %.1f; credit used = %.1f" % (GS, GS*cap, min(credit, GS*cap)))
DC=min(credit,GS*cap)
shares=283.778605; price=42.45; mcap=shares*price
# net debt for all-equity basis at 2026-06-30: LT debt incl CP (gross principal) + current + loans payable - cash
netdebt=8473.855+42.312+41.000-8.634
print("market cap %.1f  net debt (all-equity basis) %.1f" % (mcap, netdebt))
def pv(stream_fn, r, g, years=10):
    v=0.0
    for t in range(1,years+1): v+=stream_fn(t,g)/(1+r)**t
    term=stream_fn(years,g,terminal=True)/r/(1+r)**years
    return v+term
def case_equity(g, r, credit_on=True, gs_on=True, base=OCm, gsp=GS, dc=DC):
    def f(t,g,terminal=False):
        oc=base*(1+g)**t
        if terminal: return oc  # zero nominal growth after year 10, growth spending and credit stop
        return oc - (gsp*(1+g)**t if gs_on else 0) + (dc*(1+g)**t if credit_on else 0)
    return pv(f,r,g)
r=0.053
G=None
print()
results={}
for label,g in [("halves",halves),("sales(cut)",sales_g)]:
    ng=case_equity(0,r,credit_on=False,gs_on=False)
    gr=case_equity(g,r)
    print("EQUITY-ONLY  r=5.30%%  no-growth %.0f (%.2f/sh)  growth[%s %.2f%%] %.0f (%.2f/sh)" % (ng, ng/shares, label, g*100, gr, gr/shares))
    ng10=case_equity(0,0.10,credit_on=False,gs_on=False); gr10=case_equity(g,0.10)
    print("   at 10%%: no-growth %.0f (%.2f)  growth %.0f (%.2f)  FAIR (avg) %.2f" % (ng10, ng10/shares, gr10, gr10/shares, (ng10+gr10)/2/shares))
    # all-spending growth case without debt credit, beside
    gr_nc=case_equity(g,r,credit_on=False)
    print("   growth case, no debt credit: %.0f (%.2f/sh)" % (gr_nc, gr_nc/shares))
    # all-equity basis: owner cash before interest (company's own tax ~ cash taxes small; interest added back as paid)
    U=OCm+INT
    ngA=case_equity(0,r,credit_on=False,gs_on=False,base=U)-netdebt
    grA=case_equity(g,r,credit_on=False,base=U)-netdebt
    ngA10=case_equity(0,0.10,credit_on=False,gs_on=False,base=U)-netdebt
    grA10=case_equity(g,0.10,credit_on=False,base=U)-netdebt
    print("ALL-EQUITY  unlevered OC %.1f: no-growth %.2f/sh growth %.2f/sh ; at 10%%: %.2f / %.2f fair %.2f" % (U, ngA/shares, grA/shares, ngA10/shares, grA10/shares, (ngA10+grA10)/2/shares))
    results[label]=(ng,gr)
# floor test: expected return at price on each case: solve r such that value = mcap
def irr(fn):
    lo,hi=0.0001,0.5
    for _ in range(100):
        mid=(lo+hi)/2
        if fn(mid)>mcap: lo=mid
        else: hi=mid
    return mid
for label,g in [("halves",halves),("sales(cut)",sales_g)]:
    print("expected return at price: no-growth %.2f%%  growth[%s] %.2f%%" % (irr(lambda rr: case_equity(0,rr,credit_on=False,gs_on=False))*100, label, irr(lambda rr: case_equity(g,rr))*100))
# all-spending owner cash (literal), beside
print("\nliteral window: OC after all spending avg %.1f (every year negative: %s)" % (OCall, all(x<0 for x in oc_all)))
print("OC_all + debt credit avg %.1f" % (OCall+credit))
print("growth spending yr1 %.1f yr10 %.1f (at sales growth); credit yr1 %.1f yr10 %.1f" % (GS*(1+sales_g), GS*(1+sales_g)**10, DC*(1+sales_g), DC*(1+sales_g)**10))

print("\n--- extra cases ---")
for label,g in [("shown end-year CAGR (uncut)",cagr)]:
    gr=case_equity(g,r); gr10=case_equity(g,0.10)
    print("%s %.2f%%: value %.0f (%.2f/sh); at 10%% %.2f/sh; expected return at price %.2f%%" % (label,g*100,gr,gr/shares,gr10/shares, irr(lambda rr: case_equity(g,rr))*100))
# alternative debt credit: revolver excluded at 2020, capped
DC2=min(credit_alt,GS*cap)
gr=case_equity(sales_g,r,dc=DC2); gr10=case_equity(sales_g,0.10,dc=DC2)
print("alt credit %.1f (cap %.1f): growth case %.2f/sh, at 10%% %.2f/sh, fair %.2f, exp return %.2f%%" % (credit_alt, GS*cap, gr/shares, gr10/shares, (case_equity(0,0.10,credit_on=False,gs_on=False)+gr10)/2/shares, irr(lambda rr: case_equity(sales_g,rr,dc=DC2))*100))
# all-spending literal: OC after all spending + credit, no growth
lit=OCall+credit
print("literal all-spending + credit, flat: %.1f /yr -> value %.0f" % (lit, lit/r))
# width
ng=case_equity(0,r,credit_on=False,gs_on=False); gr=case_equity(sales_g,r)
print("central range %.2f to %.2f per share; width %.2f to 1" % (ng/shares, gr/shares, gr/ng))
print("deal beside: 0.305 x AWK 141.10 = %.2f" % (0.305*141.10))
