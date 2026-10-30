#!/usr/bin/env python3
import sys, statistics
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
from datetime import date

facts = S.sec_facts("0001107843")
us = facts["facts"]["us-gaap"]

def ser(tag):
    if tag not in us: return {}
    node = us[tag]["units"]; u = list(node.keys())[0]; out = {}
    for it in node[u]:
        if it.get("form") not in ("10-K","10-K/A") or it.get("fp") != "FY": continue
        s = it.get("start"); e = it["end"]
        if not s: continue
        if not (330 <= (date.fromisoformat(e)-date.fromisoformat(s)).days <= 400): continue
        y = int(e[:4])
        if y not in out or it.get("filed","") >= out[y][1]:
            out[y] = (it["val"]/1e6, it.get("filed"))
    return {k: v[0] for k, v in out.items()}

OCF = ser("NetCashProvidedByUsedInOperatingActivities")
SBC = ser("ShareBasedCompensation")
DA  = ser("DepreciationDepletionAndAmortization")
CAP = ser("PaymentsToAcquirePropertyPlantAndEquipment")
REV = ser("RevenueFromContractWithCustomerExcludingAssessedTax")
REV2= ser("Revenues"); REV = {**REV2, **REV}
NI  = ser("NetIncomeLoss"); OI = ser("OperatingIncomeLoss")

yrs = sorted(set(OCF) & set(SBC) & set(DA) & set(CAP))
print(f"{'FY':<6}{'OCF':>9}{'SBC':>9}{'OCF-SBC':>10}{'capex':>9}{'D&A':>9}{'OE@cap':>9}{'OE@D&A':>9}{'rev':>9}{'rev g':>8}{'SBC/OCF':>9}")
rows = {}
for y in yrs:
    a = OCF[y]-SBC[y]
    oc, od = a-CAP[y], a-DA[y]
    rows[y] = (OCF[y], SBC[y], a, CAP[y], DA[y], oc, od)
    g = ""
    if y-1 in REV and y in REV: g = f"{(REV[y]/REV[y-1]-1)*100:6.1f}%"
    print(f"{y:<6}{OCF[y]:>9.1f}{SBC[y]:>9.1f}{a:>10.1f}{CAP[y]:>9.1f}{DA[y]:>9.1f}{oc:>9.1f}{od:>9.1f}"
          f"{REV.get(y,0):>9.1f}{g:>8}{SBC[y]/OCF[y]*100:>8.1f}%")

print("\n=== WINDOW GRID: mean OE, both (c) ends ===")
print(f"{'window':<16}{'n':>3}{'OE@capex':>11}{'OE@D&A':>11}")
last = max(yrs)
wins = []
for n in (3,4,5,6,7,8,10):
    w = [y for y in yrs if y > last-n]
    if len(w) < n: continue
    wins.append((f"{w[0]}-{w[-1]} ({n}yr)", w))
# also trailing windows ending earlier, to expose window sensitivity [E4-38]
for endy in (2023, 2024):
    w = [y for y in yrs if endy-4 <= y <= endy]
    if len(w) == 5: wins.append((f"{w[0]}-{w[-1]} (5yr)", w))
allv = []
for label, w in wins:
    mc = statistics.mean(rows[y][5] for y in w)
    md = statistics.mean(rows[y][6] for y in w)
    allv += [mc, md]
    print(f"{label:<16}{len(w):>3}{mc:>11.1f}{md:>11.1f}")
# single latest year both ends
print(f"{'2025 only':<16}{1:>3}{rows[2025][5]:>11.1f}{rows[2025][6]:>11.1f}")
allv += [rows[2025][5], rows[2025][6]]
lo, hi = min(allv), max(allv)
print(f"\nTRUE RANGE across all windows x both (c) ends: {lo:.1f} .. {hi:.1f}  = {hi/lo:.2f}x  ({(hi/lo-1)*100:.0f}%)")
print(f"Published row said 145 .. 183 = {183/145:.2f}x (26.5%)")

CAPM = 171.65 * 34595001 / 1e6
print(f"\nMARKET CAP = 171.65 x 34,595,001 = ${CAPM:,.0f}M   (screen row used 6124 -> 35.68M shares)")
print(f"{'range':<12}{'yield':>9}{'vs sov 5.24':>13}{'g needed @10% floor':>22}")
for lbl, v in (("bottom", lo), ("top", hi), ("5yr@D&A", None), ("5yr@capex", None)):
    if v is None: continue
    y = v/CAPM*100
    print(f"{lbl:<12}{y:>8.2f}%{y-5.24:>12.2f}{10-y:>21.2f}%")
w5 = [y for y in yrs if y > last-5]
m5c = statistics.mean(rows[y][5] for y in w5); m5d = statistics.mean(rows[y][6] for y in w5)
for lbl, v in (("5yr@capex", m5c), ("5yr@D&A", m5d), ("3yr@capex", statistics.mean(rows[y][5] for y in yrs if y>last-3)),
               ("3yr@D&A", statistics.mean(rows[y][6] for y in yrs if y>last-3))):
    y = v/CAPM*100
    print(f"{lbl:<12}{y:>8.2f}%{y-5.24:>12.2f}{10-y:>21.2f}%   OE={v:.1f}")

print("\n=== ROE series [E2-01] ===")
EQ = ser("StockholdersEquity")
# StockholdersEquity is instant; re-pull
node = us["StockholdersEquity"]["units"]["USD"]; eq = {}
for it in node:
    if it.get("form") not in ("10-K",) or it.get("fp") != "FY": continue
    if it.get("start"): continue
    y = int(it["end"][:4])
    if y not in eq or it.get("filed","") >= eq[y][1]: eq[y] = (it["val"]/1e6, it.get("filed"))
eq = {k: v[0] for k, v in eq.items()}
for y in sorted(NI):
    if y in eq and y-1 in eq:
        avg = (eq[y]+eq[y-1])/2
        print(f"{y}  NI {NI[y]:8.1f}  avg equity {avg:8.1f}  ROE {NI[y]/avg*100:6.1f}%  yr-end eq {eq[y]:8.1f}  OpMargin {OI[y]/REV[y]*100 if y in REV and REV.get(y) else 0:5.1f}%")

print("\n=== cash tax % of pretax [E4-30] ===")
PT = ser("IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest")
TX = ser("IncomeTaxesPaidNet")
for y in sorted(PT):
    if y in TX: print(f"{y}  pretax {PT[y]:7.1f}  cash tax {TX[y]:6.1f}  = {TX[y]/PT[y]*100:5.1f}%")
