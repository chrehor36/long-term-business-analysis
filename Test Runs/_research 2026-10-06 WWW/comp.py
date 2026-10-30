import sys, json, urllib.request
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
import sources as S
names={"WWW":"0000110471","DECK":"0000910521","SKX":"0001065837","VFC":"0000103379","COLM":"0001050797","RCKY":"0000895456"}
T={"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax","SalesRevenueNet"],"gp":["GrossProfit"],"op":["OperatingIncomeLoss"],"ocf":["NetCashProvidedByUsedInOperatingActivities"],"capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],"sbc":["ShareBasedCompensation"]}
for tk,cik in names.items():
    f=S.sec_facts(cik); D={}
    for k,t in T.items():
        d,_,_=S.annual(f,t,vintage="newest"); D[k]={int(e[:4]) if e[5:7]>'06' else int(e[:4])-1:v for e,v in d.items()}
    yrs=[y for y in range(2011,2026) if y in D["rev"] and y in D["op"]]
    om=[D["op"][y]/D["rev"][y] for y in yrs]
    gm=[D["gp"][y]/D["rev"][y] for y in yrs if y in D["gp"]]
    oc=[ (D["ocf"][y]-D["sbc"].get(y,0)-D["capex"].get(y,0))/D["rev"][y] for y in yrs if y in D["ocf"] and y in D["capex"]]
    neg=sum(1 for x in om if x<0)
    r0,r1=yrs[0],yrs[-1]
    cagr=(D["rev"][r1]/D["rev"][r0])**(1/(r1-r0))-1
    print(f"{tk:5} yrs {r0}-{r1} n={len(yrs)} rev {D['rev'][r0]:.0f}->{D['rev'][r1]:.0f} cagr {cagr*100:5.1f}% | op margin mean {sum(om)/len(om)*100:5.1f}% min {min(om)*100:5.1f}% max {max(om)*100:5.1f}% loss-yrs {neg} | gm mean {sum(gm)/max(len(gm),1)*100:5.1f}% (n={len(gm)}) | (OCF-SBC-capex)/rev mean {sum(oc)/max(len(oc),1)*100:5.1f}% n={len(oc)}")
    print("   op margin by yr:", " ".join(f"{y%100:02d}:{D['op'][y]/D['rev'][y]*100:.0f}" for y in yrs))
    sub=json.load(urllib.request.urlopen(urllib.request.Request(f"https://data.sec.gov/submissions/CIK{cik}.json",headers=S.SEC_UA)))
    r=sub["filings"]["recent"]
    for i in range(len(r["form"])):
        if r["form"][i]=="10-K": print("   latest 10-K", r["filingDate"][i], r["accessionNumber"][i]); break
