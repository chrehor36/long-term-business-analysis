# COMPUTATION - NOT A CLEARANCE. Engine only; casts no vote [E3-34].
shares = 1597251633
price = 47.26
cap = price * shares / 1e6
sov = 0.0535
floor = 0.10
oe = {"cons_3yr": 1670, "cons_TTM": 1686, "gen_2yr": 2024}
de_ttm = 2837
print("cap $M %.0f" % cap)
for k, v in oe.items():
    y = v / cap
    print(k, "yield %.2f%%" % (100 * y), "pts vs sovereign %.2f" % (100 * (y - sov)),
          "| perpetual g needed at sovereign %.2f%%, at floor %.2f%%" % (100 * (sov - y), 100 * (floor - y)),
          "| zero-growth value/share at sov $%.1f, at floor $%.1f" % (v / sov / shares * 1e6, v / floor / shares * 1e6))
print("DE TTM yield %.2f%% (management measure, not used)" % (100 * de_ttm / cap))

def engine(base, g1, n, g2, r):
    v, cf = 0.0, base
    for t in range(1, n + 1):
        cf *= 1 + g1
        v += cf / (1 + r) ** t
    tv = cf * (1 + g2) / (r - g2) / (1 + r) ** n
    return (v + tv) / shares * 1e6

print()
for label, base, g1, n, g2 in [("conservative: 1,670, 8% x10, 3% after", 1670, 0.08, 10, 0.03),
                               ("central: 1,860, 12% x10, 4% after", 1860, 0.12, 10, 0.04),
                               ("plan-shaped: 2,024, 15% x10, 4% after", 2024, 0.15, 10, 0.04),
                               ("plan-shaped: 2,024, 15% x10, 5% after", 2024, 0.15, 10, 0.05)]:
    print(label, "| at 10%% floor $%.0f/share" % engine(base, g1, n, g2, floor))
# growth needed for 10 years (then 4%) to reach the price at the 10% floor
for base in (1670, 2024):
    lo, hi = 0.0, 0.6
    for _ in range(60):
        mid = (lo + hi) / 2
        if engine(base, mid, 10, 0.04, floor) < price: lo = mid
        else: hi = mid
    print("base", base, "10-yr growth needed (then 4%%) at the floor: %.1f%%" % (100 * mid))
# year-1 growth needed in the template sense: price = OE*(1+g)/(r-g) at the sovereign
for base in (1670, 2024):
    # solve cap = base*(1+g)/(sov-g)
    g = (cap * sov - base) / (cap + base)
    print("base", base, "perpetual growth implied at the sovereign %.2f%%" % (100 * g))
