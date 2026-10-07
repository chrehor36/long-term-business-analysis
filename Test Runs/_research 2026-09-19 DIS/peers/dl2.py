import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfetch import grab

JOBS = [
    ('1297937', '0001493152-25-027496', 'form10-k.htm', 'PRKA_10K_FY2025.txt'),
    ('1937987', '0001193125-26-131874', 'fbyd-20251231.htm', 'FBYD_10K_FY2025.txt'),
]
for cik, acc, doc, out in JOBS:
    try:
        grab(cik, acc, doc, out)
    except Exception as e:
        print('FAIL', out, e)
