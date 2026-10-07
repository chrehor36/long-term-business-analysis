# COMPUTATION - NOT A CLEARANCE. TDS by parts at 2026-06-30 (10-Q 0001051512-26-000063; Array 10-Q 0000821130-26-000046).
r = 0.0566          # 30y UST par, 2026-10-05
floor = 0.10        # CONVENTION (framework Q7), pre-tax
sh = 115.116        # TDS Common + Series A outstanding, M (10-Q balance sheet)
ad_sh, tds_ad = 86.479, 33.005877 + 37.782826   # Array shares outstanding; TDS-held (8-K 2026-06-01)
own = tds_ad / ad_sh
# consolidated stated values, $M
cash_c, tax_c, debt_c = 2194.0, 260.1, 694.1           # cash; accrued taxes; debt principal (market-risk table)
cash_a, tax_a, debt_a = 416.4, 317.4, 325.0 + 363.9    # Array cash; accrued taxes; term loan + retained notes
spectrum = 1584.7 + 10.2 + 19.6                        # C-band etc. book (not under contract) + two pending T-Mobile contract prices
pref = 16.8*25 + 27.6*25                               # liquidation preference, $M (44,400 sh x $25,000)
pref_div = 69.2
# recurring pre-tax streams, $M/yr (Q4 equity-method convention: distributions received)
part_lo, part_hi = 133.1, 158.4   # H1-2026 x2 ; 2021-25 avg ordinary (180,145,150,169,148)
tow_lo, tow_hi = -9.0, 36.0       # towers: ex-interim at current SG&A less capex ; H1-2026 OIBDA x2 less capex 30
tel_capex5 = (-101-268-298+16-87)/5     # Telecom Adj. OIBDA less all capex, 2021-2025
tel_da5 = (112+73+34+69+19)/5           # Telecom Adj. OIBDA less D&A, 2021-2025
corp_lo, corp_hi = -40.0, -30.0         # 'All other' operating loss ex strategic costs (2025: -24.5 incl.; H1-26 -31 incl. ~1)
array_netdebt = cash_a - tax_a - debt_a
tds_x_net = (cash_c - tax_c - debt_c) - array_netdebt   # TDS ex-Array net cash
def per(x): return x/sh
print(f"own of Array {own:.4f}; Array net cash {array_netdebt:,.0f}; TDS ex-Array net cash {tds_x_net:,.0f}")
stated = tds_x_net + own*array_netdebt + own*spectrum - pref
print(f"stated-value net assets to common after preferred: {stated:,.0f}M = ${per(stated):.2f}/sh")
def value(part, tow, tel, corp):
    streams = own*part + own*tow + tel + corp
    return stated + streams/r, streams
lo_v, lo_s = value(part_lo, 0 if tow_lo<0 else tow_lo, 0, corp_lo)       # low end: no-growth; tel at zero (D&A basis, shown growth negative)
hi_v, hi_s = value(part_hi, tow_hi, tel_da5, corp_hi)
print(f"RANGE (D&A variant for Telecom): ${per(lo_v):.2f} .. ${per(hi_v):.2f}  width {hi_v/lo_v:.2f}x")
cx_v, cx_s = value(part_lo, tow_lo, tel_capex5, corp_lo)
print(f"capex-basis low end (Telecom all capex, 5y avg {tel_capex5:.0f}): ${per(cx_v):.2f}  -> width vs high {hi_v/max(cx_v,1e-9):.1f}x")
# FAIR: central streams capitalised at the 10% floor plus stated values
cen_s = own*(part_lo+part_hi)/2 + own*(tow_lo+tow_hi)/2 + (tel_da5+0)/2 + (corp_lo+corp_hi)/2
fair = stated + cen_s/floor
print(f"central pre-tax streams {cen_s:.0f}M/yr; FAIR = ${per(fair):.2f}")
# CHEAP: worst variant of every part at the floor (Telecom on all-capex basis)
worst_s = own*part_lo + own*tow_lo + tel_capex5 + corp_lo
cheap = stated + worst_s/floor
print(f"worst pre-tax streams {worst_s:.0f}M/yr; CHEAP = ${per(cheap):.2f}")
print(f"price 35.11: implied market cap {35.11*sh:,.0f}M; Array stake at AD $34.50 = {tds_ad*34.5:,.0f}M")
