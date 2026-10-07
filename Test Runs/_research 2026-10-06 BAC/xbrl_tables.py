"""Transcribe year-end balance-sheet and income facts from the SEC XBRL company facts (10-K, FY frames)
for BAC and three peers. Arithmetic only. Run from the repository root with python -I.
Inputs: the companyfacts JSON saved under cache/ (gitignored). Output: printed tables.
"""
import json
import sys

CACHE = "Test Runs/_research 2026-10-06 BAC/cache/"


def load(t):
    return json.load(open(CACHE + f"facts_{t}.json"))["facts"]["us-gaap"]


def fy_end(facts, tag, year, kind="instant"):
    """Value at fiscal year-end `year` from the latest-filed 10-K that reports it."""
    if tag not in facts:
        return None
    best = None
    for unit, rows in facts[tag]["units"].items():
        if unit != "USD":
            continue
        for r in rows:
            if r.get("form") != "10-K":
                continue
            if kind == "instant" and r["end"] == f"{year}-12-31" and "start" not in r:
                pass
            elif kind == "duration" and r["end"] == f"{year}-12-31" and r.get("start") == f"{year}-01-01":
                pass
            else:
                continue
            if best is None or r["filed"] > best["filed"]:
                best = r
    return (best["val"], best["accn"]) if best else None


def first(facts, tags, year, kind="instant"):
    for t in tags:
        v = fy_end(facts, t, year, kind)
        if v:
            return v[0] / 1e9, t, v[1]
    return None, None, None


BS = [
    ("Assets", ["Assets"]),
    ("Deposits", ["Deposits"]),
    ("Loans", ["LoansAndLeasesReceivableNetReportedAmount", "FinancingReceivableExcludingAccruedInterestAfterAllowanceForCreditLoss"]),
    ("Allowance", ["FinancingReceivableAllowanceForCreditLossExcludingAccruedInterest", "LoansAndLeasesReceivableAllowance"]),
    ("TradingAssets", ["TradingSecurities", "AssetsFairValueDisclosure"]),
    ("Goodwill", ["Goodwill"]),
    ("Equity", ["StockholdersEquity"]),
    ("Preferred", ["PreferredStockValue"]),
    ("LTDebt", ["LongTermDebt", "LongTermDebtNoncurrent"]),
    ("RetainedEarnings", ["RetainedEarningsAccumulatedDeficit"]),
]
IS = [
    ("NetIncome", ["NetIncomeLoss"]),
    ("NII", ["InterestIncomeExpenseNet"]),
    ("Provision", ["ProvisionForLoanLeaseAndOtherLosses", "ProvisionForLoanAndLeaseLosses", "ProvisionForCreditLosses"]),
    ("IntOnDeposits", ["InterestExpenseDeposits"]),
    ("NonintExpense", ["NoninterestExpense"]),
    ("NonintIncome", ["NoninterestIncome"]),
    ("PrefDiv", ["PreferredStockDividendsIncomeStatementImpact", "DividendsPreferredStock"]),
]

if __name__ == "__main__":
    tickers = sys.argv[1:] or ["BAC"]
    years = range(2016, 2026)
    for t in tickers:
        f = load(t)
        print(f"\n== {t} ($bn; FY year-end; latest-filed 10-K value) ==")
        cols = [n for n, _ in BS] + [n for n, _ in IS]
        print("year | " + " | ".join(cols))
        for y in years:
            vals = []
            for n, tags in BS:
                v, tag, a = first(f, tags, y)
                vals.append("" if v is None else f"{v:,.1f}")
            for n, tags in IS:
                v, tag, a = first(f, tags, y, "duration")
                vals.append("" if v is None else f"{v:,.1f}")
            print(f"{y} | " + " | ".join(vals))
        v, tag, a = first(f, ["Deposits"], 2025)
        print("cross-check Deposits 2025:", v, tag, a)
