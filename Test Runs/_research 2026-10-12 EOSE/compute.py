# COMPUTATION, NOT A CLEARANCE. EOSE owner cash and the Q7 construction, run after the Q1 STOP.
# Inputs: 10-K XBRL as filed (accessions in the run file), USD millions.
yrs  = [2021, 2022, 2023, 2024, 2025]
ocf  = [-116.147, -196.857, -145.018, -153.936, -211.190]
intp = [0.157, 5.766, 15.133, 4.395, 8.403]          # cash paid for interest
sbc  = [15.058, 13.794, 14.057, 18.780, 24.876]
capx = [15.589, 20.072, 29.323, 33.2, 54.7]          # PP&E (+ software 2024-25, per run.py)
rev  = [4.598, 17.924, 16.378, 15.606, 114.203]
cogs = [46.494, 153.260, 89.798, 98.867, 258.040]
eq_only = [o - s - c for o, s, c in zip(ocf, sbc, capx)]
all_eq  = [o + i - s - c for o, i, s, c in zip(ocf, intp, sbc, capx)]   # company tax nil; interest added back untaxed
for y, r, g, a, e in zip(yrs, rev, cogs, all_eq, eq_only):
    print(f"{y}  rev {r:8.1f}  cogs {g:8.1f}  gross margin {100*(r-g)/r:8.1f}%   owner cash all-equity {a:8.1f}  equity-only {e:8.1f}")
mA = sum(all_eq)/5; mE = sum(eq_only)/5
print(f"5-yr mean all-equity {mA:.1f}  equity-only {mE:.1f}")
# halves (specific (b)): first half 2021-22, second half 2024-25, midpoints 3 years apart
def halves(s):
    f = (s[0]+s[1])/2; l = (s[3]+s[4])/2
    return f, l, (l/f)**(1/3) - 1
fA, lA, gA = halves(all_eq); fE, lE, gE = halves(eq_only)
print(f"halves all-equity {fA:.1f} -> {lA:.1f}: losses grow {100*gA:.1f}%/yr; equity-only {fE:.1f} -> {lE:.1f}: {100*gE:.1f}%/yr")
def value(c0, g, r, n=10):
    v = 0; c = c0
    for t in range(1, n+1):
        c *= (1+g); v += c/(1+r)**t
    return v + c/r/(1+r)**n          # zero nominal growth after year ten
sov = 0.0560; floor = 0.10
shares = 364.167744
debt_principal = 948.284; debt_carrying = 617.118
cash = 305.491 + 75.0 + 37.738 - 112.638   # 30 Jun 2026 unrestricted + RDO + rights - FPUSA contribution (10-Q note 22)
nd_p = debt_principal - cash; nd_c = debt_carrying - cash
print(f"cash after stated subsequent events {cash:.1f}; net debt principal {nd_p:.1f}; carrying {nd_c:.1f}")
for label, m, g in (("all-equity", mA, gA), ("equity-only", mE, gE)):
    ng_s = value(m, 0, sov); gr_s = value(m, g, sov)
    ng_f = value(m, 0, floor); gr_f = value(m, g, floor)
    sub = nd_p if label == "all-equity" else 0.0
    ps = lambda v: (v - sub)/shares
    print(f"{label}: at sovereign no-growth {ng_s:9.1f} ({ps(ng_s):7.2f}/sh)  loss-growth {gr_s:9.1f} ({ps(gr_s):7.2f}/sh)")
    print(f"{label}: at 10%      no-growth {ng_f:9.1f} ({ps(ng_f):7.2f}/sh)  loss-growth {gr_f:9.1f} ({ps(gr_f):7.2f}/sh)  fair (avg) {(ps(ng_f)+ps(gr_f))/2:7.2f}/sh")
print("price 2.52, market cap", round(2.52*shares,1))
