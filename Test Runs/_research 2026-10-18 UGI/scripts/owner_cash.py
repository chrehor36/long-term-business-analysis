"""UGI owner cash, capital returns, and the Q7 range. All inputs transcribed from the filed statements
(FY2021-22 from 10-K 0000884614-22-000061; FY2023-25 from 10-K 0000884614-25-000053; balance sheet 10-Q 0000884614-26-000052).
$ millions. Arithmetic only."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
Y = [2021, 2022, 2023, 2024, 2025]
OCF   = [1481, 716, 1107, 1182, 1227]
SBC   = [21, 15, 17, 8, 18]
CAPEX = [690, 804, 974, 796, 837]
ACQ   = [397, 242, 9, 0, 0]
EQINV = [65, 47, 146, 92, 38]
DISP  = [0, 0, 30, 93, 170]      # net proceeds from disposition of businesses and assets (FY2021-22 'Other, net' 39 and 55 left out: not described)
DA    = [502, 518, 532, 551, 561]
INTP  = [297, 320, 332, 403, 375]  # cash interest paid
TAXP  = [96, 61, -17, 80, 55]
REV   = [7447, 10106, 8928, 7210, 7287]
SEG_EBIT = [1134, 1166, 1158, 1178, 1176]
ASSETS = [16723, 17575, 15401, 15098, 15462]
GW     = [3770, 3612, 3027, 2871, 2852]
INTANG = [583, 500, 443, 391, 328]
T = 0.21  # CONVENTION of the run: interest added back at the 21% US federal statutory rate (see run file)
avg = lambda a: sum(a) / len(a)
oc_eq_all = [o - s - c - a - e + d for o, s, c, a, e, d in zip(OCF, SBC, CAPEX, ACQ, EQINV, DISP)]
oc_eq_capex_only = [o - s - c for o, s, c in zip(OCF, SBC, CAPEX)]  # before purchases
oc_eq_da = [o - s - d for o, s, d in zip(OCF, SBC, DA)]
aft_int = [i * (1 - T) for i in INTP]
add = lambda a, b: [x + y for x, y in zip(a, b)]
oc_all_all = add(oc_eq_all, aft_int)
oc_all_capex = add(oc_eq_capex_only, aft_int)
oc_all_da = add(oc_eq_da, aft_int)
def show(name, s): print(f"{name:52s}", " ".join(f"{v:7.0f}" for v in s), f"| avg {avg(s):7.1f}")
print("FY", Y)
show("Owner cash, equity-only, all spending incl. net purchases", oc_eq_all)
show("Owner cash, equity-only, capex only (before purchases)", oc_eq_capex_only)
show("Owner cash, equity-only, depreciation variant", oc_eq_da)
show("After-tax interest added back", aft_int)
show("Owner cash, ALL-EQUITY, all spending incl. purchases", oc_all_all)
show("Owner cash, ALL-EQUITY, capex only", oc_all_capex)
show("Owner cash, ALL-EQUITY, depreciation variant", oc_all_da)
netp = [a + e - d for a, e, d in zip(ACQ, EQINV, DISP)]
print("net purchases", netp, sum(netp), "vs half of owner cash before purchases", sum(oc_eq_capex_only) / 2)
print("Revenue CAGR FY21-25", (REV[-1] / REV[0]) ** 0.25 - 1)
print("Segment EBIT CAGR FY21-25", (SEG_EBIT[-1] / SEG_EBIT[0]) ** 0.25 - 1)
tang = [a - g - i for a, g, i in zip(ASSETS, GW, INTANG)]
print("Seg EBIT / tangible assets", [f"{e/t:.1%}" for e, t in zip(SEG_EBIT, tang)])
print("Seg EBIT / total assets", [f"{e/t:.1%}" for e, t in zip(SEG_EBIT, ASSETS)])
added = sum(CAPEX) + sum(ACQ) + sum(EQINV) - sum(DISP) - sum(DA)
print("Capital added net of depreciation FY21-25", added, "EBIT change", SEG_EBIT[-1] - SEG_EBIT[0], f"{(SEG_EBIT[-1]-SEG_EBIT[0])/added:.1%}")
# halves for growth where series changes sign
h1 = avg(oc_all_all[:2]); h2 = avg(oc_all_all[3:])
print("halves all-equity all-spending", h1, h2)
# ---- Q7 valuation
PRICE = 38.43; SH = 214.494967; MCAP = PRICE * SH
DEBT = 18 + 336 + 6695; CASH = 476
NETDEBT = DEBT - CASH
EV = MCAP + NETDEBT
R = 0.0543
def pv(cash0, g, r, years=10):
    """cash0 = base annual owner cash; grows at g for 10 years, then flat (zero nominal growth) forever."""
    v = 0; c = cash0
    for t in range(1, years + 1):
        c = c * (1 + g); v += c / (1 + r) ** t
    v += (c / r) / (1 + r) ** years
    return v
def irr(cash0, g, price):
    lo, hi = 0.0005, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if pv(cash0, g, mid) > price: lo = mid
        else: hi = mid
    return mid
print(f"\nMCAP {MCAP:.0f}  DEBT {DEBT}  CASH {CASH}  NETDEBT {NETDEBT}  EV {EV:.0f}")
cases = {
  "A all spending incl purchases, all-equity, g=0": (avg(oc_all_all), 0.0),
  "B capex only (purchases stop), all-equity, g=0": (avg(oc_all_capex), 0.0),
  "C maintenance-central (see run), all-equity, g=0": (None, 0.0),
  "D depreciation variant, all-equity, g=0": (avg(oc_all_da), 0.0),
}
MAINT = float(sys.argv[1]) if len(sys.argv) > 1 else None
if MAINT:
    capex_avg = avg(CAPEX)
    c_maint = avg(OCF) - avg(SBC) - MAINT + avg(aft_int)
    cases["C maintenance-central (see run), all-equity, g=0"] = (c_maint, 0.0)
GROWTH = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
for k, (c, g) in list(cases.items()):
    if c is None: continue
    for gg in sorted(set([0.0, GROWTH])):
        v = pv(c, gg, R); vf = pv(c, gg, 0.10)
        print(f"{k:52s} g={gg:5.1%} cash {c:7.1f}  value@5.43% {v:8.0f} -> per share {(v-NETDEBT)/SH:7.2f} | value@10% {vf:7.0f} -> per share {(vf-NETDEBT)/SH:7.2f} | IRR at EV {irr(c, gg, EV):6.2%}")
# equity-only
eq_cases = {"A' all spending, equity-only": avg(oc_eq_all), "B' capex only, equity-only": avg(oc_eq_capex_only), "D' depreciation variant, equity-only": avg(oc_eq_da)}
if MAINT: eq_cases["C' maintenance-central, equity-only"] = avg(OCF) - avg(SBC) - MAINT
for k, c in eq_cases.items():
    for gg in sorted(set([0.0, GROWTH])):
        v = pv(c, gg, R); vf = pv(c, gg, 0.10)
        print(f"{k:52s} g={gg:5.1%} cash {c:7.1f}  value@5.43% per share {v/SH:7.2f} | value@10% per share {vf/SH:7.2f} | IRR at mcap {irr(c, gg, MCAP):6.2%}")
