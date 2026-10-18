import json,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from peers import pick, B
names={'0000731802':'ATO','0001587732':'OGS','0001733998':'NWN'}
def stats(ni,eq,ocf,cap,da,yrs):
    roe=[ni[y]/((eq[y]+eq[y-1])/2) for y in yrs if y in ni and y in eq and y-1 in eq]
    return dict(roe_avg=sum(roe)/len(roe), roe=[round(r*100,1) for r in roe], cap_da=sum(cap[y] for y in yrs)/sum(da[y] for y in yrs), ocf_minus_cap=sum(ocf[y]-cap[y] for y in yrs))
for cik,n in names.items():
    f=json.load(open(os.path.join(B,f'facts_{cik}.json')))
    g=lambda tags:{int(k[:4]):v[0]/1e6 for k,v in pick(f,tags).items()}
    ni=g(['NetIncomeLoss','ProfitLoss']); eq=g(['StockholdersEquity']); ocf=g(['NetCashProvidedByUsedInOperatingActivities'])
    cap=g(['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
    da=g(['DepreciationDepletionAndAmortization','DepreciationAndAmortization','DepreciationAmortizationAndAccretionNet'])
    for w,yrs in [('2021-25',range(2021,2026)),('2017-25',range(2017,2026))]:
        try: s=stats(ni,eq,ocf,cap,da,yrs); print(n,w,{k:(round(v,3) if isinstance(v,float) else v) for k,v in s.items()})
        except Exception as e: print(n,w,'gap',e)
# NJR from filed statements
ni={2016:131.672,2017:132.065,2018:233.436,2019:169.505,2020:193.919,2021:117.890,2022:274.922,2023:264.724,2024:289.775,2025:335.627}
# restated 2019, 2020 (FY2021 10-K): 123.935, 163.007
ni_r=dict(ni); ni_r[2019]=123.935; ni_r[2020]=163.007
eq={2016:1166.591,2017:1236.643,2018:1418.978,2019:1551.717,2020:1643.896,2021:1630.862,2022:1817.210,2023:1990.735,2024:2200.443,2025:2391.666}
ocf={2016:142.630,2017:248.046,2018:398.286,2019:194.128,2020:213.481,2021:390.954,2022:323.480,2023:478.993,2024:427.407,2025:466.349}
cap={2016:354.196,2017:325.649,2018:384.588,2019:525.932,2020:470.168,2021:624.610,2022:598.428,2023:540.919,2024:571.319,2025:706.078}
da={2016:72.748,2017:81.841,2018:85.701,2019:91.730,2020:119.894,2021:111.387,2022:129.249,2023:152.941,2024:166.567,2025:188.774}
for w,yrs in [('2021-25',range(2021,2026)),('2017-25',range(2017,2026))]:
    s=stats(ni_r,eq,ocf,cap,da,yrs); print('NJR',w,{k:(round(v,3) if isinstance(v,float) else v) for k,v in s.items()})
