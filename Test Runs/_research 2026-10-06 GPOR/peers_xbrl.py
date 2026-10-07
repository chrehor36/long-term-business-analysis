# Peer comparison from each company's own XBRL company facts (10-K annual durations, latest-filed value per period).
# Transcription and sums only.
import sys, json, datetime as dt
sys.path.insert(0, r'C:/Users/chreh/OneDrive/Documents/BRK/tools')
import sources
PEERS = {'GPOR':'0000874499','EQT':'0000033213','AR':'0001433270','RRC':'0000315852','CNX':'0001070412','EXE':'0000895126'}
TAGS = {
 'ocf':['NetCashProvidedByUsedInOperatingActivities','NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
 'capex':['PaymentsToAcquireOilAndGasPropertyAndEquipment','PaymentsToAcquireOilAndGasProperty','PaymentsToExploreAndDevelopOilAndGasProperties','PaymentsToAcquireProductiveAssets','PaymentsToAcquirePropertyPlantAndEquipment'],
 'acq':['PaymentsToAcquireBusinessesNetOfCashAcquired'],
 'ni':['NetIncomeLoss','NetIncomeLossAvailableToCommonStockholdersBasic'],
 'impair':['ImpairmentOfOilAndGasProperties','ImpairmentOfLongLivedAssetsHeldForUse','AssetImpairmentCharges'],
 'rev_og':['ResultsOfOperationsRevenueFromOilAndGasProducingActivities'],
 'prodcost':['ResultsOfOperationsProductionOrLiftingCosts'],
 'dda_og':['ResultsOfOperationsDepreciationDepletionAndAmortizationAndValuationProvisions'],
}
def d(s): return dt.date.fromisoformat(s)
def series(g, tags):
    out={}
    for t in tags:
        if t not in g: continue
        for u,v in g[t]['units'].items():
            if u!='USD': continue
            for x in v:
                if x.get('form') not in ('10-K','10-K/A') or 'start' not in x: continue
                days=(d(x['end'])-d(x['start'])).days
                if not (340<=days<=380): continue
                y=x['end'][:4]
                if y in out and out[y][1]>=x['filed'] : continue
                if y in out and out[y][2]!=t: continue  # first tag wins per year
                out[y]=(x['val']/1e6,x['filed'],t)
    return out
res={}
for tk,cik in PEERS.items():
    f=sources.sec_facts(cik); g=f['facts'].get('us-gaap',{})
    res[tk]={k:series(g,v) for k,v in TAGS.items()}
json.dump({tk:{k:{y:v[0] for y,v in s.items()} for k,s in r.items()} for tk,r in res.items()}, open(r'C:/Users/chreh/OneDrive/Documents/BRK/Test Runs/_research 2026-10-06 GPOR/peers_xbrl.json','w'), indent=1)
for tk,r in res.items():
    print('=====',tk)
    yrs=sorted(set(y for s in r.values() for y in s if '2012'<=y<='2025'))
    print('year  '+''.join(f'{k:>10}' for k in TAGS))
    for y in yrs:
        print(y+'  '+''.join(f"{r[k][y][0]:10.0f}" if y in r[k] else f"{'-':>10}" for k in TAGS))
    for k in TAGS:
        tags=sorted(set(v[2] for v in r[k].values()))
        print('   ',k,tags)
