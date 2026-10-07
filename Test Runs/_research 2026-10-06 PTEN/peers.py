# Arithmetic only: sums over spans from each company's own XBRL (10-K facts, earliest vintage).
import re
def load(tk):
    d={}
    for line in open(f"peer_{tk}.txt",encoding="utf-8"):
        if "|" not in line: continue
        tag,vals=line.split("|",1)
        d[tag.strip()]={int(a):float(b) for a,b in re.findall(r"(\d{4}):(-?\d+)",vals)}
    return d
def ser(d,*tags):
    out={}
    for t in tags:
        for y,v in d.get(t,{}).items(): out.setdefault(y,v)
    return out
P={}
for tk in ["HP","NBR","LBRT","PUMP","HAL"]:
    d=load(tk)
    P[tk]=dict(ni=ser(d,"NetIncomeLoss","ProfitLoss","NetIncomeLossAvailableToCommonStockholdersBasic"),
               ocf=ser(d,"NetCashProvidedByUsedInOperatingActivities"),
               cap=ser(d,"PaymentsToAcquirePropertyPlantAndEquipment_alt","PaymentsToAcquirePropertyPlantAndEquipment"),
               rev=ser(d,"Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueNet"),
               eq=ser(d,"StockholdersEquity"),ppe=ser(d,"PropertyPlantAndEquipmentNet"),
               sh=ser(d,"WeightedAverageNumberOfDilutedSharesOutstanding"))
# PTEN from owner_cash.py table (filed statements)
import owner_cash as oc
P["PTEN"]=dict(ni={y:v[5] for y,v in oc.D.items()},ocf={y:v[0] for y,v in oc.D.items()},cap={y:v[2] for y,v in oc.D.items()},
  rev={2007:1986,2008:2064,2009:782,2010:1463,2011:2566,2012:2723,2013:2716,2014:3182,2015:1891,2016:916,2017:2357,2018:3327,2019:2471,2020:1124,2021:1357,2022:2648,2023:4146,2024:5378,2025:4827},
  eq={2012:2641,2013:2756,2014:2906,2015:2561,2016:2249,2017:3982,2018:3505,2019:2834,2020:2016,2021:1609,2022:1666,2023:4812,2024:3466,2025:3219},ppe={},sh={})
def span(tk,a,b):
    p=P[tk]; ys=range(a,b+1)
    miss=[y for y in ys if y not in p["ni"] or y not in p["ocf"] or y not in p["cap"]]
    ni=sum(p["ni"].get(y,0) for y in ys); f=sum(p["ocf"].get(y,0)-p["cap"].get(y,0) for y in ys)
    rv=sum(p["rev"].get(y,0) for y in ys)
    loss=sum(1 for y in ys if p["ni"].get(y,0)<0)
    return ni,f,rv,loss,miss
for a,b in [(2009,2025),(2015,2025),(2019,2025),(2021,2025)]:
    print(f"--- {a}-{b}: sum net income | sum (OCF - capex) | NI/revenue | loss years | missing")
    for tk in ["PTEN","HP","NBR","HAL","LBRT","PUMP"]:
        ni,f,rv,l,m=span(tk,a,b)
        print(f"  {tk:5s} {ni:8.0f} {f:8.0f}  {100*ni/rv if rv else 0:6.1f}%  {l:2d}  {m}")
