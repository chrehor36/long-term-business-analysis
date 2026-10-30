"""Competitor row, FY2025, from each bank's own 10-K XBRL facts (via xbrl_tables.first). Ratios are mine:
ROA = net income / average of year-end assets 2024 and 2025; cost of deposits = interest expense on deposits /
average of year-end deposits; efficiency = noninterest expense / (net interest income + noninterest income);
equity / assets at year-end 2025. Arithmetic only. Run from the repository root with python -I.
"""
import importlib.util

spec = importlib.util.spec_from_file_location("xt", "Test Runs/_research 2026-10-06 BAC/xbrl_tables.py")
xt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(xt)

for t in ["BAC", "JPM", "WFC", "C"]:
    f = xt.load(t)
    a25, _, accn = xt.first(f, ["Assets"], 2025)
    a24, _, _ = xt.first(f, ["Assets"], 2024)
    d25, _, _ = xt.first(f, ["Deposits"], 2025)
    d24, _, _ = xt.first(f, ["Deposits"], 2024)
    e25, _, _ = xt.first(f, ["StockholdersEquity"], 2025)
    ni, _, _ = xt.first(f, ["NetIncomeLoss"], 2025, "duration")
    nii, _, _ = xt.first(f, ["InterestIncomeExpenseNet"], 2025, "duration")
    noi, _, _ = xt.first(f, ["NoninterestIncome"], 2025, "duration")
    nie, _, _ = xt.first(f, ["NoninterestExpense"], 2025, "duration")
    iod, _, _ = xt.first(f, ["InterestExpenseDeposits"], 2025, "duration")
    print(f"{t} | accn {accn} | ROA {ni / ((a25 + a24) / 2):.2%} | cost of deposits {iod / ((d25 + d24) / 2):.2%} | "
          f"efficiency {nie / (nii + noi):.1%} | equity/assets {e25 / a25:.1%} | deposits/assets {d25 / a25:.1%} | "
          f"NI {ni:.1f} | assets {a25:,.1f}")
