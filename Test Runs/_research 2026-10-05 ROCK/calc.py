# COMPUTATION - NOT A CLEARANCE. Arithmetic for the ROCK run of 2026-10-05. USD millions.
r = 0.0563            # 30y Treasury par yield, 2026-10-02 (tools/sources.py)
N = 29.683889         # cover shares, 10-Q 2026-06-30 cover as of 2026-08-03
P = 40.32             # aggregator close 2026-10-05 (flagged)
tax = 0.24            # CONVENTION of this run: 2023-2025 continuing effective rates 26.1/21.0/22.9 -> about 24%
# Legacy continuing EBIT 2021-2025 = segments (Res+Agtech+Infra) - unallocated corporate (10-K FY2021, FY2023, FY2025)
ebit = {2021:105.821-0.931+8.911-36.971, 2022:126.458+2.914+9.003-33.516, 2023:143.068-0.928+18.529-40.100,
        2024:148.784+11.040+21.295-41.445, 2025:137.195+9.804+22.042-46.290}
amort = {2021:6.0, 2022:6.0, 2023:6.181, 2024:6.337, 2025:15.275}   # 2021-22 continuing amortization not filed: CONVENTION 6.0 (2023-24 level)
dep   = {2023:18.707-6.181, 2024:19.120-6.337, 2025:29.849-15.275}
capex = {2023:13.884, 2024:17.374, 2025:46.413}
dmc = sum(dep[y]-capex[y] for y in dep)/3
ebita5 = sum(ebit[y]+amort[y] for y in ebit)/5
leg_allcapex = ebita5 + dmc
leg_dep = ebita5
print("legacy EBIT by year", {y:round(v,1) for y,v in ebit.items()})
print("legacy 5y avg EBITA %.1f ; dep-capex 3y avg %.1f ; pre-tax unlevered owner cash all-capex %.1f dep-variant %.1f"%(ebita5,dmc,leg_allcapex,leg_dep))
# OmniMax (8-K/A 2026-04-17, audited): OI, D&A, depreciation, capex
omx = {2024:(31.667, 28.939, 7.7, 9.995), 2025:(38.495, 42.683, 9.3, 10.177)}
omx_ebita = sum(oi+(da-d) for oi,da,d,c in omx.values())/2
omx_dmc = sum(d-c for oi,da,d,c in omx.values())/2
omx_all = omx_ebita+omx_dmc
print("OmniMax 2y avg EBITA %.1f ; dep-capex %.1f ; all-capex %.1f"%(omx_ebita,omx_dmc,omx_all))
debt_gross = 625+600+21; cash=15.147; netdebt = debt_gross-cash
interest = 80.0   # CONVENTION: Q2 2026 interest 20.965 x4 = 83.9 less ~4 non-cash issuance-cost amortization
print("net debt %.1f"%netdebt)
def pv_equity(unlev_pretax, g):
    c = unlev_pretax*(1-tax)
    pv=0; x=c
    for t in range(1,11):
        x = x*(1+g) if t>1 else c*(1+g)
        pv += x/(1+r)**t
    term = x/r/(1+r)**10   # zero nominal growth after year ten
    ev = pv+term
    return ev, ev-netdebt
cases = {}
for basis,leg in (("all-capex",leg_allcapex),("dep-variant",leg_dep)):
    unlev = leg + (omx_all if basis=="all-capex" else omx_ebita)
    for gname,g in (("no growth",0.0),("shown growth capped 1.1%",0.011),("shown growth uncapped 12.4%",0.124)):
        ev,eq = pv_equity(unlev,g)
        cases[(basis,gname)] = eq/N
        print(f"{basis:12s} {gname:28s} unlev pre-tax {unlev:6.1f}  EV {ev:7.0f}  equity {eq:7.0f}  per share {eq/N:7.2f}")
# whole-cycle: Residential segment margin 2016-2025 avg vs 2021-2025 avg
res = {2016:15.1,2017:16.5,2018:15.1,2019:13.7,2020:18.1,2021:16.7,2022:16.5,2023:17.6,2024:19.0,2025:16.6}
wc = sum(res.values())/10; w5 = sum(res[y] for y in range(2021,2026))/5
print("Residential margin avg 2016-25 %.2f vs 2021-25 %.2f ratio %.3f"%(wc,w5,wc/w5))
res_profit5 = (105.821+126.458+143.068+148.784+137.195)/5
haircut = res_profit5*(1-wc/w5)
for basis,leg in (("all-capex",leg_allcapex),("dep-variant",leg_dep)):
    unlev = leg - haircut + (omx_all if basis=="all-capex" else omx_ebita)*(wc/w5)
    ev,eq = pv_equity(unlev,0.0)
    print(f"whole-cycle {basis} no growth unlev pre-tax {unlev:.1f} per share {eq/N:.2f}")
    cases[(basis,"whole-cycle no growth")] = eq/N
# Fair price: central case clears ~10% pre-tax floor. Pre-tax equity cash = unlevered pre-tax - interest; expected pre-tax return = yield + g
central_unlev = ((leg_allcapex+omx_all)+(leg_dep+omx_ebita))/2
for g in (0.0,0.011):
    eqcash = central_unlev-interest
    fair = eqcash/((0.10-g)*N)
    print("central unlev %.1f equity pre-tax cash %.1f per share %.2f ; g=%.3f fair price %.2f ; pre-tax return at price %.1f%%"%(central_unlev,eqcash,eqcash/N,g,fair,100*(eqcash/(P*N)+g)))
# worst case for cheap rule
worst_unlev = leg_allcapex - haircut + omx_all*(wc/w5)
print("worst unlev pre-tax %.1f ; equity pre-tax cash %.1f per share %.2f"%(worst_unlev, worst_unlev-interest, (worst_unlev-interest)/N))
print("cheap (worst case clears 10%% pre-tax with no growth, then one-third off): %.2f"%((worst_unlev-interest)/(0.10*N)*2/3))
print("cheap (worst case yields 15%% pre-tax): %.2f"%((worst_unlev-interest)/(0.15*N)))
