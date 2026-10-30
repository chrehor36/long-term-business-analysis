"""ADP run 2026-10-06: owner cash and the Q7 range (framework CONVENTION construction). Arithmetic only.
Inputs: filed cash-flow lines (10-K FY2026 0000008670-26-000030 for FY2024-26; XBRL first-filed vintages for
earlier years, cross-checked: FY2026 OCF 5,441.2 filed = XBRL 5,441.2). USD millions."""
ocf   = {2017:2125.9,2018:2515.2,2019:2688.3,2020:3026.2,2021:3093.3,2022:3099.5,2023:4207.6,2024:4157.6,2025:4939.7,2026:5441.2}
sbc   = {2017:138.9,2018:175.4,2019:167.3,2020:130.8,2021:175.3,2022:201.7,2023:220.4,2024:243.5,2025:266.1,2026:242.6}
capex = {2017:240.2,2018:206.1,2019:162.0,2020:172.7,2021:178.6,2022:174.4,2023:206.3,2024:208.4,2025:168.7,2026:196.6}
intan = {2017:230.4,2018:264.7,2019:404.5,2020:443.7,2021:327.3,2022:379.0,2023:365.3,2024:355.0,2025:378.3,2026:468.5}
da    = {2017:316.1,2018:377.6,2019:409.0,2020:480.0,2021:510.7,2022:515.1,2023:549.3,2024:561.9,2025:582.4,2026:585.9}
acq   = {2017:87.4,2018:612.4,2019:125.5,2020:0.0,2021:0.0,2022:11.7,2023:32.4,2024:33.6,2025:1165.1,2026:22.8}

oc = {y: ocf[y]-sbc[y]-capex[y]-intan[y] for y in ocf}          # all capital spending incl. capitalised software
od = {y: ocf[y]-sbc[y]-da[y] for y in ocf}                       # depreciation variant
print("FY   OCF    SBC  capex  intang  D&A   owner_cash  dep_variant  acquisitions")
for y in ocf:
    print(y, f"{ocf[y]:7.1f} {sbc[y]:6.1f} {capex[y]:6.1f} {intan[y]:6.1f} {da[y]:6.1f} {oc[y]:10.1f} {od[y]:10.1f} {acq[y]:8.1f}")
yrs5 = range(2022, 2027)
base = sum(oc[y] for y in yrs5)/5
based = sum(od[y] for y in yrs5)/5
base_acq = sum(oc[y]-acq[y] for y in yrs5)/5
print(f"5-yr avg owner cash FY22-26: {base:.1f}; dep variant {based:.1f}; after acquisitions too {base_acq:.1f}")
g4 = (oc[2026]/oc[2022])**(1/4)-1
g9 = (oc[2026]/oc[2017])**(1/9)-1
print(f"growth aggregate owner cash FY22-26 {g4:.2%}, FY17-26 {g9:.2%}")

r = 0.0566          # US Treasury 30-yr par yield, 10/05/2026
shares = 397.262737 # 10-K cover, as of 2026-07-31
price = 260.26      # aggregator quote 2026-10-05, flagged
net_claims = 4964.1 + 139.3 - 4368.7   # LT debt + reverse repo - corporate investments (cash + LT securities), 2026-06-30

def value(c, g, rate, years=10):
    pv, cf = 0.0, c
    for t in range(1, years+1):
        cf *= (1+g); pv += cf/(1+rate)**t
    return pv + (cf/rate)/(1+rate)**years      # then zero nominal growth

for label, c in (("five-yr base", base), ("FY2026 base", oc[2026])):
    lo = (c/r - net_claims)/shares
    hi = (value(c, min(g9, r), r) - net_claims)/shares
    print(f"{label}: no-growth ${lo:.0f}  shown-growth (capped at {min(g9,r):.2%}) ${hi:.0f}  width {hi/lo:.2f}x")

# expected return at the price: the rate that equates value to the market's enterprise value
ev = price*shares + net_claims
def irr(c, g):
    lo_, hi_ = 0.0001, 0.5
    for _ in range(200):
        m = (lo_+hi_)/2
        if value(c, g, m) > ev: lo_ = m
        else: hi_ = m
    return m
for c, lab in ((base, "five-yr base"), (oc[2026], "FY2026 base")):
    for g in (0.0, 0.05, 0.0566, 0.07):
        print(f"expected return at ${price} on {lab}, growth {g:.2%} ten years then flat: {irr(c,g):.2%}")
print(f"owner-cash yield at price: five-yr {base/ev:.2%}, FY2026 {oc[2026]/ev:.2%}")

# fair: central case at the 10% floor; cheap: no growth at the 10% floor
central_g = 0.06
for c, lab in ((oc[2026], "FY2026 base"), (base, "five-yr base")):
    fair = (value(c, central_g, 0.10) - net_claims)/shares
    cheap = (c/0.10 - net_claims)/shares
    print(f"{lab}: fair (6% x10y then flat, at 10%) ${fair:.0f}; cheap (no growth at 10%) ${cheap:.0f}")
for g in (0.04, 0.08):
    print(f"  sensitivity FY2026 base growth {g:.0%}: fair ${(value(oc[2026], g, 0.10)-net_claims)/shares:.0f}")
print(f"net claims ahead of common {net_claims:.1f}; market cap {price*shares:.0f}")

# buybacks: average prices paid (10-K FY2026 MD&A; equity statement for FY2024)
print("avg buyback price FY2024", round(1330.9/5.1, 2), "FY2025 289.11 FY2026 242.92 (filed)")
