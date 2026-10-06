"""CAT 2026-10-06 run arithmetic. Inputs are transcribed from the filed 10-Ks (accessions in the run file).
Same number sooner, no number added: every input below is a filed figure; the conventions are the framework's Q7 ones."""

years = [2021, 2022, 2023, 2024, 2025]
# MP&E (ME&T before 2025) supplemental cash-flow data and free-cash-flow reconciliations, USD millions
mpe_ocf = [7177, 6358, 11688, 11437, 12278]
sbc = [200, 193, 208, 223, 242]                 # Note 3, before-tax stock-based compensation expense
mpe_capex = [1129, 1298, 1663, 1988, 2794]      # capex used in the company's FCF reconciliation (incl. MP&E leased equipment)
mpe_da = [1550, 1439, 1361, 1368, 1497]
# consolidated
c_ocf = [7198, 7766, 12885, 12035, 11739]
c_capex = [1093, 1296, 1597, 1988, 2821]
c_leased = [1379, 1303, 1495, 1227, 1465]

oc = [o - s - c for o, s, c in zip(mpe_ocf, sbc, mpe_capex)]
dv = [o - s - d for o, s, d in zip(mpe_ocf, sbc, mpe_da)]
co = [o - s - c - l for o, s, c, l in zip(c_ocf, sbc, c_capex, c_leased)]
mean = lambda x: sum(x) / len(x)
print("owner cash MP&E", oc, "mean", mean(oc))
print("depreciation variant", dv, "mean", mean(dv))
print("consolidated variant", co, "mean", mean(co))

shares = 459.674889  # million, 10-Q Q2 2026 cover
price = 848.14
rate = 0.0566
cap = price * shares
print("market cap $M", round(cap))
print("yield on mean", mean(oc) / cap, "on 2025", oc[-1] / cap)

g = (oc[-1] / oc[0]) ** (1 / 4) - 1
print("growth shown, aggregate owner cash 2021->2025 CAGR", g)


def value(base, growth, r=rate, years=10):
    """CONVENTION (Q7): base carried at growth for ten years, then zero nominal growth, discounted at the sovereign."""
    pv, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + growth)
        pv += cf / (1 + r) ** t
    pv += (cf / r) / (1 + r) ** years
    return pv


for name, base in (("MP&E mean", mean(oc)), ("consolidated mean", mean(co))):
    lo = value(base, 0.0)
    hi = value(base, g)
    print(name, "no-growth $M", round(lo), "per share", round(lo / shares, 2),
          "| shown-growth $M", round(hi), "per share", round(hi / shares, 2), "| width", round(hi / lo, 2))

# expected return at the price: the discount rate that equates the shown-growth case to the market cap
def irr(base, growth, target):
    lo_r, hi_r = 0.001, 0.5
    for _ in range(200):
        mid = (lo_r + hi_r) / 2
        if value(base, growth, mid) > target:
            lo_r = mid
        else:
            hi_r = mid
    return mid

print("implied return at price, shown growth", irr(mean(oc), g, cap), "no growth", irr(mean(oc), 0.0, cap))
# price at which each case clears the ten percent floor (CONVENTION)
fair = value(mean(oc), g, 0.10) / shares
cheap = value(mean(oc), 0.0, 0.10) / shares
print("price at which shown-growth case returns 10%:", round(fair, 2), "; no-growth case returns 10%:", round(cheap, 2))
