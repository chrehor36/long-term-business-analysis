from fetch import get
import sys
w=sys.argv[1]
if w=='t': open('treasury_2026.csv','wb').write(get('https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2026/all?type=daily_treasury_yield_curve&field_tdr_date_value=2026&page&_format=csv'))
if w=='s': open('subs.json','wb').write(get('https://data.sec.gov/submissions/CIK0000069733.json'))
if w=='p': open('price_raw.json','wb').write(get('https://query1.finance.yahoo.com/v8/finance/chart/NATH?range=2y&interval=1d'))
