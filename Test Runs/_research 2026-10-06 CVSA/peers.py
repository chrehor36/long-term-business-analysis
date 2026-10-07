import json
from datetime import date
def annual(facts,tags):
    g=facts['facts'].get('us-gaap',{})
    out={}
    for tag in tags:
        if tag not in g: continue
        for x in g[tag]['units'].get('USD',[]):
            if x.get('form')!='10-K': continue
            if 'start' in x:
                if (date.fromisoformat(x['end'])-date.fromisoformat(x['start'])).days<350: continue
            y=x['end'][:4] if x['end'][5:7]>'06' or True else x['end'][:4]
            key=x['end']
            # keep latest-filed value per end date (restated)
            if key not in out or x['filed']>out[key][2]:
                out[key]=(x['val'],x['accn'],x['filed'])
    return out
T={'rev':['Revenues','RevenueFromContractWithCustomerExcludingAssessedTax'],
   'oi':['OperatingIncomeLoss'],
   'ocf':['NetCashProvidedByUsedInOperatingActivities'],
   'capex':['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets'],
   'sbc':['ShareBasedCompensation','AllocatedShareBasedCompensationExpense'],
   'eq':['StockholdersEquity'],'gw':['Goodwill'],'debt':['LongTermDebtNoncurrent','LongTermDebt']}
import sys
for t in ['CVSA','LOPE','STRA','APEI','PRDO']:
    f=json.load(open('facts.json' if t=='CVSA' else f'peers/{t}_facts.json'))
    data={k:annual(f,v) for k,v in T.items()}
    ends=sorted(set(data['rev'])|set(data['oi']))
    print('=====',t,f['entityName'])
    print(' end         rev     oi   oi%    ocf   capex   sbc  owner  own%   accn')
    for e in ends:
        if e<'2015-06-01': continue
        g=lambda k: data[k].get(e,(None,))[0]
        rev,oi,ocf,cx,sbc=g('rev'),g('oi'),g('ocf'),g('capex'),g('sbc')
        own=(ocf-cx-(sbc or 0)) if ocf is not None and cx is not None else None
        fmt=lambda v: f'{v/1e6:7.1f}' if v is not None else '      -'
        print(e,fmt(rev),fmt(oi),f'{100*oi/rev:5.1f}' if rev and oi else '    -',fmt(ocf),fmt(cx),fmt(sbc),fmt(own),f'{100*own/rev:5.1f}' if own and rev else '   -', data['rev'].get(e,('','',''))[1] or data['oi'].get(e,('','',''))[1])
