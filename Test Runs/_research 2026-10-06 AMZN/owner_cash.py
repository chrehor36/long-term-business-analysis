"""Owner cash after every real cost, AMZN FY2021-FY2025, USD millions. Arithmetic only.
Inputs read by hand from the filed Consolidated Statements of Cash Flows:
  FY2021, FY2022: 10-K FY2022, accession 0001018724-23-000004
  FY2023-FY2025:  10-K FY2025, accession 0001018724-26-000004
owner cash = OCF - stock pay - purchases of P&E + proceeds and incentives
             - principal repayments of finance leases - principal repayments of financing obligations
D&A variant = OCF - stock pay - D&A (D&A already includes the amortization of finance-lease assets)."""

filed = {
    #       OCF      SBC     capex  proceeds  FL prin  FO prin    D&A
    2021: (46327, 12757, 61053, 5657, 11163, 162, 34433),
    2022: (46752, 19621, 63645, 5324, 7941, 248, 41921),
    2023: (84946, 24023, 52729, 4596, 4384, 271, 48663),
    2024: (115877, 22011, 82999, 5341, 2043, 669, 52795),
    2025: (139514, 19467, 131819, 3499, 1557, 328, 65756),
}
print(f"{'FY':>5} {'OCF':>8} {'SBC':>7} {'capex':>8} {'proc':>6} {'FL':>6} {'FO':>4} {'owner cash':>11} {'D&A':>7} {'D&A var':>8}")
oc_all, dv_all = [], []
for y, (ocf, sbc, cap, pr, fl, fo, da) in filed.items():
    oc = ocf - sbc - cap + pr - fl - fo
    dv = ocf - sbc - da
    oc_all.append(oc)
    dv_all.append(dv)
    print(f"{y:>5} {ocf:>8,} {sbc:>7,} {cap:>8,} {pr:>6,} {fl:>6,} {fo:>4,} {oc:>11,} {da:>7,} {dv:>8,}")
print(f"five-year mean owner cash: {sum(oc_all)/5:,.0f}; D&A variant mean: {sum(dv_all)/5:,.0f}")
shares = 10786.313572  # millions, 10-Q Q2 2026 cover, accession 0001018724-26-000026
price = 251.40
print(f"per share: mean {sum(oc_all)/5/shares:.2f}; D&A variant mean {sum(dv_all)/5/shares:.2f}; "
      f"yield on price: {sum(oc_all)/5/shares/price*100:.2f}% / {sum(dv_all)/5/shares/price*100:.2f}%")
print(f"market cap $M: {shares*price:,.0f}")
# TTM to 2026-06-30 from the 10-Q Q2 2026 (accession 0001018724-26-000026): OCF 161,403; net purchases of P&E 169,007
print(f"TTM to 2026-06-30, OCF less net P&E purchases (the filer's free cash flow, before stock pay and lease principal): {161403-169007:,}")
