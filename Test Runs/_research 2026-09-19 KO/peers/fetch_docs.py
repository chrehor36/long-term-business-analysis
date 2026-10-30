import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import fetch_core
fetch_core.HERE = os.path.dirname(os.path.abspath(__file__))
jobs=[(865752,"0001104659-26-020831","mnst-20251231x10k.htm","MNST_10K_FY2025"),
      (865752,"0001104659-26-092193","mnst-20260630x10q.htm","MNST_10Q_2026Q2"),
      (1341766,"0001341766-26-000024","celh-20251231.htm","CELH_10K_FY2025"),
      (77476,"0000077476-26-035".replace("-035","-000035"),"pep-20260613.htm","PEP_10Q_2026Q2"),
      (1418135,"0001418135-26-000051","kdp-20260630.htm","KDP_10Q_2026Q2"),
      (1418135,"0001418135-26-000016","kdp-20251231.htm","KDP_10K_FY2025"),
      (77476,"0000077476-26-000007","pep-20251227.htm","PEP_10K_FY2025")]
for c,a,d,n in jobs:
    try: fetch_core.grab(a,d,n,cik=c)
    except Exception as e: print("ERR",n,e)
