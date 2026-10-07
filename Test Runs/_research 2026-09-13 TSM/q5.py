"""COMPUTATION - NOT A CLEARANCE. Yield, growth-needed and a staged engine at the ~10% floor [E4-28].
The engine converts growth into a rate; it casts no vote [E3-34]. NT$ millions; cap from Step 0."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
oe = json.load(open(os.path.join(HERE, "oe_out.json")))
SH = 25932364992
PX = 2410.0
CAP = PX * SH / 1e6
ADR_CAP = CAP * 1.12
TWD, USD, FLOOR = 1.886, 5.35, 10.0
bases = {
    "10-yr capex end": oe["windows"]["10-yr 2016-2025"]["oe_capex"],
    "10-yr judged end": oe["windows"]["10-yr 2016-2025"]["oe_judged"],
    "5-yr capex end": oe["windows"]["5-yr 2021-2025"]["oe_capex"],
    "5-yr judged end": oe["windows"]["5-yr 2021-2025"]["oe_judged"],
    "3-yr capex end": oe["windows"]["3-yr 2023-2025"]["oe_capex"],
    "3-yr judged end": oe["windows"]["3-yr 2023-2025"]["oe_judged"],
    "TTM capex end": oe["rows"]["TTM 2026-06"]["oe_capex"],
    "TTM judged end": oe["rows"]["TTM 2026-06"]["oe_judged"],
    "5-yr D&A end (INVALID, display)": oe["windows"]["5-yr 2021-2025"]["oe_da_INVALID"],
}


def gordon_g(oe_, cap, r=0.10):
    # cap = oe*(1+g)/(r-g)  ->  g = (cap*r - oe)/(cap + oe)
    return (cap * r - oe_) / (cap + oe_)


def staged(oe_, g1, years=10, gt=0.03, r=0.10):
    v, x = 0.0, oe_
    for t in range(1, years + 1):
        x *= (1 + g1)
        v += x / (1 + r) ** t
    tv = x * (1 + gt) / (r - gt) / (1 + r) ** years
    return v + tv

print(f"cap NT${CAP:,.0f}M  (ADR-basis cap ~NT${ADR_CAP:,.0f}M)")
out = {}
for k, b in bases.items():
    y = 100 * b / CAP
    g = 100 * gordon_g(b, CAP)
    per = {g1: staged(b, g1) * 1e6 / SH for g1 in (0.0, 0.10, 0.15, 0.20)}
    out[k] = dict(oe=b, yield_pct=y, over_twd=y - TWD, over_usd=y - USD, perpetual_g_needed=g, value_per_share=per,
                  zero_growth_floor_value_ps=b / 0.10 * 1e6 / SH)
    print(f"{k:32s} OE {b:>10,.0f} yield {y:5.2f}% (vs TWD {y-TWD:+.2f}, vs USD {y-USD:+.2f})  g needed {g:4.1f}%  "
          f"floor value/sh: g0 {b/0.10*1e6/SH:>6,.0f} | 10y@10% {per[0.10]:>6,.0f} | 10y@15% {per[0.15]:>6,.0f} | 10y@20% {per[0.20]:>6,.0f}")
json.dump(out, open(os.path.join(HERE, "q5_out.json"), "w"), indent=1)
# ten-year growth record, for 'what the business has actually done'
r = oe["rows"]
print("OE judged-end 2016->2025 CAGR", round(100 * ((r["2025"]["oe_judged"] / r["2016"]["oe_judged"]) ** (1 / 9) - 1), 1))
print("OE capex-end 3yr mean 2016-18 -> 2023-25 CAGR (7 yrs)", round(100 * (((r["2023"]["oe_capex"] + r["2024"]["oe_capex"] + r["2025"]["oe_capex"]) / (r["2016"]["oe_capex"] + r["2017"]["oe_capex"] + r["2018"]["oe_capex"])) ** (1 / 7) - 1), 1))
print("Revenue CAGR 2015-2025 NT$", round(100 * ((3809054.3 / 843497.4) ** (1 / 10) - 1), 1))
