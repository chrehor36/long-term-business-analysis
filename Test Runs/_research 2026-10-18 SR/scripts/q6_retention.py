"""Q6 retention arithmetic (USD M). Net income to common = net income less preferred dividends (filed income statements /
XBRL); common dividends paid (cash-flow statements); common stock issued for cash (cash-flow statements); fiscal year-end
closes from the aggregator (flagged, tools/sources.py chart); year-end shares from the filed equity statements / XBRL."""
ni_common = {2018: 214.2, 2019: 184.6 - 3.4, 2020: 88.6 - 14.8, 2021: 271.7 - 14.8, 2022: 220.8 - 14.8,
             2023: 217.5 - 14.8, 2024: 250.9 - 14.8, 2025: 271.7 - 14.8}
div_paid = {2018: 108.7, 2019: 119.0, 2020: 128.0, 2021: 133.2, 2022: 141.9, 2023: 150.7, 2024: 167.1, 2025: 182.2}
issued = {2018: 154.7, 2019: 19.5, 2020: 41.1, 2021: 1.0, 2022: 51.9, 2023: 41.9, 2024: 287.0, 2025: 76.2}
close = {2017: 74.65, 2020: 53.20, 2025: 81.52}
shares = {2017: 48.26, 2020: 51.61, 2025: 59.03}
for a, b in ((2020, 2025), (2017, 2025)):
    yrs = range(a + 1, b + 1)
    ret = sum(ni_common[y] - div_paid[y] for y in yrs)
    iss = sum(issued[y] for y in yrs)
    mv0, mv1 = close[a] * shares[a], close[b] * shares[b]
    print(f'FY{a+1}-FY{b}: retained {ret:.1f} + new common issued {iss:.1f} = {ret+iss:.1f} put in by owners; '
          f'market value {mv0:.1f} -> {mv1:.1f}, change {mv1-mv0:.1f}; per $1 put in: {(mv1-mv0)/(ret+iss):.2f}')
    print(f'   payout of net income to common: {sum(div_paid[y] for y in yrs)/sum(ni_common[y] for y in yrs):.1%}')
