import sys, os
sys.stdout.reconfigure(encoding="utf-8"); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xb import load, annual
for tk in ["D","DUK","SO","NEE"]:
    cf=load(tk)
    ni=annual(cf,"NetIncomeLoss",mode="first"); eq=annual(cf,"StockholdersEquity",mode="first")
    roes=[]
    line=[]
    for y in range(2016,2026):
        y=str(y); py=str(int(y)-1)
        n=ni.get(y,(None,))[0]; e=eq.get(y,(None,))[0]; pe=eq.get(py,(None,))[0]
        if n is not None and e and pe and e>0 and pe>0:
            r=n/((e+pe)/2); roes.append(r); line.append(f"{y}:{r*100:.1f}%({round(n/1e6)}/{round(e/1e6)})")
        else: line.append(f"{y}:n/a")
    print(tk, "mean", f"{sum(roes)/len(roes)*100:.1f}%", "n", len(roes)); print("  ", " ".join(line))
    print("   accn 2025:", ni.get("2025",(0,0,'-'))[2], " accn 2016:", ni.get("2016",(0,0,'-'))[2])
