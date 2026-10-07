import json
d = json.load(open("companyfacts_1406666.json"))
us = d["facts"]["us-gaap"]
def annual(tag, prefer_original=True):
    out = {}
    if tag not in us: return out
    for unit, rows in us[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K","10-K/A"): continue
            if "start" not in r: continue
            sd, ed = r["start"], r["end"]
            days=(int(ed[:4])*365+int(ed[5:7])*30+int(ed[8:10])) - (int(sd[:4])*365+int(sd[5:7])*30+int(sd[8:10]))
            if not (350 <= days <= 380): continue
            fy = int(ed[:4])
            out.setdefault(fy, []).append((r.get("filed",""), r["val"], r.get("accn")))
    # earliest filed = as originally reported
    return {y: sorted(v)[0][1] for y,v in out.items()}, {y: sorted(set(x[1] for x in v)) for y,v in out.items()}

OCF,_  = annual("NetCashProvidedByUsedInOperatingActivities")
SBC,_  = annual("ShareBasedCompensation")
CAPEX,_= annual("PaymentsToAcquirePropertyPlantAndEquipment")
DA1,_  = annual("DepreciationDepletionAndAmortization")
DA2,_  = annual("Depreciation")
GP,_   = annual("GrossProfit")
OPINC,_= annual("OperatingIncomeLoss")
RD,_   = annual("ResearchAndDevelopmentExpense")
AP,_   = annual("IncreaseDecreaseInAccountsPayable")
REVa,_ = annual("RevenueFromContractWithCustomerExcludingAssessedTax")
REVb,_ = annual("Revenues")
NI,_   = annual("NetIncomeLoss")
BB,_   = annual("PaymentsForRepurchaseOfCommonStock")
DIL,_  = annual("WeightedAverageNumberOfDilutedSharesOutstanding")

REV = {}
for y in set(list(REVa)+list(REVb)): REV[y]=REVa.get(y, REVb.get(y))
DA = {}
for y in set(list(DA1)+list(DA2)): DA[y]=DA1.get(y, DA2.get(y))

years = sorted(OCF)
k=1000.0
print(f"{'FY':>5} {'REV':>9} {'GM%':>6} {'OPINC':>9} {'NI':>9} {'OCF':>9} {'SBC':>9} {'SBC/OCF':>8} {'D&A':>8} {'CAPEX':>8} {'OE(D&A)':>9} {'OE(cpx)':>9} {'APchg':>8} {'AP/OCF':>7} {'dilSh':>7}")
rows={}
for y in years:
    ocf=OCF[y]/k; sbc=SBC.get(y,0)/k; da=DA.get(y,float('nan'))/k; cpx=CAPEX.get(y,0)/k
    rev=REV.get(y); gp=GP.get(y)
    gm = 100*gp/rev if rev and gp else float('nan')
    oed = ocf-sbc-da; oec = ocf-sbc-cpx
    ap = AP.get(y,0)/k
    rows[y]=dict(ocf=ocf,sbc=sbc,da=da,cpx=cpx,oed=oed,oec=oec,rev=(rev or 0)/k,gm=gm)
    print(f"{y:>5} {(rev or 0)/k:9.1f} {gm:6.1f} {(OPINC.get(y,0))/k:9.1f} {(NI.get(y,0))/k if y in NI else float('nan'):9.1f} {ocf:9.1f} {sbc:9.1f} {100*sbc/ocf if ocf else float('nan'):8.1f} {da:8.1f} {cpx:8.1f} {oed:9.1f} {oec:9.1f} {ap:8.1f} {100*ap/abs(ocf) if ocf else float('nan'):7.1f} {DIL.get(y,0)/1e6:7.1f}")

print()
print("CAPEX/D&A ratio by year:")
for y in years:
    if rows[y]['da']==rows[y]['da']:
        print(f"  {y} {rows[y]['cpx']/rows[y]['da']:.3f}")

print()
print("WINDOW MEANS (owner earnings, $M)")
def mean(ys, key):
    v=[rows[y][key] for y in ys]
    return sum(v)/len(v)
wins = {
 "5yr FY2021-25":[2021,2022,2023,2024,2025],
 "3yr FY2023-25":[2023,2024,2025],
 "7yr FY2019-25":list(range(2019,2026)),
 "10yr FY2016-25":list(range(2016,2026)),
 "17yr FY2009-25":list(range(2009,2026)),
 "5yr FY2016-20":[2016,2017,2018,2019,2020],
 "5yr FY2011-15":[2011,2012,2013,2014,2015],
 "post-platform FY2020-25":list(range(2020,2026)),
}
allv=[]
for n,ys in wins.items():
    a=mean(ys,'oed'); b=mean(ys,'oec')
    allv += [a,b]
    print(f"  {n:26s} D&A end {a:9.2f}   capex end {b:9.2f}   OCF mean {mean(ys,'ocf'):9.2f}  SBC mean {mean(ys,'sbc'):9.2f}")
print(f"\n  RANGE ACROSS ALL WINDOWS AND BOTH (c) ENDS: {min(allv):.2f} to {max(allv):.2f}  (width ${max(allv)-min(allv):.2f}M)")
