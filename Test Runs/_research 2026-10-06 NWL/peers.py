# gross margin and operating margin by year from each filer's own XBRL (latest-filed 10-K value per year)
import json,subprocess,sys
sys.argv=['x']
exec(open('series.py').read().split("tags=sys.argv")[0].replace("d=json.load(open(sys.argv[1]))['facts']['us-gaap']",""))
def load(f): 
    global d; d=json.load(open(f))['facts']['us-gaap']
def rev():
    out={}
    for t in ('SalesRevenueNet','Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'):
        for y,v in annual(t).items():
            if v[0]>0: out[y]=v[0]
    return out
for tk,f in (('NWL','facts.json'),('CLX','peers/CLX_facts.json'),('SPB','peers/SPB_facts.json'),('HELE','peers/HELE_facts.json'),('HBB','peers/HBB_facts.json'),('TUP','peers/TUP_facts.json')):
    load(f); R=rev(); G={y:v[0] for y,v in annual('GrossProfit').items()}; O={y:v[0] for y,v in annual('OperatingIncomeLoss').items()}
    row=[]
    for y in [str(x) for x in range(2013,2027)]:
        if y in R and y in G:
            s=f"{y}: rev {R[y]/1e6:.0f} GM {G[y]/R[y]:.1%}"
            if y in O: s+=f" OM {O[y]/R[y]:.1%}"
            row.append(s)
    print(tk,'\n  '+'\n  '.join(row))
