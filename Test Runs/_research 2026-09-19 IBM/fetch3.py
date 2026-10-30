import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch2 import grab
grab('0000051143-26-000010','ibm-20251231_d2.htm','AR_FY2025.txt')
grab('0000051143-26-000077','ibm-20260722xex991.htm','EX991_2026Q2.txt')
