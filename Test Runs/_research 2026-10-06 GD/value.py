"""GD arithmetic for the run: owner cash, growth shown, the Q7 range under the v5 CONVENTION
(five-year mean of owner cash after every real cost, carried at the growth shown for ten years, then zero nominal
growth, discounted at the US Treasury 30-year par yield). All inputs are filed figures (10-K cash-flow statements,
accessions in the run file) or the tool outputs saved beside this script. Arithmetic only, no verdict."""

ocf = {2021: 4271, 2022: 4579, 2023: 4710, 2024: 4112, 2025: 5120}
sbc = {2021: 126, 2022: 165, 2023: 181, 2024: 183, 2025: 196}
capex = {2021: 887, 2022: 1114, 2023: 904, 2024: 916, 2025: 1161}
lease_principal = {2023: 55, 2024: 64, 2025: 556}   # financing section; 2025 includes ~490 lease buy-out
rate = 0.0566            # UST 30y par yield 2026-10-05
price = 331.72           # close 2026-10-05, aggregator (Yahoo via tools), flagged
shares = 270.557195      # millions, 10-Q cover 2026-07-05, 0000040533-26-000032
net_debt_note = "debt 7,516 less cash 4,333 at 2026-07-05 (10-Q); not deducted: owner cash is after interest"

oc = {y: ocf[y] - sbc[y] - capex[y] for y in ocf}
mean5 = sum(oc.values()) / 5
oc_alt = {y: oc[y] - lease_principal.get(y, 0) for y in oc}
mean5_alt = sum(oc_alt.values()) / 5
print("owner cash by year:", oc, " mean", round(mean5, 1))
print("alt (less finance-lease principal where known):", oc_alt, " mean", round(mean5_alt, 1))
g_end = (oc[2025] / oc[2021]) ** 0.25 - 1
# least-squares log-linear slope over the five years
import math
xs = list(oc); ys = [math.log(oc[y]) for y in xs]
xm = sum(xs) / 5; ym = sum(ys) / 5
slope = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sum((x - xm) ** 2 for x in xs)
g_ls = math.exp(slope) - 1
print(f"growth shown: endpoints 2021-2025 {g_end:.4f}; log-linear fit {g_ls:.4f}")
# long record of aggregate owner cash, 2008 vs 2025 (filed series, series_gd.txt)
oc2008 = 3124 - 105 - 490
print(f"long record 2008 {oc2008} -> 2025 {oc[2025]}: {(oc[2025]/oc2008)**(1/17)-1:.4f} a year")
cap = price * shares
print(f"market cap {cap:,.0f}M; owner-cash yield {mean5/cap:.4f}; alt {mean5_alt/cap:.4f}")


def value(base, g, r=rate, years=10):
    pv = 0.0; c = base
    for t in range(1, years + 1):
        c *= (1 + g); pv += c / (1 + r) ** t
    pv += c / r / (1 + r) ** years       # zero nominal growth after year ten
    return pv


for label, base in (("mean", mean5), ("alt", mean5_alt)):
    lo = base / rate
    hi_end = value(base, g_end); hi_ls = value(base, g_ls)
    print(f"{label}: no-growth {lo:,.0f}M = ${lo/shares:,.0f}/sh; shown growth (endpoints) {hi_end:,.0f}M = "
          f"${hi_end/shares:,.0f}/sh; (fit) {hi_ls:,.0f}M = ${hi_ls/shares:,.0f}/sh")

# expected return at the price: owner-cash yield plus growth shown (after tax), and the pre-tax equivalent
tax = 0.175   # 2025 effective rate, 10-K MD&A
for g in (g_end, g_ls):
    er = mean5 / cap + g
    print(f"expected return at price, after tax {er:.4f} (yield + growth {g:.4f}); pre-tax equiv {er/(1-tax):.4f}")

# price at which the central case clears the ten percent pre-tax floor ("fair")
# and at which no-growth owner cash clears it ("cheap")
floor_after_tax = 0.10 * (1 - tax)
for g in (g_end,):
    p_fair = mean5 / (floor_after_tax - g) / shares if floor_after_tax > g else float("nan")
    print(f"fair (yield + {g:.4f} growth = {floor_after_tax:.4f} after tax): ${p_fair:,.0f}/sh")
p_cheap = mean5 / floor_after_tax / shares
print(f"cheap (no-growth owner-cash yield = {floor_after_tax:.4f}): ${p_cheap:,.0f}/sh")

# Q6 retention arithmetic: owner cash per diluted share, three-year means 2015-2017 against 2023-2025
oc_early = {2015: 2499 - 110 - 569, 2016: 2198 - 100 - 392, 2017: 3876 - 123 - 428}
dil = {2015: 326.7, 2016: 310.4, 2017: 304.6, 2023: 275.7, 2024: 277.5, 2025: 272.4}
e = sum(oc_early.values()) / 3; l = sum(oc[y] for y in (2023, 2024, 2025)) / 3
es = sum(dil[y] for y in (2015, 2016, 2017)) / 3; ls = sum(dil[y] for y in (2023, 2024, 2025)) / 3
print(f"owner cash 2015-17 mean {e:,.1f} on {es:.1f}M diluted = {e/es:.3f}/sh; 2023-25 {l:,.1f} on {ls:.1f}M = {l/ls:.3f}/sh")
print(f"per-share growth {((l/ls)/(e/es))**(1/8)-1:.4f} a year; aggregate {(l/e)**(1/8)-1:.4f} a year")
# Q6 buyback prices paid (cash paid / shares, 10-K FY2025 Note N; 10-Q Q2 2026)
for yr, cash, sh in ((2023, 434, 2.0), (2024, 1501, 5.4), (2025, 637, 2.5), ("H1 2026", 319, 0.9)):
    print(f"buyback {yr}: ${cash/sh:,.0f} a share")
# depreciation variant of the Q7 base (depreciation of plant in place of capex), 2023-2025 only
dep = {2023: 608, 2024: 644, 2025: 680}
dv = {y: ocf[y] - sbc[y] - dep[y] for y in dep}
print("depreciation variant:", dv, "mean", round(sum(dv.values()) / 3, 1),
      "no-growth value/sh", round(sum(dv.values()) / 3 / rate / shares))
dvm = sum(dv.values()) / 3
print(f"depreciation variant with shown growth {g_end:.4f}: ${value(dvm, g_end)/shares:,.0f}/sh; "
      f"expected return at price pre-tax equiv {(dvm/cap + g_end)/(1-tax):.4f}")
