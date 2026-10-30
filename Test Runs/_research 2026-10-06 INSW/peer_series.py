import json
def series(f,cands,instant=False):
    out={}
    for ns,k in cands:
        if ns not in f['facts'] or k not in f['facts'][ns]: continue
        for u,v in f['facts'][ns][k]['units'].items():
            if u!='USD': continue
            for x in v:
                if x.get('form') not in ('10-K','20-F','10-K/A','20-F/A'): continue
                if instant:
                    if 'frame' in x and x['frame'].endswith('Q4I') : out.setdefault(int(x['frame'][2:6]),x['val'])
                    elif x.get('end','').endswith('12-31'):
                        y=int(x['end'][:4]); out.setdefault(y,x['val'])
                else:
                    if 'start' in x and x['start'][5:]=='01-01' and x['end'][5:]=='12-31' and x['start'][:4]==x['end'][:4]:
                        y=int(x['end'][:4]); out.setdefault(y,x['val'])
    return out
ni=[('us-gaap','NetIncomeLoss'),('us-gaap','ProfitLoss'),('ifrs-full','ProfitLossAttributableToOwnersOfParent'),('ifrs-full','ProfitLoss')]
eq=[('us-gaap','StockholdersEquity'),('us-gaap','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'),('ifrs-full','EquityAttributableToOwnersOfParent'),('ifrs-full','Equity')]
ocf=[('us-gaap','NetCashProvidedByUsedInOperatingActivities'),('ifrs-full','CashFlowsFromUsedInOperatingActivities')]
rev=[('us-gaap','Revenues'),('ifrs-full','Revenue')]
res={}
for t in ['INSW','FRO','DHT','STNG','TNK','ASC']:
    f=json.load(open('facts.json' if t=='INSW' else f'peers/{t}_facts.json'))
    N=series(f,ni);E=series(f,eq,True);O=series(f,ocf);R=series(f,rev)
    res[t]=dict(ni=N,eq=E,ocf=O,rev=R)
    print('==',t)
    for y in range(2012,2026):
        print(y, *(f"{d.get(y,float('nan'))/1e6:9.1f}" for d in (R,N,O,E)))
json.dump({t:{k:{str(y):v for y,v in d.items()} for k,d in r.items()} for t,r in res.items()},open('peer_series.json','w'))
