# q5calc.py - COMPUTATION, NOT A CLEARANCE. Arithmetic only on oe2.py outputs.
CAP = 256.78 * 10_786_313_572 / 1e6   # $M
SH = 10_786_313_572
SOV = 0.0535
bases = [
 ("5-yr 2021-25, formation (TNA) end", -14814),
 ("5-yr 2021-25, gross capex + FL adds (screen)", -13770),
 ("5-yr 2021-25, cash plant", -12211),
 ("3-yr 2023-25, net capex + FL + BTS adds", 5141),
 ("5-yr 2021-25, (c) = 1.3x P&E D&A (renewal-at-scale judgment)", 27591),
 ("3-yr 2023-25, (c) = 1.3x P&E D&A", 46479),
 ("TTM, (c) = 1.3x P&E D&A", 77426),
 ("TTM, (c) = P&E D&A (INVALID end, most generous number constructible)", 92348),
]
print(f"cap ${CAP:,.0f}M")
print("| base | owner earnings $M | yield | vs 5.35% | perpetual g for 10% | perpetual g for bond |")
print("|---|---|---|---|---|---|")
for n, oe in bases:
    y = oe / CAP
    if oe > 0:
        g10 = (0.10 * CAP - oe) / (CAP + oe)
        gb = (SOV * CAP - oe) / (CAP + oe)
        print(f"| {n} | {oe:,} | {y*100:.2f}% | {100*(y-SOV):+.2f} pts | {g10*100:.1f}% | {gb*100:.1f}% |")
    else:
        print(f"| {n} | {oe:,} | {y*100:.2f}% | {100*(y-SOV):+.2f} pts | refused: base below zero | refused |")
# DCF engine: g for 10 years then 3% forever, discounted at 10%, solve g so PV = CAP
def pv(oe, g, r=0.10, tg=0.03, n=10):
    v = 0; c = oe
    for t in range(1, n + 1):
        c *= (1 + g); v += c / (1 + r) ** t
    return v + c * (1 + tg) / (r - tg) / (1 + r) ** n
print()
for n, oe in bases:
    if oe <= 0: continue
    lo, hi = -0.5, 1.0
    for _ in range(200):
        m = (lo + hi) / 2
        if pv(oe, m) < CAP: lo = m
        else: hi = m
    print(f"DCF engine (casts no vote): {n}: {m*100:.1f}% a year for ten years, then 3%, to justify the cap at 10%")
print()
print("| owner earnings | g=0% | 3% | 5% | 6% | 7% |  (per share, Gordon at the 10% floor)")
for n, oe in bases:
    if oe <= 0: continue
    cells = []
    for g in (0, .03, .05, .06, .07):
        cells.append(f"${oe*1e6*(1+g)/(0.10-g)/SH:,.0f}")
    print(f"| {n} ({oe:,}) | " + " | ".join(cells) + " |")
