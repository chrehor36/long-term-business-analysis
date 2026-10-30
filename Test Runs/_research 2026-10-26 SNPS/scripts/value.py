"""Q7 range and fair price for SNPS (COMPUTATION, NOT A CLEARANCE). USD millions. Arithmetic only.
Every input is a filed figure (accessions in the run file) or a stated CONVENTION of this run."""
T = 0.21            # US federal statutory rate, used only to put interest and deal costs after tax (CONVENTION of this run)
R = 0.0533          # 30-year Treasury par yield, 2026-10-23 (US Treasury, via tools/sources.py)
F = 0.10            # the floor (Part VII fair-price computation)
SH = 191.636646     # cover shares, 10-Q acc 0000883241-26-000025, as of 2026-08-24
PRICE = 430.14      # close 2026-10-23, aggregator, live quote only
DEBT = 1020.247 + 9017.113          # short-term + long-term debt, 10-Q balance sheet 2026-07-31
CASH = 3607.669                      # cash, equivalents and short-term investments, same
NET_DEBT = DEBT - CASH
# SNPS as filed: OCF, SBC, capex, interest paid, interest income (10-K FY2021..FY2025)
snps = {2021: (1492.6, 345.3, 93.8, 3.4, 2.4), 2022: (1738.9, 459.0, 136.6, 1.3, 8.5),
        2023: (1703.3, 563.3, 189.6, 1.0, 36.7), 2024: (1407.0, 692.3, 123.2, 0.8, 67.0),
        2025: (1518.6, 893.3, 169.5, 353.8, 277.7)}
# Ansys calendar years (its 10-Ks): OCF, SBC, capex, interest expense, interest income
anss = {2021: (549.5, 166.3, 23.0, 12.4, 2.1), 2022: (631.0, 168.1, 24.4, 22.7, 5.7),
        2023: (717.1, 221.9, 25.3, 47.1, 19.6), 2024: (795.7, 270.9, 44.0, 47.8, 51.1)}
lock_2025 = 121.6                    # treasury-lock settlement inside FY2025 OCF (10-K cash-flow statement)
deal_cost = {2024: 161.8 - 33.7, 2025: 267.1 - 42.0}   # transaction costs less non-cash bridge amortization (10-K Note 4, cash-flow statement)
def oc(ocf, sbc, cx): return ocf - sbc - cx
def unlev(ip, ii): return (1 - T) * (ip - ii)
rows = {}
for y in range(2021, 2026):
    o, s, c, ip, ii = snps[y]
    sn_asfiled = oc(o, s, c)
    sn = sn_asfiled + unlev(ip, ii) + (1 - T) * deal_cost.get(y, 0) + ((1 - T) * lock_2025 if y == 2025 else 0)
    if y in anss:
        a = anss[y]; an = oc(*a[:3]) + unlev(a[3], a[4])
    else:
        a = anss[2024]; an = (8.5 / 12) * (oc(*a[:3]) + unlev(a[3], a[4]))   # Ansys stub Nov 2024 - 16 Jul 2025, prorated (CONVENTION)
    rows[y] = dict(asfiled=sn_asfiled, snps_unlev=sn, anss=an, combined=sn + an)
for y, r in rows.items():
    print(y, {k: round(v, 1) for k, v in r.items()})
def avg(k): return sum(r[k] for r in rows.values()) / 5
def cagr(k): return (rows[2025][k] / rows[2021][k]) ** 0.25 - 1
def value(base, g, rate):
    """ten years at g, then zero nominal growth for ever, discounted at rate; cash in year 1 = base*(1+g)"""
    pv = 0.0; c = base
    for t in range(1, 11):
        c = c * (1 + g); pv += c / (1 + rate) ** t
    return pv + (c / rate) / (1 + rate) ** 10
def report(name, base, g, netdebt=NET_DEBT, shares=SH):
    cases = {"no growth": 0.0, f"shown growth {g*100:+.1f}%": g}
    vals = {k: value(base, v, R) for k, v in cases.items()}
    fair = sum(value(base, v, F) for v in cases.values()) / 2
    lo, hi = min(vals.values()), max(vals.values())
    ps = lambda v: (v - netdebt) / shares
    print(f"\n{name}: base {base:,.1f}  growth {g*100:+.2f}%")
    for k, v in vals.items(): print(f"   {k:28s} whole {v:10,.0f}  per share {ps(v):8.2f}")
    print(f"   range per share {ps(lo):.2f} to {ps(hi):.2f}  width {hi/lo if lo>0 else float('nan'):.2f}x (whole)  price {PRICE}")
    print(f"   fair price (each end at 10%, averaged) {ps(fair):.2f}")
    # implied return at price: rate r such that average of end cases = EV at price
    ev = PRICE * shares + netdebt
    for k, v in cases.items():
        lo_r, hi_r = 0.0001, 0.5
        for _ in range(100):
            m = (lo_r + hi_r) / 2
            if value(base, v, m) > ev: lo_r = m
            else: hi_r = m
        print(f"   expected return at price, {k}: {m*100:.2f}%")
    return ps(lo), ps(hi), ps(fair)
print(f"\nnet debt {NET_DEBT:,.1f}; market cap {PRICE*SH:,.0f}; EV {PRICE*SH+NET_DEBT:,.0f}")
c_base, c_g = avg("combined"), cagr("combined")
central = report("CENTRAL all-equity, combined companies' averages, purchases left out (serial acquirer: organic pair)", c_base, c_g)
# equity-only beside: owner cash after the run-rate interest on today's debt, against market value (net debt 0 in the subtraction)
coupon = (1000*4.55 + 1000*4.65 + 2000*4.85 + 1500*5.00 + 2400*5.15 + 2100*5.70) / 10000 / 100  # 10-Q Note 11 tranches
int_now = coupon * 10000.0           # run-rate coupon on the $10.0B Senior Notes
cash_yield = 0.040 * CASH            # CONVENTION: interest on today's cash at ~4.0%
eq_base = c_base - (1 - T) * (int_now - cash_yield)
report("EQUITY-ONLY beside (after run-rate interest, against market value)", eq_base, c_g, netdebt=0.0)
# literal window beside: SNPS as filed, no Ansys earnings, all of today's shares and debt
report("LITERAL as filed SNPS window, unadjusted (beside)", avg("asfiled"), cagr("asfiled"))
# default pair beside: purchases deducted net of divestitures, total growth credited
acq = 296.0 + 422.4 + 297.7 + 156.9 + 16681.3 + (510.8 + 386.3 + 208.9 + 1.6)   # SNPS 'Acquisitions, net of cash acquired' + Ansys 2021-24
div = 1446.6 + 746.5
print(f"\nDEFAULT PAIR beside: net purchases over window {acq-div:,.1f}, {(acq-div)/5:,.1f} a year; owner cash before purchases {c_base:,.1f} a year -> after purchases {c_base-(acq-div)/5:,.1f} (not positive; no range)")
print(f"serial-acquirer test: net purchases {acq-div:,.0f} vs half of owner cash before purchases over window {0.5*5*c_base:,.0f}")
