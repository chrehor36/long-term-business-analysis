"""Q3 arithmetic for KO: net tangible operating capital and the pre-tax return on it, FY2016-FY2025, and the capital
added over the decade against the earnings added. XBRL 10-K facts (latest vintage), USD millions.

net tangible operating capital = trade receivables + inventories + prepaid and other current + PP&E net
                                 - accounts payable and accrued expenses - accrued income taxes
(excludes cash, investments, equity-method investments, goodwill, trademarks, assets held for sale and other noncurrent
assets, which in 2024-2025 hold the IRS deposit; FY2024 payables include the $6.1bn fairlife liability, shown both ways)
pre-tax operating income before other operating charges = operating income + other operating charges
"""
import json, os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
F = json.load(open(os.path.join(HERE, "cache", "companyfacts_KO.json")))["facts"]["us-gaap"]


def inst(tag):
    out = {}
    for r in F.get(tag, {}).get("units", {}).get("USD", []):
        if r.get("form") != "10-K" or "start" in r:
            continue
        y = int(r["end"][:4])
        if r["end"][5:] != "12-31":
            continue
        if y not in out or r["filed"] > out[y][1]:
            out[y] = (r["val"] / 1e6, r["filed"])
    return {k: v[0] for k, v in out.items()}


REC = inst("AccountsReceivableNetCurrent")
INV = inst("InventoryNet")
PRE = inst("PrepaidExpenseAndOtherAssetsCurrent")
PPE = inst("PropertyPlantAndEquipmentNet")
AP = inst("AccountsPayableAndAccruedLiabilitiesCurrent")
TAX = inst("AccruedIncomeTaxesCurrent")
OI = {2016: 8657, 2017: 7755, 2018: 9152, 2019: 10086, 2020: 8997, 2021: 10308, 2022: 10909, 2023: 11311, 2024: 9992, 2025: 13762}
OOC = {2016: 1371, 2017: 1902, 2018: 1079, 2019: 458, 2020: 853, 2021: 846, 2022: 1215, 2023: 1951, 2024: 4163, 2025: 1261}
FAIRLIFE_LIAB = {2024: 6126}  # contingent consideration in payables at 2024-12-31 (paid March 2025 at 6,173 after a 47 charge)

print(f"{'FY':>4} {'recv':>6} {'inv':>6} {'prepaid':>7} {'PP&E':>7} {'AP&acc':>7} {'acc tax':>7} {'NTOC':>7} {'OI pre-charges':>14} {'pre-tax return':>14}")
for y in range(2016, 2026):
    try:
        ntoc = REC[y] + INV[y] + PRE[y] + PPE[y] - AP[y] - TAX[y]
    except KeyError as e:
        print(y, "missing", e); continue
    adj = ntoc + FAIRLIFE_LIAB.get(y, 0)
    op = OI[y] + OOC[y]
    print(f"{y:>4} {REC[y]:>6,.0f} {INV[y]:>6,.0f} {PRE[y]:>7,.0f} {PPE[y]:>7,.0f} {AP[y]:>7,.0f} {TAX[y]:>7,.0f} {ntoc:>7,.0f} {op:>14,.0f} {op/adj*100 if adj>0 else float('nan'):>13.0f}%"
          + (f"  (NTOC with the fairlife liability taken out of payables: {adj:,.0f})" if y in FAIRLIFE_LIAB else ""))

ACQ = {2016: 838, 2017: 3809, 2018: 1040, 2019: 5542, 2020: 1052, 2021: 4766, 2022: 73, 2023: 62, 2024: 315, 2025: 461}
EXTRA = {2021: 100, 2022: 637, 2023: 275 + 311, 2025: 6173}  # fairlife milestones (all legs) and BodyArmor holdbacks in financing
DISP = {2016: 1035, 2017: 3821, 2018: 1362, 2019: 429, 2020: 189, 2021: 2180, 2022: 458, 2023: 430, 2024: 3485, 2025: 3567}
CAPEX = {2016: 2262, 2017: 1750, 2018: 1548, 2019: 2054, 2020: 1177, 2021: 1367, 2022: 1484, 2023: 1852, 2024: 2064, 2025: 2112}
DA = {2016: 1787, 2017: 1260, 2018: 1086, 2019: 1365, 2020: 1536, 2021: 1452, 2022: 1260, 2023: 1128, 2024: 1075, 2025: 1050}
EQI = {2016: 835, 2025: 2031}
yrs = range(2017, 2026)  # capital added after the 2016 base year
acq = sum(ACQ[y] + EXTRA.get(y, 0) for y in yrs)
disp = sum(DISP[y] for y in yrs)
growcap = sum(CAPEX[y] - DA[y] for y in yrs)
added = acq - disp + growcap
d_op = (OI[2025] + OOC[2025]) - (OI[2016] + OOC[2016])
d_eq = EQI[2025] - EQI[2016]
print(f"\nFY2017-FY2025: acquisitions incl. fairlife milestones and BodyArmor holdbacks {acq:,.0f}; disposals {disp:,.0f};"
      f" capex above D&A {growcap:,.0f}; net capital added {added:,.0f}")
print(f"pre-tax operating income before other charges, 2016 -> 2025: {OI[2016]+OOC[2016]:,} -> {OI[2025]+OOC[2025]:,} (+{d_op:,});"
      f" equity income {EQI[2016]:,} -> {EQI[2025]:,} (+{d_eq:,})")
print(f"pre-tax earnings added per dollar of net capital added: {(d_op + d_eq)/added*100:.0f}%  (price/mix on the existing base is inside the numerator)")
