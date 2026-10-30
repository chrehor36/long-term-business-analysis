# pre-tax return on net operating tangible assets: EBIT / (inventory + net property - accounts payable). Transcription + arithmetic.
import facts
ALT={"ppe":["PropertyPlantAndEquipmentNet","PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization"],
     "inv":["InventoryNet","RetailRelatedInventoryMerchandise"]}
for t in ["LOW","HD","TSCO","FND"]:
    d,ends=facts.table(t,"2008")
    j=facts.load(t)
    ppe={};inv={}
    for n in ALT["ppe"]:
        for e,v in facts.annual(j,[n],instant=True).items(): ppe.setdefault(e,v)
    for n in ALT["inv"]:
        for e,v in facts.annual(j,[n],instant=True).items(): inv.setdefault(e,v)
    print(t,"end  EBIT  inv  ppe  ap  NOTA  EBIT/NOTA  EBIT/sales")
    for e in ends:
        r=d["rev"].get(e); o=d["opinc"].get(e)
        if not o and d["pretax"].get(e) and d["intexp"].get(e): o=(d["pretax"][e][0]+abs(d["intexp"][e][0]),)
        i=inv.get(e); p=ppe.get(e); a=d["ap"].get(e)
        if o and i and p and a and r:
            nota=i[0]+p[0]-a[0]
            print(t,e,round(o[0]/1e6),round(i[0]/1e6),round(p[0]/1e6),round(a[0]/1e6),round(nota/1e6),"%.1f%%"%(100*o[0]/nota),"%.2f%%"%(100*o[0]/r[0]))
