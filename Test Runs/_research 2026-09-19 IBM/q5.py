PRICE, SHARES = 229.55, 942134390
CAP = PRICE * SHARES / 1e6
SOV = 5.34
FLOOR = 10.0
LO, HI = 9486.0, 12234.0          # combined owner-earnings band, every window x both (c) ends x both constructions
CENTRE = 10500.0                  # cycle-normalised judgment [E4-41]
print('cap $%.0fM  shares %d  price %.2f' % (CAP, SHARES, PRICE))
for lbl, oe in [('band low', LO), ('judged centre', CENTRE), ('band high', HI)]:
    y = oe / CAP * 100
    print('%-14s OE %8.0f  yield %5.2f%%  vs sovereign %4.2f%% -> %+5.2f points  vs floor %4.1f%% -> %+5.2f points'
          % (lbl, oe, y, SOV, y - SOV, FLOOR, y - FLOOR))
print()
print('--- growth the QUOTE already assumes, to reach the %.0f%% floor (perpetuity: g = floor - yield)' % FLOOR)
for lbl, oe in [('band low', LO), ('judged centre', CENTRE), ('band high', HI)]:
    y = oe / CAP * 100
    print('  %-14s g needed = %.2f%%' % (lbl, FLOOR - y))
print()
print('--- what the business has actually done, on one perimeter (FY2022-FY2025, 3 compounding years)')
for lbl, a, b in [('revenue FY2020->FY2025 (5y, recast line)', 55179.0, 67535.0),
                  ('owner earnings A capex end FY2022->FY2025', 7587.0, 9861.0),
                  ('owner earnings B capex end FY2022->FY2025', 8287.0, 13061.0),
                  ('industrial OCF FY2022->FY2025', 11135.0, 16393.0),
                  ('IBM own free cash flow FY2022->FY2025', 9300.0, 14734.0)]:
    n = 5.0 if '5y' in lbl else 3.0
    print('  %-44s %.2f%% a year' % (lbl, ((b / a) ** (1 / n) - 1) * 100))
print()
print('--- value, as a round-number range, on the judged centre')
for lbl, r, g in [('floor standard, no growth', 0.10, 0.0),
                  ('floor standard, 2% growth', 0.10, 0.02),
                  ('floor standard, 3% growth', 0.10, 0.03),
                  ('bond parity, no growth (NOT a buying standard)', SOV / 100, 0.0)]:
    v = CENTRE / (r - g)
    print('  %-46s $%7.0fM  = $%6.2f a share' % (lbl, v, v / SHARES * 1e6))
print()
print('--- the same, at the TOP of the band (no conservatism spent anywhere)')
for lbl, r, g in [('floor standard, no growth', 0.10, 0.0), ('floor standard, 3% growth', 0.10, 0.03)]:
    v = HI / (r - g)
    print('  %-46s $%7.0fM  = $%6.2f a share' % (lbl, v, v / SHARES * 1e6))
print()
print('--- IBM own free cash flow FY2025 for comparison (no SBC subtracted, finance book added back)')
print('  $14,734M -> %.2f%% of cap ; g needed to the floor = %.2f%%' % (14734.0 / CAP * 100, FLOOR - 14734.0 / CAP * 100))
print()
print('--- dividend')
print('  $6,255M FY2025 -> %.2f%% of cap ; declared quarterly rate $1.69 -> $6.76 a year -> %.2f%% on the price'
      % (6255.0 / CAP * 100, 6.76 / PRICE * 100))
print()
print('--- [E4-35] base-rate check on the growth the floor would need')
print('  fewer than 10 of the 200 most profitable companies of 2000 attained 15%/yr EPS growth over 20 years')
print('  IBM needs about %.1f%% a year in perpetuity merely to REACH the floor at this price' % (FLOOR - CENTRE / CAP * 100))
