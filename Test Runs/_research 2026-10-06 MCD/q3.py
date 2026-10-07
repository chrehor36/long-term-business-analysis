"""Q3 arithmetic: pre-tax operating income on net tangible operating capital, 2021 and 2025, and the increment.
Balance-sheet lines from companyfacts (10-K, latest filed for each year-end); 2025 lines checked against the filed
balance sheet in 10-K 0000063908-26-000035. Usage: python q3.py <companyfacts.json>"""
import json, sys
g = json.load(open(sys.argv[1]))['facts']['us-gaap']
def inst(tag, y):
    best = None
    for unit, rows in g.get(tag, {}).get('units', {}).items():
        for r in rows:
            if r.get('form') == '10-K' and r['end'] == f'{y}-12-31':
                if best is None or r['filed'] > best[1]:
                    best = (r['val'] / 1e6, r['filed'])
    return best[0] if best else None
OPINC = {2021: 10356, 2022: 9371, 2023: 11647, 2024: 11712, 2025: 12393}   # filed income statements
# 10-K FY2023 (0000063908-24-000072) and FY2025 (0000063908-26-000035) balance sheets: lease ROU asset, current lease liability
FILED_LEASE = {2023: (13514.4, 688.1), 2024: (13339, 636), 2025: (14606, 694)}
rows = {}
for y in (2021, 2022, 2023, 2024, 2025):
    a = inst('Assets', y); gw = inst('Goodwill', y); c = inst('CashAndCashEquivalentsAtCarryingValue', y)
    cl = inst('LiabilitiesCurrent', y); ll = inst('OperatingLeaseLiabilityCurrent', y) or 0.0
    rou = inst('OperatingLeaseRightOfUseAsset', y) or 0.0
    if y in FILED_LEASE:   # tags absent; the filed balance sheets (total of operating and finance) are used
        rou, ll = FILED_LEASE[y]
    cl -= inst('DebtCurrent', y) or 0.0   # interest-bearing, not operating
    ppe = inst('PropertyPlantAndEquipmentNet', y)
    nta = a - gw - c - (cl - ll)
    rows[y] = (a, gw, c, cl, ll, rou, ppe, nta)
    print(y, f'assets {a:,.0f} goodwill {gw:,.0f} cash {c:,.0f} cur.liab {cl:,.0f} cur.lease {ll:,.0f} '
             f'opROU {rou:,.0f} netPPE {ppe:,.0f} -> NTA {nta:,.0f}; NTA ex opROU {nta - rou:,.0f}; '
             f'op.income {OPINC[y]:,} = {OPINC[y] / nta:.1%} on NTA, {OPINC[y] / (nta - rou):.1%} ex ROU')
d_oi = OPINC[2025] - OPINC[2021]
d_nta = rows[2025][7] - rows[2021][7]
d_ppe = rows[2025][6] - rows[2021][6]
print(f'increment 2021->2025: op.income +{d_oi:,}; NTA +{d_nta:,.0f} -> {d_oi / d_nta:.1%}; net PPE +{d_ppe:,.0f} -> {d_oi / d_ppe:.1%}')
