"""COMPUTATION, NOT A CLEARANCE: Q7's range and fair price for PED beneath the Q2 stop. USD thousands unless stated."""
r, floor = 0.0543, 0.10
shares = 13_290.902  # thousands
net_debt = 85_000 - 10_805 + 3_800 - 2_500  # revolver less cash at 2026-06-30; Pine Haven payment owed; Weld sale proceeds (10-Q note 18)
legacy_after_int = {2021: 757, 2022: 1_618, 2023: -13_183, 2024: -15_967, 2025: -9_542}
interest = {2025: 590}
def mean(d): return sum(d.values()) / len(d)
def nogrowth(cash, rate): return cash / rate
def per_share(whole, nd): return (whole - nd) / shares
before = {y: v + interest.get(y, 0) for y, v in legacy_after_int.items()}
rows = []
def case(label, cash_before, cash_after=None):
    v = nogrowth(cash_before, r); f = nogrowth(cash_before, floor)
    line = f"{label:58s} mean {cash_before:9,.0f}  value/sh {per_share(v, net_debt):8.2f}  fair/sh {per_share(f, net_debt):8.2f}"
    if cash_after is not None:
        line += f"  | equity-only value/sh {nogrowth(cash_after, r)/shares:7.2f} fair/sh {nogrowth(cash_after, floor)/shares:7.2f}"
    print(line)
print(f"net debt {net_debt:,} ; shares {shares*1000:,.0f} ; price 13.48 ; market cap {13.48*shares/1000:,.1f}M ; EV {(13.48*shares+net_debt)/1000:,.1f}M")
case("CENTRAL organic pair (purchases left out), no growth", mean(before), mean(legacy_after_int))
halves = (mean({k: before[k] for k in (2021, 2022)}), mean({k: before[k] for k in (2024, 2025)}))
print(f"  halves (before interest): first {halves[0]:,.0f}  second {halves[1]:,.0f}  -> sign change, growth meaningless, no-growth case alone (spec. b)")
dflt = dict(before); dflt[2025] -= 115_646
case("BESIDE default pair (merger cash deducted)", mean(dflt))
mc = dict(before); mc[2025] += 7_457
case("BESIDE 2025 merger costs added back (spec. a)", mean(mc))
dda = {2021: -3_862, 2022: 2_731, 2023: 11_998, 2024: -5_013, 2025: -10_014 + 590}
case("BESIDE depreciation variant (maintenance proxy)", mean(dda))
acq = {2023: 134_121 + 21_521 - 174_140, 2024: 69_100 + 19_455 - 50_450, 2025: 7_320 + 12_112 - 9_781}
comb = {y: before[y] + acq[y] for y in (2023, 2024, 2025)}
print("  acquired companies before interest:", acq, " combined:", comb)
case("BESIDE combined companies 2023-2025 (run's CONVENTION)", mean(comb))
h1_pre_wc = 25_873 + 10_850
rr_dda = 2 * (h1_pre_wc - 904 - 22_602 + 2_891)
rr_cash = 2 * (h1_pre_wc - 904 - 20_008 + 2_000 + 2_891)
case("BESIDE H1-2026 run rate x2, DD&A variant (not the convention)", rr_dda)
case("BESIDE H1-2026 run rate x2, cash capex (not the convention)", rr_cash)
print(f"  run-rate yields on EV: DD&A {rr_dda/(13.48*shares+net_debt)*100:.1f}%  cash {rr_cash/(13.48*shares+net_debt)*100:.1f}%")
