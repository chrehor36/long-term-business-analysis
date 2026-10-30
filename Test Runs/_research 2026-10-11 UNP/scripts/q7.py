"""Q7 arithmetic for the UNP run of 2026-10-11. Every input is a filed figure ($M) cited in the run file."""
yrs = [2021, 2022, 2023, 2024, 2025]
OCF   = {2016:7525,2017:7230,2018:8686,2019:8609,2020:8540,2021:9032,2022:9362,2023:8379,2024:9346,2025:9290}
SBC   = {2016:82,2017:103,2018:96,2019:93,2020:73,2021:88,2022:99,2023:107,2024:118,2025:142}
CAPEX = {2016:3505,2017:3238,2018:3437,2019:3453,2020:2927,2021:2936,2022:3620,2023:3606,2024:3452,2025:3791}
FLP   = {2021:106,2022:91,2023:65,2024:47,2025:36}           # finance-lease principal
GROW  = {2021:527,2022:584,2023:664,2024:500,2025:617}        # capacity and commercial facilities capex
INT   = {2016:698,2017:719,2018:870,2019:1050,2020:1141,2021:1157,2022:1271,2023:1340,2024:1269,2025:1309}
NI    = {2016:4233,2017:10712,2018:5966,2019:5919,2020:5349,2021:6523,2022:6998,2023:6379,2024:6747,2025:7138}
TAX   = {2016:2533,2017:-3080,2018:1775,2019:1828,2020:1631,2021:1955,2022:2074,2023:1854,2024:2047,2025:2028}
REV   = {2021:21804,2022:24875,2023:24119,2024:24250,2025:24510}
def etr(y):
    if y == 2017: return 0.35*0+0.37  # not used in the window; 2017 statutory-era rate, labelled
    return TAX[y]/(NI[y]+TAX[y])
def ati(y): return INT[y]*(1-etr(y))
A  = {y: OCF[y]-SBC[y]-CAPEX[y]-FLP[y] for y in yrs}           # equity basis, all spending
U  = {y: A[y]+ati(y) for y in yrs}                              # all-equity basis, all spending
M  = {y: U[y]+GROW[y] for y in yrs}                             # all-equity, maintenance only
AM = {y: A[y]+GROW[y] for y in yrs}                             # equity basis, maintenance only
mean = lambda d: sum(d[y] for y in yrs)/len(yrs)
cagr = lambda d: (d[2025]/d[2021])**(1/4)-1
def value(base, g, r, years=10):
    v = 0.0; c = base
    for t in range(1, years+1):
        c = c*(1+g); v += c/(1+r)**t
    v += (c/r)/(1+r)**years      # zero nominal growth after year ten
    return v
r = 0.056; floor = 0.10
P = 278.34; SH = 594.075; MCAP = P*SH
NETDEBT = 1288+29039-1614-500      # 10-Q 2026-06-30: debt due within one year + after one year - cash - short-term investments
EV = MCAP+NETDEBT
print(f"market cap {MCAP:,.0f}  net debt {NETDEBT:,}  EV {EV:,.0f}")
for name, d in (("A equity all-spend",A),("U all-equity all-spend",U),("M all-equity maint-only",M),("AM equity maint-only",AM)):
    print(name, {y: round(d[y]) for y in yrs}, "mean", round(mean(d)), "cagr %.2f%%" % (100*cagr(d)))
print("effective tax rates", {y: round(100*etr(y),2) for y in yrs})
print("after-tax interest", {y: round(ati(y)) for y in yrs})
def ps_eq(v): return (v-NETDEBT)/SH
def ps_eqonly(v): return v/SH
gU, gA = cagr(U), cagr(A)
cases = {}
# all-equity central: ends = maintenance-only no-growth (top, by specific (e) inversion) and all-spend shown (negative) growth (bottom)
cases["AE top: maint-only, zero growth"] = (mean(M), 0.0, "ae")
cases["AE no-growth all-spend"] = (mean(U), 0.0, "ae")
cases["AE bottom: all-spend at shown growth"] = (mean(U), gU, "ae")
cases["EO top: maint-only, zero growth"] = (mean(AM), 0.0, "eo")
cases["EO no-growth all-spend"] = (mean(A), 0.0, "eo")
cases["EO bottom: all-spend at shown growth"] = (mean(A), gA, "eo")
for k,(b,g,basis) in cases.items():
    v = value(b,g,r); v10 = value(b,g,floor)
    f = ps_eq if basis=="ae" else ps_eqonly
    print(f"{k:45s} base {b:8.0f} g {100*g:6.2f}%  value@5.6% {v:9.0f} -> ${f(v):7.2f}/sh   @10% {v10:9.0f} -> ${f(v10):7.2f}/sh")
# implied return at the price for each case (solve r such that value = EV or MCAP)
def irr(base, g, target):
    lo, hi = 0.001, 0.5
    for _ in range(200):
        mid=(lo+hi)/2
        if value(base,g,mid) > target: lo = mid
        else: hi = mid
    return mid
print("expected return at the price:")
for k,(b,g,basis) in cases.items():
    t = EV if basis=="ae" else MCAP
    print(f"  {k:45s} {100*irr(b,g,t):5.2f}%")
# cycle sensitivity: five-year averages 2016-2020 vs 2021-2025, equity basis excl finance leases (not tagged before 2019)
A0 = {y: OCF[y]-SBC[y]-CAPEX[y] for y in range(2016,2026)}
U0 = {y: A0[y]+INT[y]*(1-(0.37 if y==2017 else TAX[y]/(NI[y]+TAX[y]))) for y in range(2016,2026)}
m1 = sum(U0[y] for y in range(2016,2021))/5; m2 = sum(U0[y] for y in range(2021,2026))/5
gc = (m2/m1)**(1/5)-1
print(f"cycle sensitivity (all-equity, ex finance leases): 2016-20 avg {m1:,.0f}, 2021-25 avg {m2:,.0f}, growth {100*gc:.2f}%/yr")
vC = value(mean(U), gc, r); print(f"  shown-growth case at {100*gc:.2f}%: value {vC:,.0f} -> ${ps_eq(vC):.2f}/sh ; @10% ${ps_eq(value(mean(U),gc,floor)):.2f}; return at price {100*irr(mean(U),gc,EV):.2f}%")
# sales-growth cap check: revenue 2021->2025 cagr
print("revenue cagr 2021-25 %.2f%%" % (100*((REV[2025]/REV[2021])**0.25-1)))
# Fair price: each end case valued at 10%, averaged
top_ae = value(mean(M),0,floor); bot_ae = value(mean(U),gU,floor)
top_eo = value(mean(AM),0,floor); bot_eo = value(mean(A),gA,floor)
print(f"FAIR all-equity: (${ps_eq(top_ae):.2f} + ${ps_eq(bot_ae):.2f})/2 = ${(ps_eq(top_ae)+ps_eq(bot_ae))/2:.2f}")
print(f"FAIR equity-only: (${ps_eqonly(top_eo):.2f} + ${ps_eqonly(bot_eo):.2f})/2 = ${(ps_eqonly(top_eo)+ps_eqonly(bot_eo))/2:.2f}")
# Merger as if closed (beside, not central): NSC filed record
NOCF={2021:4255,2022:4222,2023:3179,2024:4052,2025:4361}; NSBC={2021:54,2022:53,2023:40,2024:40,2025:63}
NCAP={2021:1470,2022:1948,2023:2349,2024:2381,2025:2204}; NINT={2021:646,2022:692,2023:722,2024:807,2025:792}
NNI={2021:3005,2022:3270,2023:1827,2024:2622,2025:2873}; NTAX={2021:873,2022:860,2023:493,2024:707,2025:792}
NU={y: NOCF[y]-NSBC[y]-NCAP[y]+NINT[y]*(1-NTAX[y]/(NNI[y]+NTAX[y])) for y in yrs}
print("NSC unlevered owner cash", {y: round(NU[y]) for y in yrs}, "mean", round(mean(NU)))
CU = {y: U[y]+NU[y] for y in yrs}; gCU = cagr(CU)
NSC_ND = 649+15967-1069; CASH_CONSID = 20000; NEWSH = 224.608
CND = NETDEBT+NSC_ND+CASH_CONSID; CSH = SH+NEWSH
for lab,b,g in (("combined no-growth",mean(CU),0.0),("combined shown growth",mean(CU),gCU)):
    v=value(b,g,r); v10=value(b,g,floor)
    print(f"{lab:25s} base {b:,.0f} g {100*g:.2f}% value {v:,.0f} -> ${(v-CND)/CSH:.2f}/sh ; @10% ${(v10-CND)/CSH:.2f}/sh")
print(f"combined net debt {CND:,} shares {CSH:.1f}M; NSC net debt {NSC_ND:,}")
