import sys
sys.stdout.reconfigure(encoding="utf-8")
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xb import load, annual
def first(cf, tags):
    for t in tags:
        ns="us-gaap"
        if ":" in t: ns,t=t.split(":")
        r=annual(cf,t,ns,mode="latest")
        if r: return r,t
    return {},None
for tk in ["D","DUK","SO","NEE"]:
    cf=load(tk)
    ni,nit=first(cf,["NetIncomeLossAvailableToCommonStockholdersBasic","NetIncomeLoss"])
    eq,eqt=first(cf,["StockholdersEquity"])
    ocf,_=first(cf,["NetCashProvidedByUsedInOperatingActivities"])
    print(tk, nit, eqt)
    for y in range(2015,2026):
        y=str(y); py=str(int(y)-1)
        n=ni.get(y,(None,))[0]; e=eq.get(y,(None,))[0]; pe=eq.get(py,(None,))[0]
        roe = n/((e+pe)/2) if (n is not None and e and pe) else None
        print(" ",y, "NI", n and round(n/1e6), "EQ", e and round(e/1e6), "ROE", roe and f"{roe*100:.1f}%", "OCF", ocf.get(y,(None,))[0] and round(ocf[y][0]/1e6), ni.get(y,(0,0,''))[2])
