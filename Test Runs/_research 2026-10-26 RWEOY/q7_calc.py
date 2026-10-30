"""Q7 COMPUTATION, NOT A CLEARANCE, for RWEOY (all figures EUR million unless stated).
Inputs from RWE annual reports 2021-2025 (five-year overview, cash flow statements) and H1 2026 interim."""
cfo  = {2021:7274, 2022:2406, 2023:4223, 2024:6620, 2025:4954}
capex= {2021:3769, 2022:4484, 2023:9979, 2024:11240, 2025:10810}   # PP&E+intangibles+financial assets/acquisitions
disp = {2021:1057, 2022:110, 2023:1162, 2024:514, 2025:360}        # = FCF - CFO + capex (filer's FCF definition)
fcf  = {2021:4562, 2022:-1968, 2023:-4594, 2024:-4106, 2025:-5496}
da   = {2021:3650-2185, 2022:6310-4568, 2023:7749-5802, 2024:5680-3561, 2025:5087-2868}  # adj EBITDA - adj EBIT
mino = {2021:730-575, 2022:913-609, 2023:943-669, 2024:262, 2025:223}  # dividends to non-controlling interests
yrs = sorted(cfo)
for y in yrs: assert cfo[y]-capex[y]+disp[y]==fcf[y], y
allsp = {y: fcf[y]-mino[y] for y in yrs}                 # owner cash after ALL spending, equity-only
maint = {y: cfo[y]-da[y]-mino[y] for y in yrs}           # owner cash after maintenance guess (= operating D&A)
grow  = {y: capex[y]-disp[y]-da[y] for y in yrs}         # net growth spending above maintenance
avg = lambda d: sum(d.values())/len(d)
print("all-spending owner cash", allsp, "avg", avg(allsp))
print("maintenance owner cash", maint, "avg", avg(maint))
print("growth spending", grow, "avg", avg(grow))
# growth measured between halves (first year aberrational: crisis variation margins)
h1 = (maint[2021]+maint[2022])/2; h2 = (maint[2024]+maint[2025])/2
g_half = (h2/h1)**(1/3)-1
g_lit = (maint[2025]/maint[2021])**(1/4)-1
print(f"halves {h1:.0f} -> {h2:.0f}, g={g_half:.4f}; literal end years g={g_lit:.4f}")
r_gov = 0.0362
shares = 743.841217 + 36.143952   # million, after June 2026 placement, no treasury shares
price = 55.62
mcap = price*shares
net_debt = (23473+504) - 14996 + 1800   # financial debt (full hybrid) - financial assets, 30 Jun 2026, + July Amprion tranche
capint = {2021:0, 2022:0, 2023:0, 2024:217, 2025:798}   # borrowing costs capitalised into capex (2021-2023 not found: 0, confessed)
# net cash interest inside CFO (expense less income; 2021-2023 the filer reports interest and dividends together)
netint = {2021:284-263, 2022:428-381, 2023:923-842, 2024:751-506, 2025:438-506}
int_at = sum((netint[y]+capint[y])*0.8 for y in netint)/5   # after-tax at RWE's own 20% planning rate
print("after-tax interest cost added back for all-equity:", round(int_at,1))
def pv(base, g, spend, rate, years=10):
    v = 0.0; c = base; s = spend
    for t in range(1, years+1):
        c *= (1+g); s *= (1+g)
        v += (c - s)/(1+rate)**t
    v += (c/rate)/(1+rate)**years       # after year 10: zero growth, growth spending stops
    return v
base = avg(maint) - avg(capint); spend = avg(grow) - avg(capint)
print('equity-only base', round(base,1), 'growth spending', round(spend,1), 'yr1', round(spend*(1+g_half),0), 'yr10', round(spend*(1+g_half)**10,0))
for label, add in (("equity-only", 0.0), ("all-equity", int_at)):
    b = base + add
    top_g  = b/r_gov                      # maintenance-only, no growth (top: growth bought worth less than cost)
    bot_g  = pv(b, g_half, spend, r_gov)  # growth case with growth spending grown, stopped at year 10
    top_10 = b/0.10; bot_10 = pv(b, g_half, spend, 0.10)
    nd = net_debt if add else 0.0
    ps = lambda v: (v-nd)/shares
    print(f"{label}: range at gov rate {ps(bot_g):.2f} to {ps(top_g):.2f} EUR/share; at 10%: {ps(bot_10):.2f} / {ps(top_10):.2f}; fair = {(ps(bot_10)+ps(top_10))/2:.2f}")
    ev = mcap + nd
    print(f"   yield on price, no-growth maintenance case: {b/ev:.4f}; all-spending avg: {(avg(allsp)+add)/ev:.4f}")
    # literal window beside: all-spending owner cash, no growth
    print(f"   literal all-spending no-growth value per share at gov rate: {ps((avg(allsp)+add)/r_gov):.2f}")
print(f"mcap {mcap:.0f}, net debt {net_debt}, shares {shares:.3f}m")
# expected return at the price for each case (rate at which the case's value equals the price)
def irr(fn, target):
    lo, hi = 0.0362, 0.30
    for _ in range(200):
        mid = (lo+hi)/2
        if fn(mid) > target: lo = mid
        else: hi = mid
    return mid
for label, add, nd in (("equity-only", 0.0, 0.0), ("all-equity", int_at, net_debt)):
    b = base+add; tgt = mcap+nd
    print(label, "return at price: no-growth", round(b/tgt,4), "; growth case", round(irr(lambda r: pv(b, g_half, spend, r), tgt),4))
