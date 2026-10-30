import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fetch_core as F
F.HERE = os.path.dirname(os.path.abspath(__file__))
for acc, doc, name in [("0000109177-23-000054","spb-20230930.htm","SPB_10K_FY2023"),("0000109177-22-000034","spb-20220930.htm","SPB_10K_FY2022")]:
    F.grab(acc, doc, name, cik=109177)
