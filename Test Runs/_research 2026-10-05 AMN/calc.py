# COMPUTATION - NOT A CLEARANCE. Inputs from filings (see run file); USD millions.
r=0.0566; sh=38.730; price=36.82; tax=73.610/284.289  # 2023 effective rate, 10-K FY2025
ocf={2011:19.3,2012:60.5,2013:58.6,2014:27.7,2015:56.3,2016:131.9,2017:115.3,2018:227.0,2019:224.9,2020:256.8,2021:305.4,2022:653.7,2023:372.2,2024:320.4,2025:269.5}
sbc={2011:7.1,2012:6.2,2013:6.1,2014:7.2,2015:10.3,2016:11.4,2017:10.2,2018:10.8,2019:16.2,2020:20.5,2021:25.2,2022:30.1,2023:18.0,2024:23.3,2025:30.7}
cap={2011:4.6,2012:5.5,2013:9.0,2014:19.1,2015:27.0,2016:22.0,2017:26.5,2018:35.2,2019:35.2,2020:37.7,2021:53.6,2022:75.8,2023:103.7,2024:80.9,2025:35.6}
acq={2016:216.5,2017:0,2018:217.4,2019:247.9,2020:476.5,2021:41.3,2022:69.6,2023:292.2,2024:0,2025:0}
oe={y:ocf[y]-sbc[y]-cap[y] for y in ocf}
for y in sorted(oe): print(y, round(oe[y],1))
m5=sum(oe[y] for y in range(2021,2026))/5; m10=sum(oe[y] for y in range(2016,2026))/10; m15=sum(oe.values())/15
g5=(oe[2025]/oe[2021])**(1/4)-1
print("mean5",round(m5,1),"mean10",round(m10,1),"mean15",round(m15,1),"g5 %.2f%%"%(100*g5))
print("acq 10y mean",sum(acq.values())/10, "oe10 after acq", round(m10-sum(acq.values())/10,1))
def val(oe0,g):
    v=0;x=oe0
    for t in range(1,11): x*=1+g; v+=x/(1+r)**t
    return v+x/r/(1+r)**10
for name,base in [("5yr",m5),("10yr",m10),("15yr",m15)]:
    a=val(base,0); b=val(base,g5)
    print(name,"nogrowth %.0f = $%.2f; shown g %.0f = $%.2f; ratio %.2f"%(a,a/sh,b,b/sh,a/b))
# trough 2025 pre-working-capital
wc25=101.032; pre=269.457-wc25
t_cap=pre-30.683-35.629; t_dep=pre-30.683-(69.8+8.731)
print("2025 preWC OCF %.1f trough capex %.1f trough dep %.1f"%(pre,t_cap,t_dep))
print("tax rate %.3f"%tax)
fair=m10/(1-tax)/0.10; fair_dep=None
print("FAIR equity %.0f = $%.2f"%(fair,fair/sh))
print("fair on 5yr %.2f"%(m5/(1-tax)/0.10/sh))
for n,t in [("cheap dep",t_dep),("cheap capex",t_cap)]:
    c=t/(1-tax)/0.10; print(n,"%.0f = $%.2f"%(c,c/sh))
mc=price*sh; print("mcap %.0f; netdebt Dec25 %.0f; EV %.0f"%(mc,775-33.972,mc+775-33.972))
print("pretax yield at price on 10yr %.1f%%, on trough dep %.1f%%"%(100*m10/(1-tax)/mc,100*t_dep/(1-tax)/mc))
