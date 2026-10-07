"""Q5 COMPUTATION - NOT A CLEARANCE, NVDA run. Arithmetic only. Cap = US$218.29 (2026-09-11 close, aggregator, flagged at Step 0)
x 24,147M shares (10-Q 0001045810-26-000075 equity statement at 2026-07-26). Sovereign USD 30-yr 5.35% (US Treasury, 09/11/2026). OE from oe_out.md."""
price, shares = 218.29, 24147.0
cap = price * shares
sov, floor = 0.0535, 0.10
bases = [("5-yr FY2022-26, all out-of-OCF items as (c) (conservative)", 25925), ("5-yr FY2022-26, SBC at grant-date value", 33102),
         ("5-yr FY2022-26, (c)=capex+principal (the judged figure)", 35332), ("5-yr FY2022-26, (c)=depreciation", 36851),
         ("3-yr FY2024-26, capex end", 56525), ("TTM, stakes and full AI cloud backstop as (c)", 62239), ("TTM, capex end less acquisitions", 102545),
         ("TTM, (c)=capex+principal (best judged twelve months)", 119645), ("TTM, (c)=depreciation (most generous judged)", 124147)]
print(f"cap ${cap:,.0f}M")
print("| base | owner earnings $M | yield | vs sovereign 5.35% | perpetual growth for the 10% floor | for the bond |")
print("|---|---|---|---|---|---|")
for n, oe in bases:
    y = oe / cap
    gf = (floor * cap - oe) / (cap + oe); gb = (sov * cap - oe) / (cap + oe)
    print(f"| {n} | {oe:,} | {y*100:.2f}% | {(y-sov)*100:+.2f} pts | {gf*100:.1f}% | {gb*100:.1f}% |")

def dcf_g(oe, r=floor, years=10, term=0.03):
    lo, hi = -0.5, 2.0
    for _ in range(200):
        g = (lo + hi) / 2; v = 0; c = oe
        for t in range(1, years + 1):
            c *= (1 + g); v += c / (1 + r) ** t
        v += c * (1 + term) / (r - term) / (1 + r) ** years
        lo, hi = (g, hi) if v < cap else (lo, g)
    return g
print("\nDCF engine (casts no vote [E3-34]): ten years of growth g then 3% forever, discounted at 10%, to equal the cap:")
for n, oe in bases:
    print(f"  {n}: {dcf_g(oe)*100:.1f}% a year for ten years")
print("\nValue per share at the 10% floor, Gordon OE x (1+g)/(0.10-g):")
gs = [0, 0.03, 0.05, 0.06, 0.07, 0.08]
print("| owner earnings | " + " | ".join(f"g = {g*100:.0f}%" for g in gs) + " |")
print("|---|" + "---|" * len(gs))
for n, oe in [("$25.9bn (5-yr conservative)", 25925), ("$35.3bn (5-yr judged)", 35332), ("$56.5bn (3-yr)", 56525), ("$62.2bn (TTM with stakes and backstop)", 62239),
              ("$119.6bn (TTM judged)", 119645), ("$124.1bn (TTM depreciation end)", 124147)]:
    print(f"| {n} | " + " | ".join(f"${oe*(1+g)/(floor-g)/shares:,.0f}" for g in gs) + " |")
# what the business has done (filed): revenue, OCF, OE capex end
rev = {"FY2017": 6910, "FY2022": 26914, "FY2026": 215938, "TTM": 302970}
print(f"\nrevenue CAGR FY2017-FY2026: {((215938/6910)**(1/9)-1)*100:.1f}%; FY2022-FY2026: {((215938/26914)**(1/4)-1)*100:.1f}%")
print(f"OE (capex end) CAGR FY2017-FY2026: {((90189/1249)**(1/9)-1)*100:.1f}%; FY2022-FY2026: {((90189/6045)**(1/4)-1)*100:.1f}%")
print(f"price / TTM OE {cap/119645:.1f}x ; / 5-yr judged {cap/35332:.1f}x ; / 10-yr {cap/18972:.1f}x")
for n, sh, amt in [("FY2025", 310, 34000), ("FY2026", 282, 40400), ("H1 FY2027", 203, 39800)]:
    p = amt / sh
    print(f"  buyback avg ${p:,.2f} implies perpetual growth for 10% from TTM OE: {((floor*p*shares - 119645)/(p*shares+119645))*100:.1f}%")
