import json
exec(open('series.py').read().split('for t in sys.argv')[0])
S=annual('Revenues'); S.update({k:v for k,v in annual('SalesRevenueNet').items() if k not in S})
GP=annual('GrossProfit'); OI=annual('OperatingIncomeLoss'); OCF=annual('NetCashProvidedByUsedInOperatingActivities')
CX=annual('PaymentsToAcquirePropertyPlantAndEquipment'); SBC=annual('ShareBasedCompensation')
DEP=annual('Depreciation'); AM=annual('AmortizationOfIntangibleAssets'); ACQ=annual('PaymentsToAcquireBusinessesNetOfCashAcquired')
BB=annual('PaymentsForRepurchaseOfCommonStock'); DIV=annual('PaymentsOfDividends'); SH=annual('WeightedAverageNumberOfDilutedSharesOutstanding')
NI=annual('NetIncomeLoss')
print('yr   sales   GM%   OM%   NI    OCF   SBC  capex  D&A   OCcapex OCda  acq   buyb  div  dilsh')
rows={}
for y in range(2008,2026):
    da=DEP.get(y,0)+AM.get(y,0)
    oc=OCF[y]-SBC[y]-CX[y]; od=OCF[y]-SBC[y]-da
    rows[y]=(oc,od)
    print(f"{y} {S[y]/1e6:7.1f} {GP[y]/S[y]*100:5.1f} {OI[y]/S[y]*100:5.1f} {NI[y]/1e6:6.1f} {OCF[y]/1e6:6.1f} {SBC[y]/1e6:5.1f} {CX[y]/1e6:5.1f} {da/1e6:5.1f} {oc/1e6:7.1f} {od/1e6:6.1f} {ACQ.get(y,0)/1e6:6.1f} {BB.get(y,0)/1e6:6.1f} {DIV.get(y,0)/1e6:5.1f} {SH[y]/1e6:5.1f}")
import statistics as st
for a,b in [(2021,2025),(2016,2025),(2008,2025),(2008,2019),(2017,2019)]:
    m=st.mean(rows[y][0] for y in range(a,b+1))/1e6; m2=st.mean(rows[y][1] for y in range(a,b+1))/1e6
    mni=st.mean(NI[y] for y in range(a,b+1))/1e6
    print(a,b,'mean OC capex',round(m,1),'OC D&A',round(m2,1),'NI',round(mni,1))
