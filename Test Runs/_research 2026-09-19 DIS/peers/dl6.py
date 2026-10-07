import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfetch import grab

for cik, acc, doc, out in [
    ('1484769', '0001628280-26-053535', 'fubo-20260630.htm', 'FUBO_10Q_2026-06-30.txt'),
    ('1484769', '0001628280-26-005782', 'fubo-20251231.htm', 'FUBO_10Q_2025-12-31.txt'),
]:
    try:
        grab(cik, acc, doc, out)
    except Exception as e:
        print('FAIL', out, e)
