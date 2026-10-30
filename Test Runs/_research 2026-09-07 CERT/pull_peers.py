import sys; sys.path.insert(0,'.')
from fetch import pull, get
jobs=[
 ('1023459','0001023459-25-000060','simu-20250831.htm','SLP_10K_FY2025'),
 ('1023459','0001023459-24-000136','simu-20240831.htm','SLP_10K_FY2024'),
 ('1023459','0001023459-26-000038','simu-20260531.htm','SLP_10Q_FY2026Q3'),
 ('1490978','0001490978-26-000010','sdgr-20251231.htm','SDGR_10K_FY2025'),
]
for j in jobs:
    try: pull(*j)
    except SystemExit as e: print('FAIL',j,e)
# companyfacts
for tic,cik in [('SLP','0001023459'),('SDGR','0001490978')]:
    b=get(f'https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json')
    open(f'companyfacts_{tic}.json','wb').write(b); print('facts',tic,len(b))
