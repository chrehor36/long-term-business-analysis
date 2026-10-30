"""MSFT run 2026-10-06: arithmetic only, from filed figures (USD millions). No verdict here.

Sources: cash-flow and income lines FY2016-FY2026 from SEC companyfacts (10-K vintages; FY2022 from
0001564590-22-026876), FY2024-FY2026 checked against the FY2026 10-K filed statements
(0001193125-26-323660). Finance-lease ROU assets obtained, leases not yet commenced, contractual
obligations: FY2026 10-K Note 13 and MD&A; FY2025 10-K (0000950170-25-100235) Note 13; Q3 FY2026 10-Q
(0001193125-26-191507) Note on leases.
"""
FY = list(range(2016, 2027))
capex = dict(zip(FY, [8343, 8129, 11632, 13925, 15441, 20622, 23886, 28107, 44477, 64551, 115948]))
rev = dict(zip(FY, [91154, 96571, 110360, 125843, 143015, 168088, 198270, 211915, 245122, 281724, 331839]))
ocf = dict(zip(FY, [33325, 39507, 43884, 52185, 60675, 76740, 89035, 87582, 118548, 136162, 182935]))
sbc = dict(zip(FY, [2668, 3266, 3940, 4652, 5289, 6118, 7502, 9611, 10734, 11974, 12405]))
# finance-lease right-of-use assets obtained in exchange for lease obligations (non-cash capital put in)
fl_rou = {2023: 3128, 2024: 11633, 2025: 20511, 2026: 24608}
# "Other, net" investing, FY2026 10-K: "primarily to facilitate the purchase of components" (FY2026 only read)
other_inv_2026 = 19861
deferred_tax = {2024: -4738, 2025: -7056, 2026: 14189}

print("FY   revenue   OCF    SBC   capex  capex/rev  owner cash (OCF-SBC-capex)  OC/rev")
for y in FY:
    oc = ocf[y] - sbc[y] - capex[y]
    print(f"{y} {rev[y]:8,} {ocf[y]:7,} {sbc[y]:6,} {capex[y]:7,}  {capex[y]/rev[y]:6.1%}   {oc:9,}            {oc/rev[y]:6.1%}")

print("\nCapital put in, cash capex plus finance-lease ROU obtained:")
for y in (2023, 2024, 2025, 2026):
    tot = capex[y] + fl_rou[y]
    print(f"{y}: {capex[y]:,} + {fl_rou[y]:,} = {tot:,}  = {tot/rev[y]:.1%} of revenue;"
          f"  owner cash after it {ocf[y]-sbc[y]-tot:,}")
y = 2026
print(f"FY2026 also less 'Other, net' investing (components) {other_inv_2026:,}: "
      f"{ocf[y]-sbc[y]-capex[y]-fl_rou[y]-other_inv_2026:,}")
print(f"FY2026 OCF less the deferred-tax add-back ({deferred_tax[2026]:,}): {ocf[2026]-deferred_tax[2026]:,}")

print("\nLeases not yet commenced (USD bn): 2025-06-30 92.7; 2026-03-31 196.6; 2026-06-30 329.1")
print("Contractual obligations 2026-06-30 (bn): debt principal 46.1, interest 25.6, construction 34.6,"
      " leases incl. interest 443.5, purchase commitments 194.1, total 743.8")

# five-year mean owner cash, capex basis (FY2022-FY2026)
five = [ocf[y] - sbc[y] - capex[y] for y in range(2022, 2027)]
print(f"\nFive-year mean owner cash FY2022-26 (capex basis): {sum(five)/5:,.0f}")
mcap = 525.18 * 7425.545491  # price (aggregator, 2026-10-05) x cover shares (millions)
print(f"Market cap at $525.18 x 7,425.545M shares: {mcap:,.0f}M")
print(f"Owner-cash yield, five-year mean: {sum(five)/5/mcap:.2%};  FY2026: {five[-1]/mcap:.2%};"
      f"  FY2026 after finance leases: {(five[-1]-fl_rou[2026])/mcap:.2%}  vs Treasury 30y 5.66%")
