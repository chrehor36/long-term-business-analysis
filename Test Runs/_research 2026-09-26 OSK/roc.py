import json
b=json.load(open('bs.json'))
d=json.load(open('companyfacts.json'))['facts']['us-gaap']
def g(t,k): return b.get(t,{}).get(k,0.0)/1e6
ends=['2009-09-30','2010-09-30','2011-09-30','2012-09-30','2013-09-30','2014-09-30','2015-09-30','2016-09-30','2017-09-30','2018-09-30','2019-09-30','2020-09-30','2021-09-30','2021-12-31','2022-12-31','2023-12-31','2024-12-31','2025-12-31']
def adv(k):
    if k in b.get('ContractWithCustomerLiability',{}): return g('ContractWithCustomerLiability',k)
    if k in b.get('ContractWithCustomerLiabilityCurrent',{}): return g('ContractWithCustomerLiabilityCurrent',k)
    return g('CustomerAdvancesCurrent',k)
nto={};toc={}
for k in ends:
    rec=g('ReceivablesNetCurrent',k)+g('ContractWithCustomerAssetNetCurrent',k)
    x=rec+g('InventoryNet',k)+g('PropertyPlantAndEquipmentNet',k)+g('CapitalizedContractCostNet',k)-g('AccountsPayableCurrent',k)-adv(k)
    nto[k]=x; toc[k]=x+g('Goodwill',k)+g('IntangibleAssetsNetExcludingGoodwill',k)
    print(k,'NTOA',round(x,1),'with GW+intang',round(toc[k],1),'adv',round(adv(k),1),'equity',round(g('StockholdersEquity',k),1))
# annual op income, revenue, amort, impairment (filed)
oi={'2010':1424.8,'2011':526.1,'2012':387.7,'2013':505.7,'2014':503.3,'2015':398.6,'2016':364.0,'2017':470.3,'2018':656.0,'2019':797.0,'2020':484.8,'2021':592.1,'2022':372.3,'2023':837.6,'2024':1010.7,'2025':939.5}
rev={'2010':9820.6,'2011':7538.5,'2012':8141.1,'2013':7665.1,'2014':6808.2,'2015':6098.1,'2016':6279.2,'2017':6829.6,'2018':7705.5,'2019':8382.0,'2020':6856.8,'2021':7737.3,'2022':8282.0,'2023':9657.9,'2024':10730.2,'2025':10422.3}
am={'2010':60.5,'2011':59.3,'2012':57.7,'2013':56.6,'2014':55.3,'2015':53.2,'2016':52.5,'2017':45.8,'2018':38.3,'2019':36.9,'2020':11.0,'2021':9.6,'2022':11.6,'2023':41.7,'2024':64.9,'2025':59.7}
imp={'2010':25.6,'2011':4.8,'2013':9.0,'2016':26.9,'2022':7.7,'2024':51.6,'2025':5.7}
ni={'2010':790.0,'2011':273.4,'2012':231.9,'2013':318.0,'2014':309.3,'2015':229.5,'2016':216.4,'2017':285.6,'2018':471.9,'2019':579.4,'2020':324.5,'2021':508.9,'2022':173.9,'2023':598.0,'2024':681.4,'2025':647.0}
yend={y:(f'{y}-09-30' if int(y)<=2021 else f'{y}-12-31') for y in oi}
prev={}
order=list(oi)
for i,y in enumerate(order):
    e=yend[y]
    p = '2009-09-30' if y=='2010' else ( '2021-12-31' if y=='2022' else yend[order[i-1]])
    a1=(nto[e]+nto[p])/2; a2=(toc[e]+toc[p])/2; eq=(g('StockholdersEquity',e)+g('StockholdersEquity',p))/2
    pre=oi[y]+imp.get(y,0)+am[y]
    print(y, f"rev {rev[y]:.0f} GAAPop {oi[y]/rev[y]*100:.1f}% pre-amort/imp {pre/rev[y]*100:.1f}%  on NTOA {pre/a1*100:.1f}%  op(before imp, after amort) on total op cap {(oi[y]+imp.get(y,0))/a2*100:.1f}%  ROE {ni[y]/eq*100:.1f}%")
