import json,sys
sys.stdout.reconfigure(encoding='utf-8')
S={int(k):v for k,v in json.load(open('sup_parsed.json')).items()}
SBC={2007:146,2008:194,2009:132,2010:226,2011:193,2012:245,2013:231,2014:254,2015:283,2016:218,2017:206,2018:197,2019:205,2020:202,2021:200,2022:193,2023:208,2024:223,2025:242}
AM={2007:52,2008:61,2009:61,2010:76,2011:233,2012:387,2013:371,2014:365,2015:337,2016:326,2017:323,2018:331,2019:324,2020:311,2021:302,2022:284,2023:218,2024:176,2025:169}
STK={2009:718,2010:94}   # pension/benefit contributions paid in treasury shares, outside operating cash
SALES={2007:41962,2008:48044,2009:29540,2010:39867,2011:57392,2012:63068,2013:52694,2014:52142,2015:44147,2016:35773,2017:42676,2018:51822,2019:50755,2020:39022,2021:48188,2022:56574,2023:63869,2024:61363,2025:63980}
CADV={2016:-37,2017:-69,2018:-183,2019:-8,2020:-126,2021:33,2022:769,2023:78,2024:369,2025:1933}
def get(y,k,col):
    if y+1 in S and k in S[y+1]: return S[y+1][k][col*2+1]
    return S[y][k][col*2]
cap_m=821.58*459674889/1e6
rows={}
print('year | MP&E OCF | SBC | stock to benefit plans | MP&E capex incl. own leased | MP&E D&A | acquired amortization | OE capex end | OE depreciation end | capex/dep | OE (capex end) / MP&E sales | customer advances in OCF')
for y in range(2007,2026):
    ocf=get(y,'ocf',1); cx=-get(y,'capex',1)-get(y,'lease',1); da=get(y,'da',1); am=AM[y]; dep=da-am
    lo=ocf-SBC[y]-STK.get(y,0)-cx; hi=ocf-SBC[y]-STK.get(y,0)-dep
    rows[y]=(lo,hi)
    print(y,'|',int(ocf),'|',SBC[y],'|',STK.get(y,0),'|',int(cx),'|',int(da),'|',am,'|',round(lo),'|',round(hi),'|',round(cx/dep,2),'|',f'{lo/SALES[y]*100:.1f}%','|',CADV.get(y,''))
ocf=12278+7011-3862; sbc=242+146-131; cx=(2758+36)+(1302+11)-(1273+14); da=1497+812-716; am=169+87-87
tlo=ocf-sbc-cx; thi=ocf-sbc-(da-am)
print(f'TTM to 2026-06-30: OCF {ocf} SBC {sbc} capex {cx} D&A {da} amort {am} -> ${tlo:,.0f}M to ${thi:,.0f}M = {tlo/cap_m*100:.2f}% to {thi/cap_m*100:.2f}%')
print('cap', round(cap_m,1))
print('windows ending 2025 (capex end to depreciation end):')
for n in [1,2,3,4,5,7,10,15,19]:
    ys=range(2026-n,2026)
    lo=sum(rows[y][0] for y in ys)/n; hi=sum(rows[y][1] for y in ys)/n
    print(f'  {n}y {min(ys)}-{max(ys)}: ${lo:,.0f}M to ${hi:,.0f}M  = {lo/cap_m*100:.2f}% to {hi/cap_m*100:.2f}%')
allv=[v for y in rows for v in rows[y]]
m=[rows[y][0]/SALES[y] for y in rows]; print('mean OE margin (capex end) 2007-2025',round(sum(m)/len(m)*100,2),'% ; median', round(sorted(m)[len(m)//2]*100,2))
m2=[rows[y][1]/SALES[y] for y in rows]; print('mean OE margin (dep end) 2007-2025',round(sum(m2)/len(m2)*100,2))
# consolidated cross-check 5y
c=0
for y in range(2021,2026):
    c+=get(y,'ocf',0)-SBC[y]-(-get(y,'capex',0))-(-get(y,'lease',0))+get(y,'disp',0)
print('consolidated 5y (OCF - SBC - capex - leased-equipment capex + disposal proceeds):',round(c/5))
# 2023-2025 stripped of customer advances
s3=sum(rows[y][0]-CADV[y] for y in (2023,2024,2025))/3; print('3y capex end ex customer advances', round(s3))
s5=sum(rows[y][0]-CADV[y] for y in range(2021,2026))/5; print('5y capex end ex customer advances', round(s5))
