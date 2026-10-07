"""Rebuilt owner-earnings band for SWK.

(c) ends, both from the filed cash-flow statement:
  DEP   = depreciation and amortization of PROPERTY, PLANT AND EQUIPMENT (incl. capitalised
          software), NOT amortisation of acquired intangibles. [E3-44] names "the depreciation
          charge" as the proxy; acquired-intangible amortisation is a purchase-accounting charge
          that [E2-23] item (b) adds back, so it cannot also stand in for maintenance capex.
  CAPEX = "Capital and software expenditures".
SBC = the cash-flow add-back (equals the equity-statement line FY2023-25).
ESOP share release FY2017-19 is shown separately, not netted, because it is an estimate.
Trade working capital (TWC) = AR + inventories + AP lines of the cash-flow statement.
Newest vintage throughout.
"""
import sys, json, statistics
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources

facts = sources.sec_facts("0000093556")
A = lambda t: sources.annual(facts, t, vintage="newest")[0]
ocf = A(["NetCashProvidedByUsedInOperatingActivities"])
capex = A(["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsToAcquireProductiveAssets"])
sbc = A(["ShareBasedCompensation"])
dep_ppe = A(["DepreciationDepletionAndAmortization"])  # FY2020+ : PP&E-only line
dep = A(["Depreciation"])                               # earlier years
ar = A(["IncreaseDecreaseInAccountsReceivable"])
inv = A(["IncreaseDecreaseInInventories"])
ap = A(["IncreaseDecreaseInAccountsPayable"])
div = A(["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"])

FY = {  # fiscal-year label -> period end
 "2008": "2009-01-03", "2009": "2010-01-02", "2010": "2011-01-01", "2011": "2011-12-31",
 "2012": "2012-12-29", "2013": "2013-12-28", "2014": "2015-01-03", "2015": "2016-01-02",
 "2016": "2016-12-31", "2017": "2017-12-30", "2018": "2018-12-29", "2019": "2019-12-28",
 "2020": "2021-01-02", "2021": "2022-01-01", "2022": "2022-12-31", "2023": "2023-12-30",
 "2024": "2024-12-28", "2025": "2026-01-03"}
ESOP_RELEASE = {"2017": 133694 * 138.60 / 1e6, "2018": 207049 * 139.45 / 1e6,
                "2019": 226212 * 138.67 / 1e6}

rows = {}
print(f"{'FY':>4} {'OCF':>9} {'SBC':>6} {'capex':>7} {'depPPE':>7} {'OE@dep':>9} {'OE@capex':>9} "
      f"{'dTWC(cash)':>10} {'dAP':>8} {'AP/OCF':>7} {'div':>6} {'ESOP rel':>8}")
for fy, e in FY.items():
    d = dep_ppe.get(e, dep.get(e))
    if e not in ocf or d is None or e not in capex:
        continue
    s = sbc.get(e, 0.0)
    # XBRL IncreaseDecrease sign: an ASSET increase is positive (a cash use), a LIABILITY
    # increase is positive (a cash source). Cash effect = -dAR - dInv + dAP. First version of
    # this script summed them raw and printed the wrong sign; caught against the FY2025
    # statement (AR +190.0, Inventories +258.5, AP -284.6 = +163.9 cash).
    twc = -(ar.get(e, 0) or 0) - (inv.get(e, 0) or 0) + (ap.get(e, 0) or 0)
    r = dict(ocf=ocf[e], sbc=s, capex=capex[e], dep=d,
             oe_dep=ocf[e] - s - d, oe_capex=ocf[e] - s - capex[e],
             twc=twc, ap=ap.get(e), div=div.get(e))
    rows[fy] = r
    print(f"{fy:>4} {r['ocf']:>9,.1f} {s:>6,.1f} {r['capex']:>7,.1f} {d:>7,.1f} {r['oe_dep']:>9,.1f} "
          f"{r['oe_capex']:>9,.1f} {twc:>10,.1f} {r['ap'] or 0:>8,.1f} "
          f"{100*(r['ap'] or 0)/r['ocf']:>6.0f}% {r['div'] or 0:>6,.1f} {ESOP_RELEASE.get(fy, 0):>8,.1f}")

ys = list(rows)


def band(sel, norm=False):
    lo = [min(rows[y]["oe_dep"], rows[y]["oe_capex"]) - (rows[y]["twc"] if norm else 0) for y in sel]
    hi = [max(rows[y]["oe_dep"], rows[y]["oe_capex"]) - (rows[y]["twc"] if norm else 0) for y in sel]
    # per-end means (a single (c) choice held across the window), as the screen does it
    md = statistics.fmean(rows[y]["oe_dep"] - (rows[y]["twc"] if norm else 0) for y in sel)
    mc = statistics.fmean(rows[y]["oe_capex"] - (rows[y]["twc"] if norm else 0) for y in sel)
    return min(md, mc), max(md, mc)


print("\n--- EVERY CONTIGUOUS WINDOW OF 3+ YEARS, both (c) ends, as filed ---")
allw = []
for i in range(len(ys)):
    for j in range(i + 3, len(ys) + 1):
        sel = ys[i:j]
        lo, hi = band(sel)
        allw.append((sel[0], sel[-1], lo, hi))
print("windows:", len(allw))
print("min lo: %s-%s %.1f" % min(((a, b, l) for a, b, l, h in allw), key=lambda x: x[2]))
print("max hi: %s-%s %.1f" % max(((a, b, h) for a, b, l, h in allw), key=lambda x: x[2]))

print("\n--- TRAILING WINDOWS ending FY2025 ---")
for n in range(3, len(ys) + 1):
    sel = ys[-n:]
    lo, hi = band(sel)
    print(f"  FY{sel[0]}-FY{sel[-1]} ({n}y): {lo:>9,.1f} to {hi:>9,.1f}")

print("\n--- NAMED WINDOWS ---")
named = {
    "A current perimeter FY2023-25 (post-Security 2022-07-05, MTD in base)": ["2023", "2024", "2025"],
    "B full inventory cycle, corpus 5y default FY2021-25": ["2021", "2022", "2023", "2024", "2025"],
    "C FY2022-25 (post-MTD first full year)": ["2022", "2023", "2024", "2025"],
    "D pre-shock five FY2015-19": ["2015", "2016", "2017", "2018", "2019"],
    "E FY2020-25 incl. COVID wave": ["2020", "2021", "2022", "2023", "2024", "2025"],
}
for k, sel in named.items():
    lo, hi = band(sel)
    nlo, nhi = band(sel, norm=True)
    cum_c = sum(rows[y]["oe_capex"] for y in sel)
    cum_d = sum(rows[y]["oe_dep"] for y in sel)
    cum_div = sum(rows[y]["div"] or 0 for y in sel)
    twc = sum(rows[y]["twc"] for y in sel)
    print(f"{k}\n   as filed {lo:,.1f} to {hi:,.1f} | ex trade-WC change {nlo:,.1f} to {nhi:,.1f}"
          f" | cumulative OE {cum_c:,.1f} (capex) / {cum_d:,.1f} (dep) | dividends {cum_div:,.1f}"
          f" | cum trade-WC cash {twc:,.1f}")

json.dump(rows, open(r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\_research 2026-09-12 SWK\rebuild_rows.json", "w"), indent=1)
