import json
d = json.load(open("companyfacts_1406666.json"))
us = d["facts"]["us-gaap"]
def annual(tag):
    out = {}
    if tag not in us: return out
    for unit, rows in us[tag]["units"].items():
        for r in rows:
            if r.get("form") not in ("10-K","10-K/A") or "start" not in r: continue
            sd, ed = r["start"], r["end"]
            days=(int(ed[:4])*365+int(ed[5:7])*30+int(ed[8:10])) - (int(sd[:4])*365+int(sd[5:7])*30+int(sd[8:10]))
            if not (350 <= days <= 380): continue
            out.setdefault(int(ed[:4]), []).append((r.get("filed",""), r["val"]))
    return {y: sorted(v)[0][1] for y,v in out.items()}
OCF=annual("NetCashProvidedByUsedInOperatingActivities"); SBC=annual("ShareBasedCompensation")
CAPEX=annual("PaymentsToAcquirePropertyPlantAndEquipment")
DA1=annual("DepreciationDepletionAndAmortization"); DA2=annual("Depreciation")
DA={y:DA1.get(y,DA2.get(y)) for y in set(list(DA1)+list(DA2))}
BB=annual("PaymentsForRepurchaseOfCommonStock"); ISS=annual("ProceedsFromStockOptionsExercised")
ys=sorted(OCF); M=1e6
oed={y:(OCF[y]-SBC[y]-DA[y])/M for y in ys}; oec={y:(OCF[y]-SBC[y]-CAPEX[y])/M for y in ys}
print("CUMULATIVE 2009-2025 ($M):")
print(f"  OCF        {sum(OCF.values())/M:9.1f}")
print(f"  SBC        {sum(SBC.values())/M:9.1f}   = {100*sum(SBC.values())/sum(OCF.values()):.1f}% of cumulative OCF")
print(f"  D&A        {sum(DA.values())/M:9.1f}")
print(f"  CAPEX      {sum(CAPEX.values())/M:9.1f}")
print(f"  OE(D&A)    {sum(oed.values()):9.1f}")
print(f"  OE(capex)  {sum(oec.values()):9.1f}")
print(f"  buybacks   {sum(BB.values())/M:9.1f}    option/ESPP proceeds {sum(ISS.values())/M:9.1f}")
print()
print("ROLLING 5-YEAR WINDOWS (owner earnings mean, $M):")
allv=[]
for i in range(len(ys)-4):
    w=ys[i:i+5]
    a=sum(oed[y] for y in w)/5; b=sum(oec[y] for y in w)/5
    allv+=[a,b]
    print(f"  FY{w[0]}-{w[-1]}  D&A end {a:8.2f}   capex end {b:8.2f}")
for n,w in [("3yr FY2023-25",[2023,2024,2025]),("7yr FY2019-25",list(range(2019,2026))),("10yr FY2016-25",list(range(2016,2026))),("17yr FY2009-25",ys),("FY2020-25 (6yr)",list(range(2020,2026)))]:
    a=sum(oed[y] for y in w)/len(w); b=sum(oec[y] for y in w)/len(w); allv+=[a,b]
    print(f"  {n:16s} D&A end {a:8.2f}   capex end {b:8.2f}")
print(f"\n  FULL RANGE: {min(allv):.2f} to {max(allv):.2f}  width ${max(allv)-min(allv):.2f}M")
print(f"  positive windows: {sum(1 for v in allv if v>0)} of {len(allv)}")
print()
print("BEST-YEAR DEPENDENCE:")
for n,w in [("5yr FY2021-25",[2021,2022,2023,2024,2025]),("17yr",ys)]:
    s=sum(OCF[y] for y in w); bb=max(OCF[y] for y in w)
    print(f"  {n}: best year OCF {bb/M:.1f} / window OCF sum {s/M:.1f} = {bb/s:.3f}")
print()
print("SBC/OCF by year, ranked:")
for y in sorted(ys, key=lambda y:-(SBC[y]/OCF[y] if OCF[y]>0 else -9)):
    print(f"  {y}  SBC {SBC[y]/M:7.1f}  OCF {OCF[y]/M:7.1f}  = {100*SBC[y]/OCF[y]:8.1f}%")
