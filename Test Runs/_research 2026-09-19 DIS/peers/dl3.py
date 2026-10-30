import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfetch import grab

JOBS = [
    ('1744489', '0001744489-26-000022', 'dis-20260202.htm', 'DIS_8K_2026-02-03.txt'),
    ('1744489', '0001744489-25-000159', 'dis-20251209.htm', 'DIS_8K_2025-12-09.txt'),
]
for cik, acc, doc, out in JOBS:
    try:
        grab(cik, acc, doc, out)
    except Exception as e:
        print('FAIL', out, e)
