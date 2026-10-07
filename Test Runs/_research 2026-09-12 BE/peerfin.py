import sys, os, json, urllib.request, time
sys.path.insert(0, r"C:\Users\chreh\OneDrive\Documents\BRK\tools")
UA = {"User-Agent": "Chris Hrehor chrehor36@gmail.com"}
CIK = {"CAT":"0000018230","GEV":"0001996810","CMI":"0000026172","FCEL":"0000886128",
       "PLUG":"0001093691","BLDP":"0001453015","GNRC":"0001474735","BE":"0001664703"}
os.makedirs("peerfacts", exist_ok=True)
def facts(t):
    p = os.path.join("peerfacts", t+".json")
    if not os.path.exists(p):
        u = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[t]}.json"
        d = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=120).read()
        open(p,"wb").write(d); time.sleep(0.5)
    return json.load(open(p, encoding="utf-8"))
TAGS = {"rev":["Revenues","RevenueFromContractWithCustomerExcludingAssessedTax","RevenueFromContractWithCustomerIncludingAssessedTax"],
        "cor":["CostOfRevenue","CostOfGoodsAndServicesSold","CostOfGoodsSold"],
        "gp":["GrossProfit"],
        "ocf":["NetCashProvidedByUsedInOperatingActivities","NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
        "sbc":["AllocatedShareBasedCompensationExpense","ShareBasedCompensation"],
        "capex":["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"],
        "da":["DepreciationDepletionAndAmortization","DepreciationAmortizationAndAccretionNet","Depreciation","DepreciationAndAmortization"],
        "ni":["NetIncomeLoss"]}
def series(f, keys):
    out={}
    g=f.get("facts",{}).get("us-gaap",{})
    for tag in keys:
        if tag not in g: continue
        for u,rows in g[tag]["units"].items():
            for r in rows:
                if r.get("form") not in ("10-K","10-K/A","20-F","40-F"): continue
                if "start" in r:
                    from datetime import date
                    s=date.fromisoformat(r["start"]); e=date.fromisoformat(r["end"])
                    if not (330<=(e-s).days<=400): continue
                out.setdefault(r["end"], {}).setdefault(tag, r["val"])
        if out: break
    return {k:list(v.values())[0]/1e6 for k,v in out.items()}
for t in CIK:
    try: f=facts(t)
    except Exception as e:
        print(t,"FETCH FAIL",e); continue
    s={k:series(f,v) for k,v in TAGS.items()}
    ends=sorted(set(s["ocf"])) [-6:]
    print("="*8, t, f.get("entityName"))
    print(f"  {'FYend':12} {'rev':>10} {'GM%':>7} {'OCF':>10} {'SBC':>9} {'capex':>9} {'D&A':>9} {'OE(capex)':>10} {'OE(D&A)':>10}")
    for e in ends:
        rev=s["rev"].get(e); gp=s["gp"].get(e); cor=s["cor"].get(e)
        if gp is None and rev and cor: gp=rev-cor
        gm = (gp/rev*100) if (gp is not None and rev) else None
        ocf=s["ocf"].get(e); sbc=s["sbc"].get(e,0) or 0; cx=s["capex"].get(e); da=s["da"].get(e)
        oe1 = ocf-sbc-cx if (ocf is not None and cx is not None) else None
        oe2 = ocf-sbc-da if (ocf is not None and da is not None) else None
        fmt=lambda v,w=10: (f"{v:{w},.0f}" if v is not None else " "*(w-3)+"n/a")
        print(f"  {e:12} {fmt(rev)} {(f'{gm:7.1f}' if gm is not None else '    n/a')} {fmt(ocf)} {fmt(sbc,9)} {fmt(cx,9)} {fmt(da,9)} {fmt(oe1)} {fmt(oe2)}")
