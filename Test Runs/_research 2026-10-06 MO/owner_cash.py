"""Owner cash after every real cost, MO, FY2021-FY2025. Arithmetic only; every input is a filed figure.
OCF, capex, D&A: filed cash-flow statements (10-K FY2025 0000764180-26-000017 for 2023-2025; FY2022 10-K
0000764180-23-000020 for 2021-2022), matching tools/run.py and XBRL company facts.
SBC: the stock-compensation note (RSU + PSU pre-tax expense), 10-K FY2025 (2023-2025) and FY2022 (2021-2022);
not a separate line on the cash-flow statement (it sits inside "Other, net"), so it is deducted here."""

years = [2021, 2022, 2023, 2024, 2025]
ocf = {2021: 8405, 2022: 8256, 2023: 9287, 2024: 8753, 2025: 9290}
capex = {2021: 169, 2022: 205, 2023: 196, 2024: 142, 2025: 216}
da = {2021: 244, 2022: 226, 2023: 272, 2024: 286, 2025: 266}
sbc = {2021: 34 + 6, 2022: 41 + 9, 2023: 47 + 11, 2024: 50 + 6, 2025: 51 + 11}

oc_capex = {y: ocf[y] - sbc[y] - capex[y] for y in years}
oc_da = {y: ocf[y] - sbc[y] - da[y] for y in years}
print("FY    OCF   SBC  capex  D&A   OCF-SBC-capex  OCF-SBC-D&A")
for y in years:
    print(f"{y} {ocf[y]:>6} {sbc[y]:>5} {capex[y]:>6} {da[y]:>4}   {oc_capex[y]:>12} {oc_da[y]:>12}")
m_capex = sum(oc_capex.values()) / 5
m_da = sum(oc_da.values()) / 5
print(f"five-year mean   capex basis {m_capex:,.1f}   D&A basis {m_da:,.1f}")

# growth shown, aggregate owner cash, endpoint 2021 -> 2025 (four intervals)
g = (oc_capex[2025] / oc_capex[2021]) ** 0.25 - 1
print(f"aggregate owner cash growth 2021->2025 (capex basis), compound: {g*100:.2f}% a year")

# cash-tax relief from the JUUL ordinary loss: $4.0B claimed on the 2023 return (10-K FY2025 Note 14)
# at the 21% federal statutory rate (arithmetic; the filing does not state the cash effect by year)
relief = 4000 * 0.21
print(f"federal tax on a $4.0B ordinary loss at 21%: {relief:,.0f}")
print(f"five-year mean capex basis less that relief spread over five years: {m_capex - relief/5:,.1f}")

# price, shares, market cap, yield
price = 67.88  # aggregator, 2026-10-05, printed by tools/run.py
shares = 1669.743926  # millions, 10-Q cover 0000764180-26-000094, as of 2026-07-22
cap = price * shares
print(f"market cap: {cap:,.0f} million")
print(f"owner-cash yield at the price: capex basis {m_capex/cap*100:.2f}%  D&A basis {m_da/cap*100:.2f}%")

# debt and cash, 2025-12-31 balance sheet
debt = 24140 + 1569
cash = 4474
print(f"debt {debt:,}  cash {cash:,}  net debt {debt-cash:,}")
# smokeable volume record, 10-Ks
vol = {2016: 122930, 2019: 101799, 2022: 84678, 2025: 61752}
print(f"cigarette shipments 2016->2025: {vol[2025]/vol[2016]*100:.1f}% of 2016; compound {((vol[2025]/vol[2016])**(1/9)-1)*100:.2f}% a year")
oi = {2016: 8762, 2025: 9899 + 1158 + 978}
print(f"operating income 2016 {oi[2016]:,} ; 2025 before the goodwill and asset impairments {oi[2025]:,}")
