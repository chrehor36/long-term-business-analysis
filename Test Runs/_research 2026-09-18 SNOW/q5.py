import sys
sys.stdout.reconfigure(encoding="utf-8")
cap, caph, sov, sh = 119384.0, 123340.0, 5.29, 352.8 + 11.7
cases = [("5y FY2022-26, convention, capex end", -498.2), ("5y, convention, D&A end", -554.9), ("3y FY2024-26, capex end", -516.7),
         ("TTM to 2026-07-31, capex end", -446.6), ("5y, capex end, without the deferred-revenue increment", -1039.5),
         ("display only: TTM cash flow BEFORE stock compensation (the company's own free cash flow)", 1195.3),
         ("display only: FY2027 guided adjusted FCF, 23% x ~$6,357M revenue (product $6,070M / 0.9548)", 0.23 * 6070 / 0.9548)]
print("case | $M | yield on plain cap | yield on perimeter cap | vs sovereign (pts) | perpetual g to reach 10% | g to reach 5.29%")
for n, oe in cases:
    y1, y2 = 100 * oe / cap, 100 * oe / caph
    if oe > 0:
        g10 = 100 * (0.10 - oe / caph) / (1 + oe / caph); gs = 100 * (sov / 100 - oe / caph) / (1 + oe / caph)
        gtxt = f"{g10:.1f}% | {gs:.1f}%"
    else:
        gtxt = "refused: a negative base has no growth rate | refused"
    print(f"{n} | {oe:,.1f} | {y1:.2f}% | {y2:.2f}% | {y2 - sov:+.2f} | {gtxt}")
print("\nvalue per share = base / (0.10 - g) / 364.5M shares (352.8M + 11.7M net convertible claim)")
for n, oe in [("TTM before SBC", 1195.3), ("FY2027 guided adj. FCF", 0.23 * 6070 / 0.9548)]:
    print(n, " | ".join(f"g={g}%: ${oe / (0.10 - g / 100) / sh:,.0f}" for g in (3, 5, 7)))
