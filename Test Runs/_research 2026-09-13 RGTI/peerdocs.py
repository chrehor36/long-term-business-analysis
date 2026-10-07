import sys, os
sys.path.insert(0, os.path.join(os.getcwd(), "Test Runs/_research 2026-09-13 RGTI"))
import fetch
fetch.OUT = "Test Runs/_research 2026-09-13 RGTI/peers"
L = [("1824920","0001193125-26-071562","ionq-20251231.htm","IONQ_10K_FY2025"),
     ("1824920","0001193125-26-341001","ionq-20260630.htm","IONQ_10Q_2026-06-30"),
     ("1907982","0001907982-26-000026","qbts-20251231.htm","QBTS_10K_FY2025"),
     ("1907982","0001907982-26-000129","qbts-20260630.htm","QBTS_10Q_2026-06-30")]
for a in L:
    try: fetch.grab(*a)
    except Exception as e: print("FAIL", a[-1], e)
