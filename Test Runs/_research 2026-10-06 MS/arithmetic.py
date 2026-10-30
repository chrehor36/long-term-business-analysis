"""Step 0 and Q1 arithmetic for the MS run of 2026-10-06. Every input is a filed figure ($ millions unless stated);
sources: 10-K FY2025 acc 0000895421-26-000086; 10-Q 2Q26 acc 0000895421-26-000212; price from tools/sources.price (aggregator)."""
shares = 1_570_566_292          # 10-Q cover, acc 0000895421-26-000212
price = 190.19                  # Yahoo chart close 2026-10-05, AGGREGATOR
print("market cap $M", round(shares * price / 1e6, 1))
# balance sheet, YE2025 (10-K) and 2026-06-30 (10-Q)
ta = {"2025-12-31": 1_420_270, "2026-06-30": 1_675_057}
tl = {"2025-12-31": 1_307_618, "2026-06-30": 1_557_617}
dep = {"2025-12-31": 415_523, "2026-06-30": 446_068}
eq = {"2025-12-31": 111_632, "2026-06-30": 116_329}   # total MS shareholders' equity
for d in ta:
    print(d, "deposits/liabilities", round(dep[d] / tl[d], 3), "assets/equity", round(ta[d] / eq[d], 1))
print("asset growth H1 2026", round(ta["2026-06-30"] / ta["2025-12-31"] - 1, 3))
# segment pre-tax, 10-K segment note: IS, total
is_pt = {2023: 4_476, 2024: 8_749, 2025: 11_237}
tot_pt = {2023: 11_813, 2024: 17_596, 2025: 21_954}
for y in is_pt:
    print(y, "IS share of pre-tax", round(is_pt[y] / tot_pt[y], 3))
print("IS pre-tax 2025 / 2023", round(is_pt[2025] / is_pt[2023], 2))
print("IS segment assets share YE25", round(969_553 / 1_420_270, 3), "2026-06-30", round(1_317_904 / 1_675_057, 3))
print("Level 3 assets / FV assets YE25", round(8_039 / 532_009, 3), "/ equity", round(8_039 / 111_632, 3))
print("gross derivative notional (assets side) 2026-06-30, $19,441bn, / equity", round(19_441_000 / 116_329, 0))
