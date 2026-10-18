"""LSE run 2026-10-16: arithmetic for Step 0, Q2 rows and the Q7 COMPUTATION. USD millions unless stated.
Every input is transcribed from a filed statement named beside it."""
yrs = ["FY2021", "FY2022", "FY2023", "FY2024", "FY2025"]
# cash-flow statements: DRS 0001493152-23-030098 (FY2021-22), 20-F 0001493152-26-004368 (FY2023-25)
ocf   = [12.589158, -4.386090, 4.388621, 15.068432, -3.522067]
ppe   = [1.013660, 2.853713, 0.740515, 0.681214, 0.170978]
intan = [0.0, 0.0, 0.236814, 0.034991, 0.034771]
nci   = [0.0, 0.0, 0.0, 0.0, 0.251298]          # payment for purchasing minority interests (financing section)
da    = [0.167352, 0.292847, 0.420864, 0.519006, 0.485624]
intpd = [0.0, 0.042564, 0.067964, 0.057916, 0.071194]
taxpd = [0.059068, 0.058645, 0.107926, 0.307462, 0.170515]
taxpr = [1.257727, 1.978217, 0.729506, 0.184818, -0.508978]
dtaxp = [0.602158, 0.368891, 1.942566, 0.586035, 0.429483]  # increase in taxes payable inside OCF
# share-capital-withdrawal payments to the founders named in the notes: FY2024 1.3 + 2.9;
# FY2025 the fall in the Li Hongqi balance (4.692339 - 4.254385); FY2023 not separable, left at nil
founders = [0.0, 0.0, 0.0, 4.2, 0.437954]
rev   = [31.257412, 46.716505, 73.084448, 69.073374, 48.335553]
gp    = [9.024366, 13.535535, 18.379041, 16.034519, 8.525671]
opi   = [6.249374, 8.216726, 11.890515, 7.551893, -1.665953]
eq    = [26.029746, 29.643706, 31.758575, 40.455513, 45.457500]  # total equity at year-end
eq0   = 20.259373  # total equity 2020-09-30 (DRS)
seg = {  # segment gross profit, FY2021..FY2025
    "Clean-energy equipment": [5.853391, 6.231271, 11.867463, 10.323138, 4.534238],
    "Oil and gas engineering technical services": [2.815990, 4.966560, 5.841824, 4.503111, 3.068332],
    "New energy production and operation": [0.195082, 1.707579, 0.459218, 0.648562, 0.304573],
    "Digitalization and integration equipment": [0.159903, 0.630125, 0.210536, 0.559708, 0.618528],
}
segrev = {
    "Clean-energy equipment": [19.482911, 18.697671, 39.581383, 33.816111, 22.073207],
}


def avg(x):
    return sum(x) / len(x)


P = print
P("Segment five-year gross profit (the only segment profit the filer reports):")
tot = sum(sum(v) for v in seg.values())
for k, v in seg.items():
    P(f"  {k:45s} {sum(v):7.2f}  {100*sum(v)/tot:5.1f}%  by year {[round(x, 2) for x in v]}")
P(f"  total {tot:.2f}")
for k, v in segrev.items():
    P(f"  margin {k}: {[round(100*g/r, 1) for g, r in zip(seg[k], v)]}")
P("Company gross margin %", [round(100*g/r, 1) for g, r in zip(gp, rev)], " H1FY26", round(100*5.224828/20.978428, 1))
P("Operating margin %", [round(100*o/r, 1) for o, r in zip(opi, rev)], " H1FY26", round(-100*0.688329/20.978428, 1))
eqs = [eq0] + eq
avgeq = [(eqs[i] + eqs[i+1]) / 2 for i in range(5)]
roe_op = [o*0.75/a for o, a in zip(opi, avgeq)]
P("Operating income after 25% statutory tax / average total equity %", [round(100*x, 1) for x in roe_op])
P(f"  five-year: {100*sum(o*0.75 for o in opi)/sum(avgeq):.1f}%")
oc_all = [o - p - i - n for o, p, i, n in zip(ocf, ppe, intan, nci)]
oc_mnt = [o - d - n for o, d, n in zip(ocf, da, nci)]
P("Owner cash, all spending (OCF - PP&E - intangibles - minority buyout)", [round(x, 3) for x in oc_all], "avg", round(avg(oc_all), 3))
P("Owner cash, maintenance only (OCF - D&A - minority buyout)", [round(x, 3) for x in oc_mnt], "avg", round(avg(oc_mnt), 3))
P("Owner cash all spending / average equity, five-year %", round(100*sum(oc_all)/sum(avgeq), 1))
P("avg D&A", round(avg(da), 3), " avg capex+intangibles", round(avg([p+i for p, i in zip(ppe, intan)]), 3))
P("cash tax paid", [round(x, 3) for x in taxpd], "avg", round(avg(taxpd), 3), " provision", [round(x, 3) for x in taxpr], "avg", round(avg(taxpr), 3))
intat = avg(intpd) * 0.75
P("after-tax interest add-back (25%)", round(intat, 3))
v_found = avg(founders)
v_tax = avg(dtaxp)
P("founders' capital-withdrawal payments avg", round(v_found, 3), " taxes-payable build avg", round(v_tax, 3))
cases = {
    "A all spending": avg(oc_all),
    "B maintenance only": avg(oc_mnt),
    "A + founders' payments added back": avg(oc_all) + v_found,
    "B + founders' payments added back": avg(oc_mnt) + v_found,
    "A + founders - tax-payable build": avg(oc_all) + v_found - v_tax,
    "B + founders - tax-payable build": avg(oc_mnt) + v_found - v_tax,
}
price = 4.53
sh = 17.025
mcap = price * sh
cash_sec = 10.249822 + 0.067102 + 16.898215   # 2026-03-31 cash, restricted cash, short-term investments (6-K 0001493152-26-042590)
debt = 2.890424
netdebt = debt - cash_sec
ev = mcap + netdebt
P(f"price {price} shares {sh}M mcap {mcap:.2f} cash+sec {cash_sec:.2f} debt {debt:.2f} net debt {netdebt:.2f} EV {ev:.2f}")
r_rmb, r_usd, f = 0.0206, 0.0543, 0.10
for k, c in cases.items():
    ce = c + intat  # all-equity: before interest
    P(f"  {k:36s} oc {c:6.3f} all-eq {ce:6.3f} yield/EV {100*ce/ev:5.2f}% eq-only yield {100*c/mcap:5.2f}%"
      f" val/sh @RMB {((ce/r_rmb)-netdebt)/sh:6.2f} @USD {((ce/r_usd)-netdebt)/sh:6.2f} @10% {((ce/f)-netdebt)/sh:5.2f} eq-only@10% {(c/f)/sh:5.2f}")
A = avg(oc_all) + intat
B = avg(oc_mnt) + intat
fair = ((A/f + B/f)/2 - netdebt)/sh
fair_eq = ((avg(oc_all)/f + avg(oc_mnt)/f)/2)/sh
P(f"RANGE (no growth, RMB 2.06%): {((A/r_rmb)-netdebt)/sh:.2f} to {((B/r_rmb)-netdebt)/sh:.2f} a share; at USD 5.43%: {((A/r_usd)-netdebt)/sh:.2f} to {((B/r_usd)-netdebt)/sh:.2f}")
P(f"FAIR all-equity {fair:.2f}  equity-only {fair_eq:.2f}")
# Literal window beside: growth between halves, capped by (f)
h1 = avg(oc_all[:2])
h2 = avg(oc_all[3:])
g_oc = (h2/h1)**(1/3) - 1
s1 = avg(rev[:2])
s2 = avg(rev[3:])
g_s = (s2/s1)**(1/3) - 1
maxshare = max(o/r for o, r in zip(oc_all, rev))
oc10 = A * (1+g_oc)**10
rev10 = rev[-1]*(1+g_s)**10
P(f"literal window: owner-cash halves {h1:.3f} -> {h2:.3f}, growth {100*g_oc:.1f}%; sales halves {s1:.2f} -> {s2:.2f}, growth {100*g_s:.1f}%")
P(f"  cap test: owner cash yr10 at shown growth {oc10:.1f} vs highest share of sales {100*maxshare:.1f}% x sales yr10 at sales growth {rev10:.1f} = {maxshare*rev10:.1f}")


def pv(c, g, r, n=10):
    s = sum(c*(1+g)**t/(1+r)**t for t in range(1, n+1))
    return s + c*(1+g)**n / r / (1+r)**n


for c, lab in ((A, "A"), (B, "B")):
    P(f"  literal growth case {lab} at {100*g_s:.1f}%: EV@RMB {pv(c, g_s, r_rmb):.1f} EV@10% {pv(c, g_s, f):.1f} per share @10% {(pv(c, g_s, f)-netdebt)/sh:.2f}")
lit_fair = ((A/f + pv(A, g_s, f))/2 - netdebt)/sh
lit_fair_eq = ((avg(oc_all)/f + pv(avg(oc_all), g_s, f))/2)/sh
P(f"  literal-window fair (A no-growth and A growth averaged at 10%): all-equity {lit_fair:.2f} equity-only {lit_fair_eq:.2f}")
lo, hi = 0.0001, 1.0
for _ in range(200):
    mid = (lo+hi)/2
    if pv(A, g_s, mid) > ev:
        lo = mid
    else:
        hi = mid
P(f"  expected return at the price, literal growth case A: {100*mid:.1f}%")
ttm_ocf = -3.522067 - (-1.981527) + 0.730075
P(f"TTM OCF to 2026-03-31: {ttm_ocf:.3f}")
# Recon Technology (RCON), CNY millions, years to June 30
rc_rev = {"FY2021": 47.938575, "FY2022": 83.777571, "FY2023": 67.114378, "FY2024": 68.854280, "FY2025": 66.285032, "FY2026": 109.898245}
rc_gp = {"FY2021": 7.215028, "FY2022": 19.424737, "FY2023": 18.866983, "FY2024": 20.877444, "FY2025": 15.240537, "FY2026": 36.488040}
rc_op = {"FY2021": -61.578948, "FY2022": -82.313417, "FY2023": -69.332735, "FY2024": -71.637911, "FY2025": -57.319712, "FY2026": -41.227583}
rc_ocf = {"FY2021": -34.050468, "FY2022": -26.247237, "FY2023": -51.688331, "FY2024": -43.747933, "FY2025": -33.771174, "FY2026": -58.801965}
for k in rc_rev:
    P(f"  RCON {k}: gross margin {100*rc_gp[k]/rc_rev[k]:5.1f}%  operating margin {100*rc_op[k]/rc_rev[k]:6.1f}%  OCF {rc_ocf[k]:7.1f} CNY M")
