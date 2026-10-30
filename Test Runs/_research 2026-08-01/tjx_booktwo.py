"""TJX — BOOK TWO (Gate 6). Gates 1-5 all PASS, so Gate 6 is legitimately open.

Discount rate is the AESOP CERTAINTY SPREAD per Ruling 4, NOT WACC/ERP/beta:
sovereign 5.28% + WIDE-moat spread 1.00% = 6.28%. CAPM/beta are explicitly
rejected by the framework (Munger: an "obscenity"), so no beta appears here.

Terminal value uses the GROWING-COUPON reading (1977 inflation essay [E2-22]):
the terminal stream is an equity coupon that grows, discounted at the Aesop
rate. The bare sovereign yield is NEVER used as a perpetuity input.

Year-1 growth is anchored to the LOWER of recent OE growth or guidance. Recent
annual OE growth was +26.9% (FY23->24), +9.0% (FY24->25), +18.1% (FY25->26).
The SLOWEST of those, +9.0%, is used as the base-case anchor. Company guidance
was NOT independently verified in this run and is recorded as a data limitation;
using the slowest observed year is the conservative substitute.
"""
OE = {"FY2021": 393, "FY2022": 3106, "FY2023": 2928, "FY2024": 3716,
      "FY2025": 4050, "FY2026": 4784}          # $M, from 10-K XBRL
SHARES = 1104.7            # M, cover page filed 2026-05-29
PRICE = 157.34             # 2026-07-31 close
SOV = 5.28
SPREAD_WIDE = 3.00   # Ruling 4-A (2026-08-01): floor raised to E3-13's 'at least' +3%
R = (SOV + SPREAD_WIDE) / 100          # 6.28% Aesop rate for a WIDE moat


def dcf(base_oe, g1, tgr, r, years=10):
    """Explicit forecast with growth fading linearly from g1 to tgr, then a
    growing-coupon terminal. Returns (equity value $M, terminal share of value)."""
    pv, oe = 0.0, base_oe
    for t in range(1, years + 1):
        g = g1 + (tgr - g1) * (t - 1) / (years - 1)
        oe *= (1 + g)
        pv += oe / (1 + r) ** t
    term = oe * (1 + tgr) / (r - tgr)
    pv_term = term / (1 + r) ** years
    return pv + pv_term, pv_term / (pv + pv_term)


print("=" * 78)
print("TJX — BOOK TWO (Aesop certainty spread)   discount rate = "
      f"{SOV:.2f}% sovereign + {SPREAD_WIDE:.2f}% WIDE moat = {R*100:.2f}%")
print("=" * 78)

SC = {
    # name      base OE     g1     tgr   rationale
    "BEAR":  (OE["FY2023"], 0.03, 0.020),
    "BASE":  (OE["FY2025"], 0.09, 0.025),
    "BULL":  (OE["FY2026"], 0.12, 0.030),
}
RAT = {"BEAR": "lowest ex-COVID tier, growth near inflation only",
       "BASE": "FY2025 tier (one year back, conservative), slowest observed OE growth",
       "BULL": "latest tier, growth near the 3-yr trend"}
ivs = {}
print(f"{'':6s} {'base OE$M':>10s} {'g1':>6s} {'TGR':>6s} {'equity $B':>11s} "
      f"{'IV/share':>10s} {'term %':>8s}   rationale")
for k, (b, g1, tgr) in SC.items():
    ev, tshare = dcf(b, g1, tgr, R)
    iv = ev / SHARES
    ivs[k] = iv
    print(f"{k:6s} {b:>10,.0f} {g1*100:>5.0f}% {tgr*100:>5.1f}% {ev/1000:>11,.1f} "
          f"{iv:>10,.2f} {tshare*100:>7.0f}%   {RAT[k]}")

base_iv = ivs["BASE"]
max_buy = base_iv * 0.80
print(f"\nBase IV/share      ${base_iv:,.2f}")
print(f"MAX BUY = Base IV x 0.80 (WIDE moat, 20% MOS)   ${max_buy:,.2f}")
print(f"Price 2026-07-31   ${PRICE:,.2f}   -> "
      f"{'BELOW max buy' if PRICE <= max_buy else 'ABOVE max buy by %.0f%%' % ((PRICE/max_buy-1)*100)}")

print("\nSENSITIVITY GRID — IV/share (base case OE and g1, varying r and TGR)")
b, g1, _ = SC["BASE"]
hdr = "r / TGR"
print(f"{hdr:>10s}" + "".join(f"{t*100:>10.1f}%" for t in (0.020, 0.025, 0.030)))
holds = []
for rr in (0.0528, 0.0628, 0.0728, 0.0828):
    row = f"{rr*100:>9.2f}%"
    for tgr in (0.020, 0.025, 0.030):
        iv = dcf(b, g1, tgr, rr)[0] / SHARES
        holds.append((rr, tgr, iv, PRICE <= iv * 0.80))
        row += f"{iv:>11,.0f}"
    print(row)
n_ok = sum(1 for *_, ok in holds if ok)
print(f"\nCells where price <= IV x 0.80: {n_ok}/{len(holds)}  -> majority holds? "
      f"{'YES' if n_ok > len(holds)/2 else 'NO'}")

print("\nSCREAM TEST")
y_yield = OE["FY2026"] / (PRICE * SHARES) * 100
print(f"  Yardstick (Book One, bare sovereign 5.28%): most-recent-tier yield "
      f"{y_yield:.2f}% vs 5.28% -> FAIL")
print(f"  Build-up  (Book Two, Aesop {R*100:.2f}%): price ${PRICE:,.2f} vs max buy "
      f"${max_buy:,.2f} -> {'PASS' if PRICE <= max_buy else 'FAIL'}")
agree = (PRICE <= max_buy) == (y_yield >= 5.28)
print(f"  -> {'AGREE' if agree else 'WHISPER — pass (books disagree)'}")
