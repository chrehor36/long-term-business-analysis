"""Q3 arithmetic: return on capital employed and on the capital added, fiscal 2017-2025 (USD M).
Capital employed = shareholders' equity (incl. the preferred while outstanding) + long-term debt + current portion +
notes payable - cash. Goodwill (1,171.6 throughout 2017-2025) removed for the tangible figure.
Sources: filed balance sheets in the FY2018 10-K (2017, 2018), FY2021 10-K (2020, 2021), FY2025 10-K (2024, 2025);
2019, 2022, 2023 from XBRL company facts (transcription, flagged). Operating income from the filed income statements /
XBRL; 2020 shown with and without the 148.6 impairment."""
cap = {  # equity, LTD, current LTD, notes payable, cash
 2017: (1991.3, 1995.0, 100.0, 477.3, 7.4),
 2018: (2255.4, 1900.1, 175.5, 553.6, 4.4),
 2019: (2543.0, 2083.0, 0.0, 743.0, 6.0),     # XBRL; current portion not tagged that year
 2020: (2522.3, 2423.7, 60.4, 648.0, 4.1),
 2021: (2658.2, 2939.1, 55.8, 672.0, 4.3),
 2022: (2818.0, 2958.0, 281.0, 1038.0, 6.0),  # XBRL
 2023: (2917.0, 3554.0, 157.0, 956.0, 6.0),   # XBRL
 2024: (3232.7, 3704.4, 42.0, 947.0, 4.5),
 2025: (3389.4, 3369.4, 487.5, 1317.0, 5.7),
}
opinc = {2017: 340.9, 2018: 294.1, 2019: 302.3, 2020: 206.4 + 148.6, 2021: 450.2, 2022: 408.2, 2023: 418.6, 2024: 488.3, 2025: 523.9}
GW = 1171.6
T = 0.247  # 21% federal + 3.7% state, the 10-K's FY2025 rate reconciliation
ce = {y: e + l + c + n - k for y, (e, l, c, n, k) in cap.items()}
print('year  capital  tangible  op.income  pre-tax ROTC(avg)  after-tax at 24.7%')
for y in range(2018, 2026):
    avg_t = (ce[y] + ce[y - 1]) / 2 - GW
    r = opinc[y] / avg_t
    print(f'{y}  {ce[y]:8.1f} {ce[y]-GW:8.1f}   {opinc[y]:7.1f}      {100*r:5.1f}%            {100*r*(1-T):5.1f}%')
d_op = opinc[2025] - opinc[2017]; d_ce = ce[2025] - ce[2017]
print(f'incremental 2017->2025: op income +{d_op:.1f} on capital +{d_ce:.1f}: {100*d_op/d_ce:.1f}% pre-tax, {100*d_op/d_ce*(1-T):.1f}% after tax')
d_op2 = opinc[2025] - opinc[2021]; d_ce2 = ce[2025] - ce[2021]
print(f'incremental 2021->2025: op income +{d_op2:.1f} on capital +{d_ce2:.1f}: {100*d_op2/d_ce2:.1f}% pre-tax, {100*d_op2/d_ce2*(1-T):.1f}% after tax')
d_op3 = opinc[2025] - opinc[2022]; d_ce3 = ce[2025] - ce[2022]
print(f'incremental 2022->2025: op income +{d_op3:.1f} on capital +{d_ce3:.1f}: {100*d_op3/d_ce3:.1f}% pre-tax, {100*d_op3/d_ce3*(1-T):.1f}% after tax')
capex = {2021: 624.8, 2022: 552.2, 2023: 662.5, 2024: 861.3, 2025: 922.4}
da = {2021: 213.1, 2022: 237.3, 2023: 254.8, 2024: 278.4, 2025: 298.2}
print('capital spending / D&A, fiscal 2021-2025:', ', '.join(f'{capex[y]/da[y]:.2f}x' for y in capex),
      f'; five-year {sum(capex.values())/sum(da.values()):.2f}x')
# Spire Missouri earned vs allowed (FY2025): NI 128.3, interest 100.2, rate base plant in service 4,379.6, allowed 7.05% post-tax
earned = (128.3 + 100.2 * (1 - T)) / 4379.6
print(f'Spire Missouri FY2025: (net income + after-tax interest) / 2025-order rate base = {100*earned:.2f}% against 7.05% allowed (post-tax)')
