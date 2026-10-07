from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
L = {x.split()[2]: x.split() for x in open("filings_list.txt")}
for acc, name in [("0001840856-23-000035","8K_2023-08-04_401"),("0001840856-23-000050","8K_2023-09-13_401"),
                  ("0001213900-25-019722","NT10K_2025-03-04"),("0001213900-24-018784","NT10K_2024-03-01"),
                  ("0001213900-23-087581","NT10Q_2023-11-15"),("0001628280-25-011821","10K_FY2024")]:
    grab(acc, L[acc][3], name)
