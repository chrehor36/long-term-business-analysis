"""Owner cash of Honeywell Technologies (HON after the Aerospace spin of 2026-06-29), reconstructed two ways from filed
documents, and the Q7 arithmetic. USD millions. Every input is typed from a filing named beside it; nothing is fetched.
Usage: python -I owner_cash.py

Sources
  K25  HON 10-K FY2025, 0000773840-26-013 (cash-flow statement p.57-58; Note 22 segment data)
  F10  Honeywell Aerospace Form 10 amendment 2, Ex. 99.1, 0001628280-26-041399 (audited combined statements)
  PF   HON 8-K 2026-06-29, 0000773840-26-000084, Ex. 99.3 (pro forma statements of operations, continuing = HT)
"""

YEARS = [2023, 2024, 2025]

# K25 cash-flow statement, continuing operations (Solstice already discontinued; Aerospace still inside)
hon_cont_ocf = {2023: 4459, 2024: 5112, 2025: 6075}
hon_capex = {2023: 741, 2024: 871, 2025: 986}
hon_sbc = {2023: 197, 2024: 189, 2025: 196}
hon_dep = {2023: 490, 2024: 493, 2025: 546}
hon_amort = {2023: 514, 2024: 659, 2025: 842}
# one-off legacy-liability cash items inside continuing OCF (K25)
narco = {2023: -1325, 2024: 0, 2025: 0}          # NARCO buyout payment
resideo = {2023: 0, 2024: 0, 2025: 1590}         # Resideo termination payment received
asbestos = {2023: 0, 2024: 0, 2025: -1428}       # asbestos liabilities divestiture payment

# F10 combined statements of cash flows, Aerospace
aero_ocf = {2023: 2984, 2024: 2538, 2025: 3705}
aero_capex = {2023: 387, 2024: 488, 2025: 504}
aero_sbc = {2023: 73, 2024: 74, 2025: 83}
aero_dep = {2023: 226, 2024: 246, 2025: 275}
aero_amort = {2023: 76, 2024: 100, 2025: 137}

# PF pro forma continuing operations (HT), net income attributable, and items read from K25 / Ex. 99.2
pf_ni = {2023: 1236, 2024: 1302, 2025: 1368}
pf_interest = {2023: 582, 2024: 797, 2025: 788}
hon_interest_cont = {2023: 749, 2024: 1048, 2025: 1344}   # K25 statement of operations (Aerospace inside)
impair = {2023: 0, 2024: 219 + 48, 2025: 724 + 270 + 44}   # Ex. 99.2 reconciliation: held-for-sale, indefinite-lived, goodwill
resideo_gain_after_tax = {2023: 0, 2024: 0, 2025: 784}    # K25: $1.22 a share after tax x 642.8M diluted shares
pension_income = {2023: 408, 2024: 477, 2025: 396}         # K25 cash-flow line "Pension and other postretirement income"
TAX = 0.21   # CONVENTION: US statutory rate, used only to put pension income and interest on an after-tax footing

print("METHOD A: cash by difference (HON continuing OCF less Aerospace's audited carve-out OCF)")
print(" year   HT OCF  HT SBC  HT capex  owner cash  one-offs  ex one-offs  +interest normalised")
a_filed, a_ex, a_int = {}, {}, {}
for y in YEARS:
    ocf = hon_cont_ocf[y] - aero_ocf[y]
    sbc = hon_sbc[y] - aero_sbc[y]
    capex = hon_capex[y] - aero_capex[y]
    oc = ocf - sbc - capex
    one = narco[y] + resideo[y] + asbestos[y]
    ex = oc - one
    intadj = (hon_interest_cont[y] - pf_interest[y]) * (1 - TAX)
    a_filed[y], a_ex[y], a_int[y] = oc, ex, ex + intadj
    print(f" {y}  {ocf:7,.0f} {sbc:7,.0f} {capex:9,.0f} {oc:11,.0f} {one:9,.0f} {ex:12,.0f} {ex+intadj:12,.0f}")

print("\nMETHOD B: owner earnings built from the pro forma income account (a + b - c), not a proxy")
print(" year  PF NI    D&A   capex  impairments  Resideo gain  pension inc. a/t  owner cash")
b = {}
for y in YEARS:
    da = (hon_dep[y] + hon_amort[y]) - (aero_dep[y] + aero_amort[y])
    capex = hon_capex[y] - aero_capex[y]
    pen = pension_income[y] * (1 - TAX)
    oc = pf_ni[y] + da - capex + impair[y] - resideo_gain_after_tax[y] - pen
    b[y] = oc
    print(f" {y} {pf_ni[y]:6,.0f} {da:6,.0f} {capex:6,.0f} {impair[y]:11,.0f} {resideo_gain_after_tax[y]:13,.0f} {pen:16,.0f} {oc:11,.0f}")

mean = lambda d: sum(d.values()) / len(d)
bases = {"A as filed": mean(a_filed), "A ex one-offs": mean(a_ex), "A ex one-offs, interest normalised": mean(a_int),
         "B": mean(b)}
print("\nThree-year means:")
for k, v in bases.items():
    print(f"  {k:38s} {v:7,.0f}")

# ---- Q7 ----
PRICE, SHARES, RF = 214.14, 316.94, 0.0566
QNT = 7260   # carrying value of the 48% Quantinuum stake at 2026-06-30 (10-Q Q2 2026, Note 2), shown separately
cap = PRICE * SHARES
print(f"\nmarket cap {cap:,.0f}M at ${PRICE} x {SHARES}M shares; sovereign {RF:.2%}")


def value(base, g, r, years=10):
    """ten years at g, then zero nominal growth, discounted at r (CONVENTION, framework Q7)"""
    v, c = 0.0, base
    for t in range(1, years + 1):
        c *= (1 + g)
        v += c / (1 + r) ** t
    return v + (c / r) / (1 + r) ** years


def irr(base, g, price_total):
    lo, hi = 0.0001, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        if value(base, g, mid) > price_total:
            lo = mid
        else:
            hi = mid
    return mid


SALES = {2023: 19407, 2024: 19281, 2025: 19945}   # PF net sales, continuing (HT)
g_sales = (SALES[2025] / SALES[2023]) ** 0.5 - 1
g_b = (b[2025] / b[2023]) ** 0.5 - 1
print(f"growth shown: HT net sales 2023-2025 {g_sales:.2%} a year; method-B owner cash 2023-2025 {g_b:.2%} a year")

lo_base, hi_base = bases["B"], bases["A ex one-offs, interest normalised"]
print("\n case                                  base   growth   value@sov  /share   +QNT/share   value@10%  /share")
for name, base, g in [("no growth, low base (B)", lo_base, 0.0),
                      ("no growth, high base (A norm.)", hi_base, 0.0),
                      ("sales growth shown, high base", hi_base, g_sales),
                      ("B growth shown (uncapped), low base", lo_base, g_b)]:
    v = value(base, g, RF); v10 = value(base, g, 0.10)
    print(f" {name:36s} {base:6,.0f} {g:7.2%} {v:11,.0f} {v/SHARES:7.0f} {(v+QNT)/SHARES:11.0f} {v10:11,.0f} {v10/SHARES:7.0f}")

ops_price = cap - QNT
print(f"\nprice paid for the operations if the Quantinuum stake is worth its carrying value: {ops_price:,.0f}M")
for name, base, g in [("low base, no growth", lo_base, 0.0), ("high base, no growth", hi_base, 0.0),
                      ("high base, sales growth", hi_base, g_sales), ("low base, B growth uncapped", lo_base, g_b)]:
    print(f"  expected return at the price ({name}): whole cap {irr(base, g, cap):.2%}; ex-QNT {irr(base, g, ops_price):.2%}")

# fair and cheap prices at the ~10% floor (CONVENTION)
central = (lo_base + hi_base) / 2
print(f"\ncentral base (mean of the two methods) {central:,.0f}M")
print(f"fair price (central base, sales growth shown, at 10%): ${value(central, g_sales, 0.10)/SHARES:.0f}"
      f" (+QNT carrying value: ${(value(central, g_sales, 0.10)+QNT)/SHARES:.0f})")
print(f"cheap price (low base, no growth, at 10%): ${value(lo_base, 0.0, 0.10)/SHARES:.0f}")
