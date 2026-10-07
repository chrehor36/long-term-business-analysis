"""Return on unleveraged net tangible operating assets [E2-43] for Colgate, 2016-2025. Arithmetic only.
NTOA = total assets - cash - current marketable securities - goodwill - other intangibles - operating ROU assets
       - (current liabilities - debt due within one year - current operating lease liabilities).
Operating profit is GAAP; a second line adds back only goodwill/intangible IMPAIRMENTS (write-offs of assets NTOA
already excludes). Restructuring charges stay in [E5-33]."""
import json, os
import facts as FX
HERE = os.path.dirname(os.path.abspath(__file__))
g = lambda tag, inst=True: FX.annual(tag, instant=inst)
assets, cash, gw, intang, cl, rou = g("Assets"), g("CashAndCashEquivalentsAtCarryingValue"), g("Goodwill"), g("IntangibleAssetsNetExcludingGoodwill"), g("LiabilitiesCurrent"), g("OperatingLeaseRightOfUseAsset")
mkt = g("MarketableSecuritiesCurrent")
stb, ltdc, dc = g("ShortTermBorrowings"), g("LongTermDebtCurrent"), g("DebtCurrent")
leasec = g("OperatingLeaseLiabilityCurrent")
opinc = g("OperatingIncomeLoss", False)
sales = {}
for _t in ("Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"):
    for _y, _v in g(_t, False).items():
        sales.setdefault(_y, _v)
# impairments of goodwill and intangibles, from the filed cash-flow reconciliations (10-K FY2023, FY2025)
IMPAIR = {2021: 571, 2022: 721, 2025: 919}
# debt payable within one year as filed where tags are thin (10-K balance sheets): 2019 260+254, 2020 258+9, 2021 39+12,
# 2022 11+14, 2023 310+20, 2024 660, 2025 1,117
DEBT_FILED = {2019: 514, 2020: 267, 2021: 51, 2022: 25, 2023: 330, 2024: 660, 2025: 1117}
M = 1e6
rows = []
for y in range(2016, 2026):
    d = DEBT_FILED.get(y)
    if d is None:
        d = ((stb.get(y) or 0) + (ltdc.get(y) or 0)) / M
    ntoa = (assets[y] - cash[y] - (mkt.get(y) or 0) - gw[y] - intang[y] - (rou.get(y) or 0)) / M - (cl[y] / M - d - (leasec.get(y) or 0) / M)
    op = opinc[y] / M
    rows.append((y, sales[y] / M, op, op + IMPAIR.get(y, 0), ntoa, d, (rou.get(y) or 0) / M, (leasec.get(y) or 0) / M))
out = ["| year | net sales | GAAP op. profit | op. margin | + impairments added back | NTOA (year end) | return on avg NTOA, GAAP | return on avg NTOA, impairments added back | debt due <1y used | ROU | current lease liab. |", "|---|---|---|---|---|---|---|---|---|---|---|"]
prev = None
for r in rows:
    y, s, op, opx, nt, d, ru, lc = r
    avg = (nt + prev) / 2 if prev else nt
    out.append(f"| {y} | {s:,.0f} | {op:,.0f} | {op/s:.1%} | {opx:,.0f} | {nt:,.0f} | {op/avg:.1%} | {opx/avg:.1%} | {d:,.0f} | {ru:,.0f} | {lc:,.0f} |")
    prev = nt
open(os.path.join(HERE, "ntoa_out.md"), "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out))
print("stb", {y: v/M for y, v in stb.items() if y > 2014}, "ltdc", {y: v/M for y, v in ltdc.items() if y > 2014}, "dc", dc, "mkt", {y: v/M for y, v in mkt.items()})
