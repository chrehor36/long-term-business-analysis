price = 184.26; shares = 370.036176; units_tp = 6.665; cash = 1864.8; sov = 5.29
cap = price*shares; capu = price*(shares+units_tp)
print("cap common", round(cap,1), "cap incl third-party OP units", round(capu,1), "business ex cash", round(capu-cash,1))
cases = [("central (c), five-year FY2021-25", 337.4), ("central (c), three-year FY2023-25", 382.9), ("central (c), FY2025", 550.7),
         ("central (c), TTM to 2026-06-30 (insurance-flattered)", 994.8), ("conservative (c), FY2025", 183.7), ("conservative (c), five-year", 2.7),
         ("display: company (c), FY2025", 1870.1), ("display: central FY2025 + five-year mean realised gains 809.9", 550.7+809.9),
         ("display: AFFO FY2025 (company)", 2268.2), ("display: Core FFO FY2025 (company)", 2557.8)]
for nm, oe in cases:
    y = oe/capu*100
    print(f"{nm:62s} OE {oe:8.1f}  yield {y:5.2f}%  vs sov {y-sov:+.2f} pts  g to 10% {10-y:5.2f}%")
print("value per share (common+units) = OE/(0.10-g):")
for nm, oe in [("central FY2025", 550.7), ("central five-year", 337.4), ("company (c) FY2025", 1870.1)]:
    print(nm, {g: round(oe/(0.10-g/100)/(shares+units_tp),0) for g in (3,5,7,8)})
