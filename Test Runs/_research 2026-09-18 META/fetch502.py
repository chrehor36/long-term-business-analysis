from fetch_core import *
import sys
sys.stdout.reconfigure(encoding="utf-8")
for a,d,n in [("0001628280-26-025108","meta-20260408.htm","8K_2026-04-14_502"),("0001628280-26-002429","meta-20260112.htm","8K_2026-01-16_502"),("0001628280-25-058337","meta-20251219.htm","8K_2025-12-19_502")]:
    p=grab(a,d,n); t=open(p,encoding="utf-8").read(); i=t.find("Item 5.02"); print("==",n); print(t[i:i+2500])
