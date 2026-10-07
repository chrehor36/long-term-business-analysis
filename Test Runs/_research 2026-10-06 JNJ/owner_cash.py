"""Owner cash after every real cost, JNJ, from the FILED consolidated statements of cash flows
(10-K FY2025, accession 0000200406-26-000016, page 47). USD millions. Arithmetic only, not a verdict."""
price, shares = 252.93, 2409.898597  # price: aggregator quote 2026-10-05 via tools/run.py; shares: 10-Q cover 0000200406-26-000153
rows = {  # year: (OCF, stock-based comp, capex, acquisitions net of cash, acquired IPR&D/milestones)
    2023: (22791, 1162, 4543, 0, 470),
    2024: (24266, 1176, 4424, 15146, 1783),
    2025: (24530, 1354, 4832, 17541, 385),
}
cap = price * shares
print(f"market cap {cap:,.0f}M")
oc, oca = [], []
for y, (ocf, sbc, cx, acq, ipr) in rows.items():
    a = ocf - sbc - cx
    b = a - acq - ipr
    oc.append(a)
    oca.append(b)
    print(y, f"owner cash {a:,}  after acquisitions and IPR&D {b:,}")
m, ma = sum(oc) / 3, sum(oca) / 3
print(f"3-yr mean {m:,.0f} (yield {m/cap:.2%}); after acquisitions {ma:,.0f} (yield {ma/cap:.2%})")
print(f"per share {m/shares:.2f}; after acquisitions {ma/shares:.2f}")
