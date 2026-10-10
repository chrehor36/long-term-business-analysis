"""Competitor row: the same metrics from each filer's own 10-K XBRL (companyfacts), fiscal years 2007-2025.
Metrics: revenue, GAAP operating income, operating margin; pre-tax return on total capital = operating income /
(equity + debt - cash) at year end; goodwill+intangibles share of total assets. Transcription and arithmetic only;
writes cache/comp_out.txt. Each filer's accession for its latest 10-K value is printed beside the figure."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xbrl_series import series

HERE = os.path.dirname(os.path.abspath(__file__))
COS = [("AME", "0001037868"), ("ROP", "0000882835"), ("FTV", "0001659166"), ("DHR", "0000313616"),
       ("TDY", "0001094285"), ("MTD", "0001037646"), ("KEYS", "0001601046")]
REV = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet", "SalesRevenueGoodsNet",
       "RevenueFromContractWithCustomerIncludingAssessedTax"]
OI = ["OperatingIncomeLoss"]
EQ = ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]
DEBT_LT = ["LongTermDebtNoncurrent", "LongTermDebt", "LongTermDebtAndCapitalLeaseObligations"]
DEBT_ST = ["DebtCurrent", "ShortTermBorrowings", "LongTermDebtCurrent", "ShortTermDebtAndCurrentPortionOfLongTermDebt" ]
CASH = ["CashAndCashEquivalentsAtCarryingValue", "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]
GW = ["Goodwill"]
INT = ["IntangibleAssetsNetExcludingGoodwill", "FiniteLivedIntangibleAssetsNet"]
ASSETS = ["Assets"]
ACQ = ["PaymentsToAcquireBusinessesNetOfCashAcquired"]


def maxof(facts, tags):
    merged = {}
    for t in tags:
        for k, v in series(facts, t).items():
            if k not in merged or v[0] > merged[k][0]:
                merged[k] = v
    return merged


def first(facts, tags):
    merged = {}
    for t in tags:
        for k, v in series(facts, t).items():
            if k not in merged:
                merged[k] = v
    return merged


def byyear(s):
    out = {}
    for k, v in s.items():
        y = int(k[:4]) if int(k[5:7]) >= 6 else int(k[:4]) - 1  # fiscal year label: year in which most of FY falls
        out[y] = v
    return out


lines = []
for tk, cik in COS:
    f = json.load(open(os.path.join(HERE, "cache", f"facts_{cik}.json")))
    rev = byyear(maxof(f, REV))
    oi = byyear(first(f, OI))
    note = ""
    if not oi:  # MTD files no OperatingIncomeLoss: EBIT = pre-tax earnings + interest expense, labelled
        pt = byyear(first(f, ["IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
                              "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"]))
        ie = byyear(first(f, ["InterestExpense", "InterestExpenseNonoperating", "InterestExpenseDebt"]))
        oi = {y: (pt[y][0] + ie.get(y, (0,))[0], pt[y][1], pt[y][2]) for y in pt}
        note = "  (op.inc = pre-tax earnings + interest expense; the filer tags no operating income)"
    eq, lt, st, cash = byyear(first(f, EQ)), byyear(first(f, DEBT_LT)), byyear(first(f, ["DebtCurrent"])), byyear(first(f, CASH))
    gw, it, a, acq = byyear(first(f, GW)), byyear(first(f, INT)), byyear(first(f, ASSETS)), byyear(first(f, ACQ))
    lines.append(f"\n=== {tk} (CIK {cik})  FY  revenue  op.inc  margin  ROTC(pre-tax, OI/(eq+debt-cash))  GW+intang/assets  acquisitions")
    for y in range(2007, 2026):
        if y not in rev or y not in oi:
            continue
        r, o = rev[y][0] / 1e6, oi[y][0] / 1e6
        cap = None
        if y in eq:
            cap = eq[y][0] + (lt.get(y, (0,))[0]) + (st.get(y, (0,))[0]) - (cash.get(y, (0,))[0])
        rotc = f"{o*1e6/cap*100:5.1f}%" if cap else "   - "
        gi = f"{(gw.get(y,(0,))[0]+it.get(y,(0,))[0])/a[y][0]*100:5.1f}%" if y in a else "  -  "
        ac = f"{acq[y][0]/1e6:8,.0f}" if y in acq else "       -"
        lines.append(f"   {y}  {r:9,.0f}  {o:8,.0f}  {o/r*100:5.1f}%  {rotc}  {gi}  {ac}   [{rev[y][2]}]")
open(os.path.join(HERE, "cache", "comp_out.txt"), "w", encoding="utf-8").write("\n".join(lines))
