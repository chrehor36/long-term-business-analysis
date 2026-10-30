import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = print

# ---------- STAGE 0 ----------
sh_cover = 999_637_371          # 10-Q cover, as of 2026-07-31, accn 0001628280-26-053388
px = 60.95                      # NYSE close 2026-09-01 (aggregator, flagged)
cap = sh_cover * px / 1e6
P("cap (filed cover shares x close)      = {:,} x {} = ${:,.0f}M".format(sh_cover, px, cap))
warr22, warrBRK = 17.9e6, 83.9e6   # 10-Q Note 9, as of 2026-06-30
fd = sh_cover + warr22 + warrBRK
P("fully diluted incl. both warrants     = {:,.0f}  (+{:.1f}%)".format(fd, (fd / sh_cover - 1) * 100))
P("cap on fully diluted shares           = ${:,.0f}M".format(fd * px / 1e6))
pref_face = 84_897 * 100_000 / 1e6
P("preferred face (84,897 x $100,000)    = ${:,.0f}M   carrying $8,287M".format(pref_face))
P("preferred liquidation pref @105k      = ${:,.0f}M".format(84_897 * 105_000 / 1e6))
P("mandatory redemption cost @110% face  = ${:,.0f}M".format(pref_face * 1.10))
P("preferred dividend 8% of face         = ${:,.0f}M/yr (filed 2025 paid: $679M)".format(pref_face * 0.08))
debt = 13743   # total debt and finance leases 2026-06-30
cash = 4188
P("EV = cap + debt&leases - cash + pref  = {:,.0f} + {} - {} + {:,.0f} = ${:,.0f}M".format(cap, debt, cash, pref_face, cap + debt - cash + pref_face))

# ---------- DIVIDEND INTEGRITY ----------
P("\n--- DIVIDEND INTEGRITY (the COLM test) ---")
divyr = {2016: 3.02, 2017: 3.06, 2018: 3.10, 2019: 3.14, 2020: 0.82, 2021: 0.04, 2022: 0.52,
         2023: 0.72, 2024: 0.88, 2025: 0.96, 2026: 1.04}
for y in sorted(divyr):
    P("  {}  ${:.2f}".format(y, divyr[y]))
P("  raw 5y CAGR 2021->2026 : {:,.1f}%  <- ANCHORED ON THE CUT YEAR".format(((1.04 / 0.04) ** (1 / 5) - 1) * 100))
P("  from pre-cut 2019 rate : {:,.1f}% p.a. over 7 years".format(((1.04 / 3.14) ** (1 / 7) - 1) * 100))
P("  current rate vs 2019   : {:+.1%}".format(1.04 / 3.14 - 1))
P("  2026 declared run-rate $1.12 (Q3 raised to $0.28); yield {:.2%} at ${}".format(1.12 / px, px))

# ---------- OWNER EARNINGS: THE SHAPE ----------
P("\n--- NINE-YEAR SERIES, screen construction (OCF - capex - SBC), $M ---")
yrs = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
ocf = [4861, 7669, 7375, 3955, 10434, 16810, 12308, 11439, 10532]   # XBRL, as filed each year
capex = [3599, 4975, 6367, 2535, 2870, 4497, 6270, 7018, 6427]
sbc = [15, 180, 196, 202, 287, 343, 443, 423, 629]   # screen's implied subtraction
scr = [o - c - s for o, c, s in zip(ocf, capex, sbc)]
for y, o, c, s, v in zip(yrs, ocf, capex, sbc, scr):
    P("  {}  OCF {:6}  capex {:5}  sbc {:4}  = {:6}".format(y, o, c, s, v))
P("  screen 9-yr mean {:,.0f} | median {:,} | min {:,} | max {:,}".format(sum(scr) / 9, sorted(scr)[4], min(scr), max(scr)))
boom = scr[4] + scr[5]
P("  FY2021+FY2022 = {:,} = {:.1%} of the nine-year total, from 2 of 9 years (22% of the window)".format(boom, boom / sum(scr)))
ex = [v for y, v in zip(yrs, scr) if y not in (2021, 2022)]
P("  seven years EXCLUDING the spike: mean {:,.0f}  ({:+.1%} vs the nine-year mean)".format(sum(ex) / 7, sum(ex) / 7 / (sum(scr) / 9) - 1))
P("  ratio max/min = {:.1f}x".format(max(scr) / min(scr)))
P("  FILED SBC is 203/213/234 for 2023/24/25, NOT 443/423/629 - the screen over-subtracts")

# ---------- WTI ----------
P("\n--- IS THE MEAN MEANINGFUL? the filer's own sensitivity ---")
sens = 240.0  # $M pre-tax cash per $1/Bbl WTI, 10-K Item 7A on the budgeted 2026 plan
wti = {2017: 50.80, 2018: 64.90, 2019: 57.03, 2020: 39.16, 2021: 67.99, 2022: 94.53, 2023: 77.62, 2024: 75.72, 2025: 64.81}
rng = max(wti.values()) - min(wti.values())
P("  10-K Item 7A: $1/Bbl WTI = ${:.0f}M of budgeted-2026 pre-tax cash; $0.50/Mcf domestic gas = $120M".format(sens))
P("  WTI range across the nine-year window: ${:.2f} (2020) to ${:.2f} (2022) = ${:.2f}".format(min(wti.values()), max(wti.values()), rng))
P("  that range x $240M/$ = ${:,.2f}bn of pre-tax cash swing".format(rng * sens / 1000))
P("  against a nine-year mean owner earnings of ${:,.2f}bn".format(sum(scr) / 9 / 1000))
P("  => the price swing inside the window is {:.1f}x the mean it is being averaged into".format(rng * sens / (sum(scr) / 9)))
P("  H1-2026 WTI $82.36 vs FY2025 $64.81: +${:.2f} x $240M = +${:,.0f}M of pre-tax cash, unearned".format(82.36 - 64.81, (82.36 - 64.81) * sens))

# ---------- PRODUCTION / SCALE ----------
P("\n--- THE OTHER WINDOW ARTIFACT: SCALE ---")
prod = {2017: 601, 2019: 720, 2020: 1364, 2021: 1166, 2022: 1175, 2023: 1223, 2024: 1327, 2025: 1434, "2Q26": 1433}
P("  Mboe/d: {}".format(prod))
P("  the window spans a company that went {} -> {} Mboe/d ({:.2f}x), via Anadarko (2019) and CrownRock (2024)".format(prod[2017], prod[2025], prod[2025] / prod[2017]))

# ---------- RESERVES ----------
P("\n--- RESERVE REPLACEMENT, from the FY2025 10-K supplemental tables ---")


def boe(o, n, g):
    return o + n + g / 6.0


R = {
    2025: dict(ext=boe(149, 100, 543), ir=boe(55, 3, 14), rev=boe(105, -55, 668), pur=boe(4, 3, 19), sal=boe(-20, -18, -113), prod=boe(266, 119, 829)),
    2024: dict(ext=boe(134, 100, 549), ir=boe(44, 2, 8), rev=boe(40, 77, 315), pur=boe(254, 200, 1016), sal=boe(-30, -10, -58), prod=boe(247, 116, 739)),
    2023: dict(ext=boe(62, 45, 273), ir=boe(18, 2, 18), rev=boe(168, 185, 319), pur=boe(14, 9, 50), sal=boe(-1, -1, -2), prod=boe(234, 103, 656)),
}
tp = 0.0
to = 0.0
trev = 0.0
tpur = 0.0
for y in (2023, 2024, 2025):
    d = R[y]
    org = d["ext"] + d["ir"]
    tp += d["prod"]
    to += org
    trev += d["rev"]
    tpur += d["pur"]
    P("  {}: production {:7.1f} MMBoe | organic (ext+improved) {:7.1f} = {:5.1%} | revisions {:+7.1f} | purchases {:7.1f}".format(y, d["prod"], org, org / d["prod"], d["rev"], d["pur"]))
P("  3-YEAR ORGANIC RESERVE REPLACEMENT = {:,.1f} / {:,.1f} = {:.1%}".format(to, tp, to / tp))
P("  3-year incl. revisions             = {:.1%}   incl. revisions AND purchases = {:.1%}".format((to + trev) / tp, (to + trev + tpur) / tp))
ed = {2025: 548 + 5586, 2024: 724 + 5084, 2023: 893 + 4500}
ci = {2025: 6577, 2024: 17957, 2023: 5936}
P("\n--- F&D COST, $/Boe ---")
for y in (2023, 2024, 2025):
    d = R[y]
    org = d["ext"] + d["ir"]
    P("  {}: drill-bit (expl+dev {:,}) / organic {:.1f}  = ${:6.2f}/Boe   | incl. revisions ${:6.2f}/Boe".format(y, ed[y], org, ed[y] / org, ed[y] / (org + d["rev"])))
P("  3-yr drill-bit excl. revisions = ${:.2f}/Boe".format(sum(ed.values()) / to))
P("  3-yr drill-bit incl. revisions = ${:.2f}/Boe".format(sum(ed.values()) / (to + trev)))
P("  3-yr ALL-IN (total costs incurred {:,}) / additions excl. revisions {:,.1f} = ${:.2f}/Boe".format(sum(ci.values()), to + tpur, sum(ci.values()) / (to + tpur)))
P("  3-yr ALL-IN incl. revisions    = ${:.2f}/Boe".format(sum(ci.values()) / (to + trev + tpur)))
dda_og = {2025: 7115, 2024: 6565, 2023: 6112}
for y in (2023, 2024, 2025):
    P("  {} book DD&A (oil and gas segment) ${:,}M / {:.1f} MMBoe = ${:.2f}/Boe".format(y, dda_og[y], R[y]["prod"], dda_og[y] / R[y]["prod"]))

P("\n--- RESERVE LIFE ---")
pd_ = {2025: boe(1537, 817, 5637), 2024: boe(1492, 839, 5157), 2023: boe(1398, 639, 4277)}
tot = {2025: boe(2162, 1150, 7745), 2024: boe(2135, 1236, 7443), 2023: boe(1940, 983, 6352)}
for y in (2023, 2024, 2025):
    P("  YE{}: proved developed {:,.0f} MMBoe / production {:.1f} = {:.2f} yr | total proved {:,.0f} = {:.2f} yr".format(y, pd_[y], R[y]["prod"], pd_[y] / R[y]["prod"], tot[y], tot[y] / R[y]["prod"]))
pud = boe(625, 333, 2108)
P("  YE2025 proved UNDEVELOPED = {:,.0f} MMBoe = {:.2f} years of production of drilling inventory".format(pud, pud / R[2025]["prod"]))

# ---------- (c) ----------
P("\n--- (c) THE DISCLOSED JUDGMENT: the anchors, ascending ---")
prodM = R[2025]["prod"]
anchors = [
    ("2026 capital plan, LOW end (10-K MD&A)", 5500),
    ("2026 capital plan, HIGH end (10-K MD&A)", 5900),
    ("H1-2026 capex annualised (10-Q cash flow, $3,143M x2)", 6286),
    ("FY2025 capex as spent (10-K cash flow)", 6427),
    ("Consolidated D&A FY2025 - the corpus DEFAULT [E3-44]", 7533),
    ("Replace 100% of production at 2025 drill-bit F&D", ed[2025] / (R[2025]["ext"] + R[2025]["ir"]) * prodM),
    ("Replace 100% at 3-yr drill-bit F&D", sum(ed.values()) / to * prodM),
    ("Replace 100% at 3-yr ALL-IN F&D&A excl. revisions", sum(ci.values()) / (to + tpur) * prodM),
]
for n, v in anchors:
    P("  {:8,.0f}   {}".format(v, n))

# ---------- OWNER EARNINGS AT CURRENT SCALE ----------
P("\n--- OWNER EARNINGS AT CURRENT SCALE, continuing operations only ---")
P("  OxyChem is GONE (closed 2026-01-02). FY2025 continuing-ops OCF = $9,606M; disc-ops OCF $926M excluded.")
base = 9606 - 234    # continuing OCF less filed SBC
P("  base: continuing OCF 9,606 - SBC 234 = {:,}".format(base))
for n, c in [("2026 plan midpoint 5,700 (holds VOLUME flat)", 5700),
             ("FY2025 capex as spent 6,427", 6427),
             ("D&A 7,533 (corpus default)", 7533),
             ("3-yr all-in F&D&A 9,884 (holds the RESERVE BASE flat)", 9884)]:
    oe = base - c
    P("    (c)={:6,}  OE={:7,}  yield on cap {:6.2%}  |  after $679M preferred: {:7,} = {:6.2%} to COMMON".format(c, oe, oe / cap, oe - 679, (oe - 679) / cap))
P("\n  H1-2026 annualised (an oil price, NOT DONE as a base): OCF cont. 6,478 x2 = 12,956")
for c in (5700, 7533, 9884):
    P("    (c)={:6,}  OE={:7,}  yield {:6.2%}".format(c, 12956 - 468 - c, (12956 - 468 - c) / cap))

# ---------- Q5 ----------
P("\n--- Q5 COMPUTATION ---")
sov = 5.25
P("  sovereign USD 30-yr {}% (FRED DGS30, observation 2026-08-31)".format(sov))
for label, oe in [("bottom boundary [E5-34]: (c)=all-in F&D&A, after preferred", 9606 - 234 - 9884 - 679),
                  ("(c)=D&A, after preferred", 9606 - 234 - 7533 - 679),
                  ("(c)=2026 plan midpoint, after preferred", 9606 - 234 - 5700 - 679)]:
    y = oe / cap
    P("  {}: OE {:,}M -> yield {:.2%} -> {:+.2f} pts vs sovereign; growth to reach the 10% floor: {:+.2f} pts".format(label, oe, y, (y - sov / 100) * 100, 10.0 - y * 100))
P("\n  capitalised-at-sovereign value, on fully diluted shares:")
for c, oe in [(5700, 9606 - 234 - 5700 - 679), (7533, 9606 - 234 - 7533 - 679), (9884, 9606 - 234 - 9884 - 679)]:
    P("    (c)={:,}: OE {:,}M / {:.4f} = ${:,.1f}bn -> ${:,.2f}/share".format(c, oe, sov / 100, oe / (sov / 100) / 1000, oe / (sov / 100) / fd * 1e6))
P("\n  at the [E4-28] 10% floor: value = OE/0.10:")
for c, oe in [(5700, 9606 - 234 - 5700 - 679), (7533, 9606 - 234 - 7533 - 679), (9884, 9606 - 234 - 9884 - 679)]:
    P("    (c)={:,}: ${:,.1f}bn -> ${:,.2f}/share".format(c, oe / 0.10 / 1000, oe / 0.10 / fd * 1e6))
