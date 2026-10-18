# Q7 arithmetic for ENN Energy. RMB million unless stated. Inputs: owner_cash_out.json (from owner_cash.py),
# price and share count (Step 0), net debt from the 2026 interim report, sovereign from ChinaBond, FX from CFETS.
import json, os
H = os.path.dirname(os.path.abspath(__file__))
oc = {int(k): v for k, v in json.load(open(os.path.join(H, 'owner_cash_out.json'))).items()}
W = [2021, 2022, 2023, 2024, 2025]
SOV = 0.0206            # ChinaBond government bond yield curve (YTM), 30-year, 2026-10-16
FLOOR = 0.10
SH = 1131.839264        # million ordinary shares, monthly return for September 2026 (HKEXnews 2026-10-02)
PX_HKD = 50.15          # close 2026-10-16, aggregator (Yahoo Finance), flagged
HKD_CNY = 0.85658       # CFETS central parity 2026-10-16 (RMB per HKD)
USD_CNY = 6.7220        # CFETS central parity 2026-10-16
ADS = 4                 # ordinary shares per ADS, F-6EF 2019-11-22
borrow = 9461 + 2435 + 3740 + 3308   # bank and other loans, senior notes, 30 June 2026 (interim report)
cash = 8554
divpay = 2277           # dividend payable at 30 June 2026, paid after the balance-sheet date (stated in the filing)
ND = borrow - cash + divpay
ND_co = borrow - cash   # the company's own net-debt definition
mcap = SH * PX_HKD * HKD_CNY
EV = mcap + ND
TM = 1.0   # terminal multiplier: after year ten, growth stops and purchases stop with it (Q7 specific (c))
def pv(c0, g, r, n=10):
    v = 0; c = c0
    for t in range(1, n + 1):
        c *= (1 + g); v += c / (1 + r) ** t
    return v + c * TM / r / (1 + r) ** n
def irr(c0, g, price):
    lo, hi = 0.0001, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(c0, g, m) > price: lo = m
        else: hi = m
    return m
def cagr(a, b, n): return (b / a) ** (1 / n) - 1 if a > 0 and b > 0 else float('nan')
print(f"market cap RMB {mcap:,.0f}m; net debt {ND:,.0f}m (company definition {ND_co:,.0f}m + dividend payable {divpay:,}m); EV {EV:,.0f}m")
rows = []
PRE = {'ae_acq': 'ae', 'eq_acq': 'eq', 'maint_acq': 'maint', 'ae': 'ae'}
def case(name, key, basis):
    global TM
    base = sum(oc[y][key] for y in W) / 5
    TM = (sum(oc[y][PRE[key]] for y in W) / 5) / base
    print(f"  terminal multiplier (owner cash before purchases / after) {TM:.4f}")
    g = cagr(oc[2021][key], oc[2025][key], 4)
    h1 = (oc[2021][key] + oc[2022][key] + oc[2023][key]) / 3; h2 = (oc[2023][key] + oc[2024][key] + oc[2025][key]) / 3
    gh = cagr(h1, h2, 2)
    price = EV if basis == 'AE' else mcap
    sub = ND if basis == 'AE' else 0
    print(f"\n{name} [{key}] base (5-yr avg) {base:,.0f}; end-year growth {g*100:.2f}%/yr; halves growth {gh*100:.2f}%/yr; literal 2025 {oc[2025][key]:,.0f}")
    for lab, gg in [('no growth', 0.0), ('shown growth', g)]:
        vs = pv(base, gg, SOV); v10 = pv(base, gg, FLOOR)
        r = irr(base, gg, price)
        print(f"  {lab:13s} g={gg*100:5.2f}%  value@sov {vs:>10,.0f} -> per share RMB {(vs-sub)/SH:8.2f} | expected return at price {r*100:5.2f}% | value@10% {v10:>8,.0f} -> RMB {(v10-sub)/SH:6.2f}/sh")
        rows.append((name, lab, vs, v10, r))
    lit = oc[2025][key]
    print(f"  literal window beside: 2025 alone {lit:,.0f} -> no-growth expected return {irr(lit, 0.0, price)*100:.2f}%")
    lo = pv(base, min(0, g), SOV); hi = pv(base, max(0, g), SOV)
    f = (pv(base, 0, FLOOR) + pv(base, g, FLOOR)) / 2
    fp = (f - sub) / SH
    print(f"  range per share RMB {(min(lo,hi)-sub)/SH:.2f} to {(max(lo,hi)-sub)/SH:.2f} (width {max(lo,hi)/min(lo,hi) if basis=='EQ' else (max(lo,hi)-sub)/(min(lo,hi)-sub):.2f}x on equity value)")
    print(f"  FAIR PRICE RMB {fp:.2f} = HK$ {fp/HKD_CNY:.2f} = US$ {fp/HKD_CNY*ADS/(USD_CNY/HKD_CNY):.2f} per ADS")
case("CENTRAL all-equity, all spending, acquisitions deducted, total growth", 'ae_acq', 'AE')
case("BESIDE equity-only, all spending, acquisitions deducted", 'eq_acq', 'EQ')
case("BESIDE all-equity before purchases (pre-acquisition series)", 'ae', 'AE')
case("BESIDE depreciation variant (capex replaced by D&A), acquisitions deducted", 'maint_acq', 'AE')
print(f"\nprice per share RMB {PX_HKD*HKD_CNY:.2f}; HK$ {PX_HKD}; implied ADS US$ {PX_HKD*ADS/(USD_CNY/HKD_CNY):.2f}; USD/HKD cross {USD_CNY/HKD_CNY:.4f}")
