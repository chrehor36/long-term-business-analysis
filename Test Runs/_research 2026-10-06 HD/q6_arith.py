"""Q6 arithmetic on filed XBRL (10-K cash-flow and equity statements; accessions in history_output.txt and the run file).
Buyback average cost = treasury stock value acquired / treasury shares acquired (shares are tagged in whole millions, so
the averages are approximate)."""
buys = {  # FY: (value $M, shares M)
    "FY2018": (9963, 55), "FY2019": (7000, 32), "FY2021": (15001, 45), "FY2022": (6504, 21),
    "FY2023": (8074, 26), "FY2024": (599, 2),
}
for y, (v, n) in buys.items():
    print(f"{y}: ${v:,}M for ~{n}M shares, average ~${v/n:,.0f}")
ni = [16433, 17105, 15143, 14806, 14156]
div = [6985, 7789, 8383, 8929, 9152]
bb = [14809, 6696, 7951, 649, 0]
acq = [421, 0, 1514, 17644, 5410]
print(f"FY2021-FY2025: net earnings {sum(ni):,}; dividends {sum(div):,} ({100*sum(div)/sum(ni):.0f}%); "
      f"buybacks {sum(bb):,} ({100*sum(bb)/sum(ni):.0f}%); kept {sum(ni)-sum(div)-sum(bb):,}; acquisitions {sum(acq):,}")
print(f"FY2025 dividend payout {100*9152/14156:.0f}% of net earnings; {100*9152/12124:.0f}% of owner cash")
print("10-K performance graph, $100 at FY2020 end -> FY2025 end: HD 156.25, S&P 500 Retail 164.12, S&P 500 200.82")
