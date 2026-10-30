"""TRV: float, the two ratios, the calendar and accident-year underwriting results, and the cost of float,
under `Framework/SECTOR METHOD v5 - insurers and float companies.md` (A2 float, A3 accident-year basis, C3 window).

Inputs (all read from files in this folder):
  cache/companyfacts.json  SEC XBRL company facts (balance-sheet series; cross-checked against filed statements)
  devtables_out.txt        incurred development by accident year, parsed by devtables.py from the FY2025 and
                           FY2020 10-K claims-development tables (net of reinsurance, undiscounted)
Hand-entered from the filed 10-Ks (each figure's source is in the comment beside it).
Usage: python -I uw_float.py
"""
import json
from datetime import date

# ---- calendar figures typed from the filed 10-Ks -------------------------------------------------------------
# earned premiums (income statement), combined ratio (MD&A consolidated table or text), and the reserve
# roll-forward lines: claims arising in the current year, and the change for prior years (negative = favorable,
# includes accretion of discount, as in the roll-forward).
CAL = {
    # yr: (earned premiums, combined ratio %, current-year incurred, prior-year change)
    2016: (24534, 92.0, 15675, -680),   # 10-K FY2018 0000086312-19-000009 (CR text; roll-forward)
    2017: (25683, 97.9, 17846, -458),   # 10-K FY2018
    2018: (27059, 96.9, 18614, -406),   # 10-K FY2018
    2019: (28272, 96.5, 18854, 164),    # 10-K FY2021 0000086312-22-000013
    2020: (29044, 95.0, 19285, -267),   # 10-K FY2021
    2021: (30855, 94.5, 20698, -484),   # 10-K FY2021
    2022: (33763, 95.6, 23308, -537),   # 10-K FY2024 0000086312-25-000012
    2023: (37761, 97.0, 26159, -38),    # 10-K FY2025 0000086312-26-000065
    2024: (41941, 92.5, 27508, -548),   # 10-K FY2025
    2025: (43914, 89.9, 28051, -939),   # 10-K FY2025
}
T30 = {2016: 2.594, 2017: 2.894, 2018: 3.112, 2019: 2.580, 2020: 1.556, 2021: 2.056, 2022: 3.113,
       2023: 4.095, 2024: 4.407, 2025: 4.777}  # treasury30.py, US Treasury daily par curve, annual averages
TAX = 0.21  # CONVENTION placeholder only for display; the run applies the filer's effective rate (A4) at Q7


def xbrl_series(tag):
    d = json.load(open("cache/companyfacts.json"))["facts"]["us-gaap"][tag]
    u = list(d["units"].values())[0]
    out = {}
    for x in sorted(u, key=lambda x: x["filed"], reverse=True):  # latest filing's figure for each date wins
        if x.get("form") == "10-K" and "start" not in x:
            out.setdefault(int(x["end"][:4]), x["val"] / 1e6)
    return out


def float_table():
    res = xbrl_series("LiabilityForClaimsAndClaimsAdjustmentExpense")
    upr = xbrl_series("UnearnedPremiums")
    rec = xbrl_series("ReinsuranceRecoverablesOnPaidAndUnpaidLosses")
    pre = xbrl_series("PrepaidReinsurancePremiums")
    prm = xbrl_series("PremiumsReceivableAtCarryingValue")
    dac = xbrl_series("DeferredPolicyAcquisitionCosts")
    inv = xbrl_series("Investments")
    eq = xbrl_series("StockholdersEquity")
    rows = {}
    for y in range(2015, 2026):
        try:
            fa2 = res[y] + upr[y] - rec[y] - pre[y]
            fc1 = fa2 - prm[y] - dac[y]
            rows[y] = dict(res=res[y], upr=upr[y], rec=rec[y], pre=pre[y], prm=prm[y], dac=dac[y],
                           float_a2=fa2, float_c1=fc1, inv=inv[y], eq=eq[y])
        except KeyError as e:
            print("missing", y, e)
    return rows


def dev_by_ay():
    """later development (latest minus initial incurred) by accident year, summed over the tables.
    AY2016-2020 for the five-year tables come from the FY2020 10-K (development through 2020 only)."""
    ten = ("Business Insurance / General Liability", "Bond & Specialty Insurance / General Liability",
           "Commercial Multi-Peril", "Workers’ Compensation", "International - Canada")
    dev, cover = {}, {}
    for ln in open("devtables_out.txt", encoding="utf-8"):
        f, name, ay, a, b, n = ln.strip().split("|")[:6]
        ay, a, b = int(ay), int(a), int(b)
        use = False
        if "k2025" in f and (name in ten or ay >= 2021):
            use = True
        if "k2020" in f and name not in ten and 2016 <= ay <= 2020:
            use = True
        if use and 2016 <= ay <= 2025:
            dev[ay] = dev.get(ay, 0) + (b - a)
            cover.setdefault(ay, []).append(f"{name}:{b - a:+d}")
    return dev, cover


def main():
    ft = float_table()
    print("YEAR-END FLOAT (USD M; XBRL series, latest filing for each date)")
    print("yr   reserves   UPR  recov  ceded-UPR  float(A2)  less prem.recv+DAC = float(C1)  investments  equity  float/inv  inv/eq")
    for y, r in ft.items():
        print(f"{y} {r['res']:9.0f} {r['upr']:6.0f} {r['rec']:6.0f} {r['pre']:6.0f} {r['float_a2']:10.0f} "
              f"{r['float_c1']:12.0f} {r['inv']:12.0f} {r['eq']:7.0f} {r['float_a2']/r['inv']:9.2f} {r['inv']/r['eq']:6.2f}")
    dev, cover = dev_by_ay()
    print()
    print("UNDERWRITING (pre-tax, USD M). cal = premiums x (1 - combined ratio); AY booked = cal + prior-year change;")
    print("AY developed = AY booked - later development of that AY in the tables (positive development = adverse).")
    print("yr  premiums  CR   cal.UW  PYD(roll)  AYbooked  laterdev  AYdeveloped  AYdev/prem  avg float  cost(cal)  cost(AY)  T30")
    out = {}
    for y in range(2016, 2026):
        p, cr, cy, pyd = CAL[y]
        cal = p * (1 - cr / 100)
        ayb = cal + pyd
        ld = dev.get(y, 0)
        ayd = ayb - ld
        fl = (ft[y]["float_a2"] + ft[y - 1]["float_a2"]) / 2
        out[y] = dict(cal=cal, ayd=ayd, fl=fl, p=p)
        print(f"{y} {p:8.0f} {cr:5.1f} {cal:7.0f} {pyd:8.0f} {ayb:9.0f} {ld:8.0f} {ayd:11.0f} {ayd/p*100:9.1f}% "
              f"{fl:9.0f} {-cal/fl*100:8.2f}% {-ayd/fl*100:8.2f}% {T30[y]:.2f}%")
    mature = [y for y in range(2016, 2024)]
    print()
    for lab, ys in (("all ten 2016-2025", list(range(2016, 2026))), ("mature AY 2016-2023", mature),
                    ("first half 2016-2020", list(range(2016, 2021))), ("second half 2021-2025", list(range(2021, 2026))),
                    ("last five 2021-2025", list(range(2021, 2026)))):
        cal = sum(out[y]["cal"] for y in ys) / len(ys)
        ayd = sum(out[y]["ayd"] for y in ys) / len(ys)
        fl = sum(out[y]["fl"] for y in ys) / len(ys)
        t = sum(T30[y] for y in ys) / len(ys)
        print(f"{lab:22s} avg cal UW {cal:7.0f}  avg AY-developed UW {ayd:7.0f}  avg float {fl:7.0f}  "
              f"cost cal {-cal/fl*100:6.2f}%  cost AY {-ayd/fl*100:6.2f}%  avg T30 {t:.2f}%")
    print()
    print("coverage of later development by accident year (table:development):")
    for y in sorted(cover):
        print(y, ", ".join(cover[y]))


if __name__ == "__main__":
    main()
