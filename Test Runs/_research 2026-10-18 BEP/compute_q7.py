# Q7 arithmetic for the BEP run of 2026-10-18. Inputs are typed from the filed statements (sources in comments);
# the script only adds, divides and discounts. Run: python compute_q7.py
YEARS = [2021, 2022, 2023, 2024, 2025]
# Consolidated statements of cash flows: 2021-2022 from 20-F FY2023 (0001533232-24-000005), 2023-2025 from FY2025 (0001533232-26-000011)
CFO = [734, 1711, 1865, 1274, 1147]
PPE = [1967, 2190, 2809, 3733, 6587]          # investment in property, plant and equipment
ACQ = [1426, 2452, 791, 2940, 4435]           # acquisitions, net of cash acquired
EAI = [54, 236, 725, 389, 175]                # investment in equity-accounted investments
DISP = [827, 140, 217, 1092, 2817]            # proceeds from disposal of assets, net of cash disposed
FIN_BUY = [58, 492, 644, 979, 245]            # purchase of financial assets
FIN_SELL = [220, 70, 431, 183, 346]           # proceeds from financial assets
NCI_IN = [1200, 1863, 2593, 2343, 3125]       # capital contributions from participating NCI in operating subsidiaries
NCI_REPAID = [511, 75, 248, 317, 1397]        # capital repaid to participating NCI
NCI_DIST = [900, 1372, 967, 993, 2933]        # distributions to participating NCI, preferred shareholders, preferred LPs, perpetual notes
# Note 7 (segmented information), interest attributable to Unitholders (proportionate): FY2023 note for 2021-2022, FY2025 note for 2023-2025
INT_ATTR = [539, 596, 745, 835, 969]
# Note 7, FFO and the "other income" inside it; FY2022 note gives Unitholders' depreciation for 2021 and 2022 only
FFO = [934, 1005, 1095, 1217, 1334]
FFO_OTHER = [301, 292, 412, 669, 852]
DEP_ATTR = {2021: 922, 2022: 934}

R_GOV = 0.0543          # US Treasury 30-year par yield, 2026-10-16
R_FLOOR = 0.10          # Q7 floor CONVENTION, about ten percent
UNITS = 684.176085      # millions: fully-exchanged units 680,198,825 + GP interest 3,977,260 (Q2 2026 6-K)
PRICE = 28.40
# Proportionate debt at 2026-06-30 (Q2 2026 6-K, Borrowings table): 17,881; less BEP's share of cash 871 and marketable securities 176
NET_DEBT = 17881 - 871 - 176


def avg(x):
    return sum(x) / len(x)


def zip5(*cols):
    return list(zip(*cols))


group_pre_debt = [c - p - a - e + d - fb + fs for c, p, a, e, d, fb, fs in zip5(CFO, PPE, ACQ, EAI, DISP, FIN_BUY, FIN_SELL)]
unit_all = [g + ni - nr - nd for g, ni, nr, nd in zip5(group_pre_debt, NCI_IN, NCI_REPAID, NCI_DIST)]
net_purchases = [a + e - d for a, e, d in zip5(ACQ, EAI, DISP)]
unit_organic = [u + n for u, n in zip5(unit_all, net_purchases)]
ffo_ex = [f - o for f, o in zip5(FFO, FFO_OTHER)]

print("year   group_pre_debt  unit_all_spend  net_purchases  unit_organic  FFO_ex_other  attr_interest")
for i, y in enumerate(YEARS):
    print(f"{y}  {group_pre_debt[i]:>14,} {unit_all[i]:>15,} {net_purchases[i]:>14,} {unit_organic[i]:>13,} {ffo_ex[i]:>13,} {INT_ATTR[i]:>14,}")
for name, s in (("group_pre_debt", group_pre_debt), ("unit_all_spend", unit_all), ("unit_organic", unit_organic),
                ("FFO_ex_other", ffo_ex), ("attr_interest", INT_ATTR)):
    print(f"5-yr average {name}: {avg(s):,.0f}")
print("depreciation variant (FFO without other income less Unitholders' depreciation):",
      {y: ffo_ex[YEARS.index(y)] - d for y, d in DEP_ATTR.items()})
print("serial-acquirer test: net purchases", f"{sum(net_purchases):,}", "vs half of owner cash before purchases",
      f"{sum(unit_organic) / 2:,.0f}")


def no_growth_value(cash, r):
    return cash / r


for label, series in (("CENTRAL organic pair", unit_organic), ("BESIDE default pair (purchases deducted)", unit_all)):
    eq = avg(series)
    alleq = eq + avg(INT_ATTR)
    v_eq = no_growth_value(eq, R_GOV) / UNITS
    v_all = (no_growth_value(alleq, R_GOV) - NET_DEBT) / UNITS
    f_eq = no_growth_value(eq, R_FLOOR) / UNITS
    f_all = (no_growth_value(alleq, R_FLOOR) - NET_DEBT) / UNITS
    print(f"\n{label}: owner cash equity-only {eq:,.0f}; before interest {alleq:,.0f}")
    print(f"  no-growth value at {R_GOV:.2%}: all-equity {v_all:,.2f} per unit; equity-only {v_eq:,.2f} per unit")
    print(f"  fair price at {R_FLOOR:.0%}: all-equity {f_all:,.2f}; equity-only {f_eq:,.2f}")
    print(f"  expected return at ${PRICE}: all-equity {(alleq) / (PRICE * UNITS + NET_DEBT):.2%}; equity-only {eq / (PRICE * UNITS):.2%}")

# Strongest case for the business, shown in yields only (not a reporting figure): the filer's own FFO, gains included,
# with no capital spending charged at all, against the market value of the units.
print(f"\nFFO 2025 incl. gains / market cap: {FFO[-1] / (PRICE * UNITS):.2%}; FFO without gains / market cap: {ffo_ex[-1] / (PRICE * UNITS):.2%}")
print(f"market cap {PRICE * UNITS:,.0f}; net debt (proportionate) {NET_DEBT:,}")
