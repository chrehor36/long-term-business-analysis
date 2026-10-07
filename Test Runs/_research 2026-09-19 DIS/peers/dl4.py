import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfetch import grab

JOBS = [
    ('1091667', '0001091667-25-000034', 'chtr-20241231.htm', 'CHTR_10K_FY2024.txt'),
    ('1415404', '0001558370-25-001663', 'tmb-20241231x10k.htm', 'ECHO_10K_FY2024.txt'),
]
for cik, acc, doc, out in JOBS:
    try:
        grab(cik, acc, doc, out)
    except Exception as e:
        print('FAIL', out, e)
