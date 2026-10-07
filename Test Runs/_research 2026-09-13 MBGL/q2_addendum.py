RUN = r"C:\Users\chreh\OneDrive\Documents\BRK\Test Runs\2026-09-13 Run - MBGL Mobility Global.md"
s = open(RUN, encoding="utf-8").read()
anchor = "- **(2) Growth \"with only minor additional investment of capital\": passes.**"
assert anchor in s
add = """  - **The longer revenue record, at its honest rung.** Investor Day p.91 (S&P Global 8-K EX-99.1,
    `0001104659-26-058908`, furnished; company-compiled): revenue **$529M (2014) → $585M → $719M →
    $836M → $979M → $1,074M → $1,052M (2020) → $1,247M → $1,351M → $1,485M → $1,613M → $1,750M
    (2025)**, organic growth *"10% 11% 14% 11% 10% (2%) 18% 10% 9% 9% 9%"* against an industry series
    (FRED vehicle sales) of *"6% 0% (2%) 1% (1%) (15%) 4% (8%) 13% 2% 2%"*. The deck's own footnote:
    *"THESE NUMBERS ARE NOT PREPARED ON A CONSISTENT BASIS AND MAY NOT BE COMPARABLE PERIOD OVER
    PERIOD"* (2014-21 from IHS Markit's Transportation segment *"adjusted to exclude revenue associated
    with other businesses"*, 2022 from S&P Global's segment, 2023-25 audited carve-out). **Read for what
    it can carry: a decade of dollar growth near 10% through flat and falling vehicle volumes, and only
    −2% in 2020 against −15% for the industry — the first half of [E2-44](1) across a cycle.** It is
    revenue for the whole perimeter, not CARFAX; it carries no unit series and no comparison with
    AutoCheck, so it does not touch the two gaps that decide this gate.
"""
s = s.replace(anchor, add + anchor)
open(RUN, "w", encoding="utf-8").write(s)
print("ok")
