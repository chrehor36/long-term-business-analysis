"""Q7 range for UGI under v5's range convention. Inputs from owner_cash.py (filed statements). $ millions. Arithmetic only."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
avg = lambda a: sum(a) / len(a)
OCF   = [1481, 716, 1107, 1182, 1227]
SBC   = [21, 15, 17, 8, 18]
CAPEX = [690, 804, 974, 796, 837]
ACQ   = [397, 242, 9, 0, 0]; EQINV = [65, 47, 146, 92, 38]; DISP = [0, 0, 30, 93, 170]
DA    = [502, 518, 532, 551, 561]
INTP  = [297, 320, 332, 403, 375]
T = 0.21
AFT_INT = avg([i * (1 - T) for i in INTP])
NETPUR = avg([a + e - d for a, e, d in zip(ACQ, EQINV, DISP)])
MAINT_SHARE = 684 / 844           # Q3's maintenance guess on FY2025 segment capex
MAINT = avg(CAPEX) * MAINT_SHARE
ITC_DRAG = 0.0  # resumed session: FY2024-25 investment tax credits went mostly unused (deferred tax asset 26 -> 116, 10-K tax note), so cash taxes in the window were not sheltered by them; no drag. The killed draft charged (88 + 23) / 5 = 22.2; shown beside at the end
ITC_PV = 116                      # deferred ITC asset at 2025-09-30, added as the shelter's value (used within a few years; not discounted further)
PRICE = 38.43; SH = 214.494967; MCAP = PRICE * SH
NETDEBT = (18 + 336 + 6695) - 476
EV = MCAP + NETDEBT
R = 0.0543; FLOOR = 0.10
G_SALES = (7287 / 7447) ** 0.25 - 1
def pv(c0, g, r, purch=0.0, years=10, after=None):
    """c0: owner cash after purchases; grows (or declines) at g for 10 years; after year 10 flat, purchases stop (purch added back)."""
    v = 0; c = c0
    for t in range(1, years + 1):
        c *= (1 + g); v += c / (1 + r) ** t
    tail = (c + purch) if after is None else after
    v += (tail / r) / (1 + r) ** years
    return v
def irr(c0, g, price, purch=0.0):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(c0, g, mid, purch) > price: lo = mid
        else: hi = mid
    return mid
base_all = avg(OCF) - avg(SBC) - avg(CAPEX) - NETPUR + AFT_INT - ITC_DRAG
base_maint = avg(OCF) - avg(SBC) - MAINT + AFT_INT - ITC_DRAG
base_da = avg(OCF) - avg(SBC) - avg(DA) + AFT_INT - ITC_DRAG
eq_all = base_all - AFT_INT; eq_maint = base_maint - AFT_INT; eq_da = base_da - AFT_INT
print(f"after-tax interest avg {AFT_INT:.1f}; net purchases avg {NETPUR:.1f}; maintenance {MAINT:.1f} of capex {avg(CAPEX):.1f}; ITC drag {ITC_DRAG:.1f}")
print(f"sales growth FY2021-25 {G_SALES:.2%}; net debt {NETDEBT}; mcap {MCAP:.0f}; EV {EV:.0f}")
rows = [
 ("TOP: maintenance-only, no growth (all-equity)", base_maint, 0.0, 0.0, "all"),
 ("BOTTOM: all spending incl. purchases, sales growth carried, purchases stop after yr 10 (all-equity)", base_all, G_SALES, NETPUR, "all"),
 ("beside: all spending incl. purchases, no growth, purchases stop after yr 10 (all-equity)", base_all, 0.0, NETPUR, "all"),
 ("beside: depreciation variant, no growth (all-equity)", base_da, 0.0, 0.0, "all"),
 ("TOP equity-only: maintenance-only, no growth", eq_maint, 0.0, 0.0, "eq"),
 ("BOTTOM equity-only: all spending, sales growth, purchases stop after yr 10", eq_all, G_SALES, NETPUR, "eq"),
 ("beside equity-only: depreciation variant, no growth", eq_da, 0.0, 0.0, "eq"),
]
res = {}
for name, c, g, p, basis in rows:
    v = pv(c, g, R, p) + ITC_PV; vf = pv(c, g, FLOOR, p) + ITC_PV
    if basis == "all":
        ps, psf = (v - NETDEBT) / SH, (vf - NETDEBT) / SH; ret = irr(c, g, EV - ITC_PV, p)
    else:
        ps, psf = v / SH, vf / SH; ret = irr(c, g, MCAP - ITC_PV, p)
    res[name] = (ps, psf)
    print(f"{name}\n   base cash {c:7.1f}  g {g:6.2%}  value/share @5.43% {ps:7.2f}   @10% {psf:7.2f}   expected return at price {ret:6.2%}")
top, bot = res[rows[0][0]], res[rows[1][0]]
print(f"\nALL-EQUITY range {bot[0]:.2f} to {top[0]:.2f}; fair (avg of ends at 10%) {(bot[1]+top[1])/2:.2f}")
topq, botq = res[rows[4][0]], res[rows[5][0]]
print(f"EQUITY-ONLY range {botq[0]:.2f} to {topq[0]:.2f}; fair {(botq[1]+topq[1])/2:.2f}")
print(f"Electric Utility sale beside: +{470/SH:.2f}/share at most if its cash were worth nothing")
# literal window, no adjustments (all spending incl purchases, no growth, purchases continue forever)
lit = avg(OCF) - avg(SBC) - avg(CAPEX) - NETPUR + AFT_INT
print(f"literal window all-equity, purchases forever, no tax convention: cash {lit:.1f} -> per share {(lit/R - NETDEBT)/SH:.2f}; yield on EV {lit/EV:.2%}")

# ---- beside cases added by the resumed session (2026-10-18)
def irr2(c0, g, price, purch=0.0, after=None):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(c0, g, mid, purch, after=after) > price: lo = mid
        else: hi = mid
    return mid
hg = (748.81 / 201.715) ** (1 / 3) - 1
print(f"\n(f) check: halves growth {hg:.1%}/yr -> year-10 owner cash {800 * (1 + hg) ** 10:,.0f} vs FY2025 sales 7,287; highest owner-cash share of sales in window {max(543/7447, 697/7210, 800/7287):.1%}")
after = base_maint * (1 + G_SALES) ** 10
for r_ in (R, FLOOR):
    v = pv(base_all, G_SALES, r_, after=after) + ITC_PV
    print(f"beside BOTTOM, growth spending stops with growth after yr 10, r={r_}: per share {(v - NETDEBT)/SH:.2f}")
print(f"   expected return at price {irr2(base_all, G_SALES, EV - ITC_PV, after=after):.2%}")
d = 22.2
for name, c, g, p_ in (("TOP with the killed draft's ITC drag", base_maint - d, 0.0, 0.0), ("BOTTOM with the killed draft's ITC drag", base_all - d, G_SALES, NETPUR)):
    print(f"{name}: per share @5.43% {(pv(c, g, R, p_) + ITC_PV - NETDEBT)/SH:.2f}  @10% {(pv(c, g, FLOOR, p_) + ITC_PV - NETDEBT)/SH:.2f}")
for name, c, g, p_ in (("TOP", base_maint, 0.0, 0.0), ("BOTTOM", base_all, G_SALES, NETPUR)):
    print(f"Electric Utility as if closed (proceeds 470 off net debt, its cash lost credited at nothing), {name}: per share @5.43% {(pv(c, g, R, p_) + ITC_PV - NETDEBT + 470)/SH:.2f}; @10% {(pv(c, g, FLOOR, p_) + ITC_PV - NETDEBT + 470)/SH:.2f}; expected return at price {irr(c, g, EV - ITC_PV - 470, p_):.2%}")
