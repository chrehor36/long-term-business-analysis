"""ELUXY run 2026-10-17: owner cash and the Q7 COMPUTATION (NOT A CLEARANCE).
Every input is a line from the AB Electrolux annual reports (English, as distributed via Cision)
or the Q2 2026 interim report; sources are named in the run file. SEKm unless stated."""
T = 0.206   # Swedish statutory rate (AR2025 Note 10, Parent Company theoretical rate) - CONVENTION for the interest tax shield
SOV = 0.03162  # Riksbank SEGVB10YC, 2026-10-16
FLOOR = 0.10

# Cash flow from operations and investments (statement line, includes acquisitions/divestments)
cfoi = {2019: 321, 2020: 6816, 2021: 244, 2022: -9236, 2023: -355, 2024: -79, 2025: -1508}
# same, excluding acquisitions and divestment of operations (eleven-year review, AR2025 p.178)
cfoi_x = {2016: 7432, 2017: 5229, 2018: 2149, 2019: 348, 2020: 6824, 2021: 1250, 2022: -8868,
          2023: -355, 2024: -1051, 2025: -1502}
lease = {2016: 0, 2017: 0, 2018: 0, 2019: 870, 2020: 911, 2021: 880, 2022: 960, 2023: 1111, 2024: 1157, 2025: 1135}
# financial items paid, net (cash flow statements 2019-2025); 2016-2018 = operating income less income
# after financial items (eleven-year review), an accrual stand-in, labelled in the run file
fin = {2016: 693, 2017: 441, 2018: 423, 2019: 656, 2020: 596, 2021: 470, 2022: 1238, 2023: 2039, 2024: 1764, 2025: 1808}
sales = {2016: 121093, 2017: 120771, 2018: 124129, 2019: 118981, 2020: 115960, 2021: 125631, 2022: 134880,
         2023: 134451, 2024: 136150, 2025: 131282}

def eq(y, x=False):
    return (cfoi_x[y] if x else cfoi[y]) - lease[y]
def unlev(y, x=False):
    return eq(y, x) + fin[y] * (1 - T)

W = range(2021, 2026)
print("Five-year window, acquisitions and divestments deducted (default pair):")
for y in W:
    print(y, "equity-only", eq(y), "unlevered", round(unlev(y)))
e5 = sum(eq(y) for y in W) / 5; u5 = sum(unlev(y) for y in W) / 5
print("avg equity-only", round(e5), "avg unlevered", round(u5))
h1 = (unlev(2021) + unlev(2022)) / 2; h2 = (unlev(2024) + unlev(2025)) / 2
print("halves (unlevered) first 2021-22", round(h1), "second 2024-25", round(h2))
print("Organic pair (acquisitions/divestments left out):", [round(unlev(y, True)) for y in W], round(sum(unlev(y, True) for y in W)/5))

D = range(2016, 2026)
u10 = sum(unlev(y, True) for y in D) / 10; e10 = sum(eq(y, True) for y in D) / 10
c1 = sum(unlev(y, True) for y in range(2016, 2021)) / 5; c2 = sum(unlev(y, True) for y in range(2021, 2026)) / 5
print("Ten-year cycle base (excl. acq/div; includes Professional to its 2020 distribution): unlevered", round(u10), "equity-only", round(e10))
print("cycle halves unlevered 2016-20", round(c1), "2021-25", round(c2), "growth between halves (5 yrs)", round((c2/c1) if c1 else 0, 3))

NFD = 21035   # financial net debt, 30 June 2026 (Q2 2026 report), leases and pension surplus left out
LEASES = 3749
SH = 811.489  # million B+A shares outstanding after the rights issue, excluding treasury
PRICE = 27.60; USDSEK = 9.908459663391113; ADR_RATIO = 2

def ng(cash, r):   # no growth forever
    return cash / r
for label, cash in [("five-year no-growth (the only case: series changes sign)", u5), ("ten-year cycle base no-growth (top)", u10)]:
    for r in (SOV, FLOOR):
        ev = ng(cash, r); eqv = ev - NFD
        print(f"{label} at {r:.4%}: EV {ev:,.0f}  equity {eqv:,.0f}  per share {eqv/SH:,.2f}  (with leases in debt {(eqv-LEASES)/SH:,.2f})")
# equity-only basis
for label, cash in [("five-year equity-only", e5), ("ten-year equity-only", e10)]:
    for r in (SOV, FLOOR):
        print(f"{label} at {r:.4%}: equity {cash/r:,.0f} per share {cash/r/SH:,.2f}")
mcap = PRICE * SH
print("market cap SEKm", round(mcap), "EV (financial net debt)", round(mcap + NFD))
print("owner cash needed for 10% on EV, no growth:", round((mcap + NFD) * 0.10))
print("ADR implied USD", round(PRICE * ADR_RATIO / USDSEK, 3))
fair5 = (ng(u5, FLOOR) - NFD) / SH
fair10 = (ng(u10, FLOOR) - NFD) / SH
print("fair price five-year (single case) SEK/share", round(fair5, 2), "USD/ADR", round(fair5*2/USDSEK, 2))
print("fair price cycle-base top SEK/share", round(fair10, 2))
print("max owner cash share of sales in ten years:", max(round(unlev(y, True)/sales[y]*100, 1) for y in D))

# ---- cycle bases under specific (a): the window's first year 2021 is the filer's "record year" (peak)
cfoi_x[2015] = 4955; lease[2015] = 0; fin[2015] = 640   # 2015: operating income 2,741 less income after financial items 2,101
def cyc(a, b):
    return sum(unlev(y, True) for y in range(a, b + 1)) / (b - a + 1)
for a, b, name in [(2015, 2019, "trough-to-trough 2015-2019"), (2019, 2023, "trough-to-trough 2019-2023 (last full cycle)"),
                   (2017, 2021, "peak-to-peak 2017-2021"), (2016, 2025, "ten years 2016-2025")]:
    c = cyc(a, b)
    v_s = (c / SOV - NFD) / SH; v_f = (c / FLOOR - NFD) / SH
    print(f"{name}: owner cash {c:,.0f}; value at sovereign {v_s:,.2f}/sh; at 10% {v_f:,.2f}/sh; return on EV at price {c/(mcap+NFD):.2%}")
EV = mcap + NFD
print("EV at price", round(EV))
# Whirlpool comparison (10-K XBRL, USD m)
wsales = {2016: 20718, 2017: 21253, 2018: 21037, 2019: 20419, 2020: 19456, 2021: 21985, 2022: 19724, 2023: 19455, 2024: 16607, 2025: 15524}
wop = {2016: 1354, 2017: 1136, 2018: 279, 2019: 1571, 2020: 1623, 2021: 2348, 2022: -1056, 2023: 1015, 2024: 143, 2025: 838}
wcfo = {2016: 1203, 2017: 1264, 2018: 1229, 2019: 1230, 2020: 1500, 2021: 2176, 2022: 1390, 2023: 915, 2024: 835, 2025: 470}
wcap = {2016: 660, 2017: 684, 2018: 590, 2019: 532, 2020: 410, 2021: 525, 2022: 570, 2023: 549, 2024: 451, 2025: 389}
eop = {2016: 6274, 2017: 7407, 2018: 5310, 2019: 3189, 2020: 5778, 2021: 6801, 2022: -215, 2023: -2988, 2024: 1100, 2025: 3657}
print("year  ELUX op margin  WHR op margin  WHR CFO-capex")
for y in D:
    print(y, round(eop[y]/sales[y]*100, 1), round(wop[y]/wsales[y]*100, 1), wcfo[y]-wcap[y])
print("10y avg op margin ELUX", round(sum(eop[y] for y in D)/sum(sales[y] for y in D)*100, 2), "WHR", round(sum(wop[y] for y in D)/sum(wsales[y] for y in D)*100, 2))
print("10y owner cash/sales ELUX unlevered", round(sum(unlev(y, True) for y in D)/sum(sales[y] for y in D)*100, 2))
e1923 = sum(eq(y, True) for y in range(2019, 2024)) / 5
print("equity-only 2019-2023 avg", round(e1923), "at 10% per share", round(e1923/FLOOR/SH, 2), "at sovereign", round(e1923/SOV/SH, 2))
print("central fair price SEK/B", round((cyc(2019,2023)/FLOOR - NFD)/SH, 2), "USD/ADR", round(2*(cyc(2019,2023)/FLOOR - NFD)/SH/USDSEK, 2))

# ---- cycles defined on the owner-cash series itself (specific (a): "The series that defines the cycle is owner cash")
print("unlevered owner cash series excl. acq/div:", {y: round(unlev(y, True)) for y in range(2015, 2026)})
for a, b, name in [(2019, 2022, "LAST TROUGH-TO-TROUGH on owner cash 2019-2022 (central)"), (2016, 2020, "last peak-to-peak on owner cash 2016-2020 (2016-2018 include Electrolux Professional)")]:
    c = cyc(a, b)
    print(f"{name}: owner cash {c:,.0f}; value at sovereign {(c/SOV-NFD)/SH:,.2f}/sh; fair (10%) {(c/FLOOR-NFD)/SH:,.2f}/sh = USD {2*(c/FLOOR-NFD)/SH/USDSEK:,.2f}/ADR; return on EV at price {c/EV:.2%}")
    ee = sum(eq(y, True) for y in range(a, b + 1)) / (b - a + 1)
    print(f"   equity-only: owner cash {ee:,.0f}; at 10% {ee/FLOOR/SH:,.2f}/sh; at sovereign {ee/SOV/SH:,.2f}/sh; return on market cap {ee/mcap:.2%}")
