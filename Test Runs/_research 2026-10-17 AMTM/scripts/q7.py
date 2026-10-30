# COMPUTATION, NOT A CLEARANCE. Owner cash, the range and the fair price for AMTM, from the filed statements.
# USD millions. Sources in the run file (Q7 computation section).
T = 0.21   # CONVENTION of the run: interest added back at the U.S. statutory rate (21%) for the all-equity basis
R = 0.0543 # US Treasury 30Y par, 2026-10-16
FLOOR = 0.10
SH = 244.506413
PRICE = 19.52

# Legacy Amentum (information statement FY2021-FY2023, thousands converted; 10-K FY2025 for FY2024)
legacy = {
 # year: OCF, interest paid, SBC, capex (PP&E + software), NCI distributions, finance-lease principal, net JV contributions, MARPA inflow
 2021: (247.118, 115.252, 1.195, 20.095+0.642, 52.356, 3.992, 24.432-7.082, 0.0),
 2022: (126.019, 207.747, 2.735, 18.152+3.625, 56.322, 4.395, 34.120-24.257, 0.0),
 2023: (67.394, 361.886, 3.379, 12.455+3.140, 24.521, 4.577, 16.550-14.063, 0.0),
 2024: (47.0, 373.0, 18.0, 11.0, 6.0, 0.0, 1.0-0.0, 177.0),
}
# CMS half (information statement; FY2024 = twelve months to 2024-06-28: FY2023 - 9M FY2023 + 9M FY2024)
cms = {
 # year: OCF, SBC, capex net of disposals, NCI dividends, net JV contributions
 2021: (245, 7, 33-(-1), 1, 0),
 2022: (193, 5, 31-3, 2, -5),
 2023: (278, 5, 23-4, 12, 0),
 2024: (278-173+247, 5-4+4, (23-4)-(17-3)+(10-0), 12-10+10, 0),
}
# Combined FY2025 (10-K FY2025) and nine months FY2026 (10-Q)
comb = {
 2025: (543, 306, 21, 27, 35, 0, 56-19, 3),
 "9M2026": (235, 175, 23, 22, 23, 0, 53-23, 120),
}
def oc_lev(ocf, intp, sbc, cx, nci, fl, jv, marpa):
    return ocf + intp*(1-T) - sbc - cx - nci - fl - jv - marpa
rows = {}
for y in (2021, 2022, 2023, 2024):
    l = oc_lev(*legacy[y]); c = cms[y]; cc = c[0]-c[1]-c[2]-c[3]-c[4]
    rows[y] = (l, cc, l+cc)
rows[2025] = (None, None, oc_lev(*comb[2025]))
print("Owner cash, all-equity basis (before interest, after the company's own tax), USD M")
for y, (l, c, t) in rows.items():
    print(f"  FY{y}: legacy {'' if l is None else f'{l:7.1f}'}  CMS {'' if c is None else f'{c:6.1f}'}  combined {t:7.1f}")
nine = oc_lev(*comb["9M2026"]); print(f"  9M FY2026 combined: {nine:.1f}")
mean5 = sum(r[2] for r in rows.values())/5
print(f"  five-year mean FY2021-FY2025: {mean5:.1f}")

# Acquisitions net of divestitures in the window (cash paid for businesses)
acq = {2021: 991.092+207, 2022: 1757.697, 2023: 0, 2024: 0, 2025: 70-365}
netacq = sum(acq.values()); print(f"  net purchases of businesses FY2021-FY2025: {netacq:.1f}; half of owner cash before purchases {0.5*5*mean5:.1f}")
after = [rows[y][2]-acq[y] for y in rows]; print("  owner cash after purchases by year:", [round(x,1) for x in after], "mean", round(sum(after)/5,1))

# Organic growth from the filers' own revenue bridges
org = [ (0.7-0.4+ (5176-5080)/1000) / ((5886.978+5080)/1000),   # FY2022: Legacy new awards 0.7 less completions 0.4; CMS revenue change
        (0.5-1.2+ (5525-5176)/1000) / ((7675.956+5176)/1000),   # FY2023
        (523/1000 + (4137-4059)/1000*4/3) / ((7864.933+5525)/1000) ] # FY2024: Legacy +523 (new awards, growth); CMS 9M change annualized
g = 1.0
for x in org: g *= 1+x
g_org = g**(1/3)-1
print("  organic growth by year:", [round(100*x,2) for x in org], f"compound {100*g_org:.2f}%/yr")
g_lit = (rows[2025][2]/rows[2021][2])**(1/4)-1
print(f"  literal growth of combined owner cash FY2021->FY2025: {100*g_lit:.2f}%/yr (includes purchases and merger savings)")

def value(oc0, g, r, years=10):
    pv=0; oc=oc0
    for t in range(1, years+1):
        oc*= (1+g); pv += oc/(1+r)**t
    pv += (oc/r)/(1+r)**years
    return pv
def irr(oc0, g, price_ev):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid=(lo+hi)/2
        if value(oc0, g, mid) > price_ev: lo=mid
        else: hi=mid
    return mid
ND = 3875 - 459   # borrowings at 2026-07-03 (10-Q Note 8, principal) less cash
EV = SH*PRICE + ND
print(f"\nNet debt {ND}; market cap {SH*PRICE:.1f}; EV at price {EV:.1f}")
cases = {"no growth (organic pair, bottom)": (mean5, 0.0), f"organic growth {100*g_org:.2f}% (organic pair, top)": (mean5, g_org)}
side = {"FY2025 alone, no growth": (rows[2025][2], 0.0), "FY2025 alone, organic growth": (rows[2025][2], g_org)}
def show(name, oc0, g):
    v = value(oc0, g, R); ps = (v-ND)/SH; ret = irr(oc0, g, EV)
    v10 = value(oc0, g, FLOOR); ps10 = (v10-ND)/SH
    print(f"  {name:55s} EV {v:8.0f}  per share {ps:7.2f}  expected return at price {100*ret:5.2f}%  at 10%: EV {v10:7.0f} per share {ps10:6.2f}")
    return ps, ps10
print("RANGE (central, organic pair, all-equity):")
res = [show(n, *c) for n, c in cases.items()]
print(f"  range {res[0][0]:.2f} to {res[1][0]:.2f}; width {res[1][0]/res[0][0]:.2f}x; FAIR (all-equity) {(res[0][1]+res[1][1])/2:.2f}")
print("BESIDE:")
for n, c in side.items(): show(n, *c)
# Equity-only: owner cash after interest at the current run-rate (10-Q: Q3 FY2026 interest expense and other, net $62M x 4), after tax
INT = 62*4*(1-T)
print(f"\nEQUITY-ONLY: interest run-rate after tax {INT:.1f}")
for n,(oc0,g) in cases.items():
    oce = oc0-INT
    v=value(oce,g,R)/SH; v10=value(oce,g,FLOOR)/SH; ret=irr(oce,g,SH*PRICE)
    print(f"  {n:55s} per share {v:7.2f}  return at price {100*ret:5.2f}%  at 10% per share {v10:6.2f}")
e = [value(mean5-INT,c[1],FLOOR)/SH for c in cases.values()]
print(f"  FAIR (equity-only) {(e[0]+e[1])/2:.2f}")
# MARPA beside: sold receivables outstanding to the purchaser at 2026-07-03 $300M, treated as debt
print(f"\nBESIDE, MARPA $300M counted in net debt: fair all-equity {((value(mean5,0,FLOOR)-ND-300)/SH + (value(mean5,g_org,FLOOR)-ND-300)/SH)/2:.2f}")
