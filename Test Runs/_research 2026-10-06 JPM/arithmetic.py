"""JPM run 2026-10-06: the arithmetic behind Step 0 and Q1. Same number sooner; no number added.
Every input is a filed figure (accession in the run file) or the flagged aggregator quote."""

price = 332.38                 # close 2026-10-05, Yahoo chart via tools/sources.price (AGGREGATOR, flagged)
shares = 2_658_186_195         # 10-Q cover, accession 0001628280-26-054343
print(f"market cap            ${price * shares / 1e9:,.1f}B")

# 10-K FY2025, accession 0001628280-26-008131 ($ millions unless noted)
total_assets_25 = 4_424_900
trading_assets_25 = 802_873
equity_25 = 362_438
deriv_recv_gross_25 = 2_496 + 594_960 + 8_926   # levels 1+2+3 before netting
deriv_recv_net_25 = 57_777
netting_25 = 548_605
level3_deriv_25 = 8_926
notional_25_bn = 50_642        # $ billions, total derivative notional
deposits_avg_25 = 2_506_565
nonint_avg_25 = 572_014 + 32_169
deposit_rate_25 = 1.80         # % average rate on total deposits
loans_25 = 1_493_429
deposits_ye_25 = 2_559_320
markets_rev_25 = 35_800        # Markets revenue, $35.8B (MD&A text)
managed_rev_25 = 185_581

print(f"trading assets / total assets FY25     {trading_assets_25 / total_assets_25:.1%}")
print(f"gross derivative receivables FY25      ${deriv_recv_gross_25 / 1e3:,.1f}B; netting ${netting_25 / 1e3:,.1f}B; net ${deriv_recv_net_25 / 1e3:,.1f}B")
print(f"gross derivative receivables / equity  {deriv_recv_gross_25 / equity_25:.2f}x")
print(f"net derivative receivables / equity    {deriv_recv_net_25 / equity_25:.1%}")
print(f"level 3 derivative receivables / equity {level3_deriv_25 / equity_25:.1%}")
print(f"derivative notional / equity           {notional_25_bn * 1e3 / equity_25:,.0f}x")
print(f"noninterest-bearing / avg deposits FY25 {nonint_avg_25 / deposits_avg_25:.1%}")
print(f"loans / year-end deposits FY25          {loans_25 / deposits_ye_25:.1%}")
print(f"Markets revenue / managed revenue FY25  {markets_rev_25 / managed_rev_25:.1%}")

# 10-Q Q2 2026, accession 0001628280-26-054343
total_assets_q2 = 5_015_069
trading_assets_q2 = 1_062_072
equity_q2 = 374_598
print(f"trading assets / total assets Q2-26    {trading_assets_q2 / total_assets_q2:.1%}")
print(f"total assets / equity Q2-26            {total_assets_q2 / equity_q2:.1f}x")
print(f"total assets / equity FY25             {total_assets_25 / equity_25:.1f}x")
