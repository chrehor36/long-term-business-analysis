"""Field returns from XBRL companyfacts (transcription; cross-check in filings). python -I peers.py"""
import json, os, subprocess, sys
here=os.path.dirname(os.path.abspath(__file__))
P={'AEP':'0000004904','DUK':'0001326160','D':'0000715957','FE':'0001031296'}
def ser(d,keys):
    out={}
    for k in keys:
        v=d['facts']['us-gaap'].get(k)
        if not v: continue
        for u in v['units'].get('USD',[]):
            if u.get('form')=='10-K' and 'start' in u and u['start'][5:]=='01-01' and u['end'][5:]=='12-31' and u['start'][:4]==u['end'][:4]:
                out.setdefault(u['end'][:4],u['val'])
    return out
def inst(d,keys):
    out={}
    for k in keys:
        v=d['facts']['us-gaap'].get(k)
        if not v: continue
        for u in v['units'].get('USD',[]):
            if u.get('form')=='10-K' and u['end'][5:]=='12-31' and 'start' not in u:
                out.setdefault(u['end'][:4],u['val'])
    return out
for t,c in P.items():
    f=os.path.join(here,'cache',f'facts_{t}.json')
    if not os.path.exists(f):
        subprocess.run([sys.executable,'-I',os.path.join(here,'fetch.py'),f'https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json',f'facts_{t}.json'],check=True)
    d=json.load(open(f))
    ni=ser(d,['NetIncomeLossAvailableToCommonStockholdersBasic','NetIncomeLoss'])
    eq=inst(d,['StockholdersEquity'])
    ocf=ser(d,['NetCashProvidedByUsedInOperatingActivities'])
    cx=ser(d,['PaymentsForConstructionInProcess','PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'])
    da=ser(d,['DepreciationDepletionAndAmortization','DepreciationAndAmortization','UtilitiesOperatingExpenseDepreciationAndAmortization'])
    print(f'== {t} {d["entityName"]}')
    print(' year  NI  equity(end)  ROE(avg eq)  OCF  capex  OCF-capex  OCF-D&A')
    for y in range(2016,2026):
        y=str(y); yp=str(int(y)-1)
        if y in ni and y in eq and yp in eq:
            roe=ni[y]/((eq[y]+eq[yp])/2)
            print(f' {y} {ni[y]/1e6:7.0f} {eq[y]/1e6:8.0f} {roe*100:6.1f}%  {ocf.get(y,0)/1e6:7.0f} {cx.get(y,0)/1e6:7.0f} {(ocf.get(y,0)-cx.get(y,0))/1e6:7.0f} {(ocf.get(y,0)-da.get(y,0))/1e6:7.0f}')
