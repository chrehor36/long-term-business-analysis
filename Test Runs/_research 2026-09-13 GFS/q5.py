"""COMPUTATION - NOT A CLEARANCE. Yields, growth needed, and a staged engine (casts no vote [E3-34]) for GFS.
Cap = US$46.95 x 558,658,481 (Step 0). Floor ~10% [E4-28]; sovereign USD 30-yr 5.35% (US Treasury, 09/11/2026)."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
P, SH = 46.95, 558_658_481
CAP = P * SH / 1e6
NETCASH = (1087 + 1270 + 946) - (98 + 1024)       # 2026-06-30 interim balance sheet, leases excluded
W = json.load(open(os.path.join(HERE, "oe_out.json")))
cases = {
 "5-yr D&A end": W["windows"]["5-yr 2021-2025"]["oe_da"],
 "5-yr capex end": W["windows"]["5-yr 2021-2025"]["oe_capex"],
 "5-yr capex end less acquisitions (display)": W["windows"]["5-yr 2021-2025"]["oe_capex_less_acq"],
 "4-yr D&A end": W["windows"]["4-yr 2022-2025"]["oe_da"],
 "4-yr capex end": W["windows"]["4-yr 2022-2025"]["oe_capex"],
 "3-yr D&A end": W["windows"]["3-yr 2023-2025"]["oe_da"],
 "3-yr capex end (INVALID, display)": W["windows"]["3-yr 2023-2025"]["oe_capex"],
 "5-yr no prepayment strip, capex end (display)": W["no_strip_5yr"]["capex"],
 "TTM D&A end (display)": W["rows"]["TTM 2026-06"]["oe_da"],
}
def g_needed(oe, price, r=0.10):  # perpetual growth such that price = oe*(1+g)/(r-g)
    return (r * price - oe) / (price + oe)
def staged(oe, g, years=10, r=0.10, gt=0.03):
    v, x = 0.0, oe
    for t in range(1, years + 1):
        x *= (1 + g); v += x / (1 + r) ** t
    tv = x * (1 + gt) / (r - gt) / (1 + r) ** years
    return v + tv
def decade_g_needed(oe, price, r=0.10):
    lo, hi = -0.5, 1.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if staged(oe, mid, r=r) < price: lo = mid
        else: hi = mid
    return mid
out = {"cap": CAP, "netcash": NETCASH}
print(f"cap US${CAP:,.0f}M  net cash US${NETCASH:,.0f}M")
for k, oe in cases.items():
    y = oe / CAP * 100
    gn = g_needed(oe, CAP) * 100
    dg = decade_g_needed(oe, CAP) * 100
    vals = {g: (staged(oe, g / 100) + NETCASH * 0) / SH * 1e6 for g in (0, 5, 10)}
    out[k] = dict(oe=oe, yield_pct=round(y, 2), vs_sov=round(y - 5.35, 2), perp_g_for_10=round(gn, 1), decade_g_for_10=round(dg, 1),
                  value_per_share_0_5_10=[round(vals[0], 1), round(vals[5], 1), round(vals[10], 1)])
    print(f"{k:48s} OE {oe:7.0f}  yield {y:5.2f}%  vs 5.35: {y-5.35:+.2f}  perp g {gn:4.1f}%  decade g {dg:5.1f}%  value/sh @0/5/10% {vals[0]:5.1f} {vals[5]:5.1f} {vals[10]:5.1f}")
json.dump(out, open(os.path.join(HERE, "q5_out.json"), "w"), indent=1)
