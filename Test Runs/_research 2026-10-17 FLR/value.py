"""COMPUTATION, NOT A CLEARANCE. Q7 range and fair price for FLR (USD millions, per share in USD)."""
import sys; sys.stdout.reconfigure(encoding="utf-8")
R_SOV = 0.0543            # US Treasury 30-year par yield, 2026-10-16
SH = 135.564463           # shares issued and outstanding 2026-06-30 (10-Q 0001124198-26-000071), the date of net cash
SH_COVER = 133.741067     # cover count 2026-07-31
PRICE = 46.95             # close 2026-10-16, aggregator (live quote only)
CASH, SEC, DEBT = 2923.0, 120.0, 1072.0   # 10-Q balance sheet 2026-06-30
MEX = 175.0 - 33.0        # July 2026 sale of Mexico JV, tax funded August 2026 (stated in the 10-Q)
VIE_CASH = 320.0 + 26.0   # cash and securities related to consolidated VIEs, not available for general purposes
NET_CASH = CASH + SEC - DEBT + MEX
def pv(oc, g, r, years=10):
    v, c = 0.0, oc
    for t in range(1, years + 1):
        c = c * (1 + g); v += c / (1 + r) ** t
    return v + (c / r) / (1 + r) ** years   # zero nominal growth after year ten
def ps(v, net=NET_CASH, sh=SH): return (v + net) / sh
EV = PRICE * SH - NET_CASH
print(f"net cash {NET_CASH:.0f}  (excluding VIE cash {NET_CASH - VIE_CASH:.0f});  market value {PRICE*SH:.0f};  EV {EV:.0f}")
G_SALES = (15503.0 / 19036.5) ** (1 / 9) - 1
print(f"sales growth 2016-2025: {100*G_SALES:.2f}% a year")
for name, oc in [("central: ten-year base 2016-2025, core, all-equity", 61.3), ("beside: cycle 2017-2024", 97.9), ("beside: window 2021-2025 with Santos added back", 132.0), ("beside: literal window 2021-2025, core, all-equity", 3.6)]:
    v0 = pv(oc, 0.0, R_SOV); vd = pv(oc, G_SALES, R_SOV)
    f0 = pv(oc, 0.0, 0.10); fd = pv(oc, G_SALES, 0.10)
    print(f"{name}: OC {oc:.1f} | yield on EV {100*oc/EV:.2f}% | no-growth value {ps(v0):.2f}/sh, decline-at-sales {ps(vd):.2f}/sh | at 10%: no-growth {ps(f0):.2f}, decline {ps(fd):.2f}, average {ps((f0+fd)/2):.2f}")
# equity-only: owner cash after interest (core) against market value; no net cash added (its interest is inside the cash figure)
for name, oc in [("equity-only ten-year", 73.6), ("equity-only window", 58.5)]:
    print(f"{name}: OC {oc:.1f} | yield on market value {100*oc/(PRICE*SH):.2f}% | fair at 10% no-growth {pv(oc,0,0.10)/SH:.2f}/sh, decline {pv(oc,G_SALES,0.10)/SH:.2f}/sh")
print(f"owner cash needed to earn 10% on EV at no growth: {0.10*EV:.0f}; to reach the price at the sovereign: {R_SOV*EV:.0f}")
print(f"net cash per share {NET_CASH/SH:.2f}; at cover count {NET_CASH/SH_COVER:.2f}")
