# TXN owner cash recast and Q7 arithmetic. All USD millions. Sources: 10-K cash-flow statements (XBRL companyfacts,
# FY2025 10-K 0000097476-26-000059 cross-checked), 10-Q 0000097476-26-000152 for the balance sheet at 2026-06-30.
Y = list(range(2014, 2026))
OCF = dict(zip(Y, [4054,4397,4614,5363,7189,6649,6139,8756,8720,6420,6318,7153]))
SBC = dict(zip(Y, [277,286,252,242,232,217,224,230,289,362,387,419]))
CAPEX = dict(zip(Y, [385,551,531,695,1131,847,649,2462,2797,5071,4820,4550]))
DEP = dict(zip(Y, [850,766,605,539,590,708,733,755,925,1175,1508,1918]))
CHIPSDEP = {2023:45, 2024:159, 2025:353}          # depreciation reduced by CHIPS incentives (10-K note 2)
SWAM = dict(zip(Y, [59,48,31,47,46,54,61,57,54,63,72,81]))  # amortization of capitalized software
ITC_OCF = {2024:588, 2025:335}                     # CHIPS ITC used to reduce taxes payable, inside OCF
CHIPS_INV = {2025:335}                             # CHIPS proceeds in investing
INTPAID = dict(zip(Y, [102,99,88,75,114,156,182,181,198,321,473,542]))
OIE = dict(zip(Y, [21,-16,155,75,98,175,313,143,106,440,496,230]))  # OI&E net (mostly interest income)
REV = dict(zip(Y, [13045,13000,13370,14961,15784,14383,14461,18344,20028,17519,15641,17682]))
T = 0.21  # CONVENTION of this run: net interest taken out at the US statutory rate
def fin(y): return (INTPAID[y] - OIE[y]) * (1 - T)  # add back: interest paid net of interest-type income, after tax
OC_m, OC_c, OC_m_eq, OC_c_eq = {}, {}, {}, {}
for y in Y:
    base = OCF[y] - SBC[y] - SWAM[y]
    OC_m_eq[y] = base - (DEP[y] + CHIPSDEP.get(y,0)) - ITC_OCF.get(y,0)
    OC_c_eq[y] = base - CAPEX[y] + CHIPS_INV.get(y,0)
    OC_m[y] = OC_m_eq[y] + fin(y)
    OC_c[y] = OC_c_eq[y] + fin(y)
print("year  rev    OC_maint(all-eq)  OC_allcapex(all-eq)  OC_maint(eq)  OC_allcapex(eq)  OCm%rev")
for y in Y:
    print(y, REV[y], round(OC_m[y]), round(OC_c[y]), round(OC_m_eq[y]), round(OC_c_eq[y]), f"{100*OC_m[y]/REV[y]:.1f}")
avg = lambda d, ys: sum(d[y] for y in ys)/len(ys)
W = [2021,2022,2023,2024,2025]
C1 = [2015,2016,2017,2018]; C2 = [2019,2020,2021,2022,2023]
def cagr(a, b, n): return (b/a)**(1/n)-1 if a>0 and b>0 else float('nan')
res = {}
for name, d in [("maint_alleq", OC_m), ("allcapex_alleq", OC_c), ("maint_eq", OC_m_eq), ("allcapex_eq", OC_c_eq)]:
    wa = avg(d, W); g_lit = cagr(d[2021], d[2025], 4)
    h1 = avg(d,[2021,2022]); h2 = avg(d,[2024,2025]); g_half = cagr(h1, h2, 3)
    c1 = avg(d, C1); c2 = avg(d, C2); g_cyc = cagr(c1, c2, 4.5)
    res[name] = dict(win=wa, g_lit=g_lit, g_half=g_half, cyc=c2, cyc1=c1, g_cyc=g_cyc)
    print(f"{name}: window avg {wa:.0f}; literal CAGR 2021-25 {g_lit:.2%}; halves CAGR {g_half:.2%}; cycle1(2015-18) {c1:.0f}; cycle2(2019-23) {c2:.0f}; growth between cycles {g_cyc:.2%}")
rg = cagr(avg(REV,C1), avg(REV,C2), 4.5); print(f"revenue growth between cycle averages {rg:.2%}; revenue CAGR 2014-2025 {cagr(REV[2014],REV[2025],11):.2%}; revenue 2015->2025 {cagr(REV[2015],REV[2025],10):.2%}")
import json; json.dump({k:{kk:float(vv) for kk,vv in v.items()} for k,v in res.items()}, open("value_inputs.json","w"), indent=1)
