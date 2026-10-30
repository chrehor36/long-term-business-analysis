import json
names={'0001031296':'FirstEnergy','0000004904':'AEP','0000072741':'Eversource','0000922224':'PPL'}
def series(d,t,inst):
    got={}
    if t not in d: return got
    for u,vals in d[t]['units'].items():
        for v in vals:
            if v.get('form')!='10-K' or 'frame' not in v: continue
            f=v['frame']
            if inst and f.endswith('Q4I'): got[f[2:6]]=round(v['val']/1e6)
            if not inst and len(f)==6: got[f[2:]]=round(v['val']/1e6)
    return {y:got[y] for y in sorted(got) if y>='2020'}
for c,n in names.items():
    d=json.load(open(f'cache/facts_{c}.json'))['facts']['us-gaap']
    print('==',n)
    for t in ['StockholdersEquity','StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest','CommonStockholdersEquity']:
        s=series(d,t,True)
        if s: print(t,s)
    for t in ['PaymentsToAcquirePropertyPlantAndEquipment','PaymentsToAcquireProductiveAssets','PaymentsForConstructionInProcess','DepreciationDepletionAndAmortization','DepreciationAndAmortization','Depreciation','InterestPaidNet','ShareBasedCompensation','ProceedsFromIssuanceOfCommonStock']:
        s=series(d,t,False)
        if s: print(t,s)
