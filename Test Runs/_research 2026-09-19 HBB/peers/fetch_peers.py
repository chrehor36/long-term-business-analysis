import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import fetch_core as F
sys.stdout.reconfigure(encoding="utf-8")
F.HERE = os.path.dirname(os.path.abspath(__file__))
for acc, doc, name, cik in [("0001957132-26-000015","sharkninja-20251231.htm","SN_10K_FY2025",1957132),
                            ("0000109177-25-000043","spb-20250930.htm","SPB_10K_FY2025",109177),
                            ("0000814453-26-000008","nwl-20251231.htm","NWL_10K_FY2025",814453)]:
    try: F.grab(acc, doc, name, cik=cik)
    except Exception as e: print("ERR", name, e)
