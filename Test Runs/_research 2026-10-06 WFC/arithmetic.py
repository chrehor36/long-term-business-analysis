"""Arithmetic for the WFC run of 2026-10-06. Every input is a filed figure (in $ millions unless noted),
with its source in the comment. Same number sooner; no number added."""

# Price and shares (STEP 0)
shares = 3_023_999_336      # 10-Q cover, period 2026-06-30, accession 0000072971-26-000302 (cover_shares.py)
price = 81.44               # close 2026-10-05, Yahoo chart API via tools/sources.price -- AGGREGATOR, flagged
print("market cap $M", round(shares * price / 1e6, 1))

# Derivative notionals, Table 13.1 of each filing (hedging + not designated)
n_2025 = (377_837 + 8_854 + 6_455) + (11_919_067 + 117_863 + 634_436 + 5_601_838 + 62_336)   # 10-K FY2025
n_2026 = (522_894 + 17_554 + 5_432) + (11_475_877 + 162_959 + 701_879 + 6_496_069 + 66_808)  # 10-Q Q2 2026
equity_2026 = 182_323       # total equity, 10-Q balance sheet 2026-06-30
print("notional 2025-12-31 $M", n_2025, " 2026-06-30 $M", n_2026, " x total equity", round(n_2026 / equity_2026, 1))
print("net derivatives after netting and collateral / equity", round(19_604 / equity_2026, 3))

# Balance-sheet shares, 10-Q 2026-06-30
assets = 2_282_201
liabs = 2_099_878
cib_trading_related = 444_717   # CIB segment, period-end, trading assets ex-derivatives + derivative assets + resale
cib_assets = 862_472
print("CIB trading-related / total assets", round(cib_trading_related / assets, 3))
print("CIB assets / total assets", round(cib_assets / assets, 3))
wholesale = 251_804 + 25_168 + 56_631   # repo + short-term borrowings + trading liabilities
print("repo + STB + trading liabilities $M", wholesale, "share of liabilities", round(wholesale / liabs, 3))
print("noninterest-bearing / total deposits", round(370_116 / 1_501_405, 3))
print("loans / deposits", round(1_031_115 / 1_501_405, 3))

# One-year moves, 10-K FY2025 balance sheet (2025-12-31 against 2024-12-31)
print("repo liabilities +", 232_687 - 95_235, " resale assets +", 193_929 - 105_330,
      " trading assets +", 227_935 - 168_595, " total assets +", 2_148_631 - 1_929_845)
print("uninsured deposits share YE2025", round(600_000 / 1_426_207, 3))
