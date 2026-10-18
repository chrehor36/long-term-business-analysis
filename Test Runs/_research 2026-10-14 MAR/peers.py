# Competitor row from each filer's own XBRL (10-K / 20-F), USD millions, as filed; simple owner cash = OCF - SBC - capex - software/intangibles.
from xbrl import annual
def series(cik, tag):
    o = annual(cik,[tag]); return {int(k[1]): v[0]/1e6 for k,v in o.items()}
co = {
 "MAR": ("0001048286", "NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation", ["PaymentsToAcquirePropertyPlantAndEquipment","PaymentsToAcquireProductiveAssets"], [], "OperatingIncomeLoss"),
 "HLT": ("0001585689", "NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation", ["PaymentsToAcquirePropertyPlantAndEquipment"], ["PaymentsToAcquireSoftware"], "OperatingIncomeLoss"),
 "IHG": ("0000858446", "CashFlowsFromUsedInOperatingActivities", "AdjustmentsForSharebasedPayments", ["PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"], ["PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities"], "ProfitLossFromOperatingActivities"),
 "H":   ("0001468174", "NetCashProvidedByUsedInOperatingActivities", "ShareBasedCompensation", ["PaymentsToAcquirePropertyPlantAndEquipment"], [], None),
}
ys = range(2017,2026)
for n,(cik,ocf,sbc,capt,softt,oit) in co.items():
    O=series(cik,ocf); S=series(cik,sbc)
    C={}
    for t in capt:
        for y,v in series(cik,t).items(): C.setdefault(y,v)
    if n=="MAR": C[2025]=604
    SW={}
    for t in softt: SW.update(series(cik,t))
    if n=="IHG": SW.setdefault(2025, 43.0)   # 2025 System Fund capital investments per 20-F text (intangibles tag absent); flagged
    oc={y: O[y]-S.get(y,0)-C.get(y,0)-SW.get(y,0) for y in ys if y in O}
    OI = series(cik,oit) if oit else {}
    if n=="H":
        pt=series(cik,"IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest")
        ie=series(cik,"InterestExpense"); ie.update(series(cik,"InterestExpenseNonoperating"))
        OI={y: pt[y]+ie.get(y,0) for y in pt}
    a=lambda d,yy: sum(d[y] for y in yy)/len(yy)
    pre,post=a(oc,[2017,2018,2019]),a(oc,[2023,2024,2025])
    print(n, "owner cash:", " ".join(f"{y}:{oc[y]:,.0f}" for y in ys if y in oc))
    print(n, f"  avg 2017-19 {pre:,.0f} -> 2023-25 {post:,.0f}: {((post/pre)**(1/6)-1):.1%}/yr;  cycle avg 2019-25 {a(oc,range(2019,2026)):,.0f}")
    if OI: print(n, "  operating income:", " ".join(f"{y}:{OI[y]:,.0f}" for y in ys if y in OI), f"| 2017-19 avg {a(OI,[2017,2018,2019]):,.0f} -> 2023-25 avg {a(OI,[2023,2024,2025]):,.0f}: {((a(OI,[2023,2024,2025])/a(OI,[2017,2018,2019]))**(1/6)-1):.1%}/yr")
rooms = {"MAR":(1380921,1779936),"HLT":(971780,1351351),"IHG":(883563,1026177)}
for n,(a19,a25) in rooms.items(): print(n, f"rooms 2019 {a19:,} -> 2025 {a25:,}: {((a25/a19)**(1/6)-1):.2%}/yr")
