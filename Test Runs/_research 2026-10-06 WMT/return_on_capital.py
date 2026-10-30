"""Return on the capital the business needs (net tangible operating capital), WMT, FY2022-FY2026 ($ millions).
Net tangible operating capital = total assets - cash - goodwill - accounts payable - accrued liabilities - accrued income taxes
(operating-lease and finance-lease right-of-use assets stay in, as the stores the business needs).
Balance sheets as filed: FY2026/FY2025 10-K 0000104169-26-000055; FY2024 10-K 0000104169-25-000021 comparatives via
0000104169-26-000055 MD&A 'Certain Balance Sheet Data' (assets, AP, accrued) and run.py transcription (cash, goodwill);
FY2023/FY2022 10-K 0000104169-23-000020. FY2021 is not used: it carries Asda and Seiyu as held for sale.
Operating income from the filed income statements. Tax at the filed effective rates is not applied line by line; the
pre-tax return is shown and an after-tax reading at about 24% (FY2026 effective rate 24.4%) beside it."""
bs = {  # FY: (total assets, cash, goodwill, AP, accrued, accrued taxes)
    2022: (244860, 14760, 29014, 55261, 26060, 851),
    2023: (243197, 8625, 28174, 53742, 31126, 727),
    2024: (252399, 9867, 28113, 56812, 28759, None),
    2025: (260823, 9037, 28792, 58666, 29345, 608),
    2026: (284668, 10727, 28735, 63061, 31187, 596),
}
opinc = {2022: 25942, 2023: 20428, 2024: 27012, 2025: 29348, 2026: 29825}
cap = {}
for fy, (ta, c, gw, ap, acc, tx) in bs.items():
    tx = tx if tx is not None else 0  # FY2024 accrued income taxes not transcribed; immaterial (hundreds of millions)
    cap[fy] = ta - c - gw - ap - acc - tx
for fy in bs:
    print(f"FY{fy}: net tangible operating capital {cap[fy]:,}; operating income {opinc[fy]:,}; pre-tax return {opinc[fy]/cap[fy]:.1%}; after ~24% tax {opinc[fy]*0.76/cap[fy]:.1%}")
for a, b in ((2022, 2026), (2023, 2026)):
    dc, do = cap[b] - cap[a], opinc[b] - opinc[a]
    print(f"incremental FY{a}->FY{b}: capital +{dc:,}, operating income +{do:,}, pre-tax {do/dc:.1%}")
avg_ret = sum(opinc[y] / cap[y] for y in bs) / len(bs)
print(f"five-year mean pre-tax return {avg_ret:.1%}")
