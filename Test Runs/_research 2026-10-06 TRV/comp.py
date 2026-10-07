"""TRV: the eleven year-end balance sheets (Q4, read before the income account), and the sector method's component 2
by year (Q4 step 2 and A5: investment income and realized gains out; the calendar underwriting result replaced by the
accident-year developed result from uw_float.py).
Inputs: cache/companyfacts.json (XBRL; cross-checked to the filed statements for 2023 to 2025); uw_float.py.
Usage: python -I comp.py
"""
import json
import os
import sys
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uw_float as U  # noqa: E402

D = json.load(open("cache/companyfacts.json"))["facts"]["us-gaap"]


def inst(tag):
    u = list(D[tag]["units"].values())[0]
    out = {}
    for x in sorted(u, key=lambda x: x["filed"], reverse=True):
        if x.get("form") == "10-K" and "start" not in x:
            out.setdefault(int(x["end"][:4]), x["val"] / 1e6)
    return out


def dur(tag):
    u = list(D[tag]["units"].values())[0]
    out = {}
    for x in sorted(u, key=lambda x: x["filed"], reverse=True):
        if x.get("form") == "10-K" and "start" in x:
            s, e = date.fromisoformat(x["start"]), date.fromisoformat(x["end"])
            if 340 < (e - s).days < 380:
                out.setdefault(int(x["end"][:4]), x["val"] / 1e6)
    return out


def main():
    eq, gw, inv = inst("StockholdersEquity"), inst("Goodwill"), inst("Investments")
    res, upr = inst("LiabilityForClaimsAndClaimsAdjustmentExpense"), inst("UnearnedPremiums")
    prm, debt = inst("PremiumsReceivableAtCarryingValue"), inst("DebtLongtermAndShorttermCombinedAmount")
    aoci = inst("AccumulatedOtherComprehensiveIncomeLossNetOfTax")
    nwp = dur("PremiumsWrittenNet")
    print("BALANCE SHEETS, year-end, USD M (XBRL, latest filing per date)")
    print("yr   investments  reserves    UPR  prem.recv  debt  goodwill  AOCI   equity  eq-AOCI  prem.recv/NWP")
    for y in range(2015, 2026):
        print(f"{y} {inv[y]:11.0f} {res[y]:9.0f} {upr[y]:6.0f} {prm[y]:9.0f} {debt.get(y, float('nan')):6.0f} "
              f"{gw[y]:8.0f} {aoci.get(y, float('nan')):6.0f} {eq[y]:8.0f} {eq[y]-aoci.get(y, 0):8.0f} "
              f"{prm[y]/nwp[y]:10.3f}")
    pre, tax = dur("IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest"), dur("IncomeTaxExpenseBenefit")
    nii, rg = dur("NetInvestmentIncome"), dur("RealizedInvestmentGainsLosses")
    print()
    print("COMPONENT 2 (operating earnings other than investments), pre-tax USD M")
    print("yr   pretax    NII  realized  C2(calendar)  cal.UW  non-UW items  AY-dev UW  C2(AY basis)  eff.tax")
    rows = {}
    for y in range(2016, 2026):
        p, cr, cy, pyd = U.CAL[y]
        cal = p * (1 - cr / 100)
        c2c = pre[y] - nii[y] - rg.get(y, 0)
        non = c2c - cal
        rows[y] = c2c, non
    dev, _ = U.dev_by_ay()
    out = {}
    for y in range(2016, 2026):
        p, cr, cy, pyd = U.CAL[y]
        cal = p * (1 - cr / 100)
        ayd = cal + pyd - dev.get(y, 0)
        c2c, non = rows[y]
        c2a = ayd + non
        t = tax[y] / pre[y]
        out[y] = dict(c2c=c2c, c2a=c2a, non=non, t=t, pre=pre[y], tax=tax[y])
        print(f"{y} {pre[y]:7.0f} {nii[y]:6.0f} {rg.get(y, 0):8.0f} {c2c:12.0f} {cal:7.0f} {non:12.0f} {ayd:9.0f} "
              f"{c2a:12.0f} {t*100:6.1f}%")
    ys = range(2021, 2026)
    tp = sum(out[y]["tax"] for y in ys) / sum(out[y]["pre"] for y in ys)
    a_c = sum(out[y]["c2c"] for y in ys) / 5
    a_a = sum(out[y]["c2a"] for y in ys) / 5
    a_non = sum(out[y]["non"] for y in ys) / 5
    print()
    print(f"2021-2025: effective tax {tp*100:.1f}% (sum of tax / sum of pre-tax)")
    print(f"  five-year mean C2 calendar pre-tax {a_c:.0f}; AY basis pre-tax {a_a:.0f}; non-UW items {a_non:.0f}")
    print(f"  after tax at {tp*100:.1f}%: calendar {a_c*(1-tp):.0f}; AY basis {a_a*(1-tp):.0f}; non-UW {a_non*(1-tp):.0f}")
    print(f"  after tax at 21%: calendar {a_c*0.79:.0f}; AY basis {a_a*0.79:.0f}")
    ys10 = range(2016, 2026)
    print(f"  ten-year mean C2 AY basis pre-tax {sum(out[y]['c2a'] for y in ys10)/10:.0f}; mature 2016-2023 "
          f"{sum(out[y]['c2a'] for y in range(2016, 2024))/8:.0f}")
    print(f"  growth of aggregate C2 (AY basis) 2021->2025: {(out[2025]['c2a']/out[2021]['c2a'])**0.25-1:.3%} a year; "
          f"2016->2025: {(out[2025]['c2a']/out[2016]['c2a'])**(1/9)-1:.3%}")


if __name__ == "__main__":
    main()
