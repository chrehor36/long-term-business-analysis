import sys, os
sys.stdout.reconfigure(encoding="utf-8"); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xb import load, annual
for tk in ["D","DUK","SO","NEE"]:
    cf=load(tk)
    sh=annual(cf,"WeightedAverageNumberOfSharesOutstandingBasic",unit="shares",mode="first")
    ocf=annual(cf,"NetCashProvidedByUsedInOperatingActivities",mode="first")
    cap=annual(cf,"PaymentsToAcquirePropertyPlantAndEquipment",mode="first")
    print(tk, {y: round(sh[y][0]/1e6,1) for y in sorted(sh) if "2015"<=y<="2025"})
    print("  capex", {y: round(cap[y][0]/1e6) for y in sorted(cap) if "2016"<=y<="2025"})
