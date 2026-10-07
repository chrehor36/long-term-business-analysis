"""TRV, Q7: the two components and the range, under the v5 Q7 CONVENTION and the sector method (A1 net of float,
A2/C1 float, A4 after tax, C6 the two ends, C7 the bracket check). COMPUTATION — NOT A CLEARANCE until Q1 to Q4 close
(they closed before this was run). All inputs are typed from the filings named beside them or from comp_out.txt.
Usage: python -I value.py
"""
R = 0.0566            # US Treasury 30-year, 2026-10-05 (tools/sources.py)
SH = 208.575022       # million shares, 10-Q cover 0000086312-26-000145
PRICE = 360.70        # close 2026-10-05, aggregator (flagged)
TAXR = 0.174          # filer's effective rate 2021-2025 (comp_out.txt), CONVENTION A4
FLOOR_PRE = 0.10      # CONVENTION, Q7 floor, about ten percent pre-tax
FLOOR_AT = FLOOR_PRE * (1 - TAXR)

# June 30, 2026 balance sheet, 10-Q 0000086312-26-000145 (USD M)
INV, CASH = 103179, 621
RES, UPR, RECOV, CEDED = 67226, 23327, 8009, 1674
PREMREC, DAC = 12382, 3713
EQUITY, DEBT = 33121, 9068
FLOAT_A2 = RES + UPR - RECOV - CEDED
FLOAT_C1 = FLOAT_A2 - PREMREC - DAC

C2_AT = 1352          # five-year mean component 2, accident-year basis, after tax (comp_out.txt)
NONUW_AT = -427       # five-year mean of the items other than underwriting, after tax (comp_out.txt)
NII_YIELD_PRE = 3959 / ((94223 + 101182) / 2)   # 2025 NII on average investments, 10-K FY2025
NII_AT_SHARE = 0.85   # CONVENTION: after-tax share of investment income (munis); stated, not filed as such


def pv(base, g, r, years=10):
    """base = this year's after-tax figure; grows at g for `years`, then flat (zero nominal growth) forever."""
    v, cf = 0.0, base
    for t in range(1, years + 1):
        cf *= (1 + g)
        v += cf / (1 + r) ** t
    v += cf / r / (1 + r) ** years
    return v


def main():
    print(f"float A2 {FLOAT_A2:,.0f}; float C1 (less premiums receivable and DAC) {FLOAT_C1:,.0f}")
    for lab, fl in (("C1 float (used)", FLOAT_C1), ("A2 float (shown)", FLOAT_A2)):
        c1 = INV + CASH - fl
        print(f"\n== component 1 net of {lab}: {INV + CASH:,.0f} - {fl:,.0f} = {c1:,.0f}")
        cases = {
            "low: underwriting at zero (C6), no growth": NONUW_AT / R,
            "middle: developed average underwriting, no growth": C2_AT / R,
            "top: developed average, 5.66% for ten years (strict cap)": pv(C2_AT, R, R),
            "rejected: 21.0% shown 2021-2025, uncapped": pv(C2_AT, 0.21, R),
        }
        for k, v2 in cases.items():
            tot = c1 + v2
            print(f"  {k:58s} C2 value {v2:9,.0f}  total {tot:9,.0f}  per share ${tot/SH:7.2f}")
        lo, hi = c1 + cases["low: underwriting at zero (C6), no growth"], c1 + cases[
            "top: developed average, 5.66% for ten years (strict cap)"]
        print(f"  range ${lo/SH:.0f} to ${hi/SH:.0f}; width {hi/lo:.2f} to 1; price ${PRICE}")
        print(f"  bracket (C7): net worth {EQUITY:,}; net worth + float A2 {EQUITY + FLOAT_A2:,}")
        # expected return at the price, and fair / cheap prices (COMPUTATION)
        inv_inc_at = c1 * NII_YIELD_PRE * NII_AT_SHARE
        own = C2_AT + inv_inc_at
        print(f"  owner earnings after tax at no growth: C2 {C2_AT} + investment income on component 1 "
              f"{inv_inc_at:,.0f} = {own:,.0f}; yield at the price {own/(PRICE*SH)*100:.2f}% after tax "
              f"({own/(PRICE*SH)/(1-TAXR)*100:.2f}% pre-tax)")
        cheap = own / FLOOR_AT / SH
        fair = (pv(C2_AT, R, FLOOR_AT) + inv_inc_at / FLOOR_AT) / SH
        print(f"  floor {FLOOR_PRE*100:.0f}% pre-tax = {FLOOR_AT*100:.2f}% after tax at {TAXR*100:.1f}%")
        print(f"  cheap price (no growth meets the floor): ${cheap:.0f}")
        print(f"  fair price (top case, 5.66% growth for ten years, meets the floor): ${fair:.0f}")
        # implied growth at the price
        lo_g, hi_g = 0.0, 0.5
        for _ in range(100):
            mid = (lo_g + hi_g) / 2
            if c1 + pv(C2_AT, mid, R) < PRICE * SH:
                lo_g = mid
            else:
                hi_g = mid
        print(f"  growth of component 2 for ten years that the price implies at {R*100:.2f}%: {lo_g*100:.1f}% a year")


if __name__ == "__main__":
    main()
