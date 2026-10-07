import json
from datetime import date
TAGS={
 "rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax"],
 "cor":["CostOfRevenue","CostOfGoodsAndServicesSold","CostOfServices"],
 "opi":["OperatingIncomeLoss"],
 "ocf":["NetCashProvidedByUsedInOperatingActivities"],
 "sbc":["ShareBasedCompensation","AllocatedShareBasedCompensationExpense"],
 "ppe":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
 "sw":["PaymentsToDevelopSoftware","PaymentsForSoftware","PaymentsToAcquireSoftware"],
 "ni":["NetIncomeLoss"],
 "assets":["Assets"],"gw":["Goodwill"],"intang":["IntangibleAssetsNetExcludingGoodwill","FiniteLivedIntangibleAssetsNet"],
 "eq":["StockholdersEquity"],
}
def annual(f, tag, instant=False):
    g=f["facts"]["us-gaap"].get(tag)
    if not g: return {}
    out={}
    for u in g["units"].values():
        for x in u:
            if not x["form"].startswith("10-K"): continue
            if instant:
                if "start" in x: continue
            else:
                if "start" not in x: continue
                d=(date.fromisoformat(x["end"])-date.fromisoformat(x["start"])).days
                if not 340<d<380: continue
            k=x["end"]
            if k not in out or x["filed"]>out[k][0]: out[k]=(x["filed"],x["val"])
    return {k:v[1] for k,v in out.items()}
res={}
for t in ["ALKT","QTWO","JKHY","FISV","NCNO"]:
    f=json.load(open(f"{t}_companyfacts.json"))
    data={}
    for k,tags in TAGS.items():
        inst = k in ("assets","gw","intang","eq")
        merged={}
        for tag in tags:
            a=annual(f,tag,inst)
            for e,v in a.items():
                if k in("sbc",): merged[e]=max(merged.get(e,0),v)
                elif k=="sw": merged[e]=merged.get(e,0)+v if tag!="PaymentsToDevelopSoftware" or e not in merged else merged[e]
                else: merged.setdefault(e,v)
        data[k]=merged
    ends=sorted(e for e in data["ocf"] if e>="2020-06-01")
    res[t]={}
    print("=====",t)
    for e in ends:
        r=lambda k: data[k].get(e)
        rev=r("rev"); cor=r("cor"); opi=r("opi"); ocf=r("ocf"); sbc=r("sbc") or 0; ppe=r("ppe") or 0; sw=r("sw") or 0
        oe=ocf-sbc-ppe-sw if ocf is not None else None
        row=dict(rev=rev,gm=(rev-cor)/rev if rev and cor else None,opm=opi/rev if rev and opi is not None else None,ocf=ocf,sbc=sbc,capex=ppe+sw,oe=oe,oem=oe/rev if rev and oe is not None else None,sbc_rev=sbc/rev if rev else None)
        res[t][e]=row
        print(e, {k:(round(v,4) if isinstance(v,float) else v) for k,v in row.items()})
json.dump(res,open("computed.json","w"),indent=1)
