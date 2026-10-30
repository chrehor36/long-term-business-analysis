import math
cap=106941980*20.51/1e6; sov=5.35; nd=345.0-45.512-35.443
print("cap",round(cap,1),"net debt",round(nd,1),"EV",round(cap+nd,1))
for lab,oe in [("5y D&A-ex",-58.107),("5y capex",-60.809),("3y23-25 D&A-ex",-52.761),("3y23-25 capex",-56.322),("TTM D&A-ex",-16.579),("TTM capex",-20.315),("best window",-43.691),("worst window",-71.463),("TTM cfSBC D&A-ex",-16.449),("TTM ex-payables capex",-20.315-9.716)]:
    y=100*oe/cap; print(f"{lab:24s} {oe:9.1f} {y:6.2f}% {y-sov:6.2f} pts")
for r in (sov,10): print("needed at",r,"% on cap",round(cap*r/100,1),"on EV",round((cap+nd)*r/100,1))
g=529.5; need=cap*0.10
print("floor OE / FY26 rev guide mid", round(100*need/g,1))
for lab,m in (("JKHY",0.186),("QTWO",0.109),("FISV",0.186)):
    rev=need/m; print(lab,"rev needed",round(rev),"x guide",round(rev/g,2),"yrs@15%",round(math.log(rev/g)/math.log(1.15),1),"yrs@20%",round(math.log(rev/g)/math.log(1.20),1))
print("value at sovereign of TTM best if it were positive: n/a")
print("July-adjusted cap", round(106410360*20.51/1e6,1))
