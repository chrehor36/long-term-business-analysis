import sys
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources
from datetime import date

facts = sources.sec_facts("0000093556")


def dur(tags):
    return sources.annual(facts, tags, vintage="newest")[0]


def inst(tags):
    out = {}
    node = facts["facts"]["us-gaap"]
    for t in tags:
        if t not in node:
            continue
        for u, pts in node[t]["units"].items():
            for x in pts:
                if x.get("form") == "10-K" and not x.get("start"):
                    e, f = x["end"], x.get("filed", "")
                    if e not in out or f > out[e][1]:
                        out[e] = (x["val"] / 1e6, f)
    return {k: v[0] for k, v in out.items()}


rev = dur(["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"])
pretax = dur(["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
              "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"])
intexp = dur(["InterestExpense"])
intinc = dur(["InvestmentIncomeInterest", "InterestIncomeOther", "InterestAndOtherIncome"])
tax = dur(["IncomeTaxExpenseBenefit"])
taxpaid = dur(["IncomeTaxesPaidNet", "IncomeTaxesPaid"])
eq = inst(["StockholdersEquity"])
cash = inst(["CashAndCashEquivalentsAtCarryingValue"])
ltd = inst(["LongTermDebtNoncurrent"])
cur = inst(["LongTermDebtCurrent"])
stb = inst(["ShortTermBorrowings"])
gw = inst(["Goodwill"])

print(f"{'FY':>11} {'rev':>8} {'pretax':>8} {'intExp':>7} {'intInc':>7} {'EBIT':>8} {'EBIT%':>6} {'equity':>8} "
      f"{'debt':>8} {'cash':>7} {'IC':>8} {'preROIC':>7} {'ROE':>6} {'tax%':>6} {'cashtax':>7} {'cashtax%':>8}")
for y in sorted(rev):
    if y < "2012":
        continue
    p, ie, ii = pretax.get(y), intexp.get(y), intinc.get(y, 0.0)
    if p is None or ie is None:
        continue
    ebit = p + ie - ii
    e = eq.get(y)
    d = (ltd.get(y) or 0) + (cur.get(y) or 0) + (stb.get(y) or 0)
    c = cash.get(y) or 0
    ic = (e or 0) + d - c
    t = tax.get(y)
    tp = taxpaid.get(y)
    print(f"{y:>11} {rev[y]:>8,.0f} {p:>8,.0f} {ie:>7,.0f} {ii:>7,.0f} {ebit:>8,.0f} {100*ebit/rev[y]:>5.1f}% "
          f"{(e or 0):>8,.0f} {d:>8,.0f} {c:>7,.0f} {ic:>8,.0f} {100*ebit/ic if ic else 0:>6.1f}% "
          f"{'':>6} {100*t/p if (t and p) else float('nan'):>5.1f}% {tp if tp else float('nan'):>7,.0f} "
          f"{100*tp/p if (tp and p and p>0) else float('nan'):>7.1f}%")
